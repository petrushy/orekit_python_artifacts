# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's EclipseDetectorTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit import JArray_double, JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.bodies import CelestialBodyFactory, OneAxisEllipsoid
from org.orekit.errors import OrekitException, OrekitMessages
from org.orekit.frames import FramesFactory
from org.orekit.orbits import CartesianOrbit, EquinoctialOrbit
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.events import AbstractDetector, EclipseDetector
from org.orekit.propagation.events.handlers import StopOnDecreasing
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import IERSConventions, PVCoordinates, TimeStampedPVCoordinates


class EclipseDetectorTest(unittest.TestCase):

    def setUp(self):
        self.mu = 3.9860047e14
        position = Vector3D(-6142438.668, 3492467.560, -25767.25680)
        velocity = Vector3D(505.8479685, 942.7809215, 7435.922231)
        self.ini_date = AbsoluteDate(1969, 7, 28, 4, 0, 0.0,
                                     TimeScalesFactory.getTT())
        orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                 FramesFactory.getGCRF(), self.ini_date, self.mu)
        initial_state = SpacecraftState(orbit)
        abs_tolerance = JArray_double([0.001, 1.0e-9, 1.0e-9, 1.0e-6,
                                       1.0e-6, 1.0e-6, 0.001])
        rel_tolerance = JArray_double([1.0e-7, 1.0e-4, 1.0e-4, 1.0e-7,
                                       1.0e-7, 1.0e-7, 1.0e-7])
        integrator = DormandPrince853Integrator(0.001, 1000.0,
                                                abs_tolerance, rel_tolerance)
        integrator.setInitialStepSize(60.0)
        self.propagator = NumericalPropagator(integrator)
        self.propagator.setInitialState(initial_state)
        self.sun = CelestialBodyFactory.getSun()
        self.earth = OneAxisEllipsoid(6400000.0, 0.0,
                                      FramesFactory.getITRF(
                                          IERSConventions.IERS_2010, True))
        self.sun_radius = 696000000.0

    def _assert_settings(self, detector, max_check, threshold, max_iter):
        settings = detector.getDetectionSettings()
        self.assertAlmostEqual(max_check,
                               settings.getMaxCheckInterval().currentInterval(None, True),
                               delta=1.0e-15)
        self.assertAlmostEqual(threshold, settings.getThreshold(), delta=1.0e-15)
        self.assertEqual(max_iter, settings.getMaxIterationCount())

    def test_eclipse(self):
        detector = EclipseDetector.cast_(
            EclipseDetector(self.sun, self.sun_radius, self.earth)
            .withMaxCheck(60.0)
            .withThreshold(1.0e-3)
            .withHandler(StopOnDecreasing())
        ).withUmbra()
        self._assert_settings(detector, 60.0, 1.0e-3,
                              AbstractDetector.DEFAULT_MAX_ITER)
        self.assertAlmostEqual(0.0, detector.getMargin(), delta=1.0e-15)
        self.assertTrue(detector.getTotalEclipse())
        self.propagator.addEventDetector(detector)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(6000.0))
        self.assertAlmostEqual(2303.1835,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=1.0e-3)

    def test_penumbra(self):
        detector = EclipseDetector.cast_(
            EclipseDetector(self.sun, self.sun_radius, self.earth)
            .withMaxCheck(60.0)
            .withThreshold(1.0e-3)
        ).withPenumbra()
        self.assertFalse(detector.getTotalEclipse())
        self.propagator.addEventDetector(detector)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(6000.0))
        self.assertAlmostEqual(4388.155852,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=2.0e-6)

    def test_with_methods(self):
        detector = EclipseDetector.cast_(
            EclipseDetector(self.sun, self.sun_radius, self.earth)
            .withHandler(StopOnDecreasing())
            .withMaxCheck(120.0)
            .withThreshold(1.0e-4)
            .withMaxIter(12)
        ).withMargin(0.001)
        self._assert_settings(detector, 120.0, 1.0e-4, 12)
        self.propagator.addEventDetector(detector)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(6000.0))
        self.assertAlmostEqual(2304.188978,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=1.0e-4)

    def test_inside_occulting(self):
        detector = EclipseDetector(self.sun, self.sun_radius, self.earth)
        state = SpacecraftState(
            CartesianOrbit(
                TimeStampedPVCoordinates(AbsoluteDate.J2000_EPOCH,
                                         Vector3D(1.0e6, 2.0e6, 3.0e6),
                                         Vector3D(1000.0, 0.0, 0.0)),
                FramesFactory.getGCRF(),
                self.mu))
        with self.assertRaises(JavaError) as ctx:
            detector.g(state)
        exception = OrekitException.cast_(ctx.exception.getJavaException())
        self.assertEqual(OrekitMessages.POINT_INSIDE_ELLIPSOID,
                         exception.getSpecifier())

    def test_inside_occulted(self):
        detector = EclipseDetector(self.sun, self.sun_radius, self.earth)
        position = self.sun.getPosition(AbsoluteDate.J2000_EPOCH,
                                        FramesFactory.getGCRF())
        state = SpacecraftState(
            CartesianOrbit(
                TimeStampedPVCoordinates(AbsoluteDate.J2000_EPOCH,
                                         position.add(Vector3D.PLUS_I),
                                         Vector3D.PLUS_K),
                FramesFactory.getGCRF(),
                self.mu))
        self.assertAlmostEqual(math.pi, detector.g(state), delta=1.0e-15)

    def test_too_small_max_iteration_count(self):
        detector = EclipseDetector.cast_(
            EclipseDetector(self.sun, self.sun_radius, self.earth)
            .withHandler(StopOnDecreasing())
            .withMaxCheck(120.0)
            .withThreshold(1.0e-4)
            .withMaxIter(5)
        )
        self.propagator.addEventDetector(detector)
        with self.assertRaises(JavaError):
            self.propagator.propagate(self.ini_date.shiftedBy(6000.0))


if __name__ == '__main__':
    unittest.main()
