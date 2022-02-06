import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.orekit.data
import org.orekit.files.general
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.sampling
import org.orekit.time
import org.orekit.utils
import typing



class CPF(org.orekit.files.general.EphemerisFile['CPF.CPFCoordinate', 'CPF.CPFEphemeris']):
    """
    public class CPF extends Object implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.files.ilrs.CPF.CPFCoordinate`,:class:`~org.orekit.files.ilrs.CPF.CPFEphemeris`>
    
        This class stores all the information of the Consolidated laser ranging Prediction File (CPF) parsed by CPFParser. It
        contains the header and a list of ephemeris entry.
    
        Since:
            10.3
    """
    DEFAULT_ID: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_ID
    
        Default satellite ID, used if header is null when initializing the ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @typing.overload
    def addSatelliteCoordinate(self, string: str, cPFCoordinate: 'CPF.CPFCoordinate') -> None:
        """
            Add a new P/V coordinates to the satellite.
        
            Parameters:
                id (String): satellite ILRS identifier
                coord (:class:`~org.orekit.files.ilrs.CPF.CPFCoordinate`): the P/V coordinate of the satellite
        
            Since:
                11.0.1
        
        
        """
        ...
    @typing.overload
    def addSatelliteCoordinate(self, cPFCoordinate: 'CPF.CPFCoordinate') -> None: ...
    def addSatelliteCoordinates(self, string: str, list: java.util.List['CPF.CPFCoordinate']) -> None: ...
    def getComments(self) -> java.util.List[str]:
        """
            Get the comments contained in the file.
        
            Returns:
                the comments contained in the file
        
        
        """
        ...
    def getHeader(self) -> 'CPFHeader':
        """
            Get the CPF file header.
        
            Returns:
                the CPF file header
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'CPF.CPFEphemeris']: ...
    def getTimeScale(self) -> org.orekit.time.TimeScale:
        """
            Get the time scale used in CPF file.
        
            Returns:
                the time scale used to parse epochs in CPF file.
        
        
        """
        ...
    def setFilter(self, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter) -> None:
        """
            Set the derivatives filter.
        
            Parameters:
                filter (:class:`~org.orekit.utils.CartesianDerivativesFilter`): that indicates which derivatives of position are available.
        
        
        """
        ...
    def setInterpolationSample(self, int: int) -> None:
        """
            Set the interpolation sample.
        
            Parameters:
                interpolationSample (int): interpolation sample
        
        
        """
        ...
    def setMu(self, double: float) -> None:
        """
            Set the gravitational coefficient.
        
            Parameters:
                mu (double): the coefficient to be set
        
        
        """
        ...
    def setTimeScale(self, timeScale: org.orekit.time.TimeScale) -> None:
        """
            Set the time scale.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): use to parse dates in this file.
        
        
        """
        ...
    class CPFCoordinate(org.orekit.utils.TimeStampedPVCoordinates):
        @typing.overload
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, int: int): ...
        @typing.overload
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, int: int): ...
        def getLeap(self) -> int: ...
    class CPFEphemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris['CPF.CPFCoordinate', 'CPF.CPFEphemeris'], org.orekit.files.general.EphemerisFile.EphemerisSegment['CPF.CPFCoordinate']):
        @typing.overload
        def __init__(self, cPF: 'CPF'): ...
        @typing.overload
        def __init__(self, cPF: 'CPF', string: str): ...
        def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter: ...
        def getCoordinates(self) -> java.util.List['CPF.CPFCoordinate']: ...
        def getEphemeridesDataLines(self) -> java.util.List['CPF.CPFCoordinate']: ...
        def getFrame(self) -> org.orekit.frames.Frame: ...
        def getId(self) -> str: ...
        def getInterpolationSamples(self) -> int: ...
        def getMu(self) -> float: ...
        def getPropagator(self) -> org.orekit.propagation.BoundedPropagator: ...
        def getSegments(self) -> java.util.List['CPF.CPFEphemeris']: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...

class CPFParser(org.orekit.files.general.EphemerisFileParser[CPF]):
    """
    public class CPFParser extends Object implements :class:`~org.orekit.files.general.EphemerisFileParser`<:class:`~org.orekit.files.ilrs.CPF`>
    
        A parser for the CPF orbit file format.
    
        It supports both 1.0 and 2.0 versions
    
        **Note:** Only required header keys are read. Furthermore, only position data are read. Other keys are simply ignored
        Contributions are welcome to support more fields in the format.
    
        Since:
            10.3
    
        Also see:
            1.0 file format, 2.0 file format
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, frames: org.orekit.frames.Frames): ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> CPF:
        """
            Parse an ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFileParser.parse`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed ephemeris file.
        
        
        """
        ...

class CPFWriter(org.orekit.files.general.EphemerisFileWriter):
    """
    public class CPFWriter extends Object implements :class:`~org.orekit.files.general.EphemerisFileWriter`
    
        An CPF Writer class that can take in a general :class:`~org.orekit.files.general.EphemerisFile` object and export it as
        a valid CPF file.
    
        It supports both 1.0 and 2.0 versions
    
        **Note:** By default, only required header keys are wrote (H1 and H2). Furthermore, only position data can be written.
        Other keys (i.e. in header and other types of ephemeris entries) are simply ignored. Contributions are welcome to
        support more fields in the format.
    
        Since:
            10.3
    
        Also see:
            1.0 file format, 2.0 file format
    """
    def __init__(self, cPFHeader: 'CPFHeader', timeScale: org.orekit.time.TimeScale): ...
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    @typing.overload
    def write(self, string: str, ephemerisFile: org.orekit.files.general.EphemerisFile[_write_0__C, _write_0__S]) -> None: ...
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: org.orekit.files.general.EphemerisFile[_write_1__C, _write_1__S]) -> None: ...

