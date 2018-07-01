"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from doubly_linked_list import DLNode


class TestDLNodeMethods(unittest.TestCase):

    def test_node_not_none(self):
        dlnode = DLNode()
        self.assertIsNotNone(dlnode)


    def test_node_value_none(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.data)


    def test_node_value_init(self):
        dlnode = DLNode(3)
        self.assertEqual(dlnode.data, 3)


    def test_node_next_is_none(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.nxt)


    def test_node_next_is_not_none(self):
        dlnode = DLNode()
        dlnode.nxt = DLNode()
        self.assertIsNotNone(dlnode.nxt)


    def test_next_is_correct_node(self):
        dlnode1 = DLNode()
        dlnode = DLNode("dude", None, dlnode1)
        self.assertIsInstance(dlnode.nxt, DLNode)


    def test_node_next_value_equal(self):
        dlnode = DLNode()
        dlnode.nxt = DLNode(3)
        self.assertEqual(dlnode.nxt.data, 3)


    def test_node_prev_is_none(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.nxt)


    def test_node_prev_is_not_none(self):
        dlnode = DLNode()
        dlnode1 = DLNode()
        dlnode.prev = dlnode1
        self.assertIsNotNone(dlnode.prev)


    def test_prev_is_node(self):
        dlnode1 = DLNode();
        dlnode = DLNode("dude", dlnode1, None)
        self.assertIsInstance(dlnode.prev, DLNode);


    def test_node_prev_value_equal(self):
        dlnode = DLNode()
        dlnode1 = DLNode(2)
        dlnode.prev = dlnode1
        bit = dlnode.prev
        bit = bit.data
        self.assertEqual(bit, 2)


if __name__ == "__main__":
    unittest.main()
