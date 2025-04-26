
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
    public abstract class IIRVVectorTerm<T> extends :class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable?is`<:class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`<?>>
    
        Defines a term within an IIRV Vector, parameterized by its underlying data type.
    
        Since:
            13.0
    """
    def compareTo(self, iIRVVectorTerm: 'IIRVVectorTerm'[typing.Any]) -> int:
        """
        
            Specified by:
                :meth:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.html?is` in
                interface :class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable?is`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def length(self) -> int:
        """
            Gets the length of the term.
        
            The length is measured in number characters contained in the encoded String representation of :code:`value`, as computed
            by :meth:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm.toEncodedString`.
        
            Returns:
                Length of the term
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self, t: _IIRVVectorTerm__T) -> str:
        """
            Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
            Parameters:
                termValue (:class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`): Value of the term
        
            Returns:
                Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str:
        """
            Converts the stored :code:`value` of the IIRV term into the encoded String representation, as it would appear in the
            IIRV message.
        
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
    public class ConstantValuedIIRVTerm extends :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`<:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`>
    
        Term in an IIRV Vector representing a constant String value.
    
        Since:
            13.0
    """
    def __init__(self, string: str): ...
    @typing.overload
    def toEncodedString(self, string: str) -> str:
        """
            Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
            Specified by:
                :meth:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm.toEncodedString` in
                class :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`
        
            Parameters:
                termValue (:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Value of the term
        
            Returns:
                Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...

class DoubleValuedIIRVTerm(IIRVVectorTerm[float]):
    """
    public class DoubleValuedIIRVTerm extends :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`<:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double?is`>
    
        Term in an IIRV Vector representing a double value.
    
        Since:
            13.0
    """
    @typing.overload
    def __init__(self, string: str, double: float, int: int, int2: int, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, string2: str, int: int, int2: int, boolean: bool): ...
    @staticmethod
    def computeValueFromString(string: str, int: int) -> float:
        """
            Compute the double value of the term from a given String.
        
            Parameters:
                value (:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): String value to convert to a double
                nCharsAfterDecimalPlace (int): Number of characters before the end of :code:`value` the decimal place is assumed to occur.
        
            Returns:
                Double value corresponding to the :code:`value` String argument
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self, double: float) -> str:
        """
            Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
            Specified by:
                :meth:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm.toEncodedString` in
                class :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`
        
            Parameters:
                termValue (:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double?is`): Value of the term
        
            Returns:
                Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...

class LongValuedIIRVTerm(IIRVVectorTerm[int]):
    """
    public class LongValuedIIRVTerm extends :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`<:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Long?is`>
    
        Term in an IIRV Vector representing a Long (or integer) value.
    
        Since:
            13.0
    """
    @typing.overload
    def __init__(self, string: str, string2: str, int: int, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, long: int, int: int, boolean: bool): ...
    @staticmethod
    def computeValueFromString(string: str) -> int:
        """
            Parses a string as a long, removing any leading spaces.
        
            Parameters:
                value (:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): String value of the term.
        
            Returns:
                the long represented by the argument
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...
    @typing.overload
    def toEncodedString(self, long: int) -> str:
        """
            Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
            Specified by:
                :meth:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm.toEncodedString` in
                class :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`
        
            Parameters:
                termValue (:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.Long?is`): Value of the term
        
            Returns:
                Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    def toInt(self) -> int:
        """
            Convert the underlying :meth:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm.value` from long to int.
        
            Returns:
                The value of the term as an int
        
        
        """
        ...

class StringValuedIIRVTerm(IIRVVectorTerm[str]):
    """
    public class StringValuedIIRVTerm extends :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`<:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`>
    
        Non-numeric/mutable term in an IIRV Vector represented as a String.
    
        Since:
            13.0
    """
    def __init__(self, string: str, string2: str, int: int): ...
    @typing.overload
    def toEncodedString(self) -> str: ...
    @typing.overload
    def toEncodedString(self, string: str) -> str:
        """
            Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
            Specified by:
                :meth:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm.toEncodedString` in
                class :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`
        
            Parameters:
                termValue (:class:`~org.orekit.files.iirv.terms.base.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Value of the term
        
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
