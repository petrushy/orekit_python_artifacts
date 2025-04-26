
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import org.hipparchus.exception
import org.hipparchus.geometry
import org.hipparchus.geometry.euclidean.twod
import org.hipparchus.geometry.partitioning
import typing



class Arc:
    """
    public classArc extends :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This class represents an arc on a circle.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.spherical.oned.ArcsSet`
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def checkPoint(self, double: float) -> org.hipparchus.geometry.partitioning.Region.Location:
        """
            Check a point with respect to the arc.
        
            Parameters:
                point (double): point to check
        
            Returns:
                a code representing the point status: either :meth:`~org.hipparchus.geometry.partitioning.Region.Location.INSIDE`,
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.OUTSIDE` or
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.BOUNDARY`
        
        
        """
        ...
    def getBarycenter(self) -> float:
        """
            Get the barycenter of the arc.
        
            Returns:
                barycenter of the arc
        
        
        """
        ...
    def getInf(self) -> float:
        """
            Get the lower angular bound of the arc.
        
            Returns:
                lower angular bound of the arc, always between 0 and \( 2 \pi \)
        
        
        """
        ...
    @typing.overload
    def getOffset(self, double: float) -> float:
        """
            Get the distance (arc length) from a point to the edge of the arc.
        
            This method does not use :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getTolerance`.
        
            Parameters:
                point (double): to test.
        
            Returns:
                offset, negative if the point is inside the arc, positive if it is outside the arc, or zero if :code:`point` is
                :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getInf` or
                :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getSup`.
        
            Get the distance (arc length) from a point to the edge of the arc.
        
            This method does not use :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getTolerance`.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): to test.
        
            Returns:
                offset, negative if the point is inside the arc, positive if it is outside the arc, or zero if :code:`point` is
                :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getInf` or
                :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getSup`.
        
        
        """
        ...
    @typing.overload
    def getOffset(self, s1Point: 'S1Point') -> float: ...
    def getSize(self) -> float:
        """
            Get the angular size of the arc.
        
            Returns:
                angular size of the arc
        
        
        """
        ...
    def getSup(self) -> float:
        """
            Get the upper angular bound of the arc.
        
            Returns:
                upper angular bound of the arc, always between :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getInf` and
                :meth:`~org.hipparchus.geometry.spherical.oned.Arc.getInf` \( + 2 \pi \)
        
        
        """
        ...
    def getTolerance(self) -> float:
        """
            Get the tolerance below which angles are considered identical.
        
            Returns:
                tolerance below which angles are considered identical
        
        
        """
        ...

class ArcsSet(org.hipparchus.geometry.partitioning.AbstractRegion['Sphere1D', 'S1Point', 'LimitAngle', 'SubLimitAngle', 'Sphere1D', 'S1Point', 'LimitAngle', 'SubLimitAngle'], java.lang.Iterable[typing.MutableSequence[float]]):
    """
    public classArcsSet extends :class:`~org.hipparchus.geometry.partitioning.AbstractRegion`<:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`,:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.SubLimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`,:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.SubLimitAngle`>
    implements :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable`<double[]>
    
        This class represents a region of a circle: a set of arcs.
    
        Note that due to the wrapping around \(2 \pi\), barycenter is ill-defined here. It was defined only in order to fulfill
        the requirements of the :class:`~org.hipparchus.geometry.partitioning.Region` interface, but its use is discouraged.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection['SubLimitAngle'], typing.Sequence['SubLimitAngle'], typing.Set['SubLimitAngle']], double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree['Sphere1D', 'S1Point', 'LimitAngle', 'SubLimitAngle'], double: float): ...
    def asList(self) -> java.util.List[Arc]: ...
    def buildNew(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree['Sphere1D', 'S1Point', 'LimitAngle', 'SubLimitAngle']) -> 'ArcsSet': ...
    def getInteriorPoint(self) -> 'S1Point':
        """
            Get an interior point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.getInteriorPoint` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                an arbitrary interior point, or null if region is empty
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[typing.MutableSequence[float]]:
        """
        
            The iterator returns the limit angles pairs of sub-arcs in trigonometric order.
        
            The iterator does *not* support the optional :code:`remove` operation.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable.iterator` in
                interface :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable`
        
        
        """
        ...
    def projectToBoundary(self, s1Point: 'S1Point') -> org.hipparchus.geometry.partitioning.BoundaryProjection['Sphere1D', 'S1Point']: ...
    def split(self, arc: Arc) -> 'ArcsSet.Split':
        """
            Split the instance in two parts by an arc.
        
            Parameters:
                arc (:class:`~org.hipparchus.geometry.spherical.oned.Arc`): splitting arc
        
            Returns:
                an object containing both the part of the instance on the plus side of the arc and the part of the instance on the minus
                side of the arc
        
        
        """
        ...
    class InconsistentStateAt2PiWrapping(org.hipparchus.exception.MathIllegalStateException):
        def __init__(self): ...
    class Split:
        def getMinus(self) -> 'ArcsSet': ...
        def getPlus(self) -> 'ArcsSet': ...
        def getSide(self) -> org.hipparchus.geometry.partitioning.Side: ...

