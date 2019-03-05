# encoding: utf-8

#   Copyright 2014 SSC
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" This document contains classes that are useful for using the orekit
library in Python. """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Set up the orekit namespace
import orekit

from java.io import File

from org.orekit.data import DataProvidersManager, ZipJarCrawler
from org.orekit.time import TimeScalesFactory, AbsoluteDate
from org.orekit.utils import ElevationMask
from orekit import JArray

import math
from datetime import datetime


def setup_orekit_curdir(filename='orekit-data.zip'):
    """Setup the java engine with orekit.

    This function loads the orekit-data.zip from the current directory
    and sets up the Orekit DataProviders to access it.

    The JVM needs to be initiated prior to calling this function:

        orekit.initVM()

    Args:
        filename (str): Name of zip with orekit data. Default filename is 'orekit-data.zip'

    """

    DM = DataProvidersManager.getInstance()
    datafile = File(filename)
    if not datafile.exists():
        print('File :', datafile.absolutePath, ' not found')

    crawler = ZipJarCrawler(datafile)
    DM.clearProviders()
    DM.addProvider(crawler)


def absolutedate_to_datetime(orekit_absolutedate):
    """ Converts from orekit.AbsoluteDate objects
    to python datetime objects (utc)"""

    utc = TimeScalesFactory.getUTC()
    or_comp = orekit_absolutedate.getComponents(utc)
    or_date = or_comp.getDate()
    or_time = or_comp.getTime()
    seconds = or_time.getSecond()
    return datetime(or_date.getYear(),
                    or_date.getMonth(),
                    or_date.getDay(),
                    or_time.getHour(),
                    or_time.getMinute(),
                    int(math.floor(seconds)),
                    int(1000000.0 * (seconds - math.floor(seconds))))


def datetime_to_absolutedate(dt_date):
    """ Converts from python datetime objects (utc)
    to orekit.AbsoluteDate objects.

    Args:
        dt_date (datetime): python datetime object to convert

    Returns:
        AbsoluteDate: time in orekit format"""

    utc = TimeScalesFactory.getUTC()
    return AbsoluteDate(dt_date.year,
                        dt_date.month,
                        dt_date.day,
                        dt_date.hour,
                        dt_date.minute,
                        dt_date.second + dt_date.microsecond / 1000000.,
                        utc)


def to_elevationmask(az, el):
    """ Converts an array of azimuths and elevations to a
    orekit ElevationMask object. All unts in degrees.

        mask = to_elevationmask([0, 90, 180, 270], [5,10,8,5])

    """

    mask = JArray('object')(len(az))

    for i in range(len(az)):
        mask[i] = JArray('double')([math.radians(az[i]),
                                    math.radians(el[i])])

    return ElevationMask(mask)


def JArray_double2D(x, y):
    """Returns an JCC wrapped 2D double array

    Args:
        x: Number of rows in the array
        y: Number of columns in the array

    Note that the rows and columns are returned as objects and
    are likely needed to be casted manually.
    """

    arr = JArray('object')(x)

    for i in range(x):
        arr[i] = JArray('double')(y)

    return arr
