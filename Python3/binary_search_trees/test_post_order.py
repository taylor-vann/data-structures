"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for post order module

Requirements:
- unittest
- PostOrder.py
- BSTree.py
"""

import unittest
from PostOrder import post_order
from PostOrder import rec_post_order
from PostOrder import itr_post_order
from LevelOrder import level_order
from BSTree import BSTree

class TestPostOrderDefinitions(unittest.TestCase):

    def testPostOrderRecursive(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        expt = [1, 4, 3, 6, 8, 7, 5]
        t = post_order(tree._root)
        self.assertEqual(t, expt)


    def testPostOrderRecursivePostOrder(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        t = rec_post_order(tree._root)


    def testPostOrderIterPostOrder(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        expt = [1, 4, 3, 6, 8, 7, 5]
        t = itr_post_order(tree._root)
        self.assertEqual(t, expt)


    def testFiveIterPostOrder(self):
        tree = BSTree(5, 7, 1, 6, 8)

        expt = [1, 6, 8, 7, 5]
        t = itr_post_order(tree._root)
        self.assertEqual(t, expt)


if __name__ == "__main__":
    unittest.main()
