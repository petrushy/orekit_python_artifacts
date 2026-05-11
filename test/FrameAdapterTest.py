# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's FrameAdapterTest."""

import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import FieldVector3D, Vector3D
from org.hipparchus.util import Binary64Field
from org.orekit.bodies import CelestialBodyFactory
from org.orekit.frames import FramesFactory
from org.orekit.time import AbsoluteDate, FieldAbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants, FrameAdapter


class FrameAdapterTest(unittest.TestCase):

    def test_double(self):
        eme2000 = FramesFactory.getEME2000()
        moon = CelestialBodyFactory.getMoon()
        moon_frame = moon.getBodyOrientedFrame()
        moon_pv_provider = FrameAdapter(moon_frame)

        t0 = AbsoluteDate("2000-01-22T13:30:00", TimeScalesFactory.getUTC())
        max_p = 0.0
        max_v = 0.0
        max_a = 0.0
        dt = 0.0
        while dt < Constants.JULIAN_DAY:
            t = t0.shiftedBy(dt)
            pv_ref = moon.getPVCoordinates(t, eme2000)
            pv_adapted = moon_pv_provider.getPVCoordinates(t, eme2000)
            max_p = max(max_p, Vector3D.distance(pv_ref.getPosition(),
                                                 pv_adapted.getPosition()))
            max_v = max(max_v, Vector3D.distance(pv_ref.getVelocity(),
                                                 pv_adapted.getVelocity()))
            max_a = max(max_a, Vector3D.distance(pv_ref.getAcceleration(),
                                                 pv_adapted.getAcceleration()))
            dt += 60.0
        self.assertAlmostEqual(0.0, max_p, delta=8.2e-7)
        self.assertAlmostEqual(0.0, max_v, delta=2.9e-12)
        self.assertAlmostEqual(0.0, max_a, delta=1.1e-17)

    def test_field(self):
        field = Binary64Field.getInstance()
        eme2000 = FramesFactory.getEME2000()
        moon = CelestialBodyFactory.getMoon()
        moon_frame = moon.getBodyOrientedFrame()
        moon_pv_provider = FrameAdapter(moon_frame)

        t0 = FieldAbsoluteDate(field, AbsoluteDate("2000-01-22T13:30:00",
                                                  TimeScalesFactory.getUTC()))
        max_p = field.getZero()
        max_v = field.getZero()
        max_a = field.getZero()
        dt = 0.0
        while dt < Constants.JULIAN_DAY:
            t = t0.shiftedBy(dt)
            pv_ref = moon.getPVCoordinates(t, eme2000)
            pv_adapted = moon_pv_provider.getPVCoordinates(t, eme2000)
            max_p = max(max_p,
                        FieldVector3D.distance(pv_ref.getPosition(),
                                               pv_adapted.getPosition()),
                        key=lambda value: value.getReal())
            max_v = max(max_v,
                        FieldVector3D.distance(pv_ref.getVelocity(),
                                               pv_adapted.getVelocity()),
                        key=lambda value: value.getReal())
            max_a = max(max_a,
                        FieldVector3D.distance(pv_ref.getAcceleration(),
                                               pv_adapted.getAcceleration()),
                        key=lambda value: value.getReal())
            dt += 60.0
        self.assertAlmostEqual(0.0, max_p.getReal(), delta=8.2e-7)
        self.assertAlmostEqual(0.0, max_v.getReal(), delta=2.9e-12)
        self.assertAlmostEqual(0.0, max_a.getReal(), delta=1.1e-17)

    def test_get_position_field(self):
        eme2000 = FramesFactory.getEME2000()
        moon_frame = CelestialBodyFactory.getMoon().getBodyOrientedFrame()
        moon_pv_provider = FrameAdapter(moon_frame)
        date = AbsoluteDate.ARBITRARY_EPOCH
        field_date = FieldAbsoluteDate(Binary64Field.getInstance(), date)
        field_position = moon_pv_provider.getPosition(field_date, eme2000)
        self.assertAlmostEqual(
            0.0,
            Vector3D.distance(moon_pv_provider.getPosition(date, eme2000),
                              field_position.toVector3D()),
            delta=1.0e-15)


if __name__ == '__main__':
    unittest.main()
