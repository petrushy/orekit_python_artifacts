import java.io
import java.lang
import java.util
import org.hipparchus.exception
import org.hipparchus.stat.correlation
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.fitting
import org.hipparchus.stat.inference
import org.hipparchus.stat.interval
import org.hipparchus.stat.ranking
import org.hipparchus.stat.regression
import typing



_Frequency__T = typing.TypeVar('_Frequency__T', bound=java.lang.Comparable)  # <T>
class Frequency(java.io.Serializable, typing.Generic[_Frequency__T]):
    """
    public class Frequency<T extends Comparable<T>> extends Object implements Serializable
    
        Maintains a frequency distribution of Comparable values.
    
        The values are ordered using the default (natural order), unless a :code:`Comparator` is supplied in the constructor.
    
        Also see:
            :class:`~org.hipparchus.stat.LongFrequency`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, comparator: typing.Union[java.util.Comparator[_Frequency__T], typing.Callable[[_Frequency__T, _Frequency__T], int]]): ...
    def addValue(self, t: _Frequency__T) -> None:
        """
            Adds 1 to the frequency count for v.
        
            Parameters:
                v (:class:`~org.hipparchus.stat.Frequency`): the value to add.
        
        
        """
        ...
    def clear(self) -> None:
        """
            Clears the frequency table
        
        """
        ...
    def entrySetIterator(self) -> java.util.Iterator[java.util.Map.Entry[_Frequency__T, int]]: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getCount(self, t: _Frequency__T) -> int:
        """
            Returns the number of values equal to v. Returns 0 if the value is not comparable.
        
            Parameters:
                v (:class:`~org.hipparchus.stat.Frequency`): the value to lookup.
        
            Returns:
                the frequency of v.
        
        
        """
        ...
    def getCumFreq(self, t: _Frequency__T) -> int:
        """
            Returns the cumulative frequency of values less than or equal to v.
        
            Parameters:
                v (:class:`~org.hipparchus.stat.Frequency`): the value to lookup.
        
            Returns:
                the proportion of values equal to v
        
        
        """
        ...
    def getCumPct(self, t: _Frequency__T) -> float:
        """
            Returns the cumulative percentage of values less than or equal to v (as a proportion between 0 and 1).
        
            Returns :code:`Double.NaN` if no values have been added.
        
            Parameters:
                v (:class:`~org.hipparchus.stat.Frequency`): the value to lookup
        
            Returns:
                the proportion of values less than or equal to v
        
        
        """
        ...
    def getMode(self) -> java.util.List[_Frequency__T]: ...
    def getPct(self, t: _Frequency__T) -> float:
        """
            Returns the percentage of values that are equal to v (as a proportion between 0 and 1).
        
            Returns :code:`Double.NaN` if no values have been added.
        
            Parameters:
                v (:class:`~org.hipparchus.stat.Frequency`): the value to lookup
        
            Returns:
                the proportion of values equal to v
        
        
        """
        ...
    def getSumFreq(self) -> int:
        """
            Returns the sum of all frequencies.
        
            Returns:
                the total frequency count.
        
        
        """
        ...
    def getUniqueCount(self) -> int:
        """
            Returns the number of values in the frequency table.
        
            Returns:
                the number of unique values that have been added to the frequency table.
        
            Also see:
                :meth:`~org.hipparchus.stat.Frequency.valuesIterator`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def incrementValue(self, t: _Frequency__T, long: int) -> None:
        """
            Increments the frequency count for v.
        
            Parameters:
                v (:class:`~org.hipparchus.stat.Frequency`): the value to add.
                increment (long): the amount by which the value should be incremented
        
        
        """
        ...
    @typing.overload
    def merge(self, collection: typing.Union[java.util.Collection['Frequency'[_Frequency__T]], typing.Sequence['Frequency'[_Frequency__T]], typing.Set['Frequency'[_Frequency__T]]]) -> None: ...
    @typing.overload
    def merge(self, frequency: 'Frequency'[_Frequency__T]) -> None: ...
    def toString(self) -> str:
        """
            Return a string representation of this frequency distribution.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation.
        
        
        """
        ...
    def valuesIterator(self) -> java.util.Iterator[_Frequency__T]: ...

