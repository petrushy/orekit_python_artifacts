
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import org.hipparchus
import org.orekit.attitudes
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss
import org.orekit.propagation.analytical.gnss
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



class AbstractEphemerisMessage:
    """
    public abstract class AbstractEphemerisMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for ephemeris-based navigation messages.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage`
    """
    def __init__(self): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for the reference date of the ephemeris.
        
            Returns:
                the reference date of the ephemeris
        
        
        """
        ...
    def getEpochToc(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for the time of clock epoch.
        
            Returns:
                the time of clock epoch
        
        
        """
        ...
    def getHealth(self) -> float:
        """
            Getter for the health status.
        
            Returns:
                the health status
        
        
        """
        ...
    def getPRN(self) -> int:
        """
            Getter for the PRN number of the satellite.
        
            Returns:
                the PRN number of the satellite
        
        
        """
        ...
    def getX(self) -> float:
        """
            Getter for the satellite X position.
        
            Returns:
                the satellite X position in meters
        
        
        """
        ...
    def getXDot(self) -> float:
        """
            Getter for the satellite X velocity.
        
            Returns:
                the satellite X velocity in m/s
        
        
        """
        ...
    def getXDotDot(self) -> float:
        """
            Getter for the satellite X acceleration.
        
            Returns:
                the satellite X acceleration in m/s²
        
        
        """
        ...
    def getY(self) -> float:
        """
            Getter for the satellite Y position.
        
            Returns:
                the satellite Y position in meters
        
        
        """
        ...
    def getYDot(self) -> float:
        """
            Getter for the satellite Y velocity.
        
            Returns:
                the satellite Y velocity in m/s
        
        
        """
        ...
    def getYDotDot(self) -> float:
        """
            Getter for the satellite Y acceleration.
        
            Returns:
                the satellite Y acceleration in m/s²
        
        
        """
        ...
    def getZ(self) -> float:
        """
            Getter for the satellite Z position.
        
            Returns:
                the satellite Z position in meters
        
        
        """
        ...
    def getZDot(self) -> float:
        """
            Getter for the satellite Z velocity.
        
            Returns:
                the satellite Z velocity in m/s
        
        
        """
        ...
    def getZDotDot(self) -> float:
        """
            Getter for the satellite Z acceleration.
        
            Returns:
                the satellite Z acceleration in m/s²
        
        
        """
        ...
    def setDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the reference date of the ephemeris.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the date to set
        
        
        """
        ...
    def setEpochToc(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the time of clock epoch.
        
            Parameters:
                epochToc (:class:`~org.orekit.time.AbsoluteDate`): the epoch to set
        
        
        """
        ...
    def setHealth(self, double: float) -> None:
        """
            Setter for the health status.
        
            Parameters:
                health (double): the health status to set
        
        
        """
        ...
    def setPRN(self, int: int) -> None:
        """
            Setter for the PRN number of the satellite.
        
            Parameters:
                number (int): the prn number ot set
        
        
        """
        ...
    def setX(self, double: float) -> None:
        """
            Setter for the satellite X position.
        
            Parameters:
                x (double): satellite X position (meters) to set
        
        
        """
        ...
    def setXDot(self, double: float) -> None:
        """
            Setter for the satellite X velocity.
        
            Parameters:
                vx (double): the satellite X velocity (m/s) to set
        
        
        """
        ...
    def setXDotDot(self, double: float) -> None:
        """
            Setter for the satellite X acceleration.
        
            Parameters:
                ax (double): the satellite X acceleration (m/s²) to set
        
        
        """
        ...
    def setY(self, double: float) -> None:
        """
            Setter for the satellite Y position.
        
            Parameters:
                y (double): satellite Y position (meters) to set
        
        
        """
        ...
    def setYDot(self, double: float) -> None:
        """
            Setter for the satellite Y velocity.
        
            Parameters:
                vy (double): the satellite Y velocity (m/s) to set
        
        
        """
        ...
    def setYDotDot(self, double: float) -> None:
        """
            Setter for the satellite Y acceleration.
        
            Parameters:
                ay (double): the satellite Y acceleration (m/s²) to set
        
        
        """
        ...
    def setZ(self, double: float) -> None:
        """
            Setter for the satellite Z position.
        
            Parameters:
                z (double): satellite Z position (meters) to set
        
        
        """
        ...
    def setZDot(self, double: float) -> None:
        """
            Setter for the satellite Z velocity.
        
            Parameters:
                vz (double): the satellite Z velocity (m/s) to set
        
        
        """
        ...
    def setZDotDot(self, double: float) -> None:
        """
            Setter for the satellite Z acceleration.
        
            Parameters:
                az (double): the satellite Z acceleration (m/s²) to set
        
        
        """
        ...

