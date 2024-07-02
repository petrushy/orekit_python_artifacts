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
    def enterSection(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None: ...
    def exitSection(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None: ...
    def write(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None: ...

class HeaderKey(java.lang.Enum['HeaderKey']):
    COMMENT: typing.ClassVar['HeaderKey'] = ...
    CLASSIFICATION: typing.ClassVar['HeaderKey'] = ...
    CREATION_DATE: typing.ClassVar['HeaderKey'] = ...
    ORIGINATOR: typing.ClassVar['HeaderKey'] = ...
    MESSAGE_ID: typing.ClassVar['HeaderKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, header: 'Header') -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'HeaderKey': ...
    @staticmethod
    def values() -> typing.List['HeaderKey']: ...

class HeaderProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    def __init__(self, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool: ...

class KvnStructureKey(java.lang.Enum['KvnStructureKey']):
    META: typing.ClassVar['KvnStructureKey'] = ...
    DATA: typing.ClassVar['KvnStructureKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'KvnStructureKey': ...
    @staticmethod
    def values() -> typing.List['KvnStructureKey']: ...

class KvnStructureProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    def __init__(self, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool: ...

class MetadataKey(java.lang.Enum['MetadataKey']):
    COMMENT: typing.ClassVar['MetadataKey'] = ...
    TIME_SYSTEM: typing.ClassVar['MetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, metadata: 'Metadata') -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'MetadataKey': ...
    @staticmethod
    def values() -> typing.List['MetadataKey']: ...

class Section:
    def validate(self, double: float) -> None: ...

_Segment__M = typing.TypeVar('_Segment__M', bound='Metadata')  # <M>
_Segment__D = typing.TypeVar('_Segment__D', bound='Data')  # <D>
class Segment(typing.Generic[_Segment__M, _Segment__D]):
    def __init__(self, m: _Segment__M, d: _Segment__D): ...
    def getData(self) -> _Segment__D: ...
    def getMetadata(self) -> _Segment__M: ...
    def setMetadata(self, m: _Segment__M) -> None: ...

class XmlStructureKey(java.lang.Enum['XmlStructureKey']):
    body: typing.ClassVar['XmlStructureKey'] = ...
    segment: typing.ClassVar['XmlStructureKey'] = ...
    header: typing.ClassVar['XmlStructureKey'] = ...
    metadata: typing.ClassVar['XmlStructureKey'] = ...
    data: typing.ClassVar['XmlStructureKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'XmlStructureKey': ...
    @staticmethod
    def values() -> typing.List['XmlStructureKey']: ...

class XmlStructureProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    def __init__(self, string: str, abstractConstituentParser: org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[typing.Any, typing.Any, typing.Any]): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool: ...

class CommentsContainer(Section):
    def __init__(self): ...
    def acceptComments(self) -> bool: ...
    def addComment(self, string: str) -> bool: ...
    def checkAllowed(self, double: float, object: typing.Any, string: str, double2: float, double3: float) -> None: ...
    def checkNotNaN(self, double: float, string: str) -> None: ...
    def checkNotNegative(self, int: int, string: str) -> None: ...
    def checkNotNull(self, object: typing.Any, string: str) -> None: ...
    def getComments(self) -> java.util.List[str]: ...
    def refuseFurtherComments(self) -> None: ...
    def setComments(self, list: java.util.List[str]) -> None: ...
    def validate(self, double: float) -> None: ...

class Data(Section): ...

class PythonAbstractWriter(AbstractWriter):
    def __init__(self, string: str, string2: str): ...
    def finalize(self) -> None: ...
    def intArrayToString(self, intArray: typing.List[int]) -> str: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def writeContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None: ...

class PythonSection(Section):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def validate(self, double: float) -> None: ...

class Header(CommentsContainer):
    def __init__(self, double: float, double2: float): ...
    def getClassification(self) -> str: ...
    def getCreationDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getFormatVersion(self) -> float: ...
    def getMessageId(self) -> str: ...
    def getOriginator(self) -> str: ...
    def setClassification(self, string: str) -> None: ...
    def setCreationDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setFormatVersion(self, double: float) -> None: ...
    def setMessageId(self, string: str) -> None: ...
    def setOriginator(self, string: str) -> None: ...
    def validate(self, double: float) -> None: ...

class Metadata(CommentsContainer):
    def getTimeSystem(self) -> org.orekit.files.ccsds.definitions.TimeSystem: ...
    def setTimeSystem(self, timeSystem: org.orekit.files.ccsds.definitions.TimeSystem) -> None: ...
    def validate(self, double: float) -> None: ...


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
    PythonAbstractWriter: typing.Type[PythonAbstractWriter]
    PythonSection: typing.Type[PythonSection]
    Section: typing.Type[Section]
    Segment: typing.Type[Segment]
    XmlStructureKey: typing.Type[XmlStructureKey]
    XmlStructureProcessingState: typing.Type[XmlStructureProcessingState]
