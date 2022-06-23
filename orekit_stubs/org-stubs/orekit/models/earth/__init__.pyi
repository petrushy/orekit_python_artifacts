import java.io
import java.lang
import java.util
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.data
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.models
import org.orekit.models.earth.atmosphere
import org.orekit.models.earth.displacement
import org.orekit.models.earth.ionosphere
import org.orekit.models.earth.tessellation
import org.orekit.models.earth.troposphere
import org.orekit.models.earth.weather
import org.orekit.time
import org.orekit.utils
import typing



class EarthITU453AtmosphereRefraction(org.orekit.models.AtmosphericRefractionModel):
    """
    public class EarthITU453AtmosphereRefraction extends Object implements :class:`~org.orekit.models.AtmosphericRefractionModel`
    
        Implementation of refraction model for Earth exponential atmosphere based on ITU-R P.834-7 recommendation.
    
        Refraction angle is computed according to the International Telecommunication Union recommendation formula. For
        reference, see **ITU-R P.834-7** (October 2015).
    
        Since:
            7.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float): ...
    def getRefraction(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.AtmosphericRefractionModel.getRefraction`
            Compute the refraction angle from the true (geometrical) elevation.
        
            Specified by:
                :meth:`~org.orekit.models.AtmosphericRefractionModel.getRefraction`Â in
                interfaceÂ :class:`~org.orekit.models.AtmosphericRefractionModel`
        
            Parameters:
                elevation (double): true elevation (rad)
        
            Returns:
                refraction angle (rad)
        
        
        """
        ...
    def getTheta0(self) -> float:
        """
            Get the station elevation angle under free-space propagation .
        
            Returns:
                the elevation angle under free-space propagation (rad)
        
        
        """
        ...
    def getThetaMin(self) -> float:
        """
            Get the station minimal elevation angle.
        
            Returns:
                the minimal elevation angle (rad)
        
        
        """
        ...

class EarthShape(org.orekit.bodies.BodyShape):
    """
    public interface EarthShape extends :class:`~org.orekit.bodies.BodyShape`
    
        All models of Earth's shape have some common properties that are not shared with arbitrary
        :class:`~org.orekit.bodies.BodyShape`s. In particular, an ellipsoidal (or spherical) model is used to compute latitude
        and longitude.
    
        Also see:
            :meth:`~org.orekit.models.earth.EarthShape.getEllipsoid`
    """
    def getEllipsoid(self) -> 'ReferenceEllipsoid':
        """
            Get the underlying ellipsoid model that defines latitude and longitude. If the height component of a
            :class:`~org.orekit.bodies.GeodeticPoint` is not needed, then using the ellipsoid will provide the quickest
            transformation.
        
            Returns:
                the reference ellipsoid. May be :code:`this`, but never :code:`null`.
        
        
        """
        ...

class EarthStandardAtmosphereRefraction(org.orekit.models.AtmosphericRefractionModel):
    """
    public class EarthStandardAtmosphereRefraction extends Object implements :class:`~org.orekit.models.AtmosphericRefractionModel`
    
        Implementation of refraction model for Earth standard atmosphere.
    
        Refraction angle is 0 at zenith, about 1 arcminute at 45Â°, and 34 arcminutes at the horizon for optical wavelengths.
    
        Refraction angle is computed according to Saemundssen formula quoted by Meeus. For reference, see **Astronomical
        Algorithms** (1998), 2nd ed, (ISBN 0-943396-61-1), chap. 15.
    
        This formula is about 30 arcseconds of accuracy very close to the horizon, as variable atmospheric effects become very
        important.
    
        Local pressure and temperature can be set to correct refraction at the viewpoint.
    
        Since:
            6.1
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_CORRECTION_FACTOR: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_CORRECTION_FACTOR
    
        Default correction factor value.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_PRESSURE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_PRESSURE
    
        Default local pressure at viewpoint (Pa).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_TEMPERATURE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_TEMPERATURE
    
        Default local temperature at viewpoint (K).
    
        Also see:
            :meth:`~constant`
    
    
    """
    STANDARD_ATM_PRESSURE: typing.ClassVar[float] = ...
    """
    public static final double STANDARD_ATM_PRESSURE
    
        NIST standard atmospheric pressure (Pa).
    
        Also see:
            :meth:`~constant`
    
    
    """
    STANDARD_ATM_TEMPERATURE: typing.ClassVar[float] = ...
    """
    public static final double STANDARD_ATM_TEMPERATURE
    
        NIST standard atmospheric temperature (K).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def getPressure(self) -> float:
        """
            Get the local pressure at the evaluation location.
        
            Returns:
                the pressure (Pa)
        
        
        """
        ...
    def getRefraction(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~org.orekit.models.AtmosphericRefractionModel.getRefraction`
            Compute the refraction angle from the true (geometrical) elevation.
        
            Specified by:
                :meth:`~org.orekit.models.AtmosphericRefractionModel.getRefraction`Â in
                interfaceÂ :class:`~org.orekit.models.AtmosphericRefractionModel`
        
            Parameters:
                trueElevation (double): true elevation (rad)
        
            Returns:
                refraction angle (rad)
        
        
        """
        ...
    def getTemperature(self) -> float:
        """
            Get the local temperature at the evaluation location.
        
            Returns:
                the temperature (K)
        
        
        """
        ...
    def setPressure(self, double: float) -> None:
        """
            Set the local pressure at the evaluation location
        
            Otherwise the default value for the local pressure is set to
            :meth:`~org.orekit.models.earth.EarthStandardAtmosphereRefraction.DEFAULT_PRESSURE`.
        
            Parameters:
                pressure (double): the pressure to set (Pa)
        
        
        """
        ...
    def setTemperature(self, double: float) -> None:
        """
            Set the local temperature at the evaluation location
        
            Otherwise the default value for the local temperature is set to
            :meth:`~org.orekit.models.earth.EarthStandardAtmosphereRefraction.DEFAULT_TEMPERATURE`.
        
            Parameters:
                temperature (double): the temperature to set (K)
        
        
        """
        ...

