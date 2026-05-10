
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org
import org.orekit.data
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.conversion.averaging.converters
import org.orekit.propagation.conversion.averaging.elements
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.time
import typing



class AveragedOrbitalState(org.orekit.time.TimeStamped):
    """
    Interface representing averaged orbital elements at a specific instant. Inheritors shall implement a conversion method to transform into an osculating Orbit.
    
    Since:
        12.1
    
    Also see:
        TimeStamped,
        AveragedOrbitalElements
    """
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements:
        """
        Getter for the averaged orbital elements.
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Getter for the reference frame.
        
        Returns:
            frame
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Getter for the central body's gravitational constant.
        
        Returns:
            gravitational constant
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Getter for the averaged orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Getter for the averaged position angle.
        
        Returns:
            position angle type
        
        
        """
        ...
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Convert instance to an osculating orbit.
        
        Returns:
            osculating orbit
        
        
        """
        ...

class AbstractAveragedOrbitalState(AveragedOrbitalState):
    """
    Abstract class representing averaged orbital state. It is used to define the frame and the date.
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalState
    """
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface AveragedOrbitalState
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Getter for the reference frame.
        
        Specified by: getFrame in interface AveragedOrbitalState
        
        Returns:
            frame
        
        
        """
        ...

class PythonAveragedOrbitalState(AveragedOrbitalState):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.conversion.averaging.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements:
        """
        Description copied from interface: getAveragedElements Getter for the averaged orbital elements.
        
        Specified by: getAveragedElements in interface AveragedOrbitalState
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getDate Get the date.
        
        Specified by: getDate in interface AveragedOrbitalState
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Description copied from interface: getFrame Getter for the reference frame.
        
        Specified by: getFrame in interface AveragedOrbitalState
        
        Returns:
            frame
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Description copied from interface: getMu Getter for the central body's gravitational constant.
        
        Specified by: getMu in interface AveragedOrbitalState
        
        Returns:
            gravitational constant
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Description copied from interface: getOrbitType Getter for the averaged orbit type.
        
        Specified by: getOrbitType in interface AveragedOrbitalState
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Description copied from interface: getPositionAngleType Getter for the averaged position angle.
        
        Specified by: getPositionAngleType in interface AveragedOrbitalState
        
        Returns:
            position angle type
        
        
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
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Description copied from interface: toOsculatingOrbit Convert instance to an osculating orbit.
        
        Specified by: toOsculatingOrbit in interface AveragedOrbitalState
        
        Returns:
            osculating orbit
        
        
        """
        ...

class PythonAbstractAveragedOrbitalState(AbstractAveragedOrbitalState):
    def __init__(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame):
        """
        Protected constructor.
        
        Parameters:
            date (AbsoluteDate): epoch
            frame (Frame): reference frame
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.conversion.averaging.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements:
        """
        Description copied from interface: getAveragedElements Getter for the averaged orbital elements.
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Description copied from interface: getMu Getter for the central body's gravitational constant.
        
        Returns:
            gravitational constant
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Description copied from interface: getOrbitType Getter for the averaged orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Description copied from interface: getPositionAngleType Getter for the averaged position angle.
        
        Returns:
            position angle type
        
        
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
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Description copied from interface: toOsculatingOrbit Convert instance to an osculating orbit.
        
        Returns:
            osculating orbit
        
        
        """
        ...

class SGP4OrbitalState(AbstractAveragedOrbitalState):
    """
    Class representing an averaged orbital state as in the TLE-related theory. Note it is the averaged mean motion that is written in a Two-Line Element and that, for now, conversions back and forth to averaged semi-major axis are approximated with the osculating ones.
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalState,
        TLEPropagator
    """
    @typing.overload
    def __init__(self, date: org.orekit.time.AbsoluteDate, elements: org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle): ...
    @typing.overload
    def __init__(self, date: org.orekit.time.AbsoluteDate, elements: org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle, dataContext: org.orekit.data.DataContext): ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle:
        """
        Getter for the averaged orbital elements.
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Getter for the central body's gravitational constant.
        
        Returns:
            gravitational constant
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Getter for the averaged orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Getter for the averaged position angle.
        
        Returns:
            position angle type
        
        
        """
        ...
    @staticmethod
    def of(tle: org.orekit.propagation.analytical.tle.TLE, teme: org.orekit.frames.Frame) -> 'SGP4OrbitalState':
        """
        Static constructor. Input frame is implicitly assumed to be TEME (it is not checked).
        
        Parameters:
            tle (TLE): TLE
            teme (Frame): TEME frame (not checked)
        
        Returns:
            TLE-based averaged orbital state
        
        
        """
        ...
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Convert instance to an osculating orbit.
        
        Returns:
            osculating orbit
        
        
        """
        ...

