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

import unittest
import sys

# Python orekit specifics
import orekit
orekit.initVM()

from orekit import JArray_double
from org.orekit.data import DataProvidersManager, ZipJarCrawler
from org.orekit.propagation.integration import PythonAdditionalEquations
from org.orekit.propagation.integration import AdditionalEquations
from org.orekit.forces.gravity.potential import GravityFieldFactory
from org.orekit.forces.gravity.potential import SHMFormatReader
from java.io import File
from java.lang import System


from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator

from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit
from org.orekit.orbits import OrbitType
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.propagation.semianalytical.dsst import DSSTPropagator
from org.orekit.time import AbsoluteDate
from org.orekit.utils import PVCoordinates


# The class to be the additional equation
class InitCheckerEquations(PythonAdditionalEquations):  # implements AdditionalEquations

    # This is the method called for object creation as in java InitCheckerEquations(self, expected)
    def __init__(self, expected):
        super(InitCheckerEquations, self).__init__()
        self.expected = expected
        self.called = False

    # Part of AdditionalEquations interface
    def init(self, initialState, target):
        assert (self.expected - 1.0e-15) < initialState.getAdditionalState(self.getName())[0] < (self.expected + 1.0e-15)
        self.called = True

    # Part of AdditionalEquations interface
    def computeDerivatives(self, s, pDot):
        pDot[0] = 1.5
        return JArray_double(6)

    # Part of AdditionalEquations interface
    def getName(self):
        return "linear"

    def wasCalled(self):
        return self.called


class AdditionalEquationsTest(unittest.TestCase):

    def setUp(self):
        DM = DataProvidersManager.getInstance()
        datafile = File('resources.zip')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = ZipJarCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)
        System.setProperty(DataProvidersManager.OREKIT_DATA_PATH, 'potential/shm-format')
        GravityFieldFactory.addPotentialCoefficientsReader(SHMFormatReader("^eigen_cg03c_coef$", False))

        mu = GravityFieldFactory.getUnnormalizedProvider(0, 0).getMu()
        position = Vector3D(7.0e6, 1.0e6, 4.0e6)
        velocity = Vector3D(-500.0, 8000.0, 1000.0)
        self.initDate = AbsoluteDate.J2000_EPOCH
        orbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                 FramesFactory.getEME2000(), self.initDate, mu)
        self.initialState = SpacecraftState(orbit)
        self.tolerance = NumericalPropagator.tolerances(0.001, orbit, OrbitType.EQUINOCTIAL)

        print('Setup Finished ok')

    def tearDown(self):
        self.initDate = None
        self.initialState = None
        self.tolerance = None

    # Test for issue #401 with numerical propagator
    def testInitNumerical(self):
        # setup
        reference = 1.25
        checker = InitCheckerEquations(reference)
        self.assertFalse(checker.wasCalled())

        # action
        integrator = DormandPrince853Integrator(0.001, 200.0, JArray_double.cast_(self.tolerance[0]),
                                                JArray_double.cast_(self.tolerance[1]))
        integrator.setInitialStepSize(60.0)
        propagatorNumerical = NumericalPropagator(integrator)
        propagatorNumerical.setInitialState(self.initialState.addAdditionalState(checker.getName(), reference))
        propagatorNumerical.addAdditionalEquations(checker)
        propagatorNumerical.propagate(self.initDate.shiftedBy(600.0))

        # verify
        self.assertTrue(checker.wasCalled())

        print('testInitNumerical finished ok')

    # Test for issue #401 with a DSST propagator
    def testInitDSST(self):

        # setup
        reference = 3.5
        checker = InitCheckerEquations(reference)
        self.assertFalse(checker.wasCalled())

        # action
        integrator = DormandPrince853Integrator(0.001, 200.0, JArray_double.cast_(self.tolerance[0]),
                                                JArray_double.cast_(self.tolerance[1]))
        integrator.setInitialStepSize(60.0)

        propagatorDSST = DSSTPropagator(integrator)
        propagatorDSST.setInitialState(self.initialState.addAdditionalState(checker.getName(), reference))
        propagatorDSST.addAdditionalEquations(checker)
        propagatorDSST.propagate(self.initDate.shiftedBy(600.0))

        # verify
        self.assertTrue(checker.wasCalled())
        print('testInitDSST was successfully finished')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AdditionalEquationsTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
