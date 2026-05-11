# -*- coding: utf-8 -*-
"""
original copyright:

/* Copyright 2002-2024 CS GROUP
 * Licensed to CS GROUP (CS) under one or more
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

Python version translated from Java by Petrus Hyvönen and copilot, 2024.
JCC port adapted from the orekit_jpype version, 2026.
"""

import math
import os
import tempfile
import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.bodies import CelestialBodyFactory
from org.orekit.data import DataSource
from org.orekit.errors import OrekitException, OrekitIllegalArgumentException, OrekitMessages
from org.orekit.files.ccsds.definitions import CelestialBodyFrame
from org.orekit.files.ccsds.ndm import ParserBuilder, WriterBuilder
from org.orekit.files.ccsds.ndm.odm.opm import Opm, OpmWriter
from org.orekit.files.ccsds.utils.generation import KvnGenerator, MessageWriter
from org.orekit.frames import FramesFactory, LOFType
from org.orekit.orbits import PositionAngleType
from org.orekit.time import AbsoluteDate, TimeOffset, TimeScalesFactory
from org.orekit.utils import Constants, IERSConventions, PVCoordinates
# JCC's java.io wrapping in this build does not include CharArrayWriter;
# StringWriter implements the same Appendable interface that KvnGenerator expects.
from java.io import File, StringWriter


