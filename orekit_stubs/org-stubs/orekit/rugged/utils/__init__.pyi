
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class AbsoluteDateArrayHandling:
    """
    AbsoluteDateArrayHandling consist of additions to AbsoluteDate to handle arrays.
    """
    def __init__(self, dates: typing.Union[typing.List[org.orekit.time.AbsoluteDate], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            dates (org.orekit.time.AbsoluteDate[]): is an array of absolute dates on which we want to apply time shift or compute duration
        
        
        """
        ...
    def durationFrom(self, datesForDuration: typing.Union[typing.List[org.orekit.time.AbsoluteDate], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Get array with durations between instances dates and corresponding given dates If instance dates = [date1, date2..., daten] and argument datesForDuration = [d1, d2..., dn] then this function will return [date1 durationFrom d1, date2 durationFrom d2..., daten durationFrom dn]. If duration from from all arguments dates wants to be compute on each date see multipleDurationFrom.
        
        Parameters:
            datesForDuration (org.orekit.time.AbsoluteDate[]): dates for which we want to compute the duration form instances dates. Warning must have same length as instance dates.
        
        Returns:
            a array of double representing durations between instance dates and corresponding argument dates
        
        
        """
        ...
    def getDates(self) -> typing.MutableSequence[org.orekit.time.AbsoluteDate]:
        """
        Get instance dates array.
        
        Returns:
            dates array
        
        
        """
        ...
    def multipleDurationFrom(self, datesForDuration: typing.Union[typing.List[org.orekit.time.AbsoluteDate], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get array with durations between instances dates and given dates If instance dates = [date1, date2..., daten] and argument datesForDuration = [d1, d2..., dn] then this function will return a matrix [[date1 durationFrom d1, date1 durationFrom d2..., date1 durationFrom dn], [date2 durationFrom d1, date2 durationFrom d2..., date2 durationFrom dn], [...] [daten durationFrom d1, daten durationFrom d2..., date1 durationFrom dn]]. If ones want to compute duration from only 1 date corresponding to 1 instance date see durationFrom.
        
        Parameters:
            datesForDuration (org.orekit.time.AbsoluteDate[]): dates for which we want to compute the duration form instances dates
        
        Returns:
            a matrix of double representing durations from instance dates If instance dates = [date1, date2..., daten] each line
            correspond to one date (for example date1 duration from all given dates in arguments (building the different columns))
        
        
        """
        ...
    def multipleShiftedBy(self, dts: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[org.orekit.time.AbsoluteDate]]:
        """
        Get time-shifted dates for several dates or several time shifts. If instance dates = [date1, date2..., daten] and argument dts = [dts1, dts2..., dtsn] then this function will return a matrix [[date1 shiftedby dts1, date1 shiftedBy dts2..., date1 shiftedBy dtsn], [date2 shiftedby dts1, date2 shiftedBy dts2..., date2 shiftedBy dtsn], [...] [daten shiftedby dts1, daten shiftedBy dts2..., date1 shiftedBy dtsn]]. If ones want to apply only 1 time shift corresponding to 1 date see shiftedBy.
        
        Parameters:
            dts (double[]): time shifts array in seconds we want to apply to dates
        
        Returns:
            a matrix of new dates, shifted with respect to wanted time shifts. If instance dates = [date1, date2..., daten] each
            line correspond to one date (for example date1 shiftedBy all timeshifts (building the different columns))
        
        
        """
        ...
    def shiftedBy(self, dts: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[org.orekit.time.AbsoluteDate]:
        """
        Get time-shifted dates for several dates and corresponding time shifts. If instance dates = [date1, date2..., daten] and argument dts = [dts1, dts2..., dtsn] then this function will return [date1 shiftedby dts1, date2 shiftedBy dts2..., daten shiftedBy dtsn]. If several time shift want to be applied on each date see multipleShiftedBy.
        
        Parameters:
            dts (double[]): time shifts array in seconds we want to apply to corresponding dates. Warning, must be same length as dates.
        
        Returns:
            an 1D array of new dates, shifted with respect to wanted corresponding time shifts.
        
        
        """
        ...

_DerivativeGenerator__T = typing.TypeVar('_DerivativeGenerator__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
class DerivativeGenerator(typing.Generic[_DerivativeGenerator__T]):
    """
    Generator for Derivative instances from ParameterDriver.
    
    Note that this interface is for Rugged library internal use only.
    
    Since:
        2.0
    """
    def constant(self, value: float) -> _DerivativeGenerator__T:
        """
        Generate a constant Derivative.
        
        Parameters:
            value (double): value of the constant
        
        Returns:
            constant Derivative
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_DerivativeGenerator__T]:
        """
        Get the Field to which the generated derivatives belongs.
        
        Returns:
            Field to which the generated derivatives belongs
        
        Since:
            2.2
        
        
        """
        ...
    def getSelected(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the parameters selected for estimation.
        
        Returns:
            parameters selected for estimation
        
        
        """
        ...
    def variable(self, driver: org.orekit.utils.ParameterDriver) -> _DerivativeGenerator__T:
        """
        Generate a Derivative representing the parameter driver either as a canonical variable or a constant.
        
        The instance created is a variable only if the parameter has been selected for estimation, otherwise it is a constant.
        
        Parameters:
            driver (org.orekit.utils.ParameterDriver): driver for the variable
        
        Returns:
            variable Derivative
        
        
        """
        ...

class ExtendedEllipsoid(org.orekit.bodies.OneAxisEllipsoid):
    """
    Transform provider from Spacecraft frame to observed body frame.
    """
    def __init__(self, ae: float, f: float, bodyFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            ae (double): equatorial radius (m)
            f (double): the flattening (f = (a-b)/a)
            bodyFrame (org.orekit.frames.Frame): body frame related to body shape
        
        Also see:
            IERSConventions, boolean)
        
        
        """
        ...
    @typing.overload
    def convertLos(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Convert a line-of-sight from Cartesian to topocentric.
        
        Parameters:
            point (org.orekit.bodies.GeodeticPoint): geodetic point on the line-of-sight
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight, not necessarily normalized (in body frame and Cartesian coordinates)
        
        Returns:
            line-of-sight in topocentric frame (East, North, Zenith) of the point, scaled to match radians in the horizontal plane
            and meters along the vertical axis
        
        Convert a line-of-sight from Cartesian to topocentric.
        
        Parameters:
            primary (org.hipparchus.geometry.euclidean.threed.Vector3D): reference point on the line-of-sight (in body frame and Cartesian coordinates)
            secondary (org.hipparchus.geometry.euclidean.threed.Vector3D): secondary point on the line-of-sight, only used to define a direction with respect to the primary point (in body frame
                and Cartesian coordinates)
        
        Returns:
            line-of-sight in topocentric frame (East, North, Zenith) of the point, scaled to match radians in the horizontal plane
            and meters along the vertical axis
        
        
        """
        ...
    @typing.overload
    def convertLos(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _pointAtAltitude_0__T = typing.TypeVar('_pointAtAltitude_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pointAtAltitude(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_pointAtAltitude_0__T], t: _pointAtAltitude_0__T, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_pointAtAltitude_0__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pointAtAltitude_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_pointAtAltitude_0__T]: ...
    @typing.overload
    def pointAtAltitude(self, line: org.hipparchus.geometry.euclidean.threed.Line, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def pointAtAltitude(self, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, altitude: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get point at some altitude along a pixel line of sight.
        
        Parameters:
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): cell position (in body frame) (m)
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight, not necessarily normalized (in body frame)
            altitude (double): altitude with respect to ellipsoid (m)
        
        Returns:
            point at altitude (m)
        
        
        """
        ...
    def pointAtLatitude(self, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, latitude: float, closeReference: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get point at some latitude along a pixel line of sight.
        
        Parameters:
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): cell position (in body frame) (m)
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight, not necessarily normalized (in body frame)
            latitude (double): latitude with respect to ellipsoid (rad)
            closeReference (org.hipparchus.geometry.euclidean.threed.Vector3D): reference point used to select the closest solution when there are two points at the desired latitude along the line, it
                should be close to los surface intersection (m)
        
        Returns:
            point at latitude (m)
        
        
        """
        ...
    def pointAtLongitude(self, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, longitude: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get point at some longitude along a pixel line of sight.
        
        Parameters:
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): cell position (in body frame) (m)
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight, not necessarily normalized (in body frame)
            longitude (double): longitude with respect to ellipsoid (rad)
        
        Returns:
            point at longitude (m)
        
        
        """
        ...
    def pointOnGround(self, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, centralLongitude: float) -> 'NormalizedGeodeticPoint':
        """
        Get point on ground along a pixel line of sight.
        
        Parameters:
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): cell position (in body frame) (m)
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight, not necessarily normalized (in body frame)
            centralLongitude (double): reference longitude lc such that the point longitude will be normalized between lc-π and lc+π (rad)
        
        Returns:
            point on ground
        
        
        """
        ...
    _transform_0__T = typing.TypeVar('_transform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_transform_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_0__T]: ...
    @typing.overload
    def transform(self, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: transform in interface BodyShape
        
        Overrides: transform in class OneAxisEllipsoid
        
        Specified by: transform in interface BodyShape
        
        Overrides: transform in class OneAxisEllipsoid
        
        Transform a cartesian point to a surface-relative point.
        
        Parameters:
            point (org.hipparchus.geometry.euclidean.threed.Vector3D): cartesian point (m)
            frame (org.orekit.frames.Frame): frame in which cartesian point is expressed
            date (org.orekit.time.AbsoluteDate): date of the computation (used for frames conversions)
            centralLongitude (double): reference longitude lc such that the point longitude will be normalized between lc-π and lc+π (rad)
        
        Returns:
            point at the same location but as a surface-relative point
        
        
        """
        ...
    @typing.overload
    def transform(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_2__T]) -> org.orekit.bodies.FieldGeodeticPoint[_transform_2__T]: ...
    @typing.overload
    def transform(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.FieldGeodeticPoint[org.hipparchus.analysis.differentiation.UnivariateDerivative2]: ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint: ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> 'NormalizedGeodeticPoint': ...

class GridCreation:
    """
    Utility class for grids creation.
    
    Since:
        2.1
    """
    @staticmethod
    def createLinearGrid(min: float, max: float, n: int) -> typing.MutableSequence[float]:
        """
        Create a linear grid between min and max value for a number n of points. TBN: no checks are performed here. Must be done by the calling method.
        
        Parameters:
            min (double): value for grid[0]
            max (double): value for grid[n-1]
            n (int): number of points
        
        Returns:
            the linear grid
        
        
        """
        ...

class NormalizedGeodeticPoint(org.orekit.bodies.GeodeticPoint):
    """
    Geodetic point whose longitude can be selected with respect to the 2π boundary.
    
    Also see:
        serialized
    """
    def __init__(self, latitude: float, longitude: float, altitude: float, centralLongitude: float):
        """
        Build a new instance. The angular coordinates will be normalized to ensure that the latitude is between ±π/2 and the longitude is between lc-π and lc+π.
        
        Parameters:
            latitude (double): latitude of the point
            longitude (double): longitude of the point
            altitude (double): altitude of the point
            centralLongitude (double): central longitude lc
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: equals in class GeodeticPoint
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
        Get the longitude.
        
        Overrides: getLongitude in class GeodeticPoint
        
        Returns:
            longitude, an angular value in the range [lc-π, lc+π], where l₀ was selected at construction
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class GeodeticPoint
        
        
        """
        ...

class RoughVisibilityEstimator:
    """
    Class estimating very roughly when a point may be visible from spacecraft.
    
    The class only uses spacecraft position to compute a very rough sub-satellite point. It assumes the position-velocities are regular enough and without holes. It is intended only only has a quick estimation in order to set up search boundaries in inverse location.
    
    Also see:
        dateLocation, dateLocation,
        inverseLocation, inverseLocation
    """
    def __init__(self, ellipsoid: org.orekit.bodies.OneAxisEllipsoid, frame: org.orekit.frames.Frame, positionsVelocities: java.util.List[org.orekit.utils.TimeStampedPVCoordinates]):
        """
        Simple constructor.
        
        Parameters:
            ellipsoid (org.orekit.bodies.OneAxisEllipsoid): ground ellipsoid
            frame (org.orekit.frames.Frame): frame in which position and velocity are defined (may be inertial or body frame)
            positionsVelocities (List<org.orekit.utils.TimeStampedPVCoordinates> positionsVelocities): satellite position and velocity (m and m/s in specified frame)
        
        
        """
        ...
    def estimateVisibility(self, groundPoint: org.orekit.bodies.GeodeticPoint) -> org.orekit.time.AbsoluteDate:
        """
        Estimate very roughly when spacecraft comes close to a ground point.
        
        Parameters:
            groundPoint (org.orekit.bodies.GeodeticPoint): ground point to check
        
        Returns:
            rough date at which spacecraft comes close to ground point (never null, but may be really far from reality if ground
            point is away from trajectory)
        
        
        """
        ...

class Selector:
    """
    Class for selecting one value among two.
    
    Also see:
        MinSelector, MaxSelector
    """
    def __init__(self): ...
    def select(self, v1: float, v2: float) -> float:
        """
        Select a value.
        
        Parameters:
            v1 (double): first value
            v2 (double): second value
        
        Returns:
            selected value
        
        
        """
        ...
    def selectFirst(self, v1: float, v2: float) -> bool:
        """
        Check if first value should be selected.
        
        Parameters:
            v1 (double): first value
            v2 (double): second value
        
        Returns:
            true if v1 should be selected
        
        
        """
        ...

class SpacecraftToObservedBody(java.io.Serializable):
    """
    Provider for observation transforms.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, double: float, double2: float, list: java.util.List[org.orekit.utils.TimeStampedPVCoordinates], int: int, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, list2: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int2: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, double: float, double2: float, list: java.util.List[org.orekit.frames.Transform], list2: java.util.List[org.orekit.frames.Transform]): ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
        Get the body frame.
        
        Returns:
            body frame
        
        
        """
        ...
    def getBodyToInertial(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
        Get transform from observed body frame to inertial frame.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): date of the transform
        
        Returns:
            transform from observed body frame to inertial frame
        
        
        """
        ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
        Get the inertial frame.
        
        Returns:
            inertial frame
        
        
        """
        ...
    def getInertialToBody(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
        Get transform from inertial frame to observed body frame.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): date of the transform
        
        Returns:
            transform from inertial frame to observed body frame
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end of search time span.
        
        Returns:
            end of search time span
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start of search time span.
        
        Returns:
            start of search time span
        
        
        """
        ...
    def getOvershootTolerance(self) -> float:
        """
        Get the tolerance in seconds allowed for getMinDate and getMaxDate overshooting.
        
        Returns:
            tolerance in seconds allowed for getMinDate and
            getMaxDate overshooting
        
        
        """
        ...
    def getScToInertial(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
        Get transform from spacecraft to inertial frame.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): date of the transform
        
        Returns:
            transform from spacecraft to inertial frame
        
        
        """
        ...
    def getTStep(self) -> float:
        """
        Get the step to use for inertial frame to body frame transforms cache computations.
        
        Returns:
            step to use for inertial frame to body frame transforms cache computations
        
        
        """
        ...
    def isInRange(self, date: org.orekit.time.AbsoluteDate) -> bool:
        """
        Check if a date is in the supported range.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): date to check
        
        Returns:
            true if date is in the supported range
        
        
        """
        ...

class DSGenerator(DerivativeGenerator[org.hipparchus.analysis.differentiation.DerivativeStructure]):
    """
    Deprecated. as of 2.2, replaced by DerivativeGenerator Generator for DerivativeStructure instances from ParameterDriver.
    
    Note that this interface is for Rugged library internal use only.
    
    Since:
        2.0
    """
    ...

class MaxSelector(Selector):
    """
    Selector for max value.
    
    This selector considers NaN values correspond to non-initialized data that should be ignored rather than selected.
    
    Also see:
        MinSelector
    """
    @staticmethod
    def getInstance() -> 'MaxSelector':
        """
        Get the unique instance.
        
        Returns:
            unique instance of the min selector.
        
        
        """
        ...
    def selectFirst(self, v1: float, v2: float) -> bool:
        """
        Check if first value should be selected.
        
        Specified by: selectFirst in class Selector
        
        Parameters:
            v1 (double): first value
            v2 (double): second value
        
        Returns:
            true if v1 is higher than v2, or if v2 is NaN
        
        
        """
        ...

class MinSelector(Selector):
    """
    Selector for min value.
    
    This selector considers NaN values correspond to non-initialized data that should be ignored rather than selected.
    
    Also see:
        MaxSelector
    """
    @staticmethod
    def getInstance() -> 'MinSelector':
        """
        Get the unique instance.
        
        Returns:
            unique instance of the min selector.
        
        
        """
        ...
    def selectFirst(self, v1: float, v2: float) -> bool:
        """
        Check if first value should be selected.
        
        Specified by: selectFirst in class Selector
        
        Parameters:
            v1 (double): first value
            v2 (double): second value
        
        Returns:
            true if v1 is lower than v2, or if v2 is NaN
        
        
        """
        ...

class PythonSelector(Selector):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def selectFirst(self, double: float, double2: float) -> bool: ...

class PythonDSGenerator(DSGenerator):
    def __init__(self): ...
    def constant(self, double: float) -> org.hipparchus.analysis.differentiation.DerivativeStructure: ...
    def finalize(self) -> None: ...
    def getSelected(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def variable(self, parameterDriver: org.orekit.utils.ParameterDriver) -> org.hipparchus.analysis.differentiation.DerivativeStructure: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.utils")``.

    AbsoluteDateArrayHandling: typing.Type[AbsoluteDateArrayHandling]
    DSGenerator: typing.Type[DSGenerator]
    DerivativeGenerator: typing.Type[DerivativeGenerator]
    ExtendedEllipsoid: typing.Type[ExtendedEllipsoid]
    GridCreation: typing.Type[GridCreation]
    MaxSelector: typing.Type[MaxSelector]
    MinSelector: typing.Type[MinSelector]
    NormalizedGeodeticPoint: typing.Type[NormalizedGeodeticPoint]
    PythonDSGenerator: typing.Type[PythonDSGenerator]
    PythonSelector: typing.Type[PythonSelector]
    RoughVisibilityEstimator: typing.Type[RoughVisibilityEstimator]
    Selector: typing.Type[Selector]
    SpacecraftToObservedBody: typing.Type[SpacecraftToObservedBody]
