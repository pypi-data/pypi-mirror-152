"""
:file:      tcpip_tcp_com_if.py
:date:      13.05.2021
:brief:     TCP communication interface
:author:    R. Mueller
"""
import socket
import time
import enum
import threading
import select
from collections import deque
from typing import Union, Optional, Tuple

from spacepackets.ccsds.spacepacket import parse_space_packets

from tmtccmd.logging import get_console_logger
from tmtccmd.config.definitions import CoreModeList
from tmtccmd.com_if.com_interface_base import CommunicationInterface
from tmtccmd.tm.definitions import TelemetryListT
from tmtccmd.utility.tmtc_printer import FsfwTmTcPrinter
from tmtccmd.config.definitions import EthernetAddressT
from tmtccmd.utility.conf_util import acquire_timeout

LOGGER = get_console_logger()

TCP_RECV_WIRETAPPING_ENABLED = False
TCP_SEND_WIRETAPPING_ENABLED = False


class TcpCommunicationType(enum.Enum):
    """Parse for space packets in the TCP stream, using the space packet header"""

    SPACE_PACKETS = 0


class TcpIpTcpComIF(CommunicationInterface):
    """Communication interface for TCP communication."""

    DEFAULT_LOCK_TIMEOUT = 0.4
    TM_LOOP_DELAY = 0.2

    def __init__(
        self,
        com_if_key: str,
        com_type: TcpCommunicationType,
        space_packet_ids: Tuple[int],
        tm_polling_freqency: float,
        target_address: EthernetAddressT,
        max_recv_size: int,
        max_packets_stored: int = 50,
        init_mode: int = CoreModeList.LISTENER_MODE,
    ):
        """Initialize a communication interface to send and receive TMTC via TCP
        :param com_if_key:
        :param com_type:                Communication Type. By default, it is assumed that
                                        space packets are sent via TCP
        :param space_packet_ids:        16 bit packet header for space packet headers. Used to
                                        detect the start of PUS packets
        :param tm_polling_freqency:     Polling frequency in seconds
        """
        super().__init__(com_if_key=com_if_key)
        self.com_type = com_type
        self.space_packet_ids = space_packet_ids
        self.tm_polling_frequency = tm_polling_freqency
        self.target_address = target_address
        self.max_recv_size = max_recv_size
        self.max_packets_stored = max_packets_stored
        self.init_mode = init_mode

        self.__tcp_socket: Optional[socket.socket] = None
        self.__last_connection_time = 0
        self.__tm_thread_kill_signal = threading.Event()
        # Separate thread to request TM packets periodically if no TCs are being sent
        self.__tcp_conn_thread: Optional[threading.Thread] = threading.Thread(
            target=self.__tcp_tm_client, daemon=True
        )
        self.__tm_queue = deque()
        self.__analysis_queue = deque()
        # Only allow one connection to OBSW at a time for now by using this lock
        # self.__socket_lock = threading.Lock()
        self.__queue_lock = threading.Lock()

    def __del__(self):
        try:
            self.close()
        except IOError:
            LOGGER.warning("Could not close TCP communication interface!")

    def initialize(self, args: any = None) -> any:
        pass

    def open(self, args: any = None):
        self.__tm_thread_kill_signal.clear()
        self.set_up_socket()
        self.set_up_tcp_thread()
        self.__tcp_conn_thread.start()

    def set_up_socket(self):
        if self.__tcp_socket is None:
            self.__tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__tcp_socket.connect(self.target_address)

    def set_up_tcp_thread(self):
        if self.__tcp_conn_thread is None:
            self.__tcp_conn_thread = threading.Thread(
                target=self.__tcp_tm_client, daemon=True
            )

    def close(self, args: any = None) -> None:
        self.__tm_thread_kill_signal.set()
        if self.__tcp_conn_thread != None:
            if self.__tcp_conn_thread.is_alive():
                self.__tcp_conn_thread.join(self.tm_polling_frequency)
            try:
                self.__tcp_socket.shutdown(socket.SHUT_RDWR)
            except OSError:
                LOGGER.warning(
                    "TCP socket endpoint was already closed or not connected"
                )
            self.__tcp_socket.close()
        self.__tcp_socket = None
        self.__tcp_conn_thread = None

    def send(self, data: bytearray):
        try:
            self.__tcp_socket.sendto(data, self.target_address)
        except ConnectionRefusedError:
            LOGGER.warning("TCP connection attempt failed..")

    def receive(self, poll_timeout: float = 0) -> TelemetryListT:
        tm_packet_list = []
        with acquire_timeout(
            self.__queue_lock, timeout=self.DEFAULT_LOCK_TIMEOUT
        ) as acquired:
            if not acquired:
                LOGGER.warning("Acquiring queue lock failed!")
            while self.__tm_queue:
                self.__analysis_queue.appendleft(self.__tm_queue.pop())
        # TCP is stream based, so there might be broken packets or multiple packets in one recv
        # call. We parse the space packets contained in the stream here
        if self.com_type == TcpCommunicationType.SPACE_PACKETS:
            tm_packet_list = parse_space_packets(
                analysis_queue=self.__analysis_queue, packet_ids=self.space_packet_ids
            )
        else:
            while self.__analysis_queue:
                tm_packet_list.append(self.__analysis_queue.pop())
        return tm_packet_list

    def __tcp_tm_client(self):
        while True and not self.__tm_thread_kill_signal.is_set():
            try:
                self.__receive_tm_packets()
            except ConnectionRefusedError:
                LOGGER.warning("TCP connection attempt failed..")
            time.sleep(self.TM_LOOP_DELAY)

    def __receive_tm_packets(self):
        try:
            ready = select.select([self.__tcp_socket], [], [], 0)
            if ready[0]:
                bytes_recvd = self.__tcp_socket.recv(self.max_recv_size)
                with acquire_timeout(
                    self.__queue_lock, timeout=self.DEFAULT_LOCK_TIMEOUT
                ) as acquired:
                    if not acquired:
                        LOGGER.warning("Acquiring queue lock failed!")
                    if self.__tm_queue.__len__() >= self.max_packets_stored:
                        LOGGER.warning(
                            "Number of packets in TCP queue too large. "
                            "Overwriting old packets.."
                        )
                        self.__tm_queue.pop()
                    self.__tm_queue.appendleft(bytes(bytes_recvd))
        except ConnectionResetError:
            LOGGER.exception("ConnectionResetError. TCP server might not be up")

    def data_available(self, timeout: float = 0, parameters: any = 0) -> bool:
        if self.__tm_queue:
            return True
        else:
            return False
