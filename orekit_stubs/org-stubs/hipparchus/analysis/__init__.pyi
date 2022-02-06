import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.analysis.function
import org.hipparchus.analysis.integration
import org.hipparchus.analysis.interpolation
import org.hipparchus.analysis.polynomials
import org.hipparchus.analysis.solvers
import typing



class BivariateFunction:
    """
    public interface BivariateFunction
    
        An interface representing a bivariate real function.
    """
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

_CalculusFieldBivariateFunction__T = typing.TypeVar('_CalculusFieldBivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldBivariateFunction(typing.Generic[_CalculusFieldBivariateFunction__T]):
    """
    public interface CalculusFieldBivariateFunction<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>>
    
        An interface representing a bivariate field function.
    
        Since:
            1.5
    """
    def value(self, t: _CalculusFieldBivariateFunction__T, t2: _CalculusFieldBivariateFunction__T) -> _CalculusFieldBivariateFunction__T:
        """
            Compute the value for the function.
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.CalculusFieldBivariateFunction`): Abscissa for which the function value should be computed.
                y (:class:`~org.hipparchus.analysis.CalculusFieldBivariateFunction`): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

_CalculusFieldUnivariateFunction__T = typing.TypeVar('_CalculusFieldUnivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateFunction(typing.Generic[_CalculusFieldUnivariateFunction__T]):
    """
    public interface CalculusFieldUnivariateFunction<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>>
    
        An interface representing a univariate real function.
    
        When a *user-defined* function encounters an error during evaluation, the
        :meth:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction.value` method should throw a *user-defined* unchecked
        exception.
    
        The following code excerpt shows the recommended way to do that using a root solver as an example, but the same
        construct is applicable to ODE integrators or optimizers.
    
        .. code-block: java
        
         private static class LocalException extends RuntimeException {
             // The x value that caused the problem.
             private final SomeFieldType x;
        
             public LocalException(SomeFieldType x) {
                 this.x = x;
             }
        
             public double getX() {
                 return x;
             }
         }
        
         private static class MyFunction implements FieldUnivariateFunction<SomeFieldType> {
             public SomeFieldType value(SomeFieldType x) {
                 SomeFieldType y = hugeFormula(x);
                 if (somethingBadHappens) {
                   throw new LocalException(x);
                 }
                 return y;
             }
         }
        
         public void compute() {
             try {
                 solver.solve(maxEval, new MyFunction(a, b, c), min, max);
             } catch (LocalException le) {
                 // Retrieve the x value.
             }
         }
         
    
        As shown, the exception is local to the user's code and it is guaranteed that Hipparchus will not catch it.
    
        Also see:
            :class:`~org.hipparchus.analysis.UnivariateFunction`, :class:`~org.hipparchus.analysis.FieldUnivariateFunction`
    """
    def value(self, t: _CalculusFieldUnivariateFunction__T) -> _CalculusFieldUnivariateFunction__T:
        """
            Compute the value of the function.
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction`): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
            Raises:
                : when the activated method itself can ascertain that a precondition, specified in the API expressed at the level of the
                    activated method, has been violated. When Hipparchus throws an :code:`IllegalArgumentException`, it is usually the
                    consequence of checking the actual parameters passed to the method.
        
        
        """
        ...

_CalculusFieldUnivariateMatrixFunction__T = typing.TypeVar('_CalculusFieldUnivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateMatrixFunction(typing.Generic[_CalculusFieldUnivariateMatrixFunction__T]):
    """
    public interface CalculusFieldUnivariateMatrixFunction<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>>
    
        An interface representing a univariate matrix function.
    
        Since:
            1.3
    """
    def value(self, t: _CalculusFieldUnivariateMatrixFunction__T) -> typing.List[typing.List[_CalculusFieldUnivariateMatrixFunction__T]]:
        """
            Compute the value for the function.
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.CalculusFieldUnivariateMatrixFunction`): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

_CalculusFieldUnivariateVectorFunction__T = typing.TypeVar('_CalculusFieldUnivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateVectorFunction(typing.Generic[_CalculusFieldUnivariateVectorFunction__T]):
    """
    public interface CalculusFieldUnivariateVectorFunction<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>>
    
        An interface representing a univariate vectorial function for any field type.
    
        Since:
            1.3
    """
    def value(self, t: _CalculusFieldUnivariateVectorFunction__T) -> typing.List[_CalculusFieldUnivariateVectorFunction__T]:
        """
            Compute the value for the function.
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.CalculusFieldUnivariateVectorFunction`): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class FieldBivariateFunction:
    """
    public interface FieldBivariateFunction
    
        An interface representing a bivariate field function.
    
        Since:
            1.5
    """
    _toCalculusFieldBivariateFunction__T = typing.TypeVar('_toCalculusFieldBivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldBivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldBivariateFunction__T]) -> CalculusFieldBivariateFunction[_toCalculusFieldBivariateFunction__T]:
        """
            Convert to a :class:`~org.hipparchus.analysis.CalculusFieldBivariateFunction` with a specific type.
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field for the argument and value
        
            Returns:
                converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T, t2: _value__T) -> _value__T:
        """
            Compute the value for the function.
        
            Parameters:
                x (T): Abscissa for which the function value should be computed.
                y (T): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class FieldUnivariateFunction:
    """
    public interface FieldUnivariateFunction
    
        An interface representing a univariate real function for any field type.
    
        This interface is more general than :class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction` because the same
        instance can accept any field type, not just one.
    
        Since:
            1.3
    
        Also see:
            :class:`~org.hipparchus.analysis.UnivariateFunction`, :class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction`
    """
    _toCalculusFieldUnivariateFunction__T = typing.TypeVar('_toCalculusFieldUnivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateFunction__T]) -> CalculusFieldUnivariateFunction[_toCalculusFieldUnivariateFunction__T]:
        """
            Convert to a :class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction` with a specific type.
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field for the argument and value
        
            Returns:
                converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> _value__T:
        """
            Compute the value of the function.
        
            Parameters:
                x (T): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
            Raises:
                : when the activated method itself can ascertain that a precondition, specified in the API expressed at the level of the
                    activated method, has been violated. When Hipparchus throws an :code:`IllegalArgumentException`, it is usually the
                    consequence of checking the actual parameters passed to the method.
        
        
        """
        ...

class FieldUnivariateMatrixFunction:
    """
    public interface FieldUnivariateMatrixFunction
    
        An interface representing a univariate matrix function for any field type.
    
        Since:
            1.3
    """
    _toCalculusFieldUnivariateMatrixFunction__T = typing.TypeVar('_toCalculusFieldUnivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateMatrixFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateMatrixFunction__T]) -> CalculusFieldUnivariateMatrixFunction[_toCalculusFieldUnivariateMatrixFunction__T]:
        """
            Convert to a :class:`~org.hipparchus.analysis.CalculusFieldUnivariateMatrixFunction` with a specific type.
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field for the argument and value
        
            Returns:
                converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> typing.List[typing.List[_value__T]]:
        """
            Compute the value for the function.
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class FieldUnivariateVectorFunction:
    """
    public interface FieldUnivariateVectorFunction
    
        An interface representing a univariate vectorial function for any field type.
    
        Since:
            1.3
    """
    _toCalculusFieldUnivariateVectorFunction__T = typing.TypeVar('_toCalculusFieldUnivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateVectorFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateVectorFunction__T]) -> CalculusFieldUnivariateVectorFunction[_toCalculusFieldUnivariateVectorFunction__T]:
        """
            Convert to a :class:`~org.hipparchus.analysis.CalculusFieldUnivariateVectorFunction` with a specific type.
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field for the argument and value
        
            Returns:
                converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> typing.List[_value__T]:
        """
            Compute the value for the function.
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class FunctionUtils:
    """
    public class FunctionUtils extends Object
    
        Utilities for manipulating function objects.
    """
    @typing.overload
    @staticmethod
    def add(univariateFunctionArray: typing.List['UnivariateFunction']) -> 'UnivariateFunction':
        """
            Adds functions.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`...): List of functions.
        
            Returns:
                a function that computes the sum of the functions.
        
            Adds functions.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`...): List of functions.
        
            Returns:
                a function that computes the sum of the functions.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def add(univariateDifferentiableFunctionArray: typing.List[org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction]) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @typing.overload
    @staticmethod
    def collector(bivariateFunction: BivariateFunction, double: float) -> 'MultivariateFunction':
        """
            Returns a MultivariateFunction h(x[]) defined by
        
            .. code-block: java
            
             
             h(x[]) = combiner(...combiner(combiner(initialValue,f(x[0])),f(x[1]))...),f(x[x.length-1]))
             
        
            Parameters:
                combiner (:class:`~org.hipparchus.analysis.BivariateFunction`): Combiner function.
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function.
                initialValue (double): Initial value.
        
            Returns:
                a collector function.
        
            Returns a MultivariateFunction h(x[]) defined by
        
            .. code-block: java
            
             
             h(x[]) = combiner(...combiner(combiner(initialValue,x[0]),x[1])...),x[x.length-1])
             
        
            Parameters:
                combiner (:class:`~org.hipparchus.analysis.BivariateFunction`): Combiner function.
                initialValue (double): Initial value.
        
            Returns:
                a collector function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def collector(bivariateFunction: BivariateFunction, univariateFunction: 'UnivariateFunction', double: float) -> 'MultivariateFunction': ...
    @staticmethod
    def combine(bivariateFunction: BivariateFunction, univariateFunction: 'UnivariateFunction', univariateFunction2: 'UnivariateFunction') -> 'UnivariateFunction':
        """
            Returns the univariate function :code:`h(x) = combiner(f(x), g(x)).`
        
            Parameters:
                combiner (:class:`~org.hipparchus.analysis.BivariateFunction`): Combiner function.
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function.
                g (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function.
        
            Returns:
                the composite function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def compose(univariateFunctionArray: typing.List['UnivariateFunction']) -> 'UnivariateFunction':
        """
            Composes functions.
        
            The functions in the argument list are composed sequentially, in the given order. For example, compose(f1,f2,f3) acts
            like f1(f2(f3(x))).
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`...): List of functions.
        
            Returns:
                the composite function.
        
            Composes functions.
        
            The functions in the argument list are composed sequentially, in the given order. For example, compose(f1,f2,f3) acts
            like f1(f2(f3(x))).
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`...): List of functions.
        
            Returns:
                the composite function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def compose(univariateDifferentiableFunctionArray: typing.List[org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction]) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @typing.overload
    @staticmethod
    def derivative(multivariateDifferentiableFunction: org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction, intArray: typing.List[int]) -> 'MultivariateFunction':
        """
            Convert an :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction` to an
            :class:`~org.hipparchus.analysis.UnivariateFunction` computing n :sup:`th` order derivative.
        
            This converter is only a convenience method. Beware computing only one derivative does not save any computation as the
            original function will really be called under the hood. The derivative will be extracted from the full
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` result.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`): original function, with value and all its derivatives
                order (int): of the derivative to extract
        
            Returns:
                function computing the derivative at required order
        
            Also see:
                null, :meth:`~org.hipparchus.analysis.FunctionUtils.toDifferentiable`
        
            Convert an :class:`~org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction` to an
            :class:`~org.hipparchus.analysis.MultivariateFunction` computing n :sup:`th` order derivative.
        
            This converter is only a convenience method. Beware computing only one derivative does not save any computation as the
            original function will really be called under the hood. The derivative will be extracted from the full
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` result.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction`): original function, with value and all its derivatives
                orders (int[]): of the derivative to extract, for each free parameters
        
            Returns:
                function computing the derivative at required order
        
            Also see:
                :meth:`~org.hipparchus.analysis.FunctionUtils.derivative`,
                :meth:`~org.hipparchus.analysis.FunctionUtils.toDifferentiable`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def derivative(univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, int: int) -> 'UnivariateFunction': ...
    @staticmethod
    def fix1stArgument(bivariateFunction: BivariateFunction, double: float) -> 'UnivariateFunction':
        """
            Creates a unary function by fixing the first argument of a binary function.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.BivariateFunction`): Binary function.
                fixed (double): value to which the first argument of :code:`f` is set.
        
            Returns:
                the unary function h(x) = f(fixed, x)
        
        
        """
        ...
    @staticmethod
    def fix2ndArgument(bivariateFunction: BivariateFunction, double: float) -> 'UnivariateFunction':
        """
            Creates a unary function by fixing the second argument of a binary function.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.BivariateFunction`): Binary function.
                fixed (double): value to which the second argument of :code:`f` is set.
        
            Returns:
                the unary function h(x) = f(x, fixed)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiply(univariateFunctionArray: typing.List['UnivariateFunction']) -> 'UnivariateFunction':
        """
            Multiplies functions.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`...): List of functions.
        
            Returns:
                a function that computes the product of the functions.
        
            Multiplies functions.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`...): List of functions.
        
            Returns:
                a function that computes the product of the functions.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiply(univariateDifferentiableFunctionArray: typing.List[org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction]) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @staticmethod
    def sample(univariateFunction: 'UnivariateFunction', double: float, double2: float, int: int) -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def toDifferentiable(multivariateFunction: 'MultivariateFunction', multivariateVectorFunction: 'MultivariateVectorFunction') -> org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction:
        """
            Convert regular functions to :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`.
        
            This method handle the case with one free parameter and several derivatives. For the case with several free parameters
            and only first order derivatives, see :meth:`~org.hipparchus.analysis.FunctionUtils.toDifferentiable`. There are no
            direct support for intermediate cases, with several free parameters and order 2 or more derivatives, as is would be
            difficult to specify all the cross derivatives.
        
            Note that the derivatives are expected to be computed only with respect to the raw parameter x of the base function,
            i.e. they are df/dx, df :sup:`2` /dx :sup:`2` , ... Even if the built function is later used in a composition like
            f(sin(t)), the provided derivatives should *not* apply the composition with sine and its derivatives by themselves. The
            composition will be done automatically here and the result will properly contain f(sin(t)), df(sin(t))/dt, df :sup:`2`
            (sin(t))/dt :sup:`2` despite the provided derivatives functions know nothing about the sine function.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): base function f(x)
                derivatives (:class:`~org.hipparchus.analysis.UnivariateFunction`...): derivatives of the base function, in increasing differentiation order
        
            Returns:
                a differentiable function with value and all specified derivatives
        
            Also see:
                :meth:`~org.hipparchus.analysis.FunctionUtils.toDifferentiable`,
                :meth:`~org.hipparchus.analysis.FunctionUtils.derivative`
        
            Convert regular functions to :class:`~org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction`.
        
            This method handle the case with several free parameters and only first order derivatives. For the case with one free
            parameter and several derivatives, see :meth:`~org.hipparchus.analysis.FunctionUtils.toDifferentiable`. There are no
            direct support for intermediate cases, with several free parameters and order 2 or more derivatives, as is would be
            difficult to specify all the cross derivatives.
        
            Note that the gradient is expected to be computed only with respect to the raw parameter x of the base function, i.e. it
            is df/dx :sub:`1` , df/dx :sub:`2` , ... Even if the built function is later used in a composition like f(sin(t),
            cos(t)), the provided gradient should *not* apply the composition with sine or cosine and their derivative by itself.
            The composition will be done automatically here and the result will properly contain f(sin(t), cos(t)), df(sin(t),
            cos(t))/dt despite the provided derivatives functions know nothing about the sine or cosine functions.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.MultivariateFunction`): base function f(x)
                gradient (:class:`~org.hipparchus.analysis.MultivariateVectorFunction`): gradient of the base function
        
            Returns:
                a differentiable function with value and gradient
        
            Also see:
                :meth:`~org.hipparchus.analysis.FunctionUtils.toDifferentiable`, null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def toDifferentiable(univariateFunction: 'UnivariateFunction', univariateFunctionArray: typing.List['UnivariateFunction']) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...

class MultivariateFunction:
    """
    public interface MultivariateFunction
    
        An interface representing a multivariate real function.
    """
    def value(self, doubleArray: typing.List[float]) -> float:
        """
            Compute the value for the function at the given point.
        
            Parameters:
                point (double[]): Point at which the function must be evaluated.
        
            Returns:
                the function value for the given point.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the parameter's dimension is wrong for the function being evaluated.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: when the activated method itself can ascertain that preconditions, specified in the API expressed at the level of the
                    activated method, have been violated. In the vast majority of cases where Hipparchus throws this exception, it is the
                    result of argument checking of actual parameters immediately passed to a method.
        
        
        """
        ...

class MultivariateMatrixFunction:
    """
    public interface MultivariateMatrixFunction
    
        An interface representing a multivariate matrix function.
    """
    def value(self, doubleArray: typing.List[float]) -> typing.List[typing.List[float]]: ...

class MultivariateVectorFunction:
    """
    public interface MultivariateVectorFunction
    
        An interface representing a multivariate vectorial function.
    """
    def value(self, doubleArray: typing.List[float]) -> typing.List[float]: ...

class ParametricUnivariateFunction:
    """
    public interface ParametricUnivariateFunction
    
        An interface representing a real function that depends on one independent variable plus some extra parameters.
    """
    def gradient(self, double: float, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Compute the gradient of the function with respect to its parameters.
        
            Parameters:
                x (double): Point for which the function value should be computed.
                parameters (double...): Function parameters.
        
            Returns:
                the value.
        
        
        """
        ...
    def value(self, double: float, doubleArray: typing.List[float]) -> float:
        """
            Compute the value of the function.
        
            Parameters:
                x (double): Point for which the function value should be computed.
                parameters (double...): Function parameters.
        
            Returns:
                the value.
        
        
        """
        ...

class TrivariateFunction:
    """
    public interface TrivariateFunction
    
        An interface representing a trivariate real function.
    """
    def value(self, double: float, double2: float, double3: float) -> float:
        """
            Compute the value for the function.
        
            Parameters:
                x (double): x-coordinate for which the function value should be computed.
                y (double): y-coordinate for which the function value should be computed.
                z (double): z-coordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class UnivariateFunction:
    """
    public interface UnivariateFunction
    
        An interface representing a univariate real function.
    
        When a *user-defined* function encounters an error during evaluation, the
        :meth:`~org.hipparchus.analysis.UnivariateFunction.value` method should throw a *user-defined* unchecked exception.
    
        The following code excerpt shows the recommended way to do that using a root solver as an example, but the same
        construct is applicable to ODE integrators or optimizers.
    
        .. code-block: java
        
         private static class LocalException extends RuntimeException {
             // The x value that caused the problem.
             private final double x;
        
             public LocalException(double x) {
                 this.x = x;
             }
        
             public double getX() {
                 return x;
             }
         }
        
         private static class MyFunction implements UnivariateFunction {
             public double value(double x) {
                 double y = hugeFormula(x);
                 if (somethingBadHappens) {
                   throw new LocalException(x);
                 }
                 return y;
             }
         }
        
         public void compute() {
             try {
                 solver.solve(maxEval, new MyFunction(a, b, c), min, max);
             } catch (LocalException le) {
                 // Retrieve the x value.
             }
         }
         
        As shown, the exception is local to the user's code and it is guaranteed that Hipparchus will not catch it.
    """
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
            Raises:
                : when the activated method itself can ascertain that a precondition, specified in the API expressed at the level of the
                    activated method, has been violated. When Hipparchus throws an :code:`IllegalArgumentException`, it is usually the
                    consequence of checking the actual parameters passed to the method.
        
        
        """
        ...

class UnivariateMatrixFunction:
    """
    public interface UnivariateMatrixFunction
    
        An interface representing a univariate matrix function.
    """
    def value(self, double: float) -> typing.List[typing.List[float]]:
        """
            Compute the value for the function.
        
            Parameters:
                x (double): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class UnivariateVectorFunction:
    """
    public interface UnivariateVectorFunction
    
        An interface representing a univariate vectorial function.
    """
    def value(self, double: float) -> typing.List[float]:
        """
            Compute the value for the function.
        
            Parameters:
                x (double): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis")``.

    BivariateFunction: typing.Type[BivariateFunction]
    CalculusFieldBivariateFunction: typing.Type[CalculusFieldBivariateFunction]
    CalculusFieldUnivariateFunction: typing.Type[CalculusFieldUnivariateFunction]
    CalculusFieldUnivariateMatrixFunction: typing.Type[CalculusFieldUnivariateMatrixFunction]
    CalculusFieldUnivariateVectorFunction: typing.Type[CalculusFieldUnivariateVectorFunction]
    FieldBivariateFunction: typing.Type[FieldBivariateFunction]
    FieldUnivariateFunction: typing.Type[FieldUnivariateFunction]
    FieldUnivariateMatrixFunction: typing.Type[FieldUnivariateMatrixFunction]
    FieldUnivariateVectorFunction: typing.Type[FieldUnivariateVectorFunction]
    FunctionUtils: typing.Type[FunctionUtils]
    MultivariateFunction: typing.Type[MultivariateFunction]
    MultivariateMatrixFunction: typing.Type[MultivariateMatrixFunction]
    MultivariateVectorFunction: typing.Type[MultivariateVectorFunction]
    ParametricUnivariateFunction: typing.Type[ParametricUnivariateFunction]
    TrivariateFunction: typing.Type[TrivariateFunction]
    UnivariateFunction: typing.Type[UnivariateFunction]
    UnivariateMatrixFunction: typing.Type[UnivariateMatrixFunction]
    UnivariateVectorFunction: typing.Type[UnivariateVectorFunction]
    differentiation: org.hipparchus.analysis.differentiation.__module_protocol__
    function: org.hipparchus.analysis.function.__module_protocol__
    integration: org.hipparchus.analysis.integration.__module_protocol__
    interpolation: org.hipparchus.analysis.interpolation.__module_protocol__
    polynomials: org.hipparchus.analysis.polynomials.__module_protocol__
    solvers: org.hipparchus.analysis.solvers.__module_protocol__
