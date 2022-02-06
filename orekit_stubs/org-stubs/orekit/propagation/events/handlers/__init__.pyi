import java.util
import org.hipparchus
import org.hipparchus.ode.events
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import typing



_EventHandler__T = typing.TypeVar('_EventHandler__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class EventHandler(typing.Generic[_EventHandler__T]):
    """
    public interface EventHandler<T extends :class:`~org.orekit.propagation.events.EventDetector`>
    
        An interface defining how to override event handling behavior in the standard propagator eventing classes without
        requiring subclassing. In cases where one wishes to use anonymous classes rather than explicit subclassing this allows
        for a more direct way to override the behavior. Event classes have to specifically support this capability.
    
        Since:
            6.1
    """
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, t: _EventHandler__T, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            eventOccurred method mirrors the same interface method as in :class:`~org.orekit.propagation.events.EventDetector` and
            its subclasses, but with an additional parameter that allows the calling method to pass in an object from the detector
            which would have potential additional data to allow the implementing class to determine the correct return state.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.handlers.EventHandler`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, t: _EventHandler__T) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                target (:class:`~org.orekit.time.AbsoluteDate`): target date for the propagation
                detector (:class:`~org.orekit.propagation.events.handlers.EventHandler`): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, t: _EventHandler__T, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset the state prior to continue propagation.
        
            This method is called after the step handler has returned and before the next step is started, but only when
            :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` has itself returned the null indicator. It
            allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If the
            :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` never returns the null indicator, this
            function will never be called, and it is safe to simply return null.
        
            The default implementation simply return its argument.
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.handlers.EventHandler`): object with appropriate type that can be used in determining correct return state
                oldState (:class:`~org.orekit.propagation.SpacecraftState`): old state
        
            Returns:
                new state
        
        
        """
        ...

_FieldEventHandler__KK = typing.TypeVar('_FieldEventHandler__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_FieldEventHandler__T = typing.TypeVar('_FieldEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventHandler(typing.Generic[_FieldEventHandler__KK, _FieldEventHandler__T]):
    """
    public interface FieldEventHandler<KK extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>,T extends CalculusFieldElement<T>>
    
        An interface defining how to override event handling behavior in the standard propagator eventing classes without
        requiring subclassing. In cases where one wishes to use anonymous classes rather than explicit subclassing this allows
        for a more direct way to override the behavior. Event classes have to specifically support this capability.
    
        Since:
            6.1
    """
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], kK: _FieldEventHandler__KK, boolean: bool) -> org.hipparchus.ode.events.Action: ...
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEventHandler__T]) -> None: ...
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEventHandler__T], kK: _FieldEventHandler__KK) -> None: ...
    def resetState(self, kK: _FieldEventHandler__KK, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldEventHandler__T]: ...

_ContinueOnEvent__T = typing.TypeVar('_ContinueOnEvent__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class ContinueOnEvent(EventHandler[_ContinueOnEvent__T], typing.Generic[_ContinueOnEvent__T]):
    """
    public class ContinueOnEvent<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends Object implements :class:`~org.orekit.propagation.events.handlers.EventHandler`<T>
    
        Event handler which will always return null as a state.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, t: _ContinueOnEvent__T, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Specific implementation of the eventOccurred interface.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.handlers.ContinueOnEvent`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                null under all circumstances
        
        
        """
        ...

_EventMultipleHandler__D = typing.TypeVar('_EventMultipleHandler__D', bound=org.orekit.propagation.events.EventDetector)  # <D>
class EventMultipleHandler(EventHandler[_EventMultipleHandler__D], typing.Generic[_EventMultipleHandler__D]):
    """
    public class EventMultipleHandler<D extends :class:`~org.orekit.propagation.events.EventDetector`> extends Object implements :class:`~org.orekit.propagation.events.handlers.EventHandler`<D>
    
        Facade handlers that allows to use several handlers for one detector. Otherwise, the use of several detectors, each
        associated with one handler, that detect the same event can lead to non-deterministic behaviour. This handler manages
        several handlers. The action returned is based on a priority rule (see
        :meth:`~org.orekit.propagation.events.handlers.EventMultipleHandler.eventOccurred`) : null > null > null > null > null
    
        Since:
            10.3
    """
    def __init__(self): ...
    def addHandler(self, eventHandler: EventHandler[_EventMultipleHandler__D]) -> 'EventMultipleHandler'[_EventMultipleHandler__D]: ...
    def addHandlers(self, eventHandlerArray: typing.List[EventHandler[_EventMultipleHandler__D]]) -> 'EventMultipleHandler'[_EventMultipleHandler__D]: ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, d: _EventMultipleHandler__D, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            eventOccurred method mirrors the same interface method as in :class:`~org.orekit.propagation.events.EventDetector` and
            its subclasses, but with an additional parameter that allows the calling method to pass in an object from the detector
            which would have potential additional data to allow the implementing class to determine the correct return state. The
            MultipleEventHandler class implies a different behaviour on event detections than with other handlers : Without the
            MultipleEventHandler, there is a total order on event occurrences. Handlers H1, H2, ... that are associated with
            different instances of :class:`~org.orekit.propagation.events.AbstractDetector` are successively called and Action from
            H1 can prevent H2 from happening if H1 returned null. With the MultipleEventHandler class, when event E occurs, all
            methods eventOccurred of Handlers H1, H2... from MultiEventHandler attributes are called, then Action is decided.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.handlers.EventMultipleHandler`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def getHandlers(self) -> java.util.List[EventHandler[_EventMultipleHandler__D]]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, d: _EventMultipleHandler__D) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            All handlers' init methods are successively called, the order method is the order in which handlers are added
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                target (:class:`~org.orekit.time.AbsoluteDate`): target date for the propagation
                detector (:class:`~org.orekit.propagation.events.handlers.EventMultipleHandler`): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, d: _EventMultipleHandler__D, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset the state prior to continue propagation.
        
            All handlers that return null when calling
            :meth:`~org.orekit.propagation.events.handlers.EventMultipleHandler.eventOccurred` are saved in resetStateHandlers.
            Their methods resetState are successively called. The order for calling resetState methods is the order in which
            handlers are added.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.handlers.EventMultipleHandler`): object with appropriate type that can be used in determining correct return state
                oldState (:class:`~org.orekit.propagation.SpacecraftState`): old state
        
            Returns:
                new state
        
        
        """
        ...
    def setHandlers(self, list: java.util.List[EventHandler[_EventMultipleHandler__D]]) -> None: ...

_FieldContinueOnEvent__KK = typing.TypeVar('_FieldContinueOnEvent__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_FieldContinueOnEvent__T = typing.TypeVar('_FieldContinueOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldContinueOnEvent(FieldEventHandler[_FieldContinueOnEvent__KK, _FieldContinueOnEvent__T], typing.Generic[_FieldContinueOnEvent__KK, _FieldContinueOnEvent__T]):
    """
    public class FieldContinueOnEvent<KK extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>,T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<KK,T>
    
        Event handler which will always return null as a state.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldContinueOnEvent__T], kK: _FieldContinueOnEvent__KK, boolean: bool) -> org.hipparchus.ode.events.Action: ...

_FieldRecordAndContinue__Event__T = typing.TypeVar('_FieldRecordAndContinue__Event__T')  # <T>
_FieldRecordAndContinue__Event__F = typing.TypeVar('_FieldRecordAndContinue__Event__F', bound=org.hipparchus.CalculusFieldElement)  # <F>
_FieldRecordAndContinue__T = typing.TypeVar('_FieldRecordAndContinue__T', bound=org.orekit.propagation.events.FieldEventDetector)  # <T>
_FieldRecordAndContinue__E = typing.TypeVar('_FieldRecordAndContinue__E', bound=org.hipparchus.CalculusFieldElement)  # <E>
class FieldRecordAndContinue(FieldEventHandler[_FieldRecordAndContinue__T, _FieldRecordAndContinue__E], typing.Generic[_FieldRecordAndContinue__T, _FieldRecordAndContinue__E]):
    """
    public class FieldRecordAndContinue<T extends :class:`~org.orekit.propagation.events.FieldEventDetector`<E>,E extends CalculusFieldElement<E>> extends Object implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<T,E>
    
        Handler that will record every time an event occurs and always return null.
    
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
    def __init__(self, list: java.util.List['FieldRecordAndContinue.Event'[_FieldRecordAndContinue__T, _FieldRecordAndContinue__E]]): ...
    def clear(self) -> None:
        """
            Clear all stored events.
        
        """
        ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldRecordAndContinue__E], t: _FieldRecordAndContinue__T, boolean: bool) -> org.hipparchus.ode.events.Action: ...
    def getEvents(self) -> java.util.List['FieldRecordAndContinue.Event'[_FieldRecordAndContinue__T, _FieldRecordAndContinue__E]]: ...
    class Event(typing.Generic[_FieldRecordAndContinue__Event__T, _FieldRecordAndContinue__Event__F]):
        def getDetector(self) -> _FieldRecordAndContinue__Event__T: ...
        def getState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldRecordAndContinue__Event__F]: ...
        def isIncreasing(self) -> bool: ...
        def toString(self) -> str: ...

_FieldStopOnDecreasing__KK = typing.TypeVar('_FieldStopOnDecreasing__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_FieldStopOnDecreasing__T = typing.TypeVar('_FieldStopOnDecreasing__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnDecreasing(FieldEventHandler[_FieldStopOnDecreasing__KK, _FieldStopOnDecreasing__T], typing.Generic[_FieldStopOnDecreasing__KK, _FieldStopOnDecreasing__T]):
    """
    public class FieldStopOnDecreasing<KK extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>,T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<KK,T>
    
        Handle a detection event and choose what to do next.
    
        KKhe implementation behavior is to null propagation when ascending and to null propagation when descending.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnDecreasing__T], kK: _FieldStopOnDecreasing__KK, boolean: bool) -> org.hipparchus.ode.events.Action: ...

_FieldStopOnEvent__KK = typing.TypeVar('_FieldStopOnEvent__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_FieldStopOnEvent__T = typing.TypeVar('_FieldStopOnEvent__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnEvent(FieldEventHandler[_FieldStopOnEvent__KK, _FieldStopOnEvent__T], typing.Generic[_FieldStopOnEvent__KK, _FieldStopOnEvent__T]):
    """
    public class FieldStopOnEvent<KK extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>,T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<KK,T>
    
        Event handler which will always return null as a state.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnEvent__T], kK: _FieldStopOnEvent__KK, boolean: bool) -> org.hipparchus.ode.events.Action: ...

_FieldStopOnIncreasing__KK = typing.TypeVar('_FieldStopOnIncreasing__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_FieldStopOnIncreasing__T = typing.TypeVar('_FieldStopOnIncreasing__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStopOnIncreasing(FieldEventHandler[_FieldStopOnIncreasing__KK, _FieldStopOnIncreasing__T], typing.Generic[_FieldStopOnIncreasing__KK, _FieldStopOnIncreasing__T]):
    """
    public class FieldStopOnIncreasing<KK extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>,T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<KK,T>
    
        Handle a detection event and choose what to do next.
    
        The implementation behavior is to null propagation when descending and to null propagation when ascending.
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStopOnIncreasing__T], kK: _FieldStopOnIncreasing__KK, boolean: bool) -> org.hipparchus.ode.events.Action: ...

_PythonEventHandler__T = typing.TypeVar('_PythonEventHandler__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class PythonEventHandler(EventHandler[_PythonEventHandler__T], typing.Generic[_PythonEventHandler__T]):
    """
    public class PythonEventHandler<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends Object implements :class:`~org.orekit.propagation.events.handlers.EventHandler`<T>
    
        This interface represents space-dynamics aware events detectors.
    
        It mirrors the :code:`EventHandler` interface from ` Apache Commons Math <http://commons.apache.org/math/>` but provides
        a space-dynamics interface to the methods.
    
        Events detectors are a useful solution to meet the requirements of propagators concerning discrete conditions. The state
        of each event detector is queried by the integrator at each step. When the sign of the underlying g switching function
        changes, the step is rejected and reduced, in order to make sure the sign changes occur only at steps boundaries.
    
        When step ends exactly at a switching function sign change, the corresponding event is triggered, by calling the
        :code:`#eventOccurred(SpacecraftState, boolean)` method. The method can do whatever it needs with the event (logging it,
        performing some processing, ignore it ...). The return value of the method will be used by the propagator to stop or
        resume propagation, possibly changing the state vector.
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, t: _PythonEventHandler__T, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            eventOccurred method mirrors the same interface method as in :class:`~org.orekit.propagation.events.EventDetector` and
            its subclasses, but with an additional parameter that allows the calling method to pass in an object from the detector
            which would have potential additional data to allow the implementing class to determine the correct return state.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.handlers.PythonEventHandler`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occured in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
            Raises:
                :class:`~org.orekit.errors.OrekitException`: if some specific error occurs
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getPythonObject(self) -> int: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, t: _PythonEventHandler__T) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                target (:class:`~org.orekit.time.AbsoluteDate`): target date for the propagation
                detector (:class:`~org.orekit.propagation.events.handlers.PythonEventHandler`): event detector related to the event handler
        
        
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
    def resetState(self, t: _PythonEventHandler__T, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset the state prior to continue propagation.
        
            This method is called after the step handler has returned and before the next step is started, but only when
            :meth:`~org.orekit.propagation.events.handlers.PythonEventHandler.eventOccurred` has itself returned the null indicator.
            It allows the user to reset the state for the next step, without perturbing the step handler of the finishing step. If
            the :meth:`~org.orekit.propagation.events.handlers.PythonEventHandler.eventOccurred` never returns the null indicator,
            this function will never be called, and it is safe to simply return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.handlers.PythonEventHandler`): object with appropriate type that can be used in determining correct return state
                oldState (:class:`~org.orekit.propagation.SpacecraftState`): old state
        
            Returns:
                new state
        
            Raises:
                :class:`~org.orekit.errors.OrekitException`: if the state cannot be reseted
        
        
        """
        ...

_PythonFieldEventHandler__KK = typing.TypeVar('_PythonFieldEventHandler__KK', bound=org.orekit.propagation.events.FieldEventDetector)  # <KK>
_PythonFieldEventHandler__T = typing.TypeVar('_PythonFieldEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEventHandler(FieldEventHandler[_PythonFieldEventHandler__KK, _PythonFieldEventHandler__T], typing.Generic[_PythonFieldEventHandler__KK, _PythonFieldEventHandler__T]):
    """
    public class PythonFieldEventHandler<KK extends :class:`~org.orekit.propagation.events.FieldEventDetector`<T>,T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.events.handlers.FieldEventHandler`<KK,T>
    """
    def __init__(self): ...
    def eventOccurred(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], kK: _PythonFieldEventHandler__KK, boolean: bool) -> org.hipparchus.ode.events.Action: ...
    def finalize(self) -> None: ...
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldEventHandler__T], kK: _PythonFieldEventHandler__KK) -> None: ...
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldEventHandler__T]) -> None: ...
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
    def resetState(self, kK: _PythonFieldEventHandler__KK, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldEventHandler__T]: ...

_RecordAndContinue__Event__T = typing.TypeVar('_RecordAndContinue__Event__T')  # <T>
_RecordAndContinue__T = typing.TypeVar('_RecordAndContinue__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class RecordAndContinue(EventHandler[_RecordAndContinue__T], typing.Generic[_RecordAndContinue__T]):
    """
    public class RecordAndContinue<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends Object implements :class:`~org.orekit.propagation.events.handlers.EventHandler`<T>
    
        Handler that will record every time an event occurs and always return null.
    
        As this handler stores all observed events it may consume large amounts of memory depending on the duration of
        propagation and the frequency of events.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List['RecordAndContinue.Event'[_RecordAndContinue__T]]): ...
    def clear(self) -> None:
        """
            Clear all stored events.
        
        """
        ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, t: _RecordAndContinue__T, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`
            eventOccurred method mirrors the same interface method as in :class:`~org.orekit.propagation.events.EventDetector` and
            its subclasses, but with an additional parameter that allows the calling method to pass in an object from the detector
            which would have potential additional data to allow the implementing class to determine the correct return state.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.handlers.RecordAndContinue`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def getEvents(self) -> java.util.List['RecordAndContinue.Event'[_RecordAndContinue__T]]: ...
    class Event(typing.Generic[_RecordAndContinue__Event__T]):
        def getDetector(self) -> _RecordAndContinue__Event__T: ...
        def getState(self) -> org.orekit.propagation.SpacecraftState: ...
        def isIncreasing(self) -> bool: ...
        def toString(self) -> str: ...

_StopOnDecreasing__T = typing.TypeVar('_StopOnDecreasing__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class StopOnDecreasing(EventHandler[_StopOnDecreasing__T], typing.Generic[_StopOnDecreasing__T]):
    """
    public class StopOnDecreasing<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends Object implements :class:`~org.orekit.propagation.events.handlers.EventHandler`<T>
    
        Handle a detection event and choose what to do next.
    
        The implementation behavior is to null propagation when ascending and to null propagation when descending.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, t: _StopOnDecreasing__T, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Handle a detection event and choose what to do next.
        
            The implementation behavior is to null propagation when ascending and to null propagation when descending.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information : date, kinematics, attitude
                detector (:class:`~org.orekit.propagation.events.handlers.StopOnDecreasing`): the detector object calling this method (not used in the evaluation)
                increasing (boolean): if true, the value of the switching function increases when times increases around event
        
            Returns:
                null or null
        
        
        """
        ...

_StopOnEvent__T = typing.TypeVar('_StopOnEvent__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class StopOnEvent(EventHandler[_StopOnEvent__T], typing.Generic[_StopOnEvent__T]):
    """
    public class StopOnEvent<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends Object implements :class:`~org.orekit.propagation.events.handlers.EventHandler`<T>
    
        Event handler which will always return null as a state.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, t: _StopOnEvent__T, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Specific implementation of the eventOccurred interface.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.handlers.StopOnEvent`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                null under all circumstances
        
        
        """
        ...

_StopOnIncreasing__T = typing.TypeVar('_StopOnIncreasing__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class StopOnIncreasing(EventHandler[_StopOnIncreasing__T], typing.Generic[_StopOnIncreasing__T]):
    """
    public class StopOnIncreasing<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends Object implements :class:`~org.orekit.propagation.events.handlers.EventHandler`<T>
    
        Handle a detection event and choose what to do next.
    
        The implementation behavior is to null propagation when descending and to null propagation when ascending.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, t: _StopOnIncreasing__T, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            Handle a detection event and choose what to do next.
        
            The implementation behavior is to null propagation when descending and to null propagation when ascending.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information : date, kinematics, attitude
                detector (:class:`~org.orekit.propagation.events.handlers.StopOnIncreasing`): the detector object calling this method (not used in the evaluation)
                increasing (boolean): if true, the value of the switching function increases when times increases around event
        
            Returns:
                null or null
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events.handlers")``.

    ContinueOnEvent: typing.Type[ContinueOnEvent]
    EventHandler: typing.Type[EventHandler]
    EventMultipleHandler: typing.Type[EventMultipleHandler]
    FieldContinueOnEvent: typing.Type[FieldContinueOnEvent]
    FieldEventHandler: typing.Type[FieldEventHandler]
    FieldRecordAndContinue: typing.Type[FieldRecordAndContinue]
    FieldStopOnDecreasing: typing.Type[FieldStopOnDecreasing]
    FieldStopOnEvent: typing.Type[FieldStopOnEvent]
    FieldStopOnIncreasing: typing.Type[FieldStopOnIncreasing]
    PythonEventHandler: typing.Type[PythonEventHandler]
    PythonFieldEventHandler: typing.Type[PythonFieldEventHandler]
    RecordAndContinue: typing.Type[RecordAndContinue]
    StopOnDecreasing: typing.Type[StopOnDecreasing]
    StopOnEvent: typing.Type[StopOnEvent]
    StopOnIncreasing: typing.Type[StopOnIncreasing]
