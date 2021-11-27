import java.lang
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.solvers
import org.hipparchus.ode
import org.hipparchus.ode.sampling
import typing



class Action(java.lang.Enum['Action']):
    """
    public enum Action extends Enum<:class:`~org.hipparchus.ode.events.Action`>
    
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
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['Action']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (Action c : Action.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class EventHandlerConfiguration:
    """
    public interface EventHandlerConfiguration
    
        Interface gathering all configuration parameters for setting up an event handler.
    
        Since:
            2.0
    """
    def getConvergence(self) -> float:
        """
            Get the convergence threshold for event localization.
        
            Returns:
                convergence threshold for event localization
        
        
        """
        ...
    def getEventHandler(self) -> 'ODEEventHandler':
        """
            Get the underlying event handler.
        
            Returns:
                underlying event handler
        
        
        """
        ...
    def getMaxCheckInterval(self) -> float:
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

_FieldEventHandlerConfiguration__T = typing.TypeVar('_FieldEventHandlerConfiguration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventHandlerConfiguration(typing.Generic[_FieldEventHandlerConfiguration__T]):
    """
    public interface FieldEventHandlerConfiguration<T extends CalculusFieldElement<T>>
    
        Interface gathering all configuration parameters for setting up an event handler.
    
        Since:
            2.0
    """
    def getConvergence(self) -> _FieldEventHandlerConfiguration__T:
        """
            Get the convergence threshold for event localization.
        
            Returns:
                convergence threshold for event localization
        
        
        """
        ...
    def getEventHandler(self) -> 'FieldODEEventHandler'[_FieldEventHandlerConfiguration__T]: ...
    def getMaxCheckInterval(self) -> float:
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
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldEventHandlerConfiguration__T]: ...

_FieldODEEventHandler__T = typing.TypeVar('_FieldODEEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEEventHandler(typing.Generic[_FieldODEEventHandler__T]):
    def eventOccurred(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], boolean: bool) -> Action: ...
    def g(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T]) -> _FieldODEEventHandler__T: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], t: _FieldODEEventHandler__T) -> None: ...
    def resetState(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T]) -> org.hipparchus.ode.FieldODEState[_FieldODEEventHandler__T]: ...

class FilterType(java.lang.Enum['FilterType']):
    """
    public enum FilterType extends Enum<:class:`~org.hipparchus.ode.events.FilterType`>
    
        Enumerate for :class:`~org.hipparchus.ode.events.EventFilter`.
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
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
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

class ODEEventHandler:
    """
    public interface ODEEventHandler
    
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
    
        Also see:
            :class:`~org.hipparchus.ode.events.package`
    """
    def eventOccurred(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, boolean: bool) -> Action:
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
                increasing (boolean): if true, the value of the switching function increases when times increases around event (note that increase is measured
                    with respect to physical time, not with respect to integration which may go backward in time)
        
            Returns:
                indication of what the integrator should do next, this value must be one of
                :meth:`~org.hipparchus.ode.events.Action.STOP`, :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`,
                :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`, or
                :meth:`~org.hipparchus.ode.events.Action.CONTINUE`
        
        
        """
        ...
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
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` on this handler, as in the above example. Second, the
            definition of the g function may change when the :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` method
            of any other event handler in the same integrator returns :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`,
            :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, or :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
        
            Returns:
                value of the g switching function
        
            Also see:
                :class:`~org.hipparchus.ode.events.package`
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize event handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the event handler to initialize some
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
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
        
            Returns:
                reset state (note that it does not include the derivatives, they will be added automatically by the integrator
                afterwards)
        
        
        """
        ...

