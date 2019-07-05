# -*- coding: utf-8 -*-


"""
/* Copyright 2002-2019 CS Systèmes d'Information
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

import unittest, sys, math

# Python orekit specifics
import orekit

orekit.initVM()

from orekit import JArray_double
from org.orekit.data import DataProvidersManager, ZipJarCrawler
from org.orekit.propagation.integration import PythonFieldAdditionalEquations
from org.orekit.forces.gravity.potential import GravityFieldFactory
from org.orekit.forces.gravity.potential import SHMFormatReader
from java.io import File
from java.lang import System


from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus import RealFieldElement

from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.hipparchus.ode.nonstiff import DormandPrince853FieldIntegrator

from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit
from org.orekit.orbits import OrbitType
from org.orekit.propagation import SpacecraftState, FieldSpacecraftState
from org.orekit.propagation.numerical import NumericalPropagator, FieldNumericalPropagator
from org.orekit.propagation.semianalytical.dsst import DSSTPropagator
from org.orekit.time import AbsoluteDate, FieldAbsoluteDate
from org.orekit.utils import PVCoordinates
from org.orekit.bodies import GeodeticPoint, FieldGeodeticPoint

from org.hipparchus.util import MathArrays, Decimal64Field, FastMath, Precision

from org.orekit.models.earth.ionosphere import KlobucharIonoModel, IonosphericModel





class KlobucharModelTest(unittest.TestCase):

    epsilon = 1e-6

    # ionospheric model.
    model = None

    utc = None

    def setUp(self):
        self.model = KlobucharIonoModel([.3820e-07, .1490e-07, -.1790e-06, 0.0],
                                        [.1430e+06, 0.0, -.3280e+06, .1130e+06])

        # Initialize the data sources
        DM = DataProvidersManager.getInstance()
        datafile = File('resources.zip')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = ZipJarCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)


        print('Setup Finished ok')

    def tearDown(self):
        self.utc = None

    def testDelay(self):
        latitude = math.radians(45.0)
        longitude = math.radians(2.0)
        altitude = 500.0
        elevation = 70.0
        azimuth = 10.0

        date = AbsoluteDate()

        geo = GeodeticPoint(latitude, longitude, altitude)

        delayMeters = self.model.pathDelay(date, geo,
                                             math.radians(elevation),
                                             math.radians(azimuth),
                                             1575.42e6, IonosphericModel.cast_(self.model).getParameters())

        self.assertTrue(Precision.compareTo(delayMeters, 12., self.epsilon) < 0)
        self.assertTrue(Precision.compareTo(delayMeters, 0., self.epsilon) > 0)

    def doTestFieldDelay(self, field):
        zero = field.getZero();

        latitude  = zero.add(FastMath.toRadians(45.0))
        longitude = zero.add(FastMath.toRadians(2.0))
        altitude  = zero.add(500.0)
        elevation = zero.add(FastMath.toRadians(70.))
        azimuth   = zero.add(FastMath.toRadians(10.))

        date = FieldAbsoluteDate(field)

        geo = FieldGeodeticPoint(latitude, longitude, altitude)

        delayMeters = self.model.pathDelay(date, geo,
                                        elevation, azimuth,
                                        1575.42e6,
                                        IonosphericModel.cast_(self.model).getParameters(field))

        self.assertTrue(Precision.compareTo(delayMeters.getReal(), 12., self.epsilon) < 0)
        self.assertTrue(Precision.compareTo(delayMeters.getReal(), 0., self.epsilon) > 0)

    def testFieldDelay(self):
        self.doTestFieldDelay(Decimal64Field.getInstance())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KlobucharModelTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
