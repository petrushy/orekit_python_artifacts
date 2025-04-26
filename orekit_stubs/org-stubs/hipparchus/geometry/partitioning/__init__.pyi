
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org.hipparchus.geometry
import typing



_BSPTree__InteriorPoint__S = typing.TypeVar('_BSPTree__InteriorPoint__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__InteriorPoint__P = typing.TypeVar('_BSPTree__InteriorPoint__P', bound=org.hipparchus.geometry.Point)  # <P>
_BSPTree__LeafMerger__S = typing.TypeVar('_BSPTree__LeafMerger__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__LeafMerger__P = typing.TypeVar('_BSPTree__LeafMerger__P', bound=org.hipparchus.geometry.Point)  # <P>
_BSPTree__LeafMerger__H = typing.TypeVar('_BSPTree__LeafMerger__H', bound='Hyperplane')  # <H>
_BSPTree__LeafMerger__I = typing.TypeVar('_BSPTree__LeafMerger__I', bound='SubHyperplane')  # <I>
_BSPTree__VanishingCutHandler__S = typing.TypeVar('_BSPTree__VanishingCutHandler__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__VanishingCutHandler__P = typing.TypeVar('_BSPTree__VanishingCutHandler__P', bound=org.hipparchus.geometry.Point)  # <P>
_BSPTree__VanishingCutHandler__H = typing.TypeVar('_BSPTree__VanishingCutHandler__H', bound='Hyperplane')  # <H>
_BSPTree__VanishingCutHandler__I = typing.TypeVar('_BSPTree__VanishingCutHandler__I', bound='SubHyperplane')  # <I>
_BSPTree__S = typing.TypeVar('_BSPTree__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__P = typing.TypeVar('_BSPTree__P', bound=org.hipparchus.geometry.Point)  # <P>
_BSPTree__H = typing.TypeVar('_BSPTree__H', bound='Hyperplane')  # <H>
_BSPTree__I = typing.TypeVar('_BSPTree__I', bound='SubHyperplane')  # <I>
class BSPTree(typing.Generic[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]):
    """
    public classBSPTree<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
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
    def __init__(self, i: _BSPTree__I, bSPTree: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], bSPTree2: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], object: typing.Any): ...
    def copySelf(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def getAttribute(self) -> typing.Any:
        """
            Get the attribute associated with the instance.
        
            Returns:
                attribute associated with the node or null if no attribute has been explicitly set using the
                :meth:`~org.hipparchus.geometry.partitioning.BSPTree.setAttribute` method
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.partitioning.BSPTree.setAttribute`
        
        
        
        """
        ...
    def getCell(self, p: _BSPTree__P, double: float) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def getCut(self) -> _BSPTree__I:
        """
            Get the cut sub-hyperplane.
        
            Returns:
                cut sub-hyperplane, null if this is a leaf tree
        
        
        """
        ...
    def getInteriorPoint(self, p: _BSPTree__P) -> 'BSPTree.InteriorPoint'[_BSPTree__S, _BSPTree__P]: ...
    def getMinus(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def getParent(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def getPlus(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def insertCut(self, h: _BSPTree__H) -> bool:
        """
            Insert a cut sub-hyperplane in a node.
        
            The sub-tree starting at this node will be completely overwritten. The new cut sub-hyperplane will be built from the
            intersection of the provided hyperplane with the cell. If the hyperplane does intersect the cell, the cell will have two
            children cells with :code:`null` attributes on each side of the inserted cut sub-hyperplane. If the hyperplane does not
            intersect the cell then *no* cut hyperplane will be inserted and the cell will be changed to a leaf cell. The attribute
            of the node is never changed.
        
            This method is mainly useful when called on leaf nodes (i.e. nodes for which
            :meth:`~org.hipparchus.geometry.partitioning.BSPTree.getCut` returns :code:`null`), in this case it provides a way to
            build a tree top-down (whereas the :meth:`~org.hipparchus.geometry.partitioning.BSPTree.%3Cinit%3E` is devoted to build
            trees bottom-up).
        
            Parameters:
                hyperplane (:class:`~org.hipparchus.geometry.partitioning.BSPTree`): hyperplane to insert, it will be chopped in order to fit in the cell defined by the parent nodes of the instance
        
            Returns:
                true if a cut sub-hyperplane has been inserted (i.e. if the cell now has two leaf child nodes)
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.partitioning.BSPTree.%3Cinit%3E`
        
        
        
        """
        ...
    def insertInTree(self, bSPTree: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], boolean: bool, vanishingCutHandler: typing.Union['BSPTree.VanishingCutHandler'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], typing.Callable[['BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane']], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane']]]) -> None: ...
    def merge(self, bSPTree: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], leafMerger: typing.Union['BSPTree.LeafMerger'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], typing.Callable[['BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane'], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane'], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane'], bool, bool], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane']]]) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def pruneAroundConvexCell(self, object: typing.Any, object2: typing.Any, object3: typing.Any) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def setAttribute(self, object: typing.Any) -> None:
        """
            Associate an attribute with the instance.
        
            Parameters:
                attribute (:class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): attribute to associate with the node
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.partitioning.BSPTree.getAttribute`
        
        
        
        """
        ...
    def split(self, i: _BSPTree__I) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]: ...
    def visit(self, bSPTreeVisitor: 'BSPTreeVisitor'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]) -> None: ...
    class InteriorPoint(typing.Generic[_BSPTree__InteriorPoint__S, _BSPTree__InteriorPoint__P]):
        def getDistance(self) -> float: ...
        def getPoint(self) -> _BSPTree__InteriorPoint__P: ...
    class LeafMerger(typing.Generic[_BSPTree__LeafMerger__S, _BSPTree__LeafMerger__P, _BSPTree__LeafMerger__H, _BSPTree__LeafMerger__I]):
        def merge(self, bSPTree: 'BSPTree'[_BSPTree__LeafMerger__S, _BSPTree__LeafMerger__P, _BSPTree__LeafMerger__H, _BSPTree__LeafMerger__I], bSPTree2: 'BSPTree'[_BSPTree__LeafMerger__S, _BSPTree__LeafMerger__P, _BSPTree__LeafMerger__H, _BSPTree__LeafMerger__I], bSPTree3: 'BSPTree'[_BSPTree__LeafMerger__S, _BSPTree__LeafMerger__P, _BSPTree__LeafMerger__H, _BSPTree__LeafMerger__I], boolean: bool, boolean2: bool) -> 'BSPTree'[_BSPTree__LeafMerger__S, _BSPTree__LeafMerger__P, _BSPTree__LeafMerger__H, _BSPTree__LeafMerger__I]: ...
    class VanishingCutHandler(typing.Generic[_BSPTree__VanishingCutHandler__S, _BSPTree__VanishingCutHandler__P, _BSPTree__VanishingCutHandler__H, _BSPTree__VanishingCutHandler__I]):
        def fixNode(self, bSPTree: 'BSPTree'[_BSPTree__VanishingCutHandler__S, _BSPTree__VanishingCutHandler__P, _BSPTree__VanishingCutHandler__H, _BSPTree__VanishingCutHandler__I]) -> 'BSPTree'[_BSPTree__VanishingCutHandler__S, _BSPTree__VanishingCutHandler__P, _BSPTree__VanishingCutHandler__H, _BSPTree__VanishingCutHandler__I]: ...

_BSPTreeVisitor__S = typing.TypeVar('_BSPTreeVisitor__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTreeVisitor__P = typing.TypeVar('_BSPTreeVisitor__P', bound=org.hipparchus.geometry.Point)  # <P>
_BSPTreeVisitor__H = typing.TypeVar('_BSPTreeVisitor__H', bound='Hyperplane')  # <H>
_BSPTreeVisitor__I = typing.TypeVar('_BSPTreeVisitor__I', bound='SubHyperplane')  # <I>
class BSPTreeVisitor(typing.Generic[_BSPTreeVisitor__S, _BSPTreeVisitor__P, _BSPTreeVisitor__H, _BSPTreeVisitor__I]):
    """
    public interfaceBSPTreeVisitor<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>>
    
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
    
              - :class:`~org.hipparchus.geometry.partitioning.BSPTree`
              - :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
    """
    def visitInternalNode(self, bSPTree: BSPTree[_BSPTreeVisitor__S, _BSPTreeVisitor__P, _BSPTreeVisitor__H, _BSPTreeVisitor__I]) -> None: ...
    def visitLeafNode(self, bSPTree: BSPTree[_BSPTreeVisitor__S, _BSPTreeVisitor__P, _BSPTreeVisitor__H, _BSPTreeVisitor__I]) -> None: ...
    def visitOrder(self, bSPTree: BSPTree[_BSPTreeVisitor__S, _BSPTreeVisitor__P, _BSPTreeVisitor__H, _BSPTreeVisitor__I]) -> 'BSPTreeVisitor.Order': ...
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
        def values() -> typing.MutableSequence['BSPTreeVisitor.Order']: ...

_BoundaryAttribute__S = typing.TypeVar('_BoundaryAttribute__S', bound=org.hipparchus.geometry.Space)  # <S>
_BoundaryAttribute__P = typing.TypeVar('_BoundaryAttribute__P', bound=org.hipparchus.geometry.Point)  # <P>
_BoundaryAttribute__H = typing.TypeVar('_BoundaryAttribute__H', bound='Hyperplane')  # <H>
_BoundaryAttribute__I = typing.TypeVar('_BoundaryAttribute__I', bound='SubHyperplane')  # <I>
class BoundaryAttribute(typing.Generic[_BoundaryAttribute__S, _BoundaryAttribute__P, _BoundaryAttribute__H, _BoundaryAttribute__I]):
    """
    public classBoundaryAttribute<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class holding boundary attributes.
    
        This class is used for the attributes associated with the nodes of region boundary shell trees returned by the
        :meth:`~org.hipparchus.geometry.partitioning.Region.getTree` when the boolean :code:`includeBoundaryAttributes`
        parameter is set to :code:`true`. It contains the parts of the node cut sub-hyperplane that belong to the boundary.
    
        This class is a simple placeholder, it does not provide any processing methods.
    
        Also see:
    
              - :meth:`~org.hipparchus.geometry.partitioning.Region.getTree`
    """
    def getPlusInside(self) -> _BoundaryAttribute__I:
        """
            Get the part of the node cut sub-hyperplane that belongs to the boundary and has the inside of the region on the plus
            side of its underlying hyperplane.
        
            Returns:
                part of the node cut sub-hyperplane that belongs to the boundary and has the inside of the region on the plus side of
                its underlying hyperplane
        
        
        """
        ...
    def getPlusOutside(self) -> _BoundaryAttribute__I:
        """
            Get the part of the node cut sub-hyperplane that belongs to the boundary and has the outside of the region on the plus
            side of its underlying hyperplane.
        
            Returns:
                part of the node cut sub-hyperplane that belongs to the boundary and has the outside of the region on the plus side of
                its underlying hyperplane
        
        
        """
        ...
    def getSplitters(self) -> 'NodesSet'[_BoundaryAttribute__S, _BoundaryAttribute__P, _BoundaryAttribute__H, _BoundaryAttribute__I]: ...

_BoundaryProjection__S = typing.TypeVar('_BoundaryProjection__S', bound=org.hipparchus.geometry.Space)  # <S>
_BoundaryProjection__P = typing.TypeVar('_BoundaryProjection__P', bound=org.hipparchus.geometry.Point)  # <P>
class BoundaryProjection(typing.Generic[_BoundaryProjection__S, _BoundaryProjection__P]):
    """
    public classBoundaryProjection<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class holding the result of point projection on region boundary.
    
        This class is a simple placeholder, it does not provide any processing methods.
    
        Instances of this class are guaranteed to be immutable
    
        Also see:
    
              - :meth:`~org.hipparchus.geometry.partitioning.AbstractRegion.projectToBoundary`
    """
    def __init__(self, p: _BoundaryProjection__P, p2: _BoundaryProjection__P, double: float): ...
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
    def getOriginal(self) -> _BoundaryProjection__P:
        """
            Get the original point.
        
            Returns:
                original point
        
        
        """
        ...
    def getProjected(self) -> _BoundaryProjection__P:
        """
            Projected point.
        
            Returns:
                projected point, or null if there are no boundary
        
        
        """
        ...

_Embedding__S = typing.TypeVar('_Embedding__S', bound=org.hipparchus.geometry.Space)  # <S>
_Embedding__P = typing.TypeVar('_Embedding__P', bound=org.hipparchus.geometry.Point)  # <P>
_Embedding__T = typing.TypeVar('_Embedding__T', bound=org.hipparchus.geometry.Space)  # <T>
_Embedding__Q = typing.TypeVar('_Embedding__Q', bound=org.hipparchus.geometry.Point)  # <Q>
class Embedding(typing.Generic[_Embedding__S, _Embedding__P, _Embedding__T, _Embedding__Q]):
    """
    public interfaceEmbedding<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,T extends :class:`~org.hipparchus.geometry.Space`,Q extends :class:`~org.hipparchus.geometry.Point`<T,Q>>
    
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
    
              - :class:`~org.hipparchus.geometry.partitioning.Hyperplane`
    """
    def toSpace(self, q: _Embedding__Q) -> _Embedding__P:
        """
            Transform a sub-space point into a space point.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.Embedding`): (n-1)-dimension point of the sub-space
        
            Returns:
                n-dimension point of the space corresponding to the specified sub-space point
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSubSpace`
        
        
        
        """
        ...
    def toSubSpace(self, p: _Embedding__P) -> _Embedding__Q:
        """
            Transform a space point into a sub-space point.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.Embedding`): n-dimension point of the space
        
            Returns:
                (n-1)-dimension point of the sub-space corresponding to the specified space point
        
            Also see:
        
                  - :meth:`~org.hipparchus.geometry.partitioning.Embedding.toSpace`
        
        
        
        """
        ...

_Hyperplane__S = typing.TypeVar('_Hyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
_Hyperplane__P = typing.TypeVar('_Hyperplane__P', bound=org.hipparchus.geometry.Point)  # <P>
_Hyperplane__H = typing.TypeVar('_Hyperplane__H', bound='Hyperplane')  # <H>
_Hyperplane__I = typing.TypeVar('_Hyperplane__I', bound='SubHyperplane')  # <I>
class Hyperplane(typing.Generic[_Hyperplane__S, _Hyperplane__P, _Hyperplane__H, _Hyperplane__I]):
    """
    public interfaceHyperplane<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends Hyperplane<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>>
    
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
    def arbitraryPoint(self) -> _Hyperplane__P:
        """
            Get an arbitrary point in the hyperplane.
        
            Returns:
                arbirary point in the hyperplane
        
            Since:
                4.0
        
        
        """
        ...
    def copySelf(self) -> _Hyperplane__H:
        """
            Copy the instance.
        
            The instance created is completely independent of the original one. A deep copy is used, none of the underlying objects
            are shared (except for immutable objects).
        
            Returns:
                a new hyperplane, copy of the instance
        
        
        """
        ...
    def emptyHyperplane(self) -> _Hyperplane__I:
        """
            Build a sub-hyperplane covering nothing.
        
            Returns:
                a sub-hyperplane covering nothing
        
            Since:
                1.4
        
        
        """
        ...
    def getOffset(self, p: _Hyperplane__P) -> float:
        """
            Get the offset (oriented distance) of a point.
        
            The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of
            the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.Hyperplane`): point to check
        
            Returns:
                offset of the point
        
        
        """
        ...
    def getTolerance(self) -> float:
        """
            Get the tolerance below which points are considered to belong to the hyperplane.
        
            Returns:
                tolerance below which points are considered to belong to the hyperplane
        
        
        """
        ...
    def moveToOffset(self, p: _Hyperplane__P, double: float) -> _Hyperplane__P:
        """
            Move point up to specified offset.
        
            Motion is *orthogonal* to the hyperplane
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.Hyperplane`): point to move
                offset (double): desired offset
        
            Returns:
                moved point at desired offset
        
            Since:
                4.0
        
        
        """
        ...
    def project(self, p: _Hyperplane__P) -> _Hyperplane__P:
        """
            Project a point to the hyperplane.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.Hyperplane`): point to project
        
            Returns:
                projected point
        
        
        """
        ...
    def sameOrientationAs(self, h: _Hyperplane__H) -> bool:
        """
            Check if the instance has the same orientation as another hyperplane.
        
            This method is expected to be called on parallel hyperplanes. The method should *not* re-check for parallelism, only for
            orientation, typically by testing something like the sign of the dot-products of normals.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.partitioning.Hyperplane`): other hyperplane to check against the instance
        
            Returns:
                true if the instance and the other hyperplane have the same orientation
        
        
        """
        ...
    def wholeHyperplane(self) -> _Hyperplane__I:
        """
            Build a sub-hyperplane covering the whole hyperplane.
        
            Returns:
                a sub-hyperplane covering the whole hyperplane
        
        
        """
        ...
    def wholeSpace(self) -> 'Region'[_Hyperplane__S, _Hyperplane__P, _Hyperplane__H, _Hyperplane__I]: ...

_NodesSet__S = typing.TypeVar('_NodesSet__S', bound=org.hipparchus.geometry.Space)  # <S>
_NodesSet__P = typing.TypeVar('_NodesSet__P', bound=org.hipparchus.geometry.Point)  # <P>
_NodesSet__H = typing.TypeVar('_NodesSet__H', bound=Hyperplane)  # <H>
_NodesSet__I = typing.TypeVar('_NodesSet__I', bound='SubHyperplane')  # <I>
class NodesSet(java.lang.Iterable[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Generic[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]):
    """
    public classNodesSet<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable`<:class:`~org.hipparchus.geometry.partitioning.BSPTree`<S,P,H,I>>
    
        Set of :class:`~org.hipparchus.geometry.partitioning.BSPTree` nodes.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.partitioning.BoundaryAttribute`
    """
    def __init__(self): ...
    def add(self, bSPTree: BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]) -> None: ...
    def addAll(self, iterable: typing.Union[java.lang.Iterable[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Sequence[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Set[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None: ...
    def iterator(self) -> java.util.Iterator[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]]: ...

_Region__S = typing.TypeVar('_Region__S', bound=org.hipparchus.geometry.Space)  # <S>
_Region__P = typing.TypeVar('_Region__P', bound=org.hipparchus.geometry.Point)  # <P>
_Region__H = typing.TypeVar('_Region__H', bound=Hyperplane)  # <H>
_Region__I = typing.TypeVar('_Region__I', bound='SubHyperplane')  # <I>
class Region(typing.Generic[_Region__S, _Region__P, _Region__H, _Region__I]):
    """
    public interfaceRegion<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>>
    
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
    def buildNew(self, bSPTree: BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]) -> 'Region'[_Region__S, _Region__P, _Region__H, _Region__I]: ...
    def checkPoint(self, p: _Region__P) -> 'Region.Location':
        """
            Check a point with respect to the region.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.Region`): point to check
        
            Returns:
                a code representing the point status: either :meth:`~org.hipparchus.geometry.partitioning.Region.Location.INSIDE`,
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.OUTSIDE` or
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.BOUNDARY`
        
        
        """
        ...
    def contains(self, region: 'Region'[_Region__S, _Region__P, _Region__H, _Region__I]) -> bool: ...
    def copySelf(self) -> 'Region'[_Region__S, _Region__P, _Region__H, _Region__I]: ...
    def getBarycenter(self) -> _Region__P:
        """
            Get the barycenter of the instance.
        
            Returns:
                an object representing the barycenter
        
        
        """
        ...
    def getBoundarySize(self) -> float:
        """
            Get the size of the boundary.
        
            Returns:
                the size of the boundary (this is 0 in 1D, a length in 2D, an area in 3D ...)
        
        
        """
        ...
    def getInteriorPoint(self) -> _Region__P:
        """
            Get an interior point.
        
            Returns:
                an arbitrary interior point, or null if region is empty
        
            Since:
                4.0
        
        
        """
        ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def getTree(self, boolean: bool) -> BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]: ...
    def intersection(self, i: _Region__I) -> _Region__I:
        """
            Get the parts of a sub-hyperplane that are contained in the region.
        
            The parts of the sub-hyperplane that belong to the boundary are *not* included in the resulting parts.
        
            Parameters:
                sub (:class:`~org.hipparchus.geometry.partitioning.Region`): sub-hyperplane traversing the region
        
            Returns:
                filtered sub-hyperplane
        
        
        """
        ...
    @typing.overload
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Returns:
                true if the instance is empty
        
        boolean isEmpty(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`> node)
        
            Check if the sub-tree starting at a given node is empty.
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node is empty
        
        
        """
        ...
    @typing.overload
    def isEmpty(self, bSPTree: BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool:
        """
            Check if the instance covers the full space.
        
            Returns:
                true if the instance covers the full space
        
        boolean isFull(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`> node)
        
            Check if the sub-tree starting at a given node covers the full space.
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`,:class:`~org.hipparchus.geometry.partitioning.Region`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node covers the full space
        
        
        """
        ...
    @typing.overload
    def isFull(self, bSPTree: BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]) -> bool: ...
    def projectToBoundary(self, p: _Region__P) -> BoundaryProjection[_Region__S, _Region__P]: ...
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
        def values() -> typing.MutableSequence['Region.Location']: ...

_RegionFactory__S = typing.TypeVar('_RegionFactory__S', bound=org.hipparchus.geometry.Space)  # <S>
_RegionFactory__P = typing.TypeVar('_RegionFactory__P', bound=org.hipparchus.geometry.Point)  # <P>
_RegionFactory__H = typing.TypeVar('_RegionFactory__H', bound=Hyperplane)  # <H>
_RegionFactory__I = typing.TypeVar('_RegionFactory__I', bound='SubHyperplane')  # <I>
class RegionFactory(typing.Generic[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]):
    """
    public classRegionFactory<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This class is a factory for :class:`~org.hipparchus.geometry.partitioning.Region`.
    """
    def __init__(self): ...
    def buildConvex(self, *h: _RegionFactory__H) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]: ...
    def difference(self, region: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]: ...
    def getComplement(self, region: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]: ...
    def intersection(self, region: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]: ...
    def union(self, region: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]: ...
    def xor(self, region: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]: ...

class Side(java.lang.Enum['Side']):
    """
    public enumSide extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.geometry.partitioning.Side`>
    
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
                name (:class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['Side']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_SubHyperplane__SplitSubHyperplane__U = typing.TypeVar('_SubHyperplane__SplitSubHyperplane__U', bound=org.hipparchus.geometry.Space)  # <U>
_SubHyperplane__SplitSubHyperplane__R = typing.TypeVar('_SubHyperplane__SplitSubHyperplane__R', bound=org.hipparchus.geometry.Point)  # <R>
_SubHyperplane__SplitSubHyperplane__F = typing.TypeVar('_SubHyperplane__SplitSubHyperplane__F', bound=Hyperplane)  # <F>
_SubHyperplane__SplitSubHyperplane__J = typing.TypeVar('_SubHyperplane__SplitSubHyperplane__J', bound='SubHyperplane')  # <J>
_SubHyperplane__S = typing.TypeVar('_SubHyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
_SubHyperplane__P = typing.TypeVar('_SubHyperplane__P', bound=org.hipparchus.geometry.Point)  # <P>
_SubHyperplane__H = typing.TypeVar('_SubHyperplane__H', bound=Hyperplane)  # <H>
_SubHyperplane__I = typing.TypeVar('_SubHyperplane__I', bound='SubHyperplane')  # <I>
class SubHyperplane(typing.Generic[_SubHyperplane__S, _SubHyperplane__P, _SubHyperplane__H, _SubHyperplane__I]):
    """
    public interfaceSubHyperplane<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends SubHyperplane<S,P,H,I>>
    
        This interface represents the remaining parts of an hyperplane after other parts have been chopped off.
    
        sub-hyperplanes are obtained when parts of an :class:`~org.hipparchus.geometry.partitioning.Hyperplane` are chopped off
        by other hyperplanes that intersect it. The remaining part is a convex region. Such objects appear in
        :class:`~org.hipparchus.geometry.partitioning.BSPTree` as the intersection of a cut hyperplane with the convex region
        which it splits, the chopping hyperplanes are the cut hyperplanes closer to the tree root.
    
        Note that this interface is *not* intended to be implemented by Hipparchus users, it is only intended to be implemented
        within the library itself. New methods may be added even for minor versions, which breaks compatibility for external
        implementations.
    """
    def copySelf(self) -> _SubHyperplane__I:
        """
            Copy the instance.
        
            The instance created is completely independent from the original one. A deep copy is used, none of the underlying
            objects are shared (except for the nodes attributes and immutable objects).
        
            Returns:
                a new sub-hyperplane, copy of the instance
        
        
        """
        ...
    def getHyperplane(self) -> _SubHyperplane__H:
        """
            Get the underlying hyperplane.
        
            Returns:
                underlying hyperplane
        
        
        """
        ...
    def getInteriorPoint(self) -> _SubHyperplane__P:
        """
            Get an interior point.
        
            Returns:
                an arbitrary interior point, or null if sub-hyperplane is empty
        
            Since:
                4.0
        
        
        """
        ...
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
    def reunite(self, i: _SubHyperplane__I) -> _SubHyperplane__I:
        """
            Compute the union of the instance and another sub-hyperplane.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.partitioning.SubHyperplane`): other sub-hyperplane to union (*must* be in the same hyperplane as the instance)
        
            Returns:
                a new sub-hyperplane, union of the instance and other
        
        
        """
        ...
    def split(self, h: _SubHyperplane__H) -> 'SubHyperplane.SplitSubHyperplane'[_SubHyperplane__S, _SubHyperplane__P, _SubHyperplane__H, _SubHyperplane__I]: ...
    class SplitSubHyperplane(typing.Generic[_SubHyperplane__SplitSubHyperplane__U, _SubHyperplane__SplitSubHyperplane__R, _SubHyperplane__SplitSubHyperplane__F, _SubHyperplane__SplitSubHyperplane__J]):
        def __init__(self, j: _SubHyperplane__SplitSubHyperplane__J, j2: _SubHyperplane__SplitSubHyperplane__J): ...
        def getMinus(self) -> _SubHyperplane__SplitSubHyperplane__J: ...
        def getPlus(self) -> _SubHyperplane__SplitSubHyperplane__J: ...
        def getSide(self) -> Side: ...

_Transform__S = typing.TypeVar('_Transform__S', bound=org.hipparchus.geometry.Space)  # <S>
_Transform__P = typing.TypeVar('_Transform__P', bound=org.hipparchus.geometry.Point)  # <P>
_Transform__H = typing.TypeVar('_Transform__H', bound=Hyperplane)  # <H>
_Transform__I = typing.TypeVar('_Transform__I', bound=SubHyperplane)  # <I>
_Transform__T = typing.TypeVar('_Transform__T', bound=org.hipparchus.geometry.Space)  # <T>
_Transform__Q = typing.TypeVar('_Transform__Q', bound=org.hipparchus.geometry.Point)  # <Q>
_Transform__F = typing.TypeVar('_Transform__F', bound=Hyperplane)  # <F>
_Transform__J = typing.TypeVar('_Transform__J', bound=SubHyperplane)  # <J>
class Transform(typing.Generic[_Transform__S, _Transform__P, _Transform__H, _Transform__I, _Transform__T, _Transform__Q, _Transform__F, _Transform__J]):
    """
    public interfaceTransform<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>,T extends :class:`~org.hipparchus.geometry.Space`,Q extends :class:`~org.hipparchus.geometry.Point`<T,Q>,F extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<T,Q,F,J>,J extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<T,Q,F,J>>
    
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
    def apply(self, p: _Transform__P) -> _Transform__P:
        """
            Transform a point of a space.
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.Transform`): point to transform
        
            Returns:
                a new object representing the transformed point
        
            Transform an hyperplane of a space.
        
            Parameters:
                hyperplane (:class:`~org.hipparchus.geometry.partitioning.Transform`): hyperplane to transform
        
            Returns:
                a new object representing the transformed hyperplane
        
            Transform a sub-hyperplane embedded in an hyperplane.
        
            Parameters:
                sub (:class:`~org.hipparchus.geometry.partitioning.Transform`): sub-hyperplane to transform
                original (:class:`~org.hipparchus.geometry.partitioning.Transform`): hyperplane in which the sub-hyperplane is defined (this is the original hyperplane, the transform has *not* been applied
                    to it)
                transformed (:class:`~org.hipparchus.geometry.partitioning.Transform`): hyperplane in which the sub-hyperplane is defined (this is the transformed hyperplane, the transform *has* been applied
                    to it)
        
            Returns:
                a new object representing the transformed sub-hyperplane
        
        
        """
        ...
    @typing.overload
    def apply(self, h: _Transform__H) -> _Transform__H: ...
    @typing.overload
    def apply(self, j: _Transform__J, h: _Transform__H, h2: _Transform__H) -> _Transform__J: ...

_AbstractRegion__S = typing.TypeVar('_AbstractRegion__S', bound=org.hipparchus.geometry.Space)  # <S>
_AbstractRegion__P = typing.TypeVar('_AbstractRegion__P', bound=org.hipparchus.geometry.Point)  # <P>
_AbstractRegion__H = typing.TypeVar('_AbstractRegion__H', bound=Hyperplane)  # <H>
_AbstractRegion__I = typing.TypeVar('_AbstractRegion__I', bound=SubHyperplane)  # <I>
_AbstractRegion__T = typing.TypeVar('_AbstractRegion__T', bound=org.hipparchus.geometry.Space)  # <T>
_AbstractRegion__Q = typing.TypeVar('_AbstractRegion__Q', bound=org.hipparchus.geometry.Point)  # <Q>
_AbstractRegion__F = typing.TypeVar('_AbstractRegion__F', bound=Hyperplane)  # <F>
_AbstractRegion__J = typing.TypeVar('_AbstractRegion__J', bound=SubHyperplane)  # <J>
class AbstractRegion(Region[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I], typing.Generic[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]):
    """
    public abstract classAbstractRegion<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>,T extends :class:`~org.hipparchus.geometry.Space`,Q extends :class:`~org.hipparchus.geometry.Point`<T,Q>,F extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<T,Q,F,J>,J extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<T,Q,F,J>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.partitioning.Region`<S,P,H,I>
    
        Abstract class for all regions, independently of geometry type or dimension.
    """
    def __init__(self, hArray: typing.Union[typing.List[_AbstractRegion__H], jpype.JArray], double: float): ...
    def applyTransform(self, transform: Transform[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]: ...
    def buildNew(self, bSPTree: BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]: ...
    def checkPoint(self, p: _AbstractRegion__P) -> Region.Location:
        """
            Check a point with respect to the region.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.checkPoint` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Parameters:
                point (:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`): point to check
        
            Returns:
                a code representing the point status: either :meth:`~org.hipparchus.geometry.partitioning.Region.Location.INSIDE`,
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.OUTSIDE` or
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.BOUNDARY`
        
        protected :class:`~org.hipparchus.geometry.partitioning.Region.Location` checkPoint(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node, :class:`~org.hipparchus.geometry.partitioning.AbstractRegion` point)
        
            Check a point with respect to the region starting at a given node.
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node): root node of the region
                point (:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`): point to check
        
            Returns:
                a code representing the point status: either :meth:`~org.hipparchus.geometry.partitioning.Region.Location.INSIDE`,
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.OUTSIDE` or
                :meth:`~org.hipparchus.geometry.partitioning.Region.Location.BOUNDARY`
        
        
        """
        ...
    def contains(self, region: Region[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> bool: ...
    def copySelf(self) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]: ...
    def getBarycenter(self) -> _AbstractRegion__P:
        """
            Get the barycenter of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.getBarycenter` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                an object representing the barycenter
        
        
        """
        ...
    def getBoundarySize(self) -> float:
        """
            Get the size of the boundary.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.getBoundarySize` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                the size of the boundary (this is 0 in 1D, a length in 2D, an area in 3D ...)
        
        
        """
        ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.getSize` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
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
    def getTree(self, boolean: bool) -> BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]: ...
    def intersection(self, i: _AbstractRegion__I) -> _AbstractRegion__I:
        """
            Get the parts of a sub-hyperplane that are contained in the region.
        
            The parts of the sub-hyperplane that belong to the boundary are *not* included in the resulting parts.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.intersection` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Parameters:
                sub (:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`): sub-hyperplane traversing the region
        
            Returns:
                filtered sub-hyperplane
        
        
        """
        ...
    @typing.overload
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isEmpty` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                true if the instance is empty
        
        public boolean isEmpty(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node)
        
            Check if the sub-tree starting at a given node is empty.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isEmpty` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node is empty
        
        
        """
        ...
    @typing.overload
    def isEmpty(self, bSPTree: BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool:
        """
            Check if the instance covers the full space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isFull` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Returns:
                true if the instance covers the full space
        
        public boolean isFull(:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node)
        
            Check if the sub-tree starting at a given node covers the full space.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.Region.isFull` in
                interface :class:`~org.hipparchus.geometry.partitioning.Region`
        
            Parameters:
                node (:class:`~org.hipparchus.geometry.partitioning.BSPTree`<:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`,:class:`~org.hipparchus.geometry.partitioning.AbstractRegion`> node): root node of the sub-tree (*must* have :class:`~org.hipparchus.geometry.partitioning.Region` tree semantics, i.e. the
                    leaf nodes must have :code:`Boolean` attributes representing an inside/outside property)
        
            Returns:
                true if the sub-tree starting at the given node covers the full space
        
        
        """
        ...
    @typing.overload
    def isFull(self, bSPTree: BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> bool: ...
    def projectToBoundary(self, p: _AbstractRegion__P) -> BoundaryProjection[_AbstractRegion__S, _AbstractRegion__P]: ...

_AbstractSubHyperplane__S = typing.TypeVar('_AbstractSubHyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
_AbstractSubHyperplane__P = typing.TypeVar('_AbstractSubHyperplane__P', bound=org.hipparchus.geometry.Point)  # <P>
_AbstractSubHyperplane__H = typing.TypeVar('_AbstractSubHyperplane__H', bound=Hyperplane)  # <H>
_AbstractSubHyperplane__I = typing.TypeVar('_AbstractSubHyperplane__I', bound=SubHyperplane)  # <I>
_AbstractSubHyperplane__T = typing.TypeVar('_AbstractSubHyperplane__T', bound=org.hipparchus.geometry.Space)  # <T>
_AbstractSubHyperplane__Q = typing.TypeVar('_AbstractSubHyperplane__Q', bound=org.hipparchus.geometry.Point)  # <Q>
_AbstractSubHyperplane__F = typing.TypeVar('_AbstractSubHyperplane__F', bound=Hyperplane)  # <F>
_AbstractSubHyperplane__J = typing.TypeVar('_AbstractSubHyperplane__J', bound=SubHyperplane)  # <J>
class AbstractSubHyperplane(SubHyperplane[_AbstractSubHyperplane__S, _AbstractSubHyperplane__P, _AbstractSubHyperplane__H, _AbstractSubHyperplane__I], typing.Generic[_AbstractSubHyperplane__S, _AbstractSubHyperplane__P, _AbstractSubHyperplane__H, _AbstractSubHyperplane__I, _AbstractSubHyperplane__T, _AbstractSubHyperplane__Q, _AbstractSubHyperplane__F, _AbstractSubHyperplane__J]):
    """
    public abstract classAbstractSubHyperplane<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>,T extends :class:`~org.hipparchus.geometry.Space`,Q extends :class:`~org.hipparchus.geometry.Point`<T,Q>,F extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<T,Q,F,J>,J extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<T,Q,F,J>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>
    
        This class implements the dimension-independent parts of :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`.
    
        sub-hyperplanes are obtained when parts of an :class:`~org.hipparchus.geometry.partitioning.Hyperplane` are chopped off
        by other hyperplanes that intersect it. The remaining part is a convex region. Such objects appear in
        :class:`~org.hipparchus.geometry.partitioning.BSPTree` as the intersection of a cut hyperplane with the convex region
        which it splits, the chopping hyperplanes are the cut hyperplanes closer to the tree root.
    """
    def applyTransform(self, transform: Transform[_AbstractSubHyperplane__S, _AbstractSubHyperplane__P, _AbstractSubHyperplane__H, _AbstractSubHyperplane__I, _AbstractSubHyperplane__T, _AbstractSubHyperplane__Q, _AbstractSubHyperplane__F, _AbstractSubHyperplane__J]) -> _AbstractSubHyperplane__I: ...
    def copySelf(self) -> _AbstractSubHyperplane__I:
        """
            Copy the instance.
        
            The instance created is completely independent from the original one. A deep copy is used, none of the underlying
            objects are shared (except for the nodes attributes and immutable objects).
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.copySelf` in
                interface :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Returns:
                a new sub-hyperplane, copy of the instance
        
        
        """
        ...
    def getHyperplane(self) -> _AbstractSubHyperplane__H:
        """
            Get the underlying hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.getHyperplane` in
                interface :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Returns:
                underlying hyperplane
        
        
        """
        ...
    def getRemainingRegion(self) -> Region[_AbstractSubHyperplane__T, _AbstractSubHyperplane__Q, _AbstractSubHyperplane__F, _AbstractSubHyperplane__J]: ...
    def getSize(self) -> float:
        """
            Get the size of the instance.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.getSize` in
                interface :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Returns:
                the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Check if the instance is empty.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.isEmpty` in
                interface :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Returns:
                true if the instance is empty
        
        
        """
        ...
    def reunite(self, i: _AbstractSubHyperplane__I) -> _AbstractSubHyperplane__I:
        """
            Compute the union of the instance and another sub-hyperplane.
        
            Specified by:
                :meth:`~org.hipparchus.geometry.partitioning.SubHyperplane.reunite` in
                interface :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.partitioning.AbstractSubHyperplane`): other sub-hyperplane to union (*must* be in the same hyperplane as the instance)
        
            Returns:
                a new sub-hyperplane, union of the instance and other
        
        
        """
        ...
    def split(self, h: _AbstractSubHyperplane__H) -> SubHyperplane.SplitSubHyperplane[_AbstractSubHyperplane__S, _AbstractSubHyperplane__P, _AbstractSubHyperplane__H, _AbstractSubHyperplane__I]: ...

_InteriorPointFinder__S = typing.TypeVar('_InteriorPointFinder__S', bound=org.hipparchus.geometry.Space)  # <S>
_InteriorPointFinder__P = typing.TypeVar('_InteriorPointFinder__P', bound=org.hipparchus.geometry.Point)  # <P>
_InteriorPointFinder__H = typing.TypeVar('_InteriorPointFinder__H', bound=Hyperplane)  # <H>
_InteriorPointFinder__I = typing.TypeVar('_InteriorPointFinder__I', bound=SubHyperplane)  # <I>
class InteriorPointFinder(BSPTreeVisitor[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I], typing.Generic[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]):
    """
    public classInteriorPointFinder<S extends :class:`~org.hipparchus.geometry.Space`,P extends :class:`~org.hipparchus.geometry.Point`<S,P>,H extends :class:`~org.hipparchus.geometry.partitioning.Hyperplane`<S,P,H,I>,I extends :class:`~org.hipparchus.geometry.partitioning.SubHyperplane`<S,P,H,I>> extends :class:`~org.hipparchus.geometry.partitioning.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.geometry.partitioning.BSPTreeVisitor`<S,P,H,I>
    
        Finder for interior points.
    
        Since:
            4.0
    """
    def __init__(self, p: _InteriorPointFinder__P): ...
    def getPoint(self) -> BSPTree.InteriorPoint[_InteriorPointFinder__S, _InteriorPointFinder__P]: ...
    def visitInternalNode(self, bSPTree: BSPTree[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]) -> None: ...
    def visitLeafNode(self, bSPTree: BSPTree[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]) -> None: ...
    def visitOrder(self, bSPTree: BSPTree[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]) -> BSPTreeVisitor.Order: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.partitioning")``.

    AbstractRegion: typing.Type[AbstractRegion]
    AbstractSubHyperplane: typing.Type[AbstractSubHyperplane]
    BSPTree: typing.Type[BSPTree]
    BSPTreeVisitor: typing.Type[BSPTreeVisitor]
    BoundaryAttribute: typing.Type[BoundaryAttribute]
    BoundaryProjection: typing.Type[BoundaryProjection]
    Embedding: typing.Type[Embedding]
    Hyperplane: typing.Type[Hyperplane]
    InteriorPointFinder: typing.Type[InteriorPointFinder]
    NodesSet: typing.Type[NodesSet]
    Region: typing.Type[Region]
    RegionFactory: typing.Type[RegionFactory]
    Side: typing.Type[Side]
    SubHyperplane: typing.Type[SubHyperplane]
    Transform: typing.Type[Transform]
