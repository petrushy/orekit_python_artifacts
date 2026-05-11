# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's DateDriverTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.time import AbsoluteDate
from org.orekit.utils import DateDriver


class DateDriverTest(unittest.TestCase):

    def test_base(self):
        driver = DateDriver(AbsoluteDate.J2000_EPOCH, "start", True)
        self.assertEqual("start", str(driver.getName()))
        self.assertTrue(driver.isStart())
        self.assertFalse(driver.isSelected())
        self.assertAlmostEqual(0.0,
                               driver.getDate().durationFrom(AbsoluteDate.J2000_EPOCH),
                               delta=1.0e-15)
        self.assertIsNone(driver.getReferenceDate())
        driver.setNormalizedValue(0.001)
        self.assertAlmostEqual(0.001,
                               driver.getDate().durationFrom(AbsoluteDate.J2000_EPOCH),
                               delta=1.0e-15)
        self.assertEqual(float("-inf"), driver.getMinValue())
        self.assertEqual(float("inf"), driver.getMaxValue())


if __name__ == '__main__':
    unittest.main()
