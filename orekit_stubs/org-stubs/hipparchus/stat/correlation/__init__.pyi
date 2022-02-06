import org.hipparchus.linear
import org.hipparchus.stat.ranking
import typing



class Covariance:
    """
    public class Covariance extends Object
    
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
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]], boolean: bool): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, boolean: bool): ...
    @typing.overload
    def covariance(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def covariance(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> float: ...
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
    public class KendallsCorrelation extends Object
    
        Implementation of Kendall's Tau-b rank correlation.
    
        A pair of observations (x :sub:`1` , y :sub:`1` ) and (x :sub:`2` , y :sub:`2` ) are considered *concordant* if x
        :sub:`1` < x :sub:`2` and y :sub:`1` < y :sub:`2` or x :sub:`2` < x :sub:`1` and y :sub:`2` < y :sub:`1` . The pair is
        *discordant* if x :sub:`1` < x :sub:`2` and y :sub:`2` < y :sub:`1` or x :sub:`2` < x :sub:`1` and y :sub:`1` < y
        :sub:`2` . If either x :sub:`1` = x :sub:`2` or y :sub:`1` = y :sub:`2` , the pair is neither concordant nor discordant.
    
        Kendall's Tau-b is defined as:
    
        .. code-block: java
        
         tau :sub:`b`  = (n :sub:`c`  - n :sub:`d` ) / sqrt((n :sub:`0`  - n :sub:`1` ) * (n :sub:`0`  - n :sub:`2` ))
         
    
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
            ` Kendall tau rank correlation coefficient (Wikipedia)
            <http://en.wikipedia.org/wiki/Kendall_tau_rank_correlation_coefficient>`, `A Computer Method for Calculating Kendall's
            Tau with Ungrouped Data <http://www.jstor.org/stable/2282833>`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def computeCorrelationMatrix(self, doubleArray: typing.List[typing.List[float]]) -> org.hipparchus.linear.RealMatrix:
        """
            Computes the Kendall's Tau rank correlation matrix for the columns of the input matrix.
        
            Parameters:
                matrix (RealMatrix): matrix with columns representing variables to correlate
        
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
    def correlation(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Returns the correlation matrix.
        
            Returns:
                correlation matrix
        
        
        """
        ...

class PearsonsCorrelation:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, int: int): ...
    @typing.overload
    def __init__(self, covariance: Covariance): ...
    @typing.overload
    def computeCorrelationMatrix(self, doubleArray: typing.List[typing.List[float]]) -> org.hipparchus.linear.RealMatrix: ...
    @typing.overload
    def computeCorrelationMatrix(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def correlation(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    def covarianceToCorrelation(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix: ...
    def getCorrelationPValues(self) -> org.hipparchus.linear.RealMatrix: ...
    def getCorrelationStandardErrors(self) -> org.hipparchus.linear.RealMatrix: ...

class SpearmansCorrelation:
    """
    public class SpearmansCorrelation extends Object
    
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
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, rankingAlgorithm: org.hipparchus.stat.ranking.RankingAlgorithm): ...
    @typing.overload
    def __init__(self, rankingAlgorithm: org.hipparchus.stat.ranking.RankingAlgorithm): ...
    @typing.overload
    def computeCorrelationMatrix(self, doubleArray: typing.List[typing.List[float]]) -> org.hipparchus.linear.RealMatrix:
        """
            Computes the Spearman's rank correlation matrix for the columns of the input matrix.
        
            Parameters:
                matrix (RealMatrix): matrix with columns representing variables to correlate
        
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
    def correlation(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float:
        """
            Computes the Spearman's rank correlation coefficient between the two arrays.
        
            Parameters:
                xArray (double[]): first data array
                yArray (double[]): second data array
        
            Returns:
                Returns Spearman's rank correlation coefficient for the two arrays
        
            Raises:
                : if the arrays lengths do not match
                : if the array length is less than 2
        
        
        """
        ...
    def getCorrelationMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Calculate the Spearman Rank Correlation Matrix.
        
            Returns:
                Spearman Rank Correlation Matrix
        
            Raises:
                : if this instance was created with no data
        
        
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
    public class StorelessCovariance extends :class:`~org.hipparchus.stat.correlation.Covariance`
    
        Covariance implementation that does not require input data to be stored in memory. The size of the covariance matrix is
        specified in the constructor. Specific elements of the matrix are incrementally updated with calls to incrementRow() or
        increment Covariance().
    
        This class is based on a paper written by Philippe PÃ©bay: ` Formulas for Robust, One-Pass Parallel Computation of
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
    def getData(self) -> typing.List[typing.List[float]]: ...
    def getN(self) -> int: ...
    def increment(self, doubleArray: typing.List[float]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.correlation")``.

    Covariance: typing.Type[Covariance]
    KendallsCorrelation: typing.Type[KendallsCorrelation]
    PearsonsCorrelation: typing.Type[PearsonsCorrelation]
    SpearmansCorrelation: typing.Type[SpearmansCorrelation]
    StorelessCovariance: typing.Type[StorelessCovariance]
