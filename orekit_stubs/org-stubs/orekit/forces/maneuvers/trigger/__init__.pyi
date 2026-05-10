
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
    Wrapper for event detection triggering maneuvers (Field version).
    
    Since:
        13.0
    
    Also see:
        AbstractManeuverTriggers,
        ManeuverTriggerDetector
    """
    def __init__(self, detector: _FieldManeuverTriggerDetector__T, handler: typing.Union[org.orekit.propagation.events.handlers.FieldEventHandler[_FieldManeuverTriggerDetector__W], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], org.orekit.propagation.events.FieldEventDetector[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]):
        """
        Constructor.
        
        Parameters:
            detector (FieldManeuverTriggerDetector): prototype detector
            handler (FieldEventHandler<FieldManeuverTriggerDetector> handler): event handler
        
        
        """
        ...
    def getDetector(self) -> _FieldManeuverTriggerDetector__T:
        """
        Description copied from interface: getDetector Getter for wrapped detector.
        
        Specified by: getDetector in interface FieldDetectorModifier
        
        Returns:
            detector
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldManeuverTriggerDetector__W]:
        """
        Description copied from interface: getHandler Get the handler.
        
        Specified by: getHandler in interface FieldDetectorModifier
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...

_FieldManeuverTriggersResetter__T = typing.TypeVar('_FieldManeuverTriggersResetter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldManeuverTriggersResetter(typing.Generic[_FieldManeuverTriggersResetter__T]):
    """
    Resetter for maneuver triggers.
    
    Since:
        11.1
    
    Also see:
        AbstractManeuverTriggers
    """
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T], target: org.orekit.time.FieldAbsoluteDate[_FieldManeuverTriggersResetter__T]) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Parameters:
            initialState (FieldSpacecraftState<FieldManeuverTriggersResetter> initialState): initial spacecraft state (at the start of propagation).
            target (FieldAbsoluteDate<FieldManeuverTriggersResetter> target): date of propagation. Not equal to getDate().
        
        
        """
        ...
    def maneuverTriggered(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T], start: bool) -> None:
        """
        Observe a maneuver trigger.
        
        The start parameter corresponds to physical flow of time from past to future, not to propagation direction which can be backward. This means that during forward propagations, the first call will have start set to true and the second call will have start set to false, whereas in backward propagation, the first call will have start set to false and the second call will have start set to true.
        
        Parameters:
            state (FieldSpacecraftState<FieldManeuverTriggersResetter> state): spacecraft state at trigger date (before applying the maneuver)
            start (boolean): if true, the trigger is the start of the maneuver
        
        
        """
        ...
    def resetState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T]:
        """
        Reset state as a maneuver triggers.
        
        Parameters:
            state (FieldSpacecraftState<FieldManeuverTriggersResetter> state): spacecraft state at trigger date
        
        Returns:
            reset state taking into account maneuver start/stop
        
        
        """
        ...

