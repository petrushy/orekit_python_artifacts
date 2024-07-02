import java.io
import java.lang
import java.util
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.hipparchus.random
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.generation
import org.orekit.files.rinex.observation
import org.orekit.gnss
import org.orekit.propagation
import org.orekit.propagation.sampling
import org.orekit.time
import org.orekit.utils
import typing



_AbstractOnBoardMeasurement__T = typing.TypeVar('_AbstractOnBoardMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractOnBoardMeasurement(org.orekit.estimation.measurements.AbstractMeasurement[_AbstractOnBoardMeasurement__T], typing.Generic[_AbstractOnBoardMeasurement__T]):
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, list: java.util.List[org.orekit.estimation.measurements.ObservableSatellite]): ...

_AbstractWindUp__T = typing.TypeVar('_AbstractWindUp__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractWindUp(org.orekit.estimation.measurements.EstimationModifier[_AbstractWindUp__T], typing.Generic[_AbstractWindUp__T]):
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modifyWithoutDerivatives(self, estimatedMeasurementBase: org.orekit.estimation.measurements.EstimatedMeasurementBase[_AbstractWindUp__T]) -> None: ...

class AmbiguityAcceptance:
    def accept(self, integerLeastSquareSolutionArray: typing.List['IntegerLeastSquareSolution']) -> 'IntegerLeastSquareSolution': ...
    def numberOfCandidates(self) -> int: ...

class AmbiguityCache:
    DEFAULT_CACHE: typing.ClassVar['AmbiguityCache'] = ...
    def __init__(self): ...
    def getAmbiguity(self, string: str, string2: str, double: float) -> 'AmbiguityDriver': ...

class AmbiguityDriver(org.orekit.utils.ParameterDriver):
    PREFIX: typing.ClassVar[str] = ...
    def __init__(self, string: str, string2: str, double: float): ...
    def getEmitter(self) -> str: ...
    def getReceiver(self) -> str: ...
    def getWavelength(self) -> float: ...

class AmbiguitySolver:
    def __init__(self, list: java.util.List[org.orekit.utils.ParameterDriver], integerLeastSquareSolver: 'IntegerLeastSquareSolver', ambiguityAcceptance: AmbiguityAcceptance): ...
    def fixIntegerAmbiguities(self, int: int, list: java.util.List[org.orekit.utils.ParameterDriver], realMatrix: org.hipparchus.linear.RealMatrix) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getAllAmbiguityDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def unFixAmbiguity(self, parameterDriver: org.orekit.utils.ParameterDriver) -> None: ...

class CombinationType(java.lang.Enum['CombinationType']):
    PHASE_MINUS_CODE: typing.ClassVar['CombinationType'] = ...
    GRAPHIC: typing.ClassVar['CombinationType'] = ...
    GEOMETRY_FREE: typing.ClassVar['CombinationType'] = ...
    IONO_FREE: typing.ClassVar['CombinationType'] = ...
    NARROW_LANE: typing.ClassVar['CombinationType'] = ...
    WIDE_LANE: typing.ClassVar['CombinationType'] = ...
    MELBOURNE_WUBBENA: typing.ClassVar['CombinationType'] = ...
    def getName(self) -> str: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CombinationType': ...
    @staticmethod
    def values() -> typing.List['CombinationType']: ...

class CombinedObservationData:
    @typing.overload
    def __init__(self, double: float, double2: float, combinationType: CombinationType, measurementType: org.orekit.gnss.MeasurementType, list: java.util.List[org.orekit.files.rinex.observation.ObservationData]): ...
    @typing.overload
    def __init__(self, combinationType: CombinationType, measurementType: org.orekit.gnss.MeasurementType, double: float, double2: float, list: java.util.List[org.orekit.files.rinex.observation.ObservationData]): ...
    def getCombinationType(self) -> CombinationType: ...
    def getCombinedFrequency(self) -> float: ...
    def getCombinedMHzFrequency(self) -> float: ...
    def getMeasurementType(self) -> org.orekit.gnss.MeasurementType: ...
    def getUsedObservationData(self) -> java.util.List[org.orekit.files.rinex.observation.ObservationData]: ...
    def getValue(self) -> float: ...

class CombinedObservationDataSet(org.orekit.time.TimeStamped):
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, list: java.util.List[CombinedObservationData]): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getObservationData(self) -> java.util.List[CombinedObservationData]: ...
    def getPrnNumber(self) -> int: ...
    def getRcvrClkOffset(self) -> float: ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem: ...

