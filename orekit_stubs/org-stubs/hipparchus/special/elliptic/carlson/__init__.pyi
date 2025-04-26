
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.hipparchus.complex
import typing



class CarlsonEllipticIntegral:
    """
    public classCarlsonEllipticIntegral extends :class:`~org.hipparchus.special.elliptic.carlson.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Elliptic integrals in Carlson symmetric form.
    
        This utility class computes the various symmetric elliptic integrals defined as: \[ \left\{\begin{align} R_F(x,y,z) &=
        \frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{s(t)}\\ R_J(x,y,z,p) &=
        \frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{s(t)(t+p)}\\ R_G(x,y,z) &= \frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)}
        \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t\\ R_D(x,y,z) &= R_J(x,y,z,z)\\ R_C(x,y) &= R_F(x,y,y)
        \end{align}\right. \]
    
        where \[ s(t) = \sqrt{t+x}\sqrt{t+y}\sqrt{t+z} \]
    
        The algorithms used are based on the duplication method as described in B. C. Carlson 1995 paper "Numerical computation
        of real or complex elliptic integrals", with the improvements described in the appendix of B. C. Carlson and James
        FitzSimons 2000 paper "Reduction theorems for elliptic integrands with the square root of two quadratic factors". They
        are also described in :meth:`~org.hipparchus.special.elliptic.carlson.https:.dlmf.nist.gov.19.36#i` of Digital Library
        of Mathematical Functions.
    
        *Beware that when computing elliptic integrals in the complex plane, many issues arise due to branch cuts. See the
        :meth:`~org.hipparchus.special.elliptic.carlson.https:.www.hipparchus.org.hipparchus` for a thorough explanation.*
    
        Since:
            2.0
    """
    _rC_1__T = typing.TypeVar('_rC_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rC_3__T = typing.TypeVar('_rC_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rC(double: float, double2: float) -> float:
        """
            Compute Carlson elliptic integral R :sub:`C` .
        
            The Carlson elliptic integral R :sub:`C` is defined as \[
            R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
            Parameters:
                x (double): first symmetric variable of the integral
                y (double): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`C`
        
            Compute Carlson elliptic integral R :sub:`C` .
        
            The Carlson elliptic integral R :sub:`C` is defined as \[
            R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.Complex`): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`C`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rC(t: _rC_1__T, t2: _rC_1__T) -> _rC_1__T:
        """
            Compute Carlson elliptic integral R :sub:`C` .
        
            The Carlson elliptic integral R :sub:`C` is defined as \[
            R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
            Parameters:
                x (T): first symmetric variable of the integral
                y (T): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`C`
        
            Compute Carlson elliptic integral R :sub:`C` .
        
            The Carlson elliptic integral R :sub:`C` is defined as \[
            R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`C`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rC(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rC(fieldComplex: org.hipparchus.complex.FieldComplex[_rC_3__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_rC_3__T]) -> org.hipparchus.complex.FieldComplex[_rC_3__T]: ...
    _rD_1__T = typing.TypeVar('_rD_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rD_3__T = typing.TypeVar('_rD_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rD(double: float, double2: float, double3: float) -> float:
        """
            Compute Carlson elliptic integral R :sub:`D` .
        
            The Carlson elliptic integral R :sub:`D` is defined as \[
            R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
            Parameters:
                x (double): first symmetric variable of the integral
                y (double): second symmetric variable of the integral
                z (double): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`D`
        
            Compute Carlson elliptic integral R :sub:`D` .
        
            The Carlson elliptic integral R :sub:`D` is defined as \[
            R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.Complex`): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.Complex`): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`D`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rD(t: _rD_1__T, t2: _rD_1__T, t3: _rD_1__T) -> _rD_1__T:
        """
            Compute Carlson elliptic integral R :sub:`D` .
        
            The Carlson elliptic integral R :sub:`D` is defined as \[
            R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
            Parameters:
                x (T): first symmetric variable of the integral
                y (T): second symmetric variable of the integral
                z (T): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`D`
        
            Compute Carlson elliptic integral R :sub:`D` .
        
            The Carlson elliptic integral R :sub:`D` is defined as \[
            R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.FieldComplex`<T> z): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`D`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rD(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complex3: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rD(fieldComplex: org.hipparchus.complex.FieldComplex[_rD_3__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_rD_3__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_rD_3__T]) -> org.hipparchus.complex.FieldComplex[_rD_3__T]: ...
    _rF_1__T = typing.TypeVar('_rF_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rF_3__T = typing.TypeVar('_rF_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rF(double: float, double2: float, double3: float) -> float:
        """
            Compute Carlson elliptic integral R :sub:`F` .
        
            The Carlson elliptic integral R :sub:`F` is defined as \[
            R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
            Parameters:
                x (double): first symmetric variable of the integral
                y (double): second symmetric variable of the integral
                z (double): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`F`
        
            Compute Carlson elliptic integral R :sub:`F` .
        
            The Carlson elliptic integral R :sub:`F` is defined as \[
            R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.Complex`): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.Complex`): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`F`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rF(t: _rF_1__T, t2: _rF_1__T, t3: _rF_1__T) -> _rF_1__T:
        """
            Compute Carlson elliptic integral R :sub:`F` .
        
            The Carlson elliptic integral R :sub:`F` is defined as \[
            R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
            Parameters:
                x (T): first symmetric variable of the integral
                y (T): second symmetric variable of the integral
                z (T): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`F`
        
            Compute Carlson elliptic integral R :sub:`F` .
        
            The Carlson elliptic integral R :sub:`F` is defined as \[
            R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.FieldComplex`<T> z): third symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`F`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rF(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complex3: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rF(fieldComplex: org.hipparchus.complex.FieldComplex[_rF_3__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_rF_3__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_rF_3__T]) -> org.hipparchus.complex.FieldComplex[_rF_3__T]: ...
    _rG_1__T = typing.TypeVar('_rG_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rG_3__T = typing.TypeVar('_rG_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rG(double: float, double2: float, double3: float) -> float:
        """
            Compute Carlson elliptic integral R :sub:`G` .
        
            The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)}
            \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
            Parameters:
                x (double): first symmetric variable of the integral
                y (double): second symmetric variable of the integral
                z (double): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`G`
        
            Compute Carlson elliptic integral R :sub:`G` .
        
            The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)}
            \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.Complex`): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.Complex`): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`G`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rG(t: _rG_1__T, t2: _rG_1__T, t3: _rG_1__T) -> _rG_1__T:
        """
            Compute Carlson elliptic integral R :sub:`G` .
        
            The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)}
            \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
            Parameters:
                x (T): first symmetric variable of the integral
                y (T): second symmetric variable of the integral
                z (T): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`G`
        
            Compute Carlson elliptic integral R :sub:`G` .
        
            The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)}
            \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.FieldComplex`<T> z): second symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`G`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rG(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complex3: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rG(fieldComplex: org.hipparchus.complex.FieldComplex[_rG_3__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_rG_3__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_rG_3__T]) -> org.hipparchus.complex.FieldComplex[_rG_3__T]: ...
    _rJ_2__T = typing.TypeVar('_rJ_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rJ_3__T = typing.TypeVar('_rJ_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rJ_6__T = typing.TypeVar('_rJ_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rJ_7__T = typing.TypeVar('_rJ_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rJ(double: float, double2: float, double3: float, double4: float) -> float:
        """
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (double): first symmetric variable of the integral
                y (double): second symmetric variable of the integral
                z (double): third symmetric variable of the integral
                p (double): fourth *not* symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (double): first symmetric variable of the integral
                y (double): second symmetric variable of the integral
                z (double): third symmetric variable of the integral
                p (double): fourth *not* symmetric variable of the integral
                delta (double): precomputed value of (p-x)(p-y)(p-z)
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.Complex`): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.Complex`): third symmetric variable of the integral
                p (:class:`~org.hipparchus.complex.Complex`): fourth *not* symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.Complex`): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.Complex`): third symmetric variable of the integral
                p (:class:`~org.hipparchus.complex.Complex`): fourth *not* symmetric variable of the integral
                delta (:class:`~org.hipparchus.complex.Complex`): precomputed value of (p-x)(p-y)(p-z)
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rJ(double: float, double2: float, double3: float, double4: float, double5: float) -> float: ...
    @typing.overload
    @staticmethod
    def rJ(t: _rJ_2__T, t2: _rJ_2__T, t3: _rJ_2__T, t4: _rJ_2__T) -> _rJ_2__T:
        """
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (T): first symmetric variable of the integral
                y (T): second symmetric variable of the integral
                z (T): third symmetric variable of the integral
                p (T): fourth *not* symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (T): first symmetric variable of the integral
                y (T): second symmetric variable of the integral
                z (T): third symmetric variable of the integral
                p (T): fourth *not* symmetric variable of the integral
                delta (T): precomputed value of (p-x)(p-y)(p-z)
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.FieldComplex`<T> z): third symmetric variable of the integral
                p (:class:`~org.hipparchus.complex.FieldComplex`<T> p): fourth *not* symmetric variable of the integral
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rJ(t: _rJ_3__T, t2: _rJ_3__T, t3: _rJ_3__T, t4: _rJ_3__T, t5: _rJ_3__T) -> _rJ_3__T:
        """
            Compute Carlson elliptic integral R :sub:`J` .
        
            The Carlson elliptic integral R :sub:`J` is defined as \[
            R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): first symmetric variable of the integral
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): second symmetric variable of the integral
                z (:class:`~org.hipparchus.complex.FieldComplex`<T> z): third symmetric variable of the integral
                p (:class:`~org.hipparchus.complex.FieldComplex`<T> p): fourth *not* symmetric variable of the integral
                delta (:class:`~org.hipparchus.complex.FieldComplex`<T> delta): precomputed value of (p-x)(p-y)(p-z)
        
            Returns:
                Carlson elliptic integral R :sub:`J`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rJ(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complex3: org.hipparchus.complex.Complex, complex4: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rJ(complex: org.hipparchus.complex.Complex, complex2: org.hipparchus.complex.Complex, complex3: org.hipparchus.complex.Complex, complex4: org.hipparchus.complex.Complex, complex5: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rJ(fieldComplex: org.hipparchus.complex.FieldComplex[_rJ_6__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_rJ_6__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_rJ_6__T], fieldComplex4: org.hipparchus.complex.FieldComplex[_rJ_6__T]) -> org.hipparchus.complex.FieldComplex[_rJ_6__T]: ...
    @typing.overload
    @staticmethod
    def rJ(fieldComplex: org.hipparchus.complex.FieldComplex[_rJ_7__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_rJ_7__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_rJ_7__T], fieldComplex4: org.hipparchus.complex.FieldComplex[_rJ_7__T], fieldComplex5: org.hipparchus.complex.FieldComplex[_rJ_7__T]) -> org.hipparchus.complex.FieldComplex[_rJ_7__T]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special.elliptic.carlson")``.

    CarlsonEllipticIntegral: typing.Type[CarlsonEllipticIntegral]
