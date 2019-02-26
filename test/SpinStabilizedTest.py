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

from org.hipparchus.geometry.euclidean.threed import Rotation
from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.util import Decimal64Field
from org.hipparchus.util import FastMath

from org.orekit.bodies import CelestialBodyFactory

from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit
from org.orekit.orbits import PositionAngle
from org.orekit.propagation import FieldSpacecraftState
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.time import AbsoluteDate
from org.orekit.time import DateComponents
from org.orekit.time import FieldAbsoluteDate
from org.orekit.time import TimeComponents
from org.orekit.time import TimeScalesFactory
from org.orekit.utils import AngularCoordinates
from org.orekit.utils import PVCoordinates
from org.orekit.utils import PVCoordinatesProvider
from org.orekit.attitudes import CelestialBodyPointed, SpinStabilized, InertialProvider


class SpinStabilizedTest(unittest.TestCase):

    def setUp(self):
        DM = DataProvidersManager.getInstance()
        datafile = File('resources.zip')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = ZipJarCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)

    def testBBQModel(self):
        sun = CelestialBodyFactory.getSun()

        date = AbsoluteDate(DateComponents(1970, 1, 1),
                            TimeComponents(3, 25, 45.6789),
                            TimeScalesFactory.getTAI())

        rate = 2.0 * math.pi / (12 * 60)  # 12 minutes spin rate
        cbp = CelestialBodyPointed(FramesFactory.getEME2000(), sun, Vector3D.PLUS_K,
                                   Vector3D.PLUS_I, Vector3D.PLUS_K)

        bbq = SpinStabilized(cbp, date, Vector3D.PLUS_K, rate)
        pv = PVCoordinates(Vector3D(28812595.32012577, 5948437.4640250085, 0.0),
                           Vector3D(0.0, 0.0, 3680.853673522056))

        kep = KeplerianOrbit(pv, FramesFactory.getEME2000(), date, 3.986004415e14)

        attitude = bbq.getAttitude(kep, date, kep.getFrame())

        # Decimal64Field is The field of double precision floating-point numbers
        self.checkField(Decimal64Field.getInstance(), bbq, kep, kep.getDate(), kep.getFrame())

        xDirection = attitude.getRotation().applyInverseTo(Vector3D.PLUS_I)
        sunpos = PVCoordinatesProvider.cast_(sun).getPVCoordinates(date, FramesFactory.getEME2000()).getPosition()
        angle = Vector3D.angle(xDirection, sunpos)
        self.assertAlmostEqual(FastMath.atan(1.0 / 5000.0), angle, delta=2.0e-15)
        self.assertAlmostEqual(rate, attitude.getSpin().getNorm(), delta=1.0e-6)
        self.assertEqual(cbp.hashCode(), bbq.getUnderlyingAttitudeProvider().hashCode()) # The wrapped object seems to  thus hash is used

        print("testBBQModel finished ok")

    def testSpin(self):
        date = AbsoluteDate(DateComponents(1970, 1, 1),
                            TimeComponents(3, 25, 45.6789),
                            TimeScalesFactory.getTAI())

        rate = 2.0 * math.pi / (12 * 60)  # 12 minutes spin rate

        law = SpinStabilized(InertialProvider(Rotation.IDENTITY), date, Vector3D.PLUS_K, rate)

        orbit = KeplerianOrbit(7178000.0, 1.e-4, FastMath.toRadians(50.),
                              FastMath.toRadians(10.), FastMath.toRadians(20.),
                              FastMath.toRadians(30.), PositionAngle.MEAN,
                              FramesFactory.getEME2000(), date, 3.986004415e14)

        propagator = KeplerianPropagator(orbit, law)

        h = 10.0
        sMinus = propagator.propagate(date.shiftedBy(-h))
        s0     = propagator.propagate(date)
        sPlus  = propagator.propagate(date.shiftedBy(h))
        spin0  = s0.getAttitude().getSpin()

        # check that spin is consistent with attitude evolution
        errorAngleMinus     = Rotation.distance(sMinus.shiftedBy(h).getAttitude().getRotation(),
                                                       s0.getAttitude().getRotation())
        evolutionAngleMinus = Rotation.distance(sMinus.getAttitude().getRotation(),
                                                       s0.getAttitude().getRotation())
        self.assertTrue(errorAngleMinus <= 1.0e-6 * evolutionAngleMinus)

        errorAnglePlus      = Rotation.distance(s0.getAttitude().getRotation(),
                                                       sPlus.shiftedBy(-h).getAttitude().getRotation())
        evolutionAnglePlus  = Rotation.distance(s0.getAttitude().getRotation(),
                                                       sPlus.getAttitude().getRotation())
        self.assertTrue(errorAnglePlus <= 1.0e-6 * evolutionAnglePlus)

        # compute spin axis using finite differences
        rM = sMinus.getAttitude().getRotation()
        rP = sPlus.getAttitude().getRotation()
        reference = AngularCoordinates.estimateRate(rM, rP, 2 * h)

        self.assertAlmostEqual(2 * FastMath.PI / reference.getNorm(), 2 * FastMath.PI / spin0.getNorm(), delta=0.05)
        self.assertAlmostEqual(0.0, FastMath.toDegrees(Vector3D.angle(reference, spin0)), delta=1.0e-10)
        self.assertAlmostEqual(0.0, FastMath.toDegrees(Vector3D.angle(Vector3D.PLUS_K, spin0)), delta=1.0e-10)

    def checkField(self, field, provider, orbit, date, frame):
        attitudeD = provider.getAttitude(orbit, date, frame)
        orbitF = FieldSpacecraftState(field, SpacecraftState(orbit)).getOrbit()
        dateF = FieldAbsoluteDate(field, date)
        attitudeF = provider.getAttitude(orbitF, dateF, frame) # Get attitude in field-notation
        self.assertAlmostEqual(0.0, Rotation.distance(attitudeD.getRotation(), attitudeF.getRotation().toRotation()),
                               delta=1.0e-15)
        self.assertAlmostEqual(0.0, Vector3D.distance(attitudeD.getSpin(), attitudeF.getSpin().toVector3D()),
                               delta=1.0e-15)
        self.assertAlmostEqual(0.0,
            Vector3D.distance(attitudeD.getRotationAcceleration(), attitudeF.getRotationAcceleration().toVector3D()),
                               delta=1.0e-15)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SpinStabilizedTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
