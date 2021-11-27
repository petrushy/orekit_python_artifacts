import java.io
import java.lang
import java.util
import java.util.regex
import org.orekit.gnss
import org.orekit.gnss.metric.messages
import org.orekit.utils.units
import typing



class DataField:
    def booleanValue(self, encodedMessage: 'EncodedMessage') -> bool: ...
    def doubleValue(self, encodedMessage: 'EncodedMessage') -> float: ...
    def intValue(self, encodedMessage: 'EncodedMessage') -> int: ...
    def stringValue(self, encodedMessage: 'EncodedMessage', int: int) -> str: ...

class EncodedMessage:
    def extractBits(self, int: int) -> int: ...
    def start(self) -> None: ...

class MessageType:
    def parse(self, encodedMessage: EncodedMessage, int: int) -> org.orekit.gnss.metric.messages.ParsedMessage: ...

class MessagesParser:
    def __init__(self, list: java.util.List[int]): ...
    def parse(self, encodedMessage: EncodedMessage, boolean: bool) -> org.orekit.gnss.metric.messages.ParsedMessage: ...

class Units:
    SEMI_CIRCLE: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    NS: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    MM: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    MM_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    MM_PER_S2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    KM_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    KM_PER_S2: typing.ClassVar[org.orekit.utils.units.Unit] = ...

class AbstractEncodedMessages(EncodedMessage):
    def __init__(self): ...
    def extractBits(self, int: int) -> int: ...
    def start(self) -> None: ...

