
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.data
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.gnss
import org.orekit.frames
import org.orekit.gnss.antenna
import org.orekit.models
import org.orekit.models.earth.ionosphere
import org.orekit.models.earth.troposphere
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.time
import org.orekit.utils
import typing



class AberrationModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularRaDec]):
    """
    Class modifying theoretical angular measurement with (the inverse of) stellar aberration.
    
    This class implements equation 3.252-3 from Seidelmann, "Explanatory Supplement to the Astronmical Almanac", 1992.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    @staticmethod
    def fieldNaturalToProper(naturalRaDec: typing.Union[typing.List[org.hipparchus.analysis.differentiation.Gradient], jpype.JArray], stationToInertial: org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient], frame: org.orekit.frames.Frame) -> typing.MutableSequence[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    @staticmethod
    def fieldNaturalToProper(naturalRaDec: typing.Union[typing.List[org.hipparchus.analysis.differentiation.Gradient], jpype.JArray], stationToInertial: org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient], frame: org.orekit.frames.Frame, context: org.orekit.data.DataContext) -> typing.MutableSequence[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    @staticmethod
    def fieldProperToNatural(properRaDec: typing.Union[typing.List[org.hipparchus.analysis.differentiation.Gradient], jpype.JArray], stationToInertial: org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient], frame: org.orekit.frames.Frame) -> typing.MutableSequence[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    @staticmethod
    def fieldProperToNatural(properRaDec: typing.Union[typing.List[org.hipparchus.analysis.differentiation.Gradient], jpype.JArray], stationToInertial: org.orekit.frames.FieldTransform[org.hipparchus.analysis.differentiation.Gradient], frame: org.orekit.frames.Frame, context: org.orekit.data.DataContext) -> typing.MutableSequence[org.hipparchus.analysis.differentiation.Gradient]: ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.AngularRaDec]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<AngularRaDec> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.AngularRaDec]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<AngularRaDec> estimated): estimated measurement to modify
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def naturalToProper(naturalRaDec: typing.Union[typing.List[float], jpype.JArray], station: org.orekit.estimation.measurements.GroundStation, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Natural to proper correction for aberration of light.
        
        Parameters:
            naturalRaDec (double[]): the "natural" direction (in barycentric coordinates)
            station (GroundStation): the observer ground station
            date (AbsoluteDate): the date of the measurement
            frame (Frame): the frame of the measurement
            context (DataContext): the data context
        
        Returns:
            the "proper" direction (station-relative coordinates)
        
        Since:
            12.0.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def naturalToProper(naturalRaDec: typing.Union[typing.List[float], jpype.JArray], station: org.orekit.estimation.measurements.GroundStation, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, context: org.orekit.data.DataContext) -> typing.MutableSequence[float]: ...
    @typing.overload
    @staticmethod
    def properToNatural(properRaDec: typing.Union[typing.List[float], jpype.JArray], station: org.orekit.estimation.measurements.GroundStation, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Proper to natural correction for aberration of light.
        
        Parameters:
            properRaDec (double[]): the "proper" direction (station-relative coordinates)
            station (GroundStation): the observer ground station
            date (AbsoluteDate): the date of the measurement
            frame (Frame): the frame of the measurement
            context (DataContext): the data context
        
        Returns:
            the "natural" direction (in barycentric coordinates)
        
        Since:
            12.0.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def properToNatural(properRaDec: typing.Union[typing.List[float], jpype.JArray], station: org.orekit.estimation.measurements.GroundStation, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, context: org.orekit.data.DataContext) -> typing.MutableSequence[float]: ...

class AbstractRelativisticClockModifier:
    """
    Class modifying theoretical measurements with relativistic clock correction.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...

class AbstractRelativisticJ2ClockModifier:
    """
    Class modifying theoretical measurements with relativistic J2 clock correction.
    
    Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
    The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
    Since:
        11.2
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Equation 19.18 Springer, 2017."
    """
    def __init__(self, gm: float, c20: float, equatorialRadius: float):
        """
        Constructor for the Relativistic J2 Clock modifier.
        
        Parameters:
            gm (double): Earth gravitational constant (mu) in m³/s².
            c20 (double): Earth un-normalized second zonal coefficient (Signed J2 constant, is negative) (Typical value -1.0826e-3).
            equatorialRadius (double): Earth equatorial radius in m.
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...

class AbstractShapiroBaseModifier:
    """
    Class modifying theoretical range measurement with Shapiro time delay.
    
    Shapiro time delay is a relativistic effect due to gravity.
    
    Since:
        10.0
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...

class AngularIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    """
    Class modifying theoretical angular measurement with ionospheric delay.
    
    The effect of ionospheric correction on the angular measurement is computed through the computation of the ionospheric delay. The spacecraft state is shifted by the computed delay time and elevation and azimuth are computed again with the new spacecraft state.
    
    The ionospheric delay depends on the frequency of the signal (GNSS, VLBI...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged particles.
    
    Since 10.0, state derivatives and ionospheric parameters derivatives are computed using automatic differentiation.
    
    Since:
        8.0
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): Ionospheric delay model appropriate for the current angular measurement method.
            freq (double): frequency of the signal in Hz
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.AngularAzEl]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<AngularAzEl> estimated): estimated measurement to modify
        
        
        """
        ...

class AngularRadioRefractionModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    """
    Class modifying theoretical angular measurement with tropospheric radio refractive index. A radio ray passing through the lower (non-ionized) layer of the atmosphere undergoes bending caused by the gradient of the relative index. Since the refractive index varies mainly with altitude, only the vertical gradient of the refractive index is considered here. The effect of tropospheric correction on the angular measurement is computed directly through the computation of the apparent elevation angle. Recommendation ITU-R P.453-11 (07/2015) and Recommendation ITU-R P.834-7 (10/2015)
    
    Since:
        8.0
    """
    def __init__(self, model: typing.Union[org.orekit.models.AtmosphericRefractionModel, typing.Callable]):
        """
        Constructor.
        
        Parameters:
            model (AtmosphericRefractionModel): tropospheric refraction model appropriate for the current angular measurement method.
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.AngularAzEl]) -> None:
        """
        Description copied from interface: modifyWithoutDerivatives Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<AngularAzEl> estimated): estimated measurement to modify
        
        
        """
        ...

class BaseRangeIonosphericDelayModifier:
    """
    Base class modifying theoretical range measurement with ionospheric delay. The effect of ionospheric correction on the range is directly computed through the computation of the ionospheric delay. The ionospheric delay depends on the frequency of the signal (GNSS, VLBI...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged particles.
    
    Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
    Since:
        11.2
    """
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for this modifier parameters.
        
        Returns:
            drivers for this modifier parameters
        
        
        """
        ...

class BaseRangeRateIonosphericDelayModifier:
    """
    Base class modifying theoretical range-rate measurement with ionospheric delay. The effect of ionospheric correction on the range-rate is directly computed through the computation of the ionospheric delay difference with respect to time. The ionospheric delay depends on the frequency of the signal (GNSS, VLBI...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged particles.
    
    Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
    Since:
        11.2
    """
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for this modifier parameters.
        
        Returns:
            drivers for this modifier parameters
        
        
        """
        ...

class BaseRangeRateTroposphericDelayModifier:
    """
    Baselass modifying theoretical range-rate measurements with tropospheric delay. The effect of tropospheric correction on the range-rate is directly computed through the computation of the tropospheric delay difference with respect to time. In general, for GNSS, VLBI... there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
    Since:
        11.2
    """
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for this modifier parameters.
        
        Returns:
            drivers for this modifier parameters
        
        
        """
        ...
    _rangeRateErrorTroposphericModel_1__T = typing.TypeVar('_rangeRateErrorTroposphericModel_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rangeRateErrorTroposphericModel(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the measurement error due to Troposphere.
        
        Parameters:
            station (GroundStation): station
            state (SpacecraftState): spacecraft state
        
        Returns:
            the measurement error due to Troposphere
        
        """
        ...
    @typing.overload
    def rangeRateErrorTroposphericModel(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.FieldSpacecraftState[_rangeRateErrorTroposphericModel_1__T], parameters: typing.Union[typing.List[_rangeRateErrorTroposphericModel_1__T], jpype.JArray]) -> _rangeRateErrorTroposphericModel_1__T:
        """
        Compute the measurement error due to Troposphere.
        
        Parameters:
            station (GroundStation): station
            state (FieldSpacecraftState<T> state): spacecraft state
            parameters (T[]): tropospheric model parameters
        
        Returns:
            the measurement error due to Troposphere
        
        
        """
        ...

class BaseRangeTroposphericDelayModifier:
    """
    Base class modifying theoretical range measurements with tropospheric delay. The effect of tropospheric correction on the range is directly computed through the computation of the tropospheric delay. In general, for GNSS, VLBI... there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
    Since:
        11.2
    """
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for this modifier parameters.
        
        Returns:
            drivers for this modifier parameters
        
        
        """
        ...
    _rangeErrorTroposphericModel_1__T = typing.TypeVar('_rangeErrorTroposphericModel_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rangeErrorTroposphericModel(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the measurement error due to Troposphere.
        
        Parameters:
            station (GroundStation): station
            state (SpacecraftState): spacecraft state
        
        Returns:
            the measurement error due to Troposphere
        
        """
        ...
    @typing.overload
    def rangeErrorTroposphericModel(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.FieldSpacecraftState[_rangeErrorTroposphericModel_1__T], parameters: typing.Union[typing.List[_rangeErrorTroposphericModel_1__T], jpype.JArray]) -> _rangeErrorTroposphericModel_1__T:
        """
        Compute the measurement error due to Troposphere.
        
        Parameters:
            station (GroundStation): station
            state (FieldSpacecraftState<T> state): spacecraft state
            parameters (T[]): tropospheric model parameters
        
        Returns:
            the measurement error due to Troposphere
        
        
        """
        ...

_Bias__T = typing.TypeVar('_Bias__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class Bias(org.orekit.estimation.measurements.EstimationModifier[_Bias__T], typing.Generic[_Bias__T]):
    """
    Class modeling a measurement bias.
    
    Since:
        8.0
    """
    def __init__(self, name: typing.Union[typing.List[str], jpype.JArray], bias: typing.Union[typing.List[float], jpype.JArray], scale: typing.Union[typing.List[float], jpype.JArray], min: typing.Union[typing.List[float], jpype.JArray], max: typing.Union[typing.List[float], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            name (String[]): name of the bias
            bias (double[]): reference value of the bias
            scale (double[]): scale of the bias, for normalization
            min (double[]): minimum value of the bias
            max (double[]): maximum value of the bias
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        For a bias, there are getDimension parameter drivers, sorted in components order.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[_Bias__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<Bias> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_Bias__T]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Bias> estimated): estimated measurement to modify
        
        
        """
        ...

class ModifierGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter):
    """
    Converter for states and parameters arrays.
    
    Since:
        11.2
    """
    def __init__(self, state: org.orekit.propagation.SpacecraftState, freeStateParameters: int, provider: org.orekit.attitudes.AttitudeProvider):
        """
        Simple constructor.
        
        Parameters:
            state (SpacecraftState): regular state
            freeStateParameters (int): number of free parameters, either 3 (position) or 6 (position-velocity)
            provider (AttitudeProvider): provider to use if attitude needs to be recomputed
        
        
        """
        ...

class OnBoardAntennaTurnAroundRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    On-board antenna offset effect on turn around range measurements.
    
    Since:
        9.0
    """
    def __init__(self, antennaPhaseCenter: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Simple constructor.
        
        Parameters:
            antennaPhaseCenter (Vector3D): position of the Antenna Phase Center in satellite frame
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.TurnAroundRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<TurnAroundRange> estimated): estimated measurement to modify
        
        
        """
        ...

_OutlierFilter__T = typing.TypeVar('_OutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class OutlierFilter(org.orekit.estimation.measurements.EstimationModifier[_OutlierFilter__T], typing.Generic[_OutlierFilter__T]):
    """
    Modifier that sets estimated measurement weight to 0 if residual is too far from expected domain.
    
    Since:
        8.0
    """
    def __init__(self, warmup: int, maxSigma: float):
        """
        Simple constructor.
        
        Parameters:
            warmup (int): number of iterations before with filter is not applied
            maxSigma (double): detection limit for outliers.
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_OutlierFilter__T]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OutlierFilter> estimated): estimated measurement to modify
        
        
        """
        ...

class ParametricModelEffect:
    """
    Functional interface for parametric models.
    
    Since:
        11.2
    """
    def evaluate(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Evaluate the parametric model effect.
        
        Parameters:
            station (GroundStation): station
            state (SpacecraftState): spacecraft state
        
        Returns:
            the measurement error due to parametric model
        
        
        """
        ...

class ParametricModelEffectGradient:
    """
    Functional interface for parametric models.
    
    Since:
        11.2
    """
    def evaluate(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], parameters: typing.Union[typing.List[org.hipparchus.analysis.differentiation.Gradient], jpype.JArray]) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Evaluate the parametric model effect.
        
        Parameters:
            station (GroundStation): station
            state (FieldSpacecraftState<Gradient> state): spacecraft state
            parameters (Gradient[]): parametric model parameters
        
        Returns:
            the measurement error due to parametric model
        
        
        """
        ...

_PhaseCentersGroundReceiverBaseModifier__T = typing.TypeVar('_PhaseCentersGroundReceiverBaseModifier__T', bound=org.orekit.estimation.measurements.GroundReceiverMeasurement)  # <T>
class PhaseCentersGroundReceiverBaseModifier(typing.Generic[_PhaseCentersGroundReceiverBaseModifier__T]):
    """
    Ground and on-board antennas offsets effect on range measurements.
    
    Since:
        12.0
    """
    def __init__(self, stationPattern: org.orekit.gnss.antenna.FrequencyPattern, satellitePattern: org.orekit.gnss.antenna.FrequencyPattern):
        """
        Simple constructor.
        
        Parameters:
            stationPattern (FrequencyPattern): station pattern
            satellitePattern (FrequencyPattern): satellite pattern
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def oneWayDistanceModification(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PhaseCentersGroundReceiverBaseModifier__T]) -> float:
        """
        Compute distance modification for one way measurement.
        
        Parameters:
            estimated (EstimatedMeasurementBase<PhaseCentersGroundReceiverBaseModifier> estimated): estimated measurement to modify
        
        Returns:
            distance modification to add to raw measurement
        
        
        """
        ...
    def twoWayDistanceModification(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PhaseCentersGroundReceiverBaseModifier__T]) -> float:
        """
        Apply a modifier to a two-way range measurement.
        
        Parameters:
            estimated (EstimatedMeasurementBase<PhaseCentersGroundReceiverBaseModifier> estimated): estimated measurement to modify
        
        Returns:
            distance modification to add to raw measurement
        
        
        """
        ...

_PhaseCentersInterSatellitesBaseModifier__T = typing.TypeVar('_PhaseCentersInterSatellitesBaseModifier__T', bound=org.orekit.estimation.measurements.AbstractMeasurement)  # <T>
class PhaseCentersInterSatellitesBaseModifier(typing.Generic[_PhaseCentersInterSatellitesBaseModifier__T]):
    """
    On-board antenna offset effect on inter-satellites phase measurements.
    
    Since:
        12.1
    """
    def __init__(self, pattern1: org.orekit.gnss.antenna.FrequencyPattern, pattern2: org.orekit.gnss.antenna.FrequencyPattern):
        """
        Simple constructor.
        
        Parameters:
            pattern1 (FrequencyPattern): pattern for satellite 1 (i.e. the satellite which receives the signal and performs the measurement)
            pattern2 (FrequencyPattern): pattern for satellite 2 (i.e. the satellite which simply emits the signal in the one-way case, or reflects the signal in
                the two-way case)
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def oneWayDistanceModification(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PhaseCentersInterSatellitesBaseModifier__T]) -> float:
        """
        Compute distance modification for one way measurement.
        
        Parameters:
            estimated (EstimatedMeasurementBase<PhaseCentersInterSatellitesBaseModifier> estimated): estimated measurement to modify
        
        Returns:
            distance modification to add to raw measurement
        
        
        """
        ...
    def twoWayDistanceModification(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.InterSatellitesRange]) -> float:
        """
        Compute distance modification for two way measurement.
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesRange> estimated): estimated measurement to modify
        
        Returns:
            distance modification to add to raw measurement
        
        
        """
        ...

class PhaseCentersOffsetComputer:
    """
    Compute phase centers offset on an emitter-receiver link.
    
    Since:
        12.0
    """
    def __init__(self, emitterPattern: org.orekit.gnss.antenna.FrequencyPattern, receiverPattern: org.orekit.gnss.antenna.FrequencyPattern):
        """
        Simple constructor.
        
        Parameters:
            emitterPattern (FrequencyPattern): emitter pattern
            receiverPattern (FrequencyPattern): receiver pattern
        
        
        """
        ...
    def offset(self, emitterToInert: org.orekit.frames.StaticTransform, receiverToInert: org.orekit.frames.StaticTransform) -> float:
        """
        Compute distance offset to be added to the distance between antennas reference points.
        
        Parameters:
            emitterToInert (StaticTransform): transform from emitter to inertial frame at emission date
            receiverToInert (StaticTransform): transform from receiver to inertial frame at reception date
        
        Returns:
            offset to be added to distance between origins, in order to get distance between phase centers
        
        
        """
        ...

_PhaseCentersOneWayGNSSBaseModifier__T = typing.TypeVar('_PhaseCentersOneWayGNSSBaseModifier__T', bound=org.orekit.estimation.measurements.AbstractMeasurement)  # <T>
class PhaseCentersOneWayGNSSBaseModifier(typing.Generic[_PhaseCentersOneWayGNSSBaseModifier__T]):
    """
    On-board antenna offset effect on inter-satellites phase measurements.
    
    Since:
        12.1
    """
    def __init__(self, receiverPattern: org.orekit.gnss.antenna.FrequencyPattern, emitterPattern: org.orekit.gnss.antenna.FrequencyPattern, attitudeProvider: org.orekit.attitudes.AttitudeProvider):
        """
        Simple constructor.
        
        Parameters:
            receiverPattern (FrequencyPattern): pattern for receiver satellite
            emitterPattern (FrequencyPattern): pattern for emitter satellite
            attitudeProvider (AttitudeProvider): attitude provider of the emitting satellite
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Returns:
            name of the effect modifying the measurement
        
        Since:
            13.0
        
        
        """
        ...
    def oneWayDistanceModification(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PhaseCentersOneWayGNSSBaseModifier__T]) -> float:
        """
        Compute distance modification for one way measurement.
        
        Parameters:
            estimated (EstimatedMeasurementBase<PhaseCentersOneWayGNSSBaseModifier> estimated): estimated measurement to modify
        
        Returns:
            distance modification to add to raw measurement
        
        
        """
        ...

class PhaseIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    Class modifying theoretical phase measurement with ionospheric delay. The effect of ionospheric correction on the phase is directly computed through the computation of the ionospheric delay.
    
    Since:
        10.2
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): Ionospheric delay model appropriate for the current range measurement method.
            freq (double): frequency of the signal in Hz
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Description copied from interface: modify Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<Phase> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Description copied from interface: modifyWithoutDerivatives Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Phase> estimated): estimated measurement to modify
        
        
        """
        ...

class PhaseTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    Class modifying theoretical phase measurement with tropospheric delay. The effect of tropospheric correction on the phase is directly computed through the computation of the tropospheric delay.
    
    Since:
        10.2
    """
    def __init__(self, model: org.orekit.models.earth.troposphere.TroposphericModel):
        """
        Constructor.
        
        Parameters:
            model (TroposphericModel): Tropospheric delay model appropriate for the current range measurement method.
        
        Since:
            12.1
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<Phase> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Phase> estimated): estimated measurement to modify
        
        
        """
        ...

