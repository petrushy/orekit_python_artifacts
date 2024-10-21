import java.io
import java.lang
import java.util
import org.hipparchus
import org.orekit.bodies
import org.orekit.data
import org.orekit.models.earth.troposphere.class-use
import org.orekit.models.earth.weather
import org.orekit.models.earth.weather.water
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class AzimuthalGradientCoefficients:
    """
    public class AzimuthalGradientCoefficients extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for the azimuthal gradient coefficients gn :sub:`h` , ge :sub:`h` , gn :sub:`w` and ge :sub:`w` .
    
        Since:
            12.1
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    def getGeh(self) -> float:
        """
            Get East hydrostatic coefficient.
        
            Returns:
                East hydrostatic coefficient
        
        
        """
        ...
    def getGew(self) -> float:
        """
            Get East wet coefficient.
        
            Returns:
                East wet coefficient
        
        
        """
        ...
    def getGnh(self) -> float:
        """
            Get North hydrostatic coefficient.
        
            Returns:
                North hydrostatic coefficient
        
        
        """
        ...
    def getGnw(self) -> float:
        """
            Get North wet coefficient.
        
            Returns:
                North wet coefficient
        
        
        """
        ...

class AzimuthalGradientProvider:
    """
    public interface AzimuthalGradientProvider
    
        Provider for :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientCoefficients` and
        :class:`~org.orekit.models.earth.troposphere.FieldAzimuthalGradientCoefficients`.
    
        Since:
            12.1
    """
    _getGradientCoefficients_1__T = typing.TypeVar('_getGradientCoefficients_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGradientCoefficients(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> AzimuthalGradientCoefficients:
        """
            Get azimuthal asymmetry gradients.
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                azimuthal asymmetry gradients or null if no gradients are available
        
        """
        ...
    @typing.overload
    def getGradientCoefficients(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getGradientCoefficients_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getGradientCoefficients_1__T]) -> 'FieldAzimuthalGradientCoefficients'[_getGradientCoefficients_1__T]:
        """
            Get azimuthal asymmetry gradients.
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                azimuthal asymmetry gradients or null if no gradients are available
        
        
        """
        ...

class DiscreteTroposphericModel(org.orekit.utils.ParameterDriversProvider):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public interface DiscreteTroposphericModel extends :class:`~org.orekit.utils.ParameterDriversProvider`
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        Defines a tropospheric model, used to calculate the path delay imposed to electro-magnetic signals between an orbital
        satellite and a ground station.
    
        Models that implement this interface split the delay into hydrostatic and non-hydrostatic part:
    
        δ = δ :sub:`h` + δ :sub:`nh`
    
        With:
    
          - δ :sub:`h` = hydrostatic delay
          - δ :sub:`nh` = non-hydrostatic (or wet) delay
    """
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

_FieldAzimuthalGradientCoefficients__T = typing.TypeVar('_FieldAzimuthalGradientCoefficients__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAzimuthalGradientCoefficients(typing.Generic[_FieldAzimuthalGradientCoefficients__T]):
    """
    public class FieldAzimuthalGradientCoefficients<T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for the azimuthal gradient coefficients gn :sub:`h` , ge :sub:`h` , gn :sub:`w` and ge :sub:`w` .
    
        Since:
            12.1
    """
    def __init__(self, t: _FieldAzimuthalGradientCoefficients__T, t2: _FieldAzimuthalGradientCoefficients__T, t3: _FieldAzimuthalGradientCoefficients__T, t4: _FieldAzimuthalGradientCoefficients__T): ...
    def getGeh(self) -> _FieldAzimuthalGradientCoefficients__T:
        """
            Get East hydrostatic coefficient.
        
            Returns:
                East hydrostatic coefficient
        
        
        """
        ...
    def getGew(self) -> _FieldAzimuthalGradientCoefficients__T:
        """
            Get East wet coefficient.
        
            Returns:
                East wet coefficient
        
        
        """
        ...
    def getGnh(self) -> _FieldAzimuthalGradientCoefficients__T:
        """
            Get North hydrostatic coefficient.
        
            Returns:
                North hydrostatic coefficient
        
        
        """
        ...
    def getGnw(self) -> _FieldAzimuthalGradientCoefficients__T:
        """
            Get North wet coefficient.
        
            Returns:
                North wet coefficient
        
        
        """
        ...

_FieldTroposphericDelay__T = typing.TypeVar('_FieldTroposphericDelay__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTroposphericDelay(typing.Generic[_FieldTroposphericDelay__T]):
    """
    public class FieldTroposphericDelay<T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for tropospheric delay.
    
        Since:
            12.1
    """
    def __init__(self, t: _FieldTroposphericDelay__T, t2: _FieldTroposphericDelay__T, t3: _FieldTroposphericDelay__T, t4: _FieldTroposphericDelay__T): ...
    def getDelay(self) -> _FieldTroposphericDelay__T:
        """
            Get the total slanted delay (m).
        
            Returns:
                total slanted delay (m)
        
        
        """
        ...
    def getSh(self) -> _FieldTroposphericDelay__T:
        """
            Get slanted delay (m).
        
            Returns:
                slanted delay (m)
        
        
        """
        ...
    def getSw(self) -> _FieldTroposphericDelay__T:
        """
            Get wet slanted delay (m).
        
            Returns:
                wet slanted delay (m)
        
        
        """
        ...
    def getZh(self) -> _FieldTroposphericDelay__T:
        """
            Get hydrostatic zenith delay (m).
        
            Returns:
                hydrostatic zenith delay (m)
        
        
        """
        ...
    def getZw(self) -> _FieldTroposphericDelay__T:
        """
            Get wet zenith delay (m).
        
            Returns:
                wet zenith delay (m)
        
        
        """
        ...

_FieldViennaACoefficients__T = typing.TypeVar('_FieldViennaACoefficients__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldViennaACoefficients(typing.Generic[_FieldViennaACoefficients__T]):
    """
    public class FieldViennaACoefficients<T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for the :class:`~org.orekit.models.earth.troposphere.ViennaOne` and
        :class:`~org.orekit.models.earth.troposphere.ViennaThree` coefficients a :sub:`h` and a :sub:`w` .
    
        Since:
            12.1
    """
    def __init__(self, t: _FieldViennaACoefficients__T, t2: _FieldViennaACoefficients__T): ...
    def getAh(self) -> _FieldViennaACoefficients__T:
        """
            Get hydrostatic coefficient.
        
            Returns:
                hydrostatic coefficient
        
        
        """
        ...
    def getAw(self) -> _FieldViennaACoefficients__T:
        """
            Get wet coefficient.
        
            Returns:
                wet coefficient
        
        
        """
        ...

class MappingFunction:
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public interface MappingFunction
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
        Interface for mapping functions used in the tropospheric delay computation.
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class TroposphereMappingFunction:
    """
    public interface TroposphereMappingFunction
    
        Interface for mapping functions used in the tropospheric delay computation.
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class TroposphericDelay:
    """
    public class TroposphericDelay extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for tropospheric delay.
    
        Since:
            12.1
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    def getDelay(self) -> float:
        """
            Get the total slanted delay (m).
        
            Returns:
                total slanted delay (m)
        
        
        """
        ...
    def getSh(self) -> float:
        """
            Get slanted delay (m).
        
            Returns:
                slanted delay (m)
        
        
        """
        ...
    def getSw(self) -> float:
        """
            Get wet slanted delay (m).
        
            Returns:
                wet slanted delay (m)
        
        
        """
        ...
    def getZh(self) -> float:
        """
            Get hydrostatic zenith delay (m).
        
            Returns:
                hydrostatic zenith delay (m)
        
        
        """
        ...
    def getZw(self) -> float:
        """
            Get wet zenith delay (m).
        
            Returns:
                wet zenith delay (m)
        
        
        """
        ...

class TroposphericModel(org.orekit.utils.ParameterDriversProvider):
    """
    public interface TroposphericModel extends :class:`~org.orekit.utils.ParameterDriversProvider`
    
        Defines a tropospheric model, used to calculate the path delay imposed to electro-magnetic signals between an orbital
        satellite and a ground station.
    
        Since:
            12.1
    """
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class TroposphericModelUtils:
    """
    public class TroposphericModelUtils extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility class for tropospheric models.
    
        Since:
            11.0
    """
    NANO_M: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` NANO_M
    
        Nanometers unit.
    
        Since:
            12.1
    
    
    """
    MICRO_M: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` MICRO_M
    
        Micrometers unit.
    
        Since:
            12.1
    
    
    """
    HECTO_PASCAL: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` HECTO_PASCAL
    
        HectoPascal unit.
    
        Since:
            12.1
    
    
    """
    STANDARD_ATMOSPHERE: typing.ClassVar[org.orekit.models.earth.weather.PressureTemperatureHumidity] = ...
    """
    public static final :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity` STANDARD_ATMOSPHERE
    
        Standard atmosphere.
    
          - altitude: 0m
          - temperature: 20 degree Celsius
          - pressure: 1013.25 mbar
          - humidity: 50%
    
    
        Since:
            12.1
    
        Also see:
            :meth:`~org.orekit.models.earth.troposphere.TroposphericModelUtils.STANDARD_ATMOSPHERE_PROVIDER`
    
    
    """
    STANDARD_ATMOSPHERE_PROVIDER: typing.ClassVar[org.orekit.models.earth.weather.PressureTemperatureHumidityProvider] = ...
    """
    public static final :class:`~org.orekit.models.earth.weather.PressureTemperatureHumidityProvider` STANDARD_ATMOSPHERE_PROVIDER
    
        Provider for :meth:`~org.orekit.models.earth.troposphere.TroposphericModelUtils.STANDARD_ATMOSPHERE`.
    
        Since:
            12.1
    
    
    """
    _computeHeightCorrection_1__T = typing.TypeVar('_computeHeightCorrection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeHeightCorrection(double: float, double2: float) -> float:
        """
            This method computes the height correction for the hydrostatic component of the mapping function. The formulas are given
            by Neill's paper, 1996:
        
            Niell A. E. (1996) "Global mapping functions for the atmosphere delay of radio wavelengths,” J. Geophys. Res.,
            101(B2), pp. 3227–3246, doi: 10.1029/95JB03048.
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians.
                height (double): the height of the station in m above sea level.
        
            Returns:
                the height correction, in m
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeHeightCorrection(t: _computeHeightCorrection_1__T, t2: _computeHeightCorrection_1__T, field: org.hipparchus.Field[_computeHeightCorrection_1__T]) -> _computeHeightCorrection_1__T:
        """
            This method computes the height correction for the hydrostatic component of the mapping function. The formulas are given
            by Neill's paper, 1996:
        
            Niell A. E. (1996) "Global mapping functions for the atmosphere delay of radio wavelengths,” J. Geophys. Res.,
            101(B2), pp. 3227–3246, doi: 10.1029/95JB03048.
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians.
                height (T): the height of the station in m above sea level.
                field (:class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field to which the elements belong
        
            Returns:
                the height correction, in m
        
        
        """
        ...
    _mappingFunction_1__T = typing.TypeVar('_mappingFunction_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def mappingFunction(double: float, double2: float, double3: float, double4: float) -> float:
        """
            Compute the mapping function related to the coefficient values and the elevation.
        
            Parameters:
                a (double): a coefficient
                b (double): b coefficient
                c (double): c coefficient
                elevation (double): the elevation of the satellite, in radians.
        
            Returns:
                the value of the function at a given elevation
        
        """
        ...
    @typing.overload
    @staticmethod
    def mappingFunction(t: _mappingFunction_1__T, t2: _mappingFunction_1__T, t3: _mappingFunction_1__T, t4: _mappingFunction_1__T) -> _mappingFunction_1__T:
        """
            Compute the mapping function related to the coefficient values and the elevation.
        
            Parameters:
                a (T): a coefficient
                b (T): b coefficient
                c (T): c coefficient
                elevation (T): the elevation of the satellite, in radians.
        
            Returns:
                the value of the function at a given elevation
        
        
        """
        ...

class ViennaACoefficients:
    """
    public class ViennaACoefficients extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for the :class:`~org.orekit.models.earth.troposphere.ViennaOne` and
        :class:`~org.orekit.models.earth.troposphere.ViennaThree` coefficients a :sub:`h` and a :sub:`w` .
    
        Since:
            12.1
    """
    def __init__(self, double: float, double2: float): ...
    def getAh(self) -> float:
        """
            Get hydrostatic coefficient.
        
            Returns:
                hydrostatic coefficient
        
        
        """
        ...
    def getAw(self) -> float:
        """
            Get wet coefficient.
        
            Returns:
                wet coefficient
        
        
        """
        ...

class ViennaAProvider:
    """
    public interface ViennaAProvider
    
        Provider for :class:`~org.orekit.models.earth.troposphere.ViennaOne` and
        :class:`~org.orekit.models.earth.troposphere.ViennaThree` coefficients a :sub:`h` and a :sub:`w` .
    
        Since:
            12.1
    """
    _getA_0__T = typing.TypeVar('_getA_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getA_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getA_0__T]) -> FieldViennaACoefficients[_getA_0__T]:
        """
            Get coefficients array for VMF mapping function.
        
              - double[0] = a :sub:`h`
              - double[1] = a :sub:`w`
        
        
            Parameters:
                location (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> location): location at which parameters are requested
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which parameters are requested
        
            Returns:
                the coefficients array for VMF mapping function
        
        
        """
        ...
    @typing.overload
    def getA(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> ViennaACoefficients:
        """
            Get coefficients array for VMF mapping function.
        
              - double[0] = a :sub:`h`
              - double[1] = a :sub:`w`
        
        
            Parameters:
                location (:class:`~org.orekit.bodies.GeodeticPoint`): location at which parameters are requested
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which parameters are requested
        
            Returns:
                the coefficients array for VMF mapping function
        
        """
        ...

class ViennaModelCoefficientsLoader(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader):
    """
    public class ViennaModelCoefficientsLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.data.DataLoader`
    
        Loads Vienna tropospheric coefficients a given input stream. A stream contains, for a given day and a given hour, the
        hydrostatic and wet zenith delays and the ah and aw coefficients used for the computation of the mapping function. The
        coefficients are given with a time interval of 6 hours.
    
        A bilinear interpolation is performed the case of the user initialize the latitude and the longitude with values that
        are not contained in the stream.
    
        The coefficients are obtained from `Vienna Mapping Functions Open Access Data
        <http://vmf.geo.tuwien.ac.at/trop_products/GRID/>`. Find more on the files at the `VMF Model Documentation
        <http://vmf.geo.tuwien.ac.at/readme.txt>`.
    
        The files have to be extracted to UTF-8 text files before being read by this loader.
    
        After extraction, it is assumed they are named VMFG_YYYYMMDD.Hhh for
        :class:`~org.orekit.models.earth.troposphere.ViennaOneModel` and VMF3_YYYYMMDD.Hhh
        :class:`~org.orekit.models.earth.troposphere.ViennaThreeModel`. Where YYYY is the 4-digits year, MM the month, DD the
        day and hh the 2-digits hour.
    
        The format is always the same, with and example shown below for VMF1 model.
    
        Example:
    
        .. code-block: java
        
         ! Version:            1.0
         ! Source:             J. Boehm, TU Vienna (created: 2018-11-20)
         ! Data_types:         VMF1 (lat lon ah aw zhd zwd)
         ! Epoch:              2018 11 19 18 00  0.0
         ! Scale_factor:       1.e+00
         ! Range/resolution:   -90 90 0 360 2 2.5
         ! Comment:            http://vmf.geo.tuwien.ac.at/trop_products/GRID/2.5x2/VMF1/VMF1_OP/
          90.0   0.0 0.00116059  0.00055318  2.3043  0.0096
          90.0   2.5 0.00116059  0.00055318  2.3043  0.0096
          90.0   5.0 0.00116059  0.00055318  2.3043  0.0096
          90.0   7.5 0.00116059  0.00055318  2.3043  0.0096
          90.0  10.0 0.00116059  0.00055318  2.3043  0.0096
          90.0  12.5 0.00116059  0.00055318  2.3043  0.0096
          90.0  15.0 0.00116059  0.00055318  2.3043  0.0096
          90.0  17.5 0.00116059  0.00055318  2.3043  0.0096
          90.0  20.0 0.00116059  0.00055318  2.3043  0.0096
          90.0  22.5 0.00116059  0.00055318  2.3043  0.0096
          90.0  25.0 0.00116059  0.00055318  2.3043  0.0096
          90.0  27.5 0.00116059  0.00055318  2.3043  0.0096
         
    
        It is not safe for multiple threads to share a single instance of this class.
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_SUPPORTED_NAMES
    
        Default supported files name pattern.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, viennaModelType: 'ViennaModelType'): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, viennaModelType: 'ViennaModelType'): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, viennaModelType: 'ViennaModelType', dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getA(self) -> typing.List[float]:
        """
            Returns the a coefficients array.
        
              - double[0] = a :sub:`h`
              - double[1] = a :sub:`w`
        
        
            Returns:
                the a coefficients array
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
            Description copied from class: :meth:`~org.orekit.data.AbstractSelfFeedingLoader.getSupportedNames`
            Get the supported names regular expression.
        
            Overrides:
                :meth:`~org.orekit.data.AbstractSelfFeedingLoader.getSupportedNames` in
                class :class:`~org.orekit.data.AbstractSelfFeedingLoader`
        
            Returns:
                the supported names.
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.feed`
        
        
        """
        ...
    def getZenithDelay(self) -> typing.List[float]:
        """
            Returns the zenith delay array.
        
              - double[0] = D :sub:`hz` → zenith hydrostatic delay
              - double[1] = D :sub:`wz` → zenith wet delay
        
        
            Returns:
                the zenith delay array
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    @typing.overload
    def loadViennaCoefficients(self) -> None:
        """
            Load the data using supported names .
        """
        ...
    @typing.overload
    def loadViennaCoefficients(self, dateTimeComponents: org.orekit.time.DateTimeComponents) -> None:
        """
            Load the data for a given day.
        
            Parameters:
                dateTimeComponents (:class:`~org.orekit.time.DateTimeComponents`): date and time component.
        
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataLoader.stillAcceptsData`
            Check if the loader still accepts new data.
        
            This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the
            data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or
            Earth Orientation Parameters that are split among several files), this method should always return true to make sure no
            data is left over.
        
            Specified by:
                :meth:`~org.orekit.data.DataLoader.stillAcceptsData` in interface :class:`~org.orekit.data.DataLoader`
        
            Returns:
                true while the loader still accepts new data
        
        
        """
        ...

class ViennaModelType(java.lang.Enum['ViennaModelType']):
    """
    public enum ViennaModelType extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.models.earth.troposphere.ViennaModelType`>
    
        Enumerate for Vienna tropospheric model 1 and 3. This enumerate is used for the coefficients loader.
    
        Also see:
            :class:`~org.orekit.models.earth.troposphere.ViennaOneModel`,
            :class:`~org.orekit.models.earth.troposphere.ViennaThreeModel`
    """
    VIENNA_ONE: typing.ClassVar['ViennaModelType'] = ...
    VIENNA_THREE: typing.ClassVar['ViennaModelType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ViennaModelType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['ViennaModelType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ViennaModelType c : ViennaModelType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AbstractChaoMappingFunction(TroposphereMappingFunction):
    """
    public class AbstractChaoMappingFunction extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
    
        Chao mapping function for radio wavelengths.
    
        Since:
            12.1
    
        Also see:
            "C. C. Chao, A model for tropospheric calibration from delay surface and radiosonde ballon measurements, 1972"
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
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
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
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
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class AbstractVienna(TroposphericModel, TroposphereMappingFunction):
    """
    public abstract class AbstractVienna extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`, :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
    
        The Vienna tropospheric delay model for radio techniques.
    
        Since:
            12.1
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class AskneNordiusModel(TroposphericModel):
    """
    public class AskneNordiusModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        The Askne Nordius model.
    
        The hydrostatic part is equivalent to Saastamoinen, whereas the wet part takes into account
        :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidity.getTm` and
        :meth:`~org.orekit.models.earth.weather.PressureTemperatureHumidity.getLambda`.
    
        Since:
            12.1
    
        Also see:
            "J. Askne and H. Nordius, Estimation of tropospheric delay for microwaves from surface weather data, Radio Science,
            volume 22, number 3, pages 379-386, May-June 1987", "Landskron D (2017) Modeling tropospheric delays for space geodetic
            techniques. Dissertation, Department of Geodesy and Geoinformation, TU Wien, Supervisor: J. Böhm.
            http://repositum.tuwien.ac.at/urn:nbn:at:at-ubtuw:1-100249"
    """
    LOW_ELEVATION_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double LOW_ELEVATION_THRESHOLD
    
        Lowest acceptable elevation angle [rad].
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, troposphereMappingFunction: TroposphereMappingFunction): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class CanonicalSaastamoinenModel(TroposphericModel):
    """
    public class CanonicalSaastamoinenModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        The canonical Saastamoinen model.
    
        Estimates the path delay imposed to electro-magnetic signals by the troposphere according to the formula: \[ \delta =
        \frac{0.002277}{\cos z (1 - 0.00266\cos 2\varphi - 0.00028 h})} \left[P+(\frac{1255}{T}+0.005)e - B(h) \tan^2 z\right]
        \] with the following input data provided to the model:
    
          - z: zenith angle
          - P: atmospheric pressure
          - T: temperature
          - e: partial pressure of water vapor
    
    
        Since:
            12.1
    
        Also see:
            "J Saastamoinen, Atmospheric Correction for the Troposphere and Stratosphere in Radio Ranging of Satellites"
    """
    DEFAULT_LOW_ELEVATION_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_LOW_ELEVATION_THRESHOLD
    
        Default lowest acceptable elevation angle [rad].
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def getLowElevationThreshold(self) -> float:
        """
            Get the low elevation threshold value for path delay computation.
        
            Returns:
                low elevation threshold, in rad.
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.pathDelay`,
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.pathDelay`
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.setLowElevationThreshold`
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.setLowElevationThreshold`
        
        """
        ...
    def setLowElevationThreshold(self, double: float) -> None:
        """
            Set the low elevation threshold value for path delay computation.
        
            Parameters:
                lowElevationThreshold (double): The new value for the threshold [rad]
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.pathDelay`,
                :meth:`~org.orekit.models.earth.troposphere.CanonicalSaastamoinenModel.pathDelay`
        
        
        """
        ...

class ConstantAzimuthalGradientProvider(AzimuthalGradientProvider):
    """
    public class ConstantAzimuthalGradientProvider extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider`
    
        Constant provider for :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientCoefficients` and
        :class:`~org.orekit.models.earth.troposphere.FieldAzimuthalGradientCoefficients`.
    
        Since:
            12.1
    """
    def __init__(self, azimuthalGradientCoefficients: AzimuthalGradientCoefficients): ...
    _getGradientCoefficients_1__T = typing.TypeVar('_getGradientCoefficients_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGradientCoefficients(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> AzimuthalGradientCoefficients:
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
    def getGradientCoefficients(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getGradientCoefficients_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getGradientCoefficients_1__T]) -> FieldAzimuthalGradientCoefficients[_getGradientCoefficients_1__T]:
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

class ConstantTroposphericModel(TroposphericModel):
    """
    public class ConstantTroposphericModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        Defines a constant tropospheric model.
    
        Since:
            12.1
    """
    def __init__(self, troposphericDelay: TroposphericDelay): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class ConstantViennaAProvider(ViennaAProvider):
    """
    public class ConstantViennaAProvider extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.ViennaAProvider`
    
        Provider for constant Vienna A coefficients.
    
        Since:
            12.1
    """
    def __init__(self, viennaACoefficients: ViennaACoefficients): ...
    _getA_0__T = typing.TypeVar('_getA_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getA_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getA_0__T]) -> FieldViennaACoefficients[_getA_0__T]:
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
    def getA(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> ViennaACoefficients:
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

class DummyMappingFunction(TroposphereMappingFunction):
    """
    public class DummyMappingFunction extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
    
        Dummy mapping function.
    
        This mapping function just uses 1.0 as constant mapping factors, which implies the slanted tropospheric delays are equal
        to the zenith delays. This is mainly useful when only zenith delays are needed.
    
        Since:
            12.1
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
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
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
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
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class EstimatedModel(TroposphericModel):
    """
    public class EstimatedModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        An estimated tropospheric model. The tropospheric delay is computed according to the formula:
    
        δ = δ :sub:`h` * m :sub:`h` + (δ :sub:`t` - δ :sub:`h` ) * m :sub:`w`
    
        With:
    
          - δ :sub:`h` : Tropospheric zenith hydro-static delay.
          - δ :sub:`t` : Tropospheric total zenith delay.
          - m :sub:`h` : Hydro-static mapping function.
          - m :sub:`w` : Wet mapping function.
    
    
        The mapping functions m :sub:`h` (e) and m :sub:`w` (e) are computed thanks to a :code:`model` initialized by the user.
        The user has the possibility to use several mapping function models for the computations: the
        :class:`~org.orekit.models.earth.troposphere.GlobalMappingFunctionModel`, or the
        :class:`~org.orekit.models.earth.troposphere.NiellMappingFunctionModel`
    
        The tropospheric zenith delay δ :sub:`h` is computed empirically with a
        :class:`~org.orekit.models.earth.troposphere.TroposphericModel` while the tropospheric total zenith delay δ :sub:`t` is
        estimated as a :class:`~org.orekit.utils.ParameterDriver`, hence the wet part is the difference between the two.
    
        Since:
            12.1
    """
    TOTAL_ZENITH_DELAY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TOTAL_ZENITH_DELAY
    
        Name of the parameter of this model: the total zenith delay.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, troposphereMappingFunction: TroposphereMappingFunction, double4: float): ...
    @typing.overload
    def __init__(self, troposphereMappingFunction: TroposphereMappingFunction, double: float): ...
    @typing.overload
    def __init__(self, troposphericModel: TroposphericModel, troposphereMappingFunction: TroposphereMappingFunction, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class FixedTroposphericDelay(DiscreteTroposphericModel, TroposphericModel):
    """
    public class FixedTroposphericDelay extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`, :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        A static tropospheric model that interpolates the actual tropospheric delay based on values read from a configuration
        file (tropospheric-delay.txt) via the :class:`~org.orekit.data.DataProvidersManager`.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    @staticmethod
    def getDefaultModel() -> 'FixedTroposphericDelay': ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            All delays are affected to :meth:`~org.orekit.models.earth.troposphere.TroposphericDelay.getZh` and
            :meth:`~org.orekit.models.earth.troposphere.TroposphericDelay.getSh` delays, the wet delays are arbitrarily set to 0.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public <T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T pathDelay (T elevation, :class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point, T[] parameters, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            All delays are affected to :meth:`~org.orekit.models.earth.troposphere.FieldTroposphericDelay.getZh` and
            :meth:`~org.orekit.models.earth.troposphere.FieldTroposphericDelay.getSh` delays, the wet delays are arbitrarily set to
            0.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...

class GlobalMappingFunctionModel(MappingFunction, TroposphereMappingFunction):
    """
    public class GlobalMappingFunctionModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.MappingFunction`, :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
    
        The Global Mapping Function model for radio techniques. This model is an empirical mapping function. It only needs the
        values of the station latitude, longitude, height and the date for the computations.
    
        The Global Mapping Function is based on spherical harmonics up to degree and order of 9. It was developed to be
        consistent with the :class:`~org.orekit.models.earth.troposphere.ViennaOneModel` mapping function model.
    
        Also see:
            "Boehm, J., A.E. Niell, P. Tregoning, H. Schuh (2006), Global Mapping Functions (GMF): A new empirical mapping function
            based on numerical weather model data, Geoph. Res. Letters, Vol. 33, L07304, doi:10.1029/2005GL025545.", "Petit, G. and
            Luzum, B. (eds.), IERS Conventions (2010), IERS Technical Note No. 36, BKG (2010)"
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    _mappingFactors_2__T = typing.TypeVar('_mappingFactors_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _mappingFactors_3__T = typing.TypeVar('_mappingFactors_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
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
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public <T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T[] mappingFactors (T elevation, :class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_2__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_2__T]) -> typing.List[_mappingFactors_2__T]: ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_3__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_3__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_3__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_3__T]) -> typing.List[_mappingFactors_3__T]:
        """
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
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class MariniMurray(TroposphericModel):
    """
    public class MariniMurray extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        The Marini-Murray tropospheric delay model for laser ranging.
    
        Since:
            12.1
    
        Also see:
            "Marini, J.W., and C.W. Murray, correction of Laser Range Tracking Data for Atmospheric Refraction at Elevations Above
            10 degrees, X-591-73-351, NASA GSFC, 1973"
    """
    def __init__(self, double: float, unit: org.orekit.utils.units.Unit): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class MendesPavlisModel(DiscreteTroposphericModel, TroposphericModel, MappingFunction, TroposphereMappingFunction):
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, pressureTemperatureHumidityProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, double: float, unit: org.orekit.utils.units.Unit): ...
    _computeZenithDelay_1__T = typing.TypeVar('_computeZenithDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeZenithDelay(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def computeZenithDelay(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_computeZenithDelay_1__T], tArray: typing.List[_computeZenithDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeZenithDelay_1__T]) -> typing.List[_computeZenithDelay_1__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    @typing.overload
    @staticmethod
    def getStandardModel(double: float) -> 'MendesPavlisModel': ...
    @typing.overload
    @staticmethod
    def getStandardModel(double: float, unit: org.orekit.utils.units.Unit) -> 'MendesPavlisModel': ...
    _mappingFactors_2__T = typing.TypeVar('_mappingFactors_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _mappingFactors_3__T = typing.TypeVar('_mappingFactors_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_2__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_2__T]) -> typing.List[_mappingFactors_2__T]: ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_3__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_3__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_3__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_3__T]) -> typing.List[_mappingFactors_3__T]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]: ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...

class ModifiedHopfieldModel(TroposphericModel):
    """
    public class ModifiedHopfieldModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        The modified Hopfield model.
    
        This model from Hopfield 1969, 1970, 1972 is described in equations 5.105, 5.106, 5.107 and 5.108 in Guochang Xu, GPS -
        Theory, Algorithms and Applications, Springer, 2007.
    
        Since:
            12.1
    
        Also see:
            "Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007"
    """
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class ModifiedSaastamoinenModel(TroposphericModel, DiscreteTroposphericModel):
    """
    public class ModifiedSaastamoinenModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`, :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        The modified Saastamoinen model. Estimates the path delay imposed to electro-magnetic signals by the troposphere
        according to the formula:
    
        .. code-block: java
        
         δ = 2.277e-3 / cos z * (P + (1255 / T + 0.05) * e - B * tan² z) + δR
         
        with the following input data provided to the model:
    
          - z: zenith angle
          - P: atmospheric pressure
          - T: temperature
          - e: partial pressure of water vapour
          - B, δR: correction terms
    
    
        The model supports custom δR correction terms to be read from a configuration file (saastamoinen-correction.txt) via
        the :class:`~org.orekit.data.DataProvidersManager`.
    
        Since:
            12.0
    
        Also see:
            "Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007"
    """
    DELTA_R_FILE_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DELTA_R_FILE_NAME
    
        Default file name for δR correction term table.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_LOW_ELEVATION_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_LOW_ELEVATION_THRESHOLD
    
        Default lowest acceptable elevation angle [rad].
    
        Also see:
            :meth:`~constant`
    
    
    """
    WATER: typing.ClassVar[org.orekit.models.earth.weather.water.Wang1988] = ...
    """
    public static final :class:`~org.orekit.models.earth.weather.water.Wang1988` WATER
    
        Provider for water pressure.
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, string: str): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    @typing.overload
    def __init__(self, pressureTemperatureHumidityProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider): ...
    @typing.overload
    def __init__(self, pressureTemperatureHumidityProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, string: str): ...
    @typing.overload
    def __init__(self, pressureTemperatureHumidityProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getLowElevationThreshold(self) -> float:
        """
            Get the low elevation threshold value for path delay computation.
        
            Returns:
                low elevation threshold, in rad.
        
            Since:
                10.2
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.pathDelay`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.pathDelay`
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPth0Provider(self) -> org.orekit.models.earth.weather.PressureTemperatureHumidityProvider:
        """
            Get provider for atmospheric pressure, temperature and humidity at reference altitude.
        
            Returns:
                provider for atmospheric pressure, temperature and humidity at reference altitude
        
        
        """
        ...
    @staticmethod
    def getStandardModel() -> 'ModifiedSaastamoinenModel':
        """
            Create a new Saastamoinen model using a standard atmosphere model.
        
              - altitude: 0m
              - temperature: 18 degree Celsius
              - pressure: 1013.25 mbar
              - humidity: 50%
              - @link :class:`~org.orekit.models.earth.weather.water.Wang1988` model to compute water vapor pressure
        
        
            Returns:
                a Saastamoinen model with standard environmental values
        
        
        """
        ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.setLowElevationThreshold`
        
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.setLowElevationThreshold`
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.setLowElevationThreshold`
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.setLowElevationThreshold`
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...
    def setLowElevationThreshold(self, double: float) -> None:
        """
            Set the low elevation threshold value for path delay computation.
        
            Parameters:
                lowElevationThreshold (double): The new value for the threshold [rad]
        
            Since:
                10.2
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.pathDelay`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.pathDelay`
        
        
        """
        ...

class NiellMappingFunctionModel(MappingFunction, TroposphereMappingFunction):
    """
    public class NiellMappingFunctionModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.MappingFunction`, :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
    
        The Niell Mapping Function model for radio wavelengths. This model is an empirical mapping function. It only needs the
        values of the station latitude, height and the date for the computations.
    
        With this model, the hydrostatic mapping function is time and latitude dependent whereas the wet mapping function is
        only latitude dependent.
    
        Also see:
            "A. E. Niell(1996), Global mapping functions for the atmosphere delay of radio wavelengths, J. Geophys. Res., 101(B2),
            pp. 3227–3246, doi: 10.1029/95JB03048."
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    _mappingFactors_2__T = typing.TypeVar('_mappingFactors_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _mappingFactors_3__T = typing.TypeVar('_mappingFactors_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
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
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public <T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T[] mappingFactors (T elevation, :class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_2__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_2__T]) -> typing.List[_mappingFactors_2__T]: ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_3__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_3__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_3__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_3__T]) -> typing.List[_mappingFactors_3__T]:
        """
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
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class PythonAzimuthalGradientProvider(AzimuthalGradientProvider):
    """
    public class PythonAzimuthalGradientProvider extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.AzimuthalGradientProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getGradientCoefficients_1__T = typing.TypeVar('_getGradientCoefficients_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGradientCoefficients(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> AzimuthalGradientCoefficients:
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
    def getGradientCoefficients(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getGradientCoefficients_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getGradientCoefficients_1__T]) -> FieldAzimuthalGradientCoefficients[_getGradientCoefficients_1__T]:
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

