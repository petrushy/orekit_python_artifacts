import java.util
import org.hipparchus
import org.orekit.propagation
import org.orekit.time
import typing



_FieldOrekitFixedStepHandler__T = typing.TypeVar('_FieldOrekitFixedStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitFixedStepHandler(typing.Generic[_FieldOrekitFixedStepHandler__T]):
    """
    public interface FieldOrekitFixedStepHandler<T extends CalculusFieldElement<T>>
    
        This interface is a space-dynamics aware fixed size step handler.
    
        It mirrors the :code:`FixedStepHandler` interface from `commons-math <http://commons.apache.org/math/>` but provides a
        space-dynamics interface to the methods.
    """
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitFixedStepHandler__T]) -> None: ...
    def handleStep(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitFixedStepHandler__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitFixedStepHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrekitFixedStepHandler__T], t: _FieldOrekitFixedStepHandler__T) -> None: ...

_FieldOrekitStepHandler__T = typing.TypeVar('_FieldOrekitStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitStepHandler(typing.Generic[_FieldOrekitStepHandler__T]):
    """
    public interface FieldOrekitStepHandler<T extends CalculusFieldElement<T>>
    
        This interface is a space-dynamics aware step handler.
    
        It mirrors the :code:`StepHandler` interface from ` commons-math <http://commons.apache.org/math/>` but provides a
        space-dynamics interface to the methods.
    """
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepHandler__T]) -> None: ...
    def handleStep(self, fieldOrekitStepInterpolator: 'FieldOrekitStepInterpolator'[_FieldOrekitStepHandler__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrekitStepHandler__T]) -> None: ...

_FieldOrekitStepInterpolator__T = typing.TypeVar('_FieldOrekitStepInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitStepInterpolator(typing.Generic[_FieldOrekitStepInterpolator__T]):
    """
    public interface FieldOrekitStepInterpolator<T extends CalculusFieldElement<T>>
    
        This interface is a space-dynamics aware step interpolator.
    
        It mirrors the :code:`StepInterpolator` interface from ` commons-math <http://commons.apache.org/math/>` but provides a
        space-dynamics interface to the methods.
    """
    def getCurrentState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]: ...
    def getInterpolatedState(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrekitStepInterpolator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]: ...
    def getPreviousState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]: ...
    def isForward(self) -> bool:
        """
            Check is integration direction is forward in date.
        
            Returns:
                true if integration is forward in date
        
        
        """
        ...
    def restrictStep(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T], fieldSpacecraftState2: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepInterpolator__T]) -> 'FieldOrekitStepInterpolator'[_FieldOrekitStepInterpolator__T]: ...

