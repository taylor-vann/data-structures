"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Test for the quick_sort module

Required:
- unittest
- MergeSort.py
"""

import unittest
from MergeSort import merge_sort
from MergeSort import merge


class TestMergeSortMethods(unittest.TestCase):

    def testMergeIsNotNone(self):
        a1 = []
        a2 = []
        self.assertIsNotNone(merge(a1, a2))


    def testMergeEmpty(self):
        a1 = []
        a2 = []
        eq = []
        self.assertEqual(merge(a1, a2), eq)


    def testMergeOne(self):
        a1 = [1]
        a2 = []
        eq = [1]
        self.assertEqual(merge(a1, a2), eq)


    def testMergeTwo(self):
        a1 = [1, 2]
        a2 = [1, 2]
        eq = [1, 1, 2, 2]
        self.assertEqual(merge(a1, a2), eq)


    def testMergeSortIsNotNone(self):
        arr = []
        self.assertIsNotNone(merge_sort(arr))


    def testMergeSortEmpty(self):
        arr = []
        empty = []
        self.assertEqual(merge_sort(arr), empty)


    def testMergeSortOne(self):
        arr = [1]
        one = [1]
        self.assertEqual(merge_sort(arr), one)


    def testMergeSortTwo(self):
        arr = [2, 1]
        two = [1, 2] 
        self.assertEqual(merge_sort(arr), two)


    def testMergeSortThree(self):
        arr = [2, 3, 1]
        three = [1, 2, 3]
        self.assertEqual(merge_sort(arr), three)


    def testMergeSortThree(self):
        arr = [2, 3, 1]
        three = [1, 2, 3]
        self.assertEqual(merge_sort(arr), three)


    def testMergeSortSix(self):
        arr = [2, 1, 4, 6, 9, 0]
        sortd = [0, 1, 2, 4, 6, 9]
        self.assertEqual(merge_sort(arr), sortd)


    def testMergeSortSixNeg(self):
        arr = [-2, 1, 4, -6, 9, 0]
        sortd = [-6, -2, 0, 1, 4, 9]
        self.assertEqual(merge_sort(arr), sortd)


    def testMergeSortSixMoreNeg(self):
        arr = [-6, 9, 0, -2, 1, 4]
        sortd = [-6, -2, 0, 1, 4, 9]
        self.assertEqual(merge_sort(arr), sortd)


    def testMergeSortSixMoreFloat(self):
        arr = [-6.54, 9.7, 0.4, -2.09, 1.8, 4.2]
        sortd = [-6.54, -2.09, 0.4, 1.8, 4.2, 9.7]
        self.assertEqual(merge_sort(arr), sortd)


unittest.main()
