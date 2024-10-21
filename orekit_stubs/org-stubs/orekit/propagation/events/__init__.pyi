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
import org.orekit.propagation.events.class-use
import org.orekit.propagation.events.handlers
import org.orekit.propagation.events.intervals
import org.orekit.propagation.sampling
import org.orekit.time
import org.orekit.utils
import typing



class AdaptableInterval:
    """
    :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.FunctionalInterface?is` public interface AdaptableInterval
    
        This interface represents an event checking interval that depends on state.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.propagation.events.EventDetector`
    """
    def currentInterval(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the current value of maximal time interval between events handler checks.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                current value of maximal time interval between events handler checks
        
        
        """
        ...
    @staticmethod
    def of(double: float) -> 'AdaptableInterval':
        """
            Method creating a constant interval provider.
        
            Parameters:
                constantInterval (double): value of constant interval
        
            Returns:
                adaptable interval ready to be added to an event detector
        
            Since:
                12.1
        
        
        """
        ...

class EnablingPredicate:
    """
    public interface EnablingPredicate
    
        This interface represents an event enabling predicate function.
    
        Since:
            7.1
    """
    def eventIsEnabled(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: 'EventDetector', double: float) -> bool:
        """
            Compute an event enabling function of state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                detector (:class:`~org.orekit.propagation.events.EventDetector`): underlying detector
                g (double): value of the underlying detector for the current state
        
            Returns:
                true if the event is enabled (i.e. it can be triggered), false if it should be ignored
        
        
        """
        ...

class EventDetectionSettings:
    """
    public class EventDetectionSettings extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class containing parameters for event detection.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.propagation.events.EventDetector`
    """
    DEFAULT_MAXCHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAXCHECK
    
        Default maximum checking interval (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default convergence threshold (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITER
    
        Default maximum number of iterations in the event time search.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable], double: float, int: int): ...
    @staticmethod
    def getDefaultEventDetectionSettings() -> 'EventDetectionSettings':
        """
            Returns default settings for event detections.
        
            Returns:
                default settings
        
        
        """
        ...
    def getMaxCheckInterval(self) -> AdaptableInterval:
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

class EventDetector:
    """
    public interface EventDetector
    
        This interface represents space-dynamics aware events detectors.
    
        It mirrors the
        :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.ODEEventHandler?is`
        interface from :class:`~org.orekit.propagation.events.https:.hipparchus.org` but provides a space-dynamics interface to
        the methods.
    
        Events detectors are a useful solution to meet the requirements of propagators concerning discrete conditions. The state
        of each event detector is queried by the propagator from time to time, at least once every
        :meth:`~org.orekit.propagation.events.EventDetector.getMaxCheckInterval` but it may be more frequent. When the sign of
        the underlying g switching function changes, a root-finding algorithm is run to precisely locate the event, down to a
        configured :meth:`~org.orekit.propagation.events.EventDetector.getThreshold`. The
        :meth:`~org.orekit.propagation.events.EventDetector.getMaxCheckInterval` is therefore devoted to separate roots and is
        often much larger than the :meth:`~org.orekit.propagation.events.EventDetector.getThreshold`.
    
        The physical meaning of the g switching function is not really used by the event detection algorithms. Its varies from
        event detector to event detector. One example would be a visibility detector that could use the angular elevation of the
        satellite above horizon as a g switching function. In this case, the function would switch from negative to positive
        when the satellite raises above horizon and it would switch from positive to negative when it sets backs below horizon.
        Another example would be an apside detector that could use the dot product of position and velocity. In this case, the
        function would switch from negative to positive when the satellite crosses periapsis and it would switch from positive
        to negative when the satellite crosses apoapsis.
    
        When the precise state at which the g switching function changes has been located, the corresponding event is triggered,
        by calling the :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` method from the associated
        :meth:`~org.orekit.propagation.events.EventDetector.getHandler`. The method can do whatever it needs with the event
        (logging it, performing some processing, ignore it ...). The return value of the method will be used by the propagator
        to stop or resume propagation, possibly changing the state vector.
    """
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            This method finalizes the event detector's job.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
            Since:
                12.2
        
        
        """
        ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def getMaxCheckInterval(self) -> AdaptableInterval:
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
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class EventDetectorsProvider:
    """
    public interface EventDetectorsProvider
    
        Interface for building event detectors for force models and maneuver parameters.
    
        Objects implementing this interface are mainly :class:`~org.orekit.forces.ForceModel` and
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`.
    
        Since:
            12.0
    """
    DATATION_ACCURACY: typing.ClassVar[float] = ...
    """
    static final double DATATION_ACCURACY
    
        Accuracy of switching events dates (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[EventDetector]: ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T]) -> java.util.stream.Stream['FieldEventDetector'[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream['FieldEventDetector'[_getFieldEventDetectors_1__T]]: ...

_EventState__T = typing.TypeVar('_EventState__T', bound=EventDetector)  # <T>
class EventState(typing.Generic[_EventState__T]):
    """
    public class EventState<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class handles the state for one :class:`~org.orekit.propagation.events.EventDetector` during integration steps.
    
        This class is heavily based on the class with the same name from the Hipparchus library. The changes performed consist
        in replacing raw types (double and double arrays) with space dynamics types (:class:`~org.orekit.time.AbsoluteDate`,
        :class:`~org.orekit.propagation.SpacecraftState`).
    
        Each time the propagator proposes a step, the event detector should be checked. This class handles the state of one
        detector during one propagation step, with references to the state at the end of the preceding step. This information is
        used to determine if the detector should trigger an event or not during the proposed step (and hence the step should be
        reduced to ensure the event occurs at a bound rather than inside the step).
    """
    def __init__(self, t: _EventState__T): ...
    def doEvent(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> 'EventState.EventOccurrence':
        """
            Notify the user's listener of the event. The event occurs wholly within this method call including a call to
            :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` if necessary.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): the state at the time of the event. This must be at the same time as the current value of
                    :meth:`~org.orekit.propagation.events.EventState.getEventDate`.
        
            Returns:
                the user's requested action and the new state if the action is
                :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`.
                Otherwise the new state is :code:`state`. The stop time indicates what time propagation should stop if the action is
                :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`. This
                guarantees the integration will stop on or after the root, so that integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, orekitStepInterpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> bool: ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            This method finalizes the event detector's job.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
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
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def reinitializeBegin(self, orekitStepInterpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> None:
        """
            Reinitialize the beginning of the step.
        
            Parameters:
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): interpolator valid for the current step
        
        
        """
        ...
    def tryAdvance(self, spacecraftState: org.orekit.propagation.SpacecraftState, orekitStepInterpolator: org.orekit.propagation.sampling.OrekitStepInterpolator) -> bool:
        """
            Try to accept the current history up to the given time.
        
            It is not necessary to call this method before calling :meth:`~org.orekit.propagation.events.EventState.doEvent` with
            the same state. It is necessary to call this method before you call
            :meth:`~org.orekit.propagation.events.EventState.doEvent` on some other event detector.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): to try to accept.
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): to use to find the new root, if any.
        
            Returns:
                if the event detector has an event it has not detected before that is on or before the same time as :code:`state`. In
                other words :code:`false` means continue on while :code:`true` means stop and handle my event first.
        
        
        """
        ...
    class EventOccurrence:
        def getAction(self) -> org.hipparchus.ode.events.Action: ...
        def getNewState(self) -> org.orekit.propagation.SpacecraftState: ...
        def getStopDate(self) -> org.orekit.time.AbsoluteDate: ...

class EventsLogger:
    """
    public class EventsLogger extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class logs events detectors events during propagation.
    
        As :class:`~org.orekit.propagation.events.EventDetector` are triggered during orbit propagation, an event specific
        :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` method is called. This class can be used to
        add a global logging feature registering all events with their corresponding states in a chronological sequence (or
        reverse-chronological if propagation occurs backward).
    
        This class works by wrapping user-provided :class:`~org.orekit.propagation.events.EventDetector` before they are
        registered to the propagator. The wrapper monitor the calls to
        :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` and store the corresponding events as
        :class:`~org.orekit.propagation.events.EventsLogger.LoggedEvent` instances. After propagation is complete, the user can
        retrieve all the events that have occurred at once by calling method
        :meth:`~org.orekit.propagation.events.EventsLogger.getLoggedEvents`.
    """
    def __init__(self): ...
    def clearLoggedEvents(self) -> None:
        """
            Clear the logged events.
        
        """
        ...
    def getLoggedEvents(self) -> java.util.List['EventsLogger.LoggedEvent']: ...
    _monitorDetector__T = typing.TypeVar('_monitorDetector__T', bound=EventDetector)  # <T>
    def monitorDetector(self, t: _monitorDetector__T) -> EventDetector:
        """
            Monitor an event detector.
        
            In order to monitor an event detector, it must be wrapped thanks to this method as follows:
        
            .. code-block: java
            
             Propagator propagator = new XyzPropagator(...);
             EventsLogger logger = new EventsLogger();
             EventDetector detector = new UvwDetector(...);
             propagator.addEventDetector(logger.monitorDetector(detector));
             
        
            Note that the event detector returned by the
            :meth:`~org.orekit.propagation.events.EventsLogger.LoggedEvent.getEventDetector` method in
            :class:`~org.orekit.propagation.events.EventsLogger.LoggedEvent` instances returned by
            :meth:`~org.orekit.propagation.events.EventsLogger.getLoggedEvents` are the :code:`monitoredDetector` instances
            themselves, not the wrapping detector returned by this method.
        
            Parameters:
                monitoredDetector (T): event detector to monitor
        
            Returns:
                the wrapping detector to add to the propagator
        
        
        """
        ...
    class LoggedEvent(org.orekit.time.TimeStamped):
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getEventDetector(self) -> EventDetector: ...
        def getState(self) -> org.orekit.propagation.SpacecraftState: ...
        def isIncreasing(self) -> bool: ...

_FieldAdaptableInterval__T = typing.TypeVar('_FieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdaptableInterval(typing.Generic[_FieldAdaptableInterval__T]):
    """
    :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.FunctionalInterface?is` public interface FieldAdaptableInterval<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        This interface represents an event checking interval that depends on state.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.propagation.events.FieldEventDetector`
    """
    def currentInterval(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAdaptableInterval__T]) -> float: ...
    _of__T = typing.TypeVar('_of__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def of(double: float) -> 'FieldAdaptableInterval'[_of__T]:
        """
            Method creating a constant interval provider.
        
            Parameters:
                constantInterval (double): value of constant interval
        
            Returns:
                adaptable interval ready to be added to an event detector
        
            Since:
                12.1
        
        
        """
        ...

_FieldEnablingPredicate__T = typing.TypeVar('_FieldEnablingPredicate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEnablingPredicate(typing.Generic[_FieldEnablingPredicate__T]):
    """
    public interface FieldEnablingPredicate<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        This interface represents an event enabling predicate function.
    
        Since:
            12.0
    """
    def eventIsEnabled(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEnablingPredicate__T], fieldEventDetector: 'FieldEventDetector'[_FieldEnablingPredicate__T], t: _FieldEnablingPredicate__T) -> bool: ...

_FieldEventDetectionSettings__T = typing.TypeVar('_FieldEventDetectionSettings__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventDetectionSettings(typing.Generic[_FieldEventDetectionSettings__T]):
    """
    public class FieldEventDetectionSettings<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class containing parameters for event detection.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.propagation.events.EventDetectionSettings`,
            :class:`~org.orekit.propagation.events.FieldEventDetector`
    """
    DEFAULT_MAXCHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAXCHECK
    
        Default maximum checking interval (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default convergence threshold (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITER
    
        Default maximum number of iterations in the event time search.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, t: _FieldEventDetectionSettings__T, int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEventDetectionSettings__T], eventDetectionSettings: EventDetectionSettings): ...
    @typing.overload
    def __init__(self, fieldAdaptableInterval: typing.Union[FieldAdaptableInterval[_FieldEventDetectionSettings__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], float]], t: _FieldEventDetectionSettings__T, int: int): ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_FieldEventDetectionSettings__T]: ...
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

_FieldEventDetector__T = typing.TypeVar('_FieldEventDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventDetector(typing.Generic[_FieldEventDetector__T]):
    """
    public interface FieldEventDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        This interface represents space-dynamics aware events detectors.
    
        It mirrors the
        :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.FieldODEEventHandler?is`
        interface from :class:`~org.orekit.propagation.events.https:.hipparchus.org` but provides a space-dynamics interface to
        the methods.
    
        Events detectors are a useful solution to meet the requirements of propagators concerning discrete conditions. The state
        of each event detector is queried by the propagator from time to time, at least once every
        :meth:`~org.orekit.propagation.events.FieldEventDetector.getMaxCheckInterval` but it may be more frequent. When the sign
        of the underlying g switching function changes, a root-finding algorithm is run to precisely locate the event, down to a
        configured :meth:`~org.orekit.propagation.events.FieldEventDetector.getThreshold`. The
        :meth:`~org.orekit.propagation.events.FieldEventDetector.getMaxCheckInterval` is therefore devoted to separate roots and
        is often much larger than the :meth:`~org.orekit.propagation.events.FieldEventDetector.getThreshold`.
    
        The physical meaning of the g switching function is not really used by the event detection algorithms. Its varies from
        event detector to event detector. One example would be a visibility detector that could use the angular elevation of the
        satellite above horizon as a g switching function. In this case, the function would switch from negative to positive
        when the satellite raises above horizon and it would switch from positive to negative when it sets backs below horizon.
        Another example would be an apside detector that could use the dot product of position and velocity. In this case, the
        function would switch from negative to positive when the satellite crosses periapsis and it would switch from positive
        to negative when the satellite crosses apoapsis.
    
        When the precise state at which the g switching function changes has been located, the corresponding event is triggered,
        by calling the :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.eventOccurred` method from the
        associated :meth:`~org.orekit.propagation.events.FieldEventDetector.getHandler`. The method can do whatever it needs
        with the event (logging it, performing some processing, ignore it ...). The return value of the method will be used by
        the propagator to stop or resume propagation, possibly changing the state vector.
    """
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventDetector__T]) -> None: ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventDetector__T]) -> _FieldEventDetector__T: ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldEventDetector__T]: ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldEventDetector__T]: ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_FieldEventDetector__T]: ...
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
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventDetector__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEventDetector__T]) -> None: ...

_FieldEventState__EventOccurrence__T = typing.TypeVar('_FieldEventState__EventOccurrence__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldEventState__D = typing.TypeVar('_FieldEventState__D', bound=FieldEventDetector)  # <D>
_FieldEventState__T = typing.TypeVar('_FieldEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventState(typing.Generic[_FieldEventState__D, _FieldEventState__T]):
    """
    public class FieldEventState<D extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>, T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class handles the state for one :class:`~org.orekit.propagation.events.FieldEventDetector` during integration
        steps.
    
        This class is heavily based on the class with the same name from the Hipparchus library. The changes performed consist
        in replacing raw types (double and double arrays) with space dynamics types
        (:class:`~org.orekit.time.FieldAbsoluteDate`, :class:`~org.orekit.propagation.FieldSpacecraftState`).
    
        Each time the propagator proposes a step, the event detector should be checked. This class handles the state of one
        detector during one propagation step, with references to the state at the end of the preceding step. This information is
        used to determine if the detector should trigger an event or not during the proposed step (and hence the step should be
        reduced to ensure the event occurs at a bound rather than inside the step).
    """
    def __init__(self, d: _FieldEventState__D): ...
    def doEvent(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T]) -> 'FieldEventState.EventOccurrence'[_FieldEventState__T]: ...
    def evaluateStep(self, fieldOrekitStepInterpolator: org.orekit.propagation.sampling.FieldOrekitStepInterpolator[_FieldEventState__T]) -> bool: ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T]) -> None: ...
    def getEventDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldEventState__T]: ...
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
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEventState__T]) -> None: ...
    def reinitializeBegin(self, fieldOrekitStepInterpolator: org.orekit.propagation.sampling.FieldOrekitStepInterpolator[_FieldEventState__T]) -> None: ...
    def tryAdvance(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventState__T], fieldOrekitStepInterpolator: org.orekit.propagation.sampling.FieldOrekitStepInterpolator[_FieldEventState__T]) -> bool: ...
    class EventOccurrence(typing.Generic[_FieldEventState__EventOccurrence__T]):
        def getAction(self) -> org.hipparchus.ode.events.Action: ...
        def getNewState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventState__EventOccurrence__T]: ...
        def getStopDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldEventState__EventOccurrence__T]: ...

_FieldEventsLogger__FieldLoggedEvent__T = typing.TypeVar('_FieldEventsLogger__FieldLoggedEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldEventsLogger__T = typing.TypeVar('_FieldEventsLogger__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventsLogger(typing.Generic[_FieldEventsLogger__T]):
    """
    public class FieldEventsLogger<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class logs events detectors events during propagation.
    
        As :class:`~org.orekit.propagation.events.FieldEventDetector` are triggered during orbit propagation, an event specific
        :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.eventOccurred` method is called. This class can be used
        to add a global logging feature registering all events with their corresponding states in a chronological sequence (or
        reverse-chronological if propagation occurs backward).
    
        This class works by wrapping user-provided :class:`~org.orekit.propagation.events.FieldEventDetector` before they are
        registered to the propagator. The wrapper monitor the calls to
        :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.eventOccurred` and store the corresponding events as
        :class:`~org.orekit.propagation.events.FieldEventsLogger.FieldLoggedEvent` instances. After propagation is complete, the
        user can retrieve all the events that have occurred at once by calling method
        :meth:`~org.orekit.propagation.events.FieldEventsLogger.getLoggedEvents`.
    """
    def __init__(self): ...
    def clearLoggedEvents(self) -> None:
        """
            Clear the logged events.
        
        """
        ...
    def getLoggedEvents(self) -> java.util.List['FieldEventsLogger.FieldLoggedEvent'[_FieldEventsLogger__T]]: ...
    def monitorDetector(self, fieldEventDetector: FieldEventDetector[_FieldEventsLogger__T]) -> 'FieldAbstractDetector'['FieldEventsLogger.FieldLoggingWrapper', _FieldEventsLogger__T]: ...
    class FieldLoggedEvent(typing.Generic[_FieldEventsLogger__FieldLoggedEvent__T]):
        def getEventDetector(self) -> FieldEventDetector[_FieldEventsLogger__FieldLoggedEvent__T]: ...
        def getState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventsLogger__FieldLoggedEvent__T]: ...
        def isIncreasing(self) -> bool: ...
    class FieldLoggingWrapper: ...

class FilterType(java.lang.Enum['FilterType']):
    """
    public enum FilterType extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.propagation.events.FilterType`>
    
        Enumerate for :class:`~org.orekit.propagation.events.EventSlopeFilter`.
    
        This class is heavily based on the class with the same name from the Hipparchus library. The changes performed consist
        in package name and error handling.
    
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
    def valueOf(string: str) -> 'FilterType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['FilterType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (FilterType c : FilterType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class VisibilityTrigger(java.lang.Enum['VisibilityTrigger']):
    """
    public enum VisibilityTrigger extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.propagation.events.VisibilityTrigger`>
    
        Enumerate for triggering visibility of spherical bodies.
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.propagation.events.FieldOfViewDetector`
    """
    VISIBLE_ONLY_WHEN_FULLY_IN_FOV: typing.ClassVar['VisibilityTrigger'] = ...
    VISIBLE_AS_SOON_AS_PARTIALLY_IN_FOV: typing.ClassVar['VisibilityTrigger'] = ...
    def radiusCorrection(self, double: float) -> float:
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
    def valueOf(string: str) -> 'VisibilityTrigger':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['VisibilityTrigger']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (VisibilityTrigger c : VisibilityTrigger.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_AbstractDetector__T = typing.TypeVar('_AbstractDetector__T', bound='AbstractDetector')  # <T>
class AbstractDetector(EventDetector, typing.Generic[_AbstractDetector__T]):
    """
    public abstract class AbstractDetector<T extends AbstractDetector<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.EventDetector`
    
        Common parts shared by several orbital events finders.
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    DEFAULT_MAXCHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAXCHECK
    
        Default maximum checking interval (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default convergence threshold (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITER
    
        Default maximum number of iterations in the event time search.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
            Getter for the settings.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getDetectionSettings` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                detection settings
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
            Get the handler.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getHandler` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                event handler to call at event occurrences
        
        
        """
        ...
    def getMaxCheckInterval(self) -> AdaptableInterval:
        """
            Get maximal time interval between switching function checks.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getMaxCheckInterval` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                maximal time interval (s) between switching function checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
            Get maximal number of iterations in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getMaxIterationCount` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
            Get the convergence threshold in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getThreshold` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                convergence threshold (s)
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
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
    def withDetectionSettings(self, eventDetectionSettings: EventDetectionSettings) -> _AbstractDetector__T:
        """
            Set up the event detection settings.
        
            This will override settings previously configured.
        
            Parameters:
                newSettings (:class:`~org.orekit.propagation.events.EventDetectionSettings`): new event detection settings
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                12.2
        
        
        """
        ...
    def withHandler(self, eventHandler: org.orekit.propagation.events.handlers.EventHandler) -> _AbstractDetector__T:
        """
            Set up the event handler to call at event occurrences.
        
            This will override a handler if it has been configured previously.
        
            Parameters:
                newHandler (:class:`~org.orekit.propagation.events.handlers.EventHandler`): event handler to call at event occurrences
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                6.1
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, double: float) -> _AbstractDetector__T:
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
                newMaxCheck (:class:`~org.orekit.propagation.events.AdaptableInterval`): maximum checking interval (s)
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                12.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable]) -> _AbstractDetector__T: ...
    def withMaxIter(self, int: int) -> _AbstractDetector__T:
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
    def withThreshold(self, double: float) -> _AbstractDetector__T:
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

