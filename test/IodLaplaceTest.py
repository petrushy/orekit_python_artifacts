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

 Python version translated from Java by Petrus Hyvönen, SSC 2022

"""

import math
import sys
import unittest

# Python orekit specifics
import orekit
orekit.initVM()

from orekit.pyhelpers import  setup_orekit_curdir


from org.orekit.data import DataProvidersManager, ZipJarCrawler, DataContext
from java.io import File

# import java.util.List;
#
from org.hipparchus.geometry.euclidean.threed import Vector3D
# import org.junit.Assert;
# import org.junit.Test;
# import org.orekit.estimation.Context;
from org.hipparchus.util import FastMath

# from org.orekit.estimation import EstimationTestUtils
# import org.orekit.estimation.measurements.ObservedMeasurement;
# import org.orekit.estimation.measurements.PV;
# import org.orekit.estimation.measurements.PVMeasurementCreator;
# import org.orekit.frames.Frame;
from org.orekit.frames import FramesFactory, TopocentricFrame
# import org.orekit.orbits.KeplerianOrbit;
from org.orekit.orbits import OrbitType, KeplerianOrbit
from org.orekit.orbits import PositionAngle
# import org.orekit.propagation.Propagator;
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.propagation import SpacecraftState
# import org.orekit.propagation.conversion.NumericalPropagatorBuilder;
from org.orekit.time import AbsoluteDate, TimeScalesFactory
# import org.orekit.time.TimeScalesFactory;
from org.orekit.estimation.measurements import ObservableSatellite, PV, GroundStation, AngularRaDec
from PVMeasurementCreator import PVMeasurementCreator
from org.orekit.estimation.iod import IodLaplace
from org.orekit.utils import IERSConventions, Constants, AbsolutePVCoordinates
from org.orekit.bodies import OneAxisEllipsoid, GeodeticPoint
from orekit import JArray_double

#from .EstimationTestUtils import EstimationTestUtils

# Private class to calculate the errors between truth and estimated orbits at
# the central observation time.

class Result():
    def __init__(this, truth, estOrbit):
        this.errorNorm = JArray_double(2)

        this.errorNorm[0] = Vector3D.distance(truth.getPosition(),
						  estOrbit.getPVCoordinates().getPosition())

        this.errorNorm[1] = Vector3D.distance(truth.getVelocity(),
						  estOrbit.getPVCoordinates().getVelocity())
    def getErrorNorm(this):
        return this.errorNorm



class IodLaplaceTest(unittest.TestCase):

    def setUp(self):
        setup_orekit_curdir("resources")
        self.gcrf = FramesFactory.getGCRF()
        self.itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, False)

        # The ground station is set to Austin, Texas, U.S.A
        body = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                Constants.WGS84_EARTH_FLATTENING, self.itrf)

        self.observer = GroundStation(TopocentricFrame(body, GeodeticPoint(0.528253, -1.705768, 0.0), "Austin"))

        self.observer.getPrimeMeridianOffsetDriver().setReferenceDate(AbsoluteDate.J2000_EPOCH)
        self.observer.getPolarOffsetXDriver().setReferenceDate(AbsoluteDate.J2000_EPOCH)
        self.observer.getPolarOffsetYDriver().setReferenceDate(AbsoluteDate.J2000_EPOCH)


    def getLOSAngles(self, prop, date, observer):
        # Helper function to generate a Line of Sight angles measurement for the given
        # observer and date using the TLE propagator.

        satPvc = prop.getPVCoordinates(date, self.gcrf)
        raDec = AngularRaDec(observer, self.gcrf, date, JArray_double([0.0, 0.0]),
    						    JArray_double([1.0, 1.0]),
    						    JArray_double([1.0, 1.0]),
                                ObservableSatellite(0))

        angular = raDec.estimate(0, 0, [SpacecraftState(
    		    AbsolutePVCoordinates(self.gcrf, satPvc))]).getEstimatedValue()
        ra = angular[0]
        dec = angular[1]

        return Vector3D(FastMath.cos(dec)*FastMath.cos(ra),
    			    FastMath.cos(dec)*FastMath.sin(ra), FastMath.sin(dec))


    def estimateOrbit(self, prop, obsDate1, t2, t3):
        # Helper function to generate measurements and estimate orbit for the given propagator

        # Generate 3 Line Of Sight angles measurements
        los1 = self.getLOSAngles(prop, obsDate1, self.observer)

        obsDate2 = obsDate1.shiftedBy(t2)
        los2 = self.getLOSAngles(prop, obsDate2, self.observer)

        obsDate3 = obsDate1.shiftedBy(t3)
        los3 = self.getLOSAngles(prop, obsDate3, self.observer)

        obsPva = self.observer.getBaseFrame().getPVCoordinates(obsDate2, self.gcrf)

        # Estimate the orbit using the classical Laplace method
        truth = prop.getPVCoordinates(obsDate2, self.gcrf)
        estOrbit = IodLaplace(Constants.EGM96_EARTH_MU).estimate(self.gcrf, obsPva, obsDate1, los1, obsDate2, los2, obsDate3,
                                                                 los3)
        return Result(truth, estOrbit)

    def testLaplaceKeplerian1(self):
        # Estimate the orbit of ISS (ZARYA) based on Keplerian motion

        date = AbsoluteDate(2019, 9, 29, 22, 0, 2.0, TimeScalesFactory.getUTC())
        kep = KeplerianOrbit(6798938.970424857, 0.0021115522920270016, 0.9008866630545347,
    						      1.8278985811406743, -2.7656136723308524,
    						      0.8823034512437679, PositionAngle.MEAN, self.gcrf,
    						      date, Constants.EGM96_EARTH_MU)

        prop = KeplerianPropagator(kep)

        # With only 3 measurements, we can expect ~400 meters error in position and ~1 m/s in velocity
        error = self.estimateOrbit(prop, date, 30.0, 60.0).getErrorNorm()
        self.assertAlmostEquals(0.0, error[0], delta=275.0)
        self.assertAlmostEquals(0.0, error[1], delta=0.8)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IodLaplaceTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)