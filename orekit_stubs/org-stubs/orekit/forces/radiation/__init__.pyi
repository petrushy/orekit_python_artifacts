import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.forces
import org.orekit.forces.radiation.class-use
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class KnockeRediffusedForceModel(org.orekit.forces.ForceModel):
    """
    public class KnockeRediffusedForceModel extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.ForceModel`
    
        The Knocke Earth Albedo and IR emission force model.
    
        This model is based on "EARTH RADIATION PRESSURE EFFECTS ON SATELLITES", 1988, by P. C. Knocke, J. C. Ries, and B. D.
        Tapley.
    
        This model represents the effects of radiation pressure coming from the Earth. It considers Solar radiation which has
        been reflected by Earth (albedo) and Earth infrared emissions. The planet is considered as a sphere and is divided into
        elementary areas. Each elementary area is considered as a plane and emits radiation according to Lambert's law. The flux
        the satellite receives is then equal to the sum of the elementary fluxes coming from Earth.
    
        The radiative model of the satellite, and its ability to diffuse, reflect or absorb radiation is handled by a
        :class:`~org.orekit.forces.radiation.RadiationSensitive`.
    
        **Caution:** This model is only suitable for Earth. Using it with another central body is prone to error..
    
        Since:
            10.3
    """
    @typing.overload
    def __init__(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, radiationSensitive: 'RadiationSensitive', double: float, double2: float): ...
    @typing.overload
    def __init__(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, radiationSensitive: 'RadiationSensitive', double: float, double2: float, timeScale: org.orekit.time.TimeScale): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    _computeAlbedo_1__T = typing.TypeVar('_computeAlbedo_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeAlbedo(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Compute Earth albedo. Albedo value represents the fraction of solar radiative flux that is reflected by Earth. Its value
            is in [0;1].
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the date
                phi (double): the equatorial latitude in rad
        
            Returns:
                the albedo in [0;1]
        
        """
        ...
    @typing.overload
    def computeAlbedo(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeAlbedo_1__T], t: _computeAlbedo_1__T) -> _computeAlbedo_1__T:
        """
            Compute Earth albedo. Albedo value represents the fraction of solar radiative flux that is reflected by Earth. Its value
            is in [0;1].
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date
                phi (T): the equatorial latitude in rad
        
            Returns:
                the albedo in [0;1]
        
        
        """
        ...
    _computeElementaryFlux_0__T = typing.TypeVar('_computeElementaryFlux_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeElementaryFlux(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_computeElementaryFlux_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeElementaryFlux_0__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeElementaryFlux_0__T], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, t: _computeElementaryFlux_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeElementaryFlux_0__T]:
        """
            Compute elementary rediffused flux on satellite.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): the current spacecraft state
                elementCenter (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> elementCenter): the position of the considered area center
                sunPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> sunPosition): the position of the Sun in the spacecraft frame
                earth (:class:`~org.orekit.bodies.OneAxisEllipsoid`): the Earth model
                elementArea (T): the area of the current element
        
            Returns:
                the rediffused flux from considered element on the spacecraft
        
        
        """
        ...
    @typing.overload
    def computeElementaryFlux(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute elementary rediffused flux on satellite.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): the current spacecraft state
                elementCenter (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): the position of the considered area center
                sunPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): the position of the Sun in the spacecraft frame
                earth (:class:`~org.orekit.bodies.OneAxisEllipsoid`): the Earth model
                elementArea (double): the area of the current element
        
            Returns:
                the rediffused flux from considered element on the spacecraft
        
        """
        ...
    _computeEmissivity_1__T = typing.TypeVar('_computeEmissivity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeEmissivity(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Compute Earth emisivity. Emissivity is used to compute the infrared flux that is emitted by Earth. Its value is in
            [0;1].
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the date
                phi (double): the equatorial latitude in rad
        
            Returns:
                the emissivity in [0;1]
        
        """
        ...
    @typing.overload
    def computeEmissivity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_computeEmissivity_1__T], t: _computeEmissivity_1__T) -> _computeEmissivity_1__T:
        """
            Compute Earth emisivity. Emissivity is used to compute the infrared flux that is emitted by Earth. Its value is in
            [0;1].
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date
                phi (T): the equatorial latitude in rad
        
            Returns:
                the emissivity in [0;1]
        
        
        """
        ...
    _computeSolarFlux_1__T = typing.TypeVar('_computeSolarFlux_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeSolarFlux(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
            Compute total solar flux impacting Earth.
        
            Parameters:
                sunPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): the Sun position in an Earth centered frame
        
            Returns:
                the total solar flux impacting Earth in J/m^3
        
        """
        ...
    @typing.overload
    def computeSolarFlux(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeSolarFlux_1__T]) -> _computeSolarFlux_1__T:
        """
            Compute total solar flux impacting Earth.
        
            Parameters:
                sunPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> sunPosition): the Sun position in an Earth centered frame
        
            Returns:
                the total solar flux impacting Earth in J/m^3
        
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force model depends on position only at a given, fixed date.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.dependsOnPositionOnly` in interface :class:`~org.orekit.forces.ForceModel`
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class LightFluxModel:
    """
    public interface LightFluxModel
    
        Interface describing flux models from a light source, including shadowing effects from occulting bodies. Defines the
        flux vector itself as well as detectors for entry and exit of the different eclipse zones, if any.
    
        Since:
            12.1
    """
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]: ...
    _getLightFluxVector_0__T = typing.TypeVar('_getLightFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightFluxVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightFluxVector_0__T]:
        """
            Get the light flux vector in the state's frame. Field version.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): state
        
            Returns:
                light flux
        
        
        """
        ...
    @typing.overload
    def getLightFluxVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the light flux vector in the state's frame.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state
        
            Returns:
                light flux
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Perform initialization steps before starting propagation.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> initialState): initial state
                targetDate (:class:`~org.orekit.time.FieldAbsoluteDate`<T> targetDate): target date for propagation
        
            Since:
                12.2
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Perform initialization steps before starting propagation.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                targetDate (:class:`~org.orekit.time.AbsoluteDate`): target date for propagation
        
            Since:
                12.2
        
        """
        ...