class AdapterDetector(EventDetector):
    """
    public class AdapterDetector extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.EventDetector`
    
        Base class for adapting an existing detector.
    
        This class is intended to be a base class for changing behaviour of a wrapped existing detector. This base class
        delegates all its methods to the wrapped detector. Classes extending it can therefore override only the methods they
        want to change.
    
        Since:
            9.3
    """
    def __init__(self, eventDetector: EventDetector): ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            This method finalizes the event detector's job.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.finish` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
        
        """
        ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.g` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getDetectionSettings(self) -> EventDetectionSettings:
        """
            Getter for the settings.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getDetectionSettings` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
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
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getHandler` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                event handler to call at event occurrences
        
        
        """
        ...
    def getMaxCheckInterval(self) -> AdaptableInterval:
        """
            Get maximal time interval between switching function checks.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getMaxCheckInterval` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                maximal time interval (s) between switching function checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
            Get maximal number of iterations in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getMaxIterationCount` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
            Get the convergence threshold in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getThreshold` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                convergence threshold (s)
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

_FieldAbstractDetector__D = typing.TypeVar('_FieldAbstractDetector__D', bound='FieldAbstractDetector')  # <D>
_FieldAbstractDetector__T = typing.TypeVar('_FieldAbstractDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractDetector(FieldEventDetector[_FieldAbstractDetector__T], typing.Generic[_FieldAbstractDetector__D, _FieldAbstractDetector__T]):
    """
    public abstract class FieldAbstractDetector<D extends FieldAbstractDetector<D, T>, T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.FieldEventDetector`<T>
    
        Common parts shared by several orbital events finders.
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    DEFAULT_MAXCHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAXCHECK
    
        Default maximum checking interval (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default convergence threshold (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITER
    
        Default maximum number of iterations in the event time search.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldAbstractDetector__T]: ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldAbstractDetector__T]: ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_FieldAbstractDetector__T]: ...
    def getMaxIterationCount(self) -> int:
        """
            Get maximal number of iterations in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.FieldEventDetector.getMaxIterationCount` in
                interface :class:`~org.orekit.propagation.events.FieldEventDetector`
        
            Returns:
                maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> _FieldAbstractDetector__T:
        """
            Get the convergence threshold in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.FieldEventDetector.getThreshold` in
                interface :class:`~org.orekit.propagation.events.FieldEventDetector`
        
            Returns:
                convergence threshold (s)
        
        
        """
        ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractDetector__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractDetector__T]) -> None: ...
    def isForward(self) -> bool:
        """
            Check if the current propagation is forward or backward.
        
            Returns:
                true if the current propagation is forward
        
            Since:
                7.2
        
        
        """
        ...
    def withDetectionSettings(self, fieldEventDetectionSettings: FieldEventDetectionSettings[_FieldAbstractDetector__T]) -> _FieldAbstractDetector__D: ...
    def withHandler(self, fieldEventHandler: org.orekit.propagation.events.handlers.FieldEventHandler[_FieldAbstractDetector__T]) -> _FieldAbstractDetector__D: ...
    @typing.overload
    def withMaxCheck(self, double: float) -> _FieldAbstractDetector__D:
        """
            Set up the maximum checking interval.
        
            This will override a maximum checking interval if it has been configured previously.
        
            Parameters:
                newMaxCheck (double): maximum checking interval (s)
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                12.0
        
        public :class:`~org.orekit.propagation.events.FieldAbstractDetector` withMaxCheck (:class:`~org.orekit.propagation.events.FieldAdaptableInterval`<:class:`~org.orekit.propagation.events.FieldAbstractDetector`> newMaxCheck)
        
            Set up the maximum checking interval.
        
            This will override a maximum checking interval if it has been configured previously.
        
            Parameters:
                newMaxCheck (:class:`~org.orekit.propagation.events.FieldAdaptableInterval`<:class:`~org.orekit.propagation.events.FieldAbstractDetector`> newMaxCheck): maximum checking interval (s)
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                12.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, fieldAdaptableInterval: typing.Union[FieldAdaptableInterval[_FieldAbstractDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], float]]) -> _FieldAbstractDetector__D: ...
    def withMaxIter(self, int: int) -> _FieldAbstractDetector__D:
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
    def withThreshold(self, t: _FieldAbstractDetector__T) -> _FieldAbstractDetector__D:
        """
            Set up the convergence threshold.
        
            This will override a convergence threshold if it has been configured previously.
        
            Parameters:
                newThreshold (:class:`~org.orekit.propagation.events.FieldAbstractDetector`): convergence threshold (s)
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                6.1
        
        
        """
        ...

_FieldAdapterDetector__T = typing.TypeVar('_FieldAdapterDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdapterDetector(FieldEventDetector[_FieldAdapterDetector__T], typing.Generic[_FieldAdapterDetector__T]):
    """
    public class FieldAdapterDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.FieldEventDetector`<T>
    
        Base class for adapting an existing detector.
    
        This class is intended to be a base class for changing behaviour of a wrapped existing detector. This base class
        delegates all its methods to the wrapped detector. Classes extending it can therefore override only the methods they
        want to change.
    
        Since:
            12.0
    """
    def __init__(self, fieldEventDetector: FieldEventDetector[_FieldAdapterDetector__T]): ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAdapterDetector__T]) -> None: ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAdapterDetector__T]) -> _FieldAdapterDetector__T: ...
    def getDetectionSettings(self) -> FieldEventDetectionSettings[_FieldAdapterDetector__T]: ...
    def getDetector(self) -> FieldEventDetector[_FieldAdapterDetector__T]: ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldAdapterDetector__T]: ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_FieldAdapterDetector__T]: ...
    def getMaxIterationCount(self) -> int:
        """
            Get maximal number of iterations in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.FieldEventDetector.getMaxIterationCount` in
                interface :class:`~org.orekit.propagation.events.FieldEventDetector`
        
            Returns:
                maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> _FieldAdapterDetector__T:
        """
            Get the convergence threshold in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.FieldEventDetector.getThreshold` in
                interface :class:`~org.orekit.propagation.events.FieldEventDetector`
        
            Returns:
                convergence threshold (s)
        
        
        """
        ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAdapterDetector__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAdapterDetector__T]) -> None: ...

class PythonAdaptableInterval(AdaptableInterval):
    """
    public class PythonAdaptableInterval extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.AdaptableInterval`
    """
    def __init__(self): ...
    def currentInterval(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the current value of maximal time interval between events handler checks.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.AdaptableInterval.currentInterval` in
                interface :class:`~org.orekit.propagation.events.AdaptableInterval`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                current value of maximal time interval between events handler checks
        
        
        """
        ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

class PythonEnablingPredicate(EnablingPredicate):
    """
    public class PythonEnablingPredicate extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.EnablingPredicate`
    """
    def __init__(self): ...
    def eventIsEnabled(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: EventDetector, double: float) -> bool:
        """
            Compute an event enabling function of state.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EnablingPredicate.eventIsEnabled` in
                interface :class:`~org.orekit.propagation.events.EnablingPredicate`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                eventDetector (:class:`~org.orekit.propagation.events.EventDetector`): underlying detector
                g (double): value of the underlying detector for the current state
        
            Returns:
                true if the event is enabled (i.e. it can be triggered), false if it should be ignored
        
        
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

class PythonEventDetector(EventDetector):
    """
    public class PythonEventDetector extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.EventDetector`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            This method finalizes the event detector's job.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.finish` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
        
        """
        ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.g` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
            Get the handler.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getHandler` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                event handler to call at event occurrences
        
        
        """
        ...
    def getMaxCheckInterval(self) -> AdaptableInterval:
        """
            Get maximal time interval between switching function checks.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getMaxCheckInterval` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                maximal time interval (s) between switching function checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
            Get maximal number of iterations in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getMaxIterationCount` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
            Get the convergence threshold in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getThreshold` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                convergence threshold (s)
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

class PythonEventDetectorsProvider(EventDetectorsProvider):
    """
    public class PythonEventDetectorsProvider extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.EventDetectorsProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
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
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

_PythonFieldAdaptableInterval__T = typing.TypeVar('_PythonFieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdaptableInterval(FieldAdaptableInterval[_PythonFieldAdaptableInterval__T], typing.Generic[_PythonFieldAdaptableInterval__T]):
    """
    public class PythonFieldAdaptableInterval<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.FieldAdaptableInterval`<T>
    """
    def __init__(self): ...
    def currentInterval(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdaptableInterval__T]) -> float: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

_PythonFieldEnablingPredicate__T = typing.TypeVar('_PythonFieldEnablingPredicate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEnablingPredicate(FieldEnablingPredicate[_PythonFieldEnablingPredicate__T], typing.Generic[_PythonFieldEnablingPredicate__T]):
    """
    public class PythonFieldEnablingPredicate<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.FieldEnablingPredicate`<T>
    """
    def __init__(self): ...
    def eventIsEnabled(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEnablingPredicate__T], fieldEventDetector: FieldEventDetector[_PythonFieldEnablingPredicate__T], t: _PythonFieldEnablingPredicate__T) -> bool: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

_PythonFieldEventDetector__T = typing.TypeVar('_PythonFieldEventDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEventDetector(FieldEventDetector[_PythonFieldEventDetector__T], typing.Generic[_PythonFieldEventDetector__T]):
    """
    public class PythonFieldEventDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.FieldEventDetector`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventDetector__T]) -> None: ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventDetector__T]) -> _PythonFieldEventDetector__T: ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_PythonFieldEventDetector__T]: ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_PythonFieldEventDetector__T]: ...
    def getMaxIterationCount(self) -> int:
        """
            Get maximal number of iterations in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.FieldEventDetector.getMaxIterationCount` in
                interface :class:`~org.orekit.propagation.events.FieldEventDetector`
        
            Returns:
                maximal number of iterations in the event time search
        
        
        """
        ...
    def getThreshold(self) -> _PythonFieldEventDetector__T:
        """
            Get the convergence threshold in the event time search.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.FieldEventDetector.getThreshold` in
                interface :class:`~org.orekit.propagation.events.FieldEventDetector`
        
            Returns:
                convergence threshold (s)
        
        
        """
        ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventDetector__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldEventDetector__T]) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

