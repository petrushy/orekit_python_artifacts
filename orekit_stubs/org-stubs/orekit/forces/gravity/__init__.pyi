
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.forces
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



class AbstractBodyAttraction(org.orekit.forces.ForceModel):
    """
    Abstract class for non-central body attraction force model.
    """
    ATTRACTION_COEFFICIENT_SUFFIX: typing.ClassVar[str] = ...
    """
    Suffix for parameter name for attraction coefficient enabling Jacobian processing.
    
    Also see:
        constant
    
    
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
    def getBodyName(self) -> str:
        """
        Getter for the body's name.
        
        Returns:
            the body's name
        
        
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

class DeSitterRelativity(org.orekit.forces.ForceModel):
    """
    De Sitter post-Newtonian correction force due to general relativity.
    
    De Sitter term causes a precession of the orbital plane at a rate of 19 mas per year.
    
    Since:
        10.3
    
    Also see:
        "Petit, G. and Luzum, B. (eds.), IERS Conventions (2010), Chapter 10, General relativistic models for space-time
        coordinates and equations of motion (2010)"
    """
    ATTRACTION_COEFFICIENT_SUFFIX: typing.ClassVar[str] = ...
    """
    Suffix for parameter name for attraction coefficient enabling Jacobian processing.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody, celestialBody2: org.orekit.bodies.CelestialBody): ...
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
    def dependsOnPositionOnly(self) -> bool:
        """
        Check if force model depends on position only at a given, fixed date.
        
        Specified by: dependsOnPositionOnly in interface ForceModel
        
        Returns:
            true if force model depends on position only, false if it depends on mass or velocity, either directly or due to a
            dependency on attitude
        
        
        """
        ...
    def getEarth(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Get the Earth model used to compute De Sitter effect.
        
        Returns:
            the earth model
        
        
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
    def getSun(self) -> org.orekit.bodies.CelestialBody:
        """
        Get the sun model used to compute De Sitter effect.
        
        Returns:
            the sun model
        
        
        """
        ...

class HolmesFeatherstoneAttractionModel(org.orekit.forces.ForceModel, org.orekit.forces.gravity.potential.TideSystemProvider):
    """
    This class represents the gravitational field of a celestial body.
    
    The algorithm implemented in this class has been designed by S. A. Holmes and W. E. Featherstone from Department of Spatial Sciences, Curtin University of Technology, Perth, Australia. It is described in their 2002 paper: 226460594_A_unified_approach_to_the_Clenshaw_summation_and_the_recursive_computation_of_very_high_degree_and_order_normalised_associated_Legendre_functions (Journal of Geodesy (2002) 76: 279–299).
    
    This model directly uses normalized coefficients and stable recursion algorithms so it is more suited to high degree gravity fields than the classical Cunningham Droziner models which use un-normalized coefficients.
    
    Among the different algorithms presented in Holmes and Featherstone paper, this class implements the modified forward row method. All recursion coefficients are precomputed and stored for greater performance. This caching was suggested in the paper but not used due to the large memory requirements. Since 2002, even low end computers and mobile devices do have sufficient memory so this caching has become feasible nowadays.
    
    Since:
        6.0
    """
    def __init__(self, centralBodyFrame: org.orekit.frames.Frame, provider: org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider):
        """
        Creates a new instance.
        
        Parameters:
            centralBodyFrame (Frame): rotating body frame
            provider (NormalizedSphericalHarmonicsProvider): provider for spherical harmonics
        
        Since:
            6.0
        
        
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
    def getMu(self) -> float:
        """
        Get the central attraction coefficient μ.
        
        Returns:
            mu central attraction coefficient (m³/s²), will throw an exception if gm PDriver has several values driven (in this
            case the method getMu must be used.
        
        """
        ...
    @typing.overload
    def getMu(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the central attraction coefficient μ.
        
        Parameters:
            date (AbsoluteDate): date at which mu wants to be known
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        
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
    def getTideSystem(self) -> org.orekit.forces.gravity.potential.TideSystem:
        """
        Get the TideSystem used in the gravity field.
        
        Specified by: getTideSystem in interface TideSystemProvider
        
        Returns:
            tide system used in the gravity field
        
        
        """
        ...
    _gradient_1__T = typing.TypeVar('_gradient_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def gradient(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, mu: float) -> typing.MutableSequence[float]:
        """
        Compute the gradient of the non-central part of the gravity field.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): position at which gravity field is desired in body frame
            mu (double): central attraction coefficient to use
        
        Returns:
            gradient of the non-central part of the gravity field
        
        """
        ...
    @typing.overload
    def gradient(self, date: org.orekit.time.FieldAbsoluteDate[_gradient_1__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_gradient_1__T], mu: _gradient_1__T) -> typing.MutableSequence[_gradient_1__T]:
        """
        Compute the gradient of the non-central part of the gravity field.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): position at which gravity field is desired in body frame
            mu (T): central attraction coefficient to use
        
        Returns:
            gradient of the non-central part of the gravity field
        
        
        """
        ...
    def nonCentralPart(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, mu: float) -> float:
        """
        Compute the non-central part of the gravity field.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): position at which gravity field is desired in body frame
            mu (double): central attraction coefficient to use
        
        Returns:
            value of the non-central part of the gravity field
        
        
        """
        ...
    def value(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, mu: float) -> float:
        """
        Compute the value of the gravity field.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): position at which gravity field is desired in body frame
            mu (double): central attraction coefficient to use
        
        Returns:
            value of the gravity field (central and non-central parts summed together)
        
        
        """
        ...

class J2OnlyPerturbation(org.orekit.forces.ForceModel):
    """
    J2-only force model. This class models the oblateness part alone of the central body's potential (degree 2 and order 0), whilst avoiding the computational overhead of generic NxM spherical harmonics.
    
    This J2 coefficient has same magnitude and opposite sign than the so-called unnormalized C20 coefficient.
    
    This class should not be used in combination of HolmesFeatherstoneAttractionModel, otherwise the J2 term would be taken into account twice.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, double: float, double2: float, timeScalarFunction: org.orekit.time.TimeScalarFunction, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, frame: org.orekit.frames.Frame): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    _computeAccelerationInJ2Frame_0__T = typing.TypeVar('_computeAccelerationInJ2Frame_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeAccelerationInJ2Frame(positionInJ2Frame: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeAccelerationInJ2Frame_0__T], mu: float, rEq: float, j2: _computeAccelerationInJ2Frame_0__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_computeAccelerationInJ2Frame_0__T]:
        """
        Compute acceleration in J2 frame. Field version.
        
        Parameters:
            positionInJ2Frame (FieldVector3D<T> positionInJ2Frame): position in J2 frame@
            mu (double): gravitational parameter
            rEq (double): equatorial radius
            j2 (T): J2 coefficient
        
        Returns:
            acceleration in J2 frame
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeAccelerationInJ2Frame(positionInJ2Frame: org.hipparchus.geometry.euclidean.threed.Vector3D, mu: float, rEq: float, j2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration in J2 frame.
        
        Parameters:
            positionInJ2Frame (Vector3D): position in J2 frame@
            mu (double): gravitational parameter
            rEq (double): equatorial radius
            j2 (double): J2 coefficient
        
        Returns:
            acceleration in J2 frame
        
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
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Getter for frame.
        
        Returns:
            frame
        
        
        """
        ...
    _getJ2_1__T = typing.TypeVar('_getJ2_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getJ2(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Return J2 at requested date.
        
        Parameters:
            date (AbsoluteDate): epoch at which J2 coefficient should be retrieved
        
        Returns:
            J2 coefficient
        
        """
        ...
    @typing.overload
    def getJ2(self, date: org.orekit.time.FieldAbsoluteDate[_getJ2_1__T]) -> _getJ2_1__T:
        """
        Parameters:
            date (FieldAbsoluteDate<T> date): epoch at which J2 coefficient should be retrieved
        
        Returns:
            J2 coefficient
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Getter for mu.
        
        Returns:
            mu
        
        
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
    def getrEq(self) -> float:
        """
        Getter for equatorial radius.
        
        Returns:
            equatorial radius
        
        
        """
        ...

class LenseThirringRelativity(org.orekit.forces.ForceModel):
    """
    Lense-Thirring post-Newtonian correction force due to general relativity.
    
    Lense-Thirring term causes a precession of the orbital plane at a rate of the order of 0.8 mas per year (geostationary) to 180 mas per year (low orbit).
    
    Since:
        10.3
    
    Also see:
        "Petit, G. and Luzum, B. (eds.), IERS Conventions (2010), Chapter 10, General relativistic models for space-time
        coordinates and equations of motion (2010)"
    """
    def __init__(self, gm: float, bodyFrame: org.orekit.frames.Frame):
        """
        Constructor.
        
        Parameters:
            gm (double): Earth's gravitational parameter.
            bodyFrame (Frame): central body frame
        
        
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

class NewtonianAttraction(org.orekit.forces.ForceModel):
    """
    Force model for Newtonian central body attraction.
    """
    CENTRAL_ATTRACTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    Name of the single parameter of this model: the central attraction coefficient.
    
    Also see:
        constant
    
    
    """
    def __init__(self, mu: float):
        """
        Simple constructor.
        
        Parameters:
            mu (double): central attraction coefficient (m^3/s^2)
        
        
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
    _getMu_1__T = typing.TypeVar('_getMu_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMu(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the central attraction coefficient μ.
        
        Parameters:
            date (AbsoluteDate): date at which the mu value wants to be known
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        """
        ...
    @typing.overload
    def getMu(self, field: org.hipparchus.Field[_getMu_1__T], date: org.orekit.time.FieldAbsoluteDate[_getMu_1__T]) -> _getMu_1__T:
        """
        Get the central attraction coefficient μ.
        
        Parameters:
            field (Field<T> field): field to which the state belongs
            date (FieldAbsoluteDate<T> date): date at which the mu value wants to be known
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        
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

class OceanTides(org.orekit.forces.ForceModelModifier):
    """
    Ocean tides force model.
    
    Since:
        6.1
    """
    DEFAULT_STEP: typing.ClassVar[float] = ...
    """
    Default step for tides field sampling (seconds).
    
    Also see:
        constant
    
    
    """
    DEFAULT_POINTS: typing.ClassVar[int] = ...
    """
    Default number of points tides field sampling.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, double: float, double2: float, boolean: bool, double3: float, int: int, int2: int, int3: int, iERSConventions: org.orekit.utils.IERSConventions, uT1Scale: org.orekit.time.UT1Scale): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, double: float, double2: float, boolean: bool, double3: float, int: int, int2: int, int3: int, iERSConventions: org.orekit.utils.IERSConventions, uT1Scale: org.orekit.time.UT1Scale, gravityFields: org.orekit.forces.gravity.potential.GravityFields): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, double: float, double2: float, int: int, int2: int, iERSConventions: org.orekit.utils.IERSConventions, uT1Scale: org.orekit.time.UT1Scale): ...
    def getUnderlyingModel(self) -> org.orekit.forces.ForceModel:
        """
        Description copied from interface: getUnderlyingModel Get the underlying force model.
        
        Specified by: getUnderlyingModel in interface ForceModelModifier
        
        Returns:
            underlying model
        
        
        """
        ...

class Relativity(org.orekit.forces.ForceModel):
    """
    Post-Newtonian correction force due to general relativity. The main effect is the precession of perigee by a few arcseconds per year.
    
    Implemented from Montenbruck and Gill equation 3.146.
    
    Also see:
        "Montenbruck, Oliver, and Gill, Eberhard. Satellite orbits : models, methods, and applications. Berlin New York:
        Springer, 2000."
    """
    def __init__(self, gm: float):
        """
        Create a force model to add post-Newtonian acceleration corrections to an Earth orbit.
        
        Parameters:
            gm (double): Earth's gravitational parameter.
        
        
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

class SolidTides(org.orekit.forces.ForceModelModifier):
    """
    Solid tides force model.
    
    Since:
        6.1
    """
    DEFAULT_STEP: typing.ClassVar[float] = ...
    """
    Default step for tides field sampling (seconds).
    
    Also see:
        constant
    
    
    """
    DEFAULT_POINTS: typing.ClassVar[int] = ...
    """
    Default number of points tides field sampling.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, double: float, double2: float, tideSystem: org.orekit.forces.gravity.potential.TideSystem, boolean: bool, double3: float, int: int, iERSConventions: org.orekit.utils.IERSConventions, uT1Scale: org.orekit.time.UT1Scale, *celestialBody: org.orekit.bodies.CelestialBody): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, double: float, double2: float, tideSystem: org.orekit.forces.gravity.potential.TideSystem, iERSConventions: org.orekit.utils.IERSConventions, uT1Scale: org.orekit.time.UT1Scale, *celestialBody: org.orekit.bodies.CelestialBody): ...
    def getUnderlyingModel(self) -> org.orekit.forces.ForceModel:
        """
        Description copied from interface: getUnderlyingModel Get the underlying force model.
        
        Specified by: getUnderlyingModel in interface ForceModelModifier
        
        Returns:
            underlying model
        
        
        """
        ...

class SingleBodyAbsoluteAttraction(AbstractBodyAttraction):
    """
    Body attraction force model computed as absolute acceleration towards a body.
    
    This force model represents the same physical principles as NewtonianAttraction, but has several major differences:
    
      - the attracting body can be away from the integration frame center,
      - several instances of this force model can be added when several bodies are involved,
      - this force model is never automatically added by the numerical propagator
    
    The possibility for the attracting body to be away from the frame center allows to use this force model when integrating for example an interplanetary trajectory propagated in an Earth centered frame (in which case an instance of InertialForces must also be added to take into account the coupling effect of relative frames motion).
    
    The possibility to add several instances allows to use this in interplanetary trajectories or in trajectories about Lagrangian points
    
    The fact this force model is never automatically added by the numerical propagator differs from NewtonianAttraction as NewtonianAttraction may be added automatically when propagating a trajectory represented as an Orbit, which must always refer to a central body, if user did not add the NewtonianAttraction or set the central attraction coefficient by himself.
    
    Also see:
        InertialForces
    """
    @typing.overload
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], string: str, double: float): ...
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

class SingleBodyRelativeAttraction(AbstractBodyAttraction):
    """
    Body attraction force model computed as relative acceleration towards frame center.
    """
    @typing.overload
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], string: str, double: float): ...
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

class ThirdBodyAttraction(AbstractBodyAttraction):
    """
    Third body attraction force model.
    """
    @typing.overload
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], string: str, double: float): ...
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

class ThirdBodyAttractionEpoch(ThirdBodyAttraction):
    """
    Third body attraction force model. This class is a copy of ThirdBodyAttraction class. The computation of derivatives of the acceleration w.r.t. the Epoch has been added.
    
    Since:
        10.2
    """
    def __init__(self, body: org.orekit.bodies.CelestialBody):
        """
        Simple constructor.
        
        Parameters:
            body (CelestialBody): the third body to consider (ex: getSun or
                getMoon)
        
        
        """
        ...
    def getDerivativesToEpoch(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Compute derivatives of the state w.r.t epoch.
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters
        
        Returns:
            derivatives
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.gravity")``.

    AbstractBodyAttraction: typing.Type[AbstractBodyAttraction]
    DeSitterRelativity: typing.Type[DeSitterRelativity]
    HolmesFeatherstoneAttractionModel: typing.Type[HolmesFeatherstoneAttractionModel]
    J2OnlyPerturbation: typing.Type[J2OnlyPerturbation]
    LenseThirringRelativity: typing.Type[LenseThirringRelativity]
    NewtonianAttraction: typing.Type[NewtonianAttraction]
    OceanTides: typing.Type[OceanTides]
    Relativity: typing.Type[Relativity]
    SingleBodyAbsoluteAttraction: typing.Type[SingleBodyAbsoluteAttraction]
    SingleBodyRelativeAttraction: typing.Type[SingleBodyRelativeAttraction]
    SolidTides: typing.Type[SolidTides]
    ThirdBodyAttraction: typing.Type[ThirdBodyAttraction]
    ThirdBodyAttractionEpoch: typing.Type[ThirdBodyAttractionEpoch]
    potential: org.orekit.forces.gravity.potential.__module_protocol__
