import org.hipparchus.filtering.kalman
import org.hipparchus.linear
import org.hipparchus.util
import typing



class UnscentedEvolution:
    """
    public class UnscentedEvolution extends Object
    
        Container for :class:`~org.hipparchus.filtering.kalman.unscented.UnscentedProcess` evolution data.
    
        Since:
            2.2
    
        Also see:
            :class:`~org.hipparchus.filtering.kalman.unscented.UnscentedProcess`
    """
    def __init__(self, double: float, realVectorArray: typing.List[org.hipparchus.linear.RealVector], realVectorArray2: typing.List[org.hipparchus.linear.RealVector], realMatrix: org.hipparchus.linear.RealMatrix): ...
    def getCurrentMeasurements(self) -> typing.List[org.hipparchus.linear.RealVector]:
        """
            Get current measurements.
        
            Returns:
                current measurements
        
        
        """
        ...
    def getCurrentStates(self) -> typing.List[org.hipparchus.linear.RealVector]:
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
    def getProcessNoiseMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get process noise.
        
            Returns:
                process noise
        
        
        """
        ...

_UnscentedKalmanFilter__T = typing.TypeVar('_UnscentedKalmanFilter__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class UnscentedKalmanFilter(org.hipparchus.filtering.kalman.KalmanFilter[_UnscentedKalmanFilter__T], typing.Generic[_UnscentedKalmanFilter__T]):
    def __init__(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer, unscentedProcess: 'UnscentedProcess'[_UnscentedKalmanFilter__T], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate, unscentedTransformProvider: org.hipparchus.util.UnscentedTransformProvider): ...
    def estimationStep(self, t: _UnscentedKalmanFilter__T) -> org.hipparchus.filtering.kalman.ProcessEstimate: ...
    def getCorrected(self) -> org.hipparchus.filtering.kalman.ProcessEstimate: ...
    def getPredicted(self) -> org.hipparchus.filtering.kalman.ProcessEstimate: ...
    def getUnscentedTransformProvider(self) -> org.hipparchus.util.UnscentedTransformProvider: ...
    def predictionAndCorrectionSteps(self, t: _UnscentedKalmanFilter__T, realVectorArray: typing.List[org.hipparchus.linear.RealVector]) -> org.hipparchus.filtering.kalman.ProcessEstimate: ...

_UnscentedProcess__T = typing.TypeVar('_UnscentedProcess__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class UnscentedProcess(typing.Generic[_UnscentedProcess__T]):
    """
    public interface UnscentedProcess<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`>
    
        Unscented process that can be estimated by a :class:`~org.hipparchus.filtering.kalman.unscented.UnscentedKalmanFilter`.
    
        This interface must be implemented by users to represent the behavior of the process to be estimated
    
        Since:
            2.2
    
        Also see:
            :class:`~org.hipparchus.filtering.kalman.unscented.UnscentedKalmanFilter`,
            :class:`~org.hipparchus.filtering.kalman.unscented.UnscentedProcess`
    """
    def getEvolution(self, double: float, realVectorArray: typing.List[org.hipparchus.linear.RealVector], t: _UnscentedProcess__T) -> UnscentedEvolution:
        """
            Get the state evolution between two times.
        
            Parameters:
                previousTime (double): time of the previous state
                sigmaPoints (RealVector[]): sigma points
                measurement (:class:`~org.hipparchus.filtering.kalman.unscented.UnscentedProcess`): measurement to process
        
            Returns:
                states evolution
        
        
        """
        ...
    def getInnovation(self, t: _UnscentedProcess__T, realVector: org.hipparchus.linear.RealVector, realVector2: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealVector:
        """
            Get the innovation brought by a measurement.
        
            Parameters:
                measurement (:class:`~org.hipparchus.filtering.kalman.unscented.UnscentedProcess`): measurement to process
                predictedMeasurement (RealVector): predicted measurement
                predictedState (RealVector): predicted state
                innovationCovarianceMatrix (RealMatrix): innovation covariance matrix
        
            Returns:
                innovation brought by a measurement, may be null if measurement should be rejected
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman.unscented")``.

    UnscentedEvolution: typing.Type[UnscentedEvolution]
    UnscentedKalmanFilter: typing.Type[UnscentedKalmanFilter]
    UnscentedProcess: typing.Type[UnscentedProcess]
