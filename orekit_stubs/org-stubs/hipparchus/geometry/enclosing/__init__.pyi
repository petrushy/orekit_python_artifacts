import java.io
import java.lang
import java.util
import org.hipparchus.geometry
import typing



_Encloser__S = typing.TypeVar('_Encloser__S', bound=org.hipparchus.geometry.Space)  # <S>
_Encloser__P = typing.TypeVar('_Encloser__P', bound=org.hipparchus.geometry.Point)  # <P>
class Encloser(typing.Generic[_Encloser__S, _Encloser__P]):
    def enclose(self, iterable: typing.Union[java.lang.Iterable[_Encloser__P], typing.Sequence[_Encloser__P], typing.Set[_Encloser__P]]) -> 'EnclosingBall'[_Encloser__S, _Encloser__P]: ...

_EnclosingBall__S = typing.TypeVar('_EnclosingBall__S', bound=org.hipparchus.geometry.Space)  # <S>
_EnclosingBall__P = typing.TypeVar('_EnclosingBall__P', bound=org.hipparchus.geometry.Point)  # <P>
class EnclosingBall(java.io.Serializable, typing.Generic[_EnclosingBall__S, _EnclosingBall__P]):
    def __init__(self, p: _EnclosingBall__P, double: float, *p2: _EnclosingBall__P): ...
    @typing.overload
    def contains(self, p: _EnclosingBall__P) -> bool: ...
    @typing.overload
    def contains(self, p: _EnclosingBall__P, double: float) -> bool: ...
    def getCenter(self) -> _EnclosingBall__P: ...
    def getRadius(self) -> float: ...
    def getSupport(self) -> typing.List[_EnclosingBall__P]: ...
    def getSupportSize(self) -> int: ...

_SupportBallGenerator__S = typing.TypeVar('_SupportBallGenerator__S', bound=org.hipparchus.geometry.Space)  # <S>
_SupportBallGenerator__P = typing.TypeVar('_SupportBallGenerator__P', bound=org.hipparchus.geometry.Point)  # <P>
class SupportBallGenerator(typing.Generic[_SupportBallGenerator__S, _SupportBallGenerator__P]):
    def ballOnSupport(self, list: java.util.List[_SupportBallGenerator__P]) -> EnclosingBall[_SupportBallGenerator__S, _SupportBallGenerator__P]: ...

_WelzlEncloser__S = typing.TypeVar('_WelzlEncloser__S', bound=org.hipparchus.geometry.Space)  # <S>
_WelzlEncloser__P = typing.TypeVar('_WelzlEncloser__P', bound=org.hipparchus.geometry.Point)  # <P>
class WelzlEncloser(Encloser[_WelzlEncloser__S, _WelzlEncloser__P], typing.Generic[_WelzlEncloser__S, _WelzlEncloser__P]):
    def __init__(self, double: float, supportBallGenerator: SupportBallGenerator[_WelzlEncloser__S, _WelzlEncloser__P]): ...
    def enclose(self, iterable: typing.Union[java.lang.Iterable[_WelzlEncloser__P], typing.Sequence[_WelzlEncloser__P], typing.Set[_WelzlEncloser__P]]) -> EnclosingBall[_WelzlEncloser__S, _WelzlEncloser__P]: ...
    def selectFarthest(self, iterable: typing.Union[java.lang.Iterable[_WelzlEncloser__P], typing.Sequence[_WelzlEncloser__P], typing.Set[_WelzlEncloser__P]], enclosingBall: EnclosingBall[_WelzlEncloser__S, _WelzlEncloser__P]) -> _WelzlEncloser__P: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.enclosing")``.

    Encloser: typing.Type[Encloser]
    EnclosingBall: typing.Type[EnclosingBall]
    SupportBallGenerator: typing.Type[SupportBallGenerator]
    WelzlEncloser: typing.Type[WelzlEncloser]
