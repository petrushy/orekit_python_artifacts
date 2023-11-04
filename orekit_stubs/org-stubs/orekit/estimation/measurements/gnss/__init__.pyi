import java.io
import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.hipparchus.random
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.generation
import org.orekit.files.rinex.observation
import org.orekit.gnss
import org.orekit.propagation.sampling
import org.orekit.time
import org.orekit.utils
import typing



_AbstractWindUp__T = typing.TypeVar('_AbstractWindUp__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractWindUp(org.orekit.estimation.measurements.EstimationModifier[_AbstractWindUp__T], typing.Generic[_AbstractWindUp__T]):
    """
    public abstract class AbstractWindUp<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<T>
    
        Base class for wind-up effect computation.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.https:.gssc.esa.int.navipedia.index.php.Carrier_Phase_Wind`
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modifyWithoutDerivatives(self, estimatedMeasurementBase: org.orekit.estimation.measurements.EstimatedMeasurementBase[_AbstractWindUp__T]) -> None: ...

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
    public class AmbiguitySolver extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
    public enum CombinationType extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.estimation.measurements.gnss.CombinationType`>
    
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
                name (:class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
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

class CombinedObservationData:
    """
    public class CombinedObservationData extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Combined observation data.
    
        Since:
            10.1
    """
    def __init__(self, combinationType: CombinationType, measurementType: org.orekit.gnss.MeasurementType, double: float, double2: float, list: java.util.List[org.orekit.files.rinex.observation.ObservationData]): ...
    def getCombinationType(self) -> CombinationType:
        """
            Get the type of the combination of measurements used to build the instance.
        
            Returns:
                the combination of measurements type
        
        
        """
        ...
    def getCombinedMHzFrequency(self) -> float:
        """
            Get the value of the combined frequency in MHz.
        
            For the single frequency combinations, this method returns the common frequency of both measurements.
        
            Returns:
                value of the combined frequency in MHz
        
        
        """
        ...
    def getMeasurementType(self) -> org.orekit.gnss.MeasurementType:
        """
            Get the measurement type.
        
            Returns:
                measurement type
        
        
        """
        ...
    def getUsedObservationData(self) -> java.util.List[org.orekit.files.rinex.observation.ObservationData]: ...
    def getValue(self) -> float:
        """
            Get the combined observed value.
        
            Returns:
                observed value (may be :code:`Double.NaN` if observation not available)
        
        
        """
        ...

class CombinedObservationDataSet(org.orekit.time.TimeStamped):
    """
    public class CombinedObservationDataSet extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Combined observation data set.
    
        Since:
            10.1
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, list: java.util.List[CombinedObservationData]): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getObservationData(self) -> java.util.List[CombinedObservationData]: ...
    def getPrnNumber(self) -> int:
        """
            Get PRN number.
        
            Returns:
                PRN number of the observed satellite
        
        
        """
        ...
    def getRcvrClkOffset(self) -> float:
        """
            Get receiver clock offset.
        
            Returns:
                receiver clock offset (it is optional, may be 0)
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get Satellite System.
        
            Returns:
                satellite system of observed satellite
        
        
        """
        ...

