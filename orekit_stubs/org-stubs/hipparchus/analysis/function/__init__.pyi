
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus.analysis
import org.hipparchus.analysis.differentiation
import typing



class Abs(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Absolute value function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Acos(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Arc-cosine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Acosh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Hyperbolic arc-cosine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Add(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Add the two operands.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Asin(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Arc-sine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Asinh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Hyperbolic arc-sine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Atan(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Arc-tangent function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Atan2(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Arc-tangent function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Atanh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Hyperbolic arc-tangent function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Cbrt(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Cube root function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Ceil(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    ceil function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Constant(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Constant function.
    """
    def __init__(self, c: float):
        """
        Simple constructor.
        
        Parameters:
            c (double): Constant.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
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
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Cos(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Cosine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Cosh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Hyperbolic cosine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Divide(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Divide the first operand by the second.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Exp(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Exponential function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Expm1(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    x` -1` function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Floor(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    floor function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Gaussian(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
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
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        public <T extends Derivative<T>> T value(T t) throws MathIllegalArgumentException
        
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        Raises:
            MathIllegalArgumentException: if x does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, *double2: float) -> typing.MutableSequence[float]: ...
        def value(self, double: float, *double2: float) -> float: ...

class HarmonicOscillator(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    ` simple harmonic oscillator <http://en.wikipedia.org/wiki/Harmonic_oscillator>` function.
    """
    def __init__(self, amplitude: float, omega: float, phase: float):
        """
        Harmonic oscillator function.
        
        Parameters:
            amplitude (double): Amplitude.
            omega (double): Angular frequency.
            phase (double): Phase.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        public <T extends Derivative<T>> T value(T t) throws MathIllegalArgumentException
        
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        Raises:
            MathIllegalArgumentException: if x does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, *double2: float) -> typing.MutableSequence[float]: ...
        def value(self, double: float, *double2: float) -> float: ...

class Identity(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Identity function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
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
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Inverse(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Inverse function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
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
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Log(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Natural logarithm function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Log10(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Base 10 logarithm function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Log1p(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    log(1 + p) function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Logistic(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    ` Generalised logistic <http://en.wikipedia.org/wiki/Generalised_logistic_function>` function.
    """
    def __init__(self, k: float, m: float, b: float, q: float, a: float, n: float):
        """
        Simple constructor.
        
        Parameters:
            k (double): If b > 0, value of the function for x going towards +∞. If b < 0, value of the function for x going
                towards -∞.
            m (double): Abscissa of maximum growth.
            b (double): Growth rate.
            q (double): Parameter that affects the position of the curve along the ordinate axis.
            a (double): If b > 0, value of the function for x going towards -∞. If b < 0, value of the function for x going
                towards +∞.
            n (double): Parameter that affects near which asymptote the maximum growth occurs.
        
        Raises:
            MathIllegalArgumentException: if n <= 0.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
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
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, *double2: float) -> typing.MutableSequence[float]: ...
        def value(self, double: float, *double2: float) -> float: ...

class Logit(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    ` Logit <http://en.wikipedia.org/wiki/Logit>` function. It is the inverse of the Sigmoid function.
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
        def gradient(self, double: float, *double2: float) -> typing.MutableSequence[float]: ...
        def value(self, double: float, *double2: float) -> float: ...

class Max(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Maximum function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Min(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Minimum function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Minus(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Minus function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
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
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Multiply(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Multiply the two operands.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Pow(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Power function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Power(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Power function.
    """
    def __init__(self, p: float):
        """
        Simple constructor.
        
        Parameters:
            p (double): Power.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
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
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Rint(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    rint function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Sigmoid(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    ` Sigmoid <http://en.wikipedia.org/wiki/Sigmoid_function>` function. It is the inverse of the Logit function. A more flexible version, the generalised logistic, is implemented by the Logistic class.
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
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        public <T extends Derivative<T>> T value(T t) throws MathIllegalArgumentException
        
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        Raises:
            MathIllegalArgumentException: if x does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, *double2: float) -> typing.MutableSequence[float]: ...
        def value(self, double: float, *double2: float) -> float: ...

class Sin(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Sine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Sinc(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    `Sinc <http://en.wikipedia.org/wiki/Sinc_function>` function, defined by
    
       sinc(x) = 1            if x = 0, sin(x) / x   otherwise.
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
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        public <T extends Derivative<T>> T value(T t) throws MathIllegalArgumentException
        
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        Raises:
            MathIllegalArgumentException: if x does not satisfy the function's constraints (argument out of bound, or unsupported derivative order for
                example)
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...

class Sinh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Hyperbolic sine function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Sqrt(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Square-root function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class StepFunction(org.hipparchus.analysis.UnivariateFunction):
    """
    implements UnivariateFunction
    
    ` Step function <http://en.wikipedia.org/wiki/Step_function>`.
    """
    def __init__(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]):
        """
        Builds a step function from a list of arguments and the corresponding values. Specifically, returns the function h(x) defined by
        
         h(x) = y[0] for all x < x[1] y[1] for x[1] ≤ x < x[2] ... y[y.length - 1] for x ≥ x[x.length - 1] The value of x[0] is ignored, but it must be strictly less than x[1].
        
        Parameters:
            x (double[]): Domain values where the function changes value.
            y (double[]): Values of the function.
        
        Raises:
            MathIllegalArgumentException: if the x array is not sorted in strictly increasing order.
            NullArgumentException: if x or y are null.
            MathIllegalArgumentException: if x or y are zero-length.
            MathIllegalArgumentException: if x and y do not have the same length.
        
        
        """
        ...
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...

class Subtract(org.hipparchus.analysis.BivariateFunction):
    """
    implements BivariateFunction
    
    Subtract the second operand from the first.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float, y: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface BivariateFunction
        
        Parameters:
            x (double): Abscissa for which the function value should be computed.
            y (double): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

class Tan(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Tangent function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Tanh(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction):
    """
    implements UnivariateDifferentiableFunction
    
    Hyperbolic tangent function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        """
        ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            x (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        
        """
        ...

class Ulp(org.hipparchus.analysis.UnivariateFunction):
    """
    implements UnivariateFunction
    
    ulp function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def value(self, x: float) -> float:
        """
        Compute the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        
        """
        ...


class __module_protocol__(Protocol):
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
