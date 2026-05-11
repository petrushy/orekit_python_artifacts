# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's DataDictionaryTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JArray_double
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from java.lang import Integer
from org.orekit.utils import DataDictionary, DoubleArrayDictionary


class DataDictionaryTest(unittest.TestCase):

    def assertArrayAlmostEqual(self, expected, actual, delta=1.0e-15):
        actual = JArray_double.cast_(actual)
        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertAlmostEqual(e, float(a), delta=delta)

    def test_empty(self):
        self.assertTrue(DataDictionary().getData().isEmpty())

    def test_put_get(self):
        dictionary = DataDictionary()
        dictionary.put("a", JArray_double([1.0, 2.0, 3.0]))
        dictionary.put("string", "Lorem Ipsum")
        dictionary.put("int", Integer(9))

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))
        self.assertEqual("Lorem Ipsum", str(dictionary.get("string")))
        self.assertEqual(9, Integer.cast_(dictionary.get("int")).intValue())

    def test_get_not_existing(self):
        dictionary = DataDictionary()
        self.assertIsNone(dictionary.get("not-a-key"))

    def test_from_dictionary(self):
        original = DataDictionary()
        original.put("string", "Lorem Ipsum")
        copy = DataDictionary()
        copy.putAll(original)
        self.assertEqual("Lorem Ipsum", str(copy.get("string")))

    def test_arrays_are_copied(self):
        dictionary = DataDictionary()
        original = JArray_double([1.0, 2.0, 3.0])
        dictionary.put("a", original)
        retrieved = dictionary.get("a")
        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], retrieved)

    def test_increment(self):
        dictionary = DataDictionary()
        dictionary.put("a", JArray_double([1.0, 2.0, 3.0]))
        dictionary.getEntry("a").increment(JArray_double([2.0, 4.0, 8.0]))
        self.assertArrayAlmostEqual([3.0, 6.0, 11.0], dictionary.get("a"))

    def test_scaled_increment(self):
        dictionary = DataDictionary()
        dictionary.put("a", JArray_double([1.0, 2.0, 3.0]))
        other = DoubleArrayDictionary()
        other.put("aDot", JArray_double([3.0, 2.0, 1.0]))
        dictionary.getEntry("a").scaledIncrement(2.0, other.getEntry("aDot"))
        self.assertArrayAlmostEqual([7.0, 6.0, 5.0], dictionary.get("a"))

    def test_zero(self):
        dictionary = DataDictionary()
        dictionary.put("a", JArray_double([1.0, 2.0, 3.0]))
        dictionary.getEntry("a").zero()
        self.assertArrayAlmostEqual([0.0, 0.0, 0.0], dictionary.get("a"))

    def test_data_management(self):
        dictionary = DataDictionary()
        dictionary.put("a", JArray_double([1.0, 2.0, 3.0]))
        dictionary.put("b", JArray_double([4.0]))
        dictionary.put("another", JArray_double([17.0]))

        self.assertEqual(3, dictionary.size())
        self.assertEqual("{a[3], b[1], another[1]}", str(dictionary.toString()))

        self.assertTrue(dictionary.remove("another"))
        self.assertEqual(2, dictionary.size())
        self.assertFalse(dictionary.remove("not-a-key"))
        self.assertEqual(2, dictionary.size())

        self.assertEqual("a", str(dictionary.getData().get(0).getKey()))
        self.assertEqual("b", str(dictionary.getData().get(1).getKey()))

        dictionary.clear()
        self.assertTrue(dictionary.getData().isEmpty())

    def test_replace(self):
        dictionary = DataDictionary()
        dictionary.put("a", JArray_double([1.0, 2.0, 3.0]))
        dictionary.put("toreplace", "Lorem Ipsum")
        dictionary.put("b", Integer(9))
        self.assertEqual(3, dictionary.size())

        dictionary.put("toreplace", "replaced value")
        self.assertEqual(3, dictionary.size())

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))
        self.assertEqual("replaced value", str(dictionary.get("toreplace")))
        self.assertEqual(9, Integer.cast_(dictionary.get("b")).intValue())

    def test_to_map(self):
        dictionary = DataDictionary()
        dictionary.put("a", JArray_double([1.0, 2.0, 3.0]))
        dictionary.put("d", "Lorem Ipsum")
        dictionary.put("e", Integer(9))
        self.assertEqual(3, dictionary.size())

        map_obj = dictionary.toMap()
        self.assertEqual(3, map_obj.size())
        self.assertEqual("Lorem Ipsum", str(dictionary.get("d")))
        self.assertEqual(9, Integer.cast_(dictionary.get("e")).intValue())

        dictionary.clear()
        self.assertEqual(0, dictionary.size())
        self.assertEqual(3, map_obj.size())


if __name__ == '__main__':
    unittest.main()
