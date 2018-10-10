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

    def test_avl_insert_one_height_zero(self):
        avl = AVLTree(1)

        self.assertEqual(avl._root.height, 0)


    def test_avl_insert_two(self):
        avl = AVLTree(1, 2)

        self.assertIn(2, avl)


    def test_avl_insert_two_height_one(self):
        avl = AVLTree(1, 2)

        self.assertEqual(avl._root.height, 1)


    def test_avl_insert_two_right_height_one(self):
        avl = AVLTree(1, 2)

        self.assertEqual(avl._root.right.height, 0)


    def test_avl_insert_two_left_height_one(self):
        avl = AVLTree(2, 1)

        self.assertEqual(avl._root.left.height, 0)


    def test_avl_insert_two_balance_negative_one(self):
        avl = AVLTree(2, 1)

        self.assertEqual(avl._get_balance(avl._root), -1)


    def test_avl_insert_two_balance_negative_one(self):
        avl = AVLTree(1, 2)

        self.assertEqual(avl._get_balance(avl._root), 1)


    def test_avl_insert_three_adjust_one_right_heavy(self):
        avl = AVLTree(1, 2, 3)
        result = []
        expected = [[2], [1, 3]]
        level_order(avl._root, func=lambda x: result.append(x))

        self.assertEqual(result, expected)


    def test_avl_insert_three_adjust_one_left_heavy(self):
        avl = AVLTree(3, 2, 1)
        result = []
        expected = [[2], [1, 3]]
        level_order(avl._root, func=lambda x: result.append(x))

        self.assertEqual(result, expected)


    def test_avl_insert_three_adjust_one_right_left_heavy(self):
        avl = AVLTree(2, 4, 3)
        result = []
        expected = [[3], [2, 4]]
        level_order(avl._root, func=lambda x: result.append(x))

        self.assertEqual(result, expected)


    def test_avl_insert_three_adjust_one_left_right_heavy(self):
        avl = AVLTree(3, 1, 2)
        result = []
        expected = [[2], [1, 3]]
        level_order(avl._root, func=lambda x: result.append(x))

        self.assertEqual(result, expected)


    def test_avl_insert_three_left_right_root_height(self):
        avl = AVLTree(3, 1, 2)

        self.assertEqual(avl._root.height, 1)


    def test_avl_insert_three_left_right_height_of_right(self):
        avl = AVLTree(3, 1, 2)

        self.assertEqual(avl._root.right.height, 0)


    def test_avl_insert_three_left_right_height_of_right(self):
        avl = AVLTree(3, 1, 2)

        self.assertEqual(avl._root.left.height, 0)


    def test_avl_insert_three_root_height_one(self):
        avl = AVLTree(1, 2, 3)

        self.assertEqual(avl._root.height, 1)


    def test_avl_insert_four_to_left_height_two(self):
        avl = AVLTree(4, 3, 2, 1)

        self.assertEqual(avl._root.height, 2)


    def test_avl_insert_four_to_right_height_two(self):
        avl = AVLTree(1, 2, 3, 4)

        self.assertEqual(avl._root.height, 2)


    def test_avl_insert_four_to_right_correct_levels(self):
        avl = AVLTree(1, 2, 3, 4)

        self.assertEqual(avl._root.height, 2)


    def test_avl_insert_four_to_left_correct_levels(self):
        avl = AVLTree(4, 3, 2, 1)

        self.assertEqual(avl._root.height, 2)


    def test_avl_insert_five_to_left_correct_levels(self):
        avl = AVLTree(5, 4, 3, 2, 1)

        self.assertEqual(avl._root.height, 2)


    def test_avl_insert_five_to_right_correct_levels(self):
        avl = AVLTree(1, 2, 3, 4, 5)

        self.assertEqual(avl._root.height, 2)


    def test_avl_insert_ten_to_left_correct_levels(self):
        avl = AVLTree(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

        self.assertEqual(avl._root.height, 3)


    def test_avl_insert_hundred_correct_levels(self):
        avl = AVLTree()

        for j in range(100):
            avl.insert(j)

        level_order(avl._root)

        self.assertEqual(avl._root.height, 6)



if __name__ == "__main__":
    unittest.main()
