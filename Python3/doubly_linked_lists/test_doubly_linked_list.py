"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from doubly_linked_list import DLList


class TestDLListMethods(unittest.TestCase):

    def test_dllist_is_none(self):
        dlist = None
        self.assertIsNone(dlist)


    def test_dllist_is_not_none(self):
        dlist = DLList()
        self.assertIsNotNone(dlist)


    def test_dllist_is_instance(self):
        dlist = DLList()
        self.assertIsInstance(dlist, DLList)


    def test_dllist_peek_is_none(self):
        dlist = DLList()
        self.assertIsNone(dlist.peek())


    def test_dllist_peek_is_not_none(self):
        dlist = DLList()
        dlist.unshift(1)
        self.assertIsNotNone(dlist.peek())


    def test_dllist_peek_is_equal(self):
        dlist = DLList()
        dlist.unshift(2)
        self.assertEqual(dlist.peek(), 2)


    def test_dllist_push_two_pop_three_is_none(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.pop()
        dlist.pop()
        dlist.pop()
        self.assertIsNone(dlist.peek())


    def test_dllist_push_three_peek_correct(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.unshift(3)
        self.assertEqual(dlist.peek(), 3)


    def test_dellist_push_three_pop_one_correct(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.unshift(3)
        dlist.pop()
        self.assertEqual(dlist.peek(), 3)


    def test_dllist_unshift_equal(self):
        dlist = DLList()
        dlist.unshift(1)
        self.assertEqual(dlist.peek(), 1)


    def test_dllist_unshift_three_equal(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.unshift(3)
        self.assertEqual(dlist.peek_last(), 1)


    def test_dllist_unshift_two_pop_one(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.pop()
        self.assertEqual(dlist.peek(), 2)


    def test_dllist_unshift_two_pop_two(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.pop()
        dlist.pop()
        self.assertEqual(dlist.peek(), None)


    def test_dllist_shift_empty_is_none(self):
        dlist = DLList()
        dlist.shift()
        self.assertIsNone(dlist.peek_last())


    def test_dllist_unshift_two_shift_correct(self):
        dlist = DLList()
        dlist.unshift(1)
        dlist.unshift(2)
        dlist.shift()
        self.assertEqual(dlist.peek_last(), 1)


    def test_dllist_unshift_four_shift_two_pop_one_correct(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.unshift(3)
        dlist.unshift(4)
        dlist.shift()
        dlist.shift()
        dlist.pop()
        self.assertEqual(dlist.peek_last(), 1)


    def test_dllist_search_is_none(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.unshift(3)
        dlist.unshift(4)
        self.assertNotIn(5, dlist)


    def test_dllist_search_is_not_none(self):
        dlist = DLList()
        dlist.unshift(2)
        dlist.unshift(1)
        dlist.unshift(3)
        dlist.unshift(4)
        self.assertIn(1, dlist)


    def test_dllist_get_node_is_none(self):
        dlist = DLList(1, 2, 3, 4)
        self.assertIsNone(dlist.find(5))


    def test_dllist_get_node_equals(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.find(4)
        self.assertEqual(bit.data, 4)


    def test_dllist_pop_node_is_none(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.remove(5)
        self.assertIsNone(bit)


    def test_dllist_pop_node_is_equal(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.pop()
        self.assertEqual(bit, 4)


    def test_dllist_removed_value_is_gone(self):
        dlist = DLList(1, 2, 3, 4)
        bit = dlist.remove(3)
        self.assertIsNone(dlist.find(3))


    def test_dllist_remove_value_from_none(self):
        dlist = DLList()
        bit = dlist.remove(3)
        self.assertNotIn(3, dlist)


    def test_dllist_remove_four_without_side_effects(self):
        dlist = DLList(1, 3, 4)
        bit = dlist.remove(4)
        self.assertIn(3, dlist)


    def test_DLList_unshift_remove_all_fours(self):
        dlist = DLList(1, 3, 4)
        bit = dlist.remove(4)
        self.assertNotIn(4, dlist)


if __name__ == "__main__":
    unittest.main()
