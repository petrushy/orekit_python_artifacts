
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import jpype
import org
import org.hipparchus.geometry.euclidean.twod
import org.hipparchus.geometry.hull
import org.hipparchus.geometry.partitioning
import typing



class AklToussaintHeuristic:
    """
    A simple heuristic to improve the performance of convex hull algorithms.
    
    The heuristic is based on the idea of a convex quadrilateral, which is formed by four points with the lowest and highest x / y coordinates. Any point that lies inside this quadrilateral can not be part of the convex hull and can thus be safely discarded before generating the convex hull itself.
    
    The complexity of the operation is O(n), and may greatly improve the time it takes to construct the convex hull afterwards, depending on the point distribution.
    
    Also see:
        ` Akl-Toussaint heuristic (Wikipedia) <http://en.wikipedia.org/wiki/Convex_hull_algorithms#Akl-Toussaint_heuristic>`
    """
    @staticmethod
    def reducePoints(points: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Set[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D]:
        """
        Returns a point set that is reduced by all points for which it is safe to assume that they are not part of the convex hull.
        
        Parameters:
            points (Collection<Vector2D> points): the original point set
        
        Returns:
            a reduced point set, useful as input for convex hull algorithms
        
        
        """
        ...

class ConvexHull2D(org.hipparchus.geometry.hull.ConvexHull[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine], java.io.Serializable):
    """
    This class represents a convex hull in an two-dimensional euclidean space.
    
    Also see:
        serialized
    """
    def __init__(self, vertices: typing.Union[typing.List[org.hipparchus.geometry.euclidean.twod.Vector2D], jpype.JArray], tolerance: float):
        """
        Simple constructor.
        
        Parameters:
            vertices (Vector2D[]): the vertices of the convex hull, must be ordered
            tolerance (double): tolerance below which points are considered identical
        
        Raises:
            hipparchus: if the vertices do not form a convex hull
        
        
        """
        ...
    def createRegion(self) -> org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine]:
        """
        Returns a new region that is enclosed by the convex hull.
        
        Specified by: createRegion in interface ConvexHull
        
        Returns:
            the region enclosed by the convex hull
        
        Raises:
            hipparchus: if the number of vertices is not enough to build a region in the respective space
        
        
        """
        ...
    def getLineSegments(self) -> typing.MutableSequence[org.hipparchus.geometry.euclidean.twod.Segment]:
        """
        Get the line segments of the convex hull, ordered.
        
        Returns:
            the line segments of the convex hull
        
        
        """
        ...
    def getVertices(self) -> typing.MutableSequence[org.hipparchus.geometry.euclidean.twod.Vector2D]:
        """
        Get the vertices of the convex hull.
        
        Specified by: getVertices in interface ConvexHull
        
        Returns:
            vertices of the convex hull
        
        
        """
        ...

class ConvexHullGenerator2D(org.hipparchus.geometry.hull.ConvexHullGenerator[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine]):
    """
    Interface for convex hull generators in the two-dimensional euclidean space.
    """
    def generate(self, points: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Set[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> ConvexHull2D:
        """
        Builds the convex hull from the set of input points.
        
        Specified by: generate in interface ConvexHullGenerator
        
        Parameters:
            points (Collection<Vector2D> points): the set of input points
        
        Returns:
            the convex hull
        
        Raises:
            hipparchus: if generator fails to generate a convex hull for the given set of input points
        
        
        """
        ...

class MonotoneChain(org.hipparchus.geometry.euclidean.twod.hull.AbstractConvexHullGenerator2D):
    """
    Implements Andrew's monotone chain method to generate the convex hull of a finite set of points in the two-dimensional euclidean space.
    
    The runtime complexity is O(n log n), with n being the number of input points. If the point set is already sorted (by x-coordinate), the runtime complexity is O(n).
    
    The implementation is not sensitive to collinear points on the hull. The parameter includeCollinearPoints allows to control the behavior with regard to collinear points. If true, all points on the boundary of the hull will be added to the hull vertices, otherwise only the extreme points will be present. By default, collinear points are not added as hull vertices.
    
    The tolerance parameter (default: 1e-10) is used as epsilon criteria to determine identical and collinear points.
    
    Also see:
        ` Andrew's monotone chain algorithm (Wikibooks)
        <http://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain>`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, includeCollinearPoints: bool): ...
    @typing.overload
    def __init__(self, includeCollinearPoints: bool, tolerance: float): ...
    def findHullVertices(self, points: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Set[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D]:
        """
        Find the convex hull vertices from the set of input points.
        
        Parameters:
            points (Collection<Vector2D> points): the set of input points
        
        Returns:
            the convex hull vertices in CCW winding
        
        
        """
        ...

class AbstractConvexHullGenerator2D: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.twod.hull")``.

    AbstractConvexHullGenerator2D: typing.Type[AbstractConvexHullGenerator2D]
    AklToussaintHeuristic: typing.Type[AklToussaintHeuristic]
    ConvexHull2D: typing.Type[ConvexHull2D]
    ConvexHullGenerator2D: typing.Type[ConvexHullGenerator2D]
    MonotoneChain: typing.Type[MonotoneChain]
