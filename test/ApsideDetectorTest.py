# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's ApsideDetectorTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.frames import FramesFactory
from org.orekit.orbits import CartesianOrbit, KeplerianOrbit, OrbitType
from org.orekit.propagation.analytical import EcksteinHechlerPropagator
from org.orekit.propagation.events import AbstractDetector, ApsideDetector, EventsLogger
from org.orekit.propagation.events.handlers import ContinueOnEvent
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants, PVCoordinates


class ApsideDetectorTest(unittest.TestCase):

    def setUp(self):
        utc = TimeScalesFactory.getUTC()
        position = Vector3D(-6142438.668, 3492467.56, -25767.257)
        velocity = Vector3D(506.0, 943.0, 7450.0)
        date = AbsoluteDate(2003, 9, 16, utc)
        orbit = CartesianOrbit(PVCoordinates(position, velocity),
                               FramesFactory.getEME2000(), date,
                               Constants.EIGEN5C_EARTH_MU)
        self.propagator = EcksteinHechlerPropagator(
            orbit,
            Constants.EIGEN5C_EARTH_EQUATORIAL_RADIUS,
            Constants.EIGEN5C_EARTH_MU,
            Constants.EIGEN5C_EARTH_C20,
            Constants.EIGEN5C_EARTH_C30,
            Constants.EIGEN5C_EARTH_C40,
            Constants.EIGEN5C_EARTH_C50,
            Constants.EIGEN5C_EARTH_C60)

    def test_simple(self):
        detector = ApsideDetector.cast_(
            ApsideDetector(self.propagator.getInitialState().getOrbit())
            .withMaxCheck(600.0)
            .withThreshold(1.0e-12)
            .withHandler(ContinueOnEvent())
        )

        settings = detector.getDetectionSettings()
        self.assertAlmostEqual(
            600.0, settings.getMaxCheckInterval().currentInterval(None, True),
            delta=1.0e-15)
        self.assertAlmostEqual(1.0e-12, settings.getThreshold(), delta=1.0e-15)
        self.assertEqual(AbstractDetector.DEFAULT_MAX_ITER,
                         settings.getMaxIterationCount())

        logger = EventsLogger()
        self.propagator.addEventDetector(logger.monitorDetector(detector))
        self.propagator.propagate(
            self.propagator.getInitialState().getOrbit().getDate()
            .shiftedBy(Constants.JULIAN_DAY))

        events = logger.getLoggedEvents()
        self.assertEqual(30, events.size())
        for i in range(events.size()):
            event = events.get(i)
            orbit = OrbitType.KEPLERIAN.convertType(event.getState().getOrbit())
            kep = KeplerianOrbit(orbit)
            expected = 0.0 if event.isIncreasing() else math.pi
            diff = kep.getMeanAnomaly() - expected
            while diff > math.pi:
                diff -= 2.0 * math.pi
            while diff < -math.pi:
                diff += 2.0 * math.pi
            self.assertAlmostEqual(0.0, diff, delta=4.0e-14)


if __name__ == '__main__':
    unittest.main()
