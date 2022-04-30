import java.io
import java.lang
import java.util
import org.hipparchus.clustering.distance
import org.hipparchus.clustering.evaluation
import org.hipparchus.exception
import org.hipparchus.linear
import org.hipparchus.random
import typing



_Cluster__T = typing.TypeVar('_Cluster__T', bound='Clusterable')  # <T>
class Cluster(java.io.Serializable, typing.Generic[_Cluster__T]):
    """
    public class Cluster<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Cluster holding a set of :class:`~org.hipparchus.clustering.Clusterable` points.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def addPoint(self, t: _Cluster__T) -> None:
        """
            Add a point to this cluster.
        
            Parameters:
                point (:class:`~org.hipparchus.clustering.Cluster`): point to add
        
        
        """
        ...
    def getPoints(self) -> java.util.List[_Cluster__T]: ...

class Clusterable:
    """
    public interface Clusterable
    
        Interface for n-dimensional points that can be clustered together.
    """
    def getPoint(self) -> typing.List[float]:
        """
            Gets the n-dimensional point.
        
            Returns:
                the point array (beware, it may be a reference to an internal array)
        
        
        """
        ...

_Clusterer__T = typing.TypeVar('_Clusterer__T', bound=Clusterable)  # <T>
class Clusterer(typing.Generic[_Clusterer__T]):
    """
    public abstract class Clusterer<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for clustering algorithms.
    """
    def cluster(self, collection: typing.Union[java.util.Collection[_Clusterer__T], typing.Sequence[_Clusterer__T], typing.Set[_Clusterer__T]]) -> java.util.List[Cluster[_Clusterer__T]]: ...
    def getDistanceMeasure(self) -> org.hipparchus.clustering.distance.DistanceMeasure:
        """
            Returns the :class:`~org.hipparchus.clustering.distance.DistanceMeasure` instance used by this clusterer.
        
            Returns:
                the distance measure
        
        
        """
        ...

class LocalizedClusteringFormats(java.lang.Enum['LocalizedClusteringFormats'], org.hipparchus.exception.Localizable):
    """
    public enum LocalizedClusteringFormats extends :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.clustering.LocalizedClusteringFormats`> implements :class:`~org.hipparchus.clustering.https:.www.hipparchus.org.hipparchus`
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    EMPTY_CLUSTER_IN_K_MEANS: typing.ClassVar['LocalizedClusteringFormats'] = ...
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.clustering.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.clustering.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.clustering.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.clustering.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedClusteringFormats':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['LocalizedClusteringFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LocalizedClusteringFormats c : LocalizedClusteringFormats.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_CentroidCluster__T = typing.TypeVar('_CentroidCluster__T', bound=Clusterable)  # <T>
class CentroidCluster(Cluster[_CentroidCluster__T], typing.Generic[_CentroidCluster__T]):
    """
    public class CentroidCluster<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.Cluster`<T>
    
        A Cluster used by centroid-based clustering algorithms.
    
        Defines additionally a cluster center which may not necessarily be a member of the original data set.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, clusterable: Clusterable): ...
    def getCenter(self) -> Clusterable:
        """
            Get the point chosen to be the center of this cluster.
        
            Returns:
                chosen cluster center
        
        
        """
        ...

