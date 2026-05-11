# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's AlignmentDetectorTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JArray_double
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.bodies import CelestialBodyFactory
from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.events import AlignmentDetector
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import PVCoordinates


class AlignmentDetectorTest(unittest.TestCase):

    def setUp(self):
        mu = 3.9860047e14
        position = Vector3D(-6142438.668, 3492467.560, -25767.25680)
        velocity = Vector3D(505.8479685, 942.7809215, 7435.922231)
        self.ini_date = AbsoluteDate(1969, 7, 28, 4, 0, 0.0,
                                     TimeScalesFactory.getTT())
        orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                 FramesFactory.getEME2000(), self.ini_date, mu)
        self.initial_state = SpacecraftState(orbit)
        abs_tolerance = JArray_double([0.001, 1.0e-9, 1.0e-9, 1.0e-6,
                                       1.0e-6, 1.0e-6, 0.001])
        rel_tolerance = JArray_double([1.0e-7, 1.0e-4, 1.0e-4, 1.0e-7,
                                       1.0e-7, 1.0e-7, 1.0e-7])
        integrator = DormandPrince853Integrator(0.001, 1000.0,
                                                abs_tolerance, rel_tolerance)
        integrator.setInitialStepSize(60.0)
        self.propagator = NumericalPropagator(integrator)
        self.propagator.setInitialState(self.initial_state)

    def test_alignment(self):
        align_angle = 0.0
        sun = CelestialBodyFactory.getSun()
        align_detector = AlignmentDetector.cast_(
            AlignmentDetector(self.initial_state.getOrbit(), sun, align_angle)
            .withMaxCheck(60.0)
        )
        self.assertAlmostEqual(align_angle, align_detector.getAlignAngle(),
                               delta=1.0e-15)
        self.assertEqual(sun, align_detector.getPVCoordinatesProvider())
        self.assertAlmostEqual(
            60.0,
            align_detector.getDetectionSettings().getMaxCheckInterval()
            .currentInterval(None, True),
            delta=1.0e-15,
        )
        self.propagator.addEventDetector(align_detector)
        final_state = self.propagator.propagate(self.ini_date.shiftedBy(6000.0))
        self.assertAlmostEqual(383.3662,
                               final_state.getDate().durationFrom(self.ini_date),
                               delta=1.0e-3)


if __name__ == '__main__':
    unittest.main()
