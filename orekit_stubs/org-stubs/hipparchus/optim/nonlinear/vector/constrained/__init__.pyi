
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import typing



class ADMMQPConvergenceChecker(org.hipparchus.optim.ConvergenceChecker['LagrangeSolution'], org.hipparchus.optim.OptimizationData):
    """
    Convergence Checker for ADMM QP Optimizer.
    
    Since:
        3.1
    """
    @typing.overload
    def converged(self, rp: float, rd: float, maxPrimal: float, maxDual: float) -> bool:
        """
        Evaluate convergence.
        
        Parameters:
            rp (double): primal residual
            rd (double): dual residual
            maxPrimal (double): primal vectors max
            maxDual (double): dual vectors max
        
        Returns:
            true of convergence has been reached
        
        
        """
        ...
    @typing.overload
    def converged(self, i: int, previous: 'LagrangeSolution', current: 'LagrangeSolution') -> bool:
        """
        Check if the optimization algorithm has converged.
        
        Specified by: converged in interface ConvergenceChecker
        
        Parameters:
            i (int): Current iteration.
            previous (LagrangeSolution): Best point in the previous iteration.
            current (LagrangeSolution): Best point in the current iteration.
        
        Returns:
            true if the algorithm is considered to have converged.
        
        """
        ...
    def maxDual(self, x: org.hipparchus.linear.RealVector, y: org.hipparchus.linear.RealVector) -> float:
        """
        Compute dual vectors max.
        
        Parameters:
            x (hipparchus): primal problem solution
            y (hipparchus): dual problem solution
        
        Returns:
            dual vectors max
        
        
        """
        ...
    def maxPrimal(self, x: org.hipparchus.linear.RealVector, z: org.hipparchus.linear.RealVector) -> float:
        """
        Compute primal vectors max.
        
        Parameters:
            x (hipparchus): primal problem solution
            z (hipparchus): auxiliary variable
        
        Returns:
            primal vectors max
        
        
        """
        ...
    def residualDual(self, x: org.hipparchus.linear.RealVector, y: org.hipparchus.linear.RealVector) -> float:
        """
        Compute dual residual.
        
        Parameters:
            x (hipparchus): primal problem solution
            y (hipparchus): dual problem solution
        
        Returns:
            dual residual
        
        
        """
        ...
    def residualPrime(self, x: org.hipparchus.linear.RealVector, z: org.hipparchus.linear.RealVector) -> float:
        """
        Compute primal residual.
        
        Parameters:
            x (hipparchus): primal problem solution
            z (hipparchus): auxiliary variable
        
        Returns:
            primal residual
        
        
        """
        ...