class AlignmentDetector(AbstractDetector['AlignmentDetector']):
    """
    public class AlignmentDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.AlignmentDetector`>
    
        Finder for satellite/body alignment events in orbital plane.
    
        This class finds alignment events.
    
        Alignment means the conjunction, with some threshold angle, between the satellite position and the projection in the
        orbital plane of some body position.
    
        The default handler behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when alignment is reached. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double3: float): ...
    @typing.overload
    def __init__(self, double: float, orbit: org.orekit.orbits.Orbit, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function measures the difference between the alignment angle and the
            angle between the satellite position and the body position projection in the orbital plane.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class AltitudeDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.AltitudeDetector`>
    
        Finder for satellite altitude crossing events.
    
        This class finds altitude events (i.e. satellite crossing a predefined altitude level above ground).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when ascending and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when descending. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, double: float, double2: float, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, double: float, bodyShape: org.orekit.bodies.BodyShape): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function measures the difference between the current altitude and the
            threshold altitude.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class AngularSeparationDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.AngularSeparationDetector`>
    
        Detects when spacecraft comes close to a moving beacon, as seen from a moving observer.
    
        The main use case for this detector is when the observer is in fact a ground station, modeled as a
        :class:`~org.orekit.frames.TopocentricFrame` and when the beacon is the
        :meth:`~org.orekit.bodies.CelestialBodies.getSun`, for computing interferences for the telemetry link. Another similar
        case is when the beacon is another spacecraft, for interferences computation.
    
        The default handler behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when spacecraft enters the proximity zone. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Since:
            8.0
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, pVCoordinatesProvider2: org.orekit.utils.PVCoordinatesProvider, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function.
        
            This function measures the angular separation between beacon and spacecraft as seen from the observer minus the
            proximity angle. It therefore triggers decreasing events when the spacecraft enters the proximity zone and increasing
            events when it leaves the proximity zone.
        
            No shadowing effect is taken into account, so this method is computed and may trigger events even when the spacecraft is
            below horizon for an observer which is a ground station. If such effects must be taken into account the detector must be
            associated with a :class:`~org.orekit.propagation.events.EventEnablingPredicateFilter` where the
            :class:`~org.orekit.propagation.events.EnablingPredicate` is based on elevation.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class AngularSeparationFromSatelliteDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.AngularSeparationFromSatelliteDetector`>
    
        Detects when two moving objects come close to each other, as seen from spacecraft.
    
        The main use case for this detector is when the primary object is in fact a ground station, modeled as a
        :class:`~org.orekit.frames.TopocentricFrame` and when the secondary is the
        :meth:`~org.orekit.bodies.CelestialBodies.getSun`, for computing optical reflections.
    
        The default handler behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when objects enter the proximity zone. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Since:
            11.0
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, pVCoordinatesProvider2: org.orekit.utils.PVCoordinatesProvider, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function.
        
            This function measures the angular separation between primary and secondary objects as seen from the spacecraft minus
            the proximity angle. It therefore triggers decreasing events when the secondary object enters the proximity zone and
            increasing events when it leaves the proximity zone.
        
            No shadowing effect is taken into account, so this method is computed and may trigger events even when the secondary
            object is behind the primary. If such effects must be taken into account the detector must be associated with a
            :class:`~org.orekit.propagation.events.EventEnablingPredicateFilter` where the
            :class:`~org.orekit.propagation.events.EnablingPredicate` is based on eclipse conditions.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class ApsideDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.ApsideDetector`>
    
        Finder for apside crossing events.
    
        This class finds apside crossing events (i.e. apogee or perigee crossing).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at apogee crossing and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at perigee crossing. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Beware that apside detection will fail for almost circular orbits. If for example an apside detector is used to trigger
        an :class:`~org.orekit.forces.maneuvers.ImpulseManeuver` and the maneuver change the orbit shape to circular, then the
        detector may completely fail just after the maneuver has been performed!
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable], double: float, int: int, eventHandler: org.orekit.propagation.events.handlers.EventHandler): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function computes the dot product of the 2 vectors :
            position.velocity.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...

class BetaAngleDetector(AbstractDetector['BetaAngleDetector']):
    """
    public class BetaAngleDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.BetaAngleDetector`>
    
        Finder for beta angle crossing events.
    
        Locate events when the beta angle (the angle between the orbit plane and the celestial body) crosses a threshold. The
        :meth:`~org.orekit.propagation.events.BetaAngleDetector.g` function is negative when the beta angle is above the
        threshold and positive when the beta angle is below the threshold.
    
        The inertial frame provided must have it's origin centered at the satellite's orbit plane. The beta angle is computed as
        the angle between the celestial body's position in this frame with the satellite's orbital momentum vector.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at the first event date occurrence. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Since:
            12.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, frame: org.orekit.frames.Frame): ...
    @typing.overload
    @staticmethod
    def calculateBetaAngle(spacecraftState: org.orekit.propagation.SpacecraftState, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider) -> float:
        """
            Calculate the beta angle between the orbit plane and the celestial body.
        
            This method computes the beta angle using the frame from the spacecraft state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                celestialBodyProvider (:class:`~org.orekit.utils.PVCoordinatesProvider`): celestial body coordinate provider
        
            Returns:
                the beta angle (radians)
        
            Calculate the beta angle between the orbit plane and the celestial body.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                celestialBodyProvider (:class:`~org.orekit.utils.PVCoordinatesProvider`): celestial body coordinate provider
                frame (:class:`~org.orekit.frames.Frame`): inertial frame in which beta angle will be computed
        
            Returns:
                the beta angle (radians)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def calculateBetaAngle(spacecraftState: org.orekit.propagation.SpacecraftState, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, frame: org.orekit.frames.Frame) -> float: ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def withBetaThreshold(self, double: float) -> 'BetaAngleDetector':
        """
            Create a new instance with the provided beta angle threshold.
        
            This method does not change the current instance.
        
            Parameters:
                newBetaAngleThreshold (double): the beta angle threshold (radians)
        
            Returns:
                the new detector instance
        
        
        """
        ...
    def withCelestialProvider(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider) -> 'BetaAngleDetector':
        """
            Create a new instance with the provided coordinate provider.
        
            This method does not change the current instance.
        
            Parameters:
                newProvider (:class:`~org.orekit.utils.PVCoordinatesProvider`): the new coordinate provider
        
            Returns:
                the new detector instance
        
        
        """
        ...
    def withInertialFrame(self, frame: org.orekit.frames.Frame) -> 'BetaAngleDetector':
        """
            Create a new instance with the provided inertial frame.
        
            This method does not change the current instance.
        
            Parameters:
                newFrame (:class:`~org.orekit.frames.Frame`): the inertial frame
        
            Returns:
                the new detector instance
        
        
        """
        ...

class BooleanDetector(AbstractDetector['BooleanDetector']):
    """
    public class BooleanDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.BooleanDetector`>
    
        This class provides AND and OR operations for event detectors. This class treats positive values of the g function as
        true and negative values as false.
    
        One example for an imaging satellite might be to only detect events when a satellite is overhead (elevation > 0) AND
        when the ground point is sunlit (Sun elevation > 0). Another slightly contrived example using the OR operator would be
        to detect access to a set of ground stations and only report events when the satellite enters or leaves the field of
        view of the set, but not hand-offs between the ground stations.
    
        For the BooleanDetector is important that the sign of the g function of the underlying event detector is not arbitrary,
        but has a semantic meaning, e.g. in or out, true or false. This class works well with event detectors that detect entry
        to or exit from a region, e.g. :class:`~org.orekit.propagation.events.EclipseDetector`,
        :class:`~org.orekit.propagation.events.ElevationDetector`,
        :class:`~org.orekit.propagation.events.LatitudeCrossingDetector`. Using this detector with detectors that are not based
        on entry to or exit from a region, e.g. :class:`~org.orekit.propagation.events.DateDetector`,
        :class:`~org.orekit.propagation.events.LongitudeCrossingDetector`, will likely lead to unexpected results. To apply
        conditions to this latter type of event detectors a :class:`~org.orekit.propagation.events.EventEnablingPredicateFilter`
        is usually more appropriate.
    
        Also see:
            :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine`,
            :meth:`~org.orekit.propagation.events.BooleanDetector.orCombine`,
            :meth:`~org.orekit.propagation.events.BooleanDetector.notCombine`,
            :class:`~org.orekit.propagation.events.EventEnablingPredicateFilter`,
            :class:`~org.orekit.propagation.events.EventSlopeFilter`
    """
    @typing.overload
    @staticmethod
    def andCombine(collection: typing.Union[java.util.Collection[EventDetector], typing.Sequence[EventDetector]]) -> 'BooleanDetector':
        """
            Create a new event detector that is the logical AND of the given event detectors.
        
            The created event detector's g function is positive if and only if the g functions of all detectors in :code:`detectors`
            are positive.
        
            The starting interval, threshold, and iteration count are set to the most stringent (minimum) of all the
            :code:`detectors`. The event handlers of the underlying :code:`detectors` are not used, instead the default handler is
            :class:`~org.orekit.propagation.events.handlers.ContinueOnEvent`.
        
            Parameters:
                detectors (:class:`~org.orekit.propagation.events.EventDetector`...): the operands. Must contain at least one detector.
        
            Returns:
                a new event detector that is the logical AND of the operands.
        
            Raises:
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.NoSuchElementException?is`: if :code:`detectors` is empty.
        
            Also see:
                :class:`~org.orekit.propagation.events.BooleanDetector`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.orCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.notCombine`
        
        public static :class:`~org.orekit.propagation.events.BooleanDetector` andCombine (:class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.Collection?is`<? extends :class:`~org.orekit.propagation.events.EventDetector`> detectors)
        
            Create a new event detector that is the logical AND of the given event detectors.
        
            The created event detector's g function is positive if and only if the g functions of all detectors in :code:`detectors`
            are positive.
        
            The starting interval, threshold, and iteration count are set to the most stringent (minimum) of the :code:`detectors`.
            The event handlers of the underlying :code:`detectors` are not used, instead the default handler is
            :class:`~org.orekit.propagation.events.handlers.ContinueOnEvent`.
        
            Parameters:
                detectors (:class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.Collection?is`<? extends :class:`~org.orekit.propagation.events.EventDetector`> detectors): the operands. Must contain at least one detector.
        
            Returns:
                a new event detector that is the logical AND of the operands.
        
            Raises:
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.NoSuchElementException?is`: if :code:`detectors` is empty.
        
            Also see:
                :class:`~org.orekit.propagation.events.BooleanDetector`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.orCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.notCombine`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def andCombine(eventDetectorArray: typing.List[EventDetector]) -> 'BooleanDetector': ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.EventDetector.g`
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getDetectors(self) -> java.util.List[EventDetector]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Description copied from class: :meth:`~org.orekit.propagation.events.AbstractDetector.init`
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    @staticmethod
    def notCombine(eventDetector: EventDetector) -> 'NegateDetector':
        """
            Create a new event detector that negates the g function of another detector.
        
            This detector will be initialized with the same
            :meth:`~org.orekit.propagation.events.EventDetector.getMaxCheckInterval`,
            :meth:`~org.orekit.propagation.events.EventDetector.getThreshold`, and
            :meth:`~org.orekit.propagation.events.EventDetector.getMaxIterationCount` as :code:`detector`. The event handler of the
            underlying detector is not used, instead the default handler is
            :class:`~org.orekit.propagation.events.handlers.ContinueOnEvent`.
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.EventDetector`): to negate.
        
            Returns:
                an new event detector whose g function is the same magnitude but opposite sign of :code:`detector`.
        
            Also see:
                :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.orCombine`,
                :class:`~org.orekit.propagation.events.BooleanDetector`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def orCombine(collection: typing.Union[java.util.Collection[EventDetector], typing.Sequence[EventDetector]]) -> 'BooleanDetector':
        """
            Create a new event detector that is the logical OR of the given event detectors.
        
            The created event detector's g function is positive if and only if at least one of g functions of the event detectors in
            :code:`detectors` is positive.
        
            The starting interval, threshold, and iteration count are set to the most stringent (minimum) of the :code:`detectors`.
            The event handlers of the underlying EventDetectors are not used, instead the default handler is
            :class:`~org.orekit.propagation.events.handlers.ContinueOnEvent`.
        
            Parameters:
                detectors (:class:`~org.orekit.propagation.events.EventDetector`...): the operands. Must contain at least one detector.
        
            Returns:
                a new event detector that is the logical OR of the operands.
        
            Raises:
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.NoSuchElementException?is`: if :code:`detectors` is empty.
        
            Also see:
                :class:`~org.orekit.propagation.events.BooleanDetector`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.orCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.notCombine`
        
        public static :class:`~org.orekit.propagation.events.BooleanDetector` orCombine (:class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.Collection?is`<? extends :class:`~org.orekit.propagation.events.EventDetector`> detectors)
        
            Create a new event detector that is the logical OR of the given event detectors.
        
            The created event detector's g function is positive if and only if at least one of g functions of the event detectors in
            :code:`detectors` is positive.
        
            The starting interval, threshold, and iteration count are set to the most stringent (minimum) of the :code:`detectors`.
            The event handlers of the underlying EventDetectors are not used, instead the default handler is
            :class:`~org.orekit.propagation.events.handlers.ContinueOnEvent`.
        
            Parameters:
                detectors (:class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.Collection?is`<? extends :class:`~org.orekit.propagation.events.EventDetector`> detectors): the operands. Must contain at least one detector.
        
            Returns:
                a new event detector that is the logical OR of the operands.
        
            Raises:
                :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.util.NoSuchElementException?is`: if :code:`detectors` is empty.
        
            Also see:
                :class:`~org.orekit.propagation.events.BooleanDetector`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.orCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine`,
                :meth:`~org.orekit.propagation.events.BooleanDetector.notCombine`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def orCombine(eventDetectorArray: typing.List[EventDetector]) -> 'BooleanDetector': ...

class CylindricalShadowEclipseDetector(AbstractDetector['CylindricalShadowEclipseDetector']):
    """
    public class CylindricalShadowEclipseDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.CylindricalShadowEclipseDetector`>
    
        Event detector for eclipses from a single, infinitely-distant light source, occulted by a spherical central body. The
        shadow region is cylindrical, a model less accurate than a conical one but more computationally-performant.
    
        The so-called g function is negative in eclipse, positive otherwise.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.events.EclipseDetector`
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable], double2: float, int: int, eventHandler: org.orekit.propagation.events.handlers.EventHandler): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, eventDetectionSettings: EventDetectionSettings, eventHandler: org.orekit.propagation.events.handlers.EventHandler): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, eventHandler: org.orekit.propagation.events.handlers.EventHandler): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class DateDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.DateDetector`> implements :class:`~org.orekit.time.TimeStamped`
    
        Finder for date events.
    
        This class finds date events (i.e. occurrence of some predefined dates).
    
        As of version 5.1, it is an enhanced date detector:
    
          - it can be defined without prior date (:meth:`~org.orekit.propagation.events.DateDetector.%3Cinit%3E`)
          - several dates can be added (:meth:`~org.orekit.propagation.events.DateDetector.addEventDate`)
    
    
        The gap between the added dates must be more than the minGap.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at the first event date occurrence. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAX_CHECK
    
        Default value for max check.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MIN_GAP: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MIN_GAP
    
        Default value for minimum gap between added dates.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default value for convergence threshold.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, timeStampedArray: typing.List[org.orekit.time.TimeStamped]): ...
    def addEventDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function measures the difference between the current and the target
            date.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.g` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the current event date according to the propagator.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                event date
        
        
        """
        ...
    def getDates(self) -> java.util.List[org.orekit.time.TimeStamped]: ...
    def withMinGap(self, double: float) -> 'DateDetector':
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
    public class EclipseDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.EclipseDetector`>
    
        Finder for satellite eclipse related events.
    
        This class finds eclipse events, i.e. satellite within umbra (total eclipse) or penumbra (partial eclipse).
    
        The occulted body is given through a :class:`~org.orekit.utils.PVCoordinatesProvider` and its radius in meters. It is
        modeled as a sphere.
    
        Since v10.0 the occulting body is a :class:`~org.orekit.bodies.OneAxisEllipsoid`, before it was modeled as a sphere.
    
    
        It was changed to precisely model Solar eclipses by the Earth, especially for Low Earth Orbits.
    
    
        If you want eclipses by a spherical occulting body, set its flattening to 0. when defining its OneAxisEllipsoid model..
    
        The :meth:`~org.orekit.propagation.events.EclipseDetector.withUmbra` or
        :meth:`~org.orekit.propagation.events.EclipseDetector.withPenumbra` methods will tell you if the event is triggered when
        complete umbra/lighting is achieved or when entering/living the penumbra zone.
    
    
        The default behavior is detecting complete umbra/lighting events.
    
    
        If you want to have both, you'll need to set up two distinct detectors.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when entering the eclipse and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when exiting the eclipse.
    
    
        This can be changed by calling :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, occultationEngine: org.orekit.utils.OccultationEngine): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function becomes negative when entering the region of shadow and
            positive when exiting.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def withMargin(self, double: float) -> 'EclipseDetector':
        """
            Setup a margin to angle detection.
        
            A positive margin implies eclipses are "larger" hence entry occurs earlier and exit occurs later than a detector with 0
            margin.
        
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
                :meth:`~org.orekit.propagation.events.EclipseDetector.withUmbra`
        
        
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
                :meth:`~org.orekit.propagation.events.EclipseDetector.withPenumbra`
        
        
        """
        ...

class ElevationDetector(AbstractDetector['ElevationDetector']):
    """
    public class ElevationDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.ElevationDetector`>
    
        Finder for satellite raising/setting events that allows for the setting of azimuth and/or elevation bounds or a ground
        azimuth/elevation mask input. Each calculation be configured to use atmospheric refraction as well.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at raising and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at setting. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Since:
            6.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable], double: float, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function measures the difference between the current elevation (and
            azimuth if necessary) and the reference mask or minimum value.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getElevationMask(self) -> org.orekit.utils.ElevationMask:
        """
            Returns the currently configured elevation mask.
        
            Returns:
                elevation mask (null if instance has been configured with
                :meth:`~org.orekit.propagation.events.ElevationDetector.withConstantElevation`
        
            Also see:
                :meth:`~org.orekit.propagation.events.ElevationDetector.withElevationMask`
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
            Returns the currently configured minimum valid elevation value.
        
            Returns:
                minimum elevation value (:code:`Double.NaN` if instance has been configured with
                :meth:`~org.orekit.propagation.events.ElevationDetector.withElevationMask`
        
            Also see:
                :meth:`~org.orekit.propagation.events.ElevationDetector.withConstantElevation`
        
        
        """
        ...
    def getRefractionModel(self) -> org.orekit.models.AtmosphericRefractionModel:
        """
            Returns the currently configured refraction model.
        
            Returns:
                refraction model
        
            Also see:
                :meth:`~org.orekit.propagation.events.ElevationDetector.withRefraction`
        
        
        """
        ...
    def getTopocentricFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
            Returns the currently configured topocentric frame definitions.
        
            Returns:
                topocentric frame definition
        
        
        """
        ...
    def withConstantElevation(self, double: float) -> 'ElevationDetector':
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
                :meth:`~org.orekit.propagation.events.ElevationDetector.getMinElevation`
        
        
        """
        ...
    def withElevationMask(self, elevationMask: org.orekit.utils.ElevationMask) -> 'ElevationDetector':
        """
            Setup the elevation mask for detection using the passed in mask object.
        
            Parameters:
                newElevationMask (:class:`~org.orekit.utils.ElevationMask`): elevation mask to use for the computation
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.propagation.events.ElevationDetector.getElevationMask`
        
        
        """
        ...
    def withRefraction(self, atmosphericRefractionModel: org.orekit.models.AtmosphericRefractionModel) -> 'ElevationDetector':
        """
            Setup the elevation detector to use an atmospheric refraction model in its calculations.
        
            To disable the refraction when copying an existing elevation detector, call this method with a null argument.
        
            Parameters:
                newRefractionModel (:class:`~org.orekit.models.AtmosphericRefractionModel`): refraction model to use for the computation
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.propagation.events.ElevationDetector.getRefractionModel`
        
        
        """
        ...