class BeidouSatelliteType(java.lang.Enum['BeidouSatelliteType']):
    """
    public enum BeidouSatelliteType extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.propagation.analytical.gnss.data.BeidouSatelliteType`>
    
        Enumerate for Beidou satellite type.
    
        Since:
            12.0
    """
    RESERVED: typing.ClassVar['BeidouSatelliteType'] = ...
    GEO: typing.ClassVar['BeidouSatelliteType'] = ...
    IGSO: typing.ClassVar['BeidouSatelliteType'] = ...
    MEO: typing.ClassVar['BeidouSatelliteType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BeidouSatelliteType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['BeidouSatelliteType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (BeidouSatelliteType c : BeidouSatelliteType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_FieldGNSSClockElements__T = typing.TypeVar('_FieldGNSSClockElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGNSSClockElements(org.orekit.time.FieldTimeStamped[_FieldGNSSClockElements__T], typing.Generic[_FieldGNSSClockElements__T]):
    """
    public interface FieldGNSSClockElements<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.time.FieldTimeStamped`<T>
    
        This interface provides the minimal set of clock elements needed by the
        :class:`~org.orekit.propagation.analytical.gnss.FieldClockCorrectionsProvider`.
    
        Since:
            13.0
    """
    def getAf0(self) -> _FieldGNSSClockElements__T:
        """
            Gets the Zeroth Order Clock Correction.
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf1(self) -> _FieldGNSSClockElements__T:
        """
            Gets the First Order Clock Correction.
        
            Returns:
                the First Order Clock Correction (s/s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf2(self) -> _FieldGNSSClockElements__T:
        """
            Gets the Second Order Clock Correction.
        
            Returns:
                the Second Order Clock Correction (s/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf1`
        
        
        """
        ...
    def getTGD(self) -> _FieldGNSSClockElements__T:
        """
            Get the estimated group delay differential TGD for L1-L2 correction.
        
            Returns:
                the estimated group delay differential TGD for L1-L2 correction (s)
        
        
        """
        ...
    def getToc(self) -> _FieldGNSSClockElements__T:
        """
            Get the time of clock.
        
            Returns:
                the time of clock (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf2`
        
        
        """
        ...

class GLONASSOrbitalElements(org.orekit.time.TimeStamped):
    """
    public interface GLONASSOrbitalElements extends :class:`~org.orekit.time.TimeStamped`
    
        This interface provides the minimal set of orbital elements needed by the
        :class:`~org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator` and the
        :class:`~org.orekit.propagation.numerical.GLONASSNumericalPropagator`.
    
        Because input data are different between numerical and analytical GLONASS propagators the methods present in this
        interface are implemented by default. Depending if the user wants to use a
        :class:`~org.orekit.propagation.numerical.GLONASSNumericalPropagator` or a
        :class:`~org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator` he can create an instance of a
        :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSEphemeris` or
        :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac`.
    
        Since:
            10.0
    
        Also see:
            ` GLONASS Interface Control Document
            <http://russianspacesystems.ru/wp-content/uploads/2016/08/ICD-GLONASS-CDMA-General.-Edition-1.0-2016.pdf>`
    """
    def getDeltaI(self) -> float:
        """
            Get the correction to the mean value of inclination.
        
            Returns:
                the correction to the mean value of inclination (rad)
        
        
        """
        ...
    def getDeltaT(self) -> float:
        """
            Get the correction to the mean value of Draconian period.
        
            Returns:
                the correction to the mean value of Draconian period (s)
        
        
        """
        ...
    def getDeltaTDot(self) -> float:
        """
            Get the rate of change of Draconian period.
        
            Returns:
                the rate of change of Draconian period
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the Eccentricity.
        
            Returns:
                the Eccentricity
        
        
        """
        ...
    def getGammaN(self) -> float:
        """
            Get the relative deviation of predicted satellite carrier frequency from nominal value.
        
            Returns:
                the relative deviation of predicted satellite carrier frequency from nominal value
        
        
        """
        ...
    def getIOD(self) -> int:
        """
            Gets the GLONASS Issue Of Data (IOD).
        
            Returns:
                the IOD
        
        
        """
        ...
    def getLambda(self) -> float:
        """
            Get the longitude of ascending node of orbit.
        
            Returns:
                the longitude of ascending node of orbit (rad)
        
        
        """
        ...
    def getN4(self) -> int:
        """
            Get the number of the current four year interval.
        
            Returns:
                the number of the current four year interval
        
        
        """
        ...
    def getNa(self) -> int:
        """
            Get the number of the current day in a four year interval.
        
            Returns:
                the number of the current day in a four year interval
        
        
        """
        ...
    def getPa(self) -> float:
        """
            Get the Argument of Perigee.
        
            Returns:
                the Argument of Perigee (rad)
        
        
        """
        ...
    def getTN(self) -> float:
        """
            Get the correction to the satellite time relative to GLONASS system time.
        
            Returns:
                the correction to the satellite time relative to GLONASS system time (s)
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Get the Reference Time.
        
            Returns:
                the Reference Time (s)
        
        
        """
        ...
    def getX(self) -> float:
        """
            Get the ECEF-X component of satellite coordinates in PZ-90 datum.
        
            Returns:
                the ECEF-X component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getXDot(self) -> float:
        """
            Get the ECEF-X component of satellite velocity vector in PZ-90 datum.
        
            Returns:
                the the ECEF-X component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getXDotDot(self) -> float:
        """
            Get the GLONASS ECEF-X component of satellite acceleration vector in PZ-90 datum.
        
            Returns:
                the GLONASS ECEF-X component of satellite acceleration vector in PZ-90 datum (m/s²)
        
        
        """
        ...
    def getY(self) -> float:
        """
            Get the ECEF-Y component of satellite coordinates in PZ-90 datum.
        
            Returns:
                the ECEF-Y component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getYDot(self) -> float:
        """
            Get the ECEF-Y component of satellite velocity vector in PZ-90 datum.
        
            Returns:
                the ECEF-Y component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getYDotDot(self) -> float:
        """
            Get the GLONASS ECEF-Y component of satellite acceleration vector in PZ-90 datum.
        
            Returns:
                the GLONASS ECEF-Y component of satellite acceleration vector in PZ-90 datum (m/s²)
        
        
        """
        ...
    def getZ(self) -> float:
        """
            Get the ECEF-Z component of satellite coordinates in PZ-90 datum.
        
            Returns:
                the ECEF-Z component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getZDot(self) -> float:
        """
            Get the ECEF-Z component of satellite velocity vector in PZ-90 datum.
        
            Returns:
                the the ECEF-Z component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getZDotDot(self) -> float:
        """
            Get the GLONASS ECEF-Z component of satellite acceleration vector in PZ-90 datum.
        
            Returns:
                the GLONASS ECEF-Z component of satellite acceleration vector in PZ-90 datum (m/s²)
        
        
        """
        ...

class GNSSClockElements(org.orekit.time.TimeStamped):
    """
    public interface GNSSClockElements extends :class:`~org.orekit.time.TimeStamped`
    
        This interface provides the minimal set of clock elements needed by the
        :class:`~org.orekit.propagation.analytical.gnss.ClockCorrectionsProvider`.
    
        Since:
            11.0
    """
    def getAf0(self) -> float:
        """
            Gets the Zeroth Order Clock Correction.
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf1(self) -> float:
        """
            Gets the First Order Clock Correction.
        
            Returns:
                the First Order Clock Correction (s/s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf2(self) -> float:
        """
            Gets the Second Order Clock Correction.
        
            Returns:
                the Second Order Clock Correction (s/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1`
        
        
        """
        ...
    def getTGD(self) -> float:
        """
            Get the estimated group delay differential TGD for L1-L2 correction.
        
            Returns:
                the estimated group delay differential TGD for L1-L2 correction (s)
        
        
        """
        ...
    def getToc(self) -> float:
        """
            Get the time of clock.
        
            Returns:
                the time of clock (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`
        
        
        """
        ...

class GNSSConstants:
    """
    public interface GNSSConstants
    
        Set of useful physical constants used in Global Navigation Satellite Systems (GNSS).
    """
    GNSS_PI: typing.ClassVar[float] = ...
    """
    static final double GNSS_PI
    
        Value of Pi for conversion from semicircles to radians in GNSS.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GNSS_WEEK_IN_SECONDS: typing.ClassVar[float] = ...
    """
    static final double GNSS_WEEK_IN_SECONDS
    
        Duration of the GNSS week in seconds.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BEIDOU_MU: typing.ClassVar[float] = ...
    """
    static final double BEIDOU_MU
    
        Earth's universal gravitational parameter for Beidou user in m³/s².
    
        Also see:
            :meth:`~constant`
    
    
    """
    BEIDOU_WEEK_NB: typing.ClassVar[int] = ...
    """
    static final int BEIDOU_WEEK_NB
    
        Number of weeks in the Beidou cycle.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BEIDOU_AV: typing.ClassVar[float] = ...
    """
    static final double BEIDOU_AV
    
        Value of the earth's rotation rate in rad/s for Beidou user.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GALILEO_MU: typing.ClassVar[float] = ...
    """
    static final double GALILEO_MU
    
        Earth's universal gravitational parameter for Galileo user in m³/s².
    
        Also see:
            :meth:`~constant`
    
    
    """
    GALILEO_WEEK_NB: typing.ClassVar[int] = ...
    """
    static final int GALILEO_WEEK_NB
    
        Number of weeks in the Galileo cycle.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GALILEO_AV: typing.ClassVar[float] = ...
    """
    static final double GALILEO_AV
    
        Value of the earth's rotation rate in rad/s for Galileo user.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GLONASS_MU: typing.ClassVar[float] = ...
    """
    static final double GLONASS_MU
    
        Value of the Earth's universal gravitational parameter for GLONASS user in m³/s².
    
        Also see:
            :meth:`~constant`
    
    
    """
    GLONASS_PI: typing.ClassVar[float] = ...
    """
    static final double GLONASS_PI
    
        Value of Pi for conversion from semicircles to radian.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GPS_MU: typing.ClassVar[float] = ...
    """
    static final double GPS_MU
    
        WGS 84 value of the Earth's universal gravitational parameter for GPS user in m³/s².
    
        Also see:
            :meth:`~constant`
    
    
    """
    GPS_WEEK_NB: typing.ClassVar[int] = ...
    """
    static final int GPS_WEEK_NB
    
        Number of weeks in the GPS cycle.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GPS_AV: typing.ClassVar[float] = ...
    """
    static final double GPS_AV
    
        Value of the earth's rotation rate in rad/s for GPS user.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NAVIC_MU: typing.ClassVar[float] = ...
    """
    static final double NAVIC_MU
    
        WGS 84 value of the Earth's universal gravitational parameter for NavIC user in m³/s².
    
        Also see:
            :meth:`~constant`
    
    
    """
    NAVIC_WEEK_NB: typing.ClassVar[int] = ...
    """
    static final int NAVIC_WEEK_NB
    
        Number of weeks in the NavIC cycle.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NAVIC_AV: typing.ClassVar[float] = ...
    """
    static final double NAVIC_AV
    
        Value of the earth's rotation rate in rad/s for NavIC user.
    
        Also see:
            :meth:`~constant`
    
    
    """
    QZSS_MU: typing.ClassVar[float] = ...
    """
    static final double QZSS_MU
    
        WGS 84 value of the Earth's universal gravitational parameter for QZSS user in m³/s².
    
        Also see:
            :meth:`~constant`
    
    
    """
    QZSS_WEEK_NB: typing.ClassVar[int] = ...
    """
    static final int QZSS_WEEK_NB
    
        Number of weeks in the QZSS cycle.
    
        Also see:
            :meth:`~constant`
    
    
    """
    QZSS_AV: typing.ClassVar[float] = ...
    """
    static final double QZSS_AV
    
        Value of the earth's rotation rate in rad/s for QZSS user.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SBAS_MU: typing.ClassVar[float] = ...
    """
    static final double SBAS_MU
    
        WGS 84 value of the Earth's universal gravitational parameter for SBAS user in m³/s².
    
        Also see:
            :meth:`~constant`
    
    
    """

class GNSSOrbitalElementsDriversProvider(org.orekit.utils.ParameterDriversProvider):
    """
    public abstract class GNSSOrbitalElementsDriversProvider extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.utils.ParameterDriversProvider`
    
        This class manages the non-keplerian parameter drivers for
        :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements` and
        :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`.
    
        In both primitive double and field classes, only the non-Keplerian parameters are returned in the
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers` method, the
        Keplerian orbital parameters must be accessed independently. These groups ensure proper separate computation of state
        transition matrix and Jacobian matrix by :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator` and
        :class:`~org.orekit.propagation.analytical.gnss.FieldGnssPropagator`.
    
        Since:
            13.0
    """
    TIME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TIME
    
        Name for time parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INCLINATION_RATE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` INCLINATION_RATE
    
        Name for inclination rate parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    LONGITUDE_RATE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` LONGITUDE_RATE
    
        Name for longitude rate parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    LATITUDE_COSINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` LATITUDE_COSINE
    
        Name for cosine of latitude argument harmonic parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    LATITUDE_SINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` LATITUDE_SINE
    
        Name for sine of latitude argument harmonic parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    RADIUS_COSINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` RADIUS_COSINE
    
        Name for cosine of orbit radius harmonic parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    RADIUS_SINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` RADIUS_SINE
    
        Name for sine of orbit radius harmonic parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INCLINATION_COSINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` INCLINATION_COSINE
    
        Name for cosine of inclination harmonic parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INCLINATION_SINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` INCLINATION_SINE
    
        Name for sine of inclination harmonic parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TIME_INDEX: typing.ClassVar[int] = ...
    """
    public static final int TIME_INDEX
    
        Index of time in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    I_DOT_INDEX: typing.ClassVar[int] = ...
    """
    public static final int I_DOT_INDEX
    
        Index of inclination rate in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    OMEGA_DOT_INDEX: typing.ClassVar[int] = ...
    """
    public static final int OMEGA_DOT_INDEX
    
        Index of longitude rate in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CUC_INDEX: typing.ClassVar[int] = ...
    """
    public static final int CUC_INDEX
    
        Index of cosine on latitude argument in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CUS_INDEX: typing.ClassVar[int] = ...
    """
    public static final int CUS_INDEX
    
        Index of sine on latitude argument in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CRC_INDEX: typing.ClassVar[int] = ...
    """
    public static final int CRC_INDEX
    
        Index of cosine on radius in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CRS_INDEX: typing.ClassVar[int] = ...
    """
    public static final int CRS_INDEX
    
        Index of sine on radius in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CIC_INDEX: typing.ClassVar[int] = ...
    """
    public static final int CIC_INDEX
    
        Index of cosine on inclination in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CIS_INDEX: typing.ClassVar[int] = ...
    """
    public static final int CIS_INDEX
    
        Index of sine on inclination in the list returned by
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SIZE: typing.ClassVar[int] = ...
    """
    public static final int SIZE
    
        Size of parameters array.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getAngularVelocity(self) -> float:
        """
            Get the mean angular velocity of the Earth of the GNSS model.
        
            Returns:
                mean angular velocity of the Earth of the GNSS model
        
        
        """
        ...
    def getCic(self) -> float:
        """
            Get amplitude of the cosine harmonic correction term to the angle of inclination.
        
            Returns:
                amplitude of the cosine harmonic correction term to the angle of inclination (rad)
        
        
        """
        ...
    def getCicDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the amplitude of the cosine harmonic correction term to the angle of inclination.
        
            Returns:
                driver for the amplitude of the cosine harmonic correction term to the angle of inclination (rad)
        
        
        """
        ...
    def getCis(self) -> float:
        """
            Get amplitude of the sine harmonic correction term to the angle of inclination.
        
            Returns:
                amplitude of the sine harmonic correction term to the angle of inclination (rad)
        
        
        """
        ...
    def getCisDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the amplitude of the sine harmonic correction term to the angle of inclination.
        
            Returns:
                driver for the amplitude of the sine harmonic correction term to the angle of inclination (rad)
        
        
        """
        ...
    def getCrc(self) -> float:
        """
            Get amplitude of the cosine harmonic correction term to the orbit radius.
        
            Returns:
                amplitude of the cosine harmonic correction term to the orbit radius (m)
        
        
        """
        ...
    def getCrcDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the amplitude of the cosine harmonic correction term to the orbit radius.
        
            Returns:
                driver for the amplitude of the cosine harmonic correction term to the orbit radius (m)
        
        
        """
        ...
    def getCrs(self) -> float:
        """
            Get amplitude of the sine harmonic correction term to the orbit radius.
        
            Returns:
                amplitude of the sine harmonic correction term to the orbit radius (m)
        
        
        """
        ...
    def getCrsDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the amplitude of the sine harmonic correction term to the orbit radius.
        
            Returns:
                driver for the amplitude of the sine harmonic correction term to the orbit radius (m)
        
        
        """
        ...
    def getCuc(self) -> float:
        """
            Get amplitude of the cosine harmonic correction term to the argument of latitude.
        
            Returns:
                amplitude of the cosine harmonic correction term to the argument of latitude (rad)
        
        
        """
        ...
    def getCucDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the amplitude of the cosine harmonic correction term to the argument of latitude.
        
            Returns:
                driver for the amplitude of the cosine harmonic correction term to the argument of latitude (rad)
        
        
        """
        ...
    def getCus(self) -> float:
        """
            Get amplitude of the sine harmonic correction term to the argument of latitude.
        
            Returns:
                amplitude of the sine harmonic correction term to the argument of latitude (rad)
        
        
        """
        ...
    def getCusDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the amplitude of the sine harmonic correction term to the argument of latitude.
        
            Returns:
                driver for the amplitude of the sine harmonic correction term to the argument of latitude (rad)
        
        
        """
        ...
    def getCycleDuration(self) -> float:
        """
            Get for the duration of the GNSS cycle in seconds.
        
            Returns:
                the duration of the GNSS cycle in seconds
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get rate of inclination angle.
        
            Returns:
                rate of inclination angle (rad/s)
        
        
        """
        ...
    def getIDotDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the rate of inclination angle.
        
            Returns:
                driver for the rate of inclination angle (rad/s)
        
        
        """
        ...
    def getOmegaDot(self) -> float:
        """
            Get rate of right ascension.
        
            Returns:
                rate of right ascension (rad/s)
        
        
        """
        ...
    def getOmegaDotDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the rate of right ascension.
        
            Returns:
                driver for the rate of right ascension (rad/s)
        
        
        """
        ...
    def getPRN(self) -> int:
        """
            Get the PRN number of the satellite.
        
            Returns:
                PRN number of the satellite
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get satellite system.
        
            Returns:
                satellite system
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Get reference time of the GNSS orbit as a duration from week start.
        
            Returns:
                reference time of the GNSS orbit (s)
        
        
        """
        ...
    def getTimeDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for reference time of the GNSS orbit as a duration from week start.
        
            Returns:
                driver for the reference time of the GNSS orbit (s)
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
            Get known time scales.
        
            Returns:
                known time scales
        
        
        """
        ...
    def getWeek(self) -> int:
        """
            Get the reference week of the orbit.
        
            Returns:
                reference week of the orbit
        
        
        """
        ...
    def getWeeksInCycle(self) -> int:
        """
            Get for the duration of the GNSS cycle in weeks.
        
            Returns:
                the duration of the GNSS cycle in weeks
        
        
        """
        ...
    def setCic(self, double: float) -> None:
        """
            Set amplitude of the cosine harmonic correction term to the angle of inclination.
        
            Parameters:
                cic (double): amplitude of the cosine harmonic correction term to the angle of inclination (rad)
        
        
        """
        ...
    def setCis(self, double: float) -> None:
        """
            Set amplitude of the sine harmonic correction term to the angle of inclination.
        
            Parameters:
                cis (double): amplitude of the sine harmonic correction term to the angle of inclination (rad)
        
        
        """
        ...
    def setCrc(self, double: float) -> None:
        """
            Set amplitude of the cosine harmonic correction term to the orbit radius.
        
            Parameters:
                crc (double): amplitude of the cosine harmonic correction term to the orbit radius (m)
        
        
        """
        ...
    def setCrs(self, double: float) -> None:
        """
            Set amplitude of the sine harmonic correction term to the orbit radius.
        
            Parameters:
                crs (double): amplitude of the sine harmonic correction term to the orbit radius (m)
        
        
        """
        ...
    def setCuc(self, double: float) -> None:
        """
            Set amplitude of the cosine harmonic correction term to the argument of latitude.
        
            Parameters:
                cuc (double): amplitude of the cosine harmonic correction term to the argument of latitude (rad)
        
        
        """
        ...
    def setCus(self, double: float) -> None:
        """
            Set amplitude of the sine harmonic correction term to the argument of latitude.
        
            Parameters:
                cus (double): amplitude of the sine harmonic correction term to the argument of latitude (rad)
        
        
        """
        ...
    def setIDot(self, double: float) -> None:
        """
            Set the driver for the rate of inclination angle.
        
            Parameters:
                iDot (double): rate of inclination angle (rad/s)
        
        
        """
        ...
    def setOmegaDot(self, double: float) -> None:
        """
            Set rate of right ascension.
        
            Parameters:
                dom (double): rate of right ascension (rad/s)
        
        
        """
        ...
    def setPRN(self, int: int) -> None:
        """
            Set the PRN number of the satellite.
        
            Parameters:
                number (int): the prn number ot set
        
        
        """
        ...
    def setTime(self, double: float) -> None:
        """
            Set reference time of the GNSS orbit as a duration from week start.
        
            Parameters:
                time (double): reference time of the GNSS orbit (s)
        
        
        """
        ...
    def setWeek(self, int: int) -> None:
        """
            Set the reference week of the orbit.
        
            Parameters:
                week (int): the week to set
        
        
        """
        ...

class SBASOrbitalElements(org.orekit.time.TimeStamped):
    """
    public interface SBASOrbitalElements extends :class:`~org.orekit.time.TimeStamped`
    
        This interface provides the minimal set of orbital elements needed by the
        :class:`~org.orekit.propagation.analytical.gnss.SBASPropagator`.
    
        Since:
            10.1
    """
    def getAGf0(self) -> float:
        """
            Gets the Zeroth Order Clock Correction.
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
        
        """
        ...
    def getAGf1(self) -> float:
        """
            Gets the First Order Clock Correction.
        
            Returns:
                the First Order Clock Correction (s/s)
        
        
        """
        ...
    def getIODN(self) -> int:
        """
            Gets the Issue Of Data Navigation (IODN).
        
            Returns:
                the IODN
        
        
        """
        ...
    def getPRN(self) -> int:
        """
            Gets the PRN number of the SBAS satellite.
        
            Returns:
                the PRN number of the SBAS satellite
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Gets the Reference Time of the SBAS orbit in GPS seconds of the week.
        
            Returns:
                the Reference Time of the SBAS orbit (s)
        
        
        """
        ...
    def getToc(self) -> float:
        """
            Gets the clock correction reference time toc.
        
            Returns:
                the clock correction reference time (s)
        
        
        """
        ...
    def getWeek(self) -> int:
        """
            Gets the Reference Week of the SBAS orbit.
        
            Returns:
                the Reference Week of the SBAS orbit
        
        
        """
        ...
    def getX(self) -> float:
        """
            Get the ECEF-X component of satellite coordinates.
        
            Returns:
                the ECEF-X component of satellite coordinates (m)
        
        
        """
        ...
    def getXDot(self) -> float:
        """
            Get the ECEF-X component of satellite velocity vector.
        
            Returns:
                the the ECEF-X component of satellite velocity vector (m/s)
        
        
        """
        ...
    def getXDotDot(self) -> float:
        """
            Get the ECEF-X component of satellite acceleration vector.
        
            Returns:
                the GLONASS ECEF-X component of satellite acceleration vector (m/s²)
        
        
        """
        ...
    def getY(self) -> float:
        """
            Get the ECEF-Y component of satellite coordinates.
        
            Returns:
                the ECEF-Y component of satellite coordinates (m)
        
        
        """
        ...
    def getYDot(self) -> float:
        """
            Get the ECEF-Y component of satellite velocity vector.
        
            Returns:
                the ECEF-Y component of satellite velocity vector (m/s)
        
        
        """
        ...
    def getYDotDot(self) -> float:
        """
            Get the ECEF-Y component of satellite acceleration vector.
        
            Returns:
                the ECEF-Y component of satellite acceleration vector (m/s²)
        
        
        """
        ...
    def getZ(self) -> float:
        """
            Get the ECEF-Z component of satellite coordinates.
        
            Returns:
                the ECEF-Z component of satellite coordinates (m)
        
        
        """
        ...
    def getZDot(self) -> float:
        """
            Get the ECEF-Z component of satellite velocity vector.
        
            Returns:
                the the ECEF-Z component of satellite velocity vector (m/s)
        
        
        """
        ...
    def getZDotDot(self) -> float:
        """
            Get the ECEF-Z component of satellite acceleration vector.
        
            Returns:
                the ECEF-Z component of satellite acceleration vector (m/s²)
        
        
        """
        ...

_FieldGnssOrbitalElements__T = typing.TypeVar('_FieldGnssOrbitalElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldGnssOrbitalElements__O = typing.TypeVar('_FieldGnssOrbitalElements__O', bound='GNSSOrbitalElements')  # <O>
class FieldGnssOrbitalElements(GNSSOrbitalElementsDriversProvider, org.orekit.time.FieldTimeStamped[_FieldGnssOrbitalElements__T], typing.Generic[_FieldGnssOrbitalElements__T, _FieldGnssOrbitalElements__O]):
    """
    public abstract class FieldGnssOrbitalElements<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>, O extends :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider` implements :class:`~org.orekit.time.FieldTimeStamped`<T>
    
        This class provides the minimal set of orbital elements needed by the
        :class:`~org.orekit.propagation.analytical.gnss.FieldGnssPropagator`.
    
        Since:
            13.0
    """
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound='FieldGnssOrbitalElements')  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldGnssOrbitalElements__T, _changeField__U], typing.Callable[[_FieldGnssOrbitalElements__T], _changeField__U]]) -> _changeField__G: ...
    def getADot(self) -> _FieldGnssOrbitalElements__T:
        """
            Getter for the change rate in semi-major axis.
        
            This value is non-zero only in civilian navigation messages
        
            Returns:
                the change rate in semi-major axis
        
            Since:
                13.0
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldGnssOrbitalElements__T]: ...
    def getDeltaN0(self) -> _FieldGnssOrbitalElements__T:
        """
            Getter for the delta of satellite mean motion.
        
            This value is non-zero only in navigation messages
        
            Returns:
                delta of satellite mean motion
        
            Since:
                13.0
        
        
        """
        ...
    def getDeltaN0Dot(self) -> _FieldGnssOrbitalElements__T:
        """
            Getter for change rate in Δn₀.
        
            This value is non-zero only in civilian navigation messages
        
            Returns:
                change rate in Δn₀
        
            Since:
                13.0
        
        
        """
        ...
    def getE(self) -> _FieldGnssOrbitalElements__T:
        """
            Get eccentricity.
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getI0(self) -> _FieldGnssOrbitalElements__T:
        """
            Get the inclination angle at reference time.
        
            Returns:
                inclination angle at reference time (rad)
        
        
        """
        ...
    def getM0(self) -> _FieldGnssOrbitalElements__T:
        """
            Get mean anomaly at reference time.
        
            Returns:
                mean anomaly at reference time (rad)
        
        
        """
        ...
    def getMeanMotion0(self) -> _FieldGnssOrbitalElements__T:
        """
            Get the computed mean motion n₀.
        
            Returns:
                the computed mean motion n₀ (rad/s)
        
            Since:
                13.0
        
        
        """
        ...
    def getMu(self) -> _FieldGnssOrbitalElements__T:
        """
            Get the Earth's universal gravitational parameter.
        
            Returns:
                the Earth's universal gravitational parameter
        
        
        """
        ...
    def getOmega0(self) -> _FieldGnssOrbitalElements__T:
        """
            Get longitude of ascending node of orbit plane at weekly epoch.
        
            Returns:
                longitude of ascending node of orbit plane at weekly epoch (rad)
        
        
        """
        ...
    def getPa(self) -> _FieldGnssOrbitalElements__T:
        """
            Get argument of perigee.
        
            Returns:
                argument of perigee (rad)
        
        
        """
        ...
    def getSma(self) -> _FieldGnssOrbitalElements__T:
        """
            Get semi-major axis.
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def setE(self, t: _FieldGnssOrbitalElements__T) -> None:
        """
            Set eccentricity.
        
            Parameters:
                e (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`): eccentricity
        
        
        """
        ...
    def setI0(self, t: _FieldGnssOrbitalElements__T) -> None:
        """
            Set inclination angle at reference time.
        
            Parameters:
                i0 (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`): inclination angle at reference time (rad)
        
        
        """
        ...
    def setM0(self, t: _FieldGnssOrbitalElements__T) -> None:
        """
            Set mean anomaly at reference time.
        
            Parameters:
                m0 (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`): mean anomaly at reference time (rad)
        
        
        """
        ...
    def setOmega0(self, t: _FieldGnssOrbitalElements__T) -> None:
        """
            Set longitude of ascending node of orbit plane at weekly epoch.
        
            Parameters:
                omega0 (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`): longitude of ascending node of orbit plane at weekly epoch (rad)
        
        
        """
        ...
    def setPa(self, t: _FieldGnssOrbitalElements__T) -> None:
        """
            Set argument of perigee.
        
            Parameters:
                pa (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`): argument of perigee (rad)
        
        
        """
        ...
    def setSma(self, t: _FieldGnssOrbitalElements__T) -> None:
        """
            Set semi-major axis.
        
            Parameters:
                sma (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`): demi-major axis (m)
        
        
        """
        ...
    def toNonField(self) -> _FieldGnssOrbitalElements__O:
        """
            Create a non-field version of the instance.
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

class GLONASSAlmanac(GLONASSOrbitalElements):
    """
    public class GLONASSAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
    
        This class holds a GLONASS almanac as read from .agl files.
    
        Since:
            10.0
    """
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, timeScale: org.orekit.time.TimeScale): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeStamped.getDate`
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getDeltaI(self) -> float:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaI`
            Get the correction to the mean value of inclination.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaI` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the correction to the mean value of inclination (rad)
        
        
        """
        ...
    def getDeltaT(self) -> float:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaT`
            Get the correction to the mean value of Draconian period.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaT` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the correction to the mean value of Draconian period (s)
        
        
        """
        ...
    def getDeltaTDot(self) -> float:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaTDot`
            Get the rate of change of Draconian period.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaTDot` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the rate of change of Draconian period
        
        
        """
        ...
    def getE(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getE`
            Get the Eccentricity.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getE` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Eccentricity
        
        
        """
        ...
    def getFrequencyChannel(self) -> int:
        """
            Get the frequency channel.
        
            Returns:
                the frequency channel
        
        
        """
        ...
    def getGPS2Glo(self) -> float:
        """
            Get the correction to GPS time relative GLONASS.
        
            Returns:
                the to GPS time relative GLONASS (s)
        
        
        """
        ...
    def getGlo2UTC(self) -> float:
        """
            Get the correction from GLONASS to UTC.
        
            Returns:
                the correction from GLONASS to UTC (s)
        
        
        """
        ...
    def getGloOffset(self) -> float:
        """
            Get the correction of time relative to GLONASS system time.
        
            Returns:
                the correction of time relative to GLONASS system time (s)
        
        
        """
        ...
    def getHealth(self) -> int:
        """
            Get the Health status.
        
            Returns:
                the Health status
        
        
        """
        ...
    def getLambda(self) -> float:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getLambda`
            Get the longitude of ascending node of orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getLambda` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the longitude of ascending node of orbit (rad)
        
        
        """
        ...
    def getN4(self) -> int:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getN4`
            Get the number of the current four year interval.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getN4` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current four year interval
        
        
        """
        ...
    def getNa(self) -> int:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa`
            Get the number of the current day in a four year interval.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current day in a four year interval
        
        
        """
        ...
    def getPa(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getPa`
            Get the Argument of Perigee.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getPa` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Argument of Perigee (rad)
        
        
        """
        ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator:
        """
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default to be aligned with the EME2000 frame.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The data context is by default to the :meth:`~org.orekit.data.DataContext.getDefault`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Predefined.EME2000` in the default data context.
        
        
            The ECEF frame is set by default to the :meth:`~org.orekit.frames.Predefined.ITRF_CIO_CONV_2010_SIMPLE_EOP` in the
            default data context.
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac.getPropagator`
        
        """
        ...
    @typing.overload
    def getPropagator(self, dataContext: org.orekit.data.DataContext) -> org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator:
        """
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default to be aligned with the EME2000 frame.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Frames.getEME2000`.
        
        
            The ECEF frame is set by default to the :meth:`~org.orekit.frames.Frames.getITRF`.
        
            Parameters:
                context (:class:`~org.orekit.data.DataContext`): the data context to use for frames and time scales.
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac.getPropagator`
        
            Get the propagator corresponding to the navigation message.
        
            Parameters:
                context (:class:`~org.orekit.data.DataContext`): the data context to use for frames and time scales.
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
                inertial (:class:`~org.orekit.frames.Frame`): inertial frame, use to provide the propagated orbit
                bodyFixed (:class:`~org.orekit.frames.Frame`): body fixed frame, corresponding to the navigation message
                mass (double): spacecraft mass in kg
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac.getPropagator`
        
        
        """
        ...
    @typing.overload
    def getPropagator(self, dataContext: org.orekit.data.DataContext, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, double: float) -> org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator: ...
    def getTime(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime`
            Get the Reference Time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Reference Time (s)
        
        
        """
        ...

class GLONASSEphemeris(GLONASSOrbitalElements):
    """
    public class GLONASSEphemeris extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
    
        Class for GLONASS ephemeris used by the :class:`~org.orekit.propagation.numerical.GLONASSNumericalPropagator`.
    
        Since:
            10.0
    """
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeStamped.getDate`
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getN4(self) -> int:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getN4`
            Get the number of the current four year interval.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getN4` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current four year interval
        
        
        """
        ...
    def getNa(self) -> int:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa`
            Get the number of the current day in a four year interval.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current day in a four year interval
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime`
            Get the Reference Time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Reference Time (s)
        
        
        """
        ...
    def getX(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getX`
            Get the ECEF-X component of satellite coordinates in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getX` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-X component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getXDot(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDot`
            Get the ECEF-X component of satellite velocity vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDot` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the the ECEF-X component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getXDotDot(self) -> float:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDotDot`
            Get the GLONASS ECEF-X component of satellite acceleration vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDotDot` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the GLONASS ECEF-X component of satellite acceleration vector in PZ-90 datum (m/s²)
        
        
        """
        ...
    def getY(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getY`
            Get the ECEF-Y component of satellite coordinates in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getY` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-Y component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getYDot(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDot`
            Get the ECEF-Y component of satellite velocity vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDot` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-Y component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getYDotDot(self) -> float:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDotDot`
            Get the GLONASS ECEF-Y component of satellite acceleration vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDotDot` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the GLONASS ECEF-Y component of satellite acceleration vector in PZ-90 datum (m/s²)
        
        
        """
        ...
    def getZ(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZ`
            Get the ECEF-Z component of satellite coordinates in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZ` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-Z component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getZDot(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDot`
            Get the ECEF-Z component of satellite velocity vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDot` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the the ECEF-Z component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getZDotDot(self) -> float:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDotDot`
            Get the GLONASS ECEF-Z component of satellite acceleration vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDotDot` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the GLONASS ECEF-Z component of satellite acceleration vector in PZ-90 datum (m/s²)
        
        
        """
        ...

class GLONASSNavigationMessage(AbstractEphemerisMessage, GLONASSOrbitalElements):
    """
    public class GLONASSNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractEphemerisMessage` implements :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
    
        Container for data contained in a Glonass navigation message.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getFrequencyNumber(self) -> int:
        """
            Getter for the frequency number.
        
            Returns:
                the frequency number
        
        
        """
        ...
    def getGammaN(self) -> float:
        """
            Get the relative deviation of predicted satellite carrier frequency from nominal value.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getGammaN` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the relative deviation of predicted satellite carrier frequency from nominal value
        
        
        """
        ...
    def getGroupDelayDifference(self) -> float:
        """
            Get group delay difference.
        
            Returns:
                group delay difference
        
            Since:
                12.0
        
        
        """
        ...
    def getHealthFlags(self) -> int:
        """
            Get health flags.
        
            Returns:
                health flags
        
            Since:
                12.0
        
        
        """
        ...
    @typing.overload
    def getPropagator(self, double: float) -> org.orekit.propagation.numerical.GLONASSNumericalPropagator:
        """
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default to EME2000 aligned in the default data context.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The data context is by default to the :meth:`~org.orekit.data.DataContext.getDefault`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Predefined.EME2000` in the default data context.
        
        
        
            Parameters:
                step (double): integration step in seconds
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getPropagator`
        
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default to EME2000 aligned in the default data context.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The data context is by default to the :meth:`~org.orekit.data.DataContext.getDefault`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Predefined.EME2000` in the default data context.
        
        
        
            Parameters:
                step (double): integration step in seconds
                context (:class:`~org.orekit.data.DataContext`): data context
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getPropagator`
        
            Get the propagator corresponding to the navigation message.
        
            Parameters:
                step (double): integration step in seconds
                context (:class:`~org.orekit.data.DataContext`): data context
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
                inertial (:class:`~org.orekit.frames.Frame`): inertial frame, use to provide the propagated orbit
                mass (double): spacecraft mass in kg
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage.getPropagator`
        
        
        """
        ...
    @typing.overload
    def getPropagator(self, double: float, dataContext: org.orekit.data.DataContext) -> org.orekit.propagation.numerical.GLONASSNumericalPropagator: ...
    @typing.overload
    def getPropagator(self, double: float, dataContext: org.orekit.data.DataContext, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame, double2: float) -> org.orekit.propagation.numerical.GLONASSNumericalPropagator: ...
    def getStatusFlags(self) -> int:
        """
            Get status flags.
        
            Returns:
                status flags
        
            Since:
                12.0
        
        
        """
        ...
    def getTN(self) -> float:
        """
            Get the correction to the satellite time relative to GLONASS system time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTN` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the correction to the satellite time relative to GLONASS system time (s)
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Get the Reference Time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Reference Time (s)
        
        
        """
        ...
    def getURA(self) -> float:
        """
            Getter for the user range accuray (meters).
        
            Returns:
                the user range accuracy
        
            Since:
                12.0
        
        
        """
        ...
    def setFrequencyNumber(self, double: float) -> None:
        """
            Setter for the frequency number.
        
            Parameters:
                frequencyNumber (double): the number to set
        
        
        """
        ...
    def setGammaN(self, double: float) -> None:
        """
            Setter for the SV relative frequency bias.
        
            Parameters:
                gammaN (double): the SV relative frequency bias.
        
        
        """
        ...
    def setGroupDelayDifference(self, double: float) -> None:
        """
            Set group delay difference.
        
            Parameters:
                groupDelayDifference (double): group delay difference
        
            Since:
                12.0
        
        
        """
        ...
    def setHealthFlags(self, double: float) -> None:
        """
            Set health flag.
        
            Parameters:
                healthFlags (double): health flag (parsed as a double)
        
            Since:
                12.0
        
        
        """
        ...
    def setStatusFlags(self, double: float) -> None:
        """
            Set status flag.
        
            Parameters:
                statusFlags (double): status flag (parsed as a double)
        
            Since:
                12.0
        
        
        """
        ...
    def setTauN(self, double: float) -> None:
        """
            Setter for the SV clock bias.
        
            Parameters:
                tn (double): the SV clock bias
        
        
        """
        ...
    def setTime(self, double: float) -> None:
        """
            Setter for the message frame time.
        
            Parameters:
                time (double): the time to set
        
        
        """
        ...
    def setURA(self, double: float) -> None:
        """
            Setter for the user range accuracy.
        
            Parameters:
                accuracy (double): the value to set
        
            Since:
                12.0
        
        
        """
        ...

_GNSSOrbitalElements__O = typing.TypeVar('_GNSSOrbitalElements__O', bound='GNSSOrbitalElements')  # <O>
class GNSSOrbitalElements(GNSSOrbitalElementsDriversProvider, org.orekit.time.TimeStamped, typing.Generic[_GNSSOrbitalElements__O]):
    """
    public abstract class GNSSOrbitalElements<O extends GNSSOrbitalElements<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider` implements :class:`~org.orekit.time.TimeStamped`
    
        This class provides the minimal set of orbital elements needed by the
        :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`.
    
        The parameters are split in two groups: Keplerian orbital parameters and non-Keplerian evolution parameters. All
        parameters can be updated as they are all instances of :class:`~org.orekit.utils.ParameterDriver`. Only the
        non-Keplerian parameters are returned in the
        :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElementsDriversProvider.getParametersDrivers` method, the
        Keplerian orbital parameters must be accessed independently. These groups ensure proper separate computation of state
        transition matrix and Jacobian matrix by :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`.
    
        Since:
            13.0
    """
    SEMI_MAJOR_AXIS: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SEMI_MAJOR_AXIS
    
        Name for semi major axis parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECCENTRICITY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ECCENTRICITY
    
        Name for eccentricity parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INCLINATION: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` INCLINATION
    
        Name for inclination at reference time parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ARGUMENT_OF_PERIGEE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ARGUMENT_OF_PERIGEE
    
        Name for argument of perigee parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NODE_LONGITUDE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` NODE_LONGITUDE
    
        Name for longitude of ascending node at weekly epoch parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN_ANOMALY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEAN_ANOMALY
    
        Name for mean anomaly at reference time parameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getADot(self) -> float:
        """
            Getter for the change rate in semi-major axis.
        
            This value is non-zero only in civilian navigation messages
        
            Returns:
                the change rate in semi-major axis
        
            Since:
                13.0
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getDeltaN0(self) -> float:
        """
            Getter for the delta of satellite mean motion.
        
            This value is non-zero only in navigation messages
        
            Returns:
                delta of satellite mean motion
        
            Since:
                13.0
        
        
        """
        ...
    def getDeltaN0Dot(self) -> float:
        """
            Getter for change rate in Δn₀.
        
            This value is non-zero only in civilian navigation messages
        
            Returns:
                change rate in Δn₀
        
            Since:
                13.0
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get eccentricity.
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the eccentricity.
        
            Returns:
                driver for the eccentricity
        
        
        """
        ...
    def getI0(self) -> float:
        """
            Get the inclination angle at reference time.
        
            Returns:
                inclination angle at reference time (rad)
        
        
        """
        ...
    def getI0Driver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the inclination angle at reference time.
        
            Returns:
                driver for the inclination angle at reference time (rad)
        
        
        """
        ...
    def getM0(self) -> float:
        """
            Get mean anomaly at reference time.
        
            Returns:
                mean anomaly at reference time (rad)
        
        
        """
        ...
    def getM0Driver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the mean anomaly at reference time.
        
            Returns:
                driver for the mean anomaly at reference time (rad)
        
        
        """
        ...
    def getMeanMotion0(self) -> float:
        """
            Get the computed mean motion n₀.
        
            Returns:
                the computed mean motion n₀ (rad/s)
        
            Since:
                13.0
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the Earth's universal gravitational parameter.
        
            Returns:
                the Earth's universal gravitational parameter
        
        
        """
        ...
    def getOmega0(self) -> float:
        """
            Get longitude of ascending node of orbit plane at weekly epoch.
        
            Returns:
                longitude of ascending node of orbit plane at weekly epoch (rad)
        
        
        """
        ...
    def getOmega0Driver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the longitude of ascending node of orbit plane at weekly epoch.
        
            Returns:
                driver for the longitude of ascending node of orbit plane at weekly epoch (rad)
        
        
        """
        ...
    def getPa(self) -> float:
        """
            Get argument of perigee.
        
            Returns:
                argument of perigee (rad)
        
        
        """
        ...
    def getPaDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get the driver for the argument of perigee.
        
            Returns:
                driver for the argument of perigee (rad)
        
        
        """
        ...
    def getSma(self) -> float:
        """
            Get semi-major axis.
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getSmaDriver(self) -> org.orekit.utils.ParameterDriver:
        """
            Get semi-major axis.
        
            Returns:
                driver for the semi-major axis (m)
        
        
        """
        ...
    def setE(self, double: float) -> None:
        """
            Set eccentricity.
        
            Parameters:
                e (double): eccentricity
        
        
        """
        ...
    def setI0(self, double: float) -> None:
        """
            Set inclination angle at reference time.
        
            Parameters:
                i0 (double): inclination angle at reference time (rad)
        
        
        """
        ...
    def setM0(self, double: float) -> None:
        """
            Set mean anomaly at reference time.
        
            Parameters:
                anom (double): mean anomaly at reference time (rad)
        
        
        """
        ...
    def setOmega0(self, double: float) -> None:
        """
            Set longitude of ascending node of orbit plane at weekly epoch.
        
            Parameters:
                om0 (double): longitude of ascending node of orbit plane at weekly epoch (rad)
        
        
        """
        ...
    def setPa(self, double: float) -> None:
        """
            Set argument of perigee.
        
            Parameters:
                aop (double): argument of perigee (rad)
        
        
        """
        ...
    def setSma(self, double: float) -> None:
        """
            Set semi-major axis.
        
            Parameters:
                sma (double): demi-major axis (m)
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

_PythonFieldGNSSClockElements__T = typing.TypeVar('_PythonFieldGNSSClockElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldGNSSClockElements(FieldGNSSClockElements[_PythonFieldGNSSClockElements__T], typing.Generic[_PythonFieldGNSSClockElements__T]):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAf0(self) -> _PythonFieldGNSSClockElements__T: ...
    def getAf1(self) -> _PythonFieldGNSSClockElements__T: ...
    def getAf2(self) -> _PythonFieldGNSSClockElements__T: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldGNSSClockElements__T]: ...
    def getTGD(self) -> _PythonFieldGNSSClockElements__T: ...
    def getToc(self) -> _PythonFieldGNSSClockElements__T: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonSBASOrbitalElements(SBASOrbitalElements):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAGf0(self) -> float: ...
    def getAGf1(self) -> float: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getIODN(self) -> int: ...
    def getPRN(self) -> int: ...
    def getTime(self) -> float: ...
    def getToc(self) -> float: ...
    def getWeek(self) -> int: ...
    def getX(self) -> float: ...
    def getXDot(self) -> float: ...
    def getXDotDot(self) -> float: ...
    def getY(self) -> float: ...
    def getYDot(self) -> float: ...
    def getYDotDot(self) -> float: ...
    def getZ(self) -> float: ...
    def getZDot(self) -> float: ...
    def getZDotDot(self) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class SBASNavigationMessage(AbstractEphemerisMessage, SBASOrbitalElements):
    """
    public class SBASNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractEphemerisMessage` implements :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
    
        Container for data contained in a SBAS navigation message.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getAGf0(self) -> float:
        """
            Gets the Zeroth Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getAGf0` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
        
        """
        ...
    def getAGf1(self) -> float:
        """
            Gets the First Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getAGf1` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the First Order Clock Correction (s/s)
        
        
        """
        ...
    def getIODN(self) -> int:
        """
            Gets the Issue Of Data Navigation (IODN).
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getIODN` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the IODN
        
        
        """
        ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.analytical.gnss.SBASPropagator:
        """
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default be aligned with the EME2000 frame.
        
        
            The Earth gravity coefficient is set by default to the
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSConstants.SBAS_MU`.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Predefined.EME2000`.
        
        
            The ECEF frame is set by default to the :meth:`~org.orekit.frames.Predefined.ITRF_CIO_CONV_2010_SIMPLE_EOP`.
        
            This constructor uses the :meth:`~org.orekit.data.DataContext.getDefault`
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage.getPropagator`
        
        """
        ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames) -> org.orekit.propagation.analytical.gnss.SBASPropagator:
        """
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default be aligned with the EME2000 frame.
        
        
            The Earth gravity coefficient is set by default to the
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSConstants.SBAS_MU`.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Predefined.EME2000`.
        
        
            The ECEF frame is set by default to the :meth:`~org.orekit.frames.Predefined.ITRF_CIO_CONV_2010_SIMPLE_EOP`.
        
            Parameters:
                frames (:class:`~org.orekit.frames.Frames`): set of frames to use
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage.getPropagator`
        
            Get the propagator corresponding to the navigation message.
        
            Parameters:
                frames (:class:`~org.orekit.frames.Frames`): set of frames to use
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
                inertial (:class:`~org.orekit.frames.Frame`): inertial frame, use to provide the propagated orbit
                bodyFixed (:class:`~org.orekit.frames.Frame`): body fixed frame, corresponding to the navigation message
                mass (double): spacecraft mass in kg
                mu (double): central attraction coefficient
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage.getPropagator`
        
        
        """
        ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame2: org.orekit.frames.Frame, frame3: org.orekit.frames.Frame, double: float, double2: float) -> org.orekit.propagation.analytical.gnss.SBASPropagator: ...
    def getTime(self) -> float:
        """
            Gets the Reference Time of the SBAS orbit in GPS seconds of the week.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getTime` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the Reference Time of the SBAS orbit (s)
        
        
        """
        ...
    def getURA(self) -> float:
        """
            Getter for the user range accuray (meters).
        
            Returns:
                the user range accuracy
        
        
        """
        ...
    def getWeek(self) -> int:
        """
            Gets the Reference Week of the SBAS orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getWeek` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the Reference Week of the SBAS orbit
        
        
        """
        ...
    def setAGf0(self, double: float) -> None:
        """
            Setter for the SV clock bias.
        
            Parameters:
                a0 (double): the SV clock bias to set in seconds
        
        
        """
        ...
    def setAGf1(self, double: float) -> None:
        """
            Setter for the SV relative frequency.
        
            Parameters:
                a1 (double): the SV relative frequency to set
        
        
        """
        ...
    def setIODN(self, double: float) -> None:
        """
            Setter for the issue of data navigation.
        
            Parameters:
                iod (double): the issue of data to set
        
        
        """
        ...
    def setTime(self, double: float) -> None:
        """
            Setter for the reference time of the SBAS orbit in GPS seconds of the week.
        
            Parameters:
                time (double): the time to set
        
        
        """
        ...
    def setURA(self, double: float) -> None:
        """
            Setter for the user range accuracy.
        
            Parameters:
                accuracy (double): the value to set
        
        
        """
        ...

_CommonGnssData__O = typing.TypeVar('_CommonGnssData__O', bound='CommonGnssData')  # <O>
class CommonGnssData(GNSSOrbitalElements[_CommonGnssData__O], GNSSClockElements, typing.Generic[_CommonGnssData__O]):
    """
    public abstract class CommonGnssData<O extends CommonGnssData<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`<O> implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
    
        Container for common GNSS data contained in almanac and navigation messages.
    
        Since:
            11.0
    """
    AF0: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` AF0
    
        Name for zero-th order clock correction parameter.
    
        Since:
            13.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    AF1: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` AF1
    
        Name for first order clock correction parameter.
    
        Since:
            13.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    AF2: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` AF2
    
        Name for second order clock correction parameter.
    
        Since:
            13.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getAf0(self) -> float:
        """
            Gets the Zeroth Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf1(self) -> float:
        """
            Gets the First Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
        
            Returns:
                the First Order Clock Correction (s/s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf2(self) -> float:
        """
            Gets the Second Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
        
            Returns:
                the Second Order Clock Correction (s/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1`
        
        
        """
        ...
    def getTGD(self) -> float:
        """
            Get the estimated group delay differential TGD for L1-L2 correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getTGD` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
        
            Returns:
                the estimated group delay differential TGD for L1-L2 correction (s)
        
        
        """
        ...
    def getToc(self) -> float:
        """
            Get the time of clock.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getToc` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
        
            Returns:
                the time of clock (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`
        
        
        """
        ...
    def setAf0(self, double: float) -> None:
        """
            Setter for the SV Clock Bias Correction Coefficient (s).
        
            Parameters:
                af0 (double): the SV Clock Bias Correction Coefficient to set
        
        
        """
        ...
    def setAf1(self, double: float) -> None:
        """
            Setter for the SV Clock Drift Correction Coefficient (s/s).
        
            Parameters:
                af1 (double): the SV Clock Drift Correction Coefficient to set
        
        
        """
        ...
    def setAf2(self, double: float) -> None:
        """
            Setter for the Drift Rate Correction Coefficient (s/s²).
        
            Parameters:
                af2 (double): the Drift Rate Correction Coefficient to set
        
        
        """
        ...
    def setTGD(self, double: float) -> None:
        """
            Set the estimated group delay differential TGD for L1-L2 correction.
        
            Parameters:
                groupDelayDifferential (double): the estimated group delay differential TGD for L1-L2 correction (s)
        
        
        """
        ...
    def setToc(self, double: float) -> None:
        """
            Set the time of clock.
        
            Parameters:
                toc (double): the time of clock (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.CommonGnssData.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.CommonGnssData.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.CommonGnssData.getAf2`
        
        
        """
        ...

_FieldCommonGnssData__T = typing.TypeVar('_FieldCommonGnssData__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldCommonGnssData__O = typing.TypeVar('_FieldCommonGnssData__O', bound=CommonGnssData)  # <O>
class FieldCommonGnssData(FieldGnssOrbitalElements[_FieldCommonGnssData__T, _FieldCommonGnssData__O], FieldGNSSClockElements[_FieldCommonGnssData__T], typing.Generic[_FieldCommonGnssData__T, _FieldCommonGnssData__O]):
    """
    public abstract class FieldCommonGnssData<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>, O extends :class:`~org.orekit.propagation.analytical.gnss.data.CommonGnssData`<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`<T, O> implements :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`<T>
    
        Container for common GNSS data contained in almanac and navigation messages.
    
        Since:
            13.0
    """
    def getAf0(self) -> _FieldCommonGnssData__T:
        """
            Gets the Zeroth Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf0` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf1(self) -> _FieldCommonGnssData__T:
        """
            Gets the First Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf1` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`
        
            Returns:
                the First Order Clock Correction (s/s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf2`
        
        
        """
        ...
    def getAf2(self) -> _FieldCommonGnssData__T:
        """
            Gets the Second Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf2` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`
        
            Returns:
                the Second Order Clock Correction (s/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf1`
        
        
        """
        ...
    def getTGD(self) -> _FieldCommonGnssData__T:
        """
            Get the estimated group delay differential TGD for L1-L2 correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getTGD` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`
        
            Returns:
                the estimated group delay differential TGD for L1-L2 correction (s)
        
        
        """
        ...
    def getToc(self) -> _FieldCommonGnssData__T:
        """
            Get the time of clock.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getToc` in
                interface :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`
        
            Returns:
                the time of clock (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements.getAf2`
        
        
        """
        ...
    def setAf0(self, t: _FieldCommonGnssData__T) -> None:
        """
            Setter for the SV Clock Bias Correction Coefficient (s).
        
            Parameters:
                af0 (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData`): the SV Clock Bias Correction Coefficient to set
        
        
        """
        ...
    def setAf1(self, t: _FieldCommonGnssData__T) -> None:
        """
            Setter for the SV Clock Drift Correction Coefficient (s/s).
        
            Parameters:
                af1 (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData`): the SV Clock Drift Correction Coefficient to set
        
        
        """
        ...
    def setAf2(self, t: _FieldCommonGnssData__T) -> None:
        """
            Setter for the Drift Rate Correction Coefficient (s/s²).
        
            Parameters:
                af2 (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData`): the Drift Rate Correction Coefficient to set
        
        
        """
        ...
    def setTGD(self, t: _FieldCommonGnssData__T) -> None:
        """
            Set the estimated group delay differential TGD for L1-L2 correction.
        
            Parameters:
                groupDelayDifferential (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData`): the estimated group delay differential TGD for L1-L2 correction (s)
        
        
        """
        ...
    def setToc(self, t: _FieldCommonGnssData__T) -> None:
        """
            Set the time of clock.
        
            Parameters:
                toc (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData`): the time of clock (s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData.getAf2`
        
        
        """
        ...

_AbstractAlmanac__O = typing.TypeVar('_AbstractAlmanac__O', bound='AbstractAlmanac')  # <O>
class AbstractAlmanac(CommonGnssData[_AbstractAlmanac__O], typing.Generic[_AbstractAlmanac__O]):
    """
    public abstract class AbstractAlmanac<O extends AbstractAlmanac<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.CommonGnssData`<O>
    
        Base class for GNSS almanacs.
    
        Since:
            11.0
    """
    def __init__(self, double: float, double2: float, int: int, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.analytical.gnss.GNSSPropagator:
        """
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default to be aligned with the EME2000 frame.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Predefined.EME2000` in the default data context.
        
        
            The ECEF frame is set by default to the :meth:`~org.orekit.frames.Predefined.ITRF_CIO_CONV_2010_SIMPLE_EOP` in the
            default data context.
        
            This constructor uses the :meth:`~org.orekit.data.DataContext.getDefault`
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac.getPropagator`
        
        """
        ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames) -> org.orekit.propagation.analytical.gnss.GNSSPropagator:
        """
            Get the propagator corresponding to the navigation message.
        
            The attitude provider is set by default to be aligned with the EME2000 frame.
        
        
            The mass is set by default to the :meth:`~org.orekit.propagation.Propagator.DEFAULT_MASS`.
        
        
            The ECI frame is set by default to the :meth:`~org.orekit.frames.Predefined.EME2000` in the default data context.
        
        
            The ECEF frame is set by default to the :meth:`~org.orekit.frames.Predefined.ITRF_CIO_CONV_2010_SIMPLE_EOP` in the
            default data context.
        
            Parameters:
                frames (:class:`~org.orekit.frames.Frames`): set of frames to use
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                13.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac.getPropagator`
        
            Get the propagator corresponding to the navigation message.
        
            Parameters:
                frames (:class:`~org.orekit.frames.Frames`): set of frames to use
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
                inertial (:class:`~org.orekit.frames.Frame`): inertial frame, use to provide the propagated orbit
                bodyFixed (:class:`~org.orekit.frames.Frame`): body fixed frame, corresponding to the navigation message
                mass (double): spacecraft mass in kg
        
            Returns:
                the propagator corresponding to the navigation message
        
            Since:
                13.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac.getPropagator`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac.getPropagator`
        
        
        """
        ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame2: org.orekit.frames.Frame, frame3: org.orekit.frames.Frame, double: float) -> org.orekit.propagation.analytical.gnss.GNSSPropagator: ...

_FieldAbstractAlmanac__T = typing.TypeVar('_FieldAbstractAlmanac__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldAbstractAlmanac__O = typing.TypeVar('_FieldAbstractAlmanac__O', bound=AbstractAlmanac)  # <O>
class FieldAbstractAlmanac(FieldCommonGnssData[_FieldAbstractAlmanac__T, _FieldAbstractAlmanac__O], typing.Generic[_FieldAbstractAlmanac__T, _FieldAbstractAlmanac__O]):
    """
    public abstract class FieldAbstractAlmanac<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>, O extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac`<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldCommonGnssData`<T, O>
    
        Base class for GNSS almanacs.
    
        Since:
            13.0
    """
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.analytical.gnss.FieldGnssPropagator[_FieldAbstractAlmanac__T]: ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames) -> org.orekit.propagation.analytical.gnss.FieldGnssPropagator[_FieldAbstractAlmanac__T]: ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame2: org.orekit.frames.Frame, frame3: org.orekit.frames.Frame, t: _FieldAbstractAlmanac__T) -> org.orekit.propagation.analytical.gnss.FieldGnssPropagator[_FieldAbstractAlmanac__T]: ...

_AbstractNavigationMessage__O = typing.TypeVar('_AbstractNavigationMessage__O', bound='AbstractNavigationMessage')  # <O>
class AbstractNavigationMessage(AbstractAlmanac[_AbstractNavigationMessage__O], typing.Generic[_AbstractNavigationMessage__O]):
    """
    public abstract class AbstractNavigationMessage<O extends AbstractNavigationMessage<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac`<O>
    
        Base class for GNSS navigation messages.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.NavICLegacyNavigationMessage`
    """
    def getDeltaN0(self) -> float:
        """
            Getter for the delta of satellite mean motion.
        
            This value is non-zero only in navigation messages
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements.getDeltaN0` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
        
            Returns:
                delta of satellite mean motion
        
        
        """
        ...
    def getEpochToc(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for the time of clock epoch.
        
            Returns:
                the time of clock epoch
        
        
        """
        ...
    def getSqrtA(self) -> float:
        """
            Getter for Square Root of Semi-Major Axis (√m).
        
            Returns:
                Square Root of Semi-Major Axis (√m)
        
        
        """
        ...
    def getTransmissionTime(self) -> float:
        """
            Getter for transmission time.
        
            Returns:
                transmission time
        
            Since:
                12.0
        
        
        """
        ...
    def setDeltaN0(self, double: float) -> None:
        """
            Setter for the delta of satellite mean motion.
        
            Parameters:
                deltaN0 (double): the value to set
        
        
        """
        ...
    def setEpochToc(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the time of clock epoch.
        
            Parameters:
                epochToc (:class:`~org.orekit.time.AbsoluteDate`): the epoch to set
        
        
        """
        ...
    def setSqrtA(self, double: float) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (√m).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (double): the Square Root of Semi-Major Axis (√m)
        
        
        """
        ...
    def setTransmissionTime(self, double: float) -> None:
        """
            Setter for transmission time.
        
            Parameters:
                transmissionTime (double): transmission time
        
            Since:
                12.0
        
        
        """
        ...

class BeidouAlmanac(AbstractAlmanac['BeidouAlmanac']):
    """
    public class BeidouAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac`<:class:`~org.orekit.propagation.analytical.gnss.data.BeidouAlmanac`>
    
        Class for BeiDou almanac.
    
        Since:
            10.0
    
        Also see:
            "BeiDou Navigation Satellite System, Signal In Space, Interface Control Document, Version 2.1, Table 5-12"
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldBeidouAlmanac: 'FieldBeidouAlmanac'[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def getHealth(self) -> int:
        """
            Gets the Health status.
        
            Returns:
                the Health status
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Sets the health status.
        
            Parameters:
                health (int): the health status to set
        
        
        """
        ...
    @typing.overload
    def setI0(self, double: float, double2: float) -> None:
        """
            Sets the Inclination Angle at Reference Time (rad).
        
            Parameters:
                inc (double): the orbit reference inclination
                dinc (double): the correction of orbit reference inclination at reference time
        
        
        """
        ...
    @typing.overload
    def setI0(self, double: float) -> None: ...
    def setSqrtA(self, double: float) -> None:
        """
            Sets the Square Root of Semi-Major Axis (√m).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (double): the Square Root of Semi-Major Axis (√m)
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

_FieldAbstractNavigationMessage__T = typing.TypeVar('_FieldAbstractNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldAbstractNavigationMessage__O = typing.TypeVar('_FieldAbstractNavigationMessage__O', bound=AbstractNavigationMessage)  # <O>
class FieldAbstractNavigationMessage(FieldAbstractAlmanac[_FieldAbstractNavigationMessage__T, _FieldAbstractNavigationMessage__O], typing.Generic[_FieldAbstractNavigationMessage__T, _FieldAbstractNavigationMessage__O]):
    """
    public abstract class FieldAbstractNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>, O extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage`<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractAlmanac`<T, O>
    
        Base class for GNSS navigation messages.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.propagation.analytical.gnss.data.FieldGPSLegacyNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.FieldGalileoNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouLegacyNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.FieldQZSSLegacyNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.FieldNavicLegacyNavigationMessage`
    """
    def getDeltaN0(self) -> _FieldAbstractNavigationMessage__T:
        """
            Getter for the delta of satellite mean motion.
        
            This value is non-zero only in navigation messages
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.getDeltaN0` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                delta of satellite mean motion
        
        
        """
        ...
    def getEpochToc(self) -> org.orekit.time.FieldAbsoluteDate[_FieldAbstractNavigationMessage__T]: ...
    def getSqrtA(self) -> _FieldAbstractNavigationMessage__T:
        """
            Getter for Square Root of Semi-Major Axis (√m).
        
            Returns:
                Square Root of Semi-Major Axis (√m)
        
        
        """
        ...
    def getTransmissionTime(self) -> _FieldAbstractNavigationMessage__T:
        """
            Getter for transmission time.
        
            Returns:
                transmission time
        
        
        """
        ...
    def setDeltaN0(self, t: _FieldAbstractNavigationMessage__T) -> None:
        """
            Setter for the delta of satellite mean motion.
        
            Parameters:
                deltaN0 (:class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`): the value to set
        
        
        """
        ...
    def setEpochToc(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractNavigationMessage__T]) -> None: ...
    def setSqrtA(self, t: _FieldAbstractNavigationMessage__T) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (√m).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (:class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`): the Square Root of Semi-Major Axis (√m)
        
        
        """
        ...
    def setTransmissionTime(self, t: _FieldAbstractNavigationMessage__T) -> None:
        """
            Setter for transmission time.
        
            Parameters:
                transmissionTime (:class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`): transmission time
        
        
        """
        ...

_FieldBeidouAlmanac__T = typing.TypeVar('_FieldBeidouAlmanac__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBeidouAlmanac(FieldAbstractAlmanac[_FieldBeidouAlmanac__T, BeidouAlmanac], typing.Generic[_FieldBeidouAlmanac__T]):
    """
    public class FieldBeidouAlmanac<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractAlmanac`<T, :class:`~org.orekit.propagation.analytical.gnss.data.BeidouAlmanac`>
    
        Class for BeiDou almanac.
    
        Since:
            13.0
    
        Also see:
            "BeiDou Navigation Satellite System, Signal In Space, Interface Control Document, Version 2.1, Table 5-12"
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldBeidouAlmanac__T], typing.Callable[[___init___0__V], _FieldBeidouAlmanac__T]], fieldBeidouAlmanac: 'FieldBeidouAlmanac'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldBeidouAlmanac__T], beidouAlmanac: BeidouAlmanac): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldBeidouAlmanac__T, _changeField__U], typing.Callable[[_FieldBeidouAlmanac__T], _changeField__U]]) -> _changeField__G: ...
    def getHealth(self) -> int:
        """
            Gets the Health status.
        
            Returns:
                the Health status
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Sets the health status.
        
            Parameters:
                health (int): the health status to set
        
        
        """
        ...
    @typing.overload
    def setI0(self, t: _FieldBeidouAlmanac__T, t2: _FieldBeidouAlmanac__T) -> None:
        """
            Sets the Inclination Angle at Reference Time (rad).
        
            Parameters:
                inc (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouAlmanac`): the orbit reference inclination
                dinc (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouAlmanac`): the correction of orbit reference inclination at reference time
        
        
        """
        ...
    @typing.overload
    def setI0(self, t: _FieldBeidouAlmanac__T) -> None: ...
    def setSqrtA(self, t: _FieldBeidouAlmanac__T) -> None:
        """
            Sets the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouAlmanac`): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...
    def toNonField(self) -> BeidouAlmanac:
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldGPSAlmanac__T = typing.TypeVar('_FieldGPSAlmanac__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGPSAlmanac(FieldAbstractAlmanac[_FieldGPSAlmanac__T, 'GPSAlmanac'], typing.Generic[_FieldGPSAlmanac__T]):
    """
    public class FieldGPSAlmanac<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractAlmanac`<T, :class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac`>
    
        This class holds a GPS almanac as read from SEM or YUMA files.
    
        Depending on the source (SEM or YUMA), some fields may be filled in or not. An almanac read from a YUMA file doesn't
        hold SVN number, average URA and satellite configuration.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldGPSAlmanac__T], typing.Callable[[___init___0__V], _FieldGPSAlmanac__T]], fieldGPSAlmanac: 'FieldGPSAlmanac'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldGPSAlmanac__T], gPSAlmanac: 'GPSAlmanac'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldGPSAlmanac__T, _changeField__U], typing.Callable[[_FieldGPSAlmanac__T], _changeField__U]]) -> _changeField__G: ...
    def getHealth(self) -> int:
        """
            Gets the Health status.
        
            Returns:
                the Health status
        
        
        """
        ...
    def getSVN(self) -> int:
        """
            Gets the satellite "SVN" reference number.
        
            Returns:
                the satellite "SVN" reference number
        
        
        """
        ...
    def getSatConfiguration(self) -> int:
        """
            Gets the satellite configuration.
        
            Returns:
                the satellite configuration
        
        
        """
        ...
    def getSource(self) -> str:
        """
            Gets the source of this GPS almanac.
        
            Sources can be SEM or YUMA, when the almanac is read from a file.
        
            Returns:
                the source of this GPS almanac
        
        
        """
        ...
    def getURA(self) -> int:
        """
            Gets the average URA number.
        
            Returns:
                the average URA number
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Sets the health status.
        
            Parameters:
                health (int): the health status to set
        
        
        """
        ...
    def setSVN(self, int: int) -> None:
        """
            Sets the "SVN" reference number.
        
            Parameters:
                svnNumber (int): the number to set
        
        
        """
        ...
    def setSatConfiguration(self, int: int) -> None:
        """
            Sets the satellite configuration.
        
            Parameters:
                satConfiguration (int): the satellite configuration to set
        
        
        """
        ...
    def setSource(self, string: str) -> None:
        """
            Sets the source of this GPS almanac.
        
            Parameters:
                source (:class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the source of this GPS almanac
        
        
        """
        ...
    def setSqrtA(self, t: _FieldGPSAlmanac__T) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGPSAlmanac`): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...
    def setURA(self, int: int) -> None:
        """
            Sets the average URA number.
        
            Parameters:
                uraNumber (int): the URA number to set
        
        
        """
        ...
    def toNonField(self) -> 'GPSAlmanac':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldGalileoAlmanac__T = typing.TypeVar('_FieldGalileoAlmanac__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGalileoAlmanac(FieldAbstractAlmanac[_FieldGalileoAlmanac__T, 'GalileoAlmanac'], typing.Generic[_FieldGalileoAlmanac__T]):
    """
    public class FieldGalileoAlmanac<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractAlmanac`<T, :class:`~org.orekit.propagation.analytical.gnss.data.GalileoAlmanac`>
    
        Class for Galileo almanac.
    
        Since:
            13.0
    
        Also see:
            "European GNSS (Galileo) Open Service, Signal In Space, Interface Control Document, Table 75"
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldGalileoAlmanac__T], typing.Callable[[___init___0__V], _FieldGalileoAlmanac__T]], fieldGalileoAlmanac: 'FieldGalileoAlmanac'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldGalileoAlmanac__T], galileoAlmanac: 'GalileoAlmanac'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldGalileoAlmanac__T, _changeField__U], typing.Callable[[_FieldGalileoAlmanac__T], _changeField__U]]) -> _changeField__G: ...
    def getHealthE1(self) -> int:
        """
            Gets the E1-B/C signal health status.
        
            Returns:
                the E1-B/C signal health status
        
        
        """
        ...
    def getHealthE5a(self) -> int:
        """
            Gets the E5a signal health status.
        
            Returns:
                the E5a signal health status
        
        
        """
        ...
    def getHealthE5b(self) -> int:
        """
            Gets the E5b signal health status.
        
            Returns:
                the E5b signal health status
        
        
        """
        ...
    def getIOD(self) -> int:
        """
            Gets the Issue of Data (IOD).
        
            Returns:
                the Issue Of Data
        
        
        """
        ...
    def setDeltaInc(self, t: _FieldGalileoAlmanac__T) -> None:
        """
            Sets the the correction of orbit reference inclination at reference time.
        
            In addition, this method set the value of the reference inclination.
        
            Parameters:
                dinc (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGalileoAlmanac`): correction of orbit reference inclination at reference time in radians
        
        
        """
        ...
    def setDeltaSqrtA(self, t: _FieldGalileoAlmanac__T) -> None:
        """
            Sets the difference between the square root of the semi-major axis and the square root of the nominal semi-major axis.
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                dsqa (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGalileoAlmanac`): the value to set
        
        
        """
        ...
    def setHealthE1(self, int: int) -> None:
        """
            Sets the E1-B/C signal health status.
        
            Parameters:
                healthE1 (int): health status to set
        
        
        """
        ...
    def setHealthE5a(self, int: int) -> None:
        """
            Sets the E5a signal health status.
        
            Parameters:
                healthE5a (int): health status to set
        
        
        """
        ...
    def setHealthE5b(self, int: int) -> None:
        """
            Sets the E5b signal health status.
        
            Parameters:
                healthE5b (int): health status to set
        
        
        """
        ...
    def setIOD(self, int: int) -> None:
        """
            Sets the Issue of Data (IOD).
        
            Parameters:
                iodValue (int): the value to set
        
        
        """
        ...
    def toNonField(self) -> 'GalileoAlmanac':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldNavICAlmanac__T = typing.TypeVar('_FieldNavICAlmanac__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNavICAlmanac(FieldAbstractAlmanac[_FieldNavICAlmanac__T, 'NavICAlmanac'], typing.Generic[_FieldNavICAlmanac__T]):
    """
    public class FieldNavICAlmanac<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractAlmanac`<T, :class:`~org.orekit.propagation.analytical.gnss.data.NavICAlmanac`>
    
        Class for NavIC almanac.
    
        Since:
            13.0
    
        Also see:
            "Indian Regional Navigation Satellite System, Signal In Space ICD for standard positioning service, version 1.1 - Table
            28"
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldNavICAlmanac__T], typing.Callable[[___init___0__V], _FieldNavICAlmanac__T]], fieldNavICAlmanac: 'FieldNavICAlmanac'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNavICAlmanac__T], navICAlmanac: 'NavICAlmanac'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldNavICAlmanac__T, _changeField__U], typing.Callable[[_FieldNavICAlmanac__T], _changeField__U]]) -> _changeField__G: ...
    def setSqrtA(self, t: _FieldNavICAlmanac__T) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (:class:`~org.orekit.propagation.analytical.gnss.data.FieldNavICAlmanac`): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...
    def toNonField(self) -> 'NavICAlmanac':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldQZSSAlmanac__T = typing.TypeVar('_FieldQZSSAlmanac__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQZSSAlmanac(FieldAbstractAlmanac[_FieldQZSSAlmanac__T, 'QZSSAlmanac'], typing.Generic[_FieldQZSSAlmanac__T]):
    """
    public class FieldQZSSAlmanac<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractAlmanac`<T, :class:`~org.orekit.propagation.analytical.gnss.data.QZSSAlmanac`>
    
        This class holds a QZSS almanac as read from YUMA files.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldQZSSAlmanac__T], typing.Callable[[___init___0__V], _FieldQZSSAlmanac__T]], fieldQZSSAlmanac: 'FieldQZSSAlmanac'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldQZSSAlmanac__T], qZSSAlmanac: 'QZSSAlmanac'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldQZSSAlmanac__T, _changeField__U], typing.Callable[[_FieldQZSSAlmanac__T], _changeField__U]]) -> _changeField__G: ...
    def getHealth(self) -> int:
        """
            Gets the Health status.
        
            Returns:
                the Health status
        
        
        """
        ...
    def getSource(self) -> str:
        """
            Gets the source of this QZSS almanac.
        
            Returns:
                the source of this QZSS almanac
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Sets the health status.
        
            Parameters:
                health (int): the health status to set
        
        
        """
        ...
    def setSource(self, string: str) -> None:
        """
            Sets the source of this GPS almanac.
        
            Parameters:
                source (:class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the source of this GPS almanac
        
        
        """
        ...
    def setSqrtA(self, t: _FieldQZSSAlmanac__T) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (:class:`~org.orekit.propagation.analytical.gnss.data.FieldQZSSAlmanac`): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...
    def toNonField(self) -> 'QZSSAlmanac':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

class GPSAlmanac(AbstractAlmanac['GPSAlmanac']):
    """
    public class GPSAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac`<:class:`~org.orekit.propagation.analytical.gnss.data.GPSAlmanac`>
    
        This class holds a GPS almanac as read from SEM or YUMA files.
    
        Depending on the source (SEM or YUMA), some fields may be filled in or not. An almanac read from a YUMA file doesn't
        hold SVN number, average URA and satellite configuration.
    
        Since:
            8.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldGPSAlmanac: FieldGPSAlmanac[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def getHealth(self) -> int:
        """
            Gets the Health status.
        
            Returns:
                the Health status
        
        
        """
        ...
    def getSVN(self) -> int:
        """
            Gets the satellite "SVN" reference number.
        
            Returns:
                the satellite "SVN" reference number
        
        
        """
        ...
    def getSatConfiguration(self) -> int:
        """
            Gets the satellite configuration.
        
            Returns:
                the satellite configuration
        
        
        """
        ...
    def getSource(self) -> str:
        """
            Gets the source of this GPS almanac.
        
            Sources can be SEM or YUMA, when the almanac is read from a file.
        
            Returns:
                the source of this GPS almanac
        
        
        """
        ...
    def getURA(self) -> int:
        """
            Gets the average URA number.
        
            Returns:
                the average URA number
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Sets the health status.
        
            Parameters:
                health (int): the health status to set
        
        
        """
        ...
    def setSVN(self, int: int) -> None:
        """
            Sets the "SVN" reference number.
        
            Parameters:
                svnNumber (int): the number to set
        
        
        """
        ...
    def setSatConfiguration(self, int: int) -> None:
        """
            Sets the satellite configuration.
        
            Parameters:
                satConfiguration (int): the satellite configuration to set
        
        
        """
        ...
    def setSource(self, string: str) -> None:
        """
            Sets the source of this GPS almanac.
        
            Parameters:
                source (:class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the source of this GPS almanac
        
        
        """
        ...
    def setSqrtA(self, double: float) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (double): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...
    def setURA(self, int: int) -> None:
        """
            Sets the average URA number.
        
            Parameters:
                uraNumber (int): the URA number to set
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class GalileoAlmanac(AbstractAlmanac['GalileoAlmanac']):
    """
    public class GalileoAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac`<:class:`~org.orekit.propagation.analytical.gnss.data.GalileoAlmanac`>
    
        Class for Galileo almanac.
    
        Since:
            10.0
    
        Also see:
            "European GNSS (Galileo) Open Service, Signal In Space, Interface Control Document, Table 75"
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldGalileoAlmanac: FieldGalileoAlmanac[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def getHealthE1(self) -> int:
        """
            Gets the E1-B/C signal health status.
        
            Returns:
                the E1-B/C signal health status
        
        
        """
        ...
    def getHealthE5a(self) -> int:
        """
            Gets the E5a signal health status.
        
            Returns:
                the E5a signal health status
        
        
        """
        ...
    def getHealthE5b(self) -> int:
        """
            Gets the E5b signal health status.
        
            Returns:
                the E5b signal health status
        
        
        """
        ...
    def getIOD(self) -> int:
        """
            Gets the Issue of Data (IOD).
        
            Returns:
                the Issue Of Data
        
        
        """
        ...
    def setDeltaInc(self, double: float) -> None:
        """
            Sets the the correction of orbit reference inclination at reference time.
        
            In addition, this method set the value of the reference inclination.
        
            Parameters:
                dinc (double): correction of orbit reference inclination at reference time in radians
        
        
        """
        ...
    def setDeltaSqrtA(self, double: float) -> None:
        """
            Sets the difference between the square root of the semi-major axis and the square root of the nominal semi-major axis.
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                dsqa (double): the value to set
        
        
        """
        ...
    def setHealthE1(self, int: int) -> None:
        """
            Sets the E1-B/C signal health status.
        
            Parameters:
                healthE1 (int): health status to set
        
        
        """
        ...
    def setHealthE5a(self, int: int) -> None:
        """
            Sets the E5a signal health status.
        
            Parameters:
                healthE5a (int): health status to set
        
        
        """
        ...
    def setHealthE5b(self, int: int) -> None:
        """
            Sets the E5b signal health status.
        
            Parameters:
                healthE5b (int): health status to set
        
        
        """
        ...
    def setIOD(self, int: int) -> None:
        """
            Sets the Issue of Data (IOD).
        
            Parameters:
                iodValue (int): the value to set
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class NavICAlmanac(AbstractAlmanac['NavICAlmanac']):
    """
    public class NavICAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac`<:class:`~org.orekit.propagation.analytical.gnss.data.NavICAlmanac`>
    
        Class for NavIC almanac.
    
        Since:
            10.1
    
        Also see:
            "Indian Regional Navigation Satellite System, Signal In Space ICD for standard positioning service, version 1.1 - Table
            28"
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldNavICAlmanac: FieldNavICAlmanac[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def setSqrtA(self, double: float) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (double): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class QZSSAlmanac(AbstractAlmanac['QZSSAlmanac']):
    """
    public class QZSSAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac`<:class:`~org.orekit.propagation.analytical.gnss.data.QZSSAlmanac`>
    
        This class holds a QZSS almanac as read from YUMA files.
    
        Since:
            10.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldQZSSAlmanac: FieldQZSSAlmanac[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def getHealth(self) -> int:
        """
            Gets the Health status.
        
            Returns:
                the Health status
        
        
        """
        ...
    def getSource(self) -> str:
        """
            Gets the source of this QZSS almanac.
        
            Returns:
                the source of this QZSS almanac
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Sets the health status.
        
            Parameters:
                health (int): the health status to set
        
        
        """
        ...
    def setSource(self, string: str) -> None:
        """
            Sets the source of this GPS almanac.
        
            Parameters:
                source (:class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the source of this GPS almanac
        
        
        """
        ...
    def setSqrtA(self, double: float) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (double): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class BeidouCivilianNavigationMessage(AbstractNavigationMessage['BeidouCivilianNavigationMessage']):
    """
    public class BeidouCivilianNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.BeidouCivilianNavigationMessage`>
    
        Container for data contained in a Beidou civilian navigation message.
    
        Since:
            12.0
    """
    CNV1: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CNV1
    
        Identifier for Beidou-3 B1C message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CNV2: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CNV2
    
        Identifier for Beidou-3 B2A message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CNV3: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CNV3
    
        Identifier for Beidou-3 B2B message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ___init___1__T = typing.TypeVar('___init___1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, radioWave: typing.Union[org.orekit.gnss.RadioWave, typing.Callable], timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, fieldBeidouCivilianNavigationMessage: 'FieldBeidouCivilianNavigationMessage'[___init___1__T]): ...
    def getADot(self) -> float:
        """
            Getter for the change rate in semi-major axis.
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements.getADot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
        
            Returns:
                the change rate in semi-major axis
        
        
        """
        ...
    def getDeltaN0Dot(self) -> float:
        """
            Getter for change rate in Δn₀.
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements.getDeltaN0Dot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
        
            Returns:
                change rate in Δn₀
        
        
        """
        ...
    def getHealth(self) -> int:
        """
            Getter for health.
        
            Returns:
                health
        
        
        """
        ...
    def getIODC(self) -> int:
        """
            Getter for the Issue Of Data Clock (IODC).
        
            Returns:
                the Issue Of Data Clock (IODC)
        
        
        """
        ...
    def getIODE(self) -> int:
        """
            Getter for the Issue Of Data Ephemeris (IODE).
        
            Returns:
                the Issue Of Data Ephemeris (IODE)
        
        
        """
        ...
    def getIntegrityFlags(self) -> int:
        """
            Getter for B1C integrity flags.
        
            Returns:
                B1C integrity flags
        
        
        """
        ...
    def getIscB1CD(self) -> float:
        """
            Getter for inter Signal Delay for B1 CD.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscB1CP(self) -> float:
        """
            Getter for inter Signal Delay for B1 CP.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscB2AD(self) -> float:
        """
            Getter for inter Signal Delay for B2 AD.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getRadioWave(self) -> org.orekit.gnss.RadioWave:
        """
            Getter for radio wave.
        
            Returns:
                radio wave on which navigation signal is sent
        
        
        """
        ...
    def getSatelliteType(self) -> BeidouSatelliteType:
        """
            Getter for satellite type.
        
            Returns:
                satellite type
        
        
        """
        ...
    def getSisaiOc1(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (clock drift accuracy).
        
            Returns:
                Signal In Space Accuracy Index (clock drift accuracy)
        
        
        """
        ...
    def getSisaiOc2(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (clock drift rate accuracy).
        
            Returns:
                Signal In Space Accuracy Index (clock drift rate accuracy)
        
        
        """
        ...
    def getSisaiOcb(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (radial and clock).
        
            Returns:
                Signal In Space Accuracy Index (radial and clock)
        
        
        """
        ...
    def getSisaiOe(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (along track and across track).
        
            Returns:
                Signal In Space Accuracy Index (along track and across track)
        
        
        """
        ...
    def getSismai(self) -> int:
        """
            Getter for Signal In Space Monitoring Accuracy Index.
        
            Returns:
                Signal In Space Monitoring Accuracy Index
        
        
        """
        ...
    def getTgdB1Cp(self) -> float:
        """
            Getter for B1/B3 Group Delay Differential (s).
        
            Returns:
                B1/B3 Group Delay Differential (s)
        
        
        """
        ...
    def getTgdB2ap(self) -> float:
        """
            Getter for B2 AP Group Delay Differential (s).
        
            Returns:
                B2 AP Group Delay Differential (s)
        
        
        """
        ...
    def getTgdB2bI(self) -> float:
        """
            Getter for B2B_i / B3I Group Delay Differential (s).
        
            Returns:
                B2B_i / B3I Group Delay Differential (s)
        
        
        """
        ...
    def setADot(self, double: float) -> None:
        """
            Setter for the change rate in semi-major axis.
        
            Parameters:
                value (double): the change rate in semi-major axis
        
        
        """
        ...
    def setDeltaN0Dot(self, double: float) -> None:
        """
            Setter for change rate in Δn₀.
        
            Parameters:
                deltaN0Dot (double): change rate in Δn₀
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Setter for health.
        
            Parameters:
                health (int): health
        
        
        """
        ...
    def setIODC(self, int: int) -> None:
        """
            Setter for the Issue of Data Clock.
        
            Parameters:
                value (int): the IODC to set
        
        
        """
        ...
    def setIODE(self, int: int) -> None:
        """
            Setter for the Issue of Data Ephemeris.
        
            Parameters:
                value (int): the IODE to set
        
        
        """
        ...
    def setIntegrityFlags(self, int: int) -> None:
        """
            Setter for B1C integrity flags.
        
            Parameters:
                integrityFlags (int): integrity flags
        
        
        """
        ...
    def setIscB1CD(self, double: float) -> None:
        """
            Setter for inter Signal Delay for B1 CD.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscB1CP(self, double: float) -> None:
        """
            Setter for inter Signal Delay for B1 CP.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscB2AD(self, double: float) -> None:
        """
            Setter for inter Signal Delay for B2 AD.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setSatelliteType(self, beidouSatelliteType: BeidouSatelliteType) -> None:
        """
            Setter for satellite type.
        
            Parameters:
                satelliteType (:class:`~org.orekit.propagation.analytical.gnss.data.BeidouSatelliteType`): satellite type
        
        
        """
        ...
    def setSisaiOc1(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (clock drift accuracy).
        
            Parameters:
                sisaiOc1 (int): Signal In Space Accuracy Index (clock drift accuracy)
        
        
        """
        ...
    def setSisaiOc2(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (clock drift rate accuracy).
        
            Parameters:
                sisaiOc2 (int): Signal In Space Accuracy Index (clock drift rate accuracy)
        
        
        """
        ...
    def setSisaiOcb(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (radial and clock).
        
            Parameters:
                sisaiOcb (int): Signal In Space Accuracy Index (radial and clock)
        
        
        """
        ...
    def setSisaiOe(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (along track and across track).
        
            Parameters:
                sisaiOe (int): Signal In Space Accuracy Index (along track and across track)
        
        
        """
        ...
    def setSismai(self, int: int) -> None:
        """
            Setter for Signal In Space Monitoring Accuracy Index.
        
            Parameters:
                sismai (int): Signal In Space Monitoring Accuracy Index
        
        
        """
        ...
    def setTgdB1Cp(self, double: float) -> None:
        """
            Setter for B1/B3 Group Delay Differential (s).
        
            Parameters:
                tgdB1Cp (double): B1/B3 Group Delay Differential (s)
        
        
        """
        ...
    def setTgdB2ap(self, double: float) -> None:
        """
            Setter for B2 AP Group Delay Differential (s).
        
            Parameters:
                tgdB2ap (double): B2 AP Group Delay Differential (s)
        
        
        """
        ...
    def setTgdB2bI(self, double: float) -> None:
        """
            Setter for B2B_i / B3I Group Delay Differential (s).
        
            Parameters:
                tgdB2bI (double): B2B_i / B3I Group Delay Differential (s)
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class BeidouLegacyNavigationMessage(AbstractNavigationMessage['BeidouLegacyNavigationMessage']):
    """
    public class BeidouLegacyNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage`>
    
        Container for data contained in a BeiDou navigation message.
    
        Since:
            11.0
    """
    D1: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` D1
    
        Identifier for message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    D2: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` D2
    
        Identifier for message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldBeidouLegacyNavigationMessage: 'FieldBeidouLegacyNavigationMessage'[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def getAODC(self) -> int:
        """
            Getter for the Age Of Data Clock (AODC).
        
            Returns:
                the Age Of Data Clock (AODC)
        
        
        """
        ...
    def getAODE(self) -> int:
        """
            Getter for the Age Of Data Ephemeris (AODE).
        
            Returns:
                the Age Of Data Ephemeris (AODE)
        
        
        """
        ...
    def getSvAccuracy(self) -> float:
        """
            Getter for the user SV accuray (meters).
        
            Returns:
                the user SV accuracy
        
        
        """
        ...
    def getTGD1(self) -> float:
        """
            Getter for the estimated group delay differential TGD1 for B1I signal.
        
            Returns:
                the estimated group delay differential TGD1 for B1I signal (s)
        
        
        """
        ...
    def getTGD2(self) -> float:
        """
            Getter for the estimated group delay differential TGD for B2I signal.
        
            Returns:
                the estimated group delay differential TGD2 for B2I signal (s)
        
        
        """
        ...
    def setAODC(self, double: float) -> None:
        """
            Setter for the age of data clock.
        
            Parameters:
                aod (double): the age of data to set
        
        
        """
        ...
    def setAODE(self, double: float) -> None:
        """
            Setter for the age of data ephemeris.
        
            Parameters:
                aod (double): the age of data to set
        
        
        """
        ...
    def setSvAccuracy(self, double: float) -> None:
        """
            Setter for the user SV accuracy.
        
            Parameters:
                svAccuracy (double): the value to set
        
        
        """
        ...
    def setTGD1(self, double: float) -> None:
        """
            Setter for the B1/B3 Group Delay Differential (s).
        
            Parameters:
                tgd (double): the group delay differential to set
        
        
        """
        ...
    def setTGD2(self, double: float) -> None:
        """
            Setter for the B2/B3 Group Delay Differential (s).
        
            Parameters:
                tgd (double): the group delay differential to set
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

_CivilianNavigationMessage__O = typing.TypeVar('_CivilianNavigationMessage__O', bound='CivilianNavigationMessage')  # <O>
class CivilianNavigationMessage(AbstractNavigationMessage[_CivilianNavigationMessage__O], GNSSClockElements, typing.Generic[_CivilianNavigationMessage__O]):
    """
    public abstract class CivilianNavigationMessage<O extends CivilianNavigationMessage<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage`<O> implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
    
        Container for data contained in a GPS/QZNSS civilian navigation message.
    
        Since:
            12.0
    """
    CNAV: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CNAV
    
        Identifier for message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CNV2: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CNV2
    
        Identifier for message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    L1NV: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` L1NV
    
        Identifier for message type.
    
        Since:
            13.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getADot(self) -> float:
        """
            Getter for the change rate in semi-major axis.
        
            This value is non-zero only in civilian navigation messages
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements.getADot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
        
            Returns:
                the change rate in semi-major axis
        
        
        """
        ...
    def getDeltaN0Dot(self) -> float:
        """
            Getter for change rate in Δn₀.
        
            This value is non-zero only in civilian navigation messages
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements.getDeltaN0Dot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
        
            Returns:
                change rate in Δn₀
        
        
        """
        ...
    def getIscL1CA(self) -> float:
        """
            Getter for inter Signal Delay for L1 C/A.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1CD(self) -> float:
        """
            Getter for inter Signal Delay for L1 CD.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1CP(self) -> float:
        """
            Getter for inter Signal Delay for L1 CP.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL2C(self) -> float:
        """
            Getter for inter Signal Delay for L2 C.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL5I5(self) -> float:
        """
            Getter for inter Signal Delay for L5I.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL5Q5(self) -> float:
        """
            Getter for inter Signal Delay for L5Q.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getSvAccuracy(self) -> float:
        """
            Getter for the user SV accuray (meters).
        
            Returns:
                the user SV accuracy
        
        
        """
        ...
    def getSvHealth(self) -> int:
        """
            Getter for the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def getUraiEd(self) -> int:
        """
            Getter for Elevation-Dependent User Range Accuracy.
        
            Returns:
                Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def getUraiNed0(self) -> int:
        """
            Getter for term 0 of Non-Elevation-Dependent User Range Accuracy.
        
            Returns:
                term 0 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def getUraiNed1(self) -> int:
        """
            Getter for term 1 of Non-Elevation-Dependent User Range Accuracy.
        
            Returns:
                term 1 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def getUraiNed2(self) -> int:
        """
            Getter for term 2 of Non-Elevation-Dependent User Range Accuracy.
        
            Returns:
                term 2 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def isCnv2(self) -> bool:
        """
            Check it message is a CNV2 message.
        
            Returns:
                true if message is a CNV2 message
        
        
        """
        ...
    def setADot(self, double: float) -> None:
        """
            Setter for the change rate in semi-major axis.
        
            Parameters:
                value (double): the change rate in semi-major axis
        
        
        """
        ...
    def setDeltaN0Dot(self, double: float) -> None:
        """
            Setter for change rate in Δn₀.
        
            Parameters:
                deltaN0Dot (double): change rate in Δn₀
        
        
        """
        ...
    def setIscL1CA(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L1 C/A.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscL1CD(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L1 CD.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscL1CP(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L1 CP.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscL2C(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L2 C.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscL5I5(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L5I.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscL5Q5(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L5Q.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setSvAccuracy(self, double: float) -> None:
        """
            Setter for the user SV accuracy.
        
            Parameters:
                svAccuracy (double): the value to set
        
        
        """
        ...
    def setSvHealth(self, int: int) -> None:
        """
            Setter for the satellite health status.
        
            Parameters:
                svHealth (int): the value to set
        
        
        """
        ...
    def setUraiEd(self, int: int) -> None:
        """
            Setter for Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiEd (int): Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def setUraiNed0(self, int: int) -> None:
        """
            Setter for term 0 of Non-Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiNed0 (int): term 0 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def setUraiNed1(self, int: int) -> None:
        """
            Setter for term 1 of Non-Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiNed1 (int): term 1 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def setUraiNed2(self, int: int) -> None:
        """
            Setter for term 2 of Non-Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiNed2 (int): term 2 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...

_FieldBeidouCivilianNavigationMessage__T = typing.TypeVar('_FieldBeidouCivilianNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBeidouCivilianNavigationMessage(FieldAbstractNavigationMessage[_FieldBeidouCivilianNavigationMessage__T, BeidouCivilianNavigationMessage], typing.Generic[_FieldBeidouCivilianNavigationMessage__T]):
    """
    public class FieldBeidouCivilianNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.BeidouCivilianNavigationMessage`>
    
        Container for data contained in a Beidou civilian navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldBeidouCivilianNavigationMessage__T], typing.Callable[[___init___0__V], _FieldBeidouCivilianNavigationMessage__T]], fieldBeidouCivilianNavigationMessage: 'FieldBeidouCivilianNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldBeidouCivilianNavigationMessage__T], beidouCivilianNavigationMessage: BeidouCivilianNavigationMessage): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldBeidouCivilianNavigationMessage__T, _changeField__U], typing.Callable[[_FieldBeidouCivilianNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def getADot(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for the change rate in semi-major axis.
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.getADot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                the change rate in semi-major axis
        
        
        """
        ...
    def getDeltaN0Dot(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for change rate in Δn₀.
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.getDeltaN0Dot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                change rate in Δn₀
        
        
        """
        ...
    def getHealth(self) -> int:
        """
            Getter for health.
        
            Returns:
                health
        
        
        """
        ...
    def getIODC(self) -> int:
        """
            Getter for the Issue Of Data Clock (IODC).
        
            Returns:
                the Issue Of Data Clock (IODC)
        
        
        """
        ...
    def getIODE(self) -> int:
        """
            Getter for the Issue Of Data Ephemeris (IODE).
        
            Returns:
                the Issue Of Data Ephemeris (IODE)
        
        
        """
        ...
    def getIntegrityFlags(self) -> int:
        """
            Getter for B1C integrity flags.
        
            Returns:
                B1C integrity flags
        
        
        """
        ...
    def getIscB1CD(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for B1 CD.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscB1CP(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for B1 CP.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscB2AD(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for B2 AD.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getRadioWave(self) -> org.orekit.gnss.RadioWave:
        """
            Getter for radio wave.
        
            Returns:
                radio wave on which navigation signal is sent
        
        
        """
        ...
    def getSatelliteType(self) -> BeidouSatelliteType:
        """
            Getter for satellite type.
        
            Returns:
                satellite type
        
        
        """
        ...
    def getSisaiOc1(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (clock drift accuracy).
        
            Returns:
                Signal In Space Accuracy Index (clock drift accuracy)
        
        
        """
        ...
    def getSisaiOc2(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (clock drift rate accuracy).
        
            Returns:
                Signal In Space Accuracy Index (clock drift rate accuracy)
        
        
        """
        ...
    def getSisaiOcb(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (radial and clock).
        
            Returns:
                Signal In Space Accuracy Index (radial and clock)
        
        
        """
        ...
    def getSisaiOe(self) -> int:
        """
            Getter for Signal In Space Accuracy Index (along track and across track).
        
            Returns:
                Signal In Space Accuracy Index (along track and across track)
        
        
        """
        ...
    def getSismai(self) -> int:
        """
            Getter for Signal In Space Monitoring Accuracy Index.
        
            Returns:
                Signal In Space Monitoring Accuracy Index
        
        
        """
        ...
    def getTgdB1Cp(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for B1/B3 Group Delay Differential (s).
        
            Returns:
                B1/B3 Group Delay Differential (s)
        
        
        """
        ...
    def getTgdB2ap(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for B2 AP Group Delay Differential (s).
        
            Returns:
                B2 AP Group Delay Differential (s)
        
        
        """
        ...
    def getTgdB2bI(self) -> _FieldBeidouCivilianNavigationMessage__T:
        """
            Getter for B2B_i / B3I Group Delay Differential (s).
        
            Returns:
                B2B_i / B3I Group Delay Differential (s)
        
        
        """
        ...
    def setADot(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for the change rate in semi-major axis.
        
            Parameters:
                value (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): the change rate in semi-major axis
        
        
        """
        ...
    def setDeltaN0Dot(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for change rate in Δn₀.
        
            Parameters:
                deltaN0Dot (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): change rate in Δn₀
        
        
        """
        ...
    def setHealth(self, int: int) -> None:
        """
            Setter for health.
        
            Parameters:
                health (int): health
        
        
        """
        ...
    def setIODC(self, int: int) -> None:
        """
            Setter for the Issue of Data Clock.
        
            Parameters:
                value (int): the IODC to set
        
        
        """
        ...
    def setIODE(self, int: int) -> None:
        """
            Setter for the Issue of Data Ephemeris.
        
            Parameters:
                value (int): the IODE to set
        
        
        """
        ...
    def setIntegrityFlags(self, int: int) -> None:
        """
            Setter for B1C integrity flags.
        
            Parameters:
                integrityFlags (int): integrity flags
        
        
        """
        ...
    def setIscB1CD(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for B1 CD.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscB1CP(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for B1 CP.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscB2AD(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for B2 AD.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setSatelliteType(self, beidouSatelliteType: BeidouSatelliteType) -> None:
        """
            Setter for satellite type.
        
            Parameters:
                satelliteType (:class:`~org.orekit.propagation.analytical.gnss.data.BeidouSatelliteType`): satellite type
        
        
        """
        ...
    def setSisaiOc1(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (clock drift accuracy).
        
            Parameters:
                sisaiOc1 (int): Signal In Space Accuracy Index (clock drift accuracy)
        
        
        """
        ...
    def setSisaiOc2(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (clock drift rate accuracy).
        
            Parameters:
                sisaiOc2 (int): Signal In Space Accuracy Index (clock drift rate accuracy)
        
        
        """
        ...
    def setSisaiOcb(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (radial and clock).
        
            Parameters:
                sisaiOcb (int): Signal In Space Accuracy Index (radial and clock)
        
        
        """
        ...
    def setSisaiOe(self, int: int) -> None:
        """
            Setter for Signal In Space Accuracy Index (along track and across track).
        
            Parameters:
                sisaiOe (int): Signal In Space Accuracy Index (along track and across track)
        
        
        """
        ...
    def setSismai(self, int: int) -> None:
        """
            Setter for Signal In Space Monitoring Accuracy Index.
        
            Parameters:
                sismai (int): Signal In Space Monitoring Accuracy Index
        
        
        """
        ...
    def setTgdB1Cp(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for B1/B3 Group Delay Differential (s).
        
            Parameters:
                tgdB1Cp (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): B1/B3 Group Delay Differential (s)
        
        
        """
        ...
    def setTgdB2ap(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for B2 AP Group Delay Differential (s).
        
            Parameters:
                tgdB2ap (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): B2 AP Group Delay Differential (s)
        
        
        """
        ...
    def setTgdB2bI(self, t: _FieldBeidouCivilianNavigationMessage__T) -> None:
        """
            Setter for B2B_i / B3I Group Delay Differential (s).
        
            Parameters:
                tgdB2bI (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouCivilianNavigationMessage`): B2B_i / B3I Group Delay Differential (s)
        
        
        """
        ...
    def toNonField(self) -> BeidouCivilianNavigationMessage:
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldBeidouLegacyNavigationMessage__T = typing.TypeVar('_FieldBeidouLegacyNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBeidouLegacyNavigationMessage(FieldAbstractNavigationMessage[_FieldBeidouLegacyNavigationMessage__T, BeidouLegacyNavigationMessage], typing.Generic[_FieldBeidouLegacyNavigationMessage__T]):
    """
    public class FieldBeidouLegacyNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage`>
    
        Container for data contained in a BeiDou navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldBeidouLegacyNavigationMessage__T], typing.Callable[[___init___0__V], _FieldBeidouLegacyNavigationMessage__T]], fieldBeidouLegacyNavigationMessage: 'FieldBeidouLegacyNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldBeidouLegacyNavigationMessage__T], beidouLegacyNavigationMessage: BeidouLegacyNavigationMessage): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldBeidouLegacyNavigationMessage__T, _changeField__U], typing.Callable[[_FieldBeidouLegacyNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def getAODC(self) -> int:
        """
            Getter for the Age Of Data Clock (AODC).
        
            Returns:
                the Age Of Data Clock (AODC)
        
        
        """
        ...
    def getAODE(self) -> int:
        """
            Getter for the Age Of Data Ephemeris (AODE).
        
            Returns:
                the Age Of Data Ephemeris (AODE)
        
        
        """
        ...
    def getSvAccuracy(self) -> _FieldBeidouLegacyNavigationMessage__T:
        """
            Getter for the user SV accuray (meters).
        
            Returns:
                the user SV accuracy
        
        
        """
        ...
    def getTGD1(self) -> _FieldBeidouLegacyNavigationMessage__T:
        """
            Getter for the estimated group delay differential TGD1 for B1I signal.
        
            Returns:
                the estimated group delay differential TGD1 for B1I signal (s)
        
        
        """
        ...
    def getTGD2(self) -> _FieldBeidouLegacyNavigationMessage__T:
        """
            Getter for the estimated group delay differential TGD for B2I signal.
        
            Returns:
                the estimated group delay differential TGD2 for B2I signal (s)
        
        
        """
        ...
    def setAODC(self, t: _FieldBeidouLegacyNavigationMessage__T) -> None:
        """
            Setter for the age of data clock.
        
            Parameters:
                aod (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouLegacyNavigationMessage`): the age of data to set
        
        
        """
        ...
    def setAODE(self, t: _FieldBeidouLegacyNavigationMessage__T) -> None:
        """
            Setter for the age of data ephemeris.
        
            Parameters:
                aod (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouLegacyNavigationMessage`): the age of data to set
        
        
        """
        ...
    def setSvAccuracy(self, t: _FieldBeidouLegacyNavigationMessage__T) -> None:
        """
            Setter for the user SV accuracy.
        
            Parameters:
                svAccuracy (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouLegacyNavigationMessage`): the value to set
        
        
        """
        ...
    def setTGD1(self, t: _FieldBeidouLegacyNavigationMessage__T) -> None:
        """
            Setter for the B1/B3 Group Delay Differential (s).
        
            Parameters:
                tgd (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouLegacyNavigationMessage`): the group delay differential to set
        
        
        """
        ...
    def setTGD2(self, t: _FieldBeidouLegacyNavigationMessage__T) -> None:
        """
            Setter for the B2/B3 Group Delay Differential (s).
        
            Parameters:
                tgd (:class:`~org.orekit.propagation.analytical.gnss.data.FieldBeidouLegacyNavigationMessage`): the group delay differential to set
        
        
        """
        ...
    def toNonField(self) -> BeidouLegacyNavigationMessage:
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldCivilianNavigationMessage__T = typing.TypeVar('_FieldCivilianNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldCivilianNavigationMessage__O = typing.TypeVar('_FieldCivilianNavigationMessage__O', bound=CivilianNavigationMessage)  # <O>
class FieldCivilianNavigationMessage(FieldAbstractNavigationMessage[_FieldCivilianNavigationMessage__T, _FieldCivilianNavigationMessage__O], FieldGNSSClockElements[_FieldCivilianNavigationMessage__T], typing.Generic[_FieldCivilianNavigationMessage__T, _FieldCivilianNavigationMessage__O]):
    """
    public abstract class FieldCivilianNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>, O extends :class:`~org.orekit.propagation.analytical.gnss.data.CivilianNavigationMessage`<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`<T, O> implements :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`<T>
    
        Container for data contained in a GPS/QZNSS civilian navigation message.
    
        Since:
            13.0
    """
    def getADot(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for the change rate in semi-major axis.
        
            This value is non-zero only in civilian navigation messages
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.getADot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                the change rate in semi-major axis
        
        
        """
        ...
    def getDeltaN0Dot(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for change rate in Δn₀.
        
            This value is non-zero only in civilian navigation messages
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.getDeltaN0Dot` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                change rate in Δn₀
        
        
        """
        ...
    def getIscL1CA(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for L1 C/A.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1CD(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for L1 CD.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1CP(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for L1 CP.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL2C(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for L2 C.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL5I5(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for L5I.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL5Q5(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for inter Signal Delay for L5Q.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getSvAccuracy(self) -> _FieldCivilianNavigationMessage__T:
        """
            Getter for the user SV accuray (meters).
        
            Returns:
                the user SV accuracy
        
        
        """
        ...
    def getSvHealth(self) -> int:
        """
            Getter for the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def getUraiEd(self) -> int:
        """
            Getter for Elevation-Dependent User Range Accuracy.
        
            Returns:
                Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def getUraiNed0(self) -> int:
        """
            Getter for term 0 of Non-Elevation-Dependent User Range Accuracy.
        
            Returns:
                term 0 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def getUraiNed1(self) -> int:
        """
            Getter for term 1 of Non-Elevation-Dependent User Range Accuracy.
        
            Returns:
                term 1 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def getUraiNed2(self) -> int:
        """
            Getter for term 2 of Non-Elevation-Dependent User Range Accuracy.
        
            Returns:
                term 2 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def isCnv2(self) -> bool:
        """
            Check it message is a CNV2 message.
        
            Returns:
                true if message is a CNV2 message
        
        
        """
        ...
    def setADot(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for the change rate in semi-major axis.
        
            Parameters:
                value (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): the change rate in semi-major axis
        
        
        """
        ...
    def setDeltaN0Dot(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for change rate in Δn₀.
        
            Parameters:
                deltaN0Dot (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): change rate in Δn₀
        
        
        """
        ...
    def setIscL1CA(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L1 C/A.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscL1CD(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L1 CD.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscL1CP(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L1 CP.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscL2C(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L2 C.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscL5I5(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L5I.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscL5Q5(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L5Q.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): delay to set
        
        
        """
        ...
    def setSvAccuracy(self, t: _FieldCivilianNavigationMessage__T) -> None:
        """
            Setter for the user SV accuracy.
        
            Parameters:
                svAccuracy (:class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`): the value to set
        
        
        """
        ...
    def setSvHealth(self, int: int) -> None:
        """
            Setter for the satellite health status.
        
            Parameters:
                svHealth (int): the value to set
        
        
        """
        ...
    def setUraiEd(self, int: int) -> None:
        """
            Setter for Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiEd (int): Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def setUraiNed0(self, int: int) -> None:
        """
            Setter for term 0 of Non-Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiNed0 (int): term 0 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def setUraiNed1(self, int: int) -> None:
        """
            Setter for term 1 of Non-Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiNed1 (int): term 1 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...
    def setUraiNed2(self, int: int) -> None:
        """
            Setter for term 2 of Non-Elevation-Dependent User Range Accuracy.
        
            Parameters:
                uraiNed2 (int): term 2 of Non-Elevation-Dependent User Range Accuracy
        
        
        """
        ...

_FieldGalileoNavigationMessage__T = typing.TypeVar('_FieldGalileoNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGalileoNavigationMessage(FieldAbstractNavigationMessage[_FieldGalileoNavigationMessage__T, 'GalileoNavigationMessage'], typing.Generic[_FieldGalileoNavigationMessage__T]):
    """
    public class FieldGalileoNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage`>
    
        Container for data contained in a Galileo navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldGalileoNavigationMessage__T], typing.Callable[[___init___0__V], _FieldGalileoNavigationMessage__T]], fieldGalileoNavigationMessage: 'FieldGalileoNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldGalileoNavigationMessage__T], galileoNavigationMessage: 'GalileoNavigationMessage'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldGalileoNavigationMessage__T, _changeField__U], typing.Callable[[_FieldGalileoNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def getBGDE1E5a(self) -> _FieldGalileoNavigationMessage__T:
        """
            Getter for the E1/E5a broadcast group delay.
        
            Returns:
                the E1/E5a broadcast group delay (s)
        
        
        """
        ...
    def getBGDE5bE1(self) -> _FieldGalileoNavigationMessage__T:
        """
            Getter for the the Broadcast Group Delay E5b/E1.
        
            Returns:
                the Broadcast Group Delay E5b/E1 (s)
        
        
        """
        ...
    def getDataSource(self) -> int:
        """
            Getter for the the data source.
        
            Returns:
                the data source
        
        
        """
        ...
    def getIODNav(self) -> int:
        """
            Getter for the the Issue Of Data (IOD).
        
            Returns:
                the Issue Of Data (IOD)
        
        
        """
        ...
    def getSisa(self) -> _FieldGalileoNavigationMessage__T:
        """
            Getter for the signal in space accuracy (m).
        
            Returns:
                the signal in space accuracy
        
        
        """
        ...
    def getSvHealth(self) -> _FieldGalileoNavigationMessage__T:
        """
            Getter for the SV health status.
        
            Returns:
                the SV health status
        
        
        """
        ...
    def setBGDE1E5a(self, t: _FieldGalileoNavigationMessage__T) -> None:
        """
            Setter for the E1/E5a broadcast group delay (s).
        
            Parameters:
                bgd (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGalileoNavigationMessage`): the E1/E5a broadcast group delay to set
        
        
        """
        ...
    def setBGDE5bE1(self, t: _FieldGalileoNavigationMessage__T) -> None:
        """
            Setter for the E5b/E1 broadcast group delay (s).
        
            Parameters:
                bgd (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGalileoNavigationMessage`): the E5b/E1 broadcast group delay to set
        
        
        """
        ...
    def setDataSource(self, int: int) -> None:
        """
            Setter for the data source.
        
            Parameters:
                dataSource (int): data source
        
        
        """
        ...
    def setIODNav(self, int: int) -> None:
        """
            Setter for the Issue of Data of the navigation batch.
        
            Parameters:
                iod (int): the IOD to set
        
        
        """
        ...
    def setSisa(self, t: _FieldGalileoNavigationMessage__T) -> None:
        """
            Setter for the signal in space accuracy.
        
            Parameters:
                sisa (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGalileoNavigationMessage`): the sisa to set
        
        
        """
        ...
    def setSvHealth(self, t: _FieldGalileoNavigationMessage__T) -> None:
        """
            Setter for the SV health status.
        
            Parameters:
                svHealth (:class:`~org.orekit.propagation.analytical.gnss.data.FieldGalileoNavigationMessage`): the SV health status to set
        
        
        """
        ...
    def toNonField(self) -> 'GalileoNavigationMessage':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldLegacyNavigationMessage__T = typing.TypeVar('_FieldLegacyNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldLegacyNavigationMessage__O = typing.TypeVar('_FieldLegacyNavigationMessage__O', bound='LegacyNavigationMessage')  # <O>
class FieldLegacyNavigationMessage(FieldAbstractNavigationMessage[_FieldLegacyNavigationMessage__T, _FieldLegacyNavigationMessage__O], FieldGNSSClockElements[_FieldLegacyNavigationMessage__T], typing.Generic[_FieldLegacyNavigationMessage__T, _FieldLegacyNavigationMessage__O]):
    """
    public abstract class FieldLegacyNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>, O extends :class:`~org.orekit.propagation.analytical.gnss.data.LegacyNavigationMessage`<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldAbstractNavigationMessage`<T, O> implements :class:`~org.orekit.propagation.analytical.gnss.data.FieldGNSSClockElements`<T>
    
        Container for data contained in a GPS/QZNSS legacy navigation message.
    
        Since:
            13.0
    """
    def getFitInterval(self) -> int:
        """
            Getter for the fit interval.
        
            Returns:
                the fit interval
        
        
        """
        ...
    def getIODC(self) -> int:
        """
            Getter for the Issue Of Data Clock (IODC).
        
            Returns:
                the Issue Of Data Clock (IODC)
        
        
        """
        ...
    def getIODE(self) -> int:
        """
            Getter for the Issue Of Data Ephemeris (IODE).
        
            Returns:
                the Issue Of Data Ephemeris (IODE)
        
        
        """
        ...
    def getSvAccuracy(self) -> _FieldLegacyNavigationMessage__T:
        """
            Getter for the user SV accuray (meters).
        
            Returns:
                the user SV accuracy
        
        
        """
        ...
    def getSvHealth(self) -> int:
        """
            Getter for the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def setFitInterval(self, int: int) -> None:
        """
            Setter for the fit interval.
        
            Parameters:
                fitInterval (int): fit interval
        
        
        """
        ...
    def setIODC(self, int: int) -> None:
        """
            Setter for the Issue of Data Clock.
        
            Parameters:
                value (int): the IODC to set
        
        
        """
        ...
    def setIODE(self, t: _FieldLegacyNavigationMessage__T) -> None:
        """
            Setter for the Issue of Data Ephemeris.
        
            Parameters:
                value (:class:`~org.orekit.propagation.analytical.gnss.data.FieldLegacyNavigationMessage`): the IODE to set
        
        
        """
        ...
    def setSvAccuracy(self, t: _FieldLegacyNavigationMessage__T) -> None:
        """
            Setter for the user SV accuracy.
        
            Parameters:
                svAccuracy (:class:`~org.orekit.propagation.analytical.gnss.data.FieldLegacyNavigationMessage`): the value to set
        
        
        """
        ...
    def setSvHealth(self, int: int) -> None:
        """
            Setter for the satellite health status.
        
            Parameters:
                svHealth (int): the value to set
        
        
        """
        ...

class GalileoNavigationMessage(AbstractNavigationMessage['GalileoNavigationMessage']):
    """
    public class GalileoNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage`>
    
        Container for data contained in a Galileo navigation message.
    
        Since:
            11.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldGalileoNavigationMessage: FieldGalileoNavigationMessage[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def getBGDE1E5a(self) -> float:
        """
            Getter for the E1/E5a broadcast group delay.
        
            Returns:
                the E1/E5a broadcast group delay (s)
        
        
        """
        ...
    def getBGDE5bE1(self) -> float:
        """
            Getter for the the Broadcast Group Delay E5b/E1.
        
            Returns:
                the Broadcast Group Delay E5b/E1 (s)
        
        
        """
        ...
    def getDataSource(self) -> int:
        """
            Getter for the the data source.
        
            Returns:
                the data source
        
            Since:
                12.0
        
        
        """
        ...
    def getIODNav(self) -> int:
        """
            Getter for the the Issue Of Data (IOD).
        
            Returns:
                the Issue Of Data (IOD)
        
        
        """
        ...
    def getSisa(self) -> float:
        """
            Getter for the signal in space accuracy (m).
        
            Returns:
                the signal in space accuracy
        
        
        """
        ...
    def getSvHealth(self) -> float:
        """
            Getter for the SV health status.
        
            Returns:
                the SV health status
        
        
        """
        ...
    def setBGDE1E5a(self, double: float) -> None:
        """
            Setter for the E1/E5a broadcast group delay (s).
        
            Parameters:
                bgd (double): the E1/E5a broadcast group delay to set
        
        
        """
        ...
    def setBGDE5bE1(self, double: float) -> None:
        """
            Setter for the E5b/E1 broadcast group delay (s).
        
            Parameters:
                bgd (double): the E5b/E1 broadcast group delay to set
        
        
        """
        ...
    def setDataSource(self, int: int) -> None:
        """
            Setter for the data source.
        
            Parameters:
                dataSource (int): data source
        
            Since:
                12.0
        
        
        """
        ...
    def setIODNav(self, int: int) -> None:
        """
            Setter for the Issue of Data of the navigation batch.
        
            Parameters:
                iod (int): the IOD to set
        
        
        """
        ...
    def setSisa(self, double: float) -> None:
        """
            Setter for the signal in space accuracy.
        
            Parameters:
                sisa (double): the sisa to set
        
        
        """
        ...
    def setSvHealth(self, double: float) -> None:
        """
            Setter for the SV health status.
        
            Parameters:
                svHealth (double): the SV health status to set
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

_LegacyNavigationMessage__O = typing.TypeVar('_LegacyNavigationMessage__O', bound='LegacyNavigationMessage')  # <O>
class LegacyNavigationMessage(AbstractNavigationMessage[_LegacyNavigationMessage__O], GNSSClockElements, typing.Generic[_LegacyNavigationMessage__O]):
    """
    public abstract class LegacyNavigationMessage<O extends LegacyNavigationMessage<O>> extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage`<O> implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
    
        Container for data contained in a GPS/QZNSS legacy navigation message.
    
        Since:
            11.0
    """
    LNAV: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.gnss.data.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` LNAV
    
        Identifier for message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getFitInterval(self) -> int:
        """
            Getter for the fit interval.
        
            Returns:
                the fit interval
        
            Since:
                12.0
        
        
        """
        ...
    def getIODC(self) -> int:
        """
            Getter for the Issue Of Data Clock (IODC).
        
            Returns:
                the Issue Of Data Clock (IODC)
        
        
        """
        ...
    def getIODE(self) -> int:
        """
            Getter for the Issue Of Data Ephemeris (IODE).
        
            Returns:
                the Issue Of Data Ephemeris (IODE)
        
        
        """
        ...
    def getSvAccuracy(self) -> float:
        """
            Getter for the user SV accuray (meters).
        
            Returns:
                the user SV accuracy
        
        
        """
        ...
    def getSvHealth(self) -> int:
        """
            Getter for the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def setFitInterval(self, int: int) -> None:
        """
            Setter for the fit interval.
        
            Parameters:
                fitInterval (int): fit interval
        
            Since:
                12.0
        
        
        """
        ...
    def setIODC(self, int: int) -> None:
        """
            Setter for the Issue of Data Clock.
        
            Parameters:
                value (int): the IODC to set
        
        
        """
        ...
    def setIODE(self, double: float) -> None:
        """
            Setter for the Issue of Data Ephemeris.
        
            Parameters:
                value (double): the IODE to set
        
        
        """
        ...
    def setSvAccuracy(self, double: float) -> None:
        """
            Setter for the user SV accuracy.
        
            Parameters:
                svAccuracy (double): the value to set
        
        
        """
        ...
    def setSvHealth(self, int: int) -> None:
        """
            Setter for the satellite health status.
        
            Parameters:
                svHealth (int): the value to set
        
        
        """
        ...

_FieldGPSCivilianNavigationMessage__T = typing.TypeVar('_FieldGPSCivilianNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGPSCivilianNavigationMessage(FieldCivilianNavigationMessage[_FieldGPSCivilianNavigationMessage__T, 'GPSCivilianNavigationMessage'], typing.Generic[_FieldGPSCivilianNavigationMessage__T]):
    """
    public class FieldGPSCivilianNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.GPSCivilianNavigationMessage`>
    
        Container for data contained in a GPS navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldGPSCivilianNavigationMessage__T], typing.Callable[[___init___0__V], _FieldGPSCivilianNavigationMessage__T]], fieldGPSCivilianNavigationMessage: 'FieldGPSCivilianNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldGPSCivilianNavigationMessage__T], gPSCivilianNavigationMessage: 'GPSCivilianNavigationMessage'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldGPSCivilianNavigationMessage__T, _changeField__U], typing.Callable[[_FieldGPSCivilianNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def toNonField(self) -> 'GPSCivilianNavigationMessage':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldGPSLegacyNavigationMessage__T = typing.TypeVar('_FieldGPSLegacyNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGPSLegacyNavigationMessage(FieldLegacyNavigationMessage[_FieldGPSLegacyNavigationMessage__T, 'GPSLegacyNavigationMessage'], typing.Generic[_FieldGPSLegacyNavigationMessage__T]):
    """
    public class FieldGPSLegacyNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldLegacyNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage`>
    
        Container for data contained in a GPS navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldGPSLegacyNavigationMessage__T], typing.Callable[[___init___0__V], _FieldGPSLegacyNavigationMessage__T]], fieldGPSLegacyNavigationMessage: 'FieldGPSLegacyNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldGPSLegacyNavigationMessage__T], gPSLegacyNavigationMessage: 'GPSLegacyNavigationMessage'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldGPSLegacyNavigationMessage__T, _changeField__U], typing.Callable[[_FieldGPSLegacyNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def toNonField(self) -> 'GPSLegacyNavigationMessage':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldNavicL1NVNavigationMessage__T = typing.TypeVar('_FieldNavicL1NVNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNavicL1NVNavigationMessage(FieldCivilianNavigationMessage[_FieldNavicL1NVNavigationMessage__T, 'NavICL1NVNavigationMessage'], typing.Generic[_FieldNavicL1NVNavigationMessage__T]):
    """
    public class FieldNavicL1NVNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.NavICL1NVNavigationMessage`>
    
        Container for data contained in a NavIC navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldNavicL1NVNavigationMessage__T], typing.Callable[[___init___0__V], _FieldNavicL1NVNavigationMessage__T]], fieldNavicL1NVNavigationMessage: 'FieldNavicL1NVNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNavicL1NVNavigationMessage__T], navICL1NVNavigationMessage: 'NavICL1NVNavigationMessage'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldNavicL1NVNavigationMessage__T, _changeField__U], typing.Callable[[_FieldNavicL1NVNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def getIscL1DL1P(self) -> _FieldNavicL1NVNavigationMessage__T:
        """
            Getter for inter Signal Delay for L1D L1P.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1DS(self) -> _FieldNavicL1NVNavigationMessage__T:
        """
            Getter for inter Signal Delay for L1D S.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1PS(self) -> _FieldNavicL1NVNavigationMessage__T:
        """
            Getter for inter Signal Delay for L1P S.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscSL1P(self) -> _FieldNavicL1NVNavigationMessage__T:
        """
            Getter for inter Signal Delay for S L1P.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getReferenceSignalFlag(self) -> int:
        """
            Get reference signal flag.
        
            Returns:
                reference signal flag
        
        
        """
        ...
    def getTGDSL5(self) -> _FieldNavicL1NVNavigationMessage__T:
        """
            Set the estimated group delay differential TGD for S-L5 correction.
        
            Returns:
                estimated group delay differential TGD for S-L3 correction (s)
        
        
        """
        ...
    def setIscL1DL1P(self, t: _FieldNavicL1NVNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L1D L1P.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldNavicL1NVNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscL1DS(self, t: _FieldNavicL1NVNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L1D S.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldNavicL1NVNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscL1PS(self, t: _FieldNavicL1NVNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for L1P S.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldNavicL1NVNavigationMessage`): delay to set
        
        
        """
        ...
    def setIscSL1P(self, t: _FieldNavicL1NVNavigationMessage__T) -> None:
        """
            Setter for inter Signal Delay for S L1P.
        
            Parameters:
                delay (:class:`~org.orekit.propagation.analytical.gnss.data.FieldNavicL1NVNavigationMessage`): delay to set
        
        
        """
        ...
    def setReferenceSignalFlag(self, int: int) -> None:
        """
            Set reference signal flag.
        
            Parameters:
                referenceSignalFlag (int): reference signal flag
        
        
        """
        ...
    def setTGDSL5(self, t: _FieldNavicL1NVNavigationMessage__T) -> None:
        """
            Set the estimated group delay differential TGD for S-L5 correction.
        
            Parameters:
                groupDelayDifferential (:class:`~org.orekit.propagation.analytical.gnss.data.FieldNavicL1NVNavigationMessage`): the estimated group delay differential TGD for S-L3 correction (s)
        
        
        """
        ...
    def toNonField(self) -> 'NavICL1NVNavigationMessage':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldNavicLegacyNavigationMessage__T = typing.TypeVar('_FieldNavicLegacyNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNavicLegacyNavigationMessage(FieldLegacyNavigationMessage[_FieldNavicLegacyNavigationMessage__T, 'NavICLegacyNavigationMessage'], typing.Generic[_FieldNavicLegacyNavigationMessage__T]):
    """
    public class FieldNavicLegacyNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldLegacyNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.NavICLegacyNavigationMessage`>
    
        Container for data contained in an NavIC navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldNavicLegacyNavigationMessage__T], typing.Callable[[___init___0__V], _FieldNavicLegacyNavigationMessage__T]], fieldNavicLegacyNavigationMessage: 'FieldNavicLegacyNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNavicLegacyNavigationMessage__T], navICLegacyNavigationMessage: 'NavICLegacyNavigationMessage'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldNavicLegacyNavigationMessage__T, _changeField__U], typing.Callable[[_FieldNavicLegacyNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def toNonField(self) -> 'NavICLegacyNavigationMessage':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldQZSSCivilianNavigationMessage__T = typing.TypeVar('_FieldQZSSCivilianNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQZSSCivilianNavigationMessage(FieldCivilianNavigationMessage[_FieldQZSSCivilianNavigationMessage__T, 'QZSSCivilianNavigationMessage'], typing.Generic[_FieldQZSSCivilianNavigationMessage__T]):
    """
    public class FieldQZSSCivilianNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldCivilianNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.QZSSCivilianNavigationMessage`>
    
        Container for data contained in a QZSS navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldQZSSCivilianNavigationMessage__T], typing.Callable[[___init___0__V], _FieldQZSSCivilianNavigationMessage__T]], fieldQZSSCivilianNavigationMessage: 'FieldQZSSCivilianNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldQZSSCivilianNavigationMessage__T], qZSSCivilianNavigationMessage: 'QZSSCivilianNavigationMessage'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldQZSSCivilianNavigationMessage__T, _changeField__U], typing.Callable[[_FieldQZSSCivilianNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def toNonField(self) -> 'QZSSCivilianNavigationMessage':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

_FieldQZSSLegacyNavigationMessage__T = typing.TypeVar('_FieldQZSSLegacyNavigationMessage__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQZSSLegacyNavigationMessage(FieldLegacyNavigationMessage[_FieldQZSSLegacyNavigationMessage__T, 'QZSSLegacyNavigationMessage'], typing.Generic[_FieldQZSSLegacyNavigationMessage__T]):
    """
    public class FieldQZSSLegacyNavigationMessage<T extends :class:`~org.orekit.propagation.analytical.gnss.data.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.gnss.data.FieldLegacyNavigationMessage`<T, :class:`~org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage`>
    
        Container for data contained in a QZSS navigation message.
    
        Since:
            13.0
    """
    ___init___0__V = typing.TypeVar('___init___0__V', bound=org.hipparchus.CalculusFieldElement)  # <V>
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[___init___0__V, _FieldQZSSLegacyNavigationMessage__T], typing.Callable[[___init___0__V], _FieldQZSSLegacyNavigationMessage__T]], fieldQZSSLegacyNavigationMessage: 'FieldQZSSLegacyNavigationMessage'[___init___0__V]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldQZSSLegacyNavigationMessage__T], qZSSLegacyNavigationMessage: 'QZSSLegacyNavigationMessage'): ...
    _changeField__U = typing.TypeVar('_changeField__U', bound=org.hipparchus.CalculusFieldElement)  # <U>
    _changeField__G = typing.TypeVar('_changeField__G', bound=FieldGnssOrbitalElements)  # <G>
    def changeField(self, function: typing.Union[java.util.function.Function[_FieldQZSSLegacyNavigationMessage__T, _changeField__U], typing.Callable[[_FieldQZSSLegacyNavigationMessage__T], _changeField__U]]) -> _changeField__G: ...
    def toNonField(self) -> 'QZSSLegacyNavigationMessage':
        """
            Create a non-field version of the instance.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements.toNonField` in
                class :class:`~org.orekit.propagation.analytical.gnss.data.FieldGnssOrbitalElements`
        
            Returns:
                non-field version of the instance
        
        
        """
        ...

class GPSCivilianNavigationMessage(CivilianNavigationMessage['GPSCivilianNavigationMessage']):
    """
    public class GPSCivilianNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.CivilianNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.GPSCivilianNavigationMessage`>
    
        Container for data contained in a GPS navigation message.
    
        Since:
            12.0
    """
    ___init___1__T = typing.TypeVar('___init___1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, boolean: bool, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, fieldGPSCivilianNavigationMessage: FieldGPSCivilianNavigationMessage[___init___1__T]): ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class GPSLegacyNavigationMessage(LegacyNavigationMessage['GPSLegacyNavigationMessage']):
    """
    public class GPSLegacyNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.LegacyNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage`>
    
        Container for data contained in a GPS navigation message.
    
        Since:
            11.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldGPSLegacyNavigationMessage: FieldGPSLegacyNavigationMessage[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class NavICL1NVNavigationMessage(CivilianNavigationMessage['NavICL1NVNavigationMessage']):
    """
    public class NavICL1NVNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.CivilianNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.NavICL1NVNavigationMessage`>
    
        Container for data contained in a NavIC navigation message.
    
        Since:
            13.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldNavicL1NVNavigationMessage: FieldNavicL1NVNavigationMessage[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    def getIscL1DL1P(self) -> float:
        """
            Getter for inter Signal Delay for L1D L1P.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1DS(self) -> float:
        """
            Getter for inter Signal Delay for L1D S.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscL1PS(self) -> float:
        """
            Getter for inter Signal Delay for L1P S.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getIscSL1P(self) -> float:
        """
            Getter for inter Signal Delay for S L1P.
        
            Returns:
                inter signal delay
        
        
        """
        ...
    def getReferenceSignalFlag(self) -> int:
        """
            Get reference signal flag.
        
            Returns:
                reference signal flag
        
        
        """
        ...
    def getTGDSL5(self) -> float:
        """
            Set the estimated group delay differential TGD for S-L5 correction.
        
            Returns:
                estimated group delay differential TGD for S-L3 correction (s)
        
        
        """
        ...
    def setIscL1DL1P(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L1D L1P.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscL1DS(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L1D S.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscL1PS(self, double: float) -> None:
        """
            Setter for inter Signal Delay for L1P S.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setIscSL1P(self, double: float) -> None:
        """
            Setter for inter Signal Delay for S L1P.
        
            Parameters:
                delay (double): delay to set
        
        
        """
        ...
    def setReferenceSignalFlag(self, int: int) -> None:
        """
            Set reference signal flag.
        
            Parameters:
                referenceSignalFlag (int): reference signal flag
        
        
        """
        ...
    def setTGDSL5(self, double: float) -> None:
        """
            Set the estimated group delay differential TGD for S-L5 correction.
        
            Parameters:
                groupDelayDifferential (double): the estimated group delay differential TGD for S-L3 correction (s)
        
        
        """
        ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class NavICLegacyNavigationMessage(LegacyNavigationMessage['NavICLegacyNavigationMessage']):
    """
    public class NavICLegacyNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.LegacyNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.NavICLegacyNavigationMessage`>
    
        Container for data contained in an NavIC navigation message.
    
        Since:
            11.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldNavicLegacyNavigationMessage: FieldNavicLegacyNavigationMessage[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class QZSSCivilianNavigationMessage(CivilianNavigationMessage['QZSSCivilianNavigationMessage']):
    """
    public class QZSSCivilianNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.CivilianNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.QZSSCivilianNavigationMessage`>
    
        Container for data contained in a QZSS navigation message.
    
        Since:
            12.0
    """
    ___init___1__T = typing.TypeVar('___init___1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, boolean: bool, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, fieldQZSSCivilianNavigationMessage: FieldQZSSCivilianNavigationMessage[___init___1__T]): ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...

class QZSSLegacyNavigationMessage(LegacyNavigationMessage['QZSSLegacyNavigationMessage']):
    """
    public class QZSSLegacyNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.LegacyNavigationMessage`<:class:`~org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage`>
    
        Container for data contained in a QZSS navigation message.
    
        Since:
            11.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, fieldQZSSLegacyNavigationMessage: FieldQZSSLegacyNavigationMessage[___init___0__T]): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    _toField__T = typing.TypeVar('_toField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _toField__F = typing.TypeVar('_toField__F', bound=FieldGnssOrbitalElements)  # <F>
    def toField(self, field: org.hipparchus.Field[_toField__T]) -> _toField__F: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.gnss.data")``.

    AbstractAlmanac: typing.Type[AbstractAlmanac]
    AbstractEphemerisMessage: typing.Type[AbstractEphemerisMessage]
    AbstractNavigationMessage: typing.Type[AbstractNavigationMessage]
    BeidouAlmanac: typing.Type[BeidouAlmanac]
    BeidouCivilianNavigationMessage: typing.Type[BeidouCivilianNavigationMessage]
    BeidouLegacyNavigationMessage: typing.Type[BeidouLegacyNavigationMessage]
    BeidouSatelliteType: typing.Type[BeidouSatelliteType]
    CivilianNavigationMessage: typing.Type[CivilianNavigationMessage]
    CommonGnssData: typing.Type[CommonGnssData]
    FieldAbstractAlmanac: typing.Type[FieldAbstractAlmanac]
    FieldAbstractNavigationMessage: typing.Type[FieldAbstractNavigationMessage]
    FieldBeidouAlmanac: typing.Type[FieldBeidouAlmanac]
    FieldBeidouCivilianNavigationMessage: typing.Type[FieldBeidouCivilianNavigationMessage]
    FieldBeidouLegacyNavigationMessage: typing.Type[FieldBeidouLegacyNavigationMessage]
    FieldCivilianNavigationMessage: typing.Type[FieldCivilianNavigationMessage]
    FieldCommonGnssData: typing.Type[FieldCommonGnssData]
    FieldGNSSClockElements: typing.Type[FieldGNSSClockElements]
    FieldGPSAlmanac: typing.Type[FieldGPSAlmanac]
    FieldGPSCivilianNavigationMessage: typing.Type[FieldGPSCivilianNavigationMessage]
    FieldGPSLegacyNavigationMessage: typing.Type[FieldGPSLegacyNavigationMessage]
    FieldGalileoAlmanac: typing.Type[FieldGalileoAlmanac]
    FieldGalileoNavigationMessage: typing.Type[FieldGalileoNavigationMessage]
    FieldGnssOrbitalElements: typing.Type[FieldGnssOrbitalElements]
    FieldLegacyNavigationMessage: typing.Type[FieldLegacyNavigationMessage]
    FieldNavICAlmanac: typing.Type[FieldNavICAlmanac]
    FieldNavicL1NVNavigationMessage: typing.Type[FieldNavicL1NVNavigationMessage]
    FieldNavicLegacyNavigationMessage: typing.Type[FieldNavicLegacyNavigationMessage]
    FieldQZSSAlmanac: typing.Type[FieldQZSSAlmanac]
    FieldQZSSCivilianNavigationMessage: typing.Type[FieldQZSSCivilianNavigationMessage]
    FieldQZSSLegacyNavigationMessage: typing.Type[FieldQZSSLegacyNavigationMessage]
    GLONASSAlmanac: typing.Type[GLONASSAlmanac]
    GLONASSEphemeris: typing.Type[GLONASSEphemeris]
    GLONASSNavigationMessage: typing.Type[GLONASSNavigationMessage]
    GLONASSOrbitalElements: typing.Type[GLONASSOrbitalElements]
    GNSSClockElements: typing.Type[GNSSClockElements]
    GNSSConstants: typing.Type[GNSSConstants]
    GNSSOrbitalElements: typing.Type[GNSSOrbitalElements]
    GNSSOrbitalElementsDriversProvider: typing.Type[GNSSOrbitalElementsDriversProvider]
    GPSAlmanac: typing.Type[GPSAlmanac]
    GPSCivilianNavigationMessage: typing.Type[GPSCivilianNavigationMessage]
    GPSLegacyNavigationMessage: typing.Type[GPSLegacyNavigationMessage]
    GalileoAlmanac: typing.Type[GalileoAlmanac]
    GalileoNavigationMessage: typing.Type[GalileoNavigationMessage]
    LegacyNavigationMessage: typing.Type[LegacyNavigationMessage]
    NavICAlmanac: typing.Type[NavICAlmanac]
    NavICL1NVNavigationMessage: typing.Type[NavICL1NVNavigationMessage]
    NavICLegacyNavigationMessage: typing.Type[NavICLegacyNavigationMessage]
    PythonFieldGNSSClockElements: typing.Type[PythonFieldGNSSClockElements]
    PythonSBASOrbitalElements: typing.Type[PythonSBASOrbitalElements]
    QZSSAlmanac: typing.Type[QZSSAlmanac]
    QZSSCivilianNavigationMessage: typing.Type[QZSSCivilianNavigationMessage]
    QZSSLegacyNavigationMessage: typing.Type[QZSSLegacyNavigationMessage]
    SBASNavigationMessage: typing.Type[SBASNavigationMessage]
    SBASOrbitalElements: typing.Type[SBASOrbitalElements]