class RangeModifierUtil:
    """
    Utility class modifying theoretical range measurement.
    
    Since:
        11.2
    """
    _modify__T = typing.TypeVar('_modify__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def modify(estimated: org.orekit.estimation.measurements.EstimatedMeasurement[_modify__T], parametricModel: typing.Union[org.orekit.utils.ParameterDriversProvider, typing.Callable], converter: org.orekit.propagation.integration.AbstractGradientConverter, station: org.orekit.estimation.measurements.GroundStation, modelEffect: typing.Union[ParametricModelEffect, typing.Callable], modelEffectGradient: typing.Union[ParametricModelEffectGradient, typing.Callable], modifier: org.orekit.estimation.measurements.EstimationModifier[_modify__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Parameters:
            estimated (EstimatedMeasurement<T> estimated): estimated measurement to modify
            station (ParameterDriversProvider): ground station
            converter (AbstractGradientConverter): gradient converter
            parametricModel (GroundStation): parametric modifier model
            modelEffect (ParametricModelEffect): model effect
            modelEffectGradient (ParametricModelEffectGradient): model effect gradient
            modifier (EstimationModifier<T> modifier): applied modifier
        
        
        """
        ...
    _modifyWithoutDerivatives__T = typing.TypeVar('_modifyWithoutDerivatives__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def modifyWithoutDerivatives(estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_modifyWithoutDerivatives__T], station: org.orekit.estimation.measurements.GroundStation, modelEffect: typing.Union[ParametricModelEffect, typing.Callable], modifier: org.orekit.estimation.measurements.EstimationModifier[_modifyWithoutDerivatives__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Parameters:
            estimated (EstimatedMeasurementBase<T> estimated): estimated measurement to modify
            station (GroundStation): ground station
            modelEffect (ParametricModelEffect): model effect
            modifier (EstimationModifier<T> modifier): applied modifier
        
        Since:
            12.1
        
        
        """
        ...

class RangeRateModifierUtil:
    """
    Utility class modifying theoretical range-rate measurement.
    
    Since:
        11.2
    """
    _modify__T = typing.TypeVar('_modify__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def modify(estimated: org.orekit.estimation.measurements.EstimatedMeasurement[_modify__T], parametricModel: typing.Union[org.orekit.utils.ParameterDriversProvider, typing.Callable], converter: org.orekit.propagation.integration.AbstractGradientConverter, station: org.orekit.estimation.measurements.GroundStation, modelEffect: typing.Union[ParametricModelEffect, typing.Callable], modelEffectGradient: typing.Union[ParametricModelEffectGradient, typing.Callable], modifier: org.orekit.estimation.measurements.EstimationModifier[_modify__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Parameters:
            estimated (EstimatedMeasurement<T> estimated): estimated measurement to modify
            station (ParameterDriversProvider): ground station
            converter (AbstractGradientConverter): gradient converter
            parametricModel (GroundStation): parametric modifier model
            modelEffect (ParametricModelEffect): model effect
            modelEffectGradient (ParametricModelEffectGradient): model effect gradient
            modifier (EstimationModifier<T> modifier): applied modifier
        
        Since:
            12.1
        
        
        """
        ...
    _modifyWithoutDerivatives__T = typing.TypeVar('_modifyWithoutDerivatives__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
    @staticmethod
    def modifyWithoutDerivatives(estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_modifyWithoutDerivatives__T], station: org.orekit.estimation.measurements.GroundStation, modelEffect: typing.Union[ParametricModelEffect, typing.Callable], modifier: org.orekit.estimation.measurements.EstimationModifier[_modifyWithoutDerivatives__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Parameters:
            estimated (EstimatedMeasurementBase<T> estimated): estimated measurement to modify
            station (GroundStation): ground station
            modelEffect (ParametricModelEffect): model effect
            modifier (EstimationModifier<T> modifier): applied modifier
        
        Since:
            12.1
        
        
        """
        ...

class TDOAIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TDOA]):
    """
    Class modifying theoretical TDOA measurements with ionospheric delay.
    
    The effect of ionospheric correction on the TDOA is a time delay computed directly from the difference in ionospheric delays for each downlink.
    
    The ionospheric delay depends on the frequency of the signal.
    
    Since:
        11.2
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): ionospheric model appropriate for the current TDOA measurement method
            freq (double): frequency of the signal in Hz
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TDOA]) -> None:
        """
        Description copied from interface: modify Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<TDOA> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.TDOA]) -> None:
        """
        Description copied from interface: modifyWithoutDerivatives Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<TDOA> estimated): estimated measurement to modify
        
        
        """
        ...

class TDOATroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TDOA]):
    """
    Class modifying theoretical TDOA measurements with tropospheric delay.
    
    The effect of tropospheric correction on the TDOA is a time delay computed directly from the difference in tropospheric delays for each downlink.
    
    Tropospheric delay is not frequency dependent for signals up to 15 GHz.
    
    Since:
        11.2
    """
    def __init__(self, model: org.orekit.models.earth.troposphere.TroposphericModel):
        """
        Constructor.
        
        Parameters:
            model (TroposphericModel): tropospheric model appropriate for the current TDOA measurement method.
        
        Since:
            12.1
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TDOA]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<TDOA> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.TDOA]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<TDOA> estimated): estimated measurement to modify
        
        
        """
        ...

class TurnAroundRangeIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    Class modifying theoretical TurnAroundRange measurement with ionospheric delay.
    
    The effect of ionospheric correction on the TurnAroundRange is directly computed through the computation of the ionospheric delay.
    
    The ionospheric delay depends on the frequency of the signal (GNSS, VLBI...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged particles.
    
    Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
    Since:
        9.0
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): Ionospheric delay model appropriate for the current TurnAroundRange measurement method.
            freq (double): frequency of the signal in Hz
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None:
        """
        Description copied from interface: modify Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<TurnAroundRange> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.TurnAroundRange]) -> None:
        """
        Description copied from interface: modifyWithoutDerivatives Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<TurnAroundRange> estimated): estimated measurement to modify
        
        
        """
        ...

class TurnAroundRangeTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    """
    Class modifying theoretical turn-around TurnAroundRange measurement with tropospheric delay.
    
    The effect of tropospheric correction on the TurnAroundRange is directly computed through the computation of the tropospheric delay.
    
    In general, for GNSS, VLBI... there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
    Since:
        9.0
    """
    def __init__(self, model: org.orekit.models.earth.troposphere.TroposphericModel):
        """
        Constructor.
        
        Parameters:
            model (TroposphericModel): Tropospheric delay model appropriate for the current TurnAroundRange measurement method.
        
        Since:
            12.1
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<TurnAroundRange> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.TurnAroundRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<TurnAroundRange> estimated): estimated measurement to modify
        
        
        """
        ...

_AbstractRelativisticClockOnBoardRangeRateModifier__T = typing.TypeVar('_AbstractRelativisticClockOnBoardRangeRateModifier__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class AbstractRelativisticClockOnBoardRangeRateModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[_AbstractRelativisticClockOnBoardRangeRateModifier__T], typing.Generic[_AbstractRelativisticClockOnBoardRangeRateModifier__T]):
    """
    Class modifying theoretical range-rate measurement with relativistic frequency deviation.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        12.1
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getEffectName(self) -> str:
        """
        Get the name of the effect modifying the measurement.
        
        Specified by: getEffectName in interface EstimationModifier
        
        Overrides: getEffectName in class AbstractRelativisticClockModifier
        
        Returns:
            name of the effect modifying the measurement
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...

class BistaticRangeIonosphericDelayModifier(BaseRangeIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRange]):
    """
    Class modifying theoretical bistatic range measurement with ionospheric delay. The effect of ionospheric correction on the range is directly computed through the computation of the ionospheric delay.
    
    The ionospheric delay depends on the frequency of the signal (GNSS, VLBI...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged particles.
    
    Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
    Since:
        11.2
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): Ionospheric delay model appropriate for the current range measurement method.
            freq (double): frequency of the signal in Hz
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRange]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<BistaticRange> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.BistaticRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<BistaticRange> estimated): estimated measurement to modify
        
        
        """
        ...

class BistaticRangeRateIonosphericDelayModifier(BaseRangeRateIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRangeRate]):
    """
    Class modifying theoretical bistatic range-rate measurement with ionospheric delay.
    
    The effect of ionospheric correction on the bistatic range-rate is directly computed through the computation of the ionospheric delay difference with respect to time.
    
    The ionospheric delay depends on the frequency of the signal.
    
    Since:
        11.2
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): Ionospheric delay model appropriate for the current range-rate measurement method.
            freq (double): frequency of the signal in Hz
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<BistaticRangeRate> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.BistaticRangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<BistaticRangeRate> estimated): estimated measurement to modify
        
        
        """
        ...

class BistaticRangeRateTroposphericDelayModifier(BaseRangeRateTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRangeRate]):
    """
    Class modifying theoretical bistatic range-rate measurements with tropospheric delay.
    
    The effect of tropospheric correction on the bistatic range-rate is directly computed through the computation of the tropospheric delay difference with respect to time.
    
    Tropospheric delay is not frequency dependent for signals up to 15 GHz.
    
    Since:
        11.2
    """
    def __init__(self, model: org.orekit.models.earth.troposphere.TroposphericModel):
        """
        Constructor.
        
        Parameters:
            model (TroposphericModel): Tropospheric delay model appropriate for the current range-rate measurement method.
        
        Since:
            12.1
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<BistaticRangeRate> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.BistaticRangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<BistaticRangeRate> estimated): estimated measurement to modify
        
        
        """
        ...

class BistaticRangeTroposphericDelayModifier(BaseRangeTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.BistaticRange]):
    """
    Class modifying theoretical bistatic range measurement with tropospheric delay.
    
    The effect of tropospheric correction on the range is directly computed through the computation of the tropospheric delay.
    
    In general, for GNSS, VLBI... there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
    Since:
        11.2
    """
    def __init__(self, model: org.orekit.models.earth.troposphere.TroposphericModel):
        """
        Constructor.
        
        Parameters:
            model (TroposphericModel): Tropospheric delay model appropriate for the current range measurement method.
        
        Since:
            12.1
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.BistaticRange]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<BistaticRange> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.BistaticRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<BistaticRange> estimated): estimated measurement to modify
        
        
        """
        ...

_DynamicOutlierFilter__T = typing.TypeVar('_DynamicOutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class DynamicOutlierFilter(OutlierFilter[_DynamicOutlierFilter__T], typing.Generic[_DynamicOutlierFilter__T]):
    """
    Modifier that sets estimated measurement weight to 0 if residual is too far from expected domain. The "dynamic" aspect comes from the fact that the value of sigma can be changed on demand. This is mainly used when searching for outliers in Kalman filters' prediction phase. The value of sigma is then set to the square root of the diagonal of the matrix (H.Ppred.Ht+R) Note that in the case of the Kalman filter we use the "iteration" word to represent the number of measurements processed by the filter so far.
    
    Since:
        9.2
    """
    def __init__(self, warmup: int, maxSigma: float):
        """
        Simple constructor.
        
        Parameters:
            warmup (int): number of iterations before with filter is not applied
            maxSigma (double): detection limit for outlier
        
        
        """
        ...
    def getSigma(self) -> typing.MutableSequence[float]:
        """
        Get the current value of sigma.
        
        Returns:
            The current value of sigma
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[_DynamicOutlierFilter__T]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Parameters:
            estimated (EstimatedMeasurement<DynamicOutlierFilter> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_DynamicOutlierFilter__T]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Overrides: modifyWithoutDerivatives in class OutlierFilter
        
        Parameters:
            estimated (EstimatedMeasurementBase<DynamicOutlierFilter> estimated): estimated measurement to modify
        
        
        """
        ...
    def setSigma(self, sigma: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the current value of sigma.
        
        Parameters:
            sigma (double[]): The value of sigma to set
        
        
        """
        ...

