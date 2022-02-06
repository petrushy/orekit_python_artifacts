import java.io
import java.lang
import java.net
import java.util
import java.util.regex
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
    public abstract class AbstractSelfFeedingLoader extends Object
    
        Abstract class that combines a :class:`~org.orekit.data.DataProvidersManager` with a supported names regular expression
        for :meth:`~org.orekit.data.DataProvidersManager.feed`.
    
        Since:
            10.1
    """
    def __init__(self, string: str, dataProvidersManager: 'DataProvidersManager'): ...

class DataContext:
    """
    public interface DataContext
    
        Provides auxiliary data for portions of the application.
    
        Since:
            10.1
    """
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies:
        """
            Get a factory constructing :class:`~org.orekit.bodies.CelestialBody`s based on the auxiliary data in this context.
        
            Returns:
                the set of common celestial bodies using this data context.
        
        
        """
        ...
    @staticmethod
    def getDefault() -> 'LazyLoadedDataContext': ...
    def getFrames(self) -> org.orekit.frames.Frames:
        """
            Get a factory constructing :class:`~org.orekit.frames.Frame`s based on the auxiliary data in this context.
        
            Returns:
                the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields:
        """
            Get a factory constructing :class:`~org.orekit.models.earth.GeoMagneticField`s based on the auxiliary data in this
            context.
        
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
            Get a factory for constructing :class:`~org.orekit.time.TimeScale`s based on the auxiliary data in this context.
        
            Returns:
                the set of common time scales using this data context.
        
        
        """
        ...
    @staticmethod
    def setDefault(lazyLoadedDataContext: 'LazyLoadedDataContext') -> None:
        """
            Set the default data context that is used to implement Orekit's static factories.
        
            Calling this method will not modify any instances already retrieved from Orekit's static factories. In general this
            method should only be called at application start up before any of the static factories are used.
        
            Parameters:
                context (:class:`~org.orekit.data.LazyLoadedDataContext`): the new data context.
        
            Also see:
                :meth:`~org.orekit.data.DataContext.getDefault`
        
        
        """
        ...

class DataFilter:
    """
    public interface DataFilter
    
        Interface for filtering data (typically uncompressing it) in :class:`~org.orekit.data.DataProvider` before passing it to
        :class:`~org.orekit.data.DataLoader`.
    
        Since:
            9.2
    
        Also see:
            :class:`~org.orekit.data.DataProvider`, :class:`~org.orekit.data.DataLoader`
    """
    def filter(self, dataSource: 'DataSource') -> 'DataSource': ...

class DataLoader:
    """
    public interface DataLoader
    
        Interface for loading data files from :class:`~org.orekit.data.DataProvider`.
    
        Also see:
            :class:`~org.orekit.data.DataProvider`
    """
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def stillAcceptsData(self) -> bool:
        """
            Check if the loader still accepts new data.
        
            This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the
            data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or
            Earth Orientation Parameters that are split among several files), this method should always return true to make sure no
            data is left over.
        
            Returns:
                true while the loader still accepts new data
        
        
        """
        ...

class DataProvider:
    """
    public interface DataProvider
    
        Interface for providing data files to :class:`~org.orekit.data.DataLoader`.
    
        This interface defines a generic way to explore some collection holding data files and load some of them. The collection
        may be a list of resources in the classpath, a directories tree in filesystem, a zip or jar archive, a database, a
        connexion to a remote server ...
    
        The proper way to use this interface is to configure one or more implementations and register them in the
        :class:`~org.orekit.data.DataProvidersManager`, or to let this manager use its default configuration. Once registered,
        they will be used automatically whenever some data needs to be loaded. This allow high level applications developers to
        customize Orekit data loading mechanism and get a tighter integration of the library within their application.
    
        Also see:
            :class:`~org.orekit.data.DataLoader`, :class:`~org.orekit.data.DataProvidersManager`
    """
    ZIP_ARCHIVE_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    """
    static final Pattern ZIP_ARCHIVE_PATTERN
    
        Pattern for name of zip/jar archives.
    
    """
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: 'DataProvidersManager') -> bool:
        """
            Feed a data file loader by browsing the data collection.
        
            The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file
            supported by the file loader it asks the file loader to load it.
        
            If the method completes without exception, then the data loader is considered to have been fed successfully and the top
            level :class:`~org.orekit.data.DataProvidersManager` will return immediately without attempting to use the next
            configured providers.
        
            If the method completes abruptly with an exception, then the top level :class:`~org.orekit.data.DataProvidersManager`
            will try to use the next configured providers, in case another one can feed the :class:`~org.orekit.data.DataLoader`.
        
            Parameters:
                supported (Pattern): pattern for file names supported by the visitor
                visitor (:class:`~org.orekit.data.DataLoader`): data file visitor to use
                manager (:class:`~org.orekit.data.DataProvidersManager`): with the filters to apply to the resources.
        
            Returns:
                true if some data has been loaded
        
        
        """
        ...

