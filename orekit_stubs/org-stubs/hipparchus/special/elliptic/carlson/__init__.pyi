
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
    Elliptic integrals in Carlson symmetric form.
    
    This utility class computes the various symmetric elliptic integrals defined as: \[ \left\{\begin{align} R_F(x,y,z) &= \frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{s(t)}\\ R_J(x,y,z,p) &= \frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{s(t)(t+p)}\\ R_G(x,y,z) &= \frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)} \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t\\ R_D(x,y,z) &= R_J(x,y,z,z)\\ R_C(x,y) &= R_F(x,y,y) \end{align}\right. \]
    
    where \[ s(t) = \sqrt{t+x}\sqrt{t+y}\sqrt{t+z} \]
    
    The algorithms used are based on the duplication method as described in B. C. Carlson 1995 paper "Numerical computation of real or complex elliptic integrals", with the improvements described in the appendix of B. C. Carlson and James FitzSimons 2000 paper "Reduction theorems for elliptic integrands with the square root of two quadratic factors". They are also described in gov of Digital Library of Mathematical Functions.
    
    Beware that when computing elliptic integrals in the complex plane, many issues arise due to branch cuts. See the hipparchus for a thorough explanation.
    
    Since:
        2.0
    """
    _rC_1__T = typing.TypeVar('_rC_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rC_3__T = typing.TypeVar('_rC_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rC(x: float, y: float) -> float:
        """
        Compute Carlson elliptic integral R :sub:`C` .
        
        The Carlson elliptic integral R :sub:`C` is defined as \[ R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
        Parameters:
            x (double): first symmetric variable of the integral
            y (double): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`C`
        
        Compute Carlson elliptic integral R :sub:`C` .
        
        The Carlson elliptic integral R :sub:`C` is defined as \[ R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
        Parameters:
            x (Complex): first symmetric variable of the integral
            y (Complex): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`C`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rC(x: _rC_1__T, y: _rC_1__T) -> _rC_1__T:
        """
        Compute Carlson elliptic integral R :sub:`C` .
        
        The Carlson elliptic integral R :sub:`C` is defined as \[ R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
        Parameters:
            x (T): first symmetric variable of the integral
            y (T): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`C`
        
        Compute Carlson elliptic integral R :sub:`C` .
        
        The Carlson elliptic integral R :sub:`C` is defined as \[ R_C(x,y,z)=R_F(x,y,y)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}(t+y)} \]
        
        Parameters:
            x (FieldComplex<T> x): first symmetric variable of the integral
            y (FieldComplex<T> y): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`C`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rC(x: org.hipparchus.complex.Complex, y: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rC(x: org.hipparchus.complex.FieldComplex[_rC_3__T], y: org.hipparchus.complex.FieldComplex[_rC_3__T]) -> org.hipparchus.complex.FieldComplex[_rC_3__T]: ...
    _rD_1__T = typing.TypeVar('_rD_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rD_3__T = typing.TypeVar('_rD_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rD(x: float, y: float, z: float) -> float:
        """
        Compute Carlson elliptic integral R :sub:`D` .
        
        The Carlson elliptic integral R :sub:`D` is defined as \[ R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
        Parameters:
            x (double): first symmetric variable of the integral
            y (double): second symmetric variable of the integral
            z (double): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`D`
        
        Compute Carlson elliptic integral R :sub:`D` .
        
        The Carlson elliptic integral R :sub:`D` is defined as \[ R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
        Parameters:
            x (Complex): first symmetric variable of the integral
            y (Complex): second symmetric variable of the integral
            z (Complex): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`D`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rD(x: _rD_1__T, y: _rD_1__T, z: _rD_1__T) -> _rD_1__T:
        """
        Compute Carlson elliptic integral R :sub:`D` .
        
        The Carlson elliptic integral R :sub:`D` is defined as \[ R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
        Parameters:
            x (T): first symmetric variable of the integral
            y (T): second symmetric variable of the integral
            z (T): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`D`
        
        Compute Carlson elliptic integral R :sub:`D` .
        
        The Carlson elliptic integral R :sub:`D` is defined as \[ R_D(x,y,z)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+z)} \]
        
        Parameters:
            x (FieldComplex<T> x): first symmetric variable of the integral
            y (FieldComplex<T> y): second symmetric variable of the integral
            z (FieldComplex<T> z): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`D`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rD(x: org.hipparchus.complex.Complex, y: org.hipparchus.complex.Complex, z: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rD(x: org.hipparchus.complex.FieldComplex[_rD_3__T], y: org.hipparchus.complex.FieldComplex[_rD_3__T], z: org.hipparchus.complex.FieldComplex[_rD_3__T]) -> org.hipparchus.complex.FieldComplex[_rD_3__T]: ...
    _rF_1__T = typing.TypeVar('_rF_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rF_3__T = typing.TypeVar('_rF_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rF(x: float, y: float, z: float) -> float:
        """
        Compute Carlson elliptic integral R :sub:`F` .
        
        The Carlson elliptic integral R :sub:`F` is defined as \[ R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
        Parameters:
            x (double): first symmetric variable of the integral
            y (double): second symmetric variable of the integral
            z (double): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`F`
        
        Compute Carlson elliptic integral R :sub:`F` .
        
        The Carlson elliptic integral R :sub:`F` is defined as \[ R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
        Parameters:
            x (Complex): first symmetric variable of the integral
            y (Complex): second symmetric variable of the integral
            z (Complex): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`F`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rF(x: _rF_1__T, y: _rF_1__T, z: _rF_1__T) -> _rF_1__T:
        """
        Compute Carlson elliptic integral R :sub:`F` .
        
        The Carlson elliptic integral R :sub:`F` is defined as \[ R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
        Parameters:
            x (T): first symmetric variable of the integral
            y (T): second symmetric variable of the integral
            z (T): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`F`
        
        Compute Carlson elliptic integral R :sub:`F` .
        
        The Carlson elliptic integral R :sub:`F` is defined as \[ R_F(x,y,z)=\frac{1}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}} \]
        
        Parameters:
            x (FieldComplex<T> x): first symmetric variable of the integral
            y (FieldComplex<T> y): second symmetric variable of the integral
            z (FieldComplex<T> z): third symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`F`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rF(x: org.hipparchus.complex.Complex, y: org.hipparchus.complex.Complex, z: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rF(x: org.hipparchus.complex.FieldComplex[_rF_3__T], y: org.hipparchus.complex.FieldComplex[_rF_3__T], z: org.hipparchus.complex.FieldComplex[_rF_3__T]) -> org.hipparchus.complex.FieldComplex[_rF_3__T]: ...
    _rG_1__T = typing.TypeVar('_rG_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rG_3__T = typing.TypeVar('_rG_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rG(x: float, y: float, z: float) -> float:
        """
        Compute Carlson elliptic integral R :sub:`G` .
        
        The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)} \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
        Parameters:
            x (double): first symmetric variable of the integral
            y (double): second symmetric variable of the integral
            z (double): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`G`
        
        Compute Carlson elliptic integral R :sub:`G` .
        
        The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)} \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
        Parameters:
            x (Complex): first symmetric variable of the integral
            y (Complex): second symmetric variable of the integral
            z (Complex): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`G`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rG(x: _rG_1__T, y: _rG_1__T, z: _rG_1__T) -> _rG_1__T:
        """
        Compute Carlson elliptic integral R :sub:`G` .
        
        The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)} \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
        Parameters:
            x (T): first symmetric variable of the integral
            y (T): second symmetric variable of the integral
            z (T): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`G`
        
        Compute Carlson elliptic integral R :sub:`G` .
        
        The Carlson elliptic integral R :sub:`G` is defined as \[ R_{G}(x,y,z)=\frac{1}{4}\int_{0}^{\infty}\frac{1}{s(t)} \left(\frac{x}{t+x}+\frac{y}{t+y}+\frac{z}{t+z}\right)t\mathrm{d}t \]
        
        Parameters:
            x (FieldComplex<T> x): first symmetric variable of the integral
            y (FieldComplex<T> y): second symmetric variable of the integral
            z (FieldComplex<T> z): second symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`G`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rG(x: org.hipparchus.complex.Complex, y: org.hipparchus.complex.Complex, z: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rG(x: org.hipparchus.complex.FieldComplex[_rG_3__T], y: org.hipparchus.complex.FieldComplex[_rG_3__T], z: org.hipparchus.complex.FieldComplex[_rG_3__T]) -> org.hipparchus.complex.FieldComplex[_rG_3__T]: ...
    _rJ_2__T = typing.TypeVar('_rJ_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rJ_3__T = typing.TypeVar('_rJ_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rJ_6__T = typing.TypeVar('_rJ_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rJ_7__T = typing.TypeVar('_rJ_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rJ(x: float, y: float, z: float, p: float) -> float:
        """
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (double): first symmetric variable of the integral
            y (double): second symmetric variable of the integral
            z (double): third symmetric variable of the integral
            p (double): fourth not symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (double): first symmetric variable of the integral
            y (double): second symmetric variable of the integral
            z (double): third symmetric variable of the integral
            p (double): fourth not symmetric variable of the integral
            delta (double): precomputed value of (p-x)(p-y)(p-z)
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (Complex): first symmetric variable of the integral
            y (Complex): second symmetric variable of the integral
            z (Complex): third symmetric variable of the integral
            p (Complex): fourth not symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (Complex): first symmetric variable of the integral
            y (Complex): second symmetric variable of the integral
            z (Complex): third symmetric variable of the integral
            p (Complex): fourth not symmetric variable of the integral
            delta (Complex): precomputed value of (p-x)(p-y)(p-z)
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rJ(x: float, y: float, z: float, p: float, delta: float) -> float: ...
    @typing.overload
    @staticmethod
    def rJ(x: _rJ_2__T, y: _rJ_2__T, z: _rJ_2__T, p: _rJ_2__T) -> _rJ_2__T:
        """
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (T): first symmetric variable of the integral
            y (T): second symmetric variable of the integral
            z (T): third symmetric variable of the integral
            p (T): fourth not symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (T): first symmetric variable of the integral
            y (T): second symmetric variable of the integral
            z (T): third symmetric variable of the integral
            p (T): fourth not symmetric variable of the integral
            delta (T): precomputed value of (p-x)(p-y)(p-z)
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (FieldComplex<T> x): first symmetric variable of the integral
            y (FieldComplex<T> y): second symmetric variable of the integral
            z (FieldComplex<T> z): third symmetric variable of the integral
            p (FieldComplex<T> p): fourth not symmetric variable of the integral
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        """
        ...
    @typing.overload
    @staticmethod
    def rJ(x: _rJ_3__T, y: _rJ_3__T, z: _rJ_3__T, p: _rJ_3__T, delta: _rJ_3__T) -> _rJ_3__T:
        """
        Compute Carlson elliptic integral R :sub:`J` .
        
        The Carlson elliptic integral R :sub:`J` is defined as \[ R_J(x,y,z,p)=\frac{3}{2}\int_{0}^{\infty}\frac{\mathrm{d}t}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}(t+p)} \]
        
        Parameters:
            x (FieldComplex<T> x): first symmetric variable of the integral
            y (FieldComplex<T> y): second symmetric variable of the integral
            z (FieldComplex<T> z): third symmetric variable of the integral
            p (FieldComplex<T> p): fourth not symmetric variable of the integral
            delta (FieldComplex<T> delta): precomputed value of (p-x)(p-y)(p-z)
        
        Returns:
            Carlson elliptic integral R :sub:`J`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def rJ(x: org.hipparchus.complex.Complex, y: org.hipparchus.complex.Complex, z: org.hipparchus.complex.Complex, p: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rJ(x: org.hipparchus.complex.Complex, y: org.hipparchus.complex.Complex, z: org.hipparchus.complex.Complex, p: org.hipparchus.complex.Complex, delta: org.hipparchus.complex.Complex) -> org.hipparchus.complex.Complex: ...
    @typing.overload
    @staticmethod
    def rJ(x: org.hipparchus.complex.FieldComplex[_rJ_6__T], y: org.hipparchus.complex.FieldComplex[_rJ_6__T], z: org.hipparchus.complex.FieldComplex[_rJ_6__T], p: org.hipparchus.complex.FieldComplex[_rJ_6__T]) -> org.hipparchus.complex.FieldComplex[_rJ_6__T]: ...
    @typing.overload
    @staticmethod
    def rJ(x: org.hipparchus.complex.FieldComplex[_rJ_7__T], y: org.hipparchus.complex.FieldComplex[_rJ_7__T], z: org.hipparchus.complex.FieldComplex[_rJ_7__T], p: org.hipparchus.complex.FieldComplex[_rJ_7__T], delta: org.hipparchus.complex.FieldComplex[_rJ_7__T]) -> org.hipparchus.complex.FieldComplex[_rJ_7__T]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special.elliptic.carlson")``.

    CarlsonEllipticIntegral: typing.Type[CarlsonEllipticIntegral]
