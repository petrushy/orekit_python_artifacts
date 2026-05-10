
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
import org.orekit.time
import typing



class AstronomicalAmplitudeReader(org.orekit.data.DataLoader):
    """
    Parser for tides astronomical amplitude H :sub:`f` .
    
    Since:
        6.1
    """
    def __init__(self, supportedNames: str, columns: int, columnDoodson: int, columnHf: int, scale: float):
        """
        Simple constructor.
        
        Parameters:
            supportedNames (String): regular expression for supported files names
            columns (int): number of columns
            columnDoodson (int): Doodson number column (counting from 1)
            columnHf (int): H :sub:`f` column (counting from 1)
            scale (double): scaling factor for astronomical amplitude
        
        
        """
        ...
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
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
        
        
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

class GravityFieldFactory:
    """
    Factory used to read gravity field files in several supported formats.
    """
    ICGEM_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for ICGEM files.
    
    Also see:
        constant
    
    
    """
    SHM_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for SHM files.
    
    Also see:
        constant
    
    
    """
    EGM_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for EGM files.
    
    Also see:
        constant
    
    
    """
    GRGS_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for GRGS files.
    
    Also see:
        constant
    
    
    """
    SHA_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for SHA files.
    
    Also see:
        constant
    
    
    """
    FES_CNM_SNM_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for FES Cnm, Snm tides files.
    
    Also see:
        constant
    
    
    """
    FES_CHAT_EPSILON_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for FES C hat and epsilon tides files.
    
    Also see:
        constant
    
    
    """
    FES_HF_FILENAME: typing.ClassVar[str] = ...
    """
    Default regular expression for FES Hf tides files.
    
    Also see:
        constant
    
    
    """
    @staticmethod
    def addDefaultOceanTidesReaders() -> None:
        """
        Add the default READERS for ocean tides.
        
        The default READERS supports files similar to the fes2004_Cnm-Snm.dat and fes2004.dat as published by IERS, using the configureOceanLoadDeformationCoefficients ocean load deformation coefficients, which by default are the IERS 2010 coefficients, which are limited to degree 6. If higher degree coefficients are needed, the configureOceanLoadDeformationCoefficients method can be called prior to loading the ocean tides model with the GEGOUT computed by Pascal Gégout.
        
        WARNING: the files referenced in the published conventions have some errors. These errors have been corrected and the updated files can be found here: ` http://tai.bipm.org/iers/convupdt/convupdt_c6.html <http://tai.bipm.org/iers/convupdt/convupdt_c6.html>`.
        
        Also see:
            addPotentialCoefficientsReader,
            clearPotentialCoefficientsReaders,
            configureOceanLoadDeformationCoefficients,
            getOceanLoadDeformationCoefficients
        
        
        """
        ...
    @staticmethod
    def addDefaultPotentialCoefficientsReaders() -> None:
        """
        Add the default readers for gravity fields.
        
        The default READERS supports ICGEM, SHM, EGM, GRGS and SHA formats with the default names ICGEM_FILENAME, SHM_FILENAME, EGM_FILENAME, GRGS_FILENAME, SHA_FILENAME and don't allow missing coefficients.
        
        Also see:
            addPotentialCoefficientsReader,
            clearPotentialCoefficientsReaders
        
        
        """
        ...
    @staticmethod
    def addOceanTidesReader(reader: 'OceanTidesReader') -> None:
        """
        Add a reader for ocean tides.
        
        Parameters:
            reader (OceanTidesReader): custom reader to add for the gravity field
        
        Also see:
            addDefaultPotentialCoefficientsReaders,
            clearPotentialCoefficientsReaders
        
        
        """
        ...
    @staticmethod
    def addPotentialCoefficientsReader(reader: 'PotentialCoefficientsReader') -> None:
        """
        Add a reader for gravity fields.
        
        Parameters:
            reader (PotentialCoefficientsReader): custom reader to add for the gravity field
        
        Also see:
            addDefaultPotentialCoefficientsReaders,
            clearPotentialCoefficientsReaders
        
        
        """
        ...
    @staticmethod
    def clearOceanTidesReaders() -> None:
        """
        Clear ocean tides readers.
        
        Also see:
            addPotentialCoefficientsReader,
            addDefaultPotentialCoefficientsReaders
        
        
        """
        ...
    @staticmethod
    def clearPotentialCoefficientsReaders() -> None:
        """
        Clear gravity field readers.
        
        Also see:
            addPotentialCoefficientsReader,
            addDefaultPotentialCoefficientsReaders
        
        
        """
        ...
    @staticmethod
    def configureOceanLoadDeformationCoefficients(oldc: 'OceanLoadDeformationCoefficients') -> None:
        """
        Configure ocean load deformation coefficients.
        
        Parameters:
            oldc (OceanLoadDeformationCoefficients): ocean load deformation coefficients
        
        Also see:
            getOceanLoadDeformationCoefficients
        
        
        """
        ...
    @staticmethod
    def getConstantNormalizedProvider(degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'NormalizedSphericalHarmonicsProvider':
        """
        Get the constant gravity field coefficients provider from the first supported file.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Since:
            12.0
        
        Also see:
            getNormalizedProvider
        
        
        """
        ...
    @staticmethod
    def getConstantUnnormalizedProvider(degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Get the constant gravity field coefficients provider from the first supported file.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Since:
            6.0
        
        Also see:
            getUnnormalizedProvider
        
        
        """
        ...
    @staticmethod
    def getGravityFields() -> 'LazyLoadedGravityFields':
        """
        Get the instance of GravityFields that is called by the static methods of this class.
        
        Returns:
            the gravity fields used by this factory.
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(ae: float, mu: float, tideSystem: 'TideSystem', normalizedC: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], normalizedS: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> 'NormalizedSphericalHarmonicsProvider':
        """
        Create a time-independent NormalizedSphericalHarmonicsProvider from canonical coefficients.
        
        Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data
        
        Parameters:
            ae (double): central body reference radius
            mu (double): central body attraction coefficient
            tideSystem (TideSystem): tide system
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
    def getNormalizedProvider(degree: int, order: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(unnormalized: 'UnnormalizedSphericalHarmonicsProvider') -> 'NormalizedSphericalHarmonicsProvider':
        """
        Create a NormalizedSphericalHarmonicsProvider from an UnnormalizedSphericalHarmonicsProvider.
        
        Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data.
        
        Parameters:
            unnormalized (UnnormalizedSphericalHarmonicsProvider): provider to normalize
        
        Returns:
            provider for normalized coefficients
        
        Since:
            6.0
        
        
        """
        ...
    @staticmethod
    def getOceanLoadDeformationCoefficients() -> 'OceanLoadDeformationCoefficients':
        """
        Get the configured ocean load deformation coefficients.
        
        If configureOceanLoadDeformationCoefficients has never been called, the default value will be the IERS_2010 coefficients.
        
        Returns:
            ocean load deformation coefficients
        
        Also see:
            configureOceanLoadDeformationCoefficients
        
        
        """
        ...
    @staticmethod
    def getOceanTidesWaves(degree: int, order: int) -> java.util.List['OceanTidesWave']:
        """
        Get the ocean tides waves from the first supported file.
        
        If no OceanTidesReader has been added by calling addOceanTidesReader or if clearOceanTidesReaders has been called afterwards, the addDefaultOceanTidesReaders method will be called automatically.
        
        WARNING: as of 2013-11-17, there seem to be an inconsistency when loading one or the other file, for wave Sa (Doodson number 56.554) and P1 (Doodson number 163.555). The sign of the coefficients are different. We think the problem lies in the input files from IERS and not in the conversion (which works for all other waves), but cannot be sure. For this reason, ocean tides are still considered experimental at this date.
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            list of tides waves containing already loaded data
        
        Since:
            6.1
        
        
        """
        ...
    @staticmethod
    def getUnnormalizationFactors(degree: int, order: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
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
    def getUnnormalizedProvider(ae: float, mu: float, tideSystem: 'TideSystem', unnormalizedC: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], unnormalizedS: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Create a time-independent UnnormalizedSphericalHarmonicsProvider from canonical coefficients.
        
        Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data
        
        Parameters:
            ae (double): central body reference radius
            mu (double): central body attraction coefficient
            tideSystem (TideSystem): tide system
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
    def getUnnormalizedProvider(degree: int, order: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getUnnormalizedProvider(normalized: 'NormalizedSphericalHarmonicsProvider') -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Create an UnnormalizedSphericalHarmonicsProvider from a NormalizedSphericalHarmonicsProvider.
        
        Note that contrary to the other factory method, this one does not read any data, it simply uses the provided data.
        
        Parameters:
            normalized (NormalizedSphericalHarmonicsProvider): provider to un-normalize
        
        Returns:
            provider for un-normalized coefficients
        
        Since:
            6.0
        
        
        """
        ...
    @staticmethod
    def readGravityField(maxParseDegree: int, maxParseOrder: int) -> 'PotentialCoefficientsReader':
        """
        Read a gravity field coefficients provider from the first supported file.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
        Parameters:
            maxParseDegree (int): maximal degree to parse
            maxParseOrder (int): maximal order to parse
        
        Returns:
            a reader containing already loaded data
        
        Since:
            6.0
        
        
        """
        ...

class GravityFields:
    """
    Defines methods for obtaining gravity fields.
    
    Since:
        10.1
    
    Also see:
        GravityFieldFactory
    """
    def getConstantNormalizedProvider(self, degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'NormalizedSphericalHarmonicsProvider':
        """
        Get a constant gravity field normalized coefficients provider frozen at a given epoch.
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Since:
            12.0
        
        Also see:
            getNormalizedProvider
        
        
        """
        ...
    def getConstantUnnormalizedProvider(self, degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Get a constant gravity field unnormalized coefficients provider frozen at a given epoch.
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Since:
            12.0
        
        Also see:
            getUnnormalizedProvider
        
        
        """
        ...
    def getNormalizedProvider(self, degree: int, order: int) -> 'NormalizedSphericalHarmonicsProvider':
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
            getConstantNormalizedProvider
        
        
        """
        ...
    def getOceanTidesWaves(self, degree: int, order: int) -> java.util.List['OceanTidesWave']:
        """
        Get the ocean tides waves.
        
        WARNING: as of 2013-11-17, there seem to be an inconsistency when loading one or the other file, for wave Sa (Doodson number 56.554) and P1 (Doodson number 163.555). The sign of the coefficients are different. We think the problem lies in the input files from IERS and not in the conversion (which works for all other waves), but cannot be sure. For this reason, ocean tides are still considered experimental at this date.
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            list of tides waves containing already loaded data
        
        Since:
            6.1
        
        
        """
        ...
    def getUnnormalizedProvider(self, degree: int, order: int) -> 'UnnormalizedSphericalHarmonicsProvider':
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
            getConstantUnnormalizedProvider
        
        
        """
        ...

class OceanLoadDeformationCoefficients(java.lang.Enum['OceanLoadDeformationCoefficients']):
    """
    Supported Ocean load Deformation coefficients (Love numbers k' :sub:`i` ).
    
    Since:
        6.1
    
    Also see:
        GravityFields
    """
    IERS_1996: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    IERS_2003: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    IERS_2010: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    GEGOUT: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    def getCoefficients(self) -> typing.MutableSequence[float]:
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
    def valueOf(name: str) -> 'OceanLoadDeformationCoefficients':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['OceanLoadDeformationCoefficients']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (OceanLoadDeformationCoefficients c : OceanLoadDeformationCoefficients.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OceanTidesReader(org.orekit.data.DataLoader):
    """
    Reader for ocean tides coefficients.
    
    Since:
        6.1
    
    Also see:
        OceanTidesWave
    """
    def __init__(self, supportedNames: str):
        """
        Simple constructor.
        
        Parameters:
            supportedNames (String): regular expression for supported files names
        
        
        """
        ...
    def canAdd(self, n: int, m: int) -> bool:
        """
        Check if coefficients can be added.
        
        Parameters:
            n (int): degree of the coefficients
            m (int): order of the coefficients
        
        Returns:
            true if coefficients can be added
        
        
        """
        ...
    def getMaxAvailableDegree(self) -> int:
        """
        Get the maximal degree available in the last file parsed.
        
        Returns:
            maximal degree available in the last file parsed
        
        Since:
            12.0.1
        
        
        """
        ...
    def getMaxAvailableOrder(self) -> int:
        """
        Get the maximal order available in the last file parsed.
        
        Returns:
            maximal order available in the last file parsed
        
        Since:
            12.0.1
        
        
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
    def getWaves(self) -> java.util.List['OceanTidesWave']:
        """
        Get the loaded waves.
        
        Returns:
            loaded waves
        
        
        """
        ...
    def setMaxParseDegree(self, maxParseDegree: int) -> None:
        """
        Set the degree limit for the next file parsing.
        
        Parameters:
            maxParseDegree (int): maximal degree to parse (may be safely set to
                Integer to parse
                all available coefficients)
        
        
        """
        ...
    def setMaxParseOrder(self, maxParseOrder: int) -> None:
        """
        Set the order limit for the next file parsing.
        
        Parameters:
            maxParseOrder (int): maximal order to parse (may be safely set to
                Integer to parse
                all available coefficients)
        
        
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

class OceanTidesWave:
    """
    Container for ocen tides coefficients for one tide wave.
    
    Since:
        6.1
    
    Also see:
        OceanTides, OceanTidesReader
    """
    def __init__(self, doodson: int, degree: int, order: int, coefficients: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            doodson (int): Doodson number for the wave
            degree (int): max degree present in the coefficients array
            order (int): max order present in the coefficients array
            coefficients (double[][][]): C :sub:`n,m` :sup:`+` , S :sub:`n,m` :sup:`+` , C :sub:`n,m` :sup:`-` and S :sub:`n,m` :sup:`-` coefficients
        
        
        """
        ...
    def addContribution(self, elements: org.orekit.data.BodiesElements, cnm: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], snm: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
        Add the contribution of the wave to Stokes coefficients.
        
        Parameters:
            elements (BodiesElements): nutation elements
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
    This abstract class represents a Gravitational Potential Coefficients file reader.
    
    As it exits many different coefficients models and containers this interface represents all the methods that should be implemented by a reader. The proper way to use this interface is to call the GravityFieldFactory which will determine which reader to use with the selected potential coefficients file.
    
    Also see:
        GravityFields
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
    def getProvider(self, wantNormalized: bool, degree: int, order: int) -> 'RawSphericalHarmonicsProvider':
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
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
        Get the regular expression for supported files names.
        
        Returns:
            regular expression for supported files names
        
        
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
    def missingCoefficientsAllowed(self) -> bool:
        """
        Check if missing coefficients are allowed in the input data.
        
        Returns:
            true if missing coefficients are allowed in the input data
        
        
        """
        ...
    def setMaxParseDegree(self, maxParseDegree: int) -> None:
        """
        Set the degree limit for the next file parsing.
        
        Parameters:
            maxParseDegree (int): maximal degree to parse (may be safely set to
                Integer to parse
                all available coefficients)
        
        Since:
            6.0
        
        
        """
        ...
    def setMaxParseOrder(self, maxParseOrder: int) -> None:
        """
        Set the order limit for the next file parsing.
        
        Parameters:
            maxParseOrder (int): maximal order to parse (may be safely set to
                Integer to parse
                all available coefficients)
        
        Since:
            6.0
        
        
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

class TideSystem(java.lang.Enum['TideSystem']):
    """
    Enumerate for tie systems.
    
    Tide-systems are used to identify if the permanent tide is already present in the gravity field or if it should be handled when computing the solid tides force model.
    
    Since:
        6.0
    
    Also see:
        SphericalHarmonicsProvider
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
    def valueOf(name: str) -> 'TideSystem':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['TideSystem']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (TideSystem c : TideSystem.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TideSystemProvider:
    """
    Interface used to provide TideSystem.
    
    Since:
        6.0
    """
    def getTideSystem(self) -> TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Returns:
            tide system used in the gravity field
        
        
        """
        ...

class EGMFormatReader(PotentialCoefficientsReader):
    """
    This reader is adapted to the EGM Format.
    
    The proper way to use this class is to call the GravityFieldFactory which will determine which reader to use with the selected gravity field file.
    
    Also see:
        GravityFields
    """
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool): ...
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool, useWgs84Coefficients: bool): ...
    def getProvider(self, wantNormalized: bool, degree: int, order: int) -> 'RawSphericalHarmonicsProvider':
        """
        Get a provider for read spherical harmonics coefficients.
        
        EGM fields don't include time-dependent parts, so this method returns directly a constant provider.
        
        Specified by: getProvider in class PotentialCoefficientsReader
        
        Parameters:
            wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a new provider
        
        Since:
            6.0
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Specified by: loadData in class PotentialCoefficientsReader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...

class FESCHatEpsilonReader(OceanTidesReader):
    """
    Reader for ocean tides files following the fes2004.dat format.
    
    Since:
        6.1
    """
    def __init__(self, supportedNames: str, scaleCHat: float, scaleEpsilon: float, oldc: OceanLoadDeformationCoefficients, astronomicalAmplitudes: typing.Union[java.util.Map[int, float], typing.Mapping[int, float]]):
        """
        Simple constructor.
        
        Parameters:
            supportedNames (String): regular expression for supported files names
            scaleCHat (double): scale of the CHat parameters
            scaleEpsilon (double): scale of the epsilon parameters
            oldc (OceanLoadDeformationCoefficients): load deformation coefficients for ocean tides
            astronomicalAmplitudes (Map<Integer, Double> astronomicalAmplitudes): map for astronomical amplitudes
        
        Also see:
            getAstronomicalAmplitudesMap
        
        
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
        
        
        """
        ...

class FESCnmSnmReader(OceanTidesReader):
    """
    Reader for ocean tides files following the fes2004_Cnm-Snm.dat format.
    
    Since:
        6.1
    """
    def __init__(self, supportedNames: str, scale: float):
        """
        Simple constructor.
        
        Parameters:
            supportedNames (String): regular expression for supported files names
            scale (double): scale of the Cnm, Snm parameters
        
        
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
        
        
        """
        ...

class GRGSFormatReader(PotentialCoefficientsReader):
    """
    Reader for the GRGS gravity field format.
    
    This format was used to describe various gravity fields at GRGS (Toulouse).
    
    The proper way to use this class is to call the GravityFieldFactory which will determine which reader to use with the selected gravity field file.
    
    Also see:
        GravityFields
    """
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool): ...
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, wantNormalized: bool, degree: int, order: int) -> 'RawSphericalHarmonicsProvider':
        """
        Get a provider for read spherical harmonics coefficients.
        
        GRGS fields may include time-dependent parts which are taken into account in the returned provider.
        
        Specified by: getProvider in class PotentialCoefficientsReader
        
        Parameters:
            wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a new provider
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Specified by: loadData in class PotentialCoefficientsReader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...

class ICGEMFormatReader(PotentialCoefficientsReader):
    """
    Reader for the ICGEM gravity field format.
    
    This format is used to describe the gravity field of EIGEN models published by the GFZ Potsdam since 2004. It is described in Franz Barthelmes and Christoph Förste paper: "the ICGEM-format". The 2006-02-28 version of this paper can be found `here <http://op.gfz-potsdam.de/grace/results/grav/g005_ICGEM-Format.pdf>` and the 2011-06-07 version of this paper can be found `here <http://icgem.gfz-potsdam.de/ICGEM-Format-2011.pdf>`. These versions differ in time-dependent coefficients, which are linear-only prior to 2011 (up to eigen-5 model) and have also harmonic effects after that date (starting with eigen-6 model). A third (undocumented as of 2018-05-14) version of the file format also adds a time-span for time-dependent coefficients, allowing for piecewise models. All three versions are supported by the class.
    
    This reader uses relaxed check on the gravity constant key so any key ending in gravity_constant is accepted and not only earth_gravity_constant as specified in the previous documents. This allows to read also non Earth gravity fields as found in `ICGEM - Gravity Field Models of other Celestial Bodies <http://icgem.gfz-potsdam.de/tom_celestial>` page to be read.
    
    The proper way to use this class is to call the GravityFieldFactory which will determine which reader to use with the selected gravity field file.
    
    Also see:
        GravityFields
    """
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool): ...
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, wantNormalized: bool, degree: int, order: int) -> 'RawSphericalHarmonicsProvider':
        """
        Get a provider for read spherical harmonics coefficients.
        
        Specified by: getProvider in class PotentialCoefficientsReader
        
        Parameters:
            wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a new provider
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Specified by: loadData in class PotentialCoefficientsReader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...

class LazyLoadedGravityFields(GravityFields):
    """
    Loads gravity fields when first requested and can be configured until then. Designed to match the behavior of GravityFieldFactory in Orekit 10.0.
    
    Since:
        10.1
    
    Also see:
        GravityFieldFactory
    """
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale):
        """
        Create a factory for gravity fields that uses the given data manager to load the gravity field files.
        
        Parameters:
            dataProvidersManager (DataProvidersManager): provides access to auxiliary data files.
            timeScale (TimeScale): use to parse dates for the
                addDefaultPotentialCoefficientsReaders. In Orekit
                10.0 it is TT.
        
        
        """
        ...
    def addDefaultOceanTidesReaders(self) -> None:
        """
        Add the default readers for ocean tides.
        
        The default readers support files similar to the fes2004_Cnm-Snm.dat and fes2004.dat as published by IERS, using the configureOceanLoadDeformationCoefficients ocean load deformation coefficients, which by default are the IERS 2010 coefficients, which are limited to degree 6. If higher degree coefficients are needed, the configureOceanLoadDeformationCoefficients method can be called prior to loading the ocean tides model with the GEGOUT computed by Pascal Gégout.
        
        WARNING: the files referenced in the published conventions have some errors. These errors have been corrected and the updated files can be found here: ` http://tai.bipm.org/iers/convupdt/convupdt_c6.html <http://tai.bipm.org/iers/convupdt/convupdt_c6.html>`.
        
        Also see:
            addPotentialCoefficientsReader,
            clearPotentialCoefficientsReaders,
            configureOceanLoadDeformationCoefficients,
            getOceanLoadDeformationCoefficients
        
        
        """
        ...
    def addDefaultPotentialCoefficientsReaders(self) -> None:
        """
        Add the default readers for gravity fields.
        
        The default readers support ICGEM, SHM, EGM, GRGS and SHA formats with the default names ICGEM_FILENAME, SHM_FILENAME, EGM_FILENAME, GRGS_FILENAME, SHA_FILENAME and don't allow missing coefficients.
        
        Also see:
            addPotentialCoefficientsReader,
            clearPotentialCoefficientsReaders
        
        
        """
        ...
    def addOceanTidesReader(self, reader: OceanTidesReader) -> None:
        """
        Add a reader for ocean tides.
        
        Parameters:
            reader (OceanTidesReader): custom reader to add for the gravity field
        
        Also see:
            addDefaultPotentialCoefficientsReaders,
            clearPotentialCoefficientsReaders
        
        
        """
        ...
    def addPotentialCoefficientsReader(self, reader: PotentialCoefficientsReader) -> None:
        """
        Add a reader for gravity fields.
        
        Parameters:
            reader (PotentialCoefficientsReader): custom reader to add for the gravity field
        
        Also see:
            addDefaultPotentialCoefficientsReaders,
            clearPotentialCoefficientsReaders
        
        
        """
        ...
    def clearOceanTidesReaders(self) -> None:
        """
        Clear ocean tides readers.
        
        Also see:
            addPotentialCoefficientsReader,
            addDefaultPotentialCoefficientsReaders
        
        
        """
        ...
    def clearPotentialCoefficientsReaders(self) -> None:
        """
        Clear gravity field readers.
        
        Also see:
            addPotentialCoefficientsReader,
            addDefaultPotentialCoefficientsReaders
        
        
        """
        ...
    def configureOceanLoadDeformationCoefficients(self, oldc: OceanLoadDeformationCoefficients) -> None:
        """
        Configure ocean load deformation coefficients.
        
        Parameters:
            oldc (OceanLoadDeformationCoefficients): ocean load deformation coefficients
        
        Also see:
            getOceanLoadDeformationCoefficients
        
        
        """
        ...
    def getConstantNormalizedProvider(self, degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'NormalizedSphericalHarmonicsProvider':
        """
        Get a constant gravity field normalized coefficients provider frozen at a given epoch.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
        Specified by: getConstantNormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getNormalizedProvider
        
        
        """
        ...
    def getConstantUnnormalizedProvider(self, degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Get a constant gravity field unnormalized coefficients provider frozen at a given epoch.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
        Specified by: getConstantUnnormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getUnnormalizedProvider
        
        
        """
        ...
    def getNormalizedProvider(self, degree: int, order: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
        Get a gravity field normalized coefficients provider.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
        Specified by: getNormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getConstantNormalizedProvider
        
        
        """
        ...
    def getOceanLoadDeformationCoefficients(self) -> OceanLoadDeformationCoefficients:
        """
        Get the configured ocean load deformation coefficients.
        
        If configureOceanLoadDeformationCoefficients has never been called, the default value will be the IERS_2010 coefficients.
        
        Returns:
            ocean load deformation coefficients
        
        Also see:
            configureOceanLoadDeformationCoefficients
        
        
        """
        ...
    def getOceanTidesWaves(self, degree: int, order: int) -> java.util.List[OceanTidesWave]:
        """
        Get the ocean tides waves.
        
        WARNING: as of 2013-11-17, there seem to be an inconsistency when loading one or the other file, for wave Sa (Doodson number 56.554) and P1 (Doodson number 163.555). The sign of the coefficients are different. We think the problem lies in the input files from IERS and not in the conversion (which works for all other waves), but cannot be sure. For this reason, ocean tides are still considered experimental at this date.
        
        If no OceanTidesReader has been added by calling addOceanTidesReader or if clearOceanTidesReaders has been called afterwards, the addDefaultOceanTidesReaders method will be called automatically.
        
        Specified by: getOceanTidesWaves in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            list of tides waves containing already loaded data
        
        
        """
        ...
    def getUnnormalizedProvider(self, degree: int, order: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Get a gravity field unnormalized coefficients provider.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
        Specified by: getUnnormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getConstantUnnormalizedProvider
        
        
        """
        ...
    def readGravityField(self, maxParseDegree: int, maxParseOrder: int) -> PotentialCoefficientsReader:
        """
        Read a gravity field coefficients provider from the first supported file.
        
        If no PotentialCoefficientsReader has been added by calling addPotentialCoefficientsReader or if clearPotentialCoefficientsReaders has been called afterwards, the addDefaultPotentialCoefficientsReaders method will be called automatically.
        
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
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getConstantNormalizedProvider(self, degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'NormalizedSphericalHarmonicsProvider':
        """
        Description copied from interface: getConstantNormalizedProvider Get a constant gravity field normalized coefficients provider frozen at a given epoch.
        
        Specified by: getConstantNormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getNormalizedProvider
        
        
        """
        ...
    def getConstantUnnormalizedProvider(self, degree: int, order: int, freezingDate: org.orekit.time.AbsoluteDate) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Description copied from interface: getConstantUnnormalizedProvider Get a constant gravity field unnormalized coefficients provider frozen at a given epoch.
        
        Specified by: getConstantUnnormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
            freezingDate (AbsoluteDate): freezing epoch
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getUnnormalizedProvider
        
        
        """
        ...
    def getNormalizedProvider(self, degree: int, order: int) -> 'NormalizedSphericalHarmonicsProvider':
        """
        Description copied from interface: getNormalizedProvider Get a gravity field normalized coefficients provider.
        
        Specified by: getNormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getConstantNormalizedProvider
        
        
        """
        ...
    def getOceanTidesWaves(self, degree: int, order: int) -> java.util.List[OceanTidesWave]:
        """
        Get the ocean tides waves.
        
        WARNING: as of 2013-11-17, there seem to be an inconsistency when loading one or the other file, for wave Sa (Doodson number 56.554) and P1 (Doodson number 163.555). The sign of the coefficients are different. We think the problem lies in the input files from IERS and not in the conversion (which works for all other waves), but cannot be sure. For this reason, ocean tides are still considered experimental at this date.
        
        Specified by: getOceanTidesWaves in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            list of tides waves containing already loaded data
        
        Since:
            6.1
        
        
        """
        ...
    def getUnnormalizedProvider(self, degree: int, order: int) -> 'UnnormalizedSphericalHarmonicsProvider':
        """
        Description copied from interface: getUnnormalizedProvider Get a gravity field unnormalized coefficients provider.
        
        Specified by: getUnnormalizedProvider in interface GravityFields
        
        Parameters:
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a gravity field coefficients provider containing already loaded data
        
        Also see:
            getConstantUnnormalizedProvider
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonPotentialCoefficientsReader(PotentialCoefficientsReader):
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool): ...
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool, timeScale: org.orekit.time.TimeScale): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getProvider(self, wantNormalized: bool, degree: int, order: int) -> 'RawSphericalHarmonicsProvider':
        """
        Get a provider for read spherical harmonics coefficients.
        
        Specified by: getProvider in class PotentialCoefficientsReader
        
        Parameters:
            wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a new provider
        
        Since:
            6.0
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Specified by: loadData in class PotentialCoefficientsReader
        
        Parameters:
            input (InputStream):         name (String): 
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
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

class PythonTideSystemProvider(TideSystemProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Specified by: getTideSystem in interface TideSystemProvider
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class SHAFormatReader(PotentialCoefficientsReader):
    """
    Reader for the SHA gravity field format.
    
    This format is used by some lunar gravity models distributed by NASA's Planetary Geology, Geophysics and Geochemistry Laboratory such as GRGM1200B and GRGM1200L. It is a simple ASCII format, described in products. The first line contains 4 constants: model GM, mean radius, maximum degree and maximum order. All other lines contain 6 entries: degree, order, Clm, Slm, sigma Clm and sigma Slm (formal errors of Clm and Slm).
    
    The proper way to use this class is to call the GravityFieldFactory which will determine which reader to use with the selected gravity field file.
    
    Also see:
        GravityFields
    """
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool):
        """
        Simple constructor.
        
        Parameters:
            supportedNames (String): regular expression for supported files names
            missingCoefficientsAllowed (boolean): if true, allows missing coefficients in the input data
        
        Since:
            12.2
        
        
        """
        ...
    def getProvider(self, wantNormalized: bool, degree: int, order: int) -> 'RawSphericalHarmonicsProvider':
        """
        Provider for read spherical harmonics coefficients. Like EGM fields, SHA fields don't include time-dependent parts, so this method returns directly a constant provider.
        
        Specified by: getProvider in class PotentialCoefficientsReader
        
        Parameters:
            wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a new provider
        
        Since:
            12.2
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Specified by: loadData in class PotentialCoefficientsReader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...

class SHMFormatReader(PotentialCoefficientsReader):
    """
    Reader for the SHM gravity field format.
    
    This format was used to describe the gravity field of EIGEN models published by the GFZ Potsdam up to 2003. It was then replaced by ICGEMFormatReader. The SHM format is described in ` Potsdam university website <http://op.gfz-potsdam.de/champ/docs_CHAMP/CH-FORMAT-REFLINKS.html>`.
    
    The proper way to use this class is to call the GravityFieldFactory which will determine which reader to use with the selected gravity field file.
    
    Also see:
        GravityFields
    """
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool): ...
    @typing.overload
    def __init__(self, supportedNames: str, missingCoefficientsAllowed: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, wantNormalized: bool, degree: int, order: int) -> 'RawSphericalHarmonicsProvider':
        """
        Get a provider for read spherical harmonics coefficients.
        
        SHM fields do include time-dependent parts which are taken into account in the returned provider.
        
        Specified by: getProvider in class PotentialCoefficientsReader
        
        Parameters:
            wantNormalized (boolean): if true, the provider will provide normalized coefficients, otherwise it will provide un-normalized coefficients
            degree (int): maximal degree
            order (int): maximal order
        
        Returns:
            a new provider
        
        Since:
            6.0
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Specified by: loadData in class PotentialCoefficientsReader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...

class SphericalHarmonicsProvider(TideSystemProvider):
    """
    Interface used to provide spherical harmonics coefficients.
    
    Two interfaces are provided to distinguish between normalized and un-normalized coefficients: NormalizedSphericalHarmonicsProvider and UnnormalizedSphericalHarmonicsProvider. To account for gravity perturbations all providers are capable of providing the coefficients on specific dates, using the onDate methods.
    
    Typical usage when evaluating the geopotential:
    
    
         NormalizedSphericalHarmonicsProvider provider = ...;
         NormalizedSphericalHarmonics coeffs = provider.onDate(date);
         double c20 = coeffs.getNormalizedCnm(2, 0);
     
    
    Since:
        6.0
    
    Also see:
        GravityFields
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
            mu (m³/s²)
        
        
        """
        ...
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
    Interface used to provide normalized spherical harmonics coefficients.
    
    Since:
        6.0
    
    Also see:
        GravityFields
    """
    def getNormalizedC20(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the normalized coefficient of degree 2 and order 0 at a specific instance in time.
        
        Parameters:
            date (AbsoluteDate): of evaluation (may be null if model is not time-dependent)
        
        Returns:
            normalized C20 on date.
        
        Since:
            12.1
        
        
        """
        ...
    def onDate(self, date: org.orekit.time.AbsoluteDate) -> 'NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics':
        """
        Get the normalized spherical harmonic coefficients at a specific instance in time.
        
        Parameters:
            date (AbsoluteDate): of evaluation
        
        Returns:
            normalized coefficients on date.
        
        Since:
            6.1
        
        
        """
        ...
    class NormalizedSphericalHarmonics(org.orekit.time.TimeStamped):
        def getNormalizedCnm(self, int: int, int2: int) -> float: ...
        def getNormalizedSnm(self, int: int, int2: int) -> float: ...

class PythonSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAe(self) -> float:
        """
        Get the value of the central body reference radius.
        
        Specified by: getAe in interface SphericalHarmonicsProvider
        
        Returns:
            ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
        Description copied from interface: getMaxDegree Get the maximal supported degree.
        
        Specified by: getMaxDegree in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
        Get the maximal supported order.
        
        Specified by: getMaxOrder in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central body attraction coefficient.
        
        Specified by: getMu in interface SphericalHarmonicsProvider
        
        Returns:
            mu (m³/s²)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference date for the harmonics.
        
        For piecewise models, the latest reference date is returned.
        
        Specified by: getReferenceDate in interface SphericalHarmonicsProvider
        
        Returns:
            reference date for the harmonics (may be null if no reference date is defined)
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Specified by: getTideSystem in interface TideSystemProvider
        
        Returns:
            tide system used in the gravity field
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class RawSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    """
    Interface used to provide raw spherical harmonics coefficients.
    
    This interface is intended to be used only as the workhorse for either NormalizedSphericalHarmonicsProvider or SphericalHarmonicsProvider implementations.
    
    Since:
        6.0
    
    Also see:
        GravityFields
    """
    def onDate(self, date: org.orekit.time.AbsoluteDate) -> 'RawSphericalHarmonicsProvider.RawSphericalHarmonics':
        """
        Get the raw spherical harmonic coefficients on a specific date.
        
        Parameters:
            date (AbsoluteDate): to evaluate the spherical harmonics
        
        Returns:
            the raw spherical harmonics on date.
        
        
        """
        ...
    class RawSphericalHarmonics(org.orekit.time.TimeStamped):
        def getRawCnm(self, int: int, int2: int) -> float: ...
        def getRawSnm(self, int: int, int2: int) -> float: ...

class UnnormalizedSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    """
    Interface used to provide un-normalized spherical harmonics coefficients.
    
    Un-normalized spherical harmonics coefficients are fine for small degrees. At high degree and order the un-normalized coefficients are not representable in a double. NormalizedSphericalHarmonicsProvider is recommended for high precision applications.
    
    Since:
        6.0
    
    Also see:
        GravityFields
    """
    def getUnnormalizedC20(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the un-normalized coefficient of degree 2 and order 0 at a specific instance in time.
        
        Parameters:
            date (AbsoluteDate): of evaluation (may be null if model is not time-dependent)
        
        Returns:
            un-normalized C20 on date.
        
        Since:
            12.1
        
        
        """
        ...
    def onDate(self, date: org.orekit.time.AbsoluteDate) -> 'UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics':
        """
        Get the un-normalized spherical harmonic coefficients at a specific instance in time.
        
        Parameters:
            date (AbsoluteDate): of evaluation (may be null if model is not time-dependent)
        
        Returns:
            un-normalized coefficients on date.
        
        Since:
            6.1
        
        
        """
        ...
    class UnnormalizedSphericalHarmonics(org.orekit.time.TimeStamped):
        def getUnnormalizedCnm(self, int: int, int2: int) -> float: ...
        def getUnnormalizedSnm(self, int: int, int2: int) -> float: ...

class CachedNormalizedSphericalHarmonicsProvider(NormalizedSphericalHarmonicsProvider):
    """
    Caching wrapper for NormalizedSphericalHarmonicsProvider.
    
    This wrapper improves efficiency of NormalizedSphericalHarmonicsProvider by sampling the values at a user defined rate and using interpolation between samples. This is important with providers that have sub-daily frequencies and are computing intensive, such as tides fields.
    
    Since:
        6.1
    
    Also see:
        NormalizedSphericalHarmonicsProvider,
        SolidTides, TimeStampedCache
    """
    def __init__(self, rawProvider: NormalizedSphericalHarmonicsProvider, step: float, nbPoints: int, maxSlots: int, maxSpan: float, newSlotInterval: float):
        """
        Simple constructor.
        
        Parameters:
            rawProvider (NormalizedSphericalHarmonicsProvider): underlying raw provider
            step (double): time step between sample points for interpolation
            nbPoints (int): number of points to use for interpolation, must be at least 2
            maxSlots (int): maximum number of independent cached time slots
            maxSpan (double): maximum duration span in seconds of one slot (can be set to POSITIVE_INFINITY if desired)
            newSlotInterval (double): time interval above which a new slot is created instead of extending an existing one
        
        
        """
        ...
    def getAe(self) -> float:
        """
        Get the value of the central body reference radius.
        
        Specified by: getAe in interface SphericalHarmonicsProvider
        
        Returns:
            ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
        Get the maximal supported degree.
        
        Specified by: getMaxDegree in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
        Get the maximal supported order.
        
        Specified by: getMaxOrder in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central body attraction coefficient.
        
        Specified by: getMu in interface SphericalHarmonicsProvider
        
        Returns:
            mu (m³/s²)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference date for the harmonics.
        
        For piecewise models, the latest reference date is returned.
        
        Specified by: getReferenceDate in interface SphericalHarmonicsProvider
        
        Returns:
            reference date for the harmonics (may be null if no reference date is defined)
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Specified by: getTideSystem in interface TideSystemProvider
        
        Returns:
            tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, date: org.orekit.time.AbsoluteDate) -> NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics:
        """
        Get the normalized spherical harmonic coefficients at a specific instance in time.
        
        Specified by: onDate in interface NormalizedSphericalHarmonicsProvider
        
        Parameters:
            date (AbsoluteDate): of evaluation
        
        Returns:
            normalized coefficients on date.
        
        
        """
        ...

class PythonNormalizedSphericalHarmonicsProvider(NormalizedSphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAe(self) -> float:
        """
        Get the value of the central body reference radius.
        
        Specified by: getAe in interface SphericalHarmonicsProvider
        
        Returns:
            ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
        Get the maximal supported degree.
        
        Specified by: getMaxDegree in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
        Get the maximal supported order.
        
        Specified by: getMaxOrder in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central body attraction coefficient.
        
        Specified by: getMu in interface SphericalHarmonicsProvider
        
        Returns:
            mu (m³/s²)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference date for the harmonics.
        
        Specified by: getReferenceDate in interface SphericalHarmonicsProvider
        
        Returns:
            reference date for the harmonics
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Specified by: getTideSystem in interface TideSystemProvider
        
        Returns:
            tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, date: org.orekit.time.AbsoluteDate) -> NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics:
        """
        Get the normalized spherical harmonic coefficients at a specific instance in time.
        
        Specified by: onDate in interface NormalizedSphericalHarmonicsProvider
        
        Parameters:
            date (AbsoluteDate): of evaluation
        
        Returns:
            normalized coefficients on date.
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonRawSphericalHarmonicsProvider(RawSphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAe(self) -> float:
        """
        Get the value of the central body reference radius.
        
        Specified by: getAe in interface SphericalHarmonicsProvider
        
        Returns:
            ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
        Get the maximal supported degree.
        
        Specified by: getMaxDegree in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
        Get the maximal supported order.
        
        Specified by: getMaxOrder in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central body attraction coefficient.
        
        Specified by: getMu in interface SphericalHarmonicsProvider
        
        Returns:
            mu (m³/s²)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference date for the harmonics.
        
        For piecewise models, the latest reference date is returned.
        
        Specified by: getReferenceDate in interface SphericalHarmonicsProvider
        
        Returns:
            reference date for the harmonics (may be null if no reference date is defined)
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Specified by: getTideSystem in interface TideSystemProvider
        
        Returns:
            tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, date: org.orekit.time.AbsoluteDate) -> RawSphericalHarmonicsProvider.RawSphericalHarmonics:
        """
        Get the raw spherical harmonic coefficients on a specific date.
        
        Specified by: onDate in interface RawSphericalHarmonicsProvider
        
        Parameters:
            date (AbsoluteDate): to evaluate the spherical harmonics
        
        Returns:
            the raw spherical harmonics on date.
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonUnnormalizedSphericalHarmonics(UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def getUnnormalizedCnm(self, n: int, m: int) -> float:
        """
        Get a spherical harmonic cosine coefficient.
        
        Specified by: meth:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics.getUnnormalizedCnm` in interface UnnormalizedSphericalHarmonics
        
        Parameters:
            n (int): degree of the coefficient
            m (int): order of the coefficient
        
        Returns:
            un-normalized coefficient Cnm
        
        
        """
        ...
    def getUnnormalizedSnm(self, n: int, m: int) -> float:
        """
        Get a spherical harmonic sine coefficient.
        
        Specified by: meth:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics.getUnnormalizedSnm` in interface UnnormalizedSphericalHarmonics
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonUnnormalizedSphericalHarmonicsProvider(UnnormalizedSphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAe(self) -> float:
        """
        Get the value of the central body reference radius.
        
        Specified by: getAe in interface SphericalHarmonicsProvider
        
        Returns:
            ae (m)
        
        
        """
        ...
    def getMaxDegree(self) -> int:
        """
        Get the maximal supported degree.
        
        Specified by: getMaxDegree in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported degree
        
        
        """
        ...
    def getMaxOrder(self) -> int:
        """
        Get the maximal supported order.
        
        Specified by: getMaxOrder in interface SphericalHarmonicsProvider
        
        Returns:
            maximal supported order
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central body attraction coefficient.
        
        Specified by: getMu in interface SphericalHarmonicsProvider
        
        Returns:
            mu (m³/s²)
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference date for the harmonics.
        
        Specified by: getReferenceDate in interface SphericalHarmonicsProvider
        
        Returns:
            reference date for the harmonics
        
        
        """
        ...
    def getTideSystem(self) -> TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Specified by: getTideSystem in interface TideSystemProvider
        
        Returns:
            tide system used in the gravity field
        
        
        """
        ...
    def onDate(self, date: org.orekit.time.AbsoluteDate) -> UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics:
        """
        Get the un-normalized spherical harmonic coefficients at a specific instance in time.
        
        Specified by: onDate in interface UnnormalizedSphericalHarmonicsProvider
        
        Parameters:
            date (AbsoluteDate): of evaluation
        
        Returns:
            un-normalized coefficients on date.
        
        Since:
            6.1
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...


class __module_protocol__(Protocol):
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
    SHAFormatReader: typing.Type[SHAFormatReader]
    SHMFormatReader: typing.Type[SHMFormatReader]
    SphericalHarmonicsProvider: typing.Type[SphericalHarmonicsProvider]
    TideSystem: typing.Type[TideSystem]
    TideSystemProvider: typing.Type[TideSystemProvider]
    UnnormalizedSphericalHarmonicsProvider: typing.Type[UnnormalizedSphericalHarmonicsProvider]
