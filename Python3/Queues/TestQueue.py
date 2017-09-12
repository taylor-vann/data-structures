"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit Tests for the Queue class.

Requirements:
- unittest
- Queue.py
"""

import unittest
from Queue import Queue


class TestQueueMethods(unittest.TestCase):

    def testQueueIsNotNone(self):
        queue = Queue()
        self.assertIsNotNone(queue)


    def testPeekIsNone(self):
        queue = Queue()
        self.assertIsNone(queue.peek())


    def testHeadIsNone(self):
        queue = Queue()
        self.assertIsNone(queue.peek())


    def testHeadIsNotNone(self):
        queue = Queue()
        queue.enqueue(2)
        self.assertIsNotNone(queue.peek())


    def testHeadIsValue(self):
        queue = Queue()
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 2)


    def testEnqueueThriceValue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 3)


    def testDequeueValueNone(self):
        queue = Queue()
        queue.dequeue()
        self.assertIsNone(queue.peek())


    def testEnqueueDequeueValueNone(self):
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        self.assertIsNone(queue.peek())


    def testEnTwiceDeqOnceValueNone(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)


    def testEnThriceDeqTwiceValueNone(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)


    def testEnThriceDeqTwiceValueNone(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        self.assertEqual(queue.dequeue(), 2)


    def testEnTwiceDeqTwiceValueNone(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()
        self.assertIsNone(queue.dequeue())


    def testQueueSearchTrue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertTrue(queue.search(3))


    def testQueueSearchFalse(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertFalse(queue.search(4))


    def testQueueSearchEmptyFalse(self):
        queue = Queue()
        self.assertFalse(queue.search(4))


    def testQueueContainsTrue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertIn(3, queue)


    def testQueueContainsFalse(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertNotIn(4, queue)


    def testQueueContainsInitTrue(self):
        queue = Queue(1, 2, 3)
        self.assertIn(2, queue)


unittest.main()
