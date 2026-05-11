# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java MonthTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from org.orekit.time import Month


class MonthTest(unittest.TestCase):

    MONTHS = (
        (Month.JANUARY, "JANUARY", "january", "January", "JAN", "jan", "Jan"),
        (Month.FEBRUARY, "FEBRUARY", "february", "February", "FEB", "feb", "Feb"),
        (Month.MARCH, "MARCH", "march", "March", "MAR", "mar", "Mar"),
        (Month.APRIL, "APRIL", "april", "April", "APR", "apr", "Apr"),
        (Month.MAY, "MAY", "may", "May", "MAY", "may", "May"),
        (Month.JUNE, "JUNE", "june", "June", "JUN", "jun", "Jun"),
        (Month.JULY, "JULY", "july", "July", "JUL", "jul", "Jul"),
        (Month.AUGUST, "AUGUST", "august", "August", "AUG", "aug", "Aug"),
        (Month.SEPTEMBER, "SEPTEMBER", "september", "September", "SEP", "sep", "Sep"),
        (Month.OCTOBER, "OCTOBER", "october", "October", "OCT", "oct", "Oct"),
        (Month.NOVEMBER, "NOVEMBER", "november", "November", "NOV", "nov", "Nov"),
        (Month.DECEMBER, "DECEMBER", "december", "December", "DEC", "dec", "Dec"),
    )

    def testUpperCaseName(self):
        for month, expected, *_ in self.MONTHS:
            self.assertEqual(expected, month.getUpperCaseName())

    def testLowerCaseName(self):
        for month, _, expected, *_ in self.MONTHS:
            self.assertEqual(expected, month.getLowerCaseName())

    def testCapitalizedCaseName(self):
        for month, _, __, expected, *_ in self.MONTHS:
            self.assertEqual(expected, month.getCapitalizedName())

    def testUpperCaseAbbreviation(self):
        for month, _, __, ___, expected, *____ in self.MONTHS:
            self.assertEqual(expected, month.getUpperCaseAbbreviation())

    def testLowerCaseAbbreviation(self):
        for month, _, __, ___, ____, expected, _____ in self.MONTHS:
            self.assertEqual(expected, month.getLowerCaseAbbreviation())

    def testCapitalizedCaseAbbreviation(self):
        for month, _, __, ___, ____, _____, expected in self.MONTHS:
            self.assertEqual(expected, month.getCapitalizedAbbreviation())

    def testParsing(self):
        for text in ("   AUGUST ", " august  ", "August", "\tAUG",
                     "august", "Aug", "aUgUsT  ", " 8 ", "00008"):
            self.assertEqual(Month.AUGUST, Month.parseMonth(text))

    def testParsingErrorEmpty(self):
        with self.assertRaises(JavaError):
            Month.parseMonth("  ")

    def testParsingErrorTooLow(self):
        with self.assertRaises(JavaError):
            Month.parseMonth("0")

    def testParsingErrorTooHigh(self):
        with self.assertRaises(JavaError):
            Month.parseMonth("13")

    def testParsingErrorCorruptedString(self):
        with self.assertRaises(JavaError):
            Month.parseMonth("AUGUSTE")


if __name__ == '__main__':
    unittest.main()
