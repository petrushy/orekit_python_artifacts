
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class OceanLoadingCoefficients:
    """
    Site specific coefficients for ocean loading.
    
    Instances of this class are typically created by OceanLoadingCoefficientsBLQFactory that parses files from Onsala Space Observatory files in BLQ format found in the Orekit data configuration.
    
    Instances of this class are guaranteed to be immutable
    
    Since:
        9.1
    
    Also see:
        GroundStation,
        OceanLoadingCoefficientsBLQFactory,
        OceanLoading
    """
    def __init__(self, siteName: str, siteLocation: org.orekit.bodies.GeodeticPoint, tides: typing.Union[typing.List[typing.MutableSequence['Tide']], jpype.JArray], zAmplitude: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], zPhase: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], wAmplitude: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], wPhase: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], sAmplitude: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], sPhase: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]):
        """
        Simple constructor.
        
        Arrays must be organized by species and sorted in increasing rate order.
        
        Parameters:
            siteName (String): site name
            siteLocation (GeodeticPoint): site location
            tides (Tide[][]): main tides, by species and increasing rate
            zAmplitude (double[][]): amplitude along zenith axis
            zPhase (double[][]): phase along zenith axis
            wAmplitude (double[][]): amplitude along West
            wPhase (double[][]): phase along West axis
            sAmplitude (double[][]): amplitude along South
            sPhase (double[][]): phase along South axis
        
        
        """
        ...
    def getNbSpecies(self) -> int:
        """
        Get the number of species.
        
        Returns:
            number of species
        
        
        """
        ...
    def getNbTides(self, species: int) -> int:
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
    def getSouthAmplitude(self, i: int, j: int) -> float:
        """
        Get the amplitude along South axis.
        
        Parameters:
            i (int): species
            j (int): tide in the species
        
        Returns:
            amplitude along South axis
        
        
        """
        ...
    def getSouthPhase(self, i: int, j: int) -> float:
        """
        Get the phase along South axis.
        
        Parameters:
            i (int): species
            j (int): tide in the species
        
        Returns:
            phase along South axis
        
        
        """
        ...
    def getTide(self, i: int, j: int) -> 'Tide':
        """
        Get the tide.
        
        Parameters:
            i (int): species
            j (int): tide in the species
        
        Returns:
            tide
        
        
        """
        ...
    def getWestAmplitude(self, i: int, j: int) -> float:
        """
        Get the amplitude along west axis.
        
        Parameters:
            i (int): species
            j (int): tide in the species
        
        Returns:
            amplitude along west axis
        
        
        """
        ...
    def getWestPhase(self, i: int, j: int) -> float:
        """
        Get the phase along West axis.
        
        Parameters:
            i (int): species
            j (int): tide in the species
        
        Returns:
            phase along West axis
        
        
        """
        ...
    def getZenithAmplitude(self, i: int, j: int) -> float:
        """
        Get the amplitude along zenith axis.
        
        Parameters:
            i (int): species
            j (int): tide in the species
        
        Returns:
            amplitude along zenith axis
        
        
        """
        ...
    def getZenithPhase(self, i: int, j: int) -> float:
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
    Factory for ocean loading coefficients, using Onsala Space Observatory files in BLQ format.
    
    Files in BLQ format can be generated using the form at the `Bos-Scherneck web site <http://holt.oso.chalmers.se/loading/>`, selecting BLQ as the output format.
    
    The sites names are extracted from the file content, not the file name, because the file can contain more than one station. As we expect existing files may have been stripped from headers and footers, we do not attempt to parse them. We only parse the series of 7 lines blocks starting with the lines with the station names and their coordinates and the 6 data lines that follows. Several such blocks may appear in the file. Copy-pasting the entire mail received from OSO after completing the web site form works, as intermediate lines between the 7 lines blocks are simply ignored.
    
    Since:
        9.1
    
    Also see:
        OceanLoadingCoefficients,
        OceanLoading
    """
    DEFAULT_BLQ_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default supported files name pattern for Onsala Space Observatory files in BLQ format.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, supportedNames: str): ...
    @typing.overload
    def __init__(self, supportedNames: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getCoefficients(self, site: str) -> OceanLoadingCoefficients:
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

class OceanLoadingCoefficientsBlqParser:
    """
    Parser for ocean loading coefficients, using Onsala Space Observatory files in BLQ format.
    
    Files in BLQ format can be generated using the form at the `Bos-Scherneck web site <http://holt.oso.chalmers.se/loading/>`, selecting BLQ as the output format.
    
    The sites names are extracted from the file content, not the file name, because the file can contain more than one station. As we expect existing files may have been stripped from headers and footers, we do not attempt to parse them. We only parse the series of 7 lines blocks starting with the lines with the station names and their coordinates and the 6 data lines that follows. Several such blocks may appear in the file. Copy-pasting the entire mail received from OSO after completing the web site form works, as intermediate lines between the 7 lines blocks are simply ignored.
    
    Since:
        9.1
    
    Also see:
        OceanLoadingCoefficients,
        OceanLoading
    """
    def __init__(self): ...
    def parse(self, source: org.orekit.data.DataSource) -> java.util.List[OceanLoadingCoefficients]:
        """
        Parse a BLQ file.
        
        Files in BLQ format can be generated using the form at the loading, selecting BLQ as the output format.
        
        when completing the web site form, the email received as the following form:
        
         $$ Ocean loading displacement $$ $$ Calculated on holt using olfg/olmpp of H.-G. Scherneck $$ $$ COLUMN ORDER:  M2  S2  N2  K2  K1  O1  P1  Q1  MF  MM SSA $$ $$ ROW ORDER: $$ AMPLITUDES (m) $$   RADIAL $$   TANGENTL    EW $$   TANGENTL    NS $$ PHASES (degrees) $$   RADIAL $$   TANGENTL    EW $$   TANGENTL    NS $$ $$ Displacement is defined positive in upwards, South and West direction. $$ The phase lag is relative to Greenwich and lags positive. The $$ Gutenberg-Bullen Greens function is used. In the ocean tide model the $$ deficit of tidal water mass has been corrected by subtracting a uniform $$ layer of water with a certain phase lag globally. $$ $$ Complete <model name> : No interpolation of ocean model was necessary $$ <model name>_PP       : Ocean model has been interpolated near the station $$                         (PP = Post-Processing) $$ $$ Ocean tide model: CSR4.0, long-period tides from FES99 $$ $$ END HEADER $$ Goldstone $$ Complete CSR4.0_f $$ Computed by OLFG, H.-G. Scherneck, Onsala Space Observatory 2017-Sep-28 $$ Goldstone,                 RADI TANG  lon/lat:  243.1105   35.4259    0.000 .00130 .00155 .00064 .00052 .01031 .00661 .00339 .00119 .00005 .00002 .00003 .00136 .00020 .00024 .00004 .00322 .00202 .00106 .00036 .00007 .00003 .00001 .00372 .00165 .00082 .00045 .00175 .00113 .00057 .00022 .00004 .00002 .00003 -2.7 -106.3  -62.6 -106.8   41.6   27.3   40.4   24.0 -119.1 -123.2 -169.7 -145.3  -88.4  178.5  -66.3 -130.5 -145.3 -131.7 -148.7  124.3  139.6   23.3 90.7  111.1   74.1  111.3  176.9  165.3  175.8  164.0   48.9   25.3    4.5 $$ ONSALA $$ CSR4.0_f_PP ID: 2017-09-28 15:01:14 $$ Computed by OLMPP by H G Scherneck, Onsala Space Observatory, 2017 $$ Onsala,                    RADI TANG  lon/lat:   11.9264   57.3958    0.000 .00344 .00121 .00078 .00031 .00189 .00116 .00064 .00004 .00090 .00048 .00041 .00143 .00035 .00035 .00008 .00053 .00051 .00018 .00009 .00013 .00006 .00007 .00086 .00023 .00023 .00006 .00029 .00025 .00010 .00008 .00003 .00001 .00000 -64.6  -50.3  -95.0  -53.1  -58.8 -152.4  -65.5 -133.8    9.8    5.8    2.1 85.4  115.2   56.7  114.7   99.5   15.9   94.2  -10.0 -166.3 -169.8 -177.7 110.7  147.1   93.9  148.6   49.4  -56.5   34.8 -169.9  -35.3   -3.7   10.1 $$ END TABLE Errors: Warnings:
        
        We only parse blocks 7 lines blocks starting with the lines with the station names and their coordinates and the 6 data lines that follows. Several such blocks may appear in the file.
        
        Parameters:
            source (DataSource): source for BLQ data
        
        Returns:
            parsed coefficients
        
        
        """
        ...

class PsdCorrection:
    """
    Model for post-seismic deformation corrections.
    
    Since:
        12.1
    """
    def __init__(self, axis: 'PsdCorrection.Axis', evolution: 'PsdCorrection.TimeEvolution', earthquakeDate: org.orekit.time.AbsoluteDate, amplitude: float, relaxationTime: float):
        """
        Simple constructor.
        
        Parameters:
            axis (Axis): correction axis
            evolution (TimeEvolution): time evolution
            earthquakeDate (AbsoluteDate): earthquake date
            amplitude (double): amplitude
            relaxationTime (double): relaxation time
        
        
        """
        ...
    def displacement(self, date: org.orekit.time.AbsoluteDate, base: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute displacement.
        
        Parameters:
            date (AbsoluteDate): date
            base (GeodeticPoint): base point
        
        Returns:
            displacement vector in Earth frame
        
        
        """
        ...
    def getAmplitude(self) -> float:
        """
        Get amplitude.
        
        Returns:
            amplitude
        
        
        """
        ...
    def getAxis(self) -> 'PsdCorrection.Axis':
        """
        Get correction axis.
        
        Returns:
            correction axis
        
        
        """
        ...
    def getEarthquakeDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get earthquake date.
        
        Returns:
            earthquake date
        
        
        """
        ...
    def getEvolution(self) -> 'PsdCorrection.TimeEvolution':
        """
        Get time evolution.
        
        Returns:
            time evolution
        
        
        """
        ...
    def getRelaxationTime(self) -> float:
        """
        Get relaxation time.
        
        Returns:
            relaxation time
        
        
        """
        ...
    class Axis(java.lang.Enum['PsdCorrection.Axis']):
        EAST: typing.ClassVar['PsdCorrection.Axis'] = ...
        NORTH: typing.ClassVar['PsdCorrection.Axis'] = ...
        UP: typing.ClassVar['PsdCorrection.Axis'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'PsdCorrection.Axis': ...
        @staticmethod
        def values() -> typing.MutableSequence['PsdCorrection.Axis']: ...
        def vector(self, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    class TimeEvolution(java.lang.Enum['PsdCorrection.TimeEvolution']):
        EXP: typing.ClassVar['PsdCorrection.TimeEvolution'] = ...
        LOG: typing.ClassVar['PsdCorrection.TimeEvolution'] = ...
        def timeFactor(self, double: float) -> float: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'PsdCorrection.TimeEvolution': ...
        @staticmethod
        def values() -> typing.MutableSequence['PsdCorrection.TimeEvolution']: ...

class StationDisplacement:
    """
    Interface for computing reference points displacement.
    
    Since:
        9.1
    """
    def displacement(self, elements: org.orekit.data.BodiesElements, earthFrame: org.orekit.frames.Frame, referencePoint: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute displacement of a ground reference point.
        
        Parameters:
            elements (BodiesElements): elements affecting Earth orientation
            earthFrame (Frame): Earth frame in which reference point is defined
            referencePoint (Vector3D): reference point position in earthFrame
        
        Returns:
            displacement vector to be added to referencePoint
        
        
        """
        ...

