"""
Brian Vann
github.com/taylor-vann

Description:
- Unit Tests for the sqrt_rnewton.
"""

import unittest
from RealNewtonRoot import sqrt_rnewton

class TestNewtonRoot(unittest.TestCase):

    def testNewtonExists(self):
        self.assertIsNotNone(sqrt_rnewton)


    def testNewtonNeg(self):
        self.assertIsNone(sqrt_rnewton(-5))


    def testNewton0(self):
        self.assertEqual(sqrt_rnewton(0), 0)


    def testNewtonRoot4(self):
        self.assertEqual(sqrt_rnewton(4), 2)


    def testNewtonRoot16(self):
        self.assertEqual(sqrt_rnewton(16), 4)


    def testNewtonRoot1(self):
        self.assertEqual(sqrt_rnewton(1), 1)


    def testNewtonRoot2(self):
        self.assertEqual(sqrt_rnewton(2), 1.414213562373095)


    def testNewtonRoot3(self):
        self.assertEqual(sqrt_rnewton(3), 1.7320508075688772)



unittest.main()