class LimitAngle(org.hipparchus.geometry.partitioning.Hyperplane['Sphere1D', 'S1Point', 'LimitAngle', 'SubLimitAngle']):
    """
    public classLimitAngle extends :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`,:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.SubLimitAngle`>
    
        This class represents a 1D oriented hyperplane on the circle.
    
        An hyperplane on the 1-sphere is an angle with an orientation.
    
        Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, s1Point: 'S1Point', boolean: bool, double: float): ...
    def arbitraryPoint(self) -> 'S1Point':
        """
            Get an arbitrary point in the hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.arbitraryPoint` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                arbirary point in the hyperplane
        
        
        """
        ...
    def copySelf(self) -> 'LimitAngle':
        """
            Copy the instance.
        
            Since instances are immutable, this method directly returns the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.copySelf` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                the instance itself
        
        
        """
        ...
    def emptyHyperplane(self) -> 'SubLimitAngle':
        """
            Build a sub-hyperplane covering nothing.
        
            Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a
            dummy implementation of a :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`. This implementation is only used
            to allow the :class:`~org.hipparchus.geometry.partitioning.SubHyperplane` class implementation to work properly, it
            should *not* be used otherwise.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.emptyHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a sub-hyperplane covering nothing
        
        
        """
        ...
    def getLocation(self) -> 'S1Point':
        """
            Get the hyperplane location on the circle.
        
            Returns:
                the hyperplane location
        
        
        """
        ...
    def getOffset(self, s1Point: 'S1Point') -> float:
        """
            Get the offset (oriented distance) of a point.
        
            The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of
            the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.getOffset` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): point to check
        
            Returns:
                offset of the point
        
        
        """
        ...
    def getReverse(self) -> 'LimitAngle':
        """
            Get the reverse of the instance.
        
            Get a limit angle with reversed orientation with respect to the instance. A new object is built, the instance is
            untouched.
        
            Returns:
                a new limit angle, with orientation opposite to the instance orientation
        
        
        """
        ...
    def getTolerance(self) -> float:
        """
            Get the tolerance below which points are considered to belong to the hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.getTolerance` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                tolerance below which points are considered to belong to the hyperplane
        
        
        """
        ...
    def isDirect(self) -> bool:
        """
            Check if the hyperplane orientation is direct.
        
            Returns:
                true if the plus side of the hyperplane is towards angles greater than hyperplane location
        
        
        """
        ...
    def moveToOffset(self, s1Point: 'S1Point', double: float) -> 'S1Point':
        """
            Move point up to specified offset.
        
            Motion is *orthogonal* to the hyperplane
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.moveToOffset` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): point to move
                offset (double): desired offset
        
            Returns:
                moved point at desired offset
        
        
        """
        ...
    def project(self, s1Point: 'S1Point') -> 'S1Point':
        """
            Project a point to the hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.project` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): point to project
        
            Returns:
                projected point
        
        
        """
        ...
    def sameOrientationAs(self, limitAngle: 'LimitAngle') -> bool:
        """
            Check if the instance has the same orientation as another hyperplane.
        
            This method is expected to be called on parallel hyperplanes. The method should *not* re-check for parallelism, only for
            orientation, typically by testing something like the sign of the dot-products of normals.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.sameOrientationAs` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`): other hyperplane to check against the instance
        
            Returns:
                true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubLimitAngle':
        """
            Build a region covering the whole hyperplane.
        
            Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a
            dummy implementation of a :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`. This implementation is only used
            to allow the :class:`~org.hipparchus.geometry.partitioning.SubHyperplane` class implementation to work properly, it
            should *not* be used otherwise.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.wholeHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a dummy sub hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> ArcsSet:
        """
            Build a region covering the whole space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.wholeSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a region containing the instance (really an :class:`~org.hipparchus.geometry.spherical.oned.ArcsSet` instance)
        
        
        """
        ...

