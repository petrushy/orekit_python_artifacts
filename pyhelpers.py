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

# This document contains classes that are useful for using the orekit
# library in Python.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
from datetime import datetime

import math
from java.io import File
from orekit import JArray
from org.orekit.data import DataProvidersManager, ZipJarCrawler
from org.orekit.time import TimeScalesFactory, AbsoluteDate
from org.orekit.utils import ElevationMask


try:
    import urllib.request as urlrequest
except ImportError:
    import urllib as urlrequest


def download_orekit_data_curdir(filename='orekit-data.zip'):
    """
    Orekit needs a number of orientation and model parameters. An example file is available on the
    orekit gitlab. This funciton downloads that file to the current directory.

    Note that for non-testing purposes, this file should

    Args:
        filename (str): Store the downloaded data as this filename/path. Default is "orekit-data.zip"
    """
    url = "https://gitlab.orekit.org/orekit/orekit-data/-/archive/master/orekit-data-master.zip"
    # Download the orekit-data file and store it locally

    with urlrequest.urlopen(url) as response, open("orekit-data.zip", 'wb') as out_file:
        print('Downloading file from:', url)
        shutil.copyfileobj(response, out_file)


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
        print("""
        
        The Orekit library relies on some external data for physical models. 
        Typical data are the Earth Orientation Parameters and the leap seconds history, 
        both being provided by the IERS or the planetary ephemerides provided by JPL. 
        Such data is stored in text or binary files with specific formats that Orekit knows 
        how to read, and needs to be provided for the library to work.
        
        You can download a starting file with this data from the orekit gitlab at:
        https://gitlab.orekit.org/orekit/orekit-data
        
        or by the function:
        orekit.pyhelpers.download_orekit_data_curdir()
        
        """)

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
