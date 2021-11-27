import org.hipparchus
import org.hipparchus.complex
import typing



class LegendreEllipticIntegral:
    _bigD_2__T = typing.TypeVar('_bigD_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_3__T = typing.TypeVar('_bigD_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_6__T = typing.TypeVar('_bigD_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigD_7__T = typing.TypeVar('_bigD_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigD(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigD(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigD(t: _bigD_2__T) -> _bigD_2__T: ...
    @typing.overload
    @staticmethod
    def bigD(t: _bigD_3__T, t2: _bigD_3__T) -> _bigD_3__T: ...
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
    def bigE(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigE(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigE(t: _bigE_2__T) -> _bigE_2__T: ...
    @typing.overload
    @staticmethod
    def bigE(t: _bigE_3__T, t2: _bigE_3__T) -> _bigE_3__T: ...
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
    def bigE(fieldComplex: org.hipparchus.complex.FieldComplex[_bigE_9__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigE_9__T], fieldComplexUnivariateIntegrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigE_9__T], int: int) -> org.hipparchus.complex.FieldComplex[_bigE_9__T]: ...
    _bigF_1__T = typing.TypeVar('_bigF_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigF_4__T = typing.TypeVar('_bigF_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigF_5__T = typing.TypeVar('_bigF_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigF(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigF(t: _bigF_1__T, t2: _bigF_1__T) -> _bigF_1__T: ...
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
    def bigF(fieldComplex: org.hipparchus.complex.FieldComplex[_bigF_5__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigF_5__T], fieldComplexUnivariateIntegrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigF_5__T], int: int) -> org.hipparchus.complex.FieldComplex[_bigF_5__T]: ...
    _bigK_1__T = typing.TypeVar('_bigK_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bigK_3__T = typing.TypeVar('_bigK_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bigK(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigK(t: _bigK_1__T) -> _bigK_1__T: ...
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
    def bigKPrime(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigKPrime(t: _bigKPrime_1__T) -> _bigKPrime_1__T: ...
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
    def bigPi(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigPi(double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    @staticmethod
    def bigPi(t: _bigPi_2__T, t2: _bigPi_2__T) -> _bigPi_2__T: ...
    @typing.overload
    @staticmethod
    def bigPi(t: _bigPi_3__T, t2: _bigPi_3__T, t3: _bigPi_3__T) -> _bigPi_3__T: ...
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
    def bigPi(fieldComplex: org.hipparchus.complex.FieldComplex[_bigPi_9__T], fieldComplex2: org.hipparchus.complex.FieldComplex[_bigPi_9__T], fieldComplex3: org.hipparchus.complex.FieldComplex[_bigPi_9__T], fieldComplexUnivariateIntegrator: org.hipparchus.complex.FieldComplexUnivariateIntegrator[_bigPi_9__T], int: int) -> org.hipparchus.complex.FieldComplex[_bigPi_9__T]: ...
    _nome_1__T = typing.TypeVar('_nome_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def nome(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def nome(t: _nome_1__T) -> _nome_1__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special.elliptic.legendre")``.

    LegendreEllipticIntegral: typing.Type[LegendreEllipticIntegral]
