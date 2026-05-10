
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
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
    GNSS antenna model.
    
    Since:
        9.2
    
    Also see:
        txt
    """
    def getEccentricities(self, radioWave: typing.Union[org.orekit.gnss.RadioWave, typing.Callable]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the phase center eccentricities.
        
        Parameters:
            radioWave (RadioWave): radio wave of the signal to consider
        
        Returns:
            phase center eccentricities (m)
        
        
        """
        ...
    def getPattern(self, radioWave: typing.Union[org.orekit.gnss.RadioWave, typing.Callable]) -> 'FrequencyPattern':
        """
        Get a frequency pattern.
        
        Parameters:
            radioWave (RadioWave): radio wave of the signal to consider
        
        Returns:
            pattern for this frequency
        
        
        """
        ...
    def getPhaseCenterVariation(self, radioWave: typing.Union[org.orekit.gnss.RadioWave, typing.Callable], direction: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
        Get the value of the phase center variation in a signal direction.
        
        Parameters:
            radioWave (RadioWave): radio wave of the signal to consider
            direction (Vector3D): signal direction in antenna reference frame
        
        Returns:
            value of the phase center variation (m)
        
        
        """
        ...
    def getRadioWaves(self) -> java.util.List[org.orekit.gnss.RadioWave]:
        """
        Get supported radio waves.
        
        Returns:
            supported radio waves
        
        Since:
            13.0
        
        
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
    Factory for GNSS antennas (both receiver and satellite).
    
    The factory creates antennas by parsing an txt file.
    
    Since:
        9.2
    """
    DEFAULT_ANTEX_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default supported files name pattern for antex files.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, supportedNames: str): ...
    @typing.overload
    def __init__(self, supportedNames: str, dataProvidersManager: org.orekit.data.DataProvidersManager, gps: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, source: org.orekit.data.DataSource, gps: org.orekit.time.TimeScale): ...
    def findSatelliteAntenna(self, satInSystem: org.orekit.gnss.SatInSystem) -> org.orekit.utils.TimeSpanMap['SatelliteAntenna']:
        """
        Find the time map for a specific satellite antenna.
        
        Parameters:
            satInSystem (SatInSystem): satellite in system
        
        Returns:
            time map for the antenna
        
        
        """
        ...
    def getReceiversAntennas(self) -> java.util.List['ReceiverAntenna']:
        """
        Get parsed receivers antennas.
        
        Returns:
            unmodifiable view of parsed receivers antennas
        
        
        """
        ...
    def getSatellitesAntennas(self) -> java.util.List[org.orekit.utils.TimeSpanMap['SatelliteAntenna']]:
        """
        Get parsed satellites antennas.
        
        Returns:
            unmodifiable view of parsed satellites antennas
        
        
        """
        ...

class FrequencyPattern:
    """
    Pattern for GNSS antenna model on one frequency.
    
    Since:
        9.2
    
    Also see:
        txt
    """
    ZERO_CORRECTION: typing.ClassVar['FrequencyPattern'] = ...
    """
    Pattern with zero correction (i.e. zero eccentricities and no variations).
    
    Since:
        12.0
    
    
    """
    def __init__(self, eccentricities: org.hipparchus.geometry.euclidean.threed.Vector3D, phaseCenterVariationFunction: typing.Union['PhaseCenterVariationFunction', typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            eccentricities (Vector3D): phase center eccentricities (m)
            phaseCenterVariationFunction (PhaseCenterVariationFunction): phase center variation function (may be null if phase center does not depend on signal direction)
        
        
        """
        ...
    def getEccentricities(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the phase center eccentricities.
        
        Returns:
            phase center eccentricities (m)
        
        
        """
        ...
    def getPhaseCenterVariation(self, direction: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
        Get the value of the phase center variation in a signal direction.
        
        Parameters:
            direction (Vector3D): signal direction in antenna reference frame
        
        Returns:
            value of the phase center variation
        
        
        """
        ...
    def getPhaseCenterVariationFunction(self) -> 'PhaseCenterVariationFunction':
        """
        Get the phase center variation function.
        
        Returns:
            phase center variation function (may be null if phase center does not depend on signal direction)
        
        Since:
            12.0
        
        
        """
        ...

class PhaseCenterVariationFunction:
    """
    Model for antennas phase center variations.
    
    Since:
        9.2
    """
    def value(self, polarAngle: float, azimuthAngle: float) -> float:
        """
        Evaluate phase center variation in one signal direction.
        
        Parameters:
            polarAngle (double): angle from antenna axial direction (zenith angle for receiver antennas, nadir angle for GNSS satellites antennas)
            azimuthAngle (double): angle around axial direction, counted from +X to +Y (note that this convention is consistent with
                Vector3D,
                but it is different from getAzimuth, so care must be taken when using
                this for ground receivers)
        
        Returns:
            phase center variation in the signal direction (m)
        
        
        """
        ...

class SatelliteType(java.lang.Enum['SatelliteType']):
    """
    Enumerate for satellite types.
    
    Since:
        9.3
    """
    BEIDOU_2G: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_2I: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_2M: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3I: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3SI_SECM: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3SI_CAST: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3M_CAST: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3SM_CAST: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3M_SECM: typing.ClassVar['SatelliteType'] = ...
    BEIDOU_3G_CAST: typing.ClassVar['SatelliteType'] = ...
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
    NAVIC_1GEO: typing.ClassVar['SatelliteType'] = ...
    NAVIC_2GEO: typing.ClassVar['SatelliteType'] = ...
    NAVIC_1IGSO: typing.ClassVar['SatelliteType'] = ...
    QZSS: typing.ClassVar['SatelliteType'] = ...
    QZSS_2A: typing.ClassVar['SatelliteType'] = ...
    QZSS_2I: typing.ClassVar['SatelliteType'] = ...
    QZSS_2G: typing.ClassVar['SatelliteType'] = ...
    def buildAttitudeProvider(self, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame, prnNumber: int) -> org.orekit.gnss.attitude.GNSSAttitudeProvider:
        """
        Build an attitude provider suitable for this satellite type.
        
        Apart from the caller-provided validity interval, Sun provider, frame and PRN number, all construction parameters required for the GNSSAttitudeProvider (for example yaw rates and biases) will be the default ones. If non-default values are needed, the constructor of the appropriate GNSSAttitudeProvider must be called explicitly instead of relying on this general purpose factory method.
        
        Parameters:
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
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
    def parseSatelliteType(s: str) -> 'SatelliteType':
        """
        Parse a string to get the satellite type.
        
        The name must be either a strict IGS name (like "BLOCK IIR-B") or an IGS name canonicalized by removing all spaces, hyphen and underscore characters (like BLOCKIIRB").
        
        Parameters:
            s (String): string to parse (must be a strict IGS name)
        
        Returns:
            the satellite type
        
        Raises:
            OrekitIllegalArgumentException: if the string does not correspond to a satellite antenna code
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'SatelliteType':
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
    def values() -> typing.MutableSequence['SatelliteType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SatelliteType c : SatelliteType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OneDVariation(PhaseCenterVariationFunction):
    """
    Interpolator for 1D phase center variation data.
    
    Since:
        9.2
    """
    def __init__(self, polarStart: float, polarStep: float, variations: typing.Union[typing.List[float], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            polarStart (double): start polar angle
            polarStep (double): between grid points
            variations (double[]): sampled phase center variations
        
        
        """
        ...
    def value(self, polarAngle: float, azimuthAngle: float) -> float:
        """
        Evaluate phase center variation in one signal direction.
        
        Specified by: value in interface PhaseCenterVariationFunction
        
        Parameters:
            polarAngle (double): angle from antenna axial direction (zenith angle for receiver antennas, nadir angle for GNSS satellites antennas)
            azimuthAngle (double): angle around axial direction, counted from +X to +Y (note that this convention is consistent with
                Vector3D,
                but it is different from getAzimuth, so care must be taken when using
                this for ground receivers)
        
        Returns:
            phase center variation in the signal direction (m)
        
        
        """
        ...

class PythonPhaseCenterVariationFunction(PhaseCenterVariationFunction):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def value(self, polarAngle: float, azimuthAngle: float) -> float:
        """
        Evaluate phase center variation in one signal direction.
        
        Specified by: value in interface PhaseCenterVariationFunction
        
        Parameters:
            polarAngle (double): angle from antenna axial direction (zenith angle for receiver antennas, nadir angle for GNSS satellites antennas)
            azimuthAngle (double): angle around axial direction
        
        Returns:
            phase center variation in the signal direction (m)
        
        
        """
        ...

class ReceiverAntenna(Antenna):
    """
    GNSS receiver antenna model.
    
    Since:
        9.2
    
    Also see:
        txt
    """
    def __init__(self, type: str, sinexCode: str, patterns: typing.Union[java.util.Map[typing.Union[org.orekit.gnss.RadioWave, typing.Callable], FrequencyPattern], typing.Mapping[typing.Union[org.orekit.gnss.RadioWave, typing.Callable], FrequencyPattern]], serialNumber: str):
        """
        Simple constructor.
        
        Parameters:
            type (String): antenna type
            sinexCode (String): sinex code
            patterns (Map<RadioWave, FrequencyPattern> patterns): frequencies patterns
            serialNumber (String): serial number
        
        
        """
        ...
    def getSerialNumber(self) -> str:
        """
        Get the serial number.
        
        Returns:
            serial number
        
        
        """
        ...

class SatelliteAntenna(Antenna):
    """
    GNSS satellite antenna model.
    
    Since:
        9.2
    
    Also see:
        txt
    """
    def __init__(self, type: str, sinexCode: str, patterns: typing.Union[java.util.Map[typing.Union[org.orekit.gnss.RadioWave, typing.Callable], FrequencyPattern], typing.Mapping[typing.Union[org.orekit.gnss.RadioWave, typing.Callable], FrequencyPattern]], satInSystem: org.orekit.gnss.SatInSystem, satelliteType: SatelliteType, satelliteCode: int, cosparID: str, validFrom: org.orekit.time.AbsoluteDate, validUntil: org.orekit.time.AbsoluteDate):
        """
        Simple constructor.
        
        Parameters:
            type (String): antenna type
            sinexCode (String): sinex code
            patterns (Map<RadioWave, FrequencyPattern> patterns): frequencies patterns
            satInSystem (SatInSystem): satellite in system
            satelliteType (SatelliteType): satellite type
            satelliteCode (int): satellite code
            cosparID (String): COSPAR ID
            validFrom (AbsoluteDate): start of validity
            validUntil (AbsoluteDate): end of validity
        
        
        """
        ...
    def getCosparID(self) -> str:
        """
        Get COSPAR ID.
        
        Returns:
            COSPAR ID
        
        
        """
        ...
    def getSatInSystem(self) -> org.orekit.gnss.SatInSystem:
        """
        Get satellite in system.
        
        Returns:
            satellite in system
        
        Since:
            13.0
        
        
        """
        ...
    def getSatelliteCode(self) -> int:
        """
        Get satellite code.
        
        Returns:
            satellite code
        
        
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

class TwoDVariation(PhaseCenterVariationFunction):
    """
    Interpolator for 2D phase center variation data.
    
    Since:
        9.2
    """
    def __init__(self, polarStart: float, polarStep: float, azimuthStep: float, variations: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            polarStart (double): start polar angle
            polarStep (double): between grid points
            azimuthStep (double): step between grid points
            variations (double[][]): sampled phase center variations
        
        
        """
        ...
    def value(self, polarAngle: float, azimuthAngle: float) -> float:
        """
        Evaluate phase center variation in one signal direction.
        
        Specified by: value in interface PhaseCenterVariationFunction
        
        Parameters:
            polarAngle (double): angle from antenna axial direction (zenith angle for receiver antennas, nadir angle for GNSS satellites antennas)
            azimuthAngle (double): angle around axial direction, counted from +X to +Y (note that this convention is consistent with
                Vector3D,
                but it is different from getAzimuth, so care must be taken when using
                this for ground receivers)
        
        Returns:
            phase center variation in the signal direction (m)
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.antenna")``.

    Antenna: typing.Type[Antenna]
    AntexLoader: typing.Type[AntexLoader]
    FrequencyPattern: typing.Type[FrequencyPattern]
    OneDVariation: typing.Type[OneDVariation]
    PhaseCenterVariationFunction: typing.Type[PhaseCenterVariationFunction]
    PythonPhaseCenterVariationFunction: typing.Type[PythonPhaseCenterVariationFunction]
    ReceiverAntenna: typing.Type[ReceiverAntenna]
    SatelliteAntenna: typing.Type[SatelliteAntenna]
    SatelliteType: typing.Type[SatelliteType]
    TwoDVariation: typing.Type[TwoDVariation]
