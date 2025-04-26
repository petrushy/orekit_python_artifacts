
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.hipparchus
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.attitudes
import org.orekit.data
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.time
import typing



class MeanTheory:
    """
    public interface MeanTheory
    
        Interface for theories that convert osculating into mean orbit.
    
        Since:
            13.0
    """
    def getReferenceRadius(self) -> float:
        """
            Gets reference radius of the central body (m).
        
            Returns:
                reference radius of the central body
        
        
        """
        ...
    def getTheoryName(self) -> str:
        """
            Gets the name of the theory used for osculating to mean conversion.
        
            Returns:
                the actual theory
        
        
        """
        ...
    _initialize_0__T = typing.TypeVar('_initialize_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initialize(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_initialize_0__T]) -> org.orekit.orbits.FieldOrbit[_initialize_0__T]:
        """
            Rough initialization of the mean orbit.
        
            By default, the mean orbit is initialized with the osculating orbit.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): the osculating orbit
        
            Returns:
                initial mean orbit
        
        
        """
        ...
    @typing.overload
    def initialize(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Rough initialization of the mean orbit.
        
            By default, the mean orbit is initialized with the osculating orbit.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): the osculating orbit
        
            Returns:
                initial mean orbit
        
        """
        ...
    _meanToOsculating_0__T = typing.TypeVar('_meanToOsculating_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def meanToOsculating(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]) -> org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]:
        """
            Gets osculating orbit from mean orbit.
        
            Parameters:
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): mean orbit
        
            Returns:
                osculating orbit
        
        
        """
        ...
    @typing.overload
    def meanToOsculating(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Gets osculating orbit from mean orbit.
        
            Parameters:
                mean (:class:`~org.orekit.orbits.Orbit`): mean orbit
        
            Returns:
                osculating orbit
        
        """
        ...
    _postprocessing_0__T = typing.TypeVar('_postprocessing_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def postprocessing(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_postprocessing_0__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_postprocessing_0__T]) -> org.orekit.orbits.FieldOrbit[_postprocessing_0__T]:
        """
            Post-treatment of the converted mean orbit.
        
            By default, the mean orbit returned is of the same type as the osculating orbit to be converted.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): the osculating orbit to be converted
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): the converted mean orbit
        
            Returns:
                postprocessed mean orbit
        
        
        """
        ...
    @typing.overload
    def postprocessing(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Post-treatment of the converted mean orbit.
        
            By default, the mean orbit returned is of the same type as the osculating orbit to be converted.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): the osculating orbit to be converted
                mean (:class:`~org.orekit.orbits.Orbit`): the converted mean orbit
        
            Returns:
                postprocessed mean orbit
        
        """
        ...
    _preprocessing_0__T = typing.TypeVar('_preprocessing_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def preprocessing(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_preprocessing_0__T]) -> org.orekit.orbits.FieldOrbit[_preprocessing_0__T]:
        """
            Pre-treatment of the osculating orbit to be converted.
        
            By default, no pre-treatment is applied to the osculating orbit.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): the osculating orbit to be treated
        
            Returns:
                preprocessed osculating orbit
        
        
        """
        ...
    @typing.overload
    def preprocessing(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Pre-treatment of the osculating orbit to be converted.
        
            By default, no pre-treatment is applied to the osculating orbit.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): the osculating orbit to be treated
        
            Returns:
                preprocessed osculating orbit
        
        """
        ...

