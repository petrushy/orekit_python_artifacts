import java.io
import java.lang
import java.util
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.ode.events
import org.orekit.attitudes.class-use
import org.orekit.bodies
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.events.handlers
import org.orekit.time
import org.orekit.utils
import typing



class Attitude(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['Attitude'], java.io.Serializable):
    """
    public class Attitude extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.attitudes.Attitude`>, :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        This class handles attitude definition at a given date.
    
        This class represents the rotation between a reference frame and the satellite frame, as well as the spin of the
        satellite (axis and rotation rate).
    
        The state can be slightly shifted to close dates. This shift is based on a linear extrapolation for attitude taking the
        spin rate into account. It is *not* intended as a replacement for proper attitude propagation but should be sufficient
        for either small time shifts or coarse accuracy.
    
        The instance :code:`Attitude` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.attitudes.AttitudeProvider`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, angularCoordinates: org.orekit.utils.AngularCoordinates): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of attitude parameters.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date of the attitude parameters
        
        
        """
        ...
    def getOrientation(self) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
            Get the complete orientation including spin.
        
            Returns:
                complete orientation including spin
        
            Also see:
                :meth:`~org.orekit.attitudes.Attitude.getRotation`, :meth:`~org.orekit.attitudes.Attitude.getSpin`
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame.
        
            Returns:
                referenceFrame reference frame from which attitude is defined.
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Get the attitude rotation.
        
            Returns:
                attitude satellite rotation from reference frame.
        
            Also see:
                :meth:`~org.orekit.attitudes.Attitude.getOrientation`, :meth:`~org.orekit.attitudes.Attitude.getSpin`
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the satellite rotation acceleration.
        
            The rotation acceleration. vector is defined in **satellite** frame.
        
            Returns:
                rotation acceleration
        
            Also see:
                :meth:`~org.orekit.attitudes.Attitude.getOrientation`, :meth:`~org.orekit.attitudes.Attitude.getRotation`
        
        
        """
        ...
    def getSpin(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the satellite spin.
        
            The spin vector is defined in **satellite** frame.
        
            Returns:
                spin satellite spin (axis and velocity).
        
            Also see:
                :meth:`~org.orekit.attitudes.Attitude.getOrientation`, :meth:`~org.orekit.attitudes.Attitude.getRotation`
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'Attitude':
        """
            Get a time-shifted attitude.
        
            The state can be slightly shifted to close dates. This shift is based on a linear extrapolation for attitude taking the
            spin rate into account. It is *not* intended as a replacement for proper attitude propagation but should be sufficient
            for either small time shifts or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new attitude, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def withReferenceFrame(self, frame: org.orekit.frames.Frame) -> 'Attitude':
        """
            Get a similar attitude with a specific reference frame.
        
            If the instance reference frame is already the specified one, the instance itself is returned without any object
            creation. Otherwise, a new instance will be created with the specified reference frame. In this case, the required
            intermediate rotation and spin between the specified and the original reference frame will be inserted.
        
            Parameters:
                newReferenceFrame (:class:`~org.orekit.frames.Frame`): desired reference frame for attitude
        
            Returns:
                an attitude that has the same orientation and motion as the instance, but guaranteed to have the specified reference
                frame
        
        
        """
        ...

