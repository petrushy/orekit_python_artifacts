import java.lang
import java.net
import java.util
import org.orekit.errors
import org.orekit.gnss.metric.messages
import org.orekit.gnss.metric.parser
import typing



class Authentication(java.lang.Enum['Authentication']):
    """
    public enum Authentication extends Enum<:class:`~org.orekit.gnss.metric.ntrip.Authentication`>
    
        Enumerate for authentication method in :class:`~org.orekit.gnss.metric.ntrip.DataStreamRecord`.
    
        Since:
            11.0
    """
    NONE: typing.ClassVar['Authentication'] = ...
    BASIC: typing.ClassVar['Authentication'] = ...
    DIGEST: typing.ClassVar['Authentication'] = ...
    @staticmethod
    def getAuthentication(string: str) -> 'Authentication':
        """
            Get the authentication type corresponding to a keyword.
        
            Parameters:
                keyword (String): authentication keyword
        
            Returns:
                the authentication type corresponding to the keyword
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Authentication':
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
    def values() -> typing.List['Authentication']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (Authentication c : Authentication.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CarrierPhase(java.lang.Enum['CarrierPhase']):
    """
    public enum CarrierPhase extends Enum<:class:`~org.orekit.gnss.metric.ntrip.CarrierPhase`>
    
        Enumerate for carrier phase in :class:`~org.orekit.gnss.metric.ntrip.DataStreamRecord`.
    
        Since:
            11.0
    """
    NO: typing.ClassVar['CarrierPhase'] = ...
    L1: typing.ClassVar['CarrierPhase'] = ...
    L1_L2: typing.ClassVar['CarrierPhase'] = ...
    @staticmethod
    def getCarrierPhase(string: str) -> 'CarrierPhase':
        """
            Get the carrier phase corresponding to a code.
        
            Parameters:
                code (String): carrier phase code
        
            Returns:
                the carrier phase corresponding to the code
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CarrierPhase':
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
    def values() -> typing.List['CarrierPhase']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CarrierPhase c : CarrierPhase.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DataFormat(java.lang.Enum['DataFormat']):
    """
    public enum DataFormat extends Enum<:class:`~org.orekit.gnss.metric.ntrip.DataFormat`>
    
        Enumerate for data format in :class:`~org.orekit.gnss.metric.ntrip.DataStreamRecord`.
    
        Since:
            11.0
    """
    RTCM_2: typing.ClassVar['DataFormat'] = ...
    RTCM_3: typing.ClassVar['DataFormat'] = ...
    RTCM_SAPOS: typing.ClassVar['DataFormat'] = ...
    CMR: typing.ClassVar['DataFormat'] = ...
    CMR_PLUS: typing.ClassVar['DataFormat'] = ...
    SAPOS_ADV: typing.ClassVar['DataFormat'] = ...
    RTCA: typing.ClassVar['DataFormat'] = ...
    RAW: typing.ClassVar['DataFormat'] = ...
    RINEX: typing.ClassVar['DataFormat'] = ...
    SP3: typing.ClassVar['DataFormat'] = ...
    BINEX: typing.ClassVar['DataFormat'] = ...
    @staticmethod
    def getDataFormat(string: str) -> 'DataFormat':
        """
            Get the message type corresponding to a keyword.
        
            Parameters:
                keyword (String): data format keyword
        
            Returns:
                the message type corresponding to the keyword
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DataFormat':
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
    def values() -> typing.List['DataFormat']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (DataFormat c : DataFormat.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class GnssData:
    """
    public class GnssData extends Object
    
        GNSS data retrieved from Ntrip caster.
    
        Since:
            11.0
    """
    def __init__(self, byteArray: typing.List[int], int: int): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class MessageObserver:
    """
    public interface MessageObserver
    
        Interface for objects that needs to be notified when new encoded messages are available.
    
        Since:
            11.0
    """
    def messageAvailable(self, string: str, parsedMessage: org.orekit.gnss.metric.messages.ParsedMessage) -> None:
        """
            Notify that an encoded message is available.
        
            Beware that this method *will* be called from an internal dedicated stream-reading thread. Implementations *must* take
            to:
        
              - not perform long processing there to avoid blocking the stream-reading thread
              - take care of thread-safety when extracting data from the message
        
        
            The only filtering that can be specified when :meth:`~org.orekit.gnss.metric.ntrip.NtripClient.addObserver` an observer
            to a :class:`~org.orekit.gnss.metric.ntrip.NtripClient` is based on message type and mount point. If additional
            filtering is needed (for example on message content like satellites ids, it must be performed by the observer itself
            when notified (see example below).
        
            The recommended way to implement this method is to simply build a domain object from the message fields (for example a
            gnss propagator) and to store it in the observer class as an instance field using a null as follows:
        
            .. code-block: java
            
            
             public class GPSProvider implements PVCoordinatesProvider, RTCMMessageObserver {
            
                 private final int                                filteringId;
                 private final AtomicReference<GPSPropagator> propagator;
            
                 public void messageAvailable(String mountPoint, ParsedMessage message) {
                     MessageXXX msg = (MessageXXX) message;
                     GPSPropagator oldPropagator = propagator.get();
                     if (msg.getSatId() == filteringId) {
                         GPSPropagator newPropagator = new GPSPropagator(msg.get...(),
                                                                         msg.get...(),
                                                                         msg.get...());
                         // only set propagator if no other observer was notified
                         // while we were asleep
                         propagator.compareAndSet(oldPropagator, newPropagator);
                     }
                 }
            
                 public TimeStampedPVCoordinates getPVCoordinates(AbsoluteDate date, Frame frame) {
                     GPSPropagator lastAvailablePropagator = propagator.get();
                     // use the retrieved propagator to compute position-velocity
                 }
            
             }
             
        
            Parameters:
                mountPoint (String): mount point from which the message comes
                message (:class:`~org.orekit.gnss.metric.messages.ParsedMessage`): last available message
        
        
        """
        ...

class NavigationSystem(java.lang.Enum['NavigationSystem']):
    """
    public enum NavigationSystem extends Enum<:class:`~org.orekit.gnss.metric.ntrip.NavigationSystem`>
    
        Enumerate for navigation system in :class:`~org.orekit.gnss.metric.ntrip.DataStreamRecord`.
    
        Since:
            11.0
    """
    GPS: typing.ClassVar['NavigationSystem'] = ...
    GLO: typing.ClassVar['NavigationSystem'] = ...
    GAL: typing.ClassVar['NavigationSystem'] = ...
    BDS: typing.ClassVar['NavigationSystem'] = ...
    QZS: typing.ClassVar['NavigationSystem'] = ...
    SBAS: typing.ClassVar['NavigationSystem'] = ...
    EMPTY: typing.ClassVar['NavigationSystem'] = ...
    @staticmethod
    def getNavigationSystem(string: str) -> 'NavigationSystem':
        """
            Get the navigation system corresponding to a keyword.
        
            Parameters:
                keyword (String): navigation system keyword
        
            Returns:
                the navigation system corresponding to the keyword
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'NavigationSystem':
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
    def values() -> typing.List['NavigationSystem']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (NavigationSystem c : NavigationSystem.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class NtripClient:
    """
    public class NtripClient extends Object
    
        Source table for ntrip streams retrieval.
    
        Note that all authentication is performed automatically by just calling the standard null method to set up an
        authenticator.
    
        Since:
            11.0
    """
    DEFAULT_TIMEOUT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_TIMEOUT
    
        Default timeout for connections and reads (ms).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_PORT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_PORT
    
        Default port for ntrip communication.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_RECONNECT_DELAY: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_RECONNECT_DELAY
    
        Default delay before we reconnect after connection close (s).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_RECONNECT_DELAY_FACTOR: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_RECONNECT_DELAY_FACTOR
    
        Default factor by which reconnection delay is multiplied after each attempt.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_MAX_RECONNECT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_RECONNECT
    
        Default maximum number of reconnect a attempts without readin any data.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, int: int): ...
    def addObserver(self, int: int, string: str, messageObserver: MessageObserver) -> None:
        """
            Add an observer for an encoded messages.
        
            If messages of the specified type have already been retrieved from a stream, the observer will be immediately notified
            with the last message from each mount point (in unspecified order) as a side effect of being added.
        
            Parameters:
                typeCode (int): code for the message type (if set to 0, notification will be triggered regardless of message type)
                mountPoint (String): mountPoint from which data must come (if null, notification will be triggered regardless of mount point)
                observer (:class:`~org.orekit.gnss.metric.ntrip.MessageObserver`): observer for this message type
        
        
        """
        ...
    def checkException(self) -> None:
        """
            Check if any of the streaming thread has thrown an exception.
        
            If a streaming thread has thrown an exception, it will be rethrown here
        
        """
        ...
    def getHost(self) -> str:
        """
            Get the caster host.
        
            Returns:
                caster host
        
        
        """
        ...
    def getPort(self) -> int:
        """
            Get the port to use for connection.
        
            Returns:
                port to use for connection
        
        
        """
        ...
    def getProxy(self) -> java.net.Proxy:
        """
            Get proxy.
        
            Returns:
                proxy to use
        
        
        """
        ...
    def getSourceTable(self) -> 'SourceTable':
        """
            Get a sourcetable.
        
            Returns:
                source table from the caster
        
        
        """
        ...
    def setFix(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, double5: float) -> None:
        """
            Set GPS fix data to send as NMEA sentence to Ntrip caster if required.
        
            Parameters:
                hour (int): hour of the fix (UTC time)
                minute (int): minute of the fix (UTC time)
                second (double): second of the fix (UTC time)
                latitude (double): latitude (radians)
                longitude (double): longitude (radians)
                ellAltitude (double): altitude above ellipsoid (m)
                undulation (double): height of the geoid above ellipsoid (m)
        
        
        """
        ...
    def setProxy(self, type: java.net.Proxy.Type, string: str, int: int) -> None:
        """
            Set proxy parameters.
        
            Parameters:
                type (Proxy.Type): proxy type
                proxyHost (String): host name of the proxy (ignored if :code:`type` is :code:`Proxy.Type.DIRECT`)
                proxyPort (int): port number of the proxy (ignored if :code:`type` is :code:`Proxy.Type.DIRECT`)
        
        
        """
        ...
    def setReconnectParameters(self, double: float, double2: float, int: int) -> None:
        """
            Set Reconnect parameters.
        
            Parameters:
                delay (double): delay before we reconnect after connection close
                delayFactor (double): factor by which reconnection delay is multiplied after each attempt
                max (int): max number of reconnect a attempts without reading any data
        
        
        """
        ...
    def setTimeout(self, int: int) -> None:
        """
            Set timeout for connections and reads.
        
            Parameters:
                timeout (int): timeout for connections and reads (ms)
        
        
        """
        ...
    def startStreaming(self, string: str, type: 'Type', boolean: bool, boolean2: bool) -> None:
        """
            Connect to a mount point and start streaming data from it.
        
            This method sets up an internal dedicated thread for continuously monitoring data incoming from a mount point. When new
            complete :class:`~org.orekit.gnss.metric.messages.ParsedMessage` becomes available, the
            :class:`~org.orekit.gnss.metric.ntrip.MessageObserver` that have been registered using
            :meth:`~org.orekit.gnss.metric.ntrip.NtripClient.addObserver` method will be notified about the message.
        
            This method must be called once for each stream to monitor.
        
            Parameters:
                mountPoint (String): mount point providing the stream
                type (:class:`~org.orekit.gnss.metric.ntrip.Type`): messages type of the mount point
                requiresNMEA (boolean): if true, the mount point requires a NMEA GGA sentence in the request
                ignoreUnknownMessageTypes (boolean): if true, unknown messages types are silently ignored
        
        
        """
        ...
    def stopStreaming(self, int: int) -> None:
        """
            Stop streaming data from all connected mount points.
        
            If an exception was encountered during data streaming, it will be rethrown here
        
            Parameters:
                time (int): timeout for waiting underlying threads termination (ms)
        
        
        """
        ...

class Record:
    """
    public abstract class Record extends Object
    
        Record in source table.
    
        Since:
            11.0
    """
    def getMisc(self) -> str:
        """
            Get miscellaneous information.
        
            Returns:
                miscellaneous information
        
        
        """
        ...
    def getRecordType(self) -> 'RecordType':
        """
            Get the type of record.
        
            Returns:
                type of record
        
        
        """
        ...

class RecordType(java.lang.Enum['RecordType']):
    """
    public enum RecordType extends Enum<:class:`~org.orekit.gnss.metric.ntrip.RecordType`>
    
        Enumerate for record types in sourcetable.
    """
    STR: typing.ClassVar['RecordType'] = ...
    CAS: typing.ClassVar['RecordType'] = ...
    NET: typing.ClassVar['RecordType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RecordType':
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
    def values() -> typing.List['RecordType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (RecordType c : RecordType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SourceTable:
    """
    public class SourceTable extends Object
    
        Source table for ntrip streams retrieval.
    
        Since:
            11.0
    """
    def getCasters(self) -> java.util.List['CasterRecord']: ...
    def getDataStreams(self) -> java.util.List['DataStreamRecord']: ...
    def getNetworks(self) -> java.util.List['NetworkRecord']: ...
    def getNtripFlags(self) -> str:
        """
            Get the flags set by server.
        
            Returns:
                flags set by server
        
        
        """
        ...

class StreamMonitor(org.orekit.gnss.metric.parser.AbstractEncodedMessages, java.lang.Runnable):
    """
    public class StreamMonitor extends :class:`~org.orekit.gnss.metric.parser.AbstractEncodedMessages` implements Runnable
    
        Monitor for retrieving streamed data from one mount point.
    
        Since:
            11.0
    """
    def __init__(self, ntripClient: NtripClient, string: str, type: 'Type', boolean: bool, boolean2: bool, double: float, double2: float, int: int): ...
    def addObserver(self, int: int, messageObserver: MessageObserver) -> None:
        """
            Add an observer for encoded messages.
        
            If messages of the specified type have already been retrieved from a stream, the observer will be immediately notified
            with the last message as a side effect of being added.
        
            Parameters:
                typeCode (int): code for the message type (if set to 0, notification will be triggered regardless of message type)
                observer (:class:`~org.orekit.gnss.metric.ntrip.MessageObserver`): observer for this message type
        
        
        """
        ...
    def getException(self) -> org.orekit.errors.OrekitException:
        """
            Retrieve exception caught during monitoring.
        
            Returns:
                exception caught
        
        
        """
        ...
    def run(self) -> None:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def stopMonitoring(self) -> None:
        """
            Stop monitoring.
        
        """
        ...

class StreamedMessage:
    """
    public class StreamedMessage extends Object
    
        Container for streamed messages meta-data.
    
        Since:
            11.0
    """
    def getId(self) -> str:
        """
            Get message id.
        
            Returns:
                message id
        
        
        """
        ...
    def getRate(self) -> int:
        """
            Get refresh rate.
        
            Returns:
                refresh rate in seconds, -1 if unknown
        
        
        """
        ...

class Type(java.lang.Enum['Type']):
    """
    public enum Type extends Enum<:class:`~org.orekit.gnss.metric.ntrip.Type`>
    
        Enumerate for messages type.
    
        Since:
            11.0
    """
    RTCM: typing.ClassVar['Type'] = ...
    IGS_SSR: typing.ClassVar['Type'] = ...
    def getParser(self, list: java.util.List[int]) -> org.orekit.gnss.metric.parser.MessagesParser:
        """
            Get the message parser associated to the SSR type.
        
            Parameters:
                messages (List<Integer> messages): list of needed messages
        
            Returns:
                a configured message parser
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Type':
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
    def values() -> typing.List['Type']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (Type c : Type.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CasterRecord(Record):
    """
    public class CasterRecord extends :class:`~org.orekit.gnss.metric.ntrip.Record`
    
        Caster record in source table.
    
        Since:
            11.0
    """
    def __init__(self, string: str): ...
    def canReceiveNMEA(self) -> bool:
        """
            Check if caster can receive NMEA messages.
        
            Returns:
                true if caster can receive NMEA messages
        
        
        """
        ...
    def getCountry(self) -> str:
        """
            Get the country.
        
            Returns:
                country
        
        
        """
        ...
    def getFallbackHostOrIPAddress(self) -> str:
        """
            Get the fallback host or IP address.
        
            Returns:
                fallback host or IP address
        
        
        """
        ...
    def getFallbackPort(self) -> int:
        """
            Get the fallback port number.
        
            Returns:
                fallback port number
        
        
        """
        ...
    def getHostOrIPAddress(self) -> str:
        """
            Get the host or IP address.
        
            Returns:
                host or IP address
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
            Get the latitude.
        
            Returns:
                latitude (rad)
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
            Get the longitude.
        
            Returns:
                longitude (rad)
        
        
        """
        ...
    def getOperator(self) -> str:
        """
            Get the institution/agency/company operating the caster.
        
            Returns:
                institution/agency/company operating the caster
        
        
        """
        ...
    def getPort(self) -> int:
        """
            Get the port number.
        
            Returns:
                port number
        
        
        """
        ...
    def getRecordType(self) -> RecordType:
        """
            Get the type of record.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.ntrip.Record.getRecordType` in class :class:`~org.orekit.gnss.metric.ntrip.Record`
        
            Returns:
                type of record
        
        
        """
        ...
    def getSourceIdentifier(self) -> str:
        """
            Get the source identifier.
        
            Returns:
                source identifier
        
        
        """
        ...

class DataStreamRecord(Record):
    """
    public class DataStreamRecord extends :class:`~org.orekit.gnss.metric.ntrip.Record`
    
        Data stream record in source table.
    
        Since:
            11.0
    """
    def __init__(self, string: str): ...
    def areFeesRequired(self) -> bool:
        """
            Check if fees are required.
        
            Returns:
                true if fees are required
        
        
        """
        ...
    def getAuthentication(self) -> Authentication:
        """
            Get the authentication method.
        
            Returns:
                authentication method
        
        
        """
        ...
    def getBitRate(self) -> int:
        """
            Get the bit rate.
        
            Returns:
                bit rate
        
        
        """
        ...
    def getCarrierPhase(self) -> CarrierPhase:
        """
            Get the carrier phase.
        
            Returns:
                carrier phase
        
        
        """
        ...
    def getCompressionEncryption(self) -> str:
        """
            Get the compression/encryption algorithm applied.
        
            Returns:
                compression/encryption algorithm applied
        
        
        """
        ...
    def getCountry(self) -> str:
        """
            Get the country.
        
            Returns:
                country
        
        
        """
        ...
    def getFormat(self) -> DataFormat:
        """
            Get the data format.
        
            Returns:
                data format
        
        
        """
        ...
    def getFormatDetails(self) -> java.util.List[StreamedMessage]: ...
    def getGenerator(self) -> str:
        """
            Get the hardware or software generator.
        
            Returns:
                hardware or software generator
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
            Get the latitude.
        
            Returns:
                latitude (rad)
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
            Get the longitude.
        
            Returns:
                longitude (rad)
        
        
        """
        ...
    def getMountPoint(self) -> str:
        """
            Get the mount point.
        
            Returns:
                mount point
        
        
        """
        ...
    def getNavigationSystems(self) -> java.util.List[NavigationSystem]: ...
    def getNetwork(self) -> str:
        """
            Get the network.
        
            Returns:
                network
        
        
        """
        ...
    def getRecordType(self) -> RecordType:
        """
            Get the type of record.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.ntrip.Record.getRecordType` in class :class:`~org.orekit.gnss.metric.ntrip.Record`
        
            Returns:
                type of record
        
        
        """
        ...
    def getSourceIdentifier(self) -> str:
        """
            Get the source identifier.
        
            Returns:
                source identifier
        
        
        """
        ...
    def isNMEARequired(self) -> bool:
        """
            Check if NMEA message must be sent to caster.
        
            Returns:
                true if NMEA message must be sent to caster
        
        
        """
        ...
    def isNetworked(self) -> bool:
        """
            Check if the stream is generated from a network of stations.
        
            Returns:
                true if stream is generated from a network of stations
        
        
        """
        ...

class NetworkRecord(Record):
    """
    public class NetworkRecord extends :class:`~org.orekit.gnss.metric.ntrip.Record`
    
        Network record in source table.
    
        Since:
            11.0
    """
    def __init__(self, string: str): ...
    def areFeesRequired(self) -> bool:
        """
            Check if fees are required.
        
            Returns:
                true if fees are required
        
        
        """
        ...
    def getAuthentication(self) -> Authentication:
        """
            Get the authentication method.
        
            Returns:
                authentication method
        
        
        """
        ...
    def getNetworkIdentifier(self) -> str:
        """
            Get the network identifier.
        
            Returns:
                network identifier
        
        
        """
        ...
    def getNetworkInfoAddress(self) -> str:
        """
            Get the web address for network information.
        
            Returns:
                web address for network information
        
        
        """
        ...
    def getOperator(self) -> str:
        """
            Get the institution/agency/company operating the caster.
        
            Returns:
                institution/agency/company operating the caster
        
        
        """
        ...
    def getRecordType(self) -> RecordType:
        """
            Get the type of record.
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.ntrip.Record.getRecordType` in class :class:`~org.orekit.gnss.metric.ntrip.Record`
        
            Returns:
                type of record
        
        
        """
        ...
    def getRegistrationAddress(self) -> str:
        """
            Get the web or mail address for registration.
        
            Returns:
                web or mail address for registration
        
        
        """
        ...
    def getStreamInfoAddress(self) -> str:
        """
            Get the web address for stream information.
        
            Returns:
                web address for stream information
        
        
        """
        ...

class PythonMessageObserver(MessageObserver):
    """
    public class PythonMessageObserver extends Object implements :class:`~org.orekit.gnss.metric.ntrip.MessageObserver`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def messageAvailable(self, string: str, parsedMessage: org.orekit.gnss.metric.messages.ParsedMessage) -> None:
        """
            Notify that an encoded message is available.
        
            Beware that this method *will* be called from an internal dedicated stream-reading thread. Implementations *must* take
            to:
        
              - not perform long processing there to avoid blocking the stream-reading thread
              - take care of thread-safety when extracting data from the message
        
        
            The only filtering that can be specified when :meth:`~org.orekit.gnss.metric.ntrip.NtripClient.addObserver` an observer
            to a :class:`~org.orekit.gnss.metric.ntrip.NtripClient` is based on message type and mount point. If additional
            filtering is needed (for example on message content like satellites ids, it must be performed by the observer itself
            when notified (see example below).
        
            The recommended way to implement this method is to simply build a domain object from the message fields (for example a
            gnss propagator) and to store it in the observer class as an instance field using a null as follows:
        
            .. code-block: java
            
            
             public class GPSProvider implements PVCoordinatesProvider, RTCMMessageObserver {
            
                 private final int                                filteringId;
                 private final AtomicReference<GPSPropagator> propagator;
            
                 public void messageAvailable(String mountPoint, ParsedMessage message) {
                     MessageXXX msg = (MessageXXX) message;
                     GPSPropagator oldPropagator = propagator.get();
                     if (msg.getSatId() == filteringId) {
                         GPSPropagator newPropagator = new GPSPropagator(msg.get...(),
                                                                         msg.get...(),
                                                                         msg.get...());
                         // only set propagator if no other observer was notified
                         // while we were asleep
                         propagator.compareAndSet(oldPropagator, newPropagator);
                     }
                 }
            
                 public TimeStampedPVCoordinates getPVCoordinates(AbsoluteDate date, Frame frame) {
                     GPSPropagator lastAvailablePropagator = propagator.get();
                     // use the retrieved propagator to compute position-velocity
                 }
            
             }
             
        
            Specified by:
                :meth:`~org.orekit.gnss.metric.ntrip.MessageObserver.messageAvailable`Â in
                interfaceÂ :class:`~org.orekit.gnss.metric.ntrip.MessageObserver`
        
            Parameters:
                mountPoint (String): mount point from which the message comes
                message (:class:`~org.orekit.gnss.metric.messages.ParsedMessage`): last available message
        
        
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.ntrip")``.

    Authentication: typing.Type[Authentication]
    CarrierPhase: typing.Type[CarrierPhase]
    CasterRecord: typing.Type[CasterRecord]
    DataFormat: typing.Type[DataFormat]
    DataStreamRecord: typing.Type[DataStreamRecord]
    GnssData: typing.Type[GnssData]
    MessageObserver: typing.Type[MessageObserver]
    NavigationSystem: typing.Type[NavigationSystem]
    NetworkRecord: typing.Type[NetworkRecord]
    NtripClient: typing.Type[NtripClient]
    PythonMessageObserver: typing.Type[PythonMessageObserver]
    Record: typing.Type[Record]
    RecordType: typing.Type[RecordType]
    SourceTable: typing.Type[SourceTable]
    StreamMonitor: typing.Type[StreamMonitor]
    StreamedMessage: typing.Type[StreamedMessage]
    Type: typing.Type[Type]
