"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest

from binary_search_tree import BinarySearchTree
from level_order import level_order


class TestInOrder(unittest.TestCase):

    def test_level_order_recursive_exits(self):
        self.assertIsNotNone(level_order)


    def test_level_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        level_result = []
        level_order(tree._root, func=lambda x: level_result.append(x))

        self.assertEqual(result, level_result)


    def test_level_order_correct_none(self):
        result = []
        tree = BinarySearchTree()
        level_result = []
        level_order(tree._root, func=lambda x: level_result.append(x))

        self.assertEqual(result, level_result)


    def test_level_order_correct_one(self):
        result = [[1]]
        tree = BinarySearchTree(1)
        level_result = []
        level_order(tree._root, func=lambda x: level_result.append(x))

        self.assertEqual(result, level_result)


    def test_level_order_correct_four(self):
        result = [[1], [2], [3], [4]]
        tree = BinarySearchTree(1, 2, 3, 4)
        level_result = []
        level_order(tree._root, func=lambda x: level_result.append(x))

        self.assertEqual(result, level_result)


    def test_level_order_correct_seven(self):
        result = [[5], [3, 7], [1, 4, 6, 8]]
        tree = BinarySearchTree(5, 3, 1, 4, 7, 6, 8)
        level_result = []
        level_order(tree._root, func=lambda x: level_result.append(x))

        self.assertEqual(result, level_result)


if __name__ == "__main__":
    unittest.main()
