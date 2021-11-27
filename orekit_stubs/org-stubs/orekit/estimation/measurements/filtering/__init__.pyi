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
    public class ElevationFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
        Elevation pre-processing filter.
    
        Since:
            10.2
    """
    def __init__(self, groundStation: org.orekit.estimation.measurements.GroundStation, double: float): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_ElevationFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

_ResidualFilter__T = typing.TypeVar('_ResidualFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ResidualFilter(MeasurementFilter[_ResidualFilter__T], typing.Generic[_ResidualFilter__T]):
    """
    public class ResidualFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
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
    ResidualFilter: typing.Type[ResidualFilter]
