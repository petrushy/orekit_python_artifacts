
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
    def valueOf(name: str) -> 'Action':
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
    def values() -> typing.MutableSequence['Action']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (Action c : Action.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdaptableInterval:
    """
    This interface represents an event checking interval that depends on state.
    
    Since:
        3.0
    
    Also see:
        ODEEventDetector
    """
    def currentInterval(self, state: org.hipparchus.ode.ODEStateAndDerivative, isForward: bool) -> float:
        """
        Get the current value of maximal time interval between events handler checks.
        
        Parameters:
            state (ODEStateAndDerivative): current state
            isForward (boolean): true if propagation is forward in independent variable, false otherwise
        
        Returns:
            current value of maximal time interval between events handler checks
        
        
        """
        ...
    @staticmethod
    def of(maxCheck: float) -> 'AdaptableInterval':
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
    Class to hold the data related to an event occurrence that is needed to decide how to modify integration.
    
    Since:
        3.O
    """
    def __init__(self, action: Action, newState: org.hipparchus.ode.ODEState, stopTime: float):
        """
        Create a new occurrence of an event.
        
        Parameters:
            action (Action): the user requested action.
            newState (ODEState): for a reset event. Should be the current state unless the action is
                RESET_STATE.
            stopTime (double): to stop propagation if the action is STOP. Used to move the stop time to just
                after the root.
        
        
        """
        ...
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
    This interface handles the state for either one ODEEventHandler or one ODEStepEndHandler during integration steps.
    
    Since:
        3.0
    """
    def doEvent(self, state: org.hipparchus.ode.ODEStateAndDerivative) -> EventOccurrence:
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Parameters:
            state (ODEStateAndDerivative): the state at the time of the event. This must be at the same time as the current value of
                getEventTime.
        
        Returns:
            the user's requested action and the new state if the action is RESET_STATE.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            STOP. This guarantees the integration will stop on or after the root, so that
            integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool:
        """
        Evaluate the impact of the proposed step on the handler.
        
        Parameters:
            interpolator (ODEStateInterpolator): step interpolator for the proposed step
        
        Returns:
            true if the event handler triggers an event before the end of the proposed step
        
        Raises:
            hipparchus: if the interpolator throws one because the number of functions evaluations is exceeded
            hipparchus: if the event cannot be bracketed
        
        
        """
        ...
    def getEventTime(self) -> float:
        """
        Get the occurrence time of the event triggered in the current step.
        
        Returns:
            occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, s0: org.hipparchus.ode.ODEStateAndDerivative, t: float) -> None:
        """
        Initialize handler at the start of an integration.
        
        This method is called once at the start of the integration. It may be used by the handler to initialize some internal data if needed.
        
        Parameters:
            s0 (ODEStateAndDerivative): initial state
            t (double): target time for the integration
        
        
        """
        ...

_FieldAdaptableInterval__T = typing.TypeVar('_FieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdaptableInterval(typing.Generic[_FieldAdaptableInterval__T]):
    """
    This interface represents an event checking interval that depends on state.
    
    Since:
        3.0
    
    Also see:
        ODEEventDetector
    """
    def currentInterval(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldAdaptableInterval__T], isForward: bool) -> float:
        """
        Get the current value of maximal time interval between events handler checks.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldAdaptableInterval> state): current state
            isForward (boolean): true if propagation is forward in independent variable, false otherwise
        
        Returns:
            current value of maximal time interval between events handler checks (only as a double)
        
        
        """
        ...
    _of__W = typing.TypeVar('_of__W', bound=org.hipparchus.CalculusFieldElement)  # <W>
    @staticmethod
    def of(maxCheck: float) -> 'FieldAdaptableInterval'[_of__W]:
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
    Class to hold the data related to an event occurrence that is needed to decide how to modify integration.
    """
    def __init__(self, action: Action, newState: org.hipparchus.ode.FieldODEState[_FieldEventOccurrence__T], stopTime: _FieldEventOccurrence__T):
        """
        Create a new occurrence of an event.
        
        Parameters:
            action (Action): the user requested action.
            newState (FieldODEState<FieldEventOccurrence> newState): for a reset event. Should be the current state unless the action is
                RESET_STATE.
            stopTime (FieldEventOccurrence): to stop propagation if the action is STOP. Used to move the stop time to just
                after the root.
        
        
        """
        ...
    def getAction(self) -> Action:
        """
        Get the user requested action.
        
        Returns:
            the action.
        
        
        """
        ...
    def getNewState(self) -> org.hipparchus.ode.FieldODEState[_FieldEventOccurrence__T]:
        """
        Get the new state for a reset action.
        
        Returns:
            the new state.
        
        
        """
        ...
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
    This interface handles the state for either one FieldODEEventHandler or one FieldODEStepEndHandler during integration steps.
    
    Since:
        3.0
    """
    def doEvent(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T]) -> FieldEventOccurrence[_FieldEventState__T]:
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldEventState> state): the state at the time of the event. This must be at the same time as the current value of
                getEventTime.
        
        Returns:
            the user's requested action and the new state if the action is RESET_STATE.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            STOP. This guarantees the integration will stop on or after the root, so that
            integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> bool:
        """
        Evaluate the impact of the proposed step on the event handler.
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldEventState> interpolator): step interpolator for the proposed step
        
        Returns:
            true if the event handler triggers an event before the end of the proposed step
        
        Raises:
            hipparchus: if the interpolator throws one because the number of functions evaluations is exceeded
            hipparchus: if the event cannot be bracketed
        
        
        """
        ...
    def getEventTime(self) -> _FieldEventState__T:
        """
        Get the occurrence time of the event triggered in the current step.
        
        Returns:
            occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, s0: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T], t: _FieldEventState__T) -> None:
        """
        Initialize handler at the start of an integration.
        
        This method is called once at the start of the integration. It may be used by the event handler to initialize some internal data if needed.
        
        Parameters:
            s0 (FieldODEStateAndDerivative<FieldEventState> s0): initial state
            t (FieldEventState): target time for the integration
        
        
        """
        ...

