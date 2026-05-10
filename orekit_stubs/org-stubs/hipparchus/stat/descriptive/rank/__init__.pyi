
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus.random
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.ranking
import org.hipparchus.util
import typing



class Max(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Max'], java.io.Serializable):
    """
    Returns the maximum of the available values.
    
      - The result is NaN iff all values are NaN (i.e. NaN values have no impact on the value of the
        statistic).
      - If any of the values equals POSITIVE_INFINITY, the result is POSITIVE_INFINITY
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, original: 'Max'): ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Aggregates the provided instance into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Specified by: aggregate in interface AggregatableStatistic
        
        Parameters:
            other (Max): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'Max') -> None: ...
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        Specified by: clear in class AbstractStorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> 'Max':
        """
        Returns a copy of the statistic with the same internal state.
        
        Specified by: copy in interface StorelessUnivariateStatistic
        
        Specified by: copy in interface UnivariateStatistic
        
        Specified by: copy in class AbstractStorelessUnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    def getN(self) -> int:
        """
        Returns the number of values that have been added.
        
        Specified by: getN in interface StorelessUnivariateStatistic
        
        Returns:
            the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
        Returns the current value of the Statistic.
        
        Specified by: getResult in interface StorelessUnivariateStatistic
        
        Specified by: getResult in class AbstractStorelessUnivariateStatistic
        
        Returns:
            value of the statistic, NaN if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, d: float) -> None:
        """
        Updates the internal state of the statistic to reflect the addition of the new value.
        
        Specified by: increment in interface StorelessUnivariateStatistic
        
        Specified by: increment in class AbstractStorelessUnivariateStatistic
        
        Parameters:
            d (double): the new value.
        
        
        """
        ...

class Median(org.hipparchus.stat.descriptive.AbstractUnivariateStatistic, java.io.Serializable):
    """
    Returns the median of the available values. This is the same as the 50th percentile. See Percentile for a description of the algorithm used.
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    def __init__(self):
        """
        Default constructor.
        """
        ...
    def copy(self) -> 'Median':
        """
        Returns a copy of the statistic with the same internal state.
        
        Specified by: copy in interface UnivariateStatistic
        
        Specified by: copy in class AbstractUnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    def getEstimationType(self) -> 'Percentile.EstimationType':
        """
        Get the estimation EstimationType used for computation.
        
        Returns:
            the estimationType set
        
        
        """
        ...
    def getKthSelector(self) -> org.hipparchus.util.KthSelector:
        """
        Get the hipparchus used for computation.
        
        Returns:
            the kthSelector set
        
        
        """
        ...
    def getNaNStrategy(self) -> org.hipparchus.stat.ranking.NaNStrategy:
        """
        Get the NaNStrategy strategy used for computation.
        
        Returns:
            NaN Handling strategy set during construction
        
        
        """
        ...
    def withEstimationType(self, newEstimationType: 'Percentile.EstimationType') -> 'Median':
        """
        Build a new instance similar to the current one except for the EstimationType.
        
        Parameters:
            newEstimationType (EstimationType): estimation type for the new instance
        
        Returns:
            a new instance, with changed estimation type
        
        Raises:
            hipparchus: when newEstimationType is null
        
        
        """
        ...
    def withKthSelector(self, newKthSelector: org.hipparchus.util.KthSelector) -> 'Median':
        """
        Build a new instance similar to the current one except for the hipparchus instance specifically set.
        
        Parameters:
            newKthSelector (hipparchus): KthSelector for the new instance
        
        Returns:
            a new instance, with changed KthSelector
        
        Raises:
            hipparchus: when newKthSelector is null
        
        
        """
        ...
    def withNaNStrategy(self, newNaNStrategy: org.hipparchus.stat.ranking.NaNStrategy) -> 'Median':
        """
        Build a new instance similar to the current one except for the NaNStrategy strategy.
        
        Parameters:
            newNaNStrategy (NaNStrategy): NaN strategy for the new instance
        
        Returns:
            a new instance, with changed NaN handling strategy
        
        Raises:
            hipparchus: when newNaNStrategy is null
        
        
        """
        ...

class Min(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Min'], java.io.Serializable):
    """
    Returns the minimum of the available values.
    
      - The result is NaN iff all values are NaN (i.e. NaN values have no impact on the value of the
        statistic).
      - If any of the values equals NEGATIVE_INFINITY, the result is NEGATIVE_INFINITY
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, original: 'Min'): ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Aggregates the provided instance into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Specified by: aggregate in interface AggregatableStatistic
        
        Parameters:
            other (Min): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'Min') -> None: ...
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        Specified by: clear in class AbstractStorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> 'Min':
        """
        Returns a copy of the statistic with the same internal state.
        
        Specified by: copy in interface StorelessUnivariateStatistic
        
        Specified by: copy in interface UnivariateStatistic
        
        Specified by: copy in class AbstractStorelessUnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    def getN(self) -> int:
        """
        Returns the number of values that have been added.
        
        Specified by: getN in interface StorelessUnivariateStatistic
        
        Returns:
            the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
        Returns the current value of the Statistic.
        
        Specified by: getResult in interface StorelessUnivariateStatistic
        
        Specified by: getResult in class AbstractStorelessUnivariateStatistic
        
        Returns:
            value of the statistic, NaN if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, d: float) -> None:
        """
        Updates the internal state of the statistic to reflect the addition of the new value.
        
        Specified by: increment in interface StorelessUnivariateStatistic
        
        Specified by: increment in class AbstractStorelessUnivariateStatistic
        
        Parameters:
            d (double): the new value.
        
        
        """
        ...

