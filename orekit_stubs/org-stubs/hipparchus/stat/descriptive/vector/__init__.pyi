
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jpype
import org.hipparchus.linear
import org.hipparchus.stat.descriptive
import typing



class VectorialCovariance(java.io.Serializable):
    """
    Returns the covariance matrix of the available vectors.
    
    Also see:
        serialized
    """
    def __init__(self, dimension: int, isBiasCorrected: bool):
        """
        Constructs a VectorialCovariance.
        
        Parameters:
            dimension (int): vectors dimension
            isBiasCorrected (boolean): if true, computed the unbiased sample covariance, otherwise computes the biased population covariance
        
        
        """
        ...
    def clear(self) -> None:
        """
        Clears the internal state of the Statistic
        """
        ...
    def equals(self, obj: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getN(self) -> int:
        """
        Get the number of vectors in the sample.
        
        Returns:
            number of vectors in the sample
        
        
        """
        ...
    def getResult(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the covariance matrix.
        
        Returns:
            covariance matrix
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def increment(self, v: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add a new vector to the sample.
        
        Parameters:
            v (double[]): vector to add
        
        Raises:
            hipparchus: if the vector does not have the right dimension
        
        
        """
        ...

class VectorialStorelessStatistic(org.hipparchus.stat.descriptive.StorelessMultivariateStatistic, java.io.Serializable):
    """
    Uses an independent StorelessUnivariateStatistic instance for each component of a vector.
    
    Also see:
        serialized
    """
    def __init__(self, dimension: int, univariateStatistic: org.hipparchus.stat.descriptive.StorelessUnivariateStatistic):
        """
        Create a new VectorialStorelessStatistic with the given dimension and statistic implementation. A copy of the provided statistic will be created for each component of the vector.
        
        Parameters:
            dimension (int): the vector dimension
            univariateStatistic (StorelessUnivariateStatistic): the prototype statistic
        
        Raises:
            hipparchus: if dimension < 1
        
        
        """
        ...
    def clear(self) -> None:
        """
        Clears the internal state of the statistic.
        
        Specified by: clear in interface StorelessMultivariateStatistic
        
        
        """
        ...
    def equals(self, obj: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Returns the dimension of the statistic.
        
        Specified by: getDimension in interface StorelessMultivariateStatistic
        
        Returns:
            the dimension of the statistic
        
        
        """
        ...
    def getN(self) -> int:
        """
        Returns the number of values that have been added.
        
        Specified by: getN in interface StorelessMultivariateStatistic
        
        Returns:
            the number of values.
        
        
        """
        ...
    def getResult(self) -> typing.MutableSequence[float]:
        """
        Returns the current value of the Statistic.
        
        Specified by: getResult in interface StorelessMultivariateStatistic
        
        Returns:
            value of the statistic, NaN if it has been cleared or just instantiated.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def increment(self, d: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Updates the internal state of the statistic to reflect the addition of the new value.
        
        Specified by: increment in interface StorelessMultivariateStatistic
        
        Parameters:
            d (double[]): the new value
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.vector")``.

    VectorialCovariance: typing.Type[VectorialCovariance]
    VectorialStorelessStatistic: typing.Type[VectorialStorelessStatistic]
