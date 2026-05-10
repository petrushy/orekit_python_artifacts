
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.euclidean.twod
import org.hipparchus.linear
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class EncounterLOF(org.orekit.frames.LOF):
    """
    Interface for encounter local orbital frame.
    
    Encounter local orbital frame are defined using two objects, one of them is placed at the origin and the other is expressed relatively to the origin.
    
    Since:
        12.0
    """
    _computeProjectionMatrix_0__T = typing.TypeVar('_computeProjectionMatrix_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeProjectionMatrix(self, field: org.hipparchus.Field[_computeProjectionMatrix_0__T]) -> org.hipparchus.linear.FieldMatrix[_computeProjectionMatrix_0__T]:
        """
        Get the 2x3 projection matrix that projects values expressed in this encounter local orbital frame to the collision plane defined by this same encounter local orbital frame.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
        
        Returns:
            2x3 projection matrix
        
        
        """
        ...
    @typing.overload
    def computeProjectionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the 2x3 projection matrix that projects values expressed in this encounter local orbital frame to the collision plane.
        
        Returns:
            2x3 projection matrix
        
        """
        ...
    _getAxisNormalToCollisionPlane_0__T = typing.TypeVar('_getAxisNormalToCollisionPlane_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAxisNormalToCollisionPlane(self, field: org.hipparchus.Field[_getAxisNormalToCollisionPlane_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAxisNormalToCollisionPlane_0__T]:
        """
        Parameters:
            field (Field<T> field): field of the elements
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def getAxisNormalToCollisionPlane(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        
        """
        ...
    _getFieldOther__T = typing.TypeVar('_getFieldOther__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldOther(self, field: org.hipparchus.Field[_getFieldOther__T]) -> org.orekit.utils.FieldPVCoordinates[_getFieldOther__T]:
        """
        Get other's position and velocity coordinates.
        
        Parameters:
            field (Field<T> field): field of the element
        
        Returns:
            other's position and velocity coordinates
        
        
        """
        ...
    def getOther(self) -> org.orekit.utils.PVCoordinates:
        """
        Get other's position and velocity coordinates.
        
        Returns:
            other's position and velocity coordinates
        
        
        """
        ...
    def isQuasiInertial(self) -> bool:
        """
        Get flag that indicates if current local orbital frame shall be treated as pseudo-inertial.
        
        Specified by: isQuasiInertial in interface LOF
        
        Returns:
            flag that indicates if current local orbital frame shall be treated as pseudo-inertial
        
        
        """
        ...
    _projectOntoCollisionPlane_0__T = typing.TypeVar('_projectOntoCollisionPlane_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _projectOntoCollisionPlane_2__T = typing.TypeVar('_projectOntoCollisionPlane_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def projectOntoCollisionPlane(self, matrix: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_projectOntoCollisionPlane_0__T]) -> org.hipparchus.geometry.euclidean.twod.FieldVector2D[_projectOntoCollisionPlane_0__T]:
        """
        Project given RealMatrix expressed in this encounter local orbital frame onto the collision plane defined by this same encounter local orbital frame.
        
        Parameters:
            matrix (FieldMatrix<T> matrix): matrix to project, a 3 by 3 matrix is expected
        
        Returns:
            projected matrix onto the collision plane defined by this encounter local orbital frame
        
        Project given Vector3D expressed in this encounter local orbital frame onto the collision plane.
        
        Parameters:
            vector (FieldVector3D<T> vector): vector to project
        
        Returns:
            projected vector onto the collision plane defined by this encounter local orbital frame
        
        
        """
        ...
    @typing.overload
    def projectOntoCollisionPlane(self, matrix: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
        Project given RealMatrix expressed in this encounter local orbital frame onto the collision plane.
        
        Parameters:
            matrix (RealMatrix): matrix to project, a 3 by 3 matrix is expected
        
        Returns:
            projected matrix onto the collision plane defined by this encounter local orbital frame
        
        Project given Vector3D expressed in this encounter local orbital frame onto the collision plane.
        
        Parameters:
            vector (Vector3D): vector to project
        
        Returns:
            projected vector onto the collision plane defined by this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def projectOntoCollisionPlane(self, fieldMatrix: org.hipparchus.linear.FieldMatrix[_projectOntoCollisionPlane_2__T]) -> org.hipparchus.linear.FieldMatrix[_projectOntoCollisionPlane_2__T]: ...
    @typing.overload
    def projectOntoCollisionPlane(self, realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.RealMatrix: ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_2__T = typing.TypeVar('_rotationFromInertial_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_3__T = typing.TypeVar('_rotationFromInertial_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], date: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T], pv: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it. It is unnecessary to use this method when dealing with EncounterLOF, use rotationFromInertial instead.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            date (FieldAbsoluteDate<T> date): date of the rotation
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            origin (FieldPVCoordinates<T> origin): position-velocity of the origin in the same inertial frame as other
            other (FieldPVCoordinates<T> other): position-velocity of the other in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, date: org.orekit.utils.PVCoordinates, pv: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it. It is unnecessary to use this method when dealing with EncounterLOF, use rotationFromInertial instead.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            date (AbsoluteDate): date of the rotation
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            origin (PVCoordinates): position-velocity of the origin in the same inertial frame as other
            other (PVCoordinates): position-velocity of the other instance in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_2__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_2__T]: ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_3__T], origin: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_3__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_3__T]:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            origin (FieldPVCoordinates<T> origin): position-velocity of the origin in the same inertial frame as the one this instance has been expressed in.
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            origin (PVCoordinates): position-velocity of the origin in some inertial frame
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...

class EncounterLOFType(java.lang.Enum['EncounterLOFType']):
    """
    Enum for encounter local orbital frame.
    
    Since:
        12.0
    """
    DEFAULT: typing.ClassVar['EncounterLOFType'] = ...
    VALSECCHI: typing.ClassVar['EncounterLOFType'] = ...
    _getFrame_0__T = typing.TypeVar('_getFrame_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFrame(self, other: org.orekit.utils.FieldPVCoordinates[_getFrame_0__T]) -> EncounterLOF: ...
    @typing.overload
    def getFrame(self, other: org.orekit.utils.PVCoordinates) -> EncounterLOF:
        """
        Get encounter local orbital frame associated to this enum.
        
        Parameters:
            other (PVCoordinates): other object PVCoordinates that is not the origin of the encounter frame
        
        Returns:
            encounter local orbital frame associated to this enum
        
        public abstract <T extends CalculusFieldElement<T>> EncounterLOF getFrame (FieldPVCoordinates<T> other)
        
        Get encounter local orbital frame associated to this enum.
        
        Parameters:
            other (FieldPVCoordinates<T> other): other object PVCoordinates that is not the origin of the encounter frame
        
        Returns:
            encounter local orbital frame associated to this enum
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'EncounterLOFType':
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
    def values() -> typing.MutableSequence['EncounterLOFType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (EncounterLOFType c : EncounterLOFType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AbstractEncounterLOF(EncounterLOF):
    """
    Abstract class for encounter frame between two objects.
    
    Since:
        12.0
    """
    _getFieldOther__T = typing.TypeVar('_getFieldOther__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldOther(self, field: org.hipparchus.Field[_getFieldOther__T]) -> org.orekit.utils.FieldPVCoordinates[_getFieldOther__T]:
        """
        Get the field version of other's position and velocity coordinates. If the instance has been created with normal PVCoordinates, then it will build its field equivalent.
        
        Specified by: getFieldOther in interface EncounterLOF
        
        Parameters:
            field (Field<T> field): field of the elements
        
        Returns:
            field version of other's position and velocity coordinates
        
        
        """
        ...
    def getOther(self) -> org.orekit.utils.PVCoordinates:
        """
        Get the normal version of other's position and velocity coordinates. If the instance has been created with field FieldPVCoordinates, then it will convert it to its PVCoordinates equivalent.
        
        Specified by: getOther in interface EncounterLOF
        
        Returns:
            normal version of other's position and velocity coordinates
        
        
        """
        ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_2__T = typing.TypeVar('_rotationFromInertial_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_4__T = typing.TypeVar('_rotationFromInertial_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T], fieldPVCoordinates2: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]: ...
    @typing.overload
    def rotationFromInertial(self, field: org.orekit.utils.PVCoordinates, origin: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_2__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_2__T]: ...
    @typing.overload
    def rotationFromInertial(self, field: org.orekit.time.AbsoluteDate, origin: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_4__T], origin: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_4__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_4__T]:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Specified by: rotationFromInertial in interface EncounterLOF
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            origin (FieldPVCoordinates<T> origin): position-velocity of the origin in the same inertial frame as the one this instance has been expressed in.
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Specified by: rotationFromInertial in interface EncounterLOF
        
        Parameters:
            origin (PVCoordinates): position-velocity of the origin in some inertial frame
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        
        """
        ...

class PythonEncounterLOF(EncounterLOF):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getAxisNormalToCollisionPlane_0__T = typing.TypeVar('_getAxisNormalToCollisionPlane_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAxisNormalToCollisionPlane(self, field: org.hipparchus.Field[_getAxisNormalToCollisionPlane_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAxisNormalToCollisionPlane_0__T]:
        """
        Description copied from interface: getAxisNormalToCollisionPlane Get the axis normal to the collision plane (i, j or k) in this encounter local orbital frame.
        
        Specified by: getAxisNormalToCollisionPlane in interface EncounterLOF
        
        Parameters:
            field (Field<T> field): field of the elements
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def getAxisNormalToCollisionPlane(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from interface: getAxisNormalToCollisionPlane Get the axis normal to the collision plane (i, j or k) in this encounter local orbital frame.
        
        Specified by: getAxisNormalToCollisionPlane in interface EncounterLOF
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        
        """
        ...
    _getFieldOther__T = typing.TypeVar('_getFieldOther__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldOther(self, field: org.hipparchus.Field[_getFieldOther__T]) -> org.orekit.utils.FieldPVCoordinates[_getFieldOther__T]:
        """
        Description copied from interface: getFieldOther Get other's position and velocity coordinates.
        
        Specified by: getFieldOther in interface EncounterLOF
        
        Parameters:
            field (Field<T> field): field of the element
        
        Returns:
            other's position and velocity coordinates
        
        
        """
        ...
    def getName(self) -> str:
        """
        Description copied from interface: getName Get name of the local orbital frame.
        
        Specified by: getName in interface LOF
        
        Returns:
            name of the local orbital frame
        
        
        """
        ...
    def getOther(self) -> org.orekit.utils.PVCoordinates:
        """
        Description copied from interface: getOther Get other's position and velocity coordinates.
        
        Specified by: getOther in interface EncounterLOF
        
        Returns:
            other's position and velocity coordinates
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_1__T = typing.TypeVar('_rotationFromInertial_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_4__T = typing.TypeVar('_rotationFromInertial_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], origin: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_0__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Description copied from interface: rotationFromInertial Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Specified by: rotationFromInertial in interface EncounterLOF
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            origin (FieldPVCoordinates<T> origin): position-velocity of the origin in the same inertial frame as other
            other (FieldPVCoordinates<T> other): position-velocity of the other in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, origin: org.hipparchus.Field[_rotationFromInertial_1__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_1__T]: ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.time.AbsoluteDate, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Description copied from interface: rotationFromInertial Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Specified by: rotationFromInertial in interface EncounterLOF
        
        Parameters:
            origin (PVCoordinates): position-velocity of the origin in the same inertial frame as other
            other (PVCoordinates): position-velocity of the other instance in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_4__T], origin: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_4__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_4__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_4__T]: ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.utils.PVCoordinates, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...

class DefaultEncounterLOF(AbstractEncounterLOF):
    """
    Default encounter local orbital frame.
    
    Note that it is up to the user to choose which object should be at the origin.
    
    It is defined as follows :
    
      - z axis : Normalized relative velocity vector.
      - y axis : Normalized cross product between z axis and other relative to origin position.
      - x axis : Completes the right handed coordinate system.
    
    
    Since:
        12.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, other: org.orekit.utils.FieldPVCoordinates[___init___0__T]): ...
    @typing.overload
    def __init__(self, other: org.orekit.utils.PVCoordinates): ...
    _getAxisNormalToCollisionPlane_0__T = typing.TypeVar('_getAxisNormalToCollisionPlane_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAxisNormalToCollisionPlane(self, field: org.hipparchus.Field[_getAxisNormalToCollisionPlane_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAxisNormalToCollisionPlane_0__T]:
        """
        In this case, return (0,0,1);
        
        Parameters:
            field (Field<T> field): field of the elements
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def getAxisNormalToCollisionPlane(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        In this case, return (0,0,1);
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get name of the local orbital frame.
        
        Returns:
            name of the local orbital frame
        
        
        """
        ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_2__T = typing.TypeVar('_rotationFromInertial_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_3__T = typing.TypeVar('_rotationFromInertial_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], origin: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_0__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            origin (FieldPVCoordinates<T> origin): position-velocity of the origin in the same inertial frame as other
            other (FieldPVCoordinates<T> other): position-velocity of the other in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.time.AbsoluteDate, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            origin (PVCoordinates): position-velocity of the origin in the same inertial frame as other
            other (PVCoordinates): position-velocity of the other instance in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, origin: org.hipparchus.Field[_rotationFromInertial_2__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_2__T]: ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_3__T], origin: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_3__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_3__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_3__T]: ...
    @typing.overload
    def rotationFromInertial(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.utils.PVCoordinates, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...

class PythonAbstractEncounterLOF(AbstractEncounterLOF):
    def __init__(self, other: org.orekit.utils.PVCoordinates): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getAxisNormalToCollisionPlane_0__T = typing.TypeVar('_getAxisNormalToCollisionPlane_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAxisNormalToCollisionPlane(self, field: org.hipparchus.Field[_getAxisNormalToCollisionPlane_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAxisNormalToCollisionPlane_0__T]:
        """
        Parameters:
            field (Field<T> field): field of the elements
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def getAxisNormalToCollisionPlane(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get name of the local orbital frame.
        
        Returns:
            name of the local orbital frame
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_2__T = typing.TypeVar('_rotationFromInertial_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_4__T = typing.TypeVar('_rotationFromInertial_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], origin: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_0__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            origin (FieldPVCoordinates<T> origin): position-velocity of the origin in the same inertial frame as other
            other (FieldPVCoordinates<T> other): position-velocity of the other in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.time.AbsoluteDate, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            origin (PVCoordinates): position-velocity of the origin in the same inertial frame as other
            other (PVCoordinates): position-velocity of the other instance in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_2__T], origin: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_2__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_2__T]: ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.utils.PVCoordinates, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromInertial(self, origin: org.hipparchus.Field[_rotationFromInertial_4__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_4__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_4__T]: ...
    @typing.overload
    def rotationFromInertial(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...

class ValsecchiEncounterFrame(AbstractEncounterLOF):
    """
    Valsecchi encounter local orbital frame based on Valsecchi formulation from : "Valsecchi, G. B., Milani, A., Gronchi, G. F. & Ches- ley, S. R. Resonant returns to close approaches: Analytical theory. Astronomy & Astrophysics 408, 1179–1196 (2003).".
    
    Note that it is up to the user to choose which object should be at the origin.
    
    Since:
        12.0
    """
    ___init___0__T = typing.TypeVar('___init___0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def __init__(self, other: org.orekit.utils.FieldPVCoordinates[___init___0__T]): ...
    @typing.overload
    def __init__(self, other: org.orekit.utils.PVCoordinates): ...
    _getAxisNormalToCollisionPlane_0__T = typing.TypeVar('_getAxisNormalToCollisionPlane_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAxisNormalToCollisionPlane(self, field: org.hipparchus.Field[_getAxisNormalToCollisionPlane_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAxisNormalToCollisionPlane_0__T]:
        """
        In this case, return (0,1,0);
        
        Parameters:
            field (Field<T> field): field of the elements
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def getAxisNormalToCollisionPlane(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        In this case, return (0,1,0);
        
        Returns:
            axis normal to the collision plane (i, j or k) in this encounter local orbital frame
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get name of the local orbital frame.
        
        Returns:
            name of the local orbital frame
        
        
        """
        ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_2__T = typing.TypeVar('_rotationFromInertial_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_3__T = typing.TypeVar('_rotationFromInertial_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], origin: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_0__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            origin (FieldPVCoordinates<T> origin): position-velocity of the origin in the same inertial frame as other
            other (FieldPVCoordinates<T> other): position-velocity of the other in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.time.AbsoluteDate, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial to this encounter local orbital frame.
        
        BEWARE: The given origin's position and velocity coordinates must be given in the frame in which this instance has been expressed in.
        
        Parameters:
            origin (PVCoordinates): position-velocity of the origin in the same inertial frame as other
            other (PVCoordinates): position-velocity of the other instance in the same inertial frame as origin
        
        Returns:
            rotation from inertial to this encounter local orbital frame
        
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, origin: org.hipparchus.Field[_rotationFromInertial_2__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_2__T]: ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_3__T], origin: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_3__T], other: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_3__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_3__T]: ...
    @typing.overload
    def rotationFromInertial(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromInertial(self, origin: org.orekit.utils.PVCoordinates, other: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.frames.encounter")``.

    AbstractEncounterLOF: typing.Type[AbstractEncounterLOF]
    DefaultEncounterLOF: typing.Type[DefaultEncounterLOF]
    EncounterLOF: typing.Type[EncounterLOF]
    EncounterLOFType: typing.Type[EncounterLOFType]
    PythonAbstractEncounterLOF: typing.Type[PythonAbstractEncounterLOF]
    PythonEncounterLOF: typing.Type[PythonEncounterLOF]
    ValsecchiEncounterFrame: typing.Type[ValsecchiEncounterFrame]
