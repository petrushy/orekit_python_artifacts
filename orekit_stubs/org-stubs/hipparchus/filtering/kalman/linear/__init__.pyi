
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.filtering.kalman
import org.hipparchus.linear
import typing



class LinearEvolution:
    """
    public classLinearEvolution extends :class:`~org.hipparchus.filtering.kalman.linear.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Container for :class:`~org.hipparchus.filtering.kalman.linear.LinearProcess` evolution data.
    
        Since:
            1.3
    
        Also see:
    
              - :class:`~org.hipparchus.filtering.kalman.linear.LinearProcess`
    """
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, realMatrix2: org.hipparchus.linear.RealMatrix, realVector: org.hipparchus.linear.RealVector, realMatrix3: org.hipparchus.linear.RealMatrix, realMatrix4: org.hipparchus.linear.RealMatrix): ...
    def getCommand(self) -> org.hipparchus.linear.RealVector:
        """
            Get the command u :sub:`k-1` .
        
            Returns:
                command vector u :sub:`k-1` (can be null if there is no control)
        
        
        """
        ...
    def getControlMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the control matrix B :sub:`k-1` .
        
            Returns:
                control matrix B :sub:`k-1` (can be null if there is no control)
        
        
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
            Get the process noise matrix Q :sub:`k-1` .
        
            Returns:
                process noise matrix :sub:`k-1`
        
        
        """
        ...
    def getStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the state transition matrix A :sub:`k-1` .
        
            Returns:
                state transition matrix A :sub:`k-1`
        
        
        """
        ...

_LinearKalmanFilter__T = typing.TypeVar('_LinearKalmanFilter__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class LinearKalmanFilter(org.hipparchus.filtering.kalman.AbstractKalmanFilter[_LinearKalmanFilter__T], typing.Generic[_LinearKalmanFilter__T]):
    """
    public classLinearKalmanFilter<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`> extends :class:`~org.hipparchus.filtering.kalman.AbstractKalmanFilter`<T>
    
        Kalman filter for :class:`~org.hipparchus.filtering.kalman.linear.LinearProcess`.
    
        Since:
            1.3
    """
    def __init__(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable], linearProcess: typing.Union['LinearProcess'[_LinearKalmanFilter__T], typing.Callable[[_LinearKalmanFilter__T], LinearEvolution]], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate): ...
    def estimationStep(self, t: _LinearKalmanFilter__T) -> org.hipparchus.filtering.kalman.ProcessEstimate: ...

_LinearProcess__T = typing.TypeVar('_LinearProcess__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class LinearProcess(typing.Generic[_LinearProcess__T]):
    """
    public interfaceLinearProcess<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`>
    
        Linear process that can be estimated by a :class:`~org.hipparchus.filtering.kalman.linear.LinearKalmanFilter`.
    
        This interface must be implemented by users to represent the behavior of the process to be estimated
    
        A linear process is governed by the equation: \( x_k = A_{k-1} x_{k-1} + B_{k-1} u_{k-1} + w_{k-1} \) where
    
          - A :sub:`k-1` is the state transition matrix in the absence of control,
          - B :sub:`k-1` is the control matrix,
          - u :sub:`k-1` is the command
          - w :sub:`k-1` is the process noise, which has covariance matrix Q :sub:`k-1`
    
    
        Since:
            1.3
    
        Also see:
    
              - :class:`~org.hipparchus.filtering.kalman.linear.LinearKalmanFilter`
              - :class:`~org.hipparchus.filtering.kalman.extended.NonLinearProcess`
    """
    def getEvolution(self, t: _LinearProcess__T) -> LinearEvolution:
        """
            Get the state evolution between two times.
        
            Parameters:
                measurement (:class:`~org.hipparchus.filtering.kalman.linear.LinearProcess`): measurement to process
        
            Returns:
                state evolution
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman.linear")``.

    LinearEvolution: typing.Type[LinearEvolution]
    LinearKalmanFilter: typing.Type[LinearKalmanFilter]
    LinearProcess: typing.Type[LinearProcess]
