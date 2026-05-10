
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.spherical.twod
import org.hipparchus.ode.events
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.geometry.fov
import org.orekit.models
import org.orekit.models.earth
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.events.handlers
import org.orekit.propagation.events.intervals
import org.orekit.propagation.sampling
import org.orekit.time
import org.orekit.utils
import typing



class EnablingPredicate:
    """
    This interface represents an event enabling predicate function.
    
    Since:
        7.1
    """
    @staticmethod
    def andCombine(*enablingPredicates: typing.Union['EnablingPredicate', typing.Callable]) -> 'EnablingPredicate':
        """
        Method combining predicated based on the AND logic operator.
        
        Parameters:
            enablingPredicates (EnablingPredicate...): predicates
        
        Returns:
            combined predicate
        
        Since:
            13.1
        
        
        """
        ...
    def eventIsEnabled(self, state: org.orekit.propagation.SpacecraftState, detector: 'EventDetector', g: float) -> bool:
        """
        Compute an event enabling function of state.
        
        Parameters:
            state (SpacecraftState): current state
            detector (EventDetector): underlying detector
            g (double): value of the underlying detector for the current state
        
        Returns:
            true if the event is enabled (i.e. it can be triggered), false if it should be ignored
        
        
        """
        ...
    @staticmethod
    def orCombine(*enablingPredicates: typing.Union['EnablingPredicate', typing.Callable]) -> 'EnablingPredicate':
        """
        Method combining predicated based on the OR logic operator.
        
        Parameters:
            enablingPredicates (EnablingPredicate...): predicates
        
        Returns:
            combined predicate
        
        Since:
            13.1
        
        
        """
        ...

class EventDetectionSettings:
    """
    Class containing parameters for event detection.
    
    Since:
        12.2
    
    Also see:
        EventDetector
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    Default maximum checking interval (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default convergence threshold (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    Default maximum number of iterations in the event time search.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, adaptableInterval: typing.Union[org.orekit.propagation.events.intervals.AdaptableInterval, typing.Callable], double: float, int: int): ...
    @staticmethod
    def getDefaultEventDetectionSettings() -> 'EventDetectionSettings':
        """
        Returns default settings for event detections.
        
        Returns:
            default settings
        
        
        """
        ...
    def getMaxCheckInterval(self) -> org.orekit.propagation.events.intervals.AdaptableInterval:
        """
        Getter for adaptable interval.
        
        Returns:
            adaptable interval
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Getter for max iter.
        
        Returns:
            max iter
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
        Getter for threshold.
        
        Returns:
            threshold
        
        
        """
        ...
    def withMaxCheckInterval(self, newMaxCheckInterval: typing.Union[org.orekit.propagation.events.intervals.AdaptableInterval, typing.Callable]) -> 'EventDetectionSettings':
        """
        Builds a new instance with a new max. check interval.
        
        Parameters:
            newMaxCheckInterval (AdaptableInterval): new max. check.
        
        Returns:
            new object
        
        Since:
            13.0
        
        
        """
        ...
    def withMaxIter(self, newMaxIterationCount: int) -> 'EventDetectionSettings':
        """
        Builds a new instance with a new max. iteration count.
        
        Parameters:
            newMaxIterationCount (int): new max iteration count.
        
        Returns:
            new object
        
        Since:
            13.0
        
        
        """
        ...
    def withThreshold(self, newThreshold: float) -> 'EventDetectionSettings':
        """
        Builds a new instance with a new threshold value.
        
        Parameters:
            newThreshold (double): detection threshold in seconds
        
        Returns:
            new object
        
        Since:
            13.0
        
        
        """
        ...

class EventDetector:
    """
    This interface represents space-dynamics aware events detectors.
    
    It mirrors the ODEEventHandler interface from org but provides a space-dynamics interface to the methods.
    
    Events detectors are a useful solution to meet the requirements of propagators concerning discrete conditions. The state of each event detector is queried by the propagator from time to time, at least once every getMaxCheckInterval but it may be more frequent. When the sign of the underlying g switching function changes, a root-finding algorithm is run to precisely locate the event, down to a configured getThreshold. The getMaxCheckInterval is therefore devoted to separate roots and is often much larger than the getThreshold.
    
    The physical meaning of the g switching function is not really used by the event detection algorithms. Its varies from event detector to event detector. One example would be a visibility detector that could use the angular elevation of the satellite above horizon as a g switching function. In this case, the function would switch from negative to positive when the satellite raises above horizon and it would switch from positive to negative when it sets backs below horizon. Another example would be an apside detector that could use the dot product of position and velocity. In this case, the function would switch from negative to positive when the satellite crosses periapsis and it would switch from positive to negative when the satellite crosses apoapsis.
    
    When the precise state at which the g switching function changes has been located, the corresponding event is triggered, by calling the eventOccurred method from the associated getHandler. The method can do whatever it needs with the event (logging it, performing some processing, ignore it ...). The return value of the method will be used by the propagator to stop or resume propagation, possibly changing the state vector.
    """
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        Since:
            13.1
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        This method finalizes the event detector's job.
        
        Parameters:
            state (SpacecraftState): state at propagation end
        
        Since:
            12.2
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
        Getter for the settings.
        
        Returns:
            detection settings
        
        Since:
            12.2
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Get the handler.
        
        Returns:
            event handler to call at event occurrences
        
        Since:
            12.0
        
        
        """
        ...
    def getMaxCheckInterval(self) -> org.orekit.propagation.events.intervals.AdaptableInterval:
        """
        Get maximal time interval between switching function checks.
        
        Returns:
            maximal time interval (s) between switching function checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Get maximal number of iterations in the event time search.
        
        Returns:
            maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
        Get the convergence threshold in the event time search.
        
        Returns:
            convergence threshold (s)
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Parameters:
            state (SpacecraftState): current state
            target (AbsoluteDate): target time for the integration
        
        Since:
            13.0
        
        
        """
        ...

class EventDetectorsProvider:
    """
    Interface for building event detectors for force models and maneuver parameters.
    
    Objects implementing this interface are mainly ForceModel and DSSTForceModel.
    
    Since:
        12.0
    """
    DATATION_ACCURACY: typing.ClassVar[float] = ...
    """
    Accuracy of switching events dates (s).
    
    Also see:
        constant
    
    
    """
    def getDateDetector(self, *timeStampeds: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> 'DateDetector':
        """
        Method building dates' detector.
        
        Parameters:
            timeStampeds (TimeStamped...): dates to detect
        
        Returns:
            dates detector
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[EventDetector]: ...
    @typing.overload
    def getEventDetectors(self, parameterDrivers: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[EventDetector]: ...
    _getFieldDateDetector__T = typing.TypeVar('_getFieldDateDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldDateDetector(self, field: org.hipparchus.Field[_getFieldDateDetector__T], *timeStampeds: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> 'FieldDateDetector'[_getFieldDateDetector__T]:
        """
        Method building dates' detector.
        
        Parameters:
            field (Field<T> field): field
            timeStampeds (TimeStamped...): dates to detect
        
        Returns:
            dates detector
        
        Since:
            13.0
        
        
        """
        ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T]) -> java.util.stream.Stream['FieldEventDetector'[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T], parameterDrivers: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream['FieldEventDetector'[_getFieldEventDetectors_1__T]]: ...

_EventState__T = typing.TypeVar('_EventState__T', bound=EventDetector)  # <T>
class EventState(typing.Generic[_EventState__T]):
    """
    This class handles the state for one EventDetector during integration steps.
    
    This class is heavily based on the class with the same name from the Hipparchus library. The changes performed consist in replacing raw types (double and double arrays) with space dynamics types (AbsoluteDate, SpacecraftState).
    
    Each time the propagator proposes a step, the event detector should be checked. This class handles the state of one detector during one propagation step, with references to the state at the end of the preceding step. This information is used to determine if the detector should trigger an event or not during the proposed step (and hence the step should be reduced to ensure the event occurs at a bound rather than inside the step).
    """
    def __init__(self, detector: _EventState__T):
        """
        Simple constructor.
        
        Parameters:
            detector (EventState): monitored event detector
        
        
        """
        ...
    def doEvent(self, state: org.orekit.propagation.SpacecraftState) -> 'EventState.EventOccurrence':
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Parameters:
            state (SpacecraftState): the state at the time of the event. This must be at the same time as the current value of
                getEventDate.
        
        Returns:
            the user's requested action and the new state if the action is
            Action.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            Action. This
            guarantees the integration will stop on or after the root, so that integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> bool:
        """
        Evaluate the impact of the proposed step on the event detector.
        
        Parameters:
            interpolator (OrekitStepInterpolator): step interpolator for the proposed step
        
        Returns:
            true if the event detector triggers an event before the end of the proposed step (this implies the step should be
            rejected)
        
        Raises:
            MathRuntimeException: if an event cannot be located
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        This method finalizes the event detector's job.
        
        Parameters:
            state (SpacecraftState): state at propagation end
        
        Since:
            12.2
        
        
        """
        ...
    def getEventDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the occurrence time of the event triggered in the current step.
        
        Returns:
            occurrence time of the event triggered in the current step.
        
        
        """
        ...
    def getEventDetector(self) -> _EventState__T:
        """
        Get the underlying event detector.
        
        Returns:
            underlying event detector
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def reinitializeBegin(self, interpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> None:
        """
        Reinitialize the beginning of the step.
        
        Parameters:
            interpolator (OrekitStepInterpolator): interpolator valid for the current step
        
        
        """
        ...
    def tryAdvance(self, state: org.orekit.propagation.SpacecraftState, interpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> bool:
        """
        Try to accept the current history up to the given time.
        
        It is not necessary to call this method before calling doEvent with the same state. It is necessary to call this method before you call doEvent on some other event detector.
        
        Parameters:
            state (SpacecraftState): to try to accept.
            interpolator (OrekitStepInterpolator): to use to find the new root, if any.
        
        Returns:
            if the event detector has an event it has not detected before that is on or before the same time as state. In
            other words false means continue on while true means stop and handle my event first.
        
        
        """
        ...
    class EventOccurrence:
        def getAction(self) -> org.hipparchus.ode.events.Action: ...
        def getNewState(self) -> org.orekit.propagation.SpacecraftState: ...
        def getStopDate(self) -> org.orekit.time.AbsoluteDate: ...

class EventsLogger:
    """
    This class logs events detectors events during propagation.
    
    As EventDetector are triggered during orbit propagation, an event specific eventOccurred method is called. This class can be used to add a global logging feature registering all events with their corresponding states in a chronological sequence (or reverse-chronological if propagation occurs backward).
    
    This class works by wrapping user-provided EventDetector before they are registered to the propagator. The wrapper monitor the calls to eventOccurred and store the corresponding events as LoggedEvent instances. After propagation is complete, the user can retrieve all the events that have occurred at once by calling method getLoggedEvents.
    """
    def __init__(self):
        """
        Simple constructor.
        
        Build an empty logger for events detectors.
        """
        ...
    def clearLoggedEvents(self) -> None:
        """
        Clear the logged events.
        """
        ...
    def getLoggedEvents(self) -> java.util.List['EventsLogger.LoggedEvent']:
        """
        Get an immutable copy of the logged events.
        
        The copy is independent of the logger. It is preserved event if the clearLoggedEvents method is called and the logger reused in another propagation.
        
        Returns:
            an immutable copy of the logged events
        
        
        """
        ...
    _monitorDetector__T = typing.TypeVar('_monitorDetector__T', bound=EventDetector)  # <T>
    def monitorDetector(self, monitoredDetector: _monitorDetector__T) -> EventDetector:
        """
        Monitor an event detector.
        
        In order to monitor an event detector, it must be wrapped thanks to this method as follows:
        
        
         Propagator propagator = new XyzPropagator(...);
         EventsLogger logger = new EventsLogger();
         EventDetector detector = new UvwDetector(...);
         propagator.addEventDetector(logger.monitorDetector(detector));
         
        
        Note that the event detector returned by the getEventDetector method in LoggedEvent instances returned by getLoggedEvents are the monitoredDetector instances themselves, not the wrapping detector returned by this method.
        
        Parameters:
            monitoredDetector (T): event detector to monitor
        
        Returns:
            the wrapping detector to add to the propagator
        
        
        """
        ...
    class LoggedEvent(org.orekit.time.TimeStamped):
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getEventDetector(self) -> EventDetector: ...
        def getResetState(self) -> org.orekit.propagation.SpacecraftState: ...
        def getState(self) -> org.orekit.propagation.SpacecraftState: ...
        def isIncreasing(self) -> bool: ...

_FieldEnablingPredicate__T = typing.TypeVar('_FieldEnablingPredicate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEnablingPredicate(typing.Generic[_FieldEnablingPredicate__T]):
    """
    This interface represents an event enabling predicate function.
    
    Since:
        12.0
    """
    _andCombine__T = typing.TypeVar('_andCombine__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def andCombine(*enablingPredicates: typing.Union['FieldEnablingPredicate'[_andCombine__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], 'FieldEventDetector'[org.hipparchus.CalculusFieldElement], _andCombine__T], bool]]) -> 'FieldEnablingPredicate'[_andCombine__T]:
        """
        Method combining predicated based on the AND logic operator.
        
        Parameters:
            enablingPredicates (FieldEnablingPredicate<T>...): predicates
        
        Returns:
            combined predicate
        
        Since:
            13.1
        
        
        """
        ...
    def eventIsEnabled(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEnablingPredicate__T], detector: 'FieldEventDetector'[_FieldEnablingPredicate__T], g: _FieldEnablingPredicate__T) -> bool:
        """
        Compute an event enabling function of state.
        
        Parameters:
            state (FieldSpacecraftState<FieldEnablingPredicate> state): current state
            detector (FieldEventDetector<FieldEnablingPredicate> detector): underlying detector
            g (FieldEnablingPredicate): value of the underlying detector for the current state
        
        Returns:
            true if the event is enabled (i.e. it can be triggered), false if it should be ignored
        
        
        """
        ...
    _orCombine__T = typing.TypeVar('_orCombine__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def orCombine(*enablingPredicates: typing.Union['FieldEnablingPredicate'[_orCombine__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], 'FieldEventDetector'[org.hipparchus.CalculusFieldElement], _orCombine__T], bool]]) -> 'FieldEnablingPredicate'[_orCombine__T]:
        """
        Method combining predicated based on the OR logic operator.
        
        Parameters:
            enablingPredicates (FieldEnablingPredicate<T>...): predicates
        
        Returns:
            combined predicate
        
        Since:
            13.1
        
        
        """
        ...

_FieldEventDetectionSettings__T = typing.TypeVar('_FieldEventDetectionSettings__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventDetectionSettings(typing.Generic[_FieldEventDetectionSettings__T]):
    """
    Class containing parameters for event detection.
    
    Since:
        12.2
    
    Also see:
        EventDetectionSettings,
        FieldEventDetector
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    Default maximum checking interval (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default convergence threshold (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    Default maximum number of iterations in the event time search.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float, t: _FieldEventDetectionSettings__T, int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEventDetectionSettings__T], eventDetectionSettings: EventDetectionSettings): ...
    @typing.overload
    def __init__(self, fieldAdaptableInterval: typing.Union[org.orekit.propagation.events.intervals.FieldAdaptableInterval[_FieldEventDetectionSettings__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], bool], float]], t: _FieldEventDetectionSettings__T, int: int): ...
    _getDefaultEventDetectionSettings__T = typing.TypeVar('_getDefaultEventDetectionSettings__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getDefaultEventDetectionSettings(field: org.hipparchus.Field[_getDefaultEventDetectionSettings__T]) -> 'FieldEventDetectionSettings'[_getDefaultEventDetectionSettings__T]:
        """
        Returns default settings for event detections.
        
        Parameters:
            field (Field<T> field): field
        
        Returns:
            default settings
        
        Since:
            13.0
        
        
        """
        ...
    def getMaxCheckInterval(self) -> org.orekit.propagation.events.intervals.FieldAdaptableInterval[_FieldEventDetectionSettings__T]:
        """
        Getter for adaptable interval.
        
        Returns:
            adaptable interval
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Getter for max iter.
        
        Returns:
            max iter
        
        
        """
        ...
    def getThreshold(self) -> _FieldEventDetectionSettings__T:
        """
        Getter for threshold.
        
        Returns:
            threshold
        
        
        """
        ...
    def toEventDetectionSettings(self) -> EventDetectionSettings:
        """
        Create a non-Field equivalent object.
        
        Returns:
            event detection settings
        
        
        """
        ...
    def withMaxCheckInterval(self, newMaxCheckInterval: typing.Union[org.orekit.propagation.events.intervals.FieldAdaptableInterval[_FieldEventDetectionSettings__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], bool], float]]) -> 'FieldEventDetectionSettings'[_FieldEventDetectionSettings__T]:
        """
        Builds a new instance with a new max. check interval.
        
        Parameters:
            newMaxCheckInterval (FieldAdaptableInterval<FieldEventDetectionSettings> newMaxCheckInterval): new max. check.
        
        Returns:
            new object
        
        Since:
            13.0
        
        
        """
        ...
    def withMaxIter(self, newMaxIterationCount: int) -> 'FieldEventDetectionSettings'[_FieldEventDetectionSettings__T]:
        """
        Builds a new instance with a new max. iteration count.
        
        Parameters:
            newMaxIterationCount (int): new max iteration count.
        
        Returns:
            new object
        
        Since:
            13.0
        
        
        """
        ...
    def withThreshold(self, newThreshold: _FieldEventDetectionSettings__T) -> 'FieldEventDetectionSettings'[_FieldEventDetectionSettings__T]:
        """
        Builds a new instance with a new threshold value.
        
        Parameters:
            newThreshold (FieldEventDetectionSettings): detection threshold in seconds
        
        Returns:
            new object
        
        Since:
            13.0
        
        
        """
        ...

_FieldEventDetector__T = typing.TypeVar('_FieldEventDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventDetector(typing.Generic[_FieldEventDetector__T]):
    """
    This interface represents space-dynamics aware events detectors.
    
    It mirrors the FieldODEEventHandler interface from org but provides a space-dynamics interface to the methods.
    
    Events detectors are a useful solution to meet the requirements of propagators concerning discrete conditions. The state of each event detector is queried by the propagator from time to time, at least once every getMaxCheckInterval but it may be more frequent. When the sign of the underlying g switching function changes, a root-finding algorithm is run to precisely locate the event, down to a configured getThreshold. The getMaxCheckInterval is therefore devoted to separate roots and is often much larger than the getThreshold.
    
    The physical meaning of the g switching function is not really used by the event detection algorithms. Its varies from event detector to event detector. One example would be a visibility detector that could use the angular elevation of the satellite above horizon as a g switching function. In this case, the function would switch from negative to positive when the satellite raises above horizon and it would switch from positive to negative when it sets backs below horizon. Another example would be an apside detector that could use the dot product of position and velocity. In this case, the function would switch from negative to positive when the satellite crosses periapsis and it would switch from positive to negative when the satellite crosses apoapsis.
    
    When the precise state at which the g switching function changes has been located, the corresponding event is triggered, by calling the eventOccurred method from the associated getHandler. The method can do whatever it needs with the event (logging it, performing some processing, ignore it ...). The return value of the method will be used by the propagator to stop or resume propagation, possibly changing the state vector.
    """
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        Since:
            13.1
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventDetector__T]) -> None:
        """
        This method finalizes the event detector's job.
        
        Parameters:
            state (FieldSpacecraftState<FieldEventDetector> state): state at propagation end
        
        Since:
            12.2
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldEventDetector__T]) -> _FieldEventDetector__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<FieldEventDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldEventDetector__T]:
        """
        Getter for the settings.
        
        Returns:
            detection settings
        
        Since:
            12.2
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldEventDetector__T]:
        """
        Get the handler.
        
        Returns:
            event handler to call at event occurrences
        
        Since:
            12.0
        
        
        """
        ...
    def getMaxCheckInterval(self) -> org.orekit.propagation.events.intervals.FieldAdaptableInterval[_FieldEventDetector__T]:
        """
        Get maximal time interval between switching function checks.
        
        Returns:
            maximal time interval (s) between switching function checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Get maximal number of iterations in the event time search.
        
        Returns:
            maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> _FieldEventDetector__T:
        """
        Get the convergence threshold in the event time search.
        
        Returns:
            convergence threshold (s)
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldEventDetector__T], t: org.orekit.time.FieldAbsoluteDate[_FieldEventDetector__T]) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Parameters:
            s0 (FieldSpacecraftState<FieldEventDetector> s0): initial state
            t (FieldAbsoluteDate<FieldEventDetector> t): target time for the integration
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventDetector__T], target: org.orekit.time.FieldAbsoluteDate[_FieldEventDetector__T]) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Parameters:
            state (FieldSpacecraftState<FieldEventDetector> state): current state
            target (FieldAbsoluteDate<FieldEventDetector> target): target time for the integration
        
        Since:
            13.0
        
        
        """
        ...

_FieldEventState__EventOccurrence__T = typing.TypeVar('_FieldEventState__EventOccurrence__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldEventState__D = typing.TypeVar('_FieldEventState__D', bound=FieldEventDetector)  # <D>
_FieldEventState__T = typing.TypeVar('_FieldEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventState(typing.Generic[_FieldEventState__D, _FieldEventState__T]):
    """
    This class handles the state for one FieldEventDetector during integration steps.
    
    This class is heavily based on the class with the same name from the Hipparchus library. The changes performed consist in replacing raw types (double and double arrays) with space dynamics types (FieldAbsoluteDate, FieldSpacecraftState).
    
    Each time the propagator proposes a step, the event detector should be checked. This class handles the state of one detector during one propagation step, with references to the state at the end of the preceding step. This information is used to determine if the detector should trigger an event or not during the proposed step (and hence the step should be reduced to ensure the event occurs at a bound rather than inside the step).
    """
    def __init__(self, detector: _FieldEventState__D):
        """
        Simple constructor.
        
        Parameters:
            detector (FieldEventState): monitored event detector
        
        
        """
        ...
    def doEvent(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T]) -> 'FieldEventState.EventOccurrence'[_FieldEventState__T]:
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Parameters:
            state (FieldSpacecraftState<FieldEventState> state): the state at the time of the event. This must be at the same time as the current value of
                getEventDate.
        
        Returns:
            the user's requested action and the new state if the action is
            Action.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            Action. This
            guarantees the integration will stop on or after the root, so that integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.orekit.propagation.sampling.FieldOrekitStepInterpolator[_FieldEventState__T]) -> bool:
        """
        Evaluate the impact of the proposed step on the event detector.
        
        Parameters:
            interpolator (FieldOrekitStepInterpolator<FieldEventState> interpolator): step interpolator for the proposed step
        
        Returns:
            true if the event detector triggers an event before the end of the proposed step (this implies the step should be
            rejected)
        
        Raises:
            MathRuntimeException: if an event cannot be located
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T]) -> None:
        """
        This method finalizes the event detector's job.
        
        Parameters:
            state (FieldSpacecraftState<FieldEventState> state): state at propagation end
        
        Since:
            12.2
        
        
        """
        ...
    def getEventDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldEventState__T]:
        """
        Get the occurrence time of the event triggered in the current step.
        
        Returns:
            occurrence time of the event triggered in the current step.
        
        
        """
        ...
    def getEventDetector(self) -> _FieldEventState__D:
        """
        Get the underlying event detector.
        
        Returns:
            underlying event detector
        
        
        """
        ...
    def getPendingEvent(self) -> bool:
        """
        Get PendingEvent.
        
        Returns:
            if there is a pending event or not
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T], t: org.orekit.time.FieldAbsoluteDate[_FieldEventState__T]) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        Parameters:
            s0 (FieldSpacecraftState<FieldEventState> s0): initial state
            t (FieldAbsoluteDate<FieldEventState> t): target time for the integration
        
        
        """
        ...
    def reinitializeBegin(self, interpolator: org.orekit.propagation.sampling.FieldOrekitStepInterpolator[_FieldEventState__T]) -> None:
        """
        Reinitialize the beginning of the step.
        
        Parameters:
            interpolator (FieldOrekitStepInterpolator<FieldEventState> interpolator): interpolator valid for the current step
        
        
        """
        ...
    def tryAdvance(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T], interpolator: org.orekit.propagation.sampling.FieldOrekitStepInterpolator[_FieldEventState__T]) -> bool:
        """
        Try to accept the current history up to the given time.
        
        It is not necessary to call this method before calling doEvent with the same state. It is necessary to call this method before you call doEvent on some other event detector.
        
        Parameters:
            state (FieldSpacecraftState<FieldEventState> state): to try to accept.
            interpolator (FieldOrekitStepInterpolator<FieldEventState> interpolator): to use to find the new root, if any.
        
        Returns:
            if the event detector has an event it has not detected before that is on or before the same time as state. In
            other words false means continue on while true means stop and handle my event first.
        
        
        """
        ...
    class EventOccurrence(typing.Generic[_FieldEventState__EventOccurrence__T]):
        def getAction(self) -> org.hipparchus.ode.events.Action: ...
        def getNewState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventState__EventOccurrence__T]: ...
        def getStopDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldEventState__EventOccurrence__T]: ...

