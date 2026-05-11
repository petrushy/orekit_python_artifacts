# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java AveragedKeplerianWithMeanAngleTest."""

import unittest

import orekit
orekit.initVM()

from org.orekit.propagation.conversion.averaging.elements import AveragedKeplerianWithMeanAngle


class AveragedKeplerianWithMeanAngleTest(unittest.TestCase):

    def testToArray(self):
        elements = AveragedKeplerianWithMeanAngle(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        elementsAsArray = elements.toArray()

        self.assertEqual(elements.getAveragedSemiMajorAxis(), elementsAsArray[0])
        self.assertEqual(elements.getAveragedEccentricity(), elementsAsArray[1])
        self.assertEqual(elements.getAveragedInclination(), elementsAsArray[2])
        self.assertEqual(elements.getAveragedPerigeeArgument(), elementsAsArray[3])
        self.assertEqual(elements.getAveragedRightAscensionOfTheAscendingNode(), elementsAsArray[4])
        self.assertEqual(elements.getAveragedMeanAnomaly(), elementsAsArray[5])


if __name__ == '__main__':
    unittest.main()
