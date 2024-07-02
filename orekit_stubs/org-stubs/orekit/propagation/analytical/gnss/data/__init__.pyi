import java.lang
import org.orekit.attitudes
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss
import org.orekit.propagation.analytical.gnss
import org.orekit.propagation.numerical
import org.orekit.time
import typing



class AbstractEphemerisMessage:
    def __init__(self): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getEpochToc(self) -> org.orekit.time.AbsoluteDate: ...
    def getHealth(self) -> float: ...
    def getPRN(self) -> int: ...
    def getX(self) -> float: ...
    def getXDot(self) -> float: ...
    def getXDotDot(self) -> float: ...
    def getY(self) -> float: ...
    def getYDot(self) -> float: ...
    def getYDotDot(self) -> float: ...
    def getZ(self) -> float: ...
    def getZDot(self) -> float: ...
    def getZDotDot(self) -> float: ...
    def setDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setEpochToc(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setHealth(self, double: float) -> None: ...
    def setPRN(self, int: int) -> None: ...
    def setX(self, double: float) -> None: ...
    def setXDot(self, double: float) -> None: ...
    def setXDotDot(self, double: float) -> None: ...
    def setY(self, double: float) -> None: ...
    def setYDot(self, double: float) -> None: ...
    def setYDotDot(self, double: float) -> None: ...
    def setZ(self, double: float) -> None: ...
    def setZDot(self, double: float) -> None: ...
    def setZDotDot(self, double: float) -> None: ...

class BeidouSatelliteType(java.lang.Enum['BeidouSatelliteType']):
    RESERVED: typing.ClassVar['BeidouSatelliteType'] = ...
    GEO: typing.ClassVar['BeidouSatelliteType'] = ...
    IGSO: typing.ClassVar['BeidouSatelliteType'] = ...
    MEO: typing.ClassVar['BeidouSatelliteType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BeidouSatelliteType': ...
    @staticmethod
    def values() -> typing.List['BeidouSatelliteType']: ...

class CommonGnssData:
    def __init__(self, double: float, double2: float, int: int): ...
    def getAf0(self) -> float: ...
    def getAf1(self) -> float: ...
    def getAngularVelocity(self) -> float: ...
    def getCycleDuration(self) -> float: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getE(self) -> float: ...
    def getI0(self) -> float: ...
    def getM0(self) -> float: ...
    def getMu(self) -> float: ...
    def getOmega0(self) -> float: ...
    def getOmegaDot(self) -> float: ...
    def getPRN(self) -> int: ...
    def getPa(self) -> float: ...
    def getSma(self) -> float: ...
    def getTime(self) -> float: ...
    def getWeek(self) -> int: ...
    def setAf0(self, double: float) -> None: ...
    def setAf1(self, double: float) -> None: ...
    def setDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setE(self, double: float) -> None: ...
    def setI0(self, double: float) -> None: ...
    def setM0(self, double: float) -> None: ...
    def setOmega0(self, double: float) -> None: ...
    def setOmegaDot(self, double: float) -> None: ...
    def setPRN(self, int: int) -> None: ...
    def setPa(self, double: float) -> None: ...
    def setSma(self, double: float) -> None: ...
    def setTime(self, double: float) -> None: ...
    def setWeek(self, int: int) -> None: ...

class GLONASSOrbitalElements(org.orekit.time.TimeStamped):
    def getDeltaI(self) -> float: ...
    def getDeltaT(self) -> float: ...
    def getDeltaTDot(self) -> float: ...
    def getE(self) -> float: ...
    def getGammaN(self) -> float: ...
    def getIOD(self) -> int: ...
    def getLambda(self) -> float: ...
    def getN4(self) -> int: ...
    def getNa(self) -> int: ...
    def getPa(self) -> float: ...
    def getTN(self) -> float: ...
    def getTime(self) -> float: ...
    def getX(self) -> float: ...
    def getXDot(self) -> float: ...
    def getXDotDot(self) -> float: ...
    def getY(self) -> float: ...
    def getYDot(self) -> float: ...
    def getYDotDot(self) -> float: ...
    def getZ(self) -> float: ...
    def getZDot(self) -> float: ...
    def getZDotDot(self) -> float: ...

class GNSSClockElements(org.orekit.time.TimeStamped):
    def getAf0(self) -> float: ...
    def getAf1(self) -> float: ...
    def getAf2(self) -> float: ...
    def getCycleDuration(self) -> float: ...
    def getTGD(self) -> float: ...
    def getToc(self) -> float: ...

class GNSSConstants:
    GNSS_PI: typing.ClassVar[float] = ...
    GNSS_WEEK_IN_SECONDS: typing.ClassVar[float] = ...
    BEIDOU_MU: typing.ClassVar[float] = ...
    BEIDOU_WEEK_NB: typing.ClassVar[int] = ...
    BEIDOU_AV: typing.ClassVar[float] = ...
    GALILEO_MU: typing.ClassVar[float] = ...
    GALILEO_WEEK_NB: typing.ClassVar[int] = ...
    GALILEO_AV: typing.ClassVar[float] = ...
    GLONASS_MU: typing.ClassVar[float] = ...
    GLONASS_PI: typing.ClassVar[float] = ...
    GPS_MU: typing.ClassVar[float] = ...
    GPS_WEEK_NB: typing.ClassVar[int] = ...
    GPS_AV: typing.ClassVar[float] = ...
    IRNSS_MU: typing.ClassVar[float] = ...
    IRNSS_WEEK_NB: typing.ClassVar[int] = ...
    IRNSS_AV: typing.ClassVar[float] = ...
    QZSS_MU: typing.ClassVar[float] = ...
    QZSS_WEEK_NB: typing.ClassVar[int] = ...
    QZSS_AV: typing.ClassVar[float] = ...
    SBAS_MU: typing.ClassVar[float] = ...

class GNSSOrbitalElements(org.orekit.time.TimeStamped):
    def getAngularVelocity(self) -> float: ...
    def getCic(self) -> float: ...
    def getCis(self) -> float: ...
    def getCrc(self) -> float: ...
    def getCrs(self) -> float: ...
    def getCuc(self) -> float: ...
    def getCus(self) -> float: ...
    def getCycleDuration(self) -> float: ...
    def getE(self) -> float: ...
    def getI0(self) -> float: ...
    def getIDot(self) -> float: ...
    def getM0(self) -> float: ...
    def getMeanMotion(self) -> float: ...
    def getMu(self) -> float: ...
    def getOmega0(self) -> float: ...
    def getOmegaDot(self) -> float: ...
    def getPRN(self) -> int: ...
    def getPa(self) -> float: ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.analytical.gnss.GNSSPropagator: ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames) -> org.orekit.propagation.analytical.gnss.GNSSPropagator: ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame2: org.orekit.frames.Frame, frame3: org.orekit.frames.Frame, double: float) -> org.orekit.propagation.analytical.gnss.GNSSPropagator: ...
    def getSma(self) -> float: ...
    def getTime(self) -> float: ...
    def getWeek(self) -> int: ...

