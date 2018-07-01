"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from greatest_common_denominator import greatest_common_denominator
from least_common_multiple import least_common_multiple


class TestLCM(unittest.TestCase):

    def test_lcm_not_none(self):
        self.assertIsNotNone(least_common_multiple)


    def test_lcm_float_is_none(self):
        self.assertIsNone(least_common_multiple(3.6, 8.9))


    def test_lcm_4_and_2(self):
        self.assertEqual(least_common_multiple(4, 2), 4)


    def test_lcm_5_and_1(self):
        self.assertEqual(least_common_multiple(5, 2), 10)


    def test_lcm_24_and_18(self):
        self.assertEqual(least_common_multiple(24, 18), 72)


    def test_lcm_88_and_77(self):
        self.assertEqual(least_common_multiple(88, 77), 616)



if __name__ == "__main__":
    unittest.main()
