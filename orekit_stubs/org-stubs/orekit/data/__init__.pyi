
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.net
import java.nio
import java.util
import java.util.regex
import jpype
import jpype.protocol
import org.hipparchus
import org.orekit.bodies
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.models.earth
import org.orekit.time
import org.orekit.utils
import typing



class AbstractSelfFeedingLoader:
    """
    Abstract class that combines a DataProvidersManager with a supported names regular expression for feed.
    
    Since:
        10.1
    """
    def __init__(self, supportedNames: str, manager: 'DataProvidersManager'):
        """
        Create an abstract data loader that can feed itself.
        
        Parameters:
            supportedNames (String): regular expression. See feed.
            manager (DataProvidersManager): the source of auxiliary data files.
        
        
        """
        ...

class DataContext:
    """
    Provides auxiliary data for portions of the application.
    
    Since:
        10.1
    """
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies:
        """
        Get a factory constructing CelestialBodys based on the auxiliary data in this context.
        
        Returns:
            the set of common celestial bodies using this data context.
        
        
        """
        ...
    @staticmethod
    def getDefault() -> 'LazyLoadedDataContext':
        """
        Get the default data context that is used to implement the static factories (TimeScalesFactory, FramesFactory, etc) and loaders that feed themselves (e.g. KlobucharIonoCoefficientsLoader). It is used to maintain compatibility with auxiliary data loading in Orekit 10.0.
        
        Returns:
            Orekit's default data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.Frames:
        """
        Get a factory constructing Frames based on the auxiliary data in this context.
        
        Returns:
            the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields:
        """
        Get a factory constructing GeoMagneticFields based on the auxiliary data in this context.
        
        Returns:
            the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields:
        """
        Get a factory constructing gravity fields based on the auxiliary data in this context.
        
        Returns:
            the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
        Get a factory for constructing TimeScales based on the auxiliary data in this context.
        
        Returns:
            the set of common time scales using this data context.
        
        
        """
        ...
    @staticmethod
    def setDefault(context: 'LazyLoadedDataContext') -> None:
        """
        Set the default data context that is used to implement Orekit's static factories.
        
        Calling this method will not modify any instances already retrieved from Orekit's static factories. In general this method should only be called at application start up before any of the static factories are used.
        
        Parameters:
            context (LazyLoadedDataContext): the new data context.
        
        Also see:
            getDefault
        
        
        """
        ...

class DataFilter:
    """
    Interface for filtering data (typically uncompressing it) in DataProvider before passing it to DataLoader.
    
    Since:
        9.2
    
    Also see:
        DataProvider, DataLoader
    """
    def filter(self, original: 'DataSource') -> 'DataSource':
        """
        Filter the data source.
        
        Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
        A filter must never openStreamOnce the DataSource by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it is the upper layer that will decide to open (or not) the returned value and that a DataSource can be opened only once; this is the core principle of lazy-opening provided by DataSource.
        
        Beware that as the DataProvidersManager will attempt to pile all filters in a stack as long as their implementation of this method returns a value different from the original parameter. This implies that the filter, must perform some checks to see if it must be applied or not. If for example there is a need for a deciphering filter to be applied once to all data, then the filter should for example check for a suffix in the getName and create a new filtered DataSource instance only if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering filters being built, until a stack overflow or memory exhaustion exception occurs.
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            filtered data source, or original if this filter does not apply to this data source
        
        Raises:
            IOException: if filtered stream cannot be created
        
        
        """
        ...

class DataLoader:
    """
    Interface for loading data files from DataProvider.
    
    Also see:
        DataProvider
    """
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
        
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
        Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Returns:
            true while the loader still accepts new data
        
        
        """
        ...

class DataProvider:
    """
    Interface for providing data files to DataLoader.
    
    This interface defines a generic way to explore some collection holding data files and load some of them. The collection may be a list of resources in the classpath, a directories tree in filesystem, a zip or jar archive, a database, a connexion to a remote server ...
    
    The proper way to use this interface is to configure one or more implementations and register them in the DataProvidersManager, or to let this manager use its default configuration. Once registered, they will be used automatically whenever some data needs to be loaded. This allow high level applications developers to customize Orekit data loading mechanism and get a tighter integration of the library within their application.
    
    Also see:
        DataLoader, DataProvidersManager
    """
    ZIP_ARCHIVE_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    """
    Pattern for name of zip/jar archives.
    """
    def feed(self, supported: java.util.regex.Pattern, visitor: DataLoader, manager: 'DataProvidersManager') -> bool:
        """
        Feed a data file loader by browsing the data collection.
        
        The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file supported by the file loader it asks the file loader to load it.
        
        If the method completes without exception, then the data loader is considered to have been fed successfully and the top level DataProvidersManager will return immediately without attempting to use the next configured providers.
        
        If the method completes abruptly with an exception, then the top level DataProvidersManager will try to use the next configured providers, in case another one can feed the DataLoader.
        
        Parameters:
            supported (Pattern): pattern for file names supported by the visitor
            visitor (DataLoader): data file visitor to use
            manager (DataProvidersManager): with the filters to apply to the resources.
        
        Returns:
            true if some data has been loaded
        
        
        """
        ...

class DataProvidersManager:
    """
    This class manages supported DataProvider.
    
    This class is the primary point of access for all data loading features. It is used for example to load Earth Orientation Parameters used by IERS frames, to load UTC leap seconds used by time scales, to load planetary ephemerides...
    
    It is user-customizable: users can add their own data providers at will. This allows them for example to use a database or an existing data loading library in order to embed an Orekit enabled application in a global system with its own data handling mechanisms. There is no upper limitation on the number of providers, but often each application will use only a few.
    
    If the list of providers is empty when attempting to feed a file loader, the addDefaultProviders method is called automatically to set up a default configuration. This default configuration contains one DataProvider for each component of the path-like list specified by the java property path. See the feed method documentation for further details. The default providers configuration is not set up if the list is not empty. If users want to have both the default providers and additional providers, they must call explicitly the addDefaultProviders method.
    
    The default configuration uses a predefined set of DataFilter that already handled gzip-compressed files (recognized by the gz suffix), Unix-compressed files (recognized by the Z suffix) and Hatanaka compressed RINEX files. Users can access the getFiltersManager to set up custom filters for handling specific types of filters (decompression, deciphering...).
    
    Also see:
        DirectoryCrawler, ClasspathCrawler
    """
    OREKIT_DATA_PATH: typing.ClassVar[str] = ...
    """
    Name of the property defining the root directories or zip/jar files path for default configuration.
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Build an instance with default configuration.
        """
        ...
    def addDefaultProviders(self) -> None:
        """
        Add the default providers configuration.
        
        The default configuration contains one DataProvider for each component of the path-like list specified by the java property path.
        
        If the property is not set or is null, no data will be available to the library (for example no pole corrections will be applied and only predefined UTC steps will be taken into account). No errors will be triggered in this case.
        
        If the property is set, it must contains a list of existing directories or zip/jar archives. One DirectoryCrawler instance will be set up for each directory and one ZipJarCrawler instance (configured to look for the archive in the filesystem) will be set up for each zip/jar archive. The list elements in the java property are separated using the standard path separator for the operating system as returned by System. This standard path separator is ":" on Linux and Unix type systems and ";" on Windows types systems.
        """
        ...
    def addProvider(self, provider: typing.Union[DataProvider, typing.Callable]) -> None:
        """
        Add a data provider to the supported list.
        
        Parameters:
            provider (DataProvider): data provider to add
        
        Also see:
            removeProvider,
            clearProviders, isSupported,
            getProviders
        
        
        """
        ...
    def clearLoadedDataNames(self) -> None:
        """
        Clear the set of data file names that have been loaded.
        
        Also see:
            getLoadedDataNames
        
        
        """
        ...
    def clearProviders(self) -> None:
        """
        Remove all data providers.
        
        Also see:
            addProvider, removeProvider,
            isSupported, getProviders
        
        
        """
        ...
    def feed(self, supportedNames: str, loader: DataLoader) -> bool:
        """
        Feed a data file loader by browsing all data providers.
        
        If this method is called with an empty list of providers, a default providers configuration is set up. This default configuration contains only one DataProvider: a DirectoryCrawler instance that loads data from files located somewhere in a directory hierarchy. This default provider is not added if the list is not empty. If users want to have both the default provider and other providers, they must add it explicitly.
        
        The providers are used in the order in which they were addProvider. As soon as one provider is able to feed the data loader, the loop is stopped. If no provider is able to feed the data loader, then the last error triggered is thrown.
        
        Parameters:
            supportedNames (String): regular expression for file names supported by the visitor
            loader (DataLoader): data loader to use
        
        Returns:
            true if some data has been loaded
        
        
        """
        ...
    def getFiltersManager(self) -> 'FiltersManager':
        """
        Get the manager for filters.
        
        Returns:
            filters manager
        
        Since:
            11.0
        
        
        """
        ...
    def getLoadedDataNames(self) -> java.util.Set[str]:
        """
        Get an unmodifiable view of the set of data file names that have been loaded.
        
        The names returned are exactly the ones that were given to the loadData method.
        
        Returns:
            unmodifiable view of the set of data file names that have been loaded
        
        Also see:
            feed, clearLoadedDataNames
        
        
        """
        ...
    def getProviders(self) -> java.util.List[DataProvider]:
        """
        Get an unmodifiable view of the list of supported providers.
        
        Returns:
            unmodifiable view of the list of supported providers
        
        Also see:
            addProvider, removeProvider,
            clearProviders, isSupported
        
        
        """
        ...
    def isSupported(self, provider: typing.Union[DataProvider, typing.Callable]) -> bool:
        """
        Check if some provider is supported.
        
        Parameters:
            provider (DataProvider): provider to check
        
        Returns:
            true if the specified provider instance is already in the supported list
        
        Since:
            5.1
        
        Also see:
            addProvider, removeProvider,
            clearProviders, getProviders
        
        
        """
        ...
    def removeProvider(self, provider: typing.Union[DataProvider, typing.Callable]) -> DataProvider:
        """
        Remove one provider.
        
        Parameters:
            provider (DataProvider): provider instance to remove
        
        Returns:
            instance removed (null if the provider was not already present)
        
        Since:
            5.1
        
        Also see:
            addProvider, clearProviders,
            isSupported, getProviders
        
        
        """
        ...
    def resetFiltersToDefault(self) -> None:
        """
        Reset all filters to default.
        
        This method clearFilters the getFiltersManager and then addFilter back the default filters
        
        Since:
            11.0
        
        
        """
        ...