class MultiSatStepHandler:
    """
    public interface MultiSatStepHandler
    
        This interface is a space-dynamics aware step handler for :class:`~org.orekit.propagation.PropagatorsParallelizer`.
    
        It is a multi-satellite version of the :class:`~org.orekit.propagation.sampling.OrekitStepHandler`.
    
        Since:
            9.0
    """
    def finish(self, list: java.util.List[org.orekit.propagation.SpacecraftState]) -> None: ...
    def handleStep(self, list: java.util.List['OrekitStepInterpolator']) -> None: ...
    def init(self, list: java.util.List[org.orekit.propagation.SpacecraftState], absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class OrekitFixedStepHandler:
    """
    @FunctionalInterface public interface OrekitFixedStepHandler
    
        This interface is a space-dynamics aware fixed size step handler.
    
        It mirrors the :code:`FixedStepHandler` interface from Hipparchus but provides a space-dynamics interface to the
        methods.
    """
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Finalize propagation.
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
            Since:
                11.0
        
        
        """
        ...
    def handleStep(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Handle the current step.
        
            Parameters:
                currentState (:class:`~org.orekit.propagation.SpacecraftState`): current state at step time
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> None:
        """
            Initialize step handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
                step (double): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
            Since:
                9.0
        
        
        """
        ...

class OrekitStepHandler:
    """
    public interface OrekitStepHandler
    
        This interface is a space-dynamics aware step handler.
    
        It mirrors the :code:`StepHandler` interface from Hipparchus but provides a space-dynamics interface to the methods.
    """
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Finalize propagation.
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
            Since:
                11.0
        
        
        """
        ...
    def handleStep(self, orekitStepInterpolator: 'OrekitStepInterpolator') -> None:
        """
            Handle the current step.
        
            Parameters:
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): interpolator set up for the current step
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize step handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default method does nothing
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class OrekitStepInterpolator:
    """
    public interface OrekitStepInterpolator
    
        This interface is a space-dynamics aware step interpolator.
    
        It mirrors the :code:`ODEStateInterpolator` interface from Hipparchus but provides a space-dynamics interface to the
        methods.
    """
    def getCurrentState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Get the state at current grid point date.
        
            Returns:
                state at current grid point date
        
        
        """
        ...
    def getInterpolatedState(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
            Get the state at interpolated date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the interpolated state
        
            Returns:
                state at interpolated date
        
        
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
            Determines if the :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getCurrentState` is computed directly
            by the integrator, or if it is calculated using
            :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getInterpolatedState`.
        
            Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened
            so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
            Returns:
                :code:`true` if the current state was calculated by the interpolator and false if it was computed directly by the
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
            Determines if the :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getPreviousState` is computed directly
            by the integrator, or if it is calculated using
            :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getInterpolatedState`.
        
            Typically the previous state is directly computed by the integrator, but when events are detected the steps are
            shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
            Returns:
                :code:`true` if the previous state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def restrictStep(self, spacecraftState: org.orekit.propagation.SpacecraftState, spacecraftState2: org.orekit.propagation.SpacecraftState) -> 'OrekitStepInterpolator':
        """
            Create a new restricted version of the instance.
        
            The instance is not changed at all.
        
            Parameters:
                newPreviousState (:class:`~org.orekit.propagation.SpacecraftState`): start of the restricted step
                newCurrentState (:class:`~org.orekit.propagation.SpacecraftState`): end of the restricted step
        
            Returns:
                restricted version of the instance
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getPreviousState`,
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getCurrentState`
        
        
        """
        ...

_FieldOrekitStepNormalizer__T = typing.TypeVar('_FieldOrekitStepNormalizer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrekitStepNormalizer(FieldOrekitStepHandler[_FieldOrekitStepNormalizer__T], typing.Generic[_FieldOrekitStepNormalizer__T]):
    """
    public class FieldOrekitStepNormalizer<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.sampling.FieldOrekitStepHandler`<T>
    
        This class wraps an object implementing :class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler` into a
        :class:`~org.orekit.propagation.sampling.OrekitStepHandler`.
    
        It mirrors the :code:`StepNormalizer` interface from `commons-math <http://commons.apache.org/math/>` but provides a
        space-dynamics interface to the methods.
    """
    def __init__(self, t: _FieldOrekitStepNormalizer__T, fieldOrekitFixedStepHandler: FieldOrekitFixedStepHandler[_FieldOrekitStepNormalizer__T]): ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepNormalizer__T]) -> None: ...
    def getFixedStepHandler(self) -> FieldOrekitFixedStepHandler[_FieldOrekitStepNormalizer__T]: ...
    def getFixedTimeStep(self) -> _FieldOrekitStepNormalizer__T:
        """
            Get the fixed time step.
        
            Returns:
                fixed time step
        
            Since:
                11.0
        
        
        """
        ...
    def handleStep(self, fieldOrekitStepInterpolator: FieldOrekitStepInterpolator[_FieldOrekitStepNormalizer__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldOrekitStepNormalizer__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrekitStepNormalizer__T]) -> None: ...
    def requiresDenseOutput(self) -> bool:
        """
            Determines whether this handler needs dense output. This handler needs dense output in order to provide data at
            regularly spaced steps regardless of the steps the propagator uses, so this method always returns true.
        
            Returns:
                always true
        
        
        """
        ...

_FieldStepHandlerMultiplexer__T = typing.TypeVar('_FieldStepHandlerMultiplexer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStepHandlerMultiplexer(FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T], typing.Generic[_FieldStepHandlerMultiplexer__T]):
    """
    public class FieldStepHandlerMultiplexer<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.sampling.FieldOrekitStepHandler`<T>
    
        This class gathers several :class:`~org.orekit.propagation.sampling.OrekitStepHandler` instances into one.
    """
    def __init__(self): ...
    @typing.overload
    def add(self, t: _FieldStepHandlerMultiplexer__T, fieldOrekitFixedStepHandler: FieldOrekitFixedStepHandler[_FieldStepHandlerMultiplexer__T]) -> None: ...
    @typing.overload
    def add(self, fieldOrekitStepHandler: FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T]) -> None: ...
    def clear(self) -> None:
        """
            Remove all handlers managed by this multiplexer.
        
            If propagation is ongoing (i.e. global :meth:`~org.orekit.propagation.sampling.FieldStepHandlerMultiplexer.init` already
            called and global :meth:`~org.orekit.propagation.sampling.FieldStepHandlerMultiplexer.finish` not called yet), then the
            local :meth:`~org.orekit.propagation.sampling.FieldOrekitStepHandler.finish` and
            :meth:`~org.orekit.propagation.sampling.FieldOrekitFixedStepHandler.finish` methods of the removed handlers will be
            called with the last known state, so the handlers stop properly.
        
            Since:
                11.0
        
        
        """
        ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStepHandlerMultiplexer__T]) -> None: ...
    def getHandlers(self) -> java.util.List[FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T]]: ...
    def handleStep(self, fieldOrekitStepInterpolator: FieldOrekitStepInterpolator[_FieldStepHandlerMultiplexer__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStepHandlerMultiplexer__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStepHandlerMultiplexer__T]) -> None: ...
    @typing.overload
    def remove(self, fieldOrekitFixedStepHandler: FieldOrekitFixedStepHandler[_FieldStepHandlerMultiplexer__T]) -> None: ...
    @typing.overload
    def remove(self, fieldOrekitStepHandler: FieldOrekitStepHandler[_FieldStepHandlerMultiplexer__T]) -> None: ...

