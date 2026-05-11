# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java ParameterDriverTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.errors import OrekitIllegalStateException, OrekitMessages
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import ParameterDriver


class ParameterDriverTest(unittest.TestCase):

    def assertNamesSpanMap(self, driver):
        nb = 0
        span = driver.getNamesSpanMap().getFirstSpan()
        while span is not None:
            self.assertEqual("Span" + driver.getName() + str(nb), span.getData())
            nb += 1
            span = span.next()

    def testPDriverConstruction(self):
        p1 = ParameterDriver("p1", 0.0, 1.0, -10.0, 10.0)
        date = AbsoluteDate(2010, 11, 2, 3, 0, 0.0, TimeScalesFactory.getUTC())

        p1.addSpanAtDate(date)
        p1.setValue(3.0, date.shiftedBy(10.0))
        self.assertAlmostEqual(3.0, p1.getValue(date.shiftedBy(10.0)), delta=1.0e-10)
        self.assertAlmostEqual(0.0, p1.getValue(date.shiftedBy(-10.0)), delta=1.0e-10)
        self.assertEqual("Span" + p1.getName() + "0", p1.getNameSpan(date.shiftedBy(-10.0)))
        self.assertEqual("Span" + p1.getName() + "1", p1.getNameSpan(date.shiftedBy(10.0)))

        two_days = 2.0 * 24.0 * 3600.0
        p1.addSpanAtDate(date.shiftedBy(two_days))
        p1.setValue(6.0, date.shiftedBy(two_days))
        self.assertAlmostEqual(6.0, p1.getValue(date.shiftedBy(two_days + 10.0)),
                               delta=1.0e-10)
        self.assertNamesSpanMap(p1)

        p1.setName("p1_new")
        self.assertNamesSpanMap(p1)

    def testExceptionSetPeriod(self):
        p1 = ParameterDriver("p1", 0.0, 1.0, -1.0, 1.0)
        date = AbsoluteDate(2010, 11, 2, 3, 0, 0.0, TimeScalesFactory.getUTC())
        p1.addSpans(date, date.shiftedBy(15.0 * 3600.0), 3.0 * 3600.0)
        self.assertNamesSpanMap(p1)

        with self.assertRaises(JavaError) as ctx:
            p1.addSpans(date, date.shiftedBy(15.0 * 3600.0), 5.0 * 3600.0)
        oe = OrekitIllegalStateException.cast_(ctx.exception.getJavaException())
        self.assertEqual(OrekitMessages.PARAMETER_PERIODS_HAS_ALREADY_BEEN_SET,
                         oe.getSpecifier())
        self.assertEqual(p1.getName(), str(oe.getParts()[0]))

    def testExceptionGetValue(self):
        p1 = ParameterDriver("p1", 0.0, 1.0, -1.0, 1.0)
        date = AbsoluteDate(2010, 11, 2, 3, 0, 0.0, TimeScalesFactory.getUTC())
        p1.addSpans(date, date.shiftedBy(15.0 * 3600.0), 3.0 * 3600.0)

        with self.assertRaises(JavaError) as ctx:
            p1.getNormalizedValue()
        oe = OrekitIllegalStateException.cast_(ctx.exception.getJavaException())
        self.assertEqual(OrekitMessages.PARAMETER_WITH_SEVERAL_ESTIMATED_VALUES,
                         oe.getSpecifier())
        self.assertEqual(p1.getName(), str(oe.getParts()[0]))
        self.assertEqual("getValue(date)", str(oe.getParts()[1]))

    def testExceptionSetValue(self):
        p1 = ParameterDriver("p1", 0.0, 1.0, -1.0, 1.0)
        date = AbsoluteDate(2010, 11, 2, 3, 0, 0.0, TimeScalesFactory.getUTC())
        p1.addSpans(date, date.shiftedBy(15.0 * 3600.0), 3.0 * 3600.0)
        p1.setValue(30.0, date.shiftedBy(-100.0))
        self.assertEqual(1.0, p1.getValue(date.shiftedBy(-500.0)))
        p1.setValue(0.8, date.shiftedBy(-100.0))
        self.assertEqual(0.8, p1.getValue(date.shiftedBy(-500.0)))

        with self.assertRaises(JavaError) as ctx:
            p1.setNormalizedValue(2.0)
        oe = OrekitIllegalStateException.cast_(ctx.exception.getJavaException())
        self.assertEqual(OrekitMessages.PARAMETER_WITH_SEVERAL_ESTIMATED_VALUES,
                         oe.getSpecifier())
        self.assertEqual(p1.getName(), str(oe.getParts()[0]))
        self.assertEqual("setValue(date)", str(oe.getParts()[1]))


if __name__ == '__main__':
    unittest.main()
