"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from simpler_binary_search_tree import SimplerBSTree


class TestBSTreeMethods(unittest.TestCase):

    def test_bstree_is_not_none(self):
        bstree = SimplerBSTree()
        self.assertIsNotNone(bstree)


    def test_bstree_root_not_none(self):
        bstree = SimplerBSTree()
        bstree.insert(1)
        self.assertIsNotNone(1 in bstree)


    def test_bstree_contains(self):
        bstree = SimplerBSTree()
        bstree.insert(1)
        self.assertIn(1, bstree)


    def test_bstree_not_contains(self):
        bstree = SimplerBSTree()
        bstree.insert(1)
        self.assertNotIn(2, bstree)


    def test_bstree_insert_two_contains(self):
        bstree = SimplerBSTree()
        bstree.insert(1)
        bstree.insert(2)
        self.assertIn(2, bstree)


    def test_bstree_insert_five_contains(self):
        bstree = SimplerBSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        self.assertIn(5, bstree)


    def test_bstree_insert_five_not_contains(self):
        bstree = SimplerBSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        self.assertNotIn(2, bstree)


    # def test_bstree_insert_five_remove_none(self):
    #     bstree = SimplerBSTree(4, 3, 6)
    #     bstree.insert(5)
    #     bstree.insert(1)
    #     bstree.remove(7)
    #     self.assertNotIn(7, bstree)
    #
    #
    # def test_bstree_insert_five_remove_child_with_none(self):
    #     bstree = SimplerBSTree(4, 3, 6)
    #     bstree.insert(5)
    #     bstree.insert(1)
    #     bstree.remove(5)
    #     self.assertNotIn(5, bstree)
    #
    #
    # def test_bstree_insert_five_remove_child_with_one(self):
    #     bstree = SimplerBSTree(4, 3, 6)
    #     bstree.insert(5)
    #     bstree.insert(1)
    #     bstree.remove(3)
    #     self.assertNotIn(3, bstree)
    #
    #
    # def test_bstree_insert_five_remove_child_with_two(self):
    #     bstree = SimplerBSTree(4, 3, 6)
    #     bstree.insert(5)
    #     bstree.insert(7)
    #     bstree.insert(1)
    #     bstree.remove(6)
    #     self.assertNotIn(6, bstree)
    #
    #
    # def test_bstree_insert_five_remove_two_has(self):
    #     bstree = SimplerBSTree(4, 3, 6)
    #     bstree.insert(5)
    #     bstree.insert(7)
    #     bstree.insert(1)
    #     bstree.remove(6)
    #     self.assertIn(5, bstree)
    #
    #
    # def test_bstree_insert_five_remove_still_has(self):
    #     bstree = SimplerBSTree(4, 3, 6)
    #     bstree.insert(5)
    #     bstree.insert(7)
    #     bstree.insert(1)
    #     bstree.remove(6)
    #     self.assertIn(5, bstree)
    #
    #
    # def test_bstree_insert_seven_remove_still_has_two(self):
    #     bstree = SimplerBSTree(4, 3, 6, 5, 8, 7, 9)
    #     bstree.remove(6)
    #     self.assertIn(8, bstree)
    #
    #
    # def test_bstree_insert_seven_remove_two(self):
    #     bstree = SimplerBSTree(4, 3, 6, 5, 8, 7, 9)
    #     bstree.remove(6)
    #     self.assertNotIn(6, bstree)
    #
    #
    # def test_bstree_insert_seven_temove_two_none(self):
    #     bstree = SimplerBSTree(4, 3, 6, 5, 8, 7, 9)
    #     bstree.remove(6)
    #     bstree.remove(9)
    #     self.assertNotIn(9, bstree)
    #
    #
    # def test_bstree_insert_ten_remove_two_none(self):
    #     bstree = SimplerBSTree(4, 2, 3, 1, 6, 10, 9, 7, 8, 11)
    #     bstree.remove(6)
    #     bstree.remove(10)
    #     self.assertNotIn(10, bstree)
    #
    #
    # def test_bstree_remove_root(self):
    #     bstree = SimplerBSTree(4)
    #     bstree.remove(4)
    #     self.assertNotIn(4, bstree)
    #
    #
    # def test_bst_remove_root_with_two_children(self):
    #     bstree = SimplerBSTree(4)
    #     bstree.insert(1)
    #     bstree.insert(6)
    #     bstree.remove(4)
    #     self.assertIn(1, bstree)
    #
    #
    # def test_bstree_remove_root_big_tree(self):
    #     bstree = SimplerBSTree(4, 2, 3, 1, 6, 10, 9, 7, 8, 11)
    #     bstree.remove(4)
    #     bstree.remove(10)
    #     self.assertNotIn(4, bstree)
    #
    #
    # def test_bstree_remove_root_has(self):
    #     bstree = SimplerBSTree(4, 2, 3, 1, 6, 10, 9, 7, 8, 11)
    #     bstree.remove(4)
    #     bstree.remove(10)
    #     self.assertIn(8, bstree)


if __name__ == "__main__":
    unittest.main()
