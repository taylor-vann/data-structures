"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from selection_sort import selection_sort


class TestSelectionSortMethods(unittest.TestCase):

    def test_selection_sort_is_not_none(self):
        arr = []
        selection_sort(arr)
        self.assertIsNotNone(arr)


    def test_selection_sort_empty(self):
        arr = []
        empty = []
        selection_sort(arr)
        self.assertEqual(arr, empty)


    def test_selection_sort_one(self):
        arr = [1]
        one = [1]
        selection_sort(arr)
        self.assertEqual(arr, one)


    def test_selection_sort_two(self):
        arr = [3, 1]
        sortd = [1, 3]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


    def test_selection_sort_six(self):
        arr = [3, 1, 7, 3, 8, 9]
        sortd = [1, 3, 3, 7, 8, 9]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


    def test_selection_sort_six_neg(self):
        arr = [3, -1, 7, -3, 8, -9]
        sortd = [-9, -3, -1, 3, 7, 8]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


    def test_selection_sort_six_float(self):
        arr = [3.4, 1.02, 7.68, 3.5, 8.89, 9.35]
        sortd = [1.02, 3.4, 3.5, 7.68, 8.89, 9.35]
        selection_sort(arr)
        self.assertEqual(arr, sortd)


if __name__ == "__main__":
    unittest.main()
