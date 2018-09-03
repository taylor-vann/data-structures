"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest

from binary_search_tree import BinarySearchTree
from pre_order import pre_order
from pre_order import pre_order_iterative


class TestPreOrderDefinitions(unittest.TestCase):

    def test_pre_order_recursive_exits(self):
        self.assertIsNotNone(pre_order)


    def test_pre_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        pre_result = []
        pre_order(tree._root, func=lambda x: pre_result.append(x.value))

        self.assertEqual(result, pre_result)


    def test_pre_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        pre_result = []
        pre_order(tree._root, func=lambda x: pre_result.append(x.value))

        self.assertEqual(result, pre_result)


    def test_pre_order_correct_one(self):
        result = [1]
        tree = BinarySearchTree(1)
        pre_result = []
        pre_order(tree._root, func=lambda x: pre_result.append(x.value))

        self.assertEqual(result, pre_result)


    def test_pre_order_correct_four(self):
        result = [1, 2, 3, 4]
        tree = BinarySearchTree(1, 2, 3, 4)
        pre_result = []
        pre_order(tree._root, func=lambda x: pre_result.append(x.value))

        self.assertEqual(result, pre_result)


    def test_pre_order_correct_seven(self):
        result = [5, 3, 1, 4, 7, 6, 8]
        tree = BinarySearchTree(5, 3, 1, 4, 7, 6, 8)
        pre_result = []
        pre_order(tree._root, func=lambda x: pre_result.append(x.value))

        self.assertEqual(result, pre_result)


    def test_pre_order_iterative_exists(self):
        self.assertIsNotNone(pre_order_iterative)


    def test_pre_order_iterative_correct_none(self):
        result = []
        tree = BinarySearchTree()

        self.assertEqual(result, pre_order_iterative(tree._root))


    def test_pre_order_iterative_correct_none(self):
        result = []
        tree = BinarySearchTree()

        self.assertEqual(result, pre_order_iterative(tree._root))


    def test_pre_order_iterative_correct_one(self):
        result = [1]
        tree = BinarySearchTree(1)

        self.assertEqual(result, pre_order_iterative(tree._root))


    def test_pre_order_iterative_correct_four(self):
        result = [1, 2, 3, 4]
        tree = BinarySearchTree(1, 2, 3, 4)

        self.assertEqual(result, pre_order_iterative(tree._root))


    def test_pre_order_iterative_correct_seven(self):
        result = [5, 3, 1, 4, 7, 6, 8]
        tree = BinarySearchTree(5, 3, 1, 4, 7, 6, 8)

        self.assertEqual(result, pre_order_iterative(tree._root))


if __name__ == "__main__":
    unittest.main()
