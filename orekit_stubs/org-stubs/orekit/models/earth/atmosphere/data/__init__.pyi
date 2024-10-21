import java.io
import java.lang
import java.util
import org.orekit.data
import org.orekit.models.earth.atmosphere
import org.orekit.models.earth.atmosphere.data.class-use
import org.orekit.time
import org.orekit.utils
import typing



_AbstractSolarActivityData__L = typing.TypeVar('_AbstractSolarActivityData__L', bound='AbstractSolarActivityDataLoader.LineParameters')  # <L>
_AbstractSolarActivityData__D = typing.TypeVar('_AbstractSolarActivityData__D', bound='AbstractSolarActivityDataLoader')  # <D>
class AbstractSolarActivityData(org.orekit.models.earth.atmosphere.DTM2000InputParameters, org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters, typing.Generic[_AbstractSolarActivityData__L, _AbstractSolarActivityData__D]):
    """
    public abstract class AbstractSolarActivityData<L extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityDataLoader.LineParameters`, D extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityDataLoader`<L>> extends :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`, :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
    
        Abstract class for solar activity data.
    
        Since:
            12.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, dataSource: org.orekit.data.DataSource, d2: _AbstractSolarActivityData__D, timeScale: org.orekit.time.TimeScale, int: int, double: float, double2: float, double3: float): ...
    def getCache(self) -> org.orekit.utils.GenericTimeStampedCache[_AbstractSolarActivityData__L]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range maximum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMaxDate` in
                interface :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getMaxDate` in
                interface :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Returns:
                the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range minimum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMinDate` in
                interface :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getMinDate` in
                interface :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Returns:
                the minimum date.
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
            Get the supported names regular expression.
        
            Returns:
                the supported names.
        
        
        """
        ...
    def getUTC(self) -> org.orekit.time.TimeScale:
        """
            Get the UTC timescale.
        
            Returns:
                UTC timescale
        
        
        """
        ...

_AbstractSolarActivityDataLoader__L = typing.TypeVar('_AbstractSolarActivityDataLoader__L', bound='AbstractSolarActivityDataLoader.LineParameters')  # <L>
class AbstractSolarActivityDataLoader(org.orekit.data.DataLoader, typing.Generic[_AbstractSolarActivityDataLoader__L]):
    """
    public abstract class AbstractSolarActivityDataLoader<L extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityDataLoader.LineParameters`> extends :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.data.DataLoader`
    
        Abstract class for solar activity data loader.
    
        Since:
            12.0
    """
    def getDataSet(self) -> java.util.SortedSet[_AbstractSolarActivityDataLoader__L]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range maximum date.
        
            Returns:
                the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range minimum date.
        
            Returns:
                the minimum date.
        
        
        """
        ...
    def getUTC(self) -> org.orekit.time.TimeScale:
        """
            Get the UTC timescale.
        
            Returns:
                the UTC timescale
        
        
        """
        ...
    def setMaxDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the available data range maximum date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): available data range maximum date
        
        
        """
        ...
    def setMinDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the available data range minimum date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): available data range minimum date
        
        
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
    class LineParameters(org.orekit.time.TimeStamped, java.lang.Comparable['AbstractSolarActivityDataLoader.LineParameters'], java.io.Serializable):
        def compareTo(self, lineParameters: 'AbstractSolarActivityDataLoader.LineParameters') -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def hashCode(self) -> int: ...

class DtcDataLoader(org.orekit.data.DataLoader):
    """
    public class DtcDataLoader extends :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.data.DataLoader`
    
        This class reads solar activity data from DTCFILE files for the class
        :class:`~org.orekit.models.earth.atmosphere.data.JB2008SpaceEnvironmentData`. The code in this class is based of the
        CssiSpaceWeatherDataLoader class. The DTCFILE file contain pre-computed data from Space Environment using the Dst
        indices as well as Ap indices. This computation can be realised using the Fortran code provided by Space Environment
        Technologies. See
        :class:`~org.orekit.models.earth.atmosphere.data.https:.sol.spacenvironment.net.JB2008.indices.DTCFILE.TXT` for more
        information.
    
        The data is provided by Space Environment Technologies through their website
        :class:`~org.orekit.models.earth.atmosphere.data.https:.sol.spacenvironment.net.JB2008.indices.DTCFILE.TXT`.
        The work done for this class is based on the CssiSpaceWeatherDataLoader class by Clément Jonglez, the JB2008 interface
        by Pascal Parraud, and corrections for DataLoader implementation by Bryan Cazabonne and Evan Ward .
    
        Since:
            11.2
    """
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    def getDataSet(self) -> java.util.SortedSet['DtcDataLoader.LineParameters']: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range maximum date.
        
            Returns:
                the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range minimum date.
        
            Returns:
                the minimum date.
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
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
    class LineParameters(org.orekit.time.TimeStamped, java.io.Serializable):
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
        def getDSTDTC(self) -> float: ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...

