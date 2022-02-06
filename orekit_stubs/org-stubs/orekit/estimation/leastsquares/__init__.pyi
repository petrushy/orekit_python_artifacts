import java.util
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
    public abstract class AbstractBatchLSModel extends Object implements MultivariateJacobianFunction
    
        Bridge between :class:`~org.orekit.estimation.measurements.ObservedMeasurement` and null.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: 'ModelObserver'): ...
    @typing.overload
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, matricesHarvesterArray: typing.List[org.orekit.propagation.MatricesHarvester], modelObserver: 'ModelObserver'): ...
    def createPropagators(self, realVector: org.hipparchus.linear.RealVector) -> typing.List[org.orekit.propagation.Propagator]:
        """
            Create the propagators and parameters corresponding to an evaluation point.
        
            Parameters:
                point (RealVector): evaluation point
        
            Returns:
                an array of new propagators
        
        
        """
        ...
    def fetchEvaluatedMeasurement(self, int: int, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> None:
        """
            Fetch a measurement that was evaluated during propagation.
        
            Parameters:
                index (int): index of the measurement first component
                evaluation (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement`<?> evaluation): measurement evaluation
        
        
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
    def getSelectedOrbitalParametersDriversForBuilder(self, int: int) -> org.orekit.utils.ParameterDriversList:
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
    def getSelectedPropagationDriversForBuilder(self, int: int) -> org.orekit.utils.ParameterDriversList:
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
    def setEvaluationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None:
        """
            Set the counter for evaluations.
        
            Parameters:
                evaluationsCounter (Incrementor): counter for evaluations
        
        
        """
        ...
    def setIterationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None:
        """
            Set the counter for iterations.
        
            Parameters:
                iterationsCounter (Incrementor): counter for iterations
        
        
        """
        ...
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...

class BatchLSEstimator:
    """
    public class BatchLSEstimator extends Object
    
        Least squares estimator for orbit determination.
    
        Since 10.0, the least squares estimator can be used with both
        :class:`~org.orekit.propagation.numerical.NumericalPropagator` and
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator` orbit propagators.
    
        Since:
            8.0
    """
    def __init__(self, leastSquaresOptimizer: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder]): ...
    def addMeasurement(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> None:
        """
            Add a measurement.
        
            Parameters:
                measurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> measurement): measurement to add
        
        
        """
        ...
    def estimate(self) -> typing.List[org.orekit.propagation.Propagator]:
        """
            Estimate the orbital, propagation and measurements parameters.
        
            The initial guess for all parameters must have been set before calling this method using
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getOrbitalParametersDrivers`,
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getPropagatorParametersDrivers`, and
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getMeasurementsParametersDrivers` and then
            :meth:`~org.orekit.utils.ParameterDriver.setValue` of the parameters.
        
            For parameters whose reference date has not been set to a non-null date beforehand (i.e. the parameters for which
            :meth:`~org.orekit.utils.ParameterDriver.getReferenceDate` returns :code:`null`, a default reference date will be set
            automatically at the start of the estimation to the
            :meth:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder.getInitialOrbitDate` of the first propagator
            builder. For parameters whose reference date has been set to a non-null date, this reference date is untouched.
        
            After this method returns, the estimated parameters can be retrieved using
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getOrbitalParametersDrivers`,
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getPropagatorParametersDrivers`, and
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getMeasurementsParametersDrivers` and then
            :meth:`~org.orekit.utils.ParameterDriver.getValue` of the parameters.
        
            As a convenience, the method also returns a fully configured and ready to use propagator set up with all the estimated
            values.
        
            For even more in-depth information, the :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getOptimum` method
            provides detailed elements (covariance matrix, estimated parameters standard deviation, weighted Jacobian, RMS,
            Ã�â€¡Ã‚Â², residuals and more).
        
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
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setMaxEvaluations`
        
        
        """
        ...
    def getIterationsCount(self) -> int:
        """
            Get the number of iterations used for last estimation.
        
            Returns:
                number of iterations used for last estimation
        
            Also see:
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setMaxIterations`
        
        
        """
        ...
    def getLastEstimations(self) -> java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]: ...
    def getMeasurementsParametersDrivers(self, boolean: bool) -> org.orekit.utils.ParameterDriversList:
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
        
            The null object contains detailed elements (covariance matrix, estimated parameters standard deviation, weighted
            Jacobian, RMS, Ã�â€¡Ã‚Â², residuals and more).
        
            Beware that the returned object is the raw view from the underlying mathematical library. At this raw level, parameters
            have :meth:`~org.orekit.utils.ParameterDriver.getNormalizedValue` whereas the space flight parameters have
            :meth:`~org.orekit.utils.ParameterDriver.getValue` with their units. So there are
            :meth:`~org.orekit.utils.ParameterDriver.getScale` to apply when using these elements.
        
            Returns:
                optimum found after last call to :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.estimate`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self, boolean: bool) -> org.orekit.utils.ParameterDriversList:
        """
            Get the orbital parameters supported by this estimator.
        
            If there are more than one propagator builder, then the names of the drivers have an index marker in square brackets
            appended to them in order to distinguish the various orbits. So for example with one builder generating Keplerian orbits
            the names would be simply "a", "e", "i"... but if there are several builders the names would be "a[0]", "e[0]",
            "i[0]"..."a[1]", "e[1]", "i[1]"...
        
            Parameters:
                estimatedOnly (boolean): if true, only estimated parameters are returned
        
            Returns:
                orbital parameters supported by this estimator
        
        
        """
        ...
    def getPhysicalCovariances(self, double: float) -> org.hipparchus.linear.RealMatrix:
        """
            Get the covariances matrix in space flight dynamics physical units.
        
            This method retrieve the null from the [@link :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getOptimum`
            and applies the scaling factors to it in order to convert it from raw normalized values back to physical values.
        
            Parameters:
                threshold (double): threshold to identify matrix singularity
        
            Returns:
                covariances matrix in space flight dynamics physical units
        
            Since:
                9.1
        
        
        """
        ...
    def getPropagatorParametersDrivers(self, boolean: bool) -> org.orekit.utils.ParameterDriversList:
        """
            Get the propagator parameters supported by this estimator.
        
            Parameters:
                estimatedOnly (boolean): if true, only estimated parameters are returned
        
            Returns:
                propagator parameters supported by this estimator
        
        
        """
        ...
    def setConvergenceChecker(self, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation]) -> None:
        """
            Set a custom convergence checker.
        
            Calling this method overrides any checker that could have been set beforehand by calling
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setParametersConvergenceThreshold`. Both methods are
            mutually exclusive.
        
            Parameters:
                convergenceChecker (ConvergenceChecker<LeastSquaresProblem.Evaluation> convergenceChecker): convergence checker to set
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setParametersConvergenceThreshold`
        
        
        """
        ...
    def setMaxEvaluations(self, int: int) -> None:
        """
            Set the maximum number of model evaluations.
        
            The evaluations correspond to the orbit propagations and measurements estimations performed with a set of estimated
            parameters.
        
            For null there is one evaluation at each iteration, so the maximum numbers may be set to the same value. For null, there
            can be several evaluations at some iterations (typically for the first couple of iterations), so the maximum number of
            evaluations may be set to a higher value than the maximum number of iterations.
        
            Parameters:
                maxEvaluations (int): maximum number of model evaluations
        
            Also see:
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setMaxIterations`,
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getEvaluationsCount`
        
        
        """
        ...
    def setMaxIterations(self, int: int) -> None:
        """
            Set the maximum number of iterations.
        
            The iterations correspond to the top level iterations of the null.
        
            Parameters:
                maxIterations (int): maxIterations maximum number of iterations
        
            Also see:
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setMaxEvaluations`,
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.getIterationsCount`
        
        
        """
        ...
    def setObserver(self, batchLSObserver: 'BatchLSObserver') -> None:
        """
            Set an observer for iterations.
        
            Parameters:
                observer (:class:`~org.orekit.estimation.leastsquares.BatchLSObserver`): observer to be notified at the end of each iteration
        
        
        """
        ...
    def setParametersConvergenceThreshold(self, double: float) -> None:
        """
            Set convergence threshold.
        
            The convergence used for estimation is based on the estimated parameters
            :meth:`~org.orekit.utils.ParameterDriver.getNormalizedValue`. Convergence is considered to have been reached when the
            difference between previous and current normalized value is less than the convergence threshold for all parameters. The
            same value is used for all parameters since they are normalized and hence dimensionless.
        
            Normalized values are computed as :code:`(current - reference)/scale`, so convergence is reached when the following
            condition holds for all estimated parameters: :code:`|current[i] - previous[i]| <= threshold * scale[i]`
        
            So the convergence threshold specified here can be considered as a multiplication factor applied to scale. Since for all
            parameters the scale is often small (typically about 1 m for orbital positions for example), then the threshold should
            not be too small. A value of 10Ã¢ï¿½Â»Ã‚Â³ is often quite accurate.
        
            Calling this method overrides any checker that could have been set beforehand by calling
            :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setConvergenceChecker`. Both methods are mutually exclusive.
        
            Parameters:
                parametersConvergenceThreshold (double): convergence threshold on normalized parameters (dimensionless, related to parameters scales)
        
            Also see:
                :meth:`~org.orekit.estimation.leastsquares.BatchLSEstimator.setConvergenceChecker`, null
        
        
        """
        ...

