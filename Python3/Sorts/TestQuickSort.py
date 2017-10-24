"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Test for the quick_sort module

Required:
- unittest
- QuickSortSort.py
"""

import unittest
from QuickSort import quick_sort
from QuickSort import partition


class TestQuickSortMethods(unittest.TestCase):

    def testPartitionIsNotNone(self):
        arr = [1, 2]
        self.assertIsNotNone(partition(arr))


    def testPartitionTwo(self):
        arr = [1, 3]
        self.assertEqual(partition(arr), ([1], [3]))


    def testPartitionThree(self):
        arr = [1, 3, 2]
        self.assertEqual(partition(arr), ([1, 2], [3]))


    def testPartitionSix(self):
        arr = [1, 3, 6, 9, 0]
        self.assertEqual(partition(arr), ([0, 1, 3, 6], [9]))


    def testQuickOne(self):
        arr = [1]
        one = [1]
        self.assertEqual(quick_sort(arr), one)


    def testQuickTwo(self):
        arr = [4, 2]
        two = [2, 4]
        self.assertEqual(quick_sort(arr), two)


    def testQuickSortIsNotNone(self):
        arr = []
        self.assertIsNotNone(quick_sort(arr))


    def testQuickSortEmpty(self):
        arr = []
        empty = []
        self.assertEqual(quick_sort(arr), empty)


    def testQuickSortOne(self):
        arr = [1]
        one = [1]
        self.assertEqual(quick_sort(arr), one)


    def testQuickSortTwo(self):
        arr = [4, 2]
        two = [2, 4]
        self.assertEqual(quick_sort(arr), two)


    def testQuickSortTwo(self):
        arr = [4, 2]
        two = [2, 4]
        self.assertEqual(quick_sort(arr), two)


    def testQuickSortThree(self):
        arr = [4, 2, 7]
        three = [2, 4, 7]
        self.assertEqual(quick_sort(arr), three)


    def testQuickSortSix(self):
        arr = [4, 2, 7, 5, 8, 1]
        sortd = [1, 2, 4, 5, 7, 8]
        self.assertEqual(quick_sort(arr), sortd)


    def testQuickSortSix(self):
        arr = [1, 2, 7, 5, 8, 1]
        sortd = [1, 1, 2, 5, 7, 8]
        self.assertEqual(quick_sort(arr), sortd)


    def testQuickSortSixNeg(self):
        arr = [4, 2, -7, -5, 8, 1]
        sortd = [-7, -5, 1, 2, 4, 8]
        self.assertEqual(quick_sort(arr), sortd)


    def testQuickSortSixFloat(self):
        arr = [4.2, 2.8, -7.95, -5.32, 8.6, 1.43]
        sortd = [-7.95, -5.32, 1.43, 2.8, 4.2, 8.6]
        self.assertEqual(quick_sort(arr), sortd)


    def testImmutable(self):
        arr = [4, 2, 7, 5, 8, 1]
        sortd = quick_sort(arr)
        self.assertEqual(arr, [4, 2, 7, 5, 8, 1])



unittest.main()
