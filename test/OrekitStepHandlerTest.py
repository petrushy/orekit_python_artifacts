"""

/* Copyright 2002-2019 CS Systèmes d'Information
 * Licensed to CS Systèmes d'Information (CS) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * CS licenses this file to You under the Apache License, Version 2.0
 * (the "License") you may not use this file except in compliance with
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

Python version translated from Java by Petrus Hyvönen, SSC 2019
"""

import sys
import unittest
from collections import deque

import orekit
orekit.initVM()

#package org.orekit.propagation.sampling

#import static org.junit.Assert.assertEquals
#import static org.junit.Assert.assertNotNull
#import static org.junit.Assert.assertTrue

from org.orekit.data import DataProvidersManager, ZipJarCrawler
from java.io import File

#from java.util import ArrayDeque
from java.util import Arrays
from java.util import Queue
#from java.util.concurrent.Callable
#from java.util.concurrent.ExecutionException
#from java.util.concurrent.ExecutorService
#from java.util.concurrent import Executors
#from java.util.concurrent.Future

from org.hipparchus.ode.nonstiff import ClassicalRungeKuttaIntegrator
from org.hipparchus.util import FastMath
#from org.junit.Before
#from org.junit.Test
#from org.orekit import Utils
from org.orekit.bodies import CelestialBodyFactory
from org.orekit.frames import FactoryManagedFrame
from org.orekit.frames import Frame
from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit
from org.orekit.orbits import OrbitType
from org.orekit.orbits import PositionAngle
from org.orekit.propagation import Propagator
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.propagation.events import DateDetector
from org.orekit.propagation.events.handlers import ContinueOnEvent
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import AbsoluteDate
from org.orekit.time import TimeScalesFactory
from org.orekit.utils import Constants
from org.orekit.python import PythonOrekitStepHandler

class OrekitStepHandlerTest(unittest.TestCase):
    #
    #     def testForwardBackwardStep():
    #         initialDate = AbsoluteDate(2014, 01, 01, 00, 00,
    #                                                           00.000,
    #                                                           TimeScalesFactory.getUTC())
    #
    #         mu = CelestialBodyFactory.getEarth().getGM()
    #         inertialFrame = FramesFactory.getEME2000()
    #
    #         propagationTime = 7200.0 # seconds
    #         fixedStepSize = 3600 # seconds
    #
    #         semimajorAxis = 8000e3 # meters
    #         eccentricity = 0.001 # unitless
    #         inclination = FastMath.toRadians(15.0)
    #         argPerigee = FastMath.toRadians(10.0)
    #         raan = FastMath.toRadians(45.0)
    #         trueAnomaly = FastMath.toRadians(10.0)
    #
    #         initialOrbit = KeplerianOrbit(semimajorAxis,
    #                                                          eccentricity,
    #                                                          inclination,
    #                                                          argPerigee, raan,
    #                                                          trueAnomaly,
    #                                                          PositionAngle.TRUE,
    #                                                          inertialFrame,
    #                                                          initialDate, mu)
    #
    #         kepler = KeplerianPropagator(initialOrbit)
    #
    #         class MyHandler(PythonOrekitStepHandler):
    #             def init(self):  # All native defined calls needs to be implemented
    #                 pass
    #
    #             def handleStep(self, currentState, isLast):
    #                 pass
    #
    #         kepler.setMasterMode(fixedStepSize, MyHandler())
    #
    #         kepler.propagate(initialDate.shiftedBy(propagationTime))
    #
    #         stepSizeInSeconds = 120
    #         longestWaitTimeMS = 20
    #         service = Executors.ingleThreadExecutor()
    #         for (elapsedTime = 0 elapsedTime <= propagationTime elapsedTime += stepSizeInSeconds) {
    #             final double dt = elapsedTime
    #             Future<SpacecraftState> stateFuture = service
    #                 .submit(Callable<SpacecraftState>() {
    #
    #                     public SpacecraftState call()
    #                         {
    #                         return kepler.propagate(initialDate.shiftedBy(dt))
    #                     }
    #                 })
    #
    #             Thread.sleep(longestWaitTimeMS)
    #             assertTrue(stateFuture.isDone())
    #             SpacecraftState finalState = stateFuture.get()
    #             assertNotNull(finalState)
    #         }
    #     }

    #     /**
    #      * Check {@link OrekitStepInterpolator#isPreviousStateInterpolated()} and {@link
    #      * OrekitStepInterpolator#isCurrentStateInterpolated()}.
    #      */


    def testIsInterpolated(self):
        # setup
        propagator = NumericalPropagator(ClassicalRungeKuttaIntegrator(60.0))
        date = AbsoluteDate.J2000_EPOCH
        eci = FramesFactory.getGCRF()
        ic = SpacecraftState(KeplerianOrbit(6378137 + 500e3, 1e-3, 0.0, 0.0, 0.0, 0.0,
                 PositionAngle.TRUE, eci, date, Constants.EIGEN5C_EARTH_MU))
        propagator.setInitialState(ic)
        propagator.setOrbitType(OrbitType.CARTESIAN)
        # detector triggers half way through second step
        detector = DateDetector(date.shiftedBy(90.0)).withHandler(ContinueOnEvent())
        propagator.addEventDetector(detector)

        expected = deque([False, False, False, True, True, False])

        class MyHandler(PythonOrekitStepHandler):
            # All methods in an interface needs to be specified, even if no action is done.
            def init(self, s0, t):
                pass

            def handleStep(self, interpolator, isLast):
                assert(expected.popleft() == interpolator.isPreviousStateInterpolated())
                assert(expected.popleft() == interpolator.isCurrentStateInterpolated())

        propagator.setMasterMode(MyHandler())
        end = date.shiftedBy(120.0)
        prop_end = propagator.propagate(end)
        self.assertEqual(end, prop_end.getDate())
        print('testIsInterpolated OK')

    def setUp(self):
        #         Utils.setDataRoot("regular-data")

        DM = DataProvidersManager.getInstance()
        datafile = File('resources.zip')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = ZipJarCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OrekitStepHandlerTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
