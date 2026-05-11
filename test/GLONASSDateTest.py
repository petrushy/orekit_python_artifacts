# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's GLONASSDateTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.time import AbsoluteDate, DateComponents, GLONASSDate
from org.orekit.time import TimeComponents, TimeScalesFactory


class GLONASSDateTest(unittest.TestCase):

    def setUp(self):
        self.glo = TimeScalesFactory.getGLONASS()

    def test_from_na_and_n4(self):
        date = GLONASSDate(251, 5, 7200.0)
        ref = AbsoluteDate(DateComponents(2012, 9, 7),
                           TimeComponents(2, 0, 0.0),
                           self.glo)
        self.assertEqual(251, date.getDayNumber())
        self.assertEqual(5, date.getIntervalNumber())
        self.assertAlmostEqual(2456177.5, date.getJD0(), delta=1.0e-16)
        self.assertAlmostEqual(29191.442830, date.getGMST(), delta=3.0e-3)
        self.assertAlmostEqual(0.0, date.getDate().durationFrom(ref), delta=1.0e-15)

    def test_from_absolute_date(self):
        date = GLONASSDate(AbsoluteDate(DateComponents(2012, 9, 7),
                                        TimeComponents(2, 0, 0.0),
                                        self.glo))
        self.assertEqual(251, date.getDayNumber())
        self.assertEqual(5, date.getIntervalNumber())
        self.assertAlmostEqual(2456177.5, date.getJD0(), delta=1.0e-16)
        self.assertAlmostEqual(29191.442830, date.getGMST(), delta=3.0e-3)
        self.assertAlmostEqual(7200.0, date.getSecInDay(), delta=1.0e-15)


if __name__ == '__main__':
    unittest.main()