class ElevationExtremumDetector(AbstractDetector['ElevationExtremumDetector']):
    """
    public class ElevationExtremumDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.ElevationExtremumDetector`>
    
        Detector for elevation extremum with respect to a ground point.
    
        This detector identifies when a spacecraft reaches its extremum elevation with respect to a ground point.
    
        As in most cases only the elevation maximum is needed and the minimum is often irrelevant, this detector is often
        wrapped into an :class:`~org.orekit.propagation.events.EventSlopeFilter` configured with
        :meth:`~org.orekit.propagation.events.FilterType.TRIGGER_ONLY_DECREASING_EVENTS` (i.e. when the elevation derivative
        decreases from positive values to negative values, which correspond to a maximum). Setting up this filter saves some
        computation time as the elevation minimum occurrences are not even looked at. It is however still often necessary to do
        an additional filtering
    
        Since:
            7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is the spacecraft elevation first time derivative.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                spacecraft elevation first time derivative
        
        
        """
        ...
    def getElevation(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the elevation value.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                spacecraft elevation
        
        
        """
        ...
    def getTopocentricFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
            Returns the topocentric frame centered on ground point.
        
            Returns:
                topocentric frame centered on ground point
        
        
        """
        ...

class EventEnablingPredicateFilter(AbstractDetector['EventEnablingPredicateFilter']):
    """
    public class EventEnablingPredicateFilter extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.EventEnablingPredicateFilter`>
    
        Wrapper used to detect events only when enabled by an external predicated function.
    
        General :class:`~org.orekit.propagation.events.EventDetector` are defined implicitly by a
        :meth:`~org.orekit.propagation.events.EventDetector.g` crossing zero. This implies that during an orbit propagation,
        events are triggered at all zero crossings.
    
        Sometimes, users would like to enable or disable events by themselves, for example to trigger them only for certain
        orbits, or to check elevation maximums only when elevation itself is positive (i.e. they want to discard elevation
        maximums below ground). In these cases, looking precisely for all events location and triggering events that will later
        be ignored is a waste of computing time.
    
        Users can wrap a regular :class:`~org.orekit.propagation.events.EventDetector` in an instance of this class and provide
        this wrapping instance to a :class:`~org.orekit.propagation.Propagator` in order to avoid wasting time looking for
        uninteresting events. The wrapper will intercept the calls to the :meth:`~org.orekit.propagation.events.EventDetector.g`
        and to the :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` method in order to ignore
        uninteresting events. The wrapped regular :class:`~org.orekit.propagation.events.EventDetector` will the see only the
        interesting events, i.e. either only events that occur when a user-provided event enabling predicate function is true,
        ignoring all events that occur when the event enabling predicate function is false. The number of calls to the
        :meth:`~org.orekit.propagation.events.EventDetector.g` will also be reduced.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.propagation.events.EventSlopeFilter`
    """
    def __init__(self, eventDetector: EventDetector, enablingPredicate: EnablingPredicate): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getDetector(self) -> EventDetector:
        """
            Get the wrapped raw detector.
        
            Returns:
                the wrapped raw detector
        
            Since:
                11.1
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class EventShifter(AbstractDetector['EventShifter']):
    """
    public class EventShifter extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.EventShifter`>
    
        Wrapper shifting events occurrences times.
    
        This class wraps an :class:`~org.orekit.propagation.events.EventDetector` to slightly shift the events occurrences
        times. A typical use case is for handling operational delays before or after some physical event really occurs.
    
        For example, the satellite attitude mode may be switched from sun pointed to spin-stabilized a few minutes before
        eclipse entry, and switched back to sun pointed a few minutes after eclipse exit. This behavior is handled by wrapping
        an :class:`~org.orekit.propagation.events.EclipseDetector` into an instance of this class with a positive times shift
        for increasing events (eclipse exit) and a negative times shift for decreasing events (eclipse entry).
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`, :class:`~org.orekit.propagation.events.EventDetector`
    """
    def __init__(self, eventDetector: EventDetector, boolean: bool, double: float, double2: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def getDetector(self) -> EventDetector:
        """
            Get the detector for the raw unshifted event.
        
            Returns:
                the detector for the raw unshifted event
        
            Since:
                11.1
        
        
        """
        ...
    def getIncreasingTimeShift(self) -> float:
        """
            Get the increasing events time shift.
        
            Returns:
                increasing events time shift
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

_EventSlopeFilter__T = typing.TypeVar('_EventSlopeFilter__T', bound=EventDetector)  # <T>
class EventSlopeFilter(AbstractDetector['EventSlopeFilter'[_EventSlopeFilter__T]], typing.Generic[_EventSlopeFilter__T]):
    """
    public class EventSlopeFilter<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.EventSlopeFilter`<T>>
    
        Wrapper used to detect only increasing or decreasing events.
    
        This class is heavily based on the class EventFilter from the Hipparchus library. The changes performed consist in
        replacing raw types (double and double arrays) with space dynamics types (:class:`~org.orekit.time.AbsoluteDate`,
        :class:`~org.orekit.propagation.SpacecraftState`).
    
        General :class:`~org.orekit.propagation.events.EventDetector` are defined implicitly by a
        :meth:`~org.orekit.propagation.events.EventDetector.g` crossing zero. This function needs to be continuous in the event
        neighborhood, and its sign must remain consistent between events. This implies that during an orbit propagation, events
        triggered are alternately events for which the function increases from negative to positive values, and events for which
        the function decreases from positive to negative values.
    
        Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type.
        In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of
        computing time.
    
        Users can wrap a regular :class:`~org.orekit.propagation.events.EventDetector` in an instance of this class and provide
        this wrapping instance to a :class:`~org.orekit.propagation.Propagator` in order to avoid wasting time looking for
        uninteresting events. The wrapper will intercept the calls to the :meth:`~org.orekit.propagation.events.EventDetector.g`
        and to the :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` method in order to ignore
        uninteresting events. The wrapped regular :class:`~org.orekit.propagation.events.EventDetector` will then see only the
        interesting events, i.e. either only :code:`increasing` events or only :code:`decreasing` events. The number of calls to
        the :meth:`~org.orekit.propagation.events.EventDetector.g` will also be reduced.
    
        Also see:
            :class:`~org.orekit.propagation.events.EventEnablingPredicateFilter`
    """
    def __init__(self, t: _EventSlopeFilter__T, filterType: FilterType): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
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
            Get filter type.
        
            Returns:
                filter type
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class ExtremumApproachDetector(AbstractDetector['ExtremumApproachDetector']):
    """
    public class ExtremumApproachDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.ExtremumApproachDetector`>
    
        Finder for extremum approach events.
    
        This class finds extremum approach events (i.e. closest or farthest approach).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at farthest approach and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at closest approach. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction (go to the end of the
        documentation to see an example).
    
        As this detector needs two objects (moving relative to each other), it embeds one
        :class:`~org.orekit.utils.PVCoordinatesProvider` for the secondary object and is registered as an event detector in the
        propagator of the primary object. The secondary object :class:`~org.orekit.utils.PVCoordinatesProvider` will therefore
        be driven by this detector (and hence by the propagator in which this detector is registered).
    
        **In order to avoid infinite recursion, care must be taken to have the secondary object provider being *completely
        independent* from anything else. In particular, if the provider is a propagator, it should *not* be run together in a
        :class:`~org.orekit.propagation.PropagatorsParallelizer` with the propagator this detector is registered in. It is fine
        however to configure two separate propagators PsA and PsB with similar settings for the secondary object and one
        propagator Pm for the primary object and then use Psa in this detector registered within Pm while Pm and Psb are run in
        the context of a :class:`~org.orekit.propagation.PropagatorsParallelizer`.**
    
        For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical
        propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally
        costly.
    
        Also, it is possible to detect solely one type of event using an
        :class:`~org.orekit.propagation.events.EventSlopeFilter`. For example in order to only detect closest approach, one
        should type the following :
    
        .. code-block: java
        
         ExtremumApproachDetector extremumApproachDetector = new ExtremumApproachDetector(secondaryPVProvider);
         EventDetector closeApproachDetector = new EventSlopeFilter<ExtremumApproachDetector>(extremumApproachDetector,FilterType.TRIGGER_ONLY_INCREASING_EVENTS);
          
         
    
        Since:
            11.3
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`, :class:`~org.orekit.propagation.events.EventSlopeFilter`,
            :class:`~org.orekit.propagation.events.FilterType`
    """
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider): ...
    def computeDeltaPV(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.utils.PVCoordinates:
        """
            Deprecated.
            The output type of this method shall be modified in the future to improve code efficiency (though it will still give
            access to the relative position and velocity)
            Compute the relative PV between primary and secondary objects.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): Spacecraft state.
        
            Returns:
                Relative position between primary (=s) and secondaryPVProvider.
        
        
        """
        ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            The :code:`g` is positive when the primary object is getting further away from the secondary object and is negative when
            it is getting closer to it.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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

_FieldAltitudeDetector__T = typing.TypeVar('_FieldAltitudeDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAltitudeDetector(FieldAbstractDetector['FieldAltitudeDetector'[_FieldAltitudeDetector__T], _FieldAltitudeDetector__T], typing.Generic[_FieldAltitudeDetector__T]):
    """
    public class FieldAltitudeDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldAltitudeDetector`<T>, T>
    
        Finder for satellite altitude crossing events.
    
        This class finds altitude events (i.e. satellite crossing a predefined altitude level above ground).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when ascending and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when descending. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction.
    
        Since:
            9.0
    
        Also see:
            :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, t: _FieldAltitudeDetector__T, t2: _FieldAltitudeDetector__T, t3: _FieldAltitudeDetector__T, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, t: _FieldAltitudeDetector__T, t2: _FieldAltitudeDetector__T, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, t: _FieldAltitudeDetector__T, bodyShape: org.orekit.bodies.BodyShape): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAltitudeDetector__T]) -> _FieldAltitudeDetector__T: ...
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

_FieldApsideDetector__T = typing.TypeVar('_FieldApsideDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldApsideDetector(FieldAbstractDetector['FieldApsideDetector'[_FieldApsideDetector__T], _FieldApsideDetector__T], typing.Generic[_FieldApsideDetector__T]):
    """
    public class FieldApsideDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldApsideDetector`<T>, T>
    
        Finder for apside crossing events.
    
        This class finds apside crossing events (i.e. apogee or perigee crossing).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at apogee crossing and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at perigee crossing. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction.
    
        Beware that apside detection will fail for almost circular orbits. If for example an apside detector is used to trigger
        an :class:`~org.orekit.forces.maneuvers.ImpulseManeuver` and the maneuver change the orbit shape to circular, then the
        detector may completely fail just after the maneuver has been performed!
    
        Also see:
            :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, t: _FieldApsideDetector__T): ...
    @typing.overload
    def __init__(self, t: _FieldApsideDetector__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldApsideDetector__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldApsideDetector__T]): ...
    @typing.overload
    def __init__(self, fieldAdaptableInterval: typing.Union[FieldAdaptableInterval[_FieldApsideDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], float]], t: _FieldApsideDetector__T, int: int, fieldEventHandler: org.orekit.propagation.events.handlers.FieldEventHandler[_FieldApsideDetector__T]): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldApsideDetector__T]) -> _FieldApsideDetector__T: ...

_FieldBetaAngleDetector__T = typing.TypeVar('_FieldBetaAngleDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBetaAngleDetector(FieldAbstractDetector['FieldBetaAngleDetector'[_FieldBetaAngleDetector__T], _FieldBetaAngleDetector__T], typing.Generic[_FieldBetaAngleDetector__T]):
    """
    public class FieldBetaAngleDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldBetaAngleDetector`<T>, T>
    
        Finder for beta angle crossing events.
    
        Locate events when the beta angle (the angle between the orbit plane and the celestial body) crosses a threshold. The
        :meth:`~org.orekit.propagation.events.FieldBetaAngleDetector.g` function is negative when the beta angle is above the
        threshold and positive when the beta angle is below the threshold.
    
        The inertial frame provided must have it's origin centered at the satellite's orbit plane. The beta angle is computed as
        the angle between the celestial body's position in this frame with the satellite's orbital momentum vector.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at the first event date occurrence. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction.
    
        Since:
            12.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, t: _FieldBetaAngleDetector__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldBetaAngleDetector__T], t: _FieldBetaAngleDetector__T, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_FieldBetaAngleDetector__T], frame: org.orekit.frames.Frame): ...
    _calculateBetaAngle_0__T = typing.TypeVar('_calculateBetaAngle_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _calculateBetaAngle_1__T = typing.TypeVar('_calculateBetaAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def calculateBetaAngle(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_calculateBetaAngle_0__T], fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_calculateBetaAngle_0__T]) -> _calculateBetaAngle_0__T:
        """
            Calculate the beta angle between the orbit plane and the celestial body.
        
            This method computes the beta angle using the frame from the spacecraft state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                celestialBodyProvider (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> celestialBodyProvider): celestial body coordinate provider
        
            Returns:
                the beta angle (radians)
        
        """
        ...
    @typing.overload
    @staticmethod
    def calculateBetaAngle(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_calculateBetaAngle_1__T], fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_calculateBetaAngle_1__T], frame: org.orekit.frames.Frame) -> _calculateBetaAngle_1__T:
        """
            Calculate the beta angle between the orbit plane and the celestial body.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                celestialBodyProvider (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> celestialBodyProvider): celestial body coordinate provider
                frame (:class:`~org.orekit.frames.Frame`): inertial frame in which beta angle will be computed
        
            Returns:
                the beta angle (radians)
        
        
        """
        ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldBetaAngleDetector__T]) -> _FieldBetaAngleDetector__T: ...
    def getBetaAngleThreshold(self) -> _FieldBetaAngleDetector__T:
        """
            The beta angle threshold (radians).
        
            Returns:
                the beta angle threshold (radians)
        
        
        """
        ...
    def getCelestialBodyProvider(self) -> org.orekit.utils.FieldPVCoordinatesProvider[_FieldBetaAngleDetector__T]: ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
            The inertial frame in which beta angle is computed.
        
            Returns:
                the inertial frame
        
        
        """
        ...
    def withBetaThreshold(self, t: _FieldBetaAngleDetector__T) -> 'FieldBetaAngleDetector'[_FieldBetaAngleDetector__T]: ...
    def withCelestialProvider(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_FieldBetaAngleDetector__T]) -> 'FieldBetaAngleDetector'[_FieldBetaAngleDetector__T]: ...
    def withInertialFrame(self, frame: org.orekit.frames.Frame) -> 'FieldBetaAngleDetector'[_FieldBetaAngleDetector__T]: ...

_FieldBooleanDetector__T = typing.TypeVar('_FieldBooleanDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBooleanDetector(FieldAbstractDetector['FieldBooleanDetector'[_FieldBooleanDetector__T], _FieldBooleanDetector__T], typing.Generic[_FieldBooleanDetector__T]):
    """
    public class FieldBooleanDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldBooleanDetector`<T>, T>
    
        This class provides AND and OR operations for event detectors. This class treats positive values of the g function as
        true and negative values as false.
    
        One example for an imaging satellite might be to only detect events when a satellite is overhead (elevation > 0) AND
        when the ground point is sunlit (Sun elevation > 0). Another slightly contrived example using the OR operator would be
        to detect access to a set of ground stations and only report events when the satellite enters or leaves the field of
        view of the set, but not hand-offs between the ground stations.
    
        For the FieldBooleanDetector is important that the sign of the g function of the underlying event detector is not
        arbitrary, but has a semantic meaning, e.g. in or out, true or false. This class works well with event detectors that
        detect entry to or exit from a region, e.g. :class:`~org.orekit.propagation.events.FieldEclipseDetector`,
        :class:`~org.orekit.propagation.events.FieldElevationDetector`,
        :class:`~org.orekit.propagation.events.FieldLatitudeCrossingDetector`. Using this detector with detectors that are not
        based on entry to or exit from a region, e.g. :class:`~org.orekit.propagation.events.FieldDateDetector`, will likely
        lead to unexpected results. To apply conditions to this latter type of event detectors a
        :class:`~org.orekit.propagation.events.FieldEventEnablingPredicateFilter` is usually more appropriate.
    
        Since:
            12.0
    
        Also see:
            :meth:`~org.orekit.propagation.events.FieldBooleanDetector.andCombine`,
            :meth:`~org.orekit.propagation.events.FieldBooleanDetector.orCombine`,
            :meth:`~org.orekit.propagation.events.FieldBooleanDetector.notCombine`,
            :class:`~org.orekit.propagation.events.EventEnablingPredicateFilter`,
            :class:`~org.orekit.propagation.events.EventSlopeFilter`
    """
    _andCombine_0__T = typing.TypeVar('_andCombine_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _andCombine_1__T = typing.TypeVar('_andCombine_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def andCombine(collection: typing.Union[java.util.Collection[FieldEventDetector[_andCombine_0__T]], typing.Sequence[FieldEventDetector[_andCombine_0__T]]]) -> 'FieldBooleanDetector'[_andCombine_0__T]: ...
    @typing.overload
    @staticmethod
    def andCombine(fieldEventDetectorArray: typing.List[FieldEventDetector[_andCombine_1__T]]) -> 'FieldBooleanDetector'[_andCombine_1__T]: ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldBooleanDetector__T]) -> _FieldBooleanDetector__T: ...
    def getDetectors(self) -> java.util.List[FieldEventDetector[_FieldBooleanDetector__T]]: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldBooleanDetector__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldBooleanDetector__T]) -> None: ...
    _notCombine__T = typing.TypeVar('_notCombine__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def notCombine(fieldEventDetector: FieldEventDetector[_notCombine__T]) -> 'FieldNegateDetector'[_notCombine__T]:
        """
            Create a new event detector that negates the g function of another detector.
        
            This detector will be initialized with the same
            :meth:`~org.orekit.propagation.events.FieldEventDetector.getMaxCheckInterval`,
            :meth:`~org.orekit.propagation.events.FieldEventDetector.getThreshold`, and
            :meth:`~org.orekit.propagation.events.FieldEventDetector.getMaxIterationCount` as :code:`detector`. The event handler of
            the underlying detector is not used, instead the default handler is
            :class:`~org.orekit.propagation.events.handlers.FieldContinueOnEvent`.
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.FieldEventDetector`<T> detector): to negate.
        
            Returns:
                an new event detector whose g function is the same magnitude but opposite sign of :code:`detector`.
        
            Also see:
                :meth:`~org.orekit.propagation.events.FieldBooleanDetector.andCombine`,
                :meth:`~org.orekit.propagation.events.FieldBooleanDetector.orCombine`,
                :class:`~org.orekit.propagation.events.FieldBooleanDetector`
        
        
        """
        ...
    _orCombine_0__T = typing.TypeVar('_orCombine_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _orCombine_1__T = typing.TypeVar('_orCombine_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def orCombine(collection: typing.Union[java.util.Collection[FieldEventDetector[_orCombine_0__T]], typing.Sequence[FieldEventDetector[_orCombine_0__T]]]) -> 'FieldBooleanDetector'[_orCombine_0__T]: ...
    @typing.overload
    @staticmethod
    def orCombine(fieldEventDetectorArray: typing.List[FieldEventDetector[_orCombine_1__T]]) -> 'FieldBooleanDetector'[_orCombine_1__T]: ...

_FieldCylindricalShadowEclipseDetector__T = typing.TypeVar('_FieldCylindricalShadowEclipseDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCylindricalShadowEclipseDetector(FieldAbstractDetector['FieldCylindricalShadowEclipseDetector'[_FieldCylindricalShadowEclipseDetector__T], _FieldCylindricalShadowEclipseDetector__T], typing.Generic[_FieldCylindricalShadowEclipseDetector__T]):
    """
    public class FieldCylindricalShadowEclipseDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldCylindricalShadowEclipseDetector`<T>, T>
    
        Event detector for eclipses from a single, infinitely-distant light source, occulted by a spherical central body. The
        shadow region is cylindrical, a model less accurate than a conical one but more computationally-performant.
    
        The so-called g function is negative in eclipse, positive otherwise.
    
        Since:
            12.
    
        Also see:
            :class:`~org.orekit.propagation.events.FieldEclipseDetector`,
            :class:`~org.orekit.propagation.events.CylindricalShadowEclipseDetector`
    """
    @typing.overload
    def __init__(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, t: _FieldCylindricalShadowEclipseDetector__T, fieldAdaptableInterval: typing.Union[FieldAdaptableInterval[_FieldCylindricalShadowEclipseDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], float]], t2: _FieldCylindricalShadowEclipseDetector__T, int: int, fieldEventHandler: org.orekit.propagation.events.handlers.FieldEventHandler[_FieldCylindricalShadowEclipseDetector__T]): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, t: _FieldCylindricalShadowEclipseDetector__T, fieldEventDetectionSettings: FieldEventDetectionSettings[_FieldCylindricalShadowEclipseDetector__T], fieldEventHandler: org.orekit.propagation.events.handlers.FieldEventHandler[_FieldCylindricalShadowEclipseDetector__T]): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, t: _FieldCylindricalShadowEclipseDetector__T, fieldEventHandler: org.orekit.propagation.events.handlers.FieldEventHandler[_FieldCylindricalShadowEclipseDetector__T]): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldCylindricalShadowEclipseDetector__T]) -> _FieldCylindricalShadowEclipseDetector__T: ...
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
    public class FieldDateDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldDateDetector`<T>, T> implements :class:`~org.orekit.time.FieldTimeStamped`<T>
    
        Finder for date events.
    
        This class finds date events (i.e. occurrence of some predefined dates).
    
        As of version 5.1, it is an enhanced date detector:
    
          - it can be defined without prior date (:meth:`~org.orekit.propagation.events.FieldDateDetector.%3Cinit%3E`)
          - several dates can be added (:meth:`~org.orekit.propagation.events.FieldDateDetector.addEventDate`)
    
    
        The gap between the added dates must be more than the minGap.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at the first event date occurrence. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction.
    
        Also see:
            :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAX_CHECK
    
        Default value for max check.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MIN_GAP: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MIN_GAP
    
        Default value for minimum gap between added dates.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default value for convergence threshold.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, field: org.hipparchus.Field[_FieldDateDetector__T], fieldTimeStampedArray: typing.List[org.orekit.time.FieldTimeStamped[_FieldDateDetector__T]]): ...
    def addEventDate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldDateDetector__T]) -> None: ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldDateDetector__T]) -> _FieldDateDetector__T: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldDateDetector__T]: ...
    def getDates(self) -> java.util.List[org.orekit.time.FieldTimeStamped[_FieldDateDetector__T]]: ...
    def withMinGap(self, double: float) -> 'FieldDateDetector'[_FieldDateDetector__T]: ...

