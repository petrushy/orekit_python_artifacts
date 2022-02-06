import java.lang
import java.util
import java.util.stream
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



class ComparableMeasurement(org.orekit.time.TimeStamped, java.lang.Comparable['ComparableMeasurement']):
    """
    public interface ComparableMeasurement extends :class:`~org.orekit.time.TimeStamped`, Comparable<:class:`~org.orekit.estimation.measurements.ComparableMeasurement`>
    
        Base interface for comparing measurements regardless of their type.
    
        Since:
            9.2
    """
    def compareTo(self, comparableMeasurement: 'ComparableMeasurement') -> int:
        """
        
            Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed
            value. Even if they have the same value too, they will *not* be considered equal if they correspond to different
            instances. This allows to store measurements in null without losing any measurements, even redundant ones.
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getObservedValue(self) -> typing.List[float]:
        """
            Get the observed value.
        
            The observed value is the value that was measured by the instrument.
        
            Returns:
                observed value
        
        
        """
        ...

class EstimatedEarthFrameProvider(org.orekit.frames.TransformProvider):
    """
    public class EstimatedEarthFrameProvider extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
        Class modeling an Earth frame whose Earth Orientation Parameters can be estimated.
    
        This class adds parameters for an additional polar motion and an additional prime meridian orientation on top of an
        underlying regular Earth frame like :meth:`~org.orekit.frames.FramesFactory.getITRF`. The polar motion and prime
        meridian orientation are applied *after* regular Earth orientation parameters, so the value of the estimated parameters
        will be correction to EOP, they will not be the complete EOP values by themselves. Basically, this means that for Earth,
        the following transforms are applied in order, between inertial frame and this frame:
    
          1.  precession/nutation, as theoretical model plus celestial pole EOP parameters
          2.  body rotation, as theoretical model plus prime meridian EOP parameters
          3.  polar motion, which is only from EOP parameters (no theoretical models)
          4.  additional body rotation, controlled by
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.getPrimeMeridianOffsetDriver` and
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.getPrimeMeridianDriftDriver`
          5.  additional polar motion, controlled by
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.getPolarOffsetXDriver`,
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.getPolarDriftXDriver`,
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.getPolarOffsetYDriver` and
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.getPolarDriftYDriver`
    
    
        Since:
            9.1
    
        Also see:
            :meth:`~serialized`
    """
    EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    public static final double EARTH_ANGULAR_VELOCITY
    
        Earth Angular Velocity, in rad/s, from TIRF model.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, uT1Scale: org.orekit.time.UT1Scale): ...
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
        
            The parameter is an angle rate in radians per second. In order to convert this value to a LOD in seconds, the value must
            be multiplied by -86400 and divided by
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.EARTH_ANGULAR_VELOCITY` (nominal Angular Velocity
            of Earth).
        
            Returns:
                driver for prime meridian rotation rate
        
        
        """
        ...
    def getPrimeMeridianOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get a driver allowing to add a prime meridian rotation.
        
            The parameter is an angle in radians. In order to convert this value to a DUT1 in seconds, the value must be divided by
            :meth:`~org.orekit.estimation.measurements.EstimatedEarthFrameProvider.EARTH_ANGULAR_VELOCITY` (nominal Angular Velocity
            of Earth).
        
            Returns:
                driver for prime meridian rotation
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> org.orekit.frames.FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        """
        ...
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.analysis.differentiation.Gradient], int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient]:
        """
            Get the transform with derivatives.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<Gradient> date): date of the transform
                freeParameters (int): total number of free parameters in the gradient
                indices (Map<String,Integer> indices): indices of the estimated parameters in derivatives computations
        
            Returns:
                computed transform with derivatives
        
            Since:
                10.2
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

