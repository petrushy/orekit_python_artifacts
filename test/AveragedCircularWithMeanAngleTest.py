# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java AveragedCircularWithMeanAngleTest."""

import unittest

import orekit
orekit.initVM()

from org.orekit.propagation.conversion.averaging.elements import AveragedCircularWithMeanAngle


class AveragedCircularWithMeanAngleTest(unittest.TestCase):

    def testToArray(self):
        elements = AveragedCircularWithMeanAngle(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        elementsAsArray = elements.toArray()

        self.assertEqual(elements.getAveragedSemiMajorAxis(), elementsAsArray[0])
        self.assertEqual(elements.getAveragedCircularEx(), elementsAsArray[1])
        self.assertEqual(elements.getAveragedCircularEy(), elementsAsArray[2])
        self.assertEqual(elements.getAveragedInclination(), elementsAsArray[3])
        self.assertEqual(elements.getAveragedRightAscensionOfTheAscendingNode(), elementsAsArray[4])
        self.assertEqual(elements.getAveragedMeanLatitudeArgument(), elementsAsArray[5])


if __name__ == '__main__':
    unittest.main()