_FieldEclipseDetector__T = typing.TypeVar('_FieldEclipseDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEclipseDetector(FieldAbstractDetector['FieldEclipseDetector'[_FieldEclipseDetector__T], _FieldEclipseDetector__T], typing.Generic[_FieldEclipseDetector__T]):
    """
    public class FieldEclipseDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldEclipseDetector`<T>, T>
    
        Finder for satellite eclipse related events.
    
        This class finds eclipse events, i.e. satellite within umbra (total eclipse) or penumbra (partial eclipse).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when entering the eclipse and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when exiting the eclipse. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction.
    
        Also see:
            :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEclipseDetector__T], extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEclipseDetector__T], occultationEngine: org.orekit.utils.OccultationEngine): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEclipseDetector__T]) -> _FieldEclipseDetector__T: ...
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
    def withMargin(self, t: _FieldEclipseDetector__T) -> 'FieldEclipseDetector'[_FieldEclipseDetector__T]: ...
    def withPenumbra(self) -> 'FieldEclipseDetector'[_FieldEclipseDetector__T]: ...
    def withUmbra(self) -> 'FieldEclipseDetector'[_FieldEclipseDetector__T]: ...

_FieldElevationDetector__T = typing.TypeVar('_FieldElevationDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldElevationDetector(FieldAbstractDetector['FieldElevationDetector'[_FieldElevationDetector__T], _FieldElevationDetector__T], typing.Generic[_FieldElevationDetector__T]):
    """
    public class FieldElevationDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldElevationDetector`<T>, T>
    
        Finder for satellite raising/setting events that allows for the setting of azimuth and/or elevation bounds or a ground
        azimuth/elevation mask input. Each calculation be configured to use atmospheric refraction as well.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at raising and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at setting. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction.
    """
    @typing.overload
    def __init__(self, t: _FieldElevationDetector__T, t2: _FieldElevationDetector__T, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldElevationDetector__T], topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldElevationDetector__T]) -> _FieldElevationDetector__T: ...
    def getElevationMask(self) -> org.orekit.utils.ElevationMask:
        """
            Returns the currently configured elevation mask.
        
            Returns:
                elevation mask (null if instance has been configured with
                :meth:`~org.orekit.propagation.events.FieldElevationDetector.withConstantElevation`
        
            Also see:
                :meth:`~org.orekit.propagation.events.FieldElevationDetector.withElevationMask`
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
            Returns the currently configured minimum valid elevation value.
        
            Returns:
                minimum elevation value (:code:`Double.NaN` if instance has been configured with
                :meth:`~org.orekit.propagation.events.FieldElevationDetector.withElevationMask`
        
            Also see:
                :meth:`~org.orekit.propagation.events.FieldElevationDetector.withConstantElevation`
        
        
        """
        ...
    def getRefractionModel(self) -> org.orekit.models.AtmosphericRefractionModel:
        """
            Returns the currently configured refraction model.
        
            Returns:
                refraction model
        
            Also see:
                :meth:`~org.orekit.propagation.events.FieldElevationDetector.withRefraction`
        
        
        """
        ...
    def getTopocentricFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
            Returns the currently configured topocentric frame definitions.
        
            Returns:
                topocentric frame definition
        
        
        """
        ...
    def withConstantElevation(self, double: float) -> 'FieldElevationDetector'[_FieldElevationDetector__T]: ...
    def withElevationMask(self, elevationMask: org.orekit.utils.ElevationMask) -> 'FieldElevationDetector'[_FieldElevationDetector__T]: ...
    def withRefraction(self, atmosphericRefractionModel: org.orekit.models.AtmosphericRefractionModel) -> 'FieldElevationDetector'[_FieldElevationDetector__T]: ...

_FieldElevationExtremumDetector__T = typing.TypeVar('_FieldElevationExtremumDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldElevationExtremumDetector(FieldAbstractDetector['FieldElevationExtremumDetector'[_FieldElevationExtremumDetector__T], _FieldElevationExtremumDetector__T], typing.Generic[_FieldElevationExtremumDetector__T]):
    """
    public class FieldElevationExtremumDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldElevationExtremumDetector`<T>, T>
    
        Detector for elevation extremum with respect to a ground point.
    
        This detector identifies when a spacecraft reaches its extremum elevation with respect to a ground point.
    
        As in most cases only the elevation maximum is needed and the minimum is often irrelevant, this detector is often
        wrapped into an
        :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.FieldEventSlopeFilter?is`
        configured with :meth:`~org.orekit.propagation.events.FilterType.TRIGGER_ONLY_DECREASING_EVENTS` (i.e. when the
        elevation derivative decreases from positive values to negative values, which correspond to a maximum). Setting up this
        filter saves some computation time as the elevation minimum occurrences are not even looked at. It is however still
        often necessary to do an additional filtering
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, t: _FieldElevationExtremumDetector__T, t2: _FieldElevationExtremumDetector__T, topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldElevationExtremumDetector__T], topocentricFrame: org.orekit.frames.TopocentricFrame): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldElevationExtremumDetector__T]) -> _FieldElevationExtremumDetector__T: ...
    def getElevation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldElevationExtremumDetector__T]) -> _FieldElevationExtremumDetector__T: ...
    def getTopocentricFrame(self) -> org.orekit.frames.TopocentricFrame:
        """
            Returns the topocentric frame centered on ground point.
        
            Returns:
                topocentric frame centered on ground point
        
        
        """
        ...

_FieldEventEnablingPredicateFilter__T = typing.TypeVar('_FieldEventEnablingPredicateFilter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventEnablingPredicateFilter(FieldAbstractDetector['FieldEventEnablingPredicateFilter'[_FieldEventEnablingPredicateFilter__T], _FieldEventEnablingPredicateFilter__T], typing.Generic[_FieldEventEnablingPredicateFilter__T]):
    """
    public class FieldEventEnablingPredicateFilter<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldEventEnablingPredicateFilter`<T>, T>
    
        Wrapper used to detect events only when enabled by an external predicated function.
    
        General :class:`~org.orekit.propagation.events.FieldEventDetector` are defined implicitly by a
        :meth:`~org.orekit.propagation.events.FieldEventDetector.g` crossing zero. This implies that during an orbit
        propagation, events are triggered at all zero crossings.
    
        Sometimes, users would like to enable or disable events by themselves, for example to trigger them only for certain
        orbits, or to check elevation maximums only when elevation itself is positive (i.e. they want to discard elevation
        maximums below ground). In these cases, looking precisely for all events location and triggering events that will later
        be ignored is a waste of computing time.
    
        Users can wrap a regular :class:`~org.orekit.propagation.events.FieldEventDetector` in an instance of this class and
        provide this wrapping instance to a :class:`~org.orekit.propagation.FieldPropagator` in order to avoid wasting time
        looking for uninteresting events. The wrapper will intercept the calls to the
        :meth:`~org.orekit.propagation.events.FieldEventDetector.g` and to the
        :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.eventOccurred` method in order to ignore uninteresting
        events. The wrapped regular :class:`~org.orekit.propagation.events.FieldEventDetector` will the see only the interesting
        events, i.e. either only events that occur when a user-provided event enabling predicate function is true, ignoring all
        events that occur when the event enabling predicate function is false. The number of calls to the
        :meth:`~org.orekit.propagation.events.FieldEventDetector.g` will also be reduced.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.propagation.events.FieldEventSlopeFilter`
    """
    def __init__(self, fieldEventDetector: FieldEventDetector[_FieldEventEnablingPredicateFilter__T], fieldEnablingPredicate: FieldEnablingPredicate[_FieldEventEnablingPredicateFilter__T]): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventEnablingPredicateFilter__T]) -> _FieldEventEnablingPredicateFilter__T: ...
    def getDetector(self) -> FieldEventDetector[_FieldEventEnablingPredicateFilter__T]: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventEnablingPredicateFilter__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEventEnablingPredicateFilter__T]) -> None: ...

_FieldEventSlopeFilter__D = typing.TypeVar('_FieldEventSlopeFilter__D', bound=FieldEventDetector)  # <D>
_FieldEventSlopeFilter__T = typing.TypeVar('_FieldEventSlopeFilter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventSlopeFilter(FieldAbstractDetector['FieldEventSlopeFilter'[_FieldEventSlopeFilter__D, _FieldEventSlopeFilter__T], _FieldEventSlopeFilter__T], typing.Generic[_FieldEventSlopeFilter__D, _FieldEventSlopeFilter__T]):
    """
    public class FieldEventSlopeFilter<D extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>, T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldEventSlopeFilter`<D, T>, T>
    
        Wrapper used to detect only increasing or decreasing events.
    
        This class is heavily based on the class EventFilter from the Hipparchus library. The changes performed consist in
        replacing raw types (double and double arrays) with space dynamics types (:class:`~org.orekit.time.FieldAbsoluteDate`,
        :class:`~org.orekit.propagation.FieldSpacecraftState`).
    
        General :class:`~org.orekit.propagation.events.FieldEventDetector` are defined implicitly by a
        :meth:`~org.orekit.propagation.events.FieldEventDetector.g` crossing zero. This function needs to be continuous in the
        event neighborhood, and its sign must remain consistent between events. This implies that during an orbit propagation,
        events triggered are alternately events for which the function increases from negative to positive values, and events
        for which the function decreases from positive to negative values.
    
        Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type.
        In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of
        computing time.
    
        Users can wrap a regular :class:`~org.orekit.propagation.events.FieldEventDetector` in an instance of this class and
        provide this wrapping instance to a :class:`~org.orekit.propagation.FieldPropagator` in order to avoid wasting time
        looking for uninteresting events. The wrapper will intercept the calls to the
        :meth:`~org.orekit.propagation.events.FieldEventDetector.g` and to the
        :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.eventOccurred` method in order to ignore uninteresting
        events. The wrapped regular :class:`~org.orekit.propagation.events.FieldEventDetector` will then see only the
        interesting events, i.e. either only :code:`increasing` events or only :code:`decreasing` events. The number of calls to
        the :meth:`~org.orekit.propagation.events.FieldEventDetector.g` will also be reduced.
    
        Also see:
            :class:`~org.orekit.propagation.events.FieldEventEnablingPredicateFilter`
    """
    def __init__(self, d: _FieldEventSlopeFilter__D, filterType: FilterType): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventSlopeFilter__T]) -> _FieldEventSlopeFilter__T: ...
    def getDetector(self) -> _FieldEventSlopeFilter__D:
        """
            Get the wrapped raw detector.
        
            Returns:
                the wrapped raw detector
        
        
        """
        ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventSlopeFilter__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEventSlopeFilter__T]) -> None: ...

_FieldExtremumApproachDetector__T = typing.TypeVar('_FieldExtremumApproachDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldExtremumApproachDetector(FieldAbstractDetector['FieldExtremumApproachDetector'[_FieldExtremumApproachDetector__T], _FieldExtremumApproachDetector__T], typing.Generic[_FieldExtremumApproachDetector__T]):
    """
    public class FieldExtremumApproachDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldExtremumApproachDetector`<T>, T>
    
        Finder for extremum approach events.
    
        This class finds extremum approach events (i.e. closest or farthest approach).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at farthest approach and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at closest approach. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction (go to the end of the
        documentation to see an example).
    
        As this detector needs two objects (moving relative to each other), it embeds one
        :class:`~org.orekit.utils.FieldPVCoordinatesProvider` for the secondary object and is registered as an event detector in
        the propagator of the primary object. The secondary object :class:`~org.orekit.utils.FieldPVCoordinatesProvider` will
        therefore be driven by this detector (and hence by the propagator in which this detector is registered). Note that you
        can also create this detector using a standard :class:`~org.orekit.utils.PVCoordinatesProvider`
    
        **In order to avoid infinite recursion, care must be taken to have the secondary object provider being *completely
        independent* from anything else. In particular, if the provider is a propagator, it should *not* be run together in a
        :class:`~org.orekit.propagation.PropagatorsParallelizer` with the propagator this detector is registered in. It is fine
        however to configure two separate propagators PsA and PsB with similar settings for the secondary object and one
        propagator Pm for the primary object and then use Psa in this detector registered within Pm while Pm and Psb are run in
        the context of a :class:`~org.orekit.propagation.PropagatorsParallelizer`.**
    
        For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical
        propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally
        costly.
    
        Also, it is possible to detect solely one type of event using an
        :class:`~org.orekit.propagation.events.EventSlopeFilter`. For example in order to only detect closest approach, one
        should type the following :
    
        .. code-block: java
        
         FieldExtremumApproachDetector<Type> extremumApproachDetector = new FieldExtremumApproachDetector<>(field, secondaryPVProvider);
         FieldEventDetector<Type> closeApproachDetector = new FieldEventSlopeFilter<>(extremumApproachDetector, FilterType.TRIGGER_ONLY_INCREASING_EVENTS);
          
         
    
        Since:
            11.3
    
        Also see:
            :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`,
            :class:`~org.orekit.propagation.events.FieldEventSlopeFilter`, :class:`~org.orekit.propagation.events.FilterType`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldExtremumApproachDetector__T], fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_FieldExtremumApproachDetector__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldExtremumApproachDetector__T], pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider): ...
    def computeDeltaPV(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldExtremumApproachDetector__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldExtremumApproachDetector__T]: ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldExtremumApproachDetector__T]) -> _FieldExtremumApproachDetector__T: ...
    def getSecondaryPVProvider(self) -> org.orekit.utils.FieldPVCoordinatesProvider[_FieldExtremumApproachDetector__T]: ...

