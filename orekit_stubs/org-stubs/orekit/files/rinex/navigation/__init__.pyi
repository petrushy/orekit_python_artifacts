
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org.orekit.data
import org.orekit.files.rinex
import org.orekit.files.rinex.section
import org.orekit.gnss
import org.orekit.propagation.analytical.gnss.data
import org.orekit.time
import org.orekit.utils.units
import typing



class IonosphericCorrectionType(java.lang.Enum['IonosphericCorrectionType']):
    """
    public enum IonosphericCorrectionType extends :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.rinex.navigation.IonosphericCorrectionType`>
    
        Ionospheric correction type.
    
        Since:
            12.0
    """
    GAL: typing.ClassVar['IonosphericCorrectionType'] = ...
    GPS: typing.ClassVar['IonosphericCorrectionType'] = ...
    QZS: typing.ClassVar['IonosphericCorrectionType'] = ...
    BDS: typing.ClassVar['IonosphericCorrectionType'] = ...
    IRN: typing.ClassVar['IonosphericCorrectionType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IonosphericCorrectionType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['IonosphericCorrectionType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (IonosphericCorrectionType c : IonosphericCorrectionType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RegionCode(java.lang.Enum['RegionCode']):
    """
    public enum RegionCode extends :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.rinex.navigation.RegionCode`>
    
        Enumerate for region code.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.files.rinex.navigation.IonosphereKlobucharMessage`
    """
    WIDE_AREA: typing.ClassVar['RegionCode'] = ...
    JAPAN: typing.ClassVar['RegionCode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RegionCode':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['RegionCode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (RegionCode c : RegionCode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RinexNavigation(org.orekit.files.rinex.RinexFile['RinexNavigationHeader']):
    """
    public class RinexNavigation extends :class:`~org.orekit.files.rinex.RinexFile`<:class:`~org.orekit.files.rinex.navigation.RinexNavigationHeader`>
    
        Represents a parsed RINEX navigation messages files.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def addBDGIMMessage(self, ionosphereBDGIMMessage: 'IonosphereBDGIMMessage') -> None:
        """
            Add an ionosphere BDGIM message.
        
            Parameters:
                bdgim (:class:`~org.orekit.files.rinex.navigation.IonosphereBDGIMMessage`): ionosphere BDGIM message
        
            Since:
                12.0
        
        
        """
        ...
    def addBeidouCivilianNavigationMessage(self, beidouCivilianNavigationMessage: org.orekit.propagation.analytical.gnss.data.BeidouCivilianNavigationMessage) -> None:
        """
            Add a Beidou navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.BeidouCivilianNavigationMessage`): message to add
        
            Since:
                12.0
        
        
        """
        ...
    def addBeidouLegacyNavigationMessage(self, beidouLegacyNavigationMessage: org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage) -> None:
        """
            Add a Beidou navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage`): message to add
        
            Since:
                12.0
        
        
        """
        ...
    def addEarthOrientationParameter(self, earthOrientationParameterMessage: 'EarthOrientationParameterMessage') -> None:
        """
            Add an Earth orientation parameter.
        
            Parameters:
                eop (:class:`~org.orekit.files.rinex.navigation.EarthOrientationParameterMessage`): Earth orientation oarameter message
        
            Since:
                12.0
        
        
        """
        ...
    def addGPSCivilianNavigationMessage(self, gPSCivilianNavigationMessage: org.orekit.propagation.analytical.gnss.data.GPSCivilianNavigationMessage) -> None:
        """
            Add a GPS civilian navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.GPSCivilianNavigationMessage`): message to add
        
            Since:
                13.0
        
        
        """
        ...
    def addGPSLegacyNavigationMessage(self, gPSLegacyNavigationMessage: org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage) -> None:
        """
            Add a GPS legacy navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage`): message to add
        
            Since:
                12.0
        
        
        """
        ...
    def addGalileoNavigationMessage(self, galileoNavigationMessage: org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage) -> None:
        """
            Add a Galileo navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage`): message to add
        
        
        """
        ...
    def addGlonassNavigationMessage(self, gLONASSNavigationMessage: org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage) -> None:
        """
            Add a Glonass navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage`): message to add
        
        
        """
        ...
    def addKlobucharMessage(self, ionosphereKlobucharMessage: 'IonosphereKlobucharMessage') -> None:
        """
            Add an ionosphere Klobuchar message.
        
            Parameters:
                klobuchar (:class:`~org.orekit.files.rinex.navigation.IonosphereKlobucharMessage`): ionosphere Klobuchar message
        
            Since:
                12.0
        
        
        """
        ...
    def addNavICL1NVNavigationMessage(self, navICL1NVNavigationMessage: org.orekit.propagation.analytical.gnss.data.NavICL1NVNavigationMessage) -> None:
        """
            Add a NavIC navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.NavICL1NVNavigationMessage`): message to add
        
        
        """
        ...
    def addNavICLegacyNavigationMessage(self, navICLegacyNavigationMessage: org.orekit.propagation.analytical.gnss.data.NavICLegacyNavigationMessage) -> None:
        """
            Add a NavIC navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.NavICLegacyNavigationMessage`): message to add
        
        
        """
        ...
    def addNequickGMessage(self, ionosphereNequickGMessage: 'IonosphereNequickGMessage') -> None:
        """
            Add an ionosphere Nequick-G message.
        
            Parameters:
                nequickG (:class:`~org.orekit.files.rinex.navigation.IonosphereNequickGMessage`): ionosphere Nequick-G message
        
            Since:
                12.0
        
        
        """
        ...
    def addQZSSCivilianNavigationMessage(self, qZSSCivilianNavigationMessage: org.orekit.propagation.analytical.gnss.data.QZSSCivilianNavigationMessage) -> None:
        """
            Add a QZSS navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.QZSSCivilianNavigationMessage`): message to add
        
            Since:
                12.0
        
        
        """
        ...
    def addQZSSLegacyNavigationMessage(self, qZSSLegacyNavigationMessage: org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage) -> None:
        """
            Add a QZSS navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage`): message to add
        
            Since:
                12.0
        
        
        """
        ...
    def addSBASNavigationMessage(self, sBASNavigationMessage: org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage) -> None:
        """
            Add a SBAS navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage`): message to add
        
        
        """
        ...
    def addSystemTimeOffset(self, systemTimeOffsetMessage: 'SystemTimeOffsetMessage') -> None:
        """
            Add a system time offset.
        
            Parameters:
                systemTimeOffset (:class:`~org.orekit.files.rinex.navigation.SystemTimeOffsetMessage`): system time offset message
        
            Since:
                12.0
        
        
        """
        ...
    def getBDGIMMessages(self) -> java.util.List['IonosphereBDGIMMessage']: ...
    @typing.overload
    def getBeidouCivilianNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.BeidouCivilianNavigationMessage]: ...
    @typing.overload
    def getBeidouCivilianNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.BeidouCivilianNavigationMessage]]: ...
    @typing.overload
    def getBeidouLegacyNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage]: ...
    @typing.overload
    def getBeidouLegacyNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.BeidouLegacyNavigationMessage]]: ...
    def getEarthOrientationParameters(self) -> java.util.List['EarthOrientationParameterMessage']: ...
    @typing.overload
    def getGPSCivilianNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GPSCivilianNavigationMessage]: ...
    @typing.overload
    def getGPSCivilianNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.GPSCivilianNavigationMessage]]: ...
    @typing.overload
    def getGPSLegacyNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage]: ...
    @typing.overload
    def getGPSLegacyNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.GPSLegacyNavigationMessage]]: ...
    @typing.overload
    def getGalileoNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage]: ...
    @typing.overload
    def getGalileoNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage]]: ...
    @typing.overload
    def getGlonassNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage]: ...
    @typing.overload
    def getGlonassNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage]]: ...
    def getKlobucharAlpha(self) -> typing.MutableSequence[float]:
        """
            Get the "alpha" ionospheric parameters.
        
            They are used to initialize the :class:`~org.orekit.models.earth.ionosphere.KlobucharIonoModel`.
        
            Returns:
                the "alpha" ionospheric parameters
        
        
        """
        ...
    def getKlobucharBeta(self) -> typing.MutableSequence[float]:
        """
            Get the "beta" ionospheric parameters.
        
            They are used to initialize the :class:`~org.orekit.models.earth.ionosphere.KlobucharIonoModel`.
        
            Returns:
                the "beta" ionospheric parameters
        
        
        """
        ...
    def getKlobucharMessages(self) -> java.util.List['IonosphereKlobucharMessage']: ...
    @typing.overload
    def getNavICL1NVNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.NavICL1NVNavigationMessage]: ...
    @typing.overload
    def getNavICL1NVNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.NavICL1NVNavigationMessage]]: ...
    @typing.overload
    def getNavICLegacyNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.NavICLegacyNavigationMessage]: ...
    @typing.overload
    def getNavICLegacyNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.NavICLegacyNavigationMessage]]: ...
    def getNeQuickAlpha(self) -> typing.MutableSequence[float]:
        """
            Get the "alpha" ionospheric parameters.
        
            They are used to initialize the :class:`~org.orekit.models.earth.ionosphere.nequick.NeQuickModel`.
        
            Returns:
                the "alpha" ionospheric parameters
        
        
        """
        ...
    def getNequickGMessages(self) -> java.util.List['IonosphereNequickGMessage']: ...
    @typing.overload
    def getQZSSCivilianNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.QZSSCivilianNavigationMessage]: ...
    @typing.overload
    def getQZSSCivilianNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.QZSSCivilianNavigationMessage]]: ...
    @typing.overload
    def getQZSSLegacyNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage]: ...
    @typing.overload
    def getQZSSLegacyNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.QZSSLegacyNavigationMessage]]: ...
    @typing.overload
    def getSBASNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage]: ...
    @typing.overload
    def getSBASNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage]]: ...
    def getSystemTimeOffsets(self) -> java.util.List['SystemTimeOffsetMessage']: ...
    def setKlobucharAlpha(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Set the "alpha" ionspheric parameters.
        
            Parameters:
                klobucharAlpha (double[]): the "alpha" ionspheric parameters to set
        
        
        """
        ...
    def setKlobucharBeta(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Set the "beta" ionospheric parameters.
        
            Parameters:
                klobucharBeta (double[]): the "beta" ionospheric parameters to set
        
        
        """
        ...
    def setNeQuickAlpha(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Set the "alpha" ionospheric parameters.
        
            Parameters:
                neQuickAlpha (double[]): the "alpha" ionospheric parameters to set
        
        
        """
        ...

class RinexNavigationHeader(org.orekit.files.rinex.section.RinexBaseHeader):
    """
    public class RinexNavigationHeader extends :class:`~org.orekit.files.rinex.section.RinexBaseHeader`
    
        Header for Rinex Navigation.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def addTimeSystemCorrections(self, timeSystemCorrection: 'TimeSystemCorrection') -> None:
        """
            Add a time system correction to the list.
        
            Parameters:
                timeSystemCorrection (:class:`~org.orekit.files.rinex.navigation.TimeSystemCorrection`): the element to add
        
        
        """
        ...
    def getIonosphericCorrectionType(self) -> IonosphericCorrectionType:
        """
            Getter for the ionospheric correction type.
        
            Returns:
                the ionospheric correction type
        
        
        """
        ...
    def getMergedFiles(self) -> int:
        """
            Getter for the number of merged files.
        
            Returns:
                the number of merged files
        
        
        """
        ...
    def getNumberOfLeapSeconds(self) -> int:
        """
            Getter for the current number of leap seconds.
        
            Returns:
                the current number of leap seconds
        
        
        """
        ...
    def getTimeSystemCorrections(self) -> java.util.List['TimeSystemCorrection']: ...
    def setIonosphericCorrectionType(self, ionosphericCorrectionType: IonosphericCorrectionType) -> None:
        """
            Setter for the ionospheric correction type.
        
            Parameters:
                ionosphericCorrectionType (:class:`~org.orekit.files.rinex.navigation.IonosphericCorrectionType`): the ionospheric correction type to set
        
        
        """
        ...
    def setMergedFiles(self, int: int) -> None:
        """
            Setter for the number of merged files.
        
            Parameters:
                mergedFiles (int): the number of merged files
        
        
        """
        ...
    def setNumberOfLeapSeconds(self, int: int) -> None:
        """
            Setter for the current number of leap seconds.
        
            Parameters:
                numberOfLeapSeconds (int): the number of leap seconds to set
        
        
        """
        ...

class RinexNavigationParser:
    """
    public class RinexNavigationParser extends :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Parser for RINEX navigation messages files.
    
        This parser handles RINEX version from 2 to 4.02.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex2.txt`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex210.txt`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex211.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex301.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex302.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex303.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex304.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex305.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex_4.00.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex_4.01.pdf`,
            :class:`~org.orekit.files.rinex.navigation.https:.files.igs.org.pub.data.format.rinex_4.02.pdf`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales): ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> RinexNavigation: ...

