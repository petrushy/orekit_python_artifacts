import java.io
import org.hipparchus.linear
import typing



class MultipleLinearRegression:
    """
    public interface MultipleLinearRegression
    
        The multiple linear regression can be represented in matrix-notation.
    
        .. code-block: java
        
          y=X*b+u
         
        where y is an :code:`n-vector` **regressand**, X is a :code:`[n,k]` matrix whose :code:`k` columns are called
        **regressors**, b is :code:`k-vector` of **regression parameters** and :code:`u` is an :code:`n-vector` of **error
        terms** or **residuals**. The notation is quite standard in literature, cf eg `Davidson and MacKinnon, Econometrics
        Theory and Methods, 2004 <http://www.econ.queensu.ca/ETM>`.
    """
    def estimateRegressandVariance(self) -> float:
        """
            Returns the variance of the regressand, ie Var(y).
        
            Returns:
                The double representing the variance of y
        
        
        """
        ...
    def estimateRegressionParameters(self) -> typing.List[float]:
        """
            Estimates the regression parameters b.
        
            Returns:
                The [k,1] array representing b
        
        
        """
        ...
    def estimateRegressionParametersStandardErrors(self) -> typing.List[float]:
        """
            Returns the standard errors of the regression parameters.
        
            Returns:
                standard errors of estimated regression parameters
        
        
        """
        ...
    def estimateRegressionParametersVariance(self) -> typing.List[typing.List[float]]:
        """
            Estimates the variance of the regression parameters, ie Var(b).
        
            Returns:
                The [k,k] array representing the variance of b
        
        
        """
        ...
    def estimateResiduals(self) -> typing.List[float]:
        """
            Estimates the residuals, ie u = y - X*b.
        
            Returns:
                The [n,1] array representing the residuals
        
        
        """
        ...

