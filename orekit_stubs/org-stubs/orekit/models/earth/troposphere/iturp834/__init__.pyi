
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.orekit.bodies
import org.orekit.models.earth.troposphere
import org.orekit.models.earth.weather
import org.orekit.time
import org.orekit.utils
import typing



class ITURP834MappingFunction(org.orekit.models.earth.troposphere.TroposphereMappingFunction):
    """
    ITU-R P.834 mapping function.
    
    Since:
        13.0
    
    Also see:
        ITURP834PathDelay,
        ITURP834WeatherParametersProvider,
        R
    """
    def __init__(self, utc: org.orekit.time.TimeScale):
        """
        Simple constructor.
        
        Parameters:
            utc (TimeScale): UTC time scale
        
        
        """
        ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Description copied from interface: mappingFactors This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
          - double[0] = m :sub:`h` (e) → hydrostatic mapping function
          - double[1] = m :sub:`w` (e) → wet mapping function
        
        Specified by: mappingFactors in interface TroposphereMappingFunction
        
        Parameters:
            trackingCoordinates (TrackingCoordinates): tracking coordinates of the satellite
            point (GeodeticPoint): station location
            date (AbsoluteDate): current date
        
        Returns:
            a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], point: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], date: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.MutableSequence[_mappingFactors_1__T]:
        """
        Description copied from interface: mappingFactors This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
          - T[0] = m :sub:`h` (e) → hydrostatic mapping function
          - T[1] = m :sub:`w` (e) → wet mapping function
        
        Specified by: mappingFactors in interface TroposphereMappingFunction
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class ITURP834PathDelay(org.orekit.models.earth.troposphere.TroposphericModel):
    """
    The ITU-R P.834 tropospheric model.
    
    This class implements the excess radio path length part of the model, i.e. section 6 of the recommendation. The ray bending part of the model, i.e. section 1 of the recommendation, is implemented in the ITURP834AtmosphericRefraction class.
    
    Since:
        13.0
    
    Also see:
        ITURP834WeatherParametersProvider,
        ITURP834MappingFunction,
        R
    """
    def __init__(self, pthProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, utc: org.orekit.time.TimeScale):
        """
        Simple constructor.
        
        Parameters:
            pthProvider (PressureTemperatureHumidityProvider): provider for pressure, temperature and humidity
            utc (TimeScale): UTC time scale
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> org.orekit.models.earth.troposphere.FieldTroposphericDelay[_pathDelay_0__T]:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        Specified by: pathDelay in interface TroposphericModel
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            parameters (T[]): tropospheric model parameters at current date
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> org.orekit.models.earth.troposphere.TroposphericDelay:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        Specified by: pathDelay in interface TroposphericModel
        
        Parameters:
            trackingCoordinates (TrackingCoordinates): tracking coordinates of the satellite
            point (GeodeticPoint): station location
            parameters (double[]): tropospheric model parameters
            date (AbsoluteDate): current date
        
        Returns:
            the path delay due to the troposphere
        
        """
        ...

class ITURP834WeatherParametersProvider(org.orekit.models.earth.weather.PressureTemperatureHumidityProvider):
    """
    Provider for the ITU-R P.834 weather parameters.
    
    This class implements the weather parameters part of the model, i.e. equations 27b to 27i in section 6 of the recommendation.
    
    Since:
        13.0
    
    Also see:
        ITURP834PathDelay,
        ITURP834MappingFunction,
        R
    """
    def __init__(self, utc: org.orekit.time.TimeScale):
        """
        Simple constructor.
        
        Parameters:
            utc (TimeScale): UTC time scale to evaluate time-dependent tables
        
        
        """
        ...
    _getWeatherParameters_0__T = typing.TypeVar('_getWeatherParameters_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParameters(self, location: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParameters_0__T], date: org.orekit.time.FieldAbsoluteDate[_getWeatherParameters_0__T]) -> org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_getWeatherParameters_0__T]:
        """
        Provide weather parameters.
        
        Specified by: getWeatherParameters in interface PressureTemperatureHumidityProvider
        
        Parameters:
            location (FieldGeodeticPoint<T> location): location at which parameters are requested
            date (FieldAbsoluteDate<T> date): date at which parameters are requested
        
        Returns:
            weather parameters
        
        
        """
        ...
    @typing.overload
    def getWeatherParameters(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> org.orekit.models.earth.weather.PressureTemperatureHumidity:
        """
        Provide weather parameters.
        
        Specified by: getWeatherParameters in interface PressureTemperatureHumidityProvider
        
        Parameters:
            location (GeodeticPoint): location at which parameters are requested
            date (AbsoluteDate): date at which parameters are requested
        
        Returns:
            weather parameters
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.troposphere.iturp834")``.

    ITURP834MappingFunction: typing.Type[ITURP834MappingFunction]
    ITURP834PathDelay: typing.Type[ITURP834PathDelay]
    ITURP834WeatherParametersProvider: typing.Type[ITURP834WeatherParametersProvider]