class Tide:
    """
    Class representing a tide.
    
    Since:
        9.1
    """
    M2: typing.ClassVar['Tide'] = ...
    """
    M₂ tide.
    """
    S2: typing.ClassVar['Tide'] = ...
    """
    S₂ tide.
    """
    N2: typing.ClassVar['Tide'] = ...
    """
    N₂ tide.
    """
    K2: typing.ClassVar['Tide'] = ...
    """
    K₂ tide.
    """
    K1: typing.ClassVar['Tide'] = ...
    """
    K₁ tide.
    """
    O1: typing.ClassVar['Tide'] = ...
    """
    O₁ tide.
    """
    P1: typing.ClassVar['Tide'] = ...
    """
    P₁ tide.
    """
    Q1: typing.ClassVar['Tide'] = ...
    """
    Q₁ tide.
    """
    MF: typing.ClassVar['Tide'] = ...
    """
    Mf tide.
    """
    MM: typing.ClassVar['Tide'] = ...
    """
    Mm tide.
    """
    SSA: typing.ClassVar['Tide'] = ...
    """
    Ssa tide.
    """
    @typing.overload
    def __init__(self, doodsonNumber: int): ...
    @typing.overload
    def __init__(self, cTau: int, cS: int, cH: int, cP: int, cNprime: int, cPs: int): ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getDelaunayMultipliers(self) -> typing.MutableSequence[int]:
        """
        Get the multipliers for Delaunay arguments (l, l', F, D, Ω).
        
        Beware that for tides the multipliers for Delaunay arguments have an opposite sign with respect to the convention used for nutation computation! Here, we obey the tides convention.
        
        Returns:
            multipliers for Delaunay arguments (l, l', F, D, Ω)
        
        
        """
        ...
    def getDoodsonMultipliers(self) -> typing.MutableSequence[int]:
        """
        Get the multipliers for Doodson arguments (τ, s, h, p, N', ps).
        
        Returns:
            multipliers for Doodson arguments (τ, s, h, p, N', ps)
        
        
        """
        ...
    def getDoodsonNumber(self) -> int:
        """
        Get the Doodson number.
        
        Returns:
            Doodson number
        
        
        """
        ...
    def getPhase(self, elements: org.orekit.data.BodiesElements) -> float:
        """
        Get the phase of the tide.
        
        Parameters:
            elements (BodiesElements): elements to use
        
        Returns:
            phase of the tide (radians)
        
        
        """
        ...
    def getRate(self, elements: org.orekit.data.BodiesElements) -> float:
        """
        Get the angular rate of the tide.
        
        Parameters:
            elements (BodiesElements): elements to use
        
        Returns:
            angular rate of the tide (radians/second)
        
        
        """
        ...
    def getTauMultiplier(self) -> int:
        """
        Get the multiplier for the τ Doodson argument.
        
        This multiplier identifies semi-diurnal tides (2), diurnal tides (1) and long period tides (0)
        
        Returns:
            multiplier for the τ Doodson argument
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class OceanLoading(StationDisplacement):
    """
    Modeling of displacement of reference points due to ocean loading.
    
    This class implements the same model as IERS HARDIP.F program. For a given site, this model uses a set of amplitudes and phases for the 11 main tides (M₂, S₂, N₂, K₂, K₁, O₁, P₁, Q₁, Mf, Mm, and Ssa) in BLQ format as provided by the `Bos-Scherneck web site <http://holt.oso.chalmers.se/loading/>` at Onsala Space Observatory. From these elements, additional admittances are derived using spline interpolation based on tides frequencies for a total of 342 tides, including the 11 main tides.
    
    This implementation is a complete rewrite of the original HARDISP.F program developed by Duncan Agnew and copyright 2008 IERS Conventions center. This derived work is not endorsed by the IERS conventions center. What remains from the original program is the model (spline interpolation and coefficients). The code by itself is completely different, using the underlying mathematical library for spline interpolation and the existing Orekit features for nutation arguments, time and time scales handling, tides modeling...
    
    Instances of this class are guaranteed to be immutable
    
    The original HARDISP.F program is distributed with the following notice:
    
      Copyright (C) 2008 IERS Conventions Center
    
      ================================== IERS Conventions Software License ==================================
    
      NOTICE TO USER:
    
      BY USING THIS SOFTWARE YOU ACCEPT THE FOLLOWING TERMS AND CONDITIONS WHICH APPLY TO ITS USE.
    
      1. The Software is provided by the IERS Conventions Center ("the Center").
    
      2. Permission is granted to anyone to use the Software for any purpose, including commercial applications, free of charge, subject to the conditions and restrictions listed below.
    
      3. You (the user) may adapt the Software and its algorithms for your own purposes and you may distribute the resulting "derived work" to others, provided that the derived work complies with the following requirements:
    
         a) Your work shall be clearly identified so that it cannot be mistaken for IERS Conventions software and that it has been neither distributed by nor endorsed by the Center.
    
         b) Your work (including source code) must contain descriptions of how the derived work is based upon and/or differs from the original Software.
    
         c) The name(s) of all modified routine(s) that you distribute shall be changed.
    
         d) The origin of the IERS Conventions components of your derived work must not be misrepresented; you must not claim that you wrote the original Software.
    
         e) The source code must be included for all routine(s) that you distribute.  This notice must be reproduced intact in any source distribution.
    
      4. In any published work produced by the user and which includes results achieved by using the Software, you shall acknowledge that the Software was used in obtaining those results.
    
      5. The Software is provided to the user "as is" and the Center makes no warranty as to its use or performance.   The Center does not and cannot warrant the performance or results which the user may obtain by using the Software.  The Center makes no warranties, express or implied, as to non-infringement of third party rights, merchantability, or fitness for any particular purpose.  In no event will the Center be liable to the user for any consequential, incidental, or special damages, including any lost profits or lost savings, even if a Center representative has been advised of such damages, or for any claim by any third party.
    
      Correspondence concerning IERS Conventions software should be addressed as follows:
    
                         Gerard Petit Internet email: gpetit[at]bipm.org Postal address: IERS Conventions Center Time, frequency and gravimetry section, BIPM Pavillon de Breteuil 92312 Sevres  FRANCE
    
         or
    
                         Brian Luzum Internet email: brian.luzum[at]usno.navy.mil Postal address: IERS Conventions Center Earth Orientation Department 3450 Massachusetts Ave, NW Washington, DC 20392
    
    Since:
        9.1
    
    Also see:
        GroundStation
    """
    def __init__(self, earth: org.orekit.bodies.OneAxisEllipsoid, coefficients: OceanLoadingCoefficients):
        """
        Simple constructor.
        
        Parameters:
            earth (OneAxisEllipsoid): Earth shape
            coefficients (OceanLoadingCoefficients): coefficients for the considered site
        
        Also see:
            OceanLoadingCoefficientsBLQFactory
        
        
        """
        ...
    def displacement(self, elements: org.orekit.data.BodiesElements, earthFrame: org.orekit.frames.Frame, referencePoint: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute displacement of a ground reference point.
        
        Specified by: displacement in interface StationDisplacement
        
        Parameters:
            elements (BodiesElements): elements affecting Earth orientation
            earthFrame (Frame): Earth frame in which reference point is defined
            referencePoint (Vector3D): reference point position in earthFrame
        
        Returns:
            displacement vector to be added to referencePoint
        
        
        """
        ...

