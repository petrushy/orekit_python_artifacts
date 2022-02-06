import java.util
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.utils
import typing



class OceanLoadingCoefficients:
    """
    public class OceanLoadingCoefficients extends Object
    
        Site specific coefficients for ocean loading.
    
        Instances of this class are typically created by
        :class:`~org.orekit.models.earth.displacement.OceanLoadingCoefficientsBLQFactory` that parses files from Onsala Space
        Observatory files in BLQ format found in the Orekit data configuration.
    
        Instances of this class are guaranteed to be immutable
    
        Since:
            9.1
    
        Also see:
            :class:`~org.orekit.estimation.measurements.GroundStation`,
            :class:`~org.orekit.models.earth.displacement.OceanLoadingCoefficientsBLQFactory`,
            :class:`~org.orekit.models.earth.displacement.OceanLoading`
    """
    def __init__(self, string: str, geodeticPoint: org.orekit.bodies.GeodeticPoint, tideArray: typing.List[typing.List['Tide']], doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[typing.List[float]], doubleArray4: typing.List[typing.List[float]], doubleArray5: typing.List[typing.List[float]], doubleArray6: typing.List[typing.List[float]]): ...
    def getNbSpecies(self) -> int:
        """
            Get the number of species.
        
            Returns:
                number of species
        
        
        """
        ...
    def getNbTides(self, int: int) -> int:
        """
            Get the number of tides for one species.
        
            Parameters:
                species (int): species index
        
            Returns:
                number of tides for one species
        
        
        """
        ...
    def getSiteLocation(self) -> org.orekit.bodies.GeodeticPoint:
        """
            Get the site location.
        
            Returns:
                site location
        
        
        """
        ...
    def getSiteName(self) -> str:
        """
            Get the site name.
        
            Returns:
                site name
        
        
        """
        ...
    def getSouthAmplitude(self, int: int, int2: int) -> float:
        """
            Get the amplitude along South axis.
        
            Parameters:
                i (int): species
                j (int): tide in the species
        
            Returns:
                amplitude along South axis
        
        
        """
        ...
    def getSouthPhase(self, int: int, int2: int) -> float:
        """
            Get the phase along South axis.
        
            Parameters:
                i (int): species
                j (int): tide in the species
        
            Returns:
                phase along South axis
        
        
        """
        ...
    def getTide(self, int: int, int2: int) -> 'Tide':
        """
            Get the tide.
        
            Parameters:
                i (int): species
                j (int): tide in the species
        
            Returns:
                tide
        
        
        """
        ...
    def getWestAmplitude(self, int: int, int2: int) -> float:
        """
            Get the amplitude along west axis.
        
            Parameters:
                i (int): species
                j (int): tide in the species
        
            Returns:
                amplitude along west axis
        
        
        """
        ...
    def getWestPhase(self, int: int, int2: int) -> float:
        """
            Get the phase along West axis.
        
            Parameters:
                i (int): species
                j (int): tide in the species
        
            Returns:
                phase along West axis
        
        
        """
        ...
    def getZenithAmplitude(self, int: int, int2: int) -> float:
        """
            Get the amplitude along zenith axis.
        
            Parameters:
                i (int): species
                j (int): tide in the species
        
            Returns:
                amplitude along zenith axis
        
        
        """
        ...
    def getZenithPhase(self, int: int, int2: int) -> float:
        """
            Get the phase along zenith axis.
        
            Parameters:
                i (int): species
                j (int): tide in the species
        
            Returns:
                phase along zenith axis
        
        
        """
        ...

