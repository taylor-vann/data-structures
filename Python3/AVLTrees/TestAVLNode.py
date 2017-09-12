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


    def testAVLDataNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.get_data())


    def testAVLData(self):
        nd = AVLNode()
        nd.set_data(3)
        bit = nd.get_data()
        self.assertEqual(nd.get_data(), 3)


    def testAVLNodeLeftNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.get_left())


    def testAVLNodeRightNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.get_right())


    def testAVLNodeLeft(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.set_left(nd)
        self.assertIsInstance(nd.get_left(), AVLNode)


    def testAVLNodeRight(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.set_right(nd1)
        self.assertIsInstance(nd.get_right(), AVLNode)


    def testAVLNodeHeightOne(self):
        nd = AVLNode()
        self.assertEqual(nd.get_height(), 1)


    def testAVLNodeBothHeightTwo(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.set_left(nd1)
        self.assertEqual(nd.get_height(), 2)


    def testAVLNodeBothHeightTwo(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd2 = AVLNode()
        nd.set_left(nd1)
        nd.set_right(nd2)
        self.assertEqual(nd.get_height(), 2)


    def testAVLNodeBothHeightThree(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd2 = AVLNode()
        nd.set_left(nd1)
        nd1.set_right(nd2)
        self.assertEqual(nd.get_height(), 3)


unittest.main()