class PythonDiscreteTroposphericModel(DiscreteTroposphericModel):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class PythonDiscreteTroposphericModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        Deprecated.
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getParameters_3__T = typing.TypeVar('_getParameters_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getParameters_1__T]) -> typing.List[_getParameters_1__T]: ...
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Deprecated.
            Get model parameters.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` in
                interface :class:`~org.orekit.utils.ParameterDriversProvider`
        
            Returns:
                model parameters, will throw an exception if one PDriver has several values driven. If it's the case (if at least 1
                PDriver of the model has several values driven) the method
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` must be used.
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_3__T]) -> typing.List[_getParameters_3__T]:
        """
            Deprecated.
            Get model parameters.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` in
                interface :class:`~org.orekit.utils.ParameterDriversProvider`
        
            Parameters:
                field (:class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field to which the elements belong
        
            Returns:
                model parameters, will throw an exception if one PDriver of the has several values driven. If it's the case (if at least
                1 PDriver of the model has several values driven) the method
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` must be used.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Deprecated.
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Deprecated.
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Deprecated.
            Part of JCC Python interface to object
        """
        ...

class PythonMappingFunction(MappingFunction):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class PythonMappingFunction extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.MappingFunction`
    
        Deprecated.
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Deprecated.
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Deprecated.
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Deprecated.
            Part of JCC Python interface to object
        """
        ...

class PythonTroposphericModel(TroposphericModel):
    """
    public class PythonTroposphericModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
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

class PythonViennaAProvider(ViennaAProvider):
    """
    public class PythonViennaAProvider extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.ViennaAProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getA_0__T = typing.TypeVar('_getA_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_getA_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getA_0__T]) -> FieldViennaACoefficients[_getA_0__T]:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.troposphere.ViennaAProvider.getA`
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
    def getA(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> ViennaACoefficients:
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

class TimeSpanEstimatedModel(TroposphericModel):
    """
    public class TimeSpanEstimatedModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        Time span estimated tropospheric model.
    
        This class is closely related to :class:`~org.orekit.models.earth.troposphere.package` class.
    
    
        The difference is that it has a :class:`~org.orekit.utils.TimeSpanMap` of
        :class:`~org.orekit.models.earth.troposphere.EstimatedModel` objects as attribute.
    
    
        The idea behind this model is to allow the user to design a tropospheric model that can see its physical parameters
        (total zenith delay) change with time, at dates chosen by the user.
    
    
    
        Since:
            10.2
    """
    DATE_BEFORE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DATE_BEFORE
    
        Prefix for dates before in the tropospheric parameter drivers' name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATE_AFTER: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DATE_AFTER
    
        Prefix for dates after in the tropospheric parameter drivers' name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, estimatedModel: EstimatedModel): ...
    @typing.overload
    def __init__(self, estimatedModel: EstimatedModel, timeScale: org.orekit.time.TimeScale): ...
    def addTroposphericModelValidAfter(self, estimatedModel: EstimatedModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a EstimatedTroposphericModel entry valid after a limit date.
        
        
            Using :code:`addTroposphericModelValidAfter(entry, t)` will make :code:`entry` valid in [t, +∞[ (note the closed
            bracket).
        
            Parameters:
                model (:class:`~org.orekit.models.earth.troposphere.EstimatedModel`): EstimatedTroposphericModel entry
                earliestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date after which the entry is valid (must be different from **all** dates already used for transitions)
        
        
        """
        ...
    def addTroposphericModelValidBefore(self, estimatedModel: EstimatedModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add an EstimatedTroposphericModel entry valid before a limit date.
        
        
            Using :code:`addTroposphericValidBefore(entry, t)` will make :code:`entry` valid in ]-∞, t[ (note the open bracket).
        
            Parameters:
                model (:class:`~org.orekit.models.earth.troposphere.EstimatedModel`): EstimatedTroposphericModel entry
                latestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date before which the entry is valid (must be different from **all** dates already used for transitions)
        
        
        """
        ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Extract the proper parameter drivers' values from the array in input of the
            :meth:`~org.orekit.models.earth.troposphere.TimeSpanEstimatedModel.pathDelay` method. Parameters are filtered given an
            input date.
        
            Parameters:
                parameters (double[]): the input parameters array
                date (:class:`~org.orekit.time.AbsoluteDate`): the date
        
            Returns:
                the parameters given the date
        
        """
        ...
    @typing.overload
    def extractParameters(self, tArray: typing.List[_extractParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.List[_extractParameters_1__T]:
        """
            Extract the proper parameter drivers' values from the array in input of the
            :meth:`~org.orekit.models.earth.troposphere.TimeSpanEstimatedModel.pathDelay` method. Parameters are filtered given an
            input date.
        
            Parameters:
                parameters (T[]): the input parameters array
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date
        
            Returns:
                the parameters given the date
        
        
        """
        ...
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span[EstimatedModel]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTroposphericModel(self, absoluteDate: org.orekit.time.AbsoluteDate) -> EstimatedModel:
        """
            Get the :class:`~org.orekit.models.earth.troposphere.EstimatedModel` model valid at a date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the date of validity
        
            Returns:
                the EstimatedTroposphericModel model valid at date
        
        
        """
        ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class TimeSpanEstimatedTroposphericModel(DiscreteTroposphericModel):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class TimeSpanEstimatedTroposphericModel extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.troposphere.TimeSpanEstimatedModel`
        Time span estimated tropospheric model.
    
        This class is closely related to :class:`~org.orekit.models.earth.troposphere.package` class.
    
    
        The difference is that it has a :class:`~org.orekit.utils.TimeSpanMap` of
        :class:`~org.orekit.models.earth.troposphere.EstimatedTroposphericModel` objects as attribute.
    
    
        The idea behind this model is to allow the user to design a tropospheric model that can see its physical parameters
        (total zenith delay) change with time, at dates chosen by the user.
    
    
    
        Since:
            10.2
    """
    DATE_BEFORE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DATE_BEFORE
    
        Deprecated.
        Prefix for dates before in the tropospheric parameter drivers' name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATE_AFTER: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DATE_AFTER
    
        Deprecated.
        Prefix for dates after in the tropospheric parameter drivers' name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, estimatedTroposphericModel: 'EstimatedTroposphericModel'): ...
    @typing.overload
    def __init__(self, estimatedTroposphericModel: 'EstimatedTroposphericModel', timeScale: org.orekit.time.TimeScale): ...
    def addTroposphericModelValidAfter(self, estimatedTroposphericModel: 'EstimatedTroposphericModel', absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Deprecated.
            Add a EstimatedTroposphericModel entry valid after a limit date.
        
        
            Using :code:`addTroposphericModelValidAfter(entry, t)` will make :code:`entry` valid in [t, +∞[ (note the closed
            bracket).
        
            Parameters:
                model (:class:`~org.orekit.models.earth.troposphere.EstimatedTroposphericModel`): EstimatedTroposphericModel entry
                earliestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date after which the entry is valid (must be different from **all** dates already used for transitions)
        
        
        """
        ...
    def addTroposphericModelValidBefore(self, estimatedTroposphericModel: 'EstimatedTroposphericModel', absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Deprecated.
            Add an EstimatedTroposphericModel entry valid before a limit date.
        
        
            Using :code:`addTroposphericValidBefore(entry, t)` will make :code:`entry` valid in ]-∞, t[ (note the open bracket).
        
            Parameters:
                model (:class:`~org.orekit.models.earth.troposphere.EstimatedTroposphericModel`): EstimatedTroposphericModel entry
                latestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date before which the entry is valid (must be different from **all** dates already used for transitions)
        
        
        """
        ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
            Extract the proper parameter drivers' values from the array in input of the
            :meth:`~org.orekit.models.earth.troposphere.TimeSpanEstimatedTroposphericModel.pathDelay` method. Parameters are
            filtered given an input date.
        
            Parameters:
                parameters (double[]): the input parameters array
                date (:class:`~org.orekit.time.AbsoluteDate`): the date
        
            Returns:
                the parameters given the date
        
        """
        ...
    @typing.overload
    def extractParameters(self, tArray: typing.List[_extractParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.List[_extractParameters_1__T]:
        """
            Deprecated.
            Extract the proper parameter drivers' values from the array in input of the
            :meth:`~org.orekit.models.earth.troposphere.TimeSpanEstimatedTroposphericModel.pathDelay` method. Parameters are
            filtered given an input date.
        
            Parameters:
                parameters (T[]): the input parameters array
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date
        
            Returns:
                the parameters given the date
        
        
        """
        ...
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span['EstimatedTroposphericModel']: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTroposphericModel(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'EstimatedTroposphericModel':
        """
            Deprecated.
            Get the :class:`~org.orekit.models.earth.troposphere.EstimatedTroposphericModel` model valid at a date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the date of validity
        
            Returns:
                the EstimatedTroposphericModel model valid at date
        
        
        """
        ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

class TroposphereMappingFunctionAdapter(TroposphereMappingFunction):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class TroposphereMappingFunctionAdapter extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`
    
        Deprecated.
        temporary adapter to be removed when :class:`~org.orekit.models.earth.troposphere.MappingFunction` is removed
        Adapter between :class:`~org.orekit.models.earth.troposphere.MappingFunction` and
        :class:`~org.orekit.models.earth.troposphere.TroposphereMappingFunction`.
    
        This class is a temporary adapter, it will be removed when :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        is removed.
    
        Since:
            12.1
    """
    def __init__(self, mappingFunction: MappingFunction): ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
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
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
            Deprecated.
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
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class TroposphericModelAdapter(TroposphericModel):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class TroposphericModelAdapter extends :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
    
        Deprecated.
        temporary adapter to be removed when :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel` is removed
        Adapter between :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel` and
        :class:`~org.orekit.models.earth.troposphere.TroposphericModel`.
    
        This class is a temporary adapter, it will be removed when
        :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel` is removed.
    
        Since:
            12.1
    """
    def __init__(self, discreteTroposphericModel: DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_0__T], tArray: typing.List[_pathDelay_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            All delays are affected to :meth:`~org.orekit.models.earth.troposphere.FieldTroposphericDelay.getZh` and
            :meth:`~org.orekit.models.earth.troposphere.FieldTroposphericDelay.getSh` delays, the wet delays are arbitrarily set to
            0.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters for constant default values)
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            All delays are affected to :meth:`~org.orekit.models.earth.troposphere.TroposphericDelay.getZh` and
            :meth:`~org.orekit.models.earth.troposphere.TroposphericDelay.getSh` delays, the wet delays are arbitrarily set to 0.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.TroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.TroposphericModel`
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters for constant default values)
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere
        
        """
        ...

class ChaoMappingFunction(AbstractChaoMappingFunction):
    """
    public class ChaoMappingFunction extends :class:`~org.orekit.models.earth.troposphere.AbstractChaoMappingFunction`
    
        Chao mapping function for radio wavelengths.
    
        Since:
            12.1
    
        Also see:
            "C. C. Chao, A model for tropospheric calibration from delay surface and radiosonde ballon measurements, 1972"
    """
    def __init__(self): ...

class EstimatedTroposphericModel(EstimatedModel, DiscreteTroposphericModel):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class EstimatedTroposphericModel extends :class:`~org.orekit.models.earth.troposphere.EstimatedModel` implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.troposphere.EstimatedModel`
        An estimated tropospheric model. The tropospheric delay is computed according to the formula:
    
        δ = δ :sub:`h` * m :sub:`h` + (δ :sub:`t` - δ :sub:`h` ) * m :sub:`w`
    
        With:
    
          - δ :sub:`h` : Tropospheric zenith hydro-static delay.
          - δ :sub:`t` : Tropospheric total zenith delay.
          - m :sub:`h` : Hydro-static mapping function.
          - m :sub:`w` : Wet mapping function.
    
    
        The mapping functions m :sub:`h` (e) and m :sub:`w` (e) are computed thanks to a :code:`EstimatedModel.model`
        initialized by the user. The user has the possibility to use several mapping function models for the computations: the
        :class:`~org.orekit.models.earth.troposphere.GlobalMappingFunctionModel`, or the
        :class:`~org.orekit.models.earth.troposphere.NiellMappingFunctionModel`
    
        The tropospheric zenith delay δ :sub:`h` is computed empirically with a
        :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel` while the tropospheric total zenith delay δ
        :sub:`t` is estimated as a :class:`~org.orekit.utils.ParameterDriver`, hence the wet part is the difference between the
        two.
    """
    TOTAL_ZENITH_DELAY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TOTAL_ZENITH_DELAY
    
        Deprecated.
        Name of the parameter of this model: the total zenith delay.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, mappingFunction: MappingFunction, double3: float): ...
    @typing.overload
    def __init__(self, discreteTroposphericModel: DiscreteTroposphericModel, mappingFunction: MappingFunction, double: float): ...
    @typing.overload
    def __init__(self, mappingFunction: MappingFunction, double: float): ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public <T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T pathDelay (T elevation, :class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point, T[] parameters, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]: ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...

class MariniMurrayModel(MariniMurray, DiscreteTroposphericModel):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class MariniMurrayModel extends :class:`~org.orekit.models.earth.troposphere.MariniMurray` implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.troposphere.MariniMurray`
        The Marini-Murray tropospheric delay model for laser ranging.
    
        Also see:
            "Marini, J.W., and C.W. Murray, correction of Laser Range Tracking Data for Atmospheric Refraction at Elevations Above
            10 degrees, X-591-73-351, NASA GSFC, 1973"
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @staticmethod
    def getStandardModel(double: float) -> 'MariniMurrayModel':
        """
            Deprecated.
            Create a new Marini-Murray model using a standard atmosphere model.
        
              - temperature: 20 degree Celsius
              - pressure: 1013.25 mbar
              - humidity: 50%
        
        
            Parameters:
                lambda (double): laser wavelength (c/f), nm
        
            Returns:
                a Marini-Murray model with standard environmental values
        
        
        """
        ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]: ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...

class PythonAbstractVienna(AbstractVienna):
    """
    public class PythonAbstractVienna extends :class:`~org.orekit.models.earth.troposphere.AbstractVienna`
    """
    def __init__(self, viennaAProvider: ViennaAProvider, azimuthalGradientProvider: AzimuthalGradientProvider, troposphericModel: TroposphericModel, timeScale: org.orekit.time.TimeScale): ...
    def finalize(self) -> None: ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
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

class RevisedChaoMappingFunction(AbstractChaoMappingFunction):
    """
    public class RevisedChaoMappingFunction extends :class:`~org.orekit.models.earth.troposphere.AbstractChaoMappingFunction`
    
        Chao mapping function for radio wavelengths.
    
        The mapping function is described in A. Estefan, O. J. Sovers 1994 paper "A Comparative Survey of Current and Proposed
        Tropospheric Refraction-Delay Models for DSN Radio Metric Data Calibration"
    
        Since:
            12.1
    """
    def __init__(self): ...

class SaastamoinenModel(ModifiedSaastamoinenModel):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class SaastamoinenModel extends :class:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel`
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel`
        The modified Saastamoinen model.
    """
    DELTA_R_FILE_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DELTA_R_FILE_NAME
    
        Deprecated.
        Default file name for δR correction term table.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_LOW_ELEVATION_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_LOW_ELEVATION_THRESHOLD
    
        Deprecated.
        Default lowest acceptable elevation angle [rad].
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, string: str): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    @typing.overload
    @staticmethod
    def getStandardModel() -> ModifiedSaastamoinenModel: ...
    @typing.overload
    @staticmethod
    def getStandardModel() -> 'SaastamoinenModel': ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Overrides:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.pathDelay` in
                class :class:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.setLowElevationThreshold`
        
        :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public <T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T pathDelay (T elevation, :class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point, T[] parameters, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Overrides:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.pathDelay` in
                class :class:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.ModifiedSaastamoinenModel.setLowElevationThreshold`
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]: ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...

class ViennaOne(AbstractVienna):
    """
    public class ViennaOne extends :class:`~org.orekit.models.earth.troposphere.AbstractVienna`
    
        The Vienna 1 tropospheric delay model for radio techniques. The Vienna model data are given with a time interval of 6
        hours as well as on a global 2.5° * 2.0° grid. This version considered the height correction for the hydrostatic part
        developed by Niell, 1996.
    
        Since:
            12.1
    
        Also see:
            "Boehm, J., Werl, B., and Schuh, H., (2006), Troposhere mapping functions for GPS and very long baseline interferometry
            from European Centre for Medium-Range Weather Forecasts operational analysis data, J. Geophy. Res., Vol. 111, B02406,
            doi:10.1029/2005JB003629"
    """
    def __init__(self, viennaAProvider: ViennaAProvider, azimuthalGradientProvider: AzimuthalGradientProvider, troposphericModel: TroposphericModel, timeScale: org.orekit.time.TimeScale): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.TrackingCoordinates`): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                weather (:class:`~org.orekit.models.earth.weather.PressureTemperatureHumidity`): weather parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Parameters:
                trackingCoordinates (:class:`~org.orekit.utils.FieldTrackingCoordinates`<T> trackingCoordinates): tracking coordinates of the satellite
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                weather (:class:`~org.orekit.models.earth.weather.FieldPressureTemperatureHumidity`<T> weather): weather parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class ViennaThree(AbstractVienna):
    def __init__(self, viennaAProvider: ViennaAProvider, azimuthalGradientProvider: AzimuthalGradientProvider, troposphericModel: TroposphericModel, timeScale: org.orekit.time.TimeScale): ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]: ...

class ViennaOneModel(ViennaOne, DiscreteTroposphericModel, MappingFunction):
    """
    :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class ViennaOneModel extends :class:`~org.orekit.models.earth.troposphere.ViennaOne` implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`, :class:`~org.orekit.models.earth.troposphere.MappingFunction`
    
        Deprecated.
        as of 12.1, replaced by :class:`~org.orekit.models.earth.troposphere.ViennaOne`
        The Vienna1 tropospheric delay model for radio techniques. The Vienna model data are given with a time interval of 6
        hours as well as on a global 2.5° * 2.0° grid. This version considered the height correction for the hydrostatic part
        developed by Niell, 1996.
    
        Also see:
            "Boehm, J., Werl, B., and Schuh, H., (2006), Troposhere mapping functions for GPS and very long baseline interferometry
            from European Centre for Medium-Range Weather Forecasts operational analysis data, J. Geophy. Res., Vol. 111, B02406,
            doi:10.1029/2005JB003629"
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], timeScale: org.orekit.time.TimeScale): ...
    _computeZenithDelay_1__T = typing.TypeVar('_computeZenithDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeZenithDelay(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
            This method allows the computation of the zenith hydrostatic and zenith wet delay. The resulting element is an array
            having the following form:
        
              - T[0] = D :sub:`hz` → zenith hydrostatic delay
              - T[1] = D :sub:`wz` → zenith wet delay
        
        
            Parameters:
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the zenith hydrostatic and wet delays.
        
        """
        ...
    @typing.overload
    def computeZenithDelay(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_computeZenithDelay_1__T], tArray: typing.List[_computeZenithDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeZenithDelay_1__T]) -> typing.List[_computeZenithDelay_1__T]:
        """
            Deprecated.
            This method allows the computation of the zenith hydrostatic and zenith wet delay. The resulting element is an array
            having the following form:
        
              - T[0] = D :sub:`hz` → zenith hydrostatic delay
              - T[1] = D :sub:`wz` → zenith wet delay
        
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the zenith hydrostatic and wet delays.
        
        
        """
        ...
    _mappingFactors_2__T = typing.TypeVar('_mappingFactors_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _mappingFactors_3__T = typing.TypeVar('_mappingFactors_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) → hydrostatic mapping function
              - double[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public <T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T[] mappingFactors (T elevation, :class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Deprecated.
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) → hydrostatic mapping function
              - T[1] = m :sub:`w` (e) → wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors` in
                interface :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_2__T]) -> typing.List[_mappingFactors_2__T]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_3__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_3__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_3__T]) -> typing.List[_mappingFactors_3__T]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        :class:`~org.orekit.models.earth.troposphere.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public <T extends :class:`~org.orekit.models.earth.troposphere.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T pathDelay (T elevation, :class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point, T[] parameters, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Deprecated.
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters at current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]: ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...

class ViennaThreeModel(ViennaThree, DiscreteTroposphericModel, MappingFunction):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], timeScale: org.orekit.time.TimeScale): ...
    _computeZenithDelay_1__T = typing.TypeVar('_computeZenithDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeZenithDelay(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def computeZenithDelay(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_computeZenithDelay_1__T], tArray: typing.List[_computeZenithDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeZenithDelay_1__T]) -> typing.List[_computeZenithDelay_1__T]: ...
    _mappingFactors_2__T = typing.TypeVar('_mappingFactors_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _mappingFactors_3__T = typing.TypeVar('_mappingFactors_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_mappingFactors_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_2__T]) -> typing.List[_mappingFactors_2__T]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_3__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_3__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_3__T]) -> typing.List[_mappingFactors_3__T]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_2__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_2__T], fieldPressureTemperatureHumidity: org.orekit.models.earth.weather.FieldPressureTemperatureHumidity[_pathDelay_2__T], tArray: typing.List[_pathDelay_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_2__T]) -> FieldTroposphericDelay[_pathDelay_2__T]: ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, pressureTemperatureHumidity: org.orekit.models.earth.weather.PressureTemperatureHumidity, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.troposphere")``.

    AbstractChaoMappingFunction: typing.Type[AbstractChaoMappingFunction]
    AbstractVienna: typing.Type[AbstractVienna]
    AskneNordiusModel: typing.Type[AskneNordiusModel]
    AzimuthalGradientCoefficients: typing.Type[AzimuthalGradientCoefficients]
    AzimuthalGradientProvider: typing.Type[AzimuthalGradientProvider]
    CanonicalSaastamoinenModel: typing.Type[CanonicalSaastamoinenModel]
    ChaoMappingFunction: typing.Type[ChaoMappingFunction]
    ConstantAzimuthalGradientProvider: typing.Type[ConstantAzimuthalGradientProvider]
    ConstantTroposphericModel: typing.Type[ConstantTroposphericModel]
    ConstantViennaAProvider: typing.Type[ConstantViennaAProvider]
    DiscreteTroposphericModel: typing.Type[DiscreteTroposphericModel]
    DummyMappingFunction: typing.Type[DummyMappingFunction]
    EstimatedModel: typing.Type[EstimatedModel]
    EstimatedTroposphericModel: typing.Type[EstimatedTroposphericModel]
    FieldAzimuthalGradientCoefficients: typing.Type[FieldAzimuthalGradientCoefficients]
    FieldTroposphericDelay: typing.Type[FieldTroposphericDelay]
    FieldViennaACoefficients: typing.Type[FieldViennaACoefficients]
    FixedTroposphericDelay: typing.Type[FixedTroposphericDelay]
    GlobalMappingFunctionModel: typing.Type[GlobalMappingFunctionModel]
    MappingFunction: typing.Type[MappingFunction]
    MariniMurray: typing.Type[MariniMurray]
    MariniMurrayModel: typing.Type[MariniMurrayModel]
    MendesPavlisModel: typing.Type[MendesPavlisModel]
    ModifiedHopfieldModel: typing.Type[ModifiedHopfieldModel]
    ModifiedSaastamoinenModel: typing.Type[ModifiedSaastamoinenModel]
    NiellMappingFunctionModel: typing.Type[NiellMappingFunctionModel]
    PythonAbstractVienna: typing.Type[PythonAbstractVienna]
    PythonAzimuthalGradientProvider: typing.Type[PythonAzimuthalGradientProvider]
    PythonDiscreteTroposphericModel: typing.Type[PythonDiscreteTroposphericModel]
    PythonMappingFunction: typing.Type[PythonMappingFunction]
    PythonTroposphericModel: typing.Type[PythonTroposphericModel]
    PythonViennaAProvider: typing.Type[PythonViennaAProvider]
    RevisedChaoMappingFunction: typing.Type[RevisedChaoMappingFunction]
    SaastamoinenModel: typing.Type[SaastamoinenModel]
    TimeSpanEstimatedModel: typing.Type[TimeSpanEstimatedModel]
    TimeSpanEstimatedTroposphericModel: typing.Type[TimeSpanEstimatedTroposphericModel]
    TroposphereMappingFunction: typing.Type[TroposphereMappingFunction]
    TroposphereMappingFunctionAdapter: typing.Type[TroposphereMappingFunctionAdapter]
    TroposphericDelay: typing.Type[TroposphericDelay]
    TroposphericModel: typing.Type[TroposphericModel]
    TroposphericModelAdapter: typing.Type[TroposphericModelAdapter]
    TroposphericModelUtils: typing.Type[TroposphericModelUtils]
    ViennaACoefficients: typing.Type[ViennaACoefficients]
    ViennaAProvider: typing.Type[ViennaAProvider]
    ViennaModelCoefficientsLoader: typing.Type[ViennaModelCoefficientsLoader]
    ViennaModelType: typing.Type[ViennaModelType]
    ViennaOne: typing.Type[ViennaOne]
    ViennaOneModel: typing.Type[ViennaOneModel]
    ViennaThree: typing.Type[ViennaThree]
    ViennaThreeModel: typing.Type[ViennaThreeModel]
    class-use: org.orekit.models.earth.troposphere.class-use.__module_protocol__
