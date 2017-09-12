"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the AVLTree class

Requirements:
- unittest
- random
- AVLTree.py
- AVLNode.py
"""

import unittest
import math
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


    def testAVLInsertFiveDepthLessThanTwo(self):
        avl = AVLTree()

        for v in range(5):
            avl.insert(randrange(50))

        l = 0
        r = 0

        if avl._r.get_left():
            l = avl._r.get_left().get_height()
        if avl._r.get_right():
            r = avl._r.get_right().get_height()

        self.assertLess(abs(l - r), 2)


    def testAVLInsertThirtyDepthLessThanTwo(self):
        avl = AVLTree()

        l = 0
        r = 0

        for v in range(30):
            avl.insert(randrange(50))

        if avl._r.get_left():
            l = avl._r.get_left().get_height()
        if avl._r.get_right():
            r = avl._r.get_right().get_height()

        self.assertLess(abs(l - r), math.log(30, 2))


    def testAVLInsertTwoDepthRemoveOne(self):
        avl = AVLTree(5, 7)
        avl.remove(5)

        self.assertNotIn(1, avl)


    def testAVLInsertThreeDepthRemoveRoot(self):
        avl = AVLTree(5, 7, 4)
        avl.remove(5)

        self.assertNotIn(5, avl)


    def testAVLInsertFiveDepthTwoChildNode(self):
        avl = AVLTree(5, 7, 4, 6, 8)
        avl.remove(7)

        self.assertNotIn(7, avl)


    def testAVLInsertFiveDepthRemoveNoChildNode(self):
        avl = AVLTree(5, 7, 1, 6, 8, 9)
        avl.remove(1)

        self.assertNotIn(1, avl)


    def testAVLInsertFiveDepthRemoveParentLeftChild(self):
        avl = AVLTree(5, 7, 1, 6, 8, 9)
        avl.remove(9)

        self.assertNotIn(9, avl)


    def testAVLInsertFiveDepthRemoveParentRightChild(self):
        avl = AVLTree(5, 7, 1, 6, 8, 10)
        avl.remove(10)

        self.assertNotIn(10, avl)


    def testAVLInsertFiveDepthRemoveRootParentTwoChild(self):
        avl = AVLTree(12, 4, 11, 7, 1, 6, 5, 8, 10)
        avl.remove(6)

        self.assertNotIn(6, avl)


    def testAVLInsertTenDepthRemoveParentTwoChild(self):
        avl = AVLTree(12, 4, 11, 7, 1, 6, 5, 8, 10)
        avl.remove(4)

        self.assertNotIn(4, avl)

    def testAVLInsertTenDepthRemoveLeftParentTwoChild(self):
        avl = AVLTree(17, 5, 39, 0, 15, 29, 49, 29, 45)
        avl.remove(5)

        self.assertNotIn(5, avl)


unittest.main()
