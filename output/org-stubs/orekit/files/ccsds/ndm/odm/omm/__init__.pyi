import java.lang
import java.util
import org.orekit.data
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical.tle
import org.orekit.time
import org.orekit.utils
import typing



class Omm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment['OmmMetadata', 'OmmData']], org.orekit.time.TimeStamped):
    ROOT: typing.ClassVar[str] = ...
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    def __init__(self, header: org.orekit.files.ccsds.section.Header, list: java.util.List[org.orekit.files.ccsds.section.Segment['OmmMetadata', 'OmmData']], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...
    def generateKeplerianOrbit(self) -> org.orekit.orbits.KeplerianOrbit: ...
    def generateSpacecraftState(self) -> org.orekit.propagation.SpacecraftState: ...
    def generateTLE(self) -> org.orekit.propagation.analytical.tle.TLE: ...
    def getData(self) -> 'OmmData': ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMetadata(self) -> 'OmmMetadata': ...

class OmmData(org.orekit.files.ccsds.section.Data):
    def __init__(self, keplerianElements: org.orekit.files.ccsds.ndm.odm.KeplerianElements, spacecraftParameters: org.orekit.files.ccsds.ndm.odm.SpacecraftParameters, ommTle: 'OmmTle', cartesianCovariance: org.orekit.files.ccsds.ndm.odm.CartesianCovariance, userDefined: org.orekit.files.ccsds.ndm.odm.UserDefined, double: float): ...
    def getCovarianceBlock(self) -> org.orekit.files.ccsds.ndm.odm.CartesianCovariance: ...
    def getKeplerianElementsBlock(self) -> org.orekit.files.ccsds.ndm.odm.KeplerianElements: ...
    def getMass(self) -> float: ...
    def getSpacecraftParametersBlock(self) -> org.orekit.files.ccsds.ndm.odm.SpacecraftParameters: ...
    def getTLEBlock(self) -> 'OmmTle': ...
    def getUserDefinedBlock(self) -> org.orekit.files.ccsds.ndm.odm.UserDefined: ...
    def validate(self, double: float) -> None: ...

class OmmMetadata(org.orekit.files.ccsds.ndm.odm.CommonMetadata):
    SGP_SGP4_THEORY: typing.ClassVar[str] = ...
    DSST_THEORY: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getMeanElementTheory(self) -> str: ...
    def setMeanElementTheory(self, string: str) -> None: ...
    def theoryIsSgpSdp(self) -> bool: ...

class OmmMetadataKey(java.lang.Enum['OmmMetadataKey']):
    MEAN_ELEMENT_THEORY: typing.ClassVar['OmmMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, ommMetadata: OmmMetadata) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OmmMetadataKey': ...
    @staticmethod
    def values() -> typing.List['OmmMetadataKey']: ...

class OmmParser(org.orekit.files.ccsds.ndm.odm.OdmParser[Omm, 'OmmParser']):
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior): ...
    def build(self) -> Omm: ...
    def finalizeData(self) -> bool: ...
    def finalizeHeader(self) -> bool: ...
    def finalizeMetadata(self) -> bool: ...
    def getHeader(self) -> org.orekit.files.ccsds.section.Header: ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]: ...
    def inData(self) -> bool: ...
    def inHeader(self) -> bool: ...
    def inMetadata(self) -> bool: ...
    def prepareData(self) -> bool: ...
    def prepareHeader(self) -> bool: ...
    def prepareMetadata(self) -> bool: ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None: ...

class OmmTle(org.orekit.files.ccsds.section.CommentsContainer):
    def __init__(self): ...
    def getBStar(self) -> float: ...
    def getClassificationType(self) -> str: ...
    def getElementSetNumber(self) -> int: ...
    def getEphemerisType(self) -> int: ...
    def getMeanMotionDot(self) -> float: ...
    def getMeanMotionDotDot(self) -> float: ...
    def getNoradID(self) -> int: ...
    def getRevAtEpoch(self) -> int: ...
    def setBStar(self, double: float) -> None: ...
    def setClassificationType(self, char: str) -> None: ...
    def setElementSetNo(self, int: int) -> None: ...
    def setEphemerisType(self, int: int) -> None: ...
    def setMeanMotionDot(self, double: float) -> None: ...
    def setMeanMotionDotDot(self, double: float) -> None: ...
    def setNoradID(self, int: int) -> None: ...
    def setRevAtEpoch(self, int: int) -> None: ...
    def validate(self, double: float) -> None: ...

class OmmTleKey(java.lang.Enum['OmmTleKey']):
    EPHEMERIS_TYPE: typing.ClassVar['OmmTleKey'] = ...
    CLASSIFICATION_TYPE: typing.ClassVar['OmmTleKey'] = ...
    NORAD_CAT_ID: typing.ClassVar['OmmTleKey'] = ...
    ELEMENT_SET_NO: typing.ClassVar['OmmTleKey'] = ...
    REV_AT_EPOCH: typing.ClassVar['OmmTleKey'] = ...
    BSTAR: typing.ClassVar['OmmTleKey'] = ...
    MEAN_MOTION_DOT: typing.ClassVar['OmmTleKey'] = ...
    MEAN_MOTION_DDOT: typing.ClassVar['OmmTleKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, ommTle: OmmTle) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OmmTleKey': ...
    @staticmethod
    def values() -> typing.List['OmmTleKey']: ...

class OmmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment[OmmMetadata, OmmData], Omm]):
    CCSDS_OMM_VERS: typing.ClassVar[float] = ...
    KVN_PADDING_WIDTH: typing.ClassVar[int] = ...
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, segment: org.orekit.files.ccsds.section.Segment[OmmMetadata, OmmData]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm.omm")``.

    Omm: typing.Type[Omm]
    OmmData: typing.Type[OmmData]
    OmmMetadata: typing.Type[OmmMetadata]
    OmmMetadataKey: typing.Type[OmmMetadataKey]
    OmmParser: typing.Type[OmmParser]
    OmmTle: typing.Type[OmmTle]
    OmmTleKey: typing.Type[OmmTleKey]
    OmmWriter: typing.Type[OmmWriter]
