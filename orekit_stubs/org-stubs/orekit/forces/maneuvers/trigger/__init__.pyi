
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.ode.events
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.events.handlers
import org.orekit.time
import org.orekit.utils
import typing



_FieldManeuverTriggerDetector__W = typing.TypeVar('_FieldManeuverTriggerDetector__W', bound=org.hipparchus.CalculusFieldElement)  # <W>
_FieldManeuverTriggerDetector__T = typing.TypeVar('_FieldManeuverTriggerDetector__T', bound=org.orekit.propagation.events.FieldEventDetector)  # <T>
class FieldManeuverTriggerDetector(org.orekit.propagation.events.FieldDetectorModifier[_FieldManeuverTriggerDetector__W], typing.Generic[_FieldManeuverTriggerDetector__W, _FieldManeuverTriggerDetector__T]):
    """
    public class FieldManeuverTriggerDetector<W extends :class:`~org.orekit.forces.maneuvers.trigger.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<W>, T extends :class:`~org.orekit.propagation.events.FieldEventDetector`<W>> extends :class:`~org.orekit.forces.maneuvers.trigger.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.FieldDetectorModifier`<W>
    
        Wrapper for event detection triggering maneuvers (Field version).
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`,
            :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggerDetector`
    """
    def __init__(self, t: _FieldManeuverTriggerDetector__T, fieldEventHandler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldManeuverTriggerDetector__W], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], org.orekit.propagation.events.FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]): ...
    def getDetector(self) -> _FieldManeuverTriggerDetector__T:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.FieldDetectorModifier.getDetector`
            Getter for wrapped detector.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.FieldDetectorModifier.getDetector` in
                interface :class:`~org.orekit.propagation.events.FieldDetectorModifier`
        
            Returns:
                detector
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldManeuverTriggerDetector__W]: ...

_FieldManeuverTriggersResetter__T = typing.TypeVar('_FieldManeuverTriggersResetter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldManeuverTriggersResetter(typing.Generic[_FieldManeuverTriggersResetter__T]):
    """
    public interface FieldManeuverTriggersResetter<T extends :class:`~org.orekit.forces.maneuvers.trigger.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        Resetter for maneuver triggers.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    """
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldManeuverTriggersResetter__T]) -> None: ...
    def maneuverTriggered(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T], boolean: bool) -> None: ...
    def resetState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T]: ...

