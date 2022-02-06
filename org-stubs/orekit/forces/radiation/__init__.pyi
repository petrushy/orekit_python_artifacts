import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.forces
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class AbstractRadiationForceModel(org.orekit.forces.AbstractForceModel):
    """
    public abstract class AbstractRadiationForceModel extends :class:`~org.orekit.forces.AbstractForceModel`
    
        Base class for radiation force models.
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.forces.radiation.SolarRadiationPressure`, :class:`~org.orekit.forces.radiation.ECOM2`
    """
    def addOccultingBody(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double: float) -> None:
        """
            Add a new occulting body. Central body is already considered, it shall not be added this way.
        
            Parameters:
                provider (:class:`~org.orekit.utils.ExtendedPVCoordinatesProvider`): body PV provider
                radius (double): body mean radius
        
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getEquatorialRadius(self) -> float:
        """
            Getter for equatorial radius.
        
            Returns:
                central body equatorial radius
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getOtherOccultingBodies(self) -> java.util.Map[org.orekit.utils.ExtendedPVCoordinatesProvider, float]: ...

class KnockeRediffusedForceModel(org.orekit.forces.AbstractForceModel):
    """
    public class KnockeRediffusedForceModel extends :class:`~org.orekit.forces.AbstractForceModel`
    
        The Knocke Earth Albedo and IR emission force model.
    
        This model is based on "EARTH RADIATION PRESSURE EFFECTS ON SATELLITES", 1988, by P. C. Knocke, J. C. Ries, and B. D.
        Tapley.
    
        This model represents the effects of radiation pressure coming from the Earth. It considers Solar radiation which has
        been reflected by Earth (albedo) and Earth infrared emissions. The planet is considered as a sphere and is divided into
        elementary areas. Each elementary area is considered as a plane and emits radiation according to Lambert's law. The flux
        the satellite receives is then equal to the sum of the elementary fluxes coming from Earth.
    
        The radiative model of the satellite, and its ability to diffuse, reflect or absorb radiation is handled by a
        :class:`~org.orekit.forces.radiation.RadiationSensitive`.
    
        **Caution:** The spacecraft state must be defined in an Earth centered frame.
    
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
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
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
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class RadiationSensitive:
    """
    public interface RadiationSensitive
    
        Interface for spacecraft that are sensitive to radiation pressure forces.
    
        Also see:
            :class:`~org.orekit.forces.radiation.SolarRadiationPressure`
    """
    ABSORPTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    static final String ABSORPTION_COEFFICIENT
    
        Parameter name for absorption coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    REFLECTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    static final String REFLECTION_COEFFICIENT
    
        Parameter name for reflection coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_radiationPressureAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_radiationPressureAcceleration_0__T], t: _radiationPressureAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...

class ECOM2(AbstractRadiationForceModel):
    """
    public class ECOM2 extends :class:`~org.orekit.forces.radiation.AbstractRadiationForceModel`
    
        The Empirical CODE Orbit Model 2 (ECOM2) of the Center for Orbit Determination in Europe (CODE).
    
        The drag acceleration is computed as follows : Î³ = Î³ :sub:`0` + D(u)e :sub:`D` + Y(u)e :sub:`Y` + B(u)e :sub:`B`
    
        In the above equation, ÃŽÂ³ :sub:`0` is a selectable a priori model. Since 2013, no a priori model is used for CODE IGS
        contribution (i.e. ÃŽÂ³ :sub:`0` = 0). Moreover, u denotes the satellite's argument of latitude.
    
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
            "Arnold, Daniel, et al, CODEÃ¢â‚¬â„¢s new solar radiation pressure model for GNSS orbit determination, Journal of
            geodesy 89.8 (2015): 775-791.", "Tzu-Pang tseng and Michael Moore, Impact of solar radiation pressure mis-modeling on
            GNSS satellite orbit determination, IGS Worshop, Wuhan, China, 2018."
    """
    ECOM_COEFFICIENT: typing.ClassVar[str] = ...
    """
    public static final String ECOM_COEFFICIENT
    
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
                parameters (T[]): values of the force model parameters
        
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
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class IsotropicRadiationCNES95Convention(RadiationSensitive):
    """
    public class IsotropicRadiationCNES95Convention extends Object implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    
        This class represents the features of a simplified spacecraft.
    
        This model uses the coefficients described in the collective book edited by CNES in 1995: Spaceflight Dynamics (part I),
        in section 5.2.2.1.3.1 (page 296 of the English edition). The absorption coefficient is called ÃŽÂ± and the specular
        reflection coefficient is called Ã�â€ž. A comment in section 5.2.2.1.3.2 of the same book reads:
    
        .. code-block: java
        
        
         Some authors prefer to express thermo-optical properties for surfaces
         using the following coefficients: Ka = Î±, Ks = (1-Î±)Ï„, Kd = (1-Î±)(1-Ï„)
         
    
        Ka is the same absorption coefficient, and Ks is also called specular reflection coefficient, which leads to a
        confusion. In fact, as the Ka, Ks and Kd coefficients are the most frequently used ones (using the names Ca, Cs and Cd),
        when speaking about reflection coefficients, it is more often Cd that is considered rather than Ã�â€ž.
    
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
    def radiationPressureAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_radiationPressureAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_radiationPressureAcceleration_0__T], t: _radiationPressureAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...

class IsotropicRadiationClassicalConvention(RadiationSensitive):
    """
    public class IsotropicRadiationClassicalConvention extends Object implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    
        This class represents the features of a simplified spacecraft.
    
        This model uses the classical thermo-optical coefficients Ca for absorption, Cs for specular reflection and Kd for
        diffuse reflection. The equation Ca + Cs + Cd = 1 always holds.
    
        A less standard set of coefficients ÃŽÂ± = Ca for absorption and Ã�â€ž = Cs/(1-Ca) for specular reflection is
        implemented in the sister class :class:`~org.orekit.forces.radiation.IsotropicRadiationCNES95Convention`.
    
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
    def radiationPressureAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_radiationPressureAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_radiationPressureAcceleration_0__T], t: _radiationPressureAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...

