import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.util
import typing



class EvaluationRmsChecker(org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation']):
    """
    public class EvaluationRmsChecker extends Object implements :class:`~org.hipparchus.optim.ConvergenceChecker`<:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`>
    
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
                :meth:`~org.hipparchus.optim.ConvergenceChecker.converged`Â in
                interfaceÂ :class:`~org.hipparchus.optim.ConvergenceChecker`
        
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
    public class LeastSquaresBuilder extends Object
    
        A mutable builder for :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`s.
    
        Also see:
            :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresFactory`
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
    def checker(self, convergenceChecker: org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation']) -> 'LeastSquaresBuilder': ...
    def checkerPair(self, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointVectorValuePair]) -> 'LeastSquaresBuilder': ...
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
    def model(self, multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, multivariateMatrixFunction: org.hipparchus.analysis.MultivariateMatrixFunction) -> 'LeastSquaresBuilder':
        """
            Configure the model function.
        
            Parameters:
                value (MultivariateVectorFunction): the model function value
                jacobian (MultivariateMatrixFunction): the Jacobian of :code:`value`
        
            Returns:
                this
        
        """
        ...
    @typing.overload
    def model(self, multivariateJacobianFunction: 'MultivariateJacobianFunction') -> 'LeastSquaresBuilder':
        """
            Configure the model function.
        
            Parameters:
                newModel (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction`): the model function value and Jacobian
        
            Returns:
                this
        
        
        """
        ...
    def parameterValidator(self, parameterValidator: 'ParameterValidator') -> 'LeastSquaresBuilder':
        """
            Configure the validator of the model parameters.
        
            Parameters:
                newValidator (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.ParameterValidator`): Parameter validator.
        
            Returns:
                this object.
        
        
        """
        ...
    @typing.overload
    def start(self, doubleArray: typing.List[float]) -> 'LeastSquaresBuilder':
        """
            Configure the initial guess.
        
            Parameters:
                newStart (RealVector): the initial guess.
        
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
    def target(self, doubleArray: typing.List[float]) -> 'LeastSquaresBuilder':
        """
            Configure the observed data.
        
            Parameters:
                newTarget (RealVector): the observed data.
        
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
                newWeight (RealMatrix): the weight matrix
        
            Returns:
                this
        
        
        """
        ...

class LeastSquaresFactory:
    """
    public class LeastSquaresFactory extends Object
    
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
                counter (Incrementor): the counter to increment.
        
            Returns:
                a least squares problem that tracks evaluations
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def create(multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, multivariateMatrixFunction: org.hipparchus.analysis.MultivariateMatrixFunction, doubleArray: typing.List[float], doubleArray2: typing.List[float], realMatrix: org.hipparchus.linear.RealMatrix, convergenceChecker: org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], int: int, int2: int) -> 'LeastSquaresProblem': ...
    @typing.overload
    @staticmethod
    def create(multivariateJacobianFunction: 'MultivariateJacobianFunction', realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, convergenceChecker: org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], int: int, int2: int) -> 'LeastSquaresProblem': ...
    @typing.overload
    @staticmethod
    def create(multivariateJacobianFunction: 'MultivariateJacobianFunction', realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, convergenceChecker: org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], int: int, int2: int, boolean: bool, parameterValidator: 'ParameterValidator') -> 'LeastSquaresProblem': ...
    @typing.overload
    @staticmethod
    def create(multivariateJacobianFunction: 'MultivariateJacobianFunction', realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, convergenceChecker: org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation'], int: int, int2: int) -> 'LeastSquaresProblem': ...
    @staticmethod
    def evaluationChecker(convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointVectorValuePair]) -> org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation']: ...
    @staticmethod
    def model(multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, multivariateMatrixFunction: org.hipparchus.analysis.MultivariateMatrixFunction) -> 'MultivariateJacobianFunction':
        """
            Combine a null with a null to produce a
            :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction`.
        
            Parameters:
                value (MultivariateVectorFunction): the vector value function
                jacobian (MultivariateMatrixFunction): the Jacobian function
        
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
                weights (RealVector): the diagonal of the weight matrix
        
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
                weights (RealMatrix): the matrix of weights
        
            Returns:
                a new :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem` with the weights applied. The
                original :code:`problem` is not modified.
        
        
        """
        ...

class LeastSquaresProblem(org.hipparchus.optim.OptimizationProblem['LeastSquaresProblem.Evaluation']):
    """
    public interface LeastSquaresProblem extends :class:`~org.hipparchus.optim.OptimizationProblem`<:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation`>
    
        The data necessary to define a non-linear least squares problem.
    
        Includes the observed values, computed model function, and convergence/divergence criteria. Weights are implicit in
        :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getResiduals` and
        :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation.getJacobian`.
    
        Instances are typically either created progressively using a
        :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresBuilder` or created at once using a
        :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresFactory`.
    
        Also see:
            :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresBuilder`,
            :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresFactory`,
            :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresAdapter`
    """
    def evaluate(self, realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresProblem.Evaluation':
        """
            Evaluate the model at the specified point.
        
            Parameters:
                point (RealVector): the parameter values.
        
            Returns:
                the model's value and derivative at the given point.
        
            Raises:
                : if the maximal number of evaluations (of the model vector function) is exceeded.
        
        
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
    public interface MultivariateJacobianFunction
    
        A interface for functions that compute a vector of values and can compute their derivatives (Jacobian).
    """
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]:
        """
            Compute the function value and its Jacobian.
        
            Parameters:
                point (RealVector): the abscissae
        
            Returns:
                the values and their Jacobian of this vector valued function.
        
        
        """
        ...

class ParameterValidator:
    """
    public interface ParameterValidator
    
        Interface for validating a set of model parameters.
    """
    def validate(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
            Validates the set of parameters.
        
            Parameters:
                params (RealVector): Input parameters.
        
            Returns:
                the validated values.
        
        
        """
        ...

class AbstractEvaluation(LeastSquaresProblem.Evaluation):
    def __init__(self, int: int): ...
    def getChiSquare(self) -> float: ...
    def getCost(self) -> float: ...
    def getCovariances(self, double: float) -> org.hipparchus.linear.RealMatrix: ...
    def getRMS(self) -> float: ...
    def getReducedChiSquare(self, int: int) -> float: ...
    def getSigma(self, double: float) -> org.hipparchus.linear.RealVector: ...

class LeastSquaresAdapter(LeastSquaresProblem):
    """
    public class LeastSquaresAdapter extends Object implements :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
    
        An adapter that delegates to another implementation of
        :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`.
    """
    def __init__(self, leastSquaresProblem: LeastSquaresProblem): ...
    def evaluate(self, realVector: org.hipparchus.linear.RealVector) -> LeastSquaresProblem.Evaluation:
        """
            Evaluate the model at the specified point.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.evaluate`Â in
                interfaceÂ :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Parameters:
                point (RealVector): 
            Returns:
                the model's value and derivative at the given point.
        
        
        """
        ...
    def getConvergenceChecker(self) -> org.hipparchus.optim.ConvergenceChecker[LeastSquaresProblem.Evaluation]: ...
    def getEvaluationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of evaluations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getEvaluationCounter`Â in
                interfaceÂ :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...
    def getIterationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of iterations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getIterationCounter`Â in
                interfaceÂ :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...
    def getObservationSize(self) -> int:
        """
            Get the number of observations (rows in the Jacobian) in this problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.getObservationSize`Â in
                interfaceÂ :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Returns:
                the number of scalar observations
        
        
        """
        ...
    def getParameterSize(self) -> int:
        """
            Get the number of parameters (columns in the Jacobian) in this problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.getParameterSize`Â in
                interfaceÂ :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Returns:
                the number of scalar parameters
        
        
        """
        ...
    def getStart(self) -> org.hipparchus.linear.RealVector:
        """
            Gets the initial guess.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.getStart`Â in
                interfaceÂ :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`
        
            Returns:
                the initial guess values.
        
        
        """
        ...

class LeastSquaresOptimizer:
    """
    public interface LeastSquaresOptimizer
    
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
    public interface ValueAndJacobianFunction extends :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction`
    
        A interface for functions that compute a vector of values and can compute their derivatives (Jacobian).
    """
    def computeJacobian(self, doubleArray: typing.List[float]) -> org.hipparchus.linear.RealMatrix:
        """
            Compute the Jacobian.
        
            Parameters:
                params (double[]): Point.
        
            Returns:
                the Jacobian at the given point.
        
        
        """
        ...
    def computeValue(self, doubleArray: typing.List[float]) -> org.hipparchus.linear.RealVector:
        """
            Compute the value.
        
            Parameters:
                params (double[]): Point.
        
            Returns:
                the value at the given point.
        
        
        """
        ...

class GaussNewtonOptimizer(LeastSquaresOptimizer):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer, boolean: bool): ...
    def getDecomposer(self) -> org.hipparchus.linear.MatrixDecomposer: ...
    def isFormNormalEquations(self) -> bool: ...
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> LeastSquaresOptimizer.Optimum: ...
    def toString(self) -> str: ...
    def withDecomposer(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer) -> 'GaussNewtonOptimizer': ...
    def withFormNormalEquations(self, boolean: bool) -> 'GaussNewtonOptimizer': ...

