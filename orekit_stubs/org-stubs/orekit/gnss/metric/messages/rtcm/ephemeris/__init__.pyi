
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.gnss.metric.messages.common
import org.orekit.gnss.metric.messages.rtcm
import org.orekit.propagation.analytical.gnss.data
import org.orekit.time
import typing



class RtcmEphemerisData(org.orekit.gnss.metric.messages.rtcm.RtcmData):
    """
    public class RtcmEphemerisData extends :class:`~org.orekit.gnss.metric.messages.rtcm.RtcmData`
    
        Container for common data in RTCM ephemeris message type.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getAccuracyProvider(self) -> org.orekit.gnss.metric.messages.common.AccuracyProvider:
        """
            Get the accuracy provider of the ephemeris message.
        
            Returns:
                the accuracy provider
        
        
        """
        ...
    def getSatelliteID(self) -> int:
        """
            Get the satellite ID.
        
            Returns:
                the satellite ID
        
        
        """
        ...
    def setAccuracyProvider(self, accuracyProvider: typing.Union[org.orekit.gnss.metric.messages.common.AccuracyProvider, typing.Callable]) -> None:
        """
            Set the accuracy provider of the ephemeris message.
        
            Parameters:
                provider (:class:`~org.orekit.gnss.metric.messages.common.AccuracyProvider`): the provider to set
        
        
        """
        ...
    def setSatelliteID(self, int: int) -> None:
        """
            Set the satellite ID.
        
            Parameters:
                satelliteID (int): the ID to set
        
        
        """
        ...

_RtcmEphemerisMessage__D = typing.TypeVar('_RtcmEphemerisMessage__D', bound=RtcmEphemerisData)  # <D>
class RtcmEphemerisMessage(org.orekit.gnss.metric.messages.rtcm.RtcmMessage[_RtcmEphemerisMessage__D], typing.Generic[_RtcmEphemerisMessage__D]):
    """
    public class RtcmEphemerisMessage<D extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisData`> extends :class:`~org.orekit.gnss.metric.messages.rtcm.RtcmMessage`<D>
    
        Base class for RTCM ephemeris messages.
    
        Since:
            11.0
    """
    def __init__(self, int: int, d: _RtcmEphemerisMessage__D): ...
    def getEphemerisData(self) -> _RtcmEphemerisMessage__D:
        """
            Get the ephemeris data contain in the ephemeris message.
        
            Returns:
                the ephemeris data contain in the ephemeris message
        
        
        """
        ...

class Rtcm1019(RtcmEphemerisMessage['Rtcm1019Data']):
    """
    public class Rtcm1019 extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisMessage`<:class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.Rtcm1019Data`>
    
        RTCM 1019 message: GPS Satellite Ephemeris Data.
    
        Since:
            11.0
    """
    def __init__(self, int: int, rtcm1019Data: 'Rtcm1019Data'): ...

class Rtcm1019Data(RtcmEphemerisData):
    """
    public class Rtcm1019Data extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisData`
    
        Container for RTCM 1019 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getGpsCodeOnL2(self) -> int:
        """
            Get the GPS code on L2.
        
              - 0: Reserved
              - 1: P code on
              - 2: C/A code on
              - 3: L2C on
        
        
            Returns:
                the GPS code on L2
        
        
        """
        ...
    def getGpsFitInterval(self) -> int:
        """
            Get the GPS fit interval.
        
            Returns:
                the GPS fit interval
        
        
        """
        ...
    def getGpsL2PDataFlag(self) -> bool:
        """
            Get the GPS L2 P-Code data flag.
        
            Returns:
                true L2 P-Code NAV data ON
        
        
        """
        ...
    @typing.overload
    def getGpsNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage:
        """
            Get the GPS navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault` to initialize the time scales used to configure the
            reference epochs of the navigation message.
        
            Returns:
                the GPS navigation message
        
        """
        ...
    @typing.overload
    def getGpsNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage:
        """
            Get the GPS navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            When calling this method, the reference epochs of the navigation message (i.e. ephemeris and clock epochs) are
            initialized using the provided time scales.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): time scales to use for initializing epochs
        
            Returns:
                the GPS navigation message
        
        
        """
        ...
    def getGpsToc(self) -> float:
        """
            Get the GPS time of clock.
        
            The GPS time of clock is given in seconds since the beginning of the GPS week.
        
            Returns:
                the GPS time of clock
        
        
        """
        ...
    def setGpsCodeOnL2(self, int: int) -> None:
        """
            Set the GPS code on L2.
        
            Parameters:
                gpsCodeOnL2 (int): the code to set
        
        
        """
        ...
    def setGpsFitInterval(self, int: int) -> None:
        """
            Set the GPS fit interval.
        
            Parameters:
                gpsFitInterval (int): the GPS fit interval to set
        
        
        """
        ...
    def setGpsL2PDataFlag(self, boolean: bool) -> None:
        """
            Set the GPS L2 P-code data flag.
        
            Parameters:
                gpsL2PDataFlag (boolean): the flag to set
        
        
        """
        ...
    def setGpsNavigationMessage(self, gPSLegacyNavigationMessage: org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage) -> None:
        """
            Set the GPS navigation message.
        
            Parameters:
                gpsNavigationMessage (:class:`~org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage`): the GPS navigation message to set
        
        
        """
        ...
    def setGpsToc(self, double: float) -> None:
        """
            Set the GPS time of clock.
        
            Parameters:
                toc (double): the time of clock to set
        
        
        """
        ...

