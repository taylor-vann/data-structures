"""
Brian Vann
github.com/taylor-vann

Description:
- Unit Tests for the SLNode class.
"""

import unittest
from SLNode import SLNode

class TestSLLNodeMethods(unittest.TestCase):

    def testNotNone(self):
        node = SLNode()
        self.assertIsNotNone(node)


    def testNodeValueIsNone(self):
        node = SLNode()
        self.assertIsNone(node.data)


    def testNodeValueIsNotNone(self):
        node = SLNode("yo")
        self.assertIsNotNone(node.data)


    def testNextIsNone(self):
        node = SLNode()
        self.assertIsNone(node.nxt)


    def testNextIsNode(self):
        node1 = SLNode();
        node = SLNode("dude", node1)
        self.assertIsInstance(node.nxt, SLNode);


    def testNextValueEqual(self):
        node = SLNode()
        node1 = SLNode(2)
        node.nxt = node1
        self.assertEqual(node.nxt.data, 2)


unittest.main();
