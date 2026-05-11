# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's FixedTransformProviderTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.frames import FixedTransformProvider, FramesFactory, Transform
from org.orekit.time import AbsoluteDate
from org.orekit.utils import Constants


class FixedTransformProviderTest(unittest.TestCase):

    def test_eme2000(self):
        gcrf = FramesFactory.getGCRF()
        eme2000 = FramesFactory.getEME2000()
        fixed = FixedTransformProvider(
            gcrf.getTransformTo(eme2000, AbsoluteDate.J2000_EPOCH))
        dt = 0.0
        while dt < Constants.JULIAN_YEAR:
            date = AbsoluteDate.J2000_EPOCH.shiftedBy(dt)
            expected_identity = Transform(
                date, fixed.getTransform(date), eme2000.getTransformTo(gcrf, date))
            self.assertAlmostEqual(0.0,
                                   expected_identity.getTranslation().getNorm(),
                                   delta=1.0e-15)
            self.assertAlmostEqual(0.0,
                                   expected_identity.getRotation().getAngle(),
                                   delta=1.0e-15)
            dt += Constants.JULIAN_DAY


if __name__ == '__main__':
    unittest.main()
