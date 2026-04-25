
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.regex
import org.hipparchus.geometry.euclidean.threed
import org.orekit.data
import org.orekit.files.general
import org.orekit.files.iirv.terms
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class IIRVBuilder:
    """
    Builder for IIRVVector.
    
    Since:
        13.0
    """
    def __init__(self, utc: org.orekit.time.UTCScale):
        """
        Constructs an IIRVBuilder instance with a UTC timescale and default values for all parameters.
        
        Parameters:
            utc (UTCScale): UTC time scale
        
        
        """
        ...
    _buildEphemerisFile__C = typing.TypeVar('_buildEphemerisFile__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    def buildEphemerisFile(self, timeStampedPVCoordinates: java.util.List[_buildEphemerisFile__C]) -> 'IIRVEphemerisFile':
        """
        Constructs an IIRVEphemerisFile from the inputted list of TimeStampedPVCoordinates, inferring the start year from the first coordinate's AbsoluteDate.
        
        See buildIIRVMessage for IIRVMessage construction details.
        
        Parameters:
            timeStampedPVCoordinates (List<C> timeStampedPVCoordinates): list of time-stamped position and velocity vectors to populate the message
        
        Returns:
            the newly constructed IIRVEphemerisFile containing the given coordinates
        
        
        """
        ...
    _buildIIRVMessage__C = typing.TypeVar('_buildIIRVMessage__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    def buildIIRVMessage(self, timeStampedPVCoordinates: java.util.List[_buildIIRVMessage__C]) -> 'IIRVMessage':
        """
        Constructs an IIRVMessage where each IIRVVector in initialized from the inputted list of TimeStampedPVCoordinates.
        
        Parameters:
            timeStampedPVCoordinates (List<C> timeStampedPVCoordinates): list of time-stamped position and velocity vectors to populate the message
        
        Returns:
            the newly constructed IIRVMessage containing the given coordinates
        
        
        """
        ...
    @typing.overload
    def buildVector(self, dayOfYear: org.orekit.files.iirv.terms.DayOfYearTerm, vectorEpoch: org.orekit.files.iirv.terms.VectorEpochTerm, xPosition: org.orekit.files.iirv.terms.PositionVectorComponentTerm, yPosition: org.orekit.files.iirv.terms.PositionVectorComponentTerm, zPosition: org.orekit.files.iirv.terms.PositionVectorComponentTerm, xVelocity: org.orekit.files.iirv.terms.VelocityVectorComponentTerm, yVelocity: org.orekit.files.iirv.terms.VelocityVectorComponentTerm, zVelocity: org.orekit.files.iirv.terms.VelocityVectorComponentTerm) -> 'IIRVVector':
        """
        Constructs an IIRV object using the configured parameters.
        
        Parameters:
            dayOfYear (DayOfYearTerm): Day of year, 001 to 366
            vectorEpoch (VectorEpochTerm): Vector epoch in UTC
            xPosition (PositionVectorComponentTerm): X component of the position vector [m]
            yPosition (PositionVectorComponentTerm): Y component of the position vector [m]
            zPosition (PositionVectorComponentTerm): Z component of the position vector [m]
            xVelocity (VelocityVectorComponentTerm): X component of the velocity vector [m/s]
            yVelocity (VelocityVectorComponentTerm): Y component of the velocity vector [m/s]
            zVelocity (VelocityVectorComponentTerm): Z component of the velocity vector [m/s]
        
        Returns:
            the newly constructed IIRV object
        
        """
        ...
    @typing.overload
    def buildVector(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> 'IIRVVector':
        """
        Constructs an IIRV vector using the configured parameters, with position, velocity, and time variables derived from instances of TimeStampedPVCoordinates and AbsoluteDate.
        
        Parameters:
            timeStampedPVCoordinates (TimeStampedPVCoordinates): position and velocity components at a particular epoch corresponding to the IIRV vector
        
        Returns:
            the newly constructed IIRV object at the given coordinates
        
        
        """
        ...
    def getCoordinateSystem(self) -> org.orekit.files.iirv.terms.CoordinateSystemTerm:
        """
        Gets the current CoordinateSystemTerm value.
        
        Returns:
            the current CoordinateSystemTerm value.
        
        
        """
        ...
    def getCrossSectionalArea(self) -> org.orekit.files.iirv.terms.CrossSectionalAreaTerm:
        """
        Gets the current CrossSectionalAreaTerm value.
        
        Returns:
            the current CrossSectionalAreaTerm value.
        
        
        """
        ...
    def getDataSource(self) -> org.orekit.files.iirv.terms.DataSourceTerm:
        """
        Gets the current DataSourceTerm value.
        
        Returns:
            the current DataSourceTerm value.
        
        
        """
        ...
    def getDragCoefficient(self) -> org.orekit.files.iirv.terms.DragCoefficientTerm:
        """
        Gets the current DragCoefficientTerm value.
        
        Returns:
            the current DragCoefficientTerm value.
        
        
        """
        ...
    def getMass(self) -> org.orekit.files.iirv.terms.MassTerm:
        """
        Gets the current MassTerm value.
        
        Returns:
            the current MassTerm value.
        
        
        """
        ...
    def getMessageClass(self) -> org.orekit.files.iirv.terms.MessageClassTerm:
        """
        Gets the current MessageClassTerm value.
        
        Returns:
            the current MessageClassTerm value.
        
        
        """
        ...
    def getMessageID(self) -> org.orekit.files.iirv.terms.MessageIDTerm:
        """
        Gets the current MessageIDTerm value.
        
        Returns:
            the current MessageIDTerm value.
        
        
        """
        ...
    def getMessageSource(self) -> org.orekit.files.iirv.terms.MessageSourceTerm:
        """
        Gets the current MessageSourceTerm value.
        
        Returns:
            the current MessageSourceTerm value.
        
        
        """
        ...
    def getMessageType(self) -> org.orekit.files.iirv.terms.MessageTypeTerm:
        """
        Gets the current MessageTypeTerm value.
        
        Returns:
            the current MessageTypeTerm value.
        
        
        """
        ...
    def getOriginIdentification(self) -> org.orekit.files.iirv.terms.OriginIdentificationTerm:
        """
        Gets the current OriginIdentificationTerm value.
        
        Returns:
            the current OriginIdentificationTerm value.
        
        
        """
        ...
    def getOriginatorRoutingIndicator(self) -> org.orekit.files.iirv.terms.OriginatorRoutingIndicatorTerm:
        """
        Gets the current OriginatorRoutingIndicatorTerm value.
        
        Returns:
            the current OriginatorRoutingIndicatorTerm value.
        
        
        """
        ...
    def getRoutingIndicator(self) -> org.orekit.files.iirv.terms.RoutingIndicatorTerm:
        """
        Gets the current RoutingIndicatorTerm value.
        
        Returns:
            the current RoutingIndicatorTerm value.
        
        
        """
        ...
    def getSatelliteID(self) -> str:
        """
        Returns the satellite ID (set to the value of the VehicleIdCodeTerm).
        
        Returns:
            the satellite ID
        
        
        """
        ...
    def getSequenceNumber(self) -> org.orekit.files.iirv.terms.SequenceNumberTerm:
        """
        Gets the current SequenceNumberTerm value.
        
        Returns:
            the current SequenceNumberTerm value.
        
        
        """
        ...
    def getSolarReflectivityCoefficient(self) -> org.orekit.files.iirv.terms.SolarReflectivityCoefficientTerm:
        """
        Gets the current SolarReflectivityCoefficientTerm value.
        
        Returns:
            the current SolarReflectivityCoefficientTerm value.
        
        
        """
        ...
    def getSupportIdCode(self) -> org.orekit.files.iirv.terms.SupportIdCodeTerm:
        """
        Gets the current SupportIdCodeTerm value.
        
        Returns:
            the current SupportIdCodeTerm value.
        
        
        """
        ...
    def getVectorType(self) -> org.orekit.files.iirv.terms.VectorTypeTerm:
        """
        Gets the current VectorTypeTerm value.
        
        Returns:
            the current VectorTypeTerm value.
        
        
        """
        ...
    def getVehicleIdCode(self) -> org.orekit.files.iirv.terms.VehicleIdCodeTerm:
        """
        Gets the current VehicleIdCodeTerm value.
        
        Returns:
            the current VehicleIdCodeTerm value.
        
        
        """
        ...
    @typing.overload
    def setCoordinateSystem(self, string: str) -> None:
        """
        Parameters:
            coordinateSystem (CoordinateSystemTerm): coordinate system term value for the IIRV message
        
        Overrides the default CoordinateSystem attribute for the IIRVVector object being built.
        
        Parameters:
            coordinateSystem (String): coordinate system term value for the IIRV message
        
        Overrides the default CoordinateSystem attribute for the IIRVVector object being built.
        
        Parameters:
            coordinateSystem (long): coordinate system term value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setCoordinateSystem(self, long: int) -> None: ...
    @typing.overload
    def setCoordinateSystem(self, coordinateSystemTerm: org.orekit.files.iirv.terms.CoordinateSystemTerm) -> None: ...
    @typing.overload
    def setCrossSectionalArea(self, double: float) -> None:
        """
        IIRVVector object being built.
        
        Units: m^2
        
        Parameters:
            crossSectionalArea (CrossSectionalAreaTerm): cross-sectional area value (m^2) for the IIRV message
        
        Overrides the default CrossSectionalAreaTerm attribute for the IIRVVector object being built.
        
        Units: m^2
        
        See
        
        Parameters:
            crossSectionalArea (String): cross-sectional area value (m^2) for the IIRV message
        
        Overrides the default CrossSectionalAreaTerm attribute for the IIRVVector object being built.
        
        Units: m^2
        
        See
        
        Parameters:
            crossSectionalArea (double): cross-sectional area value (m^2) for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setCrossSectionalArea(self, string: str) -> None: ...
    @typing.overload
    def setCrossSectionalArea(self, crossSectionalAreaTerm: org.orekit.files.iirv.terms.CrossSectionalAreaTerm) -> None: ...
    @typing.overload
    def setDataSource(self, string: str) -> None:
        """
        Parameters:
            dataSource (DataSourceTerm): data source term value for the IIRV message
        
        Overrides the default DataSource attribute for the IIRVVector object being built.
        
        Parameters:
            dataSource (long): data source term value for the IIRV message
        
        Overrides the default DataSource attribute for the IIRVVector object being built.
        
        Parameters:
            dataSource (String): data source term value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setDataSource(self, long: int) -> None: ...
    @typing.overload
    def setDataSource(self, dataSourceTerm: org.orekit.files.iirv.terms.DataSourceTerm) -> None: ...
    @typing.overload
    def setDragCoefficient(self, double: float) -> None:
        """
        IIRVVector object being built.
        
        Units: dimensionless
        
        Parameters:
            dragCoefficient (DragCoefficientTerm): drag coefficient value (dimensionless) for the IIRV message
        
        Overrides the default DragCoefficientTerm attribute for the IIRVVector object being built.
        
        Units: dimensionless
        
        See
        
        Parameters:
            dragCoefficient (String): drag coefficient value (dimensionless) for the IIRV message
        
        Overrides the default DragCoefficientTerm attribute for the IIRVVector object being built.
        
        Units: dimensionless
        
        See
        
        Parameters:
            dragCoefficient (double): drag coefficient value (dimensionless) for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setDragCoefficient(self, string: str) -> None: ...
    @typing.overload
    def setDragCoefficient(self, dragCoefficientTerm: org.orekit.files.iirv.terms.DragCoefficientTerm) -> None: ...
    @typing.overload
    def setMass(self, double: float) -> None:
        """
        Units: kg
        
        Parameters:
            mass (MassTerm): mass value (kg) for the IIRV message
        
        Overrides the default Mass attribute for the IIRVVector object being built.
        
        Units: kg
        
        Parameters:
            mass (String): mass value (kg) for the IIRV message
        
        Overrides the default Mass attribute for the IIRVVector object being built.
        
        Units: kg
        
        Parameters:
            mass (double): mass value (kg) for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setMass(self, string: str) -> None: ...
    @typing.overload
    def setMass(self, massTerm: org.orekit.files.iirv.terms.MassTerm) -> None: ...
    @typing.overload
    def setMessageClass(self, string: str) -> None:
        """
        Parameters:
            messageClass (MessageClassTerm): message class value for the IIRV message
        
        Overrides the default MessageClass attribute for the IIRVVector object being built.
        
        Parameters:
            messageClass (String): message class value for the IIRV message
        
        Overrides the default MessageClass attribute for the IIRVVector object being built.
        
        Parameters:
            messageClass (long): message class value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setMessageClass(self, long: int) -> None: ...
    @typing.overload
    def setMessageClass(self, messageClassTerm: org.orekit.files.iirv.terms.MessageClassTerm) -> None: ...
    @typing.overload
    def setMessageID(self, string: str) -> None:
        """
        Parameters:
            messageID (MessageIDTerm): message ID value for the IIRV message
        
        Overrides the default MessageID attribute for the IIRVVector object being built.
        
        Parameters:
            messageID (String): message ID value for the IIRV message
        
        Overrides the default MessageID attribute for the IIRVVector object being built.
        
        Parameters:
            messageID (long): message ID value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setMessageID(self, long: int) -> None: ...
    @typing.overload
    def setMessageID(self, messageIDTerm: org.orekit.files.iirv.terms.MessageIDTerm) -> None: ...
    @typing.overload
    def setMessageSource(self, string: str) -> None:
        """
        IIRVVector object being built.
        
        Parameters:
            messageSource (String): MessageSourceTerm for the IIRV message
        
        Overrides the default MessageSourceTerm attribute for the IIRVVector object being built.
        
        Parameters:
            messageSource (MessageSourceTerm): MessageSourceTerm for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setMessageSource(self, messageSourceTerm: org.orekit.files.iirv.terms.MessageSourceTerm) -> None: ...
    @typing.overload
    def setMessageType(self, string: str) -> None:
        """
        IIRVVector object being built.
        
        Parameters:
            messageType (String): MessageTypeTerm for the IIRV message
        
        Overrides the default MessageTypeTerm attribute for the IIRVVector object being built.
        
        Parameters:
            messageType (MessageTypeTerm): MessageTypeTerm for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setMessageType(self, messageTypeTerm: org.orekit.files.iirv.terms.MessageTypeTerm) -> None: ...
    @typing.overload
    def setOriginIdentification(self, string: str) -> None:
        """
        built.
        
        Parameters:
            originIdentification (OriginIdentificationTerm): origin identification value for the IIRV message
        
        Overrides the default OriginIdentification attribute for the IIRVVector object being built.
        
        Parameters:
            originIdentification (String): origin identification value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setOriginIdentification(self, originIdentificationTerm: org.orekit.files.iirv.terms.OriginIdentificationTerm) -> None: ...
    @typing.overload
    def setOriginatorRoutingIndicator(self, string: str) -> None:
        """
        IIRVVector object being built.
        
        Parameters:
            originatorRoutingIndicator (OriginatorRoutingIndicatorTerm): originator routing indicator value for the IIRV message
        
        Overrides the default OriginatorRoutingIndicatorTerm attribute for the IIRVVector object being built.
        
        See
        
        Parameters:
            originatorRoutingIndicator (String): originator routing indicator value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setOriginatorRoutingIndicator(self, originatorRoutingIndicatorTerm: org.orekit.files.iirv.terms.OriginatorRoutingIndicatorTerm) -> None: ...
    @typing.overload
    def setRoutingIndicator(self, string: str) -> None:
        """
        Parameters:
            routingIndicator (RoutingIndicatorTerm): routing indicator term value for the IIRV message
        
        Overrides the default RoutingIndicator attribute for the IIRVVector object being built.
        
        Parameters:
            routingIndicator (String): routing indicator term value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setRoutingIndicator(self, routingIndicatorTerm: org.orekit.files.iirv.terms.RoutingIndicatorTerm) -> None: ...
    @typing.overload
    def setSequenceNumber(self, string: str) -> None:
        """
        Parameters:
            sequenceNumber (SequenceNumberTerm): sequence number value for the IIRV message
        
        Overrides the default SequenceNumber attribute for the IIRVVector object being built.
        
        Parameters:
            sequenceNumber (String): sequence number value for the IIRV message
        
        Overrides the default SequenceNumber attribute for the IIRVVector object being built.
        
        Parameters:
            sequenceNumber (long): sequence number value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setSequenceNumber(self, long: int) -> None: ...
    @typing.overload
    def setSequenceNumber(self, sequenceNumberTerm: org.orekit.files.iirv.terms.SequenceNumberTerm) -> None: ...
    @typing.overload
    def setSolarReflectivityCoefficient(self, double: float) -> None:
        """
        IIRVVector object being built.
        
        Units: dimensionless
        
        Parameters:
            solarReflectivityCoefficient (SolarReflectivityCoefficientTerm): solar reflectivity coefficient value (dimensionless) for the IIRV message
        
        Overrides the default SolarReflectivityCoefficientTerm attribute for the IIRVVector object being built.
        
        Units: dimensionless
        
        See
        
        Parameters:
            solarReflectivityCoefficient (String): solar reflectivity coefficient value (dimensionless) for the IIRV message
        
        Overrides the default SolarReflectivityCoefficientTerm attribute for the IIRVVector object being built.
        
        Units: dimensionless
        
        See
        
        Parameters:
            solarReflectivityCoefficient (double): solar reflectivity coefficient value (dimensionless) for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setSolarReflectivityCoefficient(self, string: str) -> None: ...
    @typing.overload
    def setSolarReflectivityCoefficient(self, solarReflectivityCoefficientTerm: org.orekit.files.iirv.terms.SolarReflectivityCoefficientTerm) -> None: ...
    @typing.overload
    def setSupportIdCode(self, string: str) -> None:
        """
        Parameters:
            supportIdCode (SupportIdCodeTerm): support id code value for the IIRV message
        
        Overrides the default SupportIdCode attribute for the IIRVVector object being built.
        
        Parameters:
            supportIdCode (String): support id code value for the IIRV message
        
        Overrides the default SupportIdCode attribute for the IIRVVector object being built.
        
        Parameters:
            supportIdCode (long): support id code value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setSupportIdCode(self, long: int) -> None: ...
    @typing.overload
    def setSupportIdCode(self, supportIdCodeTerm: org.orekit.files.iirv.terms.SupportIdCodeTerm) -> None: ...
    @typing.overload
    def setVectorType(self, string: str) -> None:
        """
        Parameters:
            vectorType (VectorTypeTerm): vector type term value for the IIRV message
        
        Overrides the default VectorType attribute for the IIRVVector object being built.
        
        Parameters:
            vectorType (String): vector type term value for the IIRV message
        
        Overrides the default VectorType attribute for the IIRVVector object being built.
        
        Parameters:
            vectorType (long): vector type term value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setVectorType(self, long: int) -> None: ...
    @typing.overload
    def setVectorType(self, vectorTypeTerm: org.orekit.files.iirv.terms.VectorTypeTerm) -> None: ...
    @typing.overload
    def setVehicleIdCode(self, string: str) -> None:
        """
        Parameters:
            vehicleIdCode (VehicleIdCodeTerm): vehicle id code value for the IIRV message
        
        Overrides the default VehicleIdCode attribute for the IIRVVector object being built.
        
        Parameters:
            vehicleIdCode (String): vehicle id code value for the IIRV message
        
        Overrides the default VehicleIdCode attribute for the IIRVVector object being built.
        
        Parameters:
            vehicleIdCode (long): vehicle id code value for the IIRV message
        
        
        """
        ...
    @typing.overload
    def setVehicleIdCode(self, long: int) -> None: ...
    @typing.overload
    def setVehicleIdCode(self, vehicleIdCodeTerm: org.orekit.files.iirv.terms.VehicleIdCodeTerm) -> None: ...

class IIRVEphemerisFile(org.orekit.files.general.EphemerisFile[org.orekit.utils.TimeStampedPVCoordinates, 'IIRVSegment']):
    """
    Class for associating a the IIRVEphemeris ephemeris state data (obtained from an IIRVMessage) to a single satellite, identified by its IIRV VehicleIdCodeTerm.
    """
    @typing.overload
    def __init__(self, double: float, int: int, int2: int, iIRVMessage: 'IIRVMessage'): ...
    @typing.overload
    def __init__(self, int: int, iIRVMessage: 'IIRVMessage'): ...
    @typing.overload
    def __init__(self, iIRVEphemeris: 'IIRVEphemerisFile.IIRVEphemeris'): ...
    def getIIRV(self) -> 'IIRVMessage':
        """
        Gets the IIRV message containing the ephemeris data.
        
        Returns:
            IIRVMessage containing the ephemeris data.
        
        
        """
        ...
    def getIIRVEphemeris(self) -> 'IIRVEphemerisFile.IIRVEphemeris':
        """
        Gets the IIRVEphemeris associated with this file.
        
        Returns:
            IIRVEphemeris associated with this file.
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'IIRVEphemerisFile.IIRVEphemeris']:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        STK ephemeris files define ephemeris for a single satellite, so the returned map will have a single entry.
        
        Specified by: getSatellites in interface EphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...
    def getStartYear(self) -> int:
        """
        Gets the start year for this file.
        
        Returns:
            start year for this file.
        
        
        """
        ...
    class IIRVEphemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, 'IIRVSegment']):
        def __init__(self, iIRVSegment: 'IIRVSegment'): ...
        def getIIRV(self) -> 'IIRVMessage': ...
        def getId(self) -> str: ...
        def getMu(self) -> float: ...
        def getSegment(self) -> 'IIRVSegment': ...
        def getSegments(self) -> java.util.List['IIRVSegment']: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStartYear(self) -> int: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...

class IIRVFileWriter(org.orekit.files.general.EphemerisFileWriter):
    """
    An EphemerisFileWriter for generating IIRVMessage files.
    
    This class uses an inputted IIRVBuilder object to define the message metadata values that comprise an IIRV message.
    
    This class can be used to write a list of TimeStampedPVCoordinates as an IIRV file as follows:
    
    
    
     // 1. Create an IIRVBuilder class to define the spacecraft/mission metadata values
     IIRVBuilder iirvBuilder = new IIRVBuilder(TimeScalesFactory.getUTC());
     iirvBuilder.setSupportIdCode(1221);
     iirvBuilder.setDragCoefficient(2.2);
     iirvBuilder.setOriginIdentification(OriginIdentificationTerm.GSFC);
     iirvBuilder.setRoutingIndicator("MANY");
     // ... (additional fields here)
    
     // 2. Create an IIRVFileWriter with the builder object
     IIRVFileWriter writer = new IIRVFileWriter(iirvBuilder, IIRVMessage.IncludeMessageMetadata.ALL_VECTORS);
    
     // 3. Generate an IIRVEphemerisFile containing the ephemeris data
     IIRVEphemerisFile iirvFile = iirvBuilder.buildEphemerisFile(coordinates);
    
     // 4. Write to disk. Recommendation: embed the start year in the filename (year does not appear in the IIRV itself)
     String testFilename = "TestSatellite" + "_" +
          iirvFile.getStartYear() + "_" +
          iirvFile.getIIRV().get(0).getDayOfYear().toEncodedString() + "_" +
          iirvFile.getIIRV().get(0).getVectorEpoch().toEncodedString() + ".iirv";
     writer.write(testFilename, iirvFile);
      
     
    
    Since:
        13.0
    
    Also see:
        StreamingIIRVFileWriter, IIRVMessage
    """
    def __init__(self, builder: IIRVBuilder, includeMessageMetadataSetting: 'IIRVMessage.IncludeMessageMetadata'):
        """
        Constructor.
        
        Parameters:
            builder (IIRVBuilder): Builder class for IIRV
            includeMessageMetadataSetting (IncludeMessageMetadata): Setting for when message metadata terms appear in the created IIRV message
        
        
        """
        ...
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    @typing.overload
    def write(self, string: str, ephemerisFile: typing.Union[org.orekit.files.general.EphemerisFile[_write_0__C, _write_0__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, org.orekit.files.general.EphemerisFile.EphemerisSegment]]]]) -> None: ...
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: typing.Union[org.orekit.files.general.EphemerisFile[_write_1__C, _write_1__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, org.orekit.files.general.EphemerisFile.EphemerisSegment]]]]) -> None: ...

class IIRVMessage:
    """
    Container for Improved Interrange Vector (IIRV) messages, implemented as a list of sequential IIRVVector instances.
    
    The IIRV message consists of a series of sequential IIRVVectors that each contains ephemeris state data at a particular epoch. The message body is defined as:
    
    ttuuuuuuuqjjGIIRVarrrr<<≡≡
    
    vs1ciiiibbnnndoyhhmmsssssccc<<≡≡
    
    sxxxxxxxxxxxxsyyyyyyyyyyyyszzzzzzzzzzzzccc<<==
    
    sxxxxxxxxxxxxsyyyyyyyyyyyyszzzzzzzzzzzzccc<<==
    
    mmmmmmmmaaaaakkkksrrrrrrrccc<<==
    
    ITERM oooo<<==
    
    Since:
        13.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List['IIRVVector']): ...
    @typing.overload
    def __init__(self, iIRVMessage: 'IIRVMessage'): ...
    @typing.overload
    def __init__(self, *iIRVVector: 'IIRVVector'): ...
    def add(self, v: 'IIRVVector') -> None:
        """
        Adds an IIRVVector to the message (see ArrayList).
        
        Parameters:
            v (IIRVVector): IIRV vector to add to the message
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def get(self, i: int) -> 'IIRVVector':
        """
        Gets the IIRVVector located at a given index in the message.
        
        Parameters:
            i (int): index of the element to return
        
        Returns:
            element at the given index
        
        Also see:
            ArrayList
        
        
        """
        ...
    def getSatelliteID(self) -> str:
        """
        Returns the satellite ID (set to the value of the VehicleIdCodeTerm).
        
        Returns:
            the satellite ID
        
        Also see:
            VehicleIdCodeTerm
        
        
        """
        ...
    def getVectorStrings(self, includeMessageMetadataSetting: 'IIRVMessage.IncludeMessageMetadata') -> java.util.ArrayList[str]:
        """
        Converts the IIRVVectors contained in the message file into a list of their String representations.
        
        Parameters:
            includeMessageMetadataSetting (IncludeMessageMetadata): Setting for when message metadata terms appear in the created IIRV message
        
        Returns:
            list of IIRVVector strings for each vector the message
        
        Also see:
            toIIRVString
        
        
        """
        ...
    def getVectors(self) -> java.util.List['IIRVVector']:
        """
        Gets the list of sequential IIRVVector instances contained within the overall IIRV message.
        
        Returns:
            list of sequential IIRVVector instances contained within the overall IIRV message.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
        Returns true if no vectors exist in the message.
        
        Returns:
            true if no vectors exist in the message
        
        Also see:
            ArrayList
        
        
        """
        ...
    def size(self) -> int:
        """
        Returns the number of IIRV vectors contained in the message.
        
        Returns:
            number of IIRV vectors contained in the message
        
        Also see:
            ArrayList
        
        
        """
        ...
    def toMessageString(self, includeMessageMetadataSetting: 'IIRVMessage.IncludeMessageMetadata') -> str:
        """
        Converts the IIRVVectors contained in the message file into a single String, where no deliminator included between each vector (the vectors already have trailing line carriage and line returns).
        
        Parameters:
            includeMessageMetadataSetting (IncludeMessageMetadata): Setting for when message metadata terms appear in the created IIRV message
        
        Returns:
            String containing all IIRVVectors for the IIRV message
        
        Also see:
            toIIRVString
        
        
        """
        ...
    class IncludeMessageMetadata(java.lang.Enum['IIRVMessage.IncludeMessageMetadata']):
        FIRST_VECTOR_ONLY: typing.ClassVar['IIRVMessage.IncludeMessageMetadata'] = ...
        ALL_VECTORS: typing.ClassVar['IIRVMessage.IncludeMessageMetadata'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'IIRVMessage.IncludeMessageMetadata': ...
        @staticmethod
        def values() -> typing.MutableSequence['IIRVMessage.IncludeMessageMetadata']: ...

class IIRVParser(org.orekit.files.general.EphemerisFileParser[IIRVEphemerisFile]):
    """
    Parser of IIRVEphemerisFiles.
    
    Since:
        13.0
    """
    DEFAULT_INTERPOLATION_SAMPLE: typing.ClassVar[int] = ...
    """
    Default number of sample for interpolating data (See: reference documents).
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float, int: int, int2: int, uTCScale: org.orekit.time.UTCScale): ...
    @typing.overload
    def __init__(self, int: int, uTCScale: org.orekit.time.UTCScale): ...
    @typing.overload
    def parse(self, string: str) -> IIRVEphemerisFile:
        """
        Parse an ephemeris file from a data source.
        
        Specified by: parse in interface EphemerisFileParser
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed ephemeris file.
        
        Parses a string representing an IIRV message.
        
        Parameters:
            iirv (String): String representation of an IIRV message
        
        Returns:
            newly created IIRVSegment object populated with ephemeris data parsed from
            iirvVectorStrings
        
        public IIRVEphemerisFile parse (List<String> iirvVectorStrings)
        
        Parses a list of strings that comprise an IIRVMessage.
        
        Parameters:
            iirvVectorStrings (List<String> iirvVectorStrings): list of Strings that comprise an IIRVMessage
        
        Returns:
            newly created IIRVSegment object populated with ephemeris data parsed from
            iirvVectorStrings
        
        
        """
        ...
    @typing.overload
    def parse(self, list: java.util.List[str]) -> IIRVEphemerisFile: ...
    @typing.overload
    def parse(self, dataSource: org.orekit.data.DataSource) -> IIRVEphemerisFile: ...

class IIRVSegment(org.orekit.files.general.EphemerisFile.EphemerisSegment[org.orekit.utils.TimeStampedPVCoordinates]):
    """
    Ephemeris segment from an IIRV file. Each IIRV file (i.e. IIRVMessage) is defined as containing only one IIRVSegment.
    
    Since:
        13.0
    """
    @typing.overload
    def __init__(self, double: float, int: int, int2: int, iIRVMessage: IIRVMessage): ...
    @typing.overload
    def __init__(self, int: int, iIRVMessage: IIRVMessage): ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
        Get which derivatives of position are available in this ephemeris segment.
        
        While getCoordinates always returns position, velocity, and acceleration the return value from this method indicates which of those are in the ephemeris file and are actually valid.
        
        Specified by: getAvailableDerivatives in interface EphemerisSegment
        
        Returns:
            a value indicating if the file contains velocity and/or acceleration data.
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]:
        """
        Get the coordinates for this ephemeris segment in getFrame.
        
        Specified by: getCoordinates in interface EphemerisSegment
        
        Returns:
            a list of state vectors in chronological order. The coordinates are not necessarily evenly spaced in time. The value of
            getAvailableDerivatives indicates if the velocity or
            accelerations were specified in the file. Any position, velocity, or acceleration coordinates that are not specified in
            the ephemeris file are zero in the returned values.
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame for this ephemeris segment. The defining frame for getCoordinates.
        
        Specified by: getFrame in interface EphemerisSegment
        
        Returns:
            the reference frame for this segment. Never null.
        
        
        """
        ...
    def getIIRVMessage(self) -> IIRVMessage:
        """
        Gets the IIRV message for this segment.
        
        Returns:
            IIRV message for this segment
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
        Get the number of samples to use in interpolation.
        
        Specified by: getInterpolationSamples in interface EphemerisSegment
        
        Returns:
            the number of points to use for interpolation.
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the standard gravitational parameter for the satellite.
        
        Specified by: getMu in interface EphemerisSegment
        
        Returns:
            the gravitational parameter used in getPropagator, in
            m³/s².
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of this ephemeris segment.
        
        The date returned by this method is equivalent to getMinDate().
        
        Specified by: getStart in interface EphemerisSegment
        
        Returns:
            ephemeris segment start date.
        
        
        """
        ...
    def getStartYear(self) -> int:
        """
        Gets the start year for this segment.
        
        Returns:
            start year for this segment.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of this ephemeris segment.
        
        The date returned by this method is equivalent to getMaxDate().
        
        Specified by: getStop in interface EphemerisSegment
        
        Returns:
            ephemeris segment end date.
        
        
        """
        ...