class ADMMQPModifiedRuizEquilibrium:
    """
    TBD.
    
    Since:
        3.1
    """
    def __init__(self, H: org.hipparchus.linear.RealMatrix, A: org.hipparchus.linear.RealMatrix, q: org.hipparchus.linear.RealVector):
        """
        Simple constructor
        
        Parameters:
            H (hipparchus): square matrix of weights for quadratic terms
            A (hipparchus): constraints coefficients matrix
            q (hipparchus): vector of weights for linear terms
        
        
        """
        ...
    def getScaledA(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get scaled constraints coefficients matrix.
        
        Returns:
            scaled constraints coefficients matrix
        
        
        """
        ...
    def getScaledH(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get scaled square matrix of weights for quadratic terms.
        
        Returns:
            scaled square matrix of weights for quadratic terms
        
        
        """
        ...
    def getScaledLUb(self, lb1: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
        Get scaled upper bound
        
        Parameters:
            lb1 (hipparchus): unscaled lower bound
        
        Returns:
            scaled lower bound
        
        
        """
        ...
    def getScaledQ(self) -> org.hipparchus.linear.RealVector:
        """
        Get scaled vector of weights for linear terms.
        
        Returns:
            scaled vector of weights for linear terms
        
        
        """
        ...
    def normalize(self, epsilon: float, maxIteration: int) -> None:
        """
        Normalize matrices.
        
        Parameters:
            epsilon (double): TBD
            maxIteration (int): TBD
        
        
        """
        ...
    def unscaleX(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
        Unscale solution vector.
        
        Parameters:
            x (hipparchus): scaled solution vector
        
        Returns:
            unscaled solution vector
        
        
        """
        ...
    def unscaleY(self, y: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
        Unscale Y vector.
        
        Parameters:
            y (hipparchus): scaled Y vector
        
        Returns:
            unscaled Y vector
        
        
        """
        ...
    def unscaleZ(self, z: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
        Unscale Z vector.
        
        Parameters:
            z (hipparchus): scaled Z vector
        
        Returns:
            unscaled Z vector
        
        
        """
        ...

class ADMMQPOption(org.hipparchus.optim.OptimizationData):
    """
    Container for ADMMQPOptimizer settings.
    
    Since:
        3.1
    """
    DEFAULT_EPS: typing.ClassVar[float] = ...
    """
    Default Absolute and Relative Tolerance for convergence.
    
    Also see:
        constant
    
    
    """
    DEFAULT_EPS_INFEASIBLE: typing.ClassVar[float] = ...
    """
    Default Absolute and Relative Tolerance for Infeasible Criteria.
    
    Also see:
        constant
    
    
    """
    DEFAULT_SIGMA: typing.ClassVar[float] = ...
    """
    Default Value of regularization term sigma for Karush–Kuhn–Tucker solver.
    
    Also see:
        constant
    
    
    """
    DEFAULT_ALPHA: typing.ClassVar[float] = ...
    """
    Default Value of Alpha filter for ADMM iteration.
    
    Also see:
        constant
    
    
    """
    DEFAULT_SCALING: typing.ClassVar[bool] = ...
    """
    Default Value for Enabling Problem Scaling.
    
    Also see:
        constant
    
    
    """
    DEFAULT_SCALING_MAX_ITERATION: typing.ClassVar[int] = ...
    """
    Default Value for the Max Iteration for the scaling.
    
    Also see:
        constant
    
    
    """
    DEFAULT_RHO_UPDATE: typing.ClassVar[bool] = ...
    """
    Default Value for adapting the weight during iterations.
    
    Also see:
        constant
    
    
    """
    DEFAULT_RHO_MAX: typing.ClassVar[float] = ...
    """
    Default Max Value for the Weight for ADMM iteration.
    
    Also see:
        constant
    
    
    """
    DEFAULT_RHO_MIN: typing.ClassVar[float] = ...
    """
    Default Min Value for the Weight for ADMM iteration.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_RHO_ITERATION: typing.ClassVar[int] = ...
    """
    Default Max number of weight changes.
    
    Also see:
        constant
    
    
    """
    DEFAULT_POLISHING: typing.ClassVar[bool] = ...
    """
    Default Value for enabling polishing the solution.
    
    Also see:
        constant
    
    
    """
    DEFAULT_POLISHING_ITERATION: typing.ClassVar[int] = ...
    """
    Default Value for Iteration of polishing Algorithm.
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getAlpha(self) -> float:
        """
        Get value of alpha filter for ADMM iteration.
        
        Returns:
            value of alpha filter for ADMM iteration
        
        
        """
        ...
    def getEps(self) -> float:
        """
        Get absolute and Relative Tolerance for convergence.
        
        Returns:
            absolute and Relative Tolerance for convergence
        
        
        """
        ...
    def getEpsInfeasible(self) -> float:
        """
        Get absolute and Relative Tolerance for infeasible criteria.
        
        Returns:
            absolute and Relative Tolerance for infeasible criteria
        
        
        """
        ...
    def getMaxRhoIteration(self) -> int:
        """
        Get max number of weight changes.
        
        Returns:
            max number of weight changes
        
        
        """
        ...
    def getPolishIteration(self) -> int:
        """
        Get number of iterations of polishing algorithm.
        
        Returns:
            number of iterations of polishing algorithm
        
        
        """
        ...
    def getRhoMax(self) -> float:
        """
        Get max Value for the Weight for ADMM iteration.
        
        Returns:
            max Value for the Weight for ADMM iteration
        
        
        """
        ...
    def getRhoMin(self) -> float:
        """
        Get min Value for the Weight for ADMM iteration.
        
        Returns:
            min Value for the Weight for ADMM iteration
        
        
        """
        ...
    def getScaleMaxIteration(self) -> int:
        """
        Get max iteration for the scaling.
        
        Returns:
            max iteration for the scaling
        
        
        """
        ...
    def getSigma(self) -> float:
        """
        Get value of regularization term sigma for Karush–Kuhn–Tucker solver.
        
        Returns:
            value of regularization term sigma for Karush–Kuhn–Tucker solver
        
        
        """
        ...
    def isPolishing(self) -> bool:
        """
        Check if polishing is enabled.
        
        Returns:
            true if polishing is enabled
        
        
        """
        ...
    def isScaling(self) -> bool:
        """
        Check if scaling is enabled.
        
        Returns:
            true if scaling is enabled
        
        
        """
        ...
    def setAlpha(self, alpha: float) -> None:
        """
        Set value of alpha filter for ADMM iteration.
        
        Parameters:
            alpha (double): value of alpha filter for ADMM iteration
        
        
        """
        ...
    def setEps(self, eps: float) -> None:
        """
        Set absolute and Relative Tolerance for convergence.
        
        Parameters:
            eps (double): absolute and Relative Tolerance for convergence
        
        
        """
        ...
    def setEpsInfeasible(self, epsInfeasible: float) -> None:
        """
        Set absolute and Relative Tolerance for infeasible criteria.
        
        Parameters:
            epsInfeasible (double): absolute and Relative Tolerance for infeasible criteria
        
        
        """
        ...
    def setMaxRhoIteration(self, maxRhoIteration: int) -> None:
        """
        Set max number of weight changes.
        
        Parameters:
            maxRhoIteration (int): max number of weight changes
        
        
        """
        ...
    def setPolishing(self, polishing: bool) -> None:
        """
        Set polishing enabling flag.
        
        Parameters:
            polishing (boolean): if true, polishing is enabled
        
        
        """
        ...
    def setPolishingIteration(self, polishingIteration: int) -> None:
        """
        Set number of iterations of polishing algorithm.
        
        Parameters:
            polishingIteration (int): number of iterations of polishing algorithm
        
        
        """
        ...
    def setRhoMax(self, rhoMax: float) -> None:
        """
        Set max Value for the Weight for ADMM iteration.
        
        Parameters:
            rhoMax (double): max Value for the Weight for ADMM iteration
        
        
        """
        ...
    def setRhoMin(self, rhoMin: float) -> None:
        """
        Set min Value for the Weight for ADMM iteration.
        
        Parameters:
            rhoMin (double): min Value for the Weight for ADMM iteration
        
        
        """
        ...
    def setScaleMaxIteration(self, scaleMaxIteration: int) -> None:
        """
        Set max iteration for the scaling.
        
        Parameters:
            scaleMaxIteration (int): max iteration for the scaling
        
        
        """
        ...
    def setScaling(self, scaling: bool) -> None:
        """
        Set scaling enabling flag.
        
        Parameters:
            scaling (boolean): if true, scaling is enabled
        
        
        """
        ...
    def setSigma(self, sigma: float) -> None:
        """
        Set value of regularization term sigma for Karush–Kuhn–Tucker solver.
        
        Parameters:
            sigma (double): value of regularization term sigma for Karush–Kuhn–Tucker solver
        
        
        """
        ...
    def setUpdateRho(self, updateRho: bool) -> None:
        """
        Set weight updating flag.
        
        Parameters:
            updateRho (boolean): if true, weight is updated during iterations
        
        
        """
        ...
    def updateRho(self) -> bool:
        """
        Check if weight updating is enabled.
        
        Returns:
            true if weight is updated during iterations
        
        
        """
        ...

class ConstraintOptimizer(org.hipparchus.optim.BaseMultivariateOptimizer['LagrangeSolution']):
    """
    Abstract Constraint Optimizer.
    
    Since:
        3.1
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optData: org.hipparchus.optim.OptimizationData) -> 'LagrangeSolution': ...

_KarushKuhnTuckerSolver__T = typing.TypeVar('_KarushKuhnTuckerSolver__T')  # <T>
class KarushKuhnTuckerSolver(org.hipparchus.optim.OptimizationData, typing.Generic[_KarushKuhnTuckerSolver__T]):
    """
    Karush–Kuhn–Tucker Solver.
    
    Solve Equation: \[\begin{align} |H A^{T}| & = B_1\\ |A R| & = B_2 \end{align}\]
    
    Since:
        3.1
    """
    def iterate(self, *b: org.hipparchus.linear.RealVector) -> _KarushKuhnTuckerSolver__T:
        """
        Iterate Karush–Kuhn–Tucker equation from given list of Vector
        
        Parameters:
            b (hipparchus...): list of vectors
        
        Returns:
            Tuple with the solution x,Lambda,value
        
        
        """
        ...
    def solve(self, b1: org.hipparchus.linear.RealVector, b2: org.hipparchus.linear.RealVector) -> _KarushKuhnTuckerSolver__T:
        """
        Solve Karush–Kuhn–Tucker equation from given right hand value.
        
        Parameters:
            b1 (hipparchus): first right hand vector
            b2 (hipparchus): second right hand vector
        
        Returns:
            Tuple with the solution x,Lambda,value
        
        
        """
        ...

class LagrangeSolution:
    """
    Container for Lagrange t-uple.
    
    Since:
        3.1
    """
    def __init__(self, x: org.hipparchus.linear.RealVector, lambda_: org.hipparchus.linear.RealVector, value: float):
        """
        Simple constructor.
        
        Parameters:
            x (hipparchus): solution
            lambda (hipparchus): Lagrange multipliers
            value (double): objective function value
        
        
        """
        ...
    def getLambda(self) -> org.hipparchus.linear.RealVector:
        """
        Returns Lambda Multiplier
        
        Returns:
            X Lambda Multiplier
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Returns min(max) evaluated function at x
        
        Returns:
            min(max) evaluated function at x
        
        
        """
        ...
    def getX(self) -> org.hipparchus.linear.RealVector:
        """
        Returns X solution
        
        Returns:
            X solution
        
        
        """
        ...

class SQPOption(org.hipparchus.optim.OptimizationData):
    """
    Parameter for SQP Algorithm.
    
    Since:
        3.1
    """
    DEFAULT_CONV_CRITERIA: typing.ClassVar[int] = ...
    """
    Default convergence criteria.
    
    Also see:
        constant
    
    
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    Default tolerance for convergence and active constraint.
    
    Also see:
        constant
    
    
    """
    DEFAULT_RHO: typing.ClassVar[float] = ...
    """
    Default weight for augmented QP subproblem.
    
    Also see:
        constant
    
    
    """
    DEFAULT_SIGMA_MAX: typing.ClassVar[float] = ...
    """
    Default max value admitted for additional variable in QP subproblem.
    
    Also see:
        constant
    
    
    """
    DEFAULT_QP_MAX_LOOP: typing.ClassVar[int] = ...
    """
    Default max iteration admitted for QP subproblem.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MU: typing.ClassVar[float] = ...
    """
    Default parameter for evaluation of Armijo condition for descend direction.
    
    Also see:
        constant
    
    
    """
    DEFAULT_B: typing.ClassVar[float] = ...
    """
    Default parameter for quadratic line search.
    
    Also see:
        constant
    
    
    """
    DEFAULT_USE_FUNCTION_HESSIAN: typing.ClassVar[bool] = ...
    """
    Default flag for using BFGS update formula.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_LINE_SEARCH_ITERATION: typing.ClassVar[int] = ...
    """
    Default max iteration before reset hessian.
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Simple constructor.
        
        This constructor uses all defaults values.
        """
        ...
    def getB(self) -> float:
        """
        Get parameter for quadratic line search.
        
        Returns:
            parameter for quadratic line search
        
        
        """
        ...
    def getConvCriteria(self) -> int:
        """
        Get convergence criteria.
        
        Returns:
            convergence criteria
        
        
        """
        ...
    def getEps(self) -> float:
        """
        Get tolerance for convergence and active constraint evaluation.
        
        Returns:
            tolerance for convergence and active constraint evaluation
        
        
        """
        ...
    def getMaxLineSearchIteration(self) -> int:
        """
        Get max Iteration for the line search
        
        Returns:
            max Iteration for the line search
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get parameter for evaluation of Armijo condition for descend direction.
        
        Returns:
            parameter for evaluation of Armijo condition for descend direction
        
        
        """
        ...
    def getQpMaxLoop(self) -> int:
        """
        Get max iteration admitted for QP subproblem evaluation.
        
        Returns:
            max iteration admitted for QP subproblem evaluation
        
        
        """
        ...
    def getRhoCons(self) -> float:
        """
        Get weight for augmented QP subproblem.
        
        Returns:
            weight for augmented QP subproblem
        
        
        """
        ...
    def getSigmaMax(self) -> float:
        """
        Get max value admitted for the solution of the additional variable in QP subproblem.
        
        Returns:
            max value admitted for the solution of the additional variable in QP subproblem
        
        
        """
        ...
    def setB(self, b: float) -> None:
        """
        Set parameter for quadratic line search.
        
        Parameters:
            b (double): parameter for quadratic line search
        
        
        """
        ...
    def setConvCriteria(self, convCriteria: int) -> None:
        """
        Set convergence criteria.
        
        Parameters:
            convCriteria (int): convergence criteria
        
        
        """
        ...
    def setEps(self, eps: float) -> None:
        """
        Set tolerance for convergence and active constraint evaluation.
        
        Parameters:
            eps (double): tolerance for convergence and active constraint evaluation
        
        
        """
        ...
    def setMaxLineSearchIteration(self, maxLineSearchIteration: int) -> None:
        """
        Set max Iteration for the line search
        
        Parameters:
            maxLineSearchIteration (int): max Iteration for the line search
        
        
        """
        ...
    def setMu(self, mu: float) -> None:
        """
        Set parameter for evaluation of Armijo condition for descend direction.
        
        Parameters:
            mu (double): parameter for evaluation of Armijo condition for descend direction
        
        
        """
        ...
    def setQpMaxLoop(self, qpMaxLoop: int) -> None:
        """
        Set max iteration admitted for QP subproblem evaluation.
        
        Parameters:
            qpMaxLoop (int): max iteration admitted for QP subproblem evaluation
        
        
        """
        ...
    def setRhoCons(self, rhoCons: float) -> None:
        """
        Set weight for augmented QP subproblem.
        
        Parameters:
            rhoCons (double): weight for augmented QP subproblem
        
        
        """
        ...
    def setSigmaMax(self, sigmaMax: float) -> None:
        """
        Set max value admitted for the solution of the additional variable in QP subproblem.
        
        Parameters:
            sigmaMax (double): max value admitted for the solution of the additional variable in QP subproblem
        
        
        """
        ...
    def setUseFunHessian(self, useFunHessian: bool) -> None:
        """
        Enable or Disable using direct the function Hessian.
        
        Parameters:
            useFunHessian (boolean): enable or Disable using direct the function Hessian
        
        
        """
        ...
    def useFunHessian(self) -> bool:
        """
        Check if using direct the function Hessian is enabled or disabled.
        
        Returns:
            true if using direct the function Hessian is enabled
        
        
        """
        ...

class TwiceDifferentiableFunction(org.hipparchus.analysis.MultivariateFunction):
    """
    A MultivariateFunction that also has a defined gradient and Hessian.
    
    Since:
        3.1
    """
    def __init__(self): ...
    def dim(self) -> int:
        """
        Returns the dimensionality of the function domain. If dim() returns (n) then this function expects an n-vector as its input.
        
        Returns:
            the expected dimension of the function's domain
        
        
        """
        ...
    @typing.overload
    def gradient(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
        Parameters:
            x (hipparchus): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        Returns the gradient of this function at (x)
        
        Parameters:
            x (double[]): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        
        """
        ...
    @typing.overload
    def gradient(self, x: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealVector: ...
    @typing.overload
    def hessian(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealMatrix:
        """
        Parameters:
            x (hipparchus): a point to evaluate this Hessian at
        
        Returns:
            the Hessian of this function at (x)
        
        The Hessian of this function at (x)
        
        Parameters:
            x (double[]): a point to evaluate this Hessian at
        
        Returns:
            the Hessian of this function at (x)
        
        
        """
        ...
    @typing.overload
    def hessian(self, x: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix: ...
    @typing.overload
    def value(self, x: org.hipparchus.linear.RealVector) -> float:
        """
        Parameters:
            x (hipparchus): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        Returns the value of this function at (x)
        
        Specified by: hipparchus in interface hipparchus
        
        Parameters:
            x (double[]): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: typing.Union[typing.List[float], jpype.JArray]) -> float: ...

class VectorDifferentiableFunction(org.hipparchus.analysis.MultivariateVectorFunction):
    """
    A MultivariateFunction that also has a defined gradient and Hessian.
    
    Since:
        3.1
    """
    def dim(self) -> int:
        """
        Returns the dimensionality of the function domain. If dim() returns (n) then this function expects an n-vector as its input.
        
        Returns:
            the expected dimension of the function's domain
        
        
        """
        ...
    def dimY(self) -> int:
        """
        Returns the dimensionality of the function eval.
        
        Returns:
            the expected dimension of the function's eval
        
        
        """
        ...
    def gradient(self, x: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Returns the gradient of this function at (x)
        
        Parameters:
            x (double[]): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        
        """
        ...
    def jacobian(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealMatrix:
        """
        Returns the gradient of this function at (x)
        
        Parameters:
            x (hipparchus): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
        Parameters:
            x (hipparchus): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        Returns the value of this function at (x)
        
        Specified by: hipparchus in interface hipparchus
        
        Parameters:
            x (double[]): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...

class ADMMQPKKT(KarushKuhnTuckerSolver['ADMMQPSolution']):
    """
    Alternative Direction Method of Multipliers Solver.
    
    Since:
        3.1
    """
    def initialize(self, newH: org.hipparchus.linear.RealMatrix, newA: org.hipparchus.linear.RealMatrix, newQ: org.hipparchus.linear.RealVector, me: int, newLb: org.hipparchus.linear.RealVector, newUb: org.hipparchus.linear.RealVector, rho: float, newSigma: float, newAlpha: float) -> None:
        """
        Initialize problem
        
        Parameters:
            newH (hipparchus): square matrix of weights for quadratic term
            newA (hipparchus): constraints coefficients matrix
            newQ (hipparchus): TBD
            me (int): number of equality constraints
            newLb (hipparchus): lower bound
            newUb (hipparchus): upper bound
            rho (double): step size
            newSigma (double): regularization term sigma for Karush–Kuhn–Tucker solver
            newAlpha (double): alpha filter for ADMM iteration
        
        
        """
        ...
    def iterate(self, *previousSol: org.hipparchus.linear.RealVector) -> 'ADMMQPSolution':
        """
        Iterate Karush–Kuhn–Tucker equation from given list of Vector
        
        Specified by: iterate in interface KarushKuhnTuckerSolver
        
        Parameters:
            previousSol (hipparchus...): list of vectors
        
        Returns:
            Tuple with the solution x,Lambda,value
        
        
        """
        ...
    def solve(self, b1: org.hipparchus.linear.RealVector, b2: org.hipparchus.linear.RealVector) -> 'ADMMQPSolution':
        """
        Solve Karush–Kuhn–Tucker equation from given right hand value.
        
        Specified by: solve in interface KarushKuhnTuckerSolver
        
        Parameters:
            b1 (hipparchus): first right hand vector
            b2 (hipparchus): second right hand vector
        
        Returns:
            Tuple with the solution x,Lambda,value
        
        
        """
        ...
    def updateSigmaRho(self, newSigma: float, me: int, rho: float) -> None:
        """
        Update steps
        
        Parameters:
            newSigma (double): new regularization term sigma for Karush–Kuhn–Tucker solver
            me (int): number of equality constraints
            rho (double): new step size
        
        
        """
        ...

class ADMMQPSolution(LagrangeSolution):
    """
    Internal Solution for ADMM QP Optimizer.
    
    Since:
        3.1
    """
    @typing.overload
    def __init__(self, x: org.hipparchus.linear.RealVector, v: org.hipparchus.linear.RealVector): ...
    @typing.overload
    def __init__(self, x: org.hipparchus.linear.RealVector, lambda_: org.hipparchus.linear.RealVector, value: float): ...
    @typing.overload
    def __init__(self, x: org.hipparchus.linear.RealVector, v: org.hipparchus.linear.RealVector, y: org.hipparchus.linear.RealVector, z: org.hipparchus.linear.RealVector): ...
    @typing.overload
    def __init__(self, x: org.hipparchus.linear.RealVector, v: org.hipparchus.linear.RealVector, y: org.hipparchus.linear.RealVector, z: org.hipparchus.linear.RealVector, value: float): ...
    def getV(self) -> org.hipparchus.linear.RealVector:
        """
        Returns V tilde auxiliary Variable
        
        Returns:
            V tilde auxiliary Variable
        
        
        """
        ...
    def getZ(self) -> org.hipparchus.linear.RealVector:
        """
        Returns Z auxiliary Variable
        
        Returns:
            Z auxiliary Variable
        
        
        """
        ...

class AbstractSQPOptimizer(ConstraintOptimizer):
    """
    Abstract class for Sequential Quadratic Programming solvers
    
    Since:
        3.1
    """
    def getEqConstraint(self) -> 'EqualityConstraint':
        """
        Getter for equality constraint.
        
        Returns:
            equality constraint
        
        
        """
        ...
    def getIqConstraint(self) -> 'InequalityConstraint':
        """
        Getter for inequality constraint.
        
        Returns:
            inequality constraint
        
        
        """
        ...
    def getObj(self) -> TwiceDifferentiableFunction:
        """
        Getter for objective function.
        
        Returns:
            objective function
        
        
        """
        ...
    def getSettings(self) -> SQPOption:
        """
        Getter for settings.
        
        Returns:
            settings
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optData: org.hipparchus.optim.OptimizationData) -> LagrangeSolution:
        """
        Description copied from class: optimize Stores data and performs the optimization.
        
        The list of parameters is open-ended so that sub-classes can extend it with arguments specific to their concrete implementations.
        
        When the method is called multiple times, instance data is overwritten only when actually present in the list of arguments: when not specified, data set in a previous call is retained (and thus is optional in subsequent calls).
        
        Important note: Subclasses must override parseOptimizationData if they need to register their own options; but then, they must also call parseOptimizationData(optData) within that method.
        
        Overrides: optimize in class ConstraintOptimizer
        
        Parameters:
            optData (OptimizationData...): Optimization data. In addition to those documented in parseOptimizationData,
                this method will register the following data:
        
                  - InitialGuess
                  - SimpleBounds
        
        
        Returns:
            a point/value pair that satisfies the convergence criteria.
        
        
        """
        ...

class Constraint(VectorDifferentiableFunction, org.hipparchus.optim.OptimizationData):
    """
    Generic constraint.
    
    Since:
        3.1
    """
    def getLowerBound(self) -> org.hipparchus.linear.RealVector:
        """
        Get Lower Bound for value.
        
        Returns:
            Lower Bound for value
        
        
        """
        ...
    def getUpperBound(self) -> org.hipparchus.linear.RealVector:
        """
        Get Upper Bound for value.
        
        Returns:
            Upper Bound for value
        
        
        """
        ...
    def overshoot(self, y: org.hipparchus.linear.RealVector) -> float:
        """
        Check how much a point overshoots the constraint.
        
        The overshoots is zero if the point fulfills the constraint, and positive if the value of the constraint is on the wrong side of getLowerBound or getUpperBound boundaries.
        
        Parameters:
            y (hipparchus): constraint value (y = value(x))
        
        Returns:
            L¹-norm of constraint overshoot
        
        
        """
        ...

class QPOptimizer(ConstraintOptimizer):
    """
    Quadratic programming Optimizater.
    
    Since:
        3.1
    """
    def __init__(self): ...

class QuadraticFunction(TwiceDifferentiableFunction):
    """
    Given P, Q, d, implements \(\frac{1}{2}x^T P X + Q^T x + d\). The gradient is P x + Q^T, and the Hessian is P
    
    Since:
        3.1
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, realVector: org.hipparchus.linear.RealVector, double: float): ...
    def dim(self) -> int:
        """
        Returns the dimensionality of the function domain. If dim() returns (n) then this function expects an n-vector as its input.
        
        Specified by: dim in class TwiceDifferentiableFunction
        
        Returns:
            the expected dimension of the function's domain
        
        
        """
        ...
    def getD(self) -> float:
        """
        Get constant term.
        
        Returns:
            constant term
        
        
        """
        ...
    def getP(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get square matrix of weights for quadratic terms.
        
        Returns:
            square matrix of weights for quadratic terms
        
        
        """
        ...
    def getQ(self) -> org.hipparchus.linear.RealVector:
        """
        Get vector of weights for linear terms.
        
        Returns:
            vector of weights for linear terms
        
        
        """
        ...
    @typing.overload
    def gradient(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector:
        """
        Specified by: gradient in class TwiceDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        
        """
        ...
    @typing.overload
    def gradient(self, x: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealVector: ...
    @typing.overload
    def hessian(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealMatrix:
        """
        Specified by: hessian in class TwiceDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this Hessian at
        
        Returns:
            the Hessian of this function at (x)
        
        
        """
        ...
    @typing.overload
    def hessian(self, x: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix: ...
    @typing.overload
    def value(self, x: org.hipparchus.linear.RealVector) -> float:
        """
        Specified by: value in class TwiceDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: typing.Union[typing.List[float], jpype.JArray]) -> float: ...

class ADMMQPOptimizer(QPOptimizer):
    """
    Alternating Direction Method of Multipliers Quadratic Programming Optimizer. \[ min \frac{1}{2} X^T Q X + G X a\\ A X = B_1\\ B X \ge B_2\\ l_b \le C X \le u_b \] Algorithm based on paper:"An Operator Splitting Solver for Quadratic Programs(Bartolomeo Stellato, Goran Banjac, Paul Goulart, Alberto Bemporad, Stephen Boyd,February 13 2020)"
    
    Since:
        3.1
    """
    def __init__(self):
        """
        Simple constructor.
        
        This constructor sets all ADMMQPOption to their default values
        """
        ...
    def doOptimize(self) -> LagrangeSolution:
        """
        Performs the bulk of the optimization algorithm.
        
        Overrides: doOptimize in class QPOptimizer
        
        Returns:
            the point/value pair giving the optimal value of the objective function.
        
        
        """
        ...
    def getConvergenceChecker(self) -> org.hipparchus.optim.ConvergenceChecker[LagrangeSolution]:
        """
        Gets the convergence checker.
        
        Overrides: getConvergenceChecker in class BaseOptimizer
        
        Returns:
            the object used to check for convergence.
        
        
        """
        ...
    def isConverged(self) -> bool:
        """
        Check if convergence has been reached.
        
        Returns:
            true if convergence has been reached
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optData: org.hipparchus.optim.OptimizationData) -> LagrangeSolution:
        """
        Stores data and performs the optimization.
        
        The list of parameters is open-ended so that sub-classes can extend it with arguments specific to their concrete implementations.
        
        When the method is called multiple times, instance data is overwritten only when actually present in the list of arguments: when not specified, data set in a previous call is retained (and thus is optional in subsequent calls).
        
        Important note: Subclasses must override parseOptimizationData if they need to register their own options; but then, they must also call parseOptimizationData(optData) within that method.
        
        Overrides: optimize in class ConstraintOptimizer
        
        Parameters:
            optData (OptimizationData...): Optimization data. In addition to those documented in parseOptimizationData,
                this method will register the following data:
        
                  - InitialGuess
                  - SimpleBounds
        
        
        Returns:
            a point/value pair that satisfies the convergence criteria.
        
        
        """
        ...

class BoundedConstraint(Constraint):
    """
    Constraint with lower and upper bounds: \(l \le f(x) \le u\).
    
    Since:
        3.1
    """
    def dimY(self) -> int:
        """
        Returns the dimensionality of the function eval.
        
        Specified by: dimY in interface VectorDifferentiableFunction
        
        Returns:
            the expected dimension of the function's eval
        
        
        """
        ...
    def getLowerBound(self) -> org.hipparchus.linear.RealVector:
        """
        Get Lower Bound for value.
        
        Specified by: getLowerBound in interface Constraint
        
        Returns:
            Lower Bound for value
        
        
        """
        ...
    def getUpperBound(self) -> org.hipparchus.linear.RealVector:
        """
        Get Upper Bound for value.
        
        Specified by: getUpperBound in interface Constraint
        
        Returns:
            Upper Bound for value
        
        
        """
        ...
    def overshoot(self, y: org.hipparchus.linear.RealVector) -> float:
        """
        Check how much a point overshoots the constraint.
        
        The overshoots is zero if the point fulfills the constraint, and positive if the value of the constraint is on the wrong side of getLowerBound or getUpperBound boundaries.
        
        Specified by: overshoot in interface Constraint
        
        Parameters:
            y (hipparchus): constraint value (y = value(x))
        
        Returns:
            L¹-norm of constraint overshoot
        
        
        """
        ...

class SQPOptimizerGM(AbstractSQPOptimizer):
    """
    Sequential Quadratic Programming Optimizer.
    
    min f(x)
    
    q(x)=b1
    
    h(x)>=b2
    
    Algorithm based on paper:"Some Theoretical properties of an augmented lagrangian merit function (Gill,Murray,Sauders,Wriht,April 1986)"
    
    Since:
        3.1
    """
    def __init__(self): ...
    def doOptimize(self) -> LagrangeSolution:
        """
        Performs the bulk of the optimization algorithm.
        
        Specified by: doOptimize in class BaseOptimizer
        
        Returns:
            the point/value pair giving the optimal value of the objective function.
        
        
        """
        ...

class SQPOptimizerS(AbstractSQPOptimizer):
    """
    Sequential Quadratic Programming Optimizer.
    
    min f(x)
    
    q(x)=b1
    
    h(x)>=b2
    
    Algorithm based on paper:"On the convergence of a sequential quadratic programming method(Klaus Shittkowki,January 1982)"
    
    Since:
        3.1
    """
    def __init__(self): ...
    def doOptimize(self) -> LagrangeSolution:
        """
        Performs the bulk of the optimization algorithm.
        
        Specified by: doOptimize in class BaseOptimizer
        
        Returns:
            the point/value pair giving the optimal value of the objective function.
        
        
        """
        ...

class EqualityConstraint(BoundedConstraint):
    """
    Equality Constraint.
    
    Since:
        3.1
    """
    def __init__(self, value: org.hipparchus.linear.RealVector):
        """
        Simple constructor.
        
        Parameters:
            value (hipparchus): equality value
        
        
        """
        ...

class InequalityConstraint(BoundedConstraint):
    """
    Inequality Constraint with lower bound only: \(l \le f(x)\).
    
    Since:
        3.1
    """
    def __init__(self, lower: org.hipparchus.linear.RealVector):
        """
        Simple constructor.
        
        Parameters:
            lower (hipparchus): lower bound
        
        
        """
        ...

class LinearBoundedConstraint(BoundedConstraint, org.hipparchus.optim.OptimizationData):
    """
    A set of linear inequality constraints expressed as ub>Ax>lb.
    
    Since:
        3.1
    """
    @typing.overload
    def __init__(self, a: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], lower: typing.Union[typing.List[float], jpype.JArray], upper: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, a: org.hipparchus.linear.RealMatrix, lower: org.hipparchus.linear.RealVector, upper: org.hipparchus.linear.RealVector): ...
    def dim(self) -> int:
        """
        Returns the dimensionality of the function domain. If dim() returns (n) then this function expects an n-vector as its input.
        
        Specified by: dim in interface VectorDifferentiableFunction
        
        Returns:
            the expected dimension of the function's domain
        
        
        """
        ...
    def jacobian(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealMatrix:
        """
        Returns the gradient of this function at (x)
        
        Specified by: jacobian in interface VectorDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Specified by: hipparchus in interface hipparchus
        
        Specified by: value in interface VectorDifferentiableFunction
        
        Parameters:
            x (double[]): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        Returns the value of this function at (x)
        
        Specified by: value in interface VectorDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector: ...

class LinearEqualityConstraint(EqualityConstraint, org.hipparchus.optim.OptimizationData):
    """
    A set of linear equality constraints given as Ax = b.
    
    Since:
        3.1
    """
    @typing.overload
    def __init__(self, a: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, a: org.hipparchus.linear.RealMatrix, b: org.hipparchus.linear.RealVector): ...
    def dim(self) -> int:
        """
        Description copied from interface: dim Returns the dimensionality of the function domain. If dim() returns (n) then this function expects an n-vector as its input.
        
        Specified by: dim in interface VectorDifferentiableFunction
        
        Returns:
            the expected dimension of the function's domain
        
        
        """
        ...
    def getA(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the matrix of linear weights.
        
        Returns:
            matrix of linear weights
        
        
        """
        ...
    def jacobian(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealMatrix:
        """
        Description copied from interface: jacobian Returns the gradient of this function at (x)
        
        Specified by: jacobian in interface VectorDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Description copied from interface: value Returns the value of this function at (x)
        
        Specified by: value in interface VectorDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector: ...

class LinearInequalityConstraint(InequalityConstraint, org.hipparchus.optim.OptimizationData):
    """
    Set of linear inequality constraints expressed as \( A x \gt B\).
    
    Since:
        3.1
    """
    @typing.overload
    def __init__(self, a: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, a: org.hipparchus.linear.RealMatrix, b: org.hipparchus.linear.RealVector): ...
    def dim(self) -> int:
        """
        Description copied from interface: dim Returns the dimensionality of the function domain. If dim() returns (n) then this function expects an n-vector as its input.
        
        Specified by: dim in interface VectorDifferentiableFunction
        
        Returns:
            the expected dimension of the function's domain
        
        
        """
        ...
    def jacobian(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealMatrix:
        """
        Description copied from interface: jacobian Returns the gradient of this function at (x)
        
        Specified by: jacobian in interface VectorDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this gradient at
        
        Returns:
            the gradient of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Description copied from interface: value Returns the value of this function at (x)
        
        Specified by: value in interface VectorDifferentiableFunction
        
        Parameters:
            x (hipparchus): a point to evaluate this function at.
        
        Returns:
            the value of this function at (x)
        
        
        """
        ...
    @typing.overload
    def value(self, x: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.vector.constrained")``.

    ADMMQPConvergenceChecker: typing.Type[ADMMQPConvergenceChecker]
    ADMMQPKKT: typing.Type[ADMMQPKKT]
    ADMMQPModifiedRuizEquilibrium: typing.Type[ADMMQPModifiedRuizEquilibrium]
    ADMMQPOptimizer: typing.Type[ADMMQPOptimizer]
    ADMMQPOption: typing.Type[ADMMQPOption]
    ADMMQPSolution: typing.Type[ADMMQPSolution]
    AbstractSQPOptimizer: typing.Type[AbstractSQPOptimizer]
    BoundedConstraint: typing.Type[BoundedConstraint]
    Constraint: typing.Type[Constraint]
    ConstraintOptimizer: typing.Type[ConstraintOptimizer]
    EqualityConstraint: typing.Type[EqualityConstraint]
    InequalityConstraint: typing.Type[InequalityConstraint]
    KarushKuhnTuckerSolver: typing.Type[KarushKuhnTuckerSolver]
    LagrangeSolution: typing.Type[LagrangeSolution]
    LinearBoundedConstraint: typing.Type[LinearBoundedConstraint]
    LinearEqualityConstraint: typing.Type[LinearEqualityConstraint]
    LinearInequalityConstraint: typing.Type[LinearInequalityConstraint]
    QPOptimizer: typing.Type[QPOptimizer]
    QuadraticFunction: typing.Type[QuadraticFunction]
    SQPOptimizerGM: typing.Type[SQPOptimizerGM]
    SQPOptimizerS: typing.Type[SQPOptimizerS]
    SQPOption: typing.Type[SQPOption]
    TwiceDifferentiableFunction: typing.Type[TwiceDifferentiableFunction]
    VectorDifferentiableFunction: typing.Type[VectorDifferentiableFunction]