_FieldODEEventDetector__T = typing.TypeVar('_FieldODEEventDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEEventDetector(typing.Generic[_FieldODEEventDetector__T]):
    """
    This interface represents a handler for discrete events triggered during ODE integration.
    
    Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when the derivatives have states boundaries crossings.
    
    These events are defined as occurring when a g switching function sign changes.
    
    Since events are only problem-dependent and are triggered by the independent time variable and the state vector, they can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the local error (this event handling feature is available for all integrators, including fixed step ones).
    
    Note that prior to Hipparchus 3.0, the methods in this interface were in the FieldODEEventHandler interface and the defunct FieldEventHandlerConfiguration interface. The interfaces have been reorganized to allow different objects to be used in event detection and event handling, hence allowing users to reuse predefined events detectors with custom handlers.
    
    Since:
        3.0
    
    Also see:
        package
    """
    def g(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventDetector__T]) -> _FieldODEEventDetector__T:
        """
        Compute the value of the switching function.
        
        The discrete events are generated when the sign of this switching function changes. The integrator will take care to change the stepsize in such a way these events occur exactly at step boundaries. The switching function must be continuous in its roots neighborhood (but not necessarily smooth), as the integrator will need to find its roots to locate precisely the events.
        
        Also note that the integrator expect that once an event has occurred, the sign of the switching function at the start of the next step (i.e. just after the event) is the opposite of the sign just before the event. This consistency between the steps must be preserved, otherwise hipparchus related to root not being bracketed will occur.
        
        This need for consistency is sometimes tricky to achieve. A typical example is using an event to model a ball bouncing on the floor. The first idea to represent this would be to have g(state) = h(state) where h is the height above the floor at time getTime(). When g(state) reaches 0, the ball is on the floor, so it should bounce and the typical way to do this is to reverse its vertical velocity. However, this would mean that before the event g(state) was decreasing from positive values to 0, and after the event g(state) would be increasing from 0 to positive values again. Consistency is broken here! The solution here is to have g(state) = sign * h(state), where sign is a variable with initial value set to +1. Each time eventOccurred method is called, sign is reset to -sign. This allows the g(state) function to remain continuous (and even smooth) even across events, despite h(state) is not. Basically, the event is used to fold h(state) at bounce points, and sign is used to unfold it back, so the solvers sees a g(state) function which behaves smoothly even across events.
        
        This method is idempotent, that is calling this multiple times with the same state will result in the same value, with two exceptions. First, the definition of the g function may change when an eventOccurred on the handler, as in the above example. Second, the definition of the g function may change when the eventOccurred method of any other event handler in the same integrator returns RESET_EVENTS, RESET_DERIVATIVES, or RESET_STATE.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldODEEventDetector> state): current value of the independent time variable, state vector and derivative
        
        Returns:
            value of the g switching function
        
        
        """
        ...
    def getHandler(self) -> 'FieldODEEventHandler'[_FieldODEEventDetector__T]:
        """
        Get the underlying event handler.
        
        Returns:
            underlying event handler
        
        
        """
        ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_FieldODEEventDetector__T]:
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
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldODEEventDetector__T]:
        """
        Get the root-finding algorithm to use to detect state events.
        
        Returns:
            root-finding algorithm to use to detect state events
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventDetector__T], finalTime: _FieldODEEventDetector__T) -> None:
        """
        Initialize event detector at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldODEEventDetector> initialState): initial time, state vector and derivative
            finalTime (FieldODEEventDetector): target time for the integration
        
        
        """
        ...
    def reset(self, intermediateState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventDetector__T], finalTime: _FieldODEEventDetector__T) -> None:
        """
        Reset event detector during integration.
        
        This method is called during integration if the derivatives or the state variables themselves are reset.
        
        The default implementation does nothing.
        
        Parameters:
            intermediateState (FieldODEStateAndDerivative<FieldODEEventDetector> intermediateState): intermediate time, state vector and derivative
            finalTime (FieldODEEventDetector): target time for the integration
        
        Since:
            4.0
        
        
        """
        ...

_FieldODEEventHandler__T = typing.TypeVar('_FieldODEEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEEventHandler(typing.Generic[_FieldODEEventHandler__T]):
    """
    This interface represents a handler for discrete events triggered during ODE integration.
    
    Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when the derivatives have states boundaries crossings.
    
    These events are defined as occurring when a g switching function sign changes.
    
    Since events are only problem-dependent and are triggered by the independent time variable and the state vector, they can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the local error (this event handling feature is available for all integrators, including fixed step ones).
    
    Note that prior to Hipparchus 3.0, some of the methods that are now in FieldODEEventDetector were in this interface (and the remaining ones were in the defunct FieldEventHandlerConfiguration interface). The interfaces have been reorganized to allow different objects to be used in event detection and event handling, hence allowing users to reuse predefined events detectors with custom handlers.
    
    Also see:
        package
    """
    def eventOccurred(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], detector: FieldODEEventDetector[_FieldODEEventHandler__T], increasing: bool) -> Action:
        """
        Handle an event and choose what to do next.
        
        This method is called when the integrator has accepted a step ending exactly on a sign change of the function, just after the step handler itself is called (see below for scheduling). It allows the user to update his internal data to acknowledge the fact the event has been handled (for example setting a flag in the FieldOrdinaryDifferentialEquation to switch the derivatives computation in case of discontinuity), or to direct the integrator to either stop or continue integration, possibly with a reset state or derivatives.
        
          - if STOP is returned, the integration will be stopped,
          - if RESET_STATE is returned, the
            resetState method will be called once the step handler has
            finished its task, and the integrator will also recompute the derivatives,
          - if RESET_DERIVATIVES is returned, the integrator will recompute the
            derivatives,
          - if RESET_EVENTS is returned, the integrator will recheck all event handlers,
          - if CONTINUE is returned, no specific action will be taken (apart from having
            called this method) and integration will continue.
        
        The scheduling between this method and the FieldODEStepHandler method handleStep is to call handleStep first and this method afterwards (this scheduling changed as of Hipparchus 2.0). This scheduling allows user code called by this method and user code called by step handlers to get values of the independent time variable consistent with integration direction.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldODEEventHandler> state): current value of the independent time variable, state vector and derivative
            detector (FieldODEEventDetector<FieldODEEventHandler> detector): detector that triggered the event
            increasing (boolean): if true, the value of the switching function increases when times increases around event (note that increase is measured
                with respect to physical time, not with respect to integration which may go backward in time)
        
        Returns:
            indication of what the integrator should do next, this value must be one of
            STOP, RESET_STATE,
            RESET_DERIVATIVES, RESET_EVENTS, or
            CONTINUE
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], finalTime: _FieldODEEventHandler__T, detector: FieldODEEventDetector[_FieldODEEventHandler__T]) -> None:
        """
        Initialize event handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldODEEventHandler> initialState): initial time, state vector and derivative
            finalTime (FieldODEEventHandler): target time for the integration
            detector (FieldODEEventDetector<FieldODEEventHandler> detector): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, detector: FieldODEEventDetector[_FieldODEEventHandler__T], state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T]) -> org.hipparchus.ode.FieldODEState[_FieldODEEventHandler__T]:
        """
        Reset the state prior to continue the integration.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the RESET_STATE indicator. It allows the user to reset the state vector for the next step, without perturbing the step handler of the finishing step.
        
        The default implementation returns its argument.
        
        Parameters:
            detector (FieldODEEventDetector<FieldODEEventHandler> detector): detector that triggered the event
            state (FieldODEStateAndDerivative<FieldODEEventHandler> state): current value of the independent time variable, state vector and derivative
        
        Returns:
            reset state (note that it does not include the derivatives, they will be added automatically by the integrator
            afterwards)
        
        
        """
        ...

_FieldODEStepEndHandler__T = typing.TypeVar('_FieldODEStepEndHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStepEndHandler(typing.Generic[_FieldODEStepEndHandler__T]):
    """
    This interface represents a handler for discrete events triggered during ODE integration at each step end.
    
    Since:
        3.0
    
    Also see:
        package
    """
    def init(self, initialState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepEndHandler__T], finalTime: _FieldODEStepEndHandler__T) -> None:
        """
        Initialize step end handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step end handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldODEStepEndHandler> initialState): initial time, state vector and derivative
            finalTime (FieldODEStepEndHandler): target time for the integration
        
        
        """
        ...
    def resetState(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepEndHandler__T]) -> org.hipparchus.ode.FieldODEState[_FieldODEStepEndHandler__T]:
        """
        Reset the state prior to continue the integration.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the RESET_STATE indicator. It allows the user to reset the state vector for the next step, without perturbing the step handler of the finishing step.
        
        The default implementation returns its argument.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldODEStepEndHandler> state): current value of the independent time variable, state vector and derivative at step end
        
        Returns:
            reset state (note that it does not include the derivatives, they will be added automatically by the integrator
            afterwards)
        
        
        """
        ...
    def stepEndOccurred(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepEndHandler__T], forward: bool) -> Action:
        """
        Handle an event and choose what to do next.
        
        This method is called when the integrator has accepted a step ending exactly on step end, just after the step handler itself is called (see below for scheduling). It allows the user to update his internal data to acknowledge the fact the event has been handled (for example setting a flag in the OrdinaryDifferentialEquation to switch the derivatives computation in case of discontinuity), or to direct the integrator to either stop or continue integration, possibly with a reset state or derivatives.
        
          - if STOP is returned, the integration will be stopped,
          - if RESET_STATE is returned, the
            resetState method will be called once the step handler has
            finished its task, and the integrator will also recompute the derivatives,
          - if RESET_DERIVATIVES is returned, the integrator will recompute the
            derivatives,
          - if RESET_EVENTS is returned, the integrator will recheck all event handlers,
          - if CONTINUE is returned, no specific action will be taken (apart from having
            called this method) and integration will continue.
        
        The scheduling between this method and the FieldODEStepHandler method handleStep is to call handleStep first and this method afterwards. This scheduling allows user code called by this method and user code called by step handlers to get values of the independent time variable consistent with integration direction.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldODEStepEndHandler> state): current value of the independent time variable, state vector and derivative at step end
            forward (boolean): if true, propagation is forward
        
        Returns:
            indication of what the integrator should do next, this value must be one of
            STOP, RESET_STATE,
            RESET_DERIVATIVES, RESET_EVENTS, or
            CONTINUE
        
        
        """
        ...

class FilterType(java.lang.Enum['FilterType']):
    """
    Enumerate for EventSlopeFilter.
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

