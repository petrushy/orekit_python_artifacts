import java.io
import java.lang
import java.util
import org.orekit.data
import org.orekit.time
import typing



class AstronomicalAmplitudeReader(org.orekit.data.DataLoader):
    """
    public class AstronomicalAmplitudeReader extends Object implements :class:`~org.orekit.data.DataLoader`
    
        Parser for tides astronomical amplitude H :sub:`f` .
    
        Since:
            6.1
    """
    def __init__(self, string: str, int: int, int2: int, int3: int, double: float): ...
    def getAstronomicalAmplitudesMap(self) -> java.util.Map[int, float]:
        """
            Get astronomical amplitudes map.
        
            Returns:
                an unmodifiable map containing astronomical amplitudes H :sub:`f` from a Doodson number key
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
            Get the regular expression for supported files names.
        
            Returns:
                regular expression for supported files names
        
        
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

class GravityFieldFactory:
    """
    public class GravityFieldFactory extends Object
    
        Factory used to read gravity field files in several supported formats.
    """
    ICGEM_FILENAME: typing.ClassVar[str] = ...
    """
    public static final String ICGEM_FILENAME
    
        Default regular expression for ICGEM files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SHM_FILENAME: typing.ClassVar[str] = ...
    """
    public static final String SHM_FILENAME
    
        Default regular expression for SHM files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM_FILENAME: typing.ClassVar[str] = ...
    """
    public static final String EGM_FILENAME
    
        Default regular expression for EGM files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRGS_FILENAME: typing.ClassVar[str] = ...
    """
    public static final String GRGS_FILENAME
    
        Default regular expression for GRGS files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FES_CNM_SNM_FILENAME: typing.ClassVar[str] = ...
    """
    public static final String FES_CNM_SNM_FILENAME
    
        Default regular expression for FES Cnm, Snm tides files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FES_CHAT_EPSILON_FILENAME: typing.ClassVar[str] = ...
    """
    public static final String FES_CHAT_EPSILON_FILENAME
    
        Default regular expression for FES C hat and epsilon tides files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FES_HF_FILENAME: typing.ClassVar[str] = ...
    """
    public static final String FES_HF_FILENAME
    
        Default regular expression for FES Hf tides files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def addDefaultOceanTidesReaders() -> None: ...
    @staticmethod
    def addDefaultPotentialCoefficientsReaders() -> None: ...
    @staticmethod
    def addOceanTidesReader(oceanTidesReader: 'OceanTidesReader') -> None: ...
    @staticmethod
    def addPotentialCoefficientsReader(potentialCoefficientsReader: 'PotentialCoefficientsReader') -> None: ...
    @staticmethod
    def clearOceanTidesReaders() -> None: ...
    @staticmethod
    def clearPotentialCoefficientsReaders() -> None: ...
    @staticmethod
    def configureOceanLoadDeformationCoefficients(oceanLoadDeformationCoefficients: 'OceanLoadDeformationCoefficients') -> None: ...
    @staticmethod
    def getConstantNormalizedProvider(int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    @staticmethod
    def getConstantUnnormalizedProvider(int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    @staticmethod
    def getGravityFields() -> 'LazyLoadedGravityFields': ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(double: float, double2: float, tideSystem: 'TideSystem', doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> 'NormalizedSphericalHarmonicsProvider':
        """
            Create a time-independent :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider` from
            canonical coefficients.
        
            Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data
        
            Parameters:
                ae (double): central body reference radius
                mu (double): central body attraction coefficient
                tideSystem (:class:`~org.orekit.forces.gravity.potential.TideSystem`): tide system
                normalizedC (double[][]): normalized tesseral-sectorial coefficients (cosine part)
                normalizedS (double[][]): normalized tesseral-sectorial coefficients (sine part)
        
            Returns:
                provider for normalized coefficients
        
            Since:
                6.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(unnormalizedSphericalHarmonicsProvider: 'UnnormalizedSphericalHarmonicsProvider') -> 'NormalizedSphericalHarmonicsProvider':
        """
            Create a :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider` from an
            :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`.
        
            Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data.
        
            Parameters:
                unnormalized (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): provider to normalize
        
            Returns:
                provider for normalized coefficients
        
            Since:
                6.0
        
        
        """
        ...
    @staticmethod
    def getOceanLoadDeformationCoefficients() -> 'OceanLoadDeformationCoefficients': ...
    @staticmethod
    def getOceanTidesWaves(int: int, int2: int) -> java.util.List['OceanTidesWave']: ...
    @staticmethod
    def getUnnormalizationFactors(int: int, int2: int) -> typing.List[typing.List[float]]:
        """
            Get a un-normalization factors array.
        
            Un-normalized coefficients are obtained by multiplying normalized coefficients by the factors array elements.
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                triangular un-normalization factors array
        
            Since:
                6.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getUnnormalizedProvider(double: float, double2: float, tideSystem: 'TideSystem', doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Create a time-independent :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider` from
            canonical coefficients.
        
            Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data
        
            Parameters:
                ae (double): central body reference radius
                mu (double): central body attraction coefficient
                tideSystem (:class:`~org.orekit.forces.gravity.potential.TideSystem`): tide system
                unnormalizedC (double[][]): un-normalized tesseral-sectorial coefficients (cosine part)
                unnormalizedS (double[][]): un-normalized tesseral-sectorial coefficients (sine part)
        
            Returns:
                provider for un-normalized coefficients
        
            Since:
                6.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def getUnnormalizedProvider(int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getUnnormalizedProvider(normalizedSphericalHarmonicsProvider: 'NormalizedSphericalHarmonicsProvider') -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Create an :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider` from a
            :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`.
        
            Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data.
        
            Parameters:
                normalized (:class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`): provider to un-normalize
        
            Returns:
                provider for un-normalized coefficients
        
            Since:
                6.0
        
        
        """
        ...
    @staticmethod
    def readGravityField(int: int, int2: int) -> 'PotentialCoefficientsReader': ...

class GravityFields:
    """
    public interface GravityFields
    
        Defines methods for obtaining gravity fields.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory`
    """
    def getConstantNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
            Get a constant gravity field normalized coefficients provider.
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getNormalizedProvider`
        
        
        """
        ...
    def getConstantUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Get a constant gravity field unnormalized coefficients provider.
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getUnnormalizedProvider`
        
        
        """
        ...
    def getNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
            Get a gravity field normalized coefficients provider.
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantNormalizedProvider`
        
        
        """
        ...
    def getOceanTidesWaves(self, int: int, int2: int) -> java.util.List['OceanTidesWave']: ...
    def getUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Get a gravity field unnormalized coefficients provider.
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantUnnormalizedProvider`
        
        
        """
        ...

class OceanLoadDeformationCoefficients(java.lang.Enum['OceanLoadDeformationCoefficients']):
    """
    public enum OceanLoadDeformationCoefficients extends Enum<:class:`~org.orekit.forces.gravity.potential.OceanLoadDeformationCoefficients`>
    
        Supported Ocean load Deformation coefficients (Love numbers k' :sub:`i` ).
    
        Since:
            6.1
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    IERS_1996: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    IERS_2003: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    IERS_2010: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    GEGOUT: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    def getCoefficients(self) -> typing.List[float]:
        """
            Get the load deformation coefficients for ocean tides.
        
            Returns:
                load deformation coefficients for ocean tides
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OceanLoadDeformationCoefficients':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OceanLoadDeformationCoefficients']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OceanLoadDeformationCoefficients c : OceanLoadDeformationCoefficients.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OceanTidesReader(org.orekit.data.DataLoader):
    """
    public abstract class OceanTidesReader extends Object implements :class:`~org.orekit.data.DataLoader`
    
        Reader for ocean tides coefficients.
    
        Since:
            6.1
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.OceanTidesWave`
    """
    def __init__(self, string: str): ...
    def canAdd(self, int: int, int2: int) -> bool:
        """
            Check if coefficients can be added.
        
            Parameters:
                n (int): degree of the coefficients
                m (int): order of the coefficients
        
            Returns:
                true if coefficients can be added
        
        
        """
        ...
    def getMaxParseDegree(self) -> int:
        """
            Get the degree limit for the next file parsing.
        
            Returns:
                degree limit for the next file parsing
        
        
        """
        ...
    def getMaxParseOrder(self) -> int:
        """
            Get the order limit for the next file parsing.
        
            Returns:
                order limit for the next file parsing
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
            Get the regular expression for supported files names.
        
            Returns:
                regular expression for supported files names
        
        
        """
        ...
    def getWaves(self) -> java.util.List['OceanTidesWave']: ...
    def setMaxParseDegree(self, int: int) -> None:
        """
            Set the degree limit for the next file parsing.
        
            Parameters:
                maxParseDegree (int): maximal degree to parse (may be safely set to null to parse all available coefficients)
        
        
        """
        ...
    def setMaxParseOrder(self, int: int) -> None:
        """
            Set the order limit for the next file parsing.
        
            Parameters:
                maxParseOrder (int): maximal order to parse (may be safely set to null to parse all available coefficients)
        
        
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

class OceanTidesWave:
    """
    public class OceanTidesWave extends Object
    
        Container for ocen tides coefficients for one tide wave.
    
        Since:
            6.1
    
        Also see:
            :class:`~org.orekit.forces.gravity.OceanTides`, :class:`~org.orekit.forces.gravity.potential.OceanTidesReader`
    """
    def __init__(self, int: int, int2: int, int3: int, doubleArray: typing.List[typing.List[typing.List[float]]]): ...
    def addContribution(self, bodiesElements: org.orekit.data.BodiesElements, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> None:
        """
            Add the contribution of the wave to Stokes coefficients.
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): nutation elements
                cnm (double[][]): spherical harmonic cosine coefficients table to add contribution too
                snm (double[][]): spherical harmonic sine coefficients table to add contribution too
        
        
        """
        ...
    def getDoodson(self) -> int:
        """
            Get the Doodson number for the wave.
        
            Returns:
                Doodson number for the wave
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
            Get the maximum supported degree.
        
            Returns:
                maximum supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
            Get the maximum supported order.
        
            Returns:
                maximum supported order
        
        
        """
        ...

class PotentialCoefficientsReader(org.orekit.data.DataLoader):
    """
    public abstract class PotentialCoefficientsReader extends Object implements :class:`~org.orekit.data.DataLoader`
    
        This abstract class represents a Gravitational Potential Coefficients file reader.
    
        As it exits many different coefficients models and containers this interface represents all the methods that should be
        implemented by a reader. The proper way to use this interface is to call the
        :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory` which will determine which reader to use with the
        selected potential coefficients file.
    
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    def getMaxAvailableDegree(self) -> int:
        """
            Get the maximal degree available in the last file parsed.
        
            Returns:
                maximal degree available in the last file parsed
        
            Since:
                6.0
        
        
        """
        ...
    def getMaxAvailableOrder(self) -> int:
        """
            Get the maximal order available in the last file parsed.
        
            Returns:
                maximal order available in the last file parsed
        
            Since:
                6.0
        
        
        """
        ...
    def getMaxParseDegree(self) -> int:
        """
            Get the degree limit for the next file parsing.
        
            Returns:
                degree limit for the next file parsing
        
            Since:
                6.0
        
        
        """
        ...
    def getMaxParseOrder(self) -> int:
        """
            Get the order limit for the next file parsing.
        
            Returns:
                order limit for the next file parsing
        
            Since:
                6.0
        
        
        """
        ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider':
        """
            Get a provider for read spherical harmonics coefficients.
        
            Parameters:
                wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a new provider
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getConstantProvider`
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
            Get the regular expression for supported files names.
        
            Returns:
                regular expression for supported files names
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def missingCoefficientsAllowed(self) -> bool:
        """
            Check if missing coefficients are allowed in the input data.
        
            Returns:
                true if missing coefficients are allowed in the input data
        
        
        """
        ...
    def setMaxParseDegree(self, int: int) -> None:
        """
            Set the degree limit for the next file parsing.
        
            Parameters:
                maxParseDegree (int): maximal degree to parse (may be safely set to null to parse all available coefficients)
        
            Since:
                6.0
        
        
        """
        ...
    def setMaxParseOrder(self, int: int) -> None:
        """
            Set the order limit for the next file parsing.
        
            Parameters:
                maxParseOrder (int): maximal order to parse (may be safely set to null to parse all available coefficients)
        
            Since:
                6.0
        
        
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

class TideSystem(java.lang.Enum['TideSystem']):
    """
    public enum TideSystem extends Enum<:class:`~org.orekit.forces.gravity.potential.TideSystem`>
    
        Enumerate for tie systems.
    
        Tide-systems are used to identify if the permanent tide is already present in the gravity field or if it should be
        handled when computing the solid tides force model.
    
        Since:
            6.0
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
    """
    TIDE_FREE: typing.ClassVar['TideSystem'] = ...
    ZERO_TIDE: typing.ClassVar['TideSystem'] = ...
    UNKNOWN: typing.ClassVar['TideSystem'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TideSystem':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['TideSystem']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TideSystem c : TideSystem.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TideSystemProvider:
    """
    public interface TideSystemProvider
    
        Interface used to provide :class:`~org.orekit.forces.gravity.potential.TideSystem`.
    
        Since:
            6.0
    """
    def getTideSystem(self) -> TideSystem:
        """
            Get the :class:`~org.orekit.forces.gravity.potential.TideSystem` used in the gravity field.
        
            Returns:
                tide system used in the gravity field
        
        
        """
        ...

class EGMFormatReader(PotentialCoefficientsReader):
    """
    public class EGMFormatReader extends :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
    
        This reader is adapted to the EGM Format.
    
        The proper way to use this class is to call the :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory` which
        will determine which reader to use with the selected gravity field file.
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, boolean2: bool): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider':
        """
            Get a provider for read spherical harmonics coefficients.
        
            EGM fields don't include time-dependent parts, so this method returns directly a constant provider.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getProvider`Â in
                classÂ :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
        
            Parameters:
                wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a new provider
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getConstantProvider`
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class FESCHatEpsilonReader(OceanTidesReader):
    """
    public class FESCHatEpsilonReader extends :class:`~org.orekit.forces.gravity.potential.OceanTidesReader`
    
        Reader for ocean tides files following the fes2004.dat format.
    
        Since:
            6.1
    """
    def __init__(self, string: str, double: float, double2: float, oceanLoadDeformationCoefficients: OceanLoadDeformationCoefficients, map: typing.Union[java.util.Map[int, float], typing.Mapping[int, float]]): ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class FESCnmSnmReader(OceanTidesReader):
    """
    public class FESCnmSnmReader extends :class:`~org.orekit.forces.gravity.potential.OceanTidesReader`
    
        Reader for ocean tides files following the fes2004_Cnm-Snm.dat format.
    
        Since:
            6.1
    """
    def __init__(self, string: str, double: float): ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class GRGSFormatReader(PotentialCoefficientsReader):
    """
    public class GRGSFormatReader extends :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
    
        Reader for the GRGS gravity field format.
    
        This format was used to describe various gravity fields at GRGS (Toulouse).
    
        The proper way to use this class is to call the :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory` which
        will determine which reader to use with the selected gravity field file.
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider':
        """
            Get a provider for read spherical harmonics coefficients.
        
            GRGS fields may include time-dependent parts which are taken into account in the returned provider.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getProvider`Â in
                classÂ :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
        
            Parameters:
                wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a new provider
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getConstantProvider`
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class ICGEMFormatReader(PotentialCoefficientsReader):
    """
    public class ICGEMFormatReader extends :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
    
        Reader for the ICGEM gravity field format.
    
        This format is used to describe the gravity field of EIGEN models published by the GFZ Potsdam since 2004. It is
        described in Franz Barthelmes and Christoph FÃ¶rste paper: "the ICGEM-format". The 2006-02-28 version of this paper can
        be found `here <http://op.gfz-potsdam.de/grace/results/grav/g005_ICGEM-Format.pdf>` and the 2011-06-07 version of this
        paper can be found `here <http://icgem.gfz-potsdam.de/ICGEM-Format-2011.pdf>`. These versions differ in time-dependent
        coefficients, which are linear-only prior to 2011 (up to eigen-5 model) and have also harmonic effects after that date
        (starting with eigen-6 model). A third (undocumented as of 2018-05-14) version of the file format also adds a time-span
        for time-dependent coefficients, allowing for piecewise models. All three versions are supported by the class.
    
        This reader uses relaxed check on the gravity constant key so any key ending in gravity_constant is accepted and not
        only earth_gravity_constant as specified in the previous documents. This allows to read also non Earth gravity fields as
        found in `ICGEM - Gravity Field Models of other Celestial Bodies <http://icgem.gfz-potsdam.de/tom_celestial>` page to be
        read.
    
        The proper way to use this class is to call the :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory` which
        will determine which reader to use with the selected gravity field file.
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider':
        """
            Get a provider for read spherical harmonics coefficients.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getProvider`Â in
                classÂ :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
        
            Parameters:
                wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a new provider
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getConstantProvider`
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class LazyLoadedGravityFields(GravityFields):
    """
    public class LazyLoadedGravityFields extends Object implements :class:`~org.orekit.forces.gravity.potential.GravityFields`
    
        Loads gravity fields when first requested and can be configured until then. Designed to match the behavior of
        :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory` in Orekit 10.0.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory`
    """
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    def addDefaultOceanTidesReaders(self) -> None:
        """
            Add the default readers for ocean tides.
        
            The default readers support files similar to the fes2004_Cnm-Snm.dat and fes2004.dat as published by IERS, using the
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.configureOceanLoadDeformationCoefficients` ocean
            load deformation coefficients, which by default are the IERS 2010 coefficients, which are limited to degree 6. If higher
            degree coefficients are needed, the
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.configureOceanLoadDeformationCoefficients` method
            can be called prior to loading the ocean tides model with the
            :meth:`~org.orekit.forces.gravity.potential.OceanLoadDeformationCoefficients.GEGOUT` computed by Pascal GÃƒÂ©gout.
        
            WARNING: the files referenced in the published conventions have some errors. These errors have been corrected and the
            updated files can be found here: ` http://tai.bipm.org/iers/convupdt/convupdt_c6.html
            <http://tai.bipm.org/iers/convupdt/convupdt_c6.html>`.
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.configureOceanLoadDeformationCoefficients`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.getOceanLoadDeformationCoefficients`
        
        
        """
        ...
    def addDefaultPotentialCoefficientsReaders(self) -> None:
        """
            Add the default readers for gravity fields.
        
            The default readers support ICGEM, SHM, EGM and GRGS formats with the default names
            :meth:`~org.orekit.forces.gravity.potential.GravityFieldFactory.ICGEM_FILENAME`,
            :meth:`~org.orekit.forces.gravity.potential.GravityFieldFactory.SHM_FILENAME`,
            :meth:`~org.orekit.forces.gravity.potential.GravityFieldFactory.EGM_FILENAME`,
            :meth:`~org.orekit.forces.gravity.potential.GravityFieldFactory.GRGS_FILENAME` and don't allow missing coefficients.
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders`
        
        
        """
        ...
    def addOceanTidesReader(self, oceanTidesReader: OceanTidesReader) -> None:
        """
            Add a reader for ocean tides.
        
            Parameters:
                reader (:class:`~org.orekit.forces.gravity.potential.OceanTidesReader`): custom reader to add for the gravity field
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders`
        
        
        """
        ...
    def addPotentialCoefficientsReader(self, potentialCoefficientsReader: PotentialCoefficientsReader) -> None:
        """
            Add a reader for gravity fields.
        
            Parameters:
                reader (:class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`): custom reader to add for the gravity field
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders`
        
        
        """
        ...
    def clearOceanTidesReaders(self) -> None:
        """
            Clear ocean tides readers.
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders`
        
        
        """
        ...
    def clearPotentialCoefficientsReaders(self) -> None:
        """
            Clear gravity field readers.
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader`,
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders`
        
        
        """
        ...
    def configureOceanLoadDeformationCoefficients(self, oceanLoadDeformationCoefficients: OceanLoadDeformationCoefficients) -> None:
        """
            Configure ocean load deformation coefficients.
        
            Parameters:
                oldc (:class:`~org.orekit.forces.gravity.potential.OceanLoadDeformationCoefficients`): ocean load deformation coefficients
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.getOceanLoadDeformationCoefficients`
        
        
        """
        ...
    def getConstantNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
            Get a constant gravity field normalized coefficients provider.
        
            If no :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader` has been added by calling
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader` or if
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders` has been called
            afterwards, the
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders` method will
            be called automatically.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantNormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getNormalizedProvider`
        
        
        """
        ...
    def getConstantUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Get a constant gravity field unnormalized coefficients provider.
        
            If no :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader` has been added by calling
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader` or if
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders` has been called
            afterwards, the
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders` method will
            be called automatically.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantUnnormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getUnnormalizedProvider`
        
        
        """
        ...
    def getNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
            Get a gravity field normalized coefficients provider.
        
            If no :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader` has been added by calling
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader` or if
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders` has been called
            afterwards, the
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders` method will
            be called automatically.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getNormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantNormalizedProvider`
        
        
        """
        ...
    def getOceanLoadDeformationCoefficients(self) -> OceanLoadDeformationCoefficients:
        """
            Get the configured ocean load deformation coefficients.
        
            If :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.configureOceanLoadDeformationCoefficients` has
            never been called, the default value will be the
            :meth:`~org.orekit.forces.gravity.potential.OceanLoadDeformationCoefficients.IERS_2010` coefficients.
        
            Returns:
                ocean load deformation coefficients
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.configureOceanLoadDeformationCoefficients`
        
        
        """
        ...
    def getOceanTidesWaves(self, int: int, int2: int) -> java.util.List[OceanTidesWave]: ...
    def getUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Get a gravity field unnormalized coefficients provider.
        
            If no :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader` has been added by calling
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader` or if
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders` has been called
            afterwards, the
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders` method will
            be called automatically.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getUnnormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantUnnormalizedProvider`
        
        
        """
        ...
    def readGravityField(self, int: int, int2: int) -> PotentialCoefficientsReader:
        """
            Read a gravity field coefficients provider from the first supported file.
        
            If no :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader` has been added by calling
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addPotentialCoefficientsReader` or if
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.clearPotentialCoefficientsReaders` has been called
            afterwards, the
            :meth:`~org.orekit.forces.gravity.potential.LazyLoadedGravityFields.addDefaultPotentialCoefficientsReaders` method will
            be called automatically.
        
            Parameters:
                maxParseDegree (int): maximal degree to parse
                maxParseOrder (int): maximal order to parse
        
            Returns:
                a reader containing already loaded data
        
            Since:
                6.0
        
        
        """
        ...

class PythonGravityFields(GravityFields):
    """
    public class PythonGravityFields extends Object implements :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getConstantNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
            Get a constant gravity field normalized coefficients provider.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantNormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PythonGravityFields.getNormalizedProvider`
        
        
        """
        ...
    def getConstantUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Get a constant gravity field unnormalized coefficients provider.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getConstantUnnormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PythonGravityFields.getUnnormalizedProvider`
        
        
        """
        ...
    def getNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
            Get a gravity field normalized coefficients provider.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getNormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PythonGravityFields.getConstantNormalizedProvider`
        
        
        """
        ...
    def getOceanTidesWaves(self, int: int, int2: int) -> java.util.List[OceanTidesWave]: ...
    def getUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
            Get a gravity field unnormalized coefficients provider.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.GravityFields.getUnnormalizedProvider`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.GravityFields`
        
            Parameters:
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a gravity field coefficients provider containing already loaded data
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PythonGravityFields.getConstantUnnormalizedProvider`
        
        
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

class PythonPotentialCoefficientsReader(PotentialCoefficientsReader):
    """
    public class PythonPotentialCoefficientsReader extends :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
    """
    def finalize(self) -> None: ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider':
        """
            Get a provider for read spherical harmonics coefficients.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getProvider`Â in
                classÂ :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
        
            Parameters:
                wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a new provider
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getConstantProvider`
        
        
        """
        ...
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

class PythonTideSystemProvider(TideSystemProvider):
    """
    public class PythonTideSystemProvider extends Object implements :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getTideSystem(self) -> TideSystem:
        """
            Get the :class:`~org.orekit.forces.gravity.potential.TideSystem` used in the gravity field.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.TideSystemProvider.getTideSystem`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
        
            Returns:
                tide system used in the gravity field
        
        
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

class SHMFormatReader(PotentialCoefficientsReader):
    """
    public class SHMFormatReader extends :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
    
        Reader for the SHM gravity field format.
    
        This format was used to describe the gravity field of EIGEN models published by the GFZ Potsdam up to 2003. It was then
        replaced by :class:`~org.orekit.forces.gravity.potential.ICGEMFormatReader`. The SHM format is described in ` Potsdam
        university website <http://op.gfz-potsdam.de/champ/docs_CHAMP/CH-FORMAT-REFLINKS.html>`.
    
        The proper way to use this class is to call the :class:`~org.orekit.forces.gravity.potential.GravityFieldFactory` which
        will determine which reader to use with the selected gravity field file.
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider':
        """
            Get a provider for read spherical harmonics coefficients.
        
            SHM fields do include time-dependent parts which are taken into account in the returned provider.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getProvider`Â in
                classÂ :class:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader`
        
            Parameters:
                wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
                degree (int): maximal degree
                order (int): maximal order
        
            Returns:
                a new provider
        
            Since:
                6.0
        
            Also see:
                :meth:`~org.orekit.forces.gravity.potential.PotentialCoefficientsReader.getConstantProvider`
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class SphericalHarmonicsProvider(TideSystemProvider):
    """
    public interface SphericalHarmonicsProvider extends :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
    
        Interface used to provide spherical harmonics coefficients.
    
        Two interfaces are provided to distinguish between normalized and un-normalized coefficients:
        :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider` and
        :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`. To account for gravity
        pertubations all providers are capable of providing the coefficients on specific dates, using the
        :meth:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider.onDate` methods.
    
        Typical usage when evaluating the geopotential:
    
        .. code-block: java
        
        
             NormalizedSphericalHarmonicsProvider provider = ...;
             NormalizedShpericalHarmonics coeffs = provider.onDate(date);
             double c20 = coeffs.getNormalizedCnm(2, 0);
         
    
        Since:
            6.0
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    def getAe(self) -> float:
        """
            Get the value of the central body reference radius.
        
            Returns:
                ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
            Get the maximal supported degree.
        
            Returns:
                maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
            Get the maximal supported order.
        
            Returns:
                maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central body attraction coefficient.
        
            Returns:
                mu (mÂ³/sÂ²)
        
        
        """
        ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference date for the harmonics.
        
            For piecewise models, the latest reference date is returned.
        
            Returns:
                reference date for the harmonics (may be null if no reference date is defined)
        
        
        """
        ...

class NormalizedSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    """
    public interface NormalizedSphericalHarmonicsProvider extends :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
    
        Interface used to provide normalized spherical harmonics coefficients.
    
        Since:
            6.0
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics':
        """
            Get the normalized spherical harmonic coefficients at a specific instance in time.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): of evaluation
        
            Returns:
                normalized coefficients on :code:`date`.
        
            Since:
                6.1
        
        
        """
        ...
    class NormalizedSphericalHarmonics(org.orekit.time.TimeStamped):
        def getNormalizedCnm(self, int: int, int2: int) -> float: ...
        def getNormalizedSnm(self, int: int, int2: int) -> float: ...

class PythonSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    """
    public class PythonSphericalHarmonicsProvider extends Object implements :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float:
        """
            Get the value of the central body reference radius.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getAe`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
            Get the maximal supported degree.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxDegree`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
            Get the maximal supported order.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxOrder`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central body attraction coefficient.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMu`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                mu (mÂ³/sÂ²)
        
        
        """
        ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the offset from :meth:`~org.orekit.forces.gravity.potential.PythonSphericalHarmonicsProvider.getReferenceDate` for
            the harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getOffset`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                offset between current date and reference date if there is a reference date, or 0.0 if there are no reference dates
                (i.e. if :meth:`~org.orekit.forces.gravity.potential.PythonSphericalHarmonicsProvider.getReferenceDate` returns null)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference date for the harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getReferenceDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                reference date for the harmonics
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
            Get the :class:`~org.orekit.forces.gravity.potential.TideSystem` used in the gravity field.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.TideSystemProvider.getTideSystem`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
        
            Returns:
                tide system used in the gravity field
        
        
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

class RawSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    """
    public interface RawSphericalHarmonicsProvider extends :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
    
        Interface used to provide raw spherical harmonics coefficients.
    
        This interface is intended to be used only as the workhorse for either
        :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider` or
        :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider` implementations.
    
        Since:
            6.0
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'RawSphericalHarmonicsProvider.RawSphericalHarmonics':
        """
            Get the raw spherical harmonic coefficients on a specific date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): to evaluate the spherical harmonics
        
            Returns:
                the raw spherical harmonics on :code:`date`.
        
        
        """
        ...
    class RawSphericalHarmonics(org.orekit.time.TimeStamped):
        def getRawCnm(self, int: int, int2: int) -> float: ...
        def getRawSnm(self, int: int, int2: int) -> float: ...

class UnnormalizedSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    """
    public interface UnnormalizedSphericalHarmonicsProvider extends :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
    
        Interface used to provide un-normalized spherical harmonics coefficients.
    
        Un-normalized spherical harmonics coefficients are fine for small degrees. At high degree and order the un-normalized
        coefficients are not representable in a :code:`double`.
        :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider` is recommended for high precision
        applications.
    
        Since:
            6.0
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.GravityFields`
    """
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics':
        """
            Get the un-normalized spherical harmonic coefficients at a specific instance in time.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): of evaluation (may be null if model is not time-dependent)
        
            Returns:
                un-normalized coefficients on :code:`date`.
        
            Since:
                6.1
        
        
        """
        ...
    class UnnormalizedSphericalHarmonics(org.orekit.time.TimeStamped):
        def getUnnormalizedCnm(self, int: int, int2: int) -> float: ...
        def getUnnormalizedSnm(self, int: int, int2: int) -> float: ...

class CachedNormalizedSphericalHarmonicsProvider(NormalizedSphericalHarmonicsProvider):
    """
    public class CachedNormalizedSphericalHarmonicsProvider extends Object implements :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`
    
        Caching wrapper for :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`.
    
        This wrapper improves efficiency of :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`
        by sampling the values at a user defined rate and using interpolation between samples. This is important with providers
        that have sub-daily frequencies and are computing intensive, such as tides fields.
    
        Since:
            6.1
    
        Also see:
            :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`,
            :class:`~org.orekit.forces.gravity.SolidTides`, :class:`~org.orekit.utils.TimeStampedCache`
    """
    def __init__(self, normalizedSphericalHarmonicsProvider: NormalizedSphericalHarmonicsProvider, double: float, int: int, int2: int, double2: float, double3: float): ...
    def getAe(self) -> float:
        """
            Get the value of the central body reference radius.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getAe`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
            Get the maximal supported degree.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxDegree`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
            Get the maximal supported order.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxOrder`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central body attraction coefficient.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMu`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                mu (mÂ³/sÂ²)
        
        
        """
        ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference date for the harmonics.
        
            For piecewise models, the latest reference date is returned.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getReferenceDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                reference date for the harmonics (may be null if no reference date is defined)
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
            Get the :class:`~org.orekit.forces.gravity.potential.TideSystem` used in the gravity field.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.TideSystemProvider.getTideSystem`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
        
            Returns:
                tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics:
        """
            Get the normalized spherical harmonic coefficients at a specific instance in time.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider.onDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): of evaluation
        
            Returns:
                normalized coefficients on :code:`date`.
        
        
        """
        ...

class PythonNormalizedSphericalHarmonicsProvider(NormalizedSphericalHarmonicsProvider):
    """
    public class PythonNormalizedSphericalHarmonicsProvider extends Object implements :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float:
        """
            Get the value of the central body reference radius.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getAe`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
            Get the maximal supported degree.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxDegree`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
            Get the maximal supported order.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxOrder`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central body attraction coefficient.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMu`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                mu (mÂ³/sÂ²)
        
        
        """
        ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the offset from
            :meth:`~org.orekit.forces.gravity.potential.PythonNormalizedSphericalHarmonicsProvider.getReferenceDate` for the
            harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getOffset`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                offset between current date and reference date if there is a reference date, or 0.0 if there are no reference dates
                (i.e. if :meth:`~org.orekit.forces.gravity.potential.PythonNormalizedSphericalHarmonicsProvider.getReferenceDate`
                returns null)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference date for the harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getReferenceDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                reference date for the harmonics
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
            Get the :class:`~org.orekit.forces.gravity.potential.TideSystem` used in the gravity field.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.TideSystemProvider.getTideSystem`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
        
            Returns:
                tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics:
        """
            Get the normalized spherical harmonic coefficients at a specific instance in time.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider.onDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): of evaluation
        
            Returns:
                normalized coefficients on :code:`date`.
        
            Since:
                6.1
        
        
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

class PythonRawSphericalHarmonicsProvider(RawSphericalHarmonicsProvider):
    """
    public class PythonRawSphericalHarmonicsProvider extends Object implements :class:`~org.orekit.forces.gravity.potential.RawSphericalHarmonicsProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float:
        """
            Get the value of the central body reference radius.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getAe`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
            Get the maximal supported degree.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxDegree`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
            Get the maximal supported order.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxOrder`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central body attraction coefficient.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMu`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                mu (mÂ³/sÂ²)
        
        
        """
        ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the offset from :meth:`~org.orekit.forces.gravity.potential.PythonRawSphericalHarmonicsProvider.getReferenceDate`
            for the harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getOffset`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                offset between current date and reference date if there is a reference date, or 0.0 if there are no reference dates
                (i.e. if :meth:`~org.orekit.forces.gravity.potential.PythonRawSphericalHarmonicsProvider.getReferenceDate` returns null)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference date for the harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getReferenceDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                reference date for the harmonics
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
            Get the :class:`~org.orekit.forces.gravity.potential.TideSystem` used in the gravity field.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.TideSystemProvider.getTideSystem`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
        
            Returns:
                tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> RawSphericalHarmonicsProvider.RawSphericalHarmonics:
        """
            Get the raw spherical harmonic coefficients on a specific date.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.RawSphericalHarmonicsProvider.onDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.RawSphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): to evaluate the spherical harmonics
        
            Returns:
                the raw spherical harmonics on :code:`date`.
        
        
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

class PythonUnnormalizedSphericalHarmonics(UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics):
    """
    public class PythonUnnormalizedSphericalHarmonics extends Object implements :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getUnnormalizedCnm(self, int: int, int2: int) -> float:
        """
            Get a spherical harmonic cosine coefficient.
        
            Specified by:
                
                meth:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics.getUnnormalizedCnm`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`
        
            Parameters:
                n (int): degree of the coefficient
                m (int): order of the coefficient
        
            Returns:
                un-normalized coefficient Cnm
        
        
        """
        ...
    def getUnnormalizedSnm(self, int: int, int2: int) -> float:
        """
            Get a spherical harmonic sine coefficient.
        
            Specified by:
                
                meth:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics.getUnnormalizedSnm`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`
        
            Parameters:
                n (int): degree of the coefficient
                m (int): order of the coefficient
        
            Returns:
                un-normalized coefficient Snm
        
        
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

class PythonUnnormalizedSphericalHarmonicsProvider(UnnormalizedSphericalHarmonicsProvider):
    """
    public class PythonUnnormalizedSphericalHarmonicsProvider extends Object implements :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float:
        """
            Get the value of the central body reference radius.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getAe`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
            Get the maximal supported degree.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxDegree`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
            Get the maximal supported order.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMaxOrder`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central body attraction coefficient.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getMu`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                mu (mÂ³/sÂ²)
        
        
        """
        ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the offset from
            :meth:`~org.orekit.forces.gravity.potential.PythonUnnormalizedSphericalHarmonicsProvider.getReferenceDate` for the
            harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getOffset`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                offset between current date and reference date if there is a reference date, or 0.0 if there are no reference dates
                (i.e. if :meth:`~org.orekit.forces.gravity.potential.PythonUnnormalizedSphericalHarmonicsProvider.getReferenceDate`
                returns null)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference date for the harmonics.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider.getReferenceDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.SphericalHarmonicsProvider`
        
            Returns:
                reference date for the harmonics
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
            Get the :class:`~org.orekit.forces.gravity.potential.TideSystem` used in the gravity field.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.TideSystemProvider.getTideSystem`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.TideSystemProvider`
        
            Returns:
                tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics:
        """
            Get the un-normalized spherical harmonic coefficients at a specific instance in time.
        
            Specified by:
                :meth:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.onDate`Â in
                interfaceÂ :class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): of evaluation
        
            Returns:
                un-normalized coefficients on :code:`date`.
        
            Since:
                6.1
        
        
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.gravity.potential")``.

    AstronomicalAmplitudeReader: typing.Type[AstronomicalAmplitudeReader]
    CachedNormalizedSphericalHarmonicsProvider: typing.Type[CachedNormalizedSphericalHarmonicsProvider]
    EGMFormatReader: typing.Type[EGMFormatReader]
    FESCHatEpsilonReader: typing.Type[FESCHatEpsilonReader]
    FESCnmSnmReader: typing.Type[FESCnmSnmReader]
    GRGSFormatReader: typing.Type[GRGSFormatReader]
    GravityFieldFactory: typing.Type[GravityFieldFactory]
    GravityFields: typing.Type[GravityFields]
    ICGEMFormatReader: typing.Type[ICGEMFormatReader]
    LazyLoadedGravityFields: typing.Type[LazyLoadedGravityFields]
    NormalizedSphericalHarmonicsProvider: typing.Type[NormalizedSphericalHarmonicsProvider]
    OceanLoadDeformationCoefficients: typing.Type[OceanLoadDeformationCoefficients]
    OceanTidesReader: typing.Type[OceanTidesReader]
    OceanTidesWave: typing.Type[OceanTidesWave]
    PotentialCoefficientsReader: typing.Type[PotentialCoefficientsReader]
    PythonGravityFields: typing.Type[PythonGravityFields]
    PythonNormalizedSphericalHarmonicsProvider: typing.Type[PythonNormalizedSphericalHarmonicsProvider]
    PythonPotentialCoefficientsReader: typing.Type[PythonPotentialCoefficientsReader]
    PythonRawSphericalHarmonicsProvider: typing.Type[PythonRawSphericalHarmonicsProvider]
    PythonSphericalHarmonicsProvider: typing.Type[PythonSphericalHarmonicsProvider]
    PythonTideSystemProvider: typing.Type[PythonTideSystemProvider]
    PythonUnnormalizedSphericalHarmonics: typing.Type[PythonUnnormalizedSphericalHarmonics]
    PythonUnnormalizedSphericalHarmonicsProvider: typing.Type[PythonUnnormalizedSphericalHarmonicsProvider]
    RawSphericalHarmonicsProvider: typing.Type[RawSphericalHarmonicsProvider]
    SHMFormatReader: typing.Type[SHMFormatReader]
    SphericalHarmonicsProvider: typing.Type[SphericalHarmonicsProvider]
    TideSystem: typing.Type[TideSystem]
    TideSystemProvider: typing.Type[TideSystemProvider]
    UnnormalizedSphericalHarmonicsProvider: typing.Type[UnnormalizedSphericalHarmonicsProvider]
