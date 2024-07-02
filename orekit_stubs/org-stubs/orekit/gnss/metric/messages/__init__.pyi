import org.orekit.gnss.metric.messages.common
import org.orekit.gnss.metric.messages.rtcm
import org.orekit.gnss.metric.messages.ssr
import typing



class ParsedMessage:
    def getTypeCode(self) -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages")``.

    ParsedMessage: typing.Type[ParsedMessage]
    common: org.orekit.gnss.metric.messages.common.__module_protocol__
    rtcm: org.orekit.gnss.metric.messages.rtcm.__module_protocol__
    ssr: org.orekit.gnss.metric.messages.ssr.__module_protocol__
