
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
    public class SsrIgmData extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrData`
    
        Container for common data in IGS Generic SSR Message type.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getSatelliteID(self) -> int:
        """
            Get the satellite ID.
        
            Returns:
                the satellite ID
        
        
        """
        ...
    def setSatelliteID(self, int: int) -> None:
        """
            Set the satellite ID.
        
            Parameters:
                satelliteID (int): the ID to set
        
        
        """
        ...

class SsrIgmHeader(org.orekit.gnss.metric.messages.ssr.SsrHeader):
    """
    public class SsrIgmHeader extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrHeader`
    
        Container for common data in IGS Generic SSR Message type header.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getNumberOfSatellites(self) -> int:
        """
            Get the number of satellites for the current IGM message.
        
            Returns:
                the number of satellites for the current IGM message
        
        
        """
        ...
    def setNumberOfSatellites(self, int: int) -> None:
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
    public class SsrIgmMessage<H extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`, D extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`> extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrMessage`<H, D>
    
        The IGS Generic SSR Message types provide elements to calculate GNSS satellite corrections. Corrections are orbit and
        clock corrections, code and phase biases, and the user range accuracy.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, h: _SsrIgmMessage__H, list: java.util.List[_SsrIgmMessage__D]): ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get the satellite system associated to the message.
        
            Returns:
                the satellite system
        
        
        """
        ...

class SsrIgm01(SsrIgmMessage['SsrIgm01Header', 'SsrIgm01Data']):
    """
    public class SsrIgm01 extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm01Header`, :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm01Data`>
    
        GNSS SSR Orbit Correction Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, ssrIgm01Header: 'SsrIgm01Header', list: java.util.List['SsrIgm01Data']): ...
    def getSsrIgm01Data(self) -> java.util.Map[str, java.util.List['SsrIgm01Data']]: ...

class SsrIgm01Data(SsrIgmData):
    """
    public class SsrIgm01Data extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`
    
        Container for SSR IGM01 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
    def setGnssIod(self, int: int) -> None:
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
                orbitCorrection (:class:`~org.orekit.gnss.metric.messages.common.OrbitCorrection`): the data to set
        
        
        """
        ...

class SsrIgm01Header(SsrIgmHeader):
    """
    public class SsrIgm01Header extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`
    
        Container for SSR IGM01 header.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getCrsIndicator(self) -> int:
        """
            Get the Global/Regional CRS Indicator.
        
            Returns:
                the Global/Regional CRS Indicator
        
        
        """
        ...
    def setCrsIndicator(self, int: int) -> None:
        """
            Set the Global/Regional CRS Indicator.
        
            Parameters:
                crsIndicator (int): the indicator to set
        
        
        """
        ...

class SsrIgm02(SsrIgmMessage['SsrIgm02Header', 'SsrIgm02Data']):
    """
    public class SsrIgm02 extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm02Header`, :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm02Data`>
    
        GNSS SSR Clock Correction Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, ssrIgm02Header: 'SsrIgm02Header', list: java.util.List['SsrIgm02Data']): ...
    def getSsrIgm02Data(self) -> java.util.Map[str, java.util.List['SsrIgm02Data']]: ...

class SsrIgm02Data(SsrIgmData):
    """
    public class SsrIgm02Data extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`
    
        Container for SSR IGM02 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
                clockCorrection (:class:`~org.orekit.gnss.metric.messages.common.ClockCorrection`): the data to set
        
        
        """
        ...

class SsrIgm02Header(SsrIgmHeader):
    """
    public class SsrIgm02Header extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`
    
        Container for SSR IGM02 header.
    
        Since:
            11.0
    """
    def __init__(self): ...

class SsrIgm03(SsrIgmMessage['SsrIgm03Header', 'SsrIgm03Data']):
    """
    public class SsrIgm03 extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm03Header`, :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm03Data`>
    
        GNSS SSR Combined Orbit and Clock Correction Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, ssrIgm03Header: 'SsrIgm03Header', list: java.util.List['SsrIgm03Data']): ...
    def getSsrIgm03Data(self) -> java.util.Map[str, java.util.List['SsrIgm03Data']]: ...

class SsrIgm03Data(SsrIgmData):
    """
    public class SsrIgm03Data extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`
    
        Container for SSR IGM03 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
                clockCorrection (:class:`~org.orekit.gnss.metric.messages.common.ClockCorrection`): the data to set
        
        
        """
        ...
    def setGnssIod(self, int: int) -> None:
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
                orbitCorrection (:class:`~org.orekit.gnss.metric.messages.common.OrbitCorrection`): the data to set
        
        
        """
        ...

