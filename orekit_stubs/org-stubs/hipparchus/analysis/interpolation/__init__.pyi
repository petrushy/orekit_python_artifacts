import java.io
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.differentiation
import org.hipparchus.analysis.polynomials
import org.hipparchus.random
import typing



class BicubicInterpolatingFunction(org.hipparchus.analysis.BivariateFunction):
    """
    public class BicubicInterpolatingFunction extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Function that implements the ` bicubic spline interpolation <http://en.wikipedia.org/wiki/Bicubic_interpolation>`.
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]], doubleArray4: typing.List[typing.List[float]], doubleArray5: typing.List[typing.List[float]], doubleArray6: typing.List[typing.List[float]]): ...
    def isValidPoint(self, double: float, double2: float) -> bool:
        """
            Indicates whether a point is within the interpolation range.
        
            Parameters:
                x (double): First coordinate.
                y (double): Second coordinate.
        
            Returns:
                :code:`true` if (x, y) is a valid point.
        
        
        """
        ...
    def value(self, double: float, double2: float) -> float: ...

class BilinearInterpolatingFunction(org.hipparchus.analysis.BivariateFunction, org.hipparchus.analysis.FieldBivariateFunction, java.io.Serializable):
    """
    public class BilinearInterpolatingFunction extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`, :class:`~org.hipparchus.analysis.FieldBivariateFunction`, Serializable
    
        Interpolate grid data using bi-linear interpolation.
    
        This interpolator is thread-safe.
    
        Since:
            1.4
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]]): ...
    def getXInf(self) -> float:
        """
            Get the lowest grid x coordinate.
        
            Returns:
                lowest grid x coordinate
        
        
        """
        ...
    def getXSup(self) -> float:
        """
            Get the highest grid x coordinate.
        
            Returns:
                highest grid x coordinate
        
        
        """
        ...
    def getYInf(self) -> float:
        """
            Get the lowest grid y coordinate.
        
            Returns:
                lowest grid y coordinate
        
        
        """
        ...
    def getYSup(self) -> float:
        """
            Get the highest grid y coordinate.
        
            Returns:
                highest grid y coordinate
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
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
    @typing.overload
    def value(self, t: _value_1__T, t2: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.FieldBivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.FieldBivariateFunction`
        
            Parameters:
                x (T): Abscissa for which the function value should be computed.
                y (T): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
            Since:
                1.5
        
        
        """
        ...

class BivariateGridInterpolator:
    """
    public interface BivariateGridInterpolator
    
        Interface representing a bivariate real interpolating function where the sample points must be specified on a regular
        grid.
    """
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]]) -> org.hipparchus.analysis.BivariateFunction: ...

_FieldHermiteInterpolator__T = typing.TypeVar('_FieldHermiteInterpolator__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldHermiteInterpolator(typing.Generic[_FieldHermiteInterpolator__T]):
    """
    public class FieldHermiteInterpolator<T extends :class:`~org.hipparchus.FieldElement`<T>> extends Object
    
        Polynomial interpolator using both sample values and sample derivatives.
    
        The interpolation polynomials match all sample points, including both values and provided derivatives. There is one
        polynomial for each component of the values vector. All polynomials have the same degree. The degree of the polynomials
        depends on the number of points and number of derivatives at each point. For example the interpolation polynomials for n
        sample points without any derivatives all have degree n-1. The interpolation polynomials for n sample points with the
        two extreme points having value and first derivative and the remaining points having value only all have degree n+1. The
        interpolation polynomial for n sample points with value, first and second derivative for all points all have degree
        3n-1.
    """
    def __init__(self): ...
    def addSamplePoint(self, t: _FieldHermiteInterpolator__T, tArray: typing.List[typing.List[_FieldHermiteInterpolator__T]]) -> None: ...
    def derivatives(self, t: _FieldHermiteInterpolator__T, int: int) -> typing.List[typing.List[_FieldHermiteInterpolator__T]]: ...
    def value(self, t: _FieldHermiteInterpolator__T) -> typing.List[_FieldHermiteInterpolator__T]: ...

class FieldUnivariateInterpolator:
    """
    public interface FieldUnivariateInterpolator
    
        Interface representing a univariate field interpolating function.
    
        Since:
            1.5
    """
    _interpolate__T = typing.TypeVar('_interpolate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def interpolate(self, tArray: typing.List[_interpolate__T], tArray2: typing.List[_interpolate__T]) -> org.hipparchus.analysis.CalculusFieldUnivariateFunction[_interpolate__T]: ...

class GridAxis(java.io.Serializable):
    def __init__(self, doubleArray: typing.List[float], int: int): ...
    def getN(self) -> int: ...
    def interpolationIndex(self, double: float) -> int: ...
    def node(self, int: int) -> float: ...
    def size(self) -> int: ...

class HermiteInterpolator(org.hipparchus.analysis.differentiation.UnivariateDifferentiableVectorFunction):
    """
    public class HermiteInterpolator extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableVectorFunction`
    
        Polynomial interpolator using both sample values and sample derivatives.
    
        The interpolation polynomials match all sample points, including both values and provided derivatives. There is one
        polynomial for each component of the values vector. All polynomials have the same degree. The degree of the polynomials
        depends on the number of points and number of derivatives at each point. For example the interpolation polynomials for n
        sample points without any derivatives all have degree n-1. The interpolation polynomials for n sample points with the
        two extreme points having value and first derivative and the remaining points having value only all have degree n+1. The
        interpolation polynomial for n sample points with value, first and second derivative for all points all have degree
        3n-1.
    """
    def __init__(self): ...
    def addSamplePoint(self, double: float, doubleArray: typing.List[typing.List[float]]) -> None: ...
    def derivatives(self, double: float, int: int) -> typing.List[typing.List[float]]: ...
    def getPolynomials(self) -> typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction]: ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> typing.List[float]: ...
    @typing.overload
    def value(self, t: _value_1__T) -> typing.List[_value_1__T]: ...

class InterpolatingMicrosphere:
    """
    public class InterpolatingMicrosphere extends Object
    
        Utility class for the :class:`~org.hipparchus.analysis.interpolation.MicrosphereProjectionInterpolator` algorithm.
    """
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, unitSphereRandomVectorGenerator: org.hipparchus.random.UnitSphereRandomVectorGenerator): ...
    def copy(self) -> 'InterpolatingMicrosphere':
        """
            Perform a copy.
        
            Returns:
                a copy of this instance.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the space dimensionality.
        
            Returns:
                the number of space dimensions.
        
        
        """
        ...
    def getSize(self) -> int:
        """
            Get the size of the sphere.
        
            Returns:
                the number of surface elements of the microspshere.
        
        
        """
        ...
    def value(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[float], double4: float, double5: float) -> float:
        """
            Estimate the value at the requested location. This microsphere is placed at the given :code:`point`, contribution of the
            given :code:`samplePoints` to each sphere facet is computed (illumination) and the interpolation is performed
            (integration of the illumination).
        
            Parameters:
                point (double[]): Interpolation point.
                samplePoints (double[][]): Sampling data points.
                sampleValues (double[]): Sampling data values at the corresponding :code:`samplePoints`.
                exponent (double): Exponent used in the power law that computes the weights (distance dimming factor) of the sample data.
                noInterpolationTolerance (double): When the distance between the :code:`point` and one of the :code:`samplePoints` is less than this value, no
                    interpolation will be performed, and the value of the sample will just be returned.
        
            Returns:
                the estimated value at the given :code:`point`.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`exponent < 0`.
        
        
        """
        ...

class MultivariateInterpolator:
    """
    public interface MultivariateInterpolator
    
        Interface representing a univariate real interpolating function.
    """
    def interpolate(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.MultivariateFunction: ...

class PiecewiseBicubicSplineInterpolatingFunction(org.hipparchus.analysis.BivariateFunction, org.hipparchus.analysis.FieldBivariateFunction):
    """
    public class PiecewiseBicubicSplineInterpolatingFunction extends Object implements :class:`~org.hipparchus.analysis.BivariateFunction`, :class:`~org.hipparchus.analysis.FieldBivariateFunction`
    
        Function that implements the `bicubic spline <http://www.paulinternet.nl/?page=bicubic>` interpolation. This
        implementation currently uses :class:`~org.hipparchus.analysis.interpolation.AkimaSplineInterpolator` as the underlying
        one-dimensional interpolator, which requires 5 sample points; insufficient data will raise an exception when the
        :meth:`~org.hipparchus.analysis.interpolation.PiecewiseBicubicSplineInterpolatingFunction.value` method is called.
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]]): ...
    def isValidPoint(self, double: float, double2: float) -> bool:
        """
            Indicates whether a point is within the interpolation range.
        
            Parameters:
                x (double): First coordinate.
                y (double): Second coordinate.
        
            Returns:
                :code:`true` if (x, y) is a valid point.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, double: float, double2: float) -> float: ...
    @typing.overload
    def value(self, t: _value_1__T, t2: _value_1__T) -> _value_1__T: ...

class TricubicInterpolatingFunction(org.hipparchus.analysis.TrivariateFunction):
    """
    public class TricubicInterpolatingFunction extends Object implements :class:`~org.hipparchus.analysis.TrivariateFunction`
    
        Function that implements the ` tricubic spline interpolation <http://en.wikipedia.org/wiki/Tricubic_interpolation>`, as
        proposed in
            Tricubic interpolation in three dimensions
    
    
            F. Lekien and J. Marsden
    
    
            *Int. J. Numer. Meth. Eng* 2005; **63**:455-471
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], doubleArray4: typing.List[typing.List[typing.List[float]]], doubleArray5: typing.List[typing.List[typing.List[float]]], doubleArray6: typing.List[typing.List[typing.List[float]]], doubleArray7: typing.List[typing.List[typing.List[float]]], doubleArray8: typing.List[typing.List[typing.List[float]]], doubleArray9: typing.List[typing.List[typing.List[float]]], doubleArray10: typing.List[typing.List[typing.List[float]]], doubleArray11: typing.List[typing.List[typing.List[float]]]): ...
    def isValidPoint(self, double: float, double2: float, double3: float) -> bool:
        """
            Indicates whether a point is within the interpolation range.
        
            Parameters:
                x (double): First coordinate.
                y (double): Second coordinate.
                z (double): Third coordinate.
        
            Returns:
                :code:`true` if (x, y, z) is a valid point.
        
        
        """
        ...
    def value(self, double: float, double2: float, double3: float) -> float: ...