_FieldEventsLogger__FieldLoggedEvent__T = typing.TypeVar('_FieldEventsLogger__FieldLoggedEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldEventsLogger__T = typing.TypeVar('_FieldEventsLogger__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventsLogger(typing.Generic[_FieldEventsLogger__T]):
    """
    This class logs events detectors events during propagation.
    
    As FieldEventDetector are triggered during orbit propagation, an event specific eventOccurred method is called. This class can be used to add a global logging feature registering all events with their corresponding states in a chronological sequence (or reverse-chronological if propagation occurs backward).
    
    This class works by wrapping user-provided FieldEventDetector before they are registered to the propagator. The wrapper monitor the calls to eventOccurred and store the corresponding events as FieldLoggedEvent instances. After propagation is complete, the user can retrieve all the events that have occurred at once by calling method getLoggedEvents.
    """
    def __init__(self):
        """
        Simple constructor.
        
        Build an empty logger for events detectors.
        """
        ...
    def clearLoggedEvents(self) -> None:
        """
        Clear the logged events.
        """
        ...
    def getLoggedEvents(self) -> java.util.List['FieldEventsLogger.FieldLoggedEvent'[_FieldEventsLogger__T]]:
        """
        Get an immutable copy of the logged events.
        
        The copy is independent of the logger. It is preserved event if the clearLoggedEvents method is called and the logger reused in another propagation.
        
        Returns:
            an immutable copy of the logged events
        
        
        """
        ...
    def monitorDetector(self, monitoredDetector: FieldEventDetector[_FieldEventsLogger__T]) -> FieldEventDetector[_FieldEventsLogger__T]:
        """
        Monitor an event detector.
        
        In order to monitor an event detector, it must be wrapped thanks to this method as follows:
        
        
         Propagator propagator = new XyzPropagator(...);
         EventsLogger logger = new EventsLogger();
         FieldEventDetector<T> detector = new UvwDetector(...);
         propagator.addEventDetector(logger.monitorDetector(detector));
         
        
        Note that the event detector returned by the getEventDetector method in FieldLoggedEvent instances returned by getLoggedEvents are the monitoredDetector instances themselves, not the wrapping detector returned by this method.
        
        Parameters:
            monitoredDetector (FieldEventDetector<FieldEventsLogger> monitoredDetector): event detector to monitor
        
        Returns:
            the wrapping detector to add to the propagator
        
        
        """
        ...
    class FieldLoggedEvent(typing.Generic[_FieldEventsLogger__FieldLoggedEvent__T]):
        def getEventDetector(self) -> FieldEventDetector[_FieldEventsLogger__FieldLoggedEvent__T]: ...
        def getResetState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventsLogger__FieldLoggedEvent__T]: ...
        def getState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventsLogger__FieldLoggedEvent__T]: ...
        def isIncreasing(self) -> bool: ...

class FilterType(java.lang.Enum['FilterType']):
    """
    Enumerate for EventSlopeFilter.
    
    This class is heavily based on the class with the same name from the Hipparchus library. The changes performed consist in package name and error handling.
    
    Since:
        6.0
    """
    TRIGGER_ONLY_DECREASING_EVENTS: typing.ClassVar['FilterType'] = ...
    TRIGGER_ONLY_INCREASING_EVENTS: typing.ClassVar['FilterType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'FilterType':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['FilterType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (FilterType c : FilterType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class VisibilityTrigger(java.lang.Enum['VisibilityTrigger']):
    """
    Enumerate for triggering visibility of spherical bodies.
    
    Since:
        10.0
    
    Also see:
        FieldOfViewDetector
    """
    VISIBLE_ONLY_WHEN_FULLY_IN_FOV: typing.ClassVar['VisibilityTrigger'] = ...
    VISIBLE_AS_SOON_AS_PARTIALLY_IN_FOV: typing.ClassVar['VisibilityTrigger'] = ...
    def radiusCorrection(self, angularRadius: float) -> float:
        """
        Apply radius correction.
        
        Parameters:
            angularRadius (double): target body angular radius
        
        Returns:
            corrected radius
        
        Since:
            10.1
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'VisibilityTrigger':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['VisibilityTrigger']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (VisibilityTrigger c : VisibilityTrigger.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_AbstractDetector__T = typing.TypeVar('_AbstractDetector__T', bound='AbstractDetector')  # <T>
class AbstractDetector(EventDetector, typing.Generic[_AbstractDetector__T]):
    """
    Common parts shared by several orbital events finders.
    
    Also see:
        addEventDetector
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    Default maximum checking interval (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default convergence threshold (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    Default maximum number of iterations in the event time search.
    
    Also see:
        constant
    
    
    """
    @staticmethod
    def checkIfForward(state: org.orekit.propagation.SpacecraftState, targetDate: org.orekit.time.AbsoluteDate) -> bool:
        """
        Check if propagation is forward or not.
        
        Parameters:
            state (SpacecraftState): initial state
            targetDate (AbsoluteDate): target propagation date
        
        Returns:
            forward flag
        
        Since:
            13.0
        
        
        """
        ...
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
        Getter for the settings.
        
        Specified by: getDetectionSettings in interface EventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Get the handler.
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface EventDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Returns:
            true if the current propagation is forward
        
        Since:
            7.2
        
        
        """
        ...
    def withDetectionSettings(self, newSettings: EventDetectionSettings) -> _AbstractDetector__T:
        """
        Set up the event detection settings.
        
        This will override settings previously configured.
        
        Parameters:
            newSettings (EventDetectionSettings): new event detection settings
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.2
        
        
        """
        ...
    def withHandler(self, newHandler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]) -> _AbstractDetector__T:
        """
        Set up the event handler to call at event occurrences.
        
        This will override a handler if it has been configured previously.
        
        Parameters:
            newHandler (EventHandler): event handler to call at event occurrences
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: float) -> _AbstractDetector__T:
        """
        Set up the maximum checking interval.
        
        This will override a maximum checking interval if it has been configured previously.
        
        Parameters:
            newMaxCheck (double): maximum checking interval (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Set up the maximum checking interval.
        
        This will override a maximum checking interval if it has been configured previously.
        
        Parameters:
            newMaxCheck (AdaptableInterval): maximum checking interval (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: typing.Union[org.orekit.propagation.events.intervals.AdaptableInterval, typing.Callable]) -> _AbstractDetector__T: ...
    def withMaxIter(self, newMaxIter: int) -> _AbstractDetector__T:
        """
        Set up the maximum number of iterations in the event time search.
        
        This will override a number of iterations if it has been configured previously.
        
        Parameters:
            newMaxIter (int): maximum number of iterations in the event time search
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        
        """
        ...
    def withThreshold(self, newThreshold: float) -> _AbstractDetector__T:
        """
        Set up the convergence threshold.
        
        This will override a convergence threshold if it has been configured previously.
        
        Parameters:
            newThreshold (double): convergence threshold (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        
        """
        ...

class DetectorModifier(EventDetector):
    """
    Base class for modifying an existing detector.
    
    This class is intended to be a base class for changing behaviour of a wrapped existing detector. This base class delegates all its methods to the wrapped detector. Classes extending it can therefore override only the methods they want to change.
    
    Since:
        13.0
    """
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Specified by: dependsOnTimeOnly in interface EventDetector
        
        Returns:
            flag
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        This method finalizes the event detector's job.
        
        Specified by: finish in interface EventDetector
        
        Parameters:
            state (SpacecraftState): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface EventDetector
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
        Getter for the settings.
        
        Specified by: getDetectionSettings in interface EventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> EventDetector:
        """
        Get the wrapped detector.
        
        Returns:
            wrapped detector
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Get the handler.
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface EventDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface EventDetector
        
        Parameters:
            state (SpacecraftState): current state
            target (AbsoluteDate): target time for the integration
        
        
        """
        ...

_EventSlopeFilter__T = typing.TypeVar('_EventSlopeFilter__T', bound=EventDetector)  # <T>
class EventSlopeFilter(EventDetector, typing.Generic[_EventSlopeFilter__T]):
    """
    Wrapper used to detect only increasing or decreasing events.
    
    This class is heavily based on the class EventFilter from the Hipparchus library. The changes performed consist in replacing raw types (double and double arrays) with space dynamics types (AbsoluteDate, SpacecraftState).
    
    General EventDetector are defined implicitly by a g crossing zero. This function needs to be continuous in the event neighborhood, and its sign must remain consistent between events. This implies that during an orbit propagation, events triggered are alternately events for which the function increases from negative to positive values, and events for which the function decreases from positive to negative values.
    
    Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type. In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of computing time.
    
    Users can wrap a regular EventDetector in an instance of this class and provide this wrapping instance to a Propagator in order to avoid wasting time looking for uninteresting events. The wrapper will intercept the calls to the g and to the eventOccurred method in order to ignore uninteresting events. The wrapped regular EventDetector will then see only the interesting events, i.e. either only increasing events or only decreasing events. The number of calls to the g will also be reduced.
    
    Also see:
        EventEnablingPredicateFilter
    """
    @typing.overload
    def __init__(self, detectionSettings: EventDetectionSettings, rawDetector: _EventSlopeFilter__T, filterType: FilterType): ...
    @typing.overload
    def __init__(self, rawDetector: _EventSlopeFilter__T, filter: FilterType): ...
    def finish(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        This method finalizes the event detector's job.
        
        Specified by: finish in interface EventDetector
        
        Parameters:
            state (SpacecraftState): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface EventDetector
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
        Description copied from interface: getDetectionSettings Getter for the settings.
        
        Specified by: getDetectionSettings in interface EventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> _EventSlopeFilter__T:
        """
        Get the wrapped raw detector.
        
        Returns:
            the wrapped raw detector
        
        Since:
            11.1
        
        
        """
        ...
    def getFilter(self) -> FilterType:
        """
        Deprecated. since 13.0 (use getFilterType) Get filter type.
        
        Returns:
            filter type
        
        
        """
        ...
    def getFilterType(self) -> FilterType:
        """
        Get filter type.
        
        Returns:
            filter type
        
        Since:
            13.0
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Get the handler.
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface EventDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Returns:
            true if the current propagation is forward
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface EventDetector
        
        Parameters:
            state (SpacecraftState): current state
            target (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def withDetectionSettings(self, settings: EventDetectionSettings) -> 'EventSlopeFilter'[_EventSlopeFilter__T]:
        """
        Builds a new instance from the input detection settings.
        
        Parameters:
            settings (EventDetectionSettings): event detection settings to be used
        
        Returns:
            a new detector
        
        
        """
        ...

_FieldAbstractDetector__D = typing.TypeVar('_FieldAbstractDetector__D', bound='FieldAbstractDetector')  # <D>
_FieldAbstractDetector__T = typing.TypeVar('_FieldAbstractDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractDetector(FieldEventDetector[_FieldAbstractDetector__T], typing.Generic[_FieldAbstractDetector__D, _FieldAbstractDetector__T]):
    """
    Common parts shared by several orbital events finders.
    
    Also see:
        addEventDetector
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    Default maximum checking interval (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default convergence threshold (s).
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    Default maximum number of iterations in the event time search.
    
    Also see:
        constant
    
    
    """
    _checkIfForward__W = typing.TypeVar('_checkIfForward__W', bound=org.hipparchus.CalculusFieldElement)  # <W>
    @staticmethod
    def checkIfForward(state: org.orekit.propagation.FieldSpacecraftState[_checkIfForward__W], targetDate: org.orekit.time.FieldAbsoluteDate[_checkIfForward__W]) -> bool:
        """
        Check if propagation is forward or not.
        
        Parameters:
            state (FieldSpacecraftState<W> state): initial state
            targetDate (FieldAbsoluteDate<W> targetDate): target propagation date
        
        Returns:
            forward flag
        
        Since:
            13.0
        
        
        """
        ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldAbstractDetector__T]:
        """
        Getter for the settings.
        
        Specified by: getDetectionSettings in interface FieldEventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldAbstractDetector__T]:
        """
        Get the handler.
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractDetector__T], t: org.orekit.time.FieldAbsoluteDate[_FieldAbstractDetector__T]) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface FieldEventDetector
        
        Parameters:
            s0 (FieldSpacecraftState<FieldAbstractDetector> s0): initial state
            t (FieldAbsoluteDate<FieldAbstractDetector> t): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Returns:
            true if the current propagation is forward
        
        Since:
            7.2
        
        
        """
        ...
    def withDetectionSettings(self, newSettings: FieldEventDetectionSettings[_FieldAbstractDetector__T]) -> _FieldAbstractDetector__D:
        """
        Set up the event detection settings.
        
        This will override settings previously configured.
        
        Parameters:
            newSettings (FieldEventDetectionSettings<FieldAbstractDetector> newSettings): new event detection settings
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.2
        
        
        """
        ...
    def withHandler(self, newHandler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldAbstractDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]) -> _FieldAbstractDetector__D:
        """
        Set up the event handler to call at event occurrences.
        
        This will override a handler if it has been configured previously.
        
        Parameters:
            newHandler (FieldEventHandler<FieldAbstractDetector> newHandler): event handler to call at event occurrences
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: float) -> _FieldAbstractDetector__D:
        """
        Set up the maximum checking interval.
        
        This will override a maximum checking interval if it has been configured previously.
        
        Parameters:
            newMaxCheck (double): maximum checking interval (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        public FieldAbstractDetector withMaxCheck (FieldAdaptableInterval<FieldAbstractDetector> newMaxCheck)
        
        Set up the maximum checking interval.
        
        This will override a maximum checking interval if it has been configured previously.
        
        Parameters:
            newMaxCheck (FieldAdaptableInterval<FieldAbstractDetector> newMaxCheck): maximum checking interval (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: typing.Union[org.orekit.propagation.events.intervals.FieldAdaptableInterval[_FieldAbstractDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], bool], float]]) -> _FieldAbstractDetector__D: ...
    def withMaxIter(self, newMaxIter: int) -> _FieldAbstractDetector__D:
        """
        Set up the maximum number of iterations in the event time search.
        
        This will override a number of iterations if it has been configured previously.
        
        Parameters:
            newMaxIter (int): maximum number of iterations in the event time search
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        
        """
        ...
    def withThreshold(self, newThreshold: _FieldAbstractDetector__T) -> _FieldAbstractDetector__D:
        """
        Set up the convergence threshold.
        
        This will override a convergence threshold if it has been configured previously.
        
        Parameters:
            newThreshold (FieldAbstractDetector): convergence threshold (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        
        """
        ...

_FieldDetectorModifier__T = typing.TypeVar('_FieldDetectorModifier__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDetectorModifier(FieldEventDetector[_FieldDetectorModifier__T], typing.Generic[_FieldDetectorModifier__T]):
    """
    Base class for modifying an existing getDetector().
    
    This class is intended to be a base class for changing behaviour of a wrapped existing getDetector(). This base class delegates all its methods to the wrapped getDetector(). Classes extending it can therefore override only the methods they want to change.
    
    Since:
        13.0
    """
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Specified by: dependsOnTimeOnly in interface FieldEventDetector
        
        Returns:
            flag
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldDetectorModifier__T]) -> None:
        """
        This method finalizes the event detector's job.
        
        Specified by: finish in interface FieldEventDetector
        
        Parameters:
            state (FieldSpacecraftState<FieldDetectorModifier> state): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldDetectorModifier__T]) -> _FieldDetectorModifier__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface FieldEventDetector
        
        Parameters:
            s (FieldSpacecraftState<FieldDetectorModifier> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldDetectorModifier__T]:
        """
        Getter for the settings.
        
        Specified by: getDetectionSettings in interface FieldEventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> FieldEventDetector[_FieldDetectorModifier__T]:
        """
        Getter for wrapped detector.
        
        Returns:
            detector
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldDetectorModifier__T]:
        """
        Get the handler.
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldDetectorModifier__T], t: org.orekit.time.FieldAbsoluteDate[_FieldDetectorModifier__T]) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface FieldEventDetector
        
        Parameters:
            s0 (FieldSpacecraftState<FieldDetectorModifier> s0): initial state
            t (FieldAbsoluteDate<FieldDetectorModifier> t): target time for the integration
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldDetectorModifier__T], target: org.orekit.time.FieldAbsoluteDate[_FieldDetectorModifier__T]) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface FieldEventDetector
        
        Parameters:
            state (FieldSpacecraftState<FieldDetectorModifier> state): current state
            target (FieldAbsoluteDate<FieldDetectorModifier> target): target time for the integration
        
        
        """
        ...

_FieldEventSlopeFilter__D = typing.TypeVar('_FieldEventSlopeFilter__D', bound=FieldEventDetector)  # <D>
_FieldEventSlopeFilter__T = typing.TypeVar('_FieldEventSlopeFilter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventSlopeFilter(FieldEventDetector[_FieldEventSlopeFilter__T], typing.Generic[_FieldEventSlopeFilter__D, _FieldEventSlopeFilter__T]):
    """
    Wrapper used to detect only increasing or decreasing events.
    
    This class is heavily based on the class EventFilter from the Hipparchus library. The changes performed consist in replacing raw types (double and double arrays) with space dynamics types (FieldAbsoluteDate, FieldSpacecraftState).
    
    General FieldEventDetector are defined implicitly by a g crossing zero. This function needs to be continuous in the event neighborhood, and its sign must remain consistent between events. This implies that during an orbit propagation, events triggered are alternately events for which the function increases from negative to positive values, and events for which the function decreases from positive to negative values.
    
    Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type. In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of computing time.
    
    Users can wrap a regular FieldEventDetector in an instance of this class and provide this wrapping instance to a FieldPropagator in order to avoid wasting time looking for uninteresting events. The wrapper will intercept the calls to the g and to the eventOccurred method in order to ignore uninteresting events. The wrapped regular FieldEventDetector will then see only the interesting events, i.e. either only increasing events or only decreasing events. The number of calls to the g will also be reduced.
    
    Also see:
        FieldEventEnablingPredicateFilter
    """
    @typing.overload
    def __init__(self, detectionSettings: FieldEventDetectionSettings[_FieldEventSlopeFilter__T], rawDetector: _FieldEventSlopeFilter__D, filterType: FilterType): ...
    @typing.overload
    def __init__(self, rawDetector: _FieldEventSlopeFilter__D, filterType: FilterType): ...
    def finish(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventSlopeFilter__T]) -> None:
        """
        This method finalizes the event detector's job.
        
        Specified by: finish in interface FieldEventDetector
        
        Parameters:
            state (FieldSpacecraftState<FieldEventSlopeFilter> state): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldEventSlopeFilter__T]) -> _FieldEventSlopeFilter__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface FieldEventDetector
        
        Parameters:
            s (FieldSpacecraftState<FieldEventSlopeFilter> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldEventSlopeFilter__T]:
        """
        Description copied from interface: getDetectionSettings Getter for the settings.
        
        Specified by: getDetectionSettings in interface FieldEventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> _FieldEventSlopeFilter__D:
        """
        Get the wrapped raw detector.
        
        Returns:
            the wrapped raw detector
        
        
        """
        ...
    def getFilterType(self) -> FilterType:
        """
        Get filter type.
        
        Returns:
            filter type
        
        Since:
            13.0
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldEventSlopeFilter__T]:
        """
        Description copied from interface: getHandler Get the handler.
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldEventSlopeFilter__T], t: org.orekit.time.FieldAbsoluteDate[_FieldEventSlopeFilter__T]) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface FieldEventDetector
        
        Parameters:
            s0 (FieldSpacecraftState<FieldEventSlopeFilter> s0): initial state
            t (FieldAbsoluteDate<FieldEventSlopeFilter> t): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Returns:
            true if the current propagation is forward
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventSlopeFilter__T], target: org.orekit.time.FieldAbsoluteDate[_FieldEventSlopeFilter__T]) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface FieldEventDetector
        
        Parameters:
            state (FieldSpacecraftState<FieldEventSlopeFilter> state): current state
            target (FieldAbsoluteDate<FieldEventSlopeFilter> target): target time for the integration
        
        
        """
        ...
    def withDetectionSettings(self, settings: FieldEventDetectionSettings[_FieldEventSlopeFilter__T]) -> 'FieldEventSlopeFilter'[_FieldEventSlopeFilter__D, _FieldEventSlopeFilter__T]:
        """
        Builds a new instance from the input detection settings.
        
        Parameters:
            settings (FieldEventDetectionSettings<FieldEventSlopeFilter> settings): event detection settings to be used
        
        Returns:
            a new detector
        
        
        """
        ...

class PythonEnablingPredicate(EnablingPredicate):
    def __init__(self): ...
    def eventIsEnabled(self, state: org.orekit.propagation.SpacecraftState, eventDetector: EventDetector, g: float) -> bool:
        """
        Compute an event enabling function of state.
        
        Specified by: eventIsEnabled in interface EnablingPredicate
        
        Parameters:
            state (SpacecraftState): current state
            eventDetector (EventDetector): underlying detector
            g (double): value of the underlying detector for the current state
        
        Returns:
            true if the event is enabled (i.e. it can be triggered), false if it should be ignored
        
        
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

class PythonEventDetector(EventDetector):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finish(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        This method finalizes the event detector's job.
        
        Specified by: finish in interface EventDetector
        
        Parameters:
            state (SpacecraftState): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface EventDetector
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Get the handler.
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def getMaxCheckInterval(self) -> org.orekit.propagation.events.intervals.AdaptableInterval:
        """
        Get maximal time interval between switching function checks.
        
        Specified by: getMaxCheckInterval in interface EventDetector
        
        Returns:
            maximal time interval (s) between switching function checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Get maximal number of iterations in the event time search.
        
        Specified by: getMaxIterationCount in interface EventDetector
        
        Returns:
            maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
        Get the convergence threshold in the event time search.
        
        Specified by: getThreshold in interface EventDetector
        
        Returns:
            convergence threshold (s)
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface EventDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...
    def reset(self, state: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface EventDetector
        
        Parameters:
            state (SpacecraftState): current state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class PythonEventDetectorsProvider(EventDetectorsProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

_PythonFieldEnablingPredicate__T = typing.TypeVar('_PythonFieldEnablingPredicate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEnablingPredicate(FieldEnablingPredicate[_PythonFieldEnablingPredicate__T], typing.Generic[_PythonFieldEnablingPredicate__T]):
    def __init__(self): ...
    def eventIsEnabled(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEnablingPredicate__T], detector: FieldEventDetector[_PythonFieldEnablingPredicate__T], g: _PythonFieldEnablingPredicate__T) -> bool:
        """
        Description copied from interface: eventIsEnabled Compute an event enabling function of state.
        
        Specified by: eventIsEnabled in interface FieldEnablingPredicate
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldEnablingPredicate> state): current state
            detector (FieldEventDetector<PythonFieldEnablingPredicate> detector): underlying detector
            g (PythonFieldEnablingPredicate): value of the underlying detector for the current state
        
        Returns:
            true if the event is enabled (i.e. it can be triggered), false if it should be ignored
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

_PythonFieldEventDetector__T = typing.TypeVar('_PythonFieldEventDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEventDetector(FieldEventDetector[_PythonFieldEventDetector__T], typing.Generic[_PythonFieldEventDetector__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finish(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventDetector__T]) -> None:
        """
        Description copied from interface: finish This method finalizes the event detector's job.
        
        Specified by: finish in interface FieldEventDetector
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldEventDetector> state): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventDetector__T]) -> _PythonFieldEventDetector__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface FieldEventDetector
        
        Parameters:
            s (FieldSpacecraftState<PythonFieldEventDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_PythonFieldEventDetector__T]:
        """
        Description copied from interface: getDetectionSettings Getter for the settings.
        
        Specified by: getDetectionSettings in interface FieldEventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_PythonFieldEventDetector__T]:
        """
        Description copied from interface: getHandler Get the handler.
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def getMaxCheckInterval(self) -> org.orekit.propagation.events.intervals.FieldAdaptableInterval[_PythonFieldEventDetector__T]:
        """
        Get maximal time interval between switching function checks.
        
        Specified by: getMaxCheckInterval in interface FieldEventDetector
        
        Returns:
            maximal time interval (s) between switching function checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Get maximal number of iterations in the event time search.
        
        Specified by: getMaxIterationCount in interface FieldEventDetector
        
        Returns:
            maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> _PythonFieldEventDetector__T:
        """
        Get the convergence threshold in the event time search.
        
        Specified by: getThreshold in interface FieldEventDetector
        
        Returns:
            convergence threshold (s)
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventDetector__T], t: org.orekit.time.FieldAbsoluteDate[_PythonFieldEventDetector__T]) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Specified by: init in interface FieldEventDetector
        
        Parameters:
            s0 (FieldSpacecraftState<PythonFieldEventDetector> s0): initial state
            t (FieldAbsoluteDate<PythonFieldEventDetector> t): target time for the integration
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...
    def reset(self, s0: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventDetector__T], t: org.orekit.time.FieldAbsoluteDate[_PythonFieldEventDetector__T]) -> None:
        """
        Description copied from interface: reset Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface FieldEventDetector
        
        Parameters:
            s0 (FieldSpacecraftState<PythonFieldEventDetector> s0): current state
            t (FieldAbsoluteDate<PythonFieldEventDetector> t): target time for the integration
        
        
        """
        ...