class OrekitStepNormalizer(OrekitStepHandler):
    """
    public class OrekitStepNormalizer extends Object implements :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
    
        This class wraps an object implementing :class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler` into a
        :class:`~org.orekit.propagation.sampling.OrekitStepHandler`.
    
        It mirrors the :code:`StepNormalizer` interface from Hipparchus but provides a space-dynamics interface to the methods.
    """
    def __init__(self, double: float, orekitFixedStepHandler: typing.Union[OrekitFixedStepHandler, typing.Callable]): ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Finalize propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.finish`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
        
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
    def handleStep(self, orekitStepInterpolator: OrekitStepInterpolator) -> None:
        """
            Handle the last accepted step.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.handleStep`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): interpolator for the last accepted step. For efficiency purposes, the various propagators reuse the same object on each
                    call, so if the instance wants to keep it across all calls (for example to provide at the end of the propagation a
                    continuous model valid throughout the propagation range), it should build a local copy using the clone method and store
                    this copy.
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize step handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default method does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    def requiresDenseOutput(self) -> bool:
        """
            Determines whether this handler needs dense output. This handler needs dense output in order to provide data at
            regularly spaced steps regardless of the steps the propagator uses, so this method always returns true.
        
            Returns:
                always true
        
        
        """
        ...

