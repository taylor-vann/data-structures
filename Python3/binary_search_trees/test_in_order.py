"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest

from binary_search_tree import BinarySearchTree
from in_order import in_order
from in_order import in_order_iterative


class TestInOrder(unittest.TestCase):

    def test_in_order_recursive_exits(self):
        self.assertIsNotNone(in_order)


    def test_in_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        in_result = []
        in_order(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        in_result = []
        in_order(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_correct_one(self):
        result = [1]
        tree = BinarySearchTree(1)
        in_result = []
        in_order(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_correct_four(self):
        result = [1, 2, 3, 4]
        tree = BinarySearchTree(1, 2, 3, 4)
        in_result = []
        in_order(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_correct_seven(self):
        result = [1, 3, 4, 5, 6, 7, 8]
        tree = BinarySearchTree(5, 3, 1, 4, 7, 6, 8)
        in_result = []
        in_order(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_iterative_exists(self):
        self.assertIsNotNone(in_order_iterative)


    def test_in_order_iterative_correct_none(self):
        result = []
        tree = BinarySearchTree()
        in_result = []
        in_order_iterative(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_iterative_correct_none(self):
        result = []
        tree = BinarySearchTree()
        in_result = []
        in_order_iterative(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_iterative_correct_one(self):
        result = [1]
        tree = BinarySearchTree(1)
        in_result = []
        in_order_iterative(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_iterative_correct_four(self):
        result = [1, 2, 3, 4]
        tree = BinarySearchTree(1, 2, 3, 4)
        in_result = []
        in_order_iterative(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


    def test_in_order_iterative_correct_seven(self):
        result = [1, 3, 4, 5, 6, 7, 8]
        tree = BinarySearchTree(5, 3, 1, 4, 7, 6, 8)
        in_result = []
        in_order_iterative(tree._root, func=lambda x: in_result.append(x.value))

        self.assertEqual(result, in_result)


if __name__ == "__main__":
    unittest.main()
