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


    def testAVLNodeHeightZero(self):
        nd = AVLNode()
        self.assertEqual(nd.getHeight(), 0)


    def testAVLNodeBalanceZero(self):
        nd = AVLNode()
        self.assertEqual(nd.getBalance(), 0)


unittest.main()
