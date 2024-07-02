import org.hipparchus
import org.hipparchus.complex
import typing



class CarlsonEllipticIntegral:
    _rC_1__T = typing.TypeVar('_rC_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rC_3__T = typing.TypeVar('_rC_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rC(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def rC(t: _rC_1__T, t2: _rC_1__T) -> _rC_1__T: ...
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
    def rD(double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    @staticmethod
    def rD(t: _rD_1__T, t2: _rD_1__T, t3: _rD_1__T) -> _rD_1__T: ...
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
    def rF(double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    @staticmethod
    def rF(t: _rF_1__T, t2: _rF_1__T, t3: _rF_1__T) -> _rF_1__T: ...
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
    def rG(double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    @staticmethod
    def rG(t: _rG_1__T, t2: _rG_1__T, t3: _rG_1__T) -> _rG_1__T: ...
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
    def rJ(double: float, double2: float, double3: float, double4: float) -> float: ...
    @typing.overload
    @staticmethod
    def rJ(double: float, double2: float, double3: float, double4: float, double5: float) -> float: ...
    @typing.overload
    @staticmethod
    def rJ(t: _rJ_2__T, t2: _rJ_2__T, t3: _rJ_2__T, t4: _rJ_2__T) -> _rJ_2__T: ...
    @typing.overload
    @staticmethod
    def rJ(t: _rJ_3__T, t2: _rJ_3__T, t3: _rJ_3__T, t4: _rJ_3__T, t5: _rJ_3__T) -> _rJ_3__T: ...
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special.elliptic.carlson")``.

    CarlsonEllipticIntegral: typing.Type[CarlsonEllipticIntegral]
