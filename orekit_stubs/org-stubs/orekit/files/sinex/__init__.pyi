
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.util
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss
import org.orekit.models.earth.displacement
import org.orekit.time
import org.orekit.utils
import typing



class AbstractSinex:
    """
    Base container for Solution INdependent EXchange (SINEX) files.
    
    Since:
        13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, creationDate: org.orekit.time.AbsoluteDate, startDate: org.orekit.time.AbsoluteDate, endDate: org.orekit.time.AbsoluteDate):
        """
        Simple constructor.
        
        Parameters:
            timeScales (TimeScales): time scales
            creationDate (AbsoluteDate): SINEX file creation date
            startDate (AbsoluteDate): start time of the data used in the Sinex solution
            endDate (AbsoluteDate): end time of the data used in the Sinex solution
        
        
        """
        ...
    def getCreationDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the creation date of the parsed SINEX file.
        
        Returns:
            SINEX file creation date as an AbsoluteDate
        
        
        """
        ...
    def getFileEpochEndTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the file epoch end time.
        
        Returns:
            the file epoch end time
        
        
        """
        ...
    def getFileEpochStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the file epoch start time.
        
        Returns:
            the file epoch start time
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
        Get the time scales.
        
        Returns:
            time scales
        
        
        """
        ...

_AbstractSinexParser__T = typing.TypeVar('_AbstractSinexParser__T', bound=AbstractSinex)  # <T>
_AbstractSinexParser__P = typing.TypeVar('_AbstractSinexParser__P', bound='ParseInfo')  # <P>
class AbstractSinexParser(typing.Generic[_AbstractSinexParser__T, _AbstractSinexParser__P]):
    """
    Base parser for Solution INdependent EXchange (SINEX) files.
    
    Since:
        13.0
    """
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
        Get the time scales.
        
        Returns:
            time scales
        
        
        """
        ...
    def parse(self, *sources: org.orekit.data.DataSource) -> _AbstractSinexParser__T:
        """
        Parse one or more SINEX files.
        
        Parameters:
            sources (DataSource...): sources providing the data to parse
        
        Returns:
            parsed file combining all sources
        
        
        """
        ...

class AntennaKey:
    """
    Key for antenna.
    
    Since:
        13.0
    """
    OTHER_RADOME_CODE: typing.ClassVar[str] = ...
    """
    Constant matching other radome codes.
    
    Also see:
        constant
    
    
    """
    ANY_SERIAL_NUMBER: typing.ClassVar[str] = ...
    """
    Constant matching any serial numbers.
    
    Also see:
        constant
    
    
    """
    def __init__(self, name: str, radomeCode: str, serialNumber: str):
        """
        Simple constructor.
        
        The Sinex file specification uses a single 20 characters field named "Antenna type" and described as "Antenna name and model" (Antex specification is similar). In practice this field contains a variable length name and the last four characters are a radome code, which may be set to OTHER_RADOME_CODE for a catch-all entry. Here, we separate this field into its two components, so we can provide matchingCandidates by tweaking the radome code if needed.
        
        Parameters:
            name (String): antenna name
            radomeCode (String): radome code
            serialNumber (String): serial number
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the antenna name.
        
        Returns:
            antenna name
        
        
        """
        ...
    def getRadomeCode(self) -> str:
        """
        Get the radome code.
        
        Returns:
            radome code
        
        
        """
        ...
    def getSerialNumber(self) -> str:
        """
        Get the serial number.
        
        Returns:
            serial number
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def matchingCandidates(self) -> java.util.List['AntennaKey']:
        """
        Get candidates for fuzzy matching of this antenna key.
        
        Some Sinex files use specific keys in the SITE/ANTENNA block and catch-all keys in the SITE/GPS_PHASE_CENTER, SITE/GAL_PHASE_CENTER blocks. As an example, file JAX0MGXFIN_20202440000_01D_000_SOL.SNX contains the following entries related to antenna type ASH700936D_M:
        
         SITE/ANTENNA AMU2  A ---- P 00:000:00000 00:000:00000 ASH700936D_M    SCIS 13569 ARTU  A ---- P 00:000:00000 00:000:00000 ASH700936D_M    DOME CR130 DRAG  A ---- P 00:000:00000 00:000:00000 ASH700936D_M    SNOW CR143 PALM  A ---- P 00:000:00000 00:000:00000 ASH700936D_M    SCIS CR141 SITE/GPS_PHASE_CENTER ASH700936D_M    NONE -----  .0910  .0004 -.0003  .1204 -.0001 -.0001 igs14_%Y%m ASH700936D_M    SCIS -----  .0879  .0005 -.0001  .1192  .0001 -.0001 igs14_%Y%m ASH700936D_M    SNOW -----  .0909  .0003 -.0002  .1192  .0001  .0001 igs14_%Y%m
        
        Apart from the obvious formatting error of the last field in SITE/GPS_PHASE_CENTER, it appears there are no phase center data for the antenna used at ARTU site, because no radome code match "DOME". We consider here that a "close enough" entry would be to use OTHER_RADOME_CODE as the radome code, and ANY_SERIAL_NUMBER as the serial number.
        
        Another example is file ESA0OPSFIN_20241850000_01D_01D_SOL.SNX which contains the following entries related to antenna type ASH701945G_M:
        
         SITE/ANTENNA FAIR  A    1 P 24:184:86382 24:185:86382 ASH701945G_M    JPLA CR520    0 KOKB  A    1 P 24:184:86382 24:185:86382 ASH701945G_M    NONE CR620    0 SUTH  A    1 P 24:184:86382 24:185:86382 ASH701945G_M    NONE CR620    0 SITE/GPS_PHASE_CENTER ASH701945G_M    NONE CR520 0.0895 0.0001 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR620 0.0895 0.0001 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR620 0.0895 0.0001 -.0001 0.1162 -.0007 -.0001 IGS20_2317 SITE/GAL_PHASE_CENTER ASH701945G_M    NONE CR520 0.0895 0.0001 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR520 0.1162 -.0007 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR520 0.1162 -.0007 -.0001                      IGS20_2317 ASH701945G_M    NONE CR620 0.0895 0.0001 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR620 0.1162 -.0007 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR620 0.1162 -.0007 -.0001                      IGS20_2317 ASH701945G_M    NONE CR620 0.0895 0.0001 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR620 0.1162 -.0007 -.0001 0.1162 -.0007 -.0001 IGS20_2317 ASH701945G_M    NONE CR620 0.1162 -.0007 -.0001                      IGS20_2317
        
        Here, the phase centers for serial number CR620 appear twice (fortunately with the same values). There are no phase center data for the antenna used at FAIR site, because no radome code match "JPLA". We consider here that a "close enough" entry would be to use OTHER_RADOME_CODE, and keep the provided serial number.
        
        The logic we adopted is to use the following candidates:
        
        Returns:
            candidates for matching instance key, sorted from stricter to looser match
        
        
        """
        ...