class SbasId(java.lang.Enum['SbasId']):
    """
    public enum SbasId extends :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.rinex.navigation.SbasId`>
    
        Enumerate for the SBAS ids.
    
        Since:
            12.0
    """
    WAAS: typing.ClassVar['SbasId'] = ...
    EGNOS: typing.ClassVar['SbasId'] = ...
    MSAS: typing.ClassVar['SbasId'] = ...
    GAGAN: typing.ClassVar['SbasId'] = ...
    SDCM: typing.ClassVar['SbasId'] = ...
    BDSBAS: typing.ClassVar['SbasId'] = ...
    SACCSA: typing.ClassVar['SbasId'] = ...
    KASS: typing.ClassVar['SbasId'] = ...
    A_SBAS: typing.ClassVar['SbasId'] = ...
    SPAN: typing.ClassVar['SbasId'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SbasId':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['SbasId']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SbasId c : SbasId.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TimeSystemCorrection:
    """
    public class TimeSystemCorrection extends :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for time system corrections.
    
        Since:
            12.0
    """
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float): ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Getter for the reference date of the time system correction polynomial.
        
            Returns:
                the reference date of the time system correction polynomial, or null for GLONASS correction, which is constant
        
        
        """
        ...
    def getTimeSystemCorrectionA0(self) -> float:
        """
            Getter for the A0 coefficient of the time system correction.
        
            deltaT = :meth:`~org.orekit.files.rinex.navigation.TimeSystemCorrection.getTimeSystemCorrectionA0` +
            :meth:`~org.orekit.files.rinex.navigation.TimeSystemCorrection.getTimeSystemCorrectionA1` * (t - tref)
        
            Returns:
                the A0 coefficient of the time system correction
        
        
        """
        ...
    def getTimeSystemCorrectionA1(self) -> float:
        """
            Getter for the A1 coefficient of the time system correction.
        
            deltaT = :meth:`~org.orekit.files.rinex.navigation.TimeSystemCorrection.getTimeSystemCorrectionA0` +
            :meth:`~org.orekit.files.rinex.navigation.TimeSystemCorrection.getTimeSystemCorrectionA1` * (t - tref)
        
            Returns:
                the A1 coefficient of the time system correction
        
        
        """
        ...
    def getTimeSystemCorrectionType(self) -> str:
        """
            Getter for the time system correction type.
        
            Returns:
                the time system correction type
        
        
        """
        ...

class TypeSvMessage:
    """
    public class TypeSvMessage extends :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for data shared by several navigation messages.
    
        Since:
            12.0
    """
    def getNavigationMessageType(self) -> str:
        """
            Get navigation message type.
        
            Returns:
                the navigation message type
        
        
        """
        ...
    def getPrn(self) -> int:
        """
            Get satellite number.
        
            Returns:
                the prn
        
        
        """
        ...
    def getSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Get satellite system.
        
            Returns:
                the system
        
        
        """
        ...