class LocalizedStatFormats(java.lang.Enum['LocalizedStatFormats'], org.hipparchus.exception.Localizable):
    """
    public enum LocalizedStatFormats extends Enum<:class:`~org.hipparchus.stat.LocalizedStatFormats`> implements Localizable
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    TIES_ARE_NOT_ALLOWED: typing.ClassVar['LocalizedStatFormats'] = ...
    INSUFFICIENT_DATA_FOR_T_STATISTIC: typing.ClassVar['LocalizedStatFormats'] = ...
    NOT_ENOUGH_DATA_REGRESSION: typing.ClassVar['LocalizedStatFormats'] = ...
    INVALID_REGRESSION_OBSERVATION: typing.ClassVar['LocalizedStatFormats'] = ...
    NOT_ENOUGH_DATA_FOR_NUMBER_OF_PREDICTORS: typing.ClassVar['LocalizedStatFormats'] = ...
    NOT_SUPPORTED_NAN_STRATEGY: typing.ClassVar['LocalizedStatFormats'] = ...
    NO_REGRESSORS: typing.ClassVar['LocalizedStatFormats'] = ...
    COVARIANCE_MATRIX: typing.ClassVar['LocalizedStatFormats'] = ...
    OUT_OF_BOUNDS_QUANTILE_VALUE: typing.ClassVar['LocalizedStatFormats'] = ...
    OUT_OF_BOUNDS_CONFIDENCE_LEVEL: typing.ClassVar['LocalizedStatFormats'] = ...
    OUT_OF_BOUND_SIGNIFICANCE_LEVEL: typing.ClassVar['LocalizedStatFormats'] = ...
    SIGNIFICANCE_LEVEL: typing.ClassVar['LocalizedStatFormats'] = ...
    TOO_MANY_REGRESSORS: typing.ClassVar['LocalizedStatFormats'] = ...
    TWO_OR_MORE_CATEGORIES_REQUIRED: typing.ClassVar['LocalizedStatFormats'] = ...
    TWO_OR_MORE_VALUES_IN_CATEGORY_REQUIRED: typing.ClassVar['LocalizedStatFormats'] = ...
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedStatFormats':
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
    def values() -> typing.List['LocalizedStatFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LocalizedStatFormats c : LocalizedStatFormats.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StatUtils:
    """
    public final class StatUtils extends Object
    
        StatUtils provides static methods for computing statistics based on data stored in double[] arrays.
    """
    @typing.overload
    @staticmethod
    def geometricMean(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def geometricMean(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def max(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def max(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def mean(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def mean(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @staticmethod
    def meanDifference(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def min(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def min(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def mode(doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def mode(doubleArray: typing.List[float], int: int, int2: int) -> typing.List[float]:
        """
            Returns the sample mode(s).
        
            The mode is the most frequently occurring value in the sample. If there is a unique value with maximum frequency, this
            value is returned as the only element of the output array. Otherwise, the returned array contains the maximum frequency
            elements in increasing order.
        
            For example, if :code:`sample` is {0, 12, 5, 6, 0, 13, 5, 17}, the returned array will have length two, with 0 in the
            first element and 5 in the second.
        
            NaN values are ignored when computing the mode - i.e., NaNs will never appear in the output array. If the sample
            includes only NaNs or has length 0, an empty array is returned.
        
            Parameters:
                sample (double[]): input data
                begin (int): index (0-based) of the first array element to include
                length (int): the number of elements to include
        
            Returns:
                array of array of the most frequently occurring element(s) sorted in ascending order.
        
            Raises:
                : if the indices are invalid or the array is null
        
        
        """
        ...
    @staticmethod
    def normalize(doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Normalize (standardize) the sample, so it is has a mean of 0 and a standard deviation of 1.
        
            Parameters:
                sample (double...): Sample to normalize.
        
            Returns:
                normalized (standardized) sample.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def percentile(doubleArray: typing.List[float], double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def percentile(doubleArray: typing.List[float], int: int, int2: int, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(doubleArray: typing.List[float], double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(doubleArray: typing.List[float], double2: float, int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def product(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def product(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def sum(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def sum(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @staticmethod
    def sumDifference(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def sumLog(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def sumLog(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def sumSq(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def sumSq(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def variance(doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def variance(doubleArray: typing.List[float], double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def variance(doubleArray: typing.List[float], double2: float, int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def variance(doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @staticmethod
    def varianceDifference(doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> float: ...

class LongFrequency(Frequency[int]):
    """
    public class LongFrequency extends :class:`~org.hipparchus.stat.Frequency`<Long>
    
        Maintains a frequency distribution of Long values.
    
        Accepts byte, short, int, long primitive or Integer and Long values.
    
        Integer values (byte, short, int, long, Integer, Long) are not distinguished by type, i.e.
        :code:`addValue(Long.valueOf(2)), addValue(2), addValue(2L)` all have the same effect (similarly for arguments to
        :code:`getCount()` etc.).
    
        NOTE: byte and short values will be implicitly converted to int values by the compiler, thus there are no explicit
        overloaded methods for these primitive types.
    
        The values are ordered using the default (natural order), unless a :code:`Comparator` is supplied in the constructor.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, comparator: typing.Union[java.util.Comparator[int], typing.Callable[[int, int], int]]): ...
    @typing.overload
    def addValue(self, t: java.lang.Comparable) -> None:
        """
            Adds 1 to the frequency count for v.
        
            Parameters:
                v (int): the value to add.
        
        
        """
        ...
    @typing.overload
    def addValue(self, int: int) -> None: ...
    @typing.overload
    def getCount(self, t: java.lang.Comparable) -> int:
        """
            Returns the number of values equal to v.
        
            Parameters:
                v (int): the value to lookup.
        
            Returns:
                the frequency of v.
        
        
        """
        ...
    @typing.overload
    def getCount(self, int: int) -> int: ...
    @typing.overload
    def getCumFreq(self, t: java.lang.Comparable) -> int:
        """
            Returns the cumulative frequency of values less than or equal to v.
        
            Parameters:
                v (int): the value to lookup.
        
            Returns:
                the proportion of values equal to v
        
        
        """
        ...
    @typing.overload
    def getCumFreq(self, int: int) -> int: ...
    @typing.overload
    def getCumPct(self, t: java.lang.Comparable) -> float:
        """
            Returns the cumulative percentage of values less than or equal to v (as a proportion between 0 and 1).
        
            Returns :code:`Double.NaN` if no values have been added.
        
            Parameters:
                v (int): the value to lookup
        
            Returns:
                the proportion of values less than or equal to v
        
        
        """
        ...
    @typing.overload
    def getCumPct(self, int: int) -> float: ...
    @typing.overload
    def getPct(self, t: java.lang.Comparable) -> float:
        """
            Returns the percentage of values that are equal to v (as a proportion between 0 and 1).
        
            Returns :code:`Double.NaN` if no values have been added.
        
            Parameters:
                v (int): the value to lookup
        
            Returns:
                the proportion of values equal to v
        
        
        """
        ...
    @typing.overload
    def getPct(self, int: int) -> float: ...
    @typing.overload
    def incrementValue(self, t: java.lang.Comparable, long: int) -> None:
        """
            Increments the frequency count for v.
        
            Parameters:
                v (int): the value to add.
                increment (long): the amount by which the value should be incremented
        
        
        """
        ...
    @typing.overload
    def incrementValue(self, int: int, long: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat")``.

    Frequency: typing.Type[Frequency]
    LocalizedStatFormats: typing.Type[LocalizedStatFormats]
    LongFrequency: typing.Type[LongFrequency]
    StatUtils: typing.Type[StatUtils]
    correlation: org.hipparchus.stat.correlation.__module_protocol__
    descriptive: org.hipparchus.stat.descriptive.__module_protocol__
    fitting: org.hipparchus.stat.fitting.__module_protocol__
    inference: org.hipparchus.stat.inference.__module_protocol__
    interval: org.hipparchus.stat.interval.__module_protocol__
    ranking: org.hipparchus.stat.ranking.__module_protocol__
    regression: org.hipparchus.stat.regression.__module_protocol__
