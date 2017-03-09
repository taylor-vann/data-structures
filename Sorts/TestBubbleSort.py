"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Tess for Sorting modules in Sorts.py

Required:
- Sorts.py
"""

import unittest
from BubbleSort import bubble_sort


class TestSortsMethods(unittest.TestCase):

    def testBubbleIsNotNone(self):
        arr = []
        self.assertIsNotNone(bubble_sort(arr))


    def testBubbleEmpty(self):
        arr = []
        empty = []
        self.assertEqual(bubble_sort(arr), empty)


    def testBubbleOne(self):
        arr = [1]
        empty = [1]
        self.assertEqual(bubble_sort(arr), empty)


    def testBubbleSortTwo(self):
        arr = [5, 3]
        sortd = [3, 5]
        self.assertEqual(bubble_sort(arr), sortd)


    def testBubbleSortSix(self):
        arr = [3, 5, 9, 4, 0, 12]
        sortd = [0, 3, 4, 5, 9, 12]
        self.assertEqual(bubble_sort(arr), sortd)


    def testBubbleSortPosNeg(self):
        arr = [3, 5, 9, -4, 0, -12]
        sortd = [-12, -4, 0, 3, 5, 9]
        self.assertEqual(bubble_sort(arr), sortd)


    def testBubbleSortPosNegFloat(self):
        arr = [3.7, 5.89, 9.1, -4.5, 0.4, -12.22]
        sortd = [-12.22, -4.5, 0.4, 3.7, 5.89, 9.1]
        self.assertEqual(bubble_sort(arr), sortd)


unittest.main()
