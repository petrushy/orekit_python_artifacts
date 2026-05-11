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

from orekit import JArray, JArray_double, JavaError
from orekit.pyhelpers import setup_orekit_data
# Mirrors Java's Utils.setDataRoot("regular-data:potential/icgem-format")
setup_orekit_data(filenames=["resources/regular-data",
                             "resources/potential/icgem-format"],
                  from_pip_library=False)

from org.hipparchus.geometry.euclidean.threed import Rotation
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.attitudes import BodyCenterPointing
from org.orekit.bodies import CelestialBodyFactory, OneAxisEllipsoid
from org.orekit.forces.gravity import HolmesFeatherstoneAttractionModel, SingleBodyAbsoluteAttraction
from org.orekit.forces.gravity.potential import GravityFieldFactory
from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit, PositionAngleType
from org.orekit.propagation import SpacecraftState, SpacecraftStateInterpolator
from org.orekit.propagation.analytical import EcksteinHechlerPropagator
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.time import (AbsoluteDate, AbstractTimeInterpolator,
                             DateComponents, TimeComponents, TimeScalesFactory)
from org.orekit.utils import (AbsolutePVCoordinates, AngularDerivativesFilter,
                              CartesianDerivativesFilter, Constants,
                              IERSConventions, PVCoordinates)
from java.util import ArrayList


