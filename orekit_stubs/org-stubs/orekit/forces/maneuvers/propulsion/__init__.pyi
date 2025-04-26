
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.analysis.polynomials
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.forces.maneuvers
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class PropulsionModel(org.orekit.utils.ParameterDriversProvider, org.orekit.propagation.events.EventDetectorsProvider):
    """
    public interface PropulsionModel extends :class:`~org.orekit.utils.ParameterDriversProvider`, :class:`~org.orekit.propagation.events.EventDetectorsProvider`
    
        Generic interface for a propulsion model used in a :class:`~org.orekit.forces.maneuvers.Maneuver`.
    
        Since:
            10.2
    """
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], tArray: typing.Union[typing.List[_getAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
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
    def getAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, attitude: org.orekit.attitudes.Attitude, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
            Get the control vector's cost type.
        
            Returns:
                control cost type
        
            Since:
                12.0
        
        
        """
        ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    _getMassDerivatives_1__T = typing.TypeVar('_getMassDerivatives_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
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
    def getMassDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], tArray: typing.Union[typing.List[_getMassDerivatives_1__T], jpype.JArray]) -> _getMassDerivatives_1__T:
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

class ThrustVectorProvider:
    """
    public interface ThrustVectorProvider
    
        Interface defining thrust vectors depending on date and mass only. The frame is assumed to be the satellite one.
    
        Since:
            13.0
    """
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getThrustVector_0__T], t: _getThrustVector_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
            Get thrust vector at a specified date.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to consider
                mass (T): current mass
        
            Returns:
                thrust at :code:`date` (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get thrust vector at a specified date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to consider
                mass (double): current mass
        
            Returns:
                thrust at :code:`date` (N)
        
        """
        ...

class PolynomialThrustSegment(ThrustVectorProvider):
    """
    public class PolynomialThrustSegment extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider`
    
        Thrust vector given as polynomials for the Cartesian coordinates.
    
        Since:
            12.0
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, polynomialFunction: org.hipparchus.analysis.polynomials.PolynomialFunction, polynomialFunction2: org.hipparchus.analysis.polynomials.PolynomialFunction, polynomialFunction3: org.hipparchus.analysis.polynomials.PolynomialFunction): ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getThrustVector_0__T], t: _getThrustVector_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
            Get thrust vector at a specified date.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to consider
                mass (T): current mass
        
            Returns:
                thrust at :code:`date` (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get thrust vector at a specified date.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to consider
                mass (double): current mass
        
            Returns:
                thrust at :code:`date` (N)
        
        """
        ...

class PythonPropulsionModel(PropulsionModel):
    """
    public class PythonPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], tArray: typing.Union[typing.List[_getAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getAcceleration` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.FieldAttitude`<T> maneuverAttitude): current attitude in maneuver
                parameters (T[]): propulsion model parameters
        
            Returns:
                acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, attitude: org.orekit.attitudes.Attitude, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getAcceleration` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.Attitude`): current attitude in maneuver
                parameters (double[]): propulsion model parameters
        
            Returns:
                acceleration
        
        """
        ...
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
            Get the control vector's cost type.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getControl3DVectorCostType` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                control cost type
        
        
        """
        ...
    _getMassDerivatives_1__T = typing.TypeVar('_getMassDerivatives_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getMassDerivatives` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], tArray: typing.Union[typing.List[_getMassDerivatives_1__T], jpype.JArray]) -> _getMassDerivatives_1__T:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getMassDerivatives` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
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
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getName` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
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
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.init` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
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

class PythonThrustVectorProvider(ThrustVectorProvider):
    """
    public class PythonThrustVectorProvider extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getThrustVector_0__T], t: _getThrustVector_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
            Get thrust vector at a specified date.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to consider
                mass (T): current mass
        
            Returns:
                thrust at :code:`date` (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get thrust vector at a specified date.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustVectorProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to consider
                mass (double): current mass
        
            Returns:
                thrust at :code:`date` (N)
        
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

class ThrustPropulsionModel(PropulsionModel):
    """
    public interface ThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
    
        Interface for a thrust-based propulsion model.
    
        Since:
            10.2
    """
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], tArray: typing.Union[typing.List[_getAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame. Acceleration is computed here using the
            thrust vector in S/C frame.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getAcceleration` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                maneuverAttitude (:class:`~org.orekit.attitudes.FieldAttitude`<T> maneuverAttitude): current attitude in maneuver
                parameters (T[]): propulsion model parameters
        
            Returns:
                acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, attitude: org.orekit.attitudes.Attitude, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the acceleration of the spacecraft during maneuver and in maneuver frame. Acceleration is computed here using the
            thrust vector in S/C frame.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getAcceleration` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
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
        
            Return a zero vector if there is no thrust for given spacecraft state.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust direction in spacecraft frame
        
        
        """
        ...
    @staticmethod
    def getExhaustVelocity(double: float) -> float:
        """
            Method computing the effective exhaust velocity from the specific impulse.
        
            Parameters:
                isp (double): specific impulse (s)
        
            Returns:
                effective exhaust velocity (m/s)
        
            Since:
                13.0
        
        
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
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], tArray: typing.Union[typing.List[_getFlowRate_2__T], jpype.JArray]) -> _getFlowRate_2__T:
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
    def getMassDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver. Mass derivatives are directly extracted here from the
            flow rate value.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getMassDerivatives` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], tArray: typing.Union[typing.List[_getMassDerivatives_1__T], jpype.JArray]) -> _getMassDerivatives_1__T:
        """
            Get the mass derivative (i.e. flow rate in kg/s) during maneuver. Mass derivatives are directly extracted here from the
            flow rate value.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getMassDerivatives` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                mass derivative in kg/s
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
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
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class AbstractConstantThrustPropulsionModel(ThrustPropulsionModel):
    """
    public abstract class AbstractConstantThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
    
        This abstract class simply serve as a container for a constant thrust maneuver. It re-writes all spacecraft dependent
        methods from :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel` and removes their dependencies to
        current spacecraft state. Indeed since the thrust is constant (i.e. not variable during the maneuver), most of the
        calculated parameters (thrust vector, flow rate etc.) do not depend on current spacecraft state.
    
        Since:
            10.2
    """
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
            Get the control vector's cost type.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getControl3DVectorCostType` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                control cost type
        
        
        """
        ...
    @typing.overload
    def getDirection(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust direction in S/C frame.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the direction wants to be known
        
            Returns:
                the thrust direction in S/C frame
        
        """
        ...
    @typing.overload
    def getDirection(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust direction in S/C frame.
        
            Returns:
                the thrust direction in S/C frame, will throw exception if used on PDriver having several driven values, because in this
                case a date is needed.
        
        
        """
        ...
    @typing.overload
    def getDirection(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _getFlowRate_3__T = typing.TypeVar('_getFlowRate_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Returns:
                flow rate (kg/s) will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Get the flow rate (kg/s). Here the flow rate do not depend on current S/C state
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here the flow rate do not depend on current S/C state
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        public abstract <T extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> T getFlowRate (T[] parameters)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    @typing.overload
    def getFlowRate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def getFlowRate(self, tArray: typing.Union[typing.List[_getFlowRate_3__T], jpype.JArray]) -> _getFlowRate_3__T: ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_6__T], tArray: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T:
        """
            Get the flow rate (kg/s). Here the flow rate do not depend on current S/C state
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getIsp(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the specific impulse at given date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the Isp wants to be known
        
            Returns:
                specific impulse (s).
        
        
        """
        ...
    @typing.overload
    def getIsp(self) -> float:
        """
            Get the specific impulse.
        
            Returns:
                specific impulse (s), will throw exception if used on PDriver having several driven values, because in this case a date
                is needed.
        
        """
        ...
    @typing.overload
    def getIsp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getName` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                the maneuver name
        
        
        """
        ...
    @typing.overload
    def getThrustMagnitude(self) -> float:
        """
            Get the thrust magnitude (N).
        
            Returns:
                the thrust value (N), will throw an exception if called of a driver having several values driven
        
        """
        ...
    @typing.overload
    def getThrustMagnitude(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the thrust magnitude (N) at given date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                the thrust value (N)
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_4__T = typing.TypeVar('_getThrustVector_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Returns:
                thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here the thrust vector do not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here the thrust vector do not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        public abstract <T extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> :class:`~org.orekit.forces.maneuvers.propulsion.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> getThrustVector (T[] parameters)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_4__T], tArray: typing.Union[typing.List[_getThrustVector_4__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_4__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here the thrust vector do not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
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
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class ProfileThrustPropulsionModel(ThrustPropulsionModel):
    """
    public class ProfileThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
    
        Thrust propulsion model based on segmented profile.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, timeSpanMap: org.orekit.utils.TimeSpanMap[ThrustVectorProvider], double: float, string: str): ...
    @typing.overload
    def __init__(self, timeSpanMap: org.orekit.utils.TimeSpanMap[ThrustVectorProvider], double: float, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, string: str): ...
    def getActiveProvider(self, absoluteDate: org.orekit.time.AbsoluteDate) -> ThrustVectorProvider:
        """
            Getter for active provider at input date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
        
            Returns:
                active segment
        
            Since:
                13.0
        
        
        """
        ...
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
            Get the control vector's cost type.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getControl3DVectorCostType` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                control cost type
        
        
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
    _getFlowRate_2__T = typing.TypeVar('_getFlowRate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], tArray: typing.Union[typing.List[_getFlowRate_2__T], jpype.JArray]) -> _getFlowRate_2__T:
        """
            Get the flow rate (kg/s).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the maneuver name.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getName` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                the maneuver name
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
            Get the thrust vector in spacecraft frame (N).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
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
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _of__T = typing.TypeVar('_of__T', bound=ThrustVectorProvider)  # <T>
    @staticmethod
    def of(timeSpanMap: org.orekit.utils.TimeSpanMap[_of__T], double: float, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, string: str) -> 'ProfileThrustPropulsionModel':
        """
            Build with customized profile.
        
            Parameters:
                profile (:class:`~org.orekit.utils.TimeSpanMap`<T> profile): thrust profile (N)
                isp (double): specific impulse (s)
                name (:class:`~org.orekit.forces.maneuvers.Control3DVectorCostType`): name of the maneuver
                control3DVectorCostType (:class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): control vector's cost type
        
            Returns:
                propulsion model
        
            Since:
                13.0
        
        
        """
        ...

class PythonThrustPropulsionModel(ThrustPropulsionModel):
    """
    public class PythonThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
            Get the control vector's cost type.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.getControl3DVectorCostType` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Returns:
                control cost type
        
        
        """
        ...
    _getFlowRate_2__T = typing.TypeVar('_getFlowRate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], tArray: typing.Union[typing.List[_getFlowRate_2__T], jpype.JArray]) -> _getFlowRate_2__T:
        """
            Get the flow rate (kg/s).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getFlowRate` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current spacecraft state
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
            Get the thrust vector in spacecraft frame (N).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
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
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N).
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel.getThrustVector` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.ThrustPropulsionModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method. Called in when Maneuver.init(...) is called (from ForceModel.init(...))
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel.init` in
                interface :class:`~org.orekit.forces.maneuvers.propulsion.PropulsionModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
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
    public static final :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THRUST
    
        Parameter name for thrust.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLOW_RATE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` FLOW_RATE
    
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
    @typing.overload
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    @typing.overload
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, string: str): ...
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                flow rate (kg/s) will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_5__T], tArray: typing.Union[typing.List[_getFlowRate_5__T], jpype.JArray]) -> _getFlowRate_5__T: ...
    @typing.overload
    def getFlowRate(self, tArray: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
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
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self, tArray: typing.Union[typing.List[_getThrustVector_1__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_1__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
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
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class PythonAbstractConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel):
    """
    public class PythonAbstractConstantThrustPropulsionModel extends :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
    """
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, string: str): ...
    def finalize(self) -> None: ...
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                flow rate (kg/s) will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def getFlowRate(self, tArray: typing.Union[typing.List[_getFlowRate_5__T], jpype.JArray]) -> _getFlowRate_5__T:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        
        """
        ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_6__T], tArray: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_4__T = typing.TypeVar('_getThrustVector_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (T[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Description copied from
            class: :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector`
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_4__T], tArray: typing.Union[typing.List[_getThrustVector_4__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_4__T]: ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
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
    public static final :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THRUSTX_SCALE_FACTOR
    
        Parameter name for the scale factor on the X component of the thrust in S/C frame.
    
        Also see:
            :meth:`~constant`
    
    
    """
    THRUSTY_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THRUSTY_SCALE_FACTOR
    
        Parameter name for the scale factor on the Y component of the thrust in S/C frame.
    
        Also see:
            :meth:`~constant`
    
    
    """
    THRUSTZ_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.forces.maneuvers.propulsion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THRUSTZ_SCALE_FACTOR
    
        Parameter name for the scale factor on the Z component of the thrust in S/C frame.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, double: float, double2: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                flow rate (kg/s)
        
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self) -> float:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                flow rate (kg/s) will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_5__T], tArray: typing.Union[typing.List[_getFlowRate_5__T], jpype.JArray]) -> _getFlowRate_5__T: ...
    @typing.overload
    def getFlowRate(self, tArray: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T:
        """
            Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getFlowRate` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
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
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self, tArray: typing.Union[typing.List[_getThrustVector_1__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_1__T]:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
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
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                    the thrust parameter driver as only value estimated over the all orbit determination interval
        
            Returns:
                thrust vector in spacecraft frame (N)
        
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Parameters:
                parameters (double[]): propulsion model parameters
        
            Returns:
                thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel.getThrustVector` in
                class :class:`~org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel`
        
            Returns:
                thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers.propulsion")``.

    AbstractConstantThrustPropulsionModel: typing.Type[AbstractConstantThrustPropulsionModel]
    BasicConstantThrustPropulsionModel: typing.Type[BasicConstantThrustPropulsionModel]
    PolynomialThrustSegment: typing.Type[PolynomialThrustSegment]
    ProfileThrustPropulsionModel: typing.Type[ProfileThrustPropulsionModel]
    PropulsionModel: typing.Type[PropulsionModel]
    PythonAbstractConstantThrustPropulsionModel: typing.Type[PythonAbstractConstantThrustPropulsionModel]
    PythonPropulsionModel: typing.Type[PythonPropulsionModel]
    PythonThrustPropulsionModel: typing.Type[PythonThrustPropulsionModel]
    PythonThrustVectorProvider: typing.Type[PythonThrustVectorProvider]
    ScaledConstantThrustPropulsionModel: typing.Type[ScaledConstantThrustPropulsionModel]
    ThrustPropulsionModel: typing.Type[ThrustPropulsionModel]
    ThrustVectorProvider: typing.Type[ThrustVectorProvider]
