# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java CartesianDerivativesFilterTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.utils import CartesianDerivativesFilter


class CartesianDerivativesFilterTest(unittest.TestCase):

    def testList(self):
        self.assertEqual(3, len(list(CartesianDerivativesFilter.values())))

    def testOrder(self):
        self.assertEqual(0, CartesianDerivativesFilter.USE_P.getMaxOrder())
        self.assertEqual(1, CartesianDerivativesFilter.USE_PV.getMaxOrder())
        self.assertEqual(2, CartesianDerivativesFilter.USE_PVA.getMaxOrder())

    def testBuildFromOrder(self):
        self.assertEqual(CartesianDerivativesFilter.USE_P, CartesianDerivativesFilter.getFilter(0))
        self.assertEqual(CartesianDerivativesFilter.USE_PV, CartesianDerivativesFilter.getFilter(1))
        self.assertEqual(CartesianDerivativesFilter.USE_PVA, CartesianDerivativesFilter.getFilter(2))

    def testNoNegativeOrder(self):
        with self.assertRaises(JavaError):
            CartesianDerivativesFilter.getFilter(-1)

    def testNoOrder3(self):
        with self.assertRaises(JavaError):
            CartesianDerivativesFilter.getFilter(3)


if __name__ == '__main__':
    unittest.main()