_AbstractTopocentricDetector__T = typing.TypeVar('_AbstractTopocentricDetector__T', bound=AbstractDetector)  # <T>
class AbstractTopocentricDetector(AbstractDetector[_AbstractTopocentricDetector__T], typing.Generic[_AbstractTopocentricDetector__T]):
    """
    Abstract class for detectors using a topocentric frame.
    
    Since:
        13.1
    
    Also see:
        TopocentricFrame
    """
    def getTopocentricFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
        Getter for the topocentric frame.
        
        Returns:
            frame
        
        
        """
        ...

class AdapterDetector(DetectorModifier):
    """
    Deprecated. since 13.0. Use DetectorModifier instead. Base class for adapting an existing detector.
    
    This class is intended to be a base class for changing behaviour of a wrapped existing detector. This base class delegates all its methods to the wrapped detector. Classes extending it can therefore override only the methods they want to change.
    
    Since:
        9.3
    """
    def __init__(self, detector: EventDetector):
        """
        Deprecated. Build an adaptor wrapping an existing detector.
        
        Parameters:
            detector (EventDetector): detector to wrap
        
        
        """
        ...
    def getDetector(self) -> EventDetector:
        """
        Deprecated. Get the wrapped detector.
        
        Specified by: getDetector in interface DetectorModifier
        
        Returns:
            wrapped detector
        
        
        """
        ...

class AlignmentDetector(AbstractDetector['AlignmentDetector']):
    """
    Finder for satellite/body alignment events in orbital plane.
    
    This class finds alignment events.
    
    Alignment means the conjunction, with some threshold angle, between the satellite position and the projection in the orbital plane of some body position.
    
    The default handler behavior is to Action propagation when alignment is reached. This can be changed by calling withHandler after construction.
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, double: float, double2: float, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], double3: float): ...
    @typing.overload
    def __init__(self, double: float, orbit: org.orekit.orbits.Orbit, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], double: float): ...
    @typing.overload
    def __init__(self, eventDetectionSettings: EventDetectionSettings, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], double: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function measures the difference between the alignment angle and the angle between the satellite position and the body position projection in the orbital plane.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getAlignAngle(self) -> float:
        """
        Get the alignment angle (rad).
        
        Returns:
            the alignment angle
        
        
        """
        ...
    def getPVCoordinatesProvider(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the body to align.
        
        Returns:
            the body to align
        
        
        """
        ...

class AltitudeDetector(AbstractDetector['AltitudeDetector']):
    """
    Finder for satellite altitude crossing events.
    
    This class finds altitude events (i.e. satellite crossing a predefined altitude level above ground).
    
    The default implementation behavior is to Action propagation when ascending and to Action propagation when descending. This can be changed by calling withHandler after construction.
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, maxCheck: float, altitude: float, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, altitude: float, bodyShape: org.orekit.bodies.BodyShape): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function measures the difference between the current altitude and the threshold altitude.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getAltitude(self) -> float:
        """
        Get the threshold altitude value.
        
        Returns:
            the threshold altitude value (m)
        
        
        """
        ...
    def getBodyShape(self) -> org.orekit.bodies.BodyShape:
        """
        Get the body shape.
        
        Returns:
            the body shape
        
        
        """
        ...

class AngularSeparationDetector(AbstractDetector['AngularSeparationDetector']):
    """
    Detects when spacecraft comes close to a moving beacon, as seen from a moving observer.
    
    The main use case for this detector is when the observer is in fact a ground station, modeled as a TopocentricFrame and when the beacon is the getSun, for computing interferences for the telemetry link. Another similar case is when the beacon is another spacecraft, for interferences computation.
    
    The default handler behavior is to Action propagation when spacecraft enters the proximity zone. This can be changed by calling withHandler after construction.
    
    Since:
        8.0
    
    Also see:
        addEventDetector
    """
    DEFAULT_SETTINGS: typing.ClassVar[EventDetectionSettings] = ...
    """
    Default detection settings.
    """
    def __init__(self, beacon: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], observer: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], proximityAngle: float):
        """
        Build a new angular separation detector.
        
        Parameters:
            beacon (PVCoordinatesProvider): beacon at the center of the proximity zone
            observer (PVCoordinatesProvider): observer for the spacecraft, that may also see the beacon at the same time if they are too close to each other
            proximityAngle (double): proximity angle as seen from observer, at which events are triggered (rad)
        
        protected AngularSeparationDetector (EventDetectionSettings detectionSettings, EventHandler handler, PVCoordinatesProvider beacon, PVCoordinatesProvider observer, double proximityAngle)
        
        Protected constructor with full parameters.
        
        This constructor is not public as users are expected to use the builder API with the various withXxx() methods to set up the instance in a readable manner without using a huge amount of parameters.
        
        Parameters:
            detectionSettings (EventDetectionSettings): detection settings
            handler (EventHandler): event handler to call at event occurrences
            beacon (PVCoordinatesProvider): beacon at the center of the proximity zone
            observer (PVCoordinatesProvider): observer for the spacecraft, that may also see the beacon at the same time if they are too close to each other
            proximityAngle (double): proximity angle as seen from observer, at which events are triggered (rad)
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function.
        
        This function measures the angular separation between beacon and spacecraft as seen from the observer minus the proximity angle. It therefore triggers decreasing events when the spacecraft enters the proximity zone and increasing events when it leaves the proximity zone.
        
        No shadowing effect is taken into account, so this method is computed and may trigger events even when the spacecraft is below horizon for an observer which is a ground station. If such effects must be taken into account the detector must be associated with a EventEnablingPredicateFilter where the EnablingPredicate is based on elevation.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getBeacon(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the beacon at the center of the proximity zone.
        
        Returns:
            beacon at the center of the proximity zone
        
        
        """
        ...
    def getObserver(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the observer for the spacecraft.
        
        Returns:
            observer for the spacecraft
        
        
        """
        ...
    def getProximityAngle(self) -> float:
        """
        Get the proximity angle (rad).
        
        Returns:
            the proximity angle
        
        
        """
        ...

class AngularSeparationFromSatelliteDetector(AbstractDetector['AngularSeparationFromSatelliteDetector']):
    """
    Detects when two moving objects come close to each other, as seen from spacecraft.
    
    The main use case for this detector is when the primary object is in fact a ground station, modeled as a TopocentricFrame and when the secondary is the getSun, for computing optical reflections.
    
    The default handler behavior is to Action propagation when objects enter the proximity zone. This can be changed by calling withHandler after construction.
    
    Since:
        11.0
    
    Also see:
        addEventDetector
    """
    def __init__(self, primaryObject: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], secondaryObject: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], proximityAngle: float):
        """
        Build a new angular detachment detector.
        
        Parameters:
            primaryObject (PVCoordinatesProvider): primaryObject, at the center of the proximity zone
            secondaryObject (PVCoordinatesProvider): secondaryObject, that may come close to the primaryObject as seen from the spacecraft
            proximityAngle (double): proximity angle as seen from spacecraft, at which events are triggered (rad)
        
        protected AngularSeparationFromSatelliteDetector (EventDetectionSettings detectionSettings, EventHandler handler, PVCoordinatesProvider primaryObject, PVCoordinatesProvider secondaryObject, double proximityAngle)
        
        Protected constructor with full parameters.
        
        This constructor is not public as users are expected to use the builder API with the various withXxx() methods to set up the instance in a readable manner without using a huge amount of parameters.
        
        Parameters:
            detectionSettings (EventDetectionSettings): detection Settings
            handler (EventHandler): event handler to call at event occurrences
            primaryObject (PVCoordinatesProvider): primaryObject at the center of the proximity zone
            secondaryObject (PVCoordinatesProvider): secondaryObject, that may come close to the primaryObject as seen from the spacecraft
            proximityAngle (double): proximity angle as seen from secondaryObject, at which events are triggered (rad)
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function.
        
        This function measures the angular separation between primary and secondary objects as seen from the spacecraft minus the proximity angle. It therefore triggers decreasing events when the secondary object enters the proximity zone and increasing events when it leaves the proximity zone.
        
        No shadowing effect is taken into account, so this method is computed and may trigger events even when the secondary object is behind the primary. If such effects must be taken into account the detector must be associated with a EventEnablingPredicateFilter where the EnablingPredicate is based on eclipse conditions.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getPrimaryObject(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the primaryObject, at the center of the proximity zone.
        
        Returns:
            primaryObject
        
        
        """
        ...
    def getProximityAngle(self) -> float:
        """
        Get the proximity angle (rad).
        
        Returns:
            the proximity angle
        
        
        """
        ...
    def getSecondaryObject(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the secondaryObject.
        
        Returns:
            secondaryObject
        
        
        """
        ...

class ApsideDetector(AbstractDetector['ApsideDetector']):
    """
    Finder for apside crossing events.
    
    This class finds apside crossing events (i.e. apogee or perigee crossing).
    
    The default implementation behavior is to Action propagation at apogee crossing and to Action propagation at perigee crossing. This can be changed by calling withHandler after construction.
    
    Beware that apside detection will fail for almost circular orbits. If for example an apside detector is used to trigger an ImpulseManeuver and the maneuver change the orbit shape to circular, then the detector may completely fail just after the maneuver has been performed!
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, eventDetectionSettings: EventDetectionSettings, eventHandler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function computes the dot product of the 2 vectors : position.velocity.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...

class BetaAngleDetector(AbstractDetector['BetaAngleDetector']):
    """
    Finder for beta angle crossing events.
    
    Locate events when the beta angle (the angle between the orbit plane and the celestial body) crosses a threshold. The g function is negative when the beta angle is above the threshold and positive when the beta angle is below the threshold.
    
    The inertial frame provided must have it's origin centered at the satellite's orbit plane. The beta angle is computed as the angle between the celestial body's position in this frame with the satellite's orbital momentum vector.
    
    The default implementation behavior is to Action propagation at the first event date occurrence. This can be changed by calling withHandler after construction.
    
    Since:
        12.1
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, betaAngleThreshold: float): ...
    @typing.overload
    def __init__(self, betaAngleThreshold: float, celestialBodyProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame): ...
    @typing.overload
    @staticmethod
    def calculateBetaAngle(state: org.orekit.propagation.SpacecraftState, celestialBodyProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]) -> float:
        """
        Calculate the beta angle between the orbit plane and the celestial body.
        
        This method computes the beta angle using the frame from the spacecraft state.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            celestialBodyProvider (PVCoordinatesProvider): celestial body coordinate provider
        
        Returns:
            the beta angle (radians)
        
        Calculate the beta angle between the orbit plane and the celestial body.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            celestialBodyProvider (PVCoordinatesProvider): celestial body coordinate provider
            frame (Frame): inertial frame in which beta angle will be computed
        
        Returns:
            the beta angle (radians)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def calculateBetaAngle(state: org.orekit.propagation.SpacecraftState, celestialBodyProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], frame: org.orekit.frames.Frame) -> float: ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getBetaAngleThreshold(self) -> float:
        """
        The beta angle threshold (radians).
        
        Returns:
            the beta angle threshold (radians)
        
        
        """
        ...
    def getCelestialBodyProvider(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Coordinate provider for the celestial body.
        
        Returns:
            celestial body's coordinate provider
        
        
        """
        ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
        The inertial frame in which beta angle is computed.
        
        Returns:
            the inertial frame
        
        
        """
        ...
    def withBetaThreshold(self, newBetaAngleThreshold: float) -> 'BetaAngleDetector':
        """
        Create a new instance with the provided beta angle threshold.
        
        This method does not change the current instance.
        
        Parameters:
            newBetaAngleThreshold (double): the beta angle threshold (radians)
        
        Returns:
            the new detector instance
        
        
        """
        ...
    def withCelestialProvider(self, newProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]) -> 'BetaAngleDetector':
        """
        Create a new instance with the provided coordinate provider.
        
        This method does not change the current instance.
        
        Parameters:
            newProvider (PVCoordinatesProvider): the new coordinate provider
        
        Returns:
            the new detector instance
        
        
        """
        ...
    def withInertialFrame(self, newFrame: org.orekit.frames.Frame) -> 'BetaAngleDetector':
        """
        Create a new instance with the provided inertial frame.
        
        This method does not change the current instance.
        
        Parameters:
            newFrame (Frame): the inertial frame
        
        Returns:
            the new detector instance
        
        
        """
        ...

class BooleanDetector(AbstractDetector['BooleanDetector']):
    """
    This class provides AND and OR operations for event detectors. This class treats positive values of the g function as true and negative values as false.
    
    One example for an imaging satellite might be to only detect events when a satellite is overhead (elevation > 0) AND when the ground point is sunlit (Sun elevation > 0). Another slightly contrived example using the OR operator would be to detect access to a set of ground stations and only report events when the satellite enters or leaves the field of view of the set, but not hand-offs between the ground stations.
    
    For the BooleanDetector is important that the sign of the g function of the underlying event detector is not arbitrary, but has a semantic meaning, e.g. in or out, true or false. This class works well with event detectors that detect entry to or exit from a region, e.g. EclipseDetector, ElevationDetector, LatitudeCrossingDetector. Using this detector with detectors that are not based on entry to or exit from a region, e.g. DateDetector, LongitudeCrossingDetector, will likely lead to unexpected results. To apply conditions to this latter type of event detectors a EventEnablingPredicateFilter is usually more appropriate.
    
    Also see:
        andCombine,
        orCombine,
        notCombine,
        EventEnablingPredicateFilter,
        EventSlopeFilter
    """
    @typing.overload
    @staticmethod
    def andCombine(detectors: typing.Union[java.util.Collection[EventDetector], typing.Sequence[EventDetector], typing.Set[EventDetector]]) -> 'BooleanDetector':
        """
        Create a new event detector that is the logical AND of the given event detectors.
        
        The created event detector's g function is positive if and only if the g functions of all detectors in detectors are positive.
        
        The starting interval, threshold, and iteration count are set to the most stringent (minimum) of all the detectors. The event handlers of the underlying detectors are not used, instead the default handler is ContinueOnEvent.
        
        Parameters:
            detectors (EventDetector...): the operands. Must contain at least one detector.
        
        Returns:
            a new event detector that is the logical AND of the operands.
        
        Raises:
            NoSuchElementException: if detectors is empty.
        
        Also see:
            BooleanDetector,
            andCombine,
            orCombine,
            notCombine
        
        public static BooleanDetector andCombine (Collection<? extends EventDetector> detectors)
        
        Create a new event detector that is the logical AND of the given event detectors.
        
        The created event detector's g function is positive if and only if the g functions of all detectors in detectors are positive.
        
        The starting interval, threshold, and iteration count are set to the most stringent (minimum) of the detectors. The event handlers of the underlying detectors are not used, instead the default handler is ContinueOnEvent.
        
        Parameters:
            detectors (Collection<? extends EventDetector> detectors): the operands. Must contain at least one detector.
        
        Returns:
            a new event detector that is the logical AND of the operands.
        
        Raises:
            NoSuchElementException: if detectors is empty.
        
        Also see:
            BooleanDetector,
            andCombine,
            orCombine,
            notCombine
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def andCombine(*detectors: EventDetector) -> 'BooleanDetector': ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Description copied from interface: dependsOnTimeOnly Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Description copied from interface: finish This method finalizes the event detector's job.
        
        Parameters:
            state (SpacecraftState): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectors(self) -> java.util.List[EventDetector]:
        """
        Get the list of original detectors.
        
        Returns:
            the list of original detectors
        
        Since:
            10.2
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Description copied from class: init Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface EventDetector
        
        Overrides: init in class AbstractDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    @staticmethod
    def notCombine(detector: EventDetector) -> 'NegateDetector':
        """
        Create a new event detector that negates the g function of another detector.
        
        This detector will be initialized with the same getMaxCheckInterval, getThreshold, and getMaxIterationCount as detector. The event handler of the underlying detector is not used, instead the default handler is ContinueOnEvent.
        
        Parameters:
            detector (EventDetector): to negate.
        
        Returns:
            a new event detector whose g function is the same magnitude but opposite sign of detector.
        
        Also see:
            andCombine,
            orCombine,
            BooleanDetector
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def orCombine(detectors: typing.Union[java.util.Collection[EventDetector], typing.Sequence[EventDetector], typing.Set[EventDetector]]) -> 'BooleanDetector':
        """
        Create a new event detector that is the logical OR of the given event detectors.
        
        The created event detector's g function is positive if and only if at least one of g functions of the event detectors in detectors is positive.
        
        The starting interval, threshold, and iteration count are set to the most stringent (minimum) of the detectors. The event handlers of the underlying EventDetectors are not used, instead the default handler is ContinueOnEvent.
        
        Parameters:
            detectors (EventDetector...): the operands. Must contain at least one detector.
        
        Returns:
            a new event detector that is the logical OR of the operands.
        
        Raises:
            NoSuchElementException: if detectors is empty.
        
        Also see:
            BooleanDetector,
            orCombine,
            andCombine,
            notCombine
        
        public static BooleanDetector orCombine (Collection<? extends EventDetector> detectors)
        
        Create a new event detector that is the logical OR of the given event detectors.
        
        The created event detector's g function is positive if and only if at least one of g functions of the event detectors in detectors is positive.
        
        The starting interval, threshold, and iteration count are set to the most stringent (minimum) of the detectors. The event handlers of the underlying EventDetectors are not used, instead the default handler is ContinueOnEvent.
        
        Parameters:
            detectors (Collection<? extends EventDetector> detectors): the operands. Must contain at least one detector.
        
        Returns:
            a new event detector that is the logical OR of the operands.
        
        Raises:
            NoSuchElementException: if detectors is empty.
        
        Also see:
            BooleanDetector,
            orCombine,
            andCombine,
            notCombine
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def orCombine(*detectors: EventDetector) -> 'BooleanDetector': ...
    def reset(self, state: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Description copied from interface: reset Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Parameters:
            state (SpacecraftState): current state
            target (AbsoluteDate): target time for the integration
        
        
        """
        ...

class CylindricalShadowEclipseDetector(AbstractDetector['CylindricalShadowEclipseDetector']):
    """
    Event detector for eclipses from a single, infinitely-distant light source, occulted by a spherical central body. The shadow region is cylindrical, a model less accurate than a conical one but more computationally-performant.
    
    The so-called g function is negative in eclipse, positive otherwise.
    
    Since:
        12.1
    
    Also see:
        EclipseDetector
    """
    @typing.overload
    def __init__(self, sun: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], occultingBodyRadius: float, eventDetectionSettings: EventDetectionSettings, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]): ...
    @typing.overload
    def __init__(self, sun: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], occultingBodyRadius: float, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getOccultingBodyRadius(self) -> float:
        """
        Getter for occulting body radius.
        
        Returns:
            radius
        
        
        """
        ...