class CycleSlipDetectorResults:
    def getBeginDate(self, frequency: org.orekit.gnss.Frequency) -> org.orekit.time.AbsoluteDate: ...
    def getCycleSlipMap(self) -> java.util.Map[org.orekit.gnss.Frequency, java.util.List[org.orekit.time.AbsoluteDate]]: ...
    def getEndDate(self, frequency: org.orekit.gnss.Frequency) -> org.orekit.time.AbsoluteDate: ...
    def getSatelliteName(self) -> str: ...

class CycleSlipDetectors:
    def detect(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...

class Dipole:
    CANONICAL_I_J: typing.ClassVar['Dipole'] = ...
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getPrimary(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def getSecondary(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class IntegerLeastSquareComparator(java.util.Comparator['IntegerLeastSquareSolution'], java.io.Serializable):
    def __init__(self): ...
    def compare(self, integerLeastSquareSolution: 'IntegerLeastSquareSolution', integerLeastSquareSolution2: 'IntegerLeastSquareSolution') -> int: ...

class IntegerLeastSquareSolution:
    def __init__(self, longArray: typing.List[int], double: float): ...
    def getSolution(self) -> typing.List[int]: ...
    def getSquaredDistance(self) -> float: ...

class IntegerLeastSquareSolver:
    def solveILS(self, int: int, doubleArray: typing.List[float], intArray: typing.List[int], realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[IntegerLeastSquareSolution]: ...

class InterSatellitesWindUpFactory:
    def __init__(self): ...
    def getWindUp(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, dipole: Dipole, satelliteSystem2: org.orekit.gnss.SatelliteSystem, int2: int, dipole2: Dipole) -> 'InterSatellitesWindUp': ...

class MeasurementCombination:
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet: ...
    def getName(self) -> str: ...

class MeasurementCombinationFactory:
    @staticmethod
    def getGRAPHICCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'GRAPHICCombination': ...
    @staticmethod
    def getGeometryFreeCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'GeometryFreeCombination': ...
    @staticmethod
    def getIonosphereFreeCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'IonosphereFreeCombination': ...
    @staticmethod
    def getMelbourneWubbenaCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'MelbourneWubbenaCombination': ...
    @staticmethod
    def getNarrowLaneCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'NarrowLaneCombination': ...
    @staticmethod
    def getPhaseMinusCodeCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'PhaseMinusCodeCombination': ...
    @staticmethod
    def getWideLaneCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'WideLaneCombination': ...

class OnBoardCommonParametersWithDerivatives(org.orekit.estimation.measurements.CommonParametersWithDerivatives):
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]], gradient: org.hipparchus.analysis.differentiation.Gradient, gradient2: org.hipparchus.analysis.differentiation.Gradient, gradient3: org.hipparchus.analysis.differentiation.Gradient, gradient4: org.hipparchus.analysis.differentiation.Gradient, gradient5: org.hipparchus.analysis.differentiation.Gradient, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient], timeStampedFieldPVCoordinates2: org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]): ...
    def getLocalOffset(self) -> org.hipparchus.analysis.differentiation.Gradient: ...
    def getLocalRate(self) -> org.hipparchus.analysis.differentiation.Gradient: ...
    def getRemoteOffset(self) -> org.hipparchus.analysis.differentiation.Gradient: ...
    def getRemotePV(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]: ...
    def getRemoteRate(self) -> org.hipparchus.analysis.differentiation.Gradient: ...

