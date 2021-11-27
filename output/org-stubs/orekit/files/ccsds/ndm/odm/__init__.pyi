import java.lang
import java.util
import java.util.function
import org.hipparchus.linear
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm.ocm
import org.orekit.files.ccsds.ndm.odm.oem
import org.orekit.files.ccsds.ndm.odm.omm
import org.orekit.files.ccsds.ndm.odm.opm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.frames
import org.orekit.orbits
import org.orekit.time
import org.orekit.utils
import typing



class CartesianCovariance(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    def __init__(self, supplier: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.definitions.FrameFacade], typing.Callable[[], org.orekit.files.ccsds.definitions.FrameFacade]]): ...
    def getCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix: ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate: ...
    def getReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade: ...
    def setCovarianceMatrixEntry(self, int: int, int2: int, double: float) -> None: ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None: ...
    def validate(self, double: float) -> None: ...

class CartesianCovarianceKey(java.lang.Enum['CartesianCovarianceKey']):
    COMMENT: typing.ClassVar['CartesianCovarianceKey'] = ...
    EPOCH: typing.ClassVar['CartesianCovarianceKey'] = ...
    COV_REF_FRAME: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_X_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_X_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_Y_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_X_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Y_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Z_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, cartesianCovariance: CartesianCovariance) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CartesianCovarianceKey': ...
    @staticmethod
    def values() -> typing.List['CartesianCovarianceKey']: ...

class CartesianCovarianceWriter(org.orekit.files.ccsds.section.AbstractWriter):
    def __init__(self, string: str, string2: str, cartesianCovariance: CartesianCovariance): ...

