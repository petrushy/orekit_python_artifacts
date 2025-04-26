
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
    public classLegendreEllipticIntegral extends :class:`~org.hipparchus.special.elliptic.legendre.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Complete and incomplete elliptic integrals in Legendre form.
    
        The elliptic integrals are related to Jacobi elliptic functions.
    
        *Beware that when computing elliptic integrals in the complex plane, many issues arise due to branch cuts. See the
        :meth:`~org.hipparchus.special.elliptic.legendre.https:.www.hipparchus.org.hipparchus` for a thorough explanation.*
    
        There are different conventions to interpret the arguments of Legendre elliptic integrals. In mathematical texts, these
        conventions show up using the separator between arguments. So for example for the incomplete integral of the first kind
        F we have:
    
          - F(φ, k): the first argument φ is an angle and the second argument k is the elliptic modulus: this is the trigonometric
            form of the integral
          - F(φ; m): the first argument φ is an angle and the second argument m=k² is the parameter: this is also a trigonometric
            form of the integral
          - F(x|m): the first argument x=sin(φ) is not an angle anymore and the second argument m=k² is the parameter: this is the
            Legendre form
          - F(φ\α): the first argument φ is an angle and the second argument α is the modular angle
    
    
        As we have no separator in a method call, we have to adopt one convention and stick to it. In Hipparchus, we adopted the
        Legendre form (i.e. F(x|m), with x=sin(φ) and m=k². These conventions are consistent with Wolfram Alpha functions
        EllipticF, EllipticE, ElliptiPI…
    
        Since:
            2.0
    
        Also see:
    
              - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
              - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
              - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheSecondKind`
              - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheFirstKind`
              - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheSecondKind`
              - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
    """
    _bigD_2__T = typing.TypeVar('_bigD_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_3__T = typing.TypeVar('_bigD_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_6__T = typing.TypeVar('_bigD_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_7__T = typing.TypeVar('_bigD_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigD(double: float) -> float:
        """
            Get the complete elliptic integral D(m) = [K(m) - E(m)]/m.
        
            The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral D(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
            Get the complete elliptic integral D(m) = [K(m) - E(m)]/m.
        
            The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral D(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
            Get the incomplete elliptic integral D(φ, m) = [F(φ, m) - E(φ, m)]/m.
        
            The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (double): amplitude (i.e. upper bound of the integral)
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral D(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
            Get the incomplete elliptic integral D(φ, m) = [F(φ, m) - E(φ, m)]/m.
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.Complex`): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral D(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigD(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigD(t: _bigD_2__T) -> _bigD_2__T:
        """
            Get the complete elliptic integral D(m) = [K(m) - E(m)]/m.
        
            The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral D(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
            Get the complete elliptic integral D(m) = [K(m) - E(m)]/m.
        
            The complete elliptic integral D(m) is \[ \int_0^{\frac{\pi}{2}} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral D(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
            Get the incomplete elliptic integral D(φ, m) = [F(φ, m) - E(φ, m)]/m.
        
            The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (T): amplitude (i.e. upper bound of the integral)
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral D(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigD(t: _bigD_3__T, t2: _bigD_3__T) -> _bigD_3__T:
        """
            Get the incomplete elliptic integral D(φ, m) = [F(φ, m) - E(φ, m)]/m.
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral D(φ, m) is \[ \int_0^{\phi} \frac{\sin^2\theta}{\sqrt{1-m \sin^2\theta}} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.FieldComplex`<T> phi): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral D(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigD`
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigD(complex: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigD(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigD(fieldComplex: org.hipparchus.complex.FieldComplex[_bigD_6__T]) -> org.hipparchus.complex.FieldComplex[_bigD_6__T]: ...
    @typing.overload
    @staticmethod
    def bigD(fieldComplex: org.hipparchus.complex.FieldComplex[_bigD_7__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigD_7__T]) -> org.hipparchus.complex.FieldComplex[_bigD_7__T]: ...
    _bigE_2__T = typing.TypeVar('_bigE_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_3__T = typing.TypeVar('_bigE_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_7__T = typing.TypeVar('_bigE_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_8__T = typing.TypeVar('_bigE_8__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigE_9__T = typing.TypeVar('_bigE_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigE(double: float) -> float:
        """
            Get the complete elliptic integral of the second kind E(m).
        
            The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the second kind E(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the second kind E(m).
        
            The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the second kind E(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the second kind E(φ, m).
        
            The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (double): amplitude (i.e. upper bound of the integral)
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the second kind E(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the second kind E(φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.Complex`): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the second kind E(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the second kind E(φ, m) using numerical integration.
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a
            pole of the integrand, then integration will fail with a :class:`~org.hipparchus.exception.MathIllegalStateException`
            even for very large :code:`maxEval`. This is normal behavior.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.Complex`): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
                integrator (:class:`~org.hipparchus.complex.ComplexUnivariateIntegrator`): integrator to use
                maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                    used)
        
            Returns:
                incomplete elliptic integral of the second kind E(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigE(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigE(t: _bigE_2__T) -> _bigE_2__T:
        """
            Get the complete elliptic integral of the second kind E(m).
        
            The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the second kind E(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the second kind E(m).
        
            The complete elliptic integral of the second kind E(m) is \[ \int_0^{\frac{\pi}{2}} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the second kind E(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the second kind E(φ, m).
        
            The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (T): amplitude (i.e. upper bound of the integral)
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the second kind E(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigE(t: _bigE_3__T, t2: _bigE_3__T) -> _bigE_3__T:
        """
            Get the incomplete elliptic integral of the second kind E(φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.FieldComplex`<T> phi): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the second kind E(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigE(complex: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigE(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigE(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complexUnivariateIntegrator: org.hipparchus.complex.ComplexUnivariateIntegrator, int: int) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigE(fieldComplex: org.hipparchus.complex.FieldComplex[_bigE_7__T]) -> org.hipparchus.complex.FieldComplex[_bigE_7__T]: ...
    @typing.overload
    @staticmethod
    def bigE(fieldComplex: org.hipparchus.complex.FieldComplex[_bigE_8__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigE_8__T]) -> org.hipparchus.complex.FieldComplex[_bigE_8__T]: ...
    @typing.overload
    @staticmethod
    def bigE(fieldComplex: org.hipparchus.complex.FieldComplex[_bigE_9__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigE_9__T], fieldComplexUnivariateIntegrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigE_9__T], int: int) -> org.hipparchus.complex.FieldComplex[_bigE_9__T]:
        """
            Get the incomplete elliptic integral of the second kind E(φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the second kind E(φ, m) is \[ \int_0^{\phi} \sqrt{1-m \sin^2\theta} d\theta \]
        
            The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a
            pole of the integrand, then integration will fail with a :class:`~org.hipparchus.exception.MathIllegalStateException`
            even for very large :code:`maxEval`. This is normal behavior.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.FieldComplex`<T> phi): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
                integrator (:class:`~org.hipparchus.complex.FieldComplexUnivariateIntegrator`<T> integrator): integrator to use
                maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                    used)
        
            Returns:
                incomplete elliptic integral of the second kind E(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigE`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheSecondKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        
        """
        ...
    _bigF_1__T = typing.TypeVar('_bigF_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigF_4__T = typing.TypeVar('_bigF_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigF_5__T = typing.TypeVar('_bigF_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigF(double: float, double2: float) -> float:
        """
            Get the incomplete elliptic integral of the first kind F(φ, m).
        
            The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}}
            \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (double): amplitude (i.e. upper bound of the integral)
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the first kind F(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the first kind F(φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}}
            \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.Complex`): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the first kind F(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the first kind F(φ, m) using numerical integration.
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}}
            \]
        
            The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a
            pole of the integrand, then integration will fail with a :class:`~org.hipparchus.exception.MathIllegalStateException`
            even for very large :code:`maxEval`. This is normal behavior.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.Complex`): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
                integrator (:class:`~org.hipparchus.complex.ComplexUnivariateIntegrator`): integrator to use
                maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                    used)
        
            Returns:
                incomplete elliptic integral of the first kind F(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigF(t: _bigF_1__T, t2: _bigF_1__T) -> _bigF_1__T:
        """
            Get the incomplete elliptic integral of the first kind F(φ, m).
        
            The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}}
            \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (T): amplitude (i.e. upper bound of the integral)
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the first kind F(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the first kind F(φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}}
            \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.FieldComplex`<T> phi): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the first kind F(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigF(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigF(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complexUnivariateIntegrator: org.hipparchus.complex.ComplexUnivariateIntegrator, int: int) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigF(fieldComplex: org.hipparchus.complex.FieldComplex[_bigF_4__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigF_4__T]) -> org.hipparchus.complex.FieldComplex[_bigF_4__T]: ...
    @typing.overload
    @staticmethod
    def bigF(fieldComplex: org.hipparchus.complex.FieldComplex[_bigF_5__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigF_5__T], fieldComplexUnivariateIntegrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigF_5__T], int: int) -> org.hipparchus.complex.FieldComplex[_bigF_5__T]:
        """
            Get the incomplete elliptic integral of the first kind F(φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the first kind F(φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m \sin^2\theta}}
            \]
        
            The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a
            pole of the integrand, then integration will fail with a :class:`~org.hipparchus.exception.MathIllegalStateException`
            even for very large :code:`maxEval`. This is normal behavior.
        
            Parameters:
                phi (:class:`~org.hipparchus.complex.FieldComplex`<T> phi): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
                integrator (:class:`~org.hipparchus.complex.FieldComplexUnivariateIntegrator`<T> integrator): integrator to use
                maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                    used)
        
            Returns:
                incomplete elliptic integral of the first kind F(φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        
        """
        ...
    _bigK_1__T = typing.TypeVar('_bigK_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigK_3__T = typing.TypeVar('_bigK_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigK(double: float) -> float:
        """
            Get the complete elliptic integral of the first kind K(m).
        
            The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigKPrime`
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigF`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the first kind K(m).
        
            The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigKPrime`
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigF`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigK(t: _bigK_1__T) -> _bigK_1__T:
        """
            Get the complete elliptic integral of the first kind K(m).
        
            The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigKPrime`
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigF`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the first kind K(m).
        
            The complete elliptic integral of the first kind K(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}} \] it corresponds to the real quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigKPrime`
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigF`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigK(complex: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigK(fieldComplex: org.hipparchus.complex.FieldComplex[_bigK_3__T]) -> org.hipparchus.complex.FieldComplex[_bigK_3__T]: ...
    _bigKPrime_1__T = typing.TypeVar('_bigKPrime_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigKPrime_3__T = typing.TypeVar('_bigKPrime_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigKPrime(double: float) -> float:
        """
            Get the complete elliptic integral of the first kind K'(m).
        
            The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m)
            \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K'(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the first kind K'(m).
        
            The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m)
            \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K'(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigKPrime(t: _bigKPrime_1__T) -> _bigKPrime_1__T:
        """
            Get the complete elliptic integral of the first kind K'(m).
        
            The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m)
            \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K'(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the first kind K'(m).
        
            The complete elliptic integral of the first kind K'(m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-(1-m)
            \sin^2\theta}} \] it corresponds to the imaginary quarter-period of Jacobi elliptic functions
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the first kind K'(m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigK`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.CompleteEllipticIntegraloftheFirstKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigKPrime(complex: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigKPrime(fieldComplex: org.hipparchus.complex.FieldComplex[_bigKPrime_3__T]) -> org.hipparchus.complex.FieldComplex[_bigKPrime_3__T]: ...
    _bigPi_2__T = typing.TypeVar('_bigPi_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_3__T = typing.TypeVar('_bigPi_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_7__T = typing.TypeVar('_bigPi_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_8__T = typing.TypeVar('_bigPi_8__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigPi_9__T = typing.TypeVar('_bigPi_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigPi(double: float, double2: float) -> float:
        """
            Get the complete elliptic integral of the third kind Π(n, m).
        
            The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (double): elliptic characteristic
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the third kind Π(n, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the third kind Π(n, m).
        
            The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (:class:`~org.hipparchus.complex.Complex`): elliptic characteristic
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the third kind Π(n, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
            The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (double): elliptic characteristic
                phi (double): amplitude (i.e. upper bound of the integral)
                m (double): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the third kind Π(n, φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (:class:`~org.hipparchus.complex.Complex`): elliptic characteristic
                phi (:class:`~org.hipparchus.complex.Complex`): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the third kind Π(n, φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the third kind Π(n, φ, m) using numerical integration.
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a
            pole of the integrand, then integration will fail with a :class:`~org.hipparchus.exception.MathIllegalStateException`
            even for very large :code:`maxEval`. This is normal behavior.
        
            Parameters:
                n (:class:`~org.hipparchus.complex.Complex`): elliptic characteristic
                phi (:class:`~org.hipparchus.complex.Complex`): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.Complex`): parameter (m=k² where k is the elliptic modulus)
                integrator (:class:`~org.hipparchus.complex.ComplexUnivariateIntegrator`): integrator to use
                maxEval (int): maximum number of evaluations (real and imaginary
        
            Returns:
                incomplete elliptic integral of the third kind Π(n, φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigPi(double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigPi(t: _bigPi_2__T, t2: _bigPi_2__T) -> _bigPi_2__T:
        """
            Get the complete elliptic integral of the third kind Π(n, m).
        
            The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (T): elliptic characteristic
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the third kind Π(n, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the complete elliptic integral of the third kind Π(n, m).
        
            The complete elliptic integral of the third kind Π(n, m) is \[ \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (:class:`~org.hipparchus.complex.FieldComplex`<T> n): elliptic characteristic
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                complete elliptic integral of the third kind Π(n, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
            Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
            The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (T): elliptic characteristic
                phi (T): amplitude (i.e. upper bound of the integral)
                m (T): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the third kind Π(n, φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigPi(t: _bigPi_3__T, t2: _bigPi_3__T, t3: _bigPi_3__T) -> _bigPi_3__T:
        """
            Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on
            :class:`~org.hipparchus.special.elliptic.carlson.CarlsonEllipticIntegral`.
        
            Parameters:
                n (:class:`~org.hipparchus.complex.FieldComplex`<T> n): elliptic characteristic
                phi (:class:`~org.hipparchus.complex.FieldComplex`<T> phi): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
        
            Returns:
                incomplete elliptic integral of the third kind Π(n, φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def bigPi(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigPi(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complex3: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigPi(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complex3: org.hipparchus.complex.Complex, complexUnivariateIntegrator: org.hipparchus.complex.ComplexUnivariateIntegrator, int: int) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def bigPi(fieldComplex: org.hipparchus.complex.FieldComplex[_bigPi_7__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigPi_7__T]) -> org.hipparchus.complex.FieldComplex[_bigPi_7__T]: ...
    @typing.overload
    @staticmethod
    def bigPi(fieldComplex: org.hipparchus.complex.FieldComplex[_bigPi_8__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigPi_8__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_bigPi_8__T]) -> org.hipparchus.complex.FieldComplex[_bigPi_8__T]: ...
    @typing.overload
    @staticmethod
    def bigPi(fieldComplex: org.hipparchus.complex.FieldComplex[_bigPi_9__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigPi_9__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_bigPi_9__T], fieldComplexUnivariateIntegrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigPi_9__T], int: int) -> org.hipparchus.complex.FieldComplex[_bigPi_9__T]:
        """
            Get the incomplete elliptic integral of the third kind Π(n, φ, m).
        
            *BEWARE! Elliptic integrals for complex numbers in the incomplete case are considered experimental for now, they have
            known issues.*
        
            The incomplete elliptic integral of the third kind Π(n, φ, m) is \[ \int_0^{\phi} \frac{d\theta}{\sqrt{1-m
            \sin^2\theta}(1-n \sin^2\theta)} \]
        
            The algorithm for evaluating the functions is based on numerical integration. If integration path comes too close to a
            pole of the integrand, then integration will fail with a :class:`~org.hipparchus.exception.MathIllegalStateException`
            even for very large :code:`maxEval`. This is normal behavior.
        
            Parameters:
                n (:class:`~org.hipparchus.complex.FieldComplex`<T> n): elliptic characteristic
                phi (:class:`~org.hipparchus.complex.FieldComplex`<T> phi): amplitude (i.e. upper bound of the integral)
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter (m=k² where k is the elliptic modulus)
                integrator (:class:`~org.hipparchus.complex.FieldComplexUnivariateIntegrator`<T> integrator): integrator to use
                maxEval (int): maximum number of evaluations (real and imaginary parts are evaluated separately, so up to twice this number may be
                    used)
        
            Returns:
                incomplete elliptic integral of the third kind Π(n, φ, m)
        
            Also see:
        
                  - :meth:`~org.hipparchus.special.elliptic.legendre.LegendreEllipticIntegral.bigPi`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.mathworld.wolfram.com.EllipticIntegraloftheThirdKind`
                  - :class:`~org.hipparchus.special.elliptic.legendre.https:.en.wikipedia.org.wiki.Elliptic_integral`
        
        
        
        """
        ...
    _nome_1__T = typing.TypeVar('_nome_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def nome(double: float) -> float:
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
    def nome(t: _nome_1__T) -> _nome_1__T:
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
