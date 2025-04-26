
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
    public classMax extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.rank.Max`>, :class:`~org.hipparchus.stat.descriptive.rank.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Returns the maximum of the available values.
    
          - The result is :code:`NaN` iff all values are :code:`NaN` (i.e. :code:`NaN` values have no impact on the value of the
            statistic).
          - If any of the values equals :code:`Double.POSITIVE_INFINITY`, the result is :code:`Double.POSITIVE_INFINITY.`
    
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, max: 'Max'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
            Aggregates the provided instance into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AggregatableStatistic.aggregate` in
                interface :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`
        
            Parameters:
                other (:class:`~org.hipparchus.stat.descriptive.rank.Max`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, max: 'Max') -> None: ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'Max':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...

class Median(org.hipparchus.stat.descriptive.AbstractUnivariateStatistic, java.io.Serializable):
    """
    public classMedian extends :class:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.rank.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Returns the median of the available values. This is the same as the 50th percentile. See
        :class:`~org.hipparchus.stat.descriptive.rank.Percentile` for a description of the algorithm used.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self): ...
    def copy(self) -> 'Median':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.copy` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    def getEstimationType(self) -> 'Percentile.EstimationType':
        """
            Get the estimation :class:`~org.hipparchus.stat.descriptive.rank.Percentile.EstimationType` used for computation.
        
            Returns:
                the :code:`estimationType` set
        
        
        """
        ...
    def getKthSelector(self) -> org.hipparchus.util.KthSelector:
        """
            Get the :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus` used for computation.
        
            Returns:
                the :code:`kthSelector` set
        
        
        """
        ...
    def getNaNStrategy(self) -> org.hipparchus.stat.ranking.NaNStrategy:
        """
            Get the :class:`~org.hipparchus.stat.ranking.NaNStrategy` strategy used for computation.
        
            Returns:
                :code:`NaN Handling` strategy set during construction
        
        
        """
        ...
    def withEstimationType(self, estimationType: 'Percentile.EstimationType') -> 'Median':
        """
            Build a new instance similar to the current one except for the
            :class:`~org.hipparchus.stat.descriptive.rank.Percentile.EstimationType`.
        
            Parameters:
                newEstimationType (:class:`~org.hipparchus.stat.descriptive.rank.Percentile.EstimationType`): estimation type for the new instance
        
            Returns:
                a new instance, with changed estimation type
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: when newEstimationType is null
        
        
        """
        ...
    def withKthSelector(self, kthSelector: org.hipparchus.util.KthSelector) -> 'Median':
        """
            Build a new instance similar to the current one except for the
            :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus` instance specifically set.
        
            Parameters:
                newKthSelector (:class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`): KthSelector for the new instance
        
            Returns:
                a new instance, with changed KthSelector
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: when newKthSelector is null
        
        
        """
        ...
    def withNaNStrategy(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy) -> 'Median':
        """
            Build a new instance similar to the current one except for the :class:`~org.hipparchus.stat.ranking.NaNStrategy`
            strategy.
        
            Parameters:
                newNaNStrategy (:class:`~org.hipparchus.stat.ranking.NaNStrategy`): NaN strategy for the new instance
        
            Returns:
                a new instance, with changed NaN handling strategy
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: when newNaNStrategy is null
        
        
        """
        ...

class Min(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Min'], java.io.Serializable):
    """
    public classMin extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.rank.Min`>, :class:`~org.hipparchus.stat.descriptive.rank.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Returns the minimum of the available values.
    
          - The result is :code:`NaN` iff all values are :code:`NaN` (i.e. :code:`NaN` values have no impact on the value of the
            statistic).
          - If any of the values equals :code:`Double.NEGATIVE_INFINITY`, the result is :code:`Double.NEGATIVE_INFINITY.`
    
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, min: 'Min'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
            Aggregates the provided instance into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AggregatableStatistic.aggregate` in
                interface :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`
        
            Parameters:
                other (:class:`~org.hipparchus.stat.descriptive.rank.Min`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, min: 'Min') -> None: ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'Min':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
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
    public classPercentile extends :class:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.rank.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Provides percentile computation.
    
        There are several commonly used methods for estimating percentiles (a.k.a. quantiles) based on sample data. For large
        samples, the different methods agree closely, but when sample sizes are small, different methods will give significantly
        different results. The algorithm implemented here works as follows:
    
          1.  Let :code:`n` be the length of the (sorted) array and :code:`0 < p <= 100` be the desired percentile.
          2.  If :code:`n = 1` return the unique array element (regardless of the value of :code:`p`); otherwise
          3.  Compute the estimated percentile position :code:`pos = p * (n + 1) / 100` and the difference, :code:`d` between
            :code:`pos` and :code:`floor(pos)` (i.e. the fractional part of :code:`pos`).
          4.  If :code:`pos < 1` return the smallest element in the array.
          5.  Else if :code:`pos >= n` return the largest element in the array.
          6.  Else let :code:`lower` be the element in position :code:`floor(pos)` in the array and let :code:`upper` be the next
            element in the array. Return :code:`lower + d * (upper - lower)`
    
    
        To compute percentiles, the data must be at least partially ordered. Input arrays are copied and recursively partitioned
        using an ordering definition. The ordering used by :code:`Arrays.sort(double[])` is the one determined by
        :meth:`~org.hipparchus.stat.descriptive.rank.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.compareTo`. This
        ordering makes :code:`Double.NaN` larger than any other value (including :code:`Double.POSITIVE_INFINITY`). Therefore,
        for example, the median (50th percentile) of :code:`{0, 1, 2, 3, 4, Double.NaN}` evaluates to :code:`2.5.`
    
        Since percentile estimation usually involves interpolation between array elements, arrays containing :code:`NaN` or
        infinite values will often result in :code:`NaN` or infinite values returned.
    
        Further, to include different estimation types such as R1, R2 as mentioned in `Quantile page(wikipedia)
        <http://en.wikipedia.org/wiki/Quantile>`, a type specific NaN handling strategy is used to closely match with the
        typically observed results from popular tools like R(R1-R9), Excel(R7).
    
        Percentile uses only selection instead of complete sorting and caches selection algorithm state between calls to the
        various :code:`evaluate` methods. This greatly improves efficiency, both for a single percentile and multiple percentile
        computations. To maximize performance when multiple percentiles are computed based on the same data, users should set
        the data array once using either one of the :meth:`~org.hipparchus.stat.descriptive.rank.Percentile.evaluate` or
        :meth:`~org.hipparchus.stat.descriptive.rank.Percentile.setData` methods and thereafter
        :meth:`~org.hipparchus.stat.descriptive.rank.Percentile.evaluate` with just the percentile provided.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
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
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.copy` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    @typing.overload
    def evaluate(self, double: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int, double2: float) -> float: ...
    def getEstimationType(self) -> 'Percentile.EstimationType':
        """
            Get the estimation :class:`~org.hipparchus.stat.descriptive.rank.Percentile.EstimationType` used for computation.
        
            Returns:
                the :code:`estimationType` set
        
        
        """
        ...
    def getKthSelector(self) -> org.hipparchus.util.KthSelector:
        """
            Get the :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus` used for computation.
        
            Returns:
                the :code:`kthSelector` set
        
        
        """
        ...
    def getNaNStrategy(self) -> org.hipparchus.stat.ranking.NaNStrategy:
        """
            Get the :class:`~org.hipparchus.stat.ranking.NaNStrategy` strategy used for computation.
        
            Returns:
                :code:`NaN Handling` strategy set during construction
        
        
        """
        ...
    def getPivotingStrategy(self) -> org.hipparchus.util.PivotingStrategy:
        """
            Get the :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus` used in KthSelector for
            computation.
        
            Returns:
                the pivoting strategy set
        
        
        """
        ...
    def getQuantile(self) -> float:
        """
            Returns the value of the quantile field (determines what percentile is computed when evaluate() is called with no
            quantile argument).
        
            Returns:
                quantile set while construction or :meth:`~org.hipparchus.stat.descriptive.rank.Percentile.setQuantile`
        
        
        """
        ...
    @typing.overload
    def setData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Set the data array.
        
            The stored value is a copy of the parameter array, not the array itself.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.setData` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic`
        
            Parameters:
                values (double[]): data array to store (may be null to remove stored data)
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.evaluate`
        
        
        public void setData(double[] values, int begin, int length) throws :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`
        
            Set the data array. The input array is copied, not referenced.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.setData` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic`
        
            Parameters:
                values (double[]): data array to store
                begin (int): the index of the first element to include
                length (int): the number of elements to include
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: if values is null or the indices are not valid
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.evaluate`
        
        
        
        """
        ...
    @typing.overload
    def setData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> None: ...
    def setQuantile(self, double: float) -> None: ...
    def withEstimationType(self, estimationType: 'Percentile.EstimationType') -> 'Percentile':
        """
            Build a new instance similar to the current one except for the
            :class:`~org.hipparchus.stat.descriptive.rank.Percentile.EstimationType`.
        
            This method is intended to be used as part of a fluent-type builder pattern. Building finely tune instances should be
            done as follows:
        
            .. code-block: java
            
               Percentile customized = new Percentile(quantile).
                                       withEstimationType(estimationType).
                                       withNaNStrategy(nanStrategy).
                                       withKthSelector(kthSelector);
             
        
            If any of the :code:`withXxx` method is omitted, the default value for the corresponding customization parameter will be
            used.
        
            Parameters:
                newEstimationType (:class:`~org.hipparchus.stat.descriptive.rank.Percentile.EstimationType`): estimation type for the new instance
        
            Returns:
                a new instance, with changed estimation type
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: when newEstimationType is null
        
        
        """
        ...
    def withKthSelector(self, kthSelector: org.hipparchus.util.KthSelector) -> 'Percentile':
        """
            Build a new instance similar to the current one except for the
            :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus` instance specifically set.
        
            This method is intended to be used as part of a fluent-type builder pattern. Building finely tune instances should be
            done as follows:
        
            .. code-block: java
            
               Percentile customized = new Percentile(quantile).
                                       withEstimationType(estimationType).
                                       withNaNStrategy(nanStrategy).
                                       withKthSelector(newKthSelector);
             
        
            If any of the :code:`withXxx` method is omitted, the default value for the corresponding customization parameter will be
            used.
        
            Parameters:
                newKthSelector (:class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`): KthSelector for the new instance
        
            Returns:
                a new instance, with changed KthSelector
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: when newKthSelector is null
        
        
        """
        ...
    def withNaNStrategy(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy) -> 'Percentile':
        """
            Build a new instance similar to the current one except for the :class:`~org.hipparchus.stat.ranking.NaNStrategy`
            strategy.
        
            This method is intended to be used as part of a fluent-type builder pattern. Building finely tune instances should be
            done as follows:
        
            .. code-block: java
            
               Percentile customized = new Percentile(quantile).
                                       withEstimationType(estimationType).
                                       withNaNStrategy(nanStrategy).
                                       withKthSelector(kthSelector);
             
        
            If any of the :code:`withXxx` method is omitted, the default value for the corresponding customization parameter will be
            used.
        
            Parameters:
                newNaNStrategy (:class:`~org.hipparchus.stat.ranking.NaNStrategy`): NaN strategy for the new instance
        
            Returns:
                a new instance, with changed NaN handling strategy
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: when newNaNStrategy is null
        
        
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
    public classRandomPercentile extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`, :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.rank.RandomPercentile`>, :class:`~org.hipparchus.stat.descriptive.rank.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        A :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic` estimating percentiles using the `RANDOM
        <http:/dimacs.rutgers.edu/~graham/pubs/papers/nquantiles.pdf>` Algorithm.
    
        Storage requirements for the RANDOM algorithm depend on the desired accuracy of quantile estimates. Quantile estimate
        accuracy is defined as follows.
    
        Let \(X\) be the set of all data values consumed from the stream and let \(q\) be a quantile (measured between 0 and 1)
        to be estimated. If
    
          - \(\epsilon\) is the configured accuracy
          - \(\hat{q}\) is a RandomPercentile estimate for \(q\) (what is returned by
            :meth:`~org.hipparchus.stat.descriptive.rank.RandomPercentile.getResult` or
            :meth:`~org.hipparchus.stat.descriptive.rank.RandomPercentile.getResult`) with \(100q\) as actual parameter)
          - \(rank(\hat{q}) = |\{x \in X : x < \hat{q}\}|\) is the actual rank of \(\hat{q}\) in the full data stream
          - \(n = |X|\) is the number of observations
    
        then we can expect \((q - \epsilon)n < rank(\hat{q}) < (q + \epsilon)n\).
    
        The algorithm maintains \(\left\lceil {log_{2}(1/\epsilon)}\right\rceil + 1\) buffers of size \(\left\lceil {1/\epsilon
        \sqrt{log_2(1/\epsilon)}}\right\rceil\). When :code:`epsilon` is set to the default value of \(10^{-4}\), this makes 15
        buffers of size 36,453.
    
        The algorithm uses the buffers to maintain samples of data from the stream. Until all buffers are full, the entire
        sample is stored in the buffers. If one of the :code:`getResult` methods is called when all data are available in memory
        and there is room to make a copy of the data (meaning the combined set of buffers is less than half full), the
        :code:`getResult` method delegates to a :class:`~org.hipparchus.stat.descriptive.rank.Percentile` instance to compute
        and return the exact value for the desired quantile. For default :code:`epsilon`, this means exact values will be
        returned whenever fewer than \(\left\lceil {15 \times 36453 / 2} \right\rceil = 273,398\) values have been consumed from
        the data stream.
    
        When buffers become full, the algorithm merges buffers so that they effectively represent a larger set of values than
        they can hold. Subsequently, data values are sampled from the stream to fill buffers freed by merge operations. Both the
        merging and the sampling require random selection, which is done using a :code:`RandomGenerator`. To get repeatable
        results for large data streams, users should provide :code:`RandomGenerator` instances with fixed seeds.
        :code:`RandomPercentile` itself does not reseed or otherwise initialize the :code:`RandomGenerator` provided to it. By
        default, it uses a :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus` generator with
        the default seed.
    
        Note: This implementation is not thread-safe.
    
        Also see:
    
              - :meth:`~serialized`
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_EPSILON
    
        Default quantile estimation error setting
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomPercentile: 'RandomPercentile'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None: ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, randomPercentile: 'RandomPercentile') -> None: ...
    def clear(self) -> None:
        """
            Description copied from class: :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear`
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'RandomPercentile':
        """
            Description copied from class: :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy`
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Returns an estimate of percentile over the given array.
        
            Parameters:
                percentile (double): desired percentile (scaled 0 - 100)
                values (double[]): source of input data
        
            Returns:
                estimated percentile
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: if percentile is out of the range [0, 100]
        
        
        """
        ...
    @typing.overload
    def evaluate(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Returns an estimate of the median, computed using the designated array segment as input data.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.evaluate` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.evaluate` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Parameters:
                values (double[]): source of input data
                begin (int): position of the first element of the values array to include
                length (int): number of array elements to include
        
            Returns:
                estimated percentile
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: if percentile is out of the range [0, 100]
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.evaluate`
        
        
        """
        ...
    @typing.overload
    def evaluate(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    def getAggregateN(self, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...
    def getAggregateQuantileRank(self, double: float, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...
    def getAggregateRank(self, double: float, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...
    def getN(self) -> int:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN`
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getQuantileRank(self, double: float) -> float:
        """
            Returns the estimated quantile position of value in the dataset. Specifically, what is returned is an estimate of \(|\{x
            \in X : x < value\}| / |X|\) where \(X\) is the set of values that have been consumed from the stream.
        
            Parameters:
                value (double): value whose quantile rank is sought.
        
            Returns:
                estimated proportion of sample values that are strictly less than :code:`value`
        
        
        """
        ...
    def getRank(self, double: float) -> float:
        """
            Gets the estimated rank of :code:`value`, i.e. \(|\{x \in X : x < value\}|\) where \(X\) is the set of values that have
            been consumed from the stream.
        
            Parameters:
                value (double): value whose overall rank is sought
        
            Returns:
                estimated number of sample values that are strictly less than :code:`value`
        
        
        """
        ...
    @typing.overload
    def getResult(self) -> float:
        """
            Returns an estimate of the median.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        """
        ...
    @typing.overload
    def getResult(self, double: float) -> float:
        """
            Returns an estimate of the given percentile.
        
            Parameters:
                percentile (double): desired percentile (scaled 0 - 100)
        
            Returns:
                estimated percentile
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: if percentile is out of the range [0, 100]
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Description copied from class: :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment`
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment` in
                class :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...
    @staticmethod
    def maxValuesRetained(double: float) -> int:
        """
            Returns the maximum number of :code:`double` values that a :code:`RandomPercentile` instance created with the given
            :code:`epsilon` value will retain in memory.
        
            If the number of values that have been consumed from the stream is less than 1/2 of this value, reported statistics are
            exact.
        
            Parameters:
                epsilon (double): bound on the relative quantile error (see class javadoc)
        
            Returns:
                upper bound on the total number of primitive double values retained in memory
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.rank.https:.www.hipparchus.org.hipparchus`: if epsilon is not in the interval (0,1)
        
        
        """
        ...
    def reduce(self, double: float, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.rank")``.

    Max: typing.Type[Max]
    Median: typing.Type[Median]
    Min: typing.Type[Min]
    PSquarePercentile: typing.Type[PSquarePercentile]
    Percentile: typing.Type[Percentile]
    RandomPercentile: typing.Type[RandomPercentile]
