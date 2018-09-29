"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
import math
from random import randrange
from avl_tree import AVLTree


class TestAVLNodeMethods(unittest.TestCase):

    def testAVLNodeNotNone(self):
        avl = AVLTree()

        self.assertIsNotNone(avl)

    def testAVLInsertOne(self):
        avl = AVLTree(1)

        self.assertIn(1, avl)


    def testAVLInsertTwo(self):
        avl = AVLTree(1, 2)

        self.assertIn(2, avl)


if __name__ == "__main__":
    unittest.main()