class OpmParserTest(unittest.TestCase):

    def assertDateEqual(self, expected, actual):
        """JCC's `__eq__` on wrapped Java objects is identity, not Java's
        `.equals()`. For AbsoluteDate, two distinct wrapper instances that
        represent the same moment compare as unequal. Use durationFrom()
        for a proper equality check."""
        self.assertEqual(0.0, actual.durationFrom(expected),
                         f"date mismatch: expected {expected}, got {actual}")

    def checkPVEntry(self, expected, actual):
        eps = 1e-12
        self.assertAlmostEqual(expected.getPosition().getX(), actual.getPosition().getX(), delta=eps)
        self.assertAlmostEqual(expected.getPosition().getY(), actual.getPosition().getY(), delta=eps)
        self.assertAlmostEqual(expected.getPosition().getZ(), actual.getPosition().getZ(), delta=eps)
        self.assertAlmostEqual(expected.getVelocity().getX(), actual.getVelocity().getX(), delta=eps)
        self.assertAlmostEqual(expected.getVelocity().getY(), actual.getVelocity().getY(), delta=eps)
        self.assertAlmostEqual(expected.getVelocity().getZ(), actual.getVelocity().getZ(), delta=eps)

    def testParseOPM1KVN(self):
        ex = "resources/ccsds/odm/opm/OPMExample1.txt"
        source = DataSource(File(ex))

        parser = ParserBuilder().withMu(398600e9).withDefaultMass(1000.0).buildOpmParser()
        # parseMessage is generic (T parseMessage(DataSource)); JCC returns
        # the erased Object. Cast back to Opm.
        file = Opm.cast_(parser.parseMessage(source))
        self.assertEqual(IERSConventions.IERS_2010, file.getConventions())

        # Header
        self.assertEqual(3.0, file.getHeader().getFormatVersion())
        self.assertDateEqual(AbsoluteDate(1998, 11, 6, 9, 23, 57.0, TimeScalesFactory.getUTC()),
                         file.getHeader().getCreationDate())
        self.assertEqual("JAXA", file.getHeader().getOriginator())

        # Metadata
        self.assertEqual("GODZILLA 5", file.getMetadata().getObjectName())
        self.assertEqual("1998-999A", file.getMetadata().getObjectID())
        self.assertEqual(1998, file.getMetadata().getLaunchYear())
        self.assertEqual(999, file.getMetadata().getLaunchNumber())
        self.assertEqual("A", file.getMetadata().getLaunchPiece())
        self.assertEqual("EARTH", file.getMetadata().getCenter().getName())
        self.assertIsNotNone(file.getMetadata().getCenter().getBody())
        self.assertEqual(CelestialBodyFactory.getEarth(), file.getMetadata().getCenter().getBody())
        self.assertEqual(CelestialBodyFrame.ITRF2000,
                         CelestialBodyFrame.map(file.getMetadata().getFrame()))
        self.assertEqual("UTC", file.getMetadata().getTimeSystem().name())
        self.assertIsNone(file.getData().getCovarianceBlock())

        # State Vector data
        self.assertDateEqual(AbsoluteDate(1998, 12, 18, 14, 28,
                                      TimeOffset(15, TimeOffset.SECOND,
                                                 117200, TimeOffset.MICROSECOND),
                                      TimeScalesFactory.getUTC()),
                         file.getDate())
        self.checkPVEntry(PVCoordinates(Vector3D(6503514.000, 1239647.000, -717490.000),
                                        Vector3D(-873.160, 8740.420, -4191.076)),
                          file.getPVCoordinates())

        # Three calls expected to throw OrekitIllegalArgumentException
        # (NON_PSEUDO_INERTIAL_FRAME) on a non-inertial frame.
        for accessor in (file.generateCartesianOrbit,
                         file.generateKeplerianOrbit,
                         file.generateSpacecraftState):
            with self.assertRaises(JavaError) as ctx:
                accessor()
            oiae = OrekitIllegalArgumentException.cast_(ctx.exception.getJavaException())
            self.assertEqual(OrekitMessages.NON_PSEUDO_INERTIAL_FRAME, oiae.getSpecifier())
            self.assertEqual("ITRF-2000/CIO/2010-based ITRF simple EOP", str(oiae.getParts()[0]))

    def testParseOPM2(self):
        ex = "resources/ccsds/odm/opm/OPMExample2.txt"
        source = DataSource(File(ex))

        parser = ParserBuilder().withMu(Constants.EIGEN5C_EARTH_MU).withDefaultMass(1000.0).buildOpmParser()
        # parseMessage is generic (T parseMessage(DataSource)); JCC returns
        # the erased Object. Cast back to Opm.
        file = Opm.cast_(parser.parseMessage(source))
        self.assertEqual(IERSConventions.IERS_2010, file.getConventions())

        # Header
        self.assertEqual(3.0, file.getHeader().getFormatVersion())
        headerComment = ["Generated by GSOC, R. Kiehling",
                         "Current intermediate orbit IO2 and maneuver planning data"]
        self.assertEqual(headerComment, list(file.getHeader().getComments()))
        self.assertDateEqual(AbsoluteDate(2000, 6, 3, 5, 33, 0.0, TimeScalesFactory.getUTC()),
                         file.getHeader().getCreationDate())
        self.assertEqual("GSOC", file.getHeader().getOriginator())

        # Metadata
        self.assertEqual("EUTELSAT W4", file.getMetadata().getObjectName())
        self.assertEqual("2000-028A", file.getMetadata().getObjectID())
        self.assertEqual("EARTH", file.getMetadata().getCenter().getName())
        self.assertIsNotNone(file.getMetadata().getCenter().getBody())
        self.assertEqual(CelestialBodyFactory.getEarth(), file.getMetadata().getCenter().getBody())
        self.assertEqual(FramesFactory.getTOD(IERSConventions.IERS_2010, True),
                         file.getMetadata().getFrame())
        self.assertEqual("UTC", file.getMetadata().getTimeSystem().name())
        self.assertEqual(0, file.getMetadata().getComments().size())

        # State Vector
        self.assertEqual(["State Vector"],
                         list(file.getData().getStateVectorBlock().getComments()))
        self.assertDateEqual(AbsoluteDate(2006, 6, 3, 0, 0, 0.0, TimeScalesFactory.getUTC()),
                         file.getDate())
        self.checkPVEntry(PVCoordinates(Vector3D(6655994.2, -40218575.1, -82917.7),
                                        Vector3D(3115.48208, 470.42605, -1.01495)),
                          file.getPVCoordinates())

        # Keplerian
        keplerianElements = file.getData().getKeplerianElementsBlock()
        self.assertIsNotNone(keplerianElements)
        self.assertEqual(["Keplerian elements"], list(keplerianElements.getComments()))
        self.assertAlmostEqual(41399512.3, keplerianElements.getA())
        self.assertAlmostEqual(0.020842611, keplerianElements.getE())
        self.assertAlmostEqual(math.radians(0.117746), keplerianElements.getI())
        self.assertAlmostEqual(math.radians(17.604721), keplerianElements.getRaan())
        self.assertAlmostEqual(math.radians(218.242943), keplerianElements.getPa())
        self.assertEqual(PositionAngleType.TRUE, keplerianElements.getAnomalyType())
        self.assertAlmostEqual(math.radians(41.922339), keplerianElements.getAnomaly())
        self.assertAlmostEqual(398600.4415 * 1e9, keplerianElements.getMu())

        # Spacecraft
        spacecraftParameters = file.getData().getSpacecraftParametersBlock()
        self.assertIsNotNone(spacecraftParameters)
        self.assertEqual(["Spacecraft parameters"], list(spacecraftParameters.getComments()))
        self.assertAlmostEqual(1913.000, spacecraftParameters.getMass())
        self.assertAlmostEqual(10.000, spacecraftParameters.getSolarRadArea())
        self.assertAlmostEqual(1.300, spacecraftParameters.getSolarRadCoeff())
        self.assertAlmostEqual(10.000, spacecraftParameters.getDragArea())
        self.assertAlmostEqual(2.300, spacecraftParameters.getDragCoeff())

        self.assertIsNone(file.getData().getCovarianceBlock())

        # Maneuvers
        self.assertTrue(file.getData().hasManeuvers())
        self.assertEqual(2, file.getNbManeuvers())
        stateManeuverComment0 = ["2 planned maneuvers", "First maneuver: AMF-3",
                                 "Non-impulsive, thrust direction fixed in inertial frame"]
        self.assertEqual(stateManeuverComment0, list(file.getManeuver(0).getComments()))
        self.assertDateEqual(AbsoluteDate(2000, 6, 3, 9, 0,
                                      TimeOffset(34, TimeOffset.SECOND, 100, TimeOffset.MILLISECOND),
                                      TimeScalesFactory.getUTC()),
                         file.getManeuvers().get(0).getEpochIgnition())
        self.assertEqual(132.6, file.getManeuver(0).getDuration())
        self.assertEqual(-18.418, file.getManeuver(0).getDeltaMass())
        self.assertIsNone(file.getManeuver(0).getReferenceFrame().asOrbitRelativeFrame())
        self.assertEqual(FramesFactory.getEME2000(),
                         file.getManeuver(0).getReferenceFrame().asFrame())
        self.assertAlmostEqual(0.0,
                               Vector3D(-23.25700, 16.83160, -8.93444)
                                   .distance(file.getManeuver(0).getDV()))

        stateManeuverComment1 = ["Second maneuver: first station acquisition maneuver",
                                 "impulsive, thrust direction fixed in RTN frame"]
        self.assertEqual(stateManeuverComment1, list(file.getManeuver(1).getComments()))
        self.assertDateEqual(AbsoluteDate(2000, 6, 5, 18, 59, 21.0, TimeScalesFactory.getUTC()),
                         file.getManeuvers().get(1).getEpochIgnition())
        self.assertEqual(0.0, file.getManeuver(1).getDuration())
        self.assertEqual(-1.469, file.getManeuver(1).getDeltaMass())
        self.assertEqual(LOFType.QSW_INERTIAL,
                         file.getManeuver(1).getReferenceFrame().asOrbitRelativeFrame().getLofType())
        self.assertIsNone(file.getManeuver(1).getReferenceFrame().asFrame())
        self.assertIsNone(file.getManeuver(1).getReferenceFrame().asCelestialBodyFrame())
        self.assertAlmostEqual(0.0,
                               Vector3D(1.015, -1.873, 0.0)
                                   .distance(file.getManeuver(1).getDV()))

        self.assertIsNone(file.getData().getUserDefinedBlock())
        self.assertIsNotNone(file.generateCartesianOrbit())
        self.assertIsNotNone(file.generateKeplerianOrbit())
        self.assertIsNotNone(file.generateSpacecraftState())

    def testWrongODMType(self):
        name = "resources/ccsds/odm/omm/OMMExample1.txt"
        source = DataSource(File(name))
        with self.assertRaises(JavaError) as ctx:
            ParserBuilder().withMu(Constants.EIGEN5C_EARTH_MU).withDefaultMass(1000.0) \
                .buildOpmParser().parseMessage(source)
        oe = OrekitException.cast_(ctx.exception.getJavaException())
        self.assertEqual(OrekitMessages.UNSUPPORTED_FILE_FORMAT, oe.getSpecifier())
        # getParts()[0] is typed as Object in JCC; coerce to str for comparison.
        self.assertEqual(name.split('/')[-1], str(oe.getParts()[0]))

    def testParseOPM3KVN(self):
        name = "resources/ccsds/odm/opm/OPMExample3.txt"
        source = DataSource(File(name))
        parser = ParserBuilder().withDefaultMass(1000.0).buildOpmParser()
        # parseMessage is generic (T parseMessage(DataSource)); JCC returns
        # the erased Object. Cast back to Opm.
        file = Opm.cast_(parser.parseMessage(source))
        self.assertEqual("OPM 201113719185", file.getHeader().getMessageId())
        self.assertEqual(CelestialBodyFrame.TOD,
                         file.getMetadata().getReferenceFrame().asCelestialBodyFrame())
        self.assertDateEqual(AbsoluteDate(1998, 12, 18, 14, 28,
                                      TimeOffset(15, TimeOffset.SECOND,
                                                 117200, TimeOffset.MICROSECOND),
                                      TimeScalesFactory.getUTC()),
                         file.getMetadata().getFrameEpoch())
        # Use .size(); JCC's wrapper for the List interface returned here
        # does not implement Python's __len__.
        self.assertEqual(1, file.getMetadata().getComments().size())
        self.assertEqual("GEOCENTRIC, CARTESIAN, EARTH FIXED",
                         file.getMetadata().getComments().get(0))
        # Note: jpype version had a "TODO HOW CAN THIS DIFFER SO MUCH" — kept loose tolerance.
        self.assertAlmostEqual(15951238.3495, file.generateKeplerianOrbit().getA(), places=0)
        self.assertAlmostEqual(0.5914452565, file.generateKeplerianOrbit().getE(), delta=1.0e-7)

        covariance = file.getData().getCovarianceBlock()
        self.assertIsNotNone(covariance)
        self.assertEqual(file.getMetadata().getReferenceFrame(), covariance.getReferenceFrame())
        covMatrix = [
            [333.1349476038534, 461.8927349220216, -307.0007847730449,
             -0.3349365033922630, -0.2211832501084875, -0.3041346050686871],
            [461.8927349220216, 678.2421679971363, -422.1234189514228,
             -0.4686084221046758, -0.2864186892102733, -0.4989496988610662],
            [-307.0007847730449, -422.1234189514228, 323.1931992380369,
             0.2484949578400095, 0.1798098699846038, 0.3540310904497689],
            [-0.3349365033922630, -0.4686084221046758, 0.2484949578400095,
             0.0004296022805587290, 0.0002608899201686016, 0.0001869263192954590],
            [-0.2211832501084875, -0.2864186892102733, 0.1798098699846038,
             0.0002608899201686016, 0.0001767514756338532, 0.0001008862586240695],
            [-0.3041346050686871, -0.4989496988610662, 0.3540310904497689,
             0.0001869263192954590, 0.0001008862586240695, 0.0006224444338635500],
        ]
        for i in range(6):
            for j in range(6):
                self.assertAlmostEqual(covMatrix[i][j],
                                       covariance.getCovarianceMatrix().getEntry(i, j),
                                       delta=1e-15)

    def testWriteOPM3(self):
        # Round-trip: parse OPM3.xml, write it back, re-parse, validate.
        # The jpype original uses an in-memory ByteArrayInputStream wrapped
        # in a Python class implementing DataSource.StreamOpener (via
        # @JImplements). JCC has no PythonStreamOpener bridge and cannot
        # implement the Java functional interface from Python, so this
        # port writes the rebuilt content to a temp file and reads it back
        # via DataSource(File). The parsing path being exercised is
        # identical.
        name = "resources/ccsds/odm/opm/OPMExample3.xml"
        source = DataSource(File(name))
        parser = ParserBuilder().withDefaultMass(1000.0).buildOpmParser()
        original = Opm.cast_(parser.parseMessage(source))

        caw = StringWriter()
        generator = KvnGenerator(caw, OpmWriter.KVN_PADDING_WIDTH, "dummy",
                                 Constants.JULIAN_DAY, 60)
        # writeMessage is a non-abstract method on the MessageWriter
        # interface; JCC doesn't dispatch interface defaults on subclasses,
        # so cast OpmWriter to MessageWriter first.
        MessageWriter.cast_(WriterBuilder().buildOpmWriter()) \
            .writeMessage(generator, original)

        text = str(caw.toString())
        with tempfile.NamedTemporaryFile(mode='w', suffix='.kvn',
                                         delete=False) as tmp:
            tmp.write(text)
            tmp_path = tmp.name
        try:
            source2 = DataSource(File(tmp_path))
            rebuilt = Opm.cast_(ParserBuilder().buildOpmParser().parseMessage(source2))
            self.validateOPM3XML(rebuilt)
        finally:
            os.remove(tmp_path)

    def validateOPM3XML(self, file):
        self.assertEqual("OPM 201113719185", file.getHeader().getMessageId())
        self.assertEqual(CelestialBodyFrame.TOD,
                         file.getMetadata().getReferenceFrame().asCelestialBodyFrame())
        self.assertDateEqual(AbsoluteDate(1998, 12, 18, 14, 28,
                                      TimeOffset(15, TimeOffset.SECOND,
                                                 117200, TimeOffset.MICROSECOND),
                                      TimeScalesFactory.getUTC()),
                         file.getMetadata().getFrameEpoch())
        # Use .size(); JCC's wrapper for the List interface returned here
        # does not implement Python's __len__.
        self.assertEqual(1, file.getMetadata().getComments().size())
        self.assertEqual("GEOCENTRIC, CARTESIAN, EARTH FIXED",
                         file.getMetadata().getComments().get(0))
        self.assertAlmostEqual(15951238.3495, file.generateKeplerianOrbit().getA(), places=0)
        self.assertAlmostEqual(0.5914452565, file.generateKeplerianOrbit().getE(), delta=1.0e-7)
        covariance = file.getData().getCovarianceBlock()
        self.assertIsNotNone(covariance)
        self.assertEqual(CelestialBodyFrame.ITRF1997,
                         covariance.getReferenceFrame().asCelestialBodyFrame())

        covMatrix = [
            [316000.0, 722000.0, 202000.0, 912000.0, 562000.0, 245000.0],
            [722000.0, 518000.0, 715000.0, 306000.0, 899000.0, 965000.0],
            [202000.0, 715000.0,  2000.0, 276000.0,  22000.0, 950000.0],
            [912000.0, 306000.0, 276000.0, 797000.0,  79000.0, 435000.0],
            [562000.0, 899000.0,  22000.0,  79000.0, 415000.0, 621000.0],
            [245000.0, 965000.0, 950000.0, 435000.0, 621000.0, 991000.0],
        ]
        for i in range(6):
            for j in range(6):
                self.assertAlmostEqual(covMatrix[i][j],
                                       covariance.getCovarianceMatrix().getEntry(i, j),
                                       delta=1e-15)


if __name__ == '__main__':
    unittest.main()