class AttitudeBuilder:
    """
    public interface AttitudeBuilder
    
        This interface represents a builder for attitude.
    
        It is intended to modify raw angular coordinates when build attitudes, for example if these coordinates are not defined
        from the desired reference frame.
    
        Since:
            11.0
    """
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude:
        """
            Build a filtered attitude.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> 'FieldAttitude'[_build_1__T]:
        """
            Build a filtered attitude.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedFieldAngularCoordinates`<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        
        """
        ...

class AttitudeInterpolator(org.orekit.time.AbstractTimeInterpolator[Attitude]):
    """
    public class AttitudeInterpolator extends :class:`~org.orekit.time.AbstractTimeInterpolator`<:class:`~org.orekit.attitudes.Attitude`>
    
        Class for attitude interpolation.
    
        The type of interpolation used is defined by given time stamped angular coordinates interpolator at construction.
    
        Also see:
            :class:`~org.orekit.utils.TimeStampedAngularCoordinates`, :class:`~org.orekit.time.TimeInterpolator`
    """
    def __init__(self, frame: org.orekit.frames.Frame, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.utils.TimeStampedAngularCoordinates]): ...
    def getAngularInterpolator(self) -> org.orekit.time.TimeInterpolator[org.orekit.utils.TimeStampedAngularCoordinates]: ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
            Get reference frame from which attitude is defined.
        
            Returns:
                reference frame from which attitude is defined
        
        
        """
        ...

class AttitudeProvider:
    """
    public interface AttitudeProvider
    
        This interface represents an attitude provider model set.
    
        An attitude provider provides a way to compute an :class:`~org.orekit.attitudes.Attitude` from an date and
        position-velocity local provider.
    """
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> 'FieldAttitude'[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
            Since:
                9.0
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
            Since:
                12.0
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
            Since:
                12.0
        
        """
        ...

_FieldAttitude__T = typing.TypeVar('_FieldAttitude__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAttitude(org.orekit.time.FieldTimeStamped[_FieldAttitude__T], org.orekit.time.FieldTimeShiftable['FieldAttitude'[_FieldAttitude__T], _FieldAttitude__T], typing.Generic[_FieldAttitude__T]):
    """
    public class FieldAttitude<T extends :class:`~org.orekit.attitudes.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.FieldTimeStamped`<T>, :class:`~org.orekit.time.FieldTimeShiftable`<:class:`~org.orekit.attitudes.FieldAttitude`<T>, T>
    
        This class handles attitude definition at a given date.
    
        This class represents the rotation between a reference frame and the satellite frame, as well as the spin of the
        satellite (axis and rotation rate).
    
        The state can be slightly shifted to close dates. This shift is based on a linear extrapolation for attitude taking the
        spin rate into account. It is *not* intended as a replacement for proper attitude propagation but should be sufficient
        for either small time shifts or coarse accuracy.
    
        The instance :code:`Attitude` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.attitudes.AttitudeProvider`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAttitude__T], attitude: Attitude): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitude__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T], frame: org.orekit.frames.Frame, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAttitude__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T], frame: org.orekit.frames.Frame, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, field2: org.hipparchus.Field[_FieldAttitude__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T], frame: org.orekit.frames.Frame, fieldAngularCoordinates: org.orekit.utils.FieldAngularCoordinates[_FieldAttitude__T]): ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T]: ...
    def getOrientation(self) -> org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitude__T]: ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame.
        
            Returns:
                referenceFrame reference frame from which attitude is defined.
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAttitude__T]: ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]: ...
    def getSpin(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAttitude'[_FieldAttitude__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAttitude__T) -> 'FieldAttitude'[_FieldAttitude__T]: ...
    def toAttitude(self) -> Attitude:
        """
            Converts to an Attitude instance.
        
            Returns:
                Attitude with same properties
        
        
        """
        ...
    def withReferenceFrame(self, frame: org.orekit.frames.Frame) -> 'FieldAttitude'[_FieldAttitude__T]: ...

_FieldAttitudeInterpolator__KK = typing.TypeVar('_FieldAttitudeInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldAttitudeInterpolator(org.orekit.time.AbstractFieldTimeInterpolator[FieldAttitude[_FieldAttitudeInterpolator__KK], _FieldAttitudeInterpolator__KK], typing.Generic[_FieldAttitudeInterpolator__KK]):
    """
    public class FieldAttitudeInterpolator<KK extends :class:`~org.orekit.attitudes.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<KK>> extends :class:`~org.orekit.time.AbstractFieldTimeInterpolator`<:class:`~org.orekit.attitudes.FieldAttitude`<KK>, KK>
    
        Class for attitude interpolation.
    
        The type of interpolation used is defined by given time stamped angular coordinates interpolator at construction.
    
        Also see:
            :class:`~org.orekit.utils.TimeStampedFieldAngularCoordinates`, :class:`~org.orekit.time.FieldTimeInterpolator`
    """
    def __init__(self, frame: org.orekit.frames.Frame, fieldTimeInterpolator: org.orekit.time.FieldTimeInterpolator[org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitudeInterpolator__KK], _FieldAttitudeInterpolator__KK]): ...
    def getAngularInterpolator(self) -> org.orekit.time.FieldTimeInterpolator[org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitudeInterpolator__KK], _FieldAttitudeInterpolator__KK]: ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
            Get reference frame from which attitude is defined.
        
            Returns:
                reference frame from which attitude is defined
        
        
        """
        ...

_FieldInertia__T = typing.TypeVar('_FieldInertia__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldInertia(typing.Generic[_FieldInertia__T]):
    """
    public class FieldInertia<T extends :class:`~org.orekit.attitudes.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for inertia of a 3D object.
    
        Instances of this class are immutable
    
        Since:
            12.0
    """
    def getInertiaAxis1(self) -> 'FieldInertiaAxis'[_FieldInertia__T]: ...
    def getInertiaAxis2(self) -> 'FieldInertiaAxis'[_FieldInertia__T]: ...
    def getInertiaAxis3(self) -> 'FieldInertiaAxis'[_FieldInertia__T]: ...
    def momentum(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertia__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertia__T]: ...
    def swap12(self) -> 'FieldInertia'[_FieldInertia__T]: ...
    def swap13(self) -> 'FieldInertia'[_FieldInertia__T]: ...
    def swap23(self) -> 'FieldInertia'[_FieldInertia__T]: ...

_FieldInertiaAxis__T = typing.TypeVar('_FieldInertiaAxis__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldInertiaAxis(typing.Generic[_FieldInertiaAxis__T]):
    """
    public class FieldInertiaAxis<T extends :class:`~org.orekit.attitudes.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for inertial axis.
    
        Instances of this class are immutable
    
        Since:
            12.0
    """
    def __init__(self, t: _FieldInertiaAxis__T, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertiaAxis__T]): ...
    def getA(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertiaAxis__T]: ...
    def getI(self) -> _FieldInertiaAxis__T:
        """
            Get the moment of inertia.
        
            Returns:
                moment of inertia
        
        
        """
        ...
    def negate(self) -> 'FieldInertiaAxis'[_FieldInertiaAxis__T]: ...

class Inertia:
    """
    public class Inertia extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for inertia of a 3D object.
    
        Instances of this class are immutable
    
        Since:
            12.0
    """
    def __init__(self, inertiaAxis: 'InertiaAxis', inertiaAxis2: 'InertiaAxis', inertiaAxis3: 'InertiaAxis'): ...
    def getInertiaAxis1(self) -> 'InertiaAxis':
        """
            Get inertia along first axis.
        
            Returns:
                inertia along first axis
        
        
        """
        ...
    def getInertiaAxis2(self) -> 'InertiaAxis':
        """
            Get inertia along second axis.
        
            Returns:
                inertia along second axis
        
        
        """
        ...
    def getInertiaAxis3(self) -> 'InertiaAxis':
        """
            Get inertia along third axis.
        
            Returns:
                inertia along third axis
        
        
        """
        ...
    def momentum(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute angular momentum.
        
            Parameters:
                rotationRate (:class:`~org.orekit.attitudes.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): rotation rate in body frame.
        
            Returns:
                angular momentum in body frame
        
        
        """
        ...
    def swap12(self) -> 'Inertia':
        """
            Swap axes 1 and 2.
        
            The instance is unchanged.
        
            Returns:
                inertia with swapped axes
        
        
        """
        ...
    def swap13(self) -> 'Inertia':
        """
            Swap axes 1 and 3.
        
            The instance is unchanged.
        
            Returns:
                inertia with swapped axes
        
        
        """
        ...
    def swap23(self) -> 'Inertia':
        """
            Swap axes 2 and 3.
        
            The instance is unchanged.
        
            Returns:
                inertia with swapped axes
        
        
        """
        ...

