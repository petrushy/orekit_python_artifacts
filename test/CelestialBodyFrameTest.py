# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's CelestialBodyFrameTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import FieldVector3D
from org.hipparchus.util import Binary64Field
from org.orekit.bodies import CelestialBodyFactory, GeodeticPoint, OneAxisEllipsoid
from org.orekit.data import DataContext
from org.orekit.errors import OrekitException, OrekitMessages
from org.orekit.files.ccsds.definitions import CelestialBodyFrame, ModifiedFrame
from org.orekit.frames import Frame, FramesFactory, ITRFVersion, TopocentricFrame
from org.orekit.frames import Transform
from org.orekit.time import AbsoluteDate, FieldAbsoluteDate
from org.orekit.utils import Constants, IERSConventions


class CelestialBodyFrameTest(unittest.TestCase):

    LATEST_ITRF_FRAME = CelestialBodyFrame.ITRF2020

    def test_map(self):
        for ccsds_frame in CelestialBodyFrame.values():
            frame = ccsds_frame.getFrame(IERSConventions.IERS_2010, True,
                                         DataContext.getDefault())
            actual = CelestialBodyFrame.map(frame)
            if ccsds_frame == CelestialBodyFrame.J2000:
                self.assertEqual(CelestialBodyFrame.EME2000, actual)
            elif ccsds_frame == CelestialBodyFrame.TDR:
                self.assertEqual(CelestialBodyFrame.GTOD, actual)
            elif ccsds_frame == CelestialBodyFrame.ITRF:
                self.assertEqual(self.LATEST_ITRF_FRAME, actual)
            else:
                self.assertEqual(ccsds_frame, actual)

        self.assertEqual(CelestialBodyFrame.GCRF,
                         CelestialBodyFrame.map(FramesFactory.getGCRF()))
        self.assertEqual(CelestialBodyFrame.EME2000,
                         CelestialBodyFrame.map(FramesFactory.getEME2000()))
        self.assertEqual(
            CelestialBodyFrame.GRC,
            CelestialBodyFrame.map(
                FramesFactory.getITRFEquinox(IERSConventions.IERS_2010, True)))
        self.assertEqual(CelestialBodyFrame.ICRF,
                         CelestialBodyFrame.map(FramesFactory.getICRF()))
        self.assertEqual(
            CelestialBodyFrame.ITRF2014,
            CelestialBodyFrame.map(
                FramesFactory.getITRF(IERSConventions.IERS_2010, True)))
        self.assertEqual(CelestialBodyFrame.GTOD,
                         CelestialBodyFrame.map(FramesFactory.getGTOD(True)))
        self.assertEqual(CelestialBodyFrame.TEME,
                         CelestialBodyFrame.map(FramesFactory.getTEME()))
        self.assertEqual(CelestialBodyFrame.TOD,
                         CelestialBodyFrame.map(FramesFactory.getTOD(True)))

        for version in ITRFVersion.values():
            name = str(version.getName()).replace("-", "")
            for conventions in IERSConventions.values():
                self.assertEqual(
                    name,
                    str(CelestialBodyFrame.map(
                        FramesFactory.getITRF(version, conventions, True)).name))
                self.assertEqual(
                    name,
                    str(CelestialBodyFrame.map(
                        FramesFactory.getITRF(version, conventions, False)).name))

        self.assertEqual(
            CelestialBodyFrame.MCI,
            CelestialBodyFrame.map(
                CelestialBodyFactory.getMars().getInertiallyOrientedFrame()))
        self.assertEqual(
            CelestialBodyFrame.ICRF,
            CelestialBodyFrame.map(
                CelestialBodyFactory.getSolarSystemBarycenter()
                .getInertiallyOrientedFrame()))

        frame = ModifiedFrame(FramesFactory.getEME2000(),
                              CelestialBodyFrame.EME2000,
                              CelestialBodyFactory.getMars(), "MARS")
        self.assertEqual(CelestialBodyFrame.EME2000, CelestialBodyFrame.map(frame))
        translation = frame.getTransformProvider().getTransform(
            AbsoluteDate.J2000_EPOCH).getTranslation()
        field_translation = frame.getTransformProvider().getTransform(
            FieldAbsoluteDate.getJ2000Epoch(Binary64Field.getInstance())
        ).getTranslation()
        self.assertAlmostEqual(0.0,
                               FieldVector3D.distance(field_translation,
                                                      translation).getReal(),
                               delta=1.0e-10)

        earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                 Constants.WGS84_EARTH_FLATTENING,
                                 FramesFactory.getITRF(IERSConventions.IERS_2010,
                                                       True))
        topo = TopocentricFrame(earth, GeodeticPoint(1.2, 2.3, 45.6), "dummy")
        with self.assertRaises(JavaError) as ctx:
            CelestialBodyFrame.map(topo)
        exception = OrekitException.cast_(ctx.exception.getJavaException())
        self.assertEqual(OrekitMessages.CCSDS_INVALID_FRAME,
                         exception.getSpecifier())
        self.assertEqual("dummy", str(exception.getParts()[0]))

        fake_icrf = Frame(
            FramesFactory.getGCRF(), Transform.IDENTITY,
            CelestialBodyFactory.SOLAR_SYSTEM_BARYCENTER + "/inertial")
        self.assertEqual(CelestialBodyFrame.ICRF, CelestialBodyFrame.map(fake_icrf))

    def test_no_conventions(self):
        no_conventions_ok = {
            CelestialBodyFrame.EME2000,
            CelestialBodyFrame.J2000,
            CelestialBodyFrame.GCRF,
            CelestialBodyFrame.ICRF,
            CelestialBodyFrame.MCI,
            CelestialBodyFrame.TEME,
        }
        for frame in CelestialBodyFrame.values():
            if frame in no_conventions_ok:
                self.assertIsNotNone(
                    frame.getFrame(None, False, DataContext.getDefault()))
            else:
                with self.assertRaises(JavaError) as ctx:
                    frame.getFrame(None, False, DataContext.getDefault())
                exception = OrekitException.cast_(ctx.exception.getJavaException())
                self.assertEqual(OrekitMessages.CCSDS_UNKNOWN_CONVENTIONS,
                                 exception.getSpecifier())

    def test_parse(self):
        self.assertEqual(CelestialBodyFrame.EME2000,
                         CelestialBodyFrame.parse("EME2000"))
        self.assertEqual(CelestialBodyFrame.ITRF2014,
                         CelestialBodyFrame.parse("ITRF2014"))
        self.assertEqual(CelestialBodyFrame.ITRF1997,
                         CelestialBodyFrame.parse("ITRF97"))
        self.assertEqual(CelestialBodyFrame.ITRF,
                         CelestialBodyFrame.parse("ITRF"))
        with self.assertRaises(Exception) as ctx:
            CelestialBodyFrame.parse("ITRF00")
        self.assertIn("ITRF00", str(ctx.exception))

    def test_guess_frame(self):
        itrf89 = FramesFactory.getITRF(ITRFVersion.ITRF_1989,
                                       IERSConventions.IERS_1996, True)
        self.assertEqual("ITRF1989", CelestialBodyFrame.guessFrame(itrf89))

        earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                 Constants.WGS84_EARTH_FLATTENING,
                                 FramesFactory.getITRF(IERSConventions.IERS_2010,
                                                       True))
        topo = TopocentricFrame(earth, GeodeticPoint(1.2, 2.3, 45.6), "dummy")
        self.assertEqual("dummy", CelestialBodyFrame.guessFrame(topo))


if __name__ == '__main__':
    unittest.main()
