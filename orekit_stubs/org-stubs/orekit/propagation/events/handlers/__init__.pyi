import java.util
import org.hipparchus
import org.hipparchus.ode.events
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.events.handlers.class-use
import org.orekit.time
import typing



class EventHandler:
    """
    public interface EventHandler
    
        An interface defining how to handle events occurring during propagation.
    
        Since:
            6.1
    """
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Handle an event.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            This method finalizes the event handler's job.
        
            The default implementation does nothing
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
            Since:
                12.2
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                target (:class:`~org.orekit.time.AbsoluteDate`): target date for the propagation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, eventDetector: org.orekit.propagation.events.EventDetector, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset the state prior to continue propagation.
        
            This method is called after the step handler has returned and before the next step is started, but only when
            :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` has itself returned the
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing
            step. If the :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` never returns the
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            indicator, this function will never be called, and it is safe to simply return null.
        
            The default implementation simply return its argument.
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                oldState (:class:`~org.orekit.propagation.SpacecraftState`): old state
        
            Returns:
                new state
        
        
        """
        ...

_FieldEventHandler__T = typing.TypeVar('_FieldEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventHandler(typing.Generic[_FieldEventHandler__T]):
    """
    public interface FieldEventHandler<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        An interface defining how to handle events occurring during propagation..
    
        Since:
            6.1
    """
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEventHandler__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T]) -> None: ...
    def resetState(self, fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldEventHandler__T], fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T]: ...

class ContinueOnEvent(EventHandler):
    """
    public class ContinueOnEvent extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Event handler which will always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        as a state.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Specific implementation of the eventOccurred interface.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                
                meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
                under all circumstances
        
        
        """
        ...

class EventMultipleHandler(EventHandler):
    """
    public class EventMultipleHandler extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Facade handlers that allows to use several handlers for one detector. Otherwise, the use of several detectors, each
        associated with one handler, that detect the same event can lead to non-deterministic behaviour. This handler manages
        several handlers. The action returned is based on a priority rule (see
        :meth:`~org.orekit.propagation.events.handlers.EventMultipleHandler.eventOccurred`) :
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        >
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        >
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        >
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        >
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
    
        Since:
            10.3
    """
    def __init__(self): ...
    def addHandler(self, eventHandler: EventHandler) -> 'EventMultipleHandler':
        """
            Add one handler to the managed handlers list.
        
            Parameters:
                handler (:class:`~org.orekit.propagation.events.handlers.EventHandler`): handler associated with D detector
        
            Returns:
                this object
        
        
        """
        ...
    def addHandlers(self, eventHandlerArray: typing.List[EventHandler]) -> 'EventMultipleHandler':
        """
            Add several handlers to the managed handlers list.
        
            Parameters:
                newHandlers (:class:`~org.orekit.propagation.events.handlers.EventHandler`...): handlers associated with D detector
        
            Returns:
                this object
        
        
        """
        ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Handle an event. The MultipleEventHandler class implies a different behaviour on event detections than with other
            handlers : Without the MultipleEventHandler, there is a total order on event occurrences. Handlers H1, H2, ... that are
            associated with different instances of :class:`~org.orekit.propagation.events.AbstractDetector` are successively called
            and Action from H1 can prevent H2 from happening if H1 returned
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`.
            With the MultipleEventHandler class, when event E occurs, all methods eventOccurred of Handlers H1, H2... from
            MultiEventHandler attributes are called, then Action is decided.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.handlers.EventHandler.finish`
            This method finalizes the event handler's job.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.finish` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
        
        """
        ...
    def getHandlers(self) -> java.util.List[EventHandler]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            All handlers' init methods are successively called, the order method is the order in which handlers are added
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.init` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                target (:class:`~org.orekit.time.AbsoluteDate`): target date for the propagation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, eventDetector: org.orekit.propagation.events.EventDetector, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset the state prior to continue propagation.
        
            All handlers that return
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            when calling :meth:`~org.orekit.propagation.events.handlers.EventMultipleHandler.eventOccurred` are saved in
            resetStateHandlers. Their methods resetState are successively called. The order for calling resetState methods is the
            order in which handlers are added.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                oldState (:class:`~org.orekit.propagation.SpacecraftState`): old state
        
            Returns:
                new state
        
        
        """
        ...
    def setHandlers(self, list: java.util.List[EventHandler]) -> None: ...

_FieldContinueOnEvent__T = typing.TypeVar('_FieldContinueOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldContinueOnEvent(FieldEventHandler[_FieldContinueOnEvent__T], typing.Generic[_FieldContinueOnEvent__T]):
    """
    public class FieldContinueOnEvent<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    
        Event handler which will always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        as a state.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldContinueOnEvent__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldContinueOnEvent__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...

_FieldRecallLastOccurrence__T = typing.TypeVar('_FieldRecallLastOccurrence__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRecallLastOccurrence(FieldEventHandler[_FieldRecallLastOccurrence__T], typing.Generic[_FieldRecallLastOccurrence__T]):
    """
    public class FieldRecallLastOccurrence<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    
        Event handler wrapping another, arbitrary one whilst remembering date of last detection. If never used, the cache is
        null. If used but nothing detected, it returns past infinity in case of forward propagation and future infinity
        otherwise.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.events.handlers.RecallLastOccurrence`
    """
    def __init__(self, fieldEventHandler: FieldEventHandler[_FieldRecallLastOccurrence__T]): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T]) -> None: ...
    def getLastOccurrence(self) -> org.orekit.time.FieldAbsoluteDate[_FieldRecallLastOccurrence__T]: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldRecallLastOccurrence__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T]) -> None: ...
    def resetState(self, fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldRecallLastOccurrence__T], fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldRecallLastOccurrence__T]: ...

_FieldRecordAndContinue__Event__T = typing.TypeVar('_FieldRecordAndContinue__Event__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldRecordAndContinue__T = typing.TypeVar('_FieldRecordAndContinue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRecordAndContinue(FieldEventHandler[_FieldRecordAndContinue__T], typing.Generic[_FieldRecordAndContinue__T]):
    """
    public class FieldRecordAndContinue<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    
        Handler that will record every time an event occurs and always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`.
    
        As this handler stores all observed events it may consume large amounts of memory depending on the duration of
        propagation and the frequency of events.
    
        Since:
            9.3
    
        Also see:
            :class:`~org.orekit.propagation.events.handlers.RecordAndContinue`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List['FieldRecordAndContinue.Event'[_FieldRecordAndContinue__T]]): ...
    def clear(self) -> None:
        """
            Clear all stored events.
        
        """
        ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldRecordAndContinue__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldRecordAndContinue__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...
    def getEvents(self) -> java.util.List['FieldRecordAndContinue.Event'[_FieldRecordAndContinue__T]]: ...
    class Event(typing.Generic[_FieldRecordAndContinue__Event__T]):
        def getDetector(self) -> org.orekit.propagation.events.FieldEventDetector[_FieldRecordAndContinue__Event__T]: ...
        def getState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldRecordAndContinue__Event__T]: ...
        def isIncreasing(self) -> bool: ...
        def toString(self) -> str: ...

_FieldResetDerivativesOnEvent__T = typing.TypeVar('_FieldResetDerivativesOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldResetDerivativesOnEvent(FieldEventHandler[_FieldResetDerivativesOnEvent__T], typing.Generic[_FieldResetDerivativesOnEvent__T]):
    """
    public class FieldResetDerivativesOnEvent<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    
        Event handler which will always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        as a state.
    
        Since:
            12.2
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldResetDerivativesOnEvent__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldResetDerivativesOnEvent__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...

_FieldStopOnDecreasing__T = typing.TypeVar('_FieldStopOnDecreasing__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnDecreasing(FieldEventHandler[_FieldStopOnDecreasing__T], typing.Generic[_FieldStopOnDecreasing__T]):
    """
    public class FieldStopOnDecreasing<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    
        Handle a detection event and choose what to do next.
    
        KKhe implementation behavior is to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when ascending and to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when descending.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnDecreasing__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldStopOnDecreasing__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...

_FieldStopOnEvent__T = typing.TypeVar('_FieldStopOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnEvent(FieldEventHandler[_FieldStopOnEvent__T], typing.Generic[_FieldStopOnEvent__T]):
    """
    public class FieldStopOnEvent<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    
        Event handler which will always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        as a state.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnEvent__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldStopOnEvent__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...

_FieldStopOnIncreasing__T = typing.TypeVar('_FieldStopOnIncreasing__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnIncreasing(FieldEventHandler[_FieldStopOnIncreasing__T], typing.Generic[_FieldStopOnIncreasing__T]):
    """
    public class FieldStopOnIncreasing<T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    
        Handle a detection event and choose what to do next.
    
        The implementation behavior is to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when descending and to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when ascending.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnIncreasing__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_FieldStopOnIncreasing__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...

class PythonEventHandler(EventHandler):
    """
    public class PythonEventHandler extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`
            Handle an event.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finalize(self) -> None: ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.handlers.EventHandler.finish`
            This method finalizes the event handler's job.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.finish` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.handlers.EventHandler.init`
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.init` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                target (:class:`~org.orekit.time.AbsoluteDate`): target date for the propagation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
        
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
    def resetState(self, eventDetector: org.orekit.propagation.events.EventDetector, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState`
            Reset the state prior to continue propagation.
        
            This method is called after the step handler has returned and before the next step is started, but only when
            :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` has itself returned the
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing
            step. If the :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` never returns the
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            indicator, this function will never be called, and it is safe to simply return null.
        
            The default implementation simply return its argument.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                oldState (:class:`~org.orekit.propagation.SpacecraftState`): old state
        
            Returns:
                new state
        
        
        """
        ...

_PythonFieldEventHandler__KK = typing.TypeVar('_PythonFieldEventHandler__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_PythonFieldEventHandler__T = typing.TypeVar('_PythonFieldEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEventHandler(FieldEventHandler[_PythonFieldEventHandler__T], typing.Generic[_PythonFieldEventHandler__KK, _PythonFieldEventHandler__T]):
    """
    public class PythonFieldEventHandler<KK extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>, T extends :class:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T>
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T], boolean: bool) -> org.hipparchus.ode.events.Action: ...
    def finalize(self) -> None: ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldEventHandler__T], fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T]) -> None: ...
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
    def resetState(self, fieldEventDetector: org.orekit.propagation.events.FieldEventDetector[_PythonFieldEventHandler__T], fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T]: ...

class RecallLastOccurrence(EventHandler):
    """
    public class RecallLastOccurrence extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Event handler wrapping another, arbitrary one whilst remembering date of last detection. If never used, the cache is
        null. If used but nothing detected, it returns past infinity in case of forward propagation and future infinity
        otherwise.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.events.handlers.RecordAndContinue`
    """
    def __init__(self, eventHandler: EventHandler): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Handle an event.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            This method finalizes the event handler's job.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.finish` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
        
        """
        ...
    def getLastOccurrence(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for last occurrence.
        
            Returns:
                last date when underlying event was detected
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.init` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                target (:class:`~org.orekit.time.AbsoluteDate`): target date for the propagation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, eventDetector: org.orekit.propagation.events.EventDetector, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset the state prior to continue propagation.
        
            This method is called after the step handler has returned and before the next step is started, but only when
            :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` has itself returned the
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            indicator. It allows the user to reset the state for the next step, without perturbing the step handler of the finishing
            step. If the :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` never returns the
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            indicator, this function will never be called, and it is safe to simply return null.
        
            The default implementation simply return its argument.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                oldState (:class:`~org.orekit.propagation.SpacecraftState`): old state
        
            Returns:
                new state
        
        
        """
        ...

class RecordAndContinue(EventHandler):
    """
    public class RecordAndContinue extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Handler that will record every time an event occurs and always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`.
    
        As this handler stores all observed events it may consume large amounts of memory depending on the duration of
        propagation and the frequency of events.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List['RecordAndContinue.Event']): ...
    def clear(self) -> None:
        """
            Clear all stored events.
        
        """
        ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`
            Handle an event.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def getEvents(self) -> java.util.List['RecordAndContinue.Event']: ...
    class Event:
        def getDetector(self) -> org.orekit.propagation.events.EventDetector: ...
        def getState(self) -> org.orekit.propagation.SpacecraftState: ...
        def isIncreasing(self) -> bool: ...
        def toString(self) -> str: ...

class ResetDerivativesOnEvent(EventHandler):
    """
    public class ResetDerivativesOnEvent extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Event handler which will always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        as a state.
    
        Since:
            12.2
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Specific implementation of the eventOccurred interface.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                
                meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
                under all circumstances
        
        
        """
        ...

class StopOnDecreasing(EventHandler):
    """
    public class StopOnDecreasing extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Handle a detection event and choose what to do next.
    
        The implementation behavior is to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when ascending and to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when descending.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Handle a detection event and choose what to do next.
        
            The implementation behavior is to
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            propagation when ascending and to
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            propagation when descending.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information : date, kinematics, attitude
                detector (:class:`~org.orekit.propagation.events.EventDetector`): the detector object calling this method (not used in the evaluation)
                increasing (boolean): if true, the value of the switching function increases when times increases around event
        
            Returns:
                
                meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
                or
                :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        
        
        """
        ...

class StopOnEvent(EventHandler):
    """
    public class StopOnEvent extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Event handler which will always return
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        as a state.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Specific implementation of the eventOccurred interface.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                
                meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
                under all circumstances
        
        
        """
        ...

class StopOnIncreasing(EventHandler):
    """
    public class StopOnIncreasing extends :class:`~org.orekit.propagation.events.handlers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.handlers.EventHandler`
    
        Handle a detection event and choose what to do next.
    
        The implementation behavior is to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when descending and to
        :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        propagation when ascending.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Handle a detection event and choose what to do next.
        
            The implementation behavior is to
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            propagation when descending and to
            :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
            propagation when ascending.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information : date, kinematics, attitude
                detector (:class:`~org.orekit.propagation.events.EventDetector`): the detector object calling this method (not used in the evaluation)
                increasing (boolean): if true, the value of the switching function increases when times increases around event
        
            Returns:
                
                meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
                or
                :meth:`~org.orekit.propagation.events.handlers.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events.handlers")``.

    ContinueOnEvent: typing.Type[ContinueOnEvent]
    EventHandler: typing.Type[EventHandler]
    EventMultipleHandler: typing.Type[EventMultipleHandler]
    FieldContinueOnEvent: typing.Type[FieldContinueOnEvent]
    FieldEventHandler: typing.Type[FieldEventHandler]
    FieldRecallLastOccurrence: typing.Type[FieldRecallLastOccurrence]
    FieldRecordAndContinue: typing.Type[FieldRecordAndContinue]
    FieldResetDerivativesOnEvent: typing.Type[FieldResetDerivativesOnEvent]
    FieldStopOnDecreasing: typing.Type[FieldStopOnDecreasing]
    FieldStopOnEvent: typing.Type[FieldStopOnEvent]
    FieldStopOnIncreasing: typing.Type[FieldStopOnIncreasing]
    PythonEventHandler: typing.Type[PythonEventHandler]
    PythonFieldEventHandler: typing.Type[PythonFieldEventHandler]
    RecallLastOccurrence: typing.Type[RecallLastOccurrence]
    RecordAndContinue: typing.Type[RecordAndContinue]
    ResetDerivativesOnEvent: typing.Type[ResetDerivativesOnEvent]
    StopOnDecreasing: typing.Type[StopOnDecreasing]
    StopOnEvent: typing.Type[StopOnEvent]
    StopOnIncreasing: typing.Type[StopOnIncreasing]
    class-use: org.orekit.propagation.events.handlers.class-use.__module_protocol__