_ManeuverTriggerDetector__T = typing.TypeVar('_ManeuverTriggerDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class ManeuverTriggerDetector(org.orekit.propagation.events.DetectorModifier, typing.Generic[_ManeuverTriggerDetector__T]):
    """
    public class ManeuverTriggerDetector<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends :class:`~org.orekit.forces.maneuvers.trigger.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.DetectorModifier`
    
        Wrapper for event detection triggering maneuvers.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    """
    def __init__(self, t: _ManeuverTriggerDetector__T, eventHandler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]): ...
    def getDetector(self) -> _ManeuverTriggerDetector__T:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.DetectorModifier.getDetector`
            Get the wrapped detector.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.DetectorModifier.getDetector` in
                interface :class:`~org.orekit.propagation.events.DetectorModifier`
        
            Returns:
                wrapped detector
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.DetectorModifier.getHandler`
            Get the handler.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.DetectorModifier.getHandler` in
                interface :class:`~org.orekit.propagation.events.DetectorModifier`
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getHandler` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                event handler to call at event occurrences
        
        
        """
        ...

class ManeuverTriggers(org.orekit.utils.ParameterDriversProvider, org.orekit.propagation.events.EventDetectorsProvider):
    """
    public interface ManeuverTriggers extends :class:`~org.orekit.utils.ParameterDriversProvider`, :class:`~org.orekit.propagation.events.EventDetectorsProvider`
    
        Generic interface for the maneuver triggers used in a :class:`~org.orekit.forces.maneuvers.Maneuver`.
    
        Since:
            10.2
    """
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Returns:
                the maneuver name
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> initialState): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.FieldAbsoluteDate`<T> target): date of propagation. Not equal to :code:`initialState.getDate()`.
        
            Since:
                11.1
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...
    _isFiring_1__T = typing.TypeVar('_isFiring_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                parameters (double[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        """
        ...
    @typing.overload
    def isFiring(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_1__T], tArray: typing.Union[typing.List[_isFiring_1__T], jpype.JArray]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                parameters (T[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        
        """
        ...

class ManeuverTriggersResetter:
    """
    public interface ManeuverTriggersResetter
    
        Resetter for maneuver triggers.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    """
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    def maneuverTriggered(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> None:
        """
            Observe a maneuver trigger.
        
            The :code:`start` parameter corresponds to physical flow of time from past to future, not to propagation direction which
            can be backward. This means that during forward propagations, the first call will have :code:`start` set to :code:`true`
            and the second call will have :code:`start` set to :code:`false`, whereas in backward propagation, the first call will
            have :code:`start` set to :code:`false` and the second call will have :code:`start` set to :code:`true`.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at trigger date (before applying the maneuver)
                start (boolean): if true, the trigger is the start of the maneuver
        
        
        """
        ...
    def resetState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset state as a maneuver triggers.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at trigger date
        
            Returns:
                reset state taking into account maneuver start/stop
        
        
        """
        ...

_PythonFieldManeuverTriggersResetter__T = typing.TypeVar('_PythonFieldManeuverTriggersResetter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldManeuverTriggersResetter(FieldManeuverTriggersResetter[_PythonFieldManeuverTriggersResetter__T], typing.Generic[_PythonFieldManeuverTriggersResetter__T]):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def maneuverTriggered(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T], boolean: bool) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T]: ...

class PythonManeuverTriggers(ManeuverTriggers):
    def __init__(self): ...
    def finalize(self) -> None: ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    _isFiring_1__T = typing.TypeVar('_isFiring_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> bool: ...
    @typing.overload
    def isFiring(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_1__T], tArray: typing.Union[typing.List[_isFiring_1__T], jpype.JArray]) -> bool: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonManeuverTriggersResetter(ManeuverTriggersResetter):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def maneuverTriggered(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState: ...

class ResettableManeuverTriggers(ManeuverTriggers):
    """
    public interface ResettableManeuverTriggers extends :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
    
        Interface for maneuver triggers with resetters.
    
        Since:
            10.2
    """
    _addResetter_0__T = typing.TypeVar('_addResetter_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addResetter(self, field: org.hipparchus.Field[_addResetter_0__T], fieldManeuverTriggersResetter: FieldManeuverTriggersResetter[_addResetter_0__T]) -> None:
        """
            Add a resetter.
        
            Parameters:
                field (:class:`~org.orekit.forces.maneuvers.trigger.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field to which the state belongs
                resetter (:class:`~org.orekit.forces.maneuvers.trigger.FieldManeuverTriggersResetter`<T> resetter): resetter to add
        
        
        """
        ...
    @typing.overload
    def addResetter(self, maneuverTriggersResetter: ManeuverTriggersResetter) -> None:
        """
            Add a resetter.
        
            Parameters:
                resetter (:class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`): resetter to add
        
        """
        ...

class AbstractManeuverTriggers(ResettableManeuverTriggers):
    """
    public abstract class AbstractManeuverTriggers extends :class:`~org.orekit.forces.maneuvers.trigger.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.trigger.ResettableManeuverTriggers`
    
        Base class for triggers.
    
        Since:
            11.1
    """
    _addResetter_0__T = typing.TypeVar('_addResetter_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addResetter(self, field: org.hipparchus.Field[_addResetter_0__T], fieldManeuverTriggersResetter: FieldManeuverTriggersResetter[_addResetter_0__T]) -> None:
        """
            Add a resetter.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ResettableManeuverTriggers.addResetter` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ResettableManeuverTriggers`
        
            Parameters:
                field (:class:`~org.orekit.forces.maneuvers.trigger.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field to which the state belongs
                resetter (:class:`~org.orekit.forces.maneuvers.trigger.FieldManeuverTriggersResetter`<T> resetter): resetter to add
        
        
        """
        ...
    @typing.overload
    def addResetter(self, maneuverTriggersResetter: ManeuverTriggersResetter) -> None:
        """
            Add a resetter.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ResettableManeuverTriggers.addResetter` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ResettableManeuverTriggers`
        
            Parameters:
                resetter (:class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`): resetter to add
        
        """
        ...
    def getFirings(self) -> org.orekit.utils.TimeSpanMap[bool]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> initialState): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.FieldAbsoluteDate`<T> target): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...
    _isFiring_1__S = typing.TypeVar('_isFiring_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.isFiring` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                parameters (double[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        """
        ...
    @typing.overload
    def isFiring(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_1__S], sArray: typing.Union[typing.List[_isFiring_1__S], jpype.JArray]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.isFiring` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<S> date): current date
                parameters (S[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        
        """
        ...

_IntervalEventTrigger__T = typing.TypeVar('_IntervalEventTrigger__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class IntervalEventTrigger(AbstractManeuverTriggers, typing.Generic[_IntervalEventTrigger__T]):
    """
    public abstract class IntervalEventTrigger<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    
        Maneuver triggers based on a single event detector that defines firing intervals.
    
        Firing intervals correspond to time spans with positive value of the event detector
        :meth:`~org.orekit.propagation.events.EventDetector.g` function.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.StartStopEventsTrigger`
    """
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__S = typing.TypeVar('_getFieldEventDetectors_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[org.hipparchus.CalculusFieldElement], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[org.hipparchus.CalculusFieldElement]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__S]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__S]]: ...
    def getFiringIntervalDetector(self) -> _IntervalEventTrigger__T:
        """
            Getter for the firing interval detector.
        
            Returns:
                firing interval detector
        
        
        """
        ...
    _init_0__D = typing.TypeVar('_init_0__D', bound=org.hipparchus.CalculusFieldElement)  # <D>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__D], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__D]) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Overrides:
                :meth:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers.init` in
                class :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<D> initialState): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.FieldAbsoluteDate`<D> target): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Overrides:
                :meth:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers.init` in
                class :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...

class PythonAbstractManeuverTriggers(AbstractManeuverTriggers):
    def __init__(self): ...
    def finalize(self) -> None: ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def isFiringOnInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> bool: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_StartStopEventsTrigger__A = typing.TypeVar('_StartStopEventsTrigger__A', bound=org.orekit.propagation.events.EventDetector)  # <A>
_StartStopEventsTrigger__O = typing.TypeVar('_StartStopEventsTrigger__O', bound=org.orekit.propagation.events.EventDetector)  # <O>
class StartStopEventsTrigger(AbstractManeuverTriggers, typing.Generic[_StartStopEventsTrigger__A, _StartStopEventsTrigger__O]):
    """
    public abstract class StartStopEventsTrigger<A extends :class:`~org.orekit.propagation.events.EventDetector`, O extends :class:`~org.orekit.propagation.events.EventDetector`> extends :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    
        Maneuver triggers based on a pair of event detectors that defines firing start and stop.
    
        The thruster starts firing when the start detector becomes positive. The thruster stops firing when the stop detector
        becomes positive. The 2 detectors should not be positive at the same time. A date detector is not suited as it does not
        delimit an interval. They can be both negative at the same time.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`
    """
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__S = typing.TypeVar('_getFieldEventDetectors_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__S]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__S]]: ...
    def getStartDetector(self) -> _StartStopEventsTrigger__A:
        """
            Getter for the firing start detector.
        
            Returns:
                firing start detector
        
        
        """
        ...
    def getStopDetector(self) -> _StartStopEventsTrigger__O:
        """
            Getter for the firing stop detector.
        
            Returns:
                firing stop detector
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Overrides:
                :meth:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers.init` in
                class :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...

class DateBasedManeuverTriggers(IntervalEventTrigger[org.orekit.propagation.events.ParameterDrivenDateIntervalDetector]):
    """
    public class DateBasedManeuverTriggers extends :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`<:class:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector`>
    
        Maneuver triggers based on a start and end date.
    
        Since:
            10.2
    """
    DEFAULT_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.forces.maneuvers.trigger.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_NAME
    
        Default name for trigger.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    def getDuration(self) -> float:
        """
            Get the duration of the maneuver (s). duration = endDate - startDate
        
            Returns:
                the duration of the maneuver (s)
        
        
        """
        ...
    def getEndDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date.
        
            Returns:
                the end date
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Returns:
                the maneuver name
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getStartDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date.
        
            Returns:
                the start date
        
        
        """
        ...

_PythonIntervalEventTrigger__T = typing.TypeVar('_PythonIntervalEventTrigger__T', bound=org.orekit.propagation.events.AbstractDetector)  # <T>
class PythonIntervalEventTrigger(IntervalEventTrigger[_PythonIntervalEventTrigger__T], typing.Generic[_PythonIntervalEventTrigger__T]):
    def __init__(self, t: _PythonIntervalEventTrigger__T): ...
    _convertIntervalDetector__D = typing.TypeVar('_convertIntervalDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertIntervalDetector__S = typing.TypeVar('_convertIntervalDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertIntervalDetector(self, field: org.hipparchus.Field[_convertIntervalDetector__S], t: _PythonIntervalEventTrigger__T) -> _convertIntervalDetector__D: ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonStartStopEventsTrigger__A = typing.TypeVar('_PythonStartStopEventsTrigger__A', bound=org.orekit.propagation.events.AbstractDetector)  # <A>
_PythonStartStopEventsTrigger__O = typing.TypeVar('_PythonStartStopEventsTrigger__O', bound=org.orekit.propagation.events.AbstractDetector)  # <O>
class PythonStartStopEventsTrigger(StartStopEventsTrigger[_PythonStartStopEventsTrigger__A, _PythonStartStopEventsTrigger__O], typing.Generic[_PythonStartStopEventsTrigger__A, _PythonStartStopEventsTrigger__O]):
    def __init__(self, a: _PythonStartStopEventsTrigger__A, o: _PythonStartStopEventsTrigger__O): ...
    _convertStartDetector__D = typing.TypeVar('_convertStartDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertStartDetector__S = typing.TypeVar('_convertStartDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertStartDetector(self, field: org.hipparchus.Field[_convertStartDetector__S], a: _PythonStartStopEventsTrigger__A) -> _convertStartDetector__D: ...
    _convertStopDetector__D = typing.TypeVar('_convertStopDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertStopDetector__S = typing.TypeVar('_convertStopDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertStopDetector(self, field: org.hipparchus.Field[_convertStopDetector__S], o: _PythonStartStopEventsTrigger__O) -> _convertStopDetector__D: ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class TimeIntervalsManeuverTrigger(IntervalEventTrigger[org.orekit.propagation.events.BooleanDetector]):
    """
    public class TimeIntervalsManeuverTrigger extends :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`<:class:`~org.orekit.propagation.events.BooleanDetector`>
    
        Maneuver trigger based on time intervals.
    
        Since:
            13.1
    
        Also see:
            :class:`~org.orekit.time.TimeInterval`, :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    @typing.overload
    @staticmethod
    def of(*timeIntervalDetector: org.orekit.propagation.events.TimeIntervalDetector) -> 'TimeIntervalsManeuverTrigger':
        """
            Build an instance based on the input time intervals. Detectors are created with default settings.
        
            Parameters:
                timeIntervals (:class:`~org.orekit.time.TimeInterval`...): intervals
        
            Returns:
                maneuver trigger
        
            Build an instance based on the input time interval detectors.
        
            Parameters:
                timeIntervalDetectors (:class:`~org.orekit.propagation.events.TimeIntervalDetector`...): detectors
        
            Returns:
                maneuver trigger
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(*timeInterval: org.orekit.time.TimeInterval) -> 'TimeIntervalsManeuverTrigger': ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers.trigger")``.

    AbstractManeuverTriggers: typing.Type[AbstractManeuverTriggers]
    DateBasedManeuverTriggers: typing.Type[DateBasedManeuverTriggers]
    FieldManeuverTriggerDetector: typing.Type[FieldManeuverTriggerDetector]
    FieldManeuverTriggersResetter: typing.Type[FieldManeuverTriggersResetter]
    IntervalEventTrigger: typing.Type[IntervalEventTrigger]
    ManeuverTriggerDetector: typing.Type[ManeuverTriggerDetector]
    ManeuverTriggers: typing.Type[ManeuverTriggers]
    ManeuverTriggersResetter: typing.Type[ManeuverTriggersResetter]
    PythonAbstractManeuverTriggers: typing.Type[PythonAbstractManeuverTriggers]
    PythonFieldManeuverTriggersResetter: typing.Type[PythonFieldManeuverTriggersResetter]
    PythonIntervalEventTrigger: typing.Type[PythonIntervalEventTrigger]
    PythonManeuverTriggers: typing.Type[PythonManeuverTriggers]
    PythonManeuverTriggersResetter: typing.Type[PythonManeuverTriggersResetter]
    PythonStartStopEventsTrigger: typing.Type[PythonStartStopEventsTrigger]
    ResettableManeuverTriggers: typing.Type[ResettableManeuverTriggers]
    StartStopEventsTrigger: typing.Type[StartStopEventsTrigger]
    TimeIntervalsManeuverTrigger: typing.Type[TimeIntervalsManeuverTrigger]
