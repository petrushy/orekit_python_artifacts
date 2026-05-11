# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java AngularDerivativesFilterTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.utils import AngularDerivativesFilter


class AngularDerivativesFilterTest(unittest.TestCase):

    def testList(self):
        self.assertEqual(3, len(list(AngularDerivativesFilter.values())))

    def testOrder(self):
        self.assertEqual(0, AngularDerivativesFilter.USE_R.getMaxOrder())
        self.assertEqual(1, AngularDerivativesFilter.USE_RR.getMaxOrder())
        self.assertEqual(2, AngularDerivativesFilter.USE_RRA.getMaxOrder())

    def testBuildFromOrder(self):
        self.assertEqual(AngularDerivativesFilter.USE_R, AngularDerivativesFilter.getFilter(0))
        self.assertEqual(AngularDerivativesFilter.USE_RR, AngularDerivativesFilter.getFilter(1))
        self.assertEqual(AngularDerivativesFilter.USE_RRA, AngularDerivativesFilter.getFilter(2))

    def testNoNegativeOrder(self):
        with self.assertRaises(JavaError):
            AngularDerivativesFilter.getFilter(-1)

    def testNoOrder3(self):
        with self.assertRaises(JavaError):
            AngularDerivativesFilter.getFilter(3)


if __name__ == '__main__':
    unittest.main()
