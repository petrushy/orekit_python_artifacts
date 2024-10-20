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
import os
from java.io import File
from orekit import JArray
from org.orekit.data import DataProvidersManager, ZipJarCrawler, DirectoryCrawler, DataContext
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

    with urlrequest.urlopen(url) as response, open(filename, 'wb') as out_file:
        print('Downloading file from:', url)
        shutil.copyfileobj(response, out_file)


def setup_orekit_curdir(filename='orekit-data.zip', from_pip_library=False):
    """Setup the java engine with orekit.

    This function loads the Orekit data from either:
        - A zip in the current directory (by default orekit-data.zip),
        - A folder,
        - From the `orekitdata` Python library, installable via pip (see below)
    depending on whether `filename` is the path to a file or to a folder, and whether from_pip_library is True or False

    The `orekitdata` library is installable with `pip install git+https://gitlab.orekit.org/orekit/orekit-data.git`

    Then the function sets up the Orekit DataProviders to access it.

    The JVM needs to be initiated prior to calling this function:

        orekit.initVM()

    Args:
        filename (str): Name of zip or folder with orekit data. Default filename is 'orekit-data.zip'
        from_pip_library (bool), default False: if True, will first try to load the data from the `orekitdata` python library

    """

    DM = DataContext.getDefault().getDataProvidersManager()

    data_load_from_library_sucessful = False
    if from_pip_library:
        try:
            import orekitdata
            datafile = File(orekitdata.__path__[0])
            if not datafile.exists():
                print(f"""Unable to find orekitdata library folder,
                      will try to load Orekit data using the folder or filename {filename}""")
            else:
                filename = orekitdata.__path__[0]
                data_load_from_library_sucessful = True
        except ImportError:
            print(f"""Failed to load orekitdata library.
                  Install with `pip install git+https://gitlab.orekit.org/orekit/orekit-data.git`
                  Will try to load Orekit data using the folder or filename {filename}""")

    if not data_load_from_library_sucessful:
        datafile = File(filename)
        if not datafile.exists():
            print('File or folder:', datafile.getAbsolutePath(), ' not found')
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
            return

    if os.path.isdir(filename):
        crawler = DirectoryCrawler(datafile)
    elif os.path.isfile(filename):
        crawler = ZipJarCrawler(datafile)
    else:
        print('filename ', filename, ' is neither a file nor a folder')
    DM.clearProviders()
    DM.clearLoadedDataNames()
    DM.resetFiltersToDefault()
    DM.addProvider(crawler)


def absolutedate_to_datetime(orekit_absolutedate):
    """ Converts from orekit.AbsoluteDate objects
    to python datetime objects (utc)"""

    utc = TimeScalesFactory.getUTC()
    or_comp = orekit_absolutedate.getComponents(utc)
    or_date = or_comp.getDate()
    or_time = or_comp.getTime()
    seconds = or_time.getSecond()
    seconds_int = int(math.floor(seconds))
    microseconds = int(1000000.0 * (seconds - math.floor(seconds)))
    if seconds_int > 59:  # This can take the value 60 during a leap second
        seconds_int = 59
        microseconds = 999999  # Also modifying microseconds to ensure that the time flow stays monotonic

    return datetime(or_date.getYear(),
                    or_date.getMonth(),
                    or_date.getDay(),
                    or_time.getHour(),
                    or_time.getMinute(),
                    seconds_int,
                    microseconds)


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
