
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
    Computes covariances for pairs of arrays or columns of a matrix.
    
    The constructors that take RealMatrix or double[][] arguments generate covariance matrices. The columns of the input matrices are assumed to represent variable values.
    
    The constructor argument biasCorrected determines whether or not computed covariances are bias-corrected.
    
    Unbiased covariances are given by the formula:
    
    i` - E(X))(y :sub:`i` - E(Y))] / (n - 1)`
    
    where E(X) is the mean of X and E(Y) is the mean of the Y values.
    
    Non-bias-corrected estimates use n in place of n - 1.
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
    def covariance(self, xArray: typing.Union[typing.List[float], jpype.JArray], yArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def covariance(self, xArray: typing.Union[typing.List[float], jpype.JArray], yArray: typing.Union[typing.List[float], jpype.JArray], biasCorrected: bool) -> float: ...
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
    Implementation of Kendall's Tau-b rank correlation.
    
    A pair of observations (x :sub:`1` , y :sub:`1` ) and (x :sub:`2` , y :sub:`2` ) are considered concordant if x :sub:`1` < x :sub:`2` and y :sub:`1` < y :sub:`2` or x :sub:`2` < x :sub:`1` and y :sub:`2` < y :sub:`1` . The pair is discordant if x :sub:`1` < x :sub:`2` and y :sub:`2` < y :sub:`1` or x :sub:`2` < x :sub:`1` and y :sub:`1` < y :sub:`2` . If either x :sub:`1` = x :sub:`2` or y :sub:`1` = y :sub:`2` , the pair is neither concordant nor discordant.
    
    Kendall's Tau-b is defined as: \[ \tau_b = \frac{n_c - n_d}{\sqrt{(n_0 - n_1) (n_0 - n_2)}} \]
    
    where:
    
      - n :sub:`0` = n * (n - 1) / 2
      - n :sub:`c` = Number of concordant pairs
      - n :sub:`d` = Number of discordant pairs
      - n :sub:`1` = sum of t :sub:`i` * (t :sub:`i` - 1) / 2 for all i
      - n :sub:`2` = sum of u :sub:`j` * (u :sub:`j` - 1) / 2 for all j
      - t :sub:`i` = Number of tied values in the i :sup:`th` group of ties in x
      - u :sub:`j` = Number of tied values in the j :sup:`th` group of ties in y
    
    This implementation uses the O(n log n) algorithm described in William R. Knight's 1966 paper "A Computer Method for Calculating Kendall's Tau with Ungrouped Data" in the Journal of the American Statistical Association.
    
    Also see:
        ` Kendall tau rank correlation coefficient (Wikipedia)
        <http://en.wikipedia.org/wiki/Kendall_tau_rank_correlation_coefficient>`, `A Computer Method for Calculating Kendall's
        Tau with Ungrouped Data <http://www.jstor.org/stable/2282833>`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def computeCorrelationMatrix(self, matrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Computes the Kendall's Tau rank correlation matrix for the columns of the input matrix.
        
        Parameters:
            matrix (hipparchus): matrix with columns representing variables to correlate
        
        Returns:
            correlation matrix
        
        Computes the Kendall's Tau rank correlation matrix for the columns of the input rectangular array. The columns of the array represent values of variables to be correlated.
        
        Parameters:
            matrix (double[][]): matrix with columns representing variables to correlate
        
        Returns:
            correlation matrix
        
        
        """
        ...
    @typing.overload
    def computeCorrelationMatrix(self, matrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def correlation(self, xArray: typing.Union[typing.List[float], jpype.JArray], yArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the Kendall's Tau rank correlation coefficient between the two arrays.
        
        Parameters:
            xArray (double[]): first data array
            yArray (double[]): second data array
        
        Returns:
            Returns Kendall's Tau rank correlation coefficient for the two arrays
        
        Raises:
            hipparchus: if the arrays lengths do not match
        
        
        """
        ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Returns the correlation matrix.
        
        Returns:
            correlation matrix
        
        
        """
        ...

class PearsonsCorrelation:
    """
    Computes Pearson's product-moment correlation coefficients for pairs of arrays or columns of a matrix.
    
    The constructors that take RealMatrix or double[][] arguments generate correlation matrices. The columns of the input matrices are assumed to represent variable values. Correlations are given by the formula:
    
    i` - E(X))(y :sub:`i` - E(Y))] / [(n - 1)s(X)s(Y)]`
    
    where E(X) is the mean of X, E(Y) is the mean of the Y values and s(X), s(Y) are standard deviations.
    
    To compute the correlation coefficient for a single pair of arrays, use to construct an instance with no data and then correlation. Correlation matrices can also be computed directly from an instance with no data using computeCorrelationMatrix. In order to use getCorrelationMatrix, getCorrelationPValues, or getCorrelationStandardErrors; however, one of the constructors supplying data or a covariance matrix must be used to create the instance.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, covarianceMatrix: org.hipparchus.linear.RealMatrix, numberOfObservations: int): ...
    @typing.overload
    def __init__(self, covariance: Covariance): ...
    @typing.overload
    def computeCorrelationMatrix(self, matrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Computes the correlation matrix for the columns of the input matrix, using correlation. Throws MathIllegalArgumentException if the matrix does not have at least two columns and two rows. Pairwise correlations are set to NaN if one of the correlates has zero variance.
        
        Parameters:
            matrix (hipparchus): matrix with columns representing variables to correlate
        
        Returns:
            correlation matrix
        
        Raises:
            hipparchus: if the matrix does not contain sufficient data
        
        Also see:
            correlation
        
        Computes the correlation matrix for the columns of the input rectangular array. The columns of the array represent values of variables to be correlated. Throws MathIllegalArgumentException if the matrix does not have at least two columns and two rows or if the array is not rectangular. Pairwise correlations are set to NaN if one of the correlates has zero variance.
        
        Parameters:
            data (double[][]): matrix with columns representing variables to correlate
        
        Returns:
            correlation matrix
        
        Raises:
            hipparchus: if the array does not contain sufficient data
        
        Also see:
            correlation
        
        
        """
        ...
    @typing.overload
    def computeCorrelationMatrix(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def correlation(self, xArray: typing.Union[typing.List[float], jpype.JArray], yArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the Pearson's product-moment correlation coefficient between two arrays.
        
        Throws MathIllegalArgumentException if the arrays do not have the same length or their common length is less than 2. Returns NaN if either of the arrays has zero variance (i.e., if one of the arrays does not contain at least two distinct values).
        
        Parameters:
            xArray (double[]): first data array
            yArray (double[]): second data array
        
        Returns:
            Returns Pearson's correlation coefficient for the two arrays
        
        Raises:
            hipparchus: if the arrays lengths do not match
            hipparchus: if there is insufficient data
        
        
        """
        ...
    def covarianceToCorrelation(self, covarianceMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix:
        """
        Derives a correlation matrix from a covariance matrix.
        
        Uses the formula
        
        r(X,Y) = cov(X,Y)/s(X)s(Y) where r(·,·) is the correlation coefficient and s(·) means standard deviation.
        
        Parameters:
            covarianceMatrix (hipparchus): the covariance matrix
        
        Returns:
            correlation matrix
        
        
        """
        ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Returns the correlation matrix.
        
        This method will return null if the argumentless constructor was used to create this instance, even if computeCorrelationMatrix has been called before it is activated.
        
        Returns:
            correlation matrix
        
        
        """
        ...
    def getCorrelationPValues(self) -> org.hipparchus.linear.RealMatrix:
        """
        Returns a matrix of p-values associated with the (two-sided) null hypothesis that the corresponding correlation coefficient is zero.
        
        getEntry(i,j) is the probability that a random variable distributed as n-2`` takes a value with absolute value greater than or equal to
        
        2` )) :sup:`1/2``
        
        The values in the matrix are sometimes referred to as the significance of the corresponding correlation coefficients.
        
        To use this method, one of the constructors that supply an input matrix must have been used to create this instance.
        
        Returns:
            matrix of p-values
        
        Raises:
            hipparchus: if an error occurs estimating probabilities
            NullPointerException: if this instance was created with no data
        
        
        """
        ...
    def getCorrelationStandardErrors(self) -> org.hipparchus.linear.RealMatrix:
        """
        Returns a matrix of standard errors associated with the estimates in the correlation matrix.
        
        getEntry(i,j) is the standard error associated with getEntry(i,j)
        
        The formula used to compute the standard error is
        
        r` = ((1 - r :sup:`2` ) / (n - 2)) :sup:`1/2`` where r is the estimated correlation coefficient and n is the number of observations in the source dataset.
        
        To use this method, one of the constructors that supply an input matrix must have been used to create this instance.
        
        Returns:
            matrix of correlation standard errors
        
        Raises:
            NullPointerException: if this instance was created with no data
        
        
        """
        ...

class SpearmansCorrelation:
    """
    Spearman's rank correlation. This implementation performs a rank transformation on the input data and then computes PearsonsCorrelation on the ranked data.
    
    By default, ranks are computed using NaturalRanking with default strategies for handling NaNs and ties in the data (NaNs maximal, ties averaged). The ranking algorithm can be set using a constructor argument.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, dataMatrix: org.hipparchus.linear.RealMatrix, rankingAlgorithm: typing.Union[org.hipparchus.stat.ranking.RankingAlgorithm, typing.Callable]): ...
    @typing.overload
    def __init__(self, rankingAlgorithm: typing.Union[org.hipparchus.stat.ranking.RankingAlgorithm, typing.Callable]): ...
    @typing.overload
    def computeCorrelationMatrix(self, matrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Computes the Spearman's rank correlation matrix for the columns of the input matrix.
        
        Parameters:
            matrix (hipparchus): matrix with columns representing variables to correlate
        
        Returns:
            correlation matrix
        
        Computes the Spearman's rank correlation matrix for the columns of the input rectangular array. The columns of the array represent values of variables to be correlated.
        
        Parameters:
            matrix (double[][]): matrix with columns representing variables to correlate
        
        Returns:
            correlation matrix
        
        
        """
        ...
    @typing.overload
    def computeCorrelationMatrix(self, matrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def correlation(self, xArray: typing.Union[typing.List[float], jpype.JArray], yArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the Spearman's rank correlation coefficient between the two arrays.
        
        Parameters:
            xArray (double[]): first data array
            yArray (double[]): second data array
        
        Returns:
            Returns Spearman's rank correlation coefficient for the two arrays
        
        Raises:
            hipparchus: if the arrays lengths do not match
            hipparchus: if the array length is less than 2
        
        
        """
        ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Calculate the Spearman Rank Correlation Matrix.
        
        Returns:
            Spearman Rank Correlation Matrix
        
        Raises:
            NullPointerException: if this instance was created with no data
        
        
        """
        ...
    def getRankCorrelation(self) -> PearsonsCorrelation:
        """
        Returns a PearsonsCorrelation instance constructed from the ranked input data. That is, getRankCorrelation() is equivalent to new PearsonsCorrelation(rankTransform(matrix)) where rankTransform(matrix) is the result of applying the configured RankingAlgorithm to each of the columns of matrix
        
        Returns null if this instance was created with no data.
        
        Returns:
            PearsonsCorrelation among ranked column data
        
        
        """
        ...

class StorelessCovariance(Covariance):
    """
    Covariance implementation that does not require input data to be stored in memory. The size of the covariance matrix is specified in the constructor. Specific elements of the matrix are incrementally updated with calls to incrementRow() or increment Covariance().
    
    This class is based on a paper written by Philippe Pébay: ` Formulas for Robust, One-Pass Parallel Computation of Covariances and Arbitrary-Order Statistical Moments <http://prod.sandia.gov/techlib/access-control.cgi/2008/086212.pdf>`, 2008, Technical Report SAND2008-6212, Sandia National Laboratories.
    
    Note: the underlying covariance matrix is symmetric, thus only the upper triangular part of the matrix is stored and updated each increment.
    """
    @typing.overload
    def __init__(self, dim: int): ...
    @typing.overload
    def __init__(self, dim: int, biasCorrected: bool): ...
    def append(self, sc: 'StorelessCovariance') -> None:
        """
        Appends sc to this, effectively aggregating the computations in sc with this. After invoking this method, covariances returned should be close to what would have been obtained by performing all of the increment operations in sc directly on this.
        
        Parameters:
            sc (StorelessCovariance): externally computed StorelessCovariance to add to this
        
        Raises:
            hipparchus: if the dimension of sc does not match this
        
        
        """
        ...
    def getCovariance(self, xIndex: int, yIndex: int) -> float:
        """
        Get the covariance for an individual element of the covariance matrix.
        
        Parameters:
            xIndex (int): row index in the covariance matrix
            yIndex (int): column index in the covariance matrix
        
        Returns:
            the covariance of the given element
        
        Raises:
            hipparchus: if the number of observations in the cell is < 2
        
        
        """
        ...
    def getCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Returns the covariance matrix
        
        Overrides: getCovarianceMatrix in class Covariance
        
        Returns:
            covariance matrix
        
        Raises:
            hipparchus: if the number of observations in a cell is < 2
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Return the covariance matrix as two-dimensional array.
        
        Returns:
            a two-dimensional double array of covariance values
        
        Raises:
            hipparchus: if the number of observations for a cell is < 2
        
        
        """
        ...
    def getN(self) -> int:
        """
        This Covariance method is not supported by a StorelessCovariance, since the number of bivariate observations does not have to be the same for different pairs of covariates - i.e., N as defined in getN is undefined.
        
        Overrides: getN in class Covariance
        
        Returns:
            nothing as this implementation always throws a
            hipparchus
        
        Raises:
            hipparchus: in all cases
        
        
        """
        ...
    def increment(self, data: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Increment the covariance matrix with one row of data.
        
        Parameters:
            data (double[]): array representing one row of data.
        
        Raises:
            hipparchus: if the length of rowData does not match with the covariance matrix
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.correlation")``.

    Covariance: typing.Type[Covariance]
    KendallsCorrelation: typing.Type[KendallsCorrelation]
    PearsonsCorrelation: typing.Type[PearsonsCorrelation]
    SpearmansCorrelation: typing.Type[SpearmansCorrelation]
    StorelessCovariance: typing.Type[StorelessCovariance]