class ODEEventDetector:
    """
    This interface represents a detector for discrete events triggered during ODE integration.
    
    Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when the derivatives have discontinuities, or simply when the user wants to monitor some states boundaries crossings.
    
    These events are defined as occurring when a g switching function sign changes.
    
    Since events are only problem-dependent and are triggered by the independent time variable and the state vector, they can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the local error (this event handling feature is available for all integrators, including fixed step ones).
    
    Note that prior to Hipparchus 3.0, the methods in this interface were in the ODEEventHandler interface and the defunct EventHandlerConfiguration interface. The interfaces have been reorganized to allow different objects to be used in event detection and event handling, hence allowing users to reuse predefined events detectors with custom handlers.
    
    Since:
        3.0
    
    Also see:
        package
    """
    def g(self, state: org.hipparchus.ode.ODEStateAndDerivative) -> float:
        """
        Compute the value of the switching function.
        
        The discrete events are generated when the sign of this switching function changes. The integrator will take care to change the stepsize in such a way these events occur exactly at step boundaries. The switching function must be continuous in its roots neighborhood (but not necessarily smooth), as the integrator will need to find its roots to locate precisely the events.
        
        Also note that for the integrator to detect an event the sign of the switching function must have opposite signs just before and after the event. If this consistency is not preserved the integrator may not detect any events.
        
        This need for consistency is sometimes tricky to achieve. A typical example is using an event to model a ball bouncing on the floor. The first idea to represent this would be to have g(state) = h(state) where h is the height above the floor at time getTime(). When g(state) reaches 0, the ball is on the floor, so it should bounce and the typical way to do this is to reverse its vertical velocity. However, this would mean that before the event g(state) was decreasing from positive values to 0, and after the event g(state) would be increasing from 0 to positive values again. Consistency is broken here! The solution here is to have g(state) = sign * h(state), where sign is a variable with initial value set to +1. Each time eventOccurred is called, sign is reset to -sign. This allows the g(state) function to remain continuous (and even smooth) even across events, despite h(state) is not. Basically, the event is used to fold h(state) at bounce points, and sign is used to unfold it back, so the solvers sees a g(state) function which behaves smoothly even across events.
        
        This method is idempotent, that is calling this multiple times with the same state will result in the same value, with two exceptions. First, the definition of the g function may change when an eventOccurred on the handler, as in the above example. Second, the definition of the g function may change when the eventOccurred method of any other event handler in the same integrator returns RESET_EVENTS, RESET_DERIVATIVES, or RESET_STATE.
        
        Parameters:
            state (ODEStateAndDerivative): current value of the independent time variable, state vector and derivative
        
        Returns:
            value of the g switching function
        
        Also see:
            package
        
        
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
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]:
        """
        Get the root-finding algorithm to use to detect state events.
        
        Returns:
            root-finding algorithm to use to detect state events
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Initialize event detector at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            finalTime (double): target time for the integration
        
        
        """
        ...
    def reset(self, intermediateState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Reset event detector during integration.
        
        This method is called during integration if the derivatives or the state variables themselves are reset.
        
        The default implementation does nothing.
        
        Parameters:
            intermediateState (ODEStateAndDerivative): intermediate time, state vector and derivative
            finalTime (double): target time for the integration
        
        Since:
            4.0
        
        
        """
        ...