class Rtcm1020(RtcmEphemerisMessage['Rtcm1020Data']):
    """
    public class Rtcm1020 extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisMessage`<:class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.Rtcm1020Data`>
    
        RTCM 1020 message: Glonass Satellite Ephemeris Data.
    
        Since:
            11.0
    """
    def __init__(self, int: int, rtcm1020Data: 'Rtcm1020Data'): ...

class Rtcm1020Data(RtcmEphemerisData):
    """
    public class Rtcm1020Data extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisData`
    
        Container for RTCM 1020 data.
    
        Spacecraft coordinates read from this RTCM message are given in PZ-90.02 frame.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def areAdditionalDataAvailable(self) -> bool:
        """
            Get the flag indicating if additional parameters are in the message.
        
            Returns:
                true if additional parameters are in the message
        
        
        """
        ...
    def getBN(self) -> int:
        """
            Get the GLONASS B :sub:`n` Word.
        
            Word B :sub:`n` is the health flag
        
            Returns:
                the GLONASS B :sub:`n` Word
        
        
        """
        ...
    def getDeltaTN(self) -> float:
        """
            Get the deltaTauN value.
        
            It represents the GLONASS time difference between navigation RF signal transmitted in L2 sub-band and navigation RF
            signal transmitted in L1 sub-band.
        
            Returns:
                deltaTauN
        
        
        """
        ...
    def getEn(self) -> int:
        """
            Get the GLONASS E :sub:`n` Word.
        
            It characterises the "age" of a current information.
        
            Returns:
                the GLONASS E :sub:`n` Word in days
        
        
        """
        ...
    def getFT(self) -> int:
        """
            Get the GLONASS F :sub:`T` Word.
        
            It is a parameter that provides the predicted satellite user range accuracy at time
            :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getTime`.
        
            Returns:
                the GLONASS F :sub:`T` Word
        
        
        """
        ...
    @typing.overload
    def getGlonassNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage:
        """
            Get the Glonass navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.numerical.GLONASSNumericalPropagator`
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault` to initialize the time scales used to configure the
            reference epochs of the navigation message.
        
            Returns:
                the Glonass navigation message
        
        """
        ...
    @typing.overload
    def getGlonassNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage:
        """
            Get the Glonass navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.numerical.GLONASSNumericalPropagator`
        
            When calling this method, the reference epochs of the navigation message (i.e. ephemeris and clock epochs) are
            initialized using the provided time scales.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): time scales to use for initializing epochs
        
            Returns:
                the Glonass navigation message
        
        
        """
        ...
    def getLNFifthString(self) -> int:
        """
            Get the GLONASS l :sub:`n` Word extracted from fifth string of the subframe.
        
            Returns:
                the GLONASS l :sub:`n` (fifth string)
        
        
        """
        ...
    def getLNThirdString(self) -> int:
        """
            Get the GLONASS l :sub:`n` Word extracted from third string of the subframe.
        
            Returns:
                the GLONASS l :sub:`n` (third string)
        
        
        """
        ...
    def getM(self) -> int:
        """
            Get the GLONASS M Word.
        
            Word M represents the type of satellite transmitting navigation signal. "0" refers to GLONASS satellite, "1" refers to a
            GLONASS-M satellite.
        
            Returns:
                the GLONASS M Word
        
        
        """
        ...
    def getN4(self) -> int:
        """
            Get the four-year interval number starting from 1996.
        
            Returns:
                the four-year interval number starting from 1996
        
        
        """
        ...
    def getNA(self) -> int:
        """
            Get the GLONASS N :sup:`A` Word.
        
            It is the calendar day number within the four-year period beginning since the leap year. It is used for almanac data.
        
            Returns:
                the GLONASS N :sup:`A` Word
        
        
        """
        ...
    def getNt(self) -> int:
        """
            Get the current date.
        
            Current date is a calendar number of day within four-year interval starting from the 1-st of January in a leap year
        
            Returns:
                the current date
        
        
        """
        ...
    def getP(self) -> int:
        """
            Get the GLONASS P Word.
        
            Word P is a technological parameter of control segment, indication the satellite operation mode in respect of time
            parameters.
        
            Returns:
                the GLONASS P Word
        
        
        """
        ...
    def getP1(self) -> int:
        """
            Get the GLONASS P1 Word.
        
            Word P1 is a flag of the immediate data updating. It indicates a time interval between two adjacent values of
            :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getTime` parameter (in seconds).
        
            Returns:
                the GLONASS P1 Word
        
        
        """
        ...
    def getP2(self) -> int:
        """
            Get the GLONASS P2 Word.
        
            Word P2 is flag of oddness ("1") or evenness ("0") of the value of
            :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getTime`.
        
            Returns:
                the GLONASS P2 Word
        
        
        """
        ...
    def getP3(self) -> int:
        """
            Get the GLONASS P3 Word.
        
            Word P3 is flag indicating a number of satellites for which almanac is transmitted within given frame
        
            Returns:
                the GLONASS P3 Word
        
        
        """
        ...
    def getP4(self) -> int:
        """
            Get the GLONASS P4 Word.
        
            GLONASS P4 Word is a flag to show that ephemeris parameters are present. "1" indicates that updated ephemeris or
            frequency/time parameters have been uploaded by the control segment
        
            Returns:
                the GLONASS P4 Word
        
        
        """
        ...
    def getTauC(self) -> float:
        """
            Get the GLONASS time scale correction to UTC time.
        
            Returns:
                the GLONASS time scale correction to UTC time in seconds
        
        
        """
        ...
    def getTauGps(self) -> float:
        """
            Get the correction to GPS time relative to GLONASS time.
        
            Returns:
                the correction to GPS time relative to GLONASS time in seconds
        
        
        """
        ...
    def getTk(self) -> float:
        """
            Get the time referenced to the beginning of the frame within the current day.
        
            Returns:
                the time in seconds
        
        
        """
        ...
    def isHealthAvailable(self) -> bool:
        """
            Get the flag indicating if GLONASS almanac health is available.
        
            Returns:
                true if GLONASS almanac health is available
        
        
        """
        ...
    def setAreAdditionalDataAvailable(self, boolean: bool) -> None:
        """
            Set the flag indicating if additional parameters are in the message.
        
            Parameters:
                areAdditionalDataAvailable (boolean): true if additional parameters are in the message
        
        
        """
        ...
    def setBN(self, int: int) -> None:
        """
            Set the GLONASS B :sub:`n` Word.
        
            Parameters:
                word (int): the word to set
        
        
        """
        ...
    def setDeltaTN(self, double: float) -> None:
        """
            Set the deltaTauN value.
        
            Parameters:
                deltaTN (double): the value to set
        
        
        """
        ...
    def setEn(self, int: int) -> None:
        """
            Get the GLONASS E :sub:`n` Word.
        
            Parameters:
                word (int): the word to set
        
        
        """
        ...
    def setFT(self, int: int) -> None:
        """
            Set the GLONASS F :sub:`T` Word.
        
            Parameters:
                word (int): the word to set
        
        
        """
        ...
    def setGlonassNavigationMessage(self, gLONASSNavigationMessage: org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage) -> None:
        """
            Set the Glonass navigation message.
        
            Parameters:
                glonassNavigationMessage (:class:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage`): the Glonass navigation message to set
        
        
        """
        ...
    def setHealthAvailabilityIndicator(self, boolean: bool) -> None:
        """
            Set the flag indicating if GLONASS almanac health is available.
        
            Parameters:
                healthAvailabilityIndicator (boolean): true if GLONASS almanac health is available
        
        
        """
        ...
    def setLNFifthString(self, int: int) -> None:
        """
            Set the GLONASS l :sub:`n` Word extracted from fifth string of the subframe.
        
            Parameters:
                word (int): the word to set
        
        
        """
        ...
    def setLNThirdString(self, int: int) -> None:
        """
            Set the GLONASS l :sub:`n` Word extracted from third string of the subframe.
        
            Parameters:
                word (int): the word to set
        
        
        """
        ...
    def setM(self, int: int) -> None:
        """
            Set the GLONASS M Word.
        
            Parameters:
                m (int): the GLONASS M Word to set
        
        
        """
        ...
    def setN4(self, int: int) -> None:
        """
            Set the four-year interval number starting from 1996.
        
            Parameters:
                n4 (int): the number to set
        
        
        """
        ...
    def setNA(self, int: int) -> None:
        """
            Set the GLONASS N :sup:`A` Word.
        
            Parameters:
                word (int): the word to set
        
        
        """
        ...
    def setNt(self, int: int) -> None:
        """
            Set the current date.
        
            Parameters:
                nt (int): the current date to set
        
        
        """
        ...
    def setP(self, int: int) -> None:
        """
            Set the GLONASS P Word.
        
            Parameters:
                p (int): the GLONASS P Word to set
        
        
        """
        ...
    def setP1(self, int: int) -> None:
        """
            Set the GLONASS P1 Word.
        
            Parameters:
                p1 (int): the GLONASS P1 Word to set
        
        
        """
        ...
    def setP2(self, int: int) -> None:
        """
            Set the GLONASS P2 Word.
        
            Parameters:
                p2 (int): the GLONASS P2 Word to set
        
        
        """
        ...
    def setP3(self, int: int) -> None:
        """
            Set the the GLONASS P3 Word.
        
            Parameters:
                p3 (int): the GLONASS P3 Word to set
        
        
        """
        ...
    def setP4(self, int: int) -> None:
        """
            Set the GLONASS P4 Word.
        
            Parameters:
                p4 (int): the GLONASS P4 Word to set
        
        
        """
        ...
    def setTauC(self, double: float) -> None:
        """
            Set the GLONASS time scale correction to UTC time.
        
            Parameters:
                tauC (double): the value to set in seconds.
        
        
        """
        ...
    def setTauGps(self, double: float) -> None:
        """
            Set the correction to GPS time relative to GLONASS time.
        
            Parameters:
                tauGps (double): the value to set in seconds
        
        
        """
        ...
    def setTk(self, double: float) -> None:
        """
            Set the time referenced to the beginning of the frame within the current day.
        
            Parameters:
                tk (double): the time to set in seconds
        
        
        """
        ...

class Rtcm1042(RtcmEphemerisMessage['Rtcm1042Data']):
    """
    public class Rtcm1042 extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisMessage`<:class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.Rtcm1042Data`>
    
        RTCM 1042 message: Beidou Satellite Ephemeris Data.
    
        Since:
            11.0
    """
    def __init__(self, int: int, rtcm1042Data: 'Rtcm1042Data'): ...

class Rtcm1042Data(RtcmEphemerisData):
    """
    public class Rtcm1042Data extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisData`
    
        Container for RTCM 1042 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    @typing.overload
    def getBeidouNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage:
        """
            Get the Beidou navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault` to initialize the time scales used to configure the
            reference epochs of the navigation message.
        
            Returns:
                the Beidou navigation message
        
        """
        ...
    @typing.overload
    def getBeidouNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage:
        """
            Get the Beidou navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            When calling this method, the reference epochs of the navigation message (i.e. ephemeris and clock epochs) are
            initialized using the provided time scales.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): time scales to use for initializing epochs
        
            Returns:
                the Beidou navigation message
        
        
        """
        ...
    def getBeidouToc(self) -> float:
        """
            Get the Beidou time of clock.
        
            The Beidou time of clock is given in seconds since the beginning of the Beidou week.
        
            Returns:
                the Beidou time of clock
        
        
        """
        ...
    def getSvHealth(self) -> float:
        """
            Get the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def setBeidouNavigationMessage(self, beidouLegacyNavigationMessage: org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage) -> None:
        """
            Set the Beidou navigation message.
        
            Parameters:
                beidouNavigationMessage (:class:`~org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage`): the Beidou navigation message to set
        
        
        """
        ...
    def setBeidouToc(self, double: float) -> None:
        """
            Set the Beidou time of clock.
        
            Parameters:
                toc (double): the time of clock to set
        
        
        """
        ...
    def setSvHealth(self, double: float) -> None:
        """
            Set the satellite health status.
        
            Parameters:
                svHealth (double): the health status to set
        
        
        """
        ...

class Rtcm1044(RtcmEphemerisMessage['Rtcm1044Data']):
    """
    public class Rtcm1044 extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisMessage`<:class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.Rtcm1044Data`>
    
        RTCM 1044 message: QZSS Satellite Ephemeris Data.
    
        Since:
            11.0
    """
    def __init__(self, int: int, rtcm1044Data: 'Rtcm1044Data'): ...

class Rtcm1044Data(RtcmEphemerisData):
    """
    public class Rtcm1044Data extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisData`
    
        Container for RTCM 1044 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getQzssCodeOnL2(self) -> int:
        """
            Get the QZSS code on L2 Channel.
        
            Returns:
                the QZSS code on L2
        
        
        """
        ...
    def getQzssFitInterval(self) -> int:
        """
            Get the QZSS fit interval.
        
            Returns:
                the QZSS fit interval
        
        
        """
        ...
    @typing.overload
    def getQzssNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage:
        """
            Get the QZSS navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault` to initialize the time scales used to configure the
            reference epochs of the navigation message.
        
            Returns:
                the QZSS navigation message
        
        """
        ...
    @typing.overload
    def getQzssNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage:
        """
            Get the QZSS navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            When calling this method, the reference epochs of the navigation message (i.e. ephemeris and clock epochs) are
            initialized using the provided time scales.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): time scales to use for initializing epochs
        
            Returns:
                the QZSS navigation message
        
        
        """
        ...
    def getQzssToc(self) -> float:
        """
            Get the QZSS time of clock.
        
            The QZSS time of clock is given in seconds since the beginning of the QZSS week.
        
            Returns:
                the QZSS time of clock
        
        
        """
        ...
    def setQzssCodeOnL2(self, int: int) -> None:
        """
            Set the QZSS code on L2.
        
            Parameters:
                qzssCodeOnL2 (int): the code to set
        
        
        """
        ...
    def setQzssFitInterval(self, int: int) -> None:
        """
            Set the QZSS fit interval.
        
            Parameters:
                qzssFitInterval (int): the QZSS fit interval to set
        
        
        """
        ...
    def setQzssNavigationMessage(self, qZSSLegacyNavigationMessage: org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage) -> None:
        """
            Set the QZSS navigation message.
        
            Parameters:
                qzssNavigationMessage (:class:`~org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage`): the QZSS navigation message to set
        
        
        """
        ...
    def setQzssToc(self, double: float) -> None:
        """
            Set the QZSS time of clock.
        
            Parameters:
                toc (double): the time of clock to set
        
        
        """
        ...

class Rtcm1045(RtcmEphemerisMessage['Rtcm1045Data']):
    """
    public class Rtcm1045 extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisMessage`<:class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.Rtcm1045Data`>
    
        RTCM 1045 message: Galileo F/NAV Satellite Ephemeris Data.
    
        Since:
            11.0
    """
    def __init__(self, int: int, rtcm1045Data: 'Rtcm1045Data'): ...

class Rtcm1045Data(RtcmEphemerisData):
    """
    public class Rtcm1045Data extends :class:`~org.orekit.gnss.metric.messages.rtcm.ephemeris.RtcmEphemerisData`
    
        Container for RTCM 1045 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getGalileoDataValidityStatus(self) -> int:
        """
            Get the Galileo data validity status.
        
            Returns:
                the Galileo data validity status
        
        
        """
        ...
    @typing.overload
    def getGalileoNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage:
        """
            Get the Galileo navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault` to initialize the time scales used to configure the
            reference epochs of the navigation message.
        
            Returns:
                the Galileo navigation message
        
        """
        ...
    @typing.overload
    def getGalileoNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage:
        """
            Get the Galileo navigation message corresponding to the current RTCM data.
        
            This object can be used to initialize a :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`
        
            When calling this method, the reference epochs of the navigation message (i.e. ephemeris and clock epochs) are
            initialized using the provided time scales.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): time scales to use for initializing epochs
        
            Returns:
                the Galileo navigation message
        
        
        """
        ...
    def getGalileoToc(self) -> float:
        """
            Get the Galileo time of clock.
        
            The Galileo time of clock is given in seconds since the beginning of the Galileo week.
        
            Returns:
                the Galileo time of clock
        
        
        """
        ...
    def setGalileoDataValidityStatus(self, int: int) -> None:
        """
            Set the Galileo data validity status.
        
            Parameters:
                galileoDataValidityStatus (int): the validity status to set
        
        
        """
        ...
    def setGalileoNavigationMessage(self, galileoNavigationMessage: org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage) -> None:
        """
            Set the Galileo navigation message.
        
            Parameters:
                galileoNavigationMessage (:class:`~org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage`): the Galileo navigation message to set
        
        
        """
        ...
    def setGalileoToc(self, double: float) -> None:
        """
            Set the Galileo time of clock.
        
            Parameters:
                toc (double): the time of clock to set
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.rtcm.ephemeris")``.

    Rtcm1019: typing.Type[Rtcm1019]
    Rtcm1019Data: typing.Type[Rtcm1019Data]
    Rtcm1020: typing.Type[Rtcm1020]
    Rtcm1020Data: typing.Type[Rtcm1020Data]
    Rtcm1042: typing.Type[Rtcm1042]
    Rtcm1042Data: typing.Type[Rtcm1042Data]
    Rtcm1044: typing.Type[Rtcm1044]
    Rtcm1044Data: typing.Type[Rtcm1044Data]
    Rtcm1045: typing.Type[Rtcm1045]
    Rtcm1045Data: typing.Type[Rtcm1045Data]
    RtcmEphemerisData: typing.Type[RtcmEphemerisData]
    RtcmEphemerisMessage: typing.Type[RtcmEphemerisMessage]
