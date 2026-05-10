
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.function
import jpype
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.lexical
import org.orekit.utils
import typing



_AbstractMessageParser__T = typing.TypeVar('_AbstractMessageParser__T')  # <T>
class AbstractMessageParser(org.orekit.files.ccsds.utils.lexical.MessageParser[_AbstractMessageParser__T], typing.Generic[_AbstractMessageParser__T]):
    """
    Parser for CCSDS messages.
    
    Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until the message is complete and the parseMessage method has returned. This implies that parsers should not be used in a multi-thread context. The recommended way to use parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
    Since:
        11.0
    """
    def anticipateNext(self, anticipated: typing.Union['ProcessingState', typing.Callable]) -> None:
        """
        Anticipate what next processing state should be.
        
        Parameters:
            anticipated (ProcessingState): anticipated next processing state
        
        
        """
        ...
    def getCurrent(self) -> 'ProcessingState':
        """
        Get the current processing state.
        
        Returns:
            current processing state
        
        
        """
        ...
    def getFileFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
        Get the file format of the last message parsed.
        
        Specified by: getFileFormat in interface MessageParser
        
        Returns:
            file format of the last message parsed
        
        
        """
        ...
    def getFormatVersionKey(self) -> str:
        """
        Get the key for format version.
        
        Specified by: getFormatVersionKey in interface MessageParser
        
        Returns:
            format version key
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]:
        """
        Get the non-default token builders for special XML elements.
        
        Specified by: getSpecialXmlElementsBuilders in interface MessageParser
        
        Returns:
            map of token builders for special XML elements (keyed by XML element name)
        
        
        """
        ...
    def parseMessage(self, source: org.orekit.data.DataSource) -> _AbstractMessageParser__T:
        """
        Parse a data source.
        
        Specified by: parseMessage in interface MessageParser
        
        Parameters:
            source (DataSource): data source to parse
        
        Returns:
            parsed file
        
        
        """
        ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> None:
        """
        Process a parse token.
        
        Specified by: process in interface MessageParser
        
        Parameters:
            token (ParseToken): token to process
        
        
        """
        ...
    def setEndTagSeen(self, endTagSeen: bool) -> None:
        """
        Set the flag for XML end tag.
        
        Parameters:
            endTagSeen (boolean): if true, the XML end tag has been seen
        
        
        """
        ...
    def setFallback(self, fallback: typing.Union['ProcessingState', typing.Callable]) -> None:
        """
        Set fallback processing state.
        
        The fallback processing state is used if anticipated state fails to parse the token.
        
        Parameters:
            fallback (ProcessingState): processing state to use if anticipated state does not work
        
        
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
    Interface for processing parsing tokens for CCSDS NDM files.
    
    This interface is intended for use as the state in state design pattern, the MessageParser itself being used as the context that holds the active state.
    
    Since:
        11.0
    
    Also see:
        MessageParser
    """
    def processToken(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
        
        Returns:
            true if token was processed, false otherwise
        
        
        """
        ...

_AbstractConstituentParser__H = typing.TypeVar('_AbstractConstituentParser__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_AbstractConstituentParser__T = typing.TypeVar('_AbstractConstituentParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_AbstractConstituentParser__P = typing.TypeVar('_AbstractConstituentParser__P', bound='AbstractConstituentParser')  # <P>
class AbstractConstituentParser(AbstractMessageParser[_AbstractConstituentParser__T], typing.Generic[_AbstractConstituentParser__H, _AbstractConstituentParser__T, _AbstractConstituentParser__P]):
    """
    Parser for CCSDS messages.
    
    Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until the message is complete and the parseMessage method has returned. This implies that parsers should not be used in a multi-thread context. The recommended way to use parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
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
    def getFrameMapper(self) -> org.orekit.files.ccsds.definitions.CcsdsFrameMapper:
        """
        Get the mapping between a CCSDS frame and a Frame.
        
        Returns:
            the frame mapper.
        
        Since:
            13.1.5
        
        
        """
        ...
    def getHeader(self) -> _AbstractConstituentParser__H:
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
    Special ProcessingState that always generate an error message.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def processToken(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
        Process one token.
        
        This method always generate an error, as no data is expected in this state.
        
        Specified by: processToken in interface ProcessingState
        
        Parameters:
            token (ParseToken): token to process
        
        Returns:
            true if token was processed, false otherwise
        
        
        """
        ...

_PythonAbstractMessageParser__T = typing.TypeVar('_PythonAbstractMessageParser__T')  # <T>
class PythonAbstractMessageParser(AbstractMessageParser[_PythonAbstractMessageParser__T], typing.Generic[_PythonAbstractMessageParser__T]):
    def __init__(self, root: str, formatVersionKey: str, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            root (String): root element for XML files
            formatVersionKey (String): key for format version
        
        
        """
        ...
    def build(self) -> _PythonAbstractMessageParser__T:
        """
        Build the file from parsed entries.
        
        Returns:
            parsed file
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
        Reset parser to initial state before parsing.
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...

class PythonProcessingState(ProcessingState):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def processToken(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
        Description copied from interface: processToken Process one token.
        
        Specified by: processToken in interface ProcessingState
        
        Parameters:
            token (ParseToken): token to process
        
        Returns:
            true if token was processed, false otherwise
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

_PythonAbstractConstituentParser__H = typing.TypeVar('_PythonAbstractConstituentParser__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_PythonAbstractConstituentParser__T = typing.TypeVar('_PythonAbstractConstituentParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonAbstractConstituentParser__P = typing.TypeVar('_PythonAbstractConstituentParser__P', bound=AbstractConstituentParser)  # <P>
class PythonAbstractConstituentParser(AbstractConstituentParser[_PythonAbstractConstituentParser__H, _PythonAbstractConstituentParser__T, _PythonAbstractConstituentParser__P], typing.Generic[_PythonAbstractConstituentParser__H, _PythonAbstractConstituentParser__T, _PythonAbstractConstituentParser__P]):
    def __init__(self, root: str, formatVersionKey: str, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
    def build(self) -> _PythonAbstractConstituentParser__T:
        """
        Build the file from parsed entries.
        
        Returns:
            parsed file
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finalizeData(self) -> bool:
        """
        Finalize data after parsing.
        
        Specified by: finalizeData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
        Finalize header after parsing.
        
        Specified by: finalizeHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
        Finalize metadata after parsing.
        
        Specified by: finalizeMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def getHeader(self) -> _PythonAbstractConstituentParser__H:
        """
        Get file header to fill.
        
        Specified by: getHeader in class AbstractConstituentParser
        
        Returns:
            file header to fill
        
        
        """
        ...
    def inData(self) -> bool:
        """
        Acknowledge data parsing has started.
        
        Specified by: inData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
        Acknowledge header parsing has started.
        
        Specified by: inHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
        Acknowledge metada parsing has started.
        
        Specified by: inMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
        Prepare data for parsing.
        
        Specified by: prepareData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
        Prepare header for parsing.
        
        Specified by: prepareHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
        Prepare metadata for parsing.
        
        Specified by: prepareMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
        Reset parser to initial state before parsing.
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils.parsing")``.

    AbstractConstituentParser: typing.Type[AbstractConstituentParser]
    AbstractMessageParser: typing.Type[AbstractMessageParser]
    ErrorState: typing.Type[ErrorState]
    ProcessingState: typing.Type[ProcessingState]
    PythonAbstractConstituentParser: typing.Type[PythonAbstractConstituentParser]
    PythonAbstractMessageParser: typing.Type[PythonAbstractMessageParser]
    PythonProcessingState: typing.Type[PythonProcessingState]
