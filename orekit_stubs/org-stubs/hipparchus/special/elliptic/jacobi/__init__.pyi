
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.hipparchus.complex
import typing



class CopolarC:
    """
    Copolar trio with pole at point c in Glaisher’s Notation.
    
    This is a container for the three subsidiary Jacobi elliptic functions dc(u|m), nc(u|m), and sc(u|m).
    
    Since:
        2.0
    """
    def dc(self) -> float:
        """
        Get the value of the dc function.
        
        Returns:
            dc(u|m)
        
        
        """
        ...
    def nc(self) -> float:
        """
        Get the value of the nc function.
        
        Returns:
            nc(u|m)
        
        
        """
        ...
    def sc(self) -> float:
        """
        Get the value of the sc function.
        
        Returns:
            sc(u|m)
        
        
        """
        ...

class CopolarD:
    """
    Copolar trio with pole at point d in Glaisher’s Notation.
    
    This is a container for the three subsidiary Jacobi elliptic functions nd(u|m), sd(u|m), and cd(u|m).
    
    Since:
        2.0
    """
    def cd(self) -> float:
        """
        Get the value of the cd function.
        
        Returns:
            cd(u|m)
        
        
        """
        ...
    def nd(self) -> float:
        """
        Get the value of the nd function.
        
        Returns:
            nd(u|m)
        
        
        """
        ...
    def sd(self) -> float:
        """
        Get the value of the sd function.
        
        Returns:
            sd(u|m)
        
        
        """
        ...

class CopolarN:
    """
    Copolar trio with pole at point n in Glaisher’s Notation.
    
    This is a container for the three principal Jacobi elliptic functions sn(u|m), cn(u|m), and dn(u|m).
    
    Since:
        2.0
    """
    def cn(self) -> float:
        """
        Get the value of the cn function.
        
        Returns:
            cn(u|m)
        
        
        """
        ...
    def dn(self) -> float:
        """
        Get the value of the dn function.
        
        Returns:
            dn(u|m)
        
        
        """
        ...
    def sn(self) -> float:
        """
        Get the value of the sn function.
        
        Returns:
            sn(u|m)
        
        
        """
        ...

class CopolarS:
    """
    Copolar trio with pole at point s in Glaisher’s Notation.
    
    This is a container for the three subsidiary Jacobi elliptic functions cs(u|m), ds(u|m) and ns(u|m).
    
    Since:
        2.0
    """
    def cs(self) -> float:
        """
        Get the value of the cs function.
        
        Returns:
            cs(u|m)
        
        
        """
        ...
    def ds(self) -> float:
        """
        Get the value of the ds function.
        
        Returns:
            ds(u|m)
        
        
        """
        ...
    def ns(self) -> float:
        """
        Get the value of the ns function.
        
        Returns:
            ns(u|m)
        
        
        """
        ...

