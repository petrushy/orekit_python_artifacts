# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's TimeIntervalDetectorTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.events import Action
from org.orekit.frames import FramesFactory
from org.orekit.orbits import CartesianOrbit
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.events import TimeIntervalDetector
from org.orekit.propagation.events.handlers import PythonEventHandler
from org.orekit.time import AbsoluteDate, TimeInterval
from org.orekit.utils import PVCoordinates


def make_state(date):
    pv = PVCoordinates(Vector3D(7000000.0, 0.0, 0.0),
                       Vector3D(0.0, 7500.0, 0.0))
    orbit = CartesianOrbit(pv, FramesFactory.getGCRF(), date, 3.9860047e14)
    return SpacecraftState(orbit)


class MockHandler(PythonEventHandler):

    def __init__(self):
        super().__init__()

    def eventOccurred(self, s, detector, increasing):
        return Action.CONTINUE

    def init(self, s0, target, detector):
        pass

    def finish(self, final_state, detector):
        pass

    def resetState(self, detector, old_state):
        return old_state

    def getHandler(self):
        pass


class TimeIntervalDetectorTest(unittest.TestCase):

    def test_getter(self):
        start_date = AbsoluteDate.ARBITRARY_EPOCH
        interval = TimeInterval.of(start_date, start_date.shiftedBy(1.0))
        detector = TimeIntervalDetector(MockHandler(), interval)
        self.assertEqual(interval, detector.getTimeInterval())

    def test_depends_only_on_time(self):
        start_date = AbsoluteDate.ARBITRARY_EPOCH
        interval = TimeInterval.of(start_date, start_date.shiftedBy(1.0))
        detector = TimeIntervalDetector(MockHandler(), interval)
        self.assertTrue(detector.dependsOnTimeOnly())

    def test_g_value(self):
        start_date = AbsoluteDate.ARBITRARY_EPOCH
        interval = TimeInterval.of(start_date, start_date.shiftedBy(1.0))
        detector = TimeIntervalDetector(MockHandler(), interval)
        self.assertAlmostEqual(0.0, detector.g(make_state(interval.getStartDate())),
                               delta=1.0e-15)
        self.assertAlmostEqual(0.0, detector.g(make_state(interval.getEndDate())),
                               delta=1.0e-15)

    def test_g_sign(self):
        start_date = AbsoluteDate.ARBITRARY_EPOCH
        dt = 1.0
        interval = TimeInterval.of(start_date, start_date.shiftedBy(dt))
        detector = TimeIntervalDetector(MockHandler(), interval)
        self.assertLess(detector.g(make_state(interval.getStartDate().shiftedBy(-dt))),
                        0.0)
        self.assertGreater(detector.g(make_state(interval.getStartDate().shiftedBy(dt / 2.0))),
                           0.0)
        self.assertLess(detector.g(make_state(interval.getEndDate().shiftedBy(dt))),
                        0.0)


if __name__ == '__main__':
    unittest.main()
