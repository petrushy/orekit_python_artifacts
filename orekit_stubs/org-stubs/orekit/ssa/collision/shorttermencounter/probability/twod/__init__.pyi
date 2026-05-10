
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.hipparchus
import org.hipparchus.analysis.integration
import org.hipparchus.geometry.euclidean.twod
import org.hipparchus.linear
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm.cdm
import org.orekit.frames.encounter
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.ssa.metrics
import org.orekit.time
import org.orekit.utils
import typing



_FieldShortTermEncounter2DDefinition__T = typing.TypeVar('_FieldShortTermEncounter2DDefinition__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldShortTermEncounter2DDefinition(typing.Generic[_FieldShortTermEncounter2DDefinition__T]):
    """
    Defines the encounter between two collision object at time of closest approach assuming a short-term encounter model . It uses the given EncounterLOFType to define the encounter.
    
    Both the primary and secondary collision object can be at the reference of the encounter frame, it is up to the user to choose.
    
    The "reference" object is the object considered at the reference of the given encounter frame while the "other" object is the one not placed at the reference.
    
    For example, if the user wants the primary to be at the reference of the default encounter frame, they will have to input data in the following manner:
    
    
     final FieldShortTermEncounter2DDefinition encounter = new FieldShortTermEncounter2DDefinition<>(primaryOrbitAtTCA, primaryCovarianceAtTCA, primaryRadius, secondaryOrbitAtTCA, secondaryCovarianceAtTCA, secondaryRadius);
      
     
    However, if the user wants to put the secondary at the reference and use the
    ValsecchiEncounterFrame, they will have to type :
    
    
     final FieldShortTermEncounter2DDefinition encounter = new FieldShortTermEncounter2DDefinition<>(secondaryOrbitAtTCA, secondaryCovarianceAtTCA, secondaryRadius, primaryOrbitAtTCA, primaryCovarianceAtTCA, primaryRadius, EncounterLOFType.VALSECCHI_2003);
      
     
    Note that in the current implementation, the shape of the collision objects is assumed to be a sphere.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], referenceCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], referenceRadius: _FieldShortTermEncounter2DDefinition__T, otherAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], otherCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], otherRadius: _FieldShortTermEncounter2DDefinition__T): ...
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], referenceCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], referenceRadius: _FieldShortTermEncounter2DDefinition__T, otherAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], otherCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], otherRadius: _FieldShortTermEncounter2DDefinition__T, encounterFrameType: org.orekit.frames.encounter.EncounterLOFType, tcaTolerance: float): ...
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], referenceCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], otherAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], otherCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], combinedRadius: _FieldShortTermEncounter2DDefinition__T): ...
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], referenceCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], otherAtTCA: org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T], otherCovariance: org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T], combinedRadius: _FieldShortTermEncounter2DDefinition__T, encounterFrameType: org.orekit.frames.encounter.EncounterLOFType, tcaTolerance: float): ...
    def computeCombinedCovarianceInEncounterFrame(self) -> org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T]:
        """
        Compute the combined covariance expressed in the encounter frame.
        
        Returns:
            combined covariance expressed in the encounter frame
        
        
        """
        ...
    def computeCombinedCovarianceInReferenceTNW(self) -> org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T]:
        """
        Takes both covariance matrices (expressed in their respective RTN local orbital frame) from reference and other collision object with which this instance was created and sum them in the reference collision object TNW local orbital frame.
        
        Returns:
            combined covariance matrix expressed in the reference collision object TNW local orbital frame
        
        
        """
        ...
    def computeCoppolaEncounterDuration(self) -> _FieldShortTermEncounter2DDefinition__T:
        """
        Compute the Encounter duration (s) evaluated using Coppola's formula described in : "COPPOLA, Vincent, et al. Evaluating the short encounter assumption of the probability of collision formula. 2012."
        
        This method is to be used to check the validity of the short-term encounter model. The user is expected to compare the computed duration with the orbital period from both objects and draw its own conclusions.
        
        It uses γ = 1e-16 as the resolution of a double is nearly 1e-16 so γ smaller than that are not meaningful to compute.
        
        Returns:
            encounter duration (s) evaluated using Coppola's formula
        
        
        """
        ...
    @typing.overload
    def computeMahalanobisDistance(self) -> _FieldShortTermEncounter2DDefinition__T:
        """
        called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Uses a default zero threshold of 1e-15 for the computation of the diagonalizing of the projected covariance matrix.
        
        Returns:
            Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        """
        ...
    @typing.overload
    def computeMahalanobisDistance(self, zeroThreshold: float) -> _FieldShortTermEncounter2DDefinition__T:
        """
        called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Parameters:
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        
        """
        ...
    def computeMissDistance(self) -> _FieldShortTermEncounter2DDefinition__T:
        """
        Compute the miss distance at time of closest approach.
        
        Returns:
            miss distance
        
        
        """
        ...
    def computeOtherPositionInCollisionPlane(self) -> org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldShortTermEncounter2DDefinition__T]:
        """
        Compute the other collision object FieldVector2D projected onto the collision plane.
        
        Returns:
            other collision object position projected onto the collision plane
        
        
        """
        ...
    @typing.overload
    def computeOtherPositionInRotatedCollisionPlane(self) -> org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldShortTermEncounter2DDefinition__T]: ...
    @typing.overload
    def computeOtherPositionInRotatedCollisionPlane(self, zeroThreshold: float) -> org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldShortTermEncounter2DDefinition__T]: ...
    def computeOtherRelativeToReferencePVInReferenceInertial(self) -> org.orekit.utils.FieldPVCoordinates[_FieldShortTermEncounter2DDefinition__T]:
        """
        Compute the other collision position and velocity relative to the reference collision object. Expressed in the reference collision object inertial frame.
        
        Returns:
            other collision position and velocity relative to the reference collision object, expressed in the reference collision
            object inertial frame.
        
        
        """
        ...
    def computeProjectedAndDiagonalizedCombinedPositionalCovarianceMatrix(self) -> org.hipparchus.linear.FieldMatrix[_FieldShortTermEncounter2DDefinition__T]:
        """
        Compute the combined covariance matrix diagonalized and projected onto the collision plane.
        
        Diagonalize projected positional covariance matrix in a specific manner to have σ :sub:`xx` :sup:`2` ≤ σ :sub:`yy` :sup:`2`.
        
        Returns:
            combined covariance matrix diagonalized and projected onto the collision plane
        
        
        """
        ...
    def computeProjectedCombinedPositionalCovarianceMatrix(self) -> org.hipparchus.linear.FieldMatrix[_FieldShortTermEncounter2DDefinition__T]:
        """
        Compute the projected combined covariance matrix onto the collision plane.
        
        Returns:
            projected combined covariance matrix onto the collision plane
        
        
        """
        ...
    def computeReferenceInertialToCollisionPlaneProjectionMatrix(self) -> org.hipparchus.linear.FieldMatrix[_FieldShortTermEncounter2DDefinition__T]:
        """
        Compute the projection matrix from the reference collision object inertial frame to the collision plane.
        
        Note that this matrix will only rotate from the reference collision object inertial frame to the encounter frame and project onto the collision plane, this is only a rotation.
        
        Returns:
            projection matrix from the reference collision object inertial frame to the collision plane
        
        
        """
        ...
    _computeSquaredMahalanobisDistance_2__T = typing.TypeVar('_computeSquaredMahalanobisDistance_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeSquaredMahalanobisDistance_3__T = typing.TypeVar('_computeSquaredMahalanobisDistance_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeSquaredMahalanobisDistance(self) -> _FieldShortTermEncounter2DDefinition__T:
        """
        Compute the squared Mahalanobis distance computed with the other collision object projected onto the collision plane (commonly called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Uses a default zero threshold of 1e-15 for the computation of the diagonalizing of the projected covariance matrix.
        
        Returns:
            squared Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        """
        ...
    @typing.overload
    def computeSquaredMahalanobisDistance(self, zeroThreshold: float) -> _FieldShortTermEncounter2DDefinition__T:
        """
        Compute the squared Mahalanobis distance computed with the other collision object projected onto the collision plane (commonly called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Parameters:
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            squared Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeSquaredMahalanobisDistance(xm: _computeSquaredMahalanobisDistance_2__T, ym: _computeSquaredMahalanobisDistance_2__T, sigmaX: _computeSquaredMahalanobisDistance_2__T, sigmaY: _computeSquaredMahalanobisDistance_2__T) -> _computeSquaredMahalanobisDistance_2__T:
        """
        Compute the squared Mahalanobis distance.
        
        Parameters:
            xm (T): other collision object projected xm position onto the collision plane in the rotated encounter frame
            ym (T): other collision object projected ym position onto the collision plane in the rotated encounter frame
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
        
        Returns:
            squared Mahalanobis distance
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeSquaredMahalanobisDistance(otherPosition: org.hipparchus.geometry.euclidean.twod.FieldVector2D[_computeSquaredMahalanobisDistance_3__T], covarianceMatrix: org.hipparchus.linear.FieldMatrix[_computeSquaredMahalanobisDistance_3__T]) -> _computeSquaredMahalanobisDistance_3__T:
        """
        Compute the squared Mahalanobis distance.
        
        Parameters:
            otherPosition (FieldVector2D<T> otherPosition): other collision object projected position onto the collision plane in the rotated encounter frame
            covarianceMatrix (FieldMatrix<T> covarianceMatrix): combined covariance matrix projected onto the collision plane and diagonalized
        
        Returns:
            squared Mahalanobis distance
        
        """
        ...
    def getCombinedRadius(self) -> _FieldShortTermEncounter2DDefinition__T:
        """
        Get combined radius.
        
        Returns:
            combined radius (m)
        
        
        """
        ...
    def getEncounterFrame(self) -> org.orekit.frames.encounter.EncounterLOF:
        """
        Get encounter local orbital frame.
        
        Returns:
            encounter local orbital frame
        
        
        """
        ...
    def getOtherAtTCA(self) -> org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T]:
        """
        Get other's orbit at time of closest approach.
        
        Returns:
            other's orbit at time of closest approach
        
        
        """
        ...
    def getOtherCovariance(self) -> org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T]:
        """
        Get other's covariance.
        
        Returns:
            other's covariance
        
        
        """
        ...
    def getReferenceAtTCA(self) -> org.orekit.orbits.FieldOrbit[_FieldShortTermEncounter2DDefinition__T]:
        """
        Get reference's orbit at time of closest approach.
        
        Returns:
            reference's orbit at time of closest approach
        
        
        """
        ...
    def getReferenceCovariance(self) -> org.orekit.propagation.FieldStateCovariance[_FieldShortTermEncounter2DDefinition__T]:
        """
        Get reference's covariance.
        
        Returns:
            reference's covariance
        
        
        """
        ...
    def getTca(self) -> org.orekit.time.FieldAbsoluteDate[_FieldShortTermEncounter2DDefinition__T]:
        """
        Get the Time of Closest Approach.
        
        Commonly called TCA.
        
        Returns:
            time of closest approach
        
        
        """
        ...
    def toEncounter(self) -> 'ShortTermEncounter2DDefinition':
        """
        Get new encounter instance.
        
        Returns:
            new encounter instance
        
        
        """
        ...

class ShortTermEncounter2DDefinition:
    """
    Defines the encounter between two collision object at time of closest approach assuming a short-term encounter model . It uses the given EncounterLOFType to define the encounter.
    
    Both the primary and secondary collision object can be at the reference of the encounter frame, it is up to the user to choose.
    
    The "reference" object is the object considered at the reference of the given encounter frame while the "other" object is the one not placed at the reference.
    
    For example, if the user wants the primary to be at the reference of the default encounter frame, they will have to input data in the following manner:
    
    
     final ShortTermEncounter2DDefinition encounter = new ShortTermEncounter2DDefinition(primaryOrbitAtTCA, primaryCovariance, primaryRadius, secondaryOrbitAtTCA, secondaryCovariance, secondaryRadius);
      
     
    However, if the user wants to put the secondary at the reference and use the
    ValsecchiEncounterFrame, they will have to type :
    
    
     final ShortTermEncounter2DDefinition encounter = new ShortTermEncounter2DDefinition(secondaryOrbitAtTCA, secondaryCovariance, secondaryRadius, primaryOrbitAtTCA, primaryCovariance, primaryRadius, EncounterLOFType.VALSECCHI_2003);
      
     
    Note that in the current implementation, the shape of the collision objects is assumed to be a sphere.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.Orbit, referenceCovariance: org.orekit.propagation.StateCovariance, referenceRadius: float, otherAtTCA: org.orekit.orbits.Orbit, otherCovariance: org.orekit.propagation.StateCovariance, otherRadius: float): ...
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.Orbit, referenceCovariance: org.orekit.propagation.StateCovariance, referenceRadius: float, otherAtTCA: org.orekit.orbits.Orbit, otherCovariance: org.orekit.propagation.StateCovariance, otherRadius: float, encounterFrameType: org.orekit.frames.encounter.EncounterLOFType, tcaTolerance: float): ...
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.Orbit, referenceCovariance: org.orekit.propagation.StateCovariance, otherAtTCA: org.orekit.orbits.Orbit, otherCovariance: org.orekit.propagation.StateCovariance, combinedRadius: float): ...
    @typing.overload
    def __init__(self, referenceAtTCA: org.orekit.orbits.Orbit, referenceCovariance: org.orekit.propagation.StateCovariance, otherAtTCA: org.orekit.orbits.Orbit, otherCovariance: org.orekit.propagation.StateCovariance, combinedRadius: float, encounterFrameType: org.orekit.frames.encounter.EncounterLOFType, tcaTolerance: float): ...
    def computeCombinedCovarianceInEncounterFrame(self) -> org.orekit.propagation.StateCovariance:
        """
        Compute the combined covariance expressed in the encounter frame.
        
        Returns:
            combined covariance expressed in the encounter frame
        
        
        """
        ...
    def computeCombinedCovarianceInReferenceTNW(self) -> org.orekit.propagation.StateCovariance:
        """
        Takes both covariance matrices (expressed in their respective RTN local orbital frame) from reference and other collision object with which this instance was created and sum them in the reference collision object TNW local orbital frame.
        
        Returns:
            combined covariance matrix expressed in the reference collision object TNW local orbital frame
        
        
        """
        ...
    def computeCoppolaEncounterDuration(self) -> float:
        """
        Compute the Encounter duration (s) evaluated using Coppola's formula described in : "COPPOLA, Vincent, et al. Evaluating the short encounter assumption of the probability of collision formula. 2012."
        
        This method is to be used to check the validity of the short-term encounter model. The user is expected to compare the computed duration with the orbital period from both objects and draw its own conclusions.
        
        It uses γ = 1e-16 as the resolution of a double is nearly 1e-16 so γ smaller than that are not meaningful to compute.
        
        Returns:
            encounter duration (s) evaluated using Coppola's formula
        
        
        """
        ...
    @typing.overload
    def computeMahalanobisDistance(self) -> float:
        """
        called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Uses a default zero threshold of 1e-15 for the computation of the diagonalizing of the projected covariance matrix.
        
        Returns:
            Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        """
        ...
    @typing.overload
    def computeMahalanobisDistance(self, zeroThreshold: float) -> float:
        """
        called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Parameters:
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        
        """
        ...
    def computeMissDistance(self) -> float:
        """
        Compute the miss distance at time of closest approach.
        
        Returns:
            miss distance
        
        
        """
        ...
    def computeOtherPositionInCollisionPlane(self) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
        Compute the other collision object Vector2D projected onto the collision plane.
        
        Returns:
            other collision object position projected onto the collision plane
        
        
        """
        ...
    @typing.overload
    def computeOtherPositionInRotatedCollisionPlane(self) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
        Compute the other collision object Vector2D in the rotated collision plane.
        
        Uses a default zero threshold of 1e-15.
        
        The coordinates are often noted xm and ym in probability of collision related papers.
        
        The mentioned rotation concerns the rotation that diagonalize the combined covariance matrix inside the collision plane.
        
        Returns:
            other collision object position in the rotated collision plane
        
        """
        ...
    @typing.overload
    def computeOtherPositionInRotatedCollisionPlane(self, zeroThreshold: float) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
        Compute the other collision object Vector2D in the rotated collision plane.
        
        The coordinates are often noted xm and ym in probability of collision related papers.
        
        The mentioned rotation concerns the rotation that diagonalize the combined covariance matrix inside the collision plane.
        
        Parameters:
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            other collision object position in the rotated collision plane
        
        
        """
        ...
    def computeOtherRelativeToReferencePVInReferenceInertial(self) -> org.orekit.utils.PVCoordinates:
        """
        Compute the other collision position and velocity relative to the reference collision object. Expressed in the reference collision object inertial frame.
        
        Returns:
            other collision position and velocity relative to the reference collision object, expressed in the reference collision
            object inertial frame.
        
        
        """
        ...
    def computeProjectedAndDiagonalizedCombinedPositionalCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Compute the combined covariance matrix diagonalized and projected onto the collision plane.
        
        Diagonalize projected positional covariance matrix in a specific manner to have σ :sub:`xx` :sup:`2` ≤ σ :sub:`yy` :sup:`2`.
        
        Returns:
            combined covariance matrix diagonalized and projected onto the collision plane
        
        
        """
        ...
    def computeProjectedCombinedPositionalCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Compute the projected combined covariance matrix onto the collision plane.
        
        Returns:
            projected combined covariance matrix onto the collision plane
        
        
        """
        ...
    def computeReferenceInertialToCollisionPlaneProjectionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Compute the projection matrix from the reference collision object inertial frame to the collision plane.
        
        Note that this matrix will only rotate from the reference collision object inertial frame to the encounter frame and project onto the collision plane, this is only a rotation.
        
        Returns:
            projection matrix from the reference collision object inertial frame to the collision plane
        
        
        """
        ...
    @typing.overload
    def computeSquaredMahalanobisDistance(self) -> float:
        """
        Compute the squared Mahalanobis distance computed with the other collision object projected onto the collision plane (commonly called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Uses a default zero threshold of 1e-15 for the computation of the diagonalizing of the projected covariance matrix.
        
        Returns:
            squared Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        """
        ...
    @typing.overload
    def computeSquaredMahalanobisDistance(self, zeroThreshold: float) -> float:
        """
        Compute the squared Mahalanobis distance.
        
        Parameters:
            xm (double): other collision object projected xm position onto the collision plane in the rotated encounter frame
            ym (double): other collision object projected ym position onto the collision plane in the rotated encounter frame
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
        
        Returns:
            squared Mahalanobis distance
        
        Compute the squared Mahalanobis distance.
        
        Parameters:
            otherPosition (Vector2D): other collision object projected position onto the collision plane in the rotated encounter frame
            covarianceMatrix (RealMatrix): combined covariance matrix projected onto the collision plane and diagonalized
        
        Returns:
            squared Mahalanobis distance
        
        Compute the squared Mahalanobis distance computed with the other collision object projected onto the collision plane (commonly called B-Plane) and expressed in the rotated encounter frame (frame in which the combined covariance matrix is diagonalized, see computeEncounterPlaneRotationMatrix(double) for more details).
        
        Parameters:
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            squared Mahalanobis distance between the reference and other collision object
        
        Also see:
            Mahalanobis_distance
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeSquaredMahalanobisDistance(xm: float, ym: float, sigmaX: float, sigmaY: float) -> float: ...
    @typing.overload
    @staticmethod
    def computeSquaredMahalanobisDistance(otherPosition: org.hipparchus.geometry.euclidean.twod.Vector2D, covarianceMatrix: org.hipparchus.linear.RealMatrix) -> float: ...
    def getCombinedRadius(self) -> float:
        """
        Get combined radius.
        
        Returns:
            combined radius (m)
        
        
        """
        ...
    def getEncounterFrame(self) -> org.orekit.frames.encounter.EncounterLOF:
        """
        Get encounter local orbital frame.
        
        Returns:
            encounter local orbital frame
        
        
        """
        ...
    def getOtherAtTCA(self) -> org.orekit.orbits.Orbit:
        """
        Get other's orbit at time of closest approach.
        
        Returns:
            other's orbit at time of closest approach
        
        
        """
        ...
    def getOtherCovariance(self) -> org.orekit.propagation.StateCovariance:
        """
        Get other's covariance.
        
        Returns:
            other's covariance
        
        
        """
        ...
    def getReferenceAtTCA(self) -> org.orekit.orbits.Orbit:
        """
        Get reference's orbit at time of closest approach.
        
        Returns:
            reference's orbit at time of closest approach
        
        
        """
        ...
    def getReferenceCovariance(self) -> org.orekit.propagation.StateCovariance:
        """
        Get reference's covariance.
        
        Returns:
            reference's covariance
        
        
        """
        ...
    def getTca(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the Time of Closest Approach.
        
        Commonly called TCA.
        
        Returns:
            time of closest approach
        
        
        """
        ...