_ManeuverTriggerDetector__T = typing.TypeVar('_ManeuverTriggerDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class ManeuverTriggerDetector(org.orekit.propagation.events.DetectorModifier, typing.Generic[_ManeuverTriggerDetector__T]):
    """
    Wrapper for event detection triggering maneuvers.
    
    Since:
        13.0
    
    Also see:
        AbstractManeuverTriggers
    """
    def __init__(self, detector: _ManeuverTriggerDetector__T, handler: typing.Union[org.orekit.propagation.events.handlers.EventHandler, typing.Callable]):
        """
        Constructor.
        
        Parameters:
            detector (ManeuverTriggerDetector): prototype detector
            handler (EventHandler): event handler
        
        
        """
        ...
    def getDetector(self) -> _ManeuverTriggerDetector__T:
        """
        Description copied from interface: getDetector Get the wrapped detector.
        
        Specified by: getDetector in interface DetectorModifier
        
        Returns:
            wrapped detector
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Description copied from interface: getHandler Get the handler.
        
        Specified by: getHandler in interface DetectorModifier
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...

class ManeuverTriggers(org.orekit.utils.ParameterDriversProvider, org.orekit.propagation.events.EventDetectorsProvider):
    """
    Generic interface for the maneuver triggers used in a Maneuver.
    
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
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): initial spacecraft state (at the start of propagation).
            target (FieldAbsoluteDate<T> target): date of propagation. Not equal to getDate().
        
        Since:
            11.1
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...
    _isFiring_1__T = typing.TypeVar('_isFiring_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isFiring(self, date: org.orekit.time.AbsoluteDate, parameters: typing.Union[typing.List[float], jpype.JArray]) -> bool:
        """
        Find out if the maneuver is firing or not.
        
        Parameters:
            date (AbsoluteDate): current date
            parameters (double[]): maneuver triggers parameters
        
        Returns:
            true if the maneuver is firing, false otherwise
        
        """
        ...
    @typing.overload
    def isFiring(self, date: org.orekit.time.FieldAbsoluteDate[_isFiring_1__T], parameters: typing.Union[typing.List[_isFiring_1__T], jpype.JArray]) -> bool:
        """
        Find out if the maneuver is firing or not.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            parameters (T[]): maneuver triggers parameters
        
        Returns:
            true if the maneuver is firing, false otherwise
        
        
        """
        ...

class ManeuverTriggersResetter:
    """
    Resetter for maneuver triggers.
    
    Since:
        11.1
    
    Also see:
        AbstractManeuverTriggers
    """
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...
    def maneuverTriggered(self, state: org.orekit.propagation.SpacecraftState, start: bool) -> None:
        """
        Observe a maneuver trigger.
        
        The start parameter corresponds to physical flow of time from past to future, not to propagation direction which can be backward. This means that during forward propagations, the first call will have start set to true and the second call will have start set to false, whereas in backward propagation, the first call will have start set to false and the second call will have start set to true.
        
        Parameters:
            state (SpacecraftState): spacecraft state at trigger date (before applying the maneuver)
            start (boolean): if true, the trigger is the start of the maneuver
        
        
        """
        ...
    def resetState(self, state: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Reset state as a maneuver triggers.
        
        Parameters:
            state (SpacecraftState): spacecraft state at trigger date
        
        Returns:
            reset state taking into account maneuver start/stop
        
        
        """
        ...

_PythonFieldManeuverTriggersResetter__T = typing.TypeVar('_PythonFieldManeuverTriggersResetter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldManeuverTriggersResetter(FieldManeuverTriggersResetter[_PythonFieldManeuverTriggersResetter__T], typing.Generic[_PythonFieldManeuverTriggersResetter__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def maneuverTriggered(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T], start: bool) -> None:
        """
        Observe a maneuver trigger.
        
        The start parameter corresponds to physical flow of time from past to future, not to propagation direction which can be backward. This means that during forward propagations, the first call will have start set to true and the second call will have start set to false, whereas in backward propagation, the first call will have start set to false and the second call will have start set to true.
        
        Specified by: maneuverTriggered in interface FieldManeuverTriggersResetter
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldManeuverTriggersResetter> state): spacecraft state at trigger date (before applying the maneuver)
            start (boolean): if true, the trigger is the start of the maneuver
        
        
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
    def resetState(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T]:
        """
        Reset state as a maneuver triggers.
        
        Specified by: resetState in interface FieldManeuverTriggersResetter
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldManeuverTriggersResetter> state): spacecraft state at trigger date
        
        Returns:
            reset state taking into account maneuver start/stop
        
        
        """
        ...

class PythonManeuverTriggers(ManeuverTriggers):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface ManeuverTriggers
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): initial spacecraft state (at the start of propagation).
            target (FieldAbsoluteDate<T> target): date of propagation. Not equal to getDate().
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface ManeuverTriggers
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...
    _isFiring_1__T = typing.TypeVar('_isFiring_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isFiring(self, date: org.orekit.time.AbsoluteDate, parameters: typing.Union[typing.List[float], jpype.JArray]) -> bool:
        """
        Find out if the maneuver is firing or not.
        
        Specified by: isFiring in interface ManeuverTriggers
        
        Parameters:
            date (AbsoluteDate): current date
            parameters (double[]): maneuver triggers parameters
        
        Returns:
            true if the maneuver is firing, false otherwise
        
        """
        ...
    @typing.overload
    def isFiring(self, date: org.orekit.time.FieldAbsoluteDate[_isFiring_1__T], parameters: typing.Union[typing.List[_isFiring_1__T], jpype.JArray]) -> bool:
        """
        Find out if the maneuver is firing or not.
        
        Specified by: isFiring in interface ManeuverTriggers
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            parameters (T[]): maneuver triggers parameters
        
        Returns:
            true if the maneuver is firing, false otherwise
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonManeuverTriggersResetter(ManeuverTriggersResetter):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def maneuverTriggered(self, state: org.orekit.propagation.SpacecraftState, start: bool) -> None:
        """
        Observe a maneuver trigger.
        
        The start parameter corresponds to physical flow of time from past to future, not to propagation direction which can be backward. This means that during forward propagations, the first call will have start set to true and the second call will have start set to false, whereas in backward propagation, the first call will have start set to false and the second call will have start set to true.
        
        Specified by: maneuverTriggered in interface ManeuverTriggersResetter
        
        Parameters:
            state (SpacecraftState): spacecraft state at trigger date (before applying the maneuver)
            start (boolean): if true, the trigger is the start of the maneuver
        
        
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
    def resetState(self, state: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Reset state as a maneuver triggers.
        
        Specified by: resetState in interface ManeuverTriggersResetter
        
        Parameters:
            state (SpacecraftState): spacecraft state at trigger date
        
        Returns:
            reset state taking into account maneuver start/stop
        
        
        """
        ...

class ResettableManeuverTriggers(ManeuverTriggers):
    """
    Interface for maneuver triggers with resetters.
    
    Since:
        10.2
    """
    _addResetter_0__T = typing.TypeVar('_addResetter_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addResetter(self, field: org.hipparchus.Field[_addResetter_0__T], resetter: FieldManeuverTriggersResetter[_addResetter_0__T]) -> None:
        """
        Add a resetter.
        
        Parameters:
            field (Field<T> field): field to which the state belongs
            resetter (FieldManeuverTriggersResetter<T> resetter): resetter to add
        
        
        """
        ...
    @typing.overload
    def addResetter(self, resetter: ManeuverTriggersResetter) -> None:
        """
        Add a resetter.
        
        Parameters:
            resetter (ManeuverTriggersResetter): resetter to add
        
        """
        ...

class AbstractManeuverTriggers(ResettableManeuverTriggers):
    """
    Base class for triggers.
    
    Since:
        11.1
    """
    _addResetter_0__T = typing.TypeVar('_addResetter_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addResetter(self, field: org.hipparchus.Field[_addResetter_0__T], resetter: FieldManeuverTriggersResetter[_addResetter_0__T]) -> None:
        """
        Add a resetter.
        
        Specified by: addResetter in interface ResettableManeuverTriggers
        
        Parameters:
            field (Field<T> field): field to which the state belongs
            resetter (FieldManeuverTriggersResetter<T> resetter): resetter to add
        
        
        """
        ...
    @typing.overload
    def addResetter(self, resetter: ManeuverTriggersResetter) -> None:
        """
        Add a resetter.
        
        Specified by: addResetter in interface ResettableManeuverTriggers
        
        Parameters:
            resetter (ManeuverTriggersResetter): resetter to add
        
        """
        ...
    def getFirings(self) -> org.orekit.utils.TimeSpanMap[bool]:
        """
        Get the firings detected during last propagation.
        
        Returns:
            firings detected during last propagation
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface ManeuverTriggers
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): initial spacecraft state (at the start of propagation).
            target (FieldAbsoluteDate<T> target): date of propagation. Not equal to getDate().
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface ManeuverTriggers
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...
    _isFiring_1__S = typing.TypeVar('_isFiring_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @typing.overload
    def isFiring(self, date: org.orekit.time.AbsoluteDate, parameters: typing.Union[typing.List[float], jpype.JArray]) -> bool:
        """
        Find out if the maneuver is firing or not.
        
        Specified by: isFiring in interface ManeuverTriggers
        
        Parameters:
            date (AbsoluteDate): current date
            parameters (double[]): maneuver triggers parameters
        
        Returns:
            true if the maneuver is firing, false otherwise
        
        """
        ...
    @typing.overload
    def isFiring(self, date: org.orekit.time.FieldAbsoluteDate[_isFiring_1__S], parameters: typing.Union[typing.List[_isFiring_1__S], jpype.JArray]) -> bool:
        """
        Find out if the maneuver is firing or not.
        
        Specified by: isFiring in interface ManeuverTriggers
        
        Parameters:
            date (FieldAbsoluteDate<S> date): current date
            parameters (S[]): maneuver triggers parameters
        
        Returns:
            true if the maneuver is firing, false otherwise
        
        
        """
        ...

_IntervalEventTrigger__T = typing.TypeVar('_IntervalEventTrigger__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class IntervalEventTrigger(AbstractManeuverTriggers, typing.Generic[_IntervalEventTrigger__T]):
    """
    Maneuver triggers based on a single event detector that defines firing intervals.
    
    Firing intervals correspond to time spans with positive value of the event detector g function.
    
    Since:
        11.1
    
    Also see:
        StartStopEventsTrigger
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
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__D], target: org.orekit.time.FieldAbsoluteDate[_init_0__D]) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface ManeuverTriggers
        
        Overrides: init in class AbstractManeuverTriggers
        
        Parameters:
            initialState (FieldSpacecraftState<D> initialState): initial spacecraft state (at the start of propagation).
            target (FieldAbsoluteDate<D> target): date of propagation. Not equal to getDate().
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface ManeuverTriggers
        
        Overrides: init in class AbstractManeuverTriggers
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...

class PythonAbstractManeuverTriggers(AbstractManeuverTriggers):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def isFiringOnInitialState(self, initialState: org.orekit.propagation.SpacecraftState, isForward: bool) -> bool:
        """
        Method to check if the thruster is firing on initialization. can be called by sub classes
        
        Specified by: isFiringOnInitialState in class AbstractManeuverTriggers
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state
            isForward (boolean): if true, propagation will be in the forward direction
        
        Returns:
            true if firing in propagation direction
        
        
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

_StartStopEventsTrigger__A = typing.TypeVar('_StartStopEventsTrigger__A', bound=org.orekit.propagation.events.EventDetector)  # <A>
_StartStopEventsTrigger__O = typing.TypeVar('_StartStopEventsTrigger__O', bound=org.orekit.propagation.events.EventDetector)  # <O>
class StartStopEventsTrigger(AbstractManeuverTriggers, typing.Generic[_StartStopEventsTrigger__A, _StartStopEventsTrigger__O]):
    """
    Maneuver triggers based on a pair of event detectors that defines firing start and stop.
    
    The thruster starts firing when the start detector becomes positive. The thruster stops firing when the stop detector becomes positive. The 2 detectors should not be positive at the same time. A date detector is not suited as it does not delimit an interval. They can be both negative at the same time.
    
    Since:
        11.1
    
    Also see:
        IntervalEventTrigger
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
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface ManeuverTriggers
        
        Overrides: init in class AbstractManeuverTriggers
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...

class DateBasedManeuverTriggers(IntervalEventTrigger[org.orekit.propagation.events.ParameterDrivenDateIntervalDetector]):
    """
    Maneuver triggers based on a start and end date.
    
    Since:
        10.2
    """
    DEFAULT_NAME: typing.ClassVar[str] = ...
    """
    Default name for trigger.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, name: str, date: org.orekit.time.AbsoluteDate, duration: float): ...
    @typing.overload
    def __init__(self, name: str, date: org.orekit.time.AbsoluteDate, duration: float, detectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def __init__(self, date: org.orekit.time.AbsoluteDate, duration: float): ...
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getStartDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date.
        
        Returns:
            the start date
        
        
        """
        ...

_PythonIntervalEventTrigger__T = typing.TypeVar('_PythonIntervalEventTrigger__T', bound=org.orekit.propagation.events.AbstractDetector)  # <T>
class PythonIntervalEventTrigger(IntervalEventTrigger[_PythonIntervalEventTrigger__T], typing.Generic[_PythonIntervalEventTrigger__T]):
    def __init__(self, prototypeFiringIntervalDetector: _PythonIntervalEventTrigger__T): ...
    _convertIntervalDetector__D = typing.TypeVar('_convertIntervalDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertIntervalDetector__S = typing.TypeVar('_convertIntervalDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertIntervalDetector(self, field: org.hipparchus.Field[_convertIntervalDetector__S], detector: _PythonIntervalEventTrigger__T) -> _convertIntervalDetector__D:
        """
        Convert a primitive firing intervals detector into a field firing intervals detector.
        
        The FieldEventDetectionSettings must be set up in conformance with the non-field detector.
        
        A skeleton implementation of this method to convert some XyzDetector into FieldXyzDetector, considering these detectors are created from a date and a number parameter is:
        
             protected <D extends FieldEventDetector<S>, S extends CalculusFieldElement<S>> D convertIntervalDetector(final Field<S> field, final XyzDetector detector) {
        
                 final FieldAbsoluteDate<S> date  = new FieldAbsoluteDate<>(field, detector.getDate());
                 final S                    param = field.getZero().newInstance(detector.getParam());
        
                 D converted = (D) new FieldXyzDetector<>(date, param).withDetectionSettings(field, detector.getDetectionSettings());
                 return converted;
        
             }
         
         
        
        Specified by: convertIntervalDetector in class IntervalEventTrigger
        
        Parameters:
            field (Field<S> field): field to which the state belongs
            detector (PythonIntervalEventTrigger): primitive firing intervals detector to convert
        
        Returns:
            converted firing intervals detector
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
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

_PythonStartStopEventsTrigger__A = typing.TypeVar('_PythonStartStopEventsTrigger__A', bound=org.orekit.propagation.events.AbstractDetector)  # <A>
_PythonStartStopEventsTrigger__O = typing.TypeVar('_PythonStartStopEventsTrigger__O', bound=org.orekit.propagation.events.AbstractDetector)  # <O>
class PythonStartStopEventsTrigger(StartStopEventsTrigger[_PythonStartStopEventsTrigger__A, _PythonStartStopEventsTrigger__O], typing.Generic[_PythonStartStopEventsTrigger__A, _PythonStartStopEventsTrigger__O]):
    def __init__(self, prototypeStartDetector: _PythonStartStopEventsTrigger__A, prototypeStopDetector: _PythonStartStopEventsTrigger__O): ...
    _convertStartDetector__D = typing.TypeVar('_convertStartDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertStartDetector__S = typing.TypeVar('_convertStartDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertStartDetector(self, field: org.hipparchus.Field[_convertStartDetector__S], detector: _PythonStartStopEventsTrigger__A) -> _convertStartDetector__D:
        """
        Convert a primitive firing start detector into a field firing start detector.
        
        The FieldEventDetectionSettings must be set up in conformance with the non-field detector.
        
        A skeleton implementation of this method to convert some XyzDetector into FieldXyzDetector, considering these detectors have a withDetectionSettings method and are created from a date and a number parameter is:
        
             protected <D extends FieldEventDetector<S>, S extends CalculusFieldElement<S>> D convertStartDetector(final Field<S> field, final XyzDetector detector) {
        
                 final FieldAbsoluteDate<S> date  = new FieldAbsoluteDate<>(field, detector.getDate());
                 final S                    param = field.getZero().newInstance(detector.getParam());
        
                 final D converted = (D) new FieldXyzDetector<>(date, param)
                 .withDetectionSettings(field, detector.getDetectionSettings());
                 return converted;
        
             }
         
         
        
        Specified by: convertStartDetector in class StartStopEventsTrigger
        
        Parameters:
            field (Field<S> field): field to which the state belongs
            detector (PythonStartStopEventsTrigger): primitive firing start detector to convert
        
        Returns:
            converted firing start detector
        
        
        """
        ...
    _convertStopDetector__D = typing.TypeVar('_convertStopDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertStopDetector__S = typing.TypeVar('_convertStopDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertStopDetector(self, field: org.hipparchus.Field[_convertStopDetector__S], detector: _PythonStartStopEventsTrigger__O) -> _convertStopDetector__D:
        """
        Convert a primitive firing stop detector into a field firing stop detector.
        
        The FieldEventDetectionSettings must be set up in conformance with the non-field detector.
        
        A skeleton implementation of this method to convert some XyzDetector into FieldXyzDetector, considering these detectors have a withDetectionSettings method and are created from a date and a number parameter is:
        
             protected <D extends FieldEventDetector<S>, S extends CalculusFieldElement<S>> D convertEndDetector(final Field<S> field, final XyzDetector detector) {
        
                 final FieldAbsoluteDate<S> date  = new FieldAbsoluteDate<>(field, detector.getDate());
                 final S                    param = field.getZero().newInstance(detector.getParam());
        
                 final D converted = (D) new FieldXyzDetector<>(date, param)
                 .withDetectionSettings(field, detector.getDetectionSettings());
                 return converted;
        
             }
         
         
        
        Specified by: convertStopDetector in class StartStopEventsTrigger
        
        Parameters:
            field (Field<S> field): field to which the state belongs
            detector (PythonStartStopEventsTrigger): primitive firing stop detector to convert
        
        Returns:
            converted firing stop detector
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
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

class TimeIntervalsManeuverTrigger(IntervalEventTrigger[org.orekit.propagation.events.BooleanDetector]):
    """
    Maneuver trigger based on time intervals.
    
    Since:
        13.1
    
    Also see:
        TimeInterval, IntervalEventTrigger
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Description copied from interface: getParametersDrivers Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(*timeIntervals: org.orekit.propagation.events.TimeIntervalDetector) -> 'TimeIntervalsManeuverTrigger':
        """
        Parameters:
            timeIntervals (TimeInterval...): intervals
        
        Returns:
            maneuver trigger
        
        Build an instance based on the input time interval detectors.
        
        Parameters:
            timeIntervalDetectors (TimeIntervalDetector...): detectors
        
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