class BrouwerLyddaneOrbitalState(org.orekit.propagation.conversion.averaging.AbstractHarmonicsBasedOrbitalState):
    """
    Class representing an averaged orbital state as in the Brouwer-Lyddane theory.
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalState,
        BrouwerLyddanePropagator
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, elements: org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle, frame: org.orekit.frames.Frame, harmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): epoch
            elements (AveragedKeplerianWithMeanAngle): averaged orbital elements
            frame (Frame): reference frame
            harmonicsProvider (UnnormalizedSphericalHarmonicsProvider): spherical harmonics provider
        
        
        """
        ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle:
        """
        Getter for the averaged orbital elements.
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Getter for the averaged orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Getter for the averaged position angle.
        
        Returns:
            position angle type
        
        
        """
        ...
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Convert instance to an osculating orbit.
        
        Returns:
            osculating orbit
        
        
        """
        ...

class DSST6X0OrbitalState(org.orekit.propagation.conversion.averaging.AbstractHarmonicsBasedOrbitalState):
    """
    Class representing an averaged orbital state as in the DSST theory using only the first 6 zonal harmonics as perturbations.
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalState,
        DSSTPropagator,
        DSSTZonal
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, elements: org.orekit.propagation.conversion.averaging.elements.AveragedEquinoctialWithMeanAngle, frame: org.orekit.frames.Frame, harmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): epoch
            elements (AveragedEquinoctialWithMeanAngle): averaged orbital elements
            frame (Frame): reference frame
            harmonicsProvider (UnnormalizedSphericalHarmonicsProvider): spherical harmonics provider
        
        
        """
        ...
    @staticmethod
    def createForces(provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider) -> java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]:
        """
        Create collection of fist 6 zonal DSST forces.
        
        Parameters:
            provider (UnnormalizedSphericalHarmonicsProvider): spherical harmonics provider
        
        Returns:
            six first zonal forces
        
        
        """
        ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedEquinoctialWithMeanAngle:
        """
        Getter for the averaged orbital elements.
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Getter for the averaged orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Getter for the averaged position angle.
        
        Returns:
            position angle type
        
        
        """
        ...
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Convert instance to an osculating orbit.
        
        Returns:
            osculating orbit
        
        
        """
        ...

class EcksteinHechlerOrbitalState(org.orekit.propagation.conversion.averaging.AbstractHarmonicsBasedOrbitalState):
    """
    Class representing an averaged orbital state as in the Eckstein-Hechler theory.
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalState,
        EcksteinHechlerPropagator
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, elements: org.orekit.propagation.conversion.averaging.elements.AveragedCircularWithMeanAngle, frame: org.orekit.frames.Frame, harmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider):
        """
        Constructor.
        
        Parameters:
            date (AbsoluteDate): epoch
            elements (AveragedCircularWithMeanAngle): averaged orbital elements
            frame (Frame): reference frame
            harmonicsProvider (UnnormalizedSphericalHarmonicsProvider): spherical harmonics provider
        
        
        """
        ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedCircularWithMeanAngle:
        """
        Getter for the averaged orbital elements.
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Getter for the averaged orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Getter for the averaged position angle.
        
        Returns:
            position angle type
        
        
        """
        ...
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Convert instance to an osculating orbit.
        
        Returns:
            osculating orbit
        
        
        """
        ...

class PythonAbstractHarmonicsBasedOrbitalState(org.orekit.propagation.conversion.averaging.AbstractHarmonicsBasedOrbitalState):
    def __init__(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, harmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider):
        """
        Protected constructor.
        
        Parameters:
            date (AbsoluteDate): epoch
            frame (Frame): reference frame
            harmonicsProvider (UnnormalizedSphericalHarmonicsProvider): spherical harmonics provider
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.conversion.averaging.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements:
        """
        Description copied from interface: getAveragedElements Getter for the averaged orbital elements.
        
        Returns:
            averaged elements
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Description copied from interface: getOrbitType Getter for the averaged orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Description copied from interface: getPositionAngleType Getter for the averaged position angle.
        
        Returns:
            position angle type
        
        
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
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Description copied from interface: toOsculatingOrbit Convert instance to an osculating orbit.
        
        Returns:
            osculating orbit
        
        
        """
        ...

class AbstractHarmonicsBasedOrbitalState: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion.averaging")``.

    AbstractAveragedOrbitalState: typing.Type[AbstractAveragedOrbitalState]
    AbstractHarmonicsBasedOrbitalState: typing.Type[AbstractHarmonicsBasedOrbitalState]
    AveragedOrbitalState: typing.Type[AveragedOrbitalState]
    BrouwerLyddaneOrbitalState: typing.Type[BrouwerLyddaneOrbitalState]
    DSST6X0OrbitalState: typing.Type[DSST6X0OrbitalState]
    EcksteinHechlerOrbitalState: typing.Type[EcksteinHechlerOrbitalState]
    PythonAbstractAveragedOrbitalState: typing.Type[PythonAbstractAveragedOrbitalState]
    PythonAbstractHarmonicsBasedOrbitalState: typing.Type[PythonAbstractHarmonicsBasedOrbitalState]
    PythonAveragedOrbitalState: typing.Type[PythonAveragedOrbitalState]
    SGP4OrbitalState: typing.Type[SGP4OrbitalState]
    converters: org.orekit.propagation.conversion.averaging.converters.__module_protocol__
    elements: org.orekit.propagation.conversion.averaging.elements.__module_protocol__
