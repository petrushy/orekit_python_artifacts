
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus.exception
import org.hipparchus.stat.correlation
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.fitting
import org.hipparchus.stat.inference
import org.hipparchus.stat.interval
import org.hipparchus.stat.projection
import org.hipparchus.stat.ranking
import org.hipparchus.stat.regression
import typing



_Frequency__T = typing.TypeVar('_Frequency__T', bound=java.lang.Comparable)  # <T>
class Frequency(java.io.Serializable, typing.Generic[_Frequency__T]):
    """
    Maintains a frequency distribution of Comparable values.
    
    The values are ordered using the default (natural order), unless a Comparator is supplied in the constructor.
    
    Also see:
        LongFrequency, serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, comparator: typing.Union[java.util.Comparator[_Frequency__T], typing.Callable[[_Frequency__T, _Frequency__T], int]]): ...
    def addValue(self, v: _Frequency__T) -> None:
        """
        Adds 1 to the frequency count for v.
        
        Parameters:
            v (Frequency): the value to add.
        
        
        """
        ...
    def clear(self) -> None:
        """
        Clears the frequency table
        """
        ...
    def entrySetIterator(self) -> java.util.Iterator[java.util.Map.Entry[_Frequency__T, int]]:
        """
        Return an Iterator over the set of keys and values that have been added. Using the entry set to iterate is more efficient in the case where you need to access respective counts as well as values, since it doesn't require a "get" for every key...the value is provided in the Map.Entry.
        
        Returns:
            entry set Iterator
        
        
        """
        ...
    def equals(self, obj: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getCount(self, v: _Frequency__T) -> int:
        """
        Returns the number of values equal to v. Returns 0 if the value is not comparable.
        
        Parameters:
            v (Frequency): the value to lookup.
        
        Returns:
            the frequency of v.
        
        
        """
        ...
    def getCumFreq(self, v: _Frequency__T) -> int:
        """
        Returns the cumulative frequency of values less than or equal to v.
        
        Parameters:
            v (Frequency): the value to lookup.
        
        Returns:
            the proportion of values equal to v
        
        
        """
        ...
    def getCumPct(self, v: _Frequency__T) -> float:
        """
        Returns the cumulative percentage of values less than or equal to v (as a proportion between 0 and 1).
        
        Returns NaN if no values have been added.
        
        Parameters:
            v (Frequency): the value to lookup
        
        Returns:
            the proportion of values less than or equal to v
        
        
        """
        ...
    def getMode(self) -> java.util.List[_Frequency__T]:
        """
        Returns the mode value(s) in comparator order.
        
        Returns:
            a list containing the value(s) which appear most often.
        
        
        """
        ...
    def getPct(self, v: _Frequency__T) -> float:
        """
        Returns the percentage of values that are equal to v (as a proportion between 0 and 1).
        
        Returns NaN if no values have been added.
        
        Parameters:
            v (Frequency): the value to lookup
        
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
            valuesIterator
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def incrementValue(self, v: _Frequency__T, increment: int) -> None:
        """
        Increments the frequency count for v.
        
        Parameters:
            v (Frequency): the value to add.
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
        
        Overrides: Object in class Object
        
        Returns:
            a string representation.
        
        
        """
        ...
    def valuesIterator(self) -> java.util.Iterator[_Frequency__T]:
        """
        Returns an Iterator over the set of values that have been added.
        
        Returns:
            values Iterator
        
        
        """
        ...

