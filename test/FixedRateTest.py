import unittest

import orekit
orekit.initVM()

from org.hipparchus.geometry.euclidean.threed import Rotation, Vector3D
from org.orekit.attitudes import Attitude, FixedRate
from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit
from org.orekit.time import AbsoluteDate, DateComponents, TimeComponents, TimeScalesFactory
from org.orekit.utils import PVCoordinates, AngularCoordinates
from org.hipparchus.util import FastMath
from org.orekit.orbits import PositionAngleType
from org.orekit.propagation.analytical import KeplerianPropagator

from java.io import File
from org.orekit.data import DataContext, DirectoryCrawler

class OrekitFixedRateTest(unittest.TestCase):
    def setUp(self):
        DM = DataContext.getDefault().getDataProvidersManager()
        datafile = File('resources')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = DirectoryCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)

    def test_zero_rate(self):
        date = AbsoluteDate(DateComponents(2004, 3, 2),
                            TimeComponents(13, 17, 7.865),
                            TimeScalesFactory.getUTC())
        frame = FramesFactory.getEME2000()
        law = FixedRate(Attitude(date, frame,
                                 Rotation(0.48, 0.64, 0.36, 0.48, False),
                                 Vector3D.ZERO, Vector3D.ZERO))
        pv = PVCoordinates(Vector3D(28812595.32012577, 5948437.4640250085, 0.0),
                           Vector3D(0.0, 0.0, 3680.853673522056))
        orbit = KeplerianOrbit(pv, frame, date, 3.986004415e14)
        attitude0 = law.getAttitude(orbit, date, frame).getRotation()
        self.assertAlmostEqual(0, Rotation.distance(attitude0, law.getReferenceAttitude().getRotation()), delta=1.0e-10)
        attitude1 = law.getAttitude(orbit.shiftedBy(10.0), date.shiftedBy(10.0), frame).getRotation()
        self.assertAlmostEqual(0, Rotation.distance(attitude1, law.getReferenceAttitude().getRotation()), delta=1.0e-10)
        attitude2 = law.getAttitude(orbit.shiftedBy(20.0), date.shiftedBy(20.0), frame).getRotation()
        self.assertAlmostEqual(0, Rotation.distance(attitude2, law.getReferenceAttitude().getRotation()), delta=1.0e-10)


    def test_non_zero_rate(self):
        date = AbsoluteDate(DateComponents(2004, 3, 2),
                            TimeComponents(13, 17, 7.865),
                            TimeScalesFactory.getUTC())
        rate = 2 * FastMath.PI / (12 * 60)
        frame = FramesFactory.getEME2000()
        gcrf = FramesFactory.getGCRF()
        law = FixedRate(Attitude(date, frame,
                                 Rotation(0.48, 0.64, 0.36, 0.48, False),
                                 Vector3D(rate, Vector3D.PLUS_K), Vector3D.ZERO))
        ref = law.getReferenceAttitude().getRotation().applyTo(gcrf.getTransformTo(frame, date).getRotation())
        pv = PVCoordinates(Vector3D(28812595.32012577, 5948437.4640250085, 0.0),
                           Vector3D(0.0, 0.0, 3680.853673522056))
        orbit = KeplerianOrbit(pv, frame, date, 3.986004415e14)
        attitude0 = law.getAttitude(orbit, date, gcrf).getRotation()
        self.assertAlmostEqual(0, Rotation.distance(attitude0, ref), delta=1.0e-10)
        attitude1 = law.getAttitude(orbit.shiftedBy(10.0), date.shiftedBy(10.0), gcrf).getRotation()
        self.assertAlmostEqual(10 * rate, Rotation.distance(attitude1, ref), delta=1.0e-10)
        attitude2 = law.getAttitude(orbit.shiftedBy(-20.0), date.shiftedBy(-20.0), gcrf).getRotation()
        self.assertAlmostEqual(20 * rate, Rotation.distance(attitude2, ref), delta=1.0e-10)
        self.assertAlmostEqual(30 * rate, Rotation.distance(attitude2, attitude1), delta=1.0e-10)
        attitude3 = law.getAttitude(orbit.shiftedBy(0.0), date, frame).getRotation()
        self.assertAlmostEqual(0, Rotation.distance(attitude3, law.getReferenceAttitude().getRotation()), delta=1.0e-10)


    def test_spin(self):
        date = AbsoluteDate(DateComponents(1970, 1, 1),
                            TimeComponents(3, 25, 45.6789),
                            TimeScalesFactory.getUTC())

        rate = 2 * FastMath.PI / (12 * 60)
        law = FixedRate(Attitude(date, FramesFactory.getEME2000(),
                                 Rotation(0.48, 0.64, 0.36, 0.48, False),
                                 Vector3D(rate, Vector3D.PLUS_K),
                                 Vector3D.ZERO))

        orbit = KeplerianOrbit(7178000.0, 1.e-4, FastMath.toRadians(50.0),
                               FastMath.toRadians(10.0), FastMath.toRadians(20.0),
                               FastMath.toRadians(30.0), PositionAngleType.MEAN,
                               FramesFactory.getEME2000(), date, 3.986004415e14)

        propagator = KeplerianPropagator(orbit, law)

        h = 0.01
        s_minus = propagator.propagate(date.shiftedBy(-h))
        s0 = propagator.propagate(date)
        s_plus = propagator.propagate(date.shiftedBy(h))

        error_angle_minus = Rotation.distance(s_minus.shiftedBy(h).getAttitude().getRotation(),
                                              s0.getAttitude().getRotation())
        evolution_angle_minus = Rotation.distance(s_minus.getAttitude().getRotation(),
                                                  s0.getAttitude().getRotation())
        self.assertAlmostEqual(0.0, error_angle_minus, delta=1.0e-6 * evolution_angle_minus)

        error_angle_plus = Rotation.distance(s0.getAttitude().getRotation(),
                                             s_plus.shiftedBy(-h).getAttitude().getRotation())
        evolution_angle_plus = Rotation.distance(s0.getAttitude().getRotation(),
                                                 s_plus.getAttitude().getRotation())
        self.assertAlmostEqual(0.0, error_angle_plus, delta=1.0e-6 * evolution_angle_plus)

        spin0 = s0.getAttitude().getSpin()
        reference = AngularCoordinates.estimateRate(s_minus.getAttitude().getRotation(),
                                                    s_plus.getAttitude().getRotation(),
                                                    2 * h)
        self.assertAlmostEqual(0.0, spin0.subtract(reference).getNorm(), delta=1.0e-14)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OrekitFixedRateTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

