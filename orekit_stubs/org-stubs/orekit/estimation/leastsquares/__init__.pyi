
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.hipparchus.util
import org.orekit.estimation.measurements
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.conversion
import org.orekit.propagation.integration
import org.orekit.utils
import typing



class AbstractBatchLSModel(org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction):
    """
    Bridge between ObservedMeasurement and LeastSquaresProblem.
    
    Since:
        11.0
    """
    def __init__(self, propagatorBuilders: typing.Union[typing.List[org.orekit.propagation.conversion.PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union['ModelObserver', typing.Callable]):
        """
        Constructor.
        
        Parameters:
            propagatorBuilders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        
        """
        ...
    def createPropagators(self, point: org.hipparchus.linear.RealVector) -> typing.MutableSequence[org.orekit.propagation.Propagator]:
        """
        Create the propagators and parameters corresponding to an evaluation point.
        
        Parameters:
            point (RealVector): evaluation point
        
        Returns:
            an array of new propagators
        
        
        """
        ...
    def fetchEvaluatedMeasurement(self, index: int, evaluation: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> None:
        """
        Fetch a measurement that was evaluated during propagation.
        
        Parameters:
            index (int): index of the measurement first component
            evaluation (EstimatedMeasurement<?> evaluation): measurement evaluation
        
        
        """
        ...
    def getEvaluationsCount(self) -> int:
        """
        Get the evaluations count.
        
        Returns:
            evaluations count
        
        
        """
        ...
    def getIterationsCount(self) -> int:
        """
        Get the iterations count.
        
        Returns:
            iterations count
        
        
        """
        ...
    def getSelectedOrbitalParametersDriversForBuilder(self, iBuilder: int) -> org.orekit.utils.ParameterDriversList:
        """
        Get the selected orbital drivers for a propagatorBuilder.
        
        Parameters:
            iBuilder (int): index of the builder in the builders' array
        
        Returns:
            the list of selected orbital drivers for propagatorBuilder of index iBuilder
        
        Since:
            11.1
        
        
        """
        ...
    def getSelectedPropagationDriversForBuilder(self, iBuilder: int) -> org.orekit.utils.ParameterDriversList:
        """
        Get the selected propagation drivers for a propagatorBuilder.
        
        Parameters:
            iBuilder (int): index of the builder in the builders' array
        
        Returns:
            the list of selected propagation drivers for propagatorBuilder of index iBuilder
        
        
        """
        ...
    def isForwardPropagation(self) -> bool:
        """
        Return the forward propagation flag.
        
        Returns:
            the forward propagation flag
        
        
        """
        ...
    def setEvaluationsCounter(self, evaluationsCounter: org.hipparchus.util.Incrementor) -> None:
        """
        Set the counter for evaluations.
        
        Parameters:
            evaluationsCounter (Incrementor): counter for evaluations
        
        
        """
        ...
    def setIterationsCounter(self, iterationsCounter: org.hipparchus.util.Incrementor) -> None:
        """
        Set the counter for iterations.
        
        Parameters:
            iterationsCounter (Incrementor): counter for iterations
        
        
        """
        ...
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]:
        """
        Specified by: meth:`~org.orekit.estimation.leastsquares.https:.www.hipparchus.org.apidocs.org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction.html?is` in interface MultivariateJacobianFunction
        
        
        """
        ...

class BatchLSEstimator:
    """
    Least squares estimator for orbit determination.
    
    The least squares estimator can be used with different orbit propagators in Orekit. Current propagators list of usable propagators are NumericalPropagator, DSSTPropagator, BrouwerLyddanePropagator, EcksteinHechlerPropagator, TLEPropagator, KeplerianPropagator, and Ephemeris.
    
    Since:
        8.0
    """
    def __init__(self, optimizer: typing.Union[org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer, typing.Callable], *propagatorBuilder: org.orekit.propagation.conversion.PropagatorBuilder):
        """
        Simple constructor.
        
        If multiple PropagatorBuilder are set up, the orbits of several spacecrafts will be used simultaneously. This is useful if the propagators share some model or measurements parameters (typically pole motion, prime meridian correction or ground stations positions).
        
        Setting up multiple PropagatorBuilder is also useful when inter-satellite measurements are used, even if only one of the orbit is estimated and the other ones are fixed. This is typically used when very high accuracy GNSS measurements are needed and the navigation bulletins are not considered accurate enough and the navigation constellation must be propagated numerically.
        
        Parameters:
            optimizer (LeastSquaresOptimizer): solver for least squares problem
            propagatorBuilder (PropagatorBuilder...): builders to use for propagation
        
        
        """
        ...
    def addMeasurement(self, measurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> None:
        """
        Add a measurement.
        
        Parameters:
            measurement (ObservedMeasurement<?> measurement): measurement to add
        
        
        """
        ...
    def estimate(self) -> typing.MutableSequence[org.orekit.propagation.Propagator]:
        """
        Estimate the orbital, propagation and measurements parameters.
        
        The initial guess for all parameters must have been set before calling this method using getOrbitalParametersDrivers, getPropagatorParametersDrivers, and getMeasurementsParametersDrivers and then setValue of the parameters.
        
        For parameters whose reference date has not been set to a non-null date beforehand (i.e. the parameters for which getReferenceDate returns null, a default reference date will be set automatically at the start of the estimation to the getInitialOrbitDate of the first propagator builder. For parameters whose reference date has been set to a non-null date, this reference date is untouched.
        
        After this method returns, the estimated parameters can be retrieved using getOrbitalParametersDrivers, getPropagatorParametersDrivers, and getMeasurementsParametersDrivers and then getValue of the parameters.
        
        As a convenience, the method also returns a fully configured and ready to use propagator set up with all the estimated values.
        
        For even more in-depth information, the getOptimum method provides detailed elements (covariance matrix, estimated parameters standard deviation, weighted Jacobian, RMS, χ², residuals and more).
        
        Returns:
            propagators configured with estimated orbits as initial states, and all propagators estimated parameters also set
        
        
        """
        ...
    def getEvaluationsCount(self) -> int:
        """
        Get the number of evaluations used for last estimation.
        
        Returns:
            number of evaluations used for last estimation
        
        Also see:
            setMaxEvaluations
        
        
        """
        ...
    def getIterationsCount(self) -> int:
        """
        Get the number of iterations used for last estimation.
        
        Returns:
            number of iterations used for last estimation
        
        Also see:
            setMaxIterations
        
        
        """
        ...
    def getLastEstimations(self) -> java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]:
        """
        Get the last estimations performed.
        
        Returns:
            last estimations performed
        
        
        """
        ...
    def getMeasurementsParametersDrivers(self, estimatedOnly: bool) -> org.orekit.utils.ParameterDriversList:
        """
        Get the measurements parameters supported by this estimator (including measurements and modifiers).
        
        Parameters:
            estimatedOnly (boolean): if true, only estimated parameters are returned
        
        Returns:
            measurements parameters supported by this estimator
        
        
        """
        ...
    def getOptimum(self) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.Optimum:
        """
        Get the optimum found.
        
        The Optimum object contains detailed elements (covariance matrix, estimated parameters standard deviation, weighted Jacobian, RMS, χ², residuals and more).
        
        Beware that the returned object is the raw view from the underlying mathematical library. At this raw level, parameters have getNormalizedValue whereas the space flight parameters have getValue with their units. So there are getScale to apply when using these elements.
        
        Returns:
            optimum found after last call to estimate
        
        
        """
        ...
    def getOrbitalParametersDrivers(self, estimatedOnly: bool) -> org.orekit.utils.ParameterDriversList:
        """
        Get the orbital parameters supported by this estimator.
        
        If there are more than one propagator builder, then the names of the drivers have an index marker in square brackets appended to them in order to distinguish the various orbits. So for example with one builder generating Keplerian orbits the names would be simply "a", "e", "i"... but if there are several builders the names would be "a[0]", "e[0]", "i[0]"..."a[1]", "e[1]", "i[1]"...
        
        Parameters:
            estimatedOnly (boolean): if true, only estimated parameters are returned
        
        Returns:
            orbital parameters supported by this estimator
        
        
        """
        ...
    def getPhysicalCovariances(self, threshold: float) -> org.hipparchus.linear.RealMatrix:
        """
        Get the covariances matrix in space flight dynamics physical units.
        
        This method retrieve the Evaluation from the [@link getOptimum and applies the scaling factors to it in order to convert it from raw normalized values back to physical values.
        
        Parameters:
            threshold (double): threshold to identify matrix singularity
        
        Returns:
            covariances matrix in space flight dynamics physical units
        
        Since:
            9.1
        
        
        """
        ...
    def getPropagatorParametersDrivers(self, estimatedOnly: bool) -> org.orekit.utils.ParameterDriversList:
        """
        Get the propagator parameters supported by this estimator.
        
        Parameters:
            estimatedOnly (boolean): if true, only estimated parameters are returned
        
        Returns:
            propagator parameters supported by this estimator
        
        
        """
        ...
    def setConvergenceChecker(self, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation], typing.Callable[[int, org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation, org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation], bool]]) -> None:
        """
        Set a custom convergence checker.
        
        Calling this method overrides any checker that could have been set beforehand by calling setParametersConvergenceThreshold. Both methods are mutually exclusive.
        
        Parameters:
            convergenceChecker (ConvergenceChecker<Evaluation> convergenceChecker): convergence checker to set
        
        Since:
            10.1
        
        Also see:
            setParametersConvergenceThreshold
        
        
        """
        ...
    def setMaxEvaluations(self, maxEvaluations: int) -> None:
        """
        Set the maximum number of model evaluations.
        
        The evaluations correspond to the orbit propagations and measurements estimations performed with a set of estimated parameters.
        
        For GaussNewtonOptimizer there is one evaluation at each iteration, so the maximum numbers may be set to the same value. For LevenbergMarquardtOptimizer, there can be several evaluations at some iterations (typically for the first couple of iterations), so the maximum number of evaluations may be set to a higher value than the maximum number of iterations.
        
        Parameters:
            maxEvaluations (int): maximum number of model evaluations
        
        Also see:
            setMaxIterations,
            getEvaluationsCount
        
        
        """
        ...
    def setMaxIterations(self, maxIterations: int) -> None:
        """
        Set the maximum number of iterations.
        
        The iterations correspond to the top level iterations of the LeastSquaresOptimizer.
        
        Parameters:
            maxIterations (int): maxIterations maximum number of iterations
        
        Also see:
            setMaxEvaluations,
            getIterationsCount
        
        
        """
        ...
    def setObserver(self, observer: typing.Union['BatchLSObserver', typing.Callable]) -> None:
        """
        Set an observer for iterations.
        
        Parameters:
            observer (BatchLSObserver): observer to be notified at the end of each iteration
        
        
        """
        ...
    def setParametersConvergenceThreshold(self, parametersConvergenceThreshold: float) -> None:
        """
        Set convergence threshold.
        
        The convergence used for estimation is based on the estimated parameters getNormalizedValue. Convergence is considered to have been reached when the difference between previous and current normalized value is less than the convergence threshold for all parameters. The same value is used for all parameters since they are normalized and hence dimensionless.
        
        Normalized values are computed as (current - reference)/scale, so convergence is reached when the following condition holds for all estimated parameters: |current[i] - previous[i]| <= threshold * scale[i]
        
        So the convergence threshold specified here can be considered as a multiplication factor applied to scale. Since for all parameters the scale is often small (typically about 1 m for orbital positions for example), then the threshold should not be too small. A value of 10⁻³ is often quite accurate.
        
        Calling this method overrides any checker that could have been set beforehand by calling setConvergenceChecker. Both methods are mutually exclusive.
        
        Parameters:
            parametersConvergenceThreshold (double): convergence threshold on normalized parameters (dimensionless, related to parameters scales)
        
        Also see:
            setConvergenceChecker,
            EvaluationRmsChecker
        
        
        """
        ...

