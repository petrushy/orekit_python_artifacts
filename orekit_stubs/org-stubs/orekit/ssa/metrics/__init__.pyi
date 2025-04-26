
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import typing



_FieldProbabilityOfCollision__T = typing.TypeVar('_FieldProbabilityOfCollision__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldProbabilityOfCollision(typing.Generic[_FieldProbabilityOfCollision__T]):
    """
    public class FieldProbabilityOfCollision<T extends :class:`~org.orekit.ssa.metrics.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.ssa.metrics.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for values relative to the probability of collision :
    
          - Value of the probability of collision.
          - Name of the method with which it was computed.
          - Upper and lower limit of the value if the method provides them (such as
            :class:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.Laas2015` for example).
          - Flag defining if the probability was maximized in any way (such as
            :class:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.Alfriend1999Max` for example).
    
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, t: _FieldProbabilityOfCollision__T, string: str): ...
    @typing.overload
    def __init__(self, t: _FieldProbabilityOfCollision__T, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, t: _FieldProbabilityOfCollision__T, t2: _FieldProbabilityOfCollision__T, t3: _FieldProbabilityOfCollision__T, string: str, boolean: bool): ...
    def getLowerLimit(self) -> _FieldProbabilityOfCollision__T:
        """
            Get lower limit of the probability of collision value.
        
            Returns:
                lower limit of the probability of collision value, 0 by default
        
        
        """
        ...
    def getProbabilityOfCollisionMethodName(self) -> str:
        """
            Get name of the probability computing method with which this probability was computed.
        
            Returns:
                name of the probability computing method with which this probability was computed
        
        
        """
        ...
    def getUpperLimit(self) -> _FieldProbabilityOfCollision__T:
        """
            Get upper limit of the probability of collision value.
        
            Returns:
                upper limit of the probability of collision value, 0 by default
        
        
        """
        ...
    def getValue(self) -> _FieldProbabilityOfCollision__T:
        """
            Get value of the probability of collision.
        
            Returns:
                value of the probability of collision
        
        
        """
        ...
    def isMaxProbability(self) -> bool:
        """
            Get flag that defines if this probability of collision can be considered a maximum probability of collision.
        
            Returns:
                flag that defines if this probability of collision can be considered a maximum probability of collision
        
        
        """
        ...

class ProbabilityOfCollision:
    """
    public class ProbabilityOfCollision extends :class:`~org.orekit.ssa.metrics.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for values relative to the probability of collision :
    
          - Value of the probability of collision.
          - Name of the method with which it was computed.
          - Upper and lower limit of the value if the method provides them (such as
            :class:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.Laas2015` for example).
          - Flag defining if the probability was maximized in any way (such as
            :class:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.Alfriend1999Max` for example).
    
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, string: str): ...
    @typing.overload
    def __init__(self, double: float, string: str, boolean: bool): ...
    def getLowerLimit(self) -> float:
        """
            Get lower limit of the probability of collision value.
        
            Returns:
                lower limit of the probability of collision value, 0 by default
        
        
        """
        ...
    def getProbabilityOfCollisionMethodName(self) -> str:
        """
            Get name of the probability computing method with which this probability was computed.
        
            Returns:
                name of the probability computing method with which this probability was computed
        
        
        """
        ...
    def getUpperLimit(self) -> float:
        """
            Get upper limit of the probability of collision value.
        
            Returns:
                upper limit of the probability of collision value, 0 by default
        
        
        """
        ...
    def getValue(self) -> float:
        """
            Get value of the probability of collision.
        
            Returns:
                value of the probability of collision
        
        
        """
        ...
    def isMaxProbability(self) -> bool:
        """
            Get flag that defines if this probability of collision can be considered a maximum probability of collision.
        
            Returns:
                flag that defines if this probability of collision can be considered a maximum probability of collision
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.ssa.metrics")``.

    FieldProbabilityOfCollision: typing.Type[FieldProbabilityOfCollision]
    ProbabilityOfCollision: typing.Type[ProbabilityOfCollision]
