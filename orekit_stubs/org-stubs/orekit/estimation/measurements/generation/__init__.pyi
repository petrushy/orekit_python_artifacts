import java.lang
import java.util
import java.util.function
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
    public interface GeneratedMeasurementSubscriber
    
        Interface for subscribing to generated :class:`~org.orekit.estimation.measurements.ObservedMeasurement` events.
    
        Since:
            12.0
    """
    def handleGeneratedMeasurement(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> None:
        """
            Handle a generated measurement.
        
            Parameters:
                measurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> measurement): measurements that has just been generated
        
        
        """
        ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize subscriber at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the subscriber to initialize
            some internal data if needed.
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

class Generator:
    """
    public class Generator extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
    def addSubscriber(self, generatedMeasurementSubscriber: GeneratedMeasurementSubscriber) -> None:
        """
            Add a subscriber.
        
            Parameters:
                subscriber (:class:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber`): to add
        
            Since:
                12.0
        
            Also see:
                :class:`~org.orekit.estimation.measurements.generation.GatheringSubscriber`
        
        
        """
        ...
    def generate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Generate measurements.
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...
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
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> _MeasurementBuilder__T: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_MeasurementBuilder__T]]: ...
    def getSatellites(self) -> typing.List[org.orekit.estimation.measurements.ObservableSatellite]:
        """
            Get the satellites related to this measurement.
        
            Returns:
                satellites related to this measurement
        
            Since:
                12.0
        
        
        """
        ...
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
    def generate(self, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> java.util.SortedSet[_Scheduler__T]: ...
    def getBuilder(self) -> MeasurementBuilder[_Scheduler__T]: ...
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
    public enum SignSemantic extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.estimation.measurements.generation.SignSemantic`>
    
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
                name (:class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
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
    public abstract class AbstractMeasurementBuilder<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`<T>
    
        Base class for :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`.
    
        Since:
            9.3
    """
    def addModifier(self, estimationModifier: org.orekit.estimation.measurements.EstimationModifier[_AbstractMeasurementBuilder__T]) -> None: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_AbstractMeasurementBuilder__T]]: ...
    def getSatellites(self) -> typing.List[org.orekit.estimation.measurements.ObservableSatellite]:
        """
            Get the satellites related to this measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.getSatellites` in
                interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Returns:
                satellites related to this measurement
        
        
        """
        ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize builder at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the builder to initialize some
            internal data if needed, typically setting up parameters reference dates.
        
            This implementation stores the time span of the measurements generation.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init` in
                interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

_AbstractScheduler__T = typing.TypeVar('_AbstractScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractScheduler(Scheduler[_AbstractScheduler__T], typing.Generic[_AbstractScheduler__T]):
    """
    public abstract class AbstractScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.generation.Scheduler`<T>
    
        Base implementation of :class:`~org.orekit.estimation.measurements.generation.Scheduler` managing
        :class:`~org.orekit.time.DatesSelector`.
    
        Since:
            9.3
    """
    def generate(self, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> java.util.SortedSet[_AbstractScheduler__T]: ...
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
                :meth:`~org.orekit.estimation.measurements.generation.Scheduler.init` in
                interface :class:`~org.orekit.estimation.measurements.generation.Scheduler`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

class GatheringSubscriber(GeneratedMeasurementSubscriber):
    """
    public class GatheringSubscriber extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber`
    
        Subscriber that gather all generated measurements in a sorted set.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def getGeneratedMeasurements(self) -> java.util.SortedSet[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]]: ...
    def handleGeneratedMeasurement(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> None:
        """
            Handle a generated measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber.handleGeneratedMeasurement` in
                interface :class:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber`
        
            Parameters:
                measurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> measurement): measurements that has just been generated
        
        
        """
        ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize subscriber at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the subscriber to initialize
            some internal data if needed.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber.init` in
                interface :class:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

class MultiplexedMeasurementBuilder(MeasurementBuilder[org.orekit.estimation.measurements.MultiplexedMeasurement]):
    """
    public class MultiplexedMeasurementBuilder extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`<:class:`~org.orekit.estimation.measurements.MultiplexedMeasurement`>
    
        Builder for :class:`~org.orekit.estimation.measurements.MultiplexedMeasurement` measurements.
    
        Since:
            12.0
    """
    def __init__(self, list: java.util.List[MeasurementBuilder[typing.Any]]): ...
    def addModifier(self, estimationModifier: org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.MultiplexedMeasurement]) -> None: ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.MultiplexedMeasurement: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.MultiplexedMeasurement]]: ...
    def getSatellites(self) -> typing.List[org.orekit.estimation.measurements.ObservableSatellite]:
        """
            Get the satellites related to this measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.getSatellites` in
                interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Returns:
                satellites related to this measurement
        
        
        """
        ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize builder at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the builder to initialize some
            internal data if needed, typically setting up parameters reference dates.
        
            This implementation stores the time span of the measurements generation.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init` in
                interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...

class PythonGeneratedMeasurementSubscriber(GeneratedMeasurementSubscriber):
    """
    public class PythonGeneratedMeasurementSubscriber extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def handleGeneratedMeasurement(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]) -> None:
        """
            Description copied from
            interface: :meth:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber.handleGeneratedMeasurement`
            Handle a generated measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber.handleGeneratedMeasurement` in
                interface :class:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber`
        
            Parameters:
                measurement (:class:`~org.orekit.estimation.measurements.ObservedMeasurement`<?> measurement): measurements that has just been generated
        
        
        """
        ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Description copied from
            interface: :meth:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber.init`
            Initialize subscriber at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the subscriber to initialize
            some internal data if needed.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber.init` in
                interface :class:`~org.orekit.estimation.measurements.generation.GeneratedMeasurementSubscriber`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

_PythonMeasurementBuilder__T = typing.TypeVar('_PythonMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonMeasurementBuilder(MeasurementBuilder[_PythonMeasurementBuilder__T], typing.Generic[_PythonMeasurementBuilder__T]):
    """
    public class PythonMeasurementBuilder<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`<T>
    """
    def __init__(self): ...
    def addModifier(self, estimationModifier: org.orekit.estimation.measurements.EstimationModifier[_PythonMeasurementBuilder__T]) -> None: ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> _PythonMeasurementBuilder__T: ...
    def finalize(self) -> None: ...
    def getModifiers(self) -> java.util.List[org.orekit.estimation.measurements.EstimationModifier[_PythonMeasurementBuilder__T]]: ...
    def getSatellites(self) -> typing.List[org.orekit.estimation.measurements.ObservableSatellite]:
        """
            Description copied from
            interface: :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.getSatellites`
            Get the satellites related to this measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.getSatellites` in
                interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Returns:
                satellites related to this measurement
        
        
        """
        ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize builder at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the builder to initialize some
            internal data if needed, typically setting up parameters reference dates.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init` in
                interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
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
    public class PythonScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.generation.Scheduler`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def generate(self, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> java.util.SortedSet[_PythonScheduler__T]: ...
    def getBuilder(self) -> MeasurementBuilder[_PythonScheduler__T]: ...
    def init(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize scheduler at the start of a measurements generation.
        
            This method is called once at the start of the measurements generation. It may be used by the scheduler to initialize
            some internal data if needed, typically :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.init`.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.Scheduler.init` in
                interface :class:`~org.orekit.estimation.measurements.generation.Scheduler`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start of the measurements time span
                end (:class:`~org.orekit.time.AbsoluteDate`): end of the measurements time span
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
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
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.AngularAzEl: ...

class AngularRaDecBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.AngularRaDec]):
    """
    public class AngularRaDecBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.AngularRaDec`>
    
        Builder for :class:`~org.orekit.estimation.measurements.AngularRaDec` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, frame: org.orekit.frames.Frame, doubleArray: typing.List[float], doubleArray2: typing.List[float], observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.AngularRaDec: ...

class BistaticRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.BistaticRange]):
    """
    public class BistaticRangeBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.BistaticRange`>
    
        Builder for :class:`~org.orekit.estimation.measurements.BistaticRange` measurements.
    
        Since:
            11.2
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, groundStation2: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.BistaticRange: ...

class BistaticRangeRateBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.BistaticRangeRate]):
    """
    public class BistaticRangeRateBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.BistaticRangeRate`>
    
        Builder for :class:`~org.orekit.estimation.measurements.BistaticRangeRate` measurements.
    
        Since:
            11.2
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, groundStation2: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.BistaticRangeRate: ...

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
    def measurementIsFeasible(self, absoluteDate: org.orekit.time.AbsoluteDate) -> bool:
        """
            Check if a measurement is feasible at some date.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractScheduler.measurementIsFeasible` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                true if measurement if feasible
        
        
        """
        ...

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
    def measurementIsFeasible(self, absoluteDate: org.orekit.time.AbsoluteDate) -> bool:
        """
            Check if a measurement is feasible at some date.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractScheduler.measurementIsFeasible` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                true if measurement if feasible
        
        
        """
        ...

class FDOABuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.FDOA]):
    """
    public class FDOABuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.FDOA`>
    
        Builder for :class:`~org.orekit.estimation.measurements.FDOA` measurements.
    
        Since:
            12.0
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, groundStation2: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.FDOA: ...

class InterSatellitesPhaseBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class InterSatellitesPhaseBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Builder for :class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase` measurements.
    
        Since:
            10.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, double: float, double2: float, double3: float): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.gnss.InterSatellitesPhase: ...

class InterSatellitesRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    public class InterSatellitesRangeBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        Builder for :class:`~org.orekit.estimation.measurements.InterSatellitesRange` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, boolean: bool, double: float, double2: float): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.InterSatellitesRange: ...

class OneWayGNSSPhaseBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    public class OneWayGNSSPhaseBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        Builder for :class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase` measurements.
    
        Since:
            12.0
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, toDoubleFunction: typing.Union[java.util.function.ToDoubleFunction[org.orekit.time.AbsoluteDate], typing.Callable[[org.orekit.time.AbsoluteDate], float]], double: float, double2: float, double3: float): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.gnss.OneWayGNSSPhase: ...

class OneWayGNSSRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    public class OneWayGNSSRangeBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange`>
    
        Builder for :class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange` measurements.
    
        Since:
            12.0
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite, observableSatellite2: org.orekit.estimation.measurements.ObservableSatellite, toDoubleFunction: typing.Union[java.util.function.ToDoubleFunction[org.orekit.time.AbsoluteDate], typing.Callable[[org.orekit.time.AbsoluteDate], float]], double: float, double2: float): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.gnss.OneWayGNSSRange: ...

class PVBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.PV]):
    """
    public class PVBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.PV`>
    
        Builder for :class:`~org.orekit.estimation.measurements.PV` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, double: float, double2: float, double3: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.PV: ...

class PositionBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.Position]):
    """
    public class PositionBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.Position`>
    
        Builder for :class:`~org.orekit.estimation.measurements.Position` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.Position: ...

_PythonAbstractMeasurementBuilder__T = typing.TypeVar('_PythonAbstractMeasurementBuilder__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractMeasurementBuilder(AbstractMeasurementBuilder[_PythonAbstractMeasurementBuilder__T], typing.Generic[_PythonAbstractMeasurementBuilder__T]):
    """
    public class PythonAbstractMeasurementBuilder<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<T>
    """
    @typing.overload
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, double: float, double2: float, *observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    @typing.overload
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, doubleArray: typing.List[float], doubleArray2: typing.List[float], *observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> _PythonAbstractMeasurementBuilder__T: ...
    def finalize(self) -> None: ...
    def getBaseWeight(self) -> typing.List[float]:
        """
            Get the base weight associated with the measurement
        
            The base weight is used on residuals already normalized thanks to
            :meth:`~org.orekit.estimation.measurements.generation.PythonAbstractMeasurementBuilder.getTheoreticalStandardDeviation`
            to increase or decrease relative effect of some measurements with respect to other measurements. It is a dimensionless
            value, typically between 0 and 1 (but it can really have any non-negative value).
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder.getBaseWeight` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`
        
            Returns:
                base weight
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.generation.PythonAbstractMeasurementBuilder.getTheoreticalStandardDeviation`
        
        
        """
        ...
    def getEnd(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end of the measurements time span.
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder.getEnd` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`
        
            Returns:
                end of the measurements time span
        
        
        """
        ...
    def getNoise(self) -> typing.List[float]:
        """
            Generate a noise vector.
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder.getNoise` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`
        
            Returns:
                noise vector (null if we generate perfect measurements)
        
        
        """
        ...
    def getSatellites(self) -> typing.List[org.orekit.estimation.measurements.ObservableSatellite]:
        """
            Get the satellites related to this measurement.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.MeasurementBuilder.getSatellites` in
                interface :class:`~org.orekit.estimation.measurements.generation.MeasurementBuilder`
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder.getSatellites` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`
        
            Returns:
                satellites related to this measurement
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start of the measurements time span.
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder.getStart` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`
        
            Returns:
                start of the measurements time span
        
        
        """
        ...
    def getTheoreticalStandardDeviation(self) -> typing.List[float]:
        """
            Get the theoretical standard deviation.
        
            The theoretical standard deviation is a theoretical value used for normalizing the residuals. It acts as a weighting
            factor to mix appropriately measurements with different units and different accuracy. The value has the same dimension
            as the measurement itself (i.e. when a residual is divided by this value, it becomes dimensionless).
        
            Overrides:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder.getTheoreticalStandardDeviation` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`
        
            Returns:
                expected standard deviation
        
            Also see:
                :meth:`~org.orekit.estimation.measurements.generation.PythonAbstractMeasurementBuilder.getBaseWeight`
        
        
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

