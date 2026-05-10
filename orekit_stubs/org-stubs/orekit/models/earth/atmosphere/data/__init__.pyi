
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.orekit.data
import org.orekit.models.earth.atmosphere
import org.orekit.time
import org.orekit.utils
import typing



_AbstractSolarActivityData__L = typing.TypeVar('_AbstractSolarActivityData__L', bound='AbstractSolarActivityDataLoader.LineParameters')  # <L>
_AbstractSolarActivityData__D = typing.TypeVar('_AbstractSolarActivityData__D', bound='AbstractSolarActivityDataLoader')  # <D>
class AbstractSolarActivityData(org.orekit.models.earth.atmosphere.DTM2000InputParameters, org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters, typing.Generic[_AbstractSolarActivityData__L, _AbstractSolarActivityData__D]):
    """
    Abstract class for solar activity data.
    
    Since:
        12.0
    
    Also see:
        serialized
    """
    def __init__(self, source: org.orekit.data.DataSource, loader: _AbstractSolarActivityData__D, utc: org.orekit.time.TimeScale, maxSlots: int, maxSpan: float, maxInterval: float, minimumStep: float):
        """
        Constructor.
        
        Parameters:
            supportedNames (String): regular expression for supported AGI/CSSI space weather files names
            loader (AbstractSolarActivityData): data loader
            dataProvidersManager (DataProvidersManager): provides access to auxiliary data files.
            utc (TimeScale): UTC time scale
            maxSlots (int): maximum number of independent cached time slots in the GenericTimeStampedCache
            maxSpan (double): maximum duration span in seconds of one slot in the GenericTimeStampedCache
            maxInterval (double): time interval above which a new slot is created in the GenericTimeStampedCache
            minimumStep (double): overriding minimum step designed for non-homogeneous tabulated values. To be used for example when caching monthly
                tabulated values. May be null.
        
        public AbstractSolarActivityData (DataSource source, AbstractSolarActivityData loader, TimeScale utc, int maxSlots, double maxSpan, double maxInterval, double minimumStep)
        
        Simple constructor.
        
        Parameters:
            source (DataSource): source for the data
            loader (AbstractSolarActivityData): data loader
            utc (TimeScale): UTC time scale
            maxSlots (int): maximum number of independent cached time slots in the GenericTimeStampedCache
            maxSpan (double): maximum duration span in seconds of one slot in the GenericTimeStampedCache
            maxInterval (double): time interval above which a new slot is created in the GenericTimeStampedCache
            minimumStep (double): overriding minimum step designed for non-homogeneous tabulated values. To be used for example when caching monthly
                tabulated values. May be null.
        
        Since:
            12.0
        
        
        """
        ...
    def getCache(self) -> org.orekit.utils.GenericTimeStampedCache[_AbstractSolarActivityData__L]:
        """
        Get underlying cache.
        
        Returns:
            cache
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Specified by: getMaxDate in interface DTM2000InputParameters
        
        Specified by: getMaxDate in interface NRLMSISE00InputParameters
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Specified by: getMinDate in interface DTM2000InputParameters
        
        Specified by: getMinDate in interface NRLMSISE00InputParameters
        
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
    Abstract class for solar activity data loader.
    
    Since:
        12.0
    """
    def getDataSet(self) -> java.util.SortedSet[_AbstractSolarActivityDataLoader__L]:
        """
        Get the data set.
        
        Returns:
            the data set
        
        
        """
        ...
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
    def setMaxDate(self, date: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the available data range maximum date.
        
        Parameters:
            date (AbsoluteDate): available data range maximum date
        
        
        """
        ...
    def setMinDate(self, date: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the available data range minimum date.
        
        Parameters:
            date (AbsoluteDate): available data range minimum date
        
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
        Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
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
    This class reads solar activity data from DTCFILE files for the class JB2008SpaceEnvironmentData. The code in this class is based of the CssiSpaceWeatherDataLoader class. The DTCFILE file contain pre-computed data from Space Environment using the Dst indices as well as Ap indices. This computation can be realised using the Fortran code provided by Space Environment Technologies. See TXT for more information.
    
    The data is provided by Space Environment Technologies through their website TXT. The work done for this class is based on the CssiSpaceWeatherDataLoader class by Clément Jonglez, the JB2008 interface by Pascal Parraud, and corrections for DataLoader implementation by Bryan Cazabonne and Evan Ward .
    
    Since:
        11.2
    """
    def __init__(self, utc: org.orekit.time.TimeScale):
        """
        Constructor.
        
        Parameters:
            utc (TimeScale): UTC time scale
        
        
        """
        ...
    def getDataSet(self) -> java.util.SortedSet['DtcDataLoader.LineParameters']:
        """
        Getter for the data set.
        
        Returns:
            the data set
        
        
        """
        ...
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
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
        Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
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
    This class provides a container for the solar indices data required by the JB2008 atmospheric model. This container only stores information provided in the SOLFSMY and DTCFILE text file provided by Space Environment Technologies. Therefore it doesn't provide the geomagnetic storm indices available in the SOLRESAP file. The DataLoader implementations and the parsing are handled by the SOLFSMYDataLoader DtcDataLoader classes.
    
    Data are available on Space Environment Technologies' `website <http://sol.spacenvironment.net/jb2008>`. The work done for this class is based on the CssiSpaceWeatherData class by Clément Jonglez, the JB2008 interface by Pascal Parraud, and corrections for the CssiSpaceWeatherData implementation by Bryan Cazabonne and Evan Ward.
    
    Since:
        11.2
    
    Also see:
        serialized
    """
    DEFAULT_SUPPORTED_NAMES_SOLFSMY: typing.ClassVar[str] = ...
    """
    Default regular expression for supported names that works with test and published files for the SOLFSMY file.
    
    Also see:
        constant
    
    
    """
    DEFAULT_SUPPORTED_NAMES_DTC: typing.ClassVar[str] = ...
    """
    Default regular expression for supported names that works with test and published files for the DTCFILE file.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, supportedNamesSOL: str, supportedNamesDTC: str, dataProvidersManager: org.orekit.data.DataProvidersManager, utc: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, dataSource2: org.orekit.data.DataSource): ...
    @typing.overload
    def __init__(self, sourceSolfsmy: org.orekit.data.DataSource, sourceDtc: org.orekit.data.DataSource, utc: org.orekit.time.TimeScale): ...
    def getDSTDTC(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the temperature change computed from Dst index.
        
        Specified by: getDSTDTC in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the temperature change computed from Dst index
        
        
        """
        ...
    def getF10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux index (1e :sup:`-22` Watt/(m²Hertz)).
        
        Tabular time 1.0 day earlier.
        
        Specified by: getF10 in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous F10.7 index
        
        
        """
        ...
    def getF10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux. Averaged 81-day centered F10.7 B index on the input time.
        
        Tabular time 1.0 day earlier.
        
        Specified by: getF10B in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux F10.7B index
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Specified by: getMaxDate in interface JB2008InputParameters
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Specified by: getMinDate in interface JB2008InputParameters
        
        Returns:
            the minimum date.
        
        
        """
        ...
    def getS10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV index (26-34 nm) scaled to F10.
        
        Tabular time 1.0 day earlier.
        
        Specified by: getS10 in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the EUV S10 index
        
        
        """
        ...
    def getS10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV 81-day averaged centered index.
        
        Tabular time 1.0 day earlier.
        
        Specified by: getS10B in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean EUV S10B index
        
        
        """
        ...
    def getXM10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 index scaled to F10.
        
        Tabular time 2.0 days earlier.
        
        Specified by: getXM10 in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the MG2 index
        
        
        """
        ...
    def getXM10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 81-day average centered index.
        
        Tabular time 2.0 days earlier.
        
        Specified by: getXM10B in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean MG2 index
        
        
        """
        ...
    def getY10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the Solar X-Ray & Lya index scaled to F10.
        
        Tabular time 5.0 days earlier.
        
        Specified by: getY10 in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the Solar X-Ray & Lya index scaled to F10
        
        
        """
        ...
    def getY10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the Solar X-Ray & Lya 81-day ave. centered index.
        
        Tabular time 5.0 days earlier.
        
        Specified by: getY10B in interface JB2008InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the Solar X-Ray & Lya 81-day ave. centered index
        
        
        """
        ...

class SOLFSMYDataLoader(org.orekit.data.DataLoader):
    """
    This class reads solar activity data from SOLFSMY files for the class JB2008SpaceEnvironmentData. The code in this class is based of the CssiSpaceWeatherDataLoader.
    
    The data is provided by Space Environment Technologies through their website TXT. The work done for this class is based on the CssiWpaceWeatherDataLoader class by Clément Jonglez, the JB2008 interface by Pascal Parraud, and corrections for DataLoader implementation by Bryan Cazabonne and Evan Ward .
    
    Since:
        11.2
    """
    def __init__(self, utc: org.orekit.time.TimeScale):
        """
        Constructor.
        
        Parameters:
            utc (TimeScale): UTC time scale
        
        
        """
        ...
    def getDataSet(self) -> java.util.SortedSet['SOLFSMYDataLoader.LineParameters']:
        """
        Gets the data set.
        
        Returns:
            the data set
        
        
        """
        ...
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
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
        Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
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
    This class provides three-hourly and daily solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp indexes. The DataLoader implementation and the parsing is handled by the class CssiSpaceWeatherDataLoader.
    
    The data are retrieved through space weather files offered by AGI/CSSI on the AGI SpaceWeather as well as on the CelesTrack SpaceData. These files are updated several times a day by using several sources mentioned in the SpaceWx.
    
    Since:
        10.2
    
    Also see:
        serialized
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default regular expression for supported names that works with all officially published files.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, supportedNames: str, loader: 'CssiSpaceWeatherDataLoader', dataProvidersManager: org.orekit.data.DataProvidersManager, utc: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, supportedNames: str, loader: 'CssiSpaceWeatherDataLoader', dataProvidersManager: org.orekit.data.DataProvidersManager, utc: org.orekit.time.TimeScale, maxSlots: int, maxSpan: float, maxInterval: float): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, cssiSpaceWeatherDataLoader: 'CssiSpaceWeatherDataLoader', timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, source: org.orekit.data.DataSource, loader: 'CssiSpaceWeatherDataLoader', utc: org.orekit.time.TimeScale, maxSlots: int, maxSpan: float, maxInterval: float): ...
    @typing.overload
    def __init__(self, source: org.orekit.data.DataSource, utc: org.orekit.time.TimeScale): ...
    def get24HoursKp(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the last 24H mean geomagnetic index.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 24H geomagnetic index
        
        
        """
        ...
    def getAp(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
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
            date (AbsoluteDate): the current date
        
        Returns:
            the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the daily F10.7 solar flux for previous day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the daily F10.7 flux for previous day
        
        
        """
        ...
    def getInstantFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous solar flux
        
        
        """
        ...
    def getMeanFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux
        
        
        """
        ...
    def getThreeHourlyKP(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using: delay=6-abs(lat)*0.033 (lat in deg.)
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 3H geomagnetic index
        
        
        """
        ...

class CssiSpaceWeatherDataLoader(AbstractSolarActivityDataLoader['CssiSpaceWeatherDataLoader.LineParameters']):
    """
    This class reads solar activity data from CSSI Space Weather files for the class CssiSpaceWeatherData.
    
    The data are retrieved through space weather files offered by CSSI/AGI. The data can be retrieved on the AGI SpaceWeather. This file is updated several times a day by using several sources mentioned in the SpaceWx.
    
    Since:
        10.2
    """
    def __init__(self, utc: org.orekit.time.TimeScale):
        """
        Constructor.
        
        Parameters:
            utc (TimeScale): UTC time scale
        
        
        """
        ...
    def getDataSet(self) -> java.util.SortedSet['CssiSpaceWeatherDataLoader.LineParameters']:
        """
        Getter for the data set.
        
        Specified by: getDataSet in class AbstractSolarActivityDataLoader
        
        Returns:
            the data set
        
        
        """
        ...
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
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...
    class LineParameters(AbstractSolarActivityDataLoader.LineParameters):
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray], double4: float, double5: float, int: int, double6: float, double7: float, double8: float, double9: float, double10: float): ...
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
        def getThreeHourlyAp(self) -> typing.MutableSequence[float]: ...
        @typing.overload
        def getThreeHourlyKp(self, int: int) -> float: ...
        @typing.overload
        def getThreeHourlyKp(self) -> typing.MutableSequence[float]: ...
        def hashCode(self) -> int: ...

