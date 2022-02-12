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

from org.orekit.data import DataProvidersManager, ZipJarCrawler, DataContext
from java.io import File

# import java.util.List;
#
from org.hipparchus.geometry.euclidean.threed import Vector3D
# import org.junit.Assert;
# import org.junit.Test;
# import org.orekit.estimation.Context;
# from org.orekit.estimation import EstimationTestUtils
# import org.orekit.estimation.measurements.ObservedMeasurement;
# import org.orekit.estimation.measurements.PV;
# import org.orekit.estimation.measurements.PVMeasurementCreator;
# import org.orekit.frames.Frame;
from org.orekit.frames import FramesFactory
# import org.orekit.orbits.KeplerianOrbit;
from org.orekit.orbits import OrbitType
from org.orekit.orbits import PositionAngle
# import org.orekit.propagation.Propagator;
# import org.orekit.propagation.conversion.NumericalPropagatorBuilder;
from org.orekit.time import AbsoluteDate, TimeScalesFactory
# import org.orekit.time.TimeScalesFactory;
from org.orekit.estimation.measurements import ObservableSatellite, PV
from PVMeasurementCreator import PVMeasurementCreator
from org.orekit.estimation.iod import IodGibbs

import pathlib, os
curdir = pathlib.Path(__file__).parent.resolve()

from EstimationTestUtils import EstimationTestUtils

class IodGibbsTest(unittest.TestCase):

    def testGibbs1(self):
        context = EstimationTestUtils().eccentricContext(os.path.join(curdir, "resources"))
        mu = context.initialOrbit.getMu()
        frame = context.initialOrbit.getFrame()

        propagatorBuilder = context.createBuilder(OrbitType.KEPLERIAN, PositionAngle.TRUE, True, 1.0e-6, 60.0, 0.001)

        # create perfect range measurements
        propagator = EstimationTestUtils().createPropagator(context.initialOrbit, propagatorBuilder)
        satellite = ObservableSatellite(0)
        measurements = EstimationTestUtils.createMeasurements(propagator, PVMeasurementCreator(),  0.0, 1.0, 60.0)

        position1 = Vector3D(*[x for x in measurements[0].getObservedValue()[0:3]])
        pv1 = PV(measurements[0].getDate(), position1, Vector3D.ZERO, 0., 0., 1., satellite)

        position2 = Vector3D(*[x for x in measurements[1].getObservedValue()[0:3]])
        pv2 = PV(measurements[1].getDate(), position2, Vector3D.ZERO, 0., 0., 1., satellite)

        position3 = Vector3D(*[x for x in measurements[2].getObservedValue()[0:3]])
        pv3 = PV(measurements[2].getDate(), position3, Vector3D.ZERO, 0., 0., 1., satellite)

        # instantiate the IOD method

        gibbs = IodGibbs(mu)
        orbit = gibbs.estimate(frame, pv1, pv2, pv3)

        self.assertAlmostEquals(context.initialOrbit.getA(), orbit.getA(), delta=1.0e-9 * context.initialOrbit.getA())
        self.assertAlmostEquals(context.initialOrbit.getE(), orbit.getE(), delta=1.0e-9 * context.initialOrbit.getA())
        self.assertAlmostEquals(context.initialOrbit.getI(), orbit.getI(), delta=1.0e-9 * context.initialOrbit.getA())

        pass


    def testGibbs2(self):

        # test extracted from "Fundamentals of astrodynamics & applications", D. Vallado, 3rd ed, chap Initial Orbit Determination, Exple 7-3, p457
        context = EstimationTestUtils().eccentricContext(os.path.join(curdir, "resources"))
        mu = context.initialOrbit.getMu()

        # Initialization
        gibbs = IodGibbs(mu)

        # Observation vector (EME2000)
        posR1 = Vector3D(0.0, 0.0, 6378137.0)
        posR2 = Vector3D(0.0, -4464696.0, -5102509.0)
        posR3 = Vector3D(0.0, 5740323.0, 3189068.0)

        # epoch corresponding to the observation vector
        dateRef = AbsoluteDate(2000, 1, 1, 0, 0, 0.0, TimeScalesFactory.getUTC())
        date2 = dateRef.shiftedBy(76.48)
        date3 = dateRef.shiftedBy(153.04)

        # Reference result (cf. Vallado)
        velR2 = Vector3D(0.0, 5531.148, -5191.806)

        # Gibbs IOD
        orbit = gibbs.estimate(FramesFactory.getEME2000(),
                                posR1, dateRef, posR2, date2, posR3, date3)

        # test
        self.assertAlmostEquals(0.0, orbit.getPVCoordinates().getVelocity().getNorm() - velR2.getNorm(), delta=1e-3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IodGibbsTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)