import org
import org.hipparchus
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class GNSSAttitudeProvider(org.orekit.attitudes.AttitudeProvider):
    """
    public interface GNSSAttitudeProvider extends :class:`~org.orekit.attitudes.AttitudeProvider`
    
        Attitude providers for navigation satellites.
    
        The attitude mode is compliant with IGS conventions for spacecraft frame, i.e. the +Z axis is towards Earth and the +X
        axis is in the Sun direction. This may be different from some manufacturers conventions, for example for GPS blocks
        IIR/IIRM whose X axis convention is opposite.
    
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
    """
    public class PythonGNSSAttitudeProvider extends Object implements :class:`~org.orekit.gnss.attitude.GNSSAttitudeProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.attitudes.Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> org.orekit.attitudes.FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude attitude on the specified date and position-velocity state
        
            Since:
                9.0
        
        
        """
        ...
    _getAttitude_FFF__T = typing.TypeVar('_getAttitude_FFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getAttitude_FFF(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_FFF__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_FFF__T], frame: org.orekit.frames.Frame) -> org.orekit.attitudes.FieldAttitude[_getAttitude_FFF__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude attitude on the specified date and position-velocity state
        
            Since:
                9.0
        
        
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
        
            Specified by:
                :meth:`~org.orekit.gnss.attitude.GNSSAttitudeProvider.validityEnd`Â in
                interfaceÂ :class:`~org.orekit.gnss.attitude.GNSSAttitudeProvider`
        
            Returns:
                end of validity for this provider
        
        
        """
        ...
    def validityStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start of validity for this provider.
        
            Specified by:
                :meth:`~org.orekit.gnss.attitude.GNSSAttitudeProvider.validityStart`Â in
                interfaceÂ :class:`~org.orekit.gnss.attitude.GNSSAttitudeProvider`
        
            Returns:
                start of validity for this provider
        
        
        """
        ...

class BeidouGeo(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    public class BeidouGeo extends Object
    
        Attitude providers for Beidou geostationary orbit navigation satellites.
    
        Since:
            9.2
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class BeidouIGSO(org.orekit.gnss.attitude.BeidouMeo):
    """
    public class BeidouIGSO extends :class:`~org.orekit.gnss.attitude.BeidouMeo`
    
        Attitude providers for Beidou inclined geosynchronous orbit navigation satellites.
    
        This mode is in fact similar to Beidou MEO, hence the class simply inherit for
        :class:`~org.orekit.gnss.attitude.BeidouMeo` without any change.
    
        Since:
            9.2
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class BeidouMeo(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    public class BeidouMeo extends Object
    
        Attitude providers for Beidou Medium Earth Orbit navigation satellites.
    
        Since:
            9.2
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class GPSBlockIIA(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    public class GPSBlockIIA extends Object
    
        Attitude providers for GPS block IIA navigation satellites.
    
        This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center
        Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and
        its low level models are used, but the structure of the code and the API have been completely rewritten.
    
        Since:
            9.2
    """
    DEFAULT_YAW_BIAS: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_YAW_BIAS
    
        Default yaw bias (rad).
    
    """
    def __init__(self, double: float, double2: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...
    @staticmethod
    def getDefaultYawRate(int: int) -> float:
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
    public class GPSBlockIIF extends Object
    
        Attitude providers for GPS block IIF navigation satellites.
    
        This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center
        Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and
        its low level models are used, but the structure of the code and the API have been completely rewritten.
    
        Since:
            9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_YAW_RATE
    
        Default yaw rates for all spacecrafts in radians per seconds.
    
    """
    DEFAULT_YAW_BIAS: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_YAW_BIAS
    
        Default yaw bias (rad).
    
    """
    def __init__(self, double: float, double2: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class GPSBlockIIR(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    public class GPSBlockIIR extends Object
    
        Attitude providers for GPS block IIR navigation satellites.
    
        This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center
        Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and
        its low level models are used, but the structure of the code and the API have been completely rewritten.
    
        Since:
            9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_YAW_RATE
    
        Default yaw rates for all spacecrafts in radians per seconds.
    
    """
    def __init__(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class Galileo(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    public class Galileo extends Object
    
        Attitude providers for Galileo navigation satellites.
    
        This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center
        Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and
        its low level models are used, but the structure of the code and the API have been completely rewritten.
    
        Since:
            9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_YAW_RATE
    
        Default yaw rates for all spacecrafts in radians per seconds.
    
    """
    def __init__(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class GenericGNSS(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    public class GenericGNSS extends Object
    
        Attitude providers for navigation satellites for which no specialized model is known.
    
        Since:
            9.2
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class Glonass(org.orekit.gnss.attitude.AbstractGNSSAttitudeProvider):
    """
    public class Glonass extends Object
    
        Attitude providers for Glonass navigation satellites.
    
        This class is based on the May 2017 version of J. Kouba eclips.f subroutine available at `IGS Analysis Center
        Coordinator site <http://acc.igs.org/orbits>`. The eclips.f code itself is not used ; its hard-coded data are used and
        its low level models are used, but the structure of the code and the API have been completely rewritten.
    
        Since:
            9.2
    """
    DEFAULT_YAW_RATE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_YAW_RATE
    
        Default yaw rates for all spacecrafts in radians per seconds.
    
    """
    def __init__(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, frame: org.orekit.frames.Frame): ...

class AbstractGNSSAttitudeProvider: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.attitude")``.

    AbstractGNSSAttitudeProvider: typing.Type[AbstractGNSSAttitudeProvider]
    BeidouGeo: typing.Type[BeidouGeo]
    BeidouIGSO: typing.Type[BeidouIGSO]
    BeidouMeo: typing.Type[BeidouMeo]
    GNSSAttitudeProvider: typing.Type[GNSSAttitudeProvider]
    GPSBlockIIA: typing.Type[GPSBlockIIA]
    GPSBlockIIF: typing.Type[GPSBlockIIF]
    GPSBlockIIR: typing.Type[GPSBlockIIR]
    Galileo: typing.Type[Galileo]
    GenericGNSS: typing.Type[GenericGNSS]
    Glonass: typing.Type[Glonass]
    PythonGNSSAttitudeProvider: typing.Type[PythonGNSSAttitudeProvider]