class BatchLSObserver:
    """
    public interface BatchLSObserver
    
        Observer for :class:`~org.orekit.estimation.leastsquares.BatchLSEstimator` iterations.
    
        This interface is intended to be implemented by users to monitor the progress of the estimator during estimation.
    
        Since:
            8.0
    """
    def evaluationPerformed(self, int: int, int2: int, orbitArray: typing.List[org.orekit.orbits.Orbit], parameterDriversList: org.orekit.utils.ParameterDriversList, parameterDriversList2: org.orekit.utils.ParameterDriversList, parameterDriversList3: org.orekit.utils.ParameterDriversList, estimationsProvider: org.orekit.estimation.measurements.EstimationsProvider, evaluation: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation) -> None:
        """
            Notification callback for the end of each evaluation.
        
            Parameters:
                iterationsCount (int): iterations count
                evaluationsCount (int): evaluations count
                orbits (:class:`~org.orekit.orbits.Orbit`[]): current estimated orbits
                estimatedOrbitalParameters (:class:`~org.orekit.utils.ParameterDriversList`): estimated orbital parameters
                estimatedPropagatorParameters (:class:`~org.orekit.utils.ParameterDriversList`): estimated propagator parameters
                estimatedMeasurementsParameters (:class:`~org.orekit.utils.ParameterDriversList`): estimated measurements parameters
                evaluationsProvider (:class:`~org.orekit.estimation.measurements.EstimationsProvider`): provider for measurements evaluations resulting from the current estimated orbit (this is an unmodifiable view of the
                    current evaluations, its content is changed at each iteration)
                lspEvaluation (LeastSquaresProblem.Evaluation): current evaluation of the underlying null
        
        
        """
        ...

