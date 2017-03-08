"""
Brian Taylor Vann
github.com/taylor-vann

Unit tests for SLList class
"""

import unittest
from SLList import SLList


class TestSLList(unittest.TestCase):

    def testSLListIsNotNone(self):
        slist = SLList()
        self.assertIsNotNone(slist)


    def testSLListPeekIsNone(self):
        slist = SLList()
        self.assertIsNone(slist.peek())


    def testSLListPeekNotNone(self):
        slist = SLList()
        slist.insert("dude")
        self.assertIsNotNone(slist.peek())


    def testSLListInsertThreePeekCorrect(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.insert(3)
        self.assertEqual(slist.peek(), 1)


    def testSLListEmptyRemoveNone(self):
        slist = SLList()
        slist.remove();
        self.assertIsNone(slist.peek())


    def testSLListInsertOnceRemoveTwice(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.remove()
        self.assertEqual(slist.peek(), 2)


    def testSLListRemoveIsData(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        self.assertEqual(slist.remove(), 1)


    def testSLListInsertAfterEmpty(self):
        slist = SLList()
        slist.insert_after(1, 3)
        self.assertEqual(slist.peek(), 1)


    def testSLListInsertAfterThreeRemoveOnce(self):
        slist = SLList()
        slist.insert_after(1, 3)
        slist.insert_after(2, 1)
        slist.insert_after(3, 1)
        slist.remove()
        self.assertEqual(slist.peek(), 3)


    def testSearchNone(self):
        slist = SLList()
        self.assertFalse(slist.search(1))

 
    def testSearchThreeFalse(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.insert(3)
        self.assertFalse(slist.search(4))


    def testSearchThreeTrue(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.insert(3)
        self.assertTrue(slist.search(3))


    def testContainsFalse(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.insert(3)
        self.assertNotIn(4, slist)


    def testContainsTrue(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.insert(3)
        self.assertIn(1, slist)


    def testContainsInitTrue(self):
        slist = SLList(1, 2, 3)
        self.assertIn(1, slist)


unittest.main()        
