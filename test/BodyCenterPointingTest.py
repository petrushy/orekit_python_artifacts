# -*- coding: utf-8 -*-
"""JCC port of org.orekit.attitudes.BodyCenterPointingTest."""

import math
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from java.util import ArrayList
from org.hipparchus.complex import ComplexField
from org.hipparchus.fitting import PolynomialCurveFitter, WeightedObservedPoint
from org.hipparchus.geometry.euclidean.threed import (FieldRotation, FieldVector3D,
                                                      Line, Rotation, Vector3D)
from org.hipparchus.util import Binary64Field, MathArrays
from org.orekit.attitudes import BodyCenterPointing
from org.orekit.bodies import OneAxisEllipsoid
from org.orekit.frames import FramesFactory, StaticTransform
from org.orekit.orbits import (CircularOrbit, FieldCircularOrbit,
                               FieldKeplerianOrbit, PositionAngleType)
from org.orekit.propagation.analytical import (EcksteinHechlerPropagator,
                                                FieldEcksteinHechlerPropagator)
from org.orekit.time import (AbsoluteDate, DateComponents, FieldAbsoluteDate,
                             TimeComponents, TimeScalesFactory)
from org.orekit.utils import (AngularCoordinates, Constants, FieldAngularCoordinates,
                              FieldPVCoordinates, IERSConventions, PVCoordinates)


