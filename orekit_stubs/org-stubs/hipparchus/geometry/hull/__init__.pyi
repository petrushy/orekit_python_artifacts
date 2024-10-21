import java.io
import java.util
import org.hipparchus.geometry
import org.hipparchus.geometry.hull.class-use
import org.hipparchus.geometry.partitioning
import typing



_ConvexHull__S = typing.TypeVar('_ConvexHull__S', bound=org.hipparchus.geometry.Space)  # <S>
_ConvexHull__P = typing.TypeVar('_ConvexHull__P', bound=org.hipparchus.geometry.Point)  # <P>
class ConvexHull(java.io.Serializable, typing.Generic[_ConvexHull__S, _ConvexHull__P]):
    def createRegion(self) -> org.hipparchus.geometry.partitioning.Region[_ConvexHull__S]: ...
    def getVertices(self) -> typing.List[_ConvexHull__P]: ...

_ConvexHullGenerator__S = typing.TypeVar('_ConvexHullGenerator__S', bound=org.hipparchus.geometry.Space)  # <S>
_ConvexHullGenerator__P = typing.TypeVar('_ConvexHullGenerator__P', bound=org.hipparchus.geometry.Point)  # <P>
class ConvexHullGenerator(typing.Generic[_ConvexHullGenerator__S, _ConvexHullGenerator__P]):
    def generate(self, collection: typing.Union[java.util.Collection[_ConvexHullGenerator__P], typing.Sequence[_ConvexHullGenerator__P]]) -> ConvexHull[_ConvexHullGenerator__S, _ConvexHullGenerator__P]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.hull")``.

    ConvexHull: typing.Type[ConvexHull]
    ConvexHullGenerator: typing.Type[ConvexHullGenerator]
    class-use: org.hipparchus.geometry.hull.class-use.__module_protocol__
