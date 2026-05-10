
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import jpype
import org.hipparchus.analysis
import typing



class AbstractCurveFitter:
    """
    Base class that contains common code for fitting parametric univariate real functions i` ;x)`, where x is the independent variable and the i`` are the parameters.
    
    A fitter will find the optimal values of the parameters by fitting the curve so it remains very close to a set of N observed points k` , y :sub:`k` )`, 0 <= k < N.
    
    An algorithm usually performs the fit by finding the parameter values that minimizes the objective function
    
      ∑y :sub:`k`  - f(x :sub:`k` ) :sup:`2` , which is actually a least-squares problem. This class contains boilerplate code for calling the fit method for obtaining the parameters. The problem setup, such as the choice of optimization algorithm for fitting a specific function is delegated to subclasses.
    """
    def fit(self, points: typing.Union[java.util.Collection['WeightedObservedPoint'], typing.Sequence['WeightedObservedPoint'], typing.Set['WeightedObservedPoint']]) -> typing.MutableSequence[float]:
        """
        Fits a curve. This method computes the coefficients of the curve that best fit the sample of observed points.
        
        Parameters:
            points (Collection<WeightedObservedPoint> points): Observations.
        
        Returns:
            the fitted parameters.
        
        
        """
        ...

class WeightedObservedPoint(java.io.Serializable):
    """
    This class is a simple container for weighted observed point in AbstractCurveFitter.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        serialized
    """
    def __init__(self, weight: float, x: float, y: float):
        """
        Simple constructor.
        
        Parameters:
            weight (double): Weight of the measurement in the fitting process.
            x (double): Abscissa of the measurement.
            y (double): Ordinate of the measurement.
        
        
        """
        ...
    def getWeight(self) -> float:
        """
        Gets the weight of the measurement in the fitting process.
        
        Returns:
            the weight of the measurement in the fitting process.
        
        
        """
        ...
    def getX(self) -> float:
        """
        Gets the abscissa of the point.
        
        Returns:
            the abscissa of the point.
        
        
        """
        ...
    def getY(self) -> float:
        """
        Gets the observed value of the function at x.
        
        Returns:
            the observed value of the function at x.
        
        
        """
        ...