class LocalizedStatFormats(java.lang.Enum['LocalizedStatFormats'], org.hipparchus.exception.Localizable):
    """
    Enumeration for localized messages formats used in exceptions messages.
    
    The constants in this enumeration represent the available formats as localized strings. These formats are intended to be localized using simple properties files, using the constant name as the key and the property value as the message format. The source English format is provided in the constants themselves to serve both as a reminder for developers to understand the parameters needed by each format, as a basis for translators to create localized properties files, and as a default format if some translation is missing.
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
    ILLEGAL_STATE_PCA: typing.ClassVar['LocalizedStatFormats'] = ...
    @typing.overload
    def getLocalizedString(self, string: str, string2: str, locale: java.util.Locale) -> str: ...
    @typing.overload
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        Specified by: hipparchus in interface hipparchus
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        Specified by: hipparchus in interface hipparchus
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'LocalizedStatFormats':
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
    def values() -> typing.MutableSequence['LocalizedStatFormats']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (LocalizedStatFormats c : LocalizedStatFormats.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StatUtils:
    """
    StatUtils provides static methods for computing statistics based on data stored in double[] arrays.
    """
    @typing.overload
    @staticmethod
    def geometricMean(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def geometricMean(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def max(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def max(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def mean(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def mean(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @staticmethod
    def meanDifference(sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Returns the mean of the (signed) differences between corresponding elements of the input arrays -- i.e., sum(sample1[i]
        - sample2[i]) / sample1.length.
        
        Parameters:
            sample1 (double[]): the first array
            sample2 (double[]): the second array
        
        Returns:
            mean of paired differences
        
        Raises:
            hipparchus: if the arrays do not have the same (positive) length.
            hipparchus: if the sample arrays are empty.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def min(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def min(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def mode(*sample: float) -> typing.MutableSequence[float]: ...
    @typing.overload
    @staticmethod
    def mode(sample: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> typing.MutableSequence[float]:
        """
        The mode is the most frequently occurring value in the sample. If there is a unique value with maximum frequency, this value is returned as the only element of the output array. Otherwise, the returned array contains the maximum frequency elements in increasing order.
        
        For example, if sample is {0, 12, 5, 6, 0, 13, 5, 17}, the returned array will have length two, with 0 in the first element and 5 in the second.
        
        NaN values are ignored when computing the mode - i.e., NaNs will never appear in the output array. If the sample includes only NaNs or has length 0, an empty array is returned.
        
        Parameters:
            sample (double[]): input data
            begin (int): index (0-based) of the first array element to include
            length (int): the number of elements to include
        
        Returns:
            array of array of the most frequently occurring element(s) sorted in ascending order.
        
        Raises:
            hipparchus: if the indices are invalid or the array is null
        
        
        """
        ...
    @staticmethod
    def normalize(*sample: float) -> typing.MutableSequence[float]:
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
    def percentile(values: typing.Union[typing.List[float], jpype.JArray], p: float) -> float: ...
    @typing.overload
    @staticmethod
    def percentile(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int, p: float) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(values: typing.Union[typing.List[float], jpype.JArray], mean: float) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(values: typing.Union[typing.List[float], jpype.JArray], mean: float, begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def populationVariance(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def product(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def product(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def sum(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def sum(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @staticmethod
    def sumDifference(sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Returns the sum of the (signed) differences between corresponding elements of the input arrays -- i.e., sum(sample1[i] - sample2[i]).
        
        Parameters:
            sample1 (double[]): the first array
            sample2 (double[]): the second array
        
        Returns:
            sum of paired differences
        
        Raises:
            hipparchus: if the arrays do not have the same (positive) length.
            hipparchus: if the sample arrays are empty.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def sumLog(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def sumLog(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def sumSq(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def sumSq(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def variance(*values: float) -> float: ...
    @typing.overload
    @staticmethod
    def variance(values: typing.Union[typing.List[float], jpype.JArray], mean: float) -> float: ...
    @typing.overload
    @staticmethod
    def variance(values: typing.Union[typing.List[float], jpype.JArray], mean: float, begin: int, length: int) -> float: ...
    @typing.overload
    @staticmethod
    def variance(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> float: ...
    @staticmethod
    def varianceDifference(sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray], meanDifference: float) -> float:
        """
        Returns the variance of the (signed) differences between corresponding elements of the input arrays -- i.e., var(sample1[i] - sample2[i]).
        
        Parameters:
            sample1 (double[]): the first array
            sample2 (double[]): the second array
            meanDifference (double): the mean difference between corresponding entries
        
        Returns:
            variance of paired differences
        
        Raises:
            hipparchus: if the arrays do not have the same length.
            hipparchus: if the arrays length is less than 2.
        
        Also see:
            meanDifference
        
        
        """
        ...

class LongFrequency(Frequency[int]):
    """
    Maintains a frequency distribution of Long values.
    
    Accepts byte, short, int, long primitive or Integer and Long values.
    
    Integer values (byte, short, int, long, Integer, Long) are not distinguished by type, i.e. valueOf(2)), addValue(2), addValue(2L) all have the same effect (similarly for arguments to getCount() etc.).
    
    NOTE: byte and short values will be implicitly converted to int values by the compiler, thus there are no explicit overloaded methods for these primitive types.
    
    The values are ordered using the default (natural order), unless a Comparator is supplied in the constructor.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, comparator: typing.Union[java.util.Comparator[int], typing.Callable[[int, int], int]]): ...
    @typing.overload
    def addValue(self, v: java.lang.Comparable) -> None:
        """
        Adds 1 to the frequency count for v.
        
        Parameters:
            v (int): the value to add.
        
        
        """
        ...
    @typing.overload
    def addValue(self, v: int) -> None: ...
    @typing.overload
    def getCount(self, v: java.lang.Comparable) -> int:
        """
        Returns the number of values equal to v.
        
        Parameters:
            v (int): the value to lookup.
        
        Returns:
            the frequency of v.
        
        
        """
        ...
    @typing.overload
    def getCount(self, v: int) -> int: ...
    @typing.overload
    def getCumFreq(self, v: java.lang.Comparable) -> int:
        """
        Returns the cumulative frequency of values less than or equal to v.
        
        Parameters:
            v (int): the value to lookup.
        
        Returns:
            the proportion of values equal to v
        
        
        """
        ...
    @typing.overload
    def getCumFreq(self, v: int) -> int: ...
    @typing.overload
    def getCumPct(self, v: java.lang.Comparable) -> float:
        """
        Returns NaN if no values have been added.
        
        Parameters:
            v (int): the value to lookup
        
        Returns:
            the proportion of values less than or equal to v
        
        
        """
        ...
    @typing.overload
    def getCumPct(self, v: int) -> float: ...
    @typing.overload
    def getPct(self, v: java.lang.Comparable) -> float:
        """
        Returns NaN if no values have been added.
        
        Parameters:
            v (int): the value to lookup
        
        Returns:
            the proportion of values equal to v
        
        
        """
        ...
    @typing.overload
    def getPct(self, v: int) -> float: ...
    @typing.overload
    def incrementValue(self, v: java.lang.Comparable, increment: int) -> None:
        """
        Increments the frequency count for v.
        
        Parameters:
            v (int): the value to add.
            increment (long): the amount by which the value should be incremented
        
        
        """
        ...
    @typing.overload
    def incrementValue(self, v: int, increment: int) -> None: ...


class __module_protocol__(Protocol):
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
    projection: org.hipparchus.stat.projection.__module_protocol__
    ranking: org.hipparchus.stat.ranking.__module_protocol__
    regression: org.hipparchus.stat.regression.__module_protocol__
