
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.hipparchus
import org.orekit.frames
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



_FieldOrekitFixedStepHandler__T = typing.TypeVar('_FieldOrekitFixedStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitFixedStepHandler(typing.Generic[_FieldOrekitFixedStepHandler__T]):
    """
    This interface is a space-dynamics aware fixed size step handler.
    
    It mirrors the FixedStepHandler interface from commons but provides a space-dynamics interface to the methods.
    """
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitFixedStepHandler__T]) -> None:
        """
        Finalize propagation.
        
        Parameters:
            finalState (FieldSpacecraftState<FieldOrekitFixedStepHandler> finalState): state at propagation end
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, currentState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitFixedStepHandler__T]) -> None:
        """
        Handle the current step.
        
        Parameters:
            currentState (FieldSpacecraftState<FieldOrekitFixedStepHandler> currentState): current state at step time
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitFixedStepHandler__T], t: org.orekit.time.FieldAbsoluteDate[_FieldOrekitFixedStepHandler__T], step: _FieldOrekitFixedStepHandler__T) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Parameters:
            s0 (FieldSpacecraftState<FieldOrekitFixedStepHandler> s0): initial state
            t (FieldAbsoluteDate<FieldOrekitFixedStepHandler> t): target time for the integration
            step (FieldOrekitFixedStepHandler): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        
        """
        ...

_FieldOrekitStepHandler__T = typing.TypeVar('_FieldOrekitStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitStepHandler(typing.Generic[_FieldOrekitStepHandler__T]):
    """
    This interface is a space-dynamics aware step handler.
    
    It mirrors the StepHandler interface from commons but provides a space-dynamics interface to the methods.
    """
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepHandler__T]) -> None:
        """
        Finalize propagation.
        
        Parameters:
            finalState (FieldSpacecraftState<FieldOrekitStepHandler> finalState): state at propagation end
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolator: 'FieldOrekitStepInterpolator'[_FieldOrekitStepHandler__T]) -> None:
        """
        Handle the current step.
        
        Parameters:
            interpolator (FieldOrekitStepInterpolator<FieldOrekitStepHandler> interpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepHandler__T], t: org.orekit.time.FieldAbsoluteDate[_FieldOrekitStepHandler__T]) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Parameters:
            s0 (FieldSpacecraftState<FieldOrekitStepHandler> s0): initial state
            t (FieldAbsoluteDate<FieldOrekitStepHandler> t): target time for the integration
        
        
        """
        ...

_FieldOrekitStepInterpolator__T = typing.TypeVar('_FieldOrekitStepInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitStepInterpolator(org.orekit.utils.FieldPVCoordinatesProvider[_FieldOrekitStepInterpolator__T], typing.Generic[_FieldOrekitStepInterpolator__T]):
    """
    This interface is a space-dynamics aware step interpolator.
    
    It mirrors the StepInterpolator interface from commons but provides a space-dynamics interface to the methods.
    """
    def getCurrentState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]:
        """
        Get the state at previous grid point date.
        
        Returns:
            state at previous grid point date
        
        
        """
        ...
    def getInterpolatedState(self, date: org.orekit.time.FieldAbsoluteDate[_FieldOrekitStepInterpolator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]:
        """
        Get the state at interpolated date.
        
        Parameters:
            date (FieldAbsoluteDate<FieldOrekitStepInterpolator> date): date of the interpolated state
        
        Returns:
            state at interpolated date the date
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_FieldOrekitStepInterpolator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldOrekitStepInterpolator__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<FieldOrekitStepInterpolator> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        Since:
            12.0
        
        
        """
        ...
    def getPreviousState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]:
        """
        Get the state at previous grid point date.
        
        Returns:
            state at previous grid point date
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check is integration direction is forward in date.
        
        Returns:
            true if integration is forward in date
        
        
        """
        ...
    def restrictStep(self, newPreviousState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T], newCurrentState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]) -> 'FieldOrekitStepInterpolator'[_FieldOrekitStepInterpolator__T]:
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Parameters:
            newPreviousState (FieldSpacecraftState<FieldOrekitStepInterpolator> newPreviousState): start of the restricted step
            newCurrentState (FieldSpacecraftState<FieldOrekitStepInterpolator> newCurrentState): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Since:
            11.0
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

