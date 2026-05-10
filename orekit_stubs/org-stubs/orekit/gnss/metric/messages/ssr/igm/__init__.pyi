
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.orekit.gnss
import org.orekit.gnss.metric.messages.common
import org.orekit.gnss.metric.messages.ssr
import typing



class SsrIgmData(org.orekit.gnss.metric.messages.ssr.SsrData):
    """
    Container for common data in IGS Generic SSR Message type.
    
    Since:
        11.0
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

class SsrIgmHeader(org.orekit.gnss.metric.messages.ssr.SsrHeader):
    """
    Container for common data in IGS Generic SSR Message type header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getNumberOfSatellites(self) -> int:
        """
        Get the number of satellites for the current IGM message.
        
        Returns:
            the number of satellites for the current IGM message
        
        
        """
        ...
    def setNumberOfSatellites(self, numberOfSatellites: int) -> None:
        """
        Set the number of satellites for the current IGM message.
        
        Parameters:
            numberOfSatellites (int): the number of satellites to set
        
        
        """
        ...

_SsrIgmMessage__H = typing.TypeVar('_SsrIgmMessage__H', bound=SsrIgmHeader)  # <H>
_SsrIgmMessage__D = typing.TypeVar('_SsrIgmMessage__D', bound=SsrIgmData)  # <D>
class SsrIgmMessage(org.orekit.gnss.metric.messages.ssr.SsrMessage[_SsrIgmMessage__H, _SsrIgmMessage__D], typing.Generic[_SsrIgmMessage__H, _SsrIgmMessage__D]):
    """
    The IGS Generic SSR Message types provide elements to calculate GNSS satellite corrections. Corrections are orbit and clock corrections, code and phase biases, and the user range accuracy.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: _SsrIgmMessage__H, data: java.util.List[_SsrIgmMessage__D]):
        """
        Constructor.
        
        Parameters:
            system (int): satellite system associated to the message
            typeCode (SatelliteSystem): message number
            header (SsrIgmMessage): message header
            data (List<SsrIgmMessage> data): message data
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
        Get the satellite system associated to the message.
        
        Returns:
            the satellite system
        
        
        """
        ...

class SsrIgm01(SsrIgmMessage['SsrIgm01Header', 'SsrIgm01Data']):
    """
    GNSS SSR Orbit Correction Message.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: 'SsrIgm01Header', data: java.util.List['SsrIgm01Data']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            system (SatelliteSystem): satellite system
            header (SsrIgm01Header): message header
            data (List<SsrIgm01Data> data): message data
        
        
        """
        ...
    def getSsrIgm01Data(self) -> java.util.Map[str, java.util.List['SsrIgm01Data']]:
        """
        Get the SSR IGM01 data parsed in the SSR message.
        
        Returns:
            the SSR IGM01 data for the parsed message
        
        
        """
        ...

class SsrIgm01Data(SsrIgmData):
    """
    Container for SSR IGM01 data.
    
    Since:
        11.0
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

class SsrIgm01Header(SsrIgmHeader):
    """
    Container for SSR IGM01 header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getCrsIndicator(self) -> int:
        """
        Get the Global/Regional CRS Indicator.
        
        Returns:
            the Global/Regional CRS Indicator
        
        
        """
        ...
    def setCrsIndicator(self, crsIndicator: int) -> None:
        """
        Set the Global/Regional CRS Indicator.
        
        Parameters:
            crsIndicator (int): the indicator to set
        
        
        """
        ...

class SsrIgm02(SsrIgmMessage['SsrIgm02Header', 'SsrIgm02Data']):
    """
    GNSS SSR Clock Correction Message.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: 'SsrIgm02Header', data: java.util.List['SsrIgm02Data']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            system (SatelliteSystem): satellite system
            header (SsrIgm02Header): message header
            data (List<SsrIgm02Data> data): message data
        
        
        """
        ...
    def getSsrIgm02Data(self) -> java.util.Map[str, java.util.List['SsrIgm02Data']]:
        """
        Get the SSR IGM02 data parsed in the SSR message.
        
        Returns:
            the SSR IGM02 data for the parsed message
        
        
        """
        ...

class SsrIgm02Data(SsrIgmData):
    """
    Container for SSR IGM02 data.
    
    Since:
        11.0
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

