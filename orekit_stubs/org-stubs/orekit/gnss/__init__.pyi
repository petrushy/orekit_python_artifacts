import java.io
import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.euclidean.twod
import org.orekit.bodies
import org.orekit.data
import org.orekit.estimation.measurements.gnss
import org.orekit.gnss.antenna
import org.orekit.gnss.attitude
import org.orekit.gnss.clock
import org.orekit.gnss.metric
import org.orekit.gnss.navigation
import org.orekit.propagation
import org.orekit.propagation.analytical.gnss.data
import org.orekit.time
import org.orekit.utils
import typing



class AppliedDCBS:
    """
    public class AppliedDCBS extends Object
    
        Corrections of Differential Code Biases (DCBs) applied. Contains information on the programs used to correct the
        observations in RINEX or clock files for differential code biases.
    """
    def __init__(self, satelliteSystem: 'SatelliteSystem', string: str, string2: str): ...
    def getProgDCBS(self) -> str:
        """
            Get the program name used to apply DCBs.
        
            Returns:
                Program name used to apply DCBs
        
        
        """
        ...
    def getSatelliteSystem(self) -> 'SatelliteSystem':
        """
            Get the satellite system.
        
            Returns:
                satellite system
        
        
        """
        ...
    def getSourceDCBS(self) -> str:
        """
            Get the source of corrections.
        
            Returns:
                Source of corrections (URL)
        
        
        """
        ...

class AppliedPCVS:
    """
    public class AppliedPCVS extends Object
    
        Corrections of antenna phase center variations (PCVs) applied. Contains information on the programs used to correct the
        observations in RINEX or clock files for antenna phase center variations.
    """
    def __init__(self, satelliteSystem: 'SatelliteSystem', string: str, string2: str): ...
    def getProgPCVS(self) -> str:
        """
            Get the program name used to apply PCVs.
        
            Returns:
                Program name used to apply PCVs
        
        
        """
        ...
    def getSatelliteSystem(self) -> 'SatelliteSystem':
        """
            Get the satellite system.
        
            Returns:
                satellite system
        
        
        """
        ...
    def getSourcePCVS(self) -> str:
        """
            Get the source of corrections.
        
            Returns:
                Source of corrections (URL)
        
        
        """
        ...

class CombinedObservationData:
    """
    public class CombinedObservationData extends Object
    
        Combined observation data.
    
        Since:
            10.1
    """
    def __init__(self, combinationType: org.orekit.estimation.measurements.gnss.CombinationType, measurementType: 'MeasurementType', double: float, double2: float, list: java.util.List['ObservationData']): ...
    def getCombinationType(self) -> org.orekit.estimation.measurements.gnss.CombinationType:
        """
            Get the type of the combination of measurements used to build the instance.
        
            Returns:
                the combination of measurements type
        
        
        """
        ...
    def getCombinedMHzFrequency(self) -> float:
        """
            Get the value of the combined frequency in MHz.
        
            For the single frequency combinations, this method returns the common frequency of both measurements.
        
            Returns:
                value of the combined frequency in MHz
        
        
        """
        ...
    def getMeasurementType(self) -> 'MeasurementType':
        """
            Get the measurement type.
        
            Returns:
                measurement type
        
        
        """
        ...
    def getUsedObservationData(self) -> java.util.List['ObservationData']: ...
    def getValue(self) -> float:
        """
            Get the combined observed value.
        
            Returns:
                observed value (may be :code:`Double.NaN` if observation not available)
        
        
        """
        ...

class CombinedObservationDataSet(org.orekit.time.TimeStamped):
    """
    public class CombinedObservationDataSet extends Object implements :class:`~org.orekit.time.TimeStamped`
    
        Combined observation data set.
    
        Since:
            10.1
    """
    def __init__(self, rinexObservationHeader: 'RinexObservationHeader', satelliteSystem: 'SatelliteSystem', int: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, list: java.util.List[CombinedObservationData]): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getHeader(self) -> 'RinexObservationHeader':
        """
            Get the Rinex header associated with this data set.
        
            Returns:
                Rinex header associated with this data set
        
            Since:
                9.3
        
        
        """
        ...
    def getObservationData(self) -> java.util.List[CombinedObservationData]: ...
    def getPrnNumber(self) -> int:
        """
            Get PRN number.
        
            Returns:
                PRN number of the observed satellite
        
        
        """
        ...
    def getRcvrClkOffset(self) -> float:
        """
            Get receiver clock offset.
        
            Returns:
                receiver clock offset (it is optional, may be 0)
        
        
        """
        ...
    def getSatelliteSystem(self) -> 'SatelliteSystem':
        """
            Get Satellite System.
        
            Returns:
                satellite system of observed satellite
        
        
        """
        ...

