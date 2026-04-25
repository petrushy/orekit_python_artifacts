
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.orekit.gnss
import org.orekit.gnss.metric.messages.common
import org.orekit.gnss.metric.messages.rtcm
import typing



class RtcmCorrectionData(org.orekit.gnss.metric.messages.rtcm.RtcmData):
    """
    Container for common data in RTCM corrections message type.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getSatelliteID(self) -> int:
        """
        Get the satellite ID.
        
        Returns:
            the satellite ID
        
        
        """
        ...
    def setSatelliteID(self, satelliteID: int) -> None:
        """
        Set the satellite ID.
        
        Parameters:
            satelliteID (int): the ID to set
        
        
        """
        ...

class RtcmCorrectionHeader:
    """
    Container for common data in RTCM Correction Message type header.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getEpochTime1s(self) -> float:
        """
        Get the Epoch Time 1s.
        
        Full seconds since the beginning of the GNSS week for or full seconds since the beginning of GLONASS day
        
        Returns:
            the Epoch Time 1s in seconds
        
        
        """
        ...
    def getIodSsr(self) -> int:
        """
        Get the IOD SSR.
        
        A change of Issue of Data SSR is used to indicate a change in the SSR generating configuration.
        
        Returns:
            the IOD SSR
        
        
        """
        ...
    def getMultipleMessageIndicator(self) -> int:
        """
        Get the Multiple Message Indicator.
        
        0 - Last message of a sequence. 1 - Multiple message transmitted
        
        Returns:
            the SSR Multiple Message Indicator
        
        
        """
        ...
    def getNumberOfSatellites(self) -> int:
        """
        Get the number of satellites for the current IGM message.
        
        Returns:
            the number of satellites for the current IGM message
        
        
        """
        ...
    def getSsrProviderId(self) -> int:
        """
        Get the SSR Provider ID.
        
        Returns:
            the SSR Provider ID
        
        
        """
        ...
    def getSsrSolutionId(self) -> int:
        """
        Get the SSR Solution ID.
        
        Returns:
            the SSR Solution ID
        
        
        """
        ...
    def getSsrUpdateInterval(self) -> org.orekit.gnss.metric.messages.common.SsrUpdateInterval:
        """
        Get the SSR Update Interval.
        
        Returns:
            the SSR Update Interval
        
        
        """
        ...
    def setEpochTime1s(self, epochTime1s: float) -> None:
        """
        Set the Epoch Time 1s.
        
        Parameters:
            epochTime1s (double): the Epoch Time 1s to set
        
        
        """
        ...
    def setIodSsr(self, iodSsr: int) -> None:
        """
        Set the IOD SSR.
        
        Parameters:
            iodSsr (int): the IOF SSR to set
        
        
        """
        ...
    def setMultipleMessageIndicator(self, multipleMessageIndicator: int) -> None:
        """
        Set the Multiple Message Indicator.
        
        Parameters:
            multipleMessageIndicator (int): the Multiple Message Indicator to set
        
        
        """
        ...
    def setNumberOfSatellites(self, numberOfSatellites: int) -> None:
        """
        Set the number of satellites for the current IGM message.
        
        Parameters:
            numberOfSatellites (int): the number of satellites to set
        
        
        """
        ...
    def setSsrProviderId(self, ssrProviderId: int) -> None:
        """
        Set the SSR Provider ID.
        
        Parameters:
            ssrProviderId (int): the SSR Provider ID to set
        
        
        """
        ...
    def setSsrSolutionId(self, ssrSolutionId: int) -> None:
        """
        Set the SSR Solution ID.
        
        Parameters:
            ssrSolutionId (int): the SSR Solution ID to set
        
        
        """
        ...
    def setSsrUpdateInterval(self, ssrUpdateInterval: org.orekit.gnss.metric.messages.common.SsrUpdateInterval) -> None:
        """
        Set the SSR Update Interval.
        
        Parameters:
            ssrUpdateInterval (SsrUpdateInterval): the SSR Update Interval to set
        
        
        """
        ...

