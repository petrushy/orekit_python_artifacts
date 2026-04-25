
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org
import org.hipparchus
import org.orekit.attitudes
import org.orekit.data
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.analytical.tle.generation
import org.orekit.propagation.conversion.osc2mean
import org.orekit.time
import org.orekit.utils
import typing



_FieldTLE__T = typing.TypeVar('_FieldTLE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTLE(org.orekit.time.FieldTimeStamped[_FieldTLE__T], org.orekit.utils.ParameterDriversProvider, typing.Generic[_FieldTLE__T]):
    """
    This class is a container for a single set of TLE data.
    
    TLE sets can be built either by providing directly the two lines, in which case parsing is performed internally or by providing the already parsed elements.
    
    TLE are not transparently convertible to Orbit instances. They are significant only with respect to their dedicated TLEPropagator, which also computes position and velocity coordinates. Any attempt to directly use orbital parameters like getE, getI, etc. without any reference to the TLEPropagator is prone to errors.
    
    More information on the TLE format can be found on the celestrak
    
    Since:
        11.0
    """
    DEFAULT: typing.ClassVar[int] = ...
    """
    Identifier for default type of ephemeris (SGP4/SDP4).
    
    Also see:
        constant
    
    
    """
    SGP: typing.ClassVar[int] = ...
    """
    Identifier for SGP type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SGP4: typing.ClassVar[int] = ...
    """
    Identifier for SGP4 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SDP4: typing.ClassVar[int] = ...
    """
    Identifier for SDP4 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SGP8: typing.ClassVar[int] = ...
    """
    Identifier for SGP8 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SDP8: typing.ClassVar[int] = ...
    """
    Identifier for SDP8 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    B_STAR: typing.ClassVar[str] = ...
    """
    Parameter name for B* coefficient.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLE__T], t: _FieldTLE__T, t2: _FieldTLE__T, t3: _FieldTLE__T, t4: _FieldTLE__T, t5: _FieldTLE__T, t6: _FieldTLE__T, t7: _FieldTLE__T, t8: _FieldTLE__T, int6: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLE__T], t: _FieldTLE__T, t2: _FieldTLE__T, t3: _FieldTLE__T, t4: _FieldTLE__T, t5: _FieldTLE__T, t6: _FieldTLE__T, t7: _FieldTLE__T, t8: _FieldTLE__T, int6: int, double: float, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTLE__T], string: str, string2: str): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTLE__T], string: str, string2: str, timeScale: org.orekit.time.TimeScale): ...
    def computeSemiMajorAxis(self) -> _FieldTLE__T:
        """
        Compute the semi-major axis from the mean motion of the TLE and the gravitational parameter from TLEConstants.
        
        Returns:
            the semi-major axis computed.
        
        
        """
        ...
    def equals(self, o: typing.Any) -> bool:
        """
        Check if this tle equals the provided tle.
        
        Due to the difference in precision between object and string representations of TLE, it is possible for this method to return false even if string representations returned by toString are equal.
        
        Overrides: Object in class Object
        
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
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTLE__T]:
        """
        Get the TLE current date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            the epoch
        
        
        """
        ...
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
            the ephemeris type (one of DEFAULT,
            SGP,
            SGP4,
            SGP8,
            SDP4,
            SDP8)
        
        
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
            the mean motion first derivative (rad/s²)
        
        
        """
        ...
    def getMeanMotionSecondDerivative(self) -> _FieldTLE__T:
        """
        Get the mean motion second derivative.
        
        Returns:
            the mean motion second derivative (rad/s³)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters..
        
        Get the drivers for TLE propagation SGP4 and SDP4.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for SGP4 and SDP4 model parameters
        
        
        """
        ...
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
        
        Overrides: Object in class Object
        
        Returns:
            hashcode
        
        
        """
        ...
    @staticmethod
    def isFormatOK(line1: str, line2: str) -> bool:
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
    def stateToTLE(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_stateToTLE_0__T], fieldTLE: 'FieldTLE'[_stateToTLE_0__T], tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm) -> 'FieldTLE'[_stateToTLE_0__T]:
        """
        Convert Spacecraft State into TLE.
        
        The B* is not calculated. Its value is simply copied from the template to the generated TLE.
        
        Parameters:
            state (FieldSpacecraftState<T> state): Spacecraft State to convert into TLE
            templateTLE (FieldTLE<T> templateTLE): only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained
                in the generated TLE are based on the provided state and not the template TLE.
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
            dataContext (DataContext): data context
        
        Returns:
            a generated TLE
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def stateToTLE(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_stateToTLE_1__T], fieldTLE: 'FieldTLE'[_stateToTLE_1__T], osculatingToMeanConverter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> 'FieldTLE'[_stateToTLE_1__T]: ...
    @typing.overload
    @staticmethod
    def stateToTLE(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_stateToTLE_2__T], fieldTLE: 'FieldTLE'[_stateToTLE_2__T], osculatingToMeanConverter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter, dataContext: org.orekit.data.DataContext) -> 'FieldTLE'[_stateToTLE_2__T]: ...
    def toString(self) -> str:
        """
        Get a string representation of this TLE set.
        
        The representation is simply the two lines separated by the platform line separator.
        
        Overrides: Object in class Object
        
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
    This class provides elements to propagate TLE's.
    
    The models used are SGP4 and SDP4, initially proposed by NORAD as the unique convenient propagator for TLE's. Inputs and outputs of this propagator are only suited for NORAD two lines elements sets, since it uses estimations and mean values appropriate for TLE's only.
    
    Deep- or near- space propagator is selected internally according to NORAD recommendations so that the user has not to worry about the used computation methods. One instance is created for each TLE (this instance can only be get using selectExtrapolator method, and can compute PVCoordinates at any time. Maximum accuracy is guaranteed in a 24h range period before and after the provided TLE epoch (of course this accuracy is not really measurable nor predictable: according to celestrak, the precision is close to one kilometer and error won't probably rise above 2 km).
    
    This implementation is largely inspired from the paper and source code AIAA and is fully compliant with its results and tests cases.
    
    Since:
        11.0
    
    Also see:
        FieldTLE
    """
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface FieldPropagator
        
        Overrides: getFrame in class FieldAbstractPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
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
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTLEPropagator__T]: ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], tArray: typing.Union[typing.List[_FieldTLEPropagator__T], jpype.JArray]) -> org.orekit.utils.FieldPVCoordinates[_FieldTLEPropagator__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getTLE(self) -> FieldTLE[_FieldTLEPropagator__T]:
        """
        Get the underlying TLE. If there has been calls to #resetInitialState or #resetIntermediateState, it will not be the same as given to the constructor.
        
        Returns:
            underlying TLE
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldTLEPropagator__T], parameters: typing.Union[typing.List[_FieldTLEPropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldOrbit[_FieldTLEPropagator__T]:
        """
        Propagate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<FieldTLEPropagator> date): target date for the orbit
            parameters (FieldTLEPropagator[]): model parameters
        
        Returns:
            propagated orbit
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldTLEPropagator__T]) -> None:
        """
        Reset the propagator initial state.
        
        For TLE propagator, calling this method is only recommended for covariance propagation when the new state differs from the previous one by only adding the additional state containing the derivatives.
        
        Specified by: resetInitialState in interface FieldPropagator
        
        Overrides: resetInitialState in class FieldAbstractPropagator
        
        Parameters:
            state (FieldSpacecraftState<FieldTLEPropagator> state): new initial state to consider
        
        
        """
        ...
    _selectExtrapolator_0__T = typing.TypeVar('_selectExtrapolator_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_1__T = typing.TypeVar('_selectExtrapolator_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_2__T = typing.TypeVar('_selectExtrapolator_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _selectExtrapolator_3__T = typing.TypeVar('_selectExtrapolator_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_0__T], tArray: typing.Union[typing.List[_selectExtrapolator_0__T], jpype.JArray]) -> 'FieldTLEPropagator'[_selectExtrapolator_0__T]:
        """
        Selects the extrapolator to use with the selected TLE.
        
        This method uses the getDefault.
        
        Parameters:
            tle (FieldTLE<T> tle): the TLE to propagate.
            teme (Frame): TEME frame.
            parameters (T[]): SGP4 and SDP4 model parameters
        
        Returns:
            the correct propagator.
        
        DefaultDataContext public static <T extends CalculusFieldElement<T>> FieldTLEPropagator<T> selectExtrapolator (FieldTLE<T> tle, AttitudeProvider attitudeProvider, T mass, T[] parameters)
        
        Selects the extrapolator to use with the selected TLE.
        
        This method uses the getDefault.
        
        Parameters:
            tle (FieldTLE<T> tle): the TLE to propagate.
            attitudeProvider (AttitudeProvider): provider for attitude computation
            mass (T): spacecraft mass (kg)
            parameters (T[]): SGP4 and SDP4 model parameters
        
        Returns:
            the correct propagator.
        
        Also see:
            selectExtrapolator
        
        Selects the extrapolator to use with the selected TLE.
        
        Parameters:
            tle (FieldTLE<T> tle): the TLE to propagate.
            attitudeProvider (AttitudeProvider): provider for attitude computation
            mass (T): spacecraft mass (kg)
            teme (Frame): the TEME frame to use for propagation.
            parameters (T[]): SGP4 and SDP4 model parameters
        
        Returns:
            the correct propagator.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_1__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _selectExtrapolator_1__T, tArray: typing.Union[typing.List[_selectExtrapolator_1__T], jpype.JArray]) -> 'FieldTLEPropagator'[_selectExtrapolator_1__T]: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_2__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _selectExtrapolator_2__T, frame: org.orekit.frames.Frame, tArray: typing.Union[typing.List[_selectExtrapolator_2__T], jpype.JArray]) -> 'FieldTLEPropagator'[_selectExtrapolator_2__T]: ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(fieldTLE: FieldTLE[_selectExtrapolator_3__T], frame: org.orekit.frames.Frame, tArray: typing.Union[typing.List[_selectExtrapolator_3__T], jpype.JArray]) -> 'FieldTLEPropagator'[_selectExtrapolator_3__T]: ...

class TLE(org.orekit.time.TimeStamped, org.orekit.utils.ParameterDriversProvider):
    """
    This class is a container for a single set of TLE data.
    
    TLE sets can be built either by providing directly the two lines, in which case parsing is performed internally or by providing the already parsed elements.
    
    TLE are not transparently convertible to Orbit instances. They are significant only with respect to their dedicated TLEPropagator, which also computes position and velocity coordinates. Any attempt to directly use orbital parameters like getE, getI, etc. without any reference to the TLEPropagator is prone to errors.
    
    More information on the TLE format can be found on the celestrak
    """
    SGP: typing.ClassVar[int] = ...
    """
    Identifier for SGP type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SGP4: typing.ClassVar[int] = ...
    """
    Identifier for SGP4 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SDP4: typing.ClassVar[int] = ...
    """
    Identifier for SDP4 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SGP8: typing.ClassVar[int] = ...
    """
    Identifier for SGP8 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    SDP8: typing.ClassVar[int] = ...
    """
    Identifier for SDP8 type of ephemeris.
    
    Also see:
        constant
    
    
    """
    DEFAULT: typing.ClassVar[int] = ...
    """
    Identifier for default type of ephemeris (SGP4/SDP4).
    
    Also see:
        constant
    
    
    """
    B_STAR: typing.ClassVar[str] = ...
    """
    Parameter name for B* coefficient.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int6: int, double9: float): ...
    @typing.overload
    def __init__(self, int: int, char: str, int2: int, int3: int, string: str, int4: int, int5: int, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int6: int, double9: float, timeScale: org.orekit.time.TimeScale): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, timeScale: org.orekit.time.TimeScale): ...
    def computeSemiMajorAxis(self) -> float:
        """
        Compute the semi-major axis from the mean motion of the TLE and the gravitational parameter from TLEConstants.
        
        Returns:
            the semi-major axis computed.
        
        
        """
        ...
    def equals(self, o: typing.Any) -> bool:
        """
        Check if this tle equals the provided tle.
        
        Due to the difference in precision between object and string representations of TLE, it is possible for this method to return false even if string representations returned by toString are equal.
        
        Overrides: Object in class Object
        
        Parameters:
            o (Object): other tle
        
        Returns:
            true if this tle equals the provided tle
        
        
        """
        ...
    @typing.overload
    def getBStar(self) -> float:
        """
        Get the ballistic coefficient at tle date.
        
        Returns:
            bStar
        
        """
        ...
    @typing.overload
    def getBStar(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the ballistic coefficient at a specific date.
        
        Parameters:
            date (AbsoluteDate): at which the ballistic coefficient wants to be known.
        
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
        
        Specified by: getDate in interface TimeStamped
        
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
            the ephemeris type (one of DEFAULT,
            SGP, SGP4,
            SGP8, SDP4,
            SDP8)
        
        
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
            the mean motion first derivative (rad/s²)
        
        
        """
        ...
    def getMeanMotionSecondDerivative(self) -> float:
        """
        Get the mean motion second derivative.
        
        Returns:
            the mean motion second derivative (rad/s³)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for TLE propagation SGP4 and SDP4.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for SGP4 and SDP4 model parameters
        
        
        """
        ...
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
        
        Overrides: Object in class Object
        
        Returns:
            hashcode
        
        
        """
        ...
    @staticmethod
    def isFormatOK(line1: str, line2: str) -> bool:
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
    def stateToTLE(spacecraftState: org.orekit.propagation.SpacecraftState, tLE: 'TLE', tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm) -> 'TLE':
        """
        Convert Spacecraft State into TLE.
        
        The B* is not calculated. Its value is simply copied from the model to the generated TLE.
        
        Parameters:
            state (SpacecraftState): Spacecraft State to convert into TLE
            templateTLE (TLE): only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained
                in the generated TLE are based on the provided state and not the template TLE.
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
            dataContext (DataContext): data context
        
        Returns:
            a generated TLE
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def stateToTLE(spacecraftState: org.orekit.propagation.SpacecraftState, tLE: 'TLE', osculatingToMeanConverter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> 'TLE': ...
    @typing.overload
    @staticmethod
    def stateToTLE(spacecraftState: org.orekit.propagation.SpacecraftState, tLE: 'TLE', osculatingToMeanConverter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter, dataContext: org.orekit.data.DataContext) -> 'TLE': ...
    def toString(self) -> str:
        """
        Get a string representation of this TLE set.
        
        The representation is simply the two lines separated by the platform line separator.
        
        Overrides: Object in class Object
        
        Returns:
            string representation of this TLE set
        
        
        """
        ...

class TLEConstants:
    """
    Constants necessary to TLE propagation. This constants are used in the WGS-72 model, compliant with NORAD implementations.
    """
    ONE_THIRD: typing.ClassVar[float] = ...
    """
    Constant 1.0 / 3.0.
    
    Also see:
        constant
    
    
    """
    TWO_THIRD: typing.ClassVar[float] = ...
    """
    Constant 2.0 / 3.0.
    
    Also see:
        constant
    
    
    """
    EARTH_RADIUS: typing.ClassVar[float] = ...
    """
    Earth radius in km.
    
    Also see:
        constant
    
    
    """
    NORMALIZED_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Equatorial radius rescaled (1.0).
    
    Also see:
        constant
    
    
    """
    MINUTES_PER_DAY: typing.ClassVar[float] = ...
    """
    Time units per julian day.
    
    Also see:
        constant
    
    
    """
    XKE: typing.ClassVar[float] = ...
    """
    XKE.
    
    Also see:
        constant
    
    
    """
    XJ3: typing.ClassVar[float] = ...
    """
    XJ3.
    
    Also see:
        constant
    
    
    """
    XJ2: typing.ClassVar[float] = ...
    """
    XJ2.
    
    Also see:
        constant
    
    
    """
    XJ4: typing.ClassVar[float] = ...
    """
    XJ4.
    
    Also see:
        constant
    
    
    """
    CK2: typing.ClassVar[float] = ...
    """
    CK2.
    
    Also see:
        constant
    
    
    """
    CK4: typing.ClassVar[float] = ...
    """
    CK4.
    
    Also see:
        constant
    
    
    """
    S: typing.ClassVar[float] = ...
    """
    S.
    
    Also see:
        constant
    
    
    """
    QOMS2T: typing.ClassVar[float] = ...
    """
    QOMS2T.
    
    Also see:
        constant
    
    
    """
    A3OVK2: typing.ClassVar[float] = ...
    """
    A3OVK2.
    
    Also see:
        constant
    
    
    """
    ZNS: typing.ClassVar[float] = ...
    """
    ZNS.
    
    Also see:
        constant
    
    
    """
    ZES: typing.ClassVar[float] = ...
    """
    ZES.
    
    Also see:
        constant
    
    
    """
    ZNL: typing.ClassVar[float] = ...
    """
    ZNL.
    
    Also see:
        constant
    
    
    """
    ZEL: typing.ClassVar[float] = ...
    """
    ZEL.
    
    Also see:
        constant
    
    
    """
    THDT: typing.ClassVar[float] = ...
    """
    THDT.
    
    Also see:
        constant
    
    
    """
    C1SS: typing.ClassVar[float] = ...
    """
    C1SS.
    
    Also see:
        constant
    
    
    """
    C1L: typing.ClassVar[float] = ...
    """
    C1L.
    
    Also see:
        constant
    
    
    """
    ROOT22: typing.ClassVar[float] = ...
    """
    ROOT22.
    
    Also see:
        constant
    
    
    """
    ROOT32: typing.ClassVar[float] = ...
    """
    ROOT32.
    
    Also see:
        constant
    
    
    """
    ROOT44: typing.ClassVar[float] = ...
    """
    ROOT44.
    
    Also see:
        constant
    
    
    """
    ROOT52: typing.ClassVar[float] = ...
    """
    ROOT52.
    
    Also see:
        constant
    
    
    """
    ROOT54: typing.ClassVar[float] = ...
    """
    ROOT54.
    
    Also see:
        constant
    
    
    """
    Q22: typing.ClassVar[float] = ...
    """
    Q22.
    
    Also see:
        constant
    
    
    """
    Q31: typing.ClassVar[float] = ...
    """
    Q31.
    
    Also see:
        constant
    
    
    """
    Q33: typing.ClassVar[float] = ...
    """
    Q33.
    
    Also see:
        constant
    
    
    """
    C_FASX2: typing.ClassVar[float] = ...
    """
    C_FASX2.
    
    Also see:
        constant
    
    
    """
    S_FASX2: typing.ClassVar[float] = ...
    """
    S_FASX2.
    
    Also see:
        constant
    
    
    """
    C_2FASX4: typing.ClassVar[float] = ...
    """
    C_2FASX4.
    
    Also see:
        constant
    
    
    """
    S_2FASX4: typing.ClassVar[float] = ...
    """
    S_2FASX4.
    
    Also see:
        constant
    
    
    """
    C_3FASX6: typing.ClassVar[float] = ...
    """
    C_3FASX6.
    
    Also see:
        constant
    
    
    """
    S_3FASX6: typing.ClassVar[float] = ...
    """
    S_3FASX6.
    
    Also see:
        constant
    
    
    """
    C_G22: typing.ClassVar[float] = ...
    """
    C_G22.
    
    Also see:
        constant
    
    
    """
    S_G22: typing.ClassVar[float] = ...
    """
    S_G22.
    
    Also see:
        constant
    
    
    """
    C_G32: typing.ClassVar[float] = ...
    """
    C_G32.
    
    Also see:
        constant
    
    
    """
    S_G32: typing.ClassVar[float] = ...
    """
    S_G32.
    
    Also see:
        constant
    
    
    """
    C_G44: typing.ClassVar[float] = ...
    """
    C_G44.
    
    Also see:
        constant
    
    
    """
    S_G44: typing.ClassVar[float] = ...
    """
    S_G44.
    
    Also see:
        constant
    
    
    """
    C_G52: typing.ClassVar[float] = ...
    """
    C_G52.
    
    Also see:
        constant
    
    
    """
    S_G52: typing.ClassVar[float] = ...
    """
    S_G52.
    
    Also see:
        constant
    
    
    """
    C_G54: typing.ClassVar[float] = ...
    """
    C_G54.
    
    Also see:
        constant
    
    
    """
    S_G54: typing.ClassVar[float] = ...
    """
    S_G54.
    
    Also see:
        constant
    
    
    """
    MU: typing.ClassVar[float] = ...
    """
    Earth gravity coefficient in m³/s².
    
    Also see:
        constant
    
    
    """

class TLEPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator):
    """
    This class provides elements to propagate TLE's.
    
    The models used are SGP4 and SDP4, initially proposed by NORAD as the unique convenient propagator for TLE's. Inputs and outputs of this propagator are only suited for NORAD two lines elements sets, since it uses estimations and mean values appropriate for TLE's only.
    
    Deep- or near- space propagator is selected internally according to NORAD recommendations so that the user has not to worry about the used computation methods. One instance is created for each TLE (this instance can only be get using selectExtrapolator method, and can compute PVCoordinates at any time. Maximum accuracy is guaranteed in a 24h range period before and after the provided TLE epoch (of course this accuracy is not really measurable nor predictable: according to celestrak, the precision is close to one kilometer and error won't probably rise above 2 km).
    
    This implementation is largely inspired from the paper and source code AIAA and is fully compliant with its results and tests cases.
    
    Also see:
        TLE
    """
    @staticmethod
    def getDefaultTleGenerationAlgorithm(utc: org.orekit.time.TimeScale, teme: org.orekit.frames.Frame) -> org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm:
        """
        Get the default TLE generation algorithm.
        
        Parameters:
            utc (TimeScale): UTC time scale
            teme (Frame): TEME frame
        
        Returns:
            a TLE generation algorithm
        
        Since:
            12.0
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface Propagator
        
        Overrides: getFrame in class AbstractPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
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
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates:
        """
        Get the extrapolated position and velocity from an initial TLE.
        
        Parameters:
            date (AbsoluteDate): the final date
        
        Returns:
            the final PVCoordinates
        
        
        """
        ...
    def getTLE(self) -> TLE:
        """
        Get the underlying TLE. If there has been calls to #resetInitialState or #resetIntermediateState, it will not be the same as given to the constructor.
        
        Returns:
            underlying TLE
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Extrapolate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        For TLE propagator, calling this method is only recommended for covariance propagation when the new state differs from the previous one by only adding the additional state containing the derivatives.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE) -> 'TLEPropagator':
        """
        Selects the extrapolator to use with the selected TLE.
        
        Parameters:
            tle (TLE): the TLE to propagate.
            teme (Frame): TEME frame.
        
        Returns:
            the correct propagator.
        
        Since:
            10.1
        
        Also see:
            selectExtrapolator
        
        Selects the extrapolator to use with the selected TLE.
        
        Parameters:
            tle (TLE): the TLE to propagate.
            teme (Frame): TEME frame.
            attitudeProvider (AttitudeProvider): provider for attitude computation
        
        Returns:
            the correct propagator.
        
        Since:
            12.2
        
        DefaultDataContext public static TLEPropagator selectExtrapolator (TLE tle, AttitudeProvider attitudeProvider, double mass)
        
        Selects the extrapolator to use with the selected TLE.
        
        This method uses the getDefault.
        
        Parameters:
            tle (TLE): the TLE to propagate.
            attitudeProvider (AttitudeProvider): provider for attitude computation
            mass (double): spacecraft mass (kg)
        
        Returns:
            the correct propagator.
        
        Also see:
            selectExtrapolator
        
        Selects the extrapolator to use with the selected TLE.
        
        Parameters:
            tle (TLE): the TLE to propagate.
            attitudeProvider (AttitudeProvider): provider for attitude computation
            mass (double): spacecraft mass (kg)
            teme (Frame): the TEME frame to use for propagation.
        
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
    def selectExtrapolator(tLE: TLE, frame: org.orekit.frames.Frame) -> 'TLEPropagator': ...
    @typing.overload
    @staticmethod
    def selectExtrapolator(tLE: TLE, frame: org.orekit.frames.Frame, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> 'TLEPropagator': ...

_FieldSGP4__T = typing.TypeVar('_FieldSGP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSGP4(FieldTLEPropagator[_FieldSGP4__T], typing.Generic[_FieldSGP4__T]):
    """
    This class contains methods to compute propagated coordinates with the SGP4 model.
    
    The user should not bother in this class since it is handled internaly by the TLEPropagator.
    
    This implementation is largely inspired from the paper and source code AIAA and is fully compliant with its results and tests cases.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldSGP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldSGP4__T, tArray: typing.Union[typing.List[_FieldSGP4__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldSGP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldSGP4__T, frame: org.orekit.frames.Frame, tArray: typing.Union[typing.List[_FieldSGP4__T], jpype.JArray]): ...

class PythonTLEPropagator(TLEPropagator):
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...
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
    def sxpInitialize(self) -> None:
        """
        Initialization proper to each propagator (SGP or SDP).
        
        Specified by: sxpInitialize in class TLEPropagator
        
        
        """
        ...
    def sxpPropagate(self, t: float) -> None:
        """
        Propagation proper to each propagator (SGP or SDP).
        
        Specified by: sxpPropagate in class TLEPropagator
        
        Parameters:
            t (double): the offset from initial epoch (min)
        
        
        """
        ...

class SGP4(TLEPropagator):
    """
    This class contains methods to compute propagated coordinates with the SGP4 model.
    
    The user should not bother in this class since it is handled internaly by the TLEPropagator.
    
    This implementation is largely inspired from the paper and source code AIAA and is fully compliant with its results and tests cases.
    """
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...

class DeepSDP4(org.orekit.propagation.analytical.tle.SDP4):
    """
    This class contains the methods that compute deep space perturbation terms.
    
    The user should not bother in this class since it is handled internaly by the TLEPropagator.
    
    This implementation is largely inspired from the paper and source code AIAA and is fully compliant with its results and tests cases.
    """
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, tLE: TLE, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, frame: org.orekit.frames.Frame): ...