class SBASOrbitalElements(org.orekit.time.TimeStamped):
    def getAGf0(self) -> float: ...
    def getAGf1(self) -> float: ...
    def getIODN(self) -> int: ...
    def getPRN(self) -> int: ...
    def getTime(self) -> float: ...
    def getToc(self) -> float: ...
    def getWeek(self) -> int: ...
    def getX(self) -> float: ...
    def getXDot(self) -> float: ...
    def getXDotDot(self) -> float: ...
    def getY(self) -> float: ...
    def getYDot(self) -> float: ...
    def getYDotDot(self) -> float: ...
    def getZ(self) -> float: ...
    def getZDot(self) -> float: ...
    def getZDotDot(self) -> float: ...

class AbstractAlmanac(CommonGnssData, GNSSOrbitalElements):
    def __init__(self, double: float, double2: float, int: int): ...
    def getAf2(self) -> float: ...
    def getCic(self) -> float: ...
    def getCis(self) -> float: ...
    def getCrc(self) -> float: ...
    def getCrs(self) -> float: ...
    def getCuc(self) -> float: ...
    def getCus(self) -> float: ...
    def getIDot(self) -> float: ...
    def getMeanMotion(self) -> float: ...

class AbstractNavigationMessage(CommonGnssData, GNSSOrbitalElements):
    def __init__(self, double: float, double2: float, int: int): ...
    def getAf2(self) -> float: ...
    def getCic(self) -> float: ...
    def getCis(self) -> float: ...
    def getCrc(self) -> float: ...
    def getCrs(self) -> float: ...
    def getCuc(self) -> float: ...
    def getCus(self) -> float: ...
    def getDeltaN(self) -> float: ...
    def getEpochToc(self) -> org.orekit.time.AbsoluteDate: ...
    def getIDot(self) -> float: ...
    def getMeanMotion(self) -> float: ...
    def getSqrtA(self) -> float: ...
    def getTransmissionTime(self) -> float: ...
    def setAf2(self, double: float) -> None: ...
    def setCic(self, double: float) -> None: ...
    def setCis(self, double: float) -> None: ...
    def setCrc(self, double: float) -> None: ...
    def setCrs(self, double: float) -> None: ...
    def setCuc(self, double: float) -> None: ...
    def setCus(self, double: float) -> None: ...
    def setDeltaN(self, double: float) -> None: ...
    def setEpochToc(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setIDot(self, double: float) -> None: ...
    def setSqrtA(self, double: float) -> None: ...
    def setTransmissionTime(self, double: float) -> None: ...

class GLONASSAlmanac(GLONASSOrbitalElements):
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, timeScale: org.orekit.time.TimeScale): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getDeltaI(self) -> float: ...
    def getDeltaT(self) -> float: ...
    def getDeltaTDot(self) -> float: ...
    def getE(self) -> float: ...
    def getFrequencyChannel(self) -> int: ...
    def getGPS2Glo(self) -> float: ...
    def getGlo2UTC(self) -> float: ...
    def getGloOffset(self) -> float: ...
    def getHealth(self) -> int: ...
    def getLambda(self) -> float: ...
    def getN4(self) -> int: ...
    def getNa(self) -> int: ...
    def getPa(self) -> float: ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator: ...
    @typing.overload
    def getPropagator(self, dataContext: org.orekit.data.DataContext) -> org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator: ...
    @typing.overload
    def getPropagator(self, dataContext: org.orekit.data.DataContext, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, double: float) -> org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator: ...
    def getTime(self) -> float: ...