class DataSource:
    """
    Container associating a name with a stream or reader that can be opened lazily.
    
    This association and the lazy-opening are useful in different cases:
    
      - when DirectoryCrawler a directory tree to select data to be loaded by a
        DataLoader, the files that are not meaningful for the loader can be ignored and not opened at
        all
      - when DataFilter is used, the raw stream can be opened by the filter only if the upper level
        filtered stream is opened
      - when opening a stream for loading the data it provides, the opening and closing actions can be grouped in Orekit
        internal code using a try with resources clause so closing is done properly even in case of exception
      - if some pre-reading of the first few bytes or characters are needed to decide how to load data (as in
        LexicalAnalyzerSelector), then the stream can be opened, buffered and
        rewound and a fake open method used to return the already open stream so a try with resources clause elsewhere
        works properly for closing the stream
    
    Beware that the purpose of this class is only to delay this opening (or not open the stream or reader at all), it is not intended to open the stream several times and not intended to open both the binary stream and the characters reader. Some implementations may fail if the getOpener's openStreamOnce or openReaderOnce methods are called several times or are both called separately. This is particularly true for network-based streams.
    
    Since:
        9.2
    
    Also see:
        DataFilter
    """
    @typing.overload
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, readerOpener: typing.Union['DataSource.ReaderOpener', typing.Callable]): ...
    @typing.overload
    def __init__(self, string: str, streamOpener: typing.Union['DataSource.StreamOpener', typing.Callable]): ...
    @typing.overload
    def __init__(self, uRI: java.net.URI): ...
    def getName(self) -> str:
        """
        Get the name of the data.
        
        Returns:
            name of the data
        
        
        """
        ...
    def getOpener(self) -> 'DataSource.Opener':
        """
        Get the data stream opener.
        
        Returns:
            data stream opener
        
        
        """
        ...
    class Opener:
        def openReaderOnce(self) -> java.io.Reader: ...
        def openStreamOnce(self) -> java.io.InputStream: ...
        def rawDataIsBinary(self) -> bool: ...
    class ReaderOpener:
        def openOnce(self) -> java.io.Reader: ...
    class StreamOpener:
        def openOnce(self) -> java.io.InputStream: ...

class DelaunayArguments(org.orekit.time.TimeStamped):
    """
    Delaunay arguments used for nutation or tides.
    
    This class is a simple placeholder, it does not provide any processing method.
    
    Since:
        6.1
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, tc: float, gamma: float, gammaDot: float, l: float, lDot: float, lPrime: float, lPrimeDot: float, f: float, fDot: float, d: float, dDot: float, omega: float, omegaDot: float):
        """
        Simple constructor.
        
        Parameters:
            date (AbsoluteDate): current date
            tc (double): offset in Julian centuries
            gamma (double): tide parameter γ = GMST + π
            gammaDot (double): tide parameter γ = GMST + π time derivative
            l (double): mean anomaly of the Moon
            lDot (double): mean anomaly of the Moon time derivative
            lPrime (double): mean anomaly of the Sun
            lPrimeDot (double): mean anomaly of the Sun time derivative
            f (double): L - Ω where L is the mean longitude of the Moon
            fDot (double): L - Ω where L is the mean longitude of the Moon time derivative
            d (double): mean elongation of the Moon from the Sun
            dDot (double): mean elongation of the Moon from the Sun time derivative
            omega (double): mean longitude of the ascending node of the Moon
            omegaDot (double): mean longitude of the ascending node of the Moon time derivative
        
        
        """
        ...
    def getD(self) -> float:
        """
        Get the mean elongation of the Moon from the Sun.
        
        Returns:
            mean elongation of the Moon from the Sun.
        
        
        """
        ...
    def getDDot(self) -> float:
        """
        Get the mean elongation of the Moon from the Sun time derivative.
        
        Returns:
            mean elongation of the Moon from the Sun time derivative.
        
        
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
    def getF(self) -> float:
        """
        Get L - Ω where L is the mean longitude of the Moon.
        
        Returns:
            L - Ω
        
        
        """
        ...
    def getFDot(self) -> float:
        """
        Get L - Ω where L is the mean longitude of the Moon time derivative.
        
        Returns:
            L - Ω time derivative
        
        
        """
        ...
    def getGamma(self) -> float:
        """
        Get the tide parameter γ = GMST + π.
        
        Returns:
            tide parameter γ = GMST + π
        
        
        """
        ...
    def getGammaDot(self) -> float:
        """
        Get the tide parameter γ = GMST + π time derivative.
        
        Returns:
            tide parameter γ = GMST + π time derivative
        
        
        """
        ...
    def getL(self) -> float:
        """
        Get the mean anomaly of the Moon.
        
        Returns:
            mean anomaly of the Moon
        
        
        """
        ...
    def getLDot(self) -> float:
        """
        Get the mean anomaly of the Moon time derivative.
        
        Returns:
            mean anomaly of the Moon time derivative
        
        
        """
        ...
    def getLPrime(self) -> float:
        """
        Get the mean anomaly of the Sun.
        
        Returns:
            mean anomaly of the Sun.
        
        
        """
        ...
    def getLPrimeDot(self) -> float:
        """
        Get the mean anomaly of the Sun time derivative.
        
        Returns:
            mean anomaly of the Sun time derivative.
        
        
        """
        ...
    def getOmega(self) -> float:
        """
        Get the mean longitude of the ascending node of the Moon.
        
        Returns:
            mean longitude of the ascending node of the Moon.
        
        
        """
        ...
    def getOmegaDot(self) -> float:
        """
        Get the mean longitude of the ascending node of the Moon time derivative.
        
        Returns:
            mean longitude of the ascending node of the Moon time derivative.
        
        
        """
        ...
    def getTC(self) -> float:
        """
        Get the offset in Julian centuries.
        
        Returns:
            offset in Julian centuries
        
        
        """
        ...

