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
from HeapSort import HeapSort


class TestHeapSortModule(unittest.TestCase):

    def testHeapSortIsNotNone(self):
        hp = []
        HeapSort(hp)


    def testHeapSortNone(self):
        hp = []
        srtd = []
        HeapSort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortOne(self):
        hp = [1]
        srtd = [1]
        HeapSort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortTwo(self):
        hp = [2, 1]
        srtd = [1, 2]
        HeapSort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortFive(self):
        hp = [2, 1, 5, 7, 8]
        srtd = [1, 2, 5, 7, 8]
        HeapSort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortFiveNeg(self):
        hp = [-2, 1, -5, 7, 8]
        srtd = [-5, -2, 1, 7, 8]
        HeapSort(hp)
        self.assertEqual(hp, srtd)


    def testHeapSortFiveNegFloat(self):
        hp = [-2.4, 1.3, -5.9, 7.2, 8.1]
        srtd = [-5.9, -2.4, 1.3, 7.2, 8.1]
        HeapSort(hp)
        self.assertEqual(hp, srtd)


unittest.main()
