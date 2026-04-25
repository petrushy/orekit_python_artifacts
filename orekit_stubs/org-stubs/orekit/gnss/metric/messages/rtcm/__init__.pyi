
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.orekit.gnss.metric.messages
import org.orekit.gnss.metric.messages.rtcm.correction
import org.orekit.gnss.metric.messages.rtcm.ephemeris
import typing



class RtcmData:
    """
    Container for common data in RTCM message.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...

_RtcmMessage__D = typing.TypeVar('_RtcmMessage__D', bound=RtcmData)  # <D>
class RtcmMessage(org.orekit.gnss.metric.messages.ParsedMessage, typing.Generic[_RtcmMessage__D]):
    """
    Base class for RTCM messages.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, rtcmData: java.util.List[_RtcmMessage__D]):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            rtcmData (List<RtcmMessage> rtcmData): message data
        
        
        """
        ...
    def getData(self) -> java.util.List[_RtcmMessage__D]:
        """
        Get the data.
        
        Returns:
            data
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.rtcm")``.

    RtcmData: typing.Type[RtcmData]
    RtcmMessage: typing.Type[RtcmMessage]
    correction: org.orekit.gnss.metric.messages.rtcm.correction.__module_protocol__
    ephemeris: org.orekit.gnss.metric.messages.rtcm.ephemeris.__module_protocol__