class RadiationForceModel(org.orekit.forces.ForceModel):
    """
    public interface RadiationForceModel extends :class:`~org.orekit.forces.ForceModel`
    
        Interface for radiation-related force models.
    
        Since:
            12.1
    """
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force model depends on position only at a given, fixed date.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.dependsOnPositionOnly` in interface :class:`~org.orekit.forces.ForceModel`
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...

class RadiationSensitive:
    """
    public interface RadiationSensitive
    
        Interface for spacecraft that are sensitive to radiation pressure forces.
    
        Also see:
            :class:`~org.orekit.forces.radiation.SolarRadiationPressure`
    """
    GLOBAL_RADIATION_FACTOR: typing.ClassVar[str] = ...
    """
    static final :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` GLOBAL_RADIATION_FACTOR
    
        Parameter name for global multiplicative factor.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    ABSORPTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    static final :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ABSORPTION_COEFFICIENT
    
        Parameter name for absorption coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    REFLECTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    static final :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` REFLECTION_COEFFICIENT
    
        Parameter name for reflection coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
            Since:
                12.0
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
            Since:
                12.0
        
        """
        ...

class AbstractLightFluxModel(LightFluxModel):
    """
    public abstract class AbstractLightFluxModel extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.LightFluxModel`
    
        Abstract class for light flux models. Via the definition of the lighting ratio and the unocculted flux vector, derives
        the final value.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.forces.radiation.LightFluxModel`
    """
    _getLightFluxVector_0__T = typing.TypeVar('_getLightFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightFluxVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightFluxVector_0__T]:
        """
            Get the light flux vector in the state's frame. Field version.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.LightFluxModel.getLightFluxVector` in
                interface :class:`~org.orekit.forces.radiation.LightFluxModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): state
        
            Returns:
                light flux
        
        
        """
        ...
    @typing.overload
    def getLightFluxVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the light flux vector in the state's frame.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.LightFluxModel.getLightFluxVector` in
                interface :class:`~org.orekit.forces.radiation.LightFluxModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state
        
            Returns:
                light flux
        
        """
        ...
    _getLightingRatio_1__T = typing.TypeVar('_getLightingRatio_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightingRatio(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the lighting ratio ([0-1]).
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state
        
            Returns:
                lighting ratio
        
            Get the lighting ratio ([0-1]).
        
            Parameters:
                position (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): object's position
                occultedBodyPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): occulted body position in same frame
        
            Returns:
                lighting ratio
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightingRatio_1__T]) -> _getLightingRatio_1__T:
        """
            Get the lighting ratio ([0-1]).
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): state
        
            Returns:
                lighting ratio
        
        protected abstract <T extends :class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T getLightingRatio (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> position, :class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> occultedBodyPosition)
        
            Get the lighting ratio ([0-1]). Field version.
        
            Parameters:
                position (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> position): object's position
                occultedBodyPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> occultedBodyPosition): occulted body position in same frame
        
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
    public abstract class AbstractRadiationForceModel extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationForceModel`
    
        Base class for radiation force models.
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.forces.radiation.SolarRadiationPressure`, :class:`~org.orekit.forces.radiation.ECOM2`
    """
    @typing.overload
    def addOccultingBody(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid) -> None:
        """
            Add a new occulting body.
        
            Central body is already considered, it shall not be added this way.
        
            Parameters:
                provider (:class:`~org.orekit.utils.ExtendedPVCoordinatesProvider`): body PV provider
                radius (double): body mean radius
        
            Also see:
                :meth:`~org.orekit.forces.radiation.AbstractRadiationForceModel.addOccultingBody`
        
            Add a new occulting body.
        
            Central body is already considered, it shall not be added this way.
        
            Parameters:
                occulting (:class:`~org.orekit.bodies.OneAxisEllipsoid`): occulting body to add
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.forces.radiation.AbstractRadiationForceModel.addOccultingBody`
        
        
        """
        ...
    @typing.overload
    def addOccultingBody(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double: float) -> None: ...
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
    def getOccultingBodies(self) -> java.util.List[org.orekit.utils.OccultationEngine]: ...

class IsotropicRadiationCNES95Convention(RadiationSensitive):
    """
    public class IsotropicRadiationCNES95Convention extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    
        This class represents the features of a simplified spacecraft.
    
        This model uses the coefficients described in the collective book edited by CNES in 1995: Spaceflight Dynamics (part I),
        in section 5.2.2.1.3.1 (page 296 of the English edition). The absorption coefficient is called α and the specular
        reflection coefficient is called τ. A comment in section 5.2.2.1.3.2 of the same book reads:
    
        .. code-block: java
        
         Some authors prefer to express thermo-optical properties for surfaces
         using the following coefficients: Ka = α, Ks = (1-α)τ, Kd = (1-α)(1-τ)
         
    
        Ka is the same absorption coefficient, and Ks is also called specular reflection coefficient, which leads to a
        confusion. In fact, as the Ka, Ks and Kd coefficients are the most frequently used ones (using the names Ca, Cs and Cd),
        when speaking about reflection coefficients, it is more often Cd that is considered rather than τ.
    
        The classical set of coefficients Ca, Cs, and Cd are implemented in the sister class
        :class:`~org.orekit.forces.radiation.IsotropicRadiationClassicalConvention`, which should probably be preferred to this
        legacy class.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.forces.BoxAndSolarArraySpacecraft`, :class:`~org.orekit.forces.drag.IsotropicDrag`,
            :class:`~org.orekit.forces.radiation.IsotropicRadiationClassicalConvention`
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class IsotropicRadiationClassicalConvention(RadiationSensitive):
    """
    public class IsotropicRadiationClassicalConvention extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    
        This class represents the features of a simplified spacecraft.
    
        This model uses the classical thermo-optical coefficients Ca for absorption, Cs for specular reflection and Cd for
        diffuse reflection. The equation Ca + Cs + Cd = 1 always holds.
    
        A less standard set of coefficients α = Ca for absorption and τ = Cs/(1-Ca) for specular reflection is implemented in
        the sister class :class:`~org.orekit.forces.radiation.IsotropicRadiationCNES95Convention`.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.forces.BoxAndSolarArraySpacecraft`, :class:`~org.orekit.forces.drag.IsotropicDrag`,
            :class:`~org.orekit.forces.radiation.IsotropicRadiationCNES95Convention`
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class IsotropicRadiationSingleCoefficient(RadiationSensitive):
    """
    public class IsotropicRadiationSingleCoefficient extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    
        This class represents the features of a simplified spacecraft.
    
        This model uses a single coefficient cr, considered to be a
        :meth:`~org.orekit.forces.radiation.RadiationSensitive.REFLECTION_COEFFICIENT`.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.forces.BoxAndSolarArraySpacecraft`, :class:`~org.orekit.forces.drag.IsotropicDrag`,
            :class:`~org.orekit.forces.radiation.IsotropicRadiationCNES95Convention`
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class PythonLightFluxModel(LightFluxModel):
    """
    public class PythonLightFluxModel extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.LightFluxModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]: ...
    _getLightFluxVector_0__T = typing.TypeVar('_getLightFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightFluxVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightFluxVector_0__T]:
        """
            Get the light flux vector in the state's frame. Field version.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.LightFluxModel.getLightFluxVector` in
                interface :class:`~org.orekit.forces.radiation.LightFluxModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): state
        
            Returns:
                light flux
        
        
        """
        ...
    @typing.overload
    def getLightFluxVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the light flux vector in the state's frame.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.LightFluxModel.getLightFluxVector` in
                interface :class:`~org.orekit.forces.radiation.LightFluxModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state
        
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
    """
    public class PythonRadiationForceModel extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationForceModel`
    """
    def __init__(self): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
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
    """
    public class PythonRadiationSensitive extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                flux (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class RadiationPressureModel(RadiationForceModel):
    """
    public class RadiationPressureModel extends :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationForceModel`
    
        Class representing a light-induced radiation pressure force, by leveraging on a given flux model.
    
        This class should not be used in addition to :class:`~org.orekit.forces.radiation.SolarRadiationPressure`, which is
        another way of representing the same orbital perturbation.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.forces.radiation.LightFluxModel`, :class:`~org.orekit.forces.radiation.RadiationSensitive`
    """
    def __init__(self, lightFluxModel: LightFluxModel, radiationSensitive: RadiationSensitive): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force model depends on position only at a given, fixed date.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.dependsOnPositionOnly` in interface :class:`~org.orekit.forces.ForceModel`
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationForceModel.dependsOnPositionOnly` in
                interface :class:`~org.orekit.forces.radiation.RadiationForceModel`
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getRadiationSensitive(self) -> RadiationSensitive:
        """
            Getter for radiation sensitive object.
        
            Returns:
                radiation sensitive object
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`,
            :meth:`~org.orekit.forces.ForceModel.acceleration` or :meth:`~org.orekit.forces.ForceModel.acceleration`
        
            The default implementation of this method does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.init` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> initialState): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.FieldAbsoluteDate`<T> target): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`,
            :meth:`~org.orekit.forces.ForceModel.acceleration` or :meth:`~org.orekit.forces.ForceModel.acceleration`
        
            The default implementation of this method does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.init` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...

class AbstractSolarLightFluxModel(AbstractLightFluxModel):
    """
    public abstract class AbstractSolarLightFluxModel extends :class:`~org.orekit.forces.radiation.AbstractLightFluxModel`
    
        Abstract class for the definition of the solar flux model with a single occulting body of spherical shape.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.forces.radiation.LightFluxModel`
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
    public class ECOM2 extends :class:`~org.orekit.forces.radiation.AbstractRadiationForceModel`
    
        The Empirical CODE Orbit Model 2 (ECOM2) of the Center for Orbit Determination in Europe (CODE).
    
        The drag acceleration is computed as follows : γ = γ :sub:`0` + D(u)e :sub:`D` + Y(u)e :sub:`Y` + B(u)e :sub:`B`
    
        In the above equation, γ :sub:`0` is a selectable a priori model. Since 2013, no a priori model is used for CODE IGS
        contribution (i.e. γ :sub:`0` = 0). Moreover, u denotes the satellite's argument of latitude.
    
        D(u), Y(u) and B(u) are three functions of the ECOM2 model that can be represented as Fourier series. The coefficients
        of the Fourier series are estimated during the estimation process. he ECOM2 model has user-defines upper limits *nD* and
        *nB* for the Fourier series (i.e. *nD* for D(u) and *nB* for B(u). Y(u) is defined as a constant value).
    
        It exists several configurations to initialize *nD* and *nB* values. However, Arnold et al recommend to use **D2B1**
        (i.e. *nD* = 1 and *nB* = 1) and **D4B1** (i.e. *nD* = 2 an *nB* = 1) configurations. At the opposite, in Arnold paper,
        it is recommend to not use **D2B0** (i.e. *nD* = 1 and *nB* = 0) configuration.
    
        Since Orekit 11.0, it is possible to take into account the eclipses generated by Moon in the solar radiation pressure
        force model using the :meth:`~org.orekit.forces.radiation.AbstractRadiationForceModel.addOccultingBody` method.
    
    
        :code:`ECOM2 srp =` :code:`new ECOM2(1, 1, 0.0, CelestialBodyFactory.getSun(),
        Constants.EIGEN5C_EARTH_EQUATORIAL_RADIUS);`
    
    
        :code:`srp.addOccultingBody(CelestialBodyFactory.getMoon(), Constants.MOON_EQUATORIAL_RADIUS);`
    
    
    
        Since:
            10.2
    
        Also see:
            "Arnold, Daniel, et al, CODE’s new solar radiation pressure model for GNSS orbit determination, Journal of geodesy
            89.8 (2015): 775-791.", "Tzu-Pang tseng and Michael Moore, Impact of solar radiation pressure mis-modeling on GNSS
            satellite orbit determination, IGS Worshop, Wuhan, China, 2018."
    """
    ECOM_COEFFICIENT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.forces.radiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ECOM_COEFFICIENT
    
        Parameter name for ECOM model coefficients enabling Jacobian processing.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, int: int, int2: int, double: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double2: float): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class PythonAbstractLightFluxModel(AbstractLightFluxModel):
    """
    public class PythonAbstractLightFluxModel extends :class:`~org.orekit.forces.radiation.AbstractLightFluxModel`
    """
    def __init__(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider): ...
    def finalize(self) -> None: ...
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]: ...
    _getLightingRatio_2__T = typing.TypeVar('_getLightingRatio_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getLightingRatio_3__T = typing.TypeVar('_getLightingRatio_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightingRatio(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Description copied from class: :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getLightingRatio`
            Get the lighting ratio ([0-1]).
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getLightingRatio` in
                class :class:`~org.orekit.forces.radiation.AbstractLightFluxModel`
        
            Parameters:
                position (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): object's position
                occultedBodyPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): occulted body position in same frame
        
            Returns:
                lighting ratio
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float: ...
    @typing.overload
    def getLightingRatio(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightingRatio_2__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightingRatio_2__T]) -> _getLightingRatio_2__T:
        """
            Description copied from class: :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getLightingRatio`
            Get the lighting ratio ([0-1]). Field version.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getLightingRatio` in
                class :class:`~org.orekit.forces.radiation.AbstractLightFluxModel`
        
            Parameters:
                position (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> position): object's position
                occultedBodyPosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> occultedBodyPosition): occulted body position in same frame
        
            Returns:
                lighting ratio
        
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightingRatio_3__T]) -> _getLightingRatio_3__T: ...
    _getUnoccultedFluxVector_0__T = typing.TypeVar('_getUnoccultedFluxVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getUnoccultedFluxVector(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getUnoccultedFluxVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getUnoccultedFluxVector_0__T]:
        """
            Description copied from class: :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getUnoccultedFluxVector`
            Get the light flux vector, not considering any shadowing effect. Field version.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getUnoccultedFluxVector` in
                class :class:`~org.orekit.forces.radiation.AbstractLightFluxModel`
        
            Parameters:
                relativePosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> relativePosition): relative position w.r.t. light source
        
            Returns:
                unocculted flux
        
        
        """
        ...
    @typing.overload
    def getUnoccultedFluxVector(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Description copied from class: :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getUnoccultedFluxVector`
            Get the light flux vector, not considering any shadowing effect.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.AbstractLightFluxModel.getUnoccultedFluxVector` in
                class :class:`~org.orekit.forces.radiation.AbstractLightFluxModel`
        
            Parameters:
                relativePosition (:class:`~org.orekit.forces.radiation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): relative position w.r.t. light source
        
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

class PythonAbstractRadiationForceModel(AbstractRadiationForceModel):
    """
    public class PythonAbstractRadiationForceModel extends :class:`~org.orekit.forces.radiation.AbstractRadiationForceModel`
    """
    def __init__(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`,
            :meth:`~org.orekit.forces.ForceModel.acceleration` or :meth:`~org.orekit.forces.ForceModel.acceleration`
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...

class SolarRadiationPressure(AbstractRadiationForceModel):
    """
    public class SolarRadiationPressure extends :class:`~org.orekit.forces.radiation.AbstractRadiationForceModel`
    
        Solar radiation pressure force model.
    
        Since Orekit 11.0, it is possible to take into account the eclipses generated by Moon in the solar radiation pressure
        force model using the :meth:`~org.orekit.forces.radiation.AbstractRadiationForceModel.addOccultingBody` method.
    
        Example:
    
    
        :code:`SolarRadiationPressure srp =` :code:`new SolarRadiationPressure(CelestialBodyFactory.getSun(),
        Constants.EIGEN5C_EARTH_EQUATORIAL_RADIUS,` :code:`new IsotropicRadiationClassicalConvention(50.0, 0.5, 0.5));`
    
    
        :code:`srp.addOccultingBody(CelestialBodyFactory.getMoon(), Constants.MOON_EQUATORIAL_RADIUS);`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, radiationSensitive: RadiationSensitive): ...
    @typing.overload
    def __init__(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, radiationSensitive: RadiationSensitive): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force model depends on position only at a given, fixed date.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    _getLightingRatio_1__T = typing.TypeVar('_getLightingRatio_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightingRatio(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the lighting ratio ([0-1]).
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                lighting ratio
        
            Since:
                7.1
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getLightingRatio_1__T]) -> _getLightingRatio_1__T:
        """
            Get the lighting ratio ([0-1]).
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
        
            Returns:
                lighting ratio
        
            Since:
                7.1
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
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
    public class ConicallyShadowedLightFluxModel extends :class:`~org.orekit.forces.radiation.AbstractSolarLightFluxModel`
    
        Class defining a flux model from a single occulted body, casting a shadow on a spherical occulting body. It cannot model
        oblate bodies or multiple occulting objects (for this, see
        :class:`~org.orekit.forces.radiation.SolarRadiationPressure`).
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.forces.radiation.AbstractSolarLightFluxModel`, :class:`~org.orekit.forces.radiation.LightFluxModel`,
            "Montenbruck, Oliver, and Gill, Eberhard. Satellite orbits : models, methods, and * applications. Berlin New York:
            Springer, 2000."
    """
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, double3: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def __init__(self, double: float, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, double2: float): ...
    @staticmethod
    def getDefaultEclipseDetectionSettings() -> org.orekit.propagation.events.EventDetectionSettings:
        """
            Define default detection settings for eclipses.
        
            Returns:
                default settings
        
        
        """
        ...
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Perform initialization steps before starting propagation.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> initialState): initial state
                targetDate (:class:`~org.orekit.time.FieldAbsoluteDate`<T> targetDate): target date for propagation
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Perform initialization steps before starting propagation.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                targetDate (:class:`~org.orekit.time.AbsoluteDate`): target date for propagation
        
        """
        ...

class CylindricallyShadowedLightFluxModel(AbstractSolarLightFluxModel):
    """
    public class CylindricallyShadowedLightFluxModel extends :class:`~org.orekit.forces.radiation.AbstractSolarLightFluxModel`
    
        Class defining a flux model with a single occulting body, casting a shadow whose shape is a circular cylinder
        (equivalent to the light source being infinitely distant). It is less accurate but faster to evaluate than a conical
        model.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.forces.radiation.AbstractSolarLightFluxModel`, :class:`~org.orekit.forces.radiation.LightFluxModel`
    """
    @typing.overload
    def __init__(self, double: float, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, double2: float): ...
    @typing.overload
    def __init__(self, double: float, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, double2: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, double: float): ...
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
    def getEclipseConditionsDetector(self) -> java.util.List[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEclipseConditionsDetector__T = typing.TypeVar('_getFieldEclipseConditionsDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEclipseConditionsDetector(self, field: org.hipparchus.Field[_getFieldEclipseConditionsDetector__T]) -> java.util.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEclipseConditionsDetector__T]]: ...


class __module_protocol__(typing.Protocol):
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
    PythonAbstractRadiationForceModel: typing.Type[PythonAbstractRadiationForceModel]
    PythonLightFluxModel: typing.Type[PythonLightFluxModel]
    PythonRadiationForceModel: typing.Type[PythonRadiationForceModel]
    PythonRadiationSensitive: typing.Type[PythonRadiationSensitive]
    RadiationForceModel: typing.Type[RadiationForceModel]
    RadiationPressureModel: typing.Type[RadiationPressureModel]
    RadiationSensitive: typing.Type[RadiationSensitive]
    SolarRadiationPressure: typing.Type[SolarRadiationPressure]
    class-use: org.orekit.forces.radiation.class-use.__module_protocol__
