import java.lang
import java.util
import org.orekit.bodies
import org.orekit.data
import org.orekit.files.ccsds.utils
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class BodyFacade:
    """
    public class BodyFacade extends Object
    
        Facade in front of several center bodies in CCSDS messages.
    
        Since:
            11.0
    """
    def __init__(self, string: str, celestialBody: org.orekit.bodies.CelestialBody): ...
    def getBody(self) -> org.orekit.bodies.CelestialBody:
        """
            Get the celestial body.
        
            Returns:
                celestial body (may be null)
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the CCSDS name for the body.
        
            Returns:
                CCSDS name
        
        
        """
        ...

class CelestialBodyFrame(java.lang.Enum['CelestialBodyFrame']):
    """
    public enum CelestialBodyFrame extends Enum<:class:`~org.orekit.files.ccsds.definitions.CelestialBodyFrame`>
    
        Frames used in CCSDS Orbit Data Messages.
    
        Since:
            6.1
    """
    EME2000: typing.ClassVar['CelestialBodyFrame'] = ...
    J2000: typing.ClassVar['CelestialBodyFrame'] = ...
    GCRF: typing.ClassVar['CelestialBodyFrame'] = ...
    GRC: typing.ClassVar['CelestialBodyFrame'] = ...
    GTOD: typing.ClassVar['CelestialBodyFrame'] = ...
    ICRF: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF2014: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF2008: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF2005: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF2000: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1997: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1996: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1994: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1993: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1992: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1991: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1990: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1989: typing.ClassVar['CelestialBodyFrame'] = ...
    ITRF1988: typing.ClassVar['CelestialBodyFrame'] = ...
    MCI: typing.ClassVar['CelestialBodyFrame'] = ...
    TDR: typing.ClassVar['CelestialBodyFrame'] = ...
    TEME: typing.ClassVar['CelestialBodyFrame'] = ...
    TOD: typing.ClassVar['CelestialBodyFrame'] = ...
    def getFrame(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext) -> org.orekit.frames.Frame:
        """
            Get the frame corresponding to the CCSDS constant.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions to use
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
                dataContext (:class:`~org.orekit.data.DataContext`): to use when creating the frame.
        
            Returns:
                frame corresponding to the CCSDS constant
        
            Since:
                10.1
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of celestial body frame.
        
            Returns:
                the name of celestial body frame
        
            Since:
                11.1
        
        
        """
        ...
    @staticmethod
    def guessFrame(frame: org.orekit.frames.Frame) -> str:
        """
            Guesses names from ODM Table 5-3 and Annex A.
        
            The goal of this method is to perform the opposite mapping of
            :meth:`~org.orekit.files.ccsds.definitions.CelestialBodyFrame.getFrame`.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): a reference frame.
        
            Returns:
                the string to use in the OEM file to identify :code:`frame`.
        
        
        """
        ...
    @staticmethod
    def map(frame: org.orekit.frames.Frame) -> 'CelestialBodyFrame':
        """
            Map an Orekit frame to a CCSDS frame.
        
            The goal of this method is to perform the opposite mapping of
            :meth:`~org.orekit.files.ccsds.definitions.CelestialBodyFrame.getFrame`.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): a reference frame.
        
            Returns:
                the CCSDSFrame corresponding to the Orekit frame
        
        
        """
        ...
    @staticmethod
    def parse(string: str) -> 'CelestialBodyFrame':
        """
            Parse a CCSDS frame.
        
            Parameters:
                frameName (String): name of the frame, as the value of a CCSDS key=value line
        
            Returns:
                CCSDS frame corresponding to the name
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CelestialBodyFrame':
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
    def values() -> typing.List['CelestialBodyFrame']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CelestialBodyFrame c : CelestialBodyFrame.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CenterName(java.lang.Enum['CenterName']):
    """
    public enum CenterName extends Enum<:class:`~org.orekit.files.ccsds.definitions.CenterName`>
    
        Orbit central bodies for which a Celestial body can be created.
    
        Since:
            6.1
    """
    SOLAR_SYSTEM_BARYCENTER: typing.ClassVar['CenterName'] = ...
    SUN: typing.ClassVar['CenterName'] = ...
    MERCURY: typing.ClassVar['CenterName'] = ...
    VENUS: typing.ClassVar['CenterName'] = ...
    EARTH_MOON: typing.ClassVar['CenterName'] = ...
    EARTH: typing.ClassVar['CenterName'] = ...
    MOON: typing.ClassVar['CenterName'] = ...
    MARS: typing.ClassVar['CenterName'] = ...
    JUPITER: typing.ClassVar['CenterName'] = ...
    SATURN: typing.ClassVar['CenterName'] = ...
    URANUS: typing.ClassVar['CenterName'] = ...
    NEPTUNE: typing.ClassVar['CenterName'] = ...
    PLUTO: typing.ClassVar['CenterName'] = ...
    @typing.overload
    def getCelestialBody(self) -> org.orekit.bodies.CelestialBody:
        """
            Get the celestial body corresponding to the CCSDS constant.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                celestial body corresponding to the CCSDS constant
        
            Also see:
                :meth:`~org.orekit.files.ccsds.definitions.CenterName.getCelestialBody`
        
        """
        ...
    @typing.overload
    def getCelestialBody(self, celestialBodies: org.orekit.bodies.CelestialBodies) -> org.orekit.bodies.CelestialBody:
        """
            Get the celestial body corresponding to the CCSDS constant.
        
            Parameters:
                celestialBodies (:class:`~org.orekit.bodies.CelestialBodies`): the set of celestial bodies to use.
        
            Returns:
                celestial body corresponding to the CCSDS constant
        
            Since:
                10.1
        
        
        """
        ...
    @staticmethod
    def guessCenter(frame: org.orekit.frames.Frame) -> str:
        """
            Guess the name of the center of the reference frame.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): a reference frame for ephemeris output.
        
            Returns:
                the string to use in the OEM file to describe the origin of :code:`frame`.
        
        
        """
        ...
    @staticmethod
    def map(frame: org.orekit.frames.Frame) -> 'CenterName':
        """
            Map an Orekit frame to a CCSDS center.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): a reference frame.
        
            Returns:
                the string to use in the OEM file to describe the origin of :code:`frame`, or null if no such center can be found
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CenterName':
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
    def values() -> typing.List['CenterName']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CenterName c : CenterName.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DutyCycleType(java.lang.Enum['DutyCycleType']):
    """
    public enum DutyCycleType extends Enum<:class:`~org.orekit.files.ccsds.definitions.DutyCycleType`>
    
        Type of duty cycle used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    CONTINUOUS: typing.ClassVar['DutyCycleType'] = ...
    TIME: typing.ClassVar['DutyCycleType'] = ...
    TIME_AND_ANGLE: typing.ClassVar['DutyCycleType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DutyCycleType':
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
    def values() -> typing.List['DutyCycleType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (DutyCycleType c : DutyCycleType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ElementsType(java.lang.Enum['ElementsType']):
    """
    public enum ElementsType extends Enum<:class:`~org.orekit.files.ccsds.definitions.ElementsType`>
    
        Orbit element set type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    
        Also see:
            SANA registry for orbital elements
    """
    ADBARV: typing.ClassVar['ElementsType'] = ...
    CARTP: typing.ClassVar['ElementsType'] = ...
    CARTPV: typing.ClassVar['ElementsType'] = ...
    CARTPVA: typing.ClassVar['ElementsType'] = ...
    DELAUNAY: typing.ClassVar['ElementsType'] = ...
    DELAUNAYMOD: typing.ClassVar['ElementsType'] = ...
    EIGVAL3EIGVEC3: typing.ClassVar['ElementsType'] = ...
    EQUINOCTIAL: typing.ClassVar['ElementsType'] = ...
    EQUINOCTIALMOD: typing.ClassVar['ElementsType'] = ...
    GEODETIC: typing.ClassVar['ElementsType'] = ...
    KEPLERIAN: typing.ClassVar['ElementsType'] = ...
    KEPLERIANMEAN: typing.ClassVar['ElementsType'] = ...
    LDBARV: typing.ClassVar['ElementsType'] = ...
    ONSTATION: typing.ClassVar['ElementsType'] = ...
    POINCARE: typing.ClassVar['ElementsType'] = ...
    def checkUnits(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def toCartesian(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float], double2: float) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Convert to Cartesian coordinates.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): elements date
                elements (double[]): elements values
                mu (double): gravitational parameter in mÂ³/sÂ²
        
            Returns:
                Cartesian coordinates
        
        
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
    def valueOf(string: str) -> 'ElementsType':
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
    def values() -> typing.List['ElementsType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ElementsType c : ElementsType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class FrameFacade:
    """
    public class FrameFacade extends Object
    
        Facade in front of several frames types in CCSDS messages.
    
        Since:
            11.0
    """
    def __init__(self, frame: org.orekit.frames.Frame, celestialBodyFrame: CelestialBodyFrame, orbitRelativeFrame: 'OrbitRelativeFrame', spacecraftBodyFrame: 'SpacecraftBodyFrame', string: str): ...
    def asCelestialBodyFrame(self) -> CelestialBodyFrame:
        """
            Get the associated :class:`~org.orekit.files.ccsds.definitions.CelestialBodyFrame`.
        
            Returns:
                associated celestial body frame, or null if frame is associated to a
                :meth:`~org.orekit.files.ccsds.definitions.FrameFacade.asOrbitRelativeFrame`, a
                :meth:`~org.orekit.files.ccsds.definitions.FrameFacade.asSpacecraftBodyFrame` or is not supported
        
        
        """
        ...
    def asFrame(self) -> org.orekit.frames.Frame:
        """
            Get the associated frame tree node.
        
            Returns:
                associated frame tree node, or null if none exists
        
        
        """
        ...
    def asOrbitRelativeFrame(self) -> 'OrbitRelativeFrame':
        """
            Get the associated :class:`~org.orekit.files.ccsds.definitions.OrbitRelativeFrame`.
        
            Returns:
                associated orbit relative frame, or null if frame is associated to a
                :meth:`~org.orekit.files.ccsds.definitions.FrameFacade.asCelestialBodyFrame`, a
                :meth:`~org.orekit.files.ccsds.definitions.FrameFacade.asSpacecraftBodyFrame` or is not supported
        
        
        """
        ...
    def asSpacecraftBodyFrame(self) -> 'SpacecraftBodyFrame':
        """
            Get the associated :class:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame`.
        
            Returns:
                associated spacecraft body frame, or null if frame is associated to a
                :meth:`~org.orekit.files.ccsds.definitions.FrameFacade.asCelestialBodyFrame`, an
                :meth:`~org.orekit.files.ccsds.definitions.FrameFacade.asOrbitRelativeFrame` or is not supported
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the CCSDS name for the frame.
        
            Returns:
                CCSDS name
        
        
        """
        ...
    @staticmethod
    def map(frame: org.orekit.frames.Frame) -> 'FrameFacade':
        """
            Map an Orekit frame to a CCSDS frame facade.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): a reference frame.
        
            Returns:
                the CCSDSFrame corresponding to the Orekit frame
        
        
        """
        ...
    @staticmethod
    def parse(string: str, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, boolean2: bool, boolean3: bool, boolean4: bool) -> 'FrameFacade':
        """
            Simple constructor.
        
            Parameters:
                name (String): name of the frame
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions to use
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
                dataContext (:class:`~org.orekit.data.DataContext`): to use when creating the frame
                allowCelestial (boolean): if true, :class:`~org.orekit.files.ccsds.definitions.CelestialBodyFrame` are allowed
                allowOrbit (boolean): if true, :class:`~org.orekit.files.ccsds.definitions.OrbitRelativeFrame` are allowed
                allowSpacecraft (boolean): if true, :class:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame` are allowed
        
            Returns:
                frame facade corresponding to the CCSDS name
        
        
        """
        ...

class ModifiedFrame(org.orekit.frames.Frame):
    """
    public class ModifiedFrame extends :class:`~org.orekit.frames.Frame`
    
        A reference frame created from the :code:`REF_FRAME` and :code:`CENTER_NAME` is a CCSDS OPM, OMM, or OEM file.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, frame: org.orekit.frames.Frame, celestialBodyFrame: CelestialBodyFrame, celestialBody2: org.orekit.bodies.CelestialBody, string: str): ...
    def getCenterName(self) -> str:
        """
            Get the CCSDS center name.
        
            Returns:
                the value of the :code:`CENTER_NAME` key word used to specify the origin of this frame.
        
        
        """
        ...
    def getRefFrame(self) -> CelestialBodyFrame:
        """
            Get the CCSDS reference frame.
        
            Returns:
                the reference frame used to create this frame.
        
        
        """
        ...

