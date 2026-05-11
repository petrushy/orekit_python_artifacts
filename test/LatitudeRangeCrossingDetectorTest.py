# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's LatitudeRangeCrossingDetectorTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import OneAxisEllipsoid
from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit
from org.orekit.propagation.analytical import EcksteinHechlerPropagator
from org.orekit.propagation.events import AbstractDetector, EventsLogger
from org.orekit.propagation.events import LatitudeRangeCrossingDetector
from org.orekit.propagation.events.handlers import ContinueOnEvent
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants, IERSConventions, PVCoordinates


def _earth():
    return OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                            Constants.WGS84_EARTH_FLATTENING,
                            FramesFactory.getITRF(IERSConventions.IERS_2010, True))


def _propagator(date):
    position = Vector3D(-6142438.668, 3492467.56, -25767.257)
    velocity = Vector3D(505.848, 942.781, 7435.922)
    orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                             FramesFactory.getEME2000(), date,
                             Constants.EIGEN5C_EARTH_MU)
    return EcksteinHechlerPropagator(
        orbit,
        Constants.EIGEN5C_EARTH_EQUATORIAL_RADIUS,
        Constants.EIGEN5C_EARTH_MU,
        Constants.EIGEN5C_EARTH_C20,
        Constants.EIGEN5C_EARTH_C30,
        Constants.EIGEN5C_EARTH_C40,
        Constants.EIGEN5C_EARTH_C50,
        Constants.EIGEN5C_EARTH_C60)


class LatitudeRangeCrossingDetectorTest(unittest.TestCase):

    def _assert_settings(self, detector, max_check, threshold):
        settings = detector.getDetectionSettings()
        self.assertAlmostEqual(max_check,
                               settings.getMaxCheckInterval().currentInterval(None, True),
                               delta=1.0e-15)
        self.assertAlmostEqual(threshold, settings.getThreshold(), delta=1.0e-15)
        self.assertEqual(AbstractDetector.DEFAULT_MAX_ITER,
                         settings.getMaxIterationCount())

    def test_regular_crossing(self):
        earth = _earth()
        detector = LatitudeRangeCrossingDetector.cast_(
            LatitudeRangeCrossingDetector(60.0, 1.0e-6, earth,
                                          math.radians(50.0), math.radians(60.0))
            .withHandler(ContinueOnEvent())
        )

        self._assert_settings(detector, 60.0, 1.0e-6)
        self.assertAlmostEqual(50.0, math.degrees(detector.getFromLatitude()),
                               delta=1.0e-14)
        self.assertAlmostEqual(60.0, math.degrees(detector.getToLatitude()),
                               delta=1.0e-14)

        date = AbsoluteDate(2003, 9, 16, TimeScalesFactory.getUTC())
        propagator = _propagator(date)
        logger = EventsLogger()
        propagator.addEventDetector(logger.monitorDetector(detector))
        propagator.propagate(date.shiftedBy(Constants.JULIAN_DAY))

        events = logger.getLoggedEvents()
        for i in range(events.size()):
            event = events.get(i)
            state = event.getState()
            latitude = earth.transform(
                state.getPVCoordinates(earth.getBodyFrame()).getPosition(),
                earth.getBodyFrame(), None).getLatitude()
            if event.isIncreasing():
                expected = 60.0 if state.getVelocity().getZ() < 0.0 else 50.0
            else:
                expected = 50.0 if state.getVelocity().getZ() < 0.0 else 60.0
            self.assertAlmostEqual(expected, math.degrees(latitude), delta=1.0e-4)

        self.assertEqual(60, events.size())

    def test_no_crossing(self):
        earth = _earth()
        detector = LatitudeRangeCrossingDetector.cast_(
            LatitudeRangeCrossingDetector(10.0, 1.0e-6, earth,
                                          math.radians(82.0), math.radians(87.0))
            .withHandler(ContinueOnEvent())
        )

        self._assert_settings(detector, 10.0, 1.0e-6)
        self.assertAlmostEqual(82.0, math.degrees(detector.getFromLatitude()),
                               delta=1.0e-14)
        self.assertAlmostEqual(87.0, math.degrees(detector.getToLatitude()),
                               delta=1.0e-14)

        date = AbsoluteDate(2003, 9, 16, TimeScalesFactory.getUTC())
        propagator = _propagator(date)
        logger = EventsLogger()
        propagator.addEventDetector(logger.monitorDetector(detector))
        propagator.propagate(date.shiftedBy(Constants.JULIAN_DAY))
        self.assertEqual(0, logger.getLoggedEvents().size())


if __name__ == '__main__':
    unittest.main()