class CRD:
    """
    public class CRD extends Object
    
        This class stores all the information of the Consolidated laser ranging Data Format (CRD) parsed by CRDParser. It
        contains the header and a list of data records.
    
        Since:
            10.3
    """
    def __init__(self): ...
    def addDataBlock(self, cRDDataBlock: 'CRD.CRDDataBlock') -> None:
        """
            Add a data block to the current list of data blocks.
        
            Parameters:
                dataBlock (:class:`~org.orekit.files.ilrs.CRD.CRDDataBlock`): data block to add
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]:
        """
            Get the comments contained in the file.
        
            Returns:
                the comments contained in the file
        
        
        """
        ...
    def getDataBlocks(self) -> java.util.List['CRD.CRDDataBlock']: ...
    class AnglesMeasurement(org.orekit.time.TimeStamped):
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, int: int, int2: int, boolean: bool, double3: float, double4: float): ...
        def getAzimuth(self) -> float: ...
        def getAzimuthRate(self) -> float: ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getDirectionFlag(self) -> int: ...
        def getElevation(self) -> float: ...
        def getElevationRate(self) -> float: ...
        def getOriginIndicator(self) -> int: ...
        def isRefractionCorrected(self) -> bool: ...
    class CRDDataBlock:
        def __init__(self): ...
        def addAnglesData(self, anglesMeasurement: 'CRD.AnglesMeasurement') -> None: ...
        def addMeteoData(self, meteorologicalMeasurement: 'CRD.MeteorologicalMeasurement') -> None: ...
        def addRangeData(self, rangeMeasurement: 'CRD.RangeMeasurement') -> None: ...
        def getAnglesData(self) -> java.util.List['CRD.AnglesMeasurement']: ...
        def getConfigurationRecords(self) -> 'CRDConfiguration': ...
        def getHeader(self) -> 'CRDHeader': ...
        def getMeteoData(self) -> 'CRD.Meteo': ...
        def getRangeData(self) -> java.util.List['CRD.RangeMeasurement']: ...
        def setConfigurationRecords(self, cRDConfiguration: 'CRDConfiguration') -> None: ...
        def setHeader(self, cRDHeader: 'CRDHeader') -> None: ...
    class Meteo:
        def __init__(self, sortedSet: java.util.SortedSet['CRD.MeteorologicalMeasurement']): ...
        def getData(self) -> java.util.List['CRD.MeteorologicalMeasurement']: ...
        def getMeteo(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'CRD.MeteorologicalMeasurement': ...
    class MeteorologicalMeasurement(org.orekit.time.TimeStamped):
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float): ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getHumidity(self) -> float: ...
        def getPressure(self) -> float: ...
        def getTemperature(self) -> float: ...
    class RangeMeasurement(org.orekit.time.TimeStamped):
        @typing.overload
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, int: int): ...
        @typing.overload
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, int: int, double2: float): ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getEpochEvent(self) -> int: ...
        def getSnr(self) -> float: ...
        def getTimeOfFlight(self) -> float: ...

class CRDConfiguration:
    """
    public class CRDConfiguration extends Object
    
        Container for Consolidated laser ranging Data Format (CDR) configuration records.
    
        Since:
            10.3
    """
    def __init__(self): ...
    def getDetectorRecord(self) -> 'CRDConfiguration.DetectorConfiguration':
        """
            Get the detector configuration record.
        
            Returns:
                the detector configuration record
        
        
        """
        ...
    def getLaserRecord(self) -> 'CRDConfiguration.LaserConfiguration':
        """
            Get the laser configuration record.
        
            Returns:
                the laser configuration record
        
        
        """
        ...
    def getMeteorologicalRecord(self) -> 'CRDConfiguration.MeteorologicalConfiguration':
        """
            Get the meteorological record.
        
            Returns:
                the meteorological record
        
        
        """
        ...
    def getSoftwareRecord(self) -> 'CRDConfiguration.SoftwareConfiguration':
        """
            Get the software configuration record.
        
            Returns:
                the software configuration record
        
        
        """
        ...
    def getSystemRecord(self) -> 'CRDConfiguration.SystemConfiguration':
        """
            Get the system configuration record.
        
            Returns:
                the system configuration record
        
        
        """
        ...
    def getTimingRecord(self) -> 'CRDConfiguration.TimingSystemConfiguration':
        """
            Get the timing system configuration record.
        
            Returns:
                the timing system configuration record
        
        
        """
        ...
    def getTransponderRecord(self) -> 'CRDConfiguration.TransponderConfiguration':
        """
            Get the transponder configuration record.
        
            Returns:
                the transponder configuration record
        
        
        """
        ...
    def setDetectorRecord(self, detectorConfiguration: 'CRDConfiguration.DetectorConfiguration') -> None:
        """
            Set the detector configuration record.
        
            Parameters:
                detectorRecord (:class:`~org.orekit.files.ilrs.CRDConfiguration.DetectorConfiguration`): the record to set
        
        
        """
        ...
    def setLaserRecord(self, laserConfiguration: 'CRDConfiguration.LaserConfiguration') -> None:
        """
            Set the laser configuration record.
        
            Parameters:
                laserRecord (:class:`~org.orekit.files.ilrs.CRDConfiguration.LaserConfiguration`): the record to set
        
        
        """
        ...
    def setMeteorologicalRecord(self, meteorologicalConfiguration: 'CRDConfiguration.MeteorologicalConfiguration') -> None:
        """
            Set the meteorological record.
        
            Parameters:
                meteorologicalRecord (:class:`~org.orekit.files.ilrs.CRDConfiguration.MeteorologicalConfiguration`): the meteorological record to set
        
        
        """
        ...
    def setSoftwareRecord(self, softwareConfiguration: 'CRDConfiguration.SoftwareConfiguration') -> None:
        """
            Set the software configuration record.
        
            Parameters:
                softwareRecord (:class:`~org.orekit.files.ilrs.CRDConfiguration.SoftwareConfiguration`): the record to set
        
        
        """
        ...
    def setSystemRecord(self, systemConfiguration: 'CRDConfiguration.SystemConfiguration') -> None:
        """
            Set the system configuration record.
        
            Parameters:
                systemRecord (:class:`~org.orekit.files.ilrs.CRDConfiguration.SystemConfiguration`): the record to set
        
        
        """
        ...
    def setTimingRecord(self, timingSystemConfiguration: 'CRDConfiguration.TimingSystemConfiguration') -> None:
        """
            Set the timing system configuration record.
        
            Parameters:
                timingRecord (:class:`~org.orekit.files.ilrs.CRDConfiguration.TimingSystemConfiguration`): the record to set
        
        
        """
        ...
    def setTransponderRecord(self, transponderConfiguration: 'CRDConfiguration.TransponderConfiguration') -> None:
        """
            Set the transponder configuration record.
        
            Parameters:
                transponderRecord (:class:`~org.orekit.files.ilrs.CRDConfiguration.TransponderConfiguration`): the record to set
        
        
        """
        ...
    class DetectorConfiguration:
        def __init__(self): ...
        def getAmplifierBandwidth(self) -> float: ...
        def getAmplifierGain(self) -> float: ...
        def getAmplifierInUse(self) -> str: ...
        def getApplicableWavelength(self) -> float: ...
        def getAppliedVoltage(self) -> float: ...
        def getDarkCount(self) -> float: ...
        def getDetectorId(self) -> str: ...
        def getDetectorType(self) -> str: ...
        def getExternalSignalProcessing(self) -> str: ...
        def getOutputPulseType(self) -> str: ...
        def getOutputPulseWidth(self) -> float: ...
        def getQuantumEfficiency(self) -> float: ...
        def getSpatialFilter(self) -> float: ...
        def getSpectralFilter(self) -> float: ...
        def getTransmissionOfSpectralFilter(self) -> float: ...
        def setAmplifierBandwidth(self, double: float) -> None: ...
        def setAmplifierGain(self, double: float) -> None: ...
        def setAmplifierInUse(self, string: str) -> None: ...
        def setApplicableWavelength(self, double: float) -> None: ...
        def setAppliedVoltage(self, double: float) -> None: ...
        def setDarkCount(self, double: float) -> None: ...
        def setDetectorId(self, string: str) -> None: ...
        def setDetectorType(self, string: str) -> None: ...
        def setExternalSignalProcessing(self, string: str) -> None: ...
        def setOutputPulseType(self, string: str) -> None: ...
        def setOutputPulseWidth(self, double: float) -> None: ...
        def setQuantumEfficiency(self, double: float) -> None: ...
        def setSpatialFilter(self, double: float) -> None: ...
        def setSpectralFilter(self, double: float) -> None: ...
        def setTransmissionOfSpectralFilter(self, double: float) -> None: ...
    class LaserConfiguration:
        def __init__(self): ...
        def getBeamDivergence(self) -> float: ...
        def getLaserId(self) -> str: ...
        def getLaserType(self) -> str: ...
        def getNominalFireRate(self) -> float: ...
        def getPrimaryWavelength(self) -> float: ...
        def getPulseEnergy(self) -> float: ...
        def getPulseInOutgoingSemiTrain(self) -> int: ...
        def getPulseWidth(self) -> float: ...
        def setBeamDivergence(self, double: float) -> None: ...
        def setLaserId(self, string: str) -> None: ...
        def setLaserType(self, string: str) -> None: ...
        def setNominalFireRate(self, double: float) -> None: ...
        def setPrimaryWavelength(self, double: float) -> None: ...
        def setPulseEnergy(self, double: float) -> None: ...
        def setPulseInOutgoingSemiTrain(self, int: int) -> None: ...
        def setPulseWidth(self, double: float) -> None: ...
    class MeteorologicalConfiguration:
        def __init__(self): ...
        def getHumiSensorManufacturer(self) -> str: ...
        def getHumiSensorModel(self) -> str: ...
        def getHumiSensorSerialNumber(self) -> str: ...
        def getMeteorologicalId(self) -> str: ...
        def getPressSensorManufacturer(self) -> str: ...
        def getPressSensorModel(self) -> str: ...
        def getPressSensorSerialNumber(self) -> str: ...
        def getTempSensorManufacturer(self) -> str: ...
        def getTempSensorModel(self) -> str: ...
        def getTempSensorSerialNumber(self) -> str: ...
        def setHumiSensorManufacturer(self, string: str) -> None: ...
        def setHumiSensorModel(self, string: str) -> None: ...
        def setHumiSensorSerialNumber(self, string: str) -> None: ...
        def setMeteorologicalId(self, string: str) -> None: ...
        def setPressSensorManufacturer(self, string: str) -> None: ...
        def setPressSensorModel(self, string: str) -> None: ...
        def setPressSensorSerialNumber(self, string: str) -> None: ...
        def setTempSensorManufacturer(self, string: str) -> None: ...
        def setTempSensorModel(self, string: str) -> None: ...
        def setTempSensorSerialNumber(self, string: str) -> None: ...
    class SoftwareConfiguration:
        def __init__(self): ...
        def getProcessingSoftwareVersions(self) -> typing.List[str]: ...
        def getProcessingSoftwares(self) -> typing.List[str]: ...
        def getSoftwareId(self) -> str: ...
        def getTrackingSoftwareVersions(self) -> typing.List[str]: ...
        def getTrackingSoftwares(self) -> typing.List[str]: ...
        def setProcessingSoftwareVersions(self, stringArray: typing.List[str]) -> None: ...
        def setProcessingSoftwares(self, stringArray: typing.List[str]) -> None: ...
        def setSoftwareId(self, string: str) -> None: ...
        def setTrackingSoftwareVersions(self, stringArray: typing.List[str]) -> None: ...
        def setTrackingSoftwares(self, stringArray: typing.List[str]) -> None: ...
    class SystemConfiguration:
        def __init__(self): ...
        def getSystemId(self) -> str: ...
        def getWavelength(self) -> float: ...
        def setSystemId(self, string: str) -> None: ...
        def setWavelength(self, double: float) -> None: ...
    class TimingSystemConfiguration:
        def __init__(self): ...
        def getEpochDelayCorrection(self) -> float: ...
        def getFrequencySource(self) -> str: ...
        def getLocalTimingId(self) -> str: ...
        def getTimeSource(self) -> str: ...
        def getTimer(self) -> str: ...
        def getTimerSerialNumber(self) -> str: ...
        def setEpochDelayCorrection(self, double: float) -> None: ...
        def setFrequencySource(self, string: str) -> None: ...
        def setLocalTimingId(self, string: str) -> None: ...
        def setTimeSource(self, string: str) -> None: ...
        def setTimer(self, string: str) -> None: ...
        def setTimerSerialNumber(self, string: str) -> None: ...
    class TransponderConfiguration:
        def __init__(self): ...
        def getSpacecraftClockAndDriftApplied(self) -> int: ...
        def getStationClockAndDriftApplied(self) -> int: ...
        def getStationOscDrift(self) -> float: ...
        def getStationUTCOffset(self) -> float: ...
        def getTranspClkRefTime(self) -> float: ...
        def getTranspOscDrift(self) -> float: ...
        def getTranspUTCOffset(self) -> float: ...
        def getTransponderId(self) -> str: ...
        def isSpacecraftTimeSimplified(self) -> bool: ...
        def setIsSpacecraftTimeSimplified(self, boolean: bool) -> None: ...
        def setSpacecraftClockAndDriftApplied(self, int: int) -> None: ...
        def setStationClockAndDriftApplied(self, int: int) -> None: ...
        def setStationOscDrift(self, double: float) -> None: ...
        def setStationUTCOffset(self, double: float) -> None: ...
        def setTranspClkRefTime(self, double: float) -> None: ...
        def setTranspOscDrift(self, double: float) -> None: ...
        def setTranspUTCOffset(self, double: float) -> None: ...
        def setTransponderId(self, string: str) -> None: ...

class CRDParser:
    """
    public class CRDParser extends Object
    
        A parser for the CRD data file format.
    
        It supports both 1.0 and 2.0 versions
    
        **Note**: Not all the records are read by the parser. Only the most significants are parsed. Contributions are welcome
        to support more fields in the format.
    
        Since:
            10.3
    
        Also see:
            1.0 file format, 2.0 file format
    """
    DEFAULT_CRD_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_CRD_SUPPORTED_NAMES
    
        Default supported files name pattern for CRD files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    def getTimeScale(self) -> org.orekit.time.TimeScale:
        """
            Get the time scale used to read the file.
        
            Returns:
                the time scale used to read the file
        
        
        """
        ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> CRD: ...

class ILRSHeader:
    """
    public abstract class ILRSHeader extends Object
    
        Container for common data contains in International Laser Ranging Service (ILRS) files header.
    
        Since:
            10.3
    
        Also see:
            :class:`~org.orekit.files.ilrs.CPFHeader`, :class:`~org.orekit.files.ilrs.CRDHeader`
    """
    def __init__(self): ...
    def getEndEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the ending epoch (UTC).
        
            Returns:
                the ending epoch
        
        
        """
        ...
    def getFormat(self) -> str:
        """
            Get the file format.
        
            Returns:
                the file format
        
        
        """
        ...
    def getIlrsSatelliteId(self) -> str:
        """
            Get the IRLS satellite ID (based on COSPAR ID).
        
            Returns:
                the IRLS satellite ID
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the satellite target name.
        
            Returns:
                the satellite target name
        
        
        """
        ...
    def getNoradId(self) -> str:
        """
            Get the satellite NORAD ID (i.e. Satellite Catalog Number).
        
            Returns:
                the satellite NORAD ID
        
        
        """
        ...
    def getProductionEpoch(self) -> org.orekit.time.DateComponents:
        """
            Get the date component of the ephemeris production.
        
            Returns:
                the date component of the ephemeris production
        
        
        """
        ...
    def getProductionHour(self) -> int:
        """
            Get the hour of ephemeris production (UTC).
        
            Returns:
                the hour of ephemeris production
        
        
        """
        ...
    def getSequenceNumber(self) -> int:
        """
            Get the ephemeris sequence number.
        
            Returns:
                the ephemeris sequence number
        
        
        """
        ...
    def getSic(self) -> str:
        """
            Get the SIC ID.
        
            Returns:
                the SIC ID
        
        
        """
        ...
    def getStartEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the starting epoch (UTC).
        
            Returns:
                the starting epoch
        
        
        """
        ...
    def getTargetClass(self) -> int:
        """
            Get the target class.
        
            0 = no retroreflector; 1 = passive retroreflector; ...
        
            Returns:
                the target class
        
        
        """
        ...
    def getTargetLocation(self) -> int:
        """
            Get the target location.
        
            1 = Earth orbit; 2 = Lunar orbit; ...
        
            Returns:
                the target location
        
        
        """
        ...
    def getVersion(self) -> int:
        """
            Get the format version.
        
            Returns:
                the format version
        
        
        """
        ...
    def setEndEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the ending epoch (UTC).
        
            Parameters:
                endEpoch (:class:`~org.orekit.time.AbsoluteDate`): the ending epoch to set
        
        
        """
        ...
    def setFormat(self, string: str) -> None:
        """
            Set the file format.
        
            Parameters:
                format (String): the format to set
        
        
        """
        ...
    def setIlrsSatelliteId(self, string: str) -> None:
        """
            Set the IRLS satellite ID (based on COSPAR ID).
        
            Parameters:
                ilrsSatelliteId (String): the IRLS satellite ID to set
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Set the satellite target name.
        
            Parameters:
                name (String): the satellite target name to set
        
        
        """
        ...
    def setNoradId(self, string: str) -> None:
        """
            Set the satellite NORAD ID.
        
            Parameters:
                noradId (String): the NORAD ID to set
        
        
        """
        ...
    def setProductionEpoch(self, dateComponents: org.orekit.time.DateComponents) -> None:
        """
            Set the date component of the ephemeris production.
        
            Parameters:
                productionEpoch (:class:`~org.orekit.time.DateComponents`): the date component to set
        
        
        """
        ...
    def setProductionHour(self, int: int) -> None:
        """
            Set the hour of ephemeris production.
        
            Parameters:
                productionHour (int): the hour of ephemeris production to set
        
        
        """
        ...
    def setSequenceNumber(self, int: int) -> None:
        """
            Set the ephemeris sequence number.
        
            Parameters:
                sequenceNumber (int): the ephemeris sequence number to set
        
        
        """
        ...
    def setSic(self, string: str) -> None:
        """
            Set the SIC ID.
        
            Parameters:
                sic (String): the SIC ID to set
        
        
        """
        ...
    def setStartEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the staring epoch (UTC).
        
            Parameters:
                startEpoch (:class:`~org.orekit.time.AbsoluteDate`): the starting epoch to set
        
        
        """
        ...
    def setTargetClass(self, int: int) -> None:
        """
            Set the target class.
        
            0 = no retroreflector; 1 = passive retroreflector; ...
        
            Parameters:
                targetClass (int): the target class to set
        
        
        """
        ...
    def setTargetLocation(self, int: int) -> None:
        """
            Set the target location.
        
            1 = Earth orbit; 2 = Lunar orbit; ...
        
            Parameters:
                targetLocation (int): the target location to set
        
        
        """
        ...
    def setVersion(self, int: int) -> None:
        """
            Set the format version.
        
            Parameters:
                version (int): the version to set
        
        
        """
        ...

class StreamingCpfWriter:
    """
    public class StreamingCpfWriter extends Object
    
        A writer for CPF files.
    
        Each instance corresponds to a single CPF file.
    
        This class can be used as a step handler for a :class:`~org.orekit.propagation.Propagator`. The following example shows
        its use as a step handler.
    
        **Note:** By default, only required header keys are wrote (H1 and H2). Furthermore, only position data can be written.
        Other keys (optionals) are simply ignored. Contributions are welcome to support more fields in the format.
    
        Since:
            10.3
    """
    def __init__(self, appendable: java.lang.Appendable, timeScale: org.orekit.time.TimeScale, cPFHeader: 'CPFHeader'): ...
    def newSegment(self, frame: org.orekit.frames.Frame) -> 'StreamingCpfWriter.Segment':
        """
            Create a writer for a new CPF ephemeris segment.
        
            The returned writer can only write a single ephemeris segment in a CPF.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): the reference frame to use for the segment.
        
            Returns:
                a new CPF segment, ready for writing.
        
        
        """
        ...
    def writeEndOfFile(self) -> None: ...
    def writeHeader(self) -> None: ...
    class HeaderLineWriter(java.lang.Enum['StreamingCpfWriter.HeaderLineWriter']):
        H1: typing.ClassVar['StreamingCpfWriter.HeaderLineWriter'] = ...
        H2: typing.ClassVar['StreamingCpfWriter.HeaderLineWriter'] = ...
        def getIdentifier(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'StreamingCpfWriter.HeaderLineWriter': ...
        @staticmethod
        def values() -> typing.List['StreamingCpfWriter.HeaderLineWriter']: ...
        def write(self, cPFHeader: 'CPFHeader', appendable: java.lang.Appendable, timeScale: org.orekit.time.TimeScale) -> None: ...
    class Segment(org.orekit.propagation.sampling.OrekitFixedStepHandler):
        def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def handleStep(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def writeEphemerisLine(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> None: ...

class CPFHeader(ILRSHeader):
    """
    public class CPFHeader extends :class:`~org.orekit.files.ilrs.ILRSHeader`
    
        Container for Consolidated laser ranging Prediction File (CPF) header.
    
        Note: Only the required fields are present.
    
        Since:
            10.3
    """
    def __init__(self): ...
    def getCenterOfMassOffset(self) -> float:
        """
            Get the approximate center of mass to reflector offset.
        
            Returns:
                the approximate center of mass to reflector offset in meters
        
        
        """
        ...
    def getPrf(self) -> float:
        """
            Get the Pulse Repetition Frequency (PRF).
        
            Returns:
                the Pulse Repetition Frequency (PRF) in Hz
        
        
        """
        ...
    def getRefFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame.
        
            Returns:
                the reference frame
        
        
        """
        ...
    def getRefFrameId(self) -> int:
        """
            Get the reference frame identifier.
        
            Returns:
                the reference frame
        
        
        """
        ...
    def getRotationalAngleType(self) -> int:
        """
            Get the rotation angle type.
        
            Returns:
                the rotation angle type
        
        
        """
        ...
    def getSource(self) -> str:
        """
            Get the ephemeris source.
        
            Returns:
                the ephemeris source
        
        
        """
        ...
    def getStep(self) -> int:
        """
            Get the time between table entries.
        
            Returns:
                the time between table entries in seconds
        
        
        """
        ...
    def getSubDailySequenceNumber(self) -> int:
        """
            Get the sub-daily ephemeris sequence number.
        
            Returns:
                the sub-daily ephemeris sequence number
        
        
        """
        ...
    def getTranspClkRef(self) -> float:
        """
            Get the transponder Clock Reference Time.
        
            Returns:
                the transponder Clock Reference Time
        
        
        """
        ...
    def getTranspOscDrift(self) -> float:
        """
            Get the transponder Oscillator Drift in parts in 10^15.
        
            Returns:
                the transponder Oscillator Drift in parts.
        
        
        """
        ...
    def getTranspTransmitDelay(self) -> float:
        """
            Get the transponder transmit delay.
        
            Returns:
                the transponder transmit delay in seconds
        
        
        """
        ...
    def getTranspUtcOffset(self) -> float:
        """
            Get the transponder UTC offset.
        
            Returns:
                the transponder UTC offset in seconds
        
        
        """
        ...
    def isCenterOfMassCorrectionApplied(self) -> bool:
        """
            Get the flag telling if the center of mass correction is applied.
        
            Returns:
                true if center of mass correction is applied
        
        
        """
        ...
    def isCompatibleWithTIVs(self) -> bool:
        """
            Get the flag for compatibility with TIVs.
        
            Returns:
                true if compatible with TIVs
        
        
        """
        ...
    def setCenterOfMassOffset(self, double: float) -> None:
        """
            Set the approximate center of mass to reflector offset.
        
            Parameters:
                centerOfMassOffset (double): the offset to set in meters
        
        
        """
        ...
    def setIsCenterOfMassCorrectionApplied(self, boolean: bool) -> None:
        """
            Set the flag telling if the center of mass correction is applied.
        
            Parameters:
                isCenterOfMassCorrectionApplied (boolean): true if center of mass correction is applied
        
        
        """
        ...
    def setIsCompatibleWithTIVs(self, boolean: bool) -> None:
        """
            Set the flag for compatibility with TIVs.
        
            Parameters:
                isCompatibleWithTIVs (boolean): true if compatible with TIVs
        
        
        """
        ...
    def setPrf(self, double: float) -> None:
        """
            Set the Pulse Repetition Frequency (PRF).
        
            Parameters:
                prf (double): the ulse Repetition Frequency (PRF) to set in Hz
        
        
        """
        ...
    def setRefFrame(self, frame: org.orekit.frames.Frame) -> None:
        """
            Set the reference frame.
        
            Parameters:
                refFrame (:class:`~org.orekit.frames.Frame`): the reference frame to set
        
        
        """
        ...
    def setRefFrameId(self, int: int) -> None:
        """
            Set the reference frame identifier.
        
            Parameters:
                refFrameId (int): the reference frame identifier to set
        
        
        """
        ...
    def setRotationalAngleType(self, int: int) -> None:
        """
            Set the rotation angle type.
        
            Parameters:
                rotationalAngleType (int): the rotation angle type to set
        
        
        """
        ...
    def setSource(self, string: str) -> None:
        """
            Set the ephemeris source.
        
            Parameters:
                source (String): the ephemeris source to set
        
        
        """
        ...
    def setStep(self, int: int) -> None:
        """
            Set the time between table entries.
        
            Parameters:
                step (int): the time to set in seconds
        
        
        """
        ...
    def setSubDailySequenceNumber(self, int: int) -> None:
        """
            Set the sub-daily ephemeris sequence number.
        
            Parameters:
                subDailySequenceNumber (int): the sub-daily ephemeris sequence number to set
        
        
        """
        ...
    def setTranspClkRef(self, double: float) -> None:
        """
            Set the transponder Clock Reference Time.
        
            Parameters:
                transpClkRef (double): the transponder Clock Reference Time to set
        
        
        """
        ...
    def setTranspOscDrift(self, double: float) -> None:
        """
            Set the transponder Oscillator Drift in parts.
        
            Parameters:
                transpOscDrift (double): the transponder Oscillator Drift in parts in 10^15 to set
        
        
        """
        ...
    def setTranspTransmitDelay(self, double: float) -> None:
        """
            Set the transponder transmit delay.
        
            Parameters:
                transpTransmitDelay (double): the transponder transmit delay to set in seconds
        
        
        """
        ...
    def setTranspUtcOffset(self, double: float) -> None:
        """
            Set the transponder UTC offset.
        
            Parameters:
                transpUtcOffset (double): the UTC offset to set in seconds
        
        
        """
        ...

