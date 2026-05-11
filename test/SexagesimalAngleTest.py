# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java SexagesimalAngleTest."""

import math
import unittest

import orekit
orekit.initVM()

from org.orekit.bodies import SexagesimalAngle


class SexagesimalAngleTest(unittest.TestCase):

    def testZeroDMS(self):
        self.assertAlmostEqual(0.0, SexagesimalAngle(1, 0, 0, 0.0).getAngle(),
                               delta=1.0e-15)

    def testZeroRadians(self):
        angle = SexagesimalAngle(0.0)
        self.assertEqual(1, angle.getSign())
        self.assertEqual(0, angle.getDegree())
        self.assertEqual(0, angle.getArcMinute())
        self.assertAlmostEqual(0.0, angle.getArcSecond(), delta=1.0e-15)

    def testPositiveRightAngleDMS(self):
        self.assertAlmostEqual(math.pi / 2.0,
                               SexagesimalAngle(1, 90, 0, 0.0).getAngle(),
                               delta=1.0e-15)

    def testPositiveRightAngleRadians(self):
        angle = SexagesimalAngle(math.pi / 2.0)
        self.assertEqual(1, angle.getSign())
        self.assertEqual(90, angle.getDegree())
        self.assertEqual(0, angle.getArcMinute())
        self.assertAlmostEqual(0.0, angle.getArcSecond(), delta=1.0e-15)

    def testNegativeRightAngleDMS(self):
        self.assertAlmostEqual(-math.pi / 2.0,
                               SexagesimalAngle(-1, 90, 0, 0.0).getAngle(),
                               delta=1.0e-15)

    def testNegativeRightAngleRadians(self):
        angle = SexagesimalAngle(-math.pi / 2.0)
        self.assertEqual(-1, angle.getSign())
        self.assertEqual(90, angle.getDegree())
        self.assertEqual(0, angle.getArcMinute())
        self.assertAlmostEqual(0.0, angle.getArcSecond(), delta=1.0e-15)

    def testIter(self):
        expected = [
            "00W 10\u2032 15.0\u2033", "00W 09\u2032 45.0\u2033",
            "00W 09\u2032 15.0\u2033", "00W 08\u2032 45.0\u2033",
            "00W 08\u2032 15.0\u2033", "00W 07\u2032 45.0\u2033",
            "00W 07\u2032 15.0\u2033", "00W 06\u2032 45.0\u2033",
            "00W 06\u2032 15.0\u2033", "00W 05\u2032 45.0\u2033",
            "00W 05\u2032 15.0\u2033", "00W 04\u2032 45.0\u2033",
            "00W 04\u2032 15.0\u2033", "00W 03\u2032 45.0\u2033",
            "00W 03\u2032 15.0\u2033", "00W 02\u2032 45.0\u2033",
            "00W 02\u2032 15.0\u2033", "00W 01\u2032 45.0\u2033",
            "00W 01\u2032 15.0\u2033", "00W 00\u2032 45.0\u2033",
            "00W 00\u2032 15.0\u2033", "00E 00\u2032 15.0\u2033",
            "00E 00\u2032 45.0\u2033", "00E 01\u2032 15.0\u2033",
            "00E 01\u2032 45.0\u2033", "00E 02\u2032 15.0\u2033",
            "00E 02\u2032 45.0\u2033", "00E 03\u2032 15.0\u2033",
            "00E 03\u2032 45.0\u2033", "00E 04\u2032 15.0\u2033",
            "00E 04\u2032 45.0\u2033", "00E 05\u2032 15.0\u2033",
            "00E 05\u2032 45.0\u2033", "00E 06\u2032 15.0\u2033",
            "00E 06\u2032 45.0\u2033", "00E 07\u2032 15.0\u2033",
            "00E 07\u2032 45.0\u2033", "00E 08\u2032 15.0\u2033",
            "00E 08\u2032 45.0\u2033", "00E 09\u2032 15.0\u2033",
            "00E 09\u2032 45.0\u2033", "00E 10\u2032 15.0\u2033",
        ]

        for i, expected_value in enumerate(expected):
            angle = SexagesimalAngle(math.radians(30.0 / 3600.0) * (i - 20.5))
            formatted = "%02d%s %02d\u2032 %04.1f\u2033" % (
                angle.getDegree(),
                "W" if angle.getSign() < 0 else "E",
                angle.getArcMinute(),
                angle.getArcSecond(),
            )
            self.assertEqual(expected_value, formatted)


if __name__ == '__main__':
    unittest.main()
