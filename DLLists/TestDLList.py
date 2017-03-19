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
        dlist.insert(1)
        self.assertIsNotNone(dlist.peek())


    def testDLListPeekIsEqual(self):
        dlist = DLList()
        dlist.insert(2)
        self.assertEqual(dlist.peek(), 2)


    def testDLListPushTwoPopThreeIsNone(self):
        dlist = DLList()
        dlist.insert(1)
        dlist.insert(2)
        dlist.remove()
        dlist.remove()
        dlist.remove()
        self.assertIsNone(dlist.peek())


    def testDLListPushThreePeekIsEqual(self):
        dlist = DLList()
        dlist.insert(1)
        dlist.insert(2)
        dlist.insert(3)
        self.assertEqual(dlist.peek(), 3)


    def testDLListPushThreePopOneIsEqual(self):
        dlist = DLList()
        dlist.insert(1)
        dlist.insert(2)
        dlist.insert(3)
        dlist.remove()
        self.assertEqual(dlist.peek(), 2)


    def testDLListUnshiftIsEqual(self):
        dlist = DLList()
        dlist.unshift(1)
        self.assertEqual(dlist.peek(), 1)


    def testDLListUnshiftThreeIsEqual(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.unshift(3)
        self.assertEqual(dlist.peek_last(), 3)


    def testDLListUnshiftTwoPopOne(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.remove()
        self.assertEqual(dlist.peek(), 2)


    def testDLListUnshiftTwoPopTwo(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.remove()
        dlist.remove()
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
        dlist.insert(3)
        dlist.insert(4)
        dlist.shift()
        dlist.shift()
        dlist.remove()
        self.assertEqual(dlist.peek_last(), 3)


    def testDLListSearchIsNone(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.insert(3)
        dlist.insert(4)
        self.assertNotIn(5, dlist)


    def testDLListSearchIsNotNone(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.insert(3)
        dlist.insert(4)
        self.assertIn(1, dlist)


    def testDLListGetNodeIsNone(self):
        dlist = DLList(1, 2, 3, 4)
        self.assertIsNone(dlist.find(5))


    def testDLListGetNodeEquals(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.find(4)
        self.assertEqual(bit.get_data(), 4)


    def testDLListRemoveNodeIsNone(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.remove_data(5)
        self.assertIsNone(bit)


    def testDLListRemoveNodeIsEqual(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.remove_data(4)
        self.assertEqual(bit, 4)


    def testDLListRemoveIsGone(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.remove_data(3)
        self.assertIsNone(dlist.find(3))


    def testDLListInsertAfterEmpty(self):
        dlist = DLList()
        bit = dlist.insert_after(3, 5)
        self.assertIn(3, dlist)


    def testDLListInsertAfter(self):
        dlist = DLList(1, 3, 4)
        bit = dlist.insert_after(2, 4)
        self.assertIn(2, dlist)


    def testDLListInsertAfter(self):
        dlist = DLList(1, 3, 4)
        bit = dlist.insert_after(2, 5)
        self.assertIn(2, dlist)


unittest.main()
