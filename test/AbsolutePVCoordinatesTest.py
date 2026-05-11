# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's AbsolutePVCoordinatesTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from java.lang import System
from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.errors import OrekitIllegalArgumentException
from org.orekit.frames import Frame, FramesFactory, Transform
from org.orekit.time import AbsoluteDate
from org.orekit.utils import AbsolutePVCoordinates, PVCoordinates, PVCoordinatesProvider


def _velocity_of(pv):
    return pv.getVelocity()


def _acceleration_of(pv):
    return pv.getAcceleration()


class AbsolutePVCoordinatesTest(unittest.TestCase):

    def assertVectorAlmostEqual(self, expected, actual, epsilon):
        self.assertAlmostEqual(expected.getX(), actual.getX(), delta=epsilon)
        self.assertAlmostEqual(expected.getY(), actual.getY(), delta=epsilon)
        self.assertAlmostEqual(expected.getZ(), actual.getZ(), delta=epsilon)

    def assertPVAlmostEqual(self, expected, actual, epsilon):
        expected_pv = expected.getPVCoordinates()
        actual_pv = actual.getPVCoordinates()
        self.assertAlmostEqual(0.0, actual.getDate().durationFrom(expected.getDate()),
                               delta=epsilon)
        self.assertVectorAlmostEqual(expected.getPosition(), actual.getPosition(), epsilon)
        self.assertVectorAlmostEqual(_velocity_of(expected_pv),
                                     _velocity_of(actual_pv), epsilon)
        self.assertVectorAlmostEqual(_acceleration_of(expected_pv),
                                     _acceleration_of(actual_pv), epsilon)

    def test_pv_only_constructor(self):
        date = AbsoluteDate.J2000_EPOCH
        frame = FramesFactory.getEME2000()
        position = Vector3D(1.0, 2.0, 3.0)
        velocity = Vector3D(4.0, 5.0, 6.0)

        actual = AbsolutePVCoordinates(frame, date, position, velocity)
        actual_pv = actual.getPVCoordinates()

        self.assertAlmostEqual(0.0, actual.getDate().durationFrom(date), delta=0.0)
        self.assertVectorAlmostEqual(position, actual.getPosition(), 0.0)
        self.assertVectorAlmostEqual(velocity, _velocity_of(actual_pv), 0.0)
        self.assertVectorAlmostEqual(Vector3D.ZERO, _acceleration_of(actual_pv), 0.0)

    def test_pv_coordinates_copy_constructor(self):
        date = AbsoluteDate.J2000_EPOCH
        frame = FramesFactory.getEME2000()
        pv = PVCoordinates(Vector3D(1.0, 2.0, 3.0), Vector3D(4.0, 5.0, 6.0))

        actual = AbsolutePVCoordinates(frame, date, pv)
        actual_pv = actual.getPVCoordinates()

        self.assertAlmostEqual(0.0, actual.getDate().durationFrom(date), delta=0.0)
        self.assertVectorAlmostEqual(Vector3D(1.0, 2.0, 3.0), actual.getPosition(), 0.0)
        self.assertVectorAlmostEqual(Vector3D(4.0, 5.0, 6.0),
                                     _velocity_of(actual_pv), 0.0)
        self.assertVectorAlmostEqual(Vector3D.ZERO, _acceleration_of(actual_pv), 0.0)

    def test_linear_constructors(self):
        frame = FramesFactory.getEME2000()
        pv1 = AbsolutePVCoordinates(frame, AbsoluteDate.CCSDS_EPOCH,
                                    Vector3D(1.0, 0.1, 10.0),
                                    Vector3D(-1.0, -0.1, -10.0),
                                    Vector3D(10.0, -1.0, -100.0))
        pv2 = AbsolutePVCoordinates(frame, AbsoluteDate.FIFTIES_EPOCH,
                                    Vector3D(2.0, 0.2, 20.0),
                                    Vector3D(-2.0, -0.2, -20.0),
                                    Vector3D(20.0, -2.0, -200.0))
        pv3 = AbsolutePVCoordinates(frame, AbsoluteDate.GALILEO_EPOCH,
                                    Vector3D(3.0, 0.3, 30.0),
                                    Vector3D(-3.0, -0.3, -30.0),
                                    Vector3D(30.0, -3.0, -300.0))
        pv4 = AbsolutePVCoordinates(frame, AbsoluteDate.JULIAN_EPOCH,
                                    Vector3D(4.0, 0.4, 40.0),
                                    Vector3D(-4.0, -0.4, -40.0),
                                    Vector3D(40.0, -4.0, -400.0))
        self.assertPVAlmostEqual(
            pv4, AbsolutePVCoordinates(AbsoluteDate.JULIAN_EPOCH, 4.0, pv1),
            1.0e-15)
        self.assertPVAlmostEqual(
            pv2, AbsolutePVCoordinates(AbsoluteDate.FIFTIES_EPOCH, pv1, pv3),
            1.0e-15)
        self.assertPVAlmostEqual(
            pv3, AbsolutePVCoordinates(AbsoluteDate.GALILEO_EPOCH,
                                       1.0, pv1, 1.0, pv2),
            1.0e-15)
        self.assertPVAlmostEqual(
            AbsolutePVCoordinates(AbsoluteDate.J2000_EPOCH, 2.0, pv4),
            AbsolutePVCoordinates(AbsoluteDate.J2000_EPOCH,
                                  3.0, pv1, 1.0, pv2, 1.0, pv3),
            1.0e-15)
        self.assertPVAlmostEqual(
            AbsolutePVCoordinates(AbsoluteDate.J2000_EPOCH, 3.0, pv3),
            AbsolutePVCoordinates(AbsoluteDate.J2000_EPOCH,
                                  3.0, pv1, 1.0, pv2, 1.0, pv4),
            1.0e-15)
        self.assertPVAlmostEqual(
            AbsolutePVCoordinates(AbsoluteDate.J2000_EPOCH, 5.0, pv4),
            AbsolutePVCoordinates(AbsoluteDate.J2000_EPOCH,
                                  4.0, pv1, 3.0, pv2, 2.0, pv3, 1.0, pv4),
            1.0e-15)

    def test_different_frames(self):
        apv1 = AbsolutePVCoordinates(FramesFactory.getEME2000(),
                                     AbsoluteDate.ARBITRARY_EPOCH,
                                     Vector3D.ZERO, Vector3D.ZERO, Vector3D.ZERO)
        apv2 = AbsolutePVCoordinates(FramesFactory.getGCRF(),
                                     AbsoluteDate.ARBITRARY_EPOCH,
                                     Vector3D.ZERO, Vector3D.ZERO, Vector3D.ZERO)
        with self.assertRaises(JavaError) as ctx:
            AbsolutePVCoordinates(AbsoluteDate.ARBITRARY_EPOCH, apv1, apv2)
        OrekitIllegalArgumentException.cast_(ctx.exception.getJavaException())

    def test_to_derivative_structure_vector1(self):
        vector = AbsolutePVCoordinates(
            FramesFactory.getEME2000(),
            AbsoluteDate.GALILEO_EPOCH,
            Vector3D(1.0, 0.1, 10.0),
            Vector3D(-1.0, -0.1, -10.0),
            Vector3D(10.0, -1.0, -100.0),
        ).toDerivativeStructureVector(1)
        self.assertEqual(1, vector.getX().getFreeParameters())
        self.assertEqual(1, vector.getX().getOrder())
        self.assertAlmostEqual(1.0, vector.getX().getValue(), delta=1.0e-10)
        self.assertAlmostEqual(-1.0, vector.getX().getPartialDerivative(1),
                               delta=1.0e-15)
        self.assertPVAlmostEqual(
            AbsolutePVCoordinates(FramesFactory.getEME2000(),
                                  AbsoluteDate.GALILEO_EPOCH,
                                  Vector3D(1.0, 0.1, 10.0),
                                  Vector3D(-1.0, -0.1, -10.0),
                                  Vector3D.ZERO),
            AbsolutePVCoordinates(FramesFactory.getEME2000(),
                                  AbsoluteDate.GALILEO_EPOCH, vector),
            1.0e-15)

        dt = 0.0
        while dt < 10.0:
            position = PVCoordinates(Vector3D(1.0, 0.1, 10.0),
                                     Vector3D(-1.0, -0.1, -10.0)
                                     ).shiftedBy(dt).getPosition()
            self.assertAlmostEqual(position.getX(), vector.getX().taylor(dt),
                                   delta=1.0e-14)
            self.assertAlmostEqual(position.getY(), vector.getY().taylor(dt),
                                   delta=1.0e-14)
            self.assertAlmostEqual(position.getZ(), vector.getZ().taylor(dt),
                                   delta=1.0e-14)
            dt += 0.125

    def test_to_derivative_structure_vector2(self):
        vector = AbsolutePVCoordinates(
            FramesFactory.getEME2000(),
            AbsoluteDate.GALILEO_EPOCH,
            Vector3D(1.0, 0.1, 10.0),
            Vector3D(-1.0, -0.1, -10.0),
            Vector3D(10.0, -1.0, -100.0),
        ).toDerivativeStructureVector(2)
        self.assertEqual(1, vector.getX().getFreeParameters())
        self.assertEqual(2, vector.getX().getOrder())
        self.assertAlmostEqual(10.0, vector.getX().getPartialDerivative(2),
                               delta=1.0e-15)
        self.assertPVAlmostEqual(
            AbsolutePVCoordinates(FramesFactory.getEME2000(),
                                  AbsoluteDate.GALILEO_EPOCH,
                                  Vector3D(1.0, 0.1, 10.0),
                                  Vector3D(-1.0, -0.1, -10.0),
                                  Vector3D(10.0, -1.0, -100.0)),
            AbsolutePVCoordinates(FramesFactory.getEME2000(),
                                  AbsoluteDate.GALILEO_EPOCH, vector),
            1.0e-15)

    def test_to_univariate_derivative1_vector(self):
        vector = AbsolutePVCoordinates(
            FramesFactory.getEME2000(),
            AbsoluteDate.GALILEO_EPOCH,
            Vector3D(1.0, 0.1, 10.0),
            Vector3D(-1.0, -0.1, -10.0),
            Vector3D(10.0, -1.0, -100.0),
        ).toUnivariateDerivative1Vector()
        self.assertEqual(1, vector.getX().getFreeParameters())
        self.assertEqual(1, vector.getX().toDerivativeStructure().getOrder())
        self.assertAlmostEqual(-1.0, vector.getX().getPartialDerivative(1),
                               delta=1.0e-15)

    def test_to_univariate_derivative2_vector(self):
        vector = AbsolutePVCoordinates(
            FramesFactory.getEME2000(),
            AbsoluteDate.GALILEO_EPOCH,
            Vector3D(1.0, 0.1, 10.0),
            Vector3D(-1.0, -0.1, -10.0),
            Vector3D(10.0, -1.0, -100.0),
        ).toUnivariateDerivative2Vector()
        self.assertEqual(1, vector.getX().getFreeParameters())
        self.assertEqual(2, vector.getX().getOrder())
        self.assertAlmostEqual(10.0, vector.getX().getPartialDerivative(2),
                               delta=1.0e-15)

    def test_shift(self):
        p1 = Vector3D(1.0, 0.1, 10.0)
        v1 = Vector3D(-1.0, -0.1, -10.0)
        a1 = Vector3D(10.0, 1.0, 100.0)
        p2 = Vector3D(7.0, 0.7, 70.0)
        v2 = Vector3D(-11.0, -1.1, -110.0)
        a2 = Vector3D(10.0, 1.0, 100.0)
        self.assertPVAlmostEqual(
            AbsolutePVCoordinates(FramesFactory.getEME2000(),
                                  AbsoluteDate.J2000_EPOCH, p2, v2, a2),
            AbsolutePVCoordinates(FramesFactory.getEME2000(),
                                  AbsoluteDate.J2000_EPOCH.shiftedBy(1.0),
                                  p1, v1, a1).shiftedBy(-1.0),
            1.0e-15)
        self.assertAlmostEqual(
            0.0,
            AbsolutePVCoordinates.estimateVelocity(p1, p2, -1.0)
            .subtract(Vector3D(-6.0, -0.6, -60.0)).getNorm(),
            delta=1.0e-15)

    def test_to_string(self):
        pv = AbsolutePVCoordinates(
            FramesFactory.getEME2000(),
            AbsoluteDate.J2000_EPOCH,
            Vector3D(1.0, 0.1, 10.0),
            Vector3D(-1.0, -0.1, -10.0),
            Vector3D(10.0, 1.0, 100.0),
        )
        self.assertEqual(
            "{2000-01-01T11:58:55.816, P(1.0, 0.1, 10.0), "
            "V(-1.0, -0.1, -10.0), A(10.0, 1.0, 100.0)}",
            pv.toString())

    def test_same_pv(self):
        date = AbsoluteDate.J2000_EPOCH
        frame = FramesFactory.getEME2000()
        other_eme2000 = Frame(frame, Transform.IDENTITY, "other-EME2000")
        actual = AbsolutePVCoordinates(frame, date,
                                       Vector3D(1.0, 2.0, 3.0),
                                       Vector3D(4.0, 5.0, 6.0))

        self.assertEqual(System.identityHashCode(actual.getPosition()),
                         System.identityHashCode(actual.getPosition(frame)))
        self.assertNotEqual(System.identityHashCode(actual.getPosition()),
                            System.identityHashCode(actual.getPosition(other_eme2000)))
        self.assertAlmostEqual(0.0,
                               Vector3D.distance(actual.getPosition(frame),
                                                 actual.getPosition(other_eme2000)),
                               delta=1.0e-15)

        pv_frame = actual.getPVCoordinates(frame)
        pv_date_frame = actual.getPVCoordinates(date, frame)
        pv_date_other = actual.getPVCoordinates(date, other_eme2000)
        self.assertVectorAlmostEqual(pv_frame.getPosition(),
                                     pv_date_frame.getPosition(), 1.0e-15)
        self.assertVectorAlmostEqual(_velocity_of(pv_frame),
                                     _velocity_of(pv_date_frame), 1.0e-15)
        self.assertVectorAlmostEqual(_acceleration_of(pv_frame),
                                     _acceleration_of(pv_date_frame), 1.0e-15)
        self.assertVectorAlmostEqual(pv_frame.getPosition(),
                                     pv_date_other.getPosition(), 1.0e-15)
        self.assertVectorAlmostEqual(_velocity_of(pv_frame),
                                     _velocity_of(pv_date_other), 1.0e-15)
        self.assertVectorAlmostEqual(_acceleration_of(pv_frame),
                                     _acceleration_of(pv_date_other), 1.0e-15)

    def test_issue1557(self):
        abs_pv = AbsolutePVCoordinates(
            FramesFactory.getGCRF(), AbsoluteDate(),
            PVCoordinates(Vector3D(1.0, 2.0, 3.0), Vector3D(4.0, 5.0, 6.0)))
        velocity = PVCoordinatesProvider.cast_(abs_pv).getPVCoordinates(
            abs_pv.getDate(), abs_pv.getFrame()).getVelocity()
        self.assertVectorAlmostEqual(abs_pv.getPVCoordinates().getVelocity(),
                                     velocity, 0.0)

    def test_taylor_provider(self):
        date = AbsoluteDate.J2000_EPOCH
        frame = FramesFactory.getEME2000()
        actual = AbsolutePVCoordinates(frame, date,
                                       Vector3D(1.0, 2.0, 3.0),
                                       Vector3D(4.0, 5.0, 6.0))
        provider = actual.toTaylorProvider()
        self.assertAlmostEqual(0.0,
                               Vector3D.distance(actual.getPosition(date, frame),
                                                 provider.getPosition(date, frame)),
                               delta=1.0e-15)
        self.assertEqual(actual.getPVCoordinates(date, frame).toString(),
                         provider.getPVCoordinates(date, frame).toString())


if __name__ == '__main__':
    unittest.main()
