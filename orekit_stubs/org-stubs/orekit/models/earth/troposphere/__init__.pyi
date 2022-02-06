import java.io
import java.lang
import java.util
import org.hipparchus
import org.orekit.bodies
import org.orekit.data
import org.orekit.time
import org.orekit.utils
import typing



class DiscreteTroposphericModel:
    """
    public interface DiscreteTroposphericModel
    
        Defines a tropospheric model, used to calculate the path delay imposed to electro-magnetic signals between an orbital
        satellite and a ground station.
    
        Models that implement this interface split the delay into hydrostatic and non-hydrostatic part:
    
        Î´ = Î´ :sub:`h` + Î´ :sub:`nh`
    
        With:
    
          - Î´ :sub:`h` = hydrostatic delay
          - Î´ :sub:`nh` = non-hydrostatic (or wet) delay
    """
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get tropospheric model parameters.
        
            Returns:
                tropospheric model parameters
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T]) -> typing.List[_getParameters_1__T]:
        """
            Get tropospheric model parameters.
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                tropospheric model parameters
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
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
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

class MappingFunction:
    """
    public interface MappingFunction
    
        Interface for mapping functions used in the tropospheric delay computation.
    """
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - double[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
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
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - T[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class TroposphericModelUtils:
    """
    public class TroposphericModelUtils extends Object
    
        Utility class for tropospheric models.
    
        Since:
            11.0
    """
    _computeHeightCorrection_1__T = typing.TypeVar('_computeHeightCorrection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeHeightCorrection(double: float, double2: float) -> float:
        """
            This method computes the height correction for the hydrostatic component of the mapping function. The formulas are given
            by Neill's paper, 1996:
        
            Niell A. E. (1996) "Global mapping functions for the atmosphere delay of radio wavelengths,Ã¢â‚¬ï¿½ J. Geophys. Res.,
            101(B2), pp. 3227Ã¢â‚¬â€œ3246, doi: 10.1029/95JB03048.
        
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
        
            Niell A. E. (1996) "Global mapping functions for the atmosphere delay of radio wavelengths,Ã¢â‚¬ï¿½ J. Geophys. Res.,
            101(B2), pp. 3227Ã¢â‚¬â€œ3246, doi: 10.1029/95JB03048.
        
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
    public static final String DEFAULT_SUPPORTED_NAMES
    
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
                :meth:`~org.orekit.data.AbstractSelfFeedingLoader.getSupportedNames`Â in
                classÂ :class:`~org.orekit.data.AbstractSelfFeedingLoader`
        
            Returns:
                the supported names.
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.feed`
        
        
        """
        ...
    def getZenithDelay(self) -> typing.List[float]:
        """
            Returns the zenith delay array.
        
              - double[0] = D :sub:`hz` â†’ zenith hydrostatic delay
              - double[1] = D :sub:`wz` â†’ zenith wet delay
        
        
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
    public enum ViennaModelType extends Enum<:class:`~org.orekit.models.earth.troposphere.ViennaModelType`>
    
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
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
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

class EstimatedTroposphericModel(DiscreteTroposphericModel):
    """
    public class EstimatedTroposphericModel extends Object implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        An estimated tropospheric model. The tropospheric delay is computed according to the formula:
    
        Î´ = Î´ :sub:`h` * m :sub:`h` + (Î´ :sub:`t` - Î´ :sub:`h` ) * m :sub:`w`
    
        With:
    
          - Î´ :sub:`h` : Tropospheric zenith hydro-static delay.
          - Î´ :sub:`t` : Tropospheric total zenith delay.
          - m :sub:`h` : Hydro-static mapping function.
          - m :sub:`w` : Wet mapping function.
    
    
        The mapping functions m :sub:`h` (e) and m :sub:`w` (e) are computed thanks to a
        :meth:`~org.orekit.models.earth.troposphere.EstimatedTroposphericModel.model` initialized by the user. The user has the
        possibility to use several mapping function models for the computations: the
        :class:`~org.orekit.models.earth.troposphere.GlobalMappingFunctionModel`, or the
        :class:`~org.orekit.models.earth.troposphere.NiellMappingFunctionModel`
    
        The tropospheric zenith delay ÃŽÂ´ :sub:`h` is computed empirically with a
        :class:`~org.orekit.models.earth.troposphere.SaastamoinenModel` while the tropospheric total zenith delay ÃŽÂ´ :sub:`t`
        is estimated as a :class:`~org.orekit.utils.ParameterDriver`
    """
    TOTAL_ZENITH_DELAY: typing.ClassVar[str] = ...
    """
    public static final String TOTAL_ZENITH_DELAY
    
        Name of the parameter of this model: the total zenith delay.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, mappingFunction: MappingFunction, double3: float): ...
    @typing.overload
    def __init__(self, mappingFunction: MappingFunction, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
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
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

class FixedTroposphericDelay(DiscreteTroposphericModel):
    """
    public class FixedTroposphericDelay extends Object implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
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
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
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
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

class GlobalMappingFunctionModel(MappingFunction):
    """
    public class GlobalMappingFunctionModel extends Object implements :class:`~org.orekit.models.earth.troposphere.MappingFunction`
    
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
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - double[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
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
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - T[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class MariniMurrayModel(DiscreteTroposphericModel):
    """
    public class MariniMurrayModel extends Object implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        The Marini-Murray tropospheric delay model for laser ranging.
    
        Also see:
            "Marini, J.W., and C.W. Murray, correction of Laser Range Tracking Data for Atmospheric Refraction at Elevations Above
            10 degrees, X-591-73-351, NASA GSFC, 1973"
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    @staticmethod
    def getStandardModel(double: float) -> 'MariniMurrayModel':
        """
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
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
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
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

class MendesPavlisModel(DiscreteTroposphericModel, MappingFunction):
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    _computeZenithDelay_1__T = typing.TypeVar('_computeZenithDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeZenithDelay(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def computeZenithDelay(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_computeZenithDelay_1__T], tArray: typing.List[_computeZenithDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeZenithDelay_1__T]) -> typing.List[_computeZenithDelay_1__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    @staticmethod
    def getStandardModel(double: float) -> 'MendesPavlisModel': ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...

class NiellMappingFunctionModel(MappingFunction):
    """
    public class NiellMappingFunctionModel extends Object implements :class:`~org.orekit.models.earth.troposphere.MappingFunction`
    
        The Niell Mapping Function model for radio wavelengths. This model is an empirical mapping function. It only needs the
        values of the station latitude, height and the date for the computations.
    
        With this model, the hydrostatic mapping function is time and latitude dependent whereas the wet mapping function is
        only latitude dependent.
    
        Also see:
            "A. E. Niell(1996), Global mapping functions for the atmosphere delay of radio wavelengths, J. Geophys. Res., 101(B2),
            pp. 3227Ã¢â‚¬â€œ3246, doi: 10.1029/95JB03048."
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - double[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
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
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - T[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...

class PythonDiscreteTroposphericModel(DiscreteTroposphericModel):
    """
    public class PythonDiscreteTroposphericModel extends Object implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get tropospheric model parameters. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.getParameters`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Returns:
                tropospheric model parameters
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T]) -> typing.List[_getParameters_1__T]:
        """
            Get tropospheric model parameters. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel.getParameters`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                tropospheric model parameters
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getParameters_F__T = typing.TypeVar('_getParameters_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getParameters_F(self, field: org.hipparchus.Field[_getParameters_F__T]) -> typing.List[_getParameters_F__T]:
        """
            Get tropospheric model parameters. Extension point for Python.
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                tropospheric model parameters
        
        
        """
        ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite. Extension point for
            Python.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                height (:class:`~org.orekit.bodies.GeodeticPoint`): the height of the station in m above sea level
                parameters (double[]): tropospheric model parameters.
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite. Redirects to
            pathDelay_TTTF(...) for Python extension
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                height (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): the height of the station in m above sea level
                parameters (T[]): tropospheric model parameters.
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...
    _pathDelay_TTTF__T = typing.TypeVar('_pathDelay_TTTF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def pathDelay_TTTF(self, t: _pathDelay_TTTF__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_TTTF__T], tArray: typing.List[_pathDelay_TTTF__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_TTTF__T]) -> _pathDelay_TTTF__T:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite. Extension point for
            Python. Called by pathDelay for this parameter set.
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                height (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): the height of the station in m above sea level
                parameters (T[]): tropospheric model parameters.
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
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

class PythonMappingFunction(MappingFunction):
    def __init__(self): ...
    def finalize(self) -> None: ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]: ...
    _mappingFactors_TTTF__T = typing.TypeVar('_mappingFactors_TTTF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def mappingFactors_TTTF(self, t: _mappingFactors_TTTF__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_TTTF__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_TTTF__T]) -> typing.List[_mappingFactors_TTTF__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class SaastamoinenModel(DiscreteTroposphericModel):
    """
    public class SaastamoinenModel extends Object implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
        The modified Saastamoinen model. Estimates the path delay imposed to electro-magnetic signals by the troposphere
        according to the formula:
    
        .. code-block: java
        
        
         Î´ = 2.277e-3 / cos z * (P + (1255 / T + 0.05) * e - B * tanÂ²
         z) + Î´R
         
        with the following input data provided to the model:
    
          - z: zenith angle
          - P: atmospheric pressure
          - T: temperature
          - e: partial pressure of water vapour
          - B, Î´R: correction terms
    
    
        The model supports custom ÃŽÂ´R correction terms to be read from a configuration file (saastamoinen-correction.txt) via
        the :class:`~org.orekit.data.DataProvidersManager`.
    
        Also see:
            "Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007"
    """
    DELTA_R_FILE_NAME: typing.ClassVar[str] = ...
    """
    public static final String DELTA_R_FILE_NAME
    
        Default file name for Î´R correction term table.
    
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
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, string: str): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getLowElevationThreshold(self) -> float:
        """
            Get the low elevation threshold value for path delay computation.
        
            Returns:
                low elevation threshold, in rad.
        
            Since:
                10.2
        
            Also see:
                null, null
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    @staticmethod
    def getStandardModel() -> 'SaastamoinenModel':
        """
            Create a new Saastamoinen model using a standard atmosphere model.
        
              - temperature: 18 degree Celsius
              - pressure: 1013.25 mbar
              - humidity: 50%
        
        
            Returns:
                a Saastamoinen model with standard environmental values
        
        
        """
        ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            The Saastamoinen model is not defined for altitudes below 0.0. for continuity reasons, we use the value for h = 0 when
            altitude is negative.
        
            There are also numerical issues for elevation angles close to zero. For continuity reasons, elevations lower than a
            threshold will use the value obtained for the threshold itself.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.GeodeticPoint`): station location
                parameters (double[]): tropospheric model parameters
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                the path delay due to the troposphere in m
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.SaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.SaastamoinenModel.setLowElevationThreshold`
        
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
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
            Also see:
                :meth:`~org.orekit.models.earth.troposphere.SaastamoinenModel.getLowElevationThreshold`,
                :meth:`~org.orekit.models.earth.troposphere.SaastamoinenModel.setLowElevationThreshold`
        
        
        """
        ...
    def setLowElevationThreshold(self, double: float) -> None:
        """
            Set the low elevation threshold value for path delay computation.
        
            Parameters:
                lowElevationThreshold (double): The new value for the threshold [rad]
        
            Since:
                10.2
        
            Also see:
                null, null
        
        
        """
        ...

