
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.text
import java.util
import jpype
import org.hipparchus
import org.hipparchus.geometry
import org.hipparchus.geometry.enclosing
import org.hipparchus.geometry.euclidean.oned
import org.hipparchus.geometry.euclidean.twod.hull
import org.hipparchus.geometry.partitioning
import typing



class DiskGenerator(org.hipparchus.geometry.enclosing.SupportBallGenerator['Euclidean2D', 'Vector2D']):
    """
    Class generating an enclosing ball from its support points.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def ballOnSupport(self, support: java.util.List['Vector2D']) -> org.hipparchus.geometry.enclosing.EnclosingBall['Euclidean2D', 'Vector2D']:
        """
        Create a ball whose boundary lies on prescribed support points.
        
        Specified by: ballOnSupport in interface SupportBallGenerator
        
        Parameters:
            support (List<Vector2D> support): support points (may be empty)
        
        Returns:
            ball whose boundary lies on the prescribed support points
        
        
        """
        ...

class Euclidean2D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    This class implements a two-dimensional space.
    
    Also see:
        serialized
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
    def getInstance() -> 'Euclidean2D':
        """
        Get the unique instance.
        
        Returns:
            the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> org.hipparchus.geometry.euclidean.oned.Euclidean1D:
        """
        Get the n-1 dimension subspace of this space.
        
        Specified by: getSubSpace in interface Space
        
        Returns:
            n-1 dimension sub-space of this space
        
        Also see:
            getDimension
        
        
        """
        ...