class EventFilter(ODEEventHandler):
    """
    public class EventFilter extends Object implements :class:`~org.hipparchus.ode.events.ODEEventHandler`
    
        Wrapper used to detect only increasing or decreasing events.
    
        General :class:`~org.hipparchus.ode.events.ODEEventHandler` are defined implicitly by a
        :meth:`~org.hipparchus.ode.events.ODEEventHandler.g` crossing zero. This function needs to be continuous in the event
        neighborhood, and its sign must remain consistent between events. This implies that during an ODE integration, events
        triggered are alternately events for which the function increases from negative to positive values, and events for which
        the function decreases from positive to negative values.
    
        Sometimes, users are only interested in one type of event (say increasing events for example) and not in the other type.
        In these cases, looking precisely for all events location and triggering events that will later be ignored is a waste of
        computing time.
    
        Users can wrap a regular :class:`~org.hipparchus.ode.events.ODEEventHandler` in an instance of this class and provide
        this wrapping instance to the :class:`~org.hipparchus.ode.ODEIntegrator` in order to avoid wasting time looking for
        uninteresting events. The wrapper will intercept the calls to the :meth:`~org.hipparchus.ode.events.ODEEventHandler.g`
        and to the :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` method in order to ignore uninteresting
        events. The wrapped regular :class:`~org.hipparchus.ode.events.ODEEventHandler` will the see only the interesting
        events, i.e. either only :code:`increasing` events or :code:`decreasing` events. the number of calls to the
        :meth:`~org.hipparchus.ode.events.ODEEventHandler.g` will also be reduced.
    """
    def __init__(self, oDEEventHandler: ODEEventHandler, filterType: FilterType): ...
    def eventOccurred(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, boolean: bool) -> Action:
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
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.ODEEventHandler`
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
                increasing (boolean): if true, the value of the switching function increases when times increases around event (note that increase is measured
                    with respect to physical time, not with respect to integration which may go backward in time)
        
            Returns:
                indication of what the integrator should do next, this value must be one of
                :meth:`~org.hipparchus.ode.events.Action.STOP`, :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`,
                :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`, or
                :meth:`~org.hipparchus.ode.events.Action.CONTINUE`
        
        
        """
        ...
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
            :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` on this handler, as in the above example. Second, the
            definition of the g function may change when the :meth:`~org.hipparchus.ode.events.ODEEventHandler.eventOccurred` method
            of any other event handler in the same integrator returns :meth:`~org.hipparchus.ode.events.Action.RESET_EVENTS`,
            :meth:`~org.hipparchus.ode.events.Action.RESET_DERIVATIVES`, or :meth:`~org.hipparchus.ode.events.Action.RESET_STATE`.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventHandler.g` in interface :class:`~org.hipparchus.ode.events.ODEEventHandler`
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
        
            Returns:
                value of the g switching function
        
            Also see:
                :class:`~org.hipparchus.ode.events.package`
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize event handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventHandler.init`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.ODEEventHandler`
        
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
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.ODEEventHandler.resetState`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.ODEEventHandler`
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current value of the independent *time* variable, state vector and derivative
        
            Returns:
                reset state (note that it does not include the derivatives, they will be added automatically by the integrator
                afterwards)
        
        
        """
        ...

class EventState(EventHandlerConfiguration):
    """
    public class EventState extends Object implements :class:`~org.hipparchus.ode.events.EventHandlerConfiguration`
    
        This class handles the state for one :class:`~org.hipparchus.ode.events.ODEEventHandler` during integration steps.
    
        Each time the integrator proposes a step, the event handler switching function should be checked. This class handles the
        state of one handler during one integration step, with references to the state at the end of the preceding step. This
        information is used to decide if the handler should trigger an event or not during the proposed step.
    """
    def __init__(self, oDEEventHandler: ODEEventHandler, double: float, double2: float, int: int, bracketedUnivariateSolver: org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]): ...
    def doEvent(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> 'EventState.EventOccurrence':
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
    def getConvergence(self) -> float:
        """
            Get the convergence threshold for event localization.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventHandlerConfiguration.getConvergence`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.EventHandlerConfiguration`
        
            Returns:
                convergence threshold for event localization
        
        
        """
        ...
    def getEventHandler(self) -> ODEEventHandler:
        """
            Get the underlying event handler.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventHandlerConfiguration.getEventHandler`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.EventHandlerConfiguration`
        
            Returns:
                underlying event handler
        
        
        """
        ...
    def getEventTime(self) -> float:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def getMaxCheckInterval(self) -> float:
        """
            Get the maximal time interval between events handler checks.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventHandlerConfiguration.getMaxCheckInterval`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.EventHandlerConfiguration`
        
            Returns:
                maximal time interval between events handler checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
            Get the upper limit in the iteration count for event localization.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventHandlerConfiguration.getMaxIterationCount`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.EventHandlerConfiguration`
        
            Returns:
                upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]:
        """
            Get the root-finding algorithm to use to detect state events.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.EventHandlerConfiguration.getSolver`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.EventHandlerConfiguration`
        
            Returns:
                root-finding algorithm to use to detect state events
        
        
        """
        ...
    def reinitializeBegin(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> None: ...
    def tryAdvance(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool:
        """
            Try to accept the current history up to the given time.
        
            It is not necessary to call this method before calling :meth:`~org.hipparchus.ode.events.EventState.doEvent` with the
            same state. It is necessary to call this method before you call :meth:`~org.hipparchus.ode.events.EventState.doEvent` on
            some other event detector.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): to try to accept.
                interpolator (:class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`): to use to find the new root, if any.
        
            Returns:
                if the event detector has an event it has not detected before that is on or before the same time as :code:`state`. In
                other words :code:`false` means continue on while :code:`true` means stop and handle my event first.
        
        
        """
        ...
    class EventOccurrence:
        def getAction(self) -> Action: ...
        def getNewState(self) -> org.hipparchus.ode.ODEState: ...
        def getStopTime(self) -> float: ...

_FieldEventFilter__T = typing.TypeVar('_FieldEventFilter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventFilter(FieldODEEventHandler[_FieldEventFilter__T], typing.Generic[_FieldEventFilter__T]):
    def __init__(self, field: org.hipparchus.Field[_FieldEventFilter__T], fieldODEEventHandler: FieldODEEventHandler[_FieldEventFilter__T], filterType: FilterType): ...
    def eventOccurred(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T], boolean: bool) -> Action: ...
    def g(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T]) -> _FieldEventFilter__T: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T], t: _FieldEventFilter__T) -> None: ...
    def resetState(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T]) -> org.hipparchus.ode.FieldODEState[_FieldEventFilter__T]: ...

_FieldEventState__EventOccurrence__T = typing.TypeVar('_FieldEventState__EventOccurrence__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldEventState__T = typing.TypeVar('_FieldEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventState(FieldEventHandlerConfiguration[_FieldEventState__T], typing.Generic[_FieldEventState__T]):
    """
    public class FieldEventState<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.hipparchus.ode.events.FieldEventHandlerConfiguration`<T>
    
        This class handles the state for one :class:`~org.hipparchus.ode.events.FieldODEEventHandler` during integration steps.
    
        Each time the integrator proposes a step, the event handler switching function should be checked. This class handles the
        state of one handler during one integration step, with references to the state at the end of the preceding step. This
        information is used to decide if the handler should trigger an event or not during the proposed step.
    """
    def __init__(self, fieldODEEventHandler: FieldODEEventHandler[_FieldEventState__T], double: float, t: _FieldEventState__T, int: int, bracketedRealFieldUnivariateSolver: org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldEventState__T]): ...
    def doEvent(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T]) -> 'FieldEventState.EventOccurrence'[_FieldEventState__T]: ...
    def evaluateStep(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> bool: ...
    def getConvergence(self) -> _FieldEventState__T:
        """
            Get the convergence threshold for event localization.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.FieldEventHandlerConfiguration.getConvergence`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.FieldEventHandlerConfiguration`
        
            Returns:
                convergence threshold for event localization
        
        
        """
        ...
    def getEventHandler(self) -> FieldODEEventHandler[_FieldEventState__T]: ...
    def getEventTime(self) -> _FieldEventState__T:
        """
            Get the occurrence time of the event triggered in the current step.
        
            Returns:
                occurrence time of the event triggered in the current step or infinity if no events are triggered
        
        
        """
        ...
    def getMaxCheckInterval(self) -> float:
        """
            Get the maximal time interval between events handler checks.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.FieldEventHandlerConfiguration.getMaxCheckInterval`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.FieldEventHandlerConfiguration`
        
            Returns:
                maximal time interval between events handler checks
        
        
        """
        ...
    def getMaxIterationCount(self) -> int:
        """
            Get the upper limit in the iteration count for event localization.
        
            Specified by:
                :meth:`~org.hipparchus.ode.events.FieldEventHandlerConfiguration.getMaxIterationCount`Â in
                interfaceÂ :class:`~org.hipparchus.ode.events.FieldEventHandlerConfiguration`
        
            Returns:
                upper limit in the iteration count for event localization
        
        
        """
        ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldEventState__T]: ...
    def reinitializeBegin(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> None: ...
    def tryAdvance(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T], fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> bool: ...
    class EventOccurrence(typing.Generic[_FieldEventState__EventOccurrence__T]):
        def getAction(self) -> Action: ...
        def getNewState(self) -> org.hipparchus.ode.FieldODEState[_FieldEventState__EventOccurrence__T]: ...
        def getStopTime(self) -> _FieldEventState__EventOccurrence__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.ode.events")``.

    Action: typing.Type[Action]
    EventFilter: typing.Type[EventFilter]
    EventHandlerConfiguration: typing.Type[EventHandlerConfiguration]
    EventState: typing.Type[EventState]
    FieldEventFilter: typing.Type[FieldEventFilter]
    FieldEventHandlerConfiguration: typing.Type[FieldEventHandlerConfiguration]
    FieldEventState: typing.Type[FieldEventState]
    FieldODEEventHandler: typing.Type[FieldODEEventHandler]
    FilterType: typing.Type[FilterType]
    ODEEventHandler: typing.Type[ODEEventHandler]
