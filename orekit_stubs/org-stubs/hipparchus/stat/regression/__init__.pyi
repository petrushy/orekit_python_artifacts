
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jpype
import org.hipparchus.linear
import typing



class MultipleLinearRegression:
    """
    public interfaceMultipleLinearRegression
    
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
    def estimateRegressionParameters(self) -> typing.MutableSequence[float]:
        """
            Estimates the regression parameters b.
        
            Returns:
                The [k,1] array representing b
        
        
        """
        ...
    def estimateRegressionParametersStandardErrors(self) -> typing.MutableSequence[float]:
        """
            Returns the standard errors of the regression parameters.
        
            Returns:
                standard errors of estimated regression parameters
        
        
        """
        ...
    def estimateRegressionParametersVariance(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Estimates the variance of the regression parameters, ie Var(b).
        
            Returns:
                The [k,k] array representing the variance of b
        
        
        """
        ...
    def estimateResiduals(self) -> typing.MutableSequence[float]:
        """
            Estimates the residuals, ie u = y - X*b.
        
            Returns:
                The [n,1] array representing the residuals
        
        
        """
        ...

class RegressionResults(java.io.Serializable):
    """
    public classRegressionResults extends :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Results of a Multiple Linear Regression model fit.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool, long: int, int: int, double3: float, double4: float, double5: float, boolean2: bool, boolean3: bool): ...
    def getAdjustedRSquared(self) -> float:
        """
        
            Returns the adjusted R-squared statistic, defined by the formula \( R_\mathrm{adj}^2 = 1 - \frac{\mathrm{SSR} (n -
            1)}{\mathrm{SSTO} (n - p)} \) where SSR is the sum of squared residuals}, SSTO is the total sum of squares}, n is the
            number of observations and p is the number of parameters estimated (including the intercept).
        
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
    def getParameterEstimates(self) -> typing.MutableSequence[float]:
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
    def getStdErrorOfEstimates(self) -> typing.MutableSequence[float]:
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
    public interfaceUpdatingMultipleLinearRegression
    
        An interface for regression models allowing for dynamic updating of the data. That is, the entire data set need not be
        loaded into memory. As observations become available, they can be added to the regression model and an updated estimate
        regression statistics can be calculated.
    """
    def addObservation(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
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
    def regress(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> RegressionResults: ...

class AbstractMultipleLinearRegression(MultipleLinearRegression):
    """
    public abstract classAbstractMultipleLinearRegression extends :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.regression.MultipleLinearRegression`
    
        Abstract base class for implementations of MultipleLinearRegression.
    """
    def estimateErrorVariance(self) -> float:
        """
            Estimates the variance of the error.
        
            Returns:
                estimate of the error variance
        
        
        """
        ...
    def estimateRegressandVariance(self) -> float:
        """
            Returns the variance of the regressand, ie Var(y).
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.MultipleLinearRegression.estimateRegressandVariance` in
                interface :class:`~org.hipparchus.stat.regression.MultipleLinearRegression`
        
            Returns:
                The double representing the variance of y
        
        
        """
        ...
    def estimateRegressionParameters(self) -> typing.MutableSequence[float]:
        """
            Estimates the regression parameters b.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.MultipleLinearRegression.estimateRegressionParameters` in
                interface :class:`~org.hipparchus.stat.regression.MultipleLinearRegression`
        
            Returns:
                The [k,1] array representing b
        
        
        """
        ...
    def estimateRegressionParametersStandardErrors(self) -> typing.MutableSequence[float]:
        """
            Returns the standard errors of the regression parameters.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.MultipleLinearRegression.estimateRegressionParametersStandardErrors` in
                interface :class:`~org.hipparchus.stat.regression.MultipleLinearRegression`
        
            Returns:
                standard errors of estimated regression parameters
        
        
        """
        ...
    def estimateRegressionParametersVariance(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Estimates the variance of the regression parameters, ie Var(b).
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.MultipleLinearRegression.estimateRegressionParametersVariance` in
                interface :class:`~org.hipparchus.stat.regression.MultipleLinearRegression`
        
            Returns:
                The [k,k] array representing the variance of b
        
        
        """
        ...
    def estimateRegressionStandardError(self) -> float:
        """
            Estimates the standard error of the regression.
        
            Returns:
                regression standard error
        
        
        """
        ...
    def estimateResiduals(self) -> typing.MutableSequence[float]:
        """
            Estimates the residuals, ie u = y - X*b.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.MultipleLinearRegression.estimateResiduals` in
                interface :class:`~org.hipparchus.stat.regression.MultipleLinearRegression`
        
            Returns:
                The [n,1] array representing the residuals
        
        
        """
        ...
    def isNoIntercept(self) -> bool:
        """
            Chekc if the model has no intercept term.
        
            Returns:
                true if the model has no intercept term; false otherwise
        
        
        """
        ...
    def newSampleData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> None:
        """
        
            Loads model x and y sample data from a flat input array, overriding any previous sample.
        
            Assumes that rows are concatenated with y values first in each row. For example, an input :code:`data` array containing
            the sequence of values (1, 2, 3, 4, 5, 6, 7, 8, 9) with :code:`nobs = 3` and :code:`nvars = 2` creates a regression
            dataset with two independent variables, as below:
        
            .. code-block: java
            
               y   x[0]  x[1]
               --------------
               1     2     3
               4     5     6
               7     8     9
             
        
            Note that there is no need to add an initial unitary column (column of 1's) when specifying a model including an
            intercept term. If :meth:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression.isNoIntercept` is
            :code:`true`, the X matrix will be created without an initial column of "1"s; otherwise this column will be added.
        
            Throws IllegalArgumentException if any of the following preconditions fail:
        
              - :code:`data` cannot be null
              - :code:`data.length = nobs * (nvars + 1)`
              - :code:`nobs > nvars`
        
        
            Parameters:
                data (double[]): input data array
                nobs (int): number of observations (rows)
                nvars (int): number of independent variables (columns, not counting y)
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if the data array is null
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if the length of the data array is not equal to :code:`nobs * (nvars + 1)`
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if :code:`nobs` is less than :code:`nvars + 1`
        
        
        """
        ...
    def setNoIntercept(self, boolean: bool) -> None:
        """
            Set intercept flag.
        
            Parameters:
                noIntercept (boolean): true means the model is to be estimated without an intercept term
        
        
        """
        ...

