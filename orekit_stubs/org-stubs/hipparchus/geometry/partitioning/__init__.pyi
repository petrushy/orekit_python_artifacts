import java.lang
import java.util
import org.hipparchus.geometry
import typing



_BSPTree__LeafMerger__S = typing.TypeVar('_BSPTree__LeafMerger__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__VanishingCutHandler__S = typing.TypeVar('_BSPTree__VanishingCutHandler__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__S = typing.TypeVar('_BSPTree__S', bound=org.hipparchus.geometry.Space)  # <S>
class BSPTree(typing.Generic[_BSPTree__S]):
    """
    public class BSPTree<S extends :class:`~org.hipparchus.geometry.Space`> extends Object
    
        This class represent a Binary Space Partition tree.
    
        BSP trees are an efficient way to represent space partitions and to associate attributes with each cell. Each node in a
        BSP tree represents a convex region which is partitioned in two convex sub-regions at each side of a cut hyperplane. The
        root tree contains the complete space.
    
        The main use of such partitions is to use a boolean attribute to define an inside/outside property, hence representing
        arbitrary polytopes (line segments in 1D, polygons in 2D and polyhedrons in 3D) and to operate on them.
    
        Another example would be to represent Voronoi tesselations, the attribute of each cell holding the defining point of the
        cell.
    
        The application-defined attributes are shared among copied instances and propagated to split parts. These attributes are
        not used by the BSP-tree algorithms themselves, so the application can use them for any purpose. Since the tree visiting
        method holds internal and leaf nodes differently, it is possible to use different classes for internal nodes attributes
        and leaf nodes attributes. This should be used with care, though, because if the tree is modified in any way after
        attributes have been set, some internal nodes may become leaf nodes and some leaf nodes may become internal nodes.
    
        One of the main sources for the development of this package was Bruce Naylor, John Amanatides and William Thibault paper
        `Merging BSP Trees Yields Polyhedral Set Operations <http://www.cs.yorku.ca/~amana/research/bsptSetOp.pdf>` Proc.
        Siggraph '90, Computer Graphics 24(4), August 1990, pp 115-124, published by the Association for Computing Machinery
        (ACM).
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, object: typing.Any): ...
    @typing.overload
    def __init__(self, subHyperplane: 'SubHyperplane'[_BSPTree__S], bSPTree: 'BSPTree'[_BSPTree__S], bSPTree2: 'BSPTree'[_BSPTree__S], object: typing.Any): ...
    def copySelf(self) -> 'BSPTree'[_BSPTree__S]: ...
    def getAttribute(self) -> typing.Any:
        """
            Get the attribute associated with the instance.
        
            Returns:
                attribute associated with the node or null if no attribute has been explicitly set using the
                :meth:`~org.hipparchus.geometry.partitioning.BSPTree.setAttribute` method
        
            Also see:
                :meth:`~org.hipparchus.geometry.partitioning.BSPTree.setAttribute`
        
        
        """
        ...
    def getCell(self, point: org.hipparchus.geometry.Point[_BSPTree__S], double: float) -> 'BSPTree'[_BSPTree__S]: ...
    def getCloseCuts(self, point: org.hipparchus.geometry.Point[_BSPTree__S], double: float) -> java.util.List['BSPTree'[_BSPTree__S]]: ...
    def getCut(self) -> 'SubHyperplane'[_BSPTree__S]: ...
    def getMinus(self) -> 'BSPTree'[_BSPTree__S]: ...
    def getParent(self) -> 'BSPTree'[_BSPTree__S]: ...
    def getPlus(self) -> 'BSPTree'[_BSPTree__S]: ...
    def insertCut(self, hyperplane: 'Hyperplane'[_BSPTree__S]) -> bool: ...
    def insertInTree(self, bSPTree: 'BSPTree'[_BSPTree__S], boolean: bool, vanishingCutHandler: 'BSPTree.VanishingCutHandler'[_BSPTree__S]) -> None: ...
    def merge(self, bSPTree: 'BSPTree'[_BSPTree__S], leafMerger: 'BSPTree.LeafMerger'[_BSPTree__S]) -> 'BSPTree'[_BSPTree__S]: ...
    def pruneAroundConvexCell(self, object: typing.Any, object2: typing.Any, object3: typing.Any) -> 'BSPTree'[_BSPTree__S]: ...
    def setAttribute(self, object: typing.Any) -> None:
        """
            Associate an attribute with the instance.
        
            Parameters:
                attribute (Object): attribute to associate with the node
        
            Also see:
                :meth:`~org.hipparchus.geometry.partitioning.BSPTree.getAttribute`
        
        
        """
        ...
    def split(self, subHyperplane: 'SubHyperplane'[_BSPTree__S]) -> 'BSPTree'[_BSPTree__S]: ...
    def visit(self, bSPTreeVisitor: 'BSPTreeVisitor'[_BSPTree__S]) -> None: ...
    class LeafMerger(typing.Generic[_BSPTree__LeafMerger__S]):
        def merge(self, bSPTree: 'BSPTree'[_BSPTree__LeafMerger__S], bSPTree2: 'BSPTree'[_BSPTree__LeafMerger__S], bSPTree3: 'BSPTree'[_BSPTree__LeafMerger__S], boolean: bool, boolean2: bool) -> 'BSPTree'[_BSPTree__LeafMerger__S]: ...
    class VanishingCutHandler(typing.Generic[_BSPTree__VanishingCutHandler__S]):
        def fixNode(self, bSPTree: 'BSPTree'[_BSPTree__VanishingCutHandler__S]) -> 'BSPTree'[_BSPTree__VanishingCutHandler__S]: ...

_BSPTreeVisitor__S = typing.TypeVar('_BSPTreeVisitor__S', bound=org.hipparchus.geometry.Space)  # <S>
class BSPTreeVisitor(typing.Generic[_BSPTreeVisitor__S]):
    """
    public interface BSPTreeVisitor<S extends :class:`~org.hipparchus.geometry.Space`>
    
        This interface is used to visit :class:`~org.hipparchus.geometry.partitioning.BSPTree` nodes.
    
        Navigation through :class:`~org.hipparchus.geometry.partitioning.BSPTree` can be done using two different point of
        views:
    
          - the first one is in a node-oriented way using the :meth:`~org.hipparchus.geometry.partitioning.BSPTree.getPlus`,
            :meth:`~org.hipparchus.geometry.partitioning.BSPTree.getMinus` and
            :meth:`~org.hipparchus.geometry.partitioning.BSPTree.getParent` methods. Terminal nodes without associated
            :class:`~org.hipparchus.geometry.partitioning.SubHyperplane` can be visited this way, there is no constraint in the
            visit order, and it is possible to visit either all nodes or only a subset of the nodes
          - the second one is in a sub-hyperplane-oriented way using classes implementing this interface which obeys the visitor
            design pattern. The visit order is provided by the visitor as each node is first encountered. Each node is visited
            exactly once.
    
    
        Also see:
            :class:`~org.hipparchus.geometry.partitioning.BSPTree`, :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
    """
    def visitInternalNode(self, bSPTree: BSPTree[_BSPTreeVisitor__S]) -> None: ...
    def visitLeafNode(self, bSPTree: BSPTree[_BSPTreeVisitor__S]) -> None: ...
    def visitOrder(self, bSPTree: BSPTree[_BSPTreeVisitor__S]) -> 'BSPTreeVisitor.Order': ...
    class Order(java.lang.Enum['BSPTreeVisitor.Order']):
        PLUS_MINUS_SUB: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        PLUS_SUB_MINUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        MINUS_PLUS_SUB: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        MINUS_SUB_PLUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        SUB_PLUS_MINUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        SUB_MINUS_PLUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'BSPTreeVisitor.Order': ...
        @staticmethod
        def values() -> typing.List['BSPTreeVisitor.Order']: ...

_BoundaryAttribute__S = typing.TypeVar('_BoundaryAttribute__S', bound=org.hipparchus.geometry.Space)  # <S>
class BoundaryAttribute(typing.Generic[_BoundaryAttribute__S]):
    """
    public class BoundaryAttribute<S extends :class:`~org.hipparchus.geometry.Space`> extends Object
    
        Class holding boundary attributes.
    
        This class is used for the attributes associated with the nodes of region boundary shell trees returned by the
        :meth:`~org.hipparchus.geometry.partitioning.Region.getTree` when the boolean :code:`includeBoundaryAttributes`
        parameter is set to :code:`true`. It contains the parts of the node cut sub-hyperplane that belong to the boundary.
    
        This class is a simple placeholder, it does not provide any processing methods.
    
        Also see:
            :meth:`~org.hipparchus.geometry.partitioning.Region.getTree`
    """
    def getPlusInside(self) -> 'SubHyperplane'[_BoundaryAttribute__S]: ...
    def getPlusOutside(self) -> 'SubHyperplane'[_BoundaryAttribute__S]: ...
    def getSplitters(self) -> 'NodesSet'[_BoundaryAttribute__S]: ...

_BoundaryProjection__S = typing.TypeVar('_BoundaryProjection__S', bound=org.hipparchus.geometry.Space)  # <S>
class BoundaryProjection(typing.Generic[_BoundaryProjection__S]):
    """
    public class BoundaryProjection<S extends :class:`~org.hipparchus.geometry.Space`> extends Object
    
        Class holding the result of point projection on region boundary.
    
        This class is a simple placeholder, it does not provide any processing methods.
    
        Instances of this class are guaranteed to be immutable
    
        Also see:
            :meth:`~org.hipparchus.geometry.partitioning.AbstractRegion.projectToBoundary`
    """
    def __init__(self, point: org.hipparchus.geometry.Point[_BoundaryProjection__S], point2: org.hipparchus.geometry.Point[_BoundaryProjection__S], double: float): ...
    def getOffset(self) -> float:
        """
            Offset of the point with respect to the boundary it is projected on.
        
            The offset with respect to the boundary is negative if the
            :meth:`~org.hipparchus.geometry.partitioning.BoundaryProjection.getOriginal` is inside the region, and positive
            otherwise.
        
            If there are no boundary, the value is set to either :code:`Double.POSITIVE_INFINITY` if the region is empty (i.e. all
            points are outside of the region) or :code:`Double.NEGATIVE_INFINITY` if the region covers the whole space (i.e. all
            points are inside of the region).
        
            Returns:
                offset of the point with respect to the boundary it is projected on
        
        
        """
        ...
    def getOriginal(self) -> org.hipparchus.geometry.Point[_BoundaryProjection__S]: ...
    def getProjected(self) -> org.hipparchus.geometry.Point[_BoundaryProjection__S]: ...

_Embedding__S = typing.TypeVar('_Embedding__S', bound=org.hipparchus.geometry.Space)  # <S>
_Embedding__T = typing.TypeVar('_Embedding__T', bound=org.hipparchus.geometry.Space)  # <T>
class Embedding(typing.Generic[_Embedding__S, _Embedding__T]):
    """
    public interface Embedding<S extends :class:`~org.hipparchus.geometry.Space`,T extends :class:`~org.hipparchus.geometry.Space`>
    
        This interface defines mappers between a space and one of its sub-spaces.
    
        Sub-spaces are the lower dimensions subsets of a n-dimensions space. The (n-1)-dimension sub-spaces are specific
        sub-spaces known as :class:`~org.hipparchus.geometry.partitioning.Hyperplane`. This interface can be used regardless of
        the dimensions differences. As an example, :class:`~org.hipparchus.geometry.euclidean.threed.Line` in 3D implements
        Embedding< :class:`~org.hipparchus.geometry.euclidean.threed.Vector3D`,
        :class:`~org.hipparchus.geometry.euclidean.oned.Vector1D`>, i.e. it maps directly dimensions 3 and 1.
    
        In the 3D euclidean space, hyperplanes are 2D planes, and the 1D sub-spaces are lines.
    
        Note that this interface is *not* intended to be implemented by Hipparchus users, it is only intended to be implemented
        within the library itself. New methods may be added even for minor versions, which breaks compatibility for external
        implementations.
    
        Also see:
            :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
    """
    def toSpace(self, point: org.hipparchus.geometry.Point[_Embedding__T]) -> org.hipparchus.geometry.Point[_Embedding__S]: ...
    def toSubSpace(self, point: org.hipparchus.geometry.Point[_Embedding__S]) -> org.hipparchus.geometry.Point[_Embedding__T]: ...

_Hyperplane__S = typing.TypeVar('_Hyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
class Hyperplane(typing.Generic[_Hyperplane__S]):
    """
    public interface Hyperplane<S extends :class:`~org.hipparchus.geometry.Space`>
    
        This interface represents an hyperplane of a space.
    
        The most prominent place where hyperplane appears in space partitioning is as cutters. Each partitioning node in a
        :class:`~org.hipparchus.geometry.partitioning.BSPTree` has a cut
        :class:`~org.hipparchus.geometry.partitioning.SubHyperplane` which is either an hyperplane or a part of an hyperplane.
        In an n-dimensions euclidean space, an hyperplane is an (n-1)-dimensions hyperplane (for example a traditional plane in
        the 3D euclidean space). They can be more exotic objects in specific fields, for example a circle on the surface of the
        unit sphere.
    
        Note that this interface is *not* intended to be implemented by Hipparchus users, it is only intended to be implemented
        within the library itself. New methods may be added even for minor versions, which breaks compatibility for external
        implementations.
    """
    def copySelf(self) -> 'Hyperplane'[_Hyperplane__S]: ...
    def emptyHyperplane(self) -> 'SubHyperplane'[_Hyperplane__S]: ...
    def getOffset(self, point: org.hipparchus.geometry.Point[_Hyperplane__S]) -> float: ...
    def getTolerance(self) -> float:
        """
            Get the tolerance below which points are considered to belong to the hyperplane.
        
            Returns:
                tolerance below which points are considered to belong to the hyperplane
        
        
        """
        ...
    def project(self, point: org.hipparchus.geometry.Point[_Hyperplane__S]) -> org.hipparchus.geometry.Point[_Hyperplane__S]: ...
    def sameOrientationAs(self, hyperplane: 'Hyperplane'[_Hyperplane__S]) -> bool: ...
    def wholeHyperplane(self) -> 'SubHyperplane'[_Hyperplane__S]: ...
    def wholeSpace(self) -> 'Region'[_Hyperplane__S]: ...

_NodesSet__S = typing.TypeVar('_NodesSet__S', bound=org.hipparchus.geometry.Space)  # <S>
class NodesSet(java.lang.Iterable[BSPTree[_NodesSet__S]], typing.Generic[_NodesSet__S]):
    """
    public class NodesSet<S extends :class:`~org.hipparchus.geometry.Space`> extends Object implements Iterable<:class:`~org.hipparchus.geometry.partitioning.BSPTree`<S>>
    
        Set of :class:`~org.hipparchus.geometry.partitioning.BSPTree` nodes.
    
        Also see:
            :class:`~org.hipparchus.geometry.partitioning.BoundaryAttribute`
    """
    def __init__(self): ...
    def add(self, bSPTree: BSPTree[_NodesSet__S]) -> None: ...
    def addAll(self, iterable: typing.Union[java.lang.Iterable[BSPTree[_NodesSet__S]], typing.Sequence[BSPTree[_NodesSet__S]], typing.Set[BSPTree[_NodesSet__S]]]) -> None: ...
    def iterator(self) -> java.util.Iterator[BSPTree[_NodesSet__S]]: ...

_Region__S = typing.TypeVar('_Region__S', bound=org.hipparchus.geometry.Space)  # <S>
class Region(typing.Generic[_Region__S]):
    """
    public interface Region<S extends :class:`~org.hipparchus.geometry.Space`>
    
        This interface represents a region of a space as a partition.
    
        Region are subsets of a space, they can be infinite (whole space, half space, infinite stripe ...) or finite (polygons
        in 2D, polyhedrons in 3D ...). Their main characteristic is to separate points that are considered to be *inside* the
        region from points considered to be *outside* of it. In between, there may be points on the *boundary* of the region.
    
        This implementation is limited to regions for which the boundary is composed of several
        :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`, including regions with no boundary at all: the whole space
        and the empty region. They are not necessarily finite and not necessarily path-connected. They can contain holes.
    
        Regions can be combined using the traditional sets operations : union, intersection, difference and symetric difference
        (exclusive or) for the binary operations, complement for the unary operation.
    
        Note that this interface is *not* intended to be implemented by Hipparchus users, it is only intended to be implemented
        within the library itself. New methods may be added even for minor versions, which breaks compatibility for external
        implementations.
    """
    def buildNew(self, bSPTree: BSPTree[_Region__S]) -> 'Region'[_Region__S]: ...
    def checkPoint(self, point: org.hipparchus.geometry.Point[_Region__S]) -> 'Region.Location': ...
    def contains(self, region: 'Region'[_Region__S]) -> bool: ...
    def copySelf(self) -> 'Region'[_Region__S]: ...
    def getBarycenter(self) -> org.hipparchus.geometry.Point[_Region__S]: ...
    def getBoundarySize(self) -> float:
        """
            Get the size of the boundary.
        
            Returns:
                the size of the boundary (this is 0 in 1D, a length in 2D, an area in 3D ...)
        
        
        """
        ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def getTree(self, boolean: bool) -> BSPTree[_Region__S]: ...
    def intersection(self, subHyperplane: 'SubHyperplane'[_Region__S]) -> 'SubHyperplane'[_Region__S]: ...
    @typing.overload
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Returns:
                true if the instance is empty
        
        boolean isEmpty(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`> node)
        
            Check if the sub-tree starting at a given node is empty.
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node is empty
        
        
        """
        ...
    @typing.overload
    def isEmpty(self, bSPTree: BSPTree[_Region__S]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool:
        """
            Check if the instance covers the full space.
        
            Returns:
                true if the instance covers the full space
        
        boolean isFull(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`> node)
        
            Check if the sub-tree starting at a given node covers the full space.
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node covers the full space
        
        
        """
        ...
    @typing.overload
    def isFull(self, bSPTree: BSPTree[_Region__S]) -> bool: ...
    def projectToBoundary(self, point: org.hipparchus.geometry.Point[_Region__S]) -> BoundaryProjection[_Region__S]: ...
    class Location(java.lang.Enum['Region.Location']):
        INSIDE: typing.ClassVar['Region.Location'] = ...
        OUTSIDE: typing.ClassVar['Region.Location'] = ...
        BOUNDARY: typing.ClassVar['Region.Location'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Region.Location': ...
        @staticmethod
        def values() -> typing.List['Region.Location']: ...

_RegionFactory__S = typing.TypeVar('_RegionFactory__S', bound=org.hipparchus.geometry.Space)  # <S>
class RegionFactory(typing.Generic[_RegionFactory__S]):
    """
    public class RegionFactory<S extends :class:`~org.hipparchus.geometry.Space`> extends Object
    
        This class is a factory for :class:`~org.hipparchus.geometry.partitioning.Region`.
    """
    def __init__(self): ...
    def buildConvex(self, hyperplaneArray: typing.List[Hyperplane[_RegionFactory__S]]) -> Region[_RegionFactory__S]: ...
    def difference(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def getComplement(self, region: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def intersection(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def union(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def xor(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...

class Side(java.lang.Enum['Side']):
    """
    public enum Side extends Enum<:class:`~org.hipparchus.geometry.partitioning.Side`>
    
        Enumerate representing the location of an element with respect to an
        :class:`~org.hipparchus.geometry.partitioning.Hyperplane` of a space.
    """
    PLUS: typing.ClassVar['Side'] = ...
    MINUS: typing.ClassVar['Side'] = ...
    BOTH: typing.ClassVar['Side'] = ...
    HYPER: typing.ClassVar['Side'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Side':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['Side']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (Side c : Side.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_SubHyperplane__SplitSubHyperplane__U = typing.TypeVar('_SubHyperplane__SplitSubHyperplane__U', bound=org.hipparchus.geometry.Space)  # <U>
_SubHyperplane__S = typing.TypeVar('_SubHyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
class SubHyperplane(typing.Generic[_SubHyperplane__S]):
    """
    public interface SubHyperplane<S extends :class:`~org.hipparchus.geometry.Space`>
    
        This interface represents the remaining parts of an hyperplane after other parts have been chopped off.
    
        sub-hyperplanes are obtained when parts of an :class:`~org.hipparchus.geometry.partitioning.Hyperplane` are chopped off
        by other hyperplanes that intersect it. The remaining part is a convex region. Such objects appear in
        :class:`~org.hipparchus.geometry.partitioning.BSPTree` as the intersection of a cut hyperplane with the convex region
        which it splits, the chopping hyperplanes are the cut hyperplanes closer to the tree root.
    
        Note that this interface is *not* intended to be implemented by Hipparchus users, it is only intended to be implemented
        within the library itself. New methods may be added even for minor versions, which breaks compatibility for external
        implementations.
    """
    def copySelf(self) -> 'SubHyperplane'[_SubHyperplane__S]: ...
    def getHyperplane(self) -> Hyperplane[_SubHyperplane__S]: ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Returns:
                true if the instance is empty
        
        
        """
        ...
    def reunite(self, subHyperplane: 'SubHyperplane'[_SubHyperplane__S]) -> 'SubHyperplane'[_SubHyperplane__S]: ...
    def split(self, hyperplane: Hyperplane[_SubHyperplane__S]) -> 'SubHyperplane.SplitSubHyperplane'[_SubHyperplane__S]: ...
    class SplitSubHyperplane(typing.Generic[_SubHyperplane__SplitSubHyperplane__U]):
        def __init__(self, subHyperplane: 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U], subHyperplane2: 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U]): ...
        def getMinus(self) -> 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U]: ...
        def getPlus(self) -> 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U]: ...
        def getSide(self) -> Side: ...

_Transform__S = typing.TypeVar('_Transform__S', bound=org.hipparchus.geometry.Space)  # <S>
_Transform__T = typing.TypeVar('_Transform__T', bound=org.hipparchus.geometry.Space)  # <T>
class Transform(typing.Generic[_Transform__S, _Transform__T]):
    """
    public interface Transform<S extends :class:`~org.hipparchus.geometry.Space`,T extends :class:`~org.hipparchus.geometry.Space`>
    
        This interface represents an inversible affine transform in a space.
    
        Inversible affine transform include for example scalings, translations, rotations.
    
        Transforms are dimension-specific. The consistency rules between the three :code:`apply` methods are the following ones
        for a transformed defined for dimension D:
    
          - the transform can be applied to a point in the D-dimension space using its
            :meth:`~org.hipparchus.geometry.partitioning.Transform.apply` method
          - the transform can be applied to a (D-1)-dimension hyperplane in the D-dimension space using its
            :meth:`~org.hipparchus.geometry.partitioning.Transform.apply` method
          - the transform can be applied to a (D-2)-dimension sub-hyperplane in a (D-1)-dimension hyperplane using its
            :meth:`~org.hipparchus.geometry.partitioning.Transform.apply` method
    """
    @typing.overload
    def apply(self, point: org.hipparchus.geometry.Point[_Transform__S]) -> org.hipparchus.geometry.Point[_Transform__S]: ...
    @typing.overload
    def apply(self, hyperplane: Hyperplane[_Transform__S]) -> Hyperplane[_Transform__S]: ...
    @typing.overload
    def apply(self, subHyperplane: SubHyperplane[_Transform__T], hyperplane: Hyperplane[_Transform__S], hyperplane2: Hyperplane[_Transform__S]) -> SubHyperplane[_Transform__T]: ...

_AbstractRegion__S = typing.TypeVar('_AbstractRegion__S', bound=org.hipparchus.geometry.Space)  # <S>
_AbstractRegion__T = typing.TypeVar('_AbstractRegion__T', bound=org.hipparchus.geometry.Space)  # <T>
class AbstractRegion(Region[_AbstractRegion__S], typing.Generic[_AbstractRegion__S, _AbstractRegion__T]):
    """
    public abstract class AbstractRegion<S extends :class:`~org.hipparchus.geometry.Space`,T extends :class:`~org.hipparchus.geometry.Space`> extends Object implements :class:`~org.hipparchus.geometry.partitioning.Region`<S>
    
        Abstract class for all regions, independently of geometry type or dimension.
    """
    def __init__(self, hyperplaneArray: typing.List[Hyperplane[_AbstractRegion__S]], double: float): ...
    def applyTransform(self, transform: Transform[_AbstractRegion__S, _AbstractRegion__T]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__T]: ...
    def buildNew(self, bSPTree: BSPTree[_AbstractRegion__S]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__T]: ...
    @typing.overload
    def checkPoint(self, point: org.hipparchus.geometry.Point[_AbstractRegion__S]) -> Region.Location: ...
    @typing.overload
    def checkPoint(self, vector: org.hipparchus.geometry.Vector[_AbstractRegion__S]) -> Region.Location: ...
    def contains(self, region: Region[_AbstractRegion__S]) -> bool: ...
    def copySelf(self) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__T]: ...
    def getBarycenter(self) -> org.hipparchus.geometry.Point[_AbstractRegion__S]: ...
    def getBoundarySize(self) -> float:
        """
            Get the size of the boundary.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.getBoundarySize`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                the size of the boundary (this is 0 in 1D, a length in 2D, an area in 3D ...)
        
        
        """
        ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.getSize`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def getTolerance(self) -> float:
        """
            Get the tolerance below which points are considered to belong to hyperplanes.
        
            Returns:
                tolerance below which points are considered to belong to hyperplanes
        
        
        """
        ...
    def getTree(self, boolean: bool) -> BSPTree[_AbstractRegion__S]: ...
    def intersection(self, subHyperplane: SubHyperplane[_AbstractRegion__S]) -> SubHyperplane[_AbstractRegion__S]: ...
    @typing.overload
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isEmpty`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                true if the instance is empty
        
        public boolean isEmpty(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node)
        
            Check if the sub-tree starting at a given node is empty.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isEmpty`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node is empty
        
        
        """
        ...
    @typing.overload
    def isEmpty(self, bSPTree: BSPTree[_AbstractRegion__S]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool:
        """
            Check if the instance covers the full space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isFull`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                true if the instance covers the full space
        
        public boolean isFull(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node)
        
            Check if the sub-tree starting at a given node covers the full space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isFull`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node covers the full space
        
        
        """
        ...
    @typing.overload
    def isFull(self, bSPTree: BSPTree[_AbstractRegion__S]) -> bool: ...
    def projectToBoundary(self, point: org.hipparchus.geometry.Point[_AbstractRegion__S]) -> BoundaryProjection[_AbstractRegion__S]: ...

_AbstractSubHyperplane__S = typing.TypeVar('_AbstractSubHyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
_AbstractSubHyperplane__T = typing.TypeVar('_AbstractSubHyperplane__T', bound=org.hipparchus.geometry.Space)  # <T>
class AbstractSubHyperplane(SubHyperplane[_AbstractSubHyperplane__S], typing.Generic[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]):
    """
    public abstract class AbstractSubHyperplane<S extends :class:`~org.hipparchus.geometry.Space`,T extends :class:`~org.hipparchus.geometry.Space`> extends Object implements :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S>
    
        This class implements the dimension-independent parts of :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`.
    
        sub-hyperplanes are obtained when parts of an :class:`~org.hipparchus.geometry.partitioning.Hyperplane` are chopped off
        by other hyperplanes that intersect it. The remaining part is a convex region. Such objects appear in
        :class:`~org.hipparchus.geometry.partitioning.BSPTree` as the intersection of a cut hyperplane with the convex region
        which it splits, the chopping hyperplanes are the cut hyperplanes closer to the tree root.
    """
    def applyTransform(self, transform: Transform[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]) -> 'AbstractSubHyperplane'[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]: ...
    def copySelf(self) -> 'AbstractSubHyperplane'[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]: ...
    def getHyperplane(self) -> Hyperplane[_AbstractSubHyperplane__S]: ...
    def getRemainingRegion(self) -> Region[_AbstractSubHyperplane__T]: ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.getSize`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.isEmpty`Â in
                interfaceÂ :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Returns:
                true if the instance is empty
        
        
        """
        ...
    def reunite(self, subHyperplane: SubHyperplane[_AbstractSubHyperplane__S]) -> 'AbstractSubHyperplane'[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]: ...
    def split(self, hyperplane: Hyperplane[_AbstractSubHyperplane__S]) -> SubHyperplane.SplitSubHyperplane[_AbstractSubHyperplane__S]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.partitioning")``.

    AbstractRegion: typing.Type[AbstractRegion]
    AbstractSubHyperplane: typing.Type[AbstractSubHyperplane]
    BSPTree: typing.Type[BSPTree]
    BSPTreeVisitor: typing.Type[BSPTreeVisitor]
    BoundaryAttribute: typing.Type[BoundaryAttribute]
    BoundaryProjection: typing.Type[BoundaryProjection]
    Embedding: typing.Type[Embedding]
    Hyperplane: typing.Type[Hyperplane]
    NodesSet: typing.Type[NodesSet]
    Region: typing.Type[Region]
    RegionFactory: typing.Type[RegionFactory]
    Side: typing.Type[Side]
    SubHyperplane: typing.Type[SubHyperplane]
    Transform: typing.Type[Transform]
