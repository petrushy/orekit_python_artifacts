# -*- coding: utf-8 -*-

"""

/* Copyright 2002-2019 CS Syst��mes d'Information
 * Licensed to CS Syst��mes d'Information (CS) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * CS licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

Python version translated from Java by Olivier Podevin, CS Group 2020

 """

import orekit

orekit.initVM()
from orekit.pyhelpers import setup_orekit_curdir, datetime_to_absolutedate

setup_orekit_curdir()

import unittest
import sys
import os
import math
from datetime import datetime

from java.util import ArrayList, List, HashMap, Map
from java.lang import Double, StringBuffer
from java.io import BufferedReader, StringReader

from org.hipparchus.geometry.euclidean.threed import Rotation, Vector3D
from org.hipparchus.util import FastMath

from org.orekit.attitudes import AttitudeProvider, InertialProvider
from org.orekit.bodies import CelestialBodyFactory
from org.orekit.files.ccsds import AEMParser, AEMWriter, AEMFile, Keyword, StreamingAemWriter
from org.orekit.frames import FramesFactory
from org.orekit.orbits import CartesianOrbit, KeplerianOrbit, PositionAngle
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.propagation.sampling import OrekitFixedStepHandler, OrekitFixedStepHandlerMultiplexer, PythonOrekitFixedStepHandler
from org.orekit.time import AbsoluteDate, TimeScalesFactory, TimeScale
from org.orekit.utils import Constants, IERSConventions, PVCoordinates



class InitCheckerHandler(PythonOrekitFixedStepHandler):

    def __init__(self, expected, initialized = False):
        super(InitCheckerHandler, self).__init__()
        self.expected = expected
        self.initialized = initialized

    def init(self, s0, t, step):
        self.initialized = True

    def handleStep(self, currentState, isLast):
       self.expected = 2.0        

    def isInitialized(self):
        return self.initialized

    def getExpected(self):
        return self.expected

class IncrementationHandler(PythonOrekitFixedStepHandler):

    def __init__(self):
        super(IncrementationHandler, self).__init__()      
        self.value = 0

    def init(self, s0, t, step):
        self.value = 1

    def handleStep(self, currentState, isLast):
        self.value += 1

    def getValue(self):
        return self.value

class OrekitFixedStepHandlerMultiplexerTest(unittest.TestCase):

    def testOrekitFixedStepHandlerMultiplexer(self):
        """Test the Orekit fixed StepHandler Multiplexer functionality"""

        # init
        initDate = AbsoluteDate(2020, 2, 28, 16, 15, 0.0, TimeScalesFactory.getUTC())

        initHandler = InitCheckerHandler(1.0)
        incrementationHandler = IncrementationHandler()

        multiplexer = OrekitFixedStepHandlerMultiplexer()
        multiplexer.add(initHandler)
        multiplexer.add(incrementationHandler)

        ic = KeplerianOrbit(6378137 + 500e3, 1e-3, 0.0, 0.0, 0.0, 0.0, 
                            PositionAngle.TRUE, 
                            FramesFactory.getGCRF(), 
                            initDate,
                            Constants.WGS84_EARTH_MU)
                            
        propagator = KeplerianPropagator(ic)
        propagator.setMasterMode(60.0, multiplexer)

        self.assertFalse(initHandler.isInitialized())
        self.assertTrue(math.isclose(1.0, initHandler.getExpected(), rel_tol = 0.0, abs_tol = Double.MIN_VALUE))

        propagator.propagate(initDate.shiftedBy(90.0))

        # verify
        self.assertTrue(initHandler.isInitialized())
        self.assertTrue(math.isclose(2.0, initHandler.getExpected(), rel_tol = 0.0, abs_tol = Double.MIN_VALUE))
        self.assertEqual(3, incrementationHandler.getValue())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OrekitFixedStepHandlerMultiplexerTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
