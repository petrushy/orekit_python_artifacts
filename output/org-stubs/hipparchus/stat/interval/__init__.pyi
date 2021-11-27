import typing



class BinomialProportion:
    @staticmethod
    def getAgrestiCoullInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...
    @staticmethod
    def getClopperPearsonInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...
    @staticmethod
    def getNormalApproximationInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...
    @staticmethod
    def getWilsonScoreInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...

class ConfidenceInterval:
    def __init__(self, double: float, double2: float, double3: float): ...
    def getConfidenceLevel(self) -> float: ...
    def getLowerBound(self) -> float: ...
    def getUpperBound(self) -> float: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.interval")``.

    BinomialProportion: typing.Type[BinomialProportion]
    ConfidenceInterval: typing.Type[ConfidenceInterval]
