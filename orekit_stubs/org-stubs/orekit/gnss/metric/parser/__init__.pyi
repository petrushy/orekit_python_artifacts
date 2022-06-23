import java.io
import java.lang
import java.util
import java.util.regex
import org.orekit.gnss
import org.orekit.gnss.metric.messages
import org.orekit.utils.units
import typing



class DataField:
    """
    public interface DataField
    
        Interface for data fields used to parsed encoded messages.
    
        Since:
            11.0
    """
    def booleanValue(self, encodedMessage: 'EncodedMessage') -> bool:
        """
            Get the value of the field as a boolean.
        
            Parameters:
                message (:class:`~org.orekit.gnss.metric.parser.EncodedMessage`): message containing the data
        
            Returns:
                boolean value of the field
        
        
        """
        ...
    def doubleValue(self, encodedMessage: 'EncodedMessage') -> float:
        """
            Get the value of the field as a double.
        
            Parameters:
                message (:class:`~org.orekit.gnss.metric.parser.EncodedMessage`): message containing the data
        
            Returns:
                double value of the field
        
        
        """
        ...
    def intValue(self, encodedMessage: 'EncodedMessage') -> int:
        """
            Get the value of the field as an integer.
        
            Parameters:
                message (:class:`~org.orekit.gnss.metric.parser.EncodedMessage`): message containing the data
        
            Returns:
                integer value of the field
        
        
        """
        ...
    def stringValue(self, encodedMessage: 'EncodedMessage', int: int) -> str:
        """
            Get the value of the field as a String.
        
            Parameters:
                message (:class:`~org.orekit.gnss.metric.parser.EncodedMessage`): message containing the data
                n (int): number of UTF8 characters
        
            Returns:
                String value of the field
        
        
        """
        ...

class EncodedMessage:
    """
    public interface EncodedMessage
    
        Interface for getting bits forming encoded messages.
    
        Classes implementing this interface must contain exactly one complete message.
    
        Since:
            11.0
    """
    def extractBits(self, int: int) -> int:
        """
            Extract the next n bits from the encoded message.
        
            Parameters:
                n (int): number of bits to extract (cannot exceed 32 bits)
        
            Returns:
                bits packed as the LSB of a 64 bits primitive long
        
        
        """
        ...
    def start(self) -> None:
        """
            Start message extraction.
        
        """
        ...

class MessageType:
    """
    public interface MessageType
    
        Interface for encoded message types.
    
        Since:
            11.0
    """
    def parse(self, encodedMessage: EncodedMessage, int: int) -> org.orekit.gnss.metric.messages.ParsedMessage:
        """
            Parse an encoded message.
        
            Parameters:
                encodedMessage (:class:`~org.orekit.gnss.metric.parser.EncodedMessage`): encoded message to parse
                messageNumber (int): message number
        
            Returns:
                parsed message
        
        
        """
        ...

class MessagesParser:
    """
    public abstract class MessagesParser extends Object
    
        Parser for IGS encoded messages.
    
        Since:
            11.0
    """
    def __init__(self, list: java.util.List[int]): ...
    def parse(self, encodedMessage: EncodedMessage, boolean: bool) -> org.orekit.gnss.metric.messages.ParsedMessage:
        """
            Parse one message.
        
            Parameters:
                message (:class:`~org.orekit.gnss.metric.parser.EncodedMessage`): encoded message to parse
                ignoreUnknownMessageTypes (boolean): if true, unknown messages types are silently ignored
        
            Returns:
                parsed message, or null if parse not possible and :code:`ignoreUnknownMessageTypes` is true
        
        
        """
        ...

class Units:
    """
    public class Units extends Object
    
        Units used in RTCM and IGS SSR messages.
    
        Since:
            11.0
    """
    SEMI_CIRCLE: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` SEMI_CIRCLE
    
        Semi-circles units.
    
    """
    NS: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` NS
    
        Nanoseconds units.
    
    """
    MM: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` MM
    
        Millimetres units.
    
    """
    MM_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` MM_PER_S
    
        Millimetres per second units.
    
    """
    MM_PER_S2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` MM_PER_S2
    
        Millimetres per square second units.
    
    """
    KM_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM_PER_S
    
        Kilometers par second units.
    
    """
    KM_PER_S2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM_PER_S2
    
        Kilometers par square second units.
    
    """

class AbstractEncodedMessages(EncodedMessage):
    """
    public abstract class AbstractEncodedMessages extends Object implements :class:`~org.orekit.gnss.metric.parser.EncodedMessage`
    
        Encoded messages as a sequence of bytes.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def extractBits(self, int: int) -> int:
        """
            Extract the next n bits from the encoded message.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.parser.EncodedMessage.extractBits`Â in
                interfaceÂ :class:`~org.orekit.gnss.metric.parser.EncodedMessage`
        
            Parameters:
                n (int): number of bits to extract (cannot exceed 32 bits)
        
            Returns:
                bits packed as the LSB of a 64 bits primitive long
        
        
        """
        ...
    def start(self) -> None:
        """
            Start message extraction.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.parser.EncodedMessage.start`Â in
                interfaceÂ :class:`~org.orekit.gnss.metric.parser.EncodedMessage`
        
        
        """
        ...

