
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
    public classDiskGenerator extends :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.enclosing.SupportBallGenerator`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`>
    
        Class generating an enclosing ball from its support points.
    """
    def __init__(self): ...
    def ballOnSupport(self, list: java.util.List['Vector2D']) -> org.hipparchus.geometry.enclosing.EnclosingBall['Euclidean2D', 'Vector2D']: ...

class Euclidean2D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    public classEuclidean2D extends :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`, :class:`~org.hipparchus.geometry.Space`
    
        This class implements a two-dimensional space.
    
        Also see:
    
              - :meth:`~serialized`
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
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Space.getSubSpace` in interface :class:`~org.hipparchus.geometry.Space`
        
            Returns:
                n-1 dimension sub-space of this space
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.Space.getDimension`
        
        
        
        """
        ...

_FieldVector2D__T = typing.TypeVar('_FieldVector2D__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldVector2D(typing.Generic[_FieldVector2D__T]):
    """
    public classFieldVector2D<T extends :class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This class is a re-implementation of :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` using
        :class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            1.6
    """
    @typing.overload
    def __init__(self, double: float, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T], double2: float, fieldVector2D2: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T], double2: float, fieldVector2D2: 'FieldVector2D'[_FieldVector2D__T], double3: float, fieldVector2D3: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T], double2: float, fieldVector2D2: 'FieldVector2D'[_FieldVector2D__T], double3: float, fieldVector2D3: 'FieldVector2D'[_FieldVector2D__T], double4: float, fieldVector2D4: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, t2: _FieldVector2D__T): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T], t2: _FieldVector2D__T, fieldVector2D2: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T], t2: _FieldVector2D__T, fieldVector2D2: 'FieldVector2D'[_FieldVector2D__T], t3: _FieldVector2D__T, fieldVector2D3: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T], t2: _FieldVector2D__T, fieldVector2D2: 'FieldVector2D'[_FieldVector2D__T], t3: _FieldVector2D__T, fieldVector2D3: 'FieldVector2D'[_FieldVector2D__T], t4: _FieldVector2D__T, fieldVector2D4: 'FieldVector2D'[_FieldVector2D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, vector2D: 'Vector2D'): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, vector2D: 'Vector2D', t2: _FieldVector2D__T, vector2D2: 'Vector2D'): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, vector2D: 'Vector2D', t2: _FieldVector2D__T, vector2D2: 'Vector2D', t3: _FieldVector2D__T, vector2D3: 'Vector2D'): ...
    @typing.overload
    def __init__(self, t: _FieldVector2D__T, vector2D: 'Vector2D', t2: _FieldVector2D__T, vector2D2: 'Vector2D', t3: _FieldVector2D__T, vector2D3: 'Vector2D', t4: _FieldVector2D__T, vector2D4: 'Vector2D'): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_FieldVector2D__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldVector2D__T], vector2D: 'Vector2D'): ...
    @typing.overload
    def add(self, double: float, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, double: float, vector2D: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, t: _FieldVector2D__T, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, t: _FieldVector2D__T, vector2D: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def add(self, vector2D: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    _angle_0__T = typing.TypeVar('_angle_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _angle_1__T = typing.TypeVar('_angle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _angle_2__T = typing.TypeVar('_angle_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def angle(fieldVector2D: 'FieldVector2D'[_angle_0__T], fieldVector2D2: 'FieldVector2D'[_angle_0__T]) -> _angle_0__T: ...
    @typing.overload
    @staticmethod
    def angle(fieldVector2D: 'FieldVector2D'[_angle_1__T], vector2D: 'Vector2D') -> _angle_1__T: ...
    @typing.overload
    @staticmethod
    def angle(vector2D: 'Vector2D', fieldVector2D: 'FieldVector2D'[_angle_2__T]) -> _angle_2__T: ...
    @typing.overload
    def crossProduct(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T], fieldVector2D2: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
            Compute the cross-product of the instance and the given points.
        
            The cross product can be used to determine the location of a point with regard to the line formed by (p1, p2) and is
            calculated as: \[ P = (x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) \] with \(p3 = (x_3, y_3)\) being this instance.
        
            If the result is 0, the points are collinear, i.e. lie on a single straight line L; if it is positive, this point lies
            to the left, otherwise to the right of the line formed by (p1, p2).
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first point of the line
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second point of the line
        
            Returns:
                the cross-product
        
            Also see:
        
                  - `Cross product (Wikipedia) <http://en.wikipedia.org/wiki/Cross_product>`
        
        
        
        """
        ...
    @typing.overload
    def crossProduct(self, vector2D: 'Vector2D', vector2D2: 'Vector2D') -> _FieldVector2D__T: ...
    _distance_2__T = typing.TypeVar('_distance_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance_3__T = typing.TypeVar('_distance_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance_4__T = typing.TypeVar('_distance_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distance(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
            Compute the distance between the instance and another vector according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`2` norm
        
        """
        ...
    @typing.overload
    def distance(self, vector2D: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distance(fieldVector2D: 'FieldVector2D'[_distance_2__T], fieldVector2D2: 'FieldVector2D'[_distance_2__T]) -> _distance_2__T:
        """
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(fieldVector2D: 'FieldVector2D'[_distance_3__T], vector2D: 'Vector2D') -> _distance_3__T: ...
    @typing.overload
    @staticmethod
    def distance(vector2D: 'Vector2D', fieldVector2D: 'FieldVector2D'[_distance_4__T]) -> _distance_4__T: ...
    _distance1_2__T = typing.TypeVar('_distance1_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance1_3__T = typing.TypeVar('_distance1_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance1_4__T = typing.TypeVar('_distance1_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distance1(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
            Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`1` norm
        
        """
        ...
    @typing.overload
    def distance1(self, vector2D: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distance1(fieldVector2D: 'FieldVector2D'[_distance1_2__T], fieldVector2D2: 'FieldVector2D'[_distance1_2__T]) -> _distance1_2__T:
        """
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(fieldVector2D: 'FieldVector2D'[_distance1_3__T], vector2D: 'Vector2D') -> _distance1_3__T: ...
    @typing.overload
    @staticmethod
    def distance1(vector2D: 'Vector2D', fieldVector2D: 'FieldVector2D'[_distance1_4__T]) -> _distance1_4__T: ...
    _distanceInf_2__T = typing.TypeVar('_distanceInf_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceInf_3__T = typing.TypeVar('_distanceInf_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceInf_4__T = typing.TypeVar('_distanceInf_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distanceInf(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
            Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`∞` norm
        
        """
        ...
    @typing.overload
    def distanceInf(self, vector2D: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(fieldVector2D: 'FieldVector2D'[_distanceInf_2__T], fieldVector2D2: 'FieldVector2D'[_distanceInf_2__T]) -> _distanceInf_2__T:
        """
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`∞` norm
        
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`∞` norm
        
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(fieldVector2D: 'FieldVector2D'[_distanceInf_3__T], vector2D: 'Vector2D') -> _distanceInf_3__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(vector2D: 'Vector2D', fieldVector2D: 'FieldVector2D'[_distanceInf_4__T]) -> _distanceInf_4__T: ...
    _distanceSq_2__T = typing.TypeVar('_distanceSq_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceSq_3__T = typing.TypeVar('_distanceSq_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceSq_4__T = typing.TypeVar('_distanceSq_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distanceSq(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
            Compute the square of the distance between the instance and another vector.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the square of the distance between the instance and p
        
        """
        ...
    @typing.overload
    def distanceSq(self, vector2D: 'Vector2D') -> _FieldVector2D__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(fieldVector2D: 'FieldVector2D'[_distanceSq_2__T], fieldVector2D2: 'FieldVector2D'[_distanceSq_2__T]) -> _distanceSq_2__T:
        """
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the square of the distance between p1 and p2
        
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p1): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the square of the distance between p1 and p2
        
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p2): second vector
        
            Returns:
                the square of the distance between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(fieldVector2D: 'FieldVector2D'[_distanceSq_3__T], vector2D: 'Vector2D') -> _distanceSq_3__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(vector2D: 'Vector2D', fieldVector2D: 'FieldVector2D'[_distanceSq_4__T]) -> _distanceSq_4__T: ...
    @typing.overload
    def dotProduct(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> _FieldVector2D__T:
        """
            Compute the dot-product of the instance and another vector.
        
            The implementation uses specific multiplication and addition algorithms to preserve accuracy and reduce cancellation
            effects. It should be very accurate even for nearly orthogonal vectors.
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the dot product this.v
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`
        
        
        
        """
        ...
    @typing.overload
    def dotProduct(self, vector2D: 'Vector2D') -> _FieldVector2D__T: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 2D vectors.
        
            If all coordinates of two 2D vectors are exactly the same, and none of their
            :meth:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus` are :code:`NaN`, the two 2D vectors
            are considered to be equal.
        
            :code:`NaN` coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or
            all) real part of the coordinates of the 3D vector are :code:`NaN`, the 2D vector is :code:`NaN`.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality to this
        
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
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
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
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
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
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
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
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
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
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
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
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
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
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
            Returns:
                a new vector
        
        
        """
        ...
    def getX(self) -> _FieldVector2D__T:
        """
            Get the abscissa of the vector.
        
            Returns:
                abscissa of the vector
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D.%3Cinit%3E`
        
        
        
        """
        ...
    def getY(self) -> _FieldVector2D__T:
        """
            Get the ordinate of the vector.
        
            Returns:
                ordinate of the vector
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D.%3Cinit%3E`
        
        
        
        """
        ...
    _getZero__T = typing.TypeVar('_getZero__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getZero(field: org.hipparchus.Field[_getZero__T]) -> 'FieldVector2D'[_getZero__T]:
        """
            Get null vector (coordinates: 0, 0).
        
            Parameters:
                field (:class:`~org.hipparchus.geometry.euclidean.twod.https:.www.hipparchus.org.hipparchus`<T> field): field for the components
        
            Returns:
                a new vector
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the 3D vector.
        
            All NaN values have the same hash code.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
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
    def negate(self) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    def normalize(self) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    _orientation__T = typing.TypeVar('_orientation__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def orientation(fieldVector2D: 'FieldVector2D'[_orientation__T], fieldVector2D2: 'FieldVector2D'[_orientation__T], fieldVector2D3: 'FieldVector2D'[_orientation__T]) -> _orientation__T:
        """
            Compute the orientation of a triplet of points.
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> p): first vector of the triplet
                q (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> q): second vector of the triplet
                r (:class:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D`<T> r): third vector of the triplet
        
            Returns:
                a positive value if (p, q, r) defines a counterclockwise oriented triangle, a negative value if (p, q, r) defines a
                clockwise oriented triangle, and 0 if (p, q, r) are collinear or some points are equal
        
            Since:
                1.2
        
        
        """
        ...
    @typing.overload
    def scalarMultiply(self, double: float) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def scalarMultiply(self, t: _FieldVector2D__T) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, double: float, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, double: float, vector2D: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, t: _FieldVector2D__T, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, t: _FieldVector2D__T, vector2D: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, fieldVector2D: 'FieldVector2D'[_FieldVector2D__T]) -> 'FieldVector2D'[_FieldVector2D__T]: ...
    @typing.overload
    def subtract(self, vector2D: 'Vector2D') -> 'FieldVector2D'[_FieldVector2D__T]: ...
    def toArray(self) -> typing.MutableSequence[_FieldVector2D__T]:
        """
            Get the vector coordinates as a dimension 2 array.
        
            Returns:
                vector coordinates
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.euclidean.twod.FieldVector2D.%3Cinit%3E`
        
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a string representation of this vector.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a string representation of this vector
        
        """
        ...
    @typing.overload
    def toString(self, numberFormat: java.text.NumberFormat) -> str:
        """
            Get a string representation of this vector.
        
            Parameters:
                format (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`): the custom format for components
        
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
    public classLine extends :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Line`,:class:`~org.hipparchus.geometry.euclidean.twod.SubLine`>, :class:`~org.hipparchus.geometry.partitioning.Embedding`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`,:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`,:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`>
    
        This class represents an oriented line in the 2D plane.
    
        An oriented line can be defined either by prolongating a line segment between two points past these points, or by one
        point and an angular direction (in trigonometric orientation).
    
        Since it is oriented the two half planes at its two sides are unambiguously identified as a left half plane and a right
        half plane. This can be used to identify the interior and the exterior in a simple way by local properties only when
        part of a line is used to define part of a polygon boundary.
    
        A line can also be used to completely define a reference frame in the plane. It is sufficient to select one specific
        point in the line (the orthogonal projection of the original reference frame on the line) and to use the unit vector in
        the line direction and the orthogonal vector oriented from left half plane to right half plane. We define two
        coordinates by the process, the *abscissa* along the line, and the *offset* across the line. All points of the plane are
        uniquely identified by these two coordinates. The line is the set of points at zero offset, the left half plane is the
        set of points with negative offsets and the right half plane is the set of points with positive offsets.
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
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.arbitraryPoint` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                arbirary point in the hyperplane
        
        
        """
        ...
    def contains(self, vector2D: 'Vector2D') -> bool:
        """
            Check if the line contains a point.
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): point to check
        
            Returns:
                true if p belongs to the line
        
        
        """
        ...
    def copySelf(self) -> 'Line':
        """
            Copy the instance.
        
            The instance created is completely independent of the original one. A deep copy is used, none of the underlying objects
            are shared (except for immutable objects).
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.copySelf` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a new hyperplane, copy of the instance
        
        
        """
        ...
    def distance(self, vector2D: 'Vector2D') -> float:
        """
            Compute the distance between the instance and a point.
        
            This is a shortcut for invoking FastMath.abs(getOffset(p)), and provides consistency with what is in the
            org.hipparchus.geometry.euclidean.threed.Line class.
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): to check
        
            Returns:
                distance between the instance and the point
        
        
        """
        ...
    def emptyHyperplane(self) -> 'SubLine':
        """
            Build a sub-hyperplane covering nothing.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.emptyHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
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
            Get the offset (oriented distance) of a parallel line.
        
            This method should be called only for parallel lines otherwise the result is not meaningful.
        
            The offset is 0 if both lines are the same, it is positive if the line is on the right side of the instance and negative
            if it is on the left side, according to its natural orientation.
        
            Parameters:
                line (:class:`~org.hipparchus.geometry.euclidean.twod.Line`): line to check
        
            Returns:
                offset of the line
        
            Get the offset (oriented distance) of a point.
        
            The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of
            the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.getOffset` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): point to check
        
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
    def getPointAt(self, vector1D: org.hipparchus.geometry.euclidean.oned.Vector1D, double: float) -> 'Vector2D':
        """
            Get one point from the plane.
        
            Parameters:
                abscissa (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): desired abscissa for the point
                offset (double): desired offset for the point
        
            Returns:
                one point in the plane, with given abscissa and offset relative to the line
        
        
        """
        ...
    def getReverse(self) -> 'Line':
        """
            Get the reverse of the instance.
        
            Get a line with reversed orientation with respect to the instance.
        
            As long as neither the instance nor its reverse are modified (i.e. as long as none of the
            :meth:`~org.hipparchus.geometry.euclidean.twod.Line.reset`, :meth:`~org.hipparchus.geometry.euclidean.twod.Line.reset`,
            :meth:`~org.hipparchus.geometry.euclidean.twod.Line.revertSelf`,
            :meth:`~org.hipparchus.geometry.euclidean.twod.Line.setAngle` or
            :meth:`~org.hipparchus.geometry.euclidean.twod.Line.setOriginOffset` methods are called), then the line and its reverse
            remain linked together so that :code:`line.getReverse().getReverse() == line`. When one of the line is modified, the
            link is deleted as both instance becomes independent.
        
            Returns:
                a new line, with orientation opposite to the instance orientation
        
        
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
    @staticmethod
    def getTransform(double: float, double2: float, double3: float, double4: float, double5: float, double6: float) -> org.hipparchus.geometry.partitioning.Transform[Euclidean2D, 'Vector2D', 'Line', 'SubLine', org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D, org.hipparchus.geometry.euclidean.oned.OrientedPoint, org.hipparchus.geometry.euclidean.oned.SubOrientedPoint]: ...
    def intersection(self, line: 'Line') -> 'Vector2D':
        """
            Get the intersection point of the instance and another line.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.twod.Line`): other line
        
            Returns:
                intersection point of the instance and the other line or null if there are no intersection points
        
        
        """
        ...
    def isParallelTo(self, line: 'Line') -> bool:
        """
            Check the instance is parallel to another line.
        
            Parameters:
                line (:class:`~org.hipparchus.geometry.euclidean.twod.Line`): other line to check
        
            Returns:
                true if the instance is parallel to the other line (they can have either the same or opposite orientations)
        
        
        """
        ...
    def moveToOffset(self, vector2D: 'Vector2D', double: float) -> 'Vector2D':
        """
            Move point up to specified offset.
        
            Motion is *orthogonal* to the hyperplane
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.moveToOffset` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): point to move
                offset (double): desired offset
        
            Returns:
                moved point at desired offset
        
        
        """
        ...
    def project(self, vector2D: 'Vector2D') -> 'Vector2D':
        """
            Project a point to the hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.project` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): point to project
        
            Returns:
                projected point
        
        
        """
        ...
    @typing.overload
    def reset(self, vector2D: 'Vector2D', double: float) -> None:
        """
            Reset the instance as if built from two points.
        
            The line is oriented from p1 to p2
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first point
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second point
        
            Reset the instance as if built from a line and an angle.
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): point belonging to the line
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
    def sameOrientationAs(self, line: 'Line') -> bool:
        """
            Check if the instance has the same orientation as another hyperplane.
        
            This method is expected to be called on parallel hyperplanes. The method should *not* re-check for parallelism, only for
            orientation, typically by testing something like the sign of the dot-products of normals.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.sameOrientationAs` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.twod.Line`): other hyperplane to check against the instance
        
            Returns:
                true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def setAngle(self, double: float) -> None:
        """
            Set the angle of the line.
        
            Parameters:
                angle (double): new angle of the line with respect to the abscissa axis
        
        
        """
        ...
    def setOriginOffset(self, double: float) -> None:
        """
            Set the offset of the origin.
        
            Parameters:
                offset (double): offset of the origin
        
        
        """
        ...
    def toSpace(self, vector1D: org.hipparchus.geometry.euclidean.oned.Vector1D) -> 'Vector2D':
        """
            Transform a sub-space point into a space point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Embedding`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`): (n-1)-dimension point of the sub-space
        
            Returns:
                n-dimension point of the space corresponding to the specified sub-space point
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSubSpace`
        
        
        
        """
        ...
    def toSubSpace(self, vector2D: 'Vector2D') -> org.hipparchus.geometry.euclidean.oned.Vector1D:
        """
            Transform a space point into a sub-space point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSubSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Embedding`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): n-dimension point of the space
        
            Returns:
                (n-1)-dimension point of the sub-space corresponding to the specified space point
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSpace`
        
        
        
        """
        ...
    def translateToPoint(self, vector2D: 'Vector2D') -> None:
        """
            Translate the line to force it passing by a point.
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): point by which the line should pass
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubLine':
        """
            Build a sub-hyperplane covering the whole hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.wholeHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a sub-hyperplane covering the whole hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> 'PolygonsSet':
        """
            Build a region covering the whole space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.wholeSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a region containing the instance (really a :class:`~org.hipparchus.geometry.euclidean.twod.PolygonsSet` instance)
        
        
        """
        ...

class PolygonsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Euclidean2D, 'Vector2D', Line, 'SubLine', org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D, org.hipparchus.geometry.euclidean.oned.OrientedPoint, org.hipparchus.geometry.euclidean.oned.SubOrientedPoint]):
    """
    public classPolygonsSet extends :class:`~org.hipparchus.geometry.partitioning.AbstractRegion`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Line`,:class:`~org.hipparchus.geometry.euclidean.twod.SubLine`,:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`,:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`,:class:`~org.hipparchus.geometry.euclidean.oned.OrientedPoint`,:class:`~org.hipparchus.geometry.euclidean.oned.SubOrientedPoint`>
    
        This class represents a 2D region: a set of polygons.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, double: float, *vector2D: 'Vector2D'): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection['SubLine'], typing.Sequence['SubLine'], typing.Set['SubLine']], double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean2D, 'Vector2D', Line, 'SubLine'], double: float): ...
    def buildNew(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean2D, 'Vector2D', Line, 'SubLine']) -> 'PolygonsSet': ...
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
        
            In order to identify open loops which start and end by infinite edges, the open loops arrays start with a null point. In
            this case, the first non null point and the last point of the array do not represent real vertices, they are dummy
            points intended only to get the direction of the first and last edge. An open loop consisting of a single infinite line
            will therefore be represented by a three elements array with one null point followed by two dummy points. The open loops
            are always the first ones in the loops array.
        
            If the polygon has no boundary at all, a zero length loop array will be returned.
        
            All line segments in the various loops have the inside of the region on their left side and the outside on their right
            side when moving in the underlying line direction. This means that closed loops surrounding finite areas obey the direct
            trigonometric orientation.
        
            Returns:
                vertices of the polygon, organized as oriented boundary loops with the open loops first (the returned value is
                guaranteed to be non-null)
        
        
        """
        ...

class Segment:
    """
    public classSegment extends :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Simple container for a two-points segment.
    """
    @typing.overload
    def __init__(self, vector2D: 'Vector2D', vector2D2: 'Vector2D', double: float): ...
    @typing.overload
    def __init__(self, vector2D: 'Vector2D', vector2D2: 'Vector2D', line: Line): ...
    def distance(self, vector2D: 'Vector2D') -> float:
        """
            Calculates the shortest distance from a point to this line segment.
        
            If the perpendicular extension from the point to the line does not cross in the bounds of the line segment, the shortest
            distance to the two end points will be returned.
            Algorithm adapted from: ` Thread @ Codeguru
            <http://www.codeguru.com/forum/printthread.php?s=cc8cf0596231f9a7dba4da6e77c29db3&amp;t=194400&amp;pp=15&amp;page=1>`
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): to check
        
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
    public classSubLine extends :class:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Line`,:class:`~org.hipparchus.geometry.euclidean.twod.SubLine`,:class:`~org.hipparchus.geometry.euclidean.oned.Euclidean1D`,:class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`,:class:`~org.hipparchus.geometry.euclidean.oned.OrientedPoint`,:class:`~org.hipparchus.geometry.euclidean.oned.SubOrientedPoint`>
    
        This class represents a sub-hyperplane for :class:`~org.hipparchus.geometry.euclidean.twod.Line`.
    """
    @typing.overload
    def __init__(self, line: Line, region: org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D, org.hipparchus.geometry.euclidean.oned.OrientedPoint, org.hipparchus.geometry.euclidean.oned.SubOrientedPoint]): ...
    @typing.overload
    def __init__(self, segment: Segment): ...
    @typing.overload
    def __init__(self, vector2D: 'Vector2D', vector2D2: 'Vector2D', double: float): ...
    def getInteriorPoint(self) -> 'Vector2D':
        """
            Get an interior point.
        
            Returns:
                an arbitrary interior point, or null if sub-hyperplane is empty
        
        
        """
        ...
    def getSegments(self) -> java.util.List[Segment]: ...
    def intersection(self, subLine: 'SubLine', boolean: bool) -> 'Vector2D':
        """
            Get the intersection of the instance and another sub-line.
        
            This method is related to the :meth:`~org.hipparchus.geometry.euclidean.twod.Line.intersection` method in the
            :class:`~org.hipparchus.geometry.euclidean.twod.Line` class, but in addition to compute the point along infinite lines,
            it also checks the point lies on both sub-line ranges.
        
            Parameters:
                subLine (:class:`~org.hipparchus.geometry.euclidean.twod.SubLine`): other sub-line which may intersect instance
                includeEndPoints (boolean): if true, endpoints are considered to belong to instance (i.e. they are closed sets) and may be returned, otherwise
                    endpoints are considered to not belong to instance (i.e. they are open sets) and intersection occurring on endpoints
                    lead to null being returned
        
            Returns:
                the intersection point if there is one, null if the sub-lines don't intersect
        
        
        """
        ...
    def split(self, line: Line) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean2D, 'Vector2D', Line, 'SubLine']: ...

class Vector2D(org.hipparchus.geometry.Vector[Euclidean2D, 'Vector2D']):
    """
    public classVector2D extends :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.Vector`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`>
    
        This class represents a 2D vector.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
    
              - :meth:`~serialized`
    """
    ZERO: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` ZERO
    
        Origin (coordinates: 0, 0).
    
    """
    PLUS_I: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` PLUS_I
    
        First canonical vector (coordinates: 1, 0).
    
        Since:
            1.6
    
    
    """
    MINUS_I: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` MINUS_I
    
        Opposite of the first canonical vector (coordinates: -1, 0).
    
        Since:
            1.6
    
    
    """
    PLUS_J: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` PLUS_J
    
        Second canonical vector (coordinates: 0, 1).
    
        Since:
            1.6
    
    
    """
    MINUS_J: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` MINUS_J
    
        Opposite of the second canonical vector (coordinates: 0, -1).
    
        Since:
            1.6
    
    
    """
    NaN: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` NaN
    
        A vector with all coordinates set to NaN.
    
    """
    POSITIVE_INFINITY: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` POSITIVE_INFINITY
    
        A vector with all coordinates set to positive infinity.
    
    """
    NEGATIVE_INFINITY: typing.ClassVar['Vector2D'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.euclidean.twod.Vector2D` NEGATIVE_INFINITY
    
        A vector with all coordinates set to negative infinity.
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, vector2D: 'Vector2D'): ...
    @typing.overload
    def __init__(self, double: float, vector2D: 'Vector2D', double2: float, vector2D2: 'Vector2D'): ...
    @typing.overload
    def __init__(self, double: float, vector2D: 'Vector2D', double2: float, vector2D2: 'Vector2D', double3: float, vector2D3: 'Vector2D'): ...
    @typing.overload
    def __init__(self, double: float, vector2D: 'Vector2D', double2: float, vector2D2: 'Vector2D', double3: float, vector2D3: 'Vector2D', double4: float, vector2D4: 'Vector2D'): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def add(self, double: float, vector2D: 'Vector2D') -> 'Vector2D':
        """
            Add a scaled vector to the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.add` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                factor (double): scale factor to apply to v before adding it
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): vector to add
        
            Returns:
                a new vector
        
        
        """
        ...
    @typing.overload
    def add(self, vector2D: 'Vector2D') -> 'Vector2D':
        """
            Add a vector to the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.add` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): vector to add
        
            Returns:
                a new vector
        
        """
        ...
    @staticmethod
    def angle(vector2D: 'Vector2D', vector2D2: 'Vector2D') -> float: ...
    def crossProduct(self, vector2D: 'Vector2D', vector2D2: 'Vector2D') -> float:
        """
            Compute the cross-product of the instance and the given points.
        
            The cross product can be used to determine the location of a point with regard to the line formed by (p1, p2) and is
            calculated as: \[ P = (x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) \] with \(p3 = (x_3, y_3)\) being this instance.
        
            If the result is 0, the points are collinear, i.e. lie on a single straight line L; if it is positive, this point lies
            to the left, otherwise to the right of the line formed by (p1, p2).
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first point of the line
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second point of the line
        
            Returns:
                the cross-product
        
            Also see:
        
                  - `Cross product (Wikipedia) <http://en.wikipedia.org/wiki/Cross_product>`
        
        
        
        """
        ...
    @typing.overload
    def distance(self, vector2D: 'Vector2D') -> float:
        """
            Compute the distance between the instance and another point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.distance` in interface :class:`~org.hipparchus.geometry.Point`
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second point
        
            Returns:
                the distance between the instance and p
        
            Compute the distance between two vectors according to the L :sub:`2` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(vector2D: 'Vector2D', vector2D2: 'Vector2D') -> float: ...
    @typing.overload
    def distance1(self, vector2D: 'Vector2D') -> float:
        """
            Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNorm1()` except that no intermediate vector is
            built
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.distance1` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`1` norm
        
            Compute the distance between two vectors according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`1` norm
        
            Since:
                1.6
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(vector2D: 'Vector2D', vector2D2: 'Vector2D') -> float: ...
    @typing.overload
    def distanceInf(self, vector2D: 'Vector2D') -> float:
        """
            Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormInf()` except that no intermediate vector is
            built
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.distanceInf` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`∞` norm
        
            Compute the distance between two vectors according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the distance between p1 and p2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(vector2D: 'Vector2D', vector2D2: 'Vector2D') -> float: ...
    @typing.overload
    def distanceSq(self, vector2D: 'Vector2D') -> float:
        """
            Compute the square of the distance between the instance and another vector.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormSq()` except that no intermediate vector is
            built
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.distanceSq` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the square of the distance between the instance and p
        
            Compute the square of the distance between two vectors.
        
            Calling this method is equivalent to calling: :code:`p1.subtract(p2).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector
                p2 (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the square of the distance between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(vector2D: 'Vector2D', vector2D2: 'Vector2D') -> float: ...
    def dotProduct(self, vector2D: 'Vector2D') -> float:
        """
            Compute the dot-product of the instance and another vector.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.dotProduct` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector
        
            Returns:
                the dot product this.v
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 2D vectors.
        
            If all coordinates of two 2D vectors are exactly the same, and none are :code:`Double.NaN`, the two 2D vectors are
            considered to be equal.
        
            :code:`NaN` coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or
            all) coordinates of the 2D vector are equal to :code:`Double.NaN`, the 2D vector is equal to
            :meth:`~org.hipparchus.geometry.euclidean.twod.Vector2D.NaN`.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality to this
        
            Returns:
                true if two 2D vector objects are equal, false if object is null, not an instance of Vector2D, or not equal to this
                Vector2D instance
        
        
        """
        ...
    def equalsIeee754(self, object: typing.Any) -> bool:
        """
            Test for the equality of two 2D vectors.
        
            If all coordinates of two 2D vectors are exactly the same, and none are :code:`NaN`, the two 2D vectors are considered
            to be equal.
        
            In compliance with IEEE754 handling, if any coordinates of any of the two vectors are :code:`NaN`, then the vectors are
            considered different. This implies that
            :meth:`~org.hipparchus.geometry.euclidean.twod.Vector2D.NaN`.equals(:meth:`~org.hipparchus.geometry.euclidean.twod.Vector2D.NaN`)
            returns :code:`false` despite the instance is checked against itself.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality to this
        
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
        
                  - :meth:`~org.hipparchus.geometry.euclidean.twod.Vector2D.%3Cinit%3E`
        
        
        
        """
        ...
    def getY(self) -> float:
        """
            Get the ordinate of the vector.
        
            Returns:
                ordinate of the vector
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.euclidean.twod.Vector2D.%3Cinit%3E`
        
        
        
        """
        ...
    def getZero(self) -> 'Vector2D':
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
            Get a hashCode for the 2D vector.
        
            All NaN values have the same hash code.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
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
    def moveTowards(self, vector2D: 'Vector2D', double: float) -> 'Vector2D':
        """
            Move towards another point.
        
            Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for
            moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.moveTowards` in interface :class:`~org.hipparchus.geometry.Point`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): other point
                ratio (double): motion ratio,
        
            Returns:
                moved point
        
        
        """
        ...
    def negate(self) -> 'Vector2D':
        """
            Get the opposite of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.negate` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Returns:
                a new vector which is opposite to the instance
        
        
        """
        ...
    @staticmethod
    def orientation(vector2D: 'Vector2D', vector2D2: 'Vector2D', vector2D3: 'Vector2D') -> float:
        """
            Compute the orientation of a triplet of points.
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): first vector of the triplet
                q (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): second vector of the triplet
                r (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): third vector of the triplet
        
            Returns:
                a positive value if (p, q, r) defines a counterclockwise oriented triangle, a negative value if (p, q, r) defines a
                clockwise oriented triangle, and 0 if (p, q, r) are collinear or some points are equal
        
            Since:
                1.2
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'Vector2D':
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
    def subtract(self, double: float, vector2D: 'Vector2D') -> 'Vector2D':
        """
            Subtract a scaled vector from the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.subtract` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                factor (double): scale factor to apply to v before subtracting it
                v (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): vector to subtract
        
            Returns:
                a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, vector2D: 'Vector2D') -> 'Vector2D':
        """
            Subtract a vector from the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Vector.subtract` in interface :class:`~org.hipparchus.geometry.Vector`
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`): vector to subtract
        
            Returns:
                a new vector
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
            Get the vector coordinates as a dimension 2 array.
        
            Returns:
                vector coordinates
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.euclidean.twod.Vector2D.%3Cinit%3E`
        
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a string representation of this vector.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
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
                format (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`): the custom format for components
        
            Returns:
                a string representation of this vector
        
        
        """
        ...

