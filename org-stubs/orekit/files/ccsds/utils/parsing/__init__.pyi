import java.util
import org.orekit.data
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.lexical
import org.orekit.utils
import typing



_AbstractMessageParser__T = typing.TypeVar('_AbstractMessageParser__T')  # <T>
class AbstractMessageParser(org.orekit.files.ccsds.utils.lexical.MessageParser[_AbstractMessageParser__T], typing.Generic[_AbstractMessageParser__T]):
    """
    public abstract class AbstractMessageParser<T> extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`<T>
    
        Parser for CCSDS messages.
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            11.0
    """
    def anticipateNext(self, processingState: 'ProcessingState') -> None:
        """
            Anticipate what next processing state should be.
        
            Parameters:
                anticipated (:class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`): anticipated next processing state
        
        
        """
        ...
    def getCurrent(self) -> 'ProcessingState':
        """
            Get the current processing state.
        
            Returns:
                current processing state
        
        
        """
        ...
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
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]: ...
    def parseMessage(self, dataSource: org.orekit.data.DataSource) -> _AbstractMessageParser__T:
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> None:
        """
            Process a parse token.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.process`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
        
        """
        ...
    def setEndTagSeen(self, boolean: bool) -> None:
        """
            Set the flag for XML end tag.
        
            Parameters:
                endTagSeen (boolean): if true, the XML end tag has been seen
        
        
        """
        ...
    def setFallback(self, processingState: 'ProcessingState') -> None:
        """
            Set fallback processing state.
        
            The fallback processing state is used if anticipated state fails to parse the token.
        
            Parameters:
                fallback (:class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`): processing state to use if anticipated state does not work
        
        
        """
        ...
    def wasEndTagSeen(self) -> bool:
        """
            Check if XML end tag has been seen.
        
            Returns:
                true if XML end tag has been seen
        
        
        """
        ...

class ProcessingState:
    """
    public interface ProcessingState
    
        Interface for processing parsing tokens for CCSDS NDM files.
    
        This interface is intended for use as the state in state design pattern, the
        :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser` itself being used as the context that holds the active
        state.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
    """
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
            Returns:
                true if token was processed, false otherwise
        
        
        """
        ...

_AbstractConstituentParser__T = typing.TypeVar('_AbstractConstituentParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_AbstractConstituentParser__P = typing.TypeVar('_AbstractConstituentParser__P', bound='AbstractConstituentParser')  # <P>
class AbstractConstituentParser(AbstractMessageParser[_AbstractConstituentParser__T], typing.Generic[_AbstractConstituentParser__T, _AbstractConstituentParser__P]):
    """
    public abstract class AbstractConstituentParser<T extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<?,?>,P extends AbstractConstituentParser<T,?>> extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser`<T>
    
        Parser for CCSDS messages.
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            11.0
    """
    def finalizeData(self) -> bool:
        """
            Finalize data after parsing.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
            Finalize header after parsing.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
            Finalize metadata after parsing.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
            Get IERS conventions.
        
            Returns:
                IERS conventions to use while parsing
        
        
        """
        ...
    def getDataContext(self) -> org.orekit.data.DataContext:
        """
            Get the data context used for getting frames, time scales, and celestial bodies.
        
            Returns:
                the data context.
        
        
        """
        ...
    def getHeader(self) -> org.orekit.files.ccsds.section.Header:
        """
            Get file header to fill.
        
            Returns:
                file header to fill
        
        
        """
        ...
    def getParsedUnitsBehavior(self) -> org.orekit.files.ccsds.ndm.ParsedUnitsBehavior:
        """
            Get the behavior to adopt for handling parsed units.
        
            Returns:
                behavior to adopt for handling parsed units
        
        
        """
        ...
    def inData(self) -> bool:
        """
            Acknowledge data parsing has started.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
            Acknowledge header parsing has started.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
            Acknowledge metada parsing has started.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def isSimpleEOP(self) -> bool:
        """
            Get EOP interpolation method.
        
            Returns:
                true if tidal effects are ignored when interpolating EOP
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
            Prepare data for parsing.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
            Prepare header for parsing.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
            Prepare metadata for parsing.
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...

class ErrorState(ProcessingState):
    """
    public class ErrorState extends Object implements :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
    
        Special :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState` that always generate an error message.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
            Process one token.
        
            This method always generate an error, as no data is expected in this state.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.ProcessingState.processToken`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
            Returns:
                true if token was processed, false otherwise
        
        
        """
        ...

_PythonAbstractMessageParser__T = typing.TypeVar('_PythonAbstractMessageParser__T')  # <T>
class PythonAbstractMessageParser(AbstractMessageParser[_PythonAbstractMessageParser__T], typing.Generic[_PythonAbstractMessageParser__T]):
    def build(self) -> _PythonAbstractMessageParser__T: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None: ...

_PythonAbstractConstituentParser__T = typing.TypeVar('_PythonAbstractConstituentParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonAbstractConstituentParser__P = typing.TypeVar('_PythonAbstractConstituentParser__P', bound=AbstractConstituentParser)  # <P>
class PythonAbstractConstituentParser(AbstractConstituentParser[_PythonAbstractConstituentParser__T, _PythonAbstractConstituentParser__P], typing.Generic[_PythonAbstractConstituentParser__T, _PythonAbstractConstituentParser__P]):
    def build(self) -> _PythonAbstractConstituentParser__T: ...
    def finalize(self) -> None: ...
    def finalizeData(self) -> bool: ...
    def finalizeHeader(self) -> bool: ...
    def finalizeMetadata(self) -> bool: ...
    def getHeader(self) -> org.orekit.files.ccsds.section.Header: ...
    def inData(self) -> bool: ...
    def inHeader(self) -> bool: ...
    def inMetadata(self) -> bool: ...
    def prepareData(self) -> bool: ...
    def prepareHeader(self) -> bool: ...
    def prepareMetadata(self) -> bool: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils.parsing")``.

    AbstractConstituentParser: typing.Type[AbstractConstituentParser]
    AbstractMessageParser: typing.Type[AbstractMessageParser]
    ErrorState: typing.Type[ErrorState]
    ProcessingState: typing.Type[ProcessingState]
    PythonAbstractConstituentParser: typing.Type[PythonAbstractConstituentParser]
    PythonAbstractMessageParser: typing.Type[PythonAbstractMessageParser]