class UtcId(java.lang.Enum['UtcId']):
    """
    public enum UtcId extends :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.rinex.navigation.UtcId`>
    
        Enumerate for the UTC ids.
    
        In addition to the ids listed here, Rinex 4.01 table 23 allowed UTC(BIPM) as a possible UTC id for SBAS. This was added
        in June 2023 and Rinex 4.01 was officially published in July 2023. However, this was quickly removed, in July 2023, i.e.
        just after publication of Rinex 4.01, as directed by BIPM. It does not appear anymore in Rinex 4.02 which was officially
        published in October 2024. Due to its transient appearance in the standard, we decided to not include UTC(BIPM) in this
        enumerate.
    
        Since:
            12.0
    """
    USNO: typing.ClassVar['UtcId'] = ...
    SU: typing.ClassVar['UtcId'] = ...
    GAL: typing.ClassVar['UtcId'] = ...
    NTSC: typing.ClassVar['UtcId'] = ...
    NICT: typing.ClassVar['UtcId'] = ...
    CRL: typing.ClassVar['UtcId'] = ...
    NIST: typing.ClassVar['UtcId'] = ...
    IRN: typing.ClassVar['UtcId'] = ...
    OP: typing.ClassVar['UtcId'] = ...
    @staticmethod
    def parseUtcId(string: str) -> 'UtcId': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'UtcId':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.rinex.navigation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['UtcId']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (UtcId c : UtcId.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class EarthOrientationParameterMessage(TypeSvMessage):
    """
    public class EarthOrientationParameterMessage extends :class:`~org.orekit.files.rinex.navigation.TypeSvMessage`
    
        Container for data contained in a Earth Orientation Parameter navigation message.
    
        Since:
            12.0
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, string: str): ...
    def getDut1(self) -> float:
        """
            Get the ΔUT₁.
        
            Returns:
                the ΔUT₁ (s)
        
        
        """
        ...
    def getDut1Dot(self) -> float:
        """
            Get the ΔUT₁ first derivative.
        
            Returns:
                the ΔUT₁ first derivative (s/s)
        
        
        """
        ...
    def getDut1DotDot(self) -> float:
        """
            Get the ΔUT₁ second derivative.
        
            Returns:
                the ΔUT₁ second derivative (s/s²)
        
        
        """
        ...
    def getReferenceEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference epoch.
        
            Returns:
                the reference epoch
        
        
        """
        ...
    def getTransmissionTime(self) -> float:
        """
            Get the message transmission time.
        
            Returns:
                message transmission time
        
        
        """
        ...
    def getXp(self) -> float:
        """
            Get the X component of the pole.
        
            Returns:
                the X component of the pole (rad)
        
        
        """
        ...
    def getXpDot(self) -> float:
        """
            Get the X component of the pole first derivative.
        
            Returns:
                the X component of the pole first derivative (rad/s)
        
        
        """
        ...
    def getXpDotDot(self) -> float:
        """
            Get the X component of the pole second derivative.
        
            Returns:
                the X component of the pole second derivative (rad/s²)
        
        
        """
        ...
    def getYp(self) -> float:
        """
            Get the Y component of the pole.
        
            Returns:
                the Y component of the pole (rad)
        
        
        """
        ...
    def getYpDot(self) -> float:
        """
            Get the Y component of the pole first derivative.
        
            Returns:
                the Y component of the pole first derivative (rad/s)
        
        
        """
        ...
    def getYpDotDot(self) -> float:
        """
            Get the Y component of the pole second derivative.
        
            Returns:
                the Y component of the pole second derivative (rad/s²)
        
        
        """
        ...
    def setDut1(self, double: float) -> None:
        """
            Set the ΔUT₁.
        
            Parameters:
                dUT1 (double): ΔUT₁ (s)
        
        
        """
        ...
    def setDut1Dot(self, double: float) -> None:
        """
            Set the ΔUT₁ first derivative.
        
            Parameters:
                dUT1Dot (double): ΔUT₁ first derivative (s/s)
        
        
        """
        ...
    def setDut1DotDot(self, double: float) -> None:
        """
            Set the ΔUT₁ second derivative.
        
            Parameters:
                dUT1DotDot (double): ΔUT₁ second derivative (s/s²)
        
        
        """
        ...
    def setReferenceEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the reference epoch.
        
            Parameters:
                referenceEpoch (:class:`~org.orekit.time.AbsoluteDate`): the reference epoch to set
        
        
        """
        ...
    def setTransmissionTime(self, double: float) -> None:
        """
            Set the message transmission time.
        
            Parameters:
                transmissionTime (double): the message transmission time
        
        
        """
        ...
    def setXp(self, double: float) -> None:
        """
            Set the X component of the pole.
        
            Parameters:
                xp (double): X component of the pole (rad)
        
        
        """
        ...
    def setXpDot(self, double: float) -> None:
        """
            Set the X component of the pole first derivative.
        
            Parameters:
                xpDot (double): X component of the pole first derivative (rad/s)
        
        
        """
        ...
    def setXpDotDot(self, double: float) -> None:
        """
            Set the X component of the pole second derivative.
        
            Parameters:
                xpDotDot (double): X component of the pole second derivative (rad/s²)
        
        
        """
        ...
    def setYp(self, double: float) -> None:
        """
            Set the Y component of the pole.
        
            Parameters:
                yp (double): Y component of the pole (rad)
        
        
        """
        ...
    def setYpDot(self, double: float) -> None:
        """
            Set the Y component of the pole first derivative.
        
            Parameters:
                ypDot (double): Y component of the pole first derivative (rad/s)
        
        
        """
        ...
    def setYpDotDot(self, double: float) -> None:
        """
            Set the Y component of the pole second derivative.
        
            Parameters:
                ypDotDot (double): Y component of the pole second derivative (rad/s²)
        
        
        """
        ...

class IonosphereBaseMessage(TypeSvMessage):
    """
    public class IonosphereBaseMessage extends :class:`~org.orekit.files.rinex.navigation.TypeSvMessage`
    
        Base container for data contained in a ionosphere message.
    
        Since:
            12.0
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, string: str): ...
    def getTransmitTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the transmit time.
        
            Returns:
                the transmit time
        
        
        """
        ...
    def setTransmitTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the transmit time.
        
            Parameters:
                transmitTime (:class:`~org.orekit.time.AbsoluteDate`): the transmit time to set
        
        
        """
        ...

