# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's ExtendedPositionProviderAdapterTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.bodies import CelestialBodyFactory
from org.orekit.frames import FramesFactory
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants, ExtendedPositionProviderAdapter


class ExtendedPositionProviderAdapterTest(unittest.TestCase):

    def test_double(self):
        eme2000 = FramesFactory.getEME2000()
        moon = CelestialBodyFactory.getMoon()
        moon_frame = ExtendedPositionProviderAdapter(eme2000, moon, "moon-frame")

        t0 = AbsoluteDate("2000-01-22T13:30:00", TimeScalesFactory.getUTC())
        max_p = 0.0
        max_v = 0.0
        max_a = 0.0
        max_r = 0.0

        dt = 0.0
        while dt < Constants.JULIAN_DAY:
            t = t0.shiftedBy(dt)
            pv = moon.getPVCoordinates(t, moon_frame)
            max_p = max(max_p, pv.getPosition().getNorm())
            max_v = max(max_v, pv.getVelocity().getNorm())
            max_a = max(max_a, pv.getAcceleration().getNorm())
            max_r = max(max_r,
                        moon_frame.getTransformTo(eme2000, t).getRotation().getAngle())
            dt += 60.0

        self.assertAlmostEqual(0.0, max_p, delta=5.0e-7)
        self.assertAlmostEqual(0.0, max_v, delta=1.1e-12)
        self.assertAlmostEqual(0.0, max_a, delta=2.8e-18)
        self.assertAlmostEqual(0.0, max_r, delta=1.0e-30)


if __name__ == '__main__':
    unittest.main()
