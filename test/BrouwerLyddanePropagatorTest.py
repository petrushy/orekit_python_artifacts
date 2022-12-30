# -*- coding: utf-8 -*-

"""

Python version translated from Java orekit 11.1 by Petrus Hyvönen, SSC 2022

 """

import  orekit
orekit.initVM()
from orekit.pyhelpers import  setup_orekit_curdir

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.bodies import GeodeticPoint
from org.orekit.bodies import OneAxisEllipsoid
from org.orekit.frames import TopocentricFrame
from org.orekit.orbits import KeplerianOrbit
from org.orekit.frames import FramesFactory
from org.orekit.orbits import PositionAngle, EquinoctialOrbit, OrbitType
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.propagation.events.handlers import EventHandler, PythonEventHandler
from org.orekit.time import AbsoluteDate
from org.orekit.time import TimeScalesFactory
from org.orekit.utils import Constants
from org.orekit.utils import IERSConventions, PVCoordinates
from org.orekit.propagation.events import ElevationDetector
from org.hipparchus.ode.events import Action
from org.orekit.forces.gravity.potential import GravityFieldFactory
from org.orekit.forces.gravity import HolmesFeatherstoneAttractionModel
from org.orekit.propagation.analytical import BrouwerLyddanePropagator
from org.hipparchus.util import FastMath, MathUtils

from orekit import JArray_double

import unittest
import sys
import math


class BrouwerLyddanePropagatorTest(unittest.TestCase):

    def setUp(self):
        setup_orekit_curdir("resources")
        self.provider = GravityFieldFactory.getNormalizedProvider(5, 0)

    def test_sameDateCartesian(self):
        # Definition of initial conditions with position and velocity
        #  ------------------------------------------------------------
        #  e = 0.04152500499523033 and i = 1.705015527659039

        initDate = AbsoluteDate.J2000_EPOCH.shiftedBy(584.)
        position = Vector3D(3220103., 69623., 6149822.)
        velocity = Vector3D(6414.7, -2006., -3180.)

        initialOrbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                        FramesFactory.getEME2000(), initDate, self.provider.getMu())

        # Extrapolation at the initial date
        # ---------------------------------
        extrapolator = BrouwerLyddanePropagator(initialOrbit, GravityFieldFactory.getUnnormalizedProvider(self.provider),
                                                BrouwerLyddanePropagator.M2)

        finalOrbit = extrapolator.propagate(initDate)

        # positions  velocity and semi major axis match perfectly
        self.assertAlmostEquals(0.0, Vector3D.distance(initialOrbit.getPVCoordinates().getPosition(),
                                                       finalOrbit.getPVCoordinates().getPosition()), delta=1.0e-8)

        self.assertAlmostEquals(0.0, Vector3D.distance(initialOrbit.getPVCoordinates().getVelocity(),
                                                       finalOrbit.getPVCoordinates().getVelocity()), delta= 1.0e-11)
        self.assertAlmostEquals(0.0, finalOrbit.getA() - initialOrbit.getA(), delta=0.0)

    def test_compareToNumericalPropagation(self):

        inertialFrame = FramesFactory.getEME2000()
        initDate = AbsoluteDate.J2000_EPOCH.shiftedBy(584.)
        timeshift = 60000.0 

        # Initial orbit
        a = 24396159.0 # semi major axis in meters
        e = 0.01 # eccentricity
        i = FastMath.toRadians(7.0) # inclination
        omega = FastMath.toRadians(180.0)  # perigee argument
        raan = FastMath.toRadians(261.0)  # right ascention of ascending node
        lM = 0.0 # mean anomaly
        initialOrbit =  KeplerianOrbit(a, e, i, omega, raan, lM, PositionAngle.TRUE,
                                       inertialFrame, initDate, self.provider.getMu())
        # Initial state definition
        initialState =  SpacecraftState(initialOrbit)

        #_______________________________________________________________________________________________
        # SET UP A REFERENCE NUMERICAL PROPAGATION
        #_______________________________________________________________________________________________

        # Adaptive step integrator with a minimum step of 0.001 and a maximum step of 1000
        minStep = 0.001
        maxstep = 1000.0
        positionTolerance = 10.0
        propagationType = OrbitType.KEPLERIAN
        tolerances = NumericalPropagator.tolerances(positionTolerance, initialOrbit, propagationType)
        integrator = DormandPrince853Integrator(minStep, maxstep,
                                                JArray_double.cast_(tolerances[0]),
                                                JArray_double.cast_(tolerances[1]))

        # Numerical Propagator
        NumPropagator = NumericalPropagator(integrator)
        NumPropagator.setOrbitType(propagationType)

        holmesFeatherstone = HolmesFeatherstoneAttractionModel(FramesFactory.getITRF(IERSConventions.IERS_2010, True), self.provider)
        NumPropagator.addForceModel(holmesFeatherstone)

        # Set up initial state in the propagator
        NumPropagator.setInitialState(initialState)

        # Extrapolate from the initial to the  date
        NumFinalState = NumPropagator.propagate(initDate.shiftedBy(timeshift))
        NumOrbit = KeplerianOrbit.cast_(OrbitType.KEPLERIAN.convertType(NumFinalState.getOrbit()))

        #_______________________________________________________________________________________________
        # SET UP A BROUWER LYDDANE PROPAGATION
        #_______________________________________________________________________________________________

        BLextrapolator = BrouwerLyddanePropagator(initialOrbit, GravityFieldFactory.getUnnormalizedProvider(self.provider),
                                                  BrouwerLyddanePropagator.M2)

        BLFinalState = BLextrapolator.propagate(initDate.shiftedBy(timeshift))
        BLOrbit = KeplerianOrbit.cast_(OrbitType.KEPLERIAN.convertType(BLFinalState.getOrbit()))

        self.assertAlmostEquals(NumOrbit.getA(), BLOrbit.getA(), delta=0.2)
        self.assertAlmostEquals(NumOrbit.getE(), BLOrbit.getE(), delta=0.00000028)
        self.assertAlmostEquals(NumOrbit.getI(), BLOrbit.getI(), delta=0.000004)
        self.assertAlmostEquals(MathUtils.normalizeAngle(NumOrbit.getPerigeeArgument(), FastMath.PI),
                                MathUtils.normalizeAngle(BLOrbit.getPerigeeArgument(), FastMath.PI), delta=0.119)
        self.assertAlmostEquals(MathUtils.normalizeAngle(NumOrbit.getRightAscensionOfAscendingNode(), FastMath.PI),
                                MathUtils.normalizeAngle(BLOrbit.getRightAscensionOfAscendingNode(), FastMath.PI), delta=0.000072)
        self.assertAlmostEquals(MathUtils.normalizeAngle(NumOrbit.getTrueAnomaly(), FastMath.PI),
                                MathUtils.normalizeAngle(BLOrbit.getTrueAnomaly(), FastMath.PI), delta=0.12)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BrouwerLyddanePropagatorTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)

