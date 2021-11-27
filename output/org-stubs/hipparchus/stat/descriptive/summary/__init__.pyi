import java.io
import java.lang
import org.hipparchus.stat.descriptive
import typing



class Product(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Product'], org.hipparchus.stat.descriptive.WeightedEvaluation, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, product: 'Product'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, product: 'Product') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'Product': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int: ...
    def getResult(self) -> float: ...
    def increment(self, double: float) -> None: ...

class Sum(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Sum'], org.hipparchus.stat.descriptive.WeightedEvaluation, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, sum: 'Sum'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, sum: 'Sum') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'Sum': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int: ...
    def getResult(self) -> float: ...
    def increment(self, double: float) -> None: ...

class SumOfLogs(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['SumOfLogs'], java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, sumOfLogs: 'SumOfLogs'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, sumOfLogs: 'SumOfLogs') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'SumOfLogs': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int: ...
    def getResult(self) -> float: ...
    def increment(self, double: float) -> None: ...

class SumOfSquares(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['SumOfSquares'], java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, sumOfSquares: 'SumOfSquares'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, sumOfSquares: 'SumOfSquares') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'SumOfSquares': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int: ...
    def getResult(self) -> float: ...
    def increment(self, double: float) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.summary")``.

    Product: typing.Type[Product]
    Sum: typing.Type[Sum]
    SumOfLogs: typing.Type[SumOfLogs]
    SumOfSquares: typing.Type[SumOfSquares]
