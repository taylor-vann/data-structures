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
        self.assertIsNotNone(selection_sort(arr))


    def testSelectionSortEmpty(self):
        arr = []
        empty = []
        self.assertEqual(selection_sort(arr), empty)


    def testSelectionSortOne(self):
        arr = [1]
        one = [1]
        self.assertEqual(selection_sort(arr), one)


    def testSelectionSortTwo(self):
        arr = [3, 1]
        sortd = [1, 3]
        self.assertEqual(selection_sort(arr), sortd)


    def testSelectionSortSix(self):
        arr = [3, 1, 7, 3, 8, 9]
        sortd = [1, 3, 3, 7, 8, 9]
        self.assertEqual(selection_sort(arr), sortd)


    def testSelectionSortSixNeg(self):
        arr = [3, -1, 7, -3, 8, -9]
        sortd = [-9, -3, -1, 3, 7, 8]
        self.assertEqual(selection_sort(arr), sortd)


    def testSelectionSortSixFloat(self):
        arr = [3.4, 1.02, 7.68, 3.5, 8.89, 9.35]
        sortd = [1.02, 3.4, 3.5, 7.68, 8.89, 9.35]
        self.assertEqual(selection_sort(arr), sortd)


unittest.main()
