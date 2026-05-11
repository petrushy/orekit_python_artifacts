# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's BetaAngleDetectorTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit import JArray_double
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.hipparchus.util import MathUtils
from org.orekit.bodies import CelestialBodyFactory
from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit
from org.orekit.propagation import Propagator, SpacecraftState
from org.orekit.propagation.events import BetaAngleDetector
from org.orekit.propagation.events.handlers import RecordAndContinue
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import PVCoordinates


def _normalize(vector):
    return vector.scalarMultiply(1.0 / vector.getNorm())


def _make_propagator():
    position = Vector3D(-6142438.668, 3492467.560, -25767.25680)
    velocity = Vector3D(505.8479685, 942.7809215, 7435.922231)
    ini_date = AbsoluteDate(1969, 7, 28, 4, 0, 0.0, TimeScalesFactory.getTT())
    orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                             FramesFactory.getGCRF(), ini_date, 3.9860047e14)
    initial_state = SpacecraftState(orbit)
    abs_tol = JArray_double([0.001, 1.0e-9, 1.0e-9, 1.0e-6,
                             1.0e-6, 1.0e-6, 0.001])
    rel_tol = JArray_double([1.0e-7, 1.0e-4, 1.0e-4, 1.0e-7,
                             1.0e-7, 1.0e-7, 1.0e-7])
    integrator = DormandPrince853Integrator(0.001, 1000.0, abs_tol, rel_tol)
    integrator.setInitialStepSize(60.0)
    propagator = NumericalPropagator(integrator)
    propagator.setInitialState(initial_state)
    return propagator, ini_date


class BetaAngleDetectorTest(unittest.TestCase):

    def setUp(self):
        self.propagator, self.date = _make_propagator()

    def test_evaluate(self):
        detector = BetaAngleDetector(0.0)
        gcrf = FramesFactory.getGCRF()
        sun = CelestialBodyFactory.getSun()

        date = self.date
        for _ in range(50):
            state = self.propagator.propagate(date)
            g = detector.g(state)
            beta = BetaAngleDetector.calculateBetaAngle(state, sun, gcrf)

            momentum = _normalize(state.getPVCoordinates(gcrf).getMomentum())
            sun_pos = _normalize(sun.getPosition(state.getDate(), gcrf))
            expected_beta = MathUtils.SEMI_PI - Vector3D.angle(momentum, sun_pos)

            self.assertAlmostEqual(-beta, g, delta=1.0e-9)
            self.assertAlmostEqual(expected_beta, beta, delta=1.0e-9)
            date = date.shiftedBy(86400.0)

    def test_simple_stop(self):
        detector = BetaAngleDetector(0.0,
                                     CelestialBodyFactory.getSun(),
                                     FramesFactory.getGCRF())
        self.propagator.addEventDetector(detector)
        state = Propagator.cast_(self.propagator).propagate(
            self.date, self.date.shiftedBy(30.0 * 86400.0))
        self.assertAlmostEqual(1883928.588393031,
                               state.getDate().durationFrom(self.date),
                               delta=1.0e-3)
        self.assertAlmostEqual(0.0,
                               BetaAngleDetector.calculateBetaAngle(
                                   state, self.propagator),
                               delta=1.0e-9)

    def test_record(self):
        handler = RecordAndContinue()
        detector = (BetaAngleDetector(0.0,
                                      CelestialBodyFactory.getMoon(),
                                      FramesFactory.getGCRF())
                    .withBetaThreshold(math.radians(1.0))
                    .withCelestialProvider(CelestialBodyFactory.getSun())
                    .withInertialFrame(FramesFactory.getEME2000())
                    .withHandler(handler))
        self.propagator.addEventDetector(detector)
        state = Propagator.cast_(self.propagator).propagate(
            self.date, self.date.shiftedBy(30.0 * 86400.0))
        self.assertAlmostEqual(30.0 * 86400.0,
                               state.getDate().durationFrom(self.date),
                               delta=1.0e-9)
        self.assertEqual(1, handler.getEvents().size())


if __name__ == '__main__':
    unittest.main()
