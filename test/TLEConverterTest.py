# -*- coding: utf-8 -*-

"""

/* Copyright 2002-2013 CS Syst��mes d'Information
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

Java version translated to Python by Petrus Hyvönen, SSC 2017

 """

import orekit

orekit.initVM()
from orekit.pyhelpers import setup_orekit_curdir

from org.orekit.orbits import PositionAngle
from org.orekit.propagation.conversion import FiniteDifferencePropagatorConverter
from org.orekit.propagation.conversion import TLEPropagatorBuilder
from org.orekit.propagation.analytical.tle import TLE
from org.orekit.propagation.analytical.tle import TLEPropagator
from org.orekit.data import DataProvidersManager, ZipJarCrawler
from java.util import Arrays
from java.io import File

import unittest
import sys

class TLEConverterTest(unittest.TestCase):

    def checkFit(self, tle,
                 duration,
                 stepSize,
                 threshold,
                 positionOnly,
                 withBStar,
                 expectedRMS):

        p = TLEPropagator.selectExtrapolator(tle)

        sample = []
        dt = 0.0
        while dt < duration:
            sample.append(p.propagate(tle.getDate().shiftedBy(dt)))
            dt += stepSize

        builder = TLEPropagatorBuilder(tle, PositionAngle.TRUE, 1.0)

        drivers = builder.getPropagationParametersDrivers().getDrivers()

        # there should *not *be any drivers for central attraction coefficient (see issue  # 313)
        self.assertEqual(1, drivers.size())
        self.assertEqual("BSTAR", drivers.get(0).getName())

        fitter = FiniteDifferencePropagatorConverter(builder, threshold, 1000)
        sample = Arrays.asList(sample)

        if withBStar:
            fitter.convert(sample, positionOnly, TLEPropagatorBuilder.B_STAR)
        else:
            fitter.convert(sample, positionOnly, [])

        prop = TLEPropagator.cast_(fitter.getAdaptedPropagator())
        fitted = prop.getTLE()

        tolerance = max(threshold, 0.001 * expectedRMS)

        self.assertAlmostEqual(expectedRMS, fitter.getRMS(), delta=tolerance)

        self.assertEqual(tle.getSatelliteNumber(), fitted.getSatelliteNumber())
        self.assertEqual(tle.getClassification(), fitted.getClassification())
        self.assertEqual(tle.getLaunchYear(), fitted.getLaunchYear())
        self.assertEqual(tle.getLaunchNumber(), fitted.getLaunchNumber())
        self.assertEqual(tle.getLaunchPiece(), fitted.getLaunchPiece())
        self.assertEqual(tle.getElementNumber(), fitted.getElementNumber())
        self.assertEqual(tle.getRevolutionNumberAtEpoch(), fitted.getRevolutionNumberAtEpoch())

        eps = 1.0e-5
        self.assertAlmostEqual(tle.getMeanMotion(), fitted.getMeanMotion(), delta=eps * tle.getMeanMotion())
        self.assertAlmostEqual(tle.getE(), fitted.getE(), delta=eps * tle.getE())
        self.assertAlmostEqual(tle.getI(), fitted.getI(), delta=eps * tle.getI())
        self.assertAlmostEqual(tle.getPerigeeArgument(), fitted.getPerigeeArgument(),
                                delta=eps * tle.getPerigeeArgument())
        self.assertAlmostEqual(tle.getRaan(), fitted.getRaan(), delta=eps * tle.getRaan())
        self.assertAlmostEqual(tle.getMeanAnomaly(), fitted.getMeanAnomaly(), delta=eps * tle.getMeanAnomaly())

        if withBStar:
            self.assertAlmostEqual(tle.getBStar(), fitted.getBStar(), delta=eps * tle.getBStar())

    def testConversionGeoPositionVelocity(self):
        self.checkFit(self.geoTLE, 86400, 300, 1.0e-3, False, False, 9.350e-8)

    def testConversionGeoPositionOnly(self):
        self.checkFit(self.geoTLE, 86400, 300, 1.0e-3, True, False, 1.328e-7)

    def testConversionLeoPositionVelocityWithoutBStar(self):
        self.checkFit(self.leoTLE, 86400, 300, 1.0e-3, False, False, 10.77)

    def testConversionLeoPositionOnlyWithoutBStar(self):
        self.checkFit(self.leoTLE, 86400, 300, 1.0e-3, True, False, 15.23)

    def testConversionLeoPositionVelocityWithBStar(self):
        self.checkFit(self.leoTLE, 86400, 300, 1.0e-3, False, True, 2.646e-8)

    def testConversionLeoPositionOnlyWithBStar(self):
        self.checkFit(self.leoTLE, 86400, 300, 1.0e-3, True, True, 4.102e-8)

    def setUp(self):
        #setup_orekit_curdir()

        DM = DataProvidersManager.getInstance()
        datafile = File('resources.zip')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = ZipJarCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)

        self.geoTLE = TLE("1 27508U 02040A   12021.25695307 -.00000113  00000-0  10000-3 0  7326",
                          "2 27508   0.0571 356.7800 0005033 344.4621 218.7816  1.00271798 34501")
        self.leoTLE = TLE("1 31135U 07013A   11003.00000000  .00000816  00000+0  47577-4 0    11",
                          "2 31135   2.4656 183.9084 0021119 236.4164  60.4567 15.10546832    15")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TLEConverterTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
