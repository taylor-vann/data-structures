"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from radix_sort import radix_sort


class TestRadixSortMethods(unittest.TestCase):

    def test_radix_sort_is_not_none(self):
        arr = []
        arr = radix_sort(arr)
        self.assertIsNotNone(arr)


    def test_radix_sort_empty(self):
        arr = []
        empty = []
        arr = radix_sort(arr)
        self.assertEqual(arr, empty)


    def test_radix_sort_one(self):
        arr = [1]
        one = [1]
        arr = radix_sort(arr)
        self.assertEqual(arr, one)


    def test_radix_sort_two(self):
        arr = [25, 2]
        two = [2, 25]
        arr = radix_sort(arr)
        self.assertEqual(arr, two)


    def test_radix_sort_three(self):
        arr = [25, 2, 78]
        three = [2, 25, 78]
        arr = radix_sort(arr)
        self.assertEqual(arr, three)


    def test_radix_sort_five(self):
        arr = [25, 101, 2, 189, 78]
        five = [2, 25, 78, 101, 189]
        arr = radix_sort(arr)
        self.assertEqual(arr, five)


    def test_radix_sort_seven(self):
        arr = [25, 101, 36, 97, 2, 189, 78]
        seven = [2, 25, 36, 78, 97, 101, 189]
        arr = radix_sort(arr)
        self.assertEqual(arr, seven)


    def test_radix_sort_seven_neg(self):
        arr = [25, 101, -36, -97, 2, 189, 78]
        seven = [-97, -36, 2, 25, 78, 101, 189]
        arr = radix_sort(arr)
        self.assertNotEqual(arr, seven)


if __name__ == "__main__":
    unittest.main()
