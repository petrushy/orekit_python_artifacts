# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's FrameFacadeTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit import JArray_double
from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.linear import MatrixUtils
from org.orekit.data import DataContext
from org.orekit.errors import OrekitException
from org.orekit.files.ccsds.definitions import CelestialBodyFrame, FrameFacade
from org.orekit.files.ccsds.definitions import OrbitRelativeFrame, SpacecraftBodyFrame
from org.orekit.frames import FramesFactory, Transform
from org.orekit.orbits import KeplerianOrbit, PositionAngleType
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants, IERSConventions


def _enum_name(enum_value):
    name = enum_value.name
    return str(name() if callable(name) else name)


def _matrix_entry(matrix, i, j):
    return JArray_double.cast_(matrix[i])[j]


class FrameFacadeTest(unittest.TestCase):

    def test_map_celestial(self):
        for frame in CelestialBodyFrame.values():
            facade = FrameFacade.parse(
                _enum_name(frame), IERSConventions.IERS_2010, True,
                DataContext.getDefault(), True, True, True)
            self.assertEqual(frame, facade.asCelestialBodyFrame())
            self.assertIsNone(facade.asOrbitRelativeFrame())
            self.assertIsNone(facade.asSpacecraftBodyFrame())

    def test_map_lof(self):
        for frame in OrbitRelativeFrame.values():
            facade = FrameFacade.parse(
                _enum_name(frame), IERSConventions.IERS_2010, True,
                DataContext.getDefault(), True, True, True)
            self.assertIsNone(facade.asCelestialBodyFrame())
            self.assertEqual(frame, facade.asOrbitRelativeFrame())
            self.assertIsNone(facade.asSpacecraftBodyFrame())

    def test_map_spacecraft(self):
        for equipment in SpacecraftBodyFrame.BaseEquipment.values():
            for label in ["1", "2", "A", "B"]:
                body_frame = SpacecraftBodyFrame(equipment, label)
                facade = FrameFacade.parse(
                    body_frame.toString(), IERSConventions.IERS_2010, True,
                    DataContext.getDefault(), True, True, True)
                self.assertIsNone(facade.asCelestialBodyFrame())
                self.assertIsNone(facade.asOrbitRelativeFrame())
                self.assertEqual(equipment,
                                 facade.asSpacecraftBodyFrame().getBaseEquipment())
                self.assertEqual(label, facade.asSpacecraftBodyFrame().getLabel())

    def test_unknown_frame(self):
        name = "unknown"
        facade = FrameFacade.parse(name, IERSConventions.IERS_2010, True,
                                   DataContext.getDefault(), True, True, True)
        self.assertIsNone(facade.asFrame())
        self.assertIsNone(facade.asCelestialBodyFrame())
        self.assertIsNone(facade.asOrbitRelativeFrame())
        self.assertIsNone(facade.asSpacecraftBodyFrame())
        self.assertEqual(name, facade.getName())

    def test_get_transform_lof_to_lof_at_periapsis(self):
        pivot = FramesFactory.getGCRF()
        orbit = KeplerianOrbit(7.0e6, 0.001, math.radians(45.0), 0.0, 0.0, 0.0,
                               PositionAngleType.TRUE, FramesFactory.getEME2000(),
                               AbsoluteDate(2000, 1, 1, TimeScalesFactory.getUTC()),
                               Constants.GRIM5C1_EARTH_MU)

        rtn = FrameFacade(None, None, OrbitRelativeFrame.QSW, None, "RTN")
        tnw = FrameFacade(None, None, OrbitRelativeFrame.TNW, None, "TNW")

        transform = FrameFacade.getTransform(rtn, tnw, pivot, orbit.getDate(), orbit)

        expected = [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]
        actual = transform.getRotation().getMatrix()
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(expected[i][j], _matrix_entry(actual, i, j),
                                       delta=1.0e-15)

    def test_exception_non_inertial_pivot(self):
        facade_in = FrameFacade(FramesFactory.getGCRF(), None, None, None, "in")
        facade_out = FrameFacade(FramesFactory.getEME2000(), None, None, None, "out")
        non_inertial = FramesFactory.getITRF(IERSConventions.IERS_2010, True)
        with self.assertRaises(JavaError) as ctx:
            FrameFacade.getTransform(facade_in, facade_out, non_inertial,
                                     AbsoluteDate.ARBITRARY_EPOCH, None)
        OrekitException.cast_(ctx.exception.getJavaException())

    def test_exception_unsupported_frame_facade(self):
        pivot = FramesFactory.getGCRF()
        date = AbsoluteDate.ARBITRARY_EPOCH
        output = FrameFacade(FramesFactory.getEME2000(), None, None, None,
                             "Earth inertial frame")

        input_celestial = FrameFacade(None, CelestialBodyFrame.MCI, None, None,
                                      "Celestial body frame")
        with self.assertRaises(JavaError) as ctx:
            FrameFacade.getTransform(input_celestial, output, pivot, date, None)
        OrekitException.cast_(ctx.exception.getJavaException())

        body_frame = SpacecraftBodyFrame(SpacecraftBodyFrame.BaseEquipment.SC_BODY, "1")
        input_spacecraft = FrameFacade(None, None, None, body_frame,
                                       "spacecraft frame")
        with self.assertRaises(JavaError) as ctx:
            FrameFacade.getTransform(input_spacecraft, output, pivot, date, None)
        OrekitException.cast_(ctx.exception.getJavaException())

    def test_exception_null_lof_type(self):
        pivot = FramesFactory.getGCRF()
        date = AbsoluteDate.ARBITRARY_EPOCH
        input_null_lof = FrameFacade(None, None, OrbitRelativeFrame.PQW_INERTIAL,
                                     None, "null LOF")
        output = FrameFacade(FramesFactory.getEME2000(), None, None, None, "out")
        with self.assertRaises(JavaError) as ctx:
            FrameFacade.getTransform(input_null_lof, output, pivot, date, None)
        OrekitException.cast_(ctx.exception.getJavaException())

    def test_identity_after_multiple_transforms(self):
        date = AbsoluteDate()
        pivot = FramesFactory.getGCRF()
        orbit = KeplerianOrbit(7.0e6, 0.001, math.radians(45.0), 0.0, 0.0, 0.0,
                               PositionAngleType.MEAN, FramesFactory.getEME2000(),
                               date, Constants.IERS2010_EARTH_MU)

        facade_gcrf = FrameFacade(FramesFactory.getGCRF(), None, None, None,
                                  "GCRF")
        facade_qsw = FrameFacade(None, None, OrbitRelativeFrame.QSW, None, "QSW")
        facade_qsw2 = FrameFacade(None, None, OrbitRelativeFrame.QSW, None, "TNW")
        facade_itrf = FrameFacade(FramesFactory.getITRF(IERSConventions.IERS_2010,
                                                        True),
                                  None, None, None, "ITRF")

        t1 = FrameFacade.getTransform(facade_gcrf, facade_qsw, pivot, date, orbit)
        t2 = FrameFacade.getTransform(facade_qsw, facade_qsw2, pivot, date, orbit)
        t3 = FrameFacade.getTransform(facade_qsw2, facade_itrf, pivot, date, orbit)
        t4 = FrameFacade.getTransform(facade_itrf, facade_gcrf, pivot, date, orbit)

        composed = Transform(date, Transform(date, Transform(date, t1, t2), t3), t4)

        translation = composed.getTranslation()
        rotation = composed.getRotation().getMatrix()
        identity = MatrixUtils.createRealIdentityMatrix(3).getData()

        self.assertAlmostEqual(0.0, translation.getX(), delta=2.0e-9)
        self.assertAlmostEqual(0.0, translation.getY(), delta=2.0e-9)
        self.assertAlmostEqual(0.0, translation.getZ(), delta=2.0e-9)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(_matrix_entry(identity, i, j),
                                       _matrix_entry(rotation, i, j),
                                       delta=2.0e-15)


if __name__ == '__main__':
    unittest.main()