class DateDetector(AbstractDetector['DateDetector'], org.orekit.time.TimeStamped):
    """
    Finder for date events.
    
    This class finds date events (i.e. occurrence of some predefined dates).
    
    As of version 5.1, it is an enhanced date detector:
    
      - it can be defined without prior date ()
      - several dates can be added (addEventDate)
    
    The gap between the added dates must be more than the minGap.
    
    The default implementation behavior is to Action propagation at the first event date occurrence. This can be changed by calling withHandler after construction.
    
    Also see:
        addEventDetector
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    Default value for max check.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    DEFAULT_MIN_GAP: typing.ClassVar[float] = ...
    """
    Default value for minimum gap between added dates.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default value for convergence threshold.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate): ...
    @typing.overload
    def __init__(self, double: float, *timeStamped: typing.Union[org.orekit.time.TimeStamped, typing.Callable]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate): ...
    @typing.overload
    def __init__(self, *timeStamped: typing.Union[org.orekit.time.TimeStamped, typing.Callable]): ...
    def addEventDate(self, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Add an event date.
        
        The date to add must be:
        
          - less than the smallest already registered event date minus the maxCheck
          - or more than the largest already registered event date plus the maxCheck
        
        
        Parameters:
            target (AbsoluteDate): target date
        
        Raises:
            IllegalArgumentException: if the date is too close from already defined interval
        
        
        """
        ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Specified by: dependsOnTimeOnly in interface EventDetector
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function measures the difference between the current and the target date.
        
        Specified by: g in interface EventDetector
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the current event date according to the propagator.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            event date
        
        
        """
        ...
    def getDates(self) -> java.util.List[org.orekit.time.TimeStamped]:
        """
        Get all event dates currently managed, in chronological order.
        
        Returns:
            all event dates currently managed, in chronological order
        
        Since:
            11.1
        
        
        """
        ...
    def getMinGap(self) -> float:
        """
        Get the minimum gap between added dates.
        
        Returns:
            the minimum gap between added dates (s)
        
        
        """
        ...
    def withMinGap(self, newMinGap: float) -> 'DateDetector':
        """
        Setup minimum gap between added dates.
        
        Parameters:
            newMinGap (double): new minimum gap between added dates
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        
        """
        ...

class EclipseDetector(AbstractDetector['EclipseDetector']):
    """
    Finder for satellite eclipse related events.
    
    This class finds eclipse events, i.e. satellite within umbra (total eclipse) or penumbra (partial eclipse).
    
    The occulted body is given through a PVCoordinatesProvider and its radius in meters. It is modeled as a sphere.
    
    Since v10.0 the occulting body is a OneAxisEllipsoid, before it was modeled as a sphere.
    
    It was changed to precisely model Solar eclipses by the Earth, especially for Low Earth Orbits.
    
    If you want eclipses by a spherical occulting body, set its flattening to 0. when defining its OneAxisEllipsoid model..
    
    The withUmbra or withPenumbra methods will tell you if the event is triggered when complete umbra/lighting is achieved or when entering/living the penumbra zone.
    
    The default behavior is detecting complete umbra/lighting events.
    
    If you want to have both, you'll need to set up two distinct detectors.
    
    The default implementation behavior is to Action propagation when entering the eclipse and to Action propagation when exiting the eclipse.
    
    This can be changed by calling withHandler after construction.
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, occulted: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], occultedRadius: float, occulting: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, occultationEngine: org.orekit.utils.OccultationEngine): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function becomes negative when entering the region of shadow and positive when exiting.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getMargin(self) -> float:
        """
        Get the angular margin used for eclipse detection.
        
        Returns:
            angular margin used for eclipse detection (rad)
        
        Since:
            12.0
        
        
        """
        ...
    def getOccultationEngine(self) -> org.orekit.utils.OccultationEngine:
        """
        Get the occultation engine.
        
        Returns:
            occultation engine
        
        Since:
            12.0
        
        
        """
        ...
    def getTotalEclipse(self) -> bool:
        """
        Get the total eclipse detection flag.
        
        Returns:
            the total eclipse detection flag (true for umbra events detection, false for penumbra events detection)
        
        
        """
        ...
    def withMargin(self, newMargin: float) -> 'EclipseDetector':
        """
        Setup a margin to angle detection.
        
        A positive margin implies eclipses are "larger" hence entry occurs earlier and exit occurs later than a detector with 0 margin.
        
        Parameters:
            newMargin (double): angular margin to apply to eclipse detection (rad)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        
        """
        ...
    def withPenumbra(self) -> 'EclipseDetector':
        """
        Setup the detector to penumbra detection.
        
        This will override a penumbra/umbra flag if it has been configured previously.
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            withUmbra
        
        
        """
        ...
    def withUmbra(self) -> 'EclipseDetector':
        """
        Setup the detector to full umbra detection.
        
        This will override a penumbra/umbra flag if it has been configured previously.
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            withPenumbra
        
        
        """
        ...

class EventEnablingPredicateFilter(DetectorModifier):
    """
    Wrapper used to detect events only when enabled by an external predicated function.
    
    General EventDetector are defined implicitly by a g crossing zero. This implies that during an orbit propagation, events are triggered at all zero crossings.
    
    Sometimes, users would like to enable or disable events by themselves, for example to trigger them only for certain orbits, or to check elevation maximums only when elevation itself is positive (i.e. they want to discard elevation maximums below ground). In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of computing time.
    
    Users can wrap a regular EventDetector in an instance of this class and provide this wrapping instance to a Propagator in order to avoid wasting time looking for uninteresting events. The wrapper will intercept the calls to the g and to the eventOccurred method in order to ignore uninteresting events. The wrapped regular EventDetector will the see only the interesting events, i.e. either only events that occur when a user-provided event enabling predicate function is true, ignoring all events that occur when the event enabling predicate function is false. The number of calls to the g will also be reduced.
    
    Since:
        7.1
    
    Also see:
        EventSlopeFilter
    """
    @typing.overload
    def __init__(self, detectionSettings: EventDetectionSettings, rawDetector: EventDetector, enabler: typing.Union[EnablingPredicate, typing.Callable]): ...
    @typing.overload
    def __init__(self, rawDetector: EventDetector, enabler: typing.Union[EnablingPredicate, typing.Callable]): ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Specified by: dependsOnTimeOnly in interface DetectorModifier
        
        Specified by: dependsOnTimeOnly in interface EventDetector
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface DetectorModifier
        
        Specified by: g in interface EventDetector
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
        Getter for the settings.
        
        Specified by: getDetectionSettings in interface DetectorModifier
        
        Specified by: getDetectionSettings in interface EventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> EventDetector:
        """
        Get the wrapped raw detector.
        
        Specified by: getDetector in interface DetectorModifier
        
        Returns:
            the wrapped raw detector
        
        Since:
            11.1
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Get the handler.
        
        Specified by: getHandler in interface DetectorModifier
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def getPredicate(self) -> EnablingPredicate:
        """
        Getter for the enabling predicate.
        
        Returns:
            predicate
        
        Since:
            13.1
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface DetectorModifier
        
        Specified by: init in interface EventDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Returns:
            true if the current propagation is forward
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface DetectorModifier
        
        Specified by: reset in interface EventDetector
        
        Parameters:
            state (SpacecraftState): current state
            target (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def withDetectionSettings(self, settings: EventDetectionSettings) -> 'EventEnablingPredicateFilter':
        """
        Builds a new instance from the input detection settings.
        
        Parameters:
            settings (EventDetectionSettings): event detection settings to be used
        
        Returns:
            a new detector
        
        
        """
        ...

class EventShifter(DetectorModifier):
    """
    Wrapper shifting events occurrences times.
    
    This class wraps an EventDetector to slightly shift the events occurrences times. A typical use case is for handling operational delays before or after some physical event really occurs.
    
    For example, the satellite attitude mode may be switched from sun pointed to spin-stabilized a few minutes before eclipse entry, and switched back to sun pointed a few minutes after eclipse exit. This behavior is handled by wrapping an EclipseDetector into an instance of this class with a positive times shift for increasing events (eclipse exit) and a negative times shift for decreasing events (eclipse entry).
    
    Also see:
        addEventDetector, EventDetector
    """
    @typing.overload
    def __init__(self, detectionSettings: EventDetectionSettings, detector: EventDetector, useShiftedStates: bool, increasingTimeShift: float, decreasingTimeShift: float): ...
    @typing.overload
    def __init__(self, detector: EventDetector, useShiftedStates: bool, increasingTimeShift: float, decreasingTimeShift: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface DetectorModifier
        
        Specified by: g in interface EventDetector
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDecreasingTimeShift(self) -> float:
        """
        Get the decreasing events time shift.
        
        Returns:
            decreasing events time shift
        
        
        """
        ...
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
        Getter for the settings.
        
        Specified by: getDetectionSettings in interface DetectorModifier
        
        Specified by: getDetectionSettings in interface EventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> EventDetector:
        """
        Get the detector for the raw unshifted event.
        
        Specified by: getDetector in interface DetectorModifier
        
        Returns:
            the detector for the raw unshifted event
        
        Since:
            11.1
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Get the handler.
        
        Specified by: getHandler in interface DetectorModifier
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def getIncreasingTimeShift(self) -> float:
        """
        Get the increasing events time shift.
        
        Returns:
            increasing events time shift
        
        
        """
        ...
    def withDetectionSettings(self, settings: EventDetectionSettings) -> 'EventShifter':
        """
        Builds a new instance from the input detection settings.
        
        Parameters:
            settings (EventDetectionSettings): event detection settings to be used
        
        Returns:
            a new detector
        
        
        """
        ...

class ExtremumAngularSeparationDetector(AbstractDetector['ExtremumAngularSeparationDetector']):
    """
    Detector of local extrema with angular separation.
    
    Since:
        13.1
    
    Also see:
        AngularSeparationDetector
    """
    def __init__(self, detectionSettings: EventDetectionSettings, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable], beacon: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], observer: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]):
        """
        Protected constructor with full parameters.
        
        Parameters:
            detectionSettings (EventDetectionSettings): detection settings
            handler (EventHandler): event handler to call at event occurrences
            beacon (ExtendedPositionProvider): beacon at the center of the proximity zone
            observer (ExtendedPositionProvider): observer for the spacecraft, that may also see the beacon at the same time if they are too close to each other
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getBeacon(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Get the beacon at the center of the proximity zone.
        
        Returns:
            beacon at the center of the proximity zone
        
        
        """
        ...
    def getObserver(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Get the observer for the spacecraft.
        
        Returns:
            observer for the spacecraft
        
        
        """
        ...

class ExtremumApproachDetector(AbstractDetector['ExtremumApproachDetector']):
    """
    Finder for extremum approach events.
    
    This class finds extremum approach events (i.e. closest or farthest approach).
    
    The default implementation behavior is to Action propagation at farthest approach and to Action propagation at closest approach. This can be changed by calling withHandler after construction (go to the end of the documentation to see an example).
    
    As this detector needs two objects (moving relative to each other), it embeds one PVCoordinatesProvider for the secondary object and is registered as an event detector in the propagator of the primary object. The secondary object PVCoordinatesProvider will therefore be driven by this detector (and hence by the propagator in which this detector is registered).
    
    **In order to avoid infinite recursion, care must be taken to have the secondary object provider being completely independent from anything else. In particular, if the provider is a propagator, it should not be run together in a PropagatorsParallelizer with the propagator this detector is registered in. It is fine however to configure two separate propagators PsA and PsB with similar settings for the secondary object and one propagator Pm for the primary object and then use Psa in this detector registered within Pm while Pm and Psb are run in the context of a PropagatorsParallelizer.**
    
    For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally costly.
    
    Also, it is possible to detect solely one type of event using an EventSlopeFilter. For example in order to only detect closest approach, one should type the following :
    
    
     ExtremumApproachDetector extremumApproachDetector = new ExtremumApproachDetector(secondaryPVProvider);
     EventDetector closeApproachDetector = new EventSlopeFilter<ExtremumApproachDetector>(extremumApproachDetector,FilterType.TRIGGER_ONLY_INCREASING_EVENTS);
      
     
    
    Since:
        11.3
    
    Also see:
        addEventDetector, EventSlopeFilter,
        FilterType
    """
    def __init__(self, secondaryPVProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]):
        """
        Constructor with default values.
        
        By default, the implemented behavior is to Action propagation at farthest approach and to Action propagation at closest approach.
        
        Parameters:
            secondaryPVProvider (PVCoordinatesProvider): PVCoordinates provider of the other object with which we want to find out the extremum approach.
        
        protected ExtremumApproachDetector (EventDetectionSettings detectionSettings, EventHandler handler, PVCoordinatesProvider secondaryPVProvider)
        
        Constructor.
        
        This constructor is to be used if the user wants to change the default behavior of the detector.
        
        Parameters:
            detectionSettings (EventDetectionSettings): Detection settings.
            handler (EventHandler): Event handler to call at event occurrences.
            secondaryPVProvider (PVCoordinatesProvider): PVCoordinates provider of the other object with which we want to find out the extremum approach.
        
        Since:
            13.0
        
        Also see:
            EventHandler
        
        
        """
        ...
    def computeDeltaPV(self, s: org.orekit.propagation.SpacecraftState) -> org.orekit.utils.PVCoordinates:
        """
        Compute the relative PV between primary and secondary objects.
        
        Parameters:
            s (SpacecraftState): Spacecraft state.
        
        Returns:
            Relative position between primary (=s) and secondaryPVProvider.
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        The g is positive when the primary object is getting further away from the secondary object and is negative when it is getting closer to it.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getSecondaryPVProvider(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the secondary position-velocity provider stored in this instance.
        
        Returns:
            the secondary position-velocity provider stored in this instance
        
        
        """
        ...

_FieldAbstractTopocentricDetector__D = typing.TypeVar('_FieldAbstractTopocentricDetector__D', bound=FieldAbstractDetector)  # <D>
_FieldAbstractTopocentricDetector__T = typing.TypeVar('_FieldAbstractTopocentricDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractTopocentricDetector(FieldAbstractDetector[_FieldAbstractTopocentricDetector__D, _FieldAbstractTopocentricDetector__T], typing.Generic[_FieldAbstractTopocentricDetector__D, _FieldAbstractTopocentricDetector__T]):
    """
    Abstract class for detectors using a topocentric frame.
    
    Since:
        13.1
    
    Also see:
        AbstractTopocentricDetector, TopocentricFrame
    """
    def getTopocentricFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
        Getter for the topocentric frame.
        
        Returns:
            frame
        
        
        """
        ...

_FieldAdapterDetector__T = typing.TypeVar('_FieldAdapterDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdapterDetector(FieldDetectorModifier[_FieldAdapterDetector__T], typing.Generic[_FieldAdapterDetector__T]):
    """
    Deprecated. since 13.0. Use FieldDetectorModifier instead. Base class for adapting an existing detector.
    
    This class is intended to be a base class for changing behaviour of a wrapped existing detector. This base class delegates all its methods to the wrapped detector. Classes extending it can therefore override only the methods they want to change.
    
    Since:
        12.0
    """
    def __init__(self, detector: FieldEventDetector[_FieldAdapterDetector__T]):
        """
        Deprecated. Build an adaptor wrapping an existing detector.
        
        Parameters:
            detector (FieldEventDetector<FieldAdapterDetector> detector): detector to wrap
        
        
        """
        ...
    def getDetector(self) -> FieldEventDetector[_FieldAdapterDetector__T]:
        """
        Deprecated. Get the wrapped detector.
        
        Specified by: getDetector in interface FieldDetectorModifier
        
        Returns:
            wrapped detector
        
        
        """
        ...

_FieldAltitudeDetector__T = typing.TypeVar('_FieldAltitudeDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAltitudeDetector(FieldAbstractDetector['FieldAltitudeDetector'[_FieldAltitudeDetector__T], _FieldAltitudeDetector__T], typing.Generic[_FieldAltitudeDetector__T]):
    """
    Finder for satellite altitude crossing events.
    
    This class finds altitude events (i.e. satellite crossing a predefined altitude level above ground).
    
    The default implementation behavior is to Action propagation when ascending and to Action propagation when descending. This can be changed by calling withHandler after construction.
    
    Since:
        9.0
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, t: _FieldAltitudeDetector__T, t2: _FieldAltitudeDetector__T, t3: _FieldAltitudeDetector__T, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, maxCheck: _FieldAltitudeDetector__T, altitude: _FieldAltitudeDetector__T, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, altitude: _FieldAltitudeDetector__T, bodyShape: org.orekit.bodies.BodyShape): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldAltitudeDetector__T]) -> _FieldAltitudeDetector__T:
        """
        Compute the value of the switching function. This function measures the difference between the current altitude and the threshold altitude.
        
        Parameters:
            s (FieldSpacecraftState<FieldAltitudeDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getAltitude(self) -> _FieldAltitudeDetector__T:
        """
        Get the threshold altitude value.
        
        Returns:
            the threshold altitude value (m)
        
        
        """
        ...
    def getBodyShape(self) -> org.orekit.bodies.BodyShape:
        """
        Get the body shape.
        
        Returns:
            the body shape
        
        
        """
        ...

_FieldAngularSeparationDetector__T = typing.TypeVar('_FieldAngularSeparationDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAngularSeparationDetector(FieldAbstractDetector['FieldAngularSeparationDetector'[_FieldAngularSeparationDetector__T], _FieldAngularSeparationDetector__T], typing.Generic[_FieldAngularSeparationDetector__T]):
    """
    Detects when spacecraft comes close to a moving beacon, as seen from a moving observer.
    
    The main use case for this detector is when the observer is in fact a ground station, modeled as a TopocentricFrame and when the beacon is the getSun, for computing interferences for the telemetry link. Another similar case is when the beacon is another spacecraft, for interferences computation.
    
    The default handler behavior is to Action propagation when spacecraft enters the proximity zone. This can be changed by calling after construction.
    
    Since:
        13.1
    
    Also see:
        addEventDetector,
        AngularSeparationDetector
    """
    def __init__(self, beacon: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], observer: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], proximityAngle: _FieldAngularSeparationDetector__T):
        """
        Build a new angular separation detector.
        
        Parameters:
            beacon (ExtendedPositionProvider): beacon at the center of the proximity zone
            observer (ExtendedPositionProvider): observer for the spacecraft, that may also see the beacon at the same time if they are too close to each other
            proximityAngle (FieldAngularSeparationDetector): proximity angle as seen from observer, at which events are triggered (rad)
        
        protected FieldAngularSeparationDetector (FieldEventDetectionSettings<FieldAngularSeparationDetector> detectionSettings, FieldEventHandler<FieldAngularSeparationDetector> handler, ExtendedPositionProvider beacon, ExtendedPositionProvider observer, FieldAngularSeparationDetector proximityAngle)
        
        Protected constructor with full parameters.
        
        This constructor is not public as users are expected to use the builder API with the various withXxx() methods to set up the instance in a readable manner without using a huge amount of parameters.
        
        Parameters:
            detectionSettings (FieldEventDetectionSettings<FieldAngularSeparationDetector> detectionSettings): detection settings
            handler (FieldEventHandler<FieldAngularSeparationDetector> handler): event handler to call at event occurrences
            beacon (ExtendedPositionProvider): beacon at the center of the proximity zone
            observer (ExtendedPositionProvider): observer for the spacecraft, that may also see the beacon at the same time if they are too close to each other
            proximityAngle (FieldAngularSeparationDetector): proximity angle as seen from observer, at which events are triggered (rad)
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldAngularSeparationDetector__T]) -> _FieldAngularSeparationDetector__T:
        """
        Compute the value of the switching function.
        
        This function measures the angular separation between beacon and spacecraft as seen from the observer minus the proximity angle. It therefore triggers decreasing events when the spacecraft enters the proximity zone and increasing events when it leaves the proximity zone.
        
        No shadowing effect is taken into account, so this method is computed and may trigger events even when the spacecraft is below horizon for an observer which is a ground station. If such effects must be taken into account the detector must be associated with a EventEnablingPredicateFilter where the EnablingPredicate is based on elevation.
        
        Parameters:
            s (FieldSpacecraftState<FieldAngularSeparationDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getBeacon(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Get the beacon at the center of the proximity zone.
        
        Returns:
            beacon at the center of the proximity zone
        
        
        """
        ...
    def getObserver(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Get the observer for the spacecraft.
        
        Returns:
            observer for the spacecraft
        
        
        """
        ...
    def getProximityAngle(self) -> _FieldAngularSeparationDetector__T:
        """
        Get the proximity angle (rad).
        
        Returns:
            the proximity angle
        
        
        """
        ...

_FieldApsideDetector__T = typing.TypeVar('_FieldApsideDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldApsideDetector(FieldAbstractDetector['FieldApsideDetector'[_FieldApsideDetector__T], _FieldApsideDetector__T], typing.Generic[_FieldApsideDetector__T]):
    """
    Finder for apside crossing events.
    
    This class finds apside crossing events (i.e. apogee or perigee crossing).
    
    The default implementation behavior is to Action propagation at apogee crossing and to Action propagation at perigee crossing. This can be changed by calling withHandler after construction.
    
    Beware that apside detection will fail for almost circular orbits. If for example an apside detector is used to trigger an ImpulseManeuver and the maneuver change the orbit shape to circular, then the detector may completely fail just after the maneuver has been performed!
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, t: _FieldApsideDetector__T): ...
    @typing.overload
    def __init__(self, t: _FieldApsideDetector__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldApsideDetector__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldApsideDetector__T]): ...
    @typing.overload
    def __init__(self, fieldEventDetectionSettings: FieldEventDetectionSettings[_FieldApsideDetector__T], fieldEventHandler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldApsideDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldApsideDetector__T]) -> _FieldApsideDetector__T:
        """
        Compute the value of the switching function. This function computes the dot product of the 2 vectors : position.velocity.
        
        Parameters:
            s (FieldSpacecraftState<FieldApsideDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...

_FieldBetaAngleDetector__T = typing.TypeVar('_FieldBetaAngleDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBetaAngleDetector(FieldAbstractDetector['FieldBetaAngleDetector'[_FieldBetaAngleDetector__T], _FieldBetaAngleDetector__T], typing.Generic[_FieldBetaAngleDetector__T]):
    """
    Finder for beta angle crossing events.
    
    Locate events when the beta angle (the angle between the orbit plane and the celestial body) crosses a threshold. The g function is negative when the beta angle is above the threshold and positive when the beta angle is below the threshold.
    
    The inertial frame provided must have it's origin centered at the satellite's orbit plane. The beta angle is computed as the angle between the celestial body's position in this frame with the satellite's orbital momentum vector.
    
    The default implementation behavior is to Action propagation at the first event date occurrence. This can be changed by calling withHandler after construction.
    
    Since:
        12.1
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, betaAngleThreshold: _FieldBetaAngleDetector__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldBetaAngleDetector__T], betaAngleThreshold: _FieldBetaAngleDetector__T, celestialBodyProvider: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_FieldBetaAngleDetector__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], inertialFrame: org.orekit.frames.Frame): ...
    _calculateBetaAngle_0__T = typing.TypeVar('_calculateBetaAngle_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _calculateBetaAngle_1__T = typing.TypeVar('_calculateBetaAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def calculateBetaAngle(state: org.orekit.propagation.FieldSpacecraftState[_calculateBetaAngle_0__T], celestialBodyProvider: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_calculateBetaAngle_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]]) -> _calculateBetaAngle_0__T:
        """
        Calculate the beta angle between the orbit plane and the celestial body.
        
        This method computes the beta angle using the frame from the spacecraft state.
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            celestialBodyProvider (FieldPVCoordinatesProvider<T> celestialBodyProvider): celestial body coordinate provider
        
        Returns:
            the beta angle (radians)
        
        """
        ...
    @typing.overload
    @staticmethod
    def calculateBetaAngle(state: org.orekit.propagation.FieldSpacecraftState[_calculateBetaAngle_1__T], celestialBodyProvider: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_calculateBetaAngle_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], frame: org.orekit.frames.Frame) -> _calculateBetaAngle_1__T:
        """
        Calculate the beta angle between the orbit plane and the celestial body.
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            celestialBodyProvider (FieldPVCoordinatesProvider<T> celestialBodyProvider): celestial body coordinate provider
            frame (Frame): inertial frame in which beta angle will be computed
        
        Returns:
            the beta angle (radians)
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldBetaAngleDetector__T]) -> _FieldBetaAngleDetector__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<FieldBetaAngleDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getBetaAngleThreshold(self) -> _FieldBetaAngleDetector__T:
        """
        The beta angle threshold (radians).
        
        Returns:
            the beta angle threshold (radians)
        
        
        """
        ...
    def getCelestialBodyProvider(self) -> org.orekit.utils.FieldPVCoordinatesProvider[_FieldBetaAngleDetector__T]:
        """
        Coordinate provider for the celestial body.
        
        Returns:
            celestial body's coordinate provider
        
        
        """
        ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
        The inertial frame in which beta angle is computed.
        
        Returns:
            the inertial frame
        
        
        """
        ...
    def withBetaThreshold(self, newBetaAngleThreshold: _FieldBetaAngleDetector__T) -> 'FieldBetaAngleDetector'[_FieldBetaAngleDetector__T]:
        """
        Create a new instance with the provided beta angle threshold.
        
        This method does not change the current instance.
        
        Parameters:
            newBetaAngleThreshold (FieldBetaAngleDetector): the beta angle threshold
        
        Returns:
            the new detector instance
        
        
        """
        ...
    def withCelestialProvider(self, newProvider: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_FieldBetaAngleDetector__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]]) -> 'FieldBetaAngleDetector'[_FieldBetaAngleDetector__T]:
        """
        Create a new instance with the provided coordinate provider.
        
        This method does not change the current instance.
        
        Parameters:
            newProvider (FieldPVCoordinatesProvider<FieldBetaAngleDetector> newProvider): the new coordinate provider
        
        Returns:
            the new detector instance
        
        
        """
        ...
    def withInertialFrame(self, newFrame: org.orekit.frames.Frame) -> 'FieldBetaAngleDetector'[_FieldBetaAngleDetector__T]:
        """
        Create a new instance with the provided inertial frame.
        
        This method does not change the current instance.
        
        Parameters:
            newFrame (Frame): the inertial frame
        
        Returns:
            the new detector instance
        
        
        """
        ...

_FieldBooleanDetector__T = typing.TypeVar('_FieldBooleanDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBooleanDetector(FieldAbstractDetector['FieldBooleanDetector'[_FieldBooleanDetector__T], _FieldBooleanDetector__T], typing.Generic[_FieldBooleanDetector__T]):
    """
    This class provides AND and OR operations for event detectors. This class treats positive values of the g function as true and negative values as false.
    
    One example for an imaging satellite might be to only detect events when a satellite is overhead (elevation > 0) AND when the ground point is sunlit (Sun elevation > 0). Another slightly contrived example using the OR operator would be to detect access to a set of ground stations and only report events when the satellite enters or leaves the field of view of the set, but not hand-offs between the ground stations.
    
    For the FieldBooleanDetector is important that the sign of the g function of the underlying event detector is not arbitrary, but has a semantic meaning, e.g. in or out, true or false. This class works well with event detectors that detect entry to or exit from a region, e.g. FieldEclipseDetector, FieldElevationDetector, FieldLatitudeCrossingDetector. Using this detector with detectors that are not based on entry to or exit from a region, e.g. FieldDateDetector, will likely lead to unexpected results. To apply conditions to this latter type of event detectors a FieldEventEnablingPredicateFilter is usually more appropriate.
    
    Since:
        12.0
    
    Also see:
        andCombine,
        orCombine,
        notCombine,
        EventEnablingPredicateFilter,
        EventSlopeFilter
    """
    _andCombine_0__T = typing.TypeVar('_andCombine_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _andCombine_1__T = typing.TypeVar('_andCombine_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def andCombine(detectors: typing.Union[java.util.Collection[FieldEventDetector[_andCombine_0__T]], typing.Sequence[FieldEventDetector[_andCombine_0__T]], typing.Set[FieldEventDetector[_andCombine_0__T]]]) -> 'FieldBooleanDetector'[_andCombine_0__T]: ...
    @typing.overload
    @staticmethod
    def andCombine(*detectors: FieldEventDetector[_andCombine_1__T]) -> 'FieldBooleanDetector'[_andCombine_1__T]: ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def finish(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldBooleanDetector__T]) -> None:
        """
        Description copied from interface: finish This method finalizes the event detector's job.
        
        Parameters:
            state (FieldSpacecraftState<FieldBooleanDetector> state): state at propagation end
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldBooleanDetector__T]) -> _FieldBooleanDetector__T:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<FieldBooleanDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectors(self) -> java.util.List[FieldEventDetector[_FieldBooleanDetector__T]]:
        """
        Get the list of original detectors.
        
        Returns:
            the list of original detectors
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldBooleanDetector__T], t: org.orekit.time.FieldAbsoluteDate[_FieldBooleanDetector__T]) -> None:
        """
        Description copied from class: init Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface FieldEventDetector
        
        Overrides: init in class FieldAbstractDetector
        
        Parameters:
            s0 (FieldSpacecraftState<FieldBooleanDetector> s0): initial state
            t (FieldAbsoluteDate<FieldBooleanDetector> t): target time for the integration
        
        
        """
        ...
    _notCombine__T = typing.TypeVar('_notCombine__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def notCombine(detector: FieldEventDetector[_notCombine__T]) -> 'FieldNegateDetector'[_notCombine__T]:
        """
        Create a new event detector that negates the g function of another detector.
        
        This detector will be initialized with the same getMaxCheckInterval, getThreshold, and getMaxIterationCount as detector. The event handler of the underlying detector is not used, instead the default handler is FieldContinueOnEvent.
        
        Parameters:
            detector (FieldEventDetector<T> detector): to negate.
        
        Returns:
            an new event detector whose g function is the same magnitude but opposite sign of detector.
        
        Also see:
            andCombine,
            orCombine,
            FieldBooleanDetector
        
        
        """
        ...
    _orCombine_0__T = typing.TypeVar('_orCombine_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _orCombine_1__T = typing.TypeVar('_orCombine_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def orCombine(detectors: typing.Union[java.util.Collection[FieldEventDetector[_orCombine_0__T]], typing.Sequence[FieldEventDetector[_orCombine_0__T]], typing.Set[FieldEventDetector[_orCombine_0__T]]]) -> 'FieldBooleanDetector'[_orCombine_0__T]: ...
    @typing.overload
    @staticmethod
    def orCombine(*detectors: FieldEventDetector[_orCombine_1__T]) -> 'FieldBooleanDetector'[_orCombine_1__T]: ...
    def reset(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldBooleanDetector__T], target: org.orekit.time.FieldAbsoluteDate[_FieldBooleanDetector__T]) -> None:
        """
        Description copied from interface: reset Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Parameters:
            state (FieldSpacecraftState<FieldBooleanDetector> state): current state
            target (FieldAbsoluteDate<FieldBooleanDetector> target): target time for the integration
        
        
        """
        ...

_FieldCylindricalShadowEclipseDetector__T = typing.TypeVar('_FieldCylindricalShadowEclipseDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCylindricalShadowEclipseDetector(FieldAbstractDetector['FieldCylindricalShadowEclipseDetector'[_FieldCylindricalShadowEclipseDetector__T], _FieldCylindricalShadowEclipseDetector__T], typing.Generic[_FieldCylindricalShadowEclipseDetector__T]):
    """
    Event detector for eclipses from a single, infinitely-distant light source, occulted by a spherical central body. The shadow region is cylindrical, a model less accurate than a conical one but more computationally-performant.
    
    The so-called g function is negative in eclipse, positive otherwise.
    
    Since:
        12.
    
    Also see:
        FieldEclipseDetector,
        CylindricalShadowEclipseDetector
    """
    @typing.overload
    def __init__(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], occultingBodyRadius: _FieldCylindricalShadowEclipseDetector__T, eventDetectionSettings: FieldEventDetectionSettings[_FieldCylindricalShadowEclipseDetector__T], handler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldCylindricalShadowEclipseDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]): ...
    @typing.overload
    def __init__(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], occultingBodyRadius: _FieldCylindricalShadowEclipseDetector__T, handler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldCylindricalShadowEclipseDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldCylindricalShadowEclipseDetector__T]) -> _FieldCylindricalShadowEclipseDetector__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<FieldCylindricalShadowEclipseDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getOccultingBodyRadius(self) -> _FieldCylindricalShadowEclipseDetector__T:
        """
        Getter for occulting body radius.
        
        Returns:
            radius
        
        
        """
        ...

_FieldDateDetector__T = typing.TypeVar('_FieldDateDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDateDetector(FieldAbstractDetector['FieldDateDetector'[_FieldDateDetector__T], _FieldDateDetector__T], org.orekit.time.FieldTimeStamped[_FieldDateDetector__T], typing.Generic[_FieldDateDetector__T]):
    """
    Finder for date events.
    
    This class finds date events (i.e. occurrence of some predefined dates).
    
    As of version 5.1, it is an enhanced date detector:
    
      - it can be defined without prior date ()
      - several dates can be added (addEventDate)
    
    The gap between the added dates must be more than the minGap.
    
    The default implementation behavior is to Action propagation at the first event date occurrence. This can be changed by calling withHandler after construction.
    
    Also see:
        addEventDetector
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    Default value for max check.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    DEFAULT_MIN_GAP: typing.ClassVar[float] = ...
    """
    Default value for minimum gap between added dates.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default value for convergence threshold.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDateDetector__T], *dates: typing.Union[org.orekit.time.FieldTimeStamped[_FieldDateDetector__T], typing.Callable[[], org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement]]]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldDateDetector__T]): ...
    def addEventDate(self, target: org.orekit.time.FieldAbsoluteDate[_FieldDateDetector__T]) -> None:
        """
        Add an event date.
        
        The date to add must be:
        
          - less than the smallest already registered event date minus the maxCheck
          - or more than the largest already registered event date plus the maxCheck
        
        
        Parameters:
            target (FieldAbsoluteDate<FieldDateDetector> target): target date
        
        Raises:
            IllegalArgumentException: if the date is too close from already defined interval
        
        
        """
        ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Specified by: dependsOnTimeOnly in interface FieldEventDetector
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldDateDetector__T]) -> _FieldDateDetector__T:
        """
        Compute the value of the switching function. This function measures the difference between the current and the target date.
        
        Specified by: g in interface FieldEventDetector
        
        Parameters:
            s (FieldSpacecraftState<FieldDateDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldDateDetector__T]:
        """
        Get the current event date according to the propagator.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            event date
        
        
        """
        ...
    def getDates(self) -> java.util.List[org.orekit.time.FieldTimeStamped[_FieldDateDetector__T]]:
        """
        Get all event field dates currently managed, in chronological order.
        
        Returns:
            all event field dates currently managed, in chronological order
        
        Since:
            12.0
        
        
        """
        ...
    def withMinGap(self, newMinGap: float) -> 'FieldDateDetector'[_FieldDateDetector__T]:
        """
        Setup minimum gap between added dates.
        
        Parameters:
            newMinGap (double): new minimum gap between added dates
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        
        """
        ...

_FieldEclipseDetector__T = typing.TypeVar('_FieldEclipseDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEclipseDetector(FieldAbstractDetector['FieldEclipseDetector'[_FieldEclipseDetector__T], _FieldEclipseDetector__T], typing.Generic[_FieldEclipseDetector__T]):
    """
    Finder for satellite eclipse related events.
    
    This class finds eclipse events, i.e. satellite within umbra (total eclipse) or penumbra (partial eclipse).
    
    The default implementation behavior is to Action propagation when entering the eclipse and to Action propagation when exiting the eclipse. This can be changed by calling withHandler after construction.
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEclipseDetector__T], occulted: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], occultedRadius: float, occulting: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEclipseDetector__T], occultationEngine: org.orekit.utils.OccultationEngine): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldEclipseDetector__T]) -> _FieldEclipseDetector__T:
        """
        Compute the value of the switching function. This function becomes negative when entering the region of shadow and positive when exiting.
        
        Parameters:
            s (FieldSpacecraftState<FieldEclipseDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getMargin(self) -> _FieldEclipseDetector__T:
        """
        Get the angular margin used for eclipse detection.
        
        Returns:
            angular margin used for eclipse detection (rad)
        
        Since:
            12.0
        
        
        """
        ...
    def getOccultationEngine(self) -> org.orekit.utils.OccultationEngine:
        """
        Get the occultation engine.
        
        Returns:
            occultation engine
        
        Since:
            12.0
        
        
        """
        ...
    def getTotalEclipse(self) -> bool:
        """
        Get the total eclipse detection flag.
        
        Returns:
            the total eclipse detection flag (true for umbra events detection, false for penumbra events detection)
        
        
        """
        ...
    def withMargin(self, newMargin: _FieldEclipseDetector__T) -> 'FieldEclipseDetector'[_FieldEclipseDetector__T]:
        """
        Setup a margin to angle detection.
        
        A positive margin implies eclipses are "larger" hence entry occurs earlier and exit occurs later than a detector with 0 margin.
        
        Parameters:
            newMargin (FieldEclipseDetector): angular margin to apply to eclipse detection (rad)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        
        """
        ...
    def withPenumbra(self) -> 'FieldEclipseDetector'[_FieldEclipseDetector__T]:
        """
        Setup the detector to penumbra detection.
        
        This will override a penumbra/umbra flag if it has been configured previously.
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            withUmbra
        
        
        """
        ...
    def withUmbra(self) -> 'FieldEclipseDetector'[_FieldEclipseDetector__T]:
        """
        Setup the detector to full umbra detection.
        
        This will override a penumbra/umbra flag if it has been configured previously.
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            withPenumbra
        
        
        """
        ...

_FieldEventEnablingPredicateFilter__T = typing.TypeVar('_FieldEventEnablingPredicateFilter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventEnablingPredicateFilter(FieldDetectorModifier[_FieldEventEnablingPredicateFilter__T], typing.Generic[_FieldEventEnablingPredicateFilter__T]):
    """
    Wrapper used to detect events only when enabled by an external predicated function.
    
    General FieldEventDetector are defined implicitly by a g crossing zero. This implies that during an orbit propagation, events are triggered at all zero crossings.
    
    Sometimes, users would like to enable or disable events by themselves, for example to trigger them only for certain orbits, or to check elevation maximums only when elevation itself is positive (i.e. they want to discard elevation maximums below ground). In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of computing time.
    
    Users can wrap a regular FieldEventDetector in an instance of this class and provide this wrapping instance to a FieldPropagator in order to avoid wasting time looking for uninteresting events. The wrapper will intercept the calls to the g and to the eventOccurred method in order to ignore uninteresting events. The wrapped regular FieldEventDetector will the see only the interesting events, i.e. either only events that occur when a user-provided event enabling predicate function is true, ignoring all events that occur when the event enabling predicate function is false. The number of calls to the g will also be reduced.
    
    Since:
        12.0
    
    Also see:
        FieldEventSlopeFilter
    """
    @typing.overload
    def __init__(self, detectionSettings: FieldEventDetectionSettings[_FieldEventEnablingPredicateFilter__T], rawDetector: FieldEventDetector[_FieldEventEnablingPredicateFilter__T], enabler: typing.Union[FieldEnablingPredicate[_FieldEventEnablingPredicateFilter__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], _FieldEventEnablingPredicateFilter__T], bool]]): ...
    @typing.overload
    def __init__(self, rawDetector: FieldEventDetector[_FieldEventEnablingPredicateFilter__T], enabler: typing.Union[FieldEnablingPredicate[_FieldEventEnablingPredicateFilter__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], _FieldEventEnablingPredicateFilter__T], bool]]): ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Specified by: dependsOnTimeOnly in interface FieldDetectorModifier
        
        Specified by: dependsOnTimeOnly in interface FieldEventDetector
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldEventEnablingPredicateFilter__T]) -> _FieldEventEnablingPredicateFilter__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface FieldDetectorModifier
        
        Specified by: g in interface FieldEventDetector
        
        Parameters:
            s (FieldSpacecraftState<FieldEventEnablingPredicateFilter> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldEventEnablingPredicateFilter__T]:
        """
        Getter for the settings.
        
        Specified by: getDetectionSettings in interface FieldDetectorModifier
        
        Specified by: getDetectionSettings in interface FieldEventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> FieldEventDetector[_FieldEventEnablingPredicateFilter__T]:
        """
        Get the wrapped raw detector.
        
        Specified by: getDetector in interface FieldDetectorModifier
        
        Returns:
            the wrapped raw detector
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldEventEnablingPredicateFilter__T]:
        """
        Get the handler.
        
        Specified by: getHandler in interface FieldDetectorModifier
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def getPredicate(self) -> FieldEnablingPredicate[_FieldEventEnablingPredicateFilter__T]:
        """
        Getter for the enabling predicate.
        
        Returns:
            predicate
        
        Since:
            13.1
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldEventEnablingPredicateFilter__T], t: org.orekit.time.FieldAbsoluteDate[_FieldEventEnablingPredicateFilter__T]) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface FieldDetectorModifier
        
        Specified by: init in interface FieldEventDetector
        
        Parameters:
            s0 (FieldSpacecraftState<FieldEventEnablingPredicateFilter> s0): initial state
            t (FieldAbsoluteDate<FieldEventEnablingPredicateFilter> t): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Returns:
            true if the current propagation is forward
        
        
        """
        ...
    def reset(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEventEnablingPredicateFilter__T], target: org.orekit.time.FieldAbsoluteDate[_FieldEventEnablingPredicateFilter__T]) -> None:
        """
        Description copied from interface: reset Reset the event detector during propagation when the state is modified by an event or an additional data provider.
        
        The default implementation does nothing.
        
        Specified by: reset in interface FieldDetectorModifier
        
        Specified by: reset in interface FieldEventDetector
        
        Parameters:
            state (FieldSpacecraftState<FieldEventEnablingPredicateFilter> state): current state
            target (FieldAbsoluteDate<FieldEventEnablingPredicateFilter> target): target time for the integration
        
        
        """
        ...
    def withDetectionSettings(self, settings: FieldEventDetectionSettings[_FieldEventEnablingPredicateFilter__T]) -> 'FieldEventEnablingPredicateFilter'[_FieldEventEnablingPredicateFilter__T]:
        """
        Builds a new instance from the input detection settings.
        
        Parameters:
            settings (FieldEventDetectionSettings<FieldEventEnablingPredicateFilter> settings): event detection settings to be used
        
        Returns:
            a new detector
        
        
        """
        ...

_FieldEventShifter__T = typing.TypeVar('_FieldEventShifter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventShifter(FieldDetectorModifier[_FieldEventShifter__T], typing.Generic[_FieldEventShifter__T]):
    """
    Wrapper shifting events occurrences times.
    
    This class wraps an FieldEventDetector to slightly shift the events occurrences times. A typical use case is for handling operational delays before or after some physical event really occurs.
    
    For example, the satellite attitude mode may be switched from sun pointed to spin-stabilized a few minutes before eclipse entry, and switched back to sun pointed a few minutes after eclipse exit. This behavior is handled by wrapping an FieldEclipseDetector into an instance of this class with a positive times shift for increasing events (eclipse exit) and a negative times shift for decreasing events (eclipse entry).
    
    Since:
        13.0
    
    Also see:
        addEventDetector,
        FieldEventDetector, EventShifter
    """
    @typing.overload
    def __init__(self, detectionSettings: FieldEventDetectionSettings[_FieldEventShifter__T], detector: FieldEventDetector[_FieldEventShifter__T], useShiftedStates: bool, increasingTimeShift: _FieldEventShifter__T, decreasingTimeShift: _FieldEventShifter__T): ...
    @typing.overload
    def __init__(self, detector: FieldEventDetector[_FieldEventShifter__T], useShiftedStates: bool, increasingTimeShift: _FieldEventShifter__T, decreasingTimeShift: _FieldEventShifter__T): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldEventShifter__T]) -> _FieldEventShifter__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface FieldDetectorModifier
        
        Specified by: g in interface FieldEventDetector
        
        Parameters:
            s (FieldSpacecraftState<FieldEventShifter> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDecreasingTimeShift(self) -> _FieldEventShifter__T:
        """
        Get the decreasing events time shift.
        
        Returns:
            decreasing events time shift
        
        
        """
        ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldEventShifter__T]:
        """
        Description copied from interface: getDetectionSettings Getter for the settings.
        
        Specified by: getDetectionSettings in interface FieldDetectorModifier
        
        Specified by: getDetectionSettings in interface FieldEventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getDetector(self) -> FieldEventDetector[_FieldEventShifter__T]:
        """
        Get the detector for the raw unshifted event.
        
        Specified by: getDetector in interface FieldDetectorModifier
        
        Returns:
            the detector for the raw unshifted event
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldEventShifter__T]:
        """
        Description copied from interface: getHandler Get the handler.
        
        Specified by: getHandler in interface FieldDetectorModifier
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...
    def getIncreasingTimeShift(self) -> _FieldEventShifter__T:
        """
        Get the increasing events time shift.
        
        Returns:
            increasing events time shift
        
        
        """
        ...
    def withDetectionSettings(self, settings: FieldEventDetectionSettings[_FieldEventShifter__T]) -> 'FieldEventShifter'[_FieldEventShifter__T]:
        """
        Builds a new instance from the input detection settings.
        
        Parameters:
            settings (FieldEventDetectionSettings<FieldEventShifter> settings): event detection settings to be used
        
        Returns:
            a new detector
        
        
        """
        ...