class IsotropicRadiationSingleCoefficient(RadiationSensitive):
    """
    public class IsotropicRadiationSingleCoefficient extends Object implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    
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
    def radiationPressureAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_radiationPressureAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_radiationPressureAcceleration_0__T], t: _radiationPressureAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...

class PythonAbstractRadiationForceModel(AbstractRadiationForceModel):
    """
    public class PythonAbstractRadiationForceModel extends :class:`~org.orekit.forces.radiation.AbstractRadiationForceModel`
    """
    _acceleration_1__T = typing.TypeVar('_acceleration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration. Extension point for Python.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
            Compute acceleration. Automatically directs to the Python extension point acceleration_FT
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_1__T], tArray: typing.List[_acceleration_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_1__T]: ...
    _acceleration_FT__T = typing.TypeVar('_acceleration_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def acceleration_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_FT__T], tArray: typing.List[_acceleration_FT__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_FT__T]:
        """
            Compute acceleration, Alternative python interface point for the acceleration method. Extension point for Python.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
        
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
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`, null or
            null
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...

class PythonRadiationSensitive(RadiationSensitive):
    """
    public class PythonRadiationSensitive extends Object implements :class:`~org.orekit.forces.radiation.RadiationSensitive`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
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
    _radiationPressureAcceleration_1__T = typing.TypeVar('_radiationPressureAcceleration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_radiationPressureAcceleration_1__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_1__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_radiationPressureAcceleration_1__T], t: _radiationPressureAcceleration_1__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_1__T], tArray: typing.List[_radiationPressureAcceleration_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_1__T]: ...
    _radiationPressureAcceleration_FFFFTFT__T = typing.TypeVar('_radiationPressureAcceleration_FFFFTFT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def radiationPressureAcceleration_FFFFTFT(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_radiationPressureAcceleration_FFFFTFT__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_FFFFTFT__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_radiationPressureAcceleration_FFFFTFT__T], t: _radiationPressureAcceleration_FFFFTFT__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_FFFFTFT__T], tArray: typing.List[_radiationPressureAcceleration_FFFFTFT__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_FFFFTFT__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
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
    def __init__(self, double: float, double2: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double3: float, radiationSensitive: RadiationSensitive): ...
    @typing.overload
    def __init__(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double: float, radiationSensitive: RadiationSensitive): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
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
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    _getGeneralEclipseRatio_1__T = typing.TypeVar('_getGeneralEclipseRatio_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getGeneralEclipseRatio(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float) -> float:
        """
            Get eclipse ratio between to bodies seen from a specific object. Ratio is in [0-1].
        
            Parameters:
                position (Vector3D): the satellite's position in the selected frame
                occultingPosition (Vector3D): the position of the occulting object
                occultingRadius (double): the mean radius of the occulting object
                occultedPosition (Vector3D): the position of the occulted object
                occultedRadius (double): the mean radius of the occulted object
        
            Returns:
                eclipse ratio
        
        """
        ...
    @typing.overload
    def getGeneralEclipseRatio(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getGeneralEclipseRatio_1__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getGeneralEclipseRatio_1__T], t: _getGeneralEclipseRatio_1__T, fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getGeneralEclipseRatio_1__T], t2: _getGeneralEclipseRatio_1__T) -> _getGeneralEclipseRatio_1__T:
        """
            Get eclipse ratio between to bodies seen from a specific object. Ratio is in [0-1].
        
            Parameters:
                position (FieldVector3D<T> position): the satellite's position in the selected frame
                occultingPosition (FieldVector3D<T> occultingPosition): the position of the occulting object
                occultingRadius (T): the mean radius of the occulting object
                occultedPosition (FieldVector3D<T> occultedPosition): the position of the occulted object
                occultedRadius (T): the mean radius of the occulted object
        
            Returns:
                eclipse ratio
        
        
        """
        ...
    _getLightingRatio_1__T = typing.TypeVar('_getLightingRatio_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLightingRatio(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the lighting ratio ([0-1]). Considers only central body as occulting body.
        
            Parameters:
                position (Vector3D): the satellite's position in the selected frame.
                frame (:class:`~org.orekit.frames.Frame`): in which is defined the position
                date (:class:`~org.orekit.time.AbsoluteDate`): the date
        
            Returns:
                lighting ratio
        
            Since:
                7.1
        
        """
        ...
    @typing.overload
    def getLightingRatio(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLightingRatio_1__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getLightingRatio_1__T]) -> _getLightingRatio_1__T:
        """
            Get the lighting ratio ([0-1]). Considers only central body as occulting body.
        
            Parameters:
                position (FieldVector3D<T> position): the satellite's position in the selected frame.
                frame (:class:`~org.orekit.frames.Frame`): in which is defined the position
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date
        
            Returns:
                lighting ratio
        
            Since:
                7.1
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getTotalLightingRatio_1__T = typing.TypeVar('_getTotalLightingRatio_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTotalLightingRatio(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the total lighting ratio ([0-1]). This method considers every occulting bodies.
        
            Parameters:
                position (Vector3D): the satellite's position in the selected frame.
                frame (:class:`~org.orekit.frames.Frame`): in which is defined the position
                date (:class:`~org.orekit.time.AbsoluteDate`): the date
        
            Returns:
                lighting ratio
        
        """
        ...
    @typing.overload
    def getTotalLightingRatio(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTotalLightingRatio_1__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTotalLightingRatio_1__T]) -> _getTotalLightingRatio_1__T:
        """
            Get the total lighting ratio ([0-1]). This method considers every occulting bodies.
        
            Parameters:
                position (FieldVector3D<T> position): the satellite's position in the selected frame.
                frame (:class:`~org.orekit.frames.Frame`): in which is defined the position
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date
        
            Returns:
                lighting rati
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.radiation")``.

    AbstractRadiationForceModel: typing.Type[AbstractRadiationForceModel]
    ECOM2: typing.Type[ECOM2]
    IsotropicRadiationCNES95Convention: typing.Type[IsotropicRadiationCNES95Convention]
    IsotropicRadiationClassicalConvention: typing.Type[IsotropicRadiationClassicalConvention]
    IsotropicRadiationSingleCoefficient: typing.Type[IsotropicRadiationSingleCoefficient]
    KnockeRediffusedForceModel: typing.Type[KnockeRediffusedForceModel]
    PythonAbstractRadiationForceModel: typing.Type[PythonAbstractRadiationForceModel]
    PythonRadiationSensitive: typing.Type[PythonRadiationSensitive]
    RadiationSensitive: typing.Type[RadiationSensitive]
    SolarRadiationPressure: typing.Type[SolarRadiationPressure]
