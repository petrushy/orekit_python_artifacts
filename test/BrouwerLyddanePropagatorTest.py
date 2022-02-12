# -*- coding: utf-8 -*-

"""

Python version translated from Java orekit 11.1 by Petrus Hyvönen, SSC 2022

 """

import  orekit
orekit.initVM()
from orekit.pyhelpers import  setup_orekit_curdir

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import GeodeticPoint
from org.orekit.bodies import OneAxisEllipsoid
from org.orekit.frames import TopocentricFrame
from org.orekit.orbits import KeplerianOrbit
from org.orekit.frames import FramesFactory
from org.orekit.orbits import PositionAngle, EquinoctialOrbit
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.propagation.events.handlers import EventHandler, PythonEventHandler
from org.orekit.time import AbsoluteDate
from org.orekit.time import TimeScalesFactory
from org.orekit.utils import Constants
from org.orekit.utils import IERSConventions, PVCoordinates
from org.orekit.propagation.events import ElevationDetector
from org.hipparchus.ode.events import Action
from org.orekit.forces.gravity.potential import GravityFieldFactory
from org.orekit.propagation.analytical import BrouwerLyddanePropagator

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
        self.assertAlmostEquals(0.0, finalOrbit.getA() - initialOrbit.getA(), 0.0)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BrouwerLyddanePropagatorTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)

