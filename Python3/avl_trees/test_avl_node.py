"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from avl_tree import AVLNode


class TestAVLNodeMethods(unittest.TestCase):

    def testAVLNodeNotNone(self):
        nd = AVLNode()
        self.assertIsNotNone(nd)


    def testAVLDataNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.data)


    def testAVLData(self):
        nd = AVLNode()
        nd.data = 3
        bit = nd.data
        self.assertEqual(nd.data, 3)


    def testAVLNodeLeftNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.left)


    def testAVLNodeRightNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.right)


    def testAVLNodeLeft(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.left = nd
        self.assertIsInstance(nd.left, AVLNode)


    def testAVLNodeRight(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.right = nd1
        self.assertIsInstance(nd.right, AVLNode)


if __name__ == "__main__":
    unittest.main()
