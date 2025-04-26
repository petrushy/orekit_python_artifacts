
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import jpype
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar
import typing



class Preconditioner:
    """
    public interfacePreconditioner
    
        This interface represents a preconditioner for differentiable scalar objective function optimizers.
    """
    def precondition(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Precondition a search direction.
        
            The returned preconditioned search direction must be computed fast or the algorithm performances will drop drastically.
            A classical approach is to compute only the diagonal elements of the hessian and to divide the raw search direction by
            these elements if they are all positive. If at least one of them is negative, it is safer to return a clone of the raw
            search direction as if the hessian was the identity matrix. The rationale for this simplified choice is that a negative
            diagonal element means the current point is far from the optimum and preconditioning will not be efficient anyway in
            this case.
        
            Parameters:
                point (double[]): current point at which the search direction was computed
                r (double[]): raw search direction (i.e. opposite of the gradient)
        
            Returns:
                approximation of H :sup:`-1` r where H is the objective function hessian
        
        
        """
        ...

class NonLinearConjugateGradientOptimizer(org.hipparchus.optim.nonlinear.scalar.GradientMultivariateOptimizer):
    """
    public classNonLinearConjugateGradientOptimizer extends :class:`~org.hipparchus.optim.nonlinear.scalar.GradientMultivariateOptimizer`
    
        Non-linear conjugate gradient optimizer.
    
    
        This class supports both the Fletcher-Reeves and the Polak-Ribière update formulas for the conjugate search directions.
        It also supports optional preconditioning.
    
    
        Constraints are not supported: the call to
        :meth:`~org.hipparchus.optim.nonlinear.scalar.gradient.NonLinearConjugateGradientOptimizer.optimize` will throw
        :class:`~org.hipparchus.optim.nonlinear.scalar.gradient.https:.www.hipparchus.org.hipparchus` if bounds are passed to
        it.
    """
    @typing.overload
    def __init__(self, formula: 'NonLinearConjugateGradientOptimizer.Formula', convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], typing.Callable[[int, org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], bool]]): ...
    @typing.overload
    def __init__(self, formula: 'NonLinearConjugateGradientOptimizer.Formula', convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], typing.Callable[[int, org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], bool]], double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, formula: 'NonLinearConjugateGradientOptimizer.Formula', convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], typing.Callable[[int, org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], bool]], double: float, double2: float, double3: float, preconditioner: typing.Union[Preconditioner, typing.Callable]): ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...
    class Formula(java.lang.Enum['NonLinearConjugateGradientOptimizer.Formula']):
        FLETCHER_REEVES: typing.ClassVar['NonLinearConjugateGradientOptimizer.Formula'] = ...
        POLAK_RIBIERE: typing.ClassVar['NonLinearConjugateGradientOptimizer.Formula'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'NonLinearConjugateGradientOptimizer.Formula': ...
        @staticmethod
        def values() -> typing.MutableSequence['NonLinearConjugateGradientOptimizer.Formula']: ...
    class IdentityPreconditioner(Preconditioner):
        def __init__(self): ...
        def precondition(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.scalar.gradient")``.

    NonLinearConjugateGradientOptimizer: typing.Type[NonLinearConjugateGradientOptimizer]
    Preconditioner: typing.Type[Preconditioner]
