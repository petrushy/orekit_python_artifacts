
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.text
import java.util
import org.hipparchus.exception
import org.hipparchus.geometry
import org.hipparchus.geometry.partitioning
import typing



class Euclidean1D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    implements Serializable, Space
    
    This class implements a one-dimensional space.
    
          - serialized
    """
    def getDimension(self) -> int:
        """
        Get the dimension of the space.
        
        Specified by: getDimension in interface Space
        
        Returns:
            dimension of the space
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'Euclidean1D':
        """
        Get the unique instance.
        
        Returns:
            the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> org.hipparchus.geometry.Space:
        """
        Get the n-1 dimension subspace of this space.
        
        As the 1-dimension Euclidean space does not have proper sub-spaces, this method always throws a NoSubSpaceException
        
        Specified by: getSubSpace in interface Space
        
        Returns:
            nothing
        
        Raises:
            NoSubSpaceException: in all cases
        
              - getDimension
        
        
        
        """
        ...
    class NoSubSpaceException(org.hipparchus.exception.MathRuntimeException):
        def __init__(self): ...

class Interval:
    """
    This class represents a 1D interval.
    
          - IntervalsSet
    """
    def __init__(self, lower: float, upper: float):
        """
        Simple constructor.
        
        Parameters:
            lower (double): lower bound of the interval
            upper (double): upper bound of the interval
        
        
        """
        ...
    def checkPoint(self, point: float, tolerance: float) -> org.hipparchus.geometry.partitioning.Region.Location:
        """
        Check a point with respect to the interval.
        
        Parameters:
            point (double): point to check
            tolerance (double): tolerance below which points are considered to belong to the boundary
        
        Returns:
            a code representing the point status: either INSIDE,
            OUTSIDE or
            BOUNDARY
        
        
        """
        ...
    def getBarycenter(self) -> float:
        """
        Get the barycenter of the interval.
        
        Returns:
            barycenter of the interval
        
        
        """
        ...
    def getInf(self) -> float:
        """
        Get the lower bound of the interval.
        
        Returns:
            lower bound of the interval
        
        
        """
        ...
    def getSize(self) -> float:
        """
        Get the size of the interval.
        
        Returns:
            size of the interval
        
        
        """
        ...
    def getSup(self) -> float:
        """
        Get the upper bound of the interval.
        
        Returns:
            upper bound of the interval
        
        
        """
        ...

class IntervalsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Euclidean1D, 'Vector1D', 'OrientedPoint', 'SubOrientedPoint', Euclidean1D, 'Vector1D', 'OrientedPoint', 'SubOrientedPoint'], java.lang.Iterable[typing.MutableSequence[float]]):
    """
    implements Iterable<double[]>
    
    This class represents a 1D region: a set of intervals.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection['SubOrientedPoint'], typing.Sequence['SubOrientedPoint'], typing.Set['SubOrientedPoint']], double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean1D, 'Vector1D', 'OrientedPoint', 'SubOrientedPoint'], double: float): ...
    def asList(self) -> java.util.List[Interval]:
        """
        Build an ordered list of intervals representing the instance.
        
        This method builds this intervals set as an ordered list of Interval elements. If the intervals set has no lower limit, the first interval will have its low bound equal to NEGATIVE_INFINITY. If the intervals set has no upper limit, the last interval will have its upper bound equal to POSITIVE_INFINITY. An empty tree will build an empty list while a tree representing the whole real line will build a one element list with both bounds being infinite.
        
        Returns:
            a new ordered list containing Interval elements
        
        
        """
        ...
    def buildNew(self, tree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean1D, 'Vector1D', 'OrientedPoint', 'SubOrientedPoint']) -> 'IntervalsSet':
        """
        Build a region using the instance as a prototype.
        
        This method allow to create new instances without knowing exactly the type of the region. It is an application of the prototype design pattern.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Specified by: buildNew in interface Region
        
        Specified by: buildNew in class AbstractRegion
        
        Parameters:
            tree (BSPTree<Euclidean1D,Vector1D,OrientedPoint,SubOrientedPoint> tree): inside/outside BSP tree representing the new region
        
        Returns:
            the built region
        
        
        """
        ...
    def getInf(self) -> float:
        """
        Get the lowest value belonging to the instance.
        
        Returns:
            lowest value belonging to the instance (NEGATIVE_INFINITY if the instance doesn't have any low bound,
            POSITIVE_INFINITY if the instance is empty)
        
        
        """
        ...
    def getInteriorPoint(self) -> 'Vector1D':
        """
        Get an interior point.
        
        Specified by: getInteriorPoint in interface Region
        
        Returns:
            an arbitrary interior point, or null if region is empty
        
        
        """
        ...
    def getSup(self) -> float:
        """
        Get the highest value belonging to the instance.
        
        Returns:
            highest value belonging to the instance (POSITIVE_INFINITY if the instance doesn't have any high bound,
            NEGATIVE_INFINITY if the instance is empty)
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[typing.MutableSequence[float]]:
        """
        The iterator returns the limit values of sub-intervals in ascending order.
        
        The iterator does not support the optional remove operation.
        
        Specified by: iterator in interface Iterable
        
        
        """
        ...
    def projectToBoundary(self, point: 'Vector1D') -> org.hipparchus.geometry.partitioning.BoundaryProjection[Euclidean1D, 'Vector1D']:
        """
        Project a point on the boundary of the region.
        
        Specified by: projectToBoundary in interface Region
        
        Overrides: projectToBoundary in class AbstractRegion
        
        Parameters:
            point (Vector1D): point to check
        
        Returns:
            projection of the point on the boundary
        
        
        """
        ...

class OrientedPoint(org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D, 'Vector1D', 'OrientedPoint', 'SubOrientedPoint']):
    """
    implements Hyperplane<Euclidean1D,Vector1D,OrientedPoint,SubOrientedPoint>
    
    This class represents a 1D oriented hyperplane.
    
    An hyperplane in 1D is a simple point, its orientation being a boolean.
    
    Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, location: 'Vector1D', direct: bool, tolerance: float):
        """
        Simple constructor.
        
        Parameters:
            location (Vector1D): location of the hyperplane
            direct (boolean): if true, the plus side of the hyperplane is towards abscissas greater than location
            tolerance (double): tolerance below which points are considered to belong to the hyperplane
        
        
        """
        ...
    def arbitraryPoint(self) -> 'Vector1D':
        """
        Get an arbitrary point in the hyperplane.
        
        Specified by: arbitraryPoint in interface Hyperplane
        
        Returns:
            arbirary point in the hyperplane
        
        
        """
        ...
    def copySelf(self) -> 'OrientedPoint':
        """
        Copy the instance.
        
        Since instances are immutable, this method directly returns the instance.
        
        Specified by: copySelf in interface Hyperplane
        
        Returns:
            the instance itself
        
        
        """
        ...
    def emptyHyperplane(self) -> 'SubOrientedPoint':
        """
        Build a sub-hyperplane covering nothing..
        
        Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a dummy implementation of a SubHyperplane. This implementation is only used to allow the SubHyperplane class implementation to work properly, it should not be used otherwise.
        
        Specified by: emptyHyperplane in interface Hyperplane
        
        Returns:
            a dummy sub hyperplane
        
        
        """
        ...
    def getLocation(self) -> 'Vector1D':
        """
        Get the hyperplane location on the real line.
        
        Returns:
            the hyperplane location
        
        
        """
        ...
    def getOffset(self, point: 'Vector1D') -> float:
        """
        Get the offset (oriented distance) of a point.
        
        The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
        Specified by: getOffset in interface Hyperplane
        
        Parameters:
            point (Vector1D): point to check
        
        Returns:
            offset of the point
        
        
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
            true if the plus side of the hyperplane is towards abscissae greater than hyperplane location
        
        
        """
        ...
    def moveToOffset(self, point: 'Vector1D', offset: float) -> 'Vector1D':
        """
        Move point up to specified offset.
        
        Motion is orthogonal to the hyperplane
        
        Specified by: moveToOffset in interface Hyperplane
        
        Parameters:
            point (Vector1D): point to move
            offset (double): desired offset
        
        Returns:
            moved point at desired offset
        
        
        """
        ...
    def project(self, point: 'Vector1D') -> 'Vector1D':
        """
        Project a point to the hyperplane.
        
        Specified by: project in interface Hyperplane
        
        Parameters:
            point (Vector1D): point to project
        
        Returns:
            projected point
        
        
        """
        ...
    def revertSelf(self) -> None:
        """
        Revert the instance.
        """
        ...
    def sameOrientationAs(self, other: 'OrientedPoint') -> bool:
        """
        Check if the instance has the same orientation as another hyperplane.
        
        This method is expected to be called on parallel hyperplanes. The method should not re-check for parallelism, only for orientation, typically by testing something like the sign of the dot-products of normals.
        
        Specified by: sameOrientationAs in interface Hyperplane
        
        Parameters:
            other (OrientedPoint): other hyperplane to check against the instance
        
        Returns:
            true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubOrientedPoint':
        """
        Build a region covering the whole hyperplane.
        
        Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a dummy implementation of a SubHyperplane. This implementation is only used to allow the SubHyperplane class implementation to work properly, it should not be used otherwise.
        
        Specified by: wholeHyperplane in interface Hyperplane
        
        Returns:
            a dummy sub hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> IntervalsSet:
        """
        Build a region covering the whole space.
        
        Specified by: wholeSpace in interface Hyperplane
        
        Returns:
            a region containing the instance (really an IntervalsSet instance)
        
        
        """
        ...