class SystemTimeOffsetMessage(TypeSvMessage):
    """
    public class SystemTimeOffsetMessage extends :class:`~org.orekit.files.rinex.navigation.TypeSvMessage`
    
        Container for data contained in a System Time Offset navigation message.
    
        Since:
            12.0
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, string: str): ...
    def getA0(self) -> float:
        """
            Get the constant term of the offset.
        
            Returns:
                the constant term of the offset
        
        
        """
        ...
    def getA1(self) -> float:
        """
            Get the linear term of the offset.
        
            Returns:
                the linear term of the offset
        
        
        """
        ...
    def getA2(self) -> float:
        """
            Get the quadratic term of the offset.
        
            Returns:
                the quadratic term of the offset
        
        
        """
        ...
    def getDefinedTimeSystem(self) -> org.orekit.gnss.TimeSystem:
        """
            Get the time system defined by this message.
        
            Returns:
                the time system defined by this message
        
        
        """
        ...
    def getReferenceEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference epoch.
        
            Returns:
                the reference epoch
        
        
        """
        ...
    def getReferenceTimeSystem(self) -> org.orekit.gnss.TimeSystem:
        """
            Get the time system used as a reference to define a time system.
        
            Returns:
                the time system used as a reference to define a time system
        
        
        """
        ...
    def getSbasId(self) -> SbasId:
        """
            Get the SBAS Id.
        
            Returns:
                the SBAS Id
        
        
        """
        ...
    def getTransmissionTime(self) -> float:
        """
            Get the message transmission time.
        
            Returns:
                message transmission time
        
        
        """
        ...
    def getUtcId(self) -> UtcId:
        """
            Get the UTC Id.
        
            Returns:
                the URTC Id
        
        
        """
        ...
    def setA0(self, double: float) -> None:
        """
            Set the constant term of the offset.
        
            Parameters:
                a0 (double): constant term of the offset
        
        
        """
        ...
    def setA1(self, double: float) -> None:
        """
            set the linear term of the offset.
        
            Parameters:
                a1 (double): the linear term of the offset
        
        
        """
        ...
    def setA2(self, double: float) -> None:
        """
            Set the quadratic term of the offset.
        
            Parameters:
                a2 (double): quadratic term of the offset
        
        
        """
        ...
    def setDefinedTimeSystem(self, timeSystem: org.orekit.gnss.TimeSystem) -> None:
        """
            Set the time system defined by this message.
        
            Parameters:
                definedTimeSystem (:class:`~org.orekit.gnss.TimeSystem`): the time system defined by this message
        
        
        """
        ...
    def setReferenceEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the reference epoch.
        
            Parameters:
                referenceEpoch (:class:`~org.orekit.time.AbsoluteDate`): the reference epoch to set
        
        
        """
        ...
    def setReferenceTimeSystem(self, timeSystem: org.orekit.gnss.TimeSystem) -> None:
        """
            Set the time system used as a reference to define a time system.
        
            Parameters:
                referenceTimeSystem (:class:`~org.orekit.gnss.TimeSystem`): the time system used as a reference to define a time system
        
        
        """
        ...
    def setSbasId(self, sbasId: SbasId) -> None:
        """
            Set the SBAS Id.
        
            Parameters:
                sbasId (:class:`~org.orekit.files.rinex.navigation.SbasId`): the SBAS Id to set
        
        
        """
        ...
    def setTransmissionTime(self, double: float) -> None:
        """
            Set the message transmission time.
        
            Parameters:
                transmissionTime (double): the message transmission time
        
        
        """
        ...
    def setUtcId(self, utcId: UtcId) -> None:
        """
            Set the UTC Id.
        
            Parameters:
                utcId (:class:`~org.orekit.files.rinex.navigation.UtcId`): the URC Id to set
        
        
        """
        ...

class IonosphereBDGIMMessage(IonosphereBaseMessage):
    """
    public class IonosphereBDGIMMessage extends :class:`~org.orekit.files.rinex.navigation.IonosphereBaseMessage`
    
        Container for data contained in a ionosphere BDGIM message.
    
        Since:
            12.0
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, string: str): ...
    def getAlpha(self) -> typing.MutableSequence[float]:
        """
            Get the α coefficients.
        
            Beware Orekit uses SI units here. In order to retrieve the more traditional TECu, use
            :code:`Unit.TOTAL_ELECTRON_CONTENT_UNIT.fromSI(msg.getAlpha()[i])`
        
            Returns:
                α coefficients (m⁻²)
        
            Also see:
                :meth:`~org.orekit.utils.units.Unit.TOTAL_ELECTRON_CONTENT_UNIT`
        
        
        """
        ...
    def setAlphaI(self, int: int, double: float) -> None:
        """
            Set one α coefficient.
        
            Beware Orekit uses SI units here. In order to use the more traditional TECu, use :code:`msg.setAlpha(i,
            Unit.TOTAL_ELECTRON_CONTENT_UNIT.toSI(ai))`
        
            Parameters:
                i (int): index of the coefficient
                alphaI (double): α coefficient to set (m⁻²)
        
            Also see:
                :meth:`~org.orekit.utils.units.Unit.TOTAL_ELECTRON_CONTENT_UNIT`
        
        
        """
        ...

