"""
Brian Vann
https://github.com/taylor-vann
"""

import unittest
from babylonian_root import babylonian_root

class TestBabylonRoot(unittest.TestCase):

    def test_babylonian_exists(self):
        self.assertIsNotNone(babylonian_root)


    def test_babylonian_neg(self):
        self.assertIsNone(babylonian_root(-5))


    def test_babylonian_0(self):
        self.assertAlmostEqual(babylonian_root(0), 0)


    def test_babylonian_root_4(self):
        self.assertAlmostEqual(babylonian_root(4), 2)


    def test_babylonian_root_16(self):
        self.assertAlmostEqual(babylonian_root(16), 4)


    def test_babylonian_root_1(self):
        self.assertAlmostEqual(babylonian_root(1), 1)


    def test_babylonian_root_2(self):
        self.assertAlmostEqual(babylonian_root(2), 2 ** 0.5)


    def test_babylonian_root_3(self):
        self.assertAlmostEqual(babylonian_root(3), 3 ** 0.5)


if __name__ == "__main__":
    unittest.main()
