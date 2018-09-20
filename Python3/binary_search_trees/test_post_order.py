"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest

from binary_search_tree import BinarySearchTree
from post_order import post_order
from post_order import post_order_iterative


class TestPreOrder(unittest.TestCase):

    def test_post_order_recursive_exits(self):
        self.assertIsNotNone(post_order)


    def test_post_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        post_result = []
        post_order(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        post_result = []
        post_order(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_correct_one(self):
        result = [1]
        tree = BinarySearchTree(1)
        post_result = []
        post_order(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_correct_four(self):
        result = [4, 3, 2, 1]
        tree = BinarySearchTree(1, 2, 3, 4)
        post_result = []
        post_order(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_correct_seven(self):
        result = [1, 4, 3, 6, 8, 7, 5]
        tree = BinarySearchTree(5, 3, 1, 4, 7, 6, 8)
        post_result = []
        post_order(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_iterative_exists(self):
        self.assertIsNotNone(post_order_iterative)


    def test_post_order_iterative_correct_none(self):
        result = []
        tree = BinarySearchTree()
        post_result = []
        post_order_iterative(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_iterative_correct_none(self):
        result = []
        tree = BinarySearchTree()
        post_result = []
        post_order_iterative(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_iterative_correct_one(self):
        result = [1]
        tree = BinarySearchTree(1)
        post_result = []
        post_order_iterative(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_iterative_correct_four(self):
        result = [4, 3, 2, 1]
        tree = BinarySearchTree(1, 2, 3, 4)
        post_result = []
        post_order_iterative(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


    def test_post_order_iterative_correct_seven(self):
        result = [1, 4, 3, 6, 8, 7, 5]
        tree = BinarySearchTree(5, 3, 1, 4, 7, 6, 8)
        post_result = []
        post_order_iterative(tree._root, func=lambda x: post_result.append(x.value))

        self.assertEqual(result, post_result)


if __name__ == "__main__":
    unittest.main()
