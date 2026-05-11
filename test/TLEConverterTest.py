# -*- coding: utf-8 -*-
"""
original copyright:

/* Copyright 2002-2025 CS GROUP
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

JCC port translated from Orekit's Java TLEConverterTest, 2026.
"""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.orekit.errors import OrekitException, OrekitMessages
from org.orekit.orbits import PositionAngleType
from org.orekit.propagation.analytical.tle import TLE
from org.orekit.propagation.analytical.tle.generation import FixedPointTleGenerationAlgorithm
from org.orekit.propagation.conversion import TLEPropagatorBuilder


class TLEConverterTest(unittest.TestCase):

    def testDeselectOrbitals(self):
        tle = TLE("1 27508U 02040A   12021.25695307 -.00000113  00000-0  10000-3 0  7326",
                  "2 27508   0.0571 356.7800 0005033 344.4621 218.7816  1.00271798 34501")

        builder = TLEPropagatorBuilder(tle, PositionAngleType.MEAN, 1.0,
                                       FixedPointTleGenerationAlgorithm())

        for driver in builder.getOrbitalParametersDrivers().getDrivers():
            self.assertTrue(driver.isSelected())

        builder.deselectDynamicParameters()

        for driver in builder.getOrbitalParametersDrivers().getDrivers():
            self.assertFalse(driver.isSelected())

    def testIssue859(self):
        # INTELSAT 25 TLE taken from Celestrak on 2021-11-24T07:45:00.000.
        # The eccentricity and inclination are near zero, which exposes the
        # mean-parameter convergence issue this regression test covers.
        tle = TLE("1 33153U 08034A   21327.46310733 -.00000207  00000+0  00000+0 0  9990",
                  "2 33153   0.0042  20.7353 0003042 213.9370 323.2156  1.00270917 48929")

        propagatorBuilderError = TLEPropagatorBuilder(tle, PositionAngleType.MEAN, 1.0,
                                                      FixedPointTleGenerationAlgorithm())

        # The Java test calls the no-arg buildPropagator(). In this JCC
        # wrapper that overload reaches an empty-parameter path; use the
        # explicit normalized-parameters overload used elsewhere in the
        # Python suite.
        with self.assertRaises(JavaError) as ctx:
            propagatorBuilderError.buildPropagator(
                propagatorBuilderError.getSelectedNormalizedParameters())
        oe = OrekitException.cast_(ctx.exception.getJavaException())
        self.assertEqual(OrekitMessages.UNABLE_TO_COMPUTE_MEAN_PARAMETERS,
                         oe.getSpecifier())

        algorithm = FixedPointTleGenerationAlgorithm(
            FixedPointTleGenerationAlgorithm.EPSILON_DEFAULT, 1000, 0.5)
        propagatorBuilder = TLEPropagatorBuilder(tle, PositionAngleType.MEAN, 1.0,
                                                 algorithm)
        propagator = propagatorBuilder.buildPropagator(
            propagatorBuilderError.getSelectedNormalizedParameters())
        newTLE = propagator.getTLE()

        self.assertAlmostEqual(0.0, newTLE.getDate().durationFrom(tle.getDate()),
                               delta=1.0e-15)


if __name__ == '__main__':
    unittest.main()
