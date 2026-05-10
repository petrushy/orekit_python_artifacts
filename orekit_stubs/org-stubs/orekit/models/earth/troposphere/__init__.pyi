
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus
import org.orekit.bodies
import org.orekit.data
import org.orekit.models.earth.troposphere.iturp834
import org.orekit.models.earth.weather
import org.orekit.models.earth.weather.water
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class AzimuthalGradientCoefficients:
    """
    Container for the azimuthal gradient coefficients gn :sub:`h` , ge :sub:`h` , gn :sub:`w` and ge :sub:`w` .
    
    Since:
        12.1
    """
    def __init__(self, gnh: float, geh: float, gnw: float, gew: float):
        """
        Simple constructor.
        
        Parameters:
            gnh (double): North hydrostatic coefficient
            geh (double): East hydrostatic coefficient
            gnw (double): North wet coefficient
            gew (double): East wet coefficient
        
        
        """
        ...
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
    Provider for AzimuthalGradientCoefficients and FieldAzimuthalGradientCoefficients.
    
    Since:
        12.1
    """
    _getGradientCoefficients_1__T = typing.TypeVar('_getGradientCoefficients_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGradientCoefficients(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> AzimuthalGradientCoefficients:
        """
        Get azimuthal asymmetry gradients.
        
        Parameters:
            location (GeodeticPoint): location at which parameters are requested
            date (AbsoluteDate): date at which parameters are requested
        
        Returns:
            azimuthal asymmetry gradients or null if no gradients are available
        
        """
        ...
    @typing.overload
    def getGradientCoefficients(self, location: org.orekit.bodies.FieldGeodeticPoint[_getGradientCoefficients_1__T], date: org.orekit.time.FieldAbsoluteDate[_getGradientCoefficients_1__T]) -> 'FieldAzimuthalGradientCoefficients'[_getGradientCoefficients_1__T]:
        """
        Get azimuthal asymmetry gradients.
        
        Parameters:
            location (FieldGeodeticPoint<T> location): location at which parameters are requested
            date (FieldAbsoluteDate<T> date): date at which parameters are requested
        
        Returns:
            azimuthal asymmetry gradients or null if no gradients are available
        
        
        """
        ...

_FieldAzimuthalGradientCoefficients__T = typing.TypeVar('_FieldAzimuthalGradientCoefficients__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAzimuthalGradientCoefficients(typing.Generic[_FieldAzimuthalGradientCoefficients__T]):
    """
    Container for the azimuthal gradient coefficients gn :sub:`h` , ge :sub:`h` , gn :sub:`w` and ge :sub:`w` .
    
    Since:
        12.1
    """
    def __init__(self, gnh: _FieldAzimuthalGradientCoefficients__T, geh: _FieldAzimuthalGradientCoefficients__T, gnw: _FieldAzimuthalGradientCoefficients__T, gew: _FieldAzimuthalGradientCoefficients__T):
        """
        Simple constructor.
        
        Parameters:
            gnh (FieldAzimuthalGradientCoefficients): North hydrostatic coefficient
            geh (FieldAzimuthalGradientCoefficients): East hydrostatic coefficient
            gnw (FieldAzimuthalGradientCoefficients): North wet coefficient
            gew (FieldAzimuthalGradientCoefficients): East wet coefficient
        
        
        """
        ...
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
    Container for tropospheric delay.
    
    Since:
        12.1
    """
    def __init__(self, zh: _FieldTroposphericDelay__T, zw: _FieldTroposphericDelay__T, sh: _FieldTroposphericDelay__T, sw: _FieldTroposphericDelay__T):
        """
        Simple constructor.
        
        Parameters:
            zh (FieldTroposphericDelay): hydrostatic zenith delay (m)
            zw (FieldTroposphericDelay): wet zenith delay (m)
            sh (FieldTroposphericDelay): hydrostatic slanted delay (m)
            sw (FieldTroposphericDelay): wet slanted delay (m)
        
        
        """
        ...
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
    Container for the ViennaOne and ViennaThree coefficients a :sub:`h` and a :sub:`w` .
    
    Since:
        12.1
    """
    def __init__(self, ah: _FieldViennaACoefficients__T, aw: _FieldViennaACoefficients__T):
        """
        Simple constructor.
        
        Parameters:
            ah (FieldViennaACoefficients): hydrostatic coefficient
            aw (FieldViennaACoefficients): wet coefficient
        
        
        """
        ...
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

class TroposphereMappingFunction:
    """
    Interface for mapping functions used in the tropospheric delay computation.
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
          - double[0] = m :sub:`h` (e) → hydrostatic mapping function
          - double[1] = m :sub:`w` (e) → wet mapping function
        
        
        Parameters:
            trackingCoordinates (TrackingCoordinates): tracking coordinates of the satellite
            point (GeodeticPoint): station location
            date (AbsoluteDate): current date
        
        Returns:
            a two components array containing the hydrostatic and wet mapping functions.
        
        Since:
            13.0
        
        """
        ...
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], point: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], date: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.MutableSequence[_mappingFactors_1__T]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
          - T[0] = m :sub:`h` (e) → hydrostatic mapping function
          - T[1] = m :sub:`w` (e) → wet mapping function
        
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            a two components array containing the hydrostatic and wet mapping functions.
        
        Since:
            13.0
        
        
        """
        ...

