import java.io
import java.util
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



_DerivativeGenerator__T = typing.TypeVar('_DerivativeGenerator__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
class DerivativeGenerator(typing.Generic[_DerivativeGenerator__T]):
    """
    public interface DerivativeGenerator<T extends org.hipparchus.analysis.differentiation.Derivative<T>>
    
        Generator for :code:`Derivative` instances from :code:`ParameterDriver`.
    
        Note that this interface is for Rugged library internal use only.
    
        Since:
            2.0
    """
    def constant(self, double: float) -> _DerivativeGenerator__T:
        """
            Generate a constant :code:`Derivative`.
        
            Parameters:
                value (double): value of the constant
        
            Returns:
                constant :code:`Derivative`
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_DerivativeGenerator__T]: ...
    def getSelected(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
            Get the parameters selected for estimation.
        
            Returns:
                parameters selected for estimation
        
        
        """
        ...
    def variable(self, parameterDriver: org.orekit.utils.ParameterDriver) -> _DerivativeGenerator__T:
        """
            Generate a :code:`Derivative` representing the parameter driver either as a canonical variable or a constant.
        
            The instance created is a variable only if the parameter has been selected for estimation, otherwise it is a constant.
        
            Parameters:
                driver (org.orekit.utils.ParameterDriver): driver for the variable
        
            Returns:
                variable :code:`Derivative`
        
        
        """
        ...

class ExtendedEllipsoid(org.orekit.bodies.OneAxisEllipsoid):
    """
    public class ExtendedEllipsoid extends org.orekit.bodies.OneAxisEllipsoid
    
        Transform provider from Spacecraft frame to observed body frame.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame): ...
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
    def pointAtAltitude(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    def pointAtLatitude(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    def pointAtLongitude(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    def pointOnGround(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float) -> 'NormalizedGeodeticPoint':
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
        
            Specified by:
                :code:`transform` in interface :code:`org.orekit.bodies.BodyShape`
        
            Overrides:
                :code:`transform` in class :code:`org.orekit.bodies.OneAxisEllipsoid`
        
        
            Specified by:
                :code:`transform` in interface :code:`org.orekit.bodies.BodyShape`
        
            Overrides:
                :code:`transform` in class :code:`org.orekit.bodies.OneAxisEllipsoid`
        
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
    def transform(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.FieldGeodeticPoint[org.hipparchus.analysis.differentiation.DerivativeStructure]: ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint: ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> 'NormalizedGeodeticPoint': ...

class GridCreation:
    """
    public final class GridCreation extends :class:`~org.orekit.rugged.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility class for grids creation.
    
        Since:
            2.1
    """
    @staticmethod
    def createLinearGrid(double: float, double2: float, int: int) -> typing.List[float]:
        """
            Create a linear grid between min and max value for a number n of points. TBN: no checks are performed here. Must be done
            by the calling method.
        
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
    public class NormalizedGeodeticPoint extends org.orekit.bodies.GeodeticPoint
    
        Geodetic point whose longitude can be selected with respect to the 2π boundary.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :code:`org.orekit.bodies.GeodeticPoint`
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
            Get the longitude.
        
            Overrides:
                :code:`getLongitude` in class :code:`org.orekit.bodies.GeodeticPoint`
        
            Returns:
                longitude, an angular value in the range [lc-π, lc+π], where l₀ was selected at construction
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :code:`org.orekit.bodies.GeodeticPoint`
        
        
        """
        ...

class RoughVisibilityEstimator:
    """
    public class RoughVisibilityEstimator extends :class:`~org.orekit.rugged.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class estimating very roughly when a point may be visible from spacecraft.
    
        The class only uses spacecraft position to compute a very rough sub-satellite point. It assumes the position-velocities
        are regular enough and without holes. It is intended only only has a quick estimation in order to set up search
        boundaries in inverse location.
    
        Also see:
            :meth:`~org.orekit.rugged.api.Rugged.dateLocation`, :meth:`~org.orekit.rugged.api.Rugged.dateLocation`,
            :meth:`~org.orekit.rugged.api.Rugged.inverseLocation`, :meth:`~org.orekit.rugged.api.Rugged.inverseLocation`
    """
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, frame: org.orekit.frames.Frame, list: java.util.List[org.orekit.utils.TimeStampedPVCoordinates]): ...
    def estimateVisibility(self, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.orekit.time.AbsoluteDate:
        """
            Estimate *very roughly* when spacecraft comes close to a ground point.
        
            Parameters:
                groundPoint (org.orekit.bodies.GeodeticPoint): ground point to check
        
            Returns:
                rough date at which spacecraft comes close to ground point (never null, but may be really far from reality if ground
                point is away from trajectory)
        
        
        """
        ...

class Selector:
    """
    public abstract class Selector extends :class:`~org.orekit.rugged.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class for selecting one value among two.
    
        Also see:
            :class:`~org.orekit.rugged.utils.MinSelector`, :class:`~org.orekit.rugged.utils.MaxSelector`
    """
    def __init__(self): ...
    def select(self, double: float, double2: float) -> float:
        """
            Select a value.
        
            Parameters:
                v1 (double): first value
                v2 (double): second value
        
            Returns:
                selected value
        
        
        """
        ...
    def selectFirst(self, double: float, double2: float) -> bool:
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
    public class SpacecraftToObservedBody extends :class:`~org.orekit.rugged.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.rugged.utils.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Provider for observation transforms.
    
        Also see:
            :meth:`~serialized`
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
    def getBodyToInertial(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
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
    def getInertialToBody(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
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
            Get the tolerance in seconds allowed for :meth:`~org.orekit.rugged.utils.SpacecraftToObservedBody.getMinDate` and
            :meth:`~org.orekit.rugged.utils.SpacecraftToObservedBody.getMaxDate` overshooting.
        
            Returns:
                tolerance in seconds allowed for :meth:`~org.orekit.rugged.utils.SpacecraftToObservedBody.getMinDate` and
                :meth:`~org.orekit.rugged.utils.SpacecraftToObservedBody.getMaxDate` overshooting
        
        
        """
        ...
    def getScToInertial(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
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
    def isInRange(self, absoluteDate: org.orekit.time.AbsoluteDate) -> bool:
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
    Deprecated. 
    as of 2.2, replaced by :class:`~org.orekit.rugged.utils.DerivativeGenerator`
    public interface DSGenerator extends :class:`~org.orekit.rugged.utils.DerivativeGenerator`<org.hipparchus.analysis.differentiation.DerivativeStructure>
    
        Generator for :code:`DerivativeStructure` instances from :code:`ParameterDriver`.
    
        Note that this interface is for Rugged library internal use only.
    
        Since:
            2.0
    """
    ...

class MaxSelector(Selector):
    """
    public class MaxSelector extends :class:`~org.orekit.rugged.utils.Selector`
    
        Selector for max value.
    
        This selector considers :code:`Double.NaN` values correspond to non-initialized data that should be ignored rather than
        selected.
    
        Also see:
            :class:`~org.orekit.rugged.utils.MinSelector`
    """
    @staticmethod
    def getInstance() -> 'MaxSelector':
        """
            Get the unique instance.
        
            Returns:
                unique instance of the min selector.
        
        
        """
        ...
    def selectFirst(self, double: float, double2: float) -> bool:
        """
            Check if first value should be selected.
        
            Specified by:
                :meth:`~org.orekit.rugged.utils.Selector.selectFirst` in class :class:`~org.orekit.rugged.utils.Selector`
        
            Parameters:
                v1 (double): first value
                v2 (double): second value
        
            Returns:
                true if v1 is higher than v2, or if v2 is :code:`Double.NaN`
        
        
        """
        ...

class MinSelector(Selector):
    """
    public class MinSelector extends :class:`~org.orekit.rugged.utils.Selector`
    
        Selector for min value.
    
        This selector considers :code:`Double.NaN` values correspond to non-initialized data that should be ignored rather than
        selected.
    
        Also see:
            :class:`~org.orekit.rugged.utils.MaxSelector`
    """
    @staticmethod
    def getInstance() -> 'MinSelector':
        """
            Get the unique instance.
        
            Returns:
                unique instance of the min selector.
        
        
        """
        ...
    def selectFirst(self, double: float, double2: float) -> bool:
        """
            Check if first value should be selected.
        
            Specified by:
                :meth:`~org.orekit.rugged.utils.Selector.selectFirst` in class :class:`~org.orekit.rugged.utils.Selector`
        
            Parameters:
                v1 (double): first value
                v2 (double): second value
        
            Returns:
                true if v1 is lower than v2, or if v2 is :code:`Double.NaN`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.utils")``.

    DSGenerator: typing.Type[DSGenerator]
    DerivativeGenerator: typing.Type[DerivativeGenerator]
    ExtendedEllipsoid: typing.Type[ExtendedEllipsoid]
    GridCreation: typing.Type[GridCreation]
    MaxSelector: typing.Type[MaxSelector]
    MinSelector: typing.Type[MinSelector]
    NormalizedGeodeticPoint: typing.Type[NormalizedGeodeticPoint]
    RoughVisibilityEstimator: typing.Type[RoughVisibilityEstimator]
    Selector: typing.Type[Selector]
    SpacecraftToObservedBody: typing.Type[SpacecraftToObservedBody]
