"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest

from binary_search_tree import BinarySearchTree
from pre_order import pre_order
from pre_order import iterative_pre_order

class TestPreOrderDefinitions(unittest.TestCase):

    def test_pre_order_recursive(self):
        tree = BinarySearchTree(5, 3, 7, 1, 4, 6, 8)
        expected = [5, 3, 1, 4, 7, 6, 8]

        self.assertEqual(pre_order(tree._root, []), expected)


    def test_pre_order_recursive_one(self):
        tree = BinarySearchTree(5)
        expected = [5]

        self.assertEqual(pre_order(tree._root, []), expected)


    def test_pre_order_recursive_none(self):
        tree = BinarySearchTree()
        expected = []

        self.assertEqual(pre_order(tree._root, []), expected)


    def test_pre_order_iterartive(self):
        tree = BinarySearchTree(5, 3, 7, 1, 4, 6, 8)
        expected = [5, 3, 1, 4, 7, 6, 8]

        self.assertEqual(iterative_pre_order(tree._root), expected)


    def test_pre_order_iterartive_one(self):
        tree = BinarySearchTree(5)
        expected = [5]

        self.assertEqual(iterative_pre_order(tree._root), expected)


    def test_pre_order_iterartive_none(self):
        tree = BinarySearchTree()
        expected = []

        self.assertEqual(iterative_pre_order(tree._root), expected)

if __name__ == "__main__":
    unittest.main()
