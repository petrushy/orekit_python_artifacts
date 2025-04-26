
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.solvers
import org.hipparchus.ode
import org.hipparchus.ode.sampling
import typing



class Action(java.lang.Enum['Action']):
    """
    public enumAction extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.ode.events.Action`>
    
        Enumerate for actions to be performed when an event occurs during ODE integration.
    """
    STOP: typing.ClassVar['Action'] = ...
    RESET_STATE: typing.ClassVar['Action'] = ...
    RESET_DERIVATIVES: typing.ClassVar['Action'] = ...
    CONTINUE: typing.ClassVar['Action'] = ...
    RESET_EVENTS: typing.ClassVar['Action'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Action':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['Action']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdaptableInterval:
    """
    :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.FunctionalInterface`public interfaceAdaptableInterval
    
        This interface represents an event checking interval that depends on state.
    
        Since:
            3.0
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.ODEEventDetector`
    """
    def currentInterval(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, boolean: bool) -> float:
        """
            Get the current value of maximal time interval between events handler checks.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current state
                isForward (boolean): true if propagation is forward in independent variable, false otherwise
        
            Returns:
                current value of maximal time interval between events handler checks
        
        
        """
        ...
    @staticmethod
    def of(double: float) -> 'AdaptableInterval':
        """
            Create a constant interval from the input.
        
            Parameters:
                maxCheck (double): maximum check value
        
            Returns:
                constant interval
        
            Since:
                4.0
        
        
        """
        ...

class EventOccurrence:
    """
    public classEventOccurrence extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class to hold the data related to an event occurrence that is needed to decide how to modify integration.
    
        Since:
            3.O
    """
    def __init__(self, action: Action, oDEState: org.hipparchus.ode.ODEState, double: float): ...
    def getAction(self) -> Action:
        """
            Get the user requested action.
        
            Returns:
                the action.
        
        
        """
        ...
    def getNewState(self) -> org.hipparchus.ode.ODEState:
        """
            Get the new state for a reset action.
        
            Returns:
                the new state.
        
        
        """
        ...
    def getStopTime(self) -> float:
        """
            Get the new time for a stop action.
        
            Returns:
                when to stop propagation.
        
        
        """
        ...

class EventState:
    """
    public interfaceEventState
    
        This interface handles the state for either one :class:`~org.hipparchus.ode.events.ODEEventHandler` or one
        :class:`~org.hipparchus.ode.events.ODEStepEndHandler` during integration steps.
    
        Since:
            3.0
    """
    def doEvent(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> EventOccurrence:
        """
            Notify the user's listener of the event. The event occurs wholly within this method call including a call to
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.resetState` if necessary.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): the state at the time of the event. This must be at the same time as the current value of
                    :meth:`~org.hipparchus.ode.events.EventState.getEventTime`.
        
            Returns:
                the user's requested action and the new state if the action is :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`.
                Otherwise the new state is :code:`state`. The stop time indicates what time propagation should stop if the action is
                :meth:`~org.hipparchus.ode.events.Action.STOP`. This guarantees the integration will stop on or after the root, so that
                integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool: ...
    def getEventTime(self) -> float:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize handler at the start of an integration.
        
            This method is called once at the start of the integration. It may be used by the handler to initialize some internal
            data if needed.
        
            Parameters:
                s0 (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial state
                t (double): target time for the integration
        
        
        """
        ...

_FieldAdaptableInterval__T = typing.TypeVar('_FieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdaptableInterval(typing.Generic[_FieldAdaptableInterval__T]):
    """
    :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.FunctionalInterface`public interfaceFieldAdaptableInterval<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents an event checking interval that depends on state.
    
        Since:
            3.0
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.ODEEventDetector`
    """
    def currentInterval(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldAdaptableInterval__T], boolean: bool) -> float: ...
    _of__W = typing.TypeVar('_of__W', bound=org.hipparchus.CalculusFieldElement)  # <W>
    @staticmethod
    def of(double: float) -> 'FieldAdaptableInterval'[_of__W]:
        """
            Create a constant interval from the input.
        
            Parameters:
                maxCheck (double): maximum check value
        
            Returns:
                constant interval
        
            Since:
                4.0
        
        
        """
        ...

_FieldEventOccurrence__T = typing.TypeVar('_FieldEventOccurrence__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventOccurrence(typing.Generic[_FieldEventOccurrence__T]):
    """
    public classFieldEventOccurrence<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class to hold the data related to an event occurrence that is needed to decide how to modify integration.
    """
    def __init__(self, action: Action, fieldODEState: org.hipparchus.ode.FieldODEState[_FieldEventOccurrence__T], t: _FieldEventOccurrence__T): ...
    def getAction(self) -> Action:
        """
            Get the user requested action.
        
            Returns:
                the action.
        
        
        """
        ...
    def getNewState(self) -> org.hipparchus.ode.FieldODEState[_FieldEventOccurrence__T]: ...
    def getStopTime(self) -> _FieldEventOccurrence__T:
        """
            Get the new time for a stop action.
        
            Returns:
                when to stop propagation.
        
        
        """
        ...

_FieldEventState__T = typing.TypeVar('_FieldEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventState(typing.Generic[_FieldEventState__T]):
    """
    public interfaceFieldEventState<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface handles the state for either one :class:`~org.hipparchus.ode.events.FieldODEEventHandler` or one
        :class:`~org.hipparchus.ode.events.FieldODEStepEndHandler` during integration steps.
    
        Since:
            3.0
    """
    def doEvent(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T]) -> FieldEventOccurrence[_FieldEventState__T]: ...
    def evaluateStep(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> bool: ...
    def getEventTime(self) -> _FieldEventState__T:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T], t: _FieldEventState__T) -> None: ...

_FieldODEEventDetector__T = typing.TypeVar('_FieldODEEventDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEEventDetector(typing.Generic[_FieldODEEventDetector__T]):
    """
    public interfaceFieldODEEventDetector<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents a handler for discrete events triggered during ODE integration.
    
        Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration
        process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when
        the derivatives have states boundaries crossings.
    
        These events are defined as occurring when a :code:`g` switching function sign changes.
    
        Since events are only problem-dependent and are triggered by the independent *time* variable and the state vector, they
        can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the
        steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of
        the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in
        presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the
        local error (this event handling feature is available for all integrators, including fixed step ones).
    
        Note that prior to Hipparchus 3.0, the methods in this interface were in the
        :class:`~org.hipparchus.ode.events.FieldODEEventHandler` interface and the defunct
        :code:`FieldEventHandlerConfiguration` interface. The interfaces have been reorganized to allow different objects to be
        used in event detection and event handling, hence allowing users to reuse predefined events detectors with custom
        handlers.
    
        Since:
            3.0
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.package`
    """
    def g(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventDetector__T]) -> _FieldODEEventDetector__T: ...
    def getHandler(self) -> 'FieldODEEventHandler'[_FieldODEEventDetector__T]: ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_FieldODEEventDetector__T]: ...
    def getMaxIterationCount(self) -> int:
        """
            Get the upper limit in the iteration count for event localization.
        
            Returns:
                upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldODEEventDetector__T]: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventDetector__T], t: _FieldODEEventDetector__T) -> None: ...
    def reset(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventDetector__T], t: _FieldODEEventDetector__T) -> None: ...

_FieldODEEventHandler__T = typing.TypeVar('_FieldODEEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEEventHandler(typing.Generic[_FieldODEEventHandler__T]):
    """
    public interfaceFieldODEEventHandler<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents a handler for discrete events triggered during ODE integration.
    
        Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration
        process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when
        the derivatives have states boundaries crossings.
    
        These events are defined as occurring when a :code:`g` switching function sign changes.
    
        Since events are only problem-dependent and are triggered by the independent *time* variable and the state vector, they
        can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the
        steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of
        the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in
        presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the
        local error (this event handling feature is available for all integrators, including fixed step ones).
    
        Note that prior to Hipparchus 3.0, some of the methods that are now in
        :class:`~org.hipparchus.ode.events.FieldODEEventDetector` were in this interface (and the remaining ones were in the
        defunct :code:`FieldEventHandlerConfiguration` interface). The interfaces have been reorganized to allow different
        objects to be used in event detection and event handling, hence allowing users to reuse predefined events detectors with
        custom handlers.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.package`
    """
    def eventOccurred(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], fieldODEEventDetector: FieldODEEventDetector[_FieldODEEventHandler__T], boolean: bool) -> Action: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], t: _FieldODEEventHandler__T, fieldODEEventDetector: FieldODEEventDetector[_FieldODEEventHandler__T]) -> None: ...
    def resetState(self, fieldODEEventDetector: FieldODEEventDetector[_FieldODEEventHandler__T], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T]) -> org.hipparchus.ode.FieldODEState[_FieldODEEventHandler__T]: ...

_FieldODEStepEndHandler__T = typing.TypeVar('_FieldODEStepEndHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStepEndHandler(typing.Generic[_FieldODEStepEndHandler__T]):
    """
    public interfaceFieldODEStepEndHandler<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents a handler for discrete events triggered during ODE integration at each step end.
    
        Since:
            3.0
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.package`
    """
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepEndHandler__T], t: _FieldODEStepEndHandler__T) -> None: ...
    def resetState(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepEndHandler__T]) -> org.hipparchus.ode.FieldODEState[_FieldODEStepEndHandler__T]: ...
    def stepEndOccurred(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepEndHandler__T], boolean: bool) -> Action: ...

class FilterType(java.lang.Enum['FilterType']):
    """
    public enumFilterType extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.ode.events.FilterType`>
    
        Enumerate for :class:`~org.hipparchus.ode.events.EventSlopeFilter`.
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
                name (:class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['FilterType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ODEEventDetector:
    """
    public interfaceODEEventDetector
    
        This interface represents a detector for discrete events triggered during ODE integration.
    
        Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration
        process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when
        the derivatives have discontinuities, or simply when the user wants to monitor some states boundaries crossings.
    
        These events are defined as occurring when a :code:`g` switching function sign changes.
    
        Since events are only problem-dependent and are triggered by the independent *time* variable and the state vector, they
        can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the
        steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of
        the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in
        presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the
        local error (this event handling feature is available for all integrators, including fixed step ones).
    
        Note that prior to Hipparchus 3.0, the methods in this interface were in the
        :class:`~org.hipparchus.ode.events.ODEEventHandler` interface and the defunct :code:`EventHandlerConfiguration`
        interface. The interfaces have been reorganized to allow different objects to be used in event detection and event
        handling, hence allowing users to reuse predefined events detectors with custom handlers.
    
        Since:
            3.0
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.package`
    """
    def g(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> float:
        """
            Compute the value of the switching function.
        
            The discrete events are generated when the sign of this switching function changes. The integrator will take care to
            change the stepsize in such a way these events occur exactly at step boundaries. The switching function must be
            continuous in its roots neighborhood (but not necessarily smooth), as the integrator will need to find its roots to
            locate precisely the events.
        
            Also note that for the integrator to detect an event the sign of the switching function must have opposite signs just
            before and after the event. If this consistency is not preserved the integrator may not detect any events.
        
            This need for consistency is sometimes tricky to achieve. A typical example is using an event to model a ball bouncing
            on the floor. The first idea to represent this would be to have :code:`g(state) = h(state)` where h is the height above
            the floor at time :code:`state.getTime()`. When :code:`g(state)` reaches 0, the ball is on the floor, so it should
            bounce and the typical way to do this is to reverse its vertical velocity. However, this would mean that before the
            event :code:`g(state)` was decreasing from positive values to 0, and after the event :code:`g(state)` would be
            increasing from 0 to positive values again. Consistency is broken here! The solution here is to have :code:`g(state) =
            sign * h(state)`, where sign is a variable with initial value set to :code:`+1`. Each time
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` is called, :code:`sign` is reset to :code:`-sign`. This
            allows the :code:`g(state)` function to remain continuous (and even smooth) even across events, despite :code:`h(state)`
            is not. Basically, the event is used to *fold* :code:`h(state)` at bounce points, and :code:`sign` is used to *unfold*
            it back, so the solvers sees a :code:`g(state)` function which behaves smoothly even across events.
        
            This method is idempotent, that is calling this multiple times with the same state will result in the same value, with
            two exceptions. First, the definition of the g function may change when an
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` on the handler, as in the above example. Second, the
            definition of the g function may change when the :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` method
            of any other event handler in the same integrator returns :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`,
            :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, or :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
        
            Returns:
                value of the g switching function
        
            Also see:
        
                  - :class:`~org.hipparchus.ode.events.package`
        
        
        
        """
        ...
    def getHandler(self) -> 'ODEEventHandler':
        """
            Get the underlying event handler.
        
            Returns:
                underlying event handler
        
        
        """
        ...
    def getMaxCheckInterval(self) -> AdaptableInterval:
        """
            Get the maximal time interval between events handler checks.
        
            Returns:
                maximal time interval between events handler checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
            Get the upper limit in the iteration count for event localization.
        
            Returns:
                upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]: ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize event detector at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the event detector to initialize some
            internal data if needed.
        
            The default implementation initializes the handler
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                finalTime (double): target time for the integration
        
        
        """
        ...
    def reset(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Reset event detector during integration.
        
            This method is called during integration if the derivatives or the state variables themselves are reset.
        
            The default implementation does nothing.
        
            Parameters:
                intermediateState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): intermediate time, state vector and derivative
                finalTime (double): target time for the integration
        
            Since:
                4.0
        
        
        """
        ...

