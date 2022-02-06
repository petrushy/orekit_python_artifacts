import java.lang
import java.util
import org.hipparchus.random
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.gnss
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.sampling
import org.orekit.time
import typing



class Generator:
    """
    public class Generator extends Object
    
        Main generator for :class:`~org.orekit.estimation.measurements.ObservedMeasurement`.
    
        Since:
            9.3
    """
    def __init__(self): ...
    def addPropagator(self, propagator: org.orekit.propagation.Propagator) -> org.orekit.estimation.measurements.ObservableSatellite:
        """
            Add a propagator.
        
            Parameters:
                propagator (:class:`~org.orekit.propagation.Propagator`): to add
        
            Returns:
                satellite satellite propagated by the propagator
        
        
        """
        ...
    _addScheduler__T = typing.TypeVar('_addScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    def addScheduler(self, scheduler: 'Scheduler'[_addScheduler__T]) -> None:
        """
            Add a sequences generator for a specific measurement type.
        
            Parameters:
                scheduler (:class:`~org.orekit.estimation.measurements.generation.Scheduler`<T> scheduler): sequences generator to add
        
        
        """
        ...
    def generate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> java.util.SortedSet[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]: ...
    def getPropagator(self, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite) -> org.orekit.propagation.Propagator:
        """
            Get a registered propagator.
        
            Parameters:
                satellite (:class:`~org.orekit.estimation.measurements.ObservableSatellite`): satellite propagated by the propagator :meth:`~org.orekit.estimation.measurements.generation.Generator.addPropagator`
        
            Returns:
                propagator corresponding to satellite
        
        
        """
        ...

_MeasurementBuilder__T = typing.TypeVar('_MeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class MeasurementBuilder(typing.Generic[_MeasurementBuilder__T]):
    """
    public interface MeasurementBuilder<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>>
    
        Interface for generating individual :class:`~org.orekit.estimation.measurements.ObservedMeasurement`.
    
        Since:
            9.3
    """
    def addModifier(self, estimationModifier: org.orekit.estimation.measurements.EstimationModifier[_MeasurementBuilder__T]) -> None: ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> _MeasurementBuilder__T:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_MeasurementBuilder__T]]: ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize builder at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the builder to initialize some
            internal data if needed, typically setting up parameters reference dates.
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

