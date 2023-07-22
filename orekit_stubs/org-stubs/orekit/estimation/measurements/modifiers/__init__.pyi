import java.util
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.gnss
import org.orekit.models
import org.orekit.models.earth.ionosphere
import org.orekit.models.earth.troposphere
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.utils
import typing



class AbstractAmbiguityModifier:
    """
    public class AbstractAmbiguityModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for phase ambiguity modifier.
    
        Since:
            10.3
    """
    def __init__(self, int: int, double: float): ...

class AbstractRelativisticClockModifier:
    """
    public class AbstractRelativisticClockModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class modifying theoretical measurements with relativistic clock correction.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self): ...

class AbstractRelativisticJ2ClockModifier:
    """
    public class AbstractRelativisticJ2ClockModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class modifying theoretical measurements with relativistic J2 clock correction.
    
        Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
        The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
        Since:
            11.2
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Equation 19.18 Springer, 2017."
    """
    def __init__(self, double: float, double2: float, double3: float): ...

class AbstractShapiroBaseModifier:
    """
    public class AbstractShapiroBaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class modifying theoretical range measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.0
    """
    def __init__(self, double: float): ...

class AngularIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    """
    public class AngularIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
        Class modifying theoretical angular measurement with ionospheric delay. The effect of ionospheric correction on the
        angular measurement is computed through the computation of the ionospheric delay. The spacecraft state is shifted by the
        computed delay time and elevation and azimuth are computed again with the new spacecraft state. The ionospheric delay
        depends on the frequency of the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the ray is not affected
        by ionosphere charged particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            8.0
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.AngularAzEl]) -> None: ...

class AngularRadioRefractionModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    """
    public class AngularRadioRefractionModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
        Class modifying theoretical angular measurement with ionospheric radio refractive index. A radio ray passing through the
        lower (non-ionized) layer of the atmosphere undergoes bending caused by the gradient of the relative index. Since the
        refractive index varies mainly with altitude, only the vertical gradient of the refractive index is considered here. The
        effect of ionospheric correction on the angular measurement is computed directly through the computation of the apparent
        elevation angle. Recommendation ITU-R P.453-11 (07/2015) and Recommendation ITU-R P.834-7 (10/2015)
    
        Since:
            8.0
    """
    def __init__(self, atmosphericRefractionModel: org.orekit.models.AtmosphericRefractionModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.AngularAzEl]) -> None: ...

class AngularTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    """
    public class AngularTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
        Class modifying theoretical angular measurement with tropospheric delay. The effect of tropospheric correction on the
        angular is computed through the computation of the tropospheric delay.The spacecraft state is shifted by the computed
        delay time and elevation and azimuth are computed again with the new spacecraft state. In general, for GNSS, VLBI, ...
        there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is
        sensitive.
    
        Since:
            8.0
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.AngularAzEl]) -> None: ...

class BaseRangeIonosphericDelayModifier:
    """
    public abstract class BaseRangeIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class modifying theoretical range measurement with ionospheric delay. The effect of ionospheric correction on the
        range is directly computed through the computation of the ionospheric delay. The ionospheric delay depends on the
        frequency of the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere
        charged particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            11.2
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class BaseRangeRateIonosphericDelayModifier:
    """
    public abstract class BaseRangeRateIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class modifying theoretical range-rate measurement with ionospheric delay. The effect of ionospheric correction on
        the range-rate is directly computed through the computation of the ionospheric delay difference with respect to time.
        The ionospheric delay depends on the frequency of the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the
        ray is not affected by ionosphere charged particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            11.2
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class BaseRangeRateTroposphericDelayModifier:
    """
    public abstract class BaseRangeRateTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Baselass modifying theoretical range-rate measurements with tropospheric delay. The effect of tropospheric correction on
        the range-rate is directly computed through the computation of the tropospheric delay difference with respect to time.
        In general, for GNSS, VLBI, ... there is hardly any frequency dependence in the delay. For SLR techniques however, the
        frequency dependence is sensitive.
    
        Since:
            11.2
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _rangeRateErrorTroposphericModel_1__T = typing.TypeVar('_rangeRateErrorTroposphericModel_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rangeRateErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the measurement error due to Troposphere.
        
            Parameters:
                station (:class:`~org.orekit.estimation.measurements.GroundStation`): station
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                the measurement error due to Troposphere
        
        """
        ...
    @typing.overload
    def rangeRateErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_rangeRateErrorTroposphericModel_1__T], tArray: typing.List[_rangeRateErrorTroposphericModel_1__T]) -> _rangeRateErrorTroposphericModel_1__T:
        """
            Compute the measurement error due to Troposphere.
        
            Parameters:
                station (:class:`~org.orekit.estimation.measurements.GroundStation`): station
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                parameters (T[]): tropospheric model parameters
        
            Returns:
                the measurement error due to Troposphere
        
        
        """
        ...

class BaseRangeTroposphericDelayModifier:
    """
    public abstract class BaseRangeTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class modifying theoretical range measurements with tropospheric delay. The effect of tropospheric correction on
        the range is directly computed through the computation of the tropospheric delay. In general, for GNSS, VLBI, ... there
        is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
        Since:
            11.2
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _rangeErrorTroposphericModel_1__T = typing.TypeVar('_rangeErrorTroposphericModel_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rangeErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the measurement error due to Troposphere.
        
            Parameters:
                station (:class:`~org.orekit.estimation.measurements.GroundStation`): station
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                the measurement error due to Troposphere
        
        """
        ...
    @typing.overload
    def rangeErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_rangeErrorTroposphericModel_1__T], tArray: typing.List[_rangeErrorTroposphericModel_1__T]) -> _rangeErrorTroposphericModel_1__T:
        """
            Compute the measurement error due to Troposphere.
        
            Parameters:
                station (:class:`~org.orekit.estimation.measurements.GroundStation`): station
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                parameters (T[]): tropospheric model parameters
        
            Returns:
                the measurement error due to Troposphere
        
        
        """
        ...

_Bias__T = typing.TypeVar('_Bias__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class Bias(org.orekit.estimation.measurements.EstimationModifier[_Bias__T], typing.Generic[_Bias__T]):
    """
    public class Bias<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<T>
    
        Class modeling a measurement bias.
    
        Since:
            8.0
    """
    def __init__(self, stringArray: typing.List[str], doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], doubleArray4: typing.List[float]): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_Bias__T]) -> None: ...

class ModifierGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter):
    """
    public class ModifierGradientConverter extends :class:`~org.orekit.propagation.integration.AbstractGradientConverter`
    
        Converter for states and parameters arrays.
    
        Since:
            11.2
    """
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...

class OnBoardAntennaInterSatellitesPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class OnBoardAntennaInterSatellitesPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        On-board antenna offset effect on inter-satellites phase measurements.
    
        Since:
            10.3
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class OnBoardAntennaInterSatellitesRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    public class OnBoardAntennaInterSatellitesRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        On-board antenna offset effect on inter-satellites range measurements.
    
        Since:
            9.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class OnBoardAntennaOneWayGNSSPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    public class OnBoardAntennaOneWayGNSSPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        On-board antenna offset effect on one-way GNSS phase measurements.
    
        Since:
            10.3
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class OnBoardAntennaOneWayGNSSRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    public class OnBoardAntennaOneWayGNSSRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange`>
    
        On-board antenna offset effect on one-way GNSS range measurements.
    
        Since:
            10.3
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class OnBoardAntennaPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class OnBoardAntennaPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        On-board antenna offset effect on phase measurements.
    
        Since:
            10.2
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class OnBoardAntennaRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class OnBoardAntennaRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        On-board antenna offset effect on range measurements.
    
        Since:
            9.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class OnBoardAntennaTurnAroundRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    public class OnBoardAntennaTurnAroundRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
        On-board antenna offset effect on turn around range measurements.
    
        Since:
            9.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None: ...

_OutlierFilter__T = typing.TypeVar('_OutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class OutlierFilter(org.orekit.estimation.measurements.EstimationModifier[_OutlierFilter__T], typing.Generic[_OutlierFilter__T]):
    """
    public class OutlierFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<T>
    
        Modifier that sets estimated measurement weight to 0 if residual is too far from expected domain.
    
        Since:
            8.0
    """
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_OutlierFilter__T]) -> None: ...

class PhaseIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class PhaseIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modifying theoretical phase measurement with ionospheric delay. The effect of ionospheric correction on the phase
        is directly computed through the computation of the ionospheric delay.
    
        Since:
            10.2
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class PhaseTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class PhaseTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modifying theoretical phase measurement with tropospheric delay. The effect of tropospheric correction on the
        phase is directly computed through the computation of the tropospheric delay.
    
        Since:
            10.2
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class RangeModifierUtil:
    """
    public class RangeModifierUtil extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility class modifying theoretical range measurement.
    
        Since:
            11.2
    """
    _modify__T = typing.TypeVar('_modify__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def modify(estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_modify__T], parametersDriversProvider: org.orekit.utils.ParametersDriversProvider, abstractGradientConverter: org.orekit.propagation.integration.AbstractGradientConverter, groundStation: org.orekit.estimation.measurements.GroundStation, parametricModelEffect: typing.Union['ParametricModelEffect', typing.Callable], parametricModelEffectGradient: typing.Union['ParametricModelEffectGradient', typing.Callable]) -> None:
        """
            Apply a modifier to an estimated measurement.
        
            Parameters:
                estimated (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement`<T> estimated): estimated measurement to modify
                station (:class:`~org.orekit.utils.ParametersDriversProvider`): ground station
                converter (:class:`~org.orekit.propagation.integration.AbstractGradientConverter`): gradient converter
                parametricModel (:class:`~org.orekit.estimation.measurements.GroundStation`): parametric modifier model
                modelEffect (org.orekit.estimation.measurements.modifiers.ParametricModelEffect): model effect
                modelEffectGradient (org.orekit.estimation.measurements.modifiers.ParametricModelEffectGradient): model effect gradient
        
        
        """
        ...

class RangeRateModifierUtil:
    """
    public class RangeRateModifierUtil extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility class modifying theoretical range-rate measurement.
    
        Since:
            11.2
    """
    _modify__T = typing.TypeVar('_modify__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def modify(estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_modify__T], parametersDriversProvider: org.orekit.utils.ParametersDriversProvider, abstractGradientConverter: org.orekit.propagation.integration.AbstractGradientConverter, groundStation: org.orekit.estimation.measurements.GroundStation, parametricModelEffect: typing.Union['ParametricModelEffect', typing.Callable], parametricModelEffectGradient: typing.Union['ParametricModelEffectGradient', typing.Callable]) -> None:
        """
            Apply a modifier to an estimated measurement.
        
            Parameters:
                estimated (:class:`~org.orekit.estimation.measurements.EstimatedMeasurement`<T> estimated): estimated measurement to modify
                station (:class:`~org.orekit.utils.ParametersDriversProvider`): ground station
                converter (:class:`~org.orekit.propagation.integration.AbstractGradientConverter`): gradient converter
                parametricModel (:class:`~org.orekit.estimation.measurements.GroundStation`): parametric modifier model
                modelEffect (org.orekit.estimation.measurements.modifiers.ParametricModelEffect): model effect
                modelEffectGradient (org.orekit.estimation.measurements.modifiers.ParametricModelEffectGradient): model effect gradient
        
        
        """
        ...

class TDOAIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TDOA]):
    """
    public class TDOAIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TDOA`>
    
        Class modifying theoretical TDOA measurements with ionospheric delay.
    
        The effect of ionospheric correction on the TDOA is a time delay computed directly from the difference in ionospheric
        delays for each downlink.
    
        The ionospheric delay depends on the frequency of the signal.
    
        Since:
            11.2
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TDOA]) -> None: ...

class TDOATroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TDOA]):
    """
    public class TDOATroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TDOA`>
    
        Class modifying theoretical TDOA measurements with tropospheric delay.
    
        The effect of tropospheric correction on the TDOA is a time delay computed directly from the difference in tropospheric
        delays for each downlink.
    
        Tropospheric delay is not frequency dependent for signals up to 15 GHz.
    
        Since:
            11.2
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TDOA]) -> None: ...

class TurnAroundRangeIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    public class TurnAroundRangeIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
        Class modifying theoretical TurnAroundRange measurement with ionospheric delay. The effect of ionospheric correction on
        the TurnAroundRange is directly computed through the computation of the ionospheric delay. The ionospheric delay depends
        on the frequency of the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the ray is not affected by
        ionosphere charged particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            9.0
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None: ...

class TurnAroundRangeTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    public class TurnAroundRangeTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
        Class modifying theoretical turn-around TurnAroundRange measurement with tropospheric delay. The effect of tropospheric
        correction on the TurnAroundRange is directly computed through the computation of the tropospheric delay. In general,
        for GNSS, VLBI, ... there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency
        dependence is sensitive.
    
        Since:
            9.0
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None: ...

class ParametricModelEffect: ...

class ParametricModelEffectGradient: ...

class BistaticRangeIonosphericDelayModifier(BaseRangeIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRange]):
    """
    public class BistaticRangeIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeIonosphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.BistaticRange`>
    
        Class modifying theoretical bistatic range measurement with ionospheric delay. The effect of ionospheric correction on
        the range is directly computed through the computation of the ionospheric delay.
    
        The ionospheric delay depends on the frequency of the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the
        ray is not affected by ionosphere charged particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            11.2
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRange]) -> None: ...

class BistaticRangeRateIonosphericDelayModifier(BaseRangeRateIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRangeRate]):
    """
    public class BistaticRangeRateIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateIonosphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.BistaticRangeRate`>
    
        Class modifying theoretical bistatic range-rate measurement with ionospheric delay.
    
        The effect of ionospheric correction on the bistatic range-rate is directly computed through the computation of the
        ionospheric delay difference with respect to time.
    
        The ionospheric delay depends on the frequency of the signal.
    
        Since:
            11.2
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRangeRate]) -> None: ...

