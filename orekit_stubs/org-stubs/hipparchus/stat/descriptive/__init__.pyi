
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
    An interface for statistics that can aggregate results.
    """
    @typing.overload
    def aggregate(self, others: _AggregatableStatistic__T) -> None:
        """
        Aggregates the results from the provided instances into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Parameters:
            others (AggregatableStatistic...): the other instances to aggregate into this instance
        
        Raises:
            hipparchus: if either others or any instance is null
        
        default void aggregate (Iterable<AggregatableStatistic> others)
        
        Aggregates the results from the provided instances into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Parameters:
            others (Iterable<AggregatableStatistic> others): the other instances to aggregate into this instance
        
        Raises:
            hipparchus: if either others or any instance is null
        
        
        """
        ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[_AggregatableStatistic__T], typing.Sequence[_AggregatableStatistic__T], typing.Set[_AggregatableStatistic__T], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None: ...
    @typing.overload
    def aggregate(self, *t: _AggregatableStatistic__T) -> None: ...

class StatisticalMultivariateSummary:
    """
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
        Returns an array whose i :sup:`th` entry is the geometric mean of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Returns:
            the array of component geometric means
        
        
        """
        ...
    def getMax(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the maximum of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Returns:
            the array of component maxima
        
        
        """
        ...
    def getMean(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the mean of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Returns:
            the array of component means
        
        
        """
        ...
    def getMin(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the minimum of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
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
        Returns an array whose i :sup:`th` entry is the standard deviation of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Returns:
            the array of component standard deviations
        
        
        """
        ...
    def getSum(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the sum of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Returns:
            the array of component sums
        
        
        """
        ...
    def getSumLog(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the sum of logs of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Returns:
            the array of component log sums
        
        
        """
        ...
    def getSumSq(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the sum of squares of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Returns:
            the array of component sums of squares
        
        
        """
        ...

class StatisticalSummary:
    """
    Reporting interface for basic univariate statistics.
    """
    @typing.overload
    @staticmethod
    def aggregate(statistics: typing.Union[java.lang.Iterable['StatisticalSummary'], typing.Sequence['StatisticalSummary'], typing.Set['StatisticalSummary'], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> 'StatisticalSummary':
        """
        Computes aggregated statistical summaries.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the returned StatisticalSummary should contain the same values that would have been obtained by computing a single StatisticalSummary over the combined dataset.
        
        Parameters:
            statistics (StatisticalSummary...): StatisticalSummary instances to aggregate
        
        Returns:
            summary statistics for the combined dataset
        
        Raises:
            hipparchus: if the input is null
        
        static StatisticalSummary aggregate (Iterable<? extends StatisticalSummary> statistics)
        
        Computes aggregated statistical summaries.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the returned StatisticalSummary should contain the same values that would have been obtained by computing a single StatisticalSummary over the combined dataset.
        
        Parameters:
            statistics (Iterable<? extends StatisticalSummary> statistics): iterable of StatisticalSummary instances to aggregate
        
        Returns:
            summary statistics for the combined dataset
        
        Raises:
            hipparchus: if the input is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def aggregate(*statistics: 'StatisticalSummary') -> 'StatisticalSummary': ...
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
            value of the statistic, NaN if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, d: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Updates the internal state of the statistic to reflect the addition of the new value.
        
        Parameters:
            d (double[]): the new value
        
        
        """
        ...

class UnivariateStatistic(org.hipparchus.util.MathArrays.Function):
    """
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
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray]) -> float: ...

class WeightedEvaluation:
    """
    Weighted evaluation for statistics.
    """
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], weights: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], weights: typing.Union[typing.List[float], jpype.JArray]) -> float: ...

