import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.ode.events
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.events.handlers
import org.orekit.time
import org.orekit.utils
import typing



_FieldManeuverTriggersResetter__T = typing.TypeVar('_FieldManeuverTriggersResetter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldManeuverTriggersResetter(typing.Generic[_FieldManeuverTriggersResetter__T]):
    """
    public interface FieldManeuverTriggersResetter<T extends CalculusFieldElement<T>>
    
        Resetter for maneuver triggers.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    """
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldManeuverTriggersResetter__T]) -> None: ...
    def maneuverTriggered(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T], boolean: bool) -> None: ...
    def resetState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldManeuverTriggersResetter__T]: ...

class ManeuverTriggers:
    """
    public interface ManeuverTriggers
    
        Generic interface for the maneuver triggers used in a :class:`~org.orekit.forces.maneuvers.Maneuver`.
    
        Since:
            10.2
    """
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Returns:
                the maneuver name
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
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
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]) -> bool:
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
    def isFiring(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_1__T], tArray: typing.List[_isFiring_1__T]) -> bool:
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

class AbstractManeuverTriggers(ManeuverTriggers):
    """
    public abstract class AbstractManeuverTriggers extends Object implements :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
    
        Base class for triggers.
    
        Since:
            11.1
    """
    _addResetter_0__T = typing.TypeVar('_addResetter_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addResetter(self, field: org.hipparchus.Field[_addResetter_0__T], fieldManeuverTriggersResetter: FieldManeuverTriggersResetter[_addResetter_0__T]) -> None:
        """
            Add a resetter.
        
            Parameters:
                field (Field<T> field): field to which the state belongs
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
    def getFirings(self) -> org.orekit.utils.TimeSpanMap[bool]:
        """
            Get the firings detected during last propagation.
        
            Returns:
                firings detected during last propagation
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
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
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...
    _isFiring_1__S = typing.TypeVar('_isFiring_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                parameters (double[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        """
        ...
    @typing.overload
    def isFiring(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_1__S], sArray: typing.List[_isFiring_1__S]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<S> date): current date
                parameters (S[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        
        """
        ...

class EventBasedManeuverTriggers(ManeuverTriggers, org.orekit.propagation.events.handlers.EventHandler[org.orekit.propagation.events.EventDetector]):
    """
    public class EventBasedManeuverTriggers extends Object implements :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`, :class:`~org.orekit.propagation.events.handlers.EventHandler`<:class:`~org.orekit.propagation.events.EventDetector`>
    
        Maneuver triggers based on start and stop detectors. This allow a succession of burn interval. The thruster starts
        firing when the start detector becomes positive. The thruster stops firing when the stop detector becomes positive. The
        2 detectors should not be positive at the same time. A date detector is not suited as it does not delimit an interval.
        They can be both negative at the same time.
    
        Since:
            10.2
    """
    @typing.overload
    def __init__(self, abstractDetector: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector], abstractDetector2: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector]): ...
    @typing.overload
    def __init__(self, abstractDetector: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector], abstractDetector2: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector], boolean: bool): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            eventOccurred method mirrors the same interface method as in :class:`~org.orekit.propagation.events.EventDetector` and
            its subclasses, but with an additional parameter that allows the calling method to pass in an object from the detector
            which would have potential additional data to allow the implementing class to determine the correct return state.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpaceCraft state to be used in the evaluation
                detector (:class:`~org.orekit.propagation.events.EventDetector`): object with appropriate type that can be used in determining correct return state
                increasing (boolean): with the event occurred in an "increasing" or "decreasing" slope direction
        
            Returns:
                the Action that the calling detector should pass back to the evaluation system
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getStartFiringDetector(self) -> org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector]: ...
    def getStopFiringDetector(self) -> org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector]: ...
    def getTriggeredEnd(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for the triggered date of engine stop.
        
            Returns:
                Triggered date of engine stop
        
        
        """
        ...
    def getTriggeredStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter triggered date of engine start.
        
            Returns:
                Triggered date of engine start
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, t: org.orekit.propagation.events.EventDetector) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    _isFiring_2__T = typing.TypeVar('_isFiring_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                parameters (double[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
            Check if maneuvering is on.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                true if maneuver is on at this date
        
        
        """
        ...
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]) -> bool: ...
    @typing.overload
    def isFiring(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_2__T], tArray: typing.List[_isFiring_2__T]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                parameters (T[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        """
        ...
    def setFiring(self, boolean: bool, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the firing start or end date depending on the firing flag. There is no effect if the firing state is not changing.
        
            Parameters:
                firing (boolean): true to start a maneuver, false to stop
                date (:class:`~org.orekit.time.AbsoluteDate`): date of event
        
        
        """
        ...

_PythonFieldManeuverTriggersResetter__T = typing.TypeVar('_PythonFieldManeuverTriggersResetter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldManeuverTriggersResetter(FieldManeuverTriggersResetter[_PythonFieldManeuverTriggersResetter__T], typing.Generic[_PythonFieldManeuverTriggersResetter__T]):
    """
    public class PythonFieldManeuverTriggersResetter<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.forces.maneuvers.trigger.FieldManeuverTriggersResetter`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def maneuverTriggered(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T], boolean: bool) -> None: ...
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
    def resetState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T]) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldManeuverTriggersResetter__T]: ...

