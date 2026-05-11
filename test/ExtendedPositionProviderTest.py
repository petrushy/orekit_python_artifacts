# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's ExtendedPositionProviderTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import FieldVector3D, Vector3D
from org.orekit.frames import FramesFactory
from org.orekit.time import AbsoluteDate, FieldAbsoluteDate
from org.orekit.utils import ExtendedPositionProvider, PythonExtendedPositionProvider


_REFERENCE_DATE = AbsoluteDate.ARBITRARY_EPOCH


class TestExtendedPositionProvider(PythonExtendedPositionProvider):

    def __init__(self):
        super().__init__()

    def getPosition(self, date, frame):
        if FieldAbsoluteDate.instance_(date):
            return FieldVector3D(date.getField(), Vector3D(1.0, 2.0, 3.0))
        return Vector3D(1.0, 2.0, 3.0)


class ExtendedPositionProviderTest(unittest.TestCase):

    def assertVectorAlmostEqual(self, expected, actual, delta=1.0e-15):
        self.assertAlmostEqual(expected.getX(), actual.getX(), delta=delta)
        self.assertAlmostEqual(expected.getY(), actual.getY(), delta=delta)
        self.assertAlmostEqual(expected.getZ(), actual.getZ(), delta=delta)

    def test_get_pv_coordinates(self):
        position_provider = TestExtendedPositionProvider()
        frame = FramesFactory.getGCRF()
        date = AbsoluteDate.J2000_EPOCH

        pv_coordinates = ExtendedPositionProvider.cast_(position_provider).getPVCoordinates(
            date, frame)

        expected_position = Vector3D(1.0, 2.0, 3.0)
        self.assertVectorAlmostEqual(expected_position, pv_coordinates.getPosition())
        self.assertAlmostEqual(0.0, pv_coordinates.getVelocity().getNorm(),
                               delta=1.0e-15)
        self.assertAlmostEqual(0.0, pv_coordinates.getAcceleration().getNorm(),
                               delta=1.0e-15)


if __name__ == '__main__':
    unittest.main()
