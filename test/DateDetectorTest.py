# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's DateDetectorTest."""

import unittest
from datetime import datetime, timezone

import orekit
orekit.initVM()

from orekit import JArray, JArray_double, JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.events import Action
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit, OrbitType
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.analytical.tle import TLE, TLEPropagator
from org.orekit.propagation.events import DateDetector, NodeDetector
from org.orekit.propagation.events.handlers import PythonEventHandler, StopOnEvent
from org.orekit.propagation.integration import (CombinedDerivatives,
                                                PythonAdditionalDerivativesProvider)
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import PVCoordinates


def _absolute_date_from_timestamp_ms(ts_ms):
    """Mirror jpype's helper that converts a JS-style epoch-ms to AbsoluteDate."""
    utc_dt = datetime.fromtimestamp(ts_ms / 1000.0, tz=timezone.utc)
    second = float(utc_dt.second)
    millis = utc_dt.microsecond / 1.0e6
    return AbsoluteDate(utc_dt.year, utc_dt.month, utc_dt.day,
                        utc_dt.hour, utc_dt.minute, second,
                        TimeScalesFactory.getUTC()).shiftedBy(millis)


class _DummyDerivativesProvider(PythonAdditionalDerivativesProvider):
    """Minimal AdditionalDerivativesProvider; mirrors the inner class in the
    jpype test that contributes a single zero-derivative to the integrator."""

    def __init__(self):
        super().__init__()

    def getName(self):
        return "dummy"

    def getDimension(self):
        return 1

    def init(self, s0, target):
        pass

    def yields(self, s):
        return False

    def combinedDerivatives(self, s):
        return CombinedDerivatives(JArray_double([0.0]), None)


class _NodeHandler(PythonEventHandler):
    """Records the node date and schedules the next DateDetector firing."""

    def __init__(self, outer_test):
        super().__init__()
        self.outer = outer_test

    def init(self, s0, target, detector):
        pass

    def eventOccurred(self, s, nd, increasing):
        if increasing:
            self.outer.node_date = s.getDate()
            self.outer.date_detector.addEventDate(self.outer.node_date.shiftedBy(self.outer.dt))
        return Action.CONTINUE

    def resetState(self, detector, oldState):
        return oldState

    def finish(self, finalState, detector):
        pass

    def getHandler(self):
        pass


class _AutoHandler(PythonEventHandler):
    """Repeatedly schedules a date in the past, counting events."""

    def __init__(self, outer_test):
        super().__init__()
        self.outer = outer_test

    def init(self, s0, target, detector):
        pass

    def eventOccurred(self, s, dd, increasing):
        next_date = s.getDate().shiftedBy(-self.outer.dt)
        # JCC passes the detector as EventDetector (base); cast back.
        DateDetector.cast_(dd).addEventDate(next_date)
        self.outer.evtno += 1
        return Action.CONTINUE

    def resetState(self, detector, oldState):
        return oldState

    def finish(self, finalState, detector):
        pass

    def getHandler(self):
        pass


class _ExceptionHandler(PythonEventHandler):
    """Schedules dates that violate the configured min gap to force an exception."""

    def __init__(self, outer_test):
        super().__init__()
        self.outer = outer_test

    def init(self, s0, target, detector):
        pass

    def eventOccurred(self, s, dd, increasing):
        step = (2.0 * self.outer.max_check) if (self.outer.evtno % 2 == 0) \
            else (self.outer.max_check / 2.0)
        next_date = s.getDate().shiftedBy(step)
        DateDetector.cast_(dd).addEventDate(next_date)
        self.outer.evtno += 1
        return Action.CONTINUE

    def resetState(self, detector, oldState):
        return oldState

    def finish(self, finalState, detector):
        pass

    def getHandler(self):
        pass


class _GenericStopHandler(PythonEventHandler):
    """Stops on every event."""

    def __init__(self):
        super().__init__()

    def init(self, s0, target, detector):
        pass

    def eventOccurred(self, s, detector, increasing):
        return Action.STOP

    def resetState(self, detector, oldState):
        raise RuntimeError("Should not be called")

    def finish(self, finalState, detector):
        pass

    def getHandler(self):
        pass