_PythonFieldOrekitFixedStepHandler__T = typing.TypeVar('_PythonFieldOrekitFixedStepHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldOrekitFixedStepHandler(FieldOrekitFixedStepHandler[_PythonFieldOrekitFixedStepHandler__T], typing.Generic[_PythonFieldOrekitFixedStepHandler__T]):
    """
    public class PythonFieldOrekitFixedStepHandler<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.sampling.FieldOrekitFixedStepHandler`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finish(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitFixedStepHandler__T]) -> None: ...
    def handleStep(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitFixedStepHandler__T]) -> None: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitFixedStepHandler__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldOrekitFixedStepHandler__T], t: _PythonFieldOrekitFixedStepHandler__T) -> None: ...
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
    """
    public class PythonFieldOrekitStepInterpolator<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.sampling.FieldOrekitStepInterpolator`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getCurrentState(self) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]: ...
    def getInterpolatedState(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldOrekitStepInterpolator__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]: ...
    def getPreviousState(self) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]: ...
    def isForward(self) -> bool:
        """
            Check is integration direction is forward in date.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.FieldOrekitStepInterpolator.isForward`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.FieldOrekitStepInterpolator`
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...
    def restrictStep(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T], fieldSpacecraftState2: org.orekit.propagation.FieldSpacecraftState[_PythonFieldOrekitStepInterpolator__T]) -> FieldOrekitStepInterpolator[_PythonFieldOrekitStepInterpolator__T]: ...

class PythonMultiSatStepHandler(MultiSatStepHandler):
    """
    public class PythonMultiSatStepHandler extends Object implements :class:`~org.orekit.propagation.sampling.MultiSatStepHandler`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finish(self, list: java.util.List[org.orekit.propagation.SpacecraftState]) -> None: ...
    def handleStep(self, list: java.util.List[OrekitStepInterpolator]) -> None: ...
    def init(self, list: java.util.List[org.orekit.propagation.SpacecraftState], absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
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

class PythonOrekitFixedStepHandler(OrekitFixedStepHandler):
    """
    public class PythonOrekitFixedStepHandler extends Object implements :class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`
    
        This interface is a space-dynamics aware fixed size step handler.
    
        It mirrors the :code:`FixedStepHandler` interface from `commons-math <http://commons.apache.org/math/>` but provides a
        space-dynamics interface to the methods.
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Finalize propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitFixedStepHandler.finish`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
            Since:
                11.0
        
        
        """
        ...
    def handleStep(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Handle the current step.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitFixedStepHandler.handleStep`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`
        
            Parameters:
                currentState (:class:`~org.orekit.propagation.SpacecraftState`): current state at step time
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> None:
        """
            Initialize step handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitFixedStepHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
                step (double): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        
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

class PythonOrekitStepHandler(OrekitStepHandler):
    """
    public class PythonOrekitStepHandler extends Object implements :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Finalize propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.finish`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
            Since:
                11.0
        
        
        """
        ...
    def handleStep(self, orekitStepInterpolator: OrekitStepInterpolator) -> None:
        """
            Handle the current step.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.handleStep`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): interpolator set up for the current step
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize step handler at the start of a propagation. Extension point for Python.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default method does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
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

class PythonOrekitStepInterpolator(OrekitStepInterpolator):
    """
    public class PythonOrekitStepInterpolator extends Object implements :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getCurrentState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Get the state at current grid point date. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getCurrentState`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
        
            Returns:
                state at current grid point date
        
        
        """
        ...
    def getInterpolatedState(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
            Get the state at interpolated date.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getInterpolatedState`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the interpolated state
        
            Returns:
                state at interpolated date
        
        
        """
        ...
    def getPreviousState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Get the state at previous grid point date. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.getPreviousState`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
        
            Returns:
                state at previous grid point date
        
        
        """
        ...
    def isCurrentStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.orekit.propagation.sampling.PythonOrekitStepInterpolator.getCurrentState` is computed
            directly by the integrator, or if it is calculated using
            :meth:`~org.orekit.propagation.sampling.PythonOrekitStepInterpolator.getInterpolatedState`. Extension point for Python.
        
            Typically the current state is directly computed by the integrator, but when events are detected the steps are shortened
            so that events occur on step boundaries which means the current state may be computed by the interpolator.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.isCurrentStateInterpolated`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
        
            Returns:
                :code:`true` if the current state was calculated by the interpolator and false if it was computed directly by the
                integrator.
        
        
        """
        ...
    def isForward(self) -> bool:
        """
            Check is integration direction is forward in date.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.isForward`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
        
            Returns:
                true if integration is forward in date
        
        
        """
        ...
    def isPreviousStateInterpolated(self) -> bool:
        """
            Determines if the :meth:`~org.orekit.propagation.sampling.PythonOrekitStepInterpolator.getPreviousState` is computed
            directly by the integrator, or if it is calculated using
            :meth:`~org.orekit.propagation.sampling.PythonOrekitStepInterpolator.getInterpolatedState`. Extension point for Python.
        
            Typically the previous state is directly computed by the integrator, but when events are detected the steps are
            shortened so that events occur on step boundaries which means the previous state may be computed by the interpolator.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.isPreviousStateInterpolated`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
        
            Returns:
                :code:`true` if the previous state was calculated by the interpolator and false if it was computed directly by the
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...
    def restrictStep(self, spacecraftState: org.orekit.propagation.SpacecraftState, spacecraftState2: org.orekit.propagation.SpacecraftState) -> OrekitStepInterpolator:
        """
            Create a new restricted version of the instance.
        
            The instance is not changed at all.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepInterpolator.restrictStep`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`
        
            Parameters:
                newPreviousState (:class:`~org.orekit.propagation.SpacecraftState`): start of the restricted step
                newCurrentState (:class:`~org.orekit.propagation.SpacecraftState`): end of the restricted step
        
            Returns:
                restricted version of the instance
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.propagation.sampling.PythonOrekitStepInterpolator.getPreviousState`,
                :meth:`~org.orekit.propagation.sampling.PythonOrekitStepInterpolator.getCurrentState`
        
        
        """
        ...

class StepHandlerMultiplexer(OrekitStepHandler):
    """
    public class StepHandlerMultiplexer extends Object implements :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
    
        This class gathers several :class:`~org.orekit.propagation.sampling.OrekitStepHandler` instances into one.
    """
    def __init__(self): ...
    @typing.overload
    def add(self, double: float, orekitFixedStepHandler: typing.Union[OrekitFixedStepHandler, typing.Callable]) -> None:
        """
            Add a handler for fixed size step.
        
            If propagation is ongoing (i.e. global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.init` already
            called and global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.finish` not called yet), then the local
            :meth:`~org.orekit.propagation.sampling.OrekitFixedStepHandler.init` method of the added handler will be called with the
            last known state, so the handler starts properly.
        
            Parameters:
                h (double): fixed stepsize (s)
                handler (:class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`): handler called at the end of each finalized step
        
            Since:
                11.0
        
        
        """
        ...
    @typing.overload
    def add(self, orekitStepHandler: OrekitStepHandler) -> None:
        """
            Add a handler for variable size step.
        
            If propagation is ongoing (i.e. global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.init` already
            called and global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.finish` not called yet), then the local
            :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.init` method of the added handler will be called with the last
            known state, so the handler starts properly.
        
            Parameters:
                handler (:class:`~org.orekit.propagation.sampling.OrekitStepHandler`): step handler to add
        
        """
        ...
    def clear(self) -> None:
        """
            Remove all handlers managed by this multiplexer.
        
            If propagation is ongoing (i.e. global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.init` already
            called and global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.finish` not called yet), then the local
            :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.finish` and
            :meth:`~org.orekit.propagation.sampling.OrekitFixedStepHandler.finish` methods of the removed handlers will be called
            with the last known state, so the handlers stop properly.
        
            Since:
                11.0
        
        
        """
        ...
    def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Finalize propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.finish`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                finalState (:class:`~org.orekit.propagation.SpacecraftState`): state at propagation end
        
        
        """
        ...
    def getHandlers(self) -> java.util.List[OrekitStepHandler]: ...
    def handleStep(self, orekitStepInterpolator: OrekitStepInterpolator) -> None:
        """
            Handle the current step.
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.handleStep`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                interpolator (:class:`~org.orekit.propagation.sampling.OrekitStepInterpolator`): interpolator set up for the current step
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize step handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default method does nothing
        
            Specified by:
                :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.sampling.OrekitStepHandler`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...
    @typing.overload
    def remove(self, orekitFixedStepHandler: typing.Union[OrekitFixedStepHandler, typing.Callable]) -> None:
        """
            Remove a handler.
        
            If propagation is ongoing (i.e. global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.init` already
            called and global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.finish` not called yet), then the local
            :meth:`~org.orekit.propagation.sampling.OrekitStepHandler.finish` method of the removed handler will be called with the
            last known state, so the handler stops properly.
        
            Parameters:
                handler (:class:`~org.orekit.propagation.sampling.OrekitStepHandler`): step handler to remove
        
            Since:
                11.0
        
            Remove a handler.
        
            If propagation is ongoing (i.e. global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.init` already
            called and global :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.finish` not called yet), then the local
            :meth:`~org.orekit.propagation.sampling.OrekitFixedStepHandler.finish` method of the removed handler will be called with
            the last known state, so the handler stops properly.
        
            Parameters:
                handler (:class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`): step handler to remove
        
            Since:
                11.0
        
        
        """
        ...
    @typing.overload
    def remove(self, orekitStepHandler: OrekitStepHandler) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.sampling")``.

    FieldOrekitFixedStepHandler: typing.Type[FieldOrekitFixedStepHandler]
    FieldOrekitStepHandler: typing.Type[FieldOrekitStepHandler]
    FieldOrekitStepInterpolator: typing.Type[FieldOrekitStepInterpolator]
    FieldOrekitStepNormalizer: typing.Type[FieldOrekitStepNormalizer]
    FieldStepHandlerMultiplexer: typing.Type[FieldStepHandlerMultiplexer]
    MultiSatStepHandler: typing.Type[MultiSatStepHandler]
    OrekitFixedStepHandler: typing.Type[OrekitFixedStepHandler]
    OrekitStepHandler: typing.Type[OrekitStepHandler]
    OrekitStepInterpolator: typing.Type[OrekitStepInterpolator]
    OrekitStepNormalizer: typing.Type[OrekitStepNormalizer]
    PythonFieldOrekitFixedStepHandler: typing.Type[PythonFieldOrekitFixedStepHandler]
    PythonFieldOrekitStepHandler: typing.Type[PythonFieldOrekitStepHandler]
    PythonFieldOrekitStepInterpolator: typing.Type[PythonFieldOrekitStepInterpolator]
    PythonMultiSatStepHandler: typing.Type[PythonMultiSatStepHandler]
    PythonOrekitFixedStepHandler: typing.Type[PythonOrekitFixedStepHandler]
    PythonOrekitStepHandler: typing.Type[PythonOrekitStepHandler]
    PythonOrekitStepInterpolator: typing.Type[PythonOrekitStepInterpolator]
    StepHandlerMultiplexer: typing.Type[StepHandlerMultiplexer]
