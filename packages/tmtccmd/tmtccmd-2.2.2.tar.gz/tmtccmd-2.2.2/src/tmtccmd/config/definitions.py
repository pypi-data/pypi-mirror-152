"""Definitions for the TMTC commander core
"""
import enum
from typing import Tuple, Dict, Optional, List, Union, Callable, Any

from spacepackets.ecss import PusTelecommand

from tmtccmd.com_if.com_interface_base import CommunicationInterface


def default_json_path() -> str:
    return "tmtc_conf.json"


class CoreGlobalIds(enum.IntEnum):
    """
    Numbers from 128 to 200 are reserved for core globals
    """

    # Object handles
    TMTC_HOOK = 128
    COM_INTERFACE_HANDLE = 129
    TM_LISTENER_HANDLE = 130
    TMTC_PRINTER_HANDLE = 131
    TM_HANDLER_HANDLE = 132
    PRETTY_PRINTER = 133

    # Parameters
    JSON_CFG_PATH = 139
    MODE = 141
    CURRENT_SERVICE = 142
    COM_IF = 144
    OP_CODE = 145
    TM_TIMEOUT = 146
    SERVICE_OP_CODE_DICT = 147
    COM_IF_DICT = 148

    # Miscellaneous
    DISPLAY_MODE = 150
    USE_LISTENER_AFTER_OP = 151
    PRINT_HK = 152
    PRINT_TM = 153
    PRINT_RAW_TM = 154
    PRINT_TO_FILE = 155
    RESEND_TC = 156
    TC_SEND_TIMEOUT_FACTOR = 157

    # Config dictionaries
    USE_SERIAL = 160
    SERIAL_CONFIG = 161
    USE_ETHERNET = 162
    ETHERNET_CONFIG = 163
    END = 300


class OpCodeDictKeys(enum.IntEnum):
    TIMEOUT = CoreGlobalIds.TM_TIMEOUT
    ENTER_LISTENER_MODE = CoreGlobalIds.USE_LISTENER_AFTER_OP


# Service Op Code Dictionary Types
ServiceNameT = str
ServiceInfoT = str
OpCodeNameT = Union[str, List[str]]
OpCodeInfoT = str
# Operation code options are optional. If none are supplied, default values are assumed
OpCodeOptionsT = Optional[Dict[OpCodeDictKeys, any]]
OpCodeEntryT = Dict[OpCodeNameT, Tuple[OpCodeInfoT, OpCodeOptionsT]]
# It is possible to specify a service without any op codes
ServiceDictValueT = Optional[Tuple[ServiceInfoT, OpCodeEntryT]]
ServiceOpCodeDictT = Dict[ServiceNameT, ServiceDictValueT]

# Com Interface Types
ComIFValueT = Tuple[str, any]
ComIFDictT = Dict[str, ComIFValueT]

EthernetAddressT = Tuple[str, int]


class QueueCommands(enum.Enum):
    PRINT = "print"
    RAW_PRINT = "raw_print"
    WAIT = "wait"
    SET_TIMEOUT = "set_timeout"


TcQueueEntryArg = Any
UserArg = Any
"""Third Argument: Second argument in TC queue tuple. Fouth Argument
"""
UsrSendCbT = Callable[
    [Union[bytes, QueueCommands], CommunicationInterface, TcQueueEntryArg, UserArg],
    None,
]


class DataReplyUnpacked:
    def __init__(self):
        # Name of the data fields inside a data set
        self.header_list = []
        # Corresponding list of content
        self.content_list = []


class HkReplyUnpacked(DataReplyUnpacked):
    def __init__(self):
        super().__init__()
        # Validity buffer
        self.validity_buffer = bytearray()
        # Number of variables contained in HK set
        self._num_of_vars = None

    @property
    def num_of_vars(self):
        """Unless set to a specific number, will return the length of the content list
        :return:
        """
        if self._num_of_vars is None:
            return len(self.header_list)
        return self._num_of_vars

    @num_of_vars.setter
    def num_of_vars(self, num_of_vars: int):
        self._num_of_vars = num_of_vars


class CoreComInterfaces(enum.Enum):
    DUMMY = "dummy"
    SERIAL_DLE = "ser_dle"
    TCPIP_UDP = "udp"
    TCPIP_TCP = "tcp"
    SERIAL_FIXED_FRAME = "ser_fixed"
    SERIAL_QEMU = "ser_qemu"
    UNSPECIFIED = "unspec"


CoreComInterfacesDict = {
    CoreComInterfaces.DUMMY.value: "Dummy Interface",
    CoreComInterfaces.SERIAL_DLE.value: "Serial Interace with DLE encoding",
    CoreComInterfaces.TCPIP_UDP.value: "TCP/IP with UDP datagrams",
    CoreComInterfaces.TCPIP_TCP.value: "TCP/IP with TCP",
    CoreComInterfaces.SERIAL_FIXED_FRAME.value: "Serial Interface with fixed size frames",
    CoreComInterfaces.SERIAL_QEMU.value: "Serial Interface using QEMU",
    CoreComInterfaces.UNSPECIFIED.value: "Unspecified",
}


# Mode options, set by args parser
class CoreModeList(enum.IntEnum):
    SEQUENTIAL_CMD_MODE = 0
    LISTENER_MODE = 1
    GUI_MODE = 2
    IDLE = 5
    PROMPT_MODE = 6
    CONTINUOUS_MODE = (
        7  # will start a daemon handling tm and return after sending one tc
    )


CoreModeStrings = {
    CoreModeList.SEQUENTIAL_CMD_MODE: "seqcmd",
    CoreModeList.LISTENER_MODE: "listener",
    CoreModeList.GUI_MODE: "gui",
}


class CoreServiceList(enum.Enum):
    SERVICE_2 = "2"
    SERVICE_3 = "3"
    SERVICE_5 = "5"
    SERVICE_8 = "8"
    SERVICE_9 = "9"
    SERVICE_11 = "11"
    SERVICE_17 = "17"
    SERVICE_20 = "20"
    SERVICE_23 = "23"
    SERVICE_200 = "200"


DEFAULT_APID = 0xEF
DEBUG_MODE = False
