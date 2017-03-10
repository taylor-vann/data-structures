"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Test for the insertion_sort module

Required:
- unittest
- InsertionSort.py
"""

import unittest
from InsertionSort import insertion_sort


class TestInsertionSortModule(unittest.TestCase):

    def testInsertionIsNotNone(self):
        arr = []
        insertion_sort(arr)
        self.assertIsNotNone(insertion_sort(arr))


    def testInsertionEmpty(self):
        arr = []
        empty = []
        insertion_sort(arr)
        self.assertEqual(arr, empty)


    def testInsertionOne(self):
        arr = [1]
        one = [1]
        insertion_sort(arr)
        self.assertEqual(arr, one)


    def testInsertionTwo(self):
        arr = [6, 4]
        sortd = [4, 6]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


    def testInsertionSix(self):
        arr = [6, 4, 8, 5, 7, 9]
        sortd = [4, 5, 6, 7, 8, 9]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


    def testInsertionSixNeg(self):
        arr = [6, -4, 8, 5, -7, 9]
        sortd = [-7, -4, 5, 6, 8, 9]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


    def testInsertionSixFloat(self):
        arr = [6.3, 4.1, 8.2, 5.9, 7.65, 9.3]
        sortd = [4.1, 5.9, 6.3, 7.65, 8.2, 9.3]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


unittest.main()
