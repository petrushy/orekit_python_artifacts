import org.orekit.time
import typing



class AbstractEphemerisMessage:
    """
    public abstract class AbstractEphemerisMessage extends Object
    
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
                the satellite X acceleration in m/sÂ²
        
        
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
                the satellite Y acceleration in m/sÂ²
        
        
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
                the satellite Z acceleration in m/sÂ²
        
        
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
                ax (double): the satellite X acceleration (m/sÂ²) to set
        
        
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
                ay (double): the satellite Y acceleration (m/sÂ²) to set
        
        
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
                az (double): the satellite Z acceleration (m/sÂ²) to set
        
        
        """
        ...

class CommonGnssData:
    """
    public class CommonGnssData extends Object
    
        Container for common GNSS data contained in almanac and navigation messages.
    
        Since:
            11.0
    """
    def __init__(self, double: float, double2: float, int: int): ...
    def getAf0(self) -> float:
        """
            Getter for the the SV Clock Bias Correction Coefficient.
        
            Returns:
                the SV Clock Bias Correction Coefficient (s).
        
        
        """
        ...
    def getAf1(self) -> float:
        """
            Getter for the SV Clock Drift Correction Coefficient.
        
            Returns:
                the SV Clock Drift Correction Coefficient (s/s).
        
        
        """
        ...
    def getAngularVelocity(self) -> float:
        """
            Getter for the mean angular velocity of the Earth for the GNSS model.
        
            Returns:
                the mean angular velocity of the Earth for the GNSS model
        
        
        """
        ...
    def getCycleDuration(self) -> float:
        """
            Getter for the duration of the GNSS cycle in seconds.
        
            Returns:
                the duration of the GNSS cycle in seconds
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for the ephemeris reference date.
        
            Returns:
                the ephemeris reference date
        
        
        """
        ...
    def getE(self) -> float:
        """
            Getter for the eccentricity.
        
            Returns:
                the eccentricity
        
        
        """
        ...
    def getI0(self) -> float:
        """
            Getter for the inclination angle at reference time.
        
            Returns:
                the inclination angle at reference time in radians
        
        
        """
        ...
    def getM0(self) -> float:
        """
            Getter for the mean anomaly at reference time.
        
            Returns:
                the mean anomaly at reference time in radians
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Getter for the Earth's universal gravitational parameter.
        
            Returns:
                the Earth's universal gravitational parameter
        
        
        """
        ...
    def getOmega0(self) -> float:
        """
            Getter for the longitude of ascending node of orbit plane at weekly epoch.
        
            Returns:
                the longitude of ascending node of orbit plane at weekly epoch in radians
        
        
        """
        ...
    def getOmegaDot(self) -> float:
        """
            Getter for the rate of right ascension.
        
            Returns:
                the rate of right ascension in rad/s
        
        
        """
        ...
    def getPRN(self) -> int:
        """
            Getter for the PRN number of the satellite.
        
            Returns:
                the PRN number of the satellite
        
        
        """
        ...
    def getPa(self) -> float:
        """
            Getter for the argument of perigee.
        
            Returns:
                the argument of perigee in radians
        
        
        """
        ...
    def getSma(self) -> float:
        """
            Getter for the semi-major axis.
        
            Returns:
                the semi-major axis in meters
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Getter for the reference time of the GNSS orbit as a duration from week start.
        
            Returns:
                the reference time in seconds
        
        
        """
        ...
    def getWeek(self) -> int:
        """
            Getter for the reference week of the GNSS orbit.
        
            Returns:
                the reference week of the GNSS orbit
        
        
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
    def setDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the reference epoch.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the epoch to set
        
        
        """
        ...
    def setE(self, double: float) -> None:
        """
            Setter the eccentricity.
        
            Parameters:
                e (double): the eccentricity to set
        
        
        """
        ...
    def setI0(self, double: float) -> None:
        """
            Setter for the Inclination Angle at Reference Time (rad).
        
            Parameters:
                i0 (double): the inclination to set
        
        
        """
        ...
    def setM0(self, double: float) -> None:
        """
            Setter for the Mean Anomaly at Reference Time (rad).
        
            Parameters:
                m0 (double): the mean anomaly to set
        
        
        """
        ...
    def setOmega0(self, double: float) -> None:
        """
            Setter for the Longitude of Ascending Node of Orbit Plane at Weekly Epoch (rad).
        
            Parameters:
                omega0 (double): the longitude of ascending node to set
        
        
        """
        ...
    def setOmegaDot(self, double: float) -> None:
        """
            Setter for the rate of Rate of Right Ascension (rad/s).
        
            Parameters:
                omegaDot (double): the rate of right ascension to set
        
        
        """
        ...
    def setPRN(self, int: int) -> None:
        """
            Setter for the PRN number of the satellite.
        
            Parameters:
                number (int): the prn number ot set
        
        
        """
        ...
    def setPa(self, double: float) -> None:
        """
            Setter fir the Argument of Perigee (rad).
        
            Parameters:
                omega (double): the argumet of perigee to set
        
        
        """
        ...
    def setSma(self, double: float) -> None:
        """
            Setter for the semi-major axis.
        
            Parameters:
                sma (double): the semi-major axis (m)
        
        
        """
        ...
    def setTime(self, double: float) -> None:
        """
            Setter for the reference time of the orbit as a duration from week start.
        
            Parameters:
                time (double): the time to set
        
        
        """
        ...
    def setWeek(self, int: int) -> None:
        """
            Setter for the reference week of the orbit.
        
            Parameters:
                week (int): the week to set
        
        
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
                the GLONASS ECEF-X component of satellite acceleration vector in PZ-90 datum (m/sÂ²)
        
        
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
                the GLONASS ECEF-Y component of satellite acceleration vector in PZ-90 datum (m/sÂ²)
        
        
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
                the GLONASS ECEF-Z component of satellite acceleration vector in PZ-90 datum (m/sÂ²)
        
        
        """
        ...

