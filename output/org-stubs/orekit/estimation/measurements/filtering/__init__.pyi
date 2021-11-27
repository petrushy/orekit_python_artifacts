import org.orekit.estimation.measurements
import org.orekit.propagation
import typing



_MeasurementFilter__T = typing.TypeVar('_MeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class MeasurementFilter(typing.Generic[_MeasurementFilter__T]):
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_MeasurementFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

_ElevationFilter__T = typing.TypeVar('_ElevationFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ElevationFilter(MeasurementFilter[_ElevationFilter__T], typing.Generic[_ElevationFilter__T]):
    def __init__(self, groundStation: org.orekit.estimation.measurements.GroundStation, double: float): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_ElevationFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

_PythonMeasurementFilter__T = typing.TypeVar('_PythonMeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonMeasurementFilter(MeasurementFilter[_PythonMeasurementFilter__T], typing.Generic[_PythonMeasurementFilter__T]):
    def __init__(self): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_PythonMeasurementFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_ResidualFilter__T = typing.TypeVar('_ResidualFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ResidualFilter(MeasurementFilter[_ResidualFilter__T], typing.Generic[_ResidualFilter__T]):
    def __init__(self, double: float): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_ResidualFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.filtering")``.

    ElevationFilter: typing.Type[ElevationFilter]
    MeasurementFilter: typing.Type[MeasurementFilter]
    PythonMeasurementFilter: typing.Type[PythonMeasurementFilter]
    ResidualFilter: typing.Type[ResidualFilter]
