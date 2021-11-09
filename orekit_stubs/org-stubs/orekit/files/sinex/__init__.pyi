import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.orekit.data
import org.orekit.time
import typing



class SinexLoader:
    """
    public class SinexLoader extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Loader for Solution INdependent EXchange (SINEX) files.
    
        For now only few keys are supported: SITE/ID, SITE/ECCENTRICITY, SOLUTION/EPOCHS and SOLUTION/ESTIMATE. They represent
        the minimum set of parameters that are interesting to consider in a SINEX file.
    
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

class Station:
    """
    public class Station extends :class:`~org.orekit.files.sinex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Station model.
    
        Since:
            10.3
    """
    def __init__(self): ...
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
    def getEccentricities(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the station antenna eccentricities.
        
            Vector convention: X-Y-Z or UP-NORTH-EAST
        
            Returns:
                station antenna eccentricities (m)
        
        
        """
        ...
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
            Set the station antenna eccentricities.
        
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

    SinexLoader: typing.Type[SinexLoader]
    Station: typing.Type[Station]