class CRDHeader(ILRSHeader):
    """
    public class CRDHeader extends :class:`~org.orekit.files.ilrs.ILRSHeader`
    
        Container for Consolidated laser ranging Data Format (CDR) header.
    
        Since:
            10.3
    """
    def __init__(self): ...
    def getDataReleaseFlag(self) -> int:
        """
            Get the flag indicating the data release.
        
            Returns:
                the flag indicating the data release
        
        
        """
        ...
    def getDataType(self) -> int:
        """
            Get the data type.
        
            0 = full rate ; 1 = normal point ; 2 = sampled engineering
        
            Returns:
                the data type
        
        
        """
        ...
    def getDateAndTime(self) -> str:
        """
            Get the date and time as the string value.
        
            Depending the prediction type, this value can represent the CPF starting date and hour (MMDDHH) from CPF H2 record or
            TLE epoch day/fractional day
        
            Returns:
                the date and time as the string value
        
        
        """
        ...
    def getEpochIdentifier(self) -> int:
        """
            Get the epoch identifier.
        
            3 = UTC (UNSO) ; 4 = UTC (GPS) ; 7 = UTC (BIPM) ; 10 = UTC (Station Time Scale)
        
            Returns:
                the epoch identifier
        
        
        """
        ...
    def getPredictionProvider(self) -> str:
        """
            Get the prediction provider.
        
            Returns:
                the preditction provider
        
        
        """
        ...
    def getPredictionType(self) -> int:
        """
            Get the prediction type (CPF or TLE).
        
            Returns:
                the prediction type
        
        
        """
        ...
    def getQualityIndicator(self) -> int:
        """
            Get the data quality indicator.
        
            Returns:
                the data quality indicator
        
        
        """
        ...
    def getRangeType(self) -> 'CRDHeader.RangeType':
        """
            Get the range type.
        
            Returns:
                the range type
        
        
        """
        ...
    def getSpacecraftEpochTimeScale(self) -> int:
        """
            Get the spacecraft epoch time scale.
        
            Returns:
                the spacecraft epoch time scale
        
        
        """
        ...
    def getStationName(self) -> str:
        """
            Get the station name from official list.
        
            Returns:
                the station name from official list
        
        
        """
        ...
    def getStationNetword(self) -> str:
        """
            Get the station network.
        
            Returns:
                the station network
        
        
        """
        ...
    def getSystemIdentifier(self) -> int:
        """
            Get the system identifier.
        
            Returns:
                the system identifier
        
        
        """
        ...
    def getSystemNumber(self) -> int:
        """
            Get the system number.
        
            Returns:
                the system number
        
        
        """
        ...
    def getSystemOccupancy(self) -> int:
        """
            Get the system occupancy.
        
            Returns:
                the system occupancy
        
        
        """
        ...
    def getYearOfCentury(self) -> int:
        """
            Get the year of century from CPF or TLE.
        
            Returns:
                the year of century from CPF or TLE
        
        
        """
        ...
    def isCenterOfMassCorrectionApplied(self) -> bool:
        """
            Get the center of mass correction applied indicator.
        
            Returns:
                true if center of mass correction is applied
        
        
        """
        ...
    def isReceiveAmplitudeCorrectionApplied(self) -> bool:
        """
            Get the receive amplitude correction applied indicator.
        
            Returns:
                true if receive amplitude correction is applied
        
        
        """
        ...
    def isStationSystemDelayApplied(self) -> bool:
        """
            Get the station system delay applied indicator.
        
            Returns:
                true if station system delay is applied
        
        
        """
        ...
    def isTransponderDelayApplied(self) -> bool:
        """
            Get the spacecraft system delay applied (transponders) indicator.
        
            Returns:
                true if transponder delay is applied
        
        
        """
        ...
    def isTroposphericRefractionApplied(self) -> bool:
        """
            Get the tropospheric refraction correction applied indicator.
        
            Returns:
                true if tropospheric refraction correction is applied
        
        
        """
        ...
    def setDataReleaseFlag(self, int: int) -> None:
        """
            Set the flag indicating the data release.
        
            Parameters:
                dataReleaseFlag (int): the flag to set
        
        
        """
        ...
    def setDataType(self, int: int) -> None:
        """
            Set the data type.
        
            Parameters:
                dataType (int): the data type to set
        
        
        """
        ...
    def setDateAndTime(self, string: str) -> None:
        """
            Set the string value of date and time.
        
            Parameters:
                dateAndTime (String): the date and time to set
        
        
        """
        ...
    def setEpochIdentifier(self, int: int) -> None:
        """
            Set the epoch identifier.
        
            Parameters:
                epochIdentifier (int): the epoch identifier to set
        
        
        """
        ...
    def setIsCenterOfMassCorrectionApplied(self, boolean: bool) -> None:
        """
            Set the center of mass correction applied indicator.
        
            Parameters:
                isCenterOfMassCorrectionApplied (boolean): true if center of mass correction is applied
        
        
        """
        ...
    def setIsReceiveAmplitudeCorrectionApplied(self, boolean: bool) -> None:
        """
            Set the receive amplitude correction applied indicator.
        
            Parameters:
                isReceiveAmplitudeCorrectionApplied (boolean): true if receive amplitude correction is applied
        
        
        """
        ...
    def setIsStationSystemDelayApplied(self, boolean: bool) -> None:
        """
            Set the station system delay applied indicator.
        
            Parameters:
                isStationSystemDelayApplied (boolean): true if station system delay is applied
        
        
        """
        ...
    def setIsTransponderDelayApplied(self, boolean: bool) -> None:
        """
            Set the spacecraft system delay applied (transponders) indicator.
        
            Parameters:
                isTransponderDelayApplied (boolean): true if transponder delay is applied
        
        
        """
        ...
    def setIsTroposphericRefractionApplied(self, boolean: bool) -> None:
        """
            Set the tropospheric refraction correction applied indicator.
        
            Parameters:
                isTroposphericRefractionApplied (boolean): true if tropospheric refraction correction is applied
        
        
        """
        ...
    def setPredictionProvider(self, string: str) -> None:
        """
            Set the prediction provider.
        
            Parameters:
                predictionProvider (String): the prediction provider to set
        
        
        """
        ...
    def setPredictionType(self, int: int) -> None:
        """
            Set the prediction type.
        
            Parameters:
                predictionType (int): the prediction type to set
        
        
        """
        ...
    def setQualityIndicator(self, int: int) -> None:
        """
            Set the data quality indicator.
        
            Parameters:
                qualityIndicator (int): the indicator to set
        
        
        """
        ...
    def setRangeType(self, int: int) -> None:
        """
            Set the range type indicator.
        
            Parameters:
                indicator (int): range type indicator
        
        
        """
        ...
    def setSpacecraftEpochTimeScale(self, int: int) -> None:
        """
            Set the spacecraft epoch time scale.
        
            Parameters:
                spacecraftEpochTimeScale (int): the spacecraft epoch time scale to set
        
        
        """
        ...
    def setStationName(self, string: str) -> None:
        """
            Set the station name from official list.
        
            Parameters:
                stationName (String): the station name to set
        
        
        """
        ...
    def setStationNetword(self, string: str) -> None:
        """
            Set the station network.
        
            Parameters:
                stationNetword (String): the station network to set
        
        
        """
        ...
    def setSystemIdentifier(self, int: int) -> None:
        """
            Set the system identifier.
        
            Parameters:
                systemIdentifier (int): the system identifier to set
        
        
        """
        ...
    def setSystemNumber(self, int: int) -> None:
        """
            Set the system number.
        
            Parameters:
                systemNumber (int): the system number to set
        
        
        """
        ...
    def setSystemOccupancy(self, int: int) -> None:
        """
            Set the system occupancy.
        
            Parameters:
                systemOccupancy (int): the system occupancy to set
        
        
        """
        ...
    def setYearOfCentury(self, int: int) -> None:
        """
            Set the year of century from CPF or TLE.
        
            Parameters:
                yearOfCentury (int): the year of century to set
        
        
        """
        ...
    class RangeType(java.lang.Enum['CRDHeader.RangeType']):
        NO_RANGES: typing.ClassVar['CRDHeader.RangeType'] = ...
        ONE_WAY: typing.ClassVar['CRDHeader.RangeType'] = ...
        TWO_WAY: typing.ClassVar['CRDHeader.RangeType'] = ...
        RECEIVED_ONLY: typing.ClassVar['CRDHeader.RangeType'] = ...
        MIXED: typing.ClassVar['CRDHeader.RangeType'] = ...
        def getIndicator(self) -> int: ...
        @staticmethod
        def getRangeType(int: int) -> 'CRDHeader.RangeType': ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'CRDHeader.RangeType': ...
        @staticmethod
        def values() -> typing.List['CRDHeader.RangeType']: ...

class PythonILRSHeader(ILRSHeader):
    """
    public class PythonILRSHeader extends :class:`~org.orekit.files.ilrs.ILRSHeader`
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ilrs")``.

    CPF: typing.Type[CPF]
    CPFHeader: typing.Type[CPFHeader]
    CPFParser: typing.Type[CPFParser]
    CPFWriter: typing.Type[CPFWriter]
    CRD: typing.Type[CRD]
    CRDConfiguration: typing.Type[CRDConfiguration]
    CRDHeader: typing.Type[CRDHeader]
    CRDParser: typing.Type[CRDParser]
    ILRSHeader: typing.Type[ILRSHeader]
    PythonILRSHeader: typing.Type[PythonILRSHeader]
    StreamingCpfWriter: typing.Type[StreamingCpfWriter]