class OdMethodFacade:
    """
    public class OdMethodFacade extends Object
    
        Facade in front of several orbit determination methods in CCSDS messages.
    
        Since:
            11.0
    """
    def __init__(self, string: str, odMethodType: 'OdMethodType', string2: str): ...
    def getName(self) -> str:
        """
            Get the name of the method.
        
            Returns:
                name of the method
        
        
        """
        ...
    def getTool(self) -> str:
        """
            Get the tool used for OD.
        
            Returns:
                tool used for OD
        
        
        """
        ...
    def getType(self) -> 'OdMethodType':
        """
            Get the method type.
        
            Returns:
                method type
        
        
        """
        ...
    @staticmethod
    def parse(string: str) -> 'OdMethodFacade':
        """
            Parse a string from OCM.
        
            Parameters:
                s (String): string to parse
        
            Returns:
                OD method facade
        
        
        """
        ...

class OdMethodType(java.lang.Enum['OdMethodType']):
    """
    public enum OdMethodType extends Enum<:class:`~org.orekit.files.ccsds.definitions.OdMethodType`>
    
        Type of orbit determination method used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    BWLS: typing.ClassVar['OdMethodType'] = ...
    EKF: typing.ClassVar['OdMethodType'] = ...
    SF: typing.ClassVar['OdMethodType'] = ...
    SRIF: typing.ClassVar['OdMethodType'] = ...
    SSEM: typing.ClassVar['OdMethodType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OdMethodType':
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
    def values() -> typing.List['OdMethodType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OdMethodType c : OdMethodType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OnOff(java.lang.Enum['OnOff']):
    """
    public enum OnOff extends Enum<:class:`~org.orekit.files.ccsds.definitions.OnOff`>
    
        On/Off status for various elements.
    
        Since:
            11.0
    """
    ON: typing.ClassVar['OnOff'] = ...
    OFF: typing.ClassVar['OnOff'] = ...
    def isOn(self) -> bool:
        """
            Check if status is "on".
        
            Returns:
                true if status is "on"
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OnOff':
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
    def values() -> typing.List['OnOff']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OnOff c : OnOff.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitRelativeFrame(java.lang.Enum['OrbitRelativeFrame']):
    """
    public enum OrbitRelativeFrame extends Enum<:class:`~org.orekit.files.ccsds.definitions.OrbitRelativeFrame`>
    
        Frames used in CCSDS Orbit Data Messages.
    
        Since:
            11.0
    """
    EQW_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    LVLH_ROTATING: typing.ClassVar['OrbitRelativeFrame'] = ...
    LVLH_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    LVLH: typing.ClassVar['OrbitRelativeFrame'] = ...
    NSW_ROTATING: typing.ClassVar['OrbitRelativeFrame'] = ...
    NSW_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    NTW_ROTATING: typing.ClassVar['OrbitRelativeFrame'] = ...
    NTW_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    PQW_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    RSW_ROTATING: typing.ClassVar['OrbitRelativeFrame'] = ...
    RSW_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    RSW: typing.ClassVar['OrbitRelativeFrame'] = ...
    RIC: typing.ClassVar['OrbitRelativeFrame'] = ...
    RTN: typing.ClassVar['OrbitRelativeFrame'] = ...
    QSW: typing.ClassVar['OrbitRelativeFrame'] = ...
    TNW_ROTATING: typing.ClassVar['OrbitRelativeFrame'] = ...
    TNW_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    TNW: typing.ClassVar['OrbitRelativeFrame'] = ...
    SEZ_ROTATING: typing.ClassVar['OrbitRelativeFrame'] = ...
    SEZ_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    VNC_ROTATING: typing.ClassVar['OrbitRelativeFrame'] = ...
    VNC_INERTIAL: typing.ClassVar['OrbitRelativeFrame'] = ...
    def getLofType(self) -> org.orekit.frames.LOFType:
        """
            Get the type of Local Orbital frame.
        
            Returns:
                type of Local Orbital Frame, or null if the frame is not a local orbital frame
        
        
        """
        ...
    def isQuasiInertial(self) -> bool:
        """
            Check if frame should be treated as inertial.
        
            A frame treated as an inertial coordinate system if it is considered to be redefined at each time of interest
        
            Returns:
                true if frame should be treated as inertial
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OrbitRelativeFrame':
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
    def values() -> typing.List['OrbitRelativeFrame']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OrbitRelativeFrame c : OrbitRelativeFrame.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SpacecraftBodyFrame:
    """
    public class SpacecraftBodyFrame extends Object
    
        Frames used in CCSDS Attitude Data Messages for the spacecraft body.
    
        Since:
            11.0
    """
    def __init__(self, baseEquipment: 'SpacecraftBodyFrame.BaseEquipment', string: str): ...
    def getBaseEquipment(self) -> 'SpacecraftBodyFrame.BaseEquipment':
        """
            Get the quipment on which the frame is located.
        
            Returns:
                equipment on which the frame is located
        
        
        """
        ...
    def getLabel(self) -> str:
        """
            Get the frame label.
        
            Returns:
                frame label
        
        
        """
        ...
    @staticmethod
    def parse(string: str) -> 'SpacecraftBodyFrame':
        """
            Build an instance from a normalized descriptor.
        
            Normalized strings have '_' characters replaced by spaces, and multiple spaces collapsed as one space only.
        
            Parameters:
                descriptor (String): normalized descriptor
        
            Returns:
                parsed body frame
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            The CCSDS composite name combines the :meth:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame.getBaseEquipment`
            and the :meth:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame.getLabel`
        
            Overrides:
                 in class 
        
            Returns:
                CCSDS composite name
        
        
        """
        ...
    class BaseEquipment(java.lang.Enum['SpacecraftBodyFrame.BaseEquipment']):
        ACC: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        ACTUATOR: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        AST: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        CSS: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        DSS: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        ESA: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        GYRO: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        GYRO_FRAME: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        IMU_FRAME: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        INSTRUMENT: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        MTA: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        RW: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        SA: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        SC_BODY: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        SENSOR: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        STARTRACKER: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        TAM: typing.ClassVar['SpacecraftBodyFrame.BaseEquipment'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SpacecraftBodyFrame.BaseEquipment': ...
        @staticmethod
        def values() -> typing.List['SpacecraftBodyFrame.BaseEquipment']: ...

class TimeConverter:
    """
    public class TimeConverter extends Object
    
        Dates reader/writer.
    
        Since:
            11.0
    """
    def __init__(self, timeScale: org.orekit.time.TimeScale, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def components(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.time.DateTimeComponents:
        """
            Generate calendar components.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to convert
        
            Returns:
                date components
        
        
        """
        ...
    def getTimeScale(self) -> org.orekit.time.TimeScale:
        """
            Get the base time scale.
        
            Returns:
                base time scale
        
        
        """
        ...
    def offset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Generate relative offset.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to convert
        
            Returns:
                relative offset
        
        
        """
        ...
    def parse(self, string: str) -> org.orekit.time.AbsoluteDate:
        """
            Parse a relative or absolute date.
        
            Parameters:
                s (String): string to parse
        
            Returns:
                parsed date
        
        
        """
        ...

