
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
import org.orekit.forces.drag
import org.orekit.forces.empirical
import org.orekit.forces.gravity
import org.orekit.forces.inertia
import org.orekit.forces.maneuvers
import org.orekit.forces.radiation
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



class BoxAndSolarArraySpacecraft(org.orekit.forces.radiation.RadiationSensitive, org.orekit.forces.drag.DragSensitive):
    """
    Class representing the features of a classical satellite with a convex body shape.
    
    The body can be either a simple parallelepipedic box aligned with spacecraft axes or a set of panels defined by their area and normal vector. Some panels may be moving to model solar arrays (or antennas that could point anywhere). This should handle accurately most spacecraft shapes. This model does not take cast shadows into account.
    
    The lift component of the drag force can be optionally considered. It should probably only be used for reentry computation, with much denser atmosphere than in regular orbit propagation. The lift component is computed using a ratio of molecules that experience specular reflection instead of diffuse reflection (absorption followed by outgassing at negligible velocity). Without lift (i.e. when the lift ratio is set to 0), drag force is along atmosphere relative velocity. With lift (i.e. when the lift ratio is set to any value between 0 and 1), the drag force depends on both relative velocity direction and panels normal orientation. For a single panel, if the relative velocity is head-on (i.e. aligned with the panel normal), the force will be in the same direction with and without lift, but the magnitude with lift ratio set to 1.0 will be twice the magnitude with lift ratio set to 0.0 (because atmosphere molecules bounces backward at same velocity in case of specular reflection).
    
    Each Panel has its own set of radiation and drag coefficients. In orbit determination context, it would not be possible to estimate each panel individually, therefore getDragParametersDrivers returns a single ParameterDriver representing a GLOBAL_DRAG_FACTOR that applies to all panels drag coefficients and the getRadiationParametersDrivers returns a single ParameterDriver representing a GLOBAL_RADIATION_FACTOR that applies to all panels radiation coefficients.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], double4: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, list: java.util.List['Panel']): ...
    @staticmethod
    def buildBox(xLength: float, yLength: float, zLength: float, drag: float, liftRatio: float, absorption: float, reflection: float) -> java.util.List['Panel']:
        """
        Build the panels of a simple parallelepipedic box.
        
        Parameters:
            xLength (double): length of the body along its X axis (m)
            yLength (double): length of the body along its Y axis (m)
            zLength (double): length of the body along its Z axis (m)
            drag (double): drag coefficient
            liftRatio (double): drag lift ratio (proportion between 0 and 1 of atmosphere modecules that will experience specular reflection when
                hitting spacecraft instead of experiencing diffuse reflection, hence producing lift)
            absorption (double): radiation pressure absorption coefficient (between 0 and 1)
            reflection (double): radiation pressure specular reflection coefficient (between 0 and 1)
        
        Returns:
            surface vectors array
        
        Since:
            12.0
        
        
        """
        ...
    @staticmethod
    def buildPanels(xLength: float, yLength: float, zLength: float, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], solarArrayArea: float, solarArrayAxis: org.hipparchus.geometry.euclidean.threed.Vector3D, drag: float, liftRatio: float, absorption: float, reflection: float) -> java.util.List['Panel']:
        """
        Build the panels of a simple parallelepiped box plus one solar array panel.
        
        Parameters:
            xLength (double): length of the body along its X axis (m)
            yLength (double): length of the body along its Y axis (m)
            zLength (double): length of the body along its Z axis (m)
            sun (ExtendedPositionProvider): sun model
            solarArrayArea (double): area of the solar array (m²)
            solarArrayAxis (Vector3D): solar array rotation axis in satellite frame
            drag (double): drag coefficient
            liftRatio (double): drag lift ratio (proportion between 0 and 1 of atmosphere modecules that will experience specular reflection when
                hitting spacecraft instead of experiencing diffuse reflection, hence producing lift)
            absorption (double): radiation pressure absorption coefficient (between 0 and 1)
            reflection (double): radiation pressure specular reflection coefficient (between 0 and 1)
        
        Returns:
            surface vectors array
        
        Since:
            12.0
        
        
        """
        ...
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_dragAcceleration_0__T], density: _dragAcceleration_0__T, relativeVelocity: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], parameters: typing.Union[typing.List[_dragAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Specified by: dragAcceleration in interface DragSensitive
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            density (T): atmospheric density at spacecraft position
            relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.SpacecraftState, density: float, relativeVelocity: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Specified by: dragAcceleration in interface DragSensitive
        
        Parameters:
            state (SpacecraftState): current state
            density (double): atmospheric density at spacecraft position
            relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Specified by: getDragParametersDrivers in interface DragSensitive
        
        Returns:
            parameters drivers
        
        
        """
        ...
    def getPanels(self) -> java.util.List['Panel']:
        """
        Get the panels composing the body.
        
        Returns:
            unmodifiable view of the panels composing the body
        
        Since:
            12.0
        
        
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
        
        This method implements equation 8-44 from David A. Vallado's Fundamentals of Astrodynamics and Applications, third edition, 2007, Microcosm Press.
        
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

class ForceModel(org.orekit.utils.ParameterDriversProvider, org.orekit.propagation.events.EventDetectorsProvider):
    """
    This interface represents a force modifying spacecraft motion.
    
    Objects implementing this interface are intended to be added to a NumericalPropagator before the propagation is started.
    
    The propagator will call at each step the addContribution method. The force model instance will extract all the state data it needs (date, position, velocity, frame, attitude, mass) from the first parameter. From these state data, it will compute the perturbing acceleration. It will then add this acceleration to the second parameter which will take thins contribution into account and will use the Gauss equations to evaluate its impact on the global state derivative.
    
    Force models which create discontinuous acceleration patterns (typically for maneuvers start/stop or solar eclipses entry/exit) must provide one or more EventDetector to the propagator thanks to their getEventDetectors method. This method is called once just before propagation starts. The events states will be checked by the propagator to ensure accurate propagation and proper events handling.
    """
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
        
        Since:
            9.0
        
        
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
        
        Since:
            9.0
        
        """
        ...
    _addContribution_0__T = typing.TypeVar('_addContribution_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addContribution(self, s: org.orekit.propagation.FieldSpacecraftState[_addContribution_0__T], adder: org.orekit.propagation.numerical.FieldTimeDerivativesEquations[_addContribution_0__T]) -> None:
        """
        Compute the contribution of the force model to the perturbing acceleration.
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            adder (FieldTimeDerivativesEquations<T> adder): object where the contribution should be added
        
        
        """
        ...
    @typing.overload
    def addContribution(self, s: org.orekit.propagation.SpacecraftState, adder: org.orekit.propagation.numerical.TimeDerivativesEquations) -> None:
        """
        Compute the contribution of the force model to the perturbing acceleration.
        
        The default implementation simply adds the acceleration as a non-Keplerian acceleration.
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            adder (TimeDerivativesEquations): object where the contribution should be added
        
        """
        ...
    def dependsOnAttitudeRate(self) -> bool:
        """
        Check if force model depends on attitude's rotation rate or acceleration at a given, fixed date. If false, it essentially means that at most the attitude's rotation is used when computing the acceleration vector. The default implementation returns false as common forces do not.
        
        Returns:
            true if force model depends on attitude derivatives
        
        Since:
            12.1
        
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
        Check if force model depends on position only at a given, fixed date.
        
        Returns:
            true if force model depends on position only, false if it depends on mass or velocity, either directly or due to a
            dependency on attitude
        
        Since:
            9.0
        
        
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
    _getMassDerivative_1__T = typing.TypeVar('_getMassDerivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivative(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the mass rate. Zero by default.
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date
        
        Returns:
            mass rate (kg/s)
        
        Since:
            13.1
        
        """
        ...
    @typing.overload
    def getMassDerivative(self, state: org.orekit.propagation.FieldSpacecraftState[_getMassDerivative_1__T], parameters: typing.Union[typing.List[_getMassDerivative_1__T], jpype.JArray]) -> _getMassDerivative_1__T:
        """
        Compute the mass rate. Zero by default.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date
        
        Returns:
            mass rate (kg/s)
        
        Since:
            13.1
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Initialize the force model at the start of propagation. This method will be called before any calls to addContribution, addContribution, acceleration or acceleration
        
        The default implementation of this method does nothing.
        
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
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...

class Panel:
    """
    Base class representing one panel of a satellite.
    
    Since:
        3.0
    
    Also see:
        FixedPanel, PointingPanel,
        SlewingPanel
    """
    def getAbsorption(self) -> float:
        """
        Get radiation pressure absorption coefficient.
        
        Returns:
            radiation pressure absorption coefficient
        
        
        """
        ...
    def getArea(self) -> float:
        """
        Get panel area.
        
        Returns:
            panel area
        
        
        """
        ...
    def getDrag(self) -> float:
        """
        Get drag coefficient.
        
        Returns:
            drag coefficient
        
        
        """
        ...
    def getLiftRatio(self) -> float:
        """
        Get drag lift ratio.
        
        Returns:
            drag lift ratio
        
        
        """
        ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]: ...
    @typing.overload
    def getNormal(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get panel normal in spacecraft frame.
        
        Parameters:
            state (SpacecraftState): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        public abstract <T extends CalculusFieldElement<T>> FieldVector3D<T> getNormal (FieldSpacecraftState<T> state)
        
        Get panel normal in spacecraft frame.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        
        """
        ...
    def getReflection(self) -> float:
        """
        Get radiation pressure specular reflection coefficient.
        
        Returns:
            radiation pressure specular reflection coefficient
        
        
        """
        ...
    def isDoubleSided(self) -> bool:
        """
        Check if the panel is double-sided (typically solar arrays).
        
        Returns:
            true if panel is double-sided
        
        
        """
        ...

class FixedPanel(Panel):
    """
    Class representing one panel of a satellite, fixed with respect to satellite body.
    
    It is mainly used to represent one facet of the body of the satellite.
    
    Since:
        3.0
    """
    def __init__(self, normal: org.hipparchus.geometry.euclidean.threed.Vector3D, area: float, doubleSided: bool, drag: float, liftRatio: float, absorption: float, reflection: float):
        """
        Simple constructor.
        
        As the sum of absorption coefficient, specular reflection coefficient and diffuse reflection coefficient is exactly 1, only the first two coefficients are needed here, the third one is deduced from the other ones.
        
        Parameters:
            normal (Vector3D): vector normal to the panel in spacecraft frame, pointing outward (will be normalized)
            area (double): panel area in m²
            doubleSided (boolean): if true, the panel is double-sided (typically solar arrays), otherwise it is the side of a box and only relevant for
                flux coming from its positive normal
            drag (double): drag coefficient
            liftRatio (double): drag lift ratio (proportion between 0 and 1 of atmosphere modecules that will experience specular reflection when
                hitting spacecraft instead of experiencing diffuse reflection, hence producing lift)
            absorption (double): radiation pressure absorption coefficient (between 0 and 1)
            reflection (double): radiation pressure specular reflection coefficient (between 0 and 1)
        
        
        """
        ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, state: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]:
        """
        Get panel normal in spacecraft frame.
        
        Specified by: getNormal in class Panel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        
        """
        ...
    @typing.overload
    def getNormal(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get panel normal in spacecraft frame.
        
        Specified by: getNormal in class Panel
        
        Parameters:
            state (SpacecraftState): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        """
        ...

class ForceModelModifier(ForceModel):
    """
    Interface to wrap another force model. By default, methods do not modify anything.
    
    Since:
        13.0
    """
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
    def dependsOnAttitudeRate(self) -> bool:
        """
        Check if force model depends on attitude's rotation rate or acceleration at a given, fixed date. If false, it essentially means that at most the attitude's rotation is used when computing the acceleration vector. The default implementation returns false as common forces do not.
        
        Specified by: dependsOnAttitudeRate in interface ForceModel
        
        Returns:
            true if force model depends on attitude derivatives
        
        
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getUnderlyingModel(self) -> ForceModel:
        """
        Get the underlying force model.
        
        Returns:
            underlying model
        
        
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

class PointingPanel(Panel):
    """
    Class representing one panel of a satellite, roughly pointing towards some target.
    
    It is mainly used to represent a rotating solar array that points towards the Sun.
    
    The panel rotation with respect to satellite body is the best pointing orientation achievable when the rotation axix is fixed by body attitude. Target is therefore always exactly in meridian plane defined by rotation axis and panel normal vector.
    
    These panels are considered to be always isDoubleSided.
    
    Since:
        3.0
    """
    def __init__(self, rotationAxis: org.hipparchus.geometry.euclidean.threed.Vector3D, target: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], area: float, drag: float, liftRatio: float, absorption: float, reflection: float):
        """
        Simple constructor.
        
        As the sum of absorption coefficient, specular reflection coefficient and diffuse reflection coefficient is exactly 1, only the first two coefficients are needed here, the third one is deduced from the other ones.
        
        The panel is considered to rotate about one axis in order to make its normal point as close as possible to the target. It means the target will always be in the plane defined by the rotation axis and the panel normal.
        
        Parameters:
            rotationAxis (Vector3D): rotation axis of the panel
            target (ExtendedPositionProvider): target towards which the panel will point (the Sun for a solar array)
            area (double): panel area in m²
            drag (double): drag coefficient
            liftRatio (double): drag lift ratio (proportion between 0 and 1 of atmosphere modecules that will experience specular reflection when
                hitting spacecraft instead of experiencing diffuse reflection, hence producing lift)
            absorption (double): radiation pressure absorption coefficient (between 0 and 1)
            reflection (double): radiation pressure specular reflection coefficient (between 0 and 1)
        
        
        """
        ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, state: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]:
        """
        Get panel normal in spacecraft frame.
        
        Specified by: getNormal in class Panel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        
        """
        ...
    @typing.overload
    def getNormal(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get panel normal in spacecraft frame.
        
        Specified by: getNormal in class Panel
        
        Parameters:
            state (SpacecraftState): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        """
        ...

class PythonForceModel(ForceModel):
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
    _addContribution_0__T = typing.TypeVar('_addContribution_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addContribution(self, s: org.orekit.propagation.FieldSpacecraftState[_addContribution_0__T], adder: org.orekit.propagation.numerical.FieldTimeDerivativesEquations[_addContribution_0__T]) -> None:
        """
        Compute the contribution of the force model to the perturbing acceleration.
        
        Specified by: addContribution in interface ForceModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            adder (FieldTimeDerivativesEquations<T> adder): object where the contribution should be added
        
        
        """
        ...
    @typing.overload
    def addContribution(self, s: org.orekit.propagation.SpacecraftState, adder: org.orekit.propagation.numerical.TimeDerivativesEquations) -> None:
        """
        Compute the contribution of the force model to the perturbing acceleration.
        
        The default implementation simply adds the acceleration as a non-Keplerian acceleration.
        
        Specified by: addContribution in interface ForceModel
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            adder (TimeDerivativesEquations): object where the contribution should be added
        
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
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getMassDerivative_1__T = typing.TypeVar('_getMassDerivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMassDerivative(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the mass rate. Zero by default.
        
        Specified by: getMassDerivative in interface ForceModel
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date
        
        Returns:
            mass rate (kg/s)
        
        """
        ...
    @typing.overload
    def getMassDerivative(self, s: org.orekit.propagation.FieldSpacecraftState[_getMassDerivative_1__T], parameters: typing.Union[typing.List[_getMassDerivative_1__T], jpype.JArray]) -> _getMassDerivative_1__T:
        """
        Compute the mass rate. Zero by default.
        
        Specified by: getMassDerivative in interface ForceModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date
        
        Returns:
            mass rate (kg/s)
        
        
        """
        ...
    def getParameterDriver(self, name: str) -> org.orekit.utils.ParameterDriver:
        """
        Get parameter value from its name.
        
        Specified by: getParameterDriver in interface ParameterDriversProvider
        
        Parameters:
            name (String): parameter name
        
        Returns:
            parameter value
        
        
        """
        ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getParameters_3__T = typing.TypeVar('_getParameters_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getParameters_1__T]) -> typing.MutableSequence[_getParameters_1__T]: ...
    @typing.overload
    def getParameters(self) -> typing.MutableSequence[float]:
        """
        Get model parameters.
        
        Specified by: getParameters in interface ParameterDriversProvider
        
        Returns:
            model parameters, will throw an exception if one PDriver has several values driven. If it's the case (if at least 1
            PDriver of the model has several values driven) the method
            getParameters must be used.
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_3__T]) -> typing.MutableSequence[_getParameters_3__T]:
        """
        Get model parameters.
        
        Specified by: getParameters in interface ParameterDriversProvider
        
        Parameters:
            field (Field<T> field): field to which the elements belong
        
        Returns:
            model parameters, will throw an exception if one PDriver of the has several values driven. If it's the case (if at least
            1 PDriver of the model has several values driven) the method
            getParameters must be used.
        
        
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
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
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
    def isSupported(self, name: str) -> bool:
        """
        Check if a parameter is supported.
        
        Supported parameters are those listed by getParametersDrivers.
        
        Specified by: isSupported in interface ParameterDriversProvider
        
        Parameters:
            name (String): parameter name to check
        
        Returns:
            true if the parameter is supported
        
        Also see:
            getParametersDrivers
        
        
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

class SlewingPanel(Panel):
    """
    Class representing one panel of a satellite, slewing about an axis at constant rate.
    
    It is mainly used to represent a solar array with fixed rate rotation.
    
    The panel rotation evolves linearly according to a start position and an angular rate (which can be set to 0 for non-rotating panels, which may occur in special modes or during contingencies).
    
    These panels are considered to be always isDoubleSided.
    
    Since:
        3.0
    """
    def __init__(self, rotationAxis: org.hipparchus.geometry.euclidean.threed.Vector3D, rotationRate: float, referenceDate: org.orekit.time.AbsoluteDate, referenceNormal: org.hipparchus.geometry.euclidean.threed.Vector3D, area: float, drag: float, liftRatio: float, absorption: float, reflection: float):
        """
        Simple constructor.
        
        As the sum of absorption coefficient, specular reflection coefficient and diffuse reflection coefficient is exactly 1, only the first two coefficients are needed here, the third one is deduced from the other ones.
        
        The panel is considered to rotate about one axis in order to make its normal point as close as possible to the target. It means the target will always be in the plane defined by the rotation axis and the panel normal.
        
        Parameters:
            rotationAxis (Vector3D): rotation axis of the panel
            rotationRate (double): rotation rate of the panel (rad/s)
            referenceDate (AbsoluteDate): reference date for the panel rotation
            referenceNormal (Vector3D): direction of the panel normal at reference date in spacecraft frame
            area (double): panel area in m²
            drag (double): drag coefficient
            liftRatio (double): drag lift ratio (proportion between 0 and 1 of atmosphere modecules that will experience specular reflection when
                hitting spacecraft instead of experiencing diffuse reflection, hence producing lift)
            absorption (double): radiation pressure absorption coefficient (between 0 and 1)
            reflection (double): radiation pressure specular reflection coefficient (between 0 and 1)
        
        
        """
        ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, state: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]:
        """
        Get panel normal in spacecraft frame.
        
        Specified by: getNormal in class Panel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        
        """
        ...
    @typing.overload
    def getNormal(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get panel normal in spacecraft frame.
        
        Specified by: getNormal in class Panel
        
        Parameters:
            state (SpacecraftState): current spacecraft state
        
        Returns:
            panel normal in spacecraft frame
        
        """
        ...

class PythonForceModelModifier(ForceModelModifier):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getUnderlyingModel(self) -> ForceModel:
        """
        Get the underlying force model.
        
        Specified by: getUnderlyingModel in interface ForceModelModifier
        
        Returns:
            underlying model
        
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces")``.

    BoxAndSolarArraySpacecraft: typing.Type[BoxAndSolarArraySpacecraft]
    FixedPanel: typing.Type[FixedPanel]
    ForceModel: typing.Type[ForceModel]
    ForceModelModifier: typing.Type[ForceModelModifier]
    Panel: typing.Type[Panel]
    PointingPanel: typing.Type[PointingPanel]
    PythonForceModel: typing.Type[PythonForceModel]
    PythonForceModelModifier: typing.Type[PythonForceModelModifier]
    SlewingPanel: typing.Type[SlewingPanel]
    drag: org.orekit.forces.drag.__module_protocol__
    empirical: org.orekit.forces.empirical.__module_protocol__
    gravity: org.orekit.forces.gravity.__module_protocol__
    inertia: org.orekit.forces.inertia.__module_protocol__
    maneuvers: org.orekit.forces.maneuvers.__module_protocol__
    radiation: org.orekit.forces.radiation.__module_protocol__