class BistaticRangeRateTroposphericDelayModifier(BaseRangeRateTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRangeRate]):
    """
    public class BistaticRangeRateTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.BistaticRangeRate`>
    
        Class modifying theoretical bistatic range-rate measurements with tropospheric delay.
    
        The effect of tropospheric correction on the bistatic range-rate is directly computed through the computation of the
        tropospheric delay difference with respect to time.
    
        Tropospheric delay is not frequency dependent for signals up to 15 GHz.
    
        Since:
            11.2
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRangeRate]) -> None: ...

class BistaticRangeTroposphericDelayModifier(BaseRangeTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRange]):
    """
    public class BistaticRangeTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeTroposphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.BistaticRange`>
    
        Class modifying theoretical bistatic range measurement with tropospheric delay. The effect of tropospheric correction on
        the range is directly computed through the computation of the tropospheric delay. In general, for GNSS, VLBI, ... there
        is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
        Since:
            11.2
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRange]) -> None: ...

_DynamicOutlierFilter__T = typing.TypeVar('_DynamicOutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class DynamicOutlierFilter(OutlierFilter[_DynamicOutlierFilter__T], typing.Generic[_DynamicOutlierFilter__T]):
    """
    public class DynamicOutlierFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.modifiers.OutlierFilter`<T>
    
        Modifier that sets estimated measurement weight to 0 if residual is too far from expected domain. The "dynamic" aspect
        comes from the fact that the value of sigma can be changed on demand. This is mainly used when searching for outliers in
        Kalman filters' prediction phase. The value of sigma is then set to the square root of the diagonal of the matrix
        (H.Ppred.Ht+R) Note that in the case of the Kalman filter we use the "iteration" word to represent the number of
        measurements processed by the filter so far.
    
        Since:
            9.2
    """
    def __init__(self, int: int, double: float): ...
    def getSigma(self) -> typing.List[float]:
        """
            Get the current value of sigma.
        
            Returns:
                The current value of sigma
        
        
        """
        ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_DynamicOutlierFilter__T]) -> None: ...
    def setSigma(self, doubleArray: typing.List[float]) -> None:
        """
            Set the current value of sigma.
        
            Parameters:
                sigma (double[]): The value of sigma to set
        
        
        """
        ...

class InterSatellitesPhaseAmbiguityModifier(AbstractAmbiguityModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class InterSatellitesPhaseAmbiguityModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractAmbiguityModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Class modifying theoretical inter-satellites phase measurement with ambiguity.
    
        Since:
            10.3
    """
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class IonosphericGradientConverter(ModifierGradientConverter):
    """
    :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class IonosphericGradientConverter extends :class:`~org.orekit.estimation.measurements.modifiers.ModifierGradientConverter`
    
        Deprecated.
        as of 11.2, replaced by :class:`~org.orekit.estimation.measurements.modifiers.ModifierGradientConverter`
        Converter for states and parameters arrays.
    
        Since:
            10.2
    """
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...