class ModelObserver:
    """
    public interface ModelObserver
    
        Observer for :class:`~org.orekit.estimation.leastsquares.BatchLSModel` calls.
    
        This interface is an internal one intended to pass the orbit back from
        :class:`~org.orekit.estimation.leastsquares.BatchLSModel` to
        :class:`~org.orekit.estimation.leastsquares.BatchLSEstimator`.
    
        Since:
            8.0
    """
    def modelCalled(self, orbitArray: typing.List[org.orekit.orbits.Orbit], map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]], typing.Mapping[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]]) -> None: ...

class BatchLSModel(AbstractBatchLSModel):
    """
    public class BatchLSModel extends :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
    
        Bridge between :class:`~org.orekit.estimation.measurements.ObservedMeasurement` and null.
    
        Since:
            8.0
    """
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: ModelObserver): ...

class DSSTBatchLSModel(AbstractBatchLSModel):
    """
    public class DSSTBatchLSModel extends :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
    
        Bridge between :class:`~org.orekit.estimation.measurements.ObservedMeasurement` and null.
    
        This class is an adaption of the :class:`~org.orekit.estimation.leastsquares.BatchLSModel` class but for the
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        Since:
            10.0
    """
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: ModelObserver, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType): ...

class PythonAbstractBatchLSModel(AbstractBatchLSModel):
    """
    public class PythonAbstractBatchLSModel extends :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
    """
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, abstractJacobiansMapperArray: typing.List[org.orekit.propagation.integration.AbstractJacobiansMapper], modelObserver: ModelObserver): ...
    def configureDerivatives(self, propagator: org.orekit.propagation.Propagator) -> org.orekit.propagation.integration.AbstractJacobiansMapper:
        """
            Configure the propagator to compute derivatives.
        
            Specified by:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.configureDerivatives`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Parameters:
                propagators (:class:`~org.orekit.propagation.Propagator`): :class:`~org.orekit.propagation.Propagator` to configure
        
            Returns:
                mapper for this propagator
        
        
        """
        ...
    def configureOrbits(self, matricesHarvester: org.orekit.propagation.MatricesHarvester, propagator: org.orekit.propagation.Propagator) -> org.orekit.orbits.Orbit:
        """
            Description copied from class: :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.configureOrbits`
            Configure the current estimated orbits.
        
            For DSST orbit determination, short period derivatives are also calculated.
        
            Specified by:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.configureOrbits`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Parameters:
                harvester (:class:`~org.orekit.propagation.MatricesHarvester`): harvester for matrices
                propagator (:class:`~org.orekit.propagation.Propagator`): the orbit propagator
        
            Returns:
                the current estimated orbits
        
        
        """
        ...
    def createPropagators(self, realVector: org.hipparchus.linear.RealVector) -> typing.List[org.orekit.propagation.integration.AbstractIntegratedPropagator]:
        """
            Create the propagators and parameters corresponding to an evaluation point.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.createPropagators`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Parameters:
                point (RealVector): evaluation point
        
            Returns:
                an array of new propagators
        
        
        """
        ...
    def fetchEvaluatedMeasurement(self, int: int, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> None:
        """
            Fetch a measurement that was evaluated during propagation.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.fetchEvaluatedMeasurement`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Parameters:
                index (int): index of the measurement first component
                evaluation (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement`<?> evaluation): measurement evaluation
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getEvaluationsCount(self) -> int:
        """
            Get the evaluations count.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.getEvaluationsCount`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Returns:
                evaluations count
        
        
        """
        ...
    def getIterationsCount(self) -> int:
        """
            Get the iterations count.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.getIterationsCount`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Returns:
                iterations count
        
        
        """
        ...
    def getSelectedPropagationDriversForBuilder(self, int: int) -> org.orekit.utils.ParameterDriversList:
        """
            Get the selected propagation drivers for a propagatorBuilder.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.getSelectedPropagationDriversForBuilder`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Parameters:
                iBuilder (int): index of the builder in the builders' array
        
            Returns:
                the list of selected propagation drivers for propagatorBuilder of index iBuilder
        
        
        """
        ...
    def isForwardPropagation(self) -> bool:
        """
            Return the forward propagation flag.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.isForwardPropagation`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
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
    def setEvaluationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None:
        """
            Set the counter for evaluations.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.setEvaluationsCounter`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Parameters:
                evaluationsCounter (Incrementor): counter for evaluations
        
        
        """
        ...
    def setIterationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None:
        """
            Set the counter for iterations.
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.setIterationsCounter`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
            Parameters:
                iterationsCounter (Incrementor): counter for iterations
        
        
        """
        ...
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]:
        """
            Description copied from class: :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.value`
        
            Specified by:
                 in interface 
        
            Overrides:
                :meth:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel.value`Â in
                classÂ :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
        
        
        """
        ...

