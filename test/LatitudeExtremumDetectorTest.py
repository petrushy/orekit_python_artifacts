# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's LatitudeExtremumDetectorTest."""

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
from org.orekit.propagation.events import LatitudeExtremumDetector
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


class LatitudeExtremumDetectorTest(unittest.TestCase):

    def test_leo(self):
        earth = _earth()
        detector = LatitudeExtremumDetector.cast_(
            LatitudeExtremumDetector(earth)
            .withMaxCheck(60.0)
            .withThreshold(1.0e-6)
            .withHandler(ContinueOnEvent())
        )

        settings = detector.getDetectionSettings()
        self.assertAlmostEqual(60.0,
                               settings.getMaxCheckInterval().currentInterval(None, True),
                               delta=1.0e-15)
        self.assertAlmostEqual(1.0e-6, settings.getThreshold(), delta=1.0e-15)
        self.assertEqual(AbstractDetector.DEFAULT_MAX_ITER,
                         settings.getMaxIterationCount())
        self.assertEqual(earth, detector.getBody())

        date = AbsoluteDate(2003, 9, 16, TimeScalesFactory.getUTC())
        propagator = _propagator(date)
        logger = EventsLogger()
        propagator.addEventDetector(logger.monitorDetector(detector))
        propagator.propagate(date.shiftedBy(Constants.JULIAN_DAY))

        events = logger.getLoggedEvents()
        for i in range(events.size()):
            event = events.get(i)
            state = event.getState()
            latitude = earth.transform(state.getPosition(earth.getBodyFrame()),
                                       earth.getBodyFrame(), None).getLatitude()
            if event.isIncreasing():
                self.assertAlmostEqual(-81.863, math.degrees(latitude), delta=0.001)
            else:
                self.assertAlmostEqual(+81.863, math.degrees(latitude), delta=0.001)

        self.assertEqual(29, events.size())


if __name__ == '__main__':
    unittest.main()
