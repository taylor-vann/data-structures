"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the AVLTree class

Requirements:
- unittest
- AVLTree.py
- AVLNode.py
"""

import unittest
from random import randrange
from AVLTree import AVLTree


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


    def testAVLInsertThree(self):
        avl = AVLTree(1, 3)
        avl.insert(2)
        self.assertIn(2, avl)

        #avl = AVLTree(1, 3, 2)
        #avl.traverse(avl._r)

        #avl1 = AVLTree(12, 24, 5, 7, 1, 6, 8, 9, 18)
        #avl1.traverse(avl1._r)

        avl2 = AVLTree()
        for v in range(30):
            avl2.insert(randrange(50))
        avl2.traverse(avl2._r)

unittest.main()
