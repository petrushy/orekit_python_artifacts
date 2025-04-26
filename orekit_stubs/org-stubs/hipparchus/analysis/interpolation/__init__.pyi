
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.differentiation
import org.hipparchus.analysis.polynomials
import org.hipparchus.random
import typing



class BicubicInterpolatingFunction(org.hipparchus.analysis.BivariateFunction):
    """
    public classBicubicInterpolatingFunction extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.BivariateFunction`
    
        Function that implements the ` bicubic spline interpolation <http://en.wikipedia.org/wiki/Bicubic_interpolation>`.
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray4: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray5: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray6: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
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
    public classBilinearInterpolatingFunction extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.BivariateFunction`, :class:`~org.hipparchus.analysis.FieldBivariateFunction`, :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Interpolate grid data using bi-linear interpolation.
    
        This interpolator is thread-safe.
    
        Since:
            1.4
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
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
                :meth:`~org.hipparchus.analysis.BivariateFunction.value` in
                interface :class:`~org.hipparchus.analysis.BivariateFunction`
        
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
                :meth:`~org.hipparchus.analysis.FieldBivariateFunction.value` in
                interface :class:`~org.hipparchus.analysis.FieldBivariateFunction`
        
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
    public interfaceBivariateGridInterpolator
    
        Interface representing a bivariate real interpolating function where the sample points must be specified on a regular
        grid.
    """
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.analysis.BivariateFunction: ...

