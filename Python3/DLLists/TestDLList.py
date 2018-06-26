"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for Doubly Linked List class

Requirements:
- unittest
- DLList.py
"""

import unittest
from DLList import DLList

class TestDLListMethods(unittest.TestCase):

    def testDLListIsNone(self):
        dlist = None
        self.assertIsNone(dlist)


    def testDLListIsNotNone(self):
        dlist = DLList()
        self.assertIsNotNone(dlist)


    def testDLListIsInstance(self):
        dlist = DLList()
        self.assertIsInstance(dlist, DLList)


    def testDLListPeekIsNone(self):
        dlist = DLList()
        self.assertIsNone(dlist.peek())


    def testDLListPeekIsNotNone(self):
        dlist = DLList()
        dlist.unshift(1)
        self.assertIsNotNone(dlist.peek())


    def testDLListPeekIsEqual(self):
        dlist = DLList()
        dlist.unshift(2)
        self.assertEqual(dlist.peek(), 2)


    def testDLListPushTwoPopThreeIsNone(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.pop()
        dlist.pop()
        dlist.pop()
        self.assertIsNone(dlist.peek())


    def testDLListPushThreePeekIsEqual(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.unshift(3)
        self.assertEqual(dlist.peek(), 3)


    def testDLListPushThreePopOneIsEqual(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.unshift(3)
        dlist.pop()
        self.assertEqual(dlist.peek(), 3)


    def testDLListUnshiftIsEqual(self):
        dlist = DLList()
        dlist.unshift(1)
        self.assertEqual(dlist.peek(), 1)


    def testDLListUnshiftThreeIsEqual(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.unshift(3)
        self.assertEqual(dlist.peek_last(), 1)


    def testDLListUnshiftTwoPopOne(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.pop()
        self.assertEqual(dlist.peek(), 2)


    def testDLListUnshiftTwoPopTwo(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.pop()
        dlist.pop()
        self.assertEqual(dlist.peek(), None)


    def testDLListShiftEmptyIsNone(self):
        dlist = DLList()
        dlist.shift()
        self.assertIsNone(dlist.peek_last())


    def testDLListUnshiftTwoShiftIsEqual(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.shift()
        self.assertEqual(dlist.peek_last(), 1)


    def testDLListUnshiftTwoShiftIsEqual(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.unshift(3)
        dlist.unshift(4)
        dlist.shift()
        dlist.shift()
        dlist.pop()
        self.assertEqual(dlist.peek_last(), 1)


    def testDLListSearchIsNone(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.unshift(3)
        dlist.unshift(4)
        self.assertNotIn(5, dlist)


    def testDLListSearchIsNotNone(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.unshift(3)
        dlist.unshift(4)
        self.assertIn(1, dlist)


    def testDLListGetNodeIsNone(self):
        dlist = DLList(1, 2, 3, 4)
        self.assertIsNone(dlist.find(5))


    def testDLListGetNodeEquals(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.find(4)
        self.assertEqual(bit.data, 4)


    def testDLListpopNodeIsNone(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.remove(5)
        self.assertIsNone(bit)


    def testDLListpopNodeIsEqual(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.pop()
        self.assertEqual(bit, 4)


    def testDLListpopIsGone(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.remove(3)
        self.assertIsNone(dlist.find(3))


    def testDLListunshiftAfterEmpty(self):
        dlist = DLList()
        bit = dlist.remove(3)
        self.assertNotIn(3, dlist)


    def testDLListunshiftAfter(self):
        dlist = DLList(1, 3, 4)
        bit = dlist.remove(4)
        self.assertIn(3, dlist)


    def test_DLList_unshift_remove_after(self):
        dlist = DLList(1, 3, 4)
        bit = dlist.remove(4)
        self.assertNotIn(4, dlist)


unittest.main()