class ShortTermEncounter2DPOCMethod:
    DEFAULT_ZERO_THRESHOLD: typing.ClassVar[float] = ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_8__T = typing.TypeVar('_compute_8__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_10__T = typing.TypeVar('_compute_10__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, t: _compute_0__T, t2: _compute_0__T, t3: _compute_0__T, t4: _compute_0__T, t5: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_3__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, double: float, double2: float, double3: float, double4: float, double5: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_8__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_8__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_9__T, t2: _compute_9__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_10__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_10__T], t: _compute_10__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_10__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_10__T], t2: _compute_10__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_10__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_11__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_11__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_11__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_11__T], t: _compute_11__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_12__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def getName(self) -> str: ...
    def getType(self) -> 'ShortTermEncounter2DPOCMethodType': ...
    def isAMaximumProbabilityOfCollisionMethod(self) -> bool: ...

class ShortTermEncounter2DPOCMethodType(java.lang.Enum['ShortTermEncounter2DPOCMethodType']):
    """
    This enum stores every probability of collision computing method using the short-term encounter model available in Orekit.
    
    Since:
        12.0
    """
    LAAS_2015: typing.ClassVar['ShortTermEncounter2DPOCMethodType'] = ...
    ALFANO_2005: typing.ClassVar['ShortTermEncounter2DPOCMethodType'] = ...
    PATERA_2005: typing.ClassVar['ShortTermEncounter2DPOCMethodType'] = ...
    ALFRIEND_1999: typing.ClassVar['ShortTermEncounter2DPOCMethodType'] = ...
    ALFRIEND_1999_MAX: typing.ClassVar['ShortTermEncounter2DPOCMethodType'] = ...
    CHAN_1997: typing.ClassVar['ShortTermEncounter2DPOCMethodType'] = ...
    def getCCSDSType(self) -> org.orekit.files.ccsds.definitions.PocMethodType:
        """
        Get the CCSDS type if used by the SANA registry.
        
        Note that it may return a null if the method is not used by the SANA registry.
        
        The list of available methods is available on the SANA website.
        
        Returns:
            probability of collision method
        
        Also see:
            cdm_cpm
        
        
        """
        ...
    def getMethod(self) -> ShortTermEncounter2DPOCMethod:
        """
        Get probability of collision method.
        
        Returns:
            probability of collision method
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ShortTermEncounter2DPOCMethodType':
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
    def values() -> typing.MutableSequence['ShortTermEncounter2DPOCMethodType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ShortTermEncounter2DPOCMethodType c : ShortTermEncounter2DPOCMethodType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AbstractShortTermEncounter2DPOCMethod(ShortTermEncounter2DPOCMethod):
    DEFAULT_TCA_DIFFERENCE_TOLERANCE: typing.ClassVar[float] = ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_5__T = typing.TypeVar('_compute_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_6__T = typing.TypeVar('_compute_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_13__T = typing.TypeVar('_compute_13__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, t: _compute_0__T, t2: _compute_0__T, t3: _compute_0__T, t4: _compute_0__T, t5: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]: ...
    @typing.overload
    def compute(self, double: float, double2: float, double3: float, double4: float, double5: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_3__T, t2: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_4__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_4__T], t: _compute_4__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_4__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_4__T], t2: _compute_4__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_5__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_5__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_5__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_5__T], t: _compute_5__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_5__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_6__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_6__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_11__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_12__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_12__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_12__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_12__T], t: _compute_12__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_13__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_13__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def getName(self) -> str: ...
    def isAMaximumProbabilityOfCollisionMethod(self) -> bool: ...

class PythonShortTermEncounter2DPOCMethod(ShortTermEncounter2DPOCMethod):
    def __init__(self): ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_10__T = typing.TypeVar('_compute_10__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Description copied from interface: compute Compute the probability of collision using a Conjunction Data Message (CDM).
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            cdm (Cdm): conjunction data message input
            combinedRadius (T): combined radius (m)
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        Description copied from interface: compute Compute the probability of collision using given collision definition.
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            encounter (FieldShortTermEncounter2DDefinition<T> encounter): encounter definition between a primary and a secondary collision object
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        Description copied from interface: compute Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, combinedRadius: _compute_1__T, zeroThreshold: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, primaryAtTCA: org.orekit.orbits.FieldOrbit[_compute_2__T], primaryCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], secondaryAtTCA: _compute_2__T, secondaryCovariance: org.orekit.orbits.FieldOrbit[_compute_2__T], combinedRadius: org.orekit.propagation.FieldStateCovariance[_compute_2__T], zeroThreshold: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]:
        """
        Description copied from interface: compute Compute the probability of collision using parameters necessary for creating a ShortTermEncounter2DDefinition instance.
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            primaryAtTCA (FieldOrbit<T> primaryAtTCA): primary collision object spacecraft state at time of closest approach
            primaryCovariance (FieldStateCovariance<T> primaryCovariance): primary collision object covariance
            secondaryAtTCA (FieldOrbit<T> secondaryAtTCA): secondary collision object spacecraft state at time of closest approach
            secondaryCovariance (FieldStateCovariance<T> secondaryCovariance): secondary collision object covariance
            combinedRadius (T): combined radius (m)
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.FieldOrbit[_compute_3__T], ym: org.orekit.propagation.FieldStateCovariance[_compute_3__T], sigmaX: org.orekit.orbits.FieldOrbit[_compute_3__T], sigmaY: org.orekit.propagation.FieldStateCovariance[_compute_3__T], radius: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, combinedRadius: float, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Description copied from interface: compute Compute the probability of collision using parameters necessary for creating a ShortTermEncounter2DDefinition instance.
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            primaryAtTCA (Orbit): primary collision object spacecraft state at time of closest approach
            primaryCovariance (StateCovariance): primary collision object covariance
            secondaryAtTCA (Orbit): secondary collision object spacecraft state at time of closest approach
            secondaryCovariance (StateCovariance): secondary collision object covariance
            combinedRadius (double): combined radius (m)
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        Description copied from interface: compute Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, primaryAtTCA: org.orekit.orbits.Orbit, primaryCovariance: org.orekit.propagation.StateCovariance, secondaryAtTCA: float, secondaryCovariance: org.orekit.orbits.Orbit, combinedRadius: org.orekit.propagation.StateCovariance, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.Orbit, ym: org.orekit.propagation.StateCovariance, sigmaX: org.orekit.orbits.Orbit, sigmaY: org.orekit.propagation.StateCovariance, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Description copied from interface: compute Compute the probability of collision using a Conjunction Data Message (CDM).
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            cdm (Cdm): conjunction data message input
            combinedRadius (double): combined radius (m)
        
        Returns:
            probability of collision
        
        Description copied from interface: compute Compute the probability of collision using given collision definition.
        
        Specified by: compute in interface ShortTermEncounter2DPOCMethod
        
        Parameters:
            encounter (ShortTermEncounter2DDefinition): encounter definition between a primary and a secondary collision object
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, xm: _compute_9__T, ym: _compute_9__T, sigmaX: _compute_9__T, sigmaY: _compute_9__T, radius: _compute_9__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, combinedRadius: _compute_10__T, zeroThreshold: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_10__T]: ...
    @typing.overload
    def compute(self, primaryAtTCA: org.orekit.orbits.FieldOrbit[_compute_11__T], primaryCovariance: org.orekit.propagation.FieldStateCovariance[_compute_11__T], secondaryAtTCA: org.orekit.orbits.FieldOrbit[_compute_11__T], secondaryCovariance: org.orekit.propagation.FieldStateCovariance[_compute_11__T], combinedRadius: _compute_11__T, zeroThreshold: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_12__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, primaryAtTCA: org.orekit.orbits.Orbit, primaryCovariance: org.orekit.propagation.StateCovariance, secondaryAtTCA: org.orekit.orbits.Orbit, secondaryCovariance: org.orekit.propagation.StateCovariance, combinedRadius: float, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getName(self) -> str:
        """
        Description copied from interface: getName Get name of the method.
        
        Specified by: getName in interface ShortTermEncounter2DPOCMethod
        
        Returns:
            name of the method
        
        
        """
        ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Description copied from interface: getType Get type of the method.
        
        Specified by: getType in interface ShortTermEncounter2DPOCMethod
        
        Returns:
            type of the method
        
        
        """
        ...
    def isAMaximumProbabilityOfCollisionMethod(self) -> bool:
        """
        Description copied from interface: isAMaximumProbabilityOfCollisionMethod Get flag that defines if the method is a maximum probability of collision computing method.
        
        Specified by: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.ShortTermEncounter2DPOCMethod.isAMaximumProbabilityOfCollisionMethod` in interface ShortTermEncounter2DPOCMethod
        
        Returns:
            flag that defines if the method is a maximum probability of collision computing method
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class AbstractAlfriend1999(AbstractShortTermEncounter2DPOCMethod):
    """
    Abstract class for Alfriend1999 normal and maximised methods as they share lots of similarities.
    
    Since:
        12.0
    """
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_10__T = typing.TypeVar('_compute_10__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, t2: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t2: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.FieldOrbit[_compute_3__T], ym: org.orekit.propagation.FieldStateCovariance[_compute_3__T], sigmaX: org.orekit.orbits.FieldOrbit[_compute_3__T], sigmaY: org.orekit.propagation.FieldStateCovariance[_compute_3__T], radius: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.Orbit, ym: org.orekit.propagation.StateCovariance, sigmaX: org.orekit.orbits.Orbit, sigmaY: org.orekit.propagation.StateCovariance, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: _compute_9__T, ym: _compute_9__T, sigmaX: _compute_9__T, sigmaY: _compute_9__T, radius: _compute_9__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_10__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_10__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_11__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_11__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_11__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_11__T], t: _compute_11__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_12__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...

class AbstractShortTermEncounter1DNumerical2DPOCMethod(AbstractShortTermEncounter2DPOCMethod):
    """
    This abstract class serves as a foundation to create 1D numerical 2D probability of collision computing method.
    
    Since:
        12.0
    """
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_5__T = typing.TypeVar('_compute_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_6__T = typing.TypeVar('_compute_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_13__T = typing.TypeVar('_compute_13__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_14__T = typing.TypeVar('_compute_14__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_15__T = typing.TypeVar('_compute_15__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_16__T = typing.TypeVar('_compute_16__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_17__T = typing.TypeVar('_compute_17__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, xm: _compute_0__T, ym: _compute_0__T, sigmaX: _compute_0__T, sigmaY: _compute_0__T, radius: _compute_0__T, customIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_0__T], customMaxNbOfEval: int) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Compute the probability of collision using parameters necessary for creating a ShortTermEncounter2DDefinition instance.
        
        Parameters:
            primaryAtTCA (FieldOrbit<T> primaryAtTCA): primary collision object spacecraft state at time of closest approach
            primaryCovariance (FieldStateCovariance<T> primaryCovariance): primary collision object covariance
            primaryRadius (T): primary collision object equivalent sphere radius (m)
            secondaryAtTCA (FieldOrbit<T> secondaryAtTCA): secondary collision object spacecraft state at time of closest approach
            secondaryCovariance (FieldStateCovariance<T> secondaryCovariance): secondary collision object covariance
            secondaryRadius (T): secondary collision object equivalent sphere radius (m)
            customIntegrator (FieldUnivariateIntegrator<T> customIntegrator): different univariate function numerical integrator than the one defined in the instance
            customMaxNbOfEval (int): different maximum number of function evaluation when integrating than the one defined in the instance
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float, customIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, customMaxNbOfEval: int) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Compute the probability of collision using parameters necessary for creating a ShortTermEncounter2DDefinition instance.
        
        Parameters:
            primaryAtTCA (Orbit): primary collision object spacecraft state at time of closest approach
            primaryCovariance (StateCovariance): primary collision object covariance
            primaryRadius (double): primary collision object equivalent sphere radius (m)
            secondaryAtTCA (Orbit): secondary collision object spacecraft state at time of closest approach
            secondaryCovariance (StateCovariance): secondary collision object covariance
            secondaryRadius (double): secondary collision object equivalent sphere radius (m)
            customIntegrator (UnivariateIntegrator): different univariate function numerical integrator than the one defined in the instance
            customMaxNbOfEval (int): different maximum number of function evaluation when integrating than the one defined in the instance
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        Compute the probability of collision using arguments specific to the rotated encounter frame and custom numerical configuration.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
            customIntegrator (UnivariateIntegrator): custom integrator to use in place of the integrator from the constructor
            customMaxNbOfEval (int): custom maximum number of evaluations to use in place of the custom maximum number from the constructor
        
        Returns:
            probability of collision
        
        public abstract <T extends CalculusFieldElement<T>> FieldProbabilityOfCollision<T> compute (T xm, T ym, T sigmaX, T sigmaY, T radius, FieldUnivariateIntegrator<T> customIntegrator, int customMaxNbOfEval)
        
        Compute the probability of collision using arguments specific to the rotated encounter frame and custom numerical configuration.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
            customIntegrator (FieldUnivariateIntegrator<T> customIntegrator): custom integrator to use in place of the integrator from the constructor
            customMaxNbOfEval (int): custom maximum number of evaluations to use in place of the custom maximum number from the constructor
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]:
        """
        Compute the probability of collision using an Cdm.
        
        Parameters:
            cdm (Cdm): conjunction data message
            primaryRadius (T): primary collision object equivalent sphere radius (m)
            secondaryRadius (T): secondary collision object equivalent sphere radius (m)
            zeroThreshold (FieldUnivariateIntegrator<T> customIntegrator): threshold below which values are considered equal to zero
            customIntegrator (int): different univariate function numerical integrator than the one defined in the instance
            customMaxNbOfEval (double): different maximum number of function evaluation when integrating than the one defined in the instance
        
        Returns:
            probability of collision
        
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_3__T, t2: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]:
        """
        Compute the probability of collision using given collision definition.
        
        Parameters:
            encounterDefinition (FieldShortTermEncounter2DDefinition<T> encounterDefinition): encounter definition between a primary and a secondary collision object
            customIntegrator (FieldUnivariateIntegrator<T> customIntegrator): custom integrator to use in place of the integrator from the constructor
            customMaxNbOfEval (int): custom maximum number of evaluations to use in place of the custom maximum number from the
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.orbits.FieldOrbit[_compute_4__T], primaryRadius: org.orekit.propagation.FieldStateCovariance[_compute_4__T], secondaryRadius: _compute_4__T, customIntegrator: org.orekit.orbits.FieldOrbit[_compute_4__T], customMaxNbOfEval: org.orekit.propagation.FieldStateCovariance[_compute_4__T], zeroThreshold: _compute_4__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.FieldOrbit[_compute_5__T], ym: org.orekit.propagation.FieldStateCovariance[_compute_5__T], sigmaX: org.orekit.orbits.FieldOrbit[_compute_5__T], sigmaY: org.orekit.propagation.FieldStateCovariance[_compute_5__T], radius: _compute_5__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_5__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_6__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_6__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Compute the probability of collision using an Cdm.
        
        Parameters:
            cdm (Cdm): conjunction data message input
            primaryRadius (double): primary collision object equivalent sphere radius (m)
            secondaryRadius (double): secondary collision object equivalent sphere radius (m)
            customIntegrator (UnivariateIntegrator): different univariate function numerical integrator than the one defined in the instance
            customMaxNbOfEval (int): different maximum number of function evaluation when integrating than the one defined in the instance
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        Compute the probability of collision using a given collision definition.
        
        Parameters:
            encounterDefinition (ShortTermEncounter2DDefinition): probabilityOfCollision definition between a primary and a secondary collision object
            customIntegrator (UnivariateIntegrator): different univariate function numerical integrator than the one defined in the instance
            customMaxNbOfEval (int): different maximum number of function evaluation when integrating than the one defined in the instance
            zeroThreshold (double): threshold below which values are considered equal to zero
        
        Returns:
            probability of collision
        
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        It uses the defaults integrator and maximum number of function evaluation when integrating.
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.orbits.Orbit, primaryRadius: org.orekit.propagation.StateCovariance, secondaryRadius: float, customIntegrator: org.orekit.orbits.Orbit, customMaxNbOfEval: org.orekit.propagation.StateCovariance, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.Orbit, ym: org.orekit.propagation.StateCovariance, sigmaX: org.orekit.orbits.Orbit, sigmaY: org.orekit.propagation.StateCovariance, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: _compute_11__T, ym: _compute_11__T, sigmaX: _compute_11__T, sigmaY: _compute_11__T, radius: _compute_11__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, primaryRadius: _compute_12__T, secondaryRadius: _compute_12__T, customIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_12__T], customMaxNbOfEval: int, zeroThreshold: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, primaryAtTCA: org.orekit.orbits.FieldOrbit[_compute_13__T], primaryCovariance: org.orekit.propagation.FieldStateCovariance[_compute_13__T], primaryRadius: _compute_13__T, secondaryAtTCA: org.orekit.orbits.FieldOrbit[_compute_13__T], secondaryCovariance: org.orekit.propagation.FieldStateCovariance[_compute_13__T], secondaryRadius: _compute_13__T, customIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_13__T], customMaxNbOfEval: int, zeroThreshold: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_13__T]: ...
    @typing.overload
    def compute(self, encounterDefinition: FieldShortTermEncounter2DDefinition[_compute_14__T], customIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_14__T], customMaxNbOfEval: int, zeroThreshold: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_14__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_15__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_15__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.orbits.FieldOrbit[_compute_16__T], primaryRadius: org.orekit.propagation.FieldStateCovariance[_compute_16__T], secondaryRadius: org.orekit.orbits.FieldOrbit[_compute_16__T], customIntegrator: org.orekit.propagation.FieldStateCovariance[_compute_16__T], customMaxNbOfEval: _compute_16__T, zeroThreshold: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_16__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_17__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_17__T]: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, primaryRadius: float, secondaryRadius: float, customIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, customMaxNbOfEval: int, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, primaryAtTCA: org.orekit.orbits.Orbit, primaryCovariance: org.orekit.propagation.StateCovariance, primaryRadius: float, secondaryAtTCA: org.orekit.orbits.Orbit, secondaryCovariance: org.orekit.propagation.StateCovariance, secondaryRadius: float, customIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, customMaxNbOfEval: int, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, encounterDefinition: ShortTermEncounter2DDefinition, customIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, customMaxNbOfEval: int, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.orbits.Orbit, primaryRadius: org.orekit.propagation.StateCovariance, secondaryRadius: org.orekit.orbits.Orbit, customIntegrator: org.orekit.propagation.StateCovariance, customMaxNbOfEval: float, zeroThreshold: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...

class Alfano2005(AbstractShortTermEncounter2DPOCMethod):
    """
    Compute the probability of collision using the method described in :"S. Alfano. A numerical implementation of spherical objet collision probability. Journal of Astronautical Sciences, 53(1), January-March 2005."
    
    It assumes :
    
      - Short encounter leading to a linear relative motion.
      - Spherical collision object.
      - Uncorrelated positional covariance.
      - Gaussian distribution of the position uncertainties.
      - Deterministic velocity i.e. no velocity uncertainties.
    
    Also, it has been implemented using a simpson integration scheme as explained in his paper.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Empty constructor.
        """
        ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_10__T = typing.TypeVar('_compute_10__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, t2: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t2: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.FieldOrbit[_compute_3__T], ym: org.orekit.propagation.FieldStateCovariance[_compute_3__T], sigmaX: org.orekit.orbits.FieldOrbit[_compute_3__T], sigmaY: org.orekit.propagation.FieldStateCovariance[_compute_3__T], radius: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.Orbit, ym: org.orekit.propagation.StateCovariance, sigmaX: org.orekit.orbits.Orbit, sigmaY: org.orekit.propagation.StateCovariance, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_9__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_10__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_10__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_10__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_10__T], t: _compute_10__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_10__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_11__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, xm: _compute_12__T, ym: _compute_12__T, sigmaX: _compute_12__T, sigmaY: _compute_12__T, radius: _compute_12__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...

class Chan1997(AbstractShortTermEncounter2DPOCMethod):
    """
    Compute the probability of collision using the method described in :
    
    "Chan, K. “Collision Probability Analyses for Earth Orbiting Satellites.” In Space Cooperation into the 21st Century: 7th AAS/JRS/CSA Symposium, International Space Conference of Pacific-Basin Societies (ISCOPS; formerly PISSTA) (July 15-18, 1997, Nagasaki, Japan), edited by Peter M. Bainum, et al., 1033-1048. Advances in the Astronautical Sciences Series 96. San Diego, California: Univelt, 1997. (Zeroth order analytical expression).
    
    This method is also described in depth in : "CHAN, F. Kenneth, et al. Spacecraft collision probability. El Segundo, CA : Aerospace Press, 2008."
    
    It assumes :
    
      - Short encounter leading to a linear relative motion.
      - Spherical collision object.
      - Uncorrelated positional covariance.
      - Gaussian distribution of the position uncertainties.
      - Deterministic velocity i.e. no velocity uncertainties.
      - Approximate ellipse by a disk
    
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Empty constructor.
        """
        ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_10__T = typing.TypeVar('_compute_10__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, t2: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t2: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.FieldOrbit[_compute_3__T], ym: org.orekit.propagation.FieldStateCovariance[_compute_3__T], sigmaX: org.orekit.orbits.FieldOrbit[_compute_3__T], sigmaY: org.orekit.propagation.FieldStateCovariance[_compute_3__T], radius: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.Orbit, ym: org.orekit.propagation.StateCovariance, sigmaX: org.orekit.orbits.Orbit, sigmaY: org.orekit.propagation.StateCovariance, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_9__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_10__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_10__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_10__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_10__T], t: _compute_10__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_10__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_11__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, xm: _compute_12__T, ym: _compute_12__T, sigmaX: _compute_12__T, sigmaY: _compute_12__T, radius: _compute_12__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...

class Laas2015(AbstractShortTermEncounter2DPOCMethod):
    """
    Compute the probability of collision using the method described in : "SERRA, Romain, ARZELIER, Denis, JOLDES, Mioara, et al. Fast and accurate computation of orbital collision probability for short-term encounters. Journal of Guidance, Control, and Dynamics, 2016, vol. 39, no 5, p. 1009-1021.".
    
    It is one of the recommended methods to use.
    
    It assumes :
    
      - Short encounter leading to a linear relative motion.
      - Spherical collision object.
      - Uncorrelated positional covariance.
      - Gaussian distribution of the position uncertainties.
      - Deterministic velocity i.e. no velocity uncertainties.
    
    The following constants are defined when using the empty constructor :
    
      - A default absolute accuracy of 1e-30.
      - A maximum number of computed terms of 37000.
    
    This implementation has been translated from python from the provided source code of Romain SERRA on the py
    
    Since:
        12.0
    """
    DEFAULT_SCALING_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default scaling threshold to use when sum becomes large.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, absoluteAccuracy: float, maxNumberOfTerms: int): ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_13__T = typing.TypeVar('_compute_13__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, t2: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t2: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.FieldOrbit[_compute_3__T], ym: org.orekit.propagation.FieldStateCovariance[_compute_3__T], sigmaX: org.orekit.orbits.FieldOrbit[_compute_3__T], sigmaY: org.orekit.propagation.FieldStateCovariance[_compute_3__T], radius: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        public final <T extends CalculusFieldElement<T>> FieldProbabilityOfCollision<T> compute (T xm, T ym, T sigmaX, T sigmaY, T radius)
        
        Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.Orbit, ym: org.orekit.propagation.StateCovariance, sigmaX: org.orekit.orbits.Orbit, sigmaY: org.orekit.propagation.StateCovariance, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: _compute_9__T, ym: _compute_9__T, sigmaX: _compute_9__T, sigmaY: _compute_9__T, radius: _compute_9__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_11__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_12__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_12__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_12__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_12__T], t: _compute_12__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_13__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_13__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...

class PythonAbstractShortTermEncounter2DPOCMethod(AbstractShortTermEncounter2DPOCMethod):
    def __init__(self, name: str):
        """
        Constructor.
        
        Parameters:
            name (String): name of the method
        
        
        """
        ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_13__T = typing.TypeVar('_compute_13__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Description copied from interface: compute Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, t2: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t2: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.FieldOrbit[_compute_3__T], ym: org.orekit.propagation.FieldStateCovariance[_compute_3__T], sigmaX: org.orekit.orbits.FieldOrbit[_compute_3__T], sigmaY: org.orekit.propagation.FieldStateCovariance[_compute_3__T], radius: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Description copied from interface: compute Compute the probability of collision using arguments specific to the rotated encounter frame.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: org.orekit.orbits.Orbit, ym: org.orekit.propagation.StateCovariance, sigmaX: org.orekit.orbits.Orbit, sigmaY: org.orekit.propagation.StateCovariance, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: _compute_9__T, ym: _compute_9__T, sigmaX: _compute_9__T, sigmaY: _compute_9__T, radius: _compute_9__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_11__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_12__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_12__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_12__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_12__T], t: _compute_12__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_13__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_13__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Description copied from interface: getType Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class Alfriend1999(AbstractAlfriend1999):
    """
    Compute the probability of collision using the method described in : "Kyle Alfriend, Maruthi Akella, Joseph Frisbee, James Foster, Deok-Jin Lee, and Matthew Wilkins. Probability of ProbabilityOfCollision Error Analysis. Space Debris, 1(1):21–35, 1999.".
    
    It assumes :
    
      - Short encounter leading to a linear relative motion.
      - Spherical collision object.
      - Uncorrelated positional covariance.
      - Gaussian distribution of the position uncertainties.
      - Deterministic velocity i.e. no velocity uncertainties.
      - Both objects are in circular orbits (eq 14).
      - Probability density function is constant over the collision disk (eq 18).
    
    By assuming a constant probability density function over the collision circle this method will, most of the time, give much higher probability of collision than other regular methods. That is why it is qualified as a maximum probability of collision computing method.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Empty constructor.
        """
        ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...
    def isAMaximumProbabilityOfCollisionMethod(self) -> bool:
        """
        Get flag that defines if the method is a maximum probability of collision computing method.
        
        Specified by: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.ShortTermEncounter2DPOCMethod.isAMaximumProbabilityOfCollisionMethod` in interface ShortTermEncounter2DPOCMethod
        
        Overrides: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.AbstractShortTermEncounter2DPOCMethod.isAMaximumProbabilityOfCollisionMethod` in class AbstractShortTermEncounter2DPOCMethod
        
        Returns:
            flag that defines if the method is a maximum probability of collision computing method
        
        
        """
        ...

class Alfriend1999Max(AbstractAlfriend1999):
    """
    Compute the probability of collision assuming the worst case described in : "Kyle Alfriend, Maruthi Akella, Joseph Frisbee, James Foster, Deok-Jin Lee, and Matthew Wilkins. Probability of ProbabilityOfCollision Error Analysis. Space Debris, 1(1):21–35, 1999.".
    
    It assumes:
    
      - Short encounter leading to a linear relative motion.
      - Spherical collision object.
      - Uncorrelated positional covariance.
      - Gaussian distribution of the position uncertainties.
      - Deterministic velocity i.e. no velocity uncertainties.
      - Both objects are in circular orbits (eq 14).
      - Probability density function is constant over the collision circle (eq 18).
      - Covariance multiplied by a coefficient KSquared = MahalanobisDistanceSquared / 2 (eq 19-20).
    
    By assuming a constant probability density function over the collision circle this method will, most of the time, give much higher probability of collision than other regular methods. That is why it is qualified as a maximum probability of collision computing method.
    
    Since:
        12.0
    
    Also see:
        Mahalanobis_distance
    """
    def __init__(self):
        """
        Empty constructor.
        """
        ...
    _computeValue_1__T = typing.TypeVar('_computeValue_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeValue(self, radius: float, squaredMahalanobisDistance: float, covarianceMatrixDeterminant: float) -> float:
        """
        Compute the value of the probability of collision.
        
        Parameters:
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
            squaredMahalanobisDistance (double): squared Mahalanobis distance
            covarianceMatrixDeterminant (double): covariance matrix determinant
        
        Returns:
            value of the probability of collision
        
        """
        ...
    @typing.overload
    def computeValue(self, radius: _computeValue_1__T, squaredMahalanobisDistance: _computeValue_1__T, covarianceMatrixDeterminant: _computeValue_1__T) -> _computeValue_1__T:
        """
        Compute the value of the probability of collision.
        
        Parameters:
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
            squaredMahalanobisDistance (T): squared Mahalanobis distance
            covarianceMatrixDeterminant (T): covariance matrix determinant
        
        Returns:
            value of the probability of collision
        
        
        """
        ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...
    def isAMaximumProbabilityOfCollisionMethod(self) -> bool:
        """
        Get flag that defines if the method is a maximum probability of collision computing method.
        
        Specified by: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.ShortTermEncounter2DPOCMethod.isAMaximumProbabilityOfCollisionMethod` in interface ShortTermEncounter2DPOCMethod
        
        Overrides: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.AbstractShortTermEncounter2DPOCMethod.isAMaximumProbabilityOfCollisionMethod` in class AbstractShortTermEncounter2DPOCMethod
        
        Returns:
            flag that defines if the method is a maximum probability of collision computing method
        
        
        """
        ...

class Patera2005(AbstractShortTermEncounter1DNumerical2DPOCMethod):
    """
    Compute the probability of collision using the method described in :"PATERA, Russell P. Calculating collision probability for arbitrary space vehicle shapes via numerical quadrature. Journal of guidance, control, and dynamics, 2005, vol. 28, no 6, p. 1326-1328.".
    
    It is one of the recommended methods to use.
    
    It assumes :
    
      - Short encounter leading to a linear relative motion.
      - Spherical collision object (in this implementation only. The method could be used on non spherical object).
      - Uncorrelated positional covariance.
      - Gaussian distribution of the position uncertainties.
      - Deterministic velocity i.e. no velocity uncertainties.
    
    It has been rewritten to use Orekit specific inputs.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, integrator: org.hipparchus.analysis.integration.UnivariateIntegrator, maxNbOfEval: int): ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_10__T = typing.TypeVar('_compute_10__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_13__T = typing.TypeVar('_compute_13__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_14__T = typing.TypeVar('_compute_14__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_15__T = typing.TypeVar('_compute_15__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_16__T = typing.TypeVar('_compute_16__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame and custom numerical configuration.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Specified by: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.AbstractShortTermEncounter1DNumerical2DPOCMethod.compute` in class AbstractShortTermEncounter1DNumerical2DPOCMethod
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
            customIntegrator (FieldUnivariateIntegrator<T> customIntegrator): custom integrator to use in place of the integrator from the constructor
            customMaxNbOfEval (int): custom maximum number of evaluations to use in place of the custom maximum number from the constructor
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, t2: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t2: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_3__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_3__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_3__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_3__T], t: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Compute the probability of collision using arguments specific to the rotated encounter frame and custom numerical configuration.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Specified by: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.AbstractShortTermEncounter1DNumerical2DPOCMethod.compute` in class AbstractShortTermEncounter1DNumerical2DPOCMethod
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
            integrator (UnivariateIntegrator): custom integrator to use in place of the integrator from the constructor
            customMaxNbOfEval (int): custom maximum number of evaluations to use in place of the custom maximum number from the constructor
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, t: _compute_9__T, t2: _compute_9__T, t3: _compute_9__T, t4: _compute_9__T, t5: _compute_9__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_10__T, t2: _compute_10__T, fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_10__T], int: int, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_10__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_11__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_11__T], t: _compute_11__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_11__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_11__T], t2: _compute_11__T, fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_11__T], int: int, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_12__T], fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_12__T], int: int, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_13__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_13__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_14__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_14__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_14__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_14__T], t: _compute_14__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_14__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_15__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_15__T]: ...
    @typing.overload
    def compute(self, t: _compute_16__T, t2: _compute_16__T, t3: _compute_16__T, t4: _compute_16__T, t5: _compute_16__T, fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_16__T], int: int) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_16__T]: ...
    @typing.overload
    def compute(self, double: float, double2: float, double3: float, double4: float, double5: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, int: int, double3: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, int: int, double3: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, int: int, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, double: float, double2: float, double3: float, double4: float, double5: float, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, int: int) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...

class PythonAbstractAlfriend1999(AbstractAlfriend1999):
    def __init__(self, name: str):
        """
        Default constructor.
        
        Parameters:
            name (String): name of the method
        
        
        """
        ...
    _computeValue_1__T = typing.TypeVar('_computeValue_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeValue(self, radius: float, squaredMahalanobisDistance: float, covarianceMatrixDeterminant: float) -> float: ...
    @typing.overload
    def computeValue(self, radius: _computeValue_1__T, squaredMahalanobisDistance: _computeValue_1__T, covarianceMatrixDeterminant: _computeValue_1__T) -> _computeValue_1__T: ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Description copied from interface: getType Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonAbstractShortTermEncounter1DNumerical2DPOCMethod(AbstractShortTermEncounter1DNumerical2DPOCMethod):
    def __init__(self, name: str, integrator: org.hipparchus.analysis.integration.UnivariateIntegrator, maxNbOfEval: int):
        """
        Customizable constructor.
        
        Parameters:
            name (String): name of the method
            integrator (UnivariateIntegrator): integrator
            maxNbOfEval (int): max number of evaluation
        
        
        """
        ...
    _compute_0__T = typing.TypeVar('_compute_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_1__T = typing.TypeVar('_compute_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_2__T = typing.TypeVar('_compute_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_3__T = typing.TypeVar('_compute_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_4__T = typing.TypeVar('_compute_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_9__T = typing.TypeVar('_compute_9__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_11__T = typing.TypeVar('_compute_11__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_12__T = typing.TypeVar('_compute_12__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_13__T = typing.TypeVar('_compute_13__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_14__T = typing.TypeVar('_compute_14__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_15__T = typing.TypeVar('_compute_15__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_16__T = typing.TypeVar('_compute_16__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compute_17__T = typing.TypeVar('_compute_17__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_0__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_0__T]:
        """
        Description copied from class: compute Compute the probability of collision using arguments specific to the rotated encounter frame and custom numerical configuration.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Specified by: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.AbstractShortTermEncounter1DNumerical2DPOCMethod.compute` in class AbstractShortTermEncounter1DNumerical2DPOCMethod
        
        Parameters:
            xm (T): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (T): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (T): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (T): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (T): sum of primary and secondary collision object equivalent sphere radii (m)
            customIntegrator (FieldUnivariateIntegrator<T> customIntegrator): custom integrator to use in place of the integrator from the constructor
            customMaxNbOfEval (int): custom maximum number of evaluations to use in place of the custom maximum number from the constructor
        
        Returns:
            probability of collision
        
        
        """
        ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_1__T, t2: _compute_1__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_1__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t: _compute_2__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_2__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_2__T], t2: _compute_2__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_2__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_3__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_3__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_3__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_3__T], t: _compute_3__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_3__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_4__T]) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_4__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision:
        """
        Description copied from class: compute Compute the probability of collision using arguments specific to the rotated encounter frame and custom numerical configuration.
        
        The rotated encounter frame is define by the initial encounter frame (defined in ShortTermEncounter2DDefinition) rotated by the rotation matrix which is used to diagonalize the combined covariance matrix.
        
        Specified by: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.AbstractShortTermEncounter1DNumerical2DPOCMethod.compute` in class AbstractShortTermEncounter1DNumerical2DPOCMethod
        
        Parameters:
            xm (double): other collision object projected position onto the collision plane in the rotated encounter frame x-axis (m)
            ym (double): other collision object projected position onto the collision plane in the rotated encounter frame y-axis (m)
            sigmaX (double): square root of the x-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            sigmaY (double): square root of the y-axis eigen value of the diagonalized combined covariance matrix projected onto the collision plane
                (m)
            radius (double): sum of primary and secondary collision object equivalent sphere radii (m)
            customIntegrator (UnivariateIntegrator): custom integrator to use in place of the integrator from the constructor
            customMaxNbOfEval (int): custom maximum number of evaluations to use in place of the custom maximum number from the constructor
        
        Returns:
            probability of collision
        
        """
        ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, xm: _compute_9__T, ym: _compute_9__T, sigmaX: _compute_9__T, sigmaY: _compute_9__T, radius: _compute_9__T, customIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_9__T], customMaxNbOfEval: int) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_9__T]: ...
    @typing.overload
    def compute(self, xm: float, ym: float, sigmaX: float, sigmaY: float, radius: float, customIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, customMaxNbOfEval: int) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, t: _compute_11__T, t2: _compute_11__T, t3: _compute_11__T, t4: _compute_11__T, t5: _compute_11__T) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_11__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_12__T, t2: _compute_12__T, fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_12__T], int: int, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_12__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_13__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_13__T], t: _compute_13__T, fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_13__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_13__T], t2: _compute_13__T, fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_13__T], int: int, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_13__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_14__T], fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_compute_14__T], int: int, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_14__T]: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, t: _compute_15__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_15__T]: ...
    @typing.overload
    def compute(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_compute_16__T], fieldStateCovariance: org.orekit.propagation.FieldStateCovariance[_compute_16__T], fieldOrbit2: org.orekit.orbits.FieldOrbit[_compute_16__T], fieldStateCovariance2: org.orekit.propagation.FieldStateCovariance[_compute_16__T], t: _compute_16__T, double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_16__T]: ...
    @typing.overload
    def compute(self, fieldShortTermEncounter2DDefinition: FieldShortTermEncounter2DDefinition[_compute_17__T], double: float) -> org.orekit.ssa.metrics.FieldProbabilityOfCollision[_compute_17__T]: ...
    @typing.overload
    def compute(self, double: float, double2: float, double3: float, double4: float, double5: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float, double2: float, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, int: int, double3: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, double: float, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double2: float, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, int: int, double3: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator, int: int, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, cdm: org.orekit.files.ccsds.ndm.cdm.Cdm, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, orbit: org.orekit.orbits.Orbit, stateCovariance: org.orekit.propagation.StateCovariance, orbit2: org.orekit.orbits.Orbit, stateCovariance2: org.orekit.propagation.StateCovariance, double: float, double2: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    @typing.overload
    def compute(self, shortTermEncounter2DDefinition: ShortTermEncounter2DDefinition, double: float) -> org.orekit.ssa.metrics.ProbabilityOfCollision: ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.ssa.collision.shorttermencounter.probability.twod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getType(self) -> ShortTermEncounter2DPOCMethodType:
        """
        Description copied from interface: getType Get type of the method.
        
        Returns:
            type of the method
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.ssa.collision.shorttermencounter.probability.twod")``.

    AbstractAlfriend1999: typing.Type[AbstractAlfriend1999]
    AbstractShortTermEncounter1DNumerical2DPOCMethod: typing.Type[AbstractShortTermEncounter1DNumerical2DPOCMethod]
    AbstractShortTermEncounter2DPOCMethod: typing.Type[AbstractShortTermEncounter2DPOCMethod]
    Alfano2005: typing.Type[Alfano2005]
    Alfriend1999: typing.Type[Alfriend1999]
    Alfriend1999Max: typing.Type[Alfriend1999Max]
    Chan1997: typing.Type[Chan1997]
    FieldShortTermEncounter2DDefinition: typing.Type[FieldShortTermEncounter2DDefinition]
    Laas2015: typing.Type[Laas2015]
    Patera2005: typing.Type[Patera2005]
    PythonAbstractAlfriend1999: typing.Type[PythonAbstractAlfriend1999]
    PythonAbstractShortTermEncounter1DNumerical2DPOCMethod: typing.Type[PythonAbstractShortTermEncounter1DNumerical2DPOCMethod]
    PythonAbstractShortTermEncounter2DPOCMethod: typing.Type[PythonAbstractShortTermEncounter2DPOCMethod]
    PythonShortTermEncounter2DPOCMethod: typing.Type[PythonShortTermEncounter2DPOCMethod]
    ShortTermEncounter2DDefinition: typing.Type[ShortTermEncounter2DDefinition]
    ShortTermEncounter2DPOCMethod: typing.Type[ShortTermEncounter2DPOCMethod]
    ShortTermEncounter2DPOCMethodType: typing.Type[ShortTermEncounter2DPOCMethodType]
