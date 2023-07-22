import java.io
import java.lang
import java.util
import typing



class Localizable(java.io.Serializable):
    """
    public interface Localizable extends :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Interface for localizable strings.
    """
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
            Gets the localized string.
        
            Parameters:
                locale (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): locale into which to get the string.
        
            Returns:
                the localized string or the source string if no localized version is available.
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
            Gets the source (non-localized) string.
        
            Returns:
                the source string.
        
        
        """
        ...

class LocalizedException:
    """
    public interface LocalizedException
    
        This interface specified methods implemented by localized exception classes.
    
        This interface has been copied from the interface with the same name from Orekit.
    """
    def getMessage(self, locale: java.util.Locale) -> str:
        """
            Gets the message in a specified locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): Locale in which the message should be translated
        
            Returns:
                localized message
        
        
        """
        ...
    def getParts(self) -> typing.List[typing.Any]:
        """
            Get the variable parts of the error message.
        
            Returns:
                a copy of the variable parts of the error message
        
        
        """
        ...
    def getSpecifier(self) -> Localizable:
        """
            Get the localizable specifier of the error message.
        
            Returns:
                localizable specifier of the error message
        
        
        """
        ...

class UTF8Control(java.util.ResourceBundle.Control):
    """
    public class UTF8Control extends :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.util.ResourceBundle.Control?is`
    
        Control class loading properties in UTF-8 encoding.
    
        This class has been very slightly adapted from BalusC answer to question: ` How to use UTF-8 in resource properties with
        ResourceBundle
        <http://stackoverflow.com/questions/4659929/how-to-use-utf-8-in-resource-properties-with-resourcebundle>`.
    """
    def __init__(self): ...
    def newBundle(self, string: str, locale: java.util.Locale, string2: str, classLoader: java.lang.ClassLoader, boolean: bool) -> java.util.ResourceBundle: ...

class DummyLocalizable(Localizable):
    """
    public class DummyLocalizable extends :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.exception.Localizable`
    
        Dummy implementation of the :class:`~org.hipparchus.exception.Localizable` interface, without localization.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
            Gets the localized string.
        
            Specified by:
                :meth:`~org.hipparchus.exception.Localizable.getLocalizedString` in
                interface :class:`~org.hipparchus.exception.Localizable`
        
            Parameters:
                locale (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): locale into which to get the string.
        
            Returns:
                the localized string or the source string if no localized version is available.
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
            Gets the source (non-localized) string.
        
            Specified by:
                :meth:`~org.hipparchus.exception.Localizable.getSourceString` in
                interface :class:`~org.hipparchus.exception.Localizable`
        
            Returns:
                the source string.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...

class LocalizedCoreFormats(java.lang.Enum['LocalizedCoreFormats'], Localizable):
    """
    public enum LocalizedCoreFormats extends :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.exception.LocalizedCoreFormats`> implements :class:`~org.hipparchus.exception.Localizable`
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    ARRAY_SIZE_EXCEEDS_MAX_VARIABLES: typing.ClassVar['LocalizedCoreFormats'] = ...
    ARRAY_SIZES_SHOULD_HAVE_DIFFERENCE_1: typing.ClassVar['LocalizedCoreFormats'] = ...
    ARRAY_SUMS_TO_ZERO: typing.ClassVar['LocalizedCoreFormats'] = ...
    AT_LEAST_ONE_COLUMN: typing.ClassVar['LocalizedCoreFormats'] = ...
    AT_LEAST_ONE_ROW: typing.ClassVar['LocalizedCoreFormats'] = ...
    BANDWIDTH: typing.ClassVar['LocalizedCoreFormats'] = ...
    BESSEL_FUNCTION_BAD_ARGUMENT: typing.ClassVar['LocalizedCoreFormats'] = ...
    BESSEL_FUNCTION_FAILED_CONVERGENCE: typing.ClassVar['LocalizedCoreFormats'] = ...
    BINOMIAL_INVALID_PARAMETERS_ORDER: typing.ClassVar['LocalizedCoreFormats'] = ...
    BINOMIAL_NEGATIVE_PARAMETER: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_COMPUTE_0TH_ROOT_OF_UNITY: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_COMPUTE_BETA_DENSITY_AT_0_FOR_SOME_ALPHA: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_COMPUTE_BETA_DENSITY_AT_1_FOR_SOME_BETA: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_COMPUTE_NTH_ROOT_FOR_NEGATIVE_N: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_DISCARD_NEGATIVE_NUMBER_OF_ELEMENTS: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_FORMAT_INSTANCE_AS_COMPLEX: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_FORMAT_OBJECT_TO_FRACTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_SUBSTITUTE_ELEMENT_FROM_EMPTY_ARRAY: typing.ClassVar['LocalizedCoreFormats'] = ...
    COLUMN_INDEX: typing.ClassVar['LocalizedCoreFormats'] = ...
    COMPLEX_CANNOT_BE_CONSIDERED_A_REAL_NUMBER: typing.ClassVar['LocalizedCoreFormats'] = ...
    CONSTRAINT: typing.ClassVar['LocalizedCoreFormats'] = ...
    CONTINUED_FRACTION_INFINITY_DIVERGENCE: typing.ClassVar['LocalizedCoreFormats'] = ...
    CONTINUED_FRACTION_NAN_DIVERGENCE: typing.ClassVar['LocalizedCoreFormats'] = ...
    CONTRACTION_CRITERIA_SMALLER_THAN_EXPANSION_FACTOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    CONTRACTION_CRITERIA_SMALLER_THAN_ONE: typing.ClassVar['LocalizedCoreFormats'] = ...
    CONVERGENCE_FAILED: typing.ClassVar['LocalizedCoreFormats'] = ...
    CUMULATIVE_PROBABILITY_RETURNED_NAN: typing.ClassVar['LocalizedCoreFormats'] = ...
    DERIVATION_ORDER_NOT_ALLOWED: typing.ClassVar['LocalizedCoreFormats'] = ...
    DIFFERENT_ROWS_LENGTHS: typing.ClassVar['LocalizedCoreFormats'] = ...
    DIGEST_NOT_INITIALIZED: typing.ClassVar['LocalizedCoreFormats'] = ...
    DIMENSIONS_MISMATCH_2x2: typing.ClassVar['LocalizedCoreFormats'] = ...
    DIMENSIONS_MISMATCH: typing.ClassVar['LocalizedCoreFormats'] = ...
    DISCRETE_CUMULATIVE_PROBABILITY_RETURNED_NAN: typing.ClassVar['LocalizedCoreFormats'] = ...
    DISTRIBUTION_NOT_LOADED: typing.ClassVar['LocalizedCoreFormats'] = ...
    DUPLICATED_ABSCISSA_DIVISION_BY_ZERO: typing.ClassVar['LocalizedCoreFormats'] = ...
    EMPTY_INTERPOLATION_SAMPLE: typing.ClassVar['LocalizedCoreFormats'] = ...
    EMPTY_POLYNOMIALS_COEFFICIENTS_ARRAY: typing.ClassVar['LocalizedCoreFormats'] = ...
    EMPTY_SELECTED_COLUMN_INDEX_ARRAY: typing.ClassVar['LocalizedCoreFormats'] = ...
    EMPTY_SELECTED_ROW_INDEX_ARRAY: typing.ClassVar['LocalizedCoreFormats'] = ...
    ENDPOINTS_NOT_AN_INTERVAL: typing.ClassVar['LocalizedCoreFormats'] = ...
    EVALUATION: typing.ClassVar['LocalizedCoreFormats'] = ...
    EXPANSION_FACTOR_SMALLER_THAN_ONE: typing.ClassVar['LocalizedCoreFormats'] = ...
    FACTORIAL_NEGATIVE_PARAMETER: typing.ClassVar['LocalizedCoreFormats'] = ...
    FAILED_BRACKETING: typing.ClassVar['LocalizedCoreFormats'] = ...
    FAILED_DECOMPOSITION: typing.ClassVar['LocalizedCoreFormats'] = ...
    FAILED_FRACTION_CONVERSION: typing.ClassVar['LocalizedCoreFormats'] = ...
    FIRST_COLUMNS_NOT_INITIALIZED_YET: typing.ClassVar['LocalizedCoreFormats'] = ...
    FIRST_ROWS_NOT_INITIALIZED_YET: typing.ClassVar['LocalizedCoreFormats'] = ...
    FRACTION_CONVERSION_OVERFLOW: typing.ClassVar['LocalizedCoreFormats'] = ...
    GCD_OVERFLOW_32_BITS: typing.ClassVar['LocalizedCoreFormats'] = ...
    GCD_OVERFLOW_64_BITS: typing.ClassVar['LocalizedCoreFormats'] = ...
    ILL_CONDITIONED_OPERATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    INDEX_LARGER_THAN_MAX: typing.ClassVar['LocalizedCoreFormats'] = ...
    INDEX_NOT_POSITIVE: typing.ClassVar['LocalizedCoreFormats'] = ...
    INDEX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_FINITE_NUMBER: typing.ClassVar['LocalizedCoreFormats'] = ...
    INFINITE_BOUND: typing.ClassVar['LocalizedCoreFormats'] = ...
    ARRAY_ELEMENT: typing.ClassVar['LocalizedCoreFormats'] = ...
    INFINITE_ARRAY_ELEMENT: typing.ClassVar['LocalizedCoreFormats'] = ...
    INFINITE_VALUE_CONVERSION: typing.ClassVar['LocalizedCoreFormats'] = ...
    INITIAL_CAPACITY_NOT_POSITIVE: typing.ClassVar['LocalizedCoreFormats'] = ...
    INITIAL_COLUMN_AFTER_FINAL_COLUMN: typing.ClassVar['LocalizedCoreFormats'] = ...
    INITIAL_ROW_AFTER_FINAL_ROW: typing.ClassVar['LocalizedCoreFormats'] = ...
    INSUFFICIENT_DATA: typing.ClassVar['LocalizedCoreFormats'] = ...
    INSUFFICIENT_DIMENSION: typing.ClassVar['LocalizedCoreFormats'] = ...
    DIMENSION: typing.ClassVar['LocalizedCoreFormats'] = ...
    INSUFFICIENT_OBSERVED_POINTS_IN_SAMPLE: typing.ClassVar['LocalizedCoreFormats'] = ...
    INSUFFICIENT_ROWS_AND_COLUMNS: typing.ClassVar['LocalizedCoreFormats'] = ...
    INTERNAL_ERROR: typing.ClassVar['LocalizedCoreFormats'] = ...
    INVALID_MAX_ITERATIONS: typing.ClassVar['LocalizedCoreFormats'] = ...
    INVALID_ROUNDING_METHOD: typing.ClassVar['LocalizedCoreFormats'] = ...
    ITERATIONS: typing.ClassVar['LocalizedCoreFormats'] = ...
    LCM_OVERFLOW_32_BITS: typing.ClassVar['LocalizedCoreFormats'] = ...
    LCM_OVERFLOW_64_BITS: typing.ClassVar['LocalizedCoreFormats'] = ...
    LOWER_BOUND_NOT_BELOW_UPPER_BOUND: typing.ClassVar['LocalizedCoreFormats'] = ...
    LOWER_ENDPOINT_ABOVE_UPPER_ENDPOINT: typing.ClassVar['LocalizedCoreFormats'] = ...
    EVALUATIONS: typing.ClassVar['LocalizedCoreFormats'] = ...
    MAX_COUNT_EXCEEDED: typing.ClassVar['LocalizedCoreFormats'] = ...
    NAN_ELEMENT_AT_INDEX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NAN_VALUE_CONVERSION: typing.ClassVar['LocalizedCoreFormats'] = ...
    NEGATIVE_DEFINITE_MATRIX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NEGATIVE_COMPLEX_MODULE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NEGATIVE_ELEMENT_AT_INDEX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_OF_SUCCESSES: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_OF_INTERPOLATION_POINTS: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_OF_TRIALS: typing.ClassVar['LocalizedCoreFormats'] = ...
    ROBUSTNESS_ITERATIONS: typing.ClassVar['LocalizedCoreFormats'] = ...
    START_POSITION: typing.ClassVar['LocalizedCoreFormats'] = ...
    NON_CONVERGENT_CONTINUED_FRACTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    NON_SQUARE_MATRIX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NORM: typing.ClassVar['LocalizedCoreFormats'] = ...
    NORMALIZE_INFINITE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NORMALIZE_NAN: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_DECREASING_SEQUENCE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_ENOUGH_POINTS_IN_SPLINE_PARTITION: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_INCREASING_SEQUENCE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_POSITIVE_DEFINITE_MATRIX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NON_POSITIVE_DEFINITE_OPERATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    NON_SELF_ADJOINT_OPERATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    NON_SQUARE_OPERATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    DEGREES_OF_FREEDOM: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_POSITIVE_EXPONENT: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_OF_ELEMENTS_SHOULD_BE_POSITIVE: typing.ClassVar['LocalizedCoreFormats'] = ...
    BASE: typing.ClassVar['LocalizedCoreFormats'] = ...
    EXPONENT: typing.ClassVar['LocalizedCoreFormats'] = ...
    LENGTH: typing.ClassVar['LocalizedCoreFormats'] = ...
    MEAN: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_POSITIVE_NUMBER_OF_SAMPLES: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_OF_SAMPLES: typing.ClassVar['LocalizedCoreFormats'] = ...
    PERMUTATION_SIZE: typing.ClassVar['LocalizedCoreFormats'] = ...
    POPULATION_SIZE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_POSITIVE_SCALE: typing.ClassVar['LocalizedCoreFormats'] = ...
    SCALE: typing.ClassVar['LocalizedCoreFormats'] = ...
    SHAPE: typing.ClassVar['LocalizedCoreFormats'] = ...
    STANDARD_DEVIATION: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_POSITIVE_WINDOW_SIZE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_STRICTLY_DECREASING_SEQUENCE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_STRICTLY_INCREASING_SEQUENCE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NON_SYMMETRIC_MATRIX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NO_CONVERGENCE_WITH_ANY_START_POINT: typing.ClassVar['LocalizedCoreFormats'] = ...
    NO_DATA: typing.ClassVar['LocalizedCoreFormats'] = ...
    NO_OPTIMUM_COMPUTED_YET: typing.ClassVar['LocalizedCoreFormats'] = ...
    NAN_NOT_ALLOWED: typing.ClassVar['LocalizedCoreFormats'] = ...
    NULL_NOT_ALLOWED: typing.ClassVar['LocalizedCoreFormats'] = ...
    ARRAY_ZERO_LENGTH_OR_NULL_NOT_ALLOWED: typing.ClassVar['LocalizedCoreFormats'] = ...
    DENOMINATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    DENOMINATOR_FORMAT: typing.ClassVar['LocalizedCoreFormats'] = ...
    FRACTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    FUNCTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    IMAGINARY_FORMAT: typing.ClassVar['LocalizedCoreFormats'] = ...
    INPUT_ARRAY: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMERATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMERATOR_FORMAT: typing.ClassVar['LocalizedCoreFormats'] = ...
    REAL_FORMAT: typing.ClassVar['LocalizedCoreFormats'] = ...
    WHOLE_FORMAT: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_TOO_LARGE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_TOO_SMALL: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_TOO_LARGE_BOUND_EXCLUDED: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_TOO_SMALL_BOUND_EXCLUDED: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_OF_SUCCESS_LARGER_THAN_POPULATION_SIZE: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMERATOR_OVERFLOW_AFTER_MULTIPLY: typing.ClassVar['LocalizedCoreFormats'] = ...
    OBSERVED_COUNTS_BOTTH_ZERO_FOR_ENTRY: typing.ClassVar['LocalizedCoreFormats'] = ...
    OUT_OF_RANGE_ROOT_OF_UNITY_INDEX: typing.ClassVar['LocalizedCoreFormats'] = ...
    OUT_OF_RANGE: typing.ClassVar['LocalizedCoreFormats'] = ...
    OUT_OF_RANGE_SIMPLE: typing.ClassVar['LocalizedCoreFormats'] = ...
    OUT_OF_RANGE_LEFT: typing.ClassVar['LocalizedCoreFormats'] = ...
    OVERFLOW: typing.ClassVar['LocalizedCoreFormats'] = ...
    OVERFLOW_IN_FRACTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    OVERFLOW_IN_ADDITION: typing.ClassVar['LocalizedCoreFormats'] = ...
    OVERFLOW_IN_SUBTRACTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    OVERFLOW_IN_MULTIPLICATION: typing.ClassVar['LocalizedCoreFormats'] = ...
    PERMUTATION_EXCEEDS_N: typing.ClassVar['LocalizedCoreFormats'] = ...
    POLYNOMIAL: typing.ClassVar['LocalizedCoreFormats'] = ...
    ROOTS_OF_UNITY_NOT_COMPUTED_YET: typing.ClassVar['LocalizedCoreFormats'] = ...
    ROW_INDEX: typing.ClassVar['LocalizedCoreFormats'] = ...
    NOT_BRACKETING_INTERVAL: typing.ClassVar['LocalizedCoreFormats'] = ...
    START_POINT_NOT_IN_INTERVAL: typing.ClassVar['LocalizedCoreFormats'] = ...
    SAMPLE_SIZE_EXCEEDS_COLLECTION_SIZE: typing.ClassVar['LocalizedCoreFormats'] = ...
    SAMPLE_SIZE_LARGER_THAN_POPULATION_SIZE: typing.ClassVar['LocalizedCoreFormats'] = ...
    SIMPLE_MESSAGE: typing.ClassVar['LocalizedCoreFormats'] = ...
    SINGULAR_MATRIX: typing.ClassVar['LocalizedCoreFormats'] = ...
    SINGULAR_OPERATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    SUBARRAY_ENDS_AFTER_ARRAY_END: typing.ClassVar['LocalizedCoreFormats'] = ...
    TOO_LARGE_CUTOFF_SINGULAR_VALUE: typing.ClassVar['LocalizedCoreFormats'] = ...
    TOO_MANY_ELEMENTS_TO_DISCARD_FROM_ARRAY: typing.ClassVar['LocalizedCoreFormats'] = ...
    UNKNOWN_MODE: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_PARSE_AS_TYPE: typing.ClassVar['LocalizedCoreFormats'] = ...
    CANNOT_PARSE: typing.ClassVar['LocalizedCoreFormats'] = ...
    UNSUPPORTED_OPERATION: typing.ClassVar['LocalizedCoreFormats'] = ...
    ARITHMETIC_EXCEPTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    ILLEGAL_STATE: typing.ClassVar['LocalizedCoreFormats'] = ...
    USER_EXCEPTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    URL_CONTAINS_NO_DATA: typing.ClassVar['LocalizedCoreFormats'] = ...
    VECTOR_MUST_HAVE_AT_LEAST_ONE_ELEMENT: typing.ClassVar['LocalizedCoreFormats'] = ...
    WEIGHT_AT_LEAST_ONE_NON_ZERO: typing.ClassVar['LocalizedCoreFormats'] = ...
    WRONG_NUMBER_OF_POINTS: typing.ClassVar['LocalizedCoreFormats'] = ...
    NUMBER_OF_POINTS: typing.ClassVar['LocalizedCoreFormats'] = ...
    ZERO_DENOMINATOR: typing.ClassVar['LocalizedCoreFormats'] = ...
    ZERO_DENOMINATOR_IN_FRACTION: typing.ClassVar['LocalizedCoreFormats'] = ...
    ZERO_FRACTION_TO_DIVIDE_BY: typing.ClassVar['LocalizedCoreFormats'] = ...
    ZERO_NORM: typing.ClassVar['LocalizedCoreFormats'] = ...
    ZERO_NOT_ALLOWED: typing.ClassVar['LocalizedCoreFormats'] = ...
    ZERO_STATE_SIZE: typing.ClassVar['LocalizedCoreFormats'] = ...
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
            Gets the localized string.
        
            Specified by:
                :meth:`~org.hipparchus.exception.Localizable.getLocalizedString` in
                interface :class:`~org.hipparchus.exception.Localizable`
        
            Parameters:
                locale (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): locale into which to get the string.
        
            Returns:
                the localized string or the source string if no localized version is available.
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
            Gets the source (non-localized) string.
        
            Specified by:
                :meth:`~org.hipparchus.exception.Localizable.getSourceString` in
                interface :class:`~org.hipparchus.exception.Localizable`
        
            Returns:
                the source string.
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedCoreFormats':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['LocalizedCoreFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LocalizedCoreFormats c : LocalizedCoreFormats.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class MathRuntimeException(java.lang.RuntimeException, LocalizedException):
    """
    public class MathRuntimeException extends :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.RuntimeException?is` implements :class:`~org.hipparchus.exception.LocalizedException`
    
        All exceptions thrown by the Hipparchus code inherit from this class.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, localizable: Localizable, *object: typing.Any): ...
    @typing.overload
    def __init__(self, localizable: Localizable, *object: typing.Any): ...
    @typing.overload
    @staticmethod
    def createInternalError() -> 'MathRuntimeException':
        """
            Create an exception for an internal error.
        
            Returns:
                a new runtime exception indicating an internal error
        
        """
        ...
    @typing.overload
    @staticmethod
    def createInternalError(throwable: java.lang.Throwable) -> 'MathRuntimeException':
        """
            Create an exception for an internal error.
        
            Parameters:
                cause (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable?is`): root cause
        
            Returns:
                a new runtime exception, indicating an internal error and wrapping the given throwable
        
        
        """
        ...
    def getLocalizedMessage(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable.html?is` in
                class :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable?is`
        
        
        """
        ...
    @typing.overload
    def getMessage(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable.html?is` in
                class :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable?is`
        
        
        """
        ...
    @typing.overload
    def getMessage(self, locale: java.util.Locale) -> str:
        """
            Gets the message in a specified locale.
        
            Specified by:
                :meth:`~org.hipparchus.exception.LocalizedException.getMessage` in
                interface :class:`~org.hipparchus.exception.LocalizedException`
        
            Parameters:
                locale (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): Locale in which the message should be translated
        
            Returns:
                localized message
        
        """
        ...
    def getParts(self) -> typing.List[typing.Any]:
        """
            Get the variable parts of the error message.
        
            Specified by:
                :meth:`~org.hipparchus.exception.LocalizedException.getParts` in
                interface :class:`~org.hipparchus.exception.LocalizedException`
        
            Returns:
                a copy of the variable parts of the error message
        
        
        """
        ...
    def getSpecifier(self) -> Localizable:
        """
            Get the localizable specifier of the error message.
        
            Specified by:
                :meth:`~org.hipparchus.exception.LocalizedException.getSpecifier` in
                interface :class:`~org.hipparchus.exception.LocalizedException`
        
            Returns:
                localizable specifier of the error message
        
        
        """
        ...

class NullArgumentException(java.lang.NullPointerException, LocalizedException):
    """
    public class NullArgumentException extends :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is` implements :class:`~org.hipparchus.exception.LocalizedException`
    
        All conditions checks that fail due to a :code:`null` argument must throw this exception. This class is meant to signal
        a precondition violation ("null is an illegal argument") and so does not extend the standard
        :code:`NullPointerException`. Propagation of :code:`NullPointerException` from within Hipparchus is construed to be a
        bug.
    
        Note: from 1.0 onwards, this class extends
        :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is` instead of
        :class:`~org.hipparchus.exception.MathIllegalArgumentException`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, localizable: Localizable, *object: typing.Any): ...
    def getLocalizedMessage(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable.html?is` in
                class :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable?is`
        
        
        """
        ...
    @typing.overload
    def getMessage(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable.html?is` in
                class :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.Throwable?is`
        
        
        """
        ...
    @typing.overload
    def getMessage(self, locale: java.util.Locale) -> str:
        """
            Gets the message in a specified locale.
        
            Specified by:
                :meth:`~org.hipparchus.exception.LocalizedException.getMessage` in
                interface :class:`~org.hipparchus.exception.LocalizedException`
        
            Parameters:
                locale (:class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): Locale in which the message should be translated
        
            Returns:
                localized message
        
        """
        ...
    def getParts(self) -> typing.List[typing.Any]:
        """
            Get the variable parts of the error message.
        
            Specified by:
                :meth:`~org.hipparchus.exception.LocalizedException.getParts` in
                interface :class:`~org.hipparchus.exception.LocalizedException`
        
            Returns:
                a copy of the variable parts of the error message
        
        
        """
        ...
    def getSpecifier(self) -> Localizable:
        """
            Get the localizable specifier of the error message.
        
            Specified by:
                :meth:`~org.hipparchus.exception.LocalizedException.getSpecifier` in
                interface :class:`~org.hipparchus.exception.LocalizedException`
        
            Returns:
                localizable specifier of the error message
        
        
        """
        ...

class MathIllegalArgumentException(MathRuntimeException):
    """
    public class MathIllegalArgumentException extends :class:`~org.hipparchus.exception.MathRuntimeException`
    
        Base class for all preconditions violation exceptions. In most cases, this class should not be instantiated directly: it
        should serve as a base class to create all the exceptions that have the semantics of the standard
        :class:`~org.hipparchus.exception.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, localizable: Localizable, *object: typing.Any): ...
    @typing.overload
    def __init__(self, localizable: Localizable, *object: typing.Any): ...

class MathIllegalStateException(MathRuntimeException):
    """
    public class MathIllegalStateException extends :class:`~org.hipparchus.exception.MathRuntimeException`
    
        Base class for all exceptions that signal that the process throwing the exception is in a state that does not comply
        with the set of states that it is designed to be in.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, localizable: Localizable, *object: typing.Any): ...
    @typing.overload
    def __init__(self, localizable: Localizable, *object: typing.Any): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.exception")``.

    DummyLocalizable: typing.Type[DummyLocalizable]
    Localizable: typing.Type[Localizable]
    LocalizedCoreFormats: typing.Type[LocalizedCoreFormats]
    LocalizedException: typing.Type[LocalizedException]
    MathIllegalArgumentException: typing.Type[MathIllegalArgumentException]
    MathIllegalStateException: typing.Type[MathIllegalStateException]
    MathRuntimeException: typing.Type[MathRuntimeException]
    NullArgumentException: typing.Type[NullArgumentException]
    UTF8Control: typing.Type[UTF8Control]
