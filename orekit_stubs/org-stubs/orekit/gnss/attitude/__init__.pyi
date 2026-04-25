
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org
import org.hipparchus
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class GNSSAttitudeProvider(org.orekit.attitudes.AttitudeProvider):
    """
    Attitude providers for navigation satellites.
    
    The attitude mode is compliant with IGS conventions for spacecraft frame, i.e. the +Z axis is towards Earth and the +X axis is in the Sun direction. This may be different from some manufacturers conventions, for example for GPS blocks IIR/IIRM whose X axis convention is opposite.
    
    Since:
        9.2
    """
    def validityEnd(self) -> org.orekit.time.AbsoluteDate:
        """
        Get end of validity for this provider.
        
        Returns:
            end of validity for this provider
        
        
        """
        ...
    def validityStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get start of validity for this provider.
        
        Returns:
            start of validity for this provider
        
        
        """
        ...

class PythonGNSSAttitudeProvider(GNSSAttitudeProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.attitudes.Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> org.orekit.attitudes.FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
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
    def validityEnd(self) -> org.orekit.time.AbsoluteDate:
        """
        Get end of validity for this provider.
        
        Specified by: validityEnd in interface GNSSAttitudeProvider
        
        Returns:
            end of validity for this provider
        
        
        """
        ...
    def validityStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get start of validity for this provider.
        
        Specified by: validityStart in interface GNSSAttitudeProvider
        
        Returns:
            start of validity for this provider
        
        
        """
        ...

