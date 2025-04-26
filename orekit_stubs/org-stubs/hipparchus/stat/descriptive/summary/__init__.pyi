
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus.stat.descriptive
import typing



class Product(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Product'], org.hipparchus.stat.descriptive.WeightedEvaluation, java.io.Serializable):
    """
    public classProduct extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.summary.Product`>, :class:`~org.hipparchus.stat.descriptive.WeightedEvaluation`, :class:`~org.hipparchus.stat.descriptive.summary.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Returns the product of the available values.
    
        If there are no values in the dataset, then 1 is returned. If any of the values are :code:`NaN`, then :code:`NaN` is
        returned.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, product: 'Product'): ...
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
                other (:class:`~org.hipparchus.stat.descriptive.summary.Product`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, product: 'Product') -> None: ...
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
    def copy(self) -> 'Product':
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
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
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

class Sum(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Sum'], org.hipparchus.stat.descriptive.WeightedEvaluation, java.io.Serializable):
    """
    public classSum extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.summary.Sum`>, :class:`~org.hipparchus.stat.descriptive.WeightedEvaluation`, :class:`~org.hipparchus.stat.descriptive.summary.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Returns the sum of the available values.
    
        If there are no values in the dataset, then 0 is returned. If any of the values are :code:`NaN`, then :code:`NaN` is
        returned.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, sum: 'Sum'): ...
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
                other (:class:`~org.hipparchus.stat.descriptive.summary.Sum`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, sum: 'Sum') -> None: ...
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
    def copy(self) -> 'Sum':
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
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
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

class SumOfLogs(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['SumOfLogs'], java.io.Serializable):
    """
    public classSumOfLogs extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.summary.SumOfLogs`>, :class:`~org.hipparchus.stat.descriptive.summary.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Returns the sum of the natural logs for this collection of values.
    
        Uses :meth:`~org.hipparchus.stat.descriptive.summary.https:.www.hipparchus.org.hipparchus` to compute the logs.
        Therefore,
    
          - If any of values are < 0, the result is :code:`NaN.`
          - If all values are non-negative and less than :code:`Double.POSITIVE_INFINITY`, but at least one value is 0, the result
            is :code:`Double.NEGATIVE_INFINITY.`
          - If both :code:`Double.POSITIVE_INFINITY` and :code:`Double.NEGATIVE_INFINITY` are among the values, the result is
            :code:`NaN.`
    
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, sumOfLogs: 'SumOfLogs'): ...
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
                other (:class:`~org.hipparchus.stat.descriptive.summary.SumOfLogs`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, sumOfLogs: 'SumOfLogs') -> None: ...
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
    def copy(self) -> 'SumOfLogs':
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

class SumOfSquares(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['SumOfSquares'], java.io.Serializable):
    """
    public classSumOfSquares extends :class:`~org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic`
    implements :class:`~org.hipparchus.stat.descriptive.AggregatableStatistic`<:class:`~org.hipparchus.stat.descriptive.summary.SumOfSquares`>, :class:`~org.hipparchus.stat.descriptive.summary.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Returns the sum of the squares of the available values.
    
        If there are no values in the dataset, then 0 is returned. If any of the values are :code:`NaN`, then :code:`NaN` is
        returned.
    
        **Note that this implementation is not synchronized.** If multiple threads access an instance of this class
        concurrently, and at least one of the threads invokes the :code:`increment()` or :code:`clear()` method, it must be
        synchronized externally.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, sumOfSquares: 'SumOfSquares'): ...
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
                other (:class:`~org.hipparchus.stat.descriptive.summary.SumOfSquares`): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *t: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, sumOfSquares: 'SumOfSquares') -> None: ...
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
    def copy(self) -> 'SumOfSquares':
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.summary")``.

    Product: typing.Type[Product]
    Sum: typing.Type[Sum]
    SumOfLogs: typing.Type[SumOfLogs]
    SumOfSquares: typing.Type[SumOfSquares]
