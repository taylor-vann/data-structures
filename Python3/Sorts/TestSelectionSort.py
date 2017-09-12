"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Test for the selection_sort module

Required:
- unittest
- SelectionSort.py
"""

import unittest
from SelectionSort import selection_sort


class TestSelectionSortMethods(unittest.TestCase):

    def testSelectionSortIsNotNone(self):
        arr = []
        selection_sort(arr)
        self.assertIsNotNone(arr)


    def testSelectionSortEmpty(self):
        arr = []
        empty = []
        selection_sort(arr)
        self.assertEqual(arr, empty)


    def testSelectionSortOne(self):
        arr = [1]
        one = [1]
        selection_sort(arr)
        self.assertEqual(arr, one)


    def testSelectionSortTwo(self):
        arr = [3, 1]
        sortd = [1, 3]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


    def testSelectionSortSix(self):
        arr = [3, 1, 7, 3, 8, 9]
        sortd = [1, 3, 3, 7, 8, 9]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


    def testSelectionSortSixNeg(self):
        arr = [3, -1, 7, -3, 8, -9]
        sortd = [-9, -3, -1, 3, 7, 8]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


    def testSelectionSortSixFloat(self):
        arr = [3.4, 1.02, 7.68, 3.5, 8.89, 9.35]
        sortd = [1.02, 3.4, 3.5, 7.68, 8.89, 9.35]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


unittest.main()