class PythonManeuverTriggers(ManeuverTriggers):
    """
    public class PythonManeuverTriggers extends Object implements :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...)).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    _isFiring_0__T = typing.TypeVar('_isFiring_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isFiring(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_0__T], tArray: typing.List[_isFiring_0__T]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                parameters (T[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        
        """
        ...
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]) -> bool:
        """
            Find out if the maneuver is firing or not.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                parameters (double[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        """
        ...
    _isFiring_FT__T = typing.TypeVar('_isFiring_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def isFiring_FT(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_isFiring_FT__T], tArray: typing.List[_isFiring_FT__T]) -> bool: ...
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

class PythonManeuverTriggersResetter(ManeuverTriggersResetter):
    """
    public class PythonManeuverTriggersResetter extends Object implements :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def maneuverTriggered(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> None:
        """
            Observe a maneuver trigger.
        
            The :code:`start` parameter corresponds to physical flow of time from past to future, not to propagation direction which
            can be backward. This means that during forward propagations, the first call will have :code:`start` set to :code:`true`
            and the second call will have :code:`start` set to :code:`false`, whereas in backward propagation, the first call will
            have :code:`start` set to :code:`false` and the second call will have :code:`start` set to :code:`true`.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter.maneuverTriggered`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at trigger date (before applying the maneuver)
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...
    def resetState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset state as a maneuver triggers.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter.resetState`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at trigger date
        
            Returns:
                reset state taking into account maneuver start/stop
        
        
        """
        ...

_IntervalEventTrigger__T = typing.TypeVar('_IntervalEventTrigger__T', bound=org.orekit.propagation.events.AbstractDetector)  # <T>
class IntervalEventTrigger(AbstractManeuverTriggers, typing.Generic[_IntervalEventTrigger__T]):
    """
    public abstract class IntervalEventTrigger<T extends :class:`~org.orekit.propagation.events.AbstractDetector`<T>> extends :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    
        Maneuver triggers based on a single event detector that defines firing intervals.
    
        Firing intervals correspond to time spans with positive value of the event detector
        :meth:`~org.orekit.propagation.events.EventDetector.g` function.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.StartStopEventsTrigger`
    """
    def __init__(self, t: _IntervalEventTrigger__T): ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__S = typing.TypeVar('_getFieldEventsDetectors__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__S]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__S]]: ...
    def getFiringIntervalDetector(self) -> _IntervalEventTrigger__T:
        """
            Getter for the firing interval detector.
        
            Returns:
                firing interval detector
        
        
        """
        ...

class PythonAbstractManeuverTriggers(AbstractManeuverTriggers):
    """
    public class PythonAbstractManeuverTriggers extends :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def isFiringOnInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> bool:
        """
            Method to check if the thruster is firing on initialization. can be called by sub classes
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers.isFiringOnInitialState`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

_StartStopEventsTrigger__A = typing.TypeVar('_StartStopEventsTrigger__A', bound=org.orekit.propagation.events.AbstractDetector)  # <A>
_StartStopEventsTrigger__O = typing.TypeVar('_StartStopEventsTrigger__O', bound=org.orekit.propagation.events.AbstractDetector)  # <O>
class StartStopEventsTrigger(AbstractManeuverTriggers, typing.Generic[_StartStopEventsTrigger__A, _StartStopEventsTrigger__O]):
    """
    public abstract class StartStopEventsTrigger<A extends :class:`~org.orekit.propagation.events.AbstractDetector`<A>,O extends :class:`~org.orekit.propagation.events.AbstractDetector`<O>> extends :class:`~org.orekit.forces.maneuvers.trigger.AbstractManeuverTriggers`
    
        Maneuver triggers based on a pair of event detectors that defines firing start and stop.
    
        The thruster starts firing when the start detector becomes positive. The thruster stops firing when the stop detector
        becomes positive. The 2 detectors should not be positive at the same time. A date detector is not suited as it does not
        delimit an interval. They can be both negative at the same time.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`
    """
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__S = typing.TypeVar('_getFieldEventsDetectors__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__S]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__S]]: ...
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

class DateBasedManeuverTriggers(IntervalEventTrigger[org.orekit.propagation.events.ParameterDrivenDateIntervalDetector]):
    """
    public class DateBasedManeuverTriggers extends :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`<:class:`~org.orekit.propagation.events.ParameterDrivenDateIntervalDetector`>
    
        Maneuver triggers based on a start and end date, with no parameter drivers.
    
        Since:
            10.2
    """
    DEFAULT_NAME: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_NAME
    
        Default name for trigger.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
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
    """
    public class PythonIntervalEventTrigger<T extends :class:`~org.orekit.propagation.events.AbstractDetector`<T>> extends :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`<T>
    """
    def __init__(self, t: _PythonIntervalEventTrigger__T): ...
    _convertIntervalDetector__D = typing.TypeVar('_convertIntervalDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertIntervalDetector__S = typing.TypeVar('_convertIntervalDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertIntervalDetector(self, field: org.hipparchus.Field[_convertIntervalDetector__S], t: _PythonIntervalEventTrigger__T) -> org.orekit.propagation.events.FieldAbstractDetector[_convertIntervalDetector__D, _convertIntervalDetector__S]:
        """
            Convert a primitive firing intervals detector into a field firing intervals detector.
        
            There is not need to set up :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withMaxCheck`,
            :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withThreshold`, or
            :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` in the converted detector, this will be done by
            caller.
        
            A skeleton implementation of this method to convert some :code:`XyzDetector` into :code:`FieldXyzDetector`, considering
            these detectors are created from a date and a number parameter is:
        
            .. code-block: java
            
            
                 protected <D extends FieldEventDetector<S>, S extends CalculusFieldElement<S>>
                     FieldAbstractDetector<D, S> convertIntervalDetector(final Field<S> field, final XyzDetector detector) {
            
                     final FieldAbsoluteDate<S> date  = new FieldAbsoluteDate<>(field, detector.getDate());
                     final S                    param = field.getZero().newInstance(detector.getParam());
            
                     final FieldAbstractDetector<D, S> converted = (FieldAbstractDetector<D, S>) new FieldXyzDetector<>(date, param);
                     return converted;
            
                 }
             
             
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger.convertIntervalDetector`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.trigger.IntervalEventTrigger`
        
            Parameters:
                field (Field<S> field): field to which the state belongs
                detector (:class:`~org.orekit.forces.maneuvers.trigger.PythonIntervalEventTrigger`): primitive firing intervals detector to convert
        
            Returns:
                converted firing intervals detector
        
        
        """
        ...
    def finalize(self) -> None: ...
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

_PythonStartStopEventsTrigger__A = typing.TypeVar('_PythonStartStopEventsTrigger__A', bound=org.orekit.propagation.events.AbstractDetector)  # <A>
_PythonStartStopEventsTrigger__O = typing.TypeVar('_PythonStartStopEventsTrigger__O', bound=org.orekit.propagation.events.AbstractDetector)  # <O>
class PythonStartStopEventsTrigger(StartStopEventsTrigger[_PythonStartStopEventsTrigger__A, _PythonStartStopEventsTrigger__O], typing.Generic[_PythonStartStopEventsTrigger__A, _PythonStartStopEventsTrigger__O]):
    """
    public class PythonStartStopEventsTrigger<A extends :class:`~org.orekit.propagation.events.AbstractDetector`<A>,O extends :class:`~org.orekit.propagation.events.AbstractDetector`<O>> extends :class:`~org.orekit.forces.maneuvers.trigger.StartStopEventsTrigger`<A,O>
    """
    def __init__(self, a: _PythonStartStopEventsTrigger__A, o: _PythonStartStopEventsTrigger__O): ...
    _convertStartDetector__D = typing.TypeVar('_convertStartDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertStartDetector__S = typing.TypeVar('_convertStartDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertStartDetector(self, field: org.hipparchus.Field[_convertStartDetector__S], a: _PythonStartStopEventsTrigger__A) -> org.orekit.propagation.events.FieldAbstractDetector[_convertStartDetector__D, _convertStartDetector__S]:
        """
            Convert a primitive firing start detector into a field firing start detector.
        
            There is not need to set up :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withMaxCheck`,
            :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withThreshold`, or
            :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` in the converted detector, this will be done by
            caller.
        
            A skeleton implementation of this method to convert some :code:`XyzDetector` into :code:`FieldXyzDetector`, considering
            these detectors are created from a date and a number parameter is:
        
            .. code-block: java
            
            
                 protected <D extends FieldEventDetector<S>, S extends CalculusFieldElement<S>>
                     FieldAbstractDetector<D, S> convertStartDetector(final Field<S> field, final XyzDetector detector) {
            
                     final FieldAbsoluteDate<S> date  = new FieldAbsoluteDate<>(field, detector.getDate());
                     final S                    param = field.getZero().newInstance(detector.getParam());
            
                     final FieldAbstractDetector<D, S> converted = (FieldAbstractDetector<D, S>) new FieldXyzDetector<>(date, param);
                     return converted;
            
                 }
             
             
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.StartStopEventsTrigger.convertStartDetector`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.trigger.StartStopEventsTrigger`
        
            Parameters:
                field (Field<S> field): field to which the state belongs
                detector (:class:`~org.orekit.forces.maneuvers.trigger.PythonStartStopEventsTrigger`): primitive firing start detector to convert
        
            Returns:
                converted firing start detector
        
        
        """
        ...
    _convertStopDetector__D = typing.TypeVar('_convertStopDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    _convertStopDetector__S = typing.TypeVar('_convertStopDetector__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    def convertStopDetector(self, field: org.hipparchus.Field[_convertStopDetector__S], o: _PythonStartStopEventsTrigger__O) -> org.orekit.propagation.events.FieldAbstractDetector[_convertStopDetector__D, _convertStopDetector__S]:
        """
            Convert a primitive firing stop detector into a field firing stop detector.
        
            There is not need to set up :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withMaxCheck`,
            :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withThreshold`, or
            :meth:`~org.orekit.propagation.events.FieldAbstractDetector.withHandler` in the converted detector, this will be done by
            caller.
        
            A skeleton implementation of this method to convert some :code:`XyzDetector` into :code:`FieldXyzDetector`, considering
            these detectors are created from a date and a number parameter is:
        
            .. code-block: java
            
            
                 protected <D extends FieldEventDetector<S>, S extends CalculusFieldElement<S>>
                     FieldAbstractDetector<D, S> convertStopDetector(final Field<S> field, final XyzDetector detector) {
            
                     final FieldAbsoluteDate<S> date  = new FieldAbsoluteDate<>(field, detector.getDate());
                     final S                    param = field.getZero().newInstance(detector.getParam());
            
                     final FieldAbstractDetector<D, S> converted = (FieldAbstractDetector<D, S>) new FieldXyzDetector<>(date, param);
                     return converted;
            
                 }
             
             
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.StartStopEventsTrigger.convertStopDetector`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.trigger.StartStopEventsTrigger`
        
            Parameters:
                field (Field<S> field): field to which the state belongs
                detector (:class:`~org.orekit.forces.maneuvers.trigger.PythonStartStopEventsTrigger`): primitive firing stop detector to convert
        
            Returns:
                converted firing stop detector
        
        
        """
        ...
    def finalize(self) -> None: ...
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers.trigger")``.

    AbstractManeuverTriggers: typing.Type[AbstractManeuverTriggers]
    DateBasedManeuverTriggers: typing.Type[DateBasedManeuverTriggers]
    EventBasedManeuverTriggers: typing.Type[EventBasedManeuverTriggers]
    FieldManeuverTriggersResetter: typing.Type[FieldManeuverTriggersResetter]
    IntervalEventTrigger: typing.Type[IntervalEventTrigger]
    ManeuverTriggers: typing.Type[ManeuverTriggers]
    ManeuverTriggersResetter: typing.Type[ManeuverTriggersResetter]
    PythonAbstractManeuverTriggers: typing.Type[PythonAbstractManeuverTriggers]
    PythonFieldManeuverTriggersResetter: typing.Type[PythonFieldManeuverTriggersResetter]
    PythonIntervalEventTrigger: typing.Type[PythonIntervalEventTrigger]
    PythonManeuverTriggers: typing.Type[PythonManeuverTriggers]
    PythonManeuverTriggersResetter: typing.Type[PythonManeuverTriggersResetter]
    PythonStartStopEventsTrigger: typing.Type[PythonStartStopEventsTrigger]
    StartStopEventsTrigger: typing.Type[StartStopEventsTrigger]