class ODEEventHandler:
    """
    public interfaceODEEventHandler
    
        This interface represents a handler for discrete events triggered during ODE integration.
    
        Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration
        process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when
        the derivatives have discontinuities, or simply when the user wants to monitor some states boundaries crossings.
    
        These events are defined as occurring when a :code:`g` switching function sign changes.
    
        Since events are only problem-dependent and are triggered by the independent *time* variable and the state vector, they
        can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the
        steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of
        the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in
        presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the
        local error (this event handling feature is available for all integrators, including fixed step ones).
    
        Note that prior to Hipparchus 3.0, some of the methods that are now in
        :class:`~org.hipparchus.ode.events.ODEEventDetector` were in this interface (and the remaining ones were in the defunct
        :code:`EventHandlerConfiguration` interface). The interfaces have been reorganized to allow different objects to be used
        in event detection and event handling, hence allowing users to reuse predefined events detectors with custom handlers.
    
        Since:
            3.0
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.package`
    """
    def eventOccurred(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEEventDetector: ODEEventDetector, boolean: bool) -> Action:
        """
            Handle an event and choose what to do next.
        
            This method is called when the integrator has accepted a step ending exactly on a sign change of the function, just
            *after* the step handler itself is called (see below for scheduling). It allows the user to update his internal data to
            acknowledge the fact the event has been handled (for example setting a flag in the
            :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` to switch the derivatives computation in case of
            discontinuity), or to direct the integrator to either stop or continue integration, possibly with a reset state or
            derivatives.
        
              - if :meth:`~org.hipparchus.ode.events.Action.STOP` is returned, the integration will be stopped,
              - if :meth:`~org.hipparchus.ode.events.Action.RESET_STATE` is returned, the
                :meth:`~org.hipparchus.ode.events.ODEEventHandler.resetState` method will be called once the step handler has finished
                its task, and the integrator will also recompute the derivatives,
              - if :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES` is returned, the integrator will recompute the
                derivatives,
              - if :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS` is returned, the integrator will recheck all event handlers,
              - if :meth:`~org.hipparchus.ode.events.Action.CONTINUE` is returned, no specific action will be taken (apart from having
                called this method) and integration will continue.
        
        
            The scheduling between this method and the :class:`~org.hipparchus.ode.sampling.ODEStepHandler` method
            :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.handleStep` is to call :code:`handleStep` first and this method
            afterwards (this scheduling changed as of Hipparchus 2.0). This scheduling allows user code called by this method and
            user code called by step handlers to get values of the independent time variable consistent with integration direction.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
                detector (:class:`~org.hipparchus.ode.events.ODEEventDetector`): detector that triggered the event
                increasing (boolean): if true, the value of the switching function increases when times increases around event (note that increase is measured
                    with respect to physical time, not with respect to integration which may go backward in time)
        
            Returns:
                indication of what the integrator should do next, this value must be one of
                :meth:`~org.hipparchus.ode.events.Action.STOP`, :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`,
                :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`, or
                :meth:`~org.hipparchus.ode.events.Action.CONTINUE`
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float, oDEEventDetector: ODEEventDetector) -> None:
        """
            Initialize event handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                finalTime (double): target time for the integration
                detector (:class:`~org.hipparchus.ode.events.ODEEventDetector`): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, oDEEventDetector: ODEEventDetector, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> org.hipparchus.ode.ODEState:
        """
            Reset the state prior to continue the integration.
        
            This method is called after the step handler has returned and before the next step is started, but only when
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` has itself returned the
            :meth:`~org.hipparchus.ode.events.Action.RESET_STATE` indicator. It allows the user to reset the state vector for the
            next step, without perturbing the step handler of the finishing step.
        
            The default implementation returns its argument.
        
            Parameters:
                detector (:class:`~org.hipparchus.ode.events.ODEEventDetector`): detector that triggered the event
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
        
            Returns:
                reset state (note that it does not include the derivatives, they will be added automatically by the integrator
                afterwards)
        
        
        """
        ...

