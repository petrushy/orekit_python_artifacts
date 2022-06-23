import java.io
import java.util
import org
import org.hipparchus
import org.hipparchus.linear
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.integration
import org.orekit.time
import org.orekit.utils
import typing



_FieldTLE__T = typing.TypeVar('_FieldTLE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTLE(org.orekit.time.FieldTimeStamped[_FieldTLE__T], java.io.Serializable, typing.Generic[_FieldTLE__T]):
    """
    public class FieldTLE<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.time.FieldTimeStamped`<T>, Serializable
    
        This class is a container for a single set of TLE data.
    
        TLE sets can be built either by providing directly the two lines, in which case parsing is performed internally or by
        providing the already parsed elements.
    
        TLE are not transparently convertible to :class:`~org.orekit.orbits.Orbit` instances. They are significant only with
        respect to their dedicated :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`, which also computes position
        and velocity coordinates. Any attempt to directly use orbital parameters like
        :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.getE`,
        :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.getI`, etc. without any reference to the
        :class:`~org.orekit.propagation.analytical.tle.TLEPropagator` is prone to errors.
    
        More information on the TLE format can be found on the CelesTrak website.
    
        Since:
            11.0
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT
    
        Identifier for default type of ephemeris (SGP4/SDP4).
    
        Also see:
            :meth:`~constant`
    
    
    """
    SGP: typing.ClassVar[int] = ...
    """
    public static final int SGP
    
        Identifier for SGP type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SGP4: typing.ClassVar[int] = ...
    """
    public static final int SGP4
    
        Identifier for SGP4 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SDP4: typing.ClassVar[int] = ...
    """
    public static final int SDP4
    
        Identifier for SDP4 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SGP8: typing.ClassVar[int] = ...
    """
    public static final int SGP8
    
        Identifier for SGP8 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SDP8: typing.ClassVar[int] = ...
    """
    public static final int SDP8
    
        Identifier for SDP8 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    B_STAR: typing.ClassVar[str] = ...
    """
    public static final String B_STAR
    
        Parameter name for B* coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLE__T], t: _FieldTLE__T, t2: _FieldTLE__T, t3: _FieldTLE__T, t4: _FieldTLE__T, t5: _FieldTLE__T, t6: _FieldTLE__T, t7: _FieldTLE__T, t8: _FieldTLE__T, int6: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLE__T], t: _FieldTLE__T, t2: _FieldTLE__T, t3: _FieldTLE__T, t4: _FieldTLE__T, t5: _FieldTLE__T, t6: _FieldTLE__T, t7: _FieldTLE__T, t8: _FieldTLE__T, int6: int, double: float, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTLE__T], string: str, string2: str): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTLE__T], string: str, string2: str, timeScale: org.orekit.time.TimeScale): ...
    def equals(self, object: typing.Any) -> bool:
        """
            Check if this tle equals the provided tle.
        
            Due to the difference in precision between object and string representations of TLE, it is possible for this method to
            return false even if string representations returned by :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.toString`
            are equal.
        
            Overrides:
                 in class 
        
            Parameters:
                o (Object): other tle
        
            Returns:
                true if this tle equals the provided tle
        
        
        """
        ...
    def getBStar(self) -> float:
        """
            Get the ballistic coefficient.
        
            Returns:
                bStar
        
        
        """
        ...
    def getClassification(self) -> str:
        """
            Get the classification.
        
            Returns:
                classification
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTLE__T]: ...
    def getE(self) -> _FieldTLE__T:
        """
            Get the eccentricity.
        
            Returns:
                the eccentricity
        
        
        """
        ...
    def getElementNumber(self) -> int:
        """
            Get the element number.
        
            Returns:
                the element number
        
        
        """
        ...
    def getEphemerisType(self) -> int:
        """
            Get the type of ephemeris.
        
            Returns:
                the ephemeris type (one of :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.DEFAULT`,
                :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.SGP`,
                :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.SGP4`,
                :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.SGP8`,
                :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.SDP4`,
                :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.SDP8`)
        
        
        """
        ...
    def getI(self) -> _FieldTLE__T:
        """
            Get the inclination.
        
            Returns:
                the inclination (rad)
        
        
        """
        ...
    def getLaunchNumber(self) -> int:
        """
            Get the launch number.
        
            Returns:
                the launch number
        
        
        """
        ...
    def getLaunchPiece(self) -> str:
        """
            Get the launch piece.
        
            Returns:
                the launch piece
        
        
        """
        ...
    def getLaunchYear(self) -> int:
        """
            Get the launch year.
        
            Returns:
                the launch year
        
        
        """
        ...
    def getLine1(self) -> str:
        """
            Get the first line.
        
            Returns:
                first line
        
        
        """
        ...
    def getLine2(self) -> str:
        """
            Get the second line.
        
            Returns:
                second line
        
        
        """
        ...
    def getMeanAnomaly(self) -> _FieldTLE__T:
        """
            Get the mean anomaly.
        
            Returns:
                the mean anomaly (rad)
        
        
        """
        ...
    def getMeanMotion(self) -> _FieldTLE__T:
        """
            Get the mean motion.
        
            Returns:
                the mean motion (rad/s)
        
        
        """
        ...
    def getMeanMotionFirstDerivative(self) -> _FieldTLE__T:
        """
            Get the mean motion first derivative.
        
            Returns:
                the mean motion first derivative (rad/sÂ²)
        
        
        """
        ...
    def getMeanMotionSecondDerivative(self) -> _FieldTLE__T:
        """
            Get the mean motion second derivative.
        
            Returns:
                the mean motion second derivative (rad/sÂ³)
        
        
        """
        ...
    def getParameters(self, field: org.hipparchus.Field[_FieldTLE__T]) -> typing.List[_FieldTLE__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPerigeeArgument(self) -> _FieldTLE__T:
        """
            Get the argument of perigee.
        
            Returns:
                omega (rad)
        
        
        """
        ...
    def getRaan(self) -> _FieldTLE__T:
        """
            Get Right Ascension of the Ascending node.
        
            Returns:
                the raan (rad)
        
        
        """
        ...
    def getRevolutionNumberAtEpoch(self) -> int:
        """
            Get the revolution number.
        
            Returns:
                the revolutionNumberAtEpoch
        
        
        """
        ...
    def getSatelliteNumber(self) -> int:
        """
            Get the satellite id.
        
            Returns:
                the satellite number
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashcode for this tle.
        
            Overrides:
                 in class 
        
            Returns:
                hashcode
        
        
        """
        ...
    @staticmethod
    def isFormatOK(string: str, string2: str) -> bool:
        """
            Check the lines format validity.
        
            Parameters:
                line1 (String): the first element
                line2 (String): the second element
        
            Returns:
                true if format is recognized (non null lines, 69 characters length, line content), false if not
        
        
        """
        ...
    _stateToTLE_0__T = typing.TypeVar('_stateToTLE_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _stateToTLE_1__T = typing.TypeVar('_stateToTLE_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _stateToTLE_2__T = typing.TypeVar('_stateToTLE_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def stateToTLE(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_stateToTLE_0__T], fieldTLE: 'FieldTLE'[_stateToTLE_0__T]) -> 'FieldTLE'[_stateToTLE_0__T]: ...
    @typing.overload
    @staticmethod
    def stateToTLE(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_stateToTLE_1__T], fieldTLE: 'FieldTLE'[_stateToTLE_1__T], timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame) -> 'FieldTLE'[_stateToTLE_1__T]:
        """
            Convert Spacecraft State into TLE. This converter uses Newton method to reverse SGP4 and SDP4 propagation algorithm and
            generates a usable TLE version of a state. New TLE epoch is state epoch.
        
            This method uses :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.EPSILON_DEFAULT` and
            :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.MAX_ITERATIONS_DEFAULT` for method convergence.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): Spacecraft State to convert into TLE
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> templateTLE): first guess used to get identification and estimate new TLE
                utc (:class:`~org.orekit.time.TimeScale`): the UTC time scale
                teme (:class:`~org.orekit.frames.Frame`): the TEME frame to use for propagation
        
            Returns:
                TLE matching with Spacecraft State and template identification
        
            Since:
                11.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.stateToTLE`
        
            Convert Spacecraft State into TLE. This converter uses Newton method to reverse SGP4 and SDP4 propagation algorithm and
            generates a usable TLE version of a state. New TLE epoch is state epoch.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): Spacecraft State to convert into TLE
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> templateTLE): first guess used to get identification and estimate new TLE
                utc (:class:`~org.orekit.time.TimeScale`): the UTC time scale
                teme (:class:`~org.orekit.frames.Frame`): the TEME frame to use for propagation
                epsilon (double): used to compute threshold for convergence check
                maxIterations (int): maximum number of iterations for convergence
        
            Returns:
                TLE matching with Spacecraft State and template identification
        
            Since:
                11.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def stateToTLE(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_stateToTLE_2__T], fieldTLE: 'FieldTLE'[_stateToTLE_2__T], timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame, double: float, int: int) -> 'FieldTLE'[_stateToTLE_2__T]: ...
    def toString(self) -> str:
        """
            Get a string representation of this TLE set.
        
            The representation is simply the two lines separated by the platform line separator.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of this TLE set
        
        
        """
        ...
    def toTLE(self) -> 'TLE':
        """
            Convert FieldTLE into TLE.
        
            Returns:
                TLE
        
        
        """
        ...

_FieldTLEPropagator__T = typing.TypeVar('_FieldTLEPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTLEPropagator(org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator[_FieldTLEPropagator__T], typing.Generic[_FieldTLEPropagator__T]):
    """
    public abstract class FieldTLEPropagator<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator`<T>
    
        This class provides elements to propagate TLE's.
    
        The models used are SGP4 and SDP4, initially proposed by NORAD as the unique convenient propagator for TLE's. Inputs and
        outputs of this propagator are only suited for NORAD two lines elements sets, since it uses estimations and mean values
        appropriate for TLE's only.
    
        Deep- or near- space propagator is selected internally according to NORAD recommendations so that the user has not to
        worry about the used computation methods. One instance is created for each TLE (this instance can only be get using null
        method, and can compute :class:`~org.orekit.utils.PVCoordinates` at any time. Maximum accuracy is guaranteed in a 24h
        range period before and after the provided TLE epoch (of course this accuracy is not really measurable nor predictable:
        according to CelesTrak, the precision is close to one kilometer and error won't probably rise above 2 km).
    
        This implementation is largely inspired from the paper and source code Revisiting Spacetrack Report #3 and is fully
        compliant with its results and tests cases.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.propagation.analytical.tle.FieldTLE`
    """
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getFrame` in interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.FieldAbstractPropagator.getFrame`Â in
                classÂ :class:`~org.orekit.propagation.FieldAbstractPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.resetInitialState`
        
        
        """
        ...
    @staticmethod
    def getMU() -> float:
        """
            Get the Earth gravity coefficient used for TLE propagation.
        
            Returns:
                the Earth gravity coefficient.
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], tArray: typing.List[_FieldTLEPropagator__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldTLEPropagator__T]: ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTLEPropagator__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTLE(self) -> FieldTLE[_FieldTLEPropagator__T]: ...
    def propagateOrbit(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], tArray: typing.List[_FieldTLEPropagator__T]) -> org.orekit.orbits.FieldOrbit[_FieldTLEPropagator__T]: ...
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldTLEPropagator__T]) -> None: ...
    _selectExtrapolator_0__T = typing.TypeVar('_selectExtrapolator_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_1__T = typing.TypeVar('_selectExtrapolator_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_2__T = typing.TypeVar('_selectExtrapolator_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_3__T = typing.TypeVar('_selectExtrapolator_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_0__T], tArray: typing.List[_selectExtrapolator_0__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_0__T]:
        """
            Selects the extrapolator to use with the selected TLE.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                tle (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> tle): the TLE to propagate.
                frames (:class:`~org.orekit.frames.Frames`): set of Frames to use in the propagator.
                parameters (T[]): SGP4 and SDP4 model parameters
        
            Returns:
                the correct propagator.
        
        :class:`~org.orekit.annotation.DefaultDataContext` public static <T extends CalculusFieldElement<T>> :class:`~org.orekit.propagation.analytical.tle.FieldTLEPropagator`<T> selectExtrapolator(:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> tle, :class:`~org.orekit.attitudes.AttitudeProvider` attitudeProvider, T mass, T[] parameters)
        
            Selects the extrapolator to use with the selected TLE.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                tle (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> tle): the TLE to propagate.
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): provider for attitude computation
                mass (T): spacecraft mass (kg)
                parameters (T[]): SGP4 and SDP4 model parameters
        
            Returns:
                the correct propagator.
        
            Also see:
        
            Selects the extrapolator to use with the selected TLE.
        
            Parameters:
                tle (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> tle): the TLE to propagate.
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): provider for attitude computation
                mass (T): spacecraft mass (kg)
                teme (:class:`~org.orekit.frames.Frame`): the TEME frame to use for propagation.
                parameters (T[]): SGP4 and SDP4 model parameters
        
            Returns:
                the correct propagator.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_1__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _selectExtrapolator_1__T, tArray: typing.List[_selectExtrapolator_1__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_1__T]: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_2__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _selectExtrapolator_2__T, frame: org.orekit.frames.Frame, tArray: typing.List[_selectExtrapolator_2__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_2__T]: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_3__T], frames: org.orekit.frames.Frames, tArray: typing.List[_selectExtrapolator_3__T]) -> 'FieldTLEPropagator'[_selectExtrapolator_3__T]: ...

class TLE(org.orekit.time.TimeStamped, java.io.Serializable):
    """
    public class TLE extends Object implements :class:`~org.orekit.time.TimeStamped`, Serializable
    
        This class is a container for a single set of TLE data.
    
        TLE sets can be built either by providing directly the two lines, in which case parsing is performed internally or by
        providing the already parsed elements.
    
        TLE are not transparently convertible to :class:`~org.orekit.orbits.Orbit` instances. They are significant only with
        respect to their dedicated :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`, which also computes position
        and velocity coordinates. Any attempt to directly use orbital parameters like
        :meth:`~org.orekit.propagation.analytical.tle.TLE.getE`, :meth:`~org.orekit.propagation.analytical.tle.TLE.getI`, etc.
        without any reference to the :class:`~org.orekit.propagation.analytical.tle.TLEPropagator` is prone to errors.
    
        More information on the TLE format can be found on the CelesTrak website.
    
        Also see:
            :meth:`~serialized`
    """
    SGP: typing.ClassVar[int] = ...
    """
    public static final int SGP
    
        Identifier for SGP type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SGP4: typing.ClassVar[int] = ...
    """
    public static final int SGP4
    
        Identifier for SGP4 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SDP4: typing.ClassVar[int] = ...
    """
    public static final int SDP4
    
        Identifier for SDP4 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SGP8: typing.ClassVar[int] = ...
    """
    public static final int SGP8
    
        Identifier for SGP8 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SDP8: typing.ClassVar[int] = ...
    """
    public static final int SDP8
    
        Identifier for SDP8 type of ephemeris.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT
    
        Identifier for default type of ephemeris (SGP4/SDP4).
    
        Also see:
            :meth:`~constant`
    
    
    """
    B_STAR: typing.ClassVar[str] = ...
    """
    public static final String B_STAR
    
        Parameter name for B* coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int6: int, double9: float): ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int6: int, double9: float, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, timeScale: org.orekit.time.TimeScale): ...
    def equals(self, object: typing.Any) -> bool:
        """
            Check if this tle equals the provided tle.
        
            Due to the difference in precision between object and string representations of TLE, it is possible for this method to
            return false even if string representations returned by :meth:`~org.orekit.propagation.analytical.tle.TLE.toString` are
            equal.
        
            Overrides:
                 in class 
        
            Parameters:
                o (Object): other tle
        
            Returns:
                true if this tle equals the provided tle
        
        
        """
        ...
    def getBStar(self) -> float:
        """
            Get the ballistic coefficient.
        
            Returns:
                bStar
        
        
        """
        ...
    def getClassification(self) -> str:
        """
            Get the classification.
        
            Returns:
                classification
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the TLE current date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                the epoch
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Returns:
                the eccentricity
        
        
        """
        ...
    def getElementNumber(self) -> int:
        """
            Get the element number.
        
            Returns:
                the element number
        
        
        """
        ...
    def getEphemerisType(self) -> int:
        """
            Get the type of ephemeris.
        
            Returns:
                the ephemeris type (one of :meth:`~org.orekit.propagation.analytical.tle.TLE.DEFAULT`,
                :meth:`~org.orekit.propagation.analytical.tle.TLE.SGP`, :meth:`~org.orekit.propagation.analytical.tle.TLE.SGP4`,
                :meth:`~org.orekit.propagation.analytical.tle.TLE.SGP8`, :meth:`~org.orekit.propagation.analytical.tle.TLE.SDP4`,
                :meth:`~org.orekit.propagation.analytical.tle.TLE.SDP8`)
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Returns:
                the inclination (rad)
        
        
        """
        ...
    def getLaunchNumber(self) -> int:
        """
            Get the launch number.
        
            Returns:
                the launch number
        
        
        """
        ...
    def getLaunchPiece(self) -> str:
        """
            Get the launch piece.
        
            Returns:
                the launch piece
        
        
        """
        ...
    def getLaunchYear(self) -> int:
        """
            Get the launch year.
        
            Returns:
                the launch year
        
        
        """
        ...
    def getLine1(self) -> str:
        """
            Get the first line.
        
            Returns:
                first line
        
        
        """
        ...
    def getLine2(self) -> str:
        """
            Get the second line.
        
            Returns:
                second line
        
        
        """
        ...
    def getMeanAnomaly(self) -> float:
        """
            Get the mean anomaly.
        
            Returns:
                the mean anomaly (rad)
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
            Get the mean motion.
        
            Returns:
                the mean motion (rad/s)
        
        
        """
        ...
    def getMeanMotionFirstDerivative(self) -> float:
        """
            Get the mean motion first derivative.
        
            Returns:
                the mean motion first derivative (rad/sÂ²)
        
        
        """
        ...
    def getMeanMotionSecondDerivative(self) -> float:
        """
            Get the mean motion second derivative.
        
            Returns:
                the mean motion second derivative (rad/sÂ³)
        
        
        """
        ...
    def getParameterDriver(self, string: str) -> org.orekit.utils.ParameterDriver:
        """
            Get parameter driver from its name.
        
            Parameters:
                name (String): parameter name
        
            Returns:
                parameter driver
        
            Since:
                11.1
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPerigeeArgument(self) -> float:
        """
            Get the argument of perigee.
        
            Returns:
                omega (rad)
        
        
        """
        ...
    def getRaan(self) -> float:
        """
            Get Right Ascension of the Ascending node.
        
            Returns:
                the raan (rad)
        
        
        """
        ...
    def getRevolutionNumberAtEpoch(self) -> int:
        """
            Get the revolution number.
        
            Returns:
                the revolutionNumberAtEpoch
        
        
        """
        ...
    def getSatelliteNumber(self) -> int:
        """
            Get the satellite id.
        
            Returns:
                the satellite number
        
        
        """
        ...
    def getUtc(self) -> org.orekit.time.TimeScale:
        """
            Get the UTC time scale used to create this TLE.
        
            Returns:
                UTC time scale.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashcode for this tle.
        
            Overrides:
                 in class 
        
            Returns:
                hashcode
        
        
        """
        ...
    @staticmethod
    def isFormatOK(string: str, string2: str) -> bool:
        """
            Check the lines format validity.
        
            Parameters:
                line1 (String): the first element
                line2 (String): the second element
        
            Returns:
                true if format is recognized (non null lines, 69 characters length, line content), false if not
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def stateToTLE(spacecraftState: org.orekit.propagation.SpacecraftState, tLE: 'TLE') -> 'TLE':
        """
            Convert Spacecraft State into TLE. This converter uses Fixed Point method to reverse SGP4 and SDP4 propagation algorithm
            and generates a usable TLE version of a state. Equinocital orbital parameters are used in order to get a stiff method.
            New TLE epoch is state epoch.
        
            This method uses :meth:`~org.orekit.propagation.analytical.tle.TLE.EPSILON_DEFAULT` and
            :meth:`~org.orekit.propagation.analytical.tle.TLE.MAX_ITERATIONS_DEFAULT` for method convergence.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): Spacecraft State to convert into TLE
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.TLE`): first guess used to get identification and estimate new TLE
                utc (:class:`~org.orekit.time.TimeScale`): the UTC time scale
                teme (:class:`~org.orekit.frames.Frame`): the TEME frame to use for propagation
        
            Returns:
                TLE matching with Spacecraft State and template identification
        
            Since:
                11.0
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.tle.TLE.stateToTLE`
        
            Convert Spacecraft State into TLE. This converter uses Newton method to reverse SGP4 and SDP4 propagation algorithm and
            generates a usable TLE version of a state. New TLE epoch is state epoch.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): Spacecraft State to convert into TLE
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.TLE`): first guess used to get identification and estimate new TLE
                utc (:class:`~org.orekit.time.TimeScale`): the UTC time scale
                teme (:class:`~org.orekit.frames.Frame`): the TEME frame to use for propagation
                epsilon (double): used to compute threshold for convergence check
                maxIterations (int): maximum number of iterations for convergence
        
            Returns:
                TLE matching with Spacecraft State and template identification
        
            Since:
                11.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def stateToTLE(spacecraftState: org.orekit.propagation.SpacecraftState, tLE: 'TLE', timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame) -> 'TLE': ...
    @typing.overload
    @staticmethod
    def stateToTLE(spacecraftState: org.orekit.propagation.SpacecraftState, tLE: 'TLE', timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame, double: float, int: int) -> 'TLE': ...
    def toString(self) -> str:
        """
            Get a string representation of this TLE set.
        
            The representation is simply the two lines separated by the platform line separator.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of this TLE set
        
        
        """
        ...

class TLEConstants:
    """
    public class TLEConstants extends Object
    
        Constants necessary to TLE propagation. This constants are used in the WGS-72 model, compliant with NORAD
        implementations.
    """
    ONE_THIRD: typing.ClassVar[float] = ...
    """
    public static final double ONE_THIRD
    
        Constant 1.0 / 3.0.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TWO_THIRD: typing.ClassVar[float] = ...
    """
    public static final double TWO_THIRD
    
        Constant 2.0 / 3.0.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EARTH_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double EARTH_RADIUS
    
        Earth radius in km.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NORMALIZED_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double NORMALIZED_EQUATORIAL_RADIUS
    
        Equatorial radius rescaled (1.0).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MINUTES_PER_DAY: typing.ClassVar[float] = ...
    """
    public static final double MINUTES_PER_DAY
    
        Time units per julian day.
    
        Also see:
            :meth:`~constant`
    
    
    """
    XKE: typing.ClassVar[float] = ...
    """
    public static final double XKE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    XJ3: typing.ClassVar[float] = ...
    """
    public static final double XJ3
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    XJ2: typing.ClassVar[float] = ...
    """
    public static final double XJ2
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    XJ4: typing.ClassVar[float] = ...
    """
    public static final double XJ4
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CK2: typing.ClassVar[float] = ...
    """
    public static final double CK2
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CK4: typing.ClassVar[float] = ...
    """
    public static final double CK4
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S: typing.ClassVar[float] = ...
    """
    public static final double S
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    QOMS2T: typing.ClassVar[float] = ...
    """
    public static final double QOMS2T
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    A3OVK2: typing.ClassVar[float] = ...
    """
    public static final double A3OVK2
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ZNS: typing.ClassVar[float] = ...
    """
    public static final double ZNS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ZES: typing.ClassVar[float] = ...
    """
    public static final double ZES
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ZNL: typing.ClassVar[float] = ...
    """
    public static final double ZNL
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ZEL: typing.ClassVar[float] = ...
    """
    public static final double ZEL
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    THDT: typing.ClassVar[float] = ...
    """
    public static final double THDT
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C1SS: typing.ClassVar[float] = ...
    """
    public static final double C1SS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C1L: typing.ClassVar[float] = ...
    """
    public static final double C1L
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROOT22: typing.ClassVar[float] = ...
    """
    public static final double ROOT22
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROOT32: typing.ClassVar[float] = ...
    """
    public static final double ROOT32
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROOT44: typing.ClassVar[float] = ...
    """
    public static final double ROOT44
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROOT52: typing.ClassVar[float] = ...
    """
    public static final double ROOT52
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROOT54: typing.ClassVar[float] = ...
    """
    public static final double ROOT54
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    Q22: typing.ClassVar[float] = ...
    """
    public static final double Q22
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    Q31: typing.ClassVar[float] = ...
    """
    public static final double Q31
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    Q33: typing.ClassVar[float] = ...
    """
    public static final double Q33
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_FASX2: typing.ClassVar[float] = ...
    """
    public static final double C_FASX2
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_FASX2: typing.ClassVar[float] = ...
    """
    public static final double S_FASX2
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_2FASX4: typing.ClassVar[float] = ...
    """
    public static final double C_2FASX4
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_2FASX4: typing.ClassVar[float] = ...
    """
    public static final double S_2FASX4
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_3FASX6: typing.ClassVar[float] = ...
    """
    public static final double C_3FASX6
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_3FASX6: typing.ClassVar[float] = ...
    """
    public static final double S_3FASX6
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_G22: typing.ClassVar[float] = ...
    """
    public static final double C_G22
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_G22: typing.ClassVar[float] = ...
    """
    public static final double S_G22
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_G32: typing.ClassVar[float] = ...
    """
    public static final double C_G32
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_G32: typing.ClassVar[float] = ...
    """
    public static final double S_G32
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_G44: typing.ClassVar[float] = ...
    """
    public static final double C_G44
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_G44: typing.ClassVar[float] = ...
    """
    public static final double S_G44
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_G52: typing.ClassVar[float] = ...
    """
    public static final double C_G52
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_G52: typing.ClassVar[float] = ...
    """
    public static final double S_G52
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    C_G54: typing.ClassVar[float] = ...
    """
    public static final double C_G54
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    S_G54: typing.ClassVar[float] = ...
    """
    public static final double S_G54
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MU: typing.ClassVar[float] = ...
    """
    public static final double MU
    
        Earth gravity coefficient in mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """

class TLEJacobiansMapper(org.orekit.propagation.integration.AbstractJacobiansMapper):
    """
    public class TLEJacobiansMapper extends :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
    
        Mapper between two-dimensional Jacobian matrices and one-dimensional
        :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`.
    
        This class does not hold the states by itself. Instances of this class are guaranteed to be immutable.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.propagation.analytical.tle.TLEPartialDerivativesEquations`,
            :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`,
            :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`, :class:`~org.orekit.propagation.AbstractPropagator`
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    public static final int STATE_DIMENSION
    
        State dimension, fixed to 6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, parameterDriversList: org.orekit.utils.ParameterDriversList, tLEPropagator: 'TLEPropagator'): ...
    def analyticalDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
    @typing.overload
    def getParametersJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian with respect to parameters from a one-dimensional additional state array.
        
            This method extract the data from the :code:`state` and put it in the :code:`dYdP` array.
        
            If no parameters have been set in the constructor, the method returns immediately and does not reference :code:`dYdP`
            which can safely be null in this case.
        
            Specified by:
                 in class :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dYdP (double[][]): placeholder where to put the Jacobian with respect to parameters
        
            Also see:
        
        
        """
        ...
    @typing.overload
    def getParametersJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]]) -> None: ...
    def getStateJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Get the Jacobian with respect to state from a one-dimensional additional state array.
        
            This method extract the data from the :code:`state` and put it in the :code:`dYdY0` array.
        
        
            Specified by:
                 in class :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dYdY0 (double[][]): placeholder where to put the Jacobian with respect to state
        
            Also see:
        
        
        """
        ...
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[float]) -> None:
        """
            Set the Jacobian with respect to state into a one-dimensional additional state array.
        
            Specified by:
                 in class :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dY1dY0 (double[][]): Jacobian of current state at time tâ‚� with respect to state at some previous time tâ‚€
                dY1dP (double[][]): Jacobian of current state at time tâ‚� with respect to parameters (may be null if there are no parameters)
                p (double[]): placeholder where to put the one-dimensional additional state
        
            Also see:
        
        
        """
        ...

