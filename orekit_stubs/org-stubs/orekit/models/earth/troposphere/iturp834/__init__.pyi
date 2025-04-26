
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
    public class ITURP834MappingFunction extends :class:`~org.orekit.models.earth.troposphere.iturp834.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
    
        ITU-R P.834 mapping function.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.models.earth.troposphere.iturp834.ITURP834PathDelay`,
            :class:`~org.orekit.models.earth.troposphere.iturp834.ITURP834WeatherParametersProvider`,
            :class:`~org.orekit.models.earth.troposphere.iturp834.https:.www.itu.int.rec.R`
    """
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
            Description copied from
            interface: :meth:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction.mappingFactors`
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.MutableSequence[_mappingFactors_1__T]:
        """
            Description copied from
            interface: :meth:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction.mappingFactors`
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class ITURP834PathDelay(org.orekit.models.earth.troposphere.TroposphericModel):
    """
    public class ITURP834PathDelay extends :class:`~org.orekit.models.earth.troposphere.iturp834.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        The ITU-R P.834 tropospheric model.
    
        This class implements the excess radio path length part of the model, i.e. section 6 of the recommendation. The ray
        bending part of the model, i.e. section 1 of the recommendation, is implemented in the
        :class:`~org.orekit.models.earth.ITURP834AtmosphericRefraction` class.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.models.earth.troposphere.iturp834.ITURP834WeatherParametersProvider`,
            :class:`~org.orekit.models.earth.troposphere.iturp834.ITURP834MappingFunction`,
            :class:`~org.orekit.models.earth.troposphere.iturp834.https:.www.itu.int.rec.R`
    """
    def __init__(self, pressureTemperatureHumidityProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, timeScale: org.orekit.time.TimeScale): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], tArray: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> org.orekit.models.earth.troposphere.FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.Union[typing.List[float], jpype.JArray], absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.models.earth.troposphere.TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class ITURP834WeatherParametersProvider(org.orekit.models.earth.weather.PressureTemperatureHumidityProvider):
    """
    public class ITURP834WeatherParametersProvider extends :class:`~org.orekit.models.earth.troposphere.iturp834.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider`
    
        Provider for the ITU-R P.834 weather parameters.
    
        This class implements the weather parameters part of the model, i.e. equations 27b to 27i in section 6 of the
        recommendation.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.models.earth.troposphere.iturp834.ITURP834PathDelay`,
            :class:`~org.orekit.models.earth.troposphere.iturp834.ITURP834MappingFunction`,
            :class:`~org.orekit.models.earth.troposphere.iturp834.https:.www.itu.int.rec.R`
    """
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    _getWeatherParameters_0__T = typing.TypeVar('_getWeatherParameters_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getWeatherParameters(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getWeatherParameters_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getWeatherParameters_0__T]) -> org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_getWeatherParameters_0__T]:
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
    def getWeatherParameters(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.models.earth.weather.PressureTemperatureHumidity:
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.troposphere.iturp834")``.

    ITURP834MappingFunction: typing.Type[ITURP834MappingFunction]
    ITURP834PathDelay: typing.Type[ITURP834PathDelay]
    ITURP834WeatherParametersProvider: typing.Type[ITURP834WeatherParametersProvider]
