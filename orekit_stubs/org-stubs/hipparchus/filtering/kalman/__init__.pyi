import org.hipparchus.filtering.kalman.extended
import org.hipparchus.filtering.kalman.linear
import org.hipparchus.linear
import typing



_KalmanFilter__T = typing.TypeVar('_KalmanFilter__T', bound='Measurement')  # <T>
class KalmanFilter(typing.Generic[_KalmanFilter__T]):
    """
    public interface KalmanFilter<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`>
    
        Interface representing a Kalman filter.
    
        Since:
            1.3
    """
    def estimationStep(self, t: _KalmanFilter__T) -> 'ProcessEstimate': ...
    def getCorrected(self) -> 'ProcessEstimate':
        """
            Get the current corrected state.
        
            Returns:
                current corrected state
        
        
        """
        ...
    def getPredicted(self) -> 'ProcessEstimate':
        """
            Get the current predicted state.
        
            Returns:
                current predicted state
        
        
        """
        ...

class Measurement:
    """
    public interface Measurement
    
        Interface defining a measurement on process.
    
        Since:
            1.3
    """
    def getCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the measurement covariance.
        
            Returns:
                measurement covariance
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Get the process time.
        
            Returns:
                process time (typically the time or index of a measurement)
        
        
        """
        ...
    def getValue(self) -> org.hipparchus.linear.RealVector:
        """
            Get the measurement vector.
        
            Returns:
                measurement vector
        
        
        """
        ...

class ProcessEstimate:
    """
    public class ProcessEstimate extends Object
    
        Holder for process state and covariance.
    
        The estimate always contains time, state and covariance. These data are the only ones needed to start a Kalman filter.
        Once a filter has been started and produces new estimates, these new estimates will always contain a state transition
        matrix and if the measurement has not been ignored, they will also contain measurement Jacobian, innovation covariance
        and Kalman gain.
    
        Since:
            1.3
    """
    @typing.overload
    def __init__(self, double: float, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix): ...
    @typing.overload
    def __init__(self, double: float, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix, realMatrix2: org.hipparchus.linear.RealMatrix, realMatrix3: org.hipparchus.linear.RealMatrix, realMatrix4: org.hipparchus.linear.RealMatrix, realMatrix5: org.hipparchus.linear.RealMatrix): ...
    def getCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the state covariance.
        
            Returns:
                state covariance
        
        
        """
        ...
    def getInnovationCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the innovation covariance matrix.
        
            Returns:
                innovation covariance matrix (may be null for initial process estimate or if the measurement has been ignored)
        
            Since:
                1.4
        
        
        """
        ...
    def getKalmanGain(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Kalman gain matrix.
        
            Returns:
                Kalman gain matrix (may be null for initial process estimate or if the measurement has been ignored)
        
            Since:
                1.4
        
        
        """
        ...
    def getMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian of the measurement with respect to the state (H matrix).
        
            Returns:
                Jacobian of the measurement with respect to the state (may be null for initial process estimate or if the measurement
                has been ignored)
        
            Since:
                1.4
        
        
        """
        ...
    def getState(self) -> org.hipparchus.linear.RealVector:
        """
            Get the state vector.
        
            Returns:
                state vector
        
        
        """
        ...
    def getStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get state transition matrix between previous state and estimated (but not yet corrected) state.
        
            Returns:
                state transition matrix between previous state and estimated state (but not yet corrected) (may be null for initial
                process estimate)
        
            Since:
                1.4
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Get the process time.
        
            Returns:
                process time (typically the time or index of a measurement)
        
        
        """
        ...

_AbstractKalmanFilter__T = typing.TypeVar('_AbstractKalmanFilter__T', bound=Measurement)  # <T>
class AbstractKalmanFilter(KalmanFilter[_AbstractKalmanFilter__T], typing.Generic[_AbstractKalmanFilter__T]):
    """
    public abstract class AbstractKalmanFilter<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`> extends Object implements :class:`~org.hipparchus.filtering.kalman.KalmanFilter`<T>
    
        Shared parts between linear and non-linear Kalman filters.
    
        Since:
            1.3
    """
    def getCorrected(self) -> ProcessEstimate:
        """
            Get the corrected state.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanFilter.getCorrected`Â in
                interfaceÂ :class:`~org.hipparchus.filtering.kalman.KalmanFilter`
        
            Returns:
                corrected state
        
        
        """
        ...
    def getPredicted(self) -> ProcessEstimate:
        """
            Get the predicted state.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanFilter.getPredicted`Â in
                interfaceÂ :class:`~org.hipparchus.filtering.kalman.KalmanFilter`
        
            Returns:
                predicted state
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman")``.

    AbstractKalmanFilter: typing.Type[AbstractKalmanFilter]
    KalmanFilter: typing.Type[KalmanFilter]
    Measurement: typing.Type[Measurement]
    ProcessEstimate: typing.Type[ProcessEstimate]
    extended: org.hipparchus.filtering.kalman.extended.__module_protocol__
    linear: org.hipparchus.filtering.kalman.linear.__module_protocol__