class TLEPartialDerivativesEquations:
    """
    Deprecated.
    @Deprecated public class TLEPartialDerivativesEquations extends Object
    
        Set of additional equations computing the partial derivatives of the state (orbit) with respect to initial state.
    
        This set of equations are automatically added to an
        :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator` in order to compute partial derivatives of the
        orbit along with the orbit itself. This is useful for example in orbit determination applications.
    
        The partial derivatives with respect to initial state are dimension 6 (orbit only).
    
        Since:
            11.0
    """
    def __init__(self, string: str, tLEPropagator: 'TLEPropagator'): ...
    def getMapper(self) -> TLEJacobiansMapper:
        """
            Deprecated. 
            Get a mapper between two-dimensional Jacobians and one-dimensional additional state.
        
            Returns:
                a mapper between two-dimensional Jacobians and one-dimensional additional state, with the same name as the instance
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.tle.TLEPartialDerivativesEquations.setInitialJacobians`, null
        
        
        """
        ...
    def getName(self) -> str:
        """
            Deprecated. 
            Get the name of the additional state.
        
            Returns:
                name of the additional state
        
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Deprecated. 
            Set the initial value of the Jacobian with respect to state and parameter.
        
            This method is equivalent to call null with dYdY0 set to the identity matrix and dYdP set to a zero matrix.
        
            The force models parameters for which partial derivatives are desired, *must* have been
            :meth:`~org.orekit.utils.ParameterDriver.setSelected` before this method is called, so proper matrices dimensions are
            used.
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
        
            Returns:
                state with initial Jacobians added
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> org.orekit.propagation.SpacecraftState:
        """
            Deprecated. 
            Set the initial value of the Jacobian with respect to state and parameter.
        
            The returned state must be added to the propagator (it is not done automatically, as the user may need to add more
            states to it).
        
            Parameters:
                s1 (:class:`~org.orekit.propagation.SpacecraftState`): current state
                dY1dY0 (double[][]): Jacobian of current state at time tâ‚� with respect to state at some previous time tâ‚€ (must be 6x6)
                dY1dP (double[][]): Jacobian of current state at time tâ‚� with respect to parameters (may be null if no parameters are selected)
        
            Returns:
                state with initial Jacobians added
        
        
        """
        ...

class TLEPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator):
    """
    public abstract class TLEPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        This class provides elements to propagate TLE's.
    
        The models used are SGP4 and SDP4, initially proposed by NORAD as the unique convenient propagator for TLE's. Inputs and
        outputs of this propagator are only suited for NORAD two lines elements sets, since it uses estimations and mean values
        appropriate for TLE's only.
    
        Deep- or near- space propagator is selected internally according to NORAD recommendations so that the user has not to
        worry about the used computation methods. One instance is created for each TLE (this instance can only be get using
        :meth:`~org.orekit.propagation.analytical.tle.TLEPropagator.selectExtrapolator` method, and can compute
        :class:`~org.orekit.utils.PVCoordinates` at any time. Maximum accuracy is guaranteed in a 24h range period before and
        after the provided TLE epoch (of course this accuracy is not really measurable nor predictable: according to CelesTrak,
        the precision is close to one kilometer and error won't probably rise above 2 km).
    
        This implementation is largely inspired from the paper and source code Revisiting Spacetrack Report #3 and is fully
        compliant with its results and tests cases.
    
        Also see:
            :class:`~org.orekit.propagation.analytical.tle.TLE`
    """
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getFrame` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getFrame`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState`
        
        
        """
        ...
    @staticmethod
    def getMU() -> float:
        """
            Get the Earth gravity coefficient used for TLE propagation.
        
            Returns:
                the Earth gravity coefficient.
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates:
        """
            Get the extrapolated position and velocity from an initial TLE.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the final date
        
            Returns:
                the final PVCoordinates
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def getTLE(self) -> TLE:
        """
            Get the underlying TLE.
        
            Returns:
                underlying TLE
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            For TLE propagator, calling this method is only recommended for covariance propagation when the new :code:`state`
            differs from the previous one by only adding the additional state containing the derivatives.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE) -> 'TLEPropagator':
        """
            Selects the extrapolator to use with the selected TLE.
        
            Parameters:
                tle (:class:`~org.orekit.propagation.analytical.tle.TLE`): the TLE to propagate.
                frames (:class:`~org.orekit.frames.Frames`): set of Frames to use in the propagator.
        
            Returns:
                the correct propagator.
        
            Since:
                10.1
        
        :class:`~org.orekit.annotation.DefaultDataContext` public static :class:`~org.orekit.propagation.analytical.tle.TLEPropagator` selectExtrapolator(:class:`~org.orekit.propagation.analytical.tle.TLE` tle, :class:`~org.orekit.attitudes.AttitudeProvider` attitudeProvider, double mass)
        
            Selects the extrapolator to use with the selected TLE.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                tle (:class:`~org.orekit.propagation.analytical.tle.TLE`): the TLE to propagate.
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): provider for attitude computation
                mass (double): spacecraft mass (kg)
        
            Returns:
                the correct propagator.
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.tle.TLEPropagator.selectExtrapolator`
        
            Selects the extrapolator to use with the selected TLE.
        
            Parameters:
                tle (:class:`~org.orekit.propagation.analytical.tle.TLE`): the TLE to propagate.
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): provider for attitude computation
                mass (double): spacecraft mass (kg)
                teme (:class:`~org.orekit.frames.Frame`): the TEME frame to use for propagation.
        
            Returns:
                the correct propagator.
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float) -> 'TLEPropagator': ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame) -> 'TLEPropagator': ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE, frames: org.orekit.frames.Frames) -> 'TLEPropagator': ...

_FieldSGP4__T = typing.TypeVar('_FieldSGP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSGP4(FieldTLEPropagator[_FieldSGP4__T], typing.Generic[_FieldSGP4__T]):
    """
    public class FieldSGP4<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.propagation.analytical.tle.FieldTLEPropagator`<T>
    
        This class contains methods to compute propagated coordinates with the SGP4 model.
    
        The user should not bother in this class since it is handled internaly by the
        :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`.
    
        This implementation is largely inspired from the paper and source code Revisiting Spacetrack Report #3 and is fully
        compliant with its results and tests cases.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldSGP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldSGP4__T, tArray: typing.List[_FieldSGP4__T]): ...
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldSGP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldSGP4__T, frame: org.orekit.frames.Frame, tArray: typing.List[_FieldSGP4__T]): ...

class PythonTLEPropagator(TLEPropagator):
    """
    public class PythonTLEPropagator extends :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`
    """
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...
    def finalize(self) -> None: ...
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
    def sxpInitialize(self) -> None:
        """
            Initialization proper to each propagator (SGP or SDP).
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.TLEPropagator.sxpInitialize`Â in
                classÂ :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`
        
        
        """
        ...
    def sxpPropagate(self, double: float) -> None:
        """
            Propagation proper to each propagator (SGP or SDP).
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.TLEPropagator.sxpPropagate`Â in
                classÂ :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`
        
            Parameters:
                t (double): the offset from initial epoch (min)
        
        
        """
        ...

class SGP4(TLEPropagator):
    """
    public class SGP4 extends :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`
    
        This class contains methods to compute propagated coordinates with the SGP4 model.
    
        The user should not bother in this class since it is handled internaly by the
        :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`.
    
        This implementation is largely inspired from the paper and source code Revisiting Spacetrack Report #3 and is fully
        compliant with its results and tests cases.
    """
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...

class DeepSDP4(org.orekit.propagation.analytical.tle.SDP4):
    """
    public class DeepSDP4 extends :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`
    
        This class contains the methods that compute deep space perturbation terms.
    
        The user should not bother in this class since it is handled internaly by the
        :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`.
    
        This implementation is largely inspired from the paper and source code Revisiting Spacetrack Report #3 and is fully
        compliant with its results and tests cases.
    """
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...

_FieldDeepSDP4__T = typing.TypeVar('_FieldDeepSDP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDeepSDP4(org.orekit.propagation.analytical.tle.FieldSDP4[_FieldDeepSDP4__T], typing.Generic[_FieldDeepSDP4__T]):
    """
    public class FieldDeepSDP4<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.propagation.analytical.tle.FieldTLEPropagator`<T>
    
        This class contains the methods that compute deep space perturbation terms.
    
        The user should not bother in this class since it is handled internaly by the
        :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`.
    
        This implementation is largely inspired from the paper and source code Revisiting Spacetrack Report #3 and is fully
        compliant with its results and tests cases.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldDeepSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldDeepSDP4__T, tArray: typing.List[_FieldDeepSDP4__T]): ...
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldDeepSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldDeepSDP4__T, frame: org.orekit.frames.Frame, tArray: typing.List[_FieldDeepSDP4__T]): ...

