
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
    :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.FunctionalInterface?is` public interface AdaptableInterval
    
        This interface represents an event checking interval that depends on state.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.propagation.events.EventDetector`
    """
    def currentInterval(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> float:
        """
            Get the current value of maximal time interval between events handler checks.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
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
                adaptableIntervals (:class:`~org.orekit.propagation.events.intervals.AdaptableInterval`...): intervals
        
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
    public class ApsideDetectionAdaptableIntervalFactory extends :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory class for :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` suitable for apside detection on
        eccentric orbits. It requires :class:`~org.orekit.propagation.SpacecraftState` to be based on
        :class:`~org.orekit.orbits.Orbit` in order to work.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.events.intervals.AdaptableInterval`,
            :class:`~org.orekit.propagation.events.ApsideDetector`, :class:`~org.orekit.propagation.events.EventSlopeFilter`
    """
    @staticmethod
    def computeKeplerianDurationFromPreviousApoapsis(double: float, double2: float) -> float:
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
    def computeKeplerianDurationFromPreviousPeriapsis(double: float, double2: float) -> float:
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
            Method providing a candidate :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` for apoapsis detection.
            It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for apoapsis detection
        
        
        """
        ...
    @staticmethod
    def getApsideDetectionAdaptableInterval() -> AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` for arbitrary apside
            detection. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for apside detection
        
        
        """
        ...
    @staticmethod
    def getPeriapsisDetectionAdaptableInterval() -> AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` for periapsis
            detection. It uses a Keplerian, eccentric approximation.
        
            Returns:
                adaptable interval for periaspsis detection
        
        
        """
        ...

class DateDetectionAdaptableIntervalFactory:
    """
    public class DateDetectionAdaptableIntervalFactory extends :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory for adaptable interval tuned for date(s) detection.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.propagation.events.DateDetector`, :class:`~org.orekit.propagation.events.FieldDateDetector`
    """
    DEFAULT_MAX_CHECK: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MAX_CHECK
    
        Default value for max check.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def getDatesDetectionConstantInterval(*timeStamped: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> AdaptableInterval:
        """
            Return a candidate :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` for multiple dates detection with
            a constant max. check.
        
            Parameters:
                timeStampeds (:class:`~org.orekit.time.TimeStamped`...): event dates
        
            Returns:
                adaptable interval
        
        
        """
        ...
    _getDatesDetectionFieldConstantInterval__T = typing.TypeVar('_getDatesDetectionFieldConstantInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getDatesDetectionFieldConstantInterval(*fieldTimeStamped: typing.Union[org.orekit.time.FieldTimeStamped[_getDatesDetectionFieldConstantInterval__T], typing.Callable[[], org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement]]]) -> 'FieldAdaptableInterval'[_getDatesDetectionFieldConstantInterval__T]: ...
    _getDatesDetectionFieldInterval__T = typing.TypeVar('_getDatesDetectionFieldInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getDatesDetectionFieldInterval(*fieldTimeStamped: typing.Union[org.orekit.time.FieldTimeStamped[_getDatesDetectionFieldInterval__T], typing.Callable[[], org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement]]]) -> 'FieldAdaptableInterval'[_getDatesDetectionFieldInterval__T]: ...
    @staticmethod
    def getDatesDetectionInterval(*timeStamped: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> AdaptableInterval:
        """
            Return a candidate :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` for multiple dates detection.
        
            Parameters:
                timeStampeds (:class:`~org.orekit.time.TimeStamped`...): event dates
        
            Returns:
                adaptable interval
        
        
        """
        ...
    @staticmethod
    def getMinGap(*timeStamped: typing.Union[org.orekit.time.TimeStamped, typing.Callable]) -> float:
        """
            Compute min. gap between dated objects if applicable. It ignores duplicates.
        
            Parameters:
                timeStampeds (:class:`~org.orekit.time.TimeStamped`...): time stamped objects
        
            Returns:
                minimum gap
        
        
        """
        ...
    @staticmethod
    def getSingleDateDetectionAdaptableInterval() -> AdaptableInterval:
        """
            Return a candidate :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` for single date detection.
        
            Returns:
                adaptable interval
        
        
        """
        ...
    _getSingleDateDetectionFieldAdaptableInterval__T = typing.TypeVar('_getSingleDateDetectionFieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getSingleDateDetectionFieldAdaptableInterval() -> 'FieldAdaptableInterval'[_getSingleDateDetectionFieldAdaptableInterval__T]:
        """
            Return a candidate :class:`~org.orekit.propagation.events.intervals.FieldAdaptableInterval` for single date detection.
        
            Returns:
                adaptable interval
        
        
        """
        ...

class ElevationDetectionAdaptableIntervalFactory:
    """
    public class ElevationDetectionAdaptableIntervalFactory extends :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory class for :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` suitable for elevation detection
        on eccentric orbits. It requires :class:`~org.orekit.propagation.SpacecraftState` to be based on
        :class:`~org.orekit.orbits.Orbit` in order to work.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.events.intervals.AdaptableInterval`,
            :class:`~org.orekit.propagation.events.ApsideDetector`, :class:`~org.orekit.propagation.events.EventSlopeFilter`
    """
    DEFAULT_ELEVATION_SWITCH_INF: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ELEVATION_SWITCH_INF
    
        Default elevation above which interval should be switched to fine interval (-5°).
    
        Since:
            13.0
    
    
    """
    DEFAULT_ELEVATION_SWITCH_SUP: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ELEVATION_SWITCH_SUP
    
        Default elevation below which interval should be switched to fine interval (+15°).
    
        Since:
            13.0
    
    
    """
    @staticmethod
    def getAdaptableInterval(topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, double2: float, double3: float) -> AdaptableInterval:
        """
            Method providing a candidate :class:`~org.orekit.propagation.events.intervals.AdaptableInterval` for arbitrary elevation
            detection with forward propagation. It uses a Keplerian, eccentric approximation.
        
            Parameters:
                topo (:class:`~org.orekit.frames.TopocentricFrame`): topocentric frame centered at ground interest point
                elevationSwitchInf (double): elevation above which interval will switch to :code:`fineCheckInterval` (typically
                    :meth:`~org.orekit.propagation.events.intervals.ElevationDetectionAdaptableIntervalFactory.DEFAULT_ELEVATION_SWITCH_INF`
                    which is -5°)
                elevationSwitchSup (double): elevation below which interval will switch to :code:`fineCheckInterval` (typically
                    :meth:`~org.orekit.propagation.events.intervals.ElevationDetectionAdaptableIntervalFactory.DEFAULT_ELEVATION_SWITCH_SUP`
                    which is +15°)
                fineCheckInterval (double): check interval to use when elevation is between :code:`elevationSwitchInf` and :code:`elevationSwitchSup`
        
            Returns:
                adaptable interval for detection of elevation with respect to :code:`topo`
        
            Since:
                13.0
        
        
        """
        ...

_FieldAdaptableInterval__T = typing.TypeVar('_FieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdaptableInterval(typing.Generic[_FieldAdaptableInterval__T]):
    """
    :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.FunctionalInterface?is` public interface FieldAdaptableInterval<T extends :class:`~org.orekit.propagation.events.intervals.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        This interface represents an event checking interval that depends on state.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.propagation.events.FieldEventDetector`
    """
    def currentInterval(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAdaptableInterval__T], boolean: bool) -> float: ...
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
                adaptableInterval (:class:`~org.orekit.propagation.events.intervals.AdaptableInterval`): non-Field interval
        
            Returns:
                adaptable interval ready to be added to an event detector
        
            Since:
                13.0
        
        :class:`~org.orekit.propagation.events.intervals.https:.docs.oracle.com.javase.8.docs.api.java.lang.SafeVarargs?is` static <T extends :class:`~org.orekit.propagation.events.intervals.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> :class:`~org.orekit.propagation.events.intervals.FieldAdaptableInterval`<T> of (double defaultMaxCheck, :class:`~org.orekit.propagation.events.intervals.FieldAdaptableInterval`<T>... adaptableIntervals)
        
            Method creating an interval taking the minimum value of all candidates.
        
            Parameters:
                defaultMaxCheck (double): default value if no intervals is given as inputv
                adaptableIntervals (:class:`~org.orekit.propagation.events.intervals.FieldAdaptableInterval`<T>...): intervals
        
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
    def currentInterval(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> float: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldAdaptableInterval__T = typing.TypeVar('_PythonFieldAdaptableInterval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdaptableInterval(FieldAdaptableInterval[_PythonFieldAdaptableInterval__T], typing.Generic[_PythonFieldAdaptableInterval__T]):
    def __init__(self): ...
    def currentInterval(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdaptableInterval__T], boolean: bool) -> float: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.events.intervals")``.

    AdaptableInterval: typing.Type[AdaptableInterval]
    ApsideDetectionAdaptableIntervalFactory: typing.Type[ApsideDetectionAdaptableIntervalFactory]
    DateDetectionAdaptableIntervalFactory: typing.Type[DateDetectionAdaptableIntervalFactory]
    ElevationDetectionAdaptableIntervalFactory: typing.Type[ElevationDetectionAdaptableIntervalFactory]
    FieldAdaptableInterval: typing.Type[FieldAdaptableInterval]
    PythonAdaptableInterval: typing.Type[PythonAdaptableInterval]
    PythonFieldAdaptableInterval: typing.Type[PythonFieldAdaptableInterval]
