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
        self.assertIsNone(node.get_data())


    def testNodeValueIsNotNone(self):
        node = SLNode("yo")
        self.assertIsNotNone(node.get_data())


    def testNextIsNone(self):
        node = SLNode()
        self.assertIsNone(node.get_next())


    def testNextIsNode(self):
        node1 = SLNode();
        node = SLNode("dude", node1)
        self.assertIsInstance(node.get_next(), SLNode);


    def testNextValueEqual(self):
        node = SLNode()
        node1 = SLNode(2)
        node.set_next(node1)
        bit = node.get_next()
        bit = bit.get_data()
        self.assertEqual(bit, 2)


unittest.main();