class AbstractUnivariateStatistic(UnivariateStatistic):
    """
    Abstract base class for implementations of the UnivariateStatistic interface.
    """
    def copy(self) -> UnivariateStatistic:
        """
        Returns a copy of the statistic with the same internal state.
        
        Specified by: copy in interface UnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
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
    def setData(self, values: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the data array.
        
        The stored value is a copy of the parameter array, not the array itself.
        
        Parameters:
            values (double[]): data array to store (may be null to remove stored data)
        
        Also see:
            evaluate
        
        public void setData (double[] values, int begin, int length) throws hipparchus
        
        Set the data array. The input array is copied, not referenced.
        
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

class DescriptiveStatistics(StatisticalSummary, java.util.function.DoubleConsumer, java.io.Serializable):
    """
    Maintains a dataset of values of a single variable and computes descriptive statistics based on stored data.
    
    The getWindowSize property sets a limit on the number of values that can be stored in the dataset. The default value, INFINITE_WINDOW, puts no limit on the size of the dataset. This value should be used with caution, as the backing store will grow without bound in this case.
    
    For very large datasets, StreamingStatistics, which does not store the dataset, should be used instead of this class. If windowSize is not INFINITE_WINDOW and more values are added than can be stored in the dataset, new values are added in a "rolling" manner, with new values replacing the "oldest" values in the dataset.
    
    Note: this class is not threadsafe.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, int: int): ...
    def accept(self, v: float) -> None:
        """
        Specified by: meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer.html?is` in interface DoubleConsumer
        
        
        """
        ...
    def addValue(self, v: float) -> None:
        """
        Adds the value to the dataset. If the dataset is at the maximum size (i.e., the number of stored elements equals the currently configured windowSize), the first (oldest) element in the dataset is discarded to make room for the new value.
        
        Parameters:
            v (double): the value to be added
        
        
        """
        ...
    def apply(self, stat: UnivariateStatistic) -> float:
        """
        Apply the given statistic to the data associated with this set of statistics.
        
        Parameters:
            stat (UnivariateStatistic): the statistic to apply
        
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
    def getElement(self, index: int) -> float:
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
        
        See GeometricMean for details on the computing algorithm.
        
        Returns:
            The geometricMean, Double.NaN if no values have been added, or if any negative values have been added.
        
        Also see:
            ` Geometric mean <http://www.xycoon.com/geometric_mean.htm>`
        
        
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
        
        Specified by: getMax in interface StatisticalSummary
        
        Returns:
            The max or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMean(self) -> float:
        """
        Returns the ` arithmetic mean <http://www.xycoon.com/arithmetic_mean.htm>` of the available values
        
        Specified by: getMean in interface StatisticalSummary
        
        Returns:
            The mean or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMin(self) -> float:
        """
        Returns the minimum of the available values
        
        Specified by: getMin in interface StatisticalSummary
        
        Returns:
            The min or Double.NaN if no values have been added.
        
        
        """
        ...
    def getN(self) -> int:
        """
        Returns the number of available values
        
        Specified by: getN in interface StatisticalSummary
        
        Returns:
            The number of available values
        
        
        """
        ...
    def getPercentile(self, p: float) -> float:
        """
        Returns an estimate for the pth percentile of the stored values.
        
        The implementation provided here follows the first estimation procedure presented `here. <http://www.itl.nist.gov/div898/handbook/prc/section2/prc252.htm>`
        
        Preconditions:
        
          - 0 < p ≤ 100 (otherwise an MathIllegalArgumentException is thrown)
          - at least one value must be stored (returns NaN otherwise)
        
        
        Parameters:
            p (double): the requested percentile (scaled from 0 - 100)
        
        Returns:
            An estimate for the pth percentile of the stored data
        
        Raises:
            hipparchus: if p is not a valid quantile
        
        
        """
        ...
    def getPopulationVariance(self) -> float:
        """
        Returns the population variance of the available values.
        
        Returns:
            The population variance, Double.NaN if no values have been added, or 0.0 for a single value set.
        
        Also see:
            ` Population variance <http://en.wikibooks.org/wiki/Statistics/Summary/Variance>`
        
        
        """
        ...
    def getQuadraticMean(self) -> float:
        """
        Returns the quadratic mean of the available values.
        
        Returns:
            The quadratic mean or NaN if no values have been added.
        
        Also see:
            ` Root Mean Square <http://mathworld.wolfram.com/Root-Mean-Square.html>`
        
        
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
        Returns the current set of values in an array of double primitives, sorted in ascending order. The returned array is a fresh copy of the underlying data -- i.e., it is not a reference to the stored data.
        
        Returns:
            returns the current set of numbers sorted in ascending order
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
        Returns the standard deviation of the available values.
        
        Specified by: getStandardDeviation in interface StatisticalSummary
        
        Returns:
            The standard deviation, Double.NaN if no values have been added or 0.0 for a single value set.
        
        
        """
        ...
    def getSum(self) -> float:
        """
        Returns the sum of the values that have been added to Univariate.
        
        Specified by: getSum in interface StatisticalSummary
        
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
        Returns the current set of values in an array of double primitives. The order of addition is preserved. The returned array is a fresh copy of the underlying data -- i.e., it is not a reference to the stored data.
        
        Returns:
            the current set of numbers in the order in which they were added to this set
        
        
        """
        ...
    def getVariance(self) -> float:
        """
        Returns the variance of the available values.
        
        Specified by: getVariance in interface StatisticalSummary
        
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
    def removeMostRecentValue(self) -> None:
        """
        Removes the most recent value from the dataset.
        
        Raises:
            hipparchus: if there are no elements stored
        
        
        """
        ...
    def replaceMostRecentValue(self, v: float) -> float:
        """
        Replaces the most recently stored value with the given value. There must be at least one element stored to call this method.
        
        Parameters:
            v (double): the value to replace the most recent stored value
        
        Returns:
            replaced value
        
        Raises:
            hipparchus: if there are no elements stored
        
        
        """
        ...
    def setWindowSize(self, windowSize: int) -> None:
        """
        WindowSize controls the number of values that contribute to the reported statistics. For example, if windowSize is set to 3 and the values {1,2,3,4,5} have been added in that order then the available values are {3,4,5} and all reported statistics will be based on these values. If windowSize is decreased as a result of this call and there are more than the new value of elements in the current dataset, values from the front of the array are discarded to reduce the dataset to windowSize elements.
        
        Parameters:
            windowSize (int): sets the size of the window.
        
        Raises:
            hipparchus: if window size is less than 1 but not equal to
                INFINITE_WINDOW
        
        
        """
        ...
    def toString(self) -> str:
        """
        Generates a text report displaying univariate statistics from values that have been added. Each statistic is displayed on a separate line.
        
        Overrides: Object in class Object
        
        Returns:
            String with line feeds displaying statistics
        
        
        """
        ...

class MultivariateSummaryStatistics(StatisticalMultivariateSummary, java.io.Serializable):
    """
    Computes summary statistics for a stream of n-tuples added using the addValue method. The data values are not stored in memory, so this class can be used to compute statistics for very large n-tuple streams.
    
    To compute statistics for a stream of n-tuples, construct a MultivariateSummaryStatistics instance with dimension n and then use addValue to add n-tuples. The getXxx methods where Xxx is a statistic return an array of double values, where for ,n-1 the i :sup:`th` array element is the value of the given statistic for data range consisting of the i :sup:`th` element of each of the input n-tuples. For example, if addValue is called with actual parameters {0, 1, 2}, then {3, 4, 5} and finally {6, 7, 8}, getSum will return a three-element array with values {0+3+6, 1+4+7, 2+5+8}
    
    Note: This class is not thread-safe.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, dimension: int): ...
    @typing.overload
    def __init__(self, dimension: int, covarianceBiasCorrection: bool): ...
    def addValue(self, value: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add an n-tuple to the data
        
        Parameters:
            value (double[]): the n-tuple to add
        
        Raises:
            hipparchus: if the array is null or the length of the array does not match the one used at construction
        
        
        """
        ...
    def clear(self) -> None:
        """
        Resets all statistics and storage.
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true iff object is a MultivariateSummaryStatistics instance and all statistics have the same values as this.
        
        Overrides: Object in class Object
        
        Parameters:
            object (Object): the object to test equality against.
        
        Returns:
            true if object equals this
        
        
        """
        ...
    def getCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
        Returns the covariance of the available values.
        
        Specified by: getCovariance in interface StatisticalMultivariateSummary
        
        Returns:
            The covariance, null if no multivariate sample have been added or a zeroed matrix for a single value set.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Returns the dimension of the data
        
        Specified by: getDimension in interface StatisticalMultivariateSummary
        
        Returns:
            The dimension of the data
        
        
        """
        ...
    def getGeometricMean(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the geometric mean of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Specified by: getGeometricMean in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component geometric means
        
        
        """
        ...
    def getMax(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the maximum of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Specified by: getMax in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component maxima
        
        
        """
        ...
    def getMean(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the mean of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Specified by: getMean in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component means
        
        
        """
        ...
    def getMin(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the minimum of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Specified by: getMin in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component minima
        
        
        """
        ...
    def getN(self) -> int:
        """
        Returns the number of available values
        
        Specified by: getN in interface StatisticalMultivariateSummary
        
        Returns:
            The number of available values
        
        
        """
        ...
    def getStandardDeviation(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the standard deviation of the i :sup:`th` entries of the arrays that have been added using addValue
        
        Specified by: getStandardDeviation in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component standard deviations
        
        
        """
        ...
    def getSum(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the sum of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Specified by: getSum in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component sums
        
        
        """
        ...
    def getSumLog(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the sum of logs of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Specified by: getSumLog in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component log sums
        
        
        """
        ...
    def getSumSq(self) -> typing.MutableSequence[float]:
        """
        Returns an array whose i :sup:`th` entry is the sum of squares of the i :sup:`th` entries of the arrays that correspond to each multivariate sample
        
        Specified by: getSumSq in interface StatisticalMultivariateSummary
        
        Returns:
            the array of component sums of squares
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Returns hash code based on values of statistics
        
        Overrides: Object in class Object
        
        Returns:
            hash code
        
        
        """
        ...
    def toString(self) -> str:
        """
        Generates a text report displaying summary statistics from values that have been added.
        
        Overrides: Object in class Object
        
        Returns:
            String with line feeds displaying statistics
        
        
        """
        ...

class StatisticalSummaryValues(java.io.Serializable, StatisticalSummary):
    """
    Value object representing the results of a univariate statistical summary.
    
    Also see:
        serialized
    """
    def __init__(self, mean: float, variance: float, n: int, max: float, min: float, sum: float):
        """
        Constructor.
        
        Parameters:
            mean (double): the sample mean
            variance (double): the sample variance
            n (long): the number of observations in the sample
            max (double): the maximum value
            min (double): the minimum value
            sum (double): the sum of the values
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true iff object is a StatisticalSummary instance and all statistics have the same values as this.
        
        Overrides: Object in class Object
        
        Parameters:
            object (Object): the object to test equality against.
        
        Returns:
            true if object equals this
        
        
        """
        ...
    def getMax(self) -> float:
        """
        Description copied from interface: getMax Returns the maximum of the available values
        
        Specified by: getMax in interface StatisticalSummary
        
        Returns:
            Returns the max.
        
        
        """
        ...
    def getMean(self) -> float:
        """
        Description copied from interface: getMean Returns the ` arithmetic mean <http://www.xycoon.com/arithmetic_mean.htm>` of the available values
        
        Specified by: getMean in interface StatisticalSummary
        
        Returns:
            Returns the mean.
        
        
        """
        ...
    def getMin(self) -> float:
        """
        Description copied from interface: getMin Returns the minimum of the available values
        
        Specified by: getMin in interface StatisticalSummary
        
        Returns:
            Returns the min.
        
        
        """
        ...
    def getN(self) -> int:
        """
        Description copied from interface: getN Returns the number of available values
        
        Specified by: getN in interface StatisticalSummary
        
        Returns:
            Returns the number of values.
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
        Description copied from interface: getStandardDeviation Returns the standard deviation of the available values.
        
        Specified by: getStandardDeviation in interface StatisticalSummary
        
        Returns:
            Returns the standard deviation
        
        
        """
        ...
    def getSum(self) -> float:
        """
        Description copied from interface: getSum Returns the sum of the values that have been added to Univariate.
        
        Specified by: getSum in interface StatisticalSummary
        
        Returns:
            Returns the sum.
        
        
        """
        ...
    def getVariance(self) -> float:
        """
        Description copied from interface: getVariance Returns the variance of the available values.
        
        Specified by: getVariance in interface StatisticalSummary
        
        Returns:
            Returns the variance.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Returns hash code based on values of statistics
        
        Overrides: Object in class Object
        
        Returns:
            hash code
        
        
        """
        ...
    def toString(self) -> str:
        """
        Generates a text report displaying values of statistics. Each statistic is displayed on a separate line.
        
        Overrides: Object in class Object
        
        Returns:
            String with line feeds displaying statistics
        
        
        """
        ...

class StorelessUnivariateStatistic(UnivariateStatistic, java.util.function.DoubleConsumer):
    """
    Extends the definition of UnivariateStatistic with increment and incrementAll methods for adding values and updating internal state.
    
    This interface is designed to be used for calculating statistics that can be computed in one pass through the data without storing the full array of sample values.
    
    Note: unless otherwise stated, the evaluate and evaluate methods do NOT alter the internal state of the respective statistic.
    """
    def accept(self, value: float) -> None:
        """
        Specified by: meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer.html?is` in interface DoubleConsumer
        
        
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
        
        Specified by: copy in interface UnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
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
            value of the statistic, NaN if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, d: float) -> None:
        """
        Updates the internal state of the statistic to reflect the addition of the new value.
        
        Parameters:
            d (double): the new value.
        
        
        """
        ...
    @typing.overload
    def incrementAll(self, values: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    def incrementAll(self, values: typing.Union[typing.List[float], jpype.JArray], start: int, length: int) -> None: ...

class StreamingStatistics(StatisticalSummary, AggregatableStatistic['StreamingStatistics'], java.util.function.DoubleConsumer, java.io.Serializable):
    """
    Computes summary statistics for a stream of data values added using the addValue method. The data values are not stored in memory, so this class can be used to compute statistics for very large data streams.
    
    By default, all statistics other than percentiles are maintained. Percentile calculations use an embedded RandomPercentile which carries more memory and compute overhead than the other statistics, so it is disabled by default. To enable percentiles, either pass true to the constructor or use a StreamingStatisticsBuilder to configure an instance with percentiles turned on. Other stats can also be selectively disabled using StreamingStatisticsBulder.
    
    Note: This class is not thread-safe.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, epsilon: float, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    def accept(self, value: float) -> None:
        """
        Specified by: meth:`~org.hipparchus.stat.descriptive.https:.docs.oracle.com.javase.8.docs.api.java.util.function.DoubleConsumer.html?is` in interface DoubleConsumer
        
        
        """
        ...
    def addValue(self, value: float) -> None:
        """
        Add a value to the data
        
        Parameters:
            value (double): the value to add
        
        
        """
        ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Aggregates the provided instance into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset. Statistics are aggregated only when both this and other are maintaining them. For example, if this.computeMoments is false, but other.computeMoments is true, the moment data in other will be lost.
        
        Specified by: aggregate in interface AggregatableStatistic
        
        Parameters:
            other (StreamingStatistics): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'StreamingStatistics') -> None: ...
    @staticmethod
    def builder() -> 'StreamingStatistics.StreamingStatisticsBuilder':
        """
        Returns a StreamingStatisticsBuilder to source configured StreamingStatistics instances.
        
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
        Returns true iff object is a StreamingStatistics instance and all statistics have the same values as this.
        
        Overrides: Object in class Object
        
        Parameters:
            object (Object): the object to test equality against.
        
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
        
        Specified by: getMax in interface StatisticalSummary
        
        Returns:
            The max or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMean(self) -> float:
        """
        Returns the ` arithmetic mean <http://www.xycoon.com/arithmetic_mean.htm>` of the available values
        
        Specified by: getMean in interface StatisticalSummary
        
        Returns:
            The mean or Double.NaN if no values have been added.
        
        
        """
        ...
    def getMedian(self) -> float:
        """
        Returns an estimate of the median of the values that have been entered. See RandomPercentile for a description of the algorithm used for large data streams.
        
        Returns:
            the median
        
        
        """
        ...
    def getMin(self) -> float:
        """
        Returns the minimum of the available values
        
        Specified by: getMin in interface StatisticalSummary
        
        Returns:
            The min or Double.NaN if no values have been added.
        
        
        """
        ...
    def getN(self) -> int:
        """
        Returns the number of available values
        
        Specified by: getN in interface StatisticalSummary
        
        Returns:
            The number of available values
        
        
        """
        ...
    def getPercentile(self, percentile: float) -> float:
        """
        Returns an estimate of the given percentile of the values that have been entered. See RandomPercentile for a description of the algorithm used for large data streams.
        
        Parameters:
            percentile (double): the desired percentile (must be between 0 and 100)
        
        Returns:
            estimated percentile
        
        
        """
        ...
    def getPopulationVariance(self) -> float:
        """
        Returns the ` population variance <http://en.wikibooks.org/wiki/Statistics/Summary/Variance>` of the values that have been added.
        
        Double.NaN is returned if no values have been added.
        
        Returns:
            the population variance
        
        
        """
        ...
    def getQuadraticMean(self) -> float:
        """
        Returns the quadratic mean, a.k.a. ` root-mean-square <http://mathworld.wolfram.com/Root-Mean-Square.html>` of the available values
        
        Returns:
            The quadratic mean or NaN if no values have been added.
        
        
        """
        ...
    def getSecondMoment(self) -> float:
        """
        Returns a statistic related to the Second Central Moment. Specifically, what is returned is the sum of squared deviations from the sample mean among the values that have been added.
        
        Returns NaN if no data values have been added and returns  if there is just one value in the data set.
        
        Returns:
            second central moment statistic
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
        Returns the standard deviation of the values that have been added.
        
        Double.NaN is returned if no values have been added.
        
        Specified by: getStandardDeviation in interface StatisticalSummary
        
        Returns:
            the standard deviation
        
        
        """
        ...
    def getSum(self) -> float:
        """
        Returns the sum of the values that have been added to Univariate.
        
        Specified by: getSum in interface StatisticalSummary
        
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
        Return a StatisticalSummaryValues instance reporting current statistics.
        
        Returns:
            Current values of statistics
        
        
        """
        ...
    def getVariance(self) -> float:
        """
        Returns the variance of the available values.
        
        Specified by: getVariance in interface StatisticalSummary
        
        Returns:
            The variance, Double.NaN if no values have been added or 0.0 for a single value set.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Returns hash code based on values of statistics.
        
        Overrides: Object in class Object
        
        Returns:
            hash code
        
        
        """
        ...
    def toString(self) -> str:
        """
        Generates a text report displaying summary statistics from values that have been added.
        
        Overrides: Object in class Object
        
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
    Abstract base class for implementations of the StorelessUnivariateStatistic interface.
    
    Provides default hashCode() and equals(Object) implementations.
    """
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> StorelessUnivariateStatistic:
        """
        Returns a copy of the statistic with the same internal state.
        
        Specified by: copy in interface StorelessUnivariateStatistic
        
        Specified by: copy in interface UnivariateStatistic
        
        Returns:
            a copy of the statistic
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true iff object is the same type of StorelessUnivariateStatistic (the object's class equals this instance) returning the same values as this for getResult() and getN().
        
        Overrides: Object in class Object
        
        Parameters:
            object (Object): object to test equality against.
        
        Returns:
            true if object returns the same value as this
        
        
        """
        ...
    def getResult(self) -> float:
        """
        Returns the current value of the Statistic.
        
        Specified by: getResult in interface StorelessUnivariateStatistic
        
        Returns:
            value of the statistic, NaN if it has been cleared or just instantiated.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Returns hash code based on getResult() and getN().
        
        Overrides: Object in class Object
        
        Returns:
            hash code
        
        
        """
        ...
    def increment(self, d: float) -> None:
        """
        Updates the internal state of the statistic to reflect the addition of the new value.
        
        Specified by: increment in interface StorelessUnivariateStatistic
        
        Parameters:
            d (double): the new value.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
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
