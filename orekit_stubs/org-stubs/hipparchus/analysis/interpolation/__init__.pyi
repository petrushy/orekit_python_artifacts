
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
    implements BivariateFunction
    
    Function that implements the ` bicubic spline interpolation <http://en.wikipedia.org/wiki/Bicubic_interpolation>`.
    """
    def __init__(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], f: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], dFdX: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], dFdY: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], d2FdXdY: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            x (double[]): Sample values of the x-coordinate, in increasing order.
            y (double[]): Sample values of the y-coordinate, in increasing order.
            f (double[][]): Values of the function on every grid point.
            dFdX (double[][]): Values of the partial derivative of function with respect to x on every grid point.
            dFdY (double[][]): Values of the partial derivative of function with respect to y on every grid point.
            d2FdXdY (double[][]): Values of the cross partial derivative of function on every grid point.
        
        Raises:
            MathIllegalArgumentException: if the various arrays do not contain the expected number of elements.
            MathIllegalArgumentException: if x or y are not strictly increasing.
            MathIllegalArgumentException: if any of the arrays has zero length.
        
        
        """
        ...
    def isValidPoint(self, x: float, y: float) -> bool:
        """
        Indicates whether a point is within the interpolation range.
        
        Parameters:
            x (double): First coordinate.
            y (double): Second coordinate.
        
        Returns:
            true if (x, y) is a valid point.
        
        
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
        
        Raises:
            MathIllegalArgumentException: 
        
        """
        ...

