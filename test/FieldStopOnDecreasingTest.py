# -*- coding: utf-8 -*-


"""
/* Copyright 2002-2018 CS Systèmes d'Information
 * Licensed to CS Systèmes d'Information (CS) under one or more
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

 Python version translated from Java by Petrus Hyvönen, SSC 2019

"""

import sys
import unittest

# Python orekit specifics
import orekit

orekit.initVM()

from org.orekit.frames import FramesFactory
from org.orekit.propagation import FieldSpacecraftState
from org.orekit.time import FieldAbsoluteDate
from org.hipparchus.util import Decimal64Field
from org.orekit.orbits import FieldKeplerianOrbit
from org.orekit.orbits import PositionAngle
from org.orekit.utils import Constants
from org.orekit.propagation.events.handlers import FieldStopOnDecreasing
from org.orekit.propagation.events.handlers import FieldEventHandler
from org.hipparchus.ode.events import Action


class FieldStopOnDecreasingTest(unittest.TestCase):

    def testNoReset(self):
        self.doTestNoReset(Decimal64Field.getInstance())

    def testIncreasing(self):
        self.doTestIncreasing(Decimal64Field.getInstance())

    # def testDecreasing(self):
    #    self.doTestDecreasing(Decimal64Field.getInstance())

    def doTestNoReset(self, field):
        zero = field.getZero()
        date = FieldAbsoluteDate(field)
        s = FieldSpacecraftState(FieldKeplerianOrbit(zero.add(24464560.0),
                                                     zero.add(0.7311),
                                                     zero.add(0.122138),
                                                     zero.add(3.10686),
                                                     zero.add(1.00681),
                                                     zero.add(0.048363),
                                                     PositionAngle.MEAN,
                                                     FramesFactory.getEME2000(),
                                                     date,
                                                     zero.add(Constants.EIGEN5C_EARTH_MU)))

        handler = FieldStopOnDecreasing()
        handler_casted = FieldEventHandler.cast_(handler)
        s2 = handler_casted.resetState(None, s)

        self.assertEqual(s, s2)

    def doTestIncreasing(self, field):
        zero = field.getZero()
        date = FieldAbsoluteDate(field)
        s = FieldSpacecraftState(FieldKeplerianOrbit(zero.add(24464560.0),
                                                     zero.add(0.7311),
                                                     zero.add(0.122138),
                                                     zero.add(3.10686),
                                                     zero.add(1.00681),
                                                     zero.add(0.048363),
                                                     PositionAngle.MEAN,
                                                     FramesFactory.getEME2000(),
                                                     date,
                                                     zero.add(Constants.EIGEN5C_EARTH_MU)))

        handler = FieldStopOnDecreasing()
        handler_casted = FieldEventHandler.cast_(handler)
        event = handler_casted.eventOccurred(s, None, True)

        self.assertEqual(Action.CONTINUE, event)



"""

    private <T extends RealFieldElement<T>> void doTestDecreasing(Field<T> field) {
        T zero = field.getZero();
        FieldAbsoluteDate<T> date = new FieldAbsoluteDate<>(field);
        FieldSpacecraftState<T> s = new FieldSpacecraftState<>(new FieldKeplerianOrbit<>(zero.add(24464560.0),
                                                                                         zero.add(0.7311),
                                                                                         zero.add(0.122138),
                                                                                         zero.add(3.10686),
                                                                                         zero.add(1.00681),
                                                                                         zero.add(0.048363),
                                                                                         PositionAngle.MEAN,
                                                                                         FramesFactory.getEME2000(),
                                                                                         date,
                                                                                         Constants.EIGEN5C_EARTH_MU));
        Assert.assertSame(FieldEventHandler.Action.STOP, new FieldStopOnDecreasing<FieldEventDetector<T>, T>().eventOccurred(s, null, false));
    }

}
"""
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FieldStopOnDecreasingTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