class SsrIgm02Header(SsrIgmHeader):
    """
    Container for SSR IGM02 header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...

class SsrIgm03(SsrIgmMessage['SsrIgm03Header', 'SsrIgm03Data']):
    """
    GNSS SSR Combined Orbit and Clock Correction Message.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: 'SsrIgm03Header', data: java.util.List['SsrIgm03Data']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            system (SatelliteSystem): satellite system
            header (SsrIgm03Header): message header
            data (List<SsrIgm03Data> data): message data
        
        
        """
        ...
    def getSsrIgm03Data(self) -> java.util.Map[str, java.util.List['SsrIgm03Data']]:
        """
        Get the SSR IGM03 data parsed in the SSR message.
        
        Returns:
            the SSR IGM03 data for the parsed message
        
        
        """
        ...

class SsrIgm03Data(SsrIgmData):
    """
    Container for SSR IGM03 data.
    
    Since:
        11.0
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

class SsrIgm03Header(SsrIgmHeader):
    """
    Container for SSR IGM03 header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getCrsIndicator(self) -> int:
        """
        Get the Global/Regional CRS Indicator.
        
        Returns:
            the Global/Regional CRS Indicator
        
        
        """
        ...
    def setCrsIndicator(self, crsIndicator: int) -> None:
        """
        Set the Global/Regional CRS Indicator.
        
        Parameters:
            crsIndicator (int): the indicator to set
        
        
        """
        ...

class SsrIgm04(SsrIgmMessage['SsrIgm04Header', 'SsrIgm04Data']):
    """
    GNSS SSR High Rate Clock Correction Message.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: 'SsrIgm04Header', data: java.util.List['SsrIgm04Data']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            system (SatelliteSystem): satellite system
            header (SsrIgm04Header): message header
            data (List<SsrIgm04Data> data): message data
        
        
        """
        ...
    def getSsrIgm04Data(self) -> java.util.Map[str, java.util.List['SsrIgm04Data']]:
        """
        Get the SSR IGM04 data parsed in the SSR message.
        
        Returns:
            the SSR IGM04 data for the parsed message
        
        
        """
        ...

class SsrIgm04Data(SsrIgmData):
    """
    Container for SSR IGM04 data.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getHighRateClockCorrection(self) -> float:
        """
        Get the high rate clock correction to be added to the polynomial clock correction.
        
        Returns:
            the high rate clock correction in seconds
        
        
        """
        ...
    def setHighRateClockCorrection(self, highRateClockCorrection: float) -> None:
        """
        Set the high rate clock correction to be added to the polynomial clock correction.
        
        Parameters:
            highRateClockCorrection (double): the high rate clock correction to set in seconds
        
        
        """
        ...

class SsrIgm04Header(SsrIgmHeader):
    """
    Container for SSR IGM04 header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...

class SsrIgm05(SsrIgmMessage['SsrIgm05Header', 'SsrIgm05Data']):
    """
    GNSS SSR Code Bias Message.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: 'SsrIgm05Header', data: java.util.List['SsrIgm05Data']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            system (SatelliteSystem): satellite system
            header (SsrIgm05Header): message header
            data (List<SsrIgm05Data> data): message data
        
        
        """
        ...
    def getSsrIgm05Data(self) -> java.util.Map[str, java.util.List['SsrIgm05Data']]:
        """
        Get the SSR IGM05 data parsed in the SSR message.
        
        Returns:
            the SSR IGM05 data for the parsed message
        
        
        """
        ...

class SsrIgm05Data(SsrIgmData):
    """
    Container for SSR IGM05 data.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def addCodeBias(self, bias: org.orekit.gnss.metric.messages.common.CodeBias) -> None:
        """
        Add a code bias value for the current satellite.
        
        Parameters:
            bias (CodeBias): the code bias to add
        
        
        """
        ...
    def getCodeBias(self, signalID: int) -> org.orekit.gnss.metric.messages.common.CodeBias:
        """
        Get the code bias for a given signal ID.
        
        Parameters:
            signalID (int): the signal IF
        
        Returns:
            the corresponding code bias (null if not provided)
        
        
        """
        ...
    def getCodeBiases(self) -> java.util.Map[int, org.orekit.gnss.metric.messages.common.CodeBias]:
        """
        Get the code biases for the current satellite.
        
        First key: signal ID Second key: the code bias object
        
        Returns:
            the code biases for the current satellite
        
        
        """
        ...
    def getNumberOfBiasesProcessed(self) -> int:
        """
        Get the number of biases processed for the current satellite.
        
        Returns:
            the number of biases processed
        
        
        """
        ...
    def setNumberOfBiasesProcessed(self, numberOfBiasesProcessed: int) -> None:
        """
        Set the number of biases processed for the current satellite.
        
        Parameters:
            numberOfBiasesProcessed (int): the number to set
        
        
        """
        ...

