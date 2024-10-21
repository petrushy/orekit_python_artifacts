import java.io
import java.util
import org
import org.hipparchus.geometry.euclidean.twod
import org.hipparchus.geometry.euclidean.twod.hull.class-use
import org.hipparchus.geometry.hull
import org.hipparchus.geometry.partitioning
import typing



class AklToussaintHeuristic:
    @staticmethod
    def reducePoints(collection: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D]: ...

class ConvexHull2D(org.hipparchus.geometry.hull.ConvexHull[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D], java.io.Serializable):
    def __init__(self, vector2DArray: typing.List[org.hipparchus.geometry.euclidean.twod.Vector2D], double: float): ...
    def createRegion(self) -> org.hipparchus.geometry.partitioning.Region[org.hipparchus.geometry.euclidean.twod.Euclidean2D]: ...
    def getLineSegments(self) -> typing.List[org.hipparchus.geometry.euclidean.twod.Segment]: ...
    def getVertices(self) -> typing.List[org.hipparchus.geometry.euclidean.twod.Vector2D]: ...

class ConvexHullGenerator2D(org.hipparchus.geometry.hull.ConvexHullGenerator[org.hipparchus.geometry.euclidean.twod.Euclidean2D, org.hipparchus.geometry.euclidean.twod.Vector2D]):
    def generate(self, collection: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> ConvexHull2D: ...

class MonotoneChain(org.hipparchus.geometry.euclidean.twod.hull.AbstractConvexHullGenerator2D):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, boolean: bool, double: float): ...
    def findHullVertices(self, collection: typing.Union[java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D], typing.Sequence[org.hipparchus.geometry.euclidean.twod.Vector2D]]) -> java.util.Collection[org.hipparchus.geometry.euclidean.twod.Vector2D]: ...

class AbstractConvexHullGenerator2D: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.twod.hull")``.

    AbstractConvexHullGenerator2D: typing.Type[AbstractConvexHullGenerator2D]
    AklToussaintHeuristic: typing.Type[AklToussaintHeuristic]
    ConvexHull2D: typing.Type[ConvexHull2D]
    ConvexHullGenerator2D: typing.Type[ConvexHullGenerator2D]
    MonotoneChain: typing.Type[MonotoneChain]
    class-use: org.hipparchus.geometry.euclidean.twod.hull.class-use.__module_protocol__