class IonosphereKlobucharMessage(IonosphereBaseMessage):
    """
    public class IonosphereKlobucharMessage extends :class:`~org.orekit.files.rinex.navigation.IonosphereBaseMessage`
    
        Container for data contained in a ionosphere Klobuchar message.
    
        Since:
            12.0
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, string: str): ...
    def getAlpha(self) -> typing.MutableSequence[float]:
        """
            Get the α coefficients.
        
            Beware Orekit uses SI units here. In order to retrieve the more traditional s/semi-circleⁿ, use
            :code:`IonosphereKlobucharMessage.S_PER_SC_N[i].fromSI(alpha[i])`
        
            Returns:
                α coefficients (s/radⁿ)
        
            Also see:
                :code:`S_PER_SC_N`
        
        
        """
        ...
    def getBeta(self) -> typing.MutableSequence[float]:
        """
            Get the β coefficients.
        
            Beware Orekit uses SI units here. In order to retrieve the more traditional s/semi-circleⁿ, use
            :code:`IonosphereKlobucharMessage.S_PER_SC_N[i].fromSI(beta[i])`
        
            Returns:
                β coefficients (s/radⁿ)
        
            Also see:
                :code:`S_PER_SC_N`
        
        
        """
        ...
    def getRegionCode(self) -> RegionCode:
        """
            Get the region code.
        
            Returns:
                region code
        
        
        """
        ...
    def setAlphaI(self, int: int, double: float) -> None:
        """
            Set one α coefficient.
        
            Beware Orekit uses SI units here. In order to use the more traditional s/semi-circleⁿ, use :code:`setAlphaI(i,
            IonosphereKlobucharMessage.S_PER_SC_N[i].toSi(alpha[i]))`
        
            Parameters:
                i (int): index of the coefficient
                alphaI (double): α coefficient to set (s/radⁿ)
        
            Also see:
                :code:`S_PER_SC_N`
        
        
        """
        ...
    def setBetaI(self, int: int, double: float) -> None:
        """
            Set one β coefficient.
        
            Beware Orekit uses SI units here. In order to use the more traditional s/semi-circleⁿ, use :code:`setBetaI(i,
            IonosphereKlobucharMessage.S_PER_SC_N[i].toSi(beta[i]))`
        
            Parameters:
                i (int): index of the coefficient
                betaI (double): β coefficient to set (s/radⁿ)
        
            Also see:
                :code:`S_PER_SC_N`
        
        
        """
        ...
    def setRegionCode(self, regionCode: RegionCode) -> None:
        """
            Set the region code.
        
            Parameters:
                regionCode (:class:`~org.orekit.files.rinex.navigation.RegionCode`): region code
        
        
        """
        ...

class IonosphereNequickGMessage(IonosphereBaseMessage):
    """
    public class IonosphereNequickGMessage extends :class:`~org.orekit.files.rinex.navigation.IonosphereBaseMessage`
    
        Container for data contained in a ionosphere Nequick G message.
    
        Since:
            12.0
    """
    SFU: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` SFU
    
        Converter for Nequick-G aᵢ₀ parameter.
    
    """
    SFU_PER_DEG: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` SFU_PER_DEG
    
        Converter for Nequick-G aᵢ₁ parameter.
    
    """
    SFU_PER_DEG2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` SFU_PER_DEG2
    
        Converter for Nequick-G aᵢ₂ parameter.
    
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, string: str): ...
    def getAi0(self) -> float:
        """
            Get aᵢ₀.
        
            Beware Orekit uses SI units here. In order to retrieve the more traditional SFU, use
            :code:`IonosphereNequickGMessage.SFU.fromSI(msg.getAi0())`
        
            Returns:
                aᵢ₀ (W/m²/Hz)
        
            Also see:
                :meth:`~org.orekit.files.rinex.navigation.IonosphereNequickGMessage.SFU`
        
        
        """
        ...
    def getAi1(self) -> float:
        """
            Get aᵢ₁.
        
            Beware Orekit uses SI units here. In order to retrieve the more traditional SFU/deg, use
            :code:`IonosphereNequickGMessage.SFU_PAR_DEG.fromSI(msg.getAi1())`
        
            Returns:
                aᵢ₁ (W/m²/Hz/rad)
        
            Also see:
                :meth:`~org.orekit.files.rinex.navigation.IonosphereNequickGMessage.SFU_PER_DEG`
        
        
        """
        ...
    def getAi2(self) -> float:
        """
            Get aᵢ₂.
        
            Beware Orekit uses SI units here. In order to retrieve the more traditional SFU/deg², use
            :code:`IonosphereNequickGMessage.SFU_PER_DEG_2.fromSI(msg.getAi2())`
        
            Returns:
                aᵢ₂ (W/m²/Hz/rad²)
        
            Also see:
                :meth:`~org.orekit.files.rinex.navigation.IonosphereNequickGMessage.SFU_PER_DEG2`
        
        
        """
        ...
    def getFlags(self) -> int:
        """
            Get the disturbance flags.
        
            Returns:
                disturbance flags
        
        
        """
        ...
    def setAi0(self, double: float) -> None:
        """
            Set aᵢ₀.
        
            Beware Orekit uses SI units here. In order to use the more traditional SFU, use
            :code:`msg.setAi0(IonosphereNequickGMessage.SFU.toSI(ai0))`
        
            Parameters:
                ai0 (double): aᵢ₀ (W/m²/Hz)
        
            Also see:
                :meth:`~org.orekit.files.rinex.navigation.IonosphereNequickGMessage.SFU`
        
        
        """
        ...
    def setAi1(self, double: float) -> None:
        """
            Set aᵢ₁.
        
            Beware Orekit uses SI units here. In order to use the more traditional SFU/deg, use
            :code:`msg.setAi1(IonosphereNequickGMessage.SFU_PER_DEG.toSI(ai1))`
        
            Parameters:
                ai1 (double): aᵢ₁ (W/m²/Hz/rad)
        
            Also see:
                :meth:`~org.orekit.files.rinex.navigation.IonosphereNequickGMessage.SFU_PER_DEG`
        
        
        """
        ...
    def setAi2(self, double: float) -> None:
        """
            Set aᵢ₂.
        
            Beware Orekit uses SI units here. In order to use the more traditional SFU/deg², use
            :code:`msg.setAi2(IonosphereNequickGMessage.SFU_PER_DEG2.toSI(ai2))`
        
            Parameters:
                ai2 (double): aᵢ₂ (W/m²/Hz/rad²)
        
            Also see:
                :meth:`~org.orekit.files.rinex.navigation.IonosphereNequickGMessage.SFU_PER_DEG2`
        
        
        """
        ...
    def setFlags(self, int: int) -> None:
        """
            Set the disturbance flags.
        
            Parameters:
                flags (int): disturbance flags
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.navigation")``.

    EarthOrientationParameterMessage: typing.Type[EarthOrientationParameterMessage]
    IonosphereBDGIMMessage: typing.Type[IonosphereBDGIMMessage]
    IonosphereBaseMessage: typing.Type[IonosphereBaseMessage]
    IonosphereKlobucharMessage: typing.Type[IonosphereKlobucharMessage]
    IonosphereNequickGMessage: typing.Type[IonosphereNequickGMessage]
    IonosphericCorrectionType: typing.Type[IonosphericCorrectionType]
    RegionCode: typing.Type[RegionCode]
    RinexNavigation: typing.Type[RinexNavigation]
    RinexNavigationHeader: typing.Type[RinexNavigationHeader]
    RinexNavigationParser: typing.Type[RinexNavigationParser]
    SbasId: typing.Type[SbasId]
    SystemTimeOffsetMessage: typing.Type[SystemTimeOffsetMessage]
    TimeSystemCorrection: typing.Type[TimeSystemCorrection]
    TypeSvMessage: typing.Type[TypeSvMessage]
    UtcId: typing.Type[UtcId]
