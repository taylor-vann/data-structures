"""
Brian Vann
https://github.com/taylor-vann
"""

import unittest
from newtonian_root import newtonian_root


class TestNewtonRoot(unittest.TestCase):

    def test_newton_exists(self):
        self.assertIsNotNone(newtonian_root)


    def test_newton_neg(self):
        self.assertIsNone(newtonian_root(-5))


    def test_newton_0(self):
        self.assertAlmostEqual(newtonian_root(0), 0)


    def test_newton_root_4(self):
        self.assertAlmostEqual(newtonian_root(4), 2)


    def test_newton_root_16(self):
        self.assertAlmostEqual(newtonian_root(16), 4)


    def test_newton_root_1(self):
        self.assertAlmostEqual(newtonian_root(1), 1)


    def test_newton_root_2(self):
        self.assertAlmostEqual(newtonian_root(2), 1.414213562373095)


    def test_newton_root_3(self):
        self.assertAlmostEqual(newtonian_root(3), 1.7320508075688772)


if __name__ == "__main__":
    unittest.main()
