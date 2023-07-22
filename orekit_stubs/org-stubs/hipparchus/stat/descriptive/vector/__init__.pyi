import java.io
import org.hipparchus.linear
import org.hipparchus.stat.descriptive
import typing



class VectorialCovariance(java.io.Serializable):
    """
    public class VectorialCovariance extends :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Returns the covariance matrix of the available vectors.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, boolean: bool): ...
    def clear(self) -> None:
        """
            Clears the internal state of the Statistic
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
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
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def increment(self, doubleArray: typing.List[float]) -> None: ...

class VectorialStorelessStatistic(org.hipparchus.stat.descriptive.StorelessMultivariateStatistic, java.io.Serializable):
    """
    public class VectorialStorelessStatistic extends :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic`, :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Uses an independent :class:`~org.hipparchus.stat.descriptive.StorelessUnivariateStatistic` instance for each component
        of a vector.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, storelessUnivariateStatistic: org.hipparchus.stat.descriptive.StorelessUnivariateStatistic): ...
    def clear(self) -> None:
        """
            Clears the internal state of the statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic.clear` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the dimension of the statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic.getDimension` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic`
        
            Returns:
                the dimension of the statistic
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of values that have been added.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic.getN` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic`
        
            Returns:
                the number of values.
        
        
        """
        ...
    def getResult(self) -> typing.List[float]:
        """
            Returns the current value of the Statistic.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic.getResult` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic`
        
            Returns:
                value of the statistic, :code:`Double.NaN` if it has been cleared or just instantiated.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.stat.descriptive.vector.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def increment(self, doubleArray: typing.List[float]) -> None:
        """
            Updates the internal state of the statistic to reflect the addition of the new value.
        
            Specified by:
                :meth:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic.increment` in
                interface :class:`~org.hipparchus.stat.descriptive.StorelessMultivariateStatistic`
        
            Parameters:
                d (double[]): the new value
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.vector")``.

    VectorialCovariance: typing.Type[VectorialCovariance]
    VectorialStorelessStatistic: typing.Type[VectorialStorelessStatistic]
