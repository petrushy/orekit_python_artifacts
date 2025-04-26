
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import org.hipparchus.exception
import org.hipparchus.filtering.kalman
import typing



class LocalizedFilterFormats(java.lang.Enum['LocalizedFilterFormats'], org.hipparchus.exception.Localizable):
    """
    public enumLocalizedFilterFormats extends :class:`~org.hipparchus.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.filtering.LocalizedFilterFormats`>
    implements :class:`~org.hipparchus.filtering.https:.www.hipparchus.org.hipparchus`
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    PROCESS_AT_LEAST_ONE_MEASUREMENT: typing.ClassVar['LocalizedFilterFormats'] = ...
    @typing.overload
    def getLocalizedString(self, string: str, string2: str, locale: java.util.Locale) -> str: ...
    @typing.overload
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.filtering.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.filtering.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.filtering.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.filtering.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedFilterFormats':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['LocalizedFilterFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering")``.

    LocalizedFilterFormats: typing.Type[LocalizedFilterFormats]
    kalman: org.hipparchus.filtering.kalman.__module_protocol__