class InertiaAxis:
    """
    public class InertiaAxis extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for inertial axis.
    
        Instances of this class are immutable
    
        Since:
            12.0
    """
    def __init__(self, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getA(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the inertia axis.
        
            Returns:
                inertia axis
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the moment of inertia.
        
            Returns:
                moment of inertia
        
        
        """
        ...
    def negate(self) -> 'InertiaAxis':
        """
            Reverse the inertia axis.
        
            Returns:
                new container with reversed axis
        
        
        """
        ...

class TargetProvider:
    """
    public interface TargetProvider
    
        Provider for target vector.
    
        Since:
            12.2
    """
    _getDerivative2TargetDirection_0__T = typing.TypeVar('_getDerivative2TargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_getDerivative2TargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_getDerivative2TargetDirection_0__T]]: ...
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative2]: ...
    _getTargetDirection_0__T = typing.TypeVar('_getTargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTargetDirection_0__T]:
        """
            Get a target vector.
        
            Parameters:
                sun (:class:`~org.orekit.utils.ExtendedPositionProvider`): Sun model
                earth (:class:`~org.orekit.bodies.OneAxisEllipsoid`): Earth model
                pv (:class:`~org.orekit.utils.TimeStampedFieldPVCoordinates`<T> pv): spacecraft position and velocity
                frame (:class:`~org.orekit.frames.Frame`): inertial frame
        
            Returns:
                target direction in the spacecraft state frame
        
        
        """
        ...
    @typing.overload
    def getTargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get a target vector.
        
            Parameters:
                sun (:class:`~org.orekit.utils.ExtendedPositionProvider`): Sun model
                earth (:class:`~org.orekit.bodies.OneAxisEllipsoid`): Earth model
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): spacecraft position and velocity
                frame (:class:`~org.orekit.frames.Frame`): inertial frame
        
            Returns:
                target direction in the spacecraft state frame
        
        """
        ...

class AlignedAndConstrained(AttitudeProvider):
    """
    public class AlignedAndConstrained extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        Attitude provider with one satellite vector aligned and another one constrained to two targets.
    
        Since:
            12.2
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, targetProvider: TargetProvider, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, targetProvider2: TargetProvider, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...

class AttitudeProviderModifier(AttitudeProvider):
    """
    public interface AttitudeProviderModifier extends :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This interface represents an attitude provider that modifies/wraps another underlying provider.
    
        Since:
            5.1
    """
    @staticmethod
    def getFrozenAttitudeProvider(attitudeProvider: AttitudeProvider) -> 'AttitudeProviderModifier':
        """
            Wrap the input provider with a new one always returning attitudes with zero rotation rate and acceleration. It is not
            physically sound, but remains useful for performance when a full, physical attitude with time derivatives is not needed.
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): provider to wrap
        
            Returns:
                wrapping provider
        
            Since:
                12.1
        
        
        """
        ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider:
        """
            Get the underlying attitude provider.
        
            Returns:
                underlying attitude provider
        
        
        """
        ...

class AttitudesSequence(AttitudeProvider):
    """
    public class AttitudesSequence extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This classes manages a sequence of different attitude providers that are activated in turn according to switching
        events.
    
        Only one attitude provider in the sequence is in an active state. When one of the switch event associated with the
        active provider occurs, the active provider becomes the one specified with the event. A simple example is a provider for
        the sun lighted part of the orbit and another provider for the eclipse time. When the sun lighted provider is active,
        the eclipse entry event is checked and when it occurs the eclipse provider is activated. When the eclipse provider is
        active, the eclipse exit event is checked and when it occurs the sun lighted provider is activated again. This sequence
        is a simple loop.
    
        An active attitude provider may have several switch events and next provider settings, leading to different activation
        patterns depending on which events are triggered first. An example of this feature is handling switches to safe mode if
        some contingency condition is met, in addition to the nominal switches that correspond to proper operations. Another
        example is handling of maneuver mode.
    
        Note that this attitude provider is stateful, it keeps in memory the sequence of active underlying providers with their
        switch dates and the transitions from one provider to the other. This implies that this provider should *not* be shared
        among different propagators at the same time, each propagator should use its own instance of this provider.
    
        The sequence kept in memory is reset when :meth:`~org.orekit.attitudes.AttitudesSequence.resetActiveProvider` is called,
        and only the specify provider is kept. The sequence is also partially reset each time a propagation starts. If a new
        propagation is started after a first propagation has been run, all the already computed switches that occur after
        propagation start for forward propagation or before propagation start for backward propagation will be erased. New
        switches will be computed and applied properly according to the new propagation settings. The already computed switches
        that are not in covered are kept in memory. This implies that if a propagation is interrupted and restarted in the same
        direction, then attitude switches will remain in place, ensuring that even if the interruption occurred in the middle of
        an attitude transition the second propagation will properly complete the transition that was started by the first
        propagator.
    
        Since:
            5.1
    """
    def __init__(self): ...
    _addSwitchingCondition__T = typing.TypeVar('_addSwitchingCondition__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addSwitchingCondition(self, attitudeProvider: AttitudeProvider, attitudeProvider2: AttitudeProvider, t: _addSwitchingCondition__T, boolean: bool, boolean2: bool, double: float, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, switchHandler: 'AttitudesSequence.SwitchHandler') -> None:
        """
            Add a switching condition between two attitude providers.
        
            The :code:`past` and :code:`future` attitude providers are defined with regard to the natural flow of time. This means
            that if the propagation is forward, the propagator will switch from :code:`past` provider to :code:`future` provider at
            event occurrence, but if the propagation is backward, the propagator will switch from :code:`future` provider to
            :code:`past` provider at event occurrence. The transition between the two attitude laws is not instantaneous, the switch
            event defines the start of the transition (i.e. when leaving the :code:`past` attitude law and entering the interpolated
            transition law). The end of the transition (i.e. when leaving the interpolating transition law and entering the
            :code:`future` attitude law) occurs at switch time plus :code:`transitionTime`.
        
            An attitude provider may have several different switch events associated to it. Depending on which event is triggered,
            the appropriate provider is switched to.
        
            The switch events specified here must *not* be registered to the propagator directly. The proper way to register these
            events is to call :meth:`~org.orekit.attitudes.AttitudesSequence.registerSwitchEvents` once after all switching
            conditions have been set up. The reason for this is that the events will be wrapped before being registered.
        
            If the underlying detector has an event handler associated to it, this handler will be triggered (i.e. its
            :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` method will be called), *regardless* of the
            event really triggering an attitude switch or not. As an example, if an eclipse detector is used to switch from day to
            night attitude mode when entering eclipse, with :code:`switchOnIncrease` set to :code:`false` and
            :code:`switchOnDecrease` set to :code:`true`. Then a handler set directly at eclipse detector level would be triggered
            at both eclipse entry and eclipse exit, but attitude switch would occur *only* at eclipse entry. Note that for the sake
            of symmetry, the transition start and end dates should match for both forward and backward propagation. This implies
            that for backward propagation, we have to compensate for the :code:`transitionTime` when looking for the event. An
            unfortunate consequence is that the :meth:`~org.orekit.propagation.events.handlers.EventHandler.eventOccurred` method
            may appear to be called out of sync with respect to the propagation (it will be called when propagator reaches
            transition end, despite it refers to transition start, as per :code:`transitionTime` compensation), and if the method
            returns :meth:`~org.orekit.attitudes.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.events.Action.html?is`, it
            will stop at the end of the transition instead of at the start. For these reasons, it is not recommended to set up an
            event handler for events that are used to switch attitude. If an event handler is needed for other purposes, a second
            handler should be registered to the propagator rather than relying on the side effects of attitude switches.
        
            The smoothness of the transition between past and future attitude laws can be tuned using the :code:`transitionTime` and
            :code:`transitionFilter` parameters. The :code:`transitionTime` parameter specifies how much time is spent to switch
            from one law to the other law. It should be larger than the event
            :meth:`~org.orekit.propagation.events.EventDetector.getThreshold` in order to ensure attitude continuity. The
            :code:`transitionFilter` parameter specifies the attitude time derivatives that should match at the boundaries between
            past attitude law and transition law on one side, and between transition law and future law on the other side.
            :meth:`~org.orekit.utils.AngularDerivativesFilter.USE_R` means only the rotation should be identical,
            :meth:`~org.orekit.utils.AngularDerivativesFilter.USE_RR` means both rotation and rotation rate should be identical,
            :meth:`~org.orekit.utils.AngularDerivativesFilter.USE_RRA` means both rotation, rotation rate and rotation acceleration
            should be identical. During the transition, the attitude law is computed by interpolating between past attitude law at
            switch time and future attitude law at current intermediate time.
        
            Parameters:
                past (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider applicable for times in the switch event occurrence past
                future (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider applicable for times in the switch event occurrence future
                switchEvent (T): event triggering the attitude providers switch
                switchOnIncrease (boolean): if true, switch is triggered on increasing event
                switchOnDecrease (boolean): if true, switch is triggered on decreasing event
                transitionTime (double): duration of the transition between the past and future attitude laws
                transitionFilter (:class:`~org.orekit.utils.AngularDerivativesFilter`): specification of transition law time derivatives that should match past and future attitude laws
                handler (:class:`~org.orekit.attitudes.AttitudesSequence.SwitchHandler`): handler to call for notifying when switch occurs (may be null)
        
            Since:
                7.1
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Description copied from interface: :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation`
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    def getSwitches(self) -> java.util.List['AttitudesSequence.Switch']: ...
    _registerSwitchEvents_0__T = typing.TypeVar('_registerSwitchEvents_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def registerSwitchEvents(self, field: org.hipparchus.Field[_registerSwitchEvents_0__T], fieldPropagator: org.orekit.propagation.FieldPropagator[_registerSwitchEvents_0__T]) -> None:
        """
            Register all wrapped switch events to the propagator.
        
            This method must be called once before propagation, after the switching conditions have been set up by calls to
            :meth:`~org.orekit.attitudes.AttitudesSequence.addSwitchingCondition`.
        
            Parameters:
                field (:class:`~org.orekit.attitudes.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field to which the elements belong
                propagator (:class:`~org.orekit.propagation.FieldPropagator`<T> propagator): propagator that will handle the events
        
        
        """
        ...
    @typing.overload
    def registerSwitchEvents(self, propagator: org.orekit.propagation.Propagator) -> None:
        """
            Register all wrapped switch events to the propagator.
        
            This method must be called once before propagation, after the switching conditions have been set up by calls to
            :meth:`~org.orekit.attitudes.AttitudesSequence.addSwitchingCondition`.
        
            Parameters:
                propagator (:class:`~org.orekit.propagation.Propagator`): propagator that will handle the events
        
        """
        ...
    def resetActiveProvider(self, attitudeProvider: AttitudeProvider) -> None:
        """
            Reset the active provider.
        
            Calling this method clears all already seen switch history, so it should *not* be used during the propagation itself, it
            is intended to be used only at start
        
            Parameters:
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): provider to activate
        
        
        """
        ...
    class Switch(org.orekit.propagation.events.EventDetector, org.orekit.propagation.events.handlers.EventHandler):
        def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action: ...
        def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float: ...
        def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler: ...
        def getMaxCheckInterval(self) -> org.orekit.propagation.events.AdaptableInterval: ...
        def getMaxIterationCount(self) -> int: ...
        def getThreshold(self) -> float: ...
        @typing.overload
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, eventDetector: org.orekit.propagation.events.EventDetector) -> None: ...
        @typing.overload
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
        def resetState(self, eventDetector: org.orekit.propagation.events.EventDetector, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState: ...
    class SwitchHandler:
        def switchOccurred(self, attitudeProvider: AttitudeProvider, attitudeProvider2: AttitudeProvider, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

class BoundedAttitudeProvider(AttitudeProvider):
    """
    public interface BoundedAttitudeProvider extends :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This interface is intended for attitude ephemerides valid only during a time range.
    
        This interface provides a mean to retrieve an attitude at any time within a given range. It should be implemented by
        attitude readers based on external data files.
    
        Since:
            10.3
    """
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the first date of the range.
        
            Returns:
                the first date of the range
        
        
        """
        ...

class CelestialBodyPointed(AttitudeProvider):
    """
    public class CelestialBodyPointed extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This class handles a celestial body pointed attitude provider.
    
        The celestial body pointed law is defined by two main elements:
    
          - a celestial body towards which some satellite axis is exactly aimed
          - a phasing reference defining the rotation around the pointing axis
    
    
        The celestial body implicitly defines two of the three degrees of freedom and the phasing reference defines the
        remaining degree of freedom. This definition can be represented as first aligning exactly the satellite pointing axis to
        the current direction of the celestial body, and then to find the rotation around this axis such that the satellite
        phasing axis is in the half-plane defined by a cut line on the pointing axis and containing the celestial phasing
        reference.
    
        In order for this definition to work, the user must ensure that the phasing reference is **never** aligned with the
        pointing reference. Since the pointed body moves as the date changes, this should be ensured regardless of the date. A
        simple way to do this for Sun, Moon or any planet pointing is to choose a phasing reference far from the ecliptic plane.
        Using :code:`Vector3D.PLUS_K`, the equatorial pole, is perfect in these cases.
    
        Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...

class FixedFrameBuilder(AttitudeBuilder):
    """
    public class FixedFrameBuilder extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeBuilder`
    
        Builder that assumes angular coordinates are given in a fixed frame.
    
        Since:
            11.0
    """
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude:
        """
            Build a filtered attitude.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeBuilder.build` in interface :class:`~org.orekit.attitudes.AttitudeBuilder`
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> FieldAttitude[_build_1__T]:
        """
            Build a filtered attitude.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeBuilder.build` in interface :class:`~org.orekit.attitudes.AttitudeBuilder`
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedFieldAngularCoordinates`<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        
        """
        ...

class FixedRate(AttitudeProvider):
    """
    public class FixedRate extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This class handles a simple attitude provider at constant rate around a fixed axis.
    
        This attitude provider is a simple linear extrapolation from an initial orientation, a rotation axis and a rotation
        rate. All this elements can be specified as a simple :class:`~org.orekit.attitudes.Attitude`.
    
        Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, attitude: Attitude): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    def getReferenceAttitude(self) -> Attitude:
        """
            Get the reference attitude.
        
            Returns:
                reference attitude
        
        
        """
        ...

class FrameAlignedProvider(AttitudeProvider):
    """
    public class FrameAlignedProvider extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This class handles an attitude provider aligned with a frame or a fixed offset to it.
    
        Instances of this class are guaranteed to be immutable.
    """
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @staticmethod
    def of(frame: org.orekit.frames.Frame) -> AttitudeProvider:
        """
            Creates an attitude provider aligned with the given frame.
        
            This attitude provider returned by this method is designed to be as fast as possible for when attitude is irrelevant
            while still being a valid implementation of :class:`~org.orekit.attitudes.AttitudeProvider`. To ensure good performance
            the specified attitude reference frame should be the same frame used for propagation so that computing the frame
            transformation is trivial.
        
            Parameters:
                satelliteFrame (:class:`~org.orekit.frames.Frame`): with which the satellite is aligned.
        
            Returns:
                new attitude provider aligned with the given frame.
        
            Since:
                11.0
        
        
        """
        ...

class GroundPointTarget(TargetProvider):
    """
    public class GroundPointTarget extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.TargetProvider`
    
        Ground point target for :class:`~org.orekit.attitudes.AlignedAndConstrained`.
    
        Since:
            12.2
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getDerivative2TargetDirection_0__T = typing.TypeVar('_getDerivative2TargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_getDerivative2TargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_getDerivative2TargetDirection_0__T]]: ...
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative2]: ...
    _getTargetDirection_0__T = typing.TypeVar('_getTargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTargetDirection_0__T]:
        """
            Get a target vector.
        
            Specified by:
                :meth:`~org.orekit.attitudes.TargetProvider.getTargetDirection` in
                interface :class:`~org.orekit.attitudes.TargetProvider`
        
            Parameters:
                sun (:class:`~org.orekit.utils.ExtendedPositionProvider`): Sun model
                earth (:class:`~org.orekit.bodies.OneAxisEllipsoid`): Earth model
                pv (:class:`~org.orekit.utils.TimeStampedFieldPVCoordinates`<T> pv): spacecraft position and velocity
                frame (:class:`~org.orekit.frames.Frame`): inertial frame
        
            Returns:
                target direction in the spacecraft state frame
        
        
        """
        ...
    @typing.overload
    def getTargetDirection(self, extendedPositionProvider: org.orekit.utils.ExtendedPositionProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get a target vector.
        
            Specified by:
                :meth:`~org.orekit.attitudes.TargetProvider.getTargetDirection` in
                interface :class:`~org.orekit.attitudes.TargetProvider`
        
            Parameters:
                sun (:class:`~org.orekit.utils.ExtendedPositionProvider`): Sun model
                earth (:class:`~org.orekit.bodies.OneAxisEllipsoid`): Earth model
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): spacecraft position and velocity
                frame (:class:`~org.orekit.frames.Frame`): inertial frame
        
            Returns:
                target direction in the spacecraft state frame
        
        """
        ...

class GroundPointing(AttitudeProvider):
    """
    public abstract class GroundPointing extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        Base class for ground pointing attitude providers.
    
        This class is a basic model for different kind of ground pointing attitude providers, such as : body center pointing,
        nadir pointing, target pointing, etc...
    
        The object :code:`GroundPointing` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.attitudes.AttitudeProvider`
    """
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
            Get the body frame.
        
            Returns:
                body frame
        
        
        """
        ...

class LofOffset(AttitudeProvider):
    """
    public class LofOffset extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        Attitude law defined by fixed Roll, Pitch and Yaw angles (in any order) with respect to a local orbital frame.
    
        The attitude provider is defined as a rotation offset from some local orbital frame.
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, double: float, double2: float, double3: float): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
            Get the inertial frame.
        
            Returns:
                the inertial frame.
        
        
        """
        ...
    def getLof(self) -> org.orekit.frames.LOF:
        """
            Get the local orbital frame.
        
            Returns:
                the local orbital frame.
        
        
        """
        ...
    def getOffset(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Get the rotational offset.
        
            Returns:
                the rotational offset.
        
        
        """
        ...

class PredefinedTarget(java.lang.Enum['PredefinedTarget'], TargetProvider):
    """
    public enum PredefinedTarget extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.attitudes.PredefinedTarget`> implements :class:`~org.orekit.attitudes.TargetProvider`
    
        Predefined targets for :class:`~org.orekit.attitudes.AlignedAndConstrained`.
    
        Since:
            12.2
    """
    SUN: typing.ClassVar['PredefinedTarget'] = ...
    EARTH: typing.ClassVar['PredefinedTarget'] = ...
    NADIR: typing.ClassVar['PredefinedTarget'] = ...
    NORTH: typing.ClassVar['PredefinedTarget'] = ...
    EAST: typing.ClassVar['PredefinedTarget'] = ...
    VELOCITY: typing.ClassVar['PredefinedTarget'] = ...
    MOMENTUM: typing.ClassVar['PredefinedTarget'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PredefinedTarget':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['PredefinedTarget']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PredefinedTarget c : PredefinedTarget.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PythonAttitudeBuilder(AttitudeBuilder):
    """
    public class PythonAttitudeBuilder extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeBuilder`
    """
    def __init__(self): ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude:
        """
            Build a filtered attitude.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeBuilder.build` in interface :class:`~org.orekit.attitudes.AttitudeBuilder`
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> FieldAttitude[_build_1__T]:
        """
            Build a filtered attitude.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeBuilder.build` in interface :class:`~org.orekit.attitudes.AttitudeBuilder`
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedFieldAngularCoordinates`<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        
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

class PythonAttitudeProvider(AttitudeProvider):
    """
    public class PythonAttitudeProvider extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
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

class TorqueFree(AttitudeProvider):
    """
    public class TorqueFree extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This class handles torque-free motion of a general (non-symmetrical) body.
    
        This attitude model is analytical, it can be called at any arbitrary date before or after the date of the initial
        attitude. Despite being an analytical model, it is *not* an approximation. It provides the attitude exactly in O(1)
        time.
    
        The equations are based on Landau and Lifchitz Course of Theoretical Physics, Mechanics vol 1, chapter 37. Some
        adaptations have been made to Landau and Lifchitz equations:
    
          - inertia can be in any order
          - initial conditions can be arbitrary
          - signs of several equations have been fixed to work for all initial conditions
          - equations have been rewritten to work in all octants
          - the φ angle model is based on a precomputed quadrature over one period computed at construction (the Landau and
            Lifchitz equations 37.17 to 37.20 seem to be wrong)
    
    
        The precomputed quadrature is performed numerically, but as it is performed only once at construction and the full
        integrated model over one period is saved, it can be applied analytically later on for any number of periods, hence we
        consider this attitude mode to be analytical.
    
        Since:
            12.0
    """
    def __init__(self, attitude: Attitude, inertia: Inertia): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getInertia(self) -> Inertia:
        """
            Get the spacecraft inertia.
        
            Returns:
                spacecraft inertia
        
        
        """
        ...
    def getInitialAttitude(self) -> Attitude:
        """
            Get the initial attitude.
        
            Returns:
                initial attitude
        
        
        """
        ...

class AggregateBoundedAttitudeProvider(BoundedAttitudeProvider):
    """
    public class AggregateBoundedAttitudeProvider extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
    
        A :class:`~org.orekit.attitudes.BoundedAttitudeProvider` that covers a larger time span from several constituent
        attitude providers that cover shorter time spans.
    
        Since:
            10.3
    """
    def __init__(self, collection: typing.Union[java.util.Collection[BoundedAttitudeProvider], typing.Sequence[BoundedAttitudeProvider]]): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMaxDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMinDate`
            Get the first date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMinDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the first date of the range
        
        
        """
        ...

class BodyCenterPointing(GroundPointing):
    """
    public class BodyCenterPointing extends :class:`~org.orekit.attitudes.GroundPointing`
    
        This class handles body center pointing attitude provider.
    
        This class represents the attitude provider where the satellite z axis is pointing to the body frame center.
    
        The object :code:`BodyCenterPointing` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.attitudes.GroundPointing`
    """
    def __init__(self, frame: org.orekit.frames.Frame, ellipsoid: org.orekit.bodies.Ellipsoid): ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...

class GroundPointingAttitudeModifier(GroundPointing, AttitudeProviderModifier):
    """
    public abstract class GroundPointingAttitudeModifier extends :class:`~org.orekit.attitudes.GroundPointing` implements :class:`~org.orekit.attitudes.AttitudeProviderModifier`
    
        Abstract class for attitude provider modifiers using an underlying ground pointing law.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.attitudes.GroundPointing`, :class:`~org.orekit.attitudes.AttitudeProviderModifier`
    """
    _getBaseState_1__T = typing.TypeVar('_getBaseState_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getBaseState(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the base system state at given date, without modifications.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which state is requested
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                satellite base attitude state.
        
        """
        ...
    @typing.overload
    def getBaseState(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getBaseState_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getBaseState_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getBaseState_1__T]:
        """
            Compute the base system state at given date, without modifications.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which state is requested
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                satellite base attitude state.
        
        
        """
        ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...
    def getUnderlyingAttitudeProvider(self) -> GroundPointing:
        """
            Getter for underlying ground pointing law.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProviderModifier.getUnderlyingAttitudeProvider` in
                interface :class:`~org.orekit.attitudes.AttitudeProviderModifier`
        
            Returns:
                underlying attitude provider, which in this case is a :class:`~org.orekit.attitudes.GroundPointing` instance
        
        
        """
        ...

class LofOffsetPointing(GroundPointing):
    """
    public class LofOffsetPointing extends :class:`~org.orekit.attitudes.GroundPointing`
    
        This class provides a default attitude provider.
    
        The attitude pointing law is defined by an attitude provider and the satellite axis vector chosen for pointing.
    """
    def __init__(self, frame: org.orekit.frames.Frame, bodyShape: org.orekit.bodies.BodyShape, attitudeProvider: AttitudeProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitude` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitude` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitudeRotation` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitudeRotation` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...

class NadirPointing(GroundPointing):
    """
    public class NadirPointing extends :class:`~org.orekit.attitudes.GroundPointing`
    
        This class handles nadir pointing attitude provider.
    
        This class represents the attitude provider where the satellite z axis is pointing to the vertical of the ground point
        under satellite.
    
        The object :code:`NadirPointing` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.attitudes.GroundPointing`
    """
    def __init__(self, frame: org.orekit.frames.Frame, bodyShape: org.orekit.bodies.BodyShape): ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...
    _getTargetPVViaInterpolation_0__T = typing.TypeVar('_getTargetPVViaInterpolation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPVViaInterpolation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPVViaInterpolation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPVViaInterpolation_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPVViaInterpolation_0__T]:
        """
            Compute target position-velocity-acceleration vector via interpolation (Field version).
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): PV provider
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                frame (:class:`~org.orekit.frames.Frame`): frame
        
            Returns:
                target position-velocity-acceleration
        
        
        """
        ...
    @typing.overload
    def getTargetPVViaInterpolation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute target position-velocity-acceleration vector via interpolation.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): PV provider
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                frame (:class:`~org.orekit.frames.Frame`): frame
        
            Returns:
                target position-velocity-acceleration
        
        """
        ...

class PythonAttitudeProviderModifier(AttitudeProviderModifier):
    """
    public class PythonAttitudeProviderModifier extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProviderModifier`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider:
        """
            Get the underlying attitude provider.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProviderModifier.getUnderlyingAttitudeProvider` in
                interface :class:`~org.orekit.attitudes.AttitudeProviderModifier`
        
            Returns:
                underlying attitude provider
        
        
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

class PythonBoundedAttitudeProvider(BoundedAttitudeProvider):
    """
    public class PythonBoundedAttitudeProvider extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMaxDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the first date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMinDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the first date of the range
        
        
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

class PythonGroundPointing(GroundPointing):
    """
    public class PythonGroundPointing extends :class:`~org.orekit.attitudes.GroundPointing`
    """
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    def finalize(self) -> None: ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
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

class PythonSwitchHandler(AttitudesSequence.SwitchHandler):
    """
    public class PythonSwitchHandler extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudesSequence.SwitchHandler`
    """
    def __init__(self): ...
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
    def switchOccurred(self, attitudeProvider: AttitudeProvider, attitudeProvider2: AttitudeProvider, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Method called when attitude is switched from one law to another law.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudesSequence.SwitchHandler.switchOccurred` in
                interface :class:`~org.orekit.attitudes.AttitudesSequence.SwitchHandler`
        
            Parameters:
                preceding (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude law used preceding the switch (i.e. in the past of the switch event for a forward propagation, or in the future
                    of the switch event for a backward propagation)
                following (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude law used following the switch (i.e. in the future of the switch event for a forward propagation, or in the past
                    of the switch event for a backward propagation)
                state (:class:`~org.orekit.propagation.SpacecraftState`): state at switch time (with attitude computed using the :code:`preceding` law)
        
        
        """
        ...

class SpinStabilized(AttitudeProviderModifier):
    """
    public class SpinStabilized extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeProviderModifier`
    
        This class handles a spin stabilized attitude provider.
    
        Spin stabilized laws are handled as wrappers for an underlying non-rotating law. This underlying law is typically an
        instance of :class:`~org.orekit.attitudes.CelestialBodyPointed` with the pointing axis equal to the rotation axis, but
        can in fact be anything.
    
        Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, attitudeProvider: AttitudeProvider, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Compute the attitude-related rotation corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitudeRotation` in
                interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider:
        """
            Get the underlying attitude provider.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProviderModifier.getUnderlyingAttitudeProvider` in
                interface :class:`~org.orekit.attitudes.AttitudeProviderModifier`
        
            Returns:
                underlying attitude provider
        
        
        """
        ...

class TabulatedLofOffset(BoundedAttitudeProvider):
    """
    public class TabulatedLofOffset extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
    
        This class handles an attitude provider interpolating from a predefined table containing offsets from a Local Orbital
        Frame.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.attitudes.LofOffset`, :class:`~org.orekit.attitudes.TabulatedProvider`
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMaxDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the first date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMinDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the first date of the range
        
        
        """
        ...
    def getTable(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]: ...

class TabulatedProvider(BoundedAttitudeProvider):
    """
    public class TabulatedProvider extends :class:`~org.orekit.attitudes.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
    
        This class handles an attitude provider interpolating from a predefined table.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            6.1
    
        Also see:
            :class:`~org.orekit.attitudes.TabulatedLofOffset`
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, attitudeBuilder: AttitudeBuilder): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMaxDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the first date of the range.
        
            Specified by:
                :meth:`~org.orekit.attitudes.BoundedAttitudeProvider.getMinDate` in
                interface :class:`~org.orekit.attitudes.BoundedAttitudeProvider`
        
            Returns:
                the first date of the range
        
        
        """
        ...

class TargetPointing(GroundPointing):
    """
    public class TargetPointing extends :class:`~org.orekit.attitudes.GroundPointing`
    
        This class handles target pointing attitude provider.
    
        This class represents the attitude provider where the satellite z axis is pointing to a ground point target.
    
        The target position is defined in a body frame specified by the user. It is important to make sure this frame is
        consistent.
    
        The object :code:`TargetPointing` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.attitudes.GroundPointing`
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, geodeticPoint: org.orekit.bodies.GeodeticPoint, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute the target point position/velocity in specified frame.
        
            Specified by:
                :meth:`~org.orekit.attitudes.GroundPointing.getTargetPV` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which target point is requested
                frame (:class:`~org.orekit.frames.Frame`): frame in which observed ground point should be provided
        
            Returns:
                observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...

class PythonGroundPointingAttitudeModifier(GroundPointingAttitudeModifier):
    """
    public class PythonGroundPointingAttitudeModifier extends :class:`~org.orekit.attitudes.GroundPointingAttitudeModifier`
    """
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, groundPointing: GroundPointing): ...
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

class YawCompensation(GroundPointingAttitudeModifier, AttitudeProviderModifier):
    """
    public class YawCompensation extends :class:`~org.orekit.attitudes.GroundPointingAttitudeModifier` implements :class:`~org.orekit.attitudes.AttitudeProviderModifier`
    
        This class handles yaw compensation attitude provider.
    
        Yaw compensation is mainly used for Earth observation satellites. As a satellites moves along its track, the image of
        ground points move on the focal point of the optical sensor. This motion is a combination of the satellite motion, but
        also on the Earth rotation and on the current attitude (in particular if the pointing includes Roll or Pitch offset). In
        order to reduce geometrical distortion, the yaw angle is changed a little from the simple ground pointing attitude such
        that the apparent motion of ground points is along a prescribed axis (orthogonal to the optical sensors rows), taking
        into account all effects.
    
        This attitude is implemented as a wrapper on top of an underlying ground pointing law that defines the roll and pitch
        angles.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.attitudes.GroundPointing`
    """
    def __init__(self, frame: org.orekit.frames.Frame, groundPointing: GroundPointing): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitude` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitude` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getYawAngle_1__T = typing.TypeVar('_getYawAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getYawAngle(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> float:
        """
            Compute the yaw compensation angle at date.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for PV coordinates
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which compensation is requested
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                yaw compensation angle for orbit.
        
        """
        ...
    @typing.overload
    def getYawAngle(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getYawAngle_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getYawAngle_1__T], frame: org.orekit.frames.Frame) -> _getYawAngle_1__T:
        """
            Compute the yaw compensation angle at date.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for PV coordinates
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which compensation is requested
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                yaw compensation angle for orbit.
        
            Since:
                9.0
        
        
        """
        ...

class YawSteering(GroundPointingAttitudeModifier, AttitudeProviderModifier):
    """
    public class YawSteering extends :class:`~org.orekit.attitudes.GroundPointingAttitudeModifier` implements :class:`~org.orekit.attitudes.AttitudeProviderModifier`
    
        This class handles yaw steering law.
    
        Yaw steering is mainly used for low Earth orbiting satellites with no missions-related constraints on yaw angle. It sets
        the yaw angle in such a way the solar arrays have maximal lighting without changing the roll and pitch.
    
        The motion in yaw is smooth when the Sun is far from the orbital plane, but gets more and more *square like* as the Sun
        gets closer to the orbital plane. The degenerate extreme case with the Sun in the orbital plane leads to a yaw angle
        switching between two steady states, with instantaneous π radians rotations at each switch, two times per orbit. This
        degenerate case is clearly not operationally sound so another pointing mode is chosen when Sun comes closer than some
        predefined threshold to the orbital plane.
    
        This class can handle (for now) only a theoretically perfect yaw steering (i.e. the yaw angle is exactly the optimal
        angle). Smoothed yaw steering with a few sine waves approaching the optimal angle will be added in the future if needed.
    
        This attitude is implemented as a wrapper on top of an underlying ground pointing law that defines the roll and pitch
        angles.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.attitudes.GroundPointing`
    """
    def __init__(self, frame: org.orekit.frames.Frame, groundPointing: GroundPointing, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitude` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Overrides:
                :meth:`~org.orekit.attitudes.GroundPointing.getAttitude` in class :class:`~org.orekit.attitudes.GroundPointing`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude on the specified date and position-velocity state
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.attitudes")``.

    AggregateBoundedAttitudeProvider: typing.Type[AggregateBoundedAttitudeProvider]
    AlignedAndConstrained: typing.Type[AlignedAndConstrained]
    Attitude: typing.Type[Attitude]
    AttitudeBuilder: typing.Type[AttitudeBuilder]
    AttitudeInterpolator: typing.Type[AttitudeInterpolator]
    AttitudeProvider: typing.Type[AttitudeProvider]
    AttitudeProviderModifier: typing.Type[AttitudeProviderModifier]
    AttitudesSequence: typing.Type[AttitudesSequence]
    BodyCenterPointing: typing.Type[BodyCenterPointing]
    BoundedAttitudeProvider: typing.Type[BoundedAttitudeProvider]
    CelestialBodyPointed: typing.Type[CelestialBodyPointed]
    FieldAttitude: typing.Type[FieldAttitude]
    FieldAttitudeInterpolator: typing.Type[FieldAttitudeInterpolator]
    FieldInertia: typing.Type[FieldInertia]
    FieldInertiaAxis: typing.Type[FieldInertiaAxis]
    FixedFrameBuilder: typing.Type[FixedFrameBuilder]
    FixedRate: typing.Type[FixedRate]
    FrameAlignedProvider: typing.Type[FrameAlignedProvider]
    GroundPointTarget: typing.Type[GroundPointTarget]
    GroundPointing: typing.Type[GroundPointing]
    GroundPointingAttitudeModifier: typing.Type[GroundPointingAttitudeModifier]
    Inertia: typing.Type[Inertia]
    InertiaAxis: typing.Type[InertiaAxis]
    LofOffset: typing.Type[LofOffset]
    LofOffsetPointing: typing.Type[LofOffsetPointing]
    NadirPointing: typing.Type[NadirPointing]
    PredefinedTarget: typing.Type[PredefinedTarget]
    PythonAttitudeBuilder: typing.Type[PythonAttitudeBuilder]
    PythonAttitudeProvider: typing.Type[PythonAttitudeProvider]
    PythonAttitudeProviderModifier: typing.Type[PythonAttitudeProviderModifier]
    PythonBoundedAttitudeProvider: typing.Type[PythonBoundedAttitudeProvider]
    PythonGroundPointing: typing.Type[PythonGroundPointing]
    PythonGroundPointingAttitudeModifier: typing.Type[PythonGroundPointingAttitudeModifier]
    PythonSwitchHandler: typing.Type[PythonSwitchHandler]
    SpinStabilized: typing.Type[SpinStabilized]
    TabulatedLofOffset: typing.Type[TabulatedLofOffset]
    TabulatedProvider: typing.Type[TabulatedProvider]
    TargetPointing: typing.Type[TargetPointing]
    TargetProvider: typing.Type[TargetProvider]
    TorqueFree: typing.Type[TorqueFree]
    YawCompensation: typing.Type[YawCompensation]
    YawSteering: typing.Type[YawSteering]
    class-use: org.orekit.attitudes.class-use.__module_protocol__
