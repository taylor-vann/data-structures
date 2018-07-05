"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from binary_search_tree import BSTNode


class TestBSTNode(unittest.TestCase):

    def testBSTNodeIsNotNone(self):
        node = BSTNode()
        self.assertIsNotNone(node)


    def testBSTNodeDataIsNotNone(self):
        node = BSTNode(3)
        self.assertIsNotNone(node.data)


    def testBSTNodeDataIsEqual(self):
        node = BSTNode(3)
        self.assertEqual(node.data, 3)


    def testBSTNodeDataRightIsNone(self):
        node = BSTNode(3, None, None)
        self.assertIsNone(node.right)


    def testBSTNodeDataLeftIsNone(self):
        node = BSTNode(3, None, None)
        self.assertIsNone(node.right)


    def testBSTNodeSetData(self):
        node = BSTNode()
        node.data = 2
        self.assertEqual(node.data, 2)


    def testBSTNodeSetLeftNone(self):
        node = BSTNode()
        node.left = None
        self.assertIsNone(node.left)


    def testBSTNodeSetLeft(self):
        node1 = BSTNode()
        node2 = BSTNode()
        node1.left = node2
        self.assertEqual(node1.left, node2)


    def testBSTNodeSetRightNone(self):
        node = BSTNode()
        node.right = None
        self.assertIsNone(node.right)


    def testBSTNodeSetRight(self):
        node1 = BSTNode()
        node2 = BSTNode()
        node1.right = node2
        self.assertEqual(node1.right, node2)


unittest.main()
