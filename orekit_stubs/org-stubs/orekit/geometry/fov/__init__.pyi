
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

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
    Interface representing a spacecraft sensor Field Of View.
    
    Fields Of View are zones defined on the unit sphere centered on the spacecraft. Different implementations may use specific modeling depending on the shape.
    
    Since:
        10.1
    """
    def getFootprint(self, fovToBody: org.orekit.frames.Transform, body: org.orekit.bodies.OneAxisEllipsoid, angularStep: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]:
        """
        Get the footprint of the Field Of View on ground.
        
        This method assumes the Field Of View is centered on some carrier, which will typically be a spacecraft or a ground station antenna. The points in the footprint boundary loops are all at altitude zero with respect to the ellipsoid, they correspond either to projection on ground of the edges of the Field Of View, or to points on the body limb if the Field Of View goes past horizon. The points on the limb see the carrier origin at zero elevation. If the Field Of View is so large it contains entirely the body, all points will correspond to points at limb. If the Field Of View looks away from body, the boundary loops will be an empty list. The points within footprint loops are sorted in trigonometric order as seen from the carrier. This implies that someone traveling on ground from one point to the next one will have the points visible from the carrier on his left hand side, and the points not visible from the carrier on his right hand side.
        
        The truncation of Field Of View at limb can induce strange results for complex Fields Of View. If for example a Field Of View is a ring with a hole and part of the ring goes past horizon, then instead of having a single loop with a C-shaped boundary, the method will still return two loops truncated at the limb, one clockwise and one counterclockwise, hence "closing" the C-shape twice. This behavior is considered acceptable.
        
        If the carrier is a spacecraft, then the fovToBody transform can be computed from a SpacecraftState as follows:
        
        
         Transform inertToBody = state.getFrame().getTransformTo(body.getBodyFrame(), state.getDate());
         Transform fovToBody   = new Transform(state.getDate(),
                                               state.toTransform().getInverse(),
                                               inertToBody);
         
        
        If the carrier is a ground station, located using a topocentric frame and managing its pointing direction using a transform between the dish frame and the topocentric frame, then the fovToBody transform can be computed as follows:
        
        
         Transform topoToBody = topocentricFrame.getTransformTo(body.getBodyFrame(), date);
         Transform topoToDish = ...
         Transform fovToBody  = new Transform(date,
                                              topoToDish.getInverse(),
                                              topoToBody);
         
        
        Only the raw zone is used, the angular margin is ignored here.
        
        Parameters:
            fovToBody (Transform): transform between the frame in which the Field Of View is defined and body frame.
            body (OneAxisEllipsoid): body surface the Field Of View will be projected on
            angularStep (double): step used for boundary loops sampling (radians), beware this is generally not an angle on the unit sphere, but rather
                a phase angle used by the underlying Field Of View boundary model
        
        Returns:
            list footprint boundary loops (there may be several independent loops if the Field Of View shape is complex)
        
        
        """
        ...
    def getMargin(self) -> float:
        """
        Get the angular margin to apply (radians). If angular margin is positive, points outside of the raw FoV but close enough to the boundary are considered visible. If angular margin is negative, points inside of the raw FoV but close enough to the boundary are considered not visible
        
        Returns:
            angular margin
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def offsetFromBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D, angularRadius: float, trigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
        Get the offset of target body with respect to the Field Of View Boundary.
        
        The offset is the signed angular distance between target body and closest boundary point, taking into account VisibilityTrigger and getMargin.
        
        As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of View margin and should be designed to still return a positive value if the full accurate computation would return a positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary crossings (taking VisibilityTrigger and getMargin into account), which correspond to sign changes of the offset.
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
            angularRadius (double): target body angular radius
            trigger (VisibilityTrigger): visibility trigger for spherical bodies
        
        Returns:
            an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
            (note that this cannot take into account interposing bodies)
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def projectToBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    Abstract class representing a spacecraft sensor Field Of View.
    
    Since:
        10.1
    """
    def getMargin(self) -> float:
        """
        Get the angular margin to apply (radians). If angular margin is positive, points outside of the raw FoV but close enough to the boundary are considered visible. If angular margin is negative, points inside of the raw FoV but close enough to the boundary are considered not visible
        
        Specified by: getMargin in interface FieldOfView
        
        Returns:
            angular margin
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...