class LevenbergMarquardtOptimizer(LeastSquaresOptimizer):
    """
    public class LevenbergMarquardtOptimizer extends Object implements :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
    
        This class solves a least-squares problem using the Levenberg-Marquardt algorithm.
    
        This implementation *should* work even for over-determined systems (i.e. systems having more point than equations).
        Over-determined systems are solved by ignoring the point which have the smallest impact according to their jacobian
        column norm. Only the rank of the matrix and some loop bounds are changed to implement this.
    
        The resolution engine is a simple translation of the MINPACK `lmder <http://www.netlib.org/minpack/lmder.f>` routine
        with minor changes. The changes include the over-determined resolution, the use of inherited convergence checker and the
        Q.R. decomposition which has been rewritten following the algorithm described in the P. Lascaux and R. Theodor book
        *Analyse numÃ©rique matricielle appliquÃ©e Ã  l'art de l'ingÃ©nieur*, Masson 1986.
    
        The authors of the original fortran version are:
    
          - Argonne National Laboratory. MINPACK project. March 1980
          - Burton S. Garbow
          - Kenneth E. Hillstrom
          - Jorge J. More
    
        The redistribution policy for MINPACK is available `here <http://www.netlib.org/minpack/disclaimer>`, for convenience,
        it is reproduced below.
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
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withCostRelativeTolerance`
        
        
        """
        ...
    def getInitialStepBoundFactor(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withInitialStepBoundFactor`
        
        
        """
        ...
    def getOrthoTolerance(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withOrthoTolerance`
        
        
        """
        ...
    def getParameterRelativeTolerance(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withParameterRelativeTolerance`
        
        
        """
        ...
    def getRankingThreshold(self) -> float:
        """
            Gets the value of a tuning parameter.
        
            Returns:
                the parameter's value.
        
            Also see:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LevenbergMarquardtOptimizer.withRankingThreshold`
        
        
        """
        ...
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> LeastSquaresOptimizer.Optimum:
        """
            Solve the non-linear least squares problem.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.optimize`Â in
                interfaceÂ :class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer`
        
            Parameters:
                problem (:class:`~org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem`): the problem definition, including model function and convergence criteria.
        
            Returns:
                The optimum.
        
        
        """
        ...
    def withCostRelativeTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
        
            Parameters:
                newCostRelativeTolerance (double): Desired relative error in the sum of squares.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withInitialStepBoundFactor(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
        
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
            Modifies the given parameter.
        
            Parameters:
                newOrthoTolerance (double): Desired max cosine on the orthogonality between the function vector and the columns of the Jacobian.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withParameterRelativeTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
        
            Parameters:
                newParRelativeTolerance (double): Desired relative error in the approximate solution parameters.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withRankingThreshold(self, double: float) -> 'LevenbergMarquardtOptimizer':
        """
        
            Parameters:
                newQRRankingThreshold (double): Desired threshold for QR ranking. If the squared norm of a column vector is smaller or equal to this threshold during QR
                    decomposition, it is considered to be a zero vector and hence the rank of the matrix is reduced.
        
            Returns:
                a new instance.
        
        
        """
        ...

class SequentialGaussNewtonOptimizer(LeastSquaresOptimizer):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer, boolean: bool, evaluation: LeastSquaresProblem.Evaluation): ...
    def getDecomposer(self) -> org.hipparchus.linear.MatrixDecomposer: ...
    def getOldEvaluation(self) -> LeastSquaresProblem.Evaluation: ...
    def isFormNormalEquations(self) -> bool: ...
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> LeastSquaresOptimizer.Optimum: ...
    def toString(self) -> str: ...
    def withAPrioriData(self, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> 'SequentialGaussNewtonOptimizer': ...
    def withDecomposer(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer) -> 'SequentialGaussNewtonOptimizer': ...
    def withEvaluation(self, evaluation: LeastSquaresProblem.Evaluation) -> 'SequentialGaussNewtonOptimizer': ...
    def withFormNormalEquations(self, boolean: bool) -> 'SequentialGaussNewtonOptimizer': ...


class __module_protocol__(typing.Protocol):
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
