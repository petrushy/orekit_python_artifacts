
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.time
import typing



class AbstractWriter:
    """
    Top level class for writing CCSDS message sections.
    
    Since:
        11.0
    """
    def enterSection(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None:
        """
        Enter the section.
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if an I/O error occurs.
        
        Since:
            12.0
        
        
        """
        ...
    def exitSection(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None:
        """
        Exit the section.
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if an I/O error occurs.
        
        Since:
            12.0
        
        
        """
        ...
    def write(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None:
        """
        Write the section, including surrounding tags.
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class HeaderKey(java.lang.Enum['HeaderKey']):
    """
    Keywords allowed in Header.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['HeaderKey'] = ...
    CLASSIFICATION: typing.ClassVar['HeaderKey'] = ...
    CREATION_DATE: typing.ClassVar['HeaderKey'] = ...
    ORIGINATOR: typing.ClassVar['HeaderKey'] = ...
    MESSAGE_ID: typing.ClassVar['HeaderKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, header: 'Header') -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            header (Header): header to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'HeaderKey':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['HeaderKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (HeaderKey c : HeaderKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class HeaderProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    ProcessingState for Header.
    
    Since:
        11.0
    """
    def __init__(self, parser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]):
        """
        Simple constructor.
        
        Parameters:
            parser (AbstractConstituentParser<?, ?, ?> parser): parser for the complete message
        
        
        """
        ...
    def processToken(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
        Process one token.
        
        Specified by: processToken in interface ProcessingState
        
        Parameters:
            token (ParseToken): token to process
        
        Returns:
            true if token was processed, false otherwise
        
        
        """
        ...

class KvnStructureKey(java.lang.Enum['KvnStructureKey']):
    """
    Keys for KVN format structure.
    
    Since:
        11.0
    """
    META: typing.ClassVar['KvnStructureKey'] = ...
    DATA: typing.ClassVar['KvnStructureKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, parser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            parser (AbstractConstituentParser<?, ?, ?> parser): file parser
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'KvnStructureKey':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['KvnStructureKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (KvnStructureKey c : KvnStructureKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class KvnStructureProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    ProcessingState for structure of KVN CCSDS Messages.
    
    Since:
        11.0
    """
    def __init__(self, parser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]):
        """
        Simple constructor.
        
        Parameters:
            parser (AbstractConstituentParser<?, ?, ?> parser): parser for the complete message
        
        
        """
        ...
    def processToken(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
        Process one token.
        
        Specified by: processToken in interface ProcessingState
        
        Parameters:
            token (ParseToken): token to process
        
        Returns:
            true if token was processed, false otherwise
        
        
        """
        ...

class MetadataKey(java.lang.Enum['MetadataKey']):
    """
    Keys for Metadata entries.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['MetadataKey'] = ...
    TIME_SYSTEM: typing.ClassVar['MetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, metadata: 'Metadata') -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            metadata (Metadata): metadata to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'MetadataKey':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['MetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (MetadataKey c : MetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Section:
    """
    Top level interface for all CCSDS message sections.
    
    Since:
        11.0
    """
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Parameters:
            version (double): format version
        
        
        """
        ...

_Segment__M = typing.TypeVar('_Segment__M', bound='Metadata')  # <M>
_Segment__D = typing.TypeVar('_Segment__D', bound='Data')  # <D>
class Segment(typing.Generic[_Segment__M, _Segment__D]):
    """
    NDM segments are (Metadata, Data) pairs.
    
    Since:
        11.0
    """
    def __init__(self, metadata: _Segment__M, data: _Segment__D):
        """
        Constructor.
        
        Parameters:
            metadata (Segment): segment metadata
            data (Segment): segment data
        
        
        """
        ...
    def getData(self) -> _Segment__D:
        """
        Get the segment data.
        
        Returns:
            segment data
        
        
        """
        ...
    def getMetadata(self) -> _Segment__M:
        """
        Get the segment metadata.
        
        Returns:
            segment metadata
        
        
        """
        ...
    def setMetadata(self, metadata: _Segment__M) -> None:
        """
        Set the segment metadata.
        
        Parameters:
            metadata (Segment): the segment metadata
        
        
        """
        ...

class XmlStructureKey(java.lang.Enum['XmlStructureKey']):
    """
    Keys for XML format structure.
    
    Since:
        11.0
    """
    body: typing.ClassVar['XmlStructureKey'] = ...
    segment: typing.ClassVar['XmlStructureKey'] = ...
    header: typing.ClassVar['XmlStructureKey'] = ...
    metadata: typing.ClassVar['XmlStructureKey'] = ...
    data: typing.ClassVar['XmlStructureKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, parser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            parser (AbstractConstituentParser<?, ?, ?> parser): file parser
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'XmlStructureKey':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['XmlStructureKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (XmlStructureKey c : XmlStructureKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class XmlStructureProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    ProcessingState for structure of XML CCSDS Messages.
    
    Since:
        11.0
    """
    def __init__(self, root: str, parser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]):
        """
        Simple constructor.
        
        Parameters:
            root (String): name of the root element
            parser (AbstractConstituentParser<?, ?, ?> parser): parser for the complete message
        
        
        """
        ...
    def processToken(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
        Process one token.
        
        Specified by: processToken in interface ProcessingState
        
        Parameters:
            token (ParseToken): token to process
        
        Returns:
            true if token was processed, false otherwise
        
        
        """
        ...

class CommentsContainer(Section):
    """
    Container for comments in various CCSDS messages.
    
    CCSDS files accept comments only at the beginning of sections. Once header/metadata/data content has started, comments in the corresponding section are refused.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Create a new meta-data.
        """
        ...
    def acceptComments(self) -> bool:
        """
        Check if container is still accepting comments.
        
        A container that still accept comments does not contain any other data.
        
        Returns:
            true if container is still accepting comments
        
        
        """
        ...
    def addComment(self, comment: str) -> bool:
        """
        Add comment.
        
        Comments are accepted only at start. Once other content is stored in the same section, comments are refused.
        
        Parameters:
            comment (String): comment line
        
        Returns:
            true if comment was accepted
        
        
        """
        ...
    def checkAllowed(self, version: float, field: typing.Any, key: str, minVersion: float, maxVersion: float) -> None:
        """
        Complain if a key is not allowed.
        
        Parameters:
            version (double): format version
            field (Object): field to check
            key (String): key associated with the field
            minVersion (double): version at which key started to be allowed
            maxVersion (double): version at which key started to be forbidden
        
        
        """
        ...
    def checkNotNaN(self, field: float, key: str) -> None:
        """
        Complain if a field is NaN.
        
        Parameters:
            field (double): field to check
            key (String): key associated with the field
        
        
        """
        ...
    def checkNotNegative(self, field: int, key: str) -> None:
        """
        Complain if a field is negative.
        
        Parameters:
            field (int): field to check
            key (String): key associated with the field
        
        
        """
        ...
    def checkNotNull(self, field: typing.Any, key: str) -> None:
        """
        Complain if a field is null.
        
        Parameters:
            field (Object): field to check
            key (String): key associated with the field
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]:
        """
        Get the comments.
        
        Returns:
            comments
        
        
        """
        ...
    def refuseFurtherComments(self) -> None:
        """
        Set flag to refuse further comments.
        """
        ...
    def setComments(self, comments: java.util.List[str]) -> None:
        """
        Set the comments. This removes all previous comments and replaces them with the new ones.
        
        Parameters:
            comments (List<String> comments): List with new comments
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class Data(Section):
    """
    This marker interface represents segment data.
    
    Since:
        11.0
    """
    ...

class PythonAbstractWriter(AbstractWriter):
    def __init__(self, xmlTag: str, kvnTag: str):
        """
        Simple constructor.
        
        Parameters:
            xmlTag (String): name of the XML tag surrounding the section
            kvnTag (String): name of the KVN tag surrounding the section (may be null)
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def writeContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None:
        """
        Write the content of the section, excluding surrounding tags.
        
        Specified by: writeContent in class AbstractWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class PythonSection(Section):
    def __init__(self): ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class Header(CommentsContainer):
    """
    Header of a CCSDS Navigation Data Message.
    
    Since:
        10.2
    """
    def __init__(self, minVersionMessageId: float, minVersionClassification: float):
        """
        Constructor.
        
        Parameters:
            minVersionMessageId (double): minimum version for MESSAGE_ID
            minVersionClassification (double): minimum version for CLASSIFICATION
        
        
        """
        ...
    def getClassification(self) -> str:
        """
        Get the classification/caveats.
        
        Returns:
            classification/caveats.
        
        
        """
        ...
    def getCreationDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the message creation date and time in UTC.
        
        Returns:
            the message creation date and time in UTC.
        
        
        """
        ...
    def getFormatVersion(self) -> float:
        """
        Get the CCSDS NDM (ADM, ODM or TDM) format version.
        
        Returns:
            format version
        
        
        """
        ...
    def getMessageId(self) -> str:
        """
        Get the ID that uniquely identifies a message from a given originator.
        
        Returns:
            ID that uniquely identifies a message from a given originator
        
        
        """
        ...
    def getOriginator(self) -> str:
        """
        Get the message originator.
        
        Returns:
            originator the message originator.
        
        
        """
        ...
    def setClassification(self, classification: str) -> None:
        """
        Set the classification/caveats.
        
        Parameters:
            classification (String): classification/caveats to be set
        
        
        """
        ...
    def setCreationDate(self, creationDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the message creation date and time in UTC.
        
        Parameters:
            creationDate (AbsoluteDate): the creation date to be set
        
        
        """
        ...
    def setFormatVersion(self, formatVersion: float) -> None:
        """
        Set the CCSDS NDM (ADM, ODM or TDM) format version.
        
        Parameters:
            formatVersion (double): the format version to be set
        
        
        """
        ...
    def setMessageId(self, messageId: str) -> None:
        """
        Set the ID that uniquely identifies a message from a given originator.
        
        Parameters:
            messageId (String): ID that uniquely identifies a message from a given originator
        
        
        """
        ...
    def setOriginator(self, originator: str) -> None:
        """
        Set the message originator.
        
        Parameters:
            originator (String): the originator to be set
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class Metadata(CommentsContainer):
    """
    This class gathers the meta-data present in the Navigation Data Message (ADM, ODM and TDM).
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        11.0
    """
    def getTimeSystem(self) -> org.orekit.files.ccsds.definitions.TimeSystem:
        """
        Get the Time System that: for OPM, is used for metadata, state vector, maneuver and covariance data, for OMM, is used for metadata, orbit state and covariance data, for OEM, is used for metadata, ephemeris and covariance data.
        
        Returns:
            the time system
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.files.ccsds.definitions.TimeSystem) -> None:
        """
        Set the Time System that: for OPM, is used for metadata, state vector, maneuver and covariance data, for OMM, is used for metadata, orbit state and covariance data, for OEM, is used for metadata, ephemeris and covariance data.
        
        Parameters:
            timeSystem (TimeSystem): the time system to be set
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class PyhonData(Data):
    def __init__(self): ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Parameters:
            version (double): format version
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.section")``.

    AbstractWriter: typing.Type[AbstractWriter]
    CommentsContainer: typing.Type[CommentsContainer]
    Data: typing.Type[Data]
    Header: typing.Type[Header]
    HeaderKey: typing.Type[HeaderKey]
    HeaderProcessingState: typing.Type[HeaderProcessingState]
    KvnStructureKey: typing.Type[KvnStructureKey]
    KvnStructureProcessingState: typing.Type[KvnStructureProcessingState]
    Metadata: typing.Type[Metadata]
    MetadataKey: typing.Type[MetadataKey]
    PyhonData: typing.Type[PyhonData]
    PythonAbstractWriter: typing.Type[PythonAbstractWriter]
    PythonSection: typing.Type[PythonSection]
    Section: typing.Type[Section]
    Segment: typing.Type[Segment]
    XmlStructureKey: typing.Type[XmlStructureKey]
    XmlStructureProcessingState: typing.Type[XmlStructureProcessingState]
