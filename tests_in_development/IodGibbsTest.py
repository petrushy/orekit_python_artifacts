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

 Python version translated from Java by Petrus Hyvönen, SSC 2018

"""

import math
import sys
import unittest

# Python orekit specifics
import orekit
orekit.initVM()

from org.orekit.data import DataProvidersManager, ZipJarCrawler
from java.io import File

# import java.util.List;
#
# import org.hipparchus.geometry.euclidean.threed.Vector3D;
# import org.junit.Assert;
# import org.junit.Test;
# import org.orekit.estimation.Context;
# from org.orekit.estimation import EstimationTestUtils
# import org.orekit.estimation.measurements.ObservedMeasurement;
# import org.orekit.estimation.measurements.PV;
# import org.orekit.estimation.measurements.PVMeasurementCreator;
# import org.orekit.frames.Frame;
# import org.orekit.frames.FramesFactory;
# import org.orekit.orbits.KeplerianOrbit;
# import org.orekit.orbits.OrbitType;
# import org.orekit.orbits.PositionAngle;
# import org.orekit.propagation.Propagator;
# import org.orekit.propagation.conversion.NumericalPropagatorBuilder;
# import org.orekit.time.AbsoluteDate;
# import org.orekit.time.TimeScalesFactory;

from .EstimationTestUtils import EstimationTestUtils


class IodGibbsTest(unittest.TestCase):

    def testGibbs1(self):
        DM = DataProvidersManager.getInstance()
        datafile = File('regular-data.zip')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = ZipJarCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)

        context = EstimationTestUtils().eccentricContext("potential/tides")
        mu = context.initialOrbit.getMu()
        frame = context.initialOrbit.getFrame()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IodGibbsTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)