class GeoMagneticElements(java.io.Serializable):
    """
    public class GeoMagneticElements extends Object implements Serializable
    
        Contains the elements to represent a magnetic field at a single point.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getDeclination(self) -> float:
        """
            Returns the declination of the magnetic field in radians.
        
            Returns:
                the declination (dec) in radians
        
        
        """
        ...
    def getFieldVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Returns the magnetic field vector in nTesla.
        
            Returns:
                the magnetic field vector in nTesla
        
        
        """
        ...
    def getHorizontalIntensity(self) -> float:
        """
            Returns the horizontal intensity of the magnetic field (= norm of the vector in the plane spanned by the x/y components
            of the field vector).
        
            Returns:
                the horizontal intensity in nTesla
        
        
        """
        ...
    def getInclination(self) -> float:
        """
            Returns the inclination of the magnetic field in radians.
        
            Returns:
                the inclination (dip) in radians
        
        
        """
        ...
    def getTotalIntensity(self) -> float:
        """
            Returns the total intensity of the magnetic field (= norm of the field vector).
        
            Returns:
                the total intensity in nTesla
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class GeoMagneticField:
    """
    public class GeoMagneticField extends Object
    
        Used to calculate the geomagnetic field at a given geodetic point on earth. The calculation is estimated using spherical
        harmonic expansion of the geomagnetic potential with coefficients provided by an actual geomagnetic field model (e.g.
        IGRF, WMM).
    
        Based on original software written by Manoj Nair from the National Geophysical Data Center, NOAA, as part of the WMM
        2010 software release (WMM_SubLibrary.c)
    
        Also see:
            `World Magnetic Model Overview <http://www.ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml>`, `WMM Software Downloads
            <http://www.ngdc.noaa.gov/geomag/WMM/soft.shtml>`
    """
    def calculateField(self, double: float, double2: float, double3: float) -> GeoMagneticElements:
        """
            Calculate the magnetic field at the specified geodetic point identified by latitude, longitude and altitude.
        
            Parameters:
                latitude (double): the WGS84 latitude in radians
                longitude (double): the WGS84 longitude in radians
                height (double): the height above the WGS84 ellipsoid in meters
        
            Returns:
                the :class:`~org.orekit.models.earth.GeoMagneticElements` at the given geodetic point
        
        
        """
        ...
    @staticmethod
    def getDecimalYear(int: int, int2: int, int3: int) -> float:
        """
            Utility function to get a decimal year for a given day.
        
            Parameters:
                day (int): the day (1-31)
                month (int): the month (1-12)
                year (int): the year
        
            Returns:
                the decimal year represented by the given day
        
        
        """
        ...
    def getEpoch(self) -> float:
        """
            Returns the epoch for this magnetic field model.
        
            Returns:
                the epoch
        
        
        """
        ...
    def getModelName(self) -> str:
        """
            Returns the model name.
        
            Returns:
                the model name
        
        
        """
        ...
    def supportsTimeTransform(self) -> bool:
        """
            Indicates whether this model supports time transformation or not.
        
            Returns:
                :code:`true` if this model can be transformed within its validity period, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def transformModel(self, double: float) -> 'GeoMagneticField':
        """
            Time transform the model coefficients from the base year of the model using secular variation coefficients.
        
            Parameters:
                year (double): the year to which the model shall be transformed
        
            Returns:
                a time-transformed magnetic field model
        
            Time transform the model coefficients from the base year of the model using a linear interpolation with a second model.
            The second model is required to have an adjacent validity period.
        
            Parameters:
                otherModel (:class:`~org.orekit.models.earth.GeoMagneticField`): the other magnetic field model
                year (double): the year to which the model shall be transformed
        
            Returns:
                a time-transformed magnetic field model
        
        
        """
        ...
    @typing.overload
    def transformModel(self, geoMagneticField: 'GeoMagneticField', double: float) -> 'GeoMagneticField': ...
    def validFrom(self) -> float:
        """
            Returns the start of the validity period for this model.
        
            Returns:
                the validity start as decimal year
        
        
        """
        ...
    def validTo(self) -> float:
        """
            Returns the end of the validity period for this model.
        
            Returns:
                the validity end as decimal year
        
        
        """
        ...

