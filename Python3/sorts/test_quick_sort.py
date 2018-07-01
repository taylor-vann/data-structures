"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from quick_sort import quick_sort, partition


class TestQuickSortMethods(unittest.TestCase):

    def test_quick_one(self):
        arr = [1]
        one = [1]
        self.assertEqual(quick_sort(arr), one)


    def test_quick_two(self):
        arr = [4, 2]
        two = [2, 4]
        self.assertEqual(quick_sort(arr), two)


    def test_quick_sort_is_not_none(self):
        arr = []
        self.assertIsNotNone(quick_sort(arr))


    def test_quick_sort_empty(self):
        arr = []
        empty = []
        self.assertEqual(quick_sort(arr), empty)


    def test_quick_sort_one(self):
        arr = [1]
        one = [1]
        self.assertEqual(quick_sort(arr), one)


    def test_quick_sort_two(self):
        arr = [4, 2]
        two = [2, 4]
        self.assertEqual(quick_sort(arr), two)


    def test_quick_sort_two(self):
        arr = [4, 2]
        two = [2, 4]
        self.assertEqual(quick_sort(arr), two)


    def test_quick_sort_three(self):
        arr = [4, 2, 7]
        three = [2, 4, 7]
        self.assertEqual(quick_sort(arr), three)


    def test_quick_sort_six(self):
        arr = [4, 2, 7, 5, 8, 1]
        sortd = [1, 2, 4, 5, 7, 8]
        self.assertEqual(quick_sort(arr), sortd)


    def test_quick_sort_six(self):
        arr = [1, 2, 7, 5, 8, 1]
        sortd = [1, 1, 2, 5, 7, 8]
        self.assertEqual(quick_sort(arr), sortd)


    def test_quick_sort_six_neg(self):
        arr = [4, 2, -7, -5, 8, 1]
        sortd = [-7, -5, 1, 2, 4, 8]
        self.assertEqual(quick_sort(arr), sortd)


    def test_quick_sort_six_float(self):
        arr = [4.2, 2.8, -7.95, -5.32, 8.6, 1.43]
        sortd = [-7.95, -5.32, 1.43, 2.8, 4.2, 8.6]
        self.assertEqual(quick_sort(arr), sortd)


    def test_mutates(self):
        arr = [4, 2, 7, 5, 8, 1]
        sortd = quick_sort(arr)
        self.assertEqual(arr, sortd)



if __name__ == "__main__":
    unittest.main()
