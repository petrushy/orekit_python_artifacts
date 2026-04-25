
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.forces
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class KnockeRediffusedForceModel(org.orekit.forces.ForceModel):
    """
    The Knocke Earth Albedo and IR emission force model.
    
    This model is based on "EARTH RADIATION PRESSURE EFFECTS ON SATELLITES", 1988, by P. C. Knocke, J. C. Ries, and B. D. Tapley.
    
    This model represents the effects of radiation pressure coming from the Earth. It considers Solar radiation which has been reflected by Earth (albedo) and Earth infrared emissions. The planet is considered as a sphere and is divided into elementary areas. Each elementary area is considered as a plane and emits radiation according to Lambert's law. The flux the satellite receives is then equal to the sum of the elementary fluxes coming from Earth.
    
    The radiative model of the satellite, and its ability to diffuse, reflect or absorb radiation is handled by a RadiationSensitive.
    
    Caution: This model is only suitable for Earth. Using it with another central body is prone to error..
    
    Since:
        10.3
    """
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], radiationSensitive: 'RadiationSensitive', double: float, double2: float): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], radiationSensitive: 'RadiationSensitive', double: float, double2: float, timeScale: org.orekit.time.TimeScale): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    _computeAlbedo_1__T = typing.TypeVar('_computeAlbedo_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeAlbedo(self, date: org.orekit.time.AbsoluteDate, phi: float) -> float:
        """
        Compute Earth albedo. Albedo value represents the fraction of solar radiative flux that is reflected by Earth. Its value is in [0;1].
        
        Parameters:
            date (AbsoluteDate): the date
            phi (double): the equatorial latitude in rad
        
        Returns:
            the albedo in [0;1]
        
        """
        ...
    @typing.overload
    def computeAlbedo(self, date: org.orekit.time.FieldAbsoluteDate[_computeAlbedo_1__T], phi: _computeAlbedo_1__T) -> _computeAlbedo_1__T:
        """
        Compute Earth albedo. Albedo value represents the fraction of solar radiative flux that is reflected by Earth. Its value is in [0;1].
        
        Parameters:
            date (FieldAbsoluteDate<T> date): the date
            phi (T): the equatorial latitude in rad
        
        Returns:
            the albedo in [0;1]
        
        
        """
        ...
    _computeElementaryFlux_0__T = typing.TypeVar('_computeElementaryFlux_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeElementaryFlux(self, state: org.orekit.propagation.FieldSpacecraftState[_computeElementaryFlux_0__T], elementCenter: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeElementaryFlux_0__T], sunPosition: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeElementaryFlux_0__T], elementArea: _computeElementaryFlux_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeElementaryFlux_0__T]:
        """
        Compute elementary rediffused flux on satellite.
        
        Parameters:
            state (FieldSpacecraftState<T> state): the current spacecraft state
            elementCenter (FieldVector3D<T> elementCenter): the position of the considered area center
            sunPosition (FieldVector3D<T> sunPosition): the position of the Sun in the spacecraft frame
            elementArea (T): the area of the current element
        
        Returns:
            the rediffused flux from considered element on the spacecraft
        
        
        """
        ...
    @typing.overload
    def computeElementaryFlux(self, state: org.orekit.propagation.SpacecraftState, elementCenter: org.hipparchus.geometry.euclidean.threed.Vector3D, sunPosition: org.hipparchus.geometry.euclidean.threed.Vector3D, elementArea: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute elementary rediffused flux on satellite.
        
        Parameters:
            state (SpacecraftState): the current spacecraft state
            elementCenter (Vector3D): the position of the considered area center
            sunPosition (Vector3D): the position of the Sun in the spacecraft frame
            elementArea (double): the area of the current element
        
        Returns:
            the rediffused flux from considered element on the spacecraft
        
        """
        ...
    _computeEmissivity_1__T = typing.TypeVar('_computeEmissivity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeEmissivity(self, date: org.orekit.time.AbsoluteDate, phi: float) -> float:
        """
        Compute Earth emisivity. Emissivity is used to compute the infrared flux that is emitted by Earth. Its value is in [0;1].
        
        Parameters:
            date (AbsoluteDate): the date
            phi (double): the equatorial latitude in rad
        
        Returns:
            the emissivity in [0;1]
        
        """
        ...
    @typing.overload
    def computeEmissivity(self, date: org.orekit.time.FieldAbsoluteDate[_computeEmissivity_1__T], phi: _computeEmissivity_1__T) -> _computeEmissivity_1__T:
        """
        Compute Earth emisivity. Emissivity is used to compute the infrared flux that is emitted by Earth. Its value is in [0;1].
        
        Parameters:
            date (FieldAbsoluteDate<T> date): the date
            phi (T): the equatorial latitude in rad
        
        Returns:
            the emissivity in [0;1]
        
        
        """
        ...
    _computeSolarFlux_1__T = typing.TypeVar('_computeSolarFlux_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeSolarFlux(self, sunPosition: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
        Compute total solar flux impacting Earth.
        
        Parameters:
            sunPosition (Vector3D): the Sun position in an Earth centered frame
        
        Returns:
            the total solar flux impacting Earth in J/m^3
        
        """
        ...
    @typing.overload
    def computeSolarFlux(self, sunPosition: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeSolarFlux_1__T]) -> _computeSolarFlux_1__T:
        """
        Compute total solar flux impacting Earth.
        
        Parameters:
            sunPosition (FieldVector3D<T> sunPosition): the Sun position in an Earth centered frame
        
        Returns:
            the total solar flux impacting Earth in J/m^3
        
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
        Check if force model depends on position only at a given, fixed date.
        
        Specified by: dependsOnPositionOnly in interface ForceModel
        
        Returns:
            true if force model depends on position only, false if it depends on mass or velocity, either directly or due to a
            dependency on attitude
        
        
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

class LightFluxModel:
    """
    Interface describing flux models from a light source, including shadowing effects from occulting bodies. Defines the flux vector itself as well as detectors for entry and exit of the different eclipse zones, if any.
    
    Since:
        12.1
    """
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]:
        """
        Retrieve detectors finding entries and exits in different eclipse zones.
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]:
        """
        Retrieve Field detectors finding entries and exits in different eclipse zones.
        
        Parameters:
            field (Field<T> field): calculus field
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getLightFluxVector_0__T = typing.TypeVar('_getLightFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightFluxVector(self, state: org.orekit.propagation.FieldSpacecraftState[_getLightFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightFluxVector_0__T]:
        """
        Get the light flux vector in the state's frame. Field version.
        
        Parameters:
            state (FieldSpacecraftState<T> state): state
        
        Returns:
            light flux
        
        
        """
        ...
    @typing.overload
    def getLightFluxVector(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the light flux vector in the state's frame.
        
        Parameters:
            state (SpacecraftState): state
        
        Returns:
            light flux
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], targetDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Perform initialization steps before starting propagation.
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): initial state
            targetDate (FieldAbsoluteDate<T> targetDate): target date for propagation
        
        Since:
            12.2
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, targetDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Perform initialization steps before starting propagation.
        
        Parameters:
            initialState (SpacecraftState): initial state
            targetDate (AbsoluteDate): target date for propagation
        
        Since:
            12.2
        
        """
        ...

class RadiationForceModel(org.orekit.forces.ForceModel):
    """
    Interface for radiation-related force models.
    
    Since:
        12.1
    """
    def dependsOnPositionOnly(self) -> bool:
        """
        Check if force model depends on position only at a given, fixed date.
        
        Specified by: dependsOnPositionOnly in interface ForceModel
        
        Returns:
            true if force model depends on position only, false if it depends on mass or velocity, either directly or due to a
            dependency on attitude
        
        
        """
        ...

class RadiationSensitive:
    """
    Interface for spacecraft that are sensitive to radiation pressure forces.
    
    Also see:
        SolarRadiationPressure
    """
    GLOBAL_RADIATION_FACTOR: typing.ClassVar[str] = ...
    """
    Parameter name for global multiplicative factor.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    ABSORPTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    Parameter name for absorption coefficient.
    
    Also see:
        constant
    
    
    """
    REFLECTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    Parameter name for reflection coefficient.
    
    Also see:
        constant
    
    
    """
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Returns:
            parameters drivers
        
        Since:
            8.0
        
        
        """
        ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], flux: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], parameters: typing.Union[typing.List[_radiationPressureAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
        Compute the acceleration due to radiation pressure.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.SpacecraftState, flux: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to radiation pressure.
        
        Parameters:
            state (SpacecraftState): current state
            flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        Since:
            12.0
        
        """
        ...

class AbstractLightFluxModel(LightFluxModel):
    """
    Abstract class for light flux models. Via the definition of the lighting ratio and the unocculted flux vector, derives the final value.
    
    Since:
        12.1
    
    Also see:
        LightFluxModel
    """
    _getLightFluxVector_0__T = typing.TypeVar('_getLightFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightFluxVector(self, state: org.orekit.propagation.FieldSpacecraftState[_getLightFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightFluxVector_0__T]:
        """
        Get the light flux vector in the state's frame. Field version.
        
        Specified by: getLightFluxVector in interface LightFluxModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): state
        
        Returns:
            light flux
        
        
        """
        ...
    @typing.overload
    def getLightFluxVector(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the light flux vector in the state's frame.
        
        Specified by: getLightFluxVector in interface LightFluxModel
        
        Parameters:
            state (SpacecraftState): state
        
        Returns:
            light flux
        
        """
        ...
    _getLightingRatio_1__T = typing.TypeVar('_getLightingRatio_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightingRatio(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
        Parameters:
            state (SpacecraftState): state
        
        Returns:
            lighting ratio
        
        Get the lighting ratio ([0-1]).
        
        Parameters:
            position (Vector3D): object's position
            occultedBodyPosition (Vector3D): occulted body position in same frame
        
        Returns:
            lighting ratio
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightingRatio_1__T]) -> _getLightingRatio_1__T:
        """
        Parameters:
            state (FieldSpacecraftState<T> state): state
        
        Returns:
            lighting ratio
        
        protected abstract <T extends CalculusFieldElement<T>> T getLightingRatio (FieldVector3D<T> position, FieldVector3D<T> occultedBodyPosition)
        
        Get the lighting ratio ([0-1]). Field version.
        
        Parameters:
            position (FieldVector3D<T> position): object's position
            occultedBodyPosition (FieldVector3D<T> occultedBodyPosition): occulted body position in same frame
        
        Returns:
            lighting ratio
        
        
        """
        ...
    def getOccultedBody(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Getter for the occulted body's position provider.
        
        Returns:
            occulted body
        
        
        """
        ...

class AbstractRadiationForceModel(RadiationForceModel):
    """
    Base class for radiation force models.
    
    Since:
        10.2
    
    Also see:
        SolarRadiationPressure, ECOM2
    """
    @typing.overload
    def addOccultingBody(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid) -> None:
        """
        Add a new occulting body.
        
        Central body is already considered, it shall not be added this way.
        
        Parameters:
            provider (ExtendedPositionProvider): body PV provider
            radius (double): body mean radius
        
        Also see:
            addOccultingBody
        
        Add a new occulting body.
        
        Central body is already considered, it shall not be added this way.
        
        Parameters:
            occulting (OneAxisEllipsoid): occulting body to add
        
        Since:
            12.0
        
        Also see:
            addOccultingBody
        
        
        """
        ...
    @typing.overload
    def addOccultingBody(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double: float) -> None: ...
    @staticmethod
    def getDefaultEclipseDetectionSettings() -> org.orekit.propagation.events.EventDetectionSettings:
        """
        Get the default eclipse detection settings.
        
        Returns:
            detection settings
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    def getOccultingBodies(self) -> java.util.List[org.orekit.utils.OccultationEngine]:
        """
        Get all occulting bodies to consider.
        
        The list always contains at least one element: the central body which is always the first one in the list.
        
        Returns:
            immutable list of all occulting bodies to consider, including the central body
        
        Since:
            12.0
        
        
        """
        ...

class IsotropicRadiationCNES95Convention(RadiationSensitive):
    """
    This class represents the features of a simplified spacecraft.
    
    This model uses the coefficients described in the collective book edited by CNES in 1995: Spaceflight Dynamics (part I), in section 5.2.2.1.3.1 (page 296 of the English edition). The absorption coefficient is called α and the specular reflection coefficient is called τ. A comment in section 5.2.2.1.3.2 of the same book reads:
    
     Some authors prefer to express thermo-optical properties for surfaces using the following coefficients: Ka = α, Ks = (1-α)τ, Kd = (1-α)(1-τ)
    
    Ka is the same absorption coefficient, and Ks is also called specular reflection coefficient, which leads to a confusion. In fact, as the Ka, Ks and Kd coefficients are the most frequently used ones (using the names Ca, Cs and Cd), when speaking about reflection coefficients, it is more often Cd that is considered rather than τ.
    
    The classical set of coefficients Ca, Cs, and Cd are implemented in the sister class IsotropicRadiationClassicalConvention, which should probably be preferred to this legacy class.
    
    Since:
        7.1
    
    Also see:
        BoxAndSolarArraySpacecraft, IsotropicDrag,
        IsotropicRadiationClassicalConvention
    """
    def __init__(self, crossSection: float, alpha: float, tau: float):
        """
        Simple constructor.
        
        Parameters:
            crossSection (double): Surface (m²)
            alpha (double): absorption coefficient α between 0.0 an 1.0
            tau (double): specular reflection coefficient τ between 0.0 an 1.0
        
        
        """
        ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Specified by: getRadiationParametersDrivers in interface RadiationSensitive
        
        Returns:
            parameters drivers
        
        
        """
        ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], flux: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], parameters: typing.Union[typing.List[_radiationPressureAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.SpacecraftState, flux: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (SpacecraftState): current state
            flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class IsotropicRadiationClassicalConvention(RadiationSensitive):
    """
    This class represents the features of a simplified spacecraft.
    
    This model uses the classical thermo-optical coefficients Ca for absorption, Cs for specular reflection and Cd for diffuse reflection. The equation Ca + Cs + Cd = 1 always holds.
    
    A less standard set of coefficients α = Ca for absorption and τ = Cs/(1-Ca) for specular reflection is implemented in the sister class IsotropicRadiationCNES95Convention.
    
    Since:
        7.1
    
    Also see:
        BoxAndSolarArraySpacecraft, IsotropicDrag,
        IsotropicRadiationCNES95Convention
    """
    def __init__(self, crossSection: float, ca: float, cs: float):
        """
        Simple constructor.
        
        Parameters:
            crossSection (double): Surface (m²)
            ca (double): absorption coefficient Ca between 0.0 an 1.0
            cs (double): specular reflection coefficient Cs between 0.0 an 1.0
        
        
        """
        ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Specified by: getRadiationParametersDrivers in interface RadiationSensitive
        
        Returns:
            parameters drivers
        
        
        """
        ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], flux: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], parameters: typing.Union[typing.List[_radiationPressureAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.SpacecraftState, flux: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (SpacecraftState): current state
            flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class IsotropicRadiationSingleCoefficient(RadiationSensitive):
    """
    This class represents the features of a simplified spacecraft.
    
    This model uses a single coefficient cr, considered to be a REFLECTION_COEFFICIENT.
    
    Since:
        7.1
    
    Also see:
        BoxAndSolarArraySpacecraft, IsotropicDrag,
        IsotropicRadiationCNES95Convention
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Specified by: getRadiationParametersDrivers in interface RadiationSensitive
        
        Returns:
            parameters drivers
        
        
        """
        ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], flux: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], parameters: typing.Union[typing.List[_radiationPressureAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.SpacecraftState, flux: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (SpacecraftState): current state
            flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class PythonLightFluxModel(LightFluxModel):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]:
        """
        Retrieve detectors finding entries and exits in different eclipse zones.
        
        Specified by: getEclipseConditionsDetector in interface LightFluxModel
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]:
        """
        Retrieve Field detectors finding entries and exits in different eclipse zones.
        
        Specified by: getFieldEclipseConditionsDetector in interface LightFluxModel
        
        Parameters:
            field (Field<T> field): calculus field
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getLightFluxVector_0__T = typing.TypeVar('_getLightFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightFluxVector(self, state: org.orekit.propagation.FieldSpacecraftState[_getLightFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightFluxVector_0__T]:
        """
        Get the light flux vector in the state's frame. Field version.
        
        Specified by: getLightFluxVector in interface LightFluxModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): state
        
        Returns:
            light flux
        
        
        """
        ...
    @typing.overload
    def getLightFluxVector(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the light flux vector in the state's frame.
        
        Specified by: getLightFluxVector in interface LightFluxModel
        
        Parameters:
            state (SpacecraftState): state
        
        Returns:
            light flux
        
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

class PythonRadiationForceModel(RadiationForceModel):
    def __init__(self): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
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

class PythonRadiationSensitive(RadiationSensitive):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Specified by: getRadiationParametersDrivers in interface RadiationSensitive
        
        Returns:
            parameters drivers
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], flux: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], parameters: typing.Union[typing.List[_radiationPressureAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, state: org.orekit.propagation.SpacecraftState, flux: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to radiation pressure.
        
        Specified by: radiationPressureAcceleration in interface RadiationSensitive
        
        Parameters:
            state (SpacecraftState): current state
            flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class RadiationPressureModel(RadiationForceModel):
    """
    Class representing a light-induced radiation pressure force, by leveraging on a given flux model.
    
    This class should not be used in addition to SolarRadiationPressure, which is another way of representing the same orbital perturbation.
    
    Since:
        12.1
    
    Also see:
        LightFluxModel, RadiationSensitive
    """
    def __init__(self, lightFluxModel: LightFluxModel, radiationSensitive: RadiationSensitive):
        """
        Constructor.
        
        Parameters:
            lightFluxModel (LightFluxModel): model for light flux
            radiationSensitive (RadiationSensitive): object defining radiation properties
        
        
        """
        ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    def getLightFluxModel(self) -> LightFluxModel:
        """
        Getter for light flux model.
        
        Returns:
            flux model
        
        
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
    def getRadiationSensitive(self) -> RadiationSensitive:
        """
        Getter for radiation sensitive object.
        
        Returns:
            radiation sensitive object
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Initialize the force model at the start of propagation. This method will be called before any calls to addContribution, addContribution, acceleration or acceleration
        
        The default implementation of this method does nothing.
        
        Specified by: init in interface ForceModel
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): spacecraft state at the start of propagation.
            target (FieldAbsoluteDate<T> target): date of propagation. Not equal to getDate().
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the force model at the start of propagation. This method will be called before any calls to addContribution, addContribution, acceleration or acceleration
        
        The default implementation of this method does nothing.
        
        Specified by: init in interface ForceModel
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...

class AbstractSolarLightFluxModel(AbstractLightFluxModel):
    """
    Abstract class for the definition of the solar flux model with a single occulting body of spherical shape.
    
    Since:
        12.2
    
    Also see:
        LightFluxModel
    """
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.EventDetectionSettings:
        """
        Getter for eclipse event detection settings used for eclipses.
        
        Returns:
            event detection settings
        
        
        """
        ...
    def getOccultingBodyRadius(self) -> float:
        """
        Getter for occulting body radius.
        
        Returns:
            radius
        
        
        """
        ...

class ECOM2(AbstractRadiationForceModel):
    """
    The Empirical CODE Orbit Model 2 (ECOM2) of the Center for Orbit Determination in Europe (CODE).
    
    The drag acceleration is computed as follows : γ = γ :sub:`0` + D(u)e :sub:`D` + Y(u)e :sub:`Y` + B(u)e :sub:`B`
    
    In the above equation, γ :sub:`0` is a selectable a priori model. Since 2013, no a priori model is used for CODE IGS contribution (i.e. γ :sub:`0` = 0). Moreover, u denotes the satellite's argument of latitude.
    
    D(u), Y(u) and B(u) are three functions of the ECOM2 model that can be represented as Fourier series. The coefficients of the Fourier series are estimated during the estimation process. he ECOM2 model has user-defines upper limits nD and nB for the Fourier series (i.e. nD for D(u) and nB for B(u). Y(u) is defined as a constant value).
    
    It exists several configurations to initialize nD and nB values. However, Arnold et al recommend to use D2B1 (i.e. nD = 1 and nB = 1) and D4B1 (i.e. nD = 2 an nB = 1) configurations. At the opposite, in Arnold paper, it is recommend to not use D2B0 (i.e. nD = 1 and nB = 0) configuration.
    
    Since Orekit 11.0, it is possible to take into account the eclipses generated by Moon in the solar radiation pressure force model using the addOccultingBody method.
    
    
    ECOM2 srp = EIGEN5C_EARTH_EQUATORIAL_RADIUS);
    
    
    MOON_EQUATORIAL_RADIUS);
    
    
    
    Since:
        10.2
    
    Also see:
        "Arnold, Daniel, et al, CODE’s new solar radiation pressure model for GNSS orbit determination, Journal of geodesy
        89.8 (2015): 775-791.", "Tzu-Pang tseng and Michael Moore, Impact of solar radiation pressure mis-modeling on GNSS
        satellite orbit determination, IGS Worshop, Wuhan, China, 2018."
    """
    ECOM_COEFFICIENT: typing.ClassVar[str] = ...
    """
    Parameter name for ECOM model coefficients enabling Jacobian processing.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double2: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double2: float, frames: org.orekit.frames.Frames): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...

class PythonAbstractLightFluxModel(AbstractLightFluxModel):
    def __init__(self, occultedBody: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]):
        """
        Constructor.
        
        Parameters:
            occultedBody (ExtendedPositionProvider): position provider for light source
        
        
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
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]:
        """
        Description copied from interface: getEclipseConditionsDetector Retrieve detectors finding entries and exits in different eclipse zones.
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]:
        """
        Description copied from interface: getFieldEclipseConditionsDetector Retrieve Field detectors finding entries and exits in different eclipse zones.
        
        Parameters:
            field (Field<T> field): calculus field
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getLightingRatio_2__T = typing.TypeVar('_getLightingRatio_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getLightingRatio_3__T = typing.TypeVar('_getLightingRatio_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightingRatio(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
        Description copied from class: getLightingRatio Get the lighting ratio ([0-1]).
        
        Specified by: getLightingRatio in class AbstractLightFluxModel
        
        Parameters:
            position (Vector3D): object's position
            occultedBodyPosition (Vector3D): occulted body position in same frame
        
        Returns:
            lighting ratio
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float: ...
    @typing.overload
    def getLightingRatio(self, position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightingRatio_2__T], occultedBodyPosition: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightingRatio_2__T]) -> _getLightingRatio_2__T:
        """
        Description copied from class: getLightingRatio Get the lighting ratio ([0-1]). Field version.
        
        Specified by: getLightingRatio in class AbstractLightFluxModel
        
        Parameters:
            position (FieldVector3D<T> position): object's position
            occultedBodyPosition (FieldVector3D<T> occultedBodyPosition): occulted body position in same frame
        
        Returns:
            lighting ratio
        
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightingRatio_3__T]) -> _getLightingRatio_3__T: ...
    _getUnoccultedFluxVector_0__T = typing.TypeVar('_getUnoccultedFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getUnoccultedFluxVector(self, relativePosition: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getUnoccultedFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getUnoccultedFluxVector_0__T]:
        """
        Description copied from class: getUnoccultedFluxVector Get the light flux vector, not considering any shadowing effect. Field version.
        
        Specified by: getUnoccultedFluxVector in class AbstractLightFluxModel
        
        Parameters:
            relativePosition (FieldVector3D<T> relativePosition): relative position w.r.t. light source
        
        Returns:
            unocculted flux
        
        
        """
        ...
    @typing.overload
    def getUnoccultedFluxVector(self, relativePosition: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from class: getUnoccultedFluxVector Get the light flux vector, not considering any shadowing effect.
        
        Specified by: getUnoccultedFluxVector in class AbstractLightFluxModel
        
        Parameters:
            relativePosition (Vector3D): relative position w.r.t. light source
        
        Returns:
            unocculted flux
        
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

class SolarRadiationPressure(AbstractRadiationForceModel):
    """
    Solar radiation pressure force model.
    
    Since Orekit 11.0, it is possible to take into account the eclipses generated by Moon in the solar radiation pressure force model using the addOccultingBody method.
    
    Example:
    
    
    SolarRadiationPressure srp = EIGEN5C_EARTH_EQUATORIAL_RADIUS, 5));
    
    
    MOON_EQUATORIAL_RADIUS);
    """
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, radiationSensitive: RadiationSensitive): ...
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, radiationSensitive: RadiationSensitive, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, radiationSensitive: RadiationSensitive): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    _getLightingRatio_1__T = typing.TypeVar('_getLightingRatio_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightingRatio(self, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            lighting ratio
        
        Since:
            7.1
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, state: org.orekit.propagation.FieldSpacecraftState[_getLightingRatio_1__T]) -> _getLightingRatio_1__T:
        """
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
        
        Returns:
            lighting ratio
        
        Since:
            7.1
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getRadiationSensitiveSpacecraft(self) -> RadiationSensitive:
        """
        Getter for radiation-sensitive spacecraft.
        
        Returns:
            radiation-sensitive model
        
        Since:
            12.1
        
        
        """
        ...