class GNSSClockElements(org.orekit.time.TimeStamped):
    """
    public interface GNSSClockElements extends :class:`~org.orekit.time.TimeStamped`
    
        This interface provides the minimal set of orbital elements needed by the
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
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getToc`
        
        
        """
        ...
    def getAf1(self) -> float:
        """
            Gets the First Order Clock Correction.
        
            Returns:
                the First Order Clock Correction (s/s)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf2`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getToc`
        
        
        """
        ...
    def getAf2(self) -> float:
        """
            Gets the Second Order Clock Correction.
        
            Returns:
                the Second Order Clock Correction (s/sÂ²)
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1`,
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getToc`
        
        
        """
        ...
    def getCycleDuration(self) -> float:
        """
            Gets the duration of the GNSS cycle in seconds.
        
            Returns:
                the duration of the GNSS cycle in seconds
        
        
        """
        ...
    def getTGD(self) -> float:
        """
            Gets the estimated group delay differential TGD for L1-L2 correction.
        
            Returns:
                the estimated group delay differential TGD for L1-L2 correction (s)
        
        
        """
        ...
    def getToc(self) -> float:
        """
            Gets the clock correction reference time toc.
        
            Returns:
                the clock correction reference time (s)
        
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
    
        Earth's universal gravitational parameter for Beidou user in mÂ³/sÂ².
    
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
    
        Earth's universal gravitational parameter for Galileo user in mÂ³/sÂ².
    
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
    
        Value of the Earth's universal gravitational parameter for GLONASS user in mÂ³/sÂ².
    
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
    
        WGS 84 value of the Earth's universal gravitational parameter for GPS user in mÂ³/sÂ².
    
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
    IRNSS_MU: typing.ClassVar[float] = ...
    """
    static final double IRNSS_MU
    
        WGS 84 value of the Earth's universal gravitational parameter for IRNSS user in mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    IRNSS_WEEK_NB: typing.ClassVar[int] = ...
    """
    static final int IRNSS_WEEK_NB
    
        Number of weeks in the IRNSS cycle.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IRNSS_AV: typing.ClassVar[float] = ...
    """
    static final double IRNSS_AV
    
        Value of the earth's rotation rate in rad/s for IRNSS user.
    
        Also see:
            :meth:`~constant`
    
    
    """
    QZSS_MU: typing.ClassVar[float] = ...
    """
    static final double QZSS_MU
    
        WGS 84 value of the Earth's universal gravitational parameter for QZSS user in mÂ³/sÂ².
    
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
    
        WGS 84 value of the Earth's universal gravitational parameter for SBAS user in mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """

class GNSSOrbitalElements(org.orekit.time.TimeStamped):
    """
    public interface GNSSOrbitalElements extends :class:`~org.orekit.time.TimeStamped`
    
        This interface provides the minimal set of orbital elements needed by the
        :class:`~org.orekit.propagation.analytical.gnss.GNSSPropagator`.
    """
    def getAngularVelocity(self) -> float:
        """
            Gets the mean angular velocity of the Earth of the GNSS model.
        
            Returns:
                the mean angular velocity of the Earth of the GNSS model
        
        
        """
        ...
    def getCic(self) -> float:
        """
            Gets the Amplitude of the Cosine Harmonic Correction Term to the Angle of Inclination.
        
            Returns:
                the Amplitude of the Cosine Harmonic Correction Term to the Angle of Inclination (rad)
        
        
        """
        ...
    def getCis(self) -> float:
        """
            Gets the Amplitude of the Sine Harmonic Correction Term to the Angle of Inclination.
        
            Returns:
                the Amplitude of the Sine Harmonic Correction Term to the Angle of Inclination (rad)
        
        
        """
        ...
    def getCrc(self) -> float:
        """
            Gets the Amplitude of the Cosine Harmonic Correction Term to the Orbit Radius.
        
            Returns:
                the Amplitude of the Cosine Harmonic Correction Term to the Orbit Radius (m)
        
        
        """
        ...
    def getCrs(self) -> float:
        """
            Gets the Amplitude of the Sine Harmonic Correction Term to the Orbit Radius.
        
            Returns:
                the Amplitude of the Sine Harmonic Correction Term to the Orbit Radius (m)
        
        
        """
        ...
    def getCuc(self) -> float:
        """
            Gets the Amplitude of the Cosine Harmonic Correction Term to the Argument of Latitude.
        
            Returns:
                the Amplitude of the Cosine Harmonic Correction Term to the Argument of Latitude (rad)
        
        
        """
        ...
    def getCus(self) -> float:
        """
            Gets the Amplitude of the Sine Harmonic Correction Term to the Argument of Latitude.
        
            Returns:
                the Amplitude of the Sine Harmonic Correction Term to the Argument of Latitude (rad)
        
        
        """
        ...
    def getCycleDuration(self) -> float:
        """
            Gets the duration of the GNSS cycle in seconds.
        
            Returns:
                the duration of the GNSS cycle in seconds
        
        
        """
        ...
    def getE(self) -> float:
        """
            Gets the Eccentricity.
        
            Returns:
                the Eccentricity
        
        
        """
        ...
    def getI0(self) -> float:
        """
            Gets the Inclination Angle at Reference Time.
        
            Returns:
                the Inclination Angle at Reference Time (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Gets the Rate of Inclination Angle.
        
            Returns:
                the Rate of Inclination Angle (rad/s)
        
        
        """
        ...
    def getM0(self) -> float:
        """
            Gets the Mean Anomaly at Reference Time.
        
            Returns:
                the Mean Anomaly at Reference Time (rad)
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
            Gets the Mean Motion.
        
            Returns:
                the Mean Motion (rad/s)
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Gets the Earth's universal gravitational parameter.
        
            Returns:
                the Earth's universal gravitational parameter
        
        
        """
        ...
    def getOmega0(self) -> float:
        """
            Gets the Longitude of Ascending Node of Orbit Plane at Weekly Epoch.
        
            Returns:
                the Longitude of Ascending Node of Orbit Plane at Weekly Epoch (rad)
        
        
        """
        ...
    def getOmegaDot(self) -> float:
        """
            Gets the Rate of Right Ascension.
        
            Returns:
                the Rate of Right Ascension (rad/s)
        
        
        """
        ...
    def getPRN(self) -> int:
        """
            Gets the PRN number of the GNSS satellite.
        
            Returns:
                the PRN number of the GNSS satellite
        
        
        """
        ...
    def getPa(self) -> float:
        """
            Gets the Argument of Perigee.
        
            Returns:
                the Argument of Perigee (rad)
        
        
        """
        ...
    def getSma(self) -> float:
        """
            Gets the Semi-Major Axis.
        
            Returns:
                the Semi-Major Axis (m)
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Gets the Reference Time of the GNSS orbit as a duration from week start.
        
            Returns:
                the Reference Time of the GNSS orbit (s)
        
        
        """
        ...
    def getWeek(self) -> int:
        """
            Gets the Reference Week of the GNSS orbit.
        
            Returns:
                the Reference Week of the GNSS orbit within [0, 1024[
        
        
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
                the GLONASS ECEF-X component of satellite acceleration vector (m/sÂ²)
        
        
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
                the ECEF-Y component of satellite acceleration vector (m/sÂ²)
        
        
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
                the ECEF-Z component of satellite acceleration vector (m/sÂ²)
        
        
        """
        ...