_FieldFunctionalDetector__T = typing.TypeVar('_FieldFunctionalDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldFunctionalDetector(FieldAbstractDetector['FieldFunctionalDetector'[_FieldFunctionalDetector__T], _FieldFunctionalDetector__T], typing.Generic[_FieldFunctionalDetector__T]):
    """
    public class FieldFunctionalDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldFunctionalDetector`<T>, T>
    
        A detector that implements the :meth:`~org.orekit.propagation.events.FieldFunctionalDetector.g` function using a lambda
        that can be set using :meth:`~org.orekit.propagation.events.FieldFunctionalDetector.withFunction`.
    
        For example, to create a simple date detector use:
    
        .. code-block: java
        
         FieldFunctionalDetector<T> d = new FieldFunctionalDetector<>(field)
             .withGFunction((s) -> s.getDate().durationFrom(triggerDate))
             .withMaxCheck(field.getZero().add(1e10));
         
    
        Since:
            10.2
    """
    def __init__(self, field: org.hipparchus.Field[_FieldFunctionalDetector__T]): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T]) -> _FieldFunctionalDetector__T: ...
    def getFunction(self) -> java.util.function.Function[org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T], _FieldFunctionalDetector__T]: ...
    def withFunction(self, function: typing.Union[java.util.function.Function[org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T], _FieldFunctionalDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[_FieldFunctionalDetector__T]], _FieldFunctionalDetector__T]]) -> 'FieldFunctionalDetector'[_FieldFunctionalDetector__T]: ...

_FieldLatitudeCrossingDetector__T = typing.TypeVar('_FieldLatitudeCrossingDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLatitudeCrossingDetector(FieldAbstractDetector['FieldLatitudeCrossingDetector'[_FieldLatitudeCrossingDetector__T], _FieldLatitudeCrossingDetector__T], typing.Generic[_FieldLatitudeCrossingDetector__T]):
    """
    public class FieldLatitudeCrossingDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldLatitudeCrossingDetector`<T>, T>
    
        Detector for geographic latitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed latitude with respect to a central body.
    
        Since:
            9.3
    """
    @typing.overload
    def __init__(self, t: _FieldLatitudeCrossingDetector__T, t2: _FieldLatitudeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLatitudeCrossingDetector__T], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldLatitudeCrossingDetector__T]) -> _FieldLatitudeCrossingDetector__T: ...
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
    public class FieldLatitudeRangeCrossingDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldLatitudeRangeCrossingDetector`<T>, T>
    
        Detector for geographic latitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed latitude range with respect to a central body.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, t: _FieldLatitudeRangeCrossingDetector__T, t2: _FieldLatitudeRangeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLatitudeRangeCrossingDetector__T], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldLatitudeRangeCrossingDetector__T]) -> _FieldLatitudeRangeCrossingDetector__T: ...
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
    public class FieldLongitudeCrossingDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldLongitudeCrossingDetector`<T>, T>
    
        Detector for geographic longitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed longitude with respect to a central body.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, t: _FieldLongitudeCrossingDetector__T, t2: _FieldLongitudeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLongitudeCrossingDetector__T], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldLongitudeCrossingDetector__T]) -> _FieldLongitudeCrossingDetector__T: ...
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
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldLongitudeCrossingDetector__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldLongitudeCrossingDetector__T]) -> None: ...