class BatchLSObserver:
    """
    Observer for BatchLSEstimator iterations.
    
    This interface is intended to be implemented by users to monitor the progress of the estimator during estimation.
    
    Since:
        8.0
    """
    def evaluationPerformed(self, iterationsCount: int, evaluationsCount: int, orbits: typing.Union[typing.List[org.orekit.orbits.Orbit], jpype.JArray], estimatedOrbitalParameters: org.orekit.utils.ParameterDriversList, estimatedPropagatorParameters: org.orekit.utils.ParameterDriversList, estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, evaluationsProvider: org.orekit.estimation.measurements.EstimationsProvider, lspEvaluation: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation) -> None:
        """
        Notification callback for the end of each evaluation.
        
        Parameters:
            iterationsCount (int): iterations count
            evaluationsCount (int): evaluations count
            orbits (Orbit[]): current estimated orbits
            estimatedOrbitalParameters (ParameterDriversList): estimated orbital parameters
            estimatedPropagatorParameters (ParameterDriversList): estimated propagator parameters
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            evaluationsProvider (EstimationsProvider): provider for measurements evaluations resulting from the current estimated orbit (this is an unmodifiable view of the
                current evaluations, its content is changed at each iteration)
            lspEvaluation (Evaluation): current evaluation of the underlying
                LeastSquaresProblem
        
        
        """
        ...