class BiasDescription:
    """
    Class to store the bias description parameters.
    
    This class gives important parameters from the analysis and defines the fields in the block ’BIAS/SOLUTION’ of the loaded Sinex file.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getBiasMode(self) -> str:
        """
        Get the bias mode.
        
        The bias mode describes how the included GNSS bias values have to be interpreted and applied.
        
        Returns:
            the bias mode
        
        
        """
        ...
    def getDeterminationMethod(self) -> str:
        """
        Get the determination mode used to generate the bias results.
        
        This value is optional. If the value is not present in the file, the method returns an empty string.
        
        Returns:
            the determination mode used to generate the bias results.
        
        
        """
        ...
    def getObservationSampling(self) -> int:
        """
        Get the observation sampling interval used for data analysis.
        
        This value is optional. If the value is not present in the file, the method returns -1.
        
        Returns:
            the observation sampling interval used for data analysis in seconds
        
        
        """
        ...
    def getParameterSpacing(self) -> int:
        """
        Get the parameter spacing interval between the bias value.
        
        This value is optional. If the value is not present in the file, the method returns -1.
        
        Returns:
            the pParameter spacing interval between the bias value in seconds
        
        
        """
        ...
    def getTimeSystem(self) -> org.orekit.gnss.TimeSystem:
        """
        Get the time system for DSB data.
        
        Returns:
            the time system
        
        
        """
        ...
    def setBiasMode(self, biasMode: str) -> None:
        """
        Set the bias mode.
        
        Parameters:
            biasMode (String): the bias mode to set
        
        
        """
        ...
    def setDeterminationMethod(self, determinationMethod: str) -> None:
        """
        Set the determination mode used to generate the bias results.
        
        Parameters:
            determinationMethod (String): the determination method to set
        
        
        """
        ...
    def setObservationSampling(self, observationSampling: int) -> None:
        """
        Set the observation sampling interval used for data analysis.
        
        Parameters:
            observationSampling (int): the observation sampling to set in seconds
        
        
        """
        ...
    def setParameterSpacing(self, parameterSpacing: int) -> None:
        """
        Set the parameter spacing interval between the bias value.
        
        Parameters:
            parameterSpacing (int): the parameter spacing to set in seconds
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.gnss.TimeSystem) -> None:
        """
        Set the time system used for DSB data.
        
        Parameters:
            timeSystem (TimeSystem): the time system to set
        
        
        """
        ...