class TimeSystem(java.lang.Enum['TimeSystem']):
    """
    public enum TimeSystem extends Enum<:class:`~org.orekit.files.ccsds.definitions.TimeSystem`>
    
        The set of time systems defined in CCSDS standards (ADM, ODM, NDM).
    """
    GMST: typing.ClassVar['TimeSystem'] = ...
    GPS: typing.ClassVar['TimeSystem'] = ...
    MET: typing.ClassVar['TimeSystem'] = ...
    MRT: typing.ClassVar['TimeSystem'] = ...
    SCLK: typing.ClassVar['TimeSystem'] = ...
    TAI: typing.ClassVar['TimeSystem'] = ...
    TCB: typing.ClassVar['TimeSystem'] = ...
    TDB: typing.ClassVar['TimeSystem'] = ...
    TCG: typing.ClassVar['TimeSystem'] = ...
    TT: typing.ClassVar['TimeSystem'] = ...
    UT1: typing.ClassVar['TimeSystem'] = ...
    UTC: typing.ClassVar['TimeSystem'] = ...
    def getConverter(self, contextBinding: org.orekit.files.ccsds.utils.ContextBinding) -> TimeConverter:
        """
            Get associated :class:`~org.orekit.files.ccsds.definitions.TimeConverter`.
        
            Parameters:
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
        
            Returns:
                time system for reading/writing date
        
            Since:
                11.0
        
        
        """
        ...
    @staticmethod
    def parse(string: str) -> 'TimeSystem':
        """
            Parse a value from a key=value entry.
        
            Parameters:
                value (String): value to parse
        
            Returns:
                CCSDS time system corresponding to the value
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TimeSystem':
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
    def values() -> typing.List['TimeSystem']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TimeSystem c : TimeSystem.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Units:
    """
    public class Units extends Object
    
        Units used in CCSDS messages.
    """
    ONE_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` ONE_PER_S
    
        Seconds reciprocal unit.
    
    """
    KG_M2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KG_M2
    
        kg.mÂ² unit.
    
    """
    KM3_PER_S2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM3_PER_S2
    
        kmÂ³/sÂ² unit.
    
    """
    M2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` M2
    
        mÂ² unit.
    
    """
    NB_PER_Y: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` NB_PER_Y
    
        #/year unit.
    
    """
    KM2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM2
    
        Square kilometers units.
    
    """
    KM_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM_PER_S
    
        Kilometers par second units.
    
    """
    KM_PER_S2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM_PER_S2
    
        Kilometers par square second units.
    
    """
    KM2_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM2_PER_S
    
        Square kilometers par second units.
    
    """
    KM2_PER_S2: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KM2_PER_S2
    
        Square kilometers per square second units.
    
    """
    REV_PER_DAY: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` REV_PER_DAY
    
        Revolutions per day unit.
    
    """
    REV_PER_DAY2_SCALED: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` REV_PER_DAY2_SCALED
    
        Scaled revolutions per square day unit.
    
    """
    REV_PER_DAY3_SCALED: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` REV_PER_DAY3_SCALED
    
        Scaled revolutions per cubic day divieded by 6 unit.
    
    """
    DEG_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` DEG_PER_S
    
        Degree per second unit.
    
    """
    N_M: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` N_M
    
        Newton metre unit.
    
    """
    NANO_TESLA: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` NANO_TESLA
    
        Nano Tesla unit.
    
    """
    HECTO_PASCAL: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` HECTO_PASCAL
    
        HectoPascal unit.
    
    """
    HZ_PER_S: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` HZ_PER_S
    
        Hertz per second unit.
    
    """


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.definitions")``.

    BodyFacade: typing.Type[BodyFacade]
    CelestialBodyFrame: typing.Type[CelestialBodyFrame]
    CenterName: typing.Type[CenterName]
    DutyCycleType: typing.Type[DutyCycleType]
    ElementsType: typing.Type[ElementsType]
    FrameFacade: typing.Type[FrameFacade]
    ModifiedFrame: typing.Type[ModifiedFrame]
    OdMethodFacade: typing.Type[OdMethodFacade]
    OdMethodType: typing.Type[OdMethodType]
    OnOff: typing.Type[OnOff]
    OrbitRelativeFrame: typing.Type[OrbitRelativeFrame]
    SpacecraftBodyFrame: typing.Type[SpacecraftBodyFrame]
    TimeConverter: typing.Type[TimeConverter]
    TimeSystem: typing.Type[TimeSystem]
    Units: typing.Type[Units]