class SubOrientedPoint(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Euclidean1D, 'Vector1D', OrientedPoint, 'SubOrientedPoint', Euclidean1D, 'Vector1D', OrientedPoint, 'SubOrientedPoint']):
    """
    This class represents sub-hyperplane for OrientedPoint.
    
    An hyperplane in 1D is a simple point, its orientation being a boolean.
    """
    def __init__(self, hyperplane: OrientedPoint, remainingRegion: org.hipparchus.geometry.partitioning.Region[Euclidean1D, 'Vector1D', OrientedPoint, 'SubOrientedPoint']):
        """
        Simple constructor.
        
        Parameters:
            hyperplane (OrientedPoint): underlying hyperplane
            remainingRegion (Region<Euclidean1D,Vector1D,OrientedPoint,SubOrientedPoint> remainingRegion): remaining region of the hyperplane
        
        
        """
        ...
    def getInteriorPoint(self) -> 'Vector1D':
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
    def split(self, hyperplane: OrientedPoint) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean1D, 'Vector1D', OrientedPoint, 'SubOrientedPoint']:
        """
        Split the instance in two parts by an hyperplane.
        
        Specified by: split in interface SubHyperplane
        
        Specified by: split in class AbstractSubHyperplane
        
        Parameters:
            hyperplane (OrientedPoint): splitting hyperplane
        
        Returns:
            an object containing both the part of the instance on the plus side of the hyperplane and the part of the instance on
            the minus side of the hyperplane
        
        
        """
        ...

