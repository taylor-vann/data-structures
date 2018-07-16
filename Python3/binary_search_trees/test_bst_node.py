"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from binary_search_tree import BSTNode


class TestBSTNode(unittest.TestCase):

    def test_bst_node_is_not_none(self):
        node = BSTNode()
        self.assertIsNotNone(node)


    def test_bst_node_data_is_not_none(self):
        node = BSTNode(3)
        self.assertIsNotNone(node.data)


    def test_bst_node_data_is_equal(self):
        node = BSTNode(3)
        self.assertEqual(node.data, 3)


    def test_bst_node_data_right_is_none(self):
        node = BSTNode(3, None, None)
        self.assertIsNone(node.right)


    def test_bst_node_data_left_is_none(self):
        node = BSTNode(3, None, None)
        self.assertIsNone(node.right)


    def test_bst_node_set_data(self):
        node = BSTNode()
        node.data = 2
        self.assertEqual(node.data, 2)


    def test_bst_node_set_left_none(self):
        node = BSTNode()
        node.left = None
        self.assertIsNone(node.left)


    def test_bst_node_set_left(self):
        node1 = BSTNode()
        node2 = BSTNode()
        node1.left = node2
        self.assertEqual(node1.left, node2)


    def test_bst_node_set_right_none(self):
        node = BSTNode()
        node.right = None
        self.assertIsNone(node.right)


    def test_bst_node_set_right(self):
        node1 = BSTNode()
        node2 = BSTNode()
        node1.right = node2
        self.assertEqual(node1.right, node2)


unittest.main()