class ConicallyShadowedLightFluxModel(AbstractSolarLightFluxModel):
    """
    Class defining a flux model from a single occulted body, casting a shadow on a spherical occulting body. It cannot model oblate bodies or multiple occulting objects (for this, see SolarRadiationPressure).
    
    Since:
        12.2
    
    Also see:
        AbstractSolarLightFluxModel, LightFluxModel,
        "Montenbruck, Oliver, and Gill, Eberhard. Satellite orbits : models, methods, and * applications. Berlin New York:
        Springer, 2000."
    """
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double3: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def __init__(self, double: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double2: float): ...
    @staticmethod
    def getDefaultEclipseDetectionSettings() -> org.orekit.propagation.events.EventDetectionSettings:
        """
        Define default detection settings for eclipses.
        
        Returns:
            default settings
        
        
        """
        ...
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]:
        """
        Retrieve detectors finding entries and exits in different eclipse zones.
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]:
        """
        Retrieve Field detectors finding entries and exits in different eclipse zones.
        
        Parameters:
            field (Field<T> field): calculus field
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], targetDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Perform initialization steps before starting propagation.
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): initial state
            targetDate (FieldAbsoluteDate<T> targetDate): target date for propagation
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, targetDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Perform initialization steps before starting propagation.
        
        Parameters:
            initialState (SpacecraftState): initial state
            targetDate (AbsoluteDate): target date for propagation
        
        """
        ...

class CylindricallyShadowedLightFluxModel(AbstractSolarLightFluxModel):
    """
    Class defining a flux model with a single occulting body, casting a shadow whose shape is a circular cylinder (equivalent to the light source being infinitely distant). It is less accurate but faster to evaluate than a conical model.
    
    Since:
        12.1
    
    Also see:
        AbstractSolarLightFluxModel, LightFluxModel
    """
    @typing.overload
    def __init__(self, double: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double2: float): ...
    @typing.overload
    def __init__(self, double: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double2: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double: float): ...
    @staticmethod
    def getDefaultEclipseDetectionSettings() -> org.orekit.propagation.events.EventDetectionSettings:
        """
        Define default detection settings for eclipses.
        
        Returns:
            default settings
        
        Since:
            12.2
        
        
        """
        ...
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]:
        """
        Retrieve detectors finding entries and exits in different eclipse zones.
        
        Returns:
            list of event detectors
        
        
        """
        ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]:
        """
        Retrieve Field detectors finding entries and exits in different eclipse zones.
        
        Parameters:
            field (Field<T> field): calculus field
        
        Returns:
            list of event detectors
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.radiation")``.

    AbstractLightFluxModel: typing.Type[AbstractLightFluxModel]
    AbstractRadiationForceModel: typing.Type[AbstractRadiationForceModel]
    AbstractSolarLightFluxModel: typing.Type[AbstractSolarLightFluxModel]
    ConicallyShadowedLightFluxModel: typing.Type[ConicallyShadowedLightFluxModel]
    CylindricallyShadowedLightFluxModel: typing.Type[CylindricallyShadowedLightFluxModel]
    ECOM2: typing.Type[ECOM2]
    IsotropicRadiationCNES95Convention: typing.Type[IsotropicRadiationCNES95Convention]
    IsotropicRadiationClassicalConvention: typing.Type[IsotropicRadiationClassicalConvention]
    IsotropicRadiationSingleCoefficient: typing.Type[IsotropicRadiationSingleCoefficient]
    KnockeRediffusedForceModel: typing.Type[KnockeRediffusedForceModel]
    LightFluxModel: typing.Type[LightFluxModel]
    PythonAbstractLightFluxModel: typing.Type[PythonAbstractLightFluxModel]
    PythonLightFluxModel: typing.Type[PythonLightFluxModel]
    PythonRadiationForceModel: typing.Type[PythonRadiationForceModel]
    PythonRadiationSensitive: typing.Type[PythonRadiationSensitive]
    RadiationForceModel: typing.Type[RadiationForceModel]
    RadiationPressureModel: typing.Type[RadiationPressureModel]
    RadiationSensitive: typing.Type[RadiationSensitive]
    SolarRadiationPressure: typing.Type[SolarRadiationPressure]
