"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from  singly_linked_list import SLList


class TestSLList(unittest.TestCase):

    def test_sllist_is_not_none(self):
        slist = SLList()
        self.assertIsNotNone(slist)


    def test_sllist_peek_is_none(self):
        slist = SLList()
        self.assertIsNone(slist.peek())


    def test_sllist_peek_not_none(self):
        slist = SLList()
        slist.insert("dude")
        self.assertIsNotNone(slist.peek())


    def test_sllist_insert_three_peek(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.insert(3)
        self.assertEqual(slist.peek(), 1)


    def test_sllist_empty_remove_none(self):
        slist = SLList()
        slist.remove();
        self.assertIsNone(slist.peek())


    def test_sllist_insert_once_remove_twice(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        slist.remove()
        self.assertEqual(slist.peek(), 2)


    def test_sllist_remove_correct_data(self):
        slist = SLList()
        slist.insert(1)
        slist.insert(2)
        self.assertEqual(slist.remove(), 1)


    def test_sllist_insert_after_empty(self):
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


    def testRemoveValueStart(self):
        slist = SLList(1, 2, 3)
        slist.remove_data(1)
        self.assertNotIn(1, slist)


    def testRemoveValueStartContains2(self):
        slist = SLList(1, 2, 3)
        slist.remove_data(1)
        self.assertIn(2, slist)


    def testRemoveValueStartContains3(self):
        slist = SLList(1, 2, 3)
        slist.remove_data(1)
        self.assertIn(3, slist)


    def testRemoveValueMiddle(self):
        slist = SLList(1, 2, 3)
        slist.remove_data(2)
        self.assertNotIn(2, slist)


    def testRemoveValueEnd(self):
        slist = SLList(1, 2, 3)
        slist.remove_data(3)
        self.assertNotIn(3, slist)


    def testRemoveValueEndContains(self):
        slist = SLList(1, 2, 3)
        slist.remove_data(3)
        self.assertIn(1, slist)


if __name__ = "__main__":
    unittest.main()
