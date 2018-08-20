"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def test_pq_is_not_none(self):
        pq = MinHeap()
        self.assertIsNotNone(pq)


    def test_pq_has_one(self):
        pq = MinHeap()

        pq.push(1, 1)

        self.assertIn(1, pq)


    def test_pq_insert_two_has_one(self):
        pq = MinHeap()

        pq.push(0, 1)
        pq.push(1, 2)
        pq.push(2, 3)
        pq.push(3, 4)

        self.assertIn(4, pq)


    def test_pq_insert_two_pop_one(self):
        pq = MinHeap()

        pq.push(0, 1)
        pq.push(1, 2)
        pq.push(2, 3)
        pq.push(3, 4)

        pq.pop()

        self.assertNotIn(1, pq)


    def test_pq_peek_one(self):
        pq = MinHeap()
        pq.push(0, 1)

        self.assertEqual(pq.peek(), 1)


    def test_pq_five(self):
        pq = MinHeap()

        pq.push(5, 4)
        pq.push(1, 8)
        pq.push(2, 19)
        pq.push(3, 7)
        pq.push(0, 2)

        self.assertEqual(pq.peek(), 2)


    def test_pq_seven(self):
        pq = MinHeap()

        pq.push(5, 4)
        pq.push(1, 8)
        pq.push(2, 19)
        pq.push(3, 7)
        pq.push(0, 2)
        pq.push(10, 12)
        pq.push(8, 32)

        self.assertEqual(pq.peek(), 2)


    def test_pq_push_none_pop_none(self):
        pq = MinHeap()

        pq.pop()

        self.assertEqual(pq.peek(), None)


    def test_pq_push_one_pop(self):
        pq = MinHeap()

        pq.push(1, 1)
        pq.pop()

        self.assertEqual(pq.peek(), None)


    def test_pq_seven_pop_one_peek(self):
        pq = MinHeap()

        pq.push(1, 4)
        pq.push(3, 8)
        pq.push(2, 19)
        pq.push(3, 7)
        pq.push(0, 2)
        pq.push(10, 12)
        pq.push(8, 32)

        pq.pop()

        self.assertEqual(pq.peek(), 4)


    def test_pq_seven_pop_one_not_contains(self):
        pq = MinHeap()

        pq.push(1, 4)
        pq.push(3, 8)
        pq.push(2, 19)
        pq.push(3, 7)
        pq.push(0, 2)
        pq.push(10, 12)
        pq.push(8, 32)

        pq.pop()

        self.assertNotIn(2, pq)


    def test_pq_seven_pop_one_length_six(self):
        pq = MinHeap()

        pq.push(1, 4)
        pq.push(3, 8)
        pq.push(2, 19)
        pq.push(3, 7)
        pq.push(0, 2)
        pq.push(10, 12)
        pq.push(8, 32)

        pq.pop()

        self.assertEqual(len(pq._q), 6)


    def test_pq_pop_in_order_still(self):
        pq = MinHeap()

        pq.push(1, 3)
        pq.push(4, 6)
        pq.push(2, 4)
        pq.push(3, 5)
        pq.push(0, 2)
        pq.push(8, 7)

        popped = []

        for var in range(len(pq._q)):
            popped.append(pq.pop())

        self.assertEqual(popped, [2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
