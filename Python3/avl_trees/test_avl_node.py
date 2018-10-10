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

    def testAVLValueNone(self):
        nd = AVLNode()
        self.assertIsNone(nd.value)

    def testAVLValue(self):
        nd = AVLNode()
        nd.value = 3
        self.assertEqual(nd.value, 3)

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

    def testAVLNodeRight(self):
        nd = AVLNode()
        nd1 = AVLNode()
        nd.right = nd1
        self.assertIsInstance(nd.right, AVLNode)

    def testAVLHeightNone(self):
        nd = AVLNode()
        self.assertEqual(nd.height, 0)

    def testAVLHeight(self):
        nd = AVLNode()
        nd.height = 3
        self.assertEqual(nd.height, 3)

if __name__ == "__main__":
    unittest.main()
