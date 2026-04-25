
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
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
    An interface representing a bivariate real function.
    """
    def value(self, x: float, y: float) -> float:
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
    An interface representing a bivariate field function.
    
    Since:
        1.5
    """
    def value(self, x: _CalculusFieldBivariateFunction__T, y: _CalculusFieldBivariateFunction__T) -> _CalculusFieldBivariateFunction__T:
        """
        Compute the value for the function.
        
        Parameters:
            x (CalculusFieldBivariateFunction): Abscissa for which the function value should be computed.
            y (CalculusFieldBivariateFunction): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

_CalculusFieldMultivariateFunction__T = typing.TypeVar('_CalculusFieldMultivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldMultivariateFunction(typing.Generic[_CalculusFieldMultivariateFunction__T]):
    """
    An interface representing a scalar multivariate function.
    
    Since:
        2.2
    
          - MultivariateFunction
    """
    def value(self, *x: _CalculusFieldMultivariateFunction__T) -> _CalculusFieldMultivariateFunction__T:
        """
        Compute the value of the function.
        
        Parameters:
            x (CalculusFieldMultivariateFunction...): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...

_CalculusFieldMultivariateMatrixFunction__T = typing.TypeVar('_CalculusFieldMultivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldMultivariateMatrixFunction(typing.Generic[_CalculusFieldMultivariateMatrixFunction__T]):
    """
    An interface representing a matrix multivariate function.
    
    Since:
        2.2
    
          - MultivariateMatrixFunction
    """
    def value(self, *x: _CalculusFieldMultivariateMatrixFunction__T) -> typing.MutableSequence[typing.MutableSequence[_CalculusFieldMultivariateMatrixFunction__T]]:
        """
        Compute the value of the function.
        
        Parameters:
            x (CalculusFieldMultivariateMatrixFunction...): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...

_CalculusFieldMultivariateVectorFunction__T = typing.TypeVar('_CalculusFieldMultivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldMultivariateVectorFunction(typing.Generic[_CalculusFieldMultivariateVectorFunction__T]):
    """
    An interface representing a vector multivariate function.
    
    Since:
        2.2
    
          - MultivariateVectorFunction
    """
    def value(self, *x: _CalculusFieldMultivariateVectorFunction__T) -> typing.MutableSequence[_CalculusFieldMultivariateVectorFunction__T]:
        """
        Compute the value of the function.
        
        Parameters:
            x (CalculusFieldMultivariateVectorFunction...): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...

_CalculusFieldUnivariateFunction__T = typing.TypeVar('_CalculusFieldUnivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateFunction(typing.Generic[_CalculusFieldUnivariateFunction__T]):
    """
    An interface representing a univariate real function.
    
    When a user-defined function encounters an error during evaluation, the value method should throw a user-defined unchecked exception.
    
    The following code excerpt shows the recommended way to do that using a root solver as an example, but the same construct is applicable to ODE integrators or optimizers.
    
    
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
    
          - UnivariateFunction
          - FieldUnivariateFunction
    """
    def value(self, x: _CalculusFieldUnivariateFunction__T) -> _CalculusFieldUnivariateFunction__T:
        """
        Compute the value of the function.
        
        Parameters:
            x (CalculusFieldUnivariateFunction): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        Raises:
            IllegalArgumentException: when the activated method itself can ascertain that a precondition, specified in the API expressed at the level of the
                activated method, has been violated. When Hipparchus throws an IllegalArgumentException, it is usually the
                consequence of checking the actual parameters passed to the method.
        
        
        """
        ...

_CalculusFieldUnivariateMatrixFunction__T = typing.TypeVar('_CalculusFieldUnivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateMatrixFunction(typing.Generic[_CalculusFieldUnivariateMatrixFunction__T]):
    """
    An interface representing a univariate matrix function.
    
    Since:
        1.3
    """
    def value(self, x: _CalculusFieldUnivariateMatrixFunction__T) -> typing.MutableSequence[typing.MutableSequence[_CalculusFieldUnivariateMatrixFunction__T]]:
        """
        Compute the value for the function.
        
        Parameters:
            x (CalculusFieldUnivariateMatrixFunction): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

_CalculusFieldUnivariateVectorFunction__T = typing.TypeVar('_CalculusFieldUnivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateVectorFunction(typing.Generic[_CalculusFieldUnivariateVectorFunction__T]):
    """
    An interface representing a univariate vectorial function for any field type.
    
    Since:
        1.3
    """
    def value(self, x: _CalculusFieldUnivariateVectorFunction__T) -> typing.MutableSequence[_CalculusFieldUnivariateVectorFunction__T]:
        """
        Compute the value for the function.
        
        Parameters:
            x (CalculusFieldUnivariateVectorFunction): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class FieldBivariateFunction:
    """
    An interface representing a bivariate field function.
    
    Since:
        1.5
    """
    _toCalculusFieldBivariateFunction__T = typing.TypeVar('_toCalculusFieldBivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldBivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldBivariateFunction__T]) -> CalculusFieldBivariateFunction[_toCalculusFieldBivariateFunction__T]:
        """
        Convert to a CalculusFieldBivariateFunction with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, x: _value__T, y: _value__T) -> _value__T:
        """
        Compute the value for the function.
        
        Parameters:
            x (T): Abscissa for which the function value should be computed.
            y (T): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class FieldMultivariateFunction:
    """
    An interface representing a scalar multivariate function for any field type.
    
    Since:
        2.2
    
          - MultivariateFunction
    """
    _toCalculusFieldMultivariateFunction__T = typing.TypeVar('_toCalculusFieldMultivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldMultivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldMultivariateFunction__T]) -> CalculusFieldMultivariateFunction[_toCalculusFieldMultivariateFunction__T]:
        """
        Convert to a CalculusFieldMultivariateFunction with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, *x: _value__T) -> _value__T:
        """
        Compute the value of the function.
        
        Parameters:
            x (T...): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...

class FieldMultivariateMatrixFunction:
    """
    An interface representing a matrix multivariate function for any field type.
    
    Since:
        2.2
    
          - MultivariateMatrixFunction
    """
    _toCalculusFieldMultivariateMatrixFunction__T = typing.TypeVar('_toCalculusFieldMultivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldMultivariateMatrixFunction(self, field: org.hipparchus.Field[_toCalculusFieldMultivariateMatrixFunction__T]) -> CalculusFieldMultivariateMatrixFunction[_toCalculusFieldMultivariateMatrixFunction__T]:
        """
        Convert to a CalculusFieldMultivariateMatrixFunction with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, *x: _value__T) -> typing.MutableSequence[typing.MutableSequence[_value__T]]:
        """
        Compute the value of the function.
        
        Parameters:
            x (T...): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...

class FieldMultivariateVectorFunction:
    """
    An interface representing a vector multivariate function for any field type.
    
    Since:
        2.2
    
          - MultivariateVectorFunction
    """
    _toCalculusFieldMultivariateVectorFunction__T = typing.TypeVar('_toCalculusFieldMultivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldMultivariateVectorFunction(self, field: org.hipparchus.Field[_toCalculusFieldMultivariateVectorFunction__T]) -> CalculusFieldMultivariateVectorFunction[_toCalculusFieldMultivariateVectorFunction__T]:
        """
        Convert to a CalculusFieldMultivariateVectorFunction with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, *x: _value__T) -> typing.MutableSequence[_value__T]:
        """
        Compute the value of the function.
        
        Parameters:
            x (T...): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...

class FieldUnivariateFunction:
    """
    An interface representing a univariate real function for any field type.
    
    This interface is more general than CalculusFieldUnivariateFunction because the same instance can accept any field type, not just one.
    
    Since:
        1.3
    
          - UnivariateFunction
          - CalculusFieldUnivariateFunction
    """
    _toCalculusFieldUnivariateFunction__T = typing.TypeVar('_toCalculusFieldUnivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateFunction__T]) -> CalculusFieldUnivariateFunction[_toCalculusFieldUnivariateFunction__T]:
        """
        Convert to a CalculusFieldUnivariateFunction with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, x: _value__T) -> _value__T:
        """
        Compute the value of the function.
        
        Parameters:
            x (T): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        Raises:
            IllegalArgumentException: when the activated method itself can ascertain that a precondition, specified in the API expressed at the level of the
                activated method, has been violated. When Hipparchus throws an IllegalArgumentException, it is usually the
                consequence of checking the actual parameters passed to the method.
        
        
        """
        ...

class FieldUnivariateMatrixFunction:
    """
    An interface representing a univariate matrix function for any field type.
    
    Since:
        1.3
    """
    _toCalculusFieldUnivariateMatrixFunction__T = typing.TypeVar('_toCalculusFieldUnivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateMatrixFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateMatrixFunction__T]) -> CalculusFieldUnivariateMatrixFunction[_toCalculusFieldUnivariateMatrixFunction__T]:
        """
        Convert to a CalculusFieldUnivariateMatrixFunction with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, x: _value__T) -> typing.MutableSequence[typing.MutableSequence[_value__T]]:
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
    An interface representing a univariate vectorial function for any field type.
    
    Since:
        1.3
    """
    _toCalculusFieldUnivariateVectorFunction__T = typing.TypeVar('_toCalculusFieldUnivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateVectorFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateVectorFunction__T]) -> CalculusFieldUnivariateVectorFunction[_toCalculusFieldUnivariateVectorFunction__T]:
        """
        Convert to a CalculusFieldUnivariateVectorFunction with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, x: _value__T) -> typing.MutableSequence[_value__T]:
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
    Utilities for manipulating function objects.
    """
    @typing.overload
    @staticmethod
    def add(*univariateFunction: typing.Union['UnivariateFunction', typing.Callable]) -> 'UnivariateFunction':
        """
        Adds functions.
        
        Parameters:
            f (UnivariateFunction...): List of functions.
        
        Returns:
            a function that computes the sum of the functions.
        
        Adds functions.
        
        Parameters:
            f (UnivariateDifferentiableFunction...): List of functions.
        
        Returns:
            a function that computes the sum of the functions.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def add(*univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @typing.overload
    @staticmethod
    def collector(bivariateFunction: typing.Union[BivariateFunction, typing.Callable], double: float) -> 'MultivariateFunction':
        """
         h(x[]) = combiner(...combiner(combiner(initialValue,f(x[0])),f(x[1]))...),f(x[x.length-1]))
        
        Parameters:
            combiner (BivariateFunction): Combiner function.
            f (UnivariateFunction): Function.
            initialValue (double): Initial value.
        
        Returns:
            a collector function.
        
        Returns a MultivariateFunction h(x[]) defined by
        
         h(x[]) = combiner(...combiner(combiner(initialValue,x[0]),x[1])...),x[x.length-1])
        
        Parameters:
            combiner (BivariateFunction): Combiner function.
            initialValue (double): Initial value.
        
        Returns:
            a collector function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def collector(bivariateFunction: typing.Union[BivariateFunction, typing.Callable], univariateFunction: typing.Union['UnivariateFunction', typing.Callable], double: float) -> 'MultivariateFunction': ...
    @staticmethod
    def combine(combiner: typing.Union[BivariateFunction, typing.Callable], f: typing.Union['UnivariateFunction', typing.Callable], g: typing.Union['UnivariateFunction', typing.Callable]) -> 'UnivariateFunction':
        """
        Returns the univariate function h(x) = combiner(f(x), g(x))
        
        Parameters:
            combiner (BivariateFunction): Combiner function.
            f (UnivariateFunction): Function.
            g (UnivariateFunction): Function.
        
        Returns:
            the composite function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def compose(*univariateFunction: typing.Union['UnivariateFunction', typing.Callable]) -> 'UnivariateFunction':
        """
        Composes functions.
        
        The functions in the argument list are composed sequentially, in the given order. For example, compose(f1,f2,f3) acts like f1(f2(f3(x))).
        
        Parameters:
            f (UnivariateFunction...): List of functions.
        
        Returns:
            the composite function.
        
        Composes functions.
        
        The functions in the argument list are composed sequentially, in the given order. For example, compose(f1,f2,f3) acts like f1(f2(f3(x))).
        
        Parameters:
            f (UnivariateDifferentiableFunction...): List of functions.
        
        Returns:
            the composite function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def compose(*univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @typing.overload
    @staticmethod
    def derivative(multivariateDifferentiableFunction: org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction, intArray: typing.Union[typing.List[int], jpype.JArray]) -> 'MultivariateFunction':
        """
        Convert an UnivariateDifferentiableFunction to an UnivariateFunction computing n :sup:`th` order derivative.
        
        This converter is only a convenience method. Beware computing only one derivative does not save any computation as the original function will really be called under the hood. The derivative will be extracted from the full DerivativeStructure result.
        
        Parameters:
            f (UnivariateDifferentiableFunction): original function, with value and all its derivatives
            order (int): of the derivative to extract
        
        Returns:
            function computing the derivative at required order
        
              - derivative
              - toDifferentiable
        
        Convert an MultivariateDifferentiableFunction to an MultivariateFunction computing n :sup:`th` order derivative.
        
        This converter is only a convenience method. Beware computing only one derivative does not save any computation as the original function will really be called under the hood. The derivative will be extracted from the full DerivativeStructure result.
        
        Parameters:
            f (MultivariateDifferentiableFunction): original function, with value and all its derivatives
            orders (int[]): of the derivative to extract, for each free parameters
        
        Returns:
            function computing the derivative at required order
        
              - derivative
              - toDifferentiable
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def derivative(univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, int: int) -> 'UnivariateFunction': ...
    @staticmethod
    def fix1stArgument(f: typing.Union[BivariateFunction, typing.Callable], fixed: float) -> 'UnivariateFunction':
        """
        Creates a unary function by fixing the first argument of a binary function.
        
        Parameters:
            f (BivariateFunction): Binary function.
            fixed (double): value to which the first argument of f is set.
        
        Returns:
            the unary function h(x) = f(fixed, x)
        
        
        """
        ...
    @staticmethod
    def fix2ndArgument(f: typing.Union[BivariateFunction, typing.Callable], fixed: float) -> 'UnivariateFunction':
        """
        Creates a unary function by fixing the second argument of a binary function.
        
        Parameters:
            f (BivariateFunction): Binary function.
            fixed (double): value to which the second argument of f is set.
        
        Returns:
            the unary function h(x) = f(x, fixed)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiply(*univariateFunction: typing.Union['UnivariateFunction', typing.Callable]) -> 'UnivariateFunction':
        """
        Multiplies functions.
        
        Parameters:
            f (UnivariateFunction...): List of functions.
        
        Returns:
            a function that computes the product of the functions.
        
        Multiplies functions.
        
        Parameters:
            f (UnivariateDifferentiableFunction...): List of functions.
        
        Returns:
            a function that computes the product of the functions.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiply(*univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @staticmethod
    def sample(f: typing.Union['UnivariateFunction', typing.Callable], min: float, max: float, n: int) -> typing.MutableSequence[float]:
        """
        Samples the specified univariate real function on the specified interval.
        
        The interval is divided equally into n sections and sample points are taken from min to max - (max - min) / n; therefore f is not sampled at the upper bound max.
        
        Parameters:
            f (UnivariateFunction): Function to be sampled
            min (double): Lower bound of the interval (included).
            max (double): Upper bound of the interval (excluded).
            n (int): Number of sample points.
        
        Returns:
            the array of samples.
        
        Raises:
            MathIllegalArgumentException: if the lower bound min is greater than, or equal to the upper bound max.
            MathIllegalArgumentException: if the number of sample points n is negative.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def toDifferentiable(multivariateFunction: typing.Union['MultivariateFunction', typing.Callable], multivariateVectorFunction: typing.Union['MultivariateVectorFunction', typing.Callable]) -> org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction:
        """
        Convert regular functions to UnivariateDifferentiableFunction.
        
        This method handle the case with one free parameter and several derivatives. For the case with several free parameters and only first order derivatives, see toDifferentiable. There are no direct support for intermediate cases, with several free parameters and order 2 or more derivatives, as is would be difficult to specify all the cross derivatives.
        
        Note that the derivatives are expected to be computed only with respect to the raw parameter x of the base function, i.e. they are df/dx, df :sup:`2` /dx :sup:`2` ... Even if the built function is later used in a composition like f(sin(t)), the provided derivatives should not apply the composition with sine and its derivatives by themselves. The composition will be done automatically here and the result will properly contain f(sin(t)), df(sin(t))/dt, df :sup:`2` (sin(t))/dt :sup:`2` despite the provided derivatives functions know nothing about the sine function.
        
        Parameters:
            f (UnivariateFunction): base function f(x)
            derivatives (UnivariateFunction...): derivatives of the base function, in increasing differentiation order
        
        Returns:
            a differentiable function with value and all specified derivatives
        
              - toDifferentiable
              - derivative
        
        Convert regular functions to MultivariateDifferentiableFunction.
        
        This method handle the case with several free parameters and only first order derivatives. For the case with one free parameter and several derivatives, see toDifferentiable. There are no direct support for intermediate cases, with several free parameters and order 2 or more derivatives, as is would be difficult to specify all the cross derivatives.
        
        Note that the gradient is expected to be computed only with respect to the raw parameter x of the base function, i.e. it is df/dx :sub:`1` , df/dx :sub:`2` ... Even if the built function is later used in a composition like f(sin(t), cos(t)), the provided gradient should not apply the composition with sine or cosine and their derivative by itself. The composition will be done automatically here and the result will properly contain f(sin(t), cos(t)), df(sin(t), cos(t))/dt despite the provided derivatives functions know nothing about the sine or cosine functions.
        
        Parameters:
            f (MultivariateFunction): base function f(x)
            gradient (MultivariateVectorFunction): gradient of the base function
        
        Returns:
            a differentiable function with value and gradient
        
              - toDifferentiable
              - derivative
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def toDifferentiable(univariateFunction: typing.Union['UnivariateFunction', typing.Callable], *univariateFunction2: typing.Union['UnivariateFunction', typing.Callable]) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...

class MultivariateFunction:
    """
    An interface representing a multivariate real function.
    """
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the value for the function at the given point.
        
        Parameters:
            point (double[]): Point at which the function must be evaluated.
        
        Returns:
            the function value for the given point.
        
        Raises:
            MathIllegalArgumentException: if the parameter's dimension is wrong for the function being evaluated.
            MathIllegalArgumentException: when the activated method itself can ascertain that preconditions, specified in the API expressed at the level of the
                activated method, have been violated. In the vast majority of cases where Hipparchus throws this exception, it is the
                result of argument checking of actual parameters immediately passed to a method.
        
        
        """
        ...

class MultivariateMatrixFunction:
    """
    An interface representing a multivariate matrix function.
    """
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the value for the function at the given point.
        
        Parameters:
            point (double[]): point at which the function must be evaluated
        
        Returns:
            function value for the given point
        
        Raises:
            IllegalArgumentException: if point's dimension is wrong
        
        
        """
        ...

class MultivariateVectorFunction:
    """
    An interface representing a multivariate vectorial function.
    """
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Compute the value for the function at the given point.
        
        Parameters:
            point (double[]): point at which the function must be evaluated
        
        Returns:
            function value for the given point
        
        Raises:
            IllegalArgumentException: if point's dimension is wrong
        
        
        """
        ...

class ParametricUnivariateFunction:
    """
    An interface representing a real function that depends on one independent variable plus some extra parameters.
    """
    def gradient(self, x: float, *parameters: float) -> typing.MutableSequence[float]:
        """
        Compute the gradient of the function with respect to its parameters.
        
        Parameters:
            x (double): Point for which the function value should be computed.
            parameters (double...): Function parameters.
        
        Returns:
            the value.
        
        
        """
        ...
    def value(self, x: float, *parameters: float) -> float:
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
    An interface representing a trivariate real function.
    """
    def value(self, x: float, y: float, z: float) -> float:
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
    An interface representing a univariate real function.
    
    When a user-defined function encounters an error during evaluation, the value method should throw a user-defined unchecked exception.
    
    The following code excerpt shows the recommended way to do that using a root solver as an example, but the same construct is applicable to ODE integrators or optimizers.
    
    
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
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        Raises:
            IllegalArgumentException: when the activated method itself can ascertain that a precondition, specified in the API expressed at the level of the
                activated method, has been violated. When Hipparchus throws an IllegalArgumentException, it is usually the
                consequence of checking the actual parameters passed to the method.
        
        
        """
        ...

class UnivariateMatrixFunction:
    """
    An interface representing a univariate matrix function.
    """
    def value(self, x: float) -> typing.MutableSequence[typing.MutableSequence[float]]:
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
    An interface representing a univariate vectorial function.
    """
    def value(self, x: float) -> typing.MutableSequence[float]:
        """
        Compute the value for the function.
        
        Parameters:
            x (double): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class PythonFieldUnivariateFunction(FieldUnivariateFunction):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> _value__T:
        """
        Specified by: meth:`~org.hipparchus.analysis.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.FieldUnivariateFunction.html?is` in interface FieldUnivariateFunction
        
        
        """
        ...

class PythonUnivariateFunction(UnivariateFunction):
    """
    import org.hipparchus.analysis.UnivariateFunction;
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def value(self, double: float) -> float:
        """
        Specified by: meth:`~org.hipparchus.analysis.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.UnivariateFunction.html?is` in interface UnivariateFunction
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis")``.

    BivariateFunction: typing.Type[BivariateFunction]
    CalculusFieldBivariateFunction: typing.Type[CalculusFieldBivariateFunction]
    CalculusFieldMultivariateFunction: typing.Type[CalculusFieldMultivariateFunction]
    CalculusFieldMultivariateMatrixFunction: typing.Type[CalculusFieldMultivariateMatrixFunction]
    CalculusFieldMultivariateVectorFunction: typing.Type[CalculusFieldMultivariateVectorFunction]
    CalculusFieldUnivariateFunction: typing.Type[CalculusFieldUnivariateFunction]
    CalculusFieldUnivariateMatrixFunction: typing.Type[CalculusFieldUnivariateMatrixFunction]
    CalculusFieldUnivariateVectorFunction: typing.Type[CalculusFieldUnivariateVectorFunction]
    FieldBivariateFunction: typing.Type[FieldBivariateFunction]
    FieldMultivariateFunction: typing.Type[FieldMultivariateFunction]
    FieldMultivariateMatrixFunction: typing.Type[FieldMultivariateMatrixFunction]
    FieldMultivariateVectorFunction: typing.Type[FieldMultivariateVectorFunction]
    FieldUnivariateFunction: typing.Type[FieldUnivariateFunction]
    FieldUnivariateMatrixFunction: typing.Type[FieldUnivariateMatrixFunction]
    FieldUnivariateVectorFunction: typing.Type[FieldUnivariateVectorFunction]
    FunctionUtils: typing.Type[FunctionUtils]
    MultivariateFunction: typing.Type[MultivariateFunction]
    MultivariateMatrixFunction: typing.Type[MultivariateMatrixFunction]
    MultivariateVectorFunction: typing.Type[MultivariateVectorFunction]
    ParametricUnivariateFunction: typing.Type[ParametricUnivariateFunction]
    PythonFieldUnivariateFunction: typing.Type[PythonFieldUnivariateFunction]
    PythonUnivariateFunction: typing.Type[PythonUnivariateFunction]
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
