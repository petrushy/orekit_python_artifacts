import java.io
import java.util
import org
import org.hipparchus
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.analytical.tle.generation
import org.orekit.time
import org.orekit.utils
import typing



_FieldTLE__T = typing.TypeVar('_FieldTLE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTLE(org.orekit.time.FieldTimeStamped[_FieldTLE__T], java.io.Serializable, org.orekit.utils.ParameterDriversProvider, typing.Generic[_FieldTLE__T]):
    DEFAULT: typing.ClassVar[int] = ...
    SGP: typing.ClassVar[int] = ...
    SGP4: typing.ClassVar[int] = ...
    SDP4: typing.ClassVar[int] = ...
    SGP8: typing.ClassVar[int] = ...
    SDP8: typing.ClassVar[int] = ...
    B_STAR: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLE__T], t: _FieldTLE__T, t2: _FieldTLE__T, t3: _FieldTLE__T, t4: _FieldTLE__T, t5: _FieldTLE__T, t6: _FieldTLE__T, t7: _FieldTLE__T, t8: _FieldTLE__T, int6: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLE__T], t: _FieldTLE__T, t2: _FieldTLE__T, t3: _FieldTLE__T, t4: _FieldTLE__T, t5: _FieldTLE__T, t6: _FieldTLE__T, t7: _FieldTLE__T, t8: _FieldTLE__T, int6: int, double: float, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTLE__T], string: str, string2: str): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTLE__T], string: str, string2: str, timeScale: org.orekit.time.TimeScale): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBStar(self) -> float: ...
    def getClassification(self) -> str: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTLE__T]: ...
    def getE(self) -> _FieldTLE__T: ...
    def getElementNumber(self) -> int: ...
    def getEphemerisType(self) -> int: ...
    def getI(self) -> _FieldTLE__T: ...
    def getLaunchNumber(self) -> int: ...
    def getLaunchPiece(self) -> str: ...
    def getLaunchYear(self) -> int: ...
    def getLine1(self) -> str: ...
    def getLine2(self) -> str: ...
    def getMeanAnomaly(self) -> _FieldTLE__T: ...
    def getMeanMotion(self) -> _FieldTLE__T: ...
    def getMeanMotionFirstDerivative(self) -> _FieldTLE__T: ...
    def getMeanMotionSecondDerivative(self) -> _FieldTLE__T: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPerigeeArgument(self) -> _FieldTLE__T: ...
    def getRaan(self) -> _FieldTLE__T: ...
    def getRevolutionNumberAtEpoch(self) -> int: ...
    def getSatelliteNumber(self) -> int: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def isFormatOK(string: str, string2: str) -> bool: ...
    _stateToTLE__T = typing.TypeVar('_stateToTLE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def stateToTLE(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_stateToTLE__T], fieldTLE: 'FieldTLE'[_stateToTLE__T], tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm) -> 'FieldTLE'[_stateToTLE__T]: ...
    def toString(self) -> str: ...
    def toTLE(self) -> 'TLE': ...

_FieldTLEPropagator__T = typing.TypeVar('_FieldTLEPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTLEPropagator(org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator[_FieldTLEPropagator__T], typing.Generic[_FieldTLEPropagator__T]):
    def getFrame(self) -> org.orekit.frames.Frame: ...
    @staticmethod
    def getMU() -> float: ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTLEPropagator__T]: ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], tArray: typing.List[_FieldTLEPropagator__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldTLEPropagator__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTLE(self) -> FieldTLE[_FieldTLEPropagator__T]: ...
    def propagateOrbit(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], tArray: typing.List[_FieldTLEPropagator__T]) -> org.orekit.orbits.FieldOrbit[_FieldTLEPropagator__T]: ...
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldTLEPropagator__T]) -> None: ...
    _selectExtrapolator_0__T = typing.TypeVar('_selectExtrapolator_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_1__T = typing.TypeVar('_selectExtrapolator_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_2__T = typing.TypeVar('_selectExtrapolator_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_3__T = typing.TypeVar('_selectExtrapolator_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_0__T], tArray: typing.List[_selectExtrapolator_0__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_0__T]: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_1__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _selectExtrapolator_1__T, tArray: typing.List[_selectExtrapolator_1__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_1__T]: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_2__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _selectExtrapolator_2__T, frame: org.orekit.frames.Frame, tArray: typing.List[_selectExtrapolator_2__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_2__T]: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_3__T], frame: org.orekit.frames.Frame, tArray: typing.List[_selectExtrapolator_3__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_3__T]: ...