_FieldExtremumAngularSeparationDetector__T = typing.TypeVar('_FieldExtremumAngularSeparationDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldExtremumAngularSeparationDetector(FieldAbstractDetector['FieldExtremumAngularSeparationDetector'[_FieldExtremumAngularSeparationDetector__T], _FieldExtremumAngularSeparationDetector__T], typing.Generic[_FieldExtremumAngularSeparationDetector__T]):
    """
    Detector of local extrema with angular separation.
    
    Since:
        13.1
    
    Also see:
        FieldAngularSeparationDetector
    """
    def __init__(self, detectionSettings: FieldEventDetectionSettings[_FieldExtremumAngularSeparationDetector__T], handler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldExtremumAngularSeparationDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]], beacon: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], observer: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]):
        """
        Protected constructor with full parameters.
        
        Parameters:
            detectionSettings (FieldEventDetectionSettings<FieldExtremumAngularSeparationDetector> detectionSettings): detection settings
            handler (FieldEventHandler<FieldExtremumAngularSeparationDetector> handler): event handler to call at event occurrences
            beacon (ExtendedPositionProvider): beacon at the center of the proximity zone
            observer (ExtendedPositionProvider): observer for the spacecraft, that may also see the beacon at the same time if they are too close to each other
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldExtremumAngularSeparationDetector__T]) -> _FieldExtremumAngularSeparationDetector__T:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<FieldExtremumAngularSeparationDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getBeacon(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Get the beacon at the center of the proximity zone.
        
        Returns:
            beacon at the center of the proximity zone
        
        
        """
        ...
    def getObserver(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Get the observer for the spacecraft.
        
        Returns:
            observer for the spacecraft
        
        
        """
        ...

_FieldExtremumApproachDetector__T = typing.TypeVar('_FieldExtremumApproachDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldExtremumApproachDetector(FieldAbstractDetector['FieldExtremumApproachDetector'[_FieldExtremumApproachDetector__T], _FieldExtremumApproachDetector__T], typing.Generic[_FieldExtremumApproachDetector__T]):
    """
    Finder for extremum approach events.
    
    This class finds extremum approach events (i.e. closest or farthest approach).
    
    The default implementation behavior is to Action propagation at farthest approach and to Action propagation at closest approach. This can be changed by calling withHandler after construction (go to the end of the documentation to see an example).
    
    As this detector needs two objects (moving relative to each other), it embeds one FieldPVCoordinatesProvider for the secondary object and is registered as an event detector in the propagator of the primary object. The secondary object FieldPVCoordinatesProvider will therefore be driven by this detector (and hence by the propagator in which this detector is registered). Note that you can also create this detector using a standard PVCoordinatesProvider
    
    **In order to avoid infinite recursion, care must be taken to have the secondary object provider being completely independent from anything else. In particular, if the provider is a propagator, it should not be run together in a PropagatorsParallelizer with the propagator this detector is registered in. It is fine however to configure two separate propagators PsA and PsB with similar settings for the secondary object and one propagator Pm for the primary object and then use Psa in this detector registered within Pm while Pm and Psb are run in the context of a PropagatorsParallelizer.**
    
    For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally costly.
    
    Also, it is possible to detect solely one type of event using an EventSlopeFilter. For example in order to only detect closest approach, one should type the following :
    
    
     FieldExtremumApproachDetector<Type> extremumApproachDetector = new FieldExtremumApproachDetector<>(field, secondaryPVProvider);
     FieldEventDetector<Type> closeApproachDetector = new FieldEventSlopeFilter<>(extremumApproachDetector, FilterType.TRIGGER_ONLY_INCREASING_EVENTS);
      
     
    
    Since:
        11.3
    
    Also see:
        addEventDetector,
        FieldEventSlopeFilter, FilterType
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldExtremumApproachDetector__T], secondaryPVProvider: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_FieldExtremumApproachDetector__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldExtremumApproachDetector__T], secondaryPVProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]): ...
    def computeDeltaPV(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldExtremumApproachDetector__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldExtremumApproachDetector__T]:
        """
        Compute the relative PV between primary and secondary objects.
        
        Parameters:
            s (FieldSpacecraftState<FieldExtremumApproachDetector> s): Spacecraft state.
        
        Returns:
            Relative position between primary (=s) and secondaryPVProvider.
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldExtremumApproachDetector__T]) -> _FieldExtremumApproachDetector__T:
        """
        The g is positive when the primary object is getting further away from the secondary object and is negative when it is getting closer to it.
        
        Parameters:
            s (FieldSpacecraftState<FieldExtremumApproachDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getSecondaryPVProvider(self) -> org.orekit.utils.FieldPVCoordinatesProvider[_FieldExtremumApproachDetector__T]:
        """
        Get the secondary position-velocity provider stored in this instance.
        
        Returns:
            the secondary position-velocity provider stored in this instance
        
        
        """
        ...

_FieldFunctionalDetector__T = typing.TypeVar('_FieldFunctionalDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldFunctionalDetector(FieldAbstractDetector['FieldFunctionalDetector'[_FieldFunctionalDetector__T], _FieldFunctionalDetector__T], typing.Generic[_FieldFunctionalDetector__T]):
    """
    A detector that implements the g function using a lambda that can be set using withFunction.
    
    For example, to create a simple date detector use:
    
    
     FieldFunctionalDetector<T> d = new FieldFunctionalDetector<>(field)
         .withGFunction((s) -> s.getDate().durationFrom(triggerDate))
         .withMaxCheck(field.getZero().add(1e10));
     
    
    Since:
        10.2
    """
    def __init__(self, field: org.hipparchus.Field[_FieldFunctionalDetector__T]):
        """
        Create an event detector with the default values. These are DEFAULT_MAX_CHECK, DEFAULT_THRESHOLD, DEFAULT_MAX_ITER, ContinueOnEvent, and a g function that is identically unity.
        
        Parameters:
            field (Field<FieldFunctionalDetector> field): on which this detector is defined.
        
        protected FieldFunctionalDetector (FieldEventDetectionSettings<FieldFunctionalDetector> detectionSettings, FieldEventHandler<FieldFunctionalDetector> handler, Function<FieldSpacecraftState<FieldFunctionalDetector>, FieldFunctionalDetector> function)
        
        Protected constructor.
        
        Parameters:
            detectionSettings (FieldEventDetectionSettings<FieldFunctionalDetector> detectionSettings): event detection settings
            handler (FieldEventHandler<FieldFunctionalDetector> handler): event handler to call at event occurrences
            function (Function<FieldSpacecraftState<FieldFunctionalDetector>, FieldFunctionalDetector> function): the switching function.
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T]) -> _FieldFunctionalDetector__T:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<FieldFunctionalDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getFunction(self) -> java.util.function.Function[org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T], _FieldFunctionalDetector__T]:
        """
        Get the switching function.
        
        Returns:
            the function used in g.
        
        
        """
        ...
    def withFunction(self, newGFunction: typing.Union[java.util.function.Function[org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T], _FieldFunctionalDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T]], _FieldFunctionalDetector__T]]) -> 'FieldFunctionalDetector'[_FieldFunctionalDetector__T]:
        """
        Create a new event detector with a new g function, keeping all other attributes the same. It is recommended to use withMaxCheck and withThreshold to set appropriate values for this g function.
        
        Parameters:
            newGFunction (Function<FieldSpacecraftState<FieldFunctionalDetector>, FieldFunctionalDetector> newGFunction): the new g function.
        
        Returns:
            a new detector with the new g function.
        
        
        """
        ...

_FieldLatitudeCrossingDetector__T = typing.TypeVar('_FieldLatitudeCrossingDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLatitudeCrossingDetector(FieldAbstractDetector['FieldLatitudeCrossingDetector'[_FieldLatitudeCrossingDetector__T], _FieldLatitudeCrossingDetector__T], typing.Generic[_FieldLatitudeCrossingDetector__T]):
    """
    Detector for geographic latitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed latitude with respect to a central body.
    
    Since:
        9.3
    """
    @typing.overload
    def __init__(self, t: _FieldLatitudeCrossingDetector__T, t2: _FieldLatitudeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLatitudeCrossingDetector__T], body: org.orekit.bodies.OneAxisEllipsoid, latitude: float): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldLatitudeCrossingDetector__T]) -> _FieldLatitudeCrossingDetector__T:
        """
        Compute the value of the detection function.
        
        The value is the spacecraft latitude minus the fixed latitude to be crossed. It is positive if the spacecraft is northward and negative if it is southward with respect to the fixed latitude.
        
        Parameters:
            s (FieldSpacecraftState<FieldLatitudeCrossingDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft latitude minus the fixed latitude to be crossed
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
        Get the fixed latitude to be crossed (radians).
        
        Returns:
            fixed latitude to be crossed (radians)
        
        
        """
        ...

_FieldLatitudeRangeCrossingDetector__T = typing.TypeVar('_FieldLatitudeRangeCrossingDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLatitudeRangeCrossingDetector(FieldAbstractDetector['FieldLatitudeRangeCrossingDetector'[_FieldLatitudeRangeCrossingDetector__T], _FieldLatitudeRangeCrossingDetector__T], typing.Generic[_FieldLatitudeRangeCrossingDetector__T]):
    """
    Detector for geographic latitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed latitude range with respect to a central body.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, t: _FieldLatitudeRangeCrossingDetector__T, t2: _FieldLatitudeRangeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLatitudeRangeCrossingDetector__T], body: org.orekit.bodies.OneAxisEllipsoid, fromLatitude: float, toLatitude: float): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldLatitudeRangeCrossingDetector__T]) -> _FieldLatitudeRangeCrossingDetector__T:
        """
        Compute the value of the detection function.
        
        The value is positive if the spacecraft latitude is inside the latitude range. It is positive if the spacecraft is northward to lower boundary range and southward to upper boundary range, with respect to the fixed latitude range.
        
        Parameters:
            s (FieldSpacecraftState<FieldLatitudeRangeCrossingDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            positive if spacecraft inside the range
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getFromLatitude(self) -> float:
        """
        Get the fixed latitude range to be crossed (radians), lower boundary.
        
        Returns:
            fixed lower boundary latitude range to be crossed (radians)
        
        
        """
        ...
    def getToLatitude(self) -> float:
        """
        Get the fixed latitude range to be crossed (radians), upper boundary.
        
        Returns:
            fixed lower boundary latitude range to be crossed (radians)
        
        
        """
        ...

_FieldLongitudeCrossingDetector__T = typing.TypeVar('_FieldLongitudeCrossingDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLongitudeCrossingDetector(FieldAbstractDetector['FieldLongitudeCrossingDetector'[_FieldLongitudeCrossingDetector__T], _FieldLongitudeCrossingDetector__T], typing.Generic[_FieldLongitudeCrossingDetector__T]):
    """
    Detector for geographic longitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed longitude with respect to a central body.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, t: _FieldLongitudeCrossingDetector__T, t2: _FieldLongitudeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLongitudeCrossingDetector__T], body: org.orekit.bodies.OneAxisEllipsoid, longitude: float): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldLongitudeCrossingDetector__T]) -> _FieldLongitudeCrossingDetector__T:
        """
        Compute the value of the detection function.
        
        The value is the longitude difference between the spacecraft and the fixed longitude to be crossed, with some sign tweaks to ensure continuity. These tweaks imply the increasing flag in events detection becomes irrelevant here! As an example, the longitude of a prograde spacecraft will always increase, but this g function will increase and decrease so it will cross the zero value once per orbit, in increasing and decreasing directions on alternate orbits. If eastwards and westwards crossing have to be distinguished, the velocity direction has to be checked instead of looking at the increasing flag.
        
        Parameters:
            s (FieldSpacecraftState<FieldLongitudeCrossingDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            longitude difference between the spacecraft and the fixed longitude, with some sign tweaks to ensure continuity
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
        Get the fixed longitude to be crossed (radians).
        
        Returns:
            fixed longitude to be crossed (radians)
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldLongitudeCrossingDetector__T], t: org.orekit.time.FieldAbsoluteDate[_FieldLongitudeCrossingDetector__T]) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface FieldEventDetector
        
        Overrides: init in class FieldAbstractDetector
        
        Parameters:
            s0 (FieldSpacecraftState<FieldLongitudeCrossingDetector> s0): initial state
            t (FieldAbsoluteDate<FieldLongitudeCrossingDetector> t): target time for the integration
        
        
        """
        ...

