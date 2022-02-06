import typing



class BinomialProportion:
    """
    public class BinomialProportion extends Object
    
        Utility methods to generate confidence intervals for a binomial proportion.
    
        Also see:
            ` Binomial proportion confidence interval (Wikipedia)
            <http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval>`
    """
    @staticmethod
    def getAgrestiCoullInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...
    @staticmethod
    def getClopperPearsonInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...
    @staticmethod
    def getNormalApproximationInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...
    @staticmethod
    def getWilsonScoreInterval(int: int, double: float, double2: float) -> 'ConfidenceInterval': ...

class ConfidenceInterval:
    """
    public class ConfidenceInterval extends Object
    
        Represents an interval estimate of a population parameter.
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getConfidenceLevel(self) -> float:
        """
        
            Returns:
                the asserted probability that the interval contains the population parameter
        
        
        """
        ...
    def getLowerBound(self) -> float:
        """
        
            Returns:
                the lower endpoint of the interval
        
        
        """
        ...
    def getUpperBound(self) -> float:
        """
        
            Returns:
                the upper endpoint of the interval
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
            Returns:
                String representation of the confidence interval
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.interval")``.

    BinomialProportion: typing.Type[BinomialProportion]
    ConfidenceInterval: typing.Type[ConfidenceInterval]
