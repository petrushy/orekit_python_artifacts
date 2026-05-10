
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.filtering.kalman
import org.hipparchus.linear
import typing



_ExtendedKalmanFilter__T = typing.TypeVar('_ExtendedKalmanFilter__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class ExtendedKalmanFilter(org.hipparchus.filtering.kalman.AbstractKalmanFilter[_ExtendedKalmanFilter__T], typing.Generic[_ExtendedKalmanFilter__T]):
    """
    Kalman filter for NonLinearProcess.
    
    Since:
        1.3
    """
    def __init__(self, decomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], process: 'NonLinearProcess'[_ExtendedKalmanFilter__T], initialState: org.hipparchus.filtering.kalman.ProcessEstimate):
        """
        Simple constructor.
        
        Parameters:
            decomposer (hipparchus): decomposer to use for the correction phase
            process (NonLinearProcess<ExtendedKalmanFilter> process): non-linear process to estimate
            initialState (ProcessEstimate): initial state
        
        
        """
        ...
    def estimationStep(self, measurement: _ExtendedKalmanFilter__T) -> org.hipparchus.filtering.kalman.ProcessEstimate:
        """
        Perform one estimation step.
        
        Parameters:
            measurement (ExtendedKalmanFilter): single measurement to handle
        
        Returns:
            estimated state after measurement has been considered
        
        Raises:
            hipparchus: if estimation fails
        
        
        """
        ...

class NonLinearEvolution:
    """
    Container for NonLinearProcess evolution data.
    
    Since:
        1.3
    
    Also see:
        NonLinearProcess
    """
    def __init__(self, currentTime: float, currentState: org.hipparchus.linear.RealVector, stateTransitionMatrix: org.hipparchus.linear.RealMatrix, processNoiseMatrix: org.hipparchus.linear.RealMatrix, measurementJacobian: org.hipparchus.linear.RealMatrix):
        """
        Simple constructor.
        
        Parameters:
            currentTime (double): current time
            currentState (hipparchus): state vector at current time
            stateTransitionMatrix (hipparchus): state transition matrix between previous and current state
            processNoiseMatrix (hipparchus): process noise
            measurementJacobian (hipparchus): Jacobian of the measurement with respect to the state (may be null if measurement should be ignored)
        
        
        """
        ...
    def getCurrentState(self) -> org.hipparchus.linear.RealVector:
        """
        Get current state.
        
        Returns:
            current state
        
        
        """
        ...
    def getCurrentTime(self) -> float:
        """
        Get current time.
        
        Returns:
            current time
        
        
        """
        ...
    def getMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get measurement Jacobian.
        
        Returns:
            Jacobian of the measurement with respect to the state (may be null if measurement should be ignored)
        
        
        """
        ...
    def getProcessNoiseMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get process noise.
        
        Returns:
            process noise
        
        
        """
        ...
    def getStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get state transition matrix between previous and current state.
        
        Returns:
            state transition matrix between previous and current state
        
        
        """
        ...

_NonLinearProcess__T = typing.TypeVar('_NonLinearProcess__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class NonLinearProcess(typing.Generic[_NonLinearProcess__T]):
    """
    Non-linear process that can be estimated by a ExtendedKalmanFilter.
    
    This interface must be implemented by users to represent the behavior of the process to be estimated
    
    Since:
        1.3
    
    Also see:
        ExtendedKalmanFilter,
        LinearProcess
    """
    def getEvolution(self, previousTime: float, previousState: org.hipparchus.linear.RealVector, measurement: _NonLinearProcess__T) -> NonLinearEvolution:
        """
        Get the state evolution between two times.
        
        Parameters:
            previousTime (double): time of the previous state
            previousState (hipparchus): process state at previousTime
            measurement (NonLinearProcess): measurement to process
        
        Returns:
            state evolution
        
        
        """
        ...
    def getInnovation(self, measurement: _NonLinearProcess__T, evolution: NonLinearEvolution, innovationCovarianceMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
        Get the innovation brought by a measurement.
        
        Parameters:
            measurement (NonLinearProcess): measurement to process
            evolution (NonLinearEvolution):             evolution returned by a previous call to getEvolution
            innovationCovarianceMatrix (hipparchus): innovation covariance matrix, defined as \(h.P.h^T + r\) where h is the
                getMeasurementJacobian, P is the predicted
                covariance and r is getCovariance
        
        Returns:
            innovation brought by a measurement, may be null if measurement should be rejected
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman.extended")``.

    ExtendedKalmanFilter: typing.Type[ExtendedKalmanFilter]
    NonLinearEvolution: typing.Type[NonLinearEvolution]
    NonLinearProcess: typing.Type[NonLinearProcess]
