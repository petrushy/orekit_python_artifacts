
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.gnss.metric.messages.common
import org.orekit.gnss.metric.messages.rtcm
import org.orekit.gnss.metric.messages.ssr
import typing



class ParsedMessage:
    """
    public abstract class ParsedMessage extends :class:`~org.orekit.gnss.metric.messages.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Abstract base class for decoded IGS messages.
    
        Since:
            11.0
    """
    def getTypeCode(self) -> int:
        """
            Get the code for the message type.
        
            Returns:
                code for the message type
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages")``.

    ParsedMessage: typing.Type[ParsedMessage]
    common: org.orekit.gnss.metric.messages.common.__module_protocol__
    rtcm: org.orekit.gnss.metric.messages.rtcm.__module_protocol__
    ssr: org.orekit.gnss.metric.messages.ssr.__module_protocol__
