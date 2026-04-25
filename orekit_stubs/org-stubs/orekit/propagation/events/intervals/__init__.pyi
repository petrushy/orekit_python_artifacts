
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.orekit.frames
import org.orekit.propagation
import org.orekit.time
import typing



class AdaptableInterval:
    """
    This interface represents an event checking interval that depends on state.
    
    Since:
        12.0
    
    Also see:
        EventDetector
    """
    def currentInterval(self, state: org.orekit.propagation.SpacecraftState, isForward: bool) -> float:
        """
        Get the current value of maximal time interval between events handler checks.
        
        Parameters:
            state (SpacecraftState): current state
            isForward (boolean): direction of propagation
        
        Returns:
            current value of maximal time interval between events handler checks
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(double: float) -> 'AdaptableInterval':
        """
        Method creating a constant interval provider.
        
        Parameters:
            constantInterval (double): value of constant interval
        
        Returns:
            adaptable interval ready to be added to an event detector
        
        Since:
            12.1
        
        Method creating an interval taking the minimum value of all candidates.
        
        Parameters:
            defaultMaxCheck (double): default value if no intervals is given as input
            adaptableIntervals (AdaptableInterval...): intervals
        
        Returns:
            adaptable interval ready to be added to an event detector
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(double: float, *adaptableInterval: typing.Union['AdaptableInterval', typing.Callable]) -> 'AdaptableInterval': ...

class ApsideDetectionAdaptableIntervalFactory:
    """
    Factory class for AdaptableInterval suitable for apside detection on eccentric orbits. It requires SpacecraftState to be based on Orbit in order to work.
    
    Since:
        12.1
    
    Also see:
        AdaptableInterval,
        ApsideDetector, EventSlopeFilter
    """
    @staticmethod
    def computeKeplerianDurationFromPreviousApoapsis(meanAnomaly: float, meanMotion: float) -> float:
        """
        Method computing time elapsed since last apoapsis, assuming Keplerian motion.
        
        Parameters:
            meanAnomaly (double): mean anomaly
            meanMotion (double): Keplerian mean motion
        
        Returns:
            duration elapsed since last apoapsis
        
        
        """
        ...
    @staticmethod
    def computeKeplerianDurationFromPreviousPeriapsis(meanAnomaly: float, meanMotion: float) -> float:
        """
        Method computing time elapsed since last periapsis, assuming Keplerian motion.
        
        Parameters:
            meanAnomaly (double): mean anomaly
            meanMotion (double): Keplerian mean motion
        
        Returns:
            duration elapsed since last periapsis
        
        
        """
        ...
    @staticmethod
    def getApoapsisDetectionAdaptableInterval() -> AdaptableInterval:
        """
        Method providing a candidate AdaptableInterval for apoapsis detection. It uses a Keplerian, eccentric approximation.
        
        Returns:
            adaptable interval for apoapsis detection
        
        
        """
        ...
    @staticmethod
    def getApsideDetectionAdaptableInterval() -> AdaptableInterval:
        """
        Method providing a candidate AdaptableInterval for arbitrary apside detection. It uses a Keplerian, eccentric approximation.
        
        Returns:
            adaptable interval for apside detection
        
        
        """
        ...
    @staticmethod
    def getPeriapsisDetectionAdaptableInterval() -> AdaptableInterval:
        """
        Method providing a candidate AdaptableInterval for periapsis detection. It uses a Keplerian, eccentric approximation.
        
        Returns:
            adaptable interval for periaspsis detection
        
        
        """
        ...

