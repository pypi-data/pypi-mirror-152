"""
@file       tmtcc_tm_listener.py
@date       01.11.2019
@brief      Separate class to listen to telecommands.
@author     R. Mueller
"""
import sys
import time
import threading
from collections import deque
from typing import Dict, List, Tuple, Optional
from enum import Enum

from spacepackets.ccsds.spacepacket import get_apid_from_raw_space_packet

from tmtccmd.tm.definitions import TelemetryQueueT, TelemetryListT, TmTypes
from tmtccmd.logging import get_console_logger
from tmtccmd.com_if.com_interface_base import CommunicationInterface
from tmtccmd.utility.conf_util import acquire_timeout

LOGGER = get_console_logger()

INVALID_APID = -2
UNKNOWN_TARGET_ID = -1
QueueDictT = Dict[int, Tuple[TelemetryQueueT, int]]
QueueListT = List[Tuple[int, TelemetryQueueT]]


class ListenerModes(Enum):
    MANUAL = 1
    LISTENER = 2
    SEQUENCE = 3


class TmListener:
    """Performs all TM listening operations.
    This listener to have a permanent means to receive data. A background thread is used
    to poll data with the provided communication interface. Dedicated sender and receiver object
    or any other software component can get the received packets from the internal deque container.
    """

    DEFAULT_MODE_OPERATION_TIMEOUT = 300.0
    DEFAULT_UNKNOWN_QUEUE_MAX_LEN = 50
    QUEUE_DICT_QUEUE_IDX = 0
    QUEUE_DICT_MAX_LEN_IDX = 1
    DEFAULT_TM_TIMEOUT = 5.0

    DEFAULT_LOCK_TIMEOUT = 0.5

    def __init__(
        self,
        com_if: CommunicationInterface,
        seq_timeout: float = DEFAULT_TM_TIMEOUT,
        tm_type: TmTypes = TmTypes.CCSDS_SPACE_PACKETS,
    ):
        """Initiate a TM listener.
        :param com_if: Type of communication interface,
            e.g. a serial or ethernet interface
        :param tm_type: Telemetry type. Default to CCSDS space packets for now
        """
        self.__com_if = com_if
        self._mode_op_timeout = TmListener.DEFAULT_MODE_OPERATION_TIMEOUT
        # TM Listener operations can be suspended by setting this flag
        self.event_listener_active = threading.Event()
        self.listener_active = False
        self.current_apid = INVALID_APID

        # Listener is daemon and will exit automatically if all other threads are closed
        self.listener_thread = threading.Thread(
            target=self.__perform_operation, daemon=True
        )
        self.lock_listener = threading.Lock()
        # This Event is set by sender objects to perform mode operations
        self.event_mode_change = threading.Event()
        # This Event is set and cleared by the listener to inform the sender objects
        # if a reply has been received
        self.__event_reply_received = threading.Event()
        # This Event is set by sender objects if all necessary operations are done
        # to transition back to listener mode
        self.__event_mode_op_finished = threading.Event()

        self.__listener_mode = ListenerModes.LISTENER
        self.seq_timeout = seq_timeout
        self.__tm_type = tm_type
        self.__queue_dict: QueueDictT = dict(
            {UNKNOWN_TARGET_ID: (deque(), self.DEFAULT_UNKNOWN_QUEUE_MAX_LEN)}
        )

    def start(self):
        if not self.event_listener_active.is_set():
            self.event_listener_active.set()
            if not self.listener_thread.is_alive():
                self.listener_thread.start()
        else:
            LOGGER.warning("TM listener is already active!")

    def stop(self):
        self.event_listener_active.clear()

    def set_mode_op_timeout(self, timeout: float):
        self._mode_op_timeout = timeout

    def subscribe_ccsds_tm_handler(self, apid: int, queue_max_len: int):
        if self.__tm_type == TmTypes.CCSDS_SPACE_PACKETS:
            self.__queue_dict[apid] = (deque(), queue_max_len)
        else:
            LOGGER.warning("This function only support CCSDS space packet handling")

    def set_current_apid(self, new_apid: int):
        self.current_apid = new_apid

    def set_com_if(self, com_if: CommunicationInterface):
        self.__com_if = com_if

    def is_listener_active(self) -> bool:
        return self.listener_active

    def manual_mode(self) -> bool:
        return self.__update_mode(ListenerModes.MANUAL)

    def listener_mode(self) -> bool:
        return self.__update_mode(ListenerModes.LISTENER)

    def sequence_mode(self, seq_timeout: Optional[float] = None) -> bool:
        if seq_timeout is not None:
            self.seq_timeout = seq_timeout
        return self.__update_mode(ListenerModes.SEQUENCE)

    def __update_mode(self, new_mode: ListenerModes) -> bool:
        if self.__listener_mode != new_mode:
            self.event_mode_change.set()
            self.__listener_mode = new_mode
            return True
        return False

    def reply_event(self):
        if self.__event_reply_received.is_set():
            return True
        else:
            return False

    def clear_reply_event(self):
        self.__event_reply_received.clear()

    def set_mode_op_finished(self):
        if not self.__event_mode_op_finished.is_set():
            self.__event_mode_op_finished.set()

    def ccsds_tm_received(self, apid: int = INVALID_APID):
        """This function is used to check whether any data has been received"""
        queue_dict_list = self.__queue_dict.get(apid)
        if queue_dict_list is None:
            LOGGER.warning(f"No queue available for APID {apid}")
        queue_dict = queue_dict_list[self.QUEUE_DICT_QUEUE_IDX]
        if queue_dict.__len__() > 0:
            return True
        else:
            return False

    def tm_packets_available(self):
        with acquire_timeout(
            self.lock_listener, timeout=self.DEFAULT_LOCK_TIMEOUT
        ) as acquired:
            if acquired:
                for queue_lists in self.__queue_dict.values():
                    if queue_lists[self.QUEUE_DICT_QUEUE_IDX]:
                        return True
        return False

    def retrieve_tm_packet_queues(self, clear: bool) -> QueueListT:
        queues = []
        with acquire_timeout(
            self.lock_listener, timeout=self.DEFAULT_LOCK_TIMEOUT
        ) as acquired:
            if not acquired:
                LOGGER.error("Could not acquire lock!")
            # Still continue
            for key, queue_list in self.__queue_dict.items():
                queues.append((key, queue_list[self.QUEUE_DICT_QUEUE_IDX].copy()))
            if clear:
                self.clear_tm_packet_queues(lock=False)
        return queues

    def retrieve_ccsds_tm_packet_queue(
        self, apid: int = -1, clear: bool = False
    ) -> TelemetryQueueT:
        """Retrieve the packet queue for a given APID. The TM listener will handle routing
        packets into the correct queue."""
        if apid == -1:
            apid = self.current_apid
        target_queue_list = self.__queue_dict.get(apid)
        if target_queue_list is None:
            LOGGER.warning(f"No queue available for APID {apid}")
            return deque()
        target_queue = target_queue_list[self.QUEUE_DICT_QUEUE_IDX]
        # We make sure that the queue is not manipulated while it is being copied.
        with acquire_timeout(
            self.lock_listener, timeout=self.DEFAULT_LOCK_TIMEOUT
        ) as acquired:
            if not acquired:
                LOGGER.warning(
                    f"TmListener: Blocked on lock acquisition for longer than"
                    f"{self.DEFAULT_LOCK_TIMEOUT} second!"
                )
            tm_queue_copy = target_queue.copy()
            if clear:
                target_queue.clear()
        return tm_queue_copy

    def clear_ccsds_tm_packet_queue(self, apid: int):
        if apid == -1:
            apid = self.current_apid
        target_queue = self.__queue_dict.get(apid)
        if target_queue is None:
            LOGGER.warning(f"No queue available for APID {apid}")
            return
        with acquire_timeout(
            self.lock_listener, timeout=self.DEFAULT_LOCK_TIMEOUT
        ) as acquired:
            if not acquired:
                LOGGER.warning(
                    f"TmListener: Blocked on lock acquisition for longer than"
                    f"{self.DEFAULT_LOCK_TIMEOUT} second!"
                )
            target_queue[0].clear()

    def clear_tm_packet_queues(self, lock: bool):
        locked = False
        if lock:
            locked = self.lock_listener.acquire(timeout=self.DEFAULT_LOCK_TIMEOUT)
        for queue_list in self.__queue_dict.values():
            queue_list[self.QUEUE_DICT_QUEUE_IDX].clear()
        if locked:
            self.lock_listener.release()

    def retrieve_unknown_target_queue(self):
        target_queue = self.__queue_dict.get(UNKNOWN_TARGET_ID)[
            self.QUEUE_DICT_QUEUE_IDX
        ]
        with acquire_timeout(
            self.lock_listener, timeout=self.DEFAULT_LOCK_TIMEOUT
        ) as acquired:
            if acquired:
                return target_queue.copy()

    def check_for_one_telemetry_sequence(self, seq_timeout: float) -> bool:
        """Receive all telemetry for a specified time period.
        :return: True if a sequence was received
        """
        data_available = self.__com_if.data_available(timeout=0, parameters=None)
        if data_available == 0:
            return False
        elif data_available > 0:
            self.__read_telemetry_sequence(tm_timeout=seq_timeout)
            return True
        else:
            LOGGER.error("TmListener: Configuration error in communication interface!")
            sys.exit()

    def __perform_operation(self):
        while True:
            # This is running in a daemon thread so it will stop automatically if all other
            # threads have closed
            if self.event_listener_active.is_set():
                self.listener_active = True
                self.__default_operation()
            else:
                self.listener_active = False
                # Check every 300 ms whether connection is up again.
                time.sleep(0.3)

    def __default_operation(self):
        """Core function. Normally, polls all packets"""
        self.__perform_core_operation()
        if self.event_mode_change.is_set():
            self.event_mode_change.clear()
            start_time = time.time()
            while not self.__event_mode_op_finished.is_set():
                elapsed_time = time.time() - start_time
                if elapsed_time < self._mode_op_timeout:
                    self.__perform_mode_operation()
                else:
                    LOGGER.warning("TmListener: Mode operation timeout occured!")
                    break
            self.__event_mode_op_finished.clear()
            LOGGER.info("TmListener: Transitioning to listener mode.")
            self.__listener_mode = ListenerModes.LISTENER

    def __perform_core_operation(self):
        """The core operation listens for packets."""
        packet_list = self.__com_if.receive()
        if len(packet_list) > 0:
            with acquire_timeout(
                self.lock_listener, timeout=self.DEFAULT_LOCK_TIMEOUT
            ) as acquired:
                if not acquired:
                    LOGGER.warning(
                        f"TmListener: Blocked on lock acquisition for longer than"
                        f"{self.DEFAULT_LOCK_TIMEOUT} second!"
                    )
                self.__route_packets(packet_list)
            if not self.__event_reply_received.is_set():
                self.__event_reply_received.set()
        else:
            time.sleep(0.4)

    def __perform_mode_operation(self):
        """The TmListener is instructed performs certain operations based on the current
        listener mode.
        :return:
        """
        # Listener Mode
        if self.__listener_mode == ListenerModes.LISTENER:
            if not self.__event_mode_op_finished.is_set():
                self.__event_mode_op_finished.set()
        # Single Command Mode
        elif self.__listener_mode == ListenerModes.SEQUENCE:
            # This prevents the listener from listening from one more unnecessary cycle
            if self.__event_mode_op_finished.is_set():
                return
            # Listen for one reply sequence.
            if self.check_for_one_telemetry_sequence(self.seq_timeout):
                # Set reply event, will be cleared by checkForFirstReply()
                if not self.__event_reply_received.is_set():
                    self.__event_reply_received.set()
            time.sleep(0.2)
        elif self.__listener_mode == ListenerModes.MANUAL:
            self.__perform_core_operation()

    def __read_telemetry_sequence(self, tm_timeout: float):
        """Thread-safe implementation for reading a telemetry sequence."""
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < tm_timeout:
            # Fast responsiveness in sequential mode
            if self.__event_mode_op_finished.is_set():
                if self.__listener_mode == ListenerModes.SEQUENCE:
                    return
            packets_available = self.__com_if.data_available(
                timeout=0.2, parameters=None
            )
            if packets_available > 0:
                packet_list = self.__com_if.receive()
                with acquire_timeout(
                    self.lock_listener, timeout=self.DEFAULT_LOCK_TIMEOUT
                ) as acquired:
                    if not acquired:
                        LOGGER.warning(
                            f"TmListener: Blocked on lock acquisition for longer than"
                            f"{self.DEFAULT_LOCK_TIMEOUT} second!"
                        )
                    self.__route_packets(packet_list)
            elapsed_time = time.time() - start_time
            if packets_available == 0:
                time.sleep(0.1)

    def __route_packets(self, tm_packet_list: TelemetryListT):
        """Route given packets. For CCSDS packets, use APID to do this"""
        for tm_packet in tm_packet_list:
            if self.__tm_type == TmTypes.CCSDS_SPACE_PACKETS:
                packet_handled = self.__handle_ccsds_space_packet(tm_packet=tm_packet)
                if packet_handled:
                    continue
            # No queue was found
            LOGGER.warning("No target queue found, inserting into unknown target queue")
            unknown_target_list = self.__queue_dict[UNKNOWN_TARGET_ID]
            unknown_target_queue = unknown_target_list[self.QUEUE_DICT_QUEUE_IDX]
            if (
                unknown_target_queue.__len__()
                > unknown_target_list[self.QUEUE_DICT_MAX_LEN_IDX]
            ):
                LOGGER.warning("Unknown target queue full. Removing oldest packet..")
                unknown_target_queue.pop()
            unknown_target_queue.appendleft(tm_packet)

    def __handle_ccsds_space_packet(self, tm_packet: bytes) -> bool:
        if len(tm_packet) < 6:
            LOGGER.warning("TM packet to small to be a CCSDS space packet")
        else:
            apid = get_apid_from_raw_space_packet(raw_packet=tm_packet)
            target_queue_list = self.__queue_dict.get(apid)
            if target_queue_list is None:
                LOGGER.warning(f"No TM handler assigned for APID {apid}")
            else:
                target_queue = target_queue_list[self.QUEUE_DICT_QUEUE_IDX]
                if (
                    target_queue.__len__()
                    > target_queue_list[self.QUEUE_DICT_MAX_LEN_IDX]
                ):
                    LOGGER.warning(
                        f"Target queue for APID {apid} full. Removing oldest packet.."
                    )
                    target_queue.pop()
                target_queue.appendleft(tm_packet)
                return True
        return False
