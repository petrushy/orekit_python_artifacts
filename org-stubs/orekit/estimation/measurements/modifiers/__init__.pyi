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
    public class AbstractAmbiguityModifier extends Object
    
        Base class for phase ambiguity modifier.
    
        Since:
            10.3
    """
    def __init__(self, int: int, double: float): ...

class AbstractRelativisticClockModifier:
    """
    public class AbstractRelativisticClockModifier extends Object
    
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

class AbstractShapiroBaseModifier:
    """
    public class AbstractShapiroBaseModifier extends Object
    
        Class modifying theoretical range measurement with Shapiro time delay.
    
        Shapiro time delay is a relativistic effect due to gravity.
    
        Since:
            10.0
    """
    def __init__(self, double: float): ...

class AngularIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    """
    public class AngularIonosphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
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
    public class AngularRadioRefractionModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
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
    public class AngularTroposphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.AngularAzEl`>
    
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

_Bias__T = typing.TypeVar('_Bias__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class Bias(org.orekit.estimation.measurements.EstimationModifier[_Bias__T], typing.Generic[_Bias__T]):
    """
    public class Bias<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<T>
    
        Class modeling a measurement bias.
    
        Since:
            8.0
    """
    def __init__(self, stringArray: typing.List[str], doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], doubleArray4: typing.List[float]): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_Bias__T]) -> None: ...

class IonosphericGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter):
    """
    public class IonosphericGradientConverter extends :class:`~org.orekit.propagation.integration.AbstractGradientConverter`
    
        Converter for states and parameters arrays.
    
        Since:
            10.2
    """
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getFreeStateParameters(self) -> int:
        """
            Get the number of free state parameters.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractGradientConverter.getFreeStateParameters`Â in
                classÂ :class:`~org.orekit.propagation.integration.AbstractGradientConverter`
        
            Returns:
                number of free state parameters
        
        
        """
        ...
    def getParameters(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel) -> typing.List[org.hipparchus.analysis.differentiation.Gradient]:
        """
            Get the ionospheric model parameters.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<Gradient> state): state as returned by :meth:`~org.orekit.estimation.measurements.modifiers.IonosphericGradientConverter.getState`
                ionoModel (:class:`~org.orekit.models.earth.ionosphere.IonosphericModel`): ionospheric model associated with the parameters
        
            Returns:
                ionospheric model parameters
        
        
        """
        ...
    def getState(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]:
        """
            Get the state with the number of parameters consistent with ionospheric model.
        
            Parameters:
                ionoModel (:class:`~org.orekit.models.earth.ionosphere.IonosphericModel`): ionospheric model
        
            Returns:
                state with the number of parameters consistent with ionospheric model
        
        
        """
        ...

class OnBoardAntennaInterSatellitesPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    public class OnBoardAntennaInterSatellitesPhaseModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.InterSatellitesPhase`>
    
        On-board antenna offset effect on inter-satellites phase measurements.
    
        Since:
            10.3
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class OnBoardAntennaInterSatellitesRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    public class OnBoardAntennaInterSatellitesRangeModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.InterSatellitesRange`>
    
        On-board antenna offset effect on inter-satellites range measurements.
    
        Since:
            9.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class OnBoardAntennaOneWayGNSSPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    public class OnBoardAntennaOneWayGNSSPhaseModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSPhase`>
    
        On-board antenna offset effect on one-way GNSS phase measurements.
    
        Since:
            10.3
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class OnBoardAntennaOneWayGNSSRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    public class OnBoardAntennaOneWayGNSSRangeModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.OneWayGNSSRange`>
    
        On-board antenna offset effect on one-way GNSS range measurements.
    
        Since:
            10.3
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class OnBoardAntennaPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class OnBoardAntennaPhaseModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        On-board antenna offset effect on phase measurements.
    
        Since:
            10.2
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class OnBoardAntennaRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class OnBoardAntennaRangeModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        On-board antenna offset effect on range measurements.
    
        Since:
            9.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class OnBoardAntennaTurnAroundRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    public class OnBoardAntennaTurnAroundRangeModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
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
    public class OutlierFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<T>
    
        Modifier that sets estimated measurement weight to 0 if residual is too far from expected domain.
    
        Since:
            8.0
    """
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_OutlierFilter__T]) -> None: ...

class PhaseIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    public class PhaseIonosphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
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
    public class PhaseTroposphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.gnss.Phase`>
    
        Class modifying theoretical phase measurement with tropospheric delay. The effect of tropospheric correction on the
        phase is directly computed through the computation of the tropospheric delay.
    
        Since:
            10.2
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class RangeIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class RangeIonosphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modifying theoretical range measurement with ionospheric delay. The effect of ionospheric correction on the range
        is directly computed through the computation of the ionospheric delay. The ionospheric delay depends on the frequency of
        the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged
        particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            8.0
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class RangeRateIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    public class RangeRateIonosphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Class modifying theoretical range-rate measurement with ionospheric delay. The effect of ionospheric correction on the
        range-rate is directly computed through the computation of the ionospheric delay difference with respect to time. The
        ionospheric delay depends on the frequency of the signal (GNSS, VLBI, ...). For optical measurements (e.g. SLR), the ray
        is not affected by ionosphere charged particles.
    
        Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
        Since:
            8.0
    """
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float, boolean: bool): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...

class RangeRateTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    public class RangeRateTroposphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.RangeRate`>
    
        Class modifying theoretical range-rate measurements with tropospheric delay. The effect of tropospheric correction on
        the range-rate is directly computed through the computation of the tropospheric delay difference with respect to time.
        In general, for GNSS, VLBI, ... there is hardly any frequency dependence in the delay. For SLR techniques however, the
        frequency dependence is sensitive.
    
        Since:
            8.0
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel, boolean: bool): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...
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

class RangeTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    public class RangeTroposphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.Range`>
    
        Class modifying theoretical range measurement with tropospheric delay. The effect of tropospheric correction on the
        range is directly computed through the computation of the tropospheric delay. In general, for GNSS, VLBI, ... there is
        hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
        Since:
            8.0
    """
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class TroposphericGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter):
    """
    public class TroposphericGradientConverter extends :class:`~org.orekit.propagation.integration.AbstractGradientConverter`
    
        Converter for states and parameters arrays.
    
        Since:
            10.2
    """
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getFreeStateParameters(self) -> int:
        """
            Get the number of free state parameters.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractGradientConverter.getFreeStateParameters`Â in
                classÂ :class:`~org.orekit.propagation.integration.AbstractGradientConverter`
        
            Returns:
                number of free state parameters
        
        
        """
        ...
    def getParameters(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel) -> typing.List[org.hipparchus.analysis.differentiation.Gradient]:
        """
            Get the tropospheric model parameters.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<Gradient> state): state as returned by :meth:`~org.orekit.estimation.measurements.modifiers.TroposphericGradientConverter.getState`
                tropoModel (:class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`): tropospheric model associated with the parameters
        
            Returns:
                tropospheric model parameters
        
        
        """
        ...
    def getState(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]:
        """
            Get the state with the number of parameters consistent with tropospheric model.
        
            Parameters:
                tropoModel (:class:`~org.orekit.models.earth.troposphere.DiscreteTroposphericModel`): tropospheric model
        
            Returns:
                state with the number of parameters consistent with tropospheric model
        
        
        """
        ...

class TurnAroundRangeIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    public class TurnAroundRangeIonosphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
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
    public class TurnAroundRangeTroposphericDelayModifier extends Object implements :class:`~org.orekit.estimation.measurements.EstimationModifier`<:class:`~org.orekit.estimation.measurements.TurnAroundRange`>
    
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.modifiers")``.

    AbstractAmbiguityModifier: typing.Type[AbstractAmbiguityModifier]
    AbstractRelativisticClockModifier: typing.Type[AbstractRelativisticClockModifier]
    AbstractShapiroBaseModifier: typing.Type[AbstractShapiroBaseModifier]
    AngularIonosphericDelayModifier: typing.Type[AngularIonosphericDelayModifier]
    AngularRadioRefractionModifier: typing.Type[AngularRadioRefractionModifier]
    AngularTroposphericDelayModifier: typing.Type[AngularTroposphericDelayModifier]
    Bias: typing.Type[Bias]
    DynamicOutlierFilter: typing.Type[DynamicOutlierFilter]
    InterSatellitesPhaseAmbiguityModifier: typing.Type[InterSatellitesPhaseAmbiguityModifier]
    IonosphericGradientConverter: typing.Type[IonosphericGradientConverter]
    OnBoardAntennaInterSatellitesPhaseModifier: typing.Type[OnBoardAntennaInterSatellitesPhaseModifier]
    OnBoardAntennaInterSatellitesRangeModifier: typing.Type[OnBoardAntennaInterSatellitesRangeModifier]
    OnBoardAntennaOneWayGNSSPhaseModifier: typing.Type[OnBoardAntennaOneWayGNSSPhaseModifier]
    OnBoardAntennaOneWayGNSSRangeModifier: typing.Type[OnBoardAntennaOneWayGNSSRangeModifier]
    OnBoardAntennaPhaseModifier: typing.Type[OnBoardAntennaPhaseModifier]
    OnBoardAntennaRangeModifier: typing.Type[OnBoardAntennaRangeModifier]
    OnBoardAntennaTurnAroundRangeModifier: typing.Type[OnBoardAntennaTurnAroundRangeModifier]
    OneWayGNSSPhaseAmbiguityModifier: typing.Type[OneWayGNSSPhaseAmbiguityModifier]
    OutlierFilter: typing.Type[OutlierFilter]
    PhaseAmbiguityModifier: typing.Type[PhaseAmbiguityModifier]
    PhaseIonosphericDelayModifier: typing.Type[PhaseIonosphericDelayModifier]
    PhaseTroposphericDelayModifier: typing.Type[PhaseTroposphericDelayModifier]
    RangeIonosphericDelayModifier: typing.Type[RangeIonosphericDelayModifier]
    RangeRateIonosphericDelayModifier: typing.Type[RangeRateIonosphericDelayModifier]
    RangeRateTroposphericDelayModifier: typing.Type[RangeRateTroposphericDelayModifier]
    RangeTroposphericDelayModifier: typing.Type[RangeTroposphericDelayModifier]
    RelativisticClockInterSatellitesPhaseModifier: typing.Type[RelativisticClockInterSatellitesPhaseModifier]
    RelativisticClockInterSatellitesRangeModifier: typing.Type[RelativisticClockInterSatellitesRangeModifier]
    RelativisticClockOneWayGNSSPhaseModifier: typing.Type[RelativisticClockOneWayGNSSPhaseModifier]
    RelativisticClockOneWayGNSSRangeModifier: typing.Type[RelativisticClockOneWayGNSSRangeModifier]
    RelativisticClockPhaseModifier: typing.Type[RelativisticClockPhaseModifier]
    RelativisticClockRangeModifier: typing.Type[RelativisticClockRangeModifier]
    RelativisticClockRangeRateModifier: typing.Type[RelativisticClockRangeRateModifier]
    ShapiroInterSatellitePhaseModifier: typing.Type[ShapiroInterSatellitePhaseModifier]
    ShapiroInterSatelliteRangeModifier: typing.Type[ShapiroInterSatelliteRangeModifier]
    ShapiroOneWayGNSSPhaseModifier: typing.Type[ShapiroOneWayGNSSPhaseModifier]
    ShapiroOneWayGNSSRangeModifier: typing.Type[ShapiroOneWayGNSSRangeModifier]
    ShapiroPhaseModifier: typing.Type[ShapiroPhaseModifier]
    ShapiroRangeModifier: typing.Type[ShapiroRangeModifier]
    TroposphericGradientConverter: typing.Type[TroposphericGradientConverter]
    TurnAroundRangeIonosphericDelayModifier: typing.Type[TurnAroundRangeIonosphericDelayModifier]
    TurnAroundRangeTroposphericDelayModifier: typing.Type[TurnAroundRangeTroposphericDelayModifier]