class OnBoardAntennaInterSatellitesPhaseModifier(PhaseCentersInterSatellitesBaseModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase], org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    On-board antenna offset effect on inter-satellites phase measurements.
    
    Since:
        10.3
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, frequencyPattern: org.orekit.gnss.antenna.FrequencyPattern, frequencyPattern2: org.orekit.gnss.antenna.FrequencyPattern): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None:
        """
        Description copied from interface: modifyWithoutDerivatives Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class OnBoardAntennaInterSatellitesRangeModifier(PhaseCentersInterSatellitesBaseModifier[org.orekit.estimation.measurements.InterSatellitesRange], org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    On-board antenna offset effect on inter-satellites range measurements.
    
    Since:
        9.0
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, frequencyPattern: org.orekit.gnss.antenna.FrequencyPattern, frequencyPattern2: org.orekit.gnss.antenna.FrequencyPattern): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.InterSatellitesRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesRange> estimated): estimated measurement to modify
        
        
        """
        ...

class OnBoardAntennaOneWayGNSSPhaseModifier(PhaseCentersOneWayGNSSBaseModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase], org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    On-board antenna offset effect on one-way GNSS phase measurements.
    
    Since:
        10.3
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, frequencyPattern: org.orekit.gnss.antenna.FrequencyPattern, frequencyPattern2: org.orekit.gnss.antenna.FrequencyPattern, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class OnBoardAntennaOneWayGNSSRangeModifier(PhaseCentersOneWayGNSSBaseModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange], org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    On-board antenna offset effect on one-way GNSS range measurements.
    
    Since:
        10.3
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, frequencyPattern: org.orekit.gnss.antenna.FrequencyPattern, frequencyPattern2: org.orekit.gnss.antenna.FrequencyPattern, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSRange> estimated): estimated measurement to modify
        
        
        """
        ...

class PhaseCentersPhaseModifier(PhaseCentersGroundReceiverBaseModifier[org.orekit.estimation.measurements.gnss.Phase], org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    Ground and on-board antennas offsets effect on phase measurements.
    
    Since:
        12.0
    """
    def __init__(self, stationPattern: org.orekit.gnss.antenna.FrequencyPattern, satellitePattern: org.orekit.gnss.antenna.FrequencyPattern):
        """
        Simple constructor.
        
        Parameters:
            stationPattern (FrequencyPattern): station pattern
            satellitePattern (FrequencyPattern): satellite pattern
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Phase> estimated): estimated measurement to modify
        
        
        """
        ...

