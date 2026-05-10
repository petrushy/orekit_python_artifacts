
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
    Generic interface for a propulsion model used in a Maneuver.
    
    Since:
        10.2
    """
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], maneuverAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], parameters: typing.Union[typing.List[_getAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
        """
        Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            maneuverAttitude (FieldAttitude<T> maneuverAttitude): current attitude in maneuver
            parameters (T[]): propulsion model parameters
        
        Returns:
            acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, s: org.orekit.propagation.SpacecraftState, maneuverAttitude: org.orekit.attitudes.Attitude, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            maneuverAttitude (Attitude): current attitude in maneuver
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
    def getMassDerivatives(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, s: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], parameters: typing.Union[typing.List[_getMassDerivatives_1__T], jpype.JArray]) -> _getMassDerivatives_1__T:
        """
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
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
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): initial spacecraft state (at the start of propagation).
            target (FieldAbsoluteDate<T> target): date of propagation. Not equal to getDate().
        
        Since:
            11.1
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...

class ThrustVectorProvider:
    """
    Interface defining thrust vectors depending on date and mass only. The frame is assumed to be the satellite one.
    
    Since:
        13.0
    """
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, date: org.orekit.time.FieldAbsoluteDate[_getThrustVector_0__T], mass: _getThrustVector_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
        Get thrust vector at a specified date.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to consider
            mass (T): current mass
        
        Returns:
            thrust at date (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, date: org.orekit.time.AbsoluteDate, mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get thrust vector at a specified date.
        
        Parameters:
            date (AbsoluteDate): date to consider
            mass (double): current mass
        
        Returns:
            thrust at date (N)
        
        """
        ...

class PolynomialThrustSegment(ThrustVectorProvider):
    """
    Thrust vector given as polynomials for the Cartesian coordinates.
    
    Since:
        12.0
    """
    def __init__(self, referenceDate: org.orekit.time.AbsoluteDate, xThrust: org.hipparchus.analysis.polynomials.PolynomialFunction, yThrust: org.hipparchus.analysis.polynomials.PolynomialFunction, zThrust: org.hipparchus.analysis.polynomials.PolynomialFunction):
        """
        Simple constructor.
        
        Parameters:
            referenceDate (AbsoluteDate): reference date of the polynomials
            xThrust (PolynomialFunction): thrust along X direction (N)
            yThrust (PolynomialFunction): thrust along Y direction (N)
            zThrust (PolynomialFunction): thrust along Z direction (N)
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, date: org.orekit.time.FieldAbsoluteDate[_getThrustVector_0__T], mass: _getThrustVector_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
        Get thrust vector at a specified date.
        
        Specified by: getThrustVector in interface ThrustVectorProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to consider
            mass (T): current mass
        
        Returns:
            thrust at date (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, date: org.orekit.time.AbsoluteDate, mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get thrust vector at a specified date.
        
        Specified by: getThrustVector in interface ThrustVectorProvider
        
        Parameters:
            date (AbsoluteDate): date to consider
            mass (double): current mass
        
        Returns:
            thrust at date (N)
        
        """
        ...