class BilinearInterpolatingFunction(org.hipparchus.analysis.BivariateFunction, org.hipparchus.analysis.FieldBivariateFunction, java.io.Serializable):
    """
    implements BivariateFunction, FieldBivariateFunction, Serializable
    
    Interpolate grid data using bi-linear interpolation.
    
    This interpolator is thread-safe.
    
    Since:
        1.4
    
          - serialized
    """
    def __init__(self, xVal: typing.Union[typing.List[float], jpype.JArray], yVal: typing.Union[typing.List[float], jpype.JArray], fVal: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            xVal (double[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yVal (double[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fVal (double[][]): The values of the interpolation points on all the grid knots: fVal[i][j] = f(xVal[i], yVal[j]).
        
        Raises:
            MathIllegalArgumentException: if grid size is smaller than 2 or if the grid is not sorted in strict increasing order
        
        
        """
        ...
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
    @typing.overload
    def value(self, x: _value_1__T, y: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface FieldBivariateFunction
        
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
    Interface representing a bivariate real interpolating function where the sample points must be specified on a regular grid.
    """
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.analysis.BivariateFunction:
        """
        Compute an interpolating function for the dataset.
        
        Parameters:
            xval (double[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (double[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fval (double[][]): The values of the interpolation points on all the grid knots: fval[i][j] = f(xval[i], yval[j]).
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if the array is not sorted.
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
        
        
        """
        ...

_FieldBilinearInterpolatingFunction__T = typing.TypeVar('_FieldBilinearInterpolatingFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBilinearInterpolatingFunction(org.hipparchus.analysis.CalculusFieldBivariateFunction[_FieldBilinearInterpolatingFunction__T], typing.Generic[_FieldBilinearInterpolatingFunction__T]):
    """
    implements CalculusFieldBivariateFunction<T>
    
    Interpolate grid data using bi-linear interpolation.
    
    This interpolator is thread-safe.
    
    Since:
        4.0
    """
    def __init__(self, xVal: typing.Union[typing.List[_FieldBilinearInterpolatingFunction__T], jpype.JArray], yVal: typing.Union[typing.List[_FieldBilinearInterpolatingFunction__T], jpype.JArray], fVal: typing.Union[typing.List[typing.MutableSequence[_FieldBilinearInterpolatingFunction__T]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            xVal (FieldBilinearInterpolatingFunction[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yVal (FieldBilinearInterpolatingFunction[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fVal (FieldBilinearInterpolatingFunction[][]): The values of the interpolation points on all the grid knots: fVal[i][j] = f(xVal[i], yVal[j]).
        
        Raises:
            MathIllegalArgumentException: if grid size is smaller than 2 or if the grid is not sorted in strict increasing order
        
        
        """
        ...
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
    def value(self, x: _FieldBilinearInterpolatingFunction__T, y: _FieldBilinearInterpolatingFunction__T) -> _FieldBilinearInterpolatingFunction__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface CalculusFieldBivariateFunction
        
        Parameters:
            x (FieldBilinearInterpolatingFunction): Abscissa for which the function value should be computed.
            y (FieldBilinearInterpolatingFunction): Ordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        
        """
        ...

_FieldBivariateGridInterpolator__T = typing.TypeVar('_FieldBivariateGridInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBivariateGridInterpolator(typing.Generic[_FieldBivariateGridInterpolator__T]):
    """
    Interface representing a bivariate field interpolating function where the sample points must be specified on a regular grid.
    
    Since:
        4.0
    """
    def interpolate(self, xval: typing.Union[typing.List[_FieldBivariateGridInterpolator__T], jpype.JArray], yval: typing.Union[typing.List[_FieldBivariateGridInterpolator__T], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[_FieldBivariateGridInterpolator__T]], jpype.JArray]) -> org.hipparchus.analysis.CalculusFieldBivariateFunction[_FieldBivariateGridInterpolator__T]:
        """
        Compute an interpolating function for the dataset.
        
        Parameters:
            xval (FieldBivariateGridInterpolator[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (FieldBivariateGridInterpolator[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fval (FieldBivariateGridInterpolator[][]): The values of the interpolation points on all the grid knots: fval[i][j] = f(xval[i], yval[j]).
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if the array is not sorted.
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
        
        
        """
        ...

_FieldGridAxis__T = typing.TypeVar('_FieldGridAxis__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGridAxis(typing.Generic[_FieldGridAxis__T]):
    """
    Helper for finding interpolation nodes along one axis of grid data.
    
    This class is intended to be used for interpolating inside grids. It works on any sorted data without duplication and size at least n where n is the number of points required for interpolation (i.e. 2 for linear interpolation, 3 for quadratic...)
    
    The method uses linear interpolation to select the nodes indices. It should be O(1) for sufficiently regular data, therefore much faster than bisection. It also features caching, which improves speed when interpolating several points in row in the close locations, i.e. when successive calls have a high probability to return the same interpolation nodes. This occurs for example when scanning with small steps a loose grid. The method also works on non-regular grids, but may be slower in this case.
    
    This class is thread-safe.
    
    Since:
        4.0
    """
    def __init__(self, grid: typing.Union[typing.List[_FieldGridAxis__T], jpype.JArray], n: int):
        """
        Simple constructor.
        
        Parameters:
            grid (FieldGridAxis[]): coordinates of the interpolation points, sorted in increasing order
            n (int): number of points required for interpolation, i.e. 2 for linear, 3 for quadratic...
        
        Raises:
            MathIllegalArgumentException: if grid size is smaller than n or if the grid is not sorted in strict increasing order
        
        
        """
        ...
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
        
        The index return is the one for the lowest interpolation node suitable for t. This means that if i is returned the nodes to use for interpolation at coordinate t are at indices i, i+1..., i+n-1, where n is the number of points required for interpolation passed at construction.
        
        The index is selected in order to have the subset of nodes from i to i+n-1 as balanced as possible around t:
        
          - if t is inside the grid and sufficiently far from the endpoints
        
              - if n is even, the returned nodes will be perfectly balanced: there will be n/2 nodes smaller than
                t and n/2 nodes larger than t
              - if n is odd, the returned nodes will be slightly unbalanced by one point: there will be (n+1)/2 nodes
                smaller than t and (n-1)/2 nodes larger than t
        
          - if t is inside the grid and close to endpoints, the returned nodes will be unbalanced: there will be less nodes
            on the endpoints side and more nodes on the interior side
          - if t is outside of the grid, the returned nodes will completely off balance: all nodes will be on the same side
            with respect to t
        
        It is not an error to call this method with t outside of the grid, it simply implies that the interpolation will become an extrapolation and accuracy will decrease as t goes farther from the grid points. This is intended so interpolation does not fail near the end of the grid.
        
        Parameters:
            t (FieldGridAxis): coordinate of the point to interpolate
        
        Returns:
            index i such node,
            node...
            node can be used for interpolating a value at coordinate
            t
        
        Since:
            1.4
        
        
        """
        ...
    def node(self, index: int) -> _FieldGridAxis__T:
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
    Polynomial interpolator using both sample values and sample derivatives.
    
    The interpolation polynomials match all sample points, including both values and provided derivatives. There is one polynomial for each component of the values vector. All polynomials have the same degree. The degree of the polynomials depends on the number of points and number of derivatives at each point. For example the interpolation polynomials for n sample points without any derivatives all have degree n-1. The interpolation polynomials for n sample points with the two extreme points having value and first derivative and the remaining points having value only all have degree n+1. The interpolation polynomial for n sample points with value, first and second derivative for all points all have degree 3n-1.
    """
    def __init__(self):
        """
        Create an empty interpolator.
        """
        ...
    def addSamplePoint(self, x: _FieldHermiteInterpolator__T, *value: typing.Union[typing.List[_FieldHermiteInterpolator__T], jpype.JArray]) -> None:
        """
        Add a sample point.
        
        This method must be called once for each sample point. It is allowed to mix some calls with values only with calls with values and first derivatives.
        
        The point abscissae for all calls must be different.
        
        Parameters:
            x (FieldHermiteInterpolator): abscissa of the sample point
            value (FieldHermiteInterpolator[]...): value and derivatives of the sample point (if only one row is passed, it is the value, if two rows are passed the first
                one is the value and the second the derivative and so on)
        
        Raises:
            MathIllegalArgumentException: if the abscissa difference between added point and a previous point is zero (i.e. the two points are at same abscissa)
            MathRuntimeException: if the number of derivatives is larger than 20, which prevents computation of a factorial
            MathIllegalArgumentException: if derivative structures are inconsistent
            NullArgumentException: if x is null
        
        
        """
        ...
    def derivatives(self, x: _FieldHermiteInterpolator__T, order: int) -> typing.MutableSequence[typing.MutableSequence[_FieldHermiteInterpolator__T]]:
        """
        Interpolate value and first derivatives at a specified abscissa.
        
        Parameters:
            x (FieldHermiteInterpolator): interpolation abscissa
            order (int): maximum derivation order
        
        Returns:
            interpolated value and derivatives (value in row 0, 1 :sup:`st` derivative in row 1... n :sup:`th` derivative in row
            n)
        
        Raises:
            MathIllegalArgumentException: if sample is empty
            NullArgumentException: if x is null
        
        
        """
        ...
    def value(self, x: _FieldHermiteInterpolator__T) -> typing.MutableSequence[_FieldHermiteInterpolator__T]:
        """
        Interpolate value at a specified abscissa.
        
        Parameters:
            x (FieldHermiteInterpolator): interpolation abscissa
        
        Returns:
            interpolated value
        
        Raises:
            MathIllegalArgumentException: if sample is empty
            NullArgumentException: if x is null
        
        
        """
        ...

class FieldUnivariateInterpolator:
    """
    Interface representing a univariate field interpolating function.
    
    Since:
        1.5
    """
    _interpolate__T = typing.TypeVar('_interpolate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def interpolate(self, xval: typing.Union[typing.List[_interpolate__T], jpype.JArray], yval: typing.Union[typing.List[_interpolate__T], jpype.JArray]) -> org.hipparchus.analysis.CalculusFieldUnivariateFunction[_interpolate__T]:
        """
        Compute an interpolating function for the dataset.
        
        Parameters:
            xval (T[]): Arguments for the interpolation points.
            yval (T[]): Values for the interpolation points.
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if the arguments violate assumptions made by the interpolation algorithm.
            MathIllegalArgumentException: if arrays lengthes do not match
        
        
        """
        ...

class GridAxis(java.io.Serializable):
    """
    implements Serializable
    
    Helper for finding interpolation nodes along one axis of grid data.
    
    This class is intended to be used for interpolating inside grids. It works on any sorted data without duplication and size at least n where n is the number of points required for interpolation (i.e. 2 for linear interpolation, 3 for quadratic...)
    
    The method uses linear interpolation to select the nodes indices. It should be O(1) for sufficiently regular data, therefore much faster than bisection. It also features caching, which improves speed when interpolating several points in row in the close locations, i.e. when successive calls have a high probability to return the same interpolation nodes. This occurs for example when scanning with small steps a loose grid. The method also works on non-regular grids, but may be slower in this case.
    
    This class is thread-safe.
    
    Since:
        1.4
    
          - serialized
    """
    def __init__(self, grid: typing.Union[typing.List[float], jpype.JArray], n: int):
        """
        Simple constructor.
        
        Parameters:
            grid (double[]): coordinates of the interpolation points, sorted in increasing order
            n (int): number of points required for interpolation, i.e. 2 for linear, 3 for quadratic...
        
        Raises:
            MathIllegalArgumentException: if grid size is smaller than n or if the grid is not sorted in strict increasing order
        
        
        """
        ...
    def getN(self) -> int:
        """
        Get the number of points required for interpolation.
        
        Returns:
            number of points required for interpolation
        
        
        """
        ...
    def interpolationIndex(self, t: float) -> int:
        """
        Get the index of the first interpolation node for some coordinate along the grid.
        
        The index return is the one for the lowest interpolation node suitable for t. This means that if i is returned the nodes to use for interpolation at coordinate t are at indices i, i+1..., i+n-1, where n is the number of points required for interpolation passed at construction.
        
        The index is selected in order to have the subset of nodes from i to i+n-1 as balanced as possible around t:
        
          - if t is inside the grid and sufficiently far from the endpoints
        
              - if n is even, the returned nodes will be perfectly balanced: there will be n/2 nodes smaller than
                t and n/2 nodes larger than t
              - if n is odd, the returned nodes will be slightly unbalanced by one point: there will be (n+1)/2 nodes
                smaller than t and (n-1)/2 nodes larger than t
        
          - if t is inside the grid and close to endpoints, the returned nodes will be unbalanced: there will be less nodes
            on the endpoints side and more nodes on the interior side
          - if t is outside of the grid, the returned nodes will completely off balance: all nodes will be on the same side
            with respect to t
        
        It is not an error to call this method with t outside of the grid, it simply implies that the interpolation will become an extrapolation and accuracy will decrease as t goes farther from the grid points. This is intended so interpolation does not fail near the end of the grid.
        
        Parameters:
            t (double): coordinate of the point to interpolate
        
        Returns:
            index i such node,
            node...
            node can be used for interpolating a value at coordinate
            t
        
        Since:
            1.4
        
        
        """
        ...
    def node(self, index: int) -> float:
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
    implements UnivariateDifferentiableVectorFunction
    
    Polynomial interpolator using both sample values and sample derivatives.
    
    The interpolation polynomials match all sample points, including both values and provided derivatives. There is one polynomial for each component of the values vector. All polynomials have the same degree. The degree of the polynomials depends on the number of points and number of derivatives at each point. For example the interpolation polynomials for n sample points without any derivatives all have degree n-1. The interpolation polynomials for n sample points with the two extreme points having value and first derivative and the remaining points having value only all have degree n+1. The interpolation polynomial for n sample points with value, first and second derivative for all points all have degree 3n-1.
    """
    def __init__(self):
        """
        Create an empty interpolator.
        """
        ...
    def addSamplePoint(self, x: float, *value: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add a sample point.
        
        This method must be called once for each sample point. It is allowed to mix some calls with values only with calls with values and first derivatives.
        
        The point abscissae for all calls must be different.
        
        Parameters:
            x (double): abscissa of the sample point
            value (double[]...): value and derivatives of the sample point (if only one row is passed, it is the value, if two rows are passed the first
                one is the value and the second the derivative and so on)
        
        Raises:
            MathIllegalArgumentException: if the abscissa difference between added point and a previous point is zero (i.e. the two points are at same abscissa)
            MathRuntimeException: if the number of derivatives is larger than 20, which prevents computation of a factorial
        
        
        """
        ...
    def derivatives(self, x: float, order: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Interpolate value and first derivatives at a specified abscissa.
        
        Parameters:
            x (double): interpolation abscissa
            order (int): maximum derivation order
        
        Returns:
            interpolated value and derivatives (value in row 0, 1 :sup:`st` derivative in row 1... n :sup:`th` derivative in row
            n)
        
        Raises:
            MathIllegalArgumentException: if sample is empty
            NullArgumentException: if x is null
        
        
        """
        ...
    def getPolynomials(self) -> typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]:
        """
        Compute the interpolation polynomials.
        
        Returns:
            interpolation polynomials array
        
        Raises:
            MathIllegalArgumentException: if sample is empty
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> typing.MutableSequence[float]: ...
    @typing.overload
    def value(self, t: _value_1__T) -> typing.MutableSequence[_value_1__T]: ...

class InterpolatingMicrosphere:
    """
    Utility class for the MicrosphereProjectionInterpolator algorithm.
    """
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, unitSphereRandomVectorGenerator: org.hipparchus.random.UnitSphereRandomVectorGenerator):
        """
        Create an unitialiazed sphere. Sub-classes are responsible for calling the add(double[]) add method in order to initialize all the sphere's facets.
        
        Parameters:
            dimension (int): Dimension of the data space.
            size (int): Number of surface elements of the sphere.
            maxDarkFraction (double): Maximum fraction of the facets that can be dark. If the fraction of "non-illuminated" facets is larger, no estimation of
                the value will be performed, and the background value will be returned instead.
            darkThreshold (double): Value of the illumination below which a facet is considered dark.
            background (double): Value returned when the maxDarkFraction threshold is exceeded.
        
        Raises:
            MathIllegalArgumentException: if dimension <= 0 or size <= 0.
            MathIllegalArgumentException: if darkThreshold < 0.
            MathIllegalArgumentException: if maxDarkFraction does not belong to the interval [0, 1].
        
        public InterpolatingMicrosphere(int dimension, int size, double maxDarkFraction, double darkThreshold, double background, UnitSphereRandomVectorGenerator rand)
        
        Create a sphere from randomly sampled vectors.
        
        Parameters:
            dimension (int): Dimension of the data space.
            size (int): Number of surface elements of the sphere.
            maxDarkFraction (double): Maximum fraction of the facets that can be dark. If the fraction of "non-illuminated" facets is larger, no estimation of
                the value will be performed, and the background value will be returned instead.
            darkThreshold (double): Value of the illumination below which a facet is considered dark.
            background (double): Value returned when the maxDarkFraction threshold is exceeded.
            rand (UnitSphereRandomVectorGenerator): Unit vector generator for creating the microsphere.
        
        Raises:
            MathIllegalArgumentException: if the size of the generated vectors does not match the dimension set in the constructor.
            MathIllegalArgumentException: if dimension <= 0 or size <= 0.
            MathIllegalArgumentException: if darkThreshold < 0.
            MathIllegalArgumentException: if maxDarkFraction does not belong to the interval [0, 1].
        
        protected InterpolatingMicrosphere(InterpolatingMicrosphere other)
        
        Copy constructor.
        
        Parameters:
            other (InterpolatingMicrosphere): Instance to copy.
        
        
        """
        ...
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
    def value(self, point: typing.Union[typing.List[float], jpype.JArray], samplePoints: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], sampleValues: typing.Union[typing.List[float], jpype.JArray], exponent: float, noInterpolationTolerance: float) -> float:
        """
        Estimate the value at the requested location. This microsphere is placed at the given point, contribution of the given samplePoints to each sphere facet is computed (illumination) and the interpolation is performed (integration of the illumination).
        
        Parameters:
            point (double[]): Interpolation point.
            samplePoints (double[][]): Sampling data points.
            sampleValues (double[]): Sampling data values at the corresponding samplePoints.
            exponent (double): Exponent used in the power law that computes the weights (distance dimming factor) of the sample data.
            noInterpolationTolerance (double): When the distance between the point and one of the samplePoints is less than this value, no
                interpolation will be performed, and the value of the sample will just be returned.
        
        Returns:
            the estimated value at the given point.
        
        Raises:
            MathIllegalArgumentException: if exponent < 0.
        
        
        """
        ...

class MultivariateInterpolator:
    """
    Interface representing a univariate real interpolating function.
    """
    def interpolate(self, xval: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.MultivariateFunction:
        """
        Computes an interpolating function for the data set.
        
        Parameters:
            xval (double[][]): the arguments for the interpolation points. xval[i][0] is the first component of interpolation point i,
                xval[i][1] is the second component, and so on until xval[i][d-1], the last component of that
                interpolation point (where d is thus the dimension of the space).
            yval (double[]): the values for the interpolation points
        
        Returns:
            a function which interpolates the data set
        
        Raises:
            MathIllegalArgumentException: if the arguments violate assumptions made by the interpolation algorithm.
            MathIllegalArgumentException: when the array dimensions are not consistent.
            MathIllegalArgumentException: if an array has zero-length.
            NullArgumentException: if the arguments are null.
        
        
        """
        ...

class PiecewiseBicubicSplineInterpolatingFunction(org.hipparchus.analysis.BivariateFunction, org.hipparchus.analysis.FieldBivariateFunction):
    """
    implements BivariateFunction, FieldBivariateFunction
    
    Function that implements the `bicubic spline <http://www.paulinternet.nl/?page=bicubic>` interpolation. This implementation currently uses AkimaSplineInterpolator as the underlying one-dimensional interpolator, which requires 5 sample points; insufficient data will raise an exception when the value method is called.
    """
    def __init__(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], f: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            x (double[]): Sample values of the x-coordinate, in increasing order.
            y (double[]): Sample values of the y-coordinate, in increasing order.
            f (double[][]): Values of the function on every grid point. the expected number of elements.
        
        Raises:
            MathIllegalArgumentException: if x or y are not strictly increasing.
            NullArgumentException: if any of the arguments are null
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the length of x and y don't match the row, column height of f
        
        
        """
        ...
    def isValidPoint(self, x: float, y: float) -> bool:
        """
        Indicates whether a point is within the interpolation range.
        
        Parameters:
            x (double): First coordinate.
            y (double): Second coordinate.
        
        Returns:
            true if (x, y) is a valid point.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, double: float, double2: float) -> float: ...
    @typing.overload
    def value(self, t: _value_1__T, t2: _value_1__T) -> _value_1__T: ...

class TricubicInterpolatingFunction(org.hipparchus.analysis.TrivariateFunction):
    """
    implements TrivariateFunction
    
    Function that implements the ` tricubic spline interpolation <http://en.wikipedia.org/wiki/Tricubic_interpolation>`, as proposed in Tricubic interpolation in three dimensions
    
        F. Lekien and J. Marsden
    
        Int. J. Numer. Meth. Eng 2005; 63:455-471
    """
    def __init__(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], z: typing.Union[typing.List[float], jpype.JArray], f: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], dFdX: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], dFdY: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], dFdZ: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], d2FdXdY: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], d2FdXdZ: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], d2FdYdZ: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray], d3FdXdYdZ: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            x (double[]): Sample values of the x-coordinate, in increasing order.
            y (double[]): Sample values of the y-coordinate, in increasing order.
            z (double[]): Sample values of the y-coordinate, in increasing order.
            f (double[][][]): Values of the function on every grid point.
            dFdX (double[][][]): Values of the partial derivative of function with respect to x on every grid point.
            dFdY (double[][][]): Values of the partial derivative of function with respect to y on every grid point.
            dFdZ (double[][][]): Values of the partial derivative of function with respect to z on every grid point.
            d2FdXdY (double[][][]): Values of the cross partial derivative of function on every grid point.
            d2FdXdZ (double[][][]): Values of the cross partial derivative of function on every grid point.
            d2FdYdZ (double[][][]): Values of the cross partial derivative of function on every grid point.
            d3FdXdYdZ (double[][][]): Values of the cross partial derivative of function on every grid point.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the various arrays do not contain the expected number of elements.
            MathIllegalArgumentException: if x, y or z are not strictly increasing.
        
        
        """
        ...
    def isValidPoint(self, x: float, y: float, z: float) -> bool:
        """
        Indicates whether a point is within the interpolation range.
        
        Parameters:
            x (double): First coordinate.
            y (double): Second coordinate.
            z (double): Third coordinate.
        
        Returns:
            true if (x, y, z) is a valid point.
        
        
        """
        ...
    def value(self, x: float, y: float, z: float) -> float:
        """
        Compute the value for the function.
        
        Specified by: value in interface TrivariateFunction
        
        Parameters:
            x (double): x-coordinate for which the function value should be computed.
            y (double): y-coordinate for which the function value should be computed.
            z (double): z-coordinate for which the function value should be computed.
        
        Returns:
            the value.
        
        Raises:
            MathIllegalArgumentException: if any of the variables is outside its interpolation range.
        
        
        """
        ...

class TrivariateGridInterpolator:
    """
    Interface representing a trivariate real interpolating function where the sample points must be specified on a regular grid.
    """
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray], zval: typing.Union[typing.List[float], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]) -> org.hipparchus.analysis.TrivariateFunction:
        """
        Compute an interpolating function for the dataset.
        
        Parameters:
            xval (double[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (double[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            zval (double[]): All the z-coordinates of the interpolation points, sorted in increasing order.
            fval (double[][][]): the values of the interpolation points on all the grid knots: fval[i][j][k] = f(xval[i], yval[j], zval[k]).
        
        Returns:
            a function that interpolates the data set.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if arrays are not sorted
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
        
        
        """
        ...

class UnivariateInterpolator:
    """
    Interface representing a univariate real interpolating function.
    """
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.UnivariateFunction:
        """
        Compute an interpolating function for the dataset.
        
        Parameters:
            xval (double[]): Arguments for the interpolation points.
            yval (double[]): Values for the interpolation points.
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if the arguments violate assumptions made by the interpolation algorithm.
            MathIllegalArgumentException: if arrays lengthes do not match
        
        
        """
        ...

class AkimaSplineInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    """
    implements UnivariateInterpolator, FieldUnivariateInterpolator
    
    Computes a cubic spline interpolation for the data set using the Akima algorithm, as originally formulated by Hiroshi Akima in his 1970 paper `A New Method of Interpolation and Smooth Curve Fitting Based on Local Procedures. <http://doi.acm.org/10.1145/321607.321609>` J. ACM 17, 4 (October 1970), 589-602. DOI=10.1145/321607.321609
    
    This implementation is based on the Akima implementation in the CubicSpline class in the Math.NET Numerics library. The method referenced is CubicSpline.InterpolateAkimaSorted
    
    The interpolate method returns a PolynomialSplineFunction consisting of n cubic polynomials, defined over the subintervals determined by the x values,  < x[n]. The Akima algorithm requires that n >= 5.
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
    implements BivariateGridInterpolator
    
    Generates a BicubicInterpolatingFunction.
    
    Caveat: Because the interpolation scheme requires that derivatives be specified at the sample points, those are approximated with finite differences (using the 2-points symmetric formulae). Since their values are undefined at the borders of the provided interpolation ranges, the interpolated values will be wrong at the edges of the patch. The interpolate method will return a function that overrides isValidPoint to indicate points where the interpolation will be inaccurate.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> BicubicInterpolatingFunction:
        """
        Compute an interpolating function for the dataset.
        
        Specified by: interpolate in interface BivariateGridInterpolator
        
        Parameters:
            xval (double[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (double[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fval (double[][]): The values of the interpolation points on all the grid knots: fval[i][j] = f(xval[i], yval[j]).
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if the array is not sorted.
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
        
        
        """
        ...

class BilinearInterpolator(BivariateGridInterpolator):
    """
    implements BivariateGridInterpolator
    
    Interpolate grid data using bi-linear interpolation.
    
    Since:
        1.4
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> BilinearInterpolatingFunction:
        """
        Compute an interpolating function for the dataset.
        
        Specified by: interpolate in interface BivariateGridInterpolator
        
        Parameters:
            xval (double[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (double[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fval (double[][]): The values of the interpolation points on all the grid knots: fval[i][j] = f(xval[i], yval[j]).
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if the array is not sorted.
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
        
        
        """
        ...

class DividedDifferenceInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    implements UnivariateInterpolator, Serializable
    
    Implements the ` Divided Difference Algorithm <http://mathworld.wolfram.com/NewtonsDividedDifferenceInterpolationFormula.html>` for interpolation of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 2.
    
    The actual code of Neville's evaluation is in PolynomialFunctionLagrangeForm, this class provides an easy-to-use interface to it.
    
          - serialized
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def interpolate(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialFunctionNewtonForm:
        """
        Compute an interpolating function for the dataset.
        
        Specified by: interpolate in interface UnivariateInterpolator
        
        Parameters:
            x (double[]): Interpolating points array.
            y (double[]): Interpolating values array.
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if the array lengths are different.
            MathIllegalArgumentException: if the number of points is less than 2.
            MathIllegalArgumentException: if x is not sorted in strictly increasing order.
        
        
        """
        ...

_FieldBilinearInterpolator__T = typing.TypeVar('_FieldBilinearInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBilinearInterpolator(FieldBivariateGridInterpolator[_FieldBilinearInterpolator__T], typing.Generic[_FieldBilinearInterpolator__T]):
    """
    implements FieldBivariateGridInterpolator<T>
    
    Interpolate grid data using bi-linear interpolation.
    
    Since:
        4.0
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def interpolate(self, xval: typing.Union[typing.List[_FieldBilinearInterpolator__T], jpype.JArray], yval: typing.Union[typing.List[_FieldBilinearInterpolator__T], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[_FieldBilinearInterpolator__T]], jpype.JArray]) -> FieldBilinearInterpolatingFunction[_FieldBilinearInterpolator__T]:
        """
        Compute an interpolating function for the dataset.
        
        Specified by: interpolate in interface FieldBivariateGridInterpolator
        
        Parameters:
            xval (FieldBilinearInterpolator[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (FieldBilinearInterpolator[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fval (FieldBilinearInterpolator[][]): The values of the interpolation points on all the grid knots: fval[i][j] = f(xval[i], yval[j]).
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if the array is not sorted.
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
        
        
        """
        ...

class InterpolatingMicrosphere2D(InterpolatingMicrosphere):
    """
    Utility class for the MicrosphereProjectionInterpolator algorithm. For 2D interpolation, this class constructs the microsphere as a series of evenly spaced facets (rather than generating random normals as in the base implementation).
    """
    def __init__(self, int: int, double: float, double2: float, double3: float):
        """
        Create a sphere from vectors regularly sampled around a circle.
        
        Parameters:
            size (int): Number of surface elements of the sphere.
            maxDarkFraction (double): Maximum fraction of the facets that can be dark. If the fraction of "non-illuminated" facets is larger, no estimation of
                the value will be performed, and the background value will be returned instead.
            darkThreshold (double): Value of the illumination below which a facet is considered dark.
            background (double): Value returned when the maxDarkFraction threshold is exceeded.
        
        Raises:
            MathIllegalArgumentException: if size <= 0.
            MathIllegalArgumentException: if darkThreshold < 0.
            MathIllegalArgumentException: if maxDarkFraction does not belong to the interval [0, 1].
        
        protected InterpolatingMicrosphere2D(InterpolatingMicrosphere2D other)
        
        Copy constructor.
        
        Parameters:
            other (InterpolatingMicrosphere2D): Instance to copy.
        
        
        """
        ...
    def copy(self) -> 'InterpolatingMicrosphere2D':
        """
        Perform a copy.
        
        Overrides: copy in class InterpolatingMicrosphere
        
        Returns:
            a copy of this instance.
        
        
        """
        ...

class LinearInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    """
    implements UnivariateInterpolator, FieldUnivariateInterpolator
    
    Implements a linear function for interpolation of real univariate functions.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.Union[typing.List[_interpolate_0__T], jpype.JArray], tArray2: typing.Union[typing.List[_interpolate_0__T], jpype.JArray]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class LoessInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    implements UnivariateInterpolator, Serializable
    
    Implements the ` Local Regression Algorithm <http://en.wikipedia.org/wiki/Local_regression>` (also Loess, Lowess) for interpolation of real univariate functions.
    
    For reference, see ` William S. Cleveland - Robust Locally Weighted Regression and Smoothing Scatterplots <http://amstat.tandfonline.com/doi/abs/10.1080/01621459.1979.10481038>`
    
    This class implements both the loess method and serves as an interpolation adapter to it, allowing one to build a spline on the obtained loess fit.
    
          - serialized
    """
    DEFAULT_BANDWIDTH: typing.ClassVar[float] = ...
    """
    Default value of the bandwidth parameter.
    
          - constant
    
    
    
    """
    DEFAULT_ROBUSTNESS_ITERS: typing.ClassVar[int] = ...
    """
    Default value of the number of robustness iterations.
    
          - constant
    
    
    
    """
    DEFAULT_ACCURACY: typing.ClassVar[float] = ...
    """
    Default value for accuracy.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float): ...
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction:
        """
        Compute an interpolating function by performing a loess fit on the data at the original abscissae and then building a cubic spline with a SplineInterpolator on the resulting fit.
        
        Specified by: interpolate in interface UnivariateInterpolator
        
        Parameters:
            xval (double[]): the arguments for the interpolation points
            yval (double[]): the values for the interpolation points
        
        Returns:
            A cubic spline built upon a loess fit to the data at the original abscissae
        
        Raises:
            MathIllegalArgumentException: if xval not sorted in strictly increasing order.
            MathIllegalArgumentException: if xval and yval have different sizes.
            MathIllegalArgumentException: if xval or yval has zero size.
            MathIllegalArgumentException: if any of the arguments and values are not finite real numbers.
            MathIllegalArgumentException: if the bandwidth is too small to accomodate the size of the input data (i.e. the bandwidth must be larger than 2/n).
        
        
        """
        ...
    @typing.overload
    def smooth(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def smooth(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...

class MicrosphereProjectionInterpolator(MultivariateInterpolator):
    """
    implements MultivariateInterpolator
    
    Interpolator that implements the algorithm described in William Dudziak's `MS thesis <http://www.dudziak.com/microsphere.pdf>`.
    """
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, boolean: bool, double5: float): ...
    @typing.overload
    def __init__(self, interpolatingMicrosphere: InterpolatingMicrosphere, double: float, boolean: bool, double2: float): ...
    def interpolate(self, xval: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.MultivariateFunction:
        """
        Computes an interpolating function for the data set.
        
        Specified by: interpolate in interface MultivariateInterpolator
        
        Parameters:
            xval (double[][]): the arguments for the interpolation points. xval[i][0] is the first component of interpolation point i,
                xval[i][1] is the second component, and so on until xval[i][d-1], the last component of that
                interpolation point (where d is thus the dimension of the space).
            yval (double[]): the values for the interpolation points
        
        Returns:
            a function which interpolates the data set
        
        Raises:
            MathIllegalArgumentException: if the space dimension of the given samples does not match the space dimension of the microsphere.
            NullArgumentException: if the arguments are null.
        
        
        """
        ...

class NevilleInterpolator(UnivariateInterpolator, java.io.Serializable):
    """
    implements UnivariateInterpolator, Serializable
    
    Implements the ` Neville's Algorithm <http://mathworld.wolfram.com/NevillesAlgorithm.html>` for interpolation of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 2.
    
    The actual code of Neville's algorithm is in PolynomialFunctionLagrangeForm, this class provides an easy-to-use interface to it.
    
          - serialized
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def interpolate(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialFunctionLagrangeForm:
        """
        Computes an interpolating function for the data set.
        
        Specified by: interpolate in interface UnivariateInterpolator
        
        Parameters:
            x (double[]): Interpolating points.
            y (double[]): Interpolating values.
        
        Returns:
            a function which interpolates the data set
        
        Raises:
            MathIllegalArgumentException: if the array lengths are different.
            MathIllegalArgumentException: if the number of points is less than 2.
            MathIllegalArgumentException: if two abscissae have the same value.
        
        
        """
        ...

class PiecewiseBicubicSplineInterpolator(BivariateGridInterpolator):
    """
    implements BivariateGridInterpolator
    
    Generates a piecewise-bicubic interpolating function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> PiecewiseBicubicSplineInterpolatingFunction:
        """
        Compute an interpolating function for the dataset.
        
        Specified by: interpolate in interface BivariateGridInterpolator
        
        Parameters:
            xval (double[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (double[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            fval (double[][]): The values of the interpolation points on all the grid knots: fval[i][j] = f(xval[i], yval[j]).
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if the array is not sorted.
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
            NullArgumentException: 
        
        """
        ...

class SplineInterpolator(UnivariateInterpolator, FieldUnivariateInterpolator):
    def __init__(self): ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, tArray: typing.Union[typing.List[_interpolate_0__T], jpype.JArray], tArray2: typing.Union[typing.List[_interpolate_0__T], jpype.JArray]) -> org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction[_interpolate_0__T]: ...
    @typing.overload
    def interpolate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.polynomials.PolynomialSplineFunction: ...

class TricubicInterpolator(TrivariateGridInterpolator):
    """
    implements TrivariateGridInterpolator
    
    Generates a tricubic interpolating function.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray], zval: typing.Union[typing.List[float], jpype.JArray], fval: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]) -> TricubicInterpolatingFunction:
        """
        Compute an interpolating function for the dataset.
        
        Specified by: interpolate in interface TrivariateGridInterpolator
        
        Parameters:
            xval (double[]): All the x-coordinates of the interpolation points, sorted in increasing order.
            yval (double[]): All the y-coordinates of the interpolation points, sorted in increasing order.
            zval (double[]): All the z-coordinates of the interpolation points, sorted in increasing order.
            fval (double[][][]): the values of the interpolation points on all the grid knots: fval[i][j][k] = f(xval[i], yval[j], zval[k]).
        
        Returns:
            a function that interpolates the data set.
        
        Raises:
            MathIllegalArgumentException: if any of the arrays has zero length.
            MathIllegalArgumentException: if the array lengths are inconsistent.
            MathIllegalArgumentException: if arrays are not sorted
            MathIllegalArgumentException: if the number of points is too small for the order of the interpolation
        
        
        """
        ...

class UnivariatePeriodicInterpolator(UnivariateInterpolator):
    """
    implements UnivariateInterpolator
    
    Adapter for classes implementing the UnivariateInterpolator interface. The data to be interpolated is assumed to be periodic. Thus values that are outside of the range can be passed to the interpolation function: They will be wrapped into the initial range before being passed to the class that actually computes the interpolation.
    """
    DEFAULT_EXTEND: typing.ClassVar[int] = ...
    """
    Default number of extension points of the samples array.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, univariateInterpolator: typing.Union[UnivariateInterpolator, typing.Callable], double: float): ...
    @typing.overload
    def __init__(self, univariateInterpolator: typing.Union[UnivariateInterpolator, typing.Callable], double: float, int: int): ...
    def interpolate(self, xval: typing.Union[typing.List[float], jpype.JArray], yval: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.analysis.UnivariateFunction:
        """
        Compute an interpolating function for the dataset.
        
        Specified by: interpolate in interface UnivariateInterpolator
        
        Parameters:
            xval (double[]): Arguments for the interpolation points.
            yval (double[]): Values for the interpolation points.
        
        Returns:
            a function which interpolates the dataset.
        
        Raises:
            MathIllegalArgumentException: if the number of extension points is larger than the size of xval.
        
        
        """
        ...


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
