import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.spherical.twod
import org.orekit.bodies
import org.orekit.frames
import org.orekit.propagation.events
import typing



class FieldOfView:
    """
    public interface FieldOfView
    
        Interface representing a spacecraft sensor Field Of View.
    
        Fields Of View are zones defined on the unit sphere centered on the spacecraft. Different implementations may use
        specific modeling depending on the shape.
    
        Since:
            10.1
    """
    def getFootprint(self, transform: org.orekit.frames.Transform, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]: ...
    def getMargin(self) -> float:
        """
            Get the angular margin to apply (radians). If angular margin is positive, points outside of the raw FoV but close enough
            to the boundary are considered visible. If angular margin is negative, points inside of the raw FoV but close enough to
            the boundary are considered not visible
        
            Returns:
                angular margin
        
            Also see:
                :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def offsetFromBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, visibilityTrigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
            Get the offset of target body with respect to the Field Of View Boundary.
        
            The offset is the signed angular distance between target body and closest boundary point, taking into account
            :class:`~org.orekit.propagation.events.VisibilityTrigger` and :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin`.
        
            As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be
            outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed
            about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of
            View margin and should be designed to still return a positive value if the full accurate computation would return a
            positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate
            computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary
            crossings (taking :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin` into account), which correspond to sign changes of the offset.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
                angularRadius (double): target body angular radius
                trigger (:class:`~org.orekit.propagation.events.VisibilityTrigger`): visibility trigger for spherical bodies
        
            Returns:
                an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
                (note that this cannot take into account interposing bodies)
        
            Also see:
                :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def projectToBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the direction on Field Of View Boundary closest to a line of sight.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
            Returns:
                direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...

class AbstractFieldOfView(FieldOfView):
    """
    public abstract class AbstractFieldOfView extends Object implements :class:`~org.orekit.geometry.fov.FieldOfView`
    
        Abstract class representing a spacecraft sensor Field Of View.
    
        Since:
            10.1
    """
    def getMargin(self) -> float:
        """
            Get the angular margin to apply (radians). If angular margin is positive, points outside of the raw FoV but close enough
            to the boundary are considered visible. If angular margin is negative, points inside of the raw FoV but close enough to
            the boundary are considered not visible
        
            Specified by:
                :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin` in interface :class:`~org.orekit.geometry.fov.FieldOfView`
        
            Returns:
                angular margin
        
            Also see:
                :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`
        
        
        """
        ...

class PythonFieldOfView(FieldOfView):
    """
    public class PythonFieldOfView extends Object implements :class:`~org.orekit.geometry.fov.FieldOfView`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getFootprint(self, transform: org.orekit.frames.Transform, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]: ...
    def getMargin(self) -> float:
        """
            Get the angular margin to apply (radians). If angular margin is positive, points outside of the raw FoV but close enough
            to the boundary are considered visible. If angular margin is negative, points inside of the raw FoV but close enough to
            the boundary are considered not visible
        
            Specified by:
                :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin` in interface :class:`~org.orekit.geometry.fov.FieldOfView`
        
            Returns:
                angular margin
        
            Also see:
                :meth:`~org.orekit.geometry.fov.PythonFieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def offsetFromBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, visibilityTrigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
            Get the offset of target body with respect to the Field Of View Boundary.
        
            The offset is the signed angular distance between target body and closest boundary point, taking into account
            :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.PythonFieldOfView.getMargin`.
        
            As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be
            outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed
            about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of
            View margin and should be designed to still return a positive value if the full accurate computation would return a
            positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate
            computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary
            crossings (taking :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.PythonFieldOfView.getMargin` into account), which correspond to sign changes of the
            offset.
        
            Specified by:
                :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`Â in
                interfaceÂ :class:`~org.orekit.geometry.fov.FieldOfView`
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
                angularRadius (double): target body angular radius
                trigger (:class:`~org.orekit.propagation.events.VisibilityTrigger`): visibility trigger for spherical bodies
        
            Returns:
                an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
                (note that this cannot take into account interposing bodies)
        
            Also see:
                :meth:`~org.orekit.geometry.fov.PythonFieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def projectToBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the direction on Field Of View Boundary closest to a line of sight.
        
            Specified by:
                :meth:`~org.orekit.geometry.fov.FieldOfView.projectToBoundary`Â in
                interfaceÂ :class:`~org.orekit.geometry.fov.FieldOfView`
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
            Returns:
                direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class PolygonalFieldOfView(AbstractFieldOfView):
    """
    public class PolygonalFieldOfView extends :class:`~org.orekit.geometry.fov.AbstractFieldOfView`
    
        Class representing a spacecraft sensor Field Of View with polygonal shape.
    
        Fields Of View are zones defined on the unit sphere centered on the spacecraft. They can have any shape, they can be
        split in several non-connected patches and can have holes.
    
        Since:
            10.1
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, definingConeType: 'PolygonalFieldOfView.DefiningConeType', vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, int: int, double2: float): ...
    @typing.overload
    def __init__(self, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, double: float): ...
    def getFootprint(self, transform: org.orekit.frames.Transform, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]: ...
    def getZone(self) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet:
        """
            Get the interior zone.
        
            Returns:
                the interior zone
        
        
        """
        ...
    def offsetFromBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, visibilityTrigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
            Get the offset of target body with respect to the Field Of View Boundary.
        
            The offset is the signed angular distance between target body and closest boundary point, taking into account
            :class:`~org.orekit.propagation.events.VisibilityTrigger` and :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin`.
        
            As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be
            outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed
            about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of
            View margin and should be designed to still return a positive value if the full accurate computation would return a
            positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate
            computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary
            crossings (taking :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin` into account), which correspond to sign changes of the offset.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
                angularRadius (double): target body angular radius
                trigger (:class:`~org.orekit.propagation.events.VisibilityTrigger`): visibility trigger for spherical bodies
        
            Returns:
                an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
                (note that this cannot take into account interposing bodies)
        
            Also see:
                :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def projectToBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the direction on Field Of View Boundary closest to a line of sight.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
            Returns:
                direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...
    class DefiningConeType(java.lang.Enum['PolygonalFieldOfView.DefiningConeType']):
        INSIDE_CONE_TOUCHING_POLYGON_AT_EDGES_MIDDLE: typing.ClassVar['PolygonalFieldOfView.DefiningConeType'] = ...
        OUTSIDE_CONE_TOUCHING_POLYGON_AT_VERTICES: typing.ClassVar['PolygonalFieldOfView.DefiningConeType'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'PolygonalFieldOfView.DefiningConeType': ...
        @staticmethod
        def values() -> typing.List['PolygonalFieldOfView.DefiningConeType']: ...

class PythonAbstractFieldOfView(AbstractFieldOfView):
    """
    public class PythonAbstractFieldOfView extends :class:`~org.orekit.geometry.fov.AbstractFieldOfView`
    """
    def __init__(self, double: float): ...
    def finalize(self) -> None: ...
    def getFootprint(self, transform: org.orekit.frames.Transform, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]: ...
    def offsetFromBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, visibilityTrigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
            Get the offset of target body with respect to the Field Of View Boundary.
        
            The offset is the signed angular distance between target body and closest boundary point, taking into account
            :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.AbstractFieldOfView.getMargin`.
        
            As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be
            outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed
            about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of
            View margin and should be designed to still return a positive value if the full accurate computation would return a
            positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate
            computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary
            crossings (taking :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.AbstractFieldOfView.getMargin` into account), which correspond to sign changes of the
            offset.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
                angularRadius (double): target body angular radius
                trigger (:class:`~org.orekit.propagation.events.VisibilityTrigger`): visibility trigger for spherical bodies
        
            Returns:
                an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
                (note that this cannot take into account interposing bodies)
        
            Also see:
                :meth:`~org.orekit.geometry.fov.PythonAbstractFieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def projectToBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the direction on Field Of View Boundary closest to a line of sight.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
            Returns:
                direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class SmoothFieldOfView(AbstractFieldOfView):
    """
    public abstract class SmoothFieldOfView extends :class:`~org.orekit.geometry.fov.AbstractFieldOfView`
    
        Class representing a spacecraft sensor Field Of View with shape defined by a smooth single loop.
    
        Since:
            10.1
    """
    def getCenter(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction of the FOV center, in spacecraft frame.
        
            Returns:
                direction of the FOV center, in spacecraft frame
        
        
        """
        ...
    def getFootprint(self, transform: org.orekit.frames.Transform, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]: ...
    def getX(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the X axis defining FoV boundary.
        
            Returns:
                X axis defining FoV boundary, in spacecraft frame
        
        
        """
        ...
    def getY(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the Y axis defining FoV boundary.
        
            Returns:
                Y axis defining FoV boundary, in spacecraft frame
        
        
        """
        ...
    def getZ(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the Z axis defining FoV boundary.
        
            Returns:
                Z axis defining FoV boundary, in spacecraft frame
        
        
        """
        ...

class CircularFieldOfView(SmoothFieldOfView):
    """
    public class CircularFieldOfView extends :class:`~org.orekit.geometry.fov.SmoothFieldOfView`
    
        Class representing a spacecraft sensor Field Of View with circular shape.
    
        The field of view is defined by an axis and an half-aperture angle.
    
        Since:
            10.1
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float): ...
    def getHalfAperture(self) -> float:
        """
            get the FOV half aperture angle.
        
            Returns:
                FOV half aperture angle
        
        
        """
        ...
    def offsetFromBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, visibilityTrigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
            Get the offset of target body with respect to the Field Of View Boundary.
        
            The offset is the signed angular distance between target body and closest boundary point, taking into account
            :class:`~org.orekit.propagation.events.VisibilityTrigger` and :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin`.
        
            As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be
            outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed
            about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of
            View margin and should be designed to still return a positive value if the full accurate computation would return a
            positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate
            computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary
            crossings (taking :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin` into account), which correspond to sign changes of the offset.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
                angularRadius (double): target body angular radius
                trigger (:class:`~org.orekit.propagation.events.VisibilityTrigger`): visibility trigger for spherical bodies
        
            Returns:
                an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
                (note that this cannot take into account interposing bodies)
        
            Also see:
                :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def projectToBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the direction on Field Of View Boundary closest to a line of sight.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
            Returns:
                direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...

class DoubleDihedraFieldOfView(PolygonalFieldOfView):
    """
    public class DoubleDihedraFieldOfView extends :class:`~org.orekit.geometry.fov.PolygonalFieldOfView`
    
        Class representing a spacecraft sensor Field Of View with dihedral shape (i.e. rectangular shape).
    
        Since:
            10.1
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, double3: float): ...

class EllipticalFieldOfView(SmoothFieldOfView):
    """
    public class EllipticalFieldOfView extends :class:`~org.orekit.geometry.fov.SmoothFieldOfView`
    
        Class representing a spacecraft sensor Field Of View with elliptical shape.
    
        Without loss of generality, one can assume that with a suitable rotation the ellipse center is along the Z :sub:`ell`
        axis and the ellipse principal axes are along the X :sub:`ell` and Y :sub:`ell` axes. The first defining elements for an
        ellipse are these canonical axes. This class allows specifying them by giving directly the Z :sub:`ell` axis as the
        :code:`center` of the ellipse, and giving a :code:`primaryMeridian` vector in the (+X :sub:`ell` , Z :sub:`ell` )
        half-plane. It is allowed to have :code:`primaryMeridian` not orthogonal to :code:`center` as orthogonality will be
        fixed internally (i.e :code:`primaryMeridian` may be different from X :sub:`ell` ).
    
        We can define angular coordinates \((\alpha, \beta)\) as dihedra angles around the +Y :sub:`ell` and -X :sub:`ell` axes
        respectively to specify points on the unit sphere. The corresponding Cartesian coordinates will be
        \[P_{\alpha,\beta}\left(\begin{gather*} \frac{\sin\alpha\cos\beta}{\sqrt{1-\sin^2\alpha\sin^2\beta}}\\
        \frac{\cos\alpha\sin\beta}{\sqrt{1-\sin^2\alpha\sin^2\beta}}\\
        \frac{\cos\alpha\cos\beta}{\sqrt{1-\sin^2\alpha\sin^2\beta}} \end{gather*}\right)\] which shows that angle \(\beta=0\)
        corresponds to the (X :sub:`ell` , Z :sub:`ell` ) plane and that angle \(\alpha=0\) corresponds to the (Y :sub:`ell` , Z
        :sub:`ell` ) plane. Note that at least one of the angles must be different from \(\pm\frac{\pi}{2}\), which means that
        the expression above is singular for points in the (X :sub:`ell` , Y :sub:`ell` ) plane.
    
        The size of the ellipse is defined by its half aperture angles \(\lambda\) along the X :sub:`ell` axis and \(\mu\) along
        the Y :sub:`ell` axis. For points belonging to the ellipse, we always have \(-\lambda \le \alpha \le +\lambda\) and
        \(-\mu \le \beta \le +\mu\), equalities being reached at the end of principal axes. An ellipse defined on the sphere is
        not a planar ellipse because the four endpoints \((\alpha=\pm\lambda, \beta=0)\) and \((\alpha=0, \beta=\pm\mu)\) are
        not coplanar when \(\lambda\neq\mu\).
    
        We define an ellipse on the sphere as the locus of points \(P\) such that the sum of their angular distance to two foci
        \(F_+\) and \(F_-\) is constant, all points being on the sphere. The relationship between the foci and the two half
        aperture angles \(\lambda\) and \(\mu\) is: \[\lambda \ge \mu \Rightarrow F_\pm\left(\begin{gather*} \pm\sin\delta\\ 0\\
        \cos\delta \end{gather*}\right) \quad\text{with}\quad \cos\delta = \frac{\cos\lambda}{\cos\mu}\]
    
        and \[\mu \ge \lambda \Rightarrow F_\pm\left(\begin{gather*} 0\\ \pm\sin\delta\\ \cos\delta \end{gather*}\right)
        \quad\text{with}\quad \cos\delta = \frac{\cos\mu}{\cos\lambda}\]
    
        It can be shown that the previous definition is equivalent to define first a regular planar ellipse drawn on a plane \(z
        = z_0\) (\(z_0\) being an arbitrary strictly positive number, \(z_0=1\) being the simplest choice) with semi major axis
        \(a=z_0\tan\lambda\) and semi minor axis \(b=z_0\tan\mu\) and then to project it onto the sphere using a central
        projection: \[\left\{\begin{align*} \left(\frac{x}{z_0\tan\lambda}\right)^2 + \left(\frac{y}{z_0\tan\mu}\right)^2 &=
        \left(\frac{z}{z_0}\right)^2\\ x^2 + y^2 + z^2 &= 1 \end{align*}\right.\]
    
        Simplifying first equation by \(z_0\) and eliminating \(z^2\) in it using the second equation gives:
        \[\left\{\begin{align*} \left(\frac{x}{\sin\lambda}\right)^2 + \left(\frac{y}{\sin\mu}\right)^2 &= 1\\ x^2 + y^2 + z^2
        &= 1 \end{align*}\right.\] which shows that the previous definition is also equivalent to define first a dimensionless
        planar ellipse on the \((x, y)\) plane and to project it onto the sphere using a projection along \(z\).
    
        Note however that despite the ellipse on the sphere can be computed as a projection of an ellipse on the \((x, y)\)
        plane, the foci of one ellipse are not the projection of the foci of the other ellipse. The foci on the plane are closer
        to each other by a factor \(\cos\mu\) than the projection of the foci \(F_+\) and \(F_-\)).
    
        Since:
            10.1
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float, double3: float): ...
    def getFocus1(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get first focus in spacecraft frame.
        
            Returns:
                first focus in spacecraft frame
        
        
        """
        ...
    def getFocus2(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get second focus in spacecraft frame.
        
            Returns:
                second focus in spacecraft frame
        
        
        """
        ...
    def getHalfApertureAlongX(self) -> float:
        """
            get the FOV half aperture angle for spreading along X :sub:`ell` (i.e. rotation around +Y :sub:`ell` ).
        
            Returns:
                FOV half aperture angle for spreading along X :sub:`ell` (i.e. rotation around +Y :sub:`ell`
        
        
        """
        ...
    def getHalfApertureAlongY(self) -> float:
        """
            get the FOV half aperture angle for spreading along Y :sub:`ell` (i.e. rotation around -X :sub:`ell` ).
        
            Returns:
                FOV half aperture angle for spreading along Y :sub:`ell` (i.e. rotation around -X :sub:`ell` )
        
        
        """
        ...
    def offsetFromBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, visibilityTrigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
            Get the offset of target body with respect to the Field Of View Boundary.
        
            The offset is the signed angular distance between target body and closest boundary point, taking into account
            :class:`~org.orekit.propagation.events.VisibilityTrigger` and :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin`.
        
            As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be
            outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed
            about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of
            View margin and should be designed to still return a positive value if the full accurate computation would return a
            positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate
            computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary
            crossings (taking :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.FieldOfView.getMargin` into account), which correspond to sign changes of the offset.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
                angularRadius (double): target body angular radius
                trigger (:class:`~org.orekit.propagation.events.VisibilityTrigger`): visibility trigger for spherical bodies
        
            Returns:
                an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
                (note that this cannot take into account interposing bodies)
        
            Also see:
                :meth:`~org.orekit.geometry.fov.FieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def projectToBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the direction on Field Of View Boundary closest to a line of sight.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
            Returns:
                direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...

class PythonSmoothFieldOfView(SmoothFieldOfView):
    """
    public class PythonSmoothFieldOfView extends :class:`~org.orekit.geometry.fov.SmoothFieldOfView`
    """
    def finalize(self) -> None: ...
    def offsetFromBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, visibilityTrigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
            Get the offset of target body with respect to the Field Of View Boundary.
        
            The offset is the signed angular distance between target body and closest boundary point, taking into account
            :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.AbstractFieldOfView.getMargin`.
        
            As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be
            outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed
            about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of
            View margin and should be designed to still return a positive value if the full accurate computation would return a
            positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate
            computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary
            crossings (taking :class:`~org.orekit.propagation.events.VisibilityTrigger` and
            :meth:`~org.orekit.geometry.fov.AbstractFieldOfView.getMargin` into account), which correspond to sign changes of the
            offset.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
                angularRadius (double): target body angular radius
                trigger (:class:`~org.orekit.propagation.events.VisibilityTrigger`): visibility trigger for spherical bodies
        
            Returns:
                an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
                (note that this cannot take into account interposing bodies)
        
            Also see:
                :meth:`~org.orekit.geometry.fov.PythonSmoothFieldOfView.offsetFromBoundary`
        
        
        """
        ...
    def projectToBoundary(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the direction on Field Of View Boundary closest to a line of sight.
        
            Parameters:
                lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
            Returns:
                direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.geometry.fov")``.

    AbstractFieldOfView: typing.Type[AbstractFieldOfView]
    CircularFieldOfView: typing.Type[CircularFieldOfView]
    DoubleDihedraFieldOfView: typing.Type[DoubleDihedraFieldOfView]
    EllipticalFieldOfView: typing.Type[EllipticalFieldOfView]
    FieldOfView: typing.Type[FieldOfView]
    PolygonalFieldOfView: typing.Type[PolygonalFieldOfView]
    PythonAbstractFieldOfView: typing.Type[PythonAbstractFieldOfView]
    PythonFieldOfView: typing.Type[PythonFieldOfView]
    PythonSmoothFieldOfView: typing.Type[PythonSmoothFieldOfView]
    SmoothFieldOfView: typing.Type[SmoothFieldOfView]