class OceanLoadingCoefficientsBLQFactory(org.orekit.data.AbstractSelfFeedingLoader):
    """
    public class OceanLoadingCoefficientsBLQFactory extends :class:`~org.orekit.data.AbstractSelfFeedingLoader`
    
        Factory for ocean loading coefficients, using Onsala Space Observatory files in BLQ format.
    
        Files in BLQ format can be generated using the form at the `Bos-Scherneck web site
        <http://holt.oso.chalmers.se/loading/>`, selecting BLQ as the output format.
    
        The sites names are extracted from the file content, not the file name, because the file can contain more than one
        station. As we expect existing files may have been stripped from headers and footers, we do not attempt to parse them.
        We only parse the series of 7 lines blocks starting with the lines with the station names and their coordinates and the
        6 data lines that follows. Several such blocks may appear in the file. Copy-pasting the entire mail received from OSO
        after completing the web site form works, as intermediate lines between the 7 lines blocks are simply ignored.
    
        Since:
            9.1
    
        Also see:
            :class:`~org.orekit.models.earth.displacement.OceanLoadingCoefficients`,
            :class:`~org.orekit.models.earth.displacement.OceanLoading`
    """
    DEFAULT_BLQ_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_BLQ_SUPPORTED_NAMES
    
        Default supported files name pattern for Onsala Space Observatory files in BLQ format.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getCoefficients(self, string: str) -> OceanLoadingCoefficients:
        """
            Get the coefficients for a given site.
        
            Parameters:
                site (String): site name (as it appears in the Onsala Space Observatory files in BLQ format), ignoring case
        
            Returns:
                coefficients for the site
        
        
        """
        ...
    def getSites(self) -> java.util.List[str]:
        """
            Get the list of sites for which we have found coefficients, in lexicographic order ignoring case.
        
            Returns:
                list of sites for which we have found coefficients, in lexicographic order ignoring case
        
        
        """
        ...

