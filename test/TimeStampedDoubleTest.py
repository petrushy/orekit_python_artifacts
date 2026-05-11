# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's TimeStampedDoubleTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.time import AbsoluteDate, TimeStampedDouble


class TimeStampedDoubleTest(unittest.TestCase):

    def assertDateEqual(self, expected, actual):
        self.assertEqual(0.0, actual.durationFrom(expected))

    def testConstructor(self):
        date = AbsoluteDate.J2000_EPOCH
        tsd = TimeStampedDouble(date, 1.68)
        self.assertDateEqual(date, tsd.getDate())
        self.assertEqual(1.68, tsd.getValue())

    def testDeprecatedConstructor(self):
        date = AbsoluteDate.J2000_EPOCH
        tsd = TimeStampedDouble(1.68, date)
        self.assertDateEqual(date, tsd.getDate())
        self.assertEqual(1.68, tsd.getValue())

    def testToString(self):
        date = AbsoluteDate.J2000_EPOCH
        tsd = TimeStampedDouble(date, 1.68)
        self.assertEqual("{date=2000-01-01T11:58:55.816Z, value=1.68}",
                         tsd.toString())


if __name__ == '__main__':
    unittest.main()
