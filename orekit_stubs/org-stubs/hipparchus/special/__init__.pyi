
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.special.elliptic
import typing



class BesselJ(org.hipparchus.analysis.UnivariateFunction):
    """
    public classBesselJ extends :class:`~org.hipparchus.special.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.UnivariateFunction`
    
        This class provides computation methods related to Bessel functions of the first kind. Detailed descriptions of these
        functions are available in `Wikipedia <http://en.wikipedia.org/wiki/Bessel_function>`, `Abramowitz and Stegun
        <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>` (Ch. 9-11), and `DLMF <http://dlmf.nist.gov/>` (Ch. 10).
    
        This implementation is based on the rjbesl Fortran routine at `Netlib <http://www.netlib.org/specfun/rjbesl>`.
    
        From the Fortran code:
    
        This program is based on a program written by David J. Sookne (2) that computes values of the Bessel functions J or I of
        real argument and integer order. Modifications include the restriction of the computation to the J Bessel function of
        non-negative real argument, the extension of the computation to arbitrary positive order, and the elimination of most
        underflow.
    
        References:
    
          - "A Note on Backward Recurrence Algorithms," Olver, F. W. J., and Sookne, D. J., Math. Comp. 26, 1972, pp 941-947.
          - "Bessel Functions of Real Argument and Integer Order," Sookne, D. J., NBS Jour. of Res. B. 77B, 1973, pp 125-132.
    """
    def __init__(self, double: float): ...
    @staticmethod
    def rjBesl(double: float, double2: float, int: int) -> 'BesselJ.BesselJResult':
        """
            Calculates Bessel functions \(J_{n+alpha}(x)\) for non-negative argument x, and non-negative order n + alpha.
        
            Before using the output vector, the user should check that nVals = nb, i.e., all orders have been calculated to the
            desired accuracy. See BesselResult class javadoc for details on return values.
        
            Parameters:
                x (double): non-negative real argument for which J's are to be calculated
                alpha (double): fractional part of order for which J's or exponentially scaled J's (\(J\cdot e^{x}\)) are to be calculated. 0 <= alpha <
                    1.0.
                nb (int): integer number of functions to be calculated, nb > 0. The first function calculated is of order alpha, and the last is
                    of order nb - 1 + alpha.
        
            Returns:
                BesselJResult a vector of the functions \(J_{alpha}(x)\) through \(J_{nb-1+alpha}(x)\), or the corresponding
                exponentially scaled functions and an integer output variable indicating possible errors
        
        
        """
        ...
    @typing.overload
    def value(self, double: float) -> float: ...
    @typing.overload
    @staticmethod
    def value(double: float, double2: float) -> float: ...
    class BesselJResult:
        def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int): ...
        def getVals(self) -> typing.MutableSequence[float]: ...
        def getnVals(self) -> int: ...