class BeidouGeo(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for Beidou geostationary orbit navigation satellites.
    
    Since:
        9.2
    """
    def __init__(self, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class BeidouIGSO(org.orekit.gnss.attitude.BeidouMeo):
    """
    Attitude providers for Beidou inclined geosynchronous orbit navigation satellites.
    
    This mode is in fact similar to Beidou MEO, hence the class simply inherit for BeidouMeo without any change.
    
    Since:
        9.2
    """
    def __init__(self, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class BeidouMeo(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for Beidou Medium Earth Orbit navigation satellites.
    
    Since:
        9.2
    """
    def __init__(self, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class GPSBlockIIA(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for GPS block IIA navigation satellites.
    
    This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and its low level models are used, but the structure of the code and the API have been completely rewritten.
    
    Since:
        9.2
    """
    DEFAULT_YAW_BIAS: typing.ClassVar[float] = ...
    """
    Default yaw bias (rad).
    """
    def __init__(self, yawRate: float, yawBias: float, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            yawRate (double): yaw rate to use in radians per seconds (typically getDefaultYawRate)
            yawBias (double): yaw bias to use (rad) (typicall DEFAULT_YAW_BIAS)
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        Since:
            9.3
        
        
        """
        ...
    @staticmethod
    def getDefaultYawRate(prnNumber: int) -> float:
        """
        Get the default yaw rate for a satellite.
        
        Parameters:
            prnNumber (int): satellite PRN
        
        Returns:
            default yaw rate for the specified satellite
        
        Since:
            10.0
        
        
        """
        ...

class GPSBlockIIF(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for GPS block IIF navigation satellites.
    
    This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and its low level models are used, but the structure of the code and the API have been completely rewritten.
    
    Since:
        9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    Default yaw rates for all spacecrafts in radians per seconds.
    """
    DEFAULT_YAW_BIAS: typing.ClassVar[float] = ...
    """
    Default yaw bias (rad).
    """
    def __init__(self, yawRate: float, yawBias: float, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            yawRate (double): yaw rate to use in radians per seconds (typically DEFAULT_YAW_RATE)
            yawBias (double): yaw bias to use (rad) (typicall DEFAULT_YAW_BIAS)
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class GPSBlockIIR(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for GPS block IIR navigation satellites.
    
    This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and its low level models are used, but the structure of the code and the API have been completely rewritten.
    
    Since:
        9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    Default yaw rates for all spacecrafts in radians per seconds.
    """
    def __init__(self, yawRate: float, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            yawRate (double): yaw rate to use in radians per seconds (typically DEFAULT_YAW_RATE)
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class Galileo(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for Galileo navigation satellites.
    
    This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and its low level models are used, but the structure of the code and the API have been completely rewritten.
    
    Since:
        9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    Default yaw rates for all spacecrafts in radians per seconds.
    """
    def __init__(self, yawRate: float, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            yawRate (double): yaw rate to use in radians per seconds (typically DEFAULT_YAW_RATE)
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class GenericGNSS(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for navigation satellites for which no specialized model is known.
    
    Since:
        9.2
    """
    def __init__(self, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class Glonass(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    Attitude providers for Glonass navigation satellites.
    
    This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and its low level models are used, but the structure of the code and the API have been completely rewritten.
    
    Since:
        9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    Default yaw rates for all spacecrafts in radians per seconds.
    """
    def __init__(self, yawRate: float, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            yawRate (double): yaw rate to use in radians per seconds (typically DEFAULT_YAW_RATE)
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPositionProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...

class PythonAbstractGNSSAttitudeProvider(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    def __init__(self, validityStart: org.orekit.time.AbsoluteDate, validityEnd: org.orekit.time.AbsoluteDate, sun: typing.Union[org.orekit.utils.ExtendedPVCoordinatesProvider, typing.Callable], inertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            validityStart (AbsoluteDate): start of validity for this provider
            validityEnd (AbsoluteDate): end of validity for this provider
            sun (ExtendedPVCoordinatesProvider): provider for Sun position
            inertialFrame (Frame): inertial frame where velocity are computed
        
        
        """
        ...
    _correctedYaw_1__T = typing.TypeVar('_correctedYaw_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def correctedYaw(self, context: 'GNSSAttitudeContext') -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
        Select the /** Compute GNSS attitude with midnight/noon yaw turn correction.
        
        Parameters:
            context (org.orekit.gnss.attitude.GNSSAttitudeContext): context data for attitude computation
        
        Returns:
            corrected yaw, using inertial frame as the reference
        
        """
        ...
    @typing.overload
    def correctedYaw(self, context: 'GNSSFieldAttitudeContext'[_correctedYaw_1__T]) -> org.orekit.utils.TimeStampedFieldAngularCoordinates[_correctedYaw_1__T]:
        """
        Compute GNSS attitude with midnight/noon yaw turn correction.
        
        Parameters:
            context (org.orekit.gnss.attitude.GNSSFieldAttitudeContext<T> context): context data for attitude computation
        
        Returns:
            corrected yaw, using inertial frame as the reference
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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

class AbstractGNSSAttitudeProvider: ...

class GNSSAttitudeContext: ...

class GNSSFieldAttitudeContext: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.attitude")``.

    AbstractGNSSAttitudeProvider: typing.Type[AbstractGNSSAttitudeProvider]
    BeidouGeo: typing.Type[BeidouGeo]
    BeidouIGSO: typing.Type[BeidouIGSO]
    BeidouMeo: typing.Type[BeidouMeo]
    GNSSAttitudeContext: typing.Type[GNSSAttitudeContext]
    GNSSAttitudeProvider: typing.Type[GNSSAttitudeProvider]
    GNSSFieldAttitudeContext: typing.Type[GNSSFieldAttitudeContext]
    GPSBlockIIA: typing.Type[GPSBlockIIA]
    GPSBlockIIF: typing.Type[GPSBlockIIF]
    GPSBlockIIR: typing.Type[GPSBlockIIR]
    Galileo: typing.Type[Galileo]
    GenericGNSS: typing.Type[GenericGNSS]
    Glonass: typing.Type[Glonass]
    PythonAbstractGNSSAttitudeProvider: typing.Type[PythonAbstractGNSSAttitudeProvider]
    PythonGNSSAttitudeProvider: typing.Type[PythonGNSSAttitudeProvider]
