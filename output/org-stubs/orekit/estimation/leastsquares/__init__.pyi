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
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, abstractJacobiansMapperArray: typing.List[org.orekit.propagation.integration.AbstractJacobiansMapper], modelObserver: 'ModelObserver'): ...
    def createPropagators(self, realVector: org.hipparchus.linear.RealVector) -> typing.List[org.orekit.propagation.Propagator]: ...
    def fetchEvaluatedMeasurement(self, int: int, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> None: ...
    def getEvaluationsCount(self) -> int: ...
    def getIterationsCount(self) -> int: ...
    def getSelectedPropagationDriversForBuilder(self, int: int) -> org.orekit.utils.ParameterDriversList: ...
    def isForwardPropagation(self) -> bool: ...
    def setEvaluationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None: ...
    def setIterationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None: ...
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]: ...

class BatchLSEstimator:
    def __init__(self, leastSquaresOptimizer: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder]): ...
    def addMeasurement(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> None: ...
    def estimate(self) -> typing.List[org.orekit.propagation.Propagator]: ...
    def getEvaluationsCount(self) -> int: ...
    def getIterationsCount(self) -> int: ...
    def getLastEstimations(self) -> java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]: ...
    def getMeasurementsParametersDrivers(self, boolean: bool) -> org.orekit.utils.ParameterDriversList: ...
    def getOptimum(self) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.Optimum: ...
    def getOrbitalParametersDrivers(self, boolean: bool) -> org.orekit.utils.ParameterDriversList: ...
    def getPhysicalCovariances(self, double: float) -> org.hipparchus.linear.RealMatrix: ...
    def getPropagatorParametersDrivers(self, boolean: bool) -> org.orekit.utils.ParameterDriversList: ...
    def setConvergenceChecker(self, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation]) -> None: ...
    def setMaxEvaluations(self, int: int) -> None: ...
    def setMaxIterations(self, int: int) -> None: ...
    def setObserver(self, batchLSObserver: 'BatchLSObserver') -> None: ...
    def setParametersConvergenceThreshold(self, double: float) -> None: ...

class BatchLSObserver:
    def evaluationPerformed(self, int: int, int2: int, orbitArray: typing.List[org.orekit.orbits.Orbit], parameterDriversList: org.orekit.utils.ParameterDriversList, parameterDriversList2: org.orekit.utils.ParameterDriversList, parameterDriversList3: org.orekit.utils.ParameterDriversList, estimationsProvider: org.orekit.estimation.measurements.EstimationsProvider, evaluation: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation) -> None: ...

class ModelObserver:
    def modelCalled(self, orbitArray: typing.List[org.orekit.orbits.Orbit], map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]], typing.Mapping[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]]) -> None: ...

class BatchLSModel(AbstractBatchLSModel):
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: ModelObserver): ...

class DSSTBatchLSModel(AbstractBatchLSModel):
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: ModelObserver, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType): ...

class PythonAbstractBatchLSModel(AbstractBatchLSModel):
    def __init__(self, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, abstractJacobiansMapperArray: typing.List[org.orekit.propagation.integration.AbstractJacobiansMapper], modelObserver: ModelObserver): ...
    def configureDerivatives(self, propagator: org.orekit.propagation.Propagator) -> org.orekit.propagation.integration.AbstractJacobiansMapper: ...
    def configureOrbits(self, abstractJacobiansMapper: org.orekit.propagation.integration.AbstractJacobiansMapper, propagator: org.orekit.propagation.Propagator) -> org.orekit.orbits.Orbit: ...
    def createPropagators(self, realVector: org.hipparchus.linear.RealVector) -> typing.List[org.orekit.propagation.integration.AbstractIntegratedPropagator]: ...
    def fetchEvaluatedMeasurement(self, int: int, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> None: ...
    def finalize(self) -> None: ...
    def getEvaluationsCount(self) -> int: ...
    def getIterationsCount(self) -> int: ...
    def getSelectedPropagationDriversForBuilder(self, int: int) -> org.orekit.utils.ParameterDriversList: ...
    def isForwardPropagation(self) -> bool: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def setEvaluationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None: ...
    def setIterationsCounter(self, incrementor: org.hipparchus.util.Incrementor) -> None: ...
    def value(self, realVector: org.hipparchus.linear.RealVector) -> org.hipparchus.util.Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]: ...

class PythonBatchLSObserver(BatchLSObserver):
    def __init__(self): ...
    def evaluationPerformed(self, int: int, int2: int, orbitArray: typing.List[org.orekit.orbits.Orbit], parameterDriversList: org.orekit.utils.ParameterDriversList, parameterDriversList2: org.orekit.utils.ParameterDriversList, parameterDriversList3: org.orekit.utils.ParameterDriversList, estimationsProvider: org.orekit.estimation.measurements.EstimationsProvider, evaluation: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem.Evaluation) -> None: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonModelObserver(ModelObserver):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def modelCalled(self, orbitArray: typing.List[org.orekit.orbits.Orbit], map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]], typing.Mapping[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]]]) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class SequentialBatchLSEstimator(BatchLSEstimator):
    def __init__(self, sequentialGaussNewtonOptimizer: org.hipparchus.optim.nonlinear.vector.leastsquares.SequentialGaussNewtonOptimizer, orbitDeterminationPropagatorBuilderArray: typing.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder]): ...

class TLEBatchLSModel(AbstractBatchLSModel):
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
