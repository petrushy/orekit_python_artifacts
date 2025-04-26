
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import org.hipparchus.geometry
import typing



_Encloser__S = typing.TypeVar('_Encloser__S', bound=org.hipparchus.geometry.Space)  # <S>
_Encloser__P = typing.TypeVar('_Encloser__P', bound=org.hipparchus.geometry.Point)  # <P>
class Encloser(typing.Generic[_Encloser__S, _Encloser__P]):
    """
    public interfaceEncloser<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>>
    
        Interface for algorithms computing enclosing balls.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.enclosing.EnclosingBall`
    """
    def enclose(self, iterable: typing.Union[java.lang.Iterable[_Encloser__P], typing.Sequence[_Encloser__P], typing.Set[_Encloser__P], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> 'EnclosingBall'[_Encloser__S, _Encloser__P]: ...

_EnclosingBall__S = typing.TypeVar('_EnclosingBall__S', bound=org.hipparchus.geometry.Space)  # <S>
_EnclosingBall__P = typing.TypeVar('_EnclosingBall__P', bound=org.hipparchus.geometry.Point)  # <P>
class EnclosingBall(java.io.Serializable, typing.Generic[_EnclosingBall__S, _EnclosingBall__P]):
    """
    public classEnclosingBall<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>> extends :class:`~org.hipparchus.geometry.enclosing.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.enclosing.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class represents a ball enclosing some points.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.Space`
              - :class:`~org.hipparchus.geometry.Point`
              - :class:`~org.hipparchus.geometry.enclosing.Encloser`
              - :meth:`~serialized`
    """
    def __init__(self, p: _EnclosingBall__P, double: float, *p2: _EnclosingBall__P): ...
    @typing.overload
    def contains(self, p: _EnclosingBall__P) -> bool:
        """
            Check if a point is within the ball or at boundary.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.enclosing.EnclosingBall`): point to test
        
            Returns:
                true if the point is within the ball or at boundary
        
            Check if a point is within an enlarged ball or at boundary.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.enclosing.EnclosingBall`): point to test
                margin (double): margin to consider
        
            Returns:
                true if the point is within the ball enlarged by the margin or at boundary
        
        
        """
        ...
    @typing.overload
    def contains(self, p: _EnclosingBall__P, double: float) -> bool: ...
    def getCenter(self) -> _EnclosingBall__P:
        """
            Get the center of the ball.
        
            Returns:
                center of the ball
        
        
        """
        ...
    def getRadius(self) -> float:
        """
            Get the radius of the ball.
        
            Returns:
                radius of the ball (can be negative if the ball is empty)
        
        
        """
        ...
    def getSupport(self) -> typing.MutableSequence[_EnclosingBall__P]:
        """
            Get the support points used to define the ball.
        
            Returns:
                support points used to define the ball
        
        
        """
        ...
    def getSupportSize(self) -> int:
        """
            Get the number of support points used to define the ball.
        
            Returns:
                number of support points used to define the ball
        
        
        """
        ...

_SupportBallGenerator__S = typing.TypeVar('_SupportBallGenerator__S', bound=org.hipparchus.geometry.Space)  # <S>
_SupportBallGenerator__P = typing.TypeVar('_SupportBallGenerator__P', bound=org.hipparchus.geometry.Point)  # <P>
class SupportBallGenerator(typing.Generic[_SupportBallGenerator__S, _SupportBallGenerator__P]):
    """
    public interfaceSupportBallGenerator<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>>
    
        Interface for generating balls based on support points.
    
        This generator is used in the :class:`~org.hipparchus.geometry.enclosing.WelzlEncloser` algorithm and its derivatives.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.enclosing.EnclosingBall`
    """
    def ballOnSupport(self, list: java.util.List[_SupportBallGenerator__P]) -> EnclosingBall[_SupportBallGenerator__S, _SupportBallGenerator__P]: ...

_WelzlEncloser__S = typing.TypeVar('_WelzlEncloser__S', bound=org.hipparchus.geometry.Space)  # <S>
_WelzlEncloser__P = typing.TypeVar('_WelzlEncloser__P', bound=org.hipparchus.geometry.Point)  # <P>
class WelzlEncloser(Encloser[_WelzlEncloser__S, _WelzlEncloser__P], typing.Generic[_WelzlEncloser__S, _WelzlEncloser__P]):
    """
    public classWelzlEncloser<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>> extends :class:`~org.hipparchus.geometry.enclosing.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.enclosing.Encloser`<S,P>
    
        Class implementing Emo Welzl algorithm to find the smallest enclosing ball in linear time.
    
        The class implements the algorithm described in paper `Smallest Enclosing Disks (Balls and Ellipsoids)
        <http://www.inf.ethz.ch/personal/emo/PublFiles/SmallEnclDisk_LNCS555_91.pdf>` by Emo Welzl, Lecture Notes in Computer
        Science 555 (1991) 359-370. The pivoting improvement published in the paper `Fast and Robust Smallest Enclosing Balls
        <http://www.inf.ethz.ch/personal/gaertner/texts/own_work/esa99_final.pdf>`, by Bernd Gärtner and further modified in
        paper ` Efficient Computation of Smallest Enclosing Balls in Three Dimensions
        <http://www.idt.mdh.se/kurser/ct3340/ht12/MINICONFERENCE/FinalPapers/ircse12_submission_30.pdf>` by Linus Källberg to
        avoid performing local copies of data have been included.
    """
    def __init__(self, double: float, supportBallGenerator: typing.Union[SupportBallGenerator[_WelzlEncloser__S, _WelzlEncloser__P], typing.Callable[[java.util.List[org.hipparchus.geometry.Point]], EnclosingBall[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point]]]): ...
    def enclose(self, iterable: typing.Union[java.lang.Iterable[_WelzlEncloser__P], typing.Sequence[_WelzlEncloser__P], typing.Set[_WelzlEncloser__P], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> EnclosingBall[_WelzlEncloser__S, _WelzlEncloser__P]: ...
    def selectFarthest(self, iterable: typing.Union[java.lang.Iterable[_WelzlEncloser__P], typing.Sequence[_WelzlEncloser__P], typing.Set[_WelzlEncloser__P], typing.Callable[[], java.util.Iterator[typing.Any]]], enclosingBall: EnclosingBall[_WelzlEncloser__S, _WelzlEncloser__P]) -> _WelzlEncloser__P: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.enclosing")``.

    Encloser: typing.Type[Encloser]
    EnclosingBall: typing.Type[EnclosingBall]
    SupportBallGenerator: typing.Type[SupportBallGenerator]
    WelzlEncloser: typing.Type[WelzlEncloser]