class BodyCenterPointingTest(unittest.TestCase):

    def setUp(self):
        self.date = AbsoluteDate(DateComponents(2008, 4, 7),
                                 TimeComponents.H00,
                                 TimeScalesFactory.getUTC())
        mu = 3.9860047e14
        raan = 270.0
        self.circ = CircularOrbit(7178000.0, 0.5e-4, -0.5e-4,
                                  math.radians(50.0), math.radians(raan),
                                  math.radians(5.300 - raan), PositionAngleType.MEAN,
                                  FramesFactory.getEME2000(), self.date, mu)
        self.earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                      Constants.WGS84_EARTH_FLATTENING,
                                      FramesFactory.getITRF(IERSConventions.IERS_2010, True))
        self.eme2000_to_itrf = FramesFactory.getEME2000() \
            .getTransformTo(self.earth.getBodyFrame(), self.date)
        self.earth_center_attitude_law = BodyCenterPointing(self.circ.getFrame(), self.earth)

    @unittest.skip("BodyCenterPointing.getTargetPosition is not exposed in this Orekit JCC build")
    def test_get_position(self):
        actual = self.earth_center_attitude_law.getTargetPosition(
            self.circ, self.date, self.circ.getFrame())
        expected = self.earth_center_attitude_law.getTargetPV(
            self.circ, self.date, self.circ.getFrame()).getPosition()
        self.assertEqual(expected, actual)

    @unittest.skip("BodyCenterPointing.getTargetPosition is not exposed in this Orekit JCC build")
    def test_get_position_field(self):
        field_orbit = FieldCircularOrbit(ComplexField.getInstance(), self.circ)
        actual = self.earth_center_attitude_law.getTargetPosition(
            field_orbit, field_orbit.getDate(), self.circ.getFrame())
        expected = self.earth_center_attitude_law.getTargetPV(
            field_orbit, field_orbit.getDate(), self.circ.getFrame()).getPosition()
        self.assertAlmostEqual(0.0,
                               expected.subtract(actual).getNorm().getReal(),
                               delta=1.0e-10)

    def test_target(self):
        target = self.earth_center_attitude_law.getTargetPV(
            self.circ, self.date, self.circ.getFrame())
        gp = self.earth.transform(target.getPosition(), self.circ.getFrame(), self.date)
        self.assertAlmostEqual(0.0, gp.getAltitude(), delta=1.0e-9)
        self.assertAlmostEqual(0.0, target.getDate().durationFrom(self.date), delta=0.0)

    def test_body_center_in_pointing_direction(self):
        pv_sat = self.circ.getPVCoordinates()
        rotation = self.earth_center_attitude_law.getAttitude(
            self.circ, self.date, self.circ.getFrame()).getRotation()
        z_sat = rotation.applyInverseTo(Vector3D.PLUS_K)
        # transformVector is a default method on the StaticTransform interface;
        # JCC doesn't dispatch interface defaults on subclasses.
        z_itrf = StaticTransform.cast_(self.eme2000_to_itrf).transformVector(z_sat)
        pv_itrf = self.eme2000_to_itrf.transformPVCoordinates(pv_sat)
        line = Line(pv_itrf.getPosition(),
                    pv_itrf.getPosition().add(Constants.WGS84_EARTH_EQUATORIAL_RADIUS, z_itrf),
                    2.0e-8)
        self.assertTrue(line.contains(Vector3D.ZERO))

    def test_q_dot(self):
        propagator, date = self._build_eckstein_hechler_propagator()
        self._check_q_dot(propagator, date, False)

    def test_spin(self):
        propagator, date = self._build_eckstein_hechler_propagator()
        h = 0.01
        s0 = propagator.propagate(date)
        s_minus = propagator.propagate(date.shiftedBy(-h))
        s_plus = propagator.propagate(date.shiftedBy(h))
        error_minus = Rotation.distance(s_minus.shiftedBy(h).getAttitude().getRotation(),
                                        s0.getAttitude().getRotation())
        evolution_minus = Rotation.distance(s_minus.getAttitude().getRotation(),
                                            s0.getAttitude().getRotation())
        self.assertAlmostEqual(0.0, error_minus, delta=1.0e-6 * evolution_minus)
        error_plus = Rotation.distance(s0.getAttitude().getRotation(),
                                       s_plus.shiftedBy(-h).getAttitude().getRotation())
        evolution_plus = Rotation.distance(s0.getAttitude().getRotation(),
                                           s_plus.getAttitude().getRotation())
        self.assertAlmostEqual(0.0, error_plus, delta=1.0e-6 * evolution_plus)
        spin0 = s0.getAttitude().getSpin()
        reference = AngularCoordinates.estimateRate(s_minus.getAttitude().getRotation(),
                                                    s_plus.getAttitude().getRotation(),
                                                    2.0 * h)
        self.assertTrue(spin0.getNorm() > 1.0e-3)
        self.assertAlmostEqual(0.0, spin0.subtract(reference).getNorm(), delta=2.0e-13)

    def test_target_field(self):
        field = Binary64Field.getInstance()
        date, circ, earth, law = self._build_field_context(field)
        target = law.getTargetPV(circ, date, circ.getFrame())
        gp = earth.transform(target.getPosition().toVector3D(),
                             circ.getFrame(), date.toAbsoluteDate())
        self.assertAlmostEqual(0.0, gp.getAltitude(), delta=1.0e-8)
        self.assertAlmostEqual(0.0, target.getDate().durationFrom(date).getReal(), delta=0.0)

    def test_body_center_in_pointing_direction_field(self):
        field = Binary64Field.getInstance()
        date, circ, earth, law = self._build_field_context(field)
        transform = FramesFactory.getEME2000() \
            .getStaticTransformTo(earth.getBodyFrame(), date.toAbsoluteDate())
        position = circ.getPosition()
        rotation = law.getAttitude(circ, date, circ.getFrame()).getRotation()
        z_sat = rotation.applyInverseTo(Vector3D.PLUS_K)
        z_itrf = transform.transformVector(z_sat)
        position_itrf = transform.transformPosition(position)
        line = Line(position_itrf.toVector3D(),
                    position_itrf.toVector3D().add(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                                    z_itrf.toVector3D()),
                    2.0e-8)
        self.assertTrue(line.contains(Vector3D.ZERO))

    def test_q_dot_field(self):
        propagator, date = self._build_field_eckstein_hechler_propagator(Binary64Field.getInstance())
        self._check_q_dot(propagator, date, True)

    def test_spin_field(self):
        field = Binary64Field.getInstance()
        zero = field.getZero()
        propagator, date = self._build_field_eckstein_hechler_propagator(field)
        h = 0.01
        s0 = propagator.propagate(date)
        s_minus = propagator.propagate(date.shiftedBy(-h))
        s_plus = propagator.propagate(date.shiftedBy(h))
        error_minus = FieldRotation.distance(s_minus.shiftedBy(zero.add(h))
                                             .getAttitude().getRotation(),
                                             s0.getAttitude().getRotation())
        evolution_minus = FieldRotation.distance(s_minus.getAttitude().getRotation(),
                                                 s0.getAttitude().getRotation())
        self.assertAlmostEqual(0.0, error_minus.getReal(),
                               delta=1.0e-6 * evolution_minus.getReal())
        error_plus = FieldRotation.distance(s0.getAttitude().getRotation(),
                                            s_plus.shiftedBy(zero.add(-h))
                                                .getAttitude().getRotation())
        evolution_plus = FieldRotation.distance(s0.getAttitude().getRotation(),
                                                s_plus.getAttitude().getRotation())
        self.assertAlmostEqual(0.0, error_plus.getReal(),
                               delta=1.0e-6 * evolution_plus.getReal())
        spin0 = s0.getAttitude().getSpin()
        reference = FieldAngularCoordinates.estimateRate(s_minus.getAttitude().getRotation(),
                                                         s_plus.getAttitude().getRotation(),
                                                         2.0 * h)
        self.assertTrue(spin0.getNorm().getReal() > 1.0e-3)
        self.assertAlmostEqual(0.0, spin0.subtract(reference).getNorm().getReal(),
                               delta=1.4e-13)

    def _build_field_context(self, field):
        zero = field.getZero()
        mu = zero.add(3.9860047e14)
        date = FieldAbsoluteDate(field, DateComponents(2008, 4, 7),
                                 TimeComponents.H00, TimeScalesFactory.getUTC())
        circ = FieldKeplerianOrbit(zero.add(7178000.0), zero.add(7e-5),
                                   zero.add(math.radians(50.0)),
                                   zero.add(math.radians(45.0)),
                                   zero.add(math.radians(270.0)),
                                   zero.add(math.radians(5.3 - 270.0)),
                                   PositionAngleType.MEAN,
                                   FramesFactory.getEME2000(), date, mu)
        earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                                 Constants.WGS84_EARTH_FLATTENING,
                                 FramesFactory.getITRF(IERSConventions.IERS_2010, True))
        return date, circ, earth, BodyCenterPointing(circ.getFrame(), earth)

    def _build_eckstein_hechler_propagator(self):
        eh_mu = 3.9860047e14
        date = AbsoluteDate.J2000_EPOCH.shiftedBy(584.0)
        orbit = CircularOrbit(PVCoordinates(Vector3D(3220103.0, 69623.0, 6449822.0),
                                            Vector3D(6414.7, -2006.0, -3180.0)),
                              FramesFactory.getEME2000(), date, eh_mu)
        propagator = EcksteinHechlerPropagator(orbit, 6.378137e6, eh_mu,
                                               -1.08263e-3, 2.54e-6, 1.62e-6, 2.3e-7, -5.5e-7)
        propagator.setAttitudeProvider(self.earth_center_attitude_law)
        return propagator, date

    def _build_field_eckstein_hechler_propagator(self, field):
        zero = field.getZero()
        eh_mu = zero.add(3.9860047e14)
        date = FieldAbsoluteDate.getJ2000Epoch(field).shiftedBy(584.0)
        orbit = FieldCircularOrbit(
            FieldPVCoordinates(FieldVector3D(zero.add(3220103.0), zero.add(69623.0), zero.add(6449822.0)),
                                FieldVector3D(zero.add(6414.7), zero.add(-2006.0), zero.add(-3180.0))),
            FramesFactory.getEME2000(), date, eh_mu)
        propagator = FieldEcksteinHechlerPropagator(orbit, 6.378137e6, eh_mu,
                                                    -1.08263e-3, 2.54e-6, 1.62e-6, 2.3e-7, -5.5e-7)
        propagator.setAttitudeProvider(self.earth_center_attitude_law)
        return propagator, date

    def _check_q_dot(self, propagator, date, field):
        lists = [ArrayList(), ArrayList(), ArrayList(), ArrayList()]
        dt = -1.0
        while dt < 1.0:
            rotation = propagator.propagate(date.shiftedBy(dt)).getAttitude().getRotation()
            values = [rotation.getQ0(), rotation.getQ1(), rotation.getQ2(), rotation.getQ3()]
            if field:
                values = [v.getReal() for v in values]
            for observed, value in zip(lists, values):
                observed.add(WeightedObservedPoint(1.0, dt, value))
            dt += 0.01
        refs = [PolynomialCurveFitter.create(2).fit(observed)[1] for observed in lists]
        a0 = propagator.propagate(date).getAttitude()
        q = [a0.getRotation().getQ0(), a0.getRotation().getQ1(),
             a0.getRotation().getQ2(), a0.getRotation().getQ3()]
        spin = [a0.getSpin().getX(), a0.getSpin().getY(), a0.getSpin().getZ()]
        if field:
            q = [v.getReal() for v in q]
            spin = [v.getReal() for v in spin]
        q0, q1, q2, q3 = q
        ox, oy, oz = spin
        dots = [
            0.5 * MathArrays.linearCombination(-q1, ox, -q2, oy, -q3, oz),
            0.5 * MathArrays.linearCombination(q0, ox, -q3, oy, q2, oz),
            0.5 * MathArrays.linearCombination(q3, ox, q0, oy, -q1, oz),
            0.5 * MathArrays.linearCombination(-q2, ox, q1, oy, q0, oz),
        ]
        for expected, actual in zip(refs, dots):
            self.assertAlmostEqual(expected, actual, delta=5.0e-9)


if __name__ == '__main__':
    unittest.main()
