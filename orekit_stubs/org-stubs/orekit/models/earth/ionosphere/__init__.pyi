import java.io
import java.util
import org.hipparchus
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss.metric.messages.ssr.subtype
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



class IonosphericMappingFunction:
    """
    public interface IonosphericMappingFunction
    
        Interface for mapping functions used in the ionospheric delay computation.
    
        The purpose of an ionospheric mapping function is to convert the Vertical Total Electron Content (VTEC) to a Slant Total
        Electron Content (STEC) using the following formula:
    
        .. code-block: java
        
        
         STEC = VTEC * m(e)
         
    
        With m(e) the ionospheric mapping function and e the satellite elevation.
    
        Since:
            10.2
    """
    _mappingFactor_1__T = typing.TypeVar('_mappingFactor_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactor(self, double: float) -> float:
        """
            This method allows the computation of the ionospheric mapping factor.
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians.
        
            Returns:
                the ionospheric mapping factor.
        
        """
        ...
    @typing.overload
    def mappingFactor(self, t: _mappingFactor_1__T) -> _mappingFactor_1__T:
        """
            This method allows the computation of the ionospheric mapping factor.
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians.
        
            Returns:
                the ionospheric mapping factor.
        
        
        """
        ...

class IonosphericModel(java.io.Serializable):
    """
    public interface IonosphericModel extends Serializable
    
        Defines a ionospheric model, used to calculate the path delay imposed to electro-magnetic signals between an orbital
        satellite and a ground station.
    
        Since 10.0, this interface can be used for models that aspire to estimate ionospheric parameters.
    
        Since:
            7.1
    """
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get ionospheric model parameters.
        
            Returns:
                ionospheric model parameters
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T]) -> typing.List[_getParameters_1__T]:
        """
            Get ionospheric model parameters.
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                ionospheric model parameters
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_1__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...

class KlobucharIonoCoefficientsLoader(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader):
    """
    public class KlobucharIonoCoefficientsLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.data.DataLoader`
    
        Loads Klobuchar-Style ionospheric coefficients a given input stream. A stream contains the alphas and betas coefficient
        for a given day.
    
        They are obtained from University of Bern Astronomical Institute ftp. Find more on the files at the `Astronomical
        Institute site
        <http://www.aiub.unibe.ch/research/code___analysis_center/klobuchar_style_ionospheric_coefficients/index_eng.html>`.
    
        The files are UNIX-style compressed (.Z) files. They have to be extracted to UTF-8 text files before being read by this
        loader.
    
        After extraction, it is assumed they are named CGIMDDD0.YYN where DDD and YY substitute day of year and 2-digits year.
    
        The format is always the same, with and example shown below. Only the last 2 lines contains the Klobuchar coefficients.
    
        Example:
    
        .. code-block: java
        
        
              2              NAVIGATION DATA     GPS                 RINEX VERSION / TYPE
         INXFIT V5.3         AIUB                06-JAN-17 09:12     PGM / RUN BY / DATE
         CODE'S KLOBUCHAR-STYLE IONOSPHERE MODEL FOR DAY 001, 2017   COMMENT
         Contact address: code(at)aiub.unibe.ch                      COMMENT
         Data archive:    ftp.unibe.ch/aiub/CODE/                    COMMENT
                          www.aiub.unibe.ch/download/CODE/           COMMENT
         WARNING: USE DATA AT SOUTHERN POLAR REGION WITH CARE        COMMENT
             1.2821D-08 -9.6222D-09 -3.5982D-07 -6.0901D-07          ION ALPHA
             1.0840D+05 -1.3197D+05 -2.6331D+05  4.0570D+05          ION BETA
                                                                     END OF HEADER
         
    
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
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getAlpha(self) -> typing.List[float]:
        """
            Returns the alpha coefficients array.
        
            Returns:
                the alpha coefficients array
        
        
        """
        ...
    def getBeta(self) -> typing.List[float]:
        """
            Returns the beta coefficients array.
        
            Returns:
                the beta coefficients array
        
        
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
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    @typing.overload
    def loadKlobucharIonosphericCoefficients(self) -> None:
        """
            Load the data using supported names .
        """
        ...
    @typing.overload
    def loadKlobucharIonosphericCoefficients(self, dateComponents: org.orekit.time.DateComponents) -> None:
        """
            Load the data for a given day.
        
            Parameters:
                dateComponents (:class:`~org.orekit.time.DateComponents`): day given but its DateComponents
        
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
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