class PythonFieldOfView(FieldOfView):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFootprint(self, fovToBody: org.orekit.frames.Transform, body: org.orekit.bodies.OneAxisEllipsoid, angularStep: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]:
        """
        Get the footprint of the Field Of View on ground.
        
        This method assumes the Field Of View is centered on some carrier, which will typically be a spacecraft or a ground station antenna. The points in the footprint boundary loops are all at altitude zero with respect to the ellipsoid, they correspond either to projection on ground of the edges of the Field Of View, or to points on the body limb if the Field Of View goes past horizon. The points on the limb see the carrier origin at zero elevation. If the Field Of View is so large it contains entirely the body, all points will correspond to points at limb. If the Field Of View looks away from body, the boundary loops will be an empty list. The points within footprint loops are sorted in trigonometric order as seen from the carrier. This implies that someone traveling on ground from one point to the next one will have the points visible from the carrier on his left hand side, and the points not visible from the carrier on his right hand side.
        
        The truncation of Field Of View at limb can induce strange results for complex Fields Of View. If for example a Field Of View is a ring with a hole and part of the ring goes past horizon, then instead of having a single loop with a C-shaped boundary, the method will still return two loops truncated at the limb, one clockwise and one counterclockwise, hence "closing" the C-shape twice. This behavior is considered acceptable.
        
        If the carrier is a spacecraft, then the fovToBody transform can be computed from a SpacecraftState as follows:
        
        
         Transform inertToBody = state.getFrame().getTransformTo(body.getBodyFrame(), state.getDate());
         Transform fovToBody   = new Transform(state.getDate(),
                                               state.toTransform().getInverse(),
                                               inertToBody);
         
        
        If the carrier is a ground station, located using a topocentric frame and managing its pointing direction using a transform between the dish frame and the topocentric frame, then the fovToBody transform can be computed as follows:
        
        
         Transform topoToBody = topocentricFrame.getTransformTo(body.getBodyFrame(), date);
         Transform topoToDish = ...
         Transform fovToBody  = new Transform(date,
                                              topoToDish.getInverse(),
                                              topoToBody);
         
        
        Only the raw zone is used, the angular margin is ignored here.
        
        Specified by: getFootprint in interface FieldOfView
        
        Parameters:
            fovToBody (Transform): transform between the frame in which the Field Of View is defined and body frame.
            body (OneAxisEllipsoid): body surface the Field Of View will be projected on
            angularStep (double): step used for boundary loops sampling (radians), beware this is generally not an angle on the unit sphere, but rather
                a phase angle used by the underlying Field Of View boundary model
        
        Returns:
            list footprint boundary loops (there may be several independent loops if the Field Of View shape is complex)
        
        
        """
        ...
    def getMargin(self) -> float:
        """
        Get the angular margin to apply (radians). If angular margin is positive, points outside of the raw FoV but close enough to the boundary are considered visible. If angular margin is negative, points inside of the raw FoV but close enough to the boundary are considered not visible
        
        Specified by: getMargin in interface FieldOfView
        
        Returns:
            angular margin
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def offsetFromBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D, angularRadius: float, trigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
        Get the offset of target body with respect to the Field Of View Boundary.
        
        The offset is the signed angular distance between target body and closest boundary point, taking into account VisibilityTrigger and getMargin.
        
        As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of View margin and should be designed to still return a positive value if the full accurate computation would return a positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary crossings (taking VisibilityTrigger and getMargin into account), which correspond to sign changes of the offset.
        
        Specified by: offsetFromBoundary in interface FieldOfView
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
            angularRadius (double): target body angular radius
            trigger (VisibilityTrigger): visibility trigger for spherical bodies
        
        Returns:
            an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
            (note that this cannot take into account interposing bodies)
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def projectToBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Find the direction on Field Of View Boundary closest to a line of sight.
        
        Specified by: projectToBoundary in interface FieldOfView
        
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
    Class representing a spacecraft sensor Field Of View with polygonal shape.
    
    Fields Of View are zones defined on the unit sphere centered on the spacecraft. They can have any shape, they can be split in several non-connected patches and can have holes.
    
    Since:
        10.1
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, definingConeType: 'PolygonalFieldOfView.DefiningConeType', vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, int: int, double2: float): ...
    @typing.overload
    def __init__(self, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, double: float): ...
    def getFootprint(self, fovToBody: org.orekit.frames.Transform, body: org.orekit.bodies.OneAxisEllipsoid, angularStep: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]:
        """
        Get the footprint of the Field Of View on ground.
        
        This method assumes the Field Of View is centered on some carrier, which will typically be a spacecraft or a ground station antenna. The points in the footprint boundary loops are all at altitude zero with respect to the ellipsoid, they correspond either to projection on ground of the edges of the Field Of View, or to points on the body limb if the Field Of View goes past horizon. The points on the limb see the carrier origin at zero elevation. If the Field Of View is so large it contains entirely the body, all points will correspond to points at limb. If the Field Of View looks away from body, the boundary loops will be an empty list. The points within footprint loops are sorted in trigonometric order as seen from the carrier. This implies that someone traveling on ground from one point to the next one will have the points visible from the carrier on his left hand side, and the points not visible from the carrier on his right hand side.
        
        The truncation of Field Of View at limb can induce strange results for complex Fields Of View. If for example a Field Of View is a ring with a hole and part of the ring goes past horizon, then instead of having a single loop with a C-shaped boundary, the method will still return two loops truncated at the limb, one clockwise and one counterclockwise, hence "closing" the C-shape twice. This behavior is considered acceptable.
        
        If the carrier is a spacecraft, then the fovToBody transform can be computed from a SpacecraftState as follows:
        
        
         Transform inertToBody = state.getFrame().getTransformTo(body.getBodyFrame(), state.getDate());
         Transform fovToBody   = new Transform(state.getDate(),
                                               state.toTransform().getInverse(),
                                               inertToBody);
         
        
        If the carrier is a ground station, located using a topocentric frame and managing its pointing direction using a transform between the dish frame and the topocentric frame, then the fovToBody transform can be computed as follows:
        
        
         Transform topoToBody = topocentricFrame.getTransformTo(body.getBodyFrame(), date);
         Transform topoToDish = ...
         Transform fovToBody  = new Transform(date,
                                              topoToDish.getInverse(),
                                              topoToBody);
         
        
        Only the raw zone is used, the angular margin is ignored here.
        
        Parameters:
            fovToBody (Transform): transform between the frame in which the Field Of View is defined and body frame.
            body (OneAxisEllipsoid): body surface the Field Of View will be projected on
            angularStep (double): step used for boundary loops sampling (radians), beware this is generally not an angle on the unit sphere, but rather
                a phase angle used by the underlying Field Of View boundary model
        
        Returns:
            list footprint boundary loops (there may be several independent loops if the Field Of View shape is complex)
        
        
        """
        ...
    def getZone(self) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet:
        """
        Get the interior zone.
        
        Returns:
            the interior zone
        
        
        """
        ...
    def offsetFromBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D, angularRadius: float, trigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
        Get the offset of target body with respect to the Field Of View Boundary.
        
        The offset is the signed angular distance between target body and closest boundary point, taking into account VisibilityTrigger and getMargin.
        
        As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of View margin and should be designed to still return a positive value if the full accurate computation would return a positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary crossings (taking VisibilityTrigger and getMargin into account), which correspond to sign changes of the offset.
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
            angularRadius (double): target body angular radius
            trigger (VisibilityTrigger): visibility trigger for spherical bodies
        
        Returns:
            an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
            (note that this cannot take into account interposing bodies)
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def projectToBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
        def values() -> typing.MutableSequence['PolygonalFieldOfView.DefiningConeType']: ...

class PythonAbstractFieldOfView(AbstractFieldOfView):
    def __init__(self, margin: float):
        """
        Build a new instance.
        
        Parameters:
            margin (double): angular margin to apply to the zone (if positive, points outside of the raw FoV but close enough to the boundary are
                considered visible; if negative, points inside of the raw FoV but close enough to the boundary are considered not
                visible)
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFootprint(self, fovToBody: org.orekit.frames.Transform, body: org.orekit.bodies.OneAxisEllipsoid, angularStep: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]:
        """
        Get the footprint of the Field Of View on ground.
        
        This method assumes the Field Of View is centered on some carrier, which will typically be a spacecraft or a ground station antenna. The points in the footprint boundary loops are all at altitude zero with respect to the ellipsoid, they correspond either to projection on ground of the edges of the Field Of View, or to points on the body limb if the Field Of View goes past horizon. The points on the limb see the carrier origin at zero elevation. If the Field Of View is so large it contains entirely the body, all points will correspond to points at limb. If the Field Of View looks away from body, the boundary loops will be an empty list. The points within footprint loops are sorted in trigonometric order as seen from the carrier. This implies that someone traveling on ground from one point to the next one will have the points visible from the carrier on his left hand side, and the points not visible from the carrier on his right hand side.
        
        The truncation of Field Of View at limb can induce strange results for complex Fields Of View. If for example a Field Of View is a ring with a hole and part of the ring goes past horizon, then instead of having a single loop with a C-shaped boundary, the method will still return two loops truncated at the limb, one clockwise and one counterclockwise, hence "closing" the C-shape twice. This behavior is considered acceptable.
        
        If the carrier is a spacecraft, then the fovToBody transform can be computed from a SpacecraftState as follows:
        
        
         Transform inertToBody = state.getFrame().getTransformTo(body.getBodyFrame(), state.getDate());
         Transform fovToBody   = new Transform(state.getDate(),
                                               state.toTransform().getInverse(),
                                               inertToBody);
         
        
        If the carrier is a ground station, located using a topocentric frame and managing its pointing direction using a transform between the dish frame and the topocentric frame, then the fovToBody transform can be computed as follows:
        
        
         Transform topoToBody = topocentricFrame.getTransformTo(body.getBodyFrame(), date);
         Transform topoToDish = ...
         Transform fovToBody  = new Transform(date,
                                              topoToDish.getInverse(),
                                              topoToBody);
         
        
        Only the raw zone is used, the angular margin is ignored here.
        
        Parameters:
            fovToBody (Transform): transform between the frame in which the Field Of View is defined and body frame.
            body (OneAxisEllipsoid): body surface the Field Of View will be projected on
            angularStep (double): step used for boundary loops sampling (radians), beware this is generally not an angle on the unit sphere, but rather
                a phase angle used by the underlying Field Of View boundary model
        
        Returns:
            list footprint boundary loops (there may be several independent loops if the Field Of View shape is complex)
        
        
        """
        ...
    def offsetFromBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D, angularRadius: float, trigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
        Get the offset of target body with respect to the Field Of View Boundary.
        
        The offset is the signed angular distance between target body and closest boundary point, taking into account VisibilityTrigger and getMargin.
        
        As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of View margin and should be designed to still return a positive value if the full accurate computation would return a positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary crossings (taking VisibilityTrigger and getMargin into account), which correspond to sign changes of the offset.
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
            angularRadius (double): target body angular radius
            trigger (VisibilityTrigger): visibility trigger for spherical bodies
        
        Returns:
            an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
            (note that this cannot take into account interposing bodies)
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def projectToBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    def getFootprint(self, fovToBody: org.orekit.frames.Transform, body: org.orekit.bodies.OneAxisEllipsoid, angularStep: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]:
        """
        Get the footprint of the Field Of View on ground.
        
        This method assumes the Field Of View is centered on some carrier, which will typically be a spacecraft or a ground station antenna. The points in the footprint boundary loops are all at altitude zero with respect to the ellipsoid, they correspond either to projection on ground of the edges of the Field Of View, or to points on the body limb if the Field Of View goes past horizon. The points on the limb see the carrier origin at zero elevation. If the Field Of View is so large it contains entirely the body, all points will correspond to points at limb. If the Field Of View looks away from body, the boundary loops will be an empty list. The points within footprint loops are sorted in trigonometric order as seen from the carrier. This implies that someone traveling on ground from one point to the next one will have the points visible from the carrier on his left hand side, and the points not visible from the carrier on his right hand side.
        
        The truncation of Field Of View at limb can induce strange results for complex Fields Of View. If for example a Field Of View is a ring with a hole and part of the ring goes past horizon, then instead of having a single loop with a C-shaped boundary, the method will still return two loops truncated at the limb, one clockwise and one counterclockwise, hence "closing" the C-shape twice. This behavior is considered acceptable.
        
        If the carrier is a spacecraft, then the fovToBody transform can be computed from a SpacecraftState as follows:
        
        
         Transform inertToBody = state.getFrame().getTransformTo(body.getBodyFrame(), state.getDate());
         Transform fovToBody   = new Transform(state.getDate(),
                                               state.toTransform().getInverse(),
                                               inertToBody);
         
        
        If the carrier is a ground station, located using a topocentric frame and managing its pointing direction using a transform between the dish frame and the topocentric frame, then the fovToBody transform can be computed as follows:
        
        
         Transform topoToBody = topocentricFrame.getTransformTo(body.getBodyFrame(), date);
         Transform topoToDish = ...
         Transform fovToBody  = new Transform(date,
                                              topoToDish.getInverse(),
                                              topoToBody);
         
        
        Only the raw zone is used, the angular margin is ignored here.
        
        Parameters:
            fovToBody (Transform): transform between the frame in which the Field Of View is defined and body frame.
            body (OneAxisEllipsoid): body surface the Field Of View will be projected on
            angularStep (double): step used for boundary loops sampling (radians), beware this is generally not an angle on the unit sphere, but rather
                a phase angle used by the underlying Field Of View boundary model
        
        Returns:
            list footprint boundary loops (there may be several independent loops if the Field Of View shape is complex)
        
        
        """
        ...
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
    Class representing a spacecraft sensor Field Of View with circular shape.
    
    The field of view is defined by an axis and an half-aperture angle.
    
    Since:
        10.1
    """
    def __init__(self, center: org.hipparchus.geometry.euclidean.threed.Vector3D, halfAperture: float, margin: float):
        """
        Build a new instance.
        
        Parameters:
            center (Vector3D): direction of the FOV center, in spacecraft frame
            halfAperture (double): FOV half aperture angle
            margin (double): angular margin to apply to the zone (if positive, the Field Of View will consider points slightly outside of the zone
                are still visible)
        
        
        """
        ...
    def getHalfAperture(self) -> float:
        """
        get the FOV half aperture angle.
        
        Returns:
            FOV half aperture angle
        
        
        """
        ...
    def offsetFromBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D, angularRadius: float, trigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
        Get the offset of target body with respect to the Field Of View Boundary.
        
        The offset is the signed angular distance between target body and closest boundary point, taking into account VisibilityTrigger and getMargin.
        
        As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of View margin and should be designed to still return a positive value if the full accurate computation would return a positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary crossings (taking VisibilityTrigger and getMargin into account), which correspond to sign changes of the offset.
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
            angularRadius (double): target body angular radius
            trigger (VisibilityTrigger): visibility trigger for spherical bodies
        
        Returns:
            an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
            (note that this cannot take into account interposing bodies)
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def projectToBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    Class representing a spacecraft sensor Field Of View with dihedral shape (i.e. rectangular shape).
    
    Since:
        10.1
    """
    def __init__(self, center: org.hipparchus.geometry.euclidean.threed.Vector3D, axis1: org.hipparchus.geometry.euclidean.threed.Vector3D, halfAperture1: float, axis2: org.hipparchus.geometry.euclidean.threed.Vector3D, halfAperture2: float, margin: float):
        """
        Build a Field Of View with dihedral shape (i.e. rectangular shape).
        
        Parameters:
            center (Vector3D): Direction of the FOV center, in spacecraft frame
            axis1 (Vector3D): FOV dihedral axis 1, in spacecraft frame
            halfAperture1 (double): FOV dihedral half aperture angle 1, must be less than π/2, i.e. full dihedra must be smaller then an hemisphere
            axis2 (Vector3D): FOV dihedral axis 2, in spacecraft frame
            halfAperture2 (double): FOV dihedral half aperture angle 2, must be less than π/2, i.e. full dihedra must be smaller then an hemisphere
            margin (double): angular margin to apply to the zone (if positive, points outside of the raw FoV but close enough to the boundary are
                considered visible; if negative, points inside of the raw FoV but close enough to the boundary are considered not
                visible)
        
        
        """
        ...

