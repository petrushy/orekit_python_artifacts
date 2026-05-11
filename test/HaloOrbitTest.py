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

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_data
# Mirrors Java's Utils.setDataRoot("cr3bp:regular-data")
setup_orekit_data(filenames=["resources/cr3bp", "resources/regular-data"],
                  from_pip_library=False)

from orekit import JArray_double, JavaError

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.bodies import CR3BPFactory
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.propagation.numerical.cr3bp import CR3BPForceModel, STMEquations
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import AbsolutePVCoordinates, LagrangianPoints, PVCoordinates
from org.orekit.orbits import (CR3BPDifferentialCorrection, HaloOrbit,
                               LibrationOrbitFamily, LibrationOrbitType,
                               RichardsonExpansion)


class HaloOrbitTest(unittest.TestCase):

    def test_halo_orbit(self):
        syst = CR3BPFactory.getEarthMoonCR3BP()
        firstGuess = PVCoordinates(
            Vector3D(0.0, 1.0, 2.0),
            Vector3D(3.0, 4.0, 5.0),
        )

        h1 = HaloOrbit(RichardsonExpansion(syst, LagrangianPoints.L1), 8.0e6, LibrationOrbitFamily.NORTHERN)
        h2 = HaloOrbit(syst, firstGuess, 2.0)
        h3 = HaloOrbit(RichardsonExpansion(syst, LagrangianPoints.L2), 8.0e6, LibrationOrbitFamily.SOUTHERN)

        orbitalPeriod1 = h1.getOrbitalPeriod()
        orbitalPeriod2 = h2.getOrbitalPeriod()
        orbitalPeriod3 = h3.getOrbitalPeriod()

        self.assertNotAlmostEqual(0.0, orbitalPeriod1, delta=0.5)
        self.assertNotAlmostEqual(0.0, orbitalPeriod3, delta=0.5)
        self.assertAlmostEqual(2.0, orbitalPeriod2, places=15)

        firstGuess1 = h1.getInitialPV()
        firstGuess2 = h2.getInitialPV()
        firstGuess3 = h3.getInitialPV()

        self.assertNotAlmostEqual(0.0, firstGuess1.getPosition().getX(), delta=0.6)
        self.assertAlmostEqual(0.0, firstGuess1.getPosition().getY(), places=15)
        self.assertAlmostEqual(0.0, firstGuess1.getVelocity().getX(), places=15)
        self.assertNotAlmostEqual(0.0, firstGuess1.getVelocity().getY(), delta=0.01)
        self.assertAlmostEqual(0.0, firstGuess1.getVelocity().getZ(), places=15)

        self.assertNotAlmostEqual(0.0, firstGuess3.getPosition().getX(), delta=1)
        self.assertAlmostEqual(0.0, firstGuess3.getPosition().getY(), places=15)
        self.assertAlmostEqual(0.0, firstGuess3.getVelocity().getX(), places=15)
        self.assertNotAlmostEqual(0.0, firstGuess3.getVelocity().getY(), delta=0.01)
        self.assertAlmostEqual(0.0, firstGuess3.getVelocity().getZ(), places=15)

        self.assertAlmostEqual(firstGuess.getPosition().getX(), firstGuess2.getPosition().getX(), places=15)
        self.assertAlmostEqual(firstGuess.getPosition().getY(), firstGuess2.getPosition().getY(), places=15)
        self.assertAlmostEqual(firstGuess.getPosition().getZ(), firstGuess2.getPosition().getZ(), places=15)
        self.assertAlmostEqual(firstGuess.getVelocity().getX(), firstGuess2.getVelocity().getX(), places=15)
        self.assertAlmostEqual(firstGuess.getVelocity().getY(), firstGuess2.getVelocity().getY(), places=15)
        self.assertAlmostEqual(firstGuess.getVelocity().getZ(), firstGuess2.getVelocity().getZ(), places=15)

    def test_lagrangian_error(self):
        with self.assertRaises(JavaError):
            syst = CR3BPFactory.getEarthMoonCR3BP()
            HaloOrbit(RichardsonExpansion(syst, LagrangianPoints.L3), 8.0e6, LibrationOrbitFamily.NORTHERN)

    def test_manifolds(self):
        initialDate = AbsoluteDate(1996, 6, 25, 0, 0, 0.0, TimeScalesFactory.getUTC())
        syst = CR3BPFactory.getEarthMoonCR3BP()

        syst.getPrimary().getPVCoordinates(initialDate, syst.getSecondary().getInertiallyOrientedFrame())

        frame = syst.getRotatingFrame()

        h = HaloOrbit(RichardsonExpansion(syst, LagrangianPoints.L1), 8.0e6, LibrationOrbitFamily.SOUTHERN)
        orbitalPeriod = h.getOrbitalPeriod()
        integrationTime = orbitalPeriod * 0.9

        firstGuess = h.getInitialPV()

        initialConditions = CR3BPDifferentialCorrection(firstGuess, syst, orbitalPeriod) \
            .compute(LibrationOrbitType.HALO)

        initialAbsPV = AbsolutePVCoordinates(frame, initialDate, initialConditions)
        initialState = SpacecraftState(initialAbsPV)

        minStep = 1.0e-10
        maxStep = 1.0e-2
        positionTolerance = 1.0e-4
        velocityTolerance = 1.0e-4
        massTolerance = 1.0e-6
        # JCC needs an explicit Java double[]; jpype auto-converts a Python list.
        vecAbsoluteTolerances = JArray_double([positionTolerance, positionTolerance, positionTolerance,
                                               velocityTolerance, velocityTolerance, velocityTolerance,
                                               massTolerance])
        vecRelativeTolerances = JArray_double([0.0] * 7)

        integrator = DormandPrince853Integrator(minStep, maxStep,
                                                vecAbsoluteTolerances, vecRelativeTolerances)

        stm = STMEquations(syst)
        augmentedInitialState = stm.setInitialPhi(initialState)
        propagator = NumericalPropagator(integrator)
        propagator.setOrbitType(None)
        propagator.setIgnoreCentralAttraction(True)
        propagator.addForceModel(CR3BPForceModel(syst))
        propagator.addAdditionalDerivativesProvider(stm)
        propagator.setInitialState(augmentedInitialState)

        finalState = propagator.propagate(initialDate.shiftedBy(integrationTime))

        initialUnstableManifold = h.getManifolds(finalState, False)
        initialStableManifold = h.getManifolds(finalState, True)

        self.assertNotEqual(finalState.getPosition().getX(), initialUnstableManifold.getPosition().getX())
        self.assertNotEqual(finalState.getPosition().getY(), initialUnstableManifold.getPosition().getY())
        self.assertNotEqual(finalState.getPosition().getZ(), initialUnstableManifold.getPosition().getZ())

        self.assertNotEqual(finalState.getPosition().getX(), initialStableManifold.getPosition().getX())
        self.assertNotEqual(finalState.getPosition().getY(), initialStableManifold.getPosition().getY())
        self.assertNotEqual(finalState.getPosition().getZ(), initialStableManifold.getPosition().getZ())

    def test_differential_correction_error(self):
        with self.assertRaises(JavaError):
            syst = CR3BPFactory.getEarthMoonCR3BP()
            orbitalPeriod = 1.0
            firstGuess = PVCoordinates(Vector3D(0.0, 1.0, 2.0), Vector3D(3.0, 4.0, 5.0))
            CR3BPDifferentialCorrection(firstGuess, syst, orbitalPeriod).compute(LibrationOrbitType.HALO)

    def test_stm_error(self):
        with self.assertRaises(JavaError):
            initialDate = AbsoluteDate(1996, 6, 25, 0, 0, 0.0, TimeScalesFactory.getUTC())
            syst = CR3BPFactory.getEarthMoonCR3BP()
            frame = syst.getRotatingFrame()

            h = HaloOrbit(RichardsonExpansion(syst, LagrangianPoints.L1), 8.0e6, LibrationOrbitFamily.SOUTHERN)
            pv = PVCoordinates(Vector3D(0.0, 1.0, 2.0), Vector3D(3.0, 4.0, 5.0))

            initialAbsPV = AbsolutePVCoordinates(frame, initialDate, pv)
            s = SpacecraftState(initialAbsPV)

            manifold = h.getManifolds(s, True)
            manifold.getMomentum()


if __name__ == '__main__':
    unittest.main()
