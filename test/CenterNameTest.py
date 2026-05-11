# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java CenterNameTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.bodies import CelestialBodyFactory
from org.orekit.files.ccsds.definitions import (CelestialBodyFrame, CenterName,
                                                ModifiedFrame)
from org.orekit.frames import Frame, FramesFactory, L2Frame


class CenterNameTest(unittest.TestCase):

    def testSupportedCenters(self):
        for name in ("SOLAR_SYSTEM_BARYCENTER", "SUN", "MERCURY", "VENUS",
                     "EARTH_MOON", "EARTH", "MOON", "MARS", "JUPITER",
                     "SATURN", "URANUS", "NEPTUNE", "PLUTO"):
            self.assertIsNotNone(CenterName.valueOf(name).getCelestialBody())

    def testUnsupportedCenters(self):
        for name in ("CERES", "SEDNA", "ERIS", "PLANET-9"):
            with self.assertRaises(JavaError):
                CenterName.valueOf(name)

    def testGuess(self):
        self.assertEqual("SATURN",
                         CenterName.guessCenter(
                             CelestialBodyFactory.getSaturn().getBodyOrientedFrame()))
        self.assertEqual("MERCURY",
                         CenterName.guessCenter(
                             CelestialBodyFactory.getMercury().getInertiallyOrientedFrame()))
        self.assertEqual("PLANET-X",
                         CenterName.guessCenter(
                             ModifiedFrame(FramesFactory.getEME2000(),
                                           CelestialBodyFrame.EME2000,
                                           CelestialBodyFactory.getMars(),
                                           "PLANET-X")))
        self.assertEqual("SOLAR SYSTEM BARYCENTER",
                         CenterName.guessCenter(FramesFactory.getICRF()))
        self.assertEqual("EARTH", CenterName.guessCenter(Frame.getRoot()))
        self.assertEqual("EARTH", CenterName.guessCenter(FramesFactory.getTOD(True)))
        self.assertEqual("UNKNOWN",
                         CenterName.guessCenter(
                             L2Frame(CelestialBodyFactory.getSun(),
                                     CelestialBodyFactory.getEarth())))

    def testMap(self):
        self.assertEqual(CenterName.SATURN,
                         CenterName.map(
                             CelestialBodyFactory.getSaturn().getBodyOrientedFrame()))
        self.assertIsNone(CenterName.map(
            L2Frame(CelestialBodyFactory.getSun(), CelestialBodyFactory.getEarth())))


if __name__ == '__main__':
    unittest.main()