class StationDisplacement:
    """
    public interface StationDisplacement
    
        Interface for computing reference points displacement.
    
        Since:
            9.1
    """
    def displacement(self, bodiesElements: org.orekit.data.BodiesElements, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute displacement of a ground reference point.
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): elements affecting Earth orientation
                earthFrame (:class:`~org.orekit.frames.Frame`): Earth frame in which reference point is defined
                referencePoint (Vector3D): reference point position in :code:`earthFrame`
        
            Returns:
                displacement vector to be *added* to :code:`referencePoint`
        
        
        """
        ...

class Tide:
    """
    public class Tide extends Object
    
        Class representing a tide.
    
        Since:
            9.1
    """
    M2: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` M2
    
        Mâ‚‚ tide.
    
    """
    S2: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` S2
    
        Sâ‚‚ tide.
    
    """
    N2: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` N2
    
        Nâ‚‚ tide.
    
    """
    K2: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` K2
    
        Kâ‚‚ tide.
    
    """
    K1: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` K1
    
        Kâ‚� tide.
    
    """
    O1: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` O1
    
        Oâ‚� tide.
    
    """
    P1: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` P1
    
        Pâ‚� tide.
    
    """
    Q1: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` Q1
    
        Qâ‚� tide.
    
    """
    MF: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` MF
    
        Mf tide.
    
    """
    MM: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` MM
    
        Mm tide.
    
    """
    SSA: typing.ClassVar['Tide'] = ...
    """
    public static final :class:`~org.orekit.models.earth.displacement.Tide` SSA
    
        Ssa tide.
    
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getDelaunayMultipliers(self) -> typing.List[int]:
        """
            Get the multipliers for Delaunay arguments (l, l', F, D, Î©).
        
            Beware that for tides the multipliers for Delaunay arguments have an opposite sign with respect to the convention used
            for nutation computation! Here, we obey the tides convention.
        
            Returns:
                multipliers for Delaunay arguments (l, l', F, D, Î©)
        
        
        """
        ...
    def getDoodsonMultipliers(self) -> typing.List[int]:
        """
            Get the multipliers for Doodson arguments (Ï„, s, h, p, N', ps).
        
            Returns:
                multipliers for Doodson arguments (Ï„, s, h, p, N', ps)
        
        
        """
        ...
    def getDoodsonNumber(self) -> int:
        """
            Get the Doodson number.
        
            Returns:
                Doodson number
        
        
        """
        ...
    def getPhase(self, bodiesElements: org.orekit.data.BodiesElements) -> float:
        """
            Get the phase of the tide.
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): elements to use
        
            Returns:
                phase of the tide (radians)
        
        
        """
        ...
    def getRate(self, bodiesElements: org.orekit.data.BodiesElements) -> float:
        """
            Get the angular rate of the tide.
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): elements to use
        
            Returns:
                angular rate of the tide (radians/second)
        
        
        """
        ...
    def getTauMultiplier(self) -> int:
        """
            Get the multiplier for the Ï„ Doodson argument.
        
            This multiplier identifies semi-diurnal tides (2), diurnal tides (1) and long period tides (0)
        
            Returns:
                multiplier for the Ï„ Doodson argument
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class OceanLoading(StationDisplacement):
    """
    public class OceanLoading extends Object implements :class:`~org.orekit.models.earth.displacement.StationDisplacement`
    
        Modeling of displacement of reference points due to ocean loading.
    
        This class implements the same model as IERS HARDIP.F program. For a given site, this model uses a set of amplitudes and
        phases for the 11 main tides (MÃ¢â€šâ€š, SÃ¢â€šâ€š, NÃ¢â€šâ€š, KÃ¢â€šâ€š, KÃ¢â€šï¿½, OÃ¢â€šï¿½, PÃ¢â€šï¿½, QÃ¢â€šï¿½,
        Mf, Mm, and Ssa) in BLQ format as provided by the `Bos-Scherneck web site <http://holt.oso.chalmers.se/loading/>` at
        Onsala Space Observatory. From these elements, additional admittances are derived using spline interpolation based on
        tides frequencies for a total of 342 tides, including the 11 main tides.
    
        This implementation is a complete rewrite of the original HARDISP.F program developed by Duncan Agnew and copyright 2008
        IERS Conventions center. This derived work is not endorsed by the IERS conventions center. What remains from the
        original program is the model (spline interpolation and coefficients). The code by itself is completely different, using
        the underlying mathematical library for spline interpolation and the existing Orekit features for nutation arguments,
        time and time scales handling, tides modeling...
    
        Instances of this class are guaranteed to be immutable
    
        The original HARDISP.F program is distributed with the following notice:
    
        .. code-block: java
        
        
          Copyright (C) 2008
          IERS Conventions Center
        
          ==================================
          IERS Conventions Software License
          ==================================
        
          NOTICE TO USER:
        
          BY USING THIS SOFTWARE YOU ACCEPT THE FOLLOWING TERMS AND CONDITIONS
          WHICH APPLY TO ITS USE.
        
          1. The Software is provided by the IERS Conventions Center ("the
             Center").
        
          2. Permission is granted to anyone to use the Software for any
             purpose, including commercial applications, free of charge,
             subject to the conditions and restrictions listed below.
        
          3. You (the user) may adapt the Software and its algorithms for your
             own purposes and you may distribute the resulting "derived work"
             to others, provided that the derived work complies with the
             following requirements:
        
             a) Your work shall be clearly identified so that it cannot be
                mistaken for IERS Conventions software and that it has been
                neither distributed by nor endorsed by the Center.
        
             b) Your work (including source code) must contain descriptions of
                how the derived work is based upon and/or differs from the
                original Software.
        
             c) The name(s) of all modified routine(s) that you distribute
                shall be changed.
        
             d) The origin of the IERS Conventions components of your derived
                work must not be misrepresented; you must not claim that you
                wrote the original Software.
        
             e) The source code must be included for all routine(s) that you
                distribute.  This notice must be reproduced intact in any
                source distribution.
        
          4. In any published work produced by the user and which includes
             results achieved by using the Software, you shall acknowledge
             that the Software was used in obtaining those results.
        
          5. The Software is provided to the user "as is" and the Center makes
             no warranty as to its use or performance.   The Center does not
             and cannot warrant the performance or results which the user may
             obtain by using the Software.  The Center makes no warranties,
             express or implied, as to non-infringement of third party rights,
             merchantability, or fitness for any particular purpose.  In no
             event will the Center be liable to the user for any consequential,
             incidental, or special damages, including any lost profits or lost
             savings, even if a Center representative has been advised of such
             damages, or for any claim by any third party.
        
          Correspondence concerning IERS Conventions software should be
          addressed as follows:
        
                             Gerard Petit
             Internet email: gpetit[at]bipm.org
             Postal address: IERS Conventions Center
                             Time, frequency and gravimetry section, BIPM
                             Pavillon de Breteuil
                             92312 Sevres  FRANCE
        
             or
        
                             Brian Luzum
             Internet email: brian.luzum[at]usno.navy.mil
             Postal address: IERS Conventions Center
                             Earth Orientation Department
                             3450 Massachusetts Ave, NW
                             Washington, DC 20392
         
    
        Since:
            9.1
    
        Also see:
            :class:`~org.orekit.estimation.measurements.GroundStation`
    """
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, oceanLoadingCoefficients: OceanLoadingCoefficients): ...
    def displacement(self, bodiesElements: org.orekit.data.BodiesElements, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute displacement of a ground reference point.
        
            Specified by:
                :meth:`~org.orekit.models.earth.displacement.StationDisplacement.displacement`Â in
                interfaceÂ :class:`~org.orekit.models.earth.displacement.StationDisplacement`
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): elements affecting Earth orientation
                earthFrame (:class:`~org.orekit.frames.Frame`): Earth frame in which reference point is defined
                referencePoint (Vector3D): reference point position in :code:`earthFrame`
        
            Returns:
                displacement vector to be *added* to :code:`referencePoint`
        
        
        """
        ...

class PythonStationDisplacement(StationDisplacement):
    """
    public class PythonStationDisplacement extends Object implements :class:`~org.orekit.models.earth.displacement.StationDisplacement`
    """
    def __init__(self): ...
    def displacement(self, bodiesElements: org.orekit.data.BodiesElements, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute displacement of a ground reference point.
        
            Specified by:
                :meth:`~org.orekit.models.earth.displacement.StationDisplacement.displacement`Â in
                interfaceÂ :class:`~org.orekit.models.earth.displacement.StationDisplacement`
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): elements affecting Earth orientation
                earthFrame (:class:`~org.orekit.frames.Frame`): Earth frame in which reference point is defined
                referencePoint (Vector3D): reference point position in :code:`earthFrame`
        
            Returns:
                displacement vector to be *added* to :code:`referencePoint`
        
        
        """
        ...
    def finalize(self) -> None: ...
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

class TidalDisplacement(StationDisplacement):
    """
    public class TidalDisplacement extends Object implements :class:`~org.orekit.models.earth.displacement.StationDisplacement`
    
        Modeling of displacement of reference points due to tidal effects.
    
        This class implements displacement of reference point (i.e. :class:`~org.orekit.estimation.measurements.GroundStation`)
        due to tidal effects, as per IERS conventions.
    
        Displacement can be computed with respect to either *conventional tide free* or *mean tide* coordinates. The difference
        between the two systems is about -12cm at poles and +6cm at equator. Selecting one system or the other depends on how
        the station coordinates have been computed (i.e. it depends whether the coordinates already include the permanent
        deformation or not).
    
        Instances of this class are guaranteed to be immutable
    
        Since:
            9.1
    
        Also see:
            :class:`~org.orekit.estimation.measurements.GroundStation`
    """
    def __init__(self, double: float, double2: float, double3: float, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, pVCoordinatesProvider2: org.orekit.utils.PVCoordinatesProvider, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool): ...
    def displacement(self, bodiesElements: org.orekit.data.BodiesElements, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute displacement of a ground reference point.
        
            Specified by:
                :meth:`~org.orekit.models.earth.displacement.StationDisplacement.displacement`Â in
                interfaceÂ :class:`~org.orekit.models.earth.displacement.StationDisplacement`
        
            Parameters:
                elements (:class:`~org.orekit.data.BodiesElements`): elements affecting Earth orientation
                earthFrame (:class:`~org.orekit.frames.Frame`): Earth frame in which reference point is defined
                referencePoint (Vector3D): reference point position in :code:`earthFrame`
        
            Returns:
                displacement vector to be *added* to :code:`referencePoint`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.displacement")``.

    OceanLoading: typing.Type[OceanLoading]
    OceanLoadingCoefficients: typing.Type[OceanLoadingCoefficients]
    OceanLoadingCoefficientsBLQFactory: typing.Type[OceanLoadingCoefficientsBLQFactory]
    PythonStationDisplacement: typing.Type[PythonStationDisplacement]
    StationDisplacement: typing.Type[StationDisplacement]
    TidalDisplacement: typing.Type[TidalDisplacement]
    Tide: typing.Type[Tide]