class OsculatingToMeanConverter:
    """
    public interface OsculatingToMeanConverter
    
        Interface for osculating to mean orbit converters.
    
        An osculating-to-mean converter consists of:
    
          - an algorithm performing the conversion, provided by an implementation of this interface,
          - a theory giving the meaning of the mean orbit, to be set as the
            :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`.
    
    
        Since:
            13.0
    """
    _convertToMean_0__T = typing.TypeVar('_convertToMean_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def convertToMean(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_convertToMean_0__T]) -> org.orekit.orbits.FieldOrbit[_convertToMean_0__T]:
        """
            Converts an osculating orbit into a mean orbit.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit
        
            Returns:
                mean orbit
        
        
        """
        ...
    @typing.overload
    def convertToMean(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Converts an osculating orbit into a mean orbit.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                mean orbit
        
        """
        ...
    def getMeanTheory(self) -> MeanTheory:
        """
            Gets the theory defining the mean orbit.
        
            Returns:
                the mean theory
        
        
        """
        ...
    def setMeanTheory(self, meanTheory: MeanTheory) -> None:
        """
            Sets the theory defining the mean orbit.
        
            Parameters:
                theory (:class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`): the mean theory
        
        
        """
        ...

class BrouwerLyddaneTheory(MeanTheory):
    """
    public class BrouwerLyddaneTheory extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
    
        Brouwer-Lyddane theory for osculating to mean orbit conversion.
    
        Since:
            13.0
    """
    THEORY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THEORY
    
        Theory used for converting from osculating to mean orbit.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    def getReferenceRadius(self) -> float:
        """
            Gets reference radius of the central body (m).
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getReferenceRadius` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                reference radius of the central body
        
        
        """
        ...
    def getTheoryName(self) -> str:
        """
            Gets the name of the theory used for osculating to mean conversion.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getTheoryName` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                the actual theory
        
        
        """
        ...
    _meanToOsculating_0__T = typing.TypeVar('_meanToOsculating_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def meanToOsculating(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]) -> org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): mean orbit
        
            Returns:
                osculating orbit
        
        
        """
        ...
    @typing.overload
    def meanToOsculating(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.Orbit`): mean orbit
        
            Returns:
                osculating orbit
        
        """
        ...

class DSSTTheory(MeanTheory):
    """
    public class DSSTTheory extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
    
        DSST theory for osculating to mean orbit conversion.
    
        Since:
            13.0
    """
    THEORY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THEORY
    
        Theory used for converting from osculating to mean orbit.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    def getReferenceRadius(self) -> float:
        """
            Gets reference radius of the central body (m).
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getReferenceRadius` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                reference radius of the central body
        
        
        """
        ...
    def getTheoryName(self) -> str:
        """
            Gets the name of the theory used for osculating to mean conversion.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getTheoryName` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                the actual theory
        
        
        """
        ...
    _meanToOsculating_0__T = typing.TypeVar('_meanToOsculating_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def meanToOsculating(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]) -> org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): mean orbit
        
            Returns:
                osculating orbit
        
        
        """
        ...
    @typing.overload
    def meanToOsculating(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.Orbit`): mean orbit
        
            Returns:
                osculating orbit
        
        """
        ...
    _preprocessing_0__T = typing.TypeVar('_preprocessing_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def preprocessing(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_preprocessing_0__T]) -> org.orekit.orbits.FieldOrbit[_preprocessing_0__T]:
        """
            Pre-treatment of the osculating orbit to be converted.
        
            By default, no pre-treatment is applied to the osculating orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.preprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): the osculating orbit to be treated
        
            Returns:
                preprocessed osculating orbit
        
        
        """
        ...
    @typing.overload
    def preprocessing(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Pre-treatment of the osculating orbit to be converted.
        
            By default, no pre-treatment is applied to the osculating orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.preprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): the osculating orbit to be treated
        
            Returns:
                preprocessed osculating orbit
        
        """
        ...

class EcksteinHechlerTheory(MeanTheory):
    """
    public class EcksteinHechlerTheory extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
    
        Eckstein-Hechler theory for osculating to mean orbit conversion.
    
        Since:
            13.0
    """
    THEORY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THEORY
    
        Theory used for converting from osculating to mean orbit.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    def getReferenceRadius(self) -> float:
        """
            Gets reference radius of the central body (m).
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getReferenceRadius` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                reference radius of the central body
        
        
        """
        ...
    def getTheoryName(self) -> str:
        """
            Gets the name of the theory used for osculating to mean conversion.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getTheoryName` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                the actual theory
        
        
        """
        ...
    _meanToOsculating_0__T = typing.TypeVar('_meanToOsculating_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def meanToOsculating(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]) -> org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): mean orbit
        
            Returns:
                osculating orbit
        
        
        """
        ...
    @typing.overload
    def meanToOsculating(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.Orbit`): mean orbit
        
            Returns:
                osculating orbit
        
        """
        ...
    _postprocessing_0__T = typing.TypeVar('_postprocessing_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def postprocessing(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_postprocessing_0__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_postprocessing_0__T]) -> org.orekit.orbits.FieldOrbit[_postprocessing_0__T]:
        """
            Post-treatment of the converted mean orbit.
        
            The mean orbit returned is circular.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.postprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): the osculating orbit to be converted
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): the converted mean orbit
        
            Returns:
                postprocessed mean orbit
        
        
        """
        ...
    @typing.overload
    def postprocessing(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Post-treatment of the converted mean orbit.
        
            The mean orbit returned is circular.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.postprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): the osculating orbit to be converted
                mean (:class:`~org.orekit.orbits.Orbit`): the converted mean orbit
        
            Returns:
                postprocessed mean orbit
        
        """
        ...

