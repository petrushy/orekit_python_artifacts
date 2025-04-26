
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.util
import typing



class EvaluationRmsChecker(org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation']):
    """
    public classEvaluationRmsChecker extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.ConvergenceChecker`<:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`>
    
        Check if an optimization has converged based on the change in computed RMS.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def converged(self, int: int, evaluation: 'LeastSquaresProblem.Evaluation', evaluation2: 'LeastSquaresProblem.Evaluation') -> bool:
        """
            Check if the optimization algorithm has converged.
        
            Specified by:
                :meth:`~org.hipparchus.optim.ConvergenceChecker.converged` in
                interface :class:`~org.hipparchus.optim.ConvergenceChecker`
        
            Parameters:
                iteration (int): Current iteration.
                previous (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the algorithm is considered to have converged.
        
        
        """
        ...

class LeastSquaresBuilder:
    """
    public classLeastSquaresBuilder extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        A mutable builder for :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`s.
    
        Also see:
    
              - :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresFactory`
    """
    def __init__(self): ...
    def build(self) -> 'LeastSquaresProblem':
        """
            Construct a :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem` from the data in this
            builder.
        
            Returns:
                a new :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`.
        
        
        """
        ...
    def checker(self, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], typing.Callable[[int, 'LeastSquaresProblem.Evaluation', 'LeastSquaresProblem.Evaluation'], bool]]) -> 'LeastSquaresBuilder': ...
    def checkerPair(self, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointVectorValuePair], typing.Callable[[int, org.hipparchus.optim.PointVectorValuePair, org.hipparchus.optim.PointVectorValuePair], bool]]) -> 'LeastSquaresBuilder': ...
    def lazyEvaluation(self, boolean: bool) -> 'LeastSquaresBuilder':
        """
            Configure whether evaluation will be lazy or not.
        
            Parameters:
                newValue (boolean): Whether to perform lazy evaluation.
        
            Returns:
                this object.
        
        
        """
        ...
    def maxEvaluations(self, int: int) -> 'LeastSquaresBuilder':
        """
            Configure the max evaluations.
        
            Parameters:
                newMaxEvaluations (int): the maximum number of evaluations permitted.
        
            Returns:
                this
        
        
        """
        ...
    def maxIterations(self, int: int) -> 'LeastSquaresBuilder':
        """
            Configure the max iterations.
        
            Parameters:
                newMaxIterations (int): the maximum number of iterations permitted.
        
            Returns:
                this
        
        
        """
        ...
    @typing.overload
    def model(self, multivariateVectorFunction: typing.Union[org.hipparchus.analysis.MultivariateVectorFunction, typing.Callable], multivariateMatrixFunction: typing.Union[org.hipparchus.analysis.MultivariateMatrixFunction, typing.Callable]) -> 'LeastSquaresBuilder':
        """
            Configure the model function.
        
            Parameters:
                value (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the model function value
                jacobian (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the Jacobian of :code:`value`
        
            Returns:
                this
        
        """
        ...
    @typing.overload
    def model(self, multivariateJacobianFunction: typing.Union['MultivariateJacobianFunction', typing.Callable]) -> 'LeastSquaresBuilder':
        """
            Configure the model function.
        
            Parameters:
                newModel (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction`): the model function value and Jacobian
        
            Returns:
                this
        
        
        """
        ...
    def parameterValidator(self, parameterValidator: typing.Union['ParameterValidator', typing.Callable]) -> 'LeastSquaresBuilder':
        """
            Configure the validator of the model parameters.
        
            Parameters:
                newValidator (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.ParameterValidator`): Parameter validator.
        
            Returns:
                this object.
        
        
        """
        ...
    @typing.overload
    def start(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'LeastSquaresBuilder':
        """
            Configure the initial guess.
        
            Parameters:
                newStart (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the initial guess.
        
            Returns:
                this
        
            Configure the initial guess.
        
            Parameters:
                newStart (double[]): the initial guess.
        
            Returns:
                this
        
        
        """
        ...
    @typing.overload
    def start(self, realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresBuilder': ...
    @typing.overload
    def target(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'LeastSquaresBuilder':
        """
            Configure the observed data.
        
            Parameters:
                newTarget (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the observed data.
        
            Returns:
                this
        
            Configure the observed data.
        
            Parameters:
                newTarget (double[]): the observed data.
        
            Returns:
                this
        
        
        """
        ...
    @typing.overload
    def target(self, realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresBuilder': ...
    def weight(self, realMatrix: org.hipparchus.linear.RealMatrix) -> 'LeastSquaresBuilder':
        """
            Configure the weight matrix.
        
            Parameters:
                newWeight (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the weight matrix
        
            Returns:
                this
        
        
        """
        ...

class LeastSquaresFactory:
    """
    public classLeastSquaresFactory extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        A Factory for creating :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`s.
    """
    @staticmethod
    def countEvaluations(leastSquaresProblem: 'LeastSquaresProblem', incrementor: org.hipparchus.util.Incrementor) -> 'LeastSquaresProblem':
        """
            Count the evaluations of a particular problem. The :code:`counter` will be incremented every time
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.evaluate` is called on the *returned*
            problem.
        
            Parameters:
                problem (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the problem to track.
                counter (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the counter to increment.
        
            Returns:
                a least squares problem that tracks evaluations
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def create(multivariateVectorFunction: typing.Union[org.hipparchus.analysis.MultivariateVectorFunction, typing.Callable], multivariateMatrixFunction: typing.Union[org.hipparchus.analysis.MultivariateMatrixFunction, typing.Callable], doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], realMatrix: org.hipparchus.linear.RealMatrix, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], typing.Callable[[int, 'LeastSquaresProblem.Evaluation', 'LeastSquaresProblem.Evaluation'], bool]], int: int, int2: int) -> 'LeastSquaresProblem': ...
    @typing.overload
    @staticmethod
    def create(multivariateJacobianFunction: typing.Union['MultivariateJacobianFunction', typing.Callable], realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], typing.Callable[[int, 'LeastSquaresProblem.Evaluation', 'LeastSquaresProblem.Evaluation'], bool]], int: int, int2: int) -> 'LeastSquaresProblem': ...
    @typing.overload
    @staticmethod
    def create(multivariateJacobianFunction: typing.Union['MultivariateJacobianFunction', typing.Callable], realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], typing.Callable[[int, 'LeastSquaresProblem.Evaluation', 'LeastSquaresProblem.Evaluation'], bool]], int: int, int2: int, boolean: bool, parameterValidator: typing.Union['ParameterValidator', typing.Callable]) -> 'LeastSquaresProblem': ...
    @typing.overload
    @staticmethod
    def create(multivariateJacobianFunction: typing.Union['MultivariateJacobianFunction', typing.Callable], realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], typing.Callable[[int, 'LeastSquaresProblem.Evaluation', 'LeastSquaresProblem.Evaluation'], bool]], int: int, int2: int) -> 'LeastSquaresProblem': ...
    @staticmethod
    def evaluationChecker(convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointVectorValuePair], typing.Callable[[int, org.hipparchus.optim.PointVectorValuePair, org.hipparchus.optim.PointVectorValuePair], bool]]) -> org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation']: ...
    @staticmethod
    def model(multivariateVectorFunction: typing.Union[org.hipparchus.analysis.MultivariateVectorFunction, typing.Callable], multivariateMatrixFunction: typing.Union[org.hipparchus.analysis.MultivariateMatrixFunction, typing.Callable]) -> 'MultivariateJacobianFunction':
        """
            Combine a :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus` with a
            :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus` to produce a
            :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction`.
        
            Parameters:
                value (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the vector value function
                jacobian (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the Jacobian function
        
            Returns:
                a function that computes both at the same time
        
        
        """
        ...
    @staticmethod
    def weightDiagonal(leastSquaresProblem: 'LeastSquaresProblem', realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresProblem':
        """
            Apply a diagonal weight matrix to the :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`.
        
            Parameters:
                problem (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the unweighted problem
                weights (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the diagonal of the weight matrix
        
            Returns:
                a new :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem` with the weights applied. The
                original :code:`problem` is not modified.
        
        
        """
        ...
    @staticmethod
    def weightMatrix(leastSquaresProblem: 'LeastSquaresProblem', realMatrix: org.hipparchus.linear.RealMatrix) -> 'LeastSquaresProblem':
        """
            Apply a dense weight matrix to the :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`.
        
            Parameters:
                problem (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the unweighted problem
                weights (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the matrix of weights
        
            Returns:
                a new :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem` with the weights applied. The
                original :code:`problem` is not modified.
        
        
        """
        ...

class LeastSquaresProblem(org.hipparchus.optim.OptimizationProblem['LeastSquaresProblem.Evaluation']):
    """
    public interfaceLeastSquaresProblemextends :class:`~org.hipparchus.optim.OptimizationProblem`<:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`>
    
        The data necessary to define a non-linear least squares problem.
    
        Includes the observed values, computed model function, and convergence/divergence criteria. Weights are implicit in
        :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getResiduals` and
        :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getJacobian`.
    
        Instances are typically either created progressively using a
        :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresBuilder` or created at once using a
        :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresFactory`.
    
        Also see:
    
              - :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresBuilder`
              - :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresFactory`
              - :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresAdapter`
    """
    def evaluate(self, realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresProblem.Evaluation':
        """
            Evaluate the model at the specified point.
        
            Parameters:
                point (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the parameter values.
        
            Returns:
                the model's value and derivative at the given point.
        
            Raises:
                :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`: if the maximal number of evaluations (of the model vector function) is exceeded.
        
        
        """
        ...
    def getObservationSize(self) -> int:
        """
            Get the number of observations (rows in the Jacobian) in this problem.
        
            Returns:
                the number of scalar observations
        
        
        """
        ...
    def getParameterSize(self) -> int:
        """
            Get the number of parameters (columns in the Jacobian) in this problem.
        
            Returns:
                the number of scalar parameters
        
        
        """
        ...
    def getStart(self) -> org.hipparchus.linear.RealVector:
        """
            Gets the initial guess.
        
            Returns:
                the initial guess values.
        
        
        """
        ...
    class Evaluation:
        def getChiSquare(self) -> float: ...
        def getCost(self) -> float: ...
        def getCovariances(self, double: float) -> org.hipparchus.linear.RealMatrix: ...
        def getJacobian(self) -> org.hipparchus.linear.RealMatrix: ...
        def getPoint(self) -> org.hipparchus.linear.RealVector: ...
        def getRMS(self) -> float: ...
        def getReducedChiSquare(self, int: int) -> float: ...
        def getResiduals(self) -> org.hipparchus.linear.RealVector: ...
        def getSigma(self, double: float) -> org.hipparchus.linear.RealVector: ...

class MultivariateJacobianFunction:
    """
    public interfaceMultivariateJacobianFunction
    
        A interface for functions that compute a vector of values and can compute their derivatives (Jacobian).
    """
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]: ...

class ParameterValidator:
    """
    public interfaceParameterValidator
    
        Interface for validating a set of model parameters.
    """
    def validate(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
            Validates the set of parameters.
        
            Parameters:
                params (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): Input parameters.
        
            Returns:
                the validated values.
        
        
        """
        ...

class AbstractEvaluation(LeastSquaresProblem.Evaluation):
    """
    public abstract classAbstractEvaluation extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`
    
        An implementation of :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation` that is
        designed for extension. All of the methods implemented here use the methods that are left unimplemented.
    """
    def getChiSquare(self) -> float:
        """
            Get the sum of the squares of the residuals.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getChiSquare` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`
        
            Returns:
                the cost.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getResiduals`
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getCost`
        
        
        
        """
        ...
    def getCost(self) -> float:
        """
            Get the cost. It is the square-root of the
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getChiSquare`.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getCost` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`
        
            Returns:
                the cost.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getResiduals`
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getChiSquare`
        
        
        
        """
        ...
    def getCovariances(self, double: float) -> org.hipparchus.linear.RealMatrix:
        """
            Get the covariance matrix of the optimized parameters.
        
        
            Note that this operation involves the inversion of the :code:`J :sup:`T` J` matrix, where :code:`J` is the Jacobian
            matrix. The :code:`threshold` parameter is a way for the caller to specify that the result of this computation should be
            considered meaningless, and thus trigger an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getCovariances` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`
        
            Parameters:
                threshold (double): Singularity threshold.
        
            Returns:
                the covariance matrix.
        
        
        """
        ...
    def getRMS(self) -> float:
        """
            Get the normalized cost. It is the square-root of the sum of squared of the residuals, divided by the number of
            measurements.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getRMS` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`
        
            Returns:
                the cost.
        
        
        """
        ...
    def getReducedChiSquare(self, int: int) -> float:
        """
            Get the reduced chi-square.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getReducedChiSquare` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`
        
            Parameters:
                numberOfFittedParameters (int): Number of fitted parameters.
        
            Returns:
                the sum of the squares of the residuals divided by the number of degrees of freedom.
        
        
        """
        ...
    def getSigma(self, double: float) -> org.hipparchus.linear.RealVector:
        """
            Get an estimate of the standard deviation of the parameters. The returned values are the square root of the diagonal
            coefficients of the covariance matrix, :code:`sd(a[i]) ~= sqrt(C[i][i])`, where :code:`a[i]` is the optimized value of
            the :code:`i`-th parameter, and :code:`C` is the covariance matrix.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getSigma` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`
        
            Parameters:
                covarianceSingularityThreshold (double): Singularity threshold (see
                    :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getCovariances`).
        
            Returns:
                an estimate of the standard deviation of the optimized parameters
        
        
        """
        ...

class LeastSquaresAdapter(LeastSquaresProblem):
    """
    public classLeastSquaresAdapter extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
    
        An adapter that delegates to another implementation of
        :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`.
    """
    def __init__(self, leastSquaresProblem: LeastSquaresProblem): ...
    def evaluate(self, realVector: org.hipparchus.linear.RealVector) -> LeastSquaresProblem.Evaluation:
        """
            Evaluate the model at the specified point.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.evaluate` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Parameters:
                point (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the parameter values.
        
            Returns:
                the model's value and derivative at the given point.
        
        
        """
        ...
    def getConvergenceChecker(self) -> org.hipparchus.optim.ConvergenceChecker[LeastSquaresProblem.Evaluation]: ...
    def getEvaluationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of evaluations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getEvaluationCounter` in
                interface :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...
    def getIterationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of iterations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getIterationCounter` in
                interface :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...
    def getObservationSize(self) -> int:
        """
            Get the number of observations (rows in the Jacobian) in this problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.getObservationSize` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Returns:
                the number of scalar observations
        
        
        """
        ...
    def getParameterSize(self) -> int:
        """
            Get the number of parameters (columns in the Jacobian) in this problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.getParameterSize` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Returns:
                the number of scalar parameters
        
        
        """
        ...
    def getStart(self) -> org.hipparchus.linear.RealVector:
        """
            Gets the initial guess.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.getStart` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Returns:
                the initial guess values.
        
        
        """
        ...

class LeastSquaresOptimizer:
    """
    public interfaceLeastSquaresOptimizer
    
        An algorithm that can be applied to a non-linear least squares problem.
    """
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> 'LeastSquaresOptimizer.Optimum':
        """
            Solve the non-linear least squares problem.
        
            Parameters:
                leastSquaresProblem (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the problem definition, including model function and convergence criteria.
        
            Returns:
                The optimum.
        
        
        """
        ...
    class Optimum(LeastSquaresProblem.Evaluation):
        def getEvaluations(self) -> int: ...
        def getIterations(self) -> int: ...
        @staticmethod
        def of(evaluation: LeastSquaresProblem.Evaluation, int: int, int2: int) -> 'LeastSquaresOptimizer.Optimum': ...

class ValueAndJacobianFunction(MultivariateJacobianFunction):
    """
    public interfaceValueAndJacobianFunctionextends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction`
    
        A interface for functions that compute a vector of values and can compute their derivatives (Jacobian).
    """
    def computeJacobian(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
            Compute the Jacobian.
        
            Parameters:
                params (double[]): Point.
        
            Returns:
                the Jacobian at the given point.
        
        
        """
        ...
    def computeValue(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealVector:
        """
            Compute the value.
        
            Parameters:
                params (double[]): Point.
        
            Returns:
                the value at the given point.
        
        
        """
        ...

class GaussNewtonOptimizer(LeastSquaresOptimizer):
    """
    public classGaussNewtonOptimizer extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
    
        Gauss-Newton least-squares solver.
    
        This class solve a least-square problem by solving the normal equations of the linearized problem at each iteration.
        Either LU decomposition or Cholesky decomposition can be used to solve the normal equations, or QR decomposition or SVD
        decomposition can be used to solve the linear system. Cholesky/LU decomposition is faster but QR decomposition is more
        robust for difficult problems, and SVD can compute a solution for rank-deficient problems.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], boolean: bool): ...
    def getDecomposer(self) -> org.hipparchus.linear.MatrixDecomposer:
        """
            Get the matrix decomposition algorithm.
        
            Returns:
                the decomposition algorithm.
        
        
        """
        ...
    def isFormNormalEquations(self) -> bool:
        """
            Get if the normal equations are explicitly formed.
        
            Returns:
                if the normal equations should be explicitly formed. If :code:`true` then :code:`decomposer` is used to solve J :sup:`T`
                Jx=J :sup:`T` r, otherwise :code:`decomposer` is used to solve Jx=r.
        
        
        """
        ...
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> LeastSquaresOptimizer.Optimum:
        """
            Solve the non-linear least squares problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.optimize` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
        
            Parameters:
                lsp (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the problem definition, including model function and convergence criteria.
        
            Returns:
                The optimum.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                
                meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    def withDecomposer(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]) -> 'GaussNewtonOptimizer':
        """
            Configure the matrix decomposition algorithm.
        
            Parameters:
                newDecomposer (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the decomposition algorithm to use.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withFormNormalEquations(self, boolean: bool) -> 'GaussNewtonOptimizer':
        """
            Configure if the normal equations should be explicitly formed.
        
            Parameters:
                newFormNormalEquations (boolean): whether the normal equations should be explicitly formed. If :code:`true` then :code:`decomposer` is used to solve J
                    :sup:`T` Jx=J :sup:`T` r, otherwise :code:`decomposer` is used to solve Jx=r. If :code:`decomposer` can only solve
                    square systems then this parameter should be :code:`true`.
        
            Returns:
                a new instance.
        
        
        """
        ...

class LevenbergMarquardtOptimizer(LeastSquaresOptimizer):
    """
    public classLevenbergMarquardtOptimizer extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
    
        This class solves a least-squares problem using the Levenberg-Marquardt algorithm.
    
        This implementation *should* work even for over-determined systems (i.e. systems having more point than equations).
        Over-determined systems are solved by ignoring the point which have the smallest impact according to their jacobian
        column norm. Only the rank of the matrix and some loop bounds are changed to implement this.
    
        The resolution engine is a simple translation of the MINPACK `lmder <http://www.netlib.org/minpack/lmder.f>` routine
        with minor changes. The changes include the over-determined resolution, the use of inherited convergence checker and the
        Q.R. decomposition which has been rewritten following the algorithm described in the P. Lascaux and R. Theodor book
        *Analyse numérique matricielle appliquée à l'art de l'ingénieur*, Masson 1986.
    
        The authors of the original fortran version are:
    
          - Argonne National Laboratory. MINPACK project. March 1980
          - Burton S. Garbow
          - Kenneth E. Hillstrom
          - Jorge J. More
    
    
        The redistribution policy for MINPACK is available `here <http://www.netlib.org/minpack/disclaimer>`, for convenience,
        it is reproduced below.
    
            Minpack Copyright Notice (1999) University of Chicago. All rights reserved
    
            Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
            following conditions are met:
    
              1.  Redistributions of source code must retain the above copyright notice, this list of conditions and the following
                disclaimer.
              2.  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
                disclaimer in the documentation and/or other materials provided with the distribution.
              3.  The end-user documentation included with the redistribution, if any, must include the following acknowledgment:
                :code:`This product includes software developed by the University of Chicago, as Operator of Argonne National
                Laboratory.` Alternately, this acknowledgment may appear in the software itself, if and wherever such third-party
                acknowledgments normally appear.
              4.  **WARRANTY DISCLAIMER. THE SOFTWARE IS SUPPLIED "AS IS" WITHOUT WARRANTY OF ANY KIND. THE COPYRIGHT HOLDER, THE UNITED
                STATES, THE UNITED STATES DEPARTMENT OF ENERGY, AND THEIR EMPLOYEES: (1) DISCLAIM ANY WARRANTIES, EXPRESS OR IMPLIED,
                INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR
                NON-INFRINGEMENT, (2) DO NOT ASSUME ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS
                OF THE SOFTWARE, (3) DO NOT REPRESENT THAT USE OF THE SOFTWARE WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS, (4) DO NOT
                WARRANT THAT THE SOFTWARE WILL FUNCTION UNINTERRUPTED, THAT IT IS ERROR-FREE OR THAT ANY ERRORS WILL BE CORRECTED.**
              5.  **LIMITATION OF LIABILITY. IN NO EVENT WILL THE COPYRIGHT HOLDER, THE UNITED STATES, THE UNITED STATES DEPARTMENT OF
                ENERGY, OR THEIR EMPLOYEES: BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL OR PUNITIVE DAMAGES OF ANY
                KIND OR NATURE, INCLUDING BUT NOT LIMITED TO LOSS OF PROFITS OR LOSS OF DATA, FOR ANY REASON WHATSOEVER, WHETHER SUCH
                LIABILITY IS ASSERTED ON THE BASIS OF CONTRACT, TORT (INCLUDING NEGLIGENCE OR STRICT LIABILITY), OR OTHERWISE, EVEN IF
                ANY OF SAID PARTIES HAS BEEN WARNED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGES.**
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float): ...
    def getCostRelativeTolerance(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withCostRelativeTolerance`
        
        
        
        """
        ...
    def getInitialStepBoundFactor(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withInitialStepBoundFactor`
        
        
        
        """
        ...
    def getOrthoTolerance(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withOrthoTolerance`
        
        
        
        """
        ...
    def getParameterRelativeTolerance(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withParameterRelativeTolerance`
        
        
        
        """
        ...
    def getRankingThreshold(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withRankingThreshold`
        
        
        
        """
        ...
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> LeastSquaresOptimizer.Optimum:
        """
            Solve the non-linear least squares problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.optimize` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
        
            Parameters:
                problem (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the problem definition, including model function and convergence criteria.
        
            Returns:
                The optimum.
        
        
        """
        ...
    def withCostRelativeTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
            Build new instance with cost relative tolerance.
        
            Parameters:
                newCostRelativeTolerance (double): Desired relative error in the sum of squares.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withInitialStepBoundFactor(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
            Build new instance with initial step bound factor.
        
            Parameters:
                newInitialStepBoundFactor (double): Positive input variable used in determining the initial step bound. This bound is set to the product of
                    initialStepBoundFactor and the euclidean norm of :code:`diag * x` if non-zero, or else to
                    :code:`newInitialStepBoundFactor` itself. In most cases factor should lie in the interval :code:`(0.1, 100.0)`.
                    :code:`100` is a generally recommended value. of the matrix is reduced.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withOrthoTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
            Build new instance with ortho tolerance.
        
            Parameters:
                newOrthoTolerance (double): Desired max cosine on the orthogonality between the function vector and the columns of the Jacobian.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withParameterRelativeTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
            Build new instance with parameter relative tolerance.
        
            Parameters:
                newParRelativeTolerance (double): Desired relative error in the approximate solution parameters.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withRankingThreshold(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
            Build new instance with ranking threshold.
        
            Parameters:
                newQRRankingThreshold (double): Desired threshold for QR ranking. If the squared norm of a column vector is smaller or equal to this threshold during QR
                    decomposition, it is considered to be a zero vector and hence the rank of the matrix is reduced.
        
            Returns:
                a new instance.
        
        
        """
        ...

class SequentialGaussNewtonOptimizer(LeastSquaresOptimizer):
    """
    public classSequentialGaussNewtonOptimizer extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
    
        Sequential Gauss-Newton least-squares solver.
    
        This class solve a least-square problem by solving the normal equations of the linearized problem at each iteration.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], boolean: bool, evaluation: LeastSquaresProblem.Evaluation): ...
    def getDecomposer(self) -> org.hipparchus.linear.MatrixDecomposer:
        """
            Get the matrix decomposition algorithm.
        
            Returns:
                the decomposition algorithm.
        
        
        """
        ...
    def getOldEvaluation(self) -> LeastSquaresProblem.Evaluation:
        """
            Get the previous evaluation used by the optimizer.
        
            Returns:
                the previous evaluation.
        
        
        """
        ...
    def isFormNormalEquations(self) -> bool:
        """
            Get if the normal equations are explicitly formed.
        
            Returns:
                if the normal equations should be explicitly formed. If :code:`true` then :code:`decomposer` is used to solve J :sup:`T`
                Jx=J :sup:`T` r, otherwise :code:`decomposer` is used to solve Jx=r.
        
        
        """
        ...
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> LeastSquaresOptimizer.Optimum:
        """
            Solve the non-linear least squares problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.optimize` in
                interface :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
        
            Parameters:
                lsp (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the problem definition, including model function and convergence criteria.
        
            Returns:
                The optimum.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                
                meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    @typing.overload
    def withAPrioriData(self, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> 'SequentialGaussNewtonOptimizer':
        """
            Configure from a priori state and covariance.
        
            This building method generates a fake evaluation and calls
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withEvaluation`, so either
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withAPrioriData` or
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withEvaluation` should be
            called, but not both as the last one called will override the previous one.
        
            A Cholesky decomposition is used to compute the weighted jacobian from the a priori covariance. This method uses the
            default thresholds of the decomposition.
        
            Parameters:
                aPrioriState (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): a priori state to use
                aPrioriCovariance (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): a priori covariance to use
        
            Returns:
                a new instance.
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withAPrioriData`
        
        
            Configure from a priori state and covariance.
        
            This building method generates a fake evaluation and calls
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withEvaluation`, so either
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withAPrioriData` or
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withEvaluation` should be
            called, but not both as the last one called will override the previous one.
        
            A Cholesky decomposition is used to compute the weighted jacobian from the a priori covariance.
        
            Parameters:
                aPrioriState (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): a priori state to use
                aPrioriCovariance (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): a priori covariance to use
                relativeSymmetryThreshold (double):             Cholesky decomposition threshold above which off-diagonal elements are considered too different and matrix not symmetric
                absolutePositivityThreshold (double): Cholesky decomposition threshold below which diagonal elements are considered null and matrix not positive definite
        
            Returns:
                a new instance.
        
            Since:
                2.3
        
        
        """
        ...
    @typing.overload
    def withAPrioriData(self, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, double: float, double2: float) -> 'SequentialGaussNewtonOptimizer': ...
    def withDecomposer(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]) -> 'SequentialGaussNewtonOptimizer':
        """
            Configure the matrix decomposition algorithm.
        
            Parameters:
                newDecomposer (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.https:.www.hipparchus.org.hipparchus`): the decomposition algorithm to use.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withEvaluation(self, evaluation: LeastSquaresProblem.Evaluation) -> 'SequentialGaussNewtonOptimizer':
        """
            Configure the previous evaluation used by the optimizer.
        
            This building method uses a complete evaluation to retrieve a priori data. Note that as
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withAPrioriData` generates a
            fake evaluation and calls this method, either
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withAPrioriData` or
            :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.withEvaluation` should be
            called, but not both as the last one called will override the previous one.
        
            Parameters:
                previousEvaluation (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`): the previous evaluation used by the optimizer.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withFormNormalEquations(self, boolean: bool) -> 'SequentialGaussNewtonOptimizer':
        """
            Configure if the normal equations should be explicitly formed.
        
            Parameters:
                newFormNormalEquations (boolean): whether the normal equations should be explicitly formed. If :code:`true` then :code:`decomposer` is used to solve J
                    :sup:`T` Jx=J :sup:`T` r, otherwise :code:`decomposer` is used to solve Jx=r. If :code:`decomposer` can only solve
                    square systems then this parameter should be :code:`true`.
        
            Returns:
                a new instance.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.vector.leastsquares")``.

    AbstractEvaluation: typing.Type[AbstractEvaluation]
    EvaluationRmsChecker: typing.Type[EvaluationRmsChecker]
    GaussNewtonOptimizer: typing.Type[GaussNewtonOptimizer]
    LeastSquaresAdapter: typing.Type[LeastSquaresAdapter]
    LeastSquaresBuilder: typing.Type[LeastSquaresBuilder]
    LeastSquaresFactory: typing.Type[LeastSquaresFactory]
    LeastSquaresOptimizer: typing.Type[LeastSquaresOptimizer]
    LeastSquaresProblem: typing.Type[LeastSquaresProblem]
    LevenbergMarquardtOptimizer: typing.Type[LevenbergMarquardtOptimizer]
    MultivariateJacobianFunction: typing.Type[MultivariateJacobianFunction]
    ParameterValidator: typing.Type[ParameterValidator]
    SequentialGaussNewtonOptimizer: typing.Type[SequentialGaussNewtonOptimizer]
    ValueAndJacobianFunction: typing.Type[ValueAndJacobianFunction]
