"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from shell_sort import shell_sort


class TestShellSortMethods(unittest.TestCase):

    def test_shell_sort_is_not_none(self):
        arr = []
        one = []
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_one(self):
        arr = [1]
        one = [1]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_two(self):
        arr = [4, 2]
        one = [2, 4]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_five(self):
        arr = [4, 2, 32, 14, 5]
        one = [2, 4, 5, 14, 32]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_seven(self):
        arr = [4, 2, 89, 1, 32, 14, 5]
        one = [1, 2, 4, 5, 14, 32, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_nine(self):
        arr = [4, 2, 12, 6, 89, 1, 32, 14, 5]
        one = [1, 2, 4, 5, 6, 12, 14, 32, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_nine(self):
        arr = [4, 2, 12, 6, 89, 1, 32, 14, 5]
        one = [1, 2, 4, 5, 6, 12, 14, 32, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_nine_neg(self):
        arr = [4, 2, -12, -6, 89, 1, -32, 14, 5]
        one = [-32, -12, -6, 1, 2, 4, 5, 14, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def test_shell_sort_nine_neg_float(self):
        arr = [4.1, 2.2, -12.3, -6.4, 89.5, 1.6, -32.7, 14.8, 5.9]
        one = [-32.7, -12.3, -6.4, 1.6, 2.2, 4.1, 5.9, 14.8, 89.5]
        shell_sort(arr)
        self.assertEqual(arr, one)



if __name__ == "__main__":
    unittest.main()