class IgsSsrDataField(java.lang.Enum['IgsSsrDataField'], DataField):
    """
    public enum IgsSsrDataField extends Enum<:class:`~org.orekit.gnss.metric.parser.IgsSsrDataField`> implements :class:`~org.orekit.gnss.metric.parser.DataField`
    
        Enum containing all intermediate level data fields that can be parsed to build an IGS SSR message.
    
        Since:
            11.0
    """
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
    def valueOf(string: str) -> 'IgsSsrDataField':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['IgsSsrDataField']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (IgsSsrDataField c : IgsSsrDataField.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IgsSsrMessageType(java.lang.Enum['IgsSsrMessageType'], MessageType):
    """
    public enum IgsSsrMessageType extends Enum<:class:`~org.orekit.gnss.metric.parser.IgsSsrMessageType`> implements :class:`~org.orekit.gnss.metric.parser.MessageType`
    
        Enum containing the supported IGS SSR messages types.
    
        Since:
            11.0
    
        Also see:
            "IGS State Space Representation (SSR) Format, Version 1.00, October 2020."
    """
    IGM_01: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_02: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_03: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_04: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_05: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_06: typing.ClassVar['IgsSsrMessageType'] = ...
    IGM_07: typing.ClassVar['IgsSsrMessageType'] = ...
    IM_201: typing.ClassVar['IgsSsrMessageType'] = ...
    @staticmethod
    def getMessageType(string: str) -> 'IgsSsrMessageType':
        """
            Get the message type corresponding to a message number.
        
            Parameters:
                number (String): message number
        
            Returns:
                the message type corresponding to the message number
        
        
        """
        ...
    def getPattern(self) -> java.util.regex.Pattern:
        """
            Get the message number.
        
            Returns:
                message number
        
        
        """
        ...
    @staticmethod
    def getSatelliteId(satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int) -> int:
        """
            Transform the satellite ID parsed from the IGS SSR message to the real ID.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): the satellite system of the parsed message
                id (int): the parsed satellite ID
        
            Returns:
                the real satellite ID
        
        
        """
        ...
    @staticmethod
    def messageNumberToSatelliteSystem(int: int) -> org.orekit.gnss.SatelliteSystem:
        """
            Find the satellite system corresponding to the sub-type message number.
        
            See Table 5 of reference
        
            Parameters:
                subTypeMessage (int): message umber
        
            Returns:
                the corresponding satellite system
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IgsSsrMessageType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['IgsSsrMessageType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (IgsSsrMessageType c : IgsSsrMessageType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IgsSsrMessagesParser(MessagesParser):
    """
    public class IgsSsrMessagesParser extends :class:`~org.orekit.gnss.metric.parser.MessagesParser`
    
        Parser for SSR encoded messages.
    
        Since:
            11.0
    """
    def __init__(self, list: java.util.List[int]): ...

class RtcmDataField(java.lang.Enum['RtcmDataField'], DataField):
    """
    public enum RtcmDataField extends Enum<:class:`~org.orekit.gnss.metric.parser.RtcmDataField`> implements :class:`~org.orekit.gnss.metric.parser.DataField`
    
        Enum containing all intermediate level data fields that can be parsed to build a RTCM message.
    
        Since:
            11.0
    """
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
    def valueOf(string: str) -> 'RtcmDataField':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['RtcmDataField']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (RtcmDataField c : RtcmDataField.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RtcmMessageType(java.lang.Enum['RtcmMessageType'], MessageType):
    """
    public enum RtcmMessageType extends Enum<:class:`~org.orekit.gnss.metric.parser.RtcmMessageType`> implements :class:`~org.orekit.gnss.metric.parser.MessageType`
    
        Enum containing the supported RTCM messages types.
    
        Since:
            11.0
    
        Also see:
            "RTCM STANDARD 10403.3, DIFFERENTIAL GNSS (GLOBAL NAVIGATION SATELLITE SYSTEMS) SERVICES â€“ VERSION 3, October 2016."
    """
    RTCM_1019: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1020: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1042: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1044: typing.ClassVar['RtcmMessageType'] = ...
    RTCM_1045: typing.ClassVar['RtcmMessageType'] = ...
    @staticmethod
    def getMessageType(string: str) -> 'RtcmMessageType':
        """
            Get the message type corresponding to a message number.
        
            Parameters:
                rtcmNumber (String): message number
        
            Returns:
                the message type corresponding to the message number
        
        
        """
        ...
    def getPattern(self) -> java.util.regex.Pattern:
        """
            Get the message number.
        
            Returns:
                message number
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RtcmMessageType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['RtcmMessageType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (RtcmMessageType c : RtcmMessageType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RtcmMessagesParser(MessagesParser):
    """
    public class RtcmMessagesParser extends :class:`~org.orekit.gnss.metric.parser.MessagesParser`
    
        Parser for RTCM encoded messages.
    
        Since:
            11.0
    """
    def __init__(self, list: java.util.List[int]): ...

class ByteArrayEncodedMessages(AbstractEncodedMessages):
    """
    public class ByteArrayEncodedMessages extends :class:`~org.orekit.gnss.metric.parser.AbstractEncodedMessages`
    
        Encoded messages as a byte array.
    
        Since:
            11.0
    """
    def __init__(self, byteArray: typing.List[int]): ...
    def start(self) -> None:
        """
            Start message extraction.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.parser.EncodedMessage.start`Â in
                interfaceÂ :class:`~org.orekit.gnss.metric.parser.EncodedMessage`
        
            Overrides:
                :meth:`~org.orekit.gnss.metric.parser.AbstractEncodedMessages.start`Â in
                classÂ :class:`~org.orekit.gnss.metric.parser.AbstractEncodedMessages`
        
        
        """
        ...

class InputStreamEncodedMessages(AbstractEncodedMessages):
    """
    public class InputStreamEncodedMessages extends :class:`~org.orekit.gnss.metric.parser.AbstractEncodedMessages`
    
        Encoded message from an input stream.
    
        Since:
            11.0
    """
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
