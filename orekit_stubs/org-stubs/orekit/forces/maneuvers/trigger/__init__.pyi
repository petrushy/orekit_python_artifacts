import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.ode.events
import org.orekit.forces.maneuvers.trigger.class-use
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.events.handlers
import org.orekit.time
import org.orekit.utils
import typing



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
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...)).
        
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

class DateBasedManeuverTriggers(ManeuverTriggers):
    """
    public class DateBasedManeuverTriggers extends :class:`~org.orekit.forces.maneuvers.trigger.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
    
        Maneuver triggers based on a start and end date, with no parameter drivers.
    
        Since:
            10.2
    """
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
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getStartDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date.
        
            Returns:
                the start date
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...)).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
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
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.isFiring` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
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
            Description copied from interface: :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.isFiring`
            Find out if the maneuver is firing or not.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.isFiring` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                parameters (T[]): maneuver triggers parameters
        
            Returns:
                true if the maneuver is firing, false otherwise
        
        """
        ...

class EventBasedManeuverTriggers(ManeuverTriggers, org.orekit.propagation.events.handlers.EventHandler[org.orekit.propagation.events.EventDetector]):
    """
    public class EventBasedManeuverTriggers extends :class:`~org.orekit.forces.maneuvers.trigger.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`, :class:`~org.orekit.propagation.events.handlers.EventHandler`<:class:`~org.orekit.propagation.events.EventDetector`>
    
        Maneuver triggers based on start and stop detectors. This allow a succession of burn interval. The thruster starts
        firing when the start detector becomes positive. The thruster stops firing when the stop detector becomes positive. The
        2 detectors should not be positive at the same time. A date detector is not suited as it does not delimit an interval.
        They can be both negative at the same time.
    
        Since:
            10.2
    """
    def __init__(self, abstractDetector: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector], abstractDetector2: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector]): ...
    def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action:
        """
            eventOccurred method mirrors the same interface method as in :class:`~org.orekit.propagation.events.EventDetector` and
            its subclasses, but with an additional parameter that allows the calling method to pass in an object from the detector
            which would have potential additional data to allow the implementing class to determine the correct return state.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` in
                interface :class:`~org.orekit.propagation.events.handlers.EventHandler`
        
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
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, t: org.orekit.propagation.events.EventDetector) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...)).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.init` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
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
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.isFiring` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
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
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers.isFiring` in
                interface :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggers`
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers.trigger")``.

    DateBasedManeuverTriggers: typing.Type[DateBasedManeuverTriggers]
    EventBasedManeuverTriggers: typing.Type[EventBasedManeuverTriggers]
    ManeuverTriggers: typing.Type[ManeuverTriggers]
    class-use: org.orekit.forces.maneuvers.trigger.class-use.__module_protocol__