class TLE(org.orekit.time.TimeStamped, java.io.Serializable, org.orekit.utils.ParameterDriversProvider):
    SGP: typing.ClassVar[int] = ...
    SGP4: typing.ClassVar[int] = ...
    SDP4: typing.ClassVar[int] = ...
    SGP8: typing.ClassVar[int] = ...
    SDP8: typing.ClassVar[int] = ...
    DEFAULT: typing.ClassVar[int] = ...
    B_STAR: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int6: int, double9: float): ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int6: int, double9: float, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, timeScale: org.orekit.time.TimeScale): ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def getBStar(self) -> float: ...
    @typing.overload
    def getBStar(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getClassification(self) -> str: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getE(self) -> float: ...
    def getElementNumber(self) -> int: ...
    def getEphemerisType(self) -> int: ...
    def getI(self) -> float: ...
    def getLaunchNumber(self) -> int: ...
    def getLaunchPiece(self) -> str: ...
    def getLaunchYear(self) -> int: ...
    def getLine1(self) -> str: ...
    def getLine2(self) -> str: ...
    def getMeanAnomaly(self) -> float: ...
    def getMeanMotion(self) -> float: ...
    def getMeanMotionFirstDerivative(self) -> float: ...
    def getMeanMotionSecondDerivative(self) -> float: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPerigeeArgument(self) -> float: ...
    def getRaan(self) -> float: ...
    def getRevolutionNumberAtEpoch(self) -> int: ...
    def getSatelliteNumber(self) -> int: ...
    def getUtc(self) -> org.orekit.time.TimeScale: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def isFormatOK(string: str, string2: str) -> bool: ...
    @staticmethod
    def stateToTLE(spacecraftState: org.orekit.propagation.SpacecraftState, tLE: 'TLE', tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm) -> 'TLE': ...
    def toString(self) -> str: ...

class TLEConstants:
    ONE_THIRD: typing.ClassVar[float] = ...
    TWO_THIRD: typing.ClassVar[float] = ...
    EARTH_RADIUS: typing.ClassVar[float] = ...
    NORMALIZED_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    MINUTES_PER_DAY: typing.ClassVar[float] = ...
    XKE: typing.ClassVar[float] = ...
    XJ3: typing.ClassVar[float] = ...
    XJ2: typing.ClassVar[float] = ...
    XJ4: typing.ClassVar[float] = ...
    CK2: typing.ClassVar[float] = ...
    CK4: typing.ClassVar[float] = ...
    S: typing.ClassVar[float] = ...
    QOMS2T: typing.ClassVar[float] = ...
    A3OVK2: typing.ClassVar[float] = ...
    ZNS: typing.ClassVar[float] = ...
    ZES: typing.ClassVar[float] = ...
    ZNL: typing.ClassVar[float] = ...
    ZEL: typing.ClassVar[float] = ...
    THDT: typing.ClassVar[float] = ...
    C1SS: typing.ClassVar[float] = ...
    C1L: typing.ClassVar[float] = ...
    ROOT22: typing.ClassVar[float] = ...
    ROOT32: typing.ClassVar[float] = ...
    ROOT44: typing.ClassVar[float] = ...
    ROOT52: typing.ClassVar[float] = ...
    ROOT54: typing.ClassVar[float] = ...
    Q22: typing.ClassVar[float] = ...
    Q31: typing.ClassVar[float] = ...
    Q33: typing.ClassVar[float] = ...
    C_FASX2: typing.ClassVar[float] = ...
    S_FASX2: typing.ClassVar[float] = ...
    C_2FASX4: typing.ClassVar[float] = ...
    S_2FASX4: typing.ClassVar[float] = ...
    C_3FASX6: typing.ClassVar[float] = ...
    S_3FASX6: typing.ClassVar[float] = ...
    C_G22: typing.ClassVar[float] = ...
    S_G22: typing.ClassVar[float] = ...
    C_G32: typing.ClassVar[float] = ...
    S_G32: typing.ClassVar[float] = ...
    C_G44: typing.ClassVar[float] = ...
    S_G44: typing.ClassVar[float] = ...
    C_G52: typing.ClassVar[float] = ...
    S_G52: typing.ClassVar[float] = ...
    C_G54: typing.ClassVar[float] = ...
    S_G54: typing.ClassVar[float] = ...
    MU: typing.ClassVar[float] = ...

class TLEPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator):
    @staticmethod
    def getDefaultTleGenerationAlgorithm(timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame) -> org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    @staticmethod
    def getMU() -> float: ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates: ...
    def getTLE(self) -> TLE: ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE) -> 'TLEPropagator': ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float) -> 'TLEPropagator': ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame) -> 'TLEPropagator': ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE, frame: org.orekit.frames.Frame) -> 'TLEPropagator': ...

