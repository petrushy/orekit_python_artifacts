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

from org.hipparchus.analysis.differentiation import DSFactory
from org.hipparchus.util import Binary64Field
from org.orekit.frames import FramesFactory
from org.orekit.orbits import CartesianOrbit
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.analytical.tle import FieldTLE, FieldTLEPropagator, TLE, TLEPropagator
from org.orekit.propagation.analytical.tle.generation import FixedPointTleGenerationAlgorithm
from org.orekit.utils import ParameterDriversProvider


class FixedPointTleGenerationAlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.geoTLE = TLE("1 27508U 02040A   12021.25695307 -.00000113  00000-0  10000-3 0  7326",
                          "2 27508   0.0571 356.7800 0005033 344.4621 218.7816  1.00271798 34501")
        self.leoTLE = TLE("1 31135U 07013A   11003.00000000  .00000816  00000+0  47577-4 0    11",
                          "2 31135   2.4656 183.9084 0021119 236.4164  60.4567 15.10546832    15")

    def testOneMoreRevolution(self):
        propagator = TLEPropagator.selectExtrapolator(self.leoTLE)
        initRevolutionNumber = self.leoTLE.getRevolutionNumberAtEpoch()
        dt = 2 * math.pi / self.leoTLE.getMeanMotion()
        target = self.leoTLE.getDate().shiftedBy(dt)
        endState = propagator.propagate(target)
        endLEOTLE = FixedPointTleGenerationAlgorithm().generate(endState, self.leoTLE)
        endRevolutionNumber = endLEOTLE.getRevolutionNumberAtEpoch()
        self.assertEqual(initRevolutionNumber + 1, endRevolutionNumber)

    def testOneLessRevolution(self):
        propagator = TLEPropagator.selectExtrapolator(self.leoTLE)
        initRevolutionNumber = self.leoTLE.getRevolutionNumberAtEpoch()
        dt = -2 * math.pi / self.leoTLE.getMeanMotion()
        target = self.leoTLE.getDate().shiftedBy(dt)
        endState = propagator.propagate(target)
        endLEOTLE = FixedPointTleGenerationAlgorithm().generate(endState, self.leoTLE)
        endRevolutionNumber = endLEOTLE.getRevolutionNumberAtEpoch()
        self.assertEqual(initRevolutionNumber - 1, endRevolutionNumber)

    def testIssue781(self):
        factory = DSFactory(6, 3)
        line1 = "1 05709U 71116A   21105.62692147  .00000088  00000-0  00000-0 0  9999"
        line2 = "2 05709  10.8207 310.3659 0014139  71.9531 277.0561  0.99618926100056"
        self.assertTrue(TLE.isFormatOK(line1, line2))
        fieldTLE = FieldTLE(factory.getDerivativeField(), line1, line2)
        # getParameters(Field) is a default method on ParameterDriversProvider;
        # JCC doesn't dispatch interface defaults on subclasses, so cast first.
        tlePropagator = FieldTLEPropagator.selectExtrapolator(
            fieldTLE,
            ParameterDriversProvider.cast_(fieldTLE).getParameters(factory.getDerivativeField()))
        fieldTLE1 = FixedPointTleGenerationAlgorithm().generate(tlePropagator.getInitialState(), fieldTLE)
        self.assertEqual(line2, fieldTLE1.getLine2())

    def testIssue802(self):
        tleISS = TLE("1 25544U 98067A   21035.14486477  .00001026  00000-0  26816-4 0  9998",
                     "2 25544  51.6455 280.7636 0002243 335.6496 186.1723 15.48938788267977")
        propagator = TLEPropagator.selectExtrapolator(tleISS)
        state = propagator.propagate(tleISS.getDate())
        eme2000 = FramesFactory.getEME2000()
        pv = state.getPVCoordinates(eme2000)
        orbit = CartesianOrbit(pv, eme2000, state.getOrbit().getMu())
        rebuilt = FixedPointTleGenerationAlgorithm().generate(SpacecraftState(orbit), tleISS)
        self.assertEqual(tleISS.getLine1(), rebuilt.getLine1())
        self.assertEqual(tleISS.getLine2(), rebuilt.getLine2())

    def testIssue802Field(self):
        self.doTestIssue802Field(Binary64Field.getInstance())

    def doTestIssue802Field(self, field):
        tleISS = FieldTLE(field,
                          "1 25544U 98067A   21035.14486477  .00001026  00000-0  26816-4 0  9998",
                          "2 25544  51.6455 280.7636 0002243 335.6496 186.1723 15.48938788267977")
        propagator = FieldTLEPropagator.selectExtrapolator(
            tleISS, ParameterDriversProvider.cast_(tleISS).getParameters(field))
        fieldTLE1 = FixedPointTleGenerationAlgorithm().generate(propagator.getInitialState(), tleISS)
        self.assertEqual(tleISS.getLine1(), fieldTLE1.getLine1())
        self.assertEqual(tleISS.getLine2(), fieldTLE1.getLine2())

    def testIssue864(self):
        tleISS = TLE("1 25544U 98067A   21035.14486477  .00001026  00000-0  26816-4 0  9998",
                     "2 25544  51.6455 280.7636 0002243 335.6496 186.1723 15.48938788267977")
        propagator = TLEPropagator.selectExtrapolator(tleISS)
        state = propagator.propagate(tleISS.getDate())
        # JCC can't bridge a Python lambda into a Java Consumer; iterate instead.
        for driver in tleISS.getParametersDrivers():
            driver.setSelected(True)
        rebuilt = FixedPointTleGenerationAlgorithm().generate(state, tleISS)
        for driver in rebuilt.getParametersDrivers():
            self.assertTrue(driver.isSelected())

    def testIssue859(self):
        tle = TLE("1 33153U 08034A   21327.46310733 -.00000207  00000+0  00000+0 0  9990",
                  "2 33153   0.0042  20.7353 0003042 213.9370 323.2156  1.00270917 48929")
        p = TLEPropagator.selectExtrapolator(tle)
        algorithm = FixedPointTleGenerationAlgorithm(FixedPointTleGenerationAlgorithm.EPSILON_DEFAULT, 400, 0.5)
        converted = algorithm.generate(p.getInitialState(), tle)
        self.assertEqual(tle.getLine2(), converted.getLine2())
        self.assertEqual(tle.getBStar(), converted.getBStar())
        self.assertEqual(0.0, converted.getDate().durationFrom(tle.getDate()))
        self.assertEqual(tle.getSatelliteNumber(), converted.getSatelliteNumber())
        self.assertEqual(tle.getClassification(), converted.getClassification())
        self.assertEqual(tle.getLaunchYear(), converted.getLaunchYear())
        self.assertEqual(tle.getLaunchNumber(), converted.getLaunchNumber())
        self.assertEqual(tle.getLaunchPiece(), converted.getLaunchPiece())
        self.assertEqual(tle.getElementNumber(), converted.getElementNumber())
        self.assertEqual(tle.getRevolutionNumberAtEpoch(), converted.getRevolutionNumberAtEpoch())

    def testIssue859Field(self):
        self.dotestIssue859Field(Binary64Field.getInstance())

    def dotestIssue859Field(self, field):
        tle = FieldTLE(field,
                       "1 33153U 08034A   21327.46310733 -.00000207  00000+0  00000+0 0  9990",
                       "2 33153   0.0042  20.7353 0003042 213.9370 323.2156  1.00270917 48929")
        p = FieldTLEPropagator.selectExtrapolator(
            tle, ParameterDriversProvider.cast_(tle).getParameters(field, tle.getDate()))
        algorithm = FixedPointTleGenerationAlgorithm(FixedPointTleGenerationAlgorithm.EPSILON_DEFAULT, 400, 0.5)
        converted = algorithm.generate(p.getInitialState(), tle)
        self.assertEqual(tle.getLine2(), converted.getLine2())
        self.assertEqual(tle.getBStar(), converted.getBStar())
        self.assertEqual(0.0, converted.getDate().durationFrom(tle.getDate()).getReal())
        self.assertEqual(tle.getSatelliteNumber(), converted.getSatelliteNumber())
        self.assertEqual(tle.getClassification(), converted.getClassification())
        self.assertEqual(tle.getLaunchYear(), converted.getLaunchYear())
        self.assertEqual(tle.getLaunchNumber(), converted.getLaunchNumber())
        self.assertEqual(tle.getLaunchPiece(), converted.getLaunchPiece())
        self.assertEqual(tle.getElementNumber(), converted.getElementNumber())
        self.assertEqual(tle.getRevolutionNumberAtEpoch(), converted.getRevolutionNumberAtEpoch())

    def testConversionLeo(self):
        self.checkConversion(self.leoTLE, 5.2e-9)

    def testConversionGeo(self):
        self.checkConversion(self.geoTLE, 9.2e-8)

    def checkConversion(self, tle, threshold):
        propagator = TLEPropagator.selectExtrapolator(tle)
        converted = FixedPointTleGenerationAlgorithm().generate(propagator.getInitialState(), tle)
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
        self.assertAlmostEqual(tle.getBStar(), converted.getBStar(), delta=threshold * tle.getBStar())

    def testConversionLeoField(self):
        self.doTestConversionLeoField(Binary64Field.getInstance())

    def doTestConversionLeoField(self, field):
        leoTLE = FieldTLE(field,
                          "1 31135U 07013A   11003.00000000  .00000816  00000+0  47577-4 0    11",
                          "2 31135   2.4656 183.9084 0021119 236.4164  60.4567 15.10546832    15")
        self.checkConversion_field(leoTLE, field, 5.2e-9)

    def testConversionGeoField(self):
        self.doConversionGeoField(Binary64Field.getInstance())

    def doConversionGeoField(self, field):
        geoTLE = FieldTLE(field,
                          "1 27508U 02040A   12021.25695307 -.00000113  00000-0  10000-3 0  7326",
                          "2 27508   0.0571 356.7800 0005033 344.4621 218.7816  1.00271798 34501")
        self.checkConversion_field(geoTLE, field, 9.2e-8)

    def checkConversion_field(self, tle, field, threshold):
        propagator = FieldTLEPropagator.selectExtrapolator(
            tle, ParameterDriversProvider.cast_(tle).getParameters(field, tle.getDate()))
        converted = FixedPointTleGenerationAlgorithm().generate(propagator.getInitialState(), tle)
        self.assertEqual(tle.getSatelliteNumber(), converted.getSatelliteNumber())
        self.assertEqual(tle.getClassification(), converted.getClassification())
        self.assertEqual(tle.getLaunchYear(), converted.getLaunchYear())
        self.assertEqual(tle.getLaunchNumber(), converted.getLaunchNumber())
        self.assertEqual(tle.getLaunchPiece(), converted.getLaunchPiece())
        self.assertEqual(tle.getElementNumber(), converted.getElementNumber())
        self.assertEqual(tle.getRevolutionNumberAtEpoch(), converted.getRevolutionNumberAtEpoch())
        self.assertAlmostEqual(tle.getMeanMotion().getReal(), converted.getMeanMotion().getReal(),
                               delta=threshold * tle.getMeanMotion().getReal())
        self.assertAlmostEqual(tle.getE().getReal(), converted.getE().getReal(),
                               delta=threshold * tle.getE().getReal())
        self.assertAlmostEqual(tle.getI().getReal(), converted.getI().getReal(),
                               delta=threshold * tle.getI().getReal())
        self.assertAlmostEqual(tle.getPerigeeArgument().getReal(), converted.getPerigeeArgument().getReal(),
                               delta=threshold * tle.getPerigeeArgument().getReal())
        self.assertAlmostEqual(tle.getRaan().getReal(), converted.getRaan().getReal(),
                               delta=threshold * tle.getRaan().getReal())
        self.assertAlmostEqual(tle.getMeanAnomaly().getReal(), converted.getMeanAnomaly().getReal(),
                               delta=threshold * tle.getMeanAnomaly().getReal())
        self.assertAlmostEqual(tle.getBStar(), converted.getBStar(), delta=threshold * tle.getBStar())


if __name__ == '__main__':
    unittest.main()
