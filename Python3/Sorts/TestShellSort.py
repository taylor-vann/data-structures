"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit test for the shell sort module

Required:
- unittest
- ShellSort.py
"""

import unittest
from ShellSort import shell_sort


class TestShellSortMethods(unittest.TestCase):

    def testShellSortIsNotNone(self):
        arr = []
        one = []
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortOne(self):
        arr = [1]
        one = [1]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortTwo(self):
        arr = [4, 2]
        one = [2, 4]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortFive(self):
        arr = [4, 2, 32, 14, 5]
        one = [2, 4, 5, 14, 32]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortSeven(self):
        arr = [4, 2, 89, 1, 32, 14, 5]
        one = [1, 2, 4, 5, 14, 32, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortNine(self):
        arr = [4, 2, 12, 6, 89, 1, 32, 14, 5]
        one = [1, 2, 4, 5, 6, 12, 14, 32, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortNine(self):
        arr = [4, 2, 12, 6, 89, 1, 32, 14, 5]
        one = [1, 2, 4, 5, 6, 12, 14, 32, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortNineNeg(self):
        arr = [4, 2, -12, -6, 89, 1, -32, 14, 5]
        one = [-32, -12, -6, 1, 2, 4, 5, 14, 89]
        shell_sort(arr)
        self.assertEqual(arr, one)


    def testShellSortNineNegFloat(self):
        arr = [4.1, 2.2, -12.3, -6.4, 89.5, 1.6, -32.7, 14.8, 5.9]
        one = [-32.7, -12.3, -6.4, 1.6, 2.2, 4.1, 5.9, 14.8, 89.5]
        shell_sort(arr)
        self.assertEqual(arr, one)



unittest.main() 
