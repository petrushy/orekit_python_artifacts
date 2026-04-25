
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
    implements Hyperplane<Sphere2D,S2Point,Circle,SubCircle>, Embedding<Sphere2D,S2Point,Sphere1D,S1Point>
    
    This class represents an oriented great circle on the 2-sphere.
    
    An oriented circle can be defined by a center point. The circle is the set of points that are in the normal plan the center.
    
    Since it is oriented the two spherical caps at its two sides are unambiguously identified as a left cap and a right cap. This can be used to identify the interior and the exterior in a simple way by local properties only when part of a line is used to define part of a spherical polygon boundary.
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
        
        Specified by: arbitraryPoint in interface Hyperplane
        
        Returns:
            arbirary point in the hyperplane
        
        
        """
        ...
    def copySelf(self) -> 'Circle':
        """
        Copy the instance.
        
        The instance created is completely independent of the original one. A deep copy is used, none of the underlying objects are shared (except for immutable objects).
        
        Specified by: copySelf in interface Hyperplane
        
        Returns:
            a new hyperplane, copy of the instance
        
        
        """
        ...
    def emptyHyperplane(self) -> 'SubCircle':
        """
        Build a sub-hyperplane covering nothing.
        
        Specified by: emptyHyperplane in interface Hyperplane
        
        Returns:
            a sub-hyperplane covering nothing
        
        
        """
        ...
    def getArc(self, a: 'S2Point', b: 'S2Point') -> org.hipparchus.geometry.spherical.oned.Arc:
        """
        Get the arc on this circle between two defining points. Only the point's projection on the circle matters, which is computed using getPhase.
        
        Parameters:
            a (S2Point): first point.
            b (S2Point): second point.
        
        Returns:
            an arc of the circle.
        
        
        """
        ...
    def getInsideArc(self, other: 'Circle') -> org.hipparchus.geometry.spherical.oned.Arc:
        """
        Get the arc of the instance that lies inside the other circle.
        
        Parameters:
            other (Circle): other circle
        
        Returns:
            arc of the instance that lies inside the other circle
        
        
        """
        ...
    @typing.overload
    def getOffset(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
        The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
        Specified by: getOffset in interface Hyperplane
        
        Parameters:
            point (S2Point): point to check
        
        Returns:
            offset of the point
        
              - getOffset
        
        Get the offset (oriented distance) of a direction.
        
        The offset is defined as the angular distance between the circle center and the direction minus the circle radius. It is therefore 0 on the circle, positive for directions outside of the cone delimited by the circle, and negative inside the cone.
        
        Parameters:
            direction (Vector3D): direction to check
        
        Returns:
            offset of the direction
        
              - getOffset
        
        
        
        """
        ...
    @typing.overload
    def getOffset(self, s2Point: 'S2Point') -> float: ...
    def getPhase(self, direction: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
        Get the phase angle of a direction.
        
        The direction may not belong to the circle as the phase is computed for the meridian plane between the circle pole and the direction.
        
        Parameters:
            direction (Vector3D): direction for which phase is requested
        
        Returns:
            phase angle of the direction around the circle
        
              - toSubSpace
        
        
        
        """
        ...
    def getPointAt(self, alpha: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get a circle point from its phase around the circle.
        
        Parameters:
            alpha (double): phase around the circle
        
        Returns:
            circle point on the sphere
        
              - toSpace
              - getXAxis
              - getYAxis
        
        
        
        """
        ...
    def getPole(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the pole of the circle.
        
        As the circle is a great circle, the pole does not belong to it.
        
        Returns:
            pole of the circle
        
              - getXAxis
              - getYAxis
        
        
        
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
        
        Specified by: getTolerance in interface Hyperplane
        
        Returns:
            tolerance below which points are considered to belong to the hyperplane
        
        
        """
        ...
    @staticmethod
    def getTransform(rotation: org.hipparchus.geometry.euclidean.threed.Rotation) -> org.hipparchus.geometry.partitioning.Transform['Sphere2D', 'S2Point', 'Circle', 'SubCircle', org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]:
        """
        Get a Transform embedding a 3D rotation.
        
        Parameters:
            rotation (Rotation): rotation to use
        
        Returns:
            a new transform that can be applied to either Point,
            Circle or SubHyperplane
            instances
        
        
        """
        ...
    def getXAxis(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the X axis of the circle.
        
        This method returns the same value as getPointAt but it does not do any computation and always return the same instance.
        
        Returns:
            an arbitrary x axis on the circle
        
              - getPointAt
              - getYAxis
              - getPole
        
        
        
        """
        ...
    def getYAxis(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the Y axis of the circle.
        
        This method returns the same value as getPointAt but it does not do any computation and always return the same instance.
        
        Returns:
            an arbitrary y axis point on the circle
        
              - getPointAt
              - getXAxis
              - getPole
        
        
        
        """
        ...
    def moveToOffset(self, point: 'S2Point', offset: float) -> 'S2Point':
        """
        Move point up to specified offset.
        
        Motion is orthogonal to the hyperplane
        
        Specified by: moveToOffset in interface Hyperplane
        
        Parameters:
            point (S2Point): point to move
            offset (double): desired offset
        
        Returns:
            moved point at desired offset
        
        
        """
        ...
    def project(self, point: 'S2Point') -> 'S2Point':
        """
        Project a point to the hyperplane.
        
        Specified by: project in interface Hyperplane
        
        Parameters:
            point (S2Point): point to project
        
        Returns:
            projected point
        
        
        """
        ...
    def reset(self, newPole: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Reset the instance as if built from a pole.
        
        The circle is oriented in the trigonometric direction around pole.
        
        Parameters:
            newPole (Vector3D): circle pole
        
        
        """
        ...
    def revertSelf(self) -> None:
        """
        Revert the instance.
        """
        ...
    def sameOrientationAs(self, other: 'Circle') -> bool:
        """
        Check if the instance has the same orientation as another hyperplane.
        
        This method is expected to be called on parallel hyperplanes. The method should not re-check for parallelism, only for orientation, typically by testing something like the sign of the dot-products of normals.
        
        Specified by: sameOrientationAs in interface Hyperplane
        
        Parameters:
            other (Circle): other hyperplane to check against the instance
        
        Returns:
            true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def toSpace(self, point: org.hipparchus.geometry.spherical.oned.S1Point) -> 'S2Point':
        """
        Transform a sub-space point into a space point.
        
        Specified by: toSpace in interface Embedding
        
        Parameters:
            point (S1Point): (n-1)-dimension point of the sub-space
        
        Returns:
            n-dimension point of the space corresponding to the specified sub-space point
        
              - getPointAt
        
        
        
        """
        ...
    def toSubSpace(self, point: 'S2Point') -> org.hipparchus.geometry.spherical.oned.S1Point:
        """
        Transform a space point into a sub-space point.
        
        Specified by: toSubSpace in interface Embedding
        
        Parameters:
            point (S2Point): n-dimension point of the space
        
        Returns:
            (n-1)-dimension point of the sub-space corresponding to the specified space point
        
              - getPhase
        
        
        
        """
        ...
    def wholeHyperplane(self) -> 'SubCircle':
        """
        Build a sub-hyperplane covering the whole hyperplane.
        
        Specified by: wholeHyperplane in interface Hyperplane
        
        Returns:
            a sub-hyperplane covering the whole hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> 'SphericalPolygonsSet':
        """
        Build a region covering the whole space.
        
        Specified by: wholeSpace in interface Hyperplane
        
        Returns:
            a region containing the instance (really a SphericalPolygonsSet
            instance)
        
        
        """
        ...

class Edge:
    """
    Spherical polygons boundary edge.
    
          - getBoundaryLoops
          - Vertex
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
    def getPointAt(self, alpha: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get an intermediate point.
        
        The angle along the edge should normally be between 0 and getLength in order to remain within edge limits. However, there are no checks on the value of the angle, so user can rebuild the full circle on which an edge is defined if they want.
        
        Parameters:
            alpha (double): angle along the edge, counted from getStart
        
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
    implements Point<Sphere2D,S2Point>
    
    This class represents a point on the 2-sphere.
    
    We use the mathematical convention to use the azimuthal angle \( \theta \) in the x-y plane as the first coordinate, and the polar angle \( \varphi \) as the second coordinate (see `Spherical Coordinates <http://mathworld.wolfram.com/SphericalCoordinates.html>` in MathWorld).
    
    Instances of this class are guaranteed to be immutable.
    
          - serialized
    """
    PLUS_I: typing.ClassVar['S2Point'] = ...
    """
    +I (coordinates: \( \theta = 0, \varphi = \pi/2 \)).
    """
    PLUS_J: typing.ClassVar['S2Point'] = ...
    """
    +J (coordinates: \( \theta = \pi/2, \varphi = \pi/2 \))).
    """
    PLUS_K: typing.ClassVar['S2Point'] = ...
    """
    +K (coordinates: \( \theta = any angle, \varphi = 0 \)).
    """
    MINUS_I: typing.ClassVar['S2Point'] = ...
    """
    -I (coordinates: \( \theta = \pi, \varphi = \pi/2 \)).
    """
    MINUS_J: typing.ClassVar['S2Point'] = ...
    """
    -J (coordinates: \( \theta = 3\pi/2, \varphi = \pi/2 \)).
    """
    MINUS_K: typing.ClassVar['S2Point'] = ...
    """
    -K (coordinates: \( \theta = any angle, \varphi = \pi \)).
    """
    NaN: typing.ClassVar['S2Point'] = ...
    """
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
        
        Specified by: distance in interface Point
        
        Parameters:
            point (S2Point): second point
        
        Returns:
            the distance between the instance and p
        
        Compute the distance (angular separation) between two points.
        
        Parameters:
            p1 (S2Point): first vector
            p2 (S2Point): second vector
        
        Returns:
            the angular separation between p1 and p2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(s2Point: 'S2Point', s2Point2: 'S2Point') -> float: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two points on the 2-sphere.
        
        If all coordinates of two points are exactly the same, and none are NaN, the two points are considered to be equal.
        
        NaN coordinates are considered to affect globally the point and be equals to each other - i.e, if either (or all) coordinates of the point are equal to NaN, the point is equal to NaN.
        
        Overrides: equals in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two points on the 2-sphere objects are equal, false if object is null, not an instance of S2Point, or not equal
            to this S2Point instance
        
        
        """
        ...
    def equalsIeee754(self, other: typing.Any) -> bool:
        """
        Test for the equality of two points on the 2-sphere.
        
        If all coordinates of two points are exactly the same, and none are NaN, the two points are considered to be equal.
        
        In compliance with IEEE754 handling, if any coordinates of any of the two points are NaN, then the points are considered different. This implies that NaN.equals(NaN) returns false despite the instance is checked against itself.
        
        Parameters:
            other (Object): Object to test for equality to this
        
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
        
              - 
        
        
        
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
    def getTheta(self) -> float:
        """
        Get the azimuthal angle \( \theta \) in the x-y plane.
        
        Returns:
            azimuthal angle \( \theta \) in the x-y plane
        
              - 
        
        
        
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
        
        Overrides: hashCode in class Object
        
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
    def moveTowards(self, other: 'S2Point', ratio: float) -> 'S2Point':
        """
        Move towards another point.
        
        Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
        Specified by: moveTowards in interface Point
        
        Parameters:
            other (S2Point): other point
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
        Overrides: toString in class Object
        
        
        """
        ...

class Sphere2D(java.io.Serializable, org.hipparchus.geometry.Space):
    """
    implements Serializable, Space
    
    This class implements a two-dimensional sphere (i.e. the regular sphere).
    
    We use here the topologists definition of the 2-sphere (see `Sphere <http://mathworld.wolfram.com/Sphere.html>` on MathWorld), i.e. the 2-sphere is the two-dimensional surface defined in 3D as x :sup:`2` +y :sup:`2` +z :sup:`2` =1.
    
          - serialized
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
        
        Specified by: getSubSpace in interface Space
        
        Returns:
            n-1 dimension sub-space of this space
        
              - getDimension
        
        
        
        """
        ...

class SphericalPolygonsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Sphere2D, S2Point, Circle, 'SubCircle', org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]):
    """
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
    def buildNew(self, tree: org.hipparchus.geometry.partitioning.BSPTree[Sphere2D, S2Point, Circle, 'SubCircle']) -> 'SphericalPolygonsSet':
        """
        Build a region using the instance as a prototype.
        
        This method allow to create new instances without knowing exactly the type of the region. It is an application of the prototype design pattern.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Specified by: buildNew in interface Region
        
        Specified by: buildNew in class AbstractRegion
        
        Parameters:
            tree (BSPTree<Sphere2D,S2Point,Circle,SubCircle> tree): inside/outside BSP tree representing the new region
        
        Returns:
            the built region
        
        
        """
        ...
    def getBoundaryLoops(self) -> java.util.List['Vertex']:
        """
        Get the boundary loops of the polygon.
        
        The polygon boundary can be represented as a list of closed loops, each loop being given by exactly one of its vertices. From each loop start vertex, one can follow the loop by finding the outgoing edge, then the end vertex, then the next outgoing edge ... until the start vertex of the loop (exactly the same instance) is found again once the full loop has been visited.
        
        If the polygon has no boundary at all, a zero length loop array will be returned.
        
        If the polygon is a simple one-piece polygon, then the returned array will contain a single vertex.
        
        All edges in the various loops have the inside of the region on their left side (i.e. toward their pole) and the outside on their right side (i.e. away from their pole) when moving in the underlying circle direction. This means that the closed loops obey the direct trigonometric orientation.
        
        Returns:
            boundary of the polygon, organized as an unmodifiable list of loops start vertices.
        
        Raises:
            hipparchus: if the tolerance setting does not allow to build a clean non-ambiguous boundary
        
              - Vertex
              - Edge
        
        
        
        """
        ...
    def getEnclosingCap(self) -> org.hipparchus.geometry.enclosing.EnclosingBall[Sphere2D, S2Point]:
        """
        Get a spherical cap enclosing the polygon.
        
        This method is intended as a first test to quickly identify points that are guaranteed to be outside of the region, hence performing a full checkPoint checkPoint} only if the point status remains undecided after the quick check. It is is therefore mostly useful to speed up computation for small polygons with complex shapes (say a country boundary on Earth), as the spherical cap will be small and hence will reliably identify a large part of the sphere as outside, whereas the full check can be more computing intensive. A typical use case is therefore:
        
        
           // compute region, plus an enclosing spherical cap
           SphericalPolygonsSet complexShape = ...;
           EnclosingBall<Sphere2D, S2Point> cap = complexShape.getEnclosingCap();
        
           // check lots of points
           for (Vector3D p : points) {
        
             final Location l;
             if (cap.contains(p)) {
               // we cannot be sure where the point is
               // we need to perform the full computation
               l = complexShape.checkPoint(v);
             } else {
               // no need to do further computation,
               // we already know the point is outside
               l = Location.OUTSIDE;
             }
        
             // use l ...
        
           }
         
        
        In the special cases of empty or whole sphere polygons, special spherical caps are returned, with angular radius set to negative or positive infinity so the contains method return always false or true.
        
        This method is not guaranteed to return the smallest enclosing cap.
        
        Returns:
            a spherical cap enclosing the polygon
        
        
        """
        ...
    def getInteriorPoint(self) -> S2Point:
        """
        Get an interior point.
        
        Returns:
            an arbitrary interior point, or null if region is empty
        
        
        """
        ...

class SubCircle(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Sphere2D, S2Point, Circle, 'SubCircle', org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]):
    """
    This class represents a sub-hyperplane for Circle.
    """
    def __init__(self, hyperplane: Circle, remainingRegion: org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.spherical.oned.Sphere1D, org.hipparchus.geometry.spherical.oned.S1Point, org.hipparchus.geometry.spherical.oned.LimitAngle, org.hipparchus.geometry.spherical.oned.SubLimitAngle]):
        """
        Simple constructor.
        
        Parameters:
            hyperplane (Circle): underlying hyperplane
            remainingRegion (Region<Sphere1D,S1Point,LimitAngle,SubLimitAngle> remainingRegion): remaining region of the hyperplane
        
        
        """
        ...
    def getInteriorPoint(self) -> S2Point:
        """
        Get an interior point.
        
        Returns:
            an arbitrary interior point, or null if sub-hyperplane is empty
        
        
        """
        ...
    def split(self, hyperplane: Circle) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Sphere2D, S2Point, Circle, 'SubCircle']:
        """
        Split the instance in two parts by an hyperplane.
        
        Specified by: split in interface SubHyperplane
        
        Specified by: split in class AbstractSubHyperplane
        
        Parameters:
            hyperplane (Circle): splitting hyperplane
        
        Returns:
            an object containing both the part of the instance on the plus side of the hyperplane and the part of the instance on
            the minus side of the hyperplane
        
        
        """
        ...

class Vertex:
    """
    Spherical polygons boundary vertex.
    
          - getBoundaryLoops
          - Edge
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
