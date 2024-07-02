import org.orekit.frames
import org.orekit.propagation.events
import typing



class ApsideDetectionAdaptableIntervalFactory:
    @staticmethod
    def computeKeplerianDurationFromPreviousApoapsis(double: float, double2: float) -> float: ...
    @staticmethod
    def computeKeplerianDurationFromPreviousPeriapsis(double: float, double2: float) -> float: ...
    @staticmethod
    def getBackwardApoapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval: ...
    @staticmethod
    def getBackwardApsideDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval: ...
    @staticmethod
    def getBackwardPeriapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval: ...
    @staticmethod
    def getForwardApoapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval: ...
    @staticmethod
    def getForwardApsideDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval: ...
    @staticmethod
    def getForwardPeriapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval: ...

class ElevationDetectionAdaptableIntervalFactory:
    DEFAULT_ELEVATION_SWITCH: typing.ClassVar[float] = ...
    @staticmethod
    def getAdaptableInterval(topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, double2: float) -> org.orekit.propagation.events.AdaptableInterval: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events.intervals")``.

    ApsideDetectionAdaptableIntervalFactory: typing.Type[ApsideDetectionAdaptableIntervalFactory]
    ElevationDetectionAdaptableIntervalFactory: typing.Type[ElevationDetectionAdaptableIntervalFactory]
