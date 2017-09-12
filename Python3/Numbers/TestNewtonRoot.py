"""
Brian Vann
github.com/taylor-vann

Description:
- Unit Tests for the sqrt_newton.
"""

import unittest
from NewtonRoot import sqrt_newton

class TestNewtonRoot(unittest.TestCase):

    def testNewtonExists(self):
        self.assertIsNotNone(sqrt_newton)


    def testNewtonNeg(self):
        self.assertIsNone(sqrt_newton(-5))


    def testNewton0(self):
        self.assertEqual(sqrt_newton(0), 0)


    def testNewtonRoot4(self):
        self.assertEqual(sqrt_newton(4), 2)


    def testNewtonRoot16(self):
        self.assertEqual(sqrt_newton(16), 4)


    def testNewtonRoot1(self):
        self.assertEqual(sqrt_newton(1), 1)


    def testNewtonRoot2(self):
        self.assertEqual(sqrt_newton(2), 1.414213562373095)


    def testNewtonRoot3(self):
        self.assertEqual(sqrt_newton(3), 1.7320508075688772)




unittest.main()
