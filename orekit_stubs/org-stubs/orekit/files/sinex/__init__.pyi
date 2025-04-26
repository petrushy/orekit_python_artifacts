
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
    public class AbstractSinex extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base container for Solution INdependent EXchange (SINEX) files.
    
        Since:
            13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, absoluteDate3: org.orekit.time.AbsoluteDate): ...
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
    public abstract class AbstractSinexParser<T extends :class:`~org.orekit.files.sinex.AbstractSinex`, P extends :class:`~org.orekit.files.sinex.ParseInfo`<T>> extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
    def parse(self, *dataSource: org.orekit.data.DataSource) -> _AbstractSinexParser__T:
        """
            Parse one or more SINEX files.
        
            Parameters:
                sources (:class:`~org.orekit.data.DataSource`...): sources providing the data to parse
        
            Returns:
                parsed file combining all sources
        
        
        """
        ...

class AntennaKey:
    """
    public class AntennaKey extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Key for antenna.
    
        Since:
            13.0
    """
    OTHER_RADOME_CODE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` OTHER_RADOME_CODE
    
        Constant matching other radome codes.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ANY_SERIAL_NUMBER: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ANY_SERIAL_NUMBER
    
        Constant matching any serial numbers.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, string2: str, string3: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
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
        
            Overrides:
                :meth:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def matchingCandidates(self) -> java.util.List['AntennaKey']: ...

class BiasDescription:
    """
    public class BiasDescription extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class to store the bias description parameters.
    
        This class gives important parameters from the analysis and defines the fields in the block ’BIAS/SOLUTION’ of the
        loaded Sinex file.
    
        Since:
            12.0
    """
    def __init__(self): ...
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
    def setBiasMode(self, string: str) -> None:
        """
            Set the bias mode.
        
            Parameters:
                biasMode (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the bias mode to set
        
        
        """
        ...
    def setDeterminationMethod(self, string: str) -> None:
        """
            Set the determination mode used to generate the bias results.
        
            Parameters:
                determinationMethod (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the determination method to set
        
        
        """
        ...
    def setObservationSampling(self, int: int) -> None:
        """
            Set the observation sampling interval used for data analysis.
        
            Parameters:
                observationSampling (int): the observation sampling to set in seconds
        
        
        """
        ...
    def setParameterSpacing(self, int: int) -> None:
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
                timeSystem (:class:`~org.orekit.gnss.TimeSystem`): the time system to set
        
        
        """
        ...

class DifferentialSignalBias:
    """
    public class DifferentialSignalBias extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for differential signal bias for a single link endpoint (either emitter or receiver).
    
        This class is made to handle both station and satellite DSB data. Bias values are stored in TimeSpanMaps associated with
        a given pair of observation types. Those TimeSpanMaps are stored in a Map, which associate a pair of observation types
        to a TimeSpanMap of double values.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def addBias(self, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, double: float) -> None:
        """
            Add a bias.
        
            Parameters:
                obs1 (:class:`~org.orekit.gnss.ObservationType`): first observation used for the DSB computation
                obs2 (:class:`~org.orekit.gnss.ObservationType`): second observation used for the DSB computation
                spanBegin (:class:`~org.orekit.time.AbsoluteDate`): beginning of the validity span for this bias value
                spanEnd (:class:`~org.orekit.time.AbsoluteDate`): end of the validity span for this bias value
                biasValue (double): DSB bias value (meters for code and cycle for phase)
        
        
        """
        ...
    def getAvailableObservationPairs(self) -> java.util.HashSet[org.hipparchus.util.Pair[org.orekit.gnss.ObservationType, org.orekit.gnss.ObservationType]]: ...
    def getBias(self, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the Differential Signal Bias for a given observation pair at a given date.
        
            Parameters:
                obs1 (:class:`~org.orekit.gnss.ObservationType`): first observation type
                obs2 (:class:`~org.orekit.gnss.ObservationType`): second observation type
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which to obtain the DSB
        
            Returns:
                the value of the DSB (meters for code and cycle for phase)
        
        
        """
        ...
    def getMaximumValidDateForObservationPair(self, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
            Get the maximum valid date for a given observation pair.
        
            Parameters:
                obs1 (:class:`~org.orekit.gnss.ObservationType`): first observation type
                obs2 (:class:`~org.orekit.gnss.ObservationType`): second observation type
        
            Returns:
                maximum valid date for the observation pair
        
        
        """
        ...
    def getMinimumValidDateForObservationPair(self, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
            Get the minimum valid date for a given observation pair.
        
            Parameters:
                obs1 (:class:`~org.orekit.gnss.ObservationType`): first observation type
                obs2 (:class:`~org.orekit.gnss.ObservationType`): second observation type
        
            Returns:
                minimum valid date for the observation pair
        
        
        """
        ...

_LineParser__T = typing.TypeVar('_LineParser__T', bound='ParseInfo')  # <T>
class LineParser(typing.Generic[_LineParser__T]):
    """
    public interface LineParser<T extends :class:`~org.orekit.files.sinex.ParseInfo`<?>>
    
        Parser class for one line.
    
        Since:
            13.0
    """
    def allowedNextParsers(self, t: _LineParser__T) -> java.lang.Iterable['LineParser'[_LineParser__T]]: ...
    def parseIfRecognized(self, t: _LineParser__T) -> bool:
        """
            Parse a line if recognized.
        
            Parameters:
                parseInfo (:class:`~org.orekit.files.sinex.LineParser`): holder for transient data
        
            Returns:
                true if line was recognized
        
        
        """
        ...

class ObservableSpecificSignalBias:
    """
    public class ObservableSpecificSignalBias extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for observation-specific signal bias for a single link endpoint (either emitter or receiver).
    
        This class is made to handle both station and satellite OSB data. Bias values are stored in TimeSpanMaps associated with
        a given observation type. Those TimeSpanMaps are stored in a Map, which associate an observation code to a TimeSpanMap
        of double values.
    
        Since:
            13.0
    """
    def __init__(self): ...
    def addBias(self, observationType: org.orekit.gnss.ObservationType, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, double: float) -> None:
        """
            Add a bias.
        
            Parameters:
                obs (:class:`~org.orekit.gnss.ObservationType`): observation used for the OSB computation
                spanBegin (:class:`~org.orekit.time.AbsoluteDate`): beginning of the validity span for this bias value
                spanEnd (:class:`~org.orekit.time.AbsoluteDate`): end of the validity span for this bias value
                biasValue (double): Observable-specific Signal Bias value (meters for code and cycle for phase)
        
        
        """
        ...
    def getAvailableObservations(self) -> java.util.HashSet[org.orekit.gnss.ObservationType]: ...
    def getBias(self, observationType: org.orekit.gnss.ObservationType, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the Observable-specific Signal Bias for a given observation type at a given date.
        
            Parameters:
                obs (:class:`~org.orekit.gnss.ObservationType`): observation type
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which to obtain the Observable-specific Signal Bias
        
            Returns:
                the value of the Observable-specific Signal Bias (meters for code and cycle for phase)
        
        
        """
        ...
    def getMaximumValidDateForObservation(self, observationType: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
            Get the maximum valid date for a given observation type.
        
            Parameters:
                obs (:class:`~org.orekit.gnss.ObservationType`): observation type
        
            Returns:
                maximum valid date for the observation pair
        
        
        """
        ...
    def getMinimumValidDateForObservation(self, observationType: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate:
        """
            Get the minimum valid date for a given observation type.
        
            Parameters:
                obs (:class:`~org.orekit.gnss.ObservationType`): observation type
        
            Returns:
                minimum valid date for the observation pair
        
        
        """
        ...

_ParseInfo__T = typing.TypeVar('_ParseInfo__T', bound=AbstractSinex)  # <T>
class ParseInfo(typing.Generic[_ParseInfo__T]):
    """
    public abstract class ParseInfo<T extends :class:`~org.orekit.files.sinex.AbstractSinex`> extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Transient data used for parsing a SINEX file.
    
        Since:
            13.0
    """
    ...

class SatelliteDifferentialSignalBias:
    """
    public class SatelliteDifferentialSignalBias extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class based on DSB, used to store the data parsed in :class:`~org.orekit.files.sinex.SinexBiasParser` for Differential
        Signal Biases computed for satellites.
    
        Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are
        stored in a single DSB object.
    
        Since:
            12.0
    """
    def __init__(self, satInSystem: org.orekit.gnss.SatInSystem): ...
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
    public class SatelliteObservableSpecificSignalBias extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class based on OSB, used to store the data parsed in :class:`~org.orekit.files.sinex.SinexBiasParser` for Observation
        Signal Biases computed for satellites.
    
        Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are
        stored in a single OSB object.
    
        Since:
            13.0
    """
    def __init__(self, satInSystem: org.orekit.gnss.SatInSystem): ...
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
    public class SinexEopEntry extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Container for EOP entry read in a Sinex file.
    
        Since:
            11.2
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
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
    def setLod(self, double: float) -> None:
        """
            Set the length of day.
        
            Parameters:
                lod (double): the length of day to set in seconds
        
        
        """
        ...
    def setNutLn(self, double: float) -> None:
        """
            Set the nutation correction in longitude.
        
            Parameters:
                nutLn (double): the nutation correction in longitude to set in radians
        
        
        """
        ...
    def setNutOb(self, double: float) -> None:
        """
            Set the nutation correction in obliquity.
        
            Parameters:
                nutOb (double): the nutation correction in obliquity to set in radians
        
        
        """
        ...
    def setNutX(self, double: float) -> None:
        """
            Set the nutation correction X.
        
            Parameters:
                nutX (double): the nutation correction X to set in radians
        
        
        """
        ...
    def setNutY(self, double: float) -> None:
        """
            Set the nutation correction Y.
        
            Parameters:
                nutY (double): the nutation correction Y to set in radians
        
        
        """
        ...
    def setUt1MinusUtc(self, double: float) -> None:
        """
            Set the UT1-UTC offset.
        
            Parameters:
                ut1MinusUtc (double): the value to set in seconds
        
        
        """
        ...
    def setxPo(self, double: float) -> None:
        """
            Set the X polar motion.
        
            Parameters:
                xPo (double): the X polar motion to set in radians
        
        
        """
        ...
    def setyPo(self, double: float) -> None:
        """
            Set the Y polar motion.
        
            Parameters:
                yPo (double): the Y polar motion to set in radians
        
        
        """
        ...
    def toEopEntry(self, nutationCorrectionConverter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, iTRFVersion: org.orekit.frames.ITRFVersion, timeScale: org.orekit.time.TimeScale) -> org.orekit.frames.EOPEntry:
        """
            Converts to an :class:`~org.orekit.frames.EOPEntry`.
        
            Parameters:
                converter (:class:`~org.orekit.utils.IERSConventions.NutationCorrectionConverter`): converter to use for nutation corrections
                version (:class:`~org.orekit.frames.ITRFVersion`): ITRF version
                scale (:class:`~org.orekit.time.TimeScale`): time scale for epochs
        
            Returns:
                an :code:`EOPEntry`
        
        
        """
        ...

class Station:
    """
    public class Station extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Station model.
    
        Since Orekit 11.1, this class handles multiple site antenna eccentricity. The
        :meth:`~org.orekit.files.sinex.Station.getEccentricities` method can be used to access the site antenna eccentricity
        values for a given epoch.
    
        Since:
            10.3
    """
    def __init__(self): ...
    def addAntennaKeyValidBefore(self, antennaKey: AntennaKey, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a antenna key entry valid before a limit date.
        
        
            Using :code:`addAntennaKeyValidBefore(entry, t)` will make :code:`entry` valid in ]-∞, t[ (note the open bracket).
        
            Parameters:
                entry (:class:`~org.orekit.files.sinex.AntennaKey`): antenna key entry
                latestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date before which the entry is valid (must be different from **all** dates already used for transitions)
        
            Since:
                12.0
        
        
        """
        ...
    def addPsdCorrectionValidAfter(self, psdCorrection: org.orekit.models.earth.displacement.PsdCorrection, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a Post-Seismic Deformation entry valid after a limit date.
        
        
            Using :code:`addPsdCorrectionValidAfter(entry, t)` will make :code:`entry` valid in [t, +∞[ (note the closed bracket).
        
            Parameters:
                entry (:class:`~org.orekit.models.earth.displacement.PsdCorrection`): Post-Seismic Deformation entry
                earliestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date after which the entry is valid (must be different from **all** dates already used for transitions)
        
            Since:
                12.1
        
        
        """
        ...
    def addStationEccentricitiesValidBefore(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a station eccentricity vector entry valid before a limit date.
        
        
            Using :code:`addStationEccentricitiesValidBefore(entry, t)` will make :code:`entry` valid in ]-∞, t[ (note the open
            bracket).
        
            Parameters:
                entry (:class:`~org.orekit.files.sinex.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): station eccentricity vector entry
                latestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date before which the entry is valid (must be different from **all** dates already used for transitions)
        
            Since:
                11.1
        
        
        """
        ...
    def getAntennaKey(self, absoluteDate: org.orekit.time.AbsoluteDate) -> AntennaKey:
        """
            Get the antenna key for the given epoch. If there is no antenna keys for the given epoch, an exception is thrown.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): epoch
        
            Returns:
                antenna key
        
            Since:
                13.0
        
        
        """
        ...
    def getAntennaKeyTimeSpanMap(self) -> org.orekit.utils.TimeSpanMap[AntennaKey]: ...
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
    def getEccentricities(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the station antenna eccentricities for the given epoch.
        
            Vector convention: X-Y-Z or UP-NORTH-EAST. See :meth:`~org.orekit.files.sinex.Station.getEccRefSystem` method.
        
            If there is no eccentricity values for the given epoch, an exception is thrown.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): epoch
        
            Returns:
                station antenna eccentricities (m)
        
            Since:
                11.1
        
        
        """
        ...
    def getEccentricitiesTimeSpanMap(self) -> org.orekit.utils.TimeSpanMap[org.hipparchus.geometry.euclidean.threed.Vector3D]: ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the coordinates reference epoch.
        
            Returns:
                the coordinates reference epoch
        
        
        """
        ...
    def getPhaseCenters(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]: ...
    def getPhaseCentersMap(self) -> org.orekit.utils.TimeSpanMap[java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]: ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the station position.
        
            Returns:
                the station position (m)
        
        
        """
        ...
    def getPsdTimeSpanMap(self) -> org.orekit.utils.TimeSpanMap[java.util.List[org.orekit.models.earth.displacement.PsdCorrection]]: ...
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
    def setDomes(self, string: str) -> None:
        """
            Set the DOMES number.
        
            Parameters:
                domes (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the DOMES number to set
        
        
        """
        ...
    def setEccRefSystem(self, referenceSystem: 'Station.ReferenceSystem') -> None:
        """
            Set the reference system used to define the eccentricity vector (local or cartesian).
        
            Parameters:
                eccRefSystem (:class:`~org.orekit.files.sinex.Station.ReferenceSystem`): the reference system used to define the eccentricity vector
        
        
        """
        ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the coordinates reference epoch.
        
            Parameters:
                epoch (:class:`~org.orekit.time.AbsoluteDate`): the epoch to set
        
        
        """
        ...
    def setPosition(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the station position.
        
            Parameters:
                position (:class:`~org.orekit.files.sinex.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): the position to set
        
        
        """
        ...
    def setSiteCode(self, string: str) -> None:
        """
            Set the site code (station identifier).
        
            Parameters:
                siteCode (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the site code to set
        
        
        """
        ...
    def setValidFrom(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start of validity.
        
            Parameters:
                validFrom (:class:`~org.orekit.time.AbsoluteDate`): the start of validity to set
        
        
        """
        ...
    def setValidUntil(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the end of validity.
        
            Parameters:
                validUntil (:class:`~org.orekit.time.AbsoluteDate`): the end of validity to set
        
        
        """
        ...
    def setVelocity(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the station velocity.
        
            Parameters:
                velocity (:class:`~org.orekit.files.sinex.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): the velocity to set
        
        
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
    public class StationDifferentialSignalBias extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for :class:`~org.orekit.files.sinex.DifferentialSignalBias` associated to one station.
    
        Since:
            12.0
    """
    def __init__(self, string: str): ...
    def getAvailableSatelliteSystems(self) -> java.util.Collection[org.orekit.gnss.SatelliteSystem]: ...
    def getDsb(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> DifferentialSignalBias:
        """
            Get the DSB data for a given satellite system.
        
            Parameters:
                satelliteSystem (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
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
    public class StationObservableSpecificSignalBias extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class based on OSB, used to store the data parsed in :class:`~org.orekit.files.sinex.SinexBiasParser` for Observation
        Signal Biases computed for stations.
    
        Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are
        stored in a Map of OSB, identified by the :class:`~org.orekit.gnss.SatelliteSystem`
    
        Since:
            13.0
    """
    def __init__(self, string: str): ...
    def getAvailableSatelliteSystems(self) -> java.util.Collection[org.orekit.gnss.SatelliteSystem]: ...
    def getOsb(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> ObservableSpecificSignalBias:
        """
            Get the OSB data for a given satellite system.
        
            Parameters:
                satelliteSystem (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
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
    public class Sinex extends :class:`~org.orekit.files.sinex.AbstractSinex`
    
        Container for Solution INdependent EXchange (SINEX) files.
    
        Since:
            13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, absoluteDate3: org.orekit.time.AbsoluteDate, map: typing.Union[java.util.Map[org.orekit.gnss.SatInSystem, typing.Union[java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D], typing.Mapping[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]], typing.Mapping[org.orekit.gnss.SatInSystem, typing.Union[java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D], typing.Mapping[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]]], map2: typing.Union[java.util.Map[str, Station], typing.Mapping[str, Station]], map3: typing.Union[java.util.Map[org.orekit.time.AbsoluteDate, SinexEopEntry], typing.Mapping[org.orekit.time.AbsoluteDate, SinexEopEntry]]): ...
    def getEopLoader(self, iTRFVersion: org.orekit.frames.ITRFVersion) -> org.orekit.frames.EopHistoryLoader:
        """
            Get the parsed EOP data.
        
            Parameters:
                itrfVersion (:class:`~org.orekit.frames.ITRFVersion`): ITRF version corresponding to the entries
        
            Returns:
                loader for EOP data
        
        
        """
        ...
    def getSatellitesPhaseCenters(self) -> java.util.Map[org.orekit.gnss.SatInSystem, java.util.Map[org.orekit.gnss.GnssSignal, org.hipparchus.geometry.euclidean.threed.Vector3D]]: ...
    def getStations(self) -> java.util.Map[str, Station]: ...

class SinexBias(AbstractSinex):
    """
    public class SinexBias extends :class:`~org.orekit.files.sinex.AbstractSinex`
    
        Container for Solution INdependent EXchange (SINEX) files.
    
        Since:
            13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, absoluteDate3: org.orekit.time.AbsoluteDate, biasDescription: BiasDescription, map: typing.Union[java.util.Map[str, StationDifferentialSignalBias], typing.Mapping[str, StationDifferentialSignalBias]], map2: typing.Union[java.util.Map[org.orekit.gnss.SatInSystem, SatelliteDifferentialSignalBias], typing.Mapping[org.orekit.gnss.SatInSystem, SatelliteDifferentialSignalBias]], map3: typing.Union[java.util.Map[str, StationObservableSpecificSignalBias], typing.Mapping[str, StationObservableSpecificSignalBias]], map4: typing.Union[java.util.Map[org.orekit.gnss.SatInSystem, SatelliteObservableSpecificSignalBias], typing.Mapping[org.orekit.gnss.SatInSystem, SatelliteObservableSpecificSignalBias]]): ...
    def getDescription(self) -> BiasDescription:
        """
            Get the bias description.
        
            Returns:
                bias description
        
        
        """
        ...
    def getSatellitesDsb(self) -> java.util.Map[org.orekit.gnss.SatInSystem, SatelliteDifferentialSignalBias]: ...
    def getSatellitesOsb(self) -> java.util.Map[org.orekit.gnss.SatInSystem, SatelliteObservableSpecificSignalBias]: ...
    def getStationsDsb(self) -> java.util.Map[str, StationDifferentialSignalBias]: ...
    def getStationsOsb(self) -> java.util.Map[str, StationObservableSpecificSignalBias]: ...

class SinexBiasParseInfo(ParseInfo[SinexBias]):
    """
    public class SinexBiasParseInfo extends :class:`~org.orekit.files.sinex.ParseInfo`<:class:`~org.orekit.files.sinex.SinexBias`>
    
        Parse information for Solution INdependent EXchange (SINEX) bias files.
    
        Since:
            13.0
    """
    ...

class SinexBiasParser(AbstractSinexParser[SinexBias, SinexBiasParseInfo]):
    """
    public class SinexBiasParser extends :class:`~org.orekit.files.sinex.AbstractSinexParser`<:class:`~org.orekit.files.sinex.SinexBias`, :class:`~org.orekit.files.sinex.SinexBiasParseInfo`>
    
        Parser for Solution INdependent EXchange (SINEX) bias files.
    
        Since:
            13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, biFunction: typing.Union[java.util.function.BiFunction[org.orekit.gnss.SatelliteSystem, str, org.orekit.gnss.ObservationType], typing.Callable[[org.orekit.gnss.SatelliteSystem, str], org.orekit.gnss.ObservationType]]): ...
    @staticmethod
    def defaultTypeBuilder(satelliteSystem: org.orekit.gnss.SatelliteSystem, string: str) -> org.orekit.gnss.ObservationType:
        """
            Default type builder.
        
            This default type builder directly calls :meth:`~org.orekit.gnss.PredefinedObservationType.valueOf`
        
            Parameters:
                ignoredSystem (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system (ignored here)
                typeName (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the observation type
        
            Returns:
                observation type
        
        
        """
        ...

class SinexParseInfo(ParseInfo[Sinex]):
    """
    public class SinexParseInfo extends :class:`~org.orekit.files.sinex.ParseInfo`<:class:`~org.orekit.files.sinex.Sinex`>
    
        Parse information for Solution INdependent EXchange (SINEX) files.
    
        Since:
            13.0
    """
    ...

class SinexParser(AbstractSinexParser[Sinex, SinexParseInfo]):
    """
    public class SinexParser extends :class:`~org.orekit.files.sinex.AbstractSinexParser`<:class:`~org.orekit.files.sinex.Sinex`, :class:`~org.orekit.files.sinex.SinexParseInfo`>
    
        Parser for Solution INdependent EXchange (SINEX) files.
    
        The parser can be used to load several data types contained in Sinex files. The current supported data are: station
        coordinates, site eccentricities, EOP.
    
        The parsing of EOP parameters for multiple data sources in different SinexParser objects might pose a problem in case
        validity dates are overlapping. As Sinex daily solution files provide a single EOP entry, the Sinex parser will add
        points at the limits of data dates (startDate, endDate) of the Sinex file, which in case of overlap will lead to
        inconsistencies in the final EOPHistory object. Multiple data sources can be parsed using a single SinexParser to
        overcome this issue.
    
        Since:
            13.0
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales): ...


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