_FieldLongitudeRangeCrossingDetector__T = typing.TypeVar('_FieldLongitudeRangeCrossingDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLongitudeRangeCrossingDetector(FieldAbstractDetector['FieldLongitudeRangeCrossingDetector'[_FieldLongitudeRangeCrossingDetector__T], _FieldLongitudeRangeCrossingDetector__T], typing.Generic[_FieldLongitudeRangeCrossingDetector__T]):
    """
    public class FieldLongitudeRangeCrossingDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldLongitudeRangeCrossingDetector`<T>, T>
    
        Detector for geographic longitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed longitude range with respect to a central body.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, t: _FieldLongitudeRangeCrossingDetector__T, t2: _FieldLongitudeRangeCrossingDetector__T, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldLongitudeRangeCrossingDetector__T], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldLongitudeRangeCrossingDetector__T]) -> _FieldLongitudeRangeCrossingDetector__T: ...
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
class FieldNegateDetector(FieldAbstractDetector['FieldNegateDetector'[_FieldNegateDetector__T], _FieldNegateDetector__T], typing.Generic[_FieldNegateDetector__T]):
    """
    public class FieldNegateDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldNegateDetector`<T>, T>
    
        An event detector that negates the sign on another event detector's
        :meth:`~org.orekit.propagation.events.FieldEventDetector.g` function.
    
        Since:
            12.0
    """
    def __init__(self, fieldEventDetector: FieldEventDetector[_FieldNegateDetector__T]): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldNegateDetector__T]) -> _FieldNegateDetector__T: ...
    def getOriginal(self) -> FieldEventDetector[_FieldNegateDetector__T]: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldNegateDetector__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldNegateDetector__T]) -> None: ...

_FieldNodeDetector__T = typing.TypeVar('_FieldNodeDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNodeDetector(FieldAbstractDetector['FieldNodeDetector'[_FieldNodeDetector__T], _FieldNodeDetector__T], typing.Generic[_FieldNodeDetector__T]):
    """
    public class FieldNodeDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldNodeDetector`<T>, T>
    
        Finder for node crossing events.
    
        This class finds equator crossing events (i.e. ascending or descending node crossing).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at descending node crossing and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at ascending node crossing. This can be changed by calling
        :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` after construction.
    
        Beware that node detection will fail for almost equatorial orbits. If for example a node detector is used to trigger an
        :class:`~org.orekit.forces.maneuvers.ImpulseManeuver` and the maneuver turn the orbit plane to equator, then the
        detector may completely fail just after the maneuver has been performed! This is a real case that has been encountered
        during validation ...
    
        Also see:
            :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, t: _FieldNodeDetector__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldNodeDetector__T], frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldNodeDetector__T], frame: org.orekit.frames.Frame): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldNodeDetector__T]) -> _FieldNodeDetector__T: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the equator is defined.
        
            Returns:
                the frame in which the equator is defined
        
        
        """
        ...

class FieldOfViewDetector(AbstractDetector['FieldOfViewDetector']):
    """
    public class FieldOfViewDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.FieldOfViewDetector`>
    
        Finder for target entry/exit events with respect to a satellite sensor :class:`~org.orekit.geometry.fov.FieldOfView`.
    
        Beware that this detector is unaware of any bodies occluding line-of-sight to the target. It can be therefore used for
        many contexts from Earth Observation to interplanetary mission design. For instance, in an Earth Observation context, it
        can be easily combined to an :class:`~org.orekit.propagation.events.ElevationDetector` using
        :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine` to calculate station visibility opportunities within
        the satellite's field of view.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at FOV entry and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at FOV exit. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Since:
            7.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`,
            :class:`~org.orekit.propagation.events.FootprintOverlapDetector`,
            :class:`~org.orekit.propagation.events.VisibilityTrigger`
    """
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, visibilityTrigger: VisibilityTrigger, fieldOfView: org.orekit.geometry.fov.FieldOfView): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, fieldOfView: org.orekit.geometry.fov.FieldOfView): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            The g function value is the angular offset between the target center and the
            :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`, plus or minus the target angular radius depending on
            the :class:`~org.orekit.propagation.events.VisibilityTrigger`, minus the
            :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin`. It is therefore negative if the target is visible within the
            Field Of View and positive if it is outside of the Field Of View.
        
            As per the previous definition, when the target enters the Field Of View, a decreasing event is generated, and when the
            target leaves the Field Of View, an increasing event is generated.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class FieldParameterDrivenDateIntervalDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector`<T>, T>
    
        Detector for date intervals that may be offset thanks to parameter drivers.
    
        Two dual views can be used for date intervals: either start date/stop date or median date/duration.
        :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getStartDriver`/:meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getStopDriver`
        drivers and
        :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getMedianDriver`/:meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getDurationDriver`
        drivers work in pair. Both drivers in one pair can be selected and their changes will be propagated to the other pair,
        but attempting to select drivers in both pairs at the same time will trigger an exception. Changing the value of a
        driver that is not selected should be avoided as it leads to inconsistencies between the pairs.
    
        Since:
            11.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    START_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` START_SUFFIX
    
        Default suffix for start driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    STOP_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` STOP_SUFFIX
    
        Default suffix for stop driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEDIAN_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEDIAN_SUFFIX
    
        Default suffix for median driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DURATION_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DURATION_SUFFIX
    
        Default suffix for duration driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldParameterDrivenDateIntervalDetector__T], string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldParameterDrivenDateIntervalDetector__T], string: str, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldParameterDrivenDateIntervalDetector__T]) -> _FieldParameterDrivenDateIntervalDetector__T: ...
    def getDurationDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for duration.
        
            Note that the duration is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getStartDriver` start date or
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getStopDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` changed.
        
            Returns:
                driver for duration
        
        
        """
        ...
    def getMedianDriver(self) -> org.orekit.utils.DateDriver:
        """
            Get the driver for median date.
        
            Note that the median date is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getStartDriver` start date or
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getStopDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` changed.
        
            Returns:
                driver for median date
        
        
        """
        ...
    def getStartDriver(self) -> org.orekit.utils.DateDriver:
        """
            Get the driver for start date.
        
            Note that the start date is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getMedianDriver` or
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getDurationDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` and changed.
        
            Returns:
                driver for start date
        
        
        """
        ...
    def getStopDriver(self) -> org.orekit.utils.DateDriver:
        """
            Get the driver for stop date.
        
            Note that the stop date is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getMedianDriver` or
            :meth:`~org.orekit.propagation.events.FieldParameterDrivenDateIntervalDetector.getDurationDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` changed.
        
            Returns:
                driver for stop date
        
        
        """
        ...

_FieldRelativeDistanceDetector__T = typing.TypeVar('_FieldRelativeDistanceDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRelativeDistanceDetector(FieldAbstractDetector['FieldRelativeDistanceDetector'[_FieldRelativeDistanceDetector__T], _FieldRelativeDistanceDetector__T], typing.Generic[_FieldRelativeDistanceDetector__T]):
    """
    public class FieldRelativeDistanceDetector<T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<:class:`~org.orekit.propagation.events.FieldRelativeDistanceDetector`<T>, T>
    
        Detector of specific value for the distance relative to another trajectory (using the Euclidean norm).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation. This can be changed by calling :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler`
        after construction.
    
        As this detector needs two objects (moving relative to each other), it embeds one
        :class:`~org.orekit.utils.FieldPVCoordinatesProvider` for the secondary object and is registered as an event detector in
        the propagator of the primary object. The secondary object :class:`~org.orekit.utils.FieldPVCoordinatesProvider` will
        therefore be driven by this detector (and hence by the propagator in which this detector is registered).
    
        For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical
        propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally
        costly.
    
        Since:
            12.1
    
        Also see:
            :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`
    """
    def __init__(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_FieldRelativeDistanceDetector__T], t: _FieldRelativeDistanceDetector__T): ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldRelativeDistanceDetector__T]) -> _FieldRelativeDistanceDetector__T: ...
    def getDistanceThreshold(self) -> _FieldRelativeDistanceDetector__T:
        """
            Get the relative distance threshold.
        
            Returns:
                threshold triggering detection
        
        
        """
        ...
    def getSecondaryPVProvider(self) -> org.orekit.utils.FieldPVCoordinatesProvider[_FieldRelativeDistanceDetector__T]: ...

