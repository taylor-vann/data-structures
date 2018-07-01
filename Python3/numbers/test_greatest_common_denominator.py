"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from greatest_common_denominator import greatest_common_denominator


class TestGCD(unittest.TestCase):

    def test_gcd_not_none(self):
        self.assertIsNotNone(greatest_common_denominator)


    def test_gcd_4_and_2(self):
        self.assertEqual(greatest_common_denominator(4, 2), 2)


    def test_gcd_5_and_1(self):
        self.assertEqual(greatest_common_denominator(5, 2), 1)


    def test_gcd_24_and_18(self):
        self.assertEqual(greatest_common_denominator(24, 18), 6)


    def test_gcd_88_and_77(self):
        self.assertEqual(greatest_common_denominator(88, 77), 11)



if __name__ == "__main__":
    unittest.main()
