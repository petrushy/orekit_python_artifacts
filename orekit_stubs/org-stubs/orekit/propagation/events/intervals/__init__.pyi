import org.orekit.frames
import org.orekit.propagation.events
import org.orekit.propagation.events.intervals.class-use
import typing



class ApsideDetectionAdaptableIntervalFactory:
    """
    public class ApsideDetectionAdaptableIntervalFactory extends :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory class for :class:`~org.orekit.propagation.events.AdaptableInterval` suitable for apside detection on eccentric
        orbits. It requires :class:`~org.orekit.propagation.SpacecraftState` to be based on :class:`~org.orekit.orbits.Orbit` in
        order to work.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.events.AdaptableInterval`, :class:`~org.orekit.propagation.events.ApsideDetector`,
            :class:`~org.orekit.propagation.events.EventSlopeFilter`
    """
    @staticmethod
    def computeKeplerianDurationFromPreviousApoapsis(double: float, double2: float) -> float:
        """
            Method computing time elapsed since last apoapsis, assuming Keplerian motion.
        
            Parameters:
                meanAnomaly (double): mean anomaly
                meanMotion (double): Keplerian mean motion
        
            Returns:
                duration elapsed since last apoapsis
        
        
        """
        ...
    @staticmethod
    def computeKeplerianDurationFromPreviousPeriapsis(double: float, double2: float) -> float:
        """
            Method computing time elapsed since last periapsis, assuming Keplerian motion.
        
            Parameters:
                meanAnomaly (double): mean anomaly
                meanMotion (double): Keplerian mean motion
        
            Returns:
                duration elapsed since last periapsis
        
        
        """
        ...
    @staticmethod
    def getBackwardApoapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.AdaptableInterval` for apoapsis detection with
            backward propagation. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for backward apoapsis detection
        
        
        """
        ...
    @staticmethod
    def getBackwardApsideDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.AdaptableInterval` for arbitrary apside detection
            with backward propagation. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for backward apside detection
        
        
        """
        ...
    @staticmethod
    def getBackwardPeriapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.AdaptableInterval` for periapsis detection with
            backward propagation. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for backward periaspsis detection
        
        
        """
        ...
    @staticmethod
    def getForwardApoapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.AdaptableInterval` for apoapsis detection with
            forward propagation. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for forward apoapsis detection
        
        
        """
        ...
    @staticmethod
    def getForwardApsideDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.AdaptableInterval` for arbitrary apside detection
            with forward propagation. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for forward apside detection
        
        
        """
        ...
    @staticmethod
    def getForwardPeriapsisDetectionAdaptableInterval() -> org.orekit.propagation.events.AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.AdaptableInterval` for periapsis detection with
            forward propagation. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for forward periaspsis detection
        
        
        """
        ...

class ElevationDetectionAdaptableIntervalFactory:
    """
    public class ElevationDetectionAdaptableIntervalFactory extends :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory class for :class:`~org.orekit.propagation.events.AdaptableInterval` suitable for elevation detection on
        eccentric orbits. It requires :class:`~org.orekit.propagation.SpacecraftState` to be based on
        :class:`~org.orekit.orbits.Orbit` in order to work.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.events.AdaptableInterval`, :class:`~org.orekit.propagation.events.ApsideDetector`,
            :class:`~org.orekit.propagation.events.EventSlopeFilter`
    """
    DEFAULT_ELEVATION_SWITCH: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ELEVATION_SWITCH
    
        Default elevation abovde which interval should be switched to fine interval (-5°).
    
    """
    @staticmethod
    def getAdaptableInterval(topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, double2: float) -> org.orekit.propagation.events.AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.AdaptableInterval` for arbitrary elevation detection
            with forward propagation. It uses a Keplerian, eccentric approximation.
        
            Parameters:
                topo (:class:`~org.orekit.frames.TopocentricFrame`): topocentric frame centered at ground interest point
                elevationSwitch (double): elevation above which interval will switch to :code:`fineCheckInterval` (typically
                    :meth:`~org.orekit.propagation.events.intervals.ElevationDetectionAdaptableIntervalFactory.DEFAULT_ELEVATION_SWITCH`
                    which is -5°)
                fineCheckInterval (double): check interval to use when elevation is above :code:`elevationSwitch`
        
            Returns:
                adaptable interval for detection of elevation with respect to :code:`topo`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events.intervals")``.

    ApsideDetectionAdaptableIntervalFactory: typing.Type[ApsideDetectionAdaptableIntervalFactory]
    ElevationDetectionAdaptableIntervalFactory: typing.Type[ElevationDetectionAdaptableIntervalFactory]
    class-use: org.orekit.propagation.events.intervals.class-use.__module_protocol__
