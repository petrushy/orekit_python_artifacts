
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.estimation.measurements.filtering
import org.orekit.estimation.measurements.generation
import org.orekit.estimation.measurements.gnss
import org.orekit.estimation.measurements.modifiers
import org.orekit.frames
import org.orekit.models.earth.displacement
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



class CommonParametersWithDerivatives:
    """
    Common intermediate parameters used to estimate measurements where receiver is a ground station.
    
    Since:
        12.1
    """
    def __init__(self, state: org.orekit.propagation.SpacecraftState, indices: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]], tauD: org.hipparchus.analysis.differentiation.Gradient, transitState: org.orekit.propagation.SpacecraftState, transitPV: org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]):
        """
        Simple constructor.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            indices (Map<String, Integer> indices): derivatives indices map
            tauD (Gradient): downlink delay
            transitState (SpacecraftState): transit state
            transitPV (TimeStampedFieldPVCoordinates<Gradient> transitPV): transit position/velocity as a gradient
        
        
        """
        ...
    def getIndices(self) -> java.util.Map[str, int]:
        """
        Get derivatives indices map.
        
        Returns:
            derivatives indices map
        
        
        """
        ...
    def getState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get spacecraft state.
        
        Returns:
            spacecraft state
        
        
        """
        ...
    def getTauD(self) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Get downlink delay.
        
        Returns:
            ownlink delay
        
        
        """
        ...
    def getTransitPV(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get transit position/velocity.
        
        Returns:
            transit position/velocity
        
        
        """
        ...
    def getTransitState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get transit state.
        
        Returns:
            transit state
        
        
        """
        ...

class CommonParametersWithoutDerivatives:
    """
    Common intermediate parameters used to estimate measurements.
    
    Since:
        12.1
    """
    def __init__(self, state: org.orekit.propagation.SpacecraftState, tauD: float, transitState: org.orekit.propagation.SpacecraftState, transitPV: org.orekit.utils.TimeStampedPVCoordinates):
        """
        Simple constructor.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            tauD (double): downlink delay
            transitState (SpacecraftState): transit state
            transitPV (TimeStampedPVCoordinates): transit position/velocity
        
        
        """
        ...
    def getState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get spacecraft state.
        
        Returns:
            spacecraft state
        
        
        """
        ...
    def getTauD(self) -> float:
        """
        Get downlink delay.
        
        Returns:
            ownlink delay
        
        
        """
        ...
    def getTransitPV(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get transit position/velocity.
        
        Returns:
            transit position/velocity
        
        
        """
        ...
    def getTransitState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get transit state.
        
        Returns:
            transit state
        
        
        """
        ...

class ComparableMeasurement(org.orekit.time.TimeStamped, java.lang.Comparable['ComparableMeasurement']):
    """
    Base interface for comparing measurements regardless of their type.
    
    Since:
        9.2
    """
    def compareTo(self, comparableMeasurement: 'ComparableMeasurement') -> int:
        """
        Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed value. Even if they have the same value too, they will likely not be considered equal if they correspond to different instances.
        
        Care should be taken before storing measurements in a SortedSet as it may lose redundant measurements if they, by chance, have the same identity hash code.
        
        Specified by: Comparable in interface Comparable
        
        Also see:
            System
        
        
        """
        ...
    def getObservedValue(self) -> typing.MutableSequence[float]:
        """
        Get the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Returns:
            observed value
        
        
        """
        ...
    def setObservedValue(self, newObserved: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Parameters:
            newObserved (double[]): observed value
        
        Since:
            13.0
        
        
        """
        ...

class EstimatedEarthFrameProvider(org.orekit.frames.TransformProvider):
    """
    Class modeling an Earth frame whose Earth Orientation Parameters can be estimated.
    
    This class adds parameters for an additional polar motion and an additional prime meridian orientation on top of an underlying regular Earth frame like getITRF. The polar motion and prime meridian orientation are applied after regular Earth orientation parameters, so the value of the estimated parameters will be correction to EOP, they will not be the complete EOP values by themselves. Basically, this means that for Earth, the following transforms are applied in order, between inertial frame and this frame:
    
      1.  precession/nutation, as theoretical model plus celestial pole EOP parameters 2.  body rotation, as theoretical model plus prime meridian EOP parameters 3.  polar motion, which is only from EOP parameters (no theoretical models) 4.  additional body rotation, controlled by getPrimeMeridianOffsetDriver and getPrimeMeridianDriftDriver 5.  additional polar motion, controlled by getPolarOffsetXDriver, getPolarDriftXDriver, getPolarOffsetYDriver and getPolarDriftYDriver
    
    
    Since:
        9.1
    """
    EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    Earth Angular Velocity, in rad/s, from TIRF model.
    
    Also see:
        constant
    
    
    """
    def __init__(self, baseUT1: org.orekit.time.UT1Scale):
        """
        Build an estimated Earth frame.
        
        The initial values for the pole and prime meridian parametric linear models (getPrimeMeridianOffsetDriver, getPrimeMeridianDriftDriver, getPolarOffsetXDriver, getPolarDriftXDriver, getPolarOffsetXDriver, getPolarDriftXDriver) are set to 0.
        
        Parameters:
            baseUT1 (UT1Scale): underlying base UT1
        
        Since:
            9.1
        
        
        """
        ...
    def getEstimatedUT1(self) -> org.orekit.time.UT1Scale:
        """
        Get the estimated UT1 time scale.
        
        Returns:
            estimated UT1 time scale
        
        
        """
        ...
    def getPolarDriftXDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar drift along X.
        
        The parameter is an angle rate in radians per second
        
        Returns:
            driver for polar drift along X
        
        
        """
        ...
    def getPolarDriftYDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar drift along Y.
        
        The parameter is an angle rate in radians per second
        
        Returns:
            driver for polar drift along Y
        
        
        """
        ...
    def getPolarOffsetXDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar offset along X.
        
        The parameter is an angle in radians
        
        Returns:
            driver for polar offset along X
        
        
        """
        ...
    def getPolarOffsetYDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar offset along Y.
        
        The parameter is an angle in radians
        
        Returns:
            driver for polar offset along Y
        
        
        """
        ...
    def getPrimeMeridianDriftDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a prime meridian rotation rate.
        
        The parameter is an angle rate in radians per second. In order to convert this value to a LOD in seconds, the value must be multiplied by -86400 and divided by EARTH_ANGULAR_VELOCITY (nominal Angular Velocity of Earth).
        
        Returns:
            driver for prime meridian rotation rate
        
        
        """
        ...
    def getPrimeMeridianOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a prime meridian rotation.
        
        The parameter is an angle in radians. In order to convert this value to a DUT1 in seconds, the value must be divided by EARTH_ANGULAR_VELOCITY (nominal Angular Velocity of Earth).
        
        Returns:
            driver for prime meridian rotation
        
        
        """
        ...
    _getStaticTransform_0__T = typing.TypeVar('_getStaticTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getStaticTransform_0__T]) -> org.orekit.frames.FieldStaticTransform[_getStaticTransform_0__T]:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the static transform.
        
        
        """
        ...
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.frames.StaticTransform:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation calls getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the static transform.
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> org.orekit.frames.FieldTransform[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        public FieldTransform<Gradient> getTransform (FieldAbsoluteDate<Gradient> date, int freeParameters, Map<String, Integer> indices)
        
        Get the transform with derivatives.
        
        Parameters:
            date (FieldAbsoluteDate<Gradient> date): date of the transform
            freeParameters (int): total number of free parameters in the gradient
            indices (Map<String, Integer> indices): indices of the estimated parameters in derivatives computations
        
        Returns:
            computed transform with derivatives
        
        Since:
            10.2
        
        
        """
        ...
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.analysis.differentiation.Gradient], int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

_EstimationModifier__T = typing.TypeVar('_EstimationModifier__T', bound='ObservedMeasurement')  # <T>
class EstimationModifier(org.orekit.utils.ParameterDriversProvider, typing.Generic[_EstimationModifier__T]):
    """
    Interface for estimated measurements modifiers used for orbit determination.
    
    Modifiers are used to take some physical corrections into account in the theoretical EstimatedMeasurement model. They can be used to model for example:
    
      - on board delays
      - ground delays
      - antennas mount and center of phase offsets
      - tropospheric effects
      - clock drifts
      - ground station displacements due to tidal effects
      - ...
    
    
    Since:
        8.0
    """
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def modify(self, estimated: 'EstimatedMeasurement'[_EstimationModifier__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Parameters:
            estimated (EstimatedMeasurement<EstimationModifier> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: 'EstimatedMeasurementBase'[_EstimationModifier__T]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Parameters:
            estimated (EstimatedMeasurementBase<EstimationModifier> estimated): estimated measurement to modify
        
        Since:
            12.0
        
        
        """
        ...

class EstimationsProvider:
    """
    Interface for retrieving estimated measurements during orbit determination.
    
    Implementations of this interface are provided by the orbit determination engine to user so they can BatchLSObserver the orbit determination process.
    
    Since:
        8.0
    
    Also see:
        BatchLSObserver
    """
    def getEstimatedMeasurement(self, index: int) -> 'EstimatedMeasurement'[typing.Any]:
        """
        EstimatedMeasurement<?> getEstimatedMeasurement (int index)
        
        Get one estimated measurement.
        
        Parameters:
            index (int): index of the estimated measurement, must be between 0 and
                getNumber - 1, chronologically sorted
        
        Returns:
            estimated measurement at specified index
        
        
        """
        ...
    def getNumber(self) -> int:
        """
        Get the number of evaluations available.
        
        Returns:
            number of evaluations available
        
        
        """
        ...

class GroundStation:
    """
    Class modeling a ground station that can perform some measurements.
    
    This class adds a position offset parameter to a base TopocentricFrame.
    
    Since 9.0, this class also adds parameters for an additional polar motion and an additional prime meridian orientation. Since these parameters will have the same name for all ground stations, they will be managed consistently and allow to estimate Earth orientation precisely (this is needed for precise orbit determination). The polar motion and prime meridian orientation will be applied after regular Earth orientation parameters, so the value of the estimated parameters will be correction to EOP, they will not be the complete EOP values by themselves. Basically, this means that for Earth, the following transforms are applied in order, between inertial frame and ground station frame (for non-Earth based ground stations, different precession nutation models and associated planet oritentation parameters would be applied, if available):
    
    Since 9.3, this class also adds a station clock offset parameter, which manages the value that must be subtracted from the observed measurement date to get the real physical date at which the measurement was performed (i.e. the offset is negative if the ground station clock is slow and positive if it is fast).
    
      1.  precession/nutation, as theoretical model plus celestial pole EOP parameters 2.  body rotation, as theoretical model plus prime meridian EOP parameters 3.  polar motion, which is only from EOP parameters (no theoretical models) 4.  additional body rotation, controlled by getPrimeMeridianOffsetDriver and getPrimeMeridianDriftDriver 5.  additional polar motion, controlled by getPolarOffsetXDriver, getPolarDriftXDriver, getPolarOffsetYDriver and getPolarDriftYDriver 6.  station clock offset, controlled by getClockOffsetDriver 7.  station position offset, controlled by getEastOffsetDriver, getNorthOffsetDriver and getZenithOffsetDriver
    
    
    Since:
        8.0
    """
    OFFSET_SUFFIX: typing.ClassVar[str] = ...
    """
    Suffix for ground station position and clock offset parameters names.
    
    Also see:
        constant
    
    
    """
    DRIFT_SUFFIX: typing.ClassVar[str] = ...
    """
    Suffix for ground clock drift parameters name.
    
    Also see:
        constant
    
    
    """
    ACCELERATION_SUFFIX: typing.ClassVar[str] = ...
    """
    Suffix for ground clock drift parameters name.
    
    Since:
        12.1
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame, eOPHistory: org.orekit.frames.EOPHistory, *stationDisplacement: typing.Union[org.orekit.models.earth.displacement.StationDisplacement, typing.Callable]): ...
    def getBaseFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
        Get the base frame associated with the station.
        
        The base frame corresponds to a null position offset, null polar motion, null meridian shift
        
        Returns:
            base frame associated with the station
        
        
        """
        ...
    def getClockAccelerationDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to change station clock acceleration (which is related to measurement date).
        
        Returns:
            driver for station clock acceleration
        
        Since:
            12.1
        
        
        """
        ...
    def getClockDriftDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to change station clock drift (which is related to measurement date).
        
        Returns:
            driver for station clock drift
        
        Since:
            10.3
        
        
        """
        ...
    def getClockOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to change station clock (which is related to measurement date).
        
        Returns:
            driver for station clock offset
        
        Since:
            9.3
        
        
        """
        ...
    def getDisplacements(self) -> typing.MutableSequence[org.orekit.models.earth.displacement.StationDisplacement]:
        """
        Get the displacement models.
        
        Returns:
            displacement models (empty if no model has been set up)
        
        Since:
            9.1
        
        
        """
        ...
    def getEastOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to change station position along East axis.
        
        Returns:
            driver for station position offset along East axis
        
        
        """
        ...
    def getEstimatedEarthFrame(self) -> org.orekit.frames.Frame:
        """
        Get the estimated Earth frame, including the estimated linear models for pole and prime meridian.
        
        This frame is bound to the getPrimeMeridianOffsetDriver, getPrimeMeridianDriftDriver, getPolarOffsetXDriver, getPolarDriftXDriver, getPolarOffsetYDriver, getPolarDriftYDriver, so its orientation changes when the setValue methods of the drivers are called.
        
        Returns:
            estimated Earth frame
        
        Since:
            9.1
        
        
        """
        ...
    def getEstimatedUT1(self) -> org.orekit.time.UT1Scale:
        """
        Get the estimated UT1 scale, including the estimated linear models for prime meridian.
        
        This time scale is bound to the getPrimeMeridianOffsetDriver, and getPrimeMeridianDriftDriver, so its offset from UTC changes when the setValue methods of the drivers are called.
        
        Returns:
            estimated Earth frame
        
        Since:
            9.1
        
        
        """
        ...
    def getNorthOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to change station position along North axis.
        
        Returns:
            driver for station position offset along North axis
        
        
        """
        ...
    _getOffsetGeodeticPoint_0__T = typing.TypeVar('_getOffsetGeodeticPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffsetGeodeticPoint(self, date: org.orekit.time.FieldAbsoluteDate[_getOffsetGeodeticPoint_0__T]) -> org.orekit.bodies.FieldGeodeticPoint[_getOffsetGeodeticPoint_0__T]:
        """
        Get the geodetic point at the center of the offset frame.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date(must be non-null, which is a more stringent condition * than in
                getOffsetGeodeticPoint
        
        Returns:
            geodetic point at the center of the offset frame
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def getOffsetGeodeticPoint(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint:
        """
        Get the geodetic point at the center of the offset frame.
        
        Parameters:
            date (AbsoluteDate): current date (may be null if displacements are ignored)
        
        Returns:
            geodetic point at the center of the offset frame
        
        Since:
            9.1
        
        """
        ...
    @typing.overload
    def getOffsetToInertial(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getOffsetToInertial(self, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.analysis.differentiation.Gradient], int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getOffsetToInertial(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> org.orekit.frames.Transform:
        """
        Get the transform between offset frame and inertial frame.
        
        The offset frame takes the current position offset, polar motion and the meridian shift into account. The frame returned is disconnected from later changes in the parameters. When the ParameterDriver managing these offsets are changed, the method must be called again to retrieve a new offset frame.
        
        Parameters:
            inertial (Frame): inertial frame to transform to
            date (AbsoluteDate): date of the transform
            clockOffsetAlreadyApplied (boolean): if true, the specified date is as read by the ground station clock (i.e. clock offset not compensated), if
                false, the specified date was already compensated and is a physical absolute date
        
        Returns:
            transform between offset frame and inertial frame, at real measurement date (i.e. with clock, Earth and station
            offsets applied)
        
        public FieldTransform<Gradient> getOffsetToInertial (Frame inertial, AbsoluteDate clockDate, int freeParameters, Map<String, Integer> indices)
        
        Get the transform between offset frame and inertial frame with derivatives.
        
        As the East and North vectors are not well defined at pole, the derivatives of these two vectors diverge to infinity as we get closer to the pole. So this method should not be used for stations less than 0.0001 degree from either poles.
        
        Parameters:
            inertial (Frame): inertial frame to transform to
            clockDate (AbsoluteDate): date of the transform as read by the ground station clock (i.e. clock offset not compensated)
            freeParameters (int): total number of free parameters in the gradient
            indices (Map<String, Integer> indices): indices of the estimated parameters in derivatives computations, must be driver span name in map, not driver name or
                will not give right results (see getValue)
        
        Returns:
            transform between offset frame and inertial frame, at real measurement date (i.e. with clock, Earth and station
            offsets applied)
        
        Since:
            10.2
        
        Also see:
            getOffsetToInertial
        
        public FieldTransform<Gradient> getOffsetToInertial (Frame inertial, FieldAbsoluteDate<Gradient> offsetCompensatedDate, int freeParameters, Map<String, Integer> indices)
        
        Get the transform between offset frame and inertial frame with derivatives.
        
        As the East and North vectors are not well defined at pole, the derivatives of these two vectors diverge to infinity as we get closer to the pole. So this method should not be used for stations less than 0.0001 degree from either poles.
        
        Parameters:
            inertial (Frame): inertial frame to transform to
            offsetCompensatedDate (FieldAbsoluteDate<Gradient> offsetCompensatedDate): date of the transform, clock offset and its derivatives already compensated
            freeParameters (int): total number of free parameters in the gradient
            indices (Map<String, Integer> indices): indices of the estimated parameters in derivatives computations, must be driver span name in map, not driver name or
                will not give right results (see getValue)
        
        Returns:
            transform between offset frame and inertial frame, at specified date
        
        Since:
            10.2
        
        
        """
        ...
    def getPolarDriftXDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar drift along X.
        
        The parameter is an angle rate in radians per second
        
        Returns:
            driver for polar drift along X
        
        
        """
        ...
    def getPolarDriftYDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar drift along Y.
        
        The parameter is an angle rate in radians per second
        
        Returns:
            driver for polar drift along Y
        
        
        """
        ...
    def getPolarOffsetXDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar offset along X.
        
        The parameter is an angle in radians
        
        Returns:
            driver for polar offset along X
        
        
        """
        ...
    def getPolarOffsetYDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a polar offset along Y.
        
        The parameter is an angle in radians
        
        Returns:
            driver for polar offset along Y
        
        
        """
        ...
    def getPrimeMeridianDriftDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a prime meridian rotation rate.
        
        The parameter is an angle rate in radians per second. In order to convert this value to a LOD in seconds, the value must be multiplied by -86400 and divided by 292115146706979e-5 (which is the nominal Angular Velocity of Earth from the TIRF model).
        
        Returns:
            driver for prime meridian rotation rate
        
        
        """
        ...
    def getPrimeMeridianOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to add a prime meridian rotation.
        
        The parameter is an angle in radians. In order to convert this value to a DUT1 in seconds, the value must be divided by 292115146706979e-5 (which is the nominal Angular Velocity of Earth from the TIRF model).
        
        Returns:
            driver for prime meridian rotation
        
        
        """
        ...
    def getZenithOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get a driver allowing to change station position along Zenith axis.
        
        Returns:
            driver for station position offset along Zenith axis
        
        
        """
        ...

class ObservableSatellite:
    """
    Class modeling a satellite that can be observed.
    
    Since:
        9.3
    """
    CLOCK_OFFSET_PREFIX: typing.ClassVar[str] = ...
    """
    Prefix for clock offset parameter driver, the propagator index will be appended to it.
    
    Also see:
        constant
    
    
    """
    CLOCK_DRIFT_PREFIX: typing.ClassVar[str] = ...
    """
    Prefix for clock drift parameter driver, the propagator index will be appended to it.
    
    Also see:
        constant
    
    
    """
    CLOCK_ACCELERATION_PREFIX: typing.ClassVar[str] = ...
    """
    Prefix for clock acceleration parameter driver, the propagator index will be appended to it.
    
    Since:
        12.1
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, string: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        Since:
            12.0
        
        
        """
        ...
    def getClockAccelerationDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get the clock acceleration parameter driver.
        
        Returns:
            clock acceleration parameter driver
        
        Since:
            12.1
        
        
        """
        ...
    def getClockDriftDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get the clock drift parameter driver.
        
        The drift is negative if the satellite clock is slowing down and positive if it is speeding up.
        
        Returns:
            clock drift parameter driver
        
        Since:
            10.3
        
        
        """
        ...
    def getClockOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get the clock offset parameter driver.
        
        The offset value is defined as the value in seconds that must be subtracted from the satellite clock reading of time to compute the real physical date. The offset is therefore negative if the satellite clock is slow and positive if it is fast.
        
        Returns:
            clock offset parameter driver
        
        
        """
        ...
    def getName(self) -> str:
        """
        Build a name for the satellite.
        
        This is mainly useful to build the arguments for getAmbiguity
        
        Returns:
            name for the satellite
        
        Since:
            12.1
        
        
        """
        ...
    def getPropagatorIndex(self) -> int:
        """
        Get the index of the propagator related to this satellite.
        
        Returns:
            index of the propagator related to this satellite
        
        
        """
        ...
    def getQuadraticClockModel(self) -> 'QuadraticClockModel':
        """
        Get a quadratic clock model valid at some date.
        
        Returns:
            quadratic clock model
        
        Since:
            12.1
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        Since:
            12.0
        
        
        """
        ...

class QuadraticClockModel(org.orekit.time.ClockModel):
    """
    Quadratic clock model.
    
    Since:
        12.1
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, parameterDriver: org.orekit.utils.ParameterDriver, parameterDriver2: org.orekit.utils.ParameterDriver, parameterDriver3: org.orekit.utils.ParameterDriver): ...
    _getOffset_1__T = typing.TypeVar('_getOffset_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.time.ClockOffset:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (AbsoluteDate): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        """
        ...
    @typing.overload
    def getOffset(self, date: org.orekit.time.FieldAbsoluteDate[_getOffset_1__T]) -> org.orekit.time.FieldClockOffset[_getOffset_1__T]:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        
        """
        ...
    def getValidityEnd(self) -> org.orekit.time.AbsoluteDate:
        """
        Get validity end.
        
        Specified by: getValidityEnd in interface ClockModel
        
        Returns:
            model validity end
        
        
        """
        ...
    def getValidityStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get validity start.
        
        Specified by: getValidityStart in interface ClockModel
        
        Returns:
            model validity start
        
        
        """
        ...
    def toGradientModel(self, freeParameters: int, indices: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]], date: org.orekit.time.AbsoluteDate) -> 'QuadraticFieldClockModel'[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Convert to gradient model.
        
        Parameters:
            freeParameters (int): total number of free parameters in the gradient
            indices (Map<String, Integer> indices): indices of the differentiation parameters in derivatives computations, must be span name and not driver name
            date (AbsoluteDate): date at which model must be valid
        
        Returns:
            converted clock model
        
        
        """
        ...

_QuadraticFieldClockModel__T = typing.TypeVar('_QuadraticFieldClockModel__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class QuadraticFieldClockModel(typing.Generic[_QuadraticFieldClockModel__T]):
    """
    Quadratic clock model.
    
    Since:
        12.1
    """
    def __init__(self, referenceDate: org.orekit.time.FieldAbsoluteDate[_QuadraticFieldClockModel__T], a0: _QuadraticFieldClockModel__T, a1: _QuadraticFieldClockModel__T, a2: _QuadraticFieldClockModel__T):
        """
        Simple constructor.
        
        Parameters:
            referenceDate (FieldAbsoluteDate<QuadraticFieldClockModel> referenceDate): reference date
            a0 (QuadraticFieldClockModel): constant term
            a1 (QuadraticFieldClockModel): linear term
            a2 (QuadraticFieldClockModel): quadratic term
        
        
        """
        ...
    def getOffset(self, date: org.orekit.time.FieldAbsoluteDate[_QuadraticFieldClockModel__T]) -> org.orekit.time.FieldClockOffset[_QuadraticFieldClockModel__T]:
        """
        Get the clock offset at date.
        
        Parameters:
            date (FieldAbsoluteDate<QuadraticFieldClockModel> date): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        
        """
        ...

_EstimatedMeasurementBase__T = typing.TypeVar('_EstimatedMeasurementBase__T', bound='ObservedMeasurement')  # <T>
class EstimatedMeasurementBase(ComparableMeasurement, typing.Generic[_EstimatedMeasurementBase__T]):
    """
    Class holding an estimated theoretical value associated to an ObservedMeasurement.
    
    Since:
        8.0
    """
    def __init__(self, observedMeasurement: _EstimatedMeasurementBase__T, iteration: int, count: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray], participants: typing.Union[typing.List[org.orekit.utils.TimeStampedPVCoordinates], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            observedMeasurement (EstimatedMeasurementBase): associated observed measurement
            iteration (int): iteration number
            count (int): evaluations counter
            states (SpacecraftState[]): states of the spacecrafts
            participants (TimeStampedPVCoordinates[]): coordinates of the participants in signal travel order in inertial frame of first state
        
        
        """
        ...
    def getAppliedEffects(self) -> java.util.Map[EstimationModifier[_EstimatedMeasurementBase__T], typing.MutableSequence[float]]:
        """
        Get the applied effects of modifiers.
        
        The effects have already accounted for in getEstimatedValue
        
        Returns:
            applied modifier effects
        
        Since:
            12.1
        
        
        """
        ...
    def getCount(self) -> int:
        """
        Get the evaluations counter.
        
        Returns:
            evaluations counter
        
        
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
    def getEstimatedValue(self) -> typing.MutableSequence[float]:
        """
        Get the estimated value.
        
        Returns:
            estimated value
        
        
        """
        ...
    def getIteration(self) -> int:
        """
        Get the iteration number.
        
        Returns:
            iteration number
        
        
        """
        ...
    def getObservedMeasurement(self) -> _EstimatedMeasurementBase__T:
        """
        Get the associated observed measurement.
        
        Returns:
            associated observed measurement
        
        
        """
        ...
    def getObservedValue(self) -> typing.MutableSequence[float]:
        """
        Get the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Specified by: getObservedValue in interface ComparableMeasurement
        
        Returns:
            observed value
        
        
        """
        ...
    def getOriginalEstimatedValue(self) -> typing.MutableSequence[float]:
        """
        Get the original estimated value prior to any modification.
        
        Returns:
            original estimated value prior to any modification
        
        Since:
            12.1
        
        
        """
        ...
    def getParticipants(self) -> typing.MutableSequence[org.orekit.utils.TimeStampedPVCoordinates]:
        """
        Get the coordinates of the measurements participants in signal travel order.
        
        First participant (at index 0) emits the signal (it is for example a ground station for two-way range measurement). Last participant receives the signal (it is also the ground station for two-way range measurement, but a few milliseconds later). Intermediate participants relfect the signal (it is the spacecraft for two-way range measurement).
        
        Returns:
            coordinates of the measurements participants in signal travel order in inertial frame of first state
        
        
        """
        ...
    def getStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the states of the spacecrafts.
        
        Returns:
            states of the spacecrafts
        
        
        """
        ...
    def getStatus(self) -> 'EstimatedMeasurementBase.Status':
        """
        Get the status.
        
        The status is set to PROCESSED at construction, and can be reset to REJECTED later on, typically by OutlierFilter or DynamicOutlierFilter
        
        Returns:
            status
        
        
        """
        ...
    def getTimeOffset(self) -> float:
        """
        Get the time offset from first state date to measurement date.
        
        Returns:
            time offset from first state date to measurement date
        
        
        """
        ...
    def modifyEstimatedValue(self, modifier: EstimationModifier[_EstimatedMeasurementBase__T], *newEstimatedValue: float) -> None:
        """
        Modify the estimated value.
        
        Parameters:
            modifier (EstimationModifier<EstimatedMeasurementBase> modifier): modifier that generates this estimated value
            newEstimatedValue (double...): new estimated value
        
        Since:
            12.1
        
        
        """
        ...
    def setEstimatedValue(self, *estimatedValue: float) -> None:
        """
        Set the estimated value.
        
        Parameters:
            estimatedValue (double...): estimated value
        
        Also see:
            modifyEstimatedValue
        
        
        """
        ...
    def setObservedValue(self, observed: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Specified by: setObservedValue in interface ComparableMeasurement
        
        Parameters:
            observed (double[]): observed value
        
        
        """
        ...
    def setStatus(self, status: 'EstimatedMeasurementBase.Status') -> None:
        """
        Set the status.
        
        Parameters:
            status (Status): status to set
        
        
        """
        ...
    class Status(java.lang.Enum['EstimatedMeasurementBase.Status']):
        PROCESSED: typing.ClassVar['EstimatedMeasurementBase.Status'] = ...
        REJECTED: typing.ClassVar['EstimatedMeasurementBase.Status'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'EstimatedMeasurementBase.Status': ...
        @staticmethod
        def values() -> typing.MutableSequence['EstimatedMeasurementBase.Status']: ...

class GroundReceiverCommonParametersWithDerivatives(CommonParametersWithDerivatives):
    """
    Common intermediate parameters used to estimate measurements where receiver is a ground station.
    
    Since:
        12.0
    """
    def __init__(self, state: org.orekit.propagation.SpacecraftState, indices: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]], offsetToInertialDownlink: org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient], stationDownlink: org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient], tauD: org.hipparchus.analysis.differentiation.Gradient, transitState: org.orekit.propagation.SpacecraftState, transitPV: org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]):
        """
        Simple constructor.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            indices (Map<String, Integer> indices): derivatives indices map
            offsetToInertialDownlink (FieldTransform<Gradient> offsetToInertialDownlink): transform between station and inertial frame
            stationDownlink (TimeStampedFieldPVCoordinates<Gradient> stationDownlink): station position in inertial frame at end of the downlink leg
            tauD (Gradient): downlink delay
            transitState (SpacecraftState): transit state
            transitPV (TimeStampedFieldPVCoordinates<Gradient> transitPV): transit position/velocity as a gradient
        
        
        """
        ...
    def getOffsetToInertialDownlink(self) -> org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get transform between station and inertial frame.
        
        Returns:
            transform between station and inertial frame
        
        
        """
        ...
    def getStationDownlink(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get station position in inertial frame at end of the downlink leg.
        
        Returns:
            station position in inertial frame at end of the downlink leg
        
        
        """
        ...

class GroundReceiverCommonParametersWithoutDerivatives(CommonParametersWithoutDerivatives):
    """
    Common intermediate parameters used to estimate measurements where receiver is a ground station.
    
    Since:
        12.0
    """
    def __init__(self, state: org.orekit.propagation.SpacecraftState, offsetToInertialDownlink: org.orekit.frames.Transform, stationDownlink: org.orekit.utils.TimeStampedPVCoordinates, tauD: float, transitState: org.orekit.propagation.SpacecraftState, transitPV: org.orekit.utils.TimeStampedPVCoordinates):
        """
        Simple constructor.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            offsetToInertialDownlink (Transform): transform between station and inertial frame
            stationDownlink (TimeStampedPVCoordinates): station position in inertial frame at end of the downlink leg
            tauD (double): downlink delay
            transitState (SpacecraftState): transit state
            transitPV (TimeStampedPVCoordinates): transit position/velocity
        
        
        """
        ...
    def getOffsetToInertialDownlink(self) -> org.orekit.frames.Transform:
        """
        Get transform between station and inertial frame.
        
        Returns:
            transform between station and inertial frame
        
        
        """
        ...
    def getStationDownlink(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get station position in inertial frame at end of the downlink leg.
        
        Returns:
            station position in inertial frame at end of the downlink leg
        
        
        """
        ...

_ObservedMeasurement__T = typing.TypeVar('_ObservedMeasurement__T', bound='ObservedMeasurement')  # <T>
class ObservedMeasurement(ComparableMeasurement, org.orekit.utils.ParameterDriversProvider, typing.Generic[_ObservedMeasurement__T]):
    """
    Interface for measurements used for orbit determination.
    
    The most important methods of this interface allow to:
    
      - get the observed value,
      - estimate the theoretical value of a measurement,
      - compute the corresponding partial derivatives (with respect to state and parameters)
    
    The estimated theoretical values can be modified by registering one or several EstimationModifier objects. These objects will manage notions like tropospheric delays, biases...
    
    Since:
        8.0
    """
    def addModifier(self, modifier: EstimationModifier[_ObservedMeasurement__T]) -> None:
        """
        Add a modifier.
        
        The modifiers are applied in the order in which they are added in order to estimate the measurement.
        
        Parameters:
            modifier (EstimationModifier<ObservedMeasurement> modifier): modifier to add
        
        Also see:
            getModifiers
        
        
        """
        ...
    def estimate(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> 'EstimatedMeasurement'[_ObservedMeasurement__T]:
        """
        Estimate the theoretical value of the measurement, with derivatives.
        
        The estimated value is the combination of the raw estimated value and all the modifiers that apply to the measurement.
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluations number
            states (SpacecraftState[]): orbital states corresponding to getSatellites at
                measurement date
        
        Returns:
            estimated measurement
        
        
        """
        ...
    @typing.overload
    def estimateWithoutDerivatives(self, int: int, int2: int, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_ObservedMeasurement__T]: ...
    @typing.overload
    def estimateWithoutDerivatives(self, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_ObservedMeasurement__T]: ...
    def getBaseWeight(self) -> typing.MutableSequence[float]:
        """
        Get the base weight associated with the measurement
        
        The base weight is used on residuals already normalized thanks to getTheoreticalStandardDeviation to increase or decrease relative effect of some measurements with respect to other measurements. It is a dimensionless value, typically between 0 and 1 (but it can really have any non-negative value).
        
        Returns:
            base weight
        
        Also see:
            getTheoreticalStandardDeviation
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the measurement.
        
        Dimension is the size of the array containing the value. It will be one for a scalar measurement like a range or range-rate, but 6 for a position-velocity measurement.
        
        Returns:
            dimension of the measurement
        
        
        """
        ...
    def getMeasurementType(self) -> str:
        """
        Get the type of measurement.
        
        Default behavior is to return the class simple name as a String.
        
        Returns:
            type of measurement
        
        
        """
        ...
    def getModifiers(self) -> java.util.List[EstimationModifier[_ObservedMeasurement__T]]:
        """
        Get the modifiers that apply to a measurement.
        
        Returns:
            modifiers that apply to a measurement
        
        Also see:
            addModifier
        
        
        """
        ...
    def getSatellites(self) -> java.util.List[ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Returns:
            satellites related to this measurement
        
        Since:
            9.3
        
        
        """
        ...
    def getTheoreticalStandardDeviation(self) -> typing.MutableSequence[float]:
        """
        Get the theoretical standard deviation.
        
        The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
        Returns:
            expected standard deviation
        
        Also see:
            getBaseWeight
        
        
        """
        ...
    def isEnabled(self) -> bool:
        """
        Check if a measurement is enabled.
        
        Returns:
            true if the measurement is enabled
        
        
        """
        ...
    def setEnabled(self, enabled: bool) -> None:
        """
        Enable or disable a measurement.
        
        Disabling a measurement allow to not consider it at one stage of the orbit determination (for example when it appears to be an outlier as per current estimated covariance).
        
        Parameters:
            enabled (boolean): if true the measurement will be enabled, otherwise it will be disabled
        
        
        """
        ...

class PythonComparableMeasurement(ComparableMeasurement):
    def __init__(self): ...
    def compareTo(self, comparableMeasurement: ComparableMeasurement) -> int:
        """
        Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed value. Even if they have the same value too, they will likely not be considered equal if they correspond to different instances.
        
        Care should be taken before storing measurements in a SortedSet as it may lose redundant measurements if they, by chance, have the same identity hash code.
        
        Specified by: Comparable in interface Comparable
        
        Specified by: compareTo in interface ComparableMeasurement
        
        Also see:
            System
        
        
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
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getObservedValue(self) -> typing.MutableSequence[float]:
        """
        Get the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Specified by: getObservedValue in interface ComparableMeasurement
        
        Returns:
            observed value
        
        
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
    def setObservedValue(self, newObserved: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Specified by: setObservedValue in interface ComparableMeasurement
        
        Parameters:
            newObserved (double[]): observed value
        
        
        """
        ...

_PythonEstimationModifier__T = typing.TypeVar('_PythonEstimationModifier__T', bound=ObservedMeasurement)  # <T>
class PythonEstimationModifier(EstimationModifier[_PythonEstimationModifier__T], typing.Generic[_PythonEstimationModifier__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: 'EstimatedMeasurement'[_PythonEstimationModifier__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<PythonEstimationModifier> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: EstimatedMeasurementBase[_PythonEstimationModifier__T]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<PythonEstimationModifier> estimated): estimated measurement to modify
        
        
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

class PythonEstimationsProvider(EstimationsProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEstimatedMeasurement(self, index: int) -> 'EstimatedMeasurement'[typing.Any]:
        """
        Get one estimated measurement.
        
        Specified by: getEstimatedMeasurement in interface EstimationsProvider
        
        Parameters:
            index (int): index of the estimated measurement, must be between 0 and
                getNumber - 1, chronologically sorted
        
        Returns:
            estimated measurement at specified index
        
        
        """
        ...
    def getNumber(self) -> int:
        """
        Get the number of evaluations available.
        
        Specified by: getNumber in interface EstimationsProvider
        
        Returns:
            number of evaluations available
        
        
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

_AbstractMeasurement__T = typing.TypeVar('_AbstractMeasurement__T', bound=ObservedMeasurement)  # <T>
class AbstractMeasurement(ObservedMeasurement[_AbstractMeasurement__T], typing.Generic[_AbstractMeasurement__T]):
    """
    Abstract class handling measurements boilerplate.
    
    Since:
        8.0
    """
    def addModifier(self, modifier: EstimationModifier[_AbstractMeasurement__T]) -> None:
        """
        Add a modifier.
        
        The modifiers are applied in the order in which they are added in order to estimate the measurement.
        
        Specified by: addModifier in interface ObservedMeasurement
        
        Parameters:
            modifier (EstimationModifier<AbstractMeasurement> modifier): modifier to add
        
        Also see:
            getModifiers
        
        
        """
        ...
    def estimate(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> 'EstimatedMeasurement'[_AbstractMeasurement__T]:
        """
        Estimate the theoretical value of the measurement, with derivatives.
        
        The estimated value is the combination of the raw estimated value and all the modifiers that apply to the measurement.
        
        Specified by: estimate in interface ObservedMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluations number
            states (SpacecraftState[]): orbital states corresponding to getSatellites at
                measurement date
        
        Returns:
            estimated measurement
        
        
        """
        ...
    @typing.overload
    def estimateWithoutDerivatives(self, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_AbstractMeasurement__T]: ...
    @typing.overload
    def estimateWithoutDerivatives(self, int: int, int2: int, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_AbstractMeasurement__T]: ...
    def getBaseWeight(self) -> typing.MutableSequence[float]:
        """
        Get the base weight associated with the measurement
        
        The base weight is used on residuals already normalized thanks to getTheoreticalStandardDeviation to increase or decrease relative effect of some measurements with respect to other measurements. It is a dimensionless value, typically between 0 and 1 (but it can really have any non-negative value).
        
        Specified by: getBaseWeight in interface ObservedMeasurement
        
        Returns:
            base weight
        
        Also see:
            getTheoreticalStandardDeviation
        
        
        """
        ...
    @staticmethod
    def getCoordinates(state: org.orekit.propagation.SpacecraftState, firstDerivative: int, freeParameters: int) -> org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get Cartesian coordinates as derivatives.
        
        The position will correspond to variables firstDerivative, firstDerivative + 1 and firstDerivative + 2. The velocity will correspond to variables firstDerivative + 3, firstDerivative + 4 and firstDerivative + 5. The acceleration will correspond to constants.
        
        Parameters:
            state (SpacecraftState): state of the satellite considered
            firstDerivative (int): index of the first derivative
            freeParameters (int): total number of free parameters in the gradient
        
        Returns:
            Cartesian coordinates as derivatives
        
        Since:
            10.2
        
        
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
    def getDimension(self) -> int:
        """
        Get the dimension of the measurement.
        
        Dimension is the size of the array containing the value. It will be one for a scalar measurement like a range or range-rate, but 6 for a position-velocity measurement.
        
        Specified by: getDimension in interface ObservedMeasurement
        
        Returns:
            dimension of the measurement
        
        
        """
        ...
    def getModifiers(self) -> java.util.List[EstimationModifier[_AbstractMeasurement__T]]:
        """
        Get the modifiers that apply to a measurement.
        
        Specified by: getModifiers in interface ObservedMeasurement
        
        Returns:
            modifiers that apply to a measurement
        
        Also see:
            addModifier
        
        
        """
        ...
    def getObservedValue(self) -> typing.MutableSequence[float]:
        """
        Get the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Specified by: getObservedValue in interface ComparableMeasurement
        
        Returns:
            observed value
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getSatellites(self) -> java.util.List[ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Specified by: getSatellites in interface ObservedMeasurement
        
        Returns:
            satellites related to this measurement
        
        
        """
        ...
    def getTheoreticalStandardDeviation(self) -> typing.MutableSequence[float]:
        """
        Get the theoretical standard deviation.
        
        The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
        Specified by: getTheoreticalStandardDeviation in interface ObservedMeasurement
        
        Returns:
            expected standard deviation
        
        Also see:
            getBaseWeight
        
        
        """
        ...
    def isEnabled(self) -> bool:
        """
        Check if a measurement is enabled.
        
        Specified by: isEnabled in interface ObservedMeasurement
        
        Returns:
            true if the measurement is enabled
        
        
        """
        ...
    def setEnabled(self, enabled: bool) -> None:
        """
        Enable or disable a measurement.
        
        Disabling a measurement allow to not consider it at one stage of the orbit determination (for example when it appears to be an outlier as per current estimated covariance).
        
        Specified by: setEnabled in interface ObservedMeasurement
        
        Parameters:
            enabled (boolean): if true the measurement will be enabled, otherwise it will be disabled
        
        
        """
        ...
    def setObservedValue(self, newObserved: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Specified by: setObservedValue in interface ComparableMeasurement
        
        Parameters:
            newObserved (double[]): observed value
        
        
        """
        ...
    _signalTimeOfFlightAdjustableEmitter_2__T = typing.TypeVar('_signalTimeOfFlightAdjustableEmitter_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _signalTimeOfFlightAdjustableEmitter_3__T = typing.TypeVar('_signalTimeOfFlightAdjustableEmitter_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableEmitter(adjustableEmitter: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], approxEmissionDate: org.orekit.time.AbsoluteDate, receiverPosition: org.hipparchus.geometry.euclidean.threed.Vector3D, signalArrivalDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> float:
        """
        Parameters:
            adjustableEmitter (PVCoordinatesProvider): position/velocity provider of emitter
            approxEmissionDate (AbsoluteDate): approximate emission date
            receiverPosition (Vector3D): fixed position of receiver at signalArrivalDate
            signalArrivalDate (AbsoluteDate): date at which the signal arrives to receiver
            frame (Frame): inertial frame in which receiver is defined
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableEmitter(adjustableEmitterPV: org.orekit.utils.TimeStampedPVCoordinates, receiverPosition: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.time.AbsoluteDate, signalArrivalDate: org.orekit.frames.Frame) -> float:
        """
        Parameters:
            adjustableEmitterPV (TimeStampedPVCoordinates): position/velocity of emitter that may be adjusted
            receiverPosition (Vector3D): fixed position of receiver at signalArrivalDate
            frame (AbsoluteDate): inertial frame in which both adjustableEmitterPV and receiverPosition are defined
            signalArrivalDate (Frame): date at which the signal arrives to receiver
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableEmitter(adjustableEmitter: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_signalTimeOfFlightAdjustableEmitter_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], approxEmissionDate: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlightAdjustableEmitter_2__T], receiverPosition: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_signalTimeOfFlightAdjustableEmitter_2__T], signalArrivalDate: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlightAdjustableEmitter_2__T], frame: org.orekit.frames.Frame) -> _signalTimeOfFlightAdjustableEmitter_2__T:
        """
        Parameters:
            adjustableEmitter (FieldPVCoordinatesProvider<T> adjustableEmitter): position/velocity provider of emitter
            approxEmissionDate (FieldAbsoluteDate<T> approxEmissionDate): approximate emission date
            receiverPosition (FieldVector3D<T> receiverPosition): fixed position of receiver at signalArrivalDate, in the same frame as adjustableEmitterPV
            signalArrivalDate (FieldAbsoluteDate<T> signalArrivalDate): date at which the signal arrives to receiver
            frame (Frame): inertial frame in which receiver is defined
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableEmitter(adjustableEmitterPV: org.orekit.utils.TimeStampedFieldPVCoordinates[_signalTimeOfFlightAdjustableEmitter_3__T], receiverPosition: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_signalTimeOfFlightAdjustableEmitter_3__T], signalArrivalDate: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlightAdjustableEmitter_3__T], frame: org.orekit.frames.Frame) -> _signalTimeOfFlightAdjustableEmitter_3__T:
        """
        Parameters:
            adjustableEmitterPV (TimeStampedFieldPVCoordinates<T> adjustableEmitterPV): position/velocity of emitter that may be adjusted
            receiverPosition (FieldVector3D<T> receiverPosition): fixed position of receiver at signalArrivalDate, in the same frame as adjustableEmitterPV
            signalArrivalDate (FieldAbsoluteDate<T> signalArrivalDate): date at which the signal arrives to receiver
            frame (Frame): inertial frame in which both adjustableEmitterPV and receiverPosition are defined
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        """
        ...
    _signalTimeOfFlightAdjustableReceiver_2__T = typing.TypeVar('_signalTimeOfFlightAdjustableReceiver_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _signalTimeOfFlightAdjustableReceiver_3__T = typing.TypeVar('_signalTimeOfFlightAdjustableReceiver_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableReceiver(vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate2: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> float:
        """
        Parameters:
            emitterPosition (Vector3D): fixed position of emitter
            emissionDate (AbsoluteDate): emission date
            adjustableReceiverPV (TimeStampedPVCoordinates): position/velocity of receiver that may be adjusted
            approxReceptionDate (AbsoluteDate): approximate reception date
            frame (Frame): inertial frame in which both emitterPosition and adjustableReceiverPV are defined
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        Compute propagation delay on a link leg (typically downlink or uplink).
        
        Parameters:
            emitterPosition (Vector3D): fixed position of emitter
            emissionDate (AbsoluteDate): emission date
            adjustableReceiver (PVCoordinatesProvider): provider for adjusting receiver position
            approxReceptionDate (AbsoluteDate): approximate reception date
            frame (Frame): inertial frame in which emitter is defined
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableReceiver(vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, absoluteDate2: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableReceiver(fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_signalTimeOfFlightAdjustableReceiver_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlightAdjustableReceiver_2__T], fieldPVCoordinatesProvider: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_signalTimeOfFlightAdjustableReceiver_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlightAdjustableReceiver_2__T], frame: org.orekit.frames.Frame) -> _signalTimeOfFlightAdjustableReceiver_2__T:
        """
        Parameters:
            emitterPosition (FieldVector3D<T> emitterPosition): fixed position of emitter
            emissionDate (FieldAbsoluteDate<T> emissionDate): emission date
            adjustableReceiverPV (TimeStampedFieldPVCoordinates<T> adjustableReceiverPV): position/velocity of emitter that may be adjusted
            approxReceptionDate (FieldAbsoluteDate<T> approxReceptionDate): approximate reception date
            frame (Frame): inertial frame in which both emitterPosition and adjustableReceiverPV are defined
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        Compute propagation delay on a link leg (typically downlink or uplink).
        
        Parameters:
            emitterPosition (FieldVector3D<T> emitterPosition): fixed position of emitter
            emissionDate (FieldAbsoluteDate<T> emissionDate): emission date
            adjustableReceiver (FieldPVCoordinatesProvider<T> adjustableReceiver): provider for adjusting receiver position
            approxReceptionDate (FieldAbsoluteDate<T> approxReceptionDate): approximate reception date
            frame (Frame): inertial frame in which emitter is defined
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def signalTimeOfFlightAdjustableReceiver(fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_signalTimeOfFlightAdjustableReceiver_3__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlightAdjustableReceiver_3__T], timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_signalTimeOfFlightAdjustableReceiver_3__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlightAdjustableReceiver_3__T], frame: org.orekit.frames.Frame) -> _signalTimeOfFlightAdjustableReceiver_3__T: ...

_EstimatedMeasurement__T = typing.TypeVar('_EstimatedMeasurement__T', bound=ObservedMeasurement)  # <T>
class EstimatedMeasurement(EstimatedMeasurementBase[_EstimatedMeasurement__T], typing.Generic[_EstimatedMeasurement__T]):
    """
    Class holding an estimated theoretical value associated to an ObservedMeasurement.
    
    Since:
        8.0
    """
    @typing.overload
    def __init__(self, estimatedMeasurementBase: EstimatedMeasurementBase[_EstimatedMeasurement__T]): ...
    @typing.overload
    def __init__(self, t: _EstimatedMeasurement__T, int: int, int2: int, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray], timeStampedPVCoordinatesArray: typing.Union[typing.List[org.orekit.utils.TimeStampedPVCoordinates], jpype.JArray]): ...
    def getDerivativesDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
        Get all the drivers with set derivatives.
        
        Returns:
            all the drivers with set derivatives
        
        Since:
            9.0
        
        
        """
        ...
    @typing.overload
    def getParameterDerivatives(self, parameterDriver: org.orekit.utils.ParameterDriver) -> typing.MutableSequence[float]: ...
    @typing.overload
    def getParameterDerivatives(self, parameterDriver: org.orekit.utils.ParameterDriver, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    def getStateDerivatives(self, index: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the partial derivatives of the getEstimatedValue with respect to state Cartesian coordinates.
        
        Parameters:
            index (int): index of the state, according to the states passed at construction
        
        Returns:
            partial derivatives of the simulated value (array of size
            getDimension x 6)
        
        
        """
        ...
    def getStateSize(self) -> int:
        """
        Get state size.
        
        Warning, the setStateDerivatives method must have been called before this method is called.
        
        Returns:
            state size
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def setParameterDerivatives(self, driver: org.orekit.utils.ParameterDriver, date: org.orekit.time.AbsoluteDate, *parameterDerivatives: float) -> None:
        """
        Set the partial derivatives of the getEstimatedValue with respect to parameter.
        
        Parameters:
            driver (ParameterDriver): name of the span of the driver for the parameter for which the derivative wants to be known.
            date (AbsoluteDate): date at which the parameterDerivative wants to be set
            parameterDerivatives (double...): partial derivatives with respect to parameter
        
        """
        ...
    @typing.overload
    def setParameterDerivatives(self, driver: org.orekit.utils.ParameterDriver, parameterDerivativesMap: org.orekit.utils.TimeSpanMap[typing.Union[typing.List[float], jpype.JArray]]) -> None:
        """
        Set the partial derivatives of the getEstimatedValue with respect to parameter.
        
        Parameters:
            driver (ParameterDriver): driver for the parameter
            parameterDerivativesMap (TimeSpanMap<double[]> parameterDerivativesMap): partial derivatives with respect to parameter
        
        
        """
        ...
    def setStateDerivatives(self, index: int, *derivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the partial derivatives of the getEstimatedValue with respect to state Cartesian coordinates.
        
        Parameters:
            index (int): index of the state, according to the states passed at construction
            derivatives (double[]...): partial derivatives with respect to state
        
        
        """
        ...

_PythonObservedMeasurement__T = typing.TypeVar('_PythonObservedMeasurement__T', bound=ObservedMeasurement)  # <T>
class PythonObservedMeasurement(ObservedMeasurement[_PythonObservedMeasurement__T], typing.Generic[_PythonObservedMeasurement__T]):
    def __init__(self): ...
    def addModifier(self, modifier: EstimationModifier[_PythonObservedMeasurement__T]) -> None:
        """
        Add a modifier.
        
        The modifiers are applied in the order in which they are added in order to estimate the measurement.
        
        Specified by: addModifier in interface ObservedMeasurement
        
        Parameters:
            modifier (EstimationModifier<PythonObservedMeasurement> modifier): modifier to add
        
        Also see:
            getModifiers
        
        
        """
        ...
    def compareTo(self, other: ComparableMeasurement) -> int:
        """
        Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed value. Even if they have the same value too, they will likely not be considered equal if they correspond to different instances.
        
        Care should be taken before storing measurements in a SortedSet as it may lose redundant measurements if they, by chance, have the same identity hash code.
        
        Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed value. Even if they have the same value too, they will not be considered equal if they correspond to different instances. This allows to store measurements in SortedSet without losing any measurements, even redundant ones.
        
        Specified by: Comparable in interface Comparable
        
        Specified by: compareTo in interface ComparableMeasurement
        
        Parameters:
            other (ComparableMeasurement): 
        Also see:
            System
        
        
        """
        ...
    def estimate(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurement[_PythonObservedMeasurement__T]:
        """
        Estimate the theoretical value of the measurement.
        
        The estimated value is the combination of the raw estimated value and all the modifiers that apply to the measurement.
        
        Specified by: estimate in interface ObservedMeasurement
        
        Parameters:
            iteration (int): iteration number
            evaluation (int): evaluations number
            states (SpacecraftState[]): orbital states at measurement date
        
        Returns:
            estimated measurement
        
        
        """
        ...
    @typing.overload
    def estimateWithoutDerivatives(self, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_PythonObservedMeasurement__T]: ...
    @typing.overload
    def estimateWithoutDerivatives(self, int: int, int2: int, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_PythonObservedMeasurement__T]: ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBaseWeight(self) -> typing.MutableSequence[float]:
        """
        Get the base weight associated with the measurement
        
        The base weight is used on residuals already normalized thanks to getTheoreticalStandardDeviation to increase or decrease relative effect of some measurements with respect to other measurements. It is a dimensionless value, typically between 0 and 1 (but it can really have any non-negative value).
        
        Specified by: getBaseWeight in interface ObservedMeasurement
        
        Returns:
            base weight
        
        Also see:
            getTheoreticalStandardDeviation
        
        
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
    def getDimension(self) -> int:
        """
        Get the dimension of the measurement.
        
        Dimension is the size of the array containing the value. It will be one for a scalar measurement like a range or range-rate, but 6 for a position-velocity measurement.
        
        Specified by: getDimension in interface ObservedMeasurement
        
        Returns:
            dimension of the measurement
        
        
        """
        ...
    def getMeasurementType(self) -> str:
        """
        Get the type of measurement.
        
        Specified by: getMeasurementType in interface ObservedMeasurement
        
        Returns:
            type of measurement
        
        
        """
        ...
    def getModifiers(self) -> java.util.List[EstimationModifier[_PythonObservedMeasurement__T]]:
        """
        Get the modifiers that apply to a measurement.
        
        Specified by: getModifiers in interface ObservedMeasurement
        
        Returns:
            modifiers that apply to a measurement
        
        Also see:
            addModifier
        
        
        """
        ...
    def getObservedValue(self) -> typing.MutableSequence[float]:
        """
        Get the observed value.
        
        The observed value is the value that was measured by the instrument.
        
        Specified by: getObservedValue in interface ComparableMeasurement
        
        Returns:
            observed value (array of size getDimension
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for this measurement parameters, including its modifiers parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for this measurement parameters, including its modifiers parameters
        
        
        """
        ...
    def getSatellites(self) -> java.util.List[ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Specified by: getSatellites in interface ObservedMeasurement
        
        Returns:
            satellites related to this measurement
        
        Since:
            9.3
        
        
        """
        ...
    def getTheoreticalStandardDeviation(self) -> typing.MutableSequence[float]:
        """
        Get the theoretical standard deviation.
        
        The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
        Specified by: getTheoreticalStandardDeviation in interface ObservedMeasurement
        
        Returns:
            expected standard deviation
        
        Also see:
            getBaseWeight
        
        
        """
        ...
    def isEnabled(self) -> bool:
        """
        Check if a measurement is enabled.
        
        Specified by: isEnabled in interface ObservedMeasurement
        
        Returns:
            true if the measurement is enabled
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def setEnabled(self, enabled: bool) -> None:
        """
        Enable or disable a measurement.
        
        Disabling a measurement allow to not consider it at one stage of the orbit determination (for example when it appears to be an outlier as per current estimated covariance).
        
        Specified by: setEnabled in interface ObservedMeasurement
        
        Parameters:
            enabled (boolean): if true the measurement will be enabled, otherwise it will be disabled
        
        
        """
        ...
    def setObservedValue(self, observedValue: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the observed value.
        
        This method allows setting the value that was measured by the instrument.
        
        Specified by: setObservedValue in interface ComparableMeasurement
        
        Parameters:
            observedValue (double[]): the observed value (array of size getDimension)
        
        
        """
        ...

_GroundReceiverMeasurement__T = typing.TypeVar('_GroundReceiverMeasurement__T', bound='GroundReceiverMeasurement')  # <T>
class GroundReceiverMeasurement(AbstractMeasurement[_GroundReceiverMeasurement__T], typing.Generic[_GroundReceiverMeasurement__T]):
    """
    Base class modeling a measurement where receiver is a ground station.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, groundStation: GroundStation, boolean: bool, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, groundStation: GroundStation, boolean: bool, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray], observableSatellite: ObservableSatellite): ...
    def getGroundStationCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.PVCoordinates:
        """
        Get the station coordinates for a given frame.
        
        Parameters:
            frame (Frame): inertial frame for station position
        
        Returns:
            the station coordinates in the given inertial frame
        
        Since:
            12.0
        
        
        """
        ...
    def getGroundStationPosition(self, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the station position for a given frame.
        
        Parameters:
            frame (Frame): inertial frame for station position
        
        Returns:
            the station position in the given inertial frame
        
        Since:
            12.0
        
        
        """
        ...
    def getStation(self) -> GroundStation:
        """
        Get the ground station from which measurement is performed.
        
        Returns:
            ground station from which measurement is performed
        
        
        """
        ...
    def isTwoWay(self) -> bool:
        """
        Check if the instance represents a two-way measurement.
        
        Returns:
            true if the instance represents a two-way measurement
        
        
        """
        ...

class InterSatellitesRange(AbstractMeasurement['InterSatellitesRange']):
    """
    One-way or two-way range measurements between two satellites.
    
    For one-way measurements, a signal is emitted by a remote satellite and received by local satellite. The measurement value is the elapsed time between emission and reception multiplied by c where c is the speed of light.
    
    For two-way measurements, a signal is emitted by local satellite, reflected on remote satellite, and received back by local satellite. The measurement value is the elapsed time between emission and reception multiplied by c/2 where c is the speed of light.
    
    Since 9.3, this class also uses the clock offsets of both satellites, which manage the value that must be added to each satellite reading of time to compute the real physical date. In this measurement, these offsets have two effects:
    
      - as measurement date is evaluated at reception time, the real physical date of the measurement is the observed date to
        which the local satellite clock offset is subtracted
      - as range is evaluated using the total signal time of flight, for one-way measurements the observed range is the real
        physical signal time of flight to which (Δtl - Δtr) ⨯ c is added, where Δtl (resp. Δtr) is the clock offset for
        the local satellite (resp. remote satellite). A similar effect exists in two-way measurements but it is computed as
        (Δtl - Δtl) ⨯ c / 2 as the local satellite clock is used for both initial emission and final reception and therefore
        it evaluates to zero.
    
    The motion of both satellites during the signal flight time is taken into account. The date of the measurement corresponds to the reception of the signal by satellite 1.
    
    Since:
        9.0
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, local: ObservableSatellite, remote: ObservableSatellite, twoWay: bool, date: org.orekit.time.AbsoluteDate, range: float, sigma: float, baseWeight: float):
        """
        Simple constructor.
        
        Parameters:
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): satellite which simply emits the signal in the one-way case, or reflects the signal in the two-way case
            twoWay (boolean): flag indicating whether it is a two-way measurement
            date (AbsoluteDate): date of the measurement
            range (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
        
        Since:
            9.3
        
        
        """
        ...
    def isTwoWay(self) -> bool:
        """
        Check if the instance represents a two-way measurement.
        
        Returns:
            true if the instance represents a two-way measurement
        
        
        """
        ...

class MultiplexedMeasurement(AbstractMeasurement['MultiplexedMeasurement']):
    """
    Class multiplexing several measurements as one.
    
    Date comes from the first measurement, observed and estimated values result from gathering all underlying measurements values.
    
    Since:
        10.1
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, measurements: java.util.List[ObservedMeasurement[typing.Any]]):
        """
        Simple constructor.
        
        Parameters:
            measurements (List<ObservedMeasurement<?>>): measurements to multiplex
        
        Since:
            10.1
        
        
        """
        ...
    def getEstimatedMeasurements(self) -> java.util.List[EstimatedMeasurement[typing.Any]]:
        """
        Get the underlying estimated measurements.
        
        Returns:
            underlying estimated measurements
        
        
        """
        ...
    def getEstimatedMeasurementsWithoutDerivatives(self) -> java.util.List[EstimatedMeasurementBase[typing.Any]]:
        """
        Get the underlying estimated measurements without derivatives.
        
        Returns:
            underlying estimated measurements without derivatives
        
        Since:
            12.0
        
        
        """
        ...
    def getMeasurements(self) -> java.util.List[ObservedMeasurement[typing.Any]]:
        """
        Get the underlying measurements.
        
        Returns:
            underlying measurements
        
        
        """
        ...
    def getMultiplexedStateIndex(self, measurementIndex: int, underlyingStateIndex: int) -> int:
        """
        Get the spacecraft state index in the multiplexed measurement.
        
        Parameters:
            measurementIndex (int): index of the underlying measurement
            underlyingStateIndex (int): index of the spacecraft state in the underlying array
        
        Returns:
            spacecraft state index in the multiplexed measurement
        
        Since:
            13.0
        
        
        """
        ...
    def getUnderlyingStateIndex(self, measurementIndex: int, multiplexedStateIndex: int) -> int:
        """
        Get the spacecraft state index in the underlying measurement.
        
        Parameters:
            measurementIndex (int): index of the underlying measurement
            multiplexedStateIndex (int): index of the spacecraft state in the multiplexed array
        
        Returns:
            spacecraft state index in the underlying measurement
        
        Since:
            13.0
        
        
        """
        ...

class PV(AbstractMeasurement['PV']):
    """
    Class modeling a position-velocity measurement.
    
    For position-only measurement see Position.
    
    Since:
        8.0
    
    Also see:
        Position
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float, double3: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double3: float, observableSatellite: ObservableSatellite): ...
    def getCorrelationCoefficientsMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the correlation coefficients matrix.
        
        This is the 6x6 matrix M such that:
        
        Mij = Pij/(σi.σj)
        
        Where:
        
          - P is the covariance matrix
          - σi is the i-th standard deviation (σi² = Pii)
        
        
        Returns:
            the correlation coefficient matrix (6x6)
        
        
        """
        ...
    def getCovarianceMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the covariance matrix.
        
        Returns:
            the covariance matrix
        
        
        """
        ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position.
        
        Returns:
            position
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the velocity.
        
        Returns:
            velocity
        
        
        """
        ...

class Position(AbstractMeasurement['Position']):
    """
    Class modeling a position only measurement.
    
    For position-velocity measurement see PV.
    
    Since:
        9.3
    
    Also see:
        PV
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float, observableSatellite: ObservableSatellite): ...
    def getCorrelationCoefficientsMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the correlation coefficients matrix.
        
        This is the 3x3 matrix M such that:
        
        Mij = Pij/(σi.σj)
        
        Where:
        
          - P is the covariance matrix
          - σi is the i-th standard deviation (σi² = Pii)
        
        
        Returns:
            the correlation coefficient matrix (3x3)
        
        
        """
        ...
    def getCovarianceMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the covariance matrix.
        
        Returns:
            the covariance matrix
        
        
        """
        ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position.
        
        Returns:
            position
        
        
        """
        ...

_PythonAbstractMeasurement__T = typing.TypeVar('_PythonAbstractMeasurement__T', bound=ObservedMeasurement)  # <T>
class PythonAbstractMeasurement(AbstractMeasurement[_PythonAbstractMeasurement__T], typing.Generic[_PythonAbstractMeasurement__T]):
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, list: java.util.List[ObservableSatellite]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray], list: java.util.List[ObservableSatellite]): ...
    def addParameterDriver(self, driver: org.orekit.utils.ParameterDriver) -> None:
        """
        Add a parameter driver.
        
        Overrides: addParameterDriver in class AbstractMeasurement
        
        Parameters:
            driver (ParameterDriver): parameter driver to add
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def theoreticalEvaluation(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurement[_PythonAbstractMeasurement__T]:
        """
        Estimate the theoretical value.
        
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
    def theoreticalEvaluationWithoutDerivatives(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_PythonAbstractMeasurement__T]:
        """
        Estimate the theoretical value without derivatives. The default implementation uses the computation with derivatives and ought to be overwritten for performance.
        
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

class AngularAzEl(GroundReceiverMeasurement['AngularAzEl']):
    """
    Class modeling an Azimuth-Elevation measurement from a ground station. The motion of the spacecraft during the signal flight time is taken into account. The date of the measurement corresponds to the reception on ground of the reflected signal.
    
    Since:
        8.0
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, station: GroundStation, date: org.orekit.time.AbsoluteDate, angular: typing.Union[typing.List[float], jpype.JArray], sigma: typing.Union[typing.List[float], jpype.JArray], baseWeight: typing.Union[typing.List[float], jpype.JArray], satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            station (GroundStation): ground station from which measurement is performed
            date (AbsoluteDate): date of the measurement
            angular (double[]): observed value
            sigma (double[]): theoretical standard deviation
            baseWeight (double[]): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        Since:
            9.3
        
        
        """
        ...
    def getObservedLineOfSight(self, outputFrame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Calculate the Line Of Sight of the given measurement.
        
        Parameters:
            outputFrame (Frame): output frame of the line of sight vector
        
        Returns:
            Vector3D the line of Sight of the measurement
        
        
        """
        ...

class AngularRaDec(GroundReceiverMeasurement['AngularRaDec']):
    """
    Class modeling a Right Ascension - Declination measurement from a ground point (station, telescope). The angles are given in an inertial reference frame. The motion of the spacecraft during the signal flight time is taken into account. The date of the measurement corresponds to the reception on ground of the reflected signal.
    
    Since:
        9.0
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, station: GroundStation, referenceFrame: org.orekit.frames.Frame, date: org.orekit.time.AbsoluteDate, angular: typing.Union[typing.List[float], jpype.JArray], sigma: typing.Union[typing.List[float], jpype.JArray], baseWeight: typing.Union[typing.List[float], jpype.JArray], satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            station (GroundStation): ground station from which measurement is performed
            referenceFrame (Frame): Reference frame in which the right ascension - declination angles are given
            date (AbsoluteDate): date of the measurement
            angular (double[]): observed value
            sigma (double[]): theoretical standard deviation
            baseWeight (double[]): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        Since:
            9.3
        
        
        """
        ...
    def getObservedLineOfSight(self, outputFrame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Calculate the Line Of Sight of the given measurement.
        
        Parameters:
            outputFrame (Frame): output frame of the line of sight vector
        
        Returns:
            Vector3D the line of Sight of the measurement
        
        Since:
            12.0
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame in which the right ascension - declination angles are given.
        
        Returns:
            reference frame in which the right ascension - declination angles are given
        
        
        """
        ...

class BistaticRange(GroundReceiverMeasurement['BistaticRange']):
    """
    Class modeling a bistatic range measurement using an emitter ground station and a receiver ground station.
    
    The measurement is considered to be a signal:
    
      - Emitted from the emitter ground station
      - Reflected on the spacecraft
      - Received on the receiver ground station
    
    The date of the measurement corresponds to the reception on ground of the reflected signal.
    
    The motion of the stations and the spacecraft during the signal flight time are taken into account.
    
    Since:
        11.2
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, emitter: GroundStation, receiver: GroundStation, date: org.orekit.time.AbsoluteDate, range: float, sigma: float, baseWeight: float, satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            emitter (GroundStation): ground station from which transmission is performed
            receiver (GroundStation): ground station from which measurement is performed
            date (AbsoluteDate): date of the measurement
            range (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        Since:
            11.2
        
        
        """
        ...
    def getEmitterStation(self) -> GroundStation:
        """
        Get the emitter ground station.
        
        Returns:
            emitter ground station
        
        
        """
        ...
    def getReceiverStation(self) -> GroundStation:
        """
        Get the receiver ground station.
        
        Returns:
            receiver ground station
        
        
        """
        ...

class BistaticRangeRate(GroundReceiverMeasurement['BistaticRangeRate']):
    """
    Class modeling a bistatic range rate measurement using an emitter ground station and a receiver ground station.
    
    The measurement is considered to be a signal:
    
      - Emitted from the emitter ground station
      - Reflected on the spacecraft
      - Received on the receiver ground station
    
    The date of the measurement corresponds to the reception on ground of the reflected signal. The quantity measured at the receiver is the bistatic radial velocity as the sum of the radial velocities with respect to the two stations.
    
    The motion of the stations and the spacecraft during the signal flight time are taken into account.
    
    The Doppler measurement can be obtained by multiplying the velocity by (fe/c), where fe is the emission frequency.
    
    Since:
        11.2
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, emitter: GroundStation, receiver: GroundStation, date: org.orekit.time.AbsoluteDate, rangeRate: float, sigma: float, baseWeight: float, satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            emitter (GroundStation): emitter ground station
            receiver (GroundStation): receiver ground station
            date (AbsoluteDate): date of the measurement
            rangeRate (double): observed value, m/s
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        
        """
        ...
    def getEmitterStation(self) -> GroundStation:
        """
        Get the emitter ground station.
        
        Returns:
            emitter ground station
        
        
        """
        ...
    def getReceiverStation(self) -> GroundStation:
        """
        Get the receiver ground station.
        
        Returns:
            receiver ground station
        
        
        """
        ...

class FDOA(GroundReceiverMeasurement['FDOA']):
    """
    Class modeling a Frequency Difference of Arrival measurement with a satellite as emitter and two ground stations as receivers.
    
    FDOA measures the difference in signal arrival frequency between the emitter and receivers, corresponding to a difference in range-rate from the two receivers to the emitter.
    
    The date of the measurement corresponds to the reception of the signal by the prime station. The measurement corresponds to the frequency of the signal received at the prime station at the date of the measurement minus the frequency of the signal received at the second station: 1` - f :sub:`2``
    
    The motion of the stations and the satellite during the signal flight time are taken into account.
    
    Since:
        12.0
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, primeStation: GroundStation, secondStation: GroundStation, centreFrequency: float, date: org.orekit.time.AbsoluteDate, fdoa: float, sigma: float, baseWeight: float, satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            primeStation (GroundStation): ground station that gives the date of the measurement
            secondStation (GroundStation): ground station that gives the measurement
            centreFrequency (double): satellite emitter frequency (Hz)
            date (AbsoluteDate): date of the measurement
            fdoa (double): observed value (Hz)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        
        """
        ...
    def getPrimeStation(self) -> GroundStation:
        """
        Get the prime ground station, the one that gives the date of the measurement.
        
        Returns:
            prime ground station
        
        
        """
        ...
    def getSecondStation(self) -> GroundStation:
        """
        Get the second ground station, the one that gives the measurement.
        
        Returns:
            second ground station
        
        
        """
        ...

_PythonGroundReceiverMeasurement__T = typing.TypeVar('_PythonGroundReceiverMeasurement__T', bound=GroundReceiverMeasurement)  # <T>
class PythonGroundReceiverMeasurement(GroundReceiverMeasurement[_PythonGroundReceiverMeasurement__T], typing.Generic[_PythonGroundReceiverMeasurement__T]):
    @typing.overload
    def __init__(self, groundStation: GroundStation, boolean: bool, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, groundStation: GroundStation, boolean: bool, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray], observableSatellite: ObservableSatellite): ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def theoreticalEvaluation(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurement[_PythonGroundReceiverMeasurement__T]:
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
    def theoreticalEvaluationWithoutDerivatives(self, iteration: int, evaluation: int, states: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> EstimatedMeasurementBase[_PythonGroundReceiverMeasurement__T]:
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

class Range(GroundReceiverMeasurement['Range']):
    """
    Class modeling a range measurement from a ground station.
    
    For one-way measurements, a signal is emitted by the satellite and received by the ground station. The measurement value is the elapsed time between emission and reception multiplied by c where c is the speed of light.
    
    For two-way measurements, the measurement is considered to be a signal emitted from a ground station, reflected on spacecraft, and received on the same ground station. Its value is the elapsed time between emission and reception multiplied by c/2 where c is the speed of light.
    
    The motion of both the station and the spacecraft during the signal flight time are taken into account. The date of the measurement corresponds to the reception on ground of the emitted or reflected signal.
    
    The clock offsets of both the ground station and the satellite are taken into account. These offsets correspond to the values that must be subtracted from station (resp. satellite) reading of time to compute the real physical date. These offsets have two effects:
    
      - as measurement date is evaluated at reception time, the real physical date of the measurement is the observed date to
        which the receiving ground station clock offset is subtracted
      - as range is evaluated using the total signal time of flight, for one-way measurements the observed range is the real
        physical signal time of flight to which (Δtg - Δts) ⨯ c is added, where Δtg (resp. Δts) is the clock offset for
        the receiving ground station (resp. emitting satellite). A similar effect exists in two-way measurements but it is
        computed as (Δtg - Δtg) ⨯ c / 2 as the same ground station clock is used for initial emission and final reception
        and therefore it evaluates to zero.
    
    
    Since:
        8.0
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, station: GroundStation, twoWay: bool, date: org.orekit.time.AbsoluteDate, range: float, sigma: float, baseWeight: float, satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            station (GroundStation): ground station from which measurement is performed
            twoWay (boolean): flag indicating whether it is a two-way measurement
            date (AbsoluteDate): date of the measurement
            range (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        Since:
            9.3
        
        
        """
        ...

class RangeRate(GroundReceiverMeasurement['RangeRate']):
    """
    Class modeling one-way or two-way range rate measurement between two vehicles. One-way range rate (or Doppler) measurements generally apply to specific satellites (e.g. GNSS, DORIS), where a signal is transmitted from a satellite to a measuring station. Two-way range rate measurements are applicable to any system. The signal is transmitted to the (non-spinning) satellite and returned by a transponder (or reflected back)to the same measuring station. The Doppler measurement can be obtained by multiplying the velocity by (fe/c), where fe is the emission frequency.
    
    Since:
        8.0
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, station: GroundStation, date: org.orekit.time.AbsoluteDate, rangeRate: float, sigma: float, baseWeight: float, twoway: bool, satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            station (GroundStation): ground station from which measurement is performed
            date (AbsoluteDate): date of the measurement
            rangeRate (double): observed value, m/s
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            twoway (boolean): if true, this is a two-way measurement
            satellite (ObservableSatellite): satellite related to this measurement
        
        Since:
            9.3
        
        
        """
        ...

class TDOA(GroundReceiverMeasurement['TDOA']):
    """
    Class modeling a Time Difference of Arrival measurement with a satellite as emitter and two ground stations as receivers.
    
    TDOA measures the difference in signal arrival time between the emitter and receivers, corresponding to a difference in ranges from the two receivers to the emitter.
    
    The date of the measurement corresponds to the reception of the signal by the prime station. The measurement corresponds to the date of the measurement minus the date of reception of the signal by the second station: 1` - tr :sub:`2``
    
    The motion of the stations and the satellite during the signal flight time are taken into account.
    
    Since:
        11.2
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, primeStation: GroundStation, secondStation: GroundStation, date: org.orekit.time.AbsoluteDate, tdoa: float, sigma: float, baseWeight: float, satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            primeStation (GroundStation): ground station that gives the date of the measurement
            secondStation (GroundStation): ground station that gives the measurement
            date (AbsoluteDate): date of the measurement
            tdoa (double): observed value (s)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        
        """
        ...
    _forwardSignalTimeOfFlight_1__T = typing.TypeVar('_forwardSignalTimeOfFlight_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def forwardSignalTimeOfFlight(adjustableEmitterPV: org.orekit.utils.TimeStampedPVCoordinates, receiverPosition: org.hipparchus.geometry.euclidean.threed.Vector3D, signalArrivalDate: org.orekit.time.AbsoluteDate) -> float:
        """
        advancing rather than delaying the emitter.
        
        Parameters:
            adjustableEmitterPV (TimeStampedPVCoordinates): position/velocity of emitter that may be adjusted
            receiverPosition (Vector3D): fixed position of receiver at signalArrivalDate, in the same frame as adjustableEmitterPV
            signalArrivalDate (AbsoluteDate): date at which the signal arrives to receiver
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        """
        ...
    @typing.overload
    @staticmethod
    def forwardSignalTimeOfFlight(adjustableEmitterPV: org.orekit.utils.TimeStampedFieldPVCoordinates[_forwardSignalTimeOfFlight_1__T], receiverPosition: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_forwardSignalTimeOfFlight_1__T], signalArrivalDate: org.orekit.time.FieldAbsoluteDate[_forwardSignalTimeOfFlight_1__T]) -> _forwardSignalTimeOfFlight_1__T:
        """
        advancing rather than delaying the emitter.
        
        Parameters:
            adjustableEmitterPV (TimeStampedFieldPVCoordinates<T> adjustableEmitterPV): position/velocity of emitter that may be adjusted
            receiverPosition (FieldVector3D<T> receiverPosition): fixed position of receiver at signalArrivalDate, in the same frame as adjustableEmitterPV
            signalArrivalDate (FieldAbsoluteDate<T> signalArrivalDate): date at which the signal arrives to receiver
        
        Returns:
            positive delay between signal emission and signal reception dates
        
        
        """
        ...
    def getPrimeStation(self) -> GroundStation:
        """
        Get the prime ground station, the one that gives the date of the measurement.
        
        Returns:
            prime ground station
        
        
        """
        ...
    def getSecondStation(self) -> GroundStation:
        """
        Get the second ground station, the one that gives the measurement.
        
        Returns:
            second ground station
        
        
        """
        ...

class TurnAroundRange(GroundReceiverMeasurement['TurnAroundRange']):
    """
    Class modeling a turn-around range measurement using a primary ground station and a secondary ground station.
    
    The measurement is considered to be a signal: - Emitted from the primary ground station - Reflected on the spacecraft - Reflected on the secondary ground station - Reflected on the spacecraft again - Received on the primary ground station Its value is the elapsed time between emission and reception divided by 2c were c is the speed of light. The motion of the stations and the spacecraft during the signal flight time are taken into account. The date of the measurement corresponds to the reception on ground of the reflected signal.
    
    Since:
        9.0
    """
    MEASUREMENT_TYPE: typing.ClassVar[str] = ...
    """
    Type of the measurement.
    
    Also see:
        constant
    
    
    """
    def __init__(self, primaryStation: GroundStation, secondaryStation: GroundStation, date: org.orekit.time.AbsoluteDate, turnAroundRange: float, sigma: float, baseWeight: float, satellite: ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            primaryStation (GroundStation): ground station from which measurement is performed
            secondaryStation (GroundStation): ground station reflecting the signal
            date (AbsoluteDate): date of the measurement
            turnAroundRange (double): observed value
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this measurement
        
        Since:
            9.3
        
        
        """
        ...
    def getPrimaryStation(self) -> GroundStation:
        """
        Get the primary ground station from which measurement is performed.
        
        Returns:
            primary ground station from which measurement is performed
        
        
        """
        ...
    def getSecondaryStation(self) -> GroundStation:
        """
        Get the secondary ground station reflecting the signal.
        
        Returns:
            secondary ground station reflecting the signal
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements")``.

    AbstractMeasurement: typing.Type[AbstractMeasurement]
    AngularAzEl: typing.Type[AngularAzEl]
    AngularRaDec: typing.Type[AngularRaDec]
    BistaticRange: typing.Type[BistaticRange]
    BistaticRangeRate: typing.Type[BistaticRangeRate]
    CommonParametersWithDerivatives: typing.Type[CommonParametersWithDerivatives]
    CommonParametersWithoutDerivatives: typing.Type[CommonParametersWithoutDerivatives]
    ComparableMeasurement: typing.Type[ComparableMeasurement]
    EstimatedEarthFrameProvider: typing.Type[EstimatedEarthFrameProvider]
    EstimatedMeasurement: typing.Type[EstimatedMeasurement]
    EstimatedMeasurementBase: typing.Type[EstimatedMeasurementBase]
    EstimationModifier: typing.Type[EstimationModifier]
    EstimationsProvider: typing.Type[EstimationsProvider]
    FDOA: typing.Type[FDOA]
    GroundReceiverCommonParametersWithDerivatives: typing.Type[GroundReceiverCommonParametersWithDerivatives]
    GroundReceiverCommonParametersWithoutDerivatives: typing.Type[GroundReceiverCommonParametersWithoutDerivatives]
    GroundReceiverMeasurement: typing.Type[GroundReceiverMeasurement]
    GroundStation: typing.Type[GroundStation]
    InterSatellitesRange: typing.Type[InterSatellitesRange]
    MultiplexedMeasurement: typing.Type[MultiplexedMeasurement]
    ObservableSatellite: typing.Type[ObservableSatellite]
    ObservedMeasurement: typing.Type[ObservedMeasurement]
    PV: typing.Type[PV]
    Position: typing.Type[Position]
    PythonAbstractMeasurement: typing.Type[PythonAbstractMeasurement]
    PythonComparableMeasurement: typing.Type[PythonComparableMeasurement]
    PythonEstimationModifier: typing.Type[PythonEstimationModifier]
    PythonEstimationsProvider: typing.Type[PythonEstimationsProvider]
    PythonGroundReceiverMeasurement: typing.Type[PythonGroundReceiverMeasurement]
    PythonObservedMeasurement: typing.Type[PythonObservedMeasurement]
    QuadraticClockModel: typing.Type[QuadraticClockModel]
    QuadraticFieldClockModel: typing.Type[QuadraticFieldClockModel]
    Range: typing.Type[Range]
    RangeRate: typing.Type[RangeRate]
    TDOA: typing.Type[TDOA]
    TurnAroundRange: typing.Type[TurnAroundRange]
    filtering: org.orekit.estimation.measurements.filtering.__module_protocol__
    generation: org.orekit.estimation.measurements.generation.__module_protocol__
    gnss: org.orekit.estimation.measurements.gnss.__module_protocol__
    modifiers: org.orekit.estimation.measurements.modifiers.__module_protocol__
