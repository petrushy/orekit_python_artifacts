# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's BoundedPVCoordinatesProviderTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.frames import FramesFactory
from org.orekit.time import AbsoluteDate, TimeInterval
from org.orekit.utils import (
    BoundedPVCoordinatesProvider,
    PVCoordinates,
    PythonPVCoordinatesProvider,
    TimeStampedPVCoordinates,
)


class TestProvider(PythonPVCoordinatesProvider):

    def __init__(self):
        super().__init__()

    def getPVCoordinates(self, date, frame):
        return TimeStampedPVCoordinates(date,
                                        PVCoordinates(Vector3D.MINUS_I,
                                                      Vector3D.MINUS_K))

    def getPosition(self, date, frame):
        return Vector3D.MINUS_I


class BoundedPVCoordinatesProviderTest(unittest.TestCase):

    def assertDateEqual(self, expected, actual):
        self.assertAlmostEqual(0.0, actual.durationFrom(expected), delta=1.0e-15)

    def test_of(self):
        provider = TestProvider()
        min_date = AbsoluteDate.J2000_EPOCH
        max_date = min_date.shiftedBy(1.0)
        interval = TimeInterval.of(min_date, max_date)

        bounded = BoundedPVCoordinatesProvider.of(provider, interval)

        self.assertDateEqual(max_date, bounded.getMaxDate())
        self.assertDateEqual(min_date, bounded.getMinDate())

        frame = FramesFactory.getGCRF()
        self.assertEqual(Vector3D.MINUS_I, bounded.getPosition(min_date, frame))
        self.assertEqual(Vector3D.MINUS_K,
                         bounded.getPVCoordinates(min_date, frame).getVelocity())


if __name__ == '__main__':
    unittest.main()
