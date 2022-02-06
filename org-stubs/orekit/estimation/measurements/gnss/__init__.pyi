import java.io
import java.lang
import java.util
import org.hipparchus.linear
import org.hipparchus.random
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.generation
import org.orekit.gnss
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



class AmbiguityAcceptance:
    """
    public interface AmbiguityAcceptance
    
        Interface defining ambiguity acceptance tests.
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.AmbiguitySolver`
    """
    def accept(self, integerLeastSquareSolutionArray: typing.List['IntegerLeastSquareSolution']) -> 'IntegerLeastSquareSolution':
        """
            Check if one of the candidate solutions can be accepted.
        
            Parameters:
                candidates (:class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution`[]): candidate solutions of the Integer Least Squares problem, in increasing squared distance order (the array contains at
                    least :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.numberOfCandidates` candidates)
        
            Returns:
                the candidate solution to accept (normally the one at index 0), or null if we should still use the float solution
        
        
        """
        ...
    def numberOfCandidates(self) -> int:
        """
            Get the number of candidate solutions to search for.
        
            Returns:
                number of candidate solutions to search for
        
        
        """
        ...

class AmbiguitySolver:
    """
    public class AmbiguitySolver extends Object
    
        Class for solving integer ambiguity problems.
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.LambdaMethod`
    """
    def __init__(self, list: java.util.List[org.orekit.utils.ParameterDriver], integerLeastSquareSolver: 'IntegerLeastSquareSolver', ambiguityAcceptance: AmbiguityAcceptance): ...
    def fixIntegerAmbiguities(self, int: int, list: java.util.List[org.orekit.utils.ParameterDriver], realMatrix: org.hipparchus.linear.RealMatrix) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getAllAmbiguityDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def unFixAmbiguity(self, parameterDriver: org.orekit.utils.ParameterDriver) -> None:
        """
            Un-fix an integer ambiguity (typically after a phase cycle slip).
        
            Parameters:
                ambiguityDriver (:class:`~org.orekit.utils.ParameterDriver`): driver for the ambiguity to un-fix
        
        
        """
        ...

