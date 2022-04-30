import java.util
import org.hipparchus.clustering
import org.hipparchus.clustering.distance
import typing



_ClusterEvaluator__T = typing.TypeVar('_ClusterEvaluator__T', bound=org.hipparchus.clustering.Clusterable)  # <T>
class ClusterEvaluator(typing.Generic[_ClusterEvaluator__T]):
    """
    public abstract class ClusterEvaluator<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.evaluation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for cluster evaluation methods.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure): ...
    def isBetterScore(self, double: float, double2: float) -> bool:
        """
            Returns whether the first evaluation score is considered to be better than the second one by this evaluator.
        
            Specific implementations shall override this method if the returned scores do not follow the same ordering, i.e. smaller
            score is better.
        
            Parameters:
                score1 (double): the first score
                score2 (double): the second score
        
            Returns:
                :code:`true` if the first score is considered to be better, :code:`false` otherwise
        
        
        """
        ...
    def score(self, list: java.util.List[org.hipparchus.clustering.Cluster[_ClusterEvaluator__T]]) -> float: ...

_SumOfClusterVariances__T = typing.TypeVar('_SumOfClusterVariances__T', bound=org.hipparchus.clustering.Clusterable)  # <T>
class SumOfClusterVariances(ClusterEvaluator[_SumOfClusterVariances__T], typing.Generic[_SumOfClusterVariances__T]):
    """
    public class SumOfClusterVariances<T extends :class:`~org.hipparchus.clustering.Clusterable`> extends :class:`~org.hipparchus.clustering.evaluation.ClusterEvaluator`<T>
    
        Computes the sum of intra-cluster distance variances according to the formula: \] score = \sum\limits_{i=1}^n \sigma_i^2
        \] where n is the number of clusters and \( \sigma_i^2 \) is the variance of intra-cluster distances of cluster \( c_i
        \).
    """
    def __init__(self, distanceMeasure: org.hipparchus.clustering.distance.DistanceMeasure): ...
    def score(self, list: java.util.List[org.hipparchus.clustering.Cluster[_SumOfClusterVariances__T]]) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.clustering.evaluation")``.

    ClusterEvaluator: typing.Type[ClusterEvaluator]
    SumOfClusterVariances: typing.Type[SumOfClusterVariances]