_PythonFieldSDP4__T = typing.TypeVar('_PythonFieldSDP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldSDP4(org.orekit.propagation.analytical.tle.FieldSDP4[_PythonFieldSDP4__T], typing.Generic[_PythonFieldSDP4__T]):
    """
    public class PythonFieldSDP4<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.propagation.analytical.tle.FieldTLEPropagator`<T>
    """
    def deepPeriodicEffects(self, t: _PythonFieldSDP4__T) -> None:
        """
            Computes periodic terms from current coordinates and epoch.
        
            Parameters:
                t (:class:`~org.orekit.propagation.analytical.tle.PythonFieldSDP4`): offset from initial epoch (min)
        
        
        """
        ...
    def deepSecularEffects(self, t: _PythonFieldSDP4__T) -> None:
        """
            Computes secular terms from current coordinates and epoch.
        
            Parameters:
                t (:class:`~org.orekit.propagation.analytical.tle.PythonFieldSDP4`): offset from initial epoch (min)
        
        
        """
        ...
    def finalize(self) -> None: ...
    def luniSolarTermsComputation(self) -> None:
        """
            Computes luni - solar terms from initial coordinates and epoch.
        
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

class FieldSDP4: ...

class SDP4: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.tle")``.

    DeepSDP4: typing.Type[DeepSDP4]
    FieldDeepSDP4: typing.Type[FieldDeepSDP4]
    FieldSDP4: typing.Type[FieldSDP4]
    FieldSGP4: typing.Type[FieldSGP4]
    FieldTLE: typing.Type[FieldTLE]
    FieldTLEPropagator: typing.Type[FieldTLEPropagator]
    PythonFieldSDP4: typing.Type[PythonFieldSDP4]
    PythonTLEPropagator: typing.Type[PythonTLEPropagator]
    SDP4: typing.Type[SDP4]
    SGP4: typing.Type[SGP4]
    TLE: typing.Type[TLE]
    TLEConstants: typing.Type[TLEConstants]
    TLEJacobiansMapper: typing.Type[TLEJacobiansMapper]
    TLEPartialDerivativesEquations: typing.Type[TLEPartialDerivativesEquations]
    TLEPropagator: typing.Type[TLEPropagator]
