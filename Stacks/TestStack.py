"""
Brian Vann
github.com/taylor-vann

Unit Tests for the Stack class
"""

import unittest
from Stack import Stack
from SLNode import SLNode

class TestStackMethods(unittest.TestCase):

    def testStackNotNone(self):
        stack = Stack()
        self.assertIsNotNone(stack)

    def testPeekIsNone(self):
        stack = Stack()
        node = SLNode(None, None)
        stack.push(node)
        self.assertIsNone(stack.peek())

    def testStackPeekIsNotNone(self):
        stack = Stack()
        node = SLNode(None, 3)
        stack.push(node)
        self.assertIsNotNone(stack.peek())

    def testStackPeekIsEqual(self):
        stack = Stack()
        node = SLNode(None, 3)
        stack.push(node)
        self.assertEqual(stack.peek(), 3)

    def testStackPushTwice(self):
        stack = Stack()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        stack.push(node1)
        stack.push(node2)
        self.assertEqual(stack.peek(), 2)

    def testStackPushTwicePopOnce(self):
        stack = Stack()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        stack.push(node1)
        stack.push(node2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)

    def testStackPushThricePopTwice(self):
        stack = Stack()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        stack.push(node1)
        stack.push(node2)
        stack.push(node3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.peek(), 1)

    def testStackPushOncePopTwice(self):
        stack = Stack()
        node1 = SLNode(None, 1)
        stack.push(node1)
        stack.pop()
        stack.pop()
        self.assertIsNone(stack.peek())

    def testStackContains(self):
        stack = Stack()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        stack.push(node1)
        stack.push(node2)
        stack.push(node3)
        self.assertTrue(stack.search(1))

    def testStackContainsEmpty(self):
        stack = Stack()
        self.assertFalse(stack.search(1))

    def testStackContainsTrue(self):
        stack = Stack()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        stack.push(node1)
        stack.push(node2)
        stack.push(node3)
        self.assertIn(2, stack)

    def testStackContainsFalse(self):
        stack = Stack()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        stack.push(node1)
        stack.push(node2)
        stack.push(node3)
        self.assertNotIn(4, stack)


unittest.main()