_RtcmCorrectionMessage__H = typing.TypeVar('_RtcmCorrectionMessage__H', bound=RtcmCorrectionHeader)  # <H>
_RtcmCorrectionMessage__D = typing.TypeVar('_RtcmCorrectionMessage__D', bound=RtcmCorrectionData)  # <D>
class RtcmCorrectionMessage(org.orekit.gnss.metric.messages.rtcm.RtcmMessage[_RtcmCorrectionMessage__D], typing.Generic[_RtcmCorrectionMessage__H, _RtcmCorrectionMessage__D]):
    """
    The RTCM Correction Message types provide elements to calculate GNSS satellite corrections. Corrections are orbit and clock corrections.
    
    Since:
        12.0
    """
    def __init__(self, system: int, typeCode: org.orekit.gnss.SatelliteSystem, header: _RtcmCorrectionMessage__H, data: java.util.List[_RtcmCorrectionMessage__D]):
        """
        Constructor.
        
        Parameters:
            system (int): satellite system associated to the message
            typeCode (SatelliteSystem): message number
            header (RtcmCorrectionMessage): message header
            data (List<RtcmCorrectionMessage> data): message data
        
        
        """
        ...
    def getDataMap(self) -> java.util.Map[str, java.util.List[_RtcmCorrectionMessage__D]]:
        """
        Get the all data parsed in the RTCM correction message.
        
        Key: satellite identifier (e.g. "G01")
        
        Returns:
            the all data for the parsed message
        
        
        """
        ...
    def getHeader(self) -> _RtcmCorrectionMessage__H:
        """
        Get the header.
        
        Returns:
            header
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
        Get the satellite system associated to the message.
        
        Returns:
            the satellite system
        
        
        """
        ...

