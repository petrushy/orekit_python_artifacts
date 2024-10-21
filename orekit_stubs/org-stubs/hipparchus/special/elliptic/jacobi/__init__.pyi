import org.hipparchus
import org.hipparchus.complex
import org.hipparchus.special.elliptic.jacobi.class-use
import typing



class CopolarC:
    def dc(self) -> float: ...
    def nc(self) -> float: ...
    def sc(self) -> float: ...

class CopolarD:
    def cd(self) -> float: ...
    def nd(self) -> float: ...
    def sd(self) -> float: ...

class CopolarN:
    def cn(self) -> float: ...
    def dn(self) -> float: ...
    def sn(self) -> float: ...

class CopolarS:
    def cs(self) -> float: ...
    def ds(self) -> float: ...
    def ns(self) -> float: ...

_FieldCopolarC__T = typing.TypeVar('_FieldCopolarC__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarC(typing.Generic[_FieldCopolarC__T]):
    def dc(self) -> _FieldCopolarC__T: ...
    def nc(self) -> _FieldCopolarC__T: ...
    def sc(self) -> _FieldCopolarC__T: ...

_FieldCopolarD__T = typing.TypeVar('_FieldCopolarD__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarD(typing.Generic[_FieldCopolarD__T]):
    def cd(self) -> _FieldCopolarD__T: ...
    def nd(self) -> _FieldCopolarD__T: ...
    def sd(self) -> _FieldCopolarD__T: ...

_FieldCopolarN__T = typing.TypeVar('_FieldCopolarN__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarN(typing.Generic[_FieldCopolarN__T]):
    def cn(self) -> _FieldCopolarN__T: ...
    def dn(self) -> _FieldCopolarN__T: ...
    def sn(self) -> _FieldCopolarN__T: ...

_FieldCopolarS__T = typing.TypeVar('_FieldCopolarS__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCopolarS(typing.Generic[_FieldCopolarS__T]):
    def cs(self) -> _FieldCopolarS__T: ...
    def ds(self) -> _FieldCopolarS__T: ...
    def ns(self) -> _FieldCopolarS__T: ...

_FieldJacobiElliptic__T = typing.TypeVar('_FieldJacobiElliptic__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldJacobiElliptic(typing.Generic[_FieldJacobiElliptic__T]):
    @typing.overload
    def arccd(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arccd(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arccn(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arccn(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arccs(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arccs(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcdc(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcdc(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcdn(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcdn(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcds(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcds(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcnc(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcnc(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcnd(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcnd(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcns(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcns(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsc(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsc(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsd(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsd(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsn(self, double: float) -> _FieldJacobiElliptic__T: ...
    @typing.overload
    def arcsn(self, t: _FieldJacobiElliptic__T) -> _FieldJacobiElliptic__T: ...
    def getM(self) -> _FieldJacobiElliptic__T: ...
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
    def __init__(self, t: _FieldJacobiTheta__T): ...
    def getQ(self) -> _FieldJacobiTheta__T: ...
    def values(self, t: _FieldJacobiTheta__T) -> 'FieldTheta'[_FieldJacobiTheta__T]: ...

_FieldTheta__T = typing.TypeVar('_FieldTheta__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTheta(typing.Generic[_FieldTheta__T]):
    def theta1(self) -> _FieldTheta__T: ...
    def theta2(self) -> _FieldTheta__T: ...
    def theta3(self) -> _FieldTheta__T: ...
    def theta4(self) -> _FieldTheta__T: ...

class JacobiElliptic:
    def arccd(self, double: float) -> float: ...
    def arccn(self, double: float) -> float: ...
    def arccs(self, double: float) -> float: ...
    def arcdc(self, double: float) -> float: ...
    def arcdn(self, double: float) -> float: ...
    def arcds(self, double: float) -> float: ...
    def arcnc(self, double: float) -> float: ...
    def arcnd(self, double: float) -> float: ...
    def arcns(self, double: float) -> float: ...
    def arcsc(self, double: float) -> float: ...
    def arcsd(self, double: float) -> float: ...
    def arcsn(self, double: float) -> float: ...
    def getM(self) -> float: ...
    def valuesC(self, double: float) -> CopolarC: ...
    def valuesD(self, double: float) -> CopolarD: ...
    def valuesN(self, double: float) -> CopolarN: ...
    def valuesS(self, double: float) -> CopolarS: ...

class JacobiEllipticBuilder:
    _build_0__T = typing.TypeVar('_build_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _build_2__T = typing.TypeVar('_build_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def build(t: _build_0__T) -> FieldJacobiElliptic[_build_0__T]: ...
    @typing.overload
    @staticmethod
    def build(complex: org.hipparchus.complex.Complex) -> FieldJacobiElliptic[org.hipparchus.complex.Complex]: ...
    @typing.overload
    @staticmethod
    def build(fieldComplex: org.hipparchus.complex.FieldComplex[_build_2__T]) -> FieldJacobiElliptic[org.hipparchus.complex.FieldComplex[_build_2__T]]: ...
    @typing.overload
    @staticmethod
    def build(double: float) -> JacobiElliptic: ...

class JacobiTheta:
    def __init__(self, double: float): ...
    def getQ(self) -> float: ...
    def values(self, complex: org.hipparchus.complex.Complex) -> 'Theta': ...

class Theta:
    def theta1(self) -> org.hipparchus.complex.Complex: ...
    def theta2(self) -> org.hipparchus.complex.Complex: ...
    def theta3(self) -> org.hipparchus.complex.Complex: ...
    def theta4(self) -> org.hipparchus.complex.Complex: ...


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
    class-use: org.hipparchus.special.elliptic.jacobi.class-use.__module_protocol__