class DataProvidersManager:
    """
    public class DataProvidersManager extends Object
    
        This class manages supported :class:`~org.orekit.data.DataProvider`.
    
        This class is the primary point of access for all data loading features. It is used for example to load Earth
        Orientation Parameters used by IERS frames, to load UTC leap seconds used by time scales, to load planetary
        ephemerides...
    
        It is user-customizable: users can add their own data providers at will. This allows them for example to use a database
        or an existing data loading library in order to embed an Orekit enabled application in a global system with its own data
        handling mechanisms. There is no upper limitation on the number of providers, but often each application will use only a
        few.
    
        If the list of providers is empty when attempting to :meth:`~org.orekit.data.DataProvidersManager.feed` a file loader,
        the :meth:`~org.orekit.data.DataProvidersManager.addDefaultProviders` method is called automatically to set up a default
        configuration. This default configuration contains one :class:`~org.orekit.data.DataProvider` for each component of the
        path-like list specified by the java property :code:`orekit.data.path`. See the
        :meth:`~org.orekit.data.DataProvidersManager.feed` method documentation for further details. The default providers
        configuration is *not* set up if the list is not empty. If users want to have both the default providers and additional
        providers, they must call explicitly the :meth:`~org.orekit.data.DataProvidersManager.addDefaultProviders` method.
    
        The default configuration uses a predefined set of :class:`~org.orekit.data.DataFilter` that already handled
        gzip-compressed files (recognized by the :code:`.gz` suffix), Unix-compressed files (recognized by the :code:`.Z`
        suffix) and Hatanaka compressed RINEX files. Users can access the
        :meth:`~org.orekit.data.DataProvidersManager.getFiltersManager` to set up custom filters for handling specific types of
        filters (decompression, deciphering...).
    
        Also see:
            :class:`~org.orekit.data.DirectoryCrawler`, :class:`~org.orekit.data.ClasspathCrawler`
    """
    OREKIT_DATA_PATH: typing.ClassVar[str] = ...
    """
    public static final String OREKIT_DATA_PATH
    
        Name of the property defining the root directories or zip/jar files path for default configuration.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def addDefaultProviders(self) -> None:
        """
            Add the default providers configuration.
        
            The default configuration contains one :class:`~org.orekit.data.DataProvider` for each component of the path-like list
            specified by the java property :code:`orekit.data.path`.
        
            If the property is not set or is null, no data will be available to the library (for example no pole corrections will be
            applied and only predefined UTC steps will be taken into account). No errors will be triggered in this case.
        
            If the property is set, it must contains a list of existing directories or zip/jar archives. One
            :class:`~org.orekit.data.DirectoryCrawler` instance will be set up for each directory and one
            :class:`~org.orekit.data.ZipJarCrawler` instance (configured to look for the archive in the filesystem) will be set up
            for each zip/jar archive. The list elements in the java property are separated using the standard path separator for the
            operating system as returned by null. This standard path separator is ":" on Linux and Unix type systems and ";" on
            Windows types systems.
        
        """
        ...
    def addProvider(self, dataProvider: DataProvider) -> None:
        """
            Add a data provider to the supported list.
        
            Parameters:
                provider (:class:`~org.orekit.data.DataProvider`): data provider to add
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.removeProvider`,
                :meth:`~org.orekit.data.DataProvidersManager.clearProviders`, :meth:`~org.orekit.data.DataProvidersManager.isSupported`,
                :meth:`~org.orekit.data.DataProvidersManager.getProviders`
        
        
        """
        ...
    def clearLoadedDataNames(self) -> None:
        """
            Clear the set of data file names that have been loaded.
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.getLoadedDataNames`
        
        
        """
        ...
    def clearProviders(self) -> None:
        """
            Remove all data providers.
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.addProvider`, :meth:`~org.orekit.data.DataProvidersManager.removeProvider`,
                :meth:`~org.orekit.data.DataProvidersManager.isSupported`, :meth:`~org.orekit.data.DataProvidersManager.getProviders`
        
        
        """
        ...
    def feed(self, string: str, dataLoader: DataLoader) -> bool:
        """
            Feed a data file loader by browsing all data providers.
        
            If this method is called with an empty list of providers, a default providers configuration is set up. This default
            configuration contains only one :class:`~org.orekit.data.DataProvider`: a :class:`~org.orekit.data.DirectoryCrawler`
            instance that loads data from files located somewhere in a directory hierarchy. This default provider is *not* added if
            the list is not empty. If users want to have both the default provider and other providers, they must add it explicitly.
        
            The providers are used in the order in which they were :meth:`~org.orekit.data.DataProvidersManager.addProvider`. As
            soon as one provider is able to feed the data loader, the loop is stopped. If no provider is able to feed the data
            loader, then the last error triggered is thrown.
        
            Parameters:
                supportedNames (String): regular expression for file names supported by the visitor
                loader (:class:`~org.orekit.data.DataLoader`): data loader to use
        
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
        
            The names returned are exactly the ones that were given to the :meth:`~org.orekit.data.DataLoader.loadData` method.
        
            Returns:
                unmodifiable view of the set of data file names that have been loaded
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.feed`, :meth:`~org.orekit.data.DataProvidersManager.clearLoadedDataNames`
        
        
        """
        ...
    def getProviders(self) -> java.util.List[DataProvider]: ...
    def isSupported(self, dataProvider: DataProvider) -> bool:
        """
            Check if some provider is supported.
        
            Parameters:
                provider (:class:`~org.orekit.data.DataProvider`): provider to check
        
            Returns:
                true if the specified provider instance is already in the supported list
        
            Since:
                5.1
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.addProvider`, :meth:`~org.orekit.data.DataProvidersManager.removeProvider`,
                :meth:`~org.orekit.data.DataProvidersManager.clearProviders`, :meth:`~org.orekit.data.DataProvidersManager.getProviders`
        
        
        """
        ...
    def removeProvider(self, dataProvider: DataProvider) -> DataProvider:
        """
            Remove one provider.
        
            Parameters:
                provider (:class:`~org.orekit.data.DataProvider`): provider instance to remove
        
            Returns:
                instance removed (null if the provider was not already present)
        
            Since:
                5.1
        
            Also see:
                :meth:`~org.orekit.data.DataProvidersManager.addProvider`, :meth:`~org.orekit.data.DataProvidersManager.clearProviders`,
                :meth:`~org.orekit.data.DataProvidersManager.isSupported`, :meth:`~org.orekit.data.DataProvidersManager.getProviders`
        
        
        """
        ...
    def resetFiltersToDefault(self) -> None:
        """
            Reset all filters to default.
        
            This method :meth:`~org.orekit.data.FiltersManager.clearFilters` the
            :meth:`~org.orekit.data.DataProvidersManager.getFiltersManager` and then
            :meth:`~org.orekit.data.FiltersManager.addFilter` back the default filters
        
            Since:
                11.0
        
        
        """
        ...

class DataSource:
    """
    public class DataSource extends Object
    
        Container associating a name with a stream or reader that can be opened *lazily*.
    
        This association and the lazy-opening are useful in different cases:
    
          - when :class:`~org.orekit.data.DirectoryCrawler` a directory tree to select data to be loaded by a
            :class:`~org.orekit.data.DataLoader`, the files that are not meaningful for the loader can be ignored and not opened at
            all
          - when :class:`~org.orekit.data.DataFilter` is used, the raw stream can be opened by the filter only if the upper level
            filtered stream is opened
          - when opening a stream for loading the data it provides, the opening and closing actions can be grouped in Orekit
            internal code using a :code:`try with resources` clause so closing is done properly even in case of exception
          - if some pre-reading of the first few bytes or characters are needed to decide how to load data (as in
            :class:`~org.orekit.files.ccsds.utils.lexical.LexicalAnalyzerSelector`), then the stream can be opened, buffered and
            rewound and a fake open method used to return the already open stream so a :code:`try with resources` clause elsewhere
            works properly for closing the stream
    
    
        Beware that the purpose of this class is only to delay this opening (or not open the stream or reader at all), it is
        *not* intended to open the stream several times and *not* intended to open both the binary stream and the characters
        reader. Some implementations may fail if the :meth:`~org.orekit.data.DataSource.getOpener`'s
        :meth:`~org.orekit.data.DataSource.Opener.openStreamOnce` or :meth:`~org.orekit.data.DataSource.Opener.openReaderOnce`
        methods are called several times or are both called separately. This is particularly true for network-based streams.
    
        Since:
            9.2
    
        Also see:
            :class:`~org.orekit.data.DataFilter`
    """
    @typing.overload
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, readerOpener: 'DataSource.ReaderOpener'): ...
    @typing.overload
    def __init__(self, string: str, streamOpener: 'DataSource.StreamOpener'): ...
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

class DelaunayArguments(org.orekit.time.TimeStamped, java.io.Serializable):
    """
    public class DelaunayArguments extends Object implements :class:`~org.orekit.time.TimeStamped`, Serializable
    
        Delaunay arguments used for nutation or tides.
    
        This class is a simple placeholder, it does not provide any processing method.
    
        Since:
            6.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, double13: float): ...
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
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getF(self) -> float:
        """
            Get L - Î© where L is the mean longitude of the Moon.
        
            Returns:
                L - Î©
        
        
        """
        ...
    def getFDot(self) -> float:
        """
            Get L - Î© where L is the mean longitude of the Moon time derivative.
        
            Returns:
                L - Î© time derivative
        
        
        """
        ...
    def getGamma(self) -> float:
        """
            Get the tide parameter Î³ = GMST + Ï€.
        
            Returns:
                tide parameter Î³ = GMST + Ï€
        
        
        """
        ...
    def getGammaDot(self) -> float:
        """
            Get the tide parameter Î³ = GMST + Ï€ time derivative.
        
            Returns:
                tide parameter Î³ = GMST + Ï€ time derivative
        
        
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
    public class FieldDelaunayArguments<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.time.FieldTimeStamped`<T>
    
        Delaunay arguments used for nutation or tides.
    
        This class is a simple placeholder, it does not provide any processing method.
    
        Since:
            6.1
    
        Also see:
            :class:`~org.orekit.data.DelaunayArguments`
    """
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldDelaunayArguments__T], t: _FieldDelaunayArguments__T, t2: _FieldDelaunayArguments__T, t3: _FieldDelaunayArguments__T, t4: _FieldDelaunayArguments__T, t5: _FieldDelaunayArguments__T, t6: _FieldDelaunayArguments__T, t7: _FieldDelaunayArguments__T, t8: _FieldDelaunayArguments__T, t9: _FieldDelaunayArguments__T, t10: _FieldDelaunayArguments__T, t11: _FieldDelaunayArguments__T, t12: _FieldDelaunayArguments__T, t13: _FieldDelaunayArguments__T): ...
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
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldDelaunayArguments__T]: ...
    def getF(self) -> _FieldDelaunayArguments__T:
        """
            Get L - Î© where L is the mean longitude of the Moon.
        
            Returns:
                L - Î©
        
        
        """
        ...
    def getFDot(self) -> _FieldDelaunayArguments__T:
        """
            Get L - Î© where L is the mean longitude of the Moon time derivative.
        
            Returns:
                L - Î© time derivative
        
        
        """
        ...
    def getGamma(self) -> _FieldDelaunayArguments__T:
        """
            Get the tide parameter Î³ = GMST + Ï€.
        
            Returns:
                tide parameter Î³ = GMST + Ï€
        
        
        """
        ...
    def getGammaDot(self) -> _FieldDelaunayArguments__T:
        """
            Get the tide parameter Î³ = GMST + Ï€ time derivative.
        
            Returns:
                tide parameter Î³ = GMST + Ï€ time derivative
        
        
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
    public class FiltersManager extends Object
    
        Manager for :class:`~org.orekit.data.DataFilter`.
    
        This manager holds a set of filters and applies all the relevant ones by building a stack that transforms a raw
        :class:`~org.orekit.data.DataSource` into a processed :class:`~org.orekit.data.DataSource`.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.data.DataSource`, :class:`~org.orekit.data.DataFilter`
    """
    def __init__(self): ...
    def addFilter(self, dataFilter: DataFilter) -> None:
        """
            Add a data filter.
        
            Parameters:
                filter (:class:`~org.orekit.data.DataFilter`): filter to add
        
            Also see:
                :meth:`~org.orekit.data.FiltersManager.applyRelevantFilters`, :meth:`~org.orekit.data.FiltersManager.clearFilters`
        
        
        """
        ...
    def applyRelevantFilters(self, dataSource: DataSource) -> DataSource: ...
    def clearFilters(self) -> None:
        """
            Remove all data filters.
        
            Also see:
                :meth:`~org.orekit.data.FiltersManager.addFilter`
        
        
        """
        ...

class FundamentalNutationArguments(java.io.Serializable):
    """
    public class FundamentalNutationArguments extends Object implements Serializable
    
        Class computing the fundamental arguments for nutation and tides.
    
        The fundamental arguments are split in two sets:
    
          - the Delaunay arguments for Moon and Sun effects
          - the planetary arguments for other planets
    
    
        Also see:
            :code:`SeriesTerm`, :class:`~org.orekit.data.PoissonSeries`, :class:`~org.orekit.data.BodiesElements`,
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, inputStream: java.io.InputStream, string: str): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, inputStream: java.io.InputStream, string: str, timeScales: org.orekit.time.TimeScales): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, list: java.util.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, list: java.util.List[typing.List[float]], timeScales: org.orekit.time.TimeScales): ...
    _evaluateAll_1__T = typing.TypeVar('_evaluateAll_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def evaluateAll(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'BodiesElements':
        """
            Evaluate all fundamental arguments for the current date (Delaunay plus planetary).
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                all fundamental arguments for the current date (Delaunay plus planetary)
        
        """
        ...
    @typing.overload
    def evaluateAll(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_evaluateAll_1__T]) -> 'FieldBodiesElements'[_evaluateAll_1__T]:
        """
            Evaluate all fundamental arguments for the current date (Delaunay plus planetary).
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                all fundamental arguments for the current date (Delaunay plus planetary)
        
        
        """
        ...

class PoissonSeries:
    """
    public class PoissonSeries extends Object
    
        Class representing a Poisson series for nutation or ephemeris computations.
    
        A Poisson series is composed of a time polynomial part and a non-polynomial part which consist in summation series. The
        :code:`series terms` are harmonic functions (combination of sines and cosines) of polynomial *arguments*. The polynomial
        arguments are combinations of luni-solar or planetary :class:`~org.orekit.data.BodiesElements`.
    
        Also see:
            :class:`~org.orekit.data.PoissonSeriesParser`, :code:`SeriesTerm`, :class:`~org.orekit.data.PolynomialNutation`
    """
    def __init__(self, polynomialNutation: 'PolynomialNutation', map: typing.Union[java.util.Map[int, 'SeriesTerm'], typing.Mapping[int, 'SeriesTerm']]): ...
    @staticmethod
    def compile(poissonSeriesArray: typing.List['PoissonSeries']) -> 'PoissonSeries.CompiledSeries': ...
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
    def value(self, bodiesElements: 'BodiesElements') -> float:
        """
            Evaluate the value of the series.
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): bodies elements for nutation
        
            Returns:
                value of the series
        
        """
        ...
    @typing.overload
    def value(self, fieldBodiesElements: 'FieldBodiesElements'[_value_1__T]) -> _value_1__T:
        """
            Evaluate the value of the series.
        
            Parameters:
                elements (:class:`~org.orekit.data.FieldBodiesElements`<T> elements): bodies elements for nutation
        
            Returns:
                value of the series
        
        
        """
        ...
    class CompiledSeries:
        _derivative_1__S = typing.TypeVar('_derivative_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
        @typing.overload
        def derivative(self, bodiesElements: 'BodiesElements') -> typing.List[float]: ...
        @typing.overload
        def derivative(self, fieldBodiesElements: 'FieldBodiesElements'[_derivative_1__S]) -> typing.List[_derivative_1__S]: ...
        _value_1__S = typing.TypeVar('_value_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
        @typing.overload
        def value(self, bodiesElements: 'BodiesElements') -> typing.List[float]: ...
        @typing.overload
        def value(self, fieldBodiesElements: 'FieldBodiesElements'[_value_1__S]) -> typing.List[_value_1__S]: ...

class PoissonSeriesParser:
    """
    public class PoissonSeriesParser extends Object
    
        Parser for :class:`~org.orekit.data.PoissonSeries` files.
    
        A Poisson series is composed of a time polynomial part and a non-polynomial part which consist in summation series. The
        :code:`series terms` are harmonic functions (combination of sines and cosines) of polynomial *arguments*. The polynomial
        arguments are combinations of luni-solar or planetary :class:`~org.orekit.data.BodiesElements`.
    
        The Poisson series files from IERS have various formats, with or without polynomial part, with or without planetary
        components, with or without period column, with terms of increasing degrees either in dedicated columns or in successive
        sections of the file ... This class attempts to read all the commonly found formats, by specifying the columns of
        interest.
    
        The handling of increasing degrees terms (i.e. sin, cos, t sin, t cos, t^2 sin, t^2 cos ...) is done as follows.
    
          - user must specify pairs of columns to be extracted at each line, in increasing degree order
          - negative columns indices correspond to inexistent values that will be replaced by 0.0)
          - file may provide section headers to specify a degree, which is added to the current column degree
    
    
        A file from an old convention, like table 5.1 in IERS conventions 1996, uses separate columns for degree 0 and degree 1,
        and uses only sine for nutation in longitude and cosine for nutation in obliquity. It reads as follows:
    
        .. code-block: java
        
        
         âˆ†Ïˆ = Î£ (Ai+A'it) sin(ARGUMENT), âˆ†Îµ = Î£ (Bi+B'it) cos(ARGUMENT)
        
              MULTIPLIERS OF      PERIOD           LONGITUDE         OBLIQUITY
          l    l'   F    D   Om     days         Ai       A'i       Bi       B'i
        
          0    0    0    0    1   -6798.4    -171996    -174.2    92025      8.9
          0    0    2   -2    2     182.6     -13187      -1.6     5736     -3.1
          0    0    2    0    2      13.7      -2274      -0.2      977     -0.5
          0    0    0    0    2   -3399.2       2062       0.2     -895      0.5
         
    
        In order to parse the nutation in longitude from the previous table, the following settings should be used:
    
          - totalColumns = 10 (see :meth:`~org.orekit.data.PoissonSeriesParser.PoissonSeriesParser`)
          - firstDelaunay = 1 (see :meth:`~org.orekit.data.PoissonSeriesParser.withFirstDelaunay`)
          - no calls to :meth:`~org.orekit.data.PoissonSeriesParser.withFirstPlanetary` as there are no planetary columns in this
            table
          - sinCosColumns = 7, -1 for degree 0 for Ai (see :meth:`~org.orekit.data.PoissonSeriesParser.withSinCos`)
          - sinCosColumns = 8, -1 for degree 1 for A'i (see :meth:`~org.orekit.data.PoissonSeriesParser.withSinCos`)
    
    
        In order to parse the nutation in obliquity from the previous table, the following settings should be used:
    
          - totalColumns = 10 (see :meth:`~org.orekit.data.PoissonSeriesParser.PoissonSeriesParser`)
          - firstDelaunay = 1 (see :meth:`~org.orekit.data.PoissonSeriesParser.withFirstDelaunay`)
          - no calls to :meth:`~org.orekit.data.PoissonSeriesParser.withFirstPlanetary` as there are no planetary columns in this
            table
          - sinCosColumns = -1, 9 for degree 0 for Bi (see :meth:`~org.orekit.data.PoissonSeriesParser.withSinCos`)
          - sinCosColumns = -1, 10 for degree 1 for B'i (see :meth:`~org.orekit.data.PoissonSeriesParser.withSinCos`)
    
    
        A file from a recent convention, like table 5.3a in IERS conventions 2010, uses only two columns for sin and cos, and
        separate degrees in successive sections with dedicated headers. It reads as follows:
    
        .. code-block: java
        
        
         ---------------------------------------------------------------------------------------------------
        
         (unit microarcsecond; cut-off: 0.1 microarcsecond)
         (ARG being for various combination of the fundamental arguments of the nutation theory)
        
           Sum_i[A_i * sin(ARG) + A"_i * cos(ARG)]
        
         + Sum_i[A'_i * sin(ARG) + A"'_i * cos(ARG)] * t           (see Chapter 5, Eq. (35))
        
         The Table below provides the values for A_i and A"_i (j=0) and then A'_i and A"'_i (j=1)
        
         The expressions for the fundamental arguments appearing in columns 4 to 8 (luni-solar part)
         and in columns 9 to 17 (planetary part) are those of the IERS Conventions 2003
        
         ----------------------------------------------------------------------------------------------------------
         j = 0  Number of terms = 1320
         ----------------------------------------------------------------------------------------------------------
             i        A_i             A"_i     l    l'   F    D    Om  L_Me L_Ve  L_E L_Ma  L_J L_Sa  L_U L_Ne  p_A
         ----------------------------------------------------------------------------------------------------------
             1   -17206424.18        3338.60    0    0    0    0    1    0    0    0    0    0    0    0    0    0
             2    -1317091.22       -1369.60    0    0    2   -2    2    0    0    0    0    0    0    0    0    0
             3     -227641.81         279.60    0    0    2    0    2    0    0    0    0    0    0    0    0    0
             4      207455.40         -69.80    0    0    0    0    2    0    0    0    0    0    0    0    0    0
             5      147587.70        1181.70    0    1    0    0    0    0    0    0    0    0    0    0    0    0
        
         ...
        
          1319          -0.10           0.00    0    0    0    0    0    1    0   -3    0    0    0    0    0   -2
          1320          -0.10           0.00    0    0    0    0    0    0    0    1    0    1   -2    0    0    0
        
         --------------------------------------------------------------------------------------------------------------
         j = 1  Number of terms = 38
         --------------------------------------------------------------------------------------------------------------
            i          A'_i            A"'_i    l    l'   F    D   Om L_Me L_Ve  L_E L_Ma  L_J L_Sa  L_U L_Ne  p_A
         --------------------------------------------------------------------------------------------------------------
          1321      -17418.82           2.89    0    0    0    0    1    0    0    0    0    0    0    0    0    0
          1322        -363.71          -1.50    0    1    0    0    0    0    0    0    0    0    0    0    0    0
          1323        -163.84           1.20    0    0    2   -2    2    0    0    0    0    0    0    0    0    0
          1324         122.74           0.20    0    1    2   -2    2    0    0    0    0    0    0    0    0    0
         
    
        In order to parse the nutation in longitude from the previous table, the following settings should be used:
    
          - totalColumns = 17 (see :meth:`~org.orekit.data.PoissonSeriesParser.PoissonSeriesParser`)
          - firstDelaunay = 4 (see :meth:`~org.orekit.data.PoissonSeriesParser.withFirstDelaunay`)
          - firstPlanetary = 9 (see :meth:`~org.orekit.data.PoissonSeriesParser.withFirstPlanetary`)
          - sinCosColumns = 2,3 (we specify only degree 0, so when we read section j = 0 we read degree 0, when we read section j =
            1 we read degree 1, see :meth:`~org.orekit.data.PoissonSeriesParser.withSinCos` ...)
    
    
        A file from a recent convention, like table 6.5a in IERS conventions 2010, contains both Doodson arguments (Ã�â€ž, s, h,
        p, N', ps), Doodson numbers and Delaunay parameters. In this case, the coefficients for the Delaunay parameters must be
        *subtracted* from the Ã�â€ž = GMST + Ã�â‚¬ tide parameter, so the signs in the files must be reversed in order to match
        the Doodson arguments and Doodson numbers. This is done automatically (and consistency is checked) only when the
        :meth:`~org.orekit.data.PoissonSeriesParser.withDoodson` method is called at parser configuration time. Some other files
        use the ÃŽÂ³ = GMST + Ã�â‚¬ tide parameter rather than Doodson Ã�â€ž argument and the coefficients for the Delaunay
        parameters must be *added* to the ÃŽÂ³ parameter, so no sign reversal is performed. In order to avoid ambiguity as the
        two cases are incompatible with each other, trying to add a configuration for Ã�â€ž by calling
        :meth:`~org.orekit.data.PoissonSeriesParser.withDoodson` and to also add a configuration for ÃŽÂ³ by calling
        :meth:`~org.orekit.data.PoissonSeriesParser.withGamma` triggers an exception.
    
        The table 6.5a file also contains a column for the waves names (the Darwin's symbol) which may be empty, so it must be
        identified explicitly by calling :meth:`~org.orekit.data.PoissonSeriesParser.withOptionalColumn`. The 6.5a table reads
        as follows:
    
        .. code-block: java
        
        
         The in-phase (ip) amplitudes (Aâ‚� Î´kfR Hf) and the out-of-phase (op) amplitudes (Aâ‚� Î´kfI Hf)
         of the corrections for frequency dependence of kâ‚‚â‚�â�½â�°â�¾, taking the nominal value kâ‚‚â‚� for the
         diurnal tides as (0.29830 âˆ’ i 0.00144). Units: 10â�»Â¹Â² . The entries for Î´kfR and Î´kfI are in
         units of 10â�»â�µ. Multipliers of the Doodson arguments identifying the tidal terms are given,
         as also those of the Delaunay variables characterizing the nutations produced by these
         terms.
        
         Name   deg/hr    Doodson  Ï„  s  h  p  N' ps   l  l' F  D  Î©  Î´kfR  Î´kfI     Amp.    Amp.
                            No.                                       /10âˆ’5 /10âˆ’5    (ip)    (op)
           2Qâ‚� 12.85429   125,755  1 -3  0  2   0  0   2  0  2  0  2    -29     3    -0.1     0.0
            Ïƒâ‚� 12.92714   127,555  1 -3  2  0   0  0   0  0  2  2  2    -30     3    -0.1     0.0
               13.39645   135,645  1 -2  0  1  -1  0   1  0  2  0  1    -45     5    -0.1     0.0
            Qâ‚� 13.39866   135,655  1 -2  0  1   0  0   1  0  2  0  2    -46     5    -0.7     0.1
            Ï�â‚� 13.47151   137,455  1 -2  2 -1   0  0  -1  0  2  2  2    -49     5    -0.1     0.0
         
    
          - totalColumns = 18 (see :meth:`~org.orekit.data.PoissonSeriesParser.PoissonSeriesParser`)
          - optionalColumn = 1 (see :meth:`~org.orekit.data.PoissonSeriesParser.withOptionalColumn`)
          - firstDoodson, Doodson number = 4, 3 (see :meth:`~org.orekit.data.PoissonSeriesParser.withDoodson`)
          - firstDelaunay = 10 (see :meth:`~org.orekit.data.PoissonSeriesParser.withFirstDelaunay`)
          - sinCosColumns = 17, 18, see :meth:`~org.orekit.data.PoissonSeriesParser.withSinCos` ...)
    
    
        Our parsing algorithm involves adding the section degree from the "j = 0, 1, 2 ..." header to the column degree. A side
        effect of this algorithm is that it is theoretically possible to mix both formats and have for example degree two term
        appear as degree 2 column in section j=0 and as degree 1 column in section j=1 and as degree 0 column in section j=2.
        This case is not expected to be encountered in practice. The real files use either several columns *or* several
        sections, but not both at the same time.
    
        Since:
            6.1
    
        Also see:
            :code:`SeriesTerm`, :class:`~org.orekit.data.PolynomialNutation`
    """
    def __init__(self, int: int): ...
    def parse(self, inputStream: java.io.InputStream, string: str) -> PoissonSeries:
        """
            Parse a stream.
        
            Parameters:
                stream (InputStream): stream containing the IERS table
                name (String): name of the resource file (for error messages only)
        
            Returns:
                parsed Poisson series
        
        
        """
        ...
    def withDoodson(self, int: int, int2: int) -> 'PoissonSeriesParser':
        """
            Set up columns for Doodson multipliers and Doodson number.
        
            Parameters:
                firstMultiplierColumn (int): column of the first Doodson multiplier which corresponds to Ï„ (counting from 1)
                numberColumn (int): column of the Doodson number (counting from 1)
        
            Returns:
                a new parser, with updated columns settings
        
            Also see:
                :meth:`~org.orekit.data.PoissonSeriesParser.withGamma`, :meth:`~org.orekit.data.PoissonSeriesParser.withFirstDelaunay`
        
        
        """
        ...
    def withFirstDelaunay(self, int: int) -> 'PoissonSeriesParser':
        """
            Set up first column of Delaunay multiplier.
        
            Parameters:
                firstColumn (int): column of the first Delaunay multiplier (counting from 1)
        
            Returns:
                a new parser, with updated columns settings
        
        
        """
        ...
    def withFirstPlanetary(self, int: int) -> 'PoissonSeriesParser':
        """
            Set up first column of planetary multiplier.
        
            Parameters:
                firstColumn (int): column of the first planetary multiplier (counting from 1)
        
            Returns:
                a new parser, with updated columns settings
        
        
        """
        ...
    def withGamma(self, int: int) -> 'PoissonSeriesParser':
        """
            Set up column of GMST tide multiplier.
        
            Parameters:
                column (int): column of the GMST tide multiplier (counting from 1)
        
            Returns:
                a new parser, with updated columns settings
        
            Also see:
                :meth:`~org.orekit.data.PoissonSeriesParser.withDoodson`
        
        
        """
        ...
    def withOptionalColumn(self, int: int) -> 'PoissonSeriesParser':
        """
            Set up optional column.
        
            Optional columns typically appears in tides-related files, as some waves have specific names (Ã�â€¡Ã¢â€šï¿½, MÃ¢â€šâ€š,
            ...) and other waves don't have names and hence are replaced by spaces in the corresponding file line.
        
            At most one column may be optional.
        
            Parameters:
                column (int): optional column (counting from 1)
        
            Returns:
                a new parser, with updated columns settings
        
        
        """
        ...
    def withPolynomialPart(self, char: str, unit: 'PolynomialParser.Unit') -> 'PoissonSeriesParser':
        """
            Set up polynomial part parsing.
        
            Parameters:
                freeVariable (char): name of the free variable in the polynomial part
                unit (:class:`~org.orekit.data.PolynomialParser.Unit`): default unit for polynomial, if not explicit within the file
        
            Returns:
                a new parser, with polynomial parser updated
        
        
        """
        ...
    def withSinCos(self, int: int, int2: int, double: float, int3: int, double2: float) -> 'PoissonSeriesParser':
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
    public class PolynomialNutation extends Object implements Serializable
    
        Polynomial nutation function.
    
        Also see:
            :class:`~org.orekit.data.PoissonSeries`, :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.List[float]): ...
    _derivative_1__T = typing.TypeVar('_derivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def derivative(self, double: float) -> float:
        """
            Evaluate the time derivative of the polynomial.
        
            Parameters:
                tc (double): date offset in Julian centuries
        
            Returns:
                time derivative of the polynomial
        
        """
        ...
    @typing.overload
    def derivative(self, t: _derivative_1__T) -> _derivative_1__T:
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
    def value(self, double: float) -> float:
        """
            Evaluate the value of the polynomial.
        
            Parameters:
                tc (double): date offset in Julian centuries
        
            Returns:
                value of the polynomial
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
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
    public class PolynomialParser extends Object
    
        Parser for polynomials in IERS tables.
    
        IERS conventions tables display polynomial parts using several different formats, like the following ones:
    
          - 125.04455501Â° âˆ’ 6962890.5431â€³t + 7.4722â€³tÂ² + 0.007702â€³tÂ³ âˆ’ 0.00005939â€³tâ�´
          - 0.02438175 Ã— t + 0.00000538691 Ã— tÂ²
          - 0''.014506 + 4612''.15739966t + 1''.39667721t^2 - 0''.00009344t^3 + 0''.00001882t^4
          - -16616.99 + 2004191742.88 t - 427219.05 t^2 - 198620.54 t^3 - 46.05 t^4 + 5.98 t^5
    
    
        This class parses all these formats and returns the coefficients.
    
        Also see:
            :code:`SeriesTerm`, :class:`~org.orekit.data.PoissonSeries`, :class:`~org.orekit.data.BodiesElements`
    """
    def __init__(self, char: str, unit: 'PolynomialParser.Unit'): ...
    def parse(self, string: str) -> typing.List[float]:
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
        def values() -> typing.List['PolynomialParser.Unit']: ...

_SimpleTimeStampedTableParser__RowConverter__S = typing.TypeVar('_SimpleTimeStampedTableParser__RowConverter__S', bound=org.orekit.time.TimeStamped)  # <S>
_SimpleTimeStampedTableParser__T = typing.TypeVar('_SimpleTimeStampedTableParser__T', bound=org.orekit.time.TimeStamped)  # <T>
class SimpleTimeStampedTableParser(typing.Generic[_SimpleTimeStampedTableParser__T]):
    """
    public class SimpleTimeStampedTableParser<T extends :class:`~org.orekit.time.TimeStamped`> extends Object
    
        Parser for simple tables containing :class:`~org.orekit.time.TimeStamped` data.
    
        Since:
            6.1
    """
    def __init__(self, int: int, rowConverter: 'SimpleTimeStampedTableParser.RowConverter'[_SimpleTimeStampedTableParser__T]): ...
    def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[_SimpleTimeStampedTableParser__T]: ...
    class RowConverter(typing.Generic[_SimpleTimeStampedTableParser__RowConverter__S]):
        def convert(self, doubleArray: typing.List[float]) -> _SimpleTimeStampedTableParser__RowConverter__S: ...

class SeriesTerm: ...

_AbstractListCrawler__T = typing.TypeVar('_AbstractListCrawler__T')  # <T>
class AbstractListCrawler(DataProvider, typing.Generic[_AbstractListCrawler__T]):
    """
    public abstract class AbstractListCrawler<T> extends Object implements :class:`~org.orekit.data.DataProvider`
    
        Provider for data files defined in a list.
    
        All :meth:`~org.orekit.data.FiltersManager.addFilter` :class:`~org.orekit.data.DataFilter` are applied.
    
        Zip archives entries are supported recursively.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.data.DataProvidersManager`, :class:`~org.orekit.data.NetworkCrawler`,
            :class:`~org.orekit.data.FilesListCrawler`
    """
    def addInput(self, t: _AbstractListCrawler__T) -> None:
        """
            Add an input to the supported list.
        
            Parameters:
                input (:class:`~org.orekit.data.AbstractListCrawler`): input to add
        
        
        """
        ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool:
        """
            Feed a data file loader by browsing the data collection.
        
            The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file
            supported by the file loader it asks the file loader to load it.
        
            If the method completes without exception, then the data loader is considered to have been fed successfully and the top
            level :class:`~org.orekit.data.DataProvidersManager` will return immediately without attempting to use the next
            configured providers.
        
            If the method completes abruptly with an exception, then the top level :class:`~org.orekit.data.DataProvidersManager`
            will try to use the next configured providers, in case another one can feed the :class:`~org.orekit.data.DataLoader`.
        
            Specified by:
                :meth:`~org.orekit.data.DataProvider.feed` in interface :class:`~org.orekit.data.DataProvider`
        
            Parameters:
                supported (Pattern): pattern for file names supported by the visitor
                visitor (:class:`~org.orekit.data.DataLoader`): data file visitor to use
                manager (:class:`~org.orekit.data.DataProvidersManager`): with the filters to apply to the resources.
        
            Returns:
                true if some data has been loaded
        
        
        """
        ...
    def getInputs(self) -> java.util.List[_AbstractListCrawler__T]: ...

class BodiesElements(DelaunayArguments, java.io.Serializable):
    """
    public final class BodiesElements extends :class:`~org.orekit.data.DelaunayArguments` implements Serializable
    
        Elements of the bodies having an effect on nutation.
    
        This class is a simple placeholder, it does not provide any processing method.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, double13: float, double14: float, double15: float, double16: float, double17: float, double18: float, double19: float, double20: float, double21: float, double22: float, double23: float, double24: float, double25: float, double26: float, double27: float, double28: float, double29: float, double30: float, double31: float): ...
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
    public class ClasspathCrawler extends Object implements :class:`~org.orekit.data.DataProvider`
    
        Provider for data files stored as resources in the classpath.
    
        This class handles a list of data files or zip/jar archives located in the classpath. Since the classpath is not a tree
        structure the list elements cannot be whole directories recursively browsed as in
        :class:`~org.orekit.data.DirectoryCrawler`, they must be data files or zip/jar archives.
    
        A typical use case is to put all data files in a single zip or jar archive and to build an instance of this class with
        the single name of this zip/jar archive. Two different instances may be used one for user or project specific data and
        another one for system-wide or general data.
    
        All :meth:`~org.orekit.data.FiltersManager.addFilter` :class:`~org.orekit.data.DataFilter` are applied.
    
        Zip archives entries are supported recursively.
    
        This is a simple application of the :code:`visitor` design pattern for list browsing.
    
        Also see:
            :class:`~org.orekit.data.DataProvidersManager`
    """
    @typing.overload
    def __init__(self, classLoader: java.lang.ClassLoader, stringArray: typing.List[str]): ...
    @typing.overload
    def __init__(self, stringArray: typing.List[str]): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool:
        """
            Feed a data file loader by browsing the data collection.
        
            The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file
            supported by the file loader it asks the file loader to load it.
        
            If the method completes without exception, then the data loader is considered to have been fed successfully and the top
            level :class:`~org.orekit.data.DataProvidersManager` will return immediately without attempting to use the next
            configured providers.
        
            If the method completes abruptly with an exception, then the top level :class:`~org.orekit.data.DataProvidersManager`
            will try to use the next configured providers, in case another one can feed the :class:`~org.orekit.data.DataLoader`.
        
            Specified by:
                :meth:`~org.orekit.data.DataProvider.feed` in interface :class:`~org.orekit.data.DataProvider`
        
            Parameters:
                supported (Pattern): pattern for file names supported by the visitor
                visitor (:class:`~org.orekit.data.DataLoader`): data file visitor to use
                manager (:class:`~org.orekit.data.DataProvidersManager`): with the filters to apply to the resources.
        
            Returns:
                true if some data has been loaded
        
        
        """
        ...

class CompositeDataContext(DataContext):
    """
    public class CompositeDataContext extends Object implements :class:`~org.orekit.data.DataContext`
    
        A simple implementation of :class:`~org.orekit.data.DataContext` that composes the constituent factories into a data
        context.
    
        Since:
            10.1
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, frames: org.orekit.frames.Frames, celestialBodies: org.orekit.bodies.CelestialBodies, gravityFields: org.orekit.forces.gravity.potential.GravityFields, geoMagneticFields: org.orekit.models.earth.GeoMagneticFields): ...
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getCelestialBodies`
            Get a factory constructing :class:`~org.orekit.bodies.CelestialBody`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getCelestialBodies` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the set of common celestial bodies using this data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.Frames:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getFrames`
            Get a factory constructing :class:`~org.orekit.frames.Frame`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getFrames` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getGeoMagneticFields`
            Get a factory constructing :class:`~org.orekit.models.earth.GeoMagneticField`s based on the auxiliary data in this
            context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGeoMagneticFields` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getGravityFields`
            Get a factory constructing gravity fields based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGravityFields` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getTimeScales`
            Get a factory for constructing :class:`~org.orekit.time.TimeScale`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getTimeScales` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the set of common time scales using this data context.
        
        
        """
        ...

class DirectoryCrawler(DataProvider):
    """
    public class DirectoryCrawler extends Object implements :class:`~org.orekit.data.DataProvider`
    
        Provider for data files stored in a directories tree on filesystem.
    
        This class handles data files recursively starting from a root directories tree. The organization of files in the
        directories is free. There may be sub-directories to any level. All sub-directories are browsed and all terminal files
        are checked for loading.
    
        All :meth:`~org.orekit.data.FiltersManager.addFilter` :class:`~org.orekit.data.DataFilter` are applied.
    
        Zip archives entries are supported recursively.
    
        This is a simple application of the :code:`visitor` design pattern for directory hierarchy crawling.
    
        Also see:
            :class:`~org.orekit.data.DataProvidersManager`
    """
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool:
        """
            Feed a data file loader by browsing the data collection.
        
            The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file
            supported by the file loader it asks the file loader to load it.
        
            If the method completes without exception, then the data loader is considered to have been fed successfully and the top
            level :class:`~org.orekit.data.DataProvidersManager` will return immediately without attempting to use the next
            configured providers.
        
            If the method completes abruptly with an exception, then the top level :class:`~org.orekit.data.DataProvidersManager`
            will try to use the next configured providers, in case another one can feed the :class:`~org.orekit.data.DataLoader`.
        
            Specified by:
                :meth:`~org.orekit.data.DataProvider.feed` in interface :class:`~org.orekit.data.DataProvider`
        
            Parameters:
                supported (Pattern): pattern for file names supported by the visitor
                visitor (:class:`~org.orekit.data.DataLoader`): data file visitor to use
                manager (:class:`~org.orekit.data.DataProvidersManager`): with the filters to apply to the resources.
        
            Returns:
                true if some data has been loaded
        
        
        """
        ...

_FieldBodiesElements__T = typing.TypeVar('_FieldBodiesElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBodiesElements(FieldDelaunayArguments[_FieldBodiesElements__T], typing.Generic[_FieldBodiesElements__T]):
    """
    public final class FieldBodiesElements<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.data.FieldDelaunayArguments`<T>
    
        Elements of the bodies having an effect on nutation.
    
        This class is a simple placeholder, it does not provide any processing method.
    
        Since:
            6.1
    
        Also see:
            :class:`~org.orekit.data.BodiesElements`
    """
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldBodiesElements__T], t: _FieldBodiesElements__T, t2: _FieldBodiesElements__T, t3: _FieldBodiesElements__T, t4: _FieldBodiesElements__T, t5: _FieldBodiesElements__T, t6: _FieldBodiesElements__T, t7: _FieldBodiesElements__T, t8: _FieldBodiesElements__T, t9: _FieldBodiesElements__T, t10: _FieldBodiesElements__T, t11: _FieldBodiesElements__T, t12: _FieldBodiesElements__T, t13: _FieldBodiesElements__T, t14: _FieldBodiesElements__T, t15: _FieldBodiesElements__T, t16: _FieldBodiesElements__T, t17: _FieldBodiesElements__T, t18: _FieldBodiesElements__T, t19: _FieldBodiesElements__T, t20: _FieldBodiesElements__T, t21: _FieldBodiesElements__T, t22: _FieldBodiesElements__T, t23: _FieldBodiesElements__T, t24: _FieldBodiesElements__T, t25: _FieldBodiesElements__T, t26: _FieldBodiesElements__T, t27: _FieldBodiesElements__T, t28: _FieldBodiesElements__T, t29: _FieldBodiesElements__T, t30: _FieldBodiesElements__T, t31: _FieldBodiesElements__T): ...
    def getLE(self) -> _FieldBodiesElements__T:
        """
            Get the mean Earth longitude.
        
            Returns:
                mean Earth longitude.
        
        
        """
        ...
    def getLEDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Earth longitude time derivative.
        
            Returns:
                mean Earth longitude time derivative.
        
        
        """
        ...
    def getLJu(self) -> _FieldBodiesElements__T:
        """
            Get the mean Jupiter longitude.
        
            Returns:
                mean Jupiter longitude.
        
        
        """
        ...
    def getLJuDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Jupiter longitude time derivative.
        
            Returns:
                mean Jupiter longitude time derivative.
        
        
        """
        ...
    def getLMa(self) -> _FieldBodiesElements__T:
        """
            Get the mean Mars longitude.
        
            Returns:
                mean Mars longitude.
        
        
        """
        ...
    def getLMaDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Mars longitude time derivative.
        
            Returns:
                mean Mars longitude time derivative.
        
        
        """
        ...
    def getLMe(self) -> _FieldBodiesElements__T:
        """
            Get the mean Mercury longitude.
        
            Returns:
                mean Mercury longitude.
        
        
        """
        ...
    def getLMeDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Mercury longitude time derivative.
        
            Returns:
                mean Mercury longitude time derivative.
        
        
        """
        ...
    def getLNe(self) -> _FieldBodiesElements__T:
        """
            Get the mean Neptune longitude.
        
            Returns:
                mean Neptune longitude.
        
        
        """
        ...
    def getLNeDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Neptune longitude time derivative.
        
            Returns:
                mean Neptune longitude time derivative.
        
        
        """
        ...
    def getLSa(self) -> _FieldBodiesElements__T:
        """
            Get the mean Saturn longitude.
        
            Returns:
                mean Saturn longitude.
        
        
        """
        ...
    def getLSaDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Saturn longitude time derivative.
        
            Returns:
                mean Saturn longitude time derivative.
        
        
        """
        ...
    def getLUr(self) -> _FieldBodiesElements__T:
        """
            Get the mean Uranus longitude.
        
            Returns:
                mean Uranus longitude.
        
        
        """
        ...
    def getLUrDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Uranus longitude time derivative.
        
            Returns:
                mean Uranus longitude time derivative.
        
        
        """
        ...
    def getLVe(self) -> _FieldBodiesElements__T:
        """
            Get the mean Venus longitude.
        
            Returns:
                mean Venus longitude.
        
        
        """
        ...
    def getLVeDot(self) -> _FieldBodiesElements__T:
        """
            Get the mean Venus longitude time derivative.
        
            Returns:
                mean Venus longitude time derivative.
        
        
        """
        ...
    def getPa(self) -> _FieldBodiesElements__T:
        """
            Get the general accumulated precession in longitude.
        
            Returns:
                general accumulated precession in longitude.
        
        
        """
        ...
    def getPaDot(self) -> _FieldBodiesElements__T:
        """
            Get the general accumulated precession in longitude time derivative.
        
            Returns:
                general accumulated precession in longitude time derivative.
        
        
        """
        ...

class GzipFilter(DataFilter):
    """
    public class GzipFilter extends Object implements :class:`~org.orekit.data.DataFilter`
    
        Filter for gzip compressed data.
    
        Since:
            9.2
    """
    def __init__(self): ...
    def filter(self, dataSource: DataSource) -> DataSource:
        """
            Filter the data source.
        
            Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form
            base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
            A filter must *never* :meth:`~org.orekit.data.DataSource.Opener.openStreamOnce` the :class:`~org.orekit.data.DataSource`
            by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it
            is the upper layer that will decide to open (or not) the returned value and that a :class:`~org.orekit.data.DataSource`
            can be opened only once; this is the core principle of lazy-opening provided by :class:`~org.orekit.data.DataSource`.
        
            Beware that as the :class:`~org.orekit.data.DataProvidersManager` will attempt to pile all filters in a stack as long as
            their implementation of this method returns a value different from the :code:`original` parameter. This implies that the
            filter, *must* perform some checks to see if it must be applied or not. If for example there is a need for a deciphering
            filter to be applied once to all data, then the filter should for example check for a suffix in the
            :meth:`~org.orekit.data.DataSource.getName` and create a new filtered :class:`~org.orekit.data.DataSource` instance
            *only* if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a
            filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering
            filters being built, until a stack overflow or memory exhaustion exception occurs.
        
            Specified by:
                :meth:`~org.orekit.data.DataFilter.filter` in interface :class:`~org.orekit.data.DataFilter`
        
            Parameters:
                original (:class:`~org.orekit.data.DataSource`): original data source
        
            Returns:
                filtered data source, or :code:`original` if this filter does not apply to this data source
        
        
        """
        ...

class LazyLoadedDataContext(DataContext):
    """
    public class LazyLoadedDataContext extends Object implements :class:`~org.orekit.data.DataContext`
    
        A data context that aims to match the behavior of Orekit 10.0 regarding auxiliary data. This data context only loads
        auxiliary data when it is first accessed. It allows data loaders to be added before the data is loaded.
    
        Since:
            10.1
    """
    def __init__(self): ...
    def getCelestialBodies(self) -> org.orekit.bodies.LazyLoadedCelestialBodies:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getCelestialBodies`
            Get a factory constructing :class:`~org.orekit.bodies.CelestialBody`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getCelestialBodies` in interface :class:`~org.orekit.data.DataContext`
        
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
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getFrames`
            Get a factory constructing :class:`~org.orekit.frames.Frame`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getFrames` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.LazyLoadedGeoMagneticFields:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getGeoMagneticFields`
            Get a factory constructing :class:`~org.orekit.models.earth.GeoMagneticField`s based on the auxiliary data in this
            context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGeoMagneticFields` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.LazyLoadedGravityFields:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getGravityFields`
            Get a factory constructing gravity fields based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGravityFields` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.LazyLoadedTimeScales:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getTimeScales`
            Get a factory for constructing :class:`~org.orekit.time.TimeScale`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getTimeScales` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the set of common time scales using this data context.
        
        
        """
        ...

class PythonAbstractSelfFeedingLoader(AbstractSelfFeedingLoader):
    """
    public class PythonAbstractSelfFeedingLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader`
    """
    def __init__(self, string: str, dataProvidersManager: DataProvidersManager): ...

class PythonDataContext(DataContext):
    """
    public class PythonDataContext extends Object implements :class:`~org.orekit.data.DataContext`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies:
        """
            Get a factory constructing :class:`~org.orekit.bodies.CelestialBody`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getCelestialBodies` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the set of common celestial bodies using this data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.Frames:
        """
            Get a factory constructing :class:`~org.orekit.frames.Frame`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getFrames` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields:
        """
            Get a factory constructing :class:`~org.orekit.models.earth.GeoMagneticField`s based on the auxiliary data in this
            context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGeoMagneticFields` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields:
        """
            Get a factory constructing gravity fields based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGravityFields` in interface :class:`~org.orekit.data.DataContext`
        
            Returns:
                the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
            Get a factory for constructing :class:`~org.orekit.time.TimeScale`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getTimeScales` in interface :class:`~org.orekit.data.DataContext`
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class PythonDataFilter(DataFilter):
    """
    public class PythonDataFilter extends Object implements :class:`~org.orekit.data.DataFilter`
    """
    def __init__(self): ...
    def filter(self, dataSource: DataSource) -> DataSource: ...
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

class PythonDataLoader(DataLoader):
    """
    public class PythonDataLoader extends Object implements :class:`~org.orekit.data.DataLoader`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
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
    def stillAcceptsData(self) -> bool:
        """
            Check if the loader still accepts new data. Extension point for Python.
        
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

class PythonDataProvider(DataProvider):
    """
    public class PythonDataProvider extends Object implements :class:`~org.orekit.data.DataProvider`
    """
    def __init__(self): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool:
        """
            Feed a data file loader by browsing the data collection.
        
            The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file
            supported by the file loader it asks the file loader to load it.
        
            If the method completes without exception, then the data loader is considered to have been fed successfully and the top
            level :class:`~org.orekit.data.DataProvidersManager` will return immediately without attempting to use the next
            configured providers.
        
            If the method completes abruptly with an exception, then the top level :class:`~org.orekit.data.DataProvidersManager`
            will try to use the next configured providers, in case another one can feed the :class:`~org.orekit.data.DataLoader`.
        
            The default implementation will be removed in 11.0. It calls :code:`#feed(Pattern, DataLoader)`.
        
            Specified by:
                :meth:`~org.orekit.data.DataProvider.feed` in interface :class:`~org.orekit.data.DataProvider`
        
            Parameters:
                supported (Pattern): pattern for file names supported by the visitor
                visitor (:class:`~org.orekit.data.DataLoader`): data file visitor to use
                manager (:class:`~org.orekit.data.DataProvidersManager`): with the filters to apply to the resources.
        
            Returns:
                true if some data has been loaded
        
        
        """
        ...
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

class PythonSeriesTerm(SeriesTerm):
    """
    public class PythonSeriesTerm extends Object
    """
    def __init__(self): ...
    _argument_1__T = typing.TypeVar('_argument_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def argument(self, bodiesElements: BodiesElements) -> float:
        """
            Compute the argument for the current date.
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): luni-solar and planetary elements for the current date
        
            Returns:
                current value of the argument
        
        """
        ...
    @typing.overload
    def argument(self, fieldBodiesElements: FieldBodiesElements[_argument_1__T]) -> _argument_1__T:
        """
            Compute the argument for the current date.
        
            Parameters:
                elements (:class:`~org.orekit.data.FieldBodiesElements`<T> elements): luni-solar and planetary elements for the current date
        
            Returns:
                current value of the argument
        
        
        """
        ...
    _argumentDerivative_1__T = typing.TypeVar('_argumentDerivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def argumentDerivative(self, bodiesElements: BodiesElements) -> float:
        """
            Compute the time derivative of the argument for the current date.
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): luni-solar and planetary elements for the current date
        
            Returns:
                current time derivative of the argument
        
        """
        ...
    @typing.overload
    def argumentDerivative(self, fieldBodiesElements: FieldBodiesElements[_argumentDerivative_1__T]) -> _argumentDerivative_1__T:
        """
            Compute the time derivative of the argument for the current date.
        
            Parameters:
                elements (:class:`~org.orekit.data.FieldBodiesElements`<T> elements): luni-solar and planetary elements for the current date
        
            Returns:
                current time derivative of the argument
        
        
        """
        ...
    _argumentDerivative_F__T = typing.TypeVar('_argumentDerivative_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def argumentDerivative_F(self, fieldBodiesElements: FieldBodiesElements[_argumentDerivative_F__T]) -> _argumentDerivative_F__T:
        """
            Compute the time derivative of the argument for the current date. Extension point for Python.
        
            Parameters:
                elements (:class:`~org.orekit.data.FieldBodiesElements`<T> elements): luni-solar and planetary elements for the current date
        
            Returns:
                current time derivative of the argument
        
        
        """
        ...
    _argument_F__T = typing.TypeVar('_argument_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def argument_F(self, fieldBodiesElements: FieldBodiesElements[_argument_F__T]) -> _argument_F__T:
        """
            Compute the argument for the current date. Extension point for Python
        
            Parameters:
                elements (:class:`~org.orekit.data.FieldBodiesElements`<T> elements): luni-solar and planetary elements for the current date
        
            Returns:
                current value of the argument
        
        
        """
        ...
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

class UnixCompressFilter(DataFilter):
    """
    public class UnixCompressFilter extends Object implements :class:`~org.orekit.data.DataFilter`
    
        Filter for Unix compressed data.
    
        Since:
            9.2
    """
    def __init__(self): ...
    def filter(self, dataSource: DataSource) -> DataSource:
        """
            Filter the data source.
        
            Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form
            base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
            A filter must *never* :meth:`~org.orekit.data.DataSource.Opener.openStreamOnce` the :class:`~org.orekit.data.DataSource`
            by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it
            is the upper layer that will decide to open (or not) the returned value and that a :class:`~org.orekit.data.DataSource`
            can be opened only once; this is the core principle of lazy-opening provided by :class:`~org.orekit.data.DataSource`.
        
            Beware that as the :class:`~org.orekit.data.DataProvidersManager` will attempt to pile all filters in a stack as long as
            their implementation of this method returns a value different from the :code:`original` parameter. This implies that the
            filter, *must* perform some checks to see if it must be applied or not. If for example there is a need for a deciphering
            filter to be applied once to all data, then the filter should for example check for a suffix in the
            :meth:`~org.orekit.data.DataSource.getName` and create a new filtered :class:`~org.orekit.data.DataSource` instance
            *only* if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a
            filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering
            filters being built, until a stack overflow or memory exhaustion exception occurs.
        
            Specified by:
                :meth:`~org.orekit.data.DataFilter.filter` in interface :class:`~org.orekit.data.DataFilter`
        
            Parameters:
                original (:class:`~org.orekit.data.DataSource`): original data source
        
            Returns:
                filtered data source, or :code:`original` if this filter does not apply to this data source
        
        
        """
        ...

class ZipJarCrawler(DataProvider):
    """
    public class ZipJarCrawler extends Object implements :class:`~org.orekit.data.DataProvider`
    
        Helper class for loading data files from a zip/jar archive.
    
        This class browses all entries in a zip/jar archive in filesystem or in classpath.
    
        The organization of entries within the archive is unspecified. All entries are checked in turn. If several entries of
        the archive are supported by the data loader, all of them will be loaded.
    
        All :meth:`~org.orekit.data.FiltersManager.addFilter` :class:`~org.orekit.data.DataFilter` are applied.
    
        Zip archives entries are supported recursively.
    
        This is a simple application of the :code:`visitor` design pattern for zip entries browsing.
    
        Also see:
            :class:`~org.orekit.data.DataProvidersManager`
    """
    @typing.overload
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    @typing.overload
    def __init__(self, classLoader: java.lang.ClassLoader, string: str): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, uRL: java.net.URL): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool:
        """
            Feed a data file loader by browsing the data collection.
        
            The method crawls all files referenced in the instance (for example all files in a directories tree) and for each file
            supported by the file loader it asks the file loader to load it.
        
            If the method completes without exception, then the data loader is considered to have been fed successfully and the top
            level :class:`~org.orekit.data.DataProvidersManager` will return immediately without attempting to use the next
            configured providers.
        
            If the method completes abruptly with an exception, then the top level :class:`~org.orekit.data.DataProvidersManager`
            will try to use the next configured providers, in case another one can feed the :class:`~org.orekit.data.DataLoader`.
        
            Specified by:
                :meth:`~org.orekit.data.DataProvider.feed` in interface :class:`~org.orekit.data.DataProvider`
        
            Parameters:
                supported (Pattern): pattern for file names supported by the visitor
                visitor (:class:`~org.orekit.data.DataLoader`): data file visitor to use
                manager (:class:`~org.orekit.data.DataProvidersManager`): with the filters to apply to the resources.
        
            Returns:
                true if some data has been loaded
        
        
        """
        ...

class ExceptionalDataContext(LazyLoadedDataContext, DataContext):
    """
    public class ExceptionalDataContext extends :class:`~org.orekit.data.LazyLoadedDataContext` implements :class:`~org.orekit.data.DataContext`
    
        A data context that always throws a runtime exception when it's methods are used. Can be useful for determining if the
        default data context is used. E.g. :code:`DataContext.setDefault(new ExceptionalDataContext());`. The following classes
        have static fields that are initialized using the default data context:
    
          - :class:`~org.orekit.time.AbsoluteDate`
          - :class:`~org.orekit.attitudes.InertialProvider`
    
    
        Since:
            10.1
    
        Also see:
            :meth:`~org.orekit.data.DataContext.setDefault`
    """
    def __init__(self): ...
    def getCelestialBodies(self) -> org.orekit.bodies.LazyLoadedCelestialBodies:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getCelestialBodies`
            Get a factory constructing :class:`~org.orekit.bodies.CelestialBody`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getCelestialBodies` in interface :class:`~org.orekit.data.DataContext`
        
            Overrides:
                :meth:`~org.orekit.data.LazyLoadedDataContext.getCelestialBodies`Â in
                classÂ :class:`~org.orekit.data.LazyLoadedDataContext`
        
            Returns:
                the set of common celestial bodies using this data context.
        
        
        """
        ...
    def getFrames(self) -> org.orekit.frames.LazyLoadedFrames:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getFrames`
            Get a factory constructing :class:`~org.orekit.frames.Frame`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getFrames` in interface :class:`~org.orekit.data.DataContext`
        
            Overrides:
                :meth:`~org.orekit.data.LazyLoadedDataContext.getFrames` in class :class:`~org.orekit.data.LazyLoadedDataContext`
        
            Returns:
                the set of common reference frames using this data context.
        
        
        """
        ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.LazyLoadedGeoMagneticFields:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getGeoMagneticFields`
            Get a factory constructing :class:`~org.orekit.models.earth.GeoMagneticField`s based on the auxiliary data in this
            context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGeoMagneticFields` in interface :class:`~org.orekit.data.DataContext`
        
            Overrides:
                :meth:`~org.orekit.data.LazyLoadedDataContext.getGeoMagneticFields`Â in
                classÂ :class:`~org.orekit.data.LazyLoadedDataContext`
        
            Returns:
                the geomagnetic fields using this data context.
        
        
        """
        ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.LazyLoadedGravityFields:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getGravityFields`
            Get a factory constructing gravity fields based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getGravityFields` in interface :class:`~org.orekit.data.DataContext`
        
            Overrides:
                :meth:`~org.orekit.data.LazyLoadedDataContext.getGravityFields`Â in
                classÂ :class:`~org.orekit.data.LazyLoadedDataContext`
        
            Returns:
                the gravity fields using this data context.
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.LazyLoadedTimeScales:
        """
            Description copied from interface: :meth:`~org.orekit.data.DataContext.getTimeScales`
            Get a factory for constructing :class:`~org.orekit.time.TimeScale`s based on the auxiliary data in this context.
        
            Specified by:
                :meth:`~org.orekit.data.DataContext.getTimeScales` in interface :class:`~org.orekit.data.DataContext`
        
            Overrides:
                :meth:`~org.orekit.data.LazyLoadedDataContext.getTimeScales` in class :class:`~org.orekit.data.LazyLoadedDataContext`
        
            Returns:
                the set of common time scales using this data context.
        
        
        """
        ...