_EstimationModifier__T = typing.TypeVar('_EstimationModifier__T', bound='ObservedMeasurement')  # <T>
class EstimationModifier(typing.Generic[_EstimationModifier__T]):
    """
    public interface EstimationModifier<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>>
    
        Interface for estimated measurements modifiers used for orbit determination.
    
        Modifiers are used to take some physical corrections into account in the theoretical
        :class:`~org.orekit.estimation.measurements.EstimatedMeasurement` model. They can be used to model for example:
    
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: 'EstimatedMeasurement'[_EstimationModifier__T]) -> None: ...

class EstimationsProvider:
    """
    public interface EstimationsProvider
    
        Interface for retrieving estimated measurements during orbit determination.
    
        Implementations of this interface are provided by the orbit determination engine to user so they can
        :class:`~org.orekit.estimation.leastsquares.BatchLSObserver` the orbit determination process.
    
        Since:
            8.0
    
        Also see:
            :class:`~org.orekit.estimation.leastsquares.BatchLSObserver`
    """
    def getEstimatedMeasurement(self, int: int) -> 'EstimatedMeasurement'[typing.Any]:
        """
            Get one estimated measurement.
        
            Parameters:
                index (int): index of the estimated measurement, must be between 0 and
                    :meth:`~org.orekit.estimation.measurements.EstimationsProvider.getNumber` - 1, chronologically sorted
        
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
    public class GroundStation extends Object
    
        Class modeling a ground station that can perform some measurements.
    
        This class adds a position offset parameter to a base :class:`~org.orekit.frames.TopocentricFrame`.
    
        Since 9.0, this class also adds parameters for an additional polar motion and an additional prime meridian orientation.
        Since these parameters will have the same name for all ground stations, they will be managed consistently and allow to
        estimate Earth orientation precisely (this is needed for precise orbit determination). The polar motion and prime
        meridian orientation will be applied *after* regular Earth orientation parameters, so the value of the estimated
        parameters will be correction to EOP, they will not be the complete EOP values by themselves. Basically, this means that
        for Earth, the following transforms are applied in order, between inertial frame and ground station frame (for non-Earth
        based ground stations, different precession nutation models and associated planet oritentation parameters would be
        applied, if available):
    
        Since 9.3, this class also adds a station clock offset parameter, which manages the value that must be subtracted from
        the observed measurement date to get the real physical date at which the measurement was performed (i.e. the offset is
        negative if the ground station clock is slow and positive if it is fast).
    
          1.  precession/nutation, as theoretical model plus celestial pole EOP parameters
          2.  body rotation, as theoretical model plus prime meridian EOP parameters
          3.  polar motion, which is only from EOP parameters (no theoretical models)
          4.  additional body rotation, controlled by
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPrimeMeridianOffsetDriver` and
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPrimeMeridianDriftDriver`
          5.  additional polar motion, controlled by :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarOffsetXDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarDriftXDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarOffsetYDriver` and
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarDriftYDriver`
          6.  station clock offset, controlled by :meth:`~org.orekit.estimation.measurements.GroundStation.getClockOffsetDriver`
          7.  station position offset, controlled by :meth:`~org.orekit.estimation.measurements.GroundStation.getEastOffsetDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getNorthOffsetDriver` and
            :meth:`~org.orekit.estimation.measurements.GroundStation.getZenithOffsetDriver`
    
    
        Since:
            8.0
    """
    OFFSET_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final String OFFSET_SUFFIX
    
        Suffix for ground station position and clock offset parameters names.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DRIFT_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final String DRIFT_SUFFIX
    
        Suffix for ground clock drift parameters name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INTERMEDIATE_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final String INTERMEDIATE_SUFFIX
    
        Suffix for ground station intermediate frame name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame, eOPHistory: org.orekit.frames.EOPHistory, stationDisplacementArray: typing.List[org.orekit.models.earth.displacement.StationDisplacement]): ...
    def getBaseFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
            Get the base frame associated with the station.
        
            The base frame corresponds to a null position offset, null polar motion, null meridian shift
        
            Returns:
                base frame associated with the station
        
        
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
    def getDisplacements(self) -> typing.List[org.orekit.models.earth.displacement.StationDisplacement]:
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
        
            This frame is bound to the :meth:`~org.orekit.estimation.measurements.GroundStation.getPrimeMeridianOffsetDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPrimeMeridianDriftDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarOffsetXDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarDriftXDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarOffsetYDriver`,
            :meth:`~org.orekit.estimation.measurements.GroundStation.getPolarDriftYDriver`, so its orientation changes when the
            :meth:`~org.orekit.utils.ParameterDriver.setValue` methods of the drivers are called.
        
            Returns:
                estimated Earth frame
        
            Since:
                9.1
        
        
        """
        ...
    def getEstimatedUT1(self) -> org.orekit.time.UT1Scale:
        """
            Get the estimated UT1 scale, including the estimated linear models for prime meridian.
        
            This time scale is bound to the :meth:`~org.orekit.estimation.measurements.GroundStation.getPrimeMeridianOffsetDriver`,
            and :meth:`~org.orekit.estimation.measurements.GroundStation.getPrimeMeridianDriftDriver`, so its offset from UTC
            changes when the :meth:`~org.orekit.utils.ParameterDriver.setValue` methods of the drivers are called.
        
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
    def getOffsetGeodeticPoint(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint:
        """
            Get the geodetic point at the center of the offset frame.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date (may be null if displacements are ignored)
        
            Returns:
                geodetic point at the center of the offset frame
        
            Since:
                9.1
        
        
        """
        ...
    @typing.overload
    def getOffsetToInertial(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient]:
        """
            Get the transform between offset frame and inertial frame with derivatives.
        
            As the East and North vectors are not well defined at pole, the derivatives of these two vectors diverge to infinity as
            we get closer to the pole. So this method should not be used for stations less than 0.0001 degree from either poles.
        
            Parameters:
                inertial (:class:`~org.orekit.frames.Frame`): inertial frame to transform to
                clockDate (:class:`~org.orekit.time.AbsoluteDate`): date of the transform as read by the ground station clock (i.e. clock offset *not* compensated)
                freeParameters (int): total number of free parameters in the gradient
                indices (Map<String,Integer> indices): indices of the estimated parameters in derivatives computations
        
            Returns:
                transform between offset frame and inertial frame, at *real* measurement date (i.e. with clock, Earth and station
                offsets applied)
        
            Since:
                10.2
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.GroundStation.getOffsetToInertial`
        
            Get the transform between offset frame and inertial frame with derivatives.
        
            As the East and North vectors are not well defined at pole, the derivatives of these two vectors diverge to infinity as
            we get closer to the pole. So this method should not be used for stations less than 0.0001 degree from either poles.
        
            Parameters:
                inertial (:class:`~org.orekit.frames.Frame`): inertial frame to transform to
                offsetCompensatedDate (:class:`~org.orekit.time.FieldAbsoluteDate`<Gradient> offsetCompensatedDate): date of the transform, clock offset and its derivatives already compensated
                freeParameters (int): total number of free parameters in the gradient
                indices (Map<String,Integer> indices): indices of the estimated parameters in derivatives computations
        
            Returns:
                transform between offset frame and inertial frame, at specified date
        
            Since:
                10.2
        
        
        """
        ...
    @typing.overload
    def getOffsetToInertial(self, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.analysis.differentiation.Gradient], int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getOffsetToInertial(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
            Get the transform between offset frame and inertial frame.
        
            The offset frame takes the *current* position offset, polar motion and the meridian shift into account. The frame
            returned is disconnected from later changes in the parameters. When the :class:`~org.orekit.utils.ParameterDriver`
            managing these offsets are changed, the method must be called again to retrieve a new offset frame.
        
            Parameters:
                inertial (:class:`~org.orekit.frames.Frame`): inertial frame to transform to
                clockDate (:class:`~org.orekit.time.AbsoluteDate`): date of the transform as read by the ground station clock (i.e. clock offset *not* compensated)
        
            Returns:
                transform between offset frame and inertial frame, at *real* measurement date (i.e. with clock, Earth and station
                offsets applied)
        
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
        
            The parameter is an angle rate in radians per second. In order to convert this value to a LOD in seconds, the value must
            be multiplied by -86400 and divided by :code:`ave = 7.292115146706979e-5` (which is the nominal Angular Velocity of
            Earth from the TIRF model).
        
            Returns:
                driver for prime meridian rotation rate
        
        
        """
        ...
    def getPrimeMeridianOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get a driver allowing to add a prime meridian rotation.
        
            The parameter is an angle in radians. In order to convert this value to a DUT1 in seconds, the value must be divided by
            :code:`ave = 7.292115146706979e-5` (which is the nominal Angular Velocity of Earth from the TIRF model).
        
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
    public class ObservableSatellite extends Object
    
        Class modeling a satellite that can be observed.
    
        Since:
            9.3
    """
    CLOCK_OFFSET_PREFIX: typing.ClassVar[str] = ...
    """
    public static final String CLOCK_OFFSET_PREFIX
    
        Prefix for clock offset parameter driver, the propagator index will be appended to it.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLOCK_DRIFT_PREFIX: typing.ClassVar[str] = ...
    """
    public static final String CLOCK_DRIFT_PREFIX
    
        Prefix for clock drift parameter driver, the propagator index will be appended to it.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, int: int): ...
    def getClockDriftDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the clock drift parameter driver.
        
            The drift is negative if the satellite clock is slowing down and positive if it is speeding up.
        
            Returns:
                clock offset parameter driver
        
            Since:
                10.3
        
        
        """
        ...
    def getClockOffsetDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the clock offset parameter driver.
        
            The offset value is defined as the value in seconds that must be *subtracted* from the satellite clock reading of time
            to compute the real physical date. The offset is therefore negative if the satellite clock is slow and positive if it is
            fast.
        
            Returns:
                clock offset parameter driver
        
        
        """
        ...
    def getPropagatorIndex(self) -> int:
        """
            Get the index of the propagator related to this satellite.
        
            Returns:
                index of the propagator related to this satellite
        
        
        """
        ...

_EstimatedMeasurement__T = typing.TypeVar('_EstimatedMeasurement__T', bound='ObservedMeasurement')  # <T>
class EstimatedMeasurement(ComparableMeasurement, typing.Generic[_EstimatedMeasurement__T]):
    """
    public class EstimatedMeasurement<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
    
        Class holding an estimated theoretical value associated to an
        :class:`~org.orekit.estimation.measurements.ObservedMeasurement`.
    
        Since:
            8.0
    """
    def __init__(self, t: _EstimatedMeasurement__T, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState], timeStampedPVCoordinatesArray: typing.List[org.orekit.utils.TimeStampedPVCoordinates]): ...
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
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getDerivativesDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...
    def getEstimatedValue(self) -> typing.List[float]:
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
    def getObservedMeasurement(self) -> _EstimatedMeasurement__T:
        """
            Get the associated observed measurement.
        
            Returns:
                associated observed measurement
        
        
        """
        ...
    def getObservedValue(self) -> typing.List[float]:
        """
            Get the observed value.
        
            The observed value is the value that was measured by the instrument.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ComparableMeasurement.getObservedValue`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
        
            Returns:
                observed value
        
        
        """
        ...
    def getParameterDerivatives(self, parameterDriver: org.orekit.utils.ParameterDriver) -> typing.List[float]: ...
    def getParticipants(self) -> typing.List[org.orekit.utils.TimeStampedPVCoordinates]:
        """
            Get the coordinates of the measurements participants in signal travel order.
        
            First participant (at index 0) emits the signal (it is for example a ground station for two-way range measurement). Last
            participant receives the signal (it is also the ground station for two-way range measurement, but a few milliseconds
            later). Intermediate participants relfect the signal (it is the spacecraft for two-way range measurement).
        
            Returns:
                coordinates of the measurements participants in signal travel order in inertial frame
        
        
        """
        ...
    def getStateDerivatives(self, int: int) -> typing.List[typing.List[float]]:
        """
            Get the partial derivatives of the :meth:`~org.orekit.estimation.measurements.EstimatedMeasurement.getEstimatedValue`
            with respect to state Cartesian coordinates.
        
            Parameters:
                index (int): index of the state, according to the :code:`states` passed at construction
        
            Returns:
                partial derivatives of the simulated value (array of size
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getDimension` x 6)
        
        
        """
        ...
    def getStateSize(self) -> int:
        """
            Get state size.
        
            Warning, the null method must have been called before this method is called.
        
            Returns:
                state size
        
            Since:
                10.1
        
        
        """
        ...
    def getStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the states of the spacecrafts.
        
            Returns:
                states of the spacecrafts
        
        
        """
        ...
    def getStatus(self) -> 'EstimatedMeasurement.Status':
        """
            Get the status.
        
            The status is set to :meth:`~org.orekit.estimation.measurements.EstimatedMeasurement.Status.PROCESSED` at construction,
            and can be reset to :meth:`~org.orekit.estimation.measurements.EstimatedMeasurement.Status.REJECTED` later on, typically
            by :class:`~org.orekit.estimation.measurements.modifiers.OutlierFilter` or
            :class:`~org.orekit.estimation.measurements.modifiers.DynamicOutlierFilter`
        
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
    def setEstimatedValue(self, doubleArray: typing.List[float]) -> None:
        """
            Set the estimated value.
        
            Parameters:
                estimatedValue (double...): estimated value
        
        
        """
        ...
    def setParameterDerivatives(self, parameterDriver: org.orekit.utils.ParameterDriver, doubleArray: typing.List[float]) -> None:
        """
            Set the partial derivatives of the :meth:`~org.orekit.estimation.measurements.EstimatedMeasurement.getEstimatedValue`
            with respect to parameter.
        
            Parameters:
                driver (:class:`~org.orekit.utils.ParameterDriver`): driver for the parameter
                parameterDerivatives (double...): partial derivatives with respect to parameter
        
        
        """
        ...
    def setStateDerivatives(self, int: int, doubleArray: typing.List[typing.List[float]]) -> None: ...
    def setStatus(self, status: 'EstimatedMeasurement.Status') -> None:
        """
            Set the status.
        
            Parameters:
                status (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement.Status`): status to set
        
        
        """
        ...
    class Status(java.lang.Enum['EstimatedMeasurement.Status']):
        PROCESSED: typing.ClassVar['EstimatedMeasurement.Status'] = ...
        REJECTED: typing.ClassVar['EstimatedMeasurement.Status'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'EstimatedMeasurement.Status': ...
        @staticmethod
        def values() -> typing.List['EstimatedMeasurement.Status']: ...

_ObservedMeasurement__T = typing.TypeVar('_ObservedMeasurement__T', bound='ObservedMeasurement')  # <T>
class ObservedMeasurement(ComparableMeasurement, typing.Generic[_ObservedMeasurement__T]):
    """
    public interface ObservedMeasurement<T extends ObservedMeasurement<T>> extends :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
    
        Interface for measurements used for orbit determination.
    
        The most important methods of this interface allow to:
    
          - get the observed value,
          - estimate the theoretical value of a measurement,
          - compute the corresponding partial derivatives (with respect to state and parameters)
    
    
        The estimated theoretical values can be modified by registering one or several
        :class:`~org.orekit.estimation.measurements.EstimationModifier` objects. These objects will manage notions like
        tropospheric delays, biases, ...
    
        Since:
            8.0
    """
    def addModifier(self, estimationModifier: EstimationModifier[_ObservedMeasurement__T]) -> None: ...
    def estimate(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> EstimatedMeasurement[_ObservedMeasurement__T]: ...
    def getBaseWeight(self) -> typing.List[float]:
        """
            Get the base weight associated with the measurement
        
            The base weight is used on residuals already normalized thanks to
            :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getTheoreticalStandardDeviation` to increase or decrease
            relative effect of some measurements with respect to other measurements. It is a dimensionless value, typically between
            0 and 1 (but it can really have any non-negative value).
        
            Returns:
                base weight
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getTheoreticalStandardDeviation`
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the dimension of the measurement.
        
            Dimension is the size of the array containing the value. It will be one for a scalar measurement like a range or
            range-rate, but 6 for a position-velocity measurement.
        
            Returns:
                dimension of the measurement
        
        
        """
        ...
    def getModifiers(self) -> java.util.List[EstimationModifier[_ObservedMeasurement__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getSatellites(self) -> java.util.List[ObservableSatellite]: ...
    def getTheoreticalStandardDeviation(self) -> typing.List[float]:
        """
            Get the theoretical standard deviation.
        
            The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting
            factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension
            as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
            Returns:
                expected standard deviation
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getBaseWeight`
        
        
        """
        ...
    def isEnabled(self) -> bool:
        """
            Check if a measurement is enabled.
        
            Returns:
                true if the measurement is enabled
        
        
        """
        ...
    def setEnabled(self, boolean: bool) -> None:
        """
            Enable or disable a measurement.
        
            Disabling a measurement allow to not consider it at one stage of the orbit determination (for example when it appears to
            be an outlier as per current estimated covariance).
        
            Parameters:
                enabled (boolean): if true the measurement will be enabled, otherwise it will be disabled
        
        
        """
        ...

class PythonComparableMeasurement(ComparableMeasurement):
    """
    public class PythonComparableMeasurement extends Object implements :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
    """
    def __init__(self): ...
    def compareTo(self, comparableMeasurement: ComparableMeasurement) -> int:
        """
        
            Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed
            value. Even if they have the same value too, they will *not* be considered equal if they correspond to different
            instances. This allows to store measurements in null without losing any measurements, even redundant ones.
            Extension point for Python.
        
            Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed
            value. Even if they have the same value too, they will *not* be considered equal if they correspond to different
            instances. This allows to store measurements in null without losing any measurements, even redundant ones.
        
            Specified by:
                 in interface 
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ComparableMeasurement.compareTo`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
        
            Parameters:
                other (:class:`~org.orekit.estimation.measurements.ComparableMeasurement`): 
        
        """
        ...
    def finalize(self) -> None: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getObservedValue(self) -> typing.List[float]:
        """
            Get the observed value.
        
            The observed value is the value that was measured by the instrument.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ComparableMeasurement.getObservedValue`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
        
            Returns:
                observed value (array of size :code:`#getDimension()`
        
        
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

