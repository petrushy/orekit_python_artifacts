
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.hipparchus.random
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.generation
import org.orekit.files.rinex.observation
import org.orekit.gnss
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



_AbstractOnBoardMeasurement__T = typing.TypeVar('_AbstractOnBoardMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractOnBoardMeasurement(org.orekit.estimation.measurements.AbstractMeasurement[_AbstractOnBoardMeasurement__T], typing.Generic[_AbstractOnBoardMeasurement__T]):
    """
    Base class modeling a measurement where receiver is a satellite.
    
    Since:
        12.1
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, observed: float, sigma: float, baseWeight: float, satellites: java.util.List[org.orekit.estimation.measurements.ObservableSatellite]):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): date of the measurement
            observed (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellites (List<ObservableSatellite> satellites): satellites related to this measurement
        
        
        """
        ...

_AbstractWindUp__T = typing.TypeVar('_AbstractWindUp__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractWindUp(org.orekit.estimation.measurements.EstimationModifier[_AbstractWindUp__T], typing.Generic[_AbstractWindUp__T]):
    """
    Base class for wind-up effect computation.
    
    Since:
        12.0
    
    Also see:
        Carrier_Phase_Wind
    """
    def cacheAngularWindUp(self, participants: typing.Union[typing.List[org.orekit.utils.TimeStampedPVCoordinates], jpype.JArray], receiverToInert: org.hipparchus.geometry.euclidean.threed.Rotation, emitterToInert: org.hipparchus.geometry.euclidean.threed.Rotation) -> None:
        """
        Cache angular wind-up.
        
        Parameters:
            participants (TimeStampedPVCoordinates[]): particpants to the carrier-phase measurement
            receiverToInert (Rotation): rotation for receiver to inertial frame
            emitterToInert (Rotation): rotation from emitter to inertial frame
        
        Since:
            13.0
        
        
        """
        ...
    def getAngularWindUp(self) -> float:
        """
        Get cached value of angular wind-up.
        
        Returns:
            cached value of angular wind-up
        
        Since:
            13.0
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Wind-up effect has no parameters, the returned list is always empty.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_AbstractWindUp__T]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<AbstractWindUp> estimated): estimated measurement to modify
        
        
        """
        ...
    def setAngularWindUp(self, angularWindUp: float) -> None:
        """
        Set cached value of angular wind-up.
        
        Parameters:
            angularWindUp (double): angular wind-up value
        
        Since:
            13.1
        
        
        """
        ...

class AmbiguityAcceptance:
    """
    Interface defining ambiguity acceptance tests.
    
    Since:
        10.0
    
    Also see:
        AmbiguitySolver
    """
    def accept(self, candidates: typing.Union[typing.List['IntegerLeastSquareSolution'], jpype.JArray]) -> 'IntegerLeastSquareSolution':
        """
        Check if one of the candidate solutions can be accepted.
        
        Parameters:
            candidates (IntegerLeastSquareSolution[]): candidate solutions of the Integer Least Squares problem, in increasing squared distance order (the array contains at
                least numberOfCandidates candidates)
        
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

class AmbiguityCache:
    """
    Cache for AmbiguityDriver.
    
    Since:
        12.1
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getAmbiguity(self, emitter: str, receiver: str, wavelength: float) -> 'AmbiguityDriver':
        """
        Get a cached driver for ambiguity.
        
        A new parameter driver is created and cached the first time an emitter/receiver/wavelength triplet is used; after that, the cached driver will be returned when the same triplet is passed again
        
        Parameters:
            emitter (String): emitter id
            receiver (String): receiver id
            wavelength (double): signal wavelength
        
        Returns:
            parameter driver for the emitter/receiver/wavelength triplet
        
        
        """
        ...

class AmbiguityDriver(org.orekit.utils.ParameterDriver):
    """
    Specialized ParameterDriver for ambiguity.
    
    Since:
        12.1
    """
    PREFIX: typing.ClassVar[str] = ...
    """
    Prefix for parameter drivers names.
    
    Also see:
        constant
    
    
    """
    def __init__(self, emitter: str, receiver: str, wavelength: float):
        """
        Simple constructor.
        
        Parameters:
            emitter (String): emitter id
            receiver (String): receiver id
            wavelength (double): signal wavelength
        
        
        """
        ...
    def getEmitter(self) -> str:
        """
        Get emitter id.
        
        Returns:
            emitter id
        
        
        """
        ...
    def getReceiver(self) -> str:
        """
        Get receiver id.
        
        Returns:
            receiver id
        
        
        """
        ...
    def getWavelength(self) -> float:
        """
        Get signal wavelength.
        
        Returns:
            signal wavelength
        
        
        """
        ...

class AmbiguitySolver:
    """
    Class for solving integer ambiguity problems.
    
    Since:
        10.0
    
    Also see:
        LambdaMethod
    """
    def __init__(self, ambiguityDrivers: java.util.List[org.orekit.utils.ParameterDriver], solver: typing.Union['IntegerLeastSquareSolver', typing.Callable], acceptance: AmbiguityAcceptance):
        """
        Simple constructor.
        
        Parameters:
            ambiguityDrivers (List<ParameterDriver> ambiguityDrivers): drivers for ambiguity parameters
            solver (IntegerLeastSquareSolver): solver for the underlying Integer Least Square problem
            acceptance (AmbiguityAcceptance): acceptance test to use
        
        Also see:
            LambdaMethod
        
        
        """
        ...
    def fixIntegerAmbiguities(self, startIndex: int, measurementsParametersDrivers: java.util.List[org.orekit.utils.ParameterDriver], covariance: org.hipparchus.linear.RealMatrix) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Fix integer ambiguities.
        
        Parameters:
            startIndex (int): start index for measurements parameters in global covariance matrix
            measurementsParametersDrivers (List<ParameterDriver> measurementsParametersDrivers): measurements parameters drivers in global covariance matrix order
            covariance (RealMatrix): global covariance matrix
        
        Returns:
            list of newly fixed ambiguities (ambiguities already fixed before the call are not counted)
        
        
        """
        ...
    def getAllAmbiguityDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get all the ambiguity parameters drivers.
        
        Returns:
            all ambiguity parameters drivers
        
        
        """
        ...
    def unFixAmbiguity(self, ambiguityDriver: org.orekit.utils.ParameterDriver) -> None:
        """
        Un-fix an integer ambiguity (typically after a phase cycle slip).
        
        Parameters:
            ambiguityDriver (ParameterDriver): driver for the ambiguity to un-fix
        
        
        """
        ...

class CombinationType(java.lang.Enum['CombinationType']):
    """
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
    def valueOf(name: str) -> 'CombinationType':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['CombinationType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CombinationType c : CombinationType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CombinedObservationData:
    """
    Combined observation data.
    
    Since:
        10.1
    """
    def __init__(self, combinedValue: float, combinedFrequency: float, combinationType: CombinationType, measurementType: org.orekit.gnss.MeasurementType, usedData: java.util.List[org.orekit.files.rinex.observation.ObservationData]):
        """
        Constructor.
        
        Parameters:
            combinedValue (double): combined observed value (may be NaN if combined observation not available)
            combinedFrequency (double): frequency of the combined observation data in Hz (may be NaN if combined frequency is not available)
            combinationType (CombinationType): combination of measurements used to build the combined observation data
            measurementType (MeasurementType): measurement type used for the combination of measurement
            usedData (List<ObservationData> usedData): observation data used to perform the combination of measurements
        
        Since:
            12.1
        
        
        """
        ...
    def getCombinationType(self) -> CombinationType:
        """
        Get the type of the combination of measurements used to build the instance.
        
        Returns:
            the combination of measurements type
        
        
        """
        ...
    def getCombinedFrequency(self) -> float:
        """
        Get the value of the combined frequency in MHz.
        
        For the single frequency combinations, this method returns the common frequency of both measurements.
        
        Returns:
            value of the combined frequency in Hz
        
        Since:
            12.1
        
        
        """
        ...
    def getMeasurementType(self) -> org.orekit.gnss.MeasurementType:
        """
        Get the measurement type.
        
        Returns:
            measurement type
        
        
        """
        ...
    def getUsedObservationData(self) -> java.util.List[org.orekit.files.rinex.observation.ObservationData]:
        """
        Get the list of observation data used to perform the combination of measurements.
        
        Returns:
            a list of observation data
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Get the combined observed value.
        
        Returns:
            observed value (may be NaN if observation not available)
        
        
        """
        ...

class CombinedObservationDataSet(org.orekit.time.TimeStamped):
    """
    Combined observation data set.
    
    Since:
        10.1
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, prnNumber: int, tObs: org.orekit.time.AbsoluteDate, rcvrClkOffset: float, observationData: java.util.List[CombinedObservationData]):
        """
        Simple constructor.
        
        Parameters:
            satelliteSystem (SatelliteSystem): Satellite system
            prnNumber (int): PRN number
            tObs (AbsoluteDate): Observation date
            rcvrClkOffset (double): Receiver clock offset (optional, 0 by default)
            observationData (List<CombinedObservationData> observationData): List of combined observation data
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getObservationData(self) -> java.util.List[CombinedObservationData]:
        """
        Get list of observation data.
        
        Returns:
            unmodifiable view of of observation data for the observed satellite
        
        
        """
        ...
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
    This class is used to contains all the data computed within cycle-slip detector. All these parameters are what user can get from the detectors.
    
    Since:
        10.2
    """
    def getBeginDate(self, signal: org.orekit.gnss.GnssSignal) -> org.orekit.time.AbsoluteDate:
        """
        Return the date of validity beginning of the detector.
        
        Parameters:
            signal (GnssSignal): frequency
        
        Returns:
            AbsoluteDate
        
        
        """
        ...
    def getCycleSlipMap(self) -> java.util.Map[org.orekit.gnss.GnssSignal, java.util.List[org.orekit.time.AbsoluteDate]]:
        """
        Get the cycle slip Map with contains the results.
        
        For dual-Frequency cycle-slip detector, the GnssSignal contained in the map is the higher frequency (e.g. for L1-L2 the signal in the map will be L1)
        
        Returns:
            cycle slip map containing the results
        
        
        """
        ...
    def getEndDate(self, signal: org.orekit.gnss.GnssSignal) -> org.orekit.time.AbsoluteDate:
        """
        Return the end date at the given frequency.
        
        For dual-Frequency cycle-slip detector, the GnssSignal contained in the map is the higher frequency (e.g. for L1-L2 the signal in the map will be L1)
        
        Parameters:
            signal (GnssSignal): frequency
        
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
    Interface for phase measurement cycle-slip detection.
    
    Since:
        10.2
    """
    def detect(self, observations: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]:
        """
        Detects if a cycle-slip occurs for a given list of observation data set.
        
        Parameters:
            observations (List<ObservationDataSet> observations): list of observation data set
        
        Returns:
            a list of results computed by the cycle-slip detectors
        
        
        """
        ...

class Dipole:
    """
    Dipole configuration for satellite-to-ground and inter-satellites wind-up effects.
    
    The dipole configuration is given by two vectors.
    
    Since:
        12.0
    
    Also see:
        WindUp,
        InterSatellitesWindUp
    """
    CANONICAL_I_J: typing.ClassVar['Dipole'] = ...
    """
    Canonical dipole, with primary vector set to Vector3D and secondary vector set to Vector3D.
    """
    def __init__(self, primary: org.hipparchus.geometry.euclidean.threed.Vector3D, secondary: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Simple constructor.
        
        Parameters:
            primary (Vector3D): primary dipole vector
            secondary (Vector3D): secondary dipole vector
        
        
        """
        ...
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
    Comparator for IntegerLeastSquareSolution instance.
    
    Since:
        11.0
    
    Also see:
        IntegerLeastSquareSolution, serialized
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def compare(self, ilss1: 'IntegerLeastSquareSolution', ilss2: 'IntegerLeastSquareSolution') -> int:
        """
        The comparison is based on the squared distance to the float solution.
        
        Specified by: meth:`~org.orekit.estimation.measurements.gnss.https:.docs.oracle.com.javase.8.docs.api.java.util.Comparator.html?is` in interface Comparator
        
        
        """
        ...

class IntegerLeastSquareSolution:
    """
    Class holding a solution to an Integer Least Square problem.
    
    Since:
        10.0
    """
    def __init__(self, solution: typing.Union[typing.List[int], jpype.JArray], d2: float):
        """
        Simple constructor.
        
        Parameters:
            solution (long[]): solution array
            d2 (double): squared distance to the corresponding float solution
        
        
        """
        ...
    def getSolution(self) -> typing.MutableSequence[int]:
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
    Interface for algorithms solving integer least square problems.
    
    Since:
        10.0
    
    Also see:
        IntegerLeastSquareSolution
    """
    def solveILS(self, nbSol: int, floatAmbiguities: typing.Union[typing.List[float], jpype.JArray], indirection: typing.Union[typing.List[int], jpype.JArray], covariance: org.hipparchus.linear.RealMatrix) -> typing.MutableSequence[IntegerLeastSquareSolution]:
        """
        Find the best solutions to an Integer Least Square problem.
        
        Parameters:
            nbSol (int): number of solutions to search for
            floatAmbiguities (double[]): float estimates of ambiguities
            indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
            covariance (RealMatrix): global covariance matrix (includes ambiguities among other parameters)
        
        Returns:
            at most nbSol solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

class InterSatellitesWindUpFactory:
    """
    Factory for InterSatellitesWindUp modifiers.
    
    The factory ensures the same instance is returned for all emitter/receiver pair, thus preserving phase continuity for successive measurements involving the same pair.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getWindUp(self, emitterSystem: org.orekit.gnss.SatelliteSystem, emitterPrnNumber: int, emitterDipole: Dipole, receiverSystem: org.orekit.gnss.SatelliteSystem, receiverPrnNumber: int, receiverDipole: Dipole) -> 'InterSatellitesWindUp':
        """
        Get a modifier for an emitter/receiver pair.
        
        Parameters:
            emitterSystem (SatelliteSystem): system the emitter satellite belongs to
            emitterPrnNumber (int): emitter satellite PRN number
            emitterDipole (Dipole): emitter dipole
            receiverSystem (SatelliteSystem): system the receiver satellite belongs to
            receiverPrnNumber (int): receiver satellite PRN number
            receiverDipole (Dipole): receiver dipole
        
        Returns:
            modifier for the emitter/receiver pair
        
        
        """
        ...

class MeasurementCombination:
    """
    Interface for combination of measurements.
    
    Since:
        10.1
    """
    def combine(self, observations: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
        Combines observation data using a combination of measurements.
        
        Parameters:
            observations (ObservationDataSet): observation data set
        
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
    Factory for predefined combination of measurements.
    
    This is a utility class, so its constructor is private.
    
    Since:
        10.1
    """
    @staticmethod
    def getGRAPHICCombination(system: org.orekit.gnss.SatelliteSystem) -> 'GRAPHICCombination':
        """
        Get the GRAPHIC combination of measurements.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            phase minus code combination
        
        
        """
        ...
    @staticmethod
    def getGeometryFreeCombination(system: org.orekit.gnss.SatelliteSystem) -> 'GeometryFreeCombination':
        """
        Get the Geometry-Free combination of measurements.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            Geometry-Free combination
        
        
        """
        ...
    @staticmethod
    def getIonosphereFreeCombination(system: org.orekit.gnss.SatelliteSystem) -> 'IonosphereFreeCombination':
        """
        Get the Ionosphere-Free combination of measurements.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            Ionosphere-Lane combination
        
        
        """
        ...
    @staticmethod
    def getMelbourneWubbenaCombination(system: org.orekit.gnss.SatelliteSystem) -> 'MelbourneWubbenaCombination':
        """
        Get the Melbourne-Wübbena combination of measurements.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            Melbourne-Wübbena combination
        
        
        """
        ...
    @staticmethod
    def getNarrowLaneCombination(system: org.orekit.gnss.SatelliteSystem) -> 'NarrowLaneCombination':
        """
        Get the Narrow-Lane combination of measurements.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            Narrow-Lane combination
        
        
        """
        ...
    @staticmethod
    def getPhaseMinusCodeCombination(system: org.orekit.gnss.SatelliteSystem) -> 'PhaseMinusCodeCombination':
        """
        Get the phase minus code combination of measurements.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            phase minus code combination
        
        
        """
        ...
    @staticmethod
    def getWideLaneCombination(system: org.orekit.gnss.SatelliteSystem) -> 'WideLaneCombination':
        """
        Get the Wide-Lane combination of measurements.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            Wide-Lane combination
        
        
        """
        ...

class OnBoardCommonParametersWithDerivatives(org.orekit.estimation.measurements.CommonParametersWithDerivatives):
    """
    Common intermediate parameters used to estimate measurements where receiver is a satellite.
    
    Since:
        12.1
    """
    def __init__(self, localState: org.orekit.propagation.SpacecraftState, indices: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]], localOffset: org.hipparchus.analysis.differentiation.Gradient, localRate: org.hipparchus.analysis.differentiation.Gradient, remoteOffset: org.hipparchus.analysis.differentiation.Gradient, remoteRate: org.hipparchus.analysis.differentiation.Gradient, tauD: org.hipparchus.analysis.differentiation.Gradient, localPV: org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient], remotePV: org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]):
        """
        Simple constructor.
        
        Parameters:
            localState (SpacecraftState): local spacecraft state
            indices (Map<String, Integer> indices): derivatives indices map
            localOffset (Gradient): local clock offset
            localRate (Gradient): local clock rate
            remoteOffset (Gradient): remote clock offset
            remoteRate (Gradient): remote clock rate
            tauD (Gradient): downlink delay
            localPV (TimeStampedFieldPVCoordinates<Gradient> localPV): local satellite position/velocity
            remotePV (TimeStampedFieldPVCoordinates<Gradient> remotePV): remote satellite position/velocity
        
        
        """
        ...
    def getLocalOffset(self) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Get local clock offset.
        
        Returns:
            local clock offset
        
        
        """
        ...
    def getLocalRate(self) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Get local clock rate.
        
        Returns:
            local clock rate
        
        
        """
        ...
    def getRemoteOffset(self) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Get remote clock offset.
        
        Returns:
            remote clock offset
        
        
        """
        ...
    def getRemotePV(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get remote satellite position/velocity.
        
        Returns:
            remote satellite position/velocity
        
        
        """
        ...
    def getRemoteRate(self) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Get remote clock rate.
        
        Returns:
            remote clock rate
        
        
        """
        ...

class OnBoardCommonParametersWithoutDerivatives(org.orekit.estimation.measurements.CommonParametersWithoutDerivatives):
    """
    Common intermediate parameters used to estimate measurements where receiver is a satellite.
    
    Since:
        12.1
    """
    def __init__(self, localState: org.orekit.propagation.SpacecraftState, localOffset: float, localRate: float, remoteOffset: float, remoteRate: float, tauD: float, localPV: org.orekit.utils.TimeStampedPVCoordinates, remotePV: org.orekit.utils.TimeStampedPVCoordinates):
        """
        Simple constructor.
        
        Parameters:
            localState (SpacecraftState): local spacecraft state
            localOffset (double): local clock offset
            localRate (double): local clock rate
            remoteOffset (double): remote clock offset
            remoteRate (double): remote clock rate
            tauD (double): downlink delay
            localPV (TimeStampedPVCoordinates): local satellite position/velocity
            remotePV (TimeStampedPVCoordinates): remote satellite position/velocity
        
        
        """
        ...
    def getLocalOffset(self) -> float:
        """
        Get local clock offset.
        
        Returns:
            local clock offset
        
        
        """
        ...
    def getLocalRate(self) -> float:
        """
        Get local clock rate.
        
        Returns:
            local clock rate
        
        
        """
        ...
    def getRemoteOffset(self) -> float:
        """
        Get remote clock offset.
        
        Returns:
            remote clock offset
        
        
        """
        ...
    def getRemotePV(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get remote satellite position/velocity.
        
        Returns:
            remote satellite position/velocity
        
        
        """
        ...
    def getRemoteRate(self) -> float:
        """
        Get remote clock rate.
        
        Returns:
            remote clock rate
        
        
        """
        ...

class Phase(org.orekit.estimation.measurements.GroundReceiverMeasurement['Phase']):
    """
    Class modeling a phase measurement from a ground station.
    
    The measurement is considered to be a signal emitted from a spacecraft and received on a ground station. Its value is the number of cycles between emission and reception. The motion of both the station and the spacecraft during the signal flight time are taken into account. The date of the measurement corresponds to the reception on ground of the emitted signal.
    
    Since:
        9.2
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, station: org.orekit.estimation.measurements.GroundStation, date: org.orekit.time.AbsoluteDate, phase: float, wavelength: float, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite, cache: AmbiguityCache):
        """
        Simple constructor.
        
        Parameters:
            station (GroundStation): ground station from which measurement is performed
            date (AbsoluteDate): date of the measurement
            phase (double): observed value (cycles)
            wavelength (double): phase observed value wavelength (m)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this measurement
            cache (AmbiguityCache): from which ambiguity drive should come
        
        Since:
            12.1
        
        
        """
        ...
    def getAmbiguityDriver(self) -> AmbiguityDriver:
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
    Builder for Phase measurements.
    
    Since:
        10.1
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, station: org.orekit.estimation.measurements.GroundStation, wavelength: float, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite, cache: AmbiguityCache):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            station (GroundStation): ground station from which measurement is performed
            wavelength (double): phase observed value wavelength (m)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
            cache (AmbiguityCache): from which ambiguity drive should come
        
        Since:
            12.1
        
        
        """
        ...

class WindUpFactory:
    """
    Factory for WindUp modifiers.
    
    The factory ensures the same instance is returned for all satellite/receiver pair, thus preserving phase continuity for successive measurements involving the same pair.
    
    Since:
        10.1
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getWindUp(self, system: org.orekit.gnss.SatelliteSystem, prnNumber: int, emitterDipole: Dipole, receiverName: str) -> 'WindUp':
        """
        Get a modifier for a satellite/receiver pair.
        
        Parameters:
            system (SatelliteSystem): system the satellite belongs to
            prnNumber (int): PRN number
            emitterDipole (Dipole): emitter dipole
            receiverName (String): name of the receiver
        
        Returns:
            modifier for the satellite/receiver pair
        
        
        """
        ...

class AbstractCycleSlipDetector(CycleSlipDetectors):
    """
    Base class for cycle-slip detectors.
    
    Since:
        10.2
    """
    def detect(self, observations: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]:
        """
        Detects if a cycle-slip occurs for a given list of observation data set.
        
        Specified by: detect in interface CycleSlipDetectors
        
        Parameters:
            observations (List<ObservationDataSet> observations): list of observation data set
        
        Returns:
            a list of results computed by the cycle-slip detectors
        
        
        """
        ...

class AbstractDualFrequencyCombination(MeasurementCombination):
    """
    Base class for dual frequency combination of measurements.
    
    Since:
        10.1
    """
    @typing.overload
    def combine(self, od1: org.orekit.files.rinex.observation.ObservationData, od2: org.orekit.files.rinex.observation.ObservationData) -> CombinedObservationData:
        """
        Combines observation data using a dual frequency combination of measurements.
        
        Parameters:
            od1 (ObservationData): first observation data to combined
            od2 (ObservationData): second observation data to combined
        
        Returns:
            a combined observation data
        
        """
        ...
    @typing.overload
    def combine(self, observations: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
        Combines observation data using a combination of measurements.
        
        Specified by: combine in interface MeasurementCombination
        
        Parameters:
            observations (ObservationDataSet): observation data set
        
        Returns:
            a combined observation data set
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the combination of measurements.
        
        Specified by: getName in interface MeasurementCombination
        
        Returns:
            name of the combination of measurements
        
        
        """
        ...

_AbstractInterSatellitesMeasurement__T = typing.TypeVar('_AbstractInterSatellitesMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractInterSatellitesMeasurement(AbstractOnBoardMeasurement[_AbstractInterSatellitesMeasurement__T], typing.Generic[_AbstractInterSatellitesMeasurement__T]):
    """
    Base class for measurement between two satellites that are both estimated.
    
    The measurement is considered to be a signal emitted from a remote satellite and received by a local satellite. Its value is the number of cycles between emission and reception. The motion of both spacecraft during the signal flight time are taken into account. The date of the measurement corresponds to the reception on ground of the emitted signal.
    
    Since:
        12.1
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, observed: float, sigma: float, baseWeight: float, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): date of the measurement
            observed (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): remote satellite which simply emits the signal
        
        
        """
        ...

class AbstractLambdaMethod(IntegerLeastSquareSolver):
    """
    Base class for decorrelation/reduction engine for LAMBDA type methods.
    
    This class is based on both the 1996 paper 2790708_The_LAMBDA_method_for_integer_ambiguity_estimation_implementation_aspects by Paul de Jonge and Christian Tiberius and on the 2005 paper 225518977_MLAMBDA_a_modified_LAMBDA_method_for_integer_least by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
    Since:
        10.0
    """
    def setComparator(self, newCompartor: typing.Union[java.util.Comparator[IntegerLeastSquareSolution], typing.Callable[[IntegerLeastSquareSolution, IntegerLeastSquareSolution], int]]) -> None:
        """
        Set a custom comparator for integer least square solutions comparison.
        
        Calling this method overrides any comparator that could have been set beforehand. It also overrides the default IntegerLeastSquareComparator.
        
        Parameters:
            newCompartor (Comparator<IntegerLeastSquareSolution> newCompartor): new comparator to use
        
        Since:
            11.0
        
        
        """
        ...
    def solveILS(self, nbSol: int, floatAmbiguities: typing.Union[typing.List[float], jpype.JArray], indirection: typing.Union[typing.List[int], jpype.JArray], covariance: org.hipparchus.linear.RealMatrix) -> typing.MutableSequence[IntegerLeastSquareSolution]:
        """
        Find the best solutions to an Integer Least Square problem.
        
        Specified by: solveILS in interface IntegerLeastSquareSolver
        
        Parameters:
            nbSol (int): number of solutions to search for
            floatAmbiguities (double[]): float estimates of ambiguities
            indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
            covariance (RealMatrix): global covariance matrix (includes ambiguities among other parameters)
        
        Returns:
            at most nbSol solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

_AbstractOneWayGNSSMeasurement__T = typing.TypeVar('_AbstractOneWayGNSSMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractOneWayGNSSMeasurement(AbstractOnBoardMeasurement[_AbstractOneWayGNSSMeasurement__T], typing.Generic[_AbstractOneWayGNSSMeasurement__T]):
    """
    Base class for one-way GNSS measurement.
    
    This class can be used in precise orbit determination applications for modeling a range measurement between a GNSS satellite (emitter) and a LEO satellite (receiver).
    
    The one-way GNSS range measurement assumes knowledge of the orbit and the clock offset of the emitting GNSS satellite. For instance, it is possible to use a SP3 file or a GNSS navigation message to recover the satellite's orbit and clock.
    
    This class is very similar to AbstractInterSatellitesMeasurement measurement class. However, using the one-way GNSS range measurement, the orbit and clock of the emitting GNSS satellite are NOT estimated simultaneously with LEO satellite coordinates.
    
    Since:
        12.1
    """
    def __init__(self, remotePV: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], remoteClock: org.orekit.estimation.measurements.QuadraticClockModel, date: org.orekit.time.AbsoluteDate, range: float, sigma: float, baseWeight: float, local: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            remotePV (PVCoordinatesProvider): provider for GNSS satellite which simply emits the signal
            remoteClock (QuadraticClockModel): clock offset of the GNSS satellite
            date (AbsoluteDate): date of the measurement
            range (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            local (ObservableSatellite): satellite which receives the signal and perform the measurement
        
        
        """
        ...

class AbstractSingleFrequencyCombination(MeasurementCombination):
    """
    Base class for single frequency combination of measurements.
    
    Since:
        10.1
    """
    @typing.overload
    def combine(self, phase: org.orekit.files.rinex.observation.ObservationData, pseudoRange: org.orekit.files.rinex.observation.ObservationData) -> CombinedObservationData:
        """
        Combines observation data using a single frequency combination of measurements.
        
        Parameters:
            phase (ObservationData): phase measurement
            pseudoRange (ObservationData): pseudoRange measurement
        
        Returns:
            a combined observation data
        
        
        """
        ...
    @typing.overload
    def combine(self, observations: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
        Combines observation data using a combination of measurements.
        
        Specified by: combine in interface MeasurementCombination
        
        Parameters:
            observations (ObservationDataSet): observation data set
        
        Returns:
            a combined observation data set
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the combination of measurements.
        
        Specified by: getName in interface MeasurementCombination
        
        Returns:
            name of the combination of measurements
        
        
        """
        ...

class InterSatellitesWindUp(AbstractWindUp['InterSatellitesPhase']):
    """
    Modifier for wind-up effect in GNSS InterSatellitesPhase.
    
    Since:
        12.0
    
    Also see:
        InterSatellitesWindUpFactory
    """
    ...

class MelbourneWubbenaCombination(MeasurementCombination):
    """
    Melbourne-Wübbena combination.
    
    This combination allows, thanks to the wide-lane combination, a larger wavelength than each signal individually. Moreover, the measurement noise is reduced by the narrow-lane combination of code measurements.
    
        mMW =  ΦWL- RNL mMW =  λWL * NWL+ b + ε With:
    
      - mMW : Melbourne-Wübbena measurement.
      - ΦWL : Wide-Lane phase measurement.
      - RNL : Narrow-Lane code measurement.
      - λWL : Wide-Lane wavelength.
      - NWL : Wide-Lane ambiguity (Nf1 - Nf2).
      - b : Satellite and receiver instrumental delays.
      - ε : Measurement noise.
    
    NarrowLaneCombination and WideLaneCombination combinations shall be performed with the same pair of frequencies.
    
    Since:
        10.1
    
    Also see:
        "Detector based in code and carrier phase data: The Melbourne-Wübbena combination, J. Sanz Subirana, J.M. Juan Zornoza
        and M. Hernández-Pajares, 2011"
    """
    def combine(self, observations: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
        Combines observation data using a combination of measurements.
        
        Specified by: combine in interface MeasurementCombination
        
        Parameters:
            observations (ObservationDataSet): observation data set
        
        Returns:
            a combined observation data set
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the combination of measurements.
        
        Specified by: getName in interface MeasurementCombination
        
        Returns:
            name of the combination of measurements
        
        
        """
        ...

_PythonAbstractOnBoardMeasurement__T = typing.TypeVar('_PythonAbstractOnBoardMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractOnBoardMeasurement(AbstractOnBoardMeasurement[_PythonAbstractOnBoardMeasurement__T], typing.Generic[_PythonAbstractOnBoardMeasurement__T]):
    def __init__(self, date: org.orekit.time.AbsoluteDate, observed: float, sigma: float, baseWeight: float, satellites: java.util.List[org.orekit.estimation.measurements.ObservableSatellite]):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): date of the measurement
            observed (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellites (List<ObservableSatellite> satellites): satellites related to this measurement
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getRemoteClock(self) -> org.orekit.estimation.measurements.QuadraticClockModel:
        """
        Description copied from class: getRemoteClock Get emitting satellite clock provider.
        
        Specified by: getRemoteClock in class AbstractOnBoardMeasurement
        
        Returns:
            emitting satellite clock provider
        
        
        """
        ...
    @typing.overload
    def getRemotePV(self, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray], freeParameters: int) -> org.orekit.utils.FieldPVCoordinatesProvider[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getRemotePV(self, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Description copied from class: getRemotePV Get emitting satellite position/velocity provider.
        
        Specified by: getRemotePV in class AbstractOnBoardMeasurement
        
        Parameters:
            states (SpacecraftState[]): states of all spacecraft involved in the measurement
        
        Returns:
            emitting satellite position/velocity provider
        
        public FieldPVCoordinatesProvider<Gradient> getRemotePV (SpacecraftState[] states, int freeParameters)
        
        Description copied from class: getRemotePV Get emitting satellite position/velocity provider.
        
        Specified by: getRemotePV in class AbstractOnBoardMeasurement
        
        Parameters:
            states (SpacecraftState[]): states of all spacecraft involved in the measurement
            freeParameters (int): total number of free parameters in the gradient
        
        Returns:
            emitting satellite position/velocity provider
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def theoreticalEvaluation(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurement[_PythonAbstractOnBoardMeasurement__T]:
        """
        Description copied from class: theoreticalEvaluation Estimate the theoretical value.
        
        The theoretical value does not have any modifiers applied.
        
        Specified by: theoreticalEvaluation in class AbstractMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluation number
            states (SpacecraftState[]): orbital states at measurement date
        
        Returns:
            theoretical value
        
        Also see:
            estimate
        
        
        """
        ...
    def theoreticalEvaluationWithoutDerivatives(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractOnBoardMeasurement__T]:
        """
        Description copied from class: theoreticalEvaluationWithoutDerivatives Estimate the theoretical value without derivatives. The default implementation uses the computation with derivatives and ought to be overwritten for performance.
        
        The theoretical value does not have any modifiers applied.
        
        Overrides: theoreticalEvaluationWithoutDerivatives in class AbstractMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluation number
            states (SpacecraftState[]): orbital states at measurement date
        
        Returns:
            theoretical value
        
        Also see:
            estimate
        
        
        """
        ...

_PythonAbstractWindUp__T = typing.TypeVar('_PythonAbstractWindUp__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractWindUp(AbstractWindUp[_PythonAbstractWindUp__T], typing.Generic[_PythonAbstractWindUp__T]):
    def __init__(self, emitter: Dipole, receiver: Dipole):
        """
        Simple constructor.
        
        Parameters:
            emitter (Dipole): emitter dipole
            receiver (Dipole): receiver dipole
        
        
        """
        ...
    def emitterToInert(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractWindUp__T]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Description copied from class: emitterToInert Compute rotation from emitter to inertial frame.
        
        Specified by: emitterToInert in class AbstractWindUp
        
        Parameters:
            estimated (EstimatedMeasurementBase<PythonAbstractWindUp> estimated): estimated measurement to modify
        
        Returns:
            rotation from emitter to inertial frame
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def receiverToInert(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractWindUp__T]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Description copied from class: receiverToInert Compute rotation from receiver to inertial frame.
        
        Specified by: receiverToInert in class AbstractWindUp
        
        Parameters:
            estimated (EstimatedMeasurementBase<PythonAbstractWindUp> estimated): estimated measurement to modify
        
        Returns:
            rotation from receiver to inertial frame
        
        
        """
        ...

class PythonAmbiguityAcceptance(AmbiguityAcceptance):
    def __init__(self): ...
    def accept(self, candidates: typing.Union[typing.List[IntegerLeastSquareSolution], jpype.JArray]) -> IntegerLeastSquareSolution:
        """
        Check if one of the candidate solutions can be accepted.
        
        Specified by: accept in interface AmbiguityAcceptance
        
        Parameters:
            candidates (IntegerLeastSquareSolution[]): candidate solutions of the Integer Least Squares problem, in increasing squared distance order (the array contains at
                least numberOfCandidates candidates)
        
        Returns:
            the candidate solution to accept (normally the one at index 0), or null if we should still use the float solution
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def numberOfCandidates(self) -> int:
        """
        Get the number of candidate solutions to search for.
        
        Specified by: numberOfCandidates in interface AmbiguityAcceptance
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonCycleSlipDetectors(CycleSlipDetectors):
    def __init__(self): ...
    def detect(self, observations: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet]) -> java.util.List[CycleSlipDetectorResults]:
        """
        Detects if a cycle-slip occurs for a given list of observation data set.
        
        Specified by: detect in interface CycleSlipDetectors
        
        Parameters:
            observations (List<ObservationDataSet> observations): list of observation data set
        
        Returns:
            a list of results computed by the cycle-slip detectors
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonIntegerLeastSquareSolver(IntegerLeastSquareSolver):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def solveILS(self, nbSol: int, floatAmbiguities: typing.Union[typing.List[float], jpype.JArray], indirection: typing.Union[typing.List[int], jpype.JArray], covariance: org.hipparchus.linear.RealMatrix) -> typing.MutableSequence[IntegerLeastSquareSolution]:
        """
        Find the best solutions to an Integer Least Square problem.
        
        Specified by: solveILS in interface IntegerLeastSquareSolver
        
        Parameters:
            nbSol (int): number of solutions to search for
            floatAmbiguities (double[]): float estimates of ambiguities
            indirection (int[]): indirection array to extract ambiguity covariances from global covariance matrix
            covariance (RealMatrix): global covariance matrix (includes ambiguities among other parameters)
        
        Returns:
            at most nbSol solutions a to the Integer Least Square problem, in increasing squared distance order
        
        
        """
        ...

class PythonMeasurementCombination(MeasurementCombination):
    def __init__(self): ...
    def combine(self, observations: org.orekit.files.rinex.observation.ObservationDataSet) -> CombinedObservationDataSet:
        """
        Combines observation data using a combination of measurements.
        
        Specified by: combine in interface MeasurementCombination
        
        Parameters:
            observations (ObservationDataSet): observation data set
        
        Returns:
            a combined observation data set
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the combination of measurements.
        
        Specified by: getName in interface MeasurementCombination
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class SimpleRatioAmbiguityAcceptance(AmbiguityAcceptance):
    """
    Ambiguity acceptance test based on a ratio of the two best candidates.
    
    Since:
        10.0
    
    Also see:
        AmbiguitySolver
    """
    def __init__(self, ratio: float):
        """
        Simple constructor.
        
        Parameters:
            ratio (double): acceptance ratio for candidate[0]/candidate[1], typically 0/2 or 0/3
        
        
        """
        ...
    def accept(self, candidates: typing.Union[typing.List[IntegerLeastSquareSolution], jpype.JArray]) -> IntegerLeastSquareSolution:
        """
        Check if one of the candidate solutions can be accepted.
        
        If the ratio candidate[0]/candidate[1] is smaller or equal to the ratio given at construction, then candidate[0] will be accepted
        
        Specified by: accept in interface AmbiguityAcceptance
        
        Parameters:
            candidates (IntegerLeastSquareSolution[]): candidate solutions of the Integer Least Squares problem, in increasing squared distance order (the array contains at
                least numberOfCandidates candidates)
        
        Returns:
            the candidate solution to accept (normally the one at index 0), or null if we should still use the float solution
        
        
        """
        ...
    def numberOfCandidates(self) -> int:
        """
        Get the number of candidate solutions to search for.
        
        Specified by: numberOfCandidates in interface AmbiguityAcceptance
        
        Returns:
            number of candidate solutions to search for
        
        
        """
        ...

class WindUp(AbstractWindUp[Phase]):
    """
    Modifier for wind-up effect in GNSS Phase.
    
    Since:
        10.1
    
    Also see:
        WindUpFactory
    """
    ...

class GRAPHICCombination(AbstractSingleFrequencyCombination):
    """
    GRoup And Phase Ionospheric Calibration (GRAPHIC) combination.
    
    This combination is a ionosphere-free single frequency combination of measurements.
    
        mf =  0.5 * (Φf + Rf) With:
    
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
    Geometry-free combination.
    
    This combination removes the geometry part of the measurement. It can be used to estimate the ionospheric electron content or to detect cycle slips in the carrier phase, as well.
    
        mGF =  m2 - m1 With:
    
      - mGF: Geometry-free measurement.
      - m1 : First measurement.
      - m2 : Second measurement.
    
    Geometry-Free combination is a dual frequency combination. The two measurements shall have different frequencies but they must have the same MeasurementType.
    
    Since:
        10.1
    """
    ...

class GeometryFreeCycleSlipDetector(AbstractCycleSlipDetector):
    """
    Geometry free cycle slip detectors. The detector is based the algorithm given in Detector_based_in_carrier_phase_data:_The_geometry by Zornoza and M. Hernández-Pajares. Within this class a second order polynomial is used to smooth the data. We consider a cycle-slip occurring if the current measurement is too far from the one predicted with the polynomial.
    
    For building the detector, one should give a threshold and a gap time limit. After construction of the detectors, one can have access to a List of CycleData. Each CycleDate represents a link between the station (define by the RINEX file) and a satellite at a specific frequency. For each cycle data, one has access to the begin and end of availability, and a sorted set which contains all the date at which cycle-slip have been detected
    
    Since:
        10.2
    """
    def __init__(self, dt: float, threshold: float, n: int):
        """
        Constructor.
        
        Parameters:
            dt (double): time gap threshold between two consecutive measurement (if time between two consecutive measurement is greater than dt,
                a cycle slip is declared)
            threshold (double): threshold above which cycle-slip occurs
            n (int): number of measurement before starting
        
        
        """
        ...

class InterSatellitesOneWayRangeRate(AbstractInterSatellitesMeasurement['InterSatellitesOneWayRangeRate']):
    """
    One way range-rate measurement between two satellites.
    
    Since:
        12.1
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, date: org.orekit.time.AbsoluteDate, rangeRate: float, sigma: float, baseWeight: float):
        """
        Constructor.
        
        Parameters:
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): remote satellite which simply emits the signal
            date (AbsoluteDate): date of the measurement
            rangeRate (double): observed value (m/s)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
        
        
        """
        ...

class InterSatellitesPhase(AbstractInterSatellitesMeasurement['InterSatellitesPhase']):
    """
    Phase measurement between two satellites.
    
    The measurement is considered to be a signal emitted from a remote satellite and received by a local satellite. Its value is the number of cycles between emission and reception. The motion of both spacecraft during the signal flight time are taken into account. The date of the measurement corresponds to the reception on ground of the emitted signal.
    
    Since:
        10.3
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, date: org.orekit.time.AbsoluteDate, phase: float, wavelength: float, sigma: float, baseWeight: float, cache: AmbiguityCache):
        """
        Constructor.
        
        Parameters:
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): remote satellite which simply emits the signal
            date (AbsoluteDate): date of the measurement
            phase (double): observed value (cycles)
            wavelength (double): phase observed value wavelength (m)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            cache (AmbiguityCache): from which ambiguity drive should come
        
        Since:
            12.1
        
        
        """
        ...
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

class IonosphereFreeCombination(AbstractDualFrequencyCombination):
    """
    Ionosphere-free combination.
    
    This combination removes the first order (up to 99.9%) ionospheric effect.
    
                 f1² * m1 - f2² * m2 mIF =  ----------------------- f1² - f2² With:
    
      - mIF: Ionosphere-free measurement.
      - f1 : Frequency of the first measurement.
      - m1 : First measurement.
      - f2 : Frequency of the second measurement.
      - m1 : Second measurement.
    
    Ionosphere-free combination is a dual frequency combination. The two measurements shall have different frequencies but they must have the same MeasurementType.
    
    Since:
        10.1
    """
    ...

class LambdaMethod(AbstractLambdaMethod):
    """
    Decorrelation/reduction engine for LAMBDA method.
    
    This class implements PJG Teunissen Least Square Ambiguity Decorrelation Adjustment (LAMBDA) method, as described in both the 1996 paper 2790708_The_LAMBDA_method_for_integer_ambiguity_estimation_implementation_aspects by Paul de Jonge and Christian Tiberius and on the 2005 paper 225518977_MLAMBDA_a_modified_LAMBDA_method_for_integer_least by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
    It slightly departs on the original LAMBDA method as it does implement the following improvements proposed in the de Jonge and Tiberius 1996 paper that vastly speed up the search:
    
      - alternate search starting from the middle and expanding outwards
      - automatic shrinking of ellipsoid during the search
    
    
    Since:
        10.0
    
    Also see:
        AmbiguitySolver
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...

class ModifiedLambdaMethod(AbstractLambdaMethod):
    """
    Decorrelation/reduction engine for Modified LAMBDA method.
    
    This class implements Modified Least Square Ambiguity Decorrelation Adjustment (MLAMBDA) method, as described in 225518977_MLAMBDA_a_modified_LAMBDA_method_for_integer_least by X.-W Chang, X. Yang and T. Zhou, Journal of Geodesy 79(9):552-565, DOI: 10.1007/s00190-005-0004-x
    
    Since:
        10.2
    
    Also see:
        AmbiguitySolver
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...

class NarrowLaneCombination(AbstractDualFrequencyCombination):
    """
    Narrow-Lane combination.
    
    This combination create signal with a narrow wavelength. The signal in this combination has a lower noise than each separated separeted component.
    
                  f1 * m1 + f2 * m2 mNL =  ----------------------- f1 + f2 With:
    
      - mNL : Narrow-laning measurement.
      - f1 : Frequency of the first measurement.
      - pr1 : First measurement.
      - f2 : Frequency of the second measurement.
      - m1 : Second measurement.
    
    Narrow-Lane combination is a dual frequency combination. The two measurements shall have different frequencies but they must have the same MeasurementType.
    
    Since:
        10.1
    """
    ...

class OneWayGNSSPhase(AbstractOneWayGNSSMeasurement['OneWayGNSSPhase']):
    """
    One-way GNSS phase measurement.
    
    This class can be used in precise orbit determination applications for modeling a phase measurement between a GNSS satellite (emitter) and a LEO satellite (receiver).
    
    The one-way GNSS phase measurement assumes knowledge of the orbit and the clock offset of the emitting GNSS satellite. For instance, it is possible to use a SP3 file or a GNSS navigation message to recover the satellite's orbit and clock.
    
    This class is very similar to InterSatellitesPhase measurement class. However, using the one-way GNSS phase measurement, the orbit and clock of the emitting GNSS satellite are NOT estimated simultaneously with LEO satellite coordinates.
    
    Since:
        10.3
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, remote: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], remoteName: str, remoteClock: org.orekit.estimation.measurements.QuadraticClockModel, date: org.orekit.time.AbsoluteDate, phase: float, wavelength: float, sigma: float, baseWeight: float, local: org.orekit.estimation.measurements.ObservableSatellite, cache: AmbiguityCache):
        """
        Simple constructor.
        
        Parameters:
            remote (PVCoordinatesProvider): provider for GNSS satellite which simply emits the signal
            remoteName (String): name of the remote
            remoteClock (QuadraticClockModel): clock offset of the GNSS satellite
            date (AbsoluteDate): date of the measurement
            phase (double): observed value, in cycles
            wavelength (double): phase observed value wavelength, in meters
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            local (ObservableSatellite): satellite which receives the signal and perform the measurement
            cache (AmbiguityCache): from which ambiguity drive should come
        
        Since:
            12.1
        
        
        """
        ...
    def getAmbiguityDriver(self) -> AmbiguityDriver:
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

class OneWayGNSSRange(AbstractOneWayGNSSMeasurement['OneWayGNSSRange']):
    """
    One-way GNSS range measurement.
    
    This class can be used in precise orbit determination applications for modeling a range measurement between a GNSS satellite (emitter) and a LEO satellite (receiver).
    
    The one-way GNSS range measurement assumes knowledge of the orbit and the clock offset of the emitting GNSS satellite. For instance, it is possible to use a SP3 file or a GNSS navigation message to recover the satellite's orbit and clock.
    
    This class is very similar to InterSatellitesRange measurement class. However, using the one-way GNSS range measurement, the orbit and clock of the emitting GNSS satellite are NOT estimated simultaneously with LEO satellite coordinates.
    
    Since:
        10.3
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], quadraticClockModel: org.orekit.estimation.measurements.QuadraticClockModel, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...

class OneWayGNSSRangeRate(AbstractOneWayGNSSMeasurement['OneWayGNSSRangeRate']):
    """
    One-way GNSS range rate measurement.
    
    This class can be used in precise orbit determination applications for modeling a range rate measurement between a GNSS satellite (emitter) and a LEO satellite (receiver).
    
    The one-way GNSS range rate measurement assumes knowledge of the orbit and the clock offset of the emitting GNSS satellite. For instance, it is possible to use a SP3 file or a GNSS navigation message to recover the satellite's orbit and clock.
    
    This class is very similar to InterSatellitesOneWayRangeRate measurement class. However, using the one-way GNSS range measurement, the orbit and clock of the emitting GNSS satellite are NOT estimated simultaneously with LEO satellite coordinates.
    
    Since:
        12.1
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], double: float, absoluteDate: org.orekit.time.AbsoluteDate, double2: float, double3: float, double4: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], quadraticClockModel: org.orekit.estimation.measurements.QuadraticClockModel, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...

class PhaseMinusCodeCombination(AbstractSingleFrequencyCombination):
    """
    Phase minus Code combination.
    
    This combination is a single frequency combination of measurements that can be used for cycle-slip detection.
    
        mf =  Φf - Rf With:
    
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
    Phase minus code cycle slip detectors. The detector is based the algorithm given in Examples_of_single_frequency_Cycle by Zornoza and M. Hernández-Pajares. Within this class a polynomial is used to smooth the data. We consider a cycle_slip occurring if the current measurement is too far from the one predicted with the polynomial (algorithm 1 on Navipedia).
    
    For building the detector, one should give a threshold and a gap time limit. After construction of the detectors, one can have access to a List of CycleData. Each CycleDate represents a link between the station (define by the RINEX file) and a satellite at a specific frequency. For each cycle data, one has access to the begin and end of availability, and a sorted set which contains all the date at which cycle-slip have been detected
    
    Since:
        10.2
    """
    def __init__(self, dt: float, threshold: float, n: int, order: int):
        """
        Polynomial single frequency cycle-slip detector Constructor.
        
        Parameters:
            dt (double): time gap threshold between two consecutive measurement (if time between two consecutive measurement is greater than dt,
                a cycle slip is declared)
            threshold (double): threshold above which cycle-slip occurs
            n (int): number of measurement before starting
            order (int): polynomial order
        
        
        """
        ...

class PythonAbstractCycleSlipDetector(AbstractCycleSlipDetector):
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getMaxTimeBeetween2Measurement(self) -> float:
        """
        Get the maximum time lapse between 2 measurements without considering a cycle-slip has occurring between both.
        
        Overrides: getMaxTimeBeetween2Measurement in class AbstractCycleSlipDetector
        
        Returns:
            the maximum time lapse between 2 measurements
        
        
        """
        ...
    def getMinMeasurementNumber(self) -> int:
        """
        Get the minimum number of measurement needed before being able to figure out cycle-slip occurrence.
        
        Overrides: getMinMeasurementNumber in class AbstractCycleSlipDetector
        
        Returns:
            the minimum number of measurement needed before being able to figure out cycle-slip occurrence.
        
        
        """
        ...
    def getResults(self) -> java.util.List[CycleSlipDetectorResults]:
        """
        Get on all the results computed by the detector (e.g.: dates of cycle-slip).
        
        Overrides: getResults in class AbstractCycleSlipDetector
        
        Returns:
            all the results computed by the detector (e.g.: dates of cycle-slip).
        
        
        """
        ...
    def manageData(self, observation: org.orekit.files.rinex.observation.ObservationDataSet) -> None:
        """
        The method is in charge of collecting the measurements, manage them, and call the detection method.
        
        Specified by: manageData in class AbstractCycleSlipDetector
        
        Parameters:
            observation (ObservationDataSet): observation data set
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def setName(self, numSat: int, sys: org.orekit.gnss.SatelliteSystem) -> str:
        """
        Create the name of a satellite from its PRN number and satellite System it belongs to.
        
        Overrides: setName in class AbstractCycleSlipDetector
        
        Parameters:
            numSat (int): satellite PRN number
            sys (SatelliteSystem): Satellite System of the satellite
        
        Returns:
            the satellite name on a specified format (e.g.: "GPS - 7")
        
        
        """
        ...

class PythonAbstractDualFrequencyCombination(AbstractDualFrequencyCombination):
    def __init__(self, type: CombinationType, system: org.orekit.gnss.SatelliteSystem):
        """
        Constructor.
        
        Parameters:
            type (CombinationType): combination of measurements type
            system (SatelliteSystem): satellite system
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCombinedFrequency(self, s1: org.orekit.gnss.GnssSignal, s2: org.orekit.gnss.GnssSignal) -> float:
        """
        Get the combined frequency of two measurements.
        
        Specified by: getCombinedFrequency in class AbstractDualFrequencyCombination
        
        Parameters:
            s1 (GnssSignal): frequency of the first measurement
            s2 (GnssSignal): frequency of the second measurement
        
        Returns:
            combined frequency in Hz
        
        
        """
        ...
    def getCombinedValue(self, obs1: float, s1: org.orekit.gnss.GnssSignal, obs2: float, s2: org.orekit.gnss.GnssSignal) -> float:
        """
        Get the combined observed value of two measurements.
        
        Specified by: getCombinedValue in class AbstractDualFrequencyCombination
        
        Parameters:
            obs1 (double): observed value of the first measurement
            s1 (GnssSignal): frequency of the first measurement
            obs2 (double): observed value of the second measurement
            s2 (GnssSignal): frequency of the second measurement
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

_PythonAbstractInterSatellitesMeasurement__T = typing.TypeVar('_PythonAbstractInterSatellitesMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractInterSatellitesMeasurement(AbstractInterSatellitesMeasurement[_PythonAbstractInterSatellitesMeasurement__T], typing.Generic[_PythonAbstractInterSatellitesMeasurement__T]):
    def __init__(self, date: org.orekit.time.AbsoluteDate, observed: float, sigma: float, baseWeight: float, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): date of the measurement
            observed (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): remote satellite which simply emits the signal
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def theoreticalEvaluation(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurement[_PythonAbstractInterSatellitesMeasurement__T]:
        """
        Description copied from class: theoreticalEvaluation Estimate the theoretical value.
        
        The theoretical value does not have any modifiers applied.
        
        Specified by: theoreticalEvaluation in class AbstractMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluation number
            states (SpacecraftState[]): orbital states at measurement date
        
        Returns:
            theoretical value
        
        Also see:
            estimate
        
        
        """
        ...
    def theoreticalEvaluationWithoutDerivatives(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractInterSatellitesMeasurement__T]:
        """
        Description copied from class: theoreticalEvaluationWithoutDerivatives Estimate the theoretical value without derivatives. The default implementation uses the computation with derivatives and ought to be overwritten for performance.
        
        The theoretical value does not have any modifiers applied.
        
        Overrides: theoreticalEvaluationWithoutDerivatives in class AbstractMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluation number
            states (SpacecraftState[]): orbital states at measurement date
        
        Returns:
            theoretical value
        
        Also see:
            estimate
        
        
        """
        ...

class PythonAbstractLambdaMethod(AbstractLambdaMethod):
    def __init__(self): ...
    def discreteSearch(self) -> None:
        """
        Find the best solutions to the Integer Least Square problem.
        
        Specified by: discreteSearch in class AbstractLambdaMethod
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def inverseDecomposition(self) -> None:
        """
        Inverse the decomposition.
        
        This method transforms the Lᵀ.D.L = Q decomposition of covariance into the L⁻¹.D⁻¹.L⁻ᵀ = Q⁻¹ decomposition of the inverse of covariance.
        
        Specified by: inverseDecomposition in class AbstractLambdaMethod
        
        
        """
        ...
    def ltdlDecomposition(self) -> None:
        """
        Perform Lᵀ.D.L = Q decomposition of the covariance matrix.
        
        Specified by: ltdlDecomposition in class AbstractLambdaMethod
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def reduction(self) -> None:
        """
        Perform LAMBDA reduction.
        
        Specified by: reduction in class AbstractLambdaMethod
        
        
        """
        ...

_PythonAbstractOneWayGNSSMeasurement__T = typing.TypeVar('_PythonAbstractOneWayGNSSMeasurement__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractOneWayGNSSMeasurement(AbstractOneWayGNSSMeasurement[_PythonAbstractOneWayGNSSMeasurement__T], typing.Generic[_PythonAbstractOneWayGNSSMeasurement__T]):
    def __init__(self, remotePV: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], remoteClock: org.orekit.estimation.measurements.QuadraticClockModel, date: org.orekit.time.AbsoluteDate, range: float, sigma: float, baseWeight: float, local: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            remotePV (PVCoordinatesProvider): provider for GNSS satellite which simply emits the signal
            remoteClock (QuadraticClockModel): clock offset of the GNSS satellite
            date (AbsoluteDate): date of the measurement
            range (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            local (ObservableSatellite): satellite which receives the signal and perform the measurement
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def theoreticalEvaluation(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurement[_PythonAbstractOneWayGNSSMeasurement__T]:
        """
        Description copied from class: theoreticalEvaluation Estimate the theoretical value.
        
        The theoretical value does not have any modifiers applied.
        
        Specified by: theoreticalEvaluation in class AbstractMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluation number
            states (SpacecraftState[]): orbital states at measurement date
        
        Returns:
            theoretical value
        
        Also see:
            estimate
        
        
        """
        ...
    def theoreticalEvaluationWithoutDerivatives(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractOneWayGNSSMeasurement__T]:
        """
        Description copied from class: theoreticalEvaluationWithoutDerivatives Estimate the theoretical value without derivatives. The default implementation uses the computation with derivatives and ought to be overwritten for performance.
        
        The theoretical value does not have any modifiers applied.
        
        Overrides: theoreticalEvaluationWithoutDerivatives in class AbstractMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluation number
            states (SpacecraftState[]): orbital states at measurement date
        
        Returns:
            theoretical value
        
        Also see:
            estimate
        
        
        """
        ...

class PythonAbstractSingleFrequencyCombination(AbstractSingleFrequencyCombination):
    def __init__(self, type: CombinationType, system: org.orekit.gnss.SatelliteSystem):
        """
        Constructor.
        
        Parameters:
            type (CombinationType): combination of measurements type
            system (SatelliteSystem): satellite system
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCombinedValue(self, phase: float, pseudoRange: float) -> float:
        """
        Get the combined observed value of two measurements.
        
        Specified by: getCombinedValue in class AbstractSingleFrequencyCombination
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class WideLaneCombination(AbstractDualFrequencyCombination):
    """
    Wide-Lane combination.
    
    This combination are used to create a signal with a significantly wide wavelength. This longer wavelength is useful for cycle-slips detection and ambiguity fixing
    
                  f1 * m1 - f2 * m2 mWL =  ----------------------- f1 - f2 With:
    
      - mWL: Wide-laning measurement.
      - f1 : Frequency of the first measurement.
      - m1 : First measurement.
      - f2 : Frequency of the second measurement.
      - m1 : Second measurement.
    
    Wide-Lane combination is a dual frequency combination. The two measurements shall have different frequencies but they must have the same MeasurementType.
    
    Since:
        10.1
    """
    ...

class IntegerBootstrapping(LambdaMethod):
    """
    Bootstrapping engine for ILS problem solving. This method is base on the following paper: 225773077_Success_probability_of_integer_GPS_ambiguity_rounding_and_bootstrapping by P. J. G. Teunissen 1998 and by P. J. G. Teunissen 2006.
    
    This method is really faster for integer ambiguity resolution than LAMBDA or MLAMBDA method but its success rate is really smaller. The method extends LambdaMethod as it uses LDL' factorization and reduction methods from LAMBDA method. The method is really different from LAMBDA as the solution found is not a least-square solution. It is a solution which asses a probability of success of the solution found. The probability increase with the does with LDL' factorization and reduction methods.
    
    If one want to use this method for integer ambiguity resolution, one just need to construct IntegerBootstrapping only with a double which is the minimal probability of success one wants. Then from it, one can call the solveILS method.
    
    Since:
        10.2
    """
    def __init__(self, prob: float):
        """
        Constructor for the bootstrapping ambiguity estimator.
        
        Parameters:
            prob (double): minimum probability acceptance for the bootstrap
        
        
        """
        ...


class __module_protocol__(Protocol):
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
