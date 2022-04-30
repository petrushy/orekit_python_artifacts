import java.io
import typing



class DistanceMeasure(java.io.Serializable):
    """
    public interface DistanceMeasure extends :class:`~org.hipparchus.clustering.distance.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Interface for distance measures of n-dimensional vectors.
    """
    def compute(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...

class CanberraDistance(DistanceMeasure):
    """
    public class CanberraDistance extends :class:`~org.hipparchus.clustering.distance.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.clustering.distance.DistanceMeasure`
    
        Calculates the Canberra distance between two points.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def compute(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...

class ChebyshevDistance(DistanceMeasure):
    """
    public class ChebyshevDistance extends :class:`~org.hipparchus.clustering.distance.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.clustering.distance.DistanceMeasure`
    
        Calculates the L :sub:`∞` (max of abs) distance between two points.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def compute(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...

class EarthMoversDistance(DistanceMeasure):
    """
    public class EarthMoversDistance extends :class:`~org.hipparchus.clustering.distance.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.clustering.distance.DistanceMeasure`
    
        Calculates the Earh Mover's distance (also known as Wasserstein metric) between two distributions.
    
        Also see:
            `Earth Mover's distance (Wikipedia) <http://en.wikipedia.org/wiki/Earth_mover's_distance>`, :meth:`~serialized`
    """
    def __init__(self): ...
    def compute(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...

class EuclideanDistance(DistanceMeasure):
    """
    public class EuclideanDistance extends :class:`~org.hipparchus.clustering.distance.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.clustering.distance.DistanceMeasure`
    
        Calculates the L :sub:`2` (Euclidean) distance between two points.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def compute(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...

class ManhattanDistance(DistanceMeasure):
    """
    public class ManhattanDistance extends :class:`~org.hipparchus.clustering.distance.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.clustering.distance.DistanceMeasure`
    
        Calculates the L :sub:`1` (sum of abs) distance between two points.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def compute(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.clustering.distance")``.

    CanberraDistance: typing.Type[CanberraDistance]
    ChebyshevDistance: typing.Type[ChebyshevDistance]
    DistanceMeasure: typing.Type[DistanceMeasure]
    EarthMoversDistance: typing.Type[EarthMoversDistance]
    EuclideanDistance: typing.Type[EuclideanDistance]
    ManhattanDistance: typing.Type[ManhattanDistance]
