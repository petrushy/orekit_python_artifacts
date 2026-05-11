# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's AnalyticalSolarPositionProviderTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import AnalyticalSolarPositionProvider, CelestialBodyFactory
from org.orekit.frames import FramesFactory
from org.orekit.time import AbsoluteDate, DateTimeComponents, TimeScalesFactory


class AnalyticalSolarPositionProviderTest(unittest.TestCase):

    def test_get_position(self):
        solar_position_provider = AnalyticalSolarPositionProvider()
        frame = FramesFactory.getGCRF()
        celestial_body = CelestialBodyFactory.getSun()

        for month in range(1, 6):
            date = AbsoluteDate(DateTimeComponents(2000, month, 1, 0, 0, 0.0),
                                TimeScalesFactory.getUTC())
            actual_position = solar_position_provider.getPosition(date, frame)
            expected_position = celestial_body.getPosition(date, frame)

            self.assertAlmostEqual(0.0, Vector3D.angle(expected_position, actual_position),
                                   delta=5.0e-5)
            self.assertAlmostEqual(0.0,
                                   expected_position.subtract(actual_position).getNorm(),
                                   delta=1.0e7)


if __name__ == '__main__':
    unittest.main()
