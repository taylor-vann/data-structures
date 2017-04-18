"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the heap structure class

Requirements:
- unittest
- Heap.py
"""

import unittest
from Heap import Heap


class TestHeapMethods(unittest.TestCase):


    def testHeapIsNotNone(self):
        hp = Heap()
        self.assertIsNotNone(hp)


    def testHeapHasOne(self):
        hp = Heap(1)
        self.assertIn(1, hp)


    def testHeapInsertTwoHasOne(self):
        hp = Heap(1, 2, 3)
        hp.push(4)
        self.assertIn(4, hp)


    def testHeapInsertTwoPopOne(self):
        hp = Heap(1, 2, 3)
        hp.pop()
        self.assertNotIn(3, hp)


    def testHeapifyOne(self):
        hp = Heap(1)
        self.assertEqual(hp.peek(), 1)


    def testHeapifyFive(self):
        hp = Heap(4, 8, 19, 2, 7)
        self.assertEqual(hp.peek(), 19)


    def testHeapifySeven(self):
        hp = Heap(4, 8, 19, 2, 7, 12, 32)
        self.assertEqual(hp.peek(), 32)


    def testHeapifyPushNonePopNone(self):
        hp = Heap()
        hp.pop()
        self.assertEqual(hp.peek(), None)


    def testHeapifyPushOnePop(self):
        hp = Heap(1)
        hp.pop()
        self.assertEqual(hp.peek(), None)


    def testHeapifySevenPopZero(self):
        hp = Heap(4, 8, 19, 2, 7, 12, 32)
        hp.pop()
        self.assertEqual(hp.peek(), 19)


    def testHeapifySevenPopOnePeek(self):
        hp = Heap(4, 8, 19, 2, 7, 12, 32)
        hp.pop(1)
        self.assertEqual(hp.peek(), 32)


    def testHeapifySevenPopOneContains(self):
        hp = Heap(4, 8, 19, 2, 7, 12, 32)
        hp.pop(1)
        self.assertNotIn(19, hp)


    def testHeapifySevenPopOneLengthSix(self):
        hp = Heap(4, 8, 19, 2, 7, 12, 32)
        hp.pop(1)
        self.assertEqual(len(hp._h), 6)


    def testPopInOrderStill(self):
        hp = Heap(4, 7, 1, 2, 3, 5, 6)
        hp.pop(5)

        popped = []

        for var in range(len(hp)):
            popped.append(hp.pop())

        self.assertEqual(popped, [7, 6, 5, 4, 3, 2])


    def testRemoveInOrderStill(self):
        hp = Heap(4, 8, 19, 2, 7, 12, 32)
        hp.remove(7)

        popped = []

        for var in range(len(hp)):
            popped.append(hp.pop())

        self.assertEqual(popped, [32, 19, 12, 8, 4, 2])


unittest.main()