class CombinationType(java.lang.Enum['CombinationType']):
    """
    public enum CombinationType extends Enum<:class:`~org.orekit.estimation.measurements.gnss.CombinationType`>
    
        Enumerate for combination of measurements types.
    
        Since:
            10.1
    """
    PHASE_MINUS_CODE: typing.ClassVar['CombinationType'] = ...
    GRAPHIC: typing.ClassVar['CombinationType'] = ...
    GEOMETRY_FREE: typing.ClassVar['CombinationType'] = ...
    IONO_FREE: typing.ClassVar['CombinationType'] = ...
    NARROW_LANE: typing.ClassVar['CombinationType'] = ...
    WIDE_LANE: typing.ClassVar['CombinationType'] = ...
    MELBOURNE_WUBBENA: typing.ClassVar['CombinationType'] = ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Returns:
                the name
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CombinationType':
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
    def values() -> typing.List['CombinationType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CombinationType c : CombinationType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CycleSlipDetectorResults:
    """
    public class CycleSlipDetectorResults extends Object
    
        This class is used to contains all the data computed within cycle-slip detector. All these parameters are what user can
        get from the detectors.
    
        Since:
            10.2
    """
    def getBeginDate(self, frequency: org.orekit.gnss.Frequency) -> org.orekit.time.AbsoluteDate:
        """
            Return the date of validity beginning of the detector.
        
            Parameters:
                f (:class:`~org.orekit.gnss.Frequency`): frequency
        
            Returns:
                AbsoluteDate
        
        
        """
        ...
    def getCycleSlipMap(self) -> java.util.Map[org.orekit.gnss.Frequency, java.util.List[org.orekit.time.AbsoluteDate]]: ...
    def getEndDate(self, frequency: org.orekit.gnss.Frequency) -> org.orekit.time.AbsoluteDate:
        """
            Return the end date at the given frequency.
        
            For dual-Frequency cycle-slip detector, the :class:`~org.orekit.gnss.Frequency` contained in the map is the higher
            frequency (e.g. for L1-L2 the frequency in the map will be L1)
        
            Parameters:
                f (:class:`~org.orekit.gnss.Frequency`): frequency
        
            Returns:
                date of end of validity of the detectors
        
        
        """
        ...
    def getSatelliteName(self) -> str:
        """
            Get the satellite name.
        
            Returns:
                satellite name
        
        
        """
        ...

class CycleSlipDetectors:
    """
    public interface CycleSlipDetectors
    
        Interface for phase measurement cycle-slip detection.
    
        Since:
            10.2
    """
    def detect(self, list: java.util.List[org.orekit.gnss.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...

class IntegerLeastSquareComparator(java.util.Comparator['IntegerLeastSquareSolution'], java.io.Serializable):
    """
    public class IntegerLeastSquareComparator extends Object implements Comparator<:class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution`>, Serializable
    
        Comparator for :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution` instance.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution`, :meth:`~serialized`
    """
    def __init__(self): ...
    def compare(self, integerLeastSquareSolution: 'IntegerLeastSquareSolution', integerLeastSquareSolution2: 'IntegerLeastSquareSolution') -> int:
        """
            The comparison is based on the squared distance to the float solution.
        
            Specified by:
                 in interface 
        
        
        """
        ...

class IntegerLeastSquareSolution:
    """
    public class IntegerLeastSquareSolution extends Object
    
        Class holding a solution to an Integer Least Square problem.
    
        Since:
            10.0
    """
    def __init__(self, longArray: typing.List[int], double: float): ...
    def getSolution(self) -> typing.List[int]:
        """
            Get the solution array.
        
            Returns:
                solution array
        
        
        """
        ...
    def getSquaredDistance(self) -> float:
        """
            Get the squared distance to the corresponding float solution.
        
            Returns:
                squared distance to the corresponding float solution
        
        
        """
        ...

class IntegerLeastSquareSolver:
    """
    public interface IntegerLeastSquareSolver
    
        Interface for algorithms solving integer least square problems.
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution`
    """
    def solveILS(self, int: int, doubleArray: typing.List[float], intArray: typing.List[int], realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[IntegerLeastSquareSolution]:
        """
            Find the best solutions to an Integer Least Square problem.
        
            Parameters:
                nbSol (int): number of solutions to search for
                floatAmbiguities (double[]): float estimates of ambiguities
                indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
                covariance (RealMatrix): global covariance matrix (includes ambiguities among other parameters)
        
            Returns:
                at most :code:`nbSol` solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

class InterSatellitesPhase(org.orekit.estimation.measurements.AbstractMeasurement['InterSatellitesPhase']):
    """
    public class InterSatellitesPhase extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Phase measurement between two satellites.
    
        The measurement is considered to be a signal emitted from a remote satellite and received by a local satellite. Its
        value is the number of cycles between emission and reception. The motion of both spacecrafts during the signal flight
        time are taken into account. The date of the measurement corresponds to the reception on ground of the emitted signal.
    
        Since:
            10.3
    """
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    """
    public static final String AMBIGUITY_NAME
    
        Name for ambiguity driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float): ...
    def getAmbiguityDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for phase ambiguity.
        
            Returns:
                the driver for phase ambiguity
        
        
        """
        ...
    def getWavelength(self) -> float:
        """
            Get the wavelength.
        
            Returns:
                wavelength (m)
        
        
        """
        ...

class MeasurementCombination:
    """
    public interface MeasurementCombination
    
        Interface for combination of measurements.
    
        Since:
            10.1
    """
    def combine(self, observationDataSet: org.orekit.gnss.ObservationDataSet) -> org.orekit.gnss.CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Parameters:
                observations (:class:`~org.orekit.gnss.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Returns:
                name of the combination of measurements
        
        
        """
        ...

class MeasurementCombinationFactory:
    """
    public class MeasurementCombinationFactory extends Object
    
        Factory for predefined combination of measurements.
    
        This is a utility class, so its constructor is private.
    
        Since:
            10.1
    """
    @staticmethod
    def getGRAPHICCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'GRAPHICCombination':
        """
            Get the GRAPHIC combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                phase minus code combination
        
        
        """
        ...
    @staticmethod
    def getGeometryFreeCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'GeometryFreeCombination':
        """
            Get the Geometry-Free combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                Geometry-Free combination
        
        
        """
        ...
    @staticmethod
    def getIonosphereFreeCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'IonosphereFreeCombination':
        """
            Get the Ionosphere-Free combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                Ionosphere-Lane combination
        
        
        """
        ...
    @staticmethod
    def getMelbourneWubbenaCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'MelbourneWubbenaCombination':
        """
            Get the Melbourne-WÃ¼bbena combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                Melbourne-WÃ¼bbena combination
        
        
        """
        ...
    @staticmethod
    def getNarrowLaneCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'NarrowLaneCombination':
        """
            Get the Narrow-Lane combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                Narrow-Lane combination
        
        
        """
        ...
    @staticmethod
    def getPhaseMinusCodeCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'PhaseMinusCodeCombination':
        """
            Get the phase minus code combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                phase minus code combination
        
        
        """
        ...
    @staticmethod
    def getWideLaneCombination(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'WideLaneCombination':
        """
            Get the Wide-Lane combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                Wide-Lane combination
        
        
        """
        ...

class OneWayGNSSPhase(org.orekit.estimation.measurements.AbstractMeasurement['OneWayGNSSPhase']):
    """
    public class OneWayGNSSPhase extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        One-way GNSS phase measurement.
    
        This class can be used in precise orbit determination applications for modeling a phase measurement between a GNSS
        satellite (emitter) and a LEO satellite (receiver).
    
        The one-way GNSS phase measurement assumes knowledge of the orbit and the clock offset of the emitting GNSS satellite.
        For instance, it is possible to use a SP3 file or a GNSS navigation message to recover the satellite's orbit and clock.
    
        This class is very similar to :class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase` measurement class.
        However, using the one-way GNSS phase measurement, the orbit and clock of the emitting GNSS satellite are **NOT**
        estimated simultaneously with LEO satellite coordinates.
    
        Since:
            10.3
    """
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    """
    public static final String AMBIGUITY_NAME
    
        Name for ambiguity driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, double5: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def getAmbiguityDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for phase ambiguity.
        
            Returns:
                the driver for phase ambiguity
        
        
        """
        ...
    def getWavelength(self) -> float:
        """
            Get the wavelength.
        
            Returns:
                wavelength (m)
        
        
        """
        ...

class OneWayGNSSRange(org.orekit.estimation.measurements.AbstractMeasurement['OneWayGNSSRange']):
    """
    public class OneWayGNSSRange extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange`>
    
        One-way GNSS range measurement.
    
        This class can be used in precise orbit determination applications for modeling a range measurement between a GNSS
        satellite (emitter) and a LEO satellite (receiver).
    
        The one-way GNSS range measurement assumes knowledge of the orbit and the clock offset of the emitting GNSS satellite.
        For instance, it is possible to use a SP3 file or a GNSS navigation message to recover the satellite's orbit and clock.
    
        This class is very similar to :class:`~org.orekit.estimation.measurements.InterSatellitesRange` measurement class.
        However, using the one-way GNSS range measurement, the orbit and clock of the emitting GNSS satellite are **NOT**
        estimated simultaneously with LEO satellite coordinates.
    
        Since:
            10.3
    """
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...

class Phase(org.orekit.estimation.measurements.AbstractMeasurement['Phase']):
    """
    public class Phase extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modeling a phase measurement from a ground station.
    
        The measurement is considered to be a signal emitted from a spacecraft and received on a ground station. Its value is
        the number of cycles between emission and reception. The motion of both the station and the spacecraft during the signal
        flight time are taken into account. The date of the measurement corresponds to the reception on ground of the emitted
        signal.
    
        Since:
            9.2
    """
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    """
    public static final String AMBIGUITY_NAME
    
        Name for ambiguity driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, groundStation: org.orekit.estimation.measurements.GroundStation, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def getAmbiguityDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for phase ambiguity.
        
            Returns:
                the driver for phase ambiguity
        
            Since:
                10.3
        
        
        """
        ...
    def getStation(self) -> org.orekit.estimation.measurements.GroundStation:
        """
            Get the ground station from which measurement is performed.
        
            Returns:
                ground station from which measurement is performed
        
        
        """
        ...
    def getWavelength(self) -> float:
        """
            Get the wavelength.
        
            Returns:
                wavelength (m)
        
        
        """
        ...

class PhaseBuilder(org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder[Phase]):
    """
    public class PhaseBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Builder for :class:`~org.orekit.estimation.measurements.gnss.Phase` measurements.
    
        Since:
            10.1
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> Phase:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

class WindUp(org.orekit.estimation.measurements.EstimationModifier[Phase]):
    """
    public class WindUp extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Modifier for wind-up effect in GNSS :class:`~org.orekit.estimation.measurements.gnss.Phase`.
    
        Since:
            10.1
    
        Also see:
            Carrier Phase Wind-up Effect, :class:`~org.orekit.estimation.measurements.gnss.WindUpFactory`
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[Phase]) -> None: ...

class WindUpFactory:
    """
    public class WindUpFactory extends Object
    
        Factory for :class:`~org.orekit.estimation.measurements.gnss.WindUp` modifiers.
    
        The factory ensures the same instance is returned for all satellite/receiver pair, thus preserving phase continuity for
        successive measurements involving the same pair.
    
        Since:
            10.1
    """
    def __init__(self): ...
    def getWindUp(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, string: str) -> WindUp:
        """
            Get a modifier for a satellite/receiver pair.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): system the satellite belongs to
                prnNumber (int): PRN number
                receiverName (String): name of the receiver
        
            Returns:
                modifier for the satellite/receiver pair
        
        
        """
        ...

class AbstractCycleSlipDetector(CycleSlipDetectors):
    """
    public abstract class AbstractCycleSlipDetector extends Object implements :class:`~org.orekit.estimation.measurements.gnss.CycleSlipDetectors`
    
        Base class for cycle-slip detectors.
    
        Since:
            10.2
    """
    def detect(self, list: java.util.List[org.orekit.gnss.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...

class AbstractDualFrequencyCombination(MeasurementCombination):
    """
    public abstract class AbstractDualFrequencyCombination extends Object implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    
        Base class for dual frequency combination of measurements.
    
        Since:
            10.1
    """
    MHZ_TO_HZ: typing.ClassVar[float] = ...
    """
    public static final double MHZ_TO_HZ
    
        Mega Hertz to Hertz converter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def combine(self, observationData: org.orekit.gnss.ObservationData, observationData2: org.orekit.gnss.ObservationData) -> org.orekit.gnss.CombinedObservationData:
        """
            Combines observation data using a dual frequency combination of measurements.
        
            Parameters:
                od1 (:class:`~org.orekit.gnss.ObservationData`): first observation data to combined
                od2 (:class:`~org.orekit.gnss.ObservationData`): second observation data to combined
        
            Returns:
                a combined observation data
        
        """
        ...
    @typing.overload
    def combine(self, observationDataSet: org.orekit.gnss.ObservationDataSet) -> org.orekit.gnss.CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.gnss.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Returns:
                name of the combination of measurements
        
        
        """
        ...

class AbstractLambdaMethod(IntegerLeastSquareSolver):
    """
    public abstract class AbstractLambdaMethod extends Object implements :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
    
        Base class for decorrelation/reduction engine for LAMBDA type methods.
    
        This class is based on both the 1996 paper The LAMBDA method for integer ambiguity estimation: implementation aspects by
        Paul de Jonge and Christian Tiberius and on the 2005 paper A modified LAMBDA method for integer least-squares estimation
        by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
        Since:
            10.0
    """
    def setComparator(self, comparator: typing.Union[java.util.Comparator[IntegerLeastSquareSolution], typing.Callable[[IntegerLeastSquareSolution, IntegerLeastSquareSolution], int]]) -> None: ...
    def solveILS(self, int: int, doubleArray: typing.List[float], intArray: typing.List[int], realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[IntegerLeastSquareSolution]:
        """
            Find the best solutions to an Integer Least Square problem.
        
            Specified by:
                 in interface :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
        
            Parameters:
                nbSol (int): number of solutions to search for
                floatAmbiguities (double[]): float estimates of ambiguities
                indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
                covariance (RealMatrix): global covariance matrix (includes ambiguities among other parameters)
        
            Returns:
                at most :code:`nbSol` solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

class AbstractSingleFrequencyCombination(MeasurementCombination):
    """
    public abstract class AbstractSingleFrequencyCombination extends Object implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    
        Base class for single frequency combination of measurements.
    
        Since:
            10.1
    """
    @typing.overload
    def combine(self, observationData: org.orekit.gnss.ObservationData, observationData2: org.orekit.gnss.ObservationData) -> org.orekit.gnss.CombinedObservationData:
        """
            Combines observation data using a single frequency combination of measurements.
        
            Parameters:
                phase (:class:`~org.orekit.gnss.ObservationData`): phase measurement
                pseudoRange (:class:`~org.orekit.gnss.ObservationData`): pseudoRange measurement
        
            Returns:
                a combined observation data
        
        
        """
        ...
    @typing.overload
    def combine(self, observationDataSet: org.orekit.gnss.ObservationDataSet) -> org.orekit.gnss.CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.gnss.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Returns:
                name of the combination of measurements
        
        
        """
        ...

class MelbourneWubbenaCombination(MeasurementCombination):
    """
    public class MelbourneWubbenaCombination extends Object implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    
        Melbourne-WÃ¼bbena combination.
    
        This combination allows, thanks to the wide-lane combination, a larger wavelength than each signal individually.
        Moreover, the measurement noise is reduced by the narrow-lane combination of code measurements.
    
        .. code-block: java
        
        
            mMW =  Î¦WL- RNL
            mMW =  Î»WL * NWL+ b + Îµ
         
        With:
    
          - mMW : Melbourne-WÃ¼bbena measurement.
          - Î¦WL : Wide-Lane phase measurement.
          - RNL : Narrow-Lane code measurement.
          - Î»WL : Wide-Lane wavelength.
          - NWL : Wide-Lane ambiguity (Nf1 - Nf2).
          - b : Satellite and receiver instrumental delays.
          - Îµ : Measurement noise.
    
    
        :class:`~org.orekit.estimation.measurements.gnss.NarrowLaneCombination` and
        :class:`~org.orekit.estimation.measurements.gnss.WideLaneCombination` combinations shall be performed with the same pair
        of frequencies.
    
        Since:
            10.1
    
        Also see:
            "Detector based in code and carrier phase data: The Melbourne-WÃƒÂ¼bbena combination, J. Sanz Subirana, J.M. Juan
            Zornoza and M. HernÃƒÂ¡ndez-Pajares, 2011"
    """
    def combine(self, observationDataSet: org.orekit.gnss.ObservationDataSet) -> org.orekit.gnss.CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.gnss.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Returns:
                name of the combination of measurements
        
        
        """
        ...

class PythonAmbiguityAcceptance(AmbiguityAcceptance):
    """
    public class PythonAmbiguityAcceptance extends Object implements :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
    """
    def __init__(self): ...
    def accept(self, integerLeastSquareSolutionArray: typing.List[IntegerLeastSquareSolution]) -> IntegerLeastSquareSolution:
        """
            Check if one of the candidate solutions can be accepted.
        
            Specified by:
                 in interface :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
            Parameters:
                candidates (:class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution`[]): candidate solutions of the Integer Least Squares problem, in increasing squared distance order (the array contains at
                    least :meth:`~org.orekit.estimation.measurements.gnss.PythonAmbiguityAcceptance.numberOfCandidates` candidates)
        
            Returns:
                the candidate solution to accept (normally the one at index 0), or null if we should still use the float solution
        
        
        """
        ...
    def finalize(self) -> None: ...
    def numberOfCandidates(self) -> int:
        """
            Get the number of candidate solutions to search for.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.numberOfCandidates`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
            Returns:
                number of candidate solutions to search for
        
        
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

class PythonCycleSlipDetectors(CycleSlipDetectors):
    """
    public class PythonCycleSlipDetectors extends Object implements :class:`~org.orekit.estimation.measurements.gnss.CycleSlipDetectors`
    """
    def __init__(self): ...
    def detect(self, list: java.util.List[org.orekit.gnss.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...
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

class PythonIntegerLeastSquareSolver(IntegerLeastSquareSolver):
    """
    public class PythonIntegerLeastSquareSolver extends Object implements :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
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
    def solveILS(self, int: int, doubleArray: typing.List[float], intArray: typing.List[int], realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[IntegerLeastSquareSolution]:
        """
            Find the best solutions to an Integer Least Square problem.
        
            Specified by:
                 in interface :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
        
            Parameters:
                nbSol (int): number of solutions to search for
                floatAmbiguities (double[]): float estimates of ambiguities
                indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
                covariance (RealMatrix): global covariance matrix (includes ambiguities among other parameters)
        
            Returns:
                at most :code:`nbSol` solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

class PythonMeasurementCombination(MeasurementCombination):
    """
    public class PythonMeasurementCombination extends Object implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    """
    def __init__(self): ...
    def combine(self, observationDataSet: org.orekit.gnss.ObservationDataSet) -> org.orekit.gnss.CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.gnss.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Returns:
                name of the combination of measurements
        
        
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

class SimpleRatioAmbiguityAcceptance(AmbiguityAcceptance):
    """
    public class SimpleRatioAmbiguityAcceptance extends Object implements :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
    
        Ambiguity acceptance test based on a ratio of the two best candidates.
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.AmbiguitySolver`
    """
    def __init__(self, double: float): ...
    def accept(self, integerLeastSquareSolutionArray: typing.List[IntegerLeastSquareSolution]) -> IntegerLeastSquareSolution:
        """
            Check if one of the candidate solutions can be accepted.
        
            If the ratio :code:`candidate[0]/candidate[1]` is smaller or equal to the ratio given at construction, then
            :code:`candidate[0]` will be accepted
        
            Specified by:
                 in interface :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
            Parameters:
                candidates (:class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution`[]): candidate solutions of the Integer Least Squares problem, in increasing squared distance order (the array contains at
                    least :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.numberOfCandidates` candidates)
        
            Returns:
                the candidate solution to accept (normally the one at index 0), or null if we should still use the float solution
        
        
        """
        ...
    def numberOfCandidates(self) -> int:
        """
            Get the number of candidate solutions to search for.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.numberOfCandidates`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
            Returns:
                number of candidate solutions to search for
        
        
        """
        ...

class GRAPHICCombination(AbstractSingleFrequencyCombination):
    """
    public class GRAPHICCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination`
    
        GRoup And Phase Ionospheric Calibration (GRAPHIC) combination.
    
        This combination is a ionosphere-free single frequency combination of measurements.
    
        .. code-block: java
        
        
            mf =  0.5 * (Î¦f + Rf)
         
        With:
    
          - mf : GRAPHIC measurement.
          - Î¦f : Phase measurement.
          - Rf : Code measurement.
          - f : Frequency.
    
    
        Since:
            10.1
    """
    ...

class GeometryFreeCombination(AbstractDualFrequencyCombination):
    """
    public class GeometryFreeCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
    
        Geometry-free combination.
    
        This combination removes the geometry part of the measurement. It can be used to estimate the ionospheric electron
        content or to detect cycle slips in the carrier phase, as well.
    
        .. code-block: java
        
        
            mGF =  m2 - m1
         
        With:
    
          - mGF: Geometry-free measurement.
          - m1 : First measurement.
          - m2 : Second measurement.
    
    
        Geometry-Free combination is a dual frequency combination. The two measurements shall have different frequencies but
        they must have the same :class:`~org.orekit.gnss.MeasurementType`.
    
        Since:
            10.1
    """
    ...

class GeometryFreeCycleSlipDetector(AbstractCycleSlipDetector):
    """
    public class GeometryFreeCycleSlipDetector extends :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
    
        Geometry free cycle slip detectors. The detector is based the algorithm given in Detector based in carrier phase data:
        The geometry-free combination by Zornoza and M. HernÃƒÂ¡ndez-Pajares. Within this class a second order polynomial is
        used to smooth the data. We consider a cycle-slip occurring if the current measurement is too far from the one predicted
        with the polynomial.
    
        For building the detector, one should give a threshold and a gap time limit. After construction of the detectors, one
        can have access to a List of CycleData. Each CycleDate represents a link between the station (define by the RINEX file)
        and a satellite at a specific frequency. For each cycle data, one has access to the begin and end of availability, and a
        sorted set which contains all the date at which cycle-slip have been detected
    
    
        Since:
            10.2
    """
    def __init__(self, double: float, double2: float, int: int): ...

class IonosphereFreeCombination(AbstractDualFrequencyCombination):
    """
    public class IonosphereFreeCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
    
        Ionosphere-free combination.
    
        This combination removes the first order (up to 99.9%) ionospheric effect.
    
        .. code-block: java
        
        
                     f1Â² * m1 - f2Â² * m2
            mIF =  -----------------------
                          f1Â² - f2Â²
         
        With:
    
          - mIF: Ionosphere-free measurement.
          - f1 : Frequency of the first measurement.
          - m1 : First measurement.
          - f2 : Frequency of the second measurement.
          - m1 : Second measurement.
    
    
        Ionosphere-free combination is a dual frequency combination. The two measurements shall have different frequencies but
        they must have the same :class:`~org.orekit.gnss.MeasurementType`.
    
        Since:
            10.1
    """
    ...

class LambdaMethod(AbstractLambdaMethod):
    """
    public class LambdaMethod extends :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
    
        Decorrelation/reduction engine for LAMBDA method.
    
        This class implements PJG Teunissen Least Square Ambiguity Decorrelation Adjustment (LAMBDA) method, as described in
        both the 1996 paper The LAMBDA method for integer ambiguity estimation: implementation aspects by Paul de Jonge and
        Christian Tiberius and on the 2005 paper A modified LAMBDA method for integer least-squares estimation by X.-W Chang, X.
        Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
        It slightly departs on the original LAMBDA method as it does implement the following improvements proposed in the de
        Jonge and Tiberius 1996 paper that vastly speed up the search:
    
          - alternate search starting from the middle and expanding outwards
          - automatic shrinking of ellipsoid during the search
    
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.AmbiguitySolver`
    """
    def __init__(self): ...

class ModifiedLambdaMethod(AbstractLambdaMethod):
    """
    public class ModifiedLambdaMethod extends :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
    
        Decorrelation/reduction engine for Modified LAMBDA method.
    
        This class implements Modified Least Square Ambiguity Decorrelation Adjustment (MLAMBDA) method, as described in A
        modified LAMBDA method for integer least-squares estimation by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy
        79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.AmbiguitySolver`
    """
    def __init__(self): ...

class NarrowLaneCombination(AbstractDualFrequencyCombination):
    """
    public class NarrowLaneCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
    
        Narrow-Lane combination.
    
        This combination create signal with a narrow wavelength. The signal in this combination has a lower noise than each
        separated separeted component.
    
        .. code-block: java
        
        
                      f1 * m1 + f2 * m2
            mNL =  -----------------------
                           f1 + f2
         
        With:
    
          - mNL : Narrow-laning measurement.
          - f1 : Frequency of the first measurement.
          - pr1 : First measurement.
          - f2 : Frequency of the second measurement.
          - m1 : Second measurement.
    
    
        Narrow-Lane combination is a dual frequency combination. The two measurements shall have different frequencies but they
        must have the same :class:`~org.orekit.gnss.MeasurementType`.
    
        Since:
            10.1
    """
    ...

class PhaseMinusCodeCombination(AbstractSingleFrequencyCombination):
    """
    public class PhaseMinusCodeCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination`
    
        Phase minus Code combination.
    
        This combination is a single frequency combination of measurements that can be used for cycle-slip detection.
    
        .. code-block: java
        
        
            mf =  Î¦f - Rf
         
        With:
    
          - mf : Phase minus Code measurement.
          - Î¦f : Phase measurement.
          - Rf : Code measurement.
          - f : Frequency.
    
    
        Since:
            10.1
    """
    ...

class PhaseMinusCodeCycleSlipDetector(AbstractCycleSlipDetector):
    """
    public class PhaseMinusCodeCycleSlipDetector extends :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
    
        Phase minus code cycle slip detectors. The detector is based the algorithm given in Examples of single frequency
        Cycle-Slip Detectors by Zornoza and M. HernÃƒÂ¡ndez-Pajares. Within this class a polynomial is used to smooth the data.
        We consider a cycle_slip occurring if the current measurement is too far from the one predicted with the polynomial
        (algorithm 1 on Navipedia).
    
        For building the detector, one should give a threshold and a gap time limit. After construction of the detectors, one
        can have access to a List of CycleData. Each CycleDate represents a link between the station (define by the RINEX file)
        and a satellite at a specific frequency. For each cycle data, one has access to the begin and end of availability, and a
        sorted set which contains all the date at which cycle-slip have been detected
    
    
        Since:
            10.2
    """
    def __init__(self, double: float, double2: float, int: int, int2: int): ...

class PythonAbstractCycleSlipDetector(AbstractCycleSlipDetector):
    """
    public class PythonAbstractCycleSlipDetector extends :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
    """
    def finalize(self) -> None: ...
    def manageData(self, observationDataSet: org.orekit.gnss.ObservationDataSet) -> None:
        """
            The method is in charge of collecting the measurements, manage them, and call the detection method.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector.manageData`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
        
            Parameters:
                observation (:class:`~org.orekit.gnss.ObservationDataSet`): observation data set
        
        
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

class PythonAbstractDualFrequencyCombination(AbstractDualFrequencyCombination):
    """
    public class PythonAbstractDualFrequencyCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
    """
    def __init__(self, combinationType: CombinationType, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def finalize(self) -> None: ...
    def getCombinedFrequency(self, frequency: org.orekit.gnss.Frequency, frequency2: org.orekit.gnss.Frequency) -> float:
        """
            Get the combined frequency of two measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination.getCombinedFrequency`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
        
            Parameters:
                f1 (:class:`~org.orekit.gnss.Frequency`): frequency of the first measurement
                f2 (:class:`~org.orekit.gnss.Frequency`): frequency of the second measurement
        
            Returns:
                combined frequency in MHz
        
        
        """
        ...
    def getCombinedValue(self, double: float, frequency: org.orekit.gnss.Frequency, double2: float, frequency2: org.orekit.gnss.Frequency) -> float:
        """
            Get the combined observed value of two measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination.getCombinedValue`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
        
            Parameters:
                obs1 (double): observed value of the first measurement
                f1 (:class:`~org.orekit.gnss.Frequency`): frequency of the first measurement
                obs2 (double): observed value of the second measurement
                f2 (:class:`~org.orekit.gnss.Frequency`): frequency of the second measurement
        
            Returns:
                combined observed value
        
        
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

class PythonAbstractLambdaMethod(AbstractLambdaMethod):
    """
    public class PythonAbstractLambdaMethod extends :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
    """
    def __init__(self): ...
    def discreteSearch(self) -> None:
        """
            Find the best solutions to the Integer Least Square problem.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.discreteSearch`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def inverseDecomposition(self) -> None:
        """
            Inverse the decomposition.
        
            This method transforms the LÃ¡Âµâ‚¬.D.L = Q decomposition of covariance into the
            LÃ¢ï¿½Â»Ã‚Â¹.DÃ¢ï¿½Â»Ã‚Â¹.LÃ¢ï¿½Â»Ã¡Âµâ‚¬ = QÃ¢ï¿½Â»Ã‚Â¹ decomposition of the inverse of covariance.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.inverseDecomposition`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
        """
        ...
    def ltdlDecomposition(self) -> None:
        """
            Perform Láµ€.D.L = Q decomposition of the covariance matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.ltdlDecomposition`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
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
    def reduction(self) -> None:
        """
            Perform LAMBDA reduction.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.reduction`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
        """
        ...

class PythonAbstractSingleFrequencyCombination(AbstractSingleFrequencyCombination):
    """
    public class PythonAbstractSingleFrequencyCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination`
    """
    def finalize(self) -> None: ...
    def getCombinedValue(self, double: float, double2: float) -> float:
        """
            Get the combined observed value of two measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination.getCombinedValue`Â in
                classÂ :class:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination`
        
            Parameters:
                phase (double): observed value of the phase measurement
                pseudoRange (double): observed value of the range measurement
        
            Returns:
                combined observed value
        
        
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

class WideLaneCombination(AbstractDualFrequencyCombination):
    """
    public class WideLaneCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
    
        Wide-Lane combination.
    
        This combination are used to create a signal with a significantly wide wavelength. This longer wavelength is useful for
        cycle-slips detection and ambiguity fixing
    
        .. code-block: java
        
        
                      f1 * m1 - f2 * m2
            mWL =  -----------------------
                           f1 - f2
         
        With:
    
          - mWL: Wide-laning measurement.
          - f1 : Frequency of the first measurement.
          - m1 : First measurement.
          - f2 : Frequency of the second measurement.
          - m1 : Second measurement.
    
    
        Wide-Lane combination is a dual frequency combination. The two measurements shall have different frequencies but they
        must have the same :class:`~org.orekit.gnss.MeasurementType`.
    
        Since:
            10.1
    """
    ...

class IntegerBootstrapping(LambdaMethod):
    """
    public class IntegerBootstrapping extends :class:`~org.orekit.estimation.measurements.gnss.LambdaMethod`
    
        Bootstrapping engine for ILS problem solving. This method is base on the following paper: Success probability of integer
        GPs ambiguity rounding and bootstrapping by P. J. G. Teunissen 1998 and Influence of ambiguity precision on the success
        rate of GNSS integer ambiguity bootstrapping by P. J. G. Teunissen 2006.
    
        This method is really faster for integer ambiguity resolution than LAMBDA or MLAMBDA method but its success rate is
        really smaller. The method extends LambdaMethod as it uses LDL' factorization and reduction methods from LAMBDA method.
        The method is really different from LAMBDA as the solution found is not a least-square solution. It is a solution which
        asses a probability of success of the solution found. The probability increase with the does with LDL' factorization and
        reduction methods.
    
        If one want to use this method for integer ambiguity resolution, one just need to construct IntegerBootstrapping only
        with a double which is the minimal probability of success one wants. Then from it, one can call the solveILS method.
    
        Since:
            10.2
    """
    def __init__(self, double: float): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.gnss")``.

    AbstractCycleSlipDetector: typing.Type[AbstractCycleSlipDetector]
    AbstractDualFrequencyCombination: typing.Type[AbstractDualFrequencyCombination]
    AbstractLambdaMethod: typing.Type[AbstractLambdaMethod]
    AbstractSingleFrequencyCombination: typing.Type[AbstractSingleFrequencyCombination]
    AmbiguityAcceptance: typing.Type[AmbiguityAcceptance]
    AmbiguitySolver: typing.Type[AmbiguitySolver]
    CombinationType: typing.Type[CombinationType]
    CycleSlipDetectorResults: typing.Type[CycleSlipDetectorResults]
    CycleSlipDetectors: typing.Type[CycleSlipDetectors]
    GRAPHICCombination: typing.Type[GRAPHICCombination]
    GeometryFreeCombination: typing.Type[GeometryFreeCombination]
    GeometryFreeCycleSlipDetector: typing.Type[GeometryFreeCycleSlipDetector]
    IntegerBootstrapping: typing.Type[IntegerBootstrapping]
    IntegerLeastSquareComparator: typing.Type[IntegerLeastSquareComparator]
    IntegerLeastSquareSolution: typing.Type[IntegerLeastSquareSolution]
    IntegerLeastSquareSolver: typing.Type[IntegerLeastSquareSolver]
    InterSatellitesPhase: typing.Type[InterSatellitesPhase]
    IonosphereFreeCombination: typing.Type[IonosphereFreeCombination]
    LambdaMethod: typing.Type[LambdaMethod]
    MeasurementCombination: typing.Type[MeasurementCombination]
    MeasurementCombinationFactory: typing.Type[MeasurementCombinationFactory]
    MelbourneWubbenaCombination: typing.Type[MelbourneWubbenaCombination]
    ModifiedLambdaMethod: typing.Type[ModifiedLambdaMethod]
    NarrowLaneCombination: typing.Type[NarrowLaneCombination]
    OneWayGNSSPhase: typing.Type[OneWayGNSSPhase]
    OneWayGNSSRange: typing.Type[OneWayGNSSRange]
    Phase: typing.Type[Phase]
    PhaseBuilder: typing.Type[PhaseBuilder]
    PhaseMinusCodeCombination: typing.Type[PhaseMinusCodeCombination]
    PhaseMinusCodeCycleSlipDetector: typing.Type[PhaseMinusCodeCycleSlipDetector]
    PythonAbstractCycleSlipDetector: typing.Type[PythonAbstractCycleSlipDetector]
    PythonAbstractDualFrequencyCombination: typing.Type[PythonAbstractDualFrequencyCombination]
    PythonAbstractLambdaMethod: typing.Type[PythonAbstractLambdaMethod]
    PythonAbstractSingleFrequencyCombination: typing.Type[PythonAbstractSingleFrequencyCombination]
    PythonAmbiguityAcceptance: typing.Type[PythonAmbiguityAcceptance]
    PythonCycleSlipDetectors: typing.Type[PythonCycleSlipDetectors]
    PythonIntegerLeastSquareSolver: typing.Type[PythonIntegerLeastSquareSolver]
    PythonMeasurementCombination: typing.Type[PythonMeasurementCombination]
    SimpleRatioAmbiguityAcceptance: typing.Type[SimpleRatioAmbiguityAcceptance]
    WideLaneCombination: typing.Type[WideLaneCombination]
    WindUp: typing.Type[WindUp]
    WindUpFactory: typing.Type[WindUpFactory]