class GLONASSEphemeris(GLONASSOrbitalElements):
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getN4(self) -> int: ...
    def getNa(self) -> int: ...
    def getTime(self) -> float: ...
    def getX(self) -> float: ...
    def getXDot(self) -> float: ...
    def getXDotDot(self) -> float: ...
    def getY(self) -> float: ...
    def getYDot(self) -> float: ...
    def getYDotDot(self) -> float: ...
    def getZ(self) -> float: ...
    def getZDot(self) -> float: ...
    def getZDotDot(self) -> float: ...

class GLONASSNavigationMessage(AbstractEphemerisMessage, GLONASSOrbitalElements):
    def __init__(self): ...
    def getFrequencyNumber(self) -> int: ...
    def getGammaN(self) -> float: ...
    def getGroupDelayDifference(self) -> float: ...
    def getHealthFlags(self) -> int: ...
    @typing.overload
    def getPropagator(self, double: float) -> org.orekit.propagation.numerical.GLONASSNumericalPropagator: ...
    @typing.overload
    def getPropagator(self, double: float, dataContext: org.orekit.data.DataContext) -> org.orekit.propagation.numerical.GLONASSNumericalPropagator: ...
    @typing.overload
    def getPropagator(self, double: float, dataContext: org.orekit.data.DataContext, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame, double2: float) -> org.orekit.propagation.numerical.GLONASSNumericalPropagator: ...
    def getStatusFlags(self) -> int: ...
    def getTN(self) -> float: ...
    def getTime(self) -> float: ...
    def getURA(self) -> float: ...
    def setFrequencyNumber(self, double: float) -> None: ...
    def setGammaN(self, double: float) -> None: ...
    def setGroupDelayDifference(self, double: float) -> None: ...
    def setHealthFlags(self, double: float) -> None: ...
    def setStatusFlags(self, double: float) -> None: ...
    def setTauN(self, double: float) -> None: ...
    def setTime(self, double: float) -> None: ...
    def setURA(self, double: float) -> None: ...

