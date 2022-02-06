import org.hipparchus.analysis
import org.hipparchus.analysis.differentiation
import typing



class Abs(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Abs extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Absolute value function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Acos(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Acos extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Arc-cosine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Acosh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Acosh extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Hyperbolic arc-cosine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Add(org.hipparchus.analysis.BivariateFunction):
    """
    public class Add extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Add the two operands.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Asin(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Asin extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Arc-sine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Asinh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Asinh extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Hyperbolic arc-sine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Atan(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Atan extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Arc-tangent function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Atan2(org.hipparchus.analysis.BivariateFunction):
    """
    public class Atan2 extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Arc-tangent function.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Atanh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Atanh extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Hyperbolic arc-tangent function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Cbrt(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Cbrt extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Cube root function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Ceil(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Ceil extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        :code:`ceil` function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Constant(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Constant extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Constant function.
    """
    def __init__(self, double: float): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Cos(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Cos extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Cosine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Cosh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Cosh extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Hyperbolic cosine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Divide(org.hipparchus.analysis.BivariateFunction):
    """
    public class Divide extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Divide the first operand by the second.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Exp(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Exp extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Exponential function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Expm1(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Expm1 extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        :code:`e :sup:`x` -1` function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Floor(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Floor extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        :code:`floor` function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Gaussian(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Gaussian extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        ` Gaussian <http://en.wikipedia.org/wiki/Gaussian_function>` function.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        public <T extends :class:`~org.hipparchus.analysis.differentiation.Derivative`<T>> T value(T t) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x` does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                    example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, doubleArray: typing.List[float]) -> typing.List[float]: ...
        def value(self, double: float, doubleArray: typing.List[float]) -> float: ...

class HarmonicOscillator(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class HarmonicOscillator extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        ` simple harmonic oscillator <http://en.wikipedia.org/wiki/Harmonic_oscillator>` function.
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        public <T extends :class:`~org.hipparchus.analysis.differentiation.Derivative`<T>> T value(T t) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x` does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                    example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, doubleArray: typing.List[float]) -> typing.List[float]: ...
        def value(self, double: float, doubleArray: typing.List[float]) -> float: ...

class Identity(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Identity extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Identity function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Inverse(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Inverse extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Inverse function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Log(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Log extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Natural logarithm function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Log10(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Log10 extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Base 10 logarithm function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Log1p(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Log1p extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        :code:`log(1 + p)` function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Logistic(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Logistic extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        ` Generalised logistic <http://en.wikipedia.org/wiki/Generalised_logistic_function>` function.
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, doubleArray: typing.List[float]) -> typing.List[float]: ...
        def value(self, double: float, doubleArray: typing.List[float]) -> float: ...

class Logit(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Logit extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        ` Logit <http://en.wikipedia.org/wiki/Logit>` function. It is the inverse of the
        :class:`~org.hipparchus.analysis.function.Sigmoid` function.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float: ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, doubleArray: typing.List[float]) -> typing.List[float]: ...
        def value(self, double: float, doubleArray: typing.List[float]) -> float: ...

class Max(org.hipparchus.analysis.BivariateFunction):
    """
    public class Max extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Maximum function.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Min(org.hipparchus.analysis.BivariateFunction):
    """
    public class Min extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Minimum function.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Minus(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Minus extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Minus function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Multiply(org.hipparchus.analysis.BivariateFunction):
    """
    public class Multiply extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Multiply the two operands.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Pow(org.hipparchus.analysis.BivariateFunction):
    """
    public class Pow extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Power function.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Power(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Power extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Power function.
    """
    def __init__(self, double: float): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Rint(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Rint extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        :code:`rint` function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Sigmoid(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Sigmoid extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        ` Sigmoid <http://en.wikipedia.org/wiki/Sigmoid_function>` function. It is the inverse of the
        :class:`~org.hipparchus.analysis.function.Logit` function. A more flexible version, the generalised logistic, is
        implemented by the :class:`~org.hipparchus.analysis.function.Logistic` class.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        public <T extends :class:`~org.hipparchus.analysis.differentiation.Derivative`<T>> T value(T t) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x` does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                    example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, doubleArray: typing.List[float]) -> typing.List[float]: ...
        def value(self, double: float, doubleArray: typing.List[float]) -> float: ...

class Sin(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Sin extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Sine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Sinc(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Sinc extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        `Sinc <http://en.wikipedia.org/wiki/Sinc_function>` function, defined by
    
        .. code-block: java
        
           sinc(x) = 1            if x = 0,
                     sin(x) / x   otherwise.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        public <T extends :class:`~org.hipparchus.analysis.differentiation.Derivative`<T>> T value(T t) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x` does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                    example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...

class Sinh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Sinh extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Hyperbolic sine function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Sqrt(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Sqrt extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Square-root function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class StepFunction(org.hipparchus.analysis.UnivariateFunction):
    """
    public class StepFunction extends Object implements :class:`~org.hipparchus.analysis.UnivariateFunction`
    
        ` Step function <http://en.wikipedia.org/wiki/Step_function>`.
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        
        """
        ...

class Subtract(org.hipparchus.analysis.BivariateFunction):
    """
    public class Subtract extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Subtract the second operand from the first.
    """
    def __init__(self): ...
    def value(self, double: float, double2: float) -> float:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.BivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.BivariateFunction`
        
            Parameters:
                x (double): Abscissa for which the function value should be computed.
                y (double): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

class Tan(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Tan extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Tangent function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Tanh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    public class Tanh extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
    
        Hyperbolic tangent function.
    """
    def __init__(self): ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                x (T): the point for which the function value should be computed
        
            Returns:
                the value
        
        
        """
        ...

class Ulp(org.hipparchus.analysis.UnivariateFunction):
    """
    public class Ulp extends Object implements :class:`~org.hipparchus.analysis.UnivariateFunction`
    
        :code:`ulp` function.
    """
    def __init__(self): ...
    def value(self, double: float) -> float:
        """
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.function")``.

    Abs: typing.Type[Abs]
    Acos: typing.Type[Acos]
    Acosh: typing.Type[Acosh]
    Add: typing.Type[Add]
    Asin: typing.Type[Asin]
    Asinh: typing.Type[Asinh]
    Atan: typing.Type[Atan]
    Atan2: typing.Type[Atan2]
    Atanh: typing.Type[Atanh]
    Cbrt: typing.Type[Cbrt]
    Ceil: typing.Type[Ceil]
    Constant: typing.Type[Constant]
    Cos: typing.Type[Cos]
    Cosh: typing.Type[Cosh]
    Divide: typing.Type[Divide]
    Exp: typing.Type[Exp]
    Expm1: typing.Type[Expm1]
    Floor: typing.Type[Floor]
    Gaussian: typing.Type[Gaussian]
    HarmonicOscillator: typing.Type[HarmonicOscillator]
    Identity: typing.Type[Identity]
    Inverse: typing.Type[Inverse]
    Log: typing.Type[Log]
    Log10: typing.Type[Log10]
    Log1p: typing.Type[Log1p]
    Logistic: typing.Type[Logistic]
    Logit: typing.Type[Logit]
    Max: typing.Type[Max]
    Min: typing.Type[Min]
    Minus: typing.Type[Minus]
    Multiply: typing.Type[Multiply]
    Pow: typing.Type[Pow]
    Power: typing.Type[Power]
    Rint: typing.Type[Rint]
    Sigmoid: typing.Type[Sigmoid]
    Sin: typing.Type[Sin]
    Sinc: typing.Type[Sinc]
    Sinh: typing.Type[Sinh]
    Sqrt: typing.Type[Sqrt]
    StepFunction: typing.Type[StepFunction]
    Subtract: typing.Type[Subtract]
    Tan: typing.Type[Tan]
    Tanh: typing.Type[Tanh]
    Ulp: typing.Type[Ulp]
