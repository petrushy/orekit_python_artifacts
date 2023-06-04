import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import  setup_orekit_curdir
setup_orekit_curdir("resources")

from org.hipparchus.ode.nonstiff import AdaptiveStepsizeIntegrator

from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit, OrbitType
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.events import DateDetector
from org.orekit.propagation.integration import PythonAdditionalDerivativesProvider, CombinedDerivatives
from org.orekit.propagation.sampling import PythonOrekitStepHandler
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import PVCoordinates
from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from orekit import JArray_double


class DateDetectorTest(unittest.TestCase):

    def test_simple_timer(self):
        self.dateDetector = DateDetector(self.maxCheck, self.threshold, self.iniDate.shiftedBy(2.0 * self.dt))
        self.assertEqual(2 * self.dt, self.dateDetector.getDate().durationFrom(self.iniDate), 1.0e-10)

        class DummyAdditionalDerivativesProvider(PythonAdditionalDerivativesProvider):

            def init(self, initialState, target):
                pass

            def getName(self):
                return "dummy"

            def getDimension(self):
                return 1

            def derivatives(self, state):
                return JArray_double([0.0])

            def combinedDerivatives(self, s):
                return CombinedDerivatives(JArray_double([0.0]), None)

            def yield_(self, state):
                return True

        class InterpolatorStepHandler(PythonOrekitStepHandler):

            def handleStep(self, interpolator, isLast):
                prev = interpolator.getPreviousState()
                curr = interpolator.getCurrentState()
                dt = curr.getDate().durationFrom(prev.getDate())
                restricted = interpolator.restrictStep(prev.shiftedBy(dt * +0.25), curr.shiftedBy(dt * -0.25))
                restricted_prev = restricted.getPreviousState()
                restricted_curr = restricted.getCurrentState()
                restricted_dt = restricted_curr.getDate().durationFrom(restricted_prev.getDate())
                self.assertEqual(dt * 0.5, restricted_dt, 1.0e-10)

        self.propagator.addAdditionalDerivativesProvider(DummyAdditionalDerivativesProvider())
        self.propagator.setInitialState(self.propagator.getInitialState().addAdditionalState("dummy", JArray_double([0.0])))

        self.propagator.getMultiplexer().add(InterpolatorStepHandler())
        self.propagator.setOrbitType(OrbitType.EQUINOCTIAL)
        self.propagator.addEventDetector(self.dateDetector)
        final_state = self.propagator.propagate(self.iniDate.shiftedBy(100.0 * self.dt))

        self.assertEqual(2.0 * self.dt, final_state.getDate().durationFrom(self.iniDate), self.threshold)


    def setUp(self):
        try:
            mu = 3.9860047e14
            position = Vector3D(-6142438.668, 3492467.560, -25767.25680)
            velocity = Vector3D(505.8479685, 942.7809215, 7435.922231)
            self.iniDate = AbsoluteDate(1969, 7, 28, 4, 0, 0.0, TimeScalesFactory.getTT())
            self.iniOrbit = EquinoctialOrbit(PVCoordinates(position, velocity), FramesFactory.getEME2000(),
                                             self.iniDate, mu)
            initial_state = SpacecraftState(self.iniOrbit)
            abs_tolerance = [0.001, 1.0e-9, 1.0e-9, 1.0e-6, 1.0e-6, 1.0e-6, 0.001]
            rel_tolerance = [1.0e-7, 1.0e-4, 1.0e-4, 1.0e-7, 1.0e-7, 1.0e-7, 1.0e-7]
            integrator = DormandPrince853Integrator(0.001, 1000.0,
                                                    JArray_double(abs_tolerance),
                                                    JArray_double(rel_tolerance))
            integrator.setInitialStepSize(60.0)
            self.propagator = NumericalPropagator(integrator)
            self.propagator.setInitialState(initial_state)
            self.dt = 60.0
            self.maxCheck = 10.0
            self.threshold = 10.0e-10
            self.evtno = 0
        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
