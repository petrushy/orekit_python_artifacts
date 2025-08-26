
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class FastDoubleFormatter:
    """
    public class FastDoubleFormatter extends :class:`~org.orekit.utils.formatting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Formatter for double numbers with low overhead.
    
        This class is intended to be used when formatting large amounts of data with fixed formats like, for example, large
        ephemeris or measurement files.
    
        Building the formatter is done once, and the formatter :meth:`~org.orekit.utils.formatting.FastDoubleFormatter.appendTo`
        or :meth:`~org.orekit.utils.formatting.FastDoubleFormatter.toString` methods can be called hundreds of thousands of
        times, without incurring the overhead that would occur with :code:`String.format()`. Some tests showed this formatter is
        about 5 times faster than :code:`String.format()` with :code:`%{width}.{%precision}f` format.
    
        Instances of this class are immutable
    
        Since:
            13.0.3
    """
    def __init__(self, int: int, int2: int): ...
    def appendTo(self, appendable: java.lang.Appendable, double: float) -> None: ...
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
    def toString(self, double: float) -> str:
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
    public class FastLongFormatter extends :class:`~org.orekit.utils.formatting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Formatter for long integers with low overhead.
    
        This class is intended to be used when formatting large amounts of data with fixed formats like, for example, large
        ephemeris or measurement files.
    
        Building the formatter is done once, and the formatter :meth:`~org.orekit.utils.formatting.FastLongFormatter.appendTo`
        or :meth:`~org.orekit.utils.formatting.FastLongFormatter.toString` methods can be called hundreds of thousands of times,
        without incurring the overhead that would occur with :code:`String.format()`. Some tests showed this formatter is about
        10 times faster than :code:`String.format()` with :code:`%{width}d` format.
    
        Instances of this class are immutable
    
        Since:
            13.0.3
    """
    def __init__(self, int: int, boolean: bool): ...
    def appendTo(self, appendable: java.lang.Appendable, long: int) -> None: ...
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
    def toString(self, long: int) -> str:
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
