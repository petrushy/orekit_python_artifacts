import org.hipparchus
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.models.earth
import org.orekit.models.earth.troposphere
import org.orekit.models.earth.weather.class-use
import org.orekit.models.earth.weather.water
import org.orekit.time
import typing



class CellInterpolator:
    """
    public class CellInterpolator extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Interpolator within a grid cell.
    
        Since:
            12.1
    """
    ...

_FieldCellInterpolator__T = typing.TypeVar('_FieldCellInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCellInterpolator(typing.Generic[_FieldCellInterpolator__T]):
    """
    public class FieldCellInterpolator<T extends :class:`~org.orekit.models.earth.weather.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Interpolator within a grid cell.
    
        Since:
            12.1
    """
    ...

_FieldPressureTemperature__T = typing.TypeVar('_FieldPressureTemperature__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPressureTemperature(typing.Generic[_FieldPressureTemperature__T]):
    """
    public class FieldPressureTemperature<T extends :class:`~org.orekit.models.earth.weather.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for pressure and temperature.
    
        Since:
            12.1
    """
    @typing.overload
    def __init__(self, t: _FieldPressureTemperature__T, t2: _FieldPressureTemperature__T, t3: _FieldPressureTemperature__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldPressureTemperature__T], pressureTemperatureHumidity: 'PressureTemperatureHumidity'): ...
    def getAltitude(self) -> _FieldPressureTemperature__T:
        """
            Get altitude at which weather parameters have been computed.
        
            Returns:
                altitude at which weather parameters have been computed (m)
        
        
        """
        ...
    def getPressure(self) -> _FieldPressureTemperature__T:
        """
            Get pressure.
        
            Returns:
                pressure (Pa)
        
        
        """
        ...
    def getTemperature(self) -> _FieldPressureTemperature__T:
        """
            Get temperature.
        
            Returns:
                temperature (Kelvin)
        
        
        """
        ...

class GlobalPressureTemperature:
    """
    public class GlobalPressureTemperature extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        The Global Pressure and Temperature model. This model is an empirical model that provides the temperature and the
        pressure depending the latitude and the longitude of the station.
    
        The Global Pressure and Temperature model is based on spherical harmonics up to degree and order of 9. The residual
        values   of this model can reach 20 hPa for pressure and 10 ° C for temperature. They are significant for higher
        latitudes and small near the equator (Böhm, 2007)
    
        Since:
            12.1
    
        Also see:
            "J. Böhm, R. Heinkelmann, and H. Schuh (2007), Short Note: A global model of pressure and temperature for geodetic
            applications. J Geod, doi:10.1007/s00190-007-0135-3."
    """
    @typing.overload
    def __init__(self, geoid: org.orekit.models.earth.Geoid): ...
    @typing.overload
    def __init__(self, geoid: org.orekit.models.earth.Geoid, timeScale: org.orekit.time.TimeScale): ...
    def getWeatherParameters(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PressureTemperature':
        """
            Provide weather parameters.
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                weather parameters
        
        
        """
        ...

class HeightDependentPressureTemperatureHumidityConverter:
    """
    public class HeightDependentPressureTemperatureHumidityConverter extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Converter for weather parameters that change with height.
    
        Height variations correspond to equations 5.98, 5.99 and 5.100 from Guochang Xu, GPS - Theory, Algorithms and
        Applications, Springer, 2007
    
        Since:
            12.1
    """
    def __init__(self, waterVaporPressureProvider: org.orekit.models.earth.weather.water.WaterVaporPressureProvider): ...
    _convert_0__T = typing.TypeVar('_convert_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def convert(self, fieldPressureTemperatureHumidity: 'FieldPressureTemperatureHumidity'[_convert_0__T], t: _convert_0__T) -> 'FieldPressureTemperatureHumidity'[_convert_0__T]:
        """
            Convert weather parameters.
        
            Parameters:
                pth0 (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> pth0): weather at reference altitude
                h (T): altitude at which weather is requested
        
            Returns:
                converted weather
        
        
        """
        ...
    @typing.overload
    def convert(self, pressureTemperatureHumidity: 'PressureTemperatureHumidity', double: float) -> 'PressureTemperatureHumidity':
        """
            Convert weather parameters.
        
            Parameters:
                pth0 (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather at reference altitude
                h (double): altitude at which weather is requested
        
            Returns:
                converted weather
        
        """
        ...

class PressureTemperature:
    """
    public class PressureTemperature extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for pressure and temperature.
    
        Since:
            12.1
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getAltitude(self) -> float:
        """
            Get altitude at which weather parameters have been computed.
        
            Returns:
                altitude at which weather parameters have been computed (m)
        
        
        """
        ...
    def getPressure(self) -> float:
        """
            Get pressure.
        
            Returns:
                pressure (Pa)
        
        
        """
        ...
    def getTemperature(self) -> float:
        """
            Get temperature.
        
            Returns:
                temperature (Kelvin)
        
        
        """
        ...

class PressureTemperatureHumidityProvider:
    """
    public interface PressureTemperatureHumidityProvider
    
        Interface for providing weather parameters.
    
        Since:
            12.1
    """
    _getWeatherParamerers_0__T = typing.TypeVar('_getWeatherParamerers_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParamerers(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParamerers_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParamerers_0__T]) -> 'FieldPressureTemperatureHumidity'[_getWeatherParamerers_0__T]:
        """
            Provide weather parameters.
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                weather parameters
        
        
        """
        ...
    @typing.overload
    def getWeatherParamerers(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PressureTemperatureHumidity':
        """
            Provide weather parameters.
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                weather parameters
        
        """
        ...

class WeatherModel:
    """
    :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public interface WeatherModel
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        Defines a surface meteorology model that can be used to compute the different weather parameters (pressure, temperature,
        ...).
    
        Since:
            9.3
    """
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Deprecated.
            Calculates the weather parameters of the model. In order to obtain the correct values of the parameters this method has
            to be call just after the construction of the model.
        
            Parameters:
                stationHeight (double): the height of the station in m
                currentDate (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...

class AbstractGlobalPressureTemperature(org.orekit.models.earth.troposphere.ViennaAProvider, org.orekit.models.earth.troposphere.AzimuthalGradientProvider, PressureTemperatureHumidityProvider):
    """
    public class AbstractGlobalPressureTemperature extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.ViennaAProvider`, :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider`, :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
    
        Base class for Global Pressure and Temperature 2, 2w and 3 models. These models are empirical models that provide the
        temperature, the pressure and the water vapor pressure of a site depending its latitude and longitude. These models also
        :class:`~org.orekit.models.earth.troposphere.ViennaACoefficients` the a :sub:`h` and a :sub:`w` coefficients for Vienna
        models.
    
        The requisite coefficients for the computation of the weather parameters are provided by the Department of Geodesy and
        Geoinformation of the Vienna University. They are based on an external grid file like "gpt2_1.grd" (1° x 1°),
        "gpt2_5.grd" (5° x 5°), "gpt2_1w.grd" (1° x 1°), "gpt2_5w.grd" (5° x 5°), "gpt3_1.grd" (1° x 1°), or
        "gpt3_5.grd" (5° x 5°) available at: :class:`~org.orekit.models.earth.weather.https:.vmf.geo.tuwien.ac.at.codes`
    
        A bilinear interpolation is performed in order to obtained the correct values of the weather parameters.
    
        The format is always the same, with and example shown below for the pressure and the temperature. The "GPT2w" model (w
        stands for wet) also provide humidity parameters and the "GPT3" model also provides horizontal gradient, so the number
        of columns vary depending on the model.
    
        Example:
    
        .. code-block: java
        
         %  lat    lon   p:a0    A1   B1   A2   B2  T:a0    A1   B1   A2   B2
           87.5    2.5 101421    21  409 -217 -122 259.2 -13.2 -6.1  2.6  0.3
           87.5    7.5 101416    21  411 -213 -120 259.3 -13.1 -6.1  2.6  0.3
           87.5   12.5 101411    22  413 -209 -118 259.3 -13.1 -6.1  2.6  0.3
           87.5   17.5 101407    23  415 -205 -116 259.4 -13.0 -6.1  2.6  0.3
           ...
         
    
        Since:
            12.1
    
        Also see:
            "K. Lagler, M. Schindelegger, J. Böhm, H. Krasna, T. Nilsson (2013), GPT2: empirical slant delay model for radio space
            geodetic techniques. Geophys Res Lett 40(6):1069–1073. doi:10.1002/grl.50288"
    """
    _getA_0__T = typing.TypeVar('_getA_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getA_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getA_0__T]) -> org.orekit.models.earth.troposphere.FieldViennaACoefficients[_getA_0__T]:
        """
            Get coefficients array for VMF mapping function.
        
              - double[0] = a :sub:`h`
              - double[1] = a :sub:`w`
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.ViennaAProvider.getA` in
                interface :class:`~org.orekit.models.earth.troposphere.ViennaAProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                the coefficients array for VMF mapping function
        
        
        """
        ...
    @typing.overload
    def getA(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.models.earth.troposphere.ViennaACoefficients:
        """
            Get coefficients array for VMF mapping function.
        
              - double[0] = a :sub:`h`
              - double[1] = a :sub:`w`
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.ViennaAProvider.getA` in
                interface :class:`~org.orekit.models.earth.troposphere.ViennaAProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                the coefficients array for VMF mapping function
        
        """
        ...
    _getGradientCoefficients_1__T = typing.TypeVar('_getGradientCoefficients_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGradientCoefficients(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.models.earth.troposphere.AzimuthalGradientCoefficients:
        """
            Get azimuthal asymmetry gradients.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider.getGradientCoefficients` in
                interface :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                azimuthal asymmetry gradients or null if no gradients are available
        
        """
        ...
    @typing.overload
    def getGradientCoefficients(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getGradientCoefficients_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getGradientCoefficients_1__T]) -> org.orekit.models.earth.troposphere.FieldAzimuthalGradientCoefficients[_getGradientCoefficients_1__T]:
        """
            Get azimuthal asymmetry gradients.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider.getGradientCoefficients` in
                interface :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                azimuthal asymmetry gradients or null if no gradients are available
        
        
        """
        ...
    _getWeatherParamerers_0__T = typing.TypeVar('_getWeatherParamerers_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParamerers(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParamerers_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParamerers_0__T]) -> 'FieldPressureTemperatureHumidity'[_getWeatherParamerers_0__T]:
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParamerers` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                weather parameters
        
        
        """
        ...
    @typing.overload
    def getWeatherParamerers(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PressureTemperatureHumidity':
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParamerers` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                weather parameters
        
        """
        ...

class ConstantPressureTemperatureHumidityProvider(PressureTemperatureHumidityProvider):
    """
    public class ConstantPressureTemperatureHumidityProvider extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
    
        Provider for constant weather parameters.
    
        Since:
            12.1
    """
    def __init__(self, pressureTemperatureHumidity: 'PressureTemperatureHumidity'): ...
    _getWeatherParamerers_0__T = typing.TypeVar('_getWeatherParamerers_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParamerers(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParamerers_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParamerers_0__T]) -> 'FieldPressureTemperatureHumidity'[_getWeatherParamerers_0__T]:
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParamerers` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                weather parameters
        
        
        """
        ...
    @typing.overload
    def getWeatherParamerers(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PressureTemperatureHumidity':
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParamerers` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                weather parameters
        
        """
        ...

_FieldPressureTemperatureHumidity__T = typing.TypeVar('_FieldPressureTemperatureHumidity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPressureTemperatureHumidity(FieldPressureTemperature[_FieldPressureTemperatureHumidity__T], typing.Generic[_FieldPressureTemperatureHumidity__T]):
    """
    public class FieldPressureTemperatureHumidity<T extends :class:`~org.orekit.models.earth.weather.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.models.earth.weather.FieldPressureTemperature`<T>
    
        Container for pressure, temperature, and humidity.
    
        Since:
            12.1
    """
    @typing.overload
    def __init__(self, t: _FieldPressureTemperatureHumidity__T, t2: _FieldPressureTemperatureHumidity__T, t3: _FieldPressureTemperatureHumidity__T, t4: _FieldPressureTemperatureHumidity__T, t5: _FieldPressureTemperatureHumidity__T, t6: _FieldPressureTemperatureHumidity__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldPressureTemperatureHumidity__T], pressureTemperatureHumidity: 'PressureTemperatureHumidity'): ...
    def getLambda(self) -> _FieldPressureTemperatureHumidity__T:
        """
            Get water vapor decrease factor.
        
            Returns:
                water vapor decrease factor
        
        
        """
        ...
    def getTm(self) -> _FieldPressureTemperatureHumidity__T:
        """
            Get mean temperature weighted with water vapor pressure.
        
            Returns:
                mean temperature weighted with water vapor pressure
        
        
        """
        ...
    def getWaterVaporPressure(self) -> _FieldPressureTemperatureHumidity__T:
        """
            Get humidity as water vapor pressure.
        
            Returns:
                humidity as water vapor pressure (Pa)
        
        
        """
        ...

class GlobalPressureTemperatureModel(GlobalPressureTemperature, WeatherModel):
    """
    :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class GlobalPressureTemperatureModel extends :class:`~org.orekit.models.earth.weather.GlobalPressureTemperature` implements :class:`~org.orekit.models.earth.weather.WeatherModel`
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.weather.GlobalPressureTemperature`
        The Global Pressure and Temperature model. This model is an empirical model that provides the temperature and the
        pressure depending the latitude and the longitude of the station.
    
        The Global Pressure and Temperature model is based on spherical harmonics up to degree and order of 9. The residual
        values   of this model can reach 20 hPa for pressure and 10 ° C for temperature. They are significant for higher
        latitudes and small near the equator (Böhm, 2007)
    
        Also see:
            "J. Böhm, R. Heinkelmann, and H. Schuh (2007), Short Note: A global model of pressure and temperature for geodetic
            applications. J Geod, doi:10.1007/s00190-007-0135-3."
    """
    @typing.overload
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame, dataContext: org.orekit.data.DataContext): ...
    def getPressure(self) -> float:
        """
            Deprecated.
            Get the atmospheric pressure of the station depending its position.
        
            Returns:
                the pressure in hPa
        
        
        """
        ...
    def getTemperature(self) -> float:
        """
            Deprecated.
            Get the atmospheric temperature of the station depending its position.
        
            Returns:
                the temperature in kelvins
        
        
        """
        ...
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Deprecated.
            Description copied from interface: :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters`
            Calculates the weather parameters of the model. In order to obtain the correct values of the parameters this method has
            to be call just after the construction of the model.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters` in
                interface :class:`~org.orekit.models.earth.weather.WeatherModel`
        
            Parameters:
                height (double): the height of the station in m
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...

class PressureTemperatureHumidity(PressureTemperature):
    """
    public class PressureTemperatureHumidity extends :class:`~org.orekit.models.earth.weather.PressureTemperature`
    
        Container for pressure, temperature, and humidity.
    
        Since:
            12.1
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    def getLambda(self) -> float:
        """
            Get water vapor decrease factor.
        
            Returns:
                water vapor decrease factor
        
        
        """
        ...
    def getTm(self) -> float:
        """
            Get mean temperature weighted with water vapor pressure.
        
            Returns:
                mean temperature weighted with water vapor pressure
        
        
        """
        ...
    def getWaterVaporPressure(self) -> float:
        """
            Get humidity as water vapor pressure.
        
            Returns:
                humidity as water vapor pressure (Pa)
        
        
        """
        ...

class PythonPressureTemperatureHumidityProvider(PressureTemperatureHumidityProvider):
    """
    public class PythonPressureTemperatureHumidityProvider extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getWeatherParamerers_0__T = typing.TypeVar('_getWeatherParamerers_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParamerers(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParamerers_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParamerers_0__T]) -> FieldPressureTemperatureHumidity[_getWeatherParamerers_0__T]:
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParamerers` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                weather parameters
        
        
        """
        ...
    @typing.overload
    def getWeatherParamerers(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> PressureTemperatureHumidity:
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParamerers` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                weather parameters
        
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

class PythonWeatherModel(WeatherModel):
    """
    public class PythonWeatherModel extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.WeatherModel`
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
                :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters` in
                interface :class:`~org.orekit.models.earth.weather.WeatherModel`
        
            Parameters:
                stationHeight (double): the height of the station in m
                currentDate (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...

class GlobalPressureTemperature2(AbstractGlobalPressureTemperature):
    """
    public class GlobalPressureTemperature2 extends :class:`~org.orekit.models.earth.weather.AbstractGlobalPressureTemperature`
    
        The Global Pressure and Temperature 2 (GPT2) model.
    
        Since:
            12.1
    """
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScale: org.orekit.time.TimeScale): ...

class GlobalPressureTemperature2w(AbstractGlobalPressureTemperature):
    """
    public class GlobalPressureTemperature2w extends :class:`~org.orekit.models.earth.weather.AbstractGlobalPressureTemperature`
    
        The Global Pressure and Temperature 2w (GPT2w) model.
    
        This model adds humidity data to :class:`~org.orekit.models.earth.weather.GlobalPressureTemperature2`.
    
        Since:
            12.1
    """
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScale: org.orekit.time.TimeScale): ...

class GlobalPressureTemperature3(AbstractGlobalPressureTemperature):
    """
    public class GlobalPressureTemperature3 extends :class:`~org.orekit.models.earth.weather.AbstractGlobalPressureTemperature`
    
        The Global Pressure and Temperature 3 (GPT3) model.
    
        This model adds horizontal gradient data to :class:`~org.orekit.models.earth.weather.GlobalPressureTemperature2w`.
    
        Since:
            12.1
    """
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScale: org.orekit.time.TimeScale): ...

class GlobalPressureTemperature2Model(GlobalPressureTemperature2, WeatherModel):
    """
    :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class GlobalPressureTemperature2Model extends :class:`~org.orekit.models.earth.weather.GlobalPressureTemperature2` implements :class:`~org.orekit.models.earth.weather.WeatherModel`
    
        Deprecated.
        The Global Pressure and Temperature 2 (GPT2) model. This model is an empirical model that provides the temperature, the
        pressure and the water vapor pressure of a site depending its latitude and longitude. This model also provides the a
        :sub:`h` and a :sub:`w` coefficients used for the :class:`~org.orekit.models.earth.troposphere.ViennaOneModel` model.
    
        The requisite coefficients for the computation of the weather parameters are provided by the Department of Geodesy and
        Geoinformation of the Vienna University. They are based on an external grid file like "gpt2_1.grd" (1° x 1°) or
        "gpt2_5.grd" (5° x 5°) available at: ` link <http://vmf.geo.tuwien.ac.at/codes/>`
    
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
            "K. Lagler, M. Schindelegger, J. Böhm, H. Krasna, T. Nilsson (2013), GPT2: empirical slant delay model for radio space
            geodetic techniques. Geophys Res Lett 40(6):1069–1073. doi:10.1002/grl.50288"
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_SUPPORTED_NAMES
    
        Deprecated.
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
    _getA_1__T = typing.TypeVar('_getA_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self) -> typing.List[float]:
        """
            Deprecated.
            Returns the a coefficients array.
        
              - double[0] = a :sub:`h`
              - double[1] = a :sub:`w`
        
        
            Returns:
                the a coefficients array
        
        
        """
        ...
    @typing.overload
    def getA(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getA_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getA_1__T]) -> org.orekit.models.earth.troposphere.FieldViennaACoefficients[_getA_1__T]: ...
    @typing.overload
    def getA(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.models.earth.troposphere.ViennaACoefficients: ...
    def getPressure(self) -> float:
        """
            Deprecated.
            Returns the pressure at the station [hPa].
        
            Returns:
                the pressure at the station [hPa]
        
        
        """
        ...
    def getTemperature(self) -> float:
        """
            Deprecated.
            Returns the temperature at the station [K].
        
            Returns:
                the temperature at the station [K]
        
        
        """
        ...
    def getWaterVaporPressure(self) -> float:
        """
            Deprecated.
            Returns the water vapor pressure at the station [hPa].
        
            Returns:
                the water vapor pressure at the station [hPa]
        
        
        """
        ...
    def weatherParameters(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Deprecated.
            Description copied from interface: :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters`
            Calculates the weather parameters of the model. In order to obtain the correct values of the parameters this method has
            to be call just after the construction of the model.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.WeatherModel.weatherParameters` in
                interface :class:`~org.orekit.models.earth.weather.WeatherModel`
        
            Parameters:
                stationHeight (double): the height of the station in m
                currentDate (:class:`~org.orekit.time.AbsoluteDate`): current date
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.weather")``.

    AbstractGlobalPressureTemperature: typing.Type[AbstractGlobalPressureTemperature]
    CellInterpolator: typing.Type[CellInterpolator]
    ConstantPressureTemperatureHumidityProvider: typing.Type[ConstantPressureTemperatureHumidityProvider]
    FieldCellInterpolator: typing.Type[FieldCellInterpolator]
    FieldPressureTemperature: typing.Type[FieldPressureTemperature]
    FieldPressureTemperatureHumidity: typing.Type[FieldPressureTemperatureHumidity]
    GlobalPressureTemperature: typing.Type[GlobalPressureTemperature]
    GlobalPressureTemperature2: typing.Type[GlobalPressureTemperature2]
    GlobalPressureTemperature2Model: typing.Type[GlobalPressureTemperature2Model]
    GlobalPressureTemperature2w: typing.Type[GlobalPressureTemperature2w]
    GlobalPressureTemperature3: typing.Type[GlobalPressureTemperature3]
    GlobalPressureTemperatureModel: typing.Type[GlobalPressureTemperatureModel]
    HeightDependentPressureTemperatureHumidityConverter: typing.Type[HeightDependentPressureTemperatureHumidityConverter]
    PressureTemperature: typing.Type[PressureTemperature]
    PressureTemperatureHumidity: typing.Type[PressureTemperatureHumidity]
    PressureTemperatureHumidityProvider: typing.Type[PressureTemperatureHumidityProvider]
    PythonPressureTemperatureHumidityProvider: typing.Type[PythonPressureTemperatureHumidityProvider]
    PythonWeatherModel: typing.Type[PythonWeatherModel]
    WeatherModel: typing.Type[WeatherModel]
    class-use: org.orekit.models.earth.weather.class-use.__module_protocol__
    water: org.orekit.models.earth.weather.water.__module_protocol__