_FieldLongitudeRangeCrossingDetector__T = typing.TypeVar('_FieldLongitudeRangeCrossingDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLongitudeRangeCrossingDetector(FieldAbstractDetector['FieldLongitudeRangeCrossingDetector'[_FieldLongitudeRangeCrossingDetector__T], _FieldLongitudeRangeCrossingDetector__T], typing.Generic[_FieldLongitudeRangeCrossingDetector__T]):
    """
    Detector for geographic longitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed longitude range with respect to a central body.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, t: _FieldLongitudeRangeCrossingDetector__T, t2: _FieldLongitudeRangeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLongitudeRangeCrossingDetector__T], body: org.orekit.bodies.OneAxisEllipsoid, fromLongitude: float, toLongitude: float): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldLongitudeRangeCrossingDetector__T]) -> _FieldLongitudeRangeCrossingDetector__T:
        """
        Compute the value of the detection function.
        
        The value is positive if the spacecraft longitude is inside the longitude range. The longitude value is reflected from [-PI, +PI] to [0, 2 PI] to ensure continuity.
        
        Parameters:
            s (FieldSpacecraftState<FieldLongitudeRangeCrossingDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            positive if spacecraft inside the range
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getFromLongitude(self) -> float:
        """
        Get the fixed longitude range to be crossed (radians), lower boundary.
        
        Returns:
            fixed lower boundary longitude range to be crossed (radians)
        
        
        """
        ...
    def getToLongitude(self) -> float:
        """
        Get the fixed longitude range to be crossed (radians), upper boundary.
        
        Returns:
            fixed upper boundary longitude range to be crossed (radians)
        
        
        """
        ...

_FieldNegateDetector__T = typing.TypeVar('_FieldNegateDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNegateDetector(FieldAbstractDetector['FieldNegateDetector'[_FieldNegateDetector__T], _FieldNegateDetector__T], FieldDetectorModifier[_FieldNegateDetector__T], typing.Generic[_FieldNegateDetector__T]):
    """
    An event detector that negates the sign on another event detector's g function.
    
    Since:
        12.0
    """
    def __init__(self, original: FieldEventDetector[_FieldNegateDetector__T]):
        """
        Create a new event detector that negates an existing event detector.
        
        This detector will be initialized with the same getMaxCheckInterval, getThreshold, and getMaxIterationCount as original. Initially this detector will use the FieldContinueOnEvent event handler.
        
        Parameters:
            original (FieldEventDetector<FieldNegateDetector> original): detector.
        
        protected FieldNegateDetector (FieldEventDetectionSettings<FieldNegateDetector> detectionSettings, FieldEventHandler<FieldNegateDetector> newHandler, FieldEventDetector<FieldNegateDetector> original)
        
        Protected constructor.
        
        Parameters:
            detectionSettings (FieldEventDetectionSettings<FieldNegateDetector> detectionSettings): event detection settings.
            newHandler (FieldEventHandler<FieldNegateDetector> newHandler): event handler.
            original (FieldEventDetector<FieldNegateDetector> original): event detector.
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldNegateDetector__T]) -> _FieldNegateDetector__T:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface FieldDetectorModifier
        
        Specified by: g in interface FieldEventDetector
        
        Parameters:
            s (FieldSpacecraftState<FieldNegateDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetector(self) -> FieldEventDetector[_FieldNegateDetector__T]:
        """
        Description copied from interface: getDetector Getter for wrapped detector.
        
        Specified by: getDetector in interface FieldDetectorModifier
        
        Returns:
            detector
        
        
        """
        ...
    def getOriginal(self) -> FieldEventDetector[_FieldNegateDetector__T]:
        """
        Get the delegate event detector.
        
        Returns:
            the delegate event detector
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldNegateDetector__T], t: org.orekit.time.FieldAbsoluteDate[_FieldNegateDetector__T]) -> None:
        """
        Description copied from class: init Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Specified by: init in interface FieldDetectorModifier
        
        Specified by: init in interface FieldEventDetector
        
        Overrides: init in class FieldAbstractDetector
        
        Parameters:
            s0 (FieldSpacecraftState<FieldNegateDetector> s0): initial state
            t (FieldAbsoluteDate<FieldNegateDetector> t): target time for the integration
        
        
        """
        ...

_FieldNodeDetector__T = typing.TypeVar('_FieldNodeDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNodeDetector(FieldAbstractDetector['FieldNodeDetector'[_FieldNodeDetector__T], _FieldNodeDetector__T], typing.Generic[_FieldNodeDetector__T]):
    """
    Finder for node crossing events.
    
    This class finds equator crossing events (i.e. ascending or descending node crossing).
    
    The default implementation behavior is to Action propagation at descending node crossing and to Action propagation at ascending node crossing. This can be changed by calling withHandler after construction.
    
    Beware that node detection will fail for almost equatorial orbits. If for example a node detector is used to trigger an ImpulseManeuver and the maneuver turn the orbit plane to equator, then the detector may completely fail just after the maneuver has been performed! This is a real case that has been encountered during validation ...
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, t: _FieldNodeDetector__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldNodeDetector__T], frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNodeDetector__T], frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldNodeDetector__T], frame: org.orekit.frames.Frame): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldNodeDetector__T]) -> _FieldNodeDetector__T:
        """
        Compute the value of the switching function. This function computes the Z position in the defined frame.
        
        Parameters:
            s (FieldSpacecraftState<FieldNodeDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the equator is defined.
        
        Returns:
            the frame in which the equator is defined
        
        
        """
        ...

class FieldOfViewDetector(AbstractDetector['FieldOfViewDetector']):
    """
    Finder for target entry/exit events with respect to a satellite sensor FieldOfView.
    
    Beware that this detector is unaware of any bodies occluding line-of-sight to the target. It can be therefore used for many contexts from Earth Observation to interplanetary mission design. For instance, in an Earth Observation context, it can be easily combined to an ElevationDetector using andCombine to calculate station visibility opportunities within the satellite's field of view.
    
    The default implementation behavior is to Action propagation at FOV entry and to Action propagation at FOV exit. This can be changed by calling withHandler after construction.
    
    Since:
        7.1
    
    Also see:
        addEventDetector,
        FootprintOverlapDetector,
        VisibilityTrigger
    """
    @typing.overload
    def __init__(self, pvTarget: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], radiusTarget: float, trigger: VisibilityTrigger, fov: org.orekit.geometry.fov.FieldOfView): ...
    @typing.overload
    def __init__(self, pvTarget: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], fov: org.orekit.geometry.fov.FieldOfView): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        The g function value is the angular offset between the target center and the offsetFromBoundary, plus or minus the target angular radius depending on the VisibilityTrigger, minus the getMargin. It is therefore negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View.
        
        As per the previous definition, when the target enters the Field Of View, a decreasing event is generated, and when the target leaves the Field Of View, an increasing event is generated.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getFOV(self) -> org.orekit.geometry.fov.FieldOfView:
        """
        Get the Field Of View.
        
        Returns:
            Field Of View
        
        Since:
            10.1
        
        
        """
        ...
    def getPVTarget(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the position/velocity provider of the target .
        
        Returns:
            the position/velocity provider of the target
        
        
        """
        ...

_FieldParameterDrivenDateIntervalDetector__T = typing.TypeVar('_FieldParameterDrivenDateIntervalDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldParameterDrivenDateIntervalDetector(FieldAbstractDetector['FieldParameterDrivenDateIntervalDetector'[_FieldParameterDrivenDateIntervalDetector__T], _FieldParameterDrivenDateIntervalDetector__T], typing.Generic[_FieldParameterDrivenDateIntervalDetector__T]):
    """
    Detector for date intervals that may be offset thanks to parameter drivers.
    
    Two dual views can be used for date intervals: either start date/stop date or median date/duration. getStartDriver/getStopDriver drivers and getMedianDriver/getDurationDriver drivers work in pair. Both drivers in one pair can be selected and their changes will be propagated to the other pair, but attempting to select drivers in both pairs at the same time will trigger an exception. Changing the value of a driver that is not selected should be avoided as it leads to inconsistencies between the pairs.
    
    Since:
        11.1
    
    Also see:
        addEventDetector
    """
    START_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for start driver.
    
    Also see:
        constant
    
    
    """
    STOP_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for stop driver.
    
    Also see:
        constant
    
    
    """
    MEDIAN_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for median driver.
    
    Also see:
        constant
    
    
    """
    DURATION_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for duration driver.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldParameterDrivenDateIntervalDetector__T], string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldParameterDrivenDateIntervalDetector__T], string: str, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldParameterDrivenDateIntervalDetector__T]) -> _FieldParameterDrivenDateIntervalDetector__T:
        """
        Compute the value of the switching function.
        
        The function is positive for dates within the interval defined by applying the parameter drivers shifts to reference dates, and negative for dates outside of this interval. Note that if Δt_start - Δt_stop is less than ref_stop.durationFrom(ref_start), then the interval degenerates to empty and the function never reaches positive values.
        
        Parameters:
            s (FieldSpacecraftState<FieldParameterDrivenDateIntervalDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDurationDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get the driver for duration.
        
        Note that the duration is automatically adjusted if either getStartDriver start date or getStopDriver are isSelected changed.
        
        Returns:
            driver for duration
        
        
        """
        ...
    def getMedianDriver(self) -> org.orekit.utils.DateDriver:
        """
        Get the driver for median date.
        
        Note that the median date is automatically adjusted if either getStartDriver start date or getStopDriver are isSelected changed.
        
        Returns:
            driver for median date
        
        
        """
        ...
    def getStartDriver(self) -> org.orekit.utils.DateDriver:
        """
        Get the driver for start date.
        
        Note that the start date is automatically adjusted if either getMedianDriver or getDurationDriver are isSelected and changed.
        
        Returns:
            driver for start date
        
        
        """
        ...
    def getStopDriver(self) -> org.orekit.utils.DateDriver:
        """
        Get the driver for stop date.
        
        Note that the stop date is automatically adjusted if either getMedianDriver or getDurationDriver are isSelected changed.
        
        Returns:
            driver for stop date
        
        
        """
        ...

_FieldRelativeDistanceDetector__T = typing.TypeVar('_FieldRelativeDistanceDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRelativeDistanceDetector(FieldAbstractDetector['FieldRelativeDistanceDetector'[_FieldRelativeDistanceDetector__T], _FieldRelativeDistanceDetector__T], typing.Generic[_FieldRelativeDistanceDetector__T]):
    """
    Detector of specific value for the distance relative to another trajectory (using the Euclidean norm).
    
    The default implementation behavior is to Action propagation. This can be changed by calling withHandler after construction.
    
    As this detector needs two objects (moving relative to each other), it embeds one FieldPVCoordinatesProvider for the secondary object and is registered as an event detector in the propagator of the primary object. The secondary object FieldPVCoordinatesProvider will therefore be driven by this detector (and hence by the propagator in which this detector is registered).
    
    For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally costly.
    
    Since:
        12.1
    
    Also see:
        addEventDetector
    """
    def __init__(self, secondaryPVProvider: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_FieldRelativeDistanceDetector__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], distanceThreshold: _FieldRelativeDistanceDetector__T):
        """
        Constructor with default values.
        
        By default, the implemented behavior is to Action propagation at detection.
        
        Parameters:
            secondaryPVProvider (FieldPVCoordinatesProvider<FieldRelativeDistanceDetector> secondaryPVProvider): PVCoordinates provider of the other object defining relative distance.
            distanceThreshold (FieldRelativeDistanceDetector): Relative distance threshold for event detection
        
        protected FieldRelativeDistanceDetector (FieldEventDetectionSettings<FieldRelativeDistanceDetector> detectionSettings, FieldEventHandler<FieldRelativeDistanceDetector> handler, FieldPVCoordinatesProvider<FieldRelativeDistanceDetector> secondaryPVProvider, FieldRelativeDistanceDetector distanceThreshold)
        
        Constructor.
        
        This constructor is to be used if the user wants to change the default behavior of the detector.
        
        Parameters:
            detectionSettings (FieldEventDetectionSettings<FieldRelativeDistanceDetector> detectionSettings): Detection settings.
            handler (FieldEventHandler<FieldRelativeDistanceDetector> handler): Event handler to call at event occurrences.
            secondaryPVProvider (FieldPVCoordinatesProvider<FieldRelativeDistanceDetector> secondaryPVProvider): PVCoordinates provider of the other object defining relative distance.
            distanceThreshold (FieldRelativeDistanceDetector): Relative distance threshold for event detection
        
        Since:
            12.2
        
        Also see:
            FieldEventHandler
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldRelativeDistanceDetector__T]) -> _FieldRelativeDistanceDetector__T:
        """
        The g is positive when the relative distance is larger or equal than the threshold, non-positive otherwise.
        
        Parameters:
            s (FieldSpacecraftState<FieldRelativeDistanceDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDistanceThreshold(self) -> _FieldRelativeDistanceDetector__T:
        """
        Get the relative distance threshold.
        
        Returns:
            threshold triggering detection
        
        
        """
        ...
    def getSecondaryPVProvider(self) -> org.orekit.utils.FieldPVCoordinatesProvider[_FieldRelativeDistanceDetector__T]:
        """
        Get the secondary position-velocity provider stored in this instance.
        
        Returns:
            the secondary position-velocity provider stored in this instance
        
        
        """
        ...

_FieldTimeIntervalDetector__T = typing.TypeVar('_FieldTimeIntervalDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTimeIntervalDetector(FieldAbstractDetector['FieldTimeIntervalDetector'[_FieldTimeIntervalDetector__T], _FieldTimeIntervalDetector__T], typing.Generic[_FieldTimeIntervalDetector__T]):
    """
    Detector for time intervals. Positive whenever the date is inside, negative otherwise.
    
    Since:
        13.1
    
    Also see:
        TimeInterval, TimeIntervalDetector
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTimeIntervalDetector__T], timeInterval: org.orekit.time.TimeInterval): ...
    @typing.overload
    def __init__(self, detectionSettings: FieldEventDetectionSettings[_FieldTimeIntervalDetector__T], handler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldTimeIntervalDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]], timeInterval: org.orekit.time.TimeInterval): ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldTimeIntervalDetector__T]) -> _FieldTimeIntervalDetector__T:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<FieldTimeIntervalDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getTimeInterval(self) -> org.orekit.time.TimeInterval:
        """
        Getter for the time interval.
        
        Returns:
            interval
        
        
        """
        ...

class FootprintOverlapDetector(AbstractDetector['FootprintOverlapDetector']):
    """
    Detector triggered by geographical region entering/leaving a spacecraft sensor FieldOfView.
    
    This detector is a mix between to FieldOfViewDetector and GeographicZoneDetector. Similar to the first detector above, it triggers events related to entry/exit of targets in a Field Of View, taking attitude into account. Similar to the second detector above, its target is an entire geographic region (which can even be split in several non-connected patches and can have holes).
    
    This detector is typically used for ground observation missions with agile satellites than can look away from nadir.
    
    The default implementation behavior is to Action propagation at FOV entry and to Action propagation at FOV exit. This can be changed by calling withHandler after construction.
    
    Since:
        7.1
    
    Also see:
        addEventDetector,
        FieldOfViewDetector,
        GeographicZoneDetector
    """
    def __init__(self, fov: org.orekit.geometry.fov.FieldOfView, body: org.orekit.bodies.OneAxisEllipsoid, zone: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, samplingStep: float):
        """
        Build a new instance.
        
        The maximal interval between distance to FOV boundary checks should be smaller than the half duration of the minimal pass to handle, otherwise some short passes could be missed.
        
        Parameters:
            fov (FieldOfView): sensor field of view
            body (OneAxisEllipsoid): body on which the geographic zone is defined
            zone (SphericalPolygonsSet): geographic zone to consider
            samplingStep (double): linear step used for sampling the geographic zone (in meters)
        
        Since:
            10.1
        
        protected FootprintOverlapDetector (EventDetectionSettings detectionSettings, EventHandler handler, FieldOfView fov, OneAxisEllipsoid body, SphericalPolygonsSet zone, double samplingStep, List<org.orekit.propagation.events.FootprintOverlapDetector.SamplingPoint> sampledZone)
        
        Protected constructor with full parameters.
        
        This constructor is not public as users are expected to use the builder API with the various withXxx() methods to set up the instance in a readable manner without using a huge amount of parameters.
        
        Parameters:
            detectionSettings (EventDetectionSettings): event detection settings
            handler (EventHandler): event handler to call at event occurrences
            body (FieldOfView): body on which the geographic zone is defined
            zone (OneAxisEllipsoid): geographic zone to consider
            fov (SphericalPolygonsSet): sensor field of view
            sampledZone (double): sampling of the geographic zone
            samplingStep (List<org.orekit.propagation.events.FootprintOverlapDetector.SamplingPoint> sampledZone): linear step used for sampling the geographic zone (in meters)
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        The g function value is the minimum offset among the region points with respect to the Field Of View boundary. It is positive if all region points are outside of the Field Of View, and negative if at least some of the region points are inside of the Field Of View. The minimum is computed by sampling the region, considering only the points for which the spacecraft is above the horizon. The accuracy of the detection depends on the linear sampling step set at detector construction. If the spacecraft is below horizon for all region points, an arbitrary positive value is returned.
        
        As per the previous definition, when the region enters the Field Of View, a decreasing event is generated, and when the region leaves the Field Of View, an increasing event is generated.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.BodyShape:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getFOV(self) -> org.orekit.geometry.fov.FieldOfView:
        """
        Get the Field Of View.
        
        Returns:
            Field Of View
        
        Since:
            10.1
        
        
        """
        ...
    def getZone(self) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet:
        """
        Get the geographic zone triggering the events.
        
        The zone is mapped on the unit sphere
        
        Returns:
            geographic zone triggering the events
        
        
        """
        ...

class FunctionalDetector(AbstractDetector['FunctionalDetector']):
    """
    A detector that implements the g function using a lambda that can be set using withFunction.
    
    For example, to create a simple date detector use:
    
    
     FunctionalDetector d = new FunctionalDetector()
         .withGFunction((s) -> s.getDate().durationFrom(triggerDate))
         .withMaxCheck(1e10);
     
    
    Since:
        9.2
    """
    def __init__(self):
        """
        Create an event detector with the default values. These are DEFAULT_MAX_CHECK, DEFAULT_THRESHOLD, DEFAULT_MAX_ITER, ContinueOnEvent, and a g function that is identically unity. protected FunctionalDetector (EventDetectionSettings detectionSettings, EventHandler handler, ToDoubleFunction<SpacecraftState> function)
        
        Private constructor.
        
        Parameters:
            detectionSettings (EventDetectionSettings): event detection settings
            handler (EventHandler): event handler to call at event occurrences
            function (ToDoubleFunction<SpacecraftState> function): the switching function.
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getFunction(self) -> java.util.function.ToDoubleFunction[org.orekit.propagation.SpacecraftState]:
        """
        Get the switching function.
        
        Returns:
            the function used in g.
        
        
        """
        ...
    def withFunction(self, newGFunction: typing.Union[java.util.function.ToDoubleFunction[org.orekit.propagation.SpacecraftState], typing.Callable[[org.orekit.propagation.SpacecraftState], float]]) -> 'FunctionalDetector':
        """
        Create a new event detector with a new g function, keeping all other attributes the same. It is recommended to use withMaxCheck and withThreshold to set appropriate values for this g function.
        
        Parameters:
            newGFunction (ToDoubleFunction<SpacecraftState> newGFunction): the new g function.
        
        Returns:
            a new detector with the new g function.
        
        
        """
        ...

