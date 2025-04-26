
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
    public classExtendedKalmanFilter<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`> extends :class:`~org.hipparchus.filtering.kalman.AbstractKalmanFilter`<T>
    
        Kalman filter for :class:`~org.hipparchus.filtering.kalman.extended.NonLinearProcess`.
    
        Since:
            1.3
    """
    def __init__(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], nonLinearProcess: 'NonLinearProcess'[_ExtendedKalmanFilter__T], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate): ...
    def estimationStep(self, t: _ExtendedKalmanFilter__T) -> org.hipparchus.filtering.kalman.ProcessEstimate: ...

class NonLinearEvolution:
    """
    public classNonLinearEvolution extends :class:`~org.hipparchus.filtering.kalman.extended.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Container for :class:`~org.hipparchus.filtering.kalman.extended.NonLinearProcess` evolution data.
    
        Since:
            1.3
    
        Also see:
    
              - :class:`~org.hipparchus.filtering.kalman.extended.NonLinearProcess`
    """
    def __init__(self, double: float, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, realMatrix2: org.hipparchus.linear.RealMatrix, realMatrix3: org.hipparchus.linear.RealMatrix): ...
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
    public interfaceNonLinearProcess<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`>
    
        Non-linear process that can be estimated by a :class:`~org.hipparchus.filtering.kalman.extended.ExtendedKalmanFilter`.
    
        This interface must be implemented by users to represent the behavior of the process to be estimated
    
        Since:
            1.3
    
        Also see:
    
              - :class:`~org.hipparchus.filtering.kalman.extended.ExtendedKalmanFilter`
              - :class:`~org.hipparchus.filtering.kalman.linear.LinearProcess`
    """
    def getEvolution(self, double: float, realVector: org.hipparchus.linear.RealVector, t: _NonLinearProcess__T) -> NonLinearEvolution:
        """
            Get the state evolution between two times.
        
            Parameters:
                previousTime (double): time of the previous state
                previousState (:class:`~org.hipparchus.filtering.kalman.extended.https:.www.hipparchus.org.hipparchus`): process state at :code:`previousTime`
                measurement (:class:`~org.hipparchus.filtering.kalman.extended.NonLinearProcess`): measurement to process
        
            Returns:
                state evolution
        
        
        """
        ...
    def getInnovation(self, t: _NonLinearProcess__T, nonLinearEvolution: NonLinearEvolution, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
            Get the innovation brought by a measurement.
        
            Parameters:
                measurement (:class:`~org.hipparchus.filtering.kalman.extended.NonLinearProcess`): measurement to process
                evolution (:class:`~org.hipparchus.filtering.kalman.extended.NonLinearEvolution`):             evolution returned by a previous call to :meth:`~org.hipparchus.filtering.kalman.extended.NonLinearProcess.getEvolution`
                innovationCovarianceMatrix (:class:`~org.hipparchus.filtering.kalman.extended.https:.www.hipparchus.org.hipparchus`): innovation covariance matrix, defined as \(h.P.h^T + r\) where h is the
                    :meth:`~org.hipparchus.filtering.kalman.extended.NonLinearEvolution.getMeasurementJacobian`, P is the predicted
                    covariance and r is :meth:`~org.hipparchus.filtering.kalman.Measurement.getCovariance`
        
            Returns:
                innovation brought by a measurement, may be null if measurement should be rejected
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman.extended")``.

    ExtendedKalmanFilter: typing.Type[ExtendedKalmanFilter]
    NonLinearEvolution: typing.Type[NonLinearEvolution]
    NonLinearProcess: typing.Type[NonLinearProcess]