class DateDetectionAdaptableIntervalFactory:
    """
    Factory for adaptable interval tuned for date(s) detection.
    
    Since:
        13.0
    
    Also see:
        DateDetector, FieldDateDetector
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    Default value for max check.
    
    Also see:
        constant
    
    
    """
    @staticmethod
    def getDatesDetectionConstantInterval(*timeStampeds: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> AdaptableInterval:
        """
        Return a candidate AdaptableInterval for multiple dates detection with a constant max. check.
        
        Parameters:
            timeStampeds (TimeStamped...): event dates
        
        Returns:
            adaptable interval
        
        
        """
        ...
    _getDatesDetectionFieldConstantInterval__T = typing.TypeVar('_getDatesDetectionFieldConstantInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getDatesDetectionFieldConstantInterval(*timeStampeds: typing.Union[org.orekit.time.FieldTimeStamped[_getDatesDetectionFieldConstantInterval__T], typing.Callable[[], org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement]]]) -> 'FieldAdaptableInterval'[_getDatesDetectionFieldConstantInterval__T]:
        """
        Return a candidate FieldAdaptableInterval for multiple dates detection with a constant max. check.
        
        Parameters:
            timeStampeds (FieldTimeStamped<T>...): event dates
        
        Returns:
            adaptable interval
        
        
        """
        ...
    _getDatesDetectionFieldInterval__T = typing.TypeVar('_getDatesDetectionFieldInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getDatesDetectionFieldInterval(*timeStampeds: typing.Union[org.orekit.time.FieldTimeStamped[_getDatesDetectionFieldInterval__T], typing.Callable[[], org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement]]]) -> 'FieldAdaptableInterval'[_getDatesDetectionFieldInterval__T]:
        """
        Return a candidate FieldAdaptableInterval for multiple dates detection.
        
        Parameters:
            timeStampeds (FieldTimeStamped<T>...): event dates
        
        Returns:
            adaptable interval
        
        
        """
        ...
    @staticmethod
    def getDatesDetectionInterval(*timeStampeds: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> AdaptableInterval:
        """
        Return a candidate AdaptableInterval for multiple dates detection.
        
        Parameters:
            timeStampeds (TimeStamped...): event dates
        
        Returns:
            adaptable interval
        
        
        """
        ...
    @staticmethod
    def getMinGap(*timeStampeds: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> float:
        """
        Compute min. gap between dated objects if applicable. It ignores duplicates.
        
        Parameters:
            timeStampeds (TimeStamped...): time stamped objects
        
        Returns:
            minimum gap
        
        
        """
        ...
    @staticmethod
    def getSingleDateDetectionAdaptableInterval() -> AdaptableInterval:
        """
        Return a candidate AdaptableInterval for single date detection.
        
        Returns:
            adaptable interval
        
        
        """
        ...
    _getSingleDateDetectionFieldAdaptableInterval__T = typing.TypeVar('_getSingleDateDetectionFieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getSingleDateDetectionFieldAdaptableInterval() -> 'FieldAdaptableInterval'[_getSingleDateDetectionFieldAdaptableInterval__T]:
        """
        Return a candidate FieldAdaptableInterval for single date detection.
        
        Returns:
            adaptable interval
        
        
        """
        ...

class ElevationDetectionAdaptableIntervalFactory:
    """
    Factory class for AdaptableInterval suitable for elevation detection on eccentric orbits. It requires SpacecraftState to be based on Orbit in order to work.
    
    Since:
        12.1
    
    Also see:
        AdaptableInterval,
        ApsideDetector, EventSlopeFilter
    """
    DEFAULT_ELEVATION_SWITCH_INF: typing.ClassVar[float] = ...
    """
    Default elevation above which interval should be switched to fine interval (-5°).
    
    Since:
        13.0
    
    
    """
    DEFAULT_ELEVATION_SWITCH_SUP: typing.ClassVar[float] = ...
    """
    Default elevation below which interval should be switched to fine interval (+15°).
    
    Since:
        13.0
    
    
    """
    @staticmethod
    def getAdaptableInterval(topo: org.orekit.frames.TopocentricFrame, elevationSwitchInf: float, elevationSwitchSup: float, fineCheckInterval: float) -> AdaptableInterval:
        """
        Method providing a candidate AdaptableInterval for arbitrary elevation detection with forward propagation. It uses a Keplerian, eccentric approximation.
        
        Parameters:
            topo (TopocentricFrame): topocentric frame centered at ground interest point
            elevationSwitchInf (double): elevation above which interval will switch to fineCheckInterval (typically
                DEFAULT_ELEVATION_SWITCH_INF
                which is -5°)
            elevationSwitchSup (double): elevation below which interval will switch to fineCheckInterval (typically
                DEFAULT_ELEVATION_SWITCH_SUP
                which is +15°)
            fineCheckInterval (double): check interval to use when elevation is between elevationSwitchInf and elevationSwitchSup
        
        Returns:
            adaptable interval for detection of elevation with respect to topo
        
        Since:
            13.0
        
        
        """
        ...

_FieldAdaptableInterval__T = typing.TypeVar('_FieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdaptableInterval(typing.Generic[_FieldAdaptableInterval__T]):
    """
    This interface represents an event checking interval that depends on state.
    
    Since:
        12.0
    
    Also see:
        FieldEventDetector
    """
    def currentInterval(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldAdaptableInterval__T], isForward: bool) -> float:
        """
        Get the current value of maximal time interval between events handler checks.
        
        Parameters:
            state (FieldSpacecraftState<FieldAdaptableInterval> state): current state
            isForward (boolean): direction of propagation
        
        Returns:
            current value of maximal time interval between events handler checks (only as a double)
        
        
        """
        ...
    _of_0__T = typing.TypeVar('_of_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_1__T = typing.TypeVar('_of_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_2__T = typing.TypeVar('_of_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def of(double: float) -> 'FieldAdaptableInterval'[_of_0__T]:
        """
        Method creating a constant interval provider.
        
        Parameters:
            constantInterval (double): value of constant interval
        
        Returns:
            adaptable interval ready to be added to an event detector
        
        Since:
            12.1
        
        Method creating an interval provider from a non-Field one.
        
        Parameters:
            adaptableInterval (AdaptableInterval): non-Field interval
        
        Returns:
            adaptable interval ready to be added to an event detector
        
        Since:
            13.0
        
        SafeVarargs static <T extends CalculusFieldElement<T>> FieldAdaptableInterval<T> of (double defaultMaxCheck, FieldAdaptableInterval<T>... adaptableIntervals)
        
        Method creating an interval taking the minimum value of all candidates.
        
        Parameters:
            defaultMaxCheck (double): default value if no intervals is given as inputv
            adaptableIntervals (FieldAdaptableInterval<T>...): intervals
        
        Returns:
            adaptable interval ready to be added to an event detector
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(double: float, *fieldAdaptableInterval: typing.Union['FieldAdaptableInterval'[_of_1__T], typing.Callable[[org.orekit.propagation.FieldSpacecraftState[org.hipparchus.CalculusFieldElement], bool], float]]) -> 'FieldAdaptableInterval'[_of_1__T]: ...
    @typing.overload
    @staticmethod
    def of(adaptableInterval: typing.Union[AdaptableInterval, typing.Callable]) -> 'FieldAdaptableInterval'[_of_2__T]: ...

class PythonAdaptableInterval(AdaptableInterval):
    def __init__(self): ...
    def currentInterval(self, state: org.orekit.propagation.SpacecraftState, isForward: bool) -> float:
        """
        Get the current value of maximal time interval between events handler checks.
        
        Specified by: currentInterval in interface AdaptableInterval
        
        Parameters:
            state (SpacecraftState): current state
            isForward (boolean): direction of propagation
        
        Returns:
            current value of maximal time interval between events handler checks
        
        
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

_PythonFieldAdaptableInterval__T = typing.TypeVar('_PythonFieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdaptableInterval(FieldAdaptableInterval[_PythonFieldAdaptableInterval__T], typing.Generic[_PythonFieldAdaptableInterval__T]):
    def __init__(self): ...
    def currentInterval(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdaptableInterval__T], isForward: bool) -> float:
        """
        Get the current value of maximal time interval between events handler checks.
        
        Specified by: currentInterval in interface FieldAdaptableInterval
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldAdaptableInterval> state): current state
            isForward (boolean): direction of propagation
        
        Returns:
            current value of maximal time interval between events handler checks (only as a double)
        
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events.intervals")``.

    AdaptableInterval: typing.Type[AdaptableInterval]
    ApsideDetectionAdaptableIntervalFactory: typing.Type[ApsideDetectionAdaptableIntervalFactory]
    DateDetectionAdaptableIntervalFactory: typing.Type[DateDetectionAdaptableIntervalFactory]
    ElevationDetectionAdaptableIntervalFactory: typing.Type[ElevationDetectionAdaptableIntervalFactory]
    FieldAdaptableInterval: typing.Type[FieldAdaptableInterval]
    PythonAdaptableInterval: typing.Type[PythonAdaptableInterval]
    PythonFieldAdaptableInterval: typing.Type[PythonFieldAdaptableInterval]
