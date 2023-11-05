# Python orekit specifics
import sys
import orekit
orekit.initVM()



import unittest
from org.orekit.data import DataProvidersManager, ZipJarCrawler, DataContext, DirectoryCrawler
from java.io import File

from orekit import JArray_double
from orekit.pyhelpers import absolutedate_to_datetime
from org.hipparchus import CalculusFieldElement
from org.hipparchus.analysis.differentiation import GradientField, UnivariateDerivative1, UnivariateDerivative2
from org.hipparchus.complex import ComplexField
from org.hipparchus.geometry.euclidean.threed import FieldRotation, FieldVector3D, Rotation, Vector3D
from org.hipparchus.util import Binary64Field
from org.orekit.attitudes import GroundPointing, PythonGroundPointing
from org.orekit.frames import FramesFactory, Frame
from org.orekit.orbits import EquinoctialOrbit, FieldEquinoctialOrbit, PositionAngleType
from org.orekit.time import AbsoluteDate, FieldAbsoluteDate
from org.orekit.utils import IERSConventions, Constants, PVCoordinatesProvider, TimeStampedPVCoordinates, FieldPVCoordinatesProvider, TimeStampedFieldPVCoordinates, PVCoordinates, FieldPVCoordinates
import unittest
from org.hipparchus.analysis.differentiation import GradientField, UnivariateDerivative2


class TestGroundPointing(PythonGroundPointing):
    def getTargetPV(self, pvProv, date, frame) -> TimeStampedPVCoordinates|TimeStampedFieldPVCoordinates:
        if isinstance(pvProv, FieldPVCoordinatesProvider):
            return TimeStampedFieldPVCoordinates(date, FieldPVCoordinates.getZero(date.getField()))

        elif isinstance(pvProv, PVCoordinatesProvider):
            return TimeStampedPVCoordinates(date, PVCoordinates.ZERO)

        else:
            raise RuntimeError(f'Not supported type of PVCoordinatesProvider: {type(pvProv).__name__}')


class GroundPointingTest(unittest.TestCase):
    INERTIAL_FRAME = None
    OTHER_INERTIAL_FRAME = None
    EARTH_FIXED_FRAME = None

    def setUp(self):
        
        DM = DataContext.getDefault().getDataProvidersManager()
        datafile = File('../test/resources')
        if not datafile.exists():
            print('File :', datafile.absolutePath, ' not found')

        crawler = DirectoryCrawler(datafile)
        DM.clearProviders()
        DM.addProvider(crawler)
        self.INERTIAL_FRAME = FramesFactory.getEME2000()
        self.OTHER_INERTIAL_FRAME = FramesFactory.getGCRF()
        self.EARTH_FIXED_FRAME = FramesFactory.getITRF(IERSConventions.IERS_2010, True)

    def createPVCoordinatesProvider(self):
        epoch = AbsoluteDate.ARBITRARY_EPOCH
        semiMajorAxis = 45000.0e3
        mu = Constants.EGM96_EARTH_MU
        return EquinoctialOrbit(semiMajorAxis, 0., 0., 0., 0., 0., PositionAngleType.ECCENTRIC, self.INERTIAL_FRAME, epoch, mu)

    def templateTestGetRotation(self, frame):
        # setup
        groundPointing = TestGroundPointing(self.INERTIAL_FRAME, self.EARTH_FIXED_FRAME)
        orbit = self.createPVCoordinatesProvider()

        actualRotation = groundPointing.getAttitudeRotation(orbit, orbit.getDate(), frame)
        # verify
        attitude = groundPointing.getAttitude(orbit, orbit.getDate(), frame)
        expectedRotation = attitude.getRotation()
        self.assertEquals(0., Rotation.distance(expectedRotation, actualRotation))

    def testtemplateTestGetRotationRateSameFrame(self):
        self.templateTestGetRotation(self.INERTIAL_FRAME)

    def testtemplateTestGetRotationRateDifferentFrame(self):
        self.templateTestGetRotation(self.OTHER_INERTIAL_FRAME)

    def testGetAttitudeRotiationFieldSameFrame(self):
        self.templateTestGetRotationField(ComplexField.getInstance(), self.INERTIAL_FRAME)

    def testGetAttitudeRotiationFieldDifferentFrame(self):
        self.templateTestGetRotationField(UnivariateDerivative1(0., 0.).getField(), self.OTHER_INERTIAL_FRAME)

    def templateTestGetRotationField(self, field, frame):
        # GIVEN
        groundPointing = TestGroundPointing(self.INERTIAL_FRAME, self.EARTH_FIXED_FRAME)
        orbit = self.createPVCoordinatesProvider()
        fieldOrbit = self.convertToField(field, orbit)
        # WHEN
        actualRotation = groundPointing.getAttitudeRotation(fieldOrbit, fieldOrbit.getDate(), frame)
        # THEN
        attitude = groundPointing.getAttitude(fieldOrbit, fieldOrbit.getDate(), frame)
        expectedRotation = attitude.getRotation()
        assert 0. == Rotation.distance(expectedRotation.toRotation(), actualRotation.toRotation())


    def testGetAttitudeFieldGradient(self):
        self.templateTestGetAttitudeField(GradientField.getField(1))

    def testGetAttitudeFieldUnivariateDerivative2(self):
        self.templateTestGetAttitudeField(UnivariateDerivative2(0., 0., 0.).getField())



    def templateTestGetAttitudeField(self, field):
        groundPointing = TestGroundPointing(self.INERTIAL_FRAME, self.EARTH_FIXED_FRAME)
        orbit = self.createPVCoordinatesProvider()
        fieldOrbit = self.convertToField(field, orbit)
        actualAttitude = groundPointing.getAttitude(fieldOrbit, fieldOrbit.getDate(), self.OTHER_INERTIAL_FRAME).toAttitude()
        expectedAttitude = groundPointing.getAttitude(orbit, orbit.getDate(), self.OTHER_INERTIAL_FRAME)
        assert 0. == Rotation.distance(expectedAttitude.getRotation(), actualAttitude.getRotation())
        assert str(expectedAttitude.getSpin()) == str(actualAttitude.getSpin())
        assert str(expectedAttitude.getRotationAcceleration()) == str(actualAttitude.getRotationAcceleration())

    def convertToField(self, field, orbit) -> FieldEquinoctialOrbit:
        zero = field.getZero()
        fieldSemiMajorAxis = zero.add(orbit.getA())
        fieldDate = FieldAbsoluteDate(field, orbit.getDate())
        positionAngleType = PositionAngleType.MEAN
        fieldAngle = zero.add(orbit.getL(positionAngleType))
        return FieldEquinoctialOrbit(fieldSemiMajorAxis, zero, zero, zero, zero, fieldAngle, positionAngleType, orbit.getFrame(), fieldDate, zero.add(orbit.getMu()))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GroundPointingTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
