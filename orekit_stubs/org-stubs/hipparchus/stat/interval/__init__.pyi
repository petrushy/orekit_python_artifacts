
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



class BinomialProportion:
    """
    public classBinomialProportion extends :class:`~org.hipparchus.stat.interval.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Utility methods to generate confidence intervals for a binomial proportion.
    
        Also see:
    
              - ` Binomial proportion confidence interval (Wikipedia)
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
    public classConfidenceInterval extends :class:`~org.hipparchus.stat.interval.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Represents an interval estimate of a population parameter.
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getConfidenceLevel(self) -> float:
        """
            Get asserted probability that the interval contains the population parameter.
        
            Returns:
                the asserted probability that the interval contains the population parameter
        
        
        """
        ...
    def getLowerBound(self) -> float:
        """
            Get lower endpoint of the interval.
        
            Returns:
                the lower endpoint of the interval
        
        
        """
        ...
    def getUpperBound(self) -> float:
        """
            Get upper endpoint of the interval.
        
            Returns:
                the upper endpoint of the interval
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get String representation of the confidence interval.
        
            Overrides:
                :meth:`~org.hipparchus.stat.interval.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.stat.interval.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                String representation of the confidence interval
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.interval")``.

    BinomialProportion: typing.Type[BinomialProportion]
    ConfidenceInterval: typing.Type[ConfidenceInterval]