class GeographicZoneDetector(AbstractDetector['GeographicZoneDetector']):
    """
    Detector for entry/exit of a zone defined by geographic boundaries.
    
    This detector identifies when a spacecraft crosses boundaries of general shapes defined on the surface of the globe. Typical shapes of interest can be countries, land masses or physical areas like the south atlantic anomaly. Shapes can be arbitrarily complicated: convex or non-convex, in one piece or several non-connected islands, they can include poles, they can have holes like the Caspian Sea (this would be a hole only if one is interested in land masses, of course). Complex shapes involve of course more computing time than simple shapes.
    
    Since:
        6.2
    
    Also see:
        FootprintOverlapDetector
    """
    @typing.overload
    def __init__(self, maxCheck: float, threshold: float, body: org.orekit.bodies.BodyShape, zone: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, margin: float): ...
    @typing.overload
    def __init__(self, body: org.orekit.bodies.BodyShape, zone: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, margin: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is the signed distance to boundary, minus the margin. It is positive if the spacecraft is outside of the zone and negative if it is inside.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            signed distance to boundary minus the margin
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.BodyShape:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getMargin(self) -> float:
        """
        Get the angular margin to apply (radians).
        
        Returns:
            the angular margin to apply (radians)
        
        
        """
        ...
    def getZone(self) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet:
        """
        Get the geographic zone.
        
        Returns:
            the geographic zone
        
        
        """
        ...
    def withMargin(self, newMargin: float) -> 'GeographicZoneDetector':
        """
        Setup the detector margin.
        
        Parameters:
            newMargin (double): angular margin to apply to the zone
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...

class GroundFieldOfViewDetector(AbstractDetector['GroundFieldOfViewDetector']):
    """
    Finder for satellite entry/exit events with respect to a sensor FieldOfView attached to an arbitrary frame.
    
    If you only want to compute access times then you should probably use ElevationDetector.
    
    The default implementation behavior is to Action propagation at FOV entry and to Action propagation at FOV exit. This can be changed by calling withHandler after construction.
    
    Since:
        7.1
    
    Also see:
        addEventDetector,
        FieldOfViewDetector, ElevationDetector
    """
    def __init__(self, frame: org.orekit.frames.Frame, fov: org.orekit.geometry.fov.FieldOfView):
        """
        Build a new instance.
        
        The maximal interval between distance to FOV boundary checks should be smaller than the half duration of the minimal pass to handle, otherwise some short passes could be missed.
        
        Parameters:
            frame (Frame): the reference frame attached to the sensor.
            fov (FieldOfView): Field Of View of the sensor.
        
        Since:
            10.1
        
        protected GroundFieldOfViewDetector (EventDetectionSettings detectionSettings, EventHandler handler, Frame frame, FieldOfView fov)
        
        Protected constructor with full parameters.
        
        This constructor is not public as users are expected to use the builder API with the various withXxx() methods to set up the instance in a readable manner without using a huge amount of parameters.
        
        Parameters:
            detectionSettings (EventDetectionSettings): event detection settings
            handler (EventHandler): event handler to call at event occurrences
            frame (Frame): the reference frame attached to the sensor.
            fov (FieldOfView): Field Of View of the sensor.
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        The g function value is the angular offset between the satellite and the offsetFromBoundary. It is negative if the satellite is visible within the Field Of View and positive if it is outside of the Field Of View, including the margin.
        
        As per the previous definition, when the satellite enters the Field Of View, a decreasing event is generated, and when the satellite leaves the Field Of View, an increasing event is generated.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getFOV(self) -> org.orekit.geometry.fov.FieldOfView:
        """
        Get the Field Of View.
        
        Returns:
            Field Of View
        
        Since:
            10.1
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the sensor reference frame.
        
        Returns:
            the reference frame attached to the sensor.
        
        
        """
        ...

class HaloXZPlaneCrossingDetector(AbstractDetector['HaloXZPlaneCrossingDetector']):
    """
    Detector for XZ Plane crossing.
    
    Since:
        10.2
    """
    def __init__(self, maxCheck: float, threshold: float):
        """
        Simple Constructor.
        
        Parameters:
            maxCheck (double): maximum checking interval (s)
            threshold (double): convergence threshold (s)
        
        protected HaloXZPlaneCrossingDetector (EventDetectionSettings detectionSettings, EventHandler handler)
        
        Protected constructor with full parameters.
        
        This constructor is not public as users are expected to use the builder API with the various withXxx() methods to set up the instance in a readable manner without using a huge amount of parameters.
        
        Parameters:
            detectionSettings (EventDetectionSettings): event detection settings
            handler (EventHandler): event handler to call at event occurrences
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            Position on Y axis
        
        
        """
        ...

class InterSatDirectViewDetector(AbstractDetector['InterSatDirectViewDetector']):
    """
    Detector for inter-satellites direct view (i.e. no masking by central body limb).
    
    As this detector needs two satellites, it embeds one PVCoordinatesProvider for the secondary satellite and is registered as an event detector in the propagator of the primary satellite. The secondary satellite provider will therefore be driven by this detector (and hence by the propagator in which this detector is registered).
    
    In order to avoid infinite recursion, care must be taken to have the secondary satellite provider being completely independent from anything else. In particular, if the provider is a propagator, it should not be run together in a PropagatorsParallelizer with the propagator this detector is registered in. It is fine however to configure two separate propagators PsA and PsB with similar settings for the secondary satellite and one propagator Pm for the primary satellite and then use Psa in this detector registered within Pm while Pm and Psb are run in the context of a PropagatorsParallelizer.
    
    For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally costly.
    
    The g function of this detector is positive when satellites can see each other directly and negative when the central body limb is in between and blocks the direct view.
    
    This detector only checks masking by central body limb, it does not take into account satellites antenna patterns. If these patterns must be considered, then this detector can be andCombine with the notCombine of FieldOfViewDetector.
    
    Since:
        9.3
    """
    def __init__(self, body: org.orekit.bodies.OneAxisEllipsoid, secondary: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]):
        """
        simple constructor.
        
        Parameters:
            body (OneAxisEllipsoid): central body
            secondary (PVCoordinatesProvider): provider for the secondary satellite
        
        protected InterSatDirectViewDetector (OneAxisEllipsoid body, double skimmingAltitude, PVCoordinatesProvider secondary, EventDetectionSettings detectionSettings, EventHandler handler)
        
        Protected constructor.
        
        Parameters:
            body (OneAxisEllipsoid): central body
            skimmingAltitude (double): skimming altitude at which events are triggered
            secondary (PVCoordinatesProvider): provider for the secondary satellite
            detectionSettings (EventDetectionSettings): detection settings
            handler (EventHandler): event handler to call at event occurrences
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        The g function of this detector is the difference between the minimum altitude of intermediate points along the line of sight between satellites and the getSkimmingAltitude. It is therefore positive when all intermediate points are above the skimming altitude, meaning satellites can see each other and it is negative when some intermediate points (which may be either endpoints) dive below this altitude, meaning satellites cannot see each other.
        
        Parameters:
            state (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getCentralBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the central body.
        
        Returns:
            central body
        
        
        """
        ...
    def getSecondary(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the provider for the secondary satellite.
        
        Returns:
            provider for the secondary satellite
        
        
        """
        ...
    def getSkimmingAltitude(self) -> float:
        """
        Get the skimming altitude.
        
        Returns:
            skimming altitude at which events are triggered
        
        Since:
            12.0
        
        
        """
        ...
    def withSkimmingAltitude(self, newSkimmingAltitude: float) -> 'InterSatDirectViewDetector':
        """
        Setup the skimming altitude.
        
        The skimming altitude is the lowest altitude of the path between satellites at which events should be triggered. If set to 0.0, events are triggered exactly when the path passes just at central body limb.
        
        Parameters:
            newSkimmingAltitude (double): skimming altitude (m)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        Also see:
            getSkimmingAltitude
        
        
        """
        ...

class LatitudeCrossingDetector(AbstractDetector['LatitudeCrossingDetector']):
    """
    Detector for geographic latitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed latitude with respect to a central body.
    
    Since:
        7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float): ...
    @typing.overload
    def __init__(self, body: org.orekit.bodies.OneAxisEllipsoid, latitude: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is the spacecraft latitude minus the fixed latitude to be crossed. It is positive if the spacecraft is northward and negative if it is southward with respect to the fixed latitude.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft latitude minus the fixed latitude to be crossed
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
        Get the fixed latitude to be crossed (radians).
        
        Returns:
            fixed latitude to be crossed (radians)
        
        
        """
        ...

class LatitudeExtremumDetector(AbstractDetector['LatitudeExtremumDetector']):
    """
    Detector for geographic latitude extremum.
    
    This detector identifies when a spacecraft reaches its extremum latitudes with respect to a central body.
    
    Since:
        7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, body: org.orekit.bodies.OneAxisEllipsoid): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is the spacecraft latitude time derivative.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft latitude time derivative
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.BodyShape:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...

class LatitudeRangeCrossingDetector(AbstractDetector['LatitudeRangeCrossingDetector']):
    """
    Detector for geographic latitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed latitude range with respect to a central body.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, body: org.orekit.bodies.OneAxisEllipsoid, fromLatitude: float, toLatitude: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is positive if the spacecraft latitude is inside the latitude range. It is positive if the spacecraft is northward to lower boundary range and southward to upper boundary range, with respect to the fixed latitude range.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            positive if spacecraft inside the range
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getFromLatitude(self) -> float:
        """
        Get the fixed latitude range to be crossed (radians), lower boundary.
        
        Returns:
            fixed lower boundary latitude range to be crossed (radians)
        
        
        """
        ...
    def getToLatitude(self) -> float:
        """
        Get the fixed latitude range to be crossed (radians), upper boundary.
        
        Returns:
            fixed lower boundary latitude range to be crossed (radians)
        
        
        """
        ...

class LongitudeCrossingDetector(AbstractDetector['LongitudeCrossingDetector']):
    """
    Detector for geographic longitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed longitude with respect to a central body.
    
    Since:
        7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float): ...
    @typing.overload
    def __init__(self, body: org.orekit.bodies.OneAxisEllipsoid, longitude: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is the longitude difference between the spacecraft and the fixed longitude to be crossed, with some sign tweaks to ensure continuity. These tweaks imply the increasing flag in events detection becomes irrelevant here! As an example, the longitude of a prograde spacecraft will always increase, but this g function will increase and decrease so it will cross the zero value once per orbit, in increasing and decreasing directions on alternate orbits. If eastwards and westwards crossing have to be distinguished, the velocity direction has to be checked instead of looking at the increasing flag.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            longitude difference between the spacecraft and the fixed longitude, with some sign tweaks to ensure continuity
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
        Get the fixed longitude to be crossed (radians).
        
        Returns:
            fixed longitude to be crossed (radians)
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface EventDetector
        
        Overrides: init in class AbstractDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class LongitudeExtremumDetector(AbstractDetector['LongitudeExtremumDetector']):
    """
    Detector for geographic longitude extremum.
    
    This detector identifies when a spacecraft reaches its extremum longitudes with respect to a central body.
    
    Since:
        7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, body: org.orekit.bodies.OneAxisEllipsoid): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is the spacecraft longitude time derivative.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft longitude time derivative
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.BodyShape:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...

class LongitudeRangeCrossingDetector(AbstractDetector['LongitudeRangeCrossingDetector']):
    """
    Detector for geographic longitude crossing.
    
    This detector identifies when a spacecraft crosses a fixed longitude range with respect to a central body.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, body: org.orekit.bodies.OneAxisEllipsoid, fromLongitude: float, toLongitude: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is positive if the spacecraft longitude is inside the longitude range. The longitude value is reflected from [-PI, +PI] to [0, 2 PI] to ensure continuity.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            positive if spacecraft inside the range
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Get the body on which the geographic zone is defined.
        
        Returns:
            body on which the geographic zone is defined
        
        
        """
        ...
    def getFromLongitude(self) -> float:
        """
        Get the fixed longitude range to be crossed (radians), lower boundary.
        
        Returns:
            fixed lower boundary longitude range to be crossed (radians)
        
        
        """
        ...
    def getToLongitude(self) -> float:
        """
        Get the fixed longitude range to be crossed (radians), upper boundary.
        
        Returns:
            fixed upper boundary longitude range to be crossed (radians)
        
        
        """
        ...

class MagneticFieldDetector(AbstractDetector['MagneticFieldDetector']):
    """
    Detector for Earth magnetic field strength.
    
    The detector is based on the field intensity calculated at the satellite's latitude and longitude, either at sea level or at satellite altitude, depending on the value chosen for the atSeaLevel indicator.
    
    It can detect flyovers of the South-Atlantic anomaly with a classically accepted limit value of 32,000 nT at sea level.
    """
    @typing.overload
    def __init__(self, maxCheck: float, threshold: float, limit: float, model: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, body: org.orekit.bodies.OneAxisEllipsoid, atSeaLevel: bool): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, fieldModel: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, boolean: bool, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, limit: float, model: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, body: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, limit: float, model: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, body: org.orekit.bodies.OneAxisEllipsoid, atSeaLevel: bool): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The returned value is the difference between the field intensity at spacecraft location, taking atSeaLevel switch into account, and the fixed threshold value.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            difference between the field intensity at spacecraft location and the fixed threshold value
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface EventDetector
        
        Overrides: init in class AbstractDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class NegateDetector(AbstractDetector['NegateDetector'], DetectorModifier):
    """
    An event detector that negates the sign on another event detector's g function.
    """
    def __init__(self, original: EventDetector):
        """
        Create a new event detector that negates an existing event detector.
        
        This detector will be initialized with the same getMaxCheckInterval, getThreshold, and getMaxIterationCount as original. Initially this detector will use the ContinueOnEvent event handler.
        
        Parameters:
            original (EventDetector): detector.
        
        protected NegateDetector (EventDetectionSettings eventDetectionSettings, EventHandler newHandler, EventDetector original)
        
        Private constructor.
        
        Parameters:
            eventDetectionSettings (EventDetectionSettings): event detection settings.
            newHandler (EventHandler): event handler.
            original (EventDetector): event detector.
        
        Since:
            13.0
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Specified by: g in interface DetectorModifier
        
        Specified by: g in interface EventDetector
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDetector(self) -> EventDetector:
        """
        Description copied from interface: getDetector Get the wrapped detector.
        
        Specified by: getDetector in interface DetectorModifier
        
        Returns:
            wrapped detector
        
        
        """
        ...
    def getOriginal(self) -> EventDetector:
        """
        Get the delegate event detector.
        
        Returns:
            the delegate event detector
        
        Since:
            10.2
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Description copied from class: init Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface DetectorModifier
        
        Specified by: init in interface EventDetector
        
        Overrides: init in class AbstractDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class NodeDetector(AbstractDetector['NodeDetector']):
    """
    Finder for node crossing events.
    
    This class finds equator crossing events (i.e. ascending or descending node crossing).
    
    The default implementation behavior is to Action propagation at descending node crossing and to Action propagation at ascending node crossing. This can be changed by calling withHandler after construction.
    
    Beware that node detection will fail for almost equatorial orbits. If for example a node detector is used to trigger an ImpulseManeuver and the maneuver turn the orbit plane to equator, then the detector may completely fail just after the maneuver has been performed! This is a real case that has been encountered during validation ...
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, double: float, orbit: org.orekit.orbits.Orbit, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, frame: org.orekit.frames.Frame): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function computes the Z position in the defined frame.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the equator is defined.
        
        Returns:
            the frame in which the equator is defined
        
        
        """
        ...

class ParameterDrivenDateIntervalDetector(AbstractDetector['ParameterDrivenDateIntervalDetector']):
    """
    Detector for date intervals that may be offset thanks to parameter drivers.
    
    Two dual views can be used for date intervals: either start date/stop date or median date/duration. getStartDriver/getStopDriver drivers and getMedianDriver/getDurationDriver drivers work in pair. Both drivers in one pair can be selected and their changes will be propagated to the other pair, but attempting to select drivers in both pairs at the same time will trigger an exception. Changing the value of a driver that is not selected should be avoided as it leads to inconsistencies between the pairs. . Warning, startDate driver, stopDate driver, duration driver and medianDate driver must all have the same number of values to estimate (same number of span in valueSpanMap), that is is to say that the addSpans should be called with same arguments.
    
    Since:
        11.1
    
    Also see:
        addEventDetector
    """
    START_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for start driver.
    
    Also see:
        constant
    
    
    """
    STOP_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for stop driver.
    
    Also see:
        constant
    
    
    """
    MEDIAN_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for median driver.
    
    Also see:
        constant
    
    
    """
    DURATION_SUFFIX: typing.ClassVar[str] = ...
    """
    Default suffix for duration driver.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function.
        
        The function is positive for dates within the interval defined by applying the parameter drivers shifts to reference dates, and negative for dates outside of this interval. Note that if Δt_start - Δt_stop is less than ref_stop.durationFrom(ref_start), then the interval degenerates to empty and the function never reaches positive values.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    @staticmethod
    def getDefaultDetectionSettings(refStart: org.orekit.time.AbsoluteDate, refStop: org.orekit.time.AbsoluteDate) -> EventDetectionSettings:
        """
        Get default detection settings.
        
        Parameters:
            refStart (AbsoluteDate): reference interval start date
            refStop (AbsoluteDate): reference interval stop date
        
        Returns:
            default detection settings
        
        Since:
            13.0
        
        
        """
        ...
    def getDurationDriver(self) -> org.orekit.utils.ParameterDriver:
        """
        Get the driver for duration.
        
        Note that the duration is automatically adjusted if either getStartDriver start date or getStopDriver are isSelected changed.
        
        Returns:
            driver for duration
        
        
        """
        ...
    def getMedianDriver(self) -> org.orekit.utils.DateDriver:
        """
        Get the driver for median date.
        
        Note that the median date is automatically adjusted if either getStartDriver start date or getStopDriver are isSelected changed.
        
        Returns:
            driver for median date
        
        
        """
        ...
    def getStartDriver(self) -> org.orekit.utils.DateDriver:
        """
        Get the driver for start date.
        
        Note that the start date is automatically adjusted if either getMedianDriver or getDurationDriver are isSelected and changed.
        
        Returns:
            driver for start date
        
        
        """
        ...
    def getStopDriver(self) -> org.orekit.utils.DateDriver:
        """
        Get the driver for stop date.
        
        Note that the stop date is automatically adjusted if either getMedianDriver or getDurationDriver are isSelected changed.
        
        Returns:
            driver for stop date
        
        
        """
        ...

class PositionAngleDetector(AbstractDetector['PositionAngleDetector']):
    """
    Detector for in-orbit position angle.
    
    The detector is based on anomaly for KEPLERIAN orbits, latitude argument for CIRCULAR orbits, or longitude argument for EQUINOCTIAL orbits. It does not support CARTESIAN orbits. The angles can be either TRUE, MEAN or ECCENTRIC angles.
    
    Since:
        7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, double3: float): ...
    @typing.overload
    def __init__(self, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, angle: float): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is the angle difference between the spacecraft and the fixed angle to be crossed, with some sign tweaks to ensure continuity. These tweaks imply the increasing flag in events detection becomes irrelevant here! As an example, the angle always increase in a Keplerian orbit, but this g function will increase and decrease so it will cross the zero value once per orbit, in increasing and decreasing directions on alternate orbits..
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            angle difference between the spacecraft and the fixed angle, with some sign tweaks to ensure continuity
        
        
        """
        ...
    def getAngle(self) -> float:
        """
        Get the fixed angle to be crossed (radians).
        
        Returns:
            fixed angle to be crossed (radians)
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get the orbit type defining the angle type.
        
        Returns:
            orbit type defining the angle type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get the type of position angle.
        
        Returns:
            type of position angle
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize event detector at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface EventDetector
        
        Overrides: init in class AbstractDetector
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

_PythonAbstractDetector__T = typing.TypeVar('_PythonAbstractDetector__T', bound=AbstractDetector)  # <T>
class PythonAbstractDetector(AbstractDetector[_PythonAbstractDetector__T], typing.Generic[_PythonAbstractDetector__T]):
    """
    Common parts shared by several orbital events finders.
    
    Also see:
        addEventDetector
    """
    @typing.overload
    def __init__(self, maxCheck: float, threshold: float, maxIter: int, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]): ...
    @typing.overload
    def __init__(self, detectionSettings: EventDetectionSettings, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]): ...
    def create(self, detectionSettings: EventDetectionSettings, newHandler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]) -> _PythonAbstractDetector__T:
        """
        Build a new instance.
        
        Specified by: create in class AbstractDetector
        
        Parameters:
            detectionSettings (EventDetectionSettings): detection settings
            newHandler (EventHandler): event handler to call at event occurrences
        
        Returns:
            a new instance of the appropriate sub-type
        
        
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
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
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

class PythonDetectorModifier(DetectorModifier):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDetector(self) -> EventDetector:
        """
        Get the wrapped detector.
        
        Specified by: getDetector in interface DetectorModifier
        
        Returns:
            wrapped detector
        
        
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

_PythonFieldAbstractDetector__D = typing.TypeVar('_PythonFieldAbstractDetector__D', bound=FieldAbstractDetector)  # <D>
_PythonFieldAbstractDetector__T = typing.TypeVar('_PythonFieldAbstractDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractDetector(FieldAbstractDetector[_PythonFieldAbstractDetector__D, _PythonFieldAbstractDetector__T], typing.Generic[_PythonFieldAbstractDetector__D, _PythonFieldAbstractDetector__T]):
    def __init__(self, detectionSettings: FieldEventDetectionSettings[_PythonFieldAbstractDetector__T], handler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_PythonFieldAbstractDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]):
        """
        Build a new instance.
        
        Parameters:
            detectionSettings (FieldEventDetectionSettings<PythonFieldAbstractDetector> detectionSettings): event detection settings
            handler (FieldEventHandler<PythonFieldAbstractDetector> handler): event handler to call at event occurrences
        
        Since:
            12.2
        
        
        """
        ...
    def create(self, detectionSettings: FieldEventDetectionSettings[_PythonFieldAbstractDetector__T], newHandler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_PythonFieldAbstractDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]) -> _PythonFieldAbstractDetector__D:
        """
        Build a new instance.
        
        Specified by: create in class FieldAbstractDetector
        
        Parameters:
            detectionSettings (FieldEventDetectionSettings<PythonFieldAbstractDetector> detectionSettings): detection settings
            newHandler (FieldEventHandler<PythonFieldAbstractDetector> newHandler): event handler to call at event occurrences
        
        Returns:
            a new instance of the appropriate sub-type
        
        
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
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAbstractDetector__T]) -> _PythonFieldAbstractDetector__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (FieldSpacecraftState<PythonFieldAbstractDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
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

_PythonFieldDetectorModifier__T = typing.TypeVar('_PythonFieldDetectorModifier__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldDetectorModifier(FieldDetectorModifier[_PythonFieldDetectorModifier__T], typing.Generic[_PythonFieldDetectorModifier__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDetector(self) -> FieldEventDetector[_PythonFieldDetectorModifier__T]:
        """
        Getter for wrapped detector.
        
        Specified by: getDetector in interface FieldDetectorModifier
        
        Returns:
            detector
        
        
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