_PythonAbstractScheduler__T = typing.TypeVar('_PythonAbstractScheduler__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractScheduler(AbstractScheduler[_PythonAbstractScheduler__T], typing.Generic[_PythonAbstractScheduler__T]):
    """
    public class PythonAbstractScheduler<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`<T>
    """
    def __init__(self, measurementBuilder: MeasurementBuilder[_PythonAbstractScheduler__T], datesSelector: org.orekit.time.DatesSelector): ...
    def finalize(self) -> None: ...
    def measurementIsFeasible(self, absoluteDate: org.orekit.time.AbsoluteDate) -> bool:
        """
            Description copied from
            class: :meth:`~org.orekit.estimation.measurements.generation.AbstractScheduler.measurementIsFeasible`
            Check if a measurement is feasible at some date.
        
            Specified by:
                :meth:`~org.orekit.estimation.measurements.generation.AbstractScheduler.measurementIsFeasible` in
                class :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
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
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.Range: ...

class RangeRateBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.RangeRate]):
    """
    public class RangeRateBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Builder for :class:`~org.orekit.estimation.measurements.RangeRate` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, boolean: bool, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.RangeRate: ...

class TDOABuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.TDOA]):
    """
    public class TDOABuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.TDOA`>
    
        Builder for :class:`~org.orekit.estimation.measurements.TDOA` measurements.
    
        Since:
            11.2
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, groundStation2: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.TDOA: ...

class TurnAroundRangeBuilder(AbstractMeasurementBuilder[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    public class TurnAroundRangeBuilder extends :class:`~org.orekit.estimation.measurements.generation.AbstractMeasurementBuilder`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
        Builder for :class:`~org.orekit.estimation.measurements.TurnAroundRange` measurements.
    
        Since:
            9.3
    """
    def __init__(self, correlatedRandomVectorGenerator: org.hipparchus.random.CorrelatedRandomVectorGenerator, groundStation: org.orekit.estimation.measurements.GroundStation, groundStation2: org.orekit.estimation.measurements.GroundStation, double: float, double2: float, observableSatellite: org.orekit.estimation.measurements.ObservableSatellite): ...
    def build(self, absoluteDate: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator], typing.Mapping[org.orekit.estimation.measurements.ObservableSatellite, org.orekit.propagation.sampling.OrekitStepInterpolator]]) -> org.orekit.estimation.measurements.TurnAroundRange: ...


class __module_protocol__(typing.Protocol):
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
    InterSatellitesPhaseBuilder: typing.Type[InterSatellitesPhaseBuilder]
    InterSatellitesRangeBuilder: typing.Type[InterSatellitesRangeBuilder]
    MeasurementBuilder: typing.Type[MeasurementBuilder]
    MultiplexedMeasurementBuilder: typing.Type[MultiplexedMeasurementBuilder]
    OneWayGNSSPhaseBuilder: typing.Type[OneWayGNSSPhaseBuilder]
    OneWayGNSSRangeBuilder: typing.Type[OneWayGNSSRangeBuilder]
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