class TroposphericDelay:
    """
    Container for tropospheric delay.
    
    Since:
        12.1
    """
    def __init__(self, zh: float, zw: float, sh: float, sw: float):
        """
        Simple constructor.
        
        Parameters:
            zh (double): hydrostatic zenith delay (m)
            zw (double): wet zenith delay (m)
            sh (double): hydrostatic slanted delay (m)
            sw (double): wet slanted delay (m)
        
        
        """
        ...
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
    Defines a tropospheric model, used to calculate the path delay imposed to electro-magnetic signals between an orbital satellite and a ground station.
    
    Since:
        12.1
    """
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            parameters (T[]): tropospheric model parameters at current date
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            the path delay due to the troposphere
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        Parameters:
            trackingCoordinates (TrackingCoordinates): tracking coordinates of the satellite
            point (GeodeticPoint): station location
            parameters (double[]): tropospheric model parameters
            date (AbsoluteDate): current date
        
        Returns:
            the path delay due to the troposphere
        
        Since:
            13.0
        
        """
        ...

class TroposphericModelUtils:
    """
    Utility class for tropospheric models.
    
    Since:
        11.0
    """
    NANO_M: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Nanometers unit.
    
    Since:
        12.1
    
    
    """
    MICRO_M: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Micrometers unit.
    
    Since:
        12.1
    
    
    """
    HECTO_PASCAL: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    HectoPascal unit.
    
    Since:
        12.1
    
    
    """
    STANDARD_ATMOSPHERE: typing.ClassVar[org.orekit.models.earth.weather.PressureTemperatureHumidity] = ...
    """
    Standard atmosphere.
    
      - altitude: 0m
      - temperature: 20 degree Celsius
      - pressure: 1013.25 mbar
      - humidity: 50%
    
    
    Since:
        12.1
    
    Also see:
        STANDARD_ATMOSPHERE_PROVIDER
    
    
    """
    STANDARD_ATMOSPHERE_PROVIDER: typing.ClassVar[org.orekit.models.earth.weather.PressureTemperatureHumidityProvider] = ...
    """
    Provider for STANDARD_ATMOSPHERE.
    
    Since:
        12.1
    
    
    """
    _computeHeightCorrection_1__T = typing.TypeVar('_computeHeightCorrection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeHeightCorrection(elevation: float, height: float) -> float:
        """
        This method computes the height correction for the hydrostatic component of the mapping function. The formulas are given by Neill's paper, 1996:
        
        Niell A. E. (1996) "Global mapping functions for the atmosphere delay of radio wavelengths,” J. Geophys. Res., 101(B2), pp. 3227–3246, doi: 10.1029/95JB03048.
        
        Parameters:
            elevation (double): the elevation of the satellite, in radians.
            height (double): the height of the station in m above sea level.
        
        Returns:
            the height correction, in m
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeHeightCorrection(elevation: _computeHeightCorrection_1__T, height: _computeHeightCorrection_1__T, field: org.hipparchus.Field[_computeHeightCorrection_1__T]) -> _computeHeightCorrection_1__T:
        """
        This method computes the height correction for the hydrostatic component of the mapping function. The formulas are given by Neill's paper, 1996:
        
        Niell A. E. (1996) "Global mapping functions for the atmosphere delay of radio wavelengths,” J. Geophys. Res., 101(B2), pp. 3227–3246, doi: 10.1029/95JB03048.
        
        Parameters:
            elevation (T): the elevation of the satellite, in radians.
            height (T): the height of the station in m above sea level.
            field (Field<T> field): field to which the elements belong
        
        Returns:
            the height correction, in m
        
        
        """
        ...
    _mappingFunction_1__T = typing.TypeVar('_mappingFunction_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def mappingFunction(a: float, b: float, c: float, elevation: float) -> float:
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
    def mappingFunction(a: _mappingFunction_1__T, b: _mappingFunction_1__T, c: _mappingFunction_1__T, elevation: _mappingFunction_1__T) -> _mappingFunction_1__T:
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
    Container for the ViennaOne and ViennaThree coefficients a :sub:`h` and a :sub:`w` .
    
    Since:
        12.1
    """
    def __init__(self, ah: float, aw: float):
        """
        Simple constructor.
        
        Parameters:
            ah (double): hydrostatic coefficient
            aw (double): wet coefficient
        
        
        """
        ...
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
    Provider for ViennaOne and ViennaThree coefficients a :sub:`h` and a :sub:`w` .
    
    Since:
        12.1
    """
    _getA_0__T = typing.TypeVar('_getA_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self, location: org.orekit.bodies.FieldGeodeticPoint[_getA_0__T], date: org.orekit.time.FieldAbsoluteDate[_getA_0__T]) -> FieldViennaACoefficients[_getA_0__T]:
        """
        Get coefficients array for VMF mapping function.
        
          - double[0] = a :sub:`h`
          - double[1] = a :sub:`w`
        
        
        Parameters:
            location (FieldGeodeticPoint<T> location): location at which parameters are requested
            date (FieldAbsoluteDate<T> date): date at which parameters are requested
        
        Returns:
            the coefficients array for VMF mapping function
        
        
        """
        ...
    @typing.overload
    def getA(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> ViennaACoefficients:
        """
        Get coefficients array for VMF mapping function.
        
          - double[0] = a :sub:`h`
          - double[1] = a :sub:`w`
        
        
        Parameters:
            location (GeodeticPoint): location at which parameters are requested
            date (AbsoluteDate): date at which parameters are requested
        
        Returns:
            the coefficients array for VMF mapping function
        
        """
        ...

class ViennaModelCoefficientsLoader(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader):
    """
    Loads Vienna tropospheric coefficients a given input stream. A stream contains, for a given day and a given hour, the hydrostatic and wet zenith delays and the ah and aw coefficients used for the computation of the mapping function. The coefficients are given with a time interval of 6 hours.
    
    A bilinear interpolation is performed the case of the user initialize the latitude and the longitude with values that are not contained in the stream.
    
    The coefficients are obtained from GRID. Find more on the files at the at.
    
    The files have to be extracted to UTF-8 text files before being read by this loader.
    
    After extraction, it is assumed they are named VMFG_YYYYMMDD.Hhh for ViennaOne and VMF3_YYYYMMDD.Hhh ViennaThree. Where YYYY is the 4-digits year, MM the month, DD the day and hh the 2-digits hour.
    
    The format is always the same, with and example shown below for VMF1 model.
    
    Example:
    
     ! Version:            1.0 ! Source:             J. Boehm, TU Vienna (created: 2018-11-20) ! Data_types:         VMF1 (lat lon ah aw zhd zwd) ! Epoch:              2018 11 19 18 00  0.0 ! Scale_factor:       1.e+00 ! Range/resolution:   -90 90 0 360 2 2.5 ! Comment:            https://vmf.geo.tuwien.ac.at/trop_products/GRID/2.5x2/VMF1/VMF1_OP/ 90.0   0.0 0.00116059  0.00055318  2.3043  0.0096 90.0   2.5 0.00116059  0.00055318  2.3043  0.0096 90.0   5.0 0.00116059  0.00055318  2.3043  0.0096 90.0   7.5 0.00116059  0.00055318  2.3043  0.0096 90.0  10.0 0.00116059  0.00055318  2.3043  0.0096 90.0  12.5 0.00116059  0.00055318  2.3043  0.0096 90.0  15.0 0.00116059  0.00055318  2.3043  0.0096 90.0  17.5 0.00116059  0.00055318  2.3043  0.0096 90.0  20.0 0.00116059  0.00055318  2.3043  0.0096 90.0  22.5 0.00116059  0.00055318  2.3043  0.0096 90.0  25.0 0.00116059  0.00055318  2.3043  0.0096 90.0  27.5 0.00116059  0.00055318  2.3043  0.0096
    
    It is not safe for multiple threads to share a single instance of this class.
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default supported files name pattern.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, latitude: float, longitude: float, type: 'ViennaModelType'): ...
    @typing.overload
    def __init__(self, supportedNames: str, latitude: float, longitude: float, type: 'ViennaModelType'): ...
    @typing.overload
    def __init__(self, supportedNames: str, latitude: float, longitude: float, type: 'ViennaModelType', dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getA(self) -> typing.MutableSequence[float]:
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
        Description copied from class: getSupportedNames Get the supported names regular expression.
        
        Overrides: getSupportedNames in class AbstractSelfFeedingLoader
        
        Returns:
            the supported names.
        
        Also see:
            feed
        
        
        """
        ...
    def getZenithDelay(self) -> typing.MutableSequence[float]:
        """
        Returns the zenith delay array.
        
          - double[0] = D :sub:`hz` → zenith hydrostatic delay
          - double[1] = D :sub:`wz` → zenith wet delay
        
        
        Returns:
            the zenith delay array
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Description copied from interface: loadData Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
        
        
        """
        ...
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
            dateTimeComponents (DateTimeComponents): date and time component.
        
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
        Description copied from interface: stillAcceptsData Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
        Returns:
            true while the loader still accepts new data
        
        
        """
        ...

class ViennaModelType(java.lang.Enum['ViennaModelType']):
    """
    Enumerate for Vienna tropospheric model 1 and 3. This enumerate is used for the coefficients loader.
    
    Also see:
        ViennaOne, ViennaThree
    """
    VIENNA_ONE: typing.ClassVar['ViennaModelType'] = ...
    VIENNA_THREE: typing.ClassVar['ViennaModelType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ViennaModelType':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['ViennaModelType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ViennaModelType c : ViennaModelType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AbstractChaoMappingFunction(TroposphereMappingFunction):
    """
    Chao mapping function for radio wavelengths.
    
    Since:
        12.1
    
    Also see:
        "C. C. Chao, A model for tropospheric calibration from delay surface and radiosonde ballon measurements, 1972"
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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

class AbstractVienna(TroposphericModel, TroposphereMappingFunction):
    """
    The Vienna tropospheric delay model for radio techniques.
    
    Since:
        12.1
    """
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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

class AskneNordiusModel(TroposphericModel):
    """
    The Askne Nordius model.
    
    The hydrostatic part is equivalent to Saastamoinen, whereas the wet part takes into account getTm and getLambda.
    
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
    Lowest acceptable elevation angle [rad].
    
    Also see:
        constant
    
    
    """
    def __init__(self, mappingFunction: TroposphereMappingFunction, pthProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider):
        """
        Create a new Askne Nordius model.
        
        Parameters:
            mappingFunction (TroposphereMappingFunction): mapping function
            pthProvider (PressureTemperatureHumidityProvider): provider for pressure, temperature and humidity
        
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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

class CanonicalSaastamoinenModel(TroposphericModel):
    """
    The canonical Saastamoinen model.
    
    Estimates the path delay imposed to electro-magnetic signals by the troposphere according to the formula: \[ \delta = \frac{0.002277}{\cos z} \left[P+(\frac{1255}{T}+0.005)e - B(h) \tan^2 z\right] \] with the following input data provided to the model:
    
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
    Default lowest acceptable elevation angle [rad].
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, pthProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider): ...
    def getLowElevationThreshold(self) -> float:
        """
        Get the low elevation threshold value for path delay computation.
        
        Returns:
            low elevation threshold, in rad.
        
        Also see:
            pathDelay,
            pathDelay
        
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when altitude is negative.
        
        There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a threshold will use the value obtained for the threshold itself.
        
        Specified by: pathDelay in interface TroposphericModel
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            parameters (T[]): tropospheric model parameters at current date
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            the path delay due to the troposphere
        
        Also see:
            getLowElevationThreshold,
            setLowElevationThreshold
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when altitude is negative.
        
        There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a threshold will use the value obtained for the threshold itself.
        
        Specified by: pathDelay in interface TroposphericModel
        
        Parameters:
            trackingCoordinates (TrackingCoordinates): tracking coordinates of the satellite
            point (GeodeticPoint): station location
            parameters (double[]): tropospheric model parameters
            date (AbsoluteDate): current date
        
        Returns:
            the path delay due to the troposphere
        
        Also see:
            getLowElevationThreshold,
            setLowElevationThreshold
        
        """
        ...
    def setLowElevationThreshold(self, lowElevationThreshold: float) -> None:
        """
        Set the low elevation threshold value for path delay computation.
        
        Parameters:
            lowElevationThreshold (double): The new value for the threshold [rad]
        
        Also see:
            pathDelay,
            pathDelay
        
        
        """
        ...

class ConstantAzimuthalGradientProvider(AzimuthalGradientProvider):
    """
    Constant provider for AzimuthalGradientCoefficients and FieldAzimuthalGradientCoefficients.
    
    Since:
        12.1
    """
    def __init__(self, a: AzimuthalGradientCoefficients):
        """
        Simple constructor.
        
        Parameters:
            a (AzimuthalGradientCoefficients): constant parameters (may be null if no gradients are available)
        
        
        """
        ...
    _getGradientCoefficients_1__T = typing.TypeVar('_getGradientCoefficients_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGradientCoefficients(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> AzimuthalGradientCoefficients:
        """
        Get azimuthal asymmetry gradients.
        
        Specified by: getGradientCoefficients in interface AzimuthalGradientProvider
        
        Parameters:
            location (GeodeticPoint): location at which parameters are requested
            date (AbsoluteDate): date at which parameters are requested
        
        Returns:
            azimuthal asymmetry gradients or null if no gradients are available
        
        """
        ...
    @typing.overload
    def getGradientCoefficients(self, location: org.orekit.bodies.FieldGeodeticPoint[_getGradientCoefficients_1__T], date: org.orekit.time.FieldAbsoluteDate[_getGradientCoefficients_1__T]) -> FieldAzimuthalGradientCoefficients[_getGradientCoefficients_1__T]:
        """
        Get azimuthal asymmetry gradients.
        
        Specified by: getGradientCoefficients in interface AzimuthalGradientProvider
        
        Parameters:
            location (FieldGeodeticPoint<T> location): location at which parameters are requested
            date (FieldAbsoluteDate<T> date): date at which parameters are requested
        
        Returns:
            azimuthal asymmetry gradients or null if no gradients are available
        
        
        """
        ...

class ConstantTroposphericModel(TroposphericModel):
    """
    Defines a constant tropospheric model.
    
    Since:
        12.1
    """
    def __init__(self, delay: TroposphericDelay):
        """
        Simple constructor.
        
        Parameters:
            delay (TroposphericDelay): constant delay
        
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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

class ConstantViennaAProvider(ViennaAProvider):
    """
    Provider for constant Vienna A coefficients.
    
    Since:
        12.1
    """
    def __init__(self, a: ViennaACoefficients):
        """
        Simple constructor.
        
        Parameters:
            a (ViennaACoefficients): constant parameters
        
        
        """
        ...
    _getA_0__T = typing.TypeVar('_getA_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self, location: org.orekit.bodies.FieldGeodeticPoint[_getA_0__T], date: org.orekit.time.FieldAbsoluteDate[_getA_0__T]) -> FieldViennaACoefficients[_getA_0__T]:
        """
        Get coefficients array for VMF mapping function.
        
          - double[0] = a :sub:`h`
          - double[1] = a :sub:`w`
        
        Specified by: getA in interface ViennaAProvider
        
        Parameters:
            location (FieldGeodeticPoint<T> location): location at which parameters are requested
            date (FieldAbsoluteDate<T> date): date at which parameters are requested
        
        Returns:
            the coefficients array for VMF mapping function
        
        
        """
        ...
    @typing.overload
    def getA(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> ViennaACoefficients:
        """
        Get coefficients array for VMF mapping function.
        
          - double[0] = a :sub:`h`
          - double[1] = a :sub:`w`
        
        Specified by: getA in interface ViennaAProvider
        
        Parameters:
            location (GeodeticPoint): location at which parameters are requested
            date (AbsoluteDate): date at which parameters are requested
        
        Returns:
            the coefficients array for VMF mapping function
        
        """
        ...

class DummyMappingFunction(TroposphereMappingFunction):
    """
    Dummy mapping function.
    
    This mapping function just uses 1.0 as constant mapping factors, which implies the slanted tropospheric delays are equal to the zenith delays. This is mainly useful when only zenith delays are needed.
    
    Since:
        12.1
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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

class EstimatedModel(TroposphericModel):
    """
    An estimated tropospheric model. The tropospheric delay is computed according to the formula:
    
    δ = δ :sub:`h` * m :sub:`h` + (δ :sub:`t` - δ :sub:`h` ) * m :sub:`w`
    
    With:
    
      - δ :sub:`h` : Tropospheric zenith hydro-static delay.
      - δ :sub:`t` : Tropospheric total zenith delay.
      - m :sub:`h` : Hydro-static mapping function.
      - m :sub:`w` : Wet mapping function.
    
    The mapping functions m :sub:`h` (e) and m :sub:`w` (e) are computed thanks to a model initialized by the user. The user has the possibility to use several mapping function models for the computations: the GlobalMappingFunctionModel, or the NiellMappingFunctionModel
    
    The tropospheric zenith delay δ :sub:`h` is computed empirically with a TroposphericModel while the tropospheric total zenith delay δ :sub:`t` is estimated as a ParameterDriver, hence the wet part is the difference between the two.
    
    Since:
        12.1
    """
    TOTAL_ZENITH_DELAY: typing.ClassVar[str] = ...
    """
    Name of the parameter of this model: the total zenith delay.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, h0: float, t0: float, p0: float, model: TroposphereMappingFunction, totalDelay: float): ...
    @typing.overload
    def __init__(self, model: TroposphereMappingFunction, totalDelay: float): ...
    @typing.overload
    def __init__(self, hydrostatic: TroposphericModel, model: TroposphereMappingFunction, totalDelay: float): ...
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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

class FixedTroposphericDelay(TroposphericModel):
    """
    A static tropospheric model that interpolates the actual tropospheric delay based on values read from a configuration file (tropospheric-delay.txt) via the DataProvidersManager.
    """
    @typing.overload
    def __init__(self, xArr: typing.Union[typing.List[float], jpype.JArray], yArr: typing.Union[typing.List[float], jpype.JArray], fArr: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, supportedName: str): ...
    @typing.overload
    def __init__(self, supportedName: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    @staticmethod
    def getDefaultModel() -> 'FixedTroposphericDelay':
        """
        Returns the default model, loading delay values from the file "tropospheric-delay.txt" via the getDefault.
        
        This method uses the getDefault.
        
        Returns:
            the default model
        
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        All delays are affected to getZh and getSh delays, the wet delays are arbitrarily set to 0.
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        All delays are affected to getZh and getSh delays, the wet delays are arbitrarily set to 0.
        
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

class GlobalMappingFunctionModel(TroposphereMappingFunction):
    """
    The Global Mapping Function model for radio techniques. This model is an empirical mapping function. It only needs the values of the station latitude, longitude, height and the date for the computations.
    
    The Global Mapping Function is based on spherical harmonics up to degree and order of 9. It was developed to be consistent with the ViennaOne mapping function model.
    
    Also see:
        "Boehm, J., A.E. Niell, P. Tregoning, H. Schuh (2006), Global Mapping Functions (GMF): A new empirical mapping function
        based on numerical weather model data, Geoph. Res. Letters, Vol. 33, L07304, doi:10.1029/2005GL025545.", "Petit, G. and
        Luzum, B. (eds.), IERS Conventions (2010), IERS Technical Note No. 36, BKG (2010)"
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, utc: org.orekit.time.TimeScale): ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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

class MariniMurray(TroposphericModel):
    """
    The Marini-Murray tropospheric delay model for laser ranging.
    
    Since:
        12.1
    
    Also see:
        "Marini, J.W., and C.W. Murray, correction of Laser Range Tracking Data for Atmospheric Refraction at Elevations Above
        10 degrees, X-591-73-351, NASA GSFC, 1973"
    """
    def __init__(self, lambda_: float, lambdaUnits: org.orekit.utils.units.Unit, pthProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider):
        """
        Create a new Marini-Murray model for the troposphere.
        
        Parameters:
            lambda (double): laser wavelength
            lambdaUnits (Unit): units in which lambda is given
            pthProvider (PressureTemperatureHumidityProvider): provider for pressure, temperature and humidity
        
        Since:
            12.1
        
        Also see:
            MICRO_M,
            NANO_M
        
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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

class MendesPavlisModel(TroposphericModel, TroposphereMappingFunction):
    def __init__(self, pressureTemperatureHumidityProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, double: float, unit: org.orekit.utils.units.Unit): ...
    _computeZenithDelay_1__T = typing.TypeVar('_computeZenithDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeZenithDelay(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    @typing.overload
    def computeZenithDelay(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_computeZenithDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeZenithDelay_1__T]) -> typing.MutableSequence[_computeZenithDelay_1__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    @staticmethod
    def getStandardModel(double: float, unit: org.orekit.utils.units.Unit) -> 'MendesPavlisModel': ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.MutableSequence[_mappingFactors_1__T]: ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], tArray: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]: ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.Union[typing.List[float], jpype.JArray], absoluteDate: org.orekit.time.AbsoluteDate) -> TroposphericDelay: ...

class ModifiedHopfieldModel(TroposphericModel):
    """
    The modified Hopfield model.
    
    This model from Hopfield 1969, 1970, 1972 is described in equations 5.105, 5.106, 5.107 and 5.108 in Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007.
    
    Since:
        12.1
    
    Also see:
        "Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007"
    """
    def __init__(self, pthProvider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider):
        """
        Create a new Hopfield model.
        
        Parameters:
            pthProvider (PressureTemperatureHumidityProvider): provider for pressure, temperature and humidity
        
        Since:
            13.0
        
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when altitude is negative.
        
        There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a threshold will use the value obtained for the threshold itself.
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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

class ModifiedSaastamoinenModel(TroposphericModel):
    """
    The modified Saastamoinen model. Estimates the path delay imposed to electro-magnetic signals by the troposphere according to the formula:
    
     δ = 2.277e-3 / cos z * (P + (1255 / T + 0.05) * e - B * tan² z) + δR with the following input data provided to the model:
    
      - z: zenith angle
      - P: atmospheric pressure
      - T: temperature
      - e: partial pressure of water vapour
      - B, δR: correction terms
    
    The model supports custom δR correction terms to be read from a configuration file (saastamoinen-correction.txt) via the DataProvidersManager.
    
    Since:
        12.0
    
    Also see:
        "Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007"
    """
    DELTA_R_FILE_NAME: typing.ClassVar[str] = ...
    """
    Default file name for δR correction term table.
    
    Also see:
        constant
    
    
    """
    DEFAULT_LOW_ELEVATION_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default lowest acceptable elevation angle [rad].
    
    Also see:
        constant
    
    
    """
    WATER: typing.ClassVar[org.orekit.models.earth.weather.water.Wang1988] = ...
    """
    Provider for water pressure.
    """
    @typing.overload
    def __init__(self, pth0Provider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider): ...
    @typing.overload
    def __init__(self, pth0Provider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, deltaRFileName: str): ...
    @typing.overload
    def __init__(self, pth0Provider: org.orekit.models.earth.weather.PressureTemperatureHumidityProvider, deltaRFileName: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getLowElevationThreshold(self) -> float:
        """
        Get the low elevation threshold value for path delay computation.
        
        Returns:
            low elevation threshold, in rad.
        
        Since:
            10.2
        
        Also see:
            pathDelay,
            pathDelay
        
        
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
          - @link Wang1988 model to compute water vapor pressure
        
        
        Returns:
            a Saastamoinen model with standard environmental values
        
        
        """
        ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when altitude is negative.
        
        There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a threshold will use the value obtained for the threshold itself.
        
        Specified by: pathDelay in interface TroposphericModel
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            parameters (T[]): tropospheric model parameters at current date
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            the path delay due to the troposphere
        
        Also see:
            getLowElevationThreshold,
            setLowElevationThreshold
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
        """
        Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
        The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when altitude is negative.
        
        There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a threshold will use the value obtained for the threshold itself.
        
        Specified by: pathDelay in interface TroposphericModel
        
        Parameters:
            trackingCoordinates (TrackingCoordinates): tracking coordinates of the satellite
            point (GeodeticPoint): station location
            parameters (double[]): tropospheric model parameters
            date (AbsoluteDate): current date
        
        Returns:
            the path delay due to the troposphere
        
        Also see:
            getLowElevationThreshold,
            setLowElevationThreshold
        
        """
        ...
    def setLowElevationThreshold(self, lowElevationThreshold: float) -> None:
        """
        Set the low elevation threshold value for path delay computation.
        
        Parameters:
            lowElevationThreshold (double): The new value for the threshold [rad]
        
        Since:
            10.2
        
        Also see:
            pathDelay,
            pathDelay
        
        
        """
        ...

class NiellMappingFunctionModel(TroposphereMappingFunction):
    """
    The Niell Mapping Function model for radio wavelengths. This model is an empirical mapping function. It only needs the values of the station latitude, height and the date for the computations.
    
    With this model, the hydrostatic mapping function is time and latitude dependent whereas the wet mapping function is only latitude dependent.
    
    Also see:
        "A. E. Niell(1996), Global mapping functions for the atmosphere delay of radio wavelengths, J. Geophys. Res., 101(B2),
        pp. 3227–3246, doi: 10.1029/95JB03048."
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, utc: org.orekit.time.TimeScale): ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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

class PythonAzimuthalGradientProvider(AzimuthalGradientProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getGradientCoefficients_1__T = typing.TypeVar('_getGradientCoefficients_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGradientCoefficients(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> AzimuthalGradientCoefficients:
        """
        Get azimuthal asymmetry gradients.
        
        Specified by: getGradientCoefficients in interface AzimuthalGradientProvider
        
        Parameters:
            location (GeodeticPoint): location at which parameters are requested
            date (AbsoluteDate): date at which parameters are requested
        
        Returns:
            azimuthal asymmetry gradients or null if no gradients are available
        
        """
        ...
    @typing.overload
    def getGradientCoefficients(self, location: org.orekit.bodies.FieldGeodeticPoint[_getGradientCoefficients_1__T], date: org.orekit.time.FieldAbsoluteDate[_getGradientCoefficients_1__T]) -> FieldAzimuthalGradientCoefficients[_getGradientCoefficients_1__T]:
        """
        Get azimuthal asymmetry gradients.
        
        Specified by: getGradientCoefficients in interface AzimuthalGradientProvider
        
        Parameters:
            location (FieldGeodeticPoint<T> location): location at which parameters are requested
            date (FieldAbsoluteDate<T> date): date at which parameters are requested
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonTroposphereMappingFunction(TroposphereMappingFunction):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonTroposphericModel(TroposphericModel):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonViennaAProvider(ViennaAProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getA_0__T = typing.TypeVar('_getA_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getA(self, location: org.orekit.bodies.FieldGeodeticPoint[_getA_0__T], date: org.orekit.time.FieldAbsoluteDate[_getA_0__T]) -> FieldViennaACoefficients[_getA_0__T]:
        """
        Description copied from interface: getA Get coefficients array for VMF mapping function.
        
          - double[0] = a :sub:`h`
          - double[1] = a :sub:`w`
        
        Specified by: getA in interface ViennaAProvider
        
        Parameters:
            location (FieldGeodeticPoint<T> location): location at which parameters are requested
            date (FieldAbsoluteDate<T> date): date at which parameters are requested
        
        Returns:
            the coefficients array for VMF mapping function
        
        
        """
        ...
    @typing.overload
    def getA(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> ViennaACoefficients:
        """
        Get coefficients array for VMF mapping function.
        
          - double[0] = a :sub:`h`
          - double[1] = a :sub:`w`
        
        Specified by: getA in interface ViennaAProvider
        
        Parameters:
            location (GeodeticPoint): location at which parameters are requested
            date (AbsoluteDate): date at which parameters are requested
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class TimeSpanEstimatedModel(TroposphericModel):
    """
    Time span estimated tropospheric model.
    
    This class is closely related to package class.
    
    The difference is that it has a TimeSpanMap of EstimatedModel objects as attribute.
    
    The idea behind this model is to allow the user to design a tropospheric model that can see its physical parameters (total zenith delay) change with time, at dates chosen by the user.
    
    
    
    Since:
        10.2
    """
    DATE_BEFORE: typing.ClassVar[str] = ...
    """
    Prefix for dates before in the tropospheric parameter drivers' name.
    
    Also see:
        constant
    
    
    """
    DATE_AFTER: typing.ClassVar[str] = ...
    """
    Prefix for dates after in the tropospheric parameter drivers' name.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, model: EstimatedModel): ...
    @typing.overload
    def __init__(self, model: EstimatedModel, timeScale: org.orekit.time.TimeScale): ...
    def addTroposphericModelValidAfter(self, model: EstimatedModel, earliestValidityDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Add a EstimatedTroposphericModel entry valid after a limit date.
        
        Using addTroposphericModelValidAfter(entry, t) will make entry valid in [t, +∞[ (note the closed bracket).
        
        Parameters:
            model (EstimatedModel): EstimatedTroposphericModel entry
            earliestValidityDate (AbsoluteDate): date after which the entry is valid (must be different from all dates already used for transitions)
        
        
        """
        ...
    def addTroposphericModelValidBefore(self, model: EstimatedModel, latestValidityDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Add an EstimatedTroposphericModel entry valid before a limit date.
        
        Using addTroposphericValidBefore(entry, t) will make entry valid in ]-∞, t[ (note the open bracket).
        
        Parameters:
            model (EstimatedModel): EstimatedTroposphericModel entry
            latestValidityDate (AbsoluteDate): date before which the entry is valid (must be different from all dates already used for transitions)
        
        
        """
        ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Extract the proper parameter drivers' values from the array in input of the pathDelay method. Parameters are filtered given an input date.
        
        Parameters:
            parameters (double[]): the input parameters array
            date (AbsoluteDate): the date
        
        Returns:
            the parameters given the date
        
        """
        ...
    @typing.overload
    def extractParameters(self, parameters: typing.Union[typing.List[_extractParameters_1__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.MutableSequence[_extractParameters_1__T]:
        """
        Extract the proper parameter drivers' values from the array in input of the pathDelay method. Parameters are filtered given an input date.
        
        Parameters:
            parameters (T[]): the input parameters array
            date (FieldAbsoluteDate<T> date): the date
        
        Returns:
            the parameters given the date
        
        
        """
        ...
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span[EstimatedModel]:
        """
        Get the first Span of the tropospheric model time span map.
        
        Returns:
            the first Span of the tropospheric model time span map
        
        Since:
            11.1
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        All the parameter drivers of all Estimated models are returned in an array. Models are ordered chronologically.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getTroposphericModel(self, date: org.orekit.time.AbsoluteDate) -> EstimatedModel:
        """
        Get the EstimatedModel model valid at a date.
        
        Parameters:
            date (AbsoluteDate): the date of validity
        
        Returns:
            the EstimatedTroposphericModel model valid at date
        
        
        """
        ...
    _pathDelay_0__T = typing.TypeVar('_pathDelay_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, trackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_pathDelay_0__T], point: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_0__T], parameters: typing.Union[typing.List[_pathDelay_0__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_pathDelay_0__T]) -> FieldTroposphericDelay[_pathDelay_0__T]:
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
    def pathDelay(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> TroposphericDelay:
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

class ChaoMappingFunction(AbstractChaoMappingFunction):
    """
    Chao mapping function for radio wavelengths.
    
    Since:
        12.1
    
    Also see:
        "C. C. Chao, A model for tropospheric calibration from delay surface and radiosonde ballon measurements, 1972"
    """
    def __init__(self):
        """
        Builds a new instance.
        """
        ...

class PythonAbstractVienna(AbstractVienna):
    def __init__(self, aProvider: ViennaAProvider, gProvider: AzimuthalGradientProvider, zenithDelayProvider: TroposphericModel, utc: org.orekit.time.TimeScale):
        """
        Build a new instance.
        
        Parameters:
            aProvider (ViennaAProvider): provider for a :sub:`h` and a :sub:`w` coefficients
            gProvider (AzimuthalGradientProvider): provider for AzimuthalGradientCoefficients and
                FieldAzimuthalGradientCoefficients
            zenithDelayProvider (TroposphericModel): provider for zenith delays
            utc (TimeScale): UTC time scale
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Description copied from interface: mappingFactors This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
          - double[0] = m :sub:`h` (e) → hydrostatic mapping function
          - double[1] = m :sub:`w` (e) → wet mapping function
        
        
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
        
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            date (FieldAbsoluteDate<T> date): current date
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class RevisedChaoMappingFunction(AbstractChaoMappingFunction):
    """
    Chao mapping function for radio wavelengths.
    
    The mapping function is described in A. Estefan, O. J. Sovers 1994 paper "A Comparative Survey of Current and Proposed Tropospheric Refraction-Delay Models for DSN Radio Metric Data Calibration"
    
    Since:
        12.1
    """
    def __init__(self):
        """
        Builds a new instance.
        """
        ...

class ViennaOne(AbstractVienna):
    """
    The Vienna 1 tropospheric delay model for radio techniques. The Vienna model data are given with a time interval of 6 hours as well as on a global 2.5° * 2.0° grid. This version considered the height correction for the hydrostatic part developed by Niell, 1996.
    
    Since:
        12.1
    
    Also see:
        "Boehm, J., Werl, B., and Schuh, H., (2006), Troposhere mapping functions for GPS and very long baseline interferometry
        from European Centre for Medium-Range Weather Forecasts operational analysis data, J. Geophy. Res., Vol. 111, B02406,
        doi:10.1029/2005JB003629"
    """
    def __init__(self, aProvider: ViennaAProvider, gProvider: AzimuthalGradientProvider, zenithDelayProvider: TroposphericModel, utc: org.orekit.time.TimeScale):
        """
        Build a new instance.
        
        Parameters:
            aProvider (ViennaAProvider): provider for a :sub:`h` and a :sub:`w` coefficients
            gProvider (AzimuthalGradientProvider): provider for AzimuthalGradientCoefficients and
                FieldAzimuthalGradientCoefficients
            zenithDelayProvider (TroposphericModel): provider for zenith delays
            utc (TimeScale): UTC time scale
        
        
        """
        ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
          - double[0] = m :sub:`h` (e) → hydrostatic mapping function
          - double[1] = m :sub:`w` (e) → wet mapping function
        
        
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
        This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array having the following form:
        
          - T[0] = m :sub:`h` (e) → hydrostatic mapping function
          - T[1] = m :sub:`w` (e) → wet mapping function
        
        
        Parameters:
            trackingCoordinates (FieldTrackingCoordinates<T> trackingCoordinates): tracking coordinates of the satellite
            point (FieldGeodeticPoint<T> point): station location
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class ViennaThree(AbstractVienna):
    def __init__(self, viennaAProvider: ViennaAProvider, azimuthalGradientProvider: AzimuthalGradientProvider, troposphericModel: TroposphericModel, timeScale: org.orekit.time.TimeScale): ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, trackingCoordinates: org.orekit.utils.TrackingCoordinates, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    @typing.overload
    def mappingFactors(self, fieldTrackingCoordinates: org.orekit.utils.FieldTrackingCoordinates[_mappingFactors_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.MutableSequence[_mappingFactors_1__T]: ...


class __module_protocol__(Protocol):
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
    DummyMappingFunction: typing.Type[DummyMappingFunction]
    EstimatedModel: typing.Type[EstimatedModel]
    FieldAzimuthalGradientCoefficients: typing.Type[FieldAzimuthalGradientCoefficients]
    FieldTroposphericDelay: typing.Type[FieldTroposphericDelay]
    FieldViennaACoefficients: typing.Type[FieldViennaACoefficients]
    FixedTroposphericDelay: typing.Type[FixedTroposphericDelay]
    GlobalMappingFunctionModel: typing.Type[GlobalMappingFunctionModel]
    MariniMurray: typing.Type[MariniMurray]
    MendesPavlisModel: typing.Type[MendesPavlisModel]
    ModifiedHopfieldModel: typing.Type[ModifiedHopfieldModel]
    ModifiedSaastamoinenModel: typing.Type[ModifiedSaastamoinenModel]
    NiellMappingFunctionModel: typing.Type[NiellMappingFunctionModel]
    PythonAbstractVienna: typing.Type[PythonAbstractVienna]
    PythonAzimuthalGradientProvider: typing.Type[PythonAzimuthalGradientProvider]
    PythonTroposphereMappingFunction: typing.Type[PythonTroposphereMappingFunction]
    PythonTroposphericModel: typing.Type[PythonTroposphericModel]
    PythonViennaAProvider: typing.Type[PythonViennaAProvider]
    RevisedChaoMappingFunction: typing.Type[RevisedChaoMappingFunction]
    TimeSpanEstimatedModel: typing.Type[TimeSpanEstimatedModel]
    TroposphereMappingFunction: typing.Type[TroposphereMappingFunction]
    TroposphericDelay: typing.Type[TroposphericDelay]
    TroposphericModel: typing.Type[TroposphericModel]
    TroposphericModelUtils: typing.Type[TroposphericModelUtils]
    ViennaACoefficients: typing.Type[ViennaACoefficients]
    ViennaAProvider: typing.Type[ViennaAProvider]
    ViennaModelCoefficientsLoader: typing.Type[ViennaModelCoefficientsLoader]
    ViennaModelType: typing.Type[ViennaModelType]
    ViennaOne: typing.Type[ViennaOne]
    ViennaThree: typing.Type[ViennaThree]
    iturp834: org.orekit.models.earth.troposphere.iturp834.__module_protocol__