class CycleSlipDetectorResults:
    """
    public class CycleSlipDetectorResults extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
    def detect(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...

class Dipole:
    """
    public class Dipole extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Dipole configuration for satellite-to-ground and inter-satellites wind-up effects.
    
        The dipole configuration is given by two vectors.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.WindUp`,
            :class:`~org.orekit.estimation.measurements.gnss.InterSatellitesWindUp`
    """
    CANONICAL_I_J: typing.ClassVar['Dipole'] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.Dipole` CANONICAL_I_J
    
        Canonical dipole, with primary vector set to
        :meth:`~org.orekit.estimation.measurements.gnss.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D.html?is`
        and secondary vector set to
        :meth:`~org.orekit.estimation.measurements.gnss.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D.html?is`.
    
    """
    def getPrimary(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the primary dipole vector.
        
            Returns:
                primary dipole vector
        
        
        """
        ...
    def getSecondary(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the secondary dipole vector.
        
            Returns:
                secondary dipole vector
        
        
        """
        ...

class IntegerLeastSquareComparator(java.util.Comparator['IntegerLeastSquareSolution'], java.io.Serializable):
    """
    public class IntegerLeastSquareComparator extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.util.Comparator?is`<:class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolution`>, :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
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
                
                meth:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.util.Comparator.html?is` in
                interface :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.util.Comparator?is`
        
        
        """
        ...

class IntegerLeastSquareSolution:
    """
    public class IntegerLeastSquareSolution extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
                covariance (:class:`~org.orekit.estimation.measurements.gnss.https:.www.hipparchus.org.apidocs.org.hipparchus.linear.RealMatrix?is`): global covariance matrix (includes ambiguities among other parameters)
        
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
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEASUREMENT_TYPE
    
        Type of the measurement.
    
        Also see:
            :meth:`~constant`
    
    
    """
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` AMBIGUITY_NAME
    
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

class InterSatellitesWindUpFactory:
    """
    public class InterSatellitesWindUpFactory extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory for :class:`~org.orekit.estimation.measurements.gnss.InterSatellitesWindUp` modifiers.
    
        The factory ensures the same instance is returned for all emitter/receiver pair, thus preserving phase continuity for
        successive measurements involving the same pair.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def getWindUp(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, dipole: Dipole, satelliteSystem2: org.orekit.gnss.SatelliteSystem, int2: int, dipole2: Dipole) -> 'InterSatellitesWindUp':
        """
            Get a modifier for an emitter/receiver pair.
        
            Parameters:
                emitterSystem (:class:`~org.orekit.gnss.SatelliteSystem`): system the emitter satellite belongs to
                emitterPrnNumber (int): emitter satellite PRN number
                emitterDipole (:class:`~org.orekit.estimation.measurements.gnss.Dipole`): emitter dipole
                receiverSystem (:class:`~org.orekit.gnss.SatelliteSystem`): system the receiver satellite belongs to
                receiverPrnNumber (int): receiver satellite PRN number
                receiverDipole (:class:`~org.orekit.estimation.measurements.gnss.Dipole`): receiver dipole
        
            Returns:
                modifier for the emitter/receiver pair
        
        
        """
        ...

class MeasurementCombination:
    """
    public interface MeasurementCombination
    
        Interface for combination of measurements.
    
        Since:
            10.1
    """
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Parameters:
                observations (:class:`~org.orekit.files.rinex.observation.ObservationDataSet`): observation data set
        
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
    public class MeasurementCombinationFactory extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
            Get the Melbourne-Wübbena combination of measurements.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                Melbourne-Wübbena combination
        
        
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
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEASUREMENT_TYPE
    
        Type of the measurement.
    
        Also see:
            :meth:`~constant`
    
    
    """
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` AMBIGUITY_NAME
    
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
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEASUREMENT_TYPE
    
        Type of the measurement.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...

class Phase(org.orekit.estimation.measurements.GroundReceiverMeasurement['Phase']):
    """
    public class Phase extends :class:`~org.orekit.estimation.measurements.GroundReceiverMeasurement`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modeling a phase measurement from a ground station.
    
        The measurement is considered to be a signal emitted from a spacecraft and received on a ground station. Its value is
        the number of cycles between emission and reception. The motion of both the station and the spacecraft during the signal
        flight time are taken into account. The date of the measurement corresponds to the reception on ground of the emitted
        signal.
    
        Since:
            9.2
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEASUREMENT_TYPE
    
        Type of the measurement.
    
        Also see:
            :meth:`~constant`
    
    
    """
    AMBIGUITY_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` AMBIGUITY_NAME
    
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
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> Phase: ...

class WindUpFactory:
    """
    public class WindUpFactory extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory for :class:`~org.orekit.estimation.measurements.gnss.WindUp` modifiers.
    
        The factory ensures the same instance is returned for all satellite/receiver pair, thus preserving phase continuity for
        successive measurements involving the same pair.
    
        Since:
            10.1
    """
    def __init__(self): ...
    def getWindUp(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, dipole: Dipole, string: str) -> 'WindUp':
        """
            Get a modifier for a satellite/receiver pair.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): system the satellite belongs to
                prnNumber (int): PRN number
                emitterDipole (:class:`~org.orekit.estimation.measurements.gnss.Dipole`): emitter dipole
                receiverName (:class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the receiver
        
            Returns:
                modifier for the satellite/receiver pair
        
        
        """
        ...

class AbstractCycleSlipDetector(CycleSlipDetectors):
    """
    public abstract class AbstractCycleSlipDetector extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.CycleSlipDetectors`
    
        Base class for cycle-slip detectors.
    
        Since:
            10.2
    """
    def detect(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...

class AbstractDualFrequencyCombination(MeasurementCombination):
    """
    public abstract class AbstractDualFrequencyCombination extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    
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
    def combine(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData) -> CombinedObservationData:
        """
            Combines observation data using a dual frequency combination of measurements.
        
            Parameters:
                od1 (:class:`~org.orekit.files.rinex.observation.ObservationData`): first observation data to combined
                od2 (:class:`~org.orekit.files.rinex.observation.ObservationData`): second observation data to combined
        
            Returns:
                a combined observation data
        
        """
        ...
    @typing.overload
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.files.rinex.observation.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Returns:
                name of the combination of measurements
        
        
        """
        ...

class AbstractLambdaMethod(IntegerLeastSquareSolver):
    """
    public abstract class AbstractLambdaMethod extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
    
        Base class for decorrelation/reduction engine for LAMBDA type methods.
    
        This class is based on both the 1996 paper
        :class:`~org.orekit.estimation.measurements.gnss.https:.www.researchgate.net.publication.2790708_The_LAMBDA_method_for_integer_ambiguity_estimation_implementation_aspects`
        by Paul de Jonge and Christian Tiberius and on the 2005 paper
        :class:`~org.orekit.estimation.measurements.gnss.https:.www.researchgate.net.publication.225518977_MLAMBDA_a_modified_LAMBDA_method_for_integer_least`
        by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
        Since:
            10.0
    """
    def setComparator(self, comparator: typing.Union[java.util.Comparator[IntegerLeastSquareSolution], typing.Callable[[IntegerLeastSquareSolution, IntegerLeastSquareSolution], int]]) -> None: ...
    def solveILS(self, int: int, doubleArray: typing.List[float], intArray: typing.List[int], realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[IntegerLeastSquareSolution]:
        """
            Find the best solutions to an Integer Least Square problem.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver.solveILS` in
                interface :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
        
            Parameters:
                nbSol (int): number of solutions to search for
                floatAmbiguities (double[]): float estimates of ambiguities
                indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
                covariance (:class:`~org.orekit.estimation.measurements.gnss.https:.www.hipparchus.org.apidocs.org.hipparchus.linear.RealMatrix?is`): global covariance matrix (includes ambiguities among other parameters)
        
            Returns:
                at most :code:`nbSol` solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

class AbstractSingleFrequencyCombination(MeasurementCombination):
    """
    public abstract class AbstractSingleFrequencyCombination extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    
        Base class for single frequency combination of measurements.
    
        Since:
            10.1
    """
    @typing.overload
    def combine(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData) -> CombinedObservationData:
        """
            Combines observation data using a single frequency combination of measurements.
        
            Parameters:
                phase (:class:`~org.orekit.files.rinex.observation.ObservationData`): phase measurement
                pseudoRange (:class:`~org.orekit.files.rinex.observation.ObservationData`): pseudoRange measurement
        
            Returns:
                a combined observation data
        
        
        """
        ...
    @typing.overload
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.files.rinex.observation.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Returns:
                name of the combination of measurements
        
        
        """
        ...

class InterSatellitesWindUp(AbstractWindUp[InterSatellitesPhase]):
    """
    public class InterSatellitesWindUp extends :class:`~org.orekit.estimation.measurements.gnss.AbstractWindUp`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Modifier for wind-up effect in GNSS :class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.InterSatellitesWindUpFactory`
    """
    ...

class MelbourneWubbenaCombination(MeasurementCombination):
    """
    public class MelbourneWubbenaCombination extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    
        Melbourne-Wübbena combination.
    
        This combination allows, thanks to the wide-lane combination, a larger wavelength than each signal individually.
        Moreover, the measurement noise is reduced by the narrow-lane combination of code measurements.
    
        .. code-block: java
        
            mMW =  ΦWL- RNL
            mMW =  λWL * NWL+ b + ε
         
        With:
    
          - mMW : Melbourne-Wübbena measurement.
          - ΦWL : Wide-Lane phase measurement.
          - RNL : Narrow-Lane code measurement.
          - λWL : Wide-Lane wavelength.
          - NWL : Wide-Lane ambiguity (Nf1 - Nf2).
          - b : Satellite and receiver instrumental delays.
          - ε : Measurement noise.
    
    
        :class:`~org.orekit.estimation.measurements.gnss.NarrowLaneCombination` and
        :class:`~org.orekit.estimation.measurements.gnss.WideLaneCombination` combinations shall be performed with the same pair
        of frequencies.
    
        Since:
            10.1
    
        Also see:
            "Detector based in code and carrier phase data: The Melbourne-Wübbena combination, J. Sanz Subirana, J.M. Juan Zornoza
            and M. Hernández-Pajares, 2011"
    """
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.files.rinex.observation.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Returns:
                name of the combination of measurements
        
        
        """
        ...

_PythonAbstractWindUp__T = typing.TypeVar('_PythonAbstractWindUp__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractWindUp(AbstractWindUp[_PythonAbstractWindUp__T], typing.Generic[_PythonAbstractWindUp__T]):
    """
    public class PythonAbstractWindUp<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.gnss.AbstractWindUp`<T>
    """
    def __init__(self, dipole: Dipole, dipole2: Dipole): ...
    def emitterToInert(self, estimatedMeasurementBase: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractWindUp__T]) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
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
    def receiverToInert(self, estimatedMeasurementBase: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractWindUp__T]) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...

class PythonAmbiguityAcceptance(AmbiguityAcceptance):
    """
    public class PythonAmbiguityAcceptance extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
    """
    def __init__(self): ...
    def accept(self, integerLeastSquareSolutionArray: typing.List[IntegerLeastSquareSolution]) -> IntegerLeastSquareSolution:
        """
            Check if one of the candidate solutions can be accepted.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.accept` in
                interface :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
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
                :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.numberOfCandidates` in
                interface :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
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
    public class PythonCycleSlipDetectors extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.CycleSlipDetectors`
    """
    def __init__(self): ...
    def detect(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]: ...
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
    public class PythonIntegerLeastSquareSolver extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
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
                :meth:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver.solveILS` in
                interface :class:`~org.orekit.estimation.measurements.gnss.IntegerLeastSquareSolver`
        
            Parameters:
                nbSol (int): number of solutions to search for
                floatAmbiguities (double[]): float estimates of ambiguities
                indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
                covariance (:class:`~org.orekit.estimation.measurements.gnss.https:.www.hipparchus.org.apidocs.org.hipparchus.linear.RealMatrix?is`): global covariance matrix (includes ambiguities among other parameters)
        
            Returns:
                at most :code:`nbSol` solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

class PythonMeasurementCombination(MeasurementCombination):
    """
    public class PythonMeasurementCombination extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
    """
    def __init__(self): ...
    def combine(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
            Combines observation data using a combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.combine` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
            Parameters:
                observations (:class:`~org.orekit.files.rinex.observation.ObservationDataSet`): observation data set
        
            Returns:
                a combined observation data set
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getName(self) -> str:
        """
            Get the name of the combination of measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.MeasurementCombination.getName` in
                interface :class:`~org.orekit.estimation.measurements.gnss.MeasurementCombination`
        
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
    public class SimpleRatioAmbiguityAcceptance extends :class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
    
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
                :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.accept` in
                interface :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
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
                :meth:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance.numberOfCandidates` in
                interface :class:`~org.orekit.estimation.measurements.gnss.AmbiguityAcceptance`
        
            Returns:
                number of candidate solutions to search for
        
        
        """
        ...

class WindUp(AbstractWindUp[Phase]):
    """
    public class WindUp extends :class:`~org.orekit.estimation.measurements.gnss.AbstractWindUp`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Modifier for wind-up effect in GNSS :class:`~org.orekit.estimation.measurements.gnss.Phase`.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.estimation.measurements.gnss.WindUpFactory`
    """
    ...

class GRAPHICCombination(AbstractSingleFrequencyCombination):
    """
    public class GRAPHICCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination`
    
        GRoup And Phase Ionospheric Calibration (GRAPHIC) combination.
    
        This combination is a ionosphere-free single frequency combination of measurements.
    
        .. code-block: java
        
            mf =  0.5 * (Φf + Rf)
         
        With:
    
          - mf : GRAPHIC measurement.
          - Φf : Phase measurement.
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
    
        Geometry free cycle slip detectors. The detector is based the algorithm given in
        :class:`~org.orekit.estimation.measurements.gnss.https:.gssc.esa.int.navipedia.index.php.Detector_based_in_carrier_phase_data:_The_geometry`
        by Zornoza and M. Hernández-Pajares. Within this class a second order polynomial is used to smooth the data. We
        consider a cycle-slip occurring if the current measurement is too far from the one predicted with the polynomial.
    
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
        
                     f1² * m1 - f2² * m2
            mIF =  -----------------------
                          f1² - f2²
         
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
        both the 1996 paper
        :class:`~org.orekit.estimation.measurements.gnss.https:.www.researchgate.net.publication.2790708_The_LAMBDA_method_for_integer_ambiguity_estimation_implementation_aspects`
        by Paul de Jonge and Christian Tiberius and on the 2005 paper
        :class:`~org.orekit.estimation.measurements.gnss.https:.www.researchgate.net.publication.225518977_MLAMBDA_a_modified_LAMBDA_method_for_integer_least`
        by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
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
    
        This class implements Modified Least Square Ambiguity Decorrelation Adjustment (MLAMBDA) method, as described in
        :class:`~org.orekit.estimation.measurements.gnss.https:.www.researchgate.net.publication.225518977_MLAMBDA_a_modified_LAMBDA_method_for_integer_least`
        by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
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
        
            mf =  Φf - Rf
         
        With:
    
          - mf : Phase minus Code measurement.
          - Φf : Phase measurement.
          - Rf : Code measurement.
          - f : Frequency.
    
    
        Since:
            10.1
    """
    ...

class PhaseMinusCodeCycleSlipDetector(AbstractCycleSlipDetector):
    """
    public class PhaseMinusCodeCycleSlipDetector extends :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
    
        Phase minus code cycle slip detectors. The detector is based the algorithm given in
        :class:`~org.orekit.estimation.measurements.gnss.https:.gssc.esa.int.navipedia.index.php.Examples_of_single_frequency_Cycle`
        by Zornoza and M. Hernández-Pajares. Within this class a polynomial is used to smooth the data. We consider a
        cycle_slip occurring if the current measurement is too far from the one predicted with the polynomial (algorithm 1 on
        Navipedia).
    
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
    def cycleSlipDataSet(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float, frequency: org.orekit.gnss.Frequency) -> None:
        """
            Set the data: collect data at the current Date, at the current frequency, for a given satellite, add it within the
            attributes data and stuff.
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector.cycleSlipDataSet` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
        
            Parameters:
                nameSat (:class:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the satellite (e.g. "GPS - 7")
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the measurement
                value (double): measurement at the current date
                freq (:class:`~org.orekit.gnss.Frequency`): frequency used
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getMaxTimeBeetween2Measurement(self) -> float:
        """
            Get the maximum time lapse between 2 measurements without considering a cycle-slip has occurring between both.
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector.getMaxTimeBeetween2Measurement` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
        
            Returns:
                the maximum time lapse between 2 measurements
        
        
        """
        ...
    def getMinMeasurementNumber(self) -> int:
        """
            Get the minimum number of measurement needed before being able to figure out cycle-slip occurrence.
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector.getMinMeasurementNumber` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
        
            Returns:
                the minimum number of measurement needed before being able to figure out cycle-slip occurrence.
        
        
        """
        ...
    def getResults(self) -> java.util.List[CycleSlipDetectorResults]: ...
    def getStuffReference(self) -> java.util.List[java.util.Map[org.orekit.gnss.Frequency, 'AbstractCycleSlipDetector.DataForDetection']]: ...
    def manageData(self, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet) -> None:
        """
            The method is in charge of collecting the measurements, manage them, and call the detection method.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector.manageData` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
        
            Parameters:
                observation (:class:`~org.orekit.files.rinex.observation.ObservationDataSet`): observation data set
        
        
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
    def setName(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> str:
        """
            Create the name of a satellite from its PRN number and satellite System it belongs to.
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector.setName` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractCycleSlipDetector`
        
            Parameters:
                numSat (int): satellite PRN number
                sys (:class:`~org.orekit.gnss.SatelliteSystem`): Satellite System of the satellite
        
            Returns:
                the satellite name on a specified format (e.g.: "GPS - 7")
        
        
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
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination.getCombinedFrequency` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
        
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
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination.getCombinedValue` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractDualFrequencyCombination`
        
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
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.discreteSearch` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def inverseDecomposition(self) -> None:
        """
            Inverse the decomposition.
        
            This method transforms the Lᵀ.D.L = Q decomposition of covariance into the L⁻¹.D⁻¹.L⁻ᵀ = Q⁻¹
            decomposition of the inverse of covariance.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.inverseDecomposition` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
        """
        ...
    def ltdlDecomposition(self) -> None:
        """
            Perform Lᵀ.D.L = Q decomposition of the covariance matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.ltdlDecomposition` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
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
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod.reduction` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractLambdaMethod`
        
        
        """
        ...

class PythonAbstractSingleFrequencyCombination(AbstractSingleFrequencyCombination):
    """
    public class PythonAbstractSingleFrequencyCombination extends :class:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination`
    """
    def __init__(self, combinationType: CombinationType, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def finalize(self) -> None: ...
    def getCombinedValue(self, double: float, double2: float) -> float:
        """
            Get the combined observed value of two measurements.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination.getCombinedValue` in
                class :class:`~org.orekit.estimation.measurements.gnss.AbstractSingleFrequencyCombination`
        
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
    
        Bootstrapping engine for ILS problem solving. This method is base on the following paper:
        :class:`~org.orekit.estimation.measurements.gnss.https:.www.researchgate.net.publication.225773077_Success_probability_of_integer_GPS_ambiguity_rounding_and_bootstrapping`
        by P. J. G. Teunissen 1998 and
        :class:`~org.orekit.estimation.measurements.gnss.https:.repository.tudelft.nl.islandora.object.uuid%3A1a5b8a6e` by P. J.
        G. Teunissen 2006.
    
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
    AbstractWindUp: typing.Type[AbstractWindUp]
    AmbiguityAcceptance: typing.Type[AmbiguityAcceptance]
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
    PythonAbstractWindUp: typing.Type[PythonAbstractWindUp]
    PythonAmbiguityAcceptance: typing.Type[PythonAmbiguityAcceptance]
    PythonCycleSlipDetectors: typing.Type[PythonCycleSlipDetectors]
    PythonIntegerLeastSquareSolver: typing.Type[PythonIntegerLeastSquareSolver]
    PythonMeasurementCombination: typing.Type[PythonMeasurementCombination]
    SimpleRatioAmbiguityAcceptance: typing.Type[SimpleRatioAmbiguityAcceptance]
    WideLaneCombination: typing.Type[WideLaneCombination]
    WindUp: typing.Type[WindUp]
    WindUpFactory: typing.Type[WindUpFactory]
