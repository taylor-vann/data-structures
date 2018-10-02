"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from avl_tree import AVLTree
from avl_tree_test_helpers import post_order
from avl_tree_test_helpers import level_order



class TestAVLTreeMethods(unittest.TestCase):

    def test_avl_not_none(self):
        avl = AVLTree()

        self.assertIsNotNone(avl)

    def test_avl_insert_one(self):
        avl = AVLTree(1)

        self.assertIn(1, avl)


    def test_avl_insert_two(self):
        avl = AVLTree(1, 2)

        self.assertIn(2, avl)

    def test_avl_insert_two_adjust_one(self):
        avl = AVLTree(1, 2, 3)
        result = []
        expected = [[2], [1, 3]]
        level_order(avl._root, func=lambda x: result.append(x))

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
