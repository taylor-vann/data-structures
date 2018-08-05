"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for in order module

Requirements:
- unittest
- InOrder.py
- BSTree.py
"""

import unittest
from InOrder import in_order
from InOrder import rec_in_order
from InOrder import itr_in_order
from LevelOrder import level_order
from BSTree import BSTree

class TestPostOrderDefinitions(unittest.TestCase):

    def testPostOrderRecursive(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        expt = [1, 3, 4, 5, 6, 7, 8]
        t = in_order(tree._root)
        self.assertEqual(t, expt)


    def testPostOrderRecursivePostOrder(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        t = rec_in_order(tree._root)


    def testPostOrderIterPostOrder(self):
        tree = BSTree(5, 3, 7, 1, 4, 6, 8)

        expt = [1, 3, 4, 5, 6, 7, 8]
        t = itr_in_order(tree._root)
        level_order(tree._root)
        self.assertEqual(t, expt)


unittest.main()
