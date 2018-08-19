"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):


    def test_pq_is_not_none(self):
        pq = PriorityQueue()
        self.assertIsNotNone(pq)


    def test_pq_has_one(self):
        pq = PriorityQueue()
        pq.push(4, "a")
        self.assertIn("a", pq)


    def test_pq_insert_two_has_one(self):
        pq = PriorityQueue()
        pq.push(4, "a")
        pq.push(10, "b")

        self.assertIn("a", pq)


    def test_pq_insert_two_pop_one(self):
        pq = PriorityQueue()
        pq.push(4, "a")
        pq.push(10, "b")
        pq.pop()

        self.assertNotIn("a", pq)


    def test_pq_heapify_one(self):
        pq = PriorityQueue()

        pq.push(4, "a")
        pq.push(10, "b")

        self.assertEqual(pq.peek(), "a")


    def test_pq_heapify_five(self):
        pq = PriorityQueue()

        pq.push(4, "a")
        pq.push(10, "b")
        pq.push(8, "c")
        pq.push(7, "d")
        pq.push(2, "e")
        pq.push(0, "f")

        self.assertEqual(pq.peek(), "f")



    def test_pq_heapify_seven(self):
        pq = PriorityQueue()

        pq.push(4, "a")
        pq.push(10, "b")
        pq.push(8, "c")
        pq.push(7, "d")
        pq.push(2, "e")
        pq.push(6, "f")
        pq.push(12, "g")
        pq.push(5, "h")

        self.assertEqual(pq.peek(), "e")


    def test_pq_push_none_pop_none(self):
        pq = PriorityQueue()

        pq.pop()

        self.assertEqual(pq.peek(), None)


    def test_pq_push_one_pop(self):
        pq = PriorityQueue()

        pq.push(4, "d")
        pq.pop()

        self.assertEqual(pq.peek(), None)



    def test_pq_seven_pop_one_peek(self):
        pq = PriorityQueue()

        pq.push(4, "a")
        pq.push(10, "b")
        pq.push(8, "c")
        pq.push(7, "d")
        pq.push(2, "e")
        pq.push(6, "f")
        pq.push(12, "g")
        pq.push(5, "h")

        pq.pop()

        self.assertEqual(pq.peek(), "a")


    def test_pq_seven_pop_one_contains(self):
        pq = PriorityQueue()

        pq.push(4, "a")
        pq.push(10, "b")
        pq.push(8, "c")
        pq.push(7, "d")
        pq.push(2, "e")
        pq.push(6, "f")
        pq.push(12, "g")
        pq.push(5, "h")

        pq.pop()

        self.assertNotIn("e", pq)


    def test_pq_seven_pop_one_length_six(self):
        pq = PriorityQueue()

        pq.push(4, "a")
        pq.push(10, "b")
        pq.push(8, "c")
        pq.push(7, "d")
        pq.push(2, "e")
        pq.push(6, "f")
        pq.push(12, "g")

        pq.pop()

        self.assertEqual(len(pq._q), 6)


    def test_pq_in_order_still(self):
        pq = PriorityQueue()

        pq.push(4, "a")
        pq.push(10, "b")
        pq.push(8, "c")
        pq.push(7, "d")
        pq.push(2, "e")
        pq.push(6, "f")
        pq.push(5, "h")

        popped = []

        for _ in range(len(pq)):
            popped.append(pq.pop())

        self.assertEqual(popped, ["e", "a", "h", "f", "d", "c", "b"])



unittest.main()
