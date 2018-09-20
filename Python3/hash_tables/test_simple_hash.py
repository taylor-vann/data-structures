"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from simple_hash import SimpleHash


class TestSimpleHash(unittest.TestCase):

    def testSimpleHashExists(self):
        sh = SimpleHash()

        self.assertIsNotNone(sh)

    def testHashHasOne(self):
        sh = SimpleHash()

        sh.insert("hello", "world")

        self.assertEqual(sh["hello"], "world")

    def testHashHasNone(self):
        sh = SimpleHash()

        sh.insert("hello", "world")
        sh.insert("hello", "homefry")

        self.assertNotEqual(sh["hello"], "world")

    def testHashHasTwo(self):
        sh = SimpleHash()

        sh.insert("hello", "world")
        sh.insert("yo", "homefry")

        self.assertEqual(sh["yo"], "homefry")

    def testHashHasFour(self):
        sh = SimpleHash()

        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.delete("hello")
        sh.delete("2")

        self.assertIn("goodbye", sh)


    def testHashHasFourHello(self):
        sh = SimpleHash()

        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.delete("hello")
        sh.delete("2")

        self.assertIn("1", sh)


    def testHashHasFourThriteen(self):
        sh = SimpleHash(13, 7)

        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.delete("hello")
        sh.delete("2")

        self.assertIn("goodbye", sh)

    def testHashHasSizeFiveOverload(self):
        sh = SimpleHash(5, 3)

        sh.insert("hello", "world")
        sh.insert("goodbye", "buster")
        sh.insert("1", "one")
        sh.insert("2", "two")
        sh.insert(3, "three")
        sh.insert(17, "seventeen")
        sh.insert("doggo", "pup pup")

        self.assertIn(3, sh)

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


if __name__ == "__main__":
    unittest.main()
