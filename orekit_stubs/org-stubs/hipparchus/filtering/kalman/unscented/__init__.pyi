
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus.filtering.kalman
import org.hipparchus.linear
import org.hipparchus.util
import typing



class UnscentedEvolution:
    """
    Container for UnscentedProcess evolution data.
    
    Since:
        2.2
    
          - UnscentedProcess
    """
    def __init__(self, currentTime: float, currentStates: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray]):
        """
        Constructor.
        
        Parameters:
            currentTime (double): current time
            currentStates (hipparchus[]): state vectors at current time
        
        
        """
        ...
    def getCurrentStates(self) -> typing.MutableSequence[org.hipparchus.linear.RealVector]:
        """
        Get current states.
        
        Returns:
            current states
        
        
        """
        ...
    def getCurrentTime(self) -> float:
        """
        Get current time.
        
        Returns:
            current time
        
        
        """
        ...

_UnscentedKalmanFilter__T = typing.TypeVar('_UnscentedKalmanFilter__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class UnscentedKalmanFilter(org.hipparchus.filtering.kalman.KalmanFilter[_UnscentedKalmanFilter__T], typing.Generic[_UnscentedKalmanFilter__T]):
    """
    implements KalmanFilter<T>
    
    Unscented Kalman filter for UnscentedProcess.
    
    Since:
        2.2
    
          - "Wan, E. A., & Van Der Merwe, R. (2000, October). The unscented Kalman filter for nonlinear estimation. In Proceedings
            of the IEEE 2000 Adaptive Systems for Signal Processing, Communications, and Control Symposium (Cat. No. 00EX373) (pp.
            153-158)"
    """
    def __init__(self, decomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], process: 'UnscentedProcess'[_UnscentedKalmanFilter__T], initialState: org.hipparchus.filtering.kalman.ProcessEstimate, utProvider: org.hipparchus.util.UnscentedTransformProvider):
        """
        Simple constructor.
        
        Parameters:
            decomposer (hipparchus): decomposer to use for the correction phase
            process (UnscentedProcess<UnscentedKalmanFilter> process): unscented process to estimate
            initialState (ProcessEstimate): initial state
            utProvider (hipparchus): unscented transform provider
        
        
        """
        ...
    def estimationStep(self, measurement: _UnscentedKalmanFilter__T) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
        Perform one estimation step.
        
        Specified by: estimationStep in interface KalmanFilter
        
        Parameters:
            measurement (UnscentedKalmanFilter): single measurement to handle
        
        Returns:
            estimated state after measurement has been considered
        
        Raises:
            hipparchus: if estimation fails
        
        
        """
        ...
    def getCorrected(self) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
        Get the corrected state.
        
        Specified by: getCorrected in interface KalmanEstimate
        
        Returns:
            corrected state
        
        
        """
        ...
    def getPredicted(self) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
        Get the predicted state.
        
        Specified by: getPredicted in interface KalmanEstimate
        
        Returns:
            predicted state
        
        
        """
        ...
    def getStateCrossCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the cross-covariance between the previous state and the prediction. Not required for forward filtering, but required for the smoother.
        
        Specified by: getStateCrossCovariance in interface KalmanEstimate
        
        Returns:
            cross-covariance
        
        
        """
        ...
    def getUnscentedTransformProvider(self) -> org.hipparchus.util.UnscentedTransformProvider:
        """
        Get the unscented transform provider.
        
        Returns:
            unscented transform provider
        
        
        """
        ...
    def setObserver(self, kalmanObserver: typing.Union[org.hipparchus.filtering.kalman.KalmanObserver, typing.Callable]) -> None:
        """
        Set the filter observer callback.
        
        Specified by: setObserver in interface KalmanFilter
        
        Parameters:
            kalmanObserver (KalmanObserver): the observer
        
        
        """
        ...

_UnscentedProcess__T = typing.TypeVar('_UnscentedProcess__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class UnscentedProcess(typing.Generic[_UnscentedProcess__T]):
    """
    Unscented process that can be estimated by a UnscentedKalmanFilter.
    
    This interface must be implemented by users to represent the behavior of the process to be estimated
    
    Since:
        2.2
    
          - UnscentedKalmanFilter
          - UnscentedProcess
    """
    def getEvolution(self, previousTime: float, sigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray], measurement: _UnscentedProcess__T) -> UnscentedEvolution:
        """
        Get the state evolution between two times.
        
        Parameters:
            previousTime (double): time of the previous state
            sigmaPoints (hipparchus[]): sigma points
            measurement (UnscentedProcess): measurement to process
        
        Returns:
            states evolution
        
        
        """
        ...
    def getInnovation(self, measurement: _UnscentedProcess__T, predictedMeasurement: org.hipparchus.linear.RealVector, predictedState: org.hipparchus.linear.RealVector, innovationCovarianceMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        Get the innovation brought by a measurement.
        
        Parameters:
            measurement (UnscentedProcess): measurement to process
            predictedMeasurement (hipparchus): predicted measurement
            predictedState (hipparchus): predicted state
            innovationCovarianceMatrix (hipparchus): innovation covariance matrix
        
        Returns:
            innovation brought by a measurement, may be null if measurement should be rejected
        
        
        """
        ...
    def getPredictedMeasurements(self, predictedSigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray], measurement: _UnscentedProcess__T) -> typing.MutableSequence[org.hipparchus.linear.RealVector]:
        """
        Get the state evolution between two times.
        
        Parameters:
            predictedSigmaPoints (hipparchus[]): predicted state sigma points
            measurement (UnscentedProcess): measurement to process
        
        Returns:
            predicted measurement sigma points
        
        
        """
        ...
    def getProcessNoiseMatrix(self, previousTime: float, predictedState: org.hipparchus.linear.RealVector, measurement: _UnscentedProcess__T) -> org.hipparchus.linear.RealMatrix:
        """
        Get the process noise covariance corresponding to the state evolution between two times.
        
        Parameters:
            previousTime (double): time of the previous state
            predictedState (hipparchus): predicted state
            measurement (UnscentedProcess): measurement to process
        
        Returns:
            states evolution
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman.unscented")``.

    UnscentedEvolution: typing.Type[UnscentedEvolution]
    UnscentedKalmanFilter: typing.Type[UnscentedKalmanFilter]
    UnscentedProcess: typing.Type[UnscentedProcess]
