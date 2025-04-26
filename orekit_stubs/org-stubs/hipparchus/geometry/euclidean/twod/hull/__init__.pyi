
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
    public final classAklToussaintHeuristic extends :class:`~org.hipparchus.geometry.euclidean.twod.hull.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        A simple heuristic to improve the performance of convex hull algorithms.
    
        The heuristic is based on the idea of a convex quadrilateral, which is formed by four points with the lowest and highest
        x / y coordinates. Any point that lies inside this quadrilateral can not be part of the convex hull and can thus be
        safely discarded before generating the convex hull itself.
    
        The complexity of the operation is O(n), and may greatly improve the time it takes to construct the convex hull
        afterwards, depending on the point distribution.
    
        Also see:
    
              - ` Akl-Toussaint heuristic (Wikipedia) <http://en.wikipedia.org/wiki/Convex_hull_algorithms#Akl-Toussaint_heuristic>`
    """
    @staticmethod
    def reducePoints(collection: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Set[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D]: ...

class ConvexHull2D(org.hipparchus.geometry.hull.ConvexHull[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine], java.io.Serializable):
    """
    public classConvexHull2D extends :class:`~org.hipparchus.geometry.euclidean.twod.hull.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.hull.ConvexHull`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Line`,:class:`~org.hipparchus.geometry.euclidean.twod.SubLine`>, :class:`~org.hipparchus.geometry.euclidean.twod.hull.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class represents a convex hull in an two-dimensional euclidean space.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, vector2DArray: typing.Union[typing.List[org.hipparchus.geometry.euclidean.twod.Vector2D], jpype.JArray], double: float): ...
    def createRegion(self) -> org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine]: ...
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
        
            Specified by:
                :meth:`~org.hipparchus.geometry.hull.ConvexHull.getVertices` in
                interface :class:`~org.hipparchus.geometry.hull.ConvexHull`
        
            Returns:
                vertices of the convex hull
        
        
        """
        ...

class ConvexHullGenerator2D(org.hipparchus.geometry.hull.ConvexHullGenerator[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D, org.hipparchus.geometry.euclidean.twod.Line, org.hipparchus.geometry.euclidean.twod.SubLine]):
    """
    public interfaceConvexHullGenerator2Dextends :class:`~org.hipparchus.geometry.hull.ConvexHullGenerator`<:class:`~org.hipparchus.geometry.euclidean.twod.Euclidean2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Vector2D`,:class:`~org.hipparchus.geometry.euclidean.twod.Line`,:class:`~org.hipparchus.geometry.euclidean.twod.SubLine`>
    
        Interface for convex hull generators in the two-dimensional euclidean space.
    """
    def generate(self, collection: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Set[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> ConvexHull2D: ...

class MonotoneChain(org.hipparchus.geometry.euclidean.twod.hull.AbstractConvexHullGenerator2D):
    """
    public classMonotoneChain extends :class:`~org.hipparchus.geometry.euclidean.twod.hull.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Implements Andrew's monotone chain method to generate the convex hull of a finite set of points in the two-dimensional
        euclidean space.
    
        The runtime complexity is O(n log n), with n being the number of input points. If the point set is already sorted (by
        x-coordinate), the runtime complexity is O(n).
    
        The implementation is not sensitive to collinear points on the hull. The parameter :code:`includeCollinearPoints` allows
        to control the behavior with regard to collinear points. If :code:`true`, all points on the boundary of the hull will be
        added to the hull vertices, otherwise only the extreme points will be present. By default, collinear points are not
        added as hull vertices.
    
        The :code:`tolerance` parameter (default: 1e-10) is used as epsilon criteria to determine identical and collinear
        points.
    
        Also see:
    
              - ` Andrew's monotone chain algorithm (Wikibooks)
                <http://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain>`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, boolean: bool, double: float): ...
    def findHullVertices(self, collection: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Set[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D]: ...

class AbstractConvexHullGenerator2D: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.twod.hull")``.

    AbstractConvexHullGenerator2D: typing.Type[AbstractConvexHullGenerator2D]
    AklToussaintHeuristic: typing.Type[AklToussaintHeuristic]
    ConvexHull2D: typing.Type[ConvexHull2D]
    ConvexHullGenerator2D: typing.Type[ConvexHullGenerator2D]
    MonotoneChain: typing.Type[MonotoneChain]
