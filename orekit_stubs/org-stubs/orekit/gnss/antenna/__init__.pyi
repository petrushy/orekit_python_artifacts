import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss
import org.orekit.gnss.attitude
import org.orekit.time
import org.orekit.utils
import typing



class Antenna:
    """
    public class Antenna extends Object
    
        GNSS antenna model.
    
        Since:
            9.2
    
        Also see:
            ANTEX: The Antenna Exchange Format, Version 1.4
    """
    def getEccentricities(self, frequency: org.orekit.gnss.Frequency) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the phase center eccentricities.
        
            Parameters:
                frequency (:class:`~org.orekit.gnss.Frequency`): frequency of the signal to consider
        
            Returns:
                phase center eccentricities (m)
        
        
        """
        ...
    def getFrequencies(self) -> java.util.List[org.orekit.gnss.Frequency]: ...
    def getPhaseCenterVariation(self, frequency: org.orekit.gnss.Frequency, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
            Get the value of the phase center variation in a signal direction.
        
            Parameters:
                frequency (:class:`~org.orekit.gnss.Frequency`): frequency of the signal to consider
                direction (Vector3D): signal direction in antenna reference frame
        
            Returns:
                value of the phase center variation (m)
        
        
        """
        ...
    def getSinexCode(self) -> str:
        """
            Get the sinex code of the antenna.
        
            Returns:
                sinex code of the antenna
        
        
        """
        ...
    def getType(self) -> str:
        """
            Get the type of the antenna.
        
            Returns:
                type of the antenna
        
        
        """
        ...

class AntexLoader:
    """
    public class AntexLoader extends Object
    
        Factory for GNSS antennas (both receiver and satellite).
    
        The factory creates antennas by parsing an ANTEX file.
    
        Since:
            9.2
    """
    DEFAULT_ANTEX_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_ANTEX_SUPPORTED_NAMES
    
        Default supported files name pattern for antex files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    def findSatelliteAntenna(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int) -> org.orekit.utils.TimeSpanMap['SatelliteAntenna']: ...
    def getReceiversAntennas(self) -> java.util.List['ReceiverAntenna']: ...
    def getSatellitesAntennas(self) -> java.util.List[org.orekit.utils.TimeSpanMap['SatelliteAntenna']]: ...