_DBSCANClusterer__T = typing.TypeVar('_DBSCANClusterer__T', bound=Clusterable)  # <T>
class DBSCANClusterer(Clusterer[_DBSCANClusterer__T], typing.Generic[_DBSCANClusterer__T]):
    """
    public class DBSCANClusterer<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.Clusterer`<T>
    
        DBSCAN (density-based spatial clustering of applications with noise) algorithm.
    
        The DBSCAN algorithm forms clusters based on the idea of density connectivity, i.e. a point p is density connected to
        another point q, if there exists a chain of points p :sub:`i` , with i = 1 .. n and p :sub:`1` = p and p :sub:`n` = q,
        such that each pair <p :sub:`i` , p :sub:`i+1` > is directly density-reachable. A point q is directly density-reachable
        from point p if it is in the ε-neighborhood of this point.
    
        Any point that is not density-reachable from a formed cluster is treated as noise, and will thus not be present in the
        result.
    
        The algorithm requires two parameters:
    
          - eps: the distance that defines the ε-neighborhood of a point
          - minPoints: the minimum number of density-connected points required to form a cluster
    
    
        Also see:
            `DBSCAN (wikipedia) <http://en.wikipedia.org/wiki/DBSCAN>`, ` A Density-Based Algorithm for Discovering Clusters in
            Large Spatial Databases with Noise <http://www.dbs.ifi.lmu.de/Publikationen/Papers/KDD-96.final.frame.pdf>`
    """
    @typing.overload
    def __init__(self, double: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure): ...
    def cluster(self, collection: typing.Union[java.util.Collection[_DBSCANClusterer__T], typing.Sequence[_DBSCANClusterer__T], typing.Set[_DBSCANClusterer__T]]) -> java.util.List[Cluster[_DBSCANClusterer__T]]: ...
    def getEps(self) -> float:
        """
            Returns the maximum radius of the neighborhood to be considered.
        
            Returns:
                maximum radius of the neighborhood
        
        
        """
        ...
    def getMinPts(self) -> int:
        """
            Returns the minimum number of points needed for a cluster.
        
            Returns:
                minimum number of points needed for a cluster
        
        
        """
        ...

class DoublePoint(Clusterable, java.io.Serializable):
    """
    public class DoublePoint extends :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.clustering.Clusterable`, :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        A simple implementation of :class:`~org.hipparchus.clustering.Clusterable` for points with double coordinates.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, intArray: typing.List[int]): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def getPoint(self) -> typing.List[float]:
        """
            Gets the n-dimensional point.
        
            In this implementation of the :class:`~org.hipparchus.clustering.Clusterable` interface, the method *always* returns a
            reference to an internal array.
        
            Specified by:
                :meth:`~org.hipparchus.clustering.Clusterable.getPoint` in interface :class:`~org.hipparchus.clustering.Clusterable`
        
            Returns:
                the point array (beware, it may be a reference to an internal array)
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.clustering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...