_FieldDelaunayArguments__T = typing.TypeVar('_FieldDelaunayArguments__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDelaunayArguments(org.orekit.time.FieldTimeStamped[_FieldDelaunayArguments__T], typing.Generic[_FieldDelaunayArguments__T]):
    """
    Delaunay arguments used for nutation or tides.
    
    This class is a simple placeholder, it does not provide any processing method.
    
    Since:
        6.1
    
    Also see:
        DelaunayArguments
    """
    def __init__(self, date: org.orekit.time.FieldAbsoluteDate[_FieldDelaunayArguments__T], tc: _FieldDelaunayArguments__T, gamma: _FieldDelaunayArguments__T, gammaDot: _FieldDelaunayArguments__T, l: _FieldDelaunayArguments__T, lDot: _FieldDelaunayArguments__T, lPrime: _FieldDelaunayArguments__T, lPrimeDot: _FieldDelaunayArguments__T, f: _FieldDelaunayArguments__T, fDot: _FieldDelaunayArguments__T, d: _FieldDelaunayArguments__T, dDot: _FieldDelaunayArguments__T, omega: _FieldDelaunayArguments__T, omegaDot: _FieldDelaunayArguments__T):
        """
        Simple constructor.
        
        Parameters:
            date (FieldAbsoluteDate<FieldDelaunayArguments> date): current date
            tc (FieldDelaunayArguments): offset in Julian centuries
            gamma (FieldDelaunayArguments): tide parameter γ = GMST + π
            gammaDot (FieldDelaunayArguments): tide parameter γ = GMST + π time derivative
            l (FieldDelaunayArguments): mean anomaly of the Moon
            lDot (FieldDelaunayArguments): mean anomaly of the Moon time derivative
            lPrime (FieldDelaunayArguments): mean anomaly of the Sun
            lPrimeDot (FieldDelaunayArguments): mean anomaly of the Sun time derivative
            f (FieldDelaunayArguments): L - Ω where L is the mean longitude of the Moon
            fDot (FieldDelaunayArguments): L - Ω where L is the mean longitude of the Moon time derivative
            d (FieldDelaunayArguments): mean elongation of the Moon from the Sun
            dDot (FieldDelaunayArguments): mean elongation of the Moon from the Sun time derivative
            omega (FieldDelaunayArguments): mean longitude of the ascending node of the Moon
            omegaDot (FieldDelaunayArguments): mean longitude of the ascending node of the Moon time derivative
        
        
        """
        ...
    def getD(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean elongation of the Moon from the Sun.
        
        Returns:
            mean elongation of the Moon from the Sun.
        
        
        """
        ...
    def getDDot(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean elongation of the Moon from the Sun time derivative.
        
        Returns:
            mean elongation of the Moon from the Sun time derivative.
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldDelaunayArguments__T]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getF(self) -> _FieldDelaunayArguments__T:
        """
        Get L - Ω where L is the mean longitude of the Moon.
        
        Returns:
            L - Ω
        
        
        """
        ...
    def getFDot(self) -> _FieldDelaunayArguments__T:
        """
        Get L - Ω where L is the mean longitude of the Moon time derivative.
        
        Returns:
            L - Ω time derivative
        
        
        """
        ...
    def getGamma(self) -> _FieldDelaunayArguments__T:
        """
        Get the tide parameter γ = GMST + π.
        
        Returns:
            tide parameter γ = GMST + π
        
        
        """
        ...
    def getGammaDot(self) -> _FieldDelaunayArguments__T:
        """
        Get the tide parameter γ = GMST + π time derivative.
        
        Returns:
            tide parameter γ = GMST + π time derivative
        
        
        """
        ...
    def getL(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean anomaly of the Moon.
        
        Returns:
            mean anomaly of the Moon
        
        
        """
        ...
    def getLDot(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean anomaly of the Moon time derivative.
        
        Returns:
            mean anomaly of the Moon time derivative
        
        
        """
        ...
    def getLPrime(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean anomaly of the Sun.
        
        Returns:
            mean anomaly of the Sun.
        
        
        """
        ...
    def getLPrimeDot(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean anomaly of the Sun time derivative.
        
        Returns:
            mean anomaly of the Sun time derivative.
        
        
        """
        ...
    def getOmega(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean longitude of the ascending node of the Moon.
        
        Returns:
            mean longitude of the ascending node of the Moon.
        
        
        """
        ...
    def getOmegaDot(self) -> _FieldDelaunayArguments__T:
        """
        Get the mean longitude of the ascending node of the Moon time derivative.
        
        Returns:
            mean longitude of the ascending node of the Moon time derivative.
        
        
        """
        ...
    def getTC(self) -> _FieldDelaunayArguments__T:
        """
        Get the offset in Julian centuries.
        
        Returns:
            offset in Julian centuries
        
        
        """
        ...

class FiltersManager:
    """
    Manager for DataFilter.
    
    This manager holds a set of filters and applies all the relevant ones by building a stack that transforms a raw DataSource into a processed DataSource.
    
    Since:
        11.0
    
    Also see:
        DataSource, DataFilter
    """
    def __init__(self):
        """
        Build an empty manager.
        """
        ...
    def addFilter(self, filter: typing.Union[DataFilter, typing.Callable]) -> None:
        """
        Add a data filter.
        
        Parameters:
            filter (DataFilter): filter to add
        
        Also see:
            applyRelevantFilters, clearFilters
        
        
        """
        ...
    def applyRelevantFilters(self, original: DataSource) -> DataSource:
        """
        Apply all the relevant data filters, taking care of layers.
        
        If several filters can be applied, they will all be applied as a stack, even recursively if required. This means that if filter A applies to files with names of the form base.ext.a and filter B applies to files with names of the form base.ext.b, then providing base.ext.a.b.a will result in filter A being applied on top of filter B which itself is applied on top of another instance of filter A.
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            fully filtered data source
        
        Raises:
            IOException: if some data stream cannot be filtered
        
        Since:
            9.2
        
        Also see:
            addFilter, clearFilters
        
        
        """
        ...
    def clearFilters(self) -> None:
        """
        Remove all data filters.
        
        Also see:
            addFilter
        
        
        """
        ...

class FundamentalNutationArguments:
    """
    Class computing the fundamental arguments for nutation and tides.
    
    The fundamental arguments are split in two sets:
    
      - the Delaunay arguments for Moon and Sun effects
      - the planetary arguments for other planets
    
    
    Also see:
        SeriesTerm, PoissonSeries, BodiesElements
    """
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, inputStream: java.io.InputStream, string: str): ...
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, stream: java.io.InputStream, name: str, timeScales: org.orekit.time.TimeScales): ...
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, coefficients: java.util.List[typing.Union[typing.List[float], jpype.JArray]]): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, list: java.util.List[typing.Union[typing.List[float], jpype.JArray]], timeScales: org.orekit.time.TimeScales): ...
    _evaluateAll_1__T = typing.TypeVar('_evaluateAll_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def evaluateAll(self, date: org.orekit.time.AbsoluteDate) -> 'BodiesElements':
        """
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            all fundamental arguments for the current date (Delaunay plus planetary)
        
        """
        ...
    @typing.overload
    def evaluateAll(self, date: org.orekit.time.FieldAbsoluteDate[_evaluateAll_1__T]) -> 'FieldBodiesElements'[_evaluateAll_1__T]:
        """
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            all fundamental arguments for the current date (Delaunay plus planetary)
        
        
        """
        ...

class LineOrientedFilteringReader(java.io.Reader):
    """
    Base class for implementing line-oriented data filtering readers.
    
    This reader is intended to be used in DataFilter.
    
    Since:
        12.1
    """
    def __init__(self, name: str, input: java.io.Reader):
        """
        Simple constructor.
        
        Parameters:
            name (String): file name
            input (Reader): underlying raw stream
        
        Raises:
            IOException: if first lines cannot be read
        
        
        """
        ...
    def close(self) -> None:
        """
        Specified by: AutoCloseable in interface AutoCloseable
        
        Specified by: Closeable in interface Closeable
        
        Specified by: Reader in class Reader
        
        Raises:
            IOException: 
        
        """
        ...
    @typing.overload
    def read(self) -> int: ...
    @typing.overload
    def read(self, charArray: typing.Union[typing.List[str], jpype.JArray]) -> int: ...
    @typing.overload
    def read(self, charBuffer: java.nio.CharBuffer) -> int: ...
    @typing.overload
    def read(self, b: typing.Union[typing.List[str], jpype.JArray], offset: int, len: int) -> int: ...

class PoissonSeries:
    """
    Class representing a Poisson series for nutation or ephemeris computations.
    
    A Poisson series is composed of a time polynomial part and a non-polynomial part which consist in summation series. The series terms are harmonic functions (combination of sines and cosines) of polynomial arguments. The polynomial arguments are combinations of luni-solar or planetary BodiesElements.
    
    Also see:
        PoissonSeriesParser, SeriesTerm, PolynomialNutation
    """
    def __init__(self, polynomial: 'PolynomialNutation', series: typing.Union[java.util.Map[int, 'SeriesTerm'], typing.Mapping[int, 'SeriesTerm']]):
        """
        Build a Poisson series from an IERS table file.
        
        Parameters:
            polynomial (PolynomialNutation): polynomial part (may be null)
            series (Map<Long, org.orekit.data.SeriesTerm> series): non-polynomial part
        
        
        """
        ...
    @staticmethod
    def compile(*poissonSeries: 'PoissonSeries') -> 'PoissonSeries.CompiledSeries':
        """
        Join several nutation series, for fast simultaneous evaluation.
        
        Parameters:
            poissonSeries (PoissonSeries...): Poisson series to join
        
        Returns:
            a single function that evaluates all series together
        
        Since:
            6.1
        
        
        """
        ...
    def getNonPolynomialSize(self) -> int:
        """
        Get the number of different terms in the non-polynomial part.
        
        Returns:
            number of different terms in the non-polynomial part
        
        
        """
        ...
    def getPolynomial(self) -> 'PolynomialNutation':
        """
        Get the polynomial part of the series.
        
        Returns:
            polynomial part of the series.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, elements: 'BodiesElements') -> float:
        """
        Evaluate the value of the series.
        
        Parameters:
            elements (BodiesElements): bodies elements for nutation
        
        Returns:
            value of the series
        
        """
        ...
    @typing.overload
    def value(self, elements: 'FieldBodiesElements'[_value_1__T]) -> _value_1__T:
        """
        Evaluate the value of the series.
        
        Parameters:
            elements (FieldBodiesElements<T> elements): bodies elements for nutation
        
        Returns:
            value of the series
        
        
        """
        ...
    class CompiledSeries:
        _derivative_1__S = typing.TypeVar('_derivative_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
        @typing.overload
        def derivative(self, bodiesElements: 'BodiesElements') -> typing.MutableSequence[float]: ...
        @typing.overload
        def derivative(self, fieldBodiesElements: 'FieldBodiesElements'[_derivative_1__S]) -> typing.MutableSequence[_derivative_1__S]: ...
        _value_1__S = typing.TypeVar('_value_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
        @typing.overload
        def value(self, bodiesElements: 'BodiesElements') -> typing.MutableSequence[float]: ...
        @typing.overload
        def value(self, fieldBodiesElements: 'FieldBodiesElements'[_value_1__S]) -> typing.MutableSequence[_value_1__S]: ...

class PoissonSeriesParser:
    """
    Parser for PoissonSeries files.
    
    A Poisson series is composed of a time polynomial part and a non-polynomial part which consist in summation series. The series terms are harmonic functions (combination of sines and cosines) of polynomial arguments. The polynomial arguments are combinations of luni-solar or planetary BodiesElements.
    
    The Poisson series files from IERS have various formats, with or without polynomial part, with or without planetary components, with or without period column, with terms of increasing degrees either in dedicated columns or in successive sections of the file ... This class attempts to read all the commonly found formats, by specifying the columns of interest.
    
    The handling of increasing degrees terms (i.e. sin, cos, t sin, t cos, t^2 sin, t^2 cos ...) is done as follows.
    
      - user must specify pairs of columns to be extracted at each line, in increasing degree order
      - negative columns indices correspond to inexistent values that will be replaced by 0.0)
      - file may provide section headers to specify a degree, which is added to the current column degree
    
    A file from an old convention, like table 5.1 in IERS conventions 1996, uses separate columns for degree 0 and degree 1, and uses only sine for nutation in longitude and cosine for nutation in obliquity. It reads as follows:
    
     ∆ψ = Σ (Ai+A'it) sin(ARGUMENT), ∆ε = Σ (Bi+B'it) cos(ARGUMENT)
    
          MULTIPLIERS OF      PERIOD           LONGITUDE         OBLIQUITY l    l'   F    D   Om     days         Ai       A'i       Bi       B'i
    
      0    0    0    0    1   -6798.4    -171996    -174.2    92025      8.9 0    0    2   -2    2     182.6     -13187      -1.6     5736     -3.1 0    0    2    0    2      13.7      -2274      -0.2      977     -0.5 0    0    0    0    2   -3399.2       2062       0.2     -895      0.5
    
    In order to parse the nutation in longitude from the previous table, the following settings should be used:
    
      - totalColumns = 10 (see )
      - firstDelaunay = 1 (see withFirstDelaunay)
      - no calls to withFirstPlanetary as there are no planetary columns in this
        table
      - sinCosColumns = 7, -1 for degree 0 for Ai (see withSinCos)
      - sinCosColumns = 8, -1 for degree 1 for A'i (see withSinCos)
    
    In order to parse the nutation in obliquity from the previous table, the following settings should be used:
    
      - totalColumns = 10 (see )
      - firstDelaunay = 1 (see withFirstDelaunay)
      - no calls to withFirstPlanetary as there are no planetary columns in this
        table
      - sinCosColumns = -1, 9 for degree 0 for Bi (see withSinCos)
      - sinCosColumns = -1, 10 for degree 1 for B'i (see withSinCos)
    
    A file from a recent convention, like table 5.3a in IERS conventions 2010, uses only two columns for sin and cos, and separate degrees in successive sections with dedicated headers. It reads as follows:
    
     ---------------------------------------------------------------------------------------------------
    
     (unit microarcsecond; cut-off: 0.1 microarcsecond) (ARG being for various combination of the fundamental arguments of the nutation theory)
    
       Sum_i[A_i * sin(ARG) + A"_i * cos(ARG)]
    
     + Sum_i[A'_i * sin(ARG) + A"'_i * cos(ARG)] * t           (see Chapter 5, Eq. (35))
    
     The Table below provides the values for A_i and A"_i (j=0) and then A'_i and A"'_i (j=1)
    
     The expressions for the fundamental arguments appearing in columns 4 to 8 (luni-solar part) and in columns 9 to 17 (planetary part) are those of the IERS Conventions 2003
    
     ---------------------------------------------------------------------------------------------------------- j = 0  Number of terms = 1320 ---------------------------------------------------------------------------------------------------------- i        A_i             A"_i     l    l'   F    D    Om  L_Me L_Ve  L_E L_Ma  L_J L_Sa  L_U L_Ne  p_A ---------------------------------------------------------------------------------------------------------- 1   -17206424.18        3338.60    0    0    0    0    1    0    0    0    0    0    0    0    0    0 2    -1317091.22       -1369.60    0    0    2   -2    2    0    0    0    0    0    0    0    0    0 3     -227641.81         279.60    0    0    2    0    2    0    0    0    0    0    0    0    0    0 4      207455.40         -69.80    0    0    0    0    2    0    0    0    0    0    0    0    0    0 5      147587.70        1181.70    0    1    0    0    0    0    0    0    0    0    0    0    0    0
    
     ...
    
      1319          -0.10           0.00    0    0    0    0    0    1    0   -3    0    0    0    0    0   -2 1320          -0.10           0.00    0    0    0    0    0    0    0    1    0    1   -2    0    0    0
    
     -------------------------------------------------------------------------------------------------------------- j = 1  Number of terms = 38 -------------------------------------------------------------------------------------------------------------- i          A'_i            A"'_i    l    l'   F    D   Om L_Me L_Ve  L_E L_Ma  L_J L_Sa  L_U L_Ne  p_A -------------------------------------------------------------------------------------------------------------- 1321      -17418.82           2.89    0    0    0    0    1    0    0    0    0    0    0    0    0    0 1322        -363.71          -1.50    0    1    0    0    0    0    0    0    0    0    0    0    0    0 1323        -163.84           1.20    0    0    2   -2    2    0    0    0    0    0    0    0    0    0 1324         122.74           0.20    0    1    2   -2    2    0    0    0    0    0    0    0    0    0
    
    In order to parse the nutation in longitude from the previous table, the following settings should be used:
    
      - totalColumns = 17 (see )
      - firstDelaunay = 4 (see withFirstDelaunay)
      - firstPlanetary = 9 (see withFirstPlanetary)
      - sinCosColumns = 2,3 (we specify only degree 0, so when we read section j = 0 we read degree 0, when we read section j =
        1 we read degree 1, see withSinCos ...)
    
    A file from a recent convention, like table 6.5a in IERS conventions 2010, contains both Doodson arguments (τ, s, h, p, N', ps), Doodson numbers and Delaunay parameters. In this case, the coefficients for the Delaunay parameters must be subtracted from the τ = GMST + π tide parameter, so the signs in the files must be reversed in order to match the Doodson arguments and Doodson numbers. This is done automatically (and consistency is checked) only when the withDoodson method is called at parser configuration time. Some other files use the γ = GMST + π tide parameter rather than Doodson τ argument and the coefficients for the Delaunay parameters must be added to the γ parameter, so no sign reversal is performed. In order to avoid ambiguity as the two cases are incompatible with each other, trying to add a configuration for τ by calling withDoodson and to also add a configuration for γ by calling withGamma triggers an exception.
    
    The table 6.5a file also contains a column for the waves names (the Darwin's symbol) which may be empty, so it must be identified explicitly by calling withOptionalColumn. The 6.5a table reads as follows:
    
     The in-phase (ip) amplitudes (A₁ δkfR Hf) and the out-of-phase (op) amplitudes (A₁ δkfI Hf) of the corrections for frequency dependence of k₂₁⁽⁰⁾, taking the nominal value k₂₁ for the diurnal tides as (0.29830 − i 0.00144). Units: 10⁻¹² . The entries for δkfR and δkfI are in units of 10⁻⁵. Multipliers of the Doodson arguments identifying the tidal terms are given, as also those of the Delaunay variables characterizing the nutations produced by these terms.
    
     Name   deg/hr    Doodson  τ  s  h  p  N' ps   l  l' F  D  Ω  δkfR  δkfI     Amp.    Amp. No.                                       /10−5 /10−5    (ip)    (op) 2Q₁ 12.85429   125,755  1 -3  0  2   0  0   2  0  2  0  2    -29     3    -0.1     0.0 σ₁ 12.92714   127,555  1 -3  2  0   0  0   0  0  2  2  2    -30     3    -0.1     0.0 13.39645   135,645  1 -2  0  1  -1  0   1  0  2  0  1    -45     5    -0.1     0.0 Q₁ 13.39866   135,655  1 -2  0  1   0  0   1  0  2  0  2    -46     5    -0.7     0.1 ρ₁ 13.47151   137,455  1 -2  2 -1   0  0  -1  0  2  2  2    -49     5    -0.1     0.0
    
      - totalColumns = 18 (see )
      - optionalColumn = 1 (see withOptionalColumn)
      - firstDoodson, Doodson number = 4, 3 (see withDoodson)
      - firstDelaunay = 10 (see withFirstDelaunay)
      - sinCosColumns = 17, 18, see withSinCos ...)
    
    Our parsing algorithm involves adding the section degree from the "j = 0, 1, 2 ..." header to the column degree. A side effect of this algorithm is that it is theoretically possible to mix both formats and have for example degree two term appear as degree 2 column in section j=0 and as degree 1 column in section j=1 and as degree 0 column in section j=2. This case is not expected to be encountered in practice. The real files use either several columns or several sections, but not both at the same time.
    
    Since:
        6.1
    
    Also see:
        SeriesTerm, PolynomialNutation
    """
    def __init__(self, totalColumns: int):
        """
        Build a parser for a Poisson series from an IERS table file.
        
        Parameters:
            totalColumns (int): total number of columns in the non-polynomial sections
        
        
        """
        ...
    def parse(self, stream: java.io.InputStream, name: str) -> PoissonSeries:
        """
        Parse a stream.
        
        Parameters:
            stream (InputStream): stream containing the IERS table
            name (String): name of the resource file (for error messages only)
        
        Returns:
            parsed Poisson series
        
        
        """
        ...
    def withDoodson(self, firstMultiplierColumn: int, numberColumn: int) -> 'PoissonSeriesParser':
        """
        Set up columns for Doodson multipliers and Doodson number.
        
        Parameters:
            firstMultiplierColumn (int): column of the first Doodson multiplier which corresponds to τ (counting from 1)
            numberColumn (int): column of the Doodson number (counting from 1)
        
        Returns:
            a new parser, with updated columns settings
        
        Also see:
            withGamma, withFirstDelaunay
        
        
        """
        ...
    def withFirstDelaunay(self, firstColumn: int) -> 'PoissonSeriesParser':
        """
        Set up first column of Delaunay multiplier.
        
        Parameters:
            firstColumn (int): column of the first Delaunay multiplier (counting from 1)
        
        Returns:
            a new parser, with updated columns settings
        
        
        """
        ...
    def withFirstPlanetary(self, firstColumn: int) -> 'PoissonSeriesParser':
        """
        Set up first column of planetary multiplier.
        
        Parameters:
            firstColumn (int): column of the first planetary multiplier (counting from 1)
        
        Returns:
            a new parser, with updated columns settings
        
        
        """
        ...
    def withGamma(self, column: int) -> 'PoissonSeriesParser':
        """
        Set up column of GMST tide multiplier.
        
        Parameters:
            column (int): column of the GMST tide multiplier (counting from 1)
        
        Returns:
            a new parser, with updated columns settings
        
        Also see:
            withDoodson
        
        
        """
        ...
    def withOptionalColumn(self, column: int) -> 'PoissonSeriesParser':
        """
        Set up optional column.
        
        Optional columns typically appears in tides-related files, as some waves have specific names (χ₁, M₂...) and other waves don't have names and hence are replaced by spaces in the corresponding file line.
        
        At most one column may be optional.
        
        Parameters:
            column (int): optional column (counting from 1)
        
        Returns:
            a new parser, with updated columns settings
        
        
        """
        ...
    def withPolynomialPart(self, freeVariable: str, unit: 'PolynomialParser.Unit') -> 'PoissonSeriesParser':
        """
        Set up polynomial part parsing.
        
        Parameters:
            freeVariable (char): name of the free variable in the polynomial part
            unit (Unit): default unit for polynomial, if not explicit within the file
        
        Returns:
            a new parser, with polynomial parser updated
        
        
        """
        ...
    def withSinCos(self, degree: int, sinColumn: int, sinFactor: float, cosColumn: int, cosFactor: float) -> 'PoissonSeriesParser':
        """
        Set up columns of the sine and cosine coefficients.
        
        Parameters:
            degree (int): degree to set up
            sinColumn (int): column of the sine coefficient for t :sup:`degree` counting from 1 (may be -1 if there are no sine coefficients)
            sinFactor (double): multiplicative factor for the sine coefficient
            cosColumn (int): column of the cosine coefficient for t :sup:`degree` counting from 1 (may be -1 if there are no cosine coefficients)
            cosFactor (double): multiplicative factor for the cosine coefficient
        
        Returns:
            a new parser, with updated columns settings
        
        
        """
        ...

class PolynomialNutation(java.io.Serializable):
    """
    Polynomial nutation function.
    
    Also see:
        PoissonSeries, serialized
    """
    def __init__(self, *coefficients: float):
        """
        Build a polynomial from its coefficients.
        
        Parameters:
            coefficients (double...): polynomial coefficients in increasing degree
        
        
        """
        ...
    _derivative_1__T = typing.TypeVar('_derivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def derivative(self, tc: float) -> float:
        """
        Evaluate the time derivative of the polynomial.
        
        Parameters:
            tc (double): date offset in Julian centuries
        
        Returns:
            time derivative of the polynomial
        
        """
        ...
    @typing.overload
    def derivative(self, tc: _derivative_1__T) -> _derivative_1__T:
        """
        Evaluate the time derivative of the polynomial.
        
        Parameters:
            tc (T): date offset in Julian centuries
        
        Returns:
            time derivative of the polynomial
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, tc: float) -> float:
        """
        Evaluate the value of the polynomial.
        
        Parameters:
            tc (double): date offset in Julian centuries
        
        Returns:
            value of the polynomial
        
        """
        ...
    @typing.overload
    def value(self, tc: _value_1__T) -> _value_1__T:
        """
        Evaluate the value of the polynomial.
        
        Parameters:
            tc (T): date offset in Julian centuries
        
        Returns:
            value of the polynomial
        
        
        """
        ...

class PolynomialParser:
    """
    Parser for polynomials in IERS tables.
    
    IERS conventions tables display polynomial parts using several different formats, like the following ones:
    
      - 125.04455501° − 6962890.5431″t + 7.4722″t² + 0.007702″t³ − 0.00005939″t⁴
      - 0.02438175 × t + 0.00000538691 × t²
      - 0''.014506 + 4612''.15739966t + 1''.39667721t^2 - 0''.00009344t^3 + 0''.00001882t^4
      - -16616.99 + 2004191742.88 t - 427219.05 t^2 - 198620.54 t^3 - 46.05 t^4 + 5.98 t^5
    
    This class parses all these formats and returns the coefficients.
    
    Also see:
        SeriesTerm, PoissonSeries, BodiesElements
    """
    def __init__(self, freeVariable: str, defaultUnit: 'PolynomialParser.Unit'):
        """
        Simple constructor.
        
        Parameters:
            freeVariable (char): name of the free variable
            defaultUnit (Unit): unit to use if no unit found while parsing
        
        
        """
        ...
    def parse(self, expression: str) -> typing.MutableSequence[float]:
        """
        Parse a polynomial expression.
        
        Parameters:
            expression (String): polynomial expression to parse
        
        Returns:
            polynomial coefficients array in increasing degree order, or null if expression is not a recognized polynomial
        
        
        """
        ...
    class Unit(java.lang.Enum['PolynomialParser.Unit']):
        RADIANS: typing.ClassVar['PolynomialParser.Unit'] = ...
        DEGREES: typing.ClassVar['PolynomialParser.Unit'] = ...
        ARC_SECONDS: typing.ClassVar['PolynomialParser.Unit'] = ...
        MILLI_ARC_SECONDS: typing.ClassVar['PolynomialParser.Unit'] = ...
        MICRO_ARC_SECONDS: typing.ClassVar['PolynomialParser.Unit'] = ...
        NO_UNITS: typing.ClassVar['PolynomialParser.Unit'] = ...
        def toSI(self, double: float) -> float: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'PolynomialParser.Unit': ...
        @staticmethod
        def values() -> typing.MutableSequence['PolynomialParser.Unit']: ...

_SimpleTimeStampedTableParser__RowConverter__S = typing.TypeVar('_SimpleTimeStampedTableParser__RowConverter__S', bound=org.orekit.time.TimeStamped)  # <S>
_SimpleTimeStampedTableParser__T = typing.TypeVar('_SimpleTimeStampedTableParser__T', bound=org.orekit.time.TimeStamped)  # <T>
class SimpleTimeStampedTableParser(typing.Generic[_SimpleTimeStampedTableParser__T]):
    """
    Parser for simple tables containing TimeStamped data.
    
    Since:
        6.1
    """
    def __init__(self, columns: int, converter: typing.Union['SimpleTimeStampedTableParser.RowConverter'[_SimpleTimeStampedTableParser__T], typing.Callable[[typing.MutableSequence[float]], _SimpleTimeStampedTableParser__T]]):
        """
        Simple constructor.
        
        Parameters:
            columns (int): number of columns
            converter (RowConverter<SimpleTimeStampedTableParser> converter): converter for rows
        
        
        """
        ...
    def parse(self, stream: java.io.InputStream, name: str) -> java.util.List[_SimpleTimeStampedTableParser__T]:
        """
        Parse a stream.
        
        Parameters:
            stream (InputStream): stream containing the table
            name (String): name of the resource file (for error messages only)
        
        Returns:
            parsed table
        
        
        """
        ...
    class RowConverter(typing.Generic[_SimpleTimeStampedTableParser__RowConverter__S]):
        def convert(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> _SimpleTimeStampedTableParser__RowConverter__S: ...

class SeriesTerm: ...

_AbstractListCrawler__T = typing.TypeVar('_AbstractListCrawler__T')  # <T>
class AbstractListCrawler(DataProvider, typing.Generic[_AbstractListCrawler__T]):
    """
    Provider for data files defined in a list.
    
    All addFilter DataFilter are applied.
    
    Zip archives entries are supported recursively.
    
    Since:
        10.1
    
    Also see:
        DataProvidersManager, NetworkCrawler,
        FilesListCrawler
    """
    def addInput(self, input: _AbstractListCrawler__T) -> None:
        """
        Add an input to the supported list.
        
        Parameters:
            input (AbstractListCrawler): input to add
        
        
        """
        ...
    def feed(self, supported: java.util.regex.Pattern, visitor: DataLoader, manager: DataProvidersManager) -> bool:
        """
        Feed a data file loader by browsing the data collection.
        
        The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file supported by the file loader it asks the file loader to load it.
        
        If the method completes without exception, then the data loader is considered to have been fed successfully and the top level DataProvidersManager will return immediately without attempting to use the next configured providers.
        
        If the method completes abruptly with an exception, then the top level DataProvidersManager will try to use the next configured providers, in case another one can feed the DataLoader.
        
        Specified by: feed in interface DataProvider
        
        Parameters:
            supported (Pattern): pattern for file names supported by the visitor
            visitor (DataLoader): data file visitor to use
            manager (DataProvidersManager): with the filters to apply to the resources.
        
        Returns:
            true if some data has been loaded
        
        
        """
        ...
    def getInputs(self) -> java.util.List[_AbstractListCrawler__T]:
        """
        Get the list of inputs supported by the instance.
        
        Returns:
            unmodifiable view of the list of inputs supported by the instance
        
        
        """
        ...

class BodiesElements(DelaunayArguments):
    """
    Elements of the bodies having an effect on nutation.
    
    This class is a simple placeholder, it does not provide any processing method.
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, tc: float, gamma: float, gammaDot: float, l: float, lDot: float, lPrime: float, lPrimeDot: float, f: float, fDot: float, d: float, dDot: float, omega: float, omegaDot: float, lMe: float, lMeDot: float, lVe: float, lVeDot: float, lE: float, lEDot: float, lMa: float, lMaDot: float, lJu: float, lJuDot: float, lSa: float, lSaDot: float, lUr: float, lUrDot: float, lNe: float, lNeDot: float, pa: float, paDot: float):
        """
        Simple constructor.
        
        Parameters:
            date (AbsoluteDate): current date
            tc (double): offset in Julian centuries
            gamma (double): tide parameter γ = GMST + π
            gammaDot (double): tide parameter γ = GMST + π time derivative
            l (double): mean anomaly of the Moon
            lDot (double): mean anomaly of the Moon time derivative
            lPrime (double): mean anomaly of the Sun
            lPrimeDot (double): mean anomaly of the Sun time derivative
            f (double): L - Ω where L is the mean longitude of the Moon
            fDot (double): L - Ω where L is the mean longitude of the Moon time derivative
            d (double): mean elongation of the Moon from the Sun
            dDot (double): mean elongation of the Moon from the Sun time derivative
            omega (double): mean longitude of the ascending node of the Moon
            omegaDot (double): mean longitude of the ascending node of the Moon time derivative
            lMe (double): mean Mercury longitude
            lMeDot (double): mean Mercury longitude time derivative
            lVe (double): mean Venus longitude
            lVeDot (double): mean Venus longitude time derivative
            lE (double): mean Earth longitude
            lEDot (double): mean Earth longitude time derivative
            lMa (double): mean Mars longitude
            lMaDot (double): mean Mars longitude time derivative
            lJu (double): mean Jupiter longitude
            lJuDot (double): mean Jupiter longitude time derivative
            lSa (double): mean Saturn longitude
            lSaDot (double): mean Saturn longitude time derivative
            lUr (double): mean Uranus longitude
            lUrDot (double): mean Uranus longitude time derivative
            lNe (double): mean Neptune longitude
            lNeDot (double): mean Neptune longitude time derivative
            pa (double): general accumulated precession in longitude
            paDot (double): general accumulated precession in longitude time derivative
        
        
        """
        ...
    def getLE(self) -> float:
        """
        Get the mean Earth longitude.
        
        Returns:
            mean Earth longitude.
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
        Get the mean Earth longitude time derivative.
        
        Returns:
            mean Earth longitude time derivative.
        
        
        """
        ...
    def getLJu(self) -> float:
        """
        Get the mean Jupiter longitude.
        
        Returns:
            mean Jupiter longitude.
        
        
        """
        ...
    def getLJuDot(self) -> float:
        """
        Get the mean Jupiter longitude time derivative.
        
        Returns:
            mean Jupiter longitude time derivative.
        
        
        """
        ...
    def getLMa(self) -> float:
        """
        Get the mean Mars longitude.
        
        Returns:
            mean Mars longitude.
        
        
        """
        ...
    def getLMaDot(self) -> float:
        """
        Get the mean Mars longitude time derivative.
        
        Returns:
            mean Mars longitude time derivative.
        
        
        """
        ...
    def getLMe(self) -> float:
        """
        Get the mean Mercury longitude.
        
        Returns:
            mean Mercury longitude.
        
        
        """
        ...
    def getLMeDot(self) -> float:
        """
        Get the mean Mercury longitude time derivative.
        
        Returns:
            mean Mercury longitude time derivative.
        
        
        """
        ...
    def getLNe(self) -> float:
        """
        Get the mean Neptune longitude.
        
        Returns:
            mean Neptune longitude.
        
        
        """
        ...
    def getLNeDot(self) -> float:
        """
        Get the mean Neptune longitude time derivative.
        
        Returns:
            mean Neptune longitude time derivative.
        
        
        """
        ...
    def getLSa(self) -> float:
        """
        Get the mean Saturn longitude.
        
        Returns:
            mean Saturn longitude.
        
        
        """
        ...
    def getLSaDot(self) -> float:
        """
        Get the mean Saturn longitude time derivative.
        
        Returns:
            mean Saturn longitude time derivative.
        
        
        """
        ...
    def getLUr(self) -> float:
        """
        Get the mean Uranus longitude.
        
        Returns:
            mean Uranus longitude.
        
        
        """
        ...
    def getLUrDot(self) -> float:
        """
        Get the mean Uranus longitude time derivative.
        
        Returns:
            mean Uranus longitude time derivative.
        
        
        """
        ...
    def getLVe(self) -> float:
        """
        Get the mean Venus longitude.
        
        Returns:
            mean Venus longitude.
        
        
        """
        ...
    def getLVeDot(self) -> float:
        """
        Get the mean Venus longitude time derivative.
        
        Returns:
            mean Venus longitude time derivative.
        
        
        """
        ...
    def getPa(self) -> float:
        """
        Get the general accumulated precession in longitude.
        
        Returns:
            general accumulated precession in longitude.
        
        
        """
        ...
    def getPaDot(self) -> float:
        """
        Get the general accumulated precession in longitude time derivative.
        
        Returns:
            general accumulated precession in longitude time derivative.
        
        
        """
        ...

class ClasspathCrawler(DataProvider):
    """
    Provider for data files stored as resources in the classpath.
    
    This class handles a list of data files or zip/jar archives located in the classpath. Since the classpath is not a tree structure the list elements cannot be whole directories recursively browsed as in DirectoryCrawler, they must be data files or zip/jar archives.
    
    A typical use case is to put all data files in a single zip or jar archive and to build an instance of this class with the single name of this zip/jar archive. Two different instances may be used one for user or project specific data and another one for system-wide or general data.
    
    All addFilter DataFilter are applied.
    
    Zip archives entries are supported recursively.
    
    This is a simple application of the visitor design pattern for list browsing.
    
    Also see:
        DataProvidersManager
    """
    @typing.overload
    def __init__(self, classLoader: java.lang.ClassLoader, *list: str): ...
    @typing.overload
    def __init__(self, *list: str): ...
    def feed(self, supported: java.util.regex.Pattern, visitor: DataLoader, manager: DataProvidersManager) -> bool:
        """
        Feed a data file loader by browsing the data collection.
        
        The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file supported by the file loader it asks the file loader to load it.
        
        If the method completes without exception, then the data loader is considered to have been fed successfully and the top level DataProvidersManager will return immediately without attempting to use the next configured providers.
        
        If the method completes abruptly with an exception, then the top level DataProvidersManager will try to use the next configured providers, in case another one can feed the DataLoader.
        
        Specified by: feed in interface DataProvider
        
        Parameters:
            supported (Pattern): pattern for file names supported by the visitor
            visitor (DataLoader): data file visitor to use
            manager (DataProvidersManager): with the filters to apply to the resources.
        
        Returns:
            true if some data has been loaded
        
        
        """
        ...

class CompositeDataContext(DataContext):
    """
    A simple implementation of DataContext that composes the constituent factories into a data context.
    
    Since:
        10.1
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, frames: org.orekit.frames.Frames, celestialBodies: org.orekit.bodies.CelestialBodies, gravityFields: org.orekit.forces.gravity.potential.GravityFields, geoMagneticFields: org.orekit.models.earth.GeoMagneticFields):
        """
        Simple constructor.
        
        Parameters:
            timeScales (TimeScales): used in this data context.
            frames (Frames): used in this data context.
            celestialBodies (CelestialBodies): used in this data context.
            gravityFields (GravityFields): used in this data context.
            geoMagneticFields (GeoMagneticFields): used in this data context.
        
        
        """
        ...
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies:
        """
        Description copied from interface: getCelestialBodies Get a factory constructing CelestialBodys based on the auxiliary data in this context.
        
        Specified by: getCelestialBodies in interface DataContext
        
        Returns:
            the set of common celestial bodies using this data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.Frames:
        """
        Description copied from interface: getFrames Get a factory constructing Frames based on the auxiliary data in this context.
        
        Specified by: getFrames in interface DataContext
        
        Returns:
            the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields:
        """
        Description copied from interface: getGeoMagneticFields Get a factory constructing GeoMagneticFields based on the auxiliary data in this context.
        
        Specified by: getGeoMagneticFields in interface DataContext
        
        Returns:
            the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields:
        """
        Description copied from interface: getGravityFields Get a factory constructing gravity fields based on the auxiliary data in this context.
        
        Specified by: getGravityFields in interface DataContext
        
        Returns:
            the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
        Description copied from interface: getTimeScales Get a factory for constructing TimeScales based on the auxiliary data in this context.
        
        Specified by: getTimeScales in interface DataContext
        
        Returns:
            the set of common time scales using this data context.
        
        
        """
        ...

class DirectoryCrawler(DataProvider):
    """
    Provider for data files stored in a directories tree on filesystem.
    
    This class handles data files recursively starting from a root directories tree. The organization of files in the directories is free. There may be sub-directories to any level. All sub-directories are browsed and all terminal files are checked for loading.
    
    All addFilter DataFilter are applied.
    
    Zip archives entries are supported recursively.
    
    This is a simple application of the visitor design pattern for directory hierarchy crawling.
    
    Also see:
        DataProvidersManager
    """
    def __init__(self, root: typing.Union[java.io.File, jpype.protocol.SupportsPath]):
        """
        Build a data files crawler.
        
        Parameters:
            root (File): root of the directories tree (must be a directory)
        
        
        """
        ...
    def feed(self, supported: java.util.regex.Pattern, visitor: DataLoader, manager: DataProvidersManager) -> bool:
        """
        Feed a data file loader by browsing the data collection.
        
        The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file supported by the file loader it asks the file loader to load it.
        
        If the method completes without exception, then the data loader is considered to have been fed successfully and the top level DataProvidersManager will return immediately without attempting to use the next configured providers.
        
        If the method completes abruptly with an exception, then the top level DataProvidersManager will try to use the next configured providers, in case another one can feed the DataLoader.
        
        Specified by: feed in interface DataProvider
        
        Parameters:
            supported (Pattern): pattern for file names supported by the visitor
            visitor (DataLoader): data file visitor to use
            manager (DataProvidersManager): with the filters to apply to the resources.
        
        Returns:
            true if some data has been loaded
        
        
        """
        ...

_FieldBodiesElements__T = typing.TypeVar('_FieldBodiesElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBodiesElements(FieldDelaunayArguments[_FieldBodiesElements__T], typing.Generic[_FieldBodiesElements__T]):
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldBodiesElements__T], t: _FieldBodiesElements__T, t2: _FieldBodiesElements__T, t3: _FieldBodiesElements__T, t4: _FieldBodiesElements__T, t5: _FieldBodiesElements__T, t6: _FieldBodiesElements__T, t7: _FieldBodiesElements__T, t8: _FieldBodiesElements__T, t9: _FieldBodiesElements__T, t10: _FieldBodiesElements__T, t11: _FieldBodiesElements__T, t12: _FieldBodiesElements__T, t13: _FieldBodiesElements__T, t14: _FieldBodiesElements__T, t15: _FieldBodiesElements__T, t16: _FieldBodiesElements__T, t17: _FieldBodiesElements__T, t18: _FieldBodiesElements__T, t19: _FieldBodiesElements__T, t20: _FieldBodiesElements__T, t21: _FieldBodiesElements__T, t22: _FieldBodiesElements__T, t23: _FieldBodiesElements__T, t24: _FieldBodiesElements__T, t25: _FieldBodiesElements__T, t26: _FieldBodiesElements__T, t27: _FieldBodiesElements__T, t28: _FieldBodiesElements__T, t29: _FieldBodiesElements__T, t30: _FieldBodiesElements__T, t31: _FieldBodiesElements__T): ...
    def getLE(self) -> _FieldBodiesElements__T: ...
    def getLEDot(self) -> _FieldBodiesElements__T: ...
    def getLJu(self) -> _FieldBodiesElements__T: ...
    def getLJuDot(self) -> _FieldBodiesElements__T: ...
    def getLMa(self) -> _FieldBodiesElements__T: ...
    def getLMaDot(self) -> _FieldBodiesElements__T: ...
    def getLMe(self) -> _FieldBodiesElements__T: ...
    def getLMeDot(self) -> _FieldBodiesElements__T: ...
    def getLNe(self) -> _FieldBodiesElements__T: ...
    def getLNeDot(self) -> _FieldBodiesElements__T: ...
    def getLSa(self) -> _FieldBodiesElements__T: ...
    def getLSaDot(self) -> _FieldBodiesElements__T: ...
    def getLUr(self) -> _FieldBodiesElements__T: ...
    def getLUrDot(self) -> _FieldBodiesElements__T: ...
    def getLVe(self) -> _FieldBodiesElements__T: ...
    def getLVeDot(self) -> _FieldBodiesElements__T: ...
    def getPa(self) -> _FieldBodiesElements__T: ...
    def getPaDot(self) -> _FieldBodiesElements__T: ...

class GzipFilter(DataFilter):
    """
    Filter for gzip compressed data.
    
    Since:
        9.2
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def filter(self, original: DataSource) -> DataSource:
        """
        Filter the data source.
        
        Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
        A filter must never openStreamOnce the DataSource by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it is the upper layer that will decide to open (or not) the returned value and that a DataSource can be opened only once; this is the core principle of lazy-opening provided by DataSource.
        
        Beware that as the DataProvidersManager will attempt to pile all filters in a stack as long as their implementation of this method returns a value different from the original parameter. This implies that the filter, must perform some checks to see if it must be applied or not. If for example there is a need for a deciphering filter to be applied once to all data, then the filter should for example check for a suffix in the getName and create a new filtered DataSource instance only if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering filters being built, until a stack overflow or memory exhaustion exception occurs.
        
        Specified by: filter in interface DataFilter
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            filtered data source, or original if this filter does not apply to this data source
        
        
        """
        ...

class LazyLoadedDataContext(DataContext):
    """
    A data context that aims to match the behavior of Orekit 10.0 regarding auxiliary data. This data context only loads auxiliary data when it is first accessed. It allows data loaders to be added before the data is loaded.
    
    Since:
        10.1
    """
    def __init__(self):
        """
        Create a new data context that only loads auxiliary data when it is first accessed and allows configuration of the auxiliary data sources until then.
        """
        ...
    def getCelestialBodies(self) -> org.orekit.bodies.LazyLoadedCelestialBodies:
        """
        Description copied from interface: getCelestialBodies Get a factory constructing CelestialBodys based on the auxiliary data in this context.
        
        Specified by: getCelestialBodies in interface DataContext
        
        Returns:
            the set of common celestial bodies using this data context.
        
        
        """
        ...
    def getDataProvidersManager(self) -> DataProvidersManager:
        """
        Get the provider of auxiliary data for this data context.
        
        Returns:
            the provider that supplies auxiliary data to all of the other methods of this data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.LazyLoadedFrames:
        """
        Description copied from interface: getFrames Get a factory constructing Frames based on the auxiliary data in this context.
        
        Specified by: getFrames in interface DataContext
        
        Returns:
            the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.LazyLoadedGeoMagneticFields:
        """
        Description copied from interface: getGeoMagneticFields Get a factory constructing GeoMagneticFields based on the auxiliary data in this context.
        
        Specified by: getGeoMagneticFields in interface DataContext
        
        Returns:
            the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.LazyLoadedGravityFields:
        """
        Description copied from interface: getGravityFields Get a factory constructing gravity fields based on the auxiliary data in this context.
        
        Specified by: getGravityFields in interface DataContext
        
        Returns:
            the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.LazyLoadedTimeScales:
        """
        Description copied from interface: getTimeScales Get a factory for constructing TimeScales based on the auxiliary data in this context.
        
        Specified by: getTimeScales in interface DataContext
        
        Returns:
            the set of common time scales using this data context.
        
        
        """
        ...

class PythonAbstractSelfFeedingLoader(AbstractSelfFeedingLoader):
    def __init__(self, supportedNames: str, manager: DataProvidersManager):
        """
        Create an abstract data loader that can feed itself.
        
        Parameters:
            supportedNames (String): regular expression. See feed.
            manager (DataProvidersManager): the source of auxiliary data files.
        
        
        """
        ...
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

class PythonDataContext(DataContext):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies:
        """
        Get a factory constructing CelestialBodys based on the auxiliary data in this context.
        
        Specified by: getCelestialBodies in interface DataContext
        
        Returns:
            the set of common celestial bodies using this data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.Frames:
        """
        Get a factory constructing Frames based on the auxiliary data in this context.
        
        Specified by: getFrames in interface DataContext
        
        Returns:
            the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields:
        """
        Get a factory constructing GeoMagneticFields based on the auxiliary data in this context.
        
        Specified by: getGeoMagneticFields in interface DataContext
        
        Returns:
            the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields:
        """
        Get a factory constructing gravity fields based on the auxiliary data in this context.
        
        Specified by: getGravityFields in interface DataContext
        
        Returns:
            the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
        Get a factory for constructing TimeScales based on the auxiliary data in this context.
        
        Specified by: getTimeScales in interface DataContext
        
        Returns:
            the set of common time scales using this data context.
        
        
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

class PythonDataFilter(DataFilter):
    def __init__(self): ...
    def filter(self, original: DataSource) -> DataSource:
        """
        Filter the data source.
        
        Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
        A filter must never openStreamOnce the DataSource by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it is the upper layer that will decide to open (or not) the returned value and that a DataSource can be opened only once; this is the core principle of lazy-opening provided by DataSource.
        
        Beware that as the DataProvidersManager will attempt to pile all filters in a stack as long as their implementation of this method returns a value different from the original parameter. This implies that the filter, must perform some checks to see if it must be applied or not. If for example there is a need for a deciphering filter to be applied once to all data, then the filter should for example check for a suffix in the getName and create a new filtered DataSource instance only if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering filters being built, until a stack overflow or memory exhaustion exception occurs.
        
        Specified by: filter in interface DataFilter
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            filtered data source, or original if this filter does not apply to this data source
        
        Raises:
            IOException: if filtered stream cannot be created
        
        
        """
        ...
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

class PythonDataLoader(DataLoader):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream. Extension point for Python.
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
        
        
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
    def stillAcceptsData(self) -> bool:
        """
        Check if the loader still accepts new data. Extension point for Python.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
        Returns:
            true while the loader still accepts new data
        
        
        """
        ...

class PythonDataProvider(DataProvider):
    def __init__(self): ...
    def feed(self, supported: java.util.regex.Pattern, visitor: DataLoader, manager: DataProvidersManager) -> bool:
        """
        Feed a data file loader by browsing the data collection.
        
        The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file supported by the file loader it asks the file loader to load it.
        
        If the method completes without exception, then the data loader is considered to have been fed successfully and the top level DataProvidersManager will return immediately without attempting to use the next configured providers.
        
        If the method completes abruptly with an exception, then the top level DataProvidersManager will try to use the next configured providers, in case another one can feed the DataLoader.
        
        The default implementation will be removed in 11.0. It calls .
        
        Specified by: feed in interface DataProvider
        
        Parameters:
            supported (Pattern): pattern for file names supported by the visitor
            visitor (DataLoader): data file visitor to use
            manager (DataProvidersManager): with the filters to apply to the resources.
        
        Returns:
            true if some data has been loaded
        
        
        """
        ...
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

class PythonLineOrientedFilteringReader(LineOrientedFilteringReader):
    def __init__(self, name: str, input: java.io.Reader):
        """
        Simple constructor.
        
        Parameters:
            name (String): file name
            input (Reader): underlying raw stream
        
        Raises:
            IOException: if first lines cannot be read
        
        
        """
        ...
    def filterLine(self, lineNumber: int, originalLine: str) -> java.lang.CharSequence:
        """
        Filter one line.
        
        Specified by: filterLine in class LineOrientedFilteringReader
        
        Parameters:
            lineNumber (int): line number
            originalLine (String): original line
        
        Returns:
            filtered line
        
        Raises:
            IOException: if line cannot be parsed
        
        
        """
        ...
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

class PythonReaderOpener(DataSource.ReaderOpener):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def openOnce(self) -> java.io.Reader:
        """
        Open the stream once.
        
        Beware that this interface is only intended for lazy opening a stream, i.e. to delay this opening (or not open the stream at all). It is not intended to open the stream several times. Some implementations may fail if an attempt to open a stream several times is made. This is particularly true for network-based streams.
        
        Specified by: openOnce in interface ReaderOpener
        
        Returns:
            opened stream
        
        Raises:
            IOException: if stream cannot be opened
        
        
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

class PythonSeriesTerm(SeriesTerm):
    def __init__(self): ...
    _argument_1__T = typing.TypeVar('_argument_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def argument(self, elements: BodiesElements) -> float:
        """
        Compute the argument for the current date.
        
        Parameters:
            elements (BodiesElements): luni-solar and planetary elements for the current date
        
        Returns:
            current value of the argument
        
        """
        ...
    @typing.overload
    def argument(self, elements: FieldBodiesElements[_argument_1__T]) -> _argument_1__T:
        """
        Compute the argument for the current date.
        
        Parameters:
            elements (FieldBodiesElements<T> elements): luni-solar and planetary elements for the current date
        
        Returns:
            current value of the argument
        
        
        """
        ...
    _argumentDerivative_1__T = typing.TypeVar('_argumentDerivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def argumentDerivative(self, elements: BodiesElements) -> float:
        """
        Compute the time derivative of the argument for the current date.
        
        Parameters:
            elements (BodiesElements): luni-solar and planetary elements for the current date
        
        Returns:
            current time derivative of the argument
        
        """
        ...
    @typing.overload
    def argumentDerivative(self, elements: FieldBodiesElements[_argumentDerivative_1__T]) -> _argumentDerivative_1__T:
        """
        Compute the time derivative of the argument for the current date.
        
        Parameters:
            elements (FieldBodiesElements<T> elements): luni-solar and planetary elements for the current date
        
        Returns:
            current time derivative of the argument
        
        
        """
        ...
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

class PythonStreamOpener(DataSource.StreamOpener):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def openOnce(self) -> java.io.InputStream:
        """
        Open the stream once.
        
        Beware that this interface is only intended for lazy opening a stream, i.e. to delay this opening (or not open the stream at all). It is not intended to open the stream several times. Some implementations may fail if an attempt to open a stream several times is made. This is particularly true for network-based streams.
        
        Specified by: openOnce in interface StreamOpener
        
        Returns:
            opened stream
        
        Raises:
            IOException: if stream cannot be opened
        
        
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

class TruncatingFilter(DataFilter):
    """
    Filter for truncating line-oriented files.
    
    This filter is mainly intended for test purposes, but may also be used to filter out unwanted trailing data in time series for example
    
    Since:
        12.0
    """
    def __init__(self, nbLines: int):
        """
        Simple constructor.
        
        Parameters:
            nbLines (int): number of lines to keep
        
        
        """
        ...
    def filter(self, original: DataSource) -> DataSource:
        """
        Filter the data source.
        
        Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
        A filter must never openStreamOnce the DataSource by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it is the upper layer that will decide to open (or not) the returned value and that a DataSource can be opened only once; this is the core principle of lazy-opening provided by DataSource.
        
        Beware that as the DataProvidersManager will attempt to pile all filters in a stack as long as their implementation of this method returns a value different from the original parameter. This implies that the filter, must perform some checks to see if it must be applied or not. If for example there is a need for a deciphering filter to be applied once to all data, then the filter should for example check for a suffix in the getName and create a new filtered DataSource instance only if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering filters being built, until a stack overflow or memory exhaustion exception occurs.
        
        Specified by: filter in interface DataFilter
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            filtered data source, or original if this filter does not apply to this data source
        
        Raises:
            IOException: if filtered stream cannot be created
        
        
        """
        ...

class UnixCompressFilter(DataFilter):
    """
    Filter for Unix compressed data.
    
    Since:
        9.2
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def filter(self, original: DataSource) -> DataSource:
        """
        Filter the data source.
        
        Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
        A filter must never openStreamOnce the DataSource by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it is the upper layer that will decide to open (or not) the returned value and that a DataSource can be opened only once; this is the core principle of lazy-opening provided by DataSource.
        
        Beware that as the DataProvidersManager will attempt to pile all filters in a stack as long as their implementation of this method returns a value different from the original parameter. This implies that the filter, must perform some checks to see if it must be applied or not. If for example there is a need for a deciphering filter to be applied once to all data, then the filter should for example check for a suffix in the getName and create a new filtered DataSource instance only if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering filters being built, until a stack overflow or memory exhaustion exception occurs.
        
        Specified by: filter in interface DataFilter
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            filtered data source, or original if this filter does not apply to this data source
        
        
        """
        ...

class ZipJarCrawler(DataProvider):
    """
    Helper class for loading data files from a zip/jar archive.
    
    This class browses all entries in a zip/jar archive in filesystem or in classpath.
    
    The organization of entries within the archive is unspecified. All entries are checked in turn. If several entries of the archive are supported by the data loader, all of them will be loaded.
    
    All addFilter DataFilter are applied.
    
    Zip archives entries are supported recursively.
    
    This is a simple application of the visitor design pattern for zip entries browsing.
    
    Also see:
        DataProvidersManager
    """
    @typing.overload
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    @typing.overload
    def __init__(self, classLoader: java.lang.ClassLoader, resource: str): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, uRL: java.net.URL): ...
    def feed(self, supported: java.util.regex.Pattern, visitor: DataLoader, manager: DataProvidersManager) -> bool:
        """
        Feed a data file loader by browsing the data collection.
        
        The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file supported by the file loader it asks the file loader to load it.
        
        If the method completes without exception, then the data loader is considered to have been fed successfully and the top level DataProvidersManager will return immediately without attempting to use the next configured providers.
        
        If the method completes abruptly with an exception, then the top level DataProvidersManager will try to use the next configured providers, in case another one can feed the DataLoader.
        
        Specified by: feed in interface DataProvider
        
        Parameters:
            supported (Pattern): pattern for file names supported by the visitor
            visitor (DataLoader): data file visitor to use
            manager (DataProvidersManager): with the filters to apply to the resources.
        
        Returns:
            true if some data has been loaded
        
        
        """
        ...

class ExceptionalDataContext(LazyLoadedDataContext, DataContext):
    """
    A data context that always throws a runtime exception when it's methods are used. Can be useful for determining if the default data context is used. E.g. setDefault(new ExceptionalDataContext());. The following classes have static fields that are initialized using the default data context:
    
      - AbsoluteDate
    
    
    Since:
        10.1
    
    Also see:
        setDefault
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def getCelestialBodies(self) -> org.orekit.bodies.LazyLoadedCelestialBodies:
        """
        Description copied from interface: getCelestialBodies Get a factory constructing CelestialBodys based on the auxiliary data in this context.
        
        Specified by: getCelestialBodies in interface DataContext
        
        Overrides: getCelestialBodies in class LazyLoadedDataContext
        
        Returns:
            the set of common celestial bodies using this data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.LazyLoadedFrames:
        """
        Description copied from interface: getFrames Get a factory constructing Frames based on the auxiliary data in this context.
        
        Specified by: getFrames in interface DataContext
        
        Overrides: getFrames in class LazyLoadedDataContext
        
        Returns:
            the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.LazyLoadedGeoMagneticFields:
        """
        Description copied from interface: getGeoMagneticFields Get a factory constructing GeoMagneticFields based on the auxiliary data in this context.
        
        Specified by: getGeoMagneticFields in interface DataContext
        
        Overrides: getGeoMagneticFields in class LazyLoadedDataContext
        
        Returns:
            the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.LazyLoadedGravityFields:
        """
        Description copied from interface: getGravityFields Get a factory constructing gravity fields based on the auxiliary data in this context.
        
        Specified by: getGravityFields in interface DataContext
        
        Overrides: getGravityFields in class LazyLoadedDataContext
        
        Returns:
            the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.LazyLoadedTimeScales:
        """
        Description copied from interface: getTimeScales Get a factory for constructing TimeScales based on the auxiliary data in this context.
        
        Specified by: getTimeScales in interface DataContext
        
        Overrides: getTimeScales in class LazyLoadedDataContext
        
        Returns:
            the set of common time scales using this data context.
        
        
        """
        ...

class FilesListCrawler(AbstractListCrawler[java.io.File]):
    """
    Provider for data files in an explicit list.
    
    Zip archives entries are supported recursively.
    
    This is a simple application of the visitor design pattern for list browsing.
    
    Since:
        10.1
    
    Also see:
        DataProvidersManager
    """
    def __init__(self, *inputs: typing.Union[java.io.File, jpype.protocol.SupportsPath]):
        """
        Build a data classpath crawler.
        
        The default timeout is set to 10 seconds.
        
        Parameters:
            inputs (File...): list of input files
        
        
        """
        ...

class NetworkCrawler(AbstractListCrawler[java.net.URL]):
    """
    Provider for data files directly fetched from network.
    
    This class handles a list of URLs pointing to data files or zip/jar on the net. Since the net is not a tree structure the list elements cannot be top elements recursively browsed as in DirectoryCrawler, they must be data files or zip/jar archives.
    
    The files fetched from network can be locally cached on disk. This prevents too frequent network access if the URLs are remote ones (for example original internet URLs).
    
    If the URL points to a remote server (typically on the web) on the other side of a proxy server, you need to configure the networking layer of your application to use the proxy. For a typical authenticating proxy as used in many corporate environments, this can be done as follows using for example the AuthenticatorDialog graphical authenticator class that can be found in the tests directories:
    
    
       System.setProperty("http.proxyHost",     "proxy.your.domain.com");
       System.setProperty("http.proxyPort",     "8080");
       System.setProperty("http.nonProxyHosts", "localhost|*.your.domain.com");
       Authenticator.setDefault(new AuthenticatorDialog());
     
    
    All addFilter DataFilter are applied.
    
    Zip archives entries are supported recursively.
    
    This is a simple application of the visitor design pattern for list browsing.
    
    Also see:
        DataProvidersManager
    """
    def __init__(self, *inputs: java.net.URL):
        """
        Build a data classpath crawler.
        
        The default timeout is set to 10 seconds.
        
        Parameters:
            inputs (URL...): list of input file URLs
        
        
        """
        ...
    def setTimeout(self, timeout: int) -> None:
        """
        Set the timeout for connection.
        
        Parameters:
            timeout (int): connection timeout in milliseconds
        
        
        """
        ...

_PythonAbstractListCrawler__T = typing.TypeVar('_PythonAbstractListCrawler__T')  # <T>
class PythonAbstractListCrawler(AbstractListCrawler[_PythonAbstractListCrawler__T], typing.Generic[_PythonAbstractListCrawler__T]):
    def __init__(self, *inputs: _PythonAbstractListCrawler__T): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBaseName(self, input: _PythonAbstractListCrawler__T) -> str:
        """
        Get the base name of an input.
        
        Specified by: getBaseName in class AbstractListCrawler
        
        Parameters:
            input (PythonAbstractListCrawler): input to consider
        
        Returns:
            base name of the input
        
        
        """
        ...
    def getCompleteName(self, input: _PythonAbstractListCrawler__T) -> str:
        """
        Get the complete name of a input.
        
        Specified by: getCompleteName in class AbstractListCrawler
        
        Parameters:
            input (PythonAbstractListCrawler): input to consider
        
        Returns:
            complete name of the input
        
        
        """
        ...
    def getStream(self, input: _PythonAbstractListCrawler__T) -> java.io.InputStream:
        """
        Get the stream to read from an input.
        
        Specified by: getStream in class AbstractListCrawler
        
        Parameters:
            input (PythonAbstractListCrawler): input to read from
        
        Returns:
            stream to read the content of the input
        
        Raises:
            IOException: if the input cannot be opened for reading
        
        
        """
        ...
    def getZipJarCrawler(self, input: _PythonAbstractListCrawler__T) -> ZipJarCrawler:
        """
        Get a zip/jar crawler for an input.
        
        Specified by: getZipJarCrawler in class AbstractListCrawler
        
        Parameters:
            input (PythonAbstractListCrawler): input to consider
        
        Returns:
            zip/jar crawler for an input
        
        
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.data")``.

    AbstractListCrawler: typing.Type[AbstractListCrawler]
    AbstractSelfFeedingLoader: typing.Type[AbstractSelfFeedingLoader]
    BodiesElements: typing.Type[BodiesElements]
    ClasspathCrawler: typing.Type[ClasspathCrawler]
    CompositeDataContext: typing.Type[CompositeDataContext]
    DataContext: typing.Type[DataContext]
    DataFilter: typing.Type[DataFilter]
    DataLoader: typing.Type[DataLoader]
    DataProvider: typing.Type[DataProvider]
    DataProvidersManager: typing.Type[DataProvidersManager]
    DataSource: typing.Type[DataSource]
    DelaunayArguments: typing.Type[DelaunayArguments]
    DirectoryCrawler: typing.Type[DirectoryCrawler]
    ExceptionalDataContext: typing.Type[ExceptionalDataContext]
    FieldBodiesElements: typing.Type[FieldBodiesElements]
    FieldDelaunayArguments: typing.Type[FieldDelaunayArguments]
    FilesListCrawler: typing.Type[FilesListCrawler]
    FiltersManager: typing.Type[FiltersManager]
    FundamentalNutationArguments: typing.Type[FundamentalNutationArguments]
    GzipFilter: typing.Type[GzipFilter]
    LazyLoadedDataContext: typing.Type[LazyLoadedDataContext]
    LineOrientedFilteringReader: typing.Type[LineOrientedFilteringReader]
    NetworkCrawler: typing.Type[NetworkCrawler]
    PoissonSeries: typing.Type[PoissonSeries]
    PoissonSeriesParser: typing.Type[PoissonSeriesParser]
    PolynomialNutation: typing.Type[PolynomialNutation]
    PolynomialParser: typing.Type[PolynomialParser]
    PythonAbstractListCrawler: typing.Type[PythonAbstractListCrawler]
    PythonAbstractSelfFeedingLoader: typing.Type[PythonAbstractSelfFeedingLoader]
    PythonDataContext: typing.Type[PythonDataContext]
    PythonDataFilter: typing.Type[PythonDataFilter]
    PythonDataLoader: typing.Type[PythonDataLoader]
    PythonDataProvider: typing.Type[PythonDataProvider]
    PythonLineOrientedFilteringReader: typing.Type[PythonLineOrientedFilteringReader]
    PythonReaderOpener: typing.Type[PythonReaderOpener]
    PythonSeriesTerm: typing.Type[PythonSeriesTerm]
    PythonStreamOpener: typing.Type[PythonStreamOpener]
    SeriesTerm: typing.Type[SeriesTerm]
    SimpleTimeStampedTableParser: typing.Type[SimpleTimeStampedTableParser]
    TruncatingFilter: typing.Type[TruncatingFilter]
    UnixCompressFilter: typing.Type[UnixCompressFilter]
    ZipJarCrawler: typing.Type[ZipJarCrawler]
