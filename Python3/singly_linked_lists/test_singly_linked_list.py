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
        slist.append("dude")
        self.assertIsNotNone(slist.peek())


    def test_sllist_append_three_peek(self):
        slist = SLList()
        slist.append(1)
        slist.append(2)
        slist.append(3)
        self.assertEqual(slist.peek(), 3)


    def test_sllist_empty_pop_none(self):
        slist = SLList()
        slist.pop();
        self.assertIsNone(slist.peek())


    def test_sllist_append_once_pop_twice(self):
        slist = SLList()
        slist.append(1)
        slist.append(2)
        slist.pop()
        self.assertEqual(slist.peek(), 1)


    def test_sllist_pop_correct_data(self):
        slist = SLList()
        slist.append(1)
        slist.append(2)
        self.assertEqual(slist.pop(), 2)


    def test_contains_false(self):
        slist = SLList()
        slist.append(1)
        slist.append(2)
        slist.append(3)
        self.assertNotIn(4, slist)


    def test_contains_true(self):
        slist = SLList()
        slist.append(1)
        slist.append(2)
        slist.append(3)
        self.assertIn(1, slist)


    def test_contains_init_true(self):
        slist = SLList(1, 2, 3)
        self.assertIn(1, slist)


    def test_remove_value_start(self):
        slist = SLList(1, 2, 3)
        slist.remove(1)
        self.assertNotIn(1, slist)


    def test_remove_value_start_contains_two(self):
        slist = SLList(1, 2, 3)
        slist.remove(1)
        self.assertIn(2, slist)


    def test_remove_value_start_contains_three(self):
        slist = SLList(1, 2, 3)
        slist.remove(1)
        self.assertIn(3, slist)


    def test_remove_value_middle(self):
        slist = SLList(1, 2, 3)
        slist.remove(2)
        self.assertNotIn(2, slist)


    def test_remove_value_end(self):
        slist = SLList(1, 2, 3)
        slist.remove(3)
        self.assertNotIn(3, slist)


    def test_remove_all_values(self):
        slist = SLList(1, 3, 3, 2, 3, 3)
        slist.remove(3)
        self.assertNotIn(3, slist)


if __name__ == "__main__":
    unittest.main()
