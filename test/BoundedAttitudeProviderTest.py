# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's BoundedAttitudeProviderTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Rotation, Vector3D
from org.hipparchus.util import Binary64Field
from org.orekit.attitudes import BoundedAttitudeProvider, FrameAlignedProvider
from org.orekit.frames import FramesFactory
from org.orekit.orbits import CartesianOrbit, FieldCartesianOrbit
from org.orekit.time import AbsoluteDate, TimeInterval
from org.orekit.utils import PVCoordinates


def _get_default_orbit(date):
    pv = PVCoordinates(Vector3D(6378000.0 + 400000.0, 0.0, 0.0),
                       Vector3D(0.0, 7668.631425, 0.0))
    return CartesianOrbit(pv, FramesFactory.getGCRF(), date, 398600.0e9)


class BoundedAttitudeProviderTest(unittest.TestCase):

    def assertDateEqual(self, expected, actual):
        self.assertAlmostEqual(0.0, actual.durationFrom(expected), delta=1.0e-15)

    def assertVectorEqual(self, expected, actual, delta=1.0e-15):
        self.assertAlmostEqual(expected.getX(), actual.getX(), delta=delta)
        self.assertAlmostEqual(expected.getY(), actual.getY(), delta=delta)
        self.assertAlmostEqual(expected.getZ(), actual.getZ(), delta=delta)

    def assertFieldVectorEqual(self, expected, actual, delta=1.0e-15):
        self.assertAlmostEqual(expected.getX().getReal(), actual.getX().getReal(),
                               delta=delta)
        self.assertAlmostEqual(expected.getY().getReal(), actual.getY().getReal(),
                               delta=delta)
        self.assertAlmostEqual(expected.getZ().getReal(), actual.getZ().getReal(),
                               delta=delta)

    def test_of_getters(self):
        min_date = AbsoluteDate.ARBITRARY_EPOCH
        max_date = min_date.shiftedBy(10.0)
        time_interval = TimeInterval.of(min_date, max_date)
        provider = FrameAlignedProvider(FramesFactory.getEME2000())

        bounded = BoundedAttitudeProvider.of(provider, time_interval)

        self.assertDateEqual(min_date, bounded.getMinDate())
        self.assertDateEqual(max_date, bounded.getMaxDate())

    def test_of_attitude(self):
        min_date = AbsoluteDate.ARBITRARY_EPOCH
        max_date = min_date.shiftedBy(10.0)
        time_interval = TimeInterval.of(min_date, max_date)
        provider = FrameAlignedProvider(FramesFactory.getEME2000())
        orbit = _get_default_orbit(min_date)

        bounded = BoundedAttitudeProvider.of(provider, time_interval)

        actual_attitude = bounded.getAttitude(orbit, orbit.getDate(), orbit.getFrame())
        expected_attitude = provider.getAttitude(orbit, orbit.getDate(), orbit.getFrame())
        self.assertAlmostEqual(
            0.0,
            Rotation.distance(actual_attitude.getRotation(),
                              expected_attitude.getRotation()),
            delta=1.0e-6,
        )
        self.assertVectorEqual(expected_attitude.getSpin(), actual_attitude.getSpin())
        self.assertVectorEqual(expected_attitude.getRotationAcceleration(),
                               actual_attitude.getRotationAcceleration())
        self.assertDateEqual(expected_attitude.getDate(), actual_attitude.getDate())
        self.assertEqual(actual_attitude.getReferenceFrame(),
                         expected_attitude.getReferenceFrame())

        actual_rotation = bounded.getAttitudeRotation(orbit, orbit.getDate(),
                                                      orbit.getFrame())
        expected_rotation = provider.getAttitudeRotation(orbit, orbit.getDate(),
                                                        orbit.getFrame())
        self.assertAlmostEqual(0.0, Rotation.distance(actual_rotation, expected_rotation),
                               delta=1.0e-6)

    def test_of_field_attitude(self):
        min_date = AbsoluteDate.ARBITRARY_EPOCH
        max_date = min_date.shiftedBy(10.0)
        time_interval = TimeInterval.of(min_date, max_date)
        provider = FrameAlignedProvider(FramesFactory.getEME2000())
        orbit = _get_default_orbit(max_date)
        field_orbit = FieldCartesianOrbit(Binary64Field.getInstance(), orbit)

        bounded = BoundedAttitudeProvider.of(provider, time_interval)

        actual_attitude = bounded.getAttitude(field_orbit, field_orbit.getDate(),
                                              orbit.getFrame())
        expected_attitude = provider.getAttitude(field_orbit, field_orbit.getDate(),
                                                orbit.getFrame())
        self.assertAlmostEqual(
            0.0,
            Rotation.distance(actual_attitude.getRotation().toRotation(),
                              expected_attitude.getRotation().toRotation()),
            delta=1.0e-6,
        )
        self.assertFieldVectorEqual(expected_attitude.getSpin(),
                                    actual_attitude.getSpin())
        self.assertFieldVectorEqual(expected_attitude.getRotationAcceleration(),
                                    actual_attitude.getRotationAcceleration())
        self.assertEqual(actual_attitude.getDate(), expected_attitude.getDate())
        self.assertEqual(actual_attitude.getReferenceFrame(),
                         expected_attitude.getReferenceFrame())

        actual_rotation = bounded.getAttitudeRotation(field_orbit,
                                                      field_orbit.getDate(),
                                                      orbit.getFrame())
        expected_rotation = provider.getAttitudeRotation(field_orbit,
                                                        field_orbit.getDate(),
                                                        orbit.getFrame())
        self.assertAlmostEqual(
            0.0,
            Rotation.distance(actual_rotation.toRotation(),
                              expected_rotation.toRotation()),
            delta=1.0e-6,
        )


if __name__ == '__main__':
    unittest.main()