class WeightedObservedPoints(java.io.Serializable):
    """
    Simple container for weighted observed points used in AbstractCurveFitter algorithms.
    
    Also see:
        serialized
    """
    def __init__(self):
        """
        Simple constructor.
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    def add(self, x: float, y: float) -> None:
        """
        Adds a point to the sample. Calling this method is equivalent to calling 0, x, y).
        
        Parameters:
            x (double): Abscissa of the point.
            y (double): Observed value at x. After fitting we should have f(x) as close as possible to this value.
        
        Also see:
            add, add,
            toList
        
        Adds a point to the sample.
        
        Parameters:
            weight (double): Weight of the observed point.
            x (double): Abscissa of the point.
            y (double): Observed value at x. After fitting we should have f(x) as close as possible to this value.
        
        Also see:
            add, add,
            toList
        
        """
        ...
    @typing.overload
    def add(self, weight: float, x: float, y: float) -> None: ...
    @typing.overload
    def add(self, observed: WeightedObservedPoint) -> None:
        """
        Adds a point to the sample.
        
        Parameters:
            observed (WeightedObservedPoint): Observed point to add.
        
        Also see:
            add, add,
            toList
        
        
        """
        ...
    def clear(self) -> None:
        """
        Removes all observations from this container.
        """
        ...
    def toList(self) -> java.util.List[WeightedObservedPoint]:
        """
        Gets a snapshot of the observed points. The list of stored points is copied in order to ensure that modification of the returned instance does not affect this container. Conversely, further modification of this container (through the add or clear methods) will not affect the returned list.
        
        Returns:
            the observed points, in the order they were added to this container.
        
        Also see:
            add, add,
            add
        
        
        """
        ...

class GaussianCurveFitter(AbstractCurveFitter):
    """
    Fits points to a hipparchus function.
    
    The withStartPoint must be passed in the following order:
    
      - Normalization
      - Mean
      - Sigma
    
    The optimal values will be returned in the same order.
    
    Usage example:
    
    
       WeightedObservedPoints obs = new WeightedObservedPoints();
       obs.add(4.0254623,  531026.0);
       obs.add(4.03128248, 984167.0);
       obs.add(4.03839603, 1887233.0);
       obs.add(4.04421621, 2687152.0);
       obs.add(4.05132976, 3461228.0);
       obs.add(4.05326982, 3580526.0);
       obs.add(4.05779662, 3439750.0);
       obs.add(4.0636168,  2877648.0);
       obs.add(4.06943698, 2175960.0);
       obs.add(4.07525716, 1447024.0);
       obs.add(4.08237071, 717104.0);
       obs.add(4.08366408, 620014.0);
       double[] parameters = GaussianCurveFitter.create().fit(obs.toList());
    """
    @staticmethod
    def create() -> 'GaussianCurveFitter':
        """
        Creates a default curve fitter. The initial guess for the parameters will be ParameterGuesser computed automatically, and the maximum number of iterations of the optimization algorithm is set to Integer.
        
        Returns:
            a curve fitter.
        
        Also see:
            withStartPoint,
            withMaxIterations
        
        
        """
        ...
    def withMaxIterations(self, newMaxIter: int) -> 'GaussianCurveFitter':
        """
        Configure the maximum number of iterations.
        
        Parameters:
            newMaxIter (int): maximum number of iterations
        
        Returns:
            a new instance.
        
        
        """
        ...
    def withStartPoint(self, newStart: typing.Union[typing.List[float], jpype.JArray]) -> 'GaussianCurveFitter':
        """
        Configure the start point (initial guess).
        
        Parameters:
            newStart (double[]): new start point (initial guess)
        
        Returns:
            a new instance.
        
        
        """
        ...
    class ParameterGuesser:
        def __init__(self, collection: typing.Union[java.util.Collection[WeightedObservedPoint], typing.Sequence[WeightedObservedPoint], typing.Set[WeightedObservedPoint]]): ...
        def guess(self) -> typing.MutableSequence[float]: ...

class HarmonicCurveFitter(AbstractCurveFitter):
    """
    Fits points to a hipparchus function.
    
    The withStartPoint must be passed in the following order:
    
      - Amplitude
      - Angular frequency
      - phase
    
    The optimal values will be returned in the same order.
    """
    @staticmethod
    def create() -> 'HarmonicCurveFitter':
        """
        Creates a default curve fitter. The initial guess for the parameters will be ParameterGuesser computed automatically, and the maximum number of iterations of the optimization algorithm is set to Integer.
        
        Returns:
            a curve fitter.
        
        Also see:
            withStartPoint,
            withMaxIterations
        
        
        """
        ...
    def withMaxIterations(self, newMaxIter: int) -> 'HarmonicCurveFitter':
        """
        Configure the maximum number of iterations.
        
        Parameters:
            newMaxIter (int): maximum number of iterations
        
        Returns:
            a new instance.
        
        
        """
        ...
    def withStartPoint(self, newStart: typing.Union[typing.List[float], jpype.JArray]) -> 'HarmonicCurveFitter':
        """
        Configure the start point (initial guess).
        
        Parameters:
            newStart (double[]): new start point (initial guess)
        
        Returns:
            a new instance.
        
        
        """
        ...
    class ParameterGuesser:
        def __init__(self, collection: typing.Union[java.util.Collection[WeightedObservedPoint], typing.Sequence[WeightedObservedPoint], typing.Set[WeightedObservedPoint]]): ...
        def guess(self) -> typing.MutableSequence[float]: ...

class PolynomialCurveFitter(AbstractCurveFitter):
    """
    Fits points to a hipparchus function.
    
    The size of the withStartPoint array defines the degree of the polynomial to be fitted. They must be sorted in increasing order of the polynomial's degree. The optimal values of the coefficients will be returned in the same order.
    """
    @staticmethod
    def create(degree: int) -> 'PolynomialCurveFitter':
        """
        Creates a default curve fitter. Zero will be used as initial guess for the coefficients, and the maximum number of iterations of the optimization algorithm is set to Integer.
        
        Parameters:
            degree (int): Degree of the polynomial to be fitted.
        
        Returns:
            a curve fitter.
        
        Also see:
            withStartPoint,
            withMaxIterations
        
        
        """
        ...
    def withMaxIterations(self, newMaxIter: int) -> 'PolynomialCurveFitter':
        """
        Configure the maximum number of iterations.
        
        Parameters:
            newMaxIter (int): maximum number of iterations
        
        Returns:
            a new instance.
        
        
        """
        ...
    def withStartPoint(self, newStart: typing.Union[typing.List[float], jpype.JArray]) -> 'PolynomialCurveFitter':
        """
        Configure the start point (initial guess).
        
        Parameters:
            newStart (double[]): new start point (initial guess)
        
        Returns:
            a new instance.
        
        
        """
        ...

class SimpleCurveFitter(AbstractCurveFitter):
    """
    Fits points to a user-defined hipparchus.
    """
    @staticmethod
    def create(f: org.hipparchus.analysis.ParametricUnivariateFunction, start: typing.Union[typing.List[float], jpype.JArray]) -> 'SimpleCurveFitter':
        """
        Creates a curve fitter. The maximum number of iterations of the optimization algorithm is set to Integer.
        
        Parameters:
            f (hipparchus): Function to fit.
            start (double[]): Initial guess for the parameters. Cannot be null. Its length must be consistent with the number of parameters of
                the function to fit.
        
        Returns:
            a curve fitter.
        
        Also see:
            withStartPoint,
            withMaxIterations
        
        
        """
        ...
    def withMaxIterations(self, newMaxIter: int) -> 'SimpleCurveFitter':
        """
        Configure the maximum number of iterations.
        
        Parameters:
            newMaxIter (int): maximum number of iterations
        
        Returns:
            a new instance.
        
        
        """
        ...
    def withStartPoint(self, newStart: typing.Union[typing.List[float], jpype.JArray]) -> 'SimpleCurveFitter':
        """
        Configure the start point (initial guess).
        
        Parameters:
            newStart (double[]): new start point (initial guess)
        
        Returns:
            a new instance.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.fitting")``.

    AbstractCurveFitter: typing.Type[AbstractCurveFitter]
    GaussianCurveFitter: typing.Type[GaussianCurveFitter]
    HarmonicCurveFitter: typing.Type[HarmonicCurveFitter]
    PolynomialCurveFitter: typing.Type[PolynomialCurveFitter]
    SimpleCurveFitter: typing.Type[SimpleCurveFitter]
    WeightedObservedPoint: typing.Type[WeightedObservedPoint]
    WeightedObservedPoints: typing.Type[WeightedObservedPoints]
