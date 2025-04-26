
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import java.util.function
import jpype
import org.hipparchus.linear
import org.hipparchus.random
import org.hipparchus.stat.descriptive.moment
import org.hipparchus.stat.descriptive.rank
import org.hipparchus.stat.descriptive.summary
import org.hipparchus.stat.descriptive.vector
import org.hipparchus.util
import typing



_AggregatableStatistic__T = typing.TypeVar('_AggregatableStatistic__T')  # <T>
class AggregatableStatistic(typing.Generic[_AggregatableStatistic__T]):
    """
    public interfaceAggregatableStatistic<T>
    
        An interface for statistics that can aggregate results.
    """
    @typing.overload
    def aggregate(self, t: _AggregatableStatistic__T) -> None:
        """
            Aggregates the results from the provided instances into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Parameters:
                others (:class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`...): the other instances to aggregate into this instance
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.https:.www.hipparchus.org.hipparchus`: if either others or any instance is null
        
        default void aggregate(:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable`<:class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`> others)
        
            Aggregates the results from the provided instances into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Parameters:
                others (:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable`<:class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`> others): the other instances to aggregate into this instance
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.https:.www.hipparchus.org.hipparchus`: if either others or any instance is null
        
        
        """
        ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[_AggregatableStatistic__T], typing.Sequence[_AggregatableStatistic__T], typing.Set[_AggregatableStatistic__T], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None: ...
    @typing.overload
    def aggregate(self, *t: _AggregatableStatistic__T) -> None: ...