class AbstractAlmanac(CommonGnssData):
    """
    public abstract class AbstractAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.CommonGnssData`
    
        Base class for GNSS almanacs.
    
        Since:
            11.0
    """
    def __init__(self, double: float, double2: float, int: int): ...
    def getAf2(self) -> float:
        """
            Getter for the Drift Rate Correction Coefficient.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the Drift Rate Correction Coefficient (s/sÂ²).
        
        
        """
        ...
    def getCic(self) -> float:
        """
            Getter for the Cic parameter.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the Cic parameter
        
        
        """
        ...
    def getCis(self) -> float:
        """
            Getter for the Cis parameter.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the Cis parameter
        
        
        """
        ...
    def getCrc(self) -> float:
        """
            Getter for the Crc parameter.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the Crc parameter
        
        
        """
        ...
    def getCrs(self) -> float:
        """
            Getter for the Crs parameter.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the Crs parameter
        
        
        """
        ...
    def getCuc(self) -> float:
        """
            Getter for the Cuc parameter.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the Cuc parameter
        
        
        """
        ...
    def getCus(self) -> float:
        """
            Getter for the Cus parameter.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the Cus parameter
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Getter for the rate of inclination angle.
        
            By default, not contained in a GNSS almanac
        
            Returns:
                the rate of inclination angle in rad/s
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
            Getter for the mean motion.
        
            Returns:
                the mean motion
        
        
        """
        ...

