import org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.class-use
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

class GlonassUserRangeAccuracy(AccuracyProvider):
    """
    public class GlonassUserRangeAccuracy extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider`
    
        Enumerate for GLONASS User Range Accuracy.
    
        Also see:
            "ICD L1, L2 GLONASS, Edition 5.1, Table 4.4, 2008"
    """
    def __init__(self, int: int): ...
    def getAccuracy(self) -> float:
        """
            Get the accuracy of the ephemeris data from an accuracy index.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider.getAccuracy` in
                interface :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider`
        
            Returns:
                accuracy in meters
        
        
        """
        ...

class SignalInSpaceAccuracy(AccuracyProvider):
    """
    public class SignalInSpaceAccuracy extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider`
    
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
                :meth:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider.getAccuracy` in
                interface :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider`
        
            Returns:
                accuracy in meters
        
        
        """
        ...

class UserRangeAccuracy(AccuracyProvider):
    """
    public class UserRangeAccuracy extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider`
    
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
                :meth:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider.getAccuracy` in
                interface :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider`
        
            Returns:
                accuracy in meters
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.rtcm.ephemeris.utils")``.

    AccuracyProvider: typing.Type[AccuracyProvider]
    GlonassUserRangeAccuracy: typing.Type[GlonassUserRangeAccuracy]
    SignalInSpaceAccuracy: typing.Type[SignalInSpaceAccuracy]
    UserRangeAccuracy: typing.Type[UserRangeAccuracy]
    class-use: org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.class-use.__module_protocol__