class Vector2DFormat(org.hipparchus.geometry.VectorFormat[Euclidean2D, Vector2D]):
    """
    public classVector2DFormat extends :class:`~org.hipparchus.geometry.VectorFormat`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`>
    
        Formats a 2D vector in components list format "{x; y}".
    
        The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format
        for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1;1}" and " { 1 ; 1 }
        " will be parsed without error and the same vector will be returned. In the second case, however, the parse position
        after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        **Note:** using "," as a separator may interfere with the grouping separator of the default
        :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat` for the
        current locale. Thus it is advised to use a
        :class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        instance with disabled grouping in such a case.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[org.hipparchus.geometry.Space, org.hipparchus.geometry.Vector]) -> str: ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[Euclidean2D, Vector2D], stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def getVector2DFormat() -> 'Vector2DFormat':
        """
            Returns the default 2D vector format for the current locale.
        
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
            Returns the default 2D vector format for the given locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale`): the specific locale used by the format.
        
            Returns:
                the 2D vector format specific to the given locale.
        
            Since:
                1.4
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Vector2D:
        """
            Parses a string to produce a :class:`~org.hipparchus.geometry.Vector` object.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.VectorFormat.parse` in class :class:`~org.hipparchus.geometry.VectorFormat`
        
            Parameters:
                source (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the string to parse
                pos (:class:`~org.hipparchus.geometry.euclidean.twod.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition`): input/output parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.geometry.Vector` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Vector2D: ...


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