_FieldBilinearInterpolatingFunction__T = typing.TypeVar('_FieldBilinearInterpolatingFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBilinearInterpolatingFunction(org.hipparchus.analysis.CalculusFieldBivariateFunction[_FieldBilinearInterpolatingFunction__T], typing.Generic[_FieldBilinearInterpolatingFunction__T]):
    """
    public classFieldBilinearInterpolatingFunction<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.CalculusFieldBivariateFunction`<T>
    
        Interpolate grid data using bi-linear interpolation.
    
        This interpolator is thread-safe.
    
        Since:
            4.0
    """
    def __init__(self, tArray: typing.Union[typing.List[_FieldBilinearInterpolatingFunction__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldBilinearInterpolatingFunction__T], jpype.JArray], tArray3: typing.Union[typing.List[typing.MutableSequence[_FieldBilinearInterpolatingFunction__T]], jpype.JArray]): ...
    def getXInf(self) -> _FieldBilinearInterpolatingFunction__T:
        """
            Get the lowest grid x coordinate.
        
            Returns:
                lowest grid x coordinate
        
        
        """
        ...
    def getXSup(self) -> _FieldBilinearInterpolatingFunction__T:
        """
            Get the highest grid x coordinate.
        
            Returns:
                highest grid x coordinate
        
        
        """
        ...
    def getYInf(self) -> _FieldBilinearInterpolatingFunction__T:
        """
            Get the lowest grid y coordinate.
        
            Returns:
                lowest grid y coordinate
        
        
        """
        ...
    def getYSup(self) -> _FieldBilinearInterpolatingFunction__T:
        """
            Get the highest grid y coordinate.
        
            Returns:
                highest grid y coordinate
        
        
        """
        ...
    def value(self, t: _FieldBilinearInterpolatingFunction__T, t2: _FieldBilinearInterpolatingFunction__T) -> _FieldBilinearInterpolatingFunction__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.CalculusFieldBivariateFunction.value` in
                interface :class:`~org.hipparchus.analysis.CalculusFieldBivariateFunction`
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.interpolation.FieldBilinearInterpolatingFunction`): Abscissa for which the function value should be computed.
                y (:class:`~org.hipparchus.analysis.interpolation.FieldBilinearInterpolatingFunction`): Ordinate for which the function value should be computed.
        
            Returns:
                the value.
        
        
        """
        ...

_FieldBivariateGridInterpolator__T = typing.TypeVar('_FieldBivariateGridInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBivariateGridInterpolator(typing.Generic[_FieldBivariateGridInterpolator__T]):
    """
    public interfaceFieldBivariateGridInterpolator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>>
    
        Interface representing a bivariate field interpolating function where the sample points must be specified on a regular
        grid.
    
        Since:
            4.0
    """
    def interpolate(self, tArray: typing.Union[typing.List[_FieldBivariateGridInterpolator__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldBivariateGridInterpolator__T], jpype.JArray], tArray3: typing.Union[typing.List[typing.MutableSequence[_FieldBivariateGridInterpolator__T]], jpype.JArray]) -> org.hipparchus.analysis.CalculusFieldBivariateFunction[_FieldBivariateGridInterpolator__T]: ...

_FieldGridAxis__T = typing.TypeVar('_FieldGridAxis__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGridAxis(typing.Generic[_FieldGridAxis__T]):
    """
    public classFieldGridAxis<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Helper for finding interpolation nodes along one axis of grid data.
    
        This class is intended to be used for interpolating inside grids. It works on any sorted data without duplication and
        size at least :code:`n` where :code:`n` is the number of points required for interpolation (i.e. 2 for linear
        interpolation, 3 for quadratic...)
    
        The method uses linear interpolation to select the nodes indices. It should be O(1) for sufficiently regular data,
        therefore much faster than bisection. It also features caching, which improves speed when interpolating several points
        in row in the close locations, i.e. when successive calls have a high probability to return the same interpolation
        nodes. This occurs for example when scanning with small steps a loose grid. The method also works on non-regular grids,
        but may be slower in this case.
    
        This class is thread-safe.
    
        Since:
            4.0
    """
    def __init__(self, tArray: typing.Union[typing.List[_FieldGridAxis__T], jpype.JArray], int: int): ...
    def getN(self) -> int:
        """
            Get the number of points required for interpolation.
        
            Returns:
                number of points required for interpolation
        
        
        """
        ...
    def interpolationIndex(self, t: _FieldGridAxis__T) -> int:
        """
            Get the index of the first interpolation node for some coordinate along the grid.
        
            The index return is the one for the lowest interpolation node suitable for :code:`t`. This means that if :code:`i` is
            returned the nodes to use for interpolation at coordinate :code:`t` are at indices :code:`i`, :code:`i+1`, ...,
            :code:`i+n-1`, where :code:`n` is the number of points required for interpolation passed at construction.
        
            The index is selected in order to have the subset of nodes from :code:`i` to :code:`i+n-1` as balanced as possible
            around :code:`t`:
        
              - if :code:`t` is inside the grid and sufficiently far from the endpoints
        
                  - if :code:`n` is even, the returned nodes will be perfectly balanced: there will be :code:`n/2` nodes smaller than
                    :code:`t` and :code:`n/2` nodes larger than :code:`t`
                  - if :code:`n` is odd, the returned nodes will be slightly unbalanced by one point: there will be :code:`(n+1)/2` nodes
                    smaller than :code:`t` and :code:`(n-1)/2` nodes larger than :code:`t`
        
              - if :code:`t` is inside the grid and close to endpoints, the returned nodes will be unbalanced: there will be less nodes
                on the endpoints side and more nodes on the interior side
              - if :code:`t` is outside of the grid, the returned nodes will completely off balance: all nodes will be on the same side
                with respect to :code:`t`
        
        
            It is *not* an error to call this method with :code:`t` outside of the grid, it simply implies that the interpolation
            will become an extrapolation and accuracy will decrease as :code:`t` goes farther from the grid points. This is intended
            so interpolation does not fail near the end of the grid.
        
            Parameters:
                t (:class:`~org.hipparchus.analysis.interpolation.FieldGridAxis`): coordinate of the point to interpolate
        
            Returns:
                index :code:`i` such :meth:`~org.hipparchus.analysis.interpolation.FieldGridAxis.node`,
                :meth:`~org.hipparchus.analysis.interpolation.FieldGridAxis.node`, ...
                :meth:`~org.hipparchus.analysis.interpolation.FieldGridAxis.node` can be used for interpolating a value at coordinate
                :code:`t`
        
            Since:
                1.4
        
        
        """
        ...
    def node(self, int: int) -> _FieldGridAxis__T:
        """
            Get the interpolation node at specified index.
        
            Parameters:
                index (int): node index
        
            Returns:
                coordinate of the node at specified index
        
        
        """
        ...
    def size(self) -> int:
        """
            Get the number of points of the grid.
        
            Returns:
                number of points of the grid
        
        
        """
        ...

_FieldHermiteInterpolator__T = typing.TypeVar('_FieldHermiteInterpolator__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldHermiteInterpolator(typing.Generic[_FieldHermiteInterpolator__T]):
    """
    public classFieldHermiteInterpolator<T extends :class:`~org.hipparchus.FieldElement`<T>> extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
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
    def addSamplePoint(self, t: _FieldHermiteInterpolator__T, *tArray: typing.Union[typing.List[_FieldHermiteInterpolator__T], jpype.JArray]) -> None: ...
    def derivatives(self, t: _FieldHermiteInterpolator__T, int: int) -> typing.MutableSequence[typing.MutableSequence[_FieldHermiteInterpolator__T]]: ...
    def value(self, t: _FieldHermiteInterpolator__T) -> typing.MutableSequence[_FieldHermiteInterpolator__T]: ...