class S1Point(org.hipparchus.geometry.Point['Sphere1D', 'S1Point']):
    """
    public classS1Point extends :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.Point`<:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`>
    
        This class represents a point on the 1-sphere.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
    
              - :meth:`~serialized`
    """
    NaN: typing.ClassVar['S1Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.oned.S1Point` NaN
    
        A vector with all coordinates set to NaN.
    
    """
    def __init__(self, double: float): ...
    @typing.overload
    def distance(self, s1Point: 'S1Point') -> float:
        """
            Compute the distance between the instance and another point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.distance` in interface :class:`~org.hipparchus.geometry.Point`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): second point
        
            Returns:
                the distance between the instance and p
        
            Compute the distance (angular separation) between two points.
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): first vector
                p2 (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): second vector
        
            Returns:
                the angular separation between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(s1Point: 'S1Point', s1Point2: 'S1Point') -> float: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two points on the 1-sphere.
        
            If all coordinates of two points are exactly the same, and none are :code:`Double.NaN`, the two points are considered to
            be equal.
        
            :code:`NaN` coordinates are considered to affect globally the point and be equals to each other - i.e, if either (or
            all) coordinates of the point are equal to :code:`Double.NaN`, the point is equal to
            :meth:`~org.hipparchus.geometry.spherical.oned.S1Point.NaN`.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality to this
        
            Returns:
                true if two points on the 1-sphere objects are equal, false if object is null, not an instance of S1Point, or not equal
                to this S1Point instance
        
        
        """
        ...
    def equalsIeee754(self, object: typing.Any) -> bool:
        """
            Test for the equality of two points on the 1-sphere.
        
            If all coordinates of two points are exactly the same, and none are :code:`Double.NaN`, the two points are considered to
            be equal.
        
            In compliance with IEEE754 handling, if any coordinates of any of the two points are :code:`NaN`, then the points are
            considered different. This implies that
            :meth:`~org.hipparchus.geometry.spherical.oned.S1Point.NaN`.equals(:meth:`~org.hipparchus.geometry.spherical.oned.S1Point.NaN`)
            returns :code:`false` despite the instance is checked against itself.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality to this
        
            Returns:
                true if two points objects are equal, false if object is null, not an instance of S1Point, or not equal to this S1Point
                instance
        
            Since:
                2.1
        
        
        """
        ...
    def getAlpha(self) -> float:
        """
            Get the azimuthal angle \( \alpha \).
        
            Returns:
                azimuthal angle \( \alpha \)
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.oned.S1Point.%3Cinit%3E`
        
        
        
        """
        ...
    def getSpace(self) -> org.hipparchus.geometry.Space:
        """
            Get the space to which the point belongs.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.getSpace` in interface :class:`~org.hipparchus.geometry.Point`
        
            Returns:
                containing space
        
        
        """
        ...
    def getVector(self) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
            Get the corresponding normalized vector in the 2D euclidean space.
        
            Returns:
                normalized vector
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the point.
        
            All NaN values have the same hash code.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Returns true if any coordinate of this point is NaN; false otherwise
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.isNaN` in interface :class:`~org.hipparchus.geometry.Point`
        
            Returns:
                true if any coordinate of this point is NaN; false otherwise
        
        
        """
        ...
    def moveTowards(self, s1Point: 'S1Point', double: float) -> 'S1Point':
        """
            Move towards another point.
        
            Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for
            moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.moveTowards` in interface :class:`~org.hipparchus.geometry.Point`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): other point
                ratio (double): motion ratio,
        
            Returns:
                moved point
        
        
        """
        ...

class Sphere1D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    public classSphere1D extends :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.spherical.oned.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`, :class:`~org.hipparchus.geometry.Space`
    
        This class implements a one-dimensional sphere (i.e. a circle).
    
        We use here the topologists definition of the 1-sphere (see `Sphere <http://mathworld.wolfram.com/Sphere.html>` on
        MathWorld), i.e. the 1-sphere is the one-dimensional closed curve defined in 2D as x :sup:`2` +y :sup:`2` =1.
    
        Also see:
    
              - :meth:`~serialized`
    """
    SMALLEST_TOLERANCE: typing.ClassVar[float] = ...
    """
    public static final double SMALLEST_TOLERANCE
    
        Smallest tolerance that can be managed.
    
        Tolerances smaller than this value will generate exceptions.
    
        Since:
            1.4
    
    
    """
    @staticmethod
    def checkTolerance(double: float) -> None: ...
    def getDimension(self) -> int:
        """
            Get the dimension of the space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Space.getDimension` in interface :class:`~org.hipparchus.geometry.Space`
        
            Returns:
                dimension of the space
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'Sphere1D':
        """
            Get the unique instance.
        
            Returns:
                the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> org.hipparchus.geometry.Space: ...
    class NoSubSpaceException(org.hipparchus.exception.MathRuntimeException):
        def __init__(self): ...

class SubLimitAngle(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Sphere1D, S1Point, LimitAngle, 'SubLimitAngle', Sphere1D, S1Point, LimitAngle, 'SubLimitAngle']):
    """
    public classSubLimitAngle extends :class:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane`<:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`,:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.SubLimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`,:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.SubLimitAngle`>
    
        This class represents sub-hyperplane for :class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`.
    """
    def __init__(self, limitAngle: LimitAngle, region: org.hipparchus.geometry.partitioning.Region[Sphere1D, S1Point, LimitAngle, 'SubLimitAngle']): ...
    def getInteriorPoint(self) -> S1Point:
        """
            Get an interior point.
        
            Returns:
                an arbitrary interior point, or null if sub-hyperplane is empty
        
        
        """
        ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.getSize` in
                interface :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Overrides:
                :meth:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane.getSize` in
                class :class:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane`
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.isEmpty` in
                interface :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Overrides:
                :meth:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane.isEmpty` in
                class :class:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane`
        
            Returns:
                true if the instance is empty
        
        
        """
        ...
    def split(self, limitAngle: LimitAngle) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Sphere1D, S1Point, LimitAngle, 'SubLimitAngle']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.spherical.oned")``.

    Arc: typing.Type[Arc]
    ArcsSet: typing.Type[ArcsSet]
    LimitAngle: typing.Type[LimitAngle]
    S1Point: typing.Type[S1Point]
    Sphere1D: typing.Type[Sphere1D]
    SubLimitAngle: typing.Type[SubLimitAngle]