_FieldCopolarC__T = typing.TypeVar('_FieldCopolarC__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarC(typing.Generic[_FieldCopolarC__T]):
    """
    Copolar trio with pole at point c in Glaisher’s Notation.
    
    This is a container for the three subsidiary Jacobi elliptic functions dc(u|m), nc(u|m), and sc(u|m).
    
    Since:
        2.0
    """
    def dc(self) -> _FieldCopolarC__T:
        """
        Get the value of the dc function.
        
        Returns:
            dc(u|m)
        
        
        """
        ...
    def nc(self) -> _FieldCopolarC__T:
        """
        Get the value of the nc function.
        
        Returns:
            nc(u|m)
        
        
        """
        ...
    def sc(self) -> _FieldCopolarC__T:
        """
        Get the value of the sc function.
        
        Returns:
            sc(u|m)
        
        
        """
        ...

_FieldCopolarD__T = typing.TypeVar('_FieldCopolarD__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarD(typing.Generic[_FieldCopolarD__T]):
    """
    Copolar trio with pole at point d in Glaisher’s Notation.
    
    This is a container for the three subsidiary Jacobi elliptic functions nd(u|m), sd(u|m), and cd(u|m).
    
    Since:
        2.0
    """
    def cd(self) -> _FieldCopolarD__T:
        """
        Get the value of the cd function.
        
        Returns:
            cd(u|m)
        
        
        """
        ...
    def nd(self) -> _FieldCopolarD__T:
        """
        Get the value of the nd function.
        
        Returns:
            nd(u|m)
        
        
        """
        ...
    def sd(self) -> _FieldCopolarD__T:
        """
        Get the value of the sd function.
        
        Returns:
            sd(u|m)
        
        
        """
        ...

_FieldCopolarN__T = typing.TypeVar('_FieldCopolarN__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarN(typing.Generic[_FieldCopolarN__T]):
    """
    Copolar trio with pole at point n in Glaisher’s Notation.
    
    This is a container for the three principal Jacobi elliptic functions sn(u|m), cn(u|m), and dn(u|m).
    
    Since:
        2.0
    """
    def cn(self) -> _FieldCopolarN__T:
        """
        Get the value of the cn function.
        
        Returns:
            cn(u|m)
        
        
        """
        ...
    def dn(self) -> _FieldCopolarN__T:
        """
        Get the value of the dn function.
        
        Returns:
            dn(u|m)
        
        
        """
        ...
    def sn(self) -> _FieldCopolarN__T:
        """
        Get the value of the sn function.
        
        Returns:
            sn(u|m)
        
        
        """
        ...

_FieldCopolarS__T = typing.TypeVar('_FieldCopolarS__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarS(typing.Generic[_FieldCopolarS__T]):
    """
    Copolar trio with pole at point s in Glaisher’s Notation.
    
    This is a container for the three subsidiary Jacobi elliptic functions cs(u|m), ds(u|m) and ns(u|m).
    
    Since:
        2.0
    """
    def cs(self) -> _FieldCopolarS__T:
        """
        Get the value of the cs function.
        
        Returns:
            cs(u|m)
        
        
        """
        ...
    def ds(self) -> _FieldCopolarS__T:
        """
        Get the value of the ds function.
        
        Returns:
            ds(u|m)
        
        
        """
        ...
    def ns(self) -> _FieldCopolarS__T:
        """
        Get the value of the ns function.
        
        Returns:
            ns(u|m)
        
        
        """
        ...

_FieldJacobiElliptic__T = typing.TypeVar('_FieldJacobiElliptic__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldJacobiElliptic(typing.Generic[_FieldJacobiElliptic__T]):
    """
    Computation of Jacobi elliptic functions. The Jacobi elliptic functions are related to elliptic integrals.
    
    Since:
        2.0
    """
    @typing.overload
    def arccd(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function cd.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function cd(u|m)
        
        Returns:
            u such that x=cd(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function cd.
        
        Parameters:
            x (double): value of Jacobi elliptic function cd(u|m)
        
        Returns:
            u such that x=cd(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arccd(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arccn(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function cn.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function cn(u|m)
        
        Returns:
            u such that x=cn(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function cn.
        
        Parameters:
            x (double): value of Jacobi elliptic function cn(u|m)
        
        Returns:
            u such that x=cn(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arccn(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arccs(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function cs.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function cs(u|m)
        
        Returns:
            u such that x=cs(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function cs.
        
        Parameters:
            x (double): value of Jacobi elliptic function cs(u|m)
        
        Returns:
            u such that x=cs(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arccs(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcdc(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function dc.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function dc(u|m)
        
        Returns:
            u such that x=dc(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function dc.
        
        Parameters:
            x (double): value of Jacobi elliptic function dc(u|m)
        
        Returns:
            u such that x=dc(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcdc(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcdn(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function dn.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function dn(u|m)
        
        Returns:
            u such that x=dn(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function dn.
        
        Parameters:
            x (double): value of Jacobi elliptic function dn(u|m)
        
        Returns:
            u such that x=dn(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcdn(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcds(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function ds.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function ds(u|m)
        
        Returns:
            u such that x=ds(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function ds.
        
        Parameters:
            x (double): value of Jacobi elliptic function ds(u|m)
        
        Returns:
            u such that x=ds(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcds(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcnc(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function nc.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function nc(u|m)
        
        Returns:
            u such that x=nc(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function nc.
        
        Parameters:
            x (double): value of Jacobi elliptic function nc(u|m)
        
        Returns:
            u such that x=nc(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcnc(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcnd(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function nd.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function nd(u|m)
        
        Returns:
            u such that x=nd(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function nd.
        
        Parameters:
            x (double): value of Jacobi elliptic function nd(u|m)
        
        Returns:
            u such that x=nd(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcnd(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcns(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function ns.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function ns(u|m)
        
        Returns:
            u such that x=ns(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function ns.
        
        Parameters:
            x (double): value of Jacobi elliptic function ns(u|m)
        
        Returns:
            u such that x=ns(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcns(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsc(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function sc.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function sc(u|m)
        
        Returns:
            u such that x=sc(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function sc.
        
        Parameters:
            x (double): value of Jacobi elliptic function sc(u|m)
        
        Returns:
            u such that x=sc(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcsc(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsd(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function sd.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function sd(u|m)
        
        Returns:
            u such that x=sd(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function sd.
        
        Parameters:
            x (double): value of Jacobi elliptic function sd(u|m)
        
        Returns:
            u such that x=sd(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcsd(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsn(self, double: float) -> _FieldJacobiElliptic__T:
        """
        Evaluate inverse of Jacobi elliptic function sn.
        
        Parameters:
            x (FieldJacobiElliptic): value of Jacobi elliptic function sn(u|m)
        
        Returns:
            u such that x=sn(u|m)
        
        Since:
            2.1
        
        Evaluate inverse of Jacobi elliptic function sn.
        
        Parameters:
            x (double): value of Jacobi elliptic function sn(u|m)
        
        Returns:
            u such that x=sn(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def arcsn(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    def getM(self) -> _FieldJacobiElliptic__T:
        """
        Get the parameter of the function.
        
        Returns:
            parameter of the function
        
        
        """
        ...
    @typing.overload
    def valuesC(self, double: float) -> FieldCopolarC[_FieldJacobiElliptic__T]: ...
    @typing.overload
    def valuesC(self, t: _FieldJacobiElliptic__T) -> FieldCopolarC[_FieldJacobiElliptic__T]: ...
    @typing.overload
    def valuesD(self, double: float) -> FieldCopolarD[_FieldJacobiElliptic__T]: ...
    @typing.overload
    def valuesD(self, t: _FieldJacobiElliptic__T) -> FieldCopolarD[_FieldJacobiElliptic__T]: ...
    @typing.overload
    def valuesN(self, t: _FieldJacobiElliptic__T) -> FieldCopolarN[_FieldJacobiElliptic__T]: ...
    @typing.overload
    def valuesN(self, double: float) -> FieldCopolarN[_FieldJacobiElliptic__T]: ...
    @typing.overload
    def valuesS(self, double: float) -> FieldCopolarS[_FieldJacobiElliptic__T]: ...
    @typing.overload
    def valuesS(self, t: _FieldJacobiElliptic__T) -> FieldCopolarS[_FieldJacobiElliptic__T]: ...

_FieldJacobiTheta__T = typing.TypeVar('_FieldJacobiTheta__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldJacobiTheta(typing.Generic[_FieldJacobiTheta__T]):
    """
    Algorithm computing Jacobi theta functions.
    
    Since:
        2.0
    """
    def __init__(self, q: _FieldJacobiTheta__T):
        """
        Simple constructor.
        
        The nome q can be computed using ratios of complete elliptic integrals (nome which are themselves defined in term of parameter m, where m=k² and k is the elliptic modulus.
        
        Parameters:
            q (FieldJacobiTheta): nome
        
        
        """
        ...
    def getQ(self) -> _FieldJacobiTheta__T:
        """
        Get the nome.
        
        Returns:
            nome
        
        
        """
        ...
    def values(self, z: _FieldJacobiTheta__T) -> 'FieldTheta'[_FieldJacobiTheta__T]:
        """
        Evaluate the Jacobi theta functions.
        
        Parameters:
            z (FieldJacobiTheta): argument of the functions
        
        Returns:
            container for the four Jacobi theta functions θ₁(z|τ), θ₂(z|τ), θ₃(z|τ), and θ₄(z|τ)
        
        
        """
        ...

_FieldTheta__T = typing.TypeVar('_FieldTheta__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTheta(typing.Generic[_FieldTheta__T]):
    """
    Values of FieldJacobiTheta functions.
    
    This is a container for the four Jacobi theta functions θ₁(z|τ), θ₂(z|τ), θ₃(z|τ), and θ₄(z|τ).
    
    Since:
        2.0
    
          - FieldJacobiTheta
    """
    def theta1(self) -> _FieldTheta__T:
        """
        Get the value of the θ₁(z|τ) function.
        
        Returns:
            θ₁(z|τ)
        
        
        """
        ...
    def theta2(self) -> _FieldTheta__T:
        """
        Get the value of the θ₂(z|τ) function.
        
        Returns:
            θ₂(z|τ)
        
        
        """
        ...
    def theta3(self) -> _FieldTheta__T:
        """
        Get the value of the θ₃(z|τ) function.
        
        Returns:
            θ₃(z|τ)
        
        
        """
        ...
    def theta4(self) -> _FieldTheta__T:
        """
        Get the value of the θ₄(z|τ) function.
        
        Returns:
            θ₄(z|τ)
        
        
        """
        ...

class JacobiElliptic:
    """
    Algorithm computing Jacobi elliptic functions.
    
    Since:
        2.0
    """
    def arccd(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function cd.
        
        Parameters:
            x (double): value of Jacobi elliptic function cd(u|m)
        
        Returns:
            u such that x=cd(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arccn(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function cn.
        
        Parameters:
            x (double): value of Jacobi elliptic function cn(u|m)
        
        Returns:
            u such that x=cn(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arccs(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function cs.
        
        Parameters:
            x (double): value of Jacobi elliptic function cs(u|m)
        
        Returns:
            u such that x=cs(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcdc(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function dc.
        
        Parameters:
            x (double): value of Jacobi elliptic function dc(u|m)
        
        Returns:
            u such that x=dc(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcdn(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function dn.
        
        Parameters:
            x (double): value of Jacobi elliptic function dn(u|m)
        
        Returns:
            u such that x=dn(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcds(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function ds.
        
        Parameters:
            x (double): value of Jacobi elliptic function ds(u|m)
        
        Returns:
            u such that x=ds(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcnc(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function nc.
        
        Parameters:
            x (double): value of Jacobi elliptic function nc(u|m)
        
        Returns:
            u such that x=nc(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcnd(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function nd.
        
        Parameters:
            x (double): value of Jacobi elliptic function nd(u|m)
        
        Returns:
            u such that x=nd(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcns(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function ns.
        
        Parameters:
            x (double): value of Jacobi elliptic function ns(u|m)
        
        Returns:
            u such that x=ns(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcsc(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function sc.
        
        Parameters:
            x (double): value of Jacobi elliptic function sc(u|m)
        
        Returns:
            u such that x=sc(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcsd(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function sd.
        
        Parameters:
            x (double): value of Jacobi elliptic function sd(u|m)
        
        Returns:
            u such that x=sd(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def arcsn(self, x: float) -> float:
        """
        Evaluate inverse of Jacobi elliptic function sn.
        
        Parameters:
            x (double): value of Jacobi elliptic function sn(u|m)
        
        Returns:
            u such that x=sn(u|m)
        
        Since:
            2.1
        
        
        """
        ...
    def getM(self) -> float:
        """
        Get the parameter of the function.
        
        Returns:
            parameter of the function
        
        
        """
        ...
    def valuesC(self, u: float) -> CopolarC:
        """
        Evaluate the three subsidiary Jacobi elliptic functions with pole at point c in Glaisher’s Notation.
        
        Parameters:
            u (double): argument of the functions
        
        Returns:
            copolar trio containing the three subsidiary Jacobi elliptic functions dc(u|m), nc(u|m), and
            sc(u|m).
        
        
        """
        ...
    def valuesD(self, u: float) -> CopolarD:
        """
        Evaluate the three subsidiary Jacobi elliptic functions with pole at point d in Glaisher’s Notation.
        
        Parameters:
            u (double): argument of the functions
        
        Returns:
            copolar trio containing the three subsidiary Jacobi elliptic functions nd(u|m), sd(u|m), and
            cd(u|m).
        
        
        """
        ...
    def valuesN(self, u: float) -> CopolarN:
        """
        Evaluate the three principal Jacobi elliptic functions with pole at point n in Glaisher’s Notation.
        
        Parameters:
            u (double): argument of the functions
        
        Returns:
            copolar trio containing the three principal Jacobi elliptic functions sn(u|m), cn(u|m), and
            dn(u|m).
        
        
        """
        ...
    def valuesS(self, u: float) -> CopolarS:
        """
        Evaluate the three subsidiary Jacobi elliptic functions with pole at point s in Glaisher’s Notation.
        
        Parameters:
            u (double): argument of the functions
        
        Returns:
            copolar trio containing the three subsidiary Jacobi elliptic functions cs(u|m), ds(u|m) and
            ns(u|m).
        
        
        """
        ...

class JacobiEllipticBuilder:
    """
    Builder for algorithms compmuting Jacobi elliptic functions.
    
    The Jacobi elliptic functions are related to elliptic integrals.
    
    There are different conventions to interpret the arguments of Jacobi elliptic functions. The first argument may be the amplitude φ, but is more often the variable u (with sn(u) = sin(φ) and cn(u) = cos(φ)). The second argument is either the modulus k or the parameter m with m = k². In Hipparchus, we adopted the convention to use u and m.
    
    Since:
        2.0
    """
    _build_0__T = typing.TypeVar('_build_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _build_2__T = typing.TypeVar('_build_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def build(t: _build_0__T) -> FieldJacobiElliptic[_build_0__T]:
        """
        Build an algorithm for computing Jacobi elliptic functions.
        
        Parameters:
            m (T): parameter of the Jacobi elliptic function
        
        Returns:
            selected algorithm
        
        public static FieldJacobiElliptic<Complex> build(Complex m)
        
        Build an algorithm for computing Jacobi elliptic functions.
        
        Parameters:
            m (Complex): parameter of the Jacobi elliptic function
        
        Returns:
            selected algorithm
        
        public static <T extends CalculusFieldElement<T>> FieldJacobiElliptic<FieldComplex<T>> build(FieldComplex<T> m)
        
        Build an algorithm for computing Jacobi elliptic functions.
        
        Parameters:
            m (FieldComplex<T> m): parameter of the Jacobi elliptic function
        
        Returns:
            selected algorithm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def build(m: org.hipparchus.complex.Complex) -> FieldJacobiElliptic[org.hipparchus.complex.Complex]:
        """
        Build an algorithm for computing Jacobi elliptic functions.
        
        Parameters:
            m (double): parameter of the Jacobi elliptic function
        
        Returns:
            selected algorithm
        
        """
        ...
    @typing.overload
    @staticmethod
    def build(fieldComplex: org.hipparchus.complex.FieldComplex[_build_2__T]) -> FieldJacobiElliptic[org.hipparchus.complex.FieldComplex[_build_2__T]]: ...
    @typing.overload
    @staticmethod
    def build(double: float) -> JacobiElliptic: ...

class JacobiTheta:
    """
    Algorithm computing Jacobi theta functions.
    
    Since:
        2.0
    """
    def __init__(self, q: float):
        """
        Simple constructor.
        
        The nome q can be computed using ratios of complete elliptic integrals (nome which are themselves defined in term of parameter m, where m=k² and k is the elliptic modulus.
        
        Parameters:
            q (double): nome
        
        
        """
        ...
    def getQ(self) -> float:
        """
        Get the nome.
        
        Returns:
            nome
        
        
        """
        ...
    def values(self, z: org.hipparchus.complex.Complex) -> 'Theta':
        """
        Evaluate the Jacobi theta functions.
        
        Parameters:
            z (Complex): argument of the functions
        
        Returns:
            container for the four Jacobi theta functions θ₁(z|τ), θ₂(z|τ), θ₃(z|τ), and θ₄(z|τ)
        
        
        """
        ...

class Theta:
    """
    Values of JacobiTheta functions.
    
    This is a container for the four Jacobi theta functions θ₁(z|τ), θ₂(z|τ), θ₃(z|τ), and θ₄(z|τ).
    
    Since:
        2.0
    
          - JacobiTheta
    """
    def theta1(self) -> org.hipparchus.complex.Complex:
        """
        Get the value of the θ₁(z|τ) function.
        
        Returns:
            θ₁(z|τ)
        
        
        """
        ...
    def theta2(self) -> org.hipparchus.complex.Complex:
        """
        Get the value of the θ₂(z|τ) function.
        
        Returns:
            θ₂(z|τ)
        
        
        """
        ...
    def theta3(self) -> org.hipparchus.complex.Complex:
        """
        Get the value of the θ₃(z|τ) function.
        
        Returns:
            θ₃(z|τ)
        
        
        """
        ...
    def theta4(self) -> org.hipparchus.complex.Complex:
        """
        Get the value of the θ₄(z|τ) function.
        
        Returns:
            θ₄(z|τ)
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special.elliptic.jacobi")``.

    CopolarC: typing.Type[CopolarC]
    CopolarD: typing.Type[CopolarD]
    CopolarN: typing.Type[CopolarN]
    CopolarS: typing.Type[CopolarS]
    FieldCopolarC: typing.Type[FieldCopolarC]
    FieldCopolarD: typing.Type[FieldCopolarD]
    FieldCopolarN: typing.Type[FieldCopolarN]
    FieldCopolarS: typing.Type[FieldCopolarS]
    FieldJacobiElliptic: typing.Type[FieldJacobiElliptic]
    FieldJacobiTheta: typing.Type[FieldJacobiTheta]
    FieldTheta: typing.Type[FieldTheta]
    JacobiElliptic: typing.Type[JacobiElliptic]
    JacobiEllipticBuilder: typing.Type[JacobiEllipticBuilder]
    JacobiTheta: typing.Type[JacobiTheta]
    Theta: typing.Type[Theta]
