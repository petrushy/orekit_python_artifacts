import java.io
import java.lang
import java.util
import org.hipparchus.exception
import org.orekit.data
import org.orekit.errors
import org.orekit.models.earth.atmosphere
import org.orekit.time
import typing



class CssiSpaceWeatherData(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.models.earth.atmosphere.DTM2000InputParameters, org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters):
    """
    public class CssiSpaceWeatherData extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`, :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
    
        This class provides three-hourly and daily solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp
        indexes. The :class:`~org.orekit.data.DataLoader` implementation and the parsing is handled by the class
        :class:`~org.orekit.models.earth.atmosphere.data.CssiSpaceWeatherDataLoader`.
    
        The data are retrieved through space weather files offered by AGI/CSSI on the AGI FTP as well as on the CelesTrack
        `website <http://celestrak.com/SpaceData/>`. These files are updated several times a day by using several sources
        mentioned in the `Celestrak space weather data documentation <http://celestrak.com/SpaceData/SpaceWx-format.php>`.
    
        Since:
            10.2
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_SUPPORTED_NAMES
    
        Default regular expression for supported names that works with all officially published files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    def get24HoursKp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the last 24H mean geomagnetic index.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.get24HoursKp`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
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
        
              - 0 â†’ daily A :sub:`p`
              - 1 â†’ 3 hr A :sub:`p` index for current time
              - 2 â†’ 3 hr A :sub:`p` index for 3 hrs before current time
              - 3 â†’ 3 hr A :sub:`p` index for 6 hrs before current time
              - 4 â†’ 3 hr A :sub:`p` index for 9 hrs before current time
              - 5 â†’ Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
              - 6 â†’ Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getAp`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getAverageFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the daily F10.7 solar flux for previous day.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getDailyFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the daily F10.7 flux for previous day
        
        
        """
        ...
    def getInstantFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the instantaneous solar flux.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getInstantFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the instantaneous solar flux
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range maximum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMaxDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getMaxDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Returns:
                the maximum date.
        
        
        """
        ...
    def getMeanFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the mean solar flux.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMeanFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the mean solar flux
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range minimum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMinDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getMinDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Returns:
                the minimum date.
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
            Description copied from class: :meth:`~org.orekit.data.AbstractSelfFeedingLoader.getSupportedNames`
            Get the supported names regular expression.
        
            Overrides:
                :meth:`~org.orekit.data.AbstractSelfFeedingLoader.getSupportedNames`Â in
                classÂ :class:`~org.orekit.data.AbstractSelfFeedingLoader`
        
            Returns:
                the supported names.
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.feed`
        
        
        """
        ...
    def getThreeHourlyKP(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using:
            delay=6-abs(lat)*0.033 (lat in deg.)
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getThreeHourlyKP`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 3H geomagnetic index
        
        
        """
        ...

class CssiSpaceWeatherDataLoader(org.orekit.data.DataLoader):
    """
    public class CssiSpaceWeatherDataLoader extends Object implements :class:`~org.orekit.data.DataLoader`
    
        This class reads solar activity data from CSSI Space Weather files for the class
        :class:`~org.orekit.models.earth.atmosphere.data.CssiSpaceWeatherData`.
    
        The data are retrieved through space weather files offered by CSSI/AGI. The data can be retrieved on the AGI FTP. This
        file is updated several times a day by using several sources mentioned in the ` Celestrak space weather data
        documentation <http://celestrak.com/SpaceData/SpaceWx-format.php>`.
    
        Since:
            10.2
    """
    def __init__(self, timeScale: org.orekit.time.TimeScale): ...
    def getDataSet(self) -> java.util.SortedSet[org.orekit.time.TimeStamped]: ...
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
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float], double2: float, doubleArray2: typing.List[float], double4: float, double5: float, int: int, double6: float, double7: float, double8: float, double9: float, double10: float): ...
        def getApAvg(self) -> float: ...
        def getCtr81Adj(self) -> float: ...
        def getCtr81Obs(self) -> float: ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
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
    class LineReader:
        def __init__(self, string: str, bufferedReader: java.io.BufferedReader): ...
        def getLine(self) -> str: ...
        def getLineNumber(self) -> int: ...
        def readLine(self) -> str: ...
        def readLineOrThrow(self, localizable: org.hipparchus.exception.Localizable, objectArray: typing.List[typing.Any]) -> str: ...
        def unableToParseLine(self, throwable: java.lang.Throwable) -> org.orekit.errors.OrekitException: ...

class MarshallSolarActivityFutureEstimation(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader, org.orekit.models.earth.atmosphere.DTM2000InputParameters, org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters):
    """
    public class MarshallSolarActivityFutureEstimation extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.data.DataLoader`, :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`, :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
    
        This class reads and provides solar activity data needed by atmospheric models: F107 solar flux, Ap and Kp indexes.
    
        The data are retrieved through the NASA Marshall Solar Activity Future Estimation (MSAFE) as estimates of monthly F10.7
        Mean solar flux and Ap geomagnetic parameter. The data can be retrieved at the NASA ` Marshall Solar Activity website
        <http://sail.msfc.nasa.gov/archive_index.htm>`. Here Kp indices are deduced from Ap indexes, which in turn are tabulated
        equivalent of retrieved Ap values.
    
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
    public static final String DEFAULT_SUPPORTED_NAMES
    
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
    def get24HoursKp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            The Kp index is derived from the Ap index.
        
            The method used is explained on ` NOAA website. <http://www.ngdc.noaa.gov/stp/GEOMAG/kp_ap.html>` as follows:
        
            The scale is 0 to 9 expressed in thirds of a unit, e.g. 5- is 4 2/3, 5 is 5 and 5+ is 5 1/3. The ap (equivalent range)
            index is derived from the Kp index as follows:
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.get24HoursKp`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
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
        
              - 0 â†’ daily A :sub:`p`
              - 1 â†’ 3 hr A :sub:`p` index for current time
              - 2 â†’ 3 hr A :sub:`p` index for 3 hrs before current time
              - 3 â†’ 3 hr A :sub:`p` index for 6 hrs before current time
              - 4 â†’ 3 hr A :sub:`p` index for 9 hrs before current time
              - 5 â†’ Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
              - 6 â†’ Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getAp`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getAverageFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the daily F10.7 solar flux for previous day.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getDailyFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
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
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getInstantFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the instantaneous solar flux
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range maximum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMaxDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getMaxDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Returns:
                the maximum date.
        
        
        """
        ...
    def getMeanFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the mean solar flux.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMeanFlux`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the mean solar flux
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Gets the available data range minimum date.
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getMinDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters.getMinDate`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.NRLMSISE00InputParameters`
        
            Returns:
                the minimum date.
        
        
        """
        ...
    def getStrengthLevel(self) -> 'MarshallSolarActivityFutureEstimation.StrengthLevel':
        """
            Get the strength level for activity.
        
            Returns:
                strength level to set
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
            Description copied from class: :meth:`~org.orekit.data.AbstractSelfFeedingLoader.getSupportedNames`
            Get the supported names regular expression.
        
            Overrides:
                :meth:`~org.orekit.data.AbstractSelfFeedingLoader.getSupportedNames`Â in
                classÂ :class:`~org.orekit.data.AbstractSelfFeedingLoader`
        
            Returns:
                the supported names.
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.feed`
        
        
        """
        ...
    def getThreeHourlyKP(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using:
            delay=6-abs(lat)*0.033 (lat in deg.)
        
            Specified by:
                :meth:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters.getThreeHourlyKP`Â in
                interfaceÂ :class:`~org.orekit.models.earth.atmosphere.DTM2000InputParameters`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the current date
        
            Returns:
                the 3H geomagnetic index
        
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.atmosphere.data")``.

    CssiSpaceWeatherData: typing.Type[CssiSpaceWeatherData]
    CssiSpaceWeatherDataLoader: typing.Type[CssiSpaceWeatherDataLoader]
    MarshallSolarActivityFutureEstimation: typing.Type[MarshallSolarActivityFutureEstimation]
