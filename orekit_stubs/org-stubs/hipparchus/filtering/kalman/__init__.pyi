
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.hipparchus.filtering.kalman.extended
import org.hipparchus.filtering.kalman.linear
import org.hipparchus.filtering.kalman.unscented
import org.hipparchus.linear
import typing



class KalmanEstimate:
    """
    public interfaceKalmanEstimate
    
        Interface representing a Kalman estimate.
    
        Since:
            4.0
    """
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
    def getStateCrossCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the cross-covariance between the previous state and the prediction. Not required for forward filtering, but required
            for the smoother.
        
            Returns:
                cross-covariance
        
        
        """
        ...

class KalmanObserver:
    """
    public interfaceKalmanObserver
    
        Observer for Kalman filter recursions.
    
        This interface is intended to be implemented by users to monitor the progress of the Kalman filter estimator during
        estimation.
    """
    def init(self, kalmanEstimate: KalmanEstimate) -> None:
        """
            Callback for initialisation of observer.
        
            Parameters:
                estimate (:class:`~org.hipparchus.filtering.kalman.KalmanEstimate`): estimate calculated by a Kalman filter
        
        
        """
        ...
    def updatePerformed(self, kalmanEstimate: KalmanEstimate) -> None:
        """
            Notification callback after each Kalman filter measurement update.
        
            Parameters:
                estimate (:class:`~org.hipparchus.filtering.kalman.KalmanEstimate`): estimate calculated by a Kalman filter
        
        
        """
        ...

class Measurement:
    """
    public interfaceMeasurement
    
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
    public classProcessEstimate extends :class:`~org.hipparchus.filtering.kalman.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
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

_KalmanFilter__T = typing.TypeVar('_KalmanFilter__T', bound=Measurement)  # <T>
class KalmanFilter(KalmanEstimate, typing.Generic[_KalmanFilter__T]):
    """
    public interfaceKalmanFilter<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`>extends :class:`~org.hipparchus.filtering.kalman.KalmanEstimate`
    
        Interface representing a Kalman filter.
    
        Since:
            1.3
    """
    def estimationStep(self, t: _KalmanFilter__T) -> ProcessEstimate: ...
    def setObserver(self, kalmanObserver: typing.Union[KalmanObserver, typing.Callable]) -> None:
        """
            Set the filter observer callback.
        
            Parameters:
                observer (:class:`~org.hipparchus.filtering.kalman.KalmanObserver`): the observer
        
        
        """
        ...

class KalmanSmoother(KalmanObserver):
    """
    public classKalmanSmoother extends :class:`~org.hipparchus.filtering.kalman.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.filtering.kalman.KalmanObserver`
    
        Kalman smoother for linear, extended or unscented filters.
    
        This implementation is attached to a filter using the observer mechanism. Once all measurements have been processed by
        the filter, the smoothing method can be called.
    
        For example
    
        .. code-block: java
        
             // Kalman filter
             final KalmanFilter<SimpleMeasurement> filter = new LinearKalmanFilter<>(decomposer, process, initialState);
        
             // Smoother observer
             final KalmanSmoother smoother = new KalmanSmoother(decomposer);
             filter.setObserver(smoother);
        
             // Process measurements with filter (forwards pass)
             measurements.forEach(filter::estimationStep);
        
             // Smooth backwards
             List<ProcessEstimate> smoothedStates = smoother.backwardsSmooth();
         
    
        Also see:
    
              - "Särkkä, S. Bayesian Filtering and Smoothing. Cambridge 2013"
    """
    def __init__(self, matrixDecomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]): ...
    def backwardsSmooth(self) -> java.util.List[ProcessEstimate]: ...
    def init(self, kalmanEstimate: KalmanEstimate) -> None:
        """
            Description copied from interface: :meth:`~org.hipparchus.filtering.kalman.KalmanObserver.init`
            Callback for initialisation of observer.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanObserver.init` in
                interface :class:`~org.hipparchus.filtering.kalman.KalmanObserver`
        
            Parameters:
                estimate (:class:`~org.hipparchus.filtering.kalman.KalmanEstimate`): estimate calculated by a Kalman filter
        
        
        """
        ...
    def updatePerformed(self, kalmanEstimate: KalmanEstimate) -> None:
        """
            Description copied from interface: :meth:`~org.hipparchus.filtering.kalman.KalmanObserver.updatePerformed`
            Notification callback after each Kalman filter measurement update.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanObserver.updatePerformed` in
                interface :class:`~org.hipparchus.filtering.kalman.KalmanObserver`
        
            Parameters:
                estimate (:class:`~org.hipparchus.filtering.kalman.KalmanEstimate`): estimate calculated by a Kalman filter
        
        
        """
        ...

_AbstractKalmanFilter__T = typing.TypeVar('_AbstractKalmanFilter__T', bound=Measurement)  # <T>
class AbstractKalmanFilter(KalmanFilter[_AbstractKalmanFilter__T], typing.Generic[_AbstractKalmanFilter__T]):
    """
    public abstract classAbstractKalmanFilter<T extends :class:`~org.hipparchus.filtering.kalman.Measurement`> extends :class:`~org.hipparchus.filtering.kalman.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.filtering.kalman.KalmanFilter`<T>
    
        Shared parts between linear and non-linear Kalman filters.
    
        Since:
            1.3
    """
    def getCorrected(self) -> ProcessEstimate:
        """
            Get the corrected state.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanEstimate.getCorrected` in
                interface :class:`~org.hipparchus.filtering.kalman.KalmanEstimate`
        
            Returns:
                corrected state
        
        
        """
        ...
    def getPredicted(self) -> ProcessEstimate:
        """
            Get the predicted state.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanEstimate.getPredicted` in
                interface :class:`~org.hipparchus.filtering.kalman.KalmanEstimate`
        
            Returns:
                predicted state
        
        
        """
        ...
    def getStateCrossCovariance(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the cross-covariance between the previous state and the prediction. Not required for forward filtering, but required
            for the smoother.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanEstimate.getStateCrossCovariance` in
                interface :class:`~org.hipparchus.filtering.kalman.KalmanEstimate`
        
            Returns:
                cross-covariance
        
        
        """
        ...
    def setObserver(self, kalmanObserver: typing.Union[KalmanObserver, typing.Callable]) -> None:
        """
            Set the filter observer callback.
        
            Specified by:
                :meth:`~org.hipparchus.filtering.kalman.KalmanFilter.setObserver` in
                interface :class:`~org.hipparchus.filtering.kalman.KalmanFilter`
        
            Parameters:
                kalmanObserver (:class:`~org.hipparchus.filtering.kalman.KalmanObserver`): the observer
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman")``.

    AbstractKalmanFilter: typing.Type[AbstractKalmanFilter]
    KalmanEstimate: typing.Type[KalmanEstimate]
    KalmanFilter: typing.Type[KalmanFilter]
    KalmanObserver: typing.Type[KalmanObserver]
    KalmanSmoother: typing.Type[KalmanSmoother]
    Measurement: typing.Type[Measurement]
    ProcessEstimate: typing.Type[ProcessEstimate]
    extended: org.hipparchus.filtering.kalman.extended.__module_protocol__
    linear: org.hipparchus.filtering.kalman.linear.__module_protocol__
    unscented: org.hipparchus.filtering.kalman.unscented.__module_protocol__
