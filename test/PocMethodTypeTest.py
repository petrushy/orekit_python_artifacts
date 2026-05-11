# -*- coding: utf-8 -*-
"""JCC port translated from Orekit's Java PocMethodTypeTest."""

import unittest

import orekit
orekit.initVM()

from org.orekit.files.ccsds.definitions import PocMethodType
from org.orekit.ssa.collision.shorttermencounter.probability.twod import ShortTermEncounter2DPOCMethodType


class PocMethodTypeTest(unittest.TestCase):

    def testConversionToCCSDSName(self):
        self.assertEqual("ALFANO-2005", PocMethodType.ALFANO_2005.getCCSDSName())
        self.assertEqual("CHAN-1997", PocMethodType.CHAN_1997.getCCSDSName())
        self.assertEqual("CHAN-2003", PocMethodType.CHAN_2003.getCCSDSName())

    def testShouldReturnNull(self):
        for method in (PocMethodType.AKELLAALFRIEND_2000,
                       PocMethodType.FOSTER_1992,
                       PocMethodType.PATERA_2001,
                       PocMethodType.PATERA_2003,
                       PocMethodType.CHAN_2003,
                       PocMethodType.ALFANO_TUBES_2007,
                       PocMethodType.ALFANO_VOXELS_2006,
                       PocMethodType.ALFANO_PARAL_2007,
                       PocMethodType.ALFANO_MAX_PROBABILITY,
                       PocMethodType.MCKINLEY_2006):
            self.assertIsNone(method.getMethodType())

    def testShouldReturnCorrespondingType(self):
        self.assertEqual(ShortTermEncounter2DPOCMethodType.CHAN_1997,
                         PocMethodType.CHAN_1997.getMethodType())
        self.assertEqual(ShortTermEncounter2DPOCMethodType.ALFRIEND_1999,
                         PocMethodType.ALFRIEND_1999.getMethodType())
        self.assertEqual(ShortTermEncounter2DPOCMethodType.ALFANO_2005,
                         PocMethodType.ALFANO_2005.getMethodType())
        self.assertEqual(ShortTermEncounter2DPOCMethodType.PATERA_2005,
                         PocMethodType.PATERA_2005.getMethodType())


if __name__ == '__main__':
    unittest.main()