class RegressionResults(java.io.Serializable):
    """
    public class RegressionResults extends Object implements Serializable
    
        Results of a Multiple Linear Regression model fit.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], boolean: bool, long: int, int: int, double3: float, double4: float, double5: float, boolean2: bool, boolean3: bool): ...
    def getAdjustedRSquared(self) -> float:
        """
        
            Returns the adjusted R-squared statistic, defined by the formula
        
            .. code-block: java
            
             R :sup:`2`  :sub:`adj`  = 1 - [SSR (n - 1)] / [SSTO (n - p)]
             
            where SSR is the sum of squared residuals}, SSTO is the total sum of squares}, n is the number of observations and p is
            the number of parameters estimated (including the intercept).
        
            If the regression is estimated without an intercept term, what is returned is
        
            .. code-block: java
            
             :meth:`~org.hipparchus.stat.regression.RegressionResults.getRSquared`
             
        
            Returns:
                adjusted R-Squared statistic
        
        
        """
        ...
    def getCovarianceOfParameters(self, int: int, int2: int) -> float: ...
    def getErrorSumSquares(self) -> float:
        """
        
            Returns the ` sum of squared errors <http://www.xycoon.com/SumOfSquares.htm>` (SSE) associated with the regression
            model.
        
            The return value is constrained to be non-negative - i.e., if due to rounding errors the computational formula returns a
            negative result, 0 is returned.
        
            **Preconditions**:
        
              - numberOfParameters data pairs must have been added before invoking this method. If this method is invoked before a model
                can be estimated, :code:`Double,NaN` is returned.
        
        
            Returns:
                sum of squared errors associated with the regression model
        
        
        """
        ...
    def getMeanSquareError(self) -> float:
        """
        
            Returns the sum of squared errors divided by the degrees of freedom, usually abbreviated MSE.
        
            If there are fewer than **numberOfParameters + 1** data pairs in the model, or if there is no variation in :code:`x`,
            this returns :code:`Double.NaN`.
        
            Returns:
                sum of squared deviations of y values
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of observations added to the regression model.
        
            Returns:
                Number of observations, -1 if an error condition prevents estimation
        
        
        """
        ...
    def getNumberOfParameters(self) -> int:
        """
        
            Returns the number of parameters estimated in the model.
        
            This is the maximum number of regressors, some techniques may drop redundant parameters
        
            Returns:
                number of regressors, -1 if not estimated
        
        
        """
        ...
    def getParameterEstimate(self, int: int) -> float: ...
    def getParameterEstimates(self) -> typing.List[float]:
        """
        
            Returns a copy of the regression parameters estimates.
        
            The parameter estimates are returned in the natural order of the data.
        
            A redundant regressor will have its redundancy flag set, as will a parameter estimate equal to :code:`Double.NaN`.
        
            Returns:
                array of parameter estimates, null if no estimation occurred
        
        
        """
        ...
    def getRSquared(self) -> float:
        """
        
            Returns the ` coefficient of multiple determination <http://www.xycoon.com/coefficient1.htm>`, usually denoted r-square.
        
            **Preconditions**:
        
              - At least numberOfParameters observations (with at least numberOfParameters different x values) must have been added
                before invoking this method. If this method is invoked before a model can be estimated, :code:`Double,NaN` is returned.
        
        
            Returns:
                r-square, a double in the interval [0, 1]
        
        
        """
        ...
    def getRegressionSumSquares(self) -> float:
        """
        
            Returns the sum of squared deviations of the predicted y values about their mean (which equals the mean of y).
        
            This is usually abbreviated SSR or SSM. It is defined as SSM `here <http://www.xycoon.com/SumOfSquares.htm>`
        
            **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double.NaN` is returned.
        
        
            Returns:
                sum of squared deviations of predicted y values
        
        
        """
        ...
    def getStdErrorOfEstimate(self, int: int) -> float: ...
    def getStdErrorOfEstimates(self) -> typing.List[float]:
        """
        
            Returns the `standard error of the parameter estimates <http://www.xycoon.com/standerrorb(1).htm>`, usually denoted s(b
            :sub:`i` ).
        
            If there are problems with an ill conditioned design matrix then the regressor which is redundant will be assigned
            :code:`Double.NaN`.
        
            Returns:
                an array standard errors associated with parameters estimates, null if no estimation occurred
        
        
        """
        ...
    def getTotalSumSquares(self) -> float:
        """
        
            Returns the sum of squared deviations of the y values about their mean.
        
            This is defined as SSTO `here <http://www.xycoon.com/SumOfSquares.htm>`.
        
            If :code:`n < 2`, this returns :code:`Double.NaN`.
        
            Returns:
                sum of squared deviations of y values
        
        
        """
        ...
    def hasIntercept(self) -> bool:
        """
            Returns true if the regression model has been computed including an intercept. In this case, the coefficient of the
            intercept is the first element of the :meth:`~org.hipparchus.stat.regression.RegressionResults.getParameterEstimates`.
        
            Returns:
                true if the model has an intercept term
        
        
        """
        ...

class UpdatingMultipleLinearRegression:
    """
    public interface UpdatingMultipleLinearRegression
    
        An interface for regression models allowing for dynamic updating of the data. That is, the entire data set need not be
        loaded into memory. As observations become available, they can be added to the regression model and an updated estimate
        regression statistics can be calculated.
    """
    def addObservation(self, doubleArray: typing.List[float], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> None: ...
    def clear(self) -> None:
        """
            Clears internal buffers and resets the regression model. This means all data and derived values are initialized
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of observations added to the regression model.
        
            Returns:
                Number of observations
        
        
        """
        ...
    def hasIntercept(self) -> bool:
        """
            Returns true if a constant has been included false otherwise.
        
            Returns:
                true if constant exists, false otherwise
        
        
        """
        ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.List[int]) -> RegressionResults: ...

class AbstractMultipleLinearRegression(MultipleLinearRegression):
    def __init__(self): ...
    def estimateErrorVariance(self) -> float: ...
    def estimateRegressandVariance(self) -> float: ...
    def estimateRegressionParameters(self) -> typing.List[float]: ...
    def estimateRegressionParametersStandardErrors(self) -> typing.List[float]: ...
    def estimateRegressionParametersVariance(self) -> typing.List[typing.List[float]]: ...
    def estimateRegressionStandardError(self) -> float: ...
    def estimateResiduals(self) -> typing.List[float]: ...
    def isNoIntercept(self) -> bool: ...
    def newSampleData(self, doubleArray: typing.List[float], int: int, int2: int) -> None: ...
    def setNoIntercept(self, boolean: bool) -> None: ...

class MillerUpdatingRegression(UpdatingMultipleLinearRegression):
    """
    public class MillerUpdatingRegression extends Object implements :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
    
        This class is a concrete implementation of the :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        interface.
    
        The algorithm is described in:
    
        .. code-block: java
        
         Algorithm AS 274: Least Squares Routines to Supplement Those of Gentleman
         Author(s): Alan J. Miller
         Source: Journal of the Royal Statistical Society.
         Series C (Applied Statistics), Vol. 41, No. 2
         (1992), pp. 458-478
         Published by: Blackwell Publishing for the Royal Statistical Society
         Stable URL: http://www.jstor.org/stable/2347583 
    
        This method for multiple regression forms the solution to the OLS problem by updating the QR decomposition as described
        by Gentleman.
    """
    @typing.overload
    def __init__(self, int: int, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, boolean: bool, double: float): ...
    def addObservation(self, doubleArray: typing.List[float], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> None: ...
    def clear(self) -> None:
        """
            As the name suggests, clear wipes the internals and reorders everything in the canonical order.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.clear`Â in
                interfaceÂ :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
        
        """
        ...
    def getDiagonalOfHatMatrix(self, doubleArray: typing.List[float]) -> float:
        """
            Gets the diagonal of the Hat matrix also known as the leverage matrix.
        
            Parameters:
                row_data (double[]): returns the diagonal of the hat matrix for this observation
        
            Returns:
                the diagonal element of the hatmatrix
        
        
        """
        ...
    def getN(self) -> int:
        """
            Gets the number of observations added to the regression model.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.getN`Â in
                interfaceÂ :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
            Returns:
                number of observations
        
        
        """
        ...
    def getOrderOfRegressors(self) -> typing.List[int]:
        """
            Gets the order of the regressors, useful if some type of reordering has been called. Calling regress with int[]{} args
            will trigger a reordering.
        
            Returns:
                int[] with the current order of the regressors
        
        
        """
        ...
    def getPartialCorrelations(self, int: int) -> typing.List[float]:
        """
            In the original algorithm only the partial correlations of the regressors is returned to the user. In this
            implementation, we have
        
            .. code-block: java
            
             corr =
             {
               corrxx - lower triangular
               corrxy - bottom row of the matrix
             }
             Replaces subroutines PCORR and COR of:
             ALGORITHM AS274  APPL. STATIST. (1992) VOL.41, NO. 2 
        
            Calculate partial correlations after the variables in rows 1, 2, ..., IN have been forced into the regression. If IN =
            1, and the first row of R represents a constant in the model, then the usual simple correlations are returned.
        
            If IN = 0, the value returned in array CORMAT for the correlation of variables Xi & Xj is:
        
            .. code-block: java
            
             sum ( Xi.Xj ) / Sqrt ( sum (Xi^2) . sum (Xj^2) )
        
            On return, array CORMAT contains the upper triangle of the matrix of partial correlations stored by rows, excluding the
            1's on the diagonal. e.g. if IN = 2, the consecutive elements returned are: (3,4) (3,5) ... (3,ncol), (4,5) (4,6) ...
            (4,ncol), etc. Array YCORR stores the partial correlations with the Y-variable starting with YCORR(IN+1) = partial
            correlation with the variable in position (IN+1).
        
            Parameters:
                in (int): how many of the regressors to include (either in canonical order, or in the current reordered state)
        
            Returns:
                an array with the partial correlations of the remainder of regressors with each other and the regressand, in lower
                triangular form
        
        
        """
        ...
    def hasIntercept(self) -> bool:
        """
            A getter method which determines whether a constant is included.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.hasIntercept`Â in
                interfaceÂ :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
            Returns:
                true regression has an intercept, false no intercept
        
        
        """
        ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, int: int) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.List[int]) -> RegressionResults: ...

class SimpleRegression(java.io.Serializable, UpdatingMultipleLinearRegression):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def addData(self, double: float, double2: float) -> None: ...
    @typing.overload
    def addData(self, doubleArray: typing.List[typing.List[float]]) -> None: ...
    def addObservation(self, doubleArray: typing.List[float], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> None: ...
    def append(self, simpleRegression: 'SimpleRegression') -> None: ...
    def clear(self) -> None: ...
    def getIntercept(self) -> float: ...
    def getInterceptStdErr(self) -> float: ...
    def getMeanSquareError(self) -> float: ...
    def getN(self) -> int: ...
    def getR(self) -> float: ...
    def getRSquare(self) -> float: ...
    def getRegressionSumSquares(self) -> float: ...
    def getSignificance(self) -> float: ...
    def getSlope(self) -> float: ...
    @typing.overload
    def getSlopeConfidenceInterval(self) -> float: ...
    @typing.overload
    def getSlopeConfidenceInterval(self, double: float) -> float: ...
    def getSlopeStdErr(self) -> float: ...
    def getSumOfCrossProducts(self) -> float: ...
    def getSumSquaredErrors(self) -> float: ...
    def getTotalSumSquares(self) -> float: ...
    def getXSumSquares(self) -> float: ...
    def hasIntercept(self) -> bool: ...
    def predict(self, double: float) -> float: ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.List[int]) -> RegressionResults: ...
    @typing.overload
    def removeData(self, double: float, double2: float) -> None: ...
    @typing.overload
    def removeData(self, doubleArray: typing.List[typing.List[float]]) -> None: ...

class GLSMultipleLinearRegression(AbstractMultipleLinearRegression):
    """
    public class GLSMultipleLinearRegression extends :class:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression`
    
        The GLS implementation of multiple linear regression. GLS assumes a general covariance matrix Omega of the error
    
        .. code-block: java
        
         u ~ N(0, Omega)
         
        Estimated by GLS,
    
        .. code-block: java
        
         b=(X' Omega^-1 X)^-1X'Omega^-1 y
         
        whose variance is
    
        .. code-block: java
        
         Var(b)=(X' Omega^-1 X)^-1
    """
    def __init__(self): ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], int: int, int2: int) -> None:
        """
            Replace sample data, overriding any previous sample.
        
            Parameters:
                y (double[]): y values of the sample
                x (double[][]): x values of the sample
                covariance (double[][]): array representing the covariance matrix
        
        
        """
        ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[typing.List[float]]) -> None: ...

class OLSMultipleLinearRegression(AbstractMultipleLinearRegression):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    def calculateAdjustedRSquared(self) -> float: ...
    def calculateHat(self) -> org.hipparchus.linear.RealMatrix: ...
    def calculateRSquared(self) -> float: ...
    def calculateResidualSumOfSquares(self) -> float: ...
    def calculateTotalSumOfSquares(self) -> float: ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]]) -> None: ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], int: int, int2: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.regression")``.

    AbstractMultipleLinearRegression: typing.Type[AbstractMultipleLinearRegression]
    GLSMultipleLinearRegression: typing.Type[GLSMultipleLinearRegression]
    MillerUpdatingRegression: typing.Type[MillerUpdatingRegression]
    MultipleLinearRegression: typing.Type[MultipleLinearRegression]
    OLSMultipleLinearRegression: typing.Type[OLSMultipleLinearRegression]
    RegressionResults: typing.Type[RegressionResults]
    SimpleRegression: typing.Type[SimpleRegression]
    UpdatingMultipleLinearRegression: typing.Type[UpdatingMultipleLinearRegression]