class ODEStepEndHandler:
    """
    public interfaceODEStepEndHandler
    
        This interface represents a handler for discrete events triggered during ODE integration at each step end.
    
        Since:
            3.0
    
        Also see:
    
              - :class:`~org.hipparchus.ode.events.package`
    """
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize step end handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the step end handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                finalTime (double): target time for the integration
        
        
        """
        ...
    def resetState(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> org.hipparchus.ode.ODEState:
        """
            Reset the state prior to continue the integration.
        
            This method is called after the step handler has returned and before the next step is started, but only when
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` has itself returned the
            :meth:`~org.hipparchus.ode.events.Action.RESET_STATE` indicator. It allows the user to reset the state vector for the
            next step, without perturbing the step handler of the finishing step.
        
            The default implementation returns its argument.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative at step end
        
            Returns:
                reset state (note that it does not include the derivatives, they will be added automatically by the integrator
                afterwards)
        
        
        """
        ...
    def stepEndOccurred(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, boolean: bool) -> Action:
        """
            Handle an event and choose what to do next.
        
            This method is called when the integrator has accepted a step ending exactly on step end, just *after* the step handler
            itself is called (see below for scheduling). It allows the user to update his internal data to acknowledge the fact the
            event has been handled (for example setting a flag in the :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` to
            switch the derivatives computation in case of discontinuity), or to direct the integrator to either stop or continue
            integration, possibly with a reset state or derivatives.
        
              - if :meth:`~org.hipparchus.ode.events.Action.STOP` is returned, the integration will be stopped,
              - if :meth:`~org.hipparchus.ode.events.Action.RESET_STATE` is returned, the
                :meth:`~org.hipparchus.ode.events.ODEStepEndHandler.resetState` method will be called once the step handler has finished
                its task, and the integrator will also recompute the derivatives,
              - if :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES` is returned, the integrator will recompute the
                derivatives,
              - if :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS` is returned, the integrator will recheck all event handlers,
              - if :meth:`~org.hipparchus.ode.events.Action.CONTINUE` is returned, no specific action will be taken (apart from having
                called this method) and integration will continue.
        
        
            The scheduling between this method and the :class:`~org.hipparchus.ode.sampling.ODEStepHandler` method
            :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.handleStep` is to call :code:`handleStep` first and this method
            afterwards. This scheduling allows user code called by this method and user code called by step handlers to get values
            of the independent time variable consistent with integration direction.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative at step end
                forward (boolean): if true, propagation is forward
        
            Returns:
                indication of what the integrator should do next, this value must be one of
                :meth:`~org.hipparchus.ode.events.Action.STOP`, :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`,
                :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`, or
                :meth:`~org.hipparchus.ode.events.Action.CONTINUE`
        
        
        """
        ...

_AbstractFieldODEDetector__T = typing.TypeVar('_AbstractFieldODEDetector__T', bound='AbstractFieldODEDetector')  # <T>
_AbstractFieldODEDetector__E = typing.TypeVar('_AbstractFieldODEDetector__E', bound=org.hipparchus.CalculusFieldElement)  # <E>
class AbstractFieldODEDetector(FieldODEEventDetector[_AbstractFieldODEDetector__E], typing.Generic[_AbstractFieldODEDetector__T, _AbstractFieldODEDetector__E]):
    """
    public abstract classAbstractFieldODEDetector<T extends AbstractFieldODEDetector<T,E>,E extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<E>> extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.events.FieldODEEventDetector`<E>
    
        Base class for #@link :class:`~org.hipparchus.ode.events.FieldODEEventDetector`.
    
        Since:
            3.0
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAX_CHECK
    
        Default maximum checking interval (s).
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default convergence threshold (s).
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITER
    
        Default maximum number of iterations in the event time search.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    def getHandler(self) -> FieldODEEventHandler[_AbstractFieldODEDetector__E]: ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_AbstractFieldODEDetector__E]: ...
    def getMaxIterationCount(self) -> int:
        """
            Get the upper limit in the iteration count for event localization.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.FieldODEEventDetector.getMaxIterationCount` in
                interface :class:`~org.hipparchus.ode.events.FieldODEEventDetector`
        
            Returns:
                upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_AbstractFieldODEDetector__E]: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEDetector__E], e: _AbstractFieldODEDetector__E) -> None: ...
    def isForward(self) -> bool:
        """
            Check if the current propagation is forward or backward.
        
            Returns:
                true if the current propagation is forward
        
        
        """
        ...
    def withHandler(self, fieldODEEventHandler: typing.Union[FieldODEEventHandler[_AbstractFieldODEDetector__E], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], FieldODEEventDetector[org.hipparchus.CalculusFieldElement], bool], Action]]) -> _AbstractFieldODEDetector__T: ...
    @typing.overload
    def withMaxCheck(self, e: _AbstractFieldODEDetector__E) -> _AbstractFieldODEDetector__T:
        """
            Setup the maximum checking interval.
        
            This will override a maximum checking interval if it has been configured previously.
        
            Parameters:
                newMaxCheck (:class:`~org.hipparchus.ode.events.AbstractFieldODEDetector`): maximum checking interval (s)
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
        public :class:`~org.hipparchus.ode.events.AbstractFieldODEDetector` withMaxCheck(:class:`~org.hipparchus.ode.events.FieldAdaptableInterval`<:class:`~org.hipparchus.ode.events.AbstractFieldODEDetector`> newMaxCheck)
        
            Setup the maximum checking interval.
        
            This will override a maximum checking interval if it has been configured previously.
        
            Parameters:
                newMaxCheck (:class:`~org.hipparchus.ode.events.FieldAdaptableInterval`<:class:`~org.hipparchus.ode.events.AbstractFieldODEDetector`> newMaxCheck): maximum checking interval (s)
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                3.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, fieldAdaptableInterval: typing.Union[FieldAdaptableInterval[_AbstractFieldODEDetector__E], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], float]]) -> _AbstractFieldODEDetector__T: ...
    def withMaxIter(self, int: int) -> _AbstractFieldODEDetector__T:
        """
            Setup the maximum number of iterations in the event time search.
        
            This will override a number of iterations if it has been configured previously.
        
            Parameters:
                newMaxIter (int): maximum number of iterations in the event time search
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withSolver(self, bracketedRealFieldUnivariateSolver: org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_AbstractFieldODEDetector__E]) -> _AbstractFieldODEDetector__T: ...
    def withThreshold(self, e: _AbstractFieldODEDetector__E) -> _AbstractFieldODEDetector__T:
        """
            Setup the convergence threshold.
        
            This is equivalent to call :code:`withSolver(new FieldBracketingNthOrderBrentSolver<>(zero, newThreshold, zero, 5)`,
            so it will override a solver if one has been configured previously.
        
            Parameters:
                newThreshold (:class:`~org.hipparchus.ode.events.AbstractFieldODEDetector`): convergence threshold
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.events.AbstractFieldODEDetector.withSolver`
        
        
        
        """
        ...

_AbstractODEDetector__T = typing.TypeVar('_AbstractODEDetector__T', bound='AbstractODEDetector')  # <T>
class AbstractODEDetector(ODEEventDetector, typing.Generic[_AbstractODEDetector__T]):
    """
    public abstract classAbstractODEDetector<T extends AbstractODEDetector<T>> extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.events.ODEEventDetector`
    
        Base class for #@link :class:`~org.hipparchus.ode.events.ODEEventDetector`.
    
        Since:
            3.0
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAX_CHECK
    
        Default maximum checking interval (s).
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
        Default convergence threshold (s).
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITER
    
        Default maximum number of iterations in the event time search.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    def getHandler(self) -> ODEEventHandler:
        """
            Get the underlying event handler.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventDetector.getHandler` in
                interface :class:`~org.hipparchus.ode.events.ODEEventDetector`
        
            Returns:
                underlying event handler
        
        
        """
        ...
    def getMaxCheckInterval(self) -> AdaptableInterval:
        """
            Get the maximal time interval between events handler checks.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventDetector.getMaxCheckInterval` in
                interface :class:`~org.hipparchus.ode.events.ODEEventDetector`
        
            Returns:
                maximal time interval between events handler checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
            Get the upper limit in the iteration count for event localization.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventDetector.getMaxIterationCount` in
                interface :class:`~org.hipparchus.ode.events.ODEEventDetector`
        
            Returns:
                upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]: ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize event detector at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the event detector to initialize some
            internal data if needed.
        
            The default implementation initializes the handler
        
            This implementation sets the direction of integration and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventDetector.init` in
                interface :class:`~org.hipparchus.ode.events.ODEEventDetector`
        
            Parameters:
                s0 (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                t (double): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
            Check if the current propagation is forward or backward.
        
            Returns:
                true if the current propagation is forward
        
        
        """
        ...
    def withHandler(self, oDEEventHandler: typing.Union[ODEEventHandler, typing.Callable]) -> _AbstractODEDetector__T:
        """
            Setup the event handler to call at event occurrences.
        
            This will override a handler if it has been configured previously.
        
            Parameters:
                newHandler (:class:`~org.hipparchus.ode.events.ODEEventHandler`): event handler to call at event occurrences
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, double: float) -> _AbstractODEDetector__T:
        """
            Setup the maximum checking interval.
        
            This will override a maximum checking interval if it has been configured previously.
        
            Parameters:
                newMaxCheck (double): maximum checking interval
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Setup the maximum checking interval.
        
            This will override a maximum checking interval if it has been configured previously.
        
            Parameters:
                newMaxCheck (:class:`~org.hipparchus.ode.events.AdaptableInterval`): maximum checking interval
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Since:
                3.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, adaptableInterval: typing.Union[AdaptableInterval, typing.Callable]) -> _AbstractODEDetector__T: ...
    def withMaxIter(self, int: int) -> _AbstractODEDetector__T:
        """
            Setup the maximum number of iterations in the event time search.
        
            This will override a number of iterations if it has been configured previously.
        
            Parameters:
                newMaxIter (int): maximum number of iterations in the event time search
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withSolver(self, bracketedUnivariateSolver: org.hipparchus.analysis.solvers.BracketedUnivariateSolver[typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]]) -> _AbstractODEDetector__T: ...
    def withThreshold(self, double: float) -> _AbstractODEDetector__T:
        """
            Setup the convergence threshold.
        
            This is equivalent to call :code:`withSolver(new BracketingNthOrderBrentSolver(0, newThreshold, 0, 5))`, so it will
            override a solver if one has been configured previously.
        
            Parameters:
                newThreshold (double): convergence threshold
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.events.AbstractODEDetector.withSolver`
        
        
        
        """
        ...

class DetectorBasedEventState(EventState):
    """
    public classDetectorBasedEventState extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.events.EventState`
    
        This class handles the state for one :class:`~org.hipparchus.ode.events.ODEEventHandler` during integration steps.
    
        Each time the integrator proposes a step, the event handler switching function should be checked. This class handles the
        state of one handler during one integration step, with references to the state at the end of the preceding step. This
        information is used to decide if the handler should trigger an event or not during the proposed step.
    """
    def __init__(self, oDEEventDetector: ODEEventDetector): ...
    def doEvent(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> EventOccurrence:
        """
            Notify the user's listener of the event. The event occurs wholly within this method call including a call to
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.resetState` if necessary.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventState.doEvent` in interface :class:`~org.hipparchus.ode.events.EventState`
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): the state at the time of the event. This must be at the same time as the current value of
                    :meth:`~org.hipparchus.ode.events.EventState.getEventTime`.
        
            Returns:
                the user's requested action and the new state if the action is :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`.
                Otherwise the new state is :code:`state`. The stop time indicates what time propagation should stop if the action is
                :meth:`~org.hipparchus.ode.events.Action.STOP`. This guarantees the integration will stop on or after the root, so that
                integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool: ...
    def getEventDetector(self) -> ODEEventDetector:
        """
            Get the underlying event detector.
        
            Returns:
                underlying event detector
        
            Since:
                3.0
        
        
        """
        ...
    def getEventTime(self) -> float:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventState.getEventTime` in interface :class:`~org.hipparchus.ode.events.EventState`
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize handler at the start of an integration.
        
            This method is called once at the start of the integration. It may be used by the handler to initialize some internal
            data if needed.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventState.init` in interface :class:`~org.hipparchus.ode.events.EventState`
        
            Parameters:
                s0 (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial state
                t (double): target time for the integration
        
        
        """
        ...
    def reinitializeBegin(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> None: ...
    def tryAdvance(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool:
        """
            Try to accept the current history up to the given time.
        
            It is not necessary to call this method before calling
            :meth:`~org.hipparchus.ode.events.DetectorBasedEventState.doEvent` with the same state. It is necessary to call this
            method before you call :meth:`~org.hipparchus.ode.events.DetectorBasedEventState.doEvent` on some other event detector.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): to try to accept.
                interpolator (:class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`): to use to find the new root, if any.
        
            Returns:
                if the event detector has an event it has not detected before that is on or before the same time as :code:`state`. In
                other words :code:`false` means continue on while :code:`true` means stop and handle my event first.
        
        
        """
        ...

_FieldDetectorBasedEventState__T = typing.TypeVar('_FieldDetectorBasedEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDetectorBasedEventState(FieldEventState[_FieldDetectorBasedEventState__T], typing.Generic[_FieldDetectorBasedEventState__T]):
    """
    public classFieldDetectorBasedEventState<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.events.FieldEventState`<T>
    
        This class handles the state for one :class:`~org.hipparchus.ode.events.FieldODEEventHandler` during integration steps.
    
        Each time the integrator proposes a step, the event handler switching function should be checked. This class handles the
        state of one handler during one integration step, with references to the state at the end of the preceding step. This
        information is used to decide if the handler should trigger an event or not during the proposed step.
    """
    def __init__(self, fieldODEEventDetector: FieldODEEventDetector[_FieldDetectorBasedEventState__T]): ...
    def doEvent(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldDetectorBasedEventState__T]) -> FieldEventOccurrence[_FieldDetectorBasedEventState__T]: ...
    def evaluateStep(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDetectorBasedEventState__T]) -> bool: ...
    def getEventDetector(self) -> FieldODEEventDetector[_FieldDetectorBasedEventState__T]: ...
    def getEventTime(self) -> _FieldDetectorBasedEventState__T:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.FieldEventState.getEventTime` in
                interface :class:`~org.hipparchus.ode.events.FieldEventState`
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldDetectorBasedEventState__T], t: _FieldDetectorBasedEventState__T) -> None: ...
    def reinitializeBegin(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDetectorBasedEventState__T]) -> None: ...
    def tryAdvance(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldDetectorBasedEventState__T], fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDetectorBasedEventState__T]) -> bool: ...

_FieldStepEndEventState__T = typing.TypeVar('_FieldStepEndEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStepEndEventState(FieldEventState[_FieldStepEndEventState__T], typing.Generic[_FieldStepEndEventState__T]):
    """
    public classFieldStepEndEventState<T extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.events.FieldEventState`<T>
    
        This class handles the state for one :class:`~org.hipparchus.ode.events.ODEEventHandler` that triggers at step end.
    
        Since:
            3.0
    """
    def __init__(self, fieldODEStepEndHandler: typing.Union[FieldODEStepEndHandler[_FieldStepEndEventState__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], Action]]): ...
    def doEvent(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepEndEventState__T]) -> FieldEventOccurrence[_FieldStepEndEventState__T]: ...
    def evaluateStep(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldStepEndEventState__T]) -> bool: ...
    def getEventTime(self) -> _FieldStepEndEventState__T:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.FieldEventState.getEventTime` in
                interface :class:`~org.hipparchus.ode.events.FieldEventState`
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def getHandler(self) -> FieldODEStepEndHandler[_FieldStepEndEventState__T]: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepEndEventState__T], t: _FieldStepEndEventState__T) -> None: ...
    def setStepEnd(self, t: _FieldStepEndEventState__T) -> None:
        """
            Set the step end.
        
            Parameters:
                stepEnd (:class:`~org.hipparchus.ode.events.FieldStepEndEventState`): step end
        
        
        """
        ...