class ModelObserver:
    """
    Observer for BatchLSModel calls.
    
    This interface is an internal one intended to pass the orbit back from BatchLSModel to BatchLSEstimator.
    
    Since:
        8.0
    """
    def modelCalled(self, orbits: typing.Union[typing.List[org.orekit.orbits.Orbit], jpype.JArray], estimations: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]], typing.Mapping[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]]) -> None:
        """
        Notification callback for orbit changes.
        
        Parameters:
            orbits (Orbit[]): current estimated orbits
            estimations (Map<ObservedMeasurement<?>, EstimatedMeasurement<?>>): map of measurements estimations resulting from the current estimated orbit (this is an unmodifiable view of the current
                estimations, its content is changed at each iteration)
        
        
        """
        ...

class BatchLSModel(AbstractBatchLSModel):
    """
    Bridge between ObservedMeasurement and LeastSquaresProblem.
    
    Since:
        8.0
    """
    def __init__(self, propagatorBuilders: typing.Union[typing.List[org.orekit.propagation.conversion.PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[ModelObserver, typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            propagatorBuilders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        
        """
        ...

class DSSTBatchLSModel(AbstractBatchLSModel):
    """
    Bridge between ObservedMeasurement and LeastSquaresProblem.
    
    This class is an adaption of the BatchLSModel class for the DSSTPropagator.
    
    Since:
        10.0
    """
    def __init__(self, propagatorBuilders: typing.Union[typing.List[org.orekit.propagation.conversion.PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[ModelObserver, typing.Callable], propagationType: org.orekit.propagation.PropagationType):
        """
        Simple constructor.
        
        Parameters:
            propagatorBuilders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
            propagationType (PropagationType): type of the orbit used for the propagation (mean or osculating)
        
        
        """
        ...

class PythonAbstractBatchLSModel(AbstractBatchLSModel):
    def __init__(self, propagatorBuilderArray: typing.Union[typing.List[org.orekit.propagation.conversion.PropagatorBuilder], jpype.JArray], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: typing.Union[ModelObserver, typing.Callable]): ...
    def configureHarvester(self, propagator: org.orekit.propagation.Propagator) -> org.orekit.propagation.MatricesHarvester:
        """
        Configure the propagator to compute derivatives.
        
        Specified by: configureHarvester in class AbstractBatchLSModel
        
        Parameters:
            propagator (Propagator): Propagator to configure
        
        Returns:
            harvester harvester to retrive the State Transition Matrix and Jacobian Matrix
        
        
        """
        ...
    def configureOrbits(self, harvester: org.orekit.propagation.MatricesHarvester, propagator: org.orekit.propagation.Propagator) -> org.orekit.orbits.Orbit:
        """
        Configure the current estimated orbits.
        
        For DSST orbit determination, short period derivatives are also calculated.
        
        Specified by: configureOrbits in class AbstractBatchLSModel
        
        Parameters:
            harvester (MatricesHarvester): harvester for matrices
            propagator (Propagator): the orbit propagator
        
        Returns:
            the current estimated orbits
        
        
        """
        ...
    def createPropagators(self, point: org.hipparchus.linear.RealVector) -> typing.MutableSequence[org.orekit.propagation.integration.AbstractIntegratedPropagator]:
        """
        Create the propagators and parameters corresponding to an evaluation point.
        
        Overrides: createPropagators in class AbstractBatchLSModel
        
        Parameters:
            point (RealVector): evaluation point
        
        Returns:
            an array of new propagators
        
        
        """
        ...
    def fetchEvaluatedMeasurement(self, index: int, evaluation: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> None:
        """
        Fetch a measurement that was evaluated during propagation.
        
        Overrides: fetchEvaluatedMeasurement in class AbstractBatchLSModel
        
        Parameters:
            index (int): index of the measurement first component
            evaluation (EstimatedMeasurement<?> evaluation): measurement evaluation
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEvaluationsCount(self) -> int:
        """
        Get the evaluations count.
        
        Overrides: getEvaluationsCount in class AbstractBatchLSModel
        
        Returns:
            evaluations count
        
        
        """
        ...
    def getIterationsCount(self) -> int:
        """
        Get the iterations count.
        
        Overrides: getIterationsCount in class AbstractBatchLSModel
        
        Returns:
            iterations count
        
        
        """
        ...
    def getSelectedPropagationDriversForBuilder(self, iBuilder: int) -> org.orekit.utils.ParameterDriversList:
        """
        Get the selected propagation drivers for a propagatorBuilder.
        
        Overrides: getSelectedPropagationDriversForBuilder in class AbstractBatchLSModel
        
        Parameters:
            iBuilder (int): index of the builder in the builders' array
        
        Returns:
            the list of selected propagation drivers for propagatorBuilder of index iBuilder
        
        
        """
        ...
    def isForwardPropagation(self) -> bool:
        """
        Return the forward propagation flag.
        
        Overrides: isForwardPropagation in class AbstractBatchLSModel
        
        Returns:
            the forward propagation flag
        
        
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
    def setEvaluationsCounter(self, evaluationsCounter: org.hipparchus.util.Incrementor) -> None:
        """
        Set the counter for evaluations.
        
        Overrides: setEvaluationsCounter in class AbstractBatchLSModel
        
        Parameters:
            evaluationsCounter (Incrementor): counter for evaluations
        
        
        """
        ...
    def setIterationsCounter(self, iterationsCounter: org.hipparchus.util.Incrementor) -> None:
        """
        Set the counter for iterations.
        
        Overrides: setIterationsCounter in class AbstractBatchLSModel
        
        Parameters:
            iterationsCounter (Incrementor): counter for iterations
        
        
        """
        ...
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]:
        """
        Specified by: meth:`~org.orekit.estimation.leastsquares.https:.www.hipparchus.org.apidocs.org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction.html?is` in interface MultivariateJacobianFunction
        
        Overrides: value in class AbstractBatchLSModel
        
        
        """
        ...

class PythonBatchLSObserver(BatchLSObserver):
    def __init__(self): ...
    def evaluationPerformed(self, iterationsCount: int, evaluationsCount: int, orbits: typing.Union[typing.List[org.orekit.orbits.Orbit], jpype.JArray], estimatedOrbitalParameters: org.orekit.utils.ParameterDriversList, estimatedPropagatorParameters: org.orekit.utils.ParameterDriversList, estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, evaluationsProvider: org.orekit.estimation.measurements.EstimationsProvider, lspEvaluation: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation) -> None:
        """
        Notification callback for the end of each evaluation. Extension point for Python.
        
        Specified by: evaluationPerformed in interface BatchLSObserver
        
        Parameters:
            iterationsCount (int): iterations count
            evaluationsCount (int): evaluations count
            orbits (Orbit[]): current estimated orbits
            estimatedOrbitalParameters (ParameterDriversList): estimated orbital parameters
            estimatedPropagatorParameters (ParameterDriversList): estimated propagator parameters
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            evaluationsProvider (EstimationsProvider): provider for measurements evaluations resulting from the current estimated orbit (this is an unmodifiable view of the
                current evaluations, its content is changed at each iteration)
            lspEvaluation (Evaluation): current evaluation of the underlying
                LeastSquaresProblem
        
        
        """
        ...
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

class PythonModelObserver(ModelObserver):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def modelCalled(self, orbits: typing.Union[typing.List[org.orekit.orbits.Orbit], jpype.JArray], estimations: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]], typing.Mapping[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]]) -> None:
        """
        Notification callback for orbit changes.
        
        Specified by: modelCalled in interface ModelObserver
        
        Parameters:
            orbits (Orbit[]): current estimated orbits
            estimations (Map<ObservedMeasurement<?>, EstimatedMeasurement<?>>): map of measurements estimations resulting from the current estimated orbit (this is an unmodifiable view of the
        
        
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

class SequentialBatchLSEstimator(BatchLSEstimator):
    """
    Sequential least squares estimator for orbit determination.
    
    When an orbit has already been estimated and new measurements are given, it is not efficient to re-optimize the whole problem. Only considering the new measures while optimizing will neither give good results as the old measurements will not be taken into account. Thus, a sequential estimator is used to estimate the orbit, which uses the old results of the estimation and the new measurements.
    
    In order to perform a sequential optimization, the user must configure a SequentialGaussNewtonOptimizer. Depending if its input data are an empty Evaluation, a complete Evaluation or an a priori state and covariance, different configuration are possible.
    
    1. No input data from a previous estimation
    
    Then, the SequentialBatchLSEstimator can be used like a BatchLSEstimator to perform the estimation. The user can initialize the SequentialGaussNewtonOptimizer using the default constructor.
    
    final SequentialGaussNewtonOptimizer optimizer = new SequentialGaussNewtonOptimizer();
    
    By default, a QRDecomposer is used as decomposition algorithm. In addition, normal equations are not form. It is possible to update these two default configurations by using:
    
      - 
        meth:`~org.orekit.estimation.leastsquares.https:.www.hipparchus.org.apidocs.org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.html?is`
        method: withDecomposer(newDecomposer);
      - 
        meth:`~org.orekit.estimation.leastsquares.https:.www.hipparchus.org.apidocs.org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.html?is`
        method: withFormNormalEquations(newFormNormalEquations);
    
    2. Initialization using a previous Evalutation
    
    In this situation, it is recommended to use the second constructor of the optimizer class.
    
    final SequentialGaussNewtonOptimizer optimizer = new SequentialGaussNewtonOptimizer(decomposer,
    formNormalEquations, evaluation);
    
    Using this constructor, the user can directly configure the MatrixDecomposer and set the flag for normal equations without calling the two previous presented methods.
    
    Note: This constructor can also be used to perform the initialization of 1. In this case, the Evaluation evaluation is null.
    
    3. Initialization using an a priori estimated state and covariance
    
    These situation is a classical satellite operation need. Indeed, a classical action is to use the results of a previous orbit determination (estimated state and covariance) performed a day before, to improve the initialization and the results of an orbit determination performed the current day. In this situation, the user can initialize the SequentialGaussNewtonOptimizer using the default constructor.
    
    final SequentialGaussNewtonOptimizer optimizer = new SequentialGaussNewtonOptimizer();
    
    The MatrixDecomposer and the flag about normal equations can again be updated using the two previous presented methods. The a priori state and covariance matrix can be set using:
    
      - 
        meth:`~org.orekit.estimation.leastsquares.https:.www.hipparchus.org.apidocs.org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer.html?is`
        method: withAPrioriData(aPrioriState, aPrioriCovariance);
    
    
    Since:
        11.0
    """
    def __init__(self, sequentialOptimizer: org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer, *propagatorBuilder: org.orekit.propagation.conversion.PropagatorBuilder):
        """
        Simple constructor.
        
        If multiple PropagatorBuilder are set up, the orbits of several spacecrafts will be used simultaneously. This is useful if the propagators share some model or measurements parameters (typically pole motion, prime meridian correction or ground stations positions).
        
        Setting up multiple PropagatorBuilder is also useful when inter-satellite measurements are used, even if only one of the orbit is estimated and the other ones are fixed. This is typically used when very high accuracy GNSS measurements are needed and the navigation bulletins are not considered accurate enough and the navigation constellation must be propagated numerically.
        
        The solver used for sequential least squares problem is a SequentialGaussNewtonOptimizer. Details about how initialize it are given in the class JavaDoc.
        
        Parameters:
            sequentialOptimizer (SequentialGaussNewtonOptimizer): solver for sequential least squares problem
            propagatorBuilder (PropagatorBuilder...): builders to use for propagation.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.leastsquares")``.

    AbstractBatchLSModel: typing.Type[AbstractBatchLSModel]
    BatchLSEstimator: typing.Type[BatchLSEstimator]
    BatchLSModel: typing.Type[BatchLSModel]
    BatchLSObserver: typing.Type[BatchLSObserver]
    DSSTBatchLSModel: typing.Type[DSSTBatchLSModel]
    ModelObserver: typing.Type[ModelObserver]
    PythonAbstractBatchLSModel: typing.Type[PythonAbstractBatchLSModel]
    PythonBatchLSObserver: typing.Type[PythonBatchLSObserver]
    PythonModelObserver: typing.Type[PythonModelObserver]
    SequentialBatchLSEstimator: typing.Type[SequentialBatchLSEstimator]
