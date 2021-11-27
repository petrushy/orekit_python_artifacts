import java.util
import org.orekit.gnss.metric.messages
import org.orekit.gnss.metric.messages.rtcm.ephemeris
import typing



class RtcmData:
    def __init__(self): ...

_RtcmMessage__D = typing.TypeVar('_RtcmMessage__D', bound=RtcmData)  # <D>
class RtcmMessage(org.orekit.gnss.metric.messages.ParsedMessage, typing.Generic[_RtcmMessage__D]):
    def __init__(self, int: int, list: java.util.List[_RtcmMessage__D]): ...
    def getData(self) -> java.util.List[_RtcmMessage__D]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.rtcm")``.

    RtcmData: typing.Type[RtcmData]
    RtcmMessage: typing.Type[RtcmMessage]
    ephemeris: org.orekit.gnss.metric.messages.rtcm.ephemeris.__module_protocol__
