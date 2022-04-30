import java.io
import java.lang
import java.util
import org.hipparchus.analysis
import org.hipparchus.complex
import org.hipparchus.exception
import typing



class DctNormalization(java.lang.Enum['DctNormalization']):
    """
    public enum DctNormalization extends :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.transform.DctNormalization`>
    
        This enumeration defines the various types of normalizations that can be applied to discrete cosine transforms (DCT).
        The exact definition of these normalizations is detailed below.
    
        Also see:
            :class:`~org.hipparchus.transform.FastCosineTransformer`
    """
    STANDARD_DCT_I: typing.ClassVar['DctNormalization'] = ...
    ORTHOGONAL_DCT_I: typing.ClassVar['DctNormalization'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DctNormalization':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['DctNormalization']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (DctNormalization c : DctNormalization.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DftNormalization(java.lang.Enum['DftNormalization']):
    """
    public enum DftNormalization extends :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.transform.DftNormalization`>
    
        This enumeration defines the various types of normalizations that can be applied to discrete Fourier transforms (DFT).
        The exact definition of these normalizations is detailed below.
    
        Also see:
            :class:`~org.hipparchus.transform.FastFourierTransformer`
    """
    STANDARD: typing.ClassVar['DftNormalization'] = ...
    UNITARY: typing.ClassVar['DftNormalization'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DftNormalization':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['DftNormalization']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (DftNormalization c : DftNormalization.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DstNormalization(java.lang.Enum['DstNormalization']):
    """
    public enum DstNormalization extends :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.transform.DstNormalization`>
    
        This enumeration defines the various types of normalizations that can be applied to discrete sine transforms (DST). The
        exact definition of these normalizations is detailed below.
    
        Also see:
            :class:`~org.hipparchus.transform.FastSineTransformer`
    """
    STANDARD_DST_I: typing.ClassVar['DstNormalization'] = ...
    ORTHOGONAL_DST_I: typing.ClassVar['DstNormalization'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DstNormalization':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['DstNormalization']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (DstNormalization c : DstNormalization.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class FastFourierTransformer(java.io.Serializable):
    """
    public class FastFourierTransformer extends :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Implements the Fast Fourier Transform for transformation of one-dimensional real or complex data sets. For reference,
        see *Applied Numerical Linear Algebra*, ISBN 0898713897, chapter 6.
    
        There are several variants of the discrete Fourier transform, with various normalization conventions, which are
        specified by the parameter :class:`~org.hipparchus.transform.DftNormalization`.
    
        The current implementation of the discrete Fourier transform as a fast Fourier transform requires the length of the data
        set to be a power of 2. This greatly simplifies and speeds up the code. Users can pad the data with zeros to meet this
        requirement. There are other flavors of FFT, for reference, see S. Winograd, *On computing the discrete Fourier
        transform*, Mathematics of Computation, 32 (1978), 175 - 199.
    
        Also see:
            :class:`~org.hipparchus.transform.DftNormalization`, :meth:`~serialized`
    """
    def __init__(self, dftNormalization: DftNormalization): ...
    @typing.overload
    def transform(self, doubleArray: typing.List[float], transformType: 'TransformType') -> typing.List[org.hipparchus.complex.Complex]:
        """
            Returns the (forward, inverse) transform of the specified real data set.
        
            Parameters:
                f (double[]): the real data array to be transformed
                type (:class:`~org.hipparchus.transform.TransformType`): the type of transform (forward, inverse) to be performed
        
            Returns:
                the complex transformed array
        
            Raises:
                :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`: if the length of the data array is not a power of two
        
            Returns the (forward, inverse) transform of the specified real function, sampled on the specified interval.
        
            Parameters:
                f (:class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`): the function to be sampled and transformed
                min (double): the (inclusive) lower bound for the interval
                max (double): the (exclusive) upper bound for the interval
                n (int): the number of sample points
                type (:class:`~org.hipparchus.transform.TransformType`): the type of transform (forward, inverse) to be performed
        
            Returns:
                the complex transformed array
        
            Raises:
                :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`: if the lower bound is greater than, or equal to the upper bound
                :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`: if the number of sample points :code:`n` is negative
                :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`: if the number of sample points :code:`n` is not a power of two
        
            Returns the (forward, inverse) transform of the specified complex data set.
        
            Parameters:
                f (:class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`[]): the complex data array to be transformed
                type (:class:`~org.hipparchus.transform.TransformType`): the type of transform (forward, inverse) to be performed
        
            Returns:
                the complex transformed array
        
            Raises:
                :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`: if the length of the data array is not a power of two
        
        
        """
        ...
    @typing.overload
    def transform(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float, int: int, transformType: 'TransformType') -> typing.List[org.hipparchus.complex.Complex]: ...
    @typing.overload
    def transform(self, complexArray: typing.List[org.hipparchus.complex.Complex], transformType: 'TransformType') -> typing.List[org.hipparchus.complex.Complex]: ...
    @staticmethod
    def transformInPlace(doubleArray: typing.List[typing.List[float]], dftNormalization: DftNormalization, transformType: 'TransformType') -> None:
        """
            Computes the standard transform of the specified complex data. The computation is done in place. The input data is laid
            out as follows
        
              - :code:`dataRI[0][i]` is the real part of the :code:`i`-th data point,
              - :code:`dataRI[1][i]` is the imaginary part of the :code:`i`-th data point.
        
        
            Parameters:
                dataRI (double[][]): the two dimensional array of real and imaginary parts of the data
                normalization (:class:`~org.hipparchus.transform.DftNormalization`): the normalization to be applied to the transformed data
                type (:class:`~org.hipparchus.transform.TransformType`): the type of transform (forward, inverse) to be performed
        
            Raises:
                :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`: if the number of rows of the specified array is not two, or the array is not rectangular
                :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`: if the number of data points is not a power of two
        
        
        """
        ...

class LocalizedFFTFormats(java.lang.Enum['LocalizedFFTFormats'], org.hipparchus.exception.Localizable):
    """
    public enum LocalizedFFTFormats extends :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.transform.LocalizedFFTFormats`> implements :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    FIRST_ELEMENT_NOT_ZERO: typing.ClassVar['LocalizedFFTFormats'] = ...
    NOT_POWER_OF_TWO: typing.ClassVar['LocalizedFFTFormats'] = ...
    NOT_POWER_OF_TWO_CONSIDER_PADDING: typing.ClassVar['LocalizedFFTFormats'] = ...
    NOT_POWER_OF_TWO_PLUS_ONE: typing.ClassVar['LocalizedFFTFormats'] = ...
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedFFTFormats':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['LocalizedFFTFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LocalizedFFTFormats c : LocalizedFFTFormats.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RealTransformer:
    """
    public interface RealTransformer
    
        Interface for one-dimensional data sets transformations producing real results.
    
        Such transforms include :class:`~org.hipparchus.transform.FastSineTransformer`,
        :class:`~org.hipparchus.transform.FastCosineTransformer` or :class:`~org.hipparchus.transform.FastHadamardTransformer`.
        :class:`~org.hipparchus.transform.FastFourierTransformer` is of a different kind and does not implement this interface
        since it produces :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus` results instead of real ones.
    """
    @typing.overload
    def transform(self, doubleArray: typing.List[float], transformType: 'TransformType') -> typing.List[float]: ...
    @typing.overload
    def transform(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float, int: int, transformType: 'TransformType') -> typing.List[float]: ...

class TransformType(java.lang.Enum['TransformType']):
    """
    public enum TransformType extends :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.transform.TransformType`>
    
        This enumeration defines the type of transform which is to be computed.
    """
    FORWARD: typing.ClassVar['TransformType'] = ...
    INVERSE: typing.ClassVar['TransformType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TransformType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['TransformType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (TransformType c : TransformType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TransformUtils:
    """
    public class TransformUtils extends :class:`~org.hipparchus.transform.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Useful functions for the implementation of various transforms.
    """
    @staticmethod
    def createComplexArray(doubleArray: typing.List[typing.List[float]]) -> typing.List[org.hipparchus.complex.Complex]: ...
    @staticmethod
    def createRealImaginaryArray(complexArray: typing.List[org.hipparchus.complex.Complex]) -> typing.List[typing.List[float]]:
        """
            Builds a new two dimensional array of :code:`double` filled with the real and imaginary parts of the specified
            :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus` numbers. In the returned array :code:`dataRI`,
            the data is laid out as follows
        
              - :code:`dataRI[0][i] = dataC[i].getReal()`,
              - :code:`dataRI[1][i] = dataC[i].getImaginary()`.
        
        
            Parameters:
                dataC (:class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`[]): the array of :class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus` data to be transformed
        
            Returns:
                a two dimensional array filled with the real and imaginary parts of the specified complex input
        
        
        """
        ...
    @staticmethod
    def exactLog2(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def scaleArray(doubleArray: typing.List[float], double2: float) -> typing.List[float]:
        """
            Multiply every component in the given real array by the given real number. The change is made in place.
        
            Parameters:
                f (double[]): the real array to be scaled
                d (double): the real scaling coefficient
        
            Returns:
                a reference to the scaled array
        
            Multiply every component in the given complex array by the given real number. The change is made in place.
        
            Parameters:
                f (:class:`~org.hipparchus.transform.https:.www.hipparchus.org.hipparchus`[]): the complex array to be scaled
                d (double): the real scaling coefficient
        
            Returns:
                a reference to the scaled array
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def scaleArray(complexArray: typing.List[org.hipparchus.complex.Complex], double: float) -> typing.List[org.hipparchus.complex.Complex]: ...

class FastCosineTransformer(RealTransformer, java.io.Serializable):
    def __init__(self, dctNormalization: DctNormalization): ...
    @typing.overload
    def transform(self, doubleArray: typing.List[float], transformType: TransformType) -> typing.List[float]: ...
    @typing.overload
    def transform(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float, int: int, transformType: TransformType) -> typing.List[float]: ...

class FastHadamardTransformer(RealTransformer, java.io.Serializable):
    def __init__(self): ...
    @typing.overload
    def transform(self, doubleArray: typing.List[float], transformType: TransformType) -> typing.List[float]: ...
    @typing.overload
    def transform(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float, int: int, transformType: TransformType) -> typing.List[float]: ...
    @typing.overload
    def transform(self, intArray: typing.List[int]) -> typing.List[int]: ...

class FastSineTransformer(RealTransformer, java.io.Serializable):
    def __init__(self, dstNormalization: DstNormalization): ...
    @typing.overload
    def transform(self, doubleArray: typing.List[float], transformType: TransformType) -> typing.List[float]: ...
    @typing.overload
    def transform(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float, int: int, transformType: TransformType) -> typing.List[float]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.transform")``.

    DctNormalization: typing.Type[DctNormalization]
    DftNormalization: typing.Type[DftNormalization]
    DstNormalization: typing.Type[DstNormalization]
    FastCosineTransformer: typing.Type[FastCosineTransformer]
    FastFourierTransformer: typing.Type[FastFourierTransformer]
    FastHadamardTransformer: typing.Type[FastHadamardTransformer]
    FastSineTransformer: typing.Type[FastSineTransformer]
    LocalizedFFTFormats: typing.Type[LocalizedFFTFormats]
    RealTransformer: typing.Type[RealTransformer]
    TransformType: typing.Type[TransformType]
    TransformUtils: typing.Type[TransformUtils]
