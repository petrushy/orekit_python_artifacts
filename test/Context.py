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



from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from orekit import JArray_double
from org.orekit.data import DataProvidersManager, ZipJarCrawler
from org.orekit.forces.gravity.potential import GravityFieldFactory
from org.orekit.forces.gravity.potential import SHMFormatReader
from java.io import File


from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator

from org.orekit.frames import FramesFactory
from org.orekit.orbits import EquinoctialOrbit, PositionAngleType
from org.orekit.orbits import OrbitType
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.propagation.semianalytical.dsst import DSSTPropagator
from org.orekit.time import AbsoluteDate
from org.orekit.utils import PVCoordinates

from org.orekit.data import DataProvidersManager, ZipJarCrawler
from java.io import File

from org.hipparchus.geometry.euclidean.threed import Rotation
from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.util import FastMath

from org.orekit.bodies import CelestialBodyFactory

from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit


# import java.util.List;
# import java.util.Map;
#
# import org.hipparchus.geometry.euclidean.threed.Vector3D;
# import org.hipparchus.util.FastMath;
# import org.orekit.bodies.CelestialBody;
from org.orekit.bodies import GeodeticPoint
# import org.orekit.bodies.OneAxisEllipsoid;
from org.orekit.estimation.measurements import GroundStation
# import org.orekit.forces.drag.DragSensitive;
# import org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider;
# import org.orekit.forces.radiation.RadiationSensitive;
from org.orekit.frames import TopocentricFrame
# import org.orekit.models.earth.displacement.StationDisplacement;
from org.orekit.orbits import CartesianOrbit
# import org.orekit.orbits.Orbit;
# import org.orekit.orbits.OrbitType;
# import org.orekit.orbits.PositionAngleType;
from org.orekit.propagation.conversion import DormandPrince853IntegratorBuilder
from org.orekit.propagation.conversion import NumericalPropagatorBuilder
# import org.orekit.time.TimeScale;
# import org.orekit.time.UT1Scale;
from org.orekit.utils import IERSConventions
from org.orekit.utils import PVCoordinates

class Context():


    # public class Context {
    # public IERSConventions                      conventions;
    # public OneAxisEllipsoid                     earth;
    # public CelestialBody                        sun;
    # public CelestialBody                        moon;
    # public RadiationSensitive                   radiationSensitive;
    # public DragSensitive                        dragSensitive;
    # public NormalizedSphericalHarmonicsProvider gravity;
    # public TimeScale                            utc;
    # public UT1Scale                             ut1;
    # public Orbit                                initialOrbit;
    # public StationDisplacement[]                displacements;
    # public List<GroundStation>                  stations;
    # // Stations for turn-around range
    # // Map entry = master station
    # // Map value = slave station associated
    # public Map<GroundStation, GroundStation>     TARstations;

    def createBuilder(self, orbitType, positionAngle: PositionAngleType, perfectStart, minStep, maxStep, dP, *forces):

        if perfectStart:
            # orbit estimation will start from a perfect orbit
            startOrbit = self.initialOrbit
        else:
            # orbit estimation will start from a wrong point
            initialPosition = self.initialOrbit.getPVCoordinates().getPosition()
            initialVelocity = self.initialOrbit.getPVCoordinates().getVelocity()
            wrongPosition   = self.initialPosition.add(Vector3D(1000.0, 0.0, 0.0))
            wrongVelocity   = initialVelocity.add(Vector3D(0.0, 0.0, 0.01))
            startOrbit  = CartesianOrbit(PVCoordinates(wrongPosition, wrongVelocity),
                                                                self.initialOrbit.getFrame(),
                                                                self.initialOrbit.getDate(),
                                                                self.initialOrbit.getMu())
        propagatorBuilder = NumericalPropagatorBuilder(orbitType.convertType(startOrbit),
                                                    DormandPrince853IntegratorBuilder(minStep, maxStep, dP),
                                                    positionAngle, dP)

        for force in forces:
            propagatorBuilder.addForceModel(force.getForceModel(self)) # self??

        return propagatorBuilder


    def createStation(self, latitudeInDegrees, longitudeInDegrees, altitude, name):
        gp = GeodeticPoint(FastMath.toRadians(latitudeInDegrees),
                                                   FastMath.toRadians(longitudeInDegrees),
                                                   altitude)
        return GroundStation(TopocentricFrame(self.earth, gp, name),
                                 self.ut1.getEOPHistory(), self.displacements)