class PythonSBASOrbitalElements(SBASOrbitalElements):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAGf0(self) -> float: ...
    def getAGf1(self) -> float: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getIODN(self) -> int: ...
    def getPRN(self) -> int: ...
    def getTime(self) -> float: ...
    def getToc(self) -> float: ...
    def getWeek(self) -> int: ...
    def getX(self) -> float: ...
    def getXDot(self) -> float: ...
    def getXDotDot(self) -> float: ...
    def getY(self) -> float: ...
    def getYDot(self) -> float: ...
    def getYDotDot(self) -> float: ...
    def getZ(self) -> float: ...
    def getZDot(self) -> float: ...
    def getZDotDot(self) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class SBASNavigationMessage(AbstractEphemerisMessage, SBASOrbitalElements):
    def __init__(self): ...
    def getAGf0(self) -> float: ...
    def getAGf1(self) -> float: ...
    def getIODN(self) -> int: ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.analytical.gnss.SBASPropagator: ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames) -> org.orekit.propagation.analytical.gnss.SBASPropagator: ...
    @typing.overload
    def getPropagator(self, frames: org.orekit.frames.Frames, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame2: org.orekit.frames.Frame, frame3: org.orekit.frames.Frame, double: float, double2: float) -> org.orekit.propagation.analytical.gnss.SBASPropagator: ...
    def getTime(self) -> float: ...
    def getURA(self) -> float: ...
    def getWeek(self) -> int: ...
    def setAGf0(self, double: float) -> None: ...
    def setAGf1(self, double: float) -> None: ...
    def setIODN(self, double: float) -> None: ...
    def setTime(self, double: float) -> None: ...
    def setURA(self, double: float) -> None: ...

class BeidouAlmanac(AbstractAlmanac):
    def __init__(self): ...
    def getHealth(self) -> int: ...
    def setHealth(self, int: int) -> None: ...
    @typing.overload
    def setI0(self, double: float, double2: float) -> None: ...
    @typing.overload
    def setI0(self, double: float) -> None: ...
    def setSqrtA(self, double: float) -> None: ...

class BeidouCivilianNavigationMessage(AbstractNavigationMessage):
    CNV1: typing.ClassVar[str] = ...
    CNV2: typing.ClassVar[str] = ...
    CNV3: typing.ClassVar[str] = ...
    def __init__(self, frequency: org.orekit.gnss.Frequency): ...
    def getADot(self) -> float: ...
    def getDeltaN0Dot(self) -> float: ...
    def getHealth(self) -> int: ...
    def getIODC(self) -> int: ...
    def getIODE(self) -> int: ...
    def getIntegrityFlags(self) -> int: ...
    def getIscB1CD(self) -> float: ...
    def getIscB1CP(self) -> float: ...
    def getIscB2AD(self) -> float: ...
    def getSatelliteType(self) -> BeidouSatelliteType: ...
    def getSignal(self) -> org.orekit.gnss.Frequency: ...
    def getSisaiOc1(self) -> int: ...
    def getSisaiOc2(self) -> int: ...
    def getSisaiOcb(self) -> int: ...
    def getSisaiOe(self) -> int: ...
    def getSismai(self) -> int: ...
    def getTgdB1Cp(self) -> float: ...
    def getTgdB2ap(self) -> float: ...
    def getTgdB2bI(self) -> float: ...
    def setADot(self, double: float) -> None: ...
    def setDeltaN0Dot(self, double: float) -> None: ...
    def setHealth(self, int: int) -> None: ...
    def setIODC(self, int: int) -> None: ...
    def setIODE(self, int: int) -> None: ...
    def setIntegrityFlags(self, int: int) -> None: ...
    def setIscB1CD(self, double: float) -> None: ...
    def setIscB1CP(self, double: float) -> None: ...
    def setIscB2AD(self, double: float) -> None: ...
    def setSatelliteType(self, beidouSatelliteType: BeidouSatelliteType) -> None: ...
    def setSisaiOc1(self, int: int) -> None: ...
    def setSisaiOc2(self, int: int) -> None: ...
    def setSisaiOcb(self, int: int) -> None: ...
    def setSisaiOe(self, int: int) -> None: ...
    def setSismai(self, int: int) -> None: ...
    def setTgdB1Cp(self, double: float) -> None: ...
    def setTgdB2ap(self, double: float) -> None: ...
    def setTgdB2bI(self, double: float) -> None: ...

