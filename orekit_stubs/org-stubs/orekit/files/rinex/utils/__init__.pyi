
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.orekit.files.rinex.utils.parsing
import typing



class RinexFileType(java.lang.Enum['RinexFileType']):
    """
    public enum RinexFileType extends :class:`~org.orekit.files.rinex.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.rinex.utils.RinexFileType`>
    
        Enumerate for RINEX files types.
    
        Since:
            12.0
    """
    OBSERVATION: typing.ClassVar['RinexFileType'] = ...
    NAVIGATION: typing.ClassVar['RinexFileType'] = ...
    @staticmethod
    def parseRinexFileType(string: str) -> 'RinexFileType':
        """
            Parse the string to get the type.
        
            Parameters:
                s (:class:`~org.orekit.files.rinex.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string to parse (must correspond to a one-character key)
        
            Returns:
                the type corresponding to the string
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RinexFileType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.rinex.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.rinex.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.rinex.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['RinexFileType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (RinexFileType c : RinexFileType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.utils")``.

    RinexFileType: typing.Type[RinexFileType]
    parsing: org.orekit.files.rinex.utils.parsing.__module_protocol__
