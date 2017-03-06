'''
Brian Vann
github.com/taylor-vann

Unit Tests for the SLNode class
'''

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
        node = SLNode("yo", "dude")
        self.assertIsNotNone(node.get_data())

    def testNextIsNone(self):
        node = SLNode()
        self.assertIsNone(node.get_next())

    def testNextIsNode(self):
        nextNode = SLNode();
        node = SLNode(nextNode, "dude")
        self.assertIsNotNone(node.get_next(), SLNode);


unittest.main();
