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
    public class Euclidean1D extends :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`, :class:`~org.hipparchus.geometry.Space`
    
        This class implements a one-dimensional space.
    
        Also see:
            :meth:`~serialized`
    """
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
    def getInstance() -> 'Euclidean1D':
        """
            Get the unique instance.
        
            Returns:
                the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> org.hipparchus.geometry.Space: ...
    class NoSubSpaceException(org.hipparchus.exception.MathRuntimeException):
        def __init__(self): ...

class Interval:
    """
    public class Interval extends :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class represents a 1D interval.
    
        Also see:
            :class:`~org.hipparchus.geometry.euclidean.oned.IntervalsSet`
    """
    def __init__(self, double: float, double2: float): ...
    def checkPoint(self, double: float, double2: float) -> org.hipparchus.geometry.partitioning.Region.Location:
        """
            Check a point with respect to the interval.
        
            Parameters:
                point (double): point to check
                tolerance (double): tolerance below which points are considered to belong to the boundary
        
            Returns:
                a code representing the point status: either :meth:`~org.hipparchus.geometry.partitioning.Region.Location.INSIDE`,
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.OUTSIDE` or
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.BOUNDARY`
        
        
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

class IntervalsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Euclidean1D, Euclidean1D], java.lang.Iterable[typing.List[float]]):
    """
    public class IntervalsSet extends :class:`~org.hipparchus.geometry.partitioning.AbstractRegion`<:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`, :class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`> implements :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable?is`<double[]>
    
        This class represents a 1D region: a set of intervals.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[org.hipparchus.geometry.partitioning.SubHyperplane[Euclidean1D]], typing.Sequence[org.hipparchus.geometry.partitioning.SubHyperplane[Euclidean1D]], typing.Set[org.hipparchus.geometry.partitioning.SubHyperplane[Euclidean1D]]], double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean1D], double: float): ...
    def asList(self) -> java.util.List[Interval]: ...
    def buildNew(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean1D]) -> 'IntervalsSet': ...
    def getInf(self) -> float:
        """
            Get the lowest value belonging to the instance.
        
            Returns:
                lowest value belonging to the instance (:code:`Double.NEGATIVE_INFINITY` if the instance doesn't have any low bound,
                :code:`Double.POSITIVE_INFINITY` if the instance is empty)
        
        
        """
        ...
    def getSup(self) -> float:
        """
            Get the highest value belonging to the instance.
        
            Returns:
                highest value belonging to the instance (:code:`Double.POSITIVE_INFINITY` if the instance doesn't have any high bound,
                :code:`Double.NEGATIVE_INFINITY` if the instance is empty)
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[typing.List[float]]:
        """
        
            The iterator returns the limit values of sub-intervals in ascending order.
        
            The iterator does *not* support the optional :code:`remove` operation.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable.html?is` in
                interface :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable?is`
        
        
        """
        ...
    def projectToBoundary(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> org.hipparchus.geometry.partitioning.BoundaryProjection[Euclidean1D]: ...

class OrientedPoint(org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D]):
    """
    public class OrientedPoint extends :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`>
    
        This class represents a 1D oriented hyperplane.
    
        An hyperplane in 1D is a simple point, its orientation being a boolean.
    
        Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, vector1D: 'Vector1D', boolean: bool, double: float): ...
    def copySelf(self) -> 'OrientedPoint':
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
    def emptyHyperplane(self) -> 'SubOrientedPoint':
        """
            Build a sub-hyperplane covering nothing..
        
            Since this class represent zero dimension spaces which does not have lower dimension sub-spaces, this method returns a
            dummy implementation of a :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`. This implementation is only used
            to allow the :class:`~org.hipparchus.geometry.partitioning.SubHyperplane` class implementation to work properly, it
            should *not* be used otherwise.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.emptyHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
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
    @typing.overload
    def getOffset(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> float: ...
    @typing.overload
    def getOffset(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
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
                true if the plus side of the hyperplane is towards abscissae greater than hyperplane location
        
        
        """
        ...
    def project(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> org.hipparchus.geometry.Point[Euclidean1D]: ...
    def revertSelf(self) -> None:
        """
            Revert the instance.
        
        """
        ...
    def sameOrientationAs(self, hyperplane: org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D]) -> bool: ...
    def wholeHyperplane(self) -> 'SubOrientedPoint':
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
    def wholeSpace(self) -> IntervalsSet:
        """
            Build a region covering the whole space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.wholeSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a region containing the instance (really an :class:`~org.hipparchus.geometry.euclidean.oned.IntervalsSet` instance)
        
        
        """
        ...

class SubOrientedPoint(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Euclidean1D, Euclidean1D]):
    """
    public class SubOrientedPoint extends :class:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane`<:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`, :class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`>
    
        This class represents sub-hyperplane for :class:`~org.hipparchus.geometry.euclidean.oned.OrientedPoint`.
    
        An hyperplane in 1D is a simple point, its orientation being a boolean.
    
        Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, hyperplane: org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D], region: org.hipparchus.geometry.partitioning.Region[Euclidean1D]): ...
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
    def split(self, hyperplane: org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D]) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean1D]: ...

class Vector1D(org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']):
    """
    public class Vector1D extends :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.geometry.Vector`<:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`, :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`>
    
        This class represents a 1D vector.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :meth:`~serialized`
    """
    ZERO: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D` ZERO
    
        Origin (coordinates: 0).
    
    """
    ONE: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D` ONE
    
        Unit (coordinates: 1).
    
    """
    NaN: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D` NaN
    
        A vector with all coordinates set to NaN.
    
    """
    POSITIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D` POSITIVE_INFINITY
    
        A vector with all coordinates set to positive infinity.
    
    """
    NEGATIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D` NEGATIVE_INFINITY
    
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
    def add(self, double: float, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def add(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def distance(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> float:
        """
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def distance1(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
    @typing.overload
    def distanceInf(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float:
        """
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    @typing.overload
    def distanceSq(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float:
        """
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): second vector
        
            Returns:
                the square of the distance between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def dotProduct(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 1D vectors.
        
            If all coordinates of two 1D vectors are exactly the same, and none are :code:`Double.NaN`, the two 1D vectors are
            considered to be equal.
        
            :code:`NaN` coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or
            all) coordinates of the 1D vector are equal to :code:`Double.NaN`, the 1D vector is equal to
            :meth:`~org.hipparchus.geometry.euclidean.oned.Vector1D.NaN`.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`): Object to test for equality to this
        
            Returns:
                true if two 1D vector objects are equal, false if object is null, not an instance of Vector1D, or not equal to this
                Vector1D instance
        
        
        """
        ...
    def equalsIeee754(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 1D vectors.
        
            If all coordinates of two 1D vectors are exactly the same, and none are :code:`NaN`, the two 1D vectors are considered
            to be equal.
        
            In compliance with IEEE754 handling, if any coordinates of any of the two vectors are :code:`NaN`, then the vectors are
            considered different. This implies that
            :meth:`~org.hipparchus.geometry.euclidean.oned.Vector1D.NaN`.equals(:meth:`~org.hipparchus.geometry.euclidean.oned.Vector1D.NaN`)
            returns :code:`false` despite the instance is checked against itself.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`): Object to test for equality to this
        
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
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.getNorm` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                Euclidean norm for the vector
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
            Get the L :sub:`1` norm for the vector.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.getNorm1` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                L :sub:`1` norm for the vector
        
        
        """
        ...
    def getNormInf(self) -> float:
        """
            Get the L :sub:`∞` norm for the vector.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.getNormInf` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                L :sub:`∞` norm for the vector
        
        
        """
        ...
    def getNormSq(self) -> float:
        """
            Get the square of the norm for the vector.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.getNormSq` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                square of the Euclidean norm for the vector
        
        
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
    def getX(self) -> float:
        """
            Get the abscissa of the vector.
        
            Returns:
                abscissa of the vector
        
            Also see:
                :meth:`~org.hipparchus.geometry.euclidean.oned.Vector1D.%3Cinit%3E`
        
        
        """
        ...
    def getZero(self) -> 'Vector1D':
        """
            Get the null vector of the vectorial space or origin point of the affine space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.getZero` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                null vector of the vectorial space or origin point of the affine space
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the 1D vector.
        
            All NaN values have the same hash code.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Returns true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.isInfinite` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        
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
    def negate(self) -> 'Vector1D':
        """
            Get the opposite of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.negate` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                a new vector which is opposite to the instance
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'Vector1D':
        """
            Multiply the instance by a scalar.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.scalarMultiply` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                a (double): scalar
        
            Returns:
                a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def subtract(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a string representation of this vector.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this vector
        
        """
        ...
    @typing.overload
    def toString(self, numberFormat: java.text.NumberFormat) -> str:
        """
            Get a string representation of this vector.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.toString` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                format (:class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat?is`): the custom format for components
        
            Returns:
                a string representation of this vector
        
        
        """
        ...

class Vector1DFormat(org.hipparchus.geometry.VectorFormat[Euclidean1D, Vector1D]):
    """
    public class Vector1DFormat extends :class:`~org.hipparchus.geometry.VectorFormat`<:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`, :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`>
    
        Formats a 1D vector in components list format "{x}".
    
        The prefix and suffix "{" and "}" can be replaced by any user-defined strings. The number format for components can be
        configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1}" and " { 1 } " will
        be parsed without error and the same vector will be returned. In the second case, however, the parse position after
        parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        **Note:** using "," as a separator may interfere with the grouping separator of the default
        :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat?is` for
        the current locale. Thus it is advised to use a
        :class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat?is`
        instance with disabled grouping in such a case.
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
            Returns the default 1D vector format for the current locale.
        
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
            Returns the default 1D vector format for the given locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): the specific locale used by the format.
        
            Returns:
                the 1D vector format specific to the given locale.
        
            Since:
                1.4
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Vector1D:
        """
            Parses a string to produce a :class:`~org.hipparchus.geometry.Vector` object.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.VectorFormat.parse` in class :class:`~org.hipparchus.geometry.VectorFormat`
        
            Parameters:
                source (:class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the string to parse
                pos (:class:`~org.hipparchus.geometry.euclidean.oned.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition?is`): input/output parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.geometry.Vector` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Vector1D: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.oned")``.

    Euclidean1D: typing.Type[Euclidean1D]
    Interval: typing.Type[Interval]
    IntervalsSet: typing.Type[IntervalsSet]
    OrientedPoint: typing.Type[OrientedPoint]
    SubOrientedPoint: typing.Type[SubOrientedPoint]
    Vector1D: typing.Type[Vector1D]
    Vector1DFormat: typing.Type[Vector1DFormat]
