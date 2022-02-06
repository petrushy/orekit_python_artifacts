import java.util
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



class PropulsionModel:
    """
    public interface PropulsionModel
    
        Generic interface for a propulsion model used in a :class:`~org.orekit.forces.maneuvers.Maneuver`.
    
        Since:
            10.2
    """
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], tArray: typing.List[_getAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.FieldAttitude`<T> maneuverAttitude): current attitude in maneuver
                parameters (T[]): propulsion model parameters
        
            Returns:
                acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, attitude: org.orekit.attitudes.Attitude, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.Attitude`): current attitude in maneuver
                parameters (double[]): propulsion model parameters
        
            Returns:
                acceleration
        
        """
        ...
    _getMassDerivatives_1__T = typing.TypeVar('_getMassDerivatives_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], tArray: typing.List[_getMassDerivatives_1__T]) -> _getMassDerivatives_1__T:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                mass derivative in kg/s
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Returns:
                the maneuver name
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...))
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> initialState): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.FieldAbsoluteDate`<T> target): date of propagation. Not equal to :code:`initialState.getDate()`.
        
            Since:
                11.1
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...))
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...

class ThrustDirectionAndAttitudeProvider(org.orekit.attitudes.AttitudeProvider):
    """
    public class ThrustDirectionAndAttitudeProvider extends Object implements :class:`~org.orekit.attitudes.AttitudeProvider`
    
        This class is used in to both manage the attitude of the satellite and the direction of thrust. It is used in
        ConfigurableLowThrustManeuver to set the spacecraft attitude according to the expected thrust direction. The direction
        can be variable or fixed, defined in the spaceraft frame, a Local Orbital Frame or a user frame. It is also possible to
        use an external attitude provider.
    
        Since:
            10.2
    """
    @staticmethod
    def buildFromCustomAttitude(attitudeProvider: org.orekit.attitudes.AttitudeProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'ThrustDirectionAndAttitudeProvider':
        """
            Build a ThrustDirectionAndAttitudeProvider where the attitude is provided by an external. Object the direction of thrust
            will be constant
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the object that provide the satellite attitude
                direction (Vector3D): thruster axis in satellite frame
        
            Returns:
                a new instance
        
        
        """
        ...
    @staticmethod
    def buildFromDirectionInFrame(frame: org.orekit.frames.Frame, thrustDirectionProvider: 'ThrustDirectionProvider', vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'ThrustDirectionAndAttitudeProvider':
        """
            Build a ThrustDirectionAndAttitudeProvider by a variable direction in a custom frame.
        
            Parameters:
                thrustDirectionFrame (:class:`~org.orekit.frames.Frame`): reference frame for thrust direction
                variableDirectionInFrame (:class:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider`): the object providing the thrust direction
                thrusterAxisInSatelliteFrame (Vector3D): thruster axis in satellite frame
        
            Returns:
                a new instance
        
        
        """
        ...
    @staticmethod
    def buildFromDirectionInLOF(lOFType: org.orekit.frames.LOFType, thrustDirectionProvider: 'ThrustDirectionProvider', vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'ThrustDirectionAndAttitudeProvider':
        """
            Build a ThrustDirectionAndAttitudeProvider by a variable direction in a Local Orbital Frame.
        
            Parameters:
                thrustDirectionLofType (:class:`~org.orekit.frames.LOFType`): Local Orbital Frame type
                variableDirectionInFrame (:class:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider`): the object providing the thrust direction
                thrusterAxisInSatelliteFrame (Vector3D): thruster axis in satellite frame
        
            Returns:
                a new instance
        
        
        """
        ...
    @staticmethod
    def buildFromFixedDirectionInSatelliteFrame(vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'ThrustDirectionAndAttitudeProvider':
        """
            Build a ThrustDirectionAndAttitudeProvider from a fixed direction in the satellite frame. The satellite attitude won't
            be managed by this object
        
            Parameters:
                direction (Vector3D): constant direction in the satellite frame
        
            Returns:
                a new instance
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.attitudes.Attitude:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> org.orekit.attitudes.FieldAttitude[_getAttitude_1__T]:
        """
            Compute the attitude corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeProvider.getAttitude` in interface :class:`~org.orekit.attitudes.AttitudeProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): local position-velocity provider around current date
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                attitude attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getManeuverAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Attitude provider to use.
        
            Returns:
                null in mode SATELLITE_ATTITUDE
        
        
        """
        ...
    def getThrusterAxisInSatelliteFrame(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Thruster axis in satellite frame.
        
            Returns:
                field
        
        
        """
        ...

class ThrustDirectionProvider:
    """
    public interface ThrustDirectionProvider
    
        Interface to compute the thrust direction of a maneuver.
    
        Since:
            10.2
    """
    def computeThrustDirection(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the thrust direction corresponding to an orbital state.
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                direction thrust direction at the specified date and position-velocity state
        
        
        """
        ...

class ConstantThrustDirectionProvider(ThrustDirectionProvider):
    """
    public class ConstantThrustDirectionProvider extends Object implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider`
    
        Simple implementation of VariableThrustDirectionVector, providing a constant direction.
    
        Since:
            10.2
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def computeThrustDirection(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Description copied from
            interface:Â :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider.computeThrustDirection`
            Compute the thrust direction corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider.computeThrustDirection`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                direction thrust direction at the specified date and position-velocity state
        
        
        """
        ...

class PythonPropulsionModel(PropulsionModel):
    """
    public class PythonPropulsionModel extends Object implements :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAcceleration_1__T = typing.TypeVar('_getAcceleration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, attitude: org.orekit.attitudes.Attitude, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.Attitude`): current attitude in maneuver
                parameters (double[]): propulsion model parameters
        
            Returns:
                acceleration
        
            Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.FieldAttitude`<T> maneuverAttitude): current attitude in maneuver
                parameters (T[]): propulsion model parameters
        
            Returns:
                acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_1__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_1__T], tArray: typing.List[_getAcceleration_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_1__T]: ...
    _getAcceleration_FFT__T = typing.TypeVar('_getAcceleration_FFT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getAcceleration_FFT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_FFT__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_FFT__T], tArray: typing.List[_getAcceleration_FFT__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_FFT__T]: ...
    _getMassDerivatives_1__T = typing.TypeVar('_getMassDerivatives_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters @return mass derivative in kg/s
        
            Returns:
                mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], tArray: typing.List[_getMassDerivatives_1__T]) -> _getMassDerivatives_1__T:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters @return mass derivative in kg/s
        
            Returns:
                mass derivative in kg/s
        
        
        """
        ...
    _getMassDerivatives_FT__T = typing.TypeVar('_getMassDerivatives_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getMassDerivatives_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_FT__T], tArray: typing.List[_getMassDerivatives_FT__T]) -> _getMassDerivatives_FT__T: ...
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getName`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                the maneuver name
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...))
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
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

class PythonThrustDirectionProvider(ThrustDirectionProvider):
    """
    public class PythonThrustDirectionProvider extends Object implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider`
    """
    def __init__(self): ...
    def computeThrustDirection(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the thrust direction corresponding to an orbital state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider.computeThrustDirection`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionProvider`
        
            Parameters:
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): local position-velocity provider around current date
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): reference frame from which attitude is computed
        
            Returns:
                direction thrust direction at the specified date and position-velocity state
        
        
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

class ThrustPropulsionModel(PropulsionModel):
    """
    public interface ThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
    
        Interface for a thrust-based propulsion model.
    
        Since:
            10.2
    """
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], tArray: typing.List[_getAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame. Acceleration is computed here using the
            thrust vector in S/C frame.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.FieldAttitude`<T> maneuverAttitude): current attitude in maneuver
                parameters (T[]): propulsion model parameters
        
            Returns:
                acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, attitude: org.orekit.attitudes.Attitude, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame. Acceleration is computed here using the
            thrust vector in S/C frame.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.Attitude`): current attitude in maneuver
                parameters (double[]): propulsion model parameters
        
            Returns:
                acceleration
        
        """
        ...
    def getDirection(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust direction in spacecraft frame.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust direction in spacecraft frame
        
        
        """
        ...
    _getFlowRate_2__T = typing.TypeVar('_getFlowRate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s).
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s).
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], tArray: typing.List[_getFlowRate_2__T]) -> _getFlowRate_2__T:
        """
            Get the flow rate (kg/s).
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    def getIsp(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the specific impulse (s).
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                specific impulse (s).
        
        
        """
        ...
    _getMassDerivatives_1__T = typing.TypeVar('_getMassDerivatives_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver. Mass derivatives are directly extracted here from the
            flow rate value.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], tArray: typing.List[_getMassDerivatives_1__T]) -> _getMassDerivatives_1__T:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver. Mass derivatives are directly extracted here from the
            flow rate value.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                mass derivative in kg/s
        
        
        """
        ...
    def getThrust(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the thrust norm (N).
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust norm (N)
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.List[_getThrustVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
            Get the thrust vector in spacecraft frame (N).
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N).
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N).
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class AbstractConstantThrustPropulsionModel(ThrustPropulsionModel):
    """
    public abstract class AbstractConstantThrustPropulsionModel extends Object implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
    
        This abstract class simply serve as a container for a constant thrust maneuver. It re-writes all spacecraft dependent
        methods from :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel` and removes their dependencies to
        current spacecraft state. Indeed since the thrust is constant (i.e. not variable during the maneuver), most of the
        calculated parameters (thrust vector, flow rate etc.) do not depend on current spacecraft state.
    
        Since:
            10.2
    """
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    @typing.overload
    def getDirection(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getDirection(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust direction in S/C frame.
        
            Returns:
                the thrust direction in S/C frame
        
        
        """
        ...
    _getFlowRate_2__T = typing.TypeVar('_getFlowRate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.List[float]) -> float:
        """
            Get the flow rate (kg/s). Here the flow rate do not depend on current S/C state
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here the flow rate do not depend on current S/C state
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        public abstract <T extends CalculusFieldElement<T>> T getFlowRate(T[] parameters)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    @typing.overload
    def getFlowRate(self, tArray: typing.List[_getFlowRate_2__T]) -> _getFlowRate_2__T: ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_5__T], tArray: typing.List[_getFlowRate_5__T]) -> _getFlowRate_5__T:
        """
            Get the flow rate (kg/s). Here the flow rate do not depend on current S/C state
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getIsp(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def getIsp(self) -> float:
        """
            Get the specific impulse.
        
            Returns:
                specific impulse (s).
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getName`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                the maneuver name
        
        
        """
        ...
    @typing.overload
    def getThrust(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def getThrust(self) -> float:
        """
            Get the thrust value (N).
        
            Returns:
                the thrust value (N)
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_3__T = typing.TypeVar('_getThrustVector_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, tArray: typing.List[_getThrustVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here the thrust vector do not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here the thrust vector do not depend on current S/C state.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_3__T], tArray: typing.List[_getThrustVector_3__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_3__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here the thrust vector do not depend on current S/C state.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class PythonThrustPropulsionModel(ThrustPropulsionModel):
    """
    public class PythonThrustPropulsionModel extends Object implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getFlowRate_2__T = typing.TypeVar('_getFlowRate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s).
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], tArray: typing.List[_getFlowRate_2__T]) -> _getFlowRate_2__T:
        """
            Get the flow rate (kg/s).
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    _getFlowRate_FT__T = typing.TypeVar('_getFlowRate_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFlowRate_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_FT__T], tArray: typing.List[_getFlowRate_FT__T]) -> _getFlowRate_FT__T: ...
    _getThrustVector_2__T = typing.TypeVar('_getThrustVector_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N).
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N).
        
            Specified by:
                 in interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_2__T], tArray: typing.List[_getThrustVector_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_2__T]: ...
    _getThrustVector_FT__T = typing.TypeVar('_getThrustVector_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getThrustVector_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_FT__T], tArray: typing.List[_getThrustVector_FT__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_FT__T]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Description copied from interface: :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.init`
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...))
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
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

class BasicConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel):
    """
    public class BasicConstantThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
    
        Constant thrust propulsion model with: - Constant thrust direction in spacecraft frame - Parameter drivers (for
        estimation) for the thrust norm or the flow rate. Note that both parameters CANNOT be selected at the same time since
        they depend on one another.
    
        Since:
            10.2
    """
    THRUST: typing.ClassVar[str] = ...
    """
    public static final String THRUST
    
        Parameter name for thrust.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLOW_RATE: typing.ClassVar[str] = ...
    """
    public static final String FLOW_RATE
    
        Parameter name for flow rate.
    
        Also see:
            :meth:`~constant`
    
    
    """
    THRUST_SCALE: typing.ClassVar[float] = ...
    """
    public static final double THRUST_SCALE
    
        Thrust scaling factor.
    
        We use a power of 2 to avoid numeric noise introduction in the multiplications/divisions sequences.
    
    """
    FLOW_RATE_SCALE: typing.ClassVar[float] = ...
    """
    public static final double FLOW_RATE_SCALE
    
        Flow rate scaling factor.
    
        We use a power of 2 to avoid numeric noise introduction in the multiplications/divisions sequences.
    
    """
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    _getFlowRate_4__T = typing.TypeVar('_getFlowRate_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_4__T], tArray: typing.List[_getFlowRate_4__T]) -> _getFlowRate_4__T: ...
    @typing.overload
    def getFlowRate(self, tArray: typing.List[_getFlowRate_5__T]) -> _getFlowRate_5__T:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_1__T = typing.TypeVar('_getThrustVector_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.List[_getThrustVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self, tArray: typing.List[_getThrustVector_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_1__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class PythonAbstractConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel, ThrustPropulsionModel):
    """
    public class PythonAbstractConstantThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel` implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
    """
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    def finalize(self) -> None: ...
    _getFlowRate_4__T = typing.TypeVar('_getFlowRate_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_4__T], tArray: typing.List[_getFlowRate_4__T]) -> _getFlowRate_4__T: ...
    @typing.overload
    def getFlowRate(self, tArray: typing.List[_getFlowRate_5__T]) -> _getFlowRate_5__T:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    _getFlowRate_T__T = typing.TypeVar('_getFlowRate_T__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFlowRate_T(self, tArray: typing.List[_getFlowRate_T__T]) -> _getFlowRate_T__T:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    _getThrustVector_2__T = typing.TypeVar('_getThrustVector_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_3__T = typing.TypeVar('_getThrustVector_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_2__T], tArray: typing.List[_getThrustVector_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_2__T]: ...
    @typing.overload
    def getThrustVector(self, tArray: typing.List[_getThrustVector_3__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_3__T]: ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _getThrustVector_T__T = typing.TypeVar('_getThrustVector_T__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getThrustVector_T(self, tArray: typing.List[_getThrustVector_T__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_T__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...))
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
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

class ScaledConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel):
    """
    public class ScaledConstantThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
    
        Thrust propulsion model with parameters (for estimation) represented by scale factors on the X, Y and Z axis of the
        spacecraft frame.
    
        Since:
            10.2
    """
    THRUSTX_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    public static final String THRUSTX_SCALE_FACTOR
    
        Parameter name for the scale factor on the X component of the thrust in S/C frame.
    
        Also see:
            :meth:`~constant`
    
    
    """
    THRUSTY_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    public static final String THRUSTY_SCALE_FACTOR
    
        Parameter name for the scale factor on the Y component of the thrust in S/C frame.
    
        Also see:
            :meth:`~constant`
    
    
    """
    THRUSTZ_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    public static final String THRUSTZ_SCALE_FACTOR
    
        Parameter name for the scale factor on the Z component of the thrust in S/C frame.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    _getFlowRate_4__T = typing.TypeVar('_getFlowRate_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_4__T], tArray: typing.List[_getFlowRate_4__T]) -> _getFlowRate_4__T: ...
    @typing.overload
    def getFlowRate(self, tArray: typing.List[_getFlowRate_5__T]) -> _getFlowRate_5__T:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_1__T = typing.TypeVar('_getThrustVector_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.List[_getThrustVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self, tArray: typing.List[_getThrustVector_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_1__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                 in class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector`Â in
                classÂ :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers.propulsion")``.

    AbstractConstantThrustPropulsionModel: typing.Type[AbstractConstantThrustPropulsionModel]
    BasicConstantThrustPropulsionModel: typing.Type[BasicConstantThrustPropulsionModel]
    ConstantThrustDirectionProvider: typing.Type[ConstantThrustDirectionProvider]
    PropulsionModel: typing.Type[PropulsionModel]
    PythonAbstractConstantThrustPropulsionModel: typing.Type[PythonAbstractConstantThrustPropulsionModel]
    PythonPropulsionModel: typing.Type[PythonPropulsionModel]
    PythonThrustDirectionProvider: typing.Type[PythonThrustDirectionProvider]
    PythonThrustPropulsionModel: typing.Type[PythonThrustPropulsionModel]
    ScaledConstantThrustPropulsionModel: typing.Type[ScaledConstantThrustPropulsionModel]
    ThrustDirectionAndAttitudeProvider: typing.Type[ThrustDirectionAndAttitudeProvider]
    ThrustDirectionProvider: typing.Type[ThrustDirectionProvider]
    ThrustPropulsionModel: typing.Type[ThrustPropulsionModel]
