import enum
from typing import Deque, Tuple, List, Union
from spacepackets.ecss.tm import PusTelemetry
from tmtccmd.tm.base import PusTmInfoInterface, PusTmInterface

TelemetryListT = List[bytes]
TelemetryQueueT = Deque[bytes]

PusTmQueue = Deque[PusTelemetry]
PusTmTupleT = Tuple[bytes, PusTelemetry]

PusTmListT = List[PusTelemetry]
PusTmQueueT = Deque[PusTmListT]
PusIFListT = List[Union[PusTmInfoInterface, PusTmInterface]]
PusIFQueueT = Deque[PusIFListT]

PusTmListT = List[PusTelemetry]
PusTmObjQeue = Deque[PusTelemetry]
PusTmTupleQueueT = Deque[PusTmTupleT]


class TmTypes(enum.Enum):
    NONE = enum.auto
    CCSDS_SPACE_PACKETS = enum.auto
