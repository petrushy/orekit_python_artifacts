
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org
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
import org.orekit.propagation.sampling
import org.orekit.propagation.semianalytical.dsst
import org.orekit.time
import org.orekit.utils
import typing



class AbstractKalmanEstimator:
    """
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
    def getObserver(self) -> 'KalmanObserver':
        """
        Get the observer.
        
        Returns:
            the observer
        
        
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
        
        For the Semi-analytical Kalman Filters it corresponds to the corrected filter correction. In other words, it doesn't represent an orbital state.
        
        Returns:
            the "physical" estimated state
        
        
        """
        ...
    def getPropagationParametersDrivers(self, estimatedOnly: bool) -> org.orekit.utils.ParameterDriversList:
        """
        Get the propagator parameters supported by this estimator.
        
        Parameters:
            estimatedOnly (boolean): if true, only estimated parameters are returned
        
        Returns:
            propagator parameters supported by this estimator
        
        
        """
        ...
    def setObserver(self, observer: typing.Union['KalmanObserver', typing.Callable]) -> None:
        """
        Set the observer.
        
        Parameters:
            observer (KalmanObserver): the observer
        
        
        """
        ...

class CovarianceMatrixProvider:
    """
    Provider for process noise matrices.
    
    Since:
        9.2
    """
    def getInitialCovarianceMatrix(self, initial: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the initial covariance matrix.
        
        The initial covariance matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the initial covariance matrix will be the output matrix of a previous run of the Kalman filter.
        
        Parameters:
            initial (SpacecraftState): initial state state
        
        Returns:
            physical (i.e. non normalized) initial covariance matrix
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
        """
        ...
    def getProcessNoiseMatrix(self, previous: org.orekit.propagation.SpacecraftState, current: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the process noise matrix between previous and current states.
        
        The process noise matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to 0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
        Parameters:
            previous (SpacecraftState): previous state
            current (SpacecraftState): current state
        
        Returns:
            physical (i.e. non normalized) process noise matrix between previous and current states
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
        """
        ...

class KalmanEstimation:
    """
    Interface for accessing KalmanEstimator estimations. The "physical" term used to characterize the states and matrices is used per opposition to the "normalized" states and matrices used to perform the computation.
    
    Since:
        9.2
    """
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
        EstimatedMeasurement<?> getCorrectedMeasurement()
        
        Get the estimated measurement.
        
        This estimation has been evaluated on the last corrected orbits
        
        Returns:
            corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
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
        EstimatedMeasurement<?> getPredictedMeasurement()
        
        Get the predicted measurement.
        
        This estimation has been evaluated on the last predicted orbits
        
        Returns:
            predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the predicted spacecraft states.
        
        Returns:
            predicted spacecraft states
        
        
        """
        ...

class KalmanEstimatorBuilder:
    """
    Builder for a Kalman filter estimator.
    
    Since:
        9.2
    """
    def __init__(self):
        """
        Default constructor. Set an extended Kalman filter, with linearized covariance prediction.
        """
        ...
    def addPropagationConfiguration(self, builder: org.orekit.propagation.conversion.PropagatorBuilder, provider: CovarianceMatrixProvider) -> 'KalmanEstimatorBuilder':
        """
        Add a propagation configuration.
        
        This method must be called once for each propagator to managed with the KalmanEstimator. The propagators order in the Kalman filter will be the call order.
        
        The provider should return a matrix with dimensions and ordering consistent with the builder configuration. The first 6 rows/columns correspond to the 6 orbital parameters. The remaining elements correspond to the subset of propagation parameters that are estimated, in the same order as propagatorBuilder.getPropagationParametersDrivers.getDrivers (but filtering out the non selected drivers).
        
        Parameters:
            builder (PropagatorBuilder): The propagator builder to use in the Kalman filter.
            provider (CovarianceMatrixProvider): The process noise matrices provider to use, consistent with the builder. This parameter can be equal to null if
                the input builder is an EphemerisPropagatorBuilder. Indeed, for ephemeris
                based estimation only measurement parameters are estimated. Therefore, the covariance related to dynamical parameters
                can be null.
        
        Returns:
            this object.
        
        Also see:
            getProcessNoiseMatrix
        
        
        """
        ...
    def build(self) -> 'KalmanEstimator':
        """
        Construct a KalmanEstimator from the data in this builder.
        
        Before this method is called, addPropagationConfiguration must have been called at least once, otherwise configuration is incomplete and an exception will be raised.
        
        Returns:
            a new KalmanEstimator.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]) -> 'KalmanEstimatorBuilder':
        """
        Configure the matrix decomposer.
        
        Parameters:
            matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
        Returns:
            this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, estimatedMeasurementsParams: org.orekit.utils.ParameterDriversList, provider: CovarianceMatrixProvider) -> 'KalmanEstimatorBuilder':
        """
        Configure the estimated measurement parameters.
        
        If this method is not called, no measurement parameters will be estimated.
        
        Parameters:
            estimatedMeasurementsParams (ParameterDriversList): The estimated measurements' parameters list.
            provider (CovarianceMatrixProvider): covariance matrix provider for the estimated measurement parameters
        
        Returns:
            this object.
        
        Since:
            10.3
        
        
        """
        ...

