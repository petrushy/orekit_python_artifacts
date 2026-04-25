
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
    Container for association between GLONASS satellites and frequency channels (f = f₀ + k Δf with k ranging-7 to +6).
    
    Since:
        12.0
    """
    def __init__(self, satellite: org.orekit.gnss.SatInSystem, k: int):
        """
        Simple constructor.
        
        Parameters:
            satellite (SatInSystem): satellite identifier
            k (int): channel frequency multiplier (should be between -7 and +6)
        
        
        """
        ...
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
    Observation Data.
    
    Since:
        9.2
    """
    def __init__(self, observationType: org.orekit.gnss.ObservationType, value: float, lli: int, signalStrength: int):
        """
        Simple constructor.
        
        Parameters:
            observationType (ObservationType): observation type
            value (double): observed value (may be NaN if observation not available)
            lli (int): Loss of Lock Indicator
            signalStrength (int): signal strength
        
        
        """
        ...
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
            observed value (may be NaN if observation not available)
        
        
        """
        ...

class ObservationDataSet(org.orekit.time.TimeStamped):
    """
    Observation Data set.
    
    Since:
        9.2
    """
    def __init__(self, satellite: org.orekit.gnss.SatInSystem, tObs: org.orekit.time.AbsoluteDate, eventFlag: int, rcvrClkOffset: float, observationData: java.util.List[ObservationData]):
        """
        Simple constructor.
        
        Parameters:
            satellite (SatInSystem): observed satellite
            tObs (AbsoluteDate): Observation date
            eventFlag (int): event flag
            rcvrClkOffset (double): Receiver clock offset (optional, 0 by default)
            observationData (List<ObservationData> observationData): List of observation data
        
        Since:
            12.0
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
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
    def getObservationData(self) -> java.util.List[ObservationData]:
        """
        Get list of observation data.
        
        Returns:
            unmodifiable view of observation data for the observed satellite
        
        
        """
        ...
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
    Phase Shift corrections. Contains the phase shift corrections used to generate phases consistent with respect to cycle shifts.
    
    Since:
        12.0
    """
    def __init__(self, satSystemPhaseShift: org.orekit.gnss.SatelliteSystem, typeObsPhaseShift: org.orekit.gnss.ObservationType, phaseShiftCorrection: float, satsPhaseShift: java.util.List[org.orekit.gnss.SatInSystem]):
        """
        Simple constructor.
        
        Parameters:
            satSystemPhaseShift (SatelliteSystem): Satellite System
            typeObsPhaseShift (ObservationType): Carrier Phase Observation Code (may be null)
            phaseShiftCorrection (double): Phase Shift Corrections (cycles)
            satsPhaseShift (List<SatInSystem> satsPhaseShift): List of satellites involved
        
        
        """
        ...
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
    def getSatsCorrected(self) -> java.util.List[org.orekit.gnss.SatInSystem]:
        """
        Get the list of satellites involved.
        
        Returns:
            List of satellites involved (if empty, all the sats are involved)
        
        
        """
        ...
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
    Container for Rinex observation file.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def addObservationDataSet(self, observationsDataSet: ObservationDataSet) -> None:
        """
        Add an observations data set.
        
        Observations must be added chronologically, within header date range, and separated by an integer multiple of the getInterval (ideally one interval, but entries at same dates and missing entries are allowed so any non-negative integer is allowed).
        
        Parameters:
            observationsDataSet (ObservationDataSet): observations data set
        
        
        """
        ...
    def bundleByDates(self) -> java.lang.Iterable[java.util.List[ObservationDataSet]]:
        """
        Get an iterable view of observations bundled by common date.
        
        The observations are the same as the ones provided by getObservationDataSets, but instead of one single list covering the whole Rinex file, several lists are made available, all observations within each list sharing a common date
        
        Returns:
            an iterable view of observations bundled by common date
        
        Since:
            13.0
        
        Also see:
            getObservationDataSets
        
        
        """
        ...
    def extractClockModel(self, nbInterpolationPoints: int) -> org.orekit.time.SampledClockModel:
        """
        Extract the receiver clock model.
        
        Parameters:
            nbInterpolationPoints (int): number of points to use in interpolation
        
        Returns:
            extracted clock model or null if all getRcvrClkOffset are
            zero
        
        Since:
            12.1
        
        
        """
        ...
    def getObservationDataSets(self) -> java.util.List[ObservationDataSet]:
        """
        Get an unmodifiable view of the observations.
        
        Returns:
            unmodifiable view of the observations
        
        Also see:
            bundleByDates
        
        
        """
        ...

class RinexObservationHeader(org.orekit.files.rinex.section.RinexBaseHeader):
    """
    Container for Rinex observation file header.
    
    Since:
        9.2
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def addAppliedDCBS(self, appliedDCBS: org.orekit.files.rinex.AppliedDCBS) -> None:
        """
        Add applied differential code bias corrections.
        
        Parameters:
            appliedDCBS (AppliedDCBS): applied differential code bias corrections to add
        
        
        """
        ...
    def addAppliedPCVS(self, appliedPCVS: org.orekit.files.rinex.AppliedPCVS) -> None:
        """
        Add antenna center variation corrections.
        
        Parameters:
            appliedPCVS (AppliedPCVS): antenna center variation corrections
        
        
        """
        ...
    def addGlonassChannel(self, glonassChannel: GlonassSatelliteChannel) -> None:
        """
        Add GLONASS satellite/channel association.
        
        Parameters:
            glonassChannel (GlonassSatelliteChannel): GLONASS satellite/channel association
        
        Since:
            12.0
        
        
        """
        ...
    def addPhaseShiftCorrection(self, phaseShiftCorrection: PhaseShiftCorrection) -> None:
        """
        Add phase shift correction used to generate phases consistent w/r to cycle shifts.
        
        Parameters:
            phaseShiftCorrection (PhaseShiftCorrection): phase shift correction used to generate phases consistent w/r to cycle shifts
        
        
        """
        ...
    def addScaleFactorCorrection(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, scaleFactorCorrection: 'ScaleFactorCorrection') -> None:
        """
        Add scale factor correction.
        
        Parameters:
            satelliteSystem (SatelliteSystem): system to which this scaling factor applies
            scaleFactorCorrection (ScaleFactorCorrection): scale factor correction
        
        
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
        Get the code phase bias correction for GLONASS C1C signal.
        
        Returns:
            code phase bias correction for GLONASS C1C signal
        
        Since:
            12.0
        
        
        """
        ...
    def getC1pCodePhaseBias(self) -> float:
        """
        Get the code phase bias correction for GLONASS C1P signal.
        
        Returns:
            code phase bias correction for GLONASS C1P signal
        
        Since:
            12.0
        
        
        """
        ...
    def getC2cCodePhaseBias(self) -> float:
        """
        Get the code phase bias correction for GLONASS C2C signal.
        
        Returns:
            code phase bias correction for GLONASS C2C signal
        
        Since:
            12.0
        
        
        """
        ...
    def getC2pCodePhaseBias(self) -> float:
        """
        Get the code phase bias correction for GLONASS C2P signal.
        
        Returns:
            code phase bias correction for GLONASS C2P signal
        
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
    def getGlonassChannels(self) -> java.util.List[GlonassSatelliteChannel]:
        """
        Get the list of GLONASS satellite/channel associations.
        
        Returns:
            List of GLONASS satellite/channel associations
        
        Since:
            12.0
        
        
        """
        ...
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
    def getListAppliedDCBS(self) -> java.util.List[org.orekit.files.rinex.AppliedDCBS]:
        """
        Get the list of applied differential code bias corrections.
        
        Returns:
            list of applied differential code bias corrections
        
        
        """
        ...
    def getListAppliedPCVS(self) -> java.util.List[org.orekit.files.rinex.AppliedPCVS]:
        """
        Get the list of antenna center variation corrections.
        
        Returns:
            List of antenna center variation corrections
        
        
        """
        ...
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
    def getNbObsPerSat(self) -> java.util.Map[org.orekit.gnss.SatInSystem, java.util.Map[org.orekit.gnss.ObservationType, int]]:
        """
        Get an unmodifiable view of the map of number of observations per satellites.
        
        Returns:
            unmodifiable view of the map of number of observations per satellites
        
        Since:
            12.0
        
        
        """
        ...
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
    def getPhaseShiftCorrections(self) -> java.util.List[PhaseShiftCorrection]:
        """
        Get the list of phase shift correction used to generate phases consistent w/r to cycle shifts.
        
        Returns:
            List of phase shift correction used to generate phases consistent w/r to cycle shifts
        
        
        """
        ...
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
    def getScaleFactorCorrections(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> java.util.List['ScaleFactorCorrection']:
        """
        Get the list of scale factor correction.
        
        Parameters:
            satelliteSystem (SatelliteSystem): system to which this scaling factor applies
        
        Returns:
            List of scale factor correction
        
        
        """
        ...
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
    def getTypeObs(self) -> java.util.Map[org.orekit.gnss.SatelliteSystem, java.util.List[org.orekit.gnss.ObservationType]]:
        """
        Get an unmodifiable view of the map of observation types.
        
        Returns:
            unmodifiable view of the map of observation types
        
        Since:
            12.0
        
        
        """
        ...
    def setAgencyName(self, agencyName: str) -> None:
        """
        Setter for the agency name.
        
        Parameters:
            agencyName (String): the agency name to set
        
        
        """
        ...
    def setAntennaAzimuth(self, antennaAzimuth: float) -> None:
        """
        Set the azimuth of the zero direction of a fixed antenna.
        
        Parameters:
            antennaAzimuth (double): Azimuth of the zero direction of a fixed antenna
        
        
        """
        ...
    def setAntennaBSight(self, antennaBSight: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the antenna B.Sight.
        
        Parameters:
            antennaBSight (Vector3D): Antenna B.Sight
        
        
        """
        ...
    def setAntennaHeight(self, antennaHeight: float) -> None:
        """
        Set the antenna height.
        
        Parameters:
            antennaHeight (double): height of the antenna
        
        
        """
        ...
    def setAntennaNumber(self, antennaNumber: str) -> None:
        """
        Set the number of the antenna.
        
        Parameters:
            antennaNumber (String): number of the antenna
        
        
        """
        ...
    def setAntennaPhaseCenter(self, antennaPhaseCenter: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the antenna phasecenter.
        
        Parameters:
            antennaPhaseCenter (Vector3D): Antenna phasecenter
        
        
        """
        ...
    def setAntennaReferencePoint(self, refPoint: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the position of antenna reference point for antenna on vehicle.
        
        Parameters:
            refPoint (Vector3D): Position of antenna reference point for antenna on vehicle
        
        
        """
        ...
    def setAntennaType(self, antennaType: str) -> None:
        """
        Set the type of the antenna.
        
        Parameters:
            antennaType (String): type of the antenna
        
        
        """
        ...
    def setAntennaZeroDirection(self, antennaZeroDirection: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the zero direction of antenna.
        
        Parameters:
            antennaZeroDirection (Vector3D): Zero direction of antenna
        
        
        """
        ...
    def setApproxPos(self, approxPos: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the Approximate Marker Position.
        
        Parameters:
            approxPos (Vector3D): Approximate Marker Position
        
        
        """
        ...
    def setC1cCodePhaseBias(self, c1cCodePhaseBias: float) -> None:
        """
        Set the code phase bias correction for GLONASS C1C signal.
        
        Parameters:
            c1cCodePhaseBias (double): code phase bias correction for GLONASS C1C signal
        
        Since:
            12.0
        
        
        """
        ...
    def setC1pCodePhaseBias(self, c1pCodePhaseBias: float) -> None:
        """
        Set the code phase bias correction for GLONASS C1P signal.
        
        Parameters:
            c1pCodePhaseBias (double): code phase bias correction for GLONASS C1P signal
        
        Since:
            12.0
        
        
        """
        ...
    def setC2cCodePhaseBias(self, c2cCodePhaseBias: float) -> None:
        """
        Set the code phase bias correction for GLONASS C2C signal.
        
        Parameters:
            c2cCodePhaseBias (double): code phase bias correction for GLONASS C2C signal
        
        Since:
            12.0
        
        
        """
        ...
    def setC2pCodePhaseBias(self, c2pCodePhaseBias: float) -> None:
        """
        Set the code phase bias correction for GLONASS C2P signal.
        
        Parameters:
            c2pCodePhaseBias (double): code phase bias correction for GLONASS C2P signal
        
        Since:
            12.0
        
        
        """
        ...
    def setCenterMass(self, centerMass: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the current center of mass of vehicle in body fixed coordinate system.
        
        Parameters:
            centerMass (Vector3D): Current center of mass of vehicle in body fixed coordinate system
        
        
        """
        ...
    def setClockOffsetApplied(self, clockOffsetApplied: bool) -> None:
        """
        Set the application flag for realtime-derived receiver clock offset.
        
        Parameters:
            clockOffsetApplied (boolean): application flag for realtime-derived receiver clock offset
        
        Since:
            12.1
        
        
        """
        ...
    def setEccentricities(self, eccentricities: org.hipparchus.geometry.euclidean.twod.Vector2D) -> None:
        """
        Set the eccentricities of antenna center.
        
        Parameters:
            eccentricities (Vector2D): Eccentricities of antenna center
        
        
        """
        ...
    def setInterval(self, interval: float) -> None:
        """
        Set the observation interval in seconds.
        
        Parameters:
            interval (double): Observation interval in seconds
        
        
        """
        ...
    def setLeapSeconds(self, leapSeconds: int) -> None:
        """
        Set the Number of leap seconds since 6-Jan-1980.
        
        Parameters:
            leapSeconds (int): Number of leap seconds since 6-Jan-1980
        
        
        """
        ...
    def setLeapSecondsDayNum(self, leapSecondsDayNum: int) -> None:
        """
        Set the respective leap second day number.
        
        Parameters:
            leapSecondsDayNum (int): Respective leap second day number
        
        
        """
        ...
    def setLeapSecondsFuture(self, leapSecondsFuture: int) -> None:
        """
        Set the future or past leap seconds.
        
        Parameters:
            leapSecondsFuture (int): Future or past leap seconds
        
        
        """
        ...
    def setLeapSecondsWeekNum(self, leapSecondsWeekNum: int) -> None:
        """
        Set the respective leap second week number.
        
        Parameters:
            leapSecondsWeekNum (int): Respective leap second week number
        
        
        """
        ...
    def setMarkerName(self, markerName: str) -> None:
        """
        Set name of the antenna marker.
        
        Parameters:
            markerName (String): name of the antenna marker
        
        
        """
        ...
    def setMarkerNumber(self, markerNumber: str) -> None:
        """
        Set number of the antenna marker.
        
        Parameters:
            markerNumber (String): number of the antenna marker
        
        
        """
        ...
    def setMarkerType(self, markerType: str) -> None:
        """
        Set type of the antenna marker.
        
        Parameters:
            markerType (String): type of the antenna marker
        
        
        """
        ...
    def setNbObsPerSatellite(self, sat: org.orekit.gnss.SatInSystem, type: org.orekit.gnss.ObservationType, nbObs: int) -> None:
        """
        Set number of observations for a satellite.
        
        Parameters:
            sat (SatInSystem): satellite
            type (ObservationType): observation type
            nbObs (int): number of observations of this type for this satellite
        
        Since:
            12.0
        
        
        """
        ...
    def setNbSat(self, nbSat: int) -> None:
        """
        Set number of satellites.
        
        Parameters:
            nbSat (int): number of satellites
        
        Since:
            12.0
        
        
        """
        ...
    def setObservationCode(self, observationCode: str) -> None:
        """
        Set the observation code of the average phasecenter position w/r to antenna reference point.
        
        Parameters:
            observationCode (String): Observation code of the average phasecenter position w/r to antenna reference point
        
        
        """
        ...
    def setObserverName(self, observerName: str) -> None:
        """
        Set name of the observer.
        
        Parameters:
            observerName (String): name of the observer
        
        
        """
        ...
    def setPhaseCenterSystem(self, phaseCenterSystem: org.orekit.gnss.SatelliteSystem) -> None:
        """
        Set satellite system for average phase center.
        
        Parameters:
            phaseCenterSystem (SatelliteSystem): satellite system for average phase center
        
        Since:
            12.0
        
        
        """
        ...
    def setReceiverNumber(self, receiverNumber: str) -> None:
        """
        Set the number of the receiver.
        
        Parameters:
            receiverNumber (String): number of the receiver
        
        
        """
        ...
    def setReceiverType(self, receiverType: str) -> None:
        """
        Set the type of the receiver.
        
        Parameters:
            receiverType (String): type of the receiver
        
        
        """
        ...
    def setReceiverVersion(self, receiverVersion: str) -> None:
        """
        Set the version of the receiver.
        
        Parameters:
            receiverVersion (String): version of the receiver
        
        
        """
        ...
    def setSignalStrengthUnit(self, signalStrengthUnit: str) -> None:
        """
        Set the unit of the carrier to noise ratio observables.
        
        Parameters:
            signalStrengthUnit (String): Unit of the carrier to noise ratio observables
        
        
        """
        ...
    def setTFirstObs(self, firstObs: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the time of First observation record.
        
        Parameters:
            firstObs (AbsoluteDate): Time of First observation record
        
        
        """
        ...
    def setTLastObs(self, lastObs: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the time of last observation record.
        
        Parameters:
            lastObs (AbsoluteDate): Time of last observation record
        
        
        """
        ...
    def setTypeObs(self, system: org.orekit.gnss.SatelliteSystem, types: java.util.List[org.orekit.gnss.ObservationType]) -> None:
        """
        Set number of observations for a satellite.
        
        Parameters:
            system (SatelliteSystem): satellite system
            types (List<ObservationType> types): observation types
        
        Since:
            12.0
        
        
        """
        ...

class RinexObservationParser:
    """
    Parser for Rinex measurements files.
    
    Supported versions are: 2.00, 2.10, 2.11, 2.12 (unofficial), 2.20 (unofficial), 3.00, 3.01, 3.02, 3.03, 3.04, 3.05, 4.00, 4.01, and 4.02.
    
    Since:
        12.0
    
    Also see:
        txt,
        txt,
        pdf, `unofficial rinex 2.12
        <http://www.aiub.unibe.ch/download/rinex/rinex212.txt>`, `unofficial rinex 2.20
        <http://www.aiub.unibe.ch/download/rinex/rnx_leo.txt>`,
        pdf,
        pdf,
        pdf,
        pdf,
        pdf,
        pdf,
        pdf,
        pdf,
        pdf
    """
    DEFAULT_RINEX_2_NAMES: typing.ClassVar[str] = ...
    """
    Default name pattern for rinex 2 observation files.
    
    Also see:
        constant
    
    
    """
    DEFAULT_RINEX_3_NAMES: typing.ClassVar[str] = ...
    """
    Default name pattern for rinex 3 observation files.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[str, org.orekit.gnss.ObservationType], typing.Callable[[str], org.orekit.gnss.ObservationType]], biFunction: typing.Union[java.util.function.BiFunction[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales, org.orekit.time.TimeScale], typing.Callable[[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales], org.orekit.time.TimeScale]], timeScales: org.orekit.time.TimeScales): ...
    def parse(self, source: org.orekit.data.DataSource) -> RinexObservation:
        """
        Parse RINEX observations messages.
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            parsed observations file
        
        
        """
        ...

class RinexObservationWriter(java.lang.AutoCloseable):
    """
    Writer for Rinex observation file.
    
    As RINEX file are organized in batches of observations at some dates, these observations are cached and a new batch is output only when a new date appears when calling writeObservationDataSet or when the file is closed by calling the close method. Failing to call close would imply the last batch of measurements is not written. This is the reason why this class implements AutoCloseable, so the close method can be called automatically in a try-with-resources statement.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, appendable: java.lang.Appendable, string: str): ...
    @typing.overload
    def __init__(self, appendable: java.lang.Appendable, string: str, biFunction: typing.Union[java.util.function.BiFunction[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales, org.orekit.time.TimeScale], typing.Callable[[org.orekit.gnss.SatelliteSystem, org.orekit.time.TimeScales], org.orekit.time.TimeScale]], timeScales: org.orekit.time.TimeScales): ...
    def close(self) -> None:
        """
        Specified by: AutoCloseable in interface AutoCloseable
        
        Raises:
            IOException: 
        
        """
        ...
    def prepareComments(self, comments: java.util.List[org.orekit.files.rinex.section.RinexComment]) -> None:
        """
        Prepare comments to be emitted at specified lines.
        
        Parameters:
            comments (List<RinexComment> comments): comments to be emitted
        
        
        """
        ...
    def setReceiverClockModel(self, receiverClockModel: org.orekit.time.ClockModel) -> None:
        """
        Set receiver clock model.
        
        Parameters:
            receiverClockModel (ClockModel): receiver clock model
        
        Since:
            12.1
        
        
        """
        ...
    def writeCompleteFile(self, rinexObservation: RinexObservation) -> None:
        """
        Write a complete observation file.
        
        This method calls prepareComments and writeHeader once and then loops on calling writeObservationDataSet for all observation data sets in the file
        
        Parameters:
            rinexObservation (RinexObservation): Rinex observation file to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        Also see:
            writeHeader,
            writeObservationDataSet
        
        
        """
        ...
    def writeHeader(self, header: RinexObservationHeader) -> None:
        """
        Write header.
        
        This method must be called exactly once at the beginning (directly or by writeCompleteFile)
        
        Parameters:
            header (RinexObservationHeader): header to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def writeObservationDataSet(self, observationDataSet: ObservationDataSet) -> None:
        """
        Write one observation data set.
        
        Note that this writers output only regular observations, so the event flag is always set to 0
        
        Parameters:
            observationDataSet (ObservationDataSet): observation data set to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def writePendingRinex2Observations(self) -> None:
        """
        Write one observation data set in RINEX 2 format.
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def writePendingRinex34Observations(self) -> None:
        """
        Write one observation data set in RINEX 3/4 format.
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...

class ScaleFactorCorrection:
    """
    Scale Factor to be applied. Contains the scale factors of 10 applied to the data before being stored into the RINEX file.
    
    Since:
        12.0
    """
    def __init__(self, scaleFactor: float, typesObsScaleFactor: java.util.List[org.orekit.gnss.ObservationType]):
        """
        Simple constructor.
        
        Parameters:
            scaleFactor (double): Factor to divide stored observations (1,10,100,1000)
            typesObsScaleFactor (List<ObservationType> typesObsScaleFactor): List of Observations types that have been scaled
        
        
        """
        ...
    def getCorrection(self) -> float:
        """
        Get the Scale Factor.
        
        Returns:
            Scale Factor
        
        
        """
        ...
    def getTypesObsScaled(self) -> java.util.List[org.orekit.gnss.ObservationType]:
        """
        Get the list of Observation Types scaled.
        
        Returns:
            List of Observation types scaled
        
        
        """
        ...


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
