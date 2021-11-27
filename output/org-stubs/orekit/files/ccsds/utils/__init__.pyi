import java.lang
import java.util.function
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.time
import org.orekit.utils
import typing



class ContextBinding:
    def __init__(self, supplier: typing.Union[java.util.function.Supplier[org.orekit.utils.IERSConventions], typing.Callable[[], org.orekit.utils.IERSConventions]], booleanSupplier: typing.Union[java.util.function.BooleanSupplier, typing.Callable], supplier2: typing.Union[java.util.function.Supplier[org.orekit.data.DataContext], typing.Callable[[], org.orekit.data.DataContext]], supplier3: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.ndm.ParsedUnitsBehavior], typing.Callable[[], org.orekit.files.ccsds.ndm.ParsedUnitsBehavior]], supplier4: typing.Union[java.util.function.Supplier[org.orekit.time.AbsoluteDate], typing.Callable[[], org.orekit.time.AbsoluteDate]], supplier5: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.definitions.TimeSystem], typing.Callable[[], org.orekit.files.ccsds.definitions.TimeSystem]], doubleSupplier: typing.Union[java.util.function.DoubleSupplier, typing.Callable], doubleSupplier2: typing.Union[java.util.function.DoubleSupplier, typing.Callable]): ...
    def getClockCount(self) -> float: ...
    def getClockRate(self) -> float: ...
    def getConventions(self) -> org.orekit.utils.IERSConventions: ...
    def getDataContext(self) -> org.orekit.data.DataContext: ...
    def getParsedUnitsBehavior(self) -> org.orekit.files.ccsds.ndm.ParsedUnitsBehavior: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getTimeSystem(self) -> org.orekit.files.ccsds.definitions.TimeSystem: ...
    def isSimpleEOP(self) -> bool: ...

class FileFormat(java.lang.Enum['FileFormat']):
    KVN: typing.ClassVar['FileFormat'] = ...
    XML: typing.ClassVar['FileFormat'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'FileFormat': ...
    @staticmethod
    def values() -> typing.List['FileFormat']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils")``.

    ContextBinding: typing.Type[ContextBinding]
    FileFormat: typing.Type[FileFormat]
    generation: org.orekit.files.ccsds.utils.generation.__module_protocol__
    lexical: org.orekit.files.ccsds.utils.lexical.__module_protocol__
    parsing: org.orekit.files.ccsds.utils.parsing.__module_protocol__