class PSquarePercentile(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.StorelessUnivariateStatistic, java.io.Serializable):
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, pSquarePercentile: 'PSquarePercentile'): ...
    def clear(self) -> None: ...
    def copy(self) -> 'PSquarePercentile': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getN(self) -> int: ...
    def getQuantile(self) -> float: ...
    def getResult(self) -> float: ...
    def hashCode(self) -> int: ...
    def increment(self, double: float) -> None: ...
    @staticmethod
    def newMarkers(list: java.util.List[float], double: float) -> 'PSquarePercentile.PSquareMarkers': ...
    def quantile(self) -> float: ...
    def toString(self) -> str: ...
    class PSquareMarkers: ...

class Percentile(org.hipparchus.stat.descriptive.AbstractUnivariateStatistic, java.io.Serializable):
    """
    Provides percentile computation.
    
    There are several commonly used methods for estimating percentiles (a.k.a. quantiles) based on sample data. For large samples, the different methods agree closely, but when sample sizes are small, different methods will give significantly different results. The algorithm implemented here works as follows:
    
      1.  Let n be the length of the (sorted) array and 0 < p <= 100 be the desired percentile. 2.  If n = 1 return the unique array element (regardless of the value of p); otherwise 3.  Compute the estimated percentile position pos = p * (n + 1) / 100 and the difference, d between pos and floor(pos) (i.e. the fractional part of pos). 4.  If pos < 1 return the smallest element in the array. 5.  Else if pos >= n return the largest element in the array. 6.  Else let lower be the element in position floor(pos) in the array and let upper be the next element in the array. Return lower + d * (upper - lower)
    
    To compute percentiles, the data must be at least partially ordered. Input arrays are copied and recursively partitioned using an ordering definition. The ordering used by sort(double[]) is the one determined by Double. This ordering makes NaN larger than any other value (including POSITIVE_INFINITY). Therefore, for example, the median (50th percentile) of NaN} evaluates to
    
    Since percentile estimation usually involves interpolation between array elements, arrays containing NaN or infinite values will often result in NaN or infinite values returned.
    
    Further, to include different estimation types such as R1, R2 as mentioned in `Quantile page(wikipedia) <http://en.wikipedia.org/wiki/Quantile>`, a type specific NaN handling strategy is used to closely match with the typically observed results from popular tools like R(R1-R9), Excel(R7).
    
    Percentile uses only selection instead of complete sorting and caches selection algorithm state between calls to the various evaluate methods. This greatly improves efficiency, both for a single percentile and multiple percentile computations. To maximize performance when multiple percentiles are computed based on the same data, users should set the data array once using either one of the evaluate or setData methods and thereafter evaluate with just the percentile provided.
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, percentile: 'Percentile'): ...
    def copy(self) -> 'Percentile':
        """
        Returns a copy of the statistic with the same internal state.
        
        Specified by: copy in interface UnivariateStatistic
        
        Specified by: copy in class AbstractUnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, p: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    @typing.overload
    def evaluate(self, p: float) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], p: float) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], start: int, length: int) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int, p: float) -> float: ...
    def getEstimationType(self) -> 'Percentile.EstimationType':
        """
        Get the estimation EstimationType used for computation.
        
        Returns:
            the estimationType set
        
        
        """
        ...
    def getKthSelector(self) -> org.hipparchus.util.KthSelector:
        """
        Get the hipparchus used for computation.
        
        Returns:
            the kthSelector set
        
        
        """
        ...
    def getNaNStrategy(self) -> org.hipparchus.stat.ranking.NaNStrategy:
        """
        Get the NaNStrategy strategy used for computation.
        
        Returns:
            NaN Handling strategy set during construction
        
        
        """
        ...
    def getPivotingStrategy(self) -> org.hipparchus.util.PivotingStrategy:
        """
        Get the hipparchus used in KthSelector for computation.
        
        Returns:
            the pivoting strategy set
        
        
        """
        ...
    def getQuantile(self) -> float:
        """
        Returns the value of the quantile field (determines what percentile is computed when evaluate() is called with no quantile argument).
        
        Returns:
            quantile set while construction or setQuantile
        
        
        """
        ...
    @typing.overload
    def setData(self, values: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the data array.
        
        The stored value is a copy of the parameter array, not the array itself.
        
        Overrides: setData in class AbstractUnivariateStatistic
        
        Parameters:
            values (double[]): data array to store (may be null to remove stored data)
        
        Also see:
            evaluate
        
        public void setData (double[] values, int begin, int length) throws hipparchus
        
        Set the data array. The input array is copied, not referenced.
        
        Overrides: setData in class AbstractUnivariateStatistic
        
        Parameters:
            values (double[]): data array to store
            begin (int): the index of the first element to include
            length (int): the number of elements to include
        
        Raises:
            hipparchus: if values is null or the indices are not valid
        
        Also see:
            evaluate
        
        
        """
        ...
    @typing.overload
    def setData(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> None: ...
    def setQuantile(self, p: float) -> None:
        """
        Sets the value of the quantile field (determines what percentile is computed when evaluate() is called with no quantile argument).
        
        Parameters:
            p (double): a value between 0 < p <= 100
        
        Raises:
            hipparchus: if p is not greater than 0 and less than or equal to 100
        
        
        """
        ...
    def withEstimationType(self, newEstimationType: 'Percentile.EstimationType') -> 'Percentile':
        """
        Build a new instance similar to the current one except for the EstimationType.
        
        This method is intended to be used as part of a fluent-type builder pattern. Building finely tune instances should be done as follows:
        
        
           Percentile customized = new Percentile(quantile).
                                   withEstimationType(estimationType).
                                   withNaNStrategy(nanStrategy).
                                   withKthSelector(kthSelector);
         
        
        If any of the withXxx method is omitted, the default value for the corresponding customization parameter will be used.
        
        Parameters:
            newEstimationType (EstimationType): estimation type for the new instance
        
        Returns:
            a new instance, with changed estimation type
        
        Raises:
            hipparchus: when newEstimationType is null
        
        
        """
        ...
    def withKthSelector(self, newKthSelector: org.hipparchus.util.KthSelector) -> 'Percentile':
        """
        Build a new instance similar to the current one except for the hipparchus instance specifically set.
        
        This method is intended to be used as part of a fluent-type builder pattern. Building finely tune instances should be done as follows:
        
        
           Percentile customized = new Percentile(quantile).
                                   withEstimationType(estimationType).
                                   withNaNStrategy(nanStrategy).
                                   withKthSelector(newKthSelector);
         
        
        If any of the withXxx method is omitted, the default value for the corresponding customization parameter will be used.
        
        Parameters:
            newKthSelector (hipparchus): KthSelector for the new instance
        
        Returns:
            a new instance, with changed KthSelector
        
        Raises:
            hipparchus: when newKthSelector is null
        
        
        """
        ...
    def withNaNStrategy(self, newNaNStrategy: org.hipparchus.stat.ranking.NaNStrategy) -> 'Percentile':
        """
        Build a new instance similar to the current one except for the NaNStrategy strategy.
        
        This method is intended to be used as part of a fluent-type builder pattern. Building finely tune instances should be done as follows:
        
        
           Percentile customized = new Percentile(quantile).
                                   withEstimationType(estimationType).
                                   withNaNStrategy(nanStrategy).
                                   withKthSelector(kthSelector);
         
        
        If any of the withXxx method is omitted, the default value for the corresponding customization parameter will be used.
        
        Parameters:
            newNaNStrategy (NaNStrategy): NaN strategy for the new instance
        
        Returns:
            a new instance, with changed NaN handling strategy
        
        Raises:
            hipparchus: when newNaNStrategy is null
        
        
        """
        ...
    class EstimationType(java.lang.Enum['Percentile.EstimationType']):
        LEGACY: typing.ClassVar['Percentile.EstimationType'] = ...
        R_1: typing.ClassVar['Percentile.EstimationType'] = ...
        R_2: typing.ClassVar['Percentile.EstimationType'] = ...
        R_3: typing.ClassVar['Percentile.EstimationType'] = ...
        R_4: typing.ClassVar['Percentile.EstimationType'] = ...
        R_5: typing.ClassVar['Percentile.EstimationType'] = ...
        R_6: typing.ClassVar['Percentile.EstimationType'] = ...
        R_7: typing.ClassVar['Percentile.EstimationType'] = ...
        R_8: typing.ClassVar['Percentile.EstimationType'] = ...
        R_9: typing.ClassVar['Percentile.EstimationType'] = ...
        def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, kthSelector: org.hipparchus.util.KthSelector) -> float: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Percentile.EstimationType': ...
        @staticmethod
        def values() -> typing.MutableSequence['Percentile.EstimationType']: ...

class RandomPercentile(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.StorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['RandomPercentile'], java.io.Serializable):
    """
    A StorelessUnivariateStatistic estimating percentiles using the `RANDOM <http:/dimacs.rutgers.edu/~graham/pubs/papers/nquantiles.pdf>` Algorithm.
    
    Storage requirements for the RANDOM algorithm depend on the desired accuracy of quantile estimates. Quantile estimate accuracy is defined as follows.
    
    Let \(X\) be the set of all data values consumed from the stream and let \(q\) be a quantile (measured between 0 and 1) to be estimated. If
    
      - \(\epsilon\) is the configured accuracy
      - \(\hat{q}\) is a RandomPercentile estimate for \(q\) (what is returned by
        getResult or
        getResult) with \(100q\) as actual parameter)
      - \(rank(\hat{q}) = |\{x \in X : x < \hat{q}\}|\) is the actual rank of \(\hat{q}\) in the full data stream
      - \(n = |X|\) is the number of observations
    
    then we can expect \((q - \epsilon)n < rank(\hat{q}) < (q + \epsilon)n\).
    
    The algorithm maintains \(\left\lceil {log_{2}(1/\epsilon)}\right\rceil + 1\) buffers of size \(\left\lceil {1/\epsilon \sqrt{log_2(1/\epsilon)}}\right\rceil\). When epsilon is set to the default value of \(10^{-4}\), this makes 15 buffers of size 36,453.
    
    The algorithm uses the buffers to maintain samples of data from the stream. Until all buffers are full, the entire sample is stored in the buffers. If one of the getResult methods is called when all data are available in memory and there is room to make a copy of the data (meaning the combined set of buffers is less than half full), the getResult method delegates to a Percentile instance to compute and return the exact value for the desired quantile. For default epsilon, this means exact values will be returned whenever fewer than \(\left\lceil {15 \times 36453 / 2} \right\rceil = 273,398\) values have been consumed from the data stream.
    
    When buffers become full, the algorithm merges buffers so that they effectively represent a larger set of values than they can hold. Subsequently, data values are sampled from the stream to fill buffers freed by merge operations. Both the merging and the sampling require random selection, which is done using a RandomGenerator. To get repeatable results for large data streams, users should provide RandomGenerator instances with fixed seeds. RandomPercentile itself does not reseed or otherwise initialize the RandomGenerator provided to it. By default, it uses a hipparchus generator with the default seed.
    
    Note: This implementation is not thread-safe.
    
    Also see:
        serialized
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    Default quantile estimation error setting
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, epsilon: float, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomPercentile: 'RandomPercentile'): ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None: ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'RandomPercentile') -> None: ...
    def clear(self) -> None:
        """
        Description copied from class: clear Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        Specified by: clear in class AbstractStorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> 'RandomPercentile':
        """
        Description copied from class: copy Returns a copy of the statistic with the same internal state.
        
        Specified by: copy in interface StorelessUnivariateStatistic
        
        Specified by: copy in interface UnivariateStatistic
        
        Specified by: copy in class AbstractStorelessUnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Returns an estimate of percentile over the given array.
        
        Parameters:
            values (double): source of input data
            percentile (double[]): desired percentile (scaled 0 - 100)
        
        Returns:
            estimated percentile
        
        Raises:
            hipparchus: if percentile is out of the range [0, 100]
        
        
        """
        ...
    @typing.overload
    def evaluate(self, percentile: float, values: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Returns an estimate of the median, computed using the designated array segment as input data.
        
        Specified by: hipparchus in interface hipparchus
        
        Specified by: evaluate in interface StorelessUnivariateStatistic
        
        Specified by: evaluate in interface UnivariateStatistic
        
        Parameters:
            values (double[]): source of input data
            begin (int): position of the first element of the values array to include
            length (int): number of array elements to include
        
        Returns:
            estimated percentile
        
        Raises:
            hipparchus: if percentile is out of the range [0, 100]
        
        Also see:
            evaluate
        
        """
        ...
    @typing.overload
    def evaluate(self, percentile: float, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    def getAggregateN(self, aggregates: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float:
        """
        Returns the total number of values that have been consumed by the aggregates.
        
        Parameters:
            aggregates (Collection<RandomPercentile> aggregates): collection of RandomPercentile instances whose combined sample size is sought
        
        Returns:
            total number of values that have been consumed by the aggregates
        
        
        """
        ...
    def getAggregateQuantileRank(self, value: float, aggregates: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float:
        """
        Returns the estimated quantile position of value in the combined dataset of the aggregates. Specifically, what is returned is an estimate of \(|\{x \in X : x < value\}| / |X|\) where \(X\) is the set of values that have been consumed from all of the datastreams feeding the aggregates.
        
        Parameters:
            value (double): value whose quantile rank is sought.
            aggregates (Collection<RandomPercentile> aggregates): collection of RandomPercentile instances being combined
        
        Returns:
            estimated proportion of combined sample values that are strictly less than value
        
        
        """
        ...
    def getAggregateRank(self, value: float, aggregates: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float:
        """
        Computes the estimated rank of value in the combined dataset of the aggregates. Sums the values from getRank.
        
        Parameters:
            value (double): value whose rank is sought
            aggregates (Collection<RandomPercentile> aggregates): collection to aggregate rank over
        
        Returns:
            estimated number of elements in the combined dataset that are less than value
        
        
        """
        ...
    def getN(self) -> int:
        """
        Description copied from interface: getN Returns the number of values that have been added.
        
        Specified by: getN in interface StorelessUnivariateStatistic
        
        Returns:
            the number of values.
        
        
        """
        ...
    def getQuantileRank(self, value: float) -> float:
        """
        Returns the estimated quantile position of value in the dataset. Specifically, what is returned is an estimate of \(|\{x \in X : x < value\}| / |X|\) where \(X\) is the set of values that have been consumed from the stream.
        
        Parameters:
            value (double): value whose quantile rank is sought.
        
        Returns:
            estimated proportion of sample values that are strictly less than value
        
        
        """
        ...
    def getRank(self, value: float) -> float:
        """
        Gets the estimated rank of value, i.e. \(|\{x \in X : x < value\}|\) where \(X\) is the set of values that have been consumed from the stream.
        
        Parameters:
            value (double): value whose overall rank is sought
        
        Returns:
            estimated number of sample values that are strictly less than value
        
        
        """
        ...
    @typing.overload
    def getResult(self) -> float:
        """
        Returns an estimate of the median.
        
        Specified by: getResult in interface StorelessUnivariateStatistic
        
        Specified by: getResult in class AbstractStorelessUnivariateStatistic
        
        Returns:
            value of the statistic, NaN if it has been cleared or just instantiated.
        
        """
        ...
    @typing.overload
    def getResult(self, percentile: float) -> float:
        """
        Returns an estimate of the given percentile.
        
        Parameters:
            percentile (double): desired percentile (scaled 0 - 100)
        
        Returns:
            estimated percentile
        
        Raises:
            hipparchus: if percentile is out of the range [0, 100]
        
        
        """
        ...
    def increment(self, d: float) -> None:
        """
        Description copied from class: increment Updates the internal state of the statistic to reflect the addition of the new value.
        
        Specified by: increment in interface StorelessUnivariateStatistic
        
        Specified by: increment in class AbstractStorelessUnivariateStatistic
        
        Parameters:
            d (double): the new value.
        
        
        """
        ...
    @staticmethod
    def maxValuesRetained(epsilon: float) -> int:
        """
        Returns the maximum number of double values that a RandomPercentile instance created with the given epsilon value will retain in memory.
        
        If the number of values that have been consumed from the stream is less than 1/2 of this value, reported statistics are exact.
        
        Parameters:
            epsilon (double): bound on the relative quantile error (see class javadoc)
        
        Returns:
            upper bound on the total number of primitive double values retained in memory
        
        Raises:
            hipparchus: if epsilon is not in the interval (0,1)
        
        
        """
        ...
    def reduce(self, percentile: float, aggregates: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float:
        """
        Computes the given percentile by combining the data from the collection of aggregates. The result describes the combined sample of all data added to any of the aggregates.
        
        Parameters:
            percentile (double): desired percentile (scaled 0-100)
            aggregates (Collection<RandomPercentile> aggregates): RandomPercentile instances to combine data from
        
        Returns:
            estimate of the given percentile using combined data from the aggregates
        
        Raises:
            hipparchus: if percentile is out of the range [0, 100]
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.rank")``.

    Max: typing.Type[Max]
    Median: typing.Type[Median]
    Min: typing.Type[Min]
    PSquarePercentile: typing.Type[PSquarePercentile]
    Percentile: typing.Type[Percentile]
    RandomPercentile: typing.Type[RandomPercentile]