class MillerUpdatingRegression(UpdatingMultipleLinearRegression):
    """
    public classMillerUpdatingRegression extends :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
    
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
         Stable URL: :class:`~org.hipparchus.stat.regression.https:.www.jstor.org.stable.2347583` 
    
        This method for multiple regression forms the solution to the OLS problem by updating the QR decomposition as described
        by Gentleman.
    """
    @typing.overload
    def __init__(self, int: int, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, boolean: bool, double: float): ...
    def addObservation(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def clear(self) -> None:
        """
            As the name suggests, clear wipes the internals and reorders everything in the canonical order.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.clear` in
                interface :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
        
        """
        ...
    def getDiagonalOfHatMatrix(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
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
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.getN` in
                interface :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
            Returns:
                number of observations
        
        
        """
        ...
    def getOrderOfRegressors(self) -> typing.MutableSequence[int]:
        """
            Gets the order of the regressors, useful if some type of reordering has been called. Calling regress with int[]{} args
            will trigger a reordering.
        
            Returns:
                int[] with the current order of the regressors
        
        
        """
        ...
    def getPartialCorrelations(self, int: int) -> typing.MutableSequence[float]:
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
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.hasIntercept` in
                interface :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
            Returns:
                true regression has an intercept, false no intercept
        
        
        """
        ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, int: int) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> RegressionResults: ...

class SimpleRegression(java.io.Serializable, UpdatingMultipleLinearRegression):
    """
    public classSimpleRegression extends :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`, :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
    
        Estimates an ordinary least squares regression model with one independent variable.
    
        :code:`y = intercept + slope * x`
    
        Standard errors for :code:`intercept` and :code:`slope` are available as well as ANOVA, r-square and Pearson's r
        statistics.
    
        Observations (x,y pairs) can be added to the model one at a time or they can be provided in a 2-dimensional array. The
        observations are not stored in memory, so there is no limit to the number of observations that can be added to the
        model.
    
        * **Usage Notes**:
    
          - When there are fewer than two observations in the model, or when there is no variation in the x values (i.e. all x
            values are the same) all statistics return :code:`NaN`. At least two observations with different x coordinates are
            required to estimate a bivariate regression model.
          - Getters for the statistics always compute values based on the current set of observations -- i.e., you can get
            statistics, then add more data and get updated statistics without using a new instance. There is no "compute" method
            that updates all statistics. Each of the getters performs the necessary computations to return the requested statistic.
          - The intercept term may be suppressed by passing :code:`false` to the
            :meth:`~org.hipparchus.stat.regression.SimpleRegression.%3Cinit%3E` constructor. When the :code:`hasIntercept` property
            is false, the model is estimated without a constant term and
            :meth:`~org.hipparchus.stat.regression.SimpleRegression.getIntercept` returns :code:`0`.
    
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def addData(self, double: float, double2: float) -> None:
        """
            Adds the observation (x,y) to the regression data set.
        
            Uses updating formulas for means and sums of squares defined in "Algorithms for Computing the Sample Variance: Analysis
            and Recommendations", Chan, T.F., Golub, G.H., and LeVeque, R.J. 1983, American Statistician, vol. 37, pp. 242-247,
            referenced in Weisberg, S. "Applied Linear Regression". 2nd Ed. 1985.
        
            Parameters:
                x (double): independent variable value
                y (double): dependent variable value
        
        public void addData(double[][] data) throws :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`
        
            Adds the observations represented by the elements in :code:`data`.
        
            :code:`(data[0][0],data[0][1])` will be the first observation, then :code:`(data[1][0],data[1][1])`, etc.
        
            This method does not replace data that has already been added. The observations represented by :code:`data` are added to
            the existing dataset.
        
            To replace all data, use :code:`clear()` before adding the new data.
        
            Parameters:
                data (double[][]): array of observations to be added
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if the length of :code:`data[i]` is not greater than or equal to 2
        
        
        """
        ...
    @typing.overload
    def addData(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...
    def addObservation(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def append(self, simpleRegression: 'SimpleRegression') -> None:
        """
            Appends data from another regression calculation to this one.
        
            The mean update formulae are based on a paper written by Philippe Pébay: ` Formulas for Robust, One-Pass Parallel
            Computation of Covariances and Arbitrary-Order Statistical Moments
            <http://prod.sandia.gov/techlib/access-control.cgi/2008/086212.pdf>`, 2008, Technical Report SAND2008-6212, Sandia
            National Laboratories.
        
            Parameters:
                reg (:class:`~org.hipparchus.stat.regression.SimpleRegression`): model to append data from
        
        
        """
        ...
    def clear(self) -> None:
        """
            Clears all data from the model.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.clear` in
                interface :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
        
        """
        ...
    def getIntercept(self) -> float:
        """
            Returns the intercept of the estimated regression line, if
            :meth:`~org.hipparchus.stat.regression.SimpleRegression.hasIntercept` is true; otherwise 0.
        
            The least squares estimate of the intercept is computed using the `normal equations
            <http://www.xycoon.com/estimation4.htm>`. The intercept is sometimes denoted b0.
        
            **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double,NaN` is returned.
        
        
            Returns:
                the intercept of the regression line if the model includes an intercept; 0 otherwise
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.regression.SimpleRegression.%3Cinit%3E`
        
        
        
        """
        ...
    def getInterceptStdErr(self) -> float:
        """
            Returns the ` standard error of the intercept estimate <http://www.xycoon.com/standarderrorb0.htm>`, usually denoted
            s(b0).
        
            If there are fewer that **three** observations in the model, or if there is no variation in x, this returns
            :code:`Double.NaN`.
            Additionally, a :code:`Double.NaN` is returned when the intercept is constrained to be zero
        
            Returns:
                standard error associated with intercept estimate
        
        
        """
        ...
    def getMeanSquareError(self) -> float:
        """
            Returns the sum of squared errors divided by the degrees of freedom, usually abbreviated MSE.
        
            If there are fewer than **three** data pairs in the model, or if there is no variation in :code:`x`, this returns
            :code:`Double.NaN`.
        
            Returns:
                sum of squared deviations of y values
        
        
        """
        ...
    def getN(self) -> int:
        """
            Returns the number of observations that have been added to the model.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.getN` in
                interface :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
            Returns:
                n number of observations that have been added.
        
        
        """
        ...
    def getR(self) -> float:
        """
            Returns ` Pearson's product moment correlation coefficient <http://mathworld.wolfram.com/CorrelationCoefficient.html>`,
            usually denoted r.
        
            * **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double,NaN` is returned.
        
        
            Returns:
                Pearson's r
        
        
        """
        ...
    def getRSquare(self) -> float:
        """
            Returns the ` coefficient of determination <http://www.xycoon.com/coefficient1.htm>`, usually denoted r-square.
        
            * **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double,NaN` is returned.
        
        
            Returns:
                r-square
        
        
        """
        ...
    def getRegressionSumSquares(self) -> float:
        """
            Returns the sum of squared deviations of the predicted y values about their mean (which equals the mean of y).
        
            This is usually abbreviated SSR or SSM. It is defined as SSM `here <http://www.xycoon.com/SumOfSquares.htm>`
        
            * **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double.NaN` is returned.
        
        
            Returns:
                sum of squared deviations of predicted y values
        
        
        """
        ...
    def getSignificance(self) -> float:
        """
            Returns the significance level of the slope (equiv) correlation.
        
            Specifically, the returned value is the smallest :code:`alpha` such that the slope confidence interval with significance
            level equal to :code:`alpha` does not include :code:`0`. On regression output, this is often denoted :code:`Prob(|t| >
            0)`
        
            **Usage Note**:
        
        
            The validity of this statistic depends on the assumption that the observations included in the model are drawn from a `
            Bivariate Normal Distribution <http://mathworld.wolfram.com/BivariateNormalDistribution.html>`.
        
            If there are fewer that **three** observations in the model, or if there is no variation in x, this returns
            :code:`Double.NaN`.
        
            Returns:
                significance level for slope/correlation
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if the significance level can not be computed.
        
        
        """
        ...
    def getSlope(self) -> float:
        """
            Returns the slope of the estimated regression line.
        
            The least squares estimate of the slope is computed using the `normal equations
            <http://www.xycoon.com/estimation4.htm>`. The slope is sometimes denoted b1.
        
            * **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double.NaN` is returned.
        
        
            Returns:
                the slope of the regression line
        
        
        """
        ...
    @typing.overload
    def getSlopeConfidenceInterval(self) -> float: ...
    @typing.overload
    def getSlopeConfidenceInterval(self, double: float) -> float: ...
    def getSlopeStdErr(self) -> float:
        """
            Returns the `standard error of the slope estimate <http://www.xycoon.com/standerrorb(1).htm>`, usually denoted s(b1).
        
            If there are fewer that **three** data pairs in the model, or if there is no variation in x, this returns
            :code:`Double.NaN`.
        
            Returns:
                standard error associated with slope estimate
        
        
        """
        ...
    def getSumOfCrossProducts(self) -> float:
        """
            Returns the sum of crossproducts, x :sub:`i` *y :sub:`i` .
        
            Returns:
                sum of cross products
        
        
        """
        ...
    def getSumSquaredErrors(self) -> float:
        """
            Returns the ` sum of squared errors <http://www.xycoon.com/SumOfSquares.htm>` (SSE) associated with the regression
            model.
        
            The sum is computed using the computational formula
        
            :code:`SSE = SYY - (SXY * SXY / SXX)`
        
            where :code:`SYY` is the sum of the squared deviations of the y values about their mean, :code:`SXX` is similarly
            defined and :code:`SXY` is the sum of the products of x and y mean deviations.
        
            The sums are accumulated using the updating algorithm referenced in
            :meth:`~org.hipparchus.stat.regression.SimpleRegression.addData`.
        
            The return value is constrained to be non-negative - i.e., if due to rounding errors the computational formula returns a
            negative result, 0 is returned.
        
            * **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double,NaN` is returned.
        
        
            Returns:
                sum of squared errors associated with the regression model
        
        
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
    def getXSumSquares(self) -> float:
        """
            Returns the sum of squared deviations of the x values about their mean.
        
            If :code:`n < 2`, this returns :code:`Double.NaN`.
        
            Returns:
                sum of squared deviations of x values
        
        
        """
        ...
    def hasIntercept(self) -> bool:
        """
            Returns true if the model includes an intercept term.
        
            Specified by:
                :meth:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression.hasIntercept` in
                interface :class:`~org.hipparchus.stat.regression.UpdatingMultipleLinearRegression`
        
            Returns:
                true if the regression includes an intercept; false otherwise
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.regression.SimpleRegression.%3Cinit%3E`
        
        
        
        """
        ...
    def predict(self, double: float) -> float:
        """
            Returns the "predicted" :code:`y` value associated with the supplied :code:`x` value, based on the data that has been
            added to the model when this method is activated.
        
            :code:`predict(x) = intercept + slope * x`
        
            * **Preconditions**:
        
              - At least two observations (with at least two different x values) must have been added before invoking this method. If
                this method is invoked before a model can be estimated, :code:`Double,NaN` is returned.
        
        
            Parameters:
                x (double): input :code:`x` value
        
            Returns:
                predicted :code:`y` value
        
        
        """
        ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> RegressionResults: ...
    @typing.overload
    def removeData(self, double: float, double2: float) -> None:
        """
            Removes the observation (x,y) from the regression data set.
        
            Mirrors the addData method. This method permits the use of SimpleRegression instances in streaming mode where the
            regression is applied to a sliding "window" of observations, however the caller is responsible for maintaining the set
            of observations in the window.
            The method has no effect if there are no points of data (i.e. n=0)
        
            Parameters:
                x (double): independent variable value
                y (double): dependent variable value
        
        """
        ...
    @typing.overload
    def removeData(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Removes observations represented by the elements in :code:`data`.
        
            If the array is larger than the current n, only the first n elements are processed. This method permits the use of
            SimpleRegression instances in streaming mode where the regression is applied to a sliding "window" of observations,
            however the caller is responsible for maintaining the set of observations in the window.
        
            To remove all data, use :code:`clear()`.
        
            Parameters:
                data (double[][]): array of observations to be removed
        
        
        """
        ...

class GLSMultipleLinearRegression(AbstractMultipleLinearRegression):
    """
    public classGLSMultipleLinearRegression extends :class:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression`
    
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
    def newSampleData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> None:
        """
            Replace sample data, overriding any previous sample.
        
            Parameters:
                y (double[]): y values of the sample
                x (double[][]): x values of the sample
                covariance (double[][]): array representing the covariance matrix
        
        
        """
        ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...

class OLSMultipleLinearRegression(AbstractMultipleLinearRegression):
    """
    public classOLSMultipleLinearRegression extends :class:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression`
    
    
        Implements ordinary least squares (OLS) to estimate the parameters of a multiple linear regression model.
    
        The regression coefficients, :code:`b`, satisfy the normal equations:
    
        .. code-block: java
        
         X :sup:`T`  X b = X :sup:`T`  y 
    
        To solve the normal equations, this implementation uses QR decomposition of the :code:`X` matrix. (See
        :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus` for details on the decomposition
        algorithm.) The :code:`X` matrix, also known as the *design matrix,* has rows corresponding to sample observations and
        columns corresponding to independent variables. When the model is estimated using an intercept term (i.e. when
        :meth:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression.isNoIntercept` is false as it is by default),
        the :code:`X` matrix includes an initial column identically equal to 1. We solve the normal equations as follows:
    
        .. code-block: java
        
         X :sup:`T` X b = X :sup:`T`  y
         (QR) :sup:`T`  (QR) b = (QR) :sup:`T` y
         R :sup:`T`  (Q :sup:`T` Q) R b = R :sup:`T`  Q :sup:`T`  y
         R :sup:`T`  R b = R :sup:`T`  Q :sup:`T`  y
         (R :sup:`T` ) :sup:`-1`  R :sup:`T`  R b = (R :sup:`T` ) :sup:`-1`  R :sup:`T`  Q :sup:`T`  y
         R b = Q :sup:`T`  y 
    
        Given :code:`Q` and :code:`R`, the last equation is solved by back-substitution.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    def calculateAdjustedRSquared(self) -> float:
        """
        
            Returns the adjusted R-squared statistic, defined by the formula \(R_\mathrm{adj}^2 = 1 - \frac{\mathrm{SSR} (n -
            1)}{\mathrm{SSTO} (n - p)}\) where SSR is the
            :meth:`~org.hipparchus.stat.regression.OLSMultipleLinearRegression.calculateResidualSumOfSquares`, SSTO is the
            :meth:`~org.hipparchus.stat.regression.OLSMultipleLinearRegression.calculateTotalSumOfSquares`, n is the number of
            observations and p is the number of parameters estimated (including the intercept).
        
            If the regression is estimated without an intercept term, what is returned is
        
            .. code-block: java
            
             :meth:`~org.hipparchus.stat.regression.OLSMultipleLinearRegression.calculateRSquared`
             
        
            If there is no variance in y, i.e., SSTO = 0, NaN is returned.
        
            Returns:
                adjusted R-Squared statistic
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the sample has not been set
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if the design matrix is singular
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression.isNoIntercept`
        
        
        
        """
        ...
    def calculateHat(self) -> org.hipparchus.linear.RealMatrix:
        """
        
            Compute the "hat" matrix.
        
            The hat matrix is defined in terms of the design matrix X by X(X :sup:`T` X) :sup:`-1` X :sup:`T`
        
            The implementation here uses the QR decomposition to compute the hat matrix as Q I :sub:`p` Q :sup:`T` where I :sub:`p`
            is the p-dimensional identity matrix augmented by 0's. This computational formula is from "The Hat Matrix in Regression
            and ANOVA", David C. Hoaglin and Roy E. Welsch, *The American Statistician*, Vol. 32, No. 1 (Feb., 1978), pp. 17-22.
        
            Data for the model must have been successfully loaded using one of the :code:`newSampleData` methods before invoking
            this method; otherwise a :code:`NullPointerException` will be thrown.
        
            Returns:
                the hat matrix
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: unless method :code:`newSampleData` has been called beforehand.
        
        
        """
        ...
    def calculateRSquared(self) -> float:
        """
            Returns the R-Squared statistic, defined by the formula \(R^2 = 1 - \frac{\mathrm{SSR}}{\mathrm{SSTO}}\) where SSR is
            the :meth:`~org.hipparchus.stat.regression.OLSMultipleLinearRegression.calculateResidualSumOfSquares` and SSTO is the
            :meth:`~org.hipparchus.stat.regression.OLSMultipleLinearRegression.calculateTotalSumOfSquares`
        
            If there is no variance in y, i.e., SSTO = 0, NaN is returned.
        
            Returns:
                R-square statistic
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the sample has not been set
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if the design matrix is singular
        
        
        """
        ...
    def calculateResidualSumOfSquares(self) -> float:
        """
            Returns the sum of squared residuals.
        
            Returns:
                residual sum of squares
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.www.hipparchus.org.hipparchus`: if the design matrix is singular
                :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the data for the model have not been loaded
        
        
        """
        ...
    def calculateTotalSumOfSquares(self) -> float:
        """
        
            Returns the sum of squared deviations of Y from its mean.
        
            If the model has no intercept term, :code:`0` is used for the mean of Y - i.e., what is returned is the sum of the
            squared Y values.
        
            The value returned by this method is the SSTO value used in the
            :meth:`~org.hipparchus.stat.regression.OLSMultipleLinearRegression.calculateRSquared` computation.
        
            Returns:
                SSTO - the total sum of squares
        
            Raises:
                :class:`~org.hipparchus.stat.regression.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the sample has not been set
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression.isNoIntercept`
        
        
        
        """
        ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
        
            Loads model x and y sample data from a flat input array, overriding any previous sample.
        
            Assumes that rows are concatenated with y values first in each row. For example, an input :code:`data` array containing
            the sequence of values (1, 2, 3, 4, 5, 6, 7, 8, 9) with :code:`nobs = 3` and :code:`nvars = 2` creates a regression
            dataset with two independent variables, as below:
        
            .. code-block: java
            
               y   x[0]  x[1]
               --------------
               1     2     3
               4     5     6
               7     8     9
             
        
            Note that there is no need to add an initial unitary column (column of 1's) when specifying a model including an
            intercept term. If :meth:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression.isNoIntercept` is
            :code:`true`, the X matrix will be created without an initial column of "1"s; otherwise this column will be added.
        
            Throws IllegalArgumentException if any of the following preconditions fail:
        
              - :code:`data` cannot be null
              - :code:`data.length = nobs * (nvars + 1)`
              - :code:`nobs > nvars`
        
        
            This implementation computes and caches the QR decomposition of the X matrix.
        
            Overrides:
                :meth:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression.newSampleData` in
                class :class:`~org.hipparchus.stat.regression.AbstractMultipleLinearRegression`
        
            Parameters:
                data (double[]): input data array
                nobs (int): number of observations (rows)
                nvars (int): number of independent variables (columns, not counting y)
        
        
        """
        ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.regression")``.

    AbstractMultipleLinearRegression: typing.Type[AbstractMultipleLinearRegression]
    GLSMultipleLinearRegression: typing.Type[GLSMultipleLinearRegression]
    MillerUpdatingRegression: typing.Type[MillerUpdatingRegression]
    MultipleLinearRegression: typing.Type[MultipleLinearRegression]
    OLSMultipleLinearRegression: typing.Type[OLSMultipleLinearRegression]
    RegressionResults: typing.Type[RegressionResults]
    SimpleRegression: typing.Type[SimpleRegression]
    UpdatingMultipleLinearRegression: typing.Type[UpdatingMultipleLinearRegression]