class FieldUnivariateInterpolator:
    """
    public interfaceFieldUnivariateInterpolator
    
        Interface representing a univariate field interpolating function.
    
        Since:
            1.5
    """
    _interpolate__T = typing.TypeVar('_interpolate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def interpolate(self, tArray: typing.Union[typing.List[_interpolate__T], jpype.JArray], tArray2: typing.Union[typing.List[_interpolate__T], jpype.JArray]) -> org.hipparchus.analysis.CalculusFieldUnivariateFunction[_interpolate__T]: ...

class GridAxis(java.io.Serializable):
    """
    public classGridAxis extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Helper for finding interpolation nodes along one axis of grid data.
    
        This class is intended to be used for interpolating inside grids. It works on any sorted data without duplication and
        size at least :code:`n` where :code:`n` is the number of points required for interpolation (i.e. 2 for linear
        interpolation, 3 for quadratic...)
    
        The method uses linear interpolation to select the nodes indices. It should be O(1) for sufficiently regular data,
        therefore much faster than bisection. It also features caching, which improves speed when interpolating several points
        in row in the close locations, i.e. when successive calls have a high probability to return the same interpolation
        nodes. This occurs for example when scanning with small steps a loose grid. The method also works on non-regular grids,
        but may be slower in this case.
    
        This class is thread-safe.
    
        Since:
            1.4
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int): ...
    def getN(self) -> int:
        """
            Get the number of points required for interpolation.
        
            Returns:
                number of points required for interpolation
        
        
        """
        ...
    def interpolationIndex(self, double: float) -> int:
        """
            Get the index of the first interpolation node for some coordinate along the grid.
        
            The index return is the one for the lowest interpolation node suitable for :code:`t`. This means that if :code:`i` is
            returned the nodes to use for interpolation at coordinate :code:`t` are at indices :code:`i`, :code:`i+1`, ...,
            :code:`i+n-1`, where :code:`n` is the number of points required for interpolation passed at construction.
        
            The index is selected in order to have the subset of nodes from :code:`i` to :code:`i+n-1` as balanced as possible
            around :code:`t`:
        
              - if :code:`t` is inside the grid and sufficiently far from the endpoints
        
                  - if :code:`n` is even, the returned nodes will be perfectly balanced: there will be :code:`n/2` nodes smaller than
                    :code:`t` and :code:`n/2` nodes larger than :code:`t`
                  - if :code:`n` is odd, the returned nodes will be slightly unbalanced by one point: there will be :code:`(n+1)/2` nodes
                    smaller than :code:`t` and :code:`(n-1)/2` nodes larger than :code:`t`
        
              - if :code:`t` is inside the grid and close to endpoints, the returned nodes will be unbalanced: there will be less nodes
                on the endpoints side and more nodes on the interior side
              - if :code:`t` is outside of the grid, the returned nodes will completely off balance: all nodes will be on the same side
                with respect to :code:`t`
        
        
            It is *not* an error to call this method with :code:`t` outside of the grid, it simply implies that the interpolation
            will become an extrapolation and accuracy will decrease as :code:`t` goes farther from the grid points. This is intended
            so interpolation does not fail near the end of the grid.
        
            Parameters:
                t (double): coordinate of the point to interpolate
        
            Returns:
                index :code:`i` such :meth:`~org.hipparchus.analysis.interpolation.GridAxis.node`,
                :meth:`~org.hipparchus.analysis.interpolation.GridAxis.node`, ...
                :meth:`~org.hipparchus.analysis.interpolation.GridAxis.node` can be used for interpolating a value at coordinate
                :code:`t`
        
            Since:
                1.4
        
        
        """
        ...
    def node(self, int: int) -> float:
        """
            Get the interpolation node at specified index.
        
            Parameters:
                index (int): node index
        
            Returns:
                coordinate of the node at specified index
        
        
        """
        ...
    def size(self) -> int:
        """
            Get the number of points of the grid.
        
            Returns:
                number of points of the grid
        
        
        """
        ...

class HermiteInterpolator(org.hipparchus.analysis.differentiation.UnivariateDifferentiableVectorFunction):
    """
    public classHermiteInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableVectorFunction`
    
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
    def addSamplePoint(self, double: float, *doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def derivatives(self, double: float, int: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getPolynomials(self) -> typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]: ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> typing.MutableSequence[float]: ...
    @typing.overload
    def value(self, t: _value_1__T) -> typing.MutableSequence[_value_1__T]: ...

class InterpolatingMicrosphere:
    """
    public classInterpolatingMicrosphere extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
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
    def value(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray], double4: float, double5: float) -> float:
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
    public interfaceMultivariateInterpolator
    
        Interface representing a univariate real interpolating function.
    """
    def interpolate(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.MultivariateFunction: ...

class PiecewiseBicubicSplineInterpolatingFunction(org.hipparchus.analysis.BivariateFunction, org.hipparchus.analysis.FieldBivariateFunction):
    """
    public classPiecewiseBicubicSplineInterpolatingFunction extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.BivariateFunction`, :class:`~org.hipparchus.analysis.FieldBivariateFunction`
    
        Function that implements the `bicubic spline <http://www.paulinternet.nl/?page=bicubic>` interpolation. This
        implementation currently uses :class:`~org.hipparchus.analysis.interpolation.AkimaSplineInterpolator` as the underlying
        one-dimensional interpolator, which requires 5 sample points; insufficient data will raise an exception when the
        :meth:`~org.hipparchus.analysis.interpolation.PiecewiseBicubicSplineInterpolatingFunction.value` method is called.
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
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
    public classTricubicInterpolatingFunction extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.TrivariateFunction`
    
        Function that implements the ` tricubic spline interpolation <http://en.wikipedia.org/wiki/Tricubic_interpolation>`, as
        proposed in
            Tricubic interpolation in three dimensions
    
    
            F. Lekien and J. Marsden
    
    
            *Int. J. Numer. Meth. Eng* 2005; **63**:455-471
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray], doubleArray4: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], doubleArray5: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], doubleArray6: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], doubleArray7: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], doubleArray8: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], doubleArray9: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], doubleArray10: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], doubleArray11: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]): ...
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
    public interfaceTrivariateGridInterpolator
    
        Interface representing a trivariate real interpolating function where the sample points must be specified on a regular
        grid.
    """
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray], doubleArray4: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]) -> org.hipparchus.analysis.TrivariateFunction: ...

class UnivariateInterpolator:
    """
    public interfaceUnivariateInterpolator
    
        Interface representing a univariate real interpolating function.
    """
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.UnivariateFunction: ...

class AkimaSplineInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    """
    public classAkimaSplineInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, :class:`~org.hipparchus.analysis.interpolation.FieldUnivariateInterpolator`
    
        Computes a cubic spline interpolation for the data set using the Akima algorithm, as originally formulated by Hiroshi
        Akima in his 1970 paper `A New Method of Interpolation and Smooth Curve Fitting Based on Local Procedures.
        <http://doi.acm.org/10.1145/321607.321609>` J. ACM 17, 4 (October 1970), 589-602. DOI=10.1145/321607.321609
    
        This implementation is based on the Akima implementation in the CubicSpline class in the Math.NET Numerics library. The
        method referenced is CubicSpline.InterpolateAkimaSorted
    
        The :meth:`~org.hipparchus.analysis.interpolation.AkimaSplineInterpolator.interpolate` method returns a
        :class:`~org.hipparchus.analysis.polynomials.PolynomialSplineFunction` consisting of n cubic polynomials, defined over
        the subintervals determined by the x values, :code:`x[0] < x[i] ... < x[n]`. The Akima algorithm requires that :code:`n
        >= 5`.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.Union[typing.List[_interpolate_0__T], jpype.JArray], tArray2: typing.Union[typing.List[_interpolate_0__T], jpype.JArray]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class BicubicInterpolator(BivariateGridInterpolator):
    """
    public classBicubicInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.BivariateGridInterpolator`
    
        Generates a :class:`~org.hipparchus.analysis.interpolation.BicubicInterpolatingFunction`.
    
        Caveat: Because the interpolation scheme requires that derivatives be specified at the sample points, those are
        approximated with finite differences (using the 2-points symmetric formulae). Since their values are undefined at the
        borders of the provided interpolation ranges, the interpolated values will be wrong at the edges of the patch. The
        :code:`interpolate` method will return a function that overrides
        :meth:`~org.hipparchus.analysis.interpolation.BicubicInterpolatingFunction.isValidPoint` to indicate points where the
        interpolation will be inaccurate.
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> BicubicInterpolatingFunction: ...

class BilinearInterpolator(BivariateGridInterpolator):
    """
    public classBilinearInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.BivariateGridInterpolator`
    
        Interpolate grid data using bi-linear interpolation.
    
        Since:
            1.4
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> BilinearInterpolatingFunction: ...

class DividedDifferenceInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    public classDividedDifferenceInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Implements the ` Divided Difference Algorithm
        <http://mathworld.wolfram.com/NewtonsDividedDifferenceInterpolationFormula.html>` for interpolation of real univariate
        functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 2.
    
        The actual code of Neville's evaluation is in PolynomialFunctionLagrangeForm, this class provides an easy-to-use
        interface to it.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialFunctionNewtonForm: ...