class Rtcm1057(RtcmCorrectionMessage['RtcmOrbitCorrectionHeader', 'RtcmOrbitCorrectionData']):
    """
    RTCM 1057 message: GPS Orbit Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: 'RtcmOrbitCorrectionHeader', data: java.util.List['RtcmOrbitCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmOrbitCorrectionHeader): message header
            data (List<RtcmOrbitCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1058(RtcmCorrectionMessage[RtcmCorrectionHeader, 'RtcmClockCorrectionData']):
    """
    RTCM 1057 message: GPS Clock Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: RtcmCorrectionHeader, data: java.util.List['RtcmClockCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmCorrectionHeader): message header
            data (List<RtcmClockCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1060(RtcmCorrectionMessage['RtcmOrbitCorrectionHeader', 'RtcmCombinedCorrectionData']):
    """
    RTCM 1060 message: GPS Combined Orbit and Clock Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: 'RtcmOrbitCorrectionHeader', data: java.util.List['RtcmCombinedCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmOrbitCorrectionHeader): message header
            data (List<RtcmCombinedCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1063(RtcmCorrectionMessage['RtcmOrbitCorrectionHeader', 'RtcmOrbitCorrectionData']):
    """
    RTCM 1063 message: GLONASS Orbit Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: 'RtcmOrbitCorrectionHeader', data: java.util.List['RtcmOrbitCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmOrbitCorrectionHeader): message header
            data (List<RtcmOrbitCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1064(RtcmCorrectionMessage[RtcmCorrectionHeader, 'RtcmClockCorrectionData']):
    """
    RTCM 1064 message: GLONASS Clock Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: RtcmCorrectionHeader, data: java.util.List['RtcmClockCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmCorrectionHeader): message header
            data (List<RtcmClockCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1066(RtcmCorrectionMessage['RtcmOrbitCorrectionHeader', 'RtcmCombinedCorrectionData']):
    """
    RTCM 1066 message: GLONASS Combined Orbit and Clock Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: 'RtcmOrbitCorrectionHeader', data: java.util.List['RtcmCombinedCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmOrbitCorrectionHeader): message header
            data (List<RtcmCombinedCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1240(RtcmCorrectionMessage['RtcmOrbitCorrectionHeader', 'RtcmOrbitCorrectionData']):
    """
    RTCM 1240 message: Galileo Orbit Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: 'RtcmOrbitCorrectionHeader', data: java.util.List['RtcmOrbitCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmOrbitCorrectionHeader): message header
            data (List<RtcmOrbitCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1241(RtcmCorrectionMessage[RtcmCorrectionHeader, 'RtcmClockCorrectionData']):
    """
    RTCM 1241 message: Galileo Clock Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: RtcmCorrectionHeader, data: java.util.List['RtcmClockCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmCorrectionHeader): message header
            data (List<RtcmClockCorrectionData> data): message data
        
        
        """
        ...

class Rtcm1243(RtcmCorrectionMessage['RtcmOrbitCorrectionHeader', 'RtcmCombinedCorrectionData']):
    """
    RTCM 1242 message: Combined Galileo Clock Correction Message.
    
    Since:
        12.0
    """
    def __init__(self, typeCode: int, header: 'RtcmOrbitCorrectionHeader', data: java.util.List['RtcmCombinedCorrectionData']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            header (RtcmOrbitCorrectionHeader): message header
            data (List<RtcmCombinedCorrectionData> data): message data
        
        
        """
        ...

class RtcmClockCorrectionData(RtcmCorrectionData):
    """
    Container for common data in RTCM clock correction message type.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getClockCorrection(self) -> org.orekit.gnss.metric.messages.common.ClockCorrection:
        """
        Get the clock correction data.
        
        Returns:
            the clock correction data
        
        
        """
        ...
    def setClockCorrection(self, clockCorrection: org.orekit.gnss.metric.messages.common.ClockCorrection) -> None:
        """
        Set the clock correction data.
        
        Parameters:
            clockCorrection (ClockCorrection): the data to set
        
        
        """
        ...

class RtcmCombinedCorrectionData(RtcmCorrectionData):
    """
    Container for common data in RTCM combined corrections message type.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getClockCorrection(self) -> org.orekit.gnss.metric.messages.common.ClockCorrection:
        """
        Get the clock correction data.
        
        Returns:
            the clock correction data
        
        
        """
        ...
    def getGnssIod(self) -> int:
        """
        Get the GNSS IOD.
        
        Users have to interpret the IOD value depending the satellite system of the current message.
        
        Returns:
            the GNSS IOD
        
        
        """
        ...
    def getOrbitCorrection(self) -> org.orekit.gnss.metric.messages.common.OrbitCorrection:
        """
        Get the orbit correction data.
        
        Returns:
            the orbit correction data
        
        
        """
        ...
    def setClockCorrection(self, clockCorrection: org.orekit.gnss.metric.messages.common.ClockCorrection) -> None:
        """
        Set the clock correction data.
        
        Parameters:
            clockCorrection (ClockCorrection): the data to set
        
        
        """
        ...
    def setGnssIod(self, gnssIod: int) -> None:
        """
        Set the GNSS IOD.
        
        Parameters:
            gnssIod (int): the GNSS IOD to set
        
        
        """
        ...
    def setOrbitCorrection(self, orbitCorrection: org.orekit.gnss.metric.messages.common.OrbitCorrection) -> None:
        """
        Set the orbit correction data.
        
        Parameters:
            orbitCorrection (OrbitCorrection): the data to set
        
        
        """
        ...

class RtcmOrbitCorrectionData(RtcmCorrectionData):
    """
    Container for common data in RTCM orbit correction message type.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getGnssIod(self) -> int:
        """
        Get the GNSS IOD.
        
        Users have to interpret the IOD value depending the satellite system of the current message.
        
        Returns:
            the GNSS IOD
        
        
        """
        ...
    def getOrbitCorrection(self) -> org.orekit.gnss.metric.messages.common.OrbitCorrection:
        """
        Get the orbit correction data.
        
        Returns:
            the orbit correction data
        
        
        """
        ...
    def setGnssIod(self, gnssIod: int) -> None:
        """
        Set the GNSS IOD.
        
        Parameters:
            gnssIod (int): the GNSS IOD to set
        
        
        """
        ...
    def setOrbitCorrection(self, orbitCorrection: org.orekit.gnss.metric.messages.common.OrbitCorrection) -> None:
        """
        Set the orbit correction data.
        
        Parameters:
            orbitCorrection (OrbitCorrection): the data to set
        
        
        """
        ...

class RtcmOrbitCorrectionHeader(RtcmCorrectionHeader):
    """
    Container for common data in RTCM Orbit Correction Message type header.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getSatelliteReferenceDatum(self) -> int:
        """
        Get the satellite reference datum.
        
        Orbit corrections refer to Satellite Reference Datum: 0 - ITRF. 1 - Regional
        
        Returns:
            the indicator of the satellite reference datum
        
        
        """
        ...
    def setSatelliteReferenceDatum(self, satelliteReferenceDatum: int) -> None:
        """
        Set the satellite reference datum.
        
        Parameters:
            satelliteReferenceDatum (int): the satellite reference datum to set
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.rtcm.correction")``.

    Rtcm1057: typing.Type[Rtcm1057]
    Rtcm1058: typing.Type[Rtcm1058]
    Rtcm1060: typing.Type[Rtcm1060]
    Rtcm1063: typing.Type[Rtcm1063]
    Rtcm1064: typing.Type[Rtcm1064]
    Rtcm1066: typing.Type[Rtcm1066]
    Rtcm1240: typing.Type[Rtcm1240]
    Rtcm1241: typing.Type[Rtcm1241]
    Rtcm1243: typing.Type[Rtcm1243]
    RtcmClockCorrectionData: typing.Type[RtcmClockCorrectionData]
    RtcmCombinedCorrectionData: typing.Type[RtcmCombinedCorrectionData]
    RtcmCorrectionData: typing.Type[RtcmCorrectionData]
    RtcmCorrectionHeader: typing.Type[RtcmCorrectionHeader]
    RtcmCorrectionMessage: typing.Type[RtcmCorrectionMessage]
    RtcmOrbitCorrectionData: typing.Type[RtcmOrbitCorrectionData]
    RtcmOrbitCorrectionHeader: typing.Type[RtcmOrbitCorrectionHeader]
