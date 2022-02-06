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
    public abstract class AbstractWriter extends Object
    
        Top level class for writing CCSDS message sections.
    
        Since:
            11.0
    """
    def write(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None: ...

class HeaderKey(java.lang.Enum['HeaderKey']):
    """
    public enum HeaderKey extends Enum<:class:`~org.orekit.files.ccsds.section.HeaderKey`>
    
        Keywords allowed in :class:`~org.orekit.files.ccsds.section.Header`.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['HeaderKey'] = ...
    CREATION_DATE: typing.ClassVar['HeaderKey'] = ...
    ORIGINATOR: typing.ClassVar['HeaderKey'] = ...
    MESSAGE_ID: typing.ClassVar['HeaderKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, header: 'Header') -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                header (:class:`~org.orekit.files.ccsds.section.Header`): header to fill
        
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
    def valueOf(string: str) -> 'HeaderKey':
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
    def values() -> typing.List['HeaderKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (HeaderKey c : HeaderKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class HeaderProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    public class HeaderProcessingState extends Object implements :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
    
        :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState` for :class:`~org.orekit.files.ccsds.section.Header`.
    
        Since:
            11.0
    """
    def __init__(self, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any]): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
            Process one token.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.ProcessingState.processToken`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
            Returns:
                true if token was processed, false otherwise
        
        
        """
        ...

class KvnStructureKey(java.lang.Enum['KvnStructureKey']):
    """
    public enum KvnStructureKey extends Enum<:class:`~org.orekit.files.ccsds.section.KvnStructureKey`>
    
        Keys for :meth:`~org.orekit.files.ccsds.utils.FileFormat.KVN` format structure.
    
        Since:
            11.0
    """
    META: typing.ClassVar['KvnStructureKey'] = ...
    DATA: typing.ClassVar['KvnStructureKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any]) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                parser (:class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<?,?> parser): file parser
        
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
    def valueOf(string: str) -> 'KvnStructureKey':
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
    def values() -> typing.List['KvnStructureKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (KvnStructureKey c : KvnStructureKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class KvnStructureProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    public class KvnStructureProcessingState extends Object implements :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
    
        :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState` for structure of
        :meth:`~org.orekit.files.ccsds.utils.FileFormat.KVN` CCSDS Messages.
    
        Since:
            11.0
    """
    def __init__(self, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any]): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
            Process one token.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.ProcessingState.processToken`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
            Returns:
                true if token was processed, false otherwise
        
        
        """
        ...

class MetadataKey(java.lang.Enum['MetadataKey']):
    """
    public enum MetadataKey extends Enum<:class:`~org.orekit.files.ccsds.section.MetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.section.Metadata` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['MetadataKey'] = ...
    TIME_SYSTEM: typing.ClassVar['MetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, metadata: 'Metadata') -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                metadata (:class:`~org.orekit.files.ccsds.section.Metadata`): metadata to fill
        
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
    def valueOf(string: str) -> 'MetadataKey':
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
    def values() -> typing.List['MetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (MetadataKey c : MetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Section:
    """
    public interface Section
    
        Top level interface for all CCSDS message sections.
    
        Since:
            11.0
    """
    def validate(self, double: float) -> None:
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
    public class Segment<M extends :class:`~org.orekit.files.ccsds.section.Metadata`,D extends :class:`~org.orekit.files.ccsds.section.Data`> extends Object
    
        NDM segments are (:class:`~org.orekit.files.ccsds.section.Metadata`, :class:`~org.orekit.files.ccsds.section.Data`)
        pairs.
    
        Since:
            11.0
    """
    def __init__(self, m: _Segment__M, d: _Segment__D): ...
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

class XmlStructureKey(java.lang.Enum['XmlStructureKey']):
    """
    public enum XmlStructureKey extends Enum<:class:`~org.orekit.files.ccsds.section.XmlStructureKey`>
    
        Keys for :meth:`~org.orekit.files.ccsds.utils.FileFormat.XML` format structure.
    
        Since:
            11.0
    """
    body: typing.ClassVar['XmlStructureKey'] = ...
    segment: typing.ClassVar['XmlStructureKey'] = ...
    header: typing.ClassVar['XmlStructureKey'] = ...
    metadata: typing.ClassVar['XmlStructureKey'] = ...
    data: typing.ClassVar['XmlStructureKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any]) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                parser (:class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<?,?> parser): file parser
        
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
    def valueOf(string: str) -> 'XmlStructureKey':
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
    def values() -> typing.List['XmlStructureKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (XmlStructureKey c : XmlStructureKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class XmlStructureProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    public class XmlStructureProcessingState extends Object implements :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
    
        :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState` for structure of
        :meth:`~org.orekit.files.ccsds.utils.FileFormat.XML` CCSDS Messages.
    
        Since:
            11.0
    """
    def __init__(self, string: str, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any]): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
            Process one token.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.ProcessingState.processToken`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
            Returns:
                true if token was processed, false otherwise
        
        
        """
        ...

class CommentsContainer(Section):
    """
    public class CommentsContainer extends Object implements :class:`~org.orekit.files.ccsds.section.Section`
    
        Container for comments in various CCSDS messages.
    
        CCSDS files accept comments only at the beginning of sections. Once header/metadata/data content has started, comments
        in the corresponding section are refused.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def acceptComments(self) -> bool:
        """
            Check if container is still accepting comments.
        
            A container that still accept comments does not contain any other data.
        
            Returns:
                true if container is still accepting comments
        
        
        """
        ...
    def addComment(self, string: str) -> bool:
        """
            Add comment.
        
            Comments are accepted only at start. Once other content is stored in the same section, comments are refused.
        
            Parameters:
                comment (String): comment line
        
            Returns:
                true if comment was accepted
        
        
        """
        ...
    def checkAllowed(self, double: float, object: typing.Any, enum: java.lang.Enum[typing.Any], double2: float, double3: float) -> None:
        """
            Complain if a key is not allowed.
        
            Parameters:
                version (double): format version
                field (Object): field to check
                key (Enum<?> key): key associated with the field
                minVersion (double): version at which key started to be allowed
                maxVersion (double): version at which key started to be forbidden
        
        
        """
        ...
    def checkNotNaN(self, double: float, enum: java.lang.Enum[typing.Any]) -> None:
        """
            Complain if a field is NaN.
        
            Parameters:
                field (double): field to check
                key (Enum<?> key): key associated with the field
        
        
        """
        ...
    def checkNotNegative(self, int: int, enum: java.lang.Enum[typing.Any]) -> None:
        """
            Complain if a field is negative.
        
            Parameters:
                field (int): field to check
                key (Enum<?> key): key associated with the field
        
        
        """
        ...
    def checkNotNull(self, object: typing.Any, enum: java.lang.Enum[typing.Any]) -> None:
        """
            Complain if a field is null.
        
            Parameters:
                field (Object): field to check
                key (Enum<?> key): key associated with the field
        
        
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
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class Data(Section):
    """
    public interface Data extends :class:`~org.orekit.files.ccsds.section.Section`
    
        This marker interface represents segment data.
    
        Since:
            11.0
    """
    ...

class PythonAbstractWriter(AbstractWriter):
    """
    public class PythonAbstractWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    """
    def __init__(self, string: str, string2: str): ...
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
    def writeContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None: ...

class PythonSection(Section):
    """
    public class PythonSection extends Object implements :class:`~org.orekit.files.ccsds.section.Section`
    """
    def __init__(self): ...
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
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class Header(CommentsContainer):
    """
    public class Header extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Header of a CCSDS Navigation Data Message.
    
        Since:
            10.2
    """
    def __init__(self, double: float): ...
    def getCreationDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the file creation date and time in UTC.
        
            Returns:
                the file creation date and time in UTC.
        
        
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
            Get the file originator.
        
            Returns:
                originator the file originator.
        
        
        """
        ...
    def setCreationDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the file creation date and time in UTC.
        
            Parameters:
                creationDate (:class:`~org.orekit.time.AbsoluteDate`): the creation date to be set
        
        
        """
        ...
    def setFormatVersion(self, double: float) -> None:
        """
            Set the CCSDS NDM (ADM, ODM or TDM) format version.
        
            Parameters:
                formatVersion (double): the format version to be set
        
        
        """
        ...
    def setMessageId(self, string: str) -> None:
        """
            Set the ID that uniquely identifies a message from a given originator.
        
            Parameters:
                messageId (String): ID that uniquely identifies a message from a given originator
        
        
        """
        ...
    def setOriginator(self, string: str) -> None:
        """
            Set the file originator.
        
            Parameters:
                originator (String): the originator to be set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class Metadata(CommentsContainer):
    """
    public class Metadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        This class gathers the meta-data present in the Navigation Data Message (ADM, ODM and TDM).
    
        Since:
            11.0
    """
    def getTimeSystem(self) -> org.orekit.files.ccsds.definitions.TimeSystem:
        """
            Get the Time System that: for OPM, is used for metadata, state vector, maneuver and covariance data, for OMM, is used
            for metadata, orbit state and covariance data, for OEM, is used for metadata, ephemeris and covariance data.
        
            Returns:
                the time system
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.files.ccsds.definitions.TimeSystem) -> None:
        """
            Set the Time System that: for OPM, is used for metadata, state vector, maneuver and covariance data, for OMM, is used
            for metadata, orbit state and covariance data, for OEM, is used for metadata, ephemeris and covariance data.
        
            Parameters:
                timeSystem (:class:`~org.orekit.files.ccsds.definitions.TimeSystem`): the time system to be set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class PyhonData(Data):
    """
    public class PyhonData extends Object implements :class:`~org.orekit.files.ccsds.section.Data`
    """
    def __init__(self): ...
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
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Parameters:
                version (double): format version
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
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
