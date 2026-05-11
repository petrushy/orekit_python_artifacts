# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java BodyFacadeTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.data import DataContext
from org.orekit.files.ccsds.definitions import BodyFacade, CenterName


class BodyFacadeTest(unittest.TestCase):

    def testIssue898Earth(self):
        body = BodyFacade.create(CenterName.EARTH)
        self.assertEqual("EARTH", body.getName())
        self.assertEqual("Earth", body.getBody().getName())

    def testIssue898Sun(self):
        body = BodyFacade.create(CenterName.SUN)
        self.assertEqual("SUN", body.getName())
        self.assertEqual("Sun", body.getBody().getName())

    def testIssue1137(self):
        sun = BodyFacade.create(CenterName.SUN, DataContext.getDefault())
        self.assertEqual("SUN", sun.getName())
        self.assertEqual("Sun", sun.getBody().getName())

        earth = BodyFacade.create(CenterName.EARTH,
                                  DataContext.getDefault().getCelestialBodies())
        self.assertEqual("EARTH", earth.getName())
        self.assertEqual("Earth", earth.getBody().getName())


if __name__ == '__main__':
    unittest.main()
