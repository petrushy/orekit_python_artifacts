# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java AccurateFormatterTest."""

import math
import unittest

import orekit
orekit.initVM()

from org.orekit.utils import AccurateFormatter


class AccurateFormatterTest(unittest.TestCase):

    def assertNumberCases(self, formatter):
        cases = (
            ("4.940656E-318", 4.940656E-318),
            ("1.18575755E-316", 1.18575755E-316),
            ("2.989102097996E-312", 2.989102097996E-312),
            ("9.0608011534336E15", 9.0608011534336E15),
            ("4.708356024711512E18", 4.708356024711512E18),
            ("9.409340012568248E18", 9.409340012568248E18),
            ("1.8531501765868567E21", 1.8531501765868567E21),
            ("-3.347727380279489E33", -3.347727380279489E33),
            ("-6.9741824662760956E19", -6.9741824662760956E19),
            ("4.3816050601147837E18", 4.3816050601147837E18),
        )
        for expected, value in cases:
            self.assertEqual(expected, formatter(value))

    def testNumberStatic(self):
        self.assertNumberCases(AccurateFormatter.format)

    def testDateNonTruncatedStatic(self):
        self.assertEqual("2021-03-26T09:45:32.4576",
                         AccurateFormatter.format(2021, 3, 26, 9, 45, 32.4576))
        self.assertEqual("2021-03-26T09:45:00.00000000000001",
                         AccurateFormatter.format(2021, 3, 26, 9, 45, 1.0e-14))

    def testDateTruncatedStatic(self):
        self.assertEqual("2021-03-26T09:45:00.0",
                         AccurateFormatter.format(2021, 3, 26, 9, 45, 1.0e-16))

    def testNumber(self):
        formatter = AccurateFormatter()
        self.assertNumberCases(formatter.toString)

    def testDateNonTruncated(self):
        formatter = AccurateFormatter()
        self.assertEqual("2021-03-26T09:45:32.4576",
                         formatter.toString(2021, 3, 26, 9, 45, 32.4576))
        self.assertEqual("2021-03-26T09:45:00.00000000000001",
                         formatter.toString(2021, 3, 26, 9, 45, 1.0e-14))

    def testDateTruncated(self):
        self.assertEqual("2021-03-26T09:45:00.0",
                         AccurateFormatter().toString(2021, 3, 26, 9, 45, 1.0e-16))

    def testInvalidEdgeCases(self):
        formatter = AccurateFormatter()
        self.assertEqual("2021-03-26T09:45:59.99999999999999",
                         formatter.toString(2021, 3, 26, 9, 45,
                                            math.nextafter(60.0, -math.inf)))
        self.assertEqual("20210-300-260T900:450:600.0",
                         formatter.toString(20210, 300, 260, 900, 450, 600.0))
        self.assertEqual("-2021--3--26T-9:-45:00.0",
                         formatter.toString(-2021, -3, -26, -9, -45, -1.0))


if __name__ == '__main__':
    unittest.main()
