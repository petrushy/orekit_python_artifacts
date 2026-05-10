
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
    This class represent a Binary Space Partition tree.
    
    BSP trees are an efficient way to represent space partitions and to associate attributes with each cell. Each node in a BSP tree represents a convex region which is partitioned in two convex sub-regions at each side of a cut hyperplane. The root tree contains the complete space.
    
    The main use of such partitions is to use a boolean attribute to define an inside/outside property, hence representing arbitrary polytopes (line segments in 1D, polygons in 2D and polyhedrons in 3D) and to operate on them.
    
    Another example would be to represent Voronoi tesselations, the attribute of each cell holding the defining point of the cell.
    
    The application-defined attributes are shared among copied instances and propagated to split parts. These attributes are not used by the BSP-tree algorithms themselves, so the application can use them for any purpose. Since the tree visiting method holds internal and leaf nodes differently, it is possible to use different classes for internal nodes attributes and leaf nodes attributes. This should be used with care, though, because if the tree is modified in any way after attributes have been set, some internal nodes may become leaf nodes and some leaf nodes may become internal nodes.
    
    One of the main sources for the development of this package was Bruce Naylor, John Amanatides and William Thibault paper `Merging BSP Trees Yields Polyhedral Set Operations <http://www.cs.yorku.ca/~amana/research/bsptSetOp.pdf>` Proc. Siggraph '90, Computer Graphics 24(4), August 1990, pp 115-124, published by the Association for Computing Machinery (ACM).
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, attribute: typing.Any): ...
    @typing.overload
    def __init__(self, cut: _BSPTree__I, plus: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], minus: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], attribute: typing.Any): ...
    def copySelf(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Copy the instance.
        
        The instance created is completely independent of the original one. A deep copy is used, none of the underlying objects are shared (except for the nodes attributes and immutable objects).
        
        Returns:
            a new tree, copy of the instance
        
        
        """
        ...
    def getAttribute(self) -> typing.Any:
        """
        Get the attribute associated with the instance.
        
        Returns:
            attribute associated with the node or null if no attribute has been explicitly set using the
            setAttribute method
        
        Also see:
            setAttribute
        
        
        """
        ...
    def getCell(self, point: _BSPTree__P, tolerance: float) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Get the cell to which a point belongs.
        
        If the returned cell is a leaf node the points belongs to the interior of the node, if the cell is an internal node the points belongs to the node cut sub-hyperplane.
        
        Parameters:
            point (BSPTree): point to check
            tolerance (double): tolerance below which points close to a cut hyperplane are considered to belong to the hyperplane itself
        
        Returns:
            the tree cell to which the point belongs
        
        
        """
        ...
    def getCut(self) -> _BSPTree__I:
        """
        Get the cut sub-hyperplane.
        
        Returns:
            cut sub-hyperplane, null if this is a leaf tree
        
        
        """
        ...
    def getInteriorPoint(self, defaultPoint: _BSPTree__P) -> 'BSPTree.InteriorPoint'[_BSPTree__S, _BSPTree__P]:
        """
        Get a point that is interior to the cell.
        
        Parameters:
            defaultPoint (BSPTree): default point to return if tree is empty
        
        Returns:
            point that is interior to the cell
        
        Since:
            4.0
        
        
        """
        ...
    def getMinus(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Get the tree on the minus side of the cut hyperplane.
        
        Returns:
            tree on the minus side of the cut hyperplane, null if this is a leaf tree
        
        
        """
        ...
    def getParent(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Get the parent node.
        
        Returns:
            parent node, null if the node has no parents
        
        
        """
        ...
    def getPlus(self) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Get the tree on the plus side of the cut hyperplane.
        
        Returns:
            tree on the plus side of the cut hyperplane, null if this is a leaf tree
        
        
        """
        ...
    def insertCut(self, hyperplane: _BSPTree__H) -> bool:
        """
        Insert a cut sub-hyperplane in a node.
        
        The sub-tree starting at this node will be completely overwritten. The new cut sub-hyperplane will be built from the intersection of the provided hyperplane with the cell. If the hyperplane does intersect the cell, the cell will have two children cells with null attributes on each side of the inserted cut sub-hyperplane. If the hyperplane does not intersect the cell then no cut hyperplane will be inserted and the cell will be changed to a leaf cell. The attribute of the node is never changed.
        
        This method is mainly useful when called on leaf nodes (i.e. nodes for which getCut returns null), in this case it provides a way to build a tree top-down (whereas the  is devoted to build trees bottom-up).
        
        Parameters:
            hyperplane (BSPTree): hyperplane to insert, it will be chopped in order to fit in the cell defined by the parent nodes of the instance
        
        Returns:
            true if a cut sub-hyperplane has been inserted (i.e. if the cell now has two leaf child nodes)
        
        
        """
        ...
    def insertInTree(self, parentTree: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], isPlusChild: bool, vanishingHandler: typing.Union['BSPTree.VanishingCutHandler'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], typing.Callable[['BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane']], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane']]]) -> None:
        """
        Insert the instance into another tree.
        
        The instance itself is modified so its former parent should not be used anymore.
        
        Parameters:
            parentTree (BSPTree<BSPTree, BSPTree, BSPTree, BSPTree> parentTree): parent tree to connect to (may be null)
            isPlusChild (boolean): if true and if parentTree is not null, the resulting tree should be the plus child of its parent, ignored if parentTree
                is null
            vanishingHandler (VanishingCutHandler<BSPTree, BSPTree, BSPTree, BSPTree> vanishingHandler): handler to use for handling very rare corner cases of vanishing cut sub-hyperplanes in internal nodes during merging
        
        Also see:
            LeafMerger
        
        
        """
        ...
    def merge(self, tree: 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], leafMerger: typing.Union['BSPTree.LeafMerger'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I], typing.Callable[['BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane'], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane'], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane'], bool, bool], 'BSPTree'[org.hipparchus.geometry.Space, org.hipparchus.geometry.Point, 'Hyperplane', 'SubHyperplane']]]) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Merge a BSP tree with the instance.
        
        All trees are modified (parts of them are reused in the new tree), it is the responsibility of the caller to ensure a copy has been done before if any of the former tree should be preserved, no such copy is done here!
        
        The algorithm used here is directly derived from the one described in the Naylor, Amanatides and Thibault paper (section III, Binary Partitioning of a BSP Tree).
        
        Parameters:
            tree (BSPTree<BSPTree, BSPTree, BSPTree, BSPTree> tree): other tree to merge with the instance (will be unusable after the operation, as well as the instance itself)
            leafMerger (LeafMerger<BSPTree, BSPTree, BSPTree, BSPTree> leafMerger): object implementing the final merging phase (this is where the semantic of the operation occurs, generally depending on
                the attribute of the leaf node)
        
        Returns:
            a new tree, result of instance <op> tree, this value can be ignored if parentTree is not null since all
            connections have already been established
        
        
        """
        ...
    def pruneAroundConvexCell(self, cellAttribute: typing.Any, otherLeafsAttributes: typing.Any, internalAttributes: typing.Any) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Prune a tree around a cell.
        
        This method can be used to extract a convex cell from a tree. The original cell may either be a leaf node or an internal node. If it is an internal node, it's subtree will be ignored (i.e. the extracted cell will be a leaf node in all cases). The original tree to which the original cell belongs is not touched at all, a new independent tree will be built.
        
        Parameters:
            cellAttribute (Object): attribute to set for the leaf node corresponding to the initial instance cell
            otherLeafsAttributes (Object): attribute to set for the other leaf nodes
            internalAttributes (Object): attribute to set for the internal nodes
        
        Returns:
            a new tree (the original tree is left untouched) containing a single branch with the cell as a leaf node, and other leaf
            nodes as the remnants of the pruned branches
        
        
        """
        ...
    def setAttribute(self, attribute: typing.Any) -> None:
        """
        Associate an attribute with the instance.
        
        Parameters:
            attribute (Object): attribute to associate with the node
        
        Also see:
            getAttribute
        
        
        """
        ...
    def split(self, sub: _BSPTree__I) -> 'BSPTree'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]:
        """
        Split a BSP tree by an external sub-hyperplane.
        
        Split a tree in two halves, on each side of the sub-hyperplane. The instance is not modified.
        
        The tree returned is not upward-consistent: despite all of its sub-trees cut sub-hyperplanes (including its own cut sub-hyperplane) are bounded to the current cell, it is not attached to any parent tree yet. This tree is intended to be later inserted into a higher level tree.
        
        The algorithm used here is the one given in Naylor, Amanatides and Thibault paper (section III, Binary Partitioning of a BSP Tree).
        
        Parameters:
            sub (BSPTree): partitioning sub-hyperplane, must be already clipped to the convex region represented by the instance, will be used as
                the cut sub-hyperplane of the returned tree
        
        Returns:
            a tree having the specified sub-hyperplane as its cut sub-hyperplane, the two parts of the split instance as its two
            sub-trees and a null parent
        
        
        """
        ...
    def visit(self, visitor: 'BSPTreeVisitor'[_BSPTree__S, _BSPTree__P, _BSPTree__H, _BSPTree__I]) -> None:
        """
        Visit the BSP tree nodes.
        
        Parameters:
            visitor (BSPTreeVisitor<BSPTree, BSPTree, BSPTree, BSPTree> visitor): object visiting the tree nodes
        
        
        """
        ...
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
    This interface is used to visit BSPTree nodes.
    
    Navigation through BSPTree can be done using two different point of views:
    
      - the first one is in a node-oriented way using the getPlus,
        getMinus and
        getParent methods. Terminal nodes without associated
        SubHyperplane can be visited this way, there is no constraint in the
        visit order, and it is possible to visit either all nodes or only a subset of the nodes
      - the second one is in a sub-hyperplane-oriented way using classes implementing this interface which obeys the visitor
        design pattern. The visit order is provided by the visitor as each node is first encountered. Each node is visited
        exactly once.
    
    
    Also see:
        BSPTree, SubHyperplane
    """
    def visitInternalNode(self, node: BSPTree[_BSPTreeVisitor__S, _BSPTreeVisitor__P, _BSPTreeVisitor__H, _BSPTreeVisitor__I]) -> None:
        """
        Visit a BSP tree node having a non-null sub-hyperplane.
        
        It is guaranteed that this method will be called after visitOrder has been called for a given node, it wil be called exactly once for each internal node.
        
        Parameters:
            node (BSPTree<BSPTreeVisitor, BSPTreeVisitor, BSPTreeVisitor, BSPTreeVisitor> node): BSP node guaranteed to have a non-null cut sub-hyperplane
        
        Also see:
            visitLeafNode
        
        
        """
        ...
    def visitLeafNode(self, node: BSPTree[_BSPTreeVisitor__S, _BSPTreeVisitor__P, _BSPTreeVisitor__H, _BSPTreeVisitor__I]) -> None:
        """
        Visit a leaf BSP tree node node having a null sub-hyperplane.
        
        Parameters:
            node (BSPTree<BSPTreeVisitor, BSPTreeVisitor, BSPTreeVisitor, BSPTreeVisitor> node): leaf BSP node having a null sub-hyperplane
        
        Also see:
            visitInternalNode
        
        
        """
        ...
    def visitOrder(self, node: BSPTree[_BSPTreeVisitor__S, _BSPTreeVisitor__P, _BSPTreeVisitor__H, _BSPTreeVisitor__I]) -> 'BSPTreeVisitor.Order':
        """
        Determine the visit order for this node.
        
        Before attempting to visit an internal node, this method is called to determine the desired ordering of the visit. It is guaranteed that this method will be called before visitInternalNode for a given node, it will be called exactly once for each internal node.
        
        Parameters:
            node (BSPTree<BSPTreeVisitor, BSPTreeVisitor, BSPTreeVisitor, BSPTreeVisitor> node): BSP node guaranteed to have a non-null cut sub-hyperplane
        
        Returns:
            desired visit order, must be one of PLUS_MINUS_SUB,
            PLUS_SUB_MINUS,
            MINUS_PLUS_SUB,
            MINUS_SUB_PLUS,
            SUB_PLUS_MINUS,
            SUB_MINUS_PLUS
        
        
        """
        ...
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
    Class holding boundary attributes.
    
    This class is used for the attributes associated with the nodes of region boundary shell trees returned by the getTree when the boolean includeBoundaryAttributes parameter is set to true. It contains the parts of the node cut sub-hyperplane that belong to the boundary.
    
    This class is a simple placeholder, it does not provide any processing methods.
    
    Also see:
        getTree
    """
    def getPlusInside(self) -> _BoundaryAttribute__I:
        """
        Get the part of the node cut sub-hyperplane that belongs to the boundary and has the inside of the region on the plus side of its underlying hyperplane.
        
        Returns:
            part of the node cut sub-hyperplane that belongs to the boundary and has the inside of the region on the plus side of
            its underlying hyperplane
        
        
        """
        ...
    def getPlusOutside(self) -> _BoundaryAttribute__I:
        """
        Get the part of the node cut sub-hyperplane that belongs to the boundary and has the outside of the region on the plus side of its underlying hyperplane.
        
        Returns:
            part of the node cut sub-hyperplane that belongs to the boundary and has the outside of the region on the plus side of
            its underlying hyperplane
        
        
        """
        ...
    def getSplitters(self) -> 'NodesSet'[_BoundaryAttribute__S, _BoundaryAttribute__P, _BoundaryAttribute__H, _BoundaryAttribute__I]:
        """
        Get the sub-hyperplanes that were used to split the boundary part.
        
        Returns:
            sub-hyperplanes that were used to split the boundary part
        
        
        """
        ...

_BoundaryProjection__S = typing.TypeVar('_BoundaryProjection__S', bound=org.hipparchus.geometry.Space)  # <S>
_BoundaryProjection__P = typing.TypeVar('_BoundaryProjection__P', bound=org.hipparchus.geometry.Point)  # <P>
class BoundaryProjection(typing.Generic[_BoundaryProjection__S, _BoundaryProjection__P]):
    """
    Class holding the result of point projection on region boundary.
    
    This class is a simple placeholder, it does not provide any processing methods.
    
    Instances of this class are guaranteed to be immutable
    
    Also see:
        projectToBoundary
    """
    def __init__(self, original: _BoundaryProjection__P, projected: _BoundaryProjection__P, offset: float):
        """
        Constructor from raw elements.
        
        Parameters:
            original (BoundaryProjection): original point
            projected (BoundaryProjection): projected point
            offset (double): offset of the point with respect to the boundary it is projected on
        
        
        """
        ...
    def getOffset(self) -> float:
        """
        Offset of the point with respect to the boundary it is projected on.
        
        The offset with respect to the boundary is negative if the getOriginal is inside the region, and positive otherwise.
        
        If there are no boundary, the value is set to either POSITIVE_INFINITY if the region is empty (i.e. all points are outside of the region) or NEGATIVE_INFINITY if the region covers the whole space (i.e. all points are inside of the region).
        
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
    This interface defines mappers between a space and one of its sub-spaces.
    
    Sub-spaces are the lower dimensions subsets of a n-dimensions space. The (n-1)-dimension sub-spaces are specific sub-spaces known as Hyperplane. This interface can be used regardless of the dimensions differences. As an example, Line in 3D implements Embedding< Vector3D, Vector1D>, i.e. it maps directly dimensions 3 and 1.
    
    In the 3D euclidean space, hyperplanes are 2D planes, and the 1D sub-spaces are lines.
    
    Note that this interface is not intended to be implemented by Hipparchus users, it is only intended to be implemented within the library itself. New methods may be added even for minor versions, which breaks compatibility for external implementations.
    
    Also see:
        Hyperplane
    """
    def toSpace(self, point: _Embedding__Q) -> _Embedding__P:
        """
        Transform a sub-space point into a space point.
        
        Parameters:
            point (Embedding): (n-1)-dimension point of the sub-space
        
        Returns:
            n-dimension point of the space corresponding to the specified sub-space point
        
        Also see:
            toSubSpace
        
        
        """
        ...
    def toSubSpace(self, point: _Embedding__P) -> _Embedding__Q:
        """
        Transform a space point into a sub-space point.
        
        Parameters:
            point (Embedding): n-dimension point of the space
        
        Returns:
            (n-1)-dimension point of the sub-space corresponding to the specified space point
        
        Also see:
            toSpace
        
        
        """
        ...

_Hyperplane__S = typing.TypeVar('_Hyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
_Hyperplane__P = typing.TypeVar('_Hyperplane__P', bound=org.hipparchus.geometry.Point)  # <P>
_Hyperplane__H = typing.TypeVar('_Hyperplane__H', bound='Hyperplane')  # <H>
_Hyperplane__I = typing.TypeVar('_Hyperplane__I', bound='SubHyperplane')  # <I>
class Hyperplane(typing.Generic[_Hyperplane__S, _Hyperplane__P, _Hyperplane__H, _Hyperplane__I]):
    """
    This interface represents an hyperplane of a space.
    
    The most prominent place where hyperplane appears in space partitioning is as cutters. Each partitioning node in a BSPTree has a cut SubHyperplane which is either an hyperplane or a part of an hyperplane. In an n-dimensions euclidean space, an hyperplane is an (n-1)-dimensions hyperplane (for example a traditional plane in the 3D euclidean space). They can be more exotic objects in specific fields, for example a circle on the surface of the unit sphere.
    
    Note that this interface is not intended to be implemented by Hipparchus users, it is only intended to be implemented within the library itself. New methods may be added even for minor versions, which breaks compatibility for external implementations.
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
        
        The instance created is completely independent of the original one. A deep copy is used, none of the underlying objects are shared (except for immutable objects).
        
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
    def getOffset(self, point: _Hyperplane__P) -> float:
        """
        Get the offset (oriented distance) of a point.
        
        The offset is 0 if the point is on the underlying hyperplane, it is positive if the point is on one particular side of the hyperplane, and it is negative if the point is on the other side, according to the hyperplane natural orientation.
        
        Parameters:
            point (Hyperplane): point to check
        
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
    def moveToOffset(self, point: _Hyperplane__P, offset: float) -> _Hyperplane__P:
        """
        Move point up to specified offset.
        
        Motion is orthogonal to the hyperplane
        
        Parameters:
            point (Hyperplane): point to move
            offset (double): desired offset
        
        Returns:
            moved point at desired offset
        
        Since:
            4.0
        
        
        """
        ...
    def project(self, point: _Hyperplane__P) -> _Hyperplane__P:
        """
        Project a point to the hyperplane.
        
        Parameters:
            point (Hyperplane): point to project
        
        Returns:
            projected point
        
        
        """
        ...
    def sameOrientationAs(self, other: _Hyperplane__H) -> bool:
        """
        Check if the instance has the same orientation as another hyperplane.
        
        This method is expected to be called on parallel hyperplanes. The method should not re-check for parallelism, only for orientation, typically by testing something like the sign of the dot-products of normals.
        
        Parameters:
            other (Hyperplane): other hyperplane to check against the instance
        
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
    def wholeSpace(self) -> 'Region'[_Hyperplane__S, _Hyperplane__P, _Hyperplane__H, _Hyperplane__I]:
        """
        Build a region covering the whole space.
        
        Returns:
            a region containing the instance
        
        
        """
        ...

_NodesSet__S = typing.TypeVar('_NodesSet__S', bound=org.hipparchus.geometry.Space)  # <S>
_NodesSet__P = typing.TypeVar('_NodesSet__P', bound=org.hipparchus.geometry.Point)  # <P>
_NodesSet__H = typing.TypeVar('_NodesSet__H', bound=Hyperplane)  # <H>
_NodesSet__I = typing.TypeVar('_NodesSet__I', bound='SubHyperplane')  # <I>
class NodesSet(java.lang.Iterable[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Generic[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]):
    """
    Set of BSPTree nodes.
    
    Also see:
        BoundaryAttribute
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def add(self, node: BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]) -> None:
        """
        Add a node if not already known.
        
        Parameters:
            node (BSPTree<NodesSet, NodesSet, NodesSet, NodesSet> node): node to add
        
        
        """
        ...
    def addAll(self, iterator: typing.Union[java.lang.Iterable[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Sequence[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Set[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]], typing.Callable[[], java.util.Iterator[typing.Any]]]) -> None:
        """
        Add nodes if they are not already known.
        
        Parameters:
            iterator (Iterable<BSPTree<NodesSet, NodesSet, NodesSet, NodesSet>>): nodes iterator
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[BSPTree[_NodesSet__S, _NodesSet__P, _NodesSet__H, _NodesSet__I]]:
        """
        Specified by: Iterable in interface Iterable
        
        
        """
        ...

_Region__S = typing.TypeVar('_Region__S', bound=org.hipparchus.geometry.Space)  # <S>
_Region__P = typing.TypeVar('_Region__P', bound=org.hipparchus.geometry.Point)  # <P>
_Region__H = typing.TypeVar('_Region__H', bound=Hyperplane)  # <H>
_Region__I = typing.TypeVar('_Region__I', bound='SubHyperplane')  # <I>
class Region(typing.Generic[_Region__S, _Region__P, _Region__H, _Region__I]):
    """
    This interface represents a region of a space as a partition.
    
    Region are subsets of a space, they can be infinite (whole space, half space, infinite stripe ...) or finite (polygons in 2D, polyhedrons in 3D ...). Their main characteristic is to separate points that are considered to be inside the region from points considered to be outside of it. In between, there may be points on the boundary of the region.
    
    This implementation is limited to regions for which the boundary is composed of several SubHyperplane, including regions with no boundary at all: the whole space and the empty region. They are not necessarily finite and not necessarily path-connected. They can contain holes.
    
    Regions can be combined using the traditional sets operations : union, intersection, difference and symetric difference (exclusive or) for the binary operations, complement for the unary operation.
    
    Note that this interface is not intended to be implemented by Hipparchus users, it is only intended to be implemented within the library itself. New methods may be added even for minor versions, which breaks compatibility for external implementations.
    """
    def buildNew(self, newTree: BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]) -> 'Region'[_Region__S, _Region__P, _Region__H, _Region__I]:
        """
        Build a region using the instance as a prototype.
        
        This method allow to create new instances without knowing exactly the type of the region. It is an application of the prototype design pattern.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Parameters:
            newTree (BSPTree<Region, Region, Region, Region> newTree): inside/outside BSP tree representing the new region
        
        Returns:
            the built region
        
        
        """
        ...
    def checkPoint(self, point: _Region__P) -> 'Region.Location':
        """
        Check a point with respect to the region.
        
        Parameters:
            point (Region): point to check
        
        Returns:
            a code representing the point status: either INSIDE,
            OUTSIDE or
            BOUNDARY
        
        
        """
        ...
    def contains(self, region: 'Region'[_Region__S, _Region__P, _Region__H, _Region__I]) -> bool:
        """
        Check if the instance entirely contains another region.
        
        Parameters:
            region (Region<Region, Region, Region, Region> region): region to check against the instance
        
        Returns:
            true if the instance contains the specified tree
        
        
        """
        ...
    def copySelf(self) -> 'Region'[_Region__S, _Region__P, _Region__H, _Region__I]:
        """
        Copy the instance.
        
        The instance created is completely independant of the original one. A deep copy is used, none of the underlying objects are shared (except for the underlying tree Boolean attributes and immutable objects).
        
        Returns:
            a new region, copy of the instance
        
        
        """
        ...
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
    def getTree(self, includeBoundaryAttributes: bool) -> BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]:
        """
        Get the underlying BSP tree.
        
        Regions are represented by an underlying inside/outside BSP tree whose leaf attributes are Boolean instances representing inside leaf cells if the attribute value is true and outside leaf cells if the attribute is false. These leaf attributes are always present and guaranteed to be non null.
        
        In addition to the leaf attributes, the internal nodes which correspond to cells split by cut sub-hyperplanes may contain BoundaryAttribute objects representing the parts of the corresponding cut sub-hyperplane that belong to the boundary. When the boundary attributes have been computed, all internal nodes are guaranteed to have non-null attributes, however some BoundaryAttribute instances may have their getPlusInside and getPlusOutside methods both returning null if the corresponding cut sub-hyperplane does not have any parts belonging to the boundary.
        
        Since computing the boundary is not always required and can be time-consuming for large trees, these internal nodes attributes are computed using lazy evaluation only when required by setting the includeBoundaryAttributes argument to true. Once computed, these attributes remain in the tree, which implies that in this case, further calls to the method for the same region will always include these attributes regardless of the value of the includeBoundaryAttributes argument.
        
        Parameters:
            includeBoundaryAttributes (boolean): if true, the boundary attributes at internal nodes are guaranteed to be included (they may be included even if the
                argument is false, if they have already been computed due to a previous call)
        
        Returns:
            underlying BSP tree
        
        Also see:
            BoundaryAttribute
        
        
        """
        ...
    def intersection(self, sub: _Region__I) -> _Region__I:
        """
        Get the parts of a sub-hyperplane that are contained in the region.
        
        The parts of the sub-hyperplane that belong to the boundary are not included in the resulting parts.
        
        Parameters:
            sub (Region): sub-hyperplane traversing the region
        
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
        
        boolean isEmpty (BSPTree<Region, Region, Region, Region> node)
        
        Check if the sub-tree starting at a given node is empty.
        
        Parameters:
            node (BSPTree<Region, Region, Region, Region> node): root node of the sub-tree (must have Region tree semantics, i.e. the
                leaf nodes must have Boolean attributes representing an inside/outside property)
        
        Returns:
            true if the sub-tree starting at the given node is empty
        
        
        """
        ...
    @typing.overload
    def isEmpty(self, node: BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool:
        """
        Check if the instance covers the full space.
        
        Returns:
            true if the instance covers the full space
        
        boolean isFull (BSPTree<Region, Region, Region, Region> node)
        
        Check if the sub-tree starting at a given node covers the full space.
        
        Parameters:
            node (BSPTree<Region, Region, Region, Region> node): root node of the sub-tree (must have Region tree semantics, i.e. the
                leaf nodes must have Boolean attributes representing an inside/outside property)
        
        Returns:
            true if the sub-tree starting at the given node covers the full space
        
        
        """
        ...
    @typing.overload
    def isFull(self, node: BSPTree[_Region__S, _Region__P, _Region__H, _Region__I]) -> bool: ...
    def projectToBoundary(self, point: _Region__P) -> BoundaryProjection[_Region__S, _Region__P]:
        """
        Project a point on the boundary of the region.
        
        Parameters:
            point (Region): point to check
        
        Returns:
            projection of the point on the boundary
        
        
        """
        ...
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
    This class is a factory for Region.
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def buildConvex(self, *hyperplanes: _RegionFactory__H) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]:
        """
        Build a convex region from a collection of bounding hyperplanes.
        
        Parameters:
            hyperplanes (RegionFactory...): collection of bounding hyperplanes
        
        Returns:
            a new convex region, or null if the collection is empty
        
        
        """
        ...
    def difference(self, region1: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]:
        """
        Compute the difference of two regions.
        
        Parameters:
            region1 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region1): first region (will be unusable after the operation as parts of it will be reused in the new region)
            region2 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region2): second region (will be unusable after the operation as parts of it will be reused in the new region)
        
        Returns:
            a new region, result of region1 minus region2
        
        
        """
        ...
    def getComplement(self, region: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]:
        """
        Get the complement of the region (exchanged interior/exterior).
        
        Parameters:
            region (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region): region to complement, it will not be modified, a new region independent region will be built
        
        Returns:
            a new region, complement of the specified one
        
        
        """
        ...
    def intersection(self, region1: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]:
        """
        Compute the intersection of two regions.
        
        Parameters:
            region1 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region1): first region (will be unusable after the operation as parts of it will be reused in the new region)
            region2 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region2): second region (will be unusable after the operation as parts of it will be reused in the new region)
        
        Returns:
            a new region, result of region1 intersection region2
        
        
        """
        ...
    def union(self, region1: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]:
        """
        Compute the union of two regions.
        
        Parameters:
            region1 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region1): first region (will be unusable after the operation as parts of it will be reused in the new region)
            region2 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region2): second region (will be unusable after the operation as parts of it will be reused in the new region)
        
        Returns:
            a new region, result of region1 union region2
        
        
        """
        ...
    def xor(self, region1: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I], region2: Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]) -> Region[_RegionFactory__S, _RegionFactory__P, _RegionFactory__H, _RegionFactory__I]:
        """
        Compute the symmetric difference (exclusive or) of two regions.
        
        Parameters:
            region1 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region1): first region (will be unusable after the operation as parts of it will be reused in the new region)
            region2 (Region<RegionFactory, RegionFactory, RegionFactory, RegionFactory> region2): second region (will be unusable after the operation as parts of it will be reused in the new region)
        
        Returns:
            a new region, result of region1 xor region2
        
        
        """
        ...

