"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from merge_sort import merge_sort
from merge_sort import merge


class TestMergeSortMethods(unittest.TestCase):

    def test_merge_is_not_none(self):
        a1 = []
        a2 = []
        self.assertIsNotNone(merge(a1, a2))


    def test_merge_empty(self):
        a1 = []
        a2 = []
        eq = []
        self.assertEqual(merge(a1, a2), eq)


    def test_merge_one(self):
        a1 = [1]
        a2 = []
        eq = [1]
        self.assertEqual(merge(a1, a2), eq)


    def test_merge_two(self):
        a1 = [1, 2]
        a2 = [1, 2]
        eq = [1, 1, 2, 2]
        self.assertEqual(merge(a1, a2), eq)


    def test_merge_sort_is_not_none(self):
        arr = []
        self.assertIsNotNone(merge_sort(arr))


    def test_merge_sort_empty(self):
        arr = []
        empty = []
        self.assertEqual(merge_sort(arr), empty)


    def test_merge_sort_one(self):
        arr = [1]
        one = [1]
        self.assertEqual(merge_sort(arr), one)


    def test_merge_sort_two(self):
        arr = [2, 1]
        two = [1, 2]
        self.assertEqual(merge_sort(arr), two)


    def test_merge_sort_three(self):
        arr = [2, 3, 1]
        three = [1, 2, 3]
        self.assertEqual(merge_sort(arr), three)


    def test_merge_sort_three(self):
        arr = [2, 3, 1]
        three = [1, 2, 3]
        self.assertEqual(merge_sort(arr), three)


    def test_merge_sort_six(self):
        arr = [2, 1, 4, 6, 9, 0]
        sortd = [0, 1, 2, 4, 6, 9]
        self.assertEqual(merge_sort(arr), sortd)


    def test_merge_sort_six_neg(self):
        arr = [-2, 1, 4, -6, 9, 0]
        sortd = [-6, -2, 0, 1, 4, 9]
        self.assertEqual(merge_sort(arr), sortd)


    def test_merge_sort_six_more_neg(self):
        arr = [-6, 9, 0, -2, 1, 4]
        sortd = [-6, -2, 0, 1, 4, 9]
        self.assertEqual(merge_sort(arr), sortd)


    def test_merge_sort_six_more_float(self):
        arr = [-6.54, 9.7, 0.4, -2.09, 1.8, 4.2]
        sortd = [-6.54, -2.09, 0.4, 1.8, 4.2, 9.7]
        self.assertEqual(merge_sort(arr), sortd)


if __name__ == "__main__":
    unittest.main()