class JB2008SpaceEnvironmentData(org.orekit.models.earth.atmosphere.JB2008InputParameters):
    """
    public class JB2008SpaceEnvironmentData extends :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
    
        This class provides a container for the solar indices data required by the JB2008 atmospheric model. This container only
        stores information provided in the SOLFSMY and DTCFILE text file provided by Space Environment Technologies. Therefore
        it doesn't provide the geomagnetic storm indices available in the SOLRESAP file. The
        :class:`~org.orekit.data.DataLoader` implementations and the parsing are handled by the
        :class:`~org.orekit.models.earth.atmosphere.data.SOLFSMYDataLoader`
        :class:`~org.orekit.models.earth.atmosphere.data.DtcDataLoader` classes.
    
        Data are available on Space Environment Technologies' `website <http://sol.spacenvironment.net/jb2008>`. The work done
        for this class is based on the CssiSpaceWeatherData class by Clément Jonglez, the JB2008 interface by Pascal Parraud,
        and corrections for the CssiSpaceWeatherData implementation by Bryan Cazabonne and Evan Ward.
    
        Since:
            11.2
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_SUPPORTED_NAMES_SOLFSMY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_SUPPORTED_NAMES_SOLFSMY
    
        Default regular expression for supported names that works with test and published files for the SOLFSMY file.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_SUPPORTED_NAMES_DTC: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_SUPPORTED_NAMES_DTC
    
        Default regular expression for supported names that works with test and published files for the DTCFILE file.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, dataSource2: org.orekit.data.DataSource): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, dataSource2: org.orekit.data.DataSource, timeScale: org.orekit.time.TimeScale): ...
    def getDSTDTC(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the temperature change computed from Dst index.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getDSTDTC` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the temperature change computed from Dst index
        
        
        """
        ...
    def getF10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the instantaneous solar flux index (1e :sup:`-22` *Watt/(m²*Hertz)).
        
            Tabular time 1.0 day earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getF10` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the instantaneous F10.7 index
        
        
        """
        ...
    def getF10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the mean solar flux. Averaged 81-day centered F10.7 B index on the input time.
        
            Tabular time 1.0 day earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getF10B` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the mean solar flux F10.7B index
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range maximum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getMaxDate` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Returns:
                the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range minimum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getMinDate` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Returns:
                the minimum date.
        
        
        """
        ...
    def getS10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the EUV index (26-34 nm) scaled to F10.
        
            Tabular time 1.0 day earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getS10` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the the EUV S10 index
        
        
        """
        ...
    def getS10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the EUV 81-day averaged centered index.
        
            Tabular time 1.0 day earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getS10B` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the the mean EUV S10B index
        
        
        """
        ...
    def getXM10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the MG2 index scaled to F10.
        
            Tabular time 2.0 days earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getXM10` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the the MG2 index
        
        
        """
        ...
    def getXM10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the MG2 81-day average centered index.
        
            Tabular time 2.0 days earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getXM10B` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the the mean MG2 index
        
        
        """
        ...
    def getY10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the Solar X-Ray & Lya index scaled to F10.
        
            Tabular time 5.0 days earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getY10` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the Solar X-Ray & Lya index scaled to F10
        
        
        """
        ...
    def getY10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the Solar X-Ray & Lya 81-day ave. centered index.
        
            Tabular time 5.0 days earlier.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.JB2008InputParameters.getY10B` in
                interface :class:`~org.orekit.models.earth.atmosphere.JB2008InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the Solar X-Ray & Lya 81-day ave. centered index
        
        
        """
        ...

class SOLFSMYDataLoader(org.orekit.data.DataLoader):
    """
    public class SOLFSMYDataLoader extends :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.data.DataLoader`
    
        This class reads solar activity data from SOLFSMY files for the class
        :class:`~org.orekit.models.earth.atmosphere.data.JB2008SpaceEnvironmentData`. The code in this class is based of the
        CssiSpaceWeatherDataLoader.
    
        The data is provided by Space Environment Technologies through their website
        :class:`~org.orekit.models.earth.atmosphere.data.https:.sol.spacenvironment.net.JB2008.indices.SOLFSMY.TXT`.
        The work done for this class is based on the CssiWpaceWeatherDataLoader class by Clément Jonglez, the JB2008 interface
        by Pascal Parraud, and corrections for DataLoader implementation by Bryan Cazabonne and Evan Ward .
    
        Since:
            11.2
    """
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    def getDataSet(self) -> java.util.SortedSet['SOLFSMYDataLoader.LineParameters']: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range maximum date.
        
            Returns:
                the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range minimum date.
        
            Returns:
                the minimum date.
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
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
    class LineParameters(org.orekit.time.TimeStamped, java.io.Serializable):
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float): ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getF10(self) -> float: ...
        def getF10B(self) -> float: ...
        def getS10(self) -> float: ...
        def getS10B(self) -> float: ...
        def getXM10(self) -> float: ...
        def getXM10B(self) -> float: ...
        def getY10(self) -> float: ...
        def getY10B(self) -> float: ...

class CssiSpaceWeatherData(AbstractSolarActivityData['CssiSpaceWeatherDataLoader.LineParameters', 'CssiSpaceWeatherDataLoader']):
    """
    public class CssiSpaceWeatherData extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityData`<:class:`~org.orekit.models.earth.atmosphere.data.CssiSpaceWeatherDataLoader.LineParameters`, :class:`~org.orekit.models.earth.atmosphere.data.CssiSpaceWeatherDataLoader`>
    
        This class provides three-hourly and daily solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp
        indexes. The :class:`~org.orekit.data.DataLoader` implementation and the parsing is handled by the class
        :class:`~org.orekit.models.earth.atmosphere.data.CssiSpaceWeatherDataLoader`.
    
        The data are retrieved through space weather files offered by AGI/CSSI on the AGI
        :class:`~org.orekit.models.earth.atmosphere.data.https:.ftp.agi.com.pub.DynamicEarthData.SpaceWeather` as well as on the
        CelesTrack `website <http://celestrak.com/SpaceData/>`. These files are updated several times a day by using several
        sources mentioned in the `Celestrak space weather data documentation
        <http://celestrak.com/SpaceData/SpaceWx-format.php>`.
    
        Since:
            10.2
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_SUPPORTED_NAMES
    
        Default regular expression for supported names that works with all officially published files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, string: str, cssiSpaceWeatherDataLoader: 'CssiSpaceWeatherDataLoader', dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, string: str, cssiSpaceWeatherDataLoader: 'CssiSpaceWeatherDataLoader', dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, cssiSpaceWeatherDataLoader: 'CssiSpaceWeatherDataLoader', timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, cssiSpaceWeatherDataLoader: 'CssiSpaceWeatherDataLoader', timeScale: org.orekit.time.TimeScale, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, timeScale: org.orekit.time.TimeScale): ...
    def get24HoursKp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the last 24H mean geomagnetic index.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 24H geomagnetic index
        
        
        """
        ...
    def getAp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Get the A :sub:`p` geomagnetic indices.
        
            A :sub:`p` indices are provided as an array such as:
        
              - 0 → daily A :sub:`p`
              - 1 → 3 hr A :sub:`p` index for current time
              - 2 → 3 hr A :sub:`p` index for 3 hrs before current time
              - 3 → 3 hr A :sub:`p` index for 6 hrs before current time
              - 4 → 3 hr A :sub:`p` index for 9 hrs before current time
              - 5 → Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
              - 6 → Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the daily F10.7 solar flux for previous day.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the daily F10.7 flux for previous day
        
        
        """
        ...
    def getInstantFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the instantaneous solar flux.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the instantaneous solar flux
        
        
        """
        ...
    def getMeanFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the mean solar flux.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the mean solar flux
        
        
        """
        ...
    def getThreeHourlyKP(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using:
            delay=6-abs(lat)*0.033 (lat in deg.)
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 3H geomagnetic index
        
        
        """
        ...

class CssiSpaceWeatherDataLoader(AbstractSolarActivityDataLoader['CssiSpaceWeatherDataLoader.LineParameters']):
    """
    public class CssiSpaceWeatherDataLoader extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityDataLoader`<:class:`~org.orekit.models.earth.atmosphere.data.CssiSpaceWeatherDataLoader.LineParameters`>
    
        This class reads solar activity data from CSSI Space Weather files for the class
        :class:`~org.orekit.models.earth.atmosphere.data.CssiSpaceWeatherData`.
    
        The data are retrieved through space weather files offered by CSSI/AGI. The data can be retrieved on the AGI
        :class:`~org.orekit.models.earth.atmosphere.data.ftp:.ftp.agi.com.pub.DynamicEarthData.SpaceWeather`. This file is
        updated several times a day by using several sources mentioned in the ` Celestrak space weather data documentation
        <http://celestrak.com/SpaceData/SpaceWx-format.php>`.
    
        Since:
            10.2
    """
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    def getDataSet(self) -> java.util.SortedSet['CssiSpaceWeatherDataLoader.LineParameters']: ...
    def getLastDailyPredictedDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the day (at data start) of the last daily data entry.
        
            Returns:
                the last daily predicted date
        
        
        """
        ...
    def getLastObservedDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the day (at data start) of the last observed data entry.
        
            Returns:
                the last observed date
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    class LineParameters(AbstractSolarActivityDataLoader.LineParameters):
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float], double2: float, doubleArray2: typing.List[float], double4: float, double5: float, int: int, double6: float, double7: float, double8: float, double9: float, double10: float): ...
        def compareTo(self, lineParameters: AbstractSolarActivityDataLoader.LineParameters) -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def getApAvg(self) -> float: ...
        def getCtr81Adj(self) -> float: ...
        def getCtr81Obs(self) -> float: ...
        def getF107Adj(self) -> float: ...
        def getF107Obs(self) -> float: ...
        def getFluxQualifier(self) -> int: ...
        def getKpSum(self) -> float: ...
        def getLst81Adj(self) -> float: ...
        def getLst81Obs(self) -> float: ...
        @typing.overload
        def getThreeHourlyAp(self, int: int) -> float: ...
        @typing.overload
        def getThreeHourlyAp(self) -> typing.List[float]: ...
        @typing.overload
        def getThreeHourlyKp(self, int: int) -> float: ...
        @typing.overload
        def getThreeHourlyKp(self) -> typing.List[float]: ...
        def hashCode(self) -> int: ...

