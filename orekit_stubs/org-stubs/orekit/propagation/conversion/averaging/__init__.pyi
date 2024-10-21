import java.util
import org
import org.orekit.data
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.conversion.averaging.class-use
import org.orekit.propagation.conversion.averaging.converters
import org.orekit.propagation.conversion.averaging.elements
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.time
import typing



class AveragedOrbitalState(org.orekit.time.TimeStamped):
    """
    public interface AveragedOrbitalState extends :class:`~org.orekit.time.TimeStamped`
    
        Interface representing averaged orbital elements at a specific instant. Inheritors shall implement a conversion method
        to transform into an osculating :class:`~org.orekit.orbits.Orbit`.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.time.TimeStamped`,
            :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
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
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
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
    public abstract class AbstractAveragedOrbitalState extends :class:`~org.orekit.propagation.conversion.averaging.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`
    
        Abstract class representing averaged orbital state. It is used to define the frame and the date.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`
    """
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState.getDate` in
                interface :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Getter for the reference frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState.getFrame` in
                interface :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`
        
            Returns:
                frame
        
        
        """
        ...

class PythonAbstractAveragedOrbitalState(AbstractAveragedOrbitalState):
    """
    public class PythonAbstractAveragedOrbitalState extends :class:`~org.orekit.propagation.conversion.averaging.AbstractAveragedOrbitalState`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame): ...
    def finalize(self) -> None: ...
    def getAveragedElements(self) -> org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState.getAveragedElements`
            Getter for the averaged orbital elements.
        
            Returns:
                averaged elements
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState.getMu`
            Getter for the central body's gravitational constant.
        
            Returns:
                gravitational constant
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState.getOrbitType`
            Getter for the averaged orbit type.
        
            Returns:
                orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState.getPositionAngleType`
            Getter for the averaged position angle.
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...
    def toOsculatingOrbit(self) -> org.orekit.orbits.Orbit:
        """
            Description copied from
            interface: :meth:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState.toOsculatingOrbit`
            Convert instance to an osculating orbit.
        
            Returns:
                osculating orbit
        
        
        """
        ...

class SGP4OrbitalState(AbstractAveragedOrbitalState):
    """
    public class SGP4OrbitalState extends :class:`~org.orekit.propagation.conversion.averaging.AbstractAveragedOrbitalState`
    
        Class representing an averaged orbital state as in the TLE-related theory. Note it is the averaged mean motion that is
        written in a Two-Line Element and that, for now, conversions back and forth to averaged semi-major axis are approximated
        with the osculating ones.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`,
            :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, averagedKeplerianWithMeanAngle: org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, averagedKeplerianWithMeanAngle: org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle, dataContext: org.orekit.data.DataContext): ...
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
    def of(tLE: org.orekit.propagation.analytical.tle.TLE, frame: org.orekit.frames.Frame) -> 'SGP4OrbitalState':
        """
            Static constructor. Input frame is implicitly assumed to be TEME (it is not checked).
        
            Parameters:
                tle (:class:`~org.orekit.propagation.analytical.tle.TLE`): TLE
                teme (:class:`~org.orekit.frames.Frame`): TEME frame (not checked)
        
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
    public class BrouwerLyddaneOrbitalState extends :class:`~org.orekit.propagation.conversion.averaging.AbstractAveragedOrbitalState`
    
        Class representing an averaged orbital state as in the Brouwer-Lyddane theory.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`,
            :class:`~org.orekit.propagation.analytical.BrouwerLyddanePropagator`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, averagedKeplerianWithMeanAngle: org.orekit.propagation.conversion.averaging.elements.AveragedKeplerianWithMeanAngle, frame: org.orekit.frames.Frame, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
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
    public class DSST6X0OrbitalState extends :class:`~org.orekit.propagation.conversion.averaging.AbstractAveragedOrbitalState`
    
        Class representing an averaged orbital state as in the DSST theory using only the first 6 zonal harmonics as
        perturbations.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`,
            :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`,
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTZonal`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, averagedEquinoctialWithMeanAngle: org.orekit.propagation.conversion.averaging.elements.AveragedEquinoctialWithMeanAngle, frame: org.orekit.frames.Frame, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @staticmethod
    def createForces(unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider) -> java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]: ...
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
    public class EcksteinHechlerOrbitalState extends :class:`~org.orekit.propagation.conversion.averaging.AbstractAveragedOrbitalState`
    
        Class representing an averaged orbital state as in the Eckstein-Hechler theory.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`,
            :class:`~org.orekit.propagation.analytical.EcksteinHechlerPropagator`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, averagedCircularWithMeanAngle: org.orekit.propagation.conversion.averaging.elements.AveragedCircularWithMeanAngle, frame: org.orekit.frames.Frame, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
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

class AbstractHarmonicsBasedOrbitalState: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion.averaging")``.

    AbstractAveragedOrbitalState: typing.Type[AbstractAveragedOrbitalState]
    AbstractHarmonicsBasedOrbitalState: typing.Type[AbstractHarmonicsBasedOrbitalState]
    AveragedOrbitalState: typing.Type[AveragedOrbitalState]
    BrouwerLyddaneOrbitalState: typing.Type[BrouwerLyddaneOrbitalState]
    DSST6X0OrbitalState: typing.Type[DSST6X0OrbitalState]
    EcksteinHechlerOrbitalState: typing.Type[EcksteinHechlerOrbitalState]
    PythonAbstractAveragedOrbitalState: typing.Type[PythonAbstractAveragedOrbitalState]
    SGP4OrbitalState: typing.Type[SGP4OrbitalState]
    class-use: org.orekit.propagation.conversion.averaging.class-use.__module_protocol__
    converters: org.orekit.propagation.conversion.averaging.converters.__module_protocol__
    elements: org.orekit.propagation.conversion.averaging.elements.__module_protocol__