class MultiSatFixedStepHandler:
    """
    This interface is a space-dynamics aware fixed step handler for PropagatorsParallelizer.
    
    It is a multi-satellite version of the OrekitFixedStepHandler.
    
    Since:
        12.0
    """
    def finish(self, finalStates: java.util.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
        Finalize propagation.
        
        Parameters:
            finalStates (List<SpacecraftState> finalStates): states at propagation end
        
        
        """
        ...
    def handleStep(self, states: java.util.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
        Handle the current step.
        
        When called by PropagatorsParallelizer, all states have the same date.
        
        Parameters:
            states (List<SpacecraftState> states): states in the same order used to  the
                PropagatorsParallelizer
        
        
        """
        ...
    def init(self, states0: java.util.List[org.orekit.propagation.SpacecraftState], t: org.orekit.time.AbsoluteDate, step: float) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Parameters:
            states0 (List<SpacecraftState> states0): initial states, one for each satellite in the same order used to
                 the
                PropagatorsParallelizer.
            t (AbsoluteDate): target time for the integration
            step (double): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        
        """
        ...

class MultiSatStepHandler:
    """
    This interface is a space-dynamics aware step handler for PropagatorsParallelizer.
    
    It is a multi-satellite version of the OrekitStepHandler.
    
    Since:
        9.0
    """
    def finish(self, finalStates: java.util.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
        Finalize propagation.
        
        Parameters:
            finalStates (List<SpacecraftState> finalStates): states at propagation end
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolators: java.util.List['OrekitStepInterpolator']) -> None:
        """
        Handle the current step.
        
        When called by PropagatorsParallelizer, all interpolators have the same time range.
        
        Parameters:
            interpolators (List<OrekitStepInterpolator> interpolators): interpolators set up for the current step in the same order used to
                 the
                PropagatorsParallelizer
        
        
        """
        ...
    def init(self, states0: java.util.List[org.orekit.propagation.SpacecraftState], t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Parameters:
            states0 (List<SpacecraftState> states0): initial states, one for each satellite in the same order used to
                 the
                PropagatorsParallelizer.
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class OrekitFixedStepHandler:
    """
    This interface is a space-dynamics aware fixed size step handler.
    
    It mirrors the FixedStepHandler interface from org but provides a space-dynamics interface to the methods.
    """
    def finish(self, finalState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Finalize propagation.
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, currentState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Handle the current step.
        
        Parameters:
            currentState (SpacecraftState): current state at step time
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate, step: float) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
            step (double): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        Since:
            9.0
        
        
        """
        ...

class OrekitStepHandler:
    """
    This interface is a space-dynamics aware step handler.
    
    It mirrors the StepHandler interface from org but provides a space-dynamics interface to the methods.
    """
    def finish(self, finalState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Finalize propagation.
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolator: 'OrekitStepInterpolator') -> None:
        """
        Handle the current step.
        
        Parameters:
            interpolator (OrekitStepInterpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class OrekitStepInterpolator(org.orekit.utils.PVCoordinatesProvider):
    """
    This interface is a space-dynamics aware step interpolator.
    
    It mirrors the ODEStateInterpolator interface from org but provides a space-dynamics interface to the methods.
    """
    def getCurrentState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get the state at current grid point date.
        
        Returns:
            state at current grid point date
        
        
        """
        ...
    def getInterpolatedState(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
        Get the state at interpolated date.
        
        Parameters:
            date (AbsoluteDate): date of the interpolated state
        
        Returns:
            state at interpolated date
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        Since:
            12.0
        
        
        """
        ...
    def getPreviousState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get the state at previous grid point date.
        
        Returns:
            state at previous grid point date
        
        
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
        Check is integration direction is forward in date.
        
        Returns:
            true if integration is forward in date
        
        
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
    def restrictStep(self, newPreviousState: org.orekit.propagation.SpacecraftState, newCurrentState: org.orekit.propagation.SpacecraftState) -> 'OrekitStepInterpolator':
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Parameters:
            newPreviousState (SpacecraftState): start of the restricted step
            newCurrentState (SpacecraftState): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Since:
            9.0
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

_FieldOrekitStepNormalizer__T = typing.TypeVar('_FieldOrekitStepNormalizer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitStepNormalizer(FieldOrekitStepHandler[_FieldOrekitStepNormalizer__T], typing.Generic[_FieldOrekitStepNormalizer__T]):
    """
    This class wraps an object implementing OrekitFixedStepHandler into a OrekitStepHandler.
    
    It mirrors the StepNormalizer interface from commons but provides a space-dynamics interface to the methods.
    """
    def __init__(self, h: _FieldOrekitStepNormalizer__T, handler: typing.Union[FieldOrekitFixedStepHandler[_FieldOrekitStepNormalizer__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], None]]):
        """
        Simple constructor.
        
        Parameters:
            h (FieldOrekitStepNormalizer): fixed time step (sign is not used)
            handler (FieldOrekitFixedStepHandler<FieldOrekitStepNormalizer> handler): fixed time step handler to wrap
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepNormalizer__T]) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface FieldOrekitStepHandler
        
        Parameters:
            finalState (FieldSpacecraftState<FieldOrekitStepNormalizer> finalState): state at propagation end
        
        
        """
        ...
    def getFixedStepHandler(self) -> FieldOrekitFixedStepHandler[_FieldOrekitStepNormalizer__T]:
        """
        Get the underlying fixed step handler.
        
        Returns:
            underlying fixed step handler
        
        Since:
            11.0
        
        
        """
        ...
    def getFixedTimeStep(self) -> _FieldOrekitStepNormalizer__T:
        """
        Get the fixed time step.
        
        Returns:
            fixed time step
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolator: FieldOrekitStepInterpolator[_FieldOrekitStepNormalizer__T]) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface FieldOrekitStepHandler
        
        Parameters:
            interpolator (FieldOrekitStepInterpolator<FieldOrekitStepNormalizer> interpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepNormalizer__T], t: org.orekit.time.FieldAbsoluteDate[_FieldOrekitStepNormalizer__T]) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Specified by: init in interface FieldOrekitStepHandler
        
        Parameters:
            s0 (FieldSpacecraftState<FieldOrekitStepNormalizer> s0): initial state
            t (FieldAbsoluteDate<FieldOrekitStepNormalizer> t): target time for the integration
        
        
        """
        ...
    def requiresDenseOutput(self) -> bool:
        """
        Determines whether this handler needs dense output. This handler needs dense output in order to provide data at regularly spaced steps regardless of the steps the propagator uses, so this method always returns true.
        
        Returns:
            always true
        
        
        """
        ...

_FieldPropagationStepRecorder__T = typing.TypeVar('_FieldPropagationStepRecorder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPropagationStepRecorder(FieldOrekitStepHandler[_FieldPropagationStepRecorder__T], typing.Generic[_FieldPropagationStepRecorder__T]):
    """
    Step handler recording states. Automatically clears them at start of propagation.
    
    Since:
        13.0
    
    Also see:
        PropagationStepRecorder
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, resetAutomatically: bool): ...
    def copyStates(self) -> java.util.List[org.orekit.propagation.FieldSpacecraftState[_FieldPropagationStepRecorder__T]]:
        """
        Copy the current saved steps.
        
        Returns:
            copy of steps
        
        
        """
        ...
    def handleStep(self, interpolator: FieldOrekitStepInterpolator[_FieldPropagationStepRecorder__T]) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface FieldOrekitStepHandler
        
        Parameters:
            interpolator (FieldOrekitStepInterpolator<FieldPropagationStepRecorder> interpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldPropagationStepRecorder__T], t: org.orekit.time.FieldAbsoluteDate[_FieldPropagationStepRecorder__T]) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Specified by: init in interface FieldOrekitStepHandler
        
        Parameters:
            s0 (FieldSpacecraftState<FieldPropagationStepRecorder> s0): initial state
            t (FieldAbsoluteDate<FieldPropagationStepRecorder> t): target time for the integration
        
        
        """
        ...
    def isResetAutomatically(self) -> bool:
        """
        Getter for resetting flag.
        
        Returns:
            flag
        
        Since:
            13.1
        
        
        """
        ...
    def setResetAutomatically(self, resetAutomatically: bool) -> None:
        """
        Setter for resetting flag.
        
        Parameters:
            resetAutomatically (boolean): flag
        
        Since:
            13.1
        
        
        """
        ...

_FieldStepHandlerMultiplexer__T = typing.TypeVar('_FieldStepHandlerMultiplexer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStepHandlerMultiplexer(FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T], typing.Generic[_FieldStepHandlerMultiplexer__T]):
    """
    This class gathers several OrekitStepHandler instances into one.
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    @typing.overload
    def add(self, h: _FieldStepHandlerMultiplexer__T, handler: typing.Union[FieldOrekitFixedStepHandler[_FieldStepHandlerMultiplexer__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...
    @typing.overload
    def add(self, handler: typing.Union[FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T], typing.Callable[[FieldOrekitStepInterpolator[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...
    def clear(self) -> None:
        """
        Remove all handlers managed by this multiplexer.
        
        If propagation is ongoing (i.e. global init already called and global finish not called yet), then the local finish and finish methods of the removed handlers will be called with the last known state, so the handlers stop properly.
        
        Since:
            11.0
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_FieldStepHandlerMultiplexer__T]) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface FieldOrekitStepHandler
        
        Parameters:
            finalState (FieldSpacecraftState<FieldStepHandlerMultiplexer> finalState): state at propagation end
        
        
        """
        ...
    def getHandlers(self) -> java.util.List[FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T]]:
        """
        Get an unmodifiable view of all handlers.
        
        Note that if FieldOrekitFixedStepHandler have been add, then they will show up wrapped within FieldOrekitStepNormalizer.
        
        Returns:
            an unmodifiable view of all handlers
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolator: FieldOrekitStepInterpolator[_FieldStepHandlerMultiplexer__T]) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface FieldOrekitStepHandler
        
        Parameters:
            interpolator (FieldOrekitStepInterpolator<FieldStepHandlerMultiplexer> interpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_FieldStepHandlerMultiplexer__T], t: org.orekit.time.FieldAbsoluteDate[_FieldStepHandlerMultiplexer__T]) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Specified by: init in interface FieldOrekitStepHandler
        
        Parameters:
            s0 (FieldSpacecraftState<FieldStepHandlerMultiplexer> s0): initial state
            t (FieldAbsoluteDate<FieldStepHandlerMultiplexer> t): target time for the integration
        
        
        """
        ...
    @typing.overload
    def remove(self, handler: typing.Union[FieldOrekitFixedStepHandler[_FieldStepHandlerMultiplexer__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...
    @typing.overload
    def remove(self, handler: typing.Union[FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T], typing.Callable[[FieldOrekitStepInterpolator[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...

class MultisatStepNormalizer(MultiSatStepHandler):
    """
    This class wraps an object implementing MultiSatFixedStepHandler into a MultiSatStepHandler.
    
    It mirrors the StepNormalizer interface from org but provides a space-dynamics interface to the methods.
    
    Since:
        12.0
    """
    def __init__(self, h: float, handler: typing.Union[MultiSatFixedStepHandler, typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            h (double): fixed time step (sign is not used)
            handler (MultiSatFixedStepHandler): fixed time step handler to wrap
        
        
        """
        ...
    def finish(self, finalStates: java.util.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface MultiSatStepHandler
        
        Parameters:
            finalStates (List<SpacecraftState> finalStates): states at propagation end
        
        
        """
        ...
    def getFixedStepHandler(self) -> MultiSatFixedStepHandler:
        """
        Get the underlying fixed step handler.
        
        Returns:
            underlying fixed step handler
        
        
        """
        ...
    def getFixedTimeStep(self) -> float:
        """
        Get the fixed time step.
        
        Returns:
            fixed time step
        
        
        """
        ...
    def handleStep(self, interpolators: java.util.List[OrekitStepInterpolator]) -> None:
        """
        Handle the current step.
        
        When called by PropagatorsParallelizer, all interpolators have the same time range.
        
        Specified by: handleStep in interface MultiSatStepHandler
        
        Parameters:
            interpolators (List<OrekitStepInterpolator> interpolators): interpolators set up for the current step in the same order used to
                 the
                PropagatorsParallelizer
        
        
        """
        ...
    def init(self, s0: java.util.List[org.orekit.propagation.SpacecraftState], t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface MultiSatStepHandler
        
        Parameters:
            s0 (List<SpacecraftState> s0): initial states, one for each satellite in the same order used to
                 the
                PropagatorsParallelizer.
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class OrekitStepNormalizer(OrekitStepHandler):
    """
    This class wraps an object implementing OrekitFixedStepHandler into a OrekitStepHandler.
    
    It mirrors the StepNormalizer interface from org but provides a space-dynamics interface to the methods.
    """
    def __init__(self, h: float, handler: typing.Union[OrekitFixedStepHandler, typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            h (double): fixed time step (sign is not used)
            handler (OrekitFixedStepHandler): fixed time step handler to wrap
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface OrekitStepHandler
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
        
        
        """
        ...
    def getFixedStepHandler(self) -> OrekitFixedStepHandler:
        """
        Get the underlying fixed step handler.
        
        Returns:
            underlying fixed step handler
        
        Since:
            11.0
        
        
        """
        ...
    def getFixedTimeStep(self) -> float:
        """
        Get the fixed time step.
        
        Returns:
            fixed time step
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolator: OrekitStepInterpolator) -> None:
        """
        Handle the last accepted step.
        
        Specified by: handleStep in interface OrekitStepHandler
        
        Parameters:
            interpolator (OrekitStepInterpolator): interpolator for the last accepted step. For efficiency purposes, the various propagators reuse the same object on each
                call, so if the instance wants to keep it across all calls (for example to provide at the end of the propagation a
                continuous model valid throughout the propagation range), it should build a local copy using the clone method and store
                this copy.
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface OrekitStepHandler
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...

class PropagationStepRecorder(OrekitStepHandler):
    """
    Step handler recording states. Automatically clears them at start of propagation.
    
    Since:
        13.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, resetAutomatically: bool): ...
    def copyStates(self) -> java.util.List[org.orekit.propagation.SpacecraftState]:
        """
        Copy the current saved steps.
        
        Returns:
            copy of steps
        
        
        """
        ...
    def handleStep(self, interpolator: OrekitStepInterpolator) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface OrekitStepHandler
        
        Parameters:
            interpolator (OrekitStepInterpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface OrekitStepHandler
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    def isResetAutomatically(self) -> bool:
        """
        Getter for resetting flag.
        
        Returns:
            flag
        
        Since:
            13.1
        
        
        """
        ...
    def setResetAutomatically(self, resetAutomatically: bool) -> None:
        """
        Setter for resetting flag.
        
        Parameters:
            resetAutomatically (boolean): flag
        
        Since:
            13.1
        
        
        """
        ...

_PythonFieldOrekitFixedStepHandler__T = typing.TypeVar('_PythonFieldOrekitFixedStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldOrekitFixedStepHandler(FieldOrekitFixedStepHandler[_PythonFieldOrekitFixedStepHandler__T], typing.Generic[_PythonFieldOrekitFixedStepHandler__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitFixedStepHandler__T]) -> None:
        """
        Description copied from interface: finish Finalize propagation.
        
        Specified by: finish in interface FieldOrekitFixedStepHandler
        
        Parameters:
            finalState (FieldSpacecraftState<PythonFieldOrekitFixedStepHandler> finalState): state at propagation end
        
        
        """
        ...
    def handleStep(self, currentState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitFixedStepHandler__T]) -> None:
        """
        Description copied from interface: handleStep Handle the current step.
        
        Specified by: handleStep in interface FieldOrekitFixedStepHandler
        
        Parameters:
            currentState (FieldSpacecraftState<PythonFieldOrekitFixedStepHandler> currentState): current state at step time
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitFixedStepHandler__T], t: org.orekit.time.FieldAbsoluteDate[_PythonFieldOrekitFixedStepHandler__T], step: _PythonFieldOrekitFixedStepHandler__T) -> None:
        """
        Description copied from interface: init Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Specified by: init in interface FieldOrekitFixedStepHandler
        
        Parameters:
            s0 (FieldSpacecraftState<PythonFieldOrekitFixedStepHandler> s0): initial state
            t (FieldAbsoluteDate<PythonFieldOrekitFixedStepHandler> t): target time for the integration
            step (PythonFieldOrekitFixedStepHandler): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        
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

_PythonFieldOrekitStepHandler__T = typing.TypeVar('_PythonFieldOrekitStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldOrekitStepHandler(FieldOrekitStepHandler[_PythonFieldOrekitStepHandler__T], typing.Generic[_PythonFieldOrekitStepHandler__T]):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepHandler__T]) -> None: ...
    def handleStep(self, fieldOrekitStepInterpolator: FieldOrekitStepInterpolator[_PythonFieldOrekitStepHandler__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldOrekitStepHandler__T]) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldOrekitStepInterpolator__T = typing.TypeVar('_PythonFieldOrekitStepInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldOrekitStepInterpolator(FieldOrekitStepInterpolator[_PythonFieldOrekitStepInterpolator__T], typing.Generic[_PythonFieldOrekitStepInterpolator__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCurrentState(self) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]:
        """
        Get the state at previous grid point date.
        
        Specified by: getCurrentState in interface FieldOrekitStepInterpolator
        
        Returns:
            state at previous grid point date
        
        
        """
        ...
    def getInterpolatedState(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldOrekitStepInterpolator__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]:
        """
        Get the state at interpolated date.
        
        Specified by: getInterpolatedState in interface FieldOrekitStepInterpolator
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldOrekitStepInterpolator> date): date of the interpolated state
        
        Returns:
            state at interpolated date the date
        
        
        """
        ...
    def getPreviousState(self) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]:
        """
        Get the state at previous grid point date.
        
        Specified by: getPreviousState in interface FieldOrekitStepInterpolator
        
        Returns:
            state at previous grid point date
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check is integration direction is forward in date.
        
        Specified by: isForward in interface FieldOrekitStepInterpolator
        
        Returns:
            true if integration is forward in date
        
        
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
    def restrictStep(self, newPreviousState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T], newCurrentState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]) -> FieldOrekitStepInterpolator[_PythonFieldOrekitStepInterpolator__T]:
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Specified by: restrictStep in interface FieldOrekitStepInterpolator
        
        Parameters:
            newPreviousState (FieldSpacecraftState<PythonFieldOrekitStepInterpolator> newPreviousState): start of the restricted step
            newCurrentState (FieldSpacecraftState<PythonFieldOrekitStepInterpolator> newCurrentState): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Since:
            11.0
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

class PythonMultiSatFixedStepHandler(MultiSatFixedStepHandler):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finish(self, finalStates: java.util.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
        Description copied from interface: finish Finalize propagation.
        
        Specified by: finish in interface MultiSatFixedStepHandler
        
        Parameters:
            finalStates (List<SpacecraftState> finalStates): states at propagation end
        
        
        """
        ...
    def handleStep(self, states: java.util.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
        Description copied from interface: handleStep Handle the current step.
        
        When called by PropagatorsParallelizer, all states have the same date.
        
        Specified by: handleStep in interface MultiSatFixedStepHandler
        
        Parameters:
            states (List<SpacecraftState> states): states in the same order used to  the
                PropagatorsParallelizer
        
        
        """
        ...
    def init(self, states0: java.util.List[org.orekit.propagation.SpacecraftState], t: org.orekit.time.AbsoluteDate, step: float) -> None:
        """
        Description copied from interface: init Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface MultiSatFixedStepHandler
        
        Parameters:
            states0 (List<SpacecraftState> states0): initial states, one for each satellite in the same order used to
                 the
                PropagatorsParallelizer.
            t (AbsoluteDate): target time for the integration
            step (double): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonMultiSatStepHandler(MultiSatStepHandler):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finish(self, finalStates: java.util.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface MultiSatStepHandler
        
        Parameters:
            finalStates (List<SpacecraftState> finalStates): states at propagation end
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolators: java.util.List[OrekitStepInterpolator]) -> None:
        """
        Handle the current step.
        
        When called by PropagatorsParallelizer, all interpolators have the same time range.
        
        Specified by: handleStep in interface MultiSatStepHandler
        
        Parameters:
            interpolators (List<OrekitStepInterpolator> interpolators): interpolators set up for the current step in the same order used to
                 the
                PropagatorsParallelizer
        
        
        """
        ...
    def init(self, states0: java.util.List[org.orekit.propagation.SpacecraftState], t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface MultiSatStepHandler
        
        Parameters:
            states0 (List<SpacecraftState> states0): initial states, one for each satellite in the same order used to
                 the
                PropagatorsParallelizer.
            t (AbsoluteDate): target time for the integration
        
        
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

class PythonOrekitFixedStepHandler(OrekitFixedStepHandler):
    """
    This interface is a space-dynamics aware fixed size step handler.
    
    It mirrors the FixedStepHandler interface from `commons-math <http://commons.apache.org/math/>` but provides a space-dynamics interface to the methods.
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface OrekitFixedStepHandler
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
        
        
        """
        ...
    def handleStep(self, currentState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface OrekitFixedStepHandler
        
        Parameters:
            currentState (SpacecraftState): current state at step time
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate, step: float) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Specified by: init in interface OrekitFixedStepHandler
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
            step (double): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonOrekitStepHandler(OrekitStepHandler):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface OrekitStepHandler
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolator: OrekitStepInterpolator) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface OrekitStepHandler
        
        Parameters:
            interpolator (OrekitStepInterpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation. Extension point for Python.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface OrekitStepHandler
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
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

class PythonOrekitStepInterpolator(OrekitStepInterpolator):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCurrentState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get the state at current grid point date. Extension point for Python.
        
        Specified by: getCurrentState in interface OrekitStepInterpolator
        
        Returns:
            state at current grid point date
        
        
        """
        ...
    def getInterpolatedState(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
        Get the state at interpolated date.
        
        Specified by: getInterpolatedState in interface OrekitStepInterpolator
        
        Parameters:
            date (AbsoluteDate): date of the interpolated state
        
        Returns:
            state at interpolated date
        
        
        """
        ...
    def getPreviousState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get the state at previous grid point date. Extension point for Python.
        
        Specified by: getPreviousState in interface OrekitStepInterpolator
        
        Returns:
            state at previous grid point date
        
        
        """
        ...
    def isCurrentStateInterpolated(self) -> bool:
        """
        Determines if the getCurrentState is computed directly by the integrator, or if it is calculated using getInterpolatedState. Extension point for Python.
        
        Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
        Specified by: isCurrentStateInterpolated in interface OrekitStepInterpolator
        
        Returns:
            true if the current state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
        Check is integration direction is forward in date.
        
        Specified by: isForward in interface OrekitStepInterpolator
        
        Returns:
            true if integration is forward in date
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
        Determines if the getPreviousState is computed directly by the integrator, or if it is calculated using getInterpolatedState. Extension point for Python.
        
        Typically the previous state is directly computed by the integrator, but when events are detected the steps are shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
        Specified by: isPreviousStateInterpolated in interface OrekitStepInterpolator
        
        Returns:
            true if the previous state was calculated by the interpolator and false if it was computed directly by the
            integrator.
        
        
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
    def restrictStep(self, newPreviousState: org.orekit.propagation.SpacecraftState, newCurrentState: org.orekit.propagation.SpacecraftState) -> OrekitStepInterpolator:
        """
        Create a new restricted version of the instance.
        
        The instance is not changed at all.
        
        Specified by: restrictStep in interface OrekitStepInterpolator
        
        Parameters:
            newPreviousState (SpacecraftState): start of the restricted step
            newCurrentState (SpacecraftState): end of the restricted step
        
        Returns:
            restricted version of the instance
        
        Since:
            9.0
        
        Also see:
            getPreviousState,
            getCurrentState
        
        
        """
        ...

class StepHandlerMultiplexer(OrekitStepHandler):
    """
    This class gathers several OrekitStepHandler instances into one.
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    @typing.overload
    def add(self, h: float, handler: typing.Union[OrekitFixedStepHandler, typing.Callable]) -> None:
        """
        Add a handler for fixed size step.
        
        If propagation is ongoing (i.e. global init already called and global finish not called yet), then the local init method of the added handler will be called with the last known state, so the handler starts properly.
        
        Parameters:
            h (double): fixed stepsize (s)
            handler (OrekitFixedStepHandler): handler called at the end of each finalized step
        
        Since:
            11.0
        
        
        """
        ...
    @typing.overload
    def add(self, handler: typing.Union[OrekitStepHandler, typing.Callable]) -> None:
        """
        Add a handler for variable size step.
        
        If propagation is ongoing (i.e. global init already called and global finish not called yet), then the local init method of the added handler will be called with the last known state, so the handler starts properly.
        
        Parameters:
            handler (OrekitStepHandler): step handler to add
        
        """
        ...
    def clear(self) -> None:
        """
        Remove all handlers managed by this multiplexer.
        
        If propagation is ongoing (i.e. global init already called and global finish not called yet), then the local finish and finish methods of the removed handlers will be called with the last known state, so the handlers stop properly.
        
        Since:
            11.0
        
        
        """
        ...
    def finish(self, finalState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Finalize propagation.
        
        Specified by: finish in interface OrekitStepHandler
        
        Parameters:
            finalState (SpacecraftState): state at propagation end
        
        
        """
        ...
    def getHandlers(self) -> java.util.List[OrekitStepHandler]:
        """
        Get an unmodifiable view of all handlers.
        
        Note that if OrekitFixedStepHandler have been add, then they will show up wrapped within OrekitStepNormalizer.
        
        Returns:
            an unmodifiable view of all handlers
        
        Since:
            11.0
        
        
        """
        ...
    def handleStep(self, interpolator: OrekitStepInterpolator) -> None:
        """
        Handle the current step.
        
        Specified by: handleStep in interface OrekitStepHandler
        
        Parameters:
            interpolator (OrekitStepInterpolator): interpolator set up for the current step
        
        
        """
        ...
    def init(self, s0: org.orekit.propagation.SpacecraftState, t: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        The default method does nothing
        
        Specified by: init in interface OrekitStepHandler
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
        
        
        """
        ...
    @typing.overload
    def remove(self, handler: typing.Union[OrekitFixedStepHandler, typing.Callable]) -> None:
        """
        Remove a handler.
        
        If propagation is ongoing (i.e. global init already called and global finish not called yet), then the local finish method of the removed handler will be called with the last known state, so the handler stops properly.
        
        Parameters:
            handler (OrekitStepHandler): step handler to remove
        
        Since:
            11.0
        
        Remove a handler.
        
        If propagation is ongoing (i.e. global init already called and global finish not called yet), then the local finish method of the removed handler will be called with the last known state, so the handler stops properly.
        
        Parameters:
            handler (OrekitFixedStepHandler): step handler to remove
        
        Since:
            11.0
        
        
        """
        ...
    @typing.overload
    def remove(self, handler: typing.Union[OrekitStepHandler, typing.Callable]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.sampling")``.

    FieldOrekitFixedStepHandler: typing.Type[FieldOrekitFixedStepHandler]
    FieldOrekitStepHandler: typing.Type[FieldOrekitStepHandler]
    FieldOrekitStepInterpolator: typing.Type[FieldOrekitStepInterpolator]
    FieldOrekitStepNormalizer: typing.Type[FieldOrekitStepNormalizer]
    FieldPropagationStepRecorder: typing.Type[FieldPropagationStepRecorder]
    FieldStepHandlerMultiplexer: typing.Type[FieldStepHandlerMultiplexer]
    MultiSatFixedStepHandler: typing.Type[MultiSatFixedStepHandler]
    MultiSatStepHandler: typing.Type[MultiSatStepHandler]
    MultisatStepNormalizer: typing.Type[MultisatStepNormalizer]
    OrekitFixedStepHandler: typing.Type[OrekitFixedStepHandler]
    OrekitStepHandler: typing.Type[OrekitStepHandler]
    OrekitStepInterpolator: typing.Type[OrekitStepInterpolator]
    OrekitStepNormalizer: typing.Type[OrekitStepNormalizer]
    PropagationStepRecorder: typing.Type[PropagationStepRecorder]
    PythonFieldOrekitFixedStepHandler: typing.Type[PythonFieldOrekitFixedStepHandler]
    PythonFieldOrekitStepHandler: typing.Type[PythonFieldOrekitStepHandler]
    PythonFieldOrekitStepInterpolator: typing.Type[PythonFieldOrekitStepInterpolator]
    PythonMultiSatFixedStepHandler: typing.Type[PythonMultiSatFixedStepHandler]
    PythonMultiSatStepHandler: typing.Type[PythonMultiSatStepHandler]
    PythonOrekitFixedStepHandler: typing.Type[PythonOrekitFixedStepHandler]
    PythonOrekitStepHandler: typing.Type[PythonOrekitStepHandler]
    PythonOrekitStepInterpolator: typing.Type[PythonOrekitStepInterpolator]
    StepHandlerMultiplexer: typing.Type[StepHandlerMultiplexer]