class Beta:
    """
    public classBeta extends :class:`~org.hipparchus.special.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
    
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
            Returns the value of log B(p, q) for 0 ≤ x ≤ 1 and p, q > 0. Based on the *NSWC Library of Mathematics Subroutines*
            implementation, :code:`DBETLN`.
        
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
    """
    public classErf extends :class:`~org.hipparchus.special.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This is a utility class that provides computation methods related to the error functions.
    """
    _erf_2__T = typing.TypeVar('_erf_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _erf_3__T = typing.TypeVar('_erf_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erf(double: float) -> float:
        """
            Returns the error function. \[ \mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{t=0}^x e^{-t^2}dt \]
        
            This implementation computes erf(x) using the :meth:`~org.hipparchus.special.Gamma.regularizedGammaP`, following ` Erf
            <http://mathworld.wolfram.com/Erf.html>`, equation (3)
        
            The value returned is always between -1 and 1 (inclusive). If :code:`abs(x) > 40`, then :code:`erf(x)` is
            indistinguishable from either 1 or -1 as a double, so the appropriate extreme value is returned.
        
            Parameters:
                x (double): the value.
        
            Returns:
                the error function erf(x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.Gamma.regularizedGammaP`
        
        
            Returns the difference between erf(x1) and erf(x2).
        
            The implementation uses either erf(double) or erfc(double) depending on which provides the most precise result.
        
            Parameters:
                x1 (double): the first value
                x2 (double): the second value
        
            Returns:
                erf(x2) - erf(x1)
        
        """
        ...
    @typing.overload
    @staticmethod
    def erf(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def erf(t: _erf_2__T) -> _erf_2__T:
        """
            Returns the error function. \[ \mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{t=0}^x e^{-t^2}dt \]
        
            This implementation computes erf(x) using the :meth:`~org.hipparchus.special.Gamma.regularizedGammaP`, following ` Erf
            <http://mathworld.wolfram.com/Erf.html>`, equation (3)
        
            The value returned is always between -1 and 1 (inclusive). If :code:`abs(x) > 40`, then :code:`erf(x)` is
            indistinguishable from either 1 or -1 as a double, so the appropriate extreme value is returned.
        
            Parameters:
                x (T): the value.
        
            Returns:
                the error function erf(x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.Gamma.regularizedGammaP`
        
        
            Returns the difference between erf(x1) and erf(x2).
        
            The implementation uses either erf(double) or erfc(double) depending on which provides the most precise result.
        
            Parameters:
                x1 (T): the first value
                x2 (T): the second value
        
            Returns:
                erf(x2) - erf(x1)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def erf(t: _erf_3__T, t2: _erf_3__T) -> _erf_3__T: ...
    _erfInv_1__T = typing.TypeVar('_erfInv_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erfInv(double: float) -> float:
        """
            Returns the inverse erf.
        
            This implementation is described in the paper: `Approximating the erfinv function
            <http://people.maths.ox.ac.uk/gilesm/files/gems_erfinv.pdf>` by Mike Giles, Oxford-Man Institute of Quantitative
            Finance, which was published in GPU Computing Gems, volume 2, 2010. The source code is available `here
            <http://gpucomputing.net/?q=node/1828>`.
        
            Parameters:
                x (double): the value
        
            Returns:
                t such that x = erf(t)
        
        """
        ...
    @typing.overload
    @staticmethod
    def erfInv(t: _erfInv_1__T) -> _erfInv_1__T:
        """
            Returns the inverse erf.
        
            This implementation is described in the paper: `Approximating the erfinv function
            <http://people.maths.ox.ac.uk/gilesm/files/gems_erfinv.pdf>` by Mike Giles, Oxford-Man Institute of Quantitative
            Finance, which was published in GPU Computing Gems, volume 2, 2010. The source code is available `here
            <http://gpucomputing.net/?q=node/1828>`.
        
            Parameters:
                x (T): the value
        
            Returns:
                t such that x = erf(t)
        
        
        """
        ...
    _erfc_1__T = typing.TypeVar('_erfc_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erfc(double: float) -> float:
        """
            Returns the complementary error function. \[ \mathrm{erfc}(x) = \frac{2}{\sqrt{\pi}} \int_{t=x}^\infty e^{-t^2}dt = 1 -
            \mathrm{erf}
        
            This implementation computes erfc(x) using the :meth:`~org.hipparchus.special.Gamma.regularizedGammaQ`, following ` Erf
            <http://mathworld.wolfram.com/Erf.html>`, equation (3).
        
            The value returned is always between 0 and 2 (inclusive). If :code:`abs(x) > 40`, then :code:`erf(x)` is
            indistinguishable from either 0 or 2 as a double, so the appropriate extreme value is returned.
        
            Parameters:
                x (double): the value
        
            Returns:
                the complementary error function erfc(x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.Gamma.regularizedGammaQ`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def erfc(t: _erfc_1__T) -> _erfc_1__T:
        """
            Returns the complementary error function. \[ erfc(x) = \frac{2}{\sqrt{\pi}} \int_x^\infty e^{-t^2}dt = 1 - erf(x) \]
        
            This implementation computes erfc(x) using the :meth:`~org.hipparchus.special.Gamma.regularizedGammaQ`, following ` Erf
            <http://mathworld.wolfram.com/Erf.html>`, equation (3).
        
            The value returned is always between 0 and 2 (inclusive). If :code:`abs(x) > 40`, then :code:`erf(x)` is
            indistinguishable from either 0 or 2 as a double, so the appropriate extreme value is returned. **This implies that the
            current implementation does not allow the use of :class:`~org.hipparchus.dfp.Dfp` with extended precision.**
        
            Parameters:
                x (T): the value
        
            Returns:
                the complementary error function erfc(x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.Gamma.regularizedGammaQ`
        
        
        
        """
        ...
    _erfcInv_1__T = typing.TypeVar('_erfcInv_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erfcInv(double: float) -> float:
        """
            Returns the inverse erfc.
        
            Parameters:
                x (double): the value
        
            Returns:
                t such that x = erfc(t)
        
        """
        ...
    @typing.overload
    @staticmethod
    def erfcInv(t: _erfcInv_1__T) -> _erfcInv_1__T:
        """
            Returns the inverse erfc.
        
            Parameters:
                x (T): the value
        
            Returns:
                t such that x = erfc(t)
        
        
        """
        ...

class Gamma:
    """
    public classGamma extends :class:`~org.hipparchus.special.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
    
        This is a utility class that provides computation methods related to the Γ (Gamma) family of functions.
    
        Implementation of :meth:`~org.hipparchus.special.Gamma.invGamma1pm1` and
        :meth:`~org.hipparchus.special.Gamma.logGamma1p` is based on the algorithms described in
    
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
    GAMMA: typing.ClassVar[float] = ...
    """
    public static final double GAMMA
    
        `Euler-Mascheroni constant <http://en.wikipedia.org/wiki/Euler-Mascheroni_constant>`
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    LANCZOS_G: typing.ClassVar[float] = ...
    """
    public static final double LANCZOS_G
    
        The value of the :code:`g` constant in the Lanczos approximation, see :meth:`~org.hipparchus.special.Gamma.lanczos`.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    _digamma_1__T = typing.TypeVar('_digamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def digamma(double: float) -> float:
        """
        
            Computes the digamma function of x.
        
            This is an independently written implementation of the algorithm described in Jose Bernardo, Algorithm AS 103: Psi
            (Digamma) Function, Applied Statistics, 1976.
        
            Some of the constants have been changed to increase accuracy at the moderate expense of run-time. The result should be
            accurate to within 10^-8 absolute tolerance for x >= 10^-5 and within 10^-8 relative tolerance for x > 0.
        
            Performance for large negative values of x will be quite expensive (proportional to |x|). Accuracy for negative values
            of x should be about 10^-8 absolute for results less than 10^5 and 10^-8 relative for results larger than that.
        
            Parameters:
                x (double): Argument.
        
            Returns:
                digamma(x) to within 10-8 relative or absolute error whichever is smaller.
        
            Also see:
        
                  - `Digamma <http://en.wikipedia.org/wiki/Digamma_function>`
                  - `Bernardo's original article <http://www.uv.es/~bernardo/1976AppStatist.pdf>`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def digamma(t: _digamma_1__T) -> _digamma_1__T:
        """
        
            Computes the digamma function of x.
        
            This is an independently written implementation of the algorithm described in Jose Bernardo, Algorithm AS 103: Psi
            (Digamma) Function, Applied Statistics, 1976.
        
            Some of the constants have been changed to increase accuracy at the moderate expense of run-time. The result should be
            accurate to within 10^-8 absolute tolerance for x >= 10^-5 and within 10^-8 relative tolerance for x > 0.
        
            Performance for large negative values of x will be quite expensive (proportional to |x|). Accuracy for negative values
            of x should be about 10^-8 absolute for results less than 10^5 and 10^-8 relative for results larger than that.
        
            Parameters:
                x (T): Argument.
        
            Returns:
                digamma(x) to within 10-8 relative or absolute error whichever is smaller.
        
            Also see:
        
                  - `Digamma <http://en.wikipedia.org/wiki/Digamma_function>`
                  - `Bernardo's original article <http://www.uv.es/~bernardo/1976AppStatist.pdf>`
        
        
        
        """
        ...
    _gamma_1__T = typing.TypeVar('_gamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def gamma(double: float) -> float:
        """
            Returns the value of Γ(x). Based on the *NSWC Library of Mathematics Subroutines* double precision implementation,
            :code:`DGAMMA`.
        
            Parameters:
                x (double): Argument.
        
            Returns:
                the value of :code:`Gamma(x)`.
        
        """
        ...
    @typing.overload
    @staticmethod
    def gamma(t: _gamma_1__T) -> _gamma_1__T:
        """
            Returns the value of Γ(x). Based on the *NSWC Library of Mathematics Subroutines* double precision implementation,
            :code:`DGAMMA`.
        
            Parameters:
                x (T): Argument.
        
            Returns:
                the value of :code:`Gamma(x)`.
        
        
        """
        ...
    _invGamma1pm1_1__T = typing.TypeVar('_invGamma1pm1_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def invGamma1pm1(double: float) -> float:
        """
            Returns the value of 1 / Γ(1 + x) - 1 for -0.5 ≤ x ≤ 1.5. This implementation is based on the double precision
            implementation in the *NSWC Library of Mathematics Subroutines*, :code:`DGAM1`.
        
            Parameters:
                x (double): Argument.
        
            Returns:
                The value of :code:`1.0 / Gamma(1.0 + x) - 1.0`.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x < -0.5`
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x > 1.5`
        
        """
        ...
    @typing.overload
    @staticmethod
    def invGamma1pm1(t: _invGamma1pm1_1__T) -> _invGamma1pm1_1__T:
        """
            Returns the value of 1 / Γ(1 + x) - 1 for -0.5 ≤ x ≤ 1.5. This implementation is based on the double precision
            implementation in the *NSWC Library of Mathematics Subroutines*, :code:`DGAM1`.
        
            Parameters:
                x (T): Argument.
        
            Returns:
                The value of :code:`1.0 / Gamma(1.0 + x) - 1.0`.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x < -0.5`
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x > 1.5`
        
        
        """
        ...
    _lanczos_1__T = typing.TypeVar('_lanczos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def lanczos(double: float) -> float:
        """
        
            Returns the Lanczos approximation used to compute the gamma function. The Lanczos approximation is related to the Gamma
            function by the following equation \[ \Gamma(x) = \frac{\sqrt{2\pi}}{x} \times (x + g + \frac{1}{2}) ^ (x + \frac{1}{2})
            \times e^{-x - g - 0.5} \times \mathrm{lanczos}(x) \] where :code:`g` is the Lanczos constant.
        
            Parameters:
                x (double): Argument.
        
            Returns:
                The Lanczos approximation.
        
            Also see:
        
                  - `Lanczos Approximation <http://mathworld.wolfram.com/LanczosApproximation.html>` equations (1) through (5), and Paul
                    Godfrey's `Note on the computation of the convergent Lanczos complex Gamma approximation
                    <http://my.fit.edu/~gabdo/gamma.txt>`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def lanczos(t: _lanczos_1__T) -> _lanczos_1__T:
        """
        
            Returns the Lanczos approximation used to compute the gamma function. The Lanczos approximation is related to the Gamma
            function by the following equation \[ \Gamma(x) = \frac{\sqrt{2\pi}}{x} \times (x + g + \frac{1}{2}) ^ (x + \frac{1}{2})
            \times e^{-x - g - 0.5} \times \mathrm{lanczos}(x) \] where :code:`g` is the Lanczos constant.
        
            Parameters:
                x (T): Argument.
        
            Returns:
                The Lanczos approximation.
        
            Also see:
        
                  - `Lanczos Approximation <http://mathworld.wolfram.com/LanczosApproximation.html>` equations (1) through (5), and Paul
                    Godfrey's `Note on the computation of the convergent Lanczos complex Gamma approximation
                    <http://my.fit.edu/~gabdo/gamma.txt>`
        
        
        
        """
        ...
    _logGamma_1__T = typing.TypeVar('_logGamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def logGamma(double: float) -> float:
        """
        
            Returns the value of log &Gamma;(x) for x > 0.
        
            For x ≤ 8, the implementation is based on the double precision implementation in the *NSWC Library of Mathematics
            Subroutines*, :code:`DGAMLN`. For x > 8, the implementation is based on
        
              - `Gamma Function <http://mathworld.wolfram.com/GammaFunction.html>`, equation (28).
              - ` Lanczos Approximation <http://mathworld.wolfram.com/LanczosApproximation.html>`, equations (1) through (5).
              - `Paul Godfrey, A note on the computation of the convergent Lanczos complex Gamma approximation
                <http://my.fit.edu/~gabdo/gamma.txt>`
        
        
            Parameters:
                x (double): Argument.
        
            Returns:
                the value of :code:`log(Gamma(x))`, :code:`Double.NaN` if :code:`x <= 0.0`.
        
        """
        ...
    @typing.overload
    @staticmethod
    def logGamma(t: _logGamma_1__T) -> _logGamma_1__T:
        """
        
            Returns the value of log &Gamma;(x) for x > 0.
        
            For x ≤ 8, the implementation is based on the double precision implementation in the *NSWC Library of Mathematics
            Subroutines*, :code:`DGAMLN`. For x > 8, the implementation is based on
        
              - `Gamma Function <http://mathworld.wolfram.com/GammaFunction.html>`, equation (28).
              - ` Lanczos Approximation <http://mathworld.wolfram.com/LanczosApproximation.html>`, equations (1) through (5).
              - `Paul Godfrey, A note on the computation of the convergent Lanczos complex Gamma approximation
                <http://my.fit.edu/~gabdo/gamma.txt>`
        
        
            Parameters:
                x (T): Argument.
        
            Returns:
                the value of :code:`log(Gamma(x))`, :code:`Double.NaN` if :code:`x <= 0.0`.
        
        
        """
        ...
    _logGamma1p_1__T = typing.TypeVar('_logGamma1p_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def logGamma1p(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def logGamma1p(t: _logGamma1p_1__T) -> _logGamma1p_1__T: ...
    _regularizedGammaP_2__T = typing.TypeVar('_regularizedGammaP_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _regularizedGammaP_3__T = typing.TypeVar('_regularizedGammaP_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def regularizedGammaP(double: float, double2: float) -> float:
        """
            Returns the regularized gamma function P(a, x).
        
            Parameters:
                a (double): Parameter.
                x (double): Value.
        
            Returns:
                the regularized gamma function P(a, x).
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Returns the regularized gamma function P(a, x).
        
            The implementation of this method is based on:
        
              - ` Regularized Gamma Function <http://mathworld.wolfram.com/RegularizedGammaFunction.html>`, equation (1)
              - ` Incomplete Gamma Function <http://mathworld.wolfram.com/IncompleteGammaFunction.html>`, equation (4).
              - ` Confluent Hypergeometric Function of the First Kind
                <http://mathworld.wolfram.com/ConfluentHypergeometricFunctionoftheFirstKind.html>`, equation (1).
        
        
            Parameters:
                a (double): the a parameter.
                x (double): the value.
                epsilon (double): When the absolute value of the nth item in the series is less than epsilon the approximation ceases to calculate further
                    elements in the series.
                maxIterations (int): Maximum number of "iterations" to complete.
        
            Returns:
                the regularized gamma function P(a, x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
        """
        ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(double: float, double2: float, double3: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(t: _regularizedGammaP_2__T, t2: _regularizedGammaP_2__T) -> _regularizedGammaP_2__T:
        """
            Returns the regularized gamma function P(a, x).
        
            Parameters:
                a (T): Parameter.
                x (T): Value.
        
            Returns:
                the regularized gamma function P(a, x).
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Returns the regularized gamma function P(a, x).
        
            The implementation of this method is based on:
        
              - ` Regularized Gamma Function <http://mathworld.wolfram.com/RegularizedGammaFunction.html>`, equation (1)
              - ` Incomplete Gamma Function <http://mathworld.wolfram.com/IncompleteGammaFunction.html>`, equation (4).
              - ` Confluent Hypergeometric Function of the First Kind
                <http://mathworld.wolfram.com/ConfluentHypergeometricFunctionoftheFirstKind.html>`, equation (1).
        
        
            Parameters:
                a (T): the a parameter.
                x (T): the value.
                epsilon (double): When the absolute value of the nth item in the series is less than epsilon the approximation ceases to calculate further
                    elements in the series.
                maxIterations (int): Maximum number of "iterations" to complete.
        
            Returns:
                the regularized gamma function P(a, x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(t: _regularizedGammaP_3__T, t2: _regularizedGammaP_3__T, double: float, int: int) -> _regularizedGammaP_3__T: ...
    _regularizedGammaQ_2__T = typing.TypeVar('_regularizedGammaQ_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _regularizedGammaQ_3__T = typing.TypeVar('_regularizedGammaQ_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def regularizedGammaQ(double: float, double2: float) -> float:
        """
            Returns the regularized gamma function Q(a, x) = 1 - P(a, x).
        
            Parameters:
                a (double): the a parameter.
                x (double): the value.
        
            Returns:
                the regularized gamma function Q(a, x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Returns the regularized gamma function Q(a, x) = 1 - P(a, x).
        
            The implementation of this method is based on:
        
              - ` Regularized Gamma Function <http://mathworld.wolfram.com/RegularizedGammaFunction.html>`, equation (1).
              - ` Regularized incomplete gamma function: Continued fraction representations (formula 06.08.10.0003)
                <http://functions.wolfram.com/GammaBetaErf/GammaRegularized/10/0003/>`
        
        
            Parameters:
                a (double): the a parameter.
                x (double): the value.
                epsilon (double): When the absolute value of the nth item in the series is less than epsilon the approximation ceases to calculate further
                    elements in the series.
                maxIterations (int): Maximum number of "iterations" to complete.
        
            Returns:
                the regularized gamma function P(a, x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
        """
        ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(double: float, double2: float, double3: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(t: _regularizedGammaQ_2__T, t2: _regularizedGammaQ_2__T) -> _regularizedGammaQ_2__T:
        """
            Returns the regularized gamma function Q(a, x) = 1 - P(a, x).
        
            Parameters:
                a (T): the a parameter.
                x (T): the value.
        
            Returns:
                the regularized gamma function Q(a, x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
            Returns the regularized gamma function Q(a, x) = 1 - P(a, x).
        
            The implementation of this method is based on:
        
              - ` Regularized Gamma Function <http://mathworld.wolfram.com/RegularizedGammaFunction.html>`, equation (1).
              - ` Regularized incomplete gamma function: Continued fraction representations (formula 06.08.10.0003)
                <http://functions.wolfram.com/GammaBetaErf/GammaRegularized/10/0003/>`
        
        
            Parameters:
                a (T): the a parameter.
                x (T): the value.
                epsilon (double): When the absolute value of the nth item in the series is less than epsilon the approximation ceases to calculate further
                    elements in the series.
                maxIterations (int): Maximum number of "iterations" to complete.
        
            Returns:
                the regularized gamma function P(a, x)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the algorithm fails to converge.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(t: _regularizedGammaQ_3__T, t2: _regularizedGammaQ_3__T, double: float, int: int) -> _regularizedGammaQ_3__T: ...
    _trigamma_1__T = typing.TypeVar('_trigamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def trigamma(double: float) -> float:
        """
            Computes the trigamma function of x. This function is derived by taking the derivative of the implementation of digamma.
        
            Parameters:
                x (double): Argument.
        
            Returns:
                trigamma(x) to within 10-8 relative or absolute error whichever is smaller
        
            Also see:
        
                  - `Trigamma <http://en.wikipedia.org/wiki/Trigamma_function>`
                  - :meth:`~org.hipparchus.special.Gamma.digamma`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def trigamma(t: _trigamma_1__T) -> _trigamma_1__T:
        """
            Computes the trigamma function of x. This function is derived by taking the derivative of the implementation of digamma.
        
            Parameters:
                x (T): Argument.
        
            Returns:
                trigamma(x) to within 10-8 relative or absolute error whichever is smaller
        
            Also see:
        
                  - `Trigamma <http://en.wikipedia.org/wiki/Trigamma_function>`
                  - :meth:`~org.hipparchus.special.Gamma.digamma`
        
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special")``.

    BesselJ: typing.Type[BesselJ]
    Beta: typing.Type[Beta]
    Erf: typing.Type[Erf]
    Gamma: typing.Type[Gamma]
    elliptic: org.hipparchus.special.elliptic.__module_protocol__
