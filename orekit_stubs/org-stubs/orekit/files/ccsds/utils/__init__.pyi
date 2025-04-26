
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util.function
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.time
import org.orekit.utils
import typing



class ContextBinding:
    """
    public class ContextBinding extends :class:`~org.orekit.files.ccsds.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Context for parsing/writing Navigation Data Message.
    
        This class is a facade providing late binding access to data. Late binding is mainly useful at parse time as it allows
        some data to be set up during parsing itself. This is used for example to access
        :meth:`~org.orekit.files.ccsds.utils.ContextBinding.getTimeSystem` that is generally parsed from metadata block, and
        used later on within the same metadata block.
    
        Since:
            11.0
    """
    def __init__(self, supplier: typing.Union[java.util.function.Supplier[org.orekit.utils.IERSConventions], typing.Callable[[], org.orekit.utils.IERSConventions]], booleanSupplier: typing.Union[java.util.function.BooleanSupplier, typing.Callable], supplier2: typing.Union[java.util.function.Supplier[org.orekit.data.DataContext], typing.Callable[[], org.orekit.data.DataContext]], supplier3: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.ndm.ParsedUnitsBehavior], typing.Callable[[], org.orekit.files.ccsds.ndm.ParsedUnitsBehavior]], supplier4: typing.Union[java.util.function.Supplier[org.orekit.time.AbsoluteDate], typing.Callable[[], org.orekit.time.AbsoluteDate]], supplier5: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.definitions.TimeSystem], typing.Callable[[], org.orekit.files.ccsds.definitions.TimeSystem]], doubleSupplier: typing.Union[java.util.function.DoubleSupplier, typing.Callable], doubleSupplier2: typing.Union[java.util.function.DoubleSupplier, typing.Callable]): ...
    def getClockCount(self) -> float:
        """
            Get clock count.
        
            Returns:
                clock count at reference date
        
        
        """
        ...
    def getClockRate(self) -> float:
        """
            Get clock rate.
        
            Returns:
                clock rate (in clock ticks per SI second)
        
        
        """
        ...
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
            Get IERS conventions.
        
            Returns:
                IERS conventions to use while parsing
        
        
        """
        ...
    def getDataContext(self) -> org.orekit.data.DataContext:
        """
            Get the data context used for getting frames, time scales, and celestial bodies.
        
            Returns:
                the data context.
        
        
        """
        ...
    def getParsedUnitsBehavior(self) -> org.orekit.files.ccsds.ndm.ParsedUnitsBehavior:
        """
            Get the behavior to adopt for handling parsed units.
        
            Returns:
                behavior to adopt for handling parsed units
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get initial date.
        
            Returns:
                reference date to use while parsing
        
        
        """
        ...
    def getTimeSystem(self) -> org.orekit.files.ccsds.definitions.TimeSystem:
        """
            Get the time system.
        
            Returns:
                time system
        
        
        """
        ...
    def isSimpleEOP(self) -> bool:
        """
            Get EOP interpolation method.
        
            Returns:
                true if tidal effects are ignored when interpolating EOP
        
        
        """
        ...

class FileFormat(java.lang.Enum['FileFormat']):
    """
    public enum FileFormat extends :class:`~org.orekit.files.ccsds.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.utils.FileFormat`>
    
        Enumerate for file format.
    
        Since:
            11.0
    """
    KVN: typing.ClassVar['FileFormat'] = ...
    XML: typing.ClassVar['FileFormat'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'FileFormat':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['FileFormat']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (FileFormat c : FileFormat.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils")``.

    ContextBinding: typing.Type[ContextBinding]
    FileFormat: typing.Type[FileFormat]
    generation: org.orekit.files.ccsds.utils.generation.__module_protocol__
    lexical: org.orekit.files.ccsds.utils.lexical.__module_protocol__
    parsing: org.orekit.files.ccsds.utils.parsing.__module_protocol__