class EstimatedIonosphericModel(IonosphericModel):
    """
    public class EstimatedIonosphericModel extends Object implements :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
    
        An estimated ionospheric model. The ionospheric delay is computed according to the formula:
    
        40.3 Î´ = -------- * STEC with, STEC = VTEC * F(elevation) fÂ²
        With:
    
          - f: The frequency of the signal in Hz.
          - STEC: The Slant Total Electron Content in TECUnits.
          - VTEC: The Vertical Total Electron Content in TECUnits.
          - F(elevation): A mapping function which depends on satellite elevation.
    
        The VTEC is estimated as a :class:`~org.orekit.utils.ParameterDriver`
    
        Since:
            10.2
    
        Also see:
            :meth:`~serialized`
    """
    VERTICAL_TOTAL_ELECTRON_CONTENT: typing.ClassVar[str] = ...
    """
    public static final String VERTICAL_TOTAL_ELECTRON_CONTENT
    
        Name of the parameter of this model: the Vertical Total Electron Content.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, ionosphericMappingFunction: IonosphericMappingFunction, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_3__T = typing.TypeVar('_pathDelay_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, double: float, double2: float, doubleArray: typing.List[float]) -> float:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            The path delay is computed for any elevation angle.
        
            Parameters:
                elevation (double): elevation of the satellite in radians
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def pathDelay(self, t: _pathDelay_2__T, double: float, tArray: typing.List[_pathDelay_2__T]) -> _pathDelay_2__T:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            The path delay is computed for any elevation angle.
        
            Parameters:
                elevation (T): elevation of the satellite in radians
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_3__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_3__T]) -> _pathDelay_3__T: ...

class GlobalIonosphereMapModel(org.orekit.data.AbstractSelfFeedingLoader, IonosphericModel):
    """
    public class GlobalIonosphereMapModel extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
    
        Global Ionosphere Map (GIM) model. The ionospheric delay is computed according to the formulas:
    
        .. code-block: java
        
        
                   40.3
            Î´ =  --------  *  STEC      with, STEC = VTEC * F(elevation)
                    fÂ²
         
        With:
    
          - f: The frequency of the signal in Hz.
          - STEC: The Slant Total Electron Content in TECUnits.
          - VTEC: The Vertical Total Electron Content in TECUnits.
          - F(elevation): A mapping function which depends on satellite elevation.
    
        The VTEC is read from a IONEX file. A stream contains, for a given day, the values of the TEC for each hour of the day.
        Values are given on a global 2.5Ã‚Â° x 5.0Ã‚Â° (latitude x longitude) grid.
    
        A bilinear interpolation is performed the case of the user initialize the latitude and the longitude with values that
        are not contained in the stream.
    
        A temporal interpolation is also performed to compute the VTEC at the desired date.
    
        IONEX files are obtained from The Crustal Dynamics Data Information System.
    
        The files have to be extracted to UTF-8 text files before being read by this loader.
    
        Example of file:
    
        .. code-block: java
        
        
              1.0            IONOSPHERE MAPS     GPS                 IONEX VERSION / TYPE
         BIMINX V5.3         AIUB                16-JAN-19 07:26     PGM / RUN BY / DATE
         BROADCAST IONOSPHERE MODEL FOR DAY 015, 2019                COMMENT
           2019     1    15     0     0     0                        EPOCH OF FIRST MAP
           2019     1    16     0     0     0                        EPOCH OF LAST MAP
           3600                                                      INTERVAL
             25                                                      # OF MAPS IN FILE
           NONE                                                      MAPPING FUNCTION
              0.0                                                    ELEVATION CUTOFF
                                                                     OBSERVABLES USED
           6371.0                                                    BASE RADIUS
              2                                                      MAP DIMENSION
            350.0 350.0   0.0                                        HGT1 / HGT2 / DHGT
             87.5 -87.5  -2.5                                        LAT1 / LAT2 / DLAT
           -180.0 180.0   5.0                                        LON1 / LON2 / DLON
             -1                                                      EXPONENT
         TEC/RMS values in 0.1 TECU; 9999, if no value available     COMMENT
                                                                     END OF HEADER
              1                                                      START OF TEC MAP
           2019     1    15     0     0     0                        EPOCH OF CURRENT MAP
             87.5-180.0 180.0   5.0 350.0                            LAT/LON1/LON2/DLON/H
            92   92   92   92   92   92   92   92   92   92   92   92   92   92   92   92
            92   92   92   92   92   92   92   92   92   92   92   92   92   92   92   92
            92   92   92   92   92   92   92   92   92   92   92   92   92   92   92   92
            92   92   92   92   92   92   92   92   92   92   92   92   92   92   92   92
            92   92   92   92   92   92   92   92   92
            ...
         
    
        Also see:
            "Schaer, S., W. Gurtner, and J. Feltens, 1998, IONEX: The IONosphere Map EXchange Format Version 1, February 25, 1998,
            Proceedings of the IGS AC Workshop Darmstadt, Germany, February 9Ã¢â‚¬â€œ11, 1998", :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getTEC_1__T = typing.TypeVar('_getTEC_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTEC(self, absoluteDate: org.orekit.time.AbsoluteDate, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> float:
        """
            Computes the Total Electron Content (TEC) at a given date by performing a temporal interpolation with the two closest
            date in the IONEX file.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                recPoint (:class:`~org.orekit.bodies.GeodeticPoint`): geodetic point of receiver/station
        
            Returns:
                the TEC after a temporal interpolation, in TECUnits
        
        """
        ...
    @typing.overload
    def getTEC(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTEC_1__T], geodeticPoint: org.orekit.bodies.GeodeticPoint) -> _getTEC_1__T:
        """
            Computes the Total Electron Content (TEC) at a given date by performing a temporal interpolation with the two closest
            date in the IONEX file.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                recPoint (:class:`~org.orekit.bodies.GeodeticPoint`): geodetic point of receiver/station
        
            Returns:
                the TEC after a temporal interpolation, in TECUnits
        
        
        """
        ...
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_3__T = typing.TypeVar('_pathDelay_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            The path delay can be computed for any elevation angle.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                geo (:class:`~org.orekit.bodies.GeodeticPoint`): geodetic point of receiver/station
                elevation (double): elevation of the satellite in radians
                frequency (double): frequency of the signal in Hz
        
            Returns:
                the path delay due to the ionosphere in m
        
            Description copied from interface: 
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, absoluteDate: org.orekit.time.AbsoluteDate, geodeticPoint: org.orekit.bodies.GeodeticPoint, double: float, double2: float) -> float: ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_2__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_2__T]) -> _pathDelay_2__T:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            The path delay can be computed for any elevation angle.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                geo (:class:`~org.orekit.bodies.GeodeticPoint`): geodetic point of receiver/station
                elevation (T): elevation of the satellite in radians
                frequency (double): frequency of the signal in Hz
        
            Returns:
                the path delay due to the ionosphere in m
        
            Description copied from interface: 
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_3__T], geodeticPoint: org.orekit.bodies.GeodeticPoint, t: _pathDelay_3__T, double: float) -> _pathDelay_3__T: ...

