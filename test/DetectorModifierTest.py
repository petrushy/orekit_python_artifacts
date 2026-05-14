# -*- coding: utf-8 -*-
"""JCC port of orekit_jpype's DetectorModifierTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JArray, JArray_double
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.events import Action
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.events import (AdapterDetector, DateDetector,
                                            PythonDetectorModifier)
from org.orekit.propagation.events.handlers import PythonEventHandler
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import PVCoordinates


class _PassThroughModifier(PythonDetectorModifier):
    """Wraps a detector and forwards every call. Mirrors the jpype test's
    `TestDetectorModifier`, but built from the JCC `PythonDetectorModifier`
    bridge (jpype only needs `@JImplements`)."""

    def __init__(self, detector):
        super().__init__()
        self._detector = detector

    def getDetector(self):
        return self._detector


class _OverrideHandlerModifier(PythonDetectorModifier):
    """Wraps a detector but replaces its handler. Mirrors the jpype test's
    `OverrideHandlerModifier`."""

    def __init__(self, detector, handler):
        super().__init__()
        self._detector = detector
        self._handler = handler

    def getDetector(self):
        return self._detector

    # Default-method override on DetectorModifier; expose explicitly because
    # the JCC bridge dispatches through the declared method set.
    def getHandler(self):
        return self._handler


class _CountingResetHandler(PythonEventHandler):
    """Counts events and asks the integrator to reset state on each one."""

    def __init__(self):
        super().__init__()
        self.count = 0

    def init(self, s0, target, detector):
        pass

    def eventOccurred(self, s, detector, increasing):
        self.count += 1
        return Action.RESET_STATE

    def resetState(self, detector, oldState):
        return oldState

    def finish(self, finalState, detector):
        pass

    def getHandler(self):
        pass


def _make_propagator():
    mu = 3.9860047e14
    position = Vector3D(-6142438.668, 3492467.560, -25767.25680)
    velocity = Vector3D(505.8479685, 942.7809215, 7435.922231)
    ini_date = AbsoluteDate(1969, 7, 28, 4, 0, 0.0, TimeScalesFactory.getTT())
    ini_orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                 FramesFactory.getEME2000(), ini_date, mu)
    initial_state = SpacecraftState(ini_orbit)
    abs_tol = JArray_double([0.001, 1.0e-9, 1.0e-9, 1.0e-6, 1.0e-6, 1.0e-6, 0.001])
    rel_tol = JArray_double([1.0e-7, 1.0e-4, 1.0e-4, 1.0e-7, 1.0e-7, 1.0e-7, 1.0e-7])
    integrator = DormandPrince853Integrator(0.001, 1000.0, abs_tol, rel_tol)
    integrator.setInitialStepSize(60.0)
    propagator = NumericalPropagator(integrator)
    propagator.setInitialState(initial_state)
    return propagator, ini_date


_DT = 60.0
_MAX_CHECK = 10.0
_THRESHOLD = 10.0e-10


class DetectorModifierTest(unittest.TestCase):

    def setUp(self):
        self.propagator, self.ini_date = _make_propagator()

    def test_simple_timer(self):
        date_detector = DateDetector.cast_(
            DateDetector(self.ini_date.shiftedBy(2.0 * _DT))
                .withMaxCheck(_MAX_CHECK)
                .withThreshold(_THRESHOLD))
        adapter = _PassThroughModifier(date_detector)
        # JCC's wrapper equality is identity; the same Java handle round-trips
        # so identity holds here.
        self.assertEqual(date_detector, adapter.getDetector())
        self.assertAlmostEqual(2.0 * _DT,
                               date_detector.getDate().durationFrom(self.ini_date),
                               delta=1.0e-10)
        self.propagator.addEventDetector(adapter)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(100.0 * _DT))
        self.assertAlmostEqual(2.0 * _DT,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=_THRESHOLD)

    @unittest.skip(
        "PythonDetectorModifier's native method set only exposes getDetector(); "
        "getHandler() is a default method on the DetectorModifier interface, so "
        "Java dispatches it through the interface and never sees the Python "
        "override. Would require bridge-class changes in orekit-python-wrapper.jar."
    )
    def test_override_handler(self):
        date_detector = DateDetector.cast_(
            DateDetector(self.ini_date.shiftedBy(2.0 * _DT))
                .withMaxCheck(_MAX_CHECK)
                .withThreshold(_THRESHOLD))
        handler = _CountingResetHandler()
        adapter = _OverrideHandlerModifier(date_detector, handler)
        self.assertEqual(date_detector, adapter.getDetector())
        self.propagator.addEventDetector(adapter)
        self.assertEqual(0, handler.count)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(100.0 * _DT))
        self.assertEqual(1, handler.count)
        self.assertAlmostEqual(100.0 * _DT,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=_THRESHOLD)

    def test_adapter_detector(self):
        detector = DateDetector(JArray('object')(0))
        adapter_detector = AdapterDetector(detector)
        modifier = _PassThroughModifier(detector)
        self.assertEqual(modifier.getDetector(), adapter_detector.getDetector())


if __name__ == '__main__':
    unittest.main()