class DifferentialSignalBias:
    """
    Container for differential signal bias for a single link endpoint (either emitter or receiver).
    
    This class is made to handle both station and satellite DSB data. Bias values are stored in TimeSpanMaps associated with a given pair of observation types. Those TimeSpanMaps are stored in a Map, which associate a pair of observation types to a TimeSpanMap of double values.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def addBias(self, obs1: org.orekit.gnss.ObservationType, obs2: org.orekit.gnss.ObservationType, spanBegin: org.orekit.time.AbsoluteDate, spanEnd: org.orekit.time.AbsoluteDate, biasValue: float) -> None:
        """
        Add a bias.
        
        Parameters:
            obs1 (ObservationType): first observation used for the DSB computation
            obs2 (ObservationType): second observation used for the DSB computation
            spanBegin (AbsoluteDate): beginning of the validity span for this bias value
            spanEnd (AbsoluteDate): end of the validity span for this bias value
            biasValue (double): DSB bias value (meters for code and cycle for phase)
        
        
        """
        ...
    def getAvailableObservationPairs(self) -> java.util.HashSet[org.hipparchus.util.Pair[org.orekit.gnss.ObservationType, org.orekit.gnss.ObservationType]]:
        """
        Get all available observation type pairs for the satellite.
        
        Returns:
            observation type pairs obtained.
        
        
        """
        ...
    def getBias(self, obs1: org.orekit.gnss.ObservationType, obs2: org.orekit.gnss.ObservationType, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the Differential Signal Bias for a given observation pair at a given date.
        
        Parameters:
            obs1 (ObservationType): first observation type
            obs2 (ObservationType): second observation type
            date (AbsoluteDate): date at which to obtain the DSB
        
        Returns:
            the value of the DSB (meters for code and cycle for phase)
        
        
        """
        ...
    def getMaximumValidDateForObservationPair(self, obs1: org.orekit.gnss.ObservationType, obs2: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
        Get the maximum valid date for a given observation pair.
        
        Parameters:
            obs1 (ObservationType): first observation type
            obs2 (ObservationType): second observation type
        
        Returns:
            maximum valid date for the observation pair
        
        
        """
        ...
    def getMinimumValidDateForObservationPair(self, obs1: org.orekit.gnss.ObservationType, obs2: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
        Get the minimum valid date for a given observation pair.
        
        Parameters:
            obs1 (ObservationType): first observation type
            obs2 (ObservationType): second observation type
        
        Returns:
            minimum valid date for the observation pair
        
        
        """
        ...
    def getTimeSpanMap(self, obs1: org.orekit.gnss.ObservationType, obs2: org.orekit.gnss.ObservationType) -> org.orekit.utils.TimeSpanMap[float]:
        """
        Get the TimeSpanMap object for a given observation type pair, for further operation on the object directly.
        
        Parameters:
            obs1 (ObservationType): first observation type
            obs2 (ObservationType): second observation type
        
        Returns:
            the time span map for a given observation type pair
        
        
        """
        ...

_LineParser__T = typing.TypeVar('_LineParser__T', bound='ParseInfo')  # <T>
class LineParser(typing.Generic[_LineParser__T]):
    """
    Parser class for one line.
    
    Since:
        13.0
    """
    def allowedNextParsers(self, parseInfo: _LineParser__T) -> java.lang.Iterable['LineParser'[_LineParser__T]]:
        """
        Get allowed next line parsers.
        
        Parameters:
            parseInfo (LineParser): holder for transient data
        
        Returns:
            allowed parszers for next lines
        
        
        """
        ...
    def parseIfRecognized(self, parseInfo: _LineParser__T) -> bool:
        """
        Parse a line if recognized.
        
        Parameters:
            parseInfo (LineParser): holder for transient data
        
        Returns:
            true if line was recognized
        
        
        """
        ...

class ObservableSpecificSignalBias:
    """
    Container for observation-specific signal bias for a single link endpoint (either emitter or receiver).
    
    This class is made to handle both station and satellite OSB data. Bias values are stored in TimeSpanMaps associated with a given observation type. Those TimeSpanMaps are stored in a Map, which associate an observation code to a TimeSpanMap of double values.
    
    Since:
        13.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def addBias(self, obs: org.orekit.gnss.ObservationType, spanBegin: org.orekit.time.AbsoluteDate, spanEnd: org.orekit.time.AbsoluteDate, biasValue: float) -> None:
        """
        Add a bias.
        
        Parameters:
            obs (ObservationType): observation used for the OSB computation
            spanBegin (AbsoluteDate): beginning of the validity span for this bias value
            spanEnd (AbsoluteDate): end of the validity span for this bias value
            biasValue (double): Observable-specific Signal Bias value (meters for code and cycle for phase)
        
        
        """
        ...
    def getAvailableObservations(self) -> java.util.HashSet[org.orekit.gnss.ObservationType]:
        """
        Get all available observation types for the satellite.
        
        Returns:
            Observation types obtained.
        
        
        """
        ...
    def getBias(self, obs: org.orekit.gnss.ObservationType, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the Observable-specific Signal Bias for a given observation type at a given date.
        
        Parameters:
            obs (ObservationType): observation type
            date (AbsoluteDate): date at which to obtain the Observable-specific Signal Bias
        
        Returns:
            the value of the Observable-specific Signal Bias (meters for code and cycle for phase)
        
        
        """
        ...
    def getMaximumValidDateForObservation(self, obs: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
        Get the maximum valid date for a given observation type.
        
        Parameters:
            obs (ObservationType): observation type
        
        Returns:
            maximum valid date for the observation pair
        
        
        """
        ...
    def getMinimumValidDateForObservation(self, obs: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
        Get the minimum valid date for a given observation type.
        
        Parameters:
            obs (ObservationType): observation type
        
        Returns:
            minimum valid date for the observation pair
        
        
        """
        ...
    def getTimeSpanMap(self, obs: org.orekit.gnss.ObservationType) -> org.orekit.utils.TimeSpanMap[float]:
        """
        Get the TimeSpanMap object for a given observation type, for further operation on the object directly.
        
        Parameters:
            obs (ObservationType): observation type
        
        Returns:
            the time span map for a given observation code pair
        
        
        """
        ...

_ParseInfo__T = typing.TypeVar('_ParseInfo__T', bound=AbstractSinex)  # <T>
class ParseInfo(typing.Generic[_ParseInfo__T]):
    """
    Transient data used for parsing a SINEX file.
    
    Since:
        13.0
    """
    ...

class SatelliteDifferentialSignalBias:
    """
    Class based on DSB, used to store the data parsed in SinexBiasParser for Differential Signal Biases computed for satellites.
    
    Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are stored in a single DSB object.
    
    Since:
        12.0
    """
    def __init__(self, satellite: org.orekit.gnss.SatInSystem):
        """
        Simple constructor.
        
        Parameters:
            satellite (SatInSystem): satellite identifier
        
        
        """
        ...
    def getDsb(self) -> DifferentialSignalBias:
        """
        Get the DSB data for the current satellite.
        
        Returns:
            the DSB data for the current satellite
        
        
        """
        ...
    def getSatellite(self) -> org.orekit.gnss.SatInSystem:
        """
        Return the satellite identifier.
        
        Returns:
            the satellite identifier
        
        
        """
        ...

class SatelliteObservableSpecificSignalBias:
    """
    Class based on OSB, used to store the data parsed in SinexBiasParser for Observation Signal Biases computed for satellites.
    
    Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are stored in a single OSB object.
    
    Since:
        13.0
    """
    def __init__(self, satellite: org.orekit.gnss.SatInSystem):
        """
        Simple constructor.
        
        Parameters:
            satellite (SatInSystem): satellite identifier
        
        
        """
        ...
    def getOsb(self) -> ObservableSpecificSignalBias:
        """
        Get the OSB data for the current satellite.
        
        Returns:
            the OSB data for the current satellite
        
        
        """
        ...
    def getSatellite(self) -> org.orekit.gnss.SatInSystem:
        """
        Return the satellite identifier.
        
        Returns:
            the satellite identifier
        
        
        """
        ...

class SinexEopEntry(org.orekit.time.TimeStamped):
    """
    Container for EOP entry read in a Sinex file.
    
    Since:
        11.2
    """
    def __init__(self, epoch: org.orekit.time.AbsoluteDate):
        """
        Constructor.
        
        Parameters:
            epoch (AbsoluteDate): epoch of the data
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getLod(self) -> float:
        """
        Get the length of day.
        
        Returns:
            the length of day in seconds
        
        
        """
        ...
    def getNutLn(self) -> float:
        """
        Get the nutation correction in longitude.
        
        Returns:
            the nutation correction in longitude in radians
        
        
        """
        ...
    def getNutOb(self) -> float:
        """
        Get the nutation correction in obliquity.
        
        Returns:
            the nutation correction in obliquity in radians
        
        
        """
        ...
    def getNutX(self) -> float:
        """
        Get the nutation correction X.
        
        Returns:
            the nutation correction X in radians
        
        
        """
        ...
    def getNutY(self) -> float:
        """
        Get the nutation correction Y.
        
        Returns:
            the nutation correction Y in radians
        
        
        """
        ...
    def getUt1MinusUtc(self) -> float:
        """
        Get the UT1-UTC offset.
        
        Returns:
            the UT1-UTC offset in seconds
        
        
        """
        ...
    def getXPo(self) -> float:
        """
        Get the X polar motion.
        
        Returns:
            the X polar motion in radians
        
        
        """
        ...
    def getYPo(self) -> float:
        """
        Get the Y polar motion.
        
        Returns:
            the Y polar motion in radians
        
        
        """
        ...
    def setLod(self, lod: float) -> None:
        """
        Set the length of day.
        
        Parameters:
            lod (double): the length of day to set in seconds
        
        
        """
        ...
    def setNutLn(self, nutLn: float) -> None:
        """
        Set the nutation correction in longitude.
        
        Parameters:
            nutLn (double): the nutation correction in longitude to set in radians
        
        
        """
        ...
    def setNutOb(self, nutOb: float) -> None:
        """
        Set the nutation correction in obliquity.
        
        Parameters:
            nutOb (double): the nutation correction in obliquity to set in radians
        
        
        """
        ...
    def setNutX(self, nutX: float) -> None:
        """
        Set the nutation correction X.
        
        Parameters:
            nutX (double): the nutation correction X to set in radians
        
        
        """
        ...
    def setNutY(self, nutY: float) -> None:
        """
        Set the nutation correction Y.
        
        Parameters:
            nutY (double): the nutation correction Y to set in radians
        
        
        """
        ...
    def setUt1MinusUtc(self, ut1MinusUtc: float) -> None:
        """
        Set the UT1-UTC offset.
        
        Parameters:
            ut1MinusUtc (double): the value to set in seconds
        
        
        """
        ...
    def setxPo(self, xPo: float) -> None:
        """
        Set the X polar motion.
        
        Parameters:
            xPo (double): the X polar motion to set in radians
        
        
        """
        ...
    def setyPo(self, yPo: float) -> None:
        """
        Set the Y polar motion.
        
        Parameters:
            yPo (double): the Y polar motion to set in radians
        
        
        """
        ...
    def toEopEntry(self, converter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, version: org.orekit.frames.ITRFVersion, scale: org.orekit.time.TimeScale) -> org.orekit.frames.EOPEntry:
        """
        Converts to an EOPEntry.
        
        Parameters:
            converter (NutationCorrectionConverter): converter to use for nutation corrections
            version (ITRFVersion): ITRF version
            scale (TimeScale): time scale for epochs
        
        Returns:
            an EOPEntry
        
        
        """
        ...

class Station:
    """
    Station model.
    
    Since Orekit 11.1, this class handles multiple site antenna eccentricity. The getEccentricities method can be used to access the site antenna eccentricity values for a given epoch.
    
    Since:
        10.3
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def addAntennaKeyValidBefore(self, entry: AntennaKey, latestValidityDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Add a antenna key entry valid before a limit date.
        
        Using addAntennaKeyValidBefore(entry, t) will make entry valid in ]-∞, t[ (note the open bracket).
        
        Parameters:
            entry (AntennaKey): antenna key entry
            latestValidityDate (AbsoluteDate): date before which the entry is valid (must be different from all dates already used for transitions)
        
        Since:
            12.0
        
        
        """
        ...
    def addPsdCorrectionValidAfter(self, entry: org.orekit.models.earth.displacement.PsdCorrection, earliestValidityDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Add a Post-Seismic Deformation entry valid after a limit date.
        
        Using addPsdCorrectionValidAfter(entry, t) will make entry valid in [t, +∞[ (note the closed bracket).
        
        Parameters:
            entry (PsdCorrection): Post-Seismic Deformation entry
            earliestValidityDate (AbsoluteDate): date after which the entry is valid (must be different from all dates already used for transitions)
        
        Since:
            12.1
        
        
        """
        ...
    def addStationEccentricitiesValidBefore(self, entry: org.hipparchus.geometry.euclidean.threed.Vector3D, latestValidityDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Add a station eccentricity vector entry valid before a limit date.
        
        Using addStationEccentricitiesValidBefore(entry, t) will make entry valid in ]-∞, t[ (note the open bracket).
        
        Parameters:
            entry (Vector3D): station eccentricity vector entry
            latestValidityDate (AbsoluteDate): date before which the entry is valid (must be different from all dates already used for transitions)
        
        Since:
            11.1
        
        
        """
        ...
    def getAntennaKey(self, date: org.orekit.time.AbsoluteDate) -> AntennaKey:
        """
        Get the antenna key for the given epoch. If there is no antenna keys for the given epoch, an exception is thrown.
        
        Parameters:
            date (AbsoluteDate): epoch
        
        Returns:
            antenna key
        
        Since:
            13.0
        
        
        """
        ...
    def getAntennaKeyTimeSpanMap(self) -> org.orekit.utils.TimeSpanMap[AntennaKey]:
        """
        Get the TimeSpanMap of site antenna type.
        
        Returns:
            the TimeSpanMap of site antenna type
        
        Since:
            12.0
        
        
        """
        ...
    def getDomes(self) -> str:
        """
        Get the site DOMES number.
        
        Returns:
            the DOMES number
        
        
        """
        ...
    def getEccRefSystem(self) -> 'Station.ReferenceSystem':
        """
        Get the reference system used to define the eccentricity vector (local or cartesian).
        
        Returns:
            the reference system used to define the eccentricity vector
        
        
        """
        ...
    def getEccentricities(self, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the station antenna eccentricities for the given epoch.
        
        Vector convention: X-Y-Z or UP-NORTH-EAST. See getEccRefSystem method.
        
        If there is no eccentricity values for the given epoch, an exception is thrown.
        
        Parameters:
            date (AbsoluteDate): epoch
        
        Returns:
            station antenna eccentricities (m)
        
        Since:
            11.1
        
        
        """
        ...
    def getEccentricitiesTimeSpanMap(self) -> org.orekit.utils.TimeSpanMap[org.hipparchus.geometry.euclidean.threed.Vector3D]:
        """
        Get the TimeSpanMap of site antenna eccentricities.
        
        Returns:
            the TimeSpanMap of site antenna eccentricities
        
        Since:
            11.1
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the coordinates reference epoch.
        
        Returns:
            the coordinates reference epoch
        
        
        """
        ...
    def getPhaseCenters(self, date: org.orekit.time.AbsoluteDate) -> java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]:
        """
        Get the phase centers for the given epoch. If there is no phase centers for the given epoch, an exception is thrown.
        
        Parameters:
            date (AbsoluteDate): epoch
        
        Returns:
            phase centers
        
        Since:
            13.0
        
        
        """
        ...
    def getPhaseCentersMap(self) -> org.orekit.utils.TimeSpanMap[java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]:
        """
        Get the TimeSpanMap of phase centers.
        
        Returns:
            the TimeSpanMap of phase centers
        
        Since:
            13.0
        
        
        """
        ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the station position.
        
        Returns:
            the station position (m)
        
        
        """
        ...
    def getPsdTimeSpanMap(self) -> org.orekit.utils.TimeSpanMap[java.util.List[org.orekit.models.earth.displacement.PsdCorrection]]:
        """
        Get the TimeSpanMap of Post-Seismic Deformation.
        
        Returns:
            the TimeSpanMap of Post-Seismic Deformation
        
        Since:
            12.1
        
        
        """
        ...
    def getSiteCode(self) -> str:
        """
        Get the site code (station identifier).
        
        Returns:
            the site code
        
        
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
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the station velocity.
        
        Returns:
            the station velocity (m/s)
        
        
        """
        ...
    def setDomes(self, domes: str) -> None:
        """
        Set the DOMES number.
        
        Parameters:
            domes (String): the DOMES number to set
        
        
        """
        ...
    def setEccRefSystem(self, eccRefSystem: 'Station.ReferenceSystem') -> None:
        """
        Set the reference system used to define the eccentricity vector (local or cartesian).
        
        Parameters:
            eccRefSystem (ReferenceSystem): the reference system used to define the eccentricity vector
        
        
        """
        ...
    def setEpoch(self, epoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the coordinates reference epoch.
        
        Parameters:
            epoch (AbsoluteDate): the epoch to set
        
        
        """
        ...
    def setPosition(self, position: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the station position.
        
        Parameters:
            position (Vector3D): the position to set
        
        
        """
        ...
    def setSiteCode(self, siteCode: str) -> None:
        """
        Set the site code (station identifier).
        
        Parameters:
            siteCode (String): the site code to set
        
        
        """
        ...
    def setValidFrom(self, validFrom: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the start of validity.
        
        Parameters:
            validFrom (AbsoluteDate): the start of validity to set
        
        
        """
        ...
    def setValidUntil(self, validUntil: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the end of validity.
        
        Parameters:
            validUntil (AbsoluteDate): the end of validity to set
        
        
        """
        ...
    def setVelocity(self, velocity: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the station velocity.
        
        Parameters:
            velocity (Vector3D): the velocity to set
        
        
        """
        ...
    class ReferenceSystem(java.lang.Enum['Station.ReferenceSystem']):
        UNE: typing.ClassVar['Station.ReferenceSystem'] = ...
        XYZ: typing.ClassVar['Station.ReferenceSystem'] = ...
        @staticmethod
        def getEccRefSystem(string: str) -> 'Station.ReferenceSystem': ...
        def getName(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Station.ReferenceSystem': ...
        @staticmethod
        def values() -> typing.MutableSequence['Station.ReferenceSystem']: ...

class StationDifferentialSignalBias:
    """
    Container for DifferentialSignalBias associated to one station.
    
    Since:
        12.0
    """
    def __init__(self, siteCode: str):
        """
        Simple constructor.
        
        Parameters:
            siteCode (String): the site code (station identifier)
        
        
        """
        ...
    def getAvailableSatelliteSystems(self) -> java.util.Collection[org.orekit.gnss.SatelliteSystem]:
        """
        Get the satellite systems available for the station.
        
        Returns:
            a Set containing all SatelliteSystems available for DSB computation.
        
        
        """
        ...
    def getDsb(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> DifferentialSignalBias:
        """
        Get the DSB data for a given satellite system.
        
        Parameters:
            satelliteSystem (SatelliteSystem): satellite system
        
        Returns:
            the DSB data corresponding to the satellite system
        
        
        """
        ...
    def getSiteCode(self) -> str:
        """
        Get the site code (station identifier).
        
        Returns:
            the site code
        
        
        """
        ...

class StationObservableSpecificSignalBias:
    """
    Class based on OSB, used to store the data parsed in SinexBiasParser for Observation Signal Biases computed for stations.
    
    Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are stored in a Map of OSB, identified by the SatelliteSystem
    
    Since:
        13.0
    """
    def __init__(self, siteCode: str):
        """
        Simple constructor.
        
        Parameters:
            siteCode (String): the site code (station identifier)
        
        
        """
        ...
    def getAvailableSatelliteSystems(self) -> java.util.Collection[org.orekit.gnss.SatelliteSystem]:
        """
        Get the satellite systems available for the station.
        
        Returns:
            a Set containing all SatelliteSystems available for DSB computation.
        
        
        """
        ...
    def getOsb(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> ObservableSpecificSignalBias:
        """
        Get the OSB data for a given satellite system.
        
        Parameters:
            satelliteSystem (SatelliteSystem): satellite system
        
        Returns:
            the OSB data corresponding to the satellite system
        
        
        """
        ...
    def getSiteCode(self) -> str:
        """
        Get the site code (station identifier).
        
        Returns:
            the site code
        
        
        """
        ...

class Sinex(AbstractSinex):
    """
    Container for Solution INdependent EXchange (SINEX) files.
    
    Since:
        13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, creationDate: org.orekit.time.AbsoluteDate, startDate: org.orekit.time.AbsoluteDate, endDate: org.orekit.time.AbsoluteDate, satellitesPhaseCenters: typing.Union[java.util.Map[org.orekit.gnss.SatInSystem, typing.Union[java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D], typing.Mapping[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]], typing.Mapping[org.orekit.gnss.SatInSystem, typing.Union[java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D], typing.Mapping[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]]], stations: typing.Union[java.util.Map[str, Station], typing.Mapping[str, Station]], eop: typing.Union[java.util.Map[org.orekit.time.AbsoluteDate, SinexEopEntry], typing.Mapping[org.orekit.time.AbsoluteDate, SinexEopEntry]]):
        """
        Simple constructor.
        
        Parameters:
            timeScales (TimeScales): time scales
            creationDate (AbsoluteDate): SINEX file creation date
            startDate (AbsoluteDate): start time of the data used in the Sinex solution
            endDate (AbsoluteDate): end time of the data used in the Sinex solution
            satellitesPhaseCenters (Map<SatInSystem, Map<GnssSignal, Vector3D>>): satellites phase centers
            stations (Map<String, Station> stations): station data
            eop (Map<AbsoluteDate, SinexEopEntry> eop): Earth Orientation Parameters data
        
        
        """
        ...
    def getEopLoader(self, itrfVersion: org.orekit.frames.ITRFVersion) -> org.orekit.frames.EopHistoryLoader:
        """
        Get the parsed EOP data.
        
        Parameters:
            itrfVersion (ITRFVersion): ITRF version corresponding to the entries
        
        Returns:
            loader for EOP data
        
        
        """
        ...
    def getSatellitesPhaseCenters(self) -> java.util.Map[org.orekit.gnss.SatInSystem, java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]:
        """
        Get the parsed satellites phase centers.
        
        Returns:
            unmodifiable view of parsed satellites phase centers
        
        
        """
        ...
    def getStations(self) -> java.util.Map[str, Station]:
        """
        Get the parsed station data.
        
        Returns:
            unmodifiable view of parsed station data
        
        
        """
        ...

class SinexBias(AbstractSinex):
    """
    Container for Solution INdependent EXchange (SINEX) files.
    
    Since:
        13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, creationDate: org.orekit.time.AbsoluteDate, startDate: org.orekit.time.AbsoluteDate, endDate: org.orekit.time.AbsoluteDate, description: BiasDescription, stationsDsb: typing.Union[java.util.Map[str, StationDifferentialSignalBias], typing.Mapping[str, StationDifferentialSignalBias]], satellitesDsb: typing.Union[java.util.Map[org.orekit.gnss.SatInSystem, SatelliteDifferentialSignalBias], typing.Mapping[org.orekit.gnss.SatInSystem, SatelliteDifferentialSignalBias]], stationsOsb: typing.Union[java.util.Map[str, StationObservableSpecificSignalBias], typing.Mapping[str, StationObservableSpecificSignalBias]], satellitesOsb: typing.Union[java.util.Map[org.orekit.gnss.SatInSystem, SatelliteObservableSpecificSignalBias], typing.Mapping[org.orekit.gnss.SatInSystem, SatelliteObservableSpecificSignalBias]]):
        """
        Simple constructor.
        
        Parameters:
            timeScales (TimeScales): time scales
            creationDate (AbsoluteDate): SINEX file creation date
            startDate (AbsoluteDate): start time of the data used in the Sinex solution
            endDate (AbsoluteDate): end time of the data used in the Sinex solution
            description (BiasDescription): bias description
            stationsDsb (Map<String, StationDifferentialSignalBias> stationsDsb): DSB data for stations
            satellitesDsb (Map<SatInSystem, SatelliteDifferentialSignalBias> satellitesDsb): DSB data for satellites
            stationsOsb (Map<String, StationObservableSpecificSignalBias> stationsOsb): OSB data for stations
            satellitesOsb (Map<SatInSystem, SatelliteObservableSpecificSignalBias> satellitesOsb): OSB data for satellites
        
        
        """
        ...
    def getDescription(self) -> BiasDescription:
        """
        Get the bias description.
        
        Returns:
            bias description
        
        
        """
        ...
    def getSatellitesDsb(self) -> java.util.Map[org.orekit.gnss.SatInSystem, SatelliteDifferentialSignalBias]:
        """
        Get the DSB data for satellites.
        
        Returns:
            DSB data for satellites
        
        
        """
        ...
    def getSatellitesOsb(self) -> java.util.Map[org.orekit.gnss.SatInSystem, SatelliteObservableSpecificSignalBias]:
        """
        Get the OSB data for satellites.
        
        Returns:
            OSB data for satellites
        
        
        """
        ...
    def getStationsDsb(self) -> java.util.Map[str, StationDifferentialSignalBias]:
        """
        Get the DSB data for stations.
        
        Returns:
            DSB data for stations, indexed by station site code
        
        
        """
        ...
    def getStationsOsb(self) -> java.util.Map[str, StationObservableSpecificSignalBias]:
        """
        Get the OSB data for stations.
        
        Returns:
            OSB data for stations, indexed by station site code
        
        
        """
        ...

class SinexBiasParseInfo(ParseInfo[SinexBias]):
    """
    Parse information for Solution INdependent EXchange (SINEX) bias files.
    
    Since:
        13.0
    """
    ...

class SinexBiasParser(AbstractSinexParser[SinexBias, SinexBiasParseInfo]):
    """
    Parser for Solution INdependent EXchange (SINEX) bias files.
    
    Since:
        13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, typeBuilder: typing.Union[java.util.function.BiFunction[org.orekit.gnss.SatelliteSystem, str, org.orekit.gnss.ObservationType], typing.Callable[[org.orekit.gnss.SatelliteSystem, str], org.orekit.gnss.ObservationType]]):
        """
        Simple constructor.
        
        Parameters:
            timeScales (TimeScales): time scales
            typeBuilder (BiFunction<? super SatelliteSystem, ? super String, ? extends ObservationType> typeBuilder): mapper from string to observation type (typically SinexBiasParser::defaultTypeBuilder if the file uses only
                predefined types)
        
        Also see:
            defaultTypeBuilder
        
        
        """
        ...
    @staticmethod
    def defaultTypeBuilder(ignoredSystem: org.orekit.gnss.SatelliteSystem, typeName: str) -> org.orekit.gnss.ObservationType:
        """
        Default type builder.
        
        This default type builder directly calls valueOf
        
        Parameters:
            ignoredSystem (SatelliteSystem): satellite system (ignored here)
            typeName (String): name of the observation type
        
        Returns:
            observation type
        
        
        """
        ...

class SinexParseInfo(ParseInfo[Sinex]):
    """
    Parse information for Solution INdependent EXchange (SINEX) files.
    
    Since:
        13.0
    """
    ...

class SinexParser(AbstractSinexParser[Sinex, SinexParseInfo]):
    """
    Parser for Solution INdependent EXchange (SINEX) files.
    
    The parser can be used to load several data types contained in Sinex files. The current supported data are: station coordinates, site eccentricities, EOP.
    
    The parsing of EOP parameters for multiple data sources in different SinexParser objects might pose a problem in case validity dates are overlapping. As Sinex daily solution files provide a single EOP entry, the Sinex parser will add points at the limits of data dates (startDate, endDate) of the Sinex file, which in case of overlap will lead to inconsistencies in the final EOPHistory object. Multiple data sources can be parsed using a single SinexParser to overcome this issue.
    
    Since:
        13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales):
        """
        Simple constructor.
        
        Parameters:
            timeScales (TimeScales): time scales
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.sinex")``.

    AbstractSinex: typing.Type[AbstractSinex]
    AbstractSinexParser: typing.Type[AbstractSinexParser]
    AntennaKey: typing.Type[AntennaKey]
    BiasDescription: typing.Type[BiasDescription]
    DifferentialSignalBias: typing.Type[DifferentialSignalBias]
    LineParser: typing.Type[LineParser]
    ObservableSpecificSignalBias: typing.Type[ObservableSpecificSignalBias]
    ParseInfo: typing.Type[ParseInfo]
    SatelliteDifferentialSignalBias: typing.Type[SatelliteDifferentialSignalBias]
    SatelliteObservableSpecificSignalBias: typing.Type[SatelliteObservableSpecificSignalBias]
    Sinex: typing.Type[Sinex]
    SinexBias: typing.Type[SinexBias]
    SinexBiasParseInfo: typing.Type[SinexBiasParseInfo]
    SinexBiasParser: typing.Type[SinexBiasParser]
    SinexEopEntry: typing.Type[SinexEopEntry]
    SinexParseInfo: typing.Type[SinexParseInfo]
    SinexParser: typing.Type[SinexParser]
    Station: typing.Type[Station]
    StationDifferentialSignalBias: typing.Type[StationDifferentialSignalBias]
    StationObservableSpecificSignalBias: typing.Type[StationObservableSpecificSignalBias]
