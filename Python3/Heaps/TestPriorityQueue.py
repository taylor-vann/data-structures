"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Unit tests for the heap structure class

Requirements:
- unittest
- PriorityQueue.py
"""

import unittest
from PriorityQueue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):


    def testPQIsNotNone(self):
        pq = PriorityQueue()
        self.assertIsNotNone(pq)


    def testPQHasOne(self):
        pq = PriorityQueue()
        pq.push(data = "a", weight = 4)
        self.assertIn("a", pq)


    def testPQInsertTwoHasOne(self):
        pq = PriorityQueue()
        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)

        self.assertIn("a", pq)


    def testPQInsertTwoPopOne(self):
        pq = PriorityQueue()
        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.pop()

        self.assertNotIn("a", pq)


    def testPQifyOne(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)

        self.assertEqual(pq.peek(), "a")


    def testPQifyFive(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 0)

        self.assertEqual(pq.peek(), "f")



    def testPQifySeven(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "g", weight = 12)
        pq.push(data = "h", weight = 5)

        self.assertEqual(pq.peek(), "e")


    def testPQifyPushNonePopNone(self):
        pq = PriorityQueue()
        pq.pop()
        self.assertEqual(pq.peek(), None)


    def testPQifyPushOnePop(self):
        pq = PriorityQueue()
        pq.push(data = "a", weight = 4)
        pq.pop()
        self.assertEqual(pq.peek(), None)



    def testPQifySevenPopOnePeek(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "g", weight = 12)
        pq.push(data = "h", weight = 5)

        pq.pop()

        self.assertEqual(pq.peek(), "a")


    def testPQifySevenRemoveALength(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "h", weight = 5)

        pq.remove("a")

        self.assertEqual(len(pq), 6)


    def testPQifySevenRemoveDNotThere(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "h", weight = 5)

        pq.remove("d")

        self.assertTrue("d" not in pq)


    def testPQifySevenRemoveDStillHasB(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "h", weight = 5)

        pq.remove("d")

        self.assertTrue("b" in pq)


    def testPQifySevenPopOneContains(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 10)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "g", weight = 12)
        pq.push(data = "h", weight = 5)

        pq.pop()

        self.assertNotIn(2, pq)


    def testPQifySevenPopOneLengthSix(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 9)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "h", weight = 5)

        pq.pop()

        self.assertEqual(len(pq._h), 6)


    def testPopInOrderStill(self):
        pq = PriorityQueue()

        pq.push(data = "a", weight = 4)
        pq.push(data = "b", weight = 9)
        pq.push(data = "c", weight = 8)
        pq.push(data = "d", weight = 7)
        pq.push(data = "e", weight = 2)
        pq.push(data = "f", weight = 6)
        pq.push(data = "h", weight = 5)

        popped = []

        for var in range(len(pq)):
            d = pq.pop()
            popped.append(d["data"])

        self.assertEqual(popped, ["e", "a", "h", "f", "d", "c", "b"])



unittest.main()