class PhaseCentersRangeModifier(PhaseCentersGroundReceiverBaseModifier[org.orekit.estimation.measurements.Range], org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    Ground and on-board antennas offsets effect on range measurements.
    
    Since:
        12.0
    """
    def __init__(self, stationPattern: org.orekit.gnss.antenna.FrequencyPattern, satellitePattern: org.orekit.gnss.antenna.FrequencyPattern):
        """
        Simple constructor.
        
        Parameters:
            stationPattern (FrequencyPattern): station pattern
            satellitePattern (FrequencyPattern): satellite pattern
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Range> estimated): estimated measurement to modify
        
        
        """
        ...

class PythonParametricModelEffect(ParametricModelEffect):
    def __init__(self): ...
    def evaluate(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Evaluate the parametric model effect.
        
        Specified by: evaluate in interface ParametricModelEffect
        
        Parameters:
            station (GroundStation): station
            state (SpacecraftState): spacecraft state
        
        Returns:
            the measurement error due to parametric model
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonParametricModelEffectGradient(ParametricModelEffectGradient):
    def __init__(self): ...
    def evaluate(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], parameters: typing.Union[typing.List[org.hipparchus.analysis.differentiation.Gradient], jpype.JArray]) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Evaluate the parametric model effect.
        
        Specified by: evaluate in interface ParametricModelEffectGradient
        
        Parameters:
            station (GroundStation): station
            state (FieldSpacecraftState<Gradient> state): spacecraft state
            parameters (Gradient[]): parametric model parameters
        
        Returns:
            the measurement error due to parametric model
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class RangeIonosphericDelayModifier(BaseRangeIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    Class modifying theoretical range measurement with ionospheric delay.
    
    The effect of ionospheric correction on the range is directly computed through the computation of the ionospheric delay.
    
    The ionospheric delay depends on the frequency of the signal (GNSS, VLBI...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged particles.
    
    Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
    Since:
        8.0
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): Ionospheric delay model appropriate for the current range measurement method.
            freq (double): frequency of the signal in Hz
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<Range> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Range> estimated): estimated measurement to modify
        
        
        """
        ...