class SsrIgm03Header(SsrIgmHeader):
    """
    public class SsrIgm03Header extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`
    
        Container for SSR IGM03 header.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getCrsIndicator(self) -> int:
        """
            Get the Global/Regional CRS Indicator.
        
            Returns:
                the Global/Regional CRS Indicator
        
        
        """
        ...
    def setCrsIndicator(self, int: int) -> None:
        """
            Set the Global/Regional CRS Indicator.
        
            Parameters:
                crsIndicator (int): the indicator to set
        
        
        """
        ...

class SsrIgm04(SsrIgmMessage['SsrIgm04Header', 'SsrIgm04Data']):
    """
    public class SsrIgm04 extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm04Header`, :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm04Data`>
    
        GNSS SSR High Rate Clock Correction Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, ssrIgm04Header: 'SsrIgm04Header', list: java.util.List['SsrIgm04Data']): ...
    def getSsrIgm04Data(self) -> java.util.Map[str, java.util.List['SsrIgm04Data']]: ...

class SsrIgm04Data(SsrIgmData):
    """
    public class SsrIgm04Data extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`
    
        Container for SSR IGM04 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getHighRateClockCorrection(self) -> float:
        """
            Get the high rate clock correction to be added to the polynomial clock correction.
        
            Returns:
                the high rate clock correction in seconds
        
        
        """
        ...
    def setHighRateClockCorrection(self, double: float) -> None:
        """
            Set the high rate clock correction to be added to the polynomial clock correction.
        
            Parameters:
                highRateClockCorrection (double): the high rate clock correction to set in seconds
        
        
        """
        ...

class SsrIgm04Header(SsrIgmHeader):
    """
    public class SsrIgm04Header extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`
    
        Container for SSR IGM04 header.
    
        Since:
            11.0
    """
    def __init__(self): ...

class SsrIgm05(SsrIgmMessage['SsrIgm05Header', 'SsrIgm05Data']):
    """
    public class SsrIgm05 extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm05Header`, :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm05Data`>
    
        GNSS SSR Code Bias Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, ssrIgm05Header: 'SsrIgm05Header', list: java.util.List['SsrIgm05Data']): ...
    def getSsrIgm05Data(self) -> java.util.Map[str, java.util.List['SsrIgm05Data']]: ...

class SsrIgm05Data(SsrIgmData):
    """
    public class SsrIgm05Data extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`
    
        Container for SSR IGM05 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def addCodeBias(self, codeBias: org.orekit.gnss.metric.messages.common.CodeBias) -> None:
        """
            Add a code bias value for the current satellite.
        
            Parameters:
                bias (:class:`~org.orekit.gnss.metric.messages.common.CodeBias`): the code bias to add
        
        
        """
        ...
    def getCodeBias(self, int: int) -> org.orekit.gnss.metric.messages.common.CodeBias:
        """
            Get the code bias for a given signal ID.
        
            Parameters:
                signalID (int): the signal IF
        
            Returns:
                the corresponding code bias (null if not provided)
        
        
        """
        ...
    def getCodeBiases(self) -> java.util.Map[int, org.orekit.gnss.metric.messages.common.CodeBias]: ...
    def getNumberOfBiasesProcessed(self) -> int:
        """
            Get the number of biases processed for the current satellite.
        
            Returns:
                the number of biases processed
        
        
        """
        ...
    def setNumberOfBiasesProcessed(self, int: int) -> None:
        """
            Set the number of biases processed for the current satellite.
        
            Parameters:
                numberOfBiasesProcessed (int): the number to set
        
        
        """
        ...

class SsrIgm05Header(SsrIgmHeader):
    """
    public class SsrIgm05Header extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`
    
        Container for SSR IGM05 header.
    
        Since:
            11.0
    """
    def __init__(self): ...