class BeidouLegacyNavigationMessage(AbstractNavigationMessage):
    D1: typing.ClassVar[str] = ...
    D2: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getAODC(self) -> int: ...
    def getAODE(self) -> int: ...
    def getSvAccuracy(self) -> float: ...
    def getTGD1(self) -> float: ...
    def getTGD2(self) -> float: ...
    def setAODC(self, double: float) -> None: ...
    def setAODE(self, double: float) -> None: ...
    def setSvAccuracy(self, double: float) -> None: ...
    def setTGD1(self, double: float) -> None: ...
    def setTGD2(self, double: float) -> None: ...

class CivilianNavigationMessage(AbstractNavigationMessage, GNSSClockElements):
    CNAV: typing.ClassVar[str] = ...
    CNV2: typing.ClassVar[str] = ...
    def getADot(self) -> float: ...
    def getDeltaN0Dot(self) -> float: ...
    def getIscL1CA(self) -> float: ...
    def getIscL1CD(self) -> float: ...
    def getIscL1CP(self) -> float: ...
    def getIscL2C(self) -> float: ...
    def getIscL5I5(self) -> float: ...
    def getIscL5Q5(self) -> float: ...
    def getSvAccuracy(self) -> float: ...
    def getSvHealth(self) -> int: ...
    def getTGD(self) -> float: ...
    def getUraiEd(self) -> int: ...
    def getUraiNed0(self) -> int: ...
    def getUraiNed1(self) -> int: ...
    def getUraiNed2(self) -> int: ...
    def isCnv2(self) -> bool: ...
    def setADot(self, double: float) -> None: ...
    def setDeltaN0Dot(self, double: float) -> None: ...
    def setIscL1CA(self, double: float) -> None: ...
    def setIscL1CD(self, double: float) -> None: ...
    def setIscL1CP(self, double: float) -> None: ...
    def setIscL2C(self, double: float) -> None: ...
    def setIscL5I5(self, double: float) -> None: ...
    def setIscL5Q5(self, double: float) -> None: ...
    def setSvAccuracy(self, double: float) -> None: ...
    def setSvHealth(self, int: int) -> None: ...
    def setTGD(self, double: float) -> None: ...
    def setUraiEd(self, int: int) -> None: ...
    def setUraiNed0(self, int: int) -> None: ...
    def setUraiNed1(self, int: int) -> None: ...
    def setUraiNed2(self, int: int) -> None: ...

class GPSAlmanac(AbstractAlmanac, GNSSClockElements):
    def __init__(self): ...
    def getHealth(self) -> int: ...
    def getSVN(self) -> int: ...
    def getSatConfiguration(self) -> int: ...
    def getSource(self) -> str: ...
    def getTGD(self) -> float: ...
    def getURA(self) -> int: ...
    def setHealth(self, int: int) -> None: ...
    def setSVN(self, int: int) -> None: ...
    def setSatConfiguration(self, int: int) -> None: ...
    def setSource(self, string: str) -> None: ...
    def setSqrtA(self, double: float) -> None: ...
    def setURA(self, int: int) -> None: ...

class GalileoAlmanac(AbstractAlmanac):
    def __init__(self): ...
    def getHealthE1(self) -> int: ...
    def getHealthE5a(self) -> int: ...
    def getHealthE5b(self) -> int: ...
    def getIOD(self) -> int: ...
    def setDeltaInc(self, double: float) -> None: ...
    def setDeltaSqrtA(self, double: float) -> None: ...
    def setHealthE1(self, int: int) -> None: ...
    def setHealthE5a(self, int: int) -> None: ...
    def setHealthE5b(self, int: int) -> None: ...
    def setIOD(self, int: int) -> None: ...

class GalileoNavigationMessage(AbstractNavigationMessage):
    def __init__(self): ...
    def getBGDE1E5a(self) -> float: ...
    def getBGDE5bE1(self) -> float: ...
    def getDataSource(self) -> int: ...
    def getIODNav(self) -> int: ...
    def getSisa(self) -> float: ...
    def getSvHealth(self) -> float: ...
    def setBGDE1E5a(self, double: float) -> None: ...
    def setBGDE5bE1(self, double: float) -> None: ...
    def setDataSource(self, int: int) -> None: ...
    def setIODNav(self, int: int) -> None: ...
    def setSisa(self, double: float) -> None: ...
    def setSvHealth(self, double: float) -> None: ...

class IRNSSAlmanac(AbstractAlmanac):
    def __init__(self): ...
    def setSqrtA(self, double: float) -> None: ...

