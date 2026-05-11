# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's LongitudeExtremumDetectorTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import OneAxisEllipsoid
from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit, KeplerianOrbit, PositionAngleType
from org.orekit.propagation.analytical import EcksteinHechlerPropagator, KeplerianPropagator
from org.orekit.propagation.events import AbstractDetector, EventsLogger
from org.orekit.propagation.events import LongitudeExtremumDetector
from org.orekit.propagation.events.handlers import ContinueOnEvent
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants, IERSConventions, PVCoordinates


def _earth():
    return OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                            Constants.WGS84_EARTH_FLATTENING,
                            FramesFactory.getITRF(IERSConventions.IERS_2010, True))


def _eckstein_hechler(date):
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


class LongitudeExtremumDetectorTest(unittest.TestCase):

    def test_no_crossing(self):
        earth = _earth()
        detector = LongitudeExtremumDetector.cast_(
            LongitudeExtremumDetector(earth)
            .withMaxCheck(60.0)
            .withThreshold(1.0e-6)
            .withHandler(ContinueOnEvent())
        )

        settings = detector.getDetectionSettings()
        self.assertAlmostEqual(
            60.0, settings.getMaxCheckInterval().currentInterval(None, True),
            delta=1.0e-15)
        self.assertAlmostEqual(1.0e-6, settings.getThreshold(), delta=1.0e-15)
        self.assertEqual(AbstractDetector.DEFAULT_MAX_ITER,
                         settings.getMaxIterationCount())
        self.assertEqual(earth, detector.getBody())

        date = AbsoluteDate(2003, 9, 16, TimeScalesFactory.getUTC())
        propagator = _eckstein_hechler(date)
        logger = EventsLogger()
        propagator.addEventDetector(logger.monitorDetector(detector))
        propagator.propagate(date.shiftedBy(Constants.JULIAN_DAY))
        self.assertEqual(0, logger.getLoggedEvents().size())

    def test_zig_zag(self):
        earth = _earth()
        detector = LongitudeExtremumDetector.cast_(
            LongitudeExtremumDetector(600.0, 1.0e-6, earth)
            .withHandler(ContinueOnEvent())
        )

        settings = detector.getDetectionSettings()
        self.assertAlmostEqual(
            600.0, settings.getMaxCheckInterval().currentInterval(None, True),
            delta=1.0e-15)
        self.assertAlmostEqual(1.0e-6, settings.getThreshold(), delta=1.0e-15)
        self.assertEqual(AbstractDetector.DEFAULT_MAX_ITER,
                         settings.getMaxIterationCount())

        orbit = KeplerianOrbit(24464560.0, 0.7311, 0.122138, 3.10686, 1.00681,
                               0.048363, PositionAngleType.MEAN,
                               FramesFactory.getEME2000(),
                               AbsoluteDate.J2000_EPOCH,
                               Constants.EIGEN5C_EARTH_MU)

        propagator = KeplerianPropagator(orbit)
        logger = EventsLogger()
        propagator.addEventDetector(logger.monitorDetector(detector))
        propagator.propagate(orbit.getDate().shiftedBy(Constants.JULIAN_DAY))

        expected_longitudes = [74.8511595865, 39.5103244928, -84.2572907247,
                               -119.598124966, 116.6342589464]
        expected_latitudes = [-3.840425646067, 3.423723606556, -3.84041982822,
                              3.423721448341, -3.84041336057]

        events = logger.getLoggedEvents()
        self.assertEqual(5, events.size())
        for i in range(5):
            state = events.get(i).getState()
            gp = earth.transform(state.getPosition(earth.getBodyFrame()),
                                 earth.getBodyFrame(), None)
            self.assertAlmostEqual(expected_longitudes[i],
                                   math.degrees(gp.getLongitude()), delta=1.0e-2)
            self.assertAlmostEqual(expected_latitudes[i],
                                   math.degrees(gp.getLatitude()), delta=1.0e-2)


if __name__ == '__main__':
    unittest.main()