class MarshallSolarActivityFutureEstimation(AbstractSolarActivityData['MarshallSolarActivityFutureEstimationLoader.LineParameters', 'MarshallSolarActivityFutureEstimationLoader']):
    """
    public class MarshallSolarActivityFutureEstimation extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityData`<:class:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimationLoader.LineParameters`, :class:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimationLoader`>
    
        This class provides solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp indexes.
    
        Data comes from the NASA Marshall Solar Activity Future Estimation (MSAFE) as estimates of monthly F10.7 Mean solar flux
        and Ap geomagnetic parameter (see :class:`~org.orekit.models.earth.atmosphere.data.https:.www.nasa.gov.solar`).
    
        Data can be retrieved at the NASA :class:`~org.orekit.models.earth.atmosphere.data.https:.www.nasa.gov.solar`. Here Kp
        indices are deduced from Ap indexes, which in turn are tabulated equivalent of retrieved Ap values.
    
        If several MSAFE files are available, some dates may appear in several files (for example August 2007 is in all files
        from the first one published in March 1999 to the February 2008 file). In this case, the data from the most recent file
        is used and the older ones are discarded. The date of the file is assumed to be 6 months after its first entry (which
        explains why the file having August 2007 as its first entry is the February 2008 file). This implies that MSAFE files
        must *not* be edited to change their time span, otherwise this would break the old entries overriding mechanism.
    
        With these data, the
        :meth:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimation.getInstantFlux` and
        :meth:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimation.getMeanFlux` methods return the
        same values and the :meth:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimation.get24HoursKp`
        and :meth:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimation.getThreeHourlyKP` methods
        return the same values.
    
        Conversion from Ap index values in the MSAFE file to Kp values used by atmosphere models is done using Jacchia's
        equation in [1].
    
        With these data, the :meth:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimation.getAp` method
        returns an array of seven times the same daily Ap value, i.e. it is suited to be used only with the
        :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00` atmospheric model where the switch #9 is set to 1.
    
        References
    ----------
    
    
          1.  Jacchia, L. G. "CIRA 1972, recent atmospheric models, and improvements in progress." COSPAR, 21st Plenary Meeting. Vol.
            1. 1978.
    
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.models.earth.atmosphere.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_SUPPORTED_NAMES
    
        Default regular expression for the supported name that work with all officially published files.
    
        Since:
            10.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel'): ...
    @typing.overload
    def __init__(self, string: str, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, string: str, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel'): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', timeScale: org.orekit.time.TimeScale, int: int, double: float, double2: float, double3: float): ...
    def get24HoursKp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            The Kp index is derived from the Ap index.
        
            The method used is explained on ` NOAA website. <http://www.ngdc.noaa.gov/stp/GEOMAG/kp_ap.html>` as follows:
        
            The scale is 0 to 9 expressed in thirds of a unit, e.g. 5- is 4 2/3, 5 is 5 and 5+ is 5 1/3. The ap (equivalent range)
            index is derived from the Kp index as follows:
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the Kp data
        
            Returns:
                the 24H geomagnetic index
        
        
        """
        ...
    def getAp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Get the A :sub:`p` geomagnetic indices.
        
            A :sub:`p` indices are provided as an array such as:
        
              - 0 → daily A :sub:`p`
              - 1 → 3 hr A :sub:`p` index for current time
              - 2 → 3 hr A :sub:`p` index for 3 hrs before current time
              - 3 → 3 hr A :sub:`p` index for 6 hrs before current time
              - 4 → 3 hr A :sub:`p` index for 9 hrs before current time
              - 5 → Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
              - 6 → Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getAverageFlux`
            Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the daily F10.7 solar flux for previous day.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the daily F10.7 flux for previous day
        
        
        """
        ...
    def getFileDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.time.DateComponents:
        """
            Get the date of the file from which data at the specified date comes from.
        
            If several MSAFE files are available, some dates may appear in several files (for example August 2007 is in all files
            from the first one published in March 1999 to the February 2008 file). In this case, the data from the most recent file
            is used and the older ones are discarded. The date of the file is assumed to be 6 months after its first entry (which
            explains why the file having August 2007 as its first entry is the February 2008 file). This implies that MSAFE files
            must *not* be edited to change their time span, otherwise this would break the old entries overriding mechanism.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the solar activity data
        
            Returns:
                date of the file
        
        
        """
        ...
    def getInstantFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the instantaneous solar flux.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the instantaneous solar flux
        
        
        """
        ...
    def getMeanFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the mean solar flux.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the mean solar flux
        
        
        """
        ...
    def getStrengthLevel(self) -> 'MarshallSolarActivityFutureEstimation.StrengthLevel':
        """
            Get the strength level for activity.
        
            Returns:
                strength level to set
        
        
        """
        ...
    def getThreeHourlyKP(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using:
            delay=6-abs(lat)*0.033 (lat in deg.)
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 3H geomagnetic index
        
        
        """
        ...
    class StrengthLevel(java.lang.Enum['MarshallSolarActivityFutureEstimation.StrengthLevel']):
        STRONG: typing.ClassVar['MarshallSolarActivityFutureEstimation.StrengthLevel'] = ...
        AVERAGE: typing.ClassVar['MarshallSolarActivityFutureEstimation.StrengthLevel'] = ...
        WEAK: typing.ClassVar['MarshallSolarActivityFutureEstimation.StrengthLevel'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MarshallSolarActivityFutureEstimation.StrengthLevel': ...
        @staticmethod
        def values() -> typing.List['MarshallSolarActivityFutureEstimation.StrengthLevel']: ...

class MarshallSolarActivityFutureEstimationLoader(AbstractSolarActivityDataLoader['MarshallSolarActivityFutureEstimationLoader.LineParameters']):
    """
    public class MarshallSolarActivityFutureEstimationLoader extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityDataLoader`<:class:`~org.orekit.models.earth.atmosphere.data.MarshallSolarActivityFutureEstimationLoader.LineParameters`>
    
        This class reads solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp indexes.
    
        The data are retrieved through the NASA Marshall Solar Activity Future Estimation (MSAFE) as estimates of monthly F10.7
        Mean solar flux and Ap geomagnetic parameter. The data can be retrieved at the NASA
        :class:`~org.orekit.models.earth.atmosphere.data.https:.www.nasa.gov.msfcsolar.archivedforecast`. Here Kp indices are
        deduced from Ap indexes, which in turn are tabulated equivalent of retrieved Ap values.
    
        If several MSAFE files are available, some dates may appear in several files (for example August 2007 is in all files
        from the first one published in March 1999 to the February 2008 file). In this case, the data from the most recent file
        is used and the older ones are discarded. The date of the file is assumed to be 6 months after its first entry (which
        explains why the file having August 2007 as its first entry is the February 2008 file). This implies that MSAFE files
        must *not* be edited to change their time span, otherwise this would break the old entries overriding mechanism.
    
        References
    ----------
    
    
          1.  Jacchia, L. G. "CIRA 1972, recent atmospheric models, and improvements in progress." COSPAR, 21st Plenary Meeting. Vol.
            1. 1978.
    """
    @typing.overload
    def __init__(self, strengthLevel: MarshallSolarActivityFutureEstimation.StrengthLevel): ...
    @typing.overload
    def __init__(self, strengthLevel: MarshallSolarActivityFutureEstimation.StrengthLevel, timeScale: org.orekit.time.TimeScale): ...
    def getDataSet(self) -> java.util.SortedSet['MarshallSolarActivityFutureEstimationLoader.LineParameters']: ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    class LineParameters(AbstractSolarActivityDataLoader.LineParameters):
        def compareTo(self, lineParameters: AbstractSolarActivityDataLoader.LineParameters) -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def getAp(self) -> float: ...
        def getF107(self) -> float: ...
        def getFileDate(self) -> org.orekit.time.DateComponents: ...
        def hashCode(self) -> int: ...

_PythonAbstractSolarActivityData__L = typing.TypeVar('_PythonAbstractSolarActivityData__L', bound=AbstractSolarActivityDataLoader.LineParameters)  # <L>
_PythonAbstractSolarActivityData__D = typing.TypeVar('_PythonAbstractSolarActivityData__D', bound=AbstractSolarActivityDataLoader)  # <D>
class PythonAbstractSolarActivityData(AbstractSolarActivityData[_PythonAbstractSolarActivityData__L, _PythonAbstractSolarActivityData__D], typing.Generic[_PythonAbstractSolarActivityData__L, _PythonAbstractSolarActivityData__D]):
    """
    public class PythonAbstractSolarActivityData<L extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityDataLoader.LineParameters`, D extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityDataLoader`<L>> extends :class:`~org.orekit.models.earth.atmosphere.data.AbstractSolarActivityData`<L, D>
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, d: _PythonAbstractSolarActivityData__D, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale, int: int, double: float, double2: float, double3: float): ...
    def finalize(self) -> None: ...
    def get24HoursKp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.get24HoursKp`
            Get the last 24H mean geomagnetic index.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 24H geomagnetic index
        
        
        """
        ...
    def getAp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getAp`
            Get the A :sub:`p` geomagnetic indices.
        
            A :sub:`p` indices are provided as an array such as:
        
              - 0 → daily A :sub:`p`
              - 1 → 3 hr A :sub:`p` index for current time
              - 2 → 3 hr A :sub:`p` index for 3 hrs before current time
              - 3 → 3 hr A :sub:`p` index for 6 hrs before current time
              - 4 → 3 hr A :sub:`p` index for 9 hrs before current time
              - 5 → Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
              - 6 → Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getAverageFlux`
            Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getDailyFlux`
            Get the value of the daily F10.7 solar flux for previous day.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the daily F10.7 flux for previous day
        
        
        """
        ...
    def getInstantFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getInstantFlux`
            Get the value of the instantaneous solar flux.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the instantaneous solar flux
        
        
        """
        ...
    def getMeanFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMeanFlux`
            Get the value of the mean solar flux.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the mean solar flux
        
        
        """
        ...
    def getThreeHourlyKP(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getThreeHourlyKP`
            Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using:
            delay=6-abs(lat)*0.033 (lat in deg.)
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 3H geomagnetic index
        
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.atmosphere.data")``.

    AbstractSolarActivityData: typing.Type[AbstractSolarActivityData]
    AbstractSolarActivityDataLoader: typing.Type[AbstractSolarActivityDataLoader]
    CssiSpaceWeatherData: typing.Type[CssiSpaceWeatherData]
    CssiSpaceWeatherDataLoader: typing.Type[CssiSpaceWeatherDataLoader]
    DtcDataLoader: typing.Type[DtcDataLoader]
    JB2008SpaceEnvironmentData: typing.Type[JB2008SpaceEnvironmentData]
    MarshallSolarActivityFutureEstimation: typing.Type[MarshallSolarActivityFutureEstimation]
    MarshallSolarActivityFutureEstimationLoader: typing.Type[MarshallSolarActivityFutureEstimationLoader]
    PythonAbstractSolarActivityData: typing.Type[PythonAbstractSolarActivityData]
    SOLFSMYDataLoader: typing.Type[SOLFSMYDataLoader]
    class-use: org.orekit.models.earth.atmosphere.data.class-use.__module_protocol__