class PostSeismicDeformation(StationDisplacement):
    """
    Modeling of displacement of one reference point due to post-seismic effects.
    
    Since:
        12.1
    
    Also see:
        ITRF2020
    """
    def __init__(self, base: org.orekit.bodies.GeodeticPoint, corrections: org.orekit.utils.TimeSpanMap[java.util.List[PsdCorrection]]):
        """
        Simple constructor.
        
        Parameters:
            base (GeodeticPoint): base point
            corrections (TimeSpanMap<List<PsdCorrection>>): Post-Seismic Deformation corrections
        
        
        """
        ...
    def displacement(self, elements: org.orekit.data.BodiesElements, earthFrame: org.orekit.frames.Frame, referencePoint: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute displacement of a ground reference point.
        
        Specified by: displacement in interface StationDisplacement
        
        Parameters:
            elements (BodiesElements): elements affecting Earth orientation
            earthFrame (Frame): Earth frame in which reference point is defined
            referencePoint (Vector3D): reference point position in earthFrame
        
        Returns:
            displacement vector to be added to referencePoint
        
        
        """
        ...

class PythonStationDisplacement(StationDisplacement):
    def __init__(self): ...
    def displacement(self, elements: org.orekit.data.BodiesElements, earthFrame: org.orekit.frames.Frame, referencePoint: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute displacement of a ground reference point.
        
        Specified by: displacement in interface StationDisplacement
        
        Parameters:
            elements (BodiesElements): elements affecting Earth orientation
            earthFrame (Frame): Earth frame in which reference point is defined
            referencePoint (Vector3D): reference point position in earthFrame
        
        Returns:
            displacement vector to be added to referencePoint
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class TectonicsDisplacement(StationDisplacement):
    """
    Modeling of displacement of reference points due to plate tectonics.
    
    Instances of this class are guaranteed to be immutable
    
    Since:
        12.0
    
    Also see:
        GroundStation, package
    """
    def __init__(self, epoch: org.orekit.time.AbsoluteDate, velocity: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Simple constructor.
        
        Parameters:
            velocity (AbsoluteDate): station velocity in Earth frame (m/s)
            epoch (Vector3D): coordinates reference epoch
        
        
        """
        ...
    def displacement(self, elements: org.orekit.data.BodiesElements, earthFrame: org.orekit.frames.Frame, referencePoint: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute displacement of a ground reference point.
        
        Specified by: displacement in interface StationDisplacement
        
        Parameters:
            elements (BodiesElements): elements affecting Earth orientation
            earthFrame (Frame): Earth frame in which reference point is defined
            referencePoint (Vector3D): reference point position in earthFrame
        
        Returns:
            displacement vector to be added to referencePoint
        
        
        """
        ...

class TidalDisplacement(StationDisplacement):
    """
    Modeling of displacement of reference points due to tidal effects.
    
    This class implements displacement of reference point (i.e. GroundStation) due to tidal effects, as per IERS conventions.
    
    Displacement can be computed with respect to either conventional tide free or mean tide coordinates. The difference between the two systems is about -12cm at poles and +6cm at equator. Selecting one system or the other depends on how the station coordinates have been computed (i.e. it depends whether the coordinates already include the permanent deformation or not).
    
    Instances of this class are guaranteed to be immutable
    
    Since:
        9.1
    
    Also see:
        GroundStation
    """
    def __init__(self, rEarth: float, sunEarthSystemMassRatio: float, earthMoonMassRatio: float, sun: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], moon: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], conventions: org.orekit.utils.IERSConventions, removePermanentDeformation: bool):
        """
        Simple constructor.
        
        Parameters:
            rEarth (double): Earth equatorial radius (from gravity field model)
            sunEarthSystemMassRatio (double): Sun/(Earth + Moon) mass ratio (typically JPL_SSD_SUN_EARTH_PLUS_MOON_MASS_RATIO)
            earthMoonMassRatio (double): Earth/Moon mass ratio (typically JPL_SSD_EARTH_MOON_MASS_RATIO)
            sun (PVCoordinatesProvider): Sun model
            moon (PVCoordinatesProvider): Moon model
            conventions (IERSConventions): IERS conventions to use
            removePermanentDeformation (boolean): if true, the station coordinates are considered mean tide and already include the permanent deformation, hence it
                should be removed from the displacement to avoid considering it twice; if false, the station coordinates are considered
                conventional tide free so the permanent deformation must be included in the displacement
        
        Also see:
            getITRF, getEOPHistory,
            JPL_SSD_SUN_EARTH_PLUS_MOON_MASS_RATIO,
            JPL_SSD_EARTH_MOON_MASS_RATIO
        
        
        """
        ...
    def displacement(self, elements: org.orekit.data.BodiesElements, earthFrame: org.orekit.frames.Frame, referencePoint: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute displacement of a ground reference point.
        
        Specified by: displacement in interface StationDisplacement
        
        Parameters:
            elements (BodiesElements): elements affecting Earth orientation
            earthFrame (Frame): Earth frame in which reference point is defined
            referencePoint (Vector3D): reference point position in earthFrame
        
        Returns:
            displacement vector to be added to referencePoint
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.displacement")``.

    OceanLoading: typing.Type[OceanLoading]
    OceanLoadingCoefficients: typing.Type[OceanLoadingCoefficients]
    OceanLoadingCoefficientsBLQFactory: typing.Type[OceanLoadingCoefficientsBLQFactory]
    OceanLoadingCoefficientsBlqParser: typing.Type[OceanLoadingCoefficientsBlqParser]
    PostSeismicDeformation: typing.Type[PostSeismicDeformation]
    PsdCorrection: typing.Type[PsdCorrection]
    PythonStationDisplacement: typing.Type[PythonStationDisplacement]
    StationDisplacement: typing.Type[StationDisplacement]
    TectonicsDisplacement: typing.Type[TectonicsDisplacement]
    TidalDisplacement: typing.Type[TidalDisplacement]
    Tide: typing.Type[Tide]