class PythonPropulsionModel(PropulsionModel):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], maneuverAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], parameters: typing.Union[typing.List[_getAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
        """
        Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
        Specified by: getAcceleration in interface PropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            maneuverAttitude (FieldAttitude<T> maneuverAttitude): current attitude in maneuver
            parameters (T[]): propulsion model parameters
        
        Returns:
            acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, s: org.orekit.propagation.SpacecraftState, maneuverAttitude: org.orekit.attitudes.Attitude, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the acceleration of the spacecraft during maneuver and in maneuver frame.
        
        Specified by: getAcceleration in interface PropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            maneuverAttitude (Attitude): current attitude in maneuver
            parameters (double[]): propulsion model parameters
        
        Returns:
            acceleration
        
        """
        ...
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
        Get the control vector's cost type.
        
        Specified by: getControl3DVectorCostType in interface PropulsionModel
        
        Returns:
            control cost type
        
        
        """
        ...
    _getMassDerivatives_1__T = typing.TypeVar('_getMassDerivatives_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivatives(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Specified by: getMassDerivatives in interface PropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, s: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], parameters: typing.Union[typing.List[_getMassDerivatives_1__T], jpype.JArray]) -> _getMassDerivatives_1__T:
        """
        Specified by: getMassDerivatives in interface PropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            mass derivative in kg/s
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the maneuver name.
        
        Specified by: getName in interface PropulsionModel
        
        Returns:
            the maneuver name
        
        
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
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Specified by: init in interface PropulsionModel
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
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

class PythonThrustVectorProvider(ThrustVectorProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, date: org.orekit.time.FieldAbsoluteDate[_getThrustVector_0__T], mass: _getThrustVector_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
        Get thrust vector at a specified date.
        
        Specified by: getThrustVector in interface ThrustVectorProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to consider
            mass (T): current mass
        
        Returns:
            thrust at date (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, date: org.orekit.time.AbsoluteDate, mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get thrust vector at a specified date.
        
        Specified by: getThrustVector in interface ThrustVectorProvider
        
        Parameters:
            date (AbsoluteDate): date to consider
            mass (double): current mass
        
        Returns:
            thrust at date (N)
        
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

class ThrustPropulsionModel(PropulsionModel):
    """
    Interface for a thrust-based propulsion model.
    
    Since:
        10.2
    """
    _getAcceleration_0__T = typing.TypeVar('_getAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAcceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_getAcceleration_0__T], maneuverAttitude: org.orekit.attitudes.FieldAttitude[_getAcceleration_0__T], parameters: typing.Union[typing.List[_getAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAcceleration_0__T]:
        """
        Get the acceleration of the spacecraft during maneuver and in maneuver frame. Acceleration is computed here using the thrust vector in S/C frame.
        
        Specified by: getAcceleration in interface PropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            maneuverAttitude (FieldAttitude<T> maneuverAttitude): current attitude in maneuver
            parameters (T[]): propulsion model parameters
        
        Returns:
            acceleration
        
        
        """
        ...
    @typing.overload
    def getAcceleration(self, s: org.orekit.propagation.SpacecraftState, maneuverAttitude: org.orekit.attitudes.Attitude, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the acceleration of the spacecraft during maneuver and in maneuver frame. Acceleration is computed here using the thrust vector in S/C frame.
        
        Specified by: getAcceleration in interface PropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            maneuverAttitude (Attitude): current attitude in maneuver
            parameters (double[]): propulsion model parameters
        
        Returns:
            acceleration
        
        """
        ...
    def getDirection(self, s: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the thrust direction in spacecraft frame.
        
        Return a zero vector if there is no thrust for given spacecraft state.
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            thrust direction in spacecraft frame
        
        
        """
        ...
    @staticmethod
    def getExhaustVelocity(isp: float) -> float:
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
    def getFlowRate(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s).
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], parameters: typing.Union[typing.List[_getFlowRate_2__T], jpype.JArray]) -> _getFlowRate_2__T:
        """
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        
        """
        ...
    def getIsp(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Get the specific impulse (s).
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            specific impulse (s).
        
        
        """
        ...
    _getMassDerivatives_1__T = typing.TypeVar('_getMassDerivatives_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivatives(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        flow rate value.
        
        Specified by: getMassDerivatives in interface PropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            mass derivative in kg/s
        
        """
        ...
    @typing.overload
    def getMassDerivatives(self, s: org.orekit.propagation.FieldSpacecraftState[_getMassDerivatives_1__T], parameters: typing.Union[typing.List[_getMassDerivatives_1__T], jpype.JArray]) -> _getMassDerivatives_1__T:
        """
        flow rate value.
        
        Specified by: getMassDerivatives in interface PropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            mass derivative in kg/s
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], parameters: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N).
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class AbstractConstantThrustPropulsionModel(ThrustPropulsionModel):
    """
    This abstract class simply serve as a container for a constant thrust maneuver. It re-writes all spacecraft dependent methods from ThrustPropulsionModel and removes their dependencies to current spacecraft state. Indeed since the thrust is constant (i.e. not variable during the maneuver), most of the calculated parameters (thrust vector, flow rate etc.) do not depend on current spacecraft state.
    
    Since:
        10.2
    """
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
        Get the control vector's cost type.
        
        Specified by: getControl3DVectorCostType in interface PropulsionModel
        
        Returns:
            control cost type
        
        
        """
        ...
    @typing.overload
    def getDirection(self, date: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the thrust direction in S/C frame.
        
        Parameters:
            date (AbsoluteDate): date at which the direction wants to be known
        
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
    def getDirection(self, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _getFlowRate_3__T = typing.TypeVar('_getFlowRate_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self) -> float:
        """
        Returns:
            flow rate (kg/s) will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getFlowRate(self, s: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s). Here the flow rate do not depend on current S/C state
        
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s). Here it does not depend on current S/C.
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
        Parameters:
            parameters (double[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        public abstract <T extends CalculusFieldElement<T>> T getFlowRate (T[] parameters)
        
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
    def getFlowRate(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_6__T], parameters: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T:
        """
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getIsp(self, date: org.orekit.propagation.SpacecraftState) -> float:
        """
        Get the specific impulse at given date.
        
        Parameters:
            date (AbsoluteDate): date at which the Isp wants to be known
        
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
    def getIsp(self, date: org.orekit.time.AbsoluteDate) -> float: ...
    def getName(self) -> str:
        """
        Get the maneuver name.
        
        Specified by: getName in interface PropulsionModel
        
        Returns:
            the maneuver name
        
        
        """
        ...
    @typing.overload
    def getThrustMagnitude(self) -> float:
        """
        Returns:
            the thrust value (N), will throw an exception if called of a driver having several values driven
        
        """
        ...
    @typing.overload
    def getThrustMagnitude(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
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
        Returns:
            thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, s: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N). Here the thrust vector do not depend on current S/C state.
        
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
        Parameters:
            parameters (double[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        public abstract <T extends CalculusFieldElement<T>> FieldVector3D<T> getThrustVector (T[] parameters)
        
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
    def getThrustVector(self, s: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_4__T], parameters: typing.Union[typing.List[_getThrustVector_4__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_4__T]:
        """
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class ProfileThrustPropulsionModel(ThrustPropulsionModel):
    """
    Thrust propulsion model based on segmented profile.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, profile: org.orekit.utils.TimeSpanMap[ThrustVectorProvider], isp: float, name: str): ...
    @typing.overload
    def __init__(self, profile: org.orekit.utils.TimeSpanMap[ThrustVectorProvider], isp: float, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, name: str): ...
    def getActiveProvider(self, date: org.orekit.time.AbsoluteDate) -> ThrustVectorProvider:
        """
        Getter for active provider at input date.
        
        Parameters:
            date (AbsoluteDate): date
        
        Returns:
            active segment
        
        Since:
            13.0
        
        
        """
        ...
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
        Get the control vector's cost type.
        
        Specified by: getControl3DVectorCostType in interface PropulsionModel
        
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
    def getFlowRate(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s).
        
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], parameters: typing.Union[typing.List[_getFlowRate_2__T], jpype.JArray]) -> _getFlowRate_2__T:
        """
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the maneuver name.
        
        Specified by: getName in interface PropulsionModel
        
        Returns:
            the maneuver name
        
        
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
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], parameters: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N).
        
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _of__T = typing.TypeVar('_of__T', bound=ThrustVectorProvider)  # <T>
    @staticmethod
    def of(profile: org.orekit.utils.TimeSpanMap[_of__T], isp: float, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, name: str) -> 'ProfileThrustPropulsionModel':
        """
        Build with customized profile.
        
        Parameters:
            profile (TimeSpanMap<T> profile): thrust profile (N)
            isp (double): specific impulse (s)
            name (Control3DVectorCostType): name of the maneuver
            control3DVectorCostType (String): control vector's cost type
        
        Returns:
            propulsion model
        
        Since:
            13.0
        
        
        """
        ...

class PythonThrustPropulsionModel(ThrustPropulsionModel):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getControl3DVectorCostType(self) -> org.orekit.forces.maneuvers.Control3DVectorCostType:
        """
        Get the control vector's cost type.
        
        Specified by: getControl3DVectorCostType in interface PropulsionModel
        
        Returns:
            control cost type
        
        
        """
        ...
    _getFlowRate_2__T = typing.TypeVar('_getFlowRate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.SpacecraftState) -> float:
        """
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s).
        
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        """
        ...
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, s: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_2__T], parameters: typing.Union[typing.List[_getFlowRate_2__T], jpype.JArray]) -> _getFlowRate_2__T:
        """
        Specified by: getFlowRate in interface ThrustPropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        
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
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], parameters: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current spacecraft state
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N).
        
        Specified by: getThrustVector in interface ThrustPropulsionModel
        
        Parameters:
            s (SpacecraftState): current spacecraft state
            parameters (double[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        """
        ...
    @typing.overload
    def getThrustVector(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Specified by: init in interface PropulsionModel
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class BasicConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel):
    """
    Constant thrust propulsion model with: - Constant thrust direction in spacecraft frame - Parameter drivers (for estimation) for the thrust norm or the flow rate. Note that both parameters CANNOT be selected at the same time since they depend on one another.
    
    Since:
        10.2
    """
    THRUST: typing.ClassVar[str] = ...
    """
    Parameter name for thrust.
    
    Also see:
        constant
    
    
    """
    FLOW_RATE: typing.ClassVar[str] = ...
    """
    Parameter name for flow rate.
    
    Also see:
        constant
    
    
    """
    THRUST_SCALE: typing.ClassVar[float] = ...
    """
    Thrust scaling factor.
    
    We use a power of 2 to avoid numeric noise introduction in the multiplications/divisions sequences.
    """
    FLOW_RATE_SCALE: typing.ClassVar[float] = ...
    """
    Flow rate scaling factor.
    
    We use a power of 2 to avoid numeric noise introduction in the multiplications/divisions sequences.
    """
    @typing.overload
    def __init__(self, thrust: float, isp: float, direction: org.hipparchus.geometry.euclidean.threed.Vector3D, name: str): ...
    @typing.overload
    def __init__(self, thrust: float, isp: float, direction: org.hipparchus.geometry.euclidean.threed.Vector3D, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, name: str): ...
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, date: org.orekit.propagation.SpacecraftState) -> float:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
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
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
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
    def getFlowRate(self, parameters: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_1__T = typing.TypeVar('_getThrustVector_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self, parameters: typing.Union[typing.List[_getThrustVector_1__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_1__T]:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, date: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
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
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Returns:
            thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class PythonAbstractConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel):
    @typing.overload
    def __init__(self, thrust: float, isp: float, direction: org.hipparchus.geometry.euclidean.threed.Vector3D, name: str): ...
    @typing.overload
    def __init__(self, thrust: float, isp: float, direction: org.hipparchus.geometry.euclidean.threed.Vector3D, control3DVectorCostType: org.orekit.forces.maneuvers.Control3DVectorCostType, name: str): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, date: org.orekit.propagation.SpacecraftState) -> float:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
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
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Returns:
            flow rate (kg/s) will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getFlowRate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def getFlowRate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    @typing.overload
    def getFlowRate(self, parameters: typing.Union[typing.List[_getFlowRate_5__T], jpype.JArray]) -> _getFlowRate_5__T:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        
        """
        ...
    @typing.overload
    def getFlowRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getFlowRate_6__T], tArray: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_4__T = typing.TypeVar('_getThrustVector_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, parameters: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Returns:
            thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, date: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from class: getThrustVector Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
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
    def pythonExtension(self, pythonObject: int) -> None: ...

class ScaledConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel):
    """
    Thrust propulsion model with parameters (for estimation) represented by scale factors on the X, Y and Z axis of the spacecraft frame.
    
    Since:
        10.2
    """
    THRUSTX_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    Parameter name for the scale factor on the X component of the thrust in S/C frame.
    
    Also see:
        constant
    
    
    """
    THRUSTY_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    Parameter name for the scale factor on the Y component of the thrust in S/C frame.
    
    Also see:
        constant
    
    
    """
    THRUSTZ_SCALE_FACTOR: typing.ClassVar[str] = ...
    """
    Parameter name for the scale factor on the Z component of the thrust in S/C frame.
    
    Also see:
        constant
    
    
    """
    def __init__(self, thrust: float, isp: float, direction: org.hipparchus.geometry.euclidean.threed.Vector3D, name: str):
        """
        Constructor with min/max deviation for the scale factors. Typical usage is, for example, if you know that your propulsion system usually has an error of less than 10% then set the min/max to respectively 0.9 and 1.1.
        
        Parameters:
            thrust (double): the thrust (N)
            isp (double): the isp (s)
            direction (Vector3D): in spacecraft frame
            name (String): the name of the maneuver
        
        
        """
        ...
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, date: org.orekit.propagation.SpacecraftState) -> float:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
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
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
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
    def getFlowRate(self, parameters: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_1__T = typing.TypeVar('_getThrustVector_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self, parameters: typing.Union[typing.List[_getThrustVector_1__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_1__T]:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, date: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
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
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Returns:
            thrust vector in spacecraft frame (N), will throw an exception if used on driver containing several value spans
        
        """
        ...
    @typing.overload
    def getThrustVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getThrustVector(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class SphericalConstantThrustPropulsionModel(AbstractConstantThrustPropulsionModel):
    """
    Constant thrust propulsion model with: - Constant thrust direction in spacecraft frame - Parameter drivers (for estimation) for the thrust vector in spherical coordinates.
    
    Since:
        13.1
    
    Also see:
        BasicConstantThrustPropulsionModel
    """
    THRUST_MAGNITUDE: typing.ClassVar[str] = ...
    """
    Parameter name for thrust magnitude.
    
    Also see:
        constant
    
    
    """
    THRUST_RIGHT_ASCENSION: typing.ClassVar[str] = ...
    """
    Parameter name for thrust right ascension.
    
    Also see:
        constant
    
    
    """
    THRUST_DECLINATION: typing.ClassVar[str] = ...
    """
    Parameter name for thrust declination.
    
    Also see:
        constant
    
    
    """
    THRUST_SCALE: typing.ClassVar[float] = ...
    """
    Thrust scaling factor.
    
    We use a power of 2 to avoid numeric noise introduction in the multiplications/divisions sequences.
    """
    @typing.overload
    def __init__(self, isp: float, thrustMagnitude: float, thrustDirection: org.hipparchus.geometry.euclidean.threed.Vector3D, name: str): ...
    @typing.overload
    def __init__(self, isp: float, thrustVector: org.hipparchus.geometry.euclidean.threed.Vector3D, name: str): ...
    _getFlowRate_5__T = typing.TypeVar('_getFlowRate_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFlowRate_6__T = typing.TypeVar('_getFlowRate_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFlowRate(self, date: org.orekit.propagation.SpacecraftState) -> float:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            flow rate (kg/s)
        
        Get the flow rate (kg/s). Here it does not depend on current S/C state.
        
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
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
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
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
    def getFlowRate(self, parameters: typing.Union[typing.List[_getFlowRate_6__T], jpype.JArray]) -> _getFlowRate_6__T:
        """
        Specified by: getFlowRate in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            flow rate (kg/s)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _getThrustVector_0__T = typing.TypeVar('_getThrustVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getThrustVector_1__T = typing.TypeVar('_getThrustVector_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getThrustVector(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getThrustVector_0__T], tArray: typing.Union[typing.List[_getThrustVector_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_0__T]: ...
    @typing.overload
    def getThrustVector(self, parameters: typing.Union[typing.List[_getThrustVector_1__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getThrustVector_1__T]:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            parameters (T[]): propulsion model parameters
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        
        """
        ...
    @typing.overload
    def getThrustVector(self, date: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
        Parameters:
            date (AbsoluteDate): date at which the thrust vector wants to be known, often the date parameter will not be important and can be whatever if
                the thrust parameter driver as only value estimated over the all orbit determination interval
        
        Returns:
            thrust vector in spacecraft frame (N)
        
        Get the thrust vector in spacecraft frame (N). Here it does not depend on current S/C state.
        
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
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
        Specified by: getThrustVector in class AbstractConstantThrustPropulsionModel
        
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
    SphericalConstantThrustPropulsionModel: typing.Type[SphericalConstantThrustPropulsionModel]
    ThrustPropulsionModel: typing.Type[ThrustPropulsionModel]
    ThrustVectorProvider: typing.Type[ThrustVectorProvider]
