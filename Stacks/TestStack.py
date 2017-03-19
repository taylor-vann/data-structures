"""
Brian Vann
github.com/taylor-vann

Description:
- Unit Tests for the Stack class

Requirements:
- unittest
- Stack.py
"""

import unittest
from Stack import Stack


class TestStackMethods(unittest.TestCase):

    def testStackNotNone(self):
        stack = Stack()
        self.assertIsNotNone(stack)


    def testPeekIsNone(self):
        stack = Stack()
        stack.push(None)
        self.assertIsNone(stack.peek())


    def testStackPeekIsNotNone(self):
        stack = Stack()
        stack.push(3)
        self.assertIsNotNone(stack.peek())


    def testStackPeekIsEqual(self):
        stack = Stack()
        stack.push(3)
        self.assertEqual(stack.peek(), 3)


    def testStackPushTwice(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)


    def testStackPushTwicePopOnce(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)


    def testStackPushThricePopTwice(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.peek(), 1)


    def testStackPushOncePopTwice(self):
        stack = Stack()
        stack.push(1)
        stack.pop()
        stack.pop()
        self.assertIsNone(stack.peek())


    def testStackContains(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.search(1))


    def testStackContainsEmpty(self):
        stack = Stack()
        self.assertFalse(stack.search(1))


    def testStackContainsTrue(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertIn(2, stack)


    def testStackContainsFalse(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertNotIn(4, stack)


    def testStackContainsInitTrue(self):
        stack = Stack(1, 2, 3)
        self.assertIn(2, stack)


unittest.main()