class IgsSsrDataField(java.lang.Enum['IgsSsrDataField'], DataField):
    IDF001: typing.ClassVar['IgsSsrDataField'] = ...
    IDF002: typing.ClassVar['IgsSsrDataField'] = ...
    IDF003: typing.ClassVar['IgsSsrDataField'] = ...
    IDF004: typing.ClassVar['IgsSsrDataField'] = ...
    IDF005: typing.ClassVar['IgsSsrDataField'] = ...
    IDF006: typing.ClassVar['IgsSsrDataField'] = ...
    IDF007: typing.ClassVar['IgsSsrDataField'] = ...
    IDF008: typing.ClassVar['IgsSsrDataField'] = ...
    IDF009: typing.ClassVar['IgsSsrDataField'] = ...
    IDF010: typing.ClassVar['IgsSsrDataField'] = ...
    IDF011: typing.ClassVar['IgsSsrDataField'] = ...
    IDF012: typing.ClassVar['IgsSsrDataField'] = ...
    IDF013: typing.ClassVar['IgsSsrDataField'] = ...
    IDF014: typing.ClassVar['IgsSsrDataField'] = ...
    IDF015: typing.ClassVar['IgsSsrDataField'] = ...
    IDF016: typing.ClassVar['IgsSsrDataField'] = ...
    IDF017: typing.ClassVar['IgsSsrDataField'] = ...
    IDF018: typing.ClassVar['IgsSsrDataField'] = ...
    IDF019: typing.ClassVar['IgsSsrDataField'] = ...
    IDF020: typing.ClassVar['IgsSsrDataField'] = ...
    IDF021: typing.ClassVar['IgsSsrDataField'] = ...
    IDF022: typing.ClassVar['IgsSsrDataField'] = ...
    IDF023: typing.ClassVar['IgsSsrDataField'] = ...
    IDF024: typing.ClassVar['IgsSsrDataField'] = ...
    IDF025: typing.ClassVar['IgsSsrDataField'] = ...
    IDF026: typing.ClassVar['IgsSsrDataField'] = ...
    IDF027: typing.ClassVar['IgsSsrDataField'] = ...
    IDF028: typing.ClassVar['IgsSsrDataField'] = ...
    IDF029: typing.ClassVar['IgsSsrDataField'] = ...
    IDF030: typing.ClassVar['IgsSsrDataField'] = ...
    IDF031: typing.ClassVar['IgsSsrDataField'] = ...
    IDF032: typing.ClassVar['IgsSsrDataField'] = ...
    IDF033: typing.ClassVar['IgsSsrDataField'] = ...
    IDF034: typing.ClassVar['IgsSsrDataField'] = ...
    IDF035: typing.ClassVar['IgsSsrDataField'] = ...
    IDF036: typing.ClassVar['IgsSsrDataField'] = ...
    IDF037: typing.ClassVar['IgsSsrDataField'] = ...
    IDF038: typing.ClassVar['IgsSsrDataField'] = ...
    IDF039: typing.ClassVar['IgsSsrDataField'] = ...
    IDF040: typing.ClassVar['IgsSsrDataField'] = ...
    IDF041: typing.ClassVar['IgsSsrDataField'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IgsSsrDataField': ...
    @staticmethod
    def values() -> typing.List['IgsSsrDataField']: ...

class IgsSsrMessageType(java.lang.Enum['IgsSsrMessageType'], MessageType):
    IGM_01: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_02: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_03: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_04: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_05: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_06: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_07: typing.ClassVar['IgsSsrMessageType'] = ...
    IM_201: typing.ClassVar['IgsSsrMessageType'] = ...
    @staticmethod
    def getMessageType(string: str) -> 'IgsSsrMessageType': ...
    def getPattern(self) -> java.util.regex.Pattern: ...
    @staticmethod
    def getSatelliteId(satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int) -> int: ...
    @staticmethod
    def messageNumberToSatelliteSystem(int: int) -> org.orekit.gnss.SatelliteSystem: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IgsSsrMessageType': ...
    @staticmethod
    def values() -> typing.List['IgsSsrMessageType']: ...

class IgsSsrMessagesParser(MessagesParser):
    def __init__(self, list: java.util.List[int]): ...

class RtcmDataField(java.lang.Enum['RtcmDataField'], DataField):
    DF002: typing.ClassVar['RtcmDataField'] = ...
    DF009: typing.ClassVar['RtcmDataField'] = ...
    DF038: typing.ClassVar['RtcmDataField'] = ...
    DF040: typing.ClassVar['RtcmDataField'] = ...
    DF071: typing.ClassVar['RtcmDataField'] = ...
    DF076: typing.ClassVar['RtcmDataField'] = ...
    DF077: typing.ClassVar['RtcmDataField'] = ...
    DF078: typing.ClassVar['RtcmDataField'] = ...
    DF079: typing.ClassVar['RtcmDataField'] = ...
    DF081: typing.ClassVar['RtcmDataField'] = ...
    DF082: typing.ClassVar['RtcmDataField'] = ...
    DF083: typing.ClassVar['RtcmDataField'] = ...
    DF084: typing.ClassVar['RtcmDataField'] = ...
    DF085: typing.ClassVar['RtcmDataField'] = ...
    DF086: typing.ClassVar['RtcmDataField'] = ...
    DF087: typing.ClassVar['RtcmDataField'] = ...
    DF088: typing.ClassVar['RtcmDataField'] = ...
    DF089: typing.ClassVar['RtcmDataField'] = ...
    DF090: typing.ClassVar['RtcmDataField'] = ...
    DF091: typing.ClassVar['RtcmDataField'] = ...
    DF092: typing.ClassVar['RtcmDataField'] = ...
    DF093: typing.ClassVar['RtcmDataField'] = ...
    DF094: typing.ClassVar['RtcmDataField'] = ...
    DF095: typing.ClassVar['RtcmDataField'] = ...
    DF096: typing.ClassVar['RtcmDataField'] = ...
    DF097: typing.ClassVar['RtcmDataField'] = ...
    DF098: typing.ClassVar['RtcmDataField'] = ...
    DF099: typing.ClassVar['RtcmDataField'] = ...
    DF100: typing.ClassVar['RtcmDataField'] = ...
    DF101: typing.ClassVar['RtcmDataField'] = ...
    DF102: typing.ClassVar['RtcmDataField'] = ...
    DF103: typing.ClassVar['RtcmDataField'] = ...
    DF104: typing.ClassVar['RtcmDataField'] = ...
    DF105: typing.ClassVar['RtcmDataField'] = ...
    DF106: typing.ClassVar['RtcmDataField'] = ...
    DF107: typing.ClassVar['RtcmDataField'] = ...
    DF108: typing.ClassVar['RtcmDataField'] = ...
    DF109: typing.ClassVar['RtcmDataField'] = ...
    DF110: typing.ClassVar['RtcmDataField'] = ...
    DF111: typing.ClassVar['RtcmDataField'] = ...
    DF112: typing.ClassVar['RtcmDataField'] = ...
    DF113: typing.ClassVar['RtcmDataField'] = ...
    DF114: typing.ClassVar['RtcmDataField'] = ...
    DF115: typing.ClassVar['RtcmDataField'] = ...
    DF116: typing.ClassVar['RtcmDataField'] = ...
    DF117: typing.ClassVar['RtcmDataField'] = ...
    DF118: typing.ClassVar['RtcmDataField'] = ...
    DF119: typing.ClassVar['RtcmDataField'] = ...
    DF120: typing.ClassVar['RtcmDataField'] = ...
    DF121: typing.ClassVar['RtcmDataField'] = ...
    DF122: typing.ClassVar['RtcmDataField'] = ...
    DF123: typing.ClassVar['RtcmDataField'] = ...
    DF124: typing.ClassVar['RtcmDataField'] = ...
    DF125: typing.ClassVar['RtcmDataField'] = ...
    DF126: typing.ClassVar['RtcmDataField'] = ...
    DF127: typing.ClassVar['RtcmDataField'] = ...
    DF128: typing.ClassVar['RtcmDataField'] = ...
    DF129: typing.ClassVar['RtcmDataField'] = ...
    DF130: typing.ClassVar['RtcmDataField'] = ...
    DF131: typing.ClassVar['RtcmDataField'] = ...
    DF132: typing.ClassVar['RtcmDataField'] = ...
    DF133: typing.ClassVar['RtcmDataField'] = ...
    DF134: typing.ClassVar['RtcmDataField'] = ...
    DF135: typing.ClassVar['RtcmDataField'] = ...
    DF136: typing.ClassVar['RtcmDataField'] = ...
    DF137: typing.ClassVar['RtcmDataField'] = ...
    DF252: typing.ClassVar['RtcmDataField'] = ...
    DF289: typing.ClassVar['RtcmDataField'] = ...
    DF290: typing.ClassVar['RtcmDataField'] = ...
    DF291: typing.ClassVar['RtcmDataField'] = ...
    DF292: typing.ClassVar['RtcmDataField'] = ...
    DF293: typing.ClassVar['RtcmDataField'] = ...
    DF294: typing.ClassVar['RtcmDataField'] = ...
    DF295: typing.ClassVar['RtcmDataField'] = ...
    DF296: typing.ClassVar['RtcmDataField'] = ...
    DF297: typing.ClassVar['RtcmDataField'] = ...
    DF298: typing.ClassVar['RtcmDataField'] = ...
    DF299: typing.ClassVar['RtcmDataField'] = ...
    DF300: typing.ClassVar['RtcmDataField'] = ...
    DF301: typing.ClassVar['RtcmDataField'] = ...
    DF302: typing.ClassVar['RtcmDataField'] = ...
    DF303: typing.ClassVar['RtcmDataField'] = ...
    DF304: typing.ClassVar['RtcmDataField'] = ...
    DF305: typing.ClassVar['RtcmDataField'] = ...
    DF306: typing.ClassVar['RtcmDataField'] = ...
    DF307: typing.ClassVar['RtcmDataField'] = ...
    DF308: typing.ClassVar['RtcmDataField'] = ...
    DF309: typing.ClassVar['RtcmDataField'] = ...
    DF310: typing.ClassVar['RtcmDataField'] = ...
    DF311: typing.ClassVar['RtcmDataField'] = ...
    DF312: typing.ClassVar['RtcmDataField'] = ...
    DF313: typing.ClassVar['RtcmDataField'] = ...
    DF314: typing.ClassVar['RtcmDataField'] = ...
    DF315: typing.ClassVar['RtcmDataField'] = ...
    DF316: typing.ClassVar['RtcmDataField'] = ...
    DF317: typing.ClassVar['RtcmDataField'] = ...
    DF429: typing.ClassVar['RtcmDataField'] = ...
    DF430: typing.ClassVar['RtcmDataField'] = ...
    DF431: typing.ClassVar['RtcmDataField'] = ...
    DF432: typing.ClassVar['RtcmDataField'] = ...
    DF433: typing.ClassVar['RtcmDataField'] = ...
    DF434: typing.ClassVar['RtcmDataField'] = ...
    DF435: typing.ClassVar['RtcmDataField'] = ...
    DF436: typing.ClassVar['RtcmDataField'] = ...
    DF437: typing.ClassVar['RtcmDataField'] = ...
    DF438: typing.ClassVar['RtcmDataField'] = ...
    DF439: typing.ClassVar['RtcmDataField'] = ...
    DF440: typing.ClassVar['RtcmDataField'] = ...
    DF441: typing.ClassVar['RtcmDataField'] = ...
    DF442: typing.ClassVar['RtcmDataField'] = ...
    DF443: typing.ClassVar['RtcmDataField'] = ...
    DF444: typing.ClassVar['RtcmDataField'] = ...
    DF445: typing.ClassVar['RtcmDataField'] = ...
    DF446: typing.ClassVar['RtcmDataField'] = ...
    DF447: typing.ClassVar['RtcmDataField'] = ...
    DF448: typing.ClassVar['RtcmDataField'] = ...
    DF449: typing.ClassVar['RtcmDataField'] = ...
    DF450: typing.ClassVar['RtcmDataField'] = ...
    DF451: typing.ClassVar['RtcmDataField'] = ...
    DF452: typing.ClassVar['RtcmDataField'] = ...
    DF453: typing.ClassVar['RtcmDataField'] = ...
    DF454: typing.ClassVar['RtcmDataField'] = ...
    DF455: typing.ClassVar['RtcmDataField'] = ...
    DF456: typing.ClassVar['RtcmDataField'] = ...
    DF457: typing.ClassVar['RtcmDataField'] = ...
    DF488: typing.ClassVar['RtcmDataField'] = ...
    DF489: typing.ClassVar['RtcmDataField'] = ...
    DF490: typing.ClassVar['RtcmDataField'] = ...
    DF491: typing.ClassVar['RtcmDataField'] = ...
    DF492: typing.ClassVar['RtcmDataField'] = ...
    DF493: typing.ClassVar['RtcmDataField'] = ...
    DF494: typing.ClassVar['RtcmDataField'] = ...
    DF495: typing.ClassVar['RtcmDataField'] = ...
    DF496: typing.ClassVar['RtcmDataField'] = ...
    DF497: typing.ClassVar['RtcmDataField'] = ...
    DF498: typing.ClassVar['RtcmDataField'] = ...
    DF499: typing.ClassVar['RtcmDataField'] = ...
    DF500: typing.ClassVar['RtcmDataField'] = ...
    DF501: typing.ClassVar['RtcmDataField'] = ...
    DF502: typing.ClassVar['RtcmDataField'] = ...
    DF503: typing.ClassVar['RtcmDataField'] = ...
    DF504: typing.ClassVar['RtcmDataField'] = ...
    DF505: typing.ClassVar['RtcmDataField'] = ...
    DF506: typing.ClassVar['RtcmDataField'] = ...
    DF507: typing.ClassVar['RtcmDataField'] = ...
    DF508: typing.ClassVar['RtcmDataField'] = ...
    DF509: typing.ClassVar['RtcmDataField'] = ...
    DF510: typing.ClassVar['RtcmDataField'] = ...
    DF511: typing.ClassVar['RtcmDataField'] = ...
    DF512: typing.ClassVar['RtcmDataField'] = ...
    DF513: typing.ClassVar['RtcmDataField'] = ...
    DF514: typing.ClassVar['RtcmDataField'] = ...
    DF515: typing.ClassVar['RtcmDataField'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RtcmDataField': ...
    @staticmethod
    def values() -> typing.List['RtcmDataField']: ...

class RtcmMessageType(java.lang.Enum['RtcmMessageType'], MessageType):
    RTCM_1019: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1020: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1042: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1044: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1045: typing.ClassVar['RtcmMessageType'] = ...
    @staticmethod
    def getMessageType(string: str) -> 'RtcmMessageType': ...
    def getPattern(self) -> java.util.regex.Pattern: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RtcmMessageType': ...
    @staticmethod
    def values() -> typing.List['RtcmMessageType']: ...

class RtcmMessagesParser(MessagesParser):
    def __init__(self, list: java.util.List[int]): ...

class ByteArrayEncodedMessages(AbstractEncodedMessages):
    def __init__(self, byteArray: typing.List[int]): ...
    def start(self) -> None: ...

class InputStreamEncodedMessages(AbstractEncodedMessages):
    def __init__(self, inputStream: java.io.InputStream): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.parser")``.

    AbstractEncodedMessages: typing.Type[AbstractEncodedMessages]
    ByteArrayEncodedMessages: typing.Type[ByteArrayEncodedMessages]
    DataField: typing.Type[DataField]
    EncodedMessage: typing.Type[EncodedMessage]
    IgsSsrDataField: typing.Type[IgsSsrDataField]
    IgsSsrMessageType: typing.Type[IgsSsrMessageType]
    IgsSsrMessagesParser: typing.Type[IgsSsrMessagesParser]
    InputStreamEncodedMessages: typing.Type[InputStreamEncodedMessages]
    MessageType: typing.Type[MessageType]
    MessagesParser: typing.Type[MessagesParser]
    RtcmDataField: typing.Type[RtcmDataField]
    RtcmMessageType: typing.Type[RtcmMessageType]
    RtcmMessagesParser: typing.Type[RtcmMessagesParser]
    Units: typing.Type[Units]
