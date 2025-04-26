
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus.linear
import org.hipparchus.stat.ranking
import typing



class Covariance:
    """
    public classCovariance extends :class:`~org.hipparchus.stat.correlation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Computes covariances for pairs of arrays or columns of a matrix.
    
        The constructors that take :code:`RealMatrix` or :code:`double[][]` arguments generate covariance matrices. The columns
        of the input matrices are assumed to represent variable values.
    
        The constructor argument :code:`biasCorrected` determines whether or not computed covariances are bias-corrected.
    
        Unbiased covariances are given by the formula:
    
        :code:`cov(X, Y) = Σ[(x :sub:`i` - E(X))(y :sub:`i` - E(Y))] / (n - 1)`
    
        where :code:`E(X)` is the mean of :code:`X` and :code:`E(Y)` is the mean of the :code:`Y` values.
    
        Non-bias-corrected estimates use :code:`n` in place of :code:`n - 1`.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, boolean: bool): ...
    @typing.overload
    def covariance(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def covariance(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...
    def getCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns the covariance matrix
        
            Returns:
                covariance matrix
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of observations (length of covariate vectors)
        
            Returns:
                number of observations
        
        
        """
        ...

class KendallsCorrelation:
    """
    public classKendallsCorrelation extends :class:`~org.hipparchus.stat.correlation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Implementation of Kendall's Tau-b rank correlation.
    
        A pair of observations (x :sub:`1` , y :sub:`1` ) and (x :sub:`2` , y :sub:`2` ) are considered *concordant* if x
        :sub:`1` < x :sub:`2` and y :sub:`1` < y :sub:`2` or x :sub:`2` < x :sub:`1` and y :sub:`2` < y :sub:`1` . The pair is
        *discordant* if x :sub:`1` < x :sub:`2` and y :sub:`2` < y :sub:`1` or x :sub:`2` < x :sub:`1` and y :sub:`1` < y
        :sub:`2` . If either x :sub:`1` = x :sub:`2` or y :sub:`1` = y :sub:`2` , the pair is neither concordant nor discordant.
    
        Kendall's Tau-b is defined as: \[ \tau_b = \frac{n_c - n_d}{\sqrt{(n_0 - n_1) (n_0 - n_2)}} \]
    
        where:
    
          - n :sub:`0` = n * (n - 1) / 2
          - n :sub:`c` = Number of concordant pairs
          - n :sub:`d` = Number of discordant pairs
          - n :sub:`1` = sum of t :sub:`i` * (t :sub:`i` - 1) / 2 for all i
          - n :sub:`2` = sum of u :sub:`j` * (u :sub:`j` - 1) / 2 for all j
          - t :sub:`i` = Number of tied values in the i :sup:`th` group of ties in x
          - u :sub:`j` = Number of tied values in the j :sup:`th` group of ties in y
    
    
        This implementation uses the O(n log n) algorithm described in William R. Knight's 1966 paper "A Computer Method for
        Calculating Kendall's Tau with Ungrouped Data" in the Journal of the American Statistical Association.
    
        Also see:
    
              - ` Kendall tau rank correlation coefficient (Wikipedia)
                <http://en.wikipedia.org/wiki/Kendall_tau_rank_correlation_coefficient>`
              - `A Computer Method for Calculating Kendall's Tau with Ungrouped Data <http://www.jstor.org/stable/2282833>`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def computeCorrelationMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
            Computes the Kendall's Tau rank correlation matrix for the columns of the input matrix.
        
            Parameters:
                matrix (:class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`): matrix with columns representing variables to correlate
        
            Returns:
                correlation matrix
        
            Computes the Kendall's Tau rank correlation matrix for the columns of the input rectangular array. The columns of the
            array represent values of variables to be correlated.
        
            Parameters:
                matrix (double[][]): matrix with columns representing variables to correlate
        
            Returns:
                correlation matrix
        
        
        """
        ...
    @typing.overload
    def computeCorrelationMatrix(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def correlation(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns the correlation matrix.
        
            Returns:
                correlation matrix
        
        
        """
        ...

class PearsonsCorrelation:
    """
    public classPearsonsCorrelation extends :class:`~org.hipparchus.stat.correlation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Computes Pearson's product-moment correlation coefficients for pairs of arrays or columns of a matrix.
    
        The constructors that take :code:`RealMatrix` or :code:`double[][]` arguments generate correlation matrices. The columns
        of the input matrices are assumed to represent variable values. Correlations are given by the formula:
    
        :code:`cor(X, Y) = Σ[(x :sub:`i` - E(X))(y :sub:`i` - E(Y))] / [(n - 1)s(X)s(Y)]`
    
        where :code:`E(X)` is the mean of :code:`X`, :code:`E(Y)` is the mean of the :code:`Y` values and s(X), s(Y) are
        standard deviations.
    
        To compute the correlation coefficient for a single pair of arrays, use
        :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.%3Cinit%3E` to construct an instance with no data and then
        :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.correlation`. Correlation matrices can also be computed
        directly from an instance with no data using
        :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.computeCorrelationMatrix`. In order to use
        :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.getCorrelationMatrix`,
        :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.getCorrelationPValues`, or
        :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.getCorrelationStandardErrors`; however, one of the
        constructors supplying data or a covariance matrix must be used to create the instance.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, int: int): ...
    @typing.overload
    def __init__(self, covariance: Covariance): ...
    @typing.overload
    def computeCorrelationMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
            Computes the correlation matrix for the columns of the input matrix, using
            :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.correlation`. Throws MathIllegalArgumentException if the
            matrix does not have at least two columns and two rows. Pairwise correlations are set to NaN if one of the correlates
            has zero variance.
        
            Parameters:
                matrix (:class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`): matrix with columns representing variables to correlate
        
            Returns:
                correlation matrix
        
            Raises:
                :class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`: if the matrix does not contain sufficient data
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.correlation`
        
        
            Computes the correlation matrix for the columns of the input rectangular array. The columns of the array represent
            values of variables to be correlated. Throws MathIllegalArgumentException if the matrix does not have at least two
            columns and two rows or if the array is not rectangular. Pairwise correlations are set to NaN if one of the correlates
            has zero variance.
        
            Parameters:
                data (double[][]): matrix with columns representing variables to correlate
        
            Returns:
                correlation matrix
        
            Raises:
                :class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`: if the array does not contain sufficient data
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.correlation`
        
        
        
        """
        ...
    @typing.overload
    def computeCorrelationMatrix(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def correlation(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Computes the Pearson's product-moment correlation coefficient between two arrays.
        
            Throws MathIllegalArgumentException if the arrays do not have the same length or their common length is less than 2.
            Returns :code:`NaN` if either of the arrays has zero variance (i.e., if one of the arrays does not contain at least two
            distinct values).
        
            Parameters:
                xArray (double[]): first data array
                yArray (double[]): second data array
        
            Returns:
                Returns Pearson's correlation coefficient for the two arrays
        
            Raises:
                :class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`: if the arrays lengths do not match
                :class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`: if there is insufficient data
        
        
        """
        ...
    def covarianceToCorrelation(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix:
        """
            Derives a correlation matrix from a covariance matrix.
        
            Uses the formula
        
        
            :code:`r(X,Y) = cov(X,Y)/s(X)s(Y)` where :code:`r(·,·)` is the correlation coefficient and :code:`s(·)` means
            standard deviation.
        
            Parameters:
                covarianceMatrix (:class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`): the covariance matrix
        
            Returns:
                correlation matrix
        
        
        """
        ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns the correlation matrix.
        
            This method will return null if the argumentless constructor was used to create this instance, even if
            :meth:`~org.hipparchus.stat.correlation.PearsonsCorrelation.computeCorrelationMatrix` has been called before it is
            activated.
        
            Returns:
                correlation matrix
        
        
        """
        ...
    def getCorrelationPValues(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns a matrix of p-values associated with the (two-sided) null hypothesis that the corresponding correlation
            coefficient is zero.
        
            :code:`getCorrelationPValues().getEntry(i,j)` is the probability that a random variable distributed as :code:`t
            :sub:`n-2`` takes a value with absolute value greater than or equal to
        
        
            :code:`|r|((n - 2) / (1 - r :sup:`2` )) :sup:`1/2``
        
            The values in the matrix are sometimes referred to as the *significance* of the corresponding correlation coefficients.
        
            To use this method, one of the constructors that supply an input matrix must have been used to create this instance.
        
            Returns:
                matrix of p-values
        
            Raises:
                :class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`: if an error occurs estimating probabilities
                :class:`~org.hipparchus.stat.correlation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if this instance was created with no data
        
        
        """
        ...
    def getCorrelationStandardErrors(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns a matrix of standard errors associated with the estimates in the correlation matrix.
        
        
            :code:`getCorrelationStandardErrors().getEntry(i,j)` is the standard error associated with
            :code:`getCorrelationMatrix.getEntry(i,j)`
        
            The formula used to compute the standard error is
        
        
            :code:`SE :sub:`r` = ((1 - r :sup:`2` ) / (n - 2)) :sup:`1/2`` where :code:`r` is the estimated correlation coefficient
            and :code:`n` is the number of observations in the source dataset.
        
            To use this method, one of the constructors that supply an input matrix must have been used to create this instance.
        
            Returns:
                matrix of correlation standard errors
        
            Raises:
                :class:`~org.hipparchus.stat.correlation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if this instance was created with no data
        
        
        """
        ...

class SpearmansCorrelation:
    """
    public classSpearmansCorrelation extends :class:`~org.hipparchus.stat.correlation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Spearman's rank correlation. This implementation performs a rank transformation on the input data and then computes
        :class:`~org.hipparchus.stat.correlation.PearsonsCorrelation` on the ranked data.
    
        By default, ranks are computed using :class:`~org.hipparchus.stat.ranking.NaturalRanking` with default strategies for
        handling NaNs and ties in the data (NaNs maximal, ties averaged). The ranking algorithm can be set using a constructor
        argument.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, rankingAlgorithm: typing.Union[org.hipparchus.stat.ranking.RankingAlgorithm, typing.Callable]): ...
    @typing.overload
    def __init__(self, rankingAlgorithm: typing.Union[org.hipparchus.stat.ranking.RankingAlgorithm, typing.Callable]): ...
    @typing.overload
    def computeCorrelationMatrix(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
            Computes the Spearman's rank correlation matrix for the columns of the input matrix.
        
            Parameters:
                matrix (:class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`): matrix with columns representing variables to correlate
        
            Returns:
                correlation matrix
        
            Computes the Spearman's rank correlation matrix for the columns of the input rectangular array. The columns of the array
            represent values of variables to be correlated.
        
            Parameters:
                matrix (double[][]): matrix with columns representing variables to correlate
        
            Returns:
                correlation matrix
        
        
        """
        ...
    @typing.overload
    def computeCorrelationMatrix(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def correlation(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Computes the Spearman's rank correlation coefficient between the two arrays.
        
            Parameters:
                xArray (double[]): first data array
                yArray (double[]): second data array
        
            Returns:
                Returns Spearman's rank correlation coefficient for the two arrays
        
            Raises:
                :class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`: if the arrays lengths do not match
                :class:`~org.hipparchus.stat.correlation.https:.www.hipparchus.org.hipparchus`: if the array length is less than 2
        
        
        """
        ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Calculate the Spearman Rank Correlation Matrix.
        
            Returns:
                Spearman Rank Correlation Matrix
        
            Raises:
                :class:`~org.hipparchus.stat.correlation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if this instance was created with no data
        
        
        """
        ...
    def getRankCorrelation(self) -> PearsonsCorrelation:
        """
            Returns a :class:`~org.hipparchus.stat.correlation.PearsonsCorrelation` instance constructed from the ranked input data.
            That is, :code:`new SpearmansCorrelation(matrix).getRankCorrelation()` is equivalent to :code:`new
            PearsonsCorrelation(rankTransform(matrix))` where :code:`rankTransform(matrix)` is the result of applying the configured
            :code:`RankingAlgorithm` to each of the columns of :code:`matrix.`
        
            Returns null if this instance was created with no data.
        
            Returns:
                PearsonsCorrelation among ranked column data
        
        
        """
        ...

class StorelessCovariance(Covariance):
    """
    public classStorelessCovariance extends :class:`~org.hipparchus.stat.correlation.Covariance`
    
        Covariance implementation that does not require input data to be stored in memory. The size of the covariance matrix is
        specified in the constructor. Specific elements of the matrix are incrementally updated with calls to incrementRow() or
        increment Covariance().
    
        This class is based on a paper written by Philippe Pébay: ` Formulas for Robust, One-Pass Parallel Computation of
        Covariances and Arbitrary-Order Statistical Moments
        <http://prod.sandia.gov/techlib/access-control.cgi/2008/086212.pdf>`, 2008, Technical Report SAND2008-6212, Sandia
        National Laboratories.
    
        Note: the underlying covariance matrix is symmetric, thus only the upper triangular part of the matrix is stored and
        updated each increment.
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, boolean: bool): ...
    def append(self, storelessCovariance: 'StorelessCovariance') -> None: ...
    def getCovariance(self, int: int, int2: int) -> float: ...
    def getCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix: ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getN(self) -> int: ...
    def increment(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.correlation")``.

    Covariance: typing.Type[Covariance]
    KendallsCorrelation: typing.Type[KendallsCorrelation]
    PearsonsCorrelation: typing.Type[PearsonsCorrelation]
    SpearmansCorrelation: typing.Type[SpearmansCorrelation]
    StorelessCovariance: typing.Type[StorelessCovariance]
