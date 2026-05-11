# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java AveragedEquinoctialWithMeanAngleTest."""

import unittest

import orekit
orekit.initVM()

from org.orekit.propagation.conversion.averaging.elements import AveragedEquinoctialWithMeanAngle


class AveragedEquinoctialWithMeanAngleTest(unittest.TestCase):

    def testToArray(self):
        elements = AveragedEquinoctialWithMeanAngle(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        elementsAsArray = elements.toArray()

        self.assertEqual(elements.getAveragedSemiMajorAxis(), elementsAsArray[0])
        self.assertEqual(elements.getAveragedEquinoctialEx(), elementsAsArray[1])
        self.assertEqual(elements.getAveragedEquinoctialEy(), elementsAsArray[2])
        self.assertEqual(elements.getAveragedHx(), elementsAsArray[3])
        self.assertEqual(elements.getAveragedHy(), elementsAsArray[4])
        self.assertEqual(elements.getAveragedMeanLongitudeArgument(), elementsAsArray[5])


if __name__ == '__main__':
    unittest.main()
