# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's OrDetectorTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from java.util import ArrayList, Collections
from org.hipparchus.ode.events import Action
from org.orekit.propagation.events import BooleanDetector, EventDetector
from org.orekit.propagation.events import EventDetectionSettings, PythonEventDetector
from org.orekit.propagation.events.handlers import PythonEventHandler
from org.orekit.propagation.events.intervals import PythonAdaptableInterval


class ConstantInterval(PythonAdaptableInterval):

    def __init__(self, value=10.0):
        super().__init__()
        self.value = float(value)

    def currentInterval(self, state, is_forward):
        return self.value


class ContinueHandler(PythonEventHandler):

    def __init__(self):
        super().__init__()

    def eventOccurred(self, s, detector, increasing):
        return Action.CONTINUE

    def init(self, s0, target, detector):
        pass

    def resetState(self, detector, old_state):
        return old_state

    def finish(self, final_state, detector):
        pass

    def getHandler(self):
        pass


class FixedGDetector(PythonEventDetector):

    def __init__(self, state):
        super().__init__()
        self.state = state
        self.handler = ContinueHandler()
        self.interval = ConstantInterval()

    def init(self, s0, target):
        pass

    def g(self, s):
        return float(self.state["g"])

    def getMaxCheckInterval(self):
        return self.interval

    def getThreshold(self):
        return EventDetectionSettings.DEFAULT_THRESHOLD

    def getMaxIterationCount(self):
        return EventDetectionSettings.DEFAULT_MAX_ITER

    def getHandler(self):
        return self.handler

    def reset(self, state, target):
        pass

    def finish(self, final_state):
        pass


class OrDetectorTest(unittest.TestCase):

    def setUp(self):
        self.state_a = {"g": 0.0}
        self.state_b = {"g": 0.0}
        self.a = FixedGDetector(self.state_a)
        self.b = FixedGDetector(self.state_b)
        detectors = ArrayList()
        detectors.add(EventDetector.cast_(self.a))
        detectors.add(EventDetector.cast_(self.b))
        self.or_detector = BooleanDetector.orCombine(detectors)

    def test_g(self):
        self.state_a["g"] = 0.0
        self.state_b["g"] = 0.0
        self.assertAlmostEqual(0.0, self.or_detector.g(None), delta=0.0)
        self.state_a["g"] = -1.0
        self.state_b["g"] = 0.0
        self.assertAlmostEqual(0.0, self.or_detector.g(None), delta=0.0)
        self.state_a["g"] = 0.0
        self.state_b["g"] = -1.0
        self.assertAlmostEqual(0.0, self.or_detector.g(None), delta=0.0)

        self.state_a["g"] = -1.0
        self.state_b["g"] = -1.0
        self.assertLess(self.or_detector.g(None), 0.0)

        self.state_a["g"] = 0.0
        self.state_b["g"] = 1.0
        self.assertGreater(self.or_detector.g(None), 0.0)
        self.state_a["g"] = 1.0
        self.state_b["g"] = -1.0
        self.assertGreater(self.or_detector.g(None), 0.0)
        self.state_a["g"] = 1.0
        self.state_b["g"] = 0.0
        self.assertGreater(self.or_detector.g(None), 0.0)
        self.state_a["g"] = -1.0
        self.state_b["g"] = 1.0
        self.assertGreater(self.or_detector.g(None), 0.0)
        self.state_a["g"] = 1.0
        self.state_b["g"] = 1.0
        self.assertGreater(self.or_detector.g(None), 0.0)

    def test_cancellation(self):
        self.state_a["g"] = -1.0e-10
        self.state_b["g"] = -1.0e10
        self.assertLess(self.or_detector.g(None), 0.0)
        self.state_a["g"] = -1.0e10
        self.state_b["g"] = -1.0e-10
        self.assertLess(self.or_detector.g(None), 0.0)
        self.state_a["g"] = -1.0e10
        self.state_b["g"] = 1.0e-10
        self.assertGreater(self.or_detector.g(None), 0.0)
        self.state_a["g"] = 1.0e-10
        self.state_b["g"] = -1.0e10
        self.assertGreater(self.or_detector.g(None), 0.0)
        self.state_a["g"] = 1.0e10
        self.state_b["g"] = -1.0e-10
        self.assertGreater(self.or_detector.g(None), 0.0)
        self.state_a["g"] = -1.0e-10
        self.state_b["g"] = 1.0e10
        self.assertGreater(self.or_detector.g(None), 0.0)

    def test_zero_detectors(self):
        with self.assertRaises(Exception):
            BooleanDetector.orCombine(Collections.emptyList())


if __name__ == '__main__':
    unittest.main()
