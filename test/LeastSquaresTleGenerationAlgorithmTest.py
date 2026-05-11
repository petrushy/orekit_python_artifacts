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

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.propagation.analytical.tle import TLE, TLEPropagator
from org.orekit.propagation.analytical.tle.generation import LeastSquaresTleGenerationAlgorithm


class LeastSquaresTleGenerationAlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.geoTLE = TLE("1 27508U 02040A   12021.25695307 -.00000113  00000-0  10000-3 0  7326",
                          "2 27508   0.0571 356.7800 0005033 344.4621 218.7816  1.00271798 34501")
        self.leoTLE = TLE("1 31135U 07013A   11003.00000000  .00000816  00000+0  47577-4 0    11",
                          "2 31135   2.4656 183.9084 0021119 236.4164  60.4567 15.10546832    15")

    def testConversionLeo(self):
        self.checkConversion(self.leoTLE, 1.0e-12, 3.755238453429068E-9)

    def testConversionGeo(self):
        self.checkConversion(self.geoTLE, 1.0e-12, 3.135996497102161E-9)

    def checkConversion(self, tle, threshold, rms):
        p = TLEPropagator.selectExtrapolator(tle)
        converter = LeastSquaresTleGenerationAlgorithm()
        converted = converter.generate(p.getInitialState(), tle)

        self.assertEqual(tle.getSatelliteNumber(), converted.getSatelliteNumber())
        self.assertEqual(tle.getClassification(), converted.getClassification())
        self.assertEqual(tle.getLaunchYear(), converted.getLaunchYear())
        self.assertEqual(tle.getLaunchNumber(), converted.getLaunchNumber())
        self.assertEqual(tle.getLaunchPiece(), converted.getLaunchPiece())
        self.assertEqual(tle.getElementNumber(), converted.getElementNumber())
        self.assertEqual(tle.getRevolutionNumberAtEpoch(), converted.getRevolutionNumberAtEpoch())

        self.assertAlmostEqual(tle.getMeanMotion(), converted.getMeanMotion(), delta=threshold * tle.getMeanMotion())
        self.assertAlmostEqual(tle.getE(), converted.getE(), delta=threshold * tle.getE())
        self.assertAlmostEqual(tle.getI(), converted.getI(), delta=threshold * tle.getI())
        self.assertAlmostEqual(tle.getPerigeeArgument(), converted.getPerigeeArgument(), delta=threshold * tle.getPerigeeArgument())
        self.assertAlmostEqual(tle.getRaan(), converted.getRaan(), delta=threshold * tle.getRaan())
        self.assertAlmostEqual(tle.getMeanAnomaly(), converted.getMeanAnomaly(), delta=threshold * tle.getMeanAnomaly())

        self.assertAlmostEqual(converter.getRms(), rms, delta=threshold)

    def testIssue864(self):
        tleISS = TLE("1 25544U 98067A   21035.14486477  .00001026  00000-0  26816-4 0  9998",
                     "2 25544  51.6455 280.7636 0002243 335.6496 186.1723 15.48938788267977")

        propagator = TLEPropagator.selectExtrapolator(tleISS)
        state = propagator.propagate(tleISS.getDate())

        # JCC can't bridge a Python lambda into a java.util.function.Consumer,
        # so iterate the ParameterDriver list directly instead of forEach.
        for driver in tleISS.getParametersDrivers():
            driver.setSelected(True)

        rebuilt = LeastSquaresTleGenerationAlgorithm().generate(state, tleISS)

        for driver in rebuilt.getParametersDrivers():
            self.assertTrue(driver.isSelected())


if __name__ == '__main__':
    unittest.main()