class CommonMetadataKey(java.lang.Enum['CommonMetadataKey']):
    OBJECT_ID: typing.ClassVar['CommonMetadataKey'] = ...
    CENTER_NAME: typing.ClassVar['CommonMetadataKey'] = ...
    REF_FRAME: typing.ClassVar['CommonMetadataKey'] = ...
    REF_FRAME_EPOCH: typing.ClassVar['CommonMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, commonMetadata: 'CommonMetadata') -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CommonMetadataKey': ...
    @staticmethod
    def values() -> typing.List['CommonMetadataKey']: ...

class CommonMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    def __init__(self, commonMetadata: 'CommonMetadata', timeConverter: org.orekit.files.ccsds.definitions.TimeConverter): ...

class KeplerianElements(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    def __init__(self): ...
    def generateKeplerianOrbit(self, frame: org.orekit.frames.Frame) -> org.orekit.orbits.KeplerianOrbit: ...
    def getA(self) -> float: ...
    def getAnomaly(self) -> float: ...
    def getAnomalyType(self) -> org.orekit.orbits.PositionAngle: ...
    def getE(self) -> float: ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate: ...
    def getI(self) -> float: ...
    def getMeanMotion(self) -> float: ...
    def getMu(self) -> float: ...
    def getPa(self) -> float: ...
    def getRaan(self) -> float: ...
    def setA(self, double: float) -> None: ...
    def setAnomaly(self, double: float) -> None: ...
    def setAnomalyType(self, positionAngle: org.orekit.orbits.PositionAngle) -> None: ...
    def setE(self, double: float) -> None: ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setI(self, double: float) -> None: ...
    def setMeanMotion(self, double: float) -> None: ...
    def setMu(self, double: float) -> None: ...
    def setPa(self, double: float) -> None: ...
    def setRaan(self, double: float) -> None: ...
    def validate(self, double: float) -> None: ...

class KeplerianElementsKey(java.lang.Enum['KeplerianElementsKey']):
    COMMENT: typing.ClassVar['KeplerianElementsKey'] = ...
    EPOCH: typing.ClassVar['KeplerianElementsKey'] = ...
    SEMI_MAJOR_AXIS: typing.ClassVar['KeplerianElementsKey'] = ...
    MEAN_MOTION: typing.ClassVar['KeplerianElementsKey'] = ...
    ECCENTRICITY: typing.ClassVar['KeplerianElementsKey'] = ...
    INCLINATION: typing.ClassVar['KeplerianElementsKey'] = ...
    RA_OF_ASC_NODE: typing.ClassVar['KeplerianElementsKey'] = ...
    ARG_OF_PERICENTER: typing.ClassVar['KeplerianElementsKey'] = ...
    TRUE_ANOMALY: typing.ClassVar['KeplerianElementsKey'] = ...
    MEAN_ANOMALY: typing.ClassVar['KeplerianElementsKey'] = ...
    GM: typing.ClassVar['KeplerianElementsKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, keplerianElements: KeplerianElements) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'KeplerianElementsKey': ...
    @staticmethod
    def values() -> typing.List['KeplerianElementsKey']: ...

class OdmMetadata(org.orekit.files.ccsds.section.Metadata):
    def getObjectName(self) -> str: ...
    def setObjectName(self, string: str) -> None: ...

class OdmMetadataKey(java.lang.Enum['OdmMetadataKey']):
    OBJECT_NAME: typing.ClassVar['OdmMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, odmMetadata: OdmMetadata) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OdmMetadataKey': ...
    @staticmethod
    def values() -> typing.List['OdmMetadataKey']: ...

_OdmParser__T = typing.TypeVar('_OdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_OdmParser__P = typing.TypeVar('_OdmParser__P', bound='OdmParser')  # <P>
class OdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[_OdmParser__T, _OdmParser__P], typing.Generic[_OdmParser__T, _OdmParser__P]):
    def getMissionReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getSelectedMu(self) -> float: ...

class SpacecraftParameters(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    def __init__(self): ...
    def getDragArea(self) -> float: ...
    def getDragCoeff(self) -> float: ...
    def getMass(self) -> float: ...
    def getSolarRadArea(self) -> float: ...
    def getSolarRadCoeff(self) -> float: ...
    def setDragArea(self, double: float) -> None: ...
    def setDragCoeff(self, double: float) -> None: ...
    def setMass(self, double: float) -> None: ...
    def setSolarRadArea(self, double: float) -> None: ...
    def setSolarRadCoeff(self, double: float) -> None: ...
    def validate(self, double: float) -> None: ...

class SpacecraftParametersKey(java.lang.Enum['SpacecraftParametersKey']):
    COMMENT: typing.ClassVar['SpacecraftParametersKey'] = ...
    MASS: typing.ClassVar['SpacecraftParametersKey'] = ...
    SOLAR_RAD_AREA: typing.ClassVar['SpacecraftParametersKey'] = ...
    SOLAR_RAD_COEFF: typing.ClassVar['SpacecraftParametersKey'] = ...
    DRAG_AREA: typing.ClassVar['SpacecraftParametersKey'] = ...
    DRAG_COEFF: typing.ClassVar['SpacecraftParametersKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, spacecraftParameters: SpacecraftParameters) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SpacecraftParametersKey': ...
    @staticmethod
    def values() -> typing.List['SpacecraftParametersKey']: ...

class SpacecraftParametersWriter(org.orekit.files.ccsds.section.AbstractWriter):
    def __init__(self, string: str, string2: str, spacecraftParameters: SpacecraftParameters): ...

class StateVector(org.orekit.files.ccsds.section.CommentsContainer):
    def __init__(self): ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate: ...
    def hasAcceleration(self) -> bool: ...
    def setA(self, int: int, double: float) -> None: ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setP(self, int: int, double: float) -> None: ...
    def setV(self, int: int, double: float) -> None: ...
    def toTimeStampedPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def validate(self, double: float) -> None: ...

class StateVectorKey(java.lang.Enum['StateVectorKey']):
    COMMENT: typing.ClassVar['StateVectorKey'] = ...
    EPOCH: typing.ClassVar['StateVectorKey'] = ...
    X: typing.ClassVar['StateVectorKey'] = ...
    Y: typing.ClassVar['StateVectorKey'] = ...
    Z: typing.ClassVar['StateVectorKey'] = ...
    X_DOT: typing.ClassVar['StateVectorKey'] = ...
    Y_DOT: typing.ClassVar['StateVectorKey'] = ...
    Z_DOT: typing.ClassVar['StateVectorKey'] = ...
    X_DDOT: typing.ClassVar['StateVectorKey'] = ...
    Y_DDOT: typing.ClassVar['StateVectorKey'] = ...
    Z_DDOT: typing.ClassVar['StateVectorKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, stateVector: StateVector) -> bool: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'StateVectorKey': ...
    @staticmethod
    def values() -> typing.List['StateVectorKey']: ...

class StateVectorWriter(org.orekit.files.ccsds.section.AbstractWriter):
    def __init__(self, string: str, string2: str, stateVector: StateVector, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter): ...

class UserDefined(org.orekit.files.ccsds.section.CommentsContainer):
    USER_DEFINED_XML_TAG: typing.ClassVar[str] = ...
    USER_DEFINED_XML_ATTRIBUTE: typing.ClassVar[str] = ...
    USER_DEFINED_PREFIX: typing.ClassVar[str] = ...
    def __init__(self): ...
    def addEntry(self, string: str, string2: str) -> None: ...
    def getParameters(self) -> java.util.Map[str, str]: ...

class UserDefinedWriter(org.orekit.files.ccsds.section.AbstractWriter):
    def __init__(self, string: str, string2: str, userDefined: UserDefined): ...

class CommonMetadata(OdmMetadata):
    def __init__(self): ...
    def finalizeMetadata(self, contextBinding: org.orekit.files.ccsds.utils.ContextBinding) -> None: ...
    def getCenter(self) -> org.orekit.files.ccsds.definitions.BodyFacade: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getFrameEpoch(self) -> org.orekit.time.AbsoluteDate: ...
    def getLaunchNumber(self) -> int: ...
    def getLaunchPiece(self) -> str: ...
    def getLaunchYear(self) -> int: ...
    def getObjectID(self) -> str: ...
    def getReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade: ...
    def setCenter(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None: ...
    def setFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setFrameEpochString(self, string: str) -> None: ...
    def setObjectID(self, string: str) -> None: ...
    def setReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None: ...
    def validate(self, double: float) -> None: ...

_PythonOdmParser__T = typing.TypeVar('_PythonOdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonOdmParser__P = typing.TypeVar('_PythonOdmParser__P', bound=OdmParser)  # <P>
class PythonOdmParser(OdmParser[_PythonOdmParser__T, _PythonOdmParser__P], typing.Generic[_PythonOdmParser__T, _PythonOdmParser__P]):
    def build(self) -> _PythonOdmParser__T: ...
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm")``.

    CartesianCovariance: typing.Type[CartesianCovariance]
    CartesianCovarianceKey: typing.Type[CartesianCovarianceKey]
    CartesianCovarianceWriter: typing.Type[CartesianCovarianceWriter]
    CommonMetadata: typing.Type[CommonMetadata]
    CommonMetadataKey: typing.Type[CommonMetadataKey]
    CommonMetadataWriter: typing.Type[CommonMetadataWriter]
    KeplerianElements: typing.Type[KeplerianElements]
    KeplerianElementsKey: typing.Type[KeplerianElementsKey]
    OdmMetadata: typing.Type[OdmMetadata]
    OdmMetadataKey: typing.Type[OdmMetadataKey]
    OdmParser: typing.Type[OdmParser]
    PythonOdmParser: typing.Type[PythonOdmParser]
    SpacecraftParameters: typing.Type[SpacecraftParameters]
    SpacecraftParametersKey: typing.Type[SpacecraftParametersKey]
    SpacecraftParametersWriter: typing.Type[SpacecraftParametersWriter]
    StateVector: typing.Type[StateVector]
    StateVectorKey: typing.Type[StateVectorKey]
    StateVectorWriter: typing.Type[StateVectorWriter]
    UserDefined: typing.Type[UserDefined]
    UserDefinedWriter: typing.Type[UserDefinedWriter]
    ocm: org.orekit.files.ccsds.ndm.odm.ocm.__module_protocol__
    oem: org.orekit.files.ccsds.ndm.odm.oem.__module_protocol__
    omm: org.orekit.files.ccsds.ndm.odm.omm.__module_protocol__
    opm: org.orekit.files.ccsds.ndm.odm.opm.__module_protocol__
