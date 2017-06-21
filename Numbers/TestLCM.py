"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for LC

Requirements:
- LCM.py
- GCD.py
"""

import unittest
from GCD import gcd
from LCM import lcm


class TestLCM(unittest.TestCase):

    def testLCMNotNone(self):
        self.assertIsNotNone(lcm)


    def testLCMFloatIsNone(self):
        self.assertIsNone(lcm(3.6, 8.9))


    def testLCM4and2(self):
        self.assertEqual(lcm(4, 2), 4)


    def testLCM5and1(self):
        self.assertEqual(lcm(5, 2), 10)


    def testLCM24and18(self):
        self.assertEqual(lcm(24, 18), 72)


    def testGCD88and77(self):
        self.assertEqual(lcm(88, 77), 616)



unittest.main()