class FixedPointConverter(OsculatingToMeanConverter):
    """
    public class FixedPointConverter extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
    
        Class enabling conversion from osculating to mean orbit for a given theory using a fixed-point algorithm.
    
        Since:
            13.0
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
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
    DEFAULT_DAMPING: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_DAMPING
    
        Default damping ratio.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float): ...
    @typing.overload
    def __init__(self, meanTheory: MeanTheory): ...
    @typing.overload
    def __init__(self, meanTheory: MeanTheory, double: float, int: int, double2: float): ...
    _convertToMean_0__T = typing.TypeVar('_convertToMean_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def convertToMean(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_convertToMean_0__T]) -> org.orekit.orbits.FieldOrbit[_convertToMean_0__T]:
        """
            Converts an osculating orbit into a mean orbit. Uses a fixed-point algorithm.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.convertToMean` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit
        
            Returns:
                mean orbit
        
        
        """
        ...
    @typing.overload
    def convertToMean(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Converts an osculating orbit into a mean orbit. Uses a fixed-point algorithm.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.convertToMean` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                mean orbit
        
        """
        ...
    def getDamping(self) -> float:
        """
            Gets damping ratio.
        
            Returns:
                damping ratio
        
        
        """
        ...
    def getIterationsNb(self) -> int:
        """
            Gets the number of iterations performed by the last conversion.
        
            Returns:
                number of iterations
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
            Gets maximum number of iterations.
        
            Returns:
                maximum number of iterations
        
        
        """
        ...
    def getMeanTheory(self) -> MeanTheory:
        """
            Gets the theory defining the mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.getMeanTheory` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Returns:
                the mean theory
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
            Gets convergence threshold.
        
            Returns:
                convergence threshold
        
        
        """
        ...
    def setDamping(self, double: float) -> None:
        """
            Sets damping ratio.
        
            Parameters:
                damping (double): damping ratio
        
        
        """
        ...
    def setMaxIterations(self, int: int) -> None:
        """
            Sets maximum number of iterations.
        
            Parameters:
                maxIterations (int): maximum number of iterations
        
        
        """
        ...
    def setMeanTheory(self, meanTheory: MeanTheory) -> None:
        """
            Sets the theory defining the mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.setMeanTheory` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                meanTheory (:class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`): the mean theory
        
        
        """
        ...
    def setThreshold(self, double: float) -> None:
        """
            Sets convergence threshold.
        
            Parameters:
                threshold (double): convergence threshold
        
        
        """
        ...

class LeastSquaresConverter(OsculatingToMeanConverter):
    """
    public class LeastSquaresConverter extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
    
        Class enabling conversion from osculating to mean orbit for a given theory using a least-squares algorithm.
    
        Since:
            13.0
    """
    DEFAULT_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_THRESHOLD
    
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
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    @typing.overload
    def __init__(self, meanTheory: MeanTheory): ...
    @typing.overload
    def __init__(self, meanTheory: MeanTheory, leastSquaresOptimizer: typing.Union[org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer, typing.Callable]): ...
    @typing.overload
    def __init__(self, meanTheory: MeanTheory, leastSquaresOptimizer: typing.Union[org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer, typing.Callable], double: float, int: int): ...
    _convertToMean_0__T = typing.TypeVar('_convertToMean_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def convertToMean(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_convertToMean_0__T]) -> org.orekit.orbits.FieldOrbit[_convertToMean_0__T]:
        """
            Converts an osculating orbit into a mean orbit. Uses a least-square algorithm.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.convertToMean` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit
        
            Returns:
                mean orbit
        
        
        """
        ...
    @typing.overload
    def convertToMean(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Converts an osculating orbit into a mean orbit. Uses a least-square algorithm.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.convertToMean` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                mean orbit
        
        """
        ...
    def getIterationsNb(self) -> int:
        """
            Gets the number of iterations performed by the last conversion.
        
            Returns:
                number of iterations
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
            Gets the maximum number of iterations.
        
            Returns:
                maximum number of iterations
        
        
        """
        ...
    def getMeanTheory(self) -> MeanTheory:
        """
            Gets the theory defining the mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.getMeanTheory` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Returns:
                the mean theory
        
        
        """
        ...
    def getOptimizer(self) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer:
        """
            Gets the optimizer.
        
            Returns:
                the optimizer
        
        
        """
        ...
    def getRMS(self) -> float:
        """
            Gets the RMS for the last conversion.
        
            Returns:
                the RMS
        
        
        """
        ...
    def getThreshold(self) -> float:
        """
            Gets the convergence threshold.
        
            Returns:
                convergence threshold
        
        
        """
        ...
    def setMaxIterations(self, int: int) -> None:
        """
            Sets maximum number of iterations.
        
            Parameters:
                maxIterations (int): maximum number of iterations
        
        
        """
        ...
    def setMeanTheory(self, meanTheory: MeanTheory) -> None:
        """
            Sets the theory defining the mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.setMeanTheory` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                meanTheory (:class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`): the mean theory
        
        
        """
        ...
    def setOptimizer(self, leastSquaresOptimizer: typing.Union[org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer, typing.Callable]) -> None:
        """
            Sets the optimizer.
        
            Parameters:
                optimizer (:class:`~org.orekit.propagation.conversion.osc2mean.https:.www.hipparchus.org.apidocs.org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer?is`): the optimizer
        
        
        """
        ...
    def setThreshold(self, double: float) -> None:
        """
            Sets the convergence threshold.
        
            Parameters:
                threshold (double): convergence threshold
        
        
        """
        ...

class PythonMeanTheory(MeanTheory):
    """
    public class PythonMeanTheory extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getReferenceRadius(self) -> float:
        """
            Gets reference radius of the central body (m).
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getReferenceRadius` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                reference radius of the central body
        
        
        """
        ...
    def getTheoryName(self) -> str:
        """
            Gets the name of the theory used for osculating to mean conversion.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getTheoryName` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                the actual theory
        
        
        """
        ...
    _meanToOsculating_0__T = typing.TypeVar('_meanToOsculating_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def meanToOsculating(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]) -> org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): mean orbit
        
            Returns:
                osculating orbit
        
        
        """
        ...
    @typing.overload
    def meanToOsculating(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.Orbit`): mean orbit
        
            Returns:
                osculating orbit
        
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

class PythonOsculatingToMeanConverter(OsculatingToMeanConverter):
    """
    public class PythonOsculatingToMeanConverter extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
    """
    def __init__(self): ...
    _convertToMean_0__T = typing.TypeVar('_convertToMean_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def convertToMean(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_convertToMean_0__T]) -> org.orekit.orbits.FieldOrbit[_convertToMean_0__T]:
        """
            Converts an osculating orbit into a mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.convertToMean` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit
        
            Returns:
                mean orbit
        
        
        """
        ...
    @typing.overload
    def convertToMean(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Converts an osculating orbit into a mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.convertToMean` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit
        
            Returns:
                mean orbit
        
        """
        ...
    def finalize(self) -> None: ...
    def getMeanTheory(self) -> MeanTheory:
        """
            Gets the theory defining the mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.getMeanTheory` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Returns:
                the mean theory
        
        
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
    def setMeanTheory(self, meanTheory: MeanTheory) -> None:
        """
            Sets the theory defining the mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter.setMeanTheory` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter`
        
            Parameters:
                theory (:class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`): the mean theory
        
        
        """
        ...

class TLETheory(MeanTheory):
    """
    public class TLETheory extends :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
    
        TLE, i.e. SGP4/SDP4, theory for osculating to mean orbit conversion.
    
        Since:
            13.0
    """
    TMP_L1: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TMP_L1
    
        First line of arbitrary TLE. Should not impact conversion.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TMP_L2: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TMP_L2
    
        Second line of arbitrary TLE. Should not impact conversion.
    
        Also see:
            :meth:`~constant`
    
    
    """
    THEORY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.conversion.osc2mean.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` THEORY
    
        Theory used for converting from osculating to mean orbit.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ___init___2__T = typing.TypeVar('___init___2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    ___init___3__T = typing.TypeVar('___init___3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    ___init___4__T = typing.TypeVar('___init___4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[___init___2__T]): ...
    @typing.overload
    def __init__(self, fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[___init___3__T], dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, fieldTLE: org.orekit.propagation.analytical.tle.FieldTLE[___init___4__T], timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame): ...
    def getReferenceRadius(self) -> float:
        """
            Gets reference radius of the central body (m).
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getReferenceRadius` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                reference radius of the central body
        
        
        """
        ...
    def getTheoryName(self) -> str:
        """
            Gets the name of the theory used for osculating to mean conversion.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.getTheoryName` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Returns:
                the actual theory
        
        
        """
        ...
    _meanToOsculating_0__T = typing.TypeVar('_meanToOsculating_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def meanToOsculating(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]) -> org.orekit.orbits.FieldOrbit[_meanToOsculating_0__T]:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): mean orbit
        
            Returns:
                osculating orbit
        
        
        """
        ...
    @typing.overload
    def meanToOsculating(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Gets osculating orbit from mean orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.meanToOsculating` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                mean (:class:`~org.orekit.orbits.Orbit`): mean orbit
        
            Returns:
                osculating orbit
        
        """
        ...
    _postprocessing_0__T = typing.TypeVar('_postprocessing_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def postprocessing(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_postprocessing_0__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_postprocessing_0__T]) -> org.orekit.orbits.FieldOrbit[_postprocessing_0__T]:
        """
            Post-treatment of the converted mean orbit.
        
            The mean orbit returned is a Keplerian orbit in TEME frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.postprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): the osculating orbit to be converted
                mean (:class:`~org.orekit.orbits.FieldOrbit`<T> mean): the converted mean orbit
        
            Returns:
                postprocessed mean orbit
        
        
        """
        ...
    @typing.overload
    def postprocessing(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Post-treatment of the converted mean orbit.
        
            The mean orbit returned is a Keplerian orbit in TEME frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.postprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): the osculating orbit to be converted
                mean (:class:`~org.orekit.orbits.Orbit`): the converted mean orbit
        
            Returns:
                postprocessed mean orbit
        
        """
        ...
    _preprocessing_0__T = typing.TypeVar('_preprocessing_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def preprocessing(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_preprocessing_0__T]) -> org.orekit.orbits.FieldOrbit[_preprocessing_0__T]:
        """
            Pre-treatment of the osculating orbit to be converted.
        
            The osculating orbit is transformed to TEME frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.preprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): the osculating orbit to be treated
        
            Returns:
                preprocessed osculating orbit
        
        
        """
        ...
    @typing.overload
    def preprocessing(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Pre-treatment of the osculating orbit to be converted.
        
            The osculating orbit is transformed to TEME frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.osc2mean.MeanTheory.preprocessing` in
                interface :class:`~org.orekit.propagation.conversion.osc2mean.MeanTheory`
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): the osculating orbit to be treated
        
            Returns:
                preprocessed osculating orbit
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion.osc2mean")``.

    BrouwerLyddaneTheory: typing.Type[BrouwerLyddaneTheory]
    DSSTTheory: typing.Type[DSSTTheory]
    EcksteinHechlerTheory: typing.Type[EcksteinHechlerTheory]
    FixedPointConverter: typing.Type[FixedPointConverter]
    LeastSquaresConverter: typing.Type[LeastSquaresConverter]
    MeanTheory: typing.Type[MeanTheory]
    OsculatingToMeanConverter: typing.Type[OsculatingToMeanConverter]
    PythonMeanTheory: typing.Type[PythonMeanTheory]
    PythonOsculatingToMeanConverter: typing.Type[PythonOsculatingToMeanConverter]
    TLETheory: typing.Type[TLETheory]