_Scheduler__T = typing.TypeVar('_Scheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class Scheduler(typing.Generic[_Scheduler__T]):
    """
    public interface Scheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>>
    
        Interface for generating :class:`~org.orekit.estimation.measurements.ObservedMeasurement` sequences.
    
        Since:
            9.3
    """
    def generate(self, list: java.util.List[org.orekit.propagation.sampling.OrekitStepInterpolator]) -> java.util.SortedSet[_Scheduler__T]: ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize scheduler at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the scheduler to initialize
            some internal data if needed, typically :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init`.
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

class SignSemantic(java.lang.Enum['SignSemantic']):
    """
    public enum SignSemantic extends Enum<:class:`~org.orekit.estimation.measurements.generation.SignSemantic`>
    
        Enumerate for the semantic of the :code:`g` function sign during measurements generation.
    
        Since:
            9.3
    
        Also see:
            :class:`~org.orekit.estimation.measurements.generation.EventBasedScheduler`
    """
    FEASIBLE_MEASUREMENT_WHEN_POSITIVE: typing.ClassVar['SignSemantic'] = ...
    FEASIBLE_MEASUREMENT_WHEN_NEGATIVE: typing.ClassVar['SignSemantic'] = ...
    def measurementIsFeasible(self, double: float) -> bool:
        """
            Check if measurement is feasible.
        
            Parameters:
                g (double): value of the detector g function
        
            Returns:
                true if measurement is feasible
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SignSemantic':
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
    def values() -> typing.List['SignSemantic']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (SignSemantic c : SignSemantic.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_AbstractMeasurementBuilder__T = typing.TypeVar('_AbstractMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractMeasurementBuilder(MeasurementBuilder[_AbstractMeasurementBuilder__T], typing.Generic[_AbstractMeasurementBuilder__T]):
    """
    public abstract class AbstractMeasurementBuilder<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`<T>
    
        Base class for :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`.
    
        Since:
            9.3
    """
    def addModifier(self, estimationModifier: org.orekit.estimation.measurements.EstimationModifier[_AbstractMeasurementBuilder__T]) -> None: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_AbstractMeasurementBuilder__T]]: ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize builder at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the builder to initialize some
            internal data if needed, typically setting up parameters reference dates.
        
            This implementation stores the time span of the measurements generation.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

_AbstractScheduler__T = typing.TypeVar('_AbstractScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractScheduler(Scheduler[_AbstractScheduler__T], typing.Generic[_AbstractScheduler__T]):
    """
    public abstract class AbstractScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.generation.Scheduler`<T>
    
        Base implementation of :class:`~org.orekit.estimation.measurements.generation.Scheduler` managing
        :class:`~org.orekit.time.DatesSelector`.
    
        Since:
            9.3
    """
    def getBuilder(self) -> MeasurementBuilder[_AbstractScheduler__T]: ...
    def getSelector(self) -> org.orekit.time.DatesSelector:
        """
            Get the dates selector.
        
            Returns:
                dates selector
        
        
        """
        ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize scheduler at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the scheduler to initialize
            some internal data if needed, typically :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init`.
        
            This implementation initialize the measurement builder.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.Scheduler.init`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.generation.Scheduler`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

_PythonMeasurementBuilder__T = typing.TypeVar('_PythonMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonMeasurementBuilder(MeasurementBuilder[_PythonMeasurementBuilder__T], typing.Generic[_PythonMeasurementBuilder__T]):
    """
    public class PythonMeasurementBuilder<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`<T>
    """
    def __init__(self): ...
    def addModifier(self, estimationModifier: org.orekit.estimation.measurements.EstimationModifier[_PythonMeasurementBuilder__T]) -> None: ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> _PythonMeasurementBuilder__T:
        """
            Generate a single measurement.
        
            Specified by:
                 in interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_PythonMeasurementBuilder__T]]: ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize builder at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the builder to initialize some
            internal data if needed, typically setting up parameters reference dates.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
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

_PythonScheduler__T = typing.TypeVar('_PythonScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonScheduler(Scheduler[_PythonScheduler__T], typing.Generic[_PythonScheduler__T]):
    """
    public class PythonScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.generation.Scheduler`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def generate(self, list: java.util.List[org.orekit.propagation.sampling.OrekitStepInterpolator]) -> java.util.SortedSet[_PythonScheduler__T]: ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize scheduler at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the scheduler to initialize
            some internal data if needed, typically :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init`.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.Scheduler.init`Â in
                interfaceÂ :class:`~org.orekit.estimation.measurements.generation.Scheduler`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
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

class AngularAzElBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.AngularAzEl]):
    """
    public class AngularAzElBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
        Builder for :class:`~org.orekit.estimation.measurements.AngularAzEl` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, doubleArray: typing.List[float], doubleArray2: typing.List[float], observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.AngularAzEl:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

class AngularRaDecBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.AngularRaDec]):
    """
    public class AngularRaDecBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.AngularRaDec`>
    
        Builder for :class:`~org.orekit.estimation.measurements.AngularRaDec` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, frame: org.orekit.frames.Frame, doubleArray: typing.List[float], doubleArray2: typing.List[float], observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.AngularRaDec:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

_ContinuousScheduler__T = typing.TypeVar('_ContinuousScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ContinuousScheduler(AbstractScheduler[_ContinuousScheduler__T], typing.Generic[_ContinuousScheduler__T]):
    """
    public class ContinuousScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`<T>
    
        :class:`~org.orekit.estimation.measurements.generation.Scheduler` generating measurements sequences continuously.
    
        Continuous schedulers continuously generate measurements following a repetitive pattern. The repetitive pattern can be
        either a continuous stream of measurements separated by a constant step (for example one measurement every 60s), or
        several sequences of measurements at high rate up to a maximum number, with a rest period between sequences (for example
        sequences of up to 256 measurements every 100ms with 300s between each sequence).
    
        Since:
            9.3
    """
    def __init__(self, measurementBuilder: MeasurementBuilder[_ContinuousScheduler__T], datesSelector: org.orekit.time.DatesSelector): ...
    def generate(self, list: java.util.List[org.orekit.propagation.sampling.OrekitStepInterpolator]) -> java.util.SortedSet[_ContinuousScheduler__T]: ...

_EventBasedScheduler__T = typing.TypeVar('_EventBasedScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class EventBasedScheduler(AbstractScheduler[_EventBasedScheduler__T], typing.Generic[_EventBasedScheduler__T]):
    """
    public class EventBasedScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`<T>
    
        :class:`~org.orekit.estimation.measurements.generation.Scheduler` based on
        :class:`~org.orekit.propagation.events.EventDetector` for generating measurements sequences.
    
        Event-based schedulers generate measurements following a repetitive pattern when the a
        :class:`~org.orekit.propagation.events.EventDetector` provided at construction is in a
        :class:`~org.orekit.estimation.measurements.generation.SignSemantic` state. It is important that the sign of the g
        function of the underlying event detector is not arbitrary, but has a semantic meaning, e.g. in or out, true or false.
        This class works well with event detectors that detect entry to or exit from a region, e.g.
        :class:`~org.orekit.propagation.events.EclipseDetector`, :class:`~org.orekit.propagation.events.ElevationDetector`,
        :class:`~org.orekit.propagation.events.LatitudeCrossingDetector`. Using this scheduler with detectors that are not based
        on entry to or exit from a region, e.g. :class:`~org.orekit.propagation.events.DateDetector`,
        :class:`~org.orekit.propagation.events.LongitudeCrossingDetector`, will likely lead to unexpected results.
    
        The repetitive pattern can be either a continuous stream of measurements separated by a constant step (for example one
        measurement every 60s), or several sequences of measurements at high rate up to a maximum number, with a rest period
        between sequences (for example sequences of up to 256 measurements every 100ms with 300s between each sequence).
    
        Since:
            9.3
    """
    def __init__(self, measurementBuilder: MeasurementBuilder[_EventBasedScheduler__T], datesSelector: org.orekit.time.DatesSelector, propagator: org.orekit.propagation.Propagator, eventDetector: org.orekit.propagation.events.EventDetector, signSemantic: SignSemantic): ...
    def generate(self, list: java.util.List[org.orekit.propagation.sampling.OrekitStepInterpolator]) -> java.util.SortedSet[_EventBasedScheduler__T]: ...

class InterSatellitesPhaseBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class InterSatellitesPhaseBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Builder for :class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase` measurements.
    
        Since:
            10.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, double: float, double2: float, double3: float): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.gnss.InterSatellitesPhase:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

class InterSatellitesRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    public class InterSatellitesRangeBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        Builder for :class:`~org.orekit.estimation.measurements.InterSatellitesRange` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, boolean: bool, double: float, double2: float): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.InterSatellitesRange:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

class PVBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.PV]):
    """
    public class PVBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.PV`>
    
        Builder for :class:`~org.orekit.estimation.measurements.PV` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.PV:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

class PositionBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.Position]):
    """
    public class PositionBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.Position`>
    
        Builder for :class:`~org.orekit.estimation.measurements.Position` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.Position:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

_PythonAbstractMeasurementBuilder__T = typing.TypeVar('_PythonAbstractMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractMeasurementBuilder(AbstractMeasurementBuilder[_PythonAbstractMeasurementBuilder__T], typing.Generic[_PythonAbstractMeasurementBuilder__T]):
    """
    public class PythonAbstractMeasurementBuilder<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<T>
    """
    @typing.overload
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, double: float, double2: float, observableSatelliteArray: typing.List[org.orekit.estimation.measurements.ObservableSatellite]): ...
    @typing.overload
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, doubleArray: typing.List[float], doubleArray2: typing.List[float], observableSatelliteArray: typing.List[org.orekit.estimation.measurements.ObservableSatellite]): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> _PythonAbstractMeasurementBuilder__T:
        """
            Generate a single measurement. Extension point for Python.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): spacecraft states
        
            Returns:
                generated measurement
        
        
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

_PythonAbstractScheduler__T = typing.TypeVar('_PythonAbstractScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractScheduler(AbstractScheduler[_PythonAbstractScheduler__T], typing.Generic[_PythonAbstractScheduler__T]):
    """
    public class PythonAbstractScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`<T>
    """
    def __init__(self, measurementBuilder: MeasurementBuilder[_PythonAbstractScheduler__T], datesSelector: org.orekit.time.DatesSelector): ...
    def finalize(self) -> None: ...
    def generate(self, list: java.util.List[org.orekit.propagation.sampling.OrekitStepInterpolator]) -> java.util.SortedSet[_PythonAbstractScheduler__T]: ...
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

class RangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.Range]):
    """
    public class RangeBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Builder for :class:`~org.orekit.estimation.measurements.Range` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, boolean: bool, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.Range:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

class RangeRateBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.RangeRate]):
    """
    public class RangeRateBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Builder for :class:`~org.orekit.estimation.measurements.RangeRate` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, boolean: bool, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.RangeRate:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...

class TurnAroundRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    public class TurnAroundRangeBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
        Builder for :class:`~org.orekit.estimation.measurements.TurnAroundRange` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, groundStation2: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> org.orekit.estimation.measurements.TurnAroundRange:
        """
            Generate a single measurement.
        
            Parameters:
                states (:class:`~org.orekit.propagation.SpacecraftState`[]): all spacecraft states (i.e. including ones that may not be relevant for the current builder)
        
            Returns:
                generated measurement
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.generation")``.

    AbstractMeasurementBuilder: typing.Type[AbstractMeasurementBuilder]
    AbstractScheduler: typing.Type[AbstractScheduler]
    AngularAzElBuilder: typing.Type[AngularAzElBuilder]
    AngularRaDecBuilder: typing.Type[AngularRaDecBuilder]
    ContinuousScheduler: typing.Type[ContinuousScheduler]
    EventBasedScheduler: typing.Type[EventBasedScheduler]
    Generator: typing.Type[Generator]
    InterSatellitesPhaseBuilder: typing.Type[InterSatellitesPhaseBuilder]
    InterSatellitesRangeBuilder: typing.Type[InterSatellitesRangeBuilder]
    MeasurementBuilder: typing.Type[MeasurementBuilder]
    PVBuilder: typing.Type[PVBuilder]
    PositionBuilder: typing.Type[PositionBuilder]
    PythonAbstractMeasurementBuilder: typing.Type[PythonAbstractMeasurementBuilder]
    PythonAbstractScheduler: typing.Type[PythonAbstractScheduler]
    PythonMeasurementBuilder: typing.Type[PythonMeasurementBuilder]
    PythonScheduler: typing.Type[PythonScheduler]
    RangeBuilder: typing.Type[RangeBuilder]
    RangeRateBuilder: typing.Type[RangeRateBuilder]
    Scheduler: typing.Type[Scheduler]
    SignSemantic: typing.Type[SignSemantic]
    TurnAroundRangeBuilder: typing.Type[TurnAroundRangeBuilder]
