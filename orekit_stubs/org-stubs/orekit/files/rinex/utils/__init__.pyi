import java.lang
import org.orekit.files.rinex.utils.parsing
import typing



class RinexFileType(java.lang.Enum['RinexFileType']):
    OBSERVATION: typing.ClassVar['RinexFileType'] = ...
    NAVIGATION: typing.ClassVar['RinexFileType'] = ...
    @staticmethod
    def parseRinexFileType(string: str) -> 'RinexFileType': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RinexFileType': ...
    @staticmethod
    def values() -> typing.List['RinexFileType']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.utils")``.

    RinexFileType: typing.Type[RinexFileType]
    parsing: org.orekit.files.rinex.utils.parsing.__module_protocol__