class AbstractNavigationMessage(CommonGnssData):
    """
    public abstract class AbstractNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.CommonGnssData`
    
        Base class for GNSS navigation messages.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage`,
            :class:`~org.orekit.propagation.analytical.gnss.data.IRNSSNavigationMessage`
    """
    def __init__(self, double: float, double2: float, int: int): ...
    def getAf2(self) -> float:
        """
            Getter for the Drift Rate Correction Coefficient.
        
            Returns:
                the Drift Rate Correction Coefficient (s/sÂ²).
        
        
        """
        ...
    def getCic(self) -> float:
        """
            Getter for the Cic parameter.
        
            Returns:
                the Cic parameter
        
        
        """
        ...
    def getCis(self) -> float:
        """
            Getter for the Cis parameter.
        
            Returns:
                the Cis parameter
        
        
        """
        ...
    def getCrc(self) -> float:
        """
            Getter for the Crc parameter.
        
            Returns:
                the Crc parameter
        
        
        """
        ...
    def getCrs(self) -> float:
        """
            Getter for the Crs parameter.
        
            Returns:
                the Crs parameter
        
        
        """
        ...
    def getCuc(self) -> float:
        """
            Getter for the Cuc parameter.
        
            Returns:
                the Cuc parameter
        
        
        """
        ...
    def getCus(self) -> float:
        """
            Getter for the Cus parameter.
        
            Returns:
                the Cus parameter
        
        
        """
        ...
    def getEpochToc(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for the time of clock epoch.
        
            Returns:
                the time of clock epoch
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Getter for the rate of inclination angle.
        
            Returns:
                the rate of inclination angle in rad/s
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
            Getter for the mean motion.
        
            Returns:
                the mean motion
        
        
        """
        ...
    def setAf2(self, double: float) -> None:
        """
            Setter for the Drift Rate Correction Coefficient (s/sÂ²).
        
            Parameters:
                af2 (double): the Drift Rate Correction Coefficient to set
        
        
        """
        ...
    def setCic(self, double: float) -> None:
        """
            Setter for te Cic parameter.
        
            Parameters:
                cic (double): the value to set
        
        
        """
        ...
    def setCis(self, double: float) -> None:
        """
            Setter for the Cis parameter.
        
            Parameters:
                cis (double): the value to sets
        
        
        """
        ...
    def setCrc(self, double: float) -> None:
        """
            Setter for the Crc parameter.
        
            Parameters:
                crc (double): the value to set
        
        
        """
        ...
    def setCrs(self, double: float) -> None:
        """
            Setter for the Crs parameter.
        
            Parameters:
                crs (double): the value to set
        
        
        """
        ...
    def setCuc(self, double: float) -> None:
        """
            Setter for the Cuc parameter.
        
            Parameters:
                cuc (double): the value to set
        
        
        """
        ...
    def setCus(self, double: float) -> None:
        """
            Setter for the Cus parameter.
        
            Parameters:
                cus (double): the value to set
        
        
        """
        ...
    def setDeltaN(self, double: float) -> None:
        """
            Setter for the delta of satellite mean motion.
        
            Parameters:
                deltaN (double): the value to set
        
        
        """
        ...
    def setEpochToc(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the time of clock epoch.
        
            Parameters:
                epochToc (:class:`~org.orekit.time.AbsoluteDate`): the epoch to set
        
        
        """
        ...
    def setIDot(self, double: float) -> None:
        """
            Setter for the Rate of Inclination Angle (rad/s).
        
            Parameters:
                iRate (double): the rate of inclination angle to set
        
        
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

class GLONASSAlmanac(GLONASSOrbitalElements):
    """
    public class GLONASSAlmanac extends Object implements :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
    
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
            interface:Â :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaI`
            Get the correction to the mean value of inclination.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaI`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the correction to the mean value of inclination (rad)
        
        
        """
        ...
    def getDeltaT(self) -> float:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaT`
            Get the correction to the mean value of Draconian period.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaT`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the correction to the mean value of Draconian period (s)
        
        
        """
        ...
    def getDeltaTDot(self) -> float:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaTDot`
            Get the rate of change of Draconian period.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getDeltaTDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the rate of change of Draconian period
        
        
        """
        ...
    def getE(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getE`
            Get the Eccentricity.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getE`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
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
            interface:Â :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getLambda`
            Get the longitude of ascending node of orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getLambda`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the longitude of ascending node of orbit (rad)
        
        
        """
        ...
    def getN4(self) -> int:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getN4`
            Get the number of the current four year interval.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getN4`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current four year interval
        
        
        """
        ...
    def getNa(self) -> int:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa`
            Get the number of the current day in a four year interval.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current day in a four year interval
        
        
        """
        ...
    def getPa(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getPa`
            Get the Argument of Perigee.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getPa`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Argument of Perigee (rad)
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime`
            Get the Reference Time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Reference Time (s)
        
        
        """
        ...

class GLONASSEphemeris(GLONASSOrbitalElements):
    """
    public class GLONASSEphemeris extends Object implements :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
    
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
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getN4`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current four year interval
        
        
        """
        ...
    def getNa(self) -> int:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa`
            Get the number of the current day in a four year interval.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getNa`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the number of the current day in a four year interval
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime`
            Get the Reference Time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Reference Time (s)
        
        
        """
        ...
    def getX(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getX`
            Get the ECEF-X component of satellite coordinates in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getX`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-X component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getXDot(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDot`
            Get the ECEF-X component of satellite velocity vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the the ECEF-X component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getXDotDot(self) -> float:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDotDot`
            Get the GLONASS ECEF-X component of satellite acceleration vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDotDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the GLONASS ECEF-X component of satellite acceleration vector in PZ-90 datum (m/sÂ²)
        
        
        """
        ...
    def getY(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getY`
            Get the ECEF-Y component of satellite coordinates in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getY`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-Y component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getYDot(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDot`
            Get the ECEF-Y component of satellite velocity vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-Y component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getYDotDot(self) -> float:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDotDot`
            Get the GLONASS ECEF-Y component of satellite acceleration vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDotDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the GLONASS ECEF-Y component of satellite acceleration vector in PZ-90 datum (m/sÂ²)
        
        
        """
        ...
    def getZ(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZ`
            Get the ECEF-Z component of satellite coordinates in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZ`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the ECEF-Z component of satellite coordinates in PZ-90 datum (m)
        
        
        """
        ...
    def getZDot(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDot`
            Get the ECEF-Z component of satellite velocity vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the the ECEF-Z component of satellite velocity vector in PZ-90 datum (m/s)
        
        
        """
        ...
    def getZDotDot(self) -> float:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDotDot`
            Get the GLONASS ECEF-Z component of satellite acceleration vector in PZ-90 datum.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDotDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the GLONASS ECEF-Z component of satellite acceleration vector in PZ-90 datum (m/sÂ²)
        
        
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
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getGammaN`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the relative deviation of predicted satellite carrier frequency from nominal value
        
        
        """
        ...
    def getTN(self) -> float:
        """
            Get the correction to the satellite time relative to GLONASS system time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTN`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the correction to the satellite time relative to GLONASS system time (s)
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Get the Reference Time.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getTime`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`
        
            Returns:
                the Reference Time (s)
        
        
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

class PythonSBASOrbitalElements(SBASOrbitalElements):
    """
    public class PythonSBASOrbitalElements extends Object implements :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAGf0(self) -> float:
        """
            Gets the Zeroth Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getAGf0`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
        
        """
        ...
    def getAGf1(self) -> float:
        """
            Gets the First Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getAGf1`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the First Order Clock Correction (s/s)
        
        
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
    def getIODN(self) -> int:
        """
            Gets the Issue Of Data Navigation (IODN).
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getIODN`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the IODN
        
        
        """
        ...
    def getPRN(self) -> int:
        """
            Gets the PRN number of the SBAS satellite.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getPRN`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the PRN number of the SBAS satellite
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Gets the Reference Time of the SBAS orbit in GPS seconds of the week.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getTime`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the Reference Time of the SBAS orbit (s)
        
        
        """
        ...
    def getToc(self) -> float:
        """
            Gets the clock correction reference time toc.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getToc`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the clock correction reference time (s)
        
        
        """
        ...
    def getWeek(self) -> int:
        """
            Gets the Reference Week of the SBAS orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getWeek`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the Reference Week of the SBAS orbit
        
        
        """
        ...
    def getX(self) -> float:
        """
            Get the ECEF-X component of satellite coordinates.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getX`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the ECEF-X component of satellite coordinates (m)
        
        
        """
        ...
    def getXDot(self) -> float:
        """
            Get the ECEF-X component of satellite velocity vector.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getXDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the the ECEF-X component of satellite velocity vector (m/s)
        
        
        """
        ...
    def getXDotDot(self) -> float:
        """
            Get the ECEF-X component of satellite acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getXDotDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the GLONASS ECEF-X component of satellite acceleration vector (m/sÂ²)
        
        
        """
        ...
    def getY(self) -> float:
        """
            Get the ECEF-Y component of satellite coordinates.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getY`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the ECEF-Y component of satellite coordinates (m)
        
        
        """
        ...
    def getYDot(self) -> float:
        """
            Get the ECEF-Y component of satellite velocity vector.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getYDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the ECEF-Y component of satellite velocity vector (m/s)
        
        
        """
        ...
    def getYDotDot(self) -> float:
        """
            Get the ECEF-Y component of satellite acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getYDotDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the ECEF-Y component of satellite acceleration vector (m/sÂ²)
        
        
        """
        ...
    def getZ(self) -> float:
        """
            Get the ECEF-Z component of satellite coordinates.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getZ`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the ECEF-Z component of satellite coordinates (m)
        
        
        """
        ...
    def getZDot(self) -> float:
        """
            Get the ECEF-Z component of satellite velocity vector.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getZDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the the ECEF-Z component of satellite velocity vector (m/s)
        
        
        """
        ...
    def getZDotDot(self) -> float:
        """
            Get the ECEF-Z component of satellite acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getZDotDot`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the ECEF-Z component of satellite acceleration vector (m/sÂ²)
        
        
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
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getAGf0`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the Zeroth Order Clock Correction (s)
        
        
        """
        ...
    def getAGf1(self) -> float:
        """
            Gets the First Order Clock Correction.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getAGf1`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the First Order Clock Correction (s/s)
        
        
        """
        ...
    def getIODN(self) -> int:
        """
            Gets the Issue Of Data Navigation (IODN).
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getIODN`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
            Returns:
                the IODN
        
        
        """
        ...
    def getTime(self) -> float:
        """
            Gets the Reference Time of the SBAS orbit in GPS seconds of the week.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getTime`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
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
                :meth:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements.getWeek`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`
        
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

class BeidouAlmanac(AbstractAlmanac, GNSSOrbitalElements):
    """
    public class BeidouAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        Class for BeiDou almanac.
    
        Since:
            10.0
    
        Also see:
            "BeiDou Navigation Satellite System, Signal In Space, Interface Control Document, Version 2.1, Table 5-12"
    """
    def __init__(self): ...
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
            Sets the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (double): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...

class BeidouNavigationMessage(AbstractNavigationMessage, GNSSOrbitalElements):
    """
    public class BeidouNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        Container for data contained in a BeiDou navigation message.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
            Setter for the age of data ephemeric.
        
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

class GPSAlmanac(AbstractAlmanac, GNSSOrbitalElements, GNSSClockElements):
    """
    public class GPSAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`, :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
    
        This class holds a GPS almanac as read from SEM or YUMA files.
    
        Depending on the source (SEM or YUMA), some fields may be filled in or not. An almanac read from a YUMA file doesn't
        hold SVN number, average URA and satellite configuration.
    
        Since:
            8.0
    """
    def __init__(self): ...
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
    def getTGD(self) -> float:
        """
            Gets for the Group Delay Differential (s).
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getTGD`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
        
            Returns:
                the Group Delay Differential in seconds
        
        
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
                source (String): the source of this GPS almanac
        
        
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

class GPSNavigationMessage(AbstractNavigationMessage, GNSSOrbitalElements, GNSSClockElements):
    """
    public class GPSNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`, :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
    
        Container for data contained in a GPS navigation message.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
    def getSvHealth(self) -> float:
        """
            Getter for the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def getTGD(self) -> float:
        """
            Getter for the Group Delay Differential (s).
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getTGD`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements`
        
            Returns:
                the Group Delay Differential in seconds
        
        
        """
        ...
    def setIODC(self, double: float) -> None:
        """
            Setter for the Issue of Data Clock.
        
            Parameters:
                value (double): the IODC to set
        
        
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
    def setSvHealth(self, double: float) -> None:
        """
            Setter for the satellite health status.
        
            Parameters:
                svHealth (double): the value to set
        
        
        """
        ...
    def setTGD(self, double: float) -> None:
        """
            Setter for the Group Delay Differential (s).
        
            Parameters:
                time (double): the group delay differential to set
        
        
        """
        ...

class GalileoAlmanac(AbstractAlmanac, GNSSOrbitalElements):
    """
    public class GalileoAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        Class for Galileo almanac.
    
        Since:
            10.0
    
        Also see:
            "European GNSS (Galileo) Open Service, Signal In Space, Interface Control Document, Table 75"
    """
    def __init__(self): ...
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

class GalileoNavigationMessage(AbstractNavigationMessage, GNSSOrbitalElements):
    """
    public class GalileoNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        Container for data contained in a Galileo navigation message.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
    def setIODNav(self, double: float) -> None:
        """
            Setter for the Issue of Data of the navigation batch.
        
            Parameters:
                iod (double): the IOD to set
        
        
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

class IRNSSAlmanac(AbstractAlmanac, GNSSOrbitalElements):
    """
    public class IRNSSAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        Class for IRNSS almanac.
    
        Since:
            10.1
    
        Also see:
            "Indian Regiona Navigation Satellite System, Signal In Space ICD for standard positioning service, version 1.1 - Table
            28"
    """
    def __init__(self): ...
    def setSqrtA(self, double: float) -> None:
        """
            Setter for the Square Root of Semi-Major Axis (m^1/2).
        
            In addition, this method set the value of the Semi-Major Axis.
        
            Parameters:
                sqrtA (double): the Square Root of Semi-Major Axis (m^1/2)
        
        
        """
        ...

class IRNSSNavigationMessage(AbstractNavigationMessage, GNSSOrbitalElements):
    """
    public class IRNSSNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        Container for data contained in an IRNSS navigation message.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getIODEC(self) -> int:
        """
            Getter for the Issue Of Data Ephemeris and Clock (IODEC).
        
            Returns:
                the Issue Of Data Ephemeris and Clock (IODEC)
        
        
        """
        ...
    def getSvHealth(self) -> float:
        """
            Getter for the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def getTGD(self) -> float:
        """
            Getter for the estimated group delay differential TGD for L5-S correction.
        
            Returns:
                the estimated group delay differential TGD for L5-S correction (s)
        
        
        """
        ...
    def getURA(self) -> float:
        """
            Getter for the user range accuray (meters).
        
            Returns:
                the user range accuracy
        
        
        """
        ...
    def setIODEC(self, double: float) -> None:
        """
            Setter for the Issue of Data, Ephemeris and Clock.
        
            Parameters:
                value (double): the IODEC to set
        
        
        """
        ...
    def setSvHealth(self, double: float) -> None:
        """
            Setter for the satellite health status.
        
            Parameters:
                svHealth (double): the value to set
        
        
        """
        ...
    def setTGD(self, double: float) -> None:
        """
            Setter for the Group Delay Differential (s).
        
            Parameters:
                time (double): the group delay differential to set
        
        
        """
        ...
    def setURA(self, double: float) -> None:
        """
            Setter for the user range accuracy.
        
            Parameters:
                accuracy (double): the value to set
        
        
        """
        ...

class QZSSAlmanac(AbstractAlmanac, GNSSOrbitalElements):
    """
    public class QZSSAlmanac extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractAlmanac` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        This class holds a QZSS almanac as read from YUMA files.
    
        Since:
            10.0
    """
    def __init__(self): ...
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
                source (String): the source of this GPS almanac
        
        
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

class QZSSNavigationMessage(AbstractNavigationMessage, GNSSOrbitalElements):
    """
    public class QZSSNavigationMessage extends :class:`~org.orekit.propagation.analytical.gnss.data.AbstractNavigationMessage` implements :class:`~org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements`
    
        Container for data contained in a QZSS navigation message.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
    def getSvHealth(self) -> float:
        """
            Getter for the satellite health status.
        
            Returns:
                the satellite health status
        
        
        """
        ...
    def getTGD(self) -> float:
        """
            Getter for the Group Delay Differential (s).
        
            Returns:
                the Group Delay Differential in seconds
        
        
        """
        ...
    def setIODC(self, double: float) -> None:
        """
            Setter for the Issue of Data, Clock.
        
            Parameters:
                value (double): the IODC to set
        
        
        """
        ...
    def setIODE(self, double: float) -> None:
        """
            Setter for the Issue of Data, Ephemeris.
        
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
    def setSvHealth(self, double: float) -> None:
        """
            Setter for the satellite health status.
        
            Parameters:
                svHealth (double): the value to set
        
        
        """
        ...
    def setTGD(self, double: float) -> None:
        """
            Setter for the Group Delay Differential (s).
        
            Parameters:
                time (double): the group delay differential to set
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.gnss.data")``.

    AbstractAlmanac: typing.Type[AbstractAlmanac]
    AbstractEphemerisMessage: typing.Type[AbstractEphemerisMessage]
    AbstractNavigationMessage: typing.Type[AbstractNavigationMessage]
    BeidouAlmanac: typing.Type[BeidouAlmanac]
    BeidouNavigationMessage: typing.Type[BeidouNavigationMessage]
    CommonGnssData: typing.Type[CommonGnssData]
    GLONASSAlmanac: typing.Type[GLONASSAlmanac]
    GLONASSEphemeris: typing.Type[GLONASSEphemeris]
    GLONASSNavigationMessage: typing.Type[GLONASSNavigationMessage]
    GLONASSOrbitalElements: typing.Type[GLONASSOrbitalElements]
    GNSSClockElements: typing.Type[GNSSClockElements]
    GNSSConstants: typing.Type[GNSSConstants]
    GNSSOrbitalElements: typing.Type[GNSSOrbitalElements]
    GPSAlmanac: typing.Type[GPSAlmanac]
    GPSNavigationMessage: typing.Type[GPSNavigationMessage]
    GalileoAlmanac: typing.Type[GalileoAlmanac]
    GalileoNavigationMessage: typing.Type[GalileoNavigationMessage]
    IRNSSAlmanac: typing.Type[IRNSSAlmanac]
    IRNSSNavigationMessage: typing.Type[IRNSSNavigationMessage]
    PythonSBASOrbitalElements: typing.Type[PythonSBASOrbitalElements]
    QZSSAlmanac: typing.Type[QZSSAlmanac]
    QZSSNavigationMessage: typing.Type[QZSSNavigationMessage]
    SBASNavigationMessage: typing.Type[SBASNavigationMessage]
    SBASOrbitalElements: typing.Type[SBASOrbitalElements]
