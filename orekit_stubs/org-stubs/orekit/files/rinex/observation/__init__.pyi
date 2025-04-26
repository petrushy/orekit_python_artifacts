
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.euclidean.twod
import org.orekit.data
import org.orekit.files.rinex
import org.orekit.files.rinex.section
import org.orekit.gnss
import org.orekit.time
import typing



class GlonassSatelliteChannel:
    """
    public class GlonassSatelliteChannel extends :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for association between GLONASS satellites and frequency channels (f = f₀ + k Δf with k ranging-7 to +6).
    
        Since:
            12.0
    """
    def __init__(self, satInSystem: org.orekit.gnss.SatInSystem, int: int): ...
    def getK(self) -> int:
        """
            Get the channel frequency multiplier.
        
            Returns:
                channel frequency multiplier
        
        
        """
        ...
    def getSatellite(self) -> org.orekit.gnss.SatInSystem:
        """
            Get the satellite identifier.
        
            Returns:
                satellite identifier
        
        
        """
        ...

class ObservationData:
    """
    public class ObservationData extends :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Observation Data.
    
        Since:
            9.2
    """
    def __init__(self, observationType: org.orekit.gnss.ObservationType, double: float, int: int, int2: int): ...
    def getLossOfLockIndicator(self) -> int:
        """
            Get the Loss of Lock Indicator.
        
            Returns:
                Loss of Lock Indicator
        
        
        """
        ...
    def getObservationType(self) -> org.orekit.gnss.ObservationType:
        """
            Get the observation type.
        
            Returns:
                observation type
        
        
        """
        ...
    def getSignalStrength(self) -> int:
        """
            Get the signal strength.
        
            Returns:
                signal strength
        
        
        """
        ...
    def getValue(self) -> float:
        """
            Get the observed value.
        
            Returns:
                observed value (may be :code:`Double.NaN` if observation not available)
        
        
        """
        ...

class ObservationDataSet(org.orekit.time.TimeStamped):
    """
    public class ObservationDataSet extends :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Observation Data set.
    
        Since:
            9.2
    """
    def __init__(self, satInSystem: org.orekit.gnss.SatInSystem, absoluteDate: org.orekit.time.AbsoluteDate, int: int, double: float, list: java.util.List[ObservationData]): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getEventFlag(self) -> int:
        """
            Get the event flag.
        
            Returns:
                event flag
        
            Since:
                12.0
        
        
        """
        ...
    def getObservationData(self) -> java.util.List[ObservationData]: ...
    def getRcvrClkOffset(self) -> float:
        """
            Get receiver clock offset.
        
            Returns:
                receiver clock offset (it is optional, may be 0)
        
        
        """
        ...
    def getSatellite(self) -> org.orekit.gnss.SatInSystem:
        """
            Get observed satellite.
        
            Returns:
                observed satellite
        
            Since:
                12.0
        
        
        """
        ...

