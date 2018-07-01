"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from insertion_sort import insertion_sort


class TestInsertionSortModule(unittest.TestCase):

    def test_insertion_is_not_none(self):
        arr = []
        insertion_sort(arr)
        self.assertIsNotNone(arr)


    def test_insertion_empty(self):
        arr = []
        empty = []
        insertion_sort(arr)
        self.assertEqual(arr, empty)


    def test_insertion_one(self):
        arr = [1]
        one = [1]
        insertion_sort(arr)
        self.assertEqual(arr, one)


    def test_insertion_two(self):
        arr = [6, 4]
        sortd = [4, 6]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


    def test_insertion_six(self):
        arr = [6, 4, 8, 5, 7, 9]
        sortd = [4, 5, 6, 7, 8, 9]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


    def test_insertion_six_neg(self):
        arr = [6, -4, 8, 5, -7, 9]
        sortd = [-7, -4, 5, 6, 8, 9]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


    def test_insertion_six_float(self):
        arr = [6.3, 4.1, 8.2, 5.9, 7.65, 9.3]
        sortd = [4.1, 5.9, 6.3, 7.65, 8.2, 9.3]
        insertion_sort(arr)
        self.assertEqual(arr, sortd)


if __name__ == "__main__":
    unittest.main()
