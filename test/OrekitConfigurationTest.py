# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java OrekitConfigurationTest."""

import re
import unittest

import orekit
orekit.initVM()

from org.hipparchus.util import MathUtils
from org.orekit.utils import OrekitConfiguration


class OrekitConfigurationTest(unittest.TestCase):

    def testGetSetCacheSlotsNumber(self):
        defaultSlots = OrekitConfiguration.getCacheSlotsNumber()
        self.assertNotEqual(0, defaultSlots)

        setSlots = 105
        OrekitConfiguration.setCacheSlotsNumber(setSlots)
        self.assertEqual(setSlots, OrekitConfiguration.getCacheSlotsNumber())

    def testVersions(self):
        pattern = re.compile(r"unknown|[0-9.]*(?:-SNAPSHOT)?")
        self.assertRegex(MathUtils.getHipparchusVersion(), pattern)
        self.assertRegex(OrekitConfiguration.getOrekitVersion(), pattern)


if __name__ == '__main__':
    unittest.main()