class Vector1D(org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']):
    """
    implements Vector<Euclidean1D,Vector1D>
    
    This class represents a 1D vector.
    
    Instances of this class are guaranteed to be immutable.
    
          - serialized
    """
    ZERO: typing.ClassVar['Vector1D'] = ...
    """
    Origin (coordinates: 0).
    """
    ONE: typing.ClassVar['Vector1D'] = ...
    """
    Unit (coordinates: 1).
    """
    NaN: typing.ClassVar['Vector1D'] = ...
    """
    A vector with all coordinates set to NaN.
    """
    POSITIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    """
    A vector with all coordinates set to positive infinity.
    """
    NEGATIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    """
    A vector with all coordinates set to negative infinity.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D', double3: float, vector1D3: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D', double3: float, vector1D3: 'Vector1D', double4: float, vector1D4: 'Vector1D'): ...
    @typing.overload
    def add(self, factor: float, v: 'Vector1D') -> 'Vector1D':
        """
        Add a scaled vector to the instance.
        
        Specified by: add in interface Vector
        
        Parameters:
            factor (double): scale factor to apply to v before adding it
            v (Vector1D): vector to add
        
        Returns:
            a new vector
        
        
        """
        ...
    @typing.overload
    def add(self, v: 'Vector1D') -> 'Vector1D':
        """
        Add a vector to the instance.
        
        Specified by: add in interface Vector
        
        Parameters:
            v (Vector1D): vector to add
        
        Returns:
            a new vector
        
        """
        ...
    @typing.overload
    def distance(self, vector1D: 'Vector1D') -> float:
        """
        Compute the distance between the instance and another point.
        
        Specified by: distance in interface Point
        
        Parameters:
            p (Vector1D): second point
        
        Returns:
            the distance between the instance and p
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector1D): first vector
            p2 (Vector1D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def distance1(self, p: 'Vector1D') -> float:
        """
        Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Specified by: distance1 in interface Vector
        
        Parameters:
            p (Vector1D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`1` norm
        
        
        """
        ...
    @typing.overload
    def distanceInf(self, vector1D: 'Vector1D') -> float:
        """
        Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Specified by: distanceInf in interface Vector
        
        Parameters:
            p (Vector1D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`∞` norm
        
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector1D): first vector
            p2 (Vector1D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    @typing.overload
    def distanceSq(self, vector1D: 'Vector1D') -> float:
        """
        Compute the square of the distance between the instance and another vector.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Specified by: distanceSq in interface Vector
        
        Parameters:
            p (Vector1D): second vector
        
        Returns:
            the square of the distance between the instance and p
        
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector1D): first vector
            p2 (Vector1D): second vector
        
        Returns:
            the square of the distance between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def dotProduct(self, v: 'Vector1D') -> float:
        """
        Compute the dot-product of the instance and another vector.
        
        Specified by: dotProduct in interface Vector
        
        Parameters:
            v (Vector1D): second vector
        
        Returns:
            the dot product this.v
        
        
        """
        ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 1D vectors.
        
        If all coordinates of two 1D vectors are exactly the same, and none are NaN, the two 1D vectors are considered to be equal.
        
        NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) coordinates of the 1D vector are equal to NaN, the 1D vector is equal to NaN.
        
        Overrides: equals in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 1D vector objects are equal, false if object is null, not an instance of Vector1D, or not equal to this
            Vector1D instance
        
        
        """
        ...
    def equalsIeee754(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 1D vectors.
        
        If all coordinates of two 1D vectors are exactly the same, and none are NaN, the two 1D vectors are considered to be equal.
        
        In compliance with IEEE754 handling, if any coordinates of any of the two vectors are NaN, then the vectors are considered different. This implies that NaN.equals(NaN) returns false despite the instance is checked against itself.
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 1D vector objects are equal, false if object is null, not an instance of Vector1D, or not equal to this
            Vector1D instance
        
        Since:
            2.1
        
        
        """
        ...
    def getNorm(self) -> float:
        """
        Get the L :sub:`2` norm for the vector.
        
        Specified by: getNorm in interface Vector
        
        Returns:
            Euclidean norm for the vector
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
        Get the L :sub:`1` norm for the vector.
        
        Specified by: getNorm1 in interface Vector
        
        Returns:
            L :sub:`1` norm for the vector
        
        
        """
        ...
    def getNormInf(self) -> float:
        """
        Get the L :sub:`∞` norm for the vector.
        
        Specified by: getNormInf in interface Vector
        
        Returns:
            L :sub:`∞` norm for the vector
        
        
        """
        ...
    def getNormSq(self) -> float:
        """
        Get the square of the norm for the vector.
        
        Specified by: getNormSq in interface Vector
        
        Returns:
            square of the Euclidean norm for the vector
        
        
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
    def getX(self) -> float:
        """
        Get the abscissa of the vector.
        
        Returns:
            abscissa of the vector
        
              - 
        
        
        
        """
        ...
    def getZero(self) -> 'Vector1D':
        """
        Get the null vector of the vectorial space or origin point of the affine space.
        
        Specified by: getZero in interface Vector
        
        Returns:
            null vector of the vectorial space or origin point of the affine space
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the 1D vector.
        
        All NaN values have the same hash code.
        
        Overrides: hashCode in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Returns true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        Specified by: isInfinite in interface Vector
        
        Returns:
            true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        
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
    def moveTowards(self, other: 'Vector1D', ratio: float) -> 'Vector1D':
        """
        Move towards another point.
        
        Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
        Specified by: moveTowards in interface Point
        
        Parameters:
            other (Vector1D): other point
            ratio (double): motion ratio,
        
        Returns:
            moved point
        
        
        """
        ...
    def negate(self) -> 'Vector1D':
        """
        Get the opposite of the instance.
        
        Specified by: negate in interface Vector
        
        Returns:
            a new vector which is opposite to the instance
        
        
        """
        ...
    def scalarMultiply(self, a: float) -> 'Vector1D':
        """
        Multiply the instance by a scalar.
        
        Specified by: scalarMultiply in interface Vector
        
        Parameters:
            a (double): scalar
        
        Returns:
            a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, factor: float, v: 'Vector1D') -> 'Vector1D':
        """
        Subtract a scaled vector from the instance.
        
        Specified by: subtract in interface Vector
        
        Parameters:
            factor (double): scale factor to apply to v before subtracting it
            v (Vector1D): vector to subtract
        
        Returns:
            a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, p: 'Vector1D') -> 'Vector1D':
        """
        Subtract a vector from the instance.
        
        Specified by: subtract in interface Vector
        
        Parameters:
            p (Vector1D): vector to subtract
        
        Returns:
            a new vector
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
        Get a string representation of this vector.
        
        Overrides: toString in class Object
        
        Returns:
            a string representation of this vector
        
        """
        ...
    @typing.overload
    def toString(self, format: java.text.NumberFormat) -> str:
        """
        Get a string representation of this vector.
        
        Specified by: toString in interface Vector
        
        Parameters:
            format (NumberFormat): the custom format for components
        
        Returns:
            a string representation of this vector
        
        
        """
        ...

