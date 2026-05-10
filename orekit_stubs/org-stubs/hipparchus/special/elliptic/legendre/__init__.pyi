
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.hipparchus.complex
import typing



class LegendreEllipticIntegral:
    """
    Complete and incomplete elliptic integrals in Legendre form.
    
    The elliptic integrals are related to Jacobi elliptic functions.
    
    Beware that when computing elliptic integrals in the complex plane, many issues arise due to branch cuts. See the hipparchus for a thorough explanation.
    
    There are different conventions to interpret the arguments of Legendre elliptic integrals. In mathematical texts, these conventions show up using the separator between arguments. So for example for the incomplete integral of the first kind F we have:
    
      - F(φ, k): the first argument φ is an angle and the second argument k is the elliptic modulus: this is the trigonometric
        form of the integral
      - F(φ; m): the first argument φ is an angle and the second argument m=k² is the parameter: this is also a trigonometric
        form of the integral
      - F(x|m): the first argument x=sin(φ) is not an angle anymore and the second argument m=k² is the parameter: this is the
        Legendre form
      - F(φ\α): the first argument φ is an angle and the second argument α is the modular angle
    
    As we have no separator in a method call, we have to adopt one convention and stick to it. In Hipparchus, we adopted the Legendre form (i.e. F(x|m), with x=sin(φ) and m=k². These conventions are consistent with Wolfram Alpha functions EllipticF, EllipticE, ElliptiPI…
    
    Since:
        2.0
    
    Also see:
        Elliptic_integral,
        CompleteEllipticIntegraloftheFirstKind,
        CompleteEllipticIntegraloftheSecondKind,
        EllipticIntegraloftheFirstKind,
        EllipticIntegraloftheSecondKind,
        EllipticIntegraloftheThirdKind
    """
    _bigD_2__T = typing.TypeVar('_bigD_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_3__T = typing.TypeVar('_bigD_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_6__T = typing.TypeVar('_bigD_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_7__T = typing.TypeVar('_bigD_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigD(m: float) -> float:
        """
        The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral D(m)
        
        Also see:
            bigD
        
        Get the complete elliptic integral D(m) = [K(m) - E(m)]/m.
        
        The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral D(m)
        
        Also see:
            bigD
        
        Get the incomplete elliptic integral D(φ, m) = [F(φ, m) - E(φ, m)]/m.
        
        The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (double): amplitude (i.e. upper bound of the integral)
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral D(φ, m)
        
        Also see:
            bigD
        
        Get the incomplete elliptic integral D(φ, m) = [F(φ, m) - E(φ, m)]/m.
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (Complex): amplitude (i.e. upper bound of the integral)
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral D(φ, m)
        
        Also see:
            bigD
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigD(phi: float, m: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigD(m: _bigD_2__T) -> _bigD_2__T:
        """
        The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral D(m)
        
        Also see:
            bigD
        
        Get the complete elliptic integral D(m) = [K(m) - E(m)]/m.
        
        The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral D(m)
        
        Also see:
            bigD
        
        Get the incomplete elliptic integral D(φ, m) = [F(φ, m) - E(φ, m)]/m.
        
        The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (T): amplitude (i.e. upper bound of the integral)
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral D(φ, m)
        
        Also see:
            bigD
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigD(phi: _bigD_3__T, m: _bigD_3__T) -> _bigD_3__T:
        """
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (FieldComplex<T> phi): amplitude (i.e. upper bound of the integral)
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral D(φ, m)
        
        Also see:
            bigD
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigD(m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigD(phi: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigD(m: org.hipparchus.complex.FieldComplex[_bigD_6__T]) -> org.hipparchus.complex.FieldComplex[_bigD_6__T]: ...
    @typing.overload
    @staticmethod
    def bigD(phi: org.hipparchus.complex.FieldComplex[_bigD_7__T], m: org.hipparchus.complex.FieldComplex[_bigD_7__T]) -> org.hipparchus.complex.FieldComplex[_bigD_7__T]: ...
    _bigE_2__T = typing.TypeVar('_bigE_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_3__T = typing.TypeVar('_bigE_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_7__T = typing.TypeVar('_bigE_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_8__T = typing.TypeVar('_bigE_8__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_9__T = typing.TypeVar('_bigE_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigE(m: float) -> float:
        """
        The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the second kind E(m)
        
        Also see:
            bigE,
            CompleteEllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the second kind E(m).
        
        The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the second kind E(m)
        
        Also see:
            bigE,
            CompleteEllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the second kind E(φ, m).
        
        The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (double): amplitude (i.e. upper bound of the integral)
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the second kind E(φ, m)
        
        Also see:
            bigE,
            EllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the second kind E(φ, m).
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (Complex): amplitude (i.e. upper bound of the integral)
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the second kind E(φ, m)
        
        Also see:
            bigE,
            EllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the second kind E(φ, m) using numerical integration.
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a pole of the integrand, then integration will fail with a MathIllegalStateException even for very large maxEval. This is normal behavior.
        
        Parameters:
            phi (Complex): amplitude (i.e. upper bound of the integral)
            m (Complex): parameter (m=k² where k is the elliptic modulus)
            integrator (ComplexUnivariateIntegrator): integrator to use
            maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                used)
        
        Returns:
            incomplete elliptic integral of the second kind E(φ, m)
        
        Also see:
            bigE,
            EllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigE(phi: float, m: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigE(m: _bigE_2__T) -> _bigE_2__T:
        """
        The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the second kind E(m)
        
        Also see:
            bigE,
            CompleteEllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the second kind E(m).
        
        The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the second kind E(m)
        
        Also see:
            bigE,
            CompleteEllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the second kind E(φ, m).
        
        The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (T): amplitude (i.e. upper bound of the integral)
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the second kind E(φ, m)
        
        Also see:
            bigE,
            EllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigE(phi: _bigE_3__T, m: _bigE_3__T) -> _bigE_3__T:
        """
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (FieldComplex<T> phi): amplitude (i.e. upper bound of the integral)
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the second kind E(φ, m)
        
        Also see:
            bigE,
            EllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigE(m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigE(phi: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigE(phi: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex, integrator: org.hipparchus.complex.ComplexUnivariateIntegrator, maxEval: int) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigE(m: org.hipparchus.complex.FieldComplex[_bigE_7__T]) -> org.hipparchus.complex.FieldComplex[_bigE_7__T]: ...
    @typing.overload
    @staticmethod
    def bigE(phi: org.hipparchus.complex.FieldComplex[_bigE_8__T], m: org.hipparchus.complex.FieldComplex[_bigE_8__T]) -> org.hipparchus.complex.FieldComplex[_bigE_8__T]: ...
    @typing.overload
    @staticmethod
    def bigE(phi: org.hipparchus.complex.FieldComplex[_bigE_9__T], m: org.hipparchus.complex.FieldComplex[_bigE_9__T], integrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigE_9__T], maxEval: int) -> org.hipparchus.complex.FieldComplex[_bigE_9__T]:
        """
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
        The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a pole of the integrand, then integration will fail with a MathIllegalStateException even for very large maxEval. This is normal behavior.
        
        Parameters:
            phi (FieldComplex<T> phi): amplitude (i.e. upper bound of the integral)
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
            integrator (FieldComplexUnivariateIntegrator<T> integrator): integrator to use
            maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                used)
        
        Returns:
            incomplete elliptic integral of the second kind E(φ, m)
        
        Also see:
            bigE,
            EllipticIntegraloftheSecondKind,
            Elliptic_integral
        
        
        """
        ...
    _bigF_1__T = typing.TypeVar('_bigF_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigF_4__T = typing.TypeVar('_bigF_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigF_5__T = typing.TypeVar('_bigF_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigF(phi: float, m: float) -> float:
        """
        The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (double): amplitude (i.e. upper bound of the integral)
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the first kind F(φ, m)
        
        Also see:
            bigK,
            EllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the first kind F(φ, m).
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (Complex): amplitude (i.e. upper bound of the integral)
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the first kind F(φ, m)
        
        Also see:
            bigK,
            EllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the first kind F(φ, m) using numerical integration.
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \]
        
        The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a pole of the integrand, then integration will fail with a MathIllegalStateException even for very large maxEval. This is normal behavior.
        
        Parameters:
            phi (Complex): amplitude (i.e. upper bound of the integral)
            m (Complex): parameter (m=k² where k is the elliptic modulus)
            integrator (ComplexUnivariateIntegrator): integrator to use
            maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                used)
        
        Returns:
            incomplete elliptic integral of the first kind F(φ, m)
        
        Also see:
            bigK,
            EllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigF(phi: _bigF_1__T, m: _bigF_1__T) -> _bigF_1__T:
        """
        The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (T): amplitude (i.e. upper bound of the integral)
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the first kind F(φ, m)
        
        Also see:
            bigK,
            EllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the first kind F(φ, m).
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            phi (FieldComplex<T> phi): amplitude (i.e. upper bound of the integral)
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the first kind F(φ, m)
        
        Also see:
            bigK,
            EllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigF(phi: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigF(phi: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex, integrator: org.hipparchus.complex.ComplexUnivariateIntegrator, maxEval: int) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigF(phi: org.hipparchus.complex.FieldComplex[_bigF_4__T], m: org.hipparchus.complex.FieldComplex[_bigF_4__T]) -> org.hipparchus.complex.FieldComplex[_bigF_4__T]: ...
    @typing.overload
    @staticmethod
    def bigF(phi: org.hipparchus.complex.FieldComplex[_bigF_5__T], m: org.hipparchus.complex.FieldComplex[_bigF_5__T], integrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigF_5__T], maxEval: int) -> org.hipparchus.complex.FieldComplex[_bigF_5__T]:
        """
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \]
        
        The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a pole of the integrand, then integration will fail with a MathIllegalStateException even for very large maxEval. This is normal behavior.
        
        Parameters:
            phi (FieldComplex<T> phi): amplitude (i.e. upper bound of the integral)
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
            integrator (FieldComplexUnivariateIntegrator<T> integrator): integrator to use
            maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                used)
        
        Returns:
            incomplete elliptic integral of the first kind F(φ, m)
        
        Also see:
            bigK,
            EllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        
        """
        ...
    _bigK_1__T = typing.TypeVar('_bigK_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigK_3__T = typing.TypeVar('_bigK_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigK(m: float) -> float:
        """
        The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K(m)
        
        Also see:
            bigKPrime,
            bigF,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the first kind K(m).
        
        The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K(m)
        
        Also see:
            bigKPrime,
            bigF,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigK(m: _bigK_1__T) -> _bigK_1__T:
        """
        The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K(m)
        
        Also see:
            bigKPrime,
            bigF,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the first kind K(m).
        
        The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K(m)
        
        Also see:
            bigKPrime,
            bigF,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigK(m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigK(m: org.hipparchus.complex.FieldComplex[_bigK_3__T]) -> org.hipparchus.complex.FieldComplex[_bigK_3__T]: ...
    _bigKPrime_1__T = typing.TypeVar('_bigKPrime_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigKPrime_3__T = typing.TypeVar('_bigKPrime_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigKPrime(m: float) -> float:
        """
        Get the complete elliptic integral of the first kind K'(m).
        
        The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m) \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K'(m)
        
        Also see:
            bigK,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the first kind K'(m).
        
        The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m) \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K'(m)
        
        Also see:
            bigK,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigKPrime(m: _bigKPrime_1__T) -> _bigKPrime_1__T:
        """
        Get the complete elliptic integral of the first kind K'(m).
        
        The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m) \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K'(m)
        
        Also see:
            bigK,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the first kind K'(m).
        
        The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m) \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the first kind K'(m)
        
        Also see:
            bigK,
            CompleteEllipticIntegraloftheFirstKind,
            Elliptic_integral
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigKPrime(m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigKPrime(m: org.hipparchus.complex.FieldComplex[_bigKPrime_3__T]) -> org.hipparchus.complex.FieldComplex[_bigKPrime_3__T]: ...
    _bigPi_2__T = typing.TypeVar('_bigPi_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_3__T = typing.TypeVar('_bigPi_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_7__T = typing.TypeVar('_bigPi_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_8__T = typing.TypeVar('_bigPi_8__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_9__T = typing.TypeVar('_bigPi_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigPi(n: float, m: float) -> float:
        """
        The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (double): elliptic characteristic
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the third kind Π(n, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the third kind Π(n, m).
        
        The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (Complex): elliptic characteristic
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the third kind Π(n, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
        The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (double): elliptic characteristic
            phi (double): amplitude (i.e. upper bound of the integral)
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the third kind Π(n, φ, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (Complex): elliptic characteristic
            phi (Complex): amplitude (i.e. upper bound of the integral)
            m (Complex): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the third kind Π(n, φ, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the third kind Π(n, φ, m) using numerical integration.
        
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a pole of the integrand, then integration will fail with a MathIllegalStateException even for very large maxEval. This is normal behavior.
        
        Parameters:
            n (Complex): elliptic characteristic
            phi (Complex): amplitude (i.e. upper bound of the integral)
            m (Complex): parameter (m=k² where k is the elliptic modulus)
            integrator (ComplexUnivariateIntegrator): integrator to use
            maxEval (int): maximum number of evaluations (real and imaginary
        
        Returns:
            incomplete elliptic integral of the third kind Π(n, φ, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigPi(n: float, phi: float, m: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigPi(n: _bigPi_2__T, m: _bigPi_2__T) -> _bigPi_2__T:
        """
        The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (T): elliptic characteristic
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the third kind Π(n, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        Get the complete elliptic integral of the third kind Π(n, m).
        
        The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (FieldComplex<T> n): elliptic characteristic
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            complete elliptic integral of the third kind Π(n, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
        The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (T): elliptic characteristic
            phi (T): amplitude (i.e. upper bound of the integral)
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the third kind Π(n, φ, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigPi(n: _bigPi_3__T, phi: _bigPi_3__T, m: _bigPi_3__T) -> _bigPi_3__T:
        """
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on CarlsonEllipticIntegral.
        
        Parameters:
            n (FieldComplex<T> n): elliptic characteristic
            phi (FieldComplex<T> phi): amplitude (i.e. upper bound of the integral)
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            incomplete elliptic integral of the third kind Π(n, φ, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigPi(n: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigPi(n: org.hipparchus.complex.Complex, phi: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigPi(n: org.hipparchus.complex.Complex, phi: org.hipparchus.complex.Complex, m: org.hipparchus.complex.Complex, integrator: org.hipparchus.complex.ComplexUnivariateIntegrator, maxEval: int) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigPi(n: org.hipparchus.complex.FieldComplex[_bigPi_7__T], m: org.hipparchus.complex.FieldComplex[_bigPi_7__T]) -> org.hipparchus.complex.FieldComplex[_bigPi_7__T]: ...
    @typing.overload
    @staticmethod
    def bigPi(n: org.hipparchus.complex.FieldComplex[_bigPi_8__T], phi: org.hipparchus.complex.FieldComplex[_bigPi_8__T], m: org.hipparchus.complex.FieldComplex[_bigPi_8__T]) -> org.hipparchus.complex.FieldComplex[_bigPi_8__T]: ...
    @typing.overload
    @staticmethod
    def bigPi(n: org.hipparchus.complex.FieldComplex[_bigPi_9__T], phi: org.hipparchus.complex.FieldComplex[_bigPi_9__T], m: org.hipparchus.complex.FieldComplex[_bigPi_9__T], integrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigPi_9__T], maxEval: int) -> org.hipparchus.complex.FieldComplex[_bigPi_9__T]:
        """
        BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have known issues.
        
        The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}(1-n \sin^2\theta)} \]
        
        The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a pole of the integrand, then integration will fail with a MathIllegalStateException even for very large maxEval. This is normal behavior.
        
        Parameters:
            n (FieldComplex<T> n): elliptic characteristic
            phi (FieldComplex<T> phi): amplitude (i.e. upper bound of the integral)
            m (FieldComplex<T> m): parameter (m=k² where k is the elliptic modulus)
            integrator (FieldComplexUnivariateIntegrator<T> integrator): integrator to use
            maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                used)
        
        Returns:
            incomplete elliptic integral of the third kind Π(n, φ, m)
        
        Also see:
            bigPi,
            EllipticIntegraloftheThirdKind,
            Elliptic_integral
        
        
        """
        ...
    _nome_1__T = typing.TypeVar('_nome_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def nome(m: float) -> float:
        """
        Get the nome q.
        
        Parameters:
            m (double): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            nome q
        
        """
        ...
    @typing.overload
    @staticmethod
    def nome(m: _nome_1__T) -> _nome_1__T:
        """
        Get the nome q.
        
        Parameters:
            m (T): parameter (m=k² where k is the elliptic modulus)
        
        Returns:
            nome q
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special.elliptic.legendre")``.

    LegendreEllipticIntegral: typing.Type[LegendreEllipticIntegral]
