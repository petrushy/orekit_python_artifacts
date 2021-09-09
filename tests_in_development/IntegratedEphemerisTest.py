# -*- coding: utf-8 -*-

"""

/* Copyright 2002-2013 CS Syst��mes d'Information
 * Licensed to CS Syst��mes d'Information (CS) under one or more
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

import orekit

orekit.initVM()
# from orekit.pyhelpers import  setup_orekit_curdir
from orekit import JArray_double
from orekit.pyhelpers import JArray_double2D

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.hipparchus.linear import Array2DRowRealMatrix
from org.hipparchus.linear import MatrixUtils
# import org.hipparchus.linear.RealMatrix;
# import org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator;
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
# import org.junit.Assert;
# import org.junit.Before;
# import org.junit.Test;
# import org.orekit.Utils;
# import org.orekit.bodies.CelestialBody;
# import org.orekit.bodies.CelestialBodyFactory;
# import org.orekit.errors.OrekitException;
# import org.orekit.forces.gravity.HolmesFeatherstoneAttractionModel;
# import org.orekit.forces.gravity.ThirdBodyAttraction;
# import org.orekit.forces.gravity.potential.GravityFieldFactory;
# import org.orekit.forces.gravity.potential.ICGEMFormatReader;
# import org.orekit.forces.gravity.potential.NormalizedSphericalHarmonicsProvider;
# import org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider;
# import org.orekit.forces.radiation.IsotropicRadiationSingleCoefficient;
# import org.orekit.forces.radiation.RadiationSensitive;
# import org.orekit.forces.radiation.SolarRadiationPressure;
# import org.orekit.frames.Frame;
from org.orekit.frames import FramesFactory
# import org.orekit.orbits.EquinoctialOrbit;
from org.orekit.orbits import EquinoctialOrbit

# import org.orekit.orbits.Orbit;
from org.orekit.orbits import OrbitType
# import org.orekit.propagation.BoundedPropagator;
from org.orekit.propagation import SpacecraftState
from org.orekit.propagation.analytical import KeplerianPropagator
# import org.orekit.propagation.numerical.JacobiansMapper;
from org.orekit.propagation.numerical import NumericalPropagator
from org.orekit.propagation.numerical import PartialDerivativesEquations
# import org.orekit.propagation.sampling.OrekitStepHandler;
# import org.orekit.propagation.sampling.OrekitStepInterpolator;
# import org.orekit.propagation.semianalytical.dsst.DSSTPropagator;
# import org.orekit.propagation.semianalytical.dsst.forces.DSSTSolarRadiationPressure;
# import org.orekit.propagation.semianalytical.dsst.forces.DSSTTesseral;
# import org.orekit.propagation.semianalytical.dsst.forces.DSSTThirdBody;
# import org.orekit.propagation.semianalytical.dsst.forces.DSSTZonal;
from org.orekit.time import AbsoluteDate
# import org.orekit.utils.Constants;
from org.orekit.utils import Constants
# import org.orekit.utils.IERSConventions;
# import org.orekit.utils.PVCoordinates;
from org.orekit.data import DataProvidersManager, ZipJarCrawler, DataContext
from java.io import File
from java.lang import System
from org.orekit.python import PythonOrekitStepHandler

from org.orekit.utils import PVCoordinates

import unittest


class IntegratedEphemerisTest(unittest.TestCase):

    def testNormalKeplerIntegration(self):
        # Keplerian propagator definition
        keplerEx = KeplerianPropagator(self.initialOrbit)

        # Integrated ephemeris

        # Propagation

        finalDate = self.initialOrbit.getDate().shiftedBy(Constants.JULIAN_DAY)
        self.numericalPropagator.setEphemerisMode()
        self.numericalPropagator.setInitialState(SpacecraftState(self.initialOrbit))
        self.numericalPropagator.propagate(finalDate)

        # Check the number of calls to the differential equations computation method.
        self.assertTrue(self.numericalPropagator.getCalls() < 3200)
        ephemeris = self.numericalPropagator.getGeneratedEphemeris()

        # tests
        i = 1
        while i <= Constants.JULIAN_DAY:
            intermediateDate = self.initialOrbit.getDate().shiftedBy(float(i))
            keplerIntermediateOrbit = keplerEx.propagate(intermediateDate)
            numericIntermediateOrbit = ephemeris.propagate(intermediateDate)
            kepPosition = keplerIntermediateOrbit.getPVCoordinates().getPosition()
            numPosition = numericIntermediateOrbit.getPVCoordinates().getPosition()
            self.assertAlmostEqual(0, kepPosition.subtract(numPosition).getNorm(), delta=0.06)
            i += 1

        intermediateDate = self.initialOrbit.getDate().shiftedBy(41589.0)
        keplerIntermediateOrbit = keplerEx.propagate(intermediateDate)
        state = keplerEx.propagate(finalDate)
        self.numericalPropagator.setInitialState(state)
        self.numericalPropagator.setEphemerisMode()
        self.numericalPropagator.propagate(self.initialOrbit.getDate())
        invEphemeris = self.numericalPropagator.getGeneratedEphemeris()
        numericIntermediateOrbit = invEphemeris.propagate(intermediateDate)
        kepPosition = keplerIntermediateOrbit.getPVCoordinates().getPosition()
        numPosition = numericIntermediateOrbit.getPVCoordinates().getPosition()
        self.assertAlmostEqual(0, kepPosition.subtract(numPosition).getNorm(), delta=10e-2)

    def testPartialDerivativesIssue16(self):

        eqName = "derivatives"
        self.numericalPropagator.setEphemerisMode()
        self.numericalPropagator.setOrbitType(OrbitType.CARTESIAN)
        derivatives = PartialDerivativesEquations(eqName, self.numericalPropagator)
        initialState = derivatives.setInitialJacobians(SpacecraftState(self.initialOrbit))
        mapper = derivatives.getMapper()
        self.numericalPropagator.setInitialState(initialState)
        self.numericalPropagator.propagate(self.initialOrbit.getDate().shiftedBy(3600.0))
        ephemeris = self.numericalPropagator.getGeneratedEphemeris()

        class myStepHandler(PythonOrekitStepHandler):
            dYdY0 = Array2DRowRealMatrix(6, 6)

            def init(self, s0, t):
                pass

            def handleStep(self, interpolator, isLast):
                state = interpolator.getCurrentState()
                assert mapper.getAdditionalStateDimension() == len(state.getAdditionalState(eqName))
                mapper.getStateJacobian(state, self.dYdY0.getDataRef())
                mapper.getParametersJacobian(state,
                                             JArray_double2D(1, 1))  # no parameters, this is a no-op and should work
                deltaId = self.dYdY0.subtract(MatrixUtils.createRealIdentityMatrix(6))
                assert deltaId.getNorm() > 100
                assert deltaId.getNorm() < 3100

        ephemeris.setMasterMode(myStepHandler())
        ephemeris.propagate(self.initialOrbit.getDate().shiftedBy(1800.0))

    # @Test
    # public void testGetFrame() throws OrekitException {
    #     // setup
    #     AbsoluteDate finalDate = initialOrbit.getDate().shiftedBy(Constants.JULIAN_DAY);
    #     numericalPropagator.setEphemerisMode();
    #     numericalPropagator.setInitialState(new SpacecraftState(initialOrbit));
    #     numericalPropagator.propagate(finalDate);
    #     Assert.assertTrue(numericalPropagator.getCalls() < 3200);
    #     BoundedPropagator ephemeris = numericalPropagator.getGeneratedEphemeris();
    #
    #     //action
    #     Assert.assertNotNull(ephemeris.getFrame());
    #     Assert.assertSame(ephemeris.getFrame(), numericalPropagator.getFrame());
    # }
    #
    # @Test
    # public void testSerializationNumerical() throws OrekitException, IOException, ClassNotFoundException {
    #
    #     AbsoluteDate finalDate = initialOrbit.getDate().shiftedBy(Constants.JULIAN_DAY);
    #     numericalPropagator.setEphemerisMode();
    #     numericalPropagator.setInitialState(new SpacecraftState(initialOrbit));
    #
    #     final Frame itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, true);
    #     final NormalizedSphericalHarmonicsProvider gravity =
    #                     GravityFieldFactory.getNormalizedProvider(8, 8);
    #     final CelestialBody sun  = CelestialBodyFactory.getSun();
    #     final CelestialBody moon = CelestialBodyFactory.getMoon();
    #     final RadiationSensitive spacecraft = new IsotropicRadiationSingleCoefficient(20.0, 2.0);
    #     numericalPropagator.addForceModel(new HolmesFeatherstoneAttractionModel(itrf, gravity));
    #     numericalPropagator.addForceModel(new ThirdBodyAttraction(sun));
    #     numericalPropagator.addForceModel(new ThirdBodyAttraction(moon));
    #     numericalPropagator.addForceModel(new SolarRadiationPressure(sun,
    #                                                                  Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
    #                                                                  spacecraft));
    #
    #     numericalPropagator.propagate(finalDate);
    #     IntegratedEphemeris ephemeris = (IntegratedEphemeris) numericalPropagator.getGeneratedEphemeris();
    #
    #     ByteArrayOutputStream bos = new ByteArrayOutputStream();
    #     ObjectOutputStream    oos = new ObjectOutputStream(bos);
    #     oos.writeObject(ephemeris);
    #
    #     int expectedSize = 258223;
    #     Assert.assertTrue("size = " + bos.size (), bos.size () >  9 * expectedSize / 10);
    #     Assert.assertTrue("size = " + bos.size (), bos.size () < 11 * expectedSize / 10);
    #
    #     Assert.assertNotNull(ephemeris.getFrame());
    #     Assert.assertSame(ephemeris.getFrame(), numericalPropagator.getFrame());
    #     ByteArrayInputStream  bis = new ByteArrayInputStream(bos.toByteArray());
    #     ObjectInputStream     ois = new ObjectInputStream(bis);
    #     IntegratedEphemeris deserialized  = (IntegratedEphemeris) ois.readObject();
    #     Assert.assertEquals(deserialized.getMinDate(), deserialized.getMinDate());
    #     Assert.assertEquals(deserialized.getMaxDate(), deserialized.getMaxDate());
    #
    # }
    #
    # @Test
    # public void testSerializationDSSTMean()
    #     throws OrekitException, IOException, ClassNotFoundException {
    #     doTestSerializationDSST(true, 36703);
    # }
    #
    # @Test
    # public void testSerializationDSSTOsculating()
    #     throws OrekitException, IOException, ClassNotFoundException {
    #     doTestSerializationDSST(false, 618025);
    # }
    #
    # private void doTestSerializationDSST(boolean meanOnly, int expectedSize)
    #     throws OrekitException, IOException, ClassNotFoundException {
    #
    #     AbsoluteDate finalDate = initialOrbit.getDate().shiftedBy(Constants.JULIAN_DAY);
    #     final double[][] tol = DSSTPropagator.tolerances(1.0, initialOrbit);
    #     AdaptiveStepsizeIntegrator integrator = new DormandPrince853Integrator(10, Constants.JULIAN_DAY, tol[0], tol[1]);
    #     DSSTPropagator dsstProp = new DSSTPropagator(integrator, meanOnly);
    #     dsstProp.setInitialState(new SpacecraftState(initialOrbit), false);
    #     dsstProp.setEphemerisMode();
    #
    #     final Frame itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, true);
    #     final UnnormalizedSphericalHarmonicsProvider gravity =
    #                     GravityFieldFactory.getUnnormalizedProvider(8, 8);
    #     final CelestialBody sun  = CelestialBodyFactory.getSun();
    #     final CelestialBody moon = CelestialBodyFactory.getMoon();
    #     final RadiationSensitive spacecraft = new IsotropicRadiationSingleCoefficient(20.0, 2.0);
    #     dsstProp.addForceModel(new DSSTZonal(gravity, 8, 7, 17));
    #     dsstProp.addForceModel(new DSSTTesseral(itrf, Constants.WGS84_EARTH_ANGULAR_VELOCITY,
    #                                             gravity, 8, 8, 4, 12, 8, 8, 4));
    #     dsstProp.addForceModel(new DSSTThirdBody(sun));
    #     dsstProp.addForceModel(new DSSTThirdBody(moon));
    #     dsstProp.addForceModel(new DSSTSolarRadiationPressure(sun, Constants.WGS84_EARTH_EQUATORIAL_RADIUS, spacecraft));
    #
    #     dsstProp.propagate(finalDate);
    #     IntegratedEphemeris ephemeris = (IntegratedEphemeris) dsstProp.getGeneratedEphemeris();
    #
    #     ByteArrayOutputStream bos = new ByteArrayOutputStream();
    #     ObjectOutputStream    oos = new ObjectOutputStream(bos);
    #     oos.writeObject(ephemeris);
    #
    #     Assert.assertTrue("size = " + bos.size (), bos.size () >  9 * expectedSize / 10);
    #     Assert.assertTrue("size = " + bos.size (), bos.size () < 11 * expectedSize / 10);
    #
    #
    #     Assert.assertNotNull(ephemeris.getFrame());
    #     Assert.assertSame(ephemeris.getFrame(), dsstProp.getFrame());
    #     ByteArrayInputStream  bis = new ByteArrayInputStream(bos.toByteArray());
    #     ObjectInputStream     ois = new ObjectInputStream(bis);
    #     IntegratedEphemeris deserialized  = (IntegratedEphemeris) ois.readObject();
    #     Assert.assertEquals(deserialized.getMinDate(), deserialized.getMinDate());
    #     Assert.assertEquals(deserialized.getMaxDate(), deserialized.getMaxDate());
    #
    # }

    def setUp(self):
        # setup_orekit_curdir()

        DM = DataContext.getDefault().getDataProvidersManager()
        datafile = File('regular-data.zip')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = ZipJarCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)

        System.setProperty(DataProvidersManager.OREKIT_DATA_PATH, 'potential/icgem-format')

        # Definition of initial conditions with position and velocity
        position = Vector3D(7.0e6, 1.0e6, 4.0e6)
        velocity = Vector3D(-500.0, 8000.0, 1000.0)

        mu = 3.9860047e14

        initDate = AbsoluteDate.J2000_EPOCH.shiftedBy(584.)

        self.initialOrbit = EquinoctialOrbit(PVCoordinates(position, velocity),
                                             FramesFactory.getEME2000(), initDate, mu)

        # Numerical propagator definition
        absTolerance = JArray_double([0.0001, 1.0e-11, 1.0e-11, 1.0e-8, 1.0e-8, 1.0e-8, 0.001])
        relTolerance = JArray_double([1.0e-8, 1.0e-8, 1.0e-8, 1.0e-9, 1.0e-9, 1.0e-9, 1.0e-7])

        integrator = DormandPrince853Integrator(0.001, 500.0, absTolerance, relTolerance)
        integrator.setInitialStepSize(100.0)
        self.numericalPropagator = NumericalPropagator(integrator)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IntegratedEphemerisTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
