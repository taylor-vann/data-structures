"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from queue import Queue


class TestQueueMethods(unittest.TestCase):

    def test_queue_is_not_none(self):
        queue = Queue()
        self.assertIsNotNone(queue)


    def test_peek_is_none(self):
        queue = Queue()
        self.assertIsNone(queue.peek())


    def test_head_is_none(self):
        queue = Queue()
        self.assertIsNone(queue.peek())


    def test_head_is_not_none(self):
        queue = Queue()
        queue.enqueue(2)
        self.assertIsNotNone(queue.peek())


    def test_head_is_value(self):
        queue = Queue()
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 2)


    def test_enqueue_thrice(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 3)


    def test_dequeue_value_none(self):
        queue = Queue()
        queue.dequeue()
        self.assertIsNone(queue.peek())


    def test_enqueue_dequeue_value(self):
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        self.assertIsNone(queue.peek())


    def test_enqueue_twice_dequeue_once(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)


    def test_enqueue_thrice_dequeue_thrice(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)


    def test_enqueue_thrice_dequeue_twice(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        self.assertEqual(queue.dequeue(), 2)


    def test_enqueue_twice_dequeue_twice(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()
        self.assertIsNone(queue.dequeue())


    def test_queue_find_true(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertTrue(queue.find(3))


    def test_queue_find_false(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertFalse(queue.find(4))


    def test_queue_find_empty_false(self):
        queue = Queue()
        self.assertFalse(queue.find(4))


    def test_queue_contains_true(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertIn(3, queue)


    def test_queue_contains_false(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertNotIn(4, queue)


    def test_queue_contains_init_true(self):
        queue = Queue(1, 2, 3)
        self.assertIn(2, queue)


if __name__ == "__main__":
    unittest.main()
