import java.io
import java.util
import org.hipparchus.analysis
import typing



class AbstractCurveFitter:
    def __init__(self): ...
    def fit(self, collection: typing.Union[java.util.Collection['WeightedObservedPoint'], typing.Sequence['WeightedObservedPoint'], typing.Set['WeightedObservedPoint']]) -> typing.List[float]: ...

class WeightedObservedPoint(java.io.Serializable):
    """
    public class WeightedObservedPoint extends Object implements Serializable
    
        This class is a simple container for weighted observed point in :class:`~org.hipparchus.fitting.AbstractCurveFitter`.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :meth:`~serialized`
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
    public class WeightedObservedPoints extends Object implements Serializable
    
        Simple container for weighted observed points used in :class:`~org.hipparchus.fitting.AbstractCurveFitter` algorithms.
    
        Also see:
            :meth:`~serialized`
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
                :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`, :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`,
                :meth:`~org.hipparchus.fitting.WeightedObservedPoints.toList`
        
            Adds a point to the sample.
        
            Parameters:
                weight (double): Weight of the observed point.
                x (double): Abscissa of the point.
                y (double): Observed value at :code:`x`. After fitting we should have :code:`f(x)` as close as possible to this value.
        
            Also see:
                :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`, :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`,
                :meth:`~org.hipparchus.fitting.WeightedObservedPoints.toList`
        
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
                :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`, :meth:`~org.hipparchus.fitting.WeightedObservedPoints.add`,
                :meth:`~org.hipparchus.fitting.WeightedObservedPoints.toList`
        
        
        """
        ...
    def clear(self) -> None:
        """
            Removes all observations from this container.
        
        """
        ...
    def toList(self) -> java.util.List[WeightedObservedPoint]: ...

class GaussianCurveFitter(AbstractCurveFitter):
    @staticmethod
    def create() -> 'GaussianCurveFitter': ...
    def withMaxIterations(self, int: int) -> 'GaussianCurveFitter': ...
    def withStartPoint(self, doubleArray: typing.List[float]) -> 'GaussianCurveFitter': ...
    class ParameterGuesser:
        def __init__(self, collection: typing.Union[java.util.Collection[WeightedObservedPoint], typing.Sequence[WeightedObservedPoint], typing.Set[WeightedObservedPoint]]): ...
        def guess(self) -> typing.List[float]: ...

class HarmonicCurveFitter(AbstractCurveFitter):
    @staticmethod
    def create() -> 'HarmonicCurveFitter': ...
    def withMaxIterations(self, int: int) -> 'HarmonicCurveFitter': ...
    def withStartPoint(self, doubleArray: typing.List[float]) -> 'HarmonicCurveFitter': ...
    class ParameterGuesser:
        def __init__(self, collection: typing.Union[java.util.Collection[WeightedObservedPoint], typing.Sequence[WeightedObservedPoint], typing.Set[WeightedObservedPoint]]): ...
        def guess(self) -> typing.List[float]: ...

class PolynomialCurveFitter(AbstractCurveFitter):
    @staticmethod
    def create(int: int) -> 'PolynomialCurveFitter': ...
    def withMaxIterations(self, int: int) -> 'PolynomialCurveFitter': ...
    def withStartPoint(self, doubleArray: typing.List[float]) -> 'PolynomialCurveFitter': ...

class SimpleCurveFitter(AbstractCurveFitter):
    """
    public class SimpleCurveFitter extends :class:`~org.hipparchus.fitting.AbstractCurveFitter`
    
        Fits points to a user-defined null.
    """
    @staticmethod
    def create(parametricUnivariateFunction: org.hipparchus.analysis.ParametricUnivariateFunction, doubleArray: typing.List[float]) -> 'SimpleCurveFitter':
        """
            Creates a curve fitter. The maximum number of iterations of the optimization algorithm is set to null.
        
            Parameters:
                f (ParametricUnivariateFunction): Function to fit.
                start (double[]): Initial guess for the parameters. Cannot be :code:`null`. Its length must be consistent with the number of parameters of
                    the function to fit.
        
            Returns:
                a curve fitter.
        
            Also see:
                null, :meth:`~org.hipparchus.fitting.SimpleCurveFitter.withMaxIterations`
        
        
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
    def withStartPoint(self, doubleArray: typing.List[float]) -> 'SimpleCurveFitter':
        """
            Configure the start point (initial guess).
        
            Parameters:
                newStart (double[]): new start point (initial guess)
        
            Returns:
                a new instance.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.fitting")``.

    AbstractCurveFitter: typing.Type[AbstractCurveFitter]
    GaussianCurveFitter: typing.Type[GaussianCurveFitter]
    HarmonicCurveFitter: typing.Type[HarmonicCurveFitter]
    PolynomialCurveFitter: typing.Type[PolynomialCurveFitter]
    SimpleCurveFitter: typing.Type[SimpleCurveFitter]
    WeightedObservedPoint: typing.Type[WeightedObservedPoint]
    WeightedObservedPoints: typing.Type[WeightedObservedPoints]