_FieldBilinearInterpolator__T = typing.TypeVar('_FieldBilinearInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBilinearInterpolator(FieldBivariateGridInterpolator[_FieldBilinearInterpolator__T], typing.Generic[_FieldBilinearInterpolator__T]):
    """
    public classFieldBilinearInterpolator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.FieldBivariateGridInterpolator`<T>
    
        Interpolate grid data using bi-linear interpolation.
    
        Since:
            4.0
    """
    def __init__(self): ...
    def interpolate(self, tArray: typing.Union[typing.List[_FieldBilinearInterpolator__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldBilinearInterpolator__T], jpype.JArray], tArray3: typing.Union[typing.List[typing.MutableSequence[_FieldBilinearInterpolator__T]], jpype.JArray]) -> FieldBilinearInterpolatingFunction[_FieldBilinearInterpolator__T]: ...

class InterpolatingMicrosphere2D(InterpolatingMicrosphere):
    """
    public classInterpolatingMicrosphere2D extends :class:`~org.hipparchus.analysis.interpolation.InterpolatingMicrosphere`
    
        Utility class for the :class:`~org.hipparchus.analysis.interpolation.MicrosphereProjectionInterpolator` algorithm. For
        2D interpolation, this class constructs the microsphere as a series of evenly spaced facets (rather than generating
        random normals as in the base implementation).
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def copy(self) -> 'InterpolatingMicrosphere2D':
        """
            Perform a copy.
        
            Overrides:
                :meth:`~org.hipparchus.analysis.interpolation.InterpolatingMicrosphere.copy` in
                class :class:`~org.hipparchus.analysis.interpolation.InterpolatingMicrosphere`
        
            Returns:
                a copy of this instance.
        
        
        """
        ...

class LinearInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    """
    public classLinearInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, :class:`~org.hipparchus.analysis.interpolation.FieldUnivariateInterpolator`
    
        Implements a linear function for interpolation of real univariate functions.
    """
    def __init__(self): ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.Union[typing.List[_interpolate_0__T], jpype.JArray], tArray2: typing.Union[typing.List[_interpolate_0__T], jpype.JArray]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class LoessInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    public classLoessInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Implements the ` Local Regression Algorithm <http://en.wikipedia.org/wiki/Local_regression>` (also Loess, Lowess) for
        interpolation of real univariate functions.
    
        For reference, see ` William S. Cleveland - Robust Locally Weighted Regression and Smoothing Scatterplots
        <http://amstat.tandfonline.com/doi/abs/10.1080/01621459.1979.10481038>`
    
        This class implements both the loess method and serves as an interpolation adapter to it, allowing one to build a spline
        on the obtained loess fit.
    
        Also see:
    
              - :meth:`~serialized`
    """
    DEFAULT_BANDWIDTH: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_BANDWIDTH
    
        Default value of the bandwidth parameter.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_ROBUSTNESS_ITERS: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_ROBUSTNESS_ITERS
    
        Default value of the number of robustness iterations.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_ACCURACY: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ACCURACY
    
        Default value for accuracy.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...
    @typing.overload
    def smooth(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def smooth(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...

class MicrosphereProjectionInterpolator(MultivariateInterpolator):
    """
    public classMicrosphereProjectionInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.MultivariateInterpolator`
    
        Interpolator that implements the algorithm described in *William Dudziak*'s `MS thesis
        <http://www.dudziak.com/microsphere.pdf>`.
    """
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, boolean: bool, double5: float): ...
    @typing.overload
    def __init__(self, interpolatingMicrosphere: InterpolatingMicrosphere, double: float, boolean: bool, double2: float): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.MultivariateFunction: ...

class NevilleInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    public classNevilleInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`, :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Implements the ` Neville's Algorithm <http://mathworld.wolfram.com/NevillesAlgorithm.html>` for interpolation of real
        univariate functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 2.
    
        The actual code of Neville's algorithm is in PolynomialFunctionLagrangeForm, this class provides an easy-to-use
        interface to it.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialFunctionLagrangeForm: ...

class PiecewiseBicubicSplineInterpolator(BivariateGridInterpolator):
    """
    public classPiecewiseBicubicSplineInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.BivariateGridInterpolator`
    
        Generates a piecewise-bicubic interpolating function.
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> PiecewiseBicubicSplineInterpolatingFunction: ...

class SplineInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    def __init__(self): ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.Union[typing.List[_interpolate_0__T], jpype.JArray], tArray2: typing.Union[typing.List[_interpolate_0__T], jpype.JArray]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class TricubicInterpolator(TrivariateGridInterpolator):
    """
    public classTricubicInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.TrivariateGridInterpolator`
    
        Generates a tricubic interpolating function.
    """
    def __init__(self): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray], doubleArray4: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]) -> TricubicInterpolatingFunction: ...

class UnivariatePeriodicInterpolator(UnivariateInterpolator):
    """
    public classUnivariatePeriodicInterpolator extends :class:`~org.hipparchus.analysis.interpolation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.interpolation.UnivariateInterpolator`
    
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
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self, univariateInterpolator: typing.Union[UnivariateInterpolator, typing.Callable], double: float): ...
    @typing.overload
    def __init__(self, univariateInterpolator: typing.Union[UnivariateInterpolator, typing.Callable], double: float, int: int): ...
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.UnivariateFunction: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.interpolation")``.

    AkimaSplineInterpolator: typing.Type[AkimaSplineInterpolator]
    BicubicInterpolatingFunction: typing.Type[BicubicInterpolatingFunction]
    BicubicInterpolator: typing.Type[BicubicInterpolator]
    BilinearInterpolatingFunction: typing.Type[BilinearInterpolatingFunction]
    BilinearInterpolator: typing.Type[BilinearInterpolator]
    BivariateGridInterpolator: typing.Type[BivariateGridInterpolator]
    DividedDifferenceInterpolator: typing.Type[DividedDifferenceInterpolator]
    FieldBilinearInterpolatingFunction: typing.Type[FieldBilinearInterpolatingFunction]
    FieldBilinearInterpolator: typing.Type[FieldBilinearInterpolator]
    FieldBivariateGridInterpolator: typing.Type[FieldBivariateGridInterpolator]
    FieldGridAxis: typing.Type[FieldGridAxis]
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
