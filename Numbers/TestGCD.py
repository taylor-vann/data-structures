"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for GCD

Requirements:
- GCD.py
"""

import unittest
from GCD import gcd


class TestGCD(unittest.TestCase):

    def testGCDNotNone(self):
        self.assertIsNotNone(gcd)


    def testGCD4and2(self):
        self.assertEqual(gcd(4, 2), 2)


    def testGCD5and1(self):
        self.assertEqual(gcd(5, 2), 1)


    def testGCD24and18(self):
        self.assertEqual(gcd(24, 18), 6)


    def testGCD24and18(self):
        self.assertEqual(gcd(88, 77), 11)




unittest.main()
