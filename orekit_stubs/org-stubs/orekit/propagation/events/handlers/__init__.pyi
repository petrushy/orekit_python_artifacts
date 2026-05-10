
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org
import org.hipparchus
import org.hipparchus.ode.events
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import typing



class EventHandler:
    """
    An interface defining how to handle events occurring during propagation.
    
    Since:
        6.1
    """
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event.
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        This method finalizes the event handler's job.
        
        The default implementation does nothing
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
            detector (EventDetector): event detector related to the event handler
        
        Since:
            12.2
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Parameters:
            initialState (SpacecraftState): initial state
            target (AbsoluteDate): target date for the propagation
            detector (EventDetector): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, detector: org.orekit.propagation.events.EventDetector, oldState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Reset the state prior to continue propagation.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the Action indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If the eventOccurred never returns the Action indicator, this function will never be called, and it is safe to simply return null.
        
        The default implementation simply return its argument.
        
        Parameters:
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            oldState (SpacecraftState): old state
        
        Returns:
            new state
        
        
        """
        ...

_FieldEventHandler__T = typing.TypeVar('_FieldEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventHandler(typing.Generic[_FieldEventHandler__T]):
    """
    An interface defining how to handle events occurring during propagation..
    
    Since:
        6.1
    """
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event.
        
        Parameters:
            s (FieldSpacecraftState<FieldEventHandler> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<FieldEventHandler> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T]) -> None:
        """
        This method finalize event handler at the end of a propagation.
        
        The default implementation does nothing
        
        Parameters:
            finalState (FieldSpacecraftState<FieldEventHandler> finalState): state at propagation end
            detector (FieldEventDetector<FieldEventHandler> detector): event detector related to the event handler
        
        Since:
            12.2
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], target: org.orekit.time.FieldAbsoluteDate[_FieldEventHandler__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T]) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Parameters:
            initialState (FieldSpacecraftState<FieldEventHandler> initialState): initial state
            target (FieldAbsoluteDate<FieldEventHandler> target): target date for the propagation
            detector (FieldEventDetector<FieldEventHandler> detector): event detector related to the event handler
        
        Since:
            11.1
        
        
        """
        ...
    def resetState(self, detector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T], oldState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T]:
        """
        Reset the state prior to continue propagation.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the Action indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If the eventOccurred never returns the Action indicator, this function will never be called, and it is safe to simply return null.
        
        The default implementation simply return its argument.
        
        Parameters:
            detector (FieldEventDetector<FieldEventHandler> detector): object with appropriate type that can be used in determining correct return state
            oldState (FieldSpacecraftState<FieldEventHandler> oldState): old state
        
        Returns:
            new state
        
        
        """
        ...

class ContinueOnEvent(EventHandler):
    """
    Event handler which will always return Action as a state.
    
    Since:
        6.1
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Specific implementation of the eventOccurred interface.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            under all circumstances
        
        
        """
        ...

class EventMultipleHandler(EventHandler):
    """
    Facade handlers that allows to use several handlers for one detector. Otherwise, the use of several detectors, each associated with one handler, that detect the same event can lead to non-deterministic behaviour. This handler manages several handlers. The action returned is based on a priority rule (see eventOccurred) : Action > Action > Action > Action > Action
    
    Since:
        10.3
    """
    def __init__(self):
        """
        Constructor with list initialisation.
        """
        ...
    def addHandler(self, handler: typing.Union[EventHandler, typing.Callable]) -> 'EventMultipleHandler':
        """
        Add one handler to the managed handlers list.
        
        Parameters:
            handler (EventHandler): handler associated with D detector
        
        Returns:
            this object
        
        
        """
        ...
    def addHandlers(self, *newHandlers: typing.Union[EventHandler, typing.Callable]) -> 'EventMultipleHandler':
        """
        Add several handlers to the managed handlers list.
        
        Parameters:
            newHandlers (EventHandler...): handlers associated with D detector
        
        Returns:
            this object
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event. The MultipleEventHandler class implies a different behaviour on event detections than with other handlers : Without the MultipleEventHandler, there is a total order on event occurrences. Handlers H1, H2... that are associated with different instances of AbstractDetector are successively called and Action from H1 can prevent H2 from happening if H1 returned Action. With the MultipleEventHandler class, when event E occurs, all methods eventOccurred of Handlers H1, H2... from MultiEventHandler attributes are called, then Action is decided.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        Description copied from interface: finish This method finalizes the event handler's job.
        
        The default implementation does nothing
        
        Specified by: finish in interface EventHandler
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
            detector (EventDetector): event detector related to the event handler
        
        
        """
        ...
    def getHandlers(self) -> java.util.List[EventHandler]:
        """
        Retrieve managed handlers list.
        
        Returns:
            list of handlers for event overrides
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        All handlers' init methods are successively called, the order method is the order in which handlers are added
        
        Specified by: init in interface EventHandler
        
        Parameters:
            initialState (SpacecraftState): initial state
            target (AbsoluteDate): target date for the propagation
            detector (EventDetector): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, detector: org.orekit.propagation.events.EventDetector, oldState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Reset the state prior to continue propagation.
        
        All handlers that return Action when calling eventOccurred are saved in resetStateHandlers. Their methods resetState are successively called. The order for calling resetState methods is the order in which handlers are added.
        
        Specified by: resetState in interface EventHandler
        
        Parameters:
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            oldState (SpacecraftState): old state
        
        Returns:
            new state
        
        
        """
        ...
    def setHandlers(self, newHandlers: java.util.List[typing.Union[EventHandler, typing.Callable]]) -> None:
        """
        Change handlers list with user input.
        
        Parameters:
            newHandlers (List<EventHandler> newHandlers): new handlers list associated with D detector
        
        
        """
        ...

_FieldContinueOnEvent__T = typing.TypeVar('_FieldContinueOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldContinueOnEvent(FieldEventHandler[_FieldContinueOnEvent__T], typing.Generic[_FieldContinueOnEvent__T]):
    """
    Event handler which will always return Action as a state.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldContinueOnEvent__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldContinueOnEvent__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Specific implementation of the eventOccurred interface.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldContinueOnEvent> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<FieldContinueOnEvent> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            under all circumstances
        
        
        """
        ...

_FieldRecallLastOccurrence__T = typing.TypeVar('_FieldRecallLastOccurrence__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRecallLastOccurrence(FieldEventHandler[_FieldRecallLastOccurrence__T], typing.Generic[_FieldRecallLastOccurrence__T]):
    """
    Event handler wrapping another, arbitrary one whilst remembering date of last detection. If never used, the cache is null. If used but nothing detected, it returns past infinity in case of forward propagation and future infinity otherwise.
    
    Since:
        12.1
    
    Also see:
        RecallLastOccurrence
    """
    def __init__(self, wrappedHandler: typing.Union[FieldEventHandler[_FieldRecallLastOccurrence__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], org.orekit.propagation.events.FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]):
        """
        Constructor.
        
        Parameters:
            wrappedHandler (FieldEventHandler<FieldRecallLastOccurrence> wrappedHandler): event handler to wrap
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldRecallLastOccurrence> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<FieldRecallLastOccurrence> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T]) -> None:
        """
        This method finalize event handler at the end of a propagation.
        
        The default implementation does nothing
        
        Specified by: finish in interface FieldEventHandler
        
        Parameters:
            finalState (FieldSpacecraftState<FieldRecallLastOccurrence> finalState): state at propagation end
            detector (FieldEventDetector<FieldRecallLastOccurrence> detector): event detector related to the event handler
        
        
        """
        ...
    def getLastOccurrence(self) -> org.orekit.time.FieldAbsoluteDate[_FieldRecallLastOccurrence__T]:
        """
        Getter for last occurrence.
        
        Returns:
            last date when underlying event was detected
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T], target: org.orekit.time.FieldAbsoluteDate[_FieldRecallLastOccurrence__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T]) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Specified by: init in interface FieldEventHandler
        
        Parameters:
            initialState (FieldSpacecraftState<FieldRecallLastOccurrence> initialState): initial state
            target (FieldAbsoluteDate<FieldRecallLastOccurrence> target): target date for the propagation
            detector (FieldEventDetector<FieldRecallLastOccurrence> detector): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, detector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T], oldState: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T]:
        """
        Reset the state prior to continue propagation.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the Action indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If the eventOccurred never returns the Action indicator, this function will never be called, and it is safe to simply return null.
        
        The default implementation simply return its argument.
        
        Specified by: resetState in interface FieldEventHandler
        
        Parameters:
            detector (FieldEventDetector<FieldRecallLastOccurrence> detector): object with appropriate type that can be used in determining correct return state
            oldState (FieldSpacecraftState<FieldRecallLastOccurrence> oldState): old state
        
        Returns:
            new state
        
        
        """
        ...

_FieldRecordAndContinue__Event__T = typing.TypeVar('_FieldRecordAndContinue__Event__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldRecordAndContinue__T = typing.TypeVar('_FieldRecordAndContinue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRecordAndContinue(FieldEventHandler[_FieldRecordAndContinue__T], typing.Generic[_FieldRecordAndContinue__T]):
    """
    Handler that will record every time an event occurs and always return Action.
    
    As this handler stores all observed events it may consume large amounts of memory depending on the duration of propagation and the frequency of events.
    
    Since:
        9.3
    
    Also see:
        RecordAndContinue
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, events: java.util.List['FieldRecordAndContinue.Event'[_FieldRecordAndContinue__T]]): ...
    def clear(self) -> None:
        """
        Clear all stored events.
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldRecordAndContinue__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldRecordAndContinue__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Description copied from interface: eventOccurred Handle an event.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldRecordAndContinue> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<FieldRecordAndContinue> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def getEvents(self) -> java.util.List['FieldRecordAndContinue.Event'[_FieldRecordAndContinue__T]]:
        """
        Get the events passed to this handler.
        
        Note the returned list of events is in the order the events were passed to this handler by calling eventOccurred. This may or may not be chronological order.
        
        Also not that this method returns a view of the internal collection used to store events and calling any of this handler's methods may modify both the underlying collection and the returned view. If a snapshot of the events up to a certain point is needed create a copy of the returned collection.
        
        Returns:
            the events observed by the handler in the order they were observed.
        
        
        """
        ...
    class Event(typing.Generic[_FieldRecordAndContinue__Event__T]):
        def getDetector(self) -> org.orekit.propagation.events.FieldEventDetector[_FieldRecordAndContinue__Event__T]: ...
        def getState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldRecordAndContinue__Event__T]: ...
        def isIncreasing(self) -> bool: ...
        def toString(self) -> str: ...

_FieldResetDerivativesOnEvent__T = typing.TypeVar('_FieldResetDerivativesOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldResetDerivativesOnEvent(FieldEventHandler[_FieldResetDerivativesOnEvent__T], typing.Generic[_FieldResetDerivativesOnEvent__T]):
    """
    Event handler which will always return Action as a state.
    
    Since:
        12.2
    """
    def __init__(self): ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldResetDerivativesOnEvent__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldResetDerivativesOnEvent__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Specific implementation of the eventOccurred interface.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldResetDerivativesOnEvent> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<FieldResetDerivativesOnEvent> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            under all circumstances
        
        
        """
        ...

