
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import org.hipparchus
import org.hipparchus.ode
import typing



_FieldODEFixedStepHandler__T = typing.TypeVar('_FieldODEFixedStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEFixedStepHandler(typing.Generic[_FieldODEFixedStepHandler__T]):
    """
    This interface represents a handler that should be called after each successful fixed step.
    
    This interface should be implemented by anyone who is interested in getting the solution of an ordinary differential equation at fixed time steps. Objects implementing this interface should be wrapped within an instance of FieldStepNormalizer that itself is used as the general FieldODEStepHandler by the integrator. The FieldStepNormalizer object is called according to the integrator internal algorithms and it calls objects implementing this interface as necessary at fixed time steps.
    
    Also see:
        FieldODEStepHandler, FieldStepNormalizer,
        FieldODEStateInterpolator
    """
    def handleStep(self, state: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEFixedStepHandler__T], isLast: bool) -> None:
        """
        Handle the last accepted step
        
        Parameters:
            state (FieldODEStateAndDerivative<FieldODEFixedStepHandler> state): current value of the independent time variable, state vector and derivative For efficiency purposes, the
                FieldStepNormalizer class reuses the same array on each call, so if the instance
                wants to keep it across all calls (for example to provide at the end of the integration a complete array of all steps),
                it should build a local copy store this copy.
            isLast (boolean): true if the step is the last one
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEFixedStepHandler__T], finalTime: _FieldODEFixedStepHandler__T) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldODEFixedStepHandler> initialState): initial time, state vector and derivative
            finalTime (FieldODEFixedStepHandler): target time for the integration
        
        
        """
        ...

