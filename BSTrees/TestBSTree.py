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


    def testBSTreeInsertTwoContains(self):
        bstree = BSTree()
        bstree.insert(1)
        bstree.insert(2)
        self.assertIn(2, bstree)


    def testBSTreeInsertFivecContains(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        self.assertIn(5, bstree)


    def testBSTreeInsertFiveNotContains(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        self.assertNotIn(2, bstree)


    def testBSTreeInsertFiveRemoveNone(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        bstree.remove(7)
        self.assertNotIn(7, bstree)


    def testBSTreeInsertFiveRemoveChildWithNone(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        bstree.remove(5)
        self.assertNotIn(5, bstree)


    def testBSTreeInsertFiveRemoveChildWithOne(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(1)
        bstree.remove(3)
        self.assertNotIn(3, bstree)


    def testBSTreeInsertFiveRemoveChildWithTwo(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(7)
        bstree.insert(1)
        bstree.remove(6)
        self.assertNotIn(6, bstree)


    def testBSTreeInsertFiveRemoveStillHas(self):
        bstree = BSTree(4, 3, 6)
        bstree.insert(5)
        bstree.insert(7)
        bstree.insert(1)
        bstree.remove(6)
        self.assertIn(5, bstree)


    def testBSTreeInsertSevenRemoveStillHasTwo(self):
        bstree = BSTree(4, 3, 6, 5, 8, 7, 9)
        bstree.remove(6)
        self.assertIn(8, bstree)


    def testBSTreeInsertSevenRemoveTwo(self):
        bstree = BSTree(4, 3, 6, 5, 8, 7, 9)
        bstree.remove(6)
        self.assertNotIn(6, bstree)


    def testBSTreeInsertSevenRemoveTwoNone(self):
        bstree = BSTree(4, 3, 6, 5, 8, 7, 9)
        bstree.remove(6)
        bstree.remove(9)
        self.assertNotIn(9, bstree)


    def testBSTreeInsertTenRemoveTwoNone(self):
        bstree = BSTree(4, 2, 3, 1, 6, 10, 9, 7, 8, 11)
        bstree.remove(6)
        bstree.remove(10)
        self.assertNotIn(10, bstree)


    def testBSTreeRemoveRoot(self):
        bstree = BSTree(4, 2, 3, 1, 6, 10, 9, 7, 8, 11)
        bstree.remove(4)
        bstree.remove(10)
        self.assertNotIn(4, bstree)


    def testBSTreeRemoveRoot(self):
        bstree = BSTree(4, 2, 3, 1, 6, 10, 9, 7, 8, 11)
        bstree.remove(4)
        bstree.remove(10)
        self.assertNotIn(4, bstree)



unittest.main()
