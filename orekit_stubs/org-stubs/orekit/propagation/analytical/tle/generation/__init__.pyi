import org.hipparchus
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical.tle
import org.orekit.time
import typing



class TleGenerationAlgorithm:
    """
    public interface TleGenerationAlgorithm
    
        This interface provides a way to generate a TLE from a spacecraft state.
    
        Since:
            12.0
    """
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> templateTLE): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, spacecraftState: org.orekit.propagation.SpacecraftState, tLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.TLE`): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
        """
        ...

class TleGenerationUtil:
    """
    public final class TleGenerationUtil extends :class:`~org.orekit.propagation.analytical.tle.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility class for TLE generation algorithm.
    """
    _newTLE_0__T = typing.TypeVar('_newTLE_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def newTLE(fieldKeplerianOrbit: org.orekit.orbits.FieldKeplerianOrbit[_newTLE_0__T], fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[_newTLE_0__T], t: _newTLE_0__T, timeScale: org.orekit.time.TimeScale) -> org.orekit.propagation.analytical.tle.FieldTLE[_newTLE_0__T]:
        """
            Builds a new TLE from Keplerian parameters and a template for TLE data.
        
            Parameters:
                keplerianOrbit (:class:`~org.orekit.orbits.FieldKeplerianOrbit`<T> keplerianOrbit): the Keplerian parameters to build the TLE from
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> templateTLE): TLE used to get object identification
                bStar (T): TLE B* parameter
                utc (:class:`~org.orekit.time.TimeScale`): UTC scale
        
            Returns:
                TLE with template identification and new orbital parameters
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newTLE(keplerianOrbit: org.orekit.orbits.KeplerianOrbit, tLE: org.orekit.propagation.analytical.tle.TLE, double: float, timeScale: org.orekit.time.TimeScale) -> org.orekit.propagation.analytical.tle.TLE:
        """
            Builds a new TLE from Keplerian parameters and a template for TLE data.
        
            Parameters:
                keplerianOrbit (:class:`~org.orekit.orbits.KeplerianOrbit`): the Keplerian parameters to build the TLE from
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.TLE`): TLE used to get object identification
                bStar (double): TLE B* parameter
                utc (:class:`~org.orekit.time.TimeScale`): UTC scale
        
            Returns:
                TLE with template identification and new orbital parameters
        
        """
        ...

class FixedPointTleGenerationAlgorithm(TleGenerationAlgorithm):
    """
    public class FixedPointTleGenerationAlgorithm extends :class:`~org.orekit.propagation.analytical.tle.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
    
        Fixed Point method to reverse SGP4 and SDP4 propagation algorithm and generate a usable TLE from a spacecraft state.
    
        Using this algorithm, the B* value is not computed. In other words, the B* value from the template TLE is set to the
        generated one.
    
        Since:
            12.0
    """
    EPSILON_DEFAULT: typing.ClassVar[float] = ...
    """
    public static final double EPSILON_DEFAULT
    
        Default value for epsilon.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX_ITERATIONS_DEFAULT: typing.ClassVar[int] = ...
    """
    public static final int MAX_ITERATIONS_DEFAULT
    
        Default value for maxIterations.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SCALE_DEFAULT: typing.ClassVar[float] = ...
    """
    public static final double SCALE_DEFAULT
    
        Default value for scale.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float, timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame): ...
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm.generate` in
                interface :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> templateTLE): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, spacecraftState: org.orekit.propagation.SpacecraftState, tLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm.generate` in
                interface :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.TLE`): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
        """
        ...

class LeastSquaresTleGenerationAlgorithm(TleGenerationAlgorithm):
    """
    public class LeastSquaresTleGenerationAlgorithm extends :class:`~org.orekit.propagation.analytical.tle.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
    
        Least squares method to generate a usable TLE from a spacecraft state.
    
        Since:
            12.0
    """
    DEFAULT_MAX_ITERATIONS: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITERATIONS
    
        Default value for maximum number of iterations.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame): ...
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm.generate` in
                interface :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> templateTLE): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, spacecraftState: org.orekit.propagation.SpacecraftState, tLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm.generate` in
                interface :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.TLE`): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
        """
        ...
    def getRms(self) -> float:
        """
            Get the Root Mean Square of the TLE estimation.
        
            Be careful that the RMS is updated each time the
            :meth:`~org.orekit.propagation.analytical.tle.generation.LeastSquaresTleGenerationAlgorithm.generate` method is called.
        
            Returns:
                the RMS
        
        
        """
        ...

class PythonTleGenerationAlgorithm(TleGenerationAlgorithm):
    """
    public class PythonTleGenerationAlgorithm extends :class:`~org.orekit.propagation.analytical.tle.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm.generate` in
                interface :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.FieldTLE`<T> templateTLE): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, spacecraftState: org.orekit.propagation.SpacecraftState, tLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
            Generate a TLE from a given spacecraft state and a template TLE.
        
            The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian
            elements contained in the generate TLE a based on the provided state and not the template TLE.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm.generate` in
                interface :class:`~org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                templateTLE (:class:`~org.orekit.propagation.analytical.tle.TLE`): template TLE
        
            Returns:
                a TLE corresponding to the given state
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.tle.generation")``.

    FixedPointTleGenerationAlgorithm: typing.Type[FixedPointTleGenerationAlgorithm]
    LeastSquaresTleGenerationAlgorithm: typing.Type[LeastSquaresTleGenerationAlgorithm]
    PythonTleGenerationAlgorithm: typing.Type[PythonTleGenerationAlgorithm]
    TleGenerationAlgorithm: typing.Type[TleGenerationAlgorithm]
    TleGenerationUtil: typing.Type[TleGenerationUtil]