class PhaseShiftCorrection:
    """
    public class PhaseShiftCorrection extends :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Phase Shift corrections. Contains the phase shift corrections used to generate phases consistent with respect to cycle
        shifts.
    
        Since:
            12.0
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, observationType: org.orekit.gnss.ObservationType, double: float, list: java.util.List[org.orekit.gnss.SatInSystem]): ...
    def getCorrection(self) -> float:
        """
            Get the Phase Shift Corrections.
        
            Returns:
                Phase Shift Corrections (cycles)
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get the Satellite System.
        
            Returns:
                Satellite System.
        
        
        """
        ...
    def getSatsCorrected(self) -> java.util.List[org.orekit.gnss.SatInSystem]: ...
    def getTypeObs(self) -> org.orekit.gnss.ObservationType:
        """
            Get the Carrier Phase Observation Code.
        
            The observation code may be null for the uncorrected reference signal group
        
            Returns:
                Carrier Phase Observation Code.
        
        
        """
        ...

class RinexObservation(org.orekit.files.rinex.RinexFile['RinexObservationHeader']):
    """
    public class RinexObservation extends :class:`~org.orekit.files.rinex.RinexFile`<:class:`~org.orekit.files.rinex.observation.RinexObservationHeader`>
    
        Container for Rinex observation file.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def addObservationDataSet(self, observationDataSet: ObservationDataSet) -> None:
        """
            Add an observations data set.
        
            Observations must be added chronologically, within header date range, and separated by an integer multiple of the
            :meth:`~org.orekit.files.rinex.observation.RinexObservationHeader.getInterval` (ideally one interval, but entries at
            same dates and missing entries are allowed so any non-negative integer is allowed).
        
            Parameters:
                observationsDataSet (:class:`~org.orekit.files.rinex.observation.ObservationDataSet`): observations data set
        
        
        """
        ...
    def bundleByDates(self) -> java.lang.Iterable[java.util.List[ObservationDataSet]]: ...
    def extractClockModel(self, int: int) -> org.orekit.time.SampledClockModel:
        """
            Extract the receiver clock model.
        
            Parameters:
                nbInterpolationPoints (int): number of points to use in interpolation
        
            Returns:
                extracted clock model or null if all :meth:`~org.orekit.files.rinex.observation.ObservationDataSet.getRcvrClkOffset` are
                zero
        
            Since:
                12.1
        
        
        """
        ...
    def getObservationDataSets(self) -> java.util.List[ObservationDataSet]: ...