class GeoMagneticFieldFactory:
    """
    public class GeoMagneticFieldFactory extends Object
    
        Factory for different :class:`~org.orekit.models.earth.GeoMagneticField` models.
    
        This is a utility class, so its constructor is private.
    
        Also see:
            :class:`~org.orekit.models.earth.GeoMagneticFields`, :class:`~org.orekit.models.earth.LazyLoadedGeoMagneticFields`,
            :meth:`~org.orekit.data.DataContext.getGeoMagneticFields`
    """
    @staticmethod
    def getField(fieldModel: 'GeoMagneticFieldFactory.FieldModel', double: float) -> GeoMagneticField: ...
    @staticmethod
    def getGeoMagneticFields() -> 'LazyLoadedGeoMagneticFields': ...
    @staticmethod
    def getIGRF(double: float) -> GeoMagneticField: ...
    @staticmethod
    def getWMM(double: float) -> GeoMagneticField: ...
    class FieldModel(java.lang.Enum['GeoMagneticFieldFactory.FieldModel']):
        WMM: typing.ClassVar['GeoMagneticFieldFactory.FieldModel'] = ...
        IGRF: typing.ClassVar['GeoMagneticFieldFactory.FieldModel'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'GeoMagneticFieldFactory.FieldModel': ...
        @staticmethod
        def values() -> typing.List['GeoMagneticFieldFactory.FieldModel']: ...

class GeoMagneticFields:
    """
    public interface GeoMagneticFields
    
        Methods for obtaining geomagnetic fields.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.models.earth.GeoMagneticFieldFactory`, :class:`~org.orekit.models.earth.LazyLoadedGeoMagneticFields`
    """
    def getField(self, fieldModel: GeoMagneticFieldFactory.FieldModel, double: float) -> GeoMagneticField:
        """
            Get the :class:`~org.orekit.models.earth.GeoMagneticField` for the given model type and year.
        
            Parameters:
                type (:class:`~org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel`): the field model type
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year and model
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...
    def getIGRF(self, double: float) -> GeoMagneticField:
        """
            Get the IGRF model for the given year.
        
            Parameters:
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...
    def getWMM(self, double: float) -> GeoMagneticField:
        """
            Get the WMM model for the given year.
        
            Parameters:
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...

class GeoMagneticModelLoader(org.orekit.data.DataLoader):
    """
    public class GeoMagneticModelLoader extends Object implements :class:`~org.orekit.data.DataLoader`
    
        Loads geomagnetic field models from a given input stream. A stream may contain multiple models, the loader reads all
        available models in consecutive order.
    
        The format of the expected model file is either:
    
          - combined format as used by the geomag software, available from the `IGRF model site
            <http://www.ngdc.noaa.gov/IAGA/vmod/igrf.html>`; supports multiple epochs per file
          - original format as used by the `WMM model site <http://www.ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml>`.
    
    
        **Combined Format**
    
        .. code-block: java
        
        
             {model name} {epoch} {nMax} {nMaxSec} {nMax3} {validity start} {validity end} {minAlt} {maxAlt} {model name} {line number}
         {n} {m} {gnm} {hnm} {dgnm} {dhnm} {model name} {line number}
         
    
        Example:
    
        .. code-block: java
        
        
            WMM2010  2010.00 12 12  0 2010.00 2015.00   -1.0  600.0          WMM2010   0
         1  0  -29496.6       0.0      11.6       0.0                        WMM2010   1
         1  1   -1586.3    4944.4      16.5     -25.9                        WMM2010   2
         
    
        **Original WMM Format**
    
        .. code-block: java
        
        
            {epoch} {model name} {validity start}
         {n} {m} {gnm} {hnm} {dgnm} {dhnm}
         
    
        Example:
    
        .. code-block: java
        
        
            2015.0            WMM-2015        12/15/2014
          1  0  -29438.5       0.0       10.7        0.0
          1  1   -1501.1    4796.2       17.9      -26.8
    """
    def __init__(self): ...
    def getModels(self) -> java.util.Collection[GeoMagneticField]: ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def stillAcceptsData(self) -> bool:
        """
            Check if the loader still accepts new data.
        
            This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the
            data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or
            Earth Orientation Parameters that are split among several files), this method should always return true to make sure no
            data is left over.
        
            Specified by:
                :meth:`~org.orekit.data.DataLoader.stillAcceptsData` in interface :class:`~org.orekit.data.DataLoader`
        
            Returns:
                true while the loader still accepts new data
        
        
        """
        ...

class Geoid(EarthShape):
    """
    public class Geoid extends Object implements :class:`~org.orekit.models.earth.EarthShape`
    
        A geoid is a level surface of the gravity potential of a body. The gravity potential, W, is split so W = U + T, where U
        is the normal potential (defined by the ellipsoid) and T is the anomalous potential.[3](eq. 2-137)
    
        The :meth:`~org.orekit.models.earth.Geoid.getIntersectionPoint` method is tailored specifically for Earth's geoid. All
        of the other methods in this class are general and will work for an arbitrary body.
    
        There are several components that are needed to define a geoid[1]:
    
          - Geopotential field. These are the coefficients of the spherical harmonics: S :sub:`n,m` and C :sub:`n,m`
          - Reference Ellipsoid. The ellipsoid is used to define the undulation of the geoid (distance between ellipsoid and geoid)
            and U :sub:`0` the value of the normal gravity potential at the surface of the ellipsoid.
          - W :sub:`0` , the potential at the geoid. The value of the potential on the level surface. This is taken to be U :sub:`0`
            , the normal gravity potential at the surface of the :class:`~org.orekit.models.earth.ReferenceEllipsoid`.
          - Permanent Tide System. This implementation assumes that the geopotential field and the reference ellipsoid use the same
            permanent tide system. If the assumption is false it will produce errors of about 0.5 m. Conversion between tide systems
            is a possible improvement.[1,2]
          - Topographic Masses. That is mass outside of the geoid, e.g. mountains. This implementation ignores topographic masses,
            which causes up to 3m error in the Himalayas, and ~ 1.5m error in the Rockies. This could be improved through the use of
            DTED and calculating height anomalies or using the correction coefficients.[1]
    
    
        This implementation also assumes that the normal to the reference ellipsoid is the same as the normal to the geoid. This
        assumption enables the equation: (height above geoid) = (height above ellipsoid) - (undulation), which is used in
        :meth:`~org.orekit.models.earth.Geoid.transform` and :meth:`~org.orekit.models.earth.Geoid.transform`.
    
        In testing, the error in the undulations calculated by this class were off by less than 3 meters, which matches the
        assumptions outlined above.
    
        References:
    
          1.  Dru A. Smith. There is no such thing as "The" EGM96 geoid: Subtle points on the use of a global geopotential model. IGeS
            Bulletin No. 8:17-28, 1998. `http://www.ngs.noaa.gov/PUBS_LIB/EGM96_GEOID_PAPER/egm96_geoid_paper.html
            <http://www.ngs.noaa.gov/PUBS_LIB/EGM96_GEOID_PAPER/egm96_geoid_paper.html>`
          2.  Martin Losch, Verena Seufer. How to Compute Geoid Undulations (Geoid Height Relative to a Given Reference Ellipsoid)
            from Spherical Harmonic Coefficients for Satellite Altimetry Applications. , 2003. `mitgcm.org/~mlosch/geoidcookbook.pdf
            <http://mitgcm.org/~mlosch/geoidcookbook.pdf>`
          3.  Weikko A. Heiskanen, Helmut Moritz. Physical Geodesy. W. H. Freeman and Company, 1967. (especially sections 2.13 and
            equation 2-144 Bruns Formula)
          4.  S. A. Holmes, W. E. Featherstone. A unified approach to the Clenshaw summation and the recursive computation of very
            high degree and order normalised associated Legendre functions. Journal of Geodesy, 76(5):279, 2002.
          5.  DMA TR 8350.2. 1984.
          6.  Department of Defense World Geodetic System 1984. 2000. NIMA TR 8350.2 Third Edition, Amendment 1.
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, normalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider, referenceEllipsoid: 'ReferenceEllipsoid'): ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.BodyShape.getBodyFrame`
            Get body frame related to body shape.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getBodyFrame` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Returns:
                body frame related to body shape
        
        
        """
        ...
    def getEllipsoid(self) -> 'ReferenceEllipsoid':
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.EarthShape.getEllipsoid`
            Get the underlying ellipsoid model that defines latitude and longitude. If the height component of a
            :class:`~org.orekit.bodies.GeodeticPoint` is not needed, then using the ellipsoid will provide the quickest
            transformation.
        
            Specified by:
                :meth:`~org.orekit.models.earth.EarthShape.getEllipsoid` in interface :class:`~org.orekit.models.earth.EarthShape`
        
            Returns:
                the reference ellipsoid. May be :code:`this`, but never :code:`null`.
        
        
        """
        ...
    _getIntersectionPoint_0__T = typing.TypeVar('_getIntersectionPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getIntersectionPoint(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_0__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_0__T]) -> org.orekit.bodies.FieldGeodeticPoint[_getIntersectionPoint_0__T]:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            The intersection point is computed using a line search along the specified line. This is accurate when the geoid is
            slowly varying.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                lineInFrame (FieldLine<T> lineInFrame): test line (may intersect the body or not)
                closeInFrame (FieldVector3D<T> closeInFrame): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            The intersection point is computed using a line search along the specified line. This is accurate when the geoid is
            slowly varying.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                lineInFrame (Line): test line (may intersect the body or not)
                closeInFrame (Vector3D): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    def getUndulation(self, double: float, double2: float, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Gets the Undulation of the Geoid, N at the given position. N is the distance between the
            :meth:`~org.orekit.models.earth.Geoid.getEllipsoid` and the geoid. The latitude and longitude parameters are both
            defined with respect to the reference ellipsoid. For EGM96 and the WGS84 ellipsoid the undulation is between -107m and
            +86m.
        
            NOTE: Restrictions are not put on the range of the arguments :code:`geodeticLatitude` and :code:`longitude`.
        
            Parameters:
                geodeticLatitude (double): geodetic latitude (angle between the local normal and the equatorial plane on the reference ellipsoid), in radians.
                longitude (double): on the reference ellipsoid, in radians.
                date (:class:`~org.orekit.time.AbsoluteDate`): of evaluation. Used for time varying geopotential fields.
        
            Returns:
                the undulation in m, positive means the geoid is higher than the ellipsoid.
        
            Also see:
                :class:`~org.orekit.models.earth.Geoid`, `Geoid on Wikipedia <http://en.wikipedia.org/wiki/Geoid>`
        
        
        """
        ...
    @typing.overload
    def projectToGround(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.BodyShape.projectToGround`
            Project a point to the ground.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (Vector3D): point to project
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Also see:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround`
        
        """
        ...
    @typing.overload
    def projectToGround(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.BodyShape.projectToGround`
            Project a moving point to the ground.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): moving point
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Also see:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround`
        
        
        """
        ...
    _transform_0__T = typing.TypeVar('_transform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_transform_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_0__T]:
        """
            Transform a surface-relative point to a Cartesian point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): The surface relative point to transform. Altitude is orthometric height, that is height above the
                    :class:`~org.orekit.models.earth.Geoid`. Latitude and longitude are both geodetic and defined with respect to the
                    :meth:`~org.orekit.models.earth.Geoid.getEllipsoid`.
        
            Returns:
                point at the same location but as a Cartesian point in the :meth:`~org.orekit.models.earth.Geoid.getBodyFrame`.
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.models.earth.Geoid.transform`
        
        
        """
        ...
    @typing.overload
    def transform(self, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a Cartesian point to a surface-relative point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                date (Vector3D): date of the conversion. Used for computing frame transformations and for time dependent geopotential.
                point (:class:`~org.orekit.frames.Frame`): Cartesian point
                frame (:class:`~org.orekit.time.AbsoluteDate`): frame in which Cartesian point is expressed
        
            Returns:
                The surface relative point at the same location. Altitude is orthometric height, that is height above the
                :class:`~org.orekit.models.earth.Geoid`. Latitude and longitude are both geodetic and defined with respect to the
                :meth:`~org.orekit.models.earth.Geoid.getEllipsoid`.
        
            Also see:
                :meth:`~org.orekit.models.earth.Geoid.transform`, `Orthometric_height <http://en.wikipedia.org/wiki/Orthometric_height>`
        
            Transform a surface-relative point to a Cartesian point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.GeodeticPoint`): The surface relative point to transform. Altitude is orthometric height, that is height above the
                    :class:`~org.orekit.models.earth.Geoid`. Latitude and longitude are both geodetic and defined with respect to the
                    :meth:`~org.orekit.models.earth.Geoid.getEllipsoid`.
        
            Returns:
                point at the same location but as a Cartesian point in the :meth:`~org.orekit.models.earth.Geoid.getBodyFrame`.
        
            Also see:
                :meth:`~org.orekit.models.earth.Geoid.transform`
        
        """
        ...
    @typing.overload
    def transform(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_2__T]) -> org.orekit.bodies.FieldGeodeticPoint[_transform_2__T]:
        """
            Transform a Cartesian point to a surface-relative point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                date (FieldVector3D<T> point): date of the conversion. Used for computing frame transformations and for time dependent geopotential.
                point (:class:`~org.orekit.frames.Frame`): Cartesian point
                frame (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): frame in which Cartesian point is expressed
        
            Returns:
                The surface relative point at the same location. Altitude is orthometric height, that is height above the
                :class:`~org.orekit.models.earth.Geoid`. Latitude and longitude are both geodetic and defined with respect to the
                :meth:`~org.orekit.models.earth.Geoid.getEllipsoid`.
        
            Also see:
                :meth:`~org.orekit.models.earth.Geoid.transform`, `Orthometric_height <http://en.wikipedia.org/wiki/Orthometric_height>`
        
        """
        ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint: ...

class LazyLoadedGeoMagneticFields(GeoMagneticFields):
    """
    public class LazyLoadedGeoMagneticFields extends Object implements :class:`~org.orekit.models.earth.GeoMagneticFields`
    
        Loads magnetic fields on request and can be configured after creation. Designed to match the behavior of
        :class:`~org.orekit.models.earth.GeoMagneticFieldFactory` in Orekit 10.0
    
        Since:
            10.1
    """
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getField(self, fieldModel: GeoMagneticFieldFactory.FieldModel, double: float) -> GeoMagneticField:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.GeoMagneticFields.getField`
            Get the :class:`~org.orekit.models.earth.GeoMagneticField` for the given model type and year.
        
            Specified by:
                :meth:`~org.orekit.models.earth.GeoMagneticFields.getField`Â in
                interfaceÂ :class:`~org.orekit.models.earth.GeoMagneticFields`
        
            Parameters:
                type (:class:`~org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel`): the field model type
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year and model
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...
    def getIGRF(self, double: float) -> GeoMagneticField:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.GeoMagneticFields.getIGRF`
            Get the IGRF model for the given year.
        
            Specified by:
                :meth:`~org.orekit.models.earth.GeoMagneticFields.getIGRF`Â in
                interfaceÂ :class:`~org.orekit.models.earth.GeoMagneticFields`
        
            Parameters:
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...
    def getWMM(self, double: float) -> GeoMagneticField:
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.GeoMagneticFields.getWMM`
            Get the WMM model for the given year.
        
            Specified by:
                :meth:`~org.orekit.models.earth.GeoMagneticFields.getWMM`Â in
                interfaceÂ :class:`~org.orekit.models.earth.GeoMagneticFields`
        
            Parameters:
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...

class PythonEarthShape(EarthShape):
    """
    public class PythonEarthShape extends Object implements :class:`~org.orekit.models.earth.EarthShape`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
            Get body frame related to body shape.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getBodyFrame` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Returns:
                body frame related to body shape
        
        
        """
        ...
    def getEllipsoid(self) -> 'ReferenceEllipsoid':
        """
            Get the underlying ellipsoid model that defines latitude and longitude. If the height component of a
            :class:`~org.orekit.bodies.GeodeticPoint` is not needed, then using the ellipsoid will provide the quickest
            transformation.
        
            Specified by:
                :meth:`~org.orekit.models.earth.EarthShape.getEllipsoid` in interface :class:`~org.orekit.models.earth.EarthShape`
        
            Returns:
                the reference ellipsoid. May be :code:`this`, but never :code:`null`.
        
        
        """
        ...
    _getIntersectionPoint_1__T = typing.TypeVar('_getIntersectionPoint_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                line (Line): test line (may intersect the body or not)
                close (Vector3D): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_1__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_1__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_1__T]) -> org.orekit.bodies.FieldGeodeticPoint[_getIntersectionPoint_1__T]:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                line (FieldLine<T> line): test line (may intersect the body or not)
                close (FieldVector3D<T> close): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
            Since:
                9.0
        
        
        """
        ...
    _getIntersectionPoint_FFFF__T = typing.TypeVar('_getIntersectionPoint_FFFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getIntersectionPoint_FFFF(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_FFFF__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_FFFF__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_FFFF__T]) -> org.orekit.bodies.FieldGeodeticPoint[_getIntersectionPoint_FFFF__T]: ...
    @typing.overload
    def projectToGround(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Project a point to the ground.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (Vector3D): point to project
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Since:
                7.0
        
            Also see:
                :meth:`~org.orekit.models.earth.PythonEarthShape.projectToGround`
        
        """
        ...
    @typing.overload
    def projectToGround(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Project a moving point to the ground.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): moving point
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Since:
                7.0
        
            Also see:
                :meth:`~org.orekit.models.earth.PythonEarthShape.projectToGround`
        
        
        """
        ...
    def projectToGround_TF(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
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
    _transform_1__T = typing.TypeVar('_transform_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_3__T = typing.TypeVar('_transform_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.bodies.GeodeticPoint:
        """
            Transform a Cartesian point to a surface-relative point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (Vector3D): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
        """
        ...
    @typing.overload
    def transform(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_transform_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_1__T]:
        """
            Transform a surface-relative point to a Cartesian point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def transform(self, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a surface-relative point to a Cartesian point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.GeodeticPoint`): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
        """
        ...
    @typing.overload
    def transform(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_3__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_3__T]) -> org.orekit.bodies.FieldGeodeticPoint[_transform_3__T]:
        """
            Transform a Cartesian point to a surface-relative point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (FieldVector3D<T> point): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Since:
                9.0
        
        """
        ...
    _transform_F__T = typing.TypeVar('_transform_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def transform_F(self, fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_transform_F__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_F__T]: ...
    _transform_FFF__T = typing.TypeVar('_transform_FFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def transform_FFF(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_FFF__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_FFF__T]) -> org.orekit.bodies.FieldGeodeticPoint[_transform_FFF__T]:
        """
            Transform a Cartesian point to a surface-relative point.
        
            Parameters:
                point (FieldVector3D<T> point): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Since:
                9.0
        
        
        """
        ...
    def transform_G(self, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a surface-relative point to a Cartesian point.
        
            Parameters:
                point (:class:`~org.orekit.bodies.GeodeticPoint`): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
        
        """
        ...

class PythonGeoMagneticFields(GeoMagneticFields):
    """
    public class PythonGeoMagneticFields extends Object implements :class:`~org.orekit.models.earth.GeoMagneticFields`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getField(self, fieldModel: GeoMagneticFieldFactory.FieldModel, double: float) -> GeoMagneticField:
        """
            Get the :class:`~org.orekit.models.earth.GeoMagneticField` for the given model type and year.
        
            Specified by:
                :meth:`~org.orekit.models.earth.GeoMagneticFields.getField`Â in
                interfaceÂ :class:`~org.orekit.models.earth.GeoMagneticFields`
        
            Parameters:
                type (:class:`~org.orekit.models.earth.GeoMagneticFieldFactory.FieldModel`): the field model type
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year and model
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...
    def getIGRF(self, double: float) -> GeoMagneticField:
        """
            Get the IGRF model for the given year.
        
            Specified by:
                :meth:`~org.orekit.models.earth.GeoMagneticFields.getIGRF`Â in
                interfaceÂ :class:`~org.orekit.models.earth.GeoMagneticFields`
        
            Parameters:
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
        """
        ...
    def getWMM(self, double: float) -> GeoMagneticField:
        """
            Get the WMM model for the given year.
        
            Specified by:
                :meth:`~org.orekit.models.earth.GeoMagneticFields.getWMM`Â in
                interfaceÂ :class:`~org.orekit.models.earth.GeoMagneticFields`
        
            Parameters:
                year (double): the decimal year
        
            Returns:
                a :class:`~org.orekit.models.earth.GeoMagneticField` for the given year
        
            Also see:
                :meth:`~org.orekit.models.earth.GeoMagneticField.getDecimalYear`
        
        
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

class ReferenceEllipsoid(org.orekit.bodies.OneAxisEllipsoid, EarthShape):
    """
    public class ReferenceEllipsoid extends :class:`~org.orekit.bodies.OneAxisEllipsoid` implements :class:`~org.orekit.models.earth.EarthShape`
    
        A Reference Ellipsoid for use in geodesy. The ellipsoid defines an ellipsoidal potential called the normal potential,
        and its gradient, normal gravity.
    
        These parameters are needed to define the normal potential:
    
          - a, semi-major axis
          - f, flattening
          - GM, the gravitational parameter
          - ω, the spin rate
    
    
        References:
    
          1.  Martin Losch, Verena Seufer. How to Compute Geoid Undulations (Geoid Height Relative to a Given Reference Ellipsoid)
            from Spherical Harmonic Coefficients for Satellite Altimetry Applications. , 2003. `mitgcm.org/~mlosch/geoidcookbook.pdf
            <http://mitgcm.org/~mlosch/geoidcookbook.pdf>`
          2.  Weikko A. Heiskanen, Helmut Moritz. Physical Geodesy. W. H. Freeman and Company, 1967. (especially sections 2.13 and
            equation 2-144)
          3.  Department of Defense World Geodetic System 1984. 2000. NIMA TR 8350.2 Third Edition, Amendment 1.
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame, double3: float, double4: float): ...
    def getC2n0(self, int: int) -> float:
        """
            Get the fully normalized coefficient C :sub:`2n,0` for the normal gravity potential.
        
            Parameters:
                n (int): index in C :sub:`2n,0` , n >= 1.
        
            Returns:
                normalized C :sub:`2n,0` of the ellipsoid
        
            Also see:
                "Department of Defense World Geodetic System 1984. 2000. NIMA TR 8350.2 Third Edition, Amendment 1.", "DMA TR 8350.2.
                1984."
        
        
        """
        ...
    def getEllipsoid(self) -> 'ReferenceEllipsoid':
        """
            Description copied from interface: :meth:`~org.orekit.models.earth.EarthShape.getEllipsoid`
            Get the underlying ellipsoid model that defines latitude and longitude. If the height component of a
            :class:`~org.orekit.bodies.GeodeticPoint` is not needed, then using the ellipsoid will provide the quickest
            transformation.
        
            Specified by:
                :meth:`~org.orekit.models.earth.EarthShape.getEllipsoid` in interface :class:`~org.orekit.models.earth.EarthShape`
        
            Returns:
                the reference ellipsoid. May be :code:`this`, but never :code:`null`.
        
        
        """
        ...
    def getGM(self) -> float:
        """
            Gets the gravitational parameter that is part of the definition of the reference ellipsoid.
        
            Returns:
                GM in m :sup:`3` /s :sup:`2`
        
        
        """
        ...
    @staticmethod
    def getGrs80(frame: org.orekit.frames.Frame) -> 'ReferenceEllipsoid':
        """
            Get the GRS80 ellipsoid, attached to the given body frame.
        
            Parameters:
                bodyFrame (:class:`~org.orekit.frames.Frame`): the earth centered fixed frame
        
            Returns:
                a GRS80 reference ellipsoid
        
        
        """
        ...
    @staticmethod
    def getIers2003(frame: org.orekit.frames.Frame) -> 'ReferenceEllipsoid':
        """
            Get the IERS2003 ellipsoid, attached to the given body frame.
        
            Parameters:
                bodyFrame (:class:`~org.orekit.frames.Frame`): the earth centered fixed frame
        
            Returns:
                an IERS2003 reference ellipsoid
        
        
        """
        ...
    @staticmethod
    def getIers2010(frame: org.orekit.frames.Frame) -> 'ReferenceEllipsoid':
        """
            Get the IERS2010 ellipsoid, attached to the given body frame.
        
            Parameters:
                bodyFrame (:class:`~org.orekit.frames.Frame`): the earth centered fixed frame
        
            Returns:
                an IERS2010 reference ellipsoid
        
        
        """
        ...
    @staticmethod
    def getIers96(frame: org.orekit.frames.Frame) -> 'ReferenceEllipsoid':
        """
            Get the IERS96 ellipsoid, attached to the given body frame.
        
            Parameters:
                bodyFrame (:class:`~org.orekit.frames.Frame`): the earth centered fixed frame
        
            Returns:
                an IERS96 reference ellipsoid
        
        
        """
        ...
    def getNormalGravity(self, double: float) -> float:
        """
            Gets the normal gravity, that is gravity just due to the reference ellipsoid's potential. The normal gravity only
            depends on latitude because the ellipsoid is axis symmetric.
        
            The normal gravity is a vector, having both magnitude and direction. This method only give the magnitude.
        
            Parameters:
                latitude (double): geodetic latitude, in radians. That is the angle between the local normal on the ellipsoid and the equatorial plane.
        
            Returns:
                the normal gravity, Î³, at the given latitude in m/s :sup:`2` . This is the acceleration felt by a mass at rest on the
                surface of the reference ellipsoid.
        
        
        """
        ...
    def getPolarRadius(self) -> float:
        """
            Get the radius of this ellipsoid at the poles.
        
            Returns:
                the polar radius, in meters
        
            Also see:
                :meth:`~org.orekit.bodies.OneAxisEllipsoid.getEquatorialRadius`
        
        
        """
        ...
    def getSpin(self) -> float:
        """
            Gets the rotation of the ellipsoid about its axis.
        
            Returns:
                ω in rad/s
        
        
        """
        ...
    @staticmethod
    def getWgs84(frame: org.orekit.frames.Frame) -> 'ReferenceEllipsoid':
        """
            Get the WGS84 ellipsoid, attached to the given body frame.
        
            Parameters:
                bodyFrame (:class:`~org.orekit.frames.Frame`): the earth centered fixed frame
        
            Returns:
                a WGS84 reference ellipsoid
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth")``.

    EarthITU453AtmosphereRefraction: typing.Type[EarthITU453AtmosphereRefraction]
    EarthShape: typing.Type[EarthShape]
    EarthStandardAtmosphereRefraction: typing.Type[EarthStandardAtmosphereRefraction]
    GeoMagneticElements: typing.Type[GeoMagneticElements]
    GeoMagneticField: typing.Type[GeoMagneticField]
    GeoMagneticFieldFactory: typing.Type[GeoMagneticFieldFactory]
    GeoMagneticFields: typing.Type[GeoMagneticFields]
    GeoMagneticModelLoader: typing.Type[GeoMagneticModelLoader]
    Geoid: typing.Type[Geoid]
    LazyLoadedGeoMagneticFields: typing.Type[LazyLoadedGeoMagneticFields]
    PythonEarthShape: typing.Type[PythonEarthShape]
    PythonGeoMagneticFields: typing.Type[PythonGeoMagneticFields]
    ReferenceEllipsoid: typing.Type[ReferenceEllipsoid]
    atmosphere: org.orekit.models.earth.atmosphere.__module_protocol__
    displacement: org.orekit.models.earth.displacement.__module_protocol__
    ionosphere: org.orekit.models.earth.ionosphere.__module_protocol__
    tessellation: org.orekit.models.earth.tessellation.__module_protocol__
    troposphere: org.orekit.models.earth.troposphere.__module_protocol__
    weather: org.orekit.models.earth.weather.__module_protocol__