class TrivariateGridInterpolator:
    """
    public interface TrivariateGridInterpolator
    
        Interface representing a trivariate real interpolating function where the sample points must be specified on a regular
        grid.
    """
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], doubleArray4: typing.List[typing.List[typing.List[float]]]) -> org.hipparchus.analysis.TrivariateFunction: ...

class UnivariateInterpolator:
    """
    public interface UnivariateInterpolator
    
        Interface representing a univariate real interpolating function.
    """
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.UnivariateFunction: ...

class AkimaSplineInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    """
    public class AkimaSplineInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, :class:`~org.hipparchus.analysis.interpolation.FieldUnivariateInterpolator`
    
        Computes a cubic spline interpolation for the data set using the Akima algorithm, as originally formulated by Hiroshi
        Akima in his 1970 paper "A New Method of Interpolation and Smooth Curve Fitting Based on Local Procedures." J. ACM 17, 4
        (October 1970), 589-602. DOI=10.1145/321607.321609 http://doi.acm.org/10.1145/321607.321609
    
        This implementation is based on the Akima implementation in the CubicSpline class in the Math.NET Numerics library. The
        method referenced is CubicSpline.InterpolateAkimaSorted
    
        The null method returns a :class:`~org.hipparchus.analysis.polynomials.PolynomialSplineFunction` consisting of n cubic
        polynomials, defined over the subintervals determined by the x values, :code:`x[0] < x[i] ... < x[n]`. The Akima
        algorithm requires that :code:`n >= 5`.
    """
    def __init__(self): ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.List[_interpolate_0__T], tArray2: typing.List[_interpolate_0__T]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class BicubicInterpolator(BivariateGridInterpolator):
    """
    public class BicubicInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.BivariateGridInterpolator`
    
        Generates a :class:`~org.hipparchus.analysis.interpolation.BicubicInterpolatingFunction`.
    
        Caveat: Because the interpolation scheme requires that derivatives be specified at the sample points, those are
        approximated with finite differences (using the 2-points symmetric formulae). Since their values are undefined at the
        borders of the provided interpolation ranges, the interpolated values will be wrong at the edges of the patch. The
        :code:`interpolate` method will return a function that overrides
        :meth:`~org.hipparchus.analysis.interpolation.BicubicInterpolatingFunction.isValidPoint` to indicate points where the
        interpolation will be inaccurate.
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]]) -> BicubicInterpolatingFunction: ...

class BilinearInterpolator(BivariateGridInterpolator):
    """
    public class BilinearInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.BivariateGridInterpolator`
    
        Interpolate grid data using bi-linear interpolation.
    
        Since:
            1.4
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]]) -> BilinearInterpolatingFunction: ...

class DividedDifferenceInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    public class DividedDifferenceInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, Serializable
    
        Implements the ` Divided Difference Algorithm
        <http://mathworld.wolfram.com/NewtonsDividedDifferenceInterpolationFormula.html>` for interpolation of real univariate
        functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 2.
    
        The actual code of Neville's evaluation is in PolynomialFunctionLagrangeForm, this class provides an easy-to-use
        interface to it.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.polynomials.PolynomialFunctionNewtonForm: ...