class FrequencyPattern:
    """
    public class FrequencyPattern extends Object
    
        Pattern for GNSS antenna model on one frequency.
    
        Since:
            9.2
    
        Also see:
            ANTEX: The Antenna Exchange Format, Version 1.4
    """
    def getEccentricities(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the phase center eccentricities.
        
            Returns:
                phase center eccentricities (m)
        
        
        """
        ...
    def getPhaseCenterVariation(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
            Get the value of the phase center variation in a signal direction.
        
            Parameters:
                direction (Vector3D): signal direction in antenna reference frame
        
            Returns:
                value of the phase center variation
        
        
        """
        ...

class PhaseCenterVariationFunction:
    """
    public interface PhaseCenterVariationFunction
    
        Model for antennas phase center variations.
    
        Since:
            9.2
    """
    def value(self, double: float, double2: float) -> float:
        """
            Evaluate phase center variation in one signal direction.
        
            Parameters:
                polarAngle (double): angle from antenna axial direction (zenith angle for receiver antennas, nadir angle for GNSS satellites antennas)
                azimuthAngle (double): angle around axial direction
        
            Returns:
                phase center variation in the signal direction (m)
        
        
        """
        ...

class SatelliteType(java.lang.Enum['SatelliteType']):
    """
    public enum SatelliteType extends Enum<:class:`~org.orekit.gnss.antenna.SatelliteType`>
    
        Enumerate for satellite types.
    
        Since:
            9.3
    """
    BEIDOU_2G: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_2I: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_2M: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3I: typing.ClassVar['SatelliteType'] = ...
    BLOCK_I: typing.ClassVar['SatelliteType'] = ...
    BLOCK_II: typing.ClassVar['SatelliteType'] = ...
    BLOCK_IIA: typing.ClassVar['SatelliteType'] = ...
    BLOCK_IIR_A: typing.ClassVar['SatelliteType'] = ...
    BLOCK_IIR_B: typing.ClassVar['SatelliteType'] = ...
    BLOCK_IIR_M: typing.ClassVar['SatelliteType'] = ...
    BLOCK_IIF: typing.ClassVar['SatelliteType'] = ...
    BLOCK_IIIA: typing.ClassVar['SatelliteType'] = ...
    GALILEO_0A: typing.ClassVar['SatelliteType'] = ...
    GALILEO_0B: typing.ClassVar['SatelliteType'] = ...
    GALILEO_1: typing.ClassVar['SatelliteType'] = ...
    GALILEO_2: typing.ClassVar['SatelliteType'] = ...
    GLONASS: typing.ClassVar['SatelliteType'] = ...
    GLONASS_M: typing.ClassVar['SatelliteType'] = ...
    GLONASS_K1: typing.ClassVar['SatelliteType'] = ...
    GLONASS_K2: typing.ClassVar['SatelliteType'] = ...
    IRNSS_1GEO: typing.ClassVar['SatelliteType'] = ...
    IRNSS_1IGSO: typing.ClassVar['SatelliteType'] = ...
    QZSS: typing.ClassVar['SatelliteType'] = ...
    QZSS_2I: typing.ClassVar['SatelliteType'] = ...
    QZSS_2G: typing.ClassVar['SatelliteType'] = ...
    def buildAttitudeProvider(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame, int: int) -> org.orekit.gnss.attitude.GNSSAttitudeProvider:
        """
            Build an attitude provider suitable for this satellite type.
        
            Apart from the caller-provided validity interval, Sun provider, frame and PRN number, all construction parameters
            required for the :class:`~org.orekit.gnss.attitude.GNSSAttitudeProvider` (for example yaw rates and biases) will be the
            default ones. If non-default values are needed, the constructor of the appropriate
            :class:`~org.orekit.gnss.attitude.GNSSAttitudeProvider` must be called explicitly instead of relying on this general
            purpose factory method.
        
            Parameters:
                validityStart (:class:`~org.orekit.time.AbsoluteDate`): start of validity for this provider
                validityEnd (:class:`~org.orekit.time.AbsoluteDate`): end of validity for this provider
                sun (:class:`~org.orekit.utils.ExtendedPVCoordinatesProvider`): provider for Sun position
                inertialFrame (:class:`~org.orekit.frames.Frame`): inertial frame where velocity are computed
                prnNumber (int): number within the satellite system
        
            Returns:
                an attitude provider suitable for this satellite type
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the IGS name for the antenna code.
        
            Returns:
                IGS name for the antenna code
        
        
        """
        ...
    @staticmethod
    def parseSatelliteType(string: str) -> 'SatelliteType': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SatelliteType':
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
    def values() -> typing.List['SatelliteType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (SatelliteType c : SatelliteType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PythonPhaseCenterVariationFunction(PhaseCenterVariationFunction):
    """
    public class PythonPhaseCenterVariationFunction extends Object implements :class:`~org.orekit.gnss.antenna.PhaseCenterVariationFunction`
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
    def value(self, double: float, double2: float) -> float:
        """
            Evaluate phase center variation in one signal direction.
        
            Specified by:
                :meth:`~org.orekit.gnss.antenna.PhaseCenterVariationFunction.value`Â in
                interfaceÂ :class:`~org.orekit.gnss.antenna.PhaseCenterVariationFunction`
        
            Parameters:
                polarAngle (double): angle from antenna axial direction (zenith angle for receiver antennas, nadir angle for GNSS satellites antennas)
                azimuthAngle (double): angle around axial direction
        
            Returns:
                phase center variation in the signal direction (m)
        
        
        """
        ...

class ReceiverAntenna(Antenna):
    """
    public class ReceiverAntenna extends :class:`~org.orekit.gnss.antenna.Antenna`
    
        GNSS receiver antenna model.
    
        Since:
            9.2
    
        Also see:
            ANTEX: The Antenna Exchange Format, Version 1.4
    """
    def __init__(self, string: str, string2: str, map: typing.Union[java.util.Map[org.orekit.gnss.Frequency, FrequencyPattern], typing.Mapping[org.orekit.gnss.Frequency, FrequencyPattern]], string3: str): ...
    def getSerialNumber(self) -> str:
        """
            Get the serial number.
        
            Returns:
                serial number
        
        
        """
        ...

class SatelliteAntenna(Antenna):
    """
    public class SatelliteAntenna extends :class:`~org.orekit.gnss.antenna.Antenna`
    
        GNSS satellite antenna model.
    
        Since:
            9.2
    
        Also see:
            ANTEX: The Antenna Exchange Format, Version 1.4
    """
    def __init__(self, string: str, string2: str, map: typing.Union[java.util.Map[org.orekit.gnss.Frequency, FrequencyPattern], typing.Mapping[org.orekit.gnss.Frequency, FrequencyPattern]], satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, satelliteType: SatelliteType, int2: int, string3: str, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    def getCosparID(self) -> str:
        """
            Get COSPAR ID.
        
            Returns:
                COSPAR ID
        
        
        """
        ...
    def getPrnNumber(self) -> int:
        """
            Get PRN number.
        
            Returns:
                PRN number
        
        
        """
        ...
    def getSatelliteCode(self) -> int:
        """
            Get satellite code.
        
            Returns:
                satellite code
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get satellite system.
        
            Returns:
                satellite system
        
        
        """
        ...
    def getSatelliteType(self) -> SatelliteType:
        """
            Get satellite type.
        
            Returns:
                satellite type
        
            Since:
                9.3
        
        
        """
        ...
    def getValidFrom(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start of validity.
        
            Returns:
                start of validity
        
        
        """
        ...
    def getValidUntil(self) -> org.orekit.time.AbsoluteDate:
        """
            Get end of validity.
        
            Returns:
                end of validity
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.antenna")``.

    Antenna: typing.Type[Antenna]
    AntexLoader: typing.Type[AntexLoader]
    FrequencyPattern: typing.Type[FrequencyPattern]
    PhaseCenterVariationFunction: typing.Type[PhaseCenterVariationFunction]
    PythonPhaseCenterVariationFunction: typing.Type[PythonPhaseCenterVariationFunction]
    ReceiverAntenna: typing.Type[ReceiverAntenna]
    SatelliteAntenna: typing.Type[SatelliteAntenna]
    SatelliteType: typing.Type[SatelliteType]
