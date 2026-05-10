
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
    This class represents an arc on a circle.
    
    Also see:
        ArcsSet
    """
    def __init__(self, lower: float, upper: float, tolerance: float):
        """
        Simple constructor.
        
        If either lower is equals to upper or the interval exceeds \( 2 \pi \), the arc is considered to be the full circle and its initial defining boundaries will be forgotten. lower is not allowed to be greater than upper (an exception is thrown in this case). lower will be canonicalized between 0 and \( 2 \pi \), and upper shifted accordingly, so the getInf and getSup may not return the value used at instance construction.
        
        Parameters:
            lower (double): lower angular bound of the arc
            upper (double): upper angular bound of the arc
            tolerance (double): tolerance below which angles are considered identical
        
        Raises:
            hipparchus: if lower is greater than upper or tolerance is smaller than
                SMALLEST_TOLERANCE
        
        
        """
        ...
    def checkPoint(self, point: float) -> org.hipparchus.geometry.partitioning.Region.Location:
        """
        Check a point with respect to the arc.
        
        Parameters:
            point (double): point to check
        
        Returns:
            a code representing the point status: either INSIDE,
            OUTSIDE or
            BOUNDARY
        
        
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
    def getOffset(self, point: float) -> float:
        """
        This method does not use getTolerance.
        
        Parameters:
            point (double): to test.
        
        Returns:
            offset, negative if the point is inside the arc, positive if it is outside the arc, or zero if point is
            getInf or
            getSup.
        
        Get the distance (arc length) from a point to the edge of the arc.
        
        This method does not use getTolerance.
        
        Parameters:
            point (S1Point): to test.
        
        Returns:
            offset, negative if the point is inside the arc, positive if it is outside the arc, or zero if point is
            getInf or
            getSup.
        
        
        """
        ...
    @typing.overload
    def getOffset(self, point: 'S1Point') -> float: ...
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
            upper angular bound of the arc, always between getInf and
            getInf \( + 2 \pi \)
        
        
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
    This class represents a region of a circle: a set of arcs.
    
    Note that due to the wrapping around \(2 \pi\), barycenter is ill-defined here. It was defined only in order to fulfill the requirements of the Region interface, but its use is discouraged.
    """
    @typing.overload
    def __init__(self, tolerance: float): ...
    @typing.overload
    def __init__(self, lower: float, upper: float, tolerance: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection['SubLimitAngle'], typing.Sequence['SubLimitAngle'], typing.Set['SubLimitAngle']], double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree['Sphere1D', 'S1Point', 'LimitAngle', 'SubLimitAngle'], double: float): ...
    def asList(self) -> java.util.List[Arc]:
        """
        Build an ordered list of arcs representing the instance.
        
        This method builds this arcs set as an ordered list of Arc elements. An empty tree will build an empty list while a tree representing the whole circle will build a one element list with bounds set to \( 0 and 2 \pi \).
        
        Returns:
            a new ordered list containing Arc elements
        
        
        """
        ...
    def buildNew(self, tree: org.hipparchus.geometry.partitioning.BSPTree['Sphere1D', 'S1Point', 'LimitAngle', 'SubLimitAngle']) -> 'ArcsSet':
        """
        Build a region using the instance as a prototype.
        
        This method allow to create new instances without knowing exactly the type of the region. It is an application of the prototype design pattern.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Specified by: buildNew in interface Region
        
        Specified by: buildNew in class AbstractRegion
        
        Parameters:
            tree (BSPTree<Sphere1D, S1Point, LimitAngle, SubLimitAngle> tree): inside/outside BSP tree representing the new region
        
        Returns:
            the built region
        
        
        """
        ...
    def getInteriorPoint(self) -> 'S1Point':
        """
        Get an interior point.
        
        Specified by: getInteriorPoint in interface Region
        
        Returns:
            an arbitrary interior point, or null if region is empty
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[typing.MutableSequence[float]]:
        """
        The iterator returns the limit angles pairs of sub-arcs in trigonometric order.
        
        The iterator does not support the optional remove operation.
        
        Specified by: Iterable in interface Iterable
        
        
        """
        ...
    def projectToBoundary(self, point: 'S1Point') -> org.hipparchus.geometry.partitioning.BoundaryProjection['Sphere1D', 'S1Point']:
        """
        Project a point on the boundary of the region.
        
        Specified by: projectToBoundary in interface Region
        
        Overrides: projectToBoundary in class AbstractRegion
        
        Parameters:
            point (S1Point): point to check
        
        Returns:
            projection of the point on the boundary
        
        
        """
        ...
    def split(self, arc: Arc) -> 'ArcsSet.Split':
        """
        Split the instance in two parts by an arc.
        
        Parameters:
            arc (Arc): splitting arc
        
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
    This class represents a 1D oriented hyperplane on the circle.
    
    An hyperplane on the 1-sphere is an angle with an orientation.
    
    Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, location: 'S1Point', direct: bool, tolerance: float):
        """
        Simple constructor.
        
        Parameters:
            location (S1Point): location of the hyperplane
            direct (boolean): if true, the plus side of the hyperplane is towards angles greater than location
            tolerance (double): tolerance below which angles are considered identical
        
        Raises:
            hipparchus: if tolerance is smaller than SMALLEST_TOLERANCE
        
        
        """
        ...
    def arbitraryPoint(self) -> 'S1Point':
        """
        Get an arbitrary point in the hyperplane.
        
        Specified by: arbitraryPoint in interface Hyperplane
        
        Returns:
            arbirary point in the hyperplane
        
        
        """
        ...
    def copySelf(self) -> 'LimitAngle':
        """
        Copy the instance.
        
        Since instances are immutable, this method directly returns the instance.
        
        Specified by: copySelf in interface Hyperplane
        
        Returns:
            the instance itself
        
        
        """
        ...
    def emptyHyperplane(self) -> 'SubLimitAngle':
        """
        Build a sub-hyperplane covering nothing.
        
        Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a dummy implementation of a SubHyperplane. This implementation is only used to allow the SubHyperplane class implementation to work properly, it should not be used otherwise.
        
        Specified by: emptyHyperplane in interface Hyperplane
        
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
    def getOffset(self, point: 'S1Point') -> float:
        """
        Get the offset (oriented distance) of a point.
        
        The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
        Specified by: getOffset in interface Hyperplane
        
        Parameters:
            point (S1Point): point to check
        
        Returns:
            offset of the point
        
        
        """
        ...
    def getReverse(self) -> 'LimitAngle':
        """
        Get the reverse of the instance.
        
        Get a limit angle with reversed orientation with respect to the instance. A new object is built, the instance is untouched.
        
        Returns:
            a new limit angle, with orientation opposite to the instance orientation
        
        
        """
        ...
    def getTolerance(self) -> float:
        """
        Get the tolerance below which points are considered to belong to the hyperplane.
        
        Specified by: getTolerance in interface Hyperplane
        
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
    def moveToOffset(self, point: 'S1Point', offset: float) -> 'S1Point':
        """
        Move point up to specified offset.
        
        Motion is orthogonal to the hyperplane
        
        Specified by: moveToOffset in interface Hyperplane
        
        Parameters:
            point (S1Point): point to move
            offset (double): desired offset
        
        Returns:
            moved point at desired offset
        
        
        """
        ...
    def project(self, point: 'S1Point') -> 'S1Point':
        """
        Project a point to the hyperplane.
        
        Specified by: project in interface Hyperplane
        
        Parameters:
            point (S1Point): point to project
        
        Returns:
            projected point
        
        
        """
        ...
    def sameOrientationAs(self, other: 'LimitAngle') -> bool:
        """
        Check if the instance has the same orientation as another hyperplane.
        
        This method is expected to be called on parallel hyperplanes. The method should not re-check for parallelism, only for orientation, typically by testing something like the sign of the dot-products of normals.
        
        Specified by: sameOrientationAs in interface Hyperplane
        
        Parameters:
            other (LimitAngle): other hyperplane to check against the instance
        
        Returns:
            true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubLimitAngle':
        """
        Build a region covering the whole hyperplane.
        
        Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a dummy implementation of a SubHyperplane. This implementation is only used to allow the SubHyperplane class implementation to work properly, it should not be used otherwise.
        
        Specified by: wholeHyperplane in interface Hyperplane
        
        Returns:
            a dummy sub hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> ArcsSet:
        """
        Build a region covering the whole space.
        
        Specified by: wholeSpace in interface Hyperplane
        
        Returns:
            a region containing the instance (really an ArcsSet instance)
        
        
        """
        ...

class S1Point(org.hipparchus.geometry.Point['Sphere1D', 'S1Point']):
    """
    This class represents a point on the 1-sphere.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        serialized
    """
    NaN: typing.ClassVar['S1Point'] = ...
    """
    A vector with all coordinates set to NaN.
    """
    def __init__(self, alpha: float):
        """
        Simple constructor. Build a vector from its coordinates
        
        Parameters:
            alpha (double): azimuthal angle \( \alpha \)
        
        Also see:
            getAlpha
        
        
        """
        ...
    @typing.overload
    def distance(self, point: 'S1Point') -> float:
        """
        Compute the distance between the instance and another point.
        
        Specified by: distance in interface Point
        
        Parameters:
            point (S1Point): second point
        
        Returns:
            the distance between the instance and p
        
        Compute the distance (angular separation) between two points.
        
        Parameters:
            p1 (S1Point): first vector
            p2 (S1Point): second vector
        
        Returns:
            the angular separation between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(p1: 'S1Point', p2: 'S1Point') -> float: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two points on the 1-sphere.
        
        If all coordinates of two points are exactly the same, and none are NaN, the two points are considered to be equal.
        
        NaN coordinates are considered to affect globally the point and be equals to each other - i.e, if either (or all) coordinates of the point are equal to NaN, the point is equal to NaN.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two points on the 1-sphere objects are equal, false if object is null, not an instance of S1Point, or not equal
            to this S1Point instance
        
        
        """
        ...
    def equalsIeee754(self, other: typing.Any) -> bool:
        """
        Test for the equality of two points on the 1-sphere.
        
        If all coordinates of two points are exactly the same, and none are NaN, the two points are considered to be equal.
        
        In compliance with IEEE754 handling, if any coordinates of any of the two points are NaN, then the points are considered different. This implies that NaN.equals(NaN) returns false despite the instance is checked against itself.
        
        Parameters:
            other (Object): Object to test for equality to this
        
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
        
        
        """
        ...
    def getSpace(self) -> org.hipparchus.geometry.Space:
        """
        Get the space to which the point belongs.
        
        Specified by: getSpace in interface Point
        
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
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Returns true if any coordinate of this point is NaN; false otherwise
        
        Specified by: isNaN in interface Point
        
        Returns:
            true if any coordinate of this point is NaN; false otherwise
        
        
        """
        ...
    def moveTowards(self, other: 'S1Point', ratio: float) -> 'S1Point':
        """
        Move towards another point.
        
        Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
        Specified by: moveTowards in interface Point
        
        Parameters:
            other (S1Point): other point
            ratio (double): motion ratio,
        
        Returns:
            moved point
        
        
        """
        ...

class Sphere1D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    This class implements a one-dimensional sphere (i.e. a circle).
    
    We use here the topologists definition of the 1-sphere (see `Sphere <http://mathworld.wolfram.com/Sphere.html>` on MathWorld), i.e. the 1-sphere is the one-dimensional closed curve defined in 2D as x :sup:`2` +y :sup:`2` =1.
    
    Also see:
        serialized
    """
    SMALLEST_TOLERANCE: typing.ClassVar[float] = ...
    """
    Smallest tolerance that can be managed.
    
    Tolerances smaller than this value will generate exceptions.
    
    Since:
        1.4
    
    
    """
    @staticmethod
    def checkTolerance(tolerance: float) -> None:
        """
        Check tolerance against SMALLEST_TOLERANCE.
        
        Parameters:
            tolerance (double): tolerance to check
        
        Raises:
            hipparchus: if tolerance is smaller than SMALLEST_TOLERANCE
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the space.
        
        Specified by: getDimension in interface Space
        
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
    def getSubSpace(self) -> org.hipparchus.geometry.Space:
        """
        Get the n-1 dimension subspace of this space.
        
        As the 1-dimension sphere does not have proper sub-spaces, this method always throws a NoSubSpaceException
        
        Specified by: getSubSpace in interface Space
        
        Returns:
            nothing
        
        Raises:
            NoSubSpaceException: in all cases
        
        Also see:
            getDimension
        
        
        """
        ...
    class NoSubSpaceException(org.hipparchus.exception.MathRuntimeException):
        def __init__(self): ...

class SubLimitAngle(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Sphere1D, S1Point, LimitAngle, 'SubLimitAngle', Sphere1D, S1Point, LimitAngle, 'SubLimitAngle']):
    """
    This class represents sub-hyperplane for LimitAngle.
    """
    def __init__(self, hyperplane: LimitAngle, remainingRegion: org.hipparchus.geometry.partitioning.Region[Sphere1D, S1Point, LimitAngle, 'SubLimitAngle']):
        """
        Simple constructor.
        
        Parameters:
            hyperplane (LimitAngle): underlying hyperplane
            remainingRegion (Region<Sphere1D, S1Point, LimitAngle, SubLimitAngle> remainingRegion): remaining region of the hyperplane
        
        
        """
        ...
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
        
        Specified by: getSize in interface SubHyperplane
        
        Overrides: getSize in class AbstractSubHyperplane
        
        Returns:
            the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
        Check if the instance is empty.
        
        Specified by: isEmpty in interface SubHyperplane
        
        Overrides: isEmpty in class AbstractSubHyperplane
        
        Returns:
            true if the instance is empty
        
        
        """
        ...
    def split(self, hyperplane: LimitAngle) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Sphere1D, S1Point, LimitAngle, 'SubLimitAngle']:
        """
        Split the instance in two parts by an hyperplane.
        
        Specified by: split in interface SubHyperplane
        
        Specified by: split in class AbstractSubHyperplane
        
        Parameters:
            hyperplane (LimitAngle): splitting hyperplane
        
        Returns:
            an object containing both the part of the instance on the plus side of the hyperplane and the part of the instance on
            the minus side of the hyperplane
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.spherical.oned")``.

    Arc: typing.Type[Arc]
    ArcsSet: typing.Type[ArcsSet]
    LimitAngle: typing.Type[LimitAngle]
    S1Point: typing.Type[S1Point]
    Sphere1D: typing.Type[Sphere1D]
    SubLimitAngle: typing.Type[SubLimitAngle]