class ODEEventHandler:
    """
    This interface represents a handler for discrete events triggered during ODE integration.
    
    Some events can be triggered at discrete times as an ODE problem is solved. This occurs for example when the integration process should be stopped as some state is reached (G-stop facility) when the precise date is unknown a priori, or when the derivatives have discontinuities, or simply when the user wants to monitor some states boundaries crossings.
    
    These events are defined as occurring when a g switching function sign changes.
    
    Since events are only problem-dependent and are triggered by the independent time variable and the state vector, they can occur at virtually any time, unknown in advance. The integrators will take care to avoid sign changes inside the steps, they will reduce the step size when such an event is detected in order to put this event exactly at the end of the current step. This guarantees that step interpolation (which always has a one step scope) is relevant even in presence of discontinuities. This is independent from the stepsize control provided by integrators that monitor the local error (this event handling feature is available for all integrators, including fixed step ones).
    
    Note that prior to Hipparchus 3.0, some of the methods that are now in ODEEventDetector were in this interface (and the remaining ones were in the defunct EventHandlerConfiguration interface). The interfaces have been reorganized to allow different objects to be used in event detection and event handling, hence allowing users to reuse predefined events detectors with custom handlers.
    
    Since:
        3.0
    
    Also see:
        package
    """
    def eventOccurred(self, state: org.hipparchus.ode.ODEStateAndDerivative, detector: ODEEventDetector, increasing: bool) -> Action:
        """
        Handle an event and choose what to do next.
        
        This method is called when the integrator has accepted a step ending exactly on a sign change of the function, just after the step handler itself is called (see below for scheduling). It allows the user to update his internal data to acknowledge the fact the event has been handled (for example setting a flag in the OrdinaryDifferentialEquation to switch the derivatives computation in case of discontinuity), or to direct the integrator to either stop or continue integration, possibly with a reset state or derivatives.
        
          - if STOP is returned, the integration will be stopped,
          - if RESET_STATE is returned, the
            resetState method will be called once the step handler has finished
            its task, and the integrator will also recompute the derivatives,
          - if RESET_DERIVATIVES is returned, the integrator will recompute the
            derivatives,
          - if RESET_EVENTS is returned, the integrator will recheck all event handlers,
          - if CONTINUE is returned, no specific action will be taken (apart from having
            called this method) and integration will continue.
        
        The scheduling between this method and the ODEStepHandler method handleStep is to call handleStep first and this method afterwards (this scheduling changed as of Hipparchus 2.0). This scheduling allows user code called by this method and user code called by step handlers to get values of the independent time variable consistent with integration direction.
        
        Parameters:
            state (ODEStateAndDerivative): current value of the independent time variable, state vector and derivative
            detector (ODEEventDetector): detector that triggered the event
            increasing (boolean): if true, the value of the switching function increases when times increases around event (note that increase is measured
                with respect to physical time, not with respect to integration which may go backward in time)
        
        Returns:
            indication of what the integrator should do next, this value must be one of
            STOP, RESET_STATE,
            RESET_DERIVATIVES, RESET_EVENTS, or
            CONTINUE
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float, detector: ODEEventDetector) -> None:
        """
        Initialize event handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            finalTime (double): target time for the integration
            detector (ODEEventDetector): event detector related to the event handler
        
        
        """
        ...
    def resetState(self, detector: ODEEventDetector, state: org.hipparchus.ode.ODEStateAndDerivative) -> org.hipparchus.ode.ODEState:
        """
        Reset the state prior to continue the integration.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the RESET_STATE indicator. It allows the user to reset the state vector for the next step, without perturbing the step handler of the finishing step.
        
        The default implementation returns its argument.
        
        Parameters:
            detector (ODEEventDetector): detector that triggered the event
            state (ODEStateAndDerivative): current value of the independent time variable, state vector and derivative
        
        Returns:
            reset state (note that it does not include the derivatives, they will be added automatically by the integrator
            afterwards)
        
        
        """
        ...

class ODEStepEndHandler:
    """
    This interface represents a handler for discrete events triggered during ODE integration at each step end.
    
    Since:
        3.0
    
    Also see:
        package
    """
    def init(self, initialState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Initialize step end handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step end handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            finalTime (double): target time for the integration
        
        
        """
        ...
    def resetState(self, state: org.hipparchus.ode.ODEStateAndDerivative) -> org.hipparchus.ode.ODEState:
        """
        Reset the state prior to continue the integration.
        
        This method is called after the step handler has returned and before the next step is started, but only when eventOccurred has itself returned the RESET_STATE indicator. It allows the user to reset the state vector for the next step, without perturbing the step handler of the finishing step.
        
        The default implementation returns its argument.
        
        Parameters:
            state (ODEStateAndDerivative): current value of the independent time variable, state vector and derivative at step end
        
        Returns:
            reset state (note that it does not include the derivatives, they will be added automatically by the integrator
            afterwards)
        
        
        """
        ...
    def stepEndOccurred(self, state: org.hipparchus.ode.ODEStateAndDerivative, forward: bool) -> Action:
        """
        Handle an event and choose what to do next.
        
        This method is called when the integrator has accepted a step ending exactly on step end, just after the step handler itself is called (see below for scheduling). It allows the user to update his internal data to acknowledge the fact the event has been handled (for example setting a flag in the OrdinaryDifferentialEquation to switch the derivatives computation in case of discontinuity), or to direct the integrator to either stop or continue integration, possibly with a reset state or derivatives.
        
          - if STOP is returned, the integration will be stopped,
          - if RESET_STATE is returned, the
            resetState method will be called once the step handler has finished
            its task, and the integrator will also recompute the derivatives,
          - if RESET_DERIVATIVES is returned, the integrator will recompute the
            derivatives,
          - if RESET_EVENTS is returned, the integrator will recheck all event handlers,
          - if CONTINUE is returned, no specific action will be taken (apart from having
            called this method) and integration will continue.
        
        The scheduling between this method and the ODEStepHandler method handleStep is to call handleStep first and this method afterwards. This scheduling allows user code called by this method and user code called by step handlers to get values of the independent time variable consistent with integration direction.
        
        Parameters:
            state (ODEStateAndDerivative): current value of the independent time variable, state vector and derivative at step end
            forward (boolean): if true, propagation is forward
        
        Returns:
            indication of what the integrator should do next, this value must be one of
            STOP, RESET_STATE,
            RESET_DERIVATIVES, RESET_EVENTS, or
            CONTINUE
        
        
        """
        ...