class InterpolatingMicrosphere2D(InterpolatingMicrosphere):
    """
    public class InterpolatingMicrosphere2D extends :class:`~org.hipparchus.analysis.interpolation.InterpolatingMicrosphere`
    
        Utility class for the :class:`~org.hipparchus.analysis.interpolation.MicrosphereProjectionInterpolator` algorithm. For
        2D interpolation, this class constructs the microsphere as a series of evenly spaced facets (rather than generating
        random normals as in the base implementation).
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def copy(self) -> 'InterpolatingMicrosphere2D':
        """
            Perform a copy.
        
            Overrides:
                :meth:`~org.hipparchus.analysis.interpolation.InterpolatingMicrosphere.copy`Â in
                classÂ :class:`~org.hipparchus.analysis.interpolation.InterpolatingMicrosphere`
        
            Returns:
                a copy of this instance.
        
        
        """
        ...

class LinearInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    """
    public class LinearInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, :class:`~org.hipparchus.analysis.interpolation.FieldUnivariateInterpolator`
    
        Implements a linear function for interpolation of real univariate functions.
    """
    def __init__(self): ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.List[_interpolate_0__T], tArray2: typing.List[_interpolate_0__T]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class LoessInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    public class LoessInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, Serializable
    
        Implements the ` Local Regression Algorithm <http://en.wikipedia.org/wiki/Local_regression>` (also Loess, Lowess) for
        interpolation of real univariate functions.
    
        For reference, see ` William S. Cleveland - Robust Locally Weighted Regression and Smoothing Scatterplots
        <http://amstat.tandfonline.com/doi/abs/10.1080/01621459.1979.10481038>`
    
        This class implements both the loess method and serves as an interpolation adapter to it, allowing one to build a spline
        on the obtained loess fit.
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_BANDWIDTH: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_BANDWIDTH
    
        Default value of the bandwidth parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_ROBUSTNESS_ITERS: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_ROBUSTNESS_ITERS
    
        Default value of the number of robustness iterations.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_ACCURACY: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ACCURACY
    
        Default value for accuracy.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...
    @typing.overload
    def smooth(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def smooth(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float]) -> typing.List[float]: ...

class MicrosphereProjectionInterpolator(MultivariateInterpolator):
    """
    public class MicrosphereProjectionInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.MultivariateInterpolator`
    
        Interpolator that implements the algorithm described in *William Dudziak*'s `MS thesis
        <http://www.dudziak.com/microsphere.pdf>`.
    """
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, boolean: bool, double5: float): ...
    @typing.overload
    def __init__(self, interpolatingMicrosphere: InterpolatingMicrosphere, double: float, boolean: bool, double2: float): ...
    def interpolate(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.MultivariateFunction: ...

class NevilleInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    public class NevilleInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, Serializable
    
        Implements the ` Neville's Algorithm <http://mathworld.wolfram.com/NevillesAlgorithm.html>` for interpolation of real
        univariate functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 2.
    
        The actual code of Neville's algorithm is in PolynomialFunctionLagrangeForm, this class provides an easy-to-use
        interface to it.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.polynomials.PolynomialFunctionLagrangeForm: ...

class PiecewiseBicubicSplineInterpolator(BivariateGridInterpolator):
    """
    public class PiecewiseBicubicSplineInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.BivariateGridInterpolator`
    
        Generates a piecewise-bicubic interpolating function.
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]]) -> PiecewiseBicubicSplineInterpolatingFunction: ...

class SplineInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    def __init__(self): ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.List[_interpolate_0__T], tArray2: typing.List[_interpolate_0__T]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class TricubicInterpolator(TrivariateGridInterpolator):
    """
    public class TricubicInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.TrivariateGridInterpolator`
    
        Generates a tricubic interpolating function.
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], doubleArray4: typing.List[typing.List[typing.List[float]]]) -> TricubicInterpolatingFunction: ...

