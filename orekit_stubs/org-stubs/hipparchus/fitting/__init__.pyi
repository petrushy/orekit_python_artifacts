
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
    public abstract classAbstractCurveFitter extends :class:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Base class that contains common code for fitting parametric univariate real functions :code:`y = f(p :sub:`i` ;x)`,
        where :code:`x` is the independent variable and the :code:`p :sub:`i`` are the *parameters*.
    
    
        A fitter will find the optimal values of the parameters by *fitting* the curve so it remains very close to a set of
        :code:`N` observed points :code:`(x :sub:`k` , y :sub:`k` )`, :code:`0 <= k < N`.
    
    
        An algorithm usually performs the fit by finding the parameter values that minimizes the objective function
    
        .. code-block: java
        
          ∑y :sub:`k`  - f(x :sub:`k` ) :sup:`2` ,
         
        which is actually a least-squares problem. This class contains boilerplate code for calling the
        :meth:`~org.hipparchus.fitting.AbstractCurveFitter.fit` method for obtaining the parameters. The problem setup, such as
        the choice of optimization algorithm for fitting a specific function is delegated to subclasses.
    """
    def fit(self, collection: typing.Union[java.util.Collection['WeightedObservedPoint'], typing.Sequence['WeightedObservedPoint'], typing.Set['WeightedObservedPoint']]) -> typing.MutableSequence[float]: ...

class WeightedObservedPoint(java.io.Serializable):
    """
    public classWeightedObservedPoint extends :class:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class is a simple container for weighted observed point in :class:`~org.hipparchus.fitting.AbstractCurveFitter`.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, double3: float): ...
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
    public classWeightedObservedPoints extends :class:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Simple container for weighted observed points used in :class:`~org.hipparchus.fitting.AbstractCurveFitter` algorithms.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self): ...
    @typing.overload
    def add(self, double: float, double2: float) -> None:
        """
            Adds a point to the sample. Calling this method is equivalent to calling :code:`add(1.0, x, y)`.
        
            Parameters:
                x (double): Abscissa of the point.
                y (double): Observed value at :code:`x`. After fitting we should have :code:`f(x)` as close as possible to this value.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.toList`
        
        
            Adds a point to the sample.
        
            Parameters:
                weight (double): Weight of the observed point.
                x (double): Abscissa of the point.
                y (double): Observed value at :code:`x`. After fitting we should have :code:`f(x)` as close as possible to this value.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.toList`
        
        
        """
        ...
    @typing.overload
    def add(self, double: float, double2: float, double3: float) -> None: ...
    @typing.overload
    def add(self, weightedObservedPoint: WeightedObservedPoint) -> None:
        """
            Adds a point to the sample.
        
            Parameters:
                observed (:class:`~org.hipparchus.fitting.WeightedObservedPoint`): Observed point to add.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`
                  - :meth:`~org.hipparchus.fitting.WeightedObservedPoints.toList`
        
        
        
        """
        ...
    def clear(self) -> None:
        """
            Removes all observations from this container.
        
        """
        ...
    def toList(self) -> java.util.List[WeightedObservedPoint]: ...