_AbstractFieldODEDetector__T = typing.TypeVar('_AbstractFieldODEDetector__T', bound='AbstractFieldODEDetector')  # <T>
_AbstractFieldODEDetector__E = typing.TypeVar('_AbstractFieldODEDetector__E', bound=org.hipparchus.CalculusFieldElement)  # <E>
class AbstractFieldODEDetector(FieldODEEventDetector[_AbstractFieldODEDetector__E], typing.Generic[_AbstractFieldODEDetector__T, _AbstractFieldODEDetector__E]):
    """
    Base class for #@link FieldODEEventDetector.
    
    Since:
        3.0
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
    def getHandler(self) -> FieldODEEventHandler[_AbstractFieldODEDetector__E]:
        """
        Get the underlying event handler.
        
        Specified by: getHandler in interface FieldODEEventDetector
        
        Returns:
            underlying event handler
        
        
        """
        ...
    def getMaxCheckInterval(self) -> FieldAdaptableInterval[_AbstractFieldODEDetector__E]:
        """
        Get the maximal time interval between events handler checks.
        
        Specified by: getMaxCheckInterval in interface FieldODEEventDetector
        
        Returns:
            maximal time interval between events handler checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Get the upper limit in the iteration count for event localization.
        
        Specified by: getMaxIterationCount in interface FieldODEEventDetector
        
        Returns:
            upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_AbstractFieldODEDetector__E]:
        """
        Get the root-finding algorithm to use to detect state events.
        
        Specified by: getSolver in interface FieldODEEventDetector
        
        Returns:
            root-finding algorithm to use to detect state events
        
        
        """
        ...
    def init(self, s0: org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEDetector__E], t: _AbstractFieldODEDetector__E) -> None:
        """
        Initialize event detector at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of integration and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface FieldODEEventDetector
        
        Parameters:
            s0 (FieldODEStateAndDerivative<AbstractFieldODEDetector> s0): initial time, state vector and derivative
            t (AbstractFieldODEDetector): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Returns:
            true if the current propagation is forward
        
        
        """
        ...
    def withHandler(self, newHandler: typing.Union[FieldODEEventHandler[_AbstractFieldODEDetector__E], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], FieldODEEventDetector[org.hipparchus.CalculusFieldElement], bool], Action]]) -> _AbstractFieldODEDetector__T:
        """
        Setup the event handler to call at event occurrences.
        
        This will override a handler if it has been configured previously.
        
        Parameters:
            newHandler (FieldODEEventHandler<AbstractFieldODEDetector> newHandler): event handler to call at event occurrences
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: _AbstractFieldODEDetector__E) -> _AbstractFieldODEDetector__T:
        """
        Setup the maximum checking interval.
        
        This will override a maximum checking interval if it has been configured previously.
        
        Parameters:
            newMaxCheck (AbstractFieldODEDetector): maximum checking interval (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        public AbstractFieldODEDetector withMaxCheck (FieldAdaptableInterval<AbstractFieldODEDetector> newMaxCheck)
        
        Setup the maximum checking interval.
        
        This will override a maximum checking interval if it has been configured previously.
        
        Parameters:
            newMaxCheck (FieldAdaptableInterval<AbstractFieldODEDetector> newMaxCheck): maximum checking interval (s)
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: typing.Union[FieldAdaptableInterval[_AbstractFieldODEDetector__E], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], float]]) -> _AbstractFieldODEDetector__T: ...
    def withMaxIter(self, newMaxIter: int) -> _AbstractFieldODEDetector__T:
        """
        Setup the maximum number of iterations in the event time search.
        
        This will override a number of iterations if it has been configured previously.
        
        Parameters:
            newMaxIter (int): maximum number of iterations in the event time search
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withSolver(self, newSolver: org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_AbstractFieldODEDetector__E]) -> _AbstractFieldODEDetector__T:
        """
        Setup the root-finding algorithm to use to detect state events.
        
        This will override a solver if it has been configured previously.
        
        Parameters:
            newSolver (hipparchus<AbstractFieldODEDetector> newSolver): root-finding algorithm to use to detect state events
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Also see:
            withThreshold
        
        
        """
        ...
    def withThreshold(self, newThreshold: _AbstractFieldODEDetector__E) -> _AbstractFieldODEDetector__T:
        """
        Setup the convergence threshold.
        
        This is equivalent to call withSolver(new FieldBracketingNthOrderBrentSolver<>(zero, newThreshold, zero, 5), so it will override a solver if one has been configured previously.
        
        Parameters:
            newThreshold (AbstractFieldODEDetector): convergence threshold
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Also see:
            withSolver
        
        
        """
        ...

_AbstractODEDetector__T = typing.TypeVar('_AbstractODEDetector__T', bound='AbstractODEDetector')  # <T>
class AbstractODEDetector(ODEEventDetector, typing.Generic[_AbstractODEDetector__T]):
    """
    Base class for #@link ODEEventDetector.
    
    Since:
        3.0
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
    def getHandler(self) -> ODEEventHandler:
        """
        Get the underlying event handler.
        
        Specified by: getHandler in interface ODEEventDetector
        
        Returns:
            underlying event handler
        
        
        """
        ...
    def getMaxCheckInterval(self) -> AdaptableInterval:
        """
        Get the maximal time interval between events handler checks.
        
        Specified by: getMaxCheckInterval in interface ODEEventDetector
        
        Returns:
            maximal time interval between events handler checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
        Get the upper limit in the iteration count for event localization.
        
        Specified by: getMaxIterationCount in interface ODEEventDetector
        
        Returns:
            upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]:
        """
        Get the root-finding algorithm to use to detect state events.
        
        Specified by: getSolver in interface ODEEventDetector
        
        Returns:
            root-finding algorithm to use to detect state events
        
        
        """
        ...
    def init(self, s0: org.hipparchus.ode.ODEStateAndDerivative, t: float) -> None:
        """
        Initialize event detector at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler
        
        This implementation sets the direction of integration and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface ODEEventDetector
        
        Parameters:
            s0 (ODEStateAndDerivative): initial time, state vector and derivative
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
    def withHandler(self, newHandler: typing.Union[ODEEventHandler, typing.Callable]) -> _AbstractODEDetector__T:
        """
        Setup the event handler to call at event occurrences.
        
        This will override a handler if it has been configured previously.
        
        Parameters:
            newHandler (ODEEventHandler): event handler to call at event occurrences
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: float) -> _AbstractODEDetector__T:
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
            newMaxCheck (AdaptableInterval): maximum checking interval
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    def withMaxCheck(self, newMaxCheck: typing.Union[AdaptableInterval, typing.Callable]) -> _AbstractODEDetector__T: ...
    def withMaxIter(self, newMaxIter: int) -> _AbstractODEDetector__T:
        """
        Setup the maximum number of iterations in the event time search.
        
        This will override a number of iterations if it has been configured previously.
        
        Parameters:
            newMaxIter (int): maximum number of iterations in the event time search
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withSolver(self, newSolver: org.hipparchus.analysis.solvers.BracketedUnivariateSolver[typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]]) -> _AbstractODEDetector__T:
        """
        Setup the root-finding algorithm to use to detect state events.
        
        This will override a solver if it has been configured previously.
        
        Parameters:
            newSolver (hipparchus<hipparchus> newSolver): root-finding algorithm to use to detect state events
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Also see:
            withThreshold
        
        
        """
        ...
    def withThreshold(self, newThreshold: float) -> _AbstractODEDetector__T:
        """
        Setup the convergence threshold.
        
        This is equivalent to call withSolver(new BracketingNthOrderBrentSolver(0, newThreshold, 0, 5)), so it will override a solver if one has been configured previously.
        
        Parameters:
            newThreshold (double): convergence threshold
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Also see:
            withSolver
        
        
        """
        ...

