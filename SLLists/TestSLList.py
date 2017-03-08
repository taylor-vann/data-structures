"""
Brian Taylor Vann
github.com/taylor-vann

Unit tests for SLList class
"""

import unittest
from SLNode import SLNode
from SLList import SLList

class TestSLList(unittest.TestCase):

    def testSLListIsNotNone(self):
        slist = SLList()
        self.assertIsNotNone(slist)

    def testSLListPeekIsNone(self):
        slist = SLList()
        slist.insert("yo")
        self.assertIsNone(slist.peek())

    def testSLListPeekNotNone(self):
        slist = SLList()
        node1 = SLNode("yo", "dude")
        slist.insert(node1)
        self.assertIsNotNone(slist.peek())

    def testSLListInsertThreePeekCorrect(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        slist.insert(node1)
        slist.insert(node2)
        slist.insert(node3)
        self.assertEqual(slist.peek(), 1)

    def testSLListEmptyRemoveNone(self):
        slist = SLList()
        slist.remove();
        self.assertIsNone(slist.peek())

    def testSLListInsertOnceRemoveTwice(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        slist.insert(node1)
        slist.insert(node2)
        slist.remove()
        self.assertEqual(slist.peek(), 2)

    def testSLListRemoveIsData(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        slist.insert(node1)
        slist.insert(node2)
        self.assertEqual(slist.remove(), 1)

    def testSLListInsertAfterEmpty(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        slist.insert_after(node1, 3)
        self.assertEqual(slist.peek(), 1)

    def testSLListInsertAfterThreeRemoveOnce(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        slist.insert_after(node1, 3)
        slist.insert_after(node2, 1)
        slist.insert_after(node3, 1)
        slist.remove()
        self.assertEqual(slist.peek(), 3)

    def testSearchNone(self):
        slist = SLList()
        self.assertFalse(slist.search(1))
 
    def testSearchThreeFalse(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        slist.insert(node1)
        slist.insert(node2)
        slist.insert(node3)
        self.assertFalse(slist.search(4))

    def testSearchThreeTrue(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        slist.insert(node1)
        slist.insert(node2)
        slist.insert(node3)
        self.assertTrue(slist.search(3))

    def testContainsFalse(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        slist.insert(node1)
        slist.insert(node2)
        slist.insert(node3)
        self.assertNotIn(4, slist)

    def testContainsTrue(self):
        slist = SLList()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        slist.insert(node1)
        slist.insert(node2)
        slist.insert(node3)
        self.assertIn(1, slist)

unittest.main()        