class OneWayGNSSPhaseAmbiguityModifier(AbstractAmbiguityModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    public class OneWayGNSSPhaseAmbiguityModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractAmbiguityModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        Class modifying theoretical one-way GNSS phase measurement with ambiguity.
    
        Since:
            10.3
    """
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class PhaseAmbiguityModifier(AbstractAmbiguityModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class PhaseAmbiguityModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractAmbiguityModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modifying theoretical phase measurement with ambiguity.
    
        Since:
            9.2
    """
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class PythonParametricModelEffect(ParametricModelEffect):
    """
    public class PythonParametricModelEffect extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    """
    def __init__(self): ...
    def evaluate(self, groundStation: org.orekit.estimation.measurements.GroundStation, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Evaluate the parametric model effect.
        
            Parameters:
                station (:class:`~org.orekit.estimation.measurements.GroundStation`): station
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                the measurement error due to parametric model
        
        
        """
        ...
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

class PythonParametricModelEffectGradient(ParametricModelEffectGradient):
    """
    public class PythonParametricModelEffectGradient extends :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    """
    def __init__(self): ...
    def evaluate(self, groundStation: org.orekit.estimation.measurements.GroundStation, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], gradientArray: typing.List[org.hipparchus.analysis.differentiation.Gradient]) -> org.hipparchus.analysis.differentiation.Gradient: ...
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

class RangeIonosphericDelayModifier(BaseRangeIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class RangeIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeIonosphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modifying theoretical range measurement with ionospheric delay. The effect of ionospheric correction on the range
        is directly computed through the computation of the ionospheric delay. The ionospheric delay depends on the frequency of
        the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged
        particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            8.0
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class RangeRateIonosphericDelayModifier(BaseRangeRateIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    public class RangeRateIonosphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateIonosphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Class modifying theoretical range-rate measurement with ionospheric delay. The effect of ionospheric correction on the
        range-rate is directly computed through the computation of the ionospheric delay difference with respect to time. The
        ionospheric delay depends on the frequency of the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the ray
        is not affected by ionosphere charged particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            8.0
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float, boolean: bool): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...

class RangeRateTroposphericDelayModifier(BaseRangeRateTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    public class RangeRateTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Class modifying theoretical range-rate measurements with tropospheric delay. The effect of tropospheric correction on
        the range-rate is directly computed through the computation of the tropospheric delay difference with respect to time.
        In general, for GNSS, VLBI, ... there is hardly any frequency dependence in the delay. For SLR techniques however, the
        frequency dependence is sensitive.
    
        Since:
            8.0
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel, boolean: bool): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...
    _rangeRateErrorTroposphericModel_1__T = typing.TypeVar('_rangeRateErrorTroposphericModel_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rangeRateErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the measurement error due to Troposphere.
        
            Overrides:
                
                meth:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier.rangeRateErrorTroposphericModel` in
                class :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier`
        
            Parameters:
                station (:class:`~org.orekit.estimation.measurements.GroundStation`): station
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                the measurement error due to Troposphere
        
        """
        ...
    @typing.overload
    def rangeRateErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_rangeRateErrorTroposphericModel_1__T], tArray: typing.List[_rangeRateErrorTroposphericModel_1__T]) -> _rangeRateErrorTroposphericModel_1__T:
        """
            Compute the measurement error due to Troposphere.
        
            Overrides:
                
                meth:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier.rangeRateErrorTroposphericModel` in
                class :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier`
        
            Parameters:
                station (:class:`~org.orekit.estimation.measurements.GroundStation`): station
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                parameters (T[]): tropospheric model parameters
        
            Returns:
                the measurement error due to Troposphere
        
        
        """
        ...

