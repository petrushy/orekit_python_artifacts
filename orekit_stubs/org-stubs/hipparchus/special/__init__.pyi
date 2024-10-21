import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.special.class-use
import org.hipparchus.special.elliptic
import typing



class BesselJ(org.hipparchus.analysis.UnivariateFunction):
    def __init__(self, double: float): ...
    @staticmethod
    def rjBesl(double: float, double2: float, int: int) -> 'BesselJ.BesselJResult': ...
    @typing.overload
    def value(self, double: float) -> float: ...
    @typing.overload
    @staticmethod
    def value(double: float, double2: float) -> float: ...
    class BesselJResult:
        def __init__(self, doubleArray: typing.List[float], int: int): ...
        def getVals(self) -> typing.List[float]: ...
        def getnVals(self) -> int: ...

class Beta:
    @staticmethod
    def logBeta(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedBeta(double: float, double2: float, double3: float) -> float: ...
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
    _erf_2__T = typing.TypeVar('_erf_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _erf_3__T = typing.TypeVar('_erf_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erf(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def erf(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def erf(t: _erf_2__T) -> _erf_2__T: ...
    @typing.overload
    @staticmethod
    def erf(t: _erf_3__T, t2: _erf_3__T) -> _erf_3__T: ...
    _erfInv_1__T = typing.TypeVar('_erfInv_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erfInv(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def erfInv(t: _erfInv_1__T) -> _erfInv_1__T: ...
    _erfc_1__T = typing.TypeVar('_erfc_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erfc(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def erfc(t: _erfc_1__T) -> _erfc_1__T: ...
    _erfcInv_1__T = typing.TypeVar('_erfcInv_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def erfcInv(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def erfcInv(t: _erfcInv_1__T) -> _erfcInv_1__T: ...

class Gamma:
    GAMMA: typing.ClassVar[float] = ...
    LANCZOS_G: typing.ClassVar[float] = ...
    _digamma_1__T = typing.TypeVar('_digamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def digamma(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def digamma(t: _digamma_1__T) -> _digamma_1__T: ...
    _gamma_1__T = typing.TypeVar('_gamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def gamma(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def gamma(t: _gamma_1__T) -> _gamma_1__T: ...
    _invGamma1pm1_1__T = typing.TypeVar('_invGamma1pm1_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def invGamma1pm1(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def invGamma1pm1(t: _invGamma1pm1_1__T) -> _invGamma1pm1_1__T: ...
    _lanczos_1__T = typing.TypeVar('_lanczos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def lanczos(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def lanczos(t: _lanczos_1__T) -> _lanczos_1__T: ...
    _logGamma_1__T = typing.TypeVar('_logGamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def logGamma(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def logGamma(t: _logGamma_1__T) -> _logGamma_1__T: ...
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
    def regularizedGammaP(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(double: float, double2: float, double3: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(t: _regularizedGammaP_2__T, t2: _regularizedGammaP_2__T) -> _regularizedGammaP_2__T: ...
    @typing.overload
    @staticmethod
    def regularizedGammaP(t: _regularizedGammaP_3__T, t2: _regularizedGammaP_3__T, double: float, int: int) -> _regularizedGammaP_3__T: ...
    _regularizedGammaQ_2__T = typing.TypeVar('_regularizedGammaQ_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _regularizedGammaQ_3__T = typing.TypeVar('_regularizedGammaQ_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def regularizedGammaQ(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(double: float, double2: float, double3: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(t: _regularizedGammaQ_2__T, t2: _regularizedGammaQ_2__T) -> _regularizedGammaQ_2__T: ...
    @typing.overload
    @staticmethod
    def regularizedGammaQ(t: _regularizedGammaQ_3__T, t2: _regularizedGammaQ_3__T, double: float, int: int) -> _regularizedGammaQ_3__T: ...
    _trigamma_1__T = typing.TypeVar('_trigamma_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def trigamma(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def trigamma(t: _trigamma_1__T) -> _trigamma_1__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special")``.

    BesselJ: typing.Type[BesselJ]
    Beta: typing.Type[Beta]
    Erf: typing.Type[Erf]
    Gamma: typing.Type[Gamma]
    class-use: org.hipparchus.special.class-use.__module_protocol__
    elliptic: org.hipparchus.special.elliptic.__module_protocol__
