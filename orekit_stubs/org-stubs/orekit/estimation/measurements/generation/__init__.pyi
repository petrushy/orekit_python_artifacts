
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.hipparchus.random
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.gnss
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.sampling
import org.orekit.time
import typing



class GeneratedMeasurementSubscriber:
    """
    Interface for subscribing to generated EstimatedMeasurementBase events.
    
    Since:
        12.0
    """
    def handleGeneratedMeasurement(self, measurement: org.orekit.estimation.measurements.EstimatedMeasurementBase[typing.Any]) -> None:
        """
        Handle a generated measurement.
        
        Parameters:
            measurement (EstimatedMeasurementBase<?> measurement): measurements that has just been generated
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize subscriber at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the subscriber to initialize some internal data if needed.
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...

class Generator:
    """
    Main generator for ObservedMeasurement.
    
    Since:
        9.3
    """
    def __init__(self):
        """
        Build a generator with no sequences generator.
        """
        ...
    @typing.overload
    def addPropagator(self, propagator: org.orekit.propagation.Propagator) -> org.orekit.estimation.measurements.ObservableSatellite:
        """
        Add a propagator.
        
        Parameters:
            propagator (Propagator): to add
        
        Returns:
            satellite satellite propagated by the propagator
        
        Add a propagator.
        
        Parameters:
            propagator (Propagator): to add
            name (String): satellite name (if null, a default name built from index will be used)
        
        Returns:
            satellite satellite propagated by the propagator
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def addPropagator(self, propagator: org.orekit.propagation.Propagator, name: str) -> org.orekit.estimation.measurements.ObservableSatellite: ...
    _addScheduler__T = typing.TypeVar('_addScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    def addScheduler(self, scheduler: 'Scheduler'[_addScheduler__T]) -> None:
        """
        Add a sequences generator for a specific measurement type.
        
        Parameters:
            scheduler (Scheduler<T> scheduler): sequences generator to add
        
        
        """
        ...
    def addSubscriber(self, subscriber: GeneratedMeasurementSubscriber) -> None:
        """
        Add a subscriber.
        
        Parameters:
            subscriber (GeneratedMeasurementSubscriber): to add
        
        Since:
            12.0
        
        Also see:
            GatheringSubscriber
        
        
        """
        ...
    def generate(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Generate measurements.
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...
    def getPropagator(self, satellite: org.orekit.estimation.measurements.ObservableSatellite) -> org.orekit.propagation.Propagator:
        """
        Get a registered propagator.
        
        Parameters:
            satellite (ObservableSatellite): satellite propagated by the propagator addPropagator
        
        Returns:
            propagator corresponding to satellite
        
        
        """
        ...

_MeasurementBuilder__T = typing.TypeVar('_MeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class MeasurementBuilder(typing.Generic[_MeasurementBuilder__T]):
    """
    Interface for generating individual ObservedMeasurement.
    
    Since:
        9.3
    """
    def addModifier(self, modifier: org.orekit.estimation.measurements.EstimationModifier[_MeasurementBuilder__T]) -> None:
        """
        Add a modifier.
        
        Parameters:
            modifier (EstimationModifier<MeasurementBuilder> modifier): modifier to add
        
        
        """
        ...
    @typing.overload
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_MeasurementBuilder__T]: ...
    @typing.overload
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, spacecraftStateArray: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_MeasurementBuilder__T]: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_MeasurementBuilder__T]]:
        """
        Get the modifiers that apply to a measurement.
        
        Returns:
            modifiers that apply to a measurement
        
        Also see:
            addModifier
        
        
        """
        ...
    def getSatellites(self) -> typing.MutableSequence[org.orekit.estimation.measurements.ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Returns:
            satellites related to this measurement
        
        Since:
            12.0
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize builder at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the builder to initialize some internal data if needed, typically setting up parameters reference dates.
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...

_Scheduler__T = typing.TypeVar('_Scheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class Scheduler(typing.Generic[_Scheduler__T]):
    """
    Interface for generating ObservedMeasurement sequences.
    
    Since:
        9.3
    """
    def generate(self, interpolators: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> java.util.SortedSet[org.orekit.estimation.measurements.EstimatedMeasurementBase[_Scheduler__T]]:
        """
        Generate a sequence of measurements.
        
        Parameters:
            interpolators (Map<ObservableSatellite, OrekitStepInterpolator> interpolators): interpolators for spacecraft states
        
        Returns:
            generated measurements
        
        Since:
            12.0
        
        
        """
        ...
    def getBuilder(self) -> MeasurementBuilder[_Scheduler__T]:
        """
        Get the builder associated with this scheduler.
        
        Returns:
            builder associated with this scheduler
        
        Since:
            12.0
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize scheduler at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the scheduler to initialize some internal data if needed, typically init.
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...

class SignSemantic(java.lang.Enum['SignSemantic']):
    """
    Enumerate for the semantic of the g function sign during measurements generation.
    
    Since:
        9.3
    
    Also see:
        EventBasedScheduler
    """
    FEASIBLE_MEASUREMENT_WHEN_POSITIVE: typing.ClassVar['SignSemantic'] = ...
    FEASIBLE_MEASUREMENT_WHEN_NEGATIVE: typing.ClassVar['SignSemantic'] = ...
    def measurementIsFeasible(self, g: float) -> bool:
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
    def valueOf(name: str) -> 'SignSemantic':
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
    def values() -> typing.MutableSequence['SignSemantic']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SignSemantic c : SignSemantic.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_AbstractMeasurementBuilder__T = typing.TypeVar('_AbstractMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractMeasurementBuilder(MeasurementBuilder[_AbstractMeasurementBuilder__T], typing.Generic[_AbstractMeasurementBuilder__T]):
    """
    Base class for MeasurementBuilder.
    
    Since:
        9.3
    """
    def addModifier(self, modifier: org.orekit.estimation.measurements.EstimationModifier[_AbstractMeasurementBuilder__T]) -> None:
        """
        Add a modifier.
        
        Specified by: addModifier in interface MeasurementBuilder
        
        Parameters:
            modifier (EstimationModifier<AbstractMeasurementBuilder> modifier): modifier to add
        
        
        """
        ...
    @typing.overload
    def build(self, date: org.orekit.time.AbsoluteDate, interpolators: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_AbstractMeasurementBuilder__T]: ...
    @typing.overload
    def build(self, date: org.orekit.time.AbsoluteDate, interpolators: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_AbstractMeasurementBuilder__T]: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_AbstractMeasurementBuilder__T]]:
        """
        Get the modifiers that apply to a measurement.
        
        Specified by: getModifiers in interface MeasurementBuilder
        
        Returns:
            modifiers that apply to a measurement
        
        Also see:
            addModifier
        
        
        """
        ...
    def getSatellites(self) -> typing.MutableSequence[org.orekit.estimation.measurements.ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Specified by: getSatellites in interface MeasurementBuilder
        
        Returns:
            satellites related to this measurement
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize builder at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the builder to initialize some internal data if needed, typically setting up parameters reference dates.
        
        This implementation stores the time span of the measurements generation.
        
        Specified by: init in interface MeasurementBuilder
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...

_AbstractScheduler__T = typing.TypeVar('_AbstractScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractScheduler(Scheduler[_AbstractScheduler__T], typing.Generic[_AbstractScheduler__T]):
    """
    Base implementation of Scheduler managing DatesSelector.
    
    Since:
        9.3
    """
    def generate(self, interpolators: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> java.util.SortedSet[org.orekit.estimation.measurements.EstimatedMeasurementBase[_AbstractScheduler__T]]:
        """
        Generate a sequence of measurements.
        
        Specified by: generate in interface Scheduler
        
        Parameters:
            interpolators (Map<ObservableSatellite, OrekitStepInterpolator> interpolators): interpolators for spacecraft states
        
        Returns:
            generated measurements
        
        
        """
        ...
    def getBuilder(self) -> MeasurementBuilder[_AbstractScheduler__T]:
        """
        Get the builder associated with this scheduler.
        
        Specified by: getBuilder in interface Scheduler
        
        Returns:
            builder associated with this scheduler
        
        
        """
        ...
    def getSelector(self) -> org.orekit.time.DatesSelector:
        """
        Get the dates selector.
        
        Returns:
            dates selector
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize scheduler at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the scheduler to initialize some internal data if needed, typically init.
        
        This implementation initialize the measurement builder.
        
        Specified by: init in interface Scheduler
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...

class GatheringSubscriber(GeneratedMeasurementSubscriber):
    """
    Subscriber that gather all generated measurements in a sorted set.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getGeneratedMeasurements(self) -> java.util.SortedSet[org.orekit.estimation.measurements.EstimatedMeasurementBase[typing.Any]]:
        """
        Get generated measurements.
        
        The measurements are sorted according to ComparableMeasurement if generation was chronological, or reversed ComparableMeasurement if generation was non-chronological.
        
        Returns:
            unmodifiable view of generated measurements
        
        
        """
        ...
    def handleGeneratedMeasurement(self, measurement: org.orekit.estimation.measurements.EstimatedMeasurementBase[typing.Any]) -> None:
        """
        Handle a generated measurement.
        
        Specified by: handleGeneratedMeasurement in interface GeneratedMeasurementSubscriber
        
        Parameters:
            measurement (EstimatedMeasurementBase<?> measurement): measurements that has just been generated
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize subscriber at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the subscriber to initialize some internal data if needed.
        
        Specified by: init in interface GeneratedMeasurementSubscriber
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...

class MultiplexedMeasurementBuilder(MeasurementBuilder[org.orekit.estimation.measurements.MultiplexedMeasurement]):
    """
    Builder for MultiplexedMeasurement measurements.
    
    Since:
        12.0
    """
    def __init__(self, builders: java.util.List[MeasurementBuilder[typing.Any]]):
        """
        Simple constructor.
        
        Parameters:
            builders (List<MeasurementBuilder<?>>): builders for multiplexed measurements
        
        
        """
        ...
    def addModifier(self, modifier: org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.MultiplexedMeasurement]) -> None:
        """
        Add a modifier.
        
        Specified by: addModifier in interface MeasurementBuilder
        
        Parameters:
            modifier (EstimationModifier<MultiplexedMeasurement> modifier): modifier to add
        
        
        """
        ...
    @typing.overload
    def build(self, date: org.orekit.time.AbsoluteDate, interpolators: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.ObservedMeasurement]: ...
    @typing.overload
    def build(self, date: org.orekit.time.AbsoluteDate, interpolators: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.MultiplexedMeasurement]: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.MultiplexedMeasurement]]:
        """
        Get the modifiers that apply to a measurement.
        
        Specified by: getModifiers in interface MeasurementBuilder
        
        Returns:
            modifiers that apply to a measurement
        
        Also see:
            addModifier
        
        
        """
        ...
    def getSatellites(self) -> typing.MutableSequence[org.orekit.estimation.measurements.ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Specified by: getSatellites in interface MeasurementBuilder
        
        Returns:
            satellites related to this measurement
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize builder at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the builder to initialize some internal data if needed, typically setting up parameters reference dates.
        
        This implementation stores the time span of the measurements generation.
        
        Specified by: init in interface MeasurementBuilder
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...

class PythonGeneratedMeasurementSubscriber(GeneratedMeasurementSubscriber):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def handleGeneratedMeasurement(self, measurement: org.orekit.estimation.measurements.EstimatedMeasurementBase[typing.Any]) -> None:
        """
        Description copied from interface: handleGeneratedMeasurement Handle a generated measurement.
        
        Specified by: handleGeneratedMeasurement in interface GeneratedMeasurementSubscriber
        
        Parameters:
            measurement (EstimatedMeasurementBase<?> measurement): measurements that has just been generated
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Description copied from interface: init Initialize subscriber at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the subscriber to initialize some internal data if needed.
        
        Specified by: init in interface GeneratedMeasurementSubscriber
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

_PythonMeasurementBuilder__T = typing.TypeVar('_PythonMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonMeasurementBuilder(MeasurementBuilder[_PythonMeasurementBuilder__T], typing.Generic[_PythonMeasurementBuilder__T]):
    def __init__(self): ...
    def addModifier(self, modifier: org.orekit.estimation.measurements.EstimationModifier[_PythonMeasurementBuilder__T]) -> None:
        """
        Add a modifier.
        
        Specified by: addModifier in interface MeasurementBuilder
        
        Parameters:
            modifier (EstimationModifier<PythonMeasurementBuilder> modifier): modifier to add
        
        
        """
        ...
    @typing.overload
    def build(self, date: org.orekit.time.AbsoluteDate, interpolators: typing.Union[typing.List[org.orekit.propagation.SpacecraftState], jpype.JArray]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonMeasurementBuilder__T]: ...
    @typing.overload
    def build(self, date: org.orekit.time.AbsoluteDate, interpolators: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonMeasurementBuilder__T]: ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_PythonMeasurementBuilder__T]]:
        """
        Get the modifiers that apply to a measurement.
        
        Specified by: getModifiers in interface MeasurementBuilder
        
        Returns:
            modifiers that apply to a measurement
        
        Also see:
            addModifier
        
        
        """
        ...
    def getSatellites(self) -> typing.MutableSequence[org.orekit.estimation.measurements.ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Specified by: getSatellites in interface MeasurementBuilder
        
        Returns:
            satellites related to this measurement
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize builder at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the builder to initialize some internal data if needed, typically setting up parameters reference dates.
        
        Specified by: init in interface MeasurementBuilder
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
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

_PythonScheduler__T = typing.TypeVar('_PythonScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonScheduler(Scheduler[_PythonScheduler__T], typing.Generic[_PythonScheduler__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def generate(self, interpolators: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> java.util.SortedSet[org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonScheduler__T]]:
        """
        Generate a sequence of measurements.
        
        Specified by: generate in interface Scheduler
        
        Parameters:
            interpolators (Map<ObservableSatellite, OrekitStepInterpolator> interpolators): interpolators for spacecraft states
        
        Returns:
            generated measurements
        
        
        """
        ...
    def getBuilder(self) -> MeasurementBuilder[_PythonScheduler__T]:
        """
        Get the builder associated with this scheduler.
        
        Specified by: getBuilder in interface Scheduler
        
        Returns:
            builder associated with this scheduler
        
        
        """
        ...
    def init(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize scheduler at the start of a measurements generation.
        
        This method is called once at the start of the measurements generation. It may be used by the scheduler to initialize some internal data if needed, typically init.
        
        Specified by: init in interface Scheduler
        
        Parameters:
            start (AbsoluteDate): start of the measurements time span
            end (AbsoluteDate): end of the measurements time span
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class AngularAzElBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.AngularAzEl]):
    """
    Builder for AngularAzEl measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, station: org.orekit.estimation.measurements.GroundStation, sigma: typing.Union[typing.List[float], jpype.JArray], baseWeight: typing.Union[typing.List[float], jpype.JArray], satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            station (GroundStation): ground station from which measurement is performed
            sigma (double[]): theoretical standard deviation
            baseWeight (double[]): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class AngularRaDecBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.AngularRaDec]):
    """
    Builder for AngularRaDec measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, station: org.orekit.estimation.measurements.GroundStation, referenceFrame: org.orekit.frames.Frame, sigma: typing.Union[typing.List[float], jpype.JArray], baseWeight: typing.Union[typing.List[float], jpype.JArray], satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            station (GroundStation): ground station from which measurement is performed
            referenceFrame (Frame): Reference frame in which the right ascension - declination angles are given
            sigma (double[]): theoretical standard deviation
            baseWeight (double[]): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class BistaticRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.BistaticRange]):
    """
    Builder for BistaticRange measurements.
    
    Since:
        11.2
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, emitter: org.orekit.estimation.measurements.GroundStation, receiver: org.orekit.estimation.measurements.GroundStation, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            emitter (GroundStation): emitter ground station
            receiver (GroundStation): receiver ground station, from which measurement is performed
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class BistaticRangeRateBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.BistaticRangeRate]):
    """
    Builder for BistaticRangeRate measurements.
    
    Since:
        11.2
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, emitter: org.orekit.estimation.measurements.GroundStation, receiver: org.orekit.estimation.measurements.GroundStation, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            emitter (GroundStation): emitter ground station
            receiver (GroundStation): receiver ground station, from which measurement is performed
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

_ContinuousScheduler__T = typing.TypeVar('_ContinuousScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ContinuousScheduler(AbstractScheduler[_ContinuousScheduler__T], typing.Generic[_ContinuousScheduler__T]):
    """
    Scheduler generating measurements sequences continuously.
    
    Continuous schedulers continuously generate measurements following a repetitive pattern. The repetitive pattern can be either a continuous stream of measurements separated by a constant step (for example one measurement every 60s), or several sequences of measurements at high rate up to a maximum number, with a rest period between sequences (for example sequences of up to 256 measurements every 100ms with 300s between each sequence).
    
    Since:
        9.3
    """
    @typing.overload
    def __init__(self, builder: MeasurementBuilder[_ContinuousScheduler__T], selector: typing.Union[org.orekit.time.DatesSelector, typing.Callable]): ...
    @typing.overload
    def __init__(self, builder: MeasurementBuilder[_ContinuousScheduler__T], selector: typing.Union[org.orekit.time.DatesSelector, typing.Callable], filter: typing.Union[java.util.function.Predicate[org.orekit.estimation.measurements.EstimatedMeasurementBase[_ContinuousScheduler__T]], typing.Callable[[org.orekit.estimation.measurements.EstimatedMeasurementBase[_ContinuousScheduler__T]], bool]]): ...
    def measurementIsFeasible(self, date: org.orekit.time.AbsoluteDate) -> bool:
        """
        Check if a measurement is feasible at some date.
        
        Specified by: measurementIsFeasible in class AbstractScheduler
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            true if measurement if feasible
        
        
        """
        ...

_EventBasedScheduler__T = typing.TypeVar('_EventBasedScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class EventBasedScheduler(AbstractScheduler[_EventBasedScheduler__T], typing.Generic[_EventBasedScheduler__T]):
    """
    Scheduler based on EventDetector for generating measurements sequences.
    
    Event-based schedulers generate measurements following a repetitive pattern when the a EventDetector provided at construction is in a SignSemantic state. It is important that the sign of the g function of the underlying event detector is not arbitrary, but has a semantic meaning, e.g. in or out, true or false. This class works well with event detectors that detect entry to or exit from a region, e.g. EclipseDetector, ElevationDetector, LatitudeCrossingDetector. Using this scheduler with detectors that are not based on entry to or exit from a region, e.g. DateDetector, LongitudeCrossingDetector, will likely lead to unexpected results.
    
    The repetitive pattern can be either a continuous stream of measurements separated by a constant step (for example one measurement every 60s), or several sequences of measurements at high rate up to a maximum number, with a rest period between sequences (for example sequences of up to 256 measurements every 100ms with 300s between each sequence).
    
    Since:
        9.3
    """
    @typing.overload
    def __init__(self, builder: MeasurementBuilder[_EventBasedScheduler__T], selector: typing.Union[org.orekit.time.DatesSelector, typing.Callable], filter: typing.Union[java.util.function.Predicate[org.orekit.estimation.measurements.EstimatedMeasurementBase[_EventBasedScheduler__T]], typing.Callable[[org.orekit.estimation.measurements.EstimatedMeasurementBase[_EventBasedScheduler__T]], bool]], propagator: org.orekit.propagation.Propagator, detector: org.orekit.propagation.events.EventDetector, signSemantic: SignSemantic): ...
    @typing.overload
    def __init__(self, builder: MeasurementBuilder[_EventBasedScheduler__T], selector: typing.Union[org.orekit.time.DatesSelector, typing.Callable], propagator: org.orekit.propagation.Propagator, detector: org.orekit.propagation.events.EventDetector, signSemantic: SignSemantic): ...
    def measurementIsFeasible(self, date: org.orekit.time.AbsoluteDate) -> bool:
        """
        Check if a measurement is feasible at some date.
        
        Specified by: measurementIsFeasible in class AbstractScheduler
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            true if measurement if feasible
        
        
        """
        ...

class FDOABuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.FDOA]):
    """
    Builder for FDOA measurements.
    
    Since:
        12.0
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, primeStation: org.orekit.estimation.measurements.GroundStation, secondStation: org.orekit.estimation.measurements.GroundStation, centreFrequency: float, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            primeStation (GroundStation): ground station that gives the date of the measurement
            secondStation (GroundStation): ground station that gives the measurement
            centreFrequency (double): satellite emitter frequency
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class InterSatellitesOneWayRangeRateBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.InterSatellitesOneWayRangeRate]):
    """
    Builder for InterSatellitesOneWayRangeRate measurements.
    
    Since:
        12.1
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, sigma: float, baseWeight: float):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): satellite which simply emits the signal
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
        
        
        """
        ...

class InterSatellitesPhaseBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    Builder for InterSatellitesPhase measurements.
    
    Since:
        10.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, wavelength: float, sigma: float, baseWeight: float, cache: org.orekit.estimation.measurements.gnss.AmbiguityCache):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): satellite which simply emits the signal
            wavelength (double): phase observed value wavelength (m)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            cache (AmbiguityCache): from which ambiguity drive should come
        
        Since:
            12.1
        
        
        """
        ...

class InterSatellitesRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    Builder for InterSatellitesRange measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, twoWay: bool, sigma: float, baseWeight: float):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): satellite which simply emits the signal in the one-way case, or reflects the signal in the two-way case
            twoWay (boolean): flag indicating whether it is a two-way measurement
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
        
        
        """
        ...

class OneWayGNSSPhaseBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    Builder for OneWayGNSSPhase measurements.
    
    Since:
        12.0
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, wavelength: float, sigma: float, baseWeight: float, cache: org.orekit.estimation.measurements.gnss.AmbiguityCache):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): satellite which simply emits the signal
            wavelength (double): phase observed value wavelength (m)
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            cache (AmbiguityCache): from which ambiguity drive should come
        
        Since:
            12.1
        
        
        """
        ...

class OneWayGNSSRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    Builder for OneWayGNSSRange measurements.
    
    Since:
        12.0
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, sigma: float, baseWeight: float):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): satellite which simply emits the signal
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
        
        
        """
        ...

class OneWayGNSSRangeRateBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.OneWayGNSSRangeRate]):
    """
    Builder for OneWayGNSSRangeRate measurements.
    
    Since:
        12.1
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, local: org.orekit.estimation.measurements.ObservableSatellite, remote: org.orekit.estimation.measurements.ObservableSatellite, sigma: float, baseWeight: float):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            local (ObservableSatellite): satellite which receives the signal and performs the measurement
            remote (ObservableSatellite): satellite which simply emits the signal
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
        
        
        """
        ...

class PVBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.PV]):
    """
    Builder for PV measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, sigmaPosition: float, sigmaVelocity: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            sigmaPosition (double): theoretical standard deviation on position components
            sigmaVelocity (double): theoretical standard deviation on velocity components
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class PositionBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.Position]):
    """
    Builder for Position measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

_PythonAbstractMeasurementBuilder__T = typing.TypeVar('_PythonAbstractMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractMeasurementBuilder(AbstractMeasurementBuilder[_PythonAbstractMeasurementBuilder__T], typing.Generic[_PythonAbstractMeasurementBuilder__T]):
    @typing.overload
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, sigma: float, baseWeight: float, *satellites: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, sigma: typing.Union[typing.List[float], jpype.JArray], baseWeight: typing.Union[typing.List[float], jpype.JArray], *satellites: org.orekit.estimation.measurements.ObservableSatellite): ...
    def buildObserved(self, date: org.orekit.time.AbsoluteDate, interpolators: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> _PythonAbstractMeasurementBuilder__T:
        """
        Build a dummy observed measurement.
        
        Specified by: buildObserved in class AbstractMeasurementBuilder
        
        Parameters:
            date (AbsoluteDate): measurement date
            interpolators (Map<ObservableSatellite, OrekitStepInterpolator> interpolators): interpolators relevant for this builder
        
        Returns:
            dummy observed measurement
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBaseWeight(self) -> typing.MutableSequence[float]:
        """
        Get the base weight associated with the measurement
        
        The base weight is used on residuals already normalized thanks to getTheoreticalStandardDeviation to increase or decrease relative effect of some measurements with respect to other measurements. It is a dimensionless value, typically between 0 and 1 (but it can really have any non-negative value).
        
        Overrides: getBaseWeight in class AbstractMeasurementBuilder
        
        Returns:
            base weight
        
        Also see:
            getTheoreticalStandardDeviation
        
        
        """
        ...
    def getEnd(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end of the measurements time span.
        
        Overrides: getEnd in class AbstractMeasurementBuilder
        
        Returns:
            end of the measurements time span
        
        
        """
        ...
    def getNoise(self) -> typing.MutableSequence[float]:
        """
        Generate a noise vector.
        
        Overrides: getNoise in class AbstractMeasurementBuilder
        
        Returns:
            noise vector (null if we generate perfect measurements)
        
        
        """
        ...
    def getSatellites(self) -> typing.MutableSequence[org.orekit.estimation.measurements.ObservableSatellite]:
        """
        Get the satellites related to this measurement.
        
        Specified by: getSatellites in interface MeasurementBuilder
        
        Overrides: getSatellites in class AbstractMeasurementBuilder
        
        Returns:
            satellites related to this measurement
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start of the measurements time span.
        
        Overrides: getStart in class AbstractMeasurementBuilder
        
        Returns:
            start of the measurements time span
        
        
        """
        ...
    def getTheoreticalStandardDeviation(self) -> typing.MutableSequence[float]:
        """
        Get the theoretical standard deviation.
        
        The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
        Overrides: getTheoreticalStandardDeviation in class AbstractMeasurementBuilder
        
        Returns:
            expected standard deviation
        
        Also see:
            getBaseWeight
        
        
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

_PythonAbstractScheduler__T = typing.TypeVar('_PythonAbstractScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractScheduler(AbstractScheduler[_PythonAbstractScheduler__T], typing.Generic[_PythonAbstractScheduler__T]):
    def __init__(self, builder: MeasurementBuilder[_PythonAbstractScheduler__T], selector: typing.Union[org.orekit.time.DatesSelector, typing.Callable], filter: typing.Union[java.util.function.Predicate[org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractScheduler__T]], typing.Callable[[org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractScheduler__T]], bool]]):
        """
        Simple constructor.
        
        Parameters:
            builder (MeasurementBuilder<PythonAbstractScheduler> builder): builder for individual measurements
            selector (DatesSelector): selector for dates
            filter (Predicate<EstimatedMeasurementBase<PythonAbstractScheduler>>): predicate for a posteriori filtering of generated measurements (measurements are accepted if the predicates evaluates to
                true)
        
        Since:
            13.0
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def measurementIsFeasible(self, date: org.orekit.time.AbsoluteDate) -> bool:
        """
        Description copied from class: measurementIsFeasible Check if a measurement is feasible at some date.
        
        Specified by: measurementIsFeasible in class AbstractScheduler
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            true if measurement if feasible
        
        
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

class RangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.Range]):
    """
    Builder for Range measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, station: org.orekit.estimation.measurements.GroundStation, twoWay: bool, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            station (GroundStation): ground station from which measurement is performed
            twoWay (boolean): flag indicating whether it is a two-way measurement
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class RangeRateBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.RangeRate]):
    """
    Builder for RangeRate measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, station: org.orekit.estimation.measurements.GroundStation, twoWay: bool, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            station (GroundStation): ground station from which measurement is performed
            twoWay (boolean): flag indicating whether it is a two-way measurement
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class TDOABuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.TDOA]):
    """
    Builder for TDOA measurements.
    
    Since:
        11.2
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, primeStation: org.orekit.estimation.measurements.GroundStation, secondStation: org.orekit.estimation.measurements.GroundStation, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            primeStation (GroundStation): ground station that gives the date of the measurement
            secondStation (GroundStation): ground station that gives the measurement
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...

class TurnAroundRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    Builder for TurnAroundRange measurements.
    
    Since:
        9.3
    """
    def __init__(self, noiseSource: org.hipparchus.random.CorrelatedRandomVectorGenerator, primaryStation: org.orekit.estimation.measurements.GroundStation, secondaryStation: org.orekit.estimation.measurements.GroundStation, sigma: float, baseWeight: float, satellite: org.orekit.estimation.measurements.ObservableSatellite):
        """
        Simple constructor.
        
        Parameters:
            noiseSource (CorrelatedRandomVectorGenerator): noise source, may be null for generating perfect measurements
            primaryStation (GroundStation): ground station from which measurement is performed
            secondaryStation (GroundStation): ground station reflecting the signal
            sigma (double): theoretical standard deviation
            baseWeight (double): base weight
            satellite (ObservableSatellite): satellite related to this builder
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.generation")``.

    AbstractMeasurementBuilder: typing.Type[AbstractMeasurementBuilder]
    AbstractScheduler: typing.Type[AbstractScheduler]
    AngularAzElBuilder: typing.Type[AngularAzElBuilder]
    AngularRaDecBuilder: typing.Type[AngularRaDecBuilder]
    BistaticRangeBuilder: typing.Type[BistaticRangeBuilder]
    BistaticRangeRateBuilder: typing.Type[BistaticRangeRateBuilder]
    ContinuousScheduler: typing.Type[ContinuousScheduler]
    EventBasedScheduler: typing.Type[EventBasedScheduler]
    FDOABuilder: typing.Type[FDOABuilder]
    GatheringSubscriber: typing.Type[GatheringSubscriber]
    GeneratedMeasurementSubscriber: typing.Type[GeneratedMeasurementSubscriber]
    Generator: typing.Type[Generator]
    InterSatellitesOneWayRangeRateBuilder: typing.Type[InterSatellitesOneWayRangeRateBuilder]
    InterSatellitesPhaseBuilder: typing.Type[InterSatellitesPhaseBuilder]
    InterSatellitesRangeBuilder: typing.Type[InterSatellitesRangeBuilder]
    MeasurementBuilder: typing.Type[MeasurementBuilder]
    MultiplexedMeasurementBuilder: typing.Type[MultiplexedMeasurementBuilder]
    OneWayGNSSPhaseBuilder: typing.Type[OneWayGNSSPhaseBuilder]
    OneWayGNSSRangeBuilder: typing.Type[OneWayGNSSRangeBuilder]
    OneWayGNSSRangeRateBuilder: typing.Type[OneWayGNSSRangeRateBuilder]
    PVBuilder: typing.Type[PVBuilder]
    PositionBuilder: typing.Type[PositionBuilder]
    PythonAbstractMeasurementBuilder: typing.Type[PythonAbstractMeasurementBuilder]
    PythonAbstractScheduler: typing.Type[PythonAbstractScheduler]
    PythonGeneratedMeasurementSubscriber: typing.Type[PythonGeneratedMeasurementSubscriber]
    PythonMeasurementBuilder: typing.Type[PythonMeasurementBuilder]
    PythonScheduler: typing.Type[PythonScheduler]
    RangeBuilder: typing.Type[RangeBuilder]
    RangeRateBuilder: typing.Type[RangeRateBuilder]
    Scheduler: typing.Type[Scheduler]
    SignSemantic: typing.Type[SignSemantic]
    TDOABuilder: typing.Type[TDOABuilder]
    TurnAroundRangeBuilder: typing.Type[TurnAroundRangeBuilder]
