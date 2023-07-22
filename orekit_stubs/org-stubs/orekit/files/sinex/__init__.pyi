import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.orekit.data
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



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
                the length of day
        
        
        """
        ...
    def getNutLn(self) -> float:
        """
            Get the nutation correction in longitude.
        
            Returns:
                the nutation correction in longitude
        
        
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
                the UT1-UTC offset
        
        
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
                lod (double): the length of day to set
        
        
        """
        ...
    def setNutLn(self, double: float) -> None:
        """
            Set the nutation correction in longitude.
        
            Parameters:
                nutLn (double): the nutation correction in longitude to set
        
        
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
                ut1MinusUtc (double): the value to set
        
        
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

class SinexLoader(org.orekit.frames.EOPHistoryLoader):
    """
    public class SinexLoader extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.frames.EOPHistoryLoader`
    
        Loader for Solution INdependent EXchange (SINEX) files.
    
        For now only few keys are supported: SITE/ID, SITE/ECCENTRICITY, SOLUTION/EPOCHS and SOLUTION/ESTIMATE. They represent
        the minimum set of parameters that are interesting to consider in a SINEX file.
    
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
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScale: org.orekit.time.TimeScale): ...
    def fillHistory(self, nutationCorrectionConverter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, sortedSet: java.util.SortedSet[org.orekit.frames.EOPEntry]) -> None: ...
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
        :meth:`~org.orekit.files.sinex.Station.getEccentricities` method provides the last known eccentricity values. The
        :meth:`~org.orekit.files.sinex.Station.getEccentricities` method can be used to access the site antenna eccentricity
        values for a given epoch.
    
        Since:
            10.3
    """
    def __init__(self): ...
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
    @typing.overload
    def getEccentricities(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the last known station antenna eccentricities.
        
            Vector convention: X-Y-Z or UP-NORTH-EAST. See :meth:`~org.orekit.files.sinex.Station.getEccRefSystem` method.
        
            Returns:
                station antenna eccentricities (m)
        
        """
        ...
    @typing.overload
    def getEccentricities(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the station antenna eccentricities for the given epoch.
        
            Vector convention: X-Y-Z or UP-NORTH-EAST. See :meth:`~org.orekit.files.sinex.Station.getEccRefSystem` method.
        
            If there is no eccentricity values for the given epoch, an exception is thrown. It is possible to access the last known
            values using the :meth:`~org.orekit.files.sinex.Station.getEccentricities` method.
        
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
    def setEccentricities(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the last known station antenna eccentricities.
        
            Parameters:
                eccentricities (:class:`~org.orekit.files.sinex.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): the eccenticities to set (m)
        
        
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

    SinexEopEntry: typing.Type[SinexEopEntry]
    SinexLoader: typing.Type[SinexLoader]
    Station: typing.Type[Station]