class StatisticalMultivariateSummary:
    """
    public interfaceStatisticalMultivariateSummary
    
        Reporting interface for basic multivariate statistics.
    """
    def getCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns the covariance of the available values.
        
            Returns:
                The covariance, null if no multivariate sample have been added or a zeroed matrix for a single value set.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the dimension of the data
        
            Returns:
                The dimension of the data
        
        
        """
        ...
    def getGeometricMean(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the geometric mean of the i :sup:`th` entries of the arrays that correspond
            to each multivariate sample
        
            Returns:
                the array of component geometric means
        
        
        """
        ...
    def getMax(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the maximum of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Returns:
                the array of component maxima
        
        
        """
        ...
    def getMean(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the mean of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Returns:
                the array of component means
        
        
        """
        ...
    def getMin(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the minimum of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Returns:
                the array of component minima
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of available values
        
            Returns:
                The number of available values
        
        
        """
        ...
    def getStandardDeviation(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the standard deviation of the i :sup:`th` entries of the arrays that
            correspond to each multivariate sample
        
            Returns:
                the array of component standard deviations
        
        
        """
        ...
    def getSum(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the sum of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Returns:
                the array of component sums
        
        
        """
        ...
    def getSumLog(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the sum of logs of the i :sup:`th` entries of the arrays that correspond to
            each multivariate sample
        
            Returns:
                the array of component log sums
        
        
        """
        ...
    def getSumSq(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the sum of squares of the i :sup:`th` entries of the arrays that correspond
            to each multivariate sample
        
            Returns:
                the array of component sums of squares
        
        
        """
        ...

class StatisticalSummary:
    """
    public interfaceStatisticalSummary
    
        Reporting interface for basic univariate statistics.
    """
    @typing.overload
    @staticmethod
    def aggregate(iterable: typing.Union[java.lang.Iterable['StatisticalSummary'], typing.Sequence['StatisticalSummary'], typing.Set['StatisticalSummary'], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> 'StatisticalSummary':
        """
            Computes aggregated statistical summaries.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the returned
            StatisticalSummary should contain the same values that would have been obtained by computing a single StatisticalSummary
            over the combined dataset.
        
            Parameters:
                statistics (:class:`~org.hipparchus.stat.descriptive.StatisticalSummary`...): StatisticalSummary instances to aggregate
        
            Returns:
                summary statistics for the combined dataset
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.https:.www.hipparchus.org.hipparchus`: if the input is null
        
        static :class:`~org.hipparchus.stat.descriptive.StatisticalSummary` aggregate(:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable`<? extends :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`> statistics)
        
            Computes aggregated statistical summaries.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the returned
            StatisticalSummary should contain the same values that would have been obtained by computing a single StatisticalSummary
            over the combined dataset.
        
            Parameters:
                statistics (:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable`<? extends :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`> statistics): iterable of StatisticalSummary instances to aggregate
        
            Returns:
                summary statistics for the combined dataset
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.https:.www.hipparchus.org.hipparchus`: if the input is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def aggregate(*statisticalSummary: 'StatisticalSummary') -> 'StatisticalSummary': ...
    def getMax(self) -> float:
        """
            Returns the maximum of the available values
        
            Returns:
                The max or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMean(self) -> float:
        """
            Returns the ` arithmetic mean <http://www.xycoon.com/arithmetic_mean.htm>` of the available values
        
            Returns:
                The mean or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Returns the minimum of the available values
        
            Returns:
                The min or Double.NaN if no values have been added.
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of available values
        
            Returns:
                The number of available values
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
            Returns the standard deviation of the available values.
        
            Returns:
                The standard deviation, Double.NaN if no values have been added or 0.0 for a single value set.
        
        
        """
        ...
    def getSum(self) -> float:
        """
            Returns the sum of the values that have been added to Univariate.
        
            Returns:
                The sum or Double.NaN if no values have been added
        
        
        """
        ...
    def getVariance(self) -> float:
        """
            Returns the variance of the available values.
        
            Returns:
                The variance, Double.NaN if no values have been added or 0.0 for a single value set.
        
        
        """
        ...

class StorelessMultivariateStatistic:
    """
    public interfaceStorelessMultivariateStatistic
    
        Base interface implemented by storeless multivariate statistics.
    """
    def clear(self) -> None:
        """
            Clears the internal state of the statistic.
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the dimension of the statistic.
        
            Returns:
                the dimension of the statistic
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> typing.MutableSequence[float]:
        """
            Returns the current value of the Statistic.
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Parameters:
                d (double[]): the new value
        
        
        """
        ...

class UnivariateStatistic(org.hipparchus.util.MathArrays.Function):
    """
    public interfaceUnivariateStatisticextends :class:`~org.hipparchus.stat.descriptive.https:.www.hipparchus.org.hipparchus`
    
        Base interface implemented by all statistics.
    """
    def copy(self) -> 'UnivariateStatistic':
        """
            Returns a copy of the statistic with the same internal state.
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...

class WeightedEvaluation:
    """
    public interfaceWeightedEvaluation
    
        Weighted evaluation for statistics.
    """
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...

class AbstractUnivariateStatistic(UnivariateStatistic):
    """
    public abstract classAbstractUnivariateStatistic extends :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
    
        Abstract base class for implementations of the :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic` interface.
    """
    def copy(self) -> UnivariateStatistic:
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    def getData(self) -> typing.MutableSequence[float]:
        """
            Get a copy of the stored data array.
        
            Returns:
                copy of the stored data array (may be null)
        
        
        """
        ...
    @typing.overload
    def setData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Set the data array.
        
            The stored value is a copy of the parameter array, not the array itself.
        
            Parameters:
                values (double[]): data array to store (may be null to remove stored data)
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.evaluate`
        
        
        public void setData(double[] values, int begin, int length) throws :class:`~org.hipparchus.stat.descriptive.https:.www.hipparchus.org.hipparchus`
        
            Set the data array. The input array is copied, not referenced.
        
            Parameters:
                values (double[]): data array to store
                begin (int): the index of the first element to include
                length (int): the number of elements to include
        
            Raises:
                :class:`~org.hipparchus.stat.descriptive.https:.www.hipparchus.org.hipparchus`: if values is null or the indices are not valid
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.descriptive.AbstractUnivariateStatistic.evaluate`
        
        
        
        """
        ...
    @typing.overload
    def setData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> None: ...

class DescriptiveStatistics(StatisticalSummary, java.util.function.DoubleConsumer, java.io.Serializable):
    """
    public classDescriptiveStatistics extends :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`, :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer`, :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Maintains a dataset of values of a single variable and computes descriptive statistics based on stored data.
    
        The :meth:`~org.hipparchus.stat.descriptive.DescriptiveStatistics.getWindowSize` property sets a limit on the number of
        values that can be stored in the dataset. The default value, INFINITE_WINDOW, puts no limit on the size of the dataset.
        This value should be used with caution, as the backing store will grow without bound in this case.
    
        For very large datasets, :class:`~org.hipparchus.stat.descriptive.StreamingStatistics`, which does not store the
        dataset, should be used instead of this class. If :code:`windowSize` is not INFINITE_WINDOW and more values are added
        than can be stored in the dataset, new values are added in a "rolling" manner, with new values replacing the "oldest"
        values in the dataset.
    
        Note: this class is not threadsafe.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, int: int): ...
    def accept(self, double: float) -> None:
        """
        
            Specified by:
                
                meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer.accept` in
                interface :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer`
        
        
        """
        ...
    def addValue(self, double: float) -> None:
        """
            Adds the value to the dataset. If the dataset is at the maximum size (i.e., the number of stored elements equals the
            currently configured windowSize), the first (oldest) element in the dataset is discarded to make room for the new value.
        
            Parameters:
                v (double): the value to be added
        
        
        """
        ...
    def apply(self, univariateStatistic: UnivariateStatistic) -> float:
        """
            Apply the given statistic to the data associated with this set of statistics.
        
            Parameters:
                stat (:class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`): the statistic to apply
        
            Returns:
                the computed value of the statistic.
        
        
        """
        ...
    def clear(self) -> None:
        """
            Resets all statistics and storage.
        
        """
        ...
    def copy(self) -> 'DescriptiveStatistics':
        """
            Returns a copy of this DescriptiveStatistics instance with the same internal state.
        
            Returns:
                a copy of this
        
        
        """
        ...
    def getElement(self, int: int) -> float:
        """
            Returns the element at the specified index
        
            Parameters:
                index (int): The Index of the element
        
            Returns:
                return the element at the specified index
        
        
        """
        ...
    def getGeometricMean(self) -> float:
        """
            Returns the geometric mean of the available values.
        
            See :class:`~org.hipparchus.stat.descriptive.moment.GeometricMean` for details on the computing algorithm.
        
            Returns:
                The geometricMean, Double.NaN if no values have been added, or if any negative values have been added.
        
            Also see:
        
                  - ` Geometric mean <http://www.xycoon.com/geometric_mean.htm>`
        
        
        
        """
        ...
    def getKurtosis(self) -> float:
        """
            Returns the Kurtosis of the available values. Kurtosis is a measure of the "peakedness" of a distribution.
        
            Returns:
                The kurtosis, Double.NaN if less than 4 values have been added.
        
        
        """
        ...
    def getMax(self) -> float:
        """
            Returns the maximum of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMax` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The max or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMean(self) -> float:
        """
            Returns the ` arithmetic mean <http://www.xycoon.com/arithmetic_mean.htm>` of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMean` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The mean or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Returns the minimum of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMin` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The min or Double.NaN if no values have been added.
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The number of available values
        
        
        """
        ...
    def getPercentile(self, double: float) -> float: ...
    def getPopulationVariance(self) -> float:
        """
            Returns the population variance of the available values.
        
            Returns:
                The population variance, Double.NaN if no values have been added, or 0.0 for a single value set.
        
            Also see:
        
                  - ` Population variance <http://en.wikibooks.org/wiki/Statistics/Summary/Variance>`
        
        
        
        """
        ...
    def getQuadraticMean(self) -> float:
        """
            Returns the quadratic mean of the available values.
        
            Returns:
                The quadratic mean or :code:`Double.NaN` if no values have been added.
        
            Also see:
        
                  - ` Root Mean Square <http://mathworld.wolfram.com/Root-Mean-Square.html>`
        
        
        
        """
        ...
    def getSkewness(self) -> float:
        """
            Returns the skewness of the available values. Skewness is a measure of the asymmetry of a given distribution.
        
            Returns:
                The skewness, Double.NaN if less than 3 values have been added.
        
        
        """
        ...
    def getSortedValues(self) -> typing.MutableSequence[float]:
        """
            Returns the current set of values in an array of double primitives, sorted in ascending order. The returned array is a
            fresh copy of the underlying data -- i.e., it is not a reference to the stored data.
        
            Returns:
                returns the current set of numbers sorted in ascending order
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
            Returns the standard deviation of the available values.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getStandardDeviation` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The standard deviation, Double.NaN if no values have been added or 0.0 for a single value set.
        
        
        """
        ...
    def getSum(self) -> float:
        """
            Returns the sum of the values that have been added to Univariate.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getSum` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The sum or Double.NaN if no values have been added
        
        
        """
        ...
    def getSumOfSquares(self) -> float:
        """
            Returns the sum of the squares of the available values.
        
            Returns:
                The sum of the squares or Double.NaN if no values have been added.
        
        
        """
        ...
    def getValues(self) -> typing.MutableSequence[float]:
        """
            Returns the current set of values in an array of double primitives. The order of addition is preserved. The returned
            array is a fresh copy of the underlying data -- i.e., it is not a reference to the stored data.
        
            Returns:
                the current set of numbers in the order in which they were added to this set
        
        
        """
        ...
    def getVariance(self) -> float:
        """
            Returns the variance of the available values.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getVariance` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The variance, Double.NaN if no values have been added or 0.0 for a single value set.
        
        
        """
        ...
    def getWindowSize(self) -> int:
        """
            Returns the maximum number of values that can be stored in the dataset, or INFINITE_WINDOW (-1) if there is no limit.
        
            Returns:
                The current window size or -1 if its Infinite.
        
        
        """
        ...
    def removeMostRecentValue(self) -> None: ...
    def replaceMostRecentValue(self, double: float) -> float: ...
    def setWindowSize(self, int: int) -> None: ...
    def toString(self) -> str:
        """
            Generates a text report displaying univariate statistics from values that have been added. Each statistic is displayed
            on a separate line.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                String with line feeds displaying statistics
        
        
        """
        ...

class MultivariateSummaryStatistics(StatisticalMultivariateSummary, java.io.Serializable):
    """
    public classMultivariateSummaryStatistics extends :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`, :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Computes summary statistics for a stream of n-tuples added using the
        :meth:`~org.hipparchus.stat.descriptive.MultivariateSummaryStatistics.addValue` method. The data values are not stored
        in memory, so this class can be used to compute statistics for very large n-tuple streams.
    
        To compute statistics for a stream of n-tuples, construct a
        :class:`~org.hipparchus.stat.descriptive.MultivariateSummaryStatistics` instance with dimension n and then use
        :meth:`~org.hipparchus.stat.descriptive.MultivariateSummaryStatistics.addValue` to add n-tuples. The :code:`getXxx`
        methods where Xxx is a statistic return an array of :code:`double` values, where for :code:`i = 0,...,n-1` the i
        :sup:`th` array element is the value of the given statistic for data range consisting of the i :sup:`th` element of each
        of the input n-tuples. For example, if :code:`addValue` is called with actual parameters {0, 1, 2}, then {3, 4, 5} and
        finally {6, 7, 8}, :code:`getSum` will return a three-element array with values {0+3+6, 1+4+7, 2+5+8}
    
        Note: This class is not thread-safe.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, boolean: bool): ...
    def addValue(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def clear(self) -> None:
        """
            Resets all statistics and storage.
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns true iff :code:`object` is a :code:`MultivariateSummaryStatistics` instance and all statistics have the same
            values as this.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                object (:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): the object to test equality against.
        
            Returns:
                true if object equals this
        
        
        """
        ...
    def getCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns the covariance of the available values.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getCovariance` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                The covariance, null if no multivariate sample have been added or a zeroed matrix for a single value set.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the dimension of the data
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getDimension` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                The dimension of the data
        
        
        """
        ...
    def getGeometricMean(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the geometric mean of the i :sup:`th` entries of the arrays that correspond
            to each multivariate sample
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getGeometricMean` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component geometric means
        
        
        """
        ...
    def getMax(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the maximum of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getMax` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component maxima
        
        
        """
        ...
    def getMean(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the mean of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getMean` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component means
        
        
        """
        ...
    def getMin(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the minimum of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getMin` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component minima
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                The number of available values
        
        
        """
        ...
    def getStandardDeviation(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the standard deviation of the i :sup:`th` entries of the arrays that have
            been added using :meth:`~org.hipparchus.stat.descriptive.MultivariateSummaryStatistics.addValue`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getStandardDeviation` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component standard deviations
        
        
        """
        ...
    def getSum(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the sum of the i :sup:`th` entries of the arrays that correspond to each
            multivariate sample
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getSum` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component sums
        
        
        """
        ...
    def getSumLog(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the sum of logs of the i :sup:`th` entries of the arrays that correspond to
            each multivariate sample
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getSumLog` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component log sums
        
        
        """
        ...
    def getSumSq(self) -> typing.MutableSequence[float]:
        """
            Returns an array whose i :sup:`th` entry is the sum of squares of the i :sup:`th` entries of the arrays that correspond
            to each multivariate sample
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary.getSumSq` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalMultivariateSummary`
        
            Returns:
                the array of component sums of squares
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Returns hash code based on values of statistics
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                hash code
        
        
        """
        ...
    def toString(self) -> str:
        """
            Generates a text report displaying summary statistics from values that have been added.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                String with line feeds displaying statistics
        
        
        """
        ...

class StatisticalSummaryValues(java.io.Serializable, StatisticalSummary):
    """
    public classStatisticalSummaryValues extends :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`, :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
    
        Value object representing the results of a univariate statistical summary.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, long: int, double3: float, double4: float, double5: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns true iff :code:`object` is a :code:`StatisticalSummary` instance and all statistics have the same values as
            this.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                object (:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): the object to test equality against.
        
            Returns:
                true if object equals this
        
        
        """
        ...
    def getMax(self) -> float:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMax`
            Returns the maximum of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMax` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                Returns the max.
        
        
        """
        ...
    def getMean(self) -> float:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMean`
            Returns the ` arithmetic mean <http://www.xycoon.com/arithmetic_mean.htm>` of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMean` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                Returns the mean.
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMin`
            Returns the minimum of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMin` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                Returns the min.
        
        
        """
        ...
    def getN(self) -> int:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getN`
            Returns the number of available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                Returns the number of values.
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getStandardDeviation`
            Returns the standard deviation of the available values.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getStandardDeviation` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                Returns the standard deviation
        
        
        """
        ...
    def getSum(self) -> float:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getSum`
            Returns the sum of the values that have been added to Univariate.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getSum` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                Returns the sum.
        
        
        """
        ...
    def getVariance(self) -> float:
        """
            Description copied from interface: :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getVariance`
            Returns the variance of the available values.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getVariance` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                Returns the variance.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Returns hash code based on values of statistics
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                hash code
        
        
        """
        ...
    def toString(self) -> str:
        """
            Generates a text report displaying values of statistics. Each statistic is displayed on a separate line.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                String with line feeds displaying statistics
        
        
        """
        ...

class StorelessUnivariateStatistic(UnivariateStatistic, java.util.function.DoubleConsumer):
    """
    public interfaceStorelessUnivariateStatisticextends :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`, :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer`
    
        Extends the definition of :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic` with
        :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment` and
        :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.incrementAll` methods for adding values and
        updating internal state.
    
        This interface is designed to be used for calculating statistics that can be computed in one pass through the data
        without storing the full array of sample values.
    
        Note: unless otherwise stated, the :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.evaluate` and
        :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.evaluate` methods do **NOT** alter the internal
        state of the respective statistic.
    """
    def accept(self, double: float) -> None:
        """
        
            Specified by:
                
                meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer.accept` in
                interface :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer`
        
        
        """
        ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
        """
        ...
    def copy(self) -> 'StorelessUnivariateStatistic':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...
    @typing.overload
    def incrementAll(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    def incrementAll(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> None: ...

class StreamingStatistics(StatisticalSummary, AggregatableStatistic['StreamingStatistics'], java.util.function.DoubleConsumer, java.io.Serializable):
    """
    public classStreamingStatistics extends :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`, :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.StreamingStatistics`>, :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer`, :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Computes summary statistics for a stream of data values added using the
        :meth:`~org.hipparchus.stat.descriptive.StreamingStatistics.addValue` method. The data values are not stored in memory,
        so this class can be used to compute statistics for very large data streams.
    
        By default, all statistics other than percentiles are maintained. Percentile calculations use an embedded
        :class:`~org.hipparchus.stat.descriptive.rank.RandomPercentile` which carries more memory and compute overhead than the
        other statistics, so it is disabled by default. To enable percentiles, either pass :code:`true` to the constructor or
        use a :class:`~org.hipparchus.stat.descriptive.StreamingStatistics.StreamingStatisticsBuilder` to configure an instance
        with percentiles turned on. Other stats can also be selectively disabled using :code:`StreamingStatisticsBulder`.
    
        Note: This class is not thread-safe.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    def accept(self, double: float) -> None:
        """
        
            Specified by:
                
                meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer.accept` in
                interface :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer`
        
        
        """
        ...
    def addValue(self, double: float) -> None:
        """
            Add a value to the data
        
            Parameters:
                value (double): the value to add
        
        
        """
        ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
            Aggregates the provided instance into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
            Statistics are aggregated only when both this and other are maintaining them. For example, if this.computeMoments is
            false, but other.computeMoments is true, the moment data in other will be lost.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AggregatableStatistic.aggregate` in
                interface :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`
        
            Parameters:
                other (:class:`~org.hipparchus.stat.descriptive.StreamingStatistics`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, streamingStatistics: 'StreamingStatistics') -> None: ...
    @staticmethod
    def builder() -> 'StreamingStatistics.StreamingStatisticsBuilder':
        """
            Returns a :class:`~org.hipparchus.stat.descriptive.StreamingStatistics.StreamingStatisticsBuilder` to source configured
            :code:`StreamingStatistics` instances.
        
            Returns:
                a StreamingStatisticsBuilder instance
        
        
        """
        ...
    def clear(self) -> None:
        """
            Resets all statistics and storage.
        
        """
        ...
    def copy(self) -> 'StreamingStatistics':
        """
            Returns a copy of this StreamingStatistics instance with the same internal state.
        
            Returns:
                a copy of this
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns true iff :code:`object` is a :code:`StreamingStatistics` instance and all statistics have the same values as
            this.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                object (:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): the object to test equality against.
        
            Returns:
                true if object equals this
        
        
        """
        ...
    def getGeometricMean(self) -> float:
        """
            Returns the geometric mean of the values that have been added.
        
            Double.NaN is returned if no values have been added.
        
            Returns:
                the geometric mean
        
        
        """
        ...
    def getMax(self) -> float:
        """
            Returns the maximum of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMax` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The max or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMean(self) -> float:
        """
            Returns the ` arithmetic mean <http://www.xycoon.com/arithmetic_mean.htm>` of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMean` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The mean or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMedian(self) -> float:
        """
            Returns an estimate of the median of the values that have been entered. See
            :class:`~org.hipparchus.stat.descriptive.rank.RandomPercentile` for a description of the algorithm used for large data
            streams.
        
            Returns:
                the median
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Returns the minimum of the available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getMin` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The min or Double.NaN if no values have been added.
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of available values
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The number of available values
        
        
        """
        ...
    def getPercentile(self, double: float) -> float:
        """
            Returns an estimate of the given percentile of the values that have been entered. See
            :class:`~org.hipparchus.stat.descriptive.rank.RandomPercentile` for a description of the algorithm used for large data
            streams.
        
            Parameters:
                percentile (double): the desired percentile (must be between 0 and 100)
        
            Returns:
                estimated percentile
        
        
        """
        ...
    def getPopulationVariance(self) -> float:
        """
            Returns the ` population variance <http://en.wikibooks.org/wiki/Statistics/Summary/Variance>` of the values that have
            been added.
        
            Double.NaN is returned if no values have been added.
        
            Returns:
                the population variance
        
        
        """
        ...
    def getQuadraticMean(self) -> float:
        """
            Returns the quadratic mean, a.k.a. ` root-mean-square <http://mathworld.wolfram.com/Root-Mean-Square.html>` of the
            available values
        
            Returns:
                The quadratic mean or :code:`Double.NaN` if no values have been added.
        
        
        """
        ...
    def getSecondMoment(self) -> float:
        """
            Returns a statistic related to the Second Central Moment. Specifically, what is returned is the sum of squared
            deviations from the sample mean among the values that have been added.
        
            Returns :code:`Double.NaN` if no data values have been added and returns :code:`0` if there is just one value in the
            data set.
        
            Returns:
                second central moment statistic
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
            Returns the standard deviation of the values that have been added.
        
            Double.NaN is returned if no values have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getStandardDeviation` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                the standard deviation
        
        
        """
        ...
    def getSum(self) -> float:
        """
            Returns the sum of the values that have been added to Univariate.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getSum` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The sum or Double.NaN if no values have been added
        
        
        """
        ...
    def getSumOfLogs(self) -> float:
        """
            Returns the sum of the logs of the values that have been added.
        
            Double.NaN is returned if no values have been added.
        
            Returns:
                the sum of logs
        
        
        """
        ...
    def getSumOfSquares(self) -> float:
        """
            Returns the sum of the squares of the values that have been added.
        
            Double.NaN is returned if no values have been added.
        
            Returns:
                The sum of squares
        
        
        """
        ...
    def getSummary(self) -> StatisticalSummary:
        """
            Return a :class:`~org.hipparchus.stat.descriptive.StatisticalSummaryValues` instance reporting current statistics.
        
            Returns:
                Current values of statistics
        
        
        """
        ...
    def getVariance(self) -> float:
        """
            Returns the variance of the available values.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StatisticalSummary.getVariance` in
                interface :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        
            Returns:
                The variance, Double.NaN if no values have been added or 0.0 for a single value set.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Returns hash code based on values of statistics.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                hash code
        
        
        """
        ...
    def toString(self) -> str:
        """
            Generates a text report displaying summary statistics from values that have been added.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                String with line feeds displaying statistics
        
        
        """
        ...
    class StreamingStatisticsBuilder:
        def __init__(self): ...
        def build(self) -> 'StreamingStatistics': ...
        def extrema(self, boolean: bool) -> 'StreamingStatistics.StreamingStatisticsBuilder': ...
        def moments(self, boolean: bool) -> 'StreamingStatistics.StreamingStatisticsBuilder': ...
        def percentiles(self, double: float, randomGenerator: org.hipparchus.random.RandomGenerator) -> 'StreamingStatistics.StreamingStatisticsBuilder': ...
        def sumOfLogs(self, boolean: bool) -> 'StreamingStatistics.StreamingStatisticsBuilder': ...
        def sumOfSquares(self, boolean: bool) -> 'StreamingStatistics.StreamingStatisticsBuilder': ...

class AbstractStorelessUnivariateStatistic(StorelessUnivariateStatistic):
    """
    public abstract classAbstractStorelessUnivariateStatistic extends :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
    
        Abstract base class for implementations of the :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        interface.
    
        Provides default :code:`hashCode()` and :code:`equals(Object)` implementations.
    """
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> StorelessUnivariateStatistic:
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy` in
                interface :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns true iff :code:`object` is the same type of
            :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic` (the object's class equals this instance)
            returning the same values as this for :code:`getResult()` and :code:`getN()`.
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                object (:class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): object to test equality against.
        
            Returns:
                true if object returns the same value as this
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Returns hash code based on getResult() and getN().
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                hash code
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive")``.

    AbstractStorelessUnivariateStatistic: typing.Type[AbstractStorelessUnivariateStatistic]
    AbstractUnivariateStatistic: typing.Type[AbstractUnivariateStatistic]
    AggregatableStatistic: typing.Type[AggregatableStatistic]
    DescriptiveStatistics: typing.Type[DescriptiveStatistics]
    MultivariateSummaryStatistics: typing.Type[MultivariateSummaryStatistics]
    StatisticalMultivariateSummary: typing.Type[StatisticalMultivariateSummary]
    StatisticalSummary: typing.Type[StatisticalSummary]
    StatisticalSummaryValues: typing.Type[StatisticalSummaryValues]
    StorelessMultivariateStatistic: typing.Type[StorelessMultivariateStatistic]
    StorelessUnivariateStatistic: typing.Type[StorelessUnivariateStatistic]
    StreamingStatistics: typing.Type[StreamingStatistics]
    UnivariateStatistic: typing.Type[UnivariateStatistic]
    WeightedEvaluation: typing.Type[WeightedEvaluation]
    moment: org.hipparchus.stat.descriptive.moment.__module_protocol__
    rank: org.hipparchus.stat.descriptive.rank.__module_protocol__
    summary: org.hipparchus.stat.descriptive.summary.__module_protocol__
    vector: org.hipparchus.stat.descriptive.vector.__module_protocol__
