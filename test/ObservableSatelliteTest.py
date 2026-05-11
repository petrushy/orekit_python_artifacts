# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java ObservableSatelliteTest."""

import unittest

import orekit
orekit.initVM()

from org.orekit.estimation.measurements import ObservableSatellite


class ObservableSatelliteTest(unittest.TestCase):

    def testIssue1039(self):
        self.assertEqual("sat-0", ObservableSatellite(0).getName())
        self.assertEqual("satellite", ObservableSatellite(0, "satellite").getName())


if __name__ == '__main__':
    unittest.main()
