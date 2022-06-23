import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.data
import org.orekit.errors
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.utils
import org.orekit.time
import org.orekit.utils.units
import org.xml.sax
import typing



class LexicalAnalyzer:
    """
    public interface LexicalAnalyzer
    
        Interface for CCSDS messages lexical analysis.
    
        Lexical analyzer implementations split raw streams of characters into tokens and feed them to
        :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`. Each lexical analyzer knows about a basic character stream
        format (:class:`~org.orekit.files.ccsds.utils.lexical.KvnLexicalAnalyzer` or
        :class:`~org.orekit.files.ccsds.utils.lexical.XmlLexicalAnalyzer`) but knows nothing about the CCSDS messages
        themselves. The :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser` know about CCSDS messages.
    
        Since:
            11.0
    """
    _accept__T = typing.TypeVar('_accept__T')  # <T>
    def accept(self, messageParser: 'MessageParser'[_accept__T]) -> _accept__T:
        """
            Parse a CCSDS Message.
        
            Parameters:
                messageParser (:class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`<T> messageParser): CCSDS Message parser to use
        
            Returns:
                parsed fileO
        
        
        """
        ...

class LexicalAnalyzerSelector:
    """
    public class LexicalAnalyzerSelector extends Object
    
        Utility class for selecting either :class:`~org.orekit.files.ccsds.utils.lexical.XmlLexicalAnalyzer` or
        :class:`~org.orekit.files.ccsds.utils.lexical.KvnLexicalAnalyzer` depending on data first bytes.
    
        Since:
            11.0
    """
    @staticmethod
    def select(dataSource: org.orekit.data.DataSource) -> LexicalAnalyzer: ...

_MessageParser__T = typing.TypeVar('_MessageParser__T')  # <T>
class MessageParser(typing.Generic[_MessageParser__T]):
    """
    public interface MessageParser<T>
    
        Parser for CCSDS messages.
    
        Since:
            11.0
    """
    def build(self) -> _MessageParser__T:
        """
            Build the file from parsed entries.
        
            Returns:
                parsed file
        
        
        """
        ...
    def getFormatVersionKey(self) -> str:
        """
            Get the key for format version.
        
            Returns:
                format version key
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, 'XmlTokenBuilder']: ...
    def parseMessage(self, dataSource: org.orekit.data.DataSource) -> _MessageParser__T:
        """
            Parse a data source.
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): data source to parse
        
            Returns:
                parsed file
        
        
        """
        ...
    def process(self, parseToken: 'ParseToken') -> None:
        """
            Process a parse token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