class OnBoardCommonParametersWithoutDerivatives(org.orekit.estimation.measurements.CommonParametersWithoutDerivatives):
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, double: float, double2: float, double3: float, double4: float, double5: float, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, timeStampedPVCoordinates2: org.orekit.utils.TimeStampedPVCoordinates): ...
    def getLocalOffset(self) -> float: ...
    def getLocalRate(self) -> float: ...
    def getRemoteOffset(self) -> float: ...
    def getRemotePV(self) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def getRemoteRate(self) -> float: ...

class Phase(org.orekit.estimation.measurements.GroundReceiverMeasurement['Phase']):
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, groundStation: org.orekit.estimation.measurements.GroundStation, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, groundStation: org.orekit.estimation.measurements.GroundStation, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, ambiguityCache: AmbiguityCache): ...
    def getAmbiguityDriver(self) -> AmbiguityDriver: ...
    def getWavelength(self) -> float: ...

class PhaseBuilder(org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder[Phase]):
    @typing.overload
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, ambiguityCache: AmbiguityCache): ...
    @typing.overload
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.ObservedMeasurement: ...
    @typing.overload
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> Phase: ...

class WindUpFactory:
    def __init__(self): ...
    def getWindUp(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, dipole: Dipole, string: str) -> 'WindUp': ...

