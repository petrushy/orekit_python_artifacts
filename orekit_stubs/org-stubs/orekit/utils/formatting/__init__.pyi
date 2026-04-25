
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class FastDoubleFormatter:
    """
    Formatter for double numbers with low overhead.
    
    This class is intended to be used when formatting large amounts of data with fixed formats like, for example, large ephemeris or measurement files.
    
    Building the formatter is done once, and the formatter appendTo or toString methods can be called hundreds of thousands of times, without incurring the overhead that would occur with format(). Some tests showed this formatter is about 5 times faster than format() with  format.
    
    Instances of this class are immutable
    
    Since:
        13.0.3
    """
    def __init__(self, width: int, precision: int):
        """
        Simple constructor.
        
        This constructor is equivalent to Formatter float format
        
        
        Parameters:
            width (int): number of characters to output
            precision (int): number of decimal precision
        
        
        """
        ...
    def appendTo(self, appendable: java.lang.Appendable, value: float) -> None:
        """
        Append one formatted value to an Appendable.
        
        Parameters:
            appendable (Appendable): to append value to
            value (double): value to format
        
        Raises:
            IOException: if an I/O error occurs
        
        
        """
        ...
    def getPrecision(self) -> int:
        """
        Get the precision.
        
        Returns:
            precision
        
        
        """
        ...
    def getWidth(self) -> int:
        """
        Get the width.
        
        Returns:
            width
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, value: float) -> str:
        """
        Format one value.
        
        Parameters:
            value (double): value to format
        
        Returns:
            formatted string
        
        
        """
        ...

class FastLongFormatter:
    """
    Formatter for long integers with low overhead.
    
    This class is intended to be used when formatting large amounts of data with fixed formats like, for example, large ephemeris or measurement files.
    
    Building the formatter is done once, and the formatter appendTo or toString methods can be called hundreds of thousands of times, without incurring the overhead that would occur with format(). Some tests showed this formatter is about 10 times faster than format() with  format.
    
    Instances of this class are immutable
    
    Since:
        13.0.3
    """
    def __init__(self, width: int, zeroPadding: bool):
        """
        Simple constructor.
        
        This constructor is equivalent to either Formatter integer format or
        
        Parameters:
            width (int): number of characters to output
            zeroPadding (boolean): if true, the result is left padded with '0' until it matches width
        
        
        """
        ...
    def appendTo(self, appendable: java.lang.Appendable, value: int) -> None:
        """
        Append one formatted value to an Appendable.
        
        Parameters:
            appendable (Appendable): to append value to
            value (long): value to format
        
        Raises:
            IOException: if an I/O error occurs
        
        
        """
        ...
    def getWidth(self) -> int:
        """
        Get the width.
        
        Returns:
            width
        
        
        """
        ...
    def hasZeroPadding(self) -> bool:
        """
        Check if left padding uses '0' characters.
        
        Returns:
            true if left padding uses '0' characters
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, value: int) -> str:
        """
        Format one value.
        
        Parameters:
            value (long): value to format
        
        Returns:
            formatted string
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.utils.formatting")``.

    FastDoubleFormatter: typing.Type[FastDoubleFormatter]
    FastLongFormatter: typing.Type[FastLongFormatter]