_FuzzyKMeansClusterer__T = typing.TypeVar('_FuzzyKMeansClusterer__T', bound=Clusterable)  # <T>
class FuzzyKMeansClusterer(Clusterer[_FuzzyKMeansClusterer__T], typing.Generic[_FuzzyKMeansClusterer__T]):
    """
    public class FuzzyKMeansClusterer<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.Clusterer`<T>
    
        Fuzzy K-Means clustering algorithm.
    
        The Fuzzy K-Means algorithm is a variation of the classical K-Means algorithm, with the major difference that a single
        data point is not uniquely assigned to a single cluster. Instead, each point i has a set of weights u :sub:`ij` which
        indicate the degree of membership to the cluster j.
    
        The algorithm then tries to minimize the objective function:
    
        .. code-block: java
        
         J = ∑ :sub:`i=1..C` ∑ :sub:`k=1..N`  u :sub:`ik`  :sup:`m` d :sub:`ik`  :sup:`2` 
         
        with d :sub:`ik` being the distance between data point i and the cluster center k.
    
        The algorithm requires two parameters:
    
          - k: the number of clusters
          - fuzziness: determines the level of cluster fuzziness, larger values lead to fuzzier clusters
    
        Additional, optional parameters:
    
          - maxIterations: the maximum number of iterations
          - epsilon: the convergence criteria, default is 1e-3
    
    
        The fuzzy variant of the K-Means algorithm is more robust with regard to the selection of the initial cluster centers.
    """
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, int2: int, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure): ...
    @typing.overload
    def __init__(self, int: int, double: float, int2: int, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure, double2: float, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    def cluster(self, collection: typing.Union[java.util.Collection[_FuzzyKMeansClusterer__T], typing.Sequence[_FuzzyKMeansClusterer__T], typing.Set[_FuzzyKMeansClusterer__T]]) -> java.util.List[CentroidCluster[_FuzzyKMeansClusterer__T]]: ...
    def getClusters(self) -> java.util.List[CentroidCluster[_FuzzyKMeansClusterer__T]]: ...
    def getDataPoints(self) -> java.util.List[_FuzzyKMeansClusterer__T]: ...
    def getEpsilon(self) -> float:
        """
            Returns the convergence criteria used by this instance.
        
            Returns:
                the convergence criteria
        
        
        """
        ...
    def getFuzziness(self) -> float:
        """
            Returns the fuzziness factor used by this instance.
        
            Returns:
                the fuzziness factor
        
        
        """
        ...
    def getK(self) -> int:
        """
            Return the number of clusters this instance will use.
        
            Returns:
                the number of clusters
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
            Returns the maximum number of iterations this instance will use.
        
            Returns:
                the maximum number of iterations, or -1 if no maximum is set
        
        
        """
        ...
    def getMembershipMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns the :code:`nxk` membership matrix, where :code:`n` is the number of data points and :code:`k` the number of
            clusters.
        
            The element U :sub:`i,j` represents the membership value for data point :code:`i` to cluster :code:`j`.
        
            Returns:
                the membership matrix
        
            Raises:
                :class:`~org.hipparchus.clustering.https:.www.hipparchus.org.hipparchus`: if :meth:`~org.hipparchus.clustering.FuzzyKMeansClusterer.cluster` has not been called before
        
        
        """
        ...
    def getObjectiveFunctionValue(self) -> float:
        """
            Get the value of the objective function.
        
            Returns:
                the objective function evaluation as double value
        
            Raises:
                :class:`~org.hipparchus.clustering.https:.www.hipparchus.org.hipparchus`: if :meth:`~org.hipparchus.clustering.FuzzyKMeansClusterer.cluster` has not been called before
        
        
        """
        ...
    def getRandomGenerator(self) -> org.hipparchus.random.RandomGenerator:
        """
            Returns the random generator this instance will use.
        
            Returns:
                the random generator
        
        
        """
        ...

_KMeansPlusPlusClusterer__T = typing.TypeVar('_KMeansPlusPlusClusterer__T', bound=Clusterable)  # <T>
class KMeansPlusPlusClusterer(Clusterer[_KMeansPlusPlusClusterer__T], typing.Generic[_KMeansPlusPlusClusterer__T]):
    """
    public class KMeansPlusPlusClusterer<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.Clusterer`<T>
    
        Clustering algorithm based on David Arthur and Sergei Vassilvitski k-means++ algorithm.
    
        Also see:
            `K-means++ (wikipedia) <http://en.wikipedia.org/wiki/K-means%2B%2B>`
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure): ...
    @typing.overload
    def __init__(self, int: int, int2: int, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, int: int, int2: int, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure, randomGenerator: org.hipparchus.random.RandomGenerator, emptyClusterStrategy: 'KMeansPlusPlusClusterer.EmptyClusterStrategy'): ...
    def cluster(self, collection: typing.Union[java.util.Collection[_KMeansPlusPlusClusterer__T], typing.Sequence[_KMeansPlusPlusClusterer__T], typing.Set[_KMeansPlusPlusClusterer__T]]) -> java.util.List[CentroidCluster[_KMeansPlusPlusClusterer__T]]: ...
    def getEmptyClusterStrategy(self) -> 'KMeansPlusPlusClusterer.EmptyClusterStrategy':
        """
            Returns the :class:`~org.hipparchus.clustering.KMeansPlusPlusClusterer.EmptyClusterStrategy` used by this instance.
        
            Returns:
                the :class:`~org.hipparchus.clustering.KMeansPlusPlusClusterer.EmptyClusterStrategy`
        
        
        """
        ...
    def getK(self) -> int:
        """
            Return the number of clusters this instance will use.
        
            Returns:
                the number of clusters
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
            Returns the maximum number of iterations this instance will use.
        
            Returns:
                the maximum number of iterations, or -1 if no maximum is set
        
        
        """
        ...
    def getRandomGenerator(self) -> org.hipparchus.random.RandomGenerator:
        """
            Returns the random generator this instance will use.
        
            Returns:
                the random generator
        
        
        """
        ...
    class EmptyClusterStrategy(java.lang.Enum['KMeansPlusPlusClusterer.EmptyClusterStrategy']):
        LARGEST_VARIANCE: typing.ClassVar['KMeansPlusPlusClusterer.EmptyClusterStrategy'] = ...
        LARGEST_POINTS_NUMBER: typing.ClassVar['KMeansPlusPlusClusterer.EmptyClusterStrategy'] = ...
        FARTHEST_POINT: typing.ClassVar['KMeansPlusPlusClusterer.EmptyClusterStrategy'] = ...
        ERROR: typing.ClassVar['KMeansPlusPlusClusterer.EmptyClusterStrategy'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'KMeansPlusPlusClusterer.EmptyClusterStrategy': ...
        @staticmethod
        def values() -> typing.List['KMeansPlusPlusClusterer.EmptyClusterStrategy']: ...

_MultiKMeansPlusPlusClusterer__T = typing.TypeVar('_MultiKMeansPlusPlusClusterer__T', bound=Clusterable)  # <T>
class MultiKMeansPlusPlusClusterer(Clusterer[_MultiKMeansPlusPlusClusterer__T], typing.Generic[_MultiKMeansPlusPlusClusterer__T]):
    """
    public class MultiKMeansPlusPlusClusterer<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.Clusterer`<T>
    
        A wrapper around a k-means++ clustering algorithm which performs multiple trials and returns the best solution.
    """
    @typing.overload
    def __init__(self, kMeansPlusPlusClusterer: KMeansPlusPlusClusterer[_MultiKMeansPlusPlusClusterer__T], int: int): ...
    @typing.overload
    def __init__(self, kMeansPlusPlusClusterer: KMeansPlusPlusClusterer[_MultiKMeansPlusPlusClusterer__T], int: int, clusterEvaluator: org.hipparchus.clustering.evaluation.ClusterEvaluator[_MultiKMeansPlusPlusClusterer__T]): ...
    def cluster(self, collection: typing.Union[java.util.Collection[_MultiKMeansPlusPlusClusterer__T], typing.Sequence[_MultiKMeansPlusPlusClusterer__T], typing.Set[_MultiKMeansPlusPlusClusterer__T]]) -> java.util.List[CentroidCluster[_MultiKMeansPlusPlusClusterer__T]]: ...
    def getClusterEvaluator(self) -> org.hipparchus.clustering.evaluation.ClusterEvaluator[_MultiKMeansPlusPlusClusterer__T]: ...
    def getClusterer(self) -> KMeansPlusPlusClusterer[_MultiKMeansPlusPlusClusterer__T]: ...
    def getNumTrials(self) -> int:
        """
            Returns the number of trials this instance will do.
        
            Returns:
                the number of trials
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.clustering")``.

    CentroidCluster: typing.Type[CentroidCluster]
    Cluster: typing.Type[Cluster]
    Clusterable: typing.Type[Clusterable]
    Clusterer: typing.Type[Clusterer]
    DBSCANClusterer: typing.Type[DBSCANClusterer]
    DoublePoint: typing.Type[DoublePoint]
    FuzzyKMeansClusterer: typing.Type[FuzzyKMeansClusterer]
    KMeansPlusPlusClusterer: typing.Type[KMeansPlusPlusClusterer]
    LocalizedClusteringFormats: typing.Type[LocalizedClusteringFormats]
    MultiKMeansPlusPlusClusterer: typing.Type[MultiKMeansPlusPlusClusterer]
    distance: org.hipparchus.clustering.distance.__module_protocol__
    evaluation: org.hipparchus.clustering.evaluation.__module_protocol__