_FieldODEStateInterpolator__T = typing.TypeVar('_FieldODEStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStateInterpolator(typing.Generic[_FieldODEStateInterpolator__T]):
    """
    This interface represents an interpolator over the last step during an ODE integration.
    
    The various ODE integrators provide objects implementing this interface to the step handlers. These objects are often custom objects tightly bound to the integrator internal algorithms. The handlers can use these objects to retrieve the state vector at intermediate times between the previous and the current grid points (this feature is often called dense output).
    
    Also see:
        FieldODEIntegrator, FieldODEStepHandler
    """
    def getCurrentState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]:
        """
        Get the state at current grid point time.
        
        Returns:
            state at current grid point time
        
        
        """
        ...
    def getInterpolatedState(self, time: _FieldODEStateInterpolator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]:
        """
        Get the state at interpolated time.
        
        Setting the time outside of the current step is allowed, but should be used with care since the accuracy of the interpolator will probably be very poor far from this step. This allowance has been added to simplify implementation of search algorithms near the step endpoints.
        
        Parameters:
            time (FieldODEStateInterpolator): time of the interpolated point
        
        Returns:
            state at interpolated time
        
        
        """
        ...
    def getPreviousState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]:
        """
        Get the state at previous grid point time.
        
        Returns:
            state at previous grid point time
        
        
        """
        ...
    def isCurrentStateInterpolated(self) -> bool:
        """
        Determines if the getCurrentState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
        Returns:
            true if the current state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the natural integration direction is forward.
        
        This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in degenerated cases like null steps due to cancellation at step initialization, step control or discrete events triggering.
        
        Returns:
            true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
        Determines if the getPreviousState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the previous state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
        Returns:
            true if the previous state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def restrictStep(self, previousState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T], currentState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]) -> 'FieldODEStateInterpolator'[_FieldODEStateInterpolator__T]:
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Parameters:
            previousState (FieldODEStateAndDerivative<FieldODEStateInterpolator> previousState): start of the restricted step
            currentState (FieldODEStateAndDerivative<FieldODEStateInterpolator> currentState): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

_FieldODEStepHandler__T = typing.TypeVar('_FieldODEStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStepHandler(typing.Generic[_FieldODEStepHandler__T]):
    """
    This interface represents a handler that should be called after each successful step.
    
    The ODE integrators compute the evolution of the state vector at some grid points that depend on their own internal algorithm. Once they have found a new grid point (possibly after having computed several evaluation of the derivative at intermediate points), they provide it to objects implementing this interface. These objects typically either ignore the intermediate steps and wait for the last one, store the points in an ephemeris, or forward them to specialized processing or output methods.
    
    Also see:
        FieldODEIntegrator, FieldODEStateInterpolator
    """
    def finish(self, finalState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepHandler__T]) -> None:
        """
        Finalize integration.
        
        Parameters:
            finalState (FieldODEStateAndDerivative<FieldODEStepHandler> finalState): state at integration end
        
        Since:
            2.0
        
        
        """
        ...
    def handleStep(self, interpolator: FieldODEStateInterpolator[_FieldODEStepHandler__T]) -> None:
        """
        Handle the last accepted step.
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldODEStepHandler> interpolator): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepHandler__T], finalTime: _FieldODEStepHandler__T) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldODEStepHandler> initialState): initial time, state vector and derivative
            finalTime (FieldODEStepHandler): target time for the integration
        
        
        """
        ...
    def updateOnStep(self, interpolator: FieldODEStateInterpolator[_FieldODEStepHandler__T]) -> None:
        """
        Update the handler at the beginning of the step
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldODEStepHandler> interpolator): interpolator for the current step
        
        Since:
            4.0.3
        
        
        """
        ...

class ODEFixedStepHandler:
    """
    This interface represents a handler that should be called after each successful fixed step.
    
    This interface should be implemented by anyone who is interested in getting the solution of an ordinary differential equation at fixed time steps. Objects implementing this interface should be wrapped within an instance of StepNormalizer that itself is used as the general ODEStepHandler by the integrator. The StepNormalizer object is called according to the integrator internal algorithms and it calls objects implementing this interface as necessary at fixed time steps.
    
    Also see:
        ODEStepHandler, StepNormalizer
    """
    def handleStep(self, state: org.hipparchus.ode.ODEStateAndDerivative, isLast: bool) -> None:
        """
        Handle the last accepted step
        
        Parameters:
            state (ODEStateAndDerivative): current state
            isLast (boolean): true if the step is the last one
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            finalTime (double): target time for the integration
        
        
        """
        ...

class ODEStateInterpolator(java.io.Serializable):
    """
    This interface represents an interpolator over the last step during an ODE integration.
    
    The various ODE integrators provide objects implementing this interface to the step handlers. These objects are often custom objects tightly bound to the integrator internal algorithms. The handlers can use these objects to retrieve the state vector at intermediate times between the previous and the current grid points (this feature is often called dense output).
    
    Also see:
        ODEIntegrator, ODEStepHandler
    """
    def getCurrentState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the state at current grid point time.
        
        Returns:
            state at current grid point time
        
        
        """
        ...
    def getInterpolatedState(self, time: float) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the state at interpolated time.
        
        Setting the time outside of the current step is allowed, but should be used with care since the accuracy of the interpolator will probably be very poor far from this step. This allowance has been added to simplify implementation of search algorithms near the step endpoints.
        
        Parameters:
            time (double): time of the interpolated point
        
        Returns:
            state at interpolated time
        
        
        """
        ...
    def getPreviousState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the state at previous grid point time.
        
        Returns:
            state at previous grid point time
        
        
        """
        ...
    def isCurrentStateInterpolated(self) -> bool:
        """
        Determines if the getCurrentState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
        Returns:
            true if the current state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the natural integration direction is forward.
        
        This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in degenerated cases like null steps due to cancellation at step initialization, step control or discrete events triggering.
        
        Returns:
            true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
        Determines if the getPreviousState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the previous state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
        Returns:
            true if the previous state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def restrictStep(self, previousState: org.hipparchus.ode.ODEStateAndDerivative, currentState: org.hipparchus.ode.ODEStateAndDerivative) -> 'ODEStateInterpolator':
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Parameters:
            previousState (ODEStateAndDerivative): start of the restricted step
            currentState (ODEStateAndDerivative): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

class ODEStepHandler:
    """
    This interface represents a handler that should be called after each successful step.
    
    The ODE integrators compute the evolution of the state vector at some grid points that depend on their own internal algorithm. Once they have found a new grid point (possibly after having computed several evaluation of the derivative at intermediate points), they provide it to objects implementing this interface. These objects typically either ignore the intermediate steps and wait for the last one, store the points in an ephemeris, or forward them to specialized processing or output methods.
    
    Also see:
        ODEIntegrator, ODEStateInterpolator
    """
    def finish(self, finalState: org.hipparchus.ode.ODEStateAndDerivative) -> None:
        """
        Finalize integration.
        
        Parameters:
            finalState (ODEStateAndDerivative): state at integration end
        
        Since:
            2.0
        
        
        """
        ...
    def handleStep(self, interpolator: ODEStateInterpolator) -> None:
        """
        Handle the last accepted step.
        
        Parameters:
            interpolator (ODEStateInterpolator): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            finalTime (double): target time for the integration
        
        
        """
        ...
    def updateOnStep(self, interpolator: ODEStateInterpolator) -> None:
        """
        Update the handler at the beginning of the step
        
        Parameters:
            interpolator (ODEStateInterpolator): interpolator for the current step
        
        Since:
            4.0.3
        
        
        """
        ...

class StepNormalizerBounds(java.lang.Enum['StepNormalizerBounds']):
    """
    StepNormalizer bounds settings. They influence whether the underlying fixed step size step handler is called for the first and last points. Note that if the last point coincides with a normalized point, then the underlying fixed step size step handler is always called, regardless of these settings.
    
    Also see:
        FieldStepNormalizer, StepNormalizer,
        StepNormalizerMode
    """
    NEITHER: typing.ClassVar['StepNormalizerBounds'] = ...
    FIRST: typing.ClassVar['StepNormalizerBounds'] = ...
    LAST: typing.ClassVar['StepNormalizerBounds'] = ...
    BOTH: typing.ClassVar['StepNormalizerBounds'] = ...
    def firstIncluded(self) -> bool:
        """
        Returns a value indicating whether the first point should be passed to the underlying fixed step size step handler.
        
        Returns:
            value indicating whether the first point should be passed to the underlying fixed step size step handler.
        
        
        """
        ...
    def lastIncluded(self) -> bool:
        """
        Returns a value indicating whether the last point should be passed to the underlying fixed step size step handler.
        
        Returns:
            value indicating whether the last point should be passed to the underlying fixed step size step handler.
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'StepNormalizerBounds':
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
    def values() -> typing.MutableSequence['StepNormalizerBounds']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (StepNormalizerBounds c : StepNormalizerBounds.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StepNormalizerMode(java.lang.Enum['StepNormalizerMode']):
    """
    StepNormalizer modes. Determines how the step size is interpreted.
    
    Also see:
        FieldStepNormalizer, StepNormalizer,
        StepNormalizerBounds
    """
    INCREMENT: typing.ClassVar['StepNormalizerMode'] = ...
    MULTIPLES: typing.ClassVar['StepNormalizerMode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'StepNormalizerMode':
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
    def values() -> typing.MutableSequence['StepNormalizerMode']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (StepNormalizerMode c : StepNormalizerMode.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_AbstractFieldODEStateInterpolator__T = typing.TypeVar('_AbstractFieldODEStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractFieldODEStateInterpolator(FieldODEStateInterpolator[_AbstractFieldODEStateInterpolator__T], typing.Generic[_AbstractFieldODEStateInterpolator__T]):
    """
    This abstract class represents an interpolator over the last step during an ODE integration.
    
    The various ODE integrators provide objects extending this class to the step handlers. The handlers can use these objects to retrieve the state vector at intermediate times between the previous and the current grid points (dense output).
    
    Also see:
        FieldODEIntegrator, FieldODEStepHandler
    """
    def getCurrentState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]:
        """
        Get the state at current grid point time.
        
        Specified by: getCurrentState in interface FieldODEStateInterpolator
        
        Returns:
            state at current grid point time
        
        
        """
        ...
    def getGlobalCurrentState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]:
        """
        Get the current global grid point state.
        
        Returns:
            current global grid point state
        
        
        """
        ...
    def getGlobalPreviousState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]:
        """
        Get the previous global grid point state.
        
        Returns:
            previous global grid point state
        
        
        """
        ...
    def getInterpolatedState(self, time: _AbstractFieldODEStateInterpolator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]:
        """
        Get the state at interpolated time.
        
        Setting the time outside of the current step is allowed, but should be used with care since the accuracy of the interpolator will probably be very poor far from this step. This allowance has been added to simplify implementation of search algorithms near the step endpoints.
        
        Specified by: getInterpolatedState in interface FieldODEStateInterpolator
        
        Parameters:
            time (AbstractFieldODEStateInterpolator): time of the interpolated point
        
        Returns:
            state at interpolated time
        
        
        """
        ...
    def getPreviousState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]:
        """
        Get the state at previous grid point time.
        
        Specified by: getPreviousState in interface FieldODEStateInterpolator
        
        Returns:
            state at previous grid point time
        
        
        """
        ...
    def isCurrentStateInterpolated(self) -> bool:
        """
        Determines if the getCurrentState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
        Specified by: isCurrentStateInterpolated in interface FieldODEStateInterpolator
        
        Returns:
            true if the current state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the natural integration direction is forward.
        
        This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in degenerated cases like null steps due to cancellation at step initialization, step control or discrete events triggering.
        
        Specified by: isForward in interface FieldODEStateInterpolator
        
        Returns:
            true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
        Determines if the getPreviousState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the previous state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
        Specified by: isPreviousStateInterpolated in interface FieldODEStateInterpolator
        
        Returns:
            true if the previous state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def restrictStep(self, previousState: org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T], currentState: org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]) -> 'AbstractFieldODEStateInterpolator'[_AbstractFieldODEStateInterpolator__T]:
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Specified by: restrictStep in interface FieldODEStateInterpolator
        
        Parameters:
            previousState (FieldODEStateAndDerivative<AbstractFieldODEStateInterpolator> previousState): start of the restricted step
            currentState (FieldODEStateAndDerivative<AbstractFieldODEStateInterpolator> currentState): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

class AbstractODEStateInterpolator(ODEStateInterpolator):
    """
    This abstract class represents an interpolator over the last step during an ODE integration.
    
    The various ODE integrators provide objects extending this class to the step handlers. The handlers can use these objects to retrieve the state vector at intermediate times between the previous and the current grid points (dense output).
    
    Also see:
        ODEIntegrator, ODEStepHandler, serialized
    """
    def getCurrentState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the state at current grid point time.
        
        Specified by: getCurrentState in interface ODEStateInterpolator
        
        Returns:
            state at current grid point time
        
        
        """
        ...
    def getGlobalCurrentState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the current global grid point state.
        
        Returns:
            current global grid point state
        
        
        """
        ...
    def getGlobalPreviousState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the previous global grid point state.
        
        Returns:
            previous global grid point state
        
        
        """
        ...
    def getInterpolatedState(self, time: float) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the state at interpolated time.
        
        Setting the time outside of the current step is allowed, but should be used with care since the accuracy of the interpolator will probably be very poor far from this step. This allowance has been added to simplify implementation of search algorithms near the step endpoints.
        
        Specified by: getInterpolatedState in interface ODEStateInterpolator
        
        Parameters:
            time (double): time of the interpolated point
        
        Returns:
            state at interpolated time
        
        
        """
        ...
    def getPreviousState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Get the state at previous grid point time.
        
        Specified by: getPreviousState in interface ODEStateInterpolator
        
        Returns:
            state at previous grid point time
        
        
        """
        ...
    def isCurrentStateInterpolated(self) -> bool:
        """
        Determines if the getCurrentState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
        Specified by: isCurrentStateInterpolated in interface ODEStateInterpolator
        
        Returns:
            true if the current state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check if the natural integration direction is forward.
        
        This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in degenerated cases like null steps due to cancellation at step initialization, step control or discrete events triggering.
        
        Specified by: isForward in interface ODEStateInterpolator
        
        Returns:
            true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
        Determines if the getPreviousState is computed directly by the integrator, or if it is calculated using getInterpolatedState.
        
        Typically the previous state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
        Specified by: isPreviousStateInterpolated in interface ODEStateInterpolator
        
        Returns:
            true if the previous state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def restrictStep(self, previousState: org.hipparchus.ode.ODEStateAndDerivative, currentState: org.hipparchus.ode.ODEStateAndDerivative) -> 'AbstractODEStateInterpolator':
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Specified by: restrictStep in interface ODEStateInterpolator
        
        Parameters:
            previousState (ODEStateAndDerivative): start of the restricted step
            currentState (ODEStateAndDerivative): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

_FieldStepNormalizer__T = typing.TypeVar('_FieldStepNormalizer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStepNormalizer(FieldODEStepHandler[_FieldStepNormalizer__T], typing.Generic[_FieldStepNormalizer__T]):
    """
    This class wraps an object implementing FieldODEFixedStepHandler into a FieldODEStepHandler.
    
    This wrapper allows to use fixed step handlers with general integrators which cannot guaranty their integration steps will remain constant and therefore only accept general step handlers.
    
    The stepsize used is selected at construction time. The handleStep method of the underlying FieldODEFixedStepHandler object is called at normalized times. The normalized times can be influenced by the StepNormalizerMode and StepNormalizerBounds.
    
    There is no constraint on the integrator, it can use any time step it needs (time steps longer or shorter than the fixed time step and non-integer ratios are all allowed).
    
    Also see:
        FieldODEStepHandler,
        FieldODEFixedStepHandler,
        StepNormalizerMode, StepNormalizerBounds
    """
    @typing.overload
    def __init__(self, h: float, handler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]]): ...
    @typing.overload
    def __init__(self, double: float, fieldODEFixedStepHandler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]], stepNormalizerBounds: StepNormalizerBounds): ...
    @typing.overload
    def __init__(self, double: float, fieldODEFixedStepHandler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]], stepNormalizerMode: StepNormalizerMode): ...
    @typing.overload
    def __init__(self, h: float, handler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]], mode: StepNormalizerMode, bounds: StepNormalizerBounds): ...
    def finish(self, finalState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepNormalizer__T]) -> None:
        """
        Finalize integration.
        
        Specified by: finish in interface FieldODEStepHandler
        
        Parameters:
            finalState (FieldODEStateAndDerivative<FieldStepNormalizer> finalState): state at integration end
        
        
        """
        ...
    def handleStep(self, interpolator: FieldODEStateInterpolator[_FieldStepNormalizer__T]) -> None:
        """
        Handle the last accepted step.
        
        Specified by: handleStep in interface FieldODEStepHandler
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldStepNormalizer> interpolator): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepNormalizer__T], finalTime: _FieldStepNormalizer__T) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Specified by: init in interface FieldODEStepHandler
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldStepNormalizer> initialState): initial time, state vector and derivative
            finalTime (FieldStepNormalizer): target time for the integration
        
        
        """
        ...

class StepNormalizer(ODEStepHandler):
    """
    This class wraps an object implementing ODEFixedStepHandler into a ODEStepHandler.
    
    This wrapper allows to use fixed step handlers with general integrators which cannot guaranty their integration steps will remain constant and therefore only accept general step handlers.
    
    The stepsize used is selected at construction time. The handleStep method of the underlying ODEFixedStepHandler object is called at normalized times. The normalized times can be influenced by the StepNormalizerMode and StepNormalizerBounds.
    
    There is no constraint on the integrator, it can use any time step it needs (time steps longer or shorter than the fixed time step and non-integer ratios are all allowed).
    
    Also see:
        ODEStepHandler, ODEFixedStepHandler,
        StepNormalizerMode, StepNormalizerBounds
    """
    @typing.overload
    def __init__(self, h: float, handler: typing.Union[ODEFixedStepHandler, typing.Callable]): ...
    @typing.overload
    def __init__(self, double: float, oDEFixedStepHandler: typing.Union[ODEFixedStepHandler, typing.Callable], stepNormalizerBounds: StepNormalizerBounds): ...
    @typing.overload
    def __init__(self, double: float, oDEFixedStepHandler: typing.Union[ODEFixedStepHandler, typing.Callable], stepNormalizerMode: StepNormalizerMode): ...
    @typing.overload
    def __init__(self, h: float, handler: typing.Union[ODEFixedStepHandler, typing.Callable], mode: StepNormalizerMode, bounds: StepNormalizerBounds): ...
    def finish(self, finalState: org.hipparchus.ode.ODEStateAndDerivative) -> None:
        """
        Finalize integration.
        
        Specified by: finish in interface ODEStepHandler
        
        Parameters:
            finalState (ODEStateAndDerivative): state at integration end
        
        
        """
        ...
    def handleStep(self, interpolator: ODEStateInterpolator) -> None:
        """
        Handle the last accepted step.
        
        Specified by: handleStep in interface ODEStepHandler
        
        Parameters:
            interpolator (ODEStateInterpolator): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, initialState: org.hipparchus.ode.ODEStateAndDerivative, finalTime: float) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Specified by: init in interface ODEStepHandler
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            finalTime (double): target time for the integration
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.ode.sampling")``.

    AbstractFieldODEStateInterpolator: typing.Type[AbstractFieldODEStateInterpolator]
    AbstractODEStateInterpolator: typing.Type[AbstractODEStateInterpolator]
    FieldODEFixedStepHandler: typing.Type[FieldODEFixedStepHandler]
    FieldODEStateInterpolator: typing.Type[FieldODEStateInterpolator]
    FieldODEStepHandler: typing.Type[FieldODEStepHandler]
    FieldStepNormalizer: typing.Type[FieldStepNormalizer]
    ODEFixedStepHandler: typing.Type[ODEFixedStepHandler]
    ODEStateInterpolator: typing.Type[ODEStateInterpolator]
    ODEStepHandler: typing.Type[ODEStepHandler]
    StepNormalizer: typing.Type[StepNormalizer]
    StepNormalizerBounds: typing.Type[StepNormalizerBounds]
    StepNormalizerMode: typing.Type[StepNormalizerMode]
