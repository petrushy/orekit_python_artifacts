
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



class AccuracyProvider:
    """
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
    Container for SSR clock correction data.
    
    Since:
        11.0
    """
    def __init__(self, c0: float, c1: float, c2: float):
        """
        Constructor.
        
        Parameters:
            c0 (double): delta Clock C0
            c1 (double): delta Clock C1
            c2 (double): delta Clock C2
        
        
        """
        ...
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
    Container for code bias data.
    
    Since:
        11.0
    """
    def __init__(self, signalID: int, codeBias: float):
        """
        Constructor.
        
        Parameters:
            signalID (int): GNSS signal and tracking mode identifier
            codeBias (double): code bias associated to the signal ID in meters
        
        
        """
        ...
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
    Container for SSR orbit correction data.
    
    Since:
        11.0
    """
    def __init__(self, dRadial: float, dAlongTrack: float, dCrossTrack: float, dotRadial: float, dotAlongTrack: float, dotCrossTrack: float):
        """
        Constructor.
        
        Parameters:
            dRadial (double): radial orbit correction for broadcast ephemeris (m)
            dAlongTrack (double): along-Track orbit correction for broadcast ephemeris (m)
            dCrossTrack (double): cross-Track orbit correction for broadcast ephemeris (m)
            dotRadial (double): velocity of Radial orbit correction for broadcast ephemeris. (m/s)
            dotAlongTrack (double): velocity of Along-Track orbit correction for broadcast ephemeris (m/s)
            dotCrossTrack (double): velocity of Cross-Track orbit correction for broadcast ephemeris (m/s)
        
        
        """
        ...
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
    Container for phase bias data.
    
    Since:
        11.0
    """
    def __init__(self, signalID: int, isSignalInteger: bool, signalWideLaneIntegerIndicator: int, discontinuityCounter: int, phaseBias: float):
        """
        Constructor.
        
        Parameters:
            signalID (int): GNSS signal and tracking mode identifier
            isSignalInteger (boolean): true if signal has integer property
            signalWideLaneIntegerIndicator (int): signal Wide-Lane integer indicator
            discontinuityCounter (int): signal discontinuity counter
            phaseBias (double): phase bias associated to the signal ID in meters
        
        
        """
        ...
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
    SSR Update interval.
    
    Using the indicator parsed in the RTCM message, this class provides the SSR update interval in seconds.
    
    Since:
        12.0
    """
    def __init__(self, indicator: int):
        """
        Constructor.
        
        Parameters:
            indicator (int): indicator read in the RTCM message
        
        
        """
        ...
    def getUpdateInterval(self) -> float:
        """
        Get the update interval.
        
        Returns:
            the update interval in seconds
        
        
        """
        ...

class GlonassUserRangeAccuracy(AccuracyProvider):
    """
    Enumerate for GLONASS User Range Accuracy.
    
    Also see:
        "ICD L1, L2 GLONASS, Edition 5.1, Table 4.4, 2008"
    """
    def __init__(self, index: int):
        """
        Simple constructor.
        
        Parameters:
            index (int): integer value of the Glonass user range accuracy
        
        
        """
        ...
    def getAccuracy(self) -> float:
        """
        Get the accuracy of the ephemeris data from an accuracy index.
        
        Specified by: getAccuracy in interface AccuracyProvider
        
        Returns:
            accuracy in meters
        
        
        """
        ...

class PythonAccuracyProvider(AccuracyProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAccuracy(self) -> float:
        """
        Get the accuracy of the ephemeris data from an accuracy index.
        
        Specified by: getAccuracy in interface AccuracyProvider
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class SignalInSpaceAccuracy(AccuracyProvider):
    """
    Signal-In-Space Accuracy (SISA).
    
    Since:
        11.0
    
    Also see:
        "Galileo OS Signal-In-Space Interface Control Document, Issue 1.3, December 2016, Table 76"
    """
    def __init__(self, index: int):
        """
        Simple constructor.
        
        Parameters:
            index (int): integer value of the signal in space accuracy
        
        
        """
        ...
    def getAccuracy(self) -> float:
        """
        Get the accuracy of the ephemeris data from an accuracy index.
        
        Specified by: getAccuracy in interface AccuracyProvider
        
        Returns:
            accuracy in meters
        
        
        """
        ...

class UserRangeAccuracy(AccuracyProvider):
    """
    User Range Accuracy.
    
    Since:
        11.0
    
    Also see:
        "IS-GPS-200K, 4 March 2016, Section 20.3.3.3.1.3"
    """
    def __init__(self, index: int):
        """
        Simple constructor.
        
        Parameters:
            index (int): integer value of the user range accuracy
        
        
        """
        ...
    def getAccuracy(self) -> float:
        """
        Get the accuracy of the ephemeris data from an accuracy index.
        
        Specified by: getAccuracy in interface AccuracyProvider
        
        Returns:
            accuracy in meters
        
        
        """
        ...


class __module_protocol__(Protocol):
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