class IRNSSNavigationMessage(AbstractNavigationMessage):
    def __init__(self): ...
    def getIODEC(self) -> int: ...
    def getSvHealth(self) -> float: ...
    def getTGD(self) -> float: ...
    def getURA(self) -> float: ...
    def setIODEC(self, double: float) -> None: ...
    def setSvHealth(self, double: float) -> None: ...
    def setTGD(self, double: float) -> None: ...
    def setURA(self, double: float) -> None: ...

class LegacyNavigationMessage(AbstractNavigationMessage, GNSSClockElements):
    LNAV: typing.ClassVar[str] = ...
    def getFitInterval(self) -> int: ...
    def getIODC(self) -> int: ...
    def getIODE(self) -> int: ...
    def getSvAccuracy(self) -> float: ...
    def getSvHealth(self) -> int: ...
    def getTGD(self) -> float: ...
    def setFitInterval(self, int: int) -> None: ...
    def setIODC(self, int: int) -> None: ...
    def setIODE(self, double: float) -> None: ...
    def setSvAccuracy(self, double: float) -> None: ...
    def setSvHealth(self, int: int) -> None: ...
    def setTGD(self, double: float) -> None: ...

class QZSSAlmanac(AbstractAlmanac):
    def __init__(self): ...
    def getHealth(self) -> int: ...
    def getSource(self) -> str: ...
    def setHealth(self, int: int) -> None: ...
    def setSource(self, string: str) -> None: ...
    def setSqrtA(self, double: float) -> None: ...

class GPSCivilianNavigationMessage(CivilianNavigationMessage):
    def __init__(self, boolean: bool): ...

class GPSLegacyNavigationMessage(LegacyNavigationMessage):
    def __init__(self): ...

class QZSSCivilianNavigationMessage(CivilianNavigationMessage):
    def __init__(self, boolean: bool): ...

class QZSSLegacyNavigationMessage(LegacyNavigationMessage):
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.gnss.data")``.

    AbstractAlmanac: typing.Type[AbstractAlmanac]
    AbstractEphemerisMessage: typing.Type[AbstractEphemerisMessage]
    AbstractNavigationMessage: typing.Type[AbstractNavigationMessage]
    BeidouAlmanac: typing.Type[BeidouAlmanac]
    BeidouCivilianNavigationMessage: typing.Type[BeidouCivilianNavigationMessage]
    BeidouLegacyNavigationMessage: typing.Type[BeidouLegacyNavigationMessage]
    BeidouSatelliteType: typing.Type[BeidouSatelliteType]
    CivilianNavigationMessage: typing.Type[CivilianNavigationMessage]
    CommonGnssData: typing.Type[CommonGnssData]
    GLONASSAlmanac: typing.Type[GLONASSAlmanac]
    GLONASSEphemeris: typing.Type[GLONASSEphemeris]
    GLONASSNavigationMessage: typing.Type[GLONASSNavigationMessage]
    GLONASSOrbitalElements: typing.Type[GLONASSOrbitalElements]
    GNSSClockElements: typing.Type[GNSSClockElements]
    GNSSConstants: typing.Type[GNSSConstants]
    GNSSOrbitalElements: typing.Type[GNSSOrbitalElements]
    GPSAlmanac: typing.Type[GPSAlmanac]
    GPSCivilianNavigationMessage: typing.Type[GPSCivilianNavigationMessage]
    GPSLegacyNavigationMessage: typing.Type[GPSLegacyNavigationMessage]
    GalileoAlmanac: typing.Type[GalileoAlmanac]
    GalileoNavigationMessage: typing.Type[GalileoNavigationMessage]
    IRNSSAlmanac: typing.Type[IRNSSAlmanac]
    IRNSSNavigationMessage: typing.Type[IRNSSNavigationMessage]
    LegacyNavigationMessage: typing.Type[LegacyNavigationMessage]
    PythonSBASOrbitalElements: typing.Type[PythonSBASOrbitalElements]
    QZSSAlmanac: typing.Type[QZSSAlmanac]
    QZSSCivilianNavigationMessage: typing.Type[QZSSCivilianNavigationMessage]
    QZSSLegacyNavigationMessage: typing.Type[QZSSLegacyNavigationMessage]
    SBASNavigationMessage: typing.Type[SBASNavigationMessage]
    SBASOrbitalElements: typing.Type[SBASOrbitalElements]
