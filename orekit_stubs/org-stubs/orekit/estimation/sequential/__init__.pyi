import java.lang
import java.util
import org.hipparchus.analysis
import org.hipparchus.filtering.kalman
import org.hipparchus.filtering.kalman.extended
import org.hipparchus.filtering.kalman.unscented
import org.hipparchus.linear
import org.hipparchus.util
import org.orekit.estimation.measurements
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.conversion
import org.orekit.propagation.integration
import org.orekit.propagation.sampling
import org.orekit.propagation.semianalytical.dsst
import org.orekit.time
import org.orekit.utils
import typing



class AbstractKalmanEstimator:
    """
    public abstract class AbstractKalmanEstimator extends Object
    
        Base class for Kalman estimators.
    
        Since:
            11.3
    """
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current date.
        
            Returns:
                current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
            Get the current measurement number.
        
            Returns:
                current measurement number
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated measurements parameters.
        
            Returns:
                the list of estimated measurements parameters
        
        
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
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the "physical" estimated covariance matrix (i.e. not normalized)
        
            Returns:
                the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the "physical" estimated state (i.e. not normalized)
        
            For the Semi-analytical Kalman Filters it corresponds to the corrected filter correction. In other words, it doesn't
            represent an orbital state.
        
            Returns:
                the "physical" estimated state
        
        
        """
        ...
    def getPropagationParametersDrivers(self, boolean: bool) -> org.orekit.utils.ParameterDriversList:
        """
            Get the propagator parameters supported by this estimator.
        
            Parameters:
                estimatedOnly (boolean): if true, only estimated parameters are returned
        
            Returns:
                propagator parameters supported by this estimator
        
        
        """
        ...

class CovarianceMatrixProvider:
    """
    public interface CovarianceMatrixProvider
    
        Provider for process noise matrices.
    
        Since:
            9.2
    """
    def getInitialCovarianceMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the initial covariance matrix.
        
            The initial covariance matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the initial covariance matrix will be the output matrix of a previous run of the Kalman filter.
        
            Parameters:
                initial (:class:`~org.orekit.propagation.SpacecraftState`): initial state state
        
            Returns:
                physical (i.e. non normalized) initial covariance matrix
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
        """
        ...
    def getProcessNoiseMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState, spacecraftState2: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the process noise matrix between previous and current states.
        
            The process noise matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to
            0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
            Parameters:
                previous (:class:`~org.orekit.propagation.SpacecraftState`): previous state
                current (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                physical (i.e. non normalized) process noise matrix between previous and current states
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
        """
        ...

class EskfMeasurementHandler(org.orekit.propagation.sampling.OrekitStepHandler):
    """
    @Deprecated public class EskfMeasurementHandler extends Object implements :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
    
        Deprecated.
        :class:`~org.orekit.propagation.sampling.OrekitStepHandler` picking up
        :class:`~org.orekit.estimation.measurements.ObservedMeasurement` for the
        :class:`~org.orekit.estimation.sequential.SemiAnalyticalKalmanEstimator`.
    
        Since:
            11.1
    """
    def __init__(self, semiAnalyticalKalmanModel: 'SemiAnalyticalKalmanModel', extendedKalmanFilter: org.hipparchus.filtering.kalman.extended.ExtendedKalmanFilter['MeasurementDecorator'], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], absoluteDate: org.orekit.time.AbsoluteDate): ...
    def handleStep(self, orekitStepInterpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> None:
        """
            Deprecated.
            Handle the current step.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.handleStep`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): interpolator set up for the current step
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Deprecated.
            Initialize step handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default method does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class KalmanEstimation:
    """
    public interface KalmanEstimation
    
        Interface for accessing :class:`~org.orekit.estimation.sequential.KalmanEstimator` estimations. The "physical" term used
        to characterize the states and matrices is used per opposition to the "normalized" states and matrices used to perform
        the computation.
    
        Since:
            9.2
    """
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the estimated measurement.
        
            This estimation has been evaluated on the last corrected orbits
        
            Returns:
                corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the corrected spacecraft states.
        
            Returns:
                corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current date.
        
            Returns:
                current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
            Get the current measurement number.
        
            Returns:
                current measurement number
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated measurements parameters.
        
            Returns:
                the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated orbital parameters.
        
            Returns:
                the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated propagation parameters.
        
            Returns:
                the list of estimated propagation parameters
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the "physical" estimated covariance matrix (i.e. not normalized)
        
            Returns:
                the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the "physical" estimated state (i.e. not normalized)
        
            Returns:
                the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical innovation covariance matrix.
        
            Returns:
                physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
            Since:
                9.3
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Kalman gain matrix.
        
            Returns:
                Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
            Since:
                9.3
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
            Returns:
                physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
                measurement has been ignored)
        
            Since:
                9.3
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
            Returns:
                state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
                process estimate)
        
            Since:
                9.3
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the predicted measurement.
        
            This estimation has been evaluated on the last predicted orbits
        
            Returns:
                predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the predicted spacecraft states.
        
            Returns:
                predicted spacecraft states
        
        
        """
        ...

class KalmanEstimatorBuilder:
    """
    public class KalmanEstimatorBuilder extends Object
    
        Builder for a Kalman filter estimator.
    
        Since:
            9.2
    """
    def __init__(self): ...
    def addPropagationConfiguration(self, orbitDeterminationPropagatorBuilder: org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'KalmanEstimatorBuilder':
        """
            Add a propagation configuration.
        
            This method must be called once for each propagator to managed with the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The propagators order in the Kalman filter will be the call
            order.
        
            The :code:`provider` should return a matrix with dimensions and ordering consistent with the :code:`builder`
            configuration. The first 6 rows/columns correspond to the 6 orbital parameters. The remaining elements correspond to the
            subset of propagation parameters that are estimated, in the same order as
            propagatorBuilder.:meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`.:meth:`~org.orekit.utils.ParameterDriversList.getDrivers`
            (but filtering out the non selected drivers).
        
            Parameters:
                builder (:class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`): The propagator builder to use in the Kalman filter.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): The process noise matrices provider to use, consistent with the builder. This parameter can be equal to :code:`null` if
                    the input builder is an :class:`~org.orekit.propagation.conversion.EphemerisPropagatorBuilder`. Indeed, for ephemeris
                    based estimation only measurement parameters are estimated. Therefore, the covariance related to dynamical parameters
                    can be null.
        
            Returns:
                this object.
        
            Also see:
                :meth:`~org.orekit.estimation.sequential.CovarianceMatrixProvider.getProcessNoiseMatrix`
        
        
        """
        ...
    def build(self) -> 'KalmanEstimator':
        """
            Construct a :class:`~org.orekit.estimation.sequential.KalmanEstimator` from the data in this builder.
        
            Before this method is called,
            :meth:`~org.orekit.estimation.sequential.KalmanEstimatorBuilder.addPropagationConfiguration` must have been called at
            least once, otherwise configuration is incomplete and an exception will be raised.
        
            Returns:
                a new :class:`~org.orekit.estimation.sequential.KalmanEstimator`.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer) -> 'KalmanEstimatorBuilder':
        """
            Configure the matrix decomposer.
        
            Parameters:
                matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
            Returns:
                this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'KalmanEstimatorBuilder':
        """
            Configure the estimated measurement parameters.
        
            If this method is not called, no measurement parameters will be estimated.
        
            Parameters:
                estimatedMeasurementsParams (:class:`~org.orekit.utils.ParameterDriversList`): The estimated measurements' parameters list.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): covariance matrix provider for the estimated measurement parameters
        
            Returns:
                this object.
        
            Since:
                10.3
        
        
        """
        ...

class KalmanEstimatorUtil:
    """
    public class KalmanEstimatorUtil extends Object
    
        Utility class for Kalman Filter.
    
        This class includes common methods used by the different Kalman models in Orekit (i.e., Extended, Unscented, and
        Semi-analytical)
    
        Since:
            11.3
    """
    _applyDynamicOutlierFilter__T = typing.TypeVar('_applyDynamicOutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def applyDynamicOutlierFilter(estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_applyDynamicOutlierFilter__T], realMatrix: org.hipparchus.linear.RealMatrix) -> None:
        """
            Set and apply a dynamic outlier filter on a measurement.
        
            Loop on the modifiers to see if a dynamic outlier filter needs to be applied.
        
            Compute the sigma array using the matrix in input and set the filter.
        
            Apply the filter by calling the modify method on the estimated measurement.
        
            Reset the filter.
        
            Parameters:
                measurement (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement`<T> measurement): measurement to filter
                innovationCovarianceMatrix (RealMatrix): So called innovation covariance matrix S, with:
        
                    S = H.Ppred.Ht + R
        
                    Where:
        
                    - H is the normalized measurement matrix (Ht its transpose)
        
                    - Ppred is the normalized predicted covariance matrix
        
                    - R is the normalized measurement noise matrix
        
        
        """
        ...
    @staticmethod
    def checkDimension(int: int, parameterDriversList: org.orekit.utils.ParameterDriversList, parameterDriversList2: org.orekit.utils.ParameterDriversList, parameterDriversList3: org.orekit.utils.ParameterDriversList) -> None:
        """
            Check dimension.
        
            Parameters:
                dimension (int): dimension to check
                orbitalParameters (:class:`~org.orekit.utils.ParameterDriversList`): orbital parameters
                propagationParameters (:class:`~org.orekit.utils.ParameterDriversList`): propagation parameters
                measurementParameters (:class:`~org.orekit.utils.ParameterDriversList`): measurements parameters
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeInnovationVector(estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> org.hipparchus.linear.RealVector:
        """
            Compute the unnormalized innovation vector from the given predicted measurement.
        
            Parameters:
                predicted (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement`<?> predicted): predicted measurement
        
            Returns:
                the innovation vector
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeInnovationVector(estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any], doubleArray: typing.List[float]) -> org.hipparchus.linear.RealVector:
        """
            Compute the normalized innovation vector from the given predicted measurement.
        
            Parameters:
                predicted (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement`<?> predicted): predicted measurement
                sigma (double[]): measurement standard deviation
        
            Returns:
                the innovation vector
        
        
        """
        ...
    @staticmethod
    def decorate(observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], absoluteDate: org.orekit.time.AbsoluteDate) -> 'MeasurementDecorator':
        """
            Decorate an observed measurement.
        
            The "physical" measurement noise matrix is the covariance matrix of the measurement. Normalizing it consists in applying
            the following equation: Rn[i,j] = R[i,j]/Ã�Æ’[i]/Ã�Æ’[j] Thus the normalized measurement noise matrix is the matrix of
            the correlation coefficients between the different components of the measurement.
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): the measurement
                referenceDate (:class:`~org.orekit.time.AbsoluteDate`): reference date
        
            Returns:
                decorated measurement
        
        
        """
        ...
    @staticmethod
    def filterRelevant(observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Filter relevant states for a measurement.
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): measurement to consider
                allStates (:class:`~org.orekit.propagation.SpacecraftState`[]): all states
        
            Returns:
                array containing only the states relevant to the measurement
        
        
        """
        ...

class KalmanObserver:
    """
    public interface KalmanObserver
    
        Observer for :class:`~org.orekit.estimation.sequential.KalmanEstimator` estimations.
    
        This interface is intended to be implemented by users to monitor the progress of the Kalman filter estimator during
        estimation.
    
        Since:
            9.2
    """
    def evaluationPerformed(self, kalmanEstimation: KalmanEstimation) -> None:
        """
            Notification callback after each one of a Kalman filter estimation.
        
            Parameters:
                estimation (:class:`~org.orekit.estimation.sequential.KalmanEstimation`): estimation performed by Kalman estimator
        
        
        """
        ...

class MeasurementDecorator(org.hipparchus.filtering.kalman.Measurement):
    """
    public class MeasurementDecorator extends Object implements Measurement
    
        Decorator adding null API to an :class:`~org.orekit.estimation.measurements.ObservedMeasurement`.
    
        Since:
            9.2
    """
    def __init__(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], realMatrix: org.hipparchus.linear.RealMatrix, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def getCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getObservedMeasurement(self) -> org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]:
        """
            Get the observed measurement.
        
            Returns:
                observed measurement
        
        
        """
        ...
    def getTime(self) -> float:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getValue(self) -> org.hipparchus.linear.RealVector:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...

class SemiAnalyticalKalmanEstimatorBuilder:
    """
    public class SemiAnalyticalKalmanEstimatorBuilder extends Object
    
        Builder for a Semi-analytical Kalman Filter.
    
        Since:
            11.1
    """
    def __init__(self): ...
    def addPropagationConfiguration(self, dSSTPropagatorBuilder: org.orekit.propagation.conversion.DSSTPropagatorBuilder, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'SemiAnalyticalKalmanEstimatorBuilder':
        """
            Add a propagation configuration.
        
            This method must be called once initialize the propagator builder used by the Kalman Filter.
        
            Parameters:
                builder (:class:`~org.orekit.propagation.conversion.DSSTPropagatorBuilder`): The propagator builder to use in the Kalman filter.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): The process noise matrices provider to use, consistent with the builder.
        
            Returns:
                this object.
        
        
        """
        ...
    def build(self) -> 'SemiAnalyticalKalmanEstimator':
        """
            Construct a :class:`~org.orekit.estimation.sequential.KalmanEstimator` from the data in this builder.
        
            Before this method is called,
            :meth:`~org.orekit.estimation.sequential.SemiAnalyticalKalmanEstimatorBuilder.addPropagationConfiguration` must have
            been called at least once, otherwise configuration is incomplete and an exception will be raised.
        
            Returns:
                a new :class:`~org.orekit.estimation.sequential.KalmanEstimator`.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer) -> 'SemiAnalyticalKalmanEstimatorBuilder':
        """
            Configure the matrix decomposer.
        
            Parameters:
                matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
            Returns:
                this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'SemiAnalyticalKalmanEstimatorBuilder':
        """
            Configure the estimated measurement parameters.
        
            If this method is not called, no measurement parameters will be estimated.
        
            Parameters:
                estimatedMeasurementsParams (:class:`~org.orekit.utils.ParameterDriversList`): The estimated measurements' parameters list.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): covariance matrix provider for the estimated measurement parameters
        
            Returns:
                this object.
        
        
        """
        ...

class SemiAnalyticalMeasurementHandler(org.orekit.propagation.sampling.OrekitStepHandler):
    """
    public class SemiAnalyticalMeasurementHandler extends Object implements :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
    
        :class:`~org.orekit.propagation.sampling.OrekitStepHandler` picking up
        :class:`~org.orekit.estimation.measurements.ObservedMeasurement` for both
        :class:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimator` and
        :class:`~org.orekit.estimation.sequential.SemiAnalyticalKalmanEstimator`.
    
        Since:
            11.3
    """
    def __init__(self, semiAnalyticalProcess: 'SemiAnalyticalProcess', kalmanFilter: org.hipparchus.filtering.kalman.KalmanFilter[MeasurementDecorator], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], absoluteDate: org.orekit.time.AbsoluteDate): ...
    def handleStep(self, orekitStepInterpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> None:
        """
            Handle the current step.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.handleStep`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): interpolator set up for the current step
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize step handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default method does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class SemiAnalyticalProcess:
    """
    public interface SemiAnalyticalProcess
    
        Interface for both :class:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanModel` and
        :class:`~org.orekit.estimation.sequential.SemiAnalyticalKalmanModel`.
    
        Since:
            11.3
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
            Finalize estimation.
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): measurement that has just been processed
                estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def finalizeOperationsObservationGrid(self) -> None:
        """
            Finalize estimation operations on the observation grid.
        
        """
        ...
    def getObserver(self) -> KalmanObserver:
        """
            Get the observer for Kalman Filter estimations.
        
            Returns:
                the observer for Kalman Filter estimations
        
        
        """
        ...
    def initializeShortPeriodicTerms(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Initialize the short periodic terms for the Kalman Filter.
        
            Parameters:
                meanState (:class:`~org.orekit.propagation.SpacecraftState`): mean state for auxiliary elements
        
        
        """
        ...
    def updateNominalSpacecraftState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Update the nominal spacecraft state.
        
            Parameters:
                nominal (:class:`~org.orekit.propagation.SpacecraftState`): nominal spacecraft state
        
        
        """
        ...
    def updateShortPeriods(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Update the DSST short periodic terms.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current mean state
        
        
        """
        ...

class SemiAnalyticalUnscentedKalmanEstimatorBuilder:
    """
    public class SemiAnalyticalUnscentedKalmanEstimatorBuilder extends Object
    
        Builder for an Unscented Semi-analytical Kalman filter estimator.
    
        Since:
            11.3
    """
    def __init__(self): ...
    def addPropagationConfiguration(self, dSSTPropagatorBuilder: org.orekit.propagation.conversion.DSSTPropagatorBuilder, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
        """
            Add a propagation configuration.
        
            This method must be called once initialize the propagator builder used by the Semi-Analytical Unscented Kalman Filter.
        
            Parameters:
                builder (:class:`~org.orekit.propagation.conversion.DSSTPropagatorBuilder`): The propagator builder to use in the Kalman filter.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): The process noise matrices provider to use, consistent with the builder.
        
            Returns:
                this object.
        
        
        """
        ...
    def build(self) -> 'SemiAnalyticalUnscentedKalmanEstimator':
        """
            Construct a :class:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimator` from the data in this
            builder.
        
            Before this method is called,
            :meth:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimatorBuilder.addPropagationConfiguration` must
            have been called at least once, otherwise configuration is incomplete and an exception will be raised.
        
            In addition, the
            :meth:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimatorBuilder.unscentedTransformProvider` must
            be called to configure the unscented transform provider use during the estimation process, otherwise configuration is
            incomplete and an exception will be raised.
        
            Returns:
                a new :class:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimator`.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
        """
            Configure the matrix decomposer.
        
            Parameters:
                matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
            Returns:
                this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
        """
            Configure the estimated measurement parameters.
        
            If this method is not called, no measurement parameters will be estimated.
        
            Parameters:
                estimatedMeasurementsParams (:class:`~org.orekit.utils.ParameterDriversList`): The estimated measurements' parameters list.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): covariance matrix provider for the estimated measurement parameters
        
            Returns:
                this object.
        
        
        """
        ...
    def unscentedTransformProvider(self, unscentedTransformProvider: org.hipparchus.util.UnscentedTransformProvider) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
        """
            Configure the unscented transform provider.
        
            Parameters:
                transformProvider (UnscentedTransformProvider): unscented transform to use for the prediction phase
        
            Returns:
                this object.
        
        
        """
        ...

class UnscentedKalmanEstimatorBuilder:
    """
    public class UnscentedKalmanEstimatorBuilder extends Object
    
        Builder for an Unscented Kalman filter estimator.
    
        Since:
            11.3
    """
    def __init__(self): ...
    def addPropagationConfiguration(self, numericalPropagatorBuilder: org.orekit.propagation.conversion.NumericalPropagatorBuilder, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'UnscentedKalmanEstimatorBuilder':
        """
            Add a propagation configuration.
        
            This method must be called once for each propagator to managed with the
            :class:`~org.orekit.estimation.sequential.UnscentedKalmanEstimator`. The propagators order in the Kalman filter will be
            the call order.
        
            The :code:`provider` should return a matrix with dimensions and ordering consistent with the :code:`builder`
            configuration. The first 6 rows/columns correspond to the 6 orbital parameters which must all be present, regardless of
            the fact they are estimated or not. The remaining elements correspond to the subset of propagation parameters that are
            estimated, in the same order as
            propagatorBuilder.:meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`.:meth:`~org.orekit.utils.ParameterDriversList.getDrivers`
            (but filtering out the non selected drivers).
        
            Parameters:
                builder (:class:`~org.orekit.propagation.conversion.NumericalPropagatorBuilder`): The propagator builder to use in the Kalman filter.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): The process noise matrices provider to use, consistent with the builder.
        
            Returns:
                this object.
        
            Also see:
                :meth:`~org.orekit.estimation.sequential.CovarianceMatrixProvider.getProcessNoiseMatrix`
        
        
        """
        ...
    def build(self) -> 'UnscentedKalmanEstimator':
        """
            Construct a :class:`~org.orekit.estimation.sequential.UnscentedKalmanEstimator` from the data in this builder.
        
            Before this method is called,
            :meth:`~org.orekit.estimation.sequential.UnscentedKalmanEstimatorBuilder.addPropagationConfiguration` must have been
            called at least once, otherwise configuration is incomplete and an exception will be raised.
        
            In addition, the :meth:`~org.orekit.estimation.sequential.UnscentedKalmanEstimatorBuilder.unscentedTransformProvider`
            must be called to configure the unscented transform provider use during the estimation process, otherwise configuration
            is incomplete and an exception will be raised.
        
            Returns:
                a new :class:`~org.orekit.estimation.sequential.UnscentedKalmanEstimator`.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer) -> 'UnscentedKalmanEstimatorBuilder':
        """
            Configure the matrix decomposer.
        
            Parameters:
                matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
            Returns:
                this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider) -> 'UnscentedKalmanEstimatorBuilder':
        """
            Configure the estimated measurement parameters.
        
            If this method is not called, no measurement parameters will be estimated.
        
            Parameters:
                estimatedMeasurementsParams (:class:`~org.orekit.utils.ParameterDriversList`): The estimated measurements' parameters list.
                provider (:class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`): covariance matrix provider for the estimated measurement parameters
        
            Returns:
                this object.
        
        
        """
        ...
    def unscentedTransformProvider(self, unscentedTransformProvider: org.hipparchus.util.UnscentedTransformProvider) -> 'UnscentedKalmanEstimatorBuilder':
        """
            Configure the unscented transform provider.
        
            Parameters:
                transformProvider (UnscentedTransformProvider): unscented transform to use for the prediction phase
        
            Returns:
                this object.
        
        
        """
        ...

class AbstractCovarianceMatrixProvider(CovarianceMatrixProvider):
    """
    public abstract class AbstractCovarianceMatrixProvider extends Object implements :class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`
    
        Abstract provider handling a predefined initial covariance matrix.
    
        This class always provides a predefined initial noise matrix.
    
        Since:
            9.2
    """
    def getInitialCovarianceMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the initial covariance matrix.
        
            The initial covariance matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the initial covariance matrix will be the output matrix of a previous run of the Kalman filter.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.CovarianceMatrixProvider.getInitialCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`
        
            Parameters:
                initial (:class:`~org.orekit.propagation.SpacecraftState`): initial state state
        
            Returns:
                physical (i.e. non normalized) initial covariance matrix
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
        """
        ...

class AbstractKalmanModel(KalmanEstimation, org.hipparchus.filtering.kalman.extended.NonLinearProcess[MeasurementDecorator]):
    """
    public abstract class AbstractKalmanModel extends Object implements :class:`~org.orekit.estimation.sequential.KalmanEstimation`, NonLinearProcess<:class:`~org.orekit.estimation.sequential.MeasurementDecorator`>
    
        Abstract class defining the process model dynamics to use with a
        :class:`~org.orekit.estimation.sequential.KalmanEstimator`.
    
        Since:
            11.0
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
            Finalize estimation.
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): measurement that has just been processed
                estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def getBuilders(self) -> java.util.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder]: ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the estimated measurement.
        
            This estimation has been evaluated on the last corrected orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the corrected spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current date.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentDate`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
            Get the current measurement number.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentMeasurementNumber`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current measurement number
        
        
        """
        ...
    def getEstimate(self) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
            Get the current corrected estimate.
        
            Returns:
                current corrected estimate
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated measurements parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedMeasurementsParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedOrbitalParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedPropagationParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated propagation parameters
        
        
        """
        ...
    def getEstimatedPropagators(self) -> typing.List[org.orekit.propagation.Propagator]:
        """
            Get the propagators estimated with the values set in the propagators builders.
        
            Returns:
                propagators based on the current values in the builder
        
        
        """
        ...
    def getEvolution(self, double: float, realVector: org.hipparchus.linear.RealVector, measurementDecorator: MeasurementDecorator) -> org.hipparchus.filtering.kalman.extended.NonLinearEvolution:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getInnovation(self, measurementDecorator: MeasurementDecorator, nonLinearEvolution: org.hipparchus.filtering.kalman.extended.NonLinearEvolution, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getMappers(self) -> typing.List[org.orekit.propagation.integration.AbstractJacobiansMapper]: ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the "physical" estimated covariance matrix (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the "physical" estimated state (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical innovation covariance matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalInnovationCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Kalman gain matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalKalmanGain`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalMeasurementJacobian`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
                measurement has been ignored)
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalStateTransitionMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
                process estimate)
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the predicted measurement.
        
            This estimation has been evaluated on the last predicted orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the predicted spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted spacecraft states
        
        
        """
        ...
    def getReferenceTrajectories(self) -> typing.List[org.orekit.propagation.Propagator]:
        """
            Getter for the reference trajectories.
        
            Returns:
                the referencetrajectories
        
        
        """
        ...
    def setHarvesters(self, matricesHarvesterArray: typing.List[org.orekit.propagation.MatricesHarvester]) -> None:
        """
            Setter for the jacobian harvesters.
        
            Parameters:
                harvesters (:class:`~org.orekit.propagation.MatricesHarvester`[]): the jacobian harvesters to set
        
            Since:
                11.1
        
        
        """
        ...
    def setMappers(self, abstractJacobiansMapperArray: typing.List[org.orekit.propagation.integration.AbstractJacobiansMapper]) -> None: ...
    def setReferenceTrajectories(self, propagatorArray: typing.List[org.orekit.propagation.Propagator]) -> None:
        """
            Setter for the reference trajectories.
        
            Parameters:
                referenceTrajectories (:class:`~org.orekit.propagation.Propagator`[]): the reference trajectories to be setted
        
        
        """
        ...

class KalmanEstimator(AbstractKalmanEstimator):
    """
    public class KalmanEstimator extends :class:`~org.orekit.estimation.sequential.AbstractKalmanEstimator`
    
        Implementation of a Kalman filter to perform orbit determination.
    
        The filter uses a :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder` to initialize its
        reference trajectory :class:`~org.orekit.propagation.numerical.NumericalPropagator` or
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        The estimated parameters are driven by :class:`~org.orekit.utils.ParameterDriver` objects. They are of 3 different
        types:
    
          1.  **Orbital parameters**:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized.
          2.  **Propagation parameters**: Some parameters modelling physical processes (SRP or drag coefficients etc...).
    
    
    They are also retrieved from the propagator builder during the initialization phase.
          3.  **Measurements parameters**: Parameters related to measurements (station biases, positions etc...).
    
    
    They are passed down to the filter in its constructor.
    
    
        The total number of estimated parameters is m, the size of the state vector.
    
        The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus. All the variables
        seen by Hipparchus (states, covariances, measurement matrices...) are normalized using a specific scale for each
        estimated parameters or standard deviation noise for each measurement components.
    
        A :class:`~org.orekit.estimation.sequential.KalmanEstimator` object is built using the
        :meth:`~org.orekit.estimation.sequential.KalmanEstimatorBuilder.build` method of a
        :class:`~org.orekit.estimation.sequential.KalmanEstimatorBuilder`.
    
        Since:
            9.2
    """
    def estimationStep(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> typing.List[org.orekit.propagation.Propagator]:
        """
            Process a single measurement.
        
            Update the filter with the new measurement by calling the estimate method.
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): the measurement to process
        
            Returns:
                estimated propagators
        
        
        """
        ...
    def processMeasurements(self, iterable: typing.Union[java.lang.Iterable[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Sequence[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Set[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]]) -> typing.List[org.orekit.propagation.Propagator]: ...
    def setObserver(self, kalmanObserver: KalmanObserver) -> None:
        """
            Set the observer.
        
            Parameters:
                observer (:class:`~org.orekit.estimation.sequential.KalmanObserver`): the observer
        
        
        """
        ...

class PythonAbstractKalmanEstimator(AbstractKalmanEstimator):
    """
    public class PythonAbstractKalmanEstimator extends :class:`~org.orekit.estimation.sequential.AbstractKalmanEstimator`
    """
    def __init__(self, list: java.util.List[org.orekit.propagation.conversion.PropagatorBuilder]): ...
    def finalize(self) -> None: ...
    def getKalmanEstimation(self) -> KalmanEstimation:
        """
            Description copied from class: :meth:`~org.orekit.estimation.sequential.AbstractKalmanEstimator.getKalmanEstimation`
            Get the provider for kalman filter estimations.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.AbstractKalmanEstimator.getKalmanEstimation`Â in
                classÂ :class:`~org.orekit.estimation.sequential.AbstractKalmanEstimator`
        
            Returns:
                the provider for Kalman filter estimations
        
        
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

class PythonCovarianceMatrixProvider(CovarianceMatrixProvider):
    """
    public class PythonCovarianceMatrixProvider extends Object implements :class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getInitialCovarianceMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the initial covariance matrix. Extension point for Python.
        
            The initial covariance matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the initial covariance matrix will be the output matrix of a previous run of the Kalman filter.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.CovarianceMatrixProvider.getInitialCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`
        
            Parameters:
                initial (:class:`~org.orekit.propagation.SpacecraftState`): initial state state
        
            Returns:
                physical (i.e. non normalized) initial covariance matrix
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
        """
        ...
    def getProcessNoiseMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState, spacecraftState2: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the process noise matrix between previous and current states. Extension point for Python.
        
            The process noise matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to
            0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.CovarianceMatrixProvider.getProcessNoiseMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`
        
            Parameters:
                previous (:class:`~org.orekit.propagation.SpacecraftState`): previous state
                current (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                physical (i.e. non normalized) process noise matrix between previous and current states
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
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

class PythonKalmanEstimation(KalmanEstimation):
    """
    public class PythonKalmanEstimation extends Object implements :class:`~org.orekit.estimation.sequential.KalmanEstimation`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the estimated measurement.
        
            This estimation has been evaluated on the last corrected orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the corrected spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current date.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentDate`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
            Get the current measurement number.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentMeasurementNumber`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current measurement number
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated measurements parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedMeasurementsParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedOrbitalParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedPropagationParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated propagation parameters
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the "physical" estimated covariance matrix (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the "physical" estimated state (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical innovation covariance matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalInnovationCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
            Since:
                9.3
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Kalman gain matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalKalmanGain`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
            Since:
                9.3
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalMeasurementJacobian`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
                measurement has been ignored)
        
            Since:
                9.3
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalStateTransitionMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
                process estimate)
        
            Since:
                9.3
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the predicted measurement.
        
            This estimation has been evaluated on the last predicted orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the predicted spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted spacecraft states
        
        
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

class PythonKalmanObserver(KalmanObserver):
    """
    public class PythonKalmanObserver extends Object implements :class:`~org.orekit.estimation.sequential.KalmanObserver`
    """
    def __init__(self): ...
    def evaluationPerformed(self, kalmanEstimation: KalmanEstimation) -> None:
        """
            Notification callback after each one of a Kalman filter estimation.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanObserver.evaluationPerformed`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanObserver`
        
            Parameters:
                estimation (:class:`~org.orekit.estimation.sequential.KalmanEstimation`): estimation performed by Kalman estimator
        
        
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

class PythonSemiAnalyticalProcess(SemiAnalyticalProcess):
    """
    public class PythonSemiAnalyticalProcess extends Object implements :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeEstimation`
            Finalize estimation.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeEstimation`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): measurement that has just been processed
                estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def finalizeOperationsObservationGrid(self) -> None:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeOperationsObservationGrid`
            Finalize estimation operations on the observation grid.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeOperationsObservationGrid`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
        
        """
        ...
    def getObserver(self) -> KalmanObserver:
        """
            Description copied from interface: :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.getObserver`
            Get the observer for Kalman Filter estimations.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.getObserver`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Returns:
                the observer for Kalman Filter estimations
        
        
        """
        ...
    def initializeShortPeriodicTerms(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.initializeShortPeriodicTerms`
            Initialize the short periodic terms for the Kalman Filter.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.initializeShortPeriodicTerms`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                meanState (:class:`~org.orekit.propagation.SpacecraftState`): mean state for auxiliary elements
        
        
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
    def updateNominalSpacecraftState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateNominalSpacecraftState`
            Update the nominal spacecraft state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateNominalSpacecraftState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                nominal (:class:`~org.orekit.propagation.SpacecraftState`): nominal spacecraft state
        
        
        """
        ...
    def updateShortPeriods(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateShortPeriods`
            Update the DSST short periodic terms.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateShortPeriods`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current mean state
        
        
        """
        ...

class SemiAnalyticalKalmanEstimator(AbstractKalmanEstimator):
    """
    public class SemiAnalyticalKalmanEstimator extends :class:`~org.orekit.estimation.sequential.AbstractKalmanEstimator`
    
        Implementation of an Extended Semi-analytical Kalman Filter (ESKF) to perform orbit determination.
    
        The filter uses a :class:`~org.orekit.propagation.conversion.DSSTPropagatorBuilder`.
    
        The estimated parameters are driven by :class:`~org.orekit.utils.ParameterDriver` objects. They are of 3 different
        types:
    
          1.  **Orbital parameters**:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized.
          2.  **Propagation parameters**: Some parameters modelling physical processes (SRP or drag coefficients).
    
    
    They are also retrieved from the propagator builder during the initialization phase.
          3.  **Measurements parameters**: Parameters related to measurements (station biases, positions etc...).
    
    
    They are passed down to the filter in its constructor.
    
    
        The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus. All the variables
        seen by Hipparchus (states, covariances, measurement matrices...) are normalized using a specific scale for each
        estimated parameters or standard deviation noise for each measurement components.
    
        Since:
            11.1
    
        Also see:
            "Folcik Z., Orbit Determination Using Modern Filters/Smoothers and Continuous Thrust Modeling, Master of Science Thesis,
            Department of Aeronautics and Astronautics, MIT, June, 2008.", "Cazabonne B., Bayard J., Journot M., and Cefola P. J., A
            Semi-analytical Approach for Orbit Determination based on Extended Kalman Filter, AAS Paper 21-614, AAS/AIAA
            Astrodynamics Specialist Conference, Big Sky, August 2021."
    """
    def __init__(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer, dSSTPropagatorBuilder: org.orekit.propagation.conversion.DSSTPropagatorBuilder, covarianceMatrixProvider: CovarianceMatrixProvider, parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider2: CovarianceMatrixProvider): ...
    def processMeasurements(self, list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator: ...
    def setObserver(self, kalmanObserver: KalmanObserver) -> None:
        """
            Set the observer.
        
            Parameters:
                observer (:class:`~org.orekit.estimation.sequential.KalmanObserver`): the observer
        
        
        """
        ...

class SemiAnalyticalKalmanModel(KalmanEstimation, org.hipparchus.filtering.kalman.extended.NonLinearProcess[MeasurementDecorator], SemiAnalyticalProcess):
    """
    public class SemiAnalyticalKalmanModel extends Object implements :class:`~org.orekit.estimation.sequential.KalmanEstimation`, NonLinearProcess<:class:`~org.orekit.estimation.sequential.MeasurementDecorator`>, :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
    
        Process model to use with a :class:`~org.orekit.estimation.sequential.SemiAnalyticalKalmanEstimator`.
    
        Since:
            11.1
    
        Also see:
            "Folcik Z., Orbit Determination Using Modern Filters/Smoothers and Continuous Thrust Modeling, Master of Science Thesis,
            Department of Aeronautics and Astronautics, MIT, June, 2008.", "Cazabonne B., Bayard J., Journot M., and Cefola P. J., A
            Semi-analytical Approach for Orbit Determination based on Extended Kalman Filter, AAS Paper 21-614, AAS/AIAA
            Astrodynamics Specialist Conference, Big Sky, August 2021."
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
            Finalize estimation.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeEstimation`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): measurement that has just been processed
                estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def finalizeOperationsObservationGrid(self) -> None:
        """
            Finalize estimation operations on the observation grid.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeOperationsObservationGrid`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
        
        """
        ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the estimated measurement.
        
            This estimation has been evaluated on the last corrected orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the corrected spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current date.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentDate`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
            Get the current measurement number.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentMeasurementNumber`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current measurement number
        
        
        """
        ...
    def getEstimate(self) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
            Get the current corrected estimate.
        
            Returns:
                current corrected estimate
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated measurements parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedMeasurementsParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedOrbitalParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedPropagationParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated propagation parameters
        
        
        """
        ...
    def getEstimatedPropagator(self) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
            Get the propagator estimated with the values set in the propagator builder.
        
            Returns:
                propagator based on the current values in the builder
        
        
        """
        ...
    def getEvolution(self, double: float, realVector: org.hipparchus.linear.RealVector, measurementDecorator: MeasurementDecorator) -> org.hipparchus.filtering.kalman.extended.NonLinearEvolution:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getInnovation(self, measurementDecorator: MeasurementDecorator, nonLinearEvolution: org.hipparchus.filtering.kalman.extended.NonLinearEvolution, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getObserver(self) -> KalmanObserver:
        """
            Get the observer for Kalman Filter estimations.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.getObserver`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Returns:
                the observer for Kalman Filter estimations
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the "physical" estimated covariance matrix (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the "physical" estimated state (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical innovation covariance matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalInnovationCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Kalman gain matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalKalmanGain`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalMeasurementJacobian`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
                measurement has been ignored)
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalStateTransitionMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
                process estimate)
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the predicted measurement.
        
            This estimation has been evaluated on the last predicted orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the predicted spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted spacecraft states
        
        
        """
        ...
    def initializeShortPeriodicTerms(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Initialize the short periodic terms for the Kalman Filter.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.initializeShortPeriodicTerms`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                meanState (:class:`~org.orekit.propagation.SpacecraftState`): mean state for auxiliary elements
        
        
        """
        ...
    def processMeasurements(self, list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], extendedKalmanFilter: org.hipparchus.filtering.kalman.extended.ExtendedKalmanFilter[MeasurementDecorator]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator: ...
    def setObserver(self, kalmanObserver: KalmanObserver) -> None:
        """
            Set the observer.
        
            Parameters:
                observer (:class:`~org.orekit.estimation.sequential.KalmanObserver`): the observer
        
        
        """
        ...
    def updateNominalSpacecraftState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Update the nominal spacecraft state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateNominalSpacecraftState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                nominal (:class:`~org.orekit.propagation.SpacecraftState`): nominal spacecraft state
        
        
        """
        ...
    def updateReferenceTrajectory(self, dSSTPropagator: org.orekit.propagation.semianalytical.dsst.DSSTPropagator) -> None:
        """
            Update the reference trajectories using the propagator as input.
        
            Parameters:
                propagator (:class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`): The new propagator to use
        
        
        """
        ...
    def updateShortPeriods(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Update the DSST short periodic terms.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateShortPeriods`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current mean state
        
        
        """
        ...

class SemiAnalyticalUnscentedKalmanEstimator(AbstractKalmanEstimator):
    """
    public class SemiAnalyticalUnscentedKalmanEstimator extends :class:`~org.orekit.estimation.sequential.AbstractKalmanEstimator`
    
        Implementation of an Unscented Semi-analytical Kalman filter (USKF) to perform orbit determination.
    
        The filter uses a :class:`~org.orekit.propagation.conversion.DSSTPropagatorBuilder`.
    
        The estimated parameters are driven by :class:`~org.orekit.utils.ParameterDriver` objects. They are of 3 different
        types:
    
          1.  **Orbital parameters**:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized.
          2.  **Propagation parameters**: Some parameters modeling physical processes (SRP or drag coefficients etc...).
    
    
    They are also retrieved from the propagator builder during the initialization phase.
          3.  **Measurements parameters**: Parameters related to measurements (station biases, positions etc...).
    
    
    They are passed down to the filter in its constructor.
    
    
        The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus. All the variables
        seen by Hipparchus (states, covariances...) are normalized using a specific scale for each estimated parameters or
        standard deviation noise for each measurement components.
    
        An :class:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimator` object is built using the
        :meth:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimatorBuilder.build` method of a
        :class:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimatorBuilder`.
    
        Since:
            11.3
    """
    def processMeasurements(self, list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator: ...
    def setObserver(self, kalmanObserver: KalmanObserver) -> None:
        """
            Set the observer.
        
            Parameters:
                observer (:class:`~org.orekit.estimation.sequential.KalmanObserver`): the observer
        
        
        """
        ...

class SemiAnalyticalUnscentedKalmanModel(KalmanEstimation, org.hipparchus.filtering.kalman.unscented.UnscentedProcess[MeasurementDecorator], SemiAnalyticalProcess):
    """
    public class SemiAnalyticalUnscentedKalmanModel extends Object implements :class:`~org.orekit.estimation.sequential.KalmanEstimation`, UnscentedProcess<:class:`~org.orekit.estimation.sequential.MeasurementDecorator`>, :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
    
        Class defining the process model dynamics to use with a
        :class:`~org.orekit.estimation.sequential.SemiAnalyticalUnscentedKalmanEstimator`.
    
        Since:
            11.3
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
            Finalize estimation.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeEstimation`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): measurement that has just been processed
                estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def finalizeOperationsObservationGrid(self) -> None:
        """
            Finalize estimation operations on the observation grid.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.finalizeOperationsObservationGrid`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
        
        """
        ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the estimated measurement.
        
            This estimation has been evaluated on the last corrected orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the corrected spacecraft states.
        
            Corrected state is osculating.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current date.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentDate`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
            Get the current measurement number.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentMeasurementNumber`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current measurement number
        
        
        """
        ...
    def getEstimate(self) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
            Get the current corrected estimate.
        
            For the Unscented Semi-analytical Kalman Filter it corresponds to the corrected filter correction. In other words, it
            doesn't represent an orbital state.
        
            Returns:
                current corrected estimate
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated measurements parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedMeasurementsParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedOrbitalParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedPropagationParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated propagation parameters
        
        
        """
        ...
    def getEstimatedPropagator(self) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
            Get the propagator estimated with the values set in the propagator builder.
        
            Returns:
                propagator based on the current values in the builder
        
        
        """
        ...
    def getEvolution(self, double: float, realVectorArray: typing.List[org.hipparchus.linear.RealVector], measurementDecorator: MeasurementDecorator) -> org.hipparchus.filtering.kalman.unscented.UnscentedEvolution:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getInnovation(self, measurementDecorator: MeasurementDecorator, realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getNumberSelectedMeasurementDrivers(self) -> int:
        """
            Get the number of estimated measurement parameters.
        
            Returns:
                the number of estimated measurement parameters
        
        
        """
        ...
    def getNumberSelectedOrbitalDrivers(self) -> int:
        """
            Get the number of estimated orbital parameters.
        
            Returns:
                the number of estimated orbital parameters
        
        
        """
        ...
    def getNumberSelectedPropagationDrivers(self) -> int:
        """
            Get the number of estimated propagation parameters.
        
            Returns:
                the number of estimated propagation parameters
        
        
        """
        ...
    def getObserver(self) -> KalmanObserver:
        """
            Get the observer for Kalman Filter estimations.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.getObserver`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Returns:
                the observer for Kalman Filter estimations
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the "physical" estimated covariance matrix (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the "physical" estimated state (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical innovation covariance matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalInnovationCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Kalman gain matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalKalmanGain`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalMeasurementJacobian`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
                measurement has been ignored)
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalStateTransitionMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
                process estimate)
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the predicted measurement.
        
            This estimation has been evaluated on the last predicted orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the predicted spacecraft states.
        
            Predicted state is osculating.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted spacecraft states
        
        
        """
        ...
    def initializeShortPeriodicTerms(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Initialize the short periodic terms for the Kalman Filter.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.initializeShortPeriodicTerms`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                meanState (:class:`~org.orekit.propagation.SpacecraftState`): mean state for auxiliary elements
        
        
        """
        ...
    def processMeasurements(self, list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], unscentedKalmanFilter: org.hipparchus.filtering.kalman.unscented.UnscentedKalmanFilter[MeasurementDecorator]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator: ...
    def setObserver(self, kalmanObserver: KalmanObserver) -> None:
        """
            Set the observer.
        
            Parameters:
                observer (:class:`~org.orekit.estimation.sequential.KalmanObserver`): the observer
        
        
        """
        ...
    def updateNominalSpacecraftState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Update the nominal spacecraft state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateNominalSpacecraftState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                nominal (:class:`~org.orekit.propagation.SpacecraftState`): nominal spacecraft state
        
        
        """
        ...
    def updateShortPeriods(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Update the DSST short periodic terms.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.SemiAnalyticalProcess.updateShortPeriods`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.SemiAnalyticalProcess`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current mean state
        
        
        """
        ...

class UnscentedKalmanEstimator(AbstractKalmanEstimator):
    """
    public class UnscentedKalmanEstimator extends :class:`~org.orekit.estimation.sequential.AbstractKalmanEstimator`
    
        Implementation of an Unscented Kalman filter to perform orbit determination.
    
        The filter uses a :class:`~org.orekit.propagation.conversion.NumericalPropagatorBuilder` to initialize its reference
        trajectory.
    
        The estimated parameters are driven by :class:`~org.orekit.utils.ParameterDriver` objects. They are of 3 different
        types:
    
          1.  **Orbital parameters**:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized.
          2.  **Propagation parameters**: Some parameters modelling physical processes (SRP or drag coefficients etc...).
    
    
    They are also retrieved from the propagator builder during the initialization phase.
          3.  **Measurements parameters**: Parameters related to measurements (station biases, positions etc...).
    
    
    They are passed down to the filter in its constructor.
    
    
        The total number of estimated parameters is m, the size of the state vector.
    
        The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus.
    
        An :class:`~org.orekit.estimation.sequential.UnscentedKalmanEstimator` object is built using the
        :meth:`~org.orekit.estimation.sequential.UnscentedKalmanEstimatorBuilder.build` method of a
        :class:`~org.orekit.estimation.sequential.UnscentedKalmanEstimatorBuilder`.
    
        Since:
            11.3
    """
    def estimationStep(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> typing.List[org.orekit.propagation.Propagator]:
        """
            Process a single measurement.
        
            Update the filter with the new measurement by calling the estimate method.
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): the measurement to process
        
            Returns:
                estimated propagator
        
        
        """
        ...
    def processMeasurements(self, iterable: typing.Union[java.lang.Iterable[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Sequence[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Set[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]]) -> typing.List[org.orekit.propagation.Propagator]: ...
    def setObserver(self, kalmanObserver: KalmanObserver) -> None:
        """
            Set the observer.
        
            Parameters:
                observer (:class:`~org.orekit.estimation.sequential.KalmanObserver`): the observer
        
        
        """
        ...

class UnscentedKalmanModel(KalmanEstimation, org.hipparchus.filtering.kalman.unscented.UnscentedProcess[MeasurementDecorator]):
    """
    public class UnscentedKalmanModel extends Object implements :class:`~org.orekit.estimation.sequential.KalmanEstimation`, UnscentedProcess<:class:`~org.orekit.estimation.sequential.MeasurementDecorator`>
    
        Class defining the process model dynamics to use with a
        :class:`~org.orekit.estimation.sequential.UnscentedKalmanEstimator`.
    
        Since:
            11.3
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
            Finalize estimation.
        
            Parameters:
                observedMeasurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> observedMeasurement): measurement that has just been processed
                estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the estimated measurement.
        
            This estimation has been evaluated on the last corrected orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the corrected spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCorrectedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current date.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentDate`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
            Get the current measurement number.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getCurrentMeasurementNumber`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                current measurement number
        
        
        """
        ...
    def getEstimate(self) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
            Get the current corrected estimate.
        
            Returns:
                current corrected estimate
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated measurements parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedMeasurementsParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedOrbitalParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the list of estimated propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getEstimatedPropagationParameters`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the list of estimated propagation parameters
        
        
        """
        ...
    def getEstimatedPropagators(self) -> typing.List[org.orekit.propagation.Propagator]:
        """
            Get the propagators estimated with the values set in the propagators builders.
        
            Returns:
                propagators based on the current values in the builder
        
        
        """
        ...
    def getEvolution(self, double: float, realVectorArray: typing.List[org.hipparchus.linear.RealVector], measurementDecorator: MeasurementDecorator) -> org.hipparchus.filtering.kalman.unscented.UnscentedEvolution:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getInnovation(self, measurementDecorator: MeasurementDecorator, realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the "physical" estimated covariance matrix (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the "physical" estimated state (i.e. not normalized)
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalEstimatedState`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical innovation covariance matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalInnovationCovarianceMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Kalman gain matrix.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalKalmanGain`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalMeasurementJacobian`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
                measurement has been ignored)
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPhysicalStateTransitionMatrix`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
                process estimate)
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
            Get the predicted measurement.
        
            This estimation has been evaluated on the last predicted orbits
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedMeasurement`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.List[org.orekit.propagation.SpacecraftState]:
        """
            Get the predicted spacecraft states.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.KalmanEstimation.getPredictedSpacecraftStates`Â in
                interfaceÂ :class:`~org.orekit.estimation.sequential.KalmanEstimation`
        
            Returns:
                predicted spacecraft states
        
        
        """
        ...

class ConstantProcessNoise(AbstractCovarianceMatrixProvider):
    """
    public class ConstantProcessNoise extends :class:`~org.orekit.estimation.sequential.AbstractCovarianceMatrixProvider`
    
        Provider for constant process noise matrices.
    
        This class always provides one initial noise matrix and one constant process noise matrix (both can be identical),
        regardless of states.
    
        Since:
            9.2
    """
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, realMatrix2: org.hipparchus.linear.RealMatrix): ...
    def getProcessNoiseMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState, spacecraftState2: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the process noise matrix between previous and current states.
        
            The process noise matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to
            0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
            Parameters:
                previous (:class:`~org.orekit.propagation.SpacecraftState`): previous state
                current (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                physical (i.e. non normalized) process noise matrix between previous and current states
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
        """
        ...

class DSSTKalmanModel(AbstractKalmanModel):
    """
    @Deprecated public class DSSTKalmanModel extends :class:`~org.orekit.estimation.sequential.AbstractKalmanModel`
    
        Deprecated.
        as of 11.1, replaced by :class:`~org.orekit.estimation.sequential.SemiAnalyticalKalmanModel`
        Class defining the process model dynamics to use with a :class:`~org.orekit.estimation.sequential.KalmanEstimator`.
    
        This class is an adaption of the :class:`~org.orekit.estimation.sequential.KalmanModel` class but for the
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        Since:
            10.0
    """
    def __init__(self, list: java.util.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list2: java.util.List[CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType): ...

class KalmanModel(AbstractKalmanModel):
    """
    public class KalmanModel extends :class:`~org.orekit.estimation.sequential.AbstractKalmanModel`
    
        Class defining the process model dynamics to use with a :class:`~org.orekit.estimation.sequential.KalmanEstimator`.
    
        Since:
            9.2
    """
    def __init__(self, list: java.util.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list2: java.util.List[CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider): ...

class PythonAbstractCovarianceMatrixProvider(AbstractCovarianceMatrixProvider):
    """
    public class PythonAbstractCovarianceMatrixProvider extends :class:`~org.orekit.estimation.sequential.AbstractCovarianceMatrixProvider`
    """
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix): ...
    def finalize(self) -> None: ...
    def getProcessNoiseMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState, spacecraftState2: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the process noise matrix between previous and current states. Extension point for Python.
        
            The process noise matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to
            0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
            Parameters:
                previous (:class:`~org.orekit.propagation.SpacecraftState`): previous state
                current (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                physical (i.e. non normalized) process noise matrix between previous and current states
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
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

class PythonAbstractKalmanModel(AbstractKalmanModel):
    """
    public class PythonAbstractKalmanModel extends :class:`~org.orekit.estimation.sequential.AbstractKalmanModel`
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list2: java.util.List[CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider, matricesHarvesterArray: typing.List[org.orekit.propagation.MatricesHarvester]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list2: java.util.List[CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider, matricesHarvesterArray: typing.List[org.orekit.propagation.MatricesHarvester], propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType): ...
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
    def updateReferenceTrajectories(self, propagatorArray: typing.List[org.orekit.propagation.Propagator], propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType) -> None:
        """
            Update the reference trajectories using the propagators as input.
        
            Specified by:
                :meth:`~org.orekit.estimation.sequential.AbstractKalmanModel.updateReferenceTrajectories`Â in
                classÂ :class:`~org.orekit.estimation.sequential.AbstractKalmanModel`
        
            Parameters:
                propagators (:class:`~org.orekit.propagation.Propagator`[]): The new propagators to use
                pType (:class:`~org.orekit.propagation.PropagationType`): propagationType type of the orbit used for the propagation (mean or osculating)
                sType (:class:`~org.orekit.propagation.PropagationType`): type of the elements used to define the orbital state (mean or osculating)
        
        
        """
        ...

class TLEKalmanModel(AbstractKalmanModel):
    """
    @Deprecated public class TLEKalmanModel extends :class:`~org.orekit.estimation.sequential.AbstractKalmanModel`
    
        Deprecated.
        as of 11.1, replaced by :class:`~org.orekit.estimation.sequential.KalmanModel`
        Class defining the process model dynamics to use with a :class:`~org.orekit.estimation.sequential.KalmanEstimator`.
    
        This class is an adaption of the :class:`~org.orekit.estimation.sequential.KalmanModel` class but for the
        :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`.
    
        Since:
            11.0
    """
    def __init__(self, list: java.util.List[org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder], list2: java.util.List[CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: CovarianceMatrixProvider): ...

class UnivariateProcessNoise(AbstractCovarianceMatrixProvider):
    """
    public class UnivariateProcessNoise extends :class:`~org.orekit.estimation.sequential.AbstractCovarianceMatrixProvider`
    
        Provider for a temporal evolution of the process noise matrix. All parameters (orbital or propagation) are time
        dependent and provided as null. The argument of the functions is a duration in seconds (between current and previous
        spacecraft state). The output of the functions must be of the dimension of a standard deviation. The method
        :meth:`~org.orekit.estimation.sequential.UnivariateProcessNoise.getProcessNoiseMatrix` then square the values so that
        they are consistent with a covariance matrix.
    
        The orbital parameters evolutions are provided in LOF frame and Cartesian (PV); then converted in inertial frame and
        current :class:`~org.orekit.orbits.OrbitType` and :class:`~org.orekit.orbits.PositionAngle` when method
        :meth:`~org.orekit.estimation.sequential.UnivariateProcessNoise.getProcessNoiseMatrix` is called.
    
        The time-dependent functions define a process noise matrix that is diagonal *in the Local Orbital Frame*, corresponds to
        Cartesian elements, abd represents the temporal evolution of (the standard deviation of) the process noise model. The
        first function is therefore the standard deviation along the LOF X axis, the second function represents the standard
        deviation along the LOF Y axis... This allows to set up simply a process noise representing an uncertainty that grows
        mainly along the track. The 6x6 upper left part of output matrix will however not be diagonal as it will be converted to
        the same inertial frame and orbit type as the :class:`~org.orekit.propagation.SpacecraftState` used by the
        :class:`~org.orekit.estimation.sequential.KalmanEstimator`.
    
        The propagation and measurements parameters are not associated to a specific frame and are appended as is in the lower
        right part diagonal of the output matrix. This implies this simplified model does not include correlation between the
        parameters and the orbit, but only evolution of the parameters themselves. If such correlations are needed, users must
        set up a custom :class:`~org.orekit.estimation.sequential.CovarianceMatrixProvider`. In most cases, the parameters are
        constant and their evolution noise is always 0, so the functions can be set to :code:`x -> 0`.
    
        This class always provides one initial noise matrix or initial covariance matrix and one process noise matrix.
    
        Since:
            9.2
    """
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, lOFType: org.orekit.frames.LOFType, positionAngle: org.orekit.orbits.PositionAngle, univariateFunctionArray: typing.List[org.hipparchus.analysis.UnivariateFunction], univariateFunctionArray2: typing.List[org.hipparchus.analysis.UnivariateFunction]): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, lOFType: org.orekit.frames.LOFType, positionAngle: org.orekit.orbits.PositionAngle, univariateFunctionArray: typing.List[org.hipparchus.analysis.UnivariateFunction], univariateFunctionArray2: typing.List[org.hipparchus.analysis.UnivariateFunction], univariateFunctionArray3: typing.List[org.hipparchus.analysis.UnivariateFunction]): ...
    def getLofCartesianOrbitalParametersEvolution(self) -> typing.List[org.hipparchus.analysis.UnivariateFunction]:
        """
            Getter for the lofCartesianOrbitalParametersEvolution.
        
            Returns:
                the lofCartesianOrbitalParametersEvolution
        
        
        """
        ...
    def getLofType(self) -> org.orekit.frames.LOFType:
        """
            Getter for the lofType.
        
            Returns:
                the lofType
        
        
        """
        ...
    def getMeasurementsParametersEvolution(self) -> typing.List[org.hipparchus.analysis.UnivariateFunction]:
        """
            Getter for the measurementsParametersEvolution.
        
            Returns:
                the measurementsParametersEvolution
        
        
        """
        ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle:
        """
            Getter for the positionAngle.
        
            Returns:
                the positionAngle
        
        
        """
        ...
    def getProcessNoiseMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState, spacecraftState2: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the process noise matrix between previous and current states.
        
            The process noise matrix is a covariance matrix corresponding to the parameters managed by the
            :class:`~org.orekit.estimation.sequential.KalmanEstimator`. The number of rows/columns and their order are as follows:
        
              - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
                be present, regardless of the fact they are estimated or not.
              - The following components correspond to the subset of propagation parameters of the associated propagator that are
                estimated.
              - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
                measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        
            In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to
            0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
            Parameters:
                previous (:class:`~org.orekit.propagation.SpacecraftState`): previous state
                current (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                physical (i.e. non normalized) process noise matrix between previous and current states
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`
        
        
        """
        ...
    def getPropagationParametersEvolution(self) -> typing.List[org.hipparchus.analysis.UnivariateFunction]:
        """
            Getter for the propagationParametersEvolution.
        
            Returns:
                the propagationParametersEvolution
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.sequential")``.

    AbstractCovarianceMatrixProvider: typing.Type[AbstractCovarianceMatrixProvider]
    AbstractKalmanEstimator: typing.Type[AbstractKalmanEstimator]
    AbstractKalmanModel: typing.Type[AbstractKalmanModel]
    ConstantProcessNoise: typing.Type[ConstantProcessNoise]
    CovarianceMatrixProvider: typing.Type[CovarianceMatrixProvider]
    DSSTKalmanModel: typing.Type[DSSTKalmanModel]
    EskfMeasurementHandler: typing.Type[EskfMeasurementHandler]
    KalmanEstimation: typing.Type[KalmanEstimation]
    KalmanEstimator: typing.Type[KalmanEstimator]
    KalmanEstimatorBuilder: typing.Type[KalmanEstimatorBuilder]
    KalmanEstimatorUtil: typing.Type[KalmanEstimatorUtil]
    KalmanModel: typing.Type[KalmanModel]
    KalmanObserver: typing.Type[KalmanObserver]
    MeasurementDecorator: typing.Type[MeasurementDecorator]
    PythonAbstractCovarianceMatrixProvider: typing.Type[PythonAbstractCovarianceMatrixProvider]
    PythonAbstractKalmanEstimator: typing.Type[PythonAbstractKalmanEstimator]
    PythonAbstractKalmanModel: typing.Type[PythonAbstractKalmanModel]
    PythonCovarianceMatrixProvider: typing.Type[PythonCovarianceMatrixProvider]
    PythonKalmanEstimation: typing.Type[PythonKalmanEstimation]
    PythonKalmanObserver: typing.Type[PythonKalmanObserver]
    PythonSemiAnalyticalProcess: typing.Type[PythonSemiAnalyticalProcess]
    SemiAnalyticalKalmanEstimator: typing.Type[SemiAnalyticalKalmanEstimator]
    SemiAnalyticalKalmanEstimatorBuilder: typing.Type[SemiAnalyticalKalmanEstimatorBuilder]
    SemiAnalyticalKalmanModel: typing.Type[SemiAnalyticalKalmanModel]
    SemiAnalyticalMeasurementHandler: typing.Type[SemiAnalyticalMeasurementHandler]
    SemiAnalyticalProcess: typing.Type[SemiAnalyticalProcess]
    SemiAnalyticalUnscentedKalmanEstimator: typing.Type[SemiAnalyticalUnscentedKalmanEstimator]
    SemiAnalyticalUnscentedKalmanEstimatorBuilder: typing.Type[SemiAnalyticalUnscentedKalmanEstimatorBuilder]
    SemiAnalyticalUnscentedKalmanModel: typing.Type[SemiAnalyticalUnscentedKalmanModel]
    TLEKalmanModel: typing.Type[TLEKalmanModel]
    UnivariateProcessNoise: typing.Type[UnivariateProcessNoise]
    UnscentedKalmanEstimator: typing.Type[UnscentedKalmanEstimator]
    UnscentedKalmanEstimatorBuilder: typing.Type[UnscentedKalmanEstimatorBuilder]
    UnscentedKalmanModel: typing.Type[UnscentedKalmanModel]
