"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the BSTree class

Requirements:
- unittest
- BSTree.py
"""

import unittest
from BSTree import BSTree

class TestBSTreeMethods(unittest.TestCase):

    def testBSTreeIsNotNone(self):
        bstree = BSTree()
        self.assertIsNotNone(bstree) 


    def testBSTreeRootNotNone(self):
        bstree = BSTree()
        bstree.insert(1)
        self.assertIsNotNone(bstree.search(1))


    def testBSTreeContains(self):
        bstree = BSTree()
        bstree.insert(1)
        self.assertIn(1, bstree)


    def testBSTreeNotContains(self):
        bstree = BSTree()
        bstree.insert(1)
        self.assertNotIn(2, bstree)


    def testBSTreeInsert2Contains(self):
        bstree = BSTree()
        bstree.insert(1)
        bstree.insert(2)
        self.assertIn(2, bstree)


    def testBSTreeInsert5Contains(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        self.assertIn(5, bstree)


    def testBSTreeInsert5NotContains(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        self.assertNotIn(2, bstree)


unittest.main()
