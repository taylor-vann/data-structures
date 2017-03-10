"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Test for the quick_sort module

Required:
- unittest
- QuickSort.py
"""

import unittest
from QuickSort import quick_sort


class TestQuickSortMethods(unittest.TestCase):

    def testQuickIsNotNone(self):
        arr = []
        quick_sort(arr, 0, len(arr) - 1)
        self.assertIsNotNone(arr)


    def testQuickEmpty(self):
        arr = []
        empty = []
        quick_sort(arr, 0, len(arr))
        self.assertEqual(arr, empty)


    def testQuickOne(self):
        arr = [1]
        one = [1]
        quick_sort(arr, 0, len(arr))
        self.assertEqual(arr, one)


    def testQuickTwo(self):
        arr = [4, 2]
        two = [2, 4]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, two)


    def testQuickThree(self):
        arr = [4, 2, 7]
        three = [2, 4, 7]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, three)


    def testQuickSix(self):
        arr = [4, 2, 7, 5, 8, 1]
        sortd = [1, 2, 4, 5, 7, 8]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, sortd)


    def testQuickSixNeg(self):
        arr = [4, 2, -7, -5, 8, 1]
        sortd = [-7, -5, 1, 2, 4, 8]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, sortd)


    def testQuickSixFloat(self):
        arr = [4.2, 2.8, -7.95, -5.32, 8.6, 1.43]
        sortd = [-7.95, -5.32, 1.43, 2.8, 4.2, 8.6]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, sortd)


unittest.main()
