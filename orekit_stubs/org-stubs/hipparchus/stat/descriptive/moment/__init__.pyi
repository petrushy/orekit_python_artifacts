import java.io
import java.lang
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.descriptive.summary
import typing



class GeometricMean(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['GeometricMean'], java.io.Serializable):
    """
    public class GeometricMean extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic` implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.moment.GeometricMean`>, Serializable
    
        Returns the ` geometric mean <http://www.xycoon.com/geometric_mean.htm>` of the available values.
    
        Uses a :class:`~org.hipparchus.stat.descriptive.summary.SumOfLogs` instance to compute sum of logs and returns
        :code:`exp( 1/n (sum of logs) ).` Therefore,
    
          - If any of values are < 0, the result is :code:`NaN.`
          - If all values are non-negative and less than :code:`Double.POSITIVE_INFINITY`, but at least one value is 0, the result
            is :code:`0.`
          - If both :code:`Double.POSITIVE_INFINITY` and :code:`Double.NEGATIVE_INFINITY` are among the values, the result is
            :code:`NaN.`
    
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, geometricMean: 'GeometricMean'): ...
    @typing.overload
    def __init__(self, sumOfLogs: org.hipparchus.stat.descriptive.summary.SumOfLogs): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None:
        """
            Aggregates the provided instance into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AggregatableStatistic.aggregate`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`
        
            Parameters:
                other (:class:`~org.hipparchus.stat.descriptive.moment.GeometricMean`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, geometricMean: 'GeometricMean') -> None: ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'GeometricMean':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...

