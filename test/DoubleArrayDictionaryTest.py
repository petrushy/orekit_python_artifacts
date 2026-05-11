# -*- coding: utf-8 -*-
"""JCC port adapted from orekit_jpype's DoubleArrayDictionaryTest."""

import unittest

import orekit
orekit.initVM()

from orekit import JArray_double
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources/regular-data")

from java.util import HashMap
from org.orekit.utils import DoubleArrayDictionary


def to_list(java_double_array):
    return [float(x) for x in java_double_array]


class DoubleArrayDictionaryTest(unittest.TestCase):

    def assertArrayAlmostEqual(self, expected, actual, delta=1.0e-15):
        actual_list = to_list(actual)
        self.assertEqual(len(expected), len(actual_list))
        for e, a in zip(expected, actual_list):
            self.assertAlmostEqual(e, a, delta=delta)

    def put_array(self, dictionary, key, values):
        dictionary.put(key, JArray_double(values))

    def test_empty(self):
        self.assertTrue(DoubleArrayDictionary().getData().isEmpty())

    def test_put_get(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        self.put_array(dictionary, "b", [4.0])
        self.put_array(dictionary, "another", [17.0])

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))
        self.assertArrayAlmostEqual([17.0], dictionary.get("another"))
        self.assertArrayAlmostEqual([4.0], dictionary.get("b"))
        self.assertIsNone(dictionary.get("not-a-key"))

    def test_from_dictionary(self):
        original = DoubleArrayDictionary()
        self.put_array(original, "a", [1.0, 2.0, 3.0])
        self.put_array(original, "b", [4.0])
        self.put_array(original, "another", [17.0])

        # JCC does not expose the DoubleArrayDictionary copy constructor
        # in this build despite the Java API having one; exercise the same
        # copy path through putAll(DoubleArrayDictionary).
        copy = DoubleArrayDictionary()
        copy.putAll(original)

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], copy.get("a"))
        self.assertArrayAlmostEqual([17.0], copy.get("another"))
        self.assertArrayAlmostEqual([4.0], copy.get("b"))
        self.assertIsNone(copy.get("not-a-key"))

    def test_from_map(self):
        map_ = HashMap()
        map_.put("a", JArray_double([1.0, 2.0, 3.0]))
        map_.put("b", JArray_double([4.0]))
        map_.put("another", JArray_double([17.0]))

        dictionary = DoubleArrayDictionary(map_)

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))
        self.assertArrayAlmostEqual([17.0], dictionary.get("another"))
        self.assertArrayAlmostEqual([4.0], dictionary.get("b"))
        self.assertIsNone(dictionary.get("not-a-key"))

    def test_arrays_are_copied(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        retrieved = dictionary.get("a")
        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], retrieved)
        retrieved[0] = 99.0
        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))

    def test_increment(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        dictionary.getEntry("a").increment(JArray_double([2.0, 4.0, 8.0]))
        self.assertArrayAlmostEqual([3.0, 6.0, 11.0], dictionary.get("a"))

    def test_scaled_increment(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        other = DoubleArrayDictionary()
        self.put_array(other, "aDot", [3.0, 2.0, 1.0])
        dictionary.getEntry("a").scaledIncrement(2.0, other.getEntry("aDot"))
        self.assertArrayAlmostEqual([7.0, 6.0, 5.0], dictionary.get("a"))

    def test_zero(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        dictionary.getEntry("a").zero()
        self.assertArrayAlmostEqual([0.0, 0.0, 0.0], dictionary.get("a"))

    def test_size(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        self.assertEqual(3, dictionary.getEntry("a").size())

    def test_data_management(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        self.put_array(dictionary, "b", [4.0])
        self.put_array(dictionary, "another", [17.0])

        self.assertEqual(3, dictionary.size())
        self.assertEqual("{a[3], b[1], another[1]}", dictionary.toString())

        self.assertTrue(dictionary.remove("another"))
        self.assertEqual(2, dictionary.size())
        self.assertFalse(dictionary.remove("not-a-key"))
        self.assertEqual(2, dictionary.size())

        self.assertEqual("a", dictionary.getData().get(0).getKey())
        self.assertEqual("b", dictionary.getData().get(1).getKey())

        dictionary.clear()
        self.assertTrue(dictionary.getData().isEmpty())

    def test_replace(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        self.put_array(dictionary, "b", [4.0])
        self.put_array(dictionary, "another", [17.0])
        self.assertEqual(3, dictionary.size())

        self.put_array(dictionary, "b", [-1.0, -1.0])
        self.assertEqual(3, dictionary.size())

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))
        self.assertArrayAlmostEqual([17.0], dictionary.get("another"))
        self.assertArrayAlmostEqual([-1.0, -1.0], dictionary.get("b"))
        self.assertEqual("a", dictionary.getData().get(0).getKey())
        self.assertEqual("another", dictionary.getData().get(1).getKey())
        self.assertEqual("b", dictionary.getData().get(2).getKey())

    def test_put_all_map(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        self.put_array(dictionary, "b", [4.0])
        self.put_array(dictionary, "another", [17.0])

        map_ = HashMap()
        map_.put("f", JArray_double([12.0]))
        map_.put("g", JArray_double([-12.0]))
        map_.put("b", JArray_double([19.0]))

        dictionary.putAll(map_)
        self.assertEqual(5, dictionary.size())

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))
        self.assertArrayAlmostEqual([19.0], dictionary.get("b"))
        self.assertArrayAlmostEqual([17.0], dictionary.get("another"))
        self.assertArrayAlmostEqual([12.0], dictionary.get("f"))
        self.assertArrayAlmostEqual([-12.0], dictionary.get("g"))

    def test_put_all_dictionary(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        self.put_array(dictionary, "b", [4.0])
        self.put_array(dictionary, "another", [17.0])

        other = DoubleArrayDictionary()
        self.put_array(other, "f", [12.0])
        self.put_array(other, "g", [-12.0])
        self.put_array(other, "b", [19.0])

        dictionary.putAll(other)
        self.assertEqual(5, dictionary.size())

        self.assertArrayAlmostEqual([1.0, 2.0, 3.0], dictionary.get("a"))
        self.assertArrayAlmostEqual([19.0], dictionary.get("b"))
        self.assertArrayAlmostEqual([17.0], dictionary.get("another"))
        self.assertArrayAlmostEqual([12.0], dictionary.get("f"))
        self.assertArrayAlmostEqual([-12.0], dictionary.get("g"))

    def test_to_map(self):
        dictionary = DoubleArrayDictionary()
        self.put_array(dictionary, "a", [1.0, 2.0, 3.0])
        self.put_array(dictionary, "b", [4.0])
        self.put_array(dictionary, "another", [17.0])

        map_ = dictionary.toMap()
        self.assertEqual(3, map_.size())
        self.assertArrayAlmostEqual([1.0, 2.0, 3.0],
                                    JArray_double.cast_(map_.get("a")))
        self.assertArrayAlmostEqual([4.0], JArray_double.cast_(map_.get("b")))
        self.assertArrayAlmostEqual([17.0],
                                    JArray_double.cast_(map_.get("another")))

        dictionary.clear()
        self.assertEqual(0, dictionary.size())
        self.assertEqual(3, map_.size())
        map_.put("z", JArray_double([]))
        self.assertEqual(4, map_.size())
        self.assertEqual(0, dictionary.size())


if __name__ == '__main__':
    unittest.main()
