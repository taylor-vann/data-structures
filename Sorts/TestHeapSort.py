"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for heapsort module

Requirements:
- unittest
- HeapSort.py
"""

import unittest
from HeapSort import heap_sort


class TestHeapSortModule(unittest.TestCase):

    def testHeapSortIsNotNone(self):
        hp = []
        heap_sort(hp)


    def testHeapSortNone(self):
        hp = []
        srtd = []
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortOne(self):
        hp = [1]
        srtd = [1]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortTwo(self):
        hp = [2, 1]
        srtd = [1, 2]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortFive(self):
        hp = [2, 1, 5, 7, 8]
        srtd = [1, 2, 5, 7, 8]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortFiveNeg(self):
        hp = [-2, 1, -5, 7, 8]
        srtd = [-5, -2, 1, 7, 8]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortFiveNegFloat(self):
        hp = [-2.4, 1.3, -5.9, 7.2, 8.1]
        srtd = [-5.9, -2.4, 1.3, 7.2, 8.1]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


unittest.main()
