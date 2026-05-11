# -*- coding: utf-8 -*-
"""
original copyright:

/* Copyright 2002-2024 CS GROUP
 * Licensed to CS GROUP (CS) under one or more
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

Python version translated from Java by Petrus Hyvönen and copilot, 2024.
JCC port adapted from the orekit_jpype version, 2026.
"""

import math
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.propagation.analytical import EcksteinHechlerPropagator, Ephemeris
from org.hipparchus.ode.events import Action
from org.orekit.bodies import CelestialBodyFactory, OneAxisEllipsoid
from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit, OrbitType, PositionAngleType
from org.orekit.propagation import Propagator, SpacecraftState, SpacecraftStateInterpolator
from org.orekit.propagation.events import EclipseDetector
from org.orekit.propagation.events.handlers import PythonEventHandler
from org.orekit.time import AbsoluteDate, DateComponents, TimeComponents, TimeScalesFactory
from org.orekit.utils import IERSConventions
from java.util import ArrayList


class MyContinueOnEvent(PythonEventHandler):
    def __init__(self, outer_instance, orb_type):
        super().__init__()
        self.outer_instance = outer_instance
        self.orb_type = orb_type

    def init(self, initialstate, target, detector):
        pass

    def eventOccurred(self, s, detector, increasing):
        self.outer_instance.assertEqual(self.orb_type, s.getOrbit().getType())
        if increasing:
            self.outer_instance.inEclipsecounter += 1
        else:
            self.outer_instance.outEclipsecounter += 1
        return Action.CONTINUE

    def resetState(self, detector, oldState):
        return oldState

    # Required by JCC's PythonEventHandler bridge even though the Java
    # EventHandler interface does not declare it.
    def getHandler(self):
        pass

    def finish(self, finalState, detector):
        pass


class EphemerisEventsTest(unittest.TestCase):

    inEclipsecounter = 0
    outEclipsecounter = 0

    def setUp(self):
        self.inEclipsecounter = 0
        self.outEclipsecounter = 0

    def testEphemKeplerian(self):
        self.checkEphem(OrbitType.KEPLERIAN)

    def testEphemCircular(self):
        self.checkEphem(OrbitType.CIRCULAR)

    def testEphemEquinoctial(self):
        self.checkEphem(OrbitType.EQUINOCTIAL)

    def testEphemCartesian(self):
        self.checkEphem(OrbitType.CARTESIAN)

    def buildEphem(self, orb_type):
        mass = 2500.0
        a = 7187990.1979844316
        e = 0.5e-4
        i = 1.7105407051081795
        omega = 1.9674147913622104
        OMEGA = math.radians(261.0)
        lv = 0.0
        mu = 3.9860047e14
        ae = 6.378137e6
        c20 = -1.08263e-3
        c30 = 2.54e-6
        c40 = 1.62e-6
        c50 = 2.3e-7
        c60 = -5.5e-7

        deltaT = self.finalDate.durationFrom(self.initDate)

        frame = FramesFactory.getEME2000()

        transPar = KeplerianOrbit(a, e, i, omega, OMEGA, lv,
                                  PositionAngleType.TRUE, frame, self.initDate, mu)

        nbIntervals = 720
        propagator = EcksteinHechlerPropagator(transPar, mass, ae, mu,
                                               c20, c30, c40, c50, c60)

        # JCC's ArrayList does not accept a Python list directly; populate it
        # element by element (jpype auto-converts; JCC does not).
        tab = ArrayList()
        for j in range(nbIntervals + 1):
            state = propagator.propagate(self.initDate.shiftedBy((j * deltaT) / nbIntervals))
            tab.add(SpacecraftState(orb_type.convertType(state.getOrbit()),
                                    state.getAttitude(),
                                    state.getMass()))

        interpolator = SpacecraftStateInterpolator(2, frame, frame)
        return Ephemeris(tab, interpolator)

    def buildEclipseDetector(self, orb_type):
        sunRadius = 696000000.0
        earthRadius = 6400000.0

        ecl = EclipseDetector(CelestialBodyFactory.getSun(), sunRadius,
                              OneAxisEllipsoid(earthRadius, 0.0,
                                               FramesFactory.getITRF(IERSConventions.IERS_2010, True))) \
            .withMaxCheck(60.0) \
            .withThreshold(1.0e-3) \
            .withHandler(MyContinueOnEvent(self, orb_type))

        return ecl

    def checkEphem(self, orb_type):
        self.initDate = AbsoluteDate(DateComponents(2004, 1, 1),
                                     TimeComponents.H00,
                                     TimeScalesFactory.getUTC())
        self.finalDate = AbsoluteDate(DateComponents(2004, 1, 2),
                                      TimeComponents.H00,
                                      TimeScalesFactory.getUTC())

        ephem = self.buildEphem(orb_type)
        ephem.addEventDetector(self.buildEclipseDetector(orb_type))

        computeEnd = AbsoluteDate(self.finalDate, -1000.0)

        # clearStepHandlers is a default method on the Propagator interface;
        # JCC doesn't dispatch interface defaults on subclasses, so cast first.
        Propagator.cast_(ephem).clearStepHandlers()
        state = ephem.propagate(computeEnd)
        self.assertEqual(computeEnd, state.getDate())
        self.assertEqual(14, self.inEclipsecounter)
        self.assertEqual(14, self.outEclipsecounter)


if __name__ == '__main__':
    unittest.main()
