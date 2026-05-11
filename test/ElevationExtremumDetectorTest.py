# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's ElevationExtremumDetectorTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import GeodeticPoint, OneAxisEllipsoid
from org.orekit.frames import FramesFactory, TopocentricFrame
from org.orekit.orbits import EquinoctialOrbit
from org.orekit.propagation.analytical import EcksteinHechlerPropagator
from org.orekit.propagation.events import ElevationExtremumDetector
from org.orekit.propagation.events import EventSlopeFilter, EventsLogger, FilterType
from org.orekit.propagation.events.handlers import ContinueOnEvent
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants, IERSConventions, PVCoordinates


class ElevationExtremumDetectorTest(unittest.TestCase):

    def test_leo(self):
        earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                 Constants.WGS84_EARTH_FLATTENING,
                                 FramesFactory.getITRF(IERSConventions.IERS_2010, True))

        gp = GeodeticPoint(math.radians(51.0), math.radians(66.6), 300.0)
        raw = ElevationExtremumDetector.cast_(
            ElevationExtremumDetector(TopocentricFrame(earth, gp, "test"))
            .withMaxCheck(60.0)
            .withThreshold(1.0e-6)
            .withHandler(ContinueOnEvent())
        )
        max_elevation_detector = EventSlopeFilter(
            raw, FilterType.TRIGGER_ONLY_DECREASING_EVENTS)

        settings = raw.getDetectionSettings()
        self.assertAlmostEqual(
            60.0, settings.getMaxCheckInterval().currentInterval(None, True),
            delta=1.0e-15)
        self.assertAlmostEqual(1.0e-6, settings.getThreshold(), delta=1.0e-15)
        self.assertEqual("test", raw.getTopocentricFrame().getName())

        utc = TimeScalesFactory.getUTC()
        position = Vector3D(-6142438.668, 3492467.56, -25767.257)
        velocity = Vector3D(505.848, 942.781, 7435.922)
        date = AbsoluteDate(2003, 9, 16, utc)
        orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                 FramesFactory.getEME2000(), date,
                                 Constants.EIGEN5C_EARTH_MU)

        propagator = EcksteinHechlerPropagator(
            orbit,
            Constants.EIGEN5C_EARTH_EQUATORIAL_RADIUS,
            Constants.EIGEN5C_EARTH_MU,
            Constants.EIGEN5C_EARTH_C20,
            Constants.EIGEN5C_EARTH_C30,
            Constants.EIGEN5C_EARTH_C40,
            Constants.EIGEN5C_EARTH_C50,
            Constants.EIGEN5C_EARTH_C60,
        )

        logger = EventsLogger()
        propagator.addEventDetector(logger.monitorDetector(max_elevation_detector))
        propagator.propagate(date.shiftedBy(Constants.JULIAN_DAY))

        visible_events = 0
        events = logger.getLoggedEvents()
        for i in range(events.size()):
            event = events.get(i)
            e_minus = raw.getElevation(event.getState().shiftedBy(-10.0))
            e0 = raw.getElevation(event.getState())
            e_plus = raw.getElevation(event.getState().shiftedBy(+10.0))
            if e0 > math.radians(5.0):
                visible_events += 1
            self.assertTrue(e0 > e_minus)
            self.assertTrue(e0 > e_plus)

        self.assertEqual(15, events.size())
        self.assertEqual(6, visible_events)


if __name__ == '__main__':
    unittest.main()
