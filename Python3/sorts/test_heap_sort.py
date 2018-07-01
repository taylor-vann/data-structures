"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from heap_sort import heap_sort


class TestHeapSortModule(unittest.TestCase):

    def test_heap_sort_is_not_none(self):
        hp = []
        heap_sort(hp)


    def test_heap_sort_none(self):
        hp = []
        srtd = []
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def test_heap_sort_one(self):
        hp = [1]
        srtd = [1]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def test_heap_sort_two(self):
        hp = [2, 1]
        srtd = [1, 2]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def test_heap_sort_five(self):
        hp = [2, 1, 5, 7, 8]
        srtd = [1, 2, 5, 7, 8]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def test_heap_sort_five_neg(self):
        hp = [-2, 1, -5, 7, 8]
        srtd = [-5, -2, 1, 7, 8]
        heap_sort(hp)
        self.assertEqual(hp, srtd)


    def test_heap_sort_five_neg_float(self):
        hp = [-2.4, 1.3, -5.9, 7.2, 8.1]
        srtd = [-5.9, -2.4, 1.3, 7.2, 8.1]
        heap_sort(hp)
        self.assertEqual(hp, srtd)



if __name__ == "__main__":
    unittest.main()
