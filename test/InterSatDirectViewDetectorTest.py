# -*- coding: utf-8 -*-

"""
/* Copyright 2002-2018 CS Systèmes d'Information
 * Licensed to CS Systèmes d'Information (CS) under one or more
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

Python version translated from Java by Petrus Hyvönen, SSC 2019

"""

import sys
import unittest

import orekit

orekit.initVM()
from orekit.pyhelpers import setup_orekit_curdir

setup_orekit_curdir()  # orekit-data.zip shall be in current dir

from org.orekit.propagation.events import EventsLogger
from org.hipparchus.util import FastMath
from org.orekit.frames import FramesFactory
from org.orekit.orbits import PositionAngle
from org.orekit.time import AbsoluteDate
from org.orekit.time import TimeScalesFactory
from org.orekit.utils import Constants
from org.orekit.propagation.sampling import PythonOrekitFixedStepHandler
from org.orekit.propagation.events import InterSatDirectViewDetector
from org.hipparchus.geometry.euclidean.threed import Line
from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import OneAxisEllipsoid
from org.orekit.frames import TopocentricFrame
from org.orekit.orbits import CircularOrbit
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.propagation.events.handlers import EventHandler, PythonEventHandler
from org.orekit.utils import IERSConventions

from org.hipparchus.ode.events import Action


class GrazingHandler(PythonEventHandler):

    def init(self, initialstate, target):
        pass

    def eventOccurred(self, s, detector, increasing):
        # just before increasing events and just after decreasing events,
        # the master/slave line intersects Earth limb
        detector = InterSatDirectViewDetector.cast_(detector)  # Otherwise this is just a plain EventDetector
        earth = detector.getCentralBody()
        frame = earth.getBodyFrame()
        dt = -1.0e-8 if increasing else +1.0e-8

        grazingDate = s.getDate().shiftedBy(dt)
        pMaster = s.shiftedBy(dt).getPVCoordinates(frame).getPosition()
        pSlave = detector.getSlave().getPVCoordinates(grazingDate, frame).getPosition()
        grazing = earth.getCartesianIntersectionPoint(Line(pMaster, pSlave, 1.0),
                                                      pMaster, frame, grazingDate)

        topo = TopocentricFrame(earth, earth.transform(grazing, frame, grazingDate),
                                "grazing")

        testvalue = FastMath.toDegrees(topo.getElevation(pMaster, frame, grazingDate))
        assert -2.0e4 < testvalue < 2.0e4

        testvalue = FastMath.abs(FastMath.toDegrees(topo.getAzimuth(pSlave, frame, grazingDate) -
                                                    topo.getAzimuth(pMaster, frame, grazingDate)))
        assert -6.0e-14 < testvalue - 180.0 < 6.0e-14

        return Action.CONTINUE

    # The full interface is required for java to accept it as a class of that type
    def resetState(self, detector, oldState):
        pass


class InterSatDirectViewDetectorTest(unittest.TestCase):

    def testFormationFlying(self):
        earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                 Constants.WGS84_EARTH_FLATTENING,
                                 FramesFactory.getITRF(IERSConventions.IERS_2010, True))
        utc = TimeScalesFactory.getUTC()
        o1 = CircularOrbit(7200000.0, 1.0e-3, 2.0e-4,
                           FastMath.toRadians(98.7), FastMath.toRadians(134.0),
                           FastMath.toRadians(21.0), PositionAngle.MEAN, FramesFactory.getGCRF(),
                           AbsoluteDate("2003-02-14T01:02:03.000", utc),
                           Constants.EIGEN5C_EARTH_MU)

        o2 = CircularOrbit(o1.getA(), 2.0e-4, 1.0e-3,
                           o1.getI() + 1.0e-6, o1.getRightAscensionOfAscendingNode() - 3.5e-7,
                           o1.getAlphaM() + 2.2e-6, PositionAngle.MEAN, o1.getFrame(),
                           o1.getDate(),
                           Constants.EIGEN5C_EARTH_MU)

        self.assertAlmostEqual(o1.getKeplerianPeriod(), o2.getKeplerianPeriod(), delta=1.0e-10)
        p = KeplerianPropagator(o1)
        logger = EventsLogger()
        p.addEventDetector(logger.monitorDetector(InterSatDirectViewDetector(earth, o2).
                                                  withMaxCheck(60.0)))

        class StepHandler(PythonOrekitFixedStepHandler):

            def init(self, s0, t, step):
                pass

            def handleStep(self, state, isLast):
                pos1 = state.getPVCoordinates().getPosition()
                pos2 = o2.getPVCoordinates(state.getDate(), state.getFrame()).getPosition()

                assert Vector3D.distance(pos1, pos2) > 8100.0
                assert Vector3D.distance(pos1, pos2) < 16400.0

        p.setMasterMode(10.0, StepHandler())
        p.propagate(o1.getDate().shiftedBy(o1.getKeplerianPeriod()))
        self.assertEqual(0, logger.getLoggedEvents().size())

    def testLeoMeo(self):
        earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                 Constants.WGS84_EARTH_FLATTENING,
                                 FramesFactory.getITRF(IERSConventions.IERS_2010, True))

        utc = TimeScalesFactory.getUTC()
        o1 = CircularOrbit(7200000.0, 1.0e-3, 2.0e-4,
                           FastMath.toRadians(50.0), FastMath.toRadians(134.0),
                           FastMath.toRadians(21.0), PositionAngle.MEAN, FramesFactory.getGCRF(),
                           AbsoluteDate("2003-02-14T01:02:03.000", utc),
                           Constants.EIGEN5C_EARTH_MU)

        o2 = CircularOrbit(29600000.0, 2.0e-4, 1.0e-3,
                           FastMath.toRadians(56.0), FastMath.toRadians(111.0),
                           o1.getAlphaM() + 2.2e-6, PositionAngle.MEAN, o1.getFrame(),
                           o1.getDate(),
                           Constants.EIGEN5C_EARTH_MU)

        # LEO as master, MEO as slave
        pA = KeplerianPropagator(o1)
        loggerA = EventsLogger()
        pA.addEventDetector(loggerA.monitorDetector(InterSatDirectViewDetector(earth, o2).
                                                    withMaxCheck(10.0).
                                                    withHandler(GrazingHandler().of_(InterSatDirectViewDetector))))

        propdate = o1.getDate().shiftedBy(4 * o1.getKeplerianPeriod())
        pA.propagate(propdate)

        self.assertEqual(7, loggerA.getLoggedEvents().size())

        # LEO as slave, MEO as master
        pB = KeplerianPropagator(o2)
        loggerB = EventsLogger()
        pB.addEventDetector(loggerB.monitorDetector(InterSatDirectViewDetector(earth, o1).
                                                    withMaxCheck(10.0).
                                                    withHandler(GrazingHandler().of_(InterSatDirectViewDetector))))

        pB.propagate(o1.getDate().shiftedBy(4 * o1.getKeplerianPeriod()))
        self.assertEqual(7, loggerB.getLoggedEvents().size())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InterSatDirectViewDetectorTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
