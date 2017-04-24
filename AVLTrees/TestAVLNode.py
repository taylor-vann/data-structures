"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the AVLNode class

Requirements:
- unittest
- AVLNode.py
"""

import unittest
from AVLNode import AVLNode


class TestAVLNodeMethods(unittest.TestCase):

    def testAVLNodeNotNone(self):
        nd = AVLNode()
        self.assertIsNotNone(nd)


    def testAVLNodeParNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.getParent())


    def testAVLNodeLeftNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.getLeft())


    def testAVLNodeRightNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.getRight())


    def testAVLNodePar(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.setParent(nd)
        self.assertIsInstance(nd.getParent(), AVLNode)


    def testAVLNodeLeft(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.setLeft(nd)
        self.assertIsInstance(nd.getLeft(), AVLNode)


    def testAVLNodeRight(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.setRight(nd1)
        self.assertIsInstance(nd.getRight(), AVLNode)


    def testAVLNodeHeightOne(self):
        nd = AVLNode()
        self.assertEqual(nd.getHeight(), 1)


    def testAVLNodeBothHeightTwo(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.setLeft(nd1)
        self.assertEqual(nd.getHeight(), 2)


    def testAVLNodeBothHeightTwo(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd2 = AVLNode()
        nd.setLeft(nd1)
        nd.setRight(nd2)
        self.assertEqual(nd.getHeight(), 2)


    def testAVLNodeBothHeightThree(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd2 = AVLNode()
        nd.setLeft(nd1)
        nd1.setRight(nd2)
        self.assertEqual(nd.getHeight(), 3)


    def testAVLNodeBalanceZero(self):
        nd = AVLNode()
        self.assertEqual(nd.getBalance(), 0)


    def testAVLNodeBalanceLeft(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.setLeft(nd)
        self.assertEqual(nd.getBalance(), -1)


    def testAVLNodeBalanceRight(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.setRight(nd)
        self.assertEqual(nd.getBalance(), 1)


unittest.main()