class Side(java.lang.Enum['Side']):
    """
    Enumerate representing the location of an element with respect to an Hyperplane of a space.
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
    def valueOf(name: str) -> 'Side':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['Side']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (Side c : Side.values())
            System.out.println(c);
        
        
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
    This interface represents the remaining parts of an hyperplane after other parts have been chopped off.
    
    sub-hyperplanes are obtained when parts of an Hyperplane are chopped off by other hyperplanes that intersect it. The remaining part is a convex region. Such objects appear in BSPTree as the intersection of a cut hyperplane with the convex region which it splits, the chopping hyperplanes are the cut hyperplanes closer to the tree root.
    
    Note that this interface is not intended to be implemented by Hipparchus users, it is only intended to be implemented within the library itself. New methods may be added even for minor versions, which breaks compatibility for external implementations.
    """
    def copySelf(self) -> _SubHyperplane__I:
        """
        Copy the instance.
        
        The instance created is completely independent from the original one. A deep copy is used, none of the underlying objects are shared (except for the nodes attributes and immutable objects).
        
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
    def reunite(self, other: _SubHyperplane__I) -> _SubHyperplane__I:
        """
        Compute the union of the instance and another sub-hyperplane.
        
        Parameters:
            other (SubHyperplane): other sub-hyperplane to union (must be in the same hyperplane as the instance)
        
        Returns:
            a new sub-hyperplane, union of the instance and other
        
        
        """
        ...
    def split(self, hyperplane: _SubHyperplane__H) -> 'SubHyperplane.SplitSubHyperplane'[_SubHyperplane__S, _SubHyperplane__P, _SubHyperplane__H, _SubHyperplane__I]:
        """
        Split the instance in two parts by an hyperplane.
        
        Parameters:
            hyperplane (SubHyperplane): splitting hyperplane
        
        Returns:
            an object containing both the part of the instance on the plus side of the hyperplane and the part of the instance on
            the minus side of the hyperplane
        
        
        """
        ...
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
    This interface represents an inversible affine transform in a space.
    
    Inversible affine transform include for example scalings, translations, rotations.
    
    Transforms are dimension-specific. The consistency rules between the three apply methods are the following ones for a transformed defined for dimension D:
    
      - the transform can be applied to a point in the D-dimension space using its
        apply method
      - the transform can be applied to a (D-1)-dimension hyperplane in the D-dimension space using its
        apply method
      - the transform can be applied to a (D-2)-dimension sub-hyperplane in a (D-1)-dimension hyperplane using its
        apply method
    """
    @typing.overload
    def apply(self, point: _Transform__P) -> _Transform__P:
        """
        Transform a point of a space.
        
        Parameters:
            point (Transform): point to transform
        
        Returns:
            a new object representing the transformed point
        
        Transform an hyperplane of a space.
        
        Parameters:
            hyperplane (Transform): hyperplane to transform
        
        Returns:
            a new object representing the transformed hyperplane
        
        Transform a sub-hyperplane embedded in an hyperplane.
        
        Parameters:
            sub (Transform): sub-hyperplane to transform
            original (Transform): hyperplane in which the sub-hyperplane is defined (this is the original hyperplane, the transform has not been applied
                to it)
            transformed (Transform): hyperplane in which the sub-hyperplane is defined (this is the transformed hyperplane, the transform has been applied
                to it)
        
        Returns:
            a new object representing the transformed sub-hyperplane
        
        
        """
        ...
    @typing.overload
    def apply(self, h: _Transform__H) -> _Transform__H: ...
    @typing.overload
    def apply(self, sub: _Transform__J, original: _Transform__H, transformed: _Transform__H) -> _Transform__J: ...

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
    Abstract class for all regions, independently of geometry type or dimension.
    """
    def __init__(self, hArray: typing.Union[typing.List[_AbstractRegion__H], jpype.JArray], double: float):
        """
        Build a region representing the whole space.
        
        Parameters:
            tolerance (double): tolerance below which points are considered identical.
        
        protected AbstractRegion (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> tree, double tolerance)
        
        Build a region from an inside/outside BSP tree.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Parameters:
            tree (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> tree): inside/outside BSP tree representing the region
            tolerance (double): tolerance below which points are considered identical.
        
        protected AbstractRegion (Collection<AbstractRegion> boundary, double tolerance)
        
        Build a Region from a Boundary REPresentation (B-rep).
        
        The boundary is provided as a collection of SubHyperplane. Each sub-hyperplane has the interior part of the region on its minus side and the exterior on its plus side.
        
        The boundary elements can be in any order, and can form several non-connected sets (like for example polygons with holes or a set of disjoints polyhedrons considered as a whole). In fact, the elements do not even need to be connected together (their topological connections are not used here). However, if the boundary does not really separate an inside open from an outside open (open having here its topological meaning), then subsequent calls to the checkPoint method will not be meaningful anymore.
        
        If the boundary is empty, the region will represent the whole space.
        
        Parameters:
            boundary (Collection<AbstractRegion> boundary):             collection of boundary elements, as a collection of SubHyperplane objects
            tolerance (double): tolerance below which points are considered identical.
        
        public AbstractRegion (AbstractRegion[] hyperplanes, double tolerance)
        
        Build a convex region from an array of bounding hyperplanes.
        
        Parameters:
            hyperplanes (AbstractRegion[]): array of bounding hyperplanes (if null, an empty region will be built)
            tolerance (double): tolerance below which points are considered identical.
        
        
        """
        ...
    def applyTransform(self, transform: Transform[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]:
        """
        Transform a region.
        
        Applying a transform to a region consist in applying the transform to all the hyperplanes of the underlying BSP tree and of the boundary (and also to the sub-hyperplanes embedded in these hyperplanes) and to the barycenter. The instance is not modified, a new instance is built.
        
        Parameters:
            transform (Transform<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> transform): transform to apply
        
        Returns:
            a new region, resulting from the application of the transform to the instance
        
        
        """
        ...
    def buildNew(self, newTree: BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]:
        """
        Build a region using the instance as a prototype.
        
        This method allow to create new instances without knowing exactly the type of the region. It is an application of the prototype design pattern.
        
        The leaf nodes of the BSP tree must have a Boolean attribute representing the inside status of the corresponding cell (true for inside cells, false for outside cells). In order to avoid building too many small objects, it is recommended to use the predefined constants TRUE and FALSE. The tree also must have either null internal nodes or internal nodes representing the boundary as specified in the getTree method).
        
        Specified by: buildNew in interface Region
        
        Parameters:
            newTree (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> newTree): inside/outside BSP tree representing the new region
        
        Returns:
            the built region
        
        
        """
        ...
    def checkPoint(self, point: _AbstractRegion__P) -> Region.Location:
        """
        Check a point with respect to the region.
        
        Specified by: checkPoint in interface Region
        
        Parameters:
            point (AbstractRegion): point to check
        
        Returns:
            a code representing the point status: either INSIDE,
            OUTSIDE or
            BOUNDARY
        
        protected Location checkPoint (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> node, AbstractRegion point)
        
        Check a point with respect to the region starting at a given node.
        
        Parameters:
            node (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> node): root node of the region
            point (AbstractRegion): point to check
        
        Returns:
            a code representing the point status: either INSIDE,
            OUTSIDE or
            BOUNDARY
        
        
        """
        ...
    def contains(self, region: Region[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> bool:
        """
        Check if the instance entirely contains another region.
        
        Specified by: contains in interface Region
        
        Parameters:
            region (Region<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> region): region to check against the instance
        
        Returns:
            true if the instance contains the specified tree
        
        
        """
        ...
    def copySelf(self) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I, _AbstractRegion__T, _AbstractRegion__Q, _AbstractRegion__F, _AbstractRegion__J]:
        """
        Copy the instance.
        
        The instance created is completely independant of the original one. A deep copy is used, none of the underlying objects are shared (except for the underlying tree Boolean attributes and immutable objects).
        
        Specified by: copySelf in interface Region
        
        Returns:
            a new region, copy of the instance
        
        
        """
        ...
    def getBarycenter(self) -> _AbstractRegion__P:
        """
        Get the barycenter of the instance.
        
        Specified by: getBarycenter in interface Region
        
        Returns:
            an object representing the barycenter
        
        
        """
        ...
    def getBoundarySize(self) -> float:
        """
        Get the size of the boundary.
        
        Specified by: getBoundarySize in interface Region
        
        Returns:
            the size of the boundary (this is 0 in 1D, a length in 2D, an area in 3D ...)
        
        
        """
        ...
    def getSize(self) -> float:
        """
        Get the size of the instance.
        
        Specified by: getSize in interface Region
        
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
    def getTree(self, includeBoundaryAttributes: bool) -> BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]:
        """
        Get the underlying BSP tree.
        
        Regions are represented by an underlying inside/outside BSP tree whose leaf attributes are Boolean instances representing inside leaf cells if the attribute value is true and outside leaf cells if the attribute is false. These leaf attributes are always present and guaranteed to be non null.
        
        In addition to the leaf attributes, the internal nodes which correspond to cells split by cut sub-hyperplanes may contain BoundaryAttribute objects representing the parts of the corresponding cut sub-hyperplane that belong to the boundary. When the boundary attributes have been computed, all internal nodes are guaranteed to have non-null attributes, however some BoundaryAttribute instances may have their getPlusInside and getPlusOutside methods both returning null if the corresponding cut sub-hyperplane does not have any parts belonging to the boundary.
        
        Since computing the boundary is not always required and can be time-consuming for large trees, these internal nodes attributes are computed using lazy evaluation only when required by setting the includeBoundaryAttributes argument to true. Once computed, these attributes remain in the tree, which implies that in this case, further calls to the method for the same region will always include these attributes regardless of the value of the includeBoundaryAttributes argument.
        
        Specified by: getTree in interface Region
        
        Parameters:
            includeBoundaryAttributes (boolean): if true, the boundary attributes at internal nodes are guaranteed to be included (they may be included even if the
                argument is false, if they have already been computed due to a previous call)
        
        Returns:
            underlying BSP tree
        
        Also see:
            BoundaryAttribute
        
        
        """
        ...
    def intersection(self, sub: _AbstractRegion__I) -> _AbstractRegion__I:
        """
        Get the parts of a sub-hyperplane that are contained in the region.
        
        The parts of the sub-hyperplane that belong to the boundary are not included in the resulting parts.
        
        Specified by: intersection in interface Region
        
        Parameters:
            sub (AbstractRegion): sub-hyperplane traversing the region
        
        Returns:
            filtered sub-hyperplane
        
        
        """
        ...
    @typing.overload
    def isEmpty(self) -> bool:
        """
        Check if the instance is empty.
        
        Specified by: isEmpty in interface Region
        
        Returns:
            true if the instance is empty
        
        public boolean isEmpty (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> node)
        
        Check if the sub-tree starting at a given node is empty.
        
        Specified by: isEmpty in interface Region
        
        Parameters:
            node (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> node): root node of the sub-tree (must have Region tree semantics, i.e. the
                leaf nodes must have Boolean attributes representing an inside/outside property)
        
        Returns:
            true if the sub-tree starting at the given node is empty
        
        
        """
        ...
    @typing.overload
    def isEmpty(self, node: BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool:
        """
        Check if the instance covers the full space.
        
        Specified by: isFull in interface Region
        
        Returns:
            true if the instance covers the full space
        
        public boolean isFull (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> node)
        
        Check if the sub-tree starting at a given node covers the full space.
        
        Specified by: isFull in interface Region
        
        Parameters:
            node (BSPTree<AbstractRegion, AbstractRegion, AbstractRegion, AbstractRegion> node): root node of the sub-tree (must have Region tree semantics, i.e. the
                leaf nodes must have Boolean attributes representing an inside/outside property)
        
        Returns:
            true if the sub-tree starting at the given node covers the full space
        
        
        """
        ...
    @typing.overload
    def isFull(self, node: BSPTree[_AbstractRegion__S, _AbstractRegion__P, _AbstractRegion__H, _AbstractRegion__I]) -> bool: ...
    def projectToBoundary(self, point: _AbstractRegion__P) -> BoundaryProjection[_AbstractRegion__S, _AbstractRegion__P]:
        """
        Project a point on the boundary of the region.
        
        Specified by: projectToBoundary in interface Region
        
        Parameters:
            point (AbstractRegion): point to check
        
        Returns:
            projection of the point on the boundary
        
        
        """
        ...

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
    This class implements the dimension-independent parts of SubHyperplane.
    
    sub-hyperplanes are obtained when parts of an Hyperplane are chopped off by other hyperplanes that intersect it. The remaining part is a convex region. Such objects appear in BSPTree as the intersection of a cut hyperplane with the convex region which it splits, the chopping hyperplanes are the cut hyperplanes closer to the tree root.
    """
    def applyTransform(self, transform: Transform[_AbstractSubHyperplane__S, _AbstractSubHyperplane__P, _AbstractSubHyperplane__H, _AbstractSubHyperplane__I, _AbstractSubHyperplane__T, _AbstractSubHyperplane__Q, _AbstractSubHyperplane__F, _AbstractSubHyperplane__J]) -> _AbstractSubHyperplane__I:
        """
        Apply a transform to the instance.
        
        The instance must be a (D-1)-dimension sub-hyperplane with respect to the transform not a (D-2)-dimension sub-hyperplane the transform knows how to transform by itself. The transform will consist in transforming first the hyperplane and then the all region using the various methods provided by the transform.
        
        Parameters:
            transform (Transform<AbstractSubHyperplane, AbstractSubHyperplane, AbstractSubHyperplane, AbstractSubHyperplane, AbstractSubHyperplane, AbstractSubHyperplane, AbstractSubHyperplane, AbstractSubHyperplane> transform): D-dimension transform to apply
        
        Returns:
            the transformed instance
        
        
        """
        ...
    def copySelf(self) -> _AbstractSubHyperplane__I:
        """
        Copy the instance.
        
        The instance created is completely independent from the original one. A deep copy is used, none of the underlying objects are shared (except for the nodes attributes and immutable objects).
        
        Specified by: copySelf in interface SubHyperplane
        
        Returns:
            a new sub-hyperplane, copy of the instance
        
        
        """
        ...
    def getHyperplane(self) -> _AbstractSubHyperplane__H:
        """
        Get the underlying hyperplane.
        
        Specified by: getHyperplane in interface SubHyperplane
        
        Returns:
            underlying hyperplane
        
        
        """
        ...
    def getRemainingRegion(self) -> Region[_AbstractSubHyperplane__T, _AbstractSubHyperplane__Q, _AbstractSubHyperplane__F, _AbstractSubHyperplane__J]:
        """
        Get the remaining region of the hyperplane.
        
        The returned region is expressed in the canonical hyperplane frame and has the hyperplane dimension. For example a chopped hyperplane in the 3D euclidean is a 2D plane and the corresponding region is a convex 2D polygon.
        
        Returns:
            remaining region of the hyperplane
        
        
        """
        ...
    def getSize(self) -> float:
        """
        Get the size of the instance.
        
        Specified by: getSize in interface SubHyperplane
        
        Returns:
            the size of the instance (this is a length in 1D, an area in 2D, a volume in 3D ...)
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
        Check if the instance is empty.
        
        Specified by: isEmpty in interface SubHyperplane
        
        Returns:
            true if the instance is empty
        
        
        """
        ...
    def reunite(self, other: _AbstractSubHyperplane__I) -> _AbstractSubHyperplane__I:
        """
        Compute the union of the instance and another sub-hyperplane.
        
        Specified by: reunite in interface SubHyperplane
        
        Parameters:
            other (AbstractSubHyperplane): other sub-hyperplane to union (must be in the same hyperplane as the instance)
        
        Returns:
            a new sub-hyperplane, union of the instance and other
        
        
        """
        ...
    def split(self, hyper: _AbstractSubHyperplane__H) -> SubHyperplane.SplitSubHyperplane[_AbstractSubHyperplane__S, _AbstractSubHyperplane__P, _AbstractSubHyperplane__H, _AbstractSubHyperplane__I]:
        """
        Split the instance in two parts by an hyperplane.
        
        Specified by: split in interface SubHyperplane
        
        Parameters:
            hyper (AbstractSubHyperplane): splitting hyperplane
        
        Returns:
            an object containing both the part of the instance on the plus side of the hyperplane and the part of the instance on
            the minus side of the hyperplane
        
        
        """
        ...

_InteriorPointFinder__S = typing.TypeVar('_InteriorPointFinder__S', bound=org.hipparchus.geometry.Space)  # <S>
_InteriorPointFinder__P = typing.TypeVar('_InteriorPointFinder__P', bound=org.hipparchus.geometry.Point)  # <P>
_InteriorPointFinder__H = typing.TypeVar('_InteriorPointFinder__H', bound=Hyperplane)  # <H>
_InteriorPointFinder__I = typing.TypeVar('_InteriorPointFinder__I', bound=SubHyperplane)  # <I>
class InteriorPointFinder(BSPTreeVisitor[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I], typing.Generic[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]):
    """
    Finder for interior points.
    
    Since:
        4.0
    """
    def __init__(self, defaultPoint: _InteriorPointFinder__P):
        """
        Simple constructor.
        
        Parameters:
            defaultPoint (InteriorPointFinder): default point to use for whole space
        
        
        """
        ...
    def getPoint(self) -> BSPTree.InteriorPoint[_InteriorPointFinder__S, _InteriorPointFinder__P]:
        """
        Get the point found.
        
        Returns:
            found point (null if tree was empty)
        
        
        """
        ...
    def visitInternalNode(self, node: BSPTree[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]) -> None:
        """
        Visit a BSP tree node having a non-null sub-hyperplane.
        
        It is guaranteed that this method will be called after visitOrder has been called for a given node, it wil be called exactly once for each internal node.
        
        Specified by: visitInternalNode in interface BSPTreeVisitor
        
        Parameters:
            node (BSPTree<InteriorPointFinder, InteriorPointFinder, InteriorPointFinder, InteriorPointFinder> node): BSP node guaranteed to have a non-null cut sub-hyperplane
        
        Also see:
            visitLeafNode
        
        
        """
        ...
    def visitLeafNode(self, node: BSPTree[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]) -> None:
        """
        Visit a leaf BSP tree node node having a null sub-hyperplane.
        
        Specified by: visitLeafNode in interface BSPTreeVisitor
        
        Parameters:
            node (BSPTree<InteriorPointFinder, InteriorPointFinder, InteriorPointFinder, InteriorPointFinder> node): leaf BSP node having a null sub-hyperplane
        
        Also see:
            visitInternalNode
        
        
        """
        ...
    def visitOrder(self, node: BSPTree[_InteriorPointFinder__S, _InteriorPointFinder__P, _InteriorPointFinder__H, _InteriorPointFinder__I]) -> BSPTreeVisitor.Order:
        """
        Determine the visit order for this node.
        
        Before attempting to visit an internal node, this method is called to determine the desired ordering of the visit. It is guaranteed that this method will be called before visitInternalNode for a given node, it will be called exactly once for each internal node.
        
        Specified by: visitOrder in interface BSPTreeVisitor
        
        Parameters:
            node (BSPTree<InteriorPointFinder, InteriorPointFinder, InteriorPointFinder, InteriorPointFinder> node): BSP node guaranteed to have a non-null cut sub-hyperplane
        
        Returns:
            desired visit order, must be one of PLUS_MINUS_SUB,
            PLUS_SUB_MINUS,
            MINUS_PLUS_SUB,
            MINUS_SUB_PLUS,
            SUB_PLUS_MINUS,
            SUB_MINUS_PLUS
        
        
        """
        ...


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