class RangeTroposphericDelayModifier(BaseRangeTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class RangeTroposphericDelayModifier extends :class:`~org.orekit.estimation.measurements.modifiers.BaseRangeTroposphericDelayModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modifying theoretical range measurement with tropospheric delay. The effect of tropospheric correction on the
        range is directly computed through the computation of the tropospheric delay. In general, for GNSS, VLBI, ... there is
        hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
        Since:
            8.0
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class RelativisticClockInterSatellitesPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class RelativisticClockInterSatellitesPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Class modifying theoretical inter-satellites phase measurement with relativistic clock correction.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class RelativisticClockInterSatellitesRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    public class RelativisticClockInterSatellitesRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        Class modifying theoretical inter-satellites range measurement with relativistic clock correction.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class RelativisticClockOneWayGNSSPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    public class RelativisticClockOneWayGNSSPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        Class modifying theoretical one-way GNSS phase measurement with relativistic clock correction.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class RelativisticClockOneWayGNSSRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    public class RelativisticClockOneWayGNSSRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange`>
    
        Class modifying theoretical one-way GNSS range measurement with relativistic clock correction.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class RelativisticClockPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class RelativisticClockPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modifying theoretical phase measurement with relativistic clock correction.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class RelativisticClockRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class RelativisticClockRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modifying theoretical range measurement with relativistic clock correction.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class RelativisticClockRangeRateModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    public class RelativisticClockRangeRateModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Class modifying theoretical range-rate measurement with relativistic frequency deviation.
    
        Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational
        potential
    
        Since:
            10.3
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Springer, 2017."
    """
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...

class RelativisticJ2ClockInterSatellitesPhaseModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class RelativisticJ2ClockInterSatellitesPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticJ2ClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Class modifying theoretical inter-satellites phase measurements with relativistic J2 clock correction.
    
        Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
        The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
        Since:
            11.2
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Equation 19.18 Springer, 2017."
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class RelativisticJ2ClockInterSatellitesRangeModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    public class RelativisticJ2ClockInterSatellitesRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticJ2ClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        Class modifying theoretical inter-satellites range measurements with relativistic J2 clock correction.
    
        Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
        The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
        Since:
            11.2
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Equation 19.18 Springer, 2017."
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class RelativisticJ2ClockOneWayGNSSPhaseModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    public class RelativisticJ2ClockOneWayGNSSPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticJ2ClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        Class modifying theoretical one-way phase measurements with relativistic J2 clock correction.
    
        Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
        The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
        Since:
            11.2
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Equation 19.18 Springer, 2017."
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class RelativisticJ2ClockOneWayGNSSRangeModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    public class RelativisticJ2ClockOneWayGNSSRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticJ2ClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange`>
    
        Class modifying one-way GNSS range theoretical measurements with relativistic J2 clock correction.
    
        Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
        The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
        Since:
            11.2
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Equation 19.18 Springer, 2017."
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class RelativisticJ2ClockPhaseModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class RelativisticJ2ClockPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticJ2ClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modifying theoretical phase measurements with relativistic J2 clock correction.
    
        Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
        The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
        Since:
            11.2
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Equation 19.18 Springer, 2017."
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class RelativisticJ2ClockRangeModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class RelativisticJ2ClockRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractRelativisticJ2ClockModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modifying theoretical range measurements with relativistic J2 clock correction.
    
        Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
        The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
        Since:
            11.2
    
        Also see:
            "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
            Equation 19.18 Springer, 2017."
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class ShapiroInterSatellitePhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class ShapiroInterSatellitePhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractShapiroBaseModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        Class modifying theoretical inter-satellites phase measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.3
    """
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class ShapiroInterSatelliteRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    public class ShapiroInterSatelliteRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractShapiroBaseModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        Class modifying theoretical range measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.0
    """
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class ShapiroOneWayGNSSPhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    public class ShapiroOneWayGNSSPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractShapiroBaseModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        Class modifying theoretical one-way GNSS phase measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.3
    """
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class ShapiroOneWayGNSSRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    public class ShapiroOneWayGNSSRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractShapiroBaseModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange`>
    
        Class modifying theoretical range measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.3
    """
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class ShapiroPhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class ShapiroPhaseModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractShapiroBaseModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modifying theoretical phase measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.2
    """
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class ShapiroRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class ShapiroRangeModifier extends :class:`~org.orekit.estimation.measurements.modifiers.AbstractShapiroBaseModifier` implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modifying theoretical range measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.0
    """
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class TroposphericGradientConverter(ModifierGradientConverter):
    """
    :class:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Deprecated?is` public class TroposphericGradientConverter extends :class:`~org.orekit.estimation.measurements.modifiers.ModifierGradientConverter`
    
        Deprecated.
        as of 11.2, replaced by :class:`~org.orekit.estimation.measurements.modifiers.ModifierGradientConverter`
        Converter for states and parameters arrays.
    
        Since:
            10.2
    """
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.modifiers")``.

    AbstractAmbiguityModifier: typing.Type[AbstractAmbiguityModifier]
    AbstractRelativisticClockModifier: typing.Type[AbstractRelativisticClockModifier]
    AbstractRelativisticJ2ClockModifier: typing.Type[AbstractRelativisticJ2ClockModifier]
    AbstractShapiroBaseModifier: typing.Type[AbstractShapiroBaseModifier]
    AngularIonosphericDelayModifier: typing.Type[AngularIonosphericDelayModifier]
    AngularRadioRefractionModifier: typing.Type[AngularRadioRefractionModifier]
    AngularTroposphericDelayModifier: typing.Type[AngularTroposphericDelayModifier]
    BaseRangeIonosphericDelayModifier: typing.Type[BaseRangeIonosphericDelayModifier]
    BaseRangeRateIonosphericDelayModifier: typing.Type[BaseRangeRateIonosphericDelayModifier]
    BaseRangeRateTroposphericDelayModifier: typing.Type[BaseRangeRateTroposphericDelayModifier]
    BaseRangeTroposphericDelayModifier: typing.Type[BaseRangeTroposphericDelayModifier]
    Bias: typing.Type[Bias]
    BistaticRangeIonosphericDelayModifier: typing.Type[BistaticRangeIonosphericDelayModifier]
    BistaticRangeRateIonosphericDelayModifier: typing.Type[BistaticRangeRateIonosphericDelayModifier]
    BistaticRangeRateTroposphericDelayModifier: typing.Type[BistaticRangeRateTroposphericDelayModifier]
    BistaticRangeTroposphericDelayModifier: typing.Type[BistaticRangeTroposphericDelayModifier]
    DynamicOutlierFilter: typing.Type[DynamicOutlierFilter]
    InterSatellitesPhaseAmbiguityModifier: typing.Type[InterSatellitesPhaseAmbiguityModifier]
    IonosphericGradientConverter: typing.Type[IonosphericGradientConverter]
    ModifierGradientConverter: typing.Type[ModifierGradientConverter]
    OnBoardAntennaInterSatellitesPhaseModifier: typing.Type[OnBoardAntennaInterSatellitesPhaseModifier]
    OnBoardAntennaInterSatellitesRangeModifier: typing.Type[OnBoardAntennaInterSatellitesRangeModifier]
    OnBoardAntennaOneWayGNSSPhaseModifier: typing.Type[OnBoardAntennaOneWayGNSSPhaseModifier]
    OnBoardAntennaOneWayGNSSRangeModifier: typing.Type[OnBoardAntennaOneWayGNSSRangeModifier]
    OnBoardAntennaPhaseModifier: typing.Type[OnBoardAntennaPhaseModifier]
    OnBoardAntennaRangeModifier: typing.Type[OnBoardAntennaRangeModifier]
    OnBoardAntennaTurnAroundRangeModifier: typing.Type[OnBoardAntennaTurnAroundRangeModifier]
    OneWayGNSSPhaseAmbiguityModifier: typing.Type[OneWayGNSSPhaseAmbiguityModifier]
    OutlierFilter: typing.Type[OutlierFilter]
    ParametricModelEffect: typing.Type[ParametricModelEffect]
    ParametricModelEffectGradient: typing.Type[ParametricModelEffectGradient]
    PhaseAmbiguityModifier: typing.Type[PhaseAmbiguityModifier]
    PhaseIonosphericDelayModifier: typing.Type[PhaseIonosphericDelayModifier]
    PhaseTroposphericDelayModifier: typing.Type[PhaseTroposphericDelayModifier]
    PythonParametricModelEffect: typing.Type[PythonParametricModelEffect]
    PythonParametricModelEffectGradient: typing.Type[PythonParametricModelEffectGradient]
    RangeIonosphericDelayModifier: typing.Type[RangeIonosphericDelayModifier]
    RangeModifierUtil: typing.Type[RangeModifierUtil]
    RangeRateIonosphericDelayModifier: typing.Type[RangeRateIonosphericDelayModifier]
    RangeRateModifierUtil: typing.Type[RangeRateModifierUtil]
    RangeRateTroposphericDelayModifier: typing.Type[RangeRateTroposphericDelayModifier]
    RangeTroposphericDelayModifier: typing.Type[RangeTroposphericDelayModifier]
    RelativisticClockInterSatellitesPhaseModifier: typing.Type[RelativisticClockInterSatellitesPhaseModifier]
    RelativisticClockInterSatellitesRangeModifier: typing.Type[RelativisticClockInterSatellitesRangeModifier]
    RelativisticClockOneWayGNSSPhaseModifier: typing.Type[RelativisticClockOneWayGNSSPhaseModifier]
    RelativisticClockOneWayGNSSRangeModifier: typing.Type[RelativisticClockOneWayGNSSRangeModifier]
    RelativisticClockPhaseModifier: typing.Type[RelativisticClockPhaseModifier]
    RelativisticClockRangeModifier: typing.Type[RelativisticClockRangeModifier]
    RelativisticClockRangeRateModifier: typing.Type[RelativisticClockRangeRateModifier]
    RelativisticJ2ClockInterSatellitesPhaseModifier: typing.Type[RelativisticJ2ClockInterSatellitesPhaseModifier]
    RelativisticJ2ClockInterSatellitesRangeModifier: typing.Type[RelativisticJ2ClockInterSatellitesRangeModifier]
    RelativisticJ2ClockOneWayGNSSPhaseModifier: typing.Type[RelativisticJ2ClockOneWayGNSSPhaseModifier]
    RelativisticJ2ClockOneWayGNSSRangeModifier: typing.Type[RelativisticJ2ClockOneWayGNSSRangeModifier]
    RelativisticJ2ClockPhaseModifier: typing.Type[RelativisticJ2ClockPhaseModifier]
    RelativisticJ2ClockRangeModifier: typing.Type[RelativisticJ2ClockRangeModifier]
    ShapiroInterSatellitePhaseModifier: typing.Type[ShapiroInterSatellitePhaseModifier]
    ShapiroInterSatelliteRangeModifier: typing.Type[ShapiroInterSatelliteRangeModifier]
    ShapiroOneWayGNSSPhaseModifier: typing.Type[ShapiroOneWayGNSSPhaseModifier]
    ShapiroOneWayGNSSRangeModifier: typing.Type[ShapiroOneWayGNSSRangeModifier]
    ShapiroPhaseModifier: typing.Type[ShapiroPhaseModifier]
    ShapiroRangeModifier: typing.Type[ShapiroRangeModifier]
    TDOAIonosphericDelayModifier: typing.Type[TDOAIonosphericDelayModifier]
    TDOATroposphericDelayModifier: typing.Type[TDOATroposphericDelayModifier]
    TroposphericGradientConverter: typing.Type[TroposphericGradientConverter]
    TurnAroundRangeIonosphericDelayModifier: typing.Type[TurnAroundRangeIonosphericDelayModifier]
    TurnAroundRangeTroposphericDelayModifier: typing.Type[TurnAroundRangeTroposphericDelayModifier]
