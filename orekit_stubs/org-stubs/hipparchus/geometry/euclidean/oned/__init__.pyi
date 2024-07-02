import java.io
import java.lang
import java.text
import java.util
import org.hipparchus.exception
import org.hipparchus.geometry
import org.hipparchus.geometry.partitioning
import typing



class Euclidean1D(java.io.Serializable, org.hipparchus.geometry.Space):
    def getDimension(self) -> int: ...
    @staticmethod
    def getInstance() -> 'Euclidean1D': ...
    def getSubSpace(self) -> org.hipparchus.geometry.Space: ...
    class NoSubSpaceException(org.hipparchus.exception.MathRuntimeException):
        def __init__(self): ...

class Interval:
    def __init__(self, double: float, double2: float): ...
    def checkPoint(self, double: float, double2: float) -> org.hipparchus.geometry.partitioning.Region.Location: ...
    def getBarycenter(self) -> float: ...
    def getInf(self) -> float: ...
    def getSize(self) -> float: ...
    def getSup(self) -> float: ...

class IntervalsSet(org.hipparchus.geometry.partitioning.AbstractRegion[Euclidean1D, Euclidean1D], java.lang.Iterable[typing.List[float]]):
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[org.hipparchus.geometry.partitioning.SubHyperplane[Euclidean1D]], typing.Sequence[org.hipparchus.geometry.partitioning.SubHyperplane[Euclidean1D]], typing.Set[org.hipparchus.geometry.partitioning.SubHyperplane[Euclidean1D]]], double: float): ...
    @typing.overload
    def __init__(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean1D], double: float): ...
    def asList(self) -> java.util.List[Interval]: ...
    def buildNew(self, bSPTree: org.hipparchus.geometry.partitioning.BSPTree[Euclidean1D]) -> 'IntervalsSet': ...
    def getInf(self) -> float: ...
    def getSup(self) -> float: ...
    def iterator(self) -> java.util.Iterator[typing.List[float]]: ...
    def projectToBoundary(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> org.hipparchus.geometry.partitioning.BoundaryProjection[Euclidean1D]: ...

class OrientedPoint(org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D]):
    def __init__(self, vector1D: 'Vector1D', boolean: bool, double: float): ...
    def copySelf(self) -> 'OrientedPoint': ...
    def emptyHyperplane(self) -> 'SubOrientedPoint': ...
    def getLocation(self) -> 'Vector1D': ...
    @typing.overload
    def getOffset(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> float: ...
    @typing.overload
    def getOffset(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
    def getTolerance(self) -> float: ...
    def isDirect(self) -> bool: ...
    def project(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> org.hipparchus.geometry.Point[Euclidean1D]: ...
    def revertSelf(self) -> None: ...
    def sameOrientationAs(self, hyperplane: org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D]) -> bool: ...
    def wholeHyperplane(self) -> 'SubOrientedPoint': ...
    def wholeSpace(self) -> IntervalsSet: ...

class SubOrientedPoint(org.hipparchus.geometry.partitioning.AbstractSubHyperplane[Euclidean1D, Euclidean1D]):
    def __init__(self, hyperplane: org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D], region: org.hipparchus.geometry.partitioning.Region[Euclidean1D]): ...
    def getSize(self) -> float: ...
    def isEmpty(self) -> bool: ...
    def split(self, hyperplane: org.hipparchus.geometry.partitioning.Hyperplane[Euclidean1D]) -> org.hipparchus.geometry.partitioning.SubHyperplane.SplitSubHyperplane[Euclidean1D]: ...

class Vector1D(org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']):
    ZERO: typing.ClassVar['Vector1D'] = ...
    ONE: typing.ClassVar['Vector1D'] = ...
    NaN: typing.ClassVar['Vector1D'] = ...
    POSITIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    NEGATIVE_INFINITY: typing.ClassVar['Vector1D'] = ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D', double3: float, vector1D3: 'Vector1D'): ...
    @typing.overload
    def __init__(self, double: float, vector1D: 'Vector1D', double2: float, vector1D2: 'Vector1D', double3: float, vector1D3: 'Vector1D', double4: float, vector1D4: 'Vector1D'): ...
    @typing.overload
    def add(self, double: float, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def add(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def distance(self, point: org.hipparchus.geometry.Point[Euclidean1D]) -> float: ...
    @typing.overload
    @staticmethod
    def distance(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def distance1(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
    @typing.overload
    def distanceInf(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
    @typing.overload
    @staticmethod
    def distanceInf(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    @typing.overload
    def distanceSq(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
    @typing.overload
    @staticmethod
    def distanceSq(vector1D: 'Vector1D', vector1D2: 'Vector1D') -> float: ...
    def dotProduct(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> float: ...
    def equals(self, object: typing.Any) -> bool: ...
    def equalsIeee754(self, object: typing.Any) -> bool: ...
    def getNorm(self) -> float: ...
    def getNorm1(self) -> float: ...
    def getNormInf(self) -> float: ...
    def getNormSq(self) -> float: ...
    def getSpace(self) -> org.hipparchus.geometry.Space: ...
    def getX(self) -> float: ...
    def getZero(self) -> 'Vector1D': ...
    def hashCode(self) -> int: ...
    def isInfinite(self) -> bool: ...
    def isNaN(self) -> bool: ...
    def negate(self) -> 'Vector1D': ...
    def scalarMultiply(self, double: float) -> 'Vector1D': ...
    @typing.overload
    def subtract(self, double: float, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def subtract(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, 'Vector1D']) -> 'Vector1D': ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, numberFormat: java.text.NumberFormat) -> str: ...

class Vector1DFormat(org.hipparchus.geometry.VectorFormat[Euclidean1D, Vector1D]):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[org.hipparchus.geometry.Space, org.hipparchus.geometry.Vector]) -> str: ...
    @typing.overload
    def format(self, vector: org.hipparchus.geometry.Vector[Euclidean1D, Vector1D], stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def getVector1DFormat() -> 'Vector1DFormat': ...
    @typing.overload
    @staticmethod
    def getVector1DFormat(locale: java.util.Locale) -> 'Vector1DFormat': ...
    @typing.overload
    def parse(self, string: str) -> Vector1D: ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Vector1D: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean.oned")``.

    Euclidean1D: typing.Type[Euclidean1D]
    Interval: typing.Type[Interval]
    IntervalsSet: typing.Type[IntervalsSet]
    OrientedPoint: typing.Type[OrientedPoint]
    SubOrientedPoint: typing.Type[SubOrientedPoint]
    Vector1D: typing.Type[Vector1D]
    Vector1DFormat: typing.Type[Vector1DFormat]