_ParseToken__EnumConsumer__T = typing.TypeVar('_ParseToken__EnumConsumer__T', bound=java.lang.Enum)  # <T>
_ParseToken__EnumListConsumer__T = typing.TypeVar('_ParseToken__EnumListConsumer__T', bound=java.lang.Enum)  # <T>
class ParseToken:
    """
    public class ParseToken extends Object
    
        Token occurring during CCSDS file parsing.
    
        Parse tokens correspond to:
    
          - bloc or entry start
          - entry content
          - bloc or entry end
          - raw lines
    
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
    """
    def __init__(self, tokenType: 'TokenType', string: str, string2: str, unit: org.orekit.utils.units.Unit, int: int, string3: str): ...
    def generateException(self, exception: java.lang.Exception) -> org.orekit.errors.OrekitException:
        """
            Generate a parse exception for this entry.
        
            Parameters:
                cause (Exception): underlying cause exception (may be null)
        
            Returns:
                exception for this entry
        
        
        """
        ...
    def getContentAsBoolean(self) -> bool:
        """
            Get the content of the entry as a boolean.
        
            Returns:
                content as a boolean
        
        
        """
        ...
    def getContentAsDouble(self) -> float:
        """
            Get the content of the entry as a double.
        
            Returns:
                content as a double
        
        
        """
        ...
    _getContentAsEnum__T = typing.TypeVar('_getContentAsEnum__T', bound=java.lang.Enum)  # <T>
    def getContentAsEnum(self, class_: typing.Type[_getContentAsEnum__T]) -> _getContentAsEnum__T:
        """
            Get the content of the entry as an enum.
        
            Parameters:
                cls (Class<T> cls): enum class
        
            Returns:
                entry content
        
        
        """
        ...
    _getContentAsEnumList__T = typing.TypeVar('_getContentAsEnumList__T', bound=java.lang.Enum)  # <T>
    def getContentAsEnumList(self, class_: typing.Type[_getContentAsEnumList__T]) -> java.util.List[_getContentAsEnumList__T]:
        """
            Get the content of the entry as a list of enum.
        
            Parameters:
                cls (Class<T> cls): enum class
        
            Returns:
                entry content
        
        
        """
        ...
    def getContentAsInt(self) -> int:
        """
            Get the content of the entry as an integer.
        
            Returns:
                content as an integer
        
        
        """
        ...
    def getContentAsNormalizedList(self) -> java.util.List[str]:
        """
            Get the content of the entry as a list of free-text strings.
        
            Free-text strings are normalized by replacing all occurrences of '_' with space, and collapsing several spaces as one
            space only.
        
            Returns:
                content of the entry as a list of free-test strings
        
        
        """
        ...
    def getContentAsNormalizedString(self) -> str:
        """
            Get the content of the entry.
        
            Free-text strings are normalized by replacing all occurrences of '_' with space, and collapsing several spaces as one
            space only.
        
            Returns:
                entry content
        
        
        """
        ...
    def getContentAsUppercaseCharacter(self) -> str:
        """
            Get the content of the entry as an uppercase character.
        
            Returns:
                content as an uppercase character
        
        
        """
        ...
    def getContentAsUppercaseList(self) -> java.util.List[str]:
        """
            Get the content of the entry as a list of normalized and uppercased strings.
        
            Returns:
                content of the entry as a list of normalized and uppercased strings
        
        
        """
        ...
    def getContentAsUppercaseString(self) -> str:
        """
            Get the content of the entry as normalized and uppercased.
        
            Returns:
                entry normalized and uppercased content
        
        
        """
        ...
    def getContentAsVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the content of the entry as a vector.
        
            Returns:
                content as a vector
        
        
        """
        ...
    def getFileName(self) -> str:
        """
            Get the name of the file.
        
            Returns:
                name of the file
        
        
        """
        ...
    def getLineNumber(self) -> int:
        """
            Get the number of the line in the CCSDS data message.
        
            Returns:
                number of the line in the CCSDS data message
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the block or entry.
        
            Returns:
                name of the block or entry
        
        
        """
        ...
    def getRawContent(self) -> str:
        """
            Get the raw content of the entry.
        
            Returns:
                entry raw content
        
        
        """
        ...
    def getType(self) -> 'TokenType':
        """
            Get the type of the token.
        
            Returns:
                type of the token
        
        
        """
        ...
    def getUnits(self) -> org.orekit.utils.units.Unit:
        """
            Get the units.
        
            Returns:
                units of the entry (may be null)
        
        
        """
        ...
    def processAsBoolean(self, booleanConsumer: 'ParseToken.BooleanConsumer') -> bool:
        """
            Process the content as a boolean.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.BooleanConsumer`): consumer of the boolean
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsCenter(self, centerConsumer: 'ParseToken.CenterConsumer', celestialBodies: org.orekit.bodies.CelestialBodies) -> bool:
        """
            Process the content as a body center.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.CenterConsumer`): consumer of the body center
                celestialBodies (:class:`~org.orekit.bodies.CelestialBodies`): factory for celestial bodies
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsCenterList(self, centerListConsumer: 'ParseToken.CenterListConsumer', celestialBodies: org.orekit.bodies.CelestialBodies) -> bool:
        """
            Process the content as a body center list.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.CenterListConsumer`): consumer of the body center list
                celestialBodies (:class:`~org.orekit.bodies.CelestialBodies`): factory for celestial bodies
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsDate(self, dateConsumer: 'ParseToken.DateConsumer', contextBinding: org.orekit.files.ccsds.utils.ContextBinding) -> bool:
        """
            Process the content as a date.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.DateConsumer`): consumer of the date
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
        
            Returns:
                always returns :code:`true` (or throws an exception)
        
        
        """
        ...
    def processAsDouble(self, unit: org.orekit.utils.units.Unit, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, doubleConsumer: 'ParseToken.DoubleConsumer') -> bool:
        """
            Process the content as a double.
        
            Parameters:
                standard (:class:`~org.orekit.utils.units.Unit`): units of parsed content as specified by CCSDS standard
                behavior (:class:`~org.orekit.files.ccsds.ndm.ParsedUnitsBehavior`): behavior to adopt for parsed unit
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.DoubleConsumer`): consumer of the double
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsDoublyIndexedDouble(self, int: int, int2: int, unit: org.orekit.utils.units.Unit, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, doublyIndexedDoubleConsumer: 'ParseToken.DoublyIndexedDoubleConsumer') -> bool:
        """
            Process the content as a doubly-indexed double.
        
            Parameters:
                i (int): first index
                j (int): second index
                standard (:class:`~org.orekit.utils.units.Unit`): units of parsed content as specified by CCSDS standard
                behavior (:class:`~org.orekit.files.ccsds.ndm.ParsedUnitsBehavior`): behavior to adopt for parsed unit
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.DoublyIndexedDoubleConsumer`): consumer of the doubly-indexed double
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    _processAsEnum__T = typing.TypeVar('_processAsEnum__T', bound=java.lang.Enum)  # <T>
    def processAsEnum(self, class_: typing.Type[_processAsEnum__T], enumConsumer: 'ParseToken.EnumConsumer'[_processAsEnum__T]) -> bool:
        """
            Process the content as an enum.
        
            Parameters:
                cls (Class<T> cls): enum class
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.EnumConsumer`<T> consumer): consumer of the enum
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    _processAsEnumsList__T = typing.TypeVar('_processAsEnumsList__T', bound=java.lang.Enum)  # <T>
    def processAsEnumsList(self, class_: typing.Type[_processAsEnumsList__T], enumListConsumer: 'ParseToken.EnumListConsumer'[_processAsEnumsList__T]) -> bool:
        """
            Process the content as a list of enums.
        
            Parameters:
                cls (Class<T> cls): enum class
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.EnumListConsumer`<T> consumer): consumer of the enums list
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsFrame(self, frameConsumer: 'ParseToken.FrameConsumer', contextBinding: org.orekit.files.ccsds.utils.ContextBinding, boolean: bool, boolean2: bool, boolean3: bool) -> bool:
        """
            Process the content as a frame.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.FrameConsumer`): consumer of the frame
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                allowCelestial (boolean): if true, :class:`~org.orekit.files.ccsds.definitions.CelestialBodyFrame` are allowed
                allowOrbit (boolean): if true, :class:`~org.orekit.files.ccsds.definitions.OrbitRelativeFrame` are allowed
                allowSpacecraft (boolean): if true, :class:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame` are allowed
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsIndexedDouble(self, int: int, unit: org.orekit.utils.units.Unit, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, indexedDoubleConsumer: 'ParseToken.IndexedDoubleConsumer') -> bool:
        """
            Process the content as an indexed double.
        
            Parameters:
                i (int): index
                standard (:class:`~org.orekit.utils.units.Unit`): units of parsed content as specified by CCSDS standard
                behavior (:class:`~org.orekit.files.ccsds.ndm.ParsedUnitsBehavior`): behavior to adopt for parsed unit
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.IndexedDoubleConsumer`): consumer of the indexed double
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsIndexedNormalizedString(self, int: int, indexedStringConsumer: 'ParseToken.IndexedStringConsumer') -> bool:
        """
            Process the content as an indexed normalized string.
        
            Parameters:
                index (int): index
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.IndexedStringConsumer`): consumer of the indexed normalized string
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsIndexedUppercaseString(self, int: int, indexedStringConsumer: 'ParseToken.IndexedStringConsumer') -> bool:
        """
            Process the content as an indexed normalized uppercase string.
        
            Parameters:
                index (int): index
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.IndexedStringConsumer`): consumer of the indexed normalized uppercase string
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsInteger(self, intConsumer: 'ParseToken.IntConsumer') -> bool:
        """
            Process the content as an integer.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.IntConsumer`): consumer of the integer
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsIntegerArray(self, integerArrayConsumer: 'ParseToken.IntegerArrayConsumer') -> bool:
        """
            Process the content as an array of integers.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.IntegerArrayConsumer`): consumer of the array
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsLabeledDouble(self, char: str, unit: org.orekit.utils.units.Unit, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, labeledDoubleConsumer: 'ParseToken.LabeledDoubleConsumer') -> bool:
        """
            Process the content as an labeled double.
        
            Parameters:
                label (char): label
                standard (:class:`~org.orekit.utils.units.Unit`): units of parsed content as specified by CCSDS standard
                behavior (:class:`~org.orekit.files.ccsds.ndm.ParsedUnitsBehavior`): behavior to adopt for parsed unit
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.LabeledDoubleConsumer`): consumer of the indexed double
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsNormalizedCharacter(self, charConsumer: 'ParseToken.CharConsumer') -> bool:
        """
            Process the content as a normalized character.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.CharConsumer`): consumer of the normalized character
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsNormalizedList(self, stringListConsumer: 'ParseToken.StringListConsumer') -> bool:
        """
            Process the content as a list of normalized strings.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.StringListConsumer`): consumer of the normalized strings list
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsNormalizedString(self, stringConsumer: 'ParseToken.StringConsumer') -> bool:
        """
            Process the content as a normalized string.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.StringConsumer`): consumer of the normalized string
        
            Returns:
                always returns :code:`true`
        
            Also see:
                :meth:`~org.orekit.files.ccsds.utils.lexical.ParseToken.processAsUppercaseString`
        
        
        """
        ...
    def processAsTimeSystem(self, timeSystemConsumer: 'ParseToken.TimeSystemConsumer') -> bool:
        """
            Process the content as a time system.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.TimeSystemConsumer`): consumer of the time system
        
            Returns:
                always returns :code:`true` (or throws an exception)
        
        
        """
        ...
    def processAsUnitList(self, unitListConsumer: 'ParseToken.UnitListConsumer') -> bool:
        """
            Process the content as a list of units.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.UnitListConsumer`): consumer of the time scale
        
            Returns:
                always returns :code:`true` (or throws an exception)
        
        
        """
        ...
    def processAsUppercaseList(self, stringListConsumer: 'ParseToken.StringListConsumer') -> bool:
        """
            Process the content as a list of normalized uppercase strings.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.StringListConsumer`): consumer of the normalized uppercase strings list
        
            Returns:
                always returns :code:`true`
        
        
        """
        ...
    def processAsUppercaseString(self, stringConsumer: 'ParseToken.StringConsumer') -> bool:
        """
            Process the content as a normalized uppercase string.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.StringConsumer`): consumer of the normalized uppercase string
        
            Returns:
                always returns :code:`true`
        
            Also see:
                :meth:`~org.orekit.files.ccsds.utils.lexical.ParseToken.processAsNormalizedString`
        
        
        """
        ...
    def processAsVector(self, vectorConsumer: 'ParseToken.VectorConsumer') -> bool:
        """
            Process the content as a vector.
        
            Parameters:
                consumer (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.VectorConsumer`): consumer of the vector
        
            Returns:
                always returns :code:`true` (or throws an exception)
        
        
        """
        ...
    class BooleanConsumer:
        def accept(self, boolean: bool) -> None: ...
    class CenterConsumer:
        def accept(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None: ...
    class CenterListConsumer:
        def accept(self, list: java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]) -> None: ...
    class CharConsumer:
        def accept(self, char: str) -> None: ...
    class DateConsumer:
        def accept(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    class DoubleConsumer:
        def accept(self, double: float) -> None: ...
    class DoublyIndexedDoubleConsumer:
        def accept(self, int: int, int2: int, double: float) -> None: ...
    class EnumConsumer(typing.Generic[_ParseToken__EnumConsumer__T]):
        def accept(self, t: _ParseToken__EnumConsumer__T) -> None: ...
    class EnumListConsumer(typing.Generic[_ParseToken__EnumListConsumer__T]):
        def accept(self, list: java.util.List[_ParseToken__EnumListConsumer__T]) -> None: ...
    class FrameConsumer:
        def accept(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None: ...
    class IndexedDoubleConsumer:
        def accept(self, int: int, double: float) -> None: ...
    class IndexedStringConsumer:
        def accept(self, int: int, string: str) -> None: ...
    class IntConsumer:
        def accept(self, int: int) -> None: ...
    class IntegerArrayConsumer:
        def accept(self, intArray: typing.List[int]) -> None: ...
    class LabeledDoubleConsumer:
        def accept(self, char: str, double: float) -> None: ...
    class StringConsumer:
        def accept(self, string: str) -> None: ...
    class StringListConsumer:
        def accept(self, list: java.util.List[str]) -> None: ...
    class TimeSystemConsumer:
        def accept(self, timeSystem: org.orekit.files.ccsds.definitions.TimeSystem) -> None: ...
    class UnitListConsumer:
        def accept(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
    class VectorConsumer:
        def accept(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None: ...

class TokenType(java.lang.Enum['TokenType']):
    """
    public enum TokenType extends Enum<:class:`~org.orekit.files.ccsds.utils.lexical.TokenType`>
    
        Enumerate for tokens occurring during CCSDS file parsing.
    
        Parse tokens correspond to:
    
          - bloc start
          - entry content
          - bloc end
    
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`
    """
    START: typing.ClassVar['TokenType'] = ...
    ENTRY: typing.ClassVar['TokenType'] = ...
    STOP: typing.ClassVar['TokenType'] = ...
    RAW_LINE: typing.ClassVar['TokenType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TokenType':
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
    def values() -> typing.List['TokenType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TokenType c : TokenType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class XmlTokenBuilder:
    """
    public interface XmlTokenBuilder
    
        Builder for building :class:`~org.orekit.files.ccsds.utils.lexical.ParseToken` from XML elements.
    
        The regular handling of regular XML elements is to used the element name as the token name, the element content as the
        token content and the "units" attribute for the units. In some cases however the token name should be extracted from
        attributes, and sometimes even the content. This interface allows to define all these behaviors, by providing
        specialized builders to the lexical analyzer when it calls their
        :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.getSpecialXmlElementsBuilders` method.
    
        Since:
            11.0
    """
    def buildTokens(self, boolean: bool, string: str, string2: str, attributes: org.xml.sax.Attributes, int: int, string3: str) -> java.util.List[ParseToken]: ...

class KvnLexicalAnalyzer(LexicalAnalyzer):
    """
    public class KvnLexicalAnalyzer extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer`
    
        Lexical analyzer for Key-Value Notation CCSDS messages.
    
        Since:
            11.0
    """
    def __init__(self, dataSource: org.orekit.data.DataSource): ...
    _accept__T = typing.TypeVar('_accept__T')  # <T>
    def accept(self, messageParser: MessageParser[_accept__T]) -> _accept__T:
        """
            Parse a CCSDS Message.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer.accept`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer`
        
            Parameters:
                messageParser (:class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`<T> messageParser): CCSDS Message parser to use
        
            Returns:
                parsed fileO
        
        
        """
        ...

class MessageVersionXmlTokenBuilder(XmlTokenBuilder):
    """
    public class MessageVersionXmlTokenBuilder extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder`
    
        Builder for the root element with CCSDS message version.
    
        All parsers for CCSDS ADM, ODM and TDM messages need to handle the root level XML element specially. OPM file for
        example have a root element of the form:
    
        .. code-block: java
        
        
           <opm id="CCSDS_OPM_VERS" verion="3.0">
         
    
        This :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder` will generate two
        :class:`~org.orekit.files.ccsds.utils.lexical.ParseToken` from this root element:
    
          1.  one with name set to "opm", type set to :meth:`~org.orekit.files.ccsds.utils.lexical.TokenType.START` and no content
          2.  one with name set to "CCSDS_OPM_VERS", type set to :meth:`~org.orekit.files.ccsds.utils.lexical.TokenType.ENTRY` and
            content set to "3.0"
    
    
        Since:
            11.0
    """
    def __init__(self): ...
    def buildTokens(self, boolean: bool, string: str, string2: str, attributes: org.xml.sax.Attributes, int: int, string3: str) -> java.util.List[ParseToken]: ...

class PythonLexicalAnalyzer(LexicalAnalyzer):
    """
    public class PythonLexicalAnalyzer extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer`
    """
    def __init__(self): ...
    _accept__T = typing.TypeVar('_accept__T')  # <T>
    def accept(self, messageParser: MessageParser[_accept__T]) -> _accept__T:
        """
            Parse a CCSDS Message.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer.accept`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer`
        
            Parameters:
                messageParser (:class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`<T> messageParser): CCSDS Message parser to use
        
            Returns:
                parsed fileO
        
        
        """
        ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

_PythonMessageParser__T = typing.TypeVar('_PythonMessageParser__T')  # <T>
class PythonMessageParser(MessageParser[_PythonMessageParser__T], typing.Generic[_PythonMessageParser__T]):
    """
    public class PythonMessageParser<T> extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`<T>
    """
    def __init__(self): ...
    def build(self) -> _PythonMessageParser__T:
        """
            Build the file from parsed entries.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.build`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Returns:
                parsed file
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getFormatVersionKey(self) -> str:
        """
            Get the key for format version.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.getFormatVersionKey`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Returns:
                format version key
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, XmlTokenBuilder]: ...
    def parseMessage(self, dataSource: org.orekit.data.DataSource) -> _PythonMessageParser__T:
        """
            Parse a data source.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.parseMessage`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): data source to parse
        
            Returns:
                parsed file
        
        
        """
        ...
    def process(self, parseToken: ParseToken) -> None:
        """
            Process a parse token.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.process`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.reset`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class PythonXmlTokenBuilder(XmlTokenBuilder):
    """
    public class PythonXmlTokenBuilder extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder`
    """
    def __init__(self): ...
    def buildTokens(self, boolean: bool, string: str, string2: str, attributes: org.xml.sax.Attributes, int: int, string3: str) -> java.util.List[ParseToken]: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class RegularXmlTokenBuilder(XmlTokenBuilder):
    """
    public class RegularXmlTokenBuilder extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder`
    
        Regular builder using XML elements names and content for tokens.
    
        Each tag generates exactly one token, either a :meth:`~org.orekit.files.ccsds.utils.lexical.TokenType.START`, or
        :meth:`~org.orekit.files.ccsds.utils.lexical.TokenType.STOP` token without content for non-leaf elements, or a
        :meth:`~org.orekit.files.ccsds.utils.lexical.TokenType.ENTRY` token with content for leaf elements.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def buildTokens(self, boolean: bool, string: str, string2: str, attributes: org.xml.sax.Attributes, int: int, string3: str) -> java.util.List[ParseToken]: ...

class UserDefinedXmlTokenBuilder(XmlTokenBuilder):
    """
    public class UserDefinedXmlTokenBuilder extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder`
    
        Builder for user-defined parameters.
    
        User-defined elements are of the form:
    
        .. code-block: java
        
        
           <USER_DEFINED parameter="SOME_PARAMETER_NAME">value</USER_DEFINED>
         
    
        This :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder` will generate a single
        :class:`~org.orekit.files.ccsds.utils.lexical.ParseToken` from this root element with name set to "SOME_PARAMETER_NAME",
        type set to :meth:`~org.orekit.files.ccsds.utils.lexical.TokenType.ENTRY` and content set to :code:`value`.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def buildTokens(self, boolean: bool, string: str, string2: str, attributes: org.xml.sax.Attributes, int: int, string3: str) -> java.util.List[ParseToken]: ...

class XmlLexicalAnalyzer(LexicalAnalyzer):
    """
    public class XmlLexicalAnalyzer extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer`
    
        Lexical analyzer for XML CCSDS messages.
    
        Since:
            11.0
    """
    def __init__(self, dataSource: org.orekit.data.DataSource): ...
    _accept__T = typing.TypeVar('_accept__T')  # <T>
    def accept(self, messageParser: MessageParser[_accept__T]) -> _accept__T:
        """
            Parse a CCSDS Message.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer.accept`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzer`
        
            Parameters:
                messageParser (:class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`<T> messageParser): CCSDS Message parser to use
        
            Returns:
                parsed fileO
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils.lexical")``.

    KvnLexicalAnalyzer: typing.Type[KvnLexicalAnalyzer]
    LexicalAnalyzer: typing.Type[LexicalAnalyzer]
    LexicalAnalyzerSelector: typing.Type[LexicalAnalyzerSelector]
    MessageParser: typing.Type[MessageParser]
    MessageVersionXmlTokenBuilder: typing.Type[MessageVersionXmlTokenBuilder]
    ParseToken: typing.Type[ParseToken]
    PythonLexicalAnalyzer: typing.Type[PythonLexicalAnalyzer]
    PythonMessageParser: typing.Type[PythonMessageParser]
    PythonXmlTokenBuilder: typing.Type[PythonXmlTokenBuilder]
    RegularXmlTokenBuilder: typing.Type[RegularXmlTokenBuilder]
    TokenType: typing.Type[TokenType]
    UserDefinedXmlTokenBuilder: typing.Type[UserDefinedXmlTokenBuilder]
    XmlLexicalAnalyzer: typing.Type[XmlLexicalAnalyzer]
    XmlTokenBuilder: typing.Type[XmlTokenBuilder]
