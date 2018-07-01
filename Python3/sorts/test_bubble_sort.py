"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from bubble_sort import bubble_sort


class TestSortsMethods(unittest.TestCase):

    def test_bubble_is_not_none(self):
        arr = []
        bubble_sort(arr)
        self.assertIsNotNone(arr)


    def test_bubble_empty(self):
        arr = []
        empty = []
        bubble_sort(arr)
        self.assertEqual(arr, empty)


    def test_bubble_one(self):
        arr = [1]
        empty = [1]
        bubble_sort(arr)
        self.assertEqual(arr, empty)


    def test_bubble_sort_two(self):
        arr = [5, 3]
        sortd = [3, 5]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


    def test_bubble_sort_six(self):
        arr = [3, 5, 9, 4, 0, 12]
        sortd = [0, 3, 4, 5, 9, 12]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


    def test_bubble_sort_pos_neg(self):
        arr = [3, 5, 9, -4, 0, -12]
        sortd = [-12, -4, 0, 3, 5, 9]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


    def test_bubble_sort_pos_neg_float(self):
        arr = [3.7, 5.89, 9.1, -4.5, 0.4, -12.22]
        sortd = [-12.22, -4.5, 0.4, 3.7, 5.89, 9.1]
        bubble_sort(arr)
        self.assertEqual(arr, sortd)


if __name__ == "__main__":
    unittest.main()
