
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import org.hipparchus.geometry
import org.hipparchus.geometry.partitioning
import typing



_ConvexHull__S = typing.TypeVar('_ConvexHull__S', bound=org.hipparchus.geometry.Space)  # <S>
_ConvexHull__P = typing.TypeVar('_ConvexHull__P', bound=org.hipparchus.geometry.Point)  # <P>
_ConvexHull__H = typing.TypeVar('_ConvexHull__H', bound=org.hipparchus.geometry.partitioning.Hyperplane)  # <H>
_ConvexHull__I = typing.TypeVar('_ConvexHull__I', bound=org.hipparchus.geometry.partitioning.SubHyperplane)  # <I>
class ConvexHull(java.io.Serializable, typing.Generic[_ConvexHull__S, _ConvexHull__P, _ConvexHull__H, _ConvexHull__I]):
    """
    This class represents a convex hull.
    """
    def createRegion(self) -> org.hipparchus.geometry.partitioning.Region[_ConvexHull__S, _ConvexHull__P, _ConvexHull__H, _ConvexHull__I]:
        """
        Returns a new region that is enclosed by the convex hull.
        
        Returns:
            the region enclosed by the convex hull
        
        Raises:
            hipparchus: if the number of vertices is not enough to build a region in the respective space
        
        
        """
        ...
    def getVertices(self) -> typing.MutableSequence[_ConvexHull__P]:
        """
        Get the vertices of the convex hull.
        
        Returns:
            vertices of the convex hull
        
        
        """
        ...

_ConvexHullGenerator__S = typing.TypeVar('_ConvexHullGenerator__S', bound=org.hipparchus.geometry.Space)  # <S>
_ConvexHullGenerator__P = typing.TypeVar('_ConvexHullGenerator__P', bound=org.hipparchus.geometry.Point)  # <P>
_ConvexHullGenerator__H = typing.TypeVar('_ConvexHullGenerator__H', bound=org.hipparchus.geometry.partitioning.Hyperplane)  # <H>
_ConvexHullGenerator__I = typing.TypeVar('_ConvexHullGenerator__I', bound=org.hipparchus.geometry.partitioning.SubHyperplane)  # <I>
class ConvexHullGenerator(typing.Generic[_ConvexHullGenerator__S, _ConvexHullGenerator__P, _ConvexHullGenerator__H, _ConvexHullGenerator__I]):
    """
    Interface for convex hull generators.
    
          - `Convex Hull (Wikipedia) <http://en.wikipedia.org/wiki/Convex_hull>`
          - `Convex Hull (MathWorld) <http://mathworld.wolfram.com/ConvexHull.html>`
    """
    def generate(self, points: typing.Union[java.util.Collection[_ConvexHullGenerator__P], typing.Sequence[_ConvexHullGenerator__P], typing.Set[_ConvexHullGenerator__P]]) -> ConvexHull[_ConvexHullGenerator__S, _ConvexHullGenerator__P, _ConvexHullGenerator__H, _ConvexHullGenerator__I]:
        """
        Builds the convex hull from the set of input points.
        
        Parameters:
            points (Collection<ConvexHullGenerator> points): the set of input points
        
        Returns:
            the convex hull
        
        Raises:
            hipparchus: if generator fails to generate a convex hull for the given set of input points
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.hull")``.

    ConvexHull: typing.Type[ConvexHull]
    ConvexHullGenerator: typing.Type[ConvexHullGenerator]
