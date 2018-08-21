"""
Brian Vann
https://github.com/taylor-vann
"""

import unittest
from stack import Stack


class TestStackMethods(unittest.TestCase):

    def test_stack_not_none(self):
        stack = Stack()
        self.assertIsNotNone(stack)


    def test_peek_is_none(self):
        stack = Stack()
        stack.push(None)
        self.assertIsNone(stack.peek())


    def test_stack_peek_is_not_none(self):
        stack = Stack()
        stack.push(3)
        self.assertIsNotNone(stack.peek())


    def test_stack_peek_is_equal(self):
        stack = Stack()
        stack.push(3)
        self.assertEqual(stack.peek(), 3)


    def test_stack_push_twice(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)


    def test_stack_push_twice_pop_once(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)


    def test_stack_push_thrice_pop_twice(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.peek(), 1)


    def test_stack_push_once_pop_twice(self):
        stack = Stack()
        stack.push(1)
        stack.pop()
        stack.pop()
        self.assertIsNone(stack.peek())


    def test_stack_contains(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertIn(1, stack)


    def test_stack_contains_empty(self):
        stack = Stack()
        self.assertNotIn(1, stack)


    def test_stack_contains_true(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertIn(2, stack)


    def test_stack_contains_false(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertNotIn(4, stack)


    def test_stack_contains_init_true(self):
        stack = Stack(1, 2, 3)
        self.assertIn(2, stack)


if __name__ == "__main__":
    unittest.main()
