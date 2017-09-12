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
        self.assertIsNone(dlnode.get_data())


    def testNodeValueInitEqual(self):
        dlnode = DLNode(3)
        self.assertEqual(dlnode.get_data(), 3)


    def testNodeNextIsNone(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.get_next())


    def testNodeNextIsNotNone(self):
        dlnode = DLNode()
        dlnode1 = DLNode()
        dlnode.set_next(dlnode1)
        self.assertIsNotNone(dlnode.get_next())


    def testNextIsNode(self):
        dlnode1 = DLNode();
        dlnode = DLNode("dude", None, dlnode1)
        self.assertIsInstance(dlnode.get_next(), DLNode);


    def testNodeNextValueEqual(self):
        dlnode = DLNode()
        dlnode1 = DLNode(3)
        dlnode.set_next(dlnode1)
        bit = dlnode.get_next()
        bit = bit.get_data()
        self.assertEqual(bit, 3)


    def testNodePrevIsNone(self):
        dlnode = DLNode()
        self.assertIsNone(dlnode.get_next())


    def testNodePrevIsNotNone(self):
        dlnode = DLNode()
        dlnode1 = DLNode()
        dlnode.set_prev(dlnode1)
        self.assertIsNotNone(dlnode.get_prev())


    def testPrevIsNode(self):
        dlnode1 = DLNode();
        dlnode = DLNode("dude", dlnode1, None)
        self.assertIsInstance(dlnode.get_prev(), DLNode);


    def testNodePrevValueEqual(self):
        dlnode = DLNode()
        dlnode1 = DLNode(2)
        dlnode.set_prev(dlnode1)
        bit = dlnode.get_prev()
        bit = bit.get_data()
        self.assertEqual(bit, 2)


unittest.main()
