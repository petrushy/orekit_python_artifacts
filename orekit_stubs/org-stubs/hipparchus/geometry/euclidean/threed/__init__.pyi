
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
import org.hipparchus.geometry.euclidean.twod
import org.hipparchus.geometry.partitioning
import org.hipparchus.util
import typing



class Euclidean3D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    This class implements a three-dimensional space.
    
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
    def getInstance() -> 'Euclidean3D':
        """
        Get the unique instance.
        
        Returns:
            the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> org.hipparchus.geometry.euclidean.twod.Euclidean2D:
        """
        Get the n-1 dimension subspace of this space.
        
        Specified by: getSubSpace in interface Space
        
        Returns:
            n-1 dimension sub-space of this space
        
        Also see:
            getDimension
        
        
        """
        ...

_FieldLine__T = typing.TypeVar('_FieldLine__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLine(typing.Generic[_FieldLine__T]):
    """
    The class represent lines in a three dimensional space.
    
    Each oriented line is intrinsically associated with an abscissa which is a coordinate on the line. The point at abscissa 0 is the orthogonal projection of the origin on the line, another equivalent way to express this is to say that it is the point of the line which is closest to the origin. Abscissa increases in the line direction.
    """
    @typing.overload
    def __init__(self, line: 'FieldLine'[_FieldLine__T]): ...
    @typing.overload
    def __init__(self, p1: 'FieldVector3D'[_FieldLine__T], p2: 'FieldVector3D'[_FieldLine__T], tolerance: float): ...
    def closestPoint(self, line: 'FieldLine'[_FieldLine__T]) -> 'FieldVector3D'[_FieldLine__T]:
        """
        Compute the point of the instance closest to another line.
        
        Parameters:
            line (FieldLine<FieldLine> line): line to check against the instance
        
        Returns:
            point of the instance closest to another line
        
        
        """
        ...
    @typing.overload
    def contains(self, p: 'FieldVector3D'[_FieldLine__T]) -> bool:
        """
        Check if the instance contains a point.
        
        Parameters:
            p (Vector3D): point to check
        
        Returns:
            true if p belongs to the line
        
        
        """
        ...
    @typing.overload
    def contains(self, p: 'Vector3D') -> bool: ...
    @typing.overload
    def distance(self, p: 'FieldLine'[_FieldLine__T]) -> _FieldLine__T:
        """
        Compute the distance between the instance and a point.
        
        Parameters:
            p (Vector3D): to check
        
        Returns:
            distance between the instance and the point
        
        public FieldLine distance (FieldLine<FieldLine> line)
        
        Compute the shortest distance between the instance and another line.
        
        Parameters:
            line (FieldLine<FieldLine> line): line to check against the instance
        
        Returns:
            shortest distance between the instance and the line
        
        
        """
        ...
    @typing.overload
    def distance(self, fieldVector3D: 'FieldVector3D'[_FieldLine__T]) -> _FieldLine__T: ...
    @typing.overload
    def distance(self, vector3D: 'Vector3D') -> _FieldLine__T: ...
    @typing.overload
    def getAbscissa(self, point: 'FieldVector3D'[_FieldLine__T]) -> _FieldLine__T:
        """
        Get the abscissa of a point with respect to the line.
        
        The abscissa is 0 if the projection of the point and the projection of the frame origin on the line are the same point.
        
        Parameters:
            point (Vector3D): point to check
        
        Returns:
            abscissa of the point
        
        
        """
        ...
    @typing.overload
    def getAbscissa(self, point: 'Vector3D') -> _FieldLine__T: ...
    def getDirection(self) -> 'FieldVector3D'[_FieldLine__T]:
        """
        Get the normalized direction vector.
        
        Returns:
            normalized direction vector
        
        
        """
        ...
    def getOrigin(self) -> 'FieldVector3D'[_FieldLine__T]:
        """
        Get the line point closest to the origin.
        
        Returns:
            line point closest to the origin
        
        
        """
        ...
    def getTolerance(self) -> float:
        """
        Get the tolerance below which points are considered identical.
        
        Returns:
            tolerance below which points are considered identical
        
        
        """
        ...
    def intersection(self, line: 'FieldLine'[_FieldLine__T]) -> 'FieldVector3D'[_FieldLine__T]:
        """
        Get the intersection point of the instance and another line.
        
        Parameters:
            line (FieldLine<FieldLine> line): other line
        
        Returns:
            intersection point of the instance and the other line or null if there are no intersection points
        
        
        """
        ...
    def isSimilarTo(self, line: 'FieldLine'[_FieldLine__T]) -> bool:
        """
        Check if the instance is similar to another line.
        
        Lines are considered similar if they contain the same points. This does not mean they are equal since they can have opposite directions.
        
        Parameters:
            line (FieldLine<FieldLine> line): line to which instance should be compared
        
        Returns:
            true if the lines are similar
        
        
        """
        ...
    @typing.overload
    def pointAt(self, abscissa: float) -> 'FieldVector3D'[_FieldLine__T]: ...
    @typing.overload
    def pointAt(self, abscissa: _FieldLine__T) -> 'FieldVector3D'[_FieldLine__T]: ...
    def reset(self, p1: 'FieldVector3D'[_FieldLine__T], p2: 'FieldVector3D'[_FieldLine__T]) -> None:
        """
        Reset the instance as if built from two points.
        
        Parameters:
            p1 (FieldVector3D<FieldLine> p1): first point belonging to the line (this can be any point)
            p2 (FieldVector3D<FieldLine> p2): second point belonging to the line (this can be any point, different from p1)
        
        Raises:
            hipparchus: if the points are equal
        
        
        """
        ...
    def revert(self) -> 'FieldLine'[_FieldLine__T]:
        """
        Get a line with reversed direction.
        
        Returns:
            a new instance, with reversed direction
        
        
        """
        ...

_FieldRotation__T = typing.TypeVar('_FieldRotation__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRotation(java.io.Serializable, typing.Generic[_FieldRotation__T]):
    """
    This class is a re-implementation of Rotation using hipparchus.
    
    Instance of this class are guaranteed to be immutable.
    
    Also see:
        FieldVector3D,
        RotationOrder, serialized
    """
    @typing.overload
    def __init__(self, t: _FieldRotation__T, t2: _FieldRotation__T, t3: _FieldRotation__T, t4: _FieldRotation__T, boolean: bool): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_FieldRotation__T]], jpype.JArray], double: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldRotation__T], rotation: 'Rotation'): ...
    @typing.overload
    def __init__(self, axis: 'FieldVector3D'[_FieldRotation__T], angle: _FieldRotation__T, convention: 'RotationConvention'): ...
    @typing.overload
    def __init__(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T], fieldVector3D2: 'FieldVector3D'[_FieldRotation__T]): ...
    @typing.overload
    def __init__(self, u1: 'FieldVector3D'[_FieldRotation__T], u2: 'FieldVector3D'[_FieldRotation__T], v1: 'FieldVector3D'[_FieldRotation__T], v2: 'FieldVector3D'[_FieldRotation__T]): ...
    @typing.overload
    def __init__(self, rotationOrder: 'RotationOrder', rotationConvention: 'RotationConvention', t: _FieldRotation__T, t2: _FieldRotation__T, t3: _FieldRotation__T): ...
    _applyInverseTo_4__T = typing.TypeVar('_applyInverseTo_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _applyInverseTo_5__T = typing.TypeVar('_applyInverseTo_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def applyInverseTo(self, fieldRotation: 'FieldRotation'[_FieldRotation__T]) -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyInverseTo(self, rotation: 'Rotation') -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyInverseTo(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T]) -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    def applyInverseTo(self, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    @staticmethod
    def applyInverseTo(r: 'Rotation', u: 'FieldRotation'[_applyInverseTo_4__T]) -> 'FieldRotation'[_applyInverseTo_4__T]:
        """
        Apply the inverse of a rotation to a vector.
        
        Parameters:
            r (Rotation): rotation to apply
            u (FieldVector3D<T> u): vector to apply the inverse of the rotation to
        
        Returns:
            a new vector which such that u is its image by the rotation
        
        public FieldRotation<FieldRotation> applyInverseTo (FieldRotation<FieldRotation> r)
        
        Apply the inverse of the instance to another rotation.
        
        Calling this method is equivalent to call composeInverse.
        
        Parameters:
            r (FieldRotation<FieldRotation> r): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the inverse of the instance
        
        public FieldRotation<FieldRotation> applyInverseTo (Rotation r)
        
        Apply the inverse of the instance to another rotation.
        
        Calling this method is equivalent to call composeInverse.
        
        Parameters:
            r (Rotation): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the inverse of the instance
        
        Apply the inverse of a rotation to another rotation. Applying the inverse of a rotation to another rotation is computing the composition in an order compliant with the following rule : let u be any vector and v its image by rInner (i.e. rInner.applyTo(u) = v), let w be the inverse image of v by rOuter (i.e. rOuter.applyInverseTo(v) = w), then w = comp.applyTo(u), where comp = applyInverseTo(rOuter, rInner).
        
        Parameters:
            rOuter (Rotation): rotation to apply the rotation to
            rInner (FieldRotation<T> rInner): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the inverse of the instance
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def applyInverseTo(rotation: 'Rotation', fieldVector3D: 'FieldVector3D'[_applyInverseTo_5__T]) -> 'FieldVector3D'[_applyInverseTo_5__T]: ...
    @typing.overload
    def applyInverseTo(self, in_: typing.Union[typing.List[float], jpype.JArray], out: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None:
        """
        Apply the inverse of the rotation to a vector stored in an array.
        
        Parameters:
            in (FieldRotation[]): an array with three items which stores vector to rotate
            out (FieldRotation[]): an array with three items to put result to (it can be the same array as in)
        
        Apply the inverse of the rotation to a vector stored in an array.
        
        Parameters:
            in (double[]): an array with three items which stores vector to rotate
            out (FieldRotation[]): an array with three items to put result to
        
        """
        ...
    @typing.overload
    def applyInverseTo(self, tArray: typing.Union[typing.List[_FieldRotation__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None: ...
    _applyTo_4__T = typing.TypeVar('_applyTo_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _applyTo_5__T = typing.TypeVar('_applyTo_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def applyTo(self, fieldRotation: 'FieldRotation'[_FieldRotation__T]) -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyTo(self, rotation: 'Rotation') -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def applyTo(self, fieldVector3D: 'FieldVector3D'[_FieldRotation__T]) -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    def applyTo(self, vector3D: 'Vector3D') -> 'FieldVector3D'[_FieldRotation__T]: ...
    @typing.overload
    @staticmethod
    def applyTo(r: 'Rotation', u: 'FieldRotation'[_applyTo_4__T]) -> 'FieldRotation'[_applyTo_4__T]:
        """
        Apply a rotation to a vector.
        
        Parameters:
            r (Rotation): rotation to apply
            u (FieldVector3D<T> u): vector to apply the rotation to
        
        Returns:
            a new vector which is the image of u by the rotation
        
        public FieldRotation<FieldRotation> applyTo (FieldRotation<FieldRotation> r)
        
        Apply the instance to another rotation.
        
        Calling this method is equivalent to call compose.
        
        Parameters:
            r (FieldRotation<FieldRotation> r): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the instance
        
        public FieldRotation<FieldRotation> applyTo (Rotation r)
        
        Apply the instance to another rotation.
        
        Calling this method is equivalent to call compose.
        
        Parameters:
            r (Rotation): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the instance
        
        Apply a rotation to another rotation. Applying a rotation to another rotation is computing the composition in an order compliant with the following rule : let u be any vector and v its image by rInner (i.e. rInner.applyTo(u) = v), let w be the image of v by rOuter (i.e. rOuter.applyTo(v) = w), then w = comp.applyTo(u), where comp = applyTo(rOuter, rInner).
        
        Parameters:
            r1 (Rotation): rotation to apply
            rInner (FieldRotation<T> rInner): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the instance
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def applyTo(rotation: 'Rotation', fieldVector3D: 'FieldVector3D'[_applyTo_5__T]) -> 'FieldVector3D'[_applyTo_5__T]: ...
    @typing.overload
    def applyTo(self, in_: typing.Union[typing.List[float], jpype.JArray], out: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None:
        """
        Apply the rotation to a vector stored in an array.
        
        Parameters:
            in (FieldRotation[]): an array with three items which stores vector to rotate
            out (FieldRotation[]): an array with three items to put result to (it can be the same array as in)
        
        Apply the rotation to a vector stored in an array.
        
        Parameters:
            in (double[]): an array with three items which stores vector to rotate
            out (FieldRotation[]): an array with three items to put result to
        
        """
        ...
    @typing.overload
    def applyTo(self, tArray: typing.Union[typing.List[_FieldRotation__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldRotation__T], jpype.JArray]) -> None: ...
    @typing.overload
    def compose(self, r: 'FieldRotation'[_FieldRotation__T], convention: 'RotationConvention') -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def compose(self, r: 'Rotation', convention: 'RotationConvention') -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def composeInverse(self, r: 'FieldRotation'[_FieldRotation__T], convention: 'RotationConvention') -> 'FieldRotation'[_FieldRotation__T]: ...
    @typing.overload
    def composeInverse(self, r: 'Rotation', convention: 'RotationConvention') -> 'FieldRotation'[_FieldRotation__T]: ...
    _distance__T = typing.TypeVar('_distance__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def distance(r1: 'FieldRotation'[_distance__T], r2: 'FieldRotation'[_distance__T]) -> _distance__T:
        """
        Compute the distance between two rotations.
        
        The distance is intended here as a way to check if two rotations are almost similar (i.e. they transform vectors the same way) or very different. It is mathematically defined as the angle of the rotation r that prepended to one of the rotations gives the other one: \(r_1(r) = r_2\)
        
        This distance is an angle between 0 and π. Its value is the smallest possible upper bound of the angle in radians between r :sub:`1` (v) and r :sub:`2` (v) for all possible vectors v. This upper bound is reached for some v. The distance is equal to 0 if and only if the two rotations are identical.
        
        Comparing two rotations should always be done using this value rather than for example comparing the components of the quaternions. It is much more stable, and has a geometric meaning. Also comparing quaternions components is error prone since for example quaternions (0.36, 0.48, -0.48, -0.64) and (-0.36, -0.48, 0.48, 0.64) represent exactly the same rotation despite their components are different (they are exact opposites).
        
        Parameters:
            r1 (FieldRotation<T> r1): first rotation
            r2 (FieldRotation<T> r2): second rotation
        
        Returns:
            distance between r1 and r2
        
        
        """
        ...
    def getAngle(self) -> _FieldRotation__T:
        """
        Get the angle of the rotation.
        
        Returns:
            angle of the rotation (between 0 and π)
        
        
        """
        ...
    def getAngles(self, order: 'RotationOrder', convention: 'RotationConvention') -> typing.MutableSequence[_FieldRotation__T]:
        """
        Get the Cardan or Euler angles corresponding to the instance.
        
        The equations show that each rotation can be defined by two different values of the Cardan or Euler angles set. For example if Cardan angles are used, the rotation defined by the angles a :sub:`1` , a :sub:`2` and a :sub:`3` is the same as the rotation defined by the angles π + a :sub:`1` , π - a :sub:`2` and π + a :sub:`3` . This method implements the following arbitrary choices:
        
          - for Cardan angles, the chosen set is the one for which the second angle is between -π/2 and π/2 (i.e its cosine is
            positive),
          - for Euler angles, the chosen set is the one for which the second angle is between 0 and π (i.e its sine is positive).
        
        The algorithm used here works even when the rotation is exactly at the the singularity of the rotation order and convention. In this case, one of the angles in the singular pair is arbitrarily set to exactly 0 and the second angle is computed. The angle set to 0 in the singular case is the angle of the first rotation in the case of Cardan orders, and it is the angle of the last rotation in the case of Euler orders. This implies that extracting the angles of a rotation never fails (it used to trigger an exception in singular cases up to Hipparchus 3.0).
        
        Parameters:
            order (RotationOrder): rotation order to use
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            an array of three angles, in the order specified by the set
        
        
        """
        ...
    def getAxis(self, convention: 'RotationConvention') -> 'FieldVector3D'[_FieldRotation__T]:
        """
        Get the normalized axis of the rotation.
        
        Note that as getAngle always returns an angle between 0 and π, changing the convention changes the direction of the axis, not the sign of the angle.
        
        Parameters:
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            normalized axis of the rotation
        
        
        """
        ...
    _getIdentity__T = typing.TypeVar('_getIdentity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getIdentity(field: org.hipparchus.Field[_getIdentity__T]) -> 'FieldRotation'[_getIdentity__T]:
        """
        Get identity rotation.
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new rotation
        
        
        """
        ...
    def getMatrix(self) -> typing.MutableSequence[typing.MutableSequence[_FieldRotation__T]]:
        """
        Get the 3X3 matrix corresponding to the instance
        
        Returns:
            the matrix corresponding to the instance
        
        
        """
        ...
    def getQ0(self) -> _FieldRotation__T:
        """
        Get the scalar coordinate of the quaternion.
        
        Returns:
            scalar coordinate of the quaternion
        
        
        """
        ...
    def getQ1(self) -> _FieldRotation__T:
        """
        Get the first coordinate of the vectorial part of the quaternion.
        
        Returns:
            first coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def getQ2(self) -> _FieldRotation__T:
        """
        Get the second coordinate of the vectorial part of the quaternion.
        
        Returns:
            second coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def getQ3(self) -> _FieldRotation__T:
        """
        Get the third coordinate of the vectorial part of the quaternion.
        
        Returns:
            third coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def revert(self) -> 'FieldRotation'[_FieldRotation__T]:
        """
        Revert a rotation. Build a rotation which reverse the effect of another rotation. This means that if r(u) = v, then r.revert(v) = u. The instance is not changed.
        
        Returns:
            a new rotation whose effect is the reverse of the effect of the instance
        
        
        """
        ...
    def toRotation(self) -> 'Rotation':
        """
        Convert to a constant vector without derivatives.
        
        Returns:
            a constant vector
        
        
        """
        ...

_FieldVector3D__T = typing.TypeVar('_FieldVector3D__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldVector3D(org.hipparchus.util.FieldBlendable['FieldVector3D'[_FieldVector3D__T], _FieldVector3D__T], java.io.Serializable, typing.Generic[_FieldVector3D__T]):
    """
    This class is a re-implementation of Vector3D using hipparchus.
    
    Instance of this class are guaranteed to be immutable.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, double: float, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'FieldVector3D'[_FieldVector3D__T], a2: float, u2: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'FieldVector3D'[_FieldVector3D__T], a2: float, u2: 'FieldVector3D'[_FieldVector3D__T], a3: float, u3: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'FieldVector3D'[_FieldVector3D__T], a2: float, u2: 'FieldVector3D'[_FieldVector3D__T], a3: float, u3: 'FieldVector3D'[_FieldVector3D__T], a4: float, u4: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, t2: _FieldVector3D__T): ...
    @typing.overload
    def __init__(self, x: _FieldVector3D__T, y: _FieldVector3D__T, z: _FieldVector3D__T): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, fieldVector3D: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, a1: _FieldVector3D__T, u1: 'FieldVector3D'[_FieldVector3D__T], a2: _FieldVector3D__T, u2: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, a1: _FieldVector3D__T, u1: 'FieldVector3D'[_FieldVector3D__T], a2: _FieldVector3D__T, u2: 'FieldVector3D'[_FieldVector3D__T], a3: _FieldVector3D__T, u3: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, a1: _FieldVector3D__T, u1: 'FieldVector3D'[_FieldVector3D__T], a2: _FieldVector3D__T, u2: 'FieldVector3D'[_FieldVector3D__T], a3: _FieldVector3D__T, u3: 'FieldVector3D'[_FieldVector3D__T], a4: _FieldVector3D__T, u4: 'FieldVector3D'[_FieldVector3D__T]): ...
    @typing.overload
    def __init__(self, t: _FieldVector3D__T, vector3D: 'Vector3D'): ...
    @typing.overload
    def __init__(self, a1: _FieldVector3D__T, u1: 'Vector3D', a2: _FieldVector3D__T, u2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, a1: _FieldVector3D__T, u1: 'Vector3D', a2: _FieldVector3D__T, u2: 'Vector3D', a3: _FieldVector3D__T, u3: 'Vector3D'): ...
    @typing.overload
    def __init__(self, a1: _FieldVector3D__T, u1: 'Vector3D', a2: _FieldVector3D__T, u2: 'Vector3D', a3: _FieldVector3D__T, u3: 'Vector3D', a4: _FieldVector3D__T, u4: 'Vector3D'): ...
    @typing.overload
    def __init__(self, v: typing.Union[typing.List[_FieldVector3D__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldVector3D__T], vector3D: 'Vector3D'): ...
    @typing.overload
    def add(self, factor: float, v: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, factor: float, v: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, factor: _FieldVector3D__T, v: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, factor: _FieldVector3D__T, v: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def add(self, v: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    _angle_0__T = typing.TypeVar('_angle_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _angle_1__T = typing.TypeVar('_angle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _angle_2__T = typing.TypeVar('_angle_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def angle(v1: 'FieldVector3D'[_angle_0__T], v2: 'FieldVector3D'[_angle_0__T]) -> _angle_0__T: ...
    @typing.overload
    @staticmethod
    def angle(v1: 'FieldVector3D'[_angle_1__T], v2: 'Vector3D') -> _angle_1__T: ...
    @typing.overload
    @staticmethod
    def angle(v1: 'Vector3D', v2: 'FieldVector3D'[_angle_2__T]) -> _angle_2__T: ...
    def blendArithmeticallyWith(self, other: 'FieldVector3D'[_FieldVector3D__T], blendingValue: _FieldVector3D__T) -> 'FieldVector3D'[_FieldVector3D__T]:
        """
        Specified by: hipparchus in interface hipparchus
        
        Raises:
            hipparchus: 
        
        """
        ...
    _crossProduct_2__T = typing.TypeVar('_crossProduct_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _crossProduct_3__T = typing.TypeVar('_crossProduct_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _crossProduct_4__T = typing.TypeVar('_crossProduct_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def crossProduct(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def crossProduct(self, v: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    @staticmethod
    def crossProduct(v1: 'FieldVector3D'[_crossProduct_2__T], v2: 'FieldVector3D'[_crossProduct_2__T]) -> 'FieldVector3D'[_crossProduct_2__T]:
        """
        Compute the cross-product of two vectors.
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the cross product v1 ^ v2 as a new Vector
        
        Compute the cross-product of two vectors.
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the cross product v1 ^ v2 as a new Vector
        
        Compute the cross-product of two vectors.
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the cross product v1 ^ v2 as a new Vector
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def crossProduct(v1: 'FieldVector3D'[_crossProduct_3__T], v2: 'Vector3D') -> 'FieldVector3D'[_crossProduct_3__T]: ...
    @typing.overload
    @staticmethod
    def crossProduct(v1: 'Vector3D', v2: 'FieldVector3D'[_crossProduct_4__T]) -> 'FieldVector3D'[_crossProduct_4__T]: ...
    _distance_2__T = typing.TypeVar('_distance_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance_3__T = typing.TypeVar('_distance_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance_4__T = typing.TypeVar('_distance_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distance(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
        Compute the distance between the instance and another vector according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`2` norm
        
        """
        ...
    @typing.overload
    def distance(self, v: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distance(v1: 'FieldVector3D'[_distance_2__T], v2: 'FieldVector3D'[_distance_2__T]) -> _distance_2__T:
        """
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`2` norm
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`2` norm
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(v1: 'FieldVector3D'[_distance_3__T], v2: 'Vector3D') -> _distance_3__T: ...
    @typing.overload
    @staticmethod
    def distance(v1: 'Vector3D', v2: 'FieldVector3D'[_distance_4__T]) -> _distance_4__T: ...
    _distance1_2__T = typing.TypeVar('_distance1_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance1_3__T = typing.TypeVar('_distance1_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distance1_4__T = typing.TypeVar('_distance1_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distance1(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
        Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`1` norm
        
        """
        ...
    @typing.overload
    def distance1(self, v: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distance1(v1: 'FieldVector3D'[_distance1_2__T], v2: 'FieldVector3D'[_distance1_2__T]) -> _distance1_2__T:
        """
        Compute the distance between two vectors according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`1` norm
        
        Compute the distance between two vectors according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`1` norm
        
        Compute the distance between two vectors according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`1` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(v1: 'FieldVector3D'[_distance1_3__T], v2: 'Vector3D') -> _distance1_3__T: ...
    @typing.overload
    @staticmethod
    def distance1(v1: 'Vector3D', v2: 'FieldVector3D'[_distance1_4__T]) -> _distance1_4__T: ...
    _distanceInf_2__T = typing.TypeVar('_distanceInf_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceInf_3__T = typing.TypeVar('_distanceInf_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceInf_4__T = typing.TypeVar('_distanceInf_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distanceInf(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
        Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`∞` norm
        
        """
        ...
    @typing.overload
    def distanceInf(self, v: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(v1: 'FieldVector3D'[_distanceInf_2__T], v2: 'FieldVector3D'[_distanceInf_2__T]) -> _distanceInf_2__T:
        """
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`∞` norm
        
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`∞` norm
        
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(v1: 'FieldVector3D'[_distanceInf_3__T], v2: 'Vector3D') -> _distanceInf_3__T: ...
    @typing.overload
    @staticmethod
    def distanceInf(v1: 'Vector3D', v2: 'FieldVector3D'[_distanceInf_4__T]) -> _distanceInf_4__T: ...
    _distanceSq_2__T = typing.TypeVar('_distanceSq_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceSq_3__T = typing.TypeVar('_distanceSq_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _distanceSq_4__T = typing.TypeVar('_distanceSq_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def distanceSq(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
        Compute the square of the distance between the instance and another vector.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the square of the distance between the instance and p
        
        """
        ...
    @typing.overload
    def distanceSq(self, v: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(v1: 'FieldVector3D'[_distanceSq_2__T], v2: 'FieldVector3D'[_distanceSq_2__T]) -> _distanceSq_2__T:
        """
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the square of the distance between v1 and v2
        
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the square of the distance between v1 and v2
        
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the square of the distance between v1 and v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(v1: 'FieldVector3D'[_distanceSq_3__T], v2: 'Vector3D') -> _distanceSq_3__T: ...
    @typing.overload
    @staticmethod
    def distanceSq(v1: 'Vector3D', v2: 'FieldVector3D'[_distanceSq_4__T]) -> _distanceSq_4__T: ...
    _dotProduct_2__T = typing.TypeVar('_dotProduct_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _dotProduct_3__T = typing.TypeVar('_dotProduct_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _dotProduct_4__T = typing.TypeVar('_dotProduct_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dotProduct(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> _FieldVector3D__T:
        """
        Compute the dot-product of the instance and another vector.
        
        The implementation uses specific multiplication and addition algorithms to preserve accuracy and reduce cancellation effects. It should be very accurate even for nearly orthogonal vectors.
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the dot product this.v
        
        Also see:
            hipparchus
        
        """
        ...
    @typing.overload
    def dotProduct(self, v: 'Vector3D') -> _FieldVector3D__T: ...
    @typing.overload
    @staticmethod
    def dotProduct(v1: 'FieldVector3D'[_dotProduct_2__T], v2: 'FieldVector3D'[_dotProduct_2__T]) -> _dotProduct_2__T:
        """
        Compute the dot-product of two vectors.
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the dot product v1.v2
        
        Compute the dot-product of two vectors.
        
        Parameters:
            v1 (FieldVector3D<T> v1): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the dot product v1.v2
        
        Compute the dot-product of two vectors.
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (FieldVector3D<T> v2): second vector
        
        Returns:
            the dot product v1.v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def dotProduct(v1: 'FieldVector3D'[_dotProduct_3__T], v2: 'Vector3D') -> _dotProduct_3__T: ...
    @typing.overload
    @staticmethod
    def dotProduct(v1: 'Vector3D', v2: 'FieldVector3D'[_dotProduct_4__T]) -> _dotProduct_4__T: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 3D vectors.
        
        If all coordinates of two 3D vectors are exactly the same, and none of their hipparchus are NaN, the two 3D vectors are considered to be equal.
        
        NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) real part of the coordinates of the 3D vector are NaN, the 3D vector is NaN.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 3D vector objects are equal, false if object is null, not an instance of FieldVector3D, or not equal to this
            FieldVector3D instance
        
        
        """
        ...
    def getAlpha(self) -> _FieldVector3D__T:
        """
        Get the azimuth of the vector.
        
        Returns:
            azimuth (α) of the vector, between -π and +π
        
        
        """
        ...
    def getDelta(self) -> _FieldVector3D__T:
        """
        Get the elevation of the vector.
        
        Returns:
            elevation (δ) of the vector, between -π/2 and +π/2
        
        
        """
        ...
    _getMinusI__T = typing.TypeVar('_getMinusI__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getMinusI(field: org.hipparchus.Field[_getMinusI__T]) -> 'FieldVector3D'[_getMinusI__T]:
        """
        Get opposite of the first canonical vector (coordinates: -1, 0, 0).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getMinusJ__T = typing.TypeVar('_getMinusJ__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getMinusJ(field: org.hipparchus.Field[_getMinusJ__T]) -> 'FieldVector3D'[_getMinusJ__T]:
        """
        Get opposite of the second canonical vector (coordinates: 0, -1, 0).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getMinusK__T = typing.TypeVar('_getMinusK__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getMinusK(field: org.hipparchus.Field[_getMinusK__T]) -> 'FieldVector3D'[_getMinusK__T]:
        """
        Get opposite of the third canonical vector (coordinates: 0, 0, -1).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getNaN__T = typing.TypeVar('_getNaN__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getNaN(field: org.hipparchus.Field[_getNaN__T]) -> 'FieldVector3D'[_getNaN__T]:
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
    def getNegativeInfinity(field: org.hipparchus.Field[_getNegativeInfinity__T]) -> 'FieldVector3D'[_getNegativeInfinity__T]:
        """
        Get a vector with all coordinates set to negative infinity.
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    def getNorm(self) -> _FieldVector3D__T:
        """
        Get the L :sub:`2` norm for the vector.
        
        Returns:
            Euclidean norm for the vector
        
        
        """
        ...
    def getNorm1(self) -> _FieldVector3D__T:
        """
        Get the L :sub:`1` norm for the vector.
        
        Returns:
            L :sub:`1` norm for the vector
        
        
        """
        ...
    def getNormInf(self) -> _FieldVector3D__T:
        """
        Get the L :sub:`∞` norm for the vector.
        
        Returns:
            L :sub:`∞` norm for the vector
        
        
        """
        ...
    def getNormSq(self) -> _FieldVector3D__T:
        """
        Get the square of the norm for the vector.
        
        Returns:
            square of the Euclidean norm for the vector
        
        
        """
        ...
    _getPlusI__T = typing.TypeVar('_getPlusI__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPlusI(field: org.hipparchus.Field[_getPlusI__T]) -> 'FieldVector3D'[_getPlusI__T]:
        """
        Get first canonical vector (coordinates: 1, 0, 0).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getPlusJ__T = typing.TypeVar('_getPlusJ__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPlusJ(field: org.hipparchus.Field[_getPlusJ__T]) -> 'FieldVector3D'[_getPlusJ__T]:
        """
        Get second canonical vector (coordinates: 0, 1, 0).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getPlusK__T = typing.TypeVar('_getPlusK__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPlusK(field: org.hipparchus.Field[_getPlusK__T]) -> 'FieldVector3D'[_getPlusK__T]:
        """
        Get third canonical vector (coordinates: 0, 0, 1).
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    _getPositiveInfinity__T = typing.TypeVar('_getPositiveInfinity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPositiveInfinity(field: org.hipparchus.Field[_getPositiveInfinity__T]) -> 'FieldVector3D'[_getPositiveInfinity__T]:
        """
        Get a vector with all coordinates set to positive infinity.
        
        Parameters:
            field (hipparchus<T> field): field for the components
        
        Returns:
            a new vector
        
        
        """
        ...
    def getX(self) -> _FieldVector3D__T:
        """
        Get the abscissa of the vector.
        
        Returns:
            abscissa of the vector
        
        
        """
        ...
    def getY(self) -> _FieldVector3D__T:
        """
        Get the ordinate of the vector.
        
        Returns:
            ordinate of the vector
        
        
        """
        ...
    def getZ(self) -> _FieldVector3D__T:
        """
        Get the height of the vector.
        
        Returns:
            height of the vector
        
        
        """
        ...
    _getZero__T = typing.TypeVar('_getZero__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getZero(field: org.hipparchus.Field[_getZero__T]) -> 'FieldVector3D'[_getZero__T]:
        """
        Get null vector (coordinates: 0, 0, 0).
        
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
    def negate(self) -> 'FieldVector3D'[_FieldVector3D__T]:
        """
        Get the opposite of the instance.
        
        Returns:
            a new vector which is opposite to the instance
        
        
        """
        ...
    def normalize(self) -> 'FieldVector3D'[_FieldVector3D__T]:
        """
        Get a normalized vector aligned with the instance.
        
        Returns:
            a new normalized vector
        
        Raises:
            hipparchus: if the norm is zero
        
        
        """
        ...
    def orthogonal(self) -> 'FieldVector3D'[_FieldVector3D__T]:
        """
        Get a vector orthogonal to the instance.
        
        There are an infinite number of normalized vectors orthogonal to the instance. This method picks up one of them almost arbitrarily. It is useful when one needs to compute a reference frame with one of the axes in a predefined direction. The following example shows how to build a frame having the k axis aligned with the known vector u :
        
        
           Vector3D k = u.normalize();
           Vector3D i = k.orthogonal();
           Vector3D j = Vector3D.crossProduct(k, i);
         
        
        Returns:
            a new normalized vector orthogonal to the instance
        
        Raises:
            hipparchus: if the norm of the instance is null
        
        
        """
        ...
    @typing.overload
    def scalarMultiply(self, a: float) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def scalarMultiply(self, a: _FieldVector3D__T) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, factor: float, v: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, factor: float, v: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, factor: _FieldVector3D__T, v: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, factor: _FieldVector3D__T, v: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, v: 'FieldVector3D'[_FieldVector3D__T]) -> 'FieldVector3D'[_FieldVector3D__T]: ...
    @typing.overload
    def subtract(self, v: 'Vector3D') -> 'FieldVector3D'[_FieldVector3D__T]: ...
    def toArray(self) -> typing.MutableSequence[_FieldVector3D__T]:
        """
        Get the vector coordinates as a dimension 3 array.
        
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
    def toVector3D(self) -> 'Vector3D':
        """
        Convert to a constant vector without extra field parts.
        
        Returns:
            a constant vector
        
        
        """
        ...

class Line(org.hipparchus.geometry.partitioning.Embedding[Euclidean3D, 'Vector3D', org.hipparchus.geometry.euclidean.oned.Euclidean1D, org.hipparchus.geometry.euclidean.oned.Vector1D]):
    """
    The class represent lines in a three dimensional space.
    
    Each oriented line is intrinsically associated with an abscissa which is a coordinate on the line. The point at abscissa 0 is the orthogonal projection of the origin on the line, another equivalent way to express this is to say that it is the point of the line which is closest to the origin. Abscissa increases in the line direction.
    
    Also see:
        fromDirection,
    """
    @typing.overload
    def __init__(self, line: 'Line'): ...
    @typing.overload
    def __init__(self, p1: 'Vector3D', p2: 'Vector3D', tolerance: float): ...
    def closestPoint(self, line: 'Line') -> 'Vector3D':
        """
        Compute the point of the instance closest to another line.
        
        Parameters:
            line (Line): line to check against the instance
        
        Returns:
            point of the instance closest to another line
        
        
        """
        ...
    def contains(self, p: 'Vector3D') -> bool:
        """
        Check if the instance contains a point.
        
        Parameters:
            p (Vector3D): point to check
        
        Returns:
            true if p belongs to the line
        
        
        """
        ...
    @typing.overload
    def distance(self, p: 'Line') -> float:
        """
        Compute the distance between the instance and a point.
        
        Parameters:
            p (Vector3D): to check
        
        Returns:
            distance between the instance and the point
        
        Compute the shortest distance between the instance and another line.
        
        Parameters:
            line (Line): line to check against the instance
        
        Returns:
            shortest distance between the instance and the line
        
        
        """
        ...
    @typing.overload
    def distance(self, vector3D: 'Vector3D') -> float: ...
    @staticmethod
    def fromDirection(point: 'Vector3D', direction: 'Vector3D', tolerance: float) -> 'Line':
        """
        Create a line from a point and a direction. Line = point + t * direction, where t is any real number.
        
        Parameters:
            point (Vector3D): on the line. Can be any point.
            direction (Vector3D): of the line. Must not be the zero vector.
            tolerance (double): below which points are considered identical.
        
        Returns:
            a new Line with the given point and direction.
        
        Raises:
            hipparchus: if direction is the zero vector.
        
        
        """
        ...
    def getAbscissa(self, point: 'Vector3D') -> float:
        """
        Get the abscissa of a point with respect to the line.
        
        The abscissa is 0 if the projection of the point and the projection of the frame origin on the line are the same point.
        
        Parameters:
            point (Vector3D): point to check
        
        Returns:
            abscissa of the point
        
        
        """
        ...
    def getDirection(self) -> 'Vector3D':
        """
        Get the normalized direction vector.
        
        Returns:
            normalized direction vector
        
        
        """
        ...
    def getOrigin(self) -> 'Vector3D':
        """
        Get the line point closest to the origin.
        
        Returns:
            line point closest to the origin
        
        
        """
        ...
    def getTolerance(self) -> float:
        """
        Get the tolerance below which points are considered identical.
        
        Returns:
            tolerance below which points are considered identical
        
        
        """
        ...
    def intersection(self, line: 'Line') -> 'Vector3D':
        """
        Get the intersection point of the instance and another line.
        
        Parameters:
            line (Line): other line
        
        Returns:
            intersection point of the instance and the other line or null if there are no intersection points
        
        
        """
        ...
    def isSimilarTo(self, line: 'Line') -> bool:
        """
        Check if the instance is similar to another line.
        
        Lines are considered similar if they contain the same points. This does not mean they are equal since they can have opposite directions.
        
        Parameters:
            line (Line): line to which instance should be compared
        
        Returns:
            true if the lines are similar
        
        
        """
        ...
    def pointAt(self, abscissa: float) -> 'Vector3D':
        """
        Get one point from the line.
        
        Parameters:
            abscissa (double): desired abscissa for the point
        
        Returns:
            one point belonging to the line, at specified abscissa
        
        
        """
        ...
    def reset(self, p1: 'Vector3D', p2: 'Vector3D') -> None:
        """
        Reset the instance as if built from two points.
        
        Parameters:
            p1 (Vector3D): first point belonging to the line (this can be any point)
            p2 (Vector3D): second point belonging to the line (this can be any point, different from p1)
        
        Raises:
            hipparchus: if the points are equal
        
        
        """
        ...
    def revert(self) -> 'Line':
        """
        Get a line with reversed direction.
        
        Returns:
            a new instance, with reversed direction
        
        
        """
        ...
    def toSpace(self, point: org.hipparchus.geometry.euclidean.oned.Vector1D) -> 'Vector3D':
        """
        Transform a sub-space point into a space point.
        
        Specified by: toSpace in interface Embedding
        
        Parameters:
            point (Vector1D): (n-1)-dimension point of the sub-space
        
        Returns:
            n-dimension point of the space corresponding to the specified sub-space point
        
        Also see:
            pointAt
        
        
        """
        ...
    def toSubSpace(self, point: 'Vector3D') -> org.hipparchus.geometry.euclidean.oned.Vector1D:
        """
        Transform a space point into a sub-space point.
        
        Specified by: toSubSpace in interface Embedding
        
        Parameters:
            point (Vector3D): n-dimension point of the space
        
        Returns:
            (n-1)-dimension point of the sub-space corresponding to the specified space point
        
        Also see:
            getAbscissa
        
        
        """
        ...
    def wholeLine(self) -> 'SubLine':
        """
        Build a sub-line covering the whole line.
        
        Returns:
            a sub-line covering the whole line
        
        
        """
        ...

class OutlineExtractor:
    """
    Extractor for PolygonsSet outlines.
    
    This class extracts the 2D outlines from {PolygonsSet in a specified projection plane.
    """
    def __init__(self, u: 'Vector3D', v: 'Vector3D'):
        """
        Build an extractor for a specific projection plane.
        
        Parameters:
            u (Vector3D): abscissa axis of the projection point
            v (Vector3D): ordinate axis of the projection point
        
        
        """
        ...
    def getOutline(self, polyhedronsSet: 'PolyhedronsSet') -> typing.MutableSequence[typing.MutableSequence[org.hipparchus.geometry.euclidean.twod.Vector2D]]:
        """
        Extract the outline of a polyhedrons set.
        
        Parameters:
            polyhedronsSet (PolyhedronsSet): polyhedrons set whose outline must be extracted
        
        Returns:
            an outline, as an array of loops.
        
        
        """
        ...

class Plane(org.hipparchus.geometry.partitioning.Hyperplane[Euclidean3D, 'Vector3D', 'Plane', 'SubPlane'], org.hipparchus.geometry.partitioning.Embedding[Euclidean3D, 'Vector3D', org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D]):
    """
    The class represent planes in a three dimensional space.
    """
    @typing.overload
    def __init__(self, plane: 'Plane'): ...
    @typing.overload
    def __init__(self, normal: 'Vector3D', tolerance: float): ...
    @typing.overload
    def __init__(self, p: 'Vector3D', normal: 'Vector3D', tolerance: float): ...
    @typing.overload
    def __init__(self, p1: 'Vector3D', p2: 'Vector3D', p3: 'Vector3D', tolerance: float): ...
    def arbitraryPoint(self) -> 'Vector3D':
        """
        Get an arbitrary point in the hyperplane.
        
        Specified by: arbitraryPoint in interface Hyperplane
        
        Returns:
            arbirary point in the hyperplane
        
        
        """
        ...
    def contains(self, p: 'Vector3D') -> bool:
        """
        Check if the instance contains a point.
        
        Parameters:
            p (Vector3D): point to check
        
        Returns:
            true if p belongs to the plane
        
        
        """
        ...
    def copySelf(self) -> 'Plane':
        """
        Copy the instance.
        
        The instance created is completely independant of the original one. A deep copy is used, none of the underlying objects are shared (except for immutable objects).
        
        Specified by: copySelf in interface Hyperplane
        
        Returns:
            a new hyperplane, copy of the instance
        
        
        """
        ...
    def emptyHyperplane(self) -> 'SubPlane':
        """
        Build a sub-hyperplane covering nothing.
        
        Specified by: emptyHyperplane in interface Hyperplane
        
        Returns:
            a sub-hyperplane covering nothing
        
        
        """
        ...
    def getNormal(self) -> 'Vector3D':
        """
        Get the normalized normal vector.
        
        The frame defined by (getU, getV, getNormal()) is a right-handed orthonormalized frame).
        
        Returns:
            normalized normal vector
        
        Also see:
            getU,
            getV
        
        
        """
        ...
    @typing.overload
    def getOffset(self, plane: 'Plane') -> float:
        """
        This method should be called only for parallel planes otherwise the result is not meaningful.
        
        The offset is 0 if both planes are the same, it is positive if the plane is on the plus side of the instance and negative if it is on the minus side, according to its natural orientation.
        
        Parameters:
            plane (Plane): plane to check
        
        Returns:
            offset of the plane
        
        Get the offset (oriented distance) of a point.
        
        The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
        Specified by: getOffset in interface Hyperplane
        
        Parameters:
            point (Vector3D): point to check
        
        Returns:
            offset of the point
        
        
        """
        ...
    @typing.overload
    def getOffset(self, vector3D: 'Vector3D') -> float: ...
    def getOrigin(self) -> 'Vector3D':
        """
        Get the origin point of the plane frame.
        
        The point returned is the orthogonal projection of the 3D-space origin in the plane.
        
        Returns:
            the origin point of the plane frame (point closest to the 3D-space origin)
        
        
        """
        ...
    def getPointAt(self, inPlane: org.hipparchus.geometry.euclidean.twod.Vector2D, offset: float) -> 'Vector3D':
        """
        Get one point from the 3D-space.
        
        Parameters:
            inPlane (Vector2D): desired in-plane coordinates for the point in the plane
            offset (double): desired offset for the point
        
        Returns:
            one point in the 3D-space, with given coordinates and offset relative to the plane
        
        
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
    def getU(self) -> 'Vector3D':
        """
        Get the plane first canonical vector.
        
        The frame defined by (getU(), getV, getNormal) is a right-handed orthonormalized frame).
        
        Returns:
            normalized first canonical vector
        
        Also see:
            getV,
            getNormal
        
        
        """
        ...
    def getV(self) -> 'Vector3D':
        """
        Get the plane second canonical vector.
        
        The frame defined by (getU, getV(), getNormal) is a right-handed orthonormalized frame).
        
        Returns:
            normalized second canonical vector
        
        Also see:
            getU,
            getNormal
        
        
        """
        ...
    @typing.overload
    def intersection(self, line: 'Plane') -> Line:
        """
        Get the intersection of a line with the instance.
        
        Parameters:
            line (Line): line intersecting the instance
        
        Returns:
            intersection point between between the line and the instance (null if the line is parallel to the instance)
        
        Build the line shared by the instance and another plane.
        
        Parameters:
            other (Plane): other plane
        
        Returns:
            line at the intersection of the instance and the other plane (really a
            Line instance)
        
        Get the intersection point of three planes.
        
        Parameters:
            plane1 (Plane): first plane1
            plane2 (Plane): second plane2
            plane3 (Plane): third plane2
        
        Returns:
            intersection point of three planes, null if some planes are parallel
        
        
        """
        ...
    @typing.overload
    def intersection(self, line: Line) -> 'Vector3D': ...
    @typing.overload
    @staticmethod
    def intersection(plane1: 'Plane', plane2: 'Plane', plane3: 'Plane') -> 'Vector3D': ...
    def isSimilarTo(self, plane: 'Plane') -> bool:
        """
        Check if the instance is similar to another plane.
        
        Planes are considered similar if they contain the same points. This does not mean they are equal since they can have opposite normals.
        
        Parameters:
            plane (Plane): plane to which the instance is compared
        
        Returns:
            true if the planes are similar
        
        
        """
        ...
    def moveToOffset(self, point: 'Vector3D', offset: float) -> 'Vector3D':
        """
        Move point up to specified offset.
        
        Motion is orthogonal to the hyperplane
        
        Specified by: moveToOffset in interface Hyperplane
        
        Parameters:
            point (Vector3D): point to move
            offset (double): desired offset
        
        Returns:
            moved point at desired offset
        
        
        """
        ...
    def project(self, point: 'Vector3D') -> 'Vector3D':
        """
        Project a point to the hyperplane.
        
        Specified by: project in interface Hyperplane
        
        Parameters:
            point (Vector3D): point to project
        
        Returns:
            projected point
        
        
        """
        ...
    @typing.overload
    def reset(self, original: 'Plane') -> None:
        """
        Reset the instance from another one.
        
        The updated instance is completely independant of the original one. A deep reset is used none of the underlying object is shared.
        
        Parameters:
            original (Plane): plane to reset from
        
        
        """
        ...
    @typing.overload
    def reset(self, p: 'Vector3D', normal: 'Vector3D') -> None: ...
    def revertSelf(self) -> None:
        """
        Revert the plane.
        
        Replace the instance by a similar plane with opposite orientation.
        
        The new plane frame is chosen in such a way that a 3D point that had (x, y) in-plane coordinates and z offset with respect to the plane and is unaffected by the change will have (y, x) in-plane coordinates and -z offset with respect to the new plane. This means that the u and v vectors returned by the getU and getV methods are exchanged, and the w vector returned by the getNormal method is reversed.
        """
        ...
    def rotate(self, center: 'Vector3D', rotation: 'Rotation') -> 'Plane':
        """
        Rotate the plane around the specified point.
        
        The instance is not modified, a new instance is created.
        
        Parameters:
            center (Vector3D): rotation center
            rotation (Rotation): vectorial rotation operator
        
        Returns:
            a new plane
        
        
        """
        ...
    def sameOrientationAs(self, other: 'Plane') -> bool:
        """
        Check if the instance has the same orientation as another hyperplane.
        
        Specified by: sameOrientationAs in interface Hyperplane
        
        Parameters:
            other (Plane): other hyperplane to check against the instance
        
        Returns:
            true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def toSpace(self, point: org.hipparchus.geometry.euclidean.twod.Vector2D) -> 'Vector3D':
        """
        Transform an in-plane point into a 3D space point.
        
        Specified by: toSpace in interface Embedding
        
        Parameters:
            point (Vector2D): in-plane point (must be a Vector2D instance)
        
        Returns:
            3D space point (really a Vector3D instance)
        
        Also see:
            toSubSpace
        
        
        """
        ...
    def toSubSpace(self, point: 'Vector3D') -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
        Transform a 3D space point into an in-plane point.
        
        Specified by: toSubSpace in interface Embedding
        
        Parameters:
            point (Vector3D): point of the space (must be a Vector3D instance)
        
        Returns:
            in-plane point (really a Vector2D instance)
        
        Also see:
            toSpace
        
        
        """
        ...
    def translate(self, translation: 'Vector3D') -> 'Plane':
        """
        Translate the plane by the specified amount.
        
        The instance is not modified, a new instance is created.
        
        Parameters:
            translation (Vector3D): translation to apply
        
        Returns:
            a new plane
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubPlane':
        """
        Build a region covering the whole hyperplane.
        
        Specified by: wholeHyperplane in interface Hyperplane
        
        Returns:
            a region covering the whole hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> 'PolyhedronsSet':
        """
        Build a region covering the whole space.
        
        Specified by: wholeSpace in interface Hyperplane
        
        Returns:
            a region containing the instance (really a PolyhedronsSet instance)
        
        
        """
        ...

class PolyhedronsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Euclidean3D, 'Vector3D', Plane, 'SubPlane', org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine]):
    """
    This class represents a 3D region: a set of polyhedrons.
    """
    @typing.overload
    def __init__(self, tolerance: float): ...
    @typing.overload
    def __init__(self, xMin: float, xMax: float, yMin: float, yMax: float, zMin: float, zMax: float, tolerance: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection['SubPlane'], typing.Sequence['SubPlane'], typing.Set['SubPlane']], double: float): ...
    @typing.overload
    def __init__(self, vertices: java.util.List['Vector3D'], facets: java.util.List[typing.Union[typing.List[int], jpype.JArray]], tolerance: float): ...
    @typing.overload
    def __init__(self, bRep: 'PolyhedronsSet.BRep', double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean3D, 'Vector3D', Plane, 'SubPlane'], double: float): ...
    def buildNew(self, tree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean3D, 'Vector3D', Plane, 'SubPlane']) -> 'PolyhedronsSet':
        """
        Build a region using the instance as a prototype.
        
        This method allow to create new instances without knowing exactly the type of the region. It is an application of the prototype design pattern.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Specified by: buildNew in interface Region
        
        Specified by: buildNew in class AbstractRegion
        
        Parameters:
            tree (BSPTree<Euclidean3D, Vector3D, Plane, SubPlane> tree): inside/outside BSP tree representing the new region
        
        Returns:
            the built region
        
        
        """
        ...
    def firstIntersection(self, point: 'Vector3D', line: Line) -> org.hipparchus.geometry.partitioning.SubHyperplane[Euclidean3D, 'Vector3D', Plane, 'SubPlane']:
        """
        Get the first sub-hyperplane crossed by a semi-infinite line.
        
        Parameters:
            point (Vector3D): start point of the part of the line considered
            line (Line): line to consider (contains point)
        
        Returns:
            the first sub-hyperplane crossed by the line after the given point, or null if the line does not intersect any
            sub-hyperplane
        
        
        """
        ...
    def getBRep(self) -> 'PolyhedronsSet.BRep':
        """
        Get the boundary representation of the instance.
        
        The boundary representation can be extracted only from bounded polyhedrons sets. If the polyhedrons set is unbounded, a hipparchus will be thrown.
        
        The boundary representation extracted is not minimal, as for example canonical facets may be split into several smaller independent sub-facets sharing the same plane and connected by their edges.
        
        As the BRep representation does not support facets with several boundary loops (for example facets with holes), an exception is triggered when attempting to extract B-Rep from such complex polyhedrons sets.
        
        Returns:
            boundary representation of the instance
        
        Raises:
            hipparchus: if polyhedrons is unbounded
        
        Since:
            1.2
        
        
        """
        ...
    def getInteriorPoint(self) -> 'Vector3D':
        """
        Get an interior point.
        
        Returns:
            an arbitrary interior point, or null if region is empty
        
        
        """
        ...
    def rotate(self, center: 'Vector3D', rotation: 'Rotation') -> 'PolyhedronsSet':
        """
        Rotate the region around the specified point.
        
        The instance is not modified, a new instance is created.
        
        Parameters:
            center (Vector3D): rotation center
            rotation (Rotation): vectorial rotation operator
        
        Returns:
            a new instance representing the rotated region
        
        
        """
        ...
    def translate(self, translation: 'Vector3D') -> 'PolyhedronsSet':
        """
        Translate the region by the specified amount.
        
        The instance is not modified, a new instance is created.
        
        Parameters:
            translation (Vector3D): translation to apply
        
        Returns:
            a new instance representing the translated region
        
        
        """
        ...
    class BRep:
        def __init__(self, list: java.util.List['Vector3D'], list2: java.util.List[typing.Union[typing.List[int], jpype.JArray]]): ...
        def getFacets(self) -> java.util.List[typing.MutableSequence[int]]: ...
        def getVertices(self) -> java.util.List['Vector3D']: ...

class Rotation(java.io.Serializable):
    """
    This class implements rotations in a three-dimensional space.
    
    Rotations can be represented by several different mathematical entities (matrices, axe and angle, Cardan or Euler angles, quaternions). This class presents an higher level abstraction, more user-oriented and hiding this implementation details. Well, for the curious, we use quaternions for the internal representation. The user can build a rotation from any of these representations, and any of these representations can be retrieved from a Rotation instance (see the various constructors and getters). In addition, a rotation can also be built implicitly from a set of vectors and their image.
    
    This implies that this class can be used to convert from one representation to another one. For example, converting a rotation matrix into a set of Cardan angles from can be done using the following single line of code:
    
    
     double[] angles = new Rotation(matrix, 1.0e-10).getAngles(RotationOrder.XYZ);
     
    
    Focus is oriented on what a rotation do rather than on its underlying representation. Once it has been built, and regardless of its internal representation, a rotation is an operator which basically transforms three dimensional Vector3D into other three dimensional Vector3D. Depending on the application, the meaning of these vectors may vary and the semantics of the rotation also.
    
    For example in an spacecraft attitude simulation tool, users will often consider the vectors are fixed (say the Earth direction for example) and the frames change. The rotation transforms the coordinates of the vector in inertial frame into the coordinates of the same vector in satellite frame. In this case, the rotation implicitly defines the relation between the two frames.
    
    Another example could be a telescope control application, where the rotation would transform the sighting direction at rest into the desired observing direction when the telescope is pointed towards an object of interest. In this case the rotation transforms the direction at rest in a topocentric frame into the sighting direction in the same topocentric frame. This implies in this case the frame is fixed and the vector moves.
    
    In many case, both approaches will be combined. In our telescope example, we will probably also need to transform the observing direction in the topocentric frame into the observing direction in inertial frame taking into account the observatory location and the Earth rotation, which would essentially be an application of the first approach.
    
    These examples show that a rotation is what the user wants it to be. This class does not push the user towards one specific definition and hence does not provide methods like projectVectorIntoDestinationFrame or computeTransformedDirection. It provides simpler and more generic methods: applyTo and applyInverseTo.
    
    Since a rotation is basically a vectorial operator, several rotations can be composed together and the composite operation 1` o r :sub:`2`` (which means that for each vector u, 1` (r :sub:`2` (u))`) is also a rotation. Hence we can consider that in addition to vectors, a rotation can be applied to other rotations as well (or to itself). With our previous notations, we would say we can apply 1`` to 2`` and the result we get is 1` o r :sub:`2``. For this purpose, the class provides the methods: applyTo and applyInverseTo.
    
    Rotations are guaranteed to be immutable objects.
    
    Also see:
        Vector3D,
        RotationOrder, serialized
    """
    IDENTITY: typing.ClassVar['Rotation'] = ...
    """
    Identity rotation.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, boolean: bool): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float): ...
    @typing.overload
    def __init__(self, rotationOrder: 'RotationOrder', rotationConvention: 'RotationConvention', double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, axis: 'Vector3D', angle: float, convention: 'RotationConvention'): ...
    @typing.overload
    def __init__(self, vector3D: 'Vector3D', vector3D2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, u1: 'Vector3D', u2: 'Vector3D', v1: 'Vector3D', v2: 'Vector3D'): ...
    @typing.overload
    def applyInverseTo(self, u: 'Rotation') -> 'Rotation':
        """
        Apply the inverse of the rotation to a vector.
        
        Parameters:
            u (Vector3D): vector to apply the inverse of the rotation to
        
        Returns:
            a new vector which such that u is its image by the rotation
        
        Apply the inverse of the instance to another rotation.
        
        Calling this method is equivalent to call composeInverse.
        
        Parameters:
            r (Rotation): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the inverse of the instance
        
        
        """
        ...
    @typing.overload
    def applyInverseTo(self, vector3D: 'Vector3D') -> 'Vector3D': ...
    @typing.overload
    def applyInverseTo(self, in_: typing.Union[typing.List[float], jpype.JArray], out: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Apply the inverse of the rotation to a vector stored in an array.
        
        Parameters:
            in (double[]): an array with three items which stores vector to rotate
            out (double[]): an array with three items to put result to (it can be the same array as in)
        
        """
        ...
    @typing.overload
    def applyTo(self, u: 'Rotation') -> 'Rotation':
        """
        Apply the rotation to a vector.
        
        Parameters:
            u (Vector3D): vector to apply the rotation to
        
        Returns:
            a new vector which is the image of u by the rotation
        
        Apply the instance to another rotation.
        
        Calling this method is equivalent to call compose.
        
        Parameters:
            r (Rotation): rotation to apply the rotation to
        
        Returns:
            a new rotation which is the composition of r by the instance
        
        
        """
        ...
    @typing.overload
    def applyTo(self, vector3D: 'Vector3D') -> 'Vector3D': ...
    @typing.overload
    def applyTo(self, in_: typing.Union[typing.List[float], jpype.JArray], out: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Apply the rotation to a vector stored in an array.
        
        Parameters:
            in (double[]): an array with three items which stores vector to rotate
            out (double[]): an array with three items to put result to (it can be the same array as in)
        
        """
        ...
    def compose(self, r: 'Rotation', convention: 'RotationConvention') -> 'Rotation':
        """
        Compose the instance with another rotation.
        
        If the semantics of the rotations composition corresponds to a VECTOR_OPERATOR convention, applying the instance to a rotation is computing the composition in an order compliant with the following rule : let u be any vector and v its image by r1 (i.e. applyTo(u) = v). Let w be the image of v by rotation r2 (i.e. applyTo(v) = w). Then applyTo(u), where VECTOR_OPERATOR).
        
        If the semantics of the rotations composition corresponds to a FRAME_TRANSFORM convention, the application order will be reversed. So keeping the exact same meaning of all r1, r2, u, v, w and comp as above, comp could also be computed as FRAME_TRANSFORM).
        
        Parameters:
            r (Rotation): rotation to apply the rotation to
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            a new rotation which is the composition of r by the instance
        
        
        """
        ...
    def composeInverse(self, r: 'Rotation', convention: 'RotationConvention') -> 'Rotation':
        """
        Compose the inverse of the instance with another rotation.
        
        If the semantics of the rotations composition corresponds to a VECTOR_OPERATOR convention, applying the inverse of the instance to a rotation is computing the composition in an order compliant with the following rule : let u be any vector and v its image by r1 (i.e. applyTo(u) = v). Let w be the inverse image of v by r2 (i.e. applyInverseTo(v) = w). Then applyTo(u), where composeInverse(r1).
        
        If the semantics of the rotations composition corresponds to a FRAME_TRANSFORM convention, the application order will be reversed, which means it is the innermost rotation that will be reversed. So keeping the exact same meaning of all r1, r2, u, v, w and comp as above, comp could also be computed as FRAME_TRANSFORM).
        
        Parameters:
            r (Rotation): rotation to apply the rotation to
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            a new rotation which is the composition of r by the inverse of the instance
        
        
        """
        ...
    @staticmethod
    def distance(r1: 'Rotation', r2: 'Rotation') -> float:
        """
        Compute the distance between two rotations.
        
        The distance is intended here as a way to check if two rotations are almost similar (i.e. they transform vectors the same way) or very different. It is mathematically defined as the angle of the rotation r that prepended to one of the rotations gives the other one: \(r_1(r) = r_2\)
        
        This distance is an angle between 0 and π. Its value is the smallest possible upper bound of the angle in radians between r :sub:`1` (v) and r :sub:`2` (v) for all possible vectors v. This upper bound is reached for some v. The distance is equal to 0 if and only if the two rotations are identical.
        
        Comparing two rotations should always be done using this value rather than for example comparing the components of the quaternions. It is much more stable, and has a geometric meaning. Also comparing quaternions components is error prone since for example quaternions (0.36, 0.48, -0.48, -0.64) and (-0.36, -0.48, 0.48, 0.64) represent exactly the same rotation despite their components are different (they are exact opposites).
        
        Parameters:
            r1 (Rotation): first rotation
            r2 (Rotation): second rotation
        
        Returns:
            distance between r1 and r2
        
        
        """
        ...
    def getAngle(self) -> float:
        """
        Get the angle of the rotation.
        
        Returns:
            angle of the rotation (between 0 and π)
        
        
        """
        ...
    def getAngles(self, order: 'RotationOrder', convention: 'RotationConvention') -> typing.MutableSequence[float]:
        """
        Get the Cardan or Euler angles corresponding to the instance.
        
        The equations show that each rotation can be defined by two different values of the Cardan or Euler angles set. For example if Cardan angles are used, the rotation defined by the angles a :sub:`1` , a :sub:`2` and a :sub:`3` is the same as the rotation defined by the angles π + a :sub:`1` , π - a :sub:`2` and π + a :sub:`3` . This method implements the following arbitrary choices:
        
          - for Cardan angles, the chosen set is the one for which the second angle is between -π/2 and π/2 (i.e its cosine is
            positive),
          - for Euler angles, the chosen set is the one for which the second angle is between 0 and π (i.e its sine is positive).
        
        The algorithm used here works even when the rotation is exactly at the the singularity of the rotation order and convention. In this case, one of the angles in the singular pair is arbitrarily set to exactly 0 and the second angle is computed. The angle set to 0 in the singular case is the angle of the first rotation in the case of Cardan orders, and it is the angle of the last rotation in the case of Euler orders. This implies that extracting the angles of a rotation never fails (it used to trigger an exception in singular cases up to Hipparchus 3.0).
        
        Parameters:
            order (RotationOrder): rotation order to use
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            an array of three angles, in the order specified by the set
        
        
        """
        ...
    def getAxis(self, convention: 'RotationConvention') -> 'Vector3D':
        """
        Get the normalized axis of the rotation.
        
        Note that as getAngle always returns an angle between 0 and π, changing the convention changes the direction of the axis, not the sign of the angle.
        
        Parameters:
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            normalized axis of the rotation
        
        
        """
        ...
    def getMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the 3X3 matrix corresponding to the instance
        
        Returns:
            the matrix corresponding to the instance
        
        
        """
        ...
    def getQ0(self) -> float:
        """
        Get the scalar coordinate of the quaternion.
        
        Returns:
            scalar coordinate of the quaternion
        
        
        """
        ...
    def getQ1(self) -> float:
        """
        Get the first coordinate of the vectorial part of the quaternion.
        
        Returns:
            first coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def getQ2(self) -> float:
        """
        Get the second coordinate of the vectorial part of the quaternion.
        
        Returns:
            second coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def getQ3(self) -> float:
        """
        Get the third coordinate of the vectorial part of the quaternion.
        
        Returns:
            third coordinate of the vectorial part of the quaternion
        
        
        """
        ...
    def revert(self) -> 'Rotation':
        """
        Revert a rotation. Build a rotation which reverse the effect of another rotation. This means that if r(u) = v, then r.revert(v) = u. The instance is not changed.
        
        Returns:
            a new rotation whose effect is the reverse of the effect of the instance
        
        
        """
        ...

class RotationConvention(java.lang.Enum['RotationConvention']):
    """
    This enumerates is used to differentiate the semantics of a rotation.
    
    Also see:
        Rotation
    """
    VECTOR_OPERATOR: typing.ClassVar['RotationConvention'] = ...
    FRAME_TRANSFORM: typing.ClassVar['RotationConvention'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'RotationConvention':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['RotationConvention']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RotationConvention c : RotationConvention.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RotationOrder(java.lang.Enum['RotationOrder']):
    """
    Enumerate representing a rotation order specification for Cardan or Euler angles.
    
    Since Hipparchus 1.7 this class is an enumerate class.
    """
    XYZ: typing.ClassVar['RotationOrder'] = ...
    XZY: typing.ClassVar['RotationOrder'] = ...
    YXZ: typing.ClassVar['RotationOrder'] = ...
    YZX: typing.ClassVar['RotationOrder'] = ...
    ZXY: typing.ClassVar['RotationOrder'] = ...
    ZYX: typing.ClassVar['RotationOrder'] = ...
    XYX: typing.ClassVar['RotationOrder'] = ...
    XZX: typing.ClassVar['RotationOrder'] = ...
    YXY: typing.ClassVar['RotationOrder'] = ...
    YZY: typing.ClassVar['RotationOrder'] = ...
    ZXZ: typing.ClassVar['RotationOrder'] = ...
    ZYZ: typing.ClassVar['RotationOrder'] = ...
    def getA1(self) -> 'Vector3D':
        """
        Get the axis of the first rotation.
        
        Returns:
            axis of the first rotation
        
        
        """
        ...
    def getA2(self) -> 'Vector3D':
        """
        Get the axis of the second rotation.
        
        Returns:
            axis of the second rotation
        
        
        """
        ...
    def getA3(self) -> 'Vector3D':
        """
        Get the axis of the third rotation.
        
        Returns:
            axis of the third rotation
        
        
        """
        ...
    _getAngles_1__T = typing.TypeVar('_getAngles_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAngles(self, rotation: Rotation, convention: RotationConvention) -> typing.MutableSequence[float]:
        """
        Get the Cardan or Euler angles corresponding to the instance.
        
        The algorithm used here works even when the rotation is exactly at the the singularity of the rotation order and convention. In this case, one of the angles in the singular pair is arbitrarily set to exactly 0 and the second angle is computed. The angle set to 0 in the singular case is the angle of the first rotation in the case of Cardan orders, and it is the angle of the last rotation in the case of Euler orders. This implies that extracting the angles of a rotation never fails (it used to trigger an exception in singular cases up to Hipparchus 3.0).
        
        Parameters:
            rotation (Rotation): rotation from which angles should be extracted
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            an array of three angles, in the order specified by the set
        
        Since:
            3.1
        
        """
        ...
    @typing.overload
    def getAngles(self, rotation: FieldRotation[_getAngles_1__T], convention: RotationConvention) -> typing.MutableSequence[_getAngles_1__T]:
        """
        Get the Cardan or Euler angles corresponding to the instance.
        
        The algorithm used here works even when the rotation is exactly at the the singularity of the rotation order and convention. In this case, one of the angles in the singular pair is arbitrarily set to exactly 0 and the second angle is computed. The angle set to 0 in the singular case is the angle of the first rotation in the case of Cardan orders, and it is the angle of the last rotation in the case of Euler orders. This implies that extracting the angles of a rotation never fails (it used to trigger an exception in singular cases up to Hipparchus 3.0).
        
        Parameters:
            rotation (FieldRotation<T> rotation): rotation from which angles should be extracted
            convention (RotationConvention): convention to use for the semantics of the angle
        
        Returns:
            an array of three angles, in the order specified by the set
        
        Since:
            3.1
        
        
        """
        ...
    @staticmethod
    def getRotationOrder(value: str) -> 'RotationOrder':
        """
        Get the rotation order corresponding to a string representation.
        
        Parameters:
            value (String): name
        
        Returns:
            a rotation order object
        
        Since:
            1.7
        
        
        """
        ...
    def toString(self) -> str:
        """
        Get a string representation of the instance.
        
        Overrides: Enum in class Enum
        
        Returns:
            a string representation of the instance (in fact, its name)
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'RotationOrder':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['RotationOrder']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RotationOrder c : RotationOrder.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Segment:
    """
    Simple container for a two-points segment.
    """
    def __init__(self, start: 'Vector3D', end: 'Vector3D', line: Line):
        """
        Build a segment.
        
        Parameters:
            start (Vector3D): start point of the segment
            end (Vector3D): end point of the segment
            line (Line): line containing the segment
        
        
        """
        ...
    def getEnd(self) -> 'Vector3D':
        """
        Get the end point of the segment.
        
        Returns:
            end point of the segment
        
        
        """
        ...
    def getLine(self) -> Line:
        """
        Get the line containing the segment.
        
        Returns:
            line containing the segment
        
        
        """
        ...
    def getStart(self) -> 'Vector3D':
        """
        Get the start point of the segment.
        
        Returns:
            start point of the segment
        
        
        """
        ...

class SphereGenerator(org.hipparchus.geometry.enclosing.SupportBallGenerator[Euclidean3D, 'Vector3D']):
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
    def ballOnSupport(self, support: java.util.List['Vector3D']) -> org.hipparchus.geometry.enclosing.EnclosingBall[Euclidean3D, 'Vector3D']:
        """
        Create a ball whose boundary lies on prescribed support points.
        
        Specified by: ballOnSupport in interface SupportBallGenerator
        
        Parameters:
            support (List<Vector3D> support): support points (may be empty)
        
        Returns:
            ball whose boundary lies on the prescribed support points
        
        
        """
        ...

class SphericalCoordinates(java.io.Serializable):
    """
    This class provides conversions related to `spherical coordinates <http://mathworld.wolfram.com/SphericalCoordinates.html>`.
    
    The conventions used here are the mathematical ones, i.e. spherical coordinates are related to Cartesian coordinates as follows:
    
      - x = r cos(θ) sin(Φ)
      - y = r sin(θ) sin(Φ)
      - z = r cos(Φ)
    
    
      - r = √(x :sup:`2` +y :sup:`2` +z :sup:`2` )
      - θ = atan2(y, x)
      - Φ = acos(z/r)
    
    r is the radius, θ is the azimuthal angle in the x-y plane and Φ is the polar (co-latitude) angle. These conventions are different from the conventions used in physics (and in particular in spherical harmonics) where the meanings of θ and Φ are reversed.
    
    This class provides conversion of coordinates and also of gradient and Hessian between spherical and Cartesian coordinates.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, r: float, theta: float, phi: float): ...
    @typing.overload
    def __init__(self, v: 'Vector3D'): ...
    def getCartesian(self) -> 'Vector3D':
        """
        Get the Cartesian coordinates.
        
        Returns:
            Cartesian coordinates
        
        
        """
        ...
    def getPhi(self) -> float:
        """
        Get the polar (co-latitude) angle.
        
        Returns:
            polar (co-latitude) angle Φ
        
        Also see:
            getR,
            getTheta
        
        
        """
        ...
    def getR(self) -> float:
        """
        Get the radius.
        
        Returns:
            radius r
        
        Also see:
            getTheta,
            getPhi
        
        
        """
        ...
    def getTheta(self) -> float:
        """
        Get the azimuthal angle in x-y plane.
        
        Returns:
            azimuthal angle in x-y plane θ
        
        Also see:
            getR,
            getPhi
        
        
        """
        ...
    def toCartesianGradient(self, sGradient: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Convert a gradient with respect to spherical coordinates into a gradient with respect to Cartesian coordinates.
        
        Parameters:
            sGradient (double[]): gradient with respect to spherical coordinates {df/dr, df/dθ, df/dΦ}
        
        Returns:
            gradient with respect to Cartesian coordinates {df/dx, df/dy, df/dz}
        
        
        """
        ...
    def toCartesianHessian(self, sHessian: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], sGradient: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Convert a Hessian with respect to spherical coordinates into a Hessian with respect to Cartesian coordinates.
        
        As Hessian are always symmetric, we use only the lower left part of the provided spherical Hessian, so the upper part may not be initialized. However, we still do fill up the complete array we create, with guaranteed symmetry.
        
        Parameters:
            sHessian (double[][]): Hessian with respect to spherical coordinates {{d :sup:`2` f/dr :sup:`2` , d :sup:`2` f/drdθ, d :sup:`2` f/drdΦ}, {d
                :sup:`2` f/drdθ, d :sup:`2` f/dθ :sup:`2` , d :sup:`2` f/dθdΦ}, {d :sup:`2` f/drdΦ, d :sup:`2` f/dθdΦ, d :sup:`2`
                f/dΦ :sup:`2` }
            sGradient (double[]): gradient with respect to spherical coordinates {df/dr, df/dθ, df/dΦ}
        
        Returns:
            Hessian with respect to Cartesian coordinates {{d :sup:`2` f/dx :sup:`2` , d :sup:`2` f/dxdy, d :sup:`2` f/dxdz}, {d
            :sup:`2` f/dxdy, d :sup:`2` f/dy :sup:`2` , d :sup:`2` f/dydz}, {d :sup:`2` f/dxdz, d :sup:`2` f/dydz, d :sup:`2` f/dz
            :sup:`2` }}
        
        
        """
        ...

class SubLine:
    """
    This class represents a subset of a Line.
    """
    @typing.overload
    def __init__(self, line: Line, remainingRegion: org.hipparchus.geometry.euclidean.oned.IntervalsSet): ...
    @typing.overload
    def __init__(self, segment: Segment): ...
    @typing.overload
    def __init__(self, start: 'Vector3D', end: 'Vector3D', tolerance: float): ...
    def getSegments(self) -> java.util.List[Segment]:
        """
        Get the endpoints of the sub-line.
        
        A subline may be any arbitrary number of disjoints segments, so the endpoints are provided as a list of endpoint pairs. Each element of the list represents one segment, and each segment contains a start point at index 0 and an end point at index 1. If the sub-line is unbounded in the negative infinity direction, the start point of the first segment will have infinite coordinates. If the sub-line is unbounded in the positive infinity direction, the end point of the last segment will have infinite coordinates. So a sub-line covering the whole line will contain just one row and both elements of this row will have infinite coordinates. If the sub-line is empty, the returned list will contain 0 segments.
        
        Returns:
            list of segments endpoints
        
        
        """
        ...
    def intersection(self, subLine: 'SubLine', includeEndPoints: bool) -> 'Vector3D':
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

class SubPlane(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Euclidean3D, 'Vector3D', Plane, 'SubPlane', org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine]):
    """
    This class represents a sub-hyperplane for Plane.
    """
    def __init__(self, hyperplane: Plane, remainingRegion: org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine]):
        """
        Simple constructor.
        
        Parameters:
            hyperplane (Plane): underlying hyperplane
            remainingRegion (Region<Euclidean2D, Vector2D, Line, SubLine> remainingRegion): remaining region of the hyperplane
        
        
        """
        ...
    def getInteriorPoint(self) -> 'Vector3D':
        """
        Get an interior point.
        
        Returns:
            an arbitrary interior point, or null if sub-hyperplane is empty
        
        
        """
        ...
    def split(self, hyperplane: Plane) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean3D, 'Vector3D', Plane, 'SubPlane']:
        """
        Split the instance in two parts by an hyperplane.
        
        Specified by: split in interface SubHyperplane
        
        Specified by: split in class AbstractSubHyperplane
        
        Parameters:
            hyperplane (Plane): splitting hyperplane
        
        Returns:
            an object containing both the part of the instance on the plus side of the instance and the part of the instance on the
            minus side of the instance
        
        
        """
        ...

class Vector3D(java.io.Serializable, org.hipparchus.geometry.Vector[Euclidean3D, 'Vector3D']):
    """
    This class implements vectors in a three-dimensional space.
    
    Instance of this class are guaranteed to be immutable.
    
    Also see:
        serialized
    """
    ZERO: typing.ClassVar['Vector3D'] = ...
    """
    Null vector (coordinates: 0, 0, 0).
    """
    PLUS_I: typing.ClassVar['Vector3D'] = ...
    """
    First canonical vector (coordinates: 1, 0, 0).
    """
    MINUS_I: typing.ClassVar['Vector3D'] = ...
    """
    Opposite of the first canonical vector (coordinates: -1, 0, 0).
    """
    PLUS_J: typing.ClassVar['Vector3D'] = ...
    """
    Second canonical vector (coordinates: 0, 1, 0).
    """
    MINUS_J: typing.ClassVar['Vector3D'] = ...
    """
    Opposite of the second canonical vector (coordinates: 0, -1, 0).
    """
    PLUS_K: typing.ClassVar['Vector3D'] = ...
    """
    Third canonical vector (coordinates: 0, 0, 1).
    """
    MINUS_K: typing.ClassVar['Vector3D'] = ...
    """
    Opposite of the third canonical vector (coordinates: 0, 0, -1).
    """
    NaN: typing.ClassVar['Vector3D'] = ...
    """
    A vector with all coordinates set to NaN.
    """
    POSITIVE_INFINITY: typing.ClassVar['Vector3D'] = ...
    """
    A vector with all coordinates set to positive infinity.
    """
    NEGATIVE_INFINITY: typing.ClassVar['Vector3D'] = ...
    """
    A vector with all coordinates set to negative infinity.
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, x: float, y: float, z: float): ...
    @typing.overload
    def __init__(self, double: float, vector3D: 'Vector3D'): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'Vector3D', a2: float, u2: 'Vector3D'): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'Vector3D', a2: float, u2: 'Vector3D', a3: float, u3: 'Vector3D'): ...
    @typing.overload
    def __init__(self, a1: float, u1: 'Vector3D', a2: float, u2: 'Vector3D', a3: float, u3: 'Vector3D', a4: float, u4: 'Vector3D'): ...
    @typing.overload
    def __init__(self, v: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def add(self, factor: float, v: 'Vector3D') -> 'Vector3D':
        """
        Add a scaled vector to the instance.
        
        Specified by: add in interface Vector
        
        Parameters:
            factor (double): scale factor to apply to v before adding it
            v (Vector3D): vector to add
        
        Returns:
            a new vector
        
        
        """
        ...
    @typing.overload
    def add(self, v: 'Vector3D') -> 'Vector3D':
        """
        Add a vector to the instance.
        
        Specified by: add in interface Vector
        
        Parameters:
            v (Vector3D): vector to add
        
        Returns:
            a new vector
        
        """
        ...
    @staticmethod
    def angle(v1: 'Vector3D', v2: 'Vector3D') -> float:
        """
        Compute the angular separation between two vectors.
        
        This method computes the angular separation between two vectors using the dot product for well separated vectors and the cross product for almost aligned vectors. This allows to have a good accuracy in all cases, even for vectors very close to each other.
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (Vector3D): second vector
        
        Returns:
            angular separation between v1 and v2
        
        Raises:
            hipparchus: if either vector has a null norm
        
        
        """
        ...
    @typing.overload
    def crossProduct(self, v: 'Vector3D') -> 'Vector3D':
        """
        Compute the cross-product of the instance with another vector.
        
        Parameters:
            v (Vector3D): other vector
        
        Returns:
            the cross product this ^ v as a new Vector3D
        
        Compute the cross-product of two vectors.
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the cross product v1 ^ v2 as a new Vector
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def crossProduct(v1: 'Vector3D', v2: 'Vector3D') -> 'Vector3D': ...
    @typing.overload
    def distance(self, v: 'Vector3D') -> float:
        """
        Compute the distance between the instance and another point.
        
        Specified by: distance in interface Point
        
        Parameters:
            v (Vector3D): second point
        
        Returns:
            the distance between the instance and p
        
        Compute the distance between two vectors according to the L :sub:`2` norm.
        
        Calling this method is equivalent to calling: getNorm() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`2` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(v1: 'Vector3D', v2: 'Vector3D') -> float: ...
    @typing.overload
    def distance1(self, v: 'Vector3D') -> float:
        """
        Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Specified by: distance1 in interface Vector
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`1` norm
        
        Compute the distance between two vectors according to the L :sub:`1` norm.
        
        Calling this method is equivalent to calling: getNorm1() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`1` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance1(v1: 'Vector3D', v2: 'Vector3D') -> float: ...
    @typing.overload
    def distanceInf(self, v: 'Vector3D') -> float:
        """
        Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Specified by: distanceInf in interface Vector
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the distance between the instance and p according to the L :sub:`∞` norm
        
        Compute the distance between two vectors according to the L :sub:`∞` norm.
        
        Calling this method is equivalent to calling: getNormInf() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the distance between v1 and v2 according to the L :sub:`∞` norm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceInf(v1: 'Vector3D', v2: 'Vector3D') -> float: ...
    @typing.overload
    def distanceSq(self, v: 'Vector3D') -> float:
        """
        Compute the square of the distance between the instance and another vector.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Specified by: distanceSq in interface Vector
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the square of the distance between the instance and p
        
        Compute the square of the distance between two vectors.
        
        Calling this method is equivalent to calling: getNormSq() except that no intermediate vector is built
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the square of the distance between v1 and v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distanceSq(v1: 'Vector3D', v2: 'Vector3D') -> float: ...
    @typing.overload
    def dotProduct(self, v: 'Vector3D') -> float:
        """
        Compute the dot-product of the instance and another vector.
        
        The implementation uses specific multiplication and addition algorithms to preserve accuracy and reduce cancellation effects. It should be very accurate even for nearly orthogonal vectors.
        
        Specified by: dotProduct in interface Vector
        
        Parameters:
            v (Vector3D): second vector
        
        Returns:
            the dot product this.v
        
        Also see:
            hipparchus
        
        Compute the dot-product of two vectors.
        
        Parameters:
            v1 (Vector3D): first vector
            v2 (Vector3D): second vector
        
        Returns:
            the dot product v1.v2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def dotProduct(v1: 'Vector3D', v2: 'Vector3D') -> float: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 3D vectors.
        
        If all coordinates of two 3D vectors are exactly the same, and none are NaN, the two 3D vectors are considered to be equal.
        
        NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) coordinates of the 3D vector are equal to NaN, the 3D vector is equal to NaN.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 3D vector objects are equal, false if object is null, not an instance of Vector3D, or not equal to this
            Vector3D instance
        
        
        """
        ...
    def equalsIeee754(self, other: typing.Any) -> bool:
        """
        Test for the equality of two 3D vectors.
        
        If all coordinates of two 3D vectors are exactly the same, and none are NaN, the two 3D vectors are considered to be equal.
        
        In compliance with IEEE754 handling, if any coordinates of any of the two vectors are NaN, then the vectors are considered different. This implies that NaN.equals(NaN) returns false despite the instance is checked against itself.
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two 3D vector objects are equal, false if object is null, not an instance of Vector3D, or not equal to this
            Vector3D instance
        
        Since:
            2.1
        
        
        """
        ...
    def getAlpha(self) -> float:
        """
        Get the azimuth of the vector.
        
        Returns:
            azimuth (α) of the vector, between -π and +π
        
        
        """
        ...
    def getDelta(self) -> float:
        """
        Get the elevation of the vector.
        
        Returns:
            elevation (δ) of the vector, between -π/2 and +π/2
        
        
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
    def getZ(self) -> float:
        """
        Get the height of the vector.
        
        Returns:
            height of the vector
        
        
        """
        ...
    def getZero(self) -> 'Vector3D':
        """
        Get the null vector of the vectorial space or origin point of the affine space.
        
        Specified by: getZero in interface Vector
        
        Returns:
            null vector of the vectorial space or origin point of the affine space
        
        
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
    def moveTowards(self, other: 'Vector3D', ratio: float) -> 'Vector3D':
        """
        Move towards another point.
        
        Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
        Specified by: moveTowards in interface Point
        
        Parameters:
            other (Vector3D): other point
            ratio (double): motion ratio,
        
        Returns:
            moved point
        
        
        """
        ...
    def negate(self) -> 'Vector3D':
        """
        Get the opposite of the instance.
        
        Specified by: negate in interface Vector
        
        Returns:
            a new vector which is opposite to the instance
        
        
        """
        ...
    def orthogonal(self) -> 'Vector3D':
        """
        Get a vector orthogonal to the instance.
        
        There are an infinite number of normalized vectors orthogonal to the instance. This method picks up one of them almost arbitrarily. It is useful when one needs to compute a reference frame with one of the axes in a predefined direction. The following example shows how to build a frame having the k axis aligned with the known vector u :
        
        
           Vector3D k = u.normalize();
           Vector3D i = k.orthogonal();
           Vector3D j = Vector3D.crossProduct(k, i);
         
        
        Returns:
            a new normalized vector orthogonal to the instance
        
        Raises:
            hipparchus: if the norm of the instance is null
        
        
        """
        ...
    def scalarMultiply(self, a: float) -> 'Vector3D':
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
    def subtract(self, factor: float, v: 'Vector3D') -> 'Vector3D':
        """
        Subtract a scaled vector from the instance.
        
        Specified by: subtract in interface Vector
        
        Parameters:
            factor (double): scale factor to apply to v before subtracting it
            v (Vector3D): vector to subtract
        
        Returns:
            a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, v: 'Vector3D') -> 'Vector3D':
        """
        Subtract a vector from the instance.
        
        Specified by: subtract in interface Vector
        
        Parameters:
            v (Vector3D): vector to subtract
        
        Returns:
            a new vector
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Get the vector coordinates as a dimension 3 array.
        
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

class Vector3DFormat(org.hipparchus.geometry.VectorFormat[Euclidean3D, Vector3D]):
    """
    Formats a 3D vector in components list format "{x; y; z}".
    
    The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format for components can be configured.
    
    White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the default separator does include a space character that is used at format time, both input string "{1;1;1}" and " { 1 ; 1 ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
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
    def format(self, vector: org.hipparchus.geometry.Vector[Euclidean3D, Vector3D], toAppendTo: java.lang.StringBuffer, pos: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def getVector3DFormat() -> 'Vector3DFormat':
        """
        Returns:
            the default 3D vector format.
        
        Since:
            1.4
        
        """
        ...
    @typing.overload
    @staticmethod
    def getVector3DFormat(locale: java.util.Locale) -> 'Vector3DFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the 3D vector format specific to the given locale.
        
        Since:
            1.4
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str) -> Vector3D:
        """
        Parses a string to produce a Vector3D object.
        
        Specified by: parse in class VectorFormat
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/ouput parsing parameter.
        
        Returns:
            the parsed Vector3D object.
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str, pos: java.text.ParsePosition) -> Vector3D: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.threed")``.

    Euclidean3D: typing.Type[Euclidean3D]
    FieldLine: typing.Type[FieldLine]
    FieldRotation: typing.Type[FieldRotation]
    FieldVector3D: typing.Type[FieldVector3D]
    Line: typing.Type[Line]
    OutlineExtractor: typing.Type[OutlineExtractor]
    Plane: typing.Type[Plane]
    PolyhedronsSet: typing.Type[PolyhedronsSet]
    Rotation: typing.Type[Rotation]
    RotationConvention: typing.Type[RotationConvention]
    RotationOrder: typing.Type[RotationOrder]
    Segment: typing.Type[Segment]
    SphereGenerator: typing.Type[SphereGenerator]
    SphericalCoordinates: typing.Type[SphericalCoordinates]
    SubLine: typing.Type[SubLine]
    SubPlane: typing.Type[SubPlane]
    Vector3D: typing.Type[Vector3D]
    Vector3DFormat: typing.Type[Vector3DFormat]
