import org.orekit.data
import org.orekit.forces.gravity.potential
import org.orekit.orbits
import org.orekit.propagation.conversion.averaging
import org.orekit.propagation.conversion.averaging.converters.class-use
import typing



_OsculatingToAveragedConverter__T = typing.TypeVar('_OsculatingToAveragedConverter__T', bound=org.orekit.propagation.conversion.averaging.AveragedOrbitalState)  # <T>
class OsculatingToAveragedConverter(typing.Generic[_OsculatingToAveragedConverter__T]):
    """
    public interface OsculatingToAveragedConverter<T extends :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`>
    
        Interface for osculating-to-averaged converters.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`
    """
    def convertToAveraged(self, orbit: org.orekit.orbits.Orbit) -> _OsculatingToAveragedConverter__T:
        """
            Convert osculating orbit to averaged orbital state according to underlying theory.
        
            Parameters:
                osculatingOrbit (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                averaged orbital state
        
        
        """
        ...

_FixedPointOsculatingToAveragedConverter__T = typing.TypeVar('_FixedPointOsculatingToAveragedConverter__T', bound=org.orekit.propagation.conversion.averaging.AveragedOrbitalState)  # <T>
class FixedPointOsculatingToAveragedConverter(OsculatingToAveragedConverter[_FixedPointOsculatingToAveragedConverter__T], typing.Generic[_FixedPointOsculatingToAveragedConverter__T]):
    """
    public abstract class FixedPointOsculatingToAveragedConverter<T extends :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`> extends :class:`~org.orekit.propagation.conversion.averaging.converters.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.averaging.converters.OsculatingToAveragedConverter`<T>
    
        Abstract class for osculating-to-averaged converters based on a fixed-point algorithm.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.converters.OsculatingToAveragedConverter`
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_EPSILON
    
        Default convergence threshold.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MAX_ITERATIONS: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITERATIONS
    
        Default maximum number of iterations.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getEpsilon(self) -> float:
        """
            Getter for the convergence threshold.
        
            Returns:
                convergence threshold
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
            Getter for the maximum number of iterations.
        
            Returns:
                maximum number of iterations
        
        
        """
        ...
    def setEpsilon(self, double: float) -> None:
        """
            Setter for epsilon.
        
            Parameters:
                epsilon (double): convergence threshold.
        
        
        """
        ...
    def setMaxIterations(self, int: int) -> None:
        """
            Setter for maximum number of iterations.
        
            Parameters:
                maxIterations (int): maximum iterations
        
        
        """
        ...

class OsculatingToBrouwerLyddaneConverter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.BrouwerLyddaneOrbitalState]):
    """
    public class OsculatingToBrouwerLyddaneConverter extends :class:`~org.orekit.propagation.conversion.averaging.converters.FixedPointOsculatingToAveragedConverter`<:class:`~org.orekit.propagation.conversion.averaging.BrouwerLyddaneOrbitalState`>
    
        Class for osculating-to-averaged conversion according to Brouwer-Lyddane theory. Value of M2 parameter is set to zero.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.analytical.BrouwerLyddanePropagator`,
            :class:`~org.orekit.propagation.conversion.averaging.BrouwerLyddaneOrbitalState`
    """
    @typing.overload
    def __init__(self, double: float, int: int, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    def convertToAveraged(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.BrouwerLyddaneOrbitalState:
        """
            Convert osculating orbit to averaged orbital state according to underlying theory.
        
            Parameters:
                osculatingOrbit (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                averaged orbital state
        
        
        """
        ...

class OsculatingToDSST6X0Converter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.DSST6X0OrbitalState]):
    """
    public class OsculatingToDSST6X0Converter extends :class:`~org.orekit.propagation.conversion.averaging.converters.FixedPointOsculatingToAveragedConverter`<:class:`~org.orekit.propagation.conversion.averaging.DSST6X0OrbitalState`>
    
        Class for osculating-to-averaged conversion according to DSST theory, using 6 zonal harmonics as the only perturbations.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`,
            :class:`~org.orekit.propagation.conversion.averaging.DSST6X0OrbitalState`
    """
    @typing.overload
    def __init__(self, double: float, int: int, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    def convertToAveraged(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.DSST6X0OrbitalState:
        """
            Convert osculating orbit to averaged orbital state according to underlying theory.
        
            Parameters:
                osculatingOrbit (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                averaged orbital state
        
        
        """
        ...

class OsculatingToEcksteinHechlerConverter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.EcksteinHechlerOrbitalState]):
    """
    public class OsculatingToEcksteinHechlerConverter extends :class:`~org.orekit.propagation.conversion.averaging.converters.FixedPointOsculatingToAveragedConverter`<:class:`~org.orekit.propagation.conversion.averaging.EcksteinHechlerOrbitalState`>
    
        Class for osculating-to-averaged conversion according to Eckstein-Hechler theory.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.analytical.EcksteinHechlerPropagator`,
            :class:`~org.orekit.propagation.conversion.averaging.EcksteinHechlerOrbitalState`
    """
    @typing.overload
    def __init__(self, double: float, int: int, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    def convertToAveraged(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.EcksteinHechlerOrbitalState:
        """
            Convert osculating orbit to averaged orbital state according to underlying theory.
        
            Parameters:
                osculatingOrbit (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                averaged orbital state
        
        
        """
        ...

class OsculatingToSGP4Converter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.SGP4OrbitalState]):
    """
    public class OsculatingToSGP4Converter extends :class:`~org.orekit.propagation.conversion.averaging.converters.FixedPointOsculatingToAveragedConverter`<:class:`~org.orekit.propagation.conversion.averaging.SGP4OrbitalState`>
    
        Class for osculating-to-averaged conversion according to "SGP4" theory, meant as the set of models associated to
        Two-Line Elements.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.analytical.tle.TLEPropagator`,
            :class:`~org.orekit.propagation.conversion.averaging.SGP4OrbitalState`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def convertToAveraged(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.SGP4OrbitalState:
        """
            Convert osculating orbit to averaged orbital state according to underlying theory.
        
            Parameters:
                osculatingOrbit (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                averaged orbital state
        
        
        """
        ...

_PythonFixedPointOsculatingToAveragedConverter__T = typing.TypeVar('_PythonFixedPointOsculatingToAveragedConverter__T', bound=org.orekit.propagation.conversion.averaging.AveragedOrbitalState)  # <T>
class PythonFixedPointOsculatingToAveragedConverter(FixedPointOsculatingToAveragedConverter[_PythonFixedPointOsculatingToAveragedConverter__T], typing.Generic[_PythonFixedPointOsculatingToAveragedConverter__T]):
    """
    public class PythonFixedPointOsculatingToAveragedConverter<T extends :class:`~org.orekit.propagation.conversion.averaging.AveragedOrbitalState`> extends :class:`~org.orekit.propagation.conversion.averaging.converters.FixedPointOsculatingToAveragedConverter`<T>
    """
    def __init__(self, double: float, int: int): ...
    def convertToAveraged(self, orbit: org.orekit.orbits.Orbit) -> _PythonFixedPointOsculatingToAveragedConverter__T:
        """
            Convert osculating orbit to averaged orbital state according to underlying theory.
        
            Parameters:
                osculatingOrbit (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                averaged orbital state
        
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion.averaging.converters")``.

    FixedPointOsculatingToAveragedConverter: typing.Type[FixedPointOsculatingToAveragedConverter]
    OsculatingToAveragedConverter: typing.Type[OsculatingToAveragedConverter]
    OsculatingToBrouwerLyddaneConverter: typing.Type[OsculatingToBrouwerLyddaneConverter]
    OsculatingToDSST6X0Converter: typing.Type[OsculatingToDSST6X0Converter]
    OsculatingToEcksteinHechlerConverter: typing.Type[OsculatingToEcksteinHechlerConverter]
    OsculatingToSGP4Converter: typing.Type[OsculatingToSGP4Converter]
    PythonFixedPointOsculatingToAveragedConverter: typing.Type[PythonFixedPointOsculatingToAveragedConverter]
    class-use: org.orekit.propagation.conversion.averaging.converters.class-use.__module_protocol__