class SsrIgm05Header(SsrIgmHeader):
    """
    Container for SSR IGM05 header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...

class SsrIgm06(SsrIgmMessage['SsrIgm06Header', 'SsrIgm06Data']):
    """
    GNSS SSR Phase Bias Message.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: 'SsrIgm06Header', data: java.util.List['SsrIgm06Data']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            system (SatelliteSystem): satellite system
            header (SsrIgm06Header): message header
            data (List<SsrIgm06Data> data): message data
        
        
        """
        ...
    def getSsrIgm06Data(self) -> java.util.Map[str, java.util.List['SsrIgm06Data']]:
        """
        Get the SSR IGM06 data parsed in the SSR message.
        
        Returns:
            the SSR IGM06 data for the parsed message
        
        
        """
        ...

class SsrIgm06Data(SsrIgmData):
    """
    Container for SSR IGM06 data.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def addPhaseBias(self, bias: org.orekit.gnss.metric.messages.common.PhaseBias) -> None:
        """
        Add a phase bias value for the current satellite.
        
        Parameters:
            bias (PhaseBias): the phase bias to add
        
        
        """
        ...
    def getNumberOfBiasesProcessed(self) -> int:
        """
        Get the number of biases processed for the current satellite.
        
        Returns:
            the number of biases processed
        
        
        """
        ...
    def getPhaseBias(self, signalID: int) -> org.orekit.gnss.metric.messages.common.PhaseBias:
        """
        Get the phase bias for a given signal ID.
        
        Parameters:
            signalID (int): the signal IF
        
        Returns:
            the corresponding phase bias (null if not provided)
        
        
        """
        ...
    def getPhaseBiases(self) -> java.util.Map[int, org.orekit.gnss.metric.messages.common.PhaseBias]:
        """
        Get the phase biases for the current satellite.
        
        First key: signal ID Second key: the phase bias object
        
        Returns:
            the phase biases for the current satellite
        
        
        """
        ...
    def getYawAngle(self) -> float:
        """
        Get the yaw angle used for computation of phase wind-up correction.
        
        Returns:
            the yaw angle in radians
        
        
        """
        ...
    def getYawRate(self) -> float:
        """
        Get the yaw rate.
        
        Returns:
            the yaw rate in radians per second
        
        
        """
        ...
    def setNumberOfBiasesProcessed(self, numberOfBiasesProcessed: int) -> None:
        """
        Set the number of biases processed for the current satellite.
        
        Parameters:
            numberOfBiasesProcessed (int): the number to set
        
        
        """
        ...
    def setYawAngle(self, yawAngle: float) -> None:
        """
        Set the yaw angle used for computation of phase wind-up correction.
        
        Parameters:
            yawAngle (double): the yaw angle to set in radians
        
        
        """
        ...
    def setYawRate(self, yawRate: float) -> None:
        """
        Set the yaw rate.
        
        Parameters:
            yawRate (double): the yaw rate to set in radians per second
        
        
        """
        ...