class DateDetectorTest(unittest.TestCase):

    def setUp(self):
        mu = 3.9860047e14
        position = Vector3D(-6142438.668, 3492467.560, -25767.25680)
        velocity = Vector3D(505.8479685, 942.7809215, 7435.922231)
        self.ini_date = AbsoluteDate(1969, 7, 28, 4, 0, 0.0, TimeScalesFactory.getTT())
        self.ini_orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                          FramesFactory.getEME2000(),
                                          self.ini_date, mu)
        initial_state = SpacecraftState(self.ini_orbit)
        abs_tolerance = JArray_double([0.001, 1.0e-9, 1.0e-9, 1.0e-6, 1.0e-6, 1.0e-6, 0.001])
        rel_tolerance = JArray_double([1.0e-7, 1.0e-4, 1.0e-4, 1.0e-7, 1.0e-7, 1.0e-7, 1.0e-7])
        integrator = DormandPrince853Integrator(0.001, 1000.0, abs_tolerance, rel_tolerance)
        integrator.setInitialStepSize(60.0)
        self.propagator = NumericalPropagator(integrator)
        self.propagator.setInitialState(initial_state)
        self.dt = 60.0
        self.max_check = 10.0
        self.threshold = 10.0e-10
        self.evtno = 0
        self.node_date = None
        self.date_detector = None

    def testIssue1676(self):
        expected_min_gap = 0.001
        self.assertAlmostEqual(expected_min_gap,
                               DateDetector(expected_min_gap, self.ini_date).getMinGap(),
                               delta=1.0e-10)

    def testSimpleTimer(self):
        # JCC's fluent-builder methods return AbstractDetector, losing the
        # DateDetector subtype; cast back to access getDate() / addEventDate.
        date_detector = DateDetector.cast_(
            DateDetector(self.ini_date.shiftedBy(2.0 * self.dt))
                .withMaxCheck(self.max_check)
                .withThreshold(self.threshold))
        self.assertAlmostEqual(2 * self.dt,
                               date_detector.getDate().durationFrom(self.ini_date),
                               delta=1.0e-10)

        self.propagator.addAdditionalDerivativesProvider(_DummyDerivativesProvider())
        self.propagator.setInitialState(
            self.propagator.getInitialState()
                .addAdditionalData("dummy", JArray_double([0.0])))
        self.propagator.setOrbitType(OrbitType.EQUINOCTIAL)
        self.propagator.addEventDetector(date_detector)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(100.0 * self.dt))
        self.assertAlmostEqual(2.0 * self.dt,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=self.threshold)

    def testDefaultDetectionSettings(self):
        # JCC needs an explicit empty TimeStamped[] for the no-arg-style ctor;
        # the varargs path used by jpype's `DateDetector()` is not auto-empty.
        detector = DateDetector(JArray('object')(0))
        self.assertEqual(DateDetector.DEFAULT_MAX_ITER,
                         detector.getDetectionSettings().getMaxIterationCount())
        self.assertAlmostEqual(DateDetector.DEFAULT_THRESHOLD,
                               detector.getDetectionSettings().getThreshold(),
                               delta=0.0)

    def testEmbeddedTimer(self):
        self.date_detector = DateDetector(JArray('object')(0))
        self.assertIsNone(self.date_detector.getDate())

        node_detector = (NodeDetector(self.ini_orbit, self.ini_orbit.getFrame())
                         .withHandler(_NodeHandler(self)))
        self.propagator.addEventDetector(node_detector)
        self.propagator.addEventDetector(self.date_detector)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(100.0 * self.dt))
        self.assertAlmostEqual(self.dt,
                               final_state.getDate().durationFrom(self.node_date),
                               delta=self.threshold)

    def testAutoEmbeddedTimer(self):
        self.date_detector = DateDetector.cast_(
            DateDetector(self.ini_date.shiftedBy(-self.dt))
                .withMaxCheck(self.max_check)
                .withThreshold(self.threshold)
                .withHandler(_AutoHandler(self)))
        self.propagator.addEventDetector(self.date_detector)
        self.propagator.propagate(self.ini_date.shiftedBy(-100.0 * self.dt))
        self.assertEqual(100, self.evtno)

    def testExceptionTimer(self):
        with self.assertRaises(JavaError):
            self.date_detector = DateDetector.cast_(
                DateDetector(self.ini_date.shiftedBy(self.dt))
                    .withMaxCheck(self.max_check)
                    .withMinGap(self.max_check)
                    .withThreshold(self.threshold)
                    .withHandler(_ExceptionHandler(self)))
            self.propagator.addEventDetector(self.date_detector)
            self.propagator.propagate(self.ini_date.shiftedBy(100.0 * self.dt))

    def testGenericHandler(self):
        self.date_detector = (DateDetector(self.ini_date.shiftedBy(self.dt))
                              .withMaxCheck(self.max_check)
                              .withThreshold(self.threshold)
                              .withHandler(_GenericStopHandler()))
        self.propagator.addEventDetector(self.date_detector)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(100 * self.dt))
        self.assertAlmostEqual(self.dt,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=self.threshold)

    def testIssue935(self):
        start = 1570802400000
        end = 1570838399000

        tle = TLE("1 43197U 18015F   19284.07336221  .00000533  00000-0  24811-4 0  9998",
                  "2 43197  97.4059  50.1428 0017543 265.5429 181.0400 15.24136761 93779")
        propagator = TLEPropagator.selectExtrapolator(tle)

        max_check = int((end - start) / 2000)
        date_detector = DateDetector.cast_(
            DateDetector(_absolute_date_from_timestamp_ms(start))
                .withMaxCheck(float(max_check))
                .withThreshold(1.0e-6)
                .withHandler(StopOnEvent()))
        date_detector.addEventDate(_absolute_date_from_timestamp_ms(end))
        propagator.addEventDetector(date_detector)

        start_date = _absolute_date_from_timestamp_ms(start)
        end_date = _absolute_date_from_timestamp_ms(end)
        last_state = propagator.propagate(start_date, end_date.shiftedBy(1.0))
        self.assertAlmostEqual(0.0, last_state.getDate().durationFrom(end_date),
                               delta=1.0e-15)

    def testDependsOnlyOnTime(self):
        # JCC needs an explicit empty TimeStamped[] for the no-arg-style ctor;
        # the varargs path used by jpype's `DateDetector()` is not auto-empty.
        detector = DateDetector(JArray('object')(0))
        self.assertTrue(detector.dependsOnTimeOnly())


if __name__ == '__main__':
    unittest.main()
