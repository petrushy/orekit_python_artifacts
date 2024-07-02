import java.util
import org.orekit.data
import org.orekit.files.rinex.clock
import org.orekit.files.rinex.navigation
import org.orekit.files.rinex.observation
import org.orekit.files.rinex.section
import org.orekit.files.rinex.utils
import org.orekit.gnss
import typing



class AppliedDCBS:
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, string: str, string2: str): ...
    def getProgDCBS(self) -> str: ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem: ...
    def getSourceDCBS(self) -> str: ...

class AppliedPCVS:
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, string: str, string2: str): ...
    def getProgPCVS(self) -> str: ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem: ...
    def getSourcePCVS(self) -> str: ...

class HatanakaCompressFilter(org.orekit.data.DataFilter):
    def __init__(self): ...
    def filter(self, dataSource: org.orekit.data.DataSource) -> org.orekit.data.DataSource: ...

_RinexFile__T = typing.TypeVar('_RinexFile__T', bound=org.orekit.files.rinex.section.RinexBaseHeader)  # <T>
class RinexFile(typing.Generic[_RinexFile__T]):
    def addComment(self, rinexComment: org.orekit.files.rinex.section.RinexComment) -> None: ...
    def getComments(self) -> java.util.List[org.orekit.files.rinex.section.RinexComment]: ...
    def getHeader(self) -> _RinexFile__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex")``.

    AppliedDCBS: typing.Type[AppliedDCBS]
    AppliedPCVS: typing.Type[AppliedPCVS]
    HatanakaCompressFilter: typing.Type[HatanakaCompressFilter]
    RinexFile: typing.Type[RinexFile]
    clock: org.orekit.files.rinex.clock.__module_protocol__
    navigation: org.orekit.files.rinex.navigation.__module_protocol__
    observation: org.orekit.files.rinex.observation.__module_protocol__
    section: org.orekit.files.rinex.section.__module_protocol__
    utils: org.orekit.files.rinex.utils.__module_protocol__