class GaussianCurveFitter(AbstractCurveFitter):
    """
    public classGaussianCurveFitter extends :class:`~org.hipparchus.fitting.AbstractCurveFitter`
    
        Fits points to a :class:`~org.hipparchus.fitting.https:.www.hipparchus.org.hipparchus` function.
    
    
        The :meth:`~org.hipparchus.fitting.GaussianCurveFitter.withStartPoint` must be passed in the following order:
    
          - Normalization
          - Mean
          - Sigma
    
        The optimal values will be returned in the same order.
    
        Usage example:
    
        .. code-block: java
        
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
            Creates a default curve fitter. The initial guess for the parameters will be
            :class:`~org.hipparchus.fitting.GaussianCurveFitter.ParameterGuesser` computed automatically, and the maximum number of
            iterations of the optimization algorithm is set to
            :meth:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Integer.MAX_VALUE`.
        
            Returns:
                a curve fitter.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fitting.GaussianCurveFitter.withStartPoint`
                  - :meth:`~org.hipparchus.fitting.GaussianCurveFitter.withMaxIterations`
        
        
        
        """
        ...
    def withMaxIterations(self, int: int) -> 'GaussianCurveFitter':
        """
            Configure the maximum number of iterations.
        
            Parameters:
                newMaxIter (int): maximum number of iterations
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withStartPoint(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'GaussianCurveFitter':
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
    public classHarmonicCurveFitter extends :class:`~org.hipparchus.fitting.AbstractCurveFitter`
    
        Fits points to a :class:`~org.hipparchus.fitting.https:.www.hipparchus.org.hipparchus` function.
    
    
        The :meth:`~org.hipparchus.fitting.HarmonicCurveFitter.withStartPoint` must be passed in the following order:
    
          - Amplitude
          - Angular frequency
          - phase
    
        The optimal values will be returned in the same order.
    """
    @staticmethod
    def create() -> 'HarmonicCurveFitter':
        """
            Creates a default curve fitter. The initial guess for the parameters will be
            :class:`~org.hipparchus.fitting.HarmonicCurveFitter.ParameterGuesser` computed automatically, and the maximum number of
            iterations of the optimization algorithm is set to
            :meth:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Integer.MAX_VALUE`.
        
            Returns:
                a curve fitter.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fitting.HarmonicCurveFitter.withStartPoint`
                  - :meth:`~org.hipparchus.fitting.HarmonicCurveFitter.withMaxIterations`
        
        
        
        """
        ...
    def withMaxIterations(self, int: int) -> 'HarmonicCurveFitter':
        """
            Configure the maximum number of iterations.
        
            Parameters:
                newMaxIter (int): maximum number of iterations
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withStartPoint(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'HarmonicCurveFitter':
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
    public classPolynomialCurveFitter extends :class:`~org.hipparchus.fitting.AbstractCurveFitter`
    
        Fits points to a :class:`~org.hipparchus.fitting.https:.www.hipparchus.org.hipparchus` function.
    
    
        The size of the :meth:`~org.hipparchus.fitting.PolynomialCurveFitter.withStartPoint` array defines the degree of the
        polynomial to be fitted. They must be sorted in increasing order of the polynomial's degree. The optimal values of the
        coefficients will be returned in the same order.
    """
    @staticmethod
    def create(int: int) -> 'PolynomialCurveFitter':
        """
            Creates a default curve fitter. Zero will be used as initial guess for the coefficients, and the maximum number of
            iterations of the optimization algorithm is set to
            :meth:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Integer.MAX_VALUE`.
        
            Parameters:
                degree (int): Degree of the polynomial to be fitted.
        
            Returns:
                a curve fitter.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fitting.PolynomialCurveFitter.withStartPoint`
                  - :meth:`~org.hipparchus.fitting.PolynomialCurveFitter.withMaxIterations`
        
        
        
        """
        ...
    def withMaxIterations(self, int: int) -> 'PolynomialCurveFitter':
        """
            Configure the maximum number of iterations.
        
            Parameters:
                newMaxIter (int): maximum number of iterations
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withStartPoint(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'PolynomialCurveFitter':
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
    public classSimpleCurveFitter extends :class:`~org.hipparchus.fitting.AbstractCurveFitter`
    
        Fits points to a user-defined :class:`~org.hipparchus.fitting.https:.www.hipparchus.org.hipparchus`.
    """
    @staticmethod
    def create(parametricUnivariateFunction: org.hipparchus.analysis.ParametricUnivariateFunction, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'SimpleCurveFitter':
        """
            Creates a curve fitter. The maximum number of iterations of the optimization algorithm is set to
            :meth:`~org.hipparchus.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Integer.MAX_VALUE`.
        
            Parameters:
                f (:class:`~org.hipparchus.fitting.https:.www.hipparchus.org.hipparchus`): Function to fit.
                start (double[]): Initial guess for the parameters. Cannot be :code:`null`. Its length must be consistent with the number of parameters of
                    the function to fit.
        
            Returns:
                a curve fitter.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fitting.SimpleCurveFitter.withStartPoint`
                  - :meth:`~org.hipparchus.fitting.SimpleCurveFitter.withMaxIterations`
        
        
        
        """
        ...
    def withMaxIterations(self, int: int) -> 'SimpleCurveFitter':
        """
            Configure the maximum number of iterations.
        
            Parameters:
                newMaxIter (int): maximum number of iterations
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withStartPoint(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'SimpleCurveFitter':
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