class PythonBatchLSObserver(BatchLSObserver):
    """
    public class PythonBatchLSObserver extends Object implements :class:`~org.orekit.estimation.leastsquares.BatchLSObserver`
    """
    def __init__(self): ...
    def evaluationPerformed(self, int: int, int2: int, orbitArray: typing.List[org.orekit.orbits.Orbit], parameterDriversList: org.orekit.utils.ParameterDriversList, parameterDriversList2: org.orekit.utils.ParameterDriversList, parameterDriversList3: org.orekit.utils.ParameterDriversList, estimationsProvider: org.orekit.estimation.measurements.EstimationsProvider, evaluation: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation) -> None:
        """
            Notification callback for the end of each evaluation. Extension point for Python.
        
            Specified by:
                 in interface :class:`~org.orekit.estimation.leastsquares.BatchLSObserver`
        
            Parameters:
                iterationsCount (int): iterations count
                evaluationsCount (int): evaluations count
                orbits (:class:`~org.orekit.orbits.Orbit`[]): current estimated orbits
                estimatedOrbitalParameters (:class:`~org.orekit.utils.ParameterDriversList`): estimated orbital parameters
                estimatedPropagatorParameters (:class:`~org.orekit.utils.ParameterDriversList`): estimated propagator parameters
                estimatedMeasurementsParameters (:class:`~org.orekit.utils.ParameterDriversList`): estimated measurements parameters
                evaluationsProvider (:class:`~org.orekit.estimation.measurements.EstimationsProvider`): provider for measurements evaluations resulting from the current estimated orbit (this is an unmodifiable view of the
                    current evaluations, its content is changed at each iteration)
                lspEvaluation (LeastSquaresProblem.Evaluation): current evaluation of the underlying null
        
        
        """
        ...
    def finalize(self) -> None: ...
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
    """
    public class PythonModelObserver extends Object implements :class:`~org.orekit.estimation.leastsquares.ModelObserver`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def modelCalled(self, orbitArray: typing.List[org.orekit.orbits.Orbit], map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]], typing.Mapping[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]]) -> None: ...
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
    public class SequentialBatchLSEstimator extends :class:`~org.orekit.estimation.leastsquares.BatchLSEstimator`
    
        Sequential least squares estimator for orbit determination.
    
        When an orbit has already been estimated and new measurements are given, it is not efficient to re-optimize the whole
        problem. Only considering the new measures while optimizing will neither give good results as the old measurements will
        not be taken into account. Thus, a sequential estimator is used to estimate the orbit, which uses the old results of the
        estimation and the new measurements.
    
        In order to perform a sequential optimization, the user must configure a null. Depending if its input data are an empty
        null, a complete :code:`Evaluation` or an a priori state and covariance, different configuration are possible.
    
        **1. No input data from a previous estimation**
    
        Then, the :class:`~org.orekit.estimation.leastsquares.SequentialBatchLSEstimator` can be used like a
        :class:`~org.orekit.estimation.leastsquares.BatchLSEstimator` to perform the estimation. The user can initialize the
        :code:`SequentialGaussNewtonOptimizer` using the default constructor.
    
        :code:`final SequentialGaussNewtonOptimizer optimizer = new SequentialGaussNewtonOptimizer();`
    
        By default, a null is used as decomposition algorithm. In addition, normal equations are not form. It is possible to
        update these two default configurations by using:
    
          - null method: :code:`optimizer.withDecomposer(newDecomposer);`
          - null method: :code:`optimizer.withFormNormalEquations(newFormNormalEquations);`
    
    
        **2. Initialization using a previous :code:`Evalutation`**
    
        In this situation, it is recommended to use the second constructor of the optimizer class.
    
        :code:`final SequentialGaussNewtonOptimizer optimizer = new SequentialGaussNewtonOptimizer(decomposer,
        formNormalEquations, evaluation);`
    
        Using this constructor, the user can directly configure the MatrixDecomposer and set the flag for normal equations
        without calling the two previous presented methods.
    
        *Note:* This constructor can also be used to perform the initialization of **1.** In this case, the :code:`Evaluation
        evaluation` is :code:`null`.
    
        **3. Initialization using an a priori estimated state and covariance**
    
        These situation is a classical satellite operation need. Indeed, a classical action is to use the results of a previous
        orbit determination (estimated state and covariance) performed a day before, to improve the initialization and the
        results of an orbit determination performed the current day. In this situation, the user can initialize the
        :code:`SequentialGaussNewtonOptimizer` using the default constructor.
    
        :code:`final SequentialGaussNewtonOptimizer optimizer = new SequentialGaussNewtonOptimizer();`
    
        The MatrixDecomposer and the flag about normal equations can again be updated using the two previous presented methods.
        The a priori state and covariance matrix can be set using:
    
          - null method: :code:`optimizer.withAPrioriData(aPrioriState, aPrioriCovariance);`
    
    
        Since:
            11.0
    """
    def __init__(self, sequentialGaussNewtonOptimizer: org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder]): ...

class TLEBatchLSModel(AbstractBatchLSModel):
    """
    Deprecated. 
    as of 11.1, replaced by :class:`~org.orekit.estimation.leastsquares.BatchLSModel`
    @Deprecated public class TLEBatchLSModel extends :class:`~org.orekit.estimation.leastsquares.AbstractBatchLSModel`
    
        Bridge between :class:`~org.orekit.estimation.measurements.ObservedMeasurement` and null.
    
        Since:
            11.0
    """
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: ModelObserver): ...


class __module_protocol__(typing.Protocol):
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
    TLEBatchLSModel: typing.Type[TLEBatchLSModel]
