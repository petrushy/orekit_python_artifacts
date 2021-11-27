import org.hipparchus.analysis
import org.hipparchus.special.elliptic
import typing



class BesselJ(org.hipparchus.analysis.UnivariateFunction):
    def __init__(self, double: float): ...
    @staticmethod
    def rjBesl(double: float, double2: float, int: int) -> 'BesselJ.BesselJResult': ...
    @typing.overload
    def value(self, double: float) -> float: ...
    @typing.overload
    @staticmethod
    def value(double: float, double2: float) -> float: ...
    class BesselJResult:
        def __init__(self, doubleArray: typing.List[float], int: int): ...
        def getVals(self) -> typing.List[float]: ...
        def getnVals(self) -> int: ...

class Beta:
    """
    public class Beta extends Object
    
    
        This is a utility class that provides computation methods related to the Beta family of functions.
    
        Implementation of :meth:`~org.hipparchus.special.Beta.logBeta` is based on the algorithms described in
    
          - `Didonato and Morris (1986) <http://dx.doi.org/10.1145/22721.23109>`, *Computation of the Incomplete Gamma Function
            Ratios and their Inverse*, TOMS 12(4), 377-393,
          - `Didonato and Morris (1992) <http://dx.doi.org/10.1145/131766.131776>`, *Algorithm 708: Significant Digit Computation of
            the Incomplete Beta Function Ratios*, TOMS 18(3), 360-373,
    
        and implemented in the `NSWC Library of Mathematical Functions <http://www.dtic.mil/docs/citations/ADA476840>`,
        available `here <http://www.ualberta.ca/CNS/RESEARCH/Software/NumericalNSWC/site.html>`. This library is "approved for
        public release", and the `Copyright guidance <http://www.dtic.mil/dtic/pdf/announcements/CopyrightGuidance.pdf>`
        indicates that unless otherwise stated in the code, all FORTRAN functions in this library are license free. Since no
        such notice appears in the code these functions can safely be ported to Hipparchus.
    """
    @staticmethod
    def logBeta(double: float, double2: float) -> float:
        """
            Returns the value of log B(p, q) for 0 Ã¢â€°Â¤ x Ã¢â€°Â¤ 1 and p, q > 0. Based on the *NSWC Library of Mathematics
            Subroutines* implementation, :code:`DBETLN`.
        
            Parameters:
                p (double): First argument.
                q (double): Second argument.
        
            Returns:
                the value of :code:`log(Beta(p, q))`, :code:`NaN` if :code:`p <= 0` or :code:`q <= 0`.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def regularizedBeta(double: float, double2: float, double3: float) -> float:
        """
            Returns the ` regularized beta function <http://mathworld.wolfram.com/RegularizedBetaFunction.html>` I(x, a, b).
        
            Parameters:
                x (double): Value.
                a (double): Parameter :code:`a`.
                b (double): Parameter :code:`b`.
        
            Returns:
                the regularized beta function I(x, a, b).
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Returns the ` regularized beta function <http://mathworld.wolfram.com/RegularizedBetaFunction.html>` I(x, a, b).
        
            Parameters:
                x (double): Value.
                a (double): Parameter :code:`a`.
                b (double): Parameter :code:`b`.
                epsilon (double): When the absolute value of the nth item in the series is less than epsilon the approximation ceases to calculate further
                    elements in the series.
        
            Returns:
                the regularized beta function I(x, a, b)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Returns the regularized beta function I(x, a, b).
        
            Parameters:
                x (double): the value.
                a (double): Parameter :code:`a`.
                b (double): Parameter :code:`b`.
                maxIterations (int): Maximum number of "iterations" to complete.
        
            Returns:
                the regularized beta function I(x, a, b)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Returns the regularized beta function I(x, a, b). The implementation of this method is based on:
        
              - ` Regularized Beta Function <http://mathworld.wolfram.com/RegularizedBetaFunction.html>`.
              - ` Regularized Beta Function <http://functions.wolfram.com/06.21.10.0001.01>`.
        
        
            Parameters:
                x (double): the value.
                a (double): Parameter :code:`a`.
                b (double): Parameter :code:`b`.
                epsilon (double): When the absolute value of the nth item in the series is less than epsilon the approximation ceases to calculate further
                    elements in the series.
                maxIterations (int): Maximum number of "iterations" to complete.
        
            Returns:
                the regularized beta function I(x, a, b)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def regularizedBeta(double: float, double2: float, double3: float, double4: float) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedBeta(double: float, double2: float, double3: float, double4: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedBeta(double: float, double2: float, double3: float, int: int) -> float: ...

class Erf:
    @typing.overload
    @staticmethod
    def erf(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def erf(double: float, double2: float) -> float: ...
    @staticmethod
    def erfInv(double: float) -> float: ...
    @staticmethod
    def erfc(double: float) -> float: ...
    @staticmethod
    def erfcInv(double: float) -> float: ...

class Gamma:
    GAMMA: typing.ClassVar[float] = ...
    LANCZOS_G: typing.ClassVar[float] = ...
    @staticmethod
    def digamma(double: float) -> float: ...
    @staticmethod
    def gamma(double: float) -> float: ...
    @staticmethod
    def invGamma1pm1(double: float) -> float: ...
    @staticmethod
    def lanczos(double: float) -> float: ...
    @staticmethod
    def logGamma(double: float) -> float: ...
    @staticmethod
    def logGamma1p(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(double: float, double2: float, double3: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(double: float, double2: float, double3: float, int: int) -> float: ...
    @staticmethod
    def trigamma(double: float) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special")``.

    BesselJ: typing.Type[BesselJ]
    Beta: typing.Type[Beta]
    Erf: typing.Type[Erf]
    Gamma: typing.Type[Gamma]
    elliptic: org.hipparchus.special.elliptic.__module_protocol__
