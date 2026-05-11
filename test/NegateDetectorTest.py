# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's NegateDetectorTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.ode.events import Action
from org.orekit.propagation.events import DateDetector, EventDetectionSettings
from org.orekit.propagation.events import NegateDetector, PythonEventDetector
from org.orekit.propagation.events.handlers import PythonEventHandler
from org.orekit.propagation.events.intervals import PythonAdaptableInterval
from org.orekit.time import AbsoluteDate


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


class NegateDetectorTest(unittest.TestCase):

    def test_get_detector(self):
        expected_detector = DateDetector(AbsoluteDate.J2000_EPOCH)
        detector = NegateDetector(expected_detector)
        self.assertEqual(expected_detector, detector.getDetector())
        self.assertEqual(expected_detector, detector.getOriginal())

    def test_g(self):
        state = {"g": 1.0}
        detector = NegateDetector(FixedGDetector(state))

        state["g"] = 1.0
        self.assertAlmostEqual(-1.0, detector.g(None), delta=0.0)

        state["g"] = -1.0
        self.assertAlmostEqual(1.0, detector.g(None), delta=0.0)

    def test_create(self):
        original = FixedGDetector({"g": 0.0})
        detector = NegateDetector(original)

        actual = detector.withMaxCheck(100.0)
        self.assertAlmostEqual(
            100.0,
            actual.getDetectionSettings().getMaxCheckInterval().currentInterval(None, True),
            delta=0.0,
        )
        self.assertTrue(actual.getOriginal().equals(original))


if __name__ == '__main__':
    unittest.main()