_FieldSGP4__T = typing.TypeVar('_FieldSGP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSGP4(FieldTLEPropagator[_FieldSGP4__T], typing.Generic[_FieldSGP4__T]):
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldSGP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldSGP4__T, tArray: typing.List[_FieldSGP4__T]): ...
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldSGP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldSGP4__T, frame: org.orekit.frames.Frame, tArray: typing.List[_FieldSGP4__T]): ...

class PythonTLEPropagator(TLEPropagator):
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def sxpInitialize(self) -> None: ...
    def sxpPropagate(self, double: float) -> None: ...

class SGP4(TLEPropagator):
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...

class DeepSDP4(org.orekit.propagation.analytical.tle.SDP4):
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...

_FieldDeepSDP4__T = typing.TypeVar('_FieldDeepSDP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDeepSDP4(org.orekit.propagation.analytical.tle.FieldSDP4[_FieldDeepSDP4__T], typing.Generic[_FieldDeepSDP4__T]):
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldDeepSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldDeepSDP4__T, tArray: typing.List[_FieldDeepSDP4__T]): ...
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldDeepSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldDeepSDP4__T, frame: org.orekit.frames.Frame, tArray: typing.List[_FieldDeepSDP4__T]): ...

_PythonFieldSDP4__T = typing.TypeVar('_PythonFieldSDP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldSDP4(org.orekit.propagation.analytical.tle.FieldSDP4[_PythonFieldSDP4__T], typing.Generic[_PythonFieldSDP4__T]):
    def __init__(self, fieldTLE: FieldTLE[_PythonFieldSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _PythonFieldSDP4__T, frame: org.orekit.frames.Frame, tArray: typing.List[_PythonFieldSDP4__T]): ...
    def deepPeriodicEffects(self, t: _PythonFieldSDP4__T) -> None: ...
    def deepSecularEffects(self, t: _PythonFieldSDP4__T) -> None: ...
    def finalize(self) -> None: ...
    def luniSolarTermsComputation(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class FieldSDP4: ...

class SDP4: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.tle")``.

    DeepSDP4: typing.Type[DeepSDP4]
    FieldDeepSDP4: typing.Type[FieldDeepSDP4]
    FieldSDP4: typing.Type[FieldSDP4]
    FieldSGP4: typing.Type[FieldSGP4]
    FieldTLE: typing.Type[FieldTLE]
    FieldTLEPropagator: typing.Type[FieldTLEPropagator]
    PythonFieldSDP4: typing.Type[PythonFieldSDP4]
    PythonTLEPropagator: typing.Type[PythonTLEPropagator]
    SDP4: typing.Type[SDP4]
    SGP4: typing.Type[SGP4]
    TLE: typing.Type[TLE]
    TLEConstants: typing.Type[TLEConstants]
    TLEPropagator: typing.Type[TLEPropagator]
    generation: org.orekit.propagation.analytical.tle.generation.__module_protocol__
