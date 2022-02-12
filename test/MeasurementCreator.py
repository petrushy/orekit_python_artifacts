"""/* Copyright 2002-2022 CS GROUP
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

  Python version translated from Java by Petrus Hyvönen, SSC 2022
 """

import math
import sys
import unittest

# Python orekit specifics
import orekit
orekit.initVM()

#from org.orekit.estimation.measurements
from org.orekit.propagation.sampling import PythonOrekitFixedStepHandler

class MeasurementCreator(PythonOrekitFixedStepHandler):

    def init(self, s0, t, step):
        self.measurements = []

    def addMeasurement(self, measurement):
        self.measurements.append(measurement)

    def getMeasurements(self):
        return self.measurements

    #def handleStep(self, currentState):
    #    pass

    def finish(self, finalState):
        pass