_FieldDeepSDP4__T = typing.TypeVar('_FieldDeepSDP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDeepSDP4(org.orekit.propagation.analytical.tle.FieldSDP4[_FieldDeepSDP4__T], typing.Generic[_FieldDeepSDP4__T]):
    """
    This class contains the methods that compute deep space perturbation terms.
    
    The user should not bother in this class since it is handled internaly by the TLEPropagator.
    
    This implementation is largely inspired from the paper and source code AIAA and is fully compliant with its results and tests cases.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldDeepSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldDeepSDP4__T, tArray: typing.Union[typing.List[_FieldDeepSDP4__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, fieldTLE: FieldTLE[_FieldDeepSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldDeepSDP4__T, frame: org.orekit.frames.Frame, tArray: typing.Union[typing.List[_FieldDeepSDP4__T], jpype.JArray]): ...

_PythonFieldSDP4__T = typing.TypeVar('_PythonFieldSDP4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldSDP4(org.orekit.propagation.analytical.tle.FieldSDP4[_PythonFieldSDP4__T], typing.Generic[_PythonFieldSDP4__T]):
    def __init__(self, initialTLE: FieldTLE[_PythonFieldSDP4__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, mass: _PythonFieldSDP4__T, teme: org.orekit.frames.Frame, parameters: typing.Union[typing.List[_PythonFieldSDP4__T], jpype.JArray]):
        """
        Constructor for a unique initial TLE.
        
        Parameters:
            initialTLE (FieldTLE<PythonFieldSDP4> initialTLE): the TLE to propagate.
            attitudeProvider (AttitudeProvider): provider for attitude computation
            mass (PythonFieldSDP4): spacecraft mass (kg)
            teme (Frame): the TEME frame to use for propagation.
            parameters (PythonFieldSDP4[]): SGP4 and SDP4 model parameters
        
        
        """
        ...
    def deepPeriodicEffects(self, t: _PythonFieldSDP4__T) -> None:
        """
        Computes periodic terms from current coordinates and epoch.
        
        Parameters:
            t (PythonFieldSDP4): offset from initial epoch (min)
        
        
        """
        ...
    def deepSecularEffects(self, t: _PythonFieldSDP4__T) -> None:
        """
        Computes secular terms from current coordinates and epoch.
        
        Parameters:
            t (PythonFieldSDP4): offset from initial epoch (min)
        
        
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


class __module_protocol__(Protocol):
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
    TLEPropagator: typing.Type[TLEPropagator]
    generation: org.orekit.propagation.analytical.tle.generation.__module_protocol__