class SsrIgm06Header(SsrIgmHeader):
    """
    Container for SSR IGM06 header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def isConsistencyMaintained(self) -> bool:
        """
        Get the flag indicating if phase biases maintain consistency between non-dispersive and all original dispersive phase signals.
        
        Returns:
            true if consistency is maintained
        
        
        """
        ...
    def isMelbourneWubbenaConsistencyMaintained(self) -> bool:
        """
        Get the flag indicating if consistency between code and phase biases is maintained for the MW combinations.
        
        Returns:
            true if phase biases are consistent for MW combinations
        
        
        """
        ...
    def setIsConsistencyMaintained(self, isConsistencyMaintained: bool) -> None:
        """
        Set the flag indicating if phase biases maintain consistency between non-dispersive and all original dispersive phase signals.
        
        Parameters:
            isConsistencyMaintained (boolean): the flag to set
        
        
        """
        ...
    def setIsMelbourneWubbenaConsistencyMaintained(self, isMelbourneWubbenaConsistencyMaintained: bool) -> None:
        """
        Set the flag indicating if consistency between code and phase biases is maintained for the MW combinations.
        
        Parameters:
            isMelbourneWubbenaConsistencyMaintained (boolean): the flag to set
        
        
        """
        ...

class SsrIgm07(SsrIgmMessage['SsrIgm07Header', 'SsrIgm07Data']):
    """
    GNSS SSR SSR URA Message.
    
    Since:
        11.0
    """
    def __init__(self, typeCode: int, system: org.orekit.gnss.SatelliteSystem, header: 'SsrIgm07Header', data: java.util.List['SsrIgm07Data']):
        """
        Constructor.
        
        Parameters:
            typeCode (int): message number
            system (SatelliteSystem): satellite system
            header (SsrIgm07Header): message header
            data (List<SsrIgm07Data> data): message data
        
        
        """
        ...
    def getSsrIgm07Data(self) -> java.util.Map[str, java.util.List['SsrIgm07Data']]:
        """
        Get the SSR IGM07 data parsed in the SSR message.
        
        Returns:
            the SSR IGM07 data for the parsed message
        
        
        """
        ...

class SsrIgm07Data(SsrIgmData):
    """
    Container for SSR IGM07 data.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getSsrUra(self) -> float:
        """
        Get the SSR User Range Accuracy (URA).
        
        Returns:
            the SSR User Range Accuracy (URA)
        
        
        """
        ...
    def setSsrUra(self, ssrUra: float) -> None:
        """
        Set the SSR User Range Accuracy (URA).
        
        Parameters:
            ssrUra (double): the URA to set
        
        
        """
        ...

class SsrIgm07Header(SsrIgmHeader):
    """
    Container for SSR IGM07 header.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.ssr.igm")``.

    SsrIgm01: typing.Type[SsrIgm01]
    SsrIgm01Data: typing.Type[SsrIgm01Data]
    SsrIgm01Header: typing.Type[SsrIgm01Header]
    SsrIgm02: typing.Type[SsrIgm02]
    SsrIgm02Data: typing.Type[SsrIgm02Data]
    SsrIgm02Header: typing.Type[SsrIgm02Header]
    SsrIgm03: typing.Type[SsrIgm03]
    SsrIgm03Data: typing.Type[SsrIgm03Data]
    SsrIgm03Header: typing.Type[SsrIgm03Header]
    SsrIgm04: typing.Type[SsrIgm04]
    SsrIgm04Data: typing.Type[SsrIgm04Data]
    SsrIgm04Header: typing.Type[SsrIgm04Header]
    SsrIgm05: typing.Type[SsrIgm05]
    SsrIgm05Data: typing.Type[SsrIgm05Data]
    SsrIgm05Header: typing.Type[SsrIgm05Header]
    SsrIgm06: typing.Type[SsrIgm06]
    SsrIgm06Data: typing.Type[SsrIgm06Data]
    SsrIgm06Header: typing.Type[SsrIgm06Header]
    SsrIgm07: typing.Type[SsrIgm07]
    SsrIgm07Data: typing.Type[SsrIgm07Data]
    SsrIgm07Header: typing.Type[SsrIgm07Header]
    SsrIgmData: typing.Type[SsrIgmData]
    SsrIgmHeader: typing.Type[SsrIgmHeader]
    SsrIgmMessage: typing.Type[SsrIgmMessage]
