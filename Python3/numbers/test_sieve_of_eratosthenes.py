"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from sieve_of_eratosthenes import sieve_of_eratosthenes


class TestSieve(unittest.TestCase):

    def test_sieve_not_none(self):
        self.assertIsNotNone(sieve_of_eratosthenes)


    def test_sieve_float_is_none(self):
        self.assertIsNone(sieve_of_eratosthenes(4.2))


    def test_sieve_4(self):
        self.assertEqual(sieve_of_eratosthenes(4), [1, 2, 3])


    def test_sieve_7(self):
        self.assertEqual(sieve_of_eratosthenes(7), [1, 2, 3, 5, 7])


    def test_sieve_9(self):
        self.assertEqual(sieve_of_eratosthenes(9), [1, 2, 3, 5, 7])


    def test_sieve_29(self):
        self.assertEqual(sieve_of_eratosthenes(29), [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


    def test_sieve_30(self):
        self.assertEqual(sieve_of_eratosthenes(30), [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == "__main__":
    unittest.main()
