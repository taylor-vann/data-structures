"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for pre order module

Requirements:
- unittest
- PreOrder.py
- BSTree.py
"""

import unittest
from PreOrder import pre_order
from PreOrder import rec_pre_order
from PreOrder import itr_pre_order
from LevelOrder import level_order
from BSTree import BSTree

class TestPostOrderDefinitions(unittest.TestCase):

    def testPostOrderRecursive(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        expt = [5, 3, 1, 4, 7, 6, 8]
        t = pre_order(tree._root)
        self.assertEqual(t, expt)


    def testPostOrderRecursivePostOrder(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        t = rec_pre_order(tree._root)


    def testPostOrderIterPostOrder(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        expt = [5, 3, 1, 4, 7, 6, 8]
        t = itr_pre_order(tree._root)
        level_order(tree._root)
        self.assertEqual(t, expt)


unittest.main()