class FilesListCrawler(AbstractListCrawler[java.io.File]):
    """
    public class FilesListCrawler extends :class:`~org.orekit.data.AbstractListCrawler`<File>
    
        Provider for data files in an explicit list.
    
        Zip archives entries are supported recursively.
    
        This is a simple application of the :code:`visitor` design pattern for list browsing.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.data.DataProvidersManager`
    """
    def __init__(self, fileArray: typing.List[java.io.File]): ...

class NetworkCrawler(AbstractListCrawler[java.net.URL]):
    """
    public class NetworkCrawler extends :class:`~org.orekit.data.AbstractListCrawler`<URL>
    
        Provider for data files directly fetched from network.
    
        This class handles a list of URLs pointing to data files or zip/jar on the net. Since the net is not a tree structure
        the list elements cannot be top elements recursively browsed as in :class:`~org.orekit.data.DirectoryCrawler`, they must
        be data files or zip/jar archives.
    
        The files fetched from network can be locally cached on disk. This prevents too frequent network access if the URLs are
        remote ones (for example original internet URLs).
    
        If the URL points to a remote server (typically on the web) on the other side of a proxy server, you need to configure
        the networking layer of your application to use the proxy. For a typical authenticating proxy as used in many corporate
        environments, this can be done as follows using for example the AuthenticatorDialog graphical authenticator class that
        can be found in the tests directories:
    
        .. code-block: java
        
        
           System.setProperty("http.proxyHost",     "proxy.your.domain.com");
           System.setProperty("http.proxyPort",     "8080");
           System.setProperty("http.nonProxyHosts", "localhost|*.your.domain.com");
           Authenticator.setDefault(new AuthenticatorDialog());
         
    
        All :meth:`~org.orekit.data.FiltersManager.addFilter` :class:`~org.orekit.data.DataFilter` are applied.
    
        Zip archives entries are supported recursively.
    
        This is a simple application of the :code:`visitor` design pattern for list browsing.
    
        Also see:
            :class:`~org.orekit.data.DataProvidersManager`
    """
    def __init__(self, uRLArray: typing.List[java.net.URL]): ...
    def setTimeout(self, int: int) -> None:
        """
            Set the timeout for connection.
        
            Parameters:
                timeout (int): connection timeout in milliseconds
        
        
        """
        ...

