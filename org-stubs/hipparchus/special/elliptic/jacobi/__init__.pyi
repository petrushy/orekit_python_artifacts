import org.hipparchus
import org.hipparchus.complex
import typing



class CopolarC:
    """
    public class CopolarC extends Object
    
        Copolar trio with pole at point c in Glaisherâ€™s Notation.
    
        This is a container for the three subsidiary Jacobi elliptic functions :code:`dc(u|m)`, :code:`nc(u|m)`, and
        :code:`sc(u|m)`.
    
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
    public class CopolarD extends Object
    
        Copolar trio with pole at point d in Glaisherâ€™s Notation.
    
        This is a container for the three subsidiary Jacobi elliptic functions :code:`nd(u|m)`, :code:`sd(u|m)`, and
        :code:`cd(u|m)`.
    
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
    public class CopolarN extends Object
    
        Copolar trio with pole at point n in Glaisherâ€™s Notation.
    
        This is a container for the three principal Jacobi elliptic functions :code:`sn(u|m)`, :code:`cn(u|m)`, and
        :code:`dn(u|m)`.
    
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
    public class CopolarS extends Object
    
        Copolar trio with pole at point s in Glaisherâ€™s Notation.
    
        This is a container for the three subsidiary Jacobi elliptic functions :code:`cs(u|m)`, :code:`ds(u|m)` and
        :code:`ns(u|m)`.
    
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
    public class FieldCopolarC<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Copolar trio with pole at point c in Glaisherâ€™s Notation.
    
        This is a container for the three subsidiary Jacobi elliptic functions :code:`dc(u|m)`, :code:`nc(u|m)`, and
        :code:`sc(u|m)`.
    
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
    public class FieldCopolarD<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Copolar trio with pole at point d in Glaisherâ€™s Notation.
    
        This is a container for the three subsidiary Jacobi elliptic functions :code:`nd(u|m)`, :code:`sd(u|m)`, and
        :code:`cd(u|m)`.
    
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
    public class FieldCopolarN<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Copolar trio with pole at point n in Glaisherâ€™s Notation.
    
        This is a container for the three principal Jacobi elliptic functions :code:`sn(u|m)`, :code:`cn(u|m)`, and
        :code:`dn(u|m)`.
    
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
    public class FieldCopolarS<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Copolar trio with pole at point s in Glaisherâ€™s Notation.
    
        This is a container for the three subsidiary Jacobi elliptic functions :code:`cs(u|m)`, :code:`ds(u|m)` and
        :code:`ns(u|m)`.
    
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
    public abstract class FieldJacobiElliptic<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Computation of Jacobi elliptic functions. The Jacobi elliptic functions are related to elliptic integrals.
    
        Since:
            2.0
    """
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
    public class FieldJacobiTheta<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Algorithm computing Jacobi theta functions.
    
        Since:
            2.0
    """
    def __init__(self, t: _FieldJacobiTheta__T): ...
    def getQ(self) -> _FieldJacobiTheta__T:
        """
            Get the nome.
        
            Returns:
                nome
        
        
        """
        ...
    def values(self, t: _FieldJacobiTheta__T) -> 'FieldTheta'[_FieldJacobiTheta__T]: ...

_FieldTheta__T = typing.TypeVar('_FieldTheta__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTheta(typing.Generic[_FieldTheta__T]):
    """
    public class FieldTheta<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Values of :class:`~org.hipparchus.special.elliptic.jacobi.FieldJacobiTheta` functions.
    
        This is a container for the four Jacobi theta functions Î¸â‚�(z|Ï„), Î¸â‚‚(z|Ï„), Î¸â‚ƒ(z|Ï„), and Î¸â‚„(z|Ï„).
    
        Since:
            2.0
    
        Also see:
            :class:`~org.hipparchus.special.elliptic.jacobi.FieldJacobiTheta`
    """
    def theta1(self) -> _FieldTheta__T:
        """
            Get the value of the Î¸â‚�(z|Ï„) function.
        
            Returns:
                Î¸â‚�(z|Ï„)
        
        
        """
        ...
    def theta2(self) -> _FieldTheta__T:
        """
            Get the value of the Î¸â‚‚(z|Ï„) function.
        
            Returns:
                Î¸â‚‚(z|Ï„)
        
        
        """
        ...
    def theta3(self) -> _FieldTheta__T:
        """
            Get the value of the Î¸â‚ƒ(z|Ï„) function.
        
            Returns:
                Î¸â‚ƒ(z|Ï„)
        
        
        """
        ...
    def theta4(self) -> _FieldTheta__T:
        """
            Get the value of the Î¸â‚„(z|Ï„) function.
        
            Returns:
                Î¸â‚„(z|Ï„)
        
        
        """
        ...

class JacobiElliptic:
    """
    public abstract class JacobiElliptic extends Object
    
        Algorithm computing Jacobi elliptic functions.
    
        Since:
            2.0
    """
    def getM(self) -> float:
        """
            Get the parameter of the function.
        
            Returns:
                parameter of the function
        
        
        """
        ...
    def valuesC(self, double: float) -> CopolarC:
        """
            Evaluate the three subsidiary Jacobi elliptic functions with pole at point c in Glaisherâ€™s Notation.
        
            Parameters:
                u (double): argument of the functions
        
            Returns:
                copolar trio containing the three subsidiary Jacobi elliptic functions :code:`dc(u|m)`, :code:`nc(u|m)`, and
                :code:`sc(u|m)`.
        
        
        """
        ...
    def valuesD(self, double: float) -> CopolarD:
        """
            Evaluate the three subsidiary Jacobi elliptic functions with pole at point d in Glaisherâ€™s Notation.
        
            Parameters:
                u (double): argument of the functions
        
            Returns:
                copolar trio containing the three subsidiary Jacobi elliptic functions :code:`nd(u|m)`, :code:`sd(u|m)`, and
                :code:`cd(u|m)`.
        
        
        """
        ...
    def valuesN(self, double: float) -> CopolarN:
        """
            Evaluate the three principal Jacobi elliptic functions with pole at point n in Glaisherâ€™s Notation.
        
            Parameters:
                u (double): argument of the functions
        
            Returns:
                copolar trio containing the three principal Jacobi elliptic functions :code:`sn(u|m)`, :code:`cn(u|m)`, and
                :code:`dn(u|m)`.
        
        
        """
        ...
    def valuesS(self, double: float) -> CopolarS:
        """
            Evaluate the three subsidiary Jacobi elliptic functions with pole at point s in Glaisherâ€™s Notation.
        
            Parameters:
                u (double): argument of the functions
        
            Returns:
                copolar trio containing the three subsidiary Jacobi elliptic functions :code:`cs(u|m)`, :code:`ds(u|m)` and
                :code:`ns(u|m)`.
        
        
        """
        ...

class JacobiEllipticBuilder:
    """
    public class JacobiEllipticBuilder extends Object
    
        Builder for algorithms compmuting Jacobi elliptic functions.
    
        The Jacobi elliptic functions are related to elliptic integrals.
    
        There are different conventions to interpret the arguments of Jacobi elliptic functions. The first argument may be the
        amplitude Ã�â€ , but is more often the variable u (with sn(u) = sin(Ã�â€ ) and cn(u) = cos(Ã�â€ )). The second argument
        is either the modulus k or the parameter m with m = kÃ‚Â². In Hipparchus, we adopted the convention to use u and m.
    
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
        
        public static :class:`~org.hipparchus.special.elliptic.jacobi.FieldJacobiElliptic`<:class:`~org.hipparchus.complex.Complex`> build(:class:`~org.hipparchus.complex.Complex` m)
        
            Build an algorithm for computing Jacobi elliptic functions.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.Complex`): parameter of the Jacobi elliptic function
        
            Returns:
                selected algorithm
        
        public static <T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> :class:`~org.hipparchus.special.elliptic.jacobi.FieldJacobiElliptic`<:class:`~org.hipparchus.complex.FieldComplex`<T>> build(:class:`~org.hipparchus.complex.FieldComplex`<T> m)
        
            Build an algorithm for computing Jacobi elliptic functions.
        
            Parameters:
                m (:class:`~org.hipparchus.complex.FieldComplex`<T> m): parameter of the Jacobi elliptic function
        
            Returns:
                selected algorithm
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def build(complex: org.hipparchus.complex.Complex) -> FieldJacobiElliptic[org.hipparchus.complex.Complex]:
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
    public class JacobiTheta extends Object
    
        Algorithm computing Jacobi theta functions.
    
        Since:
            2.0
    """
    def __init__(self, double: float): ...
    def getQ(self) -> float:
        """
            Get the nome.
        
            Returns:
                nome
        
        
        """
        ...
    def values(self, complex: org.hipparchus.complex.Complex) -> 'Theta':
        """
            Evaluate the Jacobi theta functions.
        
            Parameters:
                z (:class:`~org.hipparchus.complex.Complex`): argument of the functions
        
            Returns:
                container for the four Jacobi theta functions Î¸â‚�(z|Ï„), Î¸â‚‚(z|Ï„), Î¸â‚ƒ(z|Ï„), and Î¸â‚„(z|Ï„)
        
        
        """
        ...

class Theta:
    """
    public class Theta extends Object
    
        Values of :class:`~org.hipparchus.special.elliptic.jacobi.JacobiTheta` functions.
    
        This is a container for the four Jacobi theta functions Î¸â‚�(z|Ï„), Î¸â‚‚(z|Ï„), Î¸â‚ƒ(z|Ï„), and Î¸â‚„(z|Ï„).
    
        Since:
            2.0
    
        Also see:
            :class:`~org.hipparchus.special.elliptic.jacobi.JacobiTheta`
    """
    def theta1(self) -> org.hipparchus.complex.Complex:
        """
            Get the value of the Î¸â‚�(z|Ï„) function.
        
            Returns:
                Î¸â‚�(z|Ï„)
        
        
        """
        ...
    def theta2(self) -> org.hipparchus.complex.Complex:
        """
            Get the value of the Î¸â‚‚(z|Ï„) function.
        
            Returns:
                Î¸â‚‚(z|Ï„)
        
        
        """
        ...
    def theta3(self) -> org.hipparchus.complex.Complex:
        """
            Get the value of the Î¸â‚ƒ(z|Ï„) function.
        
            Returns:
                Î¸â‚ƒ(z|Ï„)
        
        
        """
        ...
    def theta4(self) -> org.hipparchus.complex.Complex:
        """
            Get the value of the Î¸â‚„(z|Ï„) function.
        
            Returns:
                Î¸â‚„(z|Ï„)
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
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