class KalmanEstimatorUtil:
    """
    Utility class for Kalman Filter.
    
    This class includes common methods used by the different Kalman models in Orekit (i.e., Extended, Unscented, and Semi-analytical)
    
    Since:
        11.3
    """
    _applyDynamicOutlierFilter__T = typing.TypeVar('_applyDynamicOutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def applyDynamicOutlierFilter(measurement: org.orekit.estimation.measurements.EstimatedMeasurement[_applyDynamicOutlierFilter__T], innovationCovarianceMatrix: org.hipparchus.linear.RealMatrix) -> None:
        """
        Set and apply a dynamic outlier filter on a measurement.
        
        Loop on the modifiers to see if a dynamic outlier filter needs to be applied.
        
        Compute the sigma array using the matrix in input and set the filter.
        
        Apply the filter by calling the modify method on the estimated measurement.
        
        Reset the filter.
        
        Parameters:
            measurement (EstimatedMeasurement<T> measurement): measurement to filter
            innovationCovarianceMatrix (RealMatrix): So called innovation covariance matrix S, with:
        
                S = H.Ppred.Ht + R
        
                Where:
        
                - H is the normalized measurement matrix (Ht its transpose)
        
                - Ppred is the normalized predicted covariance matrix
        
                - R is the normalized measurement noise matrix
        
        
        """
        ...
    @staticmethod
    def checkDimension(dimension: int, orbitalParameters: org.orekit.utils.ParameterDriversList, propagationParameters: org.orekit.utils.ParameterDriversList, measurementParameters: org.orekit.utils.ParameterDriversList) -> None:
        """
        Check dimension.
        
        Parameters:
            dimension (int): dimension to check
            orbitalParameters (ParameterDriversList): orbital parameters
            propagationParameters (ParameterDriversList): propagation parameters
            measurementParameters (ParameterDriversList): measurements parameters
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeInnovationVector(predicted: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]) -> org.hipparchus.linear.RealVector:
        """
        Compute the unnormalized innovation vector from the given predicted measurement.
        
        Parameters:
            predicted (EstimatedMeasurement<?> predicted): predicted measurement
        
        Returns:
            the innovation vector
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeInnovationVector(predicted: org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any], sigma: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealVector:
        """
        Compute the normalized innovation vector from the given predicted measurement.
        
        Parameters:
            predicted (EstimatedMeasurement<?> predicted): predicted measurement
            sigma (double[]): measurement standard deviation
        
        Returns:
            the innovation vector
        
        
        """
        ...
    @staticmethod
    def decorate(observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], referenceDate: org.orekit.time.AbsoluteDate) -> 'MeasurementDecorator':
        """
        Decorate an observed measurement.
        
        The "physical" measurement noise matrix is the covariance matrix of the measurement. Normalizing it consists in applying the following equation: Rn[i,j] = R[i,j]/σ[i]/σ[j] Thus the normalized measurement noise matrix is the matrix of the correlation coefficients between the different components of the measurement.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): the measurement
            referenceDate (AbsoluteDate): reference date
        
        Returns:
            decorated measurement
        
        
        """
        ...
    @staticmethod
    def decorateUnscented(observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], referenceDate: org.orekit.time.AbsoluteDate) -> 'MeasurementDecorator':
        """
        Decorate an observed measurement for an Unscented Kalman Filter.
        
        This method uses directly the measurement's covariance matrix, without any normalization.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): the measurement
            referenceDate (AbsoluteDate): reference date
        
        Returns:
            decorated measurement
        
        Since:
            11.3.2
        
        
        """
        ...
    @staticmethod
    def filterRelevant(observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], allStates: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Filter relevant states for a measurement.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): measurement to consider
            allStates (SpacecraftState[]): all states
        
        Returns:
            array containing only the states relevant to the measurement
        
        
        """
        ...
    @staticmethod
    def normalizeCovarianceMatrix(physicalP: org.hipparchus.linear.RealMatrix, parameterScales: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Normalize a covariance matrix.
        
        Parameters:
            physicalP (RealMatrix): "physical" covariance matrix in input
            parameterScales (double[]): scale factor of estimated parameters
        
        Returns:
            the normalized covariance matrix
        
        
        """
        ...
    @staticmethod
    def unnormalizeCovarianceMatrix(normalizedP: org.hipparchus.linear.RealMatrix, parameterScales: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Un-nomalized the covariance matrix.
        
        Parameters:
            normalizedP (RealMatrix): normalized covariance matrix
            parameterScales (double[]): scale factor of estimated parameters
        
        Returns:
            the un-normalized covariance matrix
        
        
        """
        ...
    @staticmethod
    def unnormalizeInnovationCovarianceMatrix(normalizedS: org.hipparchus.linear.RealMatrix, sigmas: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Un-normalize the innovation covariance matrix.
        
        Parameters:
            normalizedS (RealMatrix): normalized innovation covariance matrix
            sigmas (double[]): measurement theoretical standard deviation
        
        Returns:
            the un-normalized innovation covariance matrix
        
        
        """
        ...
    @staticmethod
    def unnormalizeKalmanGainMatrix(normalizedK: org.hipparchus.linear.RealMatrix, parameterScales: typing.Union[typing.List[float], jpype.JArray], sigmas: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Un-normalize the Kalman gain matrix.
        
        Parameters:
            normalizedK (RealMatrix): normalized Kalman gain matrix
            parameterScales (double[]): scale factor of estimated parameters
            sigmas (double[]): measurement theoretical standard deviation
        
        Returns:
            the un-normalized Kalman gain matrix
        
        
        """
        ...
    @staticmethod
    def unnormalizeMeasurementJacobian(normalizedH: org.hipparchus.linear.RealMatrix, parameterScales: typing.Union[typing.List[float], jpype.JArray], sigmas: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Un-normalize the measurement matrix.
        
        Parameters:
            normalizedH (RealMatrix): normalized measurement matrix
            parameterScales (double[]): scale factor of estimated parameters
            sigmas (double[]): measurement theoretical standard deviation
        
        Returns:
            the un-normalized measurement matrix
        
        
        """
        ...
    @staticmethod
    def unnormalizeStateTransitionMatrix(normalizedSTM: org.hipparchus.linear.RealMatrix, parameterScales: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Un-nomalized the state transition matrix.
        
        Parameters:
            normalizedSTM (RealMatrix): normalized state transition matrix
            parameterScales (double[]): scale factor of estimated parameters
        
        Returns:
            the un-normalized state transition matrix
        
        
        """
        ...

class KalmanObserver:
    """
    Observer for KalmanEstimator estimations.
    
    This interface is intended to be implemented by users to monitor the progress of the Kalman filter estimator during estimation.
    
    Since:
        9.2
    """
    def evaluationPerformed(self, estimation: KalmanEstimation) -> None:
        """
        Notification callback after each one of a Kalman filter estimation.
        
        Parameters:
            estimation (KalmanEstimation): estimation performed by Kalman estimator
        
        
        """
        ...
    def init(self, estimation: KalmanEstimation) -> None:
        """
        Initialise the observer on the initial state of the filter, before processing the first measurement.
        
        Parameters:
            estimation (KalmanEstimation): estimation performed by Kalman estimator
        
        
        """
        ...

class MeasurementDecorator(org.hipparchus.filtering.kalman.Measurement):
    """
    Decorator adding Measurement API to an ObservedMeasurement.
    
    Since:
        9.2
    """
    def __init__(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], covariance: org.hipparchus.linear.RealMatrix, reference: org.orekit.time.AbsoluteDate):
        """
        Simple constructor.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): observed measurement
            covariance (RealMatrix): measurement covariance
            reference (AbsoluteDate): reference date
        
        
        """
        ...
    def getCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.Measurement.html?is` in interface Measurement
        
        
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
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.Measurement.html?is` in interface Measurement
        
        
        """
        ...
    def getValue(self) -> org.hipparchus.linear.RealVector:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.Measurement.html?is` in interface Measurement
        
        
        """
        ...

class PhysicalEstimatedState(org.orekit.time.TimeStamped):
    """
    Container for smoothed states (time, mean and covariance) generated by an RtsSmoother.
    
    The order of the parameters in the state and covariance are the same as produced by the underlying sequential (Kalman or unscented) estimator.
    
    Since:
        13.0
    
    Also see:
        RtsSmoother
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, state: org.hipparchus.linear.RealVector, covarianceMatrix: org.hipparchus.linear.RealMatrix):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): date
            state (RealVector): mean state
            covarianceMatrix (RealMatrix): covariance matrix
        
        
        """
        ...
    def getCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the covariance matrix in "physical" (not normalised) units.
        
        Returns:
            the state covariance matrix
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getState(self) -> org.hipparchus.linear.RealVector:
        """
        Get the state in "physical" (not normalised) units.
        
        Returns:
            the state mean
        
        
        """
        ...

class SemiAnalyticalKalmanEstimatorBuilder:
    """
    Builder for a Semi-analytical Kalman Filter.
    
    Since:
        11.1
    """
    def __init__(self):
        """
        Default constructor. Set an Extended Semi-analytical Kalman Filter.
        """
        ...
    def addPropagationConfiguration(self, builder: org.orekit.propagation.conversion.DSSTPropagatorBuilder, provider: CovarianceMatrixProvider) -> 'SemiAnalyticalKalmanEstimatorBuilder':
        """
        Add a propagation configuration.
        
        This method must be called once initialize the propagator builder used by the Kalman Filter.
        
        Parameters:
            builder (DSSTPropagatorBuilder): The propagator builder to use in the Kalman filter.
            provider (CovarianceMatrixProvider): The process noise matrices provider to use, consistent with the builder.
        
        Returns:
            this object.
        
        
        """
        ...
    def build(self) -> 'SemiAnalyticalKalmanEstimator':
        """
        Construct a KalmanEstimator from the data in this builder.
        
        Before this method is called, addPropagationConfiguration must have been called at least once, otherwise configuration is incomplete and an exception will be raised.
        
        Returns:
            a new KalmanEstimator.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]) -> 'SemiAnalyticalKalmanEstimatorBuilder':
        """
        Configure the matrix decomposer.
        
        Parameters:
            matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
        Returns:
            this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, estimatedMeasurementsParams: org.orekit.utils.ParameterDriversList, provider: CovarianceMatrixProvider) -> 'SemiAnalyticalKalmanEstimatorBuilder':
        """
        Configure the estimated measurement parameters.
        
        If this method is not called, no measurement parameters will be estimated.
        
        Parameters:
            estimatedMeasurementsParams (ParameterDriversList): The estimated measurements' parameters list.
            provider (CovarianceMatrixProvider): covariance matrix provider for the estimated measurement parameters
        
        Returns:
            this object.
        
        
        """
        ...

class SemiAnalyticalMeasurementHandler(org.orekit.propagation.sampling.OrekitStepHandler):
    """
    OrekitStepHandler picking up ObservedMeasurement for both SemiAnalyticalUnscentedKalmanEstimator and SemiAnalyticalKalmanEstimator.
    
    Since:
        11.3
    """
    @typing.overload
    def __init__(self, model: 'SemiAnalyticalProcess', filter: org.hipparchus.filtering.kalman.KalmanFilter[MeasurementDecorator], observedMeasurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], referenceDate: org.orekit.time.AbsoluteDate): ...
    @typing.overload
    def __init__(self, model: 'SemiAnalyticalProcess', filter: org.hipparchus.filtering.kalman.KalmanFilter[MeasurementDecorator], observedMeasurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], referenceDate: org.orekit.time.AbsoluteDate, isUnscented: bool): ...
    def handleStep(self, interpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface OrekitStepHandler
        
        Parameters:
            interpolator (OrekitStepInterpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface OrekitStepHandler
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class SemiAnalyticalProcess:
    """
    Interface for both SemiAnalyticalUnscentedKalmanModel and SemiAnalyticalKalmanModel.
    
    Since:
        11.3
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], estimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
        Finalize estimation.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): measurement that has just been processed
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
    def initializeShortPeriodicTerms(self, meanState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Initialize the short periodic terms for the Kalman Filter.
        
        Parameters:
            meanState (SpacecraftState): mean state for auxiliary elements
        
        
        """
        ...
    def updateNominalSpacecraftState(self, nominal: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the nominal spacecraft state.
        
        Parameters:
            nominal (SpacecraftState): nominal spacecraft state
        
        
        """
        ...
    def updateShortPeriods(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the DSST short periodic terms.
        
        Parameters:
            state (SpacecraftState): current mean state
        
        
        """
        ...

class SemiAnalyticalUnscentedKalmanEstimatorBuilder:
    """
    Builder for an Unscented Semi-analytical Kalman filter estimator.
    
    Since:
        11.3
    """
    def __init__(self):
        """
        Default constructor. Set an Unscented Semi-analytical Kalman filter.
        """
        ...
    def addPropagationConfiguration(self, builder: org.orekit.propagation.conversion.DSSTPropagatorBuilder, provider: CovarianceMatrixProvider) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
        """
        Add a propagation configuration.
        
        This method must be called once initialize the propagator builder used by the Semi-Analytical Unscented Kalman Filter.
        
        Parameters:
            builder (DSSTPropagatorBuilder): The propagator builder to use in the Kalman filter.
            provider (CovarianceMatrixProvider): The process noise matrices provider to use, consistent with the builder.
        
        Returns:
            this object.
        
        
        """
        ...
    def build(self) -> 'SemiAnalyticalUnscentedKalmanEstimator':
        """
        Construct a SemiAnalyticalUnscentedKalmanEstimator from the data in this builder.
        
        Before this method is called, addPropagationConfiguration must have been called at least once, otherwise configuration is incomplete and an exception will be raised.
        
        In addition, the unscentedTransformProvider must be called to configure the unscented transform provider use during the estimation process, otherwise configuration is incomplete and an exception will be raised.
        
        Returns:
            a new SemiAnalyticalUnscentedKalmanEstimator.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
        """
        Configure the matrix decomposer.
        
        Parameters:
            matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
        Returns:
            this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, estimatedMeasurementsParams: org.orekit.utils.ParameterDriversList, provider: CovarianceMatrixProvider) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
        """
        Configure the estimated measurement parameters.
        
        If this method is not called, no measurement parameters will be estimated.
        
        Parameters:
            estimatedMeasurementsParams (ParameterDriversList): The estimated measurements' parameters list.
            provider (CovarianceMatrixProvider): covariance matrix provider for the estimated measurement parameters
        
        Returns:
            this object.
        
        
        """
        ...
    def unscentedTransformProvider(self, transformProvider: org.hipparchus.util.UnscentedTransformProvider) -> 'SemiAnalyticalUnscentedKalmanEstimatorBuilder':
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
    Builder for an Unscented Kalman filter estimator.
    
    The builder is generalized to accept any PropagatorBuilder. Howerver, it is absolutely not recommended to use a DSSTPropagatorBuilder. A specific SemiAnalyticalUnscentedKalmanEstimatorBuilder is implemented and shall be used.
    
    Since:
        11.3
    """
    def __init__(self):
        """
        Default constructor. Set an Unscented Kalman filter.
        """
        ...
    def addPropagationConfiguration(self, builder: org.orekit.propagation.conversion.PropagatorBuilder, provider: CovarianceMatrixProvider) -> 'UnscentedKalmanEstimatorBuilder':
        """
        Add a propagation configuration.
        
        This method must be called once for each propagator to managed with the UnscentedKalmanEstimator. The propagators order in the Kalman filter will be the call order.
        
        The provider should return a matrix with dimensions and ordering consistent with the builder configuration. The first 6 rows/columns correspond to the 6 orbital parameters which must all be present, regardless of the fact they are estimated or not. The remaining elements correspond to the subset of propagation parameters that are estimated, in the same order as propagatorBuilder.getPropagationParametersDrivers.getDrivers (but filtering out the non selected drivers).
        
        Parameters:
            builder (PropagatorBuilder): The propagator builder to use in the Kalman filter.
            provider (CovarianceMatrixProvider): The process noise matrices provider to use, consistent with the builder.
        
        Returns:
            this object.
        
        Also see:
            getProcessNoiseMatrix
        
        
        """
        ...
    def build(self) -> 'UnscentedKalmanEstimator':
        """
        Construct a UnscentedKalmanEstimator from the data in this builder.
        
        Before this method is called, addPropagationConfiguration must have been called at least once, otherwise configuration is incomplete and an exception will be raised.
        
        In addition, the unscentedTransformProvider must be called to configure the unscented transform provider use during the estimation process, otherwise configuration is incomplete and an exception will be raised.
        
        Returns:
            a new UnscentedKalmanEstimator.
        
        
        """
        ...
    def decomposer(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]) -> 'UnscentedKalmanEstimatorBuilder':
        """
        Configure the matrix decomposer.
        
        Parameters:
            matrixDecomposer (MatrixDecomposer): decomposer to use for the correction phase
        
        Returns:
            this object.
        
        
        """
        ...
    def estimatedMeasurementsParameters(self, estimatedMeasurementsParams: org.orekit.utils.ParameterDriversList, provider: CovarianceMatrixProvider) -> 'UnscentedKalmanEstimatorBuilder':
        """
        Configure the estimated measurement parameters.
        
        If this method is not called, no measurement parameters will be estimated.
        
        Parameters:
            estimatedMeasurementsParams (ParameterDriversList): The estimated measurements' parameters list.
            provider (CovarianceMatrixProvider): covariance matrix provider for the estimated measurement parameters
        
        Returns:
            this object.
        
        
        """
        ...
    def unscentedTransformProvider(self, transformProvider: org.hipparchus.util.UnscentedTransformProvider) -> 'UnscentedKalmanEstimatorBuilder':
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
    Abstract provider handling a predefined initial covariance matrix.
    
    This class always provides a predefined initial noise matrix.
    
    Since:
        9.2
    """
    def getInitialCovarianceMatrix(self, initial: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the initial covariance matrix.
        
        The initial covariance matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the initial covariance matrix will be the output matrix of a previous run of the Kalman filter.
        
        Specified by: getInitialCovarianceMatrix in interface CovarianceMatrixProvider
        
        Parameters:
            initial (SpacecraftState): initial state state
        
        Returns:
            physical (i.e. non normalized) initial covariance matrix
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
        """
        ...

class KalmanEstimator(AbstractKalmanEstimator):
    """
    Implementation of a Kalman filter to perform orbit determination.
    
    The filter uses a PropagatorBuilder to initialize its reference trajectory. The Kalman estimator can be used with a NumericalPropagator, TLEPropagator, BrouwerLyddanePropagator, EcksteinHechlerPropagator, KeplerianPropagator, or Ephemeris.
    
    Kalman estimation using a DSSTPropagator must be done using the SemiAnalyticalKalmanEstimator.
    
    The estimated parameters are driven by ParameterDriver objects. They are of 3 different types:
    
      1.  Orbital parameters:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized. 2.  Propagation parameters: Some parameters modelling physical processes (SRP or drag coefficients etc...).
    
    They are also retrieved from the propagator builder during the initialization phase. 3.  Measurements parameters: Parameters related to measurements (station biases, positions etc...).
    
    They are passed down to the filter in its constructor.
    
    The total number of estimated parameters is m, the size of the state vector.
    
    The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus. All the variables seen by Hipparchus (states, covariances, measurement matrices...) are normalized using a specific scale for each estimated parameters or standard deviation noise for each measurement components.
    
    A KalmanEstimator object is built using the build method of a KalmanEstimatorBuilder.
    
    Since:
        9.2
    """
    def estimationStep(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> typing.MutableSequence[org.orekit.propagation.Propagator]:
        """
        Process a single measurement.
        
        Update the filter with the new measurement by calling the estimate method.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): the measurement to process
        
        Returns:
            estimated propagators
        
        
        """
        ...
    def processMeasurements(self, observedMeasurements: typing.Union[java.lang.Iterable[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Sequence[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Set[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> typing.MutableSequence[org.orekit.propagation.Propagator]:
        """
        Process several measurements.
        
        Parameters:
            observedMeasurements (Iterable<ObservedMeasurement<?>>): the measurements to process in chronologically sorted order
        
        Returns:
            estimated propagators
        
        
        """
        ...

class PythonAbstractKalmanEstimator(AbstractKalmanEstimator):
    def __init__(self, decomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], builders: java.util.List[org.orekit.propagation.conversion.PropagatorBuilder]):
        """
        Constructor.
        
        Parameters:
            decomposer (MatrixDecomposer): matrix decomposer for filter
            builders (List<? extends PropagatorBuilder> builders): list of propagator builders
        
        
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
    def getKalmanEstimation(self) -> KalmanEstimation:
        """
        Description copied from class: getKalmanEstimation Get the provider for kalman filter estimations.
        
        Specified by: getKalmanEstimation in class AbstractKalmanEstimator
        
        Returns:
            the provider for Kalman filter estimations
        
        
        """
        ...
    def getKalmanFilter(self) -> org.hipparchus.filtering.kalman.KalmanFilter[MeasurementDecorator]:
        """
        Get the Hipparchus filter.
        
        Specified by: getKalmanFilter in class AbstractKalmanEstimator
        
        Returns:
            the filter
        
        
        """
        ...
    def getScale(self) -> typing.MutableSequence[float]:
        """
        Get the parameter scaling factors.
        
        Specified by: getScale in class AbstractKalmanEstimator
        
        Returns:
            the parameters scale
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonCovarianceMatrixProvider(CovarianceMatrixProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getInitialCovarianceMatrix(self, initial: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the initial covariance matrix. Extension point for Python.
        
        The initial covariance matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the initial covariance matrix will be the output matrix of a previous run of the Kalman filter.
        
        Specified by: getInitialCovarianceMatrix in interface CovarianceMatrixProvider
        
        Parameters:
            initial (SpacecraftState): initial state state
        
        Returns:
            physical (i.e. non normalized) initial covariance matrix
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
        """
        ...
    def getProcessNoiseMatrix(self, previous: org.orekit.propagation.SpacecraftState, current: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the process noise matrix between previous and current states. Extension point for Python.
        
        The process noise matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to 0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
        Specified by: getProcessNoiseMatrix in interface CovarianceMatrixProvider
        
        Parameters:
            previous (SpacecraftState): previous state
            current (SpacecraftState): current state
        
        Returns:
            physical (i.e. non normalized) process noise matrix between previous and current states
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonKalmanEstimation(KalmanEstimation):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
        Get the estimated measurement.
        
        This estimation has been evaluated on the last corrected orbits
        
        Specified by: getCorrectedMeasurement in interface KalmanEstimation
        
        Returns:
            corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the corrected spacecraft states.
        
        Specified by: getCorrectedSpacecraftStates in interface KalmanEstimation
        
        Returns:
            corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the current date.
        
        Specified by: getCurrentDate in interface KalmanEstimation
        
        Returns:
            current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
        Get the current measurement number.
        
        Specified by: getCurrentMeasurementNumber in interface KalmanEstimation
        
        Returns:
            current measurement number
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated measurements parameters.
        
        Specified by: getEstimatedMeasurementsParameters in interface KalmanEstimation
        
        Returns:
            the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated orbital parameters.
        
        Specified by: getEstimatedOrbitalParameters in interface KalmanEstimation
        
        Returns:
            the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated propagation parameters.
        
        Specified by: getEstimatedPropagationParameters in interface KalmanEstimation
        
        Returns:
            the list of estimated propagation parameters
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the "physical" estimated covariance matrix (i.e. not normalized)
        
        Specified by: getPhysicalEstimatedCovarianceMatrix in interface KalmanEstimation
        
        Returns:
            the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
        Get the "physical" estimated state (i.e. not normalized)
        
        Specified by: getPhysicalEstimatedState in interface KalmanEstimation
        
        Returns:
            the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical innovation covariance matrix.
        
        Specified by: getPhysicalInnovationCovarianceMatrix in interface KalmanEstimation
        
        Returns:
            physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        Since:
            9.3
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical Kalman gain matrix.
        
        Specified by: getPhysicalKalmanGain in interface KalmanEstimation
        
        Returns:
            Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        Since:
            9.3
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
        Specified by: getPhysicalMeasurementJacobian in interface KalmanEstimation
        
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
        
        Specified by: getPhysicalStateTransitionMatrix in interface KalmanEstimation
        
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
        
        Specified by: getPredictedMeasurement in interface KalmanEstimation
        
        Returns:
            predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the predicted spacecraft states.
        
        Specified by: getPredictedSpacecraftStates in interface KalmanEstimation
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonKalmanObserver(KalmanObserver):
    def __init__(self): ...
    def evaluationPerformed(self, estimation: KalmanEstimation) -> None:
        """
        Notification callback after each one of a Kalman filter estimation.
        
        Specified by: evaluationPerformed in interface KalmanObserver
        
        Parameters:
            estimation (KalmanEstimation): estimation performed by Kalman estimator
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonSemiAnalyticalProcess(SemiAnalyticalProcess):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], estimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
        Description copied from interface: finalizeEstimation Finalize estimation.
        
        Specified by: finalizeEstimation in interface SemiAnalyticalProcess
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): measurement that has just been processed
            estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def finalizeOperationsObservationGrid(self) -> None:
        """
        Description copied from interface: finalizeOperationsObservationGrid Finalize estimation operations on the observation grid.
        
        Specified by: finalizeOperationsObservationGrid in interface SemiAnalyticalProcess
        
        
        """
        ...
    def getObserver(self) -> KalmanObserver:
        """
        Description copied from interface: getObserver Get the observer for Kalman Filter estimations.
        
        Specified by: getObserver in interface SemiAnalyticalProcess
        
        Returns:
            the observer for Kalman Filter estimations
        
        
        """
        ...
    def initializeShortPeriodicTerms(self, meanState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Description copied from interface: initializeShortPeriodicTerms Initialize the short periodic terms for the Kalman Filter.
        
        Specified by: initializeShortPeriodicTerms in interface SemiAnalyticalProcess
        
        Parameters:
            meanState (SpacecraftState): mean state for auxiliary elements
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def updateNominalSpacecraftState(self, nominal: org.orekit.propagation.SpacecraftState) -> None:
        """
        Description copied from interface: updateNominalSpacecraftState Update the nominal spacecraft state.
        
        Specified by: updateNominalSpacecraftState in interface SemiAnalyticalProcess
        
        Parameters:
            nominal (SpacecraftState): nominal spacecraft state
        
        
        """
        ...
    def updateShortPeriods(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Description copied from interface: updateShortPeriods Update the DSST short periodic terms.
        
        Specified by: updateShortPeriods in interface SemiAnalyticalProcess
        
        Parameters:
            state (SpacecraftState): current mean state
        
        
        """
        ...

class RtsSmoother(KalmanObserver):
    """
    Perform an RTS (Rauch-Tung-Striebel) smoothing step over results from a sequential estimator.
    
    The Kalman and Unscented sequential estimators produce a state (mean and covariance) after processing each measurement. This state is a statistical summary of all the information provided to the filter, from the measurements and model of the spacecraft motion, up until the latest measurement. A smoother produces estimates that are summaries of information over all measurements, both past and future.
    
    For example, if a filter processes measurements from time 1 to 10, then the filter state at time 5 uses measurement information up to time 5, while the smoother state at time 5 uses measurement information from the entire interval, times 1 to 10. This typically results in more accurate estimates, with more information reducing the uncertainty.
    
    This smoother is implemented using the KalmanObserver mechanism. The smoother collects data from the forward estimation over the measurements, then applies a backward pass to calculate the smoothed estimates. Smoothed estimates are collected into a list of PhysicalEstimatedState, containing a timestamp, mean and covariance over all estimated parameters (orbital, propagation and measurement). The order of the parameters in these states is the same as the underlying sequential estimator, for example from a call to getPhysicalEstimatedState.
    
    The smoother is compatible with the Kalman and Unscented sequential estimators, but does not support the semi-analytical equivalents.
    
    The following code snippet demonstrates how to attach the smoother to a filter and retrieve smoothed states:
    
    
         // Build the Kalman filter
         final KalmanEstimator kalmanEstimator = new KalmanEstimatorBuilder().
             addPropagationConfiguration(propagatorBuilder, new ConstantProcessNoise(initialP, Q)).
             build();
    
         // Add smoother observer to filter
         final RtsSmoother rtsSmoother = new RtsSmoother(kalmanEstimator);
         kalmanEstimator.setObserver(rtsSmoother);
    
         // Perform forward filtering over the measurements
         Propagator[] estimated = kalmanEstimator.processMeasurements(measurements);
    
         // Perform backwards smoothing and collect the results
         rtsSmoother.backwardsSmooth();
     
    
    Note that the smoother stores data from every filter step, leading to high memory usage for long-duration runs with numerous measurements.
    
    Since:
        13.0
    
    Also see:
        KalmanEstimatorBuilder,
        UnscentedKalmanEstimatorBuilder, "Särkkä S. Bayesian Filtering and
        Smoothing. Cambridge University Press, 2013."
    """
    def __init__(self, estimator: AbstractKalmanEstimator):
        """
        Smoother observer constructor from a sequential estimator. This smoother constructor requires access to the underlying estimator to initialise some information not available from KalmanEstimation during init, including the estimated parameters drivers (orbital, propagation and measurements).
        
        Parameters:
            estimator (AbstractKalmanEstimator): the Kalman estimator
        
        
        """
        ...
    def backwardsSmooth(self) -> java.util.List[PhysicalEstimatedState]:
        """
        Perform a RTS backwards smoothing recursion over the filtered states collected by the observer.
        
        Returns:
            a list of PhysicalEstimatedState
        
        
        """
        ...
    def evaluationPerformed(self, estimation: KalmanEstimation) -> None:
        """
        Notification callback after each one of a Kalman filter estimation. This accumulates the filter states as the sequential estimator processes measurements.
        
        Specified by: evaluationPerformed in interface KalmanObserver
        
        Parameters:
            estimation (KalmanEstimation): estimation performed by Kalman estimator
        
        
        """
        ...
    def init(self, estimation: KalmanEstimation) -> None:
        """
        Initialise the observer on the initial state of the filter, before processing the first measurement.
        
        Specified by: init in interface KalmanObserver
        
        Parameters:
            estimation (KalmanEstimation): estimation performed by Kalman estimator
        
        
        """
        ...

class SemiAnalyticalKalmanEstimator(AbstractKalmanEstimator):
    """
    Implementation of an Extended Semi-analytical Kalman Filter (ESKF) to perform orbit determination.
    
    The filter uses a DSSTPropagatorBuilder.
    
    The estimated parameters are driven by ParameterDriver objects. They are of 3 different types:
    
      1.  Orbital parameters:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized. 2.  Propagation parameters: Some parameters modelling physical processes (SRP or drag coefficients).
    
    They are also retrieved from the propagator builder during the initialization phase. 3.  Measurements parameters: Parameters related to measurements (station biases, positions etc...).
    
    They are passed down to the filter in its constructor.
    
    The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus. All the variables seen by Hipparchus (states, covariances, measurement matrices...) are normalized using a specific scale for each estimated parameters or standard deviation noise for each measurement components.
    
    Since:
        11.1
    
    Also see:
        "Folcik Z., Orbit Determination Using Modern Filters/Smoothers and Continuous Thrust Modeling, Master of Science Thesis,
        Department of Aeronautics and Astronautics, MIT, June, 2008.", "Cazabonne B., Bayard J., Journot M., and Cefola P. J., A
        Semi-analytical Approach for Orbit Determination based on Extended Kalman Filter, AAS Paper 21-614, AAS/AIAA
        Astrodynamics Specialist Conference, Big Sky, August 2021."
    """
    def __init__(self, decomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], propagatorBuilder: org.orekit.propagation.conversion.DSSTPropagatorBuilder, covarianceMatrixProvider: CovarianceMatrixProvider, estimatedMeasurementParameters: org.orekit.utils.ParameterDriversList, measurementProcessNoiseMatrix: CovarianceMatrixProvider):
        """
        Kalman filter estimator constructor (package private).
        
        Parameters:
            decomposer (MatrixDecomposer): decomposer to use for the correction phase
            propagatorBuilder (DSSTPropagatorBuilder): propagator builder used to evaluate the orbit.
            covarianceMatrixProvider (CovarianceMatrixProvider): provider for process noise matrix
            estimatedMeasurementParameters (ParameterDriversList): measurement parameters to estimate
            measurementProcessNoiseMatrix (CovarianceMatrixProvider): provider for measurement process noise matrix
        
        
        """
        ...
    def getObserver(self) -> KalmanObserver:
        """
        Get the observer..
        
        Overrides: getObserver in class AbstractKalmanEstimator
        
        Returns:
            the observer
        
        
        """
        ...
    def processMeasurements(self, observedMeasurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
        Process a single measurement.
        
        Update the filter with the new measurement by calling the estimate method.
        
        Parameters:
            observedMeasurements (List<ObservedMeasurement<?>>): the list of measurements to process
        
        Returns:
            estimated propagators
        
        
        """
        ...
    def setObserver(self, observer: typing.Union[KalmanObserver, typing.Callable]) -> None:
        """
        Set the observer..
        
        Overrides: setObserver in class AbstractKalmanEstimator
        
        Parameters:
            observer (KalmanObserver): the observer
        
        
        """
        ...

class SemiAnalyticalKalmanModel(KalmanEstimation, org.hipparchus.filtering.kalman.extended.NonLinearProcess[MeasurementDecorator], SemiAnalyticalProcess):
    """
    Process model to use with a SemiAnalyticalKalmanEstimator.
    
    Since:
        11.1
    
    Also see:
        "Folcik Z., Orbit Determination Using Modern Filters/Smoothers and Continuous Thrust Modeling, Master of Science Thesis,
        Department of Aeronautics and Astronautics, MIT, June, 2008.", "Cazabonne B., Bayard J., Journot M., and Cefola P. J., A
        Semi-analytical Approach for Orbit Determination based on Extended Kalman Filter, AAS Paper 21-614, AAS/AIAA
        Astrodynamics Specialist Conference, Big Sky, August 2021."
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], estimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
        Finalize estimation.
        
        Specified by: finalizeEstimation in interface SemiAnalyticalProcess
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): measurement that has just been processed
            estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def finalizeOperationsObservationGrid(self) -> None:
        """
        Finalize estimation operations on the observation grid.
        
        Specified by: finalizeOperationsObservationGrid in interface SemiAnalyticalProcess
        
        
        """
        ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
        Get the estimated measurement.
        
        This estimation has been evaluated on the last corrected orbits
        
        Specified by: getCorrectedMeasurement in interface KalmanEstimation
        
        Returns:
            corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the corrected spacecraft states.
        
        Specified by: getCorrectedSpacecraftStates in interface KalmanEstimation
        
        Returns:
            corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the current date.
        
        Specified by: getCurrentDate in interface KalmanEstimation
        
        Returns:
            current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
        Get the current measurement number.
        
        Specified by: getCurrentMeasurementNumber in interface KalmanEstimation
        
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
        
        Specified by: getEstimatedMeasurementsParameters in interface KalmanEstimation
        
        Returns:
            the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated orbital parameters.
        
        Specified by: getEstimatedOrbitalParameters in interface KalmanEstimation
        
        Returns:
            the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated propagation parameters.
        
        Specified by: getEstimatedPropagationParameters in interface KalmanEstimation
        
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
    def getEvolution(self, previousTime: float, previousState: org.hipparchus.linear.RealVector, measurement: MeasurementDecorator) -> org.hipparchus.filtering.kalman.extended.NonLinearEvolution:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.extended.NonLinearProcess.html?is` in interface NonLinearProcess
        
        
        """
        ...
    def getInnovation(self, measurement: MeasurementDecorator, evolution: org.hipparchus.filtering.kalman.extended.NonLinearEvolution, innovationCovarianceMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.extended.NonLinearProcess.html?is` in interface NonLinearProcess
        
        
        """
        ...
    def getObserver(self) -> KalmanObserver:
        """
        Get the observer for Kalman Filter estimations.
        
        Specified by: getObserver in interface SemiAnalyticalProcess
        
        Returns:
            the observer for Kalman Filter estimations
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the "physical" estimated covariance matrix (i.e. not normalized)
        
        Specified by: getPhysicalEstimatedCovarianceMatrix in interface KalmanEstimation
        
        Returns:
            the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
        Get the "physical" estimated state (i.e. not normalized)
        
        Specified by: getPhysicalEstimatedState in interface KalmanEstimation
        
        Returns:
            the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical innovation covariance matrix.
        
        Specified by: getPhysicalInnovationCovarianceMatrix in interface KalmanEstimation
        
        Returns:
            physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical Kalman gain matrix.
        
        Specified by: getPhysicalKalmanGain in interface KalmanEstimation
        
        Returns:
            Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
        Specified by: getPhysicalMeasurementJacobian in interface KalmanEstimation
        
        Returns:
            physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
            measurement has been ignored)
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
        Specified by: getPhysicalStateTransitionMatrix in interface KalmanEstimation
        
        Returns:
            state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
            process estimate)
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
        Get the predicted measurement.
        
        This estimation has been evaluated on the last predicted orbits
        
        Specified by: getPredictedMeasurement in interface KalmanEstimation
        
        Returns:
            predicted measurement
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the predicted spacecraft states.
        
        Specified by: getPredictedSpacecraftStates in interface KalmanEstimation
        
        Returns:
            predicted spacecraft states
        
        
        """
        ...
    def initializeShortPeriodicTerms(self, meanState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Initialize the short periodic terms for the Kalman Filter.
        
        Specified by: initializeShortPeriodicTerms in interface SemiAnalyticalProcess
        
        Parameters:
            meanState (SpacecraftState): mean state for auxiliary elements
        
        
        """
        ...
    def processMeasurements(self, observedMeasurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], filter: org.hipparchus.filtering.kalman.extended.ExtendedKalmanFilter[MeasurementDecorator]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
        Process a single measurement.
        
        Update the filter with the new measurements.
        
        Parameters:
            observedMeasurements (List<ObservedMeasurement<?>>): the list of measurements to process
            filter (ExtendedKalmanFilter<MeasurementDecorator> filter): Extended Kalman Filter
        
        Returns:
            estimated propagator
        
        
        """
        ...
    def setObserver(self, observer: typing.Union[KalmanObserver, typing.Callable]) -> None:
        """
        Set the observer.
        
        Parameters:
            observer (KalmanObserver): the observer
        
        
        """
        ...
    def updateNominalSpacecraftState(self, nominal: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the nominal spacecraft state.
        
        Specified by: updateNominalSpacecraftState in interface SemiAnalyticalProcess
        
        Parameters:
            nominal (SpacecraftState): nominal spacecraft state
        
        
        """
        ...
    def updateReferenceTrajectory(self, propagator: org.orekit.propagation.semianalytical.dsst.DSSTPropagator) -> None:
        """
        Update the reference trajectories using the propagator as input.
        
        Parameters:
            propagator (DSSTPropagator): The new propagator to use
        
        
        """
        ...
    def updateShortPeriods(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the DSST short periodic terms.
        
        Specified by: updateShortPeriods in interface SemiAnalyticalProcess
        
        Parameters:
            state (SpacecraftState): current mean state
        
        
        """
        ...

class SemiAnalyticalUnscentedKalmanEstimator(AbstractKalmanEstimator):
    """
    Implementation of an Unscented Semi-analytical Kalman filter (USKF) to perform orbit determination.
    
    The filter uses a DSSTPropagatorBuilder.
    
    The estimated parameters are driven by ParameterDriver objects. They are of 3 different types:
    
      1.  Orbital parameters:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized. 2.  Propagation parameters: Some parameters modeling physical processes (SRP or drag coefficients etc...).
    
    They are also retrieved from the propagator builder during the initialization phase. 3.  Measurements parameters: Parameters related to measurements (station biases, positions etc...).
    
    They are passed down to the filter in its constructor.
    
    The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus. All the variables seen by Hipparchus (states, covariances...) are normalized using a specific scale for each estimated parameters or standard deviation noise for each measurement components.
    
    An SemiAnalyticalUnscentedKalmanEstimator object is built using the build method of a SemiAnalyticalUnscentedKalmanEstimatorBuilder.
    
    Since:
        11.3
    """
    def getObserver(self) -> KalmanObserver:
        """
        Get the observer..
        
        Overrides: getObserver in class AbstractKalmanEstimator
        
        Returns:
            the observer
        
        
        """
        ...
    def processMeasurements(self, observedMeasurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
        Process a single measurement.
        
        Update the filter with the new measurement by calling the estimate method.
        
        Parameters:
            observedMeasurements (List<ObservedMeasurement<?>>): the list of measurements to process
        
        Returns:
            estimated propagators
        
        
        """
        ...
    def setObserver(self, observer: typing.Union[KalmanObserver, typing.Callable]) -> None:
        """
        Set the observer..
        
        Overrides: setObserver in class AbstractKalmanEstimator
        
        Parameters:
            observer (KalmanObserver): the observer
        
        
        """
        ...

class SemiAnalyticalUnscentedKalmanModel(KalmanEstimation, org.hipparchus.filtering.kalman.unscented.UnscentedProcess[MeasurementDecorator], SemiAnalyticalProcess):
    """
    Class defining the process model dynamics to use with a SemiAnalyticalUnscentedKalmanEstimator.
    
    Since:
        11.3
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], estimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
        Finalize estimation.
        
        Specified by: finalizeEstimation in interface SemiAnalyticalProcess
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): measurement that has just been processed
            estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def finalizeOperationsObservationGrid(self) -> None:
        """
        Finalize estimation operations on the observation grid.
        
        Specified by: finalizeOperationsObservationGrid in interface SemiAnalyticalProcess
        
        
        """
        ...
    def getCorrectedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
        Get the estimated measurement.
        
        This estimation has been evaluated on the last corrected orbits
        
        Specified by: getCorrectedMeasurement in interface KalmanEstimation
        
        Returns:
            corrected measurement
        
        
        """
        ...
    def getCorrectedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the corrected spacecraft states.
        
        Corrected state is osculating.
        
        Specified by: getCorrectedSpacecraftStates in interface KalmanEstimation
        
        Returns:
            corrected spacecraft states
        
        
        """
        ...
    def getCurrentDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the current date.
        
        Specified by: getCurrentDate in interface KalmanEstimation
        
        Returns:
            current date
        
        
        """
        ...
    def getCurrentMeasurementNumber(self) -> int:
        """
        Get the current measurement number.
        
        Specified by: getCurrentMeasurementNumber in interface KalmanEstimation
        
        Returns:
            current measurement number
        
        
        """
        ...
    def getEstimate(self) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
        Get the current corrected estimate.
        
        For the Unscented Semi-analytical Kalman Filter it corresponds to the corrected filter correction. In other words, it doesn't represent an orbital state.
        
        Returns:
            current corrected estimate
        
        
        """
        ...
    def getEstimatedMeasurementsParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated measurements parameters.
        
        Specified by: getEstimatedMeasurementsParameters in interface KalmanEstimation
        
        Returns:
            the list of estimated measurements parameters
        
        
        """
        ...
    def getEstimatedOrbitalParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated orbital parameters.
        
        Specified by: getEstimatedOrbitalParameters in interface KalmanEstimation
        
        Returns:
            the list of estimated orbital parameters
        
        
        """
        ...
    def getEstimatedPropagationParameters(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the list of estimated propagation parameters.
        
        Specified by: getEstimatedPropagationParameters in interface KalmanEstimation
        
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
    def getEvolution(self, previousTime: float, sigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray], measurement: MeasurementDecorator) -> org.hipparchus.filtering.kalman.unscented.UnscentedEvolution:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
        """
        ...
    def getInnovation(self, measurement: MeasurementDecorator, predictedMeas: org.hipparchus.linear.RealVector, predictedState: org.hipparchus.linear.RealVector, innovationCovarianceMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
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
        
        Specified by: getObserver in interface SemiAnalyticalProcess
        
        Returns:
            the observer for Kalman Filter estimations
        
        
        """
        ...
    def getPhysicalEstimatedCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the "physical" estimated covariance matrix (i.e. not normalized)
        
        Specified by: getPhysicalEstimatedCovarianceMatrix in interface KalmanEstimation
        
        Returns:
            the "physical" estimated covariance matrix
        
        
        """
        ...
    def getPhysicalEstimatedState(self) -> org.hipparchus.linear.RealVector:
        """
        Get the "physical" estimated state (i.e. not normalized)
        
        Specified by: getPhysicalEstimatedState in interface KalmanEstimation
        
        Returns:
            the "physical" estimated state
        
        
        """
        ...
    def getPhysicalInnovationCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical innovation covariance matrix.
        
        Specified by: getPhysicalInnovationCovarianceMatrix in interface KalmanEstimation
        
        Returns:
            physical innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical Kalman gain matrix.
        
        Specified by: getPhysicalKalmanGain in interface KalmanEstimation
        
        Returns:
            Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
        
        """
        ...
    def getPhysicalMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the physical Jacobian of the measurement with respect to the state (H matrix).
        
        Specified by: getPhysicalMeasurementJacobian in interface KalmanEstimation
        
        Returns:
            physical Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the
            measurement has been ignored)
        
        
        """
        ...
    def getPhysicalStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get physical state transition matrix between previous state and estimated (but not yet corrected) state.
        
        Specified by: getPhysicalStateTransitionMatrix in interface KalmanEstimation
        
        Returns:
            state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
            process estimate)
        
        
        """
        ...
    def getPredictedMeasurement(self) -> org.orekit.estimation.measurements.EstimatedMeasurement[typing.Any]:
        """
        Get the predicted measurement.
        
        This estimation has been evaluated on the last predicted orbits
        
        Specified by: getPredictedMeasurement in interface KalmanEstimation
        
        Returns:
            predicted measurement
        
        
        """
        ...
    def getPredictedMeasurements(self, predictedSigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray], measurement: MeasurementDecorator) -> typing.MutableSequence[org.hipparchus.linear.RealVector]:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
        """
        ...
    def getPredictedSpacecraftStates(self) -> typing.MutableSequence[org.orekit.propagation.SpacecraftState]:
        """
        Get the predicted spacecraft states.
        
        Predicted state is osculating.
        
        Specified by: getPredictedSpacecraftStates in interface KalmanEstimation
        
        Returns:
            predicted spacecraft states
        
        
        """
        ...
    def getProcessNoiseMatrix(self, previousTime: float, predictedState: org.hipparchus.linear.RealVector, measurement: MeasurementDecorator) -> org.hipparchus.linear.RealMatrix:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
        """
        ...
    def initializeShortPeriodicTerms(self, meanState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Initialize the short periodic terms for the Kalman Filter.
        
        Specified by: initializeShortPeriodicTerms in interface SemiAnalyticalProcess
        
        Parameters:
            meanState (SpacecraftState): mean state for auxiliary elements
        
        
        """
        ...
    def processMeasurements(self, observedMeasurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], filter: org.hipparchus.filtering.kalman.unscented.UnscentedKalmanFilter[MeasurementDecorator]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
        Process measurements.
        
        Parameters:
            observedMeasurements (List<ObservedMeasurement<?>>): the list of measurements to process
            filter (UnscentedKalmanFilter<MeasurementDecorator> filter): Unscented Kalman Filter
        
        Returns:
            estimated propagator
        
        
        """
        ...
    def setObserver(self, observer: typing.Union[KalmanObserver, typing.Callable]) -> None:
        """
        Set the observer.
        
        Parameters:
            observer (KalmanObserver): the observer
        
        
        """
        ...
    def updateNominalSpacecraftState(self, nominal: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the nominal spacecraft state.
        
        Specified by: updateNominalSpacecraftState in interface SemiAnalyticalProcess
        
        Parameters:
            nominal (SpacecraftState): nominal spacecraft state
        
        
        """
        ...
    def updateShortPeriods(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the DSST short periodic terms.
        
        Specified by: updateShortPeriods in interface SemiAnalyticalProcess
        
        Parameters:
            state (SpacecraftState): current mean state
        
        
        """
        ...

class UnscentedKalmanEstimator(AbstractKalmanEstimator):
    """
    Implementation of an Unscented Kalman filter to perform orbit determination.
    
    The filter uses a PropagatorBuilder to initialize its reference trajectory.
    
    The estimated parameters are driven by ParameterDriver objects. They are of 3 different types:
    
      1.  Orbital parameters:The position and velocity of the spacecraft, or, more generally, its orbit.
    
    These parameters are retrieved from the reference trajectory propagator builder when the filter is initialized. 2.  Propagation parameters: Some parameters modelling physical processes (SRP or drag coefficients etc...).
    
    They are also retrieved from the propagator builder during the initialization phase. 3.  Measurements parameters: Parameters related to measurements (station biases, positions etc...).
    
    They are passed down to the filter in its constructor.
    
    The total number of estimated parameters is m, the size of the state vector.
    
    The Kalman filter implementation used is provided by the underlying mathematical library Hipparchus.
    
    An UnscentedKalmanEstimator object is built using the build method of a UnscentedKalmanEstimatorBuilder. The builder is generalized to accept any PropagatorBuilder. Howerver, it is absolutely not recommended to use a DSSTPropagatorBuilder. A specific SemiAnalyticalUnscentedKalmanEstimatorBuilder is implemented and shall be used.
    
    Since:
        11.3
    """
    def estimationStep(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> typing.MutableSequence[org.orekit.propagation.Propagator]:
        """
        Process a single measurement.
        
        Update the filter with the new measurement by calling the estimate method.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): the measurement to process
        
        Returns:
            estimated propagator
        
        
        """
        ...
    def processMeasurements(self, observedMeasurements: typing.Union[java.lang.Iterable[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Sequence[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Set[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> typing.MutableSequence[org.orekit.propagation.Propagator]:
        """
        Process several measurements.
        
        Parameters:
            observedMeasurements (Iterable<ObservedMeasurement<?>>): the measurements to process in chronologically sorted order
        
        Returns:
            estimated propagator
        
        
        """
        ...

class ConstantProcessNoise(AbstractCovarianceMatrixProvider):
    """
    Provider for constant process noise matrices.
    
    This class always provides one initial noise matrix and one constant process noise matrix (both can be identical), regardless of states.
    
    Since:
        9.2
    """
    @typing.overload
    def __init__(self, processNoiseMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, initialNoiseMatrix: org.hipparchus.linear.RealMatrix, processNoiseMatrix: org.hipparchus.linear.RealMatrix): ...
    def getProcessNoiseMatrix(self, previous: org.orekit.propagation.SpacecraftState, current: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the process noise matrix between previous and current states.
        
        The process noise matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to 0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
        Parameters:
            previous (SpacecraftState): previous state
            current (SpacecraftState): current state
        
        Returns:
            physical (i.e. non normalized) process noise matrix between previous and current states
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
        """
        ...

class PythonAbstractCovarianceMatrixProvider(AbstractCovarianceMatrixProvider):
    def __init__(self, initialNoiseMatrix: org.hipparchus.linear.RealMatrix):
        """
        Simple constructor.
        
        Parameters:
            initialNoiseMatrix (RealMatrix): initial process noise
        
        
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
    def getProcessNoiseMatrix(self, previous: org.orekit.propagation.SpacecraftState, current: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the process noise matrix between previous and current states. Extension point for Python.
        
        The process noise matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to 0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
        Parameters:
            previous (SpacecraftState): previous state
            current (SpacecraftState): current state
        
        Returns:
            physical (i.e. non normalized) process noise matrix between previous and current states
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class UnivariateProcessNoise(AbstractCovarianceMatrixProvider):
    """
    Provider for a temporal evolution of the process noise matrix. All parameters (orbital or propagation) are time dependent and provided as UnivariateFunction. The argument of the functions is a duration in seconds (between current and previous spacecraft state). The output of the functions must be of the dimension of a standard deviation. The method getProcessNoiseMatrix then square the values so that they are consistent with a covariance matrix.
    
    The orbital parameters evolutions are provided in LOF frame and Cartesian (PV); then converted in inertial frame and current OrbitType and PositionAngleType when method getProcessNoiseMatrix is called.
    
    The time-dependent functions define a process noise matrix that is diagonal in the Local Orbital Frame, corresponds to Cartesian elements, abd represents the temporal evolution of (the standard deviation of) the process noise model. The first function is therefore the standard deviation along the LOF X axis, the second function represents the standard deviation along the LOF Y axis... This allows to set up simply a process noise representing an uncertainty that grows mainly along the track. The 6x6 upper left part of output matrix will however not be diagonal as it will be converted to the same inertial frame and orbit type as the SpacecraftState used by the KalmanEstimator.
    
    The propagation and measurements parameters are not associated to a specific frame and are appended as is in the lower right part diagonal of the output matrix. This implies this simplified model does not include correlation between the parameters and the orbit, but only evolution of the parameters themselves. If such correlations are needed, users must set up a custom CovarianceMatrixProvider. In most cases, the parameters are constant and their evolution noise is always 0, so the functions can be set to x -> 0.
    
    This class always provides one initial noise matrix or initial covariance matrix and one process noise matrix.
    
    Since:
        9.2
    """
    @typing.overload
    def __init__(self, initialCovarianceMatrix: org.hipparchus.linear.RealMatrix, lofType: org.orekit.frames.LOFType, positionAngleType: org.orekit.orbits.PositionAngleType, lofCartesianOrbitalParametersEvolution: typing.Union[typing.List[org.hipparchus.analysis.UnivariateFunction], jpype.JArray], propagationParametersEvolution: typing.Union[typing.List[org.hipparchus.analysis.UnivariateFunction], jpype.JArray]): ...
    @typing.overload
    def __init__(self, initialCovarianceMatrix: org.hipparchus.linear.RealMatrix, lofType: org.orekit.frames.LOFType, positionAngleType: org.orekit.orbits.PositionAngleType, lofCartesianOrbitalParametersEvolution: typing.Union[typing.List[org.hipparchus.analysis.UnivariateFunction], jpype.JArray], propagationParametersEvolution: typing.Union[typing.List[org.hipparchus.analysis.UnivariateFunction], jpype.JArray], measurementsParametersEvolution: typing.Union[typing.List[org.hipparchus.analysis.UnivariateFunction], jpype.JArray]): ...
    def getLofCartesianOrbitalParametersEvolution(self) -> typing.MutableSequence[org.hipparchus.analysis.UnivariateFunction]:
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
    def getMeasurementsParametersEvolution(self) -> typing.MutableSequence[org.hipparchus.analysis.UnivariateFunction]:
        """
        Getter for the measurementsParametersEvolution.
        
        Returns:
            the measurementsParametersEvolution
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Getter for the positionAngle.
        
        Returns:
            the positionAngle
        
        
        """
        ...
    def getProcessNoiseMatrix(self, previous: org.orekit.propagation.SpacecraftState, current: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the process noise matrix between previous and current states.
        
        The process noise matrix is a covariance matrix corresponding to the parameters managed by the KalmanEstimator. The number of rows/columns and their order are as follows:
        
          - The first 6 components correspond to the 6 orbital parameters of the associated propagator. All 6 parameters must always
            be present, regardless of the fact they are estimated or not.
          - The following components correspond to the subset of propagation parameters of the associated propagator that are
            estimated.
          - The remaining components correspond to the subset of measurements parameters that are estimated, considering all
            measurements, even the ones that correspond to spacecrafts not related to the associated propagator
        
        In most cases, the process noise for the part corresponding to measurements (the final rows and columns) will be set to 0 for the process noise corresponding to the evolution between a non-null previous and current state.
        
        Parameters:
            previous (SpacecraftState): previous state
            current (SpacecraftState): current state
        
        Returns:
            physical (i.e. non normalized) process noise matrix between previous and current states
        
        Also see:
            getOrbitalParametersDrivers,
            getPropagationParametersDrivers
        
        
        """
        ...
    def getPropagationParametersEvolution(self) -> typing.MutableSequence[org.hipparchus.analysis.UnivariateFunction]:
        """
        Getter for the propagationParametersEvolution.
        
        Returns:
            the propagationParametersEvolution
        
        
        """
        ...

class KalmanModel(org.orekit.estimation.sequential.AbstractKalmanEstimationCommon, org.hipparchus.filtering.kalman.extended.NonLinearProcess[MeasurementDecorator]):
    """
    Class defining the process model dynamics to use with a KalmanEstimator.
    
    Since:
        9.2
    """
    def __init__(self, propagatorBuilders: java.util.List[org.orekit.propagation.conversion.PropagatorBuilder], covarianceMatricesProviders: java.util.List[CovarianceMatrixProvider], estimatedMeasurementParameters: org.orekit.utils.ParameterDriversList, measurementProcessNoiseMatrix: CovarianceMatrixProvider):
        """
        Kalman process model constructor.
        
        Parameters:
            propagatorBuilders (List<PropagatorBuilder> propagatorBuilders): propagators builders used to evaluate the orbits.
            covarianceMatricesProviders (List<CovarianceMatrixProvider> covarianceMatricesProviders): providers for covariance matrices
            estimatedMeasurementParameters (ParameterDriversList): measurement parameters to estimate
            measurementProcessNoiseMatrix (CovarianceMatrixProvider): provider for measurement process noise matrix
        
        
        """
        ...
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], estimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
        Finalize estimation.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): measurement that has just been processed
            estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def getEvolution(self, previousTime: float, previousState: org.hipparchus.linear.RealVector, measurement: MeasurementDecorator) -> org.hipparchus.filtering.kalman.extended.NonLinearEvolution:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.extended.NonLinearProcess.html?is` in interface NonLinearProcess
        
        
        """
        ...
    def getInnovation(self, measurement: MeasurementDecorator, evolution: org.hipparchus.filtering.kalman.extended.NonLinearEvolution, innovationCovarianceMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.extended.NonLinearProcess.html?is` in interface NonLinearProcess
        
        
        """
        ...
    def getReferenceTrajectories(self) -> typing.MutableSequence[org.orekit.propagation.Propagator]:
        """
        Getter for the reference trajectories.
        
        Returns:
            the referencetrajectories
        
        
        """
        ...
    def setReferenceTrajectories(self, referenceTrajectories: typing.Union[typing.List[org.orekit.propagation.Propagator], jpype.JArray]) -> None:
        """
        Setter for the reference trajectories.
        
        Parameters:
            referenceTrajectories (Propagator[]): the reference trajectories to be setted
        
        
        """
        ...

class UnscentedKalmanModel(org.orekit.estimation.sequential.AbstractKalmanEstimationCommon, org.hipparchus.filtering.kalman.unscented.UnscentedProcess[MeasurementDecorator]):
    """
    Class defining the process model dynamics to use with a UnscentedKalmanEstimator.
    
    Since:
        11.3
    """
    def finalizeEstimation(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any], estimate: org.hipparchus.filtering.kalman.ProcessEstimate) -> None:
        """
        Finalize estimation.
        
        Parameters:
            observedMeasurement (ObservedMeasurement<?> observedMeasurement): measurement that has just been processed
            estimate (ProcessEstimate): corrected estimate
        
        
        """
        ...
    def getEvolution(self, previousTime: float, sigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray], measurement: MeasurementDecorator) -> org.hipparchus.filtering.kalman.unscented.UnscentedEvolution:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
        """
        ...
    def getInnovation(self, measurement: MeasurementDecorator, predictedMeas: org.hipparchus.linear.RealVector, predictedState: org.hipparchus.linear.RealVector, innovationCovarianceMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
        """
        ...
    def getPredictedMeasurements(self, predictedSigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray], measurement: MeasurementDecorator) -> typing.MutableSequence[org.hipparchus.linear.RealVector]:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
        """
        ...
    def getProcessNoiseMatrix(self, previousTime: float, predictedState: org.hipparchus.linear.RealVector, measurement: MeasurementDecorator) -> org.hipparchus.linear.RealMatrix:
        """
        Specified by: meth:`~org.orekit.estimation.sequential.https:.www.hipparchus.org.apidocs.org.hipparchus.filtering.kalman.unscented.UnscentedProcess.html?is` in interface UnscentedProcess
        
        
        """
        ...

class AbstractKalmanEstimationCommon: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.sequential")``.

    AbstractCovarianceMatrixProvider: typing.Type[AbstractCovarianceMatrixProvider]
    AbstractKalmanEstimationCommon: typing.Type[AbstractKalmanEstimationCommon]
    AbstractKalmanEstimator: typing.Type[AbstractKalmanEstimator]
    ConstantProcessNoise: typing.Type[ConstantProcessNoise]
    CovarianceMatrixProvider: typing.Type[CovarianceMatrixProvider]
    KalmanEstimation: typing.Type[KalmanEstimation]
    KalmanEstimator: typing.Type[KalmanEstimator]
    KalmanEstimatorBuilder: typing.Type[KalmanEstimatorBuilder]
    KalmanEstimatorUtil: typing.Type[KalmanEstimatorUtil]
    KalmanModel: typing.Type[KalmanModel]
    KalmanObserver: typing.Type[KalmanObserver]
    MeasurementDecorator: typing.Type[MeasurementDecorator]
    PhysicalEstimatedState: typing.Type[PhysicalEstimatedState]
    PythonAbstractCovarianceMatrixProvider: typing.Type[PythonAbstractCovarianceMatrixProvider]
    PythonAbstractKalmanEstimator: typing.Type[PythonAbstractKalmanEstimator]
    PythonCovarianceMatrixProvider: typing.Type[PythonCovarianceMatrixProvider]
    PythonKalmanEstimation: typing.Type[PythonKalmanEstimation]
    PythonKalmanObserver: typing.Type[PythonKalmanObserver]
    PythonSemiAnalyticalProcess: typing.Type[PythonSemiAnalyticalProcess]
    RtsSmoother: typing.Type[RtsSmoother]
    SemiAnalyticalKalmanEstimator: typing.Type[SemiAnalyticalKalmanEstimator]
    SemiAnalyticalKalmanEstimatorBuilder: typing.Type[SemiAnalyticalKalmanEstimatorBuilder]
    SemiAnalyticalKalmanModel: typing.Type[SemiAnalyticalKalmanModel]
    SemiAnalyticalMeasurementHandler: typing.Type[SemiAnalyticalMeasurementHandler]
    SemiAnalyticalProcess: typing.Type[SemiAnalyticalProcess]
    SemiAnalyticalUnscentedKalmanEstimator: typing.Type[SemiAnalyticalUnscentedKalmanEstimator]
    SemiAnalyticalUnscentedKalmanEstimatorBuilder: typing.Type[SemiAnalyticalUnscentedKalmanEstimatorBuilder]
    SemiAnalyticalUnscentedKalmanModel: typing.Type[SemiAnalyticalUnscentedKalmanModel]
    UnivariateProcessNoise: typing.Type[UnivariateProcessNoise]
    UnscentedKalmanEstimator: typing.Type[UnscentedKalmanEstimator]
    UnscentedKalmanEstimatorBuilder: typing.Type[UnscentedKalmanEstimatorBuilder]
    UnscentedKalmanModel: typing.Type[UnscentedKalmanModel]
