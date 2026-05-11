# -*- coding: utf-8 -*-
"""
JCC port of orekit_jpype's test/PyhelpersTest.py.

Partial port — the JCC pyhelpers does NOT include the following helpers
that the jpype version tests:

  * `clear_factories` / `clear_factory_maps` — would need adding
    `java.lang.reflect.Field` and `java.lang.reflect.Modifier` to the
    JCC wrapping list in `orekit-feedstock/recipe/build.sh`. Deferred.
  * Numpy-aware `JArray_double2D(np_array)` — JCC's `JArray_double2D`
    keeps the legacy `(rows, cols)` signature. Skipped.
  * Numpy-vectorised `to_elevationmask` — depends on the numpy
    `JArray_double2D`. Skipped.

The translated tests below cover only the parts of `pyhelpers.py` that
exist in JCC: `setup_orekit_data`, `setup_orekit_curdir`, and
`download_orekit_data_curdir`.

See `test/TESTS_INVENTORY.md` for the partial-translation policy.
"""

import os
import unittest

import orekit
orekit.initVM()

from orekit.pyhelpers import (
    download_orekit_data_curdir,
    setup_orekit_curdir,
    setup_orekit_data,
)

from java.io import File


def _check_orekit_data_valid():
    """True if a recent UTC-TAI leap second is loaded (sentinel for valid data)."""
    from org.orekit.time import TimeScalesFactory
    utc = TimeScalesFactory.getUTC()
    last_leap_second = utc.getLastKnownLeapSecond()
    return last_leap_second.getComponents(utc).getDate().getYear() >= 2016


class PyhelpersTest(unittest.TestCase):

    def test_setup_orekit_data_from_folder(self):
        # Use the curated subset; the full `resources/` tree has a
        # documented EOP-gap problem (see CLAUDE.md). Leap-second loading
        # only needs UTC-TAI.history which is in regular-data/.
        setup_orekit_data(filenames="resources/regular-data", from_pip_library=False)
        self.assertTrue(_check_orekit_data_valid())

    def test_setup_orekit_data_from_invalid_folder(self):
        filename = "wrong_folder"
        datafile = File(filename)
        self.assertFalse(datafile.exists())

        with self.assertRaises(FileNotFoundError) as ctx:
            setup_orekit_data(filenames=filename, from_pip_library=False)

        self.assertEqual(str(ctx.exception), datafile.getAbsolutePath())

    def test_setup_orekit_data_with_list_of_paths(self):
        # Multi-path form — exercises the loop in setup_orekit_data.
        setup_orekit_data(
            filenames=["resources/regular-data",
                       "resources/potential",
                       "resources/tides"],
            from_pip_library=False,
        )
        self.assertTrue(_check_orekit_data_valid())

    def test_setup_orekit_data_with_none_raises(self):
        with self.assertRaises(FileNotFoundError) as ctx:
            setup_orekit_data(filenames=None, from_pip_library=False)
        self.assertIn("No orekit data sources specified", str(ctx.exception))

    def test_setup_orekit_curdir_backward_compat(self):
        # Legacy single-path wrapper now delegates to setup_orekit_data
        # but keeps its old positional signature.
        setup_orekit_curdir("resources/regular-data")
        self.assertTrue(_check_orekit_data_valid())

    @unittest.skipUnless(os.environ.get("OREKIT_TEST_NETWORK"),
                         "set OREKIT_TEST_NETWORK=1 to run network-dependent tests")
    def test_download_and_setup_orekit_data_from_zip(self):
        filename = "orekit-data-test.zip"
        try:
            download_orekit_data_curdir(filename=filename)
            self.assertTrue(os.path.exists(filename) and os.path.isfile(filename))

            setup_orekit_data(filenames=filename, from_pip_library=False)
            self.assertTrue(_check_orekit_data_valid())
        finally:
            if os.path.exists(filename):
                os.remove(filename)


if __name__ == '__main__':
    unittest.main()