class RangeRateIonosphericDelayModifier(BaseRangeRateIonosphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    Class modifying theoretical range-rate measurement with ionospheric delay.
    
    The effect of ionospheric correction on the range-rate is directly computed through the computation of the ionospheric delay difference with respect to time.
    
    The ionospheric delay depends on the frequency of the signal (GNSS, VLBI...). For optical measurements (e.g. SLR), the ray is not affected by ionosphere charged particles.
    
    Since 10.0, state derivatives and ionospheric parameters derivates are computed using automatic differentiation.
    
    Since:
        8.0
    """
    def __init__(self, model: org.orekit.models.earth.ionosphere.IonosphericModel, freq: float, twoWay: bool):
        """
        Constructor.
        
        Parameters:
            model (IonosphericModel): Ionospheric delay model appropriate for the current range-rate measurement method.
            freq (double): frequency of the signal in Hz
            twoWay (boolean): Flag indicating whether the measurement is two-way.
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<RangeRate> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.RangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<RangeRate> estimated): estimated measurement to modify
        
        
        """
        ...

class RangeRateTroposphericDelayModifier(BaseRangeRateTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    Class modifying theoretical range-rate measurements with tropospheric delay.
    
    The effect of tropospheric correction on the range-rate is directly computed through the computation of the tropospheric delay difference with respect to time.
    
    In general, for GNSS, VLBI... there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
    Since:
        8.0
    """
    def __init__(self, model: org.orekit.models.earth.troposphere.TroposphericModel, tw: bool):
        """
        Constructor.
        
        Parameters:
            model (TroposphericModel): Tropospheric delay model appropriate for the current range-rate measurement method.
            tw (boolean): Flag indicating whether the measurement is two-way.
        
        Since:
            12.1
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<RangeRate> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.RangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<RangeRate> estimated): estimated measurement to modify
        
        
        """
        ...
    _rangeRateErrorTroposphericModel_1__T = typing.TypeVar('_rangeRateErrorTroposphericModel_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rangeRateErrorTroposphericModel(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Compute the measurement error due to Troposphere.
        
        Overrides: meth:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier.rangeRateErrorTroposphericModel` in class BaseRangeRateTroposphericDelayModifier
        
        Parameters:
            station (GroundStation): station
            state (SpacecraftState): spacecraft state
        
        Returns:
            the measurement error due to Troposphere
        
        """
        ...
    @typing.overload
    def rangeRateErrorTroposphericModel(self, station: org.orekit.estimation.measurements.GroundStation, state: org.orekit.propagation.FieldSpacecraftState[_rangeRateErrorTroposphericModel_1__T], parameters: typing.Union[typing.List[_rangeRateErrorTroposphericModel_1__T], jpype.JArray]) -> _rangeRateErrorTroposphericModel_1__T:
        """
        Compute the measurement error due to Troposphere.
        
        Overrides: meth:`~org.orekit.estimation.measurements.modifiers.BaseRangeRateTroposphericDelayModifier.rangeRateErrorTroposphericModel` in class BaseRangeRateTroposphericDelayModifier
        
        Parameters:
            station (GroundStation): station
            state (FieldSpacecraftState<T> state): spacecraft state
            parameters (T[]): tropospheric model parameters
        
        Returns:
            the measurement error due to Troposphere
        
        
        """
        ...

class RangeTroposphericDelayModifier(BaseRangeTroposphericDelayModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    Class modifying theoretical range measurement with tropospheric delay.
    
    The effect of tropospheric correction on the range is directly computed through the computation of the tropospheric delay.
    
    In general, for GNSS, VLBI... there is hardly any frequency dependence in the delay. For SLR techniques however, the frequency dependence is sensitive.
    
    Since:
        8.0
    """
    def __init__(self, model: org.orekit.models.earth.troposphere.TroposphericModel):
        """
        Constructor.
        
        Parameters:
            model (TroposphericModel): Tropospheric delay model appropriate for the current range measurement method.
        
        Since:
            12.1
        
        
        """
        ...
    def modify(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement.
        
        Specified by: modify in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurement<Range> estimated): estimated measurement to modify
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Range> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockInterSatellitesPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    Class modifying theoretical inter-satellites phase measurement with relativistic clock correction.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockInterSatellitesRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    Class modifying theoretical inter-satellites range measurement with relativistic clock correction.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.InterSatellitesRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesRange> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockOneWayGNSSPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    Class modifying theoretical one-way GNSS phase measurement with relativistic clock correction.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockOneWayGNSSRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    Class modifying theoretical one-way GNSS range measurement with relativistic clock correction.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSRange> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    Class modifying theoretical phase measurement with relativistic clock correction.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Phase> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    Class modifying theoretical range measurement with relativistic clock correction.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Range> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockRangeRateModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    """
    Class modifying theoretical range-rate measurement with relativistic frequency deviation. It works only with orbit-based states.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        10.3
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.RangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<RangeRate> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticJ2ClockInterSatellitesPhaseModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    Class modifying theoretical inter-satellites phase measurements with relativistic J2 clock correction.
    
    Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
    The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
    Since:
        11.2
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Equation 19.18 Springer, 2017."
    """
    def __init__(self, gm: float, c20: float, equatorialRadius: float):
        """
        Modifier constructor.
        
        Parameters:
            gm (double): Earth gravitational constant (mu) in m³/s².
            c20 (double): Earth un-normalized second zonal coefficient (Signed J2 constant, is negative) (Typical value -1.0826e-3).
            equatorialRadius (double): Earth equatorial radius in m.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticJ2ClockInterSatellitesRangeModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    Class modifying theoretical inter-satellites range measurements with relativistic J2 clock correction.
    
    Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
    The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
    Since:
        11.2
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Equation 19.18 Springer, 2017."
    """
    def __init__(self, gm: float, c20: float, equatorialRadius: float):
        """
        Modifier constructor.
        
        Parameters:
            gm (double): Earth gravitational constant (mu) in m³/s².
            c20 (double): Earth un-normalized second zonal coefficient (Signed J2 constant, is negative) (Typical value -1.0826e-3).
            equatorialRadius (double): Earth equatorial radius in m.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.InterSatellitesRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesRange> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticJ2ClockOneWayGNSSPhaseModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    Class modifying theoretical one-way phase measurements with relativistic J2 clock correction.
    
    Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
    The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
    Since:
        11.2
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Equation 19.18 Springer, 2017."
    """
    def __init__(self, gm: float, c20: float, equatorialRadius: float):
        """
        Modifier constructor.
        
        Parameters:
            gm (double): Earth gravitational constant (mu) in m³/s².
            c20 (double): Earth un-normalized second zonal coefficient (Signed J2 constant, is negative) (Typical value -1.0826e-3).
            equatorialRadius (double): Earth equatorial radius in m.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticJ2ClockOneWayGNSSRangeModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    Class modifying one-way GNSS range theoretical measurements with relativistic J2 clock correction.
    
    Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
    The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
    Since:
        11.2
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Equation 19.18 Springer, 2017."
    """
    def __init__(self, gm: float, c20: float, equatorialRadius: float):
        """
        Modifier constructor.
        
        Parameters:
            gm (double): Earth gravitational constant (mu) in m³/s².
            c20 (double): Earth un-normalized second zonal coefficient (Signed J2 constant, is negative) (Typical value -1.0826e-3).
            equatorialRadius (double): Earth equatorial radius in m.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSRange> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticJ2ClockPhaseModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    Class modifying theoretical phase measurements with relativistic J2 clock correction.
    
    Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
    The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
    Since:
        11.2
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Equation 19.18 Springer, 2017."
    """
    def __init__(self, gm: float, c20: float, equatorialRadius: float):
        """
        Modifier constructor.
        
        Parameters:
            gm (double): Earth gravitational constant (mu) in m³/s².
            c20 (double): Earth un-normalized second zonal coefficient (Signed J2 constant, is negative) (Typical value -1.0826e-3).
            equatorialRadius (double): Earth equatorial radius in m.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Phase> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticJ2ClockRangeModifier(AbstractRelativisticJ2ClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    Class modifying theoretical range measurements with relativistic J2 clock correction.
    
    Relativistic clock correction of the effects caused by the oblateness of Earth on the gravity potential.
    
    The time delay caused by this effect is computed based on the orbital parameters of the emitter's orbit.
    
    Since:
        11.2
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Equation 19.18 Springer, 2017."
    """
    def __init__(self, gm: float, c20: float, equatorialRadius: float):
        """
        Modifier constructor.
        
        Parameters:
            gm (double): Earth gravitational constant (mu) in m³/s².
            c20 (double): Earth un-normalized second zonal coefficient (Signed J2 constant, is negative) (Typical value -1.0826e-3).
            equatorialRadius (double): Earth equatorial radius in m.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Range> estimated): estimated measurement to modify
        
        
        """
        ...

class ShapiroInterSatellitePhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    """
    Class modifying theoretical inter-satellites phase measurement with Shapiro time delay.
    
    Shapiro time delay is a relativistic effect due to gravity.
    
    Since:
        10.3
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class ShapiroInterSatelliteRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    """
    Class modifying theoretical range measurement with Shapiro time delay.
    
    Shapiro time delay is a relativistic effect due to gravity.
    
    Since:
        10.0
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.InterSatellitesRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesRange> estimated): estimated measurement to modify
        
        
        """
        ...

class ShapiroOneWayGNSSPhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    """
    Class modifying theoretical one-way GNSS phase measurement with Shapiro time delay.
    
    Shapiro time delay is a relativistic effect due to gravity.
    
    Since:
        10.3
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSPhase> estimated): estimated measurement to modify
        
        
        """
        ...

class ShapiroOneWayGNSSRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    """
    Class modifying theoretical range measurement with Shapiro time delay.
    
    Shapiro time delay is a relativistic effect due to gravity.
    
    Since:
        10.3
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSRange> estimated): estimated measurement to modify
        
        
        """
        ...

class ShapiroPhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    """
    Class modifying theoretical phase measurement with Shapiro time delay.
    
    Shapiro time delay is a relativistic effect due to gravity.
    
    Since:
        10.2
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.Phase]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Phase> estimated): estimated measurement to modify
        
        
        """
        ...

class ShapiroRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    """
    Class modifying theoretical range measurement with Shapiro time delay.
    
    Shapiro time delay is a relativistic effect due to gravity.
    
    Since:
        10.0
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.Range]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Specified by: modifyWithoutDerivatives in interface EstimationModifier
        
        Parameters:
            estimated (EstimatedMeasurementBase<Range> estimated): estimated measurement to modify
        
        
        """
        ...

_PythonAbstractRelativisticClockOnBoardRangeRateModifier__T = typing.TypeVar('_PythonAbstractRelativisticClockOnBoardRangeRateModifier__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonAbstractRelativisticClockOnBoardRangeRateModifier(AbstractRelativisticClockOnBoardRangeRateModifier[_PythonAbstractRelativisticClockOnBoardRangeRateModifier__T], typing.Generic[_PythonAbstractRelativisticClockOnBoardRangeRateModifier__T]):
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.modifiers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[_PythonAbstractRelativisticClockOnBoardRangeRateModifier__T]) -> None:
        """
        Description copied from interface: modifyWithoutDerivatives Apply a modifier to an estimated measurement without derivatives.
        
        Parameters:
            estimated (EstimatedMeasurementBase<PythonAbstractRelativisticClockOnBoardRangeRateModifier> estimated): estimated measurement to modify
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class RelativisticClockInterSatellitesOneWayRangeRateModifier(AbstractRelativisticClockOnBoardRangeRateModifier[org.orekit.estimation.measurements.gnss.InterSatellitesOneWayRangeRate]):
    """
    Class modifying theoretical range-rate measurement with relativistic frequency deviation.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        12.1
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.InterSatellitesOneWayRangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Parameters:
            estimated (EstimatedMeasurementBase<InterSatellitesOneWayRangeRate> estimated): estimated measurement to modify
        
        
        """
        ...

class RelativisticClockOneWayGNSSRangeRateModifier(AbstractRelativisticClockOnBoardRangeRateModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRangeRate]):
    """
    Class modifying theoretical range-rate measurement with relativistic frequency deviation. It works only with orbit-based states.
    
    Relativistic clock correction is caused by the motion of the satellite as well as the change in the gravitational potential
    
    Since:
        12.1
    
    Also see:
        "Teunissen, Peter, and Oliver Montenbruck, eds. Springer handbook of global navigation satellite systems. Chapter 19.2.
        Springer, 2017."
    """
    def __init__(self, gm: float):
        """
        Simple constructor.
        
        Parameters:
            gm (double): gravitational constant for main body in signal path vicinity.
        
        
        """
        ...
    def modifyWithoutDerivatives(self, estimated: org.orekit.estimation.measurements.EstimatedMeasurementBase[org.orekit.estimation.measurements.gnss.OneWayGNSSRangeRate]) -> None:
        """
        Apply a modifier to an estimated measurement without derivatives.
        
        Parameters:
            estimated (EstimatedMeasurementBase<OneWayGNSSRangeRate> estimated): estimated measurement to modify
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.modifiers")``.

    AberrationModifier: typing.Type[AberrationModifier]
    AbstractRelativisticClockModifier: typing.Type[AbstractRelativisticClockModifier]
    AbstractRelativisticClockOnBoardRangeRateModifier: typing.Type[AbstractRelativisticClockOnBoardRangeRateModifier]
    AbstractRelativisticJ2ClockModifier: typing.Type[AbstractRelativisticJ2ClockModifier]
    AbstractShapiroBaseModifier: typing.Type[AbstractShapiroBaseModifier]
    AngularIonosphericDelayModifier: typing.Type[AngularIonosphericDelayModifier]
    AngularRadioRefractionModifier: typing.Type[AngularRadioRefractionModifier]
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
    ModifierGradientConverter: typing.Type[ModifierGradientConverter]
    OnBoardAntennaInterSatellitesPhaseModifier: typing.Type[OnBoardAntennaInterSatellitesPhaseModifier]
    OnBoardAntennaInterSatellitesRangeModifier: typing.Type[OnBoardAntennaInterSatellitesRangeModifier]
    OnBoardAntennaOneWayGNSSPhaseModifier: typing.Type[OnBoardAntennaOneWayGNSSPhaseModifier]
    OnBoardAntennaOneWayGNSSRangeModifier: typing.Type[OnBoardAntennaOneWayGNSSRangeModifier]
    OnBoardAntennaTurnAroundRangeModifier: typing.Type[OnBoardAntennaTurnAroundRangeModifier]
    OutlierFilter: typing.Type[OutlierFilter]
    ParametricModelEffect: typing.Type[ParametricModelEffect]
    ParametricModelEffectGradient: typing.Type[ParametricModelEffectGradient]
    PhaseCentersGroundReceiverBaseModifier: typing.Type[PhaseCentersGroundReceiverBaseModifier]
    PhaseCentersInterSatellitesBaseModifier: typing.Type[PhaseCentersInterSatellitesBaseModifier]
    PhaseCentersOffsetComputer: typing.Type[PhaseCentersOffsetComputer]
    PhaseCentersOneWayGNSSBaseModifier: typing.Type[PhaseCentersOneWayGNSSBaseModifier]
    PhaseCentersPhaseModifier: typing.Type[PhaseCentersPhaseModifier]
    PhaseCentersRangeModifier: typing.Type[PhaseCentersRangeModifier]
    PhaseIonosphericDelayModifier: typing.Type[PhaseIonosphericDelayModifier]
    PhaseTroposphericDelayModifier: typing.Type[PhaseTroposphericDelayModifier]
    PythonAbstractRelativisticClockOnBoardRangeRateModifier: typing.Type[PythonAbstractRelativisticClockOnBoardRangeRateModifier]
    PythonParametricModelEffect: typing.Type[PythonParametricModelEffect]
    PythonParametricModelEffectGradient: typing.Type[PythonParametricModelEffectGradient]
    RangeIonosphericDelayModifier: typing.Type[RangeIonosphericDelayModifier]
    RangeModifierUtil: typing.Type[RangeModifierUtil]
    RangeRateIonosphericDelayModifier: typing.Type[RangeRateIonosphericDelayModifier]
    RangeRateModifierUtil: typing.Type[RangeRateModifierUtil]
    RangeRateTroposphericDelayModifier: typing.Type[RangeRateTroposphericDelayModifier]
    RangeTroposphericDelayModifier: typing.Type[RangeTroposphericDelayModifier]
    RelativisticClockInterSatellitesOneWayRangeRateModifier: typing.Type[RelativisticClockInterSatellitesOneWayRangeRateModifier]
    RelativisticClockInterSatellitesPhaseModifier: typing.Type[RelativisticClockInterSatellitesPhaseModifier]
    RelativisticClockInterSatellitesRangeModifier: typing.Type[RelativisticClockInterSatellitesRangeModifier]
    RelativisticClockOneWayGNSSPhaseModifier: typing.Type[RelativisticClockOneWayGNSSPhaseModifier]
    RelativisticClockOneWayGNSSRangeModifier: typing.Type[RelativisticClockOneWayGNSSRangeModifier]
    RelativisticClockOneWayGNSSRangeRateModifier: typing.Type[RelativisticClockOneWayGNSSRangeRateModifier]
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
    TurnAroundRangeIonosphericDelayModifier: typing.Type[TurnAroundRangeIonosphericDelayModifier]
    TurnAroundRangeTroposphericDelayModifier: typing.Type[TurnAroundRangeTroposphericDelayModifier]
