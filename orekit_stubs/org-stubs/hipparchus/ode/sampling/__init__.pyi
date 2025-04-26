
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
    public interfaceFieldODEFixedStepHandler<T extends :class:`~org.hipparchus.ode.sampling.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents a handler that should be called after each successful fixed step.
    
        This interface should be implemented by anyone who is interested in getting the solution of an ordinary differential
        equation at fixed time steps. Objects implementing this interface should be wrapped within an instance of
        :class:`~org.hipparchus.ode.sampling.FieldStepNormalizer` that itself is used as the general
        :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler` by the integrator. The
        :class:`~org.hipparchus.ode.sampling.FieldStepNormalizer` object is called according to the integrator internal
        algorithms and it calls objects implementing this interface as necessary at fixed time steps.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`
              - :class:`~org.hipparchus.ode.sampling.FieldStepNormalizer`
              - :class:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator`
    """
    def handleStep(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEFixedStepHandler__T], boolean: bool) -> None: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEFixedStepHandler__T], t: _FieldODEFixedStepHandler__T) -> None: ...

_FieldODEStateInterpolator__T = typing.TypeVar('_FieldODEStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStateInterpolator(typing.Generic[_FieldODEStateInterpolator__T]):
    """
    public interfaceFieldODEStateInterpolator<T extends :class:`~org.hipparchus.ode.sampling.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents an interpolator over the last step during an ODE integration.
    
        The various ODE integrators provide objects implementing this interface to the step handlers. These objects are often
        custom objects tightly bound to the integrator internal algorithms. The handlers can use these objects to retrieve the
        state vector at intermediate times between the previous and the current grid points (this feature is often called dense
        output).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldODEIntegrator`
              - :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`
    """
    def getCurrentState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]: ...
    def getInterpolatedState(self, t: _FieldODEStateInterpolator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]: ...
    def getPreviousState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]: ...
    def isCurrentStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getCurrentState` is computed directly by
            the integrator, or if it is calculated using
            :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getInterpolatedState`.
        
            Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened
            so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
            Returns:
                :code:`true` if the current state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
            Check if the natural integration direction is forward.
        
            This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in
            degenerated cases like null steps due to cancellation at step initialization, step control or discrete events
            triggering.
        
            Returns:
                true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getPreviousState` is computed directly
            by the integrator, or if it is calculated using
            :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getInterpolatedState`.
        
            Typically the previous state is directly computed by the integrator, but when events are detected the steps are
            shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
            Returns:
                :code:`true` if the previous state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def restrictStep(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStateInterpolator__T]) -> 'FieldODEStateInterpolator'[_FieldODEStateInterpolator__T]: ...

_FieldODEStepHandler__T = typing.TypeVar('_FieldODEStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStepHandler(typing.Generic[_FieldODEStepHandler__T]):
    """
    public interfaceFieldODEStepHandler<T extends :class:`~org.hipparchus.ode.sampling.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents a handler that should be called after each successful step.
    
        The ODE integrators compute the evolution of the state vector at some grid points that depend on their own internal
        algorithm. Once they have found a new grid point (possibly after having computed several evaluation of the derivative at
        intermediate points), they provide it to objects implementing this interface. These objects typically either ignore the
        intermediate steps and wait for the last one, store the points in an ephemeris, or forward them to specialized
        processing or output methods.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldODEIntegrator`
              - :class:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator`
    """
    def finish(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepHandler__T]) -> None: ...
    def handleStep(self, fieldODEStateInterpolator: FieldODEStateInterpolator[_FieldODEStepHandler__T]) -> None: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEStepHandler__T], t: _FieldODEStepHandler__T) -> None: ...

class ODEFixedStepHandler:
    """
    public interfaceODEFixedStepHandler
    
        This interface represents a handler that should be called after each successful fixed step.
    
        This interface should be implemented by anyone who is interested in getting the solution of an ordinary differential
        equation at fixed time steps. Objects implementing this interface should be wrapped within an instance of
        :class:`~org.hipparchus.ode.sampling.StepNormalizer` that itself is used as the general
        :class:`~org.hipparchus.ode.sampling.ODEStepHandler` by the integrator. The
        :class:`~org.hipparchus.ode.sampling.StepNormalizer` object is called according to the integrator internal algorithms
        and it calls objects implementing this interface as necessary at fixed time steps.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizer`
    """
    def handleStep(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, boolean: bool) -> None:
        """
            Handle the last accepted step
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): current state
                isLast (boolean): true if the step is the last one
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize step handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default implementation does nothing.
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                finalTime (double): target time for the integration
        
        
        """
        ...

class ODEStateInterpolator(java.io.Serializable):
    """
    public interfaceODEStateInterpolatorextends :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This interface represents an interpolator over the last step during an ODE integration.
    
        The various ODE integrators provide objects implementing this interface to the step handlers. These objects are often
        custom objects tightly bound to the integrator internal algorithms. The handlers can use these objects to retrieve the
        state vector at intermediate times between the previous and the current grid points (this feature is often called dense
        output).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
    """
    def getCurrentState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
            Get the state at current grid point time.
        
            Returns:
                state at current grid point time
        
        
        """
        ...
    def getInterpolatedState(self, double: float) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
            Get the state at interpolated time.
        
            Setting the time outside of the current step is allowed, but should be used with care since the accuracy of the
            interpolator will probably be very poor far from this step. This allowance has been added to simplify implementation of
            search algorithms near the step endpoints.
        
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
            Determines if the :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getCurrentState` is computed directly by the
            integrator, or if it is calculated using :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getInterpolatedState`.
        
            Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened
            so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
            Returns:
                :code:`true` if the current state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
            Check if the natural integration direction is forward.
        
            This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in
            degenerated cases like null steps due to cancellation at step initialization, step control or discrete events
            triggering.
        
            Returns:
                true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getPreviousState` is computed directly by the
            integrator, or if it is calculated using :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getInterpolatedState`.
        
            Typically the previous state is directly computed by the integrator, but when events are detected the steps are
            shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
            Returns:
                :code:`true` if the previous state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def restrictStep(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative) -> 'ODEStateInterpolator':
        """
            Create a new restricted version of the instance.
        
            The instance is not changed at all.
        
            Parameters:
                previousState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): start of the restricted step
                currentState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): end of the restricted step
        
            Returns:
                restricted version of the instance
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getPreviousState`
                  - :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getCurrentState`
        
        
        
        """
        ...

class ODEStepHandler:
    """
    public interfaceODEStepHandler
    
        This interface represents a handler that should be called after each successful step.
    
        The ODE integrators compute the evolution of the state vector at some grid points that depend on their own internal
        algorithm. Once they have found a new grid point (possibly after having computed several evaluation of the derivative at
        intermediate points), they provide it to objects implementing this interface. These objects typically either ignore the
        intermediate steps and wait for the last one, store the points in an ephemeris, or forward them to specialized
        processing or output methods.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
    """
    def finish(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> None:
        """
            Finalize integration.
        
            Parameters:
                finalState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): state at integration end
        
            Since:
                2.0
        
        
        """
        ...
    def handleStep(self, oDEStateInterpolator: ODEStateInterpolator) -> None:
        """
            Handle the last accepted step.
        
            Parameters:
                interpolator (:class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize step handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                finalTime (double): target time for the integration
        
        
        """
        ...

class StepNormalizerBounds(java.lang.Enum['StepNormalizerBounds']):
    """
    public enumStepNormalizerBounds extends :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.ode.sampling.StepNormalizerBounds`>
    
        :class:`~org.hipparchus.ode.sampling.StepNormalizer` bounds settings. They influence whether the underlying fixed step
        size step handler is called for the first and last points. Note that if the last point coincides with a normalized
        point, then the underlying fixed step size step handler is always called, regardless of these settings.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.FieldStepNormalizer`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizer`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizerMode`
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
    def valueOf(string: str) -> 'StepNormalizerBounds':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['StepNormalizerBounds']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StepNormalizerMode(java.lang.Enum['StepNormalizerMode']):
    """
    public enumStepNormalizerMode extends :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.ode.sampling.StepNormalizerMode`>
    
        :class:`~org.hipparchus.ode.sampling.StepNormalizer` modes. Determines how the step size is interpreted.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.FieldStepNormalizer`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizer`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizerBounds`
    """
    INCREMENT: typing.ClassVar['StepNormalizerMode'] = ...
    MULTIPLES: typing.ClassVar['StepNormalizerMode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'StepNormalizerMode':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['StepNormalizerMode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_AbstractFieldODEStateInterpolator__T = typing.TypeVar('_AbstractFieldODEStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractFieldODEStateInterpolator(FieldODEStateInterpolator[_AbstractFieldODEStateInterpolator__T], typing.Generic[_AbstractFieldODEStateInterpolator__T]):
    """
    public abstract classAbstractFieldODEStateInterpolator<T extends :class:`~org.hipparchus.ode.sampling.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator`<T>
    
        This abstract class represents an interpolator over the last step during an ODE integration.
    
        The various ODE integrators provide objects extending this class to the step handlers. The handlers can use these
        objects to retrieve the state vector at intermediate times between the previous and the current grid points (dense
        output).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldODEIntegrator`
              - :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`
    """
    def getCurrentState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]: ...
    def getGlobalCurrentState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]: ...
    def getGlobalPreviousState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]: ...
    def getInterpolatedState(self, t: _AbstractFieldODEStateInterpolator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]: ...
    def getPreviousState(self) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]: ...
    def isCurrentStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getCurrentState` is computed directly by
            the integrator, or if it is calculated using
            :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getInterpolatedState`.
        
            Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened
            so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.isCurrentStateInterpolated` in
                interface :class:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator`
        
            Returns:
                :code:`true` if the current state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
            Check if the natural integration direction is forward.
        
            This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in
            degenerated cases like null steps due to cancellation at step initialization, step control or discrete events
            triggering.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.isForward` in
                interface :class:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator`
        
            Returns:
                true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getPreviousState` is computed directly
            by the integrator, or if it is calculated using
            :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.getInterpolatedState`.
        
            Typically the previous state is directly computed by the integrator, but when events are detected the steps are
            shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator.isPreviousStateInterpolated` in
                interface :class:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator`
        
            Returns:
                :code:`true` if the previous state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def restrictStep(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_AbstractFieldODEStateInterpolator__T]) -> 'AbstractFieldODEStateInterpolator'[_AbstractFieldODEStateInterpolator__T]: ...

class AbstractODEStateInterpolator(ODEStateInterpolator):
    """
    public abstract classAbstractODEStateInterpolator extends :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
    
        This abstract class represents an interpolator over the last step during an ODE integration.
    
        The various ODE integrators provide objects extending this class to the step handlers. The handlers can use these
        objects to retrieve the state vector at intermediate times between the previous and the current grid points (dense
        output).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
              - :meth:`~serialized`
    """
    def getCurrentState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
            Get the state at current grid point time.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getCurrentState` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
        
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
    def getInterpolatedState(self, double: float) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
            Get the state at interpolated time.
        
            Setting the time outside of the current step is allowed, but should be used with care since the accuracy of the
            interpolator will probably be very poor far from this step. This allowance has been added to simplify implementation of
            search algorithms near the step endpoints.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getInterpolatedState` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
        
            Parameters:
                time (double): time of the interpolated point
        
            Returns:
                state at interpolated time
        
        
        """
        ...
    def getPreviousState(self) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
            Get the state at previous grid point time.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getPreviousState` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
        
            Returns:
                state at previous grid point time
        
        
        """
        ...
    def isCurrentStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getCurrentState` is computed directly by the
            integrator, or if it is calculated using :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getInterpolatedState`.
        
            Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened
            so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.isCurrentStateInterpolated` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
        
            Returns:
                :code:`true` if the current state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
            Check if the natural integration direction is forward.
        
            This method provides the integration direction as specified by the integrator itself, it avoid some nasty problems in
            degenerated cases like null steps due to cancellation at step initialization, step control or discrete events
            triggering.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.isForward` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
        
            Returns:
                true if the integration variable (time) increases during integration
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getPreviousState` is computed directly by the
            integrator, or if it is calculated using :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getInterpolatedState`.
        
            Typically the previous state is directly computed by the integrator, but when events are detected the steps are
            shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.isPreviousStateInterpolated` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
        
            Returns:
                :code:`true` if the previous state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def restrictStep(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative) -> 'AbstractODEStateInterpolator':
        """
            Create a new restricted version of the instance.
        
            The instance is not changed at all.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.restrictStep` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
        
            Parameters:
                previousState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): start of the restricted step
                currentState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): end of the restricted step
        
            Returns:
                restricted version of the instance
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getPreviousState`
                  - :meth:`~org.hipparchus.ode.sampling.ODEStateInterpolator.getCurrentState`
        
        
        
        """
        ...

_FieldStepNormalizer__T = typing.TypeVar('_FieldStepNormalizer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStepNormalizer(FieldODEStepHandler[_FieldStepNormalizer__T], typing.Generic[_FieldStepNormalizer__T]):
    """
    public classFieldStepNormalizer<T extends :class:`~org.hipparchus.ode.sampling.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`<T>
    
        This class wraps an object implementing :class:`~org.hipparchus.ode.sampling.FieldODEFixedStepHandler` into a
        :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`.
    
        This wrapper allows to use fixed step handlers with general integrators which cannot guaranty their integration steps
        will remain constant and therefore only accept general step handlers.
    
        The stepsize used is selected at construction time. The
        :meth:`~org.hipparchus.ode.sampling.FieldODEFixedStepHandler.handleStep` method of the underlying
        :class:`~org.hipparchus.ode.sampling.FieldODEFixedStepHandler` object is called at normalized times. The normalized
        times can be influenced by the :class:`~org.hipparchus.ode.sampling.StepNormalizerMode` and
        :class:`~org.hipparchus.ode.sampling.StepNormalizerBounds`.
    
        There is no constraint on the integrator, it can use any time step it needs (time steps longer or shorter than the fixed
        time step and non-integer ratios are all allowed).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`
              - :class:`~org.hipparchus.ode.sampling.FieldODEFixedStepHandler`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizerMode`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizerBounds`
    """
    @typing.overload
    def __init__(self, double: float, fieldODEFixedStepHandler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]]): ...
    @typing.overload
    def __init__(self, double: float, fieldODEFixedStepHandler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]], stepNormalizerBounds: StepNormalizerBounds): ...
    @typing.overload
    def __init__(self, double: float, fieldODEFixedStepHandler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]], stepNormalizerMode: StepNormalizerMode): ...
    @typing.overload
    def __init__(self, double: float, fieldODEFixedStepHandler: typing.Union[FieldODEFixedStepHandler[_FieldStepNormalizer__T], typing.Callable[[org.hipparchus.ode.FieldODEStateAndDerivative[org.hipparchus.CalculusFieldElement], bool], None]], stepNormalizerMode: StepNormalizerMode, stepNormalizerBounds: StepNormalizerBounds): ...
    def finish(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepNormalizer__T]) -> None: ...
    def handleStep(self, fieldODEStateInterpolator: FieldODEStateInterpolator[_FieldStepNormalizer__T]) -> None: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldStepNormalizer__T], t: _FieldStepNormalizer__T) -> None: ...

class StepNormalizer(ODEStepHandler):
    """
    public classStepNormalizer extends :class:`~org.hipparchus.ode.sampling.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
    
        This class wraps an object implementing :class:`~org.hipparchus.ode.sampling.ODEFixedStepHandler` into a
        :class:`~org.hipparchus.ode.sampling.ODEStepHandler`.
    
        This wrapper allows to use fixed step handlers with general integrators which cannot guaranty their integration steps
        will remain constant and therefore only accept general step handlers.
    
        The stepsize used is selected at construction time. The
        :meth:`~org.hipparchus.ode.sampling.ODEFixedStepHandler.handleStep` method of the underlying
        :class:`~org.hipparchus.ode.sampling.ODEFixedStepHandler` object is called at normalized times. The normalized times can
        be influenced by the :class:`~org.hipparchus.ode.sampling.StepNormalizerMode` and
        :class:`~org.hipparchus.ode.sampling.StepNormalizerBounds`.
    
        There is no constraint on the integrator, it can use any time step it needs (time steps longer or shorter than the fixed
        time step and non-integer ratios are all allowed).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
              - :class:`~org.hipparchus.ode.sampling.ODEFixedStepHandler`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizerMode`
              - :class:`~org.hipparchus.ode.sampling.StepNormalizerBounds`
    """
    @typing.overload
    def __init__(self, double: float, oDEFixedStepHandler: typing.Union[ODEFixedStepHandler, typing.Callable]): ...
    @typing.overload
    def __init__(self, double: float, oDEFixedStepHandler: typing.Union[ODEFixedStepHandler, typing.Callable], stepNormalizerBounds: StepNormalizerBounds): ...
    @typing.overload
    def __init__(self, double: float, oDEFixedStepHandler: typing.Union[ODEFixedStepHandler, typing.Callable], stepNormalizerMode: StepNormalizerMode): ...
    @typing.overload
    def __init__(self, double: float, oDEFixedStepHandler: typing.Union[ODEFixedStepHandler, typing.Callable], stepNormalizerMode: StepNormalizerMode, stepNormalizerBounds: StepNormalizerBounds): ...
    def finish(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> None:
        """
            Finalize integration.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.finish` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
        
            Parameters:
                finalState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): state at integration end
        
        
        """
        ...
    def handleStep(self, oDEStateInterpolator: ODEStateInterpolator) -> None:
        """
            Handle the last accepted step.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.handleStep` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
        
            Parameters:
                interpolator (:class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None:
        """
            Initialize step handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.init` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
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