class DetectorBasedEventState(EventState):
    """
    This class handles the state for one ODEEventHandler during integration steps.
    
    Each time the integrator proposes a step, the event handler switching function should be checked. This class handles the state of one handler during one integration step, with references to the state at the end of the preceding step. This information is used to decide if the handler should trigger an event or not during the proposed step.
    """
    def __init__(self, detector: ODEEventDetector):
        """
        Simple constructor.
        
        Parameters:
            detector (ODEEventDetector): event detector
        
        Since:
            3.0
        
        
        """
        ...
    def doEvent(self, state: org.hipparchus.ode.ODEStateAndDerivative) -> EventOccurrence:
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Specified by: doEvent in interface EventState
        
        Parameters:
            state (ODEStateAndDerivative): the state at the time of the event. This must be at the same time as the current value of
                getEventTime.
        
        Returns:
            the user's requested action and the new state if the action is RESET_STATE.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            STOP. This guarantees the integration will stop on or after the root, so that
            integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool:
        """
        Evaluate the impact of the proposed step on the handler.
        
        Specified by: evaluateStep in interface EventState
        
        Parameters:
            interpolator (ODEStateInterpolator): step interpolator for the proposed step
        
        Returns:
            true if the event handler triggers an event before the end of the proposed step
        
        Raises:
            hipparchus: if the event cannot be bracketed
            hipparchus: if the interpolator throws one because the number of functions evaluations is exceeded
        
        
        """
        ...
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
        
        Specified by: getEventTime in interface EventState
        
        Returns:
            occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, s0: org.hipparchus.ode.ODEStateAndDerivative, t: float) -> None:
        """
        Initialize handler at the start of an integration.
        
        This method is called once at the start of the integration. It may be used by the handler to initialize some internal data if needed.
        
        Specified by: init in interface EventState
        
        Parameters:
            s0 (ODEStateAndDerivative): initial state
            t (double): target time for the integration
        
        
        """
        ...
    def reinitializeBegin(self, interpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> None:
        """
        Reinitialize the beginning of the step.
        
        Parameters:
            interpolator (ODEStateInterpolator): valid for the current step
        
        Raises:
            hipparchus: if the interpolator throws one because the number of functions evaluations is exceeded
        
        
        """
        ...
    def tryAdvance(self, state: org.hipparchus.ode.ODEStateAndDerivative, interpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool:
        """
        Try to accept the current history up to the given time.
        
        It is not necessary to call this method before calling doEvent with the same state. It is necessary to call this method before you call doEvent on some other event detector.
        
        Parameters:
            state (ODEStateAndDerivative): to try to accept.
            interpolator (ODEStateInterpolator): to use to find the new root, if any.
        
        Returns:
            if the event detector has an event it has not detected before that is on or before the same time as state. In
            other words false means continue on while true means stop and handle my event first.
        
        
        """
        ...

_FieldDetectorBasedEventState__T = typing.TypeVar('_FieldDetectorBasedEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDetectorBasedEventState(FieldEventState[_FieldDetectorBasedEventState__T], typing.Generic[_FieldDetectorBasedEventState__T]):
    """
    This class handles the state for one FieldODEEventHandler during integration steps.
    
    Each time the integrator proposes a step, the event handler switching function should be checked. This class handles the state of one handler during one integration step, with references to the state at the end of the preceding step. This information is used to decide if the handler should trigger an event or not during the proposed step.
    """
    def __init__(self, detector: FieldODEEventDetector[_FieldDetectorBasedEventState__T]):
        """
        Simple constructor.
        
        Parameters:
            detector (FieldODEEventDetector<FieldDetectorBasedEventState> detector): event detector
        
        Since:
            3.0
        
        
        """
        ...
    def doEvent(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldDetectorBasedEventState__T]) -> FieldEventOccurrence[_FieldDetectorBasedEventState__T]:
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Specified by: doEvent in interface FieldEventState
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldDetectorBasedEventState> state): the state at the time of the event. This must be at the same time as the current value of
                getEventTime.
        
        Returns:
            the user's requested action and the new state if the action is RESET_STATE.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            STOP. This guarantees the integration will stop on or after the root, so that
            integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDetectorBasedEventState__T]) -> bool:
        """
        Evaluate the impact of the proposed step on the event handler.
        
        Specified by: evaluateStep in interface FieldEventState
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldDetectorBasedEventState> interpolator): step interpolator for the proposed step
        
        Returns:
            true if the event handler triggers an event before the end of the proposed step
        
        Raises:
            hipparchus: if the interpolator throws one because the number of functions evaluations is exceeded
            hipparchus: if the event cannot be bracketed
        
        
        """
        ...
    def getEventDetector(self) -> FieldODEEventDetector[_FieldDetectorBasedEventState__T]:
        """
        Get the underlying event detector.
        
        Returns:
            underlying event detector
        
        Since:
            3.0
        
        
        """
        ...
    def getEventTime(self) -> _FieldDetectorBasedEventState__T:
        """
        Get the occurrence time of the event triggered in the current step.
        
        Specified by: getEventTime in interface FieldEventState
        
        Returns:
            occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def init(self, s0: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldDetectorBasedEventState__T], t: _FieldDetectorBasedEventState__T) -> None:
        """
        Initialize event handler at the start of an integration.
        
        This method is called once at the start of the integration. It may be used by the event handler to initialize some internal data if needed.
        
        Specified by: init in interface FieldEventState
        
        Parameters:
            s0 (FieldODEStateAndDerivative<FieldDetectorBasedEventState> s0): initial state
            t (FieldDetectorBasedEventState): target time for the integration
        
        
        """
        ...
    def reinitializeBegin(self, interpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDetectorBasedEventState__T]) -> None:
        """
        Reinitialize the beginning of the step.
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldDetectorBasedEventState> interpolator): valid for the current step
        
        Raises:
            hipparchus: if the interpolator throws one because the number of functions evaluations is exceeded
        
        
        """
        ...
    def tryAdvance(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldDetectorBasedEventState__T], interpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDetectorBasedEventState__T]) -> bool:
        """
        Try to accept the current history up to the given time.
        
        It is not necessary to call this method before calling doEvent with the same state. It is necessary to call this method before you call doEvent on some other event detector.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldDetectorBasedEventState> state): to try to accept.
            interpolator (FieldODEStateInterpolator<FieldDetectorBasedEventState> interpolator): to use to find the new root, if any.
        
        Returns:
            if the event detector has an event it has not detected before that is on or before the same time as state. In
            other words false means continue on while true means stop and handle my event first.
        
        
        """
        ...

_FieldStepEndEventState__T = typing.TypeVar('_FieldStepEndEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStepEndEventState(FieldEventState[_FieldStepEndEventState__T], typing.Generic[_FieldStepEndEventState__T]):
    """
    This class handles the state for one ODEEventHandler that triggers at step end.
    
    Since:
        3.0
    """
    def __init__(self, handler: typing.Union[FieldODEStepEndHandler[_FieldStepEndEventState__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], Action]]):
        """
        Simple constructor.
        
        Parameters:
            handler (FieldODEStepEndHandler<FieldStepEndEventState> handler): step end handler
        
        
        """
        ...
    def doEvent(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepEndEventState__T]) -> FieldEventOccurrence[_FieldStepEndEventState__T]:
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Specified by: doEvent in interface FieldEventState
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldStepEndEventState> state): the state at the time of the event. This must be at the same time as the current value of
                getEventTime.
        
        Returns:
            the user's requested action and the new state if the action is RESET_STATE.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            STOP. This guarantees the integration will stop on or after the root, so that
            integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldStepEndEventState__T]) -> bool:
        """
        Evaluate the impact of the proposed step on the event handler.
        
        Specified by: evaluateStep in interface FieldEventState
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldStepEndEventState> interpolator): step interpolator for the proposed step
        
        Returns:
            true if the event handler triggers an event before the end of the proposed step
        
        
        """
        ...
    def getEventTime(self) -> _FieldStepEndEventState__T:
        """
        Get the occurrence time of the event triggered in the current step.
        
        Specified by: getEventTime in interface FieldEventState
        
        Returns:
            occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def getHandler(self) -> FieldODEStepEndHandler[_FieldStepEndEventState__T]:
        """
        Get the underlying step end handler.
        
        Returns:
            underlying step end handler
        
        
        """
        ...
    def init(self, s0: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepEndEventState__T], t: _FieldStepEndEventState__T) -> None:
        """
        Initialize handler at the start of an integration.
        
        This method is called once at the start of the integration. It may be used by the event handler to initialize some internal data if needed.
        
        Specified by: init in interface FieldEventState
        
        Parameters:
            s0 (FieldODEStateAndDerivative<FieldStepEndEventState> s0): initial state
            t (FieldStepEndEventState): target time for the integration
        
        
        """
        ...
    def setStepEnd(self, stepEnd: _FieldStepEndEventState__T) -> None:
        """
        Set the step end.
        
        Parameters:
            stepEnd (FieldStepEndEventState): step end
        
        
        """
        ...

