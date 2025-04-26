
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.orekit.gnss.metric.messages
import org.orekit.gnss.metric.messages.ssr.igm
import org.orekit.gnss.metric.messages.ssr.subtype
import typing



class SsrData:
    """
    public class SsrData extends :class:`~org.orekit.gnss.metric.messages.ssr.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for common data in SSR message data.
    
        Since:
            11.0
    """
    def __init__(self): ...

class SsrHeader:
    """
    public class SsrHeader extends :class:`~org.orekit.gnss.metric.messages.ssr.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for common data in SSR messages header.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getIodSsr(self) -> int:
        """
            Get the IOD SSR.
        
            A change of Issue of Data SSR is used to indicate a change in the SSR generating configuration.
        
            Returns:
                the IOD SSR
        
        
        """
        ...
    def getSsrEpoch1s(self) -> float:
        """
            Get the SSR Epoch Time 1s.
        
            Full seconds since the beginning of the week of continuous time scale with no offset from GPS, Galileo, QZSS, SBAS, UTC
            leap seconds from GLONASS, -14 s offset from BDS
        
            Returns:
                the SSR Epoch Time 1s in seconds
        
        
        """
        ...
    def getSsrMultipleMessageIndicator(self) -> int:
        """
            Get the SSR Multiple Message Indicator.
        
            0 - Last message of a sequence. 1 - Multiple message transmitted
        
            Returns:
                the SSR Multiple Message Indicator
        
        
        """
        ...
    def getSsrProviderId(self) -> int:
        """
            Get the SSR Provider ID.
        
            Returns:
                the SSR Provider ID
        
        
        """
        ...
    def getSsrSolutionId(self) -> int:
        """
            Get the SSR Solution ID.
        
            Returns:
                the SSR Solution ID
        
        
        """
        ...
    def getSsrUpdateInterval(self) -> int:
        """
            Get the SSR Update Interval.
        
            Returns:
                the SSR Update Interval in seconds
        
        
        """
        ...
    def setIodSsr(self, int: int) -> None:
        """
            Set the IOD SSR.
        
            Parameters:
                iodSsr (int): the IOF SSR to set
        
        
        """
        ...
    def setSsrEpoch1s(self, double: float) -> None:
        """
            Set the SSR Epoch Time 1s.
        
            Parameters:
                ssrEpoch1s (double): the SSR Epoch Time 1s to set
        
        
        """
        ...
    def setSsrMultipleMessageIndicator(self, int: int) -> None:
        """
            Set the SSR Multiple Message Indicator.
        
            Parameters:
                ssrMultipleMessageIndicator (int): the SSR Multiple Message Indicator to set
        
        
        """
        ...
    def setSsrProviderId(self, int: int) -> None:
        """
            Set the SSR Provider ID.
        
            Parameters:
                ssrProviderId (int): the SSR Provider ID to set
        
        
        """
        ...
    def setSsrSolutionId(self, int: int) -> None:
        """
            Set the SSR Solution ID.
        
            Parameters:
                ssrSolutionId (int): the SSR Solution ID to set
        
        
        """
        ...
    def setSsrUpdateInterval(self, int: int) -> None:
        """
            Set the SSR Update Interval.
        
            Parameters:
                ssrUpdateInterval (int): the SSR Update Interval to set
        
        
        """
        ...

_SsrMessage__H = typing.TypeVar('_SsrMessage__H', bound=SsrHeader)  # <H>
_SsrMessage__D = typing.TypeVar('_SsrMessage__D', bound=SsrData)  # <D>
class SsrMessage(org.orekit.gnss.metric.messages.ParsedMessage, typing.Generic[_SsrMessage__H, _SsrMessage__D]):
    """
    public class SsrMessage<H extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrHeader`, D extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrData`> extends :class:`~org.orekit.gnss.metric.messages.ParsedMessage`
    
        Base class for SSR messages.
    
        Since:
            11.0
    """
    def __init__(self, int: int, h: _SsrMessage__H, list: java.util.List[_SsrMessage__D]): ...
    def getData(self) -> java.util.List[_SsrMessage__D]: ...
    def getHeader(self) -> _SsrMessage__H:
        """
            Get the header.
        
            Returns:
                header
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.ssr")``.

    SsrData: typing.Type[SsrData]
    SsrHeader: typing.Type[SsrHeader]
    SsrMessage: typing.Type[SsrMessage]
    igm: org.orekit.gnss.metric.messages.ssr.igm.__module_protocol__
    subtype: org.orekit.gnss.metric.messages.ssr.subtype.__module_protocol__
