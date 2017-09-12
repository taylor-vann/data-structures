"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the heap structure class

Requirements:
- unittest
- MaxHeap.py
"""

import unittest
from MinHeap import MinHeap


class TestHeapMethods(unittest.TestCase):


    def testHeapIsNotNone(self):
        hp = MinHeap()
        self.assertIsNotNone(hp)


    def testHeapHasOne(self):
        hp = MinHeap(1)
        self.assertIn(1, hp)


    def testHeapInsertTwoHasOne(self):
        hp = MinHeap(1, 2, 3)
        hp.push(4)
        self.assertIn(4, hp)


    def testHeapInsertTwoPopOne(self):
        hp = MinHeap(1, 2, 3)
        hp.pop()
        self.assertNotIn(1, hp)


    def testHeapifyOne(self):
        hp = MinHeap(1)
        self.assertEqual(hp.peek(), 1)


    def testHeapifyFive(self):
        hp = MinHeap(4, 8, 19, 2, 7)
        self.assertEqual(hp.peek(), 2)


    def testHeapifySeven(self):
        hp = MinHeap(4, 8, 19, 2, 7, 12, 32)
        self.assertEqual(hp.peek(), 2)


    def testHeapifyPushNonePopNone(self):
        hp = MinHeap()
        hp.pop()
        self.assertEqual(hp.peek(), None)


    def testHeapifyPushOnePop(self):
        hp = MinHeap(1)
        hp.pop()
        self.assertEqual(hp.peek(), None)


    def testHeapifySevenPopZero(self):
        hp = MinHeap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertEqual(hp.peek(), 4)


    def testHeapifySevenPopOnePeek(self):
        hp = MinHeap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertEqual(hp.peek(), 4)


    def testHeapifySevenPopOneContains(self):
        hp = MinHeap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertNotIn(2, hp)


    def testHeapifySevenPopOneLengthSix(self):
        hp = MinHeap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertEqual(len(hp._h), 6)


    def testPopInOrderStill(self):
        hp = MinHeap(4, 7, 1, 2, 3, 5, 6)
        hp.pop()

        popped = []

        for var in range(len(hp)):
            popped.append(hp.pop())

        self.assertEqual(popped, [2, 3, 4, 5, 6, 7])


    def testRemoveInOrderStill(self):
        hp = MinHeap(4, 8, 19, 2, 7, 12, 32)
        hp.remove(7)

        popped = []

        for var in range(len(hp)):
            popped.append(hp.pop())

        self.assertEqual(popped, [2, 4, 8, 12, 19, 32])


unittest.main()