class KlobucharIonoModel(IonosphericModel):
    """
    public class KlobucharIonoModel extends Object implements :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
    
        Klobuchar ionospheric delay model. Klobuchar ionospheric delay model is designed as a GNSS correction model. The
        parameters for the model are provided by the GPS satellites in their broadcast messsage. This model is based on the
        assumption the electron content is concentrated in 350 km layer. The delay refers to L1 (1575.42 MHz). If the delay is
        sought for L2 (1227.60 MHz), multiply the result by 1.65 (Klobuchar, 1996). More generally, since ionospheric delay is
        inversely proportional to the square of the signal frequency f, to adapt this model to other GNSS frequencies f,
        multiply by (L1 / f)^2. References: ICD-GPS-200, Rev. C, (1997), pp. 125-128 Klobuchar, J.A., Ionospheric time-delay
        algorithm for single-frequency GPS users, IEEE Transactions on Aerospace and Electronic Systems, Vol. 23, No. 3, May
        1987 Klobuchar, J.A., "Ionospheric Effects on GPS", Global Positioning System: Theory and Applications, 1996,
        pp.513-514, Parkinson, Spilker.
    
        Since:
            7.1
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], timeScale: org.orekit.time.TimeScale): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_3__T = typing.TypeVar('_pathDelay_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            The path delay is computed for any elevation angle.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                geo (:class:`~org.orekit.bodies.GeodeticPoint`): geodetic point of receiver/station
                elevation (double): elevation of the satellite in radians
                azimuth (double): azimuth of the satellite in radians
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, absoluteDate: org.orekit.time.AbsoluteDate, geodeticPoint: org.orekit.bodies.GeodeticPoint, double: float, double2: float, double3: float, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_2__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_2__T]) -> _pathDelay_2__T:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            The path delay is computed for any elevation angle.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                geo (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> geo): geodetic point of receiver/station
                elevation (T): elevation of the satellite in radians
                azimuth (T): azimuth of the satellite in radians
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_3__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_pathDelay_3__T], t: _pathDelay_3__T, t2: _pathDelay_3__T, double: float, tArray: typing.List[_pathDelay_3__T]) -> _pathDelay_3__T: ...

class NeQuickModel(IonosphericModel):
    """
    public class NeQuickModel extends Object implements :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
    
        NeQuick ionospheric delay model.
    
        Since:
            10.1
    
        Also see:
            "European Union (2016). European GNSS (Galileo) Open Service-Ionospheric Correction Algorithm for Galileo Single
            Frequency Users. 1.2.", :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], timeScale: org.orekit.time.TimeScale): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float:
        """
            Description copied from interface: 
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_1__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Description copied from interface: 
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...
    _stec_1__T = typing.TypeVar('_stec_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def stec(self, absoluteDate: org.orekit.time.AbsoluteDate, geodeticPoint: org.orekit.bodies.GeodeticPoint, geodeticPoint2: org.orekit.bodies.GeodeticPoint) -> float:
        """
            This method allows the computation of the Stant Total Electron Content (STEC).
        
            This method follows the Gauss algorithm exposed in section 2.5.8.2.8 of the reference document.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                recP (:class:`~org.orekit.bodies.GeodeticPoint`): receiver position
                satP (:class:`~org.orekit.bodies.GeodeticPoint`): satellite position
        
            Returns:
                the STEC in TECUnits
        
        """
        ...
    @typing.overload
    def stec(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_stec_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_stec_1__T], fieldGeodeticPoint2: org.orekit.bodies.FieldGeodeticPoint[_stec_1__T]) -> _stec_1__T:
        """
            This method allows the computation of the Stant Total Electron Content (STEC).
        
            This method follows the Gauss algorithm exposed in section 2.5.8.2.8 of the reference document.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                recP (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> recP): receiver position
                satP (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> satP): satellite position
        
            Returns:
                the STEC in TECUnits
        
        
        """
        ...

class PythonIonosphericMappingFunction(IonosphericMappingFunction):
    """
    public class PythonIonosphericMappingFunction extends Object implements :class:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _mappingFactor_1__T = typing.TypeVar('_mappingFactor_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactor(self, double: float) -> float:
        """
            This method allows the computation of the ionospheric mapping factor.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction.mappingFactor`Â in
                interfaceÂ :class:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians.
        
            Returns:
                the ionospheric mapping factor.
        
        """
        ...
    @typing.overload
    def mappingFactor(self, t: _mappingFactor_1__T) -> _mappingFactor_1__T:
        """
            This method allows the computation of the ionospheric mapping factor.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction.mappingFactor`Â in
                interfaceÂ :class:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians.
        
            Returns:
                the ionospheric mapping factor.
        
        
        """
        ...
    _mappingFactor_T__T = typing.TypeVar('_mappingFactor_T__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def mappingFactor_T(self, t: _mappingFactor_T__T) -> _mappingFactor_T__T:
        """
            This method allows the computation of the ionospheric mapping factor.
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians.
        
            Returns:
                the ionospheric mapping factor.
        
        
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

class PythonIonosphericModel(IonosphericModel):
    """
    public class PythonIonosphericModel extends Object implements :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get ionospheric model parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericModel.getParameters`Â in
                interfaceÂ :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Returns:
                ionospheric model parameters
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T]) -> typing.List[_getParameters_1__T]:
        """
            Get ionospheric model parameters.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericModel.getParameters`Â in
                interfaceÂ :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                ionospheric model parameters
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getParameters_F__T = typing.TypeVar('_getParameters_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getParameters_F(self, field: org.hipparchus.Field[_getParameters_F__T]) -> typing.List[_getParameters_F__T]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_1__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...
    _pathDelay_FTdT__T = typing.TypeVar('_pathDelay_FTdT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def pathDelay_FTdT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_FTdT__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_FTdT__T]) -> _pathDelay_FTdT__T: ...
    def pathDelay_STdd(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float: ...
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

class SingleLayerModelMappingFunction(IonosphericMappingFunction):
    """
    public class SingleLayerModelMappingFunction extends Object implements :class:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction`
    
        Single Layer Model (SLM) ionospheric mapping function.
    
        The SLM mapping function assumes a single ionospheric layer with a constant height for the computation of the mapping
        factor.
    
        Since:
            10.2
    
        Also see:
            "N. YaÃ¢â‚¬â„¢acob, M. Abdullah and M. Ismail, Determination of the GPS total electron content using single layer model
            (SLM) ionospheric mapping function, in International Journal of Computer Science and Network Security, vol. 8, no. 9,
            pp. 154-160, 2008."
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    _mappingFactor_1__T = typing.TypeVar('_mappingFactor_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mappingFactor(self, double: float) -> float:
        """
            This method allows the computation of the ionospheric mapping factor.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction.mappingFactor`Â in
                interfaceÂ :class:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction`
        
            Parameters:
                elevation (double): the elevation of the satellite, in radians.
        
            Returns:
                the ionospheric mapping factor.
        
        """
        ...
    @typing.overload
    def mappingFactor(self, t: _mappingFactor_1__T) -> _mappingFactor_1__T:
        """
            This method allows the computation of the ionospheric mapping factor.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction.mappingFactor`Â in
                interfaceÂ :class:`~org.orekit.models.earth.ionosphere.IonosphericMappingFunction`
        
            Parameters:
                elevation (T): the elevation of the satellite, in radians.
        
            Returns:
                the ionospheric mapping factor.
        
        
        """
        ...

class SsrVtecIonosphericModel(IonosphericModel):
    """
    public class SsrVtecIonosphericModel extends Object implements :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
    
        Ionospheric model based on SSR IM201 message.
    
        Within this message, the ionospheric VTEC is provided using spherical harmonic expansions. For a given ionospheric
        layer, the slant TEC value is calculated using the satellite elevation and the height of the corresponding layer. The
        total slant TEC is computed by the sum of the individual slant TEC for each layer.
    
        Since:
            11.0
    
        Also see:
            "IGS State Space Representation (SSR) Format, Version 1.00, October 2020.", :meth:`~serialized`
    """
    def __init__(self, ssrIm201: org.orekit.gnss.metric.messages.ssr.subtype.SsrIm201): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.List[float]) -> float:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_1__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.List[_pathDelay_1__T]) -> _pathDelay_1__T:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0Ã‚Â° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                 in interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.ionosphere")``.

    EstimatedIonosphericModel: typing.Type[EstimatedIonosphericModel]
    GlobalIonosphereMapModel: typing.Type[GlobalIonosphereMapModel]
    IonosphericMappingFunction: typing.Type[IonosphericMappingFunction]
    IonosphericModel: typing.Type[IonosphericModel]
    KlobucharIonoCoefficientsLoader: typing.Type[KlobucharIonoCoefficientsLoader]
    KlobucharIonoModel: typing.Type[KlobucharIonoModel]
    NeQuickModel: typing.Type[NeQuickModel]
    PythonIonosphericMappingFunction: typing.Type[PythonIonosphericMappingFunction]
    PythonIonosphericModel: typing.Type[PythonIonosphericModel]
    SingleLayerModelMappingFunction: typing.Type[SingleLayerModelMappingFunction]
    SsrVtecIonosphericModel: typing.Type[SsrVtecIonosphericModel]
