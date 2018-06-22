"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the DLNode class 

Requirements:
- unittest
- DLNode.py
"""

import unittest
from DLNode import DLNode

class TestDLNodeMethods(unittest.TestCase):

    def testNodeNotNone(self):
        dlnode = DLNode()
        self.assertIsNotNone(dlnode)


    def testNodeValueNone(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.data)


    def testNodeValueInitEqual(self):
        dlnode = DLNode(3)
        self.assertEqual(dlnode.data, 3)


    def testNodeNextIsNone(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.nxt)


    def testNodeNextIsNotNone(self):
        dlnode = DLNode()
        dlnode.nxt = DLNode()
        self.assertIsNotNone(dlnode.nxt)


    def testNextIsNode(self):
        dlnode1 = DLNode()
        dlnode = DLNode("dude", None, dlnode1)
        self.assertIsInstance(dlnode.nxt, DLNode)


    def testNodeNextValueEqual(self):
        dlnode = DLNode()
        dlnode.nxt = DLNode(3)
        self.assertEqual(dlnode.nxt.data, 3)


    def testNodePrevIsNone(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.nxt)


    def testNodePrevIsNotNone(self):
        dlnode = DLNode()
        dlnode1 = DLNode()
        dlnode.prev = dlnode1
        self.assertIsNotNone(dlnode.prev)


    def testPrevIsNode(self):
        dlnode1 = DLNode();
        dlnode = DLNode("dude", dlnode1, None)
        self.assertIsInstance(dlnode.prev, DLNode);


    def testNodePrevValueEqual(self):
        dlnode = DLNode()
        dlnode1 = DLNode(2)
        dlnode.prev = dlnode1
        bit = dlnode.prev
        bit = bit.data
        self.assertEqual(bit, 2)


unittest.main()