_FieldVector2D__T = typing.TypeVar('_FieldVector2D__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldVector2D(typing.Generic[_FieldVector2D__T]):
    """
    This class is a re-implementation of Vector2D using hipparchus.
    
    Instance of this class are guaranteed to be immutable.
    
    Since:
        1.6
    """
    @typing.overload
    def __init__(self, double: float, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'FieldVector2D'[_FieldVector2D__T], a2: float, u2: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'FieldVector2D'[_FieldVector2D__T], a2: float, u2: 'FieldVector2D'[_FieldVector2D__T], a3: float, u3: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'FieldVector2D'[_FieldVector2D__T], a2: float, u2: 'FieldVector2D'[_FieldVector2D__T], a3: float, u3: 'FieldVector2D'[_FieldVector2D__T], a4: float, u4: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, t2: _FieldVector2D__T): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, a1: _FieldVector2D__T, u1: 'FieldVector2D'[_FieldVector2D__T], a2: _FieldVector2D__T, u2: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, a1: _FieldVector2D__T, u1: 'FieldVector2D'[_FieldVector2D__T], a2: _FieldVector2D__T, u2: 'FieldVector2D'[_FieldVector2D__T], a3: _FieldVector2D__T, u3: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, a1: _FieldVector2D__T, u1: 'FieldVector2D'[_FieldVector2D__T], a2: _FieldVector2D__T, u2: 'FieldVector2D'[_FieldVector2D__T], a3: _FieldVector2D__T, u3: 'FieldVector2D'[_FieldVector2D__T], a4: _FieldVector2D__T, u4: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, vector2D: 'Vector2D'): ...
    @typing.overload
    def __init__(self, a1: _FieldVector2D__T, u1: 'Vector2D', a2: _FieldVector2D__T, u2: 'Vector2D'): ...
    @typing.overload
    def __init__(self, a1: _FieldVector2D__T, u1: 'Vector2D', a2: _FieldVector2D__T, u2: 'Vector2D', a3: _FieldVector2D__T, u3: 'Vector2D'): ...
    @typing.overload
    def __init__(self, a1: _FieldVector2D__T, u1: 'Vector2D', a2: _FieldVector2D__T, u2: 'Vector2D', a3: _FieldVector2D__T, u3: 'Vector2D', a4: _FieldVector2D__T, u4: 'Vector2D'): ...
    @typing.overload
    def __init__(self, v: typing.Union[typing.List[_FieldVector2D__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldVector2D__T], vector2D: 'Vector2D'): ...
    @typing.overload
    def add(self, factor: float, v: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, factor: float, v: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, factor: _FieldVector2D__T, v: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, factor: _FieldVector2D__T, v: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, v: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, v: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    _angle_0__T = typing.TypeVar('_angle_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _angle_1__T = typing.TypeVar('_angle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _angle_2__T = typing.TypeVar('_angle_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def angle(v1: 'FieldVector2D'[_angle_0__T], v2: 'FieldVector2D'[_angle_0__T]) -> _angle_0__T: ...
    @typing.overload
    @staticmethod
    def angle(v1: 'FieldVector2D'[_angle_1__T], v2: 'Vector2D') -> _angle_1__T: ...
    @typing.overload
    @staticmethod
    def angle(v1: 'Vector2D', v2: 'FieldVector2D'[_angle_2__T]) -> _angle_2__T: ...
    @typing.overload
    def crossProduct(self, p1: 'FieldVector2D'[_FieldVector2D__T], p2: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
        Compute the cross-product of the instance and the given points.
        
        The cross product can be used to determine the location of a point with regard to the line formed by (p1, p2) and is calculated as: \[ P = (x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) \] with \(p3 = (x_3, y_3)\) being this instance.
        
        If the result is 0, the points are collinear, i.e. lie on a single straight line L; if it is positive, this point lies to the left, otherwise to the right of the line formed by (p1, p2).
        
        Parameters:
            p1 (Vector2D): first point of the line
            p2 (Vector2D): second point of the line
        
        Returns:
            the cross-product
        
        Also see:
            `Cross product (Wikipedia) <http://en.wikipedia.org/wiki/Cross_product>`
        
        
        """
        ...
    @typing.overload
    def crossProduct(self, p1: 'Vector2D', p2: 'Vector2D') -> _FieldVector2D__T: ...
    _distance_2__T = typing.TypeVar('_distance_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance_3__T = typing.TypeVar('_distance_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance_4__T = typing.TypeVar('_distance_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distance(self, v: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
        Compute the distance between the instance and another vector according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            v (Vector2D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`2` norm
        
        """
        ...
    @typing.overload
    def distance(self, v: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distance(p1: 'FieldVector2D'[_distance_2__T], p2: 'FieldVector2D'[_distance_2__T]) -> _distance_2__T:
        """
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(p1: 'FieldVector2D'[_distance_3__T], p2: 'Vector2D') -> _distance_3__T: ...
    @typing.overload
    @staticmethod
    def distance(p1: 'Vector2D', p2: 'FieldVector2D'[_distance_4__T]) -> _distance_4__T: ...
    _distance1_2__T = typing.TypeVar('_distance1_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance1_3__T = typing.TypeVar('_distance1_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance1_4__T = typing.TypeVar('_distance1_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distance1(self, v: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
        Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Parameters:
            v (Vector2D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`1` norm
        
        """
        ...
    @typing.overload
    def distance1(self, v: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distance1(p1: 'FieldVector2D'[_distance1_2__T], p2: 'FieldVector2D'[_distance1_2__T]) -> _distance1_2__T:
        """
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(p1: 'FieldVector2D'[_distance1_3__T], p2: 'Vector2D') -> _distance1_3__T: ...
    @typing.overload
    @staticmethod
    def distance1(p1: 'Vector2D', p2: 'FieldVector2D'[_distance1_4__T]) -> _distance1_4__T: ...
    _distanceInf_2__T = typing.TypeVar('_distanceInf_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceInf_3__T = typing.TypeVar('_distanceInf_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceInf_4__T = typing.TypeVar('_distanceInf_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distanceInf(self, v: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
        Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            v (Vector2D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`∞` norm
        
        """
        ...
    @typing.overload
    def distanceInf(self, v: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(p1: 'FieldVector2D'[_distanceInf_2__T], p2: 'FieldVector2D'[_distanceInf_2__T]) -> _distanceInf_2__T:
        """
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`∞` norm
        
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`∞` norm
        
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(p1: 'FieldVector2D'[_distanceInf_3__T], p2: 'Vector2D') -> _distanceInf_3__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(p1: 'Vector2D', p2: 'FieldVector2D'[_distanceInf_4__T]) -> _distanceInf_4__T: ...
    _distanceSq_2__T = typing.TypeVar('_distanceSq_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceSq_3__T = typing.TypeVar('_distanceSq_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceSq_4__T = typing.TypeVar('_distanceSq_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distanceSq(self, v: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
        Compute the square of the distance between the instance and another vector.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            v (Vector2D): second vector
        
        Returns:
            the square of the distance between the instance and p
        
        """
        ...
    @typing.overload
    def distanceSq(self, v: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(p1: 'FieldVector2D'[_distanceSq_2__T], p2: 'FieldVector2D'[_distanceSq_2__T]) -> _distanceSq_2__T:
        """
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the square of the distance between p1 and p2
        
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            p1 (FieldVector2D<T> p1): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the square of the distance between p1 and p2
        
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (FieldVector2D<T> p2): second vector
        
        Returns:
            the square of the distance between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(p1: 'FieldVector2D'[_distanceSq_3__T], p2: 'Vector2D') -> _distanceSq_3__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(p1: 'Vector2D', p2: 'FieldVector2D'[_distanceSq_4__T]) -> _distanceSq_4__T: ...
    @typing.overload
    def dotProduct(self, v: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
        Compute the dot-product of the instance and another vector.
        
        The implementation uses specific multiplication and addition algorithms to preserve accuracy and reduce cancellation effects. It should be very accurate even for nearly orthogonal vectors.
        
        Parameters:
            v (Vector2D): second vector
        
        Returns:
            the dot product this.v
        
        Also see:
            hipparchus
        
        
        """
        ...
    @typing.overload
    def dotProduct(self, v: 'Vector2D') -> _FieldVector2D__T: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 2D vectors.
        
        If all coordinates of two 2D vectors are exactly the same, and none of their hipparchus are NaN, the two 2D vectors are considered to be equal.
        
        NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) real part of the coordinates of the 3D vector are NaN, the 2D vector is NaN.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 2D vector objects are equal, false if object is null, not an instance of FieldVector2D, or not equal to this
            FieldVector2D instance
        
        
        """
        ...
    _getMinusI__T = typing.TypeVar('_getMinusI__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getMinusI(field: org.hipparchus.Field[_getMinusI__T]) -> 'FieldVector2D'[_getMinusI__T]:
        """
        Get opposite of the first canonical vector (coordinates: -1).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getMinusJ__T = typing.TypeVar('_getMinusJ__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getMinusJ(field: org.hipparchus.Field[_getMinusJ__T]) -> 'FieldVector2D'[_getMinusJ__T]:
        """
        Get opposite of the second canonical vector (coordinates: 0, -1).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getNaN__T = typing.TypeVar('_getNaN__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getNaN(field: org.hipparchus.Field[_getNaN__T]) -> 'FieldVector2D'[_getNaN__T]:
        """
        Get a vector with all coordinates set to NaN.
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getNegativeInfinity__T = typing.TypeVar('_getNegativeInfinity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getNegativeInfinity(field: org.hipparchus.Field[_getNegativeInfinity__T]) -> 'FieldVector2D'[_getNegativeInfinity__T]:
        """
        Get a vector with all coordinates set to negative infinity.
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    def getNorm(self) -> _FieldVector2D__T:
        """
        Get the L :sub:`2` norm for the vector.
        
        Returns:
            Euclidean norm for the vector
        
        
        """
        ...
    def getNorm1(self) -> _FieldVector2D__T:
        """
        Get the L :sub:`1` norm for the vector.
        
        Returns:
            L :sub:`1` norm for the vector
        
        
        """
        ...
    def getNormInf(self) -> _FieldVector2D__T:
        """
        Get the L :sub:`∞` norm for the vector.
        
        Returns:
            L :sub:`∞` norm for the vector
        
        
        """
        ...
    def getNormSq(self) -> _FieldVector2D__T:
        """
        Get the square of the norm for the vector.
        
        Returns:
            square of the Euclidean norm for the vector
        
        
        """
        ...
    _getPlusI__T = typing.TypeVar('_getPlusI__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPlusI(field: org.hipparchus.Field[_getPlusI__T]) -> 'FieldVector2D'[_getPlusI__T]:
        """
        Get first canonical vector (coordinates: 1, 0).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getPlusJ__T = typing.TypeVar('_getPlusJ__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPlusJ(field: org.hipparchus.Field[_getPlusJ__T]) -> 'FieldVector2D'[_getPlusJ__T]:
        """
        Get second canonical vector (coordinates: 0, 1).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getPositiveInfinity__T = typing.TypeVar('_getPositiveInfinity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPositiveInfinity(field: org.hipparchus.Field[_getPositiveInfinity__T]) -> 'FieldVector2D'[_getPositiveInfinity__T]:
        """
        Get a vector with all coordinates set to positive infinity.
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    def getX(self) -> _FieldVector2D__T:
        """
        Get the abscissa of the vector.
        
        Returns:
            abscissa of the vector
        
        
        """
        ...
    def getY(self) -> _FieldVector2D__T:
        """
        Get the ordinate of the vector.
        
        Returns:
            ordinate of the vector
        
        
        """
        ...
    _getZero__T = typing.TypeVar('_getZero__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getZero(field: org.hipparchus.Field[_getZero__T]) -> 'FieldVector2D'[_getZero__T]:
        """
        Get null vector (coordinates: 0, 0).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the 3D vector.
        
        All NaN values have the same hash code.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Returns true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        Returns:
            true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Returns true if any coordinate of this vector is NaN; false otherwise
        
        Returns:
            true if any coordinate of this vector is NaN; false otherwise
        
        
        """
        ...
    def negate(self) -> 'FieldVector2D'[_FieldVector2D__T]:
        """
        Get the opposite of the instance.
        
        Returns:
            a new vector which is opposite to the instance
        
        
        """
        ...
    def normalize(self) -> 'FieldVector2D'[_FieldVector2D__T]:
        """
        Get a normalized vector aligned with the instance.
        
        Returns:
            a new normalized vector
        
        Raises:
            hipparchus: if the norm is zero
        
        
        """
        ...
    _orientation__T = typing.TypeVar('_orientation__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def orientation(p: 'FieldVector2D'[_orientation__T], q: 'FieldVector2D'[_orientation__T], r: 'FieldVector2D'[_orientation__T]) -> _orientation__T:
        """
        Compute the orientation of a triplet of points.
        
        Parameters:
            p (FieldVector2D<T> p): first vector of the triplet
            q (FieldVector2D<T> q): second vector of the triplet
            r (FieldVector2D<T> r): third vector of the triplet
        
        Returns:
            a positive value if (p, q, r) defines a counterclockwise oriented triangle, a negative value if (p, q, r) defines a
            clockwise oriented triangle, and 0 if (p, q, r) are collinear or some points are equal
        
        Since:
            1.2
        
        
        """
        ...
    @typing.overload
    def scalarMultiply(self, a: float) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def scalarMultiply(self, a: _FieldVector2D__T) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, factor: float, v: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, factor: float, v: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, factor: _FieldVector2D__T, v: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, factor: _FieldVector2D__T, v: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, v: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, v: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    def toArray(self) -> typing.MutableSequence[_FieldVector2D__T]:
        """
        Get the vector coordinates as a dimension 2 array.
        
        Returns:
            vector coordinates
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
        Get a string representation of this vector.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this vector
        
        """
        ...
    @typing.overload
    def toString(self, format: java.text.NumberFormat) -> str:
        """
        Get a string representation of this vector.
        
        Parameters:
            format (NumberFormat): the custom format for components
        
        Returns:
            a string representation of this vector
        
        
        """
        ...
    def toVector2D(self) -> 'Vector2D':
        """
        Convert to a constant vector without extra field parts.
        
        Returns:
            a constant vector
        
        
        """
        ...

class Line(org.hipparchus.geometry.partitioning.Hyperplane[Euclidean2D, 'Vector2D', 'Line', 'SubLine'], org.hipparchus.geometry.partitioning.Embedding[Euclidean2D, 'Vector2D', org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D]):
    """
    This class represents an oriented line in the 2D plane.
    
    An oriented line can be defined either by prolongating a line segment between two points past these points, or by one point and an angular direction (in trigonometric orientation).
    
    Since it is oriented the two half planes at its two sides are unambiguously identified as a left half plane and a right half plane. This can be used to identify the interior and the exterior in a simple way by local properties only when part of a line is used to define part of a polygon boundary.
    
    A line can also be used to completely define a reference frame in the plane. It is sufficient to select one specific point in the line (the orthogonal projection of the original reference frame on the line) and to use the unit vector in the line direction and the orthogonal vector oriented from left half plane to right half plane. We define two coordinates by the process, the abscissa along the line, and the offset across the line. All points of the plane are uniquely identified by these two coordinates. The line is the set of points at zero offset, the left half plane is the set of points with negative offsets and the right half plane is the set of points with positive offsets.
    """
    @typing.overload
    def __init__(self, line: 'Line'): ...
    @typing.overload
    def __init__(self, vector2D: 'Vector2D', double: float, double2: float): ...
    @typing.overload
    def __init__(self, vector2D: 'Vector2D', vector2D2: 'Vector2D', double: float): ...
    def arbitraryPoint(self) -> 'Vector2D':
        """
        Get an arbitrary point in the hyperplane.
        
        Specified by: arbitraryPoint in interface Hyperplane
        
        Returns:
            arbirary point in the hyperplane
        
        
        """
        ...
    def contains(self, p: 'Vector2D') -> bool:
        """
        Check if the line contains a point.
        
        Parameters:
            p (Vector2D): point to check
        
        Returns:
            true if p belongs to the line
        
        
        """
        ...
    def copySelf(self) -> 'Line':
        """
        Copy the instance.
        
        The instance created is completely independent of the original one. A deep copy is used, none of the underlying objects are shared (except for immutable objects).
        
        Specified by: copySelf in interface Hyperplane
        
        Returns:
            a new hyperplane, copy of the instance
        
        
        """
        ...
    def distance(self, p: 'Vector2D') -> float:
        """
        Compute the distance between the instance and a point.
        
        This is a shortcut for invoking FastMath.abs(getOffset(p)), and provides consistency with what is in the org.hipparchus.geometry.euclidean.threed.Line class.
        
        Parameters:
            p (Vector2D): to check
        
        Returns:
            distance between the instance and the point
        
        
        """
        ...
    def emptyHyperplane(self) -> 'SubLine':
        """
        Build a sub-hyperplane covering nothing.
        
        Specified by: emptyHyperplane in interface Hyperplane
        
        Returns:
            a sub-hyperplane covering nothing
        
        
        """
        ...
    def getAngle(self) -> float:
        """
        Get the angle of the line.
        
        Returns:
            the angle of the line with respect to the abscissa axis
        
        
        """
        ...
    @typing.overload
    def getOffset(self, line: 'Line') -> float:
        """
        This method should be called only for parallel lines otherwise the result is not meaningful.
        
        The offset is 0 if both lines are the same, it is positive if the line is on the right side of the instance and negative if it is on the left side, according to its natural orientation.
        
        Parameters:
            line (Line): line to check
        
        Returns:
            offset of the line
        
        Get the offset (oriented distance) of a point.
        
        The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
        Specified by: getOffset in interface Hyperplane
        
        Parameters:
            point (Vector2D): point to check
        
        Returns:
            offset of the point
        
        
        """
        ...
    @typing.overload
    def getOffset(self, vector2D: 'Vector2D') -> float: ...
    def getOriginOffset(self) -> float:
        """
        Get the offset of the origin.
        
        Returns:
            the offset of the origin
        
        
        """
        ...
    def getPointAt(self, abscissa: org.hipparchus.geometry.euclidean.oned.Vector1D, offset: float) -> 'Vector2D':
        """
        Get one point from the plane.
        
        Parameters:
            abscissa (Vector1D): desired abscissa for the point
            offset (double): desired offset for the point
        
        Returns:
            one point in the plane, with given abscissa and offset relative to the line
        
        
        """
        ...
    def getReverse(self) -> 'Line':
        """
        Get the reverse of the instance.
        
        Get a line with reversed orientation with respect to the instance.
        
        As long as neither the instance nor its reverse are modified (i.e. as long as none of the reset, reset, revertSelf, setAngle or setOriginOffset methods are called), then the line and its reverse remain linked together so that getReverse() == line. When one of the line is modified, the link is deleted as both instance becomes independent.
        
        Returns:
            a new line, with orientation opposite to the instance orientation
        
        
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
    @staticmethod
    def getTransform(cXX: float, cYX: float, cXY: float, cYY: float, cX1: float, cY1: float) -> org.hipparchus.geometry.partitioning.Transform[Euclidean2D, 'Vector2D', 'Line', 'SubLine', org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D, org.hipparchus.geometry.euclidean.oned.OrientedPoint, org.hipparchus.geometry.euclidean.oned.SubOrientedPoint]:
        """
        Get a Transform embedding an affine transform.
        
        Parameters:
            cXX (double): transform factor between input abscissa and output abscissa
            cYX (double): transform factor between input abscissa and output ordinate
            cXY (double): transform factor between input ordinate and output abscissa
            cYY (double): transform factor between input ordinate and output ordinate
            cX1 (double): transform addendum for output abscissa
            cY1 (double): transform addendum for output ordinate
        
        Returns:
            a new transform that can be applied to either Vector2D,
            Line or SubHyperplane
            instances
        
        Raises:
            hipparchus: if the transform is non invertible
        
        
        """
        ...
    def intersection(self, other: 'Line') -> 'Vector2D':
        """
        Get the intersection point of the instance and another line.
        
        Parameters:
            other (Line): other line
        
        Returns:
            intersection point of the instance and the other line or null if there are no intersection points
        
        
        """
        ...
    def isParallelTo(self, line: 'Line') -> bool:
        """
        Check the instance is parallel to another line.
        
        Parameters:
            line (Line): other line to check
        
        Returns:
            true if the instance is parallel to the other line (they can have either the same or opposite orientations)
        
        
        """
        ...
    def moveToOffset(self, point: 'Vector2D', offset: float) -> 'Vector2D':
        """
        Move point up to specified offset.
        
        Motion is orthogonal to the hyperplane
        
        Specified by: moveToOffset in interface Hyperplane
        
        Parameters:
            point (Vector2D): point to move
            offset (double): desired offset
        
        Returns:
            moved point at desired offset
        
        
        """
        ...
    def project(self, point: 'Vector2D') -> 'Vector2D':
        """
        Project a point to the hyperplane.
        
        Specified by: project in interface Hyperplane
        
        Parameters:
            point (Vector2D): point to project
        
        Returns:
            projected point
        
        
        """
        ...
    @typing.overload
    def reset(self, p1: 'Vector2D', p2: float) -> None:
        """
        Reset the instance as if built from two points.
        
        The line is oriented from p1 to p2
        
        Parameters:
            p1 (Vector2D): first point
            p2 (Vector2D): second point
        
        Reset the instance as if built from a line and an angle.
        
        Parameters:
            p (Vector2D): point belonging to the line
            alpha (double): angle of the line with respect to abscissa axis
        
        
        """
        ...
    @typing.overload
    def reset(self, vector2D: 'Vector2D', vector2D2: 'Vector2D') -> None: ...
    def revertSelf(self) -> None:
        """
        Revert the instance.
        """
        ...
    def sameOrientationAs(self, other: 'Line') -> bool:
        """
        Check if the instance has the same orientation as another hyperplane.
        
        This method is expected to be called on parallel hyperplanes. The method should not re-check for parallelism, only for orientation, typically by testing something like the sign of the dot-products of normals.
        
        Specified by: sameOrientationAs in interface Hyperplane
        
        Parameters:
            other (Line): other hyperplane to check against the instance
        
        Returns:
            true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def setAngle(self, angle: float) -> None:
        """
        Set the angle of the line.
        
        Parameters:
            angle (double): new angle of the line with respect to the abscissa axis
        
        
        """
        ...
    def setOriginOffset(self, offset: float) -> None:
        """
        Set the offset of the origin.
        
        Parameters:
            offset (double): offset of the origin
        
        
        """
        ...
    def toSpace(self, point: org.hipparchus.geometry.euclidean.oned.Vector1D) -> 'Vector2D':
        """
        Transform a sub-space point into a space point.
        
        Specified by: toSpace in interface Embedding
        
        Parameters:
            point (Vector1D): (n-1)-dimension point of the sub-space
        
        Returns:
            n-dimension point of the space corresponding to the specified sub-space point
        
        Also see:
            toSubSpace
        
        
        """
        ...
    def toSubSpace(self, point: 'Vector2D') -> org.hipparchus.geometry.euclidean.oned.Vector1D:
        """
        Transform a space point into a sub-space point.
        
        Specified by: toSubSpace in interface Embedding
        
        Parameters:
            point (Vector2D): n-dimension point of the space
        
        Returns:
            (n-1)-dimension point of the sub-space corresponding to the specified space point
        
        Also see:
            toSpace
        
        
        """
        ...
    def translateToPoint(self, p: 'Vector2D') -> None:
        """
        Translate the line to force it passing by a point.
        
        Parameters:
            p (Vector2D): point by which the line should pass
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubLine':
        """
        Build a sub-hyperplane covering the whole hyperplane.
        
        Specified by: wholeHyperplane in interface Hyperplane
        
        Returns:
            a sub-hyperplane covering the whole hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> 'PolygonsSet':
        """
        Build a region covering the whole space.
        
        Specified by: wholeSpace in interface Hyperplane
        
        Returns:
            a region containing the instance (really a PolygonsSet instance)
        
        
        """
        ...

class PolygonsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Euclidean2D, 'Vector2D', Line, 'SubLine', org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D, org.hipparchus.geometry.euclidean.oned.OrientedPoint, org.hipparchus.geometry.euclidean.oned.SubOrientedPoint]):
    """
    This class represents a 2D region: a set of polygons.
    """
    @typing.overload
    def __init__(self, tolerance: float): ...
    @typing.overload
    def __init__(self, xMin: float, xMax: float, yMin: float, yMax: float, tolerance: float): ...
    @typing.overload
    def __init__(self, double: float, *vector2D: 'Vector2D'): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection['SubLine'], typing.Sequence['SubLine'], typing.Set['SubLine']], double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean2D, 'Vector2D', Line, 'SubLine'], double: float): ...
    def buildNew(self, tree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean2D, 'Vector2D', Line, 'SubLine']) -> 'PolygonsSet':
        """
        Build a region using the instance as a prototype.
        
        This method allow to create new instances without knowing exactly the type of the region. It is an application of the prototype design pattern.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Specified by: buildNew in interface Region
        
        Specified by: buildNew in class AbstractRegion
        
        Parameters:
            tree (BSPTree<Euclidean2D, Vector2D, Line, SubLine> tree): inside/outside BSP tree representing the new region
        
        Returns:
            the built region
        
        
        """
        ...
    def getInteriorPoint(self) -> 'Vector2D':
        """
        Get an interior point.
        
        Returns:
            an arbitrary interior point, or null if region is empty
        
        
        """
        ...
    def getVertices(self) -> typing.MutableSequence[typing.MutableSequence['Vector2D']]:
        """
        Get the vertices of the polygon.
        
        The polygon boundary can be represented as an array of loops, each loop being itself an array of vertices.
        
        In order to identify open loops which start and end by infinite edges, the open loops arrays start with a null point. In this case, the first non null point and the last point of the array do not represent real vertices, they are dummy points intended only to get the direction of the first and last edge. An open loop consisting of a single infinite line will therefore be represented by a three elements array with one null point followed by two dummy points. The open loops are always the first ones in the loops array.
        
        If the polygon has no boundary at all, a zero length loop array will be returned.
        
        All line segments in the various loops have the inside of the region on their left side and the outside on their right side when moving in the underlying line direction. This means that closed loops surrounding finite areas obey the direct trigonometric orientation.
        
        Returns:
            vertices of the polygon, organized as oriented boundary loops with the open loops first (the returned value is
            guaranteed to be non-null)
        
        
        """
        ...

class Segment:
    """
    Simple container for a two-points segment.
    """
    @typing.overload
    def __init__(self, vector2D: 'Vector2D', vector2D2: 'Vector2D', double: float): ...
    @typing.overload
    def __init__(self, vector2D: 'Vector2D', vector2D2: 'Vector2D', line: Line): ...
    def distance(self, p: 'Vector2D') -> float:
        """
        Calculates the shortest distance from a point to this line segment.
        
        If the perpendicular extension from the point to the line does not cross in the bounds of the line segment, the shortest distance to the two end points will be returned. Algorithm adapted from: ` Thread @ Codeguru <http://www.codeguru.com/forum/printthread.php?s=cc8cf0596231f9a7dba4da6e77c29db3&amp;t=194400&amp;pp=15&amp;page=1>`
        
        Parameters:
            p (Vector2D): to check
        
        Returns:
            distance between the instance and the point
        
        
        """
        ...
    def getEnd(self) -> 'Vector2D':
        """
        Get the end point of the segment.
        
        Returns:
            end point of the segment
        
        
        """
        ...
    def getLength(self) -> float:
        """
        Get the length of the line segment.
        
        Returns:
            line segment length.
        
        
        """
        ...
    def getLine(self) -> Line:
        """
        Get the line containing the segment.
        
        Returns:
            line containing the segment
        
        
        """
        ...
    def getStart(self) -> 'Vector2D':
        """
        Get the start point of the segment.
        
        Returns:
            start point of the segment
        
        
        """
        ...

class SubLine(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Euclidean2D, 'Vector2D', Line, 'SubLine', org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D, org.hipparchus.geometry.euclidean.oned.OrientedPoint, org.hipparchus.geometry.euclidean.oned.SubOrientedPoint]):
    """
    This class represents a sub-hyperplane for Line.
    """
    @typing.overload
    def __init__(self, hyperplane: Line, remainingRegion: org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D, org.hipparchus.geometry.euclidean.oned.OrientedPoint, org.hipparchus.geometry.euclidean.oned.SubOrientedPoint]): ...
    @typing.overload
    def __init__(self, segment: Segment): ...
    @typing.overload
    def __init__(self, start: 'Vector2D', end: 'Vector2D', tolerance: float): ...
    def getInteriorPoint(self) -> 'Vector2D':
        """
        Get an interior point.
        
        Returns:
            an arbitrary interior point, or null if sub-hyperplane is empty
        
        
        """
        ...
    def getSegments(self) -> java.util.List[Segment]:
        """
        Get the endpoints of the sub-line.
        
        A subline may be any arbitrary number of disjoints segments, so the endpoints are provided as a list of endpoint pairs. Each element of the list represents one segment, and each segment contains a start point at index 0 and an end point at index 1. If the sub-line is unbounded in the negative infinity direction, the start point of the first segment will have infinite coordinates. If the sub-line is unbounded in the positive infinity direction, the end point of the last segment will have infinite coordinates. So a sub-line covering the whole line will contain just one row and both elements of this row will have infinite coordinates. If the sub-line is empty, the returned list will contain 0 segments.
        
        Returns:
            list of segments endpoints
        
        
        """
        ...
    def intersection(self, subLine: 'SubLine', includeEndPoints: bool) -> 'Vector2D':
        """
        Get the intersection of the instance and another sub-line.
        
        This method is related to the intersection method in the Line class, but in addition to compute the point along infinite lines, it also checks the point lies on both sub-line ranges.
        
        Parameters:
            subLine (SubLine): other sub-line which may intersect instance
            includeEndPoints (boolean): if true, endpoints are considered to belong to instance (i.e. they are closed sets) and may be returned, otherwise
                endpoints are considered to not belong to instance (i.e. they are open sets) and intersection occurring on endpoints
                lead to null being returned
        
        Returns:
            the intersection point if there is one, null if the sub-lines don't intersect
        
        
        """
        ...
    def split(self, hyperplane: Line) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean2D, 'Vector2D', Line, 'SubLine']:
        """
        Split the instance in two parts by an hyperplane.
        
        Specified by: split in interface SubHyperplane
        
        Specified by: split in class AbstractSubHyperplane
        
        Parameters:
            hyperplane (Line): splitting hyperplane
        
        Returns:
            an object containing both the part of the instance on the plus side of the hyperplane and the part of the instance on
            the minus side of the hyperplane
        
        
        """
        ...

class Vector2D(org.hipparchus.geometry.Vector[Euclidean2D, 'Vector2D']):
    """
    This class represents a 2D vector.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        serialized
    """
    ZERO: typing.ClassVar['Vector2D'] = ...
    """
    Origin (coordinates: 0, 0).
    """
    PLUS_I: typing.ClassVar['Vector2D'] = ...
    """
    First canonical vector (coordinates: 1, 0).
    
    Since:
        1.6
    
    
    """
    MINUS_I: typing.ClassVar['Vector2D'] = ...
    """
    Opposite of the first canonical vector (coordinates: -1, 0).
    
    Since:
        1.6
    
    
    """
    PLUS_J: typing.ClassVar['Vector2D'] = ...
    """
    Second canonical vector (coordinates: 0, 1).
    
    Since:
        1.6
    
    
    """
    MINUS_J: typing.ClassVar['Vector2D'] = ...
    """
    Opposite of the second canonical vector (coordinates: 0, -1).
    
    Since:
        1.6
    
    
    """
    NaN: typing.ClassVar['Vector2D'] = ...
    """
    A vector with all coordinates set to NaN.
    """
    POSITIVE_INFINITY: typing.ClassVar['Vector2D'] = ...
    """
    A vector with all coordinates set to positive infinity.
    """
    NEGATIVE_INFINITY: typing.ClassVar['Vector2D'] = ...
    """
    A vector with all coordinates set to negative infinity.
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, vector2D: 'Vector2D'): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'Vector2D', a2: float, u2: 'Vector2D'): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'Vector2D', a2: float, u2: 'Vector2D', a3: float, u3: 'Vector2D'): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'Vector2D', a2: float, u2: 'Vector2D', a3: float, u3: 'Vector2D', a4: float, u4: 'Vector2D'): ...
    @typing.overload
    def __init__(self, v: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def add(self, factor: float, v: 'Vector2D') -> 'Vector2D':
        """
        Add a scaled vector to the instance.
        
        Specified by: add in interface Vector
        
        Parameters:
            factor (double): scale factor to apply to v before adding it
            v (Vector2D): vector to add
        
        Returns:
            a new vector
        
        
        """
        ...
    @typing.overload
    def add(self, v: 'Vector2D') -> 'Vector2D':
        """
        Add a vector to the instance.
        
        Specified by: add in interface Vector
        
        Parameters:
            v (Vector2D): vector to add
        
        Returns:
            a new vector
        
        """
        ...
    @staticmethod
    def angle(v1: 'Vector2D', v2: 'Vector2D') -> float:
        """
        Compute the angular separation between two vectors.
        
        This method computes the angular separation between two vectors using the dot product for well separated vectors and the cross product for almost aligned vectors. This allows to have a good accuracy in all cases, even for vectors very close to each other.
        
        Parameters:
            v1 (Vector2D): first vector
            v2 (Vector2D): second vector
        
        Returns:
            angular separation between v1 and v2
        
        Raises:
            hipparchus: if either vector has a null norm
        
        
        """
        ...
    def crossProduct(self, p1: 'Vector2D', p2: 'Vector2D') -> float:
        """
        Compute the cross-product of the instance and the given points.
        
        The cross product can be used to determine the location of a point with regard to the line formed by (p1, p2) and is calculated as: \[ P = (x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) \] with \(p3 = (x_3, y_3)\) being this instance.
        
        If the result is 0, the points are collinear, i.e. lie on a single straight line L; if it is positive, this point lies to the left, otherwise to the right of the line formed by (p1, p2).
        
        Parameters:
            p1 (Vector2D): first point of the line
            p2 (Vector2D): second point of the line
        
        Returns:
            the cross-product
        
        Also see:
            `Cross product (Wikipedia) <http://en.wikipedia.org/wiki/Cross_product>`
        
        
        """
        ...
    @typing.overload
    def distance(self, p: 'Vector2D') -> float:
        """
        Compute the distance between the instance and another point.
        
        Specified by: distance in interface Point
        
        Parameters:
            p (Vector2D): second point
        
        Returns:
            the distance between the instance and p
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(p1: 'Vector2D', p2: 'Vector2D') -> float: ...
    @typing.overload
    def distance1(self, p: 'Vector2D') -> float:
        """
        Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Specified by: distance1 in interface Vector
        
        Parameters:
            p (Vector2D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`1` norm
        
        Compute the distance between two vectors according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`1` norm
        
        Since:
            1.6
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(p1: 'Vector2D', p2: 'Vector2D') -> float: ...
    @typing.overload
    def distanceInf(self, p: 'Vector2D') -> float:
        """
        Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Specified by: distanceInf in interface Vector
        
        Parameters:
            p (Vector2D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`∞` norm
        
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the distance between p1 and p2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(p1: 'Vector2D', p2: 'Vector2D') -> float: ...
    @typing.overload
    def distanceSq(self, p: 'Vector2D') -> float:
        """
        Compute the square of the distance between the instance and another vector.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Specified by: distanceSq in interface Vector
        
        Parameters:
            p (Vector2D): second vector
        
        Returns:
            the square of the distance between the instance and p
        
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            p1 (Vector2D): first vector
            p2 (Vector2D): second vector
        
        Returns:
            the square of the distance between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(p1: 'Vector2D', p2: 'Vector2D') -> float: ...
    def dotProduct(self, v: 'Vector2D') -> float:
        """
        Compute the dot-product of the instance and another vector.
        
        Specified by: dotProduct in interface Vector
        
        Parameters:
            v (Vector2D): second vector
        
        Returns:
            the dot product this.v
        
        
        """
        ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 2D vectors.
        
        If all coordinates of two 2D vectors are exactly the same, and none are NaN, the two 2D vectors are considered to be equal.
        
        NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) coordinates of the 2D vector are equal to NaN, the 2D vector is equal to NaN.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 2D vector objects are equal, false if object is null, not an instance of Vector2D, or not equal to this
            Vector2D instance
        
        
        """
        ...
    def equalsIeee754(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 2D vectors.
        
        If all coordinates of two 2D vectors are exactly the same, and none are NaN, the two 2D vectors are considered to be equal.
        
        In compliance with IEEE754 handling, if any coordinates of any of the two vectors are NaN, then the vectors are considered different. This implies that NaN.equals(NaN) returns false despite the instance is checked against itself.
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 2D vector objects are equal, false if object is null, not an instance of Vector2D, or not equal to this
            Vector2D instance
        
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
        
        
        """
        ...
    def getY(self) -> float:
        """
        Get the ordinate of the vector.
        
        Returns:
            ordinate of the vector
        
        
        """
        ...
    def getZero(self) -> 'Vector2D':
        """
        Get the null vector of the vectorial space or origin point of the affine space.
        
        Specified by: getZero in interface Vector
        
        Returns:
            null vector of the vectorial space or origin point of the affine space
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the 2D vector.
        
        All NaN values have the same hash code.
        
        Overrides: Object in class Object
        
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
    def moveTowards(self, other: 'Vector2D', ratio: float) -> 'Vector2D':
        """
        Move towards another point.
        
        Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
        Specified by: moveTowards in interface Point
        
        Parameters:
            other (Vector2D): other point
            ratio (double): motion ratio,
        
        Returns:
            moved point
        
        
        """
        ...
    def negate(self) -> 'Vector2D':
        """
        Get the opposite of the instance.
        
        Specified by: negate in interface Vector
        
        Returns:
            a new vector which is opposite to the instance
        
        
        """
        ...
    @staticmethod
    def orientation(p: 'Vector2D', q: 'Vector2D', r: 'Vector2D') -> float:
        """
        Compute the orientation of a triplet of points.
        
        Parameters:
            p (Vector2D): first vector of the triplet
            q (Vector2D): second vector of the triplet
            r (Vector2D): third vector of the triplet
        
        Returns:
            a positive value if (p, q, r) defines a counterclockwise oriented triangle, a negative value if (p, q, r) defines a
            clockwise oriented triangle, and 0 if (p, q, r) are collinear or some points are equal
        
        Since:
            1.2
        
        
        """
        ...
    def scalarMultiply(self, a: float) -> 'Vector2D':
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
    def subtract(self, factor: float, v: 'Vector2D') -> 'Vector2D':
        """
        Subtract a scaled vector from the instance.
        
        Specified by: subtract in interface Vector
        
        Parameters:
            factor (double): scale factor to apply to v before subtracting it
            v (Vector2D): vector to subtract
        
        Returns:
            a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, p: 'Vector2D') -> 'Vector2D':
        """
        Subtract a vector from the instance.
        
        Specified by: subtract in interface Vector
        
        Parameters:
            p (Vector2D): vector to subtract
        
        Returns:
            a new vector
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Get the vector coordinates as a dimension 2 array.
        
        Returns:
            vector coordinates
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
        Get a string representation of this vector.
        
        Overrides: Object in class Object
        
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

class Vector2DFormat(org.hipparchus.geometry.VectorFormat[Euclidean2D, Vector2D]):
    """
    Formats a 2D vector in components list format "{x; y}".
    
    The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format for components can be configured.
    
    White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the default separator does include a space character that is used at format time, both input string "{1;1}" and " { 1 ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
    Note: using "," as a separator may interfere with the grouping separator of the default NumberFormat for the current locale. Thus it is advised to use a NumberFormat instance with disabled grouping in such a case.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, prefix: str, suffix: str, separator: str): ...
    @typing.overload
    def __init__(self, prefix: str, suffix: str, separator: str, format: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, format: java.text.NumberFormat): ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[org.hipparchus.geometry.Space, org.hipparchus.geometry.Vector]) -> str: ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[Euclidean2D, Vector2D], toAppendTo: java.lang.StringBuffer, pos: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def getVector2DFormat() -> 'Vector2DFormat':
        """
        Returns:
            the default 2D vector format.
        
        Since:
            1.4
        
        """
        ...
    @typing.overload
    @staticmethod
    def getVector2DFormat(locale: java.util.Locale) -> 'Vector2DFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the 2D vector format specific to the given locale.
        
        Since:
            1.4
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str) -> Vector2D:
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
    def parse(self, source: str, pos: java.text.ParsePosition) -> Vector2D: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.twod")``.

    DiskGenerator: typing.Type[DiskGenerator]
    Euclidean2D: typing.Type[Euclidean2D]
    FieldVector2D: typing.Type[FieldVector2D]
    Line: typing.Type[Line]
    PolygonsSet: typing.Type[PolygonsSet]
    Segment: typing.Type[Segment]
    SubLine: typing.Type[SubLine]
    Vector2D: typing.Type[Vector2D]
    Vector2DFormat: typing.Type[Vector2DFormat]
    hull: org.hipparchus.geometry.euclidean.twod.hull.__module_protocol__