_PythonEstimationModifier__T = typing.TypeVar('_PythonEstimationModifier__T', bound=ObservedMeasurement)  # <T>
class PythonEstimationModifier(EstimationModifier[_PythonEstimationModifier__T], typing.Generic[_PythonEstimationModifier__T]):
    """
    public class PythonEstimationModifier<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: EstimatedMeasurement[_PythonEstimationModifier__T]) -> None: ...
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
    """
    public class PythonEstimationsProvider extends Object implements :class:`~org.orekit.estimation.measurements.EstimationsProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getEstimatedMeasurement(self, int: int) -> EstimatedMeasurement[typing.Any]:
        """
            Get one estimated measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.EstimationsProvider.getEstimatedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.EstimationsProvider`
        
            Parameters:
                index (int): index of the estimated measurement, must be between 0 and
                    :meth:`~org.orekit.estimation.measurements.PythonEstimationsProvider.getNumber` - 1, chronologically sorted
        
            Returns:
                estimated measurement at specified index
        
        
        """
        ...
    def getNumber(self) -> int:
        """
            Get the number of evaluations available.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.EstimationsProvider.getNumber`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.EstimationsProvider`
        
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
    public abstract class AbstractMeasurement<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>
    
        Abstract class handling measurements boilerplate.
    
        Since:
            8.0
    """
    def addModifier(self, estimationModifier: EstimationModifier[_AbstractMeasurement__T]) -> None: ...
    def estimate(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> EstimatedMeasurement[_AbstractMeasurement__T]: ...
    def getBaseWeight(self) -> typing.List[float]:
        """
            Get the base weight associated with the measurement
        
            The base weight is used on residuals already normalized thanks to
            :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getTheoreticalStandardDeviation` to increase or decrease
            relative effect of some measurements with respect to other measurements. It is a dimensionless value, typically between
            0 and 1 (but it can really have any non-negative value).
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getBaseWeight`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                base weight
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getTheoreticalStandardDeviation`
        
        
        """
        ...
    @staticmethod
    def getCoordinates(spacecraftState: org.orekit.propagation.SpacecraftState, int: int, int2: int) -> org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.analysis.differentiation.Gradient]:
        """
            Get Cartesian coordinates as derivatives.
        
            The position will correspond to variables :code:`firstDerivative`, :code:`firstDerivative + 1` and
            :code:`firstDerivative + 2`. The velocity will correspond to variables :code:`firstDerivative + 3`,
            :code:`firstDerivative + 4` and :code:`firstDerivative + 5`. The acceleration will correspond to constants.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state of the satellite considered
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
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the dimension of the measurement.
        
            Dimension is the size of the array containing the value. It will be one for a scalar measurement like a range or
            range-rate, but 6 for a position-velocity measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getDimension`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                dimension of the measurement
        
        
        """
        ...
    def getModifiers(self) -> java.util.List[EstimationModifier[_AbstractMeasurement__T]]: ...
    def getObservedValue(self) -> typing.List[float]:
        """
            Get the observed value.
        
            The observed value is the value that was measured by the instrument.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ComparableMeasurement.getObservedValue`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
        
            Returns:
                observed value
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getSatellites(self) -> java.util.List[ObservableSatellite]: ...
    def getTheoreticalStandardDeviation(self) -> typing.List[float]:
        """
            Get the theoretical standard deviation.
        
            The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting
            factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension
            as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getTheoreticalStandardDeviation`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                expected standard deviation
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getBaseWeight`
        
        
        """
        ...
    def isEnabled(self) -> bool:
        """
            Check if a measurement is enabled.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.isEnabled`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                true if the measurement is enabled
        
        
        """
        ...
    def setEnabled(self, boolean: bool) -> None:
        """
            Enable or disable a measurement.
        
            Disabling a measurement allow to not consider it at one stage of the orbit determination (for example when it appears to
            be an outlier as per current estimated covariance).
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.setEnabled`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Parameters:
                enabled (boolean): if true the measurement will be enabled, otherwise it will be disabled
        
        
        """
        ...
    _signalTimeOfFlight_1__T = typing.TypeVar('_signalTimeOfFlight_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def signalTimeOfFlight(timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Compute propagation delay on a link leg (typically downlink or uplink).
        
            Parameters:
                adjustableEmitterPV (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): position/velocity of emitter that may be adjusted
                receiverPosition (Vector3D): fixed position of receiver at :code:`signalArrivalDate`, in the same frame as :code:`adjustableEmitterPV`
                signalArrivalDate (:class:`~org.orekit.time.AbsoluteDate`): date at which the signal arrives to receiver
        
            Returns:
                *positive* delay between signal emission and signal reception dates
        
        """
        ...
    @typing.overload
    @staticmethod
    def signalTimeOfFlight(timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_signalTimeOfFlight_1__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_signalTimeOfFlight_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_signalTimeOfFlight_1__T]) -> _signalTimeOfFlight_1__T:
        """
            Compute propagation delay on a link leg (typically downlink or uplink).
        
            Parameters:
                adjustableEmitterPV (:class:`~org.orekit.utils.TimeStampedFieldPVCoordinates`<T> adjustableEmitterPV): position/velocity of emitter that may be adjusted
                receiverPosition (FieldVector3D<T> receiverPosition): fixed position of receiver at :code:`signalArrivalDate`, in the same frame as :code:`adjustableEmitterPV`
                signalArrivalDate (:class:`~org.orekit.time.FieldAbsoluteDate`<T> signalArrivalDate): date at which the signal arrives to receiver
        
            Returns:
                *positive* delay between signal emission and signal reception dates
        
        
        """
        ...

_PythonObservedMeasurement__T = typing.TypeVar('_PythonObservedMeasurement__T', bound=ObservedMeasurement)  # <T>
class PythonObservedMeasurement(ObservedMeasurement[_PythonObservedMeasurement__T], typing.Generic[_PythonObservedMeasurement__T]):
    """
    public class PythonObservedMeasurement<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>
    """
    def __init__(self): ...
    def addModifier(self, estimationModifier: EstimationModifier[_PythonObservedMeasurement__T]) -> None: ...
    def compareTo(self, comparableMeasurement: ComparableMeasurement) -> int:
        """
        
            Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed
            value. Even if they have the same value too, they will *not* be considered equal if they correspond to different
            instances. This allows to store measurements in null without losing any measurements, even redundant ones.
        
            Measurements comparison is primarily chronological, but measurements with the same date are sorted based on the observed
            value. Even if they have the same value too, they will *not* be considered equal if they correspond to different
            instances. This allows to store measurements in null without losing any measurements, even redundant ones.
        
            Specified by:
                 in interface 
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ComparableMeasurement.compareTo`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
        
            Parameters:
                other (:class:`~org.orekit.estimation.measurements.ComparableMeasurement`): 
        
        """
        ...
    def estimate(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> EstimatedMeasurement[_PythonObservedMeasurement__T]: ...
    def finalize(self) -> None: ...
    def getBaseWeight(self) -> typing.List[float]:
        """
            Get the base weight associated with the measurement
        
            The base weight is used on residuals already normalized thanks to
            :meth:`~org.orekit.estimation.measurements.PythonObservedMeasurement.getTheoreticalStandardDeviation` to increase or
            decrease relative effect of some measurements with respect to other measurements. It is a dimensionless value, typically
            between 0 and 1 (but it can really have any non-negative value).
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getBaseWeight`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                base weight
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.PythonObservedMeasurement.getTheoreticalStandardDeviation`,
                :code:`EstimatedMeasurement#getCurrentWeight()`
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the dimension of the measurement.
        
            Dimension is the size of the array containing the value. It will be one for a scalar measurement like a range or
            range-rate, but 6 for a position-velocity measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getDimension`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                dimension of the measurement
        
        
        """
        ...
    def getModifiers(self) -> java.util.List[EstimationModifier[_PythonObservedMeasurement__T]]: ...
    def getObservedValue(self) -> typing.List[float]:
        """
            Get the observed value.
        
            The observed value is the value that was measured by the instrument.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ComparableMeasurement.getObservedValue`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ComparableMeasurement`
        
            Returns:
                observed value (array of size :meth:`~org.orekit.estimation.measurements.PythonObservedMeasurement.getDimension`
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getSatellites(self) -> java.util.List[ObservableSatellite]: ...
    def getTheoreticalStandardDeviation(self) -> typing.List[float]:
        """
            Get the theoretical standard deviation.
        
            The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting
            factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension
            as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.getTheoreticalStandardDeviation`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                expected standard deviation
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.PythonObservedMeasurement.getBaseWeight`
        
        
        """
        ...
    def isEnabled(self) -> bool:
        """
            Check if a measurement is enabled.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.isEnabled`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Returns:
                true if the measurement is enabled
        
        
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
    def setEnabled(self, boolean: bool) -> None:
        """
            Enable or disable a measurement.
        
            Disabling a measurement allow to not consider it at one stage of the orbit determination (for example when it appears to
            be an outlier as per current estimated covariance).
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.ObservedMeasurement.setEnabled`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.ObservedMeasurement`
        
            Parameters:
                enabled (boolean): if true the measurement will be enabled, otherwise it will be disabled
        
        
        """
        ...