class StepEndEventState(EventState):
    """
    This class handles the state for one ODEEventHandler that triggers at step end.
    
    Since:
        3.0
    """
    def __init__(self, handler: typing.Union[ODEStepEndHandler, typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            handler (ODEStepEndHandler): step end handler
        
        
        """
        ...
    def doEvent(self, state: org.hipparchus.ode.ODEStateAndDerivative) -> EventOccurrence:
        """
        Notify the user's listener of the event. The event occurs wholly within this method call including a call to resetState if necessary.
        
        Specified by: doEvent in interface EventState
        
        Parameters:
            state (ODEStateAndDerivative): the state at the time of the event. This must be at the same time as the current value of
                getEventTime.
        
        Returns:
            the user's requested action and the new state if the action is RESET_STATE.
            Otherwise the new state is state. The stop time indicates what time propagation should stop if the action is
            STOP. This guarantees the integration will stop on or after the root, so that
            integration may be restarted safely.
        
        
        """
        ...
    def evaluateStep(self, interpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool:
        """
        Evaluate the impact of the proposed step on the handler.
        
        Specified by: evaluateStep in interface EventState
        
        Parameters:
            interpolator (ODEStateInterpolator): step interpolator for the proposed step
        
        Returns:
            true if the event handler triggers an event before the end of the proposed step
        
        
        """
        ...
    def getEventTime(self) -> float:
        """
        Get the occurrence time of the event triggered in the current step.
        
        Specified by: getEventTime in interface EventState
        
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
    def init(self, s0: org.hipparchus.ode.ODEStateAndDerivative, t: float) -> None:
        """
        Initialize handler at the start of an integration.
        
        This method is called once at the start of the integration. It may be used by the handler to initialize some internal data if needed.
        
        Specified by: init in interface EventState
        
        Parameters:
            s0 (ODEStateAndDerivative): initial state
            t (double): target time for the integration
        
        
        """
        ...
    def setStepEnd(self, stepEnd: float) -> None:
        """
        Set the step end.
        
        Parameters:
            stepEnd (double): step end
        
        
        """
        ...

_EventSlopeFilter__T = typing.TypeVar('_EventSlopeFilter__T', bound=ODEEventDetector)  # <T>
class EventSlopeFilter(AbstractODEDetector['EventSlopeFilter'[_EventSlopeFilter__T]], typing.Generic[_EventSlopeFilter__T]):
    """
    Wrapper used to detect only increasing or decreasing events.
    
    General ODEEventDetector are defined implicitly by a g crossing zero. This function needs to be continuous in the event neighborhood, and its sign must remain consistent between events. This implies that during an ODE integration, events triggered are alternately events for which the function increases from negative to positive values, and events for which the function decreases from positive to negative values.
    
    Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type. In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of computing time.
    
    Users can wrap a regular ODEEventDetector in an instance of this class and provide this wrapping instance to the ODEIntegrator in order to avoid wasting time looking for uninteresting events. The wrapper will intercept the calls to the g and to the eventOccurred method in order to ignore uninteresting events. The wrapped regular ODEEventHandler will the see only the interesting events, i.e. either only increasing events or decreasing events. the number of calls to the g will also be reduced.
    
    Since:
        3.0
    """
    def __init__(self, rawDetector: _EventSlopeFilter__T, filter: FilterType):
        """
        Wrap an ODEEventDetector.
        
        Parameters:
            rawDetector (EventSlopeFilter): event detector to wrap
            filter (FilterType): filter to use
        
        Since:
            3.0
        
        
        """
        ...
    def g(self, state: org.hipparchus.ode.ODEStateAndDerivative) -> float:
        """
        Compute the value of the switching function.
        
        The discrete events are generated when the sign of this switching function changes. The integrator will take care to change the stepsize in such a way these events occur exactly at step boundaries. The switching function must be continuous in its roots neighborhood (but not necessarily smooth), as the integrator will need to find its roots to locate precisely the events.
        
        Also note that for the integrator to detect an event the sign of the switching function must have opposite signs just before and after the event. If this consistency is not preserved the integrator may not detect any events.
        
        This need for consistency is sometimes tricky to achieve. A typical example is using an event to model a ball bouncing on the floor. The first idea to represent this would be to have g(state) = h(state) where h is the height above the floor at time getTime(). When g(state) reaches 0, the ball is on the floor, so it should bounce and the typical way to do this is to reverse its vertical velocity. However, this would mean that before the event g(state) was decreasing from positive values to 0, and after the event g(state) would be increasing from 0 to positive values again. Consistency is broken here! The solution here is to have g(state) = sign * h(state), where sign is a variable with initial value set to +1. Each time eventOccurred is called, sign is reset to -sign. This allows the g(state) function to remain continuous (and even smooth) even across events, despite h(state) is not. Basically, the event is used to fold h(state) at bounce points, and sign is used to unfold it back, so the solvers sees a g(state) function which behaves smoothly even across events.
        
        This method is idempotent, that is calling this multiple times with the same state will result in the same value, with two exceptions. First, the definition of the g function may change when an eventOccurred on the handler, as in the above example. Second, the definition of the g function may change when the eventOccurred method of any other event handler in the same integrator returns RESET_EVENTS, RESET_DERIVATIVES, or RESET_STATE.
        
        Parameters:
            state (ODEStateAndDerivative): current value of the independent time variable, state vector and derivative
        
        Returns:
            value of the g switching function
        
        Also see:
            package
        
        
        """
        ...
    def getDetector(self) -> _EventSlopeFilter__T:
        """
        Get the wrapped raw detector.
        
        Returns:
            the wrapped raw detector
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Initialize event detector at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler
        
        This implementation sets the direction of integration and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface ODEEventDetector
        
        Overrides: init in class AbstractODEDetector
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            finalTime (double): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Overrides: isForward in class AbstractODEDetector
        
        Returns:
            true if the current propagation is forward
        
        
        """
        ...
    def reset(self, intermediateState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Reset event detector during integration.
        
        This method is called during integration if the derivatives or the state variables themselves are reset.
        
        The default implementation does nothing.
        
        Parameters:
            intermediateState (ODEStateAndDerivative): intermediate time, state vector and derivative
            finalTime (double): target time for the integration
        
        
        """
        ...

_FieldEventSlopeFilter__T = typing.TypeVar('_FieldEventSlopeFilter__T', bound=FieldODEEventDetector)  # <T>
_FieldEventSlopeFilter__E = typing.TypeVar('_FieldEventSlopeFilter__E', bound=org.hipparchus.CalculusFieldElement)  # <E>
class FieldEventSlopeFilter(AbstractFieldODEDetector['FieldEventSlopeFilter'[_FieldEventSlopeFilter__T, _FieldEventSlopeFilter__E], _FieldEventSlopeFilter__E], typing.Generic[_FieldEventSlopeFilter__T, _FieldEventSlopeFilter__E]):
    """
    Wrapper used to detect only increasing or decreasing events.
    
    General FieldODEEventDetector are defined implicitly by a g crossing zero. This function needs to be continuous in the event neighborhood, and its sign must remain consistent between events. This implies that during an ODE integration, events triggered are alternately events for which the function increases from negative to positive values, and events for which the function decreases from positive to negative values.
    
    Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type. In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of computing time.
    
    Users can wrap a regular FieldODEEventDetector in an instance of this class and provide this wrapping instance to the FieldODEIntegrator in order to avoid wasting time looking for uninteresting events. The wrapper will intercept the calls to the g and to the eventOccurred method in order to ignore uninteresting events. The wrapped regular FieldODEEventDetector will the see only the interesting events, i.e. either only increasing events or decreasing events. the number of calls to the g will also be reduced.
    
    Since:
        3.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldEventSlopeFilter__E], rawDetector: _FieldEventSlopeFilter__T, filter: FilterType):
        """
        Wrap a FieldODEEventDetector.
        
        Parameters:
            field (hipparchus<FieldEventSlopeFilter> field): field to which array elements belong
            rawDetector (FieldEventSlopeFilter): event detector to wrap
            filter (FilterType): filter to use
        
        
        """
        ...
    def g(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventSlopeFilter__E]) -> _FieldEventSlopeFilter__E:
        """
        Compute the value of the switching function.
        
        The discrete events are generated when the sign of this switching function changes. The integrator will take care to change the stepsize in such a way these events occur exactly at step boundaries. The switching function must be continuous in its roots neighborhood (but not necessarily smooth), as the integrator will need to find its roots to locate precisely the events.
        
        Also note that the integrator expect that once an event has occurred, the sign of the switching function at the start of the next step (i.e. just after the event) is the opposite of the sign just before the event. This consistency between the steps must be preserved, otherwise hipparchus related to root not being bracketed will occur.
        
        This need for consistency is sometimes tricky to achieve. A typical example is using an event to model a ball bouncing on the floor. The first idea to represent this would be to have g(state) = h(state) where h is the height above the floor at time getTime(). When g(state) reaches 0, the ball is on the floor, so it should bounce and the typical way to do this is to reverse its vertical velocity. However, this would mean that before the event g(state) was decreasing from positive values to 0, and after the event g(state) would be increasing from 0 to positive values again. Consistency is broken here! The solution here is to have g(state) = sign * h(state), where sign is a variable with initial value set to +1. Each time eventOccurred method is called, sign is reset to -sign. This allows the g(state) function to remain continuous (and even smooth) even across events, despite h(state) is not. Basically, the event is used to fold h(state) at bounce points, and sign is used to unfold it back, so the solvers sees a g(state) function which behaves smoothly even across events.
        
        This method is idempotent, that is calling this multiple times with the same state will result in the same value, with two exceptions. First, the definition of the g function may change when an eventOccurred on the handler, as in the above example. Second, the definition of the g function may change when the eventOccurred method of any other event handler in the same integrator returns RESET_EVENTS, RESET_DERIVATIVES, or RESET_STATE.
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldEventSlopeFilter> state): current value of the independent time variable, state vector and derivative
        
        Returns:
            value of the g switching function
        
        
        """
        ...
    def getDetector(self) -> _FieldEventSlopeFilter__T:
        """
        Get the wrapped raw detector.
        
        Returns:
            the wrapped raw detector
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventSlopeFilter__E], finalTime: _FieldEventSlopeFilter__E) -> None:
        """
        Initialize event detector at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the event detector to initialize some internal data if needed.
        
        The default implementation initializes the handler.
        
        This implementation sets the direction of integration and initializes the event handler. If a subclass overrides this method it should call init(s0, t).
        
        Specified by: init in interface FieldODEEventDetector
        
        Overrides: init in class AbstractFieldODEDetector
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldEventSlopeFilter> initialState): initial time, state vector and derivative
            finalTime (FieldEventSlopeFilter): target time for the integration
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the current propagation is forward or backward.
        
        Overrides: isForward in class AbstractFieldODEDetector
        
        Returns:
            true if the current propagation is forward
        
        
        """
        ...
    def reset(self, intermediateState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventSlopeFilter__E], finalTime: _FieldEventSlopeFilter__E) -> None:
        """
        Reset event detector during integration.
        
        This method is called during integration if the derivatives or the state variables themselves are reset.
        
        The default implementation does nothing.
        
        Parameters:
            intermediateState (FieldODEStateAndDerivative<FieldEventSlopeFilter> intermediateState): intermediate time, state vector and derivative
            finalTime (FieldEventSlopeFilter): target time for the integration
        
        
        """
        ...


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
