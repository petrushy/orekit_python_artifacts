import org.orekit.gnss.metric.messages.common.class-use
import typing



class AccuracyProvider:
    """
    public interface AccuracyProvider
    
        This interface represents an accuracy providerused to validate RTCM ephemeris messages.
    
        Since:
            11.0
    """
    def getAccuracy(self) -> float:
        """
            Get the accuracy of the ephemeris data from an accuracy index.
        
            Returns:
                accuracy in meters
        
        
        """
        ...

class ClockCorrection:
    """
    public class ClockCorrection extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for SSR clock correction data.
    
        Since:
            11.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getDeltaClockC0(self) -> float:
        """
            Get the delta clock C0.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the delta clock C0 in seconds
        
        
        """
        ...
    def getDeltaClockC1(self) -> float:
        """
            Get the delta clock C1.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the delta clock C1 in seconds
        
        
        """
        ...
    def getDeltaClockC2(self) -> float:
        """
            Get the delta clock C2.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the delta clock C2 in seconds
        
        
        """
        ...

class CodeBias:
    """
    public class CodeBias extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for code bias data.
    
        Since:
            11.0
    """
    def __init__(self, int: int, double: float): ...
    def getCodeBias(self) -> float:
        """
            Get the code bias associated to the signal ID.
        
            Returns:
                the code bias in meters
        
        
        """
        ...
    def getSignalID(self) -> int:
        """
            Get the GNSS signal and tracking mode identifier.
        
            Returns:
                the GNSS signal and tracking mode identifier
        
        
        """
        ...

class OrbitCorrection:
    """
    public class OrbitCorrection extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for SSR orbit correction data.
    
        Since:
            11.0
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    def getDeltaOrbitAlongTrack(self) -> float:
        """
            Get the along-track orbit correction for broadcast ephemeris.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the along-track orbit correction for broadcast ephemeris in meters
        
        
        """
        ...
    def getDeltaOrbitCrossTrack(self) -> float:
        """
            Get the cross-track orbit correction for broadcast ephemeris.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the cross-track orbit correction for broadcast ephemeris
        
        
        """
        ...
    def getDeltaOrbitRadial(self) -> float:
        """
            Get the radial orbit correction for broadcast ephemeris.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the radial orbit correction for broadcast ephemeris in meters
        
        
        """
        ...
    def getDotOrbitDeltaAlongTrack(self) -> float:
        """
            Get the velocity of along-track orbit correction for broadcast ephemeris.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the velocity of along-track orbit correction for broadcast ephemeris in m/s
        
        
        """
        ...
    def getDotOrbitDeltaCrossTrack(self) -> float:
        """
            Get the velocity of cross-track orbit correction for broadcast ephemeris.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the velocity of cross-track orbit correction for broadcast ephemeris in m/s
        
        
        """
        ...
    def getDotOrbitDeltaRadial(self) -> float:
        """
            Get the velocity of radial orbit correction for broadcast ephemeris.
        
            The reference time t0 is SSR Epoch Time (IDF003) plus ½ SSR Update Interval.
        
            Returns:
                the velocity of Radial orbit correction for broadcast ephemeris in m/s
        
        
        """
        ...

class PhaseBias:
    """
    public class PhaseBias extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for phase bias data.
    
        Since:
            11.0
    """
    def __init__(self, int: int, boolean: bool, int2: int, int3: int, double: float): ...
    def getDiscontinuityCounter(self) -> int:
        """
            Get the signal phase discontinuity counter.
        
            Increased for every discontinuity in phase
        
            Returns:
                the signal phase discontinuity counter
        
        
        """
        ...
    def getPhaseBias(self) -> float:
        """
            Get the phase bias associated to the signal ID.
        
            Returns:
                the phase bias in meters
        
        
        """
        ...
    def getSignalID(self) -> int:
        """
            Get the GNSS signal and tracking mode identifier.
        
            Returns:
                the GNSS signal and tracking mode identifier
        
        
        """
        ...
    def getSignalWideLaneIntegerIndicator(self) -> int:
        """
            Get the signal Wide-Lane integer indicator.
        
              - 0: No wide-lane with integer property for this signal or satellite
              - 1: Signal belongs to group two of wide-lanes with integer property
              - 2: Signal belongs to group one of wide-lanes with integer property
              - 3: Signal belongs to group one of wide-lanes with integer property
        
        
            Returns:
                the signal Wide-Lane indicator
        
        
        """
        ...
    def isSignalInteger(self) -> bool:
        """
            Get the flag indicating is signal has integer property.
        
            Returns:
                true is signal has integer property
        
        
        """
        ...

