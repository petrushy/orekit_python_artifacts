import org.orekit.data
import org.orekit.frames
import org.orekit.models.earth
import org.orekit.time
import typing



class WeatherModel:
    """
    public interface WeatherModel
    
        Defines a surface meteorology model that can be used to compute the different weather parameters (pressure, temperature,
        ...).
    
        Since:
            9.3
    """
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Calculates the weather parameters of the model. In order to obtain the correct values of the parameters this method has
            to be call just after the construction of the model.
        
            Parameters:
                stationHeight (double): the height of the station in m
                currentDate (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...

class GlobalPressureTemperature2Model(WeatherModel):
    """
    public class GlobalPressureTemperature2Model extends Object implements :class:`~org.orekit.models.earth.weather.WeatherModel`
    
        The Global Pressure and Temperature 2 (GPT2) model. This model is an empirical model that provides the temperature, the
        pressure and the water vapor pressure of a site depending its latitude and longitude. This model also provides the a
        :sub:`h` and a :sub:`w` coefficients used for the :class:`~org.orekit.models.earth.troposphere.ViennaOneModel` model.
    
        The requisite coefficients for the computation of the weather parameters are provided by the Department of Geodesy and
        Geoinformation of the Vienna University. They are based on an external grid file like "gpt2_1.grd" (1Ã‚Â° x 1Ã‚Â°) or
        "gpt2_5.grd" (5Ã‚Â° x 5Ã‚Â°) available at: ` link <http://vmf.geo.tuwien.ac.at/codes/>`
    
        A bilinear interpolation is performed in order to obtained the correct values of the weather parameters.
    
        The format is always the same, with and example shown below for the pressure and the temperature.
    
        Example:
    
        .. code-block: java
        
        
         %  lat    lon   p:a0    A1   B1   A2   B2  T:a0    A1   B1   A2   B2
           87.5    2.5 101421    21  409 -217 -122 259.2 -13.2 -6.1  2.6  0.3
           87.5    7.5 101416    21  411 -213 -120 259.3 -13.1 -6.1  2.6  0.3
           87.5   12.5 101411    22  413 -209 -118 259.3 -13.1 -6.1  2.6  0.3
           87.5   17.5 101407    23  415 -205 -116 259.4 -13.0 -6.1  2.6  0.3
           ...
         
    
        Also see:
            "K. Lagler, M. Schindelegger, J. BÃƒÂ¶hm, H. Krasna, T. Nilsson (2013), GPT2: empirical slant delay model for radio
            space geodetic techniques. Geophys Res Lett 40(6):1069Ã¢â‚¬â€œ1073. doi:10.1002/grl.50288"
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_SUPPORTED_NAMES
    
        Default supported files name pattern.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, geoid: org.orekit.models.earth.Geoid): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, geoid: org.orekit.models.earth.Geoid): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, geoid: org.orekit.models.earth.Geoid, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    def getA(self) -> typing.List[float]:
        """
            Returns the a coefficients array.
        
              - double[0] = a :sub:`h`
              - double[1] = a :sub:`w`
        
        
            Returns:
                the a coefficients array
        
        
        """
        ...
    def getPressure(self) -> float:
        """
            Returns the pressure at the station [hPa].
        
            Returns:
                the pressure at the station [hPa]
        
        
        """
        ...
    def getTemperature(self) -> float:
        """
            Returns the temperature at the station [K].
        
            Returns:
                the temperature at the station [K]
        
        
        """
        ...
    def getWaterVaporPressure(self) -> float:
        """
            Returns the water vapor pressure at the station [hPa].
        
            Returns:
                the water vapor pressure at the station [hPa]
        
        
        """
        ...
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters`
            Calculates the weather parameters of the model. In order to obtain the correct values of the parameters this method has
            to be call just after the construction of the model.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters`Â in
                interfaceÂ :class:`~org.orekit.models.earth.weather.WeatherModel`
        
            Parameters:
                stationHeight (double): the height of the station in m
                currentDate (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...

class GlobalPressureTemperatureModel(WeatherModel):
    """
    public class GlobalPressureTemperatureModel extends Object implements :class:`~org.orekit.models.earth.weather.WeatherModel`
    
        The Global Pressure and Temperature model. This model is an empirical model that provides the temperature and the
        pressure depending the latitude and the longitude of the station.
    
        The Global Pressure and Temperature model is based on spherical harmonics up to degree and order of 9. The residual
        values Ã¢â‚¬â€¹Ã¢â‚¬â€¹of this model can reach 20 hPa for pressure and 10 Ã‚Â° C for temperature. They are significant
        for higher latitudes and small near the equator (BÃƒÂ¶hm, 2007)
    
        Also see:
            "J. BÃƒÂ¶hm, R. Heinkelmann, and H. Schuh (2007), Short Note: A global model of pressure and temperature for geodetic
            applications. J Geod, doi:10.1007/s00190-007-0135-3."
    """
    @typing.overload
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame, dataContext: org.orekit.data.DataContext): ...
    def getPressure(self) -> float:
        """
            Get the atmospheric pressure of the station depending its position.
        
            Returns:
                the pressure in hPa
        
        
        """
        ...
    def getTemperature(self) -> float:
        """
            Get the atmospheric temperature of the station depending its position.
        
            Returns:
                the temperature in kelvins
        
        
        """
        ...
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters`
            Calculates the weather parameters of the model. In order to obtain the correct values of the parameters this method has
            to be call just after the construction of the model.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters`Â in
                interfaceÂ :class:`~org.orekit.models.earth.weather.WeatherModel`
        
            Parameters:
                height (double): the height of the station in m
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...

class PythonWeatherModel(WeatherModel):
    """
    public class PythonWeatherModel extends Object implements :class:`~org.orekit.models.earth.weather.WeatherModel`
    """
    def __init__(self): ...
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
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Calculates the weather parameters of the model. In order to obtain the correct values of the parameters this method has
            to be call just after the construction of the model.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters`Â in
                interfaceÂ :class:`~org.orekit.models.earth.weather.WeatherModel`
        
            Parameters:
                stationHeight (double): the height of the station in m
                currentDate (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.weather")``.

    GlobalPressureTemperature2Model: typing.Type[GlobalPressureTemperature2Model]
    GlobalPressureTemperatureModel: typing.Type[GlobalPressureTemperatureModel]
    PythonWeatherModel: typing.Type[PythonWeatherModel]
    WeatherModel: typing.Type[WeatherModel]