class SpacecraftStateInterpolatorTest(unittest.TestCase):

    def setUp(self):
        mu = 3.9860047e14
        ae = 6.378137e6
        c20 = -1.08263e-3
        c30 = 2.54e-6
        c40 = 1.62e-6
        c50 = 2.3e-7
        c60 = -5.5e-7

        self.mass = 2500.0
        a = 7187990.1979844316
        e = 0.5e-4
        i = 1.7105407051081795
        omega = 1.9674147913622104
        OMEGA = math.radians(261.0)
        lv = 0.0

        date = AbsoluteDate(DateComponents(2004, 1, 1),
                            TimeComponents.H00,
                            TimeScalesFactory.getUTC())
        frame = FramesFactory.getEME2000()
        self.orbit = KeplerianOrbit(a, e, i, omega, OMEGA, lv,
                                    PositionAngleType.TRUE, frame, date, mu)
        earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                 Constants.WGS84_EARTH_FLATTENING,
                                 FramesFactory.getITRF(IERSConventions.IERS_2010, True))

        self.absPV = AbsolutePVCoordinates(frame, date, self.orbit.getPVCoordinates())

        self.attitudeLaw = BodyCenterPointing(self.orbit.getFrame(), earth)
        self.orbitPropagator = EcksteinHechlerPropagator(self.orbit, self.attitudeLaw, self.mass,
                                                         ae, mu, c20, c30, c40, c50, c60)

        self.absPVPropagator = self._set_up_numerical_propagator()

    def tearDown(self):
        self.mass = None
        self.orbit = None
        self.attitudeLaw = None

    def _set_up_numerical_propagator(self):
        integrator = self._set_up_integrator()
        propagator = NumericalPropagator(integrator)

        propagator.setOrbitType(None)

        itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, True)
        provider = GravityFieldFactory.getNormalizedProvider(6, 6)
        potential = HolmesFeatherstoneAttractionModel(itrf, provider)

        propagator.addForceModel(potential)
        propagator.addForceModel(SingleBodyAbsoluteAttraction(CelestialBodyFactory.getEarth()))

        propagator.setInitialState(SpacecraftState(self.absPV))
        propagator.setAttitudeProvider(self.attitudeLaw)
        return propagator

    def _set_up_integrator(self):
        dP = 1.0
        minStep = 0.001
        maxStep = 100.0
        tolerances = NumericalPropagator.tolerances(dP, self.absPV)
        # JCC wraps double[][] as JArray_object; indexing returns a generic
        # Object that the integrator constructor doesn't accept as double[].
        # Cast each row back to double[].
        absTol = JArray('double').cast_(tolerances[0])
        relTol = JArray('double').cast_(tolerances[1])
        return DormandPrince853Integrator(minStep, maxStep, absTol, relTol)

    @staticmethod
    def _add_quadratic(state, dt):
        # JCC: addAdditionalData expects a Java Object; pass an explicit
        # double[] so getAdditionalState(...) returns the same double[].
        # addAdditionalStateDerivative is double... varargs; pass a
        # double[] to satisfy the varargs signature.
        return state.addAdditionalData("quadratic",
                                       JArray_double([dt * dt])) \
                    .addAdditionalStateDerivative("quadratic-dot",
                                                  JArray_double([dt * dt]))

    def _check_abspv_interpolation_error(self, n, expectedErrorP, expectedErrorV,
                                         expectedErrorA, expectedErrorM, interpolator):
        centerDate = self.absPV.getDate().shiftedBy(100.0)
        sample = ArrayList()
        for i in range(n):
            dt = i * 900.0 / (n - 1)
            state = self.absPVPropagator.propagate(centerDate.shiftedBy(dt))
            sample.add(self._add_quadratic(state, dt))

        maxErrorP = 0.0
        maxErrorV = 0.0
        maxErrorA = 0.0
        maxErrorM = 0.0
        dt = 0.0
        while dt < 900.0:
            interpolated = interpolator.interpolate(centerDate.shiftedBy(dt), sample)
            propagated = self.absPVPropagator.propagate(centerDate.shiftedBy(dt))
            dpv = PVCoordinates(propagated.getPVCoordinates(), interpolated.getPVCoordinates())
            maxErrorP = max(maxErrorP, dpv.getPosition().getNorm())
            maxErrorV = max(maxErrorV, dpv.getVelocity().getNorm())
            maxErrorA = max(maxErrorA, math.degrees(Rotation.distance(
                interpolated.getAttitude().getRotation(),
                propagated.getAttitude().getRotation())))
            maxErrorM = max(maxErrorM, abs(interpolated.getMass() - propagated.getMass()))
            dt += 5.0

        self.assertTrue(math.isclose(expectedErrorP, maxErrorP, abs_tol=1e-1),
                        f"P: expected {expectedErrorP}, got {maxErrorP}")
        self.assertTrue(math.isclose(expectedErrorV, maxErrorV, abs_tol=1e-1),
                        f"V: expected {expectedErrorV}, got {maxErrorV}")
        self.assertTrue(math.isclose(expectedErrorA, maxErrorA, abs_tol=1e-1),
                        f"A: expected {expectedErrorA}, got {maxErrorA}")
        self.assertTrue(math.isclose(expectedErrorM, maxErrorM, abs_tol=1e-1),
                        f"M: expected {expectedErrorM}, got {maxErrorM}")

    def _check_orbit_interpolation_error(self, n, expectedErrorP, expectedErrorV,
                                          expectedErrorA, expectedErrorM,
                                          expectedErrorQ, expectedErrorD, interpolator):
        centerDate = self.orbit.getDate().shiftedBy(100.0)
        sample = ArrayList()
        for i in range(n):
            dt = i * 900.0 / (n - 1)
            state = self.orbitPropagator.propagate(centerDate.shiftedBy(dt))
            sample.add(self._add_quadratic(state, dt))

        maxErrorP = 0.0
        maxErrorV = 0.0
        maxErrorA = 0.0
        maxErrorM = 0.0
        maxErrorQ = 0.0
        maxErrorD = 0.0
        dt = 0.0
        while dt < 900.0:
            interpolated = interpolator.interpolate(centerDate.shiftedBy(dt), sample)
            propagated = self.orbitPropagator.propagate(centerDate.shiftedBy(dt))
            dpv = PVCoordinates(propagated.getPVCoordinates(), interpolated.getPVCoordinates())
            maxErrorP = max(maxErrorP, dpv.getPosition().getNorm())
            maxErrorV = max(maxErrorV, dpv.getVelocity().getNorm())
            maxErrorA = max(maxErrorA, math.degrees(Rotation.distance(
                interpolated.getAttitude().getRotation(),
                propagated.getAttitude().getRotation())))
            maxErrorM = max(maxErrorM, abs(interpolated.getMass() - propagated.getMass()))
            maxErrorQ = max(maxErrorQ, abs(interpolated.getAdditionalState("quadratic")[0] - dt * dt))
            maxErrorD = max(maxErrorD, abs(interpolated.getAdditionalStateDerivative("quadratic-dot")[0] - dt * dt))
            dt += 5.0

        self.assertTrue(math.isclose(expectedErrorP, maxErrorP, abs_tol=1e-1))
        self.assertTrue(math.isclose(expectedErrorV, maxErrorV, abs_tol=1e-1))
        self.assertTrue(math.isclose(expectedErrorA, maxErrorA, abs_tol=1e-1))
        self.assertTrue(math.isclose(expectedErrorM, maxErrorM, abs_tol=1e-1))
        self.assertTrue(math.isclose(expectedErrorQ, maxErrorQ, abs_tol=1e-1))
        self.assertTrue(math.isclose(expectedErrorD, maxErrorD, abs_tol=1e-1))

    def testOrbitInterpolation(self):
        interpolationPoints1 = 2
        interpolationPoints2 = 3
        interpolationPoints3 = 4

        inertialFrame = FramesFactory.getEME2000()

        interpolator1 = SpacecraftStateInterpolator(interpolationPoints1, inertialFrame, inertialFrame)
        interpolator2 = SpacecraftStateInterpolator(interpolationPoints2, inertialFrame, inertialFrame)
        interpolator3 = SpacecraftStateInterpolator(interpolationPoints3, inertialFrame, inertialFrame)

        self._check_orbit_interpolation_error(interpolationPoints1, 106.46533, 0.40709287,
                                               169847806.33e-9, 0.0, 450 * 450, 450 * 450,
                                               interpolator1)
        self._check_orbit_interpolation_error(interpolationPoints3, 0.00002, 0.00000023, 232.25e-9,
                                               0.0, 0.0, 0.0, interpolator3)
        self._check_orbit_interpolation_error(interpolationPoints2, 0.00353, 0.00003250, 189886.01e-9,
                                               0.0, 0.0, 0.0, interpolator2)

    def _build_all_type_of_interpolator(self, interpolation_points, inertial_frame):
        pva_filters = list(CartesianDerivativesFilter.values())
        angular_filters = list(AngularDerivativesFilter.values())

        dim = len(pva_filters)
        interpolators = []
        for i in range(dim):
            interpolator = SpacecraftStateInterpolator(
                interpolation_points,
                AbstractTimeInterpolator.DEFAULT_EXTRAPOLATION_THRESHOLD_SEC,
                inertial_frame, inertial_frame,
                pva_filters[i], angular_filters[i])
            interpolators.append(interpolator)
        return interpolators

    def testAbsPVAInterpolation(self):
        interpolationPoints1 = 2
        interpolationPoints2 = 3
        interpolationPoints3 = 4

        inertialFrame = self.absPV.getFrame()

        interpolator1 = self._build_all_type_of_interpolator(interpolationPoints1, inertialFrame)
        interpolator2 = self._build_all_type_of_interpolator(interpolationPoints2, inertialFrame)
        interpolator3 = self._build_all_type_of_interpolator(interpolationPoints3, inertialFrame)

        # P and R
        self._check_abspv_interpolation_error(interpolationPoints1, 766704.6033758943, 3385.895505018284,
                                              9.503905101141868, 0.0, interpolator1[0])
        self._check_abspv_interpolation_error(interpolationPoints2, 46190.78568215623, 531.3506621730367,
                                              0.5601906427491941, 0.0, interpolator2[0])
        self._check_abspv_interpolation_error(interpolationPoints3, 2787.7069621834926, 55.5146607205871,
                                              0.03372344505743245, 0.0, interpolator3[0])

        # PV and RR
        self._check_abspv_interpolation_error(interpolationPoints1, 14023.999059896296, 48.022197580401084,
                                              0.16984517369482555, 0.0, interpolator1[1])
        self._check_abspv_interpolation_error(interpolationPoints2, 16.186825338590722, 0.13418685366189476,
                                              1.898961129289559e-4, 0.0, interpolator2[1])
        self._check_abspv_interpolation_error(interpolationPoints3, 0.025110113133073413, 3.5069332429486154e-4,
                                              2.3306042475258594e-7, 0.0, interpolator3[1])

        # PVA and RRR
        self._check_abspv_interpolation_error(interpolationPoints1, 108.13907262943746, 0.4134494277844817,
                                              0.001389170843175492, 0.0, interpolator1[2])
        self._check_abspv_interpolation_error(interpolationPoints2, 0.002974408269435121, 2.6937387601886076e-5,
                                              2.051629855188969e-4, 0.0, interpolator2[2])
        self._check_abspv_interpolation_error(interpolationPoints3, 0.0, 0.0,
                                              1.3779131041190534e-4, 0.0, interpolator3[2])


if __name__ == '__main__':
    unittest.main()