class SsrUpdateInterval:
    """
    public class SsrUpdateInterval extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        SSR Update interval.
    
        Using the indicator parsed in the RTCM message, this class provides the SSR update interval in seconds.
    
        Since:
            12.0
    """
    def __init__(self, int: int): ...
    def getUpdateInterval(self) -> float:
        """
            Get the update interval.
        
            Returns:
                the update interval in seconds
        
        
        """
        ...

class GlonassUserRangeAccuracy(AccuracyProvider):
    """
    public class GlonassUserRangeAccuracy extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
    
        Enumerate for GLONASS User Range Accuracy.
    
        Also see:
            "ICD L1, L2 GLONASS, Edition 5.1, Table 4.4, 2008"
    """
    def __init__(self, int: int): ...
    def getAccuracy(self) -> float:
        """
            Get the accuracy of the ephemeris data from an accuracy index.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.messages.common.AccuracyProvider.getAccuracy` in
                interface :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
        
            Returns:
                accuracy in meters
        
        
        """
        ...

class PythonAccuracyProvider(AccuracyProvider):
    """
    public class PythonAccuracyProvider extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAccuracy(self) -> float:
        """
            Get the accuracy of the ephemeris data from an accuracy index.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.messages.common.AccuracyProvider.getAccuracy` in
                interface :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
        
            Returns:
                accuracy in meters
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class SignalInSpaceAccuracy(AccuracyProvider):
    """
    public class SignalInSpaceAccuracy extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
    
        Signal-In-Space Accuracy (SISA).
    
        Since:
            11.0
    
        Also see:
            "Galileo OS Signal-In-Space Interface Control Document, Issue 1.3, December 2016, Table 76"
    """
    def __init__(self, int: int): ...
    def getAccuracy(self) -> float:
        """
            Get the accuracy of the ephemeris data from an accuracy index.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.messages.common.AccuracyProvider.getAccuracy` in
                interface :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
        
            Returns:
                accuracy in meters
        
        
        """
        ...

class UserRangeAccuracy(AccuracyProvider):
    """
    public class UserRangeAccuracy extends :class:`~org.orekit.gnss.metric.messages.common.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
    
        User Range Accuracy.
    
        Since:
            11.0
    
        Also see:
            "IS-GPS-200K, 4 March 2016, Section 20.3.3.3.1.3"
    """
    def __init__(self, int: int): ...
    def getAccuracy(self) -> float:
        """
            Get the accuracy of the ephemeris data from an accuracy index.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.messages.common.AccuracyProvider.getAccuracy` in
                interface :class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`
        
            Returns:
                accuracy in meters
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.common")``.

    AccuracyProvider: typing.Type[AccuracyProvider]
    ClockCorrection: typing.Type[ClockCorrection]
    CodeBias: typing.Type[CodeBias]
    GlonassUserRangeAccuracy: typing.Type[GlonassUserRangeAccuracy]
    OrbitCorrection: typing.Type[OrbitCorrection]
    PhaseBias: typing.Type[PhaseBias]
    PythonAccuracyProvider: typing.Type[PythonAccuracyProvider]
    SignalInSpaceAccuracy: typing.Type[SignalInSpaceAccuracy]
    SsrUpdateInterval: typing.Type[SsrUpdateInterval]
    UserRangeAccuracy: typing.Type[UserRangeAccuracy]
    class-use: org.orekit.gnss.metric.messages.common.class-use.__module_protocol__
