# -*- coding: utf-8 -*-

"""

/* Copyright 2002-2019 CS Syst��mes d'Information
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

Python version translated from Java by Olivier Podevin, CS Group 2020

 """

import orekit

orekit.initVM()
from orekit.pyhelpers import setup_orekit_curdir, datetime_to_absolutedate

setup_orekit_curdir()

import unittest
import sys
import os
import math
from datetime import datetime

from java.util import ArrayList, List, HashMap, Map
from java.lang import Double, StringBuffer
from java.io import BufferedReader, StringReader

from org.hipparchus.geometry.euclidean.threed import Rotation, Vector3D

from org.orekit.attitudes import AttitudeProvider, InertialProvider
from org.orekit.bodies import CelestialBodyFactory
from org.orekit.files.ccsds import AEMParser, AEMWriter, AEMFile, Keyword, StreamingAemWriter
from org.orekit.frames import FramesFactory
from org.orekit.orbits import CartesianOrbit
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.time import AbsoluteDate, TimeScalesFactory, TimeScale
from org.orekit.utils import IERSConventions, PVCoordinates

class AEMTest(unittest.TestCase):

    def testAemParsing(self):
        """Test the parsing of an AEM file functionality"""
        inFilename = "./resources/ccsds/AEMExample.txt"
        aemParser = AEMParser()
        aemParser = aemParser.withMu(CelestialBodyFactory.getEarth().getGM()). \
                    withConventions(IERSConventions.IERS_2010). \
                    withSimpleEOP(True)
        aemFile = aemParser.parse(inFilename)
        
        ####### Checks

        # Start date
        startRef = datetime_to_absolutedate(datetime(1996, 11, 28, 22, 8, 2, 555500))
        startFile = aemFile.getSatellites().get("1996-062A").getStart()
        # print("start ref=" + startRef.toString() + ", type=" + str(type(startRef)))
        # print("start file=" + startFile.toString() + ", type=" + str(type(startFile)))
        # print("delta=" + str(startRef.durationFrom(startFile)))
        self.assertTrue(math.isclose(startRef.durationFrom(startFile), 0, rel_tol=0.0, abs_tol=Double.MIN_VALUE))

        # Stop date
        stopRef = datetime_to_absolutedate(datetime(1996, 12, 28, 21, 23, 0, 555500))
        stopFile = aemFile.getSatellites().get("1996-062A").getStop()
        self.assertTrue(math.isclose(stopRef.durationFrom(stopFile), 0, rel_tol=0.0, abs_tol=Double.MIN_VALUE))

    def testAemWriting(self):
        """Test the writing of an AEM file functionality"""
        inFilename = "./resources/ccsds/AEMExample.txt"

        aemParser = AEMParser()
        aemParser = aemParser.withMu(CelestialBodyFactory.getEarth().getGM()) \
        .withConventions(IERSConventions.IERS_2010)

        aemFile = aemParser.parse(inFilename)
        
        ####### Read values
        originator = aemFile.getOriginator()
        objectName = aemFile.getAttitudeBlocks().get(0).getMetaData().getObjectName()
        objectID   = aemFile.getAttitudeBlocks().get(0).getMetaData().getObjectID()

        ####### Create AEM file
        outputDir = "./output/ccsds"
        tempFilename = "TestWriteAEM1.aem"
        tempAEMFilePath = os.path.join(outputDir, tempFilename)

        # Create output dir if needed
        if (not os.path.isdir(outputDir)):
            os.makedirs(outputDir)

        aemWriter = AEMWriter(originator, objectID, objectName)
        aemWriter.write(tempAEMFilePath, aemFile)

        ####### Checks
        generatedAemFile = aemParser.parse(tempAEMFilePath)
        originatorOut = aemFile.getOriginator()
        objectNameOut = aemFile.getAttitudeBlocks().get(0).getMetaData().getObjectName()
        objectIDOut   = aemFile.getAttitudeBlocks().get(0).getMetaData().getObjectID()

        self.assertEqual(originator, originatorOut)
        self.assertEqual(objectName, objectNameOut)
        self.assertEqual(objectID, objectIDOut)
        
    def testAemStreamWriting(self):
        """Test the stream writing of an AEM file functionality""" 

        QUATERNION_PRECISION = 1e-5
        DATE_PRECISION = 1e-3

        # Time scale
        utc = TimeScalesFactory.getUTC()

        inFilename = "./resources/ccsds/AEMExample.txt"

        # Create a list of files
        files = ["./resources/ccsds/AEMExample7.txt"]

        for ex in files:
            # Reference AEM file
            aemParser = AEMParser()
            aemParser = aemParser.withMu(CelestialBodyFactory.getEarth().getGM()) \
            .withConventions(IERSConventions.IERS_2010)

            aemFile = aemParser.parse(ex)

            # Satellite attitude ephemeris as read from the reference file
            satellite = aemFile.getSatellites().values().iterator().next()

            # Meta data are extracted from the reference file
            originator   = aemFile.getOriginator()
            objectName   = satellite.getSegments().get(0).getMetaData().getObjectName()
            objectID     = satellite.getSegments().get(0).getMetaData().getObjectID()
            headerCmt    = aemFile.getHeaderComment().get(0)
            attitudeDir  = satellite.getSegments().get(0).getAttitudeDirection()
            refFrameA    = satellite.getSegments().get(0).getRefFrameAString()
            refFrameB    = satellite.getSegments().get(0).getRefFrameBString()
            attitudeType = satellite.getSegments().get(0).getAttitudeType()
            isFirst      = "LAST"

            metadata = HashMap()
            metadata.put(Keyword.ORIGINATOR,  originator)
            metadata.put(Keyword.OBJECT_NAME, "will be overwritten")
            metadata.put(Keyword.OBJECT_ID,   objectID)
            metadata.put(Keyword.COMMENT,     headerCmt)

            segmentData = HashMap()
            segmentData.put(Keyword.OBJECT_NAME,     objectName)
            segmentData.put(Keyword.ATTITUDE_DIR,    attitudeDir)
            segmentData.put(Keyword.QUATERNION_TYPE, isFirst)
            segmentData.put(Keyword.ATTITUDE_TYPE,   attitudeType)
            segmentData.put(Keyword.REF_FRAME_A,     refFrameA)
            segmentData.put(Keyword.REF_FRAME_B,     refFrameB.replace(' ', '_'))

            # Initialize a Keplerian propagator with an Inertial attitude provider
            # It is expected that all attitude data lines will have the same value
            buffer = StringBuffer()
            streamingAemWriter = StreamingAemWriter(buffer, utc, metadata)
            streamingAemWriter.writeHeader()
            segment = streamingAemWriter.newSegment(segmentData)
            
            #### Create a Keplerian propagator. 
            startingDate = satellite.getSegments().get(0).getStart()
            attitudeProvider = InertialProvider(satellite.getSegments().get(0).getAngularCoordinates().get(0).getRotation(), \
                FramesFactory.getEME2000())
            position = Vector3D(-29536113.0, 30329259.0, -100125.0)
            velocity = Vector3D(-2194.0, -2141.0, -8.0)
            pvCoordinates = PVCoordinates( position, velocity)
            mu = 3.9860047e14
            cartesianOrbit = CartesianOrbit(pvCoordinates, FramesFactory.getEME2000(), startingDate, mu)
            propagator = KeplerianPropagator(cartesianOrbit, attitudeProvider)

            # We propagate 60 seconds after the start date with a step equals to 10.0 seconds
            # It is expected to have an attitude data block containing 7 data lines
            step = 10.0
            propagator.setMasterMode(step, segment)
            propagator.propagate(satellite.getSegments().get(0).getStart().shiftedBy(60.0))

            # Generated AEM file
            reader = BufferedReader(StringReader(buffer.toString()))
            generatedAemFile = aemParser.parse(reader, "buffer")

            # There is only one attitude ephemeris block
            self.assertEqual(1, generatedAemFile.getAttitudeBlocks().size())
            # There are 7 data lines in the attitude ephemeris block
            ac  = generatedAemFile.getAttitudeBlocks().get(0).getAngularCoordinates()
            self.assertEqual(7, ac.size())

            # Verify
            i = 0
            while (i < 7):
                #self.assertEqual(step * i, ac.get(i).getDate().durationFrom(satellite.getSegments().get(0).getStart()), DATE_PRECISION)
                self.assertTrue(math.isclose(step * i, ac.get(i).getDate().durationFrom(satellite.getSegments().get(0).getStart()), rel_tol=0.0, abs_tol=DATE_PRECISION))
                rot = ac.get(i).getRotation()
                self.assertTrue(math.isclose(0.68427, rot.getQ0(), rel_tol=0.0, abs_tol=QUATERNION_PRECISION))
                self.assertTrue(math.isclose(0.56748, rot.getQ1(), rel_tol=0.0, abs_tol=QUATERNION_PRECISION))
                self.assertTrue(math.isclose(0.03146, rot.getQ2(), rel_tol=0.0, abs_tol=QUATERNION_PRECISION))
                self.assertTrue(math.isclose(0.45689, rot.getQ3(), rel_tol=0.0, abs_tol=QUATERNION_PRECISION))
                i += 1

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AEMTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