_FieldStopOnDecreasing__T = typing.TypeVar('_FieldStopOnDecreasing__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnDecreasing(FieldEventHandler[_FieldStopOnDecreasing__T], typing.Generic[_FieldStopOnDecreasing__T]):
    """
    Handle a detection event and choose what to do next.
    
    KKhe implementation behavior is to Action propagation when ascending and to Action propagation when descending.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnDecreasing__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldStopOnDecreasing__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle a detection event and choose what to do next.
        
        KKhe implementation behavior is to Action propagation when ascending and to Action propagation when descending.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldStopOnDecreasing> s): the current state information : date, kinematics, attitude
            detector (FieldEventDetector<FieldStopOnDecreasing> detector): the detector object calling this method (not used in the evaluation)
            increasing (boolean): if true, the value of the switching function increases when times increases around event
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            or
            Action
        
        
        """
        ...

_FieldStopOnEvent__T = typing.TypeVar('_FieldStopOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnEvent(FieldEventHandler[_FieldStopOnEvent__T], typing.Generic[_FieldStopOnEvent__T]):
    """
    Event handler which will always return Action as a state.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnEvent__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldStopOnEvent__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Specific implementation of the eventOccurred interface.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldStopOnEvent> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<FieldStopOnEvent> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            under all circumstances
        
        
        """
        ...

_FieldStopOnIncreasing__T = typing.TypeVar('_FieldStopOnIncreasing__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnIncreasing(FieldEventHandler[_FieldStopOnIncreasing__T], typing.Generic[_FieldStopOnIncreasing__T]):
    """
    Handle a detection event and choose what to do next.
    
    The implementation behavior is to Action propagation when descending and to Action propagation when ascending.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnIncreasing__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldStopOnIncreasing__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle a detection event and choose what to do next.
        
        The implementation behavior is to Action propagation when descending and to Action propagation when ascending.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldStopOnIncreasing> s): the current state information : date, kinematics, attitude
            detector (FieldEventDetector<FieldStopOnIncreasing> detector): the detector object calling this method (not used in the evaluation)
            increasing (boolean): if true, the value of the switching function increases when times increases around event
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            or
            Action
        
        
        """
        ...

class PythonEventHandler(EventHandler):
    def __init__(self): ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Description copied from interface: eventOccurred Handle an event.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
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
    def finish(self, finalState: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        Description copied from interface: finish This method finalizes the event handler's job.
        
        The default implementation does nothing
        
        Specified by: finish in interface EventHandler
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
            detector (EventDetector): event detector related to the event handler
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        Description copied from interface: init Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Specified by: init in interface EventHandler
        
        Parameters:
            initialState (SpacecraftState): initial state
            target (AbsoluteDate): target date for the propagation
            detector (EventDetector): event detector related to the event handler
        
        
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
    def resetState(self, detector: org.orekit.propagation.events.EventDetector, oldState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Description copied from interface: resetState Reset the state prior to continue propagation.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the Action indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If the eventOccurred never returns the Action indicator, this function will never be called, and it is safe to simply return null.
        
        The default implementation simply return its argument.
        
        Specified by: resetState in interface EventHandler
        
        Parameters:
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            oldState (SpacecraftState): old state
        
        Returns:
            new state
        
        
        """
        ...

_PythonFieldEventHandler__KK = typing.TypeVar('_PythonFieldEventHandler__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_PythonFieldEventHandler__T = typing.TypeVar('_PythonFieldEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEventHandler(FieldEventHandler[_PythonFieldEventHandler__T], typing.Generic[_PythonFieldEventHandler__KK, _PythonFieldEventHandler__T]):
    def __init__(self): ...
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], detector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<PythonFieldEventHandler> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<PythonFieldEventHandler> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
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
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], detector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T]) -> None:
        """
        This method finalize event handler at the end of a propagation.
        
        The default implementation does nothing
        
        Specified by: finish in interface FieldEventHandler
        
        Parameters:
            finalState (FieldSpacecraftState<PythonFieldEventHandler> finalState): state at propagation end
            detector (FieldEventDetector<PythonFieldEventHandler> detector): event detector related to the event handler
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], target: org.orekit.time.FieldAbsoluteDate[_PythonFieldEventHandler__T], detector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T]) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Specified by: init in interface FieldEventHandler
        
        Parameters:
            initialState (FieldSpacecraftState<PythonFieldEventHandler> initialState): initial state
            target (FieldAbsoluteDate<PythonFieldEventHandler> target): target date for the propagation
            detector (FieldEventDetector<PythonFieldEventHandler> detector): event detector related to the event handler
        
        
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
    def resetState(self, detector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T], oldState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T]:
        """
        Reset the state prior to continue propagation.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the Action indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If the eventOccurred never returns the Action indicator, this function will never be called, and it is safe to simply return null.
        
        The default implementation simply return its argument.
        
        Specified by: resetState in interface FieldEventHandler
        
        Parameters:
            detector (FieldEventDetector<PythonFieldEventHandler> detector): object with appropriate type that can be used in determining correct return state
            oldState (FieldSpacecraftState<PythonFieldEventHandler> oldState): old state
        
        Returns:
            new state
        
        
        """
        ...

class RecallLastOccurrence(EventHandler):
    """
    Event handler wrapping another, arbitrary one whilst remembering date of last detection. If never used, the cache is null. If used but nothing detected, it returns past infinity in case of forward propagation and future infinity otherwise.
    
    Since:
        12.1
    
    Also see:
        RecordAndContinue
    """
    def __init__(self, wrappedHandler: typing.Union[EventHandler, typing.Callable]):
        """
        Constructor.
        
        Parameters:
            wrappedHandler (EventHandler): event handler to wrap
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        This method finalizes the event handler's job.
        
        The default implementation does nothing
        
        Specified by: finish in interface EventHandler
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
            detector (EventDetector): event detector related to the event handler
        
        
        """
        ...
    def getLastOccurrence(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for last occurrence.
        
        Returns:
            last date when underlying event was detected
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        Initialize event handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Specified by: init in interface EventHandler
        
        Parameters:
            initialState (SpacecraftState): initial state
            target (AbsoluteDate): target date for the propagation
            detector (EventDetector): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, detector: org.orekit.propagation.events.EventDetector, oldState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Reset the state prior to continue propagation.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the Action indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If the eventOccurred never returns the Action indicator, this function will never be called, and it is safe to simply return null.
        
        The default implementation simply return its argument.
        
        Specified by: resetState in interface EventHandler
        
        Parameters:
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            oldState (SpacecraftState): old state
        
        Returns:
            new state
        
        
        """
        ...

class RecordAndContinue(EventHandler):
    """
    Handler that will record every time an event occurs and always return Action.
    
    As this handler stores all observed events it may consume large amounts of memory depending on the duration of propagation and the frequency of events.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, events: java.util.List['RecordAndContinue.Event']): ...
    def clear(self) -> None:
        """
        Clear all stored events.
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Description copied from interface: eventOccurred Handle an event.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def getEvents(self) -> java.util.List['RecordAndContinue.Event']:
        """
        Get the events passed to this handler.
        
        Note the returned list of events is in the order the events were passed to this handler by calling eventOccurred. This may or may not be chronological order.
        
        Also not that this method returns a view of the internal collection used to store events and calling any of this handler's methods may modify both the underlying collection and the returned view. If a snapshot of the events up to a certain point is needed create a copy of the returned collection.
        
        Returns:
            the events observed by the handler in the order they were observed.
        
        
        """
        ...
    class Event:
        def getDetector(self) -> org.orekit.propagation.events.EventDetector: ...
        def getState(self) -> org.orekit.propagation.SpacecraftState: ...
        def isIncreasing(self) -> bool: ...
        def toString(self) -> str: ...

class ResetDerivativesOnEvent(EventHandler):
    """
    Event handler which will always return Action as a state.
    
    Since:
        12.2
    """
    def __init__(self): ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Specific implementation of the eventOccurred interface.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            under all circumstances
        
        
        """
        ...

class StopOnDecreasing(EventHandler):
    """
    Handle a detection event and choose what to do next.
    
    The implementation behavior is to Action propagation when ascending and to Action propagation when descending.
    
    Since:
        6.1
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle a detection event and choose what to do next.
        
        The implementation behavior is to Action propagation when ascending and to Action propagation when descending.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): the current state information : date, kinematics, attitude
            detector (EventDetector): the detector object calling this method (not used in the evaluation)
            increasing (boolean): if true, the value of the switching function increases when times increases around event
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            or
            Action
        
        
        """
        ...

class StopOnEvent(EventHandler):
    """
    Event handler which will always return Action as a state.
    
    Since:
        6.1
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Specific implementation of the eventOccurred interface.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            under all circumstances
        
        
        """
        ...

class StopOnIncreasing(EventHandler):
    """
    Handle a detection event and choose what to do next.
    
    The implementation behavior is to Action propagation when descending and to Action propagation when ascending.
    
    Since:
        6.1
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle a detection event and choose what to do next.
        
        The implementation behavior is to Action propagation when descending and to Action propagation when ascending.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): the current state information : date, kinematics, attitude
            detector (EventDetector): the detector object calling this method (not used in the evaluation)
            increasing (boolean): if true, the value of the switching function increases when times increases around event
        
        Returns:
            
            meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            or
            Action
        
        
        """
        ...

class CountAndContinue(org.orekit.propagation.events.handlers.CountingHandler):
    """
    Event handler counting event occurrences and always returning Action.
    
    Since:
        13.0
    
    Also see:
        CountingHandler
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, startingCount: int): ...

class CountingHandler(org.orekit.propagation.events.handlers.AbstractGenericCountingHandler, EventHandler):
    """
    Abstract class for handlers counting event occurrences. The Action can be modified according to the count.
    
    Since:
        13.0
    """
    def eventOccurred(self, s: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event.
        
        Specified by: eventOccurred in interface EventHandler
        
        Parameters:
            s (SpacecraftState): SpaceCraft state to be used in the evaluation
            detector (EventDetector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...

_FieldCountAndContinue__T = typing.TypeVar('_FieldCountAndContinue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCountAndContinue(org.orekit.propagation.events.handlers.FieldCountingHandler[_FieldCountAndContinue__T], typing.Generic[_FieldCountAndContinue__T]):
    """
    Event handler counting event occurrences and always returning Action.
    
    Since:
        13.0
    """
    def __init__(self, startingCount: int):
        """
        Constructor.
        
        Parameters:
            startingCount (int): value to initialize count
        
        
        """
        ...

_FieldCountingHandler__T = typing.TypeVar('_FieldCountingHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCountingHandler(org.orekit.propagation.events.handlers.AbstractGenericCountingHandler, FieldEventHandler[_FieldCountingHandler__T], typing.Generic[_FieldCountingHandler__T]):
    """
    Abstract class for handlers counting event occurrences. The Action can be modified according to the count.
    
    Since:
        13.0
    """
    def eventOccurred(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldCountingHandler__T], detector: org.orekit.propagation.events.FieldEventDetector[_FieldCountingHandler__T], increasing: bool) -> org.hipparchus.ode.events.Action:
        """
        Handle an event.
        
        Specified by: eventOccurred in interface FieldEventHandler
        
        Parameters:
            s (FieldSpacecraftState<FieldCountingHandler> s): SpaceCraft state to be used in the evaluation
            detector (FieldEventDetector<FieldCountingHandler> detector): object with appropriate type that can be used in determining correct return state
            increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
        Returns:
            the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...

class PythonAbstractGenericCountingHandler(org.orekit.propagation.events.handlers.AbstractGenericCountingHandler):
    def __init__(self, startingCount: int, action: org.hipparchus.ode.events.Action):
        """
        Constructor.
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
    def getAction(self) -> org.hipparchus.ode.events.Action:
        """
        Getter for action.
        
        Returns:
            action
        
        
        """
        ...
    def getCount(self) -> int:
        """
        Getter for count.
        
        Returns:
            count
        
        
        """
        ...
    def increment(self) -> None:
        """
        Increment count.
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
    def reset(self) -> None:
        """
        Reset count.
        """
        ...
    def setAction(self, action: org.hipparchus.ode.events.Action) -> None:
        """
        Setter for action.
        
        Parameters:
            action (Action): new action
        
        
        """
        ...

class PythonCountingHandler(CountingHandler):
    def __init__(self, startingCount: int, action: org.hipparchus.ode.events.Action):
        """
        Constructor.
        """
        ...
    def doesCount(self, state: org.orekit.propagation.SpacecraftState, detector: org.orekit.propagation.events.EventDetector, increasing: bool) -> bool:
        """
        Abstract method to implement in Python.
        
        Specified by: doesCount in class CountingHandler
        
        Parameters:
            state (SpacecraftState): state at detection
            detector (EventDetector): detector
            increasing (boolean): flag on direction of event function
        
        Returns:
            flag on counting
        
        
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

class PythonFieldCountingHandler(FieldCountingHandler):
    def __init__(self, startingCount: int, action: org.hipparchus.ode.events.Action):
        """
        Constructor.
        """
        ...
    def doesCount(self, state: org.orekit.propagation.FieldSpacecraftState, detector: org.orekit.propagation.events.FieldEventDetector, increasing: bool) -> bool:
        """
        Method returning true if and only if the count needs to be incremented.
        
        Specified by: doesCount in class FieldCountingHandler
        
        Parameters:
            state (FieldSpacecraftState): state at detection
            detector (FieldEventDetector): detector
            increasing (boolean): flag on direction of event function
        
        Returns:
            flag on counting
        
        
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

class AbstractGenericCountingHandler: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events.handlers")``.

    AbstractGenericCountingHandler: typing.Type[AbstractGenericCountingHandler]
    ContinueOnEvent: typing.Type[ContinueOnEvent]
    CountAndContinue: typing.Type[CountAndContinue]
    CountingHandler: typing.Type[CountingHandler]
    EventHandler: typing.Type[EventHandler]
    EventMultipleHandler: typing.Type[EventMultipleHandler]
    FieldContinueOnEvent: typing.Type[FieldContinueOnEvent]
    FieldCountAndContinue: typing.Type[FieldCountAndContinue]
    FieldCountingHandler: typing.Type[FieldCountingHandler]
    FieldEventHandler: typing.Type[FieldEventHandler]
    FieldRecallLastOccurrence: typing.Type[FieldRecallLastOccurrence]
    FieldRecordAndContinue: typing.Type[FieldRecordAndContinue]
    FieldResetDerivativesOnEvent: typing.Type[FieldResetDerivativesOnEvent]
    FieldStopOnDecreasing: typing.Type[FieldStopOnDecreasing]
    FieldStopOnEvent: typing.Type[FieldStopOnEvent]
    FieldStopOnIncreasing: typing.Type[FieldStopOnIncreasing]
    PythonAbstractGenericCountingHandler: typing.Type[PythonAbstractGenericCountingHandler]
    PythonCountingHandler: typing.Type[PythonCountingHandler]
    PythonEventHandler: typing.Type[PythonEventHandler]
    PythonFieldCountingHandler: typing.Type[PythonFieldCountingHandler]
    PythonFieldEventHandler: typing.Type[PythonFieldEventHandler]
    RecallLastOccurrence: typing.Type[RecallLastOccurrence]
    RecordAndContinue: typing.Type[RecordAndContinue]
    ResetDerivativesOnEvent: typing.Type[ResetDerivativesOnEvent]
    StopOnDecreasing: typing.Type[StopOnDecreasing]
    StopOnEvent: typing.Type[StopOnEvent]
    StopOnIncreasing: typing.Type[StopOnIncreasing]
