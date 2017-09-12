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

    def testHashHasTwo(self):
        sh = SimpleHash()
        sh.insert("hello", "world")
        sh.insert("yo", "homefry")

        self.assertEqual(sh.search("yo"), "homefry")

    def testHashHasFour(self):
        sh = SimpleHash()
        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.delete("hello")
        sh.delete("2")

        self.assertEqual(sh.search("goodbye"), "buster")


    def testHashHasFourHello(self):
        sh = SimpleHash()
        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.delete("hello")
        sh.delete("2")

        self.assertEqual(sh.search("1"), "one")


    def testHashHasFourThriteen(self):
        sh = SimpleHash(13, 7)
        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.delete("hello")
        sh.delete("2")

        self.assertEqual(sh.search("goodbye"), "buster")

    def testHashHasSizeFiveOverload(self):
        sh = SimpleHash(5, 3)
        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.insert(3, "three")
        sh.insert(17, "seventeen")
        sh.insert("doggo", "pup pup")

        self.assertEqual(sh.search("3"), "three")

    def testHashContains(self):
        sh = SimpleHash(5, 3)
        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.insert(3, "three")
        sh.insert(17, "seventeen")
        sh.insert("doggo", "pup pup")

        self.assertTrue("hello" in sh)

    def testHashNotContains(self):
        sh = SimpleHash(5, 3)
        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.insert(3, "three")
        sh.insert(17, "seventeen")
        sh.insert("doggo", "pup pup")

        self.assertFalse("blue" in sh)


    def testHashLengthNone(self):
        sh = SimpleHash(5, 3)

        self.assertEqual(len(sh), 0)


    def testHashLengthSeven(self):
        sh = SimpleHash(5, 3)
        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.insert(3, "three")
        sh.insert(17, "seventeen")
        sh.insert("doggo", "pup pup")

        self.assertEqual(len(sh), 7)


unittest.main()
