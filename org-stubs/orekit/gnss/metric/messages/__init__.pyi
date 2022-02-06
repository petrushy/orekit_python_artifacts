import org.orekit.gnss.metric.messages.rtcm
import org.orekit.gnss.metric.messages.ssr
import typing



class ParsedMessage:
    """
    public abstract class ParsedMessage extends Object
    
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages")``.

    ParsedMessage: typing.Type[ParsedMessage]
    rtcm: org.orekit.gnss.metric.messages.rtcm.__module_protocol__
    ssr: org.orekit.gnss.metric.messages.ssr.__module_protocol__