class Kurtosis(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, java.io.Serializable):
    """
    public class Kurtosis extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic` implements Serializable
    
        Computes the Kurtosis of the available values.
    
        We use the following (unbiased) formula to define kurtosis:
    
        kurtosis = { [n(n+1) / (n -1)(n - 2)(n-3)] sum[(x_i - mean)^4] / std^4 } - [3(n-1)^2 / (n-2)(n-3)]
    
        where n is the number of values, mean is the :class:`~org.hipparchus.stat.descriptive.moment.Mean` and std is the
        :class:`~org.hipparchus.stat.descriptive.moment.StandardDeviation`.
    
        Note that this statistic is undefined for n < 4. :code:`Double.Nan` is returned when there is not sufficient data to
        compute the statistic. Note that Double.NaN may also be returned if the input includes NaN and / or infinite values.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, fourthMoment: 'FourthMoment'): ...
    @typing.overload
    def __init__(self, kurtosis: 'Kurtosis'): ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'Kurtosis':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Note that when :meth:`~org.hipparchus.stat.descriptive.moment.Kurtosis.Kurtosis` is used to create a Variance, this
            method does nothing. In that case, the FourthMoment should be incremented directly.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...

class Mean(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Mean'], org.hipparchus.stat.descriptive.WeightedEvaluation, java.io.Serializable):
    """
    public class Mean extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic` implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.moment.Mean`>, :class:`~org.hipparchus.stat.descriptive.WeightedEvaluation`, Serializable
    
        Computes the arithmetic mean of a set of values. Uses the definitional formula:
    
        mean = sum(x_i) / n
    
        where :code:`n` is the number of observations.
    
        When :meth:`~org.hipparchus.stat.descriptive.moment.Mean.increment` is used to add data incrementally from a stream of
        (unstored) values, the value of the statistic that :meth:`~org.hipparchus.stat.descriptive.moment.Mean.getResult`
        returns is computed using the following recursive updating algorithm:
    
          1.  Initialize :code:`m =` the first value
          2.  For each additional value, update using
    
    
    :code:`m = m + (new value - m) / (number of observations)`
    
    
        If null is used to compute the mean of an array of stored values, a two-pass, corrected algorithm is used, starting with
        the definitional formula computed using the array of stored values and then correcting this by adding the mean deviation
        of the data values from the arithmetic mean. See, e.g. "Comparison of Several Algorithms for Computing Sample Means and
        Variances," Robert F. Ling, Journal of the American Statistical Association, Vol. 69, No. 348 (Dec., 1974), pp. 859-866.
    
        Returns :code:`Double.NaN` if the dataset is empty. Note that Double.NaN may also be returned if the input includes NaN
        and / or infinite values.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, firstMoment: 'FirstMoment'): ...
    @typing.overload
    def __init__(self, mean: 'Mean'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None:
        """
            Aggregates the provided instance into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AggregatableStatistic.aggregate`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`
        
            Parameters:
                other (:class:`~org.hipparchus.stat.descriptive.moment.Mean`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, mean: 'Mean') -> None: ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'Mean':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Note that when :meth:`~org.hipparchus.stat.descriptive.moment.Mean.Mean` is used to create a Mean, this method does
            nothing. In that case, the FirstMoment should be incremented directly.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...

class SemiVariance(org.hipparchus.stat.descriptive.AbstractUnivariateStatistic, java.io.Serializable):
    UPSIDE_VARIANCE: typing.ClassVar['SemiVariance.Direction'] = ...
    DOWNSIDE_VARIANCE: typing.ClassVar['SemiVariance.Direction'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, boolean: bool, direction: 'SemiVariance.Direction'): ...
    @typing.overload
    def __init__(self, direction: 'SemiVariance.Direction'): ...
    @typing.overload
    def __init__(self, semiVariance: 'SemiVariance'): ...
    def copy(self) -> 'SemiVariance': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float, direction: 'SemiVariance.Direction') -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float, direction: 'SemiVariance.Direction', boolean: bool, int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], direction: 'SemiVariance.Direction') -> float: ...
    def getVarianceDirection(self) -> 'SemiVariance.Direction': ...
    def isBiasCorrected(self) -> bool: ...
    def withBiasCorrected(self, boolean: bool) -> 'SemiVariance': ...
    def withVarianceDirection(self, direction: 'SemiVariance.Direction') -> 'SemiVariance': ...
    class Direction(java.lang.Enum['SemiVariance.Direction']):
        UPSIDE: typing.ClassVar['SemiVariance.Direction'] = ...
        DOWNSIDE: typing.ClassVar['SemiVariance.Direction'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SemiVariance.Direction': ...
        @staticmethod
        def values() -> typing.List['SemiVariance.Direction']: ...

class Skewness(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, java.io.Serializable):
    """
    public class Skewness extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic` implements Serializable
    
        Computes the skewness of the available values.
    
        We use the following (unbiased) formula to define skewness:
    
        skewness = [n / (n -1) (n - 2)] sum[(x_i - mean)^3] / std^3
    
        where n is the number of values, mean is the :class:`~org.hipparchus.stat.descriptive.moment.Mean` and std is the
        :class:`~org.hipparchus.stat.descriptive.moment.StandardDeviation`.
    
        Note that this statistic is undefined for n < 3. :code:`Double.Nan` is returned when there is not sufficient data to
        compute the statistic. Double.NaN may also be returned if the input includes NaN and / or infinite values.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, skewness: 'Skewness'): ...
    @typing.overload
    def __init__(self, thirdMoment: 'ThirdMoment'): ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'Skewness':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the value of the statistic based on the values that have been added.
        
            See :class:`~org.hipparchus.stat.descriptive.moment.Skewness` for the definition used in the computation.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                the skewness of the available values.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Note that when :meth:`~org.hipparchus.stat.descriptive.moment.Skewness.Skewness` is used to create a Skewness, this
            method does nothing. In that case, the ThirdMoment should be incremented directly.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...

class StandardDeviation(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, java.io.Serializable):
    """
    public class StandardDeviation extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic` implements Serializable
    
        Computes the sample standard deviation.
    
        The standard deviation is the positive square root of the variance. This implementation wraps a
        :class:`~org.hipparchus.stat.descriptive.moment.Variance` instance.
    
        The :code:`isBiasCorrected` property of the wrapped Variance instance is exposed, so that this class can be used to
        compute both the "sample standard deviation" (the square root of the bias-corrected "sample variance") or the
        "population standard deviation" (the square root of the non-bias-corrected "population variance"). See
        :class:`~org.hipparchus.stat.descriptive.moment.Variance` for more information.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, boolean: bool, secondMoment: 'SecondMoment'): ...
    @typing.overload
    def __init__(self, secondMoment: 'SecondMoment'): ...
    @typing.overload
    def __init__(self, standardDeviation: 'StandardDeviation'): ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'StandardDeviation':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float, int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...
    def isBiasCorrected(self) -> bool:
        """
        
            Returns:
                Returns the isBiasCorrected.
        
        
        """
        ...
    def withBiasCorrection(self, boolean: bool) -> 'StandardDeviation':
        """
            Returns a new copy of this standard deviation with the given bias correction setting.
        
            Parameters:
                biasCorrection (boolean): The bias correction flag to set.
        
            Returns:
                a copy of this instance with the given bias correction setting
        
        
        """
        ...

