# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's ConstantPVCoordinatesProviderTest."""

import math
import random
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import GeodeticPoint
from org.orekit.frames import FramesFactory
from org.orekit.models.earth import ReferenceEllipsoid
from org.orekit.time import AbsoluteDate, DateTimeComponents, TimeScalesFactory
from org.orekit.utils import ConstantPVCoordinatesProvider, IERSConventions
from org.orekit.utils import PVCoordinates


class ConstantPVCoordinatesProviderTest(unittest.TestCase):

    def assertDateEqual(self, expected, actual):
        self.assertAlmostEqual(0.0, actual.durationFrom(expected), delta=1.0e-15)

    def assertVectorEqual(self, expected, actual, delta=0.0):
        self.assertAlmostEqual(expected.getX(), actual.getX(), delta=delta)
        self.assertAlmostEqual(expected.getY(), actual.getY(), delta=delta)
        self.assertAlmostEqual(expected.getZ(), actual.getZ(), delta=delta)

    def assertPVEqual(self, expected, actual, delta=0.0):
        self.assertVectorEqual(expected.getPosition(), actual.getPosition(), delta)
        self.assertVectorEqual(expected.getVelocity(), actual.getVelocity(), delta)
        self.assertVectorEqual(expected.getAcceleration(), actual.getAcceleration(), delta)

    def test_verify_ellipsoid_location(self):
        itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, True)
        body = ReferenceEllipsoid.getWgs84(itrf)

        point = GeodeticPoint(math.radians(39.952330),
                              math.radians(-75.16379),
                              12.192)

        pos_itrf = body.transform(point)
        vel_itrf = Vector3D.ZERO
        pv_itrf = PVCoordinates(pos_itrf, vel_itrf)

        gcrf = FramesFactory.getGCRF()
        eme2000 = FramesFactory.getEME2000()

        utc = TimeScalesFactory.getUTC()
        epoch = AbsoluteDate(DateTimeComponents.parseDateTime("2022-06-01T10:35:00Z"),
                             utc)

        pv_prov = ConstantPVCoordinatesProvider(point, body)

        tpv_itrf = pv_prov.getPVCoordinates(epoch, itrf)
        self.assertDateEqual(epoch, tpv_itrf.getDate())
        self.assertVectorEqual(pos_itrf, tpv_itrf.getPosition())
        self.assertVectorEqual(vel_itrf, tpv_itrf.getVelocity())
        self.assertVectorEqual(Vector3D.ZERO, tpv_itrf.getAcceleration())

        pv_gcrf = itrf.getTransformTo(gcrf, epoch).transformPVCoordinates(pv_itrf)
        tpv_gcrf = pv_prov.getPVCoordinates(epoch, gcrf)
        self.assertDateEqual(epoch, tpv_gcrf.getDate())
        self.assertPVEqual(pv_gcrf, tpv_gcrf, 0.0)

        pv_eme2000 = itrf.getTransformTo(eme2000, epoch).transformPVCoordinates(pv_itrf)
        tpv_eme2000 = pv_prov.getPVCoordinates(epoch, eme2000)
        self.assertDateEqual(epoch, tpv_eme2000.getDate())
        self.assertPVEqual(pv_eme2000, tpv_eme2000, 0.0)

        rng = random.Random(0x5EED)
        for _ in range(100):
            dt = rng.uniform(1.0, 604800.0)
            date = epoch.shiftedBy(dt)

            actual_itrf = pv_prov.getPVCoordinates(date, itrf)
            self.assertDateEqual(date, actual_itrf.getDate())
            self.assertVectorEqual(pos_itrf, actual_itrf.getPosition())
            self.assertVectorEqual(vel_itrf, actual_itrf.getVelocity())
            self.assertVectorEqual(Vector3D.ZERO, actual_itrf.getAcceleration())

            expected_gcrf = itrf.getTransformTo(gcrf, date).transformPVCoordinates(pv_itrf)
            actual_gcrf = pv_prov.getPVCoordinates(date, gcrf)
            self.assertDateEqual(date, actual_gcrf.getDate())
            self.assertPVEqual(expected_gcrf, actual_gcrf, 0.0)

            expected_eme2000 = itrf.getTransformTo(eme2000, date).transformPVCoordinates(
                pv_itrf)
            actual_eme2000 = pv_prov.getPVCoordinates(date, eme2000)
            self.assertDateEqual(date, actual_eme2000.getDate())
            self.assertPVEqual(expected_eme2000, actual_eme2000, 0.0)


if __name__ == '__main__':
    unittest.main()