class UnivariatePeriodicInterpolator(UnivariateInterpolator):
    """
    public class UnivariatePeriodicInterpolator extends Object implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`
    
        Adapter for classes implementing the :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator` interface.
        The data to be interpolated is assumed to be periodic. Thus values that are outside of the range can be passed to the
        interpolation function: They will be wrapped into the initial range before being passed to the class that actually
        computes the interpolation.
    """
    DEFAULT_EXTEND: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_EXTEND
    
        Default number of extension points of the samples array.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, univariateInterpolator: UnivariateInterpolator, double: float): ...
    @typing.overload
    def __init__(self, univariateInterpolator: UnivariateInterpolator, double: float, int: int): ...
    def interpolate(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.analysis.UnivariateFunction: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.interpolation")``.

    AkimaSplineInterpolator: typing.Type[AkimaSplineInterpolator]
    BicubicInterpolatingFunction: typing.Type[BicubicInterpolatingFunction]
    BicubicInterpolator: typing.Type[BicubicInterpolator]
    BilinearInterpolatingFunction: typing.Type[BilinearInterpolatingFunction]
    BilinearInterpolator: typing.Type[BilinearInterpolator]
    BivariateGridInterpolator: typing.Type[BivariateGridInterpolator]
    DividedDifferenceInterpolator: typing.Type[DividedDifferenceInterpolator]
    FieldHermiteInterpolator: typing.Type[FieldHermiteInterpolator]
    FieldUnivariateInterpolator: typing.Type[FieldUnivariateInterpolator]
    GridAxis: typing.Type[GridAxis]
    HermiteInterpolator: typing.Type[HermiteInterpolator]
    InterpolatingMicrosphere: typing.Type[InterpolatingMicrosphere]
    InterpolatingMicrosphere2D: typing.Type[InterpolatingMicrosphere2D]
    LinearInterpolator: typing.Type[LinearInterpolator]
    LoessInterpolator: typing.Type[LoessInterpolator]
    MicrosphereProjectionInterpolator: typing.Type[MicrosphereProjectionInterpolator]
    MultivariateInterpolator: typing.Type[MultivariateInterpolator]
    NevilleInterpolator: typing.Type[NevilleInterpolator]
    PiecewiseBicubicSplineInterpolatingFunction: typing.Type[PiecewiseBicubicSplineInterpolatingFunction]
    PiecewiseBicubicSplineInterpolator: typing.Type[PiecewiseBicubicSplineInterpolator]
    SplineInterpolator: typing.Type[SplineInterpolator]
    TricubicInterpolatingFunction: typing.Type[TricubicInterpolatingFunction]
    TricubicInterpolator: typing.Type[TricubicInterpolator]
    TrivariateGridInterpolator: typing.Type[TrivariateGridInterpolator]
    UnivariateInterpolator: typing.Type[UnivariateInterpolator]
    UnivariatePeriodicInterpolator: typing.Type[UnivariatePeriodicInterpolator]