class FootprintOverlapDetector(AbstractDetector['FootprintOverlapDetector']):
    """
    public class FootprintOverlapDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.FootprintOverlapDetector`>
    
        Detector triggered by geographical region entering/leaving a spacecraft sensor
        :class:`~org.orekit.geometry.fov.FieldOfView`.
    
        This detector is a mix between to :class:`~org.orekit.propagation.events.FieldOfViewDetector` and
        :class:`~org.orekit.propagation.events.GeographicZoneDetector`. Similar to the first detector above, it triggers events
        related to entry/exit of targets in a Field Of View, taking attitude into account. Similar to the second detector above,
        its target is an entire geographic region (which can even be split in several non-connected patches and can have holes).
    
        This detector is typically used for ground observation missions with agile satellites than can look away from nadir.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at FOV entry and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at FOV exit. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Since:
            7.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`,
            :class:`~org.orekit.propagation.events.FieldOfViewDetector`,
            :class:`~org.orekit.propagation.events.GeographicZoneDetector`
    """
    def __init__(self, fieldOfView: org.orekit.geometry.fov.FieldOfView, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            The g function value is the minimum offset among the region points with respect to the Field Of View boundary. It is
            positive if all region points are outside of the Field Of View, and negative if at least some of the region points are
            inside of the Field Of View. The minimum is computed by sampling the region, considering only the points for which the
            spacecraft is above the horizon. The accuracy of the detection depends on the linear sampling step set at detector
            construction. If the spacecraft is below horizon for all region points, an arbitrary positive value is returned.
        
            As per the previous definition, when the region enters the Field Of View, a decreasing event is generated, and when the
            region leaves the Field Of View, an increasing event is generated.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class FunctionalDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.FunctionalDetector`>
    
        A detector that implements the :meth:`~org.orekit.propagation.events.FunctionalDetector.g` function using a lambda that
        can be set using :meth:`~org.orekit.propagation.events.FunctionalDetector.withFunction`.
    
        For example, to create a simple date detector use:
    
        .. code-block: java
        
         FunctionalDetector d = new FunctionalDetector()
             .withGFunction((s) -> s.getDate().durationFrom(triggerDate))
             .withMaxCheck(1e10);
         
    
        Since:
            9.2
    """
    def __init__(self): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.EventDetector.g`
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getFunction(self) -> java.util.function.ToDoubleFunction[org.orekit.propagation.SpacecraftState]: ...
    def withFunction(self, toDoubleFunction: typing.Union[java.util.function.ToDoubleFunction[org.orekit.propagation.SpacecraftState], typing.Callable[[org.orekit.propagation.SpacecraftState], float]]) -> 'FunctionalDetector': ...

class GeographicZoneDetector(AbstractDetector['GeographicZoneDetector']):
    """
    public class GeographicZoneDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.GeographicZoneDetector`>
    
        Detector for entry/exit of a zone defined by geographic boundaries.
    
        This detector identifies when a spacecraft crosses boundaries of general shapes defined on the surface of the globe.
        Typical shapes of interest can be countries, land masses or physical areas like the south atlantic anomaly. Shapes can
        be arbitrarily complicated: convex or non-convex, in one piece or several non-connected islands, they can include poles,
        they can have holes like the Caspian Sea (this would be a hole only if one is interested in land masses, of course).
        Complex shapes involve of course more computing time than simple shapes.
    
        Since:
            6.2
    
        Also see:
            :class:`~org.orekit.propagation.events.FootprintOverlapDetector`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, bodyShape: org.orekit.bodies.BodyShape, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, double3: float): ...
    @typing.overload
    def __init__(self, bodyShape: org.orekit.bodies.BodyShape, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is the signed distance to boundary, minus the margin. It is positive if the spacecraft is outside of the zone
            and negative if it is inside.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def withMargin(self, double: float) -> 'GeographicZoneDetector':
        """
            Setup the detector margin.
        
            Parameters:
                newMargin (double): angular margin to apply to the zone
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...

class GroundAtNightDetector(AbstractDetector['GroundAtNightDetector']):
    """
    public class GroundAtNightDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.GroundAtNightDetector`>
    
        Detector for ground location being at night.
    
        This detector is mainly useful for scheduling optical measurements (either passive telescope observation of satellites
        against the stars background or active satellite laser ranging).
    
        The :code:`g` function of this detector is positive when ground is at night (i.e. Sun is below dawn/dusk elevation
        angle).
    
        Since:
            9.3
    """
    CIVIL_DAWN_DUSK_ELEVATION: typing.ClassVar[float] = ...
    """
    public static final double CIVIL_DAWN_DUSK_ELEVATION
    
        Sun elevation at civil dawn/dusk (6° below horizon).
    
    """
    NAUTICAL_DAWN_DUSK_ELEVATION: typing.ClassVar[float] = ...
    """
    public static final double NAUTICAL_DAWN_DUSK_ELEVATION
    
        Sun elevation at nautical dawn/dusk (12° below horizon).
    
    """
    ASTRONOMICAL_DAWN_DUSK_ELEVATION: typing.ClassVar[float] = ...
    """
    public static final double ASTRONOMICAL_DAWN_DUSK_ELEVATION
    
        Sun elevation at astronomical dawn/dusk (18° below horizon).
    
    """
    def __init__(self, topocentricFrame: org.orekit.frames.TopocentricFrame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, atmosphericRefractionModel: org.orekit.models.AtmosphericRefractionModel): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            The :code:`g` function of this detector is positive when ground is at night (i.e. Sun is below dawn/dusk elevation
            angle).
        
            This function only depends on date, not on the actual position of the spacecraft.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...

class GroundFieldOfViewDetector(AbstractDetector['GroundFieldOfViewDetector']):
    """
    public class GroundFieldOfViewDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.GroundFieldOfViewDetector`>
    
        Finder for satellite entry/exit events with respect to a sensor :class:`~org.orekit.geometry.fov.FieldOfView` attached
        to an arbitrary frame.
    
        If you only want to compute access times then you should probably use
        :class:`~org.orekit.propagation.events.ElevationDetector`.
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at FOV entry and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at FOV exit. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Since:
            7.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`,
            :class:`~org.orekit.propagation.events.FieldOfViewDetector`, :class:`~org.orekit.propagation.events.ElevationDetector`
    """
    def __init__(self, frame: org.orekit.frames.Frame, fieldOfView: org.orekit.geometry.fov.FieldOfView): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            The g function value is the angular offset between the satellite and the
            :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`. It is negative if the satellite is visible within the
            Field Of View and positive if it is outside of the Field Of View, including the margin.
        
            As per the previous definition, when the satellite enters the Field Of View, a decreasing event is generated, and when
            the satellite leaves the Field Of View, an increasing event is generated.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class HaloXZPlaneCrossingDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.HaloXZPlaneCrossingDetector`>
    
        Detector for XZ Plane crossing.
    
        Since:
            10.2
    """
    def __init__(self, double: float, double2: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                Position on Y axis
        
        
        """
        ...

class InterSatDirectViewDetector(AbstractDetector['InterSatDirectViewDetector']):
    """
    public class InterSatDirectViewDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.InterSatDirectViewDetector`>
    
        Detector for inter-satellites direct view (i.e. no masking by central body limb).
    
        As this detector needs two satellites, it embeds one :class:`~org.orekit.utils.PVCoordinatesProvider` for the secondary
        satellite and is registered as an event detector in the propagator of the primary satellite. The secondary satellite
        provider will therefore be driven by this detector (and hence by the propagator in which this detector is registered).
    
        In order to avoid infinite recursion, care must be taken to have the secondary satellite provider being *completely
        independent* from anything else. In particular, if the provider is a propagator, it should *not* be run together in a
        :class:`~org.orekit.propagation.PropagatorsParallelizer` with the propagator this detector is registered in. It is fine
        however to configure two separate propagators PsA and PsB with similar settings for the secondary satellite and one
        propagator Pm for the primary satellite and then use Psa in this detector registered within Pm while Pm and Psb are run
        in the context of a :class:`~org.orekit.propagation.PropagatorsParallelizer`.
    
        For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical
        propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally
        costly.
    
        The :code:`g` function of this detector is positive when satellites can see each other directly and negative when the
        central body limb is in between and blocks the direct view.
    
        This detector only checks masking by central body limb, it does not take into account satellites antenna patterns. If
        these patterns must be considered, then this detector can be
        :meth:`~org.orekit.propagation.events.BooleanDetector.andCombine` with the
        :meth:`~org.orekit.propagation.events.BooleanDetector.notCombine` of
        :class:`~org.orekit.propagation.events.FieldOfViewDetector`.
    
        Since:
            9.3
    """
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            The :code:`g` function of this detector is the difference between the minimum altitude of intermediate points along the
            line of sight between satellites and the
            :meth:`~org.orekit.propagation.events.InterSatDirectViewDetector.getSkimmingAltitude`. It is therefore positive when all
            intermediate points are above the skimming altitude, meaning satellites can see each other and it is negative when some
            intermediate points (which may be either endpoints) dive below this altitude, meaning satellites cannot see each other.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def withSkimmingAltitude(self, double: float) -> 'InterSatDirectViewDetector':
        """
            Setup the skimming altitude.
        
            The skimming altitude is the lowest altitude of the path between satellites at which events should be triggered. If set
            to 0.0, events are triggered exactly when the path passes just at central body limb.
        
            Parameters:
                newSkimmingAltitude (double): skimming altitude (m)
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.events.InterSatDirectViewDetector.getSkimmingAltitude`
        
        
        """
        ...

class LatitudeCrossingDetector(AbstractDetector['LatitudeCrossingDetector']):
    """
    public class LatitudeCrossingDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.LatitudeCrossingDetector`>
    
        Detector for geographic latitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed latitude with respect to a central body.
    
        Since:
            7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float): ...
    @typing.overload
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is the spacecraft latitude minus the fixed latitude to be crossed. It is positive if the spacecraft is
            northward and negative if it is southward with respect to the fixed latitude.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class LatitudeExtremumDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.LatitudeExtremumDetector`>
    
        Detector for geographic latitude extremum.
    
        This detector identifies when a spacecraft reaches its extremum latitudes with respect to a central body.
    
        Since:
            7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is the spacecraft latitude time derivative.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class LatitudeRangeCrossingDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.LatitudeRangeCrossingDetector`>
    
        Detector for geographic latitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed latitude range with respect to a central body.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is positive if the spacecraft latitude is inside the latitude range. It is positive if the spacecraft is
            northward to lower boundary range and southward to upper boundary range, with respect to the fixed latitude range.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class LongitudeCrossingDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.LongitudeCrossingDetector`>
    
        Detector for geographic longitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed longitude with respect to a central body.
    
        Since:
            7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float): ...
    @typing.overload
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is the longitude difference between the spacecraft and the fixed longitude to be crossed, with some sign
            tweaks to ensure continuity. These tweaks imply the :code:`increasing` flag in events detection becomes irrelevant here!
            As an example, the longitude of a prograde spacecraft will always increase, but this g function will increase and
            decrease so it will cross the zero value once per orbit, in increasing and decreasing directions on alternate orbits. If
            eastwards and westwards crossing have to be distinguished, the velocity direction has to be checked instead of looking
            at the :code:`increasing` flag.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class LongitudeExtremumDetector(AbstractDetector['LongitudeExtremumDetector']):
    """
    public class LongitudeExtremumDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.LongitudeExtremumDetector`>
    
        Detector for geographic longitude extremum.
    
        This detector identifies when a spacecraft reaches its extremum longitudes with respect to a central body.
    
        Since:
            7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is the spacecraft longitude time derivative.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class LongitudeRangeCrossingDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.LongitudeRangeCrossingDetector`>
    
        Detector for geographic longitude crossing.
    
        This detector identifies when a spacecraft crosses a fixed longitude range with respect to a central body.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float, double2: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is positive if the spacecraft longitude is inside the longitude range. The longitude value is reflected from
            [-PI, +PI] to [0, 2 PI] to ensure continuity.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class MagneticFieldDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.MagneticFieldDetector`>
    
        Detector for Earth magnetic field strength.
    
        The detector is based on the field intensity calculated at the satellite's latitude and longitude, either at sea level
        or at satellite altitude, depending on the value chosen for the :code:`atSeaLevel` indicator.
    
    
        It can detect flyovers of the South-Atlantic anomaly with a classically accepted limit value of 32,000 nT at sea level.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, fieldModel: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, fieldModel: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, boolean: bool, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, double: float, fieldModel: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, double: float, fieldModel: org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, boolean: bool): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The returned value is the difference between the field intensity at spacecraft location, taking :code:`atSeaLevel`
            switch into account, and the fixed threshold value.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                difference between the field intensity at spacecraft location and the fixed threshold value
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class NegateDetector(AbstractDetector['NegateDetector']):
    """
    public class NegateDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.NegateDetector`>
    
        An event detector that negates the sign on another event detector's
        :meth:`~org.orekit.propagation.events.EventDetector.g` function.
    """
    def __init__(self, eventDetector: EventDetector): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.EventDetector.g`
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
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
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Description copied from class: :meth:`~org.orekit.propagation.events.AbstractDetector.init`
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class NodeDetector(AbstractDetector['NodeDetector']):
    """
    public class NodeDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.NodeDetector`>
    
        Finder for node crossing events.
    
        This class finds equator crossing events (i.e. ascending or descending node crossing).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at descending node crossing and to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation at ascending node crossing. This can be changed by calling
        :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after construction.
    
        Beware that node detection will fail for almost equatorial orbits. If for example a node detector is used to trigger an
        :class:`~org.orekit.forces.maneuvers.ImpulseManeuver` and the maneuver turn the orbit plane to equator, then the
        detector may completely fail just after the maneuver has been performed! This is a real case that has been encountered
        during validation ...
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, double: float, orbit: org.orekit.orbits.Orbit, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, frame: org.orekit.frames.Frame): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function computes the Z position in the defined frame.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    public class ParameterDrivenDateIntervalDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector`>
    
        Detector for date intervals that may be offset thanks to parameter drivers.
    
        Two dual views can be used for date intervals: either start date/stop date or median date/duration.
        :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getStartDriver`/:meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getStopDriver`
        drivers and
        :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getMedianDriver`/:meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getDurationDriver`
        drivers work in pair. Both drivers in one pair can be selected and their changes will be propagated to the other pair,
        but attempting to select drivers in both pairs at the same time will trigger an exception. Changing the value of a
        driver that is not selected should be avoided as it leads to inconsistencies between the pairs.
        . Warning, startDate driver, stopDate driver, duration driver and medianDate driver must all have the same number of
        values to estimate (same number of span in valueSpanMap), that is is to say that the
        :meth:`~org.orekit.utils.ParameterDriver.addSpans` should be called with same arguments.
    
        Since:
            11.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    START_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` START_SUFFIX
    
        Default suffix for start driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    STOP_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` STOP_SUFFIX
    
        Default suffix for stop driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEDIAN_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEDIAN_SUFFIX
    
        Default suffix for median driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DURATION_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DURATION_SUFFIX
    
        Default suffix for duration driver.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function.
        
            The function is positive for dates within the interval defined by applying the parameter drivers shifts to reference
            dates, and negative for dates outside of this interval. Note that if Δt_start - Δt_stop is less than
            ref_stop.durationFrom(ref_start), then the interval degenerates to empty and the function never reaches positive values.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getDurationDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for duration.
        
            Note that the duration is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getStartDriver` start date or
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getStopDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` changed.
        
            Returns:
                driver for duration
        
        
        """
        ...
    def getMedianDriver(self) -> org.orekit.utils.DateDriver:
        """
            Get the driver for median date.
        
            Note that the median date is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getStartDriver` start date or
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getStopDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` changed.
        
            Returns:
                driver for median date
        
        
        """
        ...
    def getStartDriver(self) -> org.orekit.utils.DateDriver:
        """
            Get the driver for start date.
        
            Note that the start date is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getMedianDriver` or
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getDurationDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` and changed.
        
            Returns:
                driver for start date
        
        
        """
        ...
    def getStopDriver(self) -> org.orekit.utils.DateDriver:
        """
            Get the driver for stop date.
        
            Note that the stop date is automatically adjusted if either
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getMedianDriver` or
            :meth:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector.getDurationDriver` are
            :meth:`~org.orekit.utils.ParameterDriver.isSelected` changed.
        
            Returns:
                driver for stop date
        
        
        """
        ...

class PositionAngleDetector(AbstractDetector['PositionAngleDetector']):
    """
    public class PositionAngleDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.PositionAngleDetector`>
    
        Detector for in-orbit position angle.
    
        The detector is based on anomaly for :meth:`~org.orekit.orbits.OrbitType.KEPLERIAN` orbits, latitude argument for
        :meth:`~org.orekit.orbits.OrbitType.CIRCULAR` orbits, or longitude argument for
        :meth:`~org.orekit.orbits.OrbitType.EQUINOCTIAL` orbits. It does not support
        :meth:`~org.orekit.orbits.OrbitType.CARTESIAN` orbits. The angles can be either
        :meth:`~org.orekit.orbits.PositionAngleType.TRUE`, :meth:`~org.orekit.orbits.PositionAngleType.MEAN` or
        :meth:`~org.orekit.orbits.PositionAngleType.ECCENTRIC` angles.
    
        Since:
            7.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, double3: float): ...
    @typing.overload
    def __init__(self, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the detection function.
        
            The value is the angle difference between the spacecraft and the fixed angle to be crossed, with some sign tweaks to
            ensure continuity. These tweaks imply the :code:`increasing` flag in events detection becomes irrelevant here! As an
            example, the angle always increase in a Keplerian orbit, but this g function will increase and decrease so it will cross
            the zero value once per orbit, in increasing and decreasing directions on alternate orbits..
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

_PythonAbstractDetector__T = typing.TypeVar('_PythonAbstractDetector__T', bound=AbstractDetector)  # <T>
class PythonAbstractDetector(AbstractDetector[_PythonAbstractDetector__T], typing.Generic[_PythonAbstractDetector__T]):
    """
    public class PythonAbstractDetector<T extends :class:`~org.orekit.propagation.events.AbstractDetector`<T>> extends :class:`~org.orekit.propagation.events.AbstractDetector`<T>
    
        Common parts shared by several orbital events finders.
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, int: int, eventHandler: org.orekit.propagation.events.handlers.EventHandler): ...
    @typing.overload
    def __init__(self, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable], double: float, int: int, eventHandler: org.orekit.propagation.events.handlers.EventHandler): ...
    def create(self, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable], double: float, int: int, eventHandler: org.orekit.propagation.events.handlers.EventHandler) -> _PythonAbstractDetector__T:
        """
            Build a new instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.AbstractDetector.create` in
                class :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                newMaxCheck (:class:`~org.orekit.propagation.events.AdaptableInterval`): maximum checking interval (s)
                newThreshold (double): convergence threshold (s)
                newMaxIter (int): maximum number of iterations in the event time search
                newHandler (:class:`~org.orekit.propagation.events.handlers.EventHandler`): event handler to call at event occurrences
        
            Returns:
                a new instance of the appropriate sub-type
        
        
        """
        ...
    def finalize(self) -> None: ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

_PythonFieldAbstractDetector__D = typing.TypeVar('_PythonFieldAbstractDetector__D', bound=FieldAbstractDetector)  # <D>
_PythonFieldAbstractDetector__T = typing.TypeVar('_PythonFieldAbstractDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractDetector(FieldAbstractDetector[_PythonFieldAbstractDetector__D, _PythonFieldAbstractDetector__T], typing.Generic[_PythonFieldAbstractDetector__D, _PythonFieldAbstractDetector__T]):
    """
    public class PythonFieldAbstractDetector<D extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<D, T>, T extends :class:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.FieldAbstractDetector`<D, T>
    """
    def __init__(self, fieldAdaptableInterval: typing.Union[FieldAdaptableInterval[_PythonFieldAbstractDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], float]], t: _PythonFieldAbstractDetector__T, int: int, fieldEventHandler: org.orekit.propagation.events.handlers.FieldEventHandler[_PythonFieldAbstractDetector__T]): ...
    def create(self, fieldAdaptableInterval: typing.Union[FieldAdaptableInterval[_PythonFieldAbstractDetector__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], float]], t: _PythonFieldAbstractDetector__T, int: int, fieldEventHandler: org.orekit.propagation.events.handlers.FieldEventHandler[_PythonFieldAbstractDetector__T]) -> _PythonFieldAbstractDetector__D: ...
    def finalize(self) -> None: ...
    def g(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAbstractDetector__T]) -> _PythonFieldAbstractDetector__T: ...
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

class RelativeDistanceDetector(AbstractDetector['RelativeDistanceDetector']):
    """
    public class RelativeDistanceDetector extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.propagation.events.RelativeDistanceDetector`>
    
        Detector of specific value for the distance relative to another trajectory (using the Euclidean norm).
    
        The default implementation behavior is to
        :meth:`~org.orekit.propagation.events.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation. This can be changed by calling :meth:`~org.orekit.propagation.events.AbstractDetector.withHandler` after
        construction.
    
        As this detector needs two objects (moving relative to each other), it embeds one
        :class:`~org.orekit.utils.PVCoordinatesProvider` for the secondary object and is registered as an event detector in the
        propagator of the primary object. The secondary object :class:`~org.orekit.utils.PVCoordinatesProvider` will therefore
        be driven by this detector (and hence by the propagator in which this detector is registered).
    
        **In order to avoid infinite recursion, care must be taken to have the secondary object provider being *completely
        independent* from anything else. In particular, if the provider is a propagator, it should *not* be run together in a
        :class:`~org.orekit.propagation.PropagatorsParallelizer` with the propagator this detector is registered in. It is fine
        however to configure two separate propagators PsA and PsB with similar settings for the secondary object and one
        propagator Pm for the primary object and then use Psa in this detector registered within Pm while Pm and Psb are run in
        the context of a :class:`~org.orekit.propagation.PropagatorsParallelizer`.**
    
        For efficiency reason during the event search loop, it is recommended to have the secondary provider be an analytical
        propagator or an ephemeris. A numerical propagator as a secondary propagator works but is expected to be computationally
        costly.
    
        Since:
            12.1
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            The :code:`g` is positive when the relative distance is larger or equal than the threshold, non-positive otherwise.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events")``.

    AbstractDetector: typing.Type[AbstractDetector]
    AdaptableInterval: typing.Type[AdaptableInterval]
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
    ExtremumApproachDetector: typing.Type[ExtremumApproachDetector]
    FieldAbstractDetector: typing.Type[FieldAbstractDetector]
    FieldAdaptableInterval: typing.Type[FieldAdaptableInterval]
    FieldAdapterDetector: typing.Type[FieldAdapterDetector]
    FieldAltitudeDetector: typing.Type[FieldAltitudeDetector]
    FieldApsideDetector: typing.Type[FieldApsideDetector]
    FieldBetaAngleDetector: typing.Type[FieldBetaAngleDetector]
    FieldBooleanDetector: typing.Type[FieldBooleanDetector]
    FieldCylindricalShadowEclipseDetector: typing.Type[FieldCylindricalShadowEclipseDetector]
    FieldDateDetector: typing.Type[FieldDateDetector]
    FieldEclipseDetector: typing.Type[FieldEclipseDetector]
    FieldElevationDetector: typing.Type[FieldElevationDetector]
    FieldElevationExtremumDetector: typing.Type[FieldElevationExtremumDetector]
    FieldEnablingPredicate: typing.Type[FieldEnablingPredicate]
    FieldEventDetectionSettings: typing.Type[FieldEventDetectionSettings]
    FieldEventDetector: typing.Type[FieldEventDetector]
    FieldEventEnablingPredicateFilter: typing.Type[FieldEventEnablingPredicateFilter]
    FieldEventSlopeFilter: typing.Type[FieldEventSlopeFilter]
    FieldEventState: typing.Type[FieldEventState]
    FieldEventsLogger: typing.Type[FieldEventsLogger]
    FieldExtremumApproachDetector: typing.Type[FieldExtremumApproachDetector]
    FieldFunctionalDetector: typing.Type[FieldFunctionalDetector]
    FieldLatitudeCrossingDetector: typing.Type[FieldLatitudeCrossingDetector]
    FieldLatitudeRangeCrossingDetector: typing.Type[FieldLatitudeRangeCrossingDetector]
    FieldLongitudeCrossingDetector: typing.Type[FieldLongitudeCrossingDetector]
    FieldLongitudeRangeCrossingDetector: typing.Type[FieldLongitudeRangeCrossingDetector]
    FieldNegateDetector: typing.Type[FieldNegateDetector]
    FieldNodeDetector: typing.Type[FieldNodeDetector]
    FieldOfViewDetector: typing.Type[FieldOfViewDetector]
    FieldParameterDrivenDateIntervalDetector: typing.Type[FieldParameterDrivenDateIntervalDetector]
    FieldRelativeDistanceDetector: typing.Type[FieldRelativeDistanceDetector]
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
    PythonAdaptableInterval: typing.Type[PythonAdaptableInterval]
    PythonEnablingPredicate: typing.Type[PythonEnablingPredicate]
    PythonEventDetector: typing.Type[PythonEventDetector]
    PythonEventDetectorsProvider: typing.Type[PythonEventDetectorsProvider]
    PythonFieldAbstractDetector: typing.Type[PythonFieldAbstractDetector]
    PythonFieldAdaptableInterval: typing.Type[PythonFieldAdaptableInterval]
    PythonFieldEnablingPredicate: typing.Type[PythonFieldEnablingPredicate]
    PythonFieldEventDetector: typing.Type[PythonFieldEventDetector]
    RelativeDistanceDetector: typing.Type[RelativeDistanceDetector]
    VisibilityTrigger: typing.Type[VisibilityTrigger]
    class-use: org.orekit.propagation.events.class-use.__module_protocol__
    handlers: org.orekit.propagation.events.handlers.__module_protocol__
    intervals: org.orekit.propagation.events.intervals.__module_protocol__