class AbstractCycleSlipDetector(CycleSlipDetectors):
    def detect(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...

class AbstractDualFrequencyCombination(MeasurementCombination):
    MHZ_TO_HZ: typing.ClassVar[float] = ...
    @typing.overload
    def combine(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData) -> CombinedObservationData: ...
    @typing.overload
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet: ...
    def getName(self) -> str: ...

_AbstractInterSatellitesMeasurement__T = typing.TypeVar('_AbstractInterSatellitesMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractInterSatellitesMeasurement(AbstractOnBoardMeasurement[_AbstractInterSatellitesMeasurement__T], typing.Generic[_AbstractInterSatellitesMeasurement__T]):
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite): ...

class AbstractLambdaMethod(IntegerLeastSquareSolver):
    def setComparator(self, comparator: typing.Union[java.util.Comparator[IntegerLeastSquareSolution], typing.Callable[[IntegerLeastSquareSolution, IntegerLeastSquareSolution], int]]) -> None: ...
    def solveILS(self, int: int, doubleArray: typing.List[float], intArray: typing.List[int], realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[IntegerLeastSquareSolution]: ...

_AbstractOneWayGNSSMeasurement__T = typing.TypeVar('_AbstractOneWayGNSSMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractOneWayGNSSMeasurement(AbstractOnBoardMeasurement[_AbstractOneWayGNSSMeasurement__T], typing.Generic[_AbstractOneWayGNSSMeasurement__T]):
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, quadraticClockModel: org.orekit.estimation.measurements.QuadraticClockModel, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...

class AbstractSingleFrequencyCombination(MeasurementCombination):
    @typing.overload
    def combine(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData) -> CombinedObservationData: ...
    @typing.overload
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet: ...
    def getName(self) -> str: ...

class InterSatellitesWindUp(AbstractWindUp['InterSatellitesPhase']): ...

class MelbourneWubbenaCombination(MeasurementCombination):
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet: ...
    def getName(self) -> str: ...

_PythonAbstractOnBoardMeasurement__T = typing.TypeVar('_PythonAbstractOnBoardMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractOnBoardMeasurement(AbstractOnBoardMeasurement[_PythonAbstractOnBoardMeasurement__T], typing.Generic[_PythonAbstractOnBoardMeasurement__T]):
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, list: java.util.List[org.orekit.estimation.measurements.ObservableSatellite]): ...
    def finalize(self) -> None: ...
    def getRemoteClock(self) -> org.orekit.estimation.measurements.QuadraticClockModel: ...
    @typing.overload
    def getRemotePV(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState], int: int) -> org.orekit.utils.FieldPVCoordinatesProvider[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getRemotePV(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.utils.PVCoordinatesProvider: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def theoreticalEvaluation(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.EstimatedMeasurement[_PythonAbstractOnBoardMeasurement__T]: ...
    def theoreticalEvaluationWithoutDerivatives(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractOnBoardMeasurement__T]: ...

_PythonAbstractWindUp__T = typing.TypeVar('_PythonAbstractWindUp__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractWindUp(AbstractWindUp[_PythonAbstractWindUp__T], typing.Generic[_PythonAbstractWindUp__T]):
    def __init__(self, dipole: Dipole, dipole2: Dipole): ...
    def emitterToInert(self, estimatedMeasurementBase: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractWindUp__T]) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def receiverToInert(self, estimatedMeasurementBase: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractWindUp__T]) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...

class PythonAmbiguityAcceptance(AmbiguityAcceptance):
    def __init__(self): ...
    def accept(self, integerLeastSquareSolutionArray: typing.List[IntegerLeastSquareSolution]) -> IntegerLeastSquareSolution: ...
    def finalize(self) -> None: ...
    def numberOfCandidates(self) -> int: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonCycleSlipDetectors(CycleSlipDetectors):
    def __init__(self): ...
    def detect(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonIntegerLeastSquareSolver(IntegerLeastSquareSolver):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def solveILS(self, int: int, doubleArray: typing.List[float], intArray: typing.List[int], realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[IntegerLeastSquareSolution]: ...

class PythonMeasurementCombination(MeasurementCombination):
    def __init__(self): ...
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet: ...
    def finalize(self) -> None: ...
    def getName(self) -> str: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class SimpleRatioAmbiguityAcceptance(AmbiguityAcceptance):
    def __init__(self, double: float): ...
    def accept(self, integerLeastSquareSolutionArray: typing.List[IntegerLeastSquareSolution]) -> IntegerLeastSquareSolution: ...
    def numberOfCandidates(self) -> int: ...

class WindUp(AbstractWindUp[Phase]): ...

class GRAPHICCombination(AbstractSingleFrequencyCombination): ...

class GeometryFreeCombination(AbstractDualFrequencyCombination): ...

class GeometryFreeCycleSlipDetector(AbstractCycleSlipDetector):
    def __init__(self, double: float, double2: float, int: int): ...

class InterSatellitesOneWayRangeRate(AbstractInterSatellitesMeasurement['InterSatellitesOneWayRangeRate']):
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    def __init__(self, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float): ...

class InterSatellitesPhase(AbstractInterSatellitesMeasurement['InterSatellitesPhase']):
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, ambiguityCache: AmbiguityCache): ...
    def getAmbiguityDriver(self) -> org.orekit.utils.ParameterDriver: ...
    def getWavelength(self) -> float: ...

class IonosphereFreeCombination(AbstractDualFrequencyCombination): ...

class LambdaMethod(AbstractLambdaMethod):
    def __init__(self): ...

class ModifiedLambdaMethod(AbstractLambdaMethod):
    def __init__(self): ...

class NarrowLaneCombination(AbstractDualFrequencyCombination): ...

class OneWayGNSSPhase(AbstractOneWayGNSSMeasurement['OneWayGNSSPhase']):
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, double5: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, string: str, quadraticClockModel: org.orekit.estimation.measurements.QuadraticClockModel, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, ambiguityCache: AmbiguityCache): ...
    def getAmbiguityDriver(self) -> AmbiguityDriver: ...
    def getWavelength(self) -> float: ...

class OneWayGNSSRange(AbstractOneWayGNSSMeasurement['OneWayGNSSRange']):
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, quadraticClockModel: org.orekit.estimation.measurements.QuadraticClockModel, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...

class OneWayGNSSRangeRate(AbstractOneWayGNSSMeasurement['OneWayGNSSRangeRate']):
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, quadraticClockModel: org.orekit.estimation.measurements.QuadraticClockModel, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...

class PhaseMinusCodeCombination(AbstractSingleFrequencyCombination): ...

class PhaseMinusCodeCycleSlipDetector(AbstractCycleSlipDetector):
    def __init__(self, double: float, double2: float, int: int, int2: int): ...

class PythonAbstractCycleSlipDetector(AbstractCycleSlipDetector):
    def cycleSlipDataSet(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float, frequency: org.orekit.gnss.Frequency) -> None: ...
    def finalize(self) -> None: ...
    def getMaxTimeBeetween2Measurement(self) -> float: ...
    def getMinMeasurementNumber(self) -> int: ...
    def getResults(self) -> java.util.List[CycleSlipDetectorResults]: ...
    def getStuffReference(self) -> java.util.List[java.util.Map[org.orekit.gnss.Frequency, 'AbstractCycleSlipDetector.DataForDetection']]: ...
    def manageData(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def setName(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> str: ...

class PythonAbstractDualFrequencyCombination(AbstractDualFrequencyCombination):
    def __init__(self, combinationType: CombinationType, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def finalize(self) -> None: ...
    def getCombinedFrequency(self, frequency: org.orekit.gnss.Frequency, frequency2: org.orekit.gnss.Frequency) -> float: ...
    def getCombinedValue(self, double: float, frequency: org.orekit.gnss.Frequency, double2: float, frequency2: org.orekit.gnss.Frequency) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonAbstractInterSatellitesMeasurement__T = typing.TypeVar('_PythonAbstractInterSatellitesMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractInterSatellitesMeasurement(AbstractInterSatellitesMeasurement[_PythonAbstractInterSatellitesMeasurement__T], typing.Generic[_PythonAbstractInterSatellitesMeasurement__T]):
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def theoreticalEvaluation(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.EstimatedMeasurement[_PythonAbstractInterSatellitesMeasurement__T]: ...
    def theoreticalEvaluationWithoutDerivatives(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractInterSatellitesMeasurement__T]: ...

class PythonAbstractLambdaMethod(AbstractLambdaMethod):
    def __init__(self): ...
    def discreteSearch(self) -> None: ...
    def finalize(self) -> None: ...
    def inverseDecomposition(self) -> None: ...
    def ltdlDecomposition(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def reduction(self) -> None: ...

_PythonAbstractOneWayGNSSMeasurement__T = typing.TypeVar('_PythonAbstractOneWayGNSSMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractOneWayGNSSMeasurement(AbstractOneWayGNSSMeasurement[_PythonAbstractOneWayGNSSMeasurement__T], typing.Generic[_PythonAbstractOneWayGNSSMeasurement__T]):
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, quadraticClockModel: org.orekit.estimation.measurements.QuadraticClockModel, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def theoreticalEvaluation(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.EstimatedMeasurement[_PythonAbstractOneWayGNSSMeasurement__T]: ...
    def theoreticalEvaluationWithoutDerivatives(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractOneWayGNSSMeasurement__T]: ...

class PythonAbstractSingleFrequencyCombination(AbstractSingleFrequencyCombination):
    def __init__(self, combinationType: CombinationType, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def finalize(self) -> None: ...
    def getCombinedValue(self, double: float, double2: float) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class WideLaneCombination(AbstractDualFrequencyCombination): ...

class IntegerBootstrapping(LambdaMethod):
    def __init__(self, double: float): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.gnss")``.

    AbstractCycleSlipDetector: typing.Type[AbstractCycleSlipDetector]
    AbstractDualFrequencyCombination: typing.Type[AbstractDualFrequencyCombination]
    AbstractInterSatellitesMeasurement: typing.Type[AbstractInterSatellitesMeasurement]
    AbstractLambdaMethod: typing.Type[AbstractLambdaMethod]
    AbstractOnBoardMeasurement: typing.Type[AbstractOnBoardMeasurement]
    AbstractOneWayGNSSMeasurement: typing.Type[AbstractOneWayGNSSMeasurement]
    AbstractSingleFrequencyCombination: typing.Type[AbstractSingleFrequencyCombination]
    AbstractWindUp: typing.Type[AbstractWindUp]
    AmbiguityAcceptance: typing.Type[AmbiguityAcceptance]
    AmbiguityCache: typing.Type[AmbiguityCache]
    AmbiguityDriver: typing.Type[AmbiguityDriver]
    AmbiguitySolver: typing.Type[AmbiguitySolver]
    CombinationType: typing.Type[CombinationType]
    CombinedObservationData: typing.Type[CombinedObservationData]
    CombinedObservationDataSet: typing.Type[CombinedObservationDataSet]
    CycleSlipDetectorResults: typing.Type[CycleSlipDetectorResults]
    CycleSlipDetectors: typing.Type[CycleSlipDetectors]
    Dipole: typing.Type[Dipole]
    GRAPHICCombination: typing.Type[GRAPHICCombination]
    GeometryFreeCombination: typing.Type[GeometryFreeCombination]
    GeometryFreeCycleSlipDetector: typing.Type[GeometryFreeCycleSlipDetector]
    IntegerBootstrapping: typing.Type[IntegerBootstrapping]
    IntegerLeastSquareComparator: typing.Type[IntegerLeastSquareComparator]
    IntegerLeastSquareSolution: typing.Type[IntegerLeastSquareSolution]
    IntegerLeastSquareSolver: typing.Type[IntegerLeastSquareSolver]
    InterSatellitesOneWayRangeRate: typing.Type[InterSatellitesOneWayRangeRate]
    InterSatellitesPhase: typing.Type[InterSatellitesPhase]
    InterSatellitesWindUp: typing.Type[InterSatellitesWindUp]
    InterSatellitesWindUpFactory: typing.Type[InterSatellitesWindUpFactory]
    IonosphereFreeCombination: typing.Type[IonosphereFreeCombination]
    LambdaMethod: typing.Type[LambdaMethod]
    MeasurementCombination: typing.Type[MeasurementCombination]
    MeasurementCombinationFactory: typing.Type[MeasurementCombinationFactory]
    MelbourneWubbenaCombination: typing.Type[MelbourneWubbenaCombination]
    ModifiedLambdaMethod: typing.Type[ModifiedLambdaMethod]
    NarrowLaneCombination: typing.Type[NarrowLaneCombination]
    OnBoardCommonParametersWithDerivatives: typing.Type[OnBoardCommonParametersWithDerivatives]
    OnBoardCommonParametersWithoutDerivatives: typing.Type[OnBoardCommonParametersWithoutDerivatives]
    OneWayGNSSPhase: typing.Type[OneWayGNSSPhase]
    OneWayGNSSRange: typing.Type[OneWayGNSSRange]
    OneWayGNSSRangeRate: typing.Type[OneWayGNSSRangeRate]
    Phase: typing.Type[Phase]
    PhaseBuilder: typing.Type[PhaseBuilder]
    PhaseMinusCodeCombination: typing.Type[PhaseMinusCodeCombination]
    PhaseMinusCodeCycleSlipDetector: typing.Type[PhaseMinusCodeCycleSlipDetector]
    PythonAbstractCycleSlipDetector: typing.Type[PythonAbstractCycleSlipDetector]
    PythonAbstractDualFrequencyCombination: typing.Type[PythonAbstractDualFrequencyCombination]
    PythonAbstractInterSatellitesMeasurement: typing.Type[PythonAbstractInterSatellitesMeasurement]
    PythonAbstractLambdaMethod: typing.Type[PythonAbstractLambdaMethod]
    PythonAbstractOnBoardMeasurement: typing.Type[PythonAbstractOnBoardMeasurement]
    PythonAbstractOneWayGNSSMeasurement: typing.Type[PythonAbstractOneWayGNSSMeasurement]
    PythonAbstractSingleFrequencyCombination: typing.Type[PythonAbstractSingleFrequencyCombination]
    PythonAbstractWindUp: typing.Type[PythonAbstractWindUp]
    PythonAmbiguityAcceptance: typing.Type[PythonAmbiguityAcceptance]
    PythonCycleSlipDetectors: typing.Type[PythonCycleSlipDetectors]
    PythonIntegerLeastSquareSolver: typing.Type[PythonIntegerLeastSquareSolver]
    PythonMeasurementCombination: typing.Type[PythonMeasurementCombination]
    SimpleRatioAmbiguityAcceptance: typing.Type[SimpleRatioAmbiguityAcceptance]
    WideLaneCombination: typing.Type[WideLaneCombination]
    WindUp: typing.Type[WindUp]
    WindUpFactory: typing.Type[WindUpFactory]
