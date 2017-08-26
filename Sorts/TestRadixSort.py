"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Test for the radix_sort module

Required:
- unittest
- RadixSort.py
"""

import unittest
from RadixSort import radix_sort


class TestRadixSortMethods(unittest.TestCase):

    def testRadixSortIsNotNone(self):
        arr = []
        arr = radix_sort(arr)
        self.assertIsNotNone(arr)


    def testRadixSortEmpty(self):
        arr = []
        empty = []
        arr = radix_sort(arr)
        self.assertEqual(arr, empty)


    def testRadixSortOne(self):
        arr = [1]
        one = [1]
        arr = radix_sort(arr)
        self.assertEqual(arr, one)


    def testRadixSortTwo(self):
        arr = [25, 2]
        two = [2, 25]
        arr = radix_sort(arr)
        self.assertEqual(arr, two)


    def testRadixSortThree(self):
        arr = [25, 2, 78]
        three = [2, 25, 78]
        arr = radix_sort(arr)
        self.assertEqual(arr, three)


    def testRadixSortFive(self):
        arr = [25, 101, 2, 189, 78]
        five = [2, 25, 78, 101, 189]
        arr = radix_sort(arr)
        self.assertEqual(arr, five)


    def testRadixSortSeven(self):
        arr = [25, 101, 36, 97, 2, 189, 78]
        seven = [2, 25, 36, 78, 97, 101, 189]
        arr = radix_sort(arr)
        self.assertEqual(arr, seven)


    def testRadixSortSevenNeg(self):
        arr = [25, 101, -36, -97, 2, 189, 78]
        seven = [-97, -36, 2, 25, 78, 101, 189]
        arr = radix_sort(arr)
        self.assertNotEqual(arr, seven)


unittest.main()
