"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the SimpleHash structure class

Requirements:
- unittest
- MaxHeap.py
"""

import unittest
from SimpleHash import SimpleHash


class TestSimpleHash(unittest.TestCase):

    def testSimpleHashExists(self):
        sh = SimpleHash()

        self.assertIsNotNone(sh)

    def testHashHasOne(self):
        sh = SimpleHash()
        sh.insert("hello", "world")

        self.assertEqual(sh.search("hello"), "world")

    def testHashHasNone(self):
        sh = SimpleHash()
        sh.insert("hello", "world")
        sh.insert("hello", "homefry")

        self.assertNotEqual(sh.search("hello"), "world")

    def testHashHasNone(self):
        sh = SimpleHash()
        sh.insert("hello", "world")
        sh.insert("hello", "homefry")

        self.assertNotEqual(sh.search("hello"), "world")

    def testHashHasFour(self):
        sh = SimpleHash()
        sh.insert("hello", "world")
        sh.delete("hello")

        self.assertIsNone(sh.search("hello"))


unittest.main()
