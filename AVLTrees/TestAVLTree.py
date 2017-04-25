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

        if abs(l - r) > 1:
            avl.traverse(avl._r)
        self.assertLess(abs(l - r), 2)


    def testAVLInsertFiveDepthRemoveOne(self):
        avl = AVLTree(12, 24, 5, 7, 1, 6, 8, 9, 18)
        avl.remove(7)

        l = 0
        r = 0

        if avl._r.get_left():
            l = avl._r.get_left().get_height()
        if avl._r.get_right():
            r = avl._r.get_right().get_height()

        self.assertNotIn(7, avl)


    def testAVLInsertFiveDepthRemoveOneHeightTwo(self):
        avl = AVLTree(12, 24, 5, 7, 1, 6, 8, 9, 18)
        avl.remove(7)

        l = 0
        r = 0

        if avl._r.get_left():
            l = avl._r.get_left().get_height()
        if avl._r.get_right():
            r = avl._r.get_right().get_height()

        self.assertLess(abs(l - r), 2)


unittest.main()