class SsrIgm06(SsrIgmMessage['SsrIgm06Header', 'SsrIgm06Data']):
    """
    public class SsrIgm06 extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm06Header`, :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm06Data`>
    
        GNSS SSR Phase Bias Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, ssrIgm06Header: 'SsrIgm06Header', list: java.util.List['SsrIgm06Data']): ...
    def getSsrIgm06Data(self) -> java.util.Map[str, java.util.List['SsrIgm06Data']]: ...

class SsrIgm06Data(SsrIgmData):
    """
    public class SsrIgm06Data extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`
    
        Container for SSR IGM06 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def addPhaseBias(self, phaseBias: org.orekit.gnss.metric.messages.common.PhaseBias) -> None:
        """
            Add a phase bias value for the current satellite.
        
            Parameters:
                bias (:class:`~org.orekit.gnss.metric.messages.common.PhaseBias`): the phase bias to add
        
        
        """
        ...
    def getNumberOfBiasesProcessed(self) -> int:
        """
            Get the number of biases processed for the current satellite.
        
            Returns:
                the number of biases processed
        
        
        """
        ...
    def getPhaseBias(self, int: int) -> org.orekit.gnss.metric.messages.common.PhaseBias:
        """
            Get the phase bias for a given signal ID.
        
            Parameters:
                signalID (int): the signal IF
        
            Returns:
                the corresponding phase bias (null if not provided)
        
        
        """
        ...
    def getPhaseBiases(self) -> java.util.Map[int, org.orekit.gnss.metric.messages.common.PhaseBias]: ...
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
    def setNumberOfBiasesProcessed(self, int: int) -> None:
        """
            Set the number of biases processed for the current satellite.
        
            Parameters:
                numberOfBiasesProcessed (int): the number to set
        
        
        """
        ...
    def setYawAngle(self, double: float) -> None:
        """
            Set the yaw angle used for computation of phase wind-up correction.
        
            Parameters:
                yawAngle (double): the yaw angle to set in radians
        
        
        """
        ...
    def setYawRate(self, double: float) -> None:
        """
            Set the yaw rate.
        
            Parameters:
                yawRate (double): the yaw rate to set in radians per second
        
        
        """
        ...

class SsrIgm06Header(SsrIgmHeader):
    """
    public class SsrIgm06Header extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`
    
        Container for SSR IGM06 header.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def isConsistencyMaintained(self) -> bool:
        """
            Get the flag indicating if phase biases maintain consistency between non-dispersive and all original dispersive phase
            signals.
        
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
    def setIsConsistencyMaintained(self, boolean: bool) -> None:
        """
            Set the flag indicating if phase biases maintain consistency between non-dispersive and all original dispersive phase
            signals.
        
            Parameters:
                isConsistencyMaintained (boolean): the flag to set
        
        
        """
        ...
    def setIsMelbourneWubbenaConsistencyMaintained(self, boolean: bool) -> None:
        """
            Set the flag indicating if consistency between code and phase biases is maintained for the MW combinations.
        
            Parameters:
                isMelbourneWubbenaConsistencyMaintained (boolean): the flag to set
        
        
        """
        ...

class SsrIgm07(SsrIgmMessage['SsrIgm07Header', 'SsrIgm07Data']):
    """
    public class SsrIgm07 extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm07Header`, :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgm07Data`>
    
        GNSS SSR SSR URA Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, satelliteSystem: org.orekit.gnss.SatelliteSystem, ssrIgm07Header: 'SsrIgm07Header', list: java.util.List['SsrIgm07Data']): ...
    def getSsrIgm07Data(self) -> java.util.Map[str, java.util.List['SsrIgm07Data']]: ...

class SsrIgm07Data(SsrIgmData):
    """
    public class SsrIgm07Data extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmData`
    
        Container for SSR IGM07 data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getSsrUra(self) -> float:
        """
            Get the SSR User Range Accuracy (URA).
        
            Returns:
                the SSR User Range Accuracy (URA)
        
        
        """
        ...
    def setSsrUra(self, double: float) -> None:
        """
            Set the SSR User Range Accuracy (URA).
        
            Parameters:
                ssrUra (double): the URA to set
        
        
        """
        ...

class SsrIgm07Header(SsrIgmHeader):
    """
    public class SsrIgm07Header extends :class:`~org.orekit.gnss.metric.messages.ssr.igm.SsrIgmHeader`
    
        Container for SSR IGM07 header.
    
        Since:
            11.0
    """
    def __init__(self): ...


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