class MarshallSolarActivityFutureEstimation(AbstractSolarActivityData['MarshallSolarActivityFutureEstimationLoader.LineParameters', 'MarshallSolarActivityFutureEstimationLoader']):
    """
    This class provides solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp indexes.
    
    Data comes from the NASA Marshall Solar Activity Future Estimation (MSAFE) as estimates of monthly F10.7 Mean solar flux and Ap geomagnetic parameter (see solar).
    
    Data can be retrieved at the NASA solar. Here Kp indices are deduced from Ap indexes, which in turn are tabulated equivalent of retrieved Ap values.
    
    If several MSAFE files are available, some dates may appear in several files (for example August 2007 is in all files from the first one published in March 1999 to the February 2008 file). In this case, the data from the most recent file is used and the older ones are discarded. The date of the file is assumed to be 6 months after its first entry (which explains why the file having August 2007 as its first entry is the February 2008 file). This implies that MSAFE files must not be edited to change their time span, otherwise this would break the old entries overriding mechanism.
    
    With these data, the getInstantFlux and getMeanFlux methods return the same values and the get24HoursKp and getThreeHourlyKP methods return the same values.
    
    Conversion from Ap index values in the MSAFE file to Kp values used by atmosphere models is done using Jacchia's equation in [1].
    
    With these data, the getAp method returns an array of seven times the same daily Ap value, i.e. it is suited to be used only with the NRLMSISE00 atmospheric model where the switch #9 is set to 1.
    
    References ----------
    
      1.  Jacchia, L. G. "CIRA 1972, recent atmospheric models, and improvements in progress." COSPAR, 21st Plenary Meeting. Vol. 1. 1978.
    
    
    Also see:
        serialized
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default regular expression for the supported name that work with all officially published files.
    
    Since:
        10.0
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel'): ...
    @typing.overload
    def __init__(self, supportedNames: str, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', dataProvidersManager: org.orekit.data.DataProvidersManager, utc: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, supportedNames: str, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', dataProvidersManager: org.orekit.data.DataProvidersManager, utc: org.orekit.time.TimeScale, maxSlots: int, maxSpan: float, maxInterval: float, minimumStep: float): ...
    @typing.overload
    def __init__(self, dataSource: org.orekit.data.DataSource, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel'): ...
    @typing.overload
    def __init__(self, source: org.orekit.data.DataSource, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', utc: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, source: org.orekit.data.DataSource, strengthLevel: 'MarshallSolarActivityFutureEstimation.StrengthLevel', utc: org.orekit.time.TimeScale, maxSlots: int, maxSpan: float, maxInterval: float, minimumStep: float): ...
    def get24HoursKp(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        The Kp index is derived from the Ap index.
        
        The method used is explained on kp_ap as follows:
        
        The scale is 0 to 9 expressed in thirds of a unit, e.g. 5- is 4 2/3, 5 is 5 and 5+ is 5 1/3. The ap (equivalent range) index is derived from the Kp index as follows:
        
        Parameters:
            date (AbsoluteDate): date of the Kp data
        
        Returns:
            the 24H geomagnetic index
        
        
        """
        ...
    def getAp(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
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
            date (AbsoluteDate): the current date
        
        Returns:
            the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Description copied from interface: getAverageFlux Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the daily F10.7 solar flux for previous day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the daily F10.7 flux for previous day
        
        
        """
        ...
    def getFileDate(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.time.DateComponents:
        """
        Get the date of the file from which data at the specified date comes from.
        
        If several MSAFE files are available, some dates may appear in several files (for example August 2007 is in all files from the first one published in March 1999 to the February 2008 file). In this case, the data from the most recent file is used and the older ones are discarded. The date of the file is assumed to be 6 months after its first entry (which explains why the file having August 2007 as its first entry is the February 2008 file). This implies that MSAFE files must not be edited to change their time span, otherwise this would break the old entries overriding mechanism.
        
        Parameters:
            date (AbsoluteDate): date of the solar activity data
        
        Returns:
            date of the file
        
        
        """
        ...
    def getInstantFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous solar flux
        
        
        """
        ...
    def getMeanFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
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
    def getThreeHourlyKP(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using: delay=6-abs(lat)*0.033 (lat in deg.)
        
        Parameters:
            date (AbsoluteDate): the current date
        
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
        def values() -> typing.MutableSequence['MarshallSolarActivityFutureEstimation.StrengthLevel']: ...

class MarshallSolarActivityFutureEstimationLoader(AbstractSolarActivityDataLoader['MarshallSolarActivityFutureEstimationLoader.LineParameters']):
    """
    This class reads solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp indexes.
    
    The data are retrieved through the NASA Marshall Solar Activity Future Estimation (MSAFE) as estimates of monthly F10.7 Mean solar flux and Ap geomagnetic parameter. The data can be retrieved at the NASA archivedforecast. Here Kp indices are deduced from Ap indexes, which in turn are tabulated equivalent of retrieved Ap values.
    
    If several MSAFE files are available, some dates may appear in several files (for example August 2007 is in all files from the first one published in March 1999 to the February 2008 file). In this case, the data from the most recent file is used and the older ones are discarded. The date of the file is assumed to be 6 months after its first entry (which explains why the file having August 2007 as its first entry is the February 2008 file). This implies that MSAFE files must not be edited to change their time span, otherwise this would break the old entries overriding mechanism.
    
    References ----------
    
      1.  Jacchia, L. G. "CIRA 1972, recent atmospheric models, and improvements in progress." COSPAR, 21st Plenary Meeting. Vol. 1. 1978.
    """
    @typing.overload
    def __init__(self, strengthLevel: MarshallSolarActivityFutureEstimation.StrengthLevel): ...
    @typing.overload
    def __init__(self, strengthLevel: MarshallSolarActivityFutureEstimation.StrengthLevel, utc: org.orekit.time.TimeScale): ...
    def getDataSet(self) -> java.util.SortedSet['MarshallSolarActivityFutureEstimationLoader.LineParameters']:
        """
        Description copied from class: getDataSet Get the data set.
        
        Specified by: getDataSet in class AbstractSolarActivityDataLoader
        
        Returns:
            the data set
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...
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
    Also see:
        serialized
    """
    def __init__(self, supportedNames: str, loader: _PythonAbstractSolarActivityData__D, dataProvidersManager: org.orekit.data.DataProvidersManager, utc: org.orekit.time.TimeScale, maxSlots: int, maxSpan: float, maxInterval: float, minimumStep: float): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def get24HoursKp(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Description copied from interface: get24HoursKp Get the last 24H mean geomagnetic index.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 24H geomagnetic index
        
        
        """
        ...
    def getAp(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Description copied from interface: getAp Get the A :sub:`p` geomagnetic indices.
        
        A :sub:`p` indices are provided as an array such as:
        
          - 0 → daily A :sub:`p`
          - 1 → 3 hr A :sub:`p` index for current time
          - 2 → 3 hr A :sub:`p` index for 3 hrs before current time
          - 3 → 3 hr A :sub:`p` index for 6 hrs before current time
          - 4 → 3 hr A :sub:`p` index for 9 hrs before current time
          - 5 → Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
          - 6 → Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Description copied from interface: getAverageFlux Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Description copied from interface: getDailyFlux Get the value of the daily F10.7 solar flux for previous day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the daily F10.7 flux for previous day
        
        
        """
        ...
    def getInstantFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Description copied from interface: getInstantFlux Get the value of the instantaneous solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous solar flux
        
        
        """
        ...
    def getMeanFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Description copied from interface: getMeanFlux Get the value of the mean solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux
        
        
        """
        ...
    def getThreeHourlyKP(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Description copied from interface: getThreeHourlyKP Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using: delay=6-abs(lat)*0.033 (lat in deg.)
        
        Parameters:
            date (AbsoluteDate): the current date
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...


class __module_protocol__(Protocol):
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
