"""
Brian Vann
https://github.com/taylor-vann
"""

import unittest
from singly_linked_list import SLNode


class TestSLLNodeMethods(unittest.TestCase):

    def test_not_node(self):
        node = SLNode()
        self.assertIsNotNone(node)


    def test_node_value_is_none(self):
        node = SLNode()
        self.assertIsNone(node.value)


    def test_node_value_is_not_none(self):
        node = SLNode("yo")
        self.assertIsNotNone(node.value)


    def test_next_is_none(self):
        node = SLNode()
        self.assertIsNone(node.nxt)


    def test_next_is_node(self):
        node1 = SLNode();
        node = SLNode("dude", node1)
        self.assertIsInstance(node.nxt, SLNode);


    def test_next_value_equal(self):
        node = SLNode()
        node1 = SLNode(2)
        node.nxt = node1
        self.assertEqual(node.nxt.value, 2)


if __name__ == "__main__":
    unittest.main()