class EllipticalFieldOfView(SmoothFieldOfView):
    """
    Class representing a spacecraft sensor Field Of View with elliptical shape.
    
    Without loss of generality, one can assume that with a suitable rotation the ellipse center is along the Z :sub:`ell` axis and the ellipse principal axes are along the X :sub:`ell` and Y :sub:`ell` axes. The first defining elements for an ellipse are these canonical axes. This class allows specifying them by giving directly the Z :sub:`ell` axis as the center of the ellipse, and giving a primaryMeridian vector in the (+X :sub:`ell` , Z :sub:`ell` ) half-plane. It is allowed to have primaryMeridian not orthogonal to center as orthogonality will be fixed internally (i.e primaryMeridian may be different from X :sub:`ell` ).
    
    We can define angular coordinates \((\alpha, \beta)\) as dihedra angles around the +Y :sub:`ell` and -X :sub:`ell` axes respectively to specify points on the unit sphere. The corresponding Cartesian coordinates will be \[P_{\alpha,\beta}\left(\begin{gather} \frac{\sin\alpha\cos\beta}{\sqrt{1-\sin^2\alpha\sin^2\beta}}\\ \frac{\cos\alpha\sin\beta}{\sqrt{1-\sin^2\alpha\sin^2\beta}}\\ \frac{\cos\alpha\cos\beta}{\sqrt{1-\sin^2\alpha\sin^2\beta}} \end{gather}\right)\] which shows that angle \(\beta=0\) corresponds to the (X :sub:`ell` , Z :sub:`ell` ) plane and that angle \(\alpha=0\) corresponds to the (Y :sub:`ell` , Z :sub:`ell` ) plane. Note that at least one of the angles must be different from \(\pm\frac{\pi}{2}\), which means that the expression above is singular for points in the (X :sub:`ell` , Y :sub:`ell` ) plane.
    
    The size of the ellipse is defined by its half aperture angles \(\lambda\) along the X :sub:`ell` axis and \(\mu\) along the Y :sub:`ell` axis. For points belonging to the ellipse, we always have \(-\lambda \le \alpha \le +\lambda\) and \(-\mu \le \beta \le +\mu\), equalities being reached at the end of principal axes. An ellipse defined on the sphere is not a planar ellipse because the four endpoints \((\alpha=\pm\lambda, \beta=0)\) and \((\alpha=0, \beta=\pm\mu)\) are not coplanar when \(\lambda\neq\mu\).
    
    We define an ellipse on the sphere as the locus of points \(P\) such that the sum of their angular distance to two foci \(F_+\) and \(F_-\) is constant, all points being on the sphere. The relationship between the foci and the two half aperture angles \(\lambda\) and \(\mu\) is: \[\lambda \ge \mu \Rightarrow F_\pm\left(\begin{gather} \pm\sin\delta\\ 0\\ \cos\delta \end{gather}\right) \quad\text{with}\quad \cos\delta = \frac{\cos\lambda}{\cos\mu}\]
    
    and \[\mu \ge \lambda \Rightarrow F_\pm\left(\begin{gather} 0\\ \pm\sin\delta\\ \cos\delta \end{gather}\right) \quad\text{with}\quad \cos\delta = \frac{\cos\mu}{\cos\lambda}\]
    
    It can be shown that the previous definition is equivalent to define first a regular planar ellipse drawn on a plane \(z = z_0\) (\(z_0\) being an arbitrary strictly positive number, \(z_0=1\) being the simplest choice) with semi major axis \(a=z_0\tan\lambda\) and semi minor axis \(b=z_0\tan\mu\) and then to project it onto the sphere using a central projection: \[\left\{\begin{align} \left(\frac{x}{z_0\tan\lambda}\right)^2 + \left(\frac{y}{z_0\tan\mu}\right)^2 &= \left(\frac{z}{z_0}\right)^2\\ x^2 + y^2 + z^2 &= 1 \end{align}\right.\]
    
    Simplifying first equation by \(z_0\) and eliminating \(z^2\) in it using the second equation gives: \[\left\{\begin{align} \left(\frac{x}{\sin\lambda}\right)^2 + \left(\frac{y}{\sin\mu}\right)^2 &= 1\\ x^2 + y^2 + z^2 &= 1 \end{align}\right.\] which shows that the previous definition is also equivalent to define first a dimensionless planar ellipse on the \((x, y)\) plane and to project it onto the sphere using a projection along \(z\).
    
    Note however that despite the ellipse on the sphere can be computed as a projection of an ellipse on the \((x, y)\) plane, the foci of one ellipse are not the projection of the foci of the other ellipse. The foci on the plane are closer to each other by a factor \(\cos\mu\) than the projection of the foci \(F_+\) and \(F_-\)).
    
    Since:
        10.1
    """
    def __init__(self, center: org.hipparchus.geometry.euclidean.threed.Vector3D, primaryMeridian: org.hipparchus.geometry.euclidean.threed.Vector3D, halfApertureAlongX: float, halfApertureAlongY: float, margin: float):
        """
        Build a new instance.
        
        Using a suitable rotation, an elliptical Field Of View can be oriented such that the ellipse center is along the Z :sub:`ell` axis, one of its principal axes is in the (X :sub:`ell` , Z :sub:`ell` ) plane and the other principal axis is in the (Y :sub:`ell` , Z :sub:`ell` ) plane. Beware that the ellipse principal axis that spreads along the Y :sub:`ell` direction corresponds to a rotation around -X :sub:`ell` axis and that the ellipse principal axis that spreads along the X :sub:`ell` direction corresponds to a rotation around +Y :sub:`ell` axis. The naming convention used here is that the angles are named after the spreading axis.
        
        Parameters:
            center (Vector3D): direction of the FOV center (i.e. Z :sub:`ell` ), in spacecraft frame
            primaryMeridian (Vector3D): vector defining the (+X :sub:`ell` , Z :sub:`ell` ) half-plane (it is allowed to have primaryMeridian not
                orthogonal to center as orthogonality will be fixed internally)
            halfApertureAlongX (double): FOV half aperture angle defining the ellipse spreading along X :sub:`ell` (i.e. it corresponds to a rotation around +Y
                :sub:`ell` )
            halfApertureAlongY (double): FOV half aperture angle defining the ellipse spreading along Y :sub:`ell` (i.e. it corresponds to a rotation around -X
                :sub:`ell` )
            margin (double): angular margin to apply to the zone (if positive, the Field Of View will consider points slightly outside of the zone
                are still visible)
        
        
        """
        ...
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
    def offsetFromBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D, angularRadius: float, trigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
        Get the offset of target body with respect to the Field Of View Boundary.
        
        The offset is the signed angular distance between target body and closest boundary point, taking into account VisibilityTrigger and getMargin.
        
        As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of View margin and should be designed to still return a positive value if the full accurate computation would return a positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary crossings (taking VisibilityTrigger and getMargin into account), which correspond to sign changes of the offset.
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
            angularRadius (double): target body angular radius
            trigger (VisibilityTrigger): visibility trigger for spherical bodies
        
        Returns:
            an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
            (note that this cannot take into account interposing bodies)
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def projectToBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Find the direction on Field Of View Boundary closest to a line of sight.
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
        
        Returns:
            direction on Field Of View Boundary closest to a line of sight
        
        
        """
        ...

class PythonSmoothFieldOfView(SmoothFieldOfView):
    def __init__(self, center: org.hipparchus.geometry.euclidean.threed.Vector3D, primaryMeridian: org.hipparchus.geometry.euclidean.threed.Vector3D, margin: float):
        """
        Build a new instance.
        
        Parameters:
            center (Vector3D): direction of the FOV center (Z :sub:`smooth` ), in spacecraft frame
            primaryMeridian (Vector3D): vector defining the (+X :sub:`smooth` , Z :sub:`smooth` ) half-plane (it is allowed to have primaryMeridian not
                orthogonal to center as orthogonality will be fixed internally)
            margin (double): angular margin to apply to the zone (if positive, the Field Of View will consider points slightly outside of the
        
        
        """
        ...
    def directionAt(self, angle: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get boundary direction at angle.
        
        Specified by: directionAt in class SmoothFieldOfView
        
        Parameters:
            angle (double): phase angle of the boundary direction
        
        Returns:
            boundary direction at phase angle in spacecraft frame
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def offsetFromBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D, angularRadius: float, trigger: org.orekit.propagation.events.VisibilityTrigger) -> float:
        """
        Get the offset of target body with respect to the Field Of View Boundary.
        
        The offset is the signed angular distance between target body and closest boundary point, taking into account VisibilityTrigger and getMargin.
        
        As Field Of View can have complex shapes that may require long computation, when the target point can be proven to be outside of the Field Of View, a faster but approximate computation can be used. This approximation is only performed about 0.01 radians outside of the Field Of View augmented by the deadband defined by target body radius and Field Of View margin and should be designed to still return a positive value if the full accurate computation would return a positive value. When target point is close to the zone (and furthermore when it is inside the zone), the full accurate computation is performed. This design allows this offset to be used as a reliable way to detect Field Of View boundary crossings (taking VisibilityTrigger and getMargin into account), which correspond to sign changes of the offset.
        
        Parameters:
            lineOfSight (Vector3D): line of sight from the center of the Field Of View support unit sphere to the target in spacecraft frame
            angularRadius (double): target body angular radius
            trigger (VisibilityTrigger): visibility trigger for spherical bodies
        
        Returns:
            an offset negative if the target is visible within the Field Of View and positive if it is outside of the Field Of View
            (note that this cannot take into account interposing bodies)
        
        Also see:
            offsetFromBoundary
        
        
        """
        ...
    def projectToBoundary(self, lineOfSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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


class __module_protocol__(Protocol):
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
