import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.forces
import org.orekit.frames
import org.orekit.models.earth.atmosphere
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class AbstractDragForceModel(org.orekit.forces.AbstractForceModel):
    """
    public abstract class AbstractDragForceModel extends :class:`~org.orekit.forces.AbstractForceModel`
    
        Base class for drag force models.
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.forces.drag.DragForce`, :class:`~org.orekit.forces.drag.TimeSpanDragForce`
    """
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...

class DragSensitive:
    """
    public interface DragSensitive
    
        Interface for spacecraft that are sensitive to atmospheric drag forces.
    
        Also see:
            :class:`~org.orekit.forces.drag.DragForce`
    """
    DRAG_COEFFICIENT: typing.ClassVar[str] = ...
    """
    static final String DRAG_COEFFICIENT
    
        Parameter name for drag coefficient enabling Jacobian processing.
    
        Also see:
            :meth:`~constant`
    
    
    """
    LIFT_RATIO: typing.ClassVar[str] = ...
    """
    static final String LIFT_RATIO
    
        Parameter name for lift ration enabling Jacobian processing.
    
        The lift ratio is the proportion of atmosphere modecules that will experience specular reflection when hitting
        spacecraft instead of experiencing diffuse reflection. The ratio is between 0 and 1, 0 meaning there are no specular
        reflection, only diffuse reflection, and hence no lift effect.
    
        Since:
            9.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_dragAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_dragAcceleration_0__T], t: _dragAcceleration_0__T, t2: _dragAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], tArray: typing.List[_dragAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                density (T): atmospheric density at spacecraft position
                relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, double2: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                density (double): atmospheric density at spacecraft position
                relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class DragForce(AbstractDragForceModel):
    """
    public class DragForce extends :class:`~org.orekit.forces.drag.AbstractDragForceModel`
    
        Atmospheric drag force model. The drag acceleration is computed as follows : ÃŽÂ³ = (1/2 * Ã�ï¿½ * VÃ‚Â² * S / Mass) *
        DragCoefVector With DragCoefVector = {C :sub:`x` , C :sub:`y` , C :sub:`z` } and S given by the user through the
        interface :class:`~org.orekit.forces.drag.DragSensitive`
    """
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, dragSensitive: DragSensitive): ...
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
    def getAtmosphere(self) -> org.orekit.models.earth.atmosphere.Atmosphere:
        """
            Get the atmospheric model.
        
            Returns:
                atmosphere model
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getSpacecraft(self) -> DragSensitive:
        """
            Get spacecraft that are sensitive to atmospheric drag forces.
        
            Returns:
                drag sensitive spacecraft model
        
        
        """
        ...

class IsotropicDrag(DragSensitive):
    """
    public class IsotropicDrag extends Object implements :class:`~org.orekit.forces.drag.DragSensitive`
    
        This class models isotropic drag effects.
    
        The model of this spacecraft is a simple spherical model, this means that all coefficients are constant and do not
        depend of the direction.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.forces.BoxAndSolarArraySpacecraft`,
            :class:`~org.orekit.forces.radiation.IsotropicRadiationCNES95Convention`
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_dragAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_dragAcceleration_0__T], t: _dragAcceleration_0__T, t2: _dragAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], tArray: typing.List[_dragAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                density (T): atmospheric density at spacecraft position
                relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, double2: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                density (double): atmospheric density at spacecraft position
                relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...

class PythonAbstractDragForceModel(AbstractDragForceModel):
    """
    public class PythonAbstractDragForceModel extends :class:`~org.orekit.forces.drag.AbstractDragForceModel`
    """
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere): ...
    _acceleration_1__T = typing.TypeVar('_acceleration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
            Compute acceleration.
        
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
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
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

class PythonDragSensitive(DragSensitive):
    """
    public class PythonDragSensitive extends Object implements :class:`~org.orekit.forces.drag.DragSensitive`
    """
    def __init__(self): ...
    _dragAcceleration_1__T = typing.TypeVar('_dragAcceleration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, double2: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to drag. Extension point for Python.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                density (double): atmospheric density at spacecraft position
                relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
            Compute the acceleration due to drag. Connects to dragAcceleration_FFFFTTFT for Python extension.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                density (T): atmospheric density at spacecraft position
                relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_dragAcceleration_1__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_1__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_dragAcceleration_1__T], t: _dragAcceleration_1__T, t2: _dragAcceleration_1__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_1__T], tArray: typing.List[_dragAcceleration_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_1__T]: ...
    _dragAcceleration_FFFFTTFT__T = typing.TypeVar('_dragAcceleration_FFFFTTFT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def dragAcceleration_FFFFTTFT(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_dragAcceleration_FFFFTTFT__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_FFFFTTFT__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_dragAcceleration_FFFFTTFT__T], t: _dragAcceleration_FFFFTTFT__T, t2: _dragAcceleration_FFFFTTFT__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_FFFFTTFT__T], tArray: typing.List[_dragAcceleration_FFFFTTFT__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_FFFFTTFT__T]: ...
    def finalize(self) -> None: ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
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

class TimeSpanDragForce(AbstractDragForceModel):
    DATE_BEFORE: typing.ClassVar[str] = ...
    DATE_AFTER: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, dragSensitive: DragSensitive): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, dragSensitive: DragSensitive, timeScale: org.orekit.time.TimeScale): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def addDragSensitiveValidAfter(self, dragSensitive: DragSensitive, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def addDragSensitiveValidBefore(self, dragSensitive: DragSensitive, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def extractDragSensitiveRange(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap[DragSensitive]: ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def extractParameters(self, tArray: typing.List[_extractParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.List[_extractParameters_1__T]: ...
    def getDragSensitive(self, absoluteDate: org.orekit.time.AbsoluteDate) -> DragSensitive: ...
    def getDragSensitiveSpan(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap.Span[DragSensitive]: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span[DragSensitive]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTransitions(self) -> java.util.NavigableSet[org.orekit.utils.TimeSpanMap.Transition[DragSensitive]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.drag")``.

    AbstractDragForceModel: typing.Type[AbstractDragForceModel]
    DragForce: typing.Type[DragForce]
    DragSensitive: typing.Type[DragSensitive]
    IsotropicDrag: typing.Type[IsotropicDrag]
    PythonAbstractDragForceModel: typing.Type[PythonAbstractDragForceModel]
    PythonDragSensitive: typing.Type[PythonDragSensitive]
    TimeSpanDragForce: typing.Type[TimeSpanDragForce]
