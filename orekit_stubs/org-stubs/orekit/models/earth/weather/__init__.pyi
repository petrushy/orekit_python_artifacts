
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.hipparchus
import org.orekit.bodies
import org.orekit.data
import org.orekit.models.earth
import org.orekit.models.earth.troposphere
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
    def getProvider(self, pressureTemperatureHumidity: 'PressureTemperatureHumidity') -> 'PressureTemperatureHumidityProvider':
        """
            Generate a provider applying altitude dependency to fixed weather parameters.
        
            Parameters:
                basePTH (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): base weather parameters
        
            Returns:
                a provider that applies altitude dependency
        
            Since:
                13.0
        
        
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
    _getWeatherParameters_0__T = typing.TypeVar('_getWeatherParameters_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParameters(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParameters_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParameters_0__T]) -> 'FieldPressureTemperatureHumidity'[_getWeatherParameters_0__T]:
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
    def getWeatherParameters(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PressureTemperatureHumidity':
        """
            Provide weather parameters.
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                weather parameters
        
        """
        ...

class SeasonalModelType(java.lang.Enum['SeasonalModelType']):
    PRESSURE: typing.ClassVar['SeasonalModelType'] = ...
    TEMPERATURE: typing.ClassVar['SeasonalModelType'] = ...
    QV: typing.ClassVar['SeasonalModelType'] = ...
    DT: typing.ClassVar['SeasonalModelType'] = ...
    AH: typing.ClassVar['SeasonalModelType'] = ...
    AW: typing.ClassVar['SeasonalModelType'] = ...
    LAMBDA: typing.ClassVar['SeasonalModelType'] = ...
    TM: typing.ClassVar['SeasonalModelType'] = ...
    GN_H: typing.ClassVar['SeasonalModelType'] = ...
    GE_H: typing.ClassVar['SeasonalModelType'] = ...
    GN_W: typing.ClassVar['SeasonalModelType'] = ...
    GE_W: typing.ClassVar['SeasonalModelType'] = ...
    @staticmethod
    def parseType(string: str) -> 'SeasonalModelType': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SeasonalModelType': ...
    @staticmethod
    def values() -> typing.MutableSequence['SeasonalModelType']: ...

class AbstractGlobalPressureTemperature(org.orekit.models.earth.troposphere.ViennaAProvider, org.orekit.models.earth.troposphere.AzimuthalGradientProvider, PressureTemperatureHumidityProvider):
    """
    public abstract class AbstractGlobalPressureTemperature extends :class:`~org.orekit.models.earth.weather.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.ViennaAProvider`, :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider`, :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
    
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
    _getWeatherParameters_0__T = typing.TypeVar('_getWeatherParameters_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParameters(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParameters_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParameters_0__T]) -> 'FieldPressureTemperatureHumidity'[_getWeatherParameters_0__T]:
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParameters` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                weather parameters
        
        
        """
        ...
    @typing.overload
    def getWeatherParameters(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PressureTemperatureHumidity':
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParameters` in
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
    _getWeatherParameters_0__T = typing.TypeVar('_getWeatherParameters_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParameters(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParameters_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParameters_0__T]) -> 'FieldPressureTemperatureHumidity'[_getWeatherParameters_0__T]:
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParameters` in
                interface :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                weather parameters
        
        
        """
        ...
    @typing.overload
    def getWeatherParameters(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PressureTemperatureHumidity':
        """
            Provide weather parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider.getWeatherParameters` in
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
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getWeatherParameters_0__T = typing.TypeVar('_getWeatherParameters_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParameters(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParameters_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParameters_0__T]) -> FieldPressureTemperatureHumidity[_getWeatherParameters_0__T]: ...
    @typing.overload
    def getWeatherParameters(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> PressureTemperatureHumidity: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class GlobalPressureTemperature2(AbstractGlobalPressureTemperature):
    """
    public class GlobalPressureTemperature2 extends :class:`~org.orekit.models.earth.weather.AbstractGlobalPressureTemperature`
    
        The Global Pressure and Temperature 2 (GPT2) model.
    
        Since:
            12.1
    """
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScales: org.orekit.time.TimeScales): ...

class GlobalPressureTemperature2w(AbstractGlobalPressureTemperature):
    """
    public class GlobalPressureTemperature2w extends :class:`~org.orekit.models.earth.weather.AbstractGlobalPressureTemperature`
    
        The Global Pressure and Temperature 2w (GPT2w) model.
    
        This model adds humidity data to :class:`~org.orekit.models.earth.weather.GlobalPressureTemperature2`.
    
        Since:
            12.1
    """
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScales: org.orekit.time.TimeScales): ...

class GlobalPressureTemperature3(AbstractGlobalPressureTemperature):
    """
    public class GlobalPressureTemperature3 extends :class:`~org.orekit.models.earth.weather.AbstractGlobalPressureTemperature`
    
        The Global Pressure and Temperature 3 (GPT3) model.
    
        This model adds horizontal gradient data to :class:`~org.orekit.models.earth.weather.GlobalPressureTemperature2w`.
    
        Since:
            12.1
    """
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScale: org.orekit.time.TimeScale): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.weather")``.

    AbstractGlobalPressureTemperature: typing.Type[AbstractGlobalPressureTemperature]
    CellInterpolator: typing.Type[CellInterpolator]
    ConstantPressureTemperatureHumidityProvider: typing.Type[ConstantPressureTemperatureHumidityProvider]
    FieldCellInterpolator: typing.Type[FieldCellInterpolator]
    FieldPressureTemperature: typing.Type[FieldPressureTemperature]
    FieldPressureTemperatureHumidity: typing.Type[FieldPressureTemperatureHumidity]
    GlobalPressureTemperature: typing.Type[GlobalPressureTemperature]
    GlobalPressureTemperature2: typing.Type[GlobalPressureTemperature2]
    GlobalPressureTemperature2w: typing.Type[GlobalPressureTemperature2w]
    GlobalPressureTemperature3: typing.Type[GlobalPressureTemperature3]
    HeightDependentPressureTemperatureHumidityConverter: typing.Type[HeightDependentPressureTemperatureHumidityConverter]
    PressureTemperature: typing.Type[PressureTemperature]
    PressureTemperatureHumidity: typing.Type[PressureTemperatureHumidity]
    PressureTemperatureHumidityProvider: typing.Type[PressureTemperatureHumidityProvider]
    PythonPressureTemperatureHumidityProvider: typing.Type[PythonPressureTemperatureHumidityProvider]
    SeasonalModelType: typing.Type[SeasonalModelType]
    water: org.orekit.models.earth.weather.water.__module_protocol__
