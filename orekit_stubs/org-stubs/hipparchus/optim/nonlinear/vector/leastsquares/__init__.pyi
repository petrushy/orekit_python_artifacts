import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.util
import typing



class EvaluationRmsChecker(org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation']):
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def converged(self, int: int, evaluation: 'LeastSquaresProblem.Evaluation', evaluation2: 'LeastSquaresProblem.Evaluation') -> bool: ...

class LeastSquaresBuilder:
    def __init__(self): ...
    def build(self) -> 'LeastSquaresProblem': ...
    def checker(self, convergenceChecker: org.hipparchus.optim.ConvergenceChecker['LeastSquaresProblem.Evaluation']) -> 'LeastSquaresBuilder': ...
    def checkerPair(self, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointVectorValuePair]) -> 'LeastSquaresBuilder': ...
    def lazyEvaluation(self, boolean: bool) -> 'LeastSquaresBuilder': ...
    def maxEvaluations(self, int: int) -> 'LeastSquaresBuilder': ...
    def maxIterations(self, int: int) -> 'LeastSquaresBuilder': ...
    @typing.overload
    def model(self, multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, multivariateMatrixFunction: org.hipparchus.analysis.MultivariateMatrixFunction) -> 'LeastSquaresBuilder': ...
    @typing.overload
    def model(self, multivariateJacobianFunction: 'MultivariateJacobianFunction') -> 'LeastSquaresBuilder': ...
    def parameterValidator(self, parameterValidator: 'ParameterValidator') -> 'LeastSquaresBuilder': ...
    @typing.overload
    def start(self, doubleArray: typing.List[float]) -> 'LeastSquaresBuilder': ...
    @typing.overload
    def start(self, realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresBuilder': ...
    @typing.overload
    def target(self, doubleArray: typing.List[float]) -> 'LeastSquaresBuilder': ...
    @typing.overload
    def target(self, realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresBuilder': ...
    def weight(self, realMatrix: org.hipparchus.linear.RealMatrix) -> 'LeastSquaresBuilder': ...

class LeastSquaresFactory:
    @staticmethod
    def countEvaluations(leastSquaresProblem: 'LeastSquaresProblem', incrementor: org.hipparchus.util.Incrementor) -> 'LeastSquaresProblem': ...
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
    def model(multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, multivariateMatrixFunction: org.hipparchus.analysis.MultivariateMatrixFunction) -> 'MultivariateJacobianFunction': ...
    @staticmethod
    def weightDiagonal(leastSquaresProblem: 'LeastSquaresProblem', realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresProblem': ...
    @staticmethod
    def weightMatrix(leastSquaresProblem: 'LeastSquaresProblem', realMatrix: org.hipparchus.linear.RealMatrix) -> 'LeastSquaresProblem': ...

class LeastSquaresProblem(org.hipparchus.optim.OptimizationProblem['LeastSquaresProblem.Evaluation']):
    def evaluate(self, realVector: org.hipparchus.linear.RealVector) -> 'LeastSquaresProblem.Evaluation': ...
    def getObservationSize(self) -> int: ...
    def getParameterSize(self) -> int: ...
    def getStart(self) -> org.hipparchus.linear.RealVector: ...
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
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]: ...

class ParameterValidator:
    def validate(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealVector: ...

class AbstractEvaluation(LeastSquaresProblem.Evaluation):
    def __init__(self, int: int): ...
    def getChiSquare(self) -> float: ...
    def getCost(self) -> float: ...
    def getCovariances(self, double: float) -> org.hipparchus.linear.RealMatrix: ...
    def getRMS(self) -> float: ...
    def getReducedChiSquare(self, int: int) -> float: ...
    def getSigma(self, double: float) -> org.hipparchus.linear.RealVector: ...

class LeastSquaresAdapter(LeastSquaresProblem):
    def __init__(self, leastSquaresProblem: LeastSquaresProblem): ...
    def evaluate(self, realVector: org.hipparchus.linear.RealVector) -> LeastSquaresProblem.Evaluation: ...
    def getConvergenceChecker(self) -> org.hipparchus.optim.ConvergenceChecker[LeastSquaresProblem.Evaluation]: ...
    def getEvaluationCounter(self) -> org.hipparchus.util.Incrementor: ...
    def getIterationCounter(self) -> org.hipparchus.util.Incrementor: ...
    def getObservationSize(self) -> int: ...
    def getParameterSize(self) -> int: ...
    def getStart(self) -> org.hipparchus.linear.RealVector: ...

class LeastSquaresOptimizer:
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> 'LeastSquaresOptimizer.Optimum': ...
    class Optimum(LeastSquaresProblem.Evaluation):
        def getEvaluations(self) -> int: ...
        def getIterations(self) -> int: ...
        @staticmethod
        def of(evaluation: LeastSquaresProblem.Evaluation, int: int, int2: int) -> 'LeastSquaresOptimizer.Optimum': ...

class ValueAndJacobianFunction(MultivariateJacobianFunction):
    def computeJacobian(self, doubleArray: typing.List[float]) -> org.hipparchus.linear.RealMatrix: ...
    def computeValue(self, doubleArray: typing.List[float]) -> org.hipparchus.linear.RealVector: ...

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
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float): ...
    def getCostRelativeTolerance(self) -> float: ...
    def getInitialStepBoundFactor(self) -> float: ...
    def getOrthoTolerance(self) -> float: ...
    def getParameterRelativeTolerance(self) -> float: ...
    def getRankingThreshold(self) -> float: ...
    def optimize(self, leastSquaresProblem: LeastSquaresProblem) -> LeastSquaresOptimizer.Optimum: ...
    def withCostRelativeTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer': ...
    def withInitialStepBoundFactor(self, double: float) -> 'LevenbergMarquardtOptimizer': ...
    def withOrthoTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer': ...
    def withParameterRelativeTolerance(self, double: float) -> 'LevenbergMarquardtOptimizer': ...
    def withRankingThreshold(self, double: float) -> 'LevenbergMarquardtOptimizer': ...

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
    @typing.overload
    def withAPrioriData(self, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> 'SequentialGaussNewtonOptimizer': ...
    @typing.overload
    def withAPrioriData(self, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, double: float, double2: float) -> 'SequentialGaussNewtonOptimizer': ...
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