class StepEndEventState(EventState):
    """
    public classStepEndEventState extends :class:`~org.hipparchus.ode.events.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.events.EventState`
    
        This class handles the state for one :class:`~org.hipparchus.ode.events.ODEEventHandler` that triggers at step end.
    
        Since:
            3.0
    """
    def __init__(self, oDEStepEndHandler: typing.Union[ODEStepEndHandler, typing.Callable]): ...
    def doEvent(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> EventOccurrence:
        """
            Notify the user's listener of the event. The event occurs wholly within this method call including a call to
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.resetState` if necessary.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventState.doEvent` in interface :class:`~org.hipparchus.ode.events.EventState`
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): the state at the time of the event. This must be at the same time as the current value of
                    :meth:`~org.hipparchus.ode.events.EventState.getEventTime`.
        
            Returns:
                the user's requested action and the new state if the action is :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`.
                Otherwise the new state is :code:`state`. The stop time indicates what time propagation should stop if the action is
                :meth:`~org.hipparchus.ode.events.Action.STOP`. This guarantees the integration will stop on or after the root, so that
                integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool:
        """
            Evaluate the impact of the proposed step on the handler.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventState.evaluateStep` in interface :class:`~org.hipparchus.ode.events.EventState`
        
            Parameters:
                interpolator (:class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`): step interpolator for the proposed step
        
            Returns:
                true if the event handler triggers an event before the end of the proposed step
        
        
        """
        ...
    def getEventTime(self) -> float:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventState.getEventTime` in interface :class:`~org.hipparchus.ode.events.EventState`
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def getHandler(self) -> ODEStepEndHandler:
        """
            Get the underlying step end handler.
        
            Returns:
                underlying step end handler
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize handler at the start of an integration.
        
            This method is called once at the start of the integration. It may be used by the handler to initialize some internal
            data if needed.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventState.init` in interface :class:`~org.hipparchus.ode.events.EventState`
        
            Parameters:
                s0 (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial state
                t (double): target time for the integration
        
        
        """
        ...
    def setStepEnd(self, double: float) -> None:
        """
            Set the step end.
        
            Parameters:
                stepEnd (double): step end
        
        
        """
        ...

_EventSlopeFilter__T = typing.TypeVar('_EventSlopeFilter__T', bound=ODEEventDetector)  # <T>
class EventSlopeFilter(AbstractODEDetector['EventSlopeFilter'[_EventSlopeFilter__T]], typing.Generic[_EventSlopeFilter__T]):
    """
    public classEventSlopeFilter<T extends :class:`~org.hipparchus.ode.events.ODEEventDetector`> extends :class:`~org.hipparchus.ode.events.AbstractODEDetector`<:class:`~org.hipparchus.ode.events.EventSlopeFilter`<T>>
    
        Wrapper used to detect only increasing or decreasing events.
    
        General :class:`~org.hipparchus.ode.events.ODEEventDetector` are defined implicitly by a
        :meth:`~org.hipparchus.ode.events.ODEEventDetector.g` crossing zero. This function needs to be continuous in the event
        neighborhood, and its sign must remain consistent between events. This implies that during an ODE integration, events
        triggered are alternately events for which the function increases from negative to positive values, and events for which
        the function decreases from positive to negative values.
    
        Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type.
        In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of
        computing time.
    
        Users can wrap a regular :class:`~org.hipparchus.ode.events.ODEEventDetector` in an instance of this class and provide
        this wrapping instance to the :class:`~org.hipparchus.ode.ODEIntegrator` in order to avoid wasting time looking for
        uninteresting events. The wrapper will intercept the calls to the :meth:`~org.hipparchus.ode.events.ODEEventDetector.g`
        and to the :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` method in order to ignore uninteresting
        events. The wrapped regular :class:`~org.hipparchus.ode.events.ODEEventHandler` will the see only the interesting
        events, i.e. either only :code:`increasing` events or :code:`decreasing` events. the number of calls to the
        :meth:`~org.hipparchus.ode.events.ODEEventDetector.g` will also be reduced.
    
        Since:
            3.0
    """
    def __init__(self, t: _EventSlopeFilter__T, filterType: FilterType): ...
    def g(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> float:
        """
            Compute the value of the switching function.
        
            The discrete events are generated when the sign of this switching function changes. The integrator will take care to
            change the stepsize in such a way these events occur exactly at step boundaries. The switching function must be
            continuous in its roots neighborhood (but not necessarily smooth), as the integrator will need to find its roots to
            locate precisely the events.
        
            Also note that for the integrator to detect an event the sign of the switching function must have opposite signs just
            before and after the event. If this consistency is not preserved the integrator may not detect any events.
        
            This need for consistency is sometimes tricky to achieve. A typical example is using an event to model a ball bouncing
            on the floor. The first idea to represent this would be to have :code:`g(state) = h(state)` where h is the height above
            the floor at time :code:`state.getTime()`. When :code:`g(state)` reaches 0, the ball is on the floor, so it should
            bounce and the typical way to do this is to reverse its vertical velocity. However, this would mean that before the
            event :code:`g(state)` was decreasing from positive values to 0, and after the event :code:`g(state)` would be
            increasing from 0 to positive values again. Consistency is broken here! The solution here is to have :code:`g(state) =
            sign * h(state)`, where sign is a variable with initial value set to :code:`+1`. Each time
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` is called, :code:`sign` is reset to :code:`-sign`. This
            allows the :code:`g(state)` function to remain continuous (and even smooth) even across events, despite :code:`h(state)`
            is not. Basically, the event is used to *fold* :code:`h(state)` at bounce points, and :code:`sign` is used to *unfold*
            it back, so the solvers sees a :code:`g(state)` function which behaves smoothly even across events.
        
            This method is idempotent, that is calling this multiple times with the same state will result in the same value, with
            two exceptions. First, the definition of the g function may change when an
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` on the handler, as in the above example. Second, the
            definition of the g function may change when the :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` method
            of any other event handler in the same integrator returns :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`,
            :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, or :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
        
            Returns:
                value of the g switching function
        
            Also see:
        
                  - :class:`~org.hipparchus.ode.events.package`
        
        
        
        """
        ...
    def getDetector(self) -> _EventSlopeFilter__T:
        """
            Get the wrapped raw detector.
        
            Returns:
                the wrapped raw detector
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize event detector at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the event detector to initialize some
            internal data if needed.
        
            The default implementation initializes the handler
        
            This implementation sets the direction of integration and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventDetector.init` in
                interface :class:`~org.hipparchus.ode.events.ODEEventDetector`
        
            Overrides:
                :meth:`~org.hipparchus.ode.events.AbstractODEDetector.init` in
                class :class:`~org.hipparchus.ode.events.AbstractODEDetector`
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                finalTime (double): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
            Check if the current propagation is forward or backward.
        
            Overrides:
                :meth:`~org.hipparchus.ode.events.AbstractODEDetector.isForward` in
                class :class:`~org.hipparchus.ode.events.AbstractODEDetector`
        
            Returns:
                true if the current propagation is forward
        
        
        """
        ...
    def reset(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Reset event detector during integration.
        
            This method is called during integration if the derivatives or the state variables themselves are reset.
        
            The default implementation does nothing.
        
            Parameters:
                intermediateState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): intermediate time, state vector and derivative
                finalTime (double): target time for the integration
        
        
        """
        ...

_FieldEventSlopeFilter__T = typing.TypeVar('_FieldEventSlopeFilter__T', bound=FieldODEEventDetector)  # <T>
_FieldEventSlopeFilter__E = typing.TypeVar('_FieldEventSlopeFilter__E', bound=org.hipparchus.CalculusFieldElement)  # <E>
class FieldEventSlopeFilter(AbstractFieldODEDetector['FieldEventSlopeFilter'[_FieldEventSlopeFilter__T, _FieldEventSlopeFilter__E], _FieldEventSlopeFilter__E], typing.Generic[_FieldEventSlopeFilter__T, _FieldEventSlopeFilter__E]):
    """
    public classFieldEventSlopeFilter<T extends :class:`~org.hipparchus.ode.events.FieldODEEventDetector`<E>,E extends :class:`~org.hipparchus.ode.events.https:.www.hipparchus.org.hipparchus`<E>> extends :class:`~org.hipparchus.ode.events.AbstractFieldODEDetector`<:class:`~org.hipparchus.ode.events.FieldEventSlopeFilter`<T,E>,E>
    
        Wrapper used to detect only increasing or decreasing events.
    
        General :class:`~org.hipparchus.ode.events.FieldODEEventDetector` are defined implicitly by a
        :meth:`~org.hipparchus.ode.events.FieldODEEventDetector.g` crossing zero. This function needs to be continuous in the
        event neighborhood, and its sign must remain consistent between events. This implies that during an ODE integration,
        events triggered are alternately events for which the function increases from negative to positive values, and events
        for which the function decreases from positive to negative values.
    
        Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type.
        In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of
        computing time.
    
        Users can wrap a regular :class:`~org.hipparchus.ode.events.FieldODEEventDetector` in an instance of this class and
        provide this wrapping instance to the :class:`~org.hipparchus.ode.FieldODEIntegrator` in order to avoid wasting time
        looking for uninteresting events. The wrapper will intercept the calls to the
        :meth:`~org.hipparchus.ode.events.FieldODEEventDetector.g` and to the
        :meth:`~org.hipparchus.ode.events.FieldODEEventHandler.eventOccurred` method in order to ignore uninteresting events.
        The wrapped regular :class:`~org.hipparchus.ode.events.FieldODEEventDetector` will the see only the interesting events,
        i.e. either only :code:`increasing` events or :code:`decreasing` events. the number of calls to the
        :meth:`~org.hipparchus.ode.events.FieldODEEventDetector.g` will also be reduced.
    
        Since:
            3.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldEventSlopeFilter__E], t: _FieldEventSlopeFilter__T, filterType: FilterType): ...
    def g(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventSlopeFilter__E]) -> _FieldEventSlopeFilter__E: ...
    def getDetector(self) -> _FieldEventSlopeFilter__T:
        """
            Get the wrapped raw detector.
        
            Returns:
                the wrapped raw detector
        
        
        """
        ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventSlopeFilter__E], e: _FieldEventSlopeFilter__E) -> None: ...
    def isForward(self) -> bool:
        """
            Check if the current propagation is forward or backward.
        
            Overrides:
                :meth:`~org.hipparchus.ode.events.AbstractFieldODEDetector.isForward` in
                class :class:`~org.hipparchus.ode.events.AbstractFieldODEDetector`
        
            Returns:
                true if the current propagation is forward
        
        
        """
        ...
    def reset(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventSlopeFilter__E], e: _FieldEventSlopeFilter__E) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.ode.events")``.

    AbstractFieldODEDetector: typing.Type[AbstractFieldODEDetector]
    AbstractODEDetector: typing.Type[AbstractODEDetector]
    Action: typing.Type[Action]
    AdaptableInterval: typing.Type[AdaptableInterval]
    DetectorBasedEventState: typing.Type[DetectorBasedEventState]
    EventOccurrence: typing.Type[EventOccurrence]
    EventSlopeFilter: typing.Type[EventSlopeFilter]
    EventState: typing.Type[EventState]
    FieldAdaptableInterval: typing.Type[FieldAdaptableInterval]
    FieldDetectorBasedEventState: typing.Type[FieldDetectorBasedEventState]
    FieldEventOccurrence: typing.Type[FieldEventOccurrence]
    FieldEventSlopeFilter: typing.Type[FieldEventSlopeFilter]
    FieldEventState: typing.Type[FieldEventState]
    FieldODEEventDetector: typing.Type[FieldODEEventDetector]
    FieldODEEventHandler: typing.Type[FieldODEEventHandler]
    FieldODEStepEndHandler: typing.Type[FieldODEStepEndHandler]
    FieldStepEndEventState: typing.Type[FieldStepEndEventState]
    FilterType: typing.Type[FilterType]
    ODEEventDetector: typing.Type[ODEEventDetector]
    ODEEventHandler: typing.Type[ODEEventHandler]
    ODEStepEndHandler: typing.Type[ODEStepEndHandler]
    StepEndEventState: typing.Type[StepEndEventState]