_PythonAbstractListCrawler__T = typing.TypeVar('_PythonAbstractListCrawler__T')  # <T>
class PythonAbstractListCrawler(AbstractListCrawler[_PythonAbstractListCrawler__T], typing.Generic[_PythonAbstractListCrawler__T]):
    """
    public class PythonAbstractListCrawler<T> extends :class:`~org.orekit.data.AbstractListCrawler`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getBaseName(self, t: _PythonAbstractListCrawler__T) -> str:
        """
            Get the base name of an input.
        
            Specified by:
                :meth:`~org.orekit.data.AbstractListCrawler.getBaseName` in class :class:`~org.orekit.data.AbstractListCrawler`
        
            Parameters:
                input (:class:`~org.orekit.data.PythonAbstractListCrawler`): input to consider
        
            Returns:
                base name of the input
        
        
        """
        ...
    def getCompleteName(self, t: _PythonAbstractListCrawler__T) -> str:
        """
            Get the complete name of a input.
        
            Specified by:
                :meth:`~org.orekit.data.AbstractListCrawler.getCompleteName` in class :class:`~org.orekit.data.AbstractListCrawler`
        
            Parameters:
                input (:class:`~org.orekit.data.PythonAbstractListCrawler`): input to consider
        
            Returns:
                complete name of the input
        
        
        """
        ...
    def getStream(self, t: _PythonAbstractListCrawler__T) -> java.io.InputStream: ...
    def getZipJarCrawler(self, t: _PythonAbstractListCrawler__T) -> ZipJarCrawler:
        """
            Get a zip/jar crawler for an input.
        
            Specified by:
                :meth:`~org.orekit.data.AbstractListCrawler.getZipJarCrawler` in class :class:`~org.orekit.data.AbstractListCrawler`
        
            Parameters:
                input (:class:`~org.orekit.data.PythonAbstractListCrawler`): input to consider
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...


class __module_protocol__(typing.Protocol):
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
    PythonSeriesTerm: typing.Type[PythonSeriesTerm]
    SeriesTerm: typing.Type[SeriesTerm]
    SimpleTimeStampedTableParser: typing.Type[SimpleTimeStampedTableParser]
    UnixCompressFilter: typing.Type[UnixCompressFilter]
    ZipJarCrawler: typing.Type[ZipJarCrawler]
