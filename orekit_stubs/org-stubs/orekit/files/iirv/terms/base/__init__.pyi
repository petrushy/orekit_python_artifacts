
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



_IIRVVectorTerm__T = typing.TypeVar('_IIRVVectorTerm__T')  # <T>
class IIRVVectorTerm(java.lang.Comparable['IIRVVectorTerm'[typing.Any]], typing.Generic[_IIRVVectorTerm__T]):
    """
    Defines a term within an IIRV Vector, parameterized by its underlying data type.
    
    Since:
        13.0
    """
    def compareTo(self, o: 'IIRVVectorTerm'[typing.Any]) -> int:
        """
        Specified by: Comparable in interface Comparable
        
        
        """
        ...
    def equals(self, o: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def length(self) -> int:
        """
        Gets the length of the term.
        
        The length is measured in number characters contained in the encoded String representation of value, as computed by toEncodedString.
        
        Returns:
            Length of the term
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self, termValue: _IIRVVectorTerm__T) -> str:
        """
        Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
        Parameters:
            termValue (IIRVVectorTerm): Value of the term
        
        Returns:
            Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str:
        """
        Converts the stored value of the IIRV term into the encoded String representation, as it would appear in the IIRV message.
        
        Returns:
            Encoded String representing of the value of the stored vector term, as it would appear in the IIRV message
        
        
        """
        ...
    def value(self) -> _IIRVVectorTerm__T:
        """
        Gets the value of the term in the IIRV vector.
        
        Returns:
            value of the term in the IIRV vector
        
        
        """
        ...

class ConstantValuedIIRVTerm(IIRVVectorTerm[str]):
    """
    Term in an IIRV Vector representing a constant String value.
    
    Since:
        13.0
    """
    def __init__(self, value: str):
        """
        Constructs a ConstantValuedIIRVTerm instance with a given String value.
        
        Parameters:
            value (String): Constant (immutable) value of the term
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self, termValue: str) -> str:
        """
        Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
        Specified by: toEncodedString in class IIRVVectorTerm
        
        Parameters:
            termValue (String): Value of the term
        
        Returns:
            Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...

class DoubleValuedIIRVTerm(IIRVVectorTerm[float]):
    """
    Term in an IIRV Vector representing a double value.
    
    Since:
        13.0
    """
    @typing.overload
    def __init__(self, pattern: str, value: float, length: int, nCharsAfterDecimalPlace: int, isSigned: bool): ...
    @typing.overload
    def __init__(self, pattern: str, value: str, length: int, nCharsAfterDecimalPlace: int, isSigned: bool): ...
    @staticmethod
    def computeValueFromString(value: str, nCharsAfterDecimalPlace: int) -> float:
        """
        Compute the double value of the term from a given String.
        
        Parameters:
            value (String): String value to convert to a double
            nCharsAfterDecimalPlace (int): Number of characters before the end of value the decimal place is assumed to occur.
        
        Returns:
            Double value corresponding to the value String argument
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self, termValue: float) -> str:
        """
        Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
        Specified by: toEncodedString in class IIRVVectorTerm
        
        Parameters:
            termValue (Double): Value of the term
        
        Returns:
            Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...

class LongValuedIIRVTerm(IIRVVectorTerm[int]):
    """
    Term in an IIRV Vector representing a Long (or integer) value.
    
    Since:
        13.0
    """
    @typing.overload
    def __init__(self, pattern: str, value: str, length: int, isSigned: bool): ...
    @typing.overload
    def __init__(self, pattern: str, value: int, length: int, isSigned: bool): ...
    @staticmethod
    def computeValueFromString(value: str) -> int:
        """
        Parses a string as a long, removing any leading spaces.
        
        Parameters:
            value (String): String value of the term.
        
        Returns:
            the long represented by the argument
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...
    @typing.overload
    def toEncodedString(self, termValue: int) -> str:
        """
        Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
        Specified by: toEncodedString in class IIRVVectorTerm
        
        Parameters:
            termValue (Long): Value of the term
        
        Returns:
            Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    def toInt(self) -> int:
        """
        Convert the underlying value from long to int.
        
        Returns:
            The value of the term as an int
        
        
        """
        ...

class StringValuedIIRVTerm(IIRVVectorTerm[str]):
    """
    Non-numeric/mutable term in an IIRV Vector represented as a String.
    
    Since:
        13.0
    """
    def __init__(self, pattern: str, value: str, length: int):
        """
        Constructs an IIRV Vector Term represented by a long. This representation is used for any numeric terms in the IIRV Vector that do not contain a decimal point.
        
        Parameters:
            pattern (String): Regular expression pattern that validates the term
            value (String): Value of the term
            length (int): Length of the term, measured in number of characters in the String representation
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...
    @typing.overload
    def toEncodedString(self, termValue: str) -> str:
        """
        Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
        Specified by: toEncodedString in class IIRVVectorTerm
        
        Parameters:
            termValue (String): Value of the term
        
        Returns:
            Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.iirv.terms.base")``.

    ConstantValuedIIRVTerm: typing.Type[ConstantValuedIIRVTerm]
    DoubleValuedIIRVTerm: typing.Type[DoubleValuedIIRVTerm]
    IIRVVectorTerm: typing.Type[IIRVVectorTerm]
    LongValuedIIRVTerm: typing.Type[LongValuedIIRVTerm]
    StringValuedIIRVTerm: typing.Type[StringValuedIIRVTerm]
