# -*- coding: utf-8 -*-
"""
JCC port adapted from orekit_jpype's test/RuggedTest.py.
"""

import datetime
import math
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import datetime_to_absolutedate, setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from java.util import ArrayList
from org.hipparchus.geometry.euclidean.threed import Rotation, Vector3D
from org.orekit.attitudes import FrameAlignedProvider
from org.orekit.bodies import GeodeticPoint
from org.orekit.frames import FramesFactory
from org.orekit.models.earth import ReferenceEllipsoid
from org.orekit.orbits import CartesianOrbit
from org.orekit.propagation import Propagator
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.propagation.analytical.tle import SGP4, TLE
from org.orekit.rugged.api import AlgorithmId, Rugged, RuggedBuilder
from org.orekit.rugged.linesensor import LinearLineDatation, LineSensor
from org.orekit.rugged.los import LOSBuilder
from org.orekit.time import AbsoluteDate
from org.orekit.utils import (AngularDerivativesFilter,
                              CartesianDerivativesFilter, Constants,
                              IERSConventions, TimeStampedPVCoordinates)


class RuggedTest(unittest.TestCase):

    def setUp(self):
        self.tod = FramesFactory.getTOD(IERSConventions.IERS_2010, True)
        self.itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, True)
        self.wgs84_ellipsoid = ReferenceEllipsoid.getWgs84(self.itrf)

        self.t_step = 1.0
        self.overshoot_tolerance = 1.0
        self.n_interpolation_neighbours = 2

    def build_line_sensor(self, line_epoch: AbsoluteDate) -> LineSensor:
        viewing_directions = ArrayList()
        viewing_directions.add(Vector3D(0.0, 0.0, 1.0))

        line_of_sight = LOSBuilder(viewing_directions).build()
        line_datation = LinearLineDatation(line_epoch, 0.0, 1.0e3)

        return LineSensor("LineSensor", line_datation, Vector3D.ZERO, line_of_sight)

    def build_propagator(self, timestamp: datetime.datetime, pos_TOD,
                         vel_TOD, att_provider) -> Propagator:
        timestamped_pv = TimeStampedPVCoordinates(
            datetime_to_absolutedate(timestamp),
            Vector3D(pos_TOD[0], pos_TOD[1], pos_TOD[2]),
            Vector3D(vel_TOD[0], vel_TOD[1], vel_TOD[2]))

        orbit = CartesianOrbit(timestamped_pv, self.tod,
                               Constants.WGS84_EARTH_MU)

        return KeplerianPropagator(orbit, att_provider)

    def build_rugged(self, propagator: Propagator, min_date: AbsoluteDate,
                     max_date: AbsoluteDate, line_sensor: LineSensor) -> Rugged:
        rugged_builder = RuggedBuilder()

        rugged_builder.setAlgorithm(AlgorithmId.IGNORE_DEM_USE_ELLIPSOID)
        rugged_builder.setEllipsoid(self.wgs84_ellipsoid)
        rugged_builder.setTimeSpan(min_date, max_date,
                                   self.t_step, self.overshoot_tolerance)

        rugged_builder.setTrajectory(self.t_step,
                                     self.n_interpolation_neighbours,
                                     CartesianDerivativesFilter.USE_PV,
                                     AngularDerivativesFilter.USE_RR,
                                     propagator)
        rugged_builder.addLineSensor(line_sensor)

        return rugged_builder.build()

    def build_frame_aligned_provider(self, q_TODfromSAT):
        rotation = Rotation(q_TODfromSAT[0], q_TODfromSAT[1],
                            q_TODfromSAT[2], q_TODfromSAT[3],
                            True)
        return FrameAlignedProvider(rotation, self.tod)

    def build_tle_propagator(self, att_provider, tle_line1: str,
                             tle_line2: str) -> Propagator:
        tle = TLE(tle_line1, tle_line2)
        return SGP4(tle, att_provider, 50.0)

    def direct_location(self, timestamp: datetime.datetime,
                        propagator: Propagator) -> GeodeticPoint:
        absolute_date = datetime_to_absolutedate(timestamp)
        min_date = absolute_date.shiftedBy(-self.t_step)
        max_date = absolute_date.shiftedBy(self.t_step)

        line_sensor = self.build_line_sensor(line_epoch=min_date)
        rugged = self.build_rugged(propagator=propagator,
                                   min_date=min_date,
                                   max_date=max_date,
                                   line_sensor=line_sensor)

        los = line_sensor.getLOS(absolute_date, 0)
        return rugged.directLocation(absolute_date, Vector3D.ZERO, los)

    def assertTenerife(self, geodetic_point):
        self.assertAlmostEqual(28.5, math.degrees(geodetic_point.getLatitude()),
                               delta=1.0)
        self.assertAlmostEqual(-17.0, math.degrees(geodetic_point.getLongitude()),
                               delta=1.0)

    def test_rugged_direct_location_single_pva_point(self):
        timestamp = datetime.datetime(2023, 8, 17, 16, 6, 26, 400000)

        inertial_att_provider = self.build_frame_aligned_provider(
            [0.1288, 0.85362673, -0.12312595, 0.48946089])

        bounded_prop = self.build_propagator(
            timestamp=timestamp,
            pos_TOD=[-5984085.0, -831225.0, 3291501.75],
            vel_TOD=[-3744.86083984, 638.70556641, -6598.59521484],
            att_provider=inertial_att_provider)

        geodetic_point = self.direct_location(timestamp=timestamp,
                                              propagator=bounded_prop)

        self.assertTenerife(geodetic_point)

    def test_rugged_direct_location_from_tle(self):
        timestamp = datetime.datetime(2023, 8, 17, 16, 6, 26, 400000)

        inertial_att_provider = self.build_frame_aligned_provider(
            [0.1288, 0.85362673, -0.12312595, 0.48946089])

        propagator = self.build_tle_propagator(
            inertial_att_provider,
            tle_line1="1 48900U 21059X   23229.44616644  .00010250  00000-0  47112-3 0  9997",
            tle_line2="2 48900  97.6079   3.5060 0009943  72.3812 287.8508 15.20521326118480")

        geodetic_point = self.direct_location(timestamp=timestamp,
                                              propagator=propagator)

        self.assertTenerife(geodetic_point)


if __name__ == '__main__':
    unittest.main()