class RelativeDistanceDetector(AbstractDetector['RelativeDistanceDetector']):
    """
    Detector of specific value for the distance relative to another trajectory (using the Euclidean norm).
    
    The default implementation behavior is to Action propagation. This can be changed by calling withHandler after construction.
    
    As this detector needs two objects (moving relative to each other), it embeds one PVCoordinatesProvider for the secondary object and is registered as an event detector in the propagator of the primary object. The secondary object PVCoordinatesProvider will therefore be driven by this detector (and hence by the propagator in which this detector is registered).
    
    **In order to avoid infinite recursion, care must be taken to have the secondary object provider being completely independent from anything else. In particular, if the provider is a propagator, it should not be run together in a PropagatorsParallelizer with the propagator this detector is registered in. It is fine however to configure two separate propagators PsA and PsB with similar settings for the secondary object and one propagator Pm for the primary object and then use Psa in this detector registered within Pm while Pm and Psb are run in the context of a PropagatorsParallelizer.**
    
    For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally costly.
    
    Since:
        12.1
    
    Also see:
        addEventDetector
    """
    def __init__(self, secondaryPVProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], distanceThreshold: float):
        """
        Constructor with default values.
        
        By default, the implemented behavior is to Action propagation at detection.
        
        Parameters:
            secondaryPVProvider (PVCoordinatesProvider): PVCoordinates provider of the other object defining relative distance.
            distanceThreshold (double): Relative distance threshold for event detection
        
        protected RelativeDistanceDetector (EventDetectionSettings detectionSettings, EventHandler handler, PVCoordinatesProvider secondaryPVProvider, double distanceThreshold)
        
        Constructor.
        
        This constructor is to be used if the user wants to change the default behavior of the detector.
        
        Parameters:
            detectionSettings (EventDetectionSettings): Detection settings
            handler (EventHandler): Event handler to call at event occurrences.
            secondaryPVProvider (PVCoordinatesProvider): PVCoordinates provider of the other object defining relative distance.
            distanceThreshold (double): Relative distance threshold for event detection
        
        Since:
            12.2
        
        Also see:
            EventHandler
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        The g is positive when the relative distance is larger or equal than the threshold, non-positive otherwise.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getDistanceThreshold(self) -> float:
        """
        Get the relative distance threshold.
        
        Returns:
            threshold triggering detection
        
        
        """
        ...
    def getSecondaryPVProvider(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
        Get the secondary position-velocity provider stored in this instance.
        
        Returns:
            the secondary position-velocity provider stored in this instance
        
        
        """
        ...

class TimeIntervalDetector(AbstractDetector['TimeIntervalDetector']):
    """
    Detector for time intervals. Positive whenever the date is inside, negative otherwise.
    
    Since:
        13.1
    
    Also see:
        TimeInterval
    """
    @typing.overload
    def __init__(self, detectionSettings: EventDetectionSettings, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable], timeInterval: org.orekit.time.TimeInterval): ...
    @typing.overload
    def __init__(self, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable], timeInterval: org.orekit.time.TimeInterval): ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Description copied from interface: g Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getTimeInterval(self) -> org.orekit.time.TimeInterval:
        """
        Getter for the time interval.
        
        Returns:
            interval
        
        
        """
        ...

class ElevationDetector(AbstractTopocentricDetector['ElevationDetector']):
    """
    Finder for satellite raising/setting events that allows for the setting of azimuth and/or elevation bounds or a ground azimuth/elevation mask input. Each calculation be configured to use atmospheric refraction as well.
    
    The default implementation behavior is to Action propagation at raising and to Action propagation at setting. This can be changed by calling withHandler after construction.
    
    Since:
        6.1
    """
    @typing.overload
    def __init__(self, maxCheck: float, threshold: float, topo: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, topo: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, maxCheck: typing.Union[org.orekit.propagation.events.intervals.AdaptableInterval, typing.Callable], threshold: float, topo: org.orekit.frames.TopocentricFrame): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function measures the difference between the current elevation (and azimuth if necessary) and the reference mask or minimum value.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getElevationMask(self) -> org.orekit.utils.ElevationMask:
        """
        Returns the currently configured elevation mask.
        
        Returns:
            elevation mask (null if instance has been configured with
            withConstantElevation
        
        Also see:
            withElevationMask
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
        Returns the currently configured minimum valid elevation value.
        
        Returns:
            minimum elevation value (NaN if instance has been configured with
            withElevationMask
        
        Also see:
            withConstantElevation
        
        
        """
        ...
    def getRefractionModel(self) -> org.orekit.models.AtmosphericRefractionModel:
        """
        Returns the currently configured refraction model.
        
        Returns:
            refraction model
        
        Also see:
            withRefraction
        
        
        """
        ...
    def withConstantElevation(self, newMinElevation: float) -> 'ElevationDetector':
        """
        Setup the minimum elevation for detection.
        
        This will override an elevation mask if it has been configured as such previously.
        
        Parameters:
            newMinElevation (double): minimum elevation for visibility in radians (rad)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            getMinElevation
        
        
        """
        ...
    def withElevationMask(self, newElevationMask: org.orekit.utils.ElevationMask) -> 'ElevationDetector':
        """
        Setup the elevation mask for detection using the passed in mask object.
        
        Parameters:
            newElevationMask (ElevationMask): elevation mask to use for the computation
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            getElevationMask
        
        
        """
        ...
    def withRefraction(self, newRefractionModel: typing.Union[org.orekit.models.AtmosphericRefractionModel, typing.Callable]) -> 'ElevationDetector':
        """
        Setup the elevation detector to use an atmospheric refraction model in its calculations.
        
        To disable the refraction when copying an existing elevation detector, call this method with a null argument.
        
        Parameters:
            newRefractionModel (AtmosphericRefractionModel): refraction model to use for the computation
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            getRefractionModel
        
        
        """
        ...

class ElevationExtremumDetector(AbstractTopocentricDetector['ElevationExtremumDetector']):
    """
    Detector for elevation extremum with respect to a ground point.
    
    This detector identifies when a spacecraft reaches its extremum elevation with respect to a ground point.
    
    As in most cases only the elevation maximum is needed and the minimum is often irrelevant, this detector is often wrapped into an EventSlopeFilter configured with TRIGGER_ONLY_DECREASING_EVENTS (i.e. when the elevation derivative decreases from positive values to negative values, which correspond to a maximum). Setting up this filter saves some computation time as the elevation minimum occurrences are not even looked at. It is however still often necessary to do an additional filtering
    
    Since:
        7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, topo: org.orekit.frames.TopocentricFrame): ...
    def g(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the detection function.
        
        The value is the spacecraft elevation first time derivative.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft elevation first time derivative
        
        
        """
        ...
    def getElevation(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Get the elevation value.
        
        Parameters:
            s (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft elevation
        
        
        """
        ...

_FieldElevationDetector__T = typing.TypeVar('_FieldElevationDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldElevationDetector(FieldAbstractTopocentricDetector['FieldElevationDetector'[_FieldElevationDetector__T], _FieldElevationDetector__T], typing.Generic[_FieldElevationDetector__T]):
    """
    Finder for satellite raising/setting events that allows for the setting of azimuth and/or elevation bounds or a ground azimuth/elevation mask input. Each calculation be configured to use atmospheric refraction as well.
    
    The default implementation behavior is to Action propagation at raising and to Action propagation at setting. This can be changed by calling withHandler after construction.
    """
    @typing.overload
    def __init__(self, maxCheck: _FieldElevationDetector__T, threshold: _FieldElevationDetector__T, topo: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldElevationDetector__T], topo: org.orekit.frames.TopocentricFrame): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldElevationDetector__T]) -> _FieldElevationDetector__T:
        """
        Compute the value of the switching function. This function measures the difference between the current elevation (and azimuth if necessary) and the reference mask or minimum value.
        
        Parameters:
            s (FieldSpacecraftState<FieldElevationDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...
    def getElevationMask(self) -> org.orekit.utils.ElevationMask:
        """
        Returns the currently configured elevation mask.
        
        Returns:
            elevation mask (null if instance has been configured with
            withConstantElevation
        
        Also see:
            withElevationMask
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
        Returns the currently configured minimum valid elevation value.
        
        Returns:
            minimum elevation value (NaN if instance has been configured with
            withElevationMask
        
        Also see:
            withConstantElevation
        
        
        """
        ...
    def getRefractionModel(self) -> org.orekit.models.AtmosphericRefractionModel:
        """
        Returns the currently configured refraction model.
        
        Returns:
            refraction model
        
        Also see:
            withRefraction
        
        
        """
        ...
    def withConstantElevation(self, newMinElevation: float) -> 'FieldElevationDetector'[_FieldElevationDetector__T]:
        """
        Setup the minimum elevation for detection.
        
        This will override an elevation mask if it has been configured as such previously.
        
        Parameters:
            newMinElevation (double): minimum elevation for visibility in radians (rad)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            getMinElevation
        
        
        """
        ...
    def withElevationMask(self, newElevationMask: org.orekit.utils.ElevationMask) -> 'FieldElevationDetector'[_FieldElevationDetector__T]:
        """
        Setup the elevation mask for detection using the passed in mask object.
        
        Parameters:
            newElevationMask (ElevationMask): elevation mask to use for the computation
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            getElevationMask
        
        
        """
        ...
    def withRefraction(self, newRefractionModel: typing.Union[org.orekit.models.AtmosphericRefractionModel, typing.Callable]) -> 'FieldElevationDetector'[_FieldElevationDetector__T]:
        """
        Setup the elevation detector to use an atmospheric refraction model in its calculations.
        
        To disable the refraction when copying an existing elevation detector, call this method with a null argument.
        
        Parameters:
            newRefractionModel (AtmosphericRefractionModel): refraction model to use for the computation
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            6.1
        
        Also see:
            getRefractionModel
        
        
        """
        ...

_FieldElevationExtremumDetector__T = typing.TypeVar('_FieldElevationExtremumDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldElevationExtremumDetector(FieldAbstractTopocentricDetector['FieldElevationExtremumDetector'[_FieldElevationExtremumDetector__T], _FieldElevationExtremumDetector__T], typing.Generic[_FieldElevationExtremumDetector__T]):
    """
    Detector for elevation extremum with respect to a ground point.
    
    This detector identifies when a spacecraft reaches its extremum elevation with respect to a ground point.
    
    As in most cases only the elevation maximum is needed and the minimum is often irrelevant, this detector is often wrapped into an FieldEventSlopeFilter configured with TRIGGER_ONLY_DECREASING_EVENTS (i.e. when the elevation derivative decreases from positive values to negative values, which correspond to a maximum). Setting up this filter saves some computation time as the elevation minimum occurrences are not even looked at. It is however still often necessary to do an additional filtering
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, t: _FieldElevationExtremumDetector__T, t2: _FieldElevationExtremumDetector__T, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldElevationExtremumDetector__T], topo: org.orekit.frames.TopocentricFrame): ...
    def g(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldElevationExtremumDetector__T]) -> _FieldElevationExtremumDetector__T:
        """
        Compute the value of the detection function.
        
        The value is the spacecraft elevation first time derivative.
        
        Parameters:
            s (FieldSpacecraftState<FieldElevationExtremumDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft elevation first time derivative
        
        
        """
        ...
    def getElevation(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldElevationExtremumDetector__T]) -> _FieldElevationExtremumDetector__T:
        """
        Get the elevation value.
        
        Parameters:
            s (FieldSpacecraftState<FieldElevationExtremumDetector> s): the current state information: date, kinematics, attitude
        
        Returns:
            spacecraft elevation
        
        
        """
        ...

_FieldGroundAtNightDetector__T = typing.TypeVar('_FieldGroundAtNightDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGroundAtNightDetector(FieldAbstractTopocentricDetector['FieldGroundAtNightDetector'[_FieldGroundAtNightDetector__T], _FieldGroundAtNightDetector__T], typing.Generic[_FieldGroundAtNightDetector__T]):
    """
    Detector for ground location being at night.
    
    This detector is mainly useful for scheduling optical measurements (either passive telescope observation of satellites against the stars background or active satellite laser ranging).
    
    The g function of this detector is positive when ground is at night (i.e. Sun is below dawn/dusk elevation angle).
    
    Since:
        13.1
    
    Also see:
        GroundAtNightDetector
    """
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], dawnDuskElevation: _FieldGroundAtNightDetector__T, refractionModel: typing.Union[org.orekit.models.AtmosphericRefractionModel, typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            topocentricFrame (TopocentricFrame): ground location to check
            sun (ExtendedPositionProvider): provider for Sun position
            dawnDuskElevation (FieldGroundAtNightDetector): Sun elevation below which we consider night is dark enough (rad)
            refractionModel (AtmosphericRefractionModel): reference to refraction model (null if refraction should be ignored)
        
        protected FieldGroundAtNightDetector (TopocentricFrame topocentricFrame, ExtendedPositionProvider sun, FieldGroundAtNightDetector dawnDuskElevation, AtmosphericRefractionModel refractionModel, FieldEventDetectionSettings<FieldGroundAtNightDetector> detectionSettings, FieldEventHandler<FieldGroundAtNightDetector> handler)
        
        Private constructor.
        
        Parameters:
            topocentricFrame (TopocentricFrame): ground location from which measurement is performed
            sun (ExtendedPositionProvider): provider for Sun position
            dawnDuskElevation (FieldGroundAtNightDetector): Sun elevation below which we consider night is dark enough (rad)
            refractionModel (AtmosphericRefractionModel): reference to refraction model (null if refraction should be ignored),
            detectionSettings (FieldEventDetectionSettings<FieldGroundAtNightDetector> detectionSettings): event detection settings
            handler (FieldEventHandler<FieldGroundAtNightDetector> handler): event handler to call at event occurrences
        
        
        """
        ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Description copied from interface: dependsOnTimeOnly Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldGroundAtNightDetector__T]) -> _FieldGroundAtNightDetector__T:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        The g function of this detector is positive when ground is at night (i.e. Sun is below dawn/dusk elevation angle).
        
        This function only depends on date, not on the actual position of the spacecraft.
        
        Parameters:
            state (FieldSpacecraftState<FieldGroundAtNightDetector> state): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...

class GroundAtNightDetector(AbstractTopocentricDetector['GroundAtNightDetector']):
    """
    Detector for ground location being at night.
    
    This detector is mainly useful for scheduling optical measurements (either passive telescope observation of satellites against the stars background or active satellite laser ranging).
    
    The g function of this detector is positive when ground is at night (i.e. Sun is below dawn/dusk elevation angle).
    
    Since:
        9.3
    """
    CIVIL_DAWN_DUSK_ELEVATION: typing.ClassVar[float] = ...
    """
    Sun elevation at civil dawn/dusk (6° below horizon).
    """
    NAUTICAL_DAWN_DUSK_ELEVATION: typing.ClassVar[float] = ...
    """
    Sun elevation at nautical dawn/dusk (12° below horizon).
    """
    ASTRONOMICAL_DAWN_DUSK_ELEVATION: typing.ClassVar[float] = ...
    """
    Sun elevation at astronomical dawn/dusk (18° below horizon).
    """
    def __init__(self, groundLocation: org.orekit.frames.TopocentricFrame, sun: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], dawnDuskElevation: float, refractionModel: typing.Union[org.orekit.models.AtmosphericRefractionModel, typing.Callable]):
        """
        Simple constructor.
        
        Beware that EarthStandardAtmosphereRefraction does apply only for elevations above -2°. It is therefore not suitable for used with CIVIL_DAWN_DUSK_ELEVATION (-6°), NAUTICAL_DAWN_DUSK_ELEVATION (-12°) or ASTRONOMICAL_DAWN_DUSK_ELEVATION (-18°). The ITURP834AtmosphericRefraction which can compute refraction at large negative elevations should be preferred.
        
        Parameters:
            groundLocation (TopocentricFrame): ground location to check
            sun (PVCoordinatesProvider): provider for Sun position
            dawnDuskElevation (double): Sun elevation below which we consider night is dark enough (rad) (typically
                ASTRONOMICAL_DAWN_DUSK_ELEVATION)
            refractionModel (AtmosphericRefractionModel): reference to refraction model (null if refraction should be ignored)
        
        protected GroundAtNightDetector (TopocentricFrame groundLocation, PVCoordinatesProvider sun, double dawnDuskElevation, AtmosphericRefractionModel refractionModel, EventDetectionSettings detectionSettings, EventHandler handler)
        
        Private constructor.
        
        Parameters:
            groundLocation (TopocentricFrame): ground location from which measurement is performed
            sun (PVCoordinatesProvider): provider for Sun position
            dawnDuskElevation (double): Sun elevation below which we consider night is dark enough (rad) (typically
                ASTRONOMICAL_DAWN_DUSK_ELEVATION)
            refractionModel (AtmosphericRefractionModel): reference to refraction model (null if refraction should be ignored),
            detectionSettings (EventDetectionSettings): event detection settings
            handler (EventHandler): event handler to call at event occurrences
        
        Since:
            13.0
        
        
        """
        ...
    def dependsOnTimeOnly(self) -> bool:
        """
        Description copied from interface: dependsOnTimeOnly Method returning true if and only if the detection function g does not depend on dependent variables, just the independent one i.e. time. This information is used for performance in propagation.
        
        Returns:
            flag
        
        
        """
        ...
    def g(self, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as the integrator will need to find its roots to locate the events.
        
        The g function of this detector is positive when ground is at night (i.e. Sun is below dawn/dusk elevation angle).
        
        This function only depends on date, not on the actual position of the spacecraft.
        
        Parameters:
            state (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            value of the switching function
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events")``.

    AbstractDetector: typing.Type[AbstractDetector]
    AbstractTopocentricDetector: typing.Type[AbstractTopocentricDetector]
    AdapterDetector: typing.Type[AdapterDetector]
    AlignmentDetector: typing.Type[AlignmentDetector]
    AltitudeDetector: typing.Type[AltitudeDetector]
    AngularSeparationDetector: typing.Type[AngularSeparationDetector]
    AngularSeparationFromSatelliteDetector: typing.Type[AngularSeparationFromSatelliteDetector]
    ApsideDetector: typing.Type[ApsideDetector]
    BetaAngleDetector: typing.Type[BetaAngleDetector]
    BooleanDetector: typing.Type[BooleanDetector]
    CylindricalShadowEclipseDetector: typing.Type[CylindricalShadowEclipseDetector]
    DateDetector: typing.Type[DateDetector]
    DetectorModifier: typing.Type[DetectorModifier]
    EclipseDetector: typing.Type[EclipseDetector]
    ElevationDetector: typing.Type[ElevationDetector]
    ElevationExtremumDetector: typing.Type[ElevationExtremumDetector]
    EnablingPredicate: typing.Type[EnablingPredicate]
    EventDetectionSettings: typing.Type[EventDetectionSettings]
    EventDetector: typing.Type[EventDetector]
    EventDetectorsProvider: typing.Type[EventDetectorsProvider]
    EventEnablingPredicateFilter: typing.Type[EventEnablingPredicateFilter]
    EventShifter: typing.Type[EventShifter]
    EventSlopeFilter: typing.Type[EventSlopeFilter]
    EventState: typing.Type[EventState]
    EventsLogger: typing.Type[EventsLogger]
    ExtremumAngularSeparationDetector: typing.Type[ExtremumAngularSeparationDetector]
    ExtremumApproachDetector: typing.Type[ExtremumApproachDetector]
    FieldAbstractDetector: typing.Type[FieldAbstractDetector]
    FieldAbstractTopocentricDetector: typing.Type[FieldAbstractTopocentricDetector]
    FieldAdapterDetector: typing.Type[FieldAdapterDetector]
    FieldAltitudeDetector: typing.Type[FieldAltitudeDetector]
    FieldAngularSeparationDetector: typing.Type[FieldAngularSeparationDetector]
    FieldApsideDetector: typing.Type[FieldApsideDetector]
    FieldBetaAngleDetector: typing.Type[FieldBetaAngleDetector]
    FieldBooleanDetector: typing.Type[FieldBooleanDetector]
    FieldCylindricalShadowEclipseDetector: typing.Type[FieldCylindricalShadowEclipseDetector]
    FieldDateDetector: typing.Type[FieldDateDetector]
    FieldDetectorModifier: typing.Type[FieldDetectorModifier]
    FieldEclipseDetector: typing.Type[FieldEclipseDetector]
    FieldElevationDetector: typing.Type[FieldElevationDetector]
    FieldElevationExtremumDetector: typing.Type[FieldElevationExtremumDetector]
    FieldEnablingPredicate: typing.Type[FieldEnablingPredicate]
    FieldEventDetectionSettings: typing.Type[FieldEventDetectionSettings]
    FieldEventDetector: typing.Type[FieldEventDetector]
    FieldEventEnablingPredicateFilter: typing.Type[FieldEventEnablingPredicateFilter]
    FieldEventShifter: typing.Type[FieldEventShifter]
    FieldEventSlopeFilter: typing.Type[FieldEventSlopeFilter]
    FieldEventState: typing.Type[FieldEventState]
    FieldEventsLogger: typing.Type[FieldEventsLogger]
    FieldExtremumAngularSeparationDetector: typing.Type[FieldExtremumAngularSeparationDetector]
    FieldExtremumApproachDetector: typing.Type[FieldExtremumApproachDetector]
    FieldFunctionalDetector: typing.Type[FieldFunctionalDetector]
    FieldGroundAtNightDetector: typing.Type[FieldGroundAtNightDetector]
    FieldLatitudeCrossingDetector: typing.Type[FieldLatitudeCrossingDetector]
    FieldLatitudeRangeCrossingDetector: typing.Type[FieldLatitudeRangeCrossingDetector]
    FieldLongitudeCrossingDetector: typing.Type[FieldLongitudeCrossingDetector]
    FieldLongitudeRangeCrossingDetector: typing.Type[FieldLongitudeRangeCrossingDetector]
    FieldNegateDetector: typing.Type[FieldNegateDetector]
    FieldNodeDetector: typing.Type[FieldNodeDetector]
    FieldOfViewDetector: typing.Type[FieldOfViewDetector]
    FieldParameterDrivenDateIntervalDetector: typing.Type[FieldParameterDrivenDateIntervalDetector]
    FieldRelativeDistanceDetector: typing.Type[FieldRelativeDistanceDetector]
    FieldTimeIntervalDetector: typing.Type[FieldTimeIntervalDetector]
    FilterType: typing.Type[FilterType]
    FootprintOverlapDetector: typing.Type[FootprintOverlapDetector]
    FunctionalDetector: typing.Type[FunctionalDetector]
    GeographicZoneDetector: typing.Type[GeographicZoneDetector]
    GroundAtNightDetector: typing.Type[GroundAtNightDetector]
    GroundFieldOfViewDetector: typing.Type[GroundFieldOfViewDetector]
    HaloXZPlaneCrossingDetector: typing.Type[HaloXZPlaneCrossingDetector]
    InterSatDirectViewDetector: typing.Type[InterSatDirectViewDetector]
    LatitudeCrossingDetector: typing.Type[LatitudeCrossingDetector]
    LatitudeExtremumDetector: typing.Type[LatitudeExtremumDetector]
    LatitudeRangeCrossingDetector: typing.Type[LatitudeRangeCrossingDetector]
    LongitudeCrossingDetector: typing.Type[LongitudeCrossingDetector]
    LongitudeExtremumDetector: typing.Type[LongitudeExtremumDetector]
    LongitudeRangeCrossingDetector: typing.Type[LongitudeRangeCrossingDetector]
    MagneticFieldDetector: typing.Type[MagneticFieldDetector]
    NegateDetector: typing.Type[NegateDetector]
    NodeDetector: typing.Type[NodeDetector]
    ParameterDrivenDateIntervalDetector: typing.Type[ParameterDrivenDateIntervalDetector]
    PositionAngleDetector: typing.Type[PositionAngleDetector]
    PythonAbstractDetector: typing.Type[PythonAbstractDetector]
    PythonDetectorModifier: typing.Type[PythonDetectorModifier]
    PythonEnablingPredicate: typing.Type[PythonEnablingPredicate]
    PythonEventDetector: typing.Type[PythonEventDetector]
    PythonEventDetectorsProvider: typing.Type[PythonEventDetectorsProvider]
    PythonFieldAbstractDetector: typing.Type[PythonFieldAbstractDetector]
    PythonFieldDetectorModifier: typing.Type[PythonFieldDetectorModifier]
    PythonFieldEnablingPredicate: typing.Type[PythonFieldEnablingPredicate]
    PythonFieldEventDetector: typing.Type[PythonFieldEventDetector]
    RelativeDistanceDetector: typing.Type[RelativeDistanceDetector]
    TimeIntervalDetector: typing.Type[TimeIntervalDetector]
    VisibilityTrigger: typing.Type[VisibilityTrigger]
    handlers: org.orekit.propagation.events.handlers.__module_protocol__
    intervals: org.orekit.propagation.events.intervals.__module_protocol__