class AngularAzEl(AbstractMeasurement['AngularAzEl']):
    """
    public class AngularAzEl extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
        Class modeling an Azimuth-Elevation measurement from a ground station. The motion of the spacecraft during the signal
        flight time is taken into account. The date of the measurement corresponds to the reception on ground of the reflected
        signal.
    
        Since:
            8.0
    """
    def __init__(self, groundStation: GroundStation, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], observableSatellite: ObservableSatellite): ...
    def getStation(self) -> GroundStation:
        """
            Get the ground station from which measurement is performed.
        
            Returns:
                ground station from which measurement is performed
        
        
        """
        ...

class AngularRaDec(AbstractMeasurement['AngularRaDec']):
    """
    public class AngularRaDec extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.AngularRaDec`>
    
        Class modeling an Right Ascension - Declination measurement from a ground point (station, telescope). The angles are
        given in an inertial reference frame. The motion of the spacecraft during the signal flight time is taken into account.
        The date of the measurement corresponds to the reception on ground of the reflected signal.
    
        Since:
            9.0
    """
    def __init__(self, groundStation: GroundStation, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], observableSatellite: ObservableSatellite): ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame in which the right ascension - declination angles are given.
        
            Returns:
                reference frame in which the right ascension - declination angles are given
        
        
        """
        ...
    def getStation(self) -> GroundStation:
        """
            Get the ground station from which measurement is performed.
        
            Returns:
                ground station from which measurement is performed
        
        
        """
        ...

class InterSatellitesRange(AbstractMeasurement['InterSatellitesRange']):
    """
    public class InterSatellitesRange extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        One-way or two-way range measurements between two satellites.
    
        For one-way measurements, a signal is emitted by a remote satellite and received by local satellite. The measurement
        value is the elapsed time between emission and reception multiplied by c where c is the speed of light.
    
        For two-way measurements, a signal is emitted by local satellite, reflected on remote satellite, and received back by
        local satellite. The measurement value is the elapsed time between emission and reception multiplied by c/2 where c is
        the speed of light.
    
        Since 9.3, this class also uses the clock offsets of both satellites, which manage the value that must be added to each
        satellite reading of time to compute the real physical date. In this measurement, these offsets have two effects:
    
          - as measurement date is evaluated at reception time, the real physical date of the measurement is the observed date to
            which the local satellite clock offset is subtracted
          - as range is evaluated using the total signal time of flight, for one-way measurements the observed range is the real
            physical signal time of flight to which (ÃŽâ€�tl - ÃŽâ€�tr) Ã¢Â¨â€° c is added, where ÃŽâ€�tl (resp. ÃŽâ€�tr) is the
            clock offset for the local satellite (resp. remote satellite). A similar effect exists in two-way measurements but it is
            computed as (ÃŽâ€�tl - ÃŽâ€�tl) Ã¢Â¨â€° c / 2 as the local satellite clock is used for both initial emission and final
            reception and therefore it evaluates to zero.
    
    
        The motion of both satellites during the signal flight time is taken into account. The date of the measurement
        corresponds to the reception of the signal by satellite 1.
    
        Since:
            9.0
    """
    def __init__(self, observableSatellite: ObservableSatellite, observableSatellite2: ObservableSatellite, boolean: bool, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float): ...
    def isTwoWay(self) -> bool:
        """
            Check if the instance represents a two-way measurement.
        
            Returns:
                true if the instance represents a two-way measurement
        
        
        """
        ...

class MultiplexedMeasurement(AbstractMeasurement['MultiplexedMeasurement']):
    """
    public class MultiplexedMeasurement extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.MultiplexedMeasurement`>
    
        Class multiplexing several measurements as one.
    
        Date comes from the first measurement, observed and estimated values result from gathering all underlying measurements
        values.
    
        Since:
            10.1
    """
    def __init__(self, list: java.util.List[ObservedMeasurement[typing.Any]]): ...
    def getEstimatedMeasurements(self) -> java.util.List[EstimatedMeasurement[typing.Any]]: ...
    def getMeasurements(self) -> java.util.List[ObservedMeasurement[typing.Any]]: ...

class PV(AbstractMeasurement['PV']):
    """
    public class PV extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.PV`>
    
        Class modeling a position-velocity measurement.
    
        For position-only measurement see :class:`~org.orekit.estimation.measurements.Position`.
    
        Since:
            8.0
    
        Also see:
            :class:`~org.orekit.estimation.measurements.Position`
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float, double3: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float], double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[typing.List[float]], double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]], double3: float, observableSatellite: ObservableSatellite): ...
    def getCorrelationCoefficientsMatrix(self) -> typing.List[typing.List[float]]:
        """
            Get the correlation coefficients matrix.
        
            This is the 6x6 matrix M such that:
        
            Mij = Pij/(Ïƒi.Ïƒj)
        
            Where:
        
              - P is the covariance matrix
              - Ïƒi is the i-th standard deviation (ÏƒiÂ² = Pii)
        
        
            Returns:
                the correlation coefficient matrix (6x6)
        
        
        """
        ...
    def getCovarianceMatrix(self) -> typing.List[typing.List[float]]:
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
    public class Position extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.Position`>
    
        Class modeling a position only measurement.
    
        For position-velocity measurement see :class:`~org.orekit.estimation.measurements.PV`.
    
        Since:
            9.3
    
        Also see:
            :class:`~org.orekit.estimation.measurements.PV`
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float], double2: float, observableSatellite: ObservableSatellite): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[typing.List[float]], double2: float, observableSatellite: ObservableSatellite): ...
    def getCorrelationCoefficientsMatrix(self) -> typing.List[typing.List[float]]:
        """
            Get the correlation coefficients matrix.
        
            This is the 3x3 matrix M such that:
        
            Mij = Pij/(Ïƒi.Ïƒj)
        
            Where:
        
              - P is the covariance matrix
              - Ïƒi is the i-th standard deviation (ÏƒiÂ² = Pii)
        
        
            Returns:
                the correlation coefficient matrix (3x3)
        
        
        """
        ...
    def getCovarianceMatrix(self) -> typing.List[typing.List[float]]:
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
    """
    public class PythonAbstractMeasurement<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<T>
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, list: java.util.List[ObservableSatellite]): ...
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
    def theoreticalEvaluation(self, int: int, int2: int, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> EstimatedMeasurement[_PythonAbstractMeasurement__T]: ...

class Range(AbstractMeasurement['Range']):
    """
    public class Range extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modeling a range measurement from a ground station.
    
        For one-way measurements, a signal is emitted by the satellite and received by the ground station. The measurement value
        is the elapsed time between emission and reception multiplied by c where c is the speed of light.
    
        For two-way measurements, the measurement is considered to be a signal emitted from a ground station, reflected on
        spacecraft, and received on the same ground station. Its value is the elapsed time between emission and reception
        multiplied by c/2 where c is the speed of light.
    
        The motion of both the station and the spacecraft during the signal flight time are taken into account. The date of the
        measurement corresponds to the reception on ground of the emitted or reflected signal.
    
        The clock offsets of both the ground station and the satellite are taken into account. These offsets correspond to the
        values that must be subtracted from station (resp. satellite) reading of time to compute the real physical date. These
        offsets have two effects:
    
          - as measurement date is evaluated at reception time, the real physical date of the measurement is the observed date to
            which the receiving ground station clock offset is subtracted
          - as range is evaluated using the total signal time of flight, for one-way measurements the observed range is the real
            physical signal time of flight to which (ÃŽâ€�tg - ÃŽâ€�ts) Ã¢Â¨â€° c is added, where ÃŽâ€�tg (resp. ÃŽâ€�ts) is the
            clock offset for the receiving ground station (resp. emitting satellite). A similar effect exists in two-way
            measurements but it is computed as (ÃŽâ€�tg - ÃŽâ€�tg) Ã¢Â¨â€° c / 2 as the same ground station clock is used for
            initial emission and final reception and therefore it evaluates to zero.
    
    
    
        Since:
            8.0
    """
    def __init__(self, groundStation: GroundStation, boolean: bool, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: ObservableSatellite): ...
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

class RangeRate(AbstractMeasurement['RangeRate']):
    """
    public class RangeRate extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Class modeling one-way or two-way range rate measurement between two vehicles. One-way range rate (or Doppler)
        measurements generally apply to specific satellites (e.g. GNSS, DORIS), where a signal is transmitted from a satellite
        to a measuring station. Two-way range rate measurements are applicable to any system. The signal is transmitted to the
        (non-spinning) satellite and returned by a transponder (or reflected back)to the same measuring station. The Doppler
        measurement can be obtained by multiplying the velocity by (fe/c), where fe is the emission frequency.
    
        Since:
            8.0
    """
    def __init__(self, groundStation: GroundStation, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, boolean: bool, observableSatellite: ObservableSatellite): ...
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

class TurnAroundRange(AbstractMeasurement['TurnAroundRange']):
    """
    public class TurnAroundRange extends :class:`~org.orekit.estimation.measurements.AbstractMeasurement`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
        Class modeling a turn-around range measurement using a primary ground station and a secondary ground station.
    
        The measurement is considered to be a signal: - Emitted from the primary ground station - Reflected on the spacecraft -
        Reflected on the secondary ground station - Reflected on the spacecraft again - Received on the primary ground station
        Its value is the elapsed time between emission and reception divided by 2c were c is the speed of light. The motion of
        the stations and the spacecraft during the signal flight time are taken into account. The date of the measurement
        corresponds to the reception on ground of the reflected signal.
    
        Since:
            9.0
    """
    def __init__(self, groundStation: GroundStation, groundStation2: GroundStation, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, observableSatellite: ObservableSatellite): ...
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements")``.

    AbstractMeasurement: typing.Type[AbstractMeasurement]
    AngularAzEl: typing.Type[AngularAzEl]
    AngularRaDec: typing.Type[AngularRaDec]
    ComparableMeasurement: typing.Type[ComparableMeasurement]
    EstimatedEarthFrameProvider: typing.Type[EstimatedEarthFrameProvider]
    EstimatedMeasurement: typing.Type[EstimatedMeasurement]
    EstimationModifier: typing.Type[EstimationModifier]
    EstimationsProvider: typing.Type[EstimationsProvider]
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
    PythonObservedMeasurement: typing.Type[PythonObservedMeasurement]
    Range: typing.Type[Range]
    RangeRate: typing.Type[RangeRate]
    TurnAroundRange: typing.Type[TurnAroundRange]
    filtering: org.orekit.estimation.measurements.filtering.__module_protocol__
    generation: org.orekit.estimation.measurements.generation.__module_protocol__
    gnss: org.orekit.estimation.measurements.gnss.__module_protocol__
    modifiers: org.orekit.estimation.measurements.modifiers.__module_protocol__