class TimeSpanEstimatedTroposphericModel(DiscreteTroposphericModel):
    """
    public class TimeSpanEstimatedTroposphericModel extends Object implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
    
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
    public static final String DATE_BEFORE
    
        Prefix for dates before in the tropospheric parameter drivers' name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATE_AFTER: typing.ClassVar[str] = ...
    """
    public static final String DATE_AFTER
    
        Prefix for dates after in the tropospheric parameter drivers' name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, estimatedTroposphericModel: EstimatedTroposphericModel): ...
    @typing.overload
    def __init__(self, estimatedTroposphericModel: EstimatedTroposphericModel, timeScale: org.orekit.time.TimeScale): ...
    def addTroposphericModelValidAfter(self, estimatedTroposphericModel: EstimatedTroposphericModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a EstimatedTroposphericModel entry valid after a limit date.
        
        
            Using :code:`addTroposphericModelValidAfter(entry, t)` will make :code:`entry` valid in [t, +Ã¢Ë†Å¾[ (note the closed
            bracket).
        
            Parameters:
                model (:class:`~org.orekit.models.earth.troposphere.EstimatedTroposphericModel`): EstimatedTroposphericModel entry
                earliestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date after which the entry is valid (must be different from **all** dates already used for transitions)
        
        
        """
        ...
    def addTroposphericModelValidBefore(self, estimatedTroposphericModel: EstimatedTroposphericModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add an EstimatedTroposphericModel entry valid before a limit date.
        
        
            Using :code:`addTroposphericValidBefore(entry, t)` will make :code:`entry` valid in ]-âˆž, t[ (note the open bracket).
        
            Parameters:
                model (:class:`~org.orekit.models.earth.troposphere.EstimatedTroposphericModel`): EstimatedTroposphericModel entry
                latestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date before which the entry is valid (must be different from **all** dates already used for transitions)
        
        
        """
        ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Extract the proper parameter drivers' values from the array in input of the null method. Parameters are filtered given
            an input date.
        
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
            Extract the proper parameter drivers' values from the array in input of the null method. Parameters are filtered given
            an input date.
        
            Parameters:
                parameters (T[]): the input parameters array
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date
        
            Returns:
                the parameters given the date
        
        
        """
        ...
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span[EstimatedTroposphericModel]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTransitions(self) -> java.util.NavigableSet[org.orekit.utils.TimeSpanMap.Transition[EstimatedTroposphericModel]]: ...
    def getTroposphericModel(self, absoluteDate: org.orekit.time.AbsoluteDate) -> EstimatedTroposphericModel:
        """
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
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
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
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

class ViennaOneModel(DiscreteTroposphericModel, MappingFunction):
    """
    public class ViennaOneModel extends Object implements :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`, :class:`~org.orekit.models.earth.troposphere.MappingFunction`
    
        The Vienna1 tropospheric delay model for radio techniques. The Vienna model data are given with a time interval of 6
        hours as well as on a global 2.5Ã‚Â° * 2.0Ã‚Â° grid. This version considered the height correction for the hydrostatic
        part developed by Niell, 1996.
    
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
            This method allows the computation of the zenith hydrostatic and zenith wet delay. The resulting element is an array
            having the following form:
        
              - T[0] = D :sub:`hz` â†’ zenith hydrostatic delay
              - T[1] = D :sub:`wz` â†’ zenith wet delay
        
        
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
            This method allows the computation of the zenith hydrostatic and zenith wet delay. The resulting element is an array
            having the following form:
        
              - T[0] = D :sub:`hz` â†’ zenith hydrostatic delay
              - T[1] = D :sub:`wz` â†’ zenith wet delay
        
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the zenith hydrostatic and wet delays.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - double[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - double[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
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
            This method allows the computation of the hydrostatic and wet mapping functions. The resulting element is an array
            having the following form:
        
              - T[0] = m :sub:`h` (e) â†’ hydrostatic mapping function
              - T[1] = m :sub:`w` (e) â†’ wet mapping function
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.troposphere.MappingFunction.mappingFactors`Â in
                interfaceÂ :class:`~org.orekit.models.earth.troposphere.MappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                a two components array containing the hydrostatic and wet mapping functions.
        
        
        """
        ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
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
            Calculates the tropospheric path delay for the signal path from a ground station to a satellite.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): station location
                parameters (T[]): tropospheric model parameters
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                the path delay due to the troposphere in m
        
        
        """
        ...

class ViennaThreeModel(DiscreteTroposphericModel, MappingFunction):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], timeScale: org.orekit.time.TimeScale): ...
    _computeZenithDelay_1__T = typing.TypeVar('_computeZenithDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeZenithDelay(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def computeZenithDelay(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_computeZenithDelay_1__T], tArray: typing.List[_computeZenithDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeZenithDelay_1__T]) -> typing.List[_computeZenithDelay_1__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _mappingFactors_1__T = typing.TypeVar('_mappingFactors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactors(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def mappingFactors(self, t: _mappingFactors_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_mappingFactors_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mappingFactors_1__T]) -> typing.List[_mappingFactors_1__T]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, geodeticPoint: org.orekit.bodies.GeodeticPoint, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_1__T, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_1__T], tArray: typing.List[_pathDelay_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_1__T]) -> _pathDelay_1__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.troposphere")``.

    DiscreteTroposphericModel: typing.Type[DiscreteTroposphericModel]
    EstimatedTroposphericModel: typing.Type[EstimatedTroposphericModel]
    FixedTroposphericDelay: typing.Type[FixedTroposphericDelay]
    GlobalMappingFunctionModel: typing.Type[GlobalMappingFunctionModel]
    MappingFunction: typing.Type[MappingFunction]
    MariniMurrayModel: typing.Type[MariniMurrayModel]
    MendesPavlisModel: typing.Type[MendesPavlisModel]
    NiellMappingFunctionModel: typing.Type[NiellMappingFunctionModel]
    PythonDiscreteTroposphericModel: typing.Type[PythonDiscreteTroposphericModel]
    PythonMappingFunction: typing.Type[PythonMappingFunction]
    SaastamoinenModel: typing.Type[SaastamoinenModel]
    TimeSpanEstimatedTroposphericModel: typing.Type[TimeSpanEstimatedTroposphericModel]
    TroposphericModelUtils: typing.Type[TroposphericModelUtils]
    ViennaModelCoefficientsLoader: typing.Type[ViennaModelCoefficientsLoader]
    ViennaModelType: typing.Type[ViennaModelType]
    ViennaOneModel: typing.Type[ViennaOneModel]
    ViennaThreeModel: typing.Type[ViennaThreeModel]