class RinexObservationHeader(org.orekit.files.rinex.section.RinexBaseHeader):
    """
    public class RinexObservationHeader extends :class:`~org.orekit.files.rinex.section.RinexBaseHeader`
    
        Container for Rinex observation file header.
    
        Since:
            9.2
    """
    def __init__(self): ...
    def addAppliedDCBS(self, appliedDCBS: org.orekit.files.rinex.AppliedDCBS) -> None:
        """
            Add applied differential code bias corrections.
        
            Parameters:
                appliedDCBS (:class:`~org.orekit.files.rinex.AppliedDCBS`): applied differential code bias corrections to add
        
        
        """
        ...
    def addAppliedPCVS(self, appliedPCVS: org.orekit.files.rinex.AppliedPCVS) -> None:
        """
            Add antenna center variation corrections.
        
            Parameters:
                appliedPCVS (:class:`~org.orekit.files.rinex.AppliedPCVS`): antenna center variation corrections
        
        
        """
        ...
    def addGlonassChannel(self, glonassSatelliteChannel: GlonassSatelliteChannel) -> None:
        """
            Add GLONASS satellite/channel association.
        
            Parameters:
                glonassChannel (:class:`~org.orekit.files.rinex.observation.GlonassSatelliteChannel`): GLONASS satellite/channel association
        
            Since:
                12.0
        
        
        """
        ...
    def addPhaseShiftCorrection(self, phaseShiftCorrection: PhaseShiftCorrection) -> None:
        """
            Add phase shift correction used to generate phases consistent w/r to cycle shifts.
        
            Parameters:
                phaseShiftCorrection (:class:`~org.orekit.files.rinex.observation.PhaseShiftCorrection`): phase shift correction used to generate phases consistent w/r to cycle shifts
        
        
        """
        ...
    def addScaleFactorCorrection(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, scaleFactorCorrection: 'ScaleFactorCorrection') -> None:
        """
            Add scale factor correction.
        
            Parameters:
                satelliteSystem (:class:`~org.orekit.gnss.SatelliteSystem`): system to which this scaling factor applies
                scaleFactorCorrection (:class:`~org.orekit.files.rinex.observation.ScaleFactorCorrection`): scale factor correction
        
        
        """
        ...
    def getAgencyName(self) -> str:
        """
            Get name of the agency.
        
            Returns:
                name of the agency
        
        
        """
        ...
    def getAntennaAzimuth(self) -> float:
        """
            Get the azimuth of the zero direction of a fixed antenna.
        
            Returns:
                Azimuth of the zero direction of a fixed antenna
        
        
        """
        ...
    def getAntennaBSight(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the antenna B.Sight.
        
            Returns:
                Antenna B.Sight
        
        
        """
        ...
    def getAntennaHeight(self) -> float:
        """
            Get the antenna height.
        
            Returns:
                height of the antenna
        
        
        """
        ...
    def getAntennaNumber(self) -> str:
        """
            Get the number of the antenna.
        
            Returns:
                number of the antenna
        
        
        """
        ...
    def getAntennaPhaseCenter(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the antenna phasecenter.
        
            Returns:
                Antenna phasecenter
        
        
        """
        ...
    def getAntennaReferencePoint(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position of antenna reference point for antenna on vehicle.
        
            Returns:
                Position of antenna reference point for antenna on vehicle
        
        
        """
        ...
    def getAntennaType(self) -> str:
        """
            Get the type of the antenna.
        
            Returns:
                type of the antenna
        
        
        """
        ...
    def getAntennaZeroDirection(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the zero direction of antenna.
        
            Returns:
                Zero direction of antenna
        
        
        """
        ...
    def getApproxPos(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the Approximate Marker Position.
        
            Returns:
                Approximate Marker Position
        
        
        """
        ...
    def getC1cCodePhaseBias(self) -> float:
        """
            Get the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1C` signal.
        
            Returns:
                code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1C` signal
        
            Since:
                12.0
        
        
        """
        ...
    def getC1pCodePhaseBias(self) -> float:
        """
            Get the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1P` signal.
        
            Returns:
                code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1P` signal
        
            Since:
                12.0
        
        
        """
        ...
    def getC2cCodePhaseBias(self) -> float:
        """
            Get the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2C` signal.
        
            Returns:
                code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2C` signal
        
            Since:
                12.0
        
        
        """
        ...
    def getC2pCodePhaseBias(self) -> float:
        """
            Get the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2P` signal.
        
            Returns:
                code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2P` signal
        
            Since:
                12.0
        
        
        """
        ...
    def getCenterMass(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the current center of mass of vehicle in body fixed coordinate system.
        
            Returns:
                Current center of mass of vehicle in body fixed coordinate system
        
        
        """
        ...
    def getClockOffsetApplied(self) -> bool:
        """
            Get the application flag for realtime-derived receiver clock offset.
        
            Returns:
                application flag for realtime-derived receiver clock offset
        
            Since:
                12.1
        
        
        """
        ...
    def getEccentricities(self) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
            Get the eccentricities of antenna center.
        
            Returns:
                Eccentricities of antenna center
        
        
        """
        ...
    def getGlonassChannels(self) -> java.util.List[GlonassSatelliteChannel]: ...
    def getInterval(self) -> float:
        """
            Get the observation interval in seconds.
        
            Returns:
                Observation interval in seconds
        
        
        """
        ...
    def getLeapSeconds(self) -> int:
        """
            Get the Number of leap seconds since 6-Jan-1980.
        
            Returns:
                Number of leap seconds since 6-Jan-1980
        
        
        """
        ...
    def getLeapSecondsDayNum(self) -> int:
        """
            Get the respective leap second day number.
        
            Returns:
                Respective leap second day number
        
        
        """
        ...
    def getLeapSecondsFuture(self) -> int:
        """
            Get the future or past leap seconds.
        
            Returns:
                Future or past leap seconds
        
        
        """
        ...
    def getLeapSecondsWeekNum(self) -> int:
        """
            Get the respective leap second week number.
        
            Returns:
                Respective leap second week number
        
        
        """
        ...
    def getListAppliedDCBS(self) -> java.util.List[org.orekit.files.rinex.AppliedDCBS]: ...
    def getListAppliedPCVS(self) -> java.util.List[org.orekit.files.rinex.AppliedPCVS]: ...
    def getMarkerName(self) -> str:
        """
            Get name of the antenna marker.
        
            Returns:
                name of the antenna marker
        
        
        """
        ...
    def getMarkerNumber(self) -> str:
        """
            Get number of the antenna marker.
        
            Returns:
                number of the antenna marker
        
        
        """
        ...
    def getMarkerType(self) -> str:
        """
            Get type of the antenna marker.
        
            Returns:
                type of the antenna marker
        
        
        """
        ...
    def getNbObsPerSat(self) -> java.util.Map[org.orekit.gnss.SatInSystem, java.util.Map[org.orekit.gnss.ObservationType, int]]: ...
    def getNbSat(self) -> int:
        """
            Get number of satellites.
        
            Returns:
                number of satellites
        
            Since:
                12.0
        
        
        """
        ...
    def getObservationCode(self) -> str:
        """
            Get the observation code of the average phasecenter position w/r to antenna reference point.
        
            Returns:
                Observation code of the average phasecenter position w/r to antenna reference point
        
        
        """
        ...
    def getObserverName(self) -> str:
        """
            Get name of the observer.
        
            Returns:
                name of the observer
        
        
        """
        ...
    def getPhaseCenterSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get satellite system for average phase center.
        
            Returns:
                satellite system for average phase center
        
            Since:
                12.0
        
        
        """
        ...
    def getPhaseShiftCorrections(self) -> java.util.List[PhaseShiftCorrection]: ...
    def getReceiverNumber(self) -> str:
        """
            Get the number of the receiver.
        
            Returns:
                number of the receiver
        
        
        """
        ...
    def getReceiverType(self) -> str:
        """
            Get the type of the receiver.
        
            Returns:
                type of the receiver
        
        
        """
        ...
    def getReceiverVersion(self) -> str:
        """
            Get the version of the receiver.
        
            Returns:
                version of the receiver
        
        
        """
        ...
    def getScaleFactorCorrections(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> java.util.List['ScaleFactorCorrection']: ...
    def getSignalStrengthUnit(self) -> str:
        """
            Get the unit of the carrier to noise ratio observables.
        
            Returns:
                Unit of the carrier to noise ratio observables
        
        
        """
        ...
    def getTFirstObs(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the time of First observation record.
        
            Returns:
                Time of First observation record
        
        
        """
        ...
    def getTLastObs(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the time of last observation record.
        
            Returns:
                Time of last observation record
        
        
        """
        ...
    def getTypeObs(self) -> java.util.Map[org.orekit.gnss.SatelliteSystem, java.util.List[org.orekit.gnss.ObservationType]]: ...
    def setAgencyName(self, string: str) -> None:
        """
            Setter for the agency name.
        
            Parameters:
                agencyName (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the agency name to set
        
        
        """
        ...
    def setAntennaAzimuth(self, double: float) -> None:
        """
            Set the azimuth of the zero direction of a fixed antenna.
        
            Parameters:
                antennaAzimuth (double): Azimuth of the zero direction of a fixed antenna
        
        
        """
        ...
    def setAntennaBSight(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the antenna B.Sight.
        
            Parameters:
                antennaBSight (:class:`~org.orekit.files.rinex.observation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Antenna B.Sight
        
        
        """
        ...
    def setAntennaHeight(self, double: float) -> None:
        """
            Set the antenna height.
        
            Parameters:
                antennaHeight (double): height of the antenna
        
        
        """
        ...
    def setAntennaNumber(self, string: str) -> None:
        """
            Set the number of the antenna.
        
            Parameters:
                antennaNumber (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): number of the antenna
        
        
        """
        ...
    def setAntennaPhaseCenter(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the antenna phasecenter.
        
            Parameters:
                antennaPhaseCenter (:class:`~org.orekit.files.rinex.observation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Antenna phasecenter
        
        
        """
        ...
    def setAntennaReferencePoint(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the position of antenna reference point for antenna on vehicle.
        
            Parameters:
                refPoint (:class:`~org.orekit.files.rinex.observation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Position of antenna reference point for antenna on vehicle
        
        
        """
        ...
    def setAntennaType(self, string: str) -> None:
        """
            Set the type of the antenna.
        
            Parameters:
                antennaType (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): type of the antenna
        
        
        """
        ...
    def setAntennaZeroDirection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the zero direction of antenna.
        
            Parameters:
                antennaZeroDirection (:class:`~org.orekit.files.rinex.observation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Zero direction of antenna
        
        
        """
        ...
    def setApproxPos(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the Approximate Marker Position.
        
            Parameters:
                approxPos (:class:`~org.orekit.files.rinex.observation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Approximate Marker Position
        
        
        """
        ...
    def setC1cCodePhaseBias(self, double: float) -> None:
        """
            Set the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1C` signal.
        
            Parameters:
                c1cCodePhaseBias (double): code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1C` signal
        
            Since:
                12.0
        
        
        """
        ...
    def setC1pCodePhaseBias(self, double: float) -> None:
        """
            Set the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1P` signal.
        
            Parameters:
                c1pCodePhaseBias (double): code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C1P` signal
        
            Since:
                12.0
        
        
        """
        ...
    def setC2cCodePhaseBias(self, double: float) -> None:
        """
            Set the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2C` signal.
        
            Parameters:
                c2cCodePhaseBias (double): code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2C` signal
        
            Since:
                12.0
        
        
        """
        ...
    def setC2pCodePhaseBias(self, double: float) -> None:
        """
            Set the code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2P` signal.
        
            Parameters:
                c2pCodePhaseBias (double): code phase bias correction for GLONASS :meth:`~org.orekit.gnss.PredefinedObservationType.C2P` signal
        
            Since:
                12.0
        
        
        """
        ...
    def setCenterMass(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the current center of mass of vehicle in body fixed coordinate system.
        
            Parameters:
                centerMass (:class:`~org.orekit.files.rinex.observation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Current center of mass of vehicle in body fixed coordinate system
        
        
        """
        ...
    def setClockOffsetApplied(self, boolean: bool) -> None:
        """
            Set the application flag for realtime-derived receiver clock offset.
        
            Parameters:
                clockOffsetApplied (boolean): application flag for realtime-derived receiver clock offset
        
            Since:
                12.1
        
        
        """
        ...
    def setEccentricities(self, vector2D: org.hipparchus.geometry.euclidean.twod.Vector2D) -> None:
        """
            Set the eccentricities of antenna center.
        
            Parameters:
                eccentricities (:class:`~org.orekit.files.rinex.observation.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.twod.Vector2D?is`): Eccentricities of antenna center
        
        
        """
        ...
    def setInterval(self, double: float) -> None:
        """
            Set the observation interval in seconds.
        
            Parameters:
                interval (double): Observation interval in seconds
        
        
        """
        ...
    def setLeapSeconds(self, int: int) -> None:
        """
            Set the Number of leap seconds since 6-Jan-1980.
        
            Parameters:
                leapSeconds (int): Number of leap seconds since 6-Jan-1980
        
        
        """
        ...
    def setLeapSecondsDayNum(self, int: int) -> None:
        """
            Set the respective leap second day number.
        
            Parameters:
                leapSecondsDayNum (int): Respective leap second day number
        
        
        """
        ...
    def setLeapSecondsFuture(self, int: int) -> None:
        """
            Set the future or past leap seconds.
        
            Parameters:
                leapSecondsFuture (int): Future or past leap seconds
        
        
        """
        ...
    def setLeapSecondsWeekNum(self, int: int) -> None:
        """
            Set the respective leap second week number.
        
            Parameters:
                leapSecondsWeekNum (int): Respective leap second week number
        
        
        """
        ...
    def setMarkerName(self, string: str) -> None:
        """
            Set name of the antenna marker.
        
            Parameters:
                markerName (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the antenna marker
        
        
        """
        ...
    def setMarkerNumber(self, string: str) -> None:
        """
            Set number of the antenna marker.
        
            Parameters:
                markerNumber (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): number of the antenna marker
        
        
        """
        ...
    def setMarkerType(self, string: str) -> None:
        """
            Set type of the antenna marker.
        
            Parameters:
                markerType (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): type of the antenna marker
        
        
        """
        ...
    def setNbObsPerSatellite(self, satInSystem: org.orekit.gnss.SatInSystem, observationType: org.orekit.gnss.ObservationType, int: int) -> None:
        """
            Set number of observations for a satellite.
        
            Parameters:
                sat (:class:`~org.orekit.gnss.SatInSystem`): satellite
                type (:class:`~org.orekit.gnss.ObservationType`): observation type
                nbObs (int): number of observations of this type for this satellite
        
            Since:
                12.0
        
        
        """
        ...
    def setNbSat(self, int: int) -> None:
        """
            Set number of satellites.
        
            Parameters:
                nbSat (int): number of satellites
        
            Since:
                12.0
        
        
        """
        ...
    def setObservationCode(self, string: str) -> None:
        """
            Set the observation code of the average phasecenter position w/r to antenna reference point.
        
            Parameters:
                observationCode (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Observation code of the average phasecenter position w/r to antenna reference point
        
        
        """
        ...
    def setObserverName(self, string: str) -> None:
        """
            Set name of the observer.
        
            Parameters:
                observerName (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the observer
        
        
        """
        ...
    def setPhaseCenterSystem(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> None:
        """
            Set satellite system for average phase center.
        
            Parameters:
                phaseCenterSystem (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system for average phase center
        
            Since:
                12.0
        
        
        """
        ...
    def setReceiverNumber(self, string: str) -> None:
        """
            Set the number of the receiver.
        
            Parameters:
                receiverNumber (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): number of the receiver
        
        
        """
        ...
    def setReceiverType(self, string: str) -> None:
        """
            Set the type of the receiver.
        
            Parameters:
                receiverType (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): type of the receiver
        
        
        """
        ...
    def setReceiverVersion(self, string: str) -> None:
        """
            Set the version of the receiver.
        
            Parameters:
                receiverVersion (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): version of the receiver
        
        
        """
        ...
    def setSignalStrengthUnit(self, string: str) -> None:
        """
            Set the unit of the carrier to noise ratio observables.
        
            Parameters:
                signalStrengthUnit (:class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Unit of the carrier to noise ratio observables
        
        
        """
        ...
    def setTFirstObs(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time of First observation record.
        
            Parameters:
                firstObs (:class:`~org.orekit.time.AbsoluteDate`): Time of First observation record
        
        
        """
        ...
    def setTLastObs(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time of last observation record.
        
            Parameters:
                lastObs (:class:`~org.orekit.time.AbsoluteDate`): Time of last observation record
        
        
        """
        ...
    def setTypeObs(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, list: java.util.List[org.orekit.gnss.ObservationType]) -> None: ...

class RinexObservationParser:
    """
    public class RinexObservationParser extends :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Parser for Rinex measurements files.
    
        Supported versions are: 2.00, 2.10, 2.11, 2.12 (unofficial), 2.20 (unofficial), 3.00, 3.01, 3.02, 3.03, 3.04, 3.05,
        4.00, 4.01, and 4.02.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex2.txt`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex210.txt`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex211.pdf`, `unofficial rinex 2.12
            <http://www.aiub.unibe.ch/download/rinex/rinex212.txt>`, `unofficial rinex 2.20
            <http://www.aiub.unibe.ch/download/rinex/rnx_leo.txt>`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex300.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex301.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex302.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex303.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex304.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex305.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex_4.00.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex_4.01.pdf`,
            :class:`~org.orekit.files.rinex.observation.https:.files.igs.org.pub.data.format.rinex_4.02.pdf`
    """
    DEFAULT_RINEX_2_NAMES: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_RINEX_2_NAMES
    
        Default name pattern for rinex 2 observation files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_RINEX_3_NAMES: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_RINEX_3_NAMES
    
        Default name pattern for rinex 3 observation files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[str, org.orekit.gnss.ObservationType], typing.Callable[[str], org.orekit.gnss.ObservationType]], biFunction: typing.Union[java.util.function.BiFunction[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales, org.orekit.time.TimeScale], typing.Callable[[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales], org.orekit.time.TimeScale]], timeScales: org.orekit.time.TimeScales): ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> RinexObservation:
        """
            Parse RINEX observations messages.
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                parsed observations file
        
        
        """
        ...

class RinexObservationWriter(java.lang.AutoCloseable):
    """
    public class RinexObservationWriter extends :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable?is`
    
        Writer for Rinex observation file.
    
        As RINEX file are organized in batches of observations at some dates, these observations are cached and a new batch is
        output only when a new date appears when calling
        :meth:`~org.orekit.files.rinex.observation.RinexObservationWriter.writeObservationDataSet` or when the file is closed by
        calling the :meth:`~org.orekit.files.rinex.observation.RinexObservationWriter.close` method. Failing to call
        :meth:`~org.orekit.files.rinex.observation.RinexObservationWriter.close` would imply the last batch of measurements is
        not written. This is the reason why this class implements
        :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable?is`, so the
        :meth:`~org.orekit.files.rinex.observation.RinexObservationWriter.close` method can be called automatically in a
        :code:`try-with-resources` statement.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, appendable: java.lang.Appendable, string: str): ...
    @typing.overload
    def __init__(self, appendable: java.lang.Appendable, string: str, biFunction: typing.Union[java.util.function.BiFunction[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales, org.orekit.time.TimeScale], typing.Callable[[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales], org.orekit.time.TimeScale]], timeScales: org.orekit.time.TimeScales): ...
    def close(self) -> None: ...
    def prepareComments(self, list: java.util.List[org.orekit.files.rinex.section.RinexComment]) -> None: ...
    def setReceiverClockModel(self, clockModel: org.orekit.time.ClockModel) -> None:
        """
            Set receiver clock model.
        
            Parameters:
                receiverClockModel (:class:`~org.orekit.time.ClockModel`): receiver clock model
        
            Since:
                12.1
        
        
        """
        ...
    def writeCompleteFile(self, rinexObservation: RinexObservation) -> None: ...
    def writeHeader(self, rinexObservationHeader: RinexObservationHeader) -> None: ...
    def writeObservationDataSet(self, observationDataSet: ObservationDataSet) -> None: ...
    def writePendingRinex2Observations(self) -> None: ...
    def writePendingRinex34Observations(self) -> None: ...

class ScaleFactorCorrection:
    """
    public class ScaleFactorCorrection extends :class:`~org.orekit.files.rinex.observation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Scale Factor to be applied. Contains the scale factors of 10 applied to the data before being stored into the RINEX
        file.
    
        Since:
            12.0
    """
    def __init__(self, double: float, list: java.util.List[org.orekit.gnss.ObservationType]): ...
    def getCorrection(self) -> float:
        """
            Get the Scale Factor.
        
            Returns:
                Scale Factor
        
        
        """
        ...
    def getTypesObsScaled(self) -> java.util.List[org.orekit.gnss.ObservationType]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.observation")``.

    GlonassSatelliteChannel: typing.Type[GlonassSatelliteChannel]
    ObservationData: typing.Type[ObservationData]
    ObservationDataSet: typing.Type[ObservationDataSet]
    PhaseShiftCorrection: typing.Type[PhaseShiftCorrection]
    RinexObservation: typing.Type[RinexObservation]
    RinexObservationHeader: typing.Type[RinexObservationHeader]
    RinexObservationParser: typing.Type[RinexObservationParser]
    RinexObservationWriter: typing.Type[RinexObservationWriter]
    ScaleFactorCorrection: typing.Type[ScaleFactorCorrection]
