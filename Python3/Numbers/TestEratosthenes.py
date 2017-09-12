"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for Sieve of Eratosthenes

Requirements:
- Eratosthenes.py
"""

import unittest
from Eratosthenes import sieve


class TestSieve(unittest.TestCase):

    def testSieveNotNone(self):
        self.assertIsNotNone(sieve)


    def testSieveFloatIsNone(self):
        self.assertIsNone(sieve(4.2))


    def testSieve4(self):
        self.assertEqual(sieve(4), [1, 2, 3])


    def testSieve7(self):
        self.assertEqual(sieve(7), [1, 2, 3, 5, 7])


    def testSieve9(self):
        self.assertEqual(sieve(9), [1, 2, 3, 5, 7])


    def testSieve29(self):
        self.assertEqual(sieve(29), [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


    def testSieve30(self):
        self.assertEqual(sieve(30), [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


unittest.main()
