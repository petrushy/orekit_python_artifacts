# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's ShiftingPVCoordinatesProviderTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit, PositionAngleType
from org.orekit.time import AbsoluteDate
from org.orekit.utils import ShiftingPVCoordinatesProvider


class ShiftingPVCoordinatesProviderTest(unittest.TestCase):

    def test_get_position(self):
        mu = 3.9860047e14
        orbit = KeplerianOrbit(7000000.0, 0.001, 0.5, 0.1, 0.2, 0.3,
                               PositionAngleType.MEAN,
                               FramesFactory.getEME2000(),
                               AbsoluteDate.ARBITRARY_EPOCH, mu)

        pv_provider = ShiftingPVCoordinatesProvider(orbit.getPVCoordinates(),
                                                    orbit.getFrame())
        frame = FramesFactory.getEME2000()
        shifted_date = orbit.getDate().shiftedBy(1000.0)

        position = pv_provider.getPosition(shifted_date, frame)
        shifted_pv = pv_provider.getPVCoordinates(shifted_date, frame)

        self.assertAlmostEqual(shifted_pv.getPosition().getX(), position.getX(),
                               delta=1.0e-9)
        self.assertAlmostEqual(shifted_pv.getPosition().getY(), position.getY(),
                               delta=1.0e-9)
        self.assertAlmostEqual(shifted_pv.getPosition().getZ(), position.getZ(),
                               delta=1.0e-9)


if __name__ == '__main__':
    unittest.main()
