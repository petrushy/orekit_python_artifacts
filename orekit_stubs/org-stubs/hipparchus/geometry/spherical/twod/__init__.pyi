
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import org.hipparchus.geometry
import org.hipparchus.geometry.enclosing
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.partitioning
import org.hipparchus.geometry.spherical.oned
import typing



class Circle(org.hipparchus.geometry.partitioning.Hyperplane['Sphere2D', 'S2Point', 'Circle', 'SubCircle'], org.hipparchus.geometry.partitioning.Embedding['Sphere2D', 'S2Point', org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point]):
    """
    public classCircle extends :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<:class:`~org.hipparchus.geometry.spherical.twod.Sphere2D`,:class:`~org.hipparchus.geometry.spherical.twod.S2Point`,:class:`~org.hipparchus.geometry.spherical.twod.Circle`,:class:`~org.hipparchus.geometry.spherical.twod.SubCircle`>, :class:`~org.hipparchus.geometry.partitioning.Embedding`<:class:`~org.hipparchus.geometry.spherical.twod.Sphere2D`,:class:`~org.hipparchus.geometry.spherical.twod.S2Point`,:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`>
    
        This class represents an oriented great circle on the 2-sphere.
    
        An oriented circle can be defined by a center point. The circle is the set of points that are in the normal plan the
        center.
    
        Since it is oriented the two spherical caps at its two sides are unambiguously identified as a left cap and a right cap.
        This can be used to identify the interior and the exterior in a simple way by local properties only when part of a line
        is used to define part of a spherical polygon boundary.
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    @typing.overload
    def __init__(self, circle: 'Circle'): ...
    @typing.overload
    def __init__(self, s2Point: 'S2Point', s2Point2: 'S2Point', double: float): ...
    def arbitraryPoint(self) -> 'S2Point':
        """
            Get an arbitrary point in the hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.arbitraryPoint` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                arbirary point in the hyperplane
        
        
        """
        ...
    def copySelf(self) -> 'Circle':
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
    def emptyHyperplane(self) -> 'SubCircle':
        """
            Build a sub-hyperplane covering nothing.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.emptyHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a sub-hyperplane covering nothing
        
        
        """
        ...
    def getArc(self, s2Point: 'S2Point', s2Point2: 'S2Point') -> org.hipparchus.geometry.spherical.oned.Arc:
        """
            Get the arc on this circle between two defining points. Only the point's projection on the circle matters, which is
            computed using :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPhase`.
        
            Parameters:
                a (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): first point.
                b (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): second point.
        
            Returns:
                an arc of the circle.
        
        
        """
        ...
    def getInsideArc(self, circle: 'Circle') -> org.hipparchus.geometry.spherical.oned.Arc:
        """
            Get the arc of the instance that lies inside the other circle.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.twod.Circle`): other circle
        
            Returns:
                arc of the instance that lies inside the other circle
        
        
        """
        ...
    @typing.overload
    def getOffset(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
            Get the offset (oriented distance) of a point.
        
            The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of
            the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.getOffset` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): point to check
        
            Returns:
                offset of the point
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getOffset`
        
        
            Get the offset (oriented distance) of a direction.
        
            The offset is defined as the angular distance between the circle center and the direction minus the circle radius. It is
            therefore 0 on the circle, positive for directions outside of the cone delimited by the circle, and negative inside the
            cone.
        
            Parameters:
                direction (:class:`~org.hipparchus.geometry.euclidean.threed.Vector3D`): direction to check
        
            Returns:
                offset of the direction
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getOffset`
        
        
        
        """
        ...
    @typing.overload
    def getOffset(self, s2Point: 'S2Point') -> float: ...
    def getPhase(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
            Get the phase angle of a direction.
        
            The direction may not belong to the circle as the phase is computed for the meridian plane between the circle pole and
            the direction.
        
            Parameters:
                direction (:class:`~org.hipparchus.geometry.euclidean.threed.Vector3D`): direction for which phase is requested
        
            Returns:
                phase angle of the direction around the circle
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.toSubSpace`
        
        
        
        """
        ...
    def getPointAt(self, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get a circle point from its phase around the circle.
        
            Parameters:
                alpha (double): phase around the circle
        
            Returns:
                circle point on the sphere
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.toSpace`
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getXAxis`
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getYAxis`
        
        
        
        """
        ...
    def getPole(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the pole of the circle.
        
            As the circle is a great circle, the pole does *not* belong to it.
        
            Returns:
                pole of the circle
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getXAxis`
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getYAxis`
        
        
        
        """
        ...
    def getReverse(self) -> 'Circle':
        """
            Get the reverse of the instance.
        
            Get a circle with reversed orientation with respect to the instance. A new object is built, the instance is untouched.
        
            Returns:
                a new circle, with orientation opposite to the instance orientation
        
        
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
    def getTransform(rotation: org.hipparchus.geometry.euclidean.threed.Rotation) -> org.hipparchus.geometry.partitioning.Transform['Sphere2D', 'S2Point', 'Circle', 'SubCircle', org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]: ...
    def getXAxis(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the X axis of the circle.
        
            This method returns the same value as :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPointAt` but it does not
            do any computation and always return the same instance.
        
            Returns:
                an arbitrary x axis on the circle
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPointAt`
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getYAxis`
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPole`
        
        
        
        """
        ...
    def getYAxis(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the Y axis of the circle.
        
            This method returns the same value as :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPointAt` but it does not
            do any computation and always return the same instance.
        
            Returns:
                an arbitrary y axis point on the circle
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPointAt`
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getXAxis`
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPole`
        
        
        
        """
        ...
    def moveToOffset(self, s2Point: 'S2Point', double: float) -> 'S2Point':
        """
            Move point up to specified offset.
        
            Motion is *orthogonal* to the hyperplane
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.moveToOffset` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): point to move
                offset (double): desired offset
        
            Returns:
                moved point at desired offset
        
        
        """
        ...
    def project(self, s2Point: 'S2Point') -> 'S2Point':
        """
            Project a point to the hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.project` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): point to project
        
            Returns:
                projected point
        
        
        """
        ...
    def reset(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Reset the instance as if built from a pole.
        
            The circle is oriented in the trigonometric direction around pole.
        
            Parameters:
                newPole (:class:`~org.hipparchus.geometry.euclidean.threed.Vector3D`): circle pole
        
        
        """
        ...
    def revertSelf(self) -> None:
        """
            Revert the instance.
        
        """
        ...
    def sameOrientationAs(self, circle: 'Circle') -> bool:
        """
            Check if the instance has the same orientation as another hyperplane.
        
            This method is expected to be called on parallel hyperplanes. The method should *not* re-check for parallelism, only for
            orientation, typically by testing something like the sign of the dot-products of normals.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.sameOrientationAs` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.twod.Circle`): other hyperplane to check against the instance
        
            Returns:
                true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def toSpace(self, s1Point: org.hipparchus.geometry.spherical.oned.S1Point) -> 'S2Point':
        """
            Transform a sub-space point into a space point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Embedding`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.oned.S1Point`): (n-1)-dimension point of the sub-space
        
            Returns:
                n-dimension point of the space corresponding to the specified sub-space point
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPointAt`
        
        
        
        """
        ...
    def toSubSpace(self, s2Point: 'S2Point') -> org.hipparchus.geometry.spherical.oned.S1Point:
        """
            Transform a space point into a sub-space point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSubSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Embedding`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): n-dimension point of the space
        
            Returns:
                (n-1)-dimension point of the sub-space corresponding to the specified space point
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.Circle.getPhase`
        
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubCircle':
        """
            Build a sub-hyperplane covering the whole hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.wholeHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a sub-hyperplane covering the whole hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> 'SphericalPolygonsSet':
        """
            Build a region covering the whole space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Hyperplane.wholeSpace` in
                interface :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
        
            Returns:
                a region containing the instance (really a :class:`~org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet`
                instance)
        
        
        """
        ...

class Edge:
    """
    public classEdge extends :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Spherical polygons boundary edge.
    
        Also see:
    
              - :meth:`~org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet.getBoundaryLoops`
              - :class:`~org.hipparchus.geometry.spherical.twod.Vertex`
    """
    def getCircle(self) -> Circle:
        """
            Get the circle supporting this edge.
        
            Returns:
                circle supporting this edge
        
        
        """
        ...
    def getEnd(self) -> 'Vertex':
        """
            Get end vertex.
        
            Returns:
                end vertex
        
        
        """
        ...
    def getLength(self) -> float:
        """
            Get the length of the arc.
        
            Returns:
                length of the arc (can be greater than \( \pi \))
        
        
        """
        ...
    def getPointAt(self, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get an intermediate point.
        
            The angle along the edge should normally be between 0 and :meth:`~org.hipparchus.geometry.spherical.twod.Edge.getLength`
            in order to remain within edge limits. However, there are no checks on the value of the angle, so user can rebuild the
            full circle on which an edge is defined if they want.
        
            Parameters:
                alpha (double): angle along the edge, counted from :meth:`~org.hipparchus.geometry.spherical.twod.Edge.getStart`
        
            Returns:
                an intermediate point
        
        
        """
        ...
    def getStart(self) -> 'Vertex':
        """
            Get start vertex.
        
            Returns:
                start vertex
        
        
        """
        ...

class S2Point(org.hipparchus.geometry.Point['Sphere2D', 'S2Point']):
    """
    public classS2Point extends :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.Point`<:class:`~org.hipparchus.geometry.spherical.twod.Sphere2D`,:class:`~org.hipparchus.geometry.spherical.twod.S2Point`>
    
        This class represents a point on the 2-sphere.
    
        We use the mathematical convention to use the azimuthal angle \( \theta \) in the x-y plane as the first coordinate, and
        the polar angle \( \varphi \) as the second coordinate (see `Spherical Coordinates
        <http://mathworld.wolfram.com/SphericalCoordinates.html>` in MathWorld).
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
    
              - :meth:`~serialized`
    """
    PLUS_I: typing.ClassVar['S2Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.twod.S2Point` PLUS_I
    
        +I (coordinates: \( \theta = 0, \varphi = \pi/2 \)).
    
    """
    PLUS_J: typing.ClassVar['S2Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.twod.S2Point` PLUS_J
    
        +J (coordinates: \( \theta = \pi/2, \varphi = \pi/2 \))).
    
    """
    PLUS_K: typing.ClassVar['S2Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.twod.S2Point` PLUS_K
    
        +K (coordinates: \( \theta = any angle, \varphi = 0 \)).
    
    """
    MINUS_I: typing.ClassVar['S2Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.twod.S2Point` MINUS_I
    
        -I (coordinates: \( \theta = \pi, \varphi = \pi/2 \)).
    
    """
    MINUS_J: typing.ClassVar['S2Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.twod.S2Point` MINUS_J
    
        -J (coordinates: \( \theta = 3\pi/2, \varphi = \pi/2 \)).
    
    """
    MINUS_K: typing.ClassVar['S2Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.twod.S2Point` MINUS_K
    
        -K (coordinates: \( \theta = any angle, \varphi = \pi \)).
    
    """
    NaN: typing.ClassVar['S2Point'] = ...
    """
    public static final :class:`~org.hipparchus.geometry.spherical.twod.S2Point` NaN
    
        A vector with all coordinates set to NaN.
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def distance(self, s2Point: 'S2Point') -> float:
        """
            Compute the distance between the instance and another point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.distance` in interface :class:`~org.hipparchus.geometry.Point`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): second point
        
            Returns:
                the distance between the instance and p
        
            Compute the distance (angular separation) between two points.
        
            Parameters:
                p1 (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): first vector
                p2 (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): second vector
        
            Returns:
                the angular separation between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(s2Point: 'S2Point', s2Point2: 'S2Point') -> float: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two points on the 2-sphere.
        
            If all coordinates of two points are exactly the same, and none are :code:`Double.NaN`, the two points are considered to
            be equal.
        
            :code:`NaN` coordinates are considered to affect globally the point and be equals to each other - i.e, if either (or
            all) coordinates of the point are equal to :code:`Double.NaN`, the point is equal to
            :meth:`~org.hipparchus.geometry.spherical.twod.S2Point.NaN`.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality to this
        
            Returns:
                true if two points on the 2-sphere objects are equal, false if object is null, not an instance of S2Point, or not equal
                to this S2Point instance
        
        
        """
        ...
    def equalsIeee754(self, object: typing.Any) -> bool:
        """
            Test for the equality of two points on the 2-sphere.
        
            If all coordinates of two points are exactly the same, and none are :code:`Double.NaN`, the two points are considered to
            be equal.
        
            In compliance with IEEE754 handling, if any coordinates of any of the two points are :code:`NaN`, then the points are
            considered different. This implies that
            :meth:`~org.hipparchus.geometry.spherical.twod.S2Point.NaN`.equals(:meth:`~org.hipparchus.geometry.spherical.twod.S2Point.NaN`)
            returns :code:`false` despite the instance is checked against itself.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality to this
        
            Returns:
                true if two points objects are equal, false if object is null, not an instance of S2Point, or not equal to this S2Point
                instance
        
            Since:
                2.1
        
        
        """
        ...
    def getPhi(self) -> float:
        """
            Get the polar angle \( \varphi \).
        
            Returns:
                polar angle \( \varphi \)
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.S2Point.%3Cinit%3E`
        
        
        
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
    def getTheta(self) -> float:
        """
            Get the azimuthal angle \( \theta \) in the x-y plane.
        
            Returns:
                azimuthal angle \( \theta \) in the x-y plane
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.spherical.twod.S2Point.%3Cinit%3E`
        
        
        
        """
        ...
    def getVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the corresponding normalized vector in the 3D euclidean space.
        
            Returns:
                normalized vector
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the point.
        
            All NaN values have the same hash code.
        
            Overrides:
                :meth:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
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
    def moveTowards(self, s2Point: 'S2Point', double: float) -> 'S2Point':
        """
            Move towards another point.
        
            Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for
            moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.Point.moveTowards` in interface :class:`~org.hipparchus.geometry.Point`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.spherical.twod.S2Point`): other point
                ratio (double): motion ratio,
        
            Returns:
                moved point
        
        
        """
        ...
    def negate(self) -> 'S2Point':
        """
            Get the opposite of the instance.
        
            Returns:
                a new vector which is opposite to the instance
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...

class Sphere2D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    public classSphere2D extends :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`, :class:`~org.hipparchus.geometry.Space`
    
        This class implements a two-dimensional sphere (i.e. the regular sphere).
    
        We use here the topologists definition of the 2-sphere (see `Sphere <http://mathworld.wolfram.com/Sphere.html>` on
        MathWorld), i.e. the 2-sphere is the two-dimensional surface defined in 3D as x :sup:`2` +y :sup:`2` +z :sup:`2` =1.
    
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
    def getInstance() -> 'Sphere2D':
        """
            Get the unique instance.
        
            Returns:
                the unique instance
        
        
        """
        ...
    def getSubSpace(self) -> org.hipparchus.geometry.spherical.oned.Sphere1D:
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

class SphericalPolygonsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Sphere2D, S2Point, Circle, 'SubCircle', org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]):
    """
    public classSphericalPolygonsSet extends :class:`~org.hipparchus.geometry.partitioning.AbstractRegion`<:class:`~org.hipparchus.geometry.spherical.twod.Sphere2D`,:class:`~org.hipparchus.geometry.spherical.twod.S2Point`,:class:`~org.hipparchus.geometry.spherical.twod.Circle`,:class:`~org.hipparchus.geometry.spherical.twod.SubCircle`,:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`,:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.SubLimitAngle`>
    
        This class represents a region on the 2-sphere: a set of spherical polygons.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, *s2Point: S2Point): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection['SubCircle'], typing.Sequence['SubCircle'], typing.Set['SubCircle']], double: float): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, int: int, double2: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Sphere2D, S2Point, Circle, 'SubCircle'], double: float): ...
    def buildNew(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Sphere2D, S2Point, Circle, 'SubCircle']) -> 'SphericalPolygonsSet': ...
    def getBoundaryLoops(self) -> java.util.List['Vertex']: ...
    def getEnclosingCap(self) -> org.hipparchus.geometry.enclosing.EnclosingBall[Sphere2D, S2Point]: ...
    def getInteriorPoint(self) -> S2Point:
        """
            Get an interior point.
        
            Returns:
                an arbitrary interior point, or null if region is empty
        
        
        """
        ...

class SubCircle(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Sphere2D, S2Point, Circle, 'SubCircle', org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]):
    """
    public classSubCircle extends :class:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane`<:class:`~org.hipparchus.geometry.spherical.twod.Sphere2D`,:class:`~org.hipparchus.geometry.spherical.twod.S2Point`,:class:`~org.hipparchus.geometry.spherical.twod.Circle`,:class:`~org.hipparchus.geometry.spherical.twod.SubCircle`,:class:`~org.hipparchus.geometry.spherical.oned.Sphere1D`,:class:`~org.hipparchus.geometry.spherical.oned.S1Point`,:class:`~org.hipparchus.geometry.spherical.oned.LimitAngle`,:class:`~org.hipparchus.geometry.spherical.oned.SubLimitAngle`>
    
        This class represents a sub-hyperplane for :class:`~org.hipparchus.geometry.spherical.twod.Circle`.
    """
    def __init__(self, circle: Circle, region: org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]): ...
    def getInteriorPoint(self) -> S2Point:
        """
            Get an interior point.
        
            Returns:
                an arbitrary interior point, or null if sub-hyperplane is empty
        
        
        """
        ...
    def split(self, circle: Circle) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Sphere2D, S2Point, Circle, 'SubCircle']: ...

class Vertex:
    """
    public classVertex extends :class:`~org.hipparchus.geometry.spherical.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Spherical polygons boundary vertex.
    
        Also see:
    
              - :meth:`~org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet.getBoundaryLoops`
              - :class:`~org.hipparchus.geometry.spherical.twod.Edge`
    """
    def getIncoming(self) -> Edge:
        """
            Get incoming edge.
        
            Returns:
                incoming edge
        
        
        """
        ...
    def getLocation(self) -> S2Point:
        """
            Get Vertex location.
        
            Returns:
                vertex location
        
        
        """
        ...
    def getOutgoing(self) -> Edge:
        """
            Get outgoing edge.
        
            Returns:
                outgoing edge
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.spherical.twod")``.

    Circle: typing.Type[Circle]
    Edge: typing.Type[Edge]
    S2Point: typing.Type[S2Point]
    Sphere2D: typing.Type[Sphere2D]
    SphericalPolygonsSet: typing.Type[SphericalPolygonsSet]
    SubCircle: typing.Type[SubCircle]
    Vertex: typing.Type[Vertex]
