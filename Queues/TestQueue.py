"""
Brian Taylor Vann
github.com/taylor-vann


Unit Tests for the Queue class.
"""

import unittest
from SLNode import SLNode
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
        node = SLNode(None, 2)
        queue.enqueue(node)
        self.assertIsNotNone(queue.peek())

    def testHeadIsValue(self):
        queue = Queue()
        node = SLNode(None, 2)
        queue.enqueue(node)
        self.assertEqual(queue.peek(), 2)

    def testEnqueueThriceValue(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertEqual(queue.peek(), 3)

    def testDequeueValueNone(self):
        queue = Queue()
        queue.dequeue()
        self.assertIsNone(queue.peek())

    def testEnqueueDequeueValueNone(self):
        queue = Queue()
        node = SLNode(None, 1)
        queue.enqueue(node)
        queue.dequeue()
        self.assertIsNone(queue.peek())

    def testEnTwiceDeqOnceValueNone(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        queue.enqueue(node1)
        queue.enqueue(node2)
        self.assertEqual(queue.dequeue(), 1)

    def testEnThriceDeqTwiceValueNone(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertEqual(queue.dequeue(), 1)

    def testEnThriceDeqTwiceValueNone(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        queue.dequeue()
        self.assertEqual(queue.dequeue(), 2)

    def testEnTwiceDeqTwiceValueNone(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.dequeue()
        queue.dequeue()
        self.assertIsNone(queue.dequeue())

    def testQueueSearchTrue(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertTrue(queue.search(3))

    def testQueueSearchFalse(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertFalse(queue.search(4))

    def testQueueSearchEmptyFalse(self):
        queue = Queue()
        self.assertFalse(queue.search(4))

    def testQueueContainsTrue(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertIn(3, queue)

    def testQueueContainsFalse(self):
        queue = Queue()
        node1 = SLNode(None, 1)
        node2 = SLNode(None, 2)
        node3 = SLNode(None, 3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertNotIn(4, queue)


unittest.main()
