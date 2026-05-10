
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
    Returns the product of the available values.
    
    If there are no values in the dataset, then 1 is returned. If any of the values are NaN, then NaN is returned.
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, original: 'Product'): ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Aggregates the provided instance into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Specified by: aggregate in interface AggregatableStatistic
        
        Parameters:
            other (Product): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'Product') -> None: ...
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        Specified by: clear in class AbstractStorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> 'Product':
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
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], weights: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
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

class Sum(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Sum'], org.hipparchus.stat.descriptive.WeightedEvaluation, java.io.Serializable):
    """
    Returns the sum of the available values.
    
    If there are no values in the dataset, then 0 is returned. If any of the values are NaN, then NaN is returned.
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, original: 'Sum'): ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Aggregates the provided instance into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Specified by: aggregate in interface AggregatableStatistic
        
        Parameters:
            other (Sum): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'Sum') -> None: ...
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        Specified by: clear in class AbstractStorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> 'Sum':
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
    def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def evaluate(self, values: typing.Union[typing.List[float], jpype.JArray], weights: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
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

class SumOfLogs(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['SumOfLogs'], java.io.Serializable):
    """
    Returns the sum of the natural logs for this collection of values.
    
    Uses hipparchus to compute the logs. Therefore,
    
      - If any of values are < 0, the result is NaN
      - If all values are non-negative and less than POSITIVE_INFINITY, but at least one value is 0, the result
        is NEGATIVE_INFINITY
      - If both POSITIVE_INFINITY and NEGATIVE_INFINITY are among the values, the result is
        NaN
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, original: 'SumOfLogs'): ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Aggregates the provided instance into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Specified by: aggregate in interface AggregatableStatistic
        
        Parameters:
            other (SumOfLogs): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'SumOfLogs') -> None: ...
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        Specified by: clear in class AbstractStorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> 'SumOfLogs':
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

class SumOfSquares(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['SumOfSquares'], java.io.Serializable):
    """
    Returns the sum of the squares of the available values.
    
    If there are no values in the dataset, then 0 is returned. If any of the values are NaN, then NaN is returned.
    
    Note that this implementation is not synchronized. If multiple threads access an instance of this class concurrently, and at least one of the threads invokes the increment() or clear() method, it must be synchronized externally.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, original: 'SumOfSquares'): ...
    @typing.overload
    def aggregate(self, other: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Aggregates the provided instance into this instance.
        
        This method can be used to combine statistics computed over partitions or subsamples - i.e., the value of this instance after this operation should be the same as if a single statistic would have been applied over the combined dataset.
        
        Specified by: aggregate in interface AggregatableStatistic
        
        Parameters:
            other (SumOfSquares): the instance to aggregate into this instance
        
        
        """
        ...
    @typing.overload
    def aggregate(self, *other: typing.Any) -> None: ...
    @typing.overload
    def aggregate(self, other: 'SumOfSquares') -> None: ...
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        
        Specified by: clear in interface StorelessUnivariateStatistic
        
        Specified by: clear in class AbstractStorelessUnivariateStatistic
        
        
        """
        ...
    def copy(self) -> 'SumOfSquares':
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.summary")``.

    Product: typing.Type[Product]
    Sum: typing.Type[Sum]
    SumOfLogs: typing.Type[SumOfLogs]
    SumOfSquares: typing.Type[SumOfSquares]
