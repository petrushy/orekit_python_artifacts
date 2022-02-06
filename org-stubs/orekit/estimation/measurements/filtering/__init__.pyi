import org.orekit.estimation.measurements
import org.orekit.propagation
import typing



_MeasurementFilter__T = typing.TypeVar('_MeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class MeasurementFilter(typing.Generic[_MeasurementFilter__T]):
    """
    public interface MeasurementFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>>
    
        Interface for measurement pre-processing filter.
    
        Pre-processing filters are used to disabled measurements before they are used during an orbit determination process.
        Example of pre-processing filters are:
    
          - Minimum satellite elevation
          - Minimum value of the signal-to-noise ratio
          - Measurement residual
    
    
        Since:
            10.2
    """
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_MeasurementFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

_ElevationFilter__T = typing.TypeVar('_ElevationFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ElevationFilter(MeasurementFilter[_ElevationFilter__T], typing.Generic[_ElevationFilter__T]):
    """
    public class ElevationFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
        Elevation pre-processing filter.
    
        Since:
            10.2
    """
    def __init__(self, groundStation: org.orekit.estimation.measurements.GroundStation, double: float): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_ElevationFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

_PythonMeasurementFilter__T = typing.TypeVar('_PythonMeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonMeasurementFilter(MeasurementFilter[_PythonMeasurementFilter__T], typing.Generic[_PythonMeasurementFilter__T]):
    """
    public class PythonMeasurementFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
        Interface for measurement pre-processing filter.
    
        Pre-processing filters are used to disabled measurements before they are used during an orbit determination process.
        Example of pre-processing filters are:
    
          - Minimum satellite elevation
          - Minimum value of the signal-to-noise ratio
          - Measurement residual
    
    
        Since:
            10.2
    """
    def __init__(self): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_PythonMeasurementFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
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

_ResidualFilter__T = typing.TypeVar('_ResidualFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ResidualFilter(MeasurementFilter[_ResidualFilter__T], typing.Generic[_ResidualFilter__T]):
    """
    public class ResidualFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
        Residual pre-processing filter.
    
        The measurement residual is defined by the difference between the observed value and the estimated value of the
        measurement.
    
        Since:
            10.2
    """
    def __init__(self, double: float): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_ResidualFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.filtering")``.

    ElevationFilter: typing.Type[ElevationFilter]
    MeasurementFilter: typing.Type[MeasurementFilter]
    PythonMeasurementFilter: typing.Type[PythonMeasurementFilter]
    ResidualFilter: typing.Type[ResidualFilter]
