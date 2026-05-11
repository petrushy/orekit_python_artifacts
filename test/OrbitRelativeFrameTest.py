# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java OrbitRelativeFrameTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JavaError
from org.orekit.files.ccsds.definitions import OrbitRelativeFrame
from org.orekit.frames import LOF, LOFType


class OrbitRelativeFrameTest(unittest.TestCase):

    @staticmethod
    def isLofQuasiInertial(lof):
        # JCC exposes isQuasiInertial on the LOF interface, not directly on
        # the LOFType enum wrapper.
        return LOF.cast_(lof).isQuasiInertial()

    def assertSameOrbitRelativeFrame(self, initialCCSDSFrame, ccsdsFrameFromOrekitLOF):
        if initialCCSDSFrame in (OrbitRelativeFrame.RSW,
                                 OrbitRelativeFrame.QSW,
                                 OrbitRelativeFrame.RTN,
                                 OrbitRelativeFrame.RIC):
            self.assertEqual(OrbitRelativeFrame.RSW_INERTIAL, ccsdsFrameFromOrekitLOF)
        elif initialCCSDSFrame == OrbitRelativeFrame.LVLH:
            self.assertEqual(OrbitRelativeFrame.LVLH_INERTIAL, ccsdsFrameFromOrekitLOF)
        elif initialCCSDSFrame == OrbitRelativeFrame.TNW:
            self.assertEqual(OrbitRelativeFrame.TNW_INERTIAL, ccsdsFrameFromOrekitLOF)
        else:
            self.assertEqual(initialCCSDSFrame, ccsdsFrameFromOrekitLOF)

    def testOrbitRelativeFrameDefinitionsAndLOFTypeEquivalent(self):
        cases = (
            (OrbitRelativeFrame.LVLH_INERTIAL, LOFType.VVLH_INERTIAL),
            (OrbitRelativeFrame.LVLH_ROTATING, LOFType.VVLH),
            (OrbitRelativeFrame.LVLH, None),
            (OrbitRelativeFrame.NTW_ROTATING, None),
            (OrbitRelativeFrame.RSW_ROTATING, None),
            (OrbitRelativeFrame.RSW_INERTIAL, None),
            (OrbitRelativeFrame.RSW, None),
            (OrbitRelativeFrame.RIC, None),
            (OrbitRelativeFrame.RTN, None),
            (OrbitRelativeFrame.QSW, None),
            (OrbitRelativeFrame.TNW_ROTATING, None),
            (OrbitRelativeFrame.TNW_INERTIAL, None),
            (OrbitRelativeFrame.TNW, None),
            (OrbitRelativeFrame.VNC_ROTATING, None),
            (OrbitRelativeFrame.VNC_INERTIAL, None),
        )
        for ccsdsFrame, comparableLof in cases:
            lof = ccsdsFrame.getLofType()
            self.assertIsNotNone(lof)
            self.assertEqual(ccsdsFrame.isQuasiInertial(),
                             self.isLofQuasiInertial(lof))
            if comparableLof is not None:
                self.assertEqual(ccsdsFrame.isQuasiInertial(),
                                 self.isLofQuasiInertial(comparableLof))

        self.assertEqual(OrbitRelativeFrame.LVLH_ROTATING,
                         LOFType.VVLH.toOrbitRelativeFrame())
        self.assertIsNone(OrbitRelativeFrame.NSW_ROTATING.getLofType())
        self.assertIsNone(OrbitRelativeFrame.NSW_INERTIAL.getLofType())
        self.assertIsNone(OrbitRelativeFrame.PQW_INERTIAL.getLofType())
        self.assertIsNone(OrbitRelativeFrame.SEZ_ROTATING.getLofType())
        self.assertIsNone(OrbitRelativeFrame.SEZ_INERTIAL.getLofType())

    def testConversionFromToOrbitRelativeFrameToFromLOFType(self):
        for ccsdsFrame in OrbitRelativeFrame.values():
            orekitEquivalentLOF = ccsdsFrame.getLofType()
            if orekitEquivalentLOF is not None:
                ccsdsFrameFromOrekitLOF = orekitEquivalentLOF.toOrbitRelativeFrame()
                self.assertSameOrbitRelativeFrame(ccsdsFrame, ccsdsFrameFromOrekitLOF)

    def testErrorThrownWhenTryingToConvertLVLHLOFTypeToOrbitRelativeFrame(self):
        expected = "this LVLH local orbital frame uses a different definition, please use LVLH_CCSDS instead"
        for lof in (LOFType.LVLH, LOFType.LVLH_INERTIAL):
            with self.assertRaises(JavaError) as ctx:
                lof.toOrbitRelativeFrame()
            self.assertEqual(expected, ctx.exception.getJavaException().getMessage())


if __name__ == '__main__':
    unittest.main()