class IIRVVector(java.lang.Comparable['IIRVVector']):
    LINE_SEPARATOR: typing.ClassVar[str] = ...
    LINE_1_PATTERN_METADATA_INCLUDED: typing.ClassVar[java.util.regex.Pattern] = ...
    LINE_1_PATTERN_METADATA_OMITTED: typing.ClassVar[java.util.regex.Pattern] = ...
    LINE_2_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    LINE_3_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    LINE_4_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    LINE_5_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    LINE_6_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, uTCScale: org.orekit.time.UTCScale): ...
    @typing.overload
    def __init__(self, list: java.util.List[str], uTCScale: org.orekit.time.UTCScale): ...
    @typing.overload
    def __init__(self, iIRVVector: 'IIRVVector'): ...
    @typing.overload
    def __init__(self, messageTypeTerm: org.orekit.files.iirv.terms.MessageTypeTerm, messageIDTerm: org.orekit.files.iirv.terms.MessageIDTerm, messageSourceTerm: org.orekit.files.iirv.terms.MessageSourceTerm, messageClassTerm: org.orekit.files.iirv.terms.MessageClassTerm, originIdentificationTerm: org.orekit.files.iirv.terms.OriginIdentificationTerm, routingIndicatorTerm: org.orekit.files.iirv.terms.RoutingIndicatorTerm, vectorTypeTerm: org.orekit.files.iirv.terms.VectorTypeTerm, dataSourceTerm: org.orekit.files.iirv.terms.DataSourceTerm, coordinateSystemTerm: org.orekit.files.iirv.terms.CoordinateSystemTerm, supportIdCodeTerm: org.orekit.files.iirv.terms.SupportIdCodeTerm, vehicleIdCodeTerm: org.orekit.files.iirv.terms.VehicleIdCodeTerm, sequenceNumberTerm: org.orekit.files.iirv.terms.SequenceNumberTerm, dayOfYearTerm: org.orekit.files.iirv.terms.DayOfYearTerm, vectorEpochTerm: org.orekit.files.iirv.terms.VectorEpochTerm, positionVectorComponentTerm: org.orekit.files.iirv.terms.PositionVectorComponentTerm, positionVectorComponentTerm2: org.orekit.files.iirv.terms.PositionVectorComponentTerm, positionVectorComponentTerm3: org.orekit.files.iirv.terms.PositionVectorComponentTerm, velocityVectorComponentTerm: org.orekit.files.iirv.terms.VelocityVectorComponentTerm, velocityVectorComponentTerm2: org.orekit.files.iirv.terms.VelocityVectorComponentTerm, velocityVectorComponentTerm3: org.orekit.files.iirv.terms.VelocityVectorComponentTerm, massTerm: org.orekit.files.iirv.terms.MassTerm, crossSectionalAreaTerm: org.orekit.files.iirv.terms.CrossSectionalAreaTerm, dragCoefficientTerm: org.orekit.files.iirv.terms.DragCoefficientTerm, solarReflectivityCoefficientTerm: org.orekit.files.iirv.terms.SolarReflectivityCoefficientTerm, originatorRoutingIndicatorTerm: org.orekit.files.iirv.terms.OriginatorRoutingIndicatorTerm, uTCScale: org.orekit.time.UTCScale): ...
    def buildLine1(self, boolean: bool) -> str: ...
    def buildLine2(self) -> str: ...
    def buildLine3(self) -> str: ...
    def buildLine4(self) -> str: ...
    def buildLine5(self) -> str: ...
    def buildLine6(self) -> str: ...
    def compareTo(self, iIRVVector: 'IIRVVector') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAbsoluteDate(self, int: int) -> org.orekit.time.AbsoluteDate: ...
    def getCoordinateSystem(self) -> org.orekit.files.iirv.terms.CoordinateSystemTerm: ...
    def getCrossSectionalArea(self) -> org.orekit.files.iirv.terms.CrossSectionalAreaTerm: ...
    def getDataSource(self) -> org.orekit.files.iirv.terms.DataSourceTerm: ...
    def getDayOfYear(self) -> org.orekit.files.iirv.terms.DayOfYearTerm: ...
    def getDragCoefficient(self) -> org.orekit.files.iirv.terms.DragCoefficientTerm: ...
    @typing.overload
    def getFrame(self) -> org.orekit.frames.Frame: ...
    @typing.overload
    def getFrame(self, dataContext: org.orekit.data.DataContext) -> org.orekit.frames.Frame: ...
    def getLine2CheckSum(self) -> org.orekit.files.iirv.terms.CheckSumTerm: ...
    def getLine3CheckSum(self) -> org.orekit.files.iirv.terms.CheckSumTerm: ...
    def getLine4CheckSum(self) -> org.orekit.files.iirv.terms.CheckSumTerm: ...
    def getLine5CheckSum(self) -> org.orekit.files.iirv.terms.CheckSumTerm: ...
    def getMass(self) -> org.orekit.files.iirv.terms.MassTerm: ...
    def getMessageClass(self) -> org.orekit.files.iirv.terms.MessageClassTerm: ...
    def getMessageEnd(self) -> org.orekit.files.iirv.terms.MessageEndConstantTerm: ...
    def getMessageID(self) -> org.orekit.files.iirv.terms.MessageIDTerm: ...
    def getMessageSource(self) -> org.orekit.files.iirv.terms.MessageSourceTerm: ...
    def getMessageStart(self) -> org.orekit.files.iirv.terms.MessageStartConstantTerm: ...
    def getMessageType(self) -> org.orekit.files.iirv.terms.MessageTypeTerm: ...
    def getOriginIdentification(self) -> org.orekit.files.iirv.terms.OriginIdentificationTerm: ...
    def getOriginatorRoutingIndicator(self) -> org.orekit.files.iirv.terms.OriginatorRoutingIndicatorTerm: ...
    def getPVCoordinates(self) -> org.orekit.utils.PVCoordinates: ...
    def getPositionVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def getRoutingIndicator(self) -> org.orekit.files.iirv.terms.RoutingIndicatorTerm: ...
    def getSequenceNumber(self) -> org.orekit.files.iirv.terms.SequenceNumberTerm: ...
    def getSolarReflectivityCoefficient(self) -> org.orekit.files.iirv.terms.SolarReflectivityCoefficientTerm: ...
    def getSpareTerm(self) -> org.orekit.files.iirv.terms.SpareConstantTerm: ...
    def getSupportIdCode(self) -> org.orekit.files.iirv.terms.SupportIdCodeTerm: ...
    def getTimeStampedPVCoordinates(self, int: int) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def getTransferType(self) -> org.orekit.files.iirv.terms.TransferTypeConstantTerm: ...
    def getVectorEpoch(self) -> org.orekit.files.iirv.terms.VectorEpochTerm: ...
    def getVectorType(self) -> org.orekit.files.iirv.terms.VectorTypeTerm: ...
    def getVehicleIdCode(self) -> org.orekit.files.iirv.terms.VehicleIdCodeTerm: ...
    def getVelocityVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def getXPosition(self) -> org.orekit.files.iirv.terms.PositionVectorComponentTerm: ...
    def getXVelocity(self) -> org.orekit.files.iirv.terms.VelocityVectorComponentTerm: ...
    def getYPosition(self) -> org.orekit.files.iirv.terms.PositionVectorComponentTerm: ...
    def getYVelocity(self) -> org.orekit.files.iirv.terms.VelocityVectorComponentTerm: ...
    def getZPosition(self) -> org.orekit.files.iirv.terms.PositionVectorComponentTerm: ...
    def getZVelocity(self) -> org.orekit.files.iirv.terms.VelocityVectorComponentTerm: ...
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def isFormatOK(string: str, string2: str, string3: str, string4: str, string5: str, string6: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isFormatOK(list: java.util.List[str]) -> bool: ...
    def toHumanReadableLines(self) -> java.util.List[str]: ...
    def toIIRVString(self, boolean: bool) -> str: ...
    def toIIRVStrings(self, boolean: bool) -> java.util.List[str]: ...
    def toString(self) -> str: ...
    @staticmethod
    def validateLine(int: int, string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def validateLines(string: str, string2: str, string3: str, string4: str, string5: str, string6: str, boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def validateLines(list: java.util.List[str], boolean: bool) -> None: ...

class StreamingIIRVFileWriter:
    """
    Writer class that outputs IIRVMessage data to an output stream.
    
    Since:
        13.0
    
    Also see:
        IIRVFileWriter
    """
    def __init__(self, writer: java.lang.Appendable, includeMessageMetadataSetting: IIRVMessage.IncludeMessageMetadata):
        """
        Create an IIRV writer that streams data to the given output stream.
        
        Parameters:
            writer (Appendable): the output stream for the IIRV file.
            includeMessageMetadataSetting (IncludeMessageMetadata): Setting for when message metadata terms appear in the created IIRV message
        
        
        """
        ...
    def getIncludeMessageMetadataSetting(self) -> IIRVMessage.IncludeMessageMetadata:
        """
        Gets the setting for when message metadata terms appear in the created IIRV message.
        
        Returns:
            setting for when message metadata terms appear in the created IIRV message
        
        
        """
        ...
    def writeIIRVMessage(self, iirvMessage: IIRVMessage) -> None:
        """
        Write the passed in IIRVMessage using the passed in Appendable.
        
        Parameters:
            iirvMessage (IIRVMessage): a an IIRVMessage instance populated with IIRVVector
                terms.
        
        Raises:
            IOException: if any buffer writing operations fail
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.iirv")``.

    IIRVBuilder: typing.Type[IIRVBuilder]
    IIRVEphemerisFile: typing.Type[IIRVEphemerisFile]
    IIRVFileWriter: typing.Type[IIRVFileWriter]
    IIRVMessage: typing.Type[IIRVMessage]
    IIRVParser: typing.Type[IIRVParser]
    IIRVSegment: typing.Type[IIRVSegment]
    IIRVVector: typing.Type[IIRVVector]
    StreamingIIRVFileWriter: typing.Type[StreamingIIRVFileWriter]
    terms: org.orekit.files.iirv.terms.__module_protocol__
