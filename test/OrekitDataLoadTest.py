import os
import orekit
from orekit.pyhelpers import setup_orekit_curdir, download_orekit_data_curdir
from org.orekit.utils import Constants

def test_load_data_from_library():
    orekit.initVM()
    setup_orekit_curdir(from_pip_library=True)
    assert(Constants.WGS84_EARTH_EQUATORIAL_RADIUS == 6378137.0)

def test_download_and_load_data():
    orekit.initVM()

    orekit_data_zip = 'orekit-data.zip'
    if os.path.isfile(orekit_data_zip):
        os.remove(orekit_data_zip)

    download_orekit_data_curdir(filename=orekit_data_zip)
    setup_orekit_curdir(filename=orekit_data_zip)
    assert(Constants.WGS84_EARTH_EQUATORIAL_RADIUS == 6378137.0)

    if os.path.isfile(orekit_data_zip):
        os.remove(orekit_data_zip)
