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
from MaxHeap import MaxHeap


class TestHeapMethods(unittest.TestCase):


    def testHeapIsNotNone(self):
        hp = MaxHeap()
        self.assertIsNotNone(hp)


    def testHeapHasOne(self):
        hp = MaxHeap(1)
        self.assertIn(1, hp)


    def testHeapInsertTwoHasOne(self):
        hp = MaxHeap(1, 2, 3)
        hp.push(4)
        self.assertIn(4, hp)


    def testHeapInsertTwoPopOne(self):
        hp = MaxHeap(1, 2, 3)
        hp.pop()
        self.assertNotIn(3, hp)


    def testHeapifyOne(self):
        hp = MaxHeap(1)
        self.assertEqual(hp.peek(), 1)


    def testHeapifyFive(self):
        hp = MaxHeap(4, 8, 19, 2, 7)
        self.assertEqual(hp.peek(), 19)


    def testHeapifySeven(self):
        hp = MaxHeap(4, 8, 19, 2, 7, 12, 32)
        self.assertEqual(hp.peek(), 32)


    def testHeapifyPushNonePopNone(self):
        hp = MaxHeap()
        hp.pop()
        self.assertEqual(hp.peek(), None)


    def testHeapifyPushOnePop(self):
        hp = MaxHeap(1)
        hp.pop()
        self.assertEqual(hp.peek(), None)


    def testHeapifySevenPopZero(self):
        hp = MaxHeap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertEqual(hp.peek(), 19)


    def testHeapifySevenPopOnePeek(self):
        hp = MaxHeap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertEqual(hp.peek(), 19)


    def testHeapifySevenPopOneLengthSix(self):
        hp = MaxHeap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertEqual(len(hp._h), 6)


    def testPopInOrderStill(self):
        hp = MaxHeap(4, 7, 1, 2, 3, 5, 6)
        hp.pop()

        popped = []

        for var in range(len(hp)):
            popped.append(hp.pop())

        self.assertEqual(popped, [6, 5, 4, 3, 2, 1])


    def testRemoveInOrderStill(self):
        hp = MaxHeap(4, 8, 19, 2, 7, 12, 32)
        hp.remove(7)

        popped = []

        for var in range(len(hp)):
            popped.append(hp.pop())

        self.assertEqual(popped, [32, 19, 12, 8, 7, 4])


unittest.main()
