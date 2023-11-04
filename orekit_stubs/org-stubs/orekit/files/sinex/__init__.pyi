import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.util
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss
import org.orekit.time
import org.orekit.utils
import typing



class Dcb:
    """
    public class Dcb extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class to store DCB Solution data parsed in the SinexLoader.
    
        This class is made to handle both station and satellite DCB data. Bias values are stored in TimeSpanMaps associated with
        a given pair of observation codes. Those TimeSpanMaps are stored in a Map, which associate a pair of observation code
        (as a HashSet of ObservationType) to a TimeSpanMap, encapsulated in a DCBCode object.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def addDcbLine(self, string: str, string2: str, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, double: float) -> None:
        """
            Add the content of a DCB line to the DCBSatellite object.
        
            The method check the presence of a Code pair in a map, and add values to the corresponding TimeSpanMap.
        
            Parameters:
                obs1 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): String corresponding to the first code used for the DCB computation
                obs2 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): String corresponding to the second code used for the DCB computation
                spanBegin (:class:`~org.orekit.time.AbsoluteDate`): Absolute Date corresponding to the beginning of the validity span for this bias value
                spanEnd (:class:`~org.orekit.time.AbsoluteDate`): Absolute Date corresponding to the end of the validity span for this bias value
                biasValue (double): DCB bias value expressed in S.I. units
        
        
        """
        ...
    def getAvailableObservationPairs(self) -> java.util.HashSet[org.hipparchus.util.Pair[org.orekit.gnss.ObservationType, org.orekit.gnss.ObservationType]]: ...
    @typing.overload
    def getDcb(self, string: str, string2: str, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the Differential Code Bias for a given observation pair and a at a given date.
        
            Parameters:
                obs1 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string corresponding to the first code used for the DCB computation
                obs2 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string corresponding to the second code used for the DCB computation
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which to obtain the DCB
        
            Returns:
                the value of the DCB in S.I. units
        
            Get the value of the Differential Code Bias for a given observation pair and a at a given date.
        
            Parameters:
                obs1 (:class:`~org.orekit.gnss.ObservationType`): first observation type
                obs2 (:class:`~org.orekit.gnss.ObservationType`): second observation type
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which to obtain the DCB
        
            Returns:
                the value of the DCB in S.I. units
        
        
        """
        ...
    @typing.overload
    def getDcb(self, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def getMaximumValidDateForObservationPair(self, string: str, string2: str) -> org.orekit.time.AbsoluteDate:
        """
            Get the maximum valid date for a given observation pair.
        
            Parameters:
                obs1 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string corresponding to the first code used for the DCB computation
                obs2 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string corresponding to the second code used for the DCB computation
        
            Returns:
                maximum valid date for the observation pair
        
            Get the maximum valid date for a given observation pair.
        
            Parameters:
                obs1 (:class:`~org.orekit.gnss.ObservationType`): first observation type
                obs2 (:class:`~org.orekit.gnss.ObservationType`): second observation type
        
            Returns:
                maximum valid date for the observation pair
        
        
        """
        ...
    @typing.overload
    def getMaximumValidDateForObservationPair(self, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate: ...
    @typing.overload
    def getMinimumValidDateForObservationPair(self, string: str, string2: str) -> org.orekit.time.AbsoluteDate:
        """
            Get the minimum valid date for a given observation pair.
        
            Parameters:
                obs1 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): sString corresponding to the first code used for the DCB computation
                obs2 (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string corresponding to the second code used for the DCB computation
        
            Returns:
                minimum valid date for the observation pair
        
            Get the minimum valid date for a given observation pair.
        
            Parameters:
                obs1 (:class:`~org.orekit.gnss.ObservationType`): first observation type
                obs2 (:class:`~org.orekit.gnss.ObservationType`): second observation type
        
            Returns:
                minimum valid date for the observation pair
        
        
        """
        ...
    @typing.overload
    def getMinimumValidDateForObservationPair(self, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType) -> org.orekit.time.AbsoluteDate: ...

class DcbDescription:
    """
    public class DcbDescription extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class to store the DCB description parameters.
    
        This class gives important parameters from the analysis and defines the fields in the block ’BIAS/SOLUTION’ of the
        loaded Sinex file.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def getBiasMode(self) -> str:
        """
            Get the bias mode
        
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
            Get the time system for DCB data.
        
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
            Set the time system used for DCB data.
        
            Parameters:
                timeSystem (:class:`~org.orekit.gnss.TimeSystem`): the time system to set
        
        
        """
        ...

class DcbSatellite:
    """
    public class DcbSatellite extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class based on DCB, used to store the data parsed in :class:`~org.orekit.files.sinex.SinexLoader` for Differential Code
        Biases computed for satellites.
    
        Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are
        stored in a single DCB object.
    
        Since:
            12.0
    """
    def __init__(self, string: str): ...
    def getDcbData(self) -> Dcb:
        """
            Get the DCB data for the current satellite.
        
            Returns:
                the DCB data for the current satellite
        
        
        """
        ...
    def getDescription(self) -> DcbDescription:
        """
            Get the data contained in "DCB/DESCRIPTION" block of the Sinex file.
        
            This block gives important parameters from the analysis and defines the fields in the block ’BIAS/SOLUTION’
        
            Returns:
                the "DCB/DESCRIPTION" parameters.
        
        
        """
        ...
    def getPRN(self) -> str:
        """
            Return the satellite PRN, as a String.
        
            Example of satellite PRN: "G01"
        
            Returns:
                the satellite PRN
        
        
        """
        ...
    def getSatelliteSytem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get the satellite sytem corresponding to the satellite.
        
            Satellite system is extracted from the first letter of the PRN.
        
            Returns:
                the satellite from which the DCB are extracted.
        
        
        """
        ...
    def setDescription(self, dcbDescription: DcbDescription) -> None:
        """
            Set the data contained in "DCB/DESCRIPTION" block of the Sinex file.
        
            Parameters:
                description (:class:`~org.orekit.files.sinex.DcbDescription`): the "DCB/DESCRIPTION" parameters to set
        
        
        """
        ...

class DcbStation:
    """
    public class DcbStation extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class based on DCB, used to store the data parsed in :class:`~org.orekit.files.sinex.SinexLoader` for Differential Code
        Biases computed for stations.
    
        Satellites and stations have differentiated classes as stations might have multiple satellite systems. The data are
        stored in a Map of DCB, identified by the :class:`~org.orekit.gnss.SatelliteSystem`
    
        Since:
            12.0
    """
    def __init__(self, string: str): ...
    def addDcb(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, dcb: Dcb) -> None:
        """
            Add the DCB data corresponding to a satellite system.
        
            If the instance previously contained DCB data for the satellite system, the old value is replaced.
        
            Parameters:
                satelliteSystem (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system for which the DCB is added
                dcb (:class:`~org.orekit.files.sinex.Dcb`): DCB data
        
        
        """
        ...
    def getAvailableSatelliteSystems(self) -> java.lang.Iterable[org.orekit.gnss.SatelliteSystem]: ...
    def getDcbData(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> Dcb:
        """
            Get the DCB data for a given satellite system.
        
            Parameters:
                satelliteSystem (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system
        
            Returns:
                the DCB data corresponding to the satellite system (can be null is no DCB available)
        
        
        """
        ...
    def getDescription(self) -> DcbDescription:
        """
            Get the data contained in "DCB/DESCRIPTION" block of the Sinex file.
        
            This block gives important parameters from the analysis and defines the fields in the block ’BIAS/SOLUTION’
        
            Returns:
                the "DCB/DESCRIPTION" parameters.
        
        
        """
        ...
    def getSiteCode(self) -> str:
        """
            Get the site code (station identifier).
        
            Returns:
                the site code
        
        
        """
        ...
    def setDescription(self, dcbDescription: DcbDescription) -> None:
        """
            Set the data contained in "DCB/DESCRIPTION" block of the Sinex file.
        
            Parameters:
                description (:class:`~org.orekit.files.sinex.DcbDescription`): the "DCB/DESCRIPTION" parameters to set
        
        
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

class SinexLoader(org.orekit.frames.EopHistoryLoader):
    """
    public class SinexLoader extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.frames.EopHistoryLoader`
    
        Loader for Solution INdependent EXchange (SINEX) files.
    
        The loader can be used to load several data types contained in Sinex files. The current supported data are: station
        coordinates, site eccentricities, EOP, and Difference Code Bias (DCB). Several instances of Sinex loader must be created
        in order to parse different data types.
    
        The parsing of EOP parameters for multiple files in different SinexLoader object, fed into the default DataContext might
        pose a problem in case validity dates are overlapping. As Sinex daily solution files provide a single EOP entry, the
        Sinex loader will add points at the limits of data dates (startDate, endDate) of the Sinex file, which in case of
        overlap will lead to inconsistencies in the final EOPHistory object. Multiple files can be parsed using a single
        SinexLoader with a regex to overcome this issue.
    
        Since:
            10.3
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScales: org.orekit.time.TimeScales): ...
    def fillHistory(self, nutationCorrectionConverter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, sortedSet: java.util.SortedSet[org.orekit.frames.EOPEntry]) -> None: ...
    def getCreationDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the creation date of the parsed SINEX file.
        
            Returns:
                SINEX file creation date as an AbsoluteDate
        
            Since:
                12.0
        
        
        """
        ...
    def getDcbSatellite(self, string: str) -> DcbSatellite:
        """
            Get the DCB data for a given satellite identified by its PRN.
        
            Parameters:
                prn (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the satellite PRN (e.g. "G01" for GPS 01)
        
            Returns:
                the DCB data for the satellite
        
            Since:
                12.0
        
        
        """
        ...
    def getDcbStation(self, string: str) -> DcbStation:
        """
            Get the DCB data for a given station.
        
            Parameters:
                siteCode (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): site code
        
            Returns:
                DCB data for the station
        
            Since:
                12.0
        
        
        """
        ...
    def getFileEpochEndTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the file epoch end time.
        
            Returns:
                the file epoch end time
        
            Since:
                12.0
        
        
        """
        ...
    def getFileEpochStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the file epoch start time.
        
            Returns:
                the file epoch start time
        
            Since:
                12.0
        
        
        """
        ...
    def getITRFVersion(self) -> org.orekit.frames.ITRFVersion:
        """
            Get the ITRF version used for the EOP entries processing.
        
            Returns:
                the ITRF Version used for the EOP processing.
        
            Since:
                11.2
        
        
        """
        ...
    def getParsedEop(self) -> java.util.Map[org.orekit.time.AbsoluteDate, SinexEopEntry]: ...
    def getStation(self, string: str) -> 'Station':
        """
            Get the station corresponding to the given site code.
        
            Parameters:
                siteCode (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): site code
        
            Returns:
                the corresponding station
        
        
        """
        ...
    def getStations(self) -> java.util.Map[str, 'Station']: ...
    def setITRFVersion(self, int: int) -> None:
        """
            Set the ITRF version used in EOP entries processing.
        
            Parameters:
                year (int): Year of the ITRF Version used for parsing EOP.
        
            Since:
                11.2
        
        
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
    def addAntennaTypeValidAfter(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a antenna type entry valid after a limit date.
        
        
            Using :code:`addAntennaTypeValidAfter(entry, t)` will make :code:`entry` valid in [t, +∞[ (note the closed bracket).
        
            Parameters:
                entry (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): antenna type entry
                earliestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date after which the entry is valid (must be different from **all** dates already used for transitions)
        
            Since:
                12.0
        
        
        """
        ...
    def addAntennaTypeValidBefore(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a antenna type entry valid before a limit date.
        
        
            Using :code:`addAntennaTypeValidBefore(entry, t)` will make :code:`entry` valid in ]-∞, t[ (note the open bracket).
        
            Parameters:
                entry (:class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): antenna type entry
                latestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date before which the entry is valid (must be different from **all** dates already used for transitions)
        
            Since:
                12.0
        
        
        """
        ...
    def addStationEccentricitiesValidAfter(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Add a station eccentricity vector entry valid after a limit date.
        
        
            Using :code:`addStationEccentricitiesValidAfter(entry, t)` will make :code:`entry` valid in [t, +∞[ (note the closed
            bracket).
        
            Parameters:
                entry (:class:`~org.orekit.files.sinex.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): station eccentricity vector entry
                earliestValidityDate (:class:`~org.orekit.time.AbsoluteDate`): date after which the entry is valid (must be different from **all** dates already used for transitions)
        
            Since:
                11.1
        
        
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
    def getAntennaType(self, absoluteDate: org.orekit.time.AbsoluteDate) -> str:
        """
            Get the antenna type for the given epoch. If there is no antenna types for the given epoch, an exception is thrown.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): epoch
        
            Returns:
                antenna type
        
            Since:
                12.0
        
        
        """
        ...
    def getAntennaTypeTimeSpanMap(self) -> org.orekit.utils.TimeSpanMap[str]: ...
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
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the station position.
        
            Returns:
                the station position (m)
        
        
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
        def values() -> typing.List['Station.ReferenceSystem']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.sinex")``.

    Dcb: typing.Type[Dcb]
    DcbDescription: typing.Type[DcbDescription]
    DcbSatellite: typing.Type[DcbSatellite]
    DcbStation: typing.Type[DcbStation]
    SinexEopEntry: typing.Type[SinexEopEntry]
    SinexLoader: typing.Type[SinexLoader]
    Station: typing.Type[Station]
