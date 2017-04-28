"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the BSTNode class

Requirements:
- unittest
- BSTNode.py
"""

import unittest
from BSTNode import BSTNode


class TestBSTNode(unittest.TestCase):

    def testBSTNodeIsNotNone(self):
        node = BSTNode()
        self.assertIsNotNone(node)


    def testBSTNodeDataIsNotNone(self):
        node = BSTNode(3)
        self.assertIsNotNone(node.get_data())


    def testBSTNodeDataIsEqual(self):
        node = BSTNode(3)
        self.assertEqual(node.get_data(), 3)


    def testBSTNodeDataRightIsNone(self):
        node = BSTNode(3, None, None)
        self.assertIsNone(node.get_right())


    def testBSTNodeDataLeftIsNone(self):
        node = BSTNode(3, None, None)
        self.assertIsNone(node.get_right())


    def testBSTNodeSetData(self):
        node = BSTNode()
        node.set_data(2)
        self.assertEqual(node.get_data(), 2)


    def testBSTNodeSetLeftNone(self):
        node = BSTNode()
        node.set_left(2)
        self.assertIsNone(node.get_left())


    def testBSTNodeSetLeft(self):
        node1 = BSTNode()
        node2 = BSTNode()
        node1.set_left(node2)
        self.assertEqual(node1.get_left(), node2)


    def testBSTNodeSetRightNone(self):
        node = BSTNode()
        node.set_right(2)
        self.assertIsNone(node.get_right())


    def testBSTNodeSetRight(self):
        node1 = BSTNode()
        node2 = BSTNode()
        node1.set_right(node2)
        self.assertEqual(node1.get_right(), node2)


unittest.main()