class Variance(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Variance'], org.hipparchus.stat.descriptive.WeightedEvaluation, java.io.Serializable):
    """
    public class Variance extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic` implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.moment.Variance`>, :class:`~org.hipparchus.stat.descriptive.WeightedEvaluation`, Serializable
    
        Computes the variance of the available values. By default, the unbiased "sample variance" definitional formula is used:
    
        variance = sum((x_i - mean)^2) / (n - 1)
    
        where mean is the :class:`~org.hipparchus.stat.descriptive.moment.Mean` and :code:`n` is the number of sample
        observations.
    
        The definitional formula does not have good numerical properties, so this implementation does not compute the statistic
        using the definitional formula.
    
          - The :code:`getResult` method computes the variance using updating formulas based on West's algorithm, as described in `
            Chan, T. F. and J. G. Lewis 1979, *Communications of the ACM*, vol. 22 no. 9, pp. 526-531.
            <http://doi.acm.org/10.1145/359146.359152>`
          - The :code:`evaluate` methods leverage the fact that they have the full array of values in memory to execute a two-pass
            algorithm. Specifically, these methods use the "corrected two-pass algorithm" from Chan, Golub, Levesque, *Algorithms
            for Computing the Sample Variance*, American Statistician, vol. 37, no. 3 (1983) pp. 242-247.
    
    
        Note that adding values using :code:`increment` or :code:`incrementAll` and then executing :code:`getResult` will
        sometimes give a different, less accurate, result than executing :code:`evaluate` with the full array of values. The
        former approach should only be used when the full array of values is not available.
    
        The "population variance" ( sum((x_i - mean)^2) / n ) can also be computed using this statistic. The
        :code:`isBiasCorrected` property determines whether the "population" or "sample" value is returned by the
        :code:`evaluate` and :code:`getResult` methods. To compute population variances, set this property to :code:`false.`
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, boolean: bool, secondMoment: 'SecondMoment'): ...
    @typing.overload
    def __init__(self, secondMoment: 'SecondMoment'): ...
    @typing.overload
    def __init__(self, variance: 'Variance'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None:
        """
            Aggregates the provided instance into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AggregatableStatistic.aggregate`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`
        
            Parameters:
                other (:class:`~org.hipparchus.stat.descriptive.moment.Variance`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, variance: 'Variance') -> None: ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.clear`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'Variance':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.copy`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float, int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float, int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getN`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.getResult`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            If all values are available, it is more accurate to use null rather than adding values one at a time using this method
            and then executing :meth:`~org.hipparchus.stat.descriptive.moment.Variance.getResult`, since :code:`evaluate` leverages
            the fact that is has the full list of values together to execute a two-pass algorithm. See
            :class:`~org.hipparchus.stat.descriptive.moment.Variance`.
        
            Note also that when :meth:`~org.hipparchus.stat.descriptive.moment.Variance.Variance` is used to create a Variance, this
            method does nothing. In that case, the SecondMoment should be incremented directly.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic.increment`Â in
                classÂ :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...
    def isBiasCorrected(self) -> bool:
        """
        
            Returns:
                Returns the isBiasCorrected.
        
        
        """
        ...
    def withBiasCorrection(self, boolean: bool) -> 'Variance':
        """
            Returns a new copy of this variance with the given bias correction setting.
        
            Parameters:
                biasCorrection (boolean): The bias correction flag to set.
        
            Returns:
                a copy of this instance with the given bias correction setting
        
        
        """
        ...

class FirstMoment: ...

class FourthMoment: ...

class ThirdMoment: ...

class SecondMoment(FirstMoment, org.hipparchus.stat.descriptive.AggregatableStatistic['SecondMoment'], java.io.Serializable):
    """
    public class SecondMoment extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic` implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.moment.SecondMoment`>, Serializable
    
        Computes a statistic related to the Second Central Moment. Specifically, what is computed is the sum of squared
        deviations from the sample mean.
    
        The following recursive updating formula is used:
    
        Let
    
          - dev = (current obs - previous mean)
          - n = number of observations (including current obs)
    
        Then
    
        new value = old value + dev^2 * (n - 1) / n.
    
        Returns :code:`Double.NaN` if no data values have been added and returns :code:`0` if there is just one value in the
        data set. Note that Double.NaN may also be returned if the input includes NaN and / or infinite values.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, secondMoment: 'SecondMoment'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None:
        """
            Aggregates the provided instance into this instance.
        
            This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance
            after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.AggregatableStatistic.aggregate`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`
        
            Parameters:
                other (:class:`~org.hipparchus.stat.descriptive.moment.SecondMoment`): the instance to aggregate into this instance
        
            Aggregates the results of the provided instance into this instance.
        
            Parameters:
                other (org.hipparchus.stat.descriptive.moment.FirstMoment): the instance to aggregate from
        
        
        """
        ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, secondMoment: 'SecondMoment') -> None: ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
        
        """
        ...
    def copy(self) -> 'SecondMoment':
        """
            Returns a copy of the statistic with the same internal state.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.UnivariateStatistic.copy`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.UnivariateStatistic`
        
            Returns:
                a copy of the statistic
        
        
        """
        ...
    def getResult(self) -> float:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.getResult`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def increment(self, double: float) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic.increment`Â in
                interfaceÂ :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic`
        
            Parameters:
                d (double): the new value.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.moment")``.

    FirstMoment: typing.Type[FirstMoment]
    FourthMoment: typing.Type[FourthMoment]
    GeometricMean: typing.Type[GeometricMean]
    Kurtosis: typing.Type[Kurtosis]
    Mean: typing.Type[Mean]
    SecondMoment: typing.Type[SecondMoment]
    SemiVariance: typing.Type[SemiVariance]
    Skewness: typing.Type[Skewness]
    StandardDeviation: typing.Type[StandardDeviation]
    ThirdMoment: typing.Type[ThirdMoment]
    Variance: typing.Type[Variance]