class Vector1DFormat(org.hipparchus.geometry.VectorFormat[Euclidean1D, Vector1D]):
    """
    Formats a 1D vector in components list format "{x}".
    
    The prefix and suffix "{" and "}" can be replaced by any user-defined strings. The number format for components can be configured.
    
    White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the default separator does include a space character that is used at format time, both input string "{1}" and " { 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
    Note: using "," as a separator may interfere with the grouping separator of the default NumberFormat for the current locale. Thus it is advised to use a NumberFormat instance with disabled grouping in such a case.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[org.hipparchus.geometry.Space, org.hipparchus.geometry.Vector]) -> str: ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, Vector1D], stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def getVector1DFormat() -> 'Vector1DFormat':
        """
        Returns:
            the default 1D vector format.
        
        Since:
            1.4
        
        """
        ...
    @typing.overload
    @staticmethod
    def getVector1DFormat(locale: java.util.Locale) -> 'Vector1DFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the 1D vector format specific to the given locale.
        
        Since:
            1.4
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Vector1D:
        """
        Parses a string to produce a Vector object.
        
        Specified by: parse in class VectorFormat
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/output parsing parameter.
        
        Returns:
            the parsed Vector object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Vector1D: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.oned")``.

    Euclidean1D: typing.Type[Euclidean1D]
    Interval: typing.Type[Interval]
    IntervalsSet: typing.Type[IntervalsSet]
    OrientedPoint: typing.Type[OrientedPoint]
    SubOrientedPoint: typing.Type[SubOrientedPoint]
    Vector1D: typing.Type[Vector1D]
    Vector1DFormat: typing.Type[Vector1DFormat]
