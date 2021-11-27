import org.orekit.data
import org.orekit.frames
import org.orekit.models.earth
import org.orekit.time
import typing



class WeatherModel:
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class GlobalPressureTemperature2Model(WeatherModel):
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, double: float, double2: float, geoid: org.orekit.models.earth.Geoid): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, geoid: org.orekit.models.earth.Geoid): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, geoid: org.orekit.models.earth.Geoid, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    def getA(self) -> typing.List[float]: ...
    def getPressure(self) -> float: ...
    def getTemperature(self) -> float: ...
    def getWaterVaporPressure(self) -> float: ...
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class GlobalPressureTemperatureModel(WeatherModel):
    @typing.overload
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame, dataContext: org.orekit.data.DataContext): ...
    def getPressure(self) -> float: ...
    def getTemperature(self) -> float: ...
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class PythonWeatherModel(WeatherModel):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.weather")``.

    GlobalPressureTemperature2Model: typing.Type[GlobalPressureTemperature2Model]
    GlobalPressureTemperatureModel: typing.Type[GlobalPressureTemperatureModel]
    PythonWeatherModel: typing.Type[PythonWeatherModel]
    WeatherModel: typing.Type[WeatherModel]
