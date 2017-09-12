"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Test for the bubble_sort module

Required:
- unittest
- BubbleSort.py
"""

import unittest
from BubbleSort import bubble_sort


class TestSortsMethods(unittest.TestCase):

    def testBubbleIsNotNone(self):
        arr = []
        bubble_sort(arr)
        self.assertIsNotNone(arr)


    def testBubbleEmpty(self):
        arr = []
        empty = []
        bubble_sort(arr)
        self.assertEqual(arr, empty)


    def testBubbleOne(self):
        arr = [1]
        empty = [1]
        bubble_sort(arr)
        self.assertEqual(arr, empty)


    def testBubbleSortTwo(self):
        arr = [5, 3]
        sortd = [3, 5]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


    def testBubbleSortSix(self):
        arr = [3, 5, 9, 4, 0, 12]
        sortd = [0, 3, 4, 5, 9, 12]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


    def testBubbleSortPosNeg(self):
        arr = [3, 5, 9, -4, 0, -12]
        sortd = [-12, -4, 0, 3, 5, 9]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


    def testBubbleSortPosNegFloat(self):
        arr = [3.7, 5.89, 9.1, -4.5, 0.4, -12.22]
        sortd = [-12.22, -4.5, 0.4, 3.7, 5.89, 9.1]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


unittest.main()