class DOP:
    """
    public class DOP extends Object
    
        This class is a container for the result of a single DOP computation.
    
        Since:
            8.0
    
        Also see:
            `Dilution of precision <http://en.wikipedia.org/wiki/Dilution_of_precision_%28GPS%29>`
    """
    def __init__(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate: org.orekit.time.AbsoluteDate, int: int, double: float, double2: float, double3: float, double4: float, double5: float): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the calculation date of the DOP.
        
            Returns:
                the calculation date of the DOP
        
        
        """
        ...
    def getGdop(self) -> float:
        """
            Gets the geometric dilution of precision.
        
            Returns:
                the GDOP
        
        
        """
        ...
    def getGnssNb(self) -> int:
        """
            Gets the number of GNSS satellites taken into account for DOP computation.
        
            Returns:
                the number of GNSS satellites taken into account for DOP computation
        
        
        """
        ...
    def getHdop(self) -> float:
        """
            Gets the horizontal dilution of precision.
        
            Returns:
                the HDOP
        
        
        """
        ...
    def getLocation(self) -> org.orekit.bodies.GeodeticPoint:
        """
            Gets the location with respect to the Earth where DOP was calculated.
        
            Returns:
                the location with respect to the Earth where DOP was calculated
        
        
        """
        ...
    def getPdop(self) -> float:
        """
            Gets the position dilution of precision.
        
            Returns:
                the PDOP
        
        
        """
        ...
    def getTdop(self) -> float:
        """
            Gets the time dilution of precision.
        
            Returns:
                the TDOP
        
        
        """
        ...
    def getVdop(self) -> float:
        """
            Gets the vertical dilution of precision.
        
            Returns:
                the VDOP
        
        
        """
        ...

class DOPComputer:
    """
    public class DOPComputer extends Object
    
        This class aims at computing the dilution of precision.
    
        Since:
            8.0
    
        Also see:
            `Dilution of precision <http://en.wikipedia.org/wiki/Dilution_of_precision_%28GPS%29>`
    """
    DOP_MIN_ELEVATION: typing.ClassVar[float] = ...
    """
    public static final double DOP_MIN_ELEVATION
    
        Minimum elevation : 0Â°.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def compute(self, absoluteDate: org.orekit.time.AbsoluteDate, list: java.util.List[org.orekit.propagation.Propagator]) -> DOP: ...
    @staticmethod
    def create(oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> 'DOPComputer':
        """
            Creates a DOP computer for one location.
        
            A minimum elevation of 0Â° is taken into account to compute visibility between the location and the GNSS spacecrafts.
        
            Parameters:
                shape (:class:`~org.orekit.bodies.OneAxisEllipsoid`): the body shape on which the location is defined
                location (:class:`~org.orekit.bodies.GeodeticPoint`): the point of interest
        
            Returns:
                a configured DOP computer
        
        
        """
        ...
    def getElevationMask(self) -> org.orekit.utils.ElevationMask:
        """
            Get the elevation mask.
        
            Returns:
                the elevation mask
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
            Get the minimum elevation.
        
            Returns:
                the minimum elevation (rad)
        
        
        """
        ...
    def withElevationMask(self, elevationMask: org.orekit.utils.ElevationMask) -> 'DOPComputer':
        """
            Set the elevation mask.
        
            This will override the min elevation if it has been configured as such previously.
        
            Parameters:
                newElevationMask (:class:`~org.orekit.utils.ElevationMask`): elevation mask to use for the computation
        
            Returns:
                a new detector with updated configuration (the instance is not changed)
        
            Also see:
                :meth:`~org.orekit.gnss.DOPComputer.getElevationMask`
        
        
        """
        ...
    def withMinElevation(self, double: float) -> 'DOPComputer':
        """
            Set the minimum elevation.
        
            This will override an elevation mask if it has been configured as such previously.
        
            Parameters:
                newMinElevation (double): minimum elevation for visibility (rad)
        
            Returns:
                a new DOP computer with updated configuration (the instance is not changed)
        
            Also see:
                :meth:`~org.orekit.gnss.DOPComputer.getMinElevation`
        
        
        """
        ...

class Frequency(java.lang.Enum['Frequency']):
    """
    public enum Frequency extends Enum<:class:`~org.orekit.gnss.Frequency`>
    
        Enumerate for GNSS frequencies.
    
        Since:
            9.2
    """
    G01: typing.ClassVar['Frequency'] = ...
    G02: typing.ClassVar['Frequency'] = ...
    G05: typing.ClassVar['Frequency'] = ...
    R01: typing.ClassVar['Frequency'] = ...
    R02: typing.ClassVar['Frequency'] = ...
    R03: typing.ClassVar['Frequency'] = ...
    R04: typing.ClassVar['Frequency'] = ...
    R06: typing.ClassVar['Frequency'] = ...
    E01: typing.ClassVar['Frequency'] = ...
    E05: typing.ClassVar['Frequency'] = ...
    E07: typing.ClassVar['Frequency'] = ...
    E08: typing.ClassVar['Frequency'] = ...
    E06: typing.ClassVar['Frequency'] = ...
    C01: typing.ClassVar['Frequency'] = ...
    C02: typing.ClassVar['Frequency'] = ...
    C06: typing.ClassVar['Frequency'] = ...
    C07: typing.ClassVar['Frequency'] = ...
    B01: typing.ClassVar['Frequency'] = ...
    B02: typing.ClassVar['Frequency'] = ...
    B03: typing.ClassVar['Frequency'] = ...
    J01: typing.ClassVar['Frequency'] = ...
    J02: typing.ClassVar['Frequency'] = ...
    J05: typing.ClassVar['Frequency'] = ...
    J06: typing.ClassVar['Frequency'] = ...
    I05: typing.ClassVar['Frequency'] = ...
    I09: typing.ClassVar['Frequency'] = ...
    S01: typing.ClassVar['Frequency'] = ...
    S05: typing.ClassVar['Frequency'] = ...
    F0: typing.ClassVar[float] = ...
    """
    public static final double F0
    
        Common frequency F0 in MHz (10.23 MHz).
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getMHzFrequency(self) -> float:
        """
            Get the value of the frequency in MHz.
        
            Returns:
                value of the frequency in MHz
        
            Also see:
                :meth:`~org.orekit.gnss.Frequency.F0`, :meth:`~org.orekit.gnss.Frequency.getRatio`,
                :meth:`~org.orekit.gnss.Frequency.getWavelength`
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the RINEX name for the frequency.
        
            Returns:
                RINEX name for the frequency
        
        
        """
        ...
    def getRatio(self) -> float:
        """
            Get the ratio f/f0, where :meth:`~org.orekit.gnss.Frequency.F0` is the common frequency.
        
            Returns:
                ratio f/f0, where :meth:`~org.orekit.gnss.Frequency.F0` is the common frequency
        
            Also see:
                :meth:`~org.orekit.gnss.Frequency.F0`, :meth:`~org.orekit.gnss.Frequency.getMHzFrequency`
        
        
        """
        ...
    def getSatelliteSystem(self) -> 'SatelliteSystem':
        """
            Get the satellite system for which this frequency is defined.
        
            Returns:
                satellite system for which this frequency is defined
        
        
        """
        ...
    def getWavelength(self) -> float:
        """
            Get the wavelength in meters.
        
            Returns:
                wavelength in meters
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.gnss.Frequency.getMHzFrequency`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Frequency':
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
    def values() -> typing.List['Frequency']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (Frequency c : Frequency.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class HatanakaCompressFilter(org.orekit.data.DataFilter):
    """
    public class HatanakaCompressFilter extends Object implements :class:`~org.orekit.data.DataFilter`
    
        Decompression filter for Hatanaka compressed RINEX files.
    
        Since:
            10.1
    
        Also see:
            `A Compression Format and Tools for GNSS Observation Data
            <http://cedadocs.ceda.ac.uk/1254/1/Hatanaka%5C_compressed%5C_format%5C_help.pdf>`
    """
    def __init__(self): ...
    def filter(self, dataSource: org.orekit.data.DataSource) -> org.orekit.data.DataSource:
        """
            Filter the data source.
        
            Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form
            base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
            A filter must *never* :meth:`~org.orekit.data.DataSource.Opener.openStreamOnce` the :class:`~org.orekit.data.DataSource`
            by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it
            is the upper layer that will decide to open (or not) the returned value and that a :class:`~org.orekit.data.DataSource`
            can be opened only once; this is the core principle of lazy-opening provided by :class:`~org.orekit.data.DataSource`.
        
            Beware that as the :class:`~org.orekit.data.DataProvidersManager` will attempt to pile all filters in a stack as long as
            their implementation of this method returns a value different from the :code:`original` parameter. This implies that the
            filter, *must* perform some checks to see if it must be applied or not. If for example there is a need for a deciphering
            filter to be applied once to all data, then the filter should for example check for a suffix in the
            :meth:`~org.orekit.data.DataSource.getName` and create a new filtered :class:`~org.orekit.data.DataSource` instance
            *only* if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a
            filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering
            filters being built, until a stack overflow or memory exhaustion exception occurs.
        
            Specified by:
                :meth:`~org.orekit.data.DataFilter.filter` in interface :class:`~org.orekit.data.DataFilter`
        
            Parameters:
                original (:class:`~org.orekit.data.DataSource`): original data source
        
            Returns:
                filtered data source, or :code:`original` if this filter does not apply to this data source
        
        
        """
        ...

class MeasurementType(java.lang.Enum['MeasurementType']):
    """
    public enum MeasurementType extends Enum<:class:`~org.orekit.gnss.MeasurementType`>
    
        Enumerate for measurement type.
    
        Since:
            9.2
    """
    PSEUDO_RANGE: typing.ClassVar['MeasurementType'] = ...
    CARRIER_PHASE: typing.ClassVar['MeasurementType'] = ...
    DOPPLER: typing.ClassVar['MeasurementType'] = ...
    SIGNAL_STRENGTH: typing.ClassVar['MeasurementType'] = ...
    COMBINED_RANGE_PHASE: typing.ClassVar['MeasurementType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'MeasurementType':
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
    def values() -> typing.List['MeasurementType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (MeasurementType c : MeasurementType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ObservationData:
    """
    public class ObservationData extends Object
    
        Observation Data.
    
        Since:
            9.2
    """
    def __init__(self, observationType: 'ObservationType', double: float, int: int, int2: int): ...
    def getLossOfLockIndicator(self) -> int:
        """
            Get the Loss of Lock Indicator.
        
            Returns:
                Loss of Lock Indicator
        
        
        """
        ...
    def getObservationType(self) -> 'ObservationType':
        """
            Get the observation type.
        
            Returns:
                observation type
        
        
        """
        ...
    def getSignalStrength(self) -> int:
        """
            Get the signal strength.
        
            Returns:
                signal strength
        
        
        """
        ...
    def getValue(self) -> float:
        """
            Get the observed value.
        
            Returns:
                observed value (may be :code:`Double.NaN` if observation not available)
        
        
        """
        ...

class ObservationDataSet(org.orekit.time.TimeStamped):
    """
    public class ObservationDataSet extends Object implements :class:`~org.orekit.time.TimeStamped`
    
        Observation Data set.
    
        Since:
            9.2
    """
    def __init__(self, rinexObservationHeader: 'RinexObservationHeader', satelliteSystem: 'SatelliteSystem', int: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, list: java.util.List[ObservationData]): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getHeader(self) -> 'RinexObservationHeader':
        """
            Get the Rinex header associated with this data set.
        
            Returns:
                Rinex header associated with this data set
        
            Since:
                9.3
        
        
        """
        ...
    def getObservationData(self) -> java.util.List[ObservationData]: ...
    def getPrnNumber(self) -> int:
        """
            Get PRN number.
        
            Returns:
                PRN number of the observed satellite
        
        
        """
        ...
    def getRcvrClkOffset(self) -> float:
        """
            Get receiver clock offset.
        
            Returns:
                receiver clock offset (it is optional, may be 0)
        
        
        """
        ...
    def getSatelliteSystem(self) -> 'SatelliteSystem':
        """
            Get Satellite System.
        
            Returns:
                satellite system of observed satellite
        
        
        """
        ...

class ObservationType(java.lang.Enum['ObservationType']):
    """
    public enum ObservationType extends Enum<:class:`~org.orekit.gnss.ObservationType`>
    
        Enumerate for all the Observation Types for Rinex 2 and 3. For Rinex 2, there is an two-character enumerate composed of
        the Observation Code (C,P,L,D,S) and the Frequency code (1,2,5,6,7,8). For Rinex 3 there is a three-character enumerate
        composed of the Observation Code (C,L,D,S), the frequency code (1,2,5,6,7,8) and a final attribute depending on the
        tracking mode or channel.
    """
    C1: typing.ClassVar['ObservationType'] = ...
    C2: typing.ClassVar['ObservationType'] = ...
    C5: typing.ClassVar['ObservationType'] = ...
    C6: typing.ClassVar['ObservationType'] = ...
    C7: typing.ClassVar['ObservationType'] = ...
    C8: typing.ClassVar['ObservationType'] = ...
    P1: typing.ClassVar['ObservationType'] = ...
    P2: typing.ClassVar['ObservationType'] = ...
    L1: typing.ClassVar['ObservationType'] = ...
    L2: typing.ClassVar['ObservationType'] = ...
    L5: typing.ClassVar['ObservationType'] = ...
    L6: typing.ClassVar['ObservationType'] = ...
    L7: typing.ClassVar['ObservationType'] = ...
    L8: typing.ClassVar['ObservationType'] = ...
    LA: typing.ClassVar['ObservationType'] = ...
    LB: typing.ClassVar['ObservationType'] = ...
    LC: typing.ClassVar['ObservationType'] = ...
    LD: typing.ClassVar['ObservationType'] = ...
    D1: typing.ClassVar['ObservationType'] = ...
    D2: typing.ClassVar['ObservationType'] = ...
    D5: typing.ClassVar['ObservationType'] = ...
    D6: typing.ClassVar['ObservationType'] = ...
    D7: typing.ClassVar['ObservationType'] = ...
    D8: typing.ClassVar['ObservationType'] = ...
    S1: typing.ClassVar['ObservationType'] = ...
    S2: typing.ClassVar['ObservationType'] = ...
    S5: typing.ClassVar['ObservationType'] = ...
    S6: typing.ClassVar['ObservationType'] = ...
    S7: typing.ClassVar['ObservationType'] = ...
    S8: typing.ClassVar['ObservationType'] = ...
    C1A: typing.ClassVar['ObservationType'] = ...
    C1B: typing.ClassVar['ObservationType'] = ...
    C1C: typing.ClassVar['ObservationType'] = ...
    C1I: typing.ClassVar['ObservationType'] = ...
    C1L: typing.ClassVar['ObservationType'] = ...
    C1M: typing.ClassVar['ObservationType'] = ...
    C1P: typing.ClassVar['ObservationType'] = ...
    C1Q: typing.ClassVar['ObservationType'] = ...
    C1S: typing.ClassVar['ObservationType'] = ...
    C1W: typing.ClassVar['ObservationType'] = ...
    C1X: typing.ClassVar['ObservationType'] = ...
    C1Y: typing.ClassVar['ObservationType'] = ...
    C1Z: typing.ClassVar['ObservationType'] = ...
    C2C: typing.ClassVar['ObservationType'] = ...
    C2D: typing.ClassVar['ObservationType'] = ...
    C2I: typing.ClassVar['ObservationType'] = ...
    C2L: typing.ClassVar['ObservationType'] = ...
    C2M: typing.ClassVar['ObservationType'] = ...
    C2P: typing.ClassVar['ObservationType'] = ...
    C2Q: typing.ClassVar['ObservationType'] = ...
    C2S: typing.ClassVar['ObservationType'] = ...
    C2W: typing.ClassVar['ObservationType'] = ...
    C2X: typing.ClassVar['ObservationType'] = ...
    C2Y: typing.ClassVar['ObservationType'] = ...
    C3I: typing.ClassVar['ObservationType'] = ...
    C3Q: typing.ClassVar['ObservationType'] = ...
    C3X: typing.ClassVar['ObservationType'] = ...
    C4A: typing.ClassVar['ObservationType'] = ...
    C4B: typing.ClassVar['ObservationType'] = ...
    C4X: typing.ClassVar['ObservationType'] = ...
    C5A: typing.ClassVar['ObservationType'] = ...
    C5B: typing.ClassVar['ObservationType'] = ...
    C5C: typing.ClassVar['ObservationType'] = ...
    C5D: typing.ClassVar['ObservationType'] = ...
    C5I: typing.ClassVar['ObservationType'] = ...
    C5P: typing.ClassVar['ObservationType'] = ...
    C5Q: typing.ClassVar['ObservationType'] = ...
    C5X: typing.ClassVar['ObservationType'] = ...
    C5Z: typing.ClassVar['ObservationType'] = ...
    C6A: typing.ClassVar['ObservationType'] = ...
    C6B: typing.ClassVar['ObservationType'] = ...
    C6C: typing.ClassVar['ObservationType'] = ...
    C6E: typing.ClassVar['ObservationType'] = ...
    C6I: typing.ClassVar['ObservationType'] = ...
    C6Q: typing.ClassVar['ObservationType'] = ...
    C6L: typing.ClassVar['ObservationType'] = ...
    C6S: typing.ClassVar['ObservationType'] = ...
    C6X: typing.ClassVar['ObservationType'] = ...
    C6Z: typing.ClassVar['ObservationType'] = ...
    C7I: typing.ClassVar['ObservationType'] = ...
    C7Q: typing.ClassVar['ObservationType'] = ...
    C7X: typing.ClassVar['ObservationType'] = ...
    C8I: typing.ClassVar['ObservationType'] = ...
    C8Q: typing.ClassVar['ObservationType'] = ...
    C8X: typing.ClassVar['ObservationType'] = ...
    C9A: typing.ClassVar['ObservationType'] = ...
    C9B: typing.ClassVar['ObservationType'] = ...
    C9C: typing.ClassVar['ObservationType'] = ...
    C9X: typing.ClassVar['ObservationType'] = ...
    C0: typing.ClassVar['ObservationType'] = ...
    CA: typing.ClassVar['ObservationType'] = ...
    CB: typing.ClassVar['ObservationType'] = ...
    CC: typing.ClassVar['ObservationType'] = ...
    CD: typing.ClassVar['ObservationType'] = ...
    D1A: typing.ClassVar['ObservationType'] = ...
    D1B: typing.ClassVar['ObservationType'] = ...
    D1C: typing.ClassVar['ObservationType'] = ...
    D1I: typing.ClassVar['ObservationType'] = ...
    D1L: typing.ClassVar['ObservationType'] = ...
    D1M: typing.ClassVar['ObservationType'] = ...
    D1N: typing.ClassVar['ObservationType'] = ...
    D1P: typing.ClassVar['ObservationType'] = ...
    D1S: typing.ClassVar['ObservationType'] = ...
    D1W: typing.ClassVar['ObservationType'] = ...
    D1X: typing.ClassVar['ObservationType'] = ...
    D1Y: typing.ClassVar['ObservationType'] = ...
    D1Z: typing.ClassVar['ObservationType'] = ...
    D2C: typing.ClassVar['ObservationType'] = ...
    D2D: typing.ClassVar['ObservationType'] = ...
    D2I: typing.ClassVar['ObservationType'] = ...
    D2L: typing.ClassVar['ObservationType'] = ...
    D2M: typing.ClassVar['ObservationType'] = ...
    D2N: typing.ClassVar['ObservationType'] = ...
    D2P: typing.ClassVar['ObservationType'] = ...
    D2Q: typing.ClassVar['ObservationType'] = ...
    D2S: typing.ClassVar['ObservationType'] = ...
    D2W: typing.ClassVar['ObservationType'] = ...
    D2X: typing.ClassVar['ObservationType'] = ...
    D2Y: typing.ClassVar['ObservationType'] = ...
    D3I: typing.ClassVar['ObservationType'] = ...
    D3Q: typing.ClassVar['ObservationType'] = ...
    D3X: typing.ClassVar['ObservationType'] = ...
    D4A: typing.ClassVar['ObservationType'] = ...
    D4B: typing.ClassVar['ObservationType'] = ...
    D4X: typing.ClassVar['ObservationType'] = ...
    D5A: typing.ClassVar['ObservationType'] = ...
    D5B: typing.ClassVar['ObservationType'] = ...
    D5C: typing.ClassVar['ObservationType'] = ...
    D5D: typing.ClassVar['ObservationType'] = ...
    D5I: typing.ClassVar['ObservationType'] = ...
    D5P: typing.ClassVar['ObservationType'] = ...
    D5Q: typing.ClassVar['ObservationType'] = ...
    D5X: typing.ClassVar['ObservationType'] = ...
    D5Z: typing.ClassVar['ObservationType'] = ...
    D6A: typing.ClassVar['ObservationType'] = ...
    D6B: typing.ClassVar['ObservationType'] = ...
    D6C: typing.ClassVar['ObservationType'] = ...
    D6E: typing.ClassVar['ObservationType'] = ...
    D6I: typing.ClassVar['ObservationType'] = ...
    D6Q: typing.ClassVar['ObservationType'] = ...
    D6L: typing.ClassVar['ObservationType'] = ...
    D6S: typing.ClassVar['ObservationType'] = ...
    D6X: typing.ClassVar['ObservationType'] = ...
    D6Z: typing.ClassVar['ObservationType'] = ...
    D7I: typing.ClassVar['ObservationType'] = ...
    D7Q: typing.ClassVar['ObservationType'] = ...
    D7X: typing.ClassVar['ObservationType'] = ...
    D8I: typing.ClassVar['ObservationType'] = ...
    D8Q: typing.ClassVar['ObservationType'] = ...
    D8X: typing.ClassVar['ObservationType'] = ...
    D9A: typing.ClassVar['ObservationType'] = ...
    D9B: typing.ClassVar['ObservationType'] = ...
    D9C: typing.ClassVar['ObservationType'] = ...
    D9X: typing.ClassVar['ObservationType'] = ...
    D0: typing.ClassVar['ObservationType'] = ...
    DA: typing.ClassVar['ObservationType'] = ...
    DB: typing.ClassVar['ObservationType'] = ...
    DC: typing.ClassVar['ObservationType'] = ...
    DD: typing.ClassVar['ObservationType'] = ...
    L1A: typing.ClassVar['ObservationType'] = ...
    L1B: typing.ClassVar['ObservationType'] = ...
    L1C: typing.ClassVar['ObservationType'] = ...
    L1I: typing.ClassVar['ObservationType'] = ...
    L1L: typing.ClassVar['ObservationType'] = ...
    L1M: typing.ClassVar['ObservationType'] = ...
    L1N: typing.ClassVar['ObservationType'] = ...
    L1P: typing.ClassVar['ObservationType'] = ...
    L1S: typing.ClassVar['ObservationType'] = ...
    L1W: typing.ClassVar['ObservationType'] = ...
    L1X: typing.ClassVar['ObservationType'] = ...
    L1Y: typing.ClassVar['ObservationType'] = ...
    L1Z: typing.ClassVar['ObservationType'] = ...
    L2C: typing.ClassVar['ObservationType'] = ...
    L2D: typing.ClassVar['ObservationType'] = ...
    L2I: typing.ClassVar['ObservationType'] = ...
    L2L: typing.ClassVar['ObservationType'] = ...
    L2M: typing.ClassVar['ObservationType'] = ...
    L2N: typing.ClassVar['ObservationType'] = ...
    L2P: typing.ClassVar['ObservationType'] = ...
    L2Q: typing.ClassVar['ObservationType'] = ...
    L2S: typing.ClassVar['ObservationType'] = ...
    L2W: typing.ClassVar['ObservationType'] = ...
    L2X: typing.ClassVar['ObservationType'] = ...
    L2Y: typing.ClassVar['ObservationType'] = ...
    L3I: typing.ClassVar['ObservationType'] = ...
    L3Q: typing.ClassVar['ObservationType'] = ...
    L3X: typing.ClassVar['ObservationType'] = ...
    L4A: typing.ClassVar['ObservationType'] = ...
    L4B: typing.ClassVar['ObservationType'] = ...
    L4X: typing.ClassVar['ObservationType'] = ...
    L5A: typing.ClassVar['ObservationType'] = ...
    L5B: typing.ClassVar['ObservationType'] = ...
    L5C: typing.ClassVar['ObservationType'] = ...
    L5D: typing.ClassVar['ObservationType'] = ...
    L5I: typing.ClassVar['ObservationType'] = ...
    L5P: typing.ClassVar['ObservationType'] = ...
    L5Q: typing.ClassVar['ObservationType'] = ...
    L5X: typing.ClassVar['ObservationType'] = ...
    L5Z: typing.ClassVar['ObservationType'] = ...
    L6A: typing.ClassVar['ObservationType'] = ...
    L6B: typing.ClassVar['ObservationType'] = ...
    L6C: typing.ClassVar['ObservationType'] = ...
    L6E: typing.ClassVar['ObservationType'] = ...
    L6I: typing.ClassVar['ObservationType'] = ...
    L6Q: typing.ClassVar['ObservationType'] = ...
    L6L: typing.ClassVar['ObservationType'] = ...
    L6S: typing.ClassVar['ObservationType'] = ...
    L6X: typing.ClassVar['ObservationType'] = ...
    L6Z: typing.ClassVar['ObservationType'] = ...
    L7I: typing.ClassVar['ObservationType'] = ...
    L7Q: typing.ClassVar['ObservationType'] = ...
    L7X: typing.ClassVar['ObservationType'] = ...
    L8I: typing.ClassVar['ObservationType'] = ...
    L8Q: typing.ClassVar['ObservationType'] = ...
    L8X: typing.ClassVar['ObservationType'] = ...
    L9A: typing.ClassVar['ObservationType'] = ...
    L9B: typing.ClassVar['ObservationType'] = ...
    L9C: typing.ClassVar['ObservationType'] = ...
    L9X: typing.ClassVar['ObservationType'] = ...
    L0: typing.ClassVar['ObservationType'] = ...
    S1A: typing.ClassVar['ObservationType'] = ...
    S1B: typing.ClassVar['ObservationType'] = ...
    S1C: typing.ClassVar['ObservationType'] = ...
    S1I: typing.ClassVar['ObservationType'] = ...
    S1L: typing.ClassVar['ObservationType'] = ...
    S1M: typing.ClassVar['ObservationType'] = ...
    S1N: typing.ClassVar['ObservationType'] = ...
    S1P: typing.ClassVar['ObservationType'] = ...
    S1S: typing.ClassVar['ObservationType'] = ...
    S1W: typing.ClassVar['ObservationType'] = ...
    S1X: typing.ClassVar['ObservationType'] = ...
    S1Y: typing.ClassVar['ObservationType'] = ...
    S1Z: typing.ClassVar['ObservationType'] = ...
    S2C: typing.ClassVar['ObservationType'] = ...
    S2D: typing.ClassVar['ObservationType'] = ...
    S2I: typing.ClassVar['ObservationType'] = ...
    S2L: typing.ClassVar['ObservationType'] = ...
    S2M: typing.ClassVar['ObservationType'] = ...
    S2N: typing.ClassVar['ObservationType'] = ...
    S2P: typing.ClassVar['ObservationType'] = ...
    S2Q: typing.ClassVar['ObservationType'] = ...
    S2S: typing.ClassVar['ObservationType'] = ...
    S2W: typing.ClassVar['ObservationType'] = ...
    S2X: typing.ClassVar['ObservationType'] = ...
    S2Y: typing.ClassVar['ObservationType'] = ...
    S3I: typing.ClassVar['ObservationType'] = ...
    S3Q: typing.ClassVar['ObservationType'] = ...
    S3X: typing.ClassVar['ObservationType'] = ...
    S4A: typing.ClassVar['ObservationType'] = ...
    S4B: typing.ClassVar['ObservationType'] = ...
    S4X: typing.ClassVar['ObservationType'] = ...
    S5A: typing.ClassVar['ObservationType'] = ...
    S5B: typing.ClassVar['ObservationType'] = ...
    S5C: typing.ClassVar['ObservationType'] = ...
    S5D: typing.ClassVar['ObservationType'] = ...
    S5I: typing.ClassVar['ObservationType'] = ...
    S5P: typing.ClassVar['ObservationType'] = ...
    S5Q: typing.ClassVar['ObservationType'] = ...
    S5X: typing.ClassVar['ObservationType'] = ...
    S5Z: typing.ClassVar['ObservationType'] = ...
    S6A: typing.ClassVar['ObservationType'] = ...
    S6B: typing.ClassVar['ObservationType'] = ...
    S6C: typing.ClassVar['ObservationType'] = ...
    S6E: typing.ClassVar['ObservationType'] = ...
    S6I: typing.ClassVar['ObservationType'] = ...
    S6Q: typing.ClassVar['ObservationType'] = ...
    S6L: typing.ClassVar['ObservationType'] = ...
    S6S: typing.ClassVar['ObservationType'] = ...
    S6X: typing.ClassVar['ObservationType'] = ...
    S6Z: typing.ClassVar['ObservationType'] = ...
    S7I: typing.ClassVar['ObservationType'] = ...
    S7Q: typing.ClassVar['ObservationType'] = ...
    S7X: typing.ClassVar['ObservationType'] = ...
    S8I: typing.ClassVar['ObservationType'] = ...
    S8Q: typing.ClassVar['ObservationType'] = ...
    S8X: typing.ClassVar['ObservationType'] = ...
    S9A: typing.ClassVar['ObservationType'] = ...
    S9B: typing.ClassVar['ObservationType'] = ...
    S9C: typing.ClassVar['ObservationType'] = ...
    S9X: typing.ClassVar['ObservationType'] = ...
    S0: typing.ClassVar['ObservationType'] = ...
    SA: typing.ClassVar['ObservationType'] = ...
    SB: typing.ClassVar['ObservationType'] = ...
    SC: typing.ClassVar['ObservationType'] = ...
    SD: typing.ClassVar['ObservationType'] = ...
    def getFrequency(self, satelliteSystem: 'SatelliteSystem') -> Frequency:
        """
            Get the frequency for a specified satellite system.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                frequency for the satellite system, or null if satellite system not compatible
        
        
        """
        ...
    def getMeasurementType(self) -> MeasurementType:
        """
            Get the measurement type.
        
            Returns:
                measurement type
        
        
        """
        ...
    def getSignalCode(self) -> 'SignalCode':
        """
            Get the signal code.
        
            Returns:
                signal code
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ObservationType':
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
    def values() -> typing.List['ObservationType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ObservationType c : ObservationType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RinexObservationHeader:
    """
    public class RinexObservationHeader extends Object
    
        Container for Rinex observation file header.
    
        Since:
            9.2
    """
    @typing.overload
    def __init__(self, double: float, satelliteSystem: 'SatelliteSystem', string: str, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str, string8: str, string9: str, string10: str, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, vector2D: org.hipparchus.geometry.euclidean.twod.Vector2D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, string11: str, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, double3: float, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, string12: str, double4: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, int: int, list: java.util.List[AppliedDCBS], list2: java.util.List[AppliedPCVS], list3: java.util.List['RinexObservationLoader.Parser.PhaseShiftCorrection'], int2: int, int3: int, int4: int, int5: int): ...
    @typing.overload
    def __init__(self, double: float, satelliteSystem: 'SatelliteSystem', string: str, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str, string8: str, string9: str, string10: str, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, vector2D: org.hipparchus.geometry.euclidean.twod.Vector2D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, double3: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, int: int, int2: int): ...
    def getAgencyName(self) -> str:
        """
            Get name of the agency.
        
            Returns:
                name of the agency
        
        
        """
        ...
    def getAntennaAzimuth(self) -> float:
        """
            Get the azimuth of the zero direction of a fixed antenna.
        
            Returns:
                Azimuth of the zero direction of a fixed antenna
        
        
        """
        ...
    def getAntennaBSight(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the antenna B.Sight.
        
            Returns:
                Antenna B.Sight
        
        
        """
        ...
    def getAntennaHeight(self) -> float:
        """
            Get the antenna height.
        
            Returns:
                height of the antenna
        
        
        """
        ...
    def getAntennaNumber(self) -> str:
        """
            Get the number of the antenna.
        
            Returns:
                number of the antenna
        
        
        """
        ...
    def getAntennaPhaseCenter(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the antenna phasecenter.
        
            Returns:
                Antenna phasecenter
        
        
        """
        ...
    def getAntennaReferencePoint(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position of antenna reference point for antenna on vehicle.
        
            Returns:
                Position of antenna reference point for antenna on vehicle
        
        
        """
        ...
    def getAntennaType(self) -> str:
        """
            Get the type of the antenna.
        
            Returns:
                type of the antenna
        
        
        """
        ...
    def getAntennaZeroDirection(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the zero direction of antenna.
        
            Returns:
                Zero direction of antenna
        
        
        """
        ...
    def getApproxPos(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the Approximate Marker Position.
        
            Returns:
                Approximate Marker Position
        
        
        """
        ...
    def getCenterMass(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the current center of mass of vehicle in body fixed coordinate system.
        
            Returns:
                Current center of mass of vehicle in body fixed coordinate system
        
        
        """
        ...
    def getClkOffset(self) -> int:
        """
            Get the realtime-derived receiver clock offset.
        
            Returns:
                realtime-derived receiver clock offset
        
        
        """
        ...
    def getEccentricities(self) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
            Get the eccentricities of antenna center.
        
            Returns:
                Eccentricities of antenna center
        
        
        """
        ...
    def getInterval(self) -> float:
        """
            Get the observation interval in seconds.
        
            Returns:
                Observation interval in seconds
        
        
        """
        ...
    def getLeapSeconds(self) -> int:
        """
            Get the Number of leap seconds since 6-Jan-1980.
        
            Returns:
                Number of leap seconds since 6-Jan-1980
        
        
        """
        ...
    def getLeapSecondsDayNum(self) -> int:
        """
            Get the respective leap second day number.
        
            Returns:
                Respective leap second day number
        
        
        """
        ...
    def getLeapSecondsFuture(self) -> int:
        """
            Get the future or past leap seconds.
        
            Returns:
                Future or past leap seconds
        
        
        """
        ...
    def getLeapSecondsWeekNum(self) -> int:
        """
            Get the respective leap second week number.
        
            Returns:
                Respective leap second week number
        
        
        """
        ...
    def getListAppliedDCBS(self) -> java.util.List[AppliedDCBS]: ...
    def getListAppliedPCVS(self) -> java.util.List[AppliedPCVS]: ...
    def getMarkerName(self) -> str:
        """
            Get name of the antenna marker.
        
            Returns:
                name of the antenna marker
        
        
        """
        ...
    def getMarkerNumber(self) -> str:
        """
            Get number of the antenna marker.
        
            Returns:
                number of the antenna marker
        
        
        """
        ...
    def getMarkerType(self) -> str:
        """
            Get type of the antenna marker.
        
            Returns:
                type of the antenna marker
        
        
        """
        ...
    def getObservationCode(self) -> str:
        """
            Get the observation code of the average phasecenter position w/r to antenna reference point.
        
            Returns:
                Observation code of the average phasecenter position w/r to antenna reference point
        
        
        """
        ...
    def getObserverName(self) -> str:
        """
            Get name of the observer.
        
            Returns:
                name of the observer
        
        
        """
        ...
    def getPhaseShiftCorrections(self) -> java.util.List['RinexObservationLoader.Parser.PhaseShiftCorrection']: ...
    def getReceiverNumber(self) -> str:
        """
            Get the number of the receiver.
        
            Returns:
                number of the receiver
        
        
        """
        ...
    def getReceiverType(self) -> str:
        """
            Get the type of the receiver.
        
            Returns:
                type of the receiver
        
        
        """
        ...
    def getReceiverVersion(self) -> str:
        """
            Get the version of the receiver.
        
            Returns:
                version of the receiver
        
        
        """
        ...
    def getRinexVersion(self) -> float:
        """
            Get Rinex Version.
        
            Returns:
                rinex version of the file
        
        
        """
        ...
    def getSatelliteSystem(self) -> 'SatelliteSystem':
        """
            Get Satellite System.
        
            Returns:
                satellite system of the observation file
        
        
        """
        ...
    def getSignalStrengthUnit(self) -> str:
        """
            Get the unit of the carrier to noise ratio observables.
        
            Returns:
                Unit of the carrier to noise ratio observables
        
        
        """
        ...
    def getTFirstObs(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the time of First observation record.
        
            Returns:
                Time of First observation record
        
        
        """
        ...
    def getTLastObs(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the time of last observation record.
        
            Returns:
                Time of last observation record
        
        
        """
        ...

class RinexObservationLoader:
    """
    public class RinexObservationLoader extends Object
    
        Loader for Rinex measurements files.
    
        Supported versions are: 2.00, 2.10, 2.11, 2.12 (unofficial), 2.20 (unofficial), 3.00, 3.01, 3.02, 3.03, and 3.04.
    
        Since:
            9.2
    
        Also see:
            rinex 2.0, rinex 2.10, rinex 2.11, `unofficial rinex 2.12 <http://www.aiub.unibe.ch/download/rinex/rinex212.txt>`,
            `unofficial rinex 2.20 <http://www.aiub.unibe.ch/download/rinex/rnx_leo.txt>`, rinex 3.00, rinex 3.01, rinex 3.02, rinex
            3.03, rinex 3.04
    """
    DEFAULT_RINEX_2_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_RINEX_2_SUPPORTED_NAMES
    
        Default supported files name pattern for rinex 2 observation files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_RINEX_3_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_RINEX_3_SUPPORTED_NAMES
    
        Default supported files name pattern for rinex 3 observation files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScales: org.orekit.time.TimeScales): ...
    def getObservationDataSets(self) -> java.util.List[ObservationDataSet]: ...
    class Parser(org.orekit.data.DataLoader):
        def __init__(self, rinexObservationLoader: 'RinexObservationLoader'): ...
        def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
        def stillAcceptsData(self) -> bool: ...
        class PhaseShiftCorrection:
            def getCorrection(self) -> float: ...
            def getSatelliteSystem(self) -> 'SatelliteSystem': ...
            def getSatsCorrected(self) -> typing.List[str]: ...
            def getTypeObs(self) -> ObservationType: ...
        class ScaleFactorCorrection:
            def getCorrection(self) -> float: ...
            def getSatelliteSystem(self) -> 'SatelliteSystem': ...
            def getTypesObsScaled(self) -> java.util.List[ObservationType]: ...

class SEMParser(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader):
    """
    public class SEMParser extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.data.DataLoader`
    
        This class reads SEM almanac files and provides :class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac`.
    
        The definition of a SEM almanac comes from the `U.S. COAST GUARD NAVIGATION CENTER
        <http://www.navcen.uscg.gov/?pageName=gpsSem>`.
    
        The format of the files holding SEM almanacs is not precisely specified, so the parsing rules have been deduced from the
        downloadable files at `NAVCEN <http://www.navcen.uscg.gov/?pageName=gpsAlmanacs>` and at CelesTrak.
    
        Since:
            8.0
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales): ...
    def getAlmanacs(self) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GPSAlmanac]: ...
    def getPRNNumbers(self) -> java.util.List[int]:
        """
            Gets the PRN numbers of all the :class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac` read from the file.
        
            Returns:
                the PRN numbers of all the :class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac` read from the file
        
        
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
    @typing.overload
    def loadData(self) -> None:
        """
            Loads almanacs.
        
            The almanacs already loaded in the instance will be discarded and replaced by the newly loaded data.
        
            This feature is useful when the file selection is already set up by the :class:`~org.orekit.data.DataProvidersManager`
            configuration.
        public void loadData(InputStream input, String name) throws IOException, ParseException, :class:`~org.orekit.errors.OrekitException`
        
            Description copied from interface: :meth:`~org.orekit.data.DataLoader.loadData`
            Load data from a stream.
        
            Specified by:
                :meth:`~org.orekit.data.DataLoader.loadData` in interface :class:`~org.orekit.data.DataLoader`
        
            Parameters:
                input (InputStream): data input stream
                name (String): name of the file (or zip entry)
        
            Raises:
                : if data can't be read
                : if data can't be parsed or if some loader specific error occurs
                :class:`~org.orekit.errors.OrekitException`: 
        
        """
        ...
    @typing.overload
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
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

class SatelliteSystem(java.lang.Enum['SatelliteSystem']):
    """
    public enum SatelliteSystem extends Enum<:class:`~org.orekit.gnss.SatelliteSystem`>
    
        Enumerate for satellite system.
    
        Since:
            9.2
    """
    GPS: typing.ClassVar['SatelliteSystem'] = ...
    GLONASS: typing.ClassVar['SatelliteSystem'] = ...
    GALILEO: typing.ClassVar['SatelliteSystem'] = ...
    BEIDOU: typing.ClassVar['SatelliteSystem'] = ...
    QZSS: typing.ClassVar['SatelliteSystem'] = ...
    IRNSS: typing.ClassVar['SatelliteSystem'] = ...
    SBAS: typing.ClassVar['SatelliteSystem'] = ...
    MIXED: typing.ClassVar['SatelliteSystem'] = ...
    def getDefaultTimeSystem(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScale:
        """
            Get default time scale for satellite system.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): the set of timeScales to use
        
            Returns:
                the default time scale among the given set matching to satellite system, null if there are not
        
        
        """
        ...
    def getKey(self) -> str:
        """
            Get the key for the system.
        
            Returns:
                key for the system
        
        
        """
        ...
    @staticmethod
    def parseSatelliteSystem(string: str) -> 'SatelliteSystem': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SatelliteSystem':
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
    def values() -> typing.List['SatelliteSystem']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (SatelliteSystem c : SatelliteSystem.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SignalCode(java.lang.Enum['SignalCode']):
    """
    public enum SignalCode extends Enum<:class:`~org.orekit.gnss.SignalCode`>
    
        Enumerate for satellite signal code.
    
        Since:
            10.1
    """
    A: typing.ClassVar['SignalCode'] = ...
    B: typing.ClassVar['SignalCode'] = ...
    C: typing.ClassVar['SignalCode'] = ...
    D: typing.ClassVar['SignalCode'] = ...
    E: typing.ClassVar['SignalCode'] = ...
    I: typing.ClassVar['SignalCode'] = ...
    L: typing.ClassVar['SignalCode'] = ...
    M: typing.ClassVar['SignalCode'] = ...
    P: typing.ClassVar['SignalCode'] = ...
    Q: typing.ClassVar['SignalCode'] = ...
    S: typing.ClassVar['SignalCode'] = ...
    W: typing.ClassVar['SignalCode'] = ...
    X: typing.ClassVar['SignalCode'] = ...
    Y: typing.ClassVar['SignalCode'] = ...
    Z: typing.ClassVar['SignalCode'] = ...
    CODELESS: typing.ClassVar['SignalCode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SignalCode':
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
    def values() -> typing.List['SignalCode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (SignalCode c : SignalCode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TimeSystem(java.lang.Enum['TimeSystem']):
    """
    public enum TimeSystem extends Enum<:class:`~org.orekit.gnss.TimeSystem`>
    
        Enumerate for the time systems used in navigation files.
    
        Since:
            11.0
    """
    GPS: typing.ClassVar['TimeSystem'] = ...
    GLONASS: typing.ClassVar['TimeSystem'] = ...
    GALILEO: typing.ClassVar['TimeSystem'] = ...
    TAI: typing.ClassVar['TimeSystem'] = ...
    UTC: typing.ClassVar['TimeSystem'] = ...
    QZSS: typing.ClassVar['TimeSystem'] = ...
    BEIDOU: typing.ClassVar['TimeSystem'] = ...
    IRNSS: typing.ClassVar['TimeSystem'] = ...
    UNKNOWN: typing.ClassVar['TimeSystem'] = ...
    def getKey(self) -> str:
        """
            Get the key for the system.
        
            Returns:
                key for the system
        
        
        """
        ...
    def getTimeScale(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScale:
        """
            Get the time scale corresponding to time system.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): the set of time scales to use
        
            Returns:
                the time scale corresponding to time system in the set of time scales
        
        
        """
        ...
    @staticmethod
    def parseTimeSystem(string: str) -> 'TimeSystem': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TimeSystem':
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
    def values() -> typing.List['TimeSystem']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TimeSystem c : TimeSystem.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class YUMAParser(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader):
    """
    public class YUMAParser extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.data.DataLoader`
    
        This class reads Yuma almanac files and provides :class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac`.
    
        The definition of a Yuma almanac comes from the `U.S. COAST GUARD NAVIGATION CENTER
        <http://www.navcen.uscg.gov/?pageName=gpsYuma>`.
    
        The format of the files holding Yuma almanacs is not precisely specified, so the parsing rules have been deduced from
        the downloadable files at `NAVCEN <http://www.navcen.uscg.gov/?pageName=gpsAlmanacs>` and at CelesTrak.
    
        Since:
            8.0
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales): ...
    def getAlmanacs(self) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GPSAlmanac]: ...
    def getPRNNumbers(self) -> java.util.List[int]:
        """
            Gets the PRN numbers of all the :class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac` read from the file.
        
            Returns:
                the PRN numbers of all the :class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac` read from the file
        
        
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
    @typing.overload
    def loadData(self) -> None:
        """
            Loads almanacs.
        
            The almanacs already loaded in the instance will be discarded and replaced by the newly loaded data.
        
            This feature is useful when the file selection is already set up by the :class:`~org.orekit.data.DataProvidersManager`
            configuration.
        public void loadData(InputStream input, String name) throws IOException, ParseException, :class:`~org.orekit.errors.OrekitException`
        
            Description copied from interface: :meth:`~org.orekit.data.DataLoader.loadData`
            Load data from a stream.
        
            Specified by:
                :meth:`~org.orekit.data.DataLoader.loadData` in interface :class:`~org.orekit.data.DataLoader`
        
            Parameters:
                input (InputStream): data input stream
                name (String): name of the file (or zip entry)
        
            Raises:
                : if data can't be read
                : if data can't be parsed or if some loader specific error occurs
                :class:`~org.orekit.errors.OrekitException`: 
        
        """
        ...
    @typing.overload
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss")``.

    AppliedDCBS: typing.Type[AppliedDCBS]
    AppliedPCVS: typing.Type[AppliedPCVS]
    CombinedObservationData: typing.Type[CombinedObservationData]
    CombinedObservationDataSet: typing.Type[CombinedObservationDataSet]
    DOP: typing.Type[DOP]
    DOPComputer: typing.Type[DOPComputer]
    Frequency: typing.Type[Frequency]
    HatanakaCompressFilter: typing.Type[HatanakaCompressFilter]
    MeasurementType: typing.Type[MeasurementType]
    ObservationData: typing.Type[ObservationData]
    ObservationDataSet: typing.Type[ObservationDataSet]
    ObservationType: typing.Type[ObservationType]
    RinexObservationHeader: typing.Type[RinexObservationHeader]
    RinexObservationLoader: typing.Type[RinexObservationLoader]
    SEMParser: typing.Type[SEMParser]
    SatelliteSystem: typing.Type[SatelliteSystem]
    SignalCode: typing.Type[SignalCode]
    TimeSystem: typing.Type[TimeSystem]
    YUMAParser: typing.Type[YUMAParser]
    antenna: org.orekit.gnss.antenna.__module_protocol__
    attitude: org.orekit.gnss.attitude.__module_protocol__
    clock: org.orekit.gnss.clock.__module_protocol__
    metric: org.orekit.gnss.metric.__module_protocol__
    navigation: org.orekit.gnss.navigation.__module_protocol__
