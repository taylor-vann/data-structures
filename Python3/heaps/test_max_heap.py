"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from max_heap import MaxHeap


class TestMaxHeap(unittest.TestCase):

    def test_heap_is_not_none(self):
        hp = MaxHeap()
        self.assertIsNotNone(hp)


    def test_heap_has_one(self):
        hp = MaxHeap()

        hp.push(1, 1)

        self.assertIn(1, hp)


    def test_heap_insert_two_has_one(self):
        hp = MaxHeap()

        hp.push(0, 1)
        hp.push(1, 2)
        hp.push(2, 3)
        hp.push(3, 4)

        self.assertIn(4, hp)


    def test_heap_insert_two_pop_one(self):
        hp = MaxHeap()

        hp.push(0, 1)
        hp.push(1, 2)
        hp.push(2, 3)
        hp.push(3, 4)

        hp.pop()

        self.assertNotIn(4, hp)


    def test_heap_peek_one(self):
        hp = MaxHeap()
        hp.push(0, 1)

        self.assertEqual(hp.peek(), 1)


    def test_heap_five(self):
        hp = MaxHeap()

        hp.push(5, 4)
        hp.push(1, 8)
        hp.push(2, 19)
        hp.push(3, 7)
        hp.push(0, 2)

        self.assertEqual(hp.peek(), 4)


    def test_heap_seven(self):
        hp = MaxHeap()

        hp.push(5, 4)
        hp.push(1, 8)
        hp.push(2, 19)
        hp.push(3, 7)
        hp.push(0, 2)
        hp.push(10, 12)
        hp.push(8, 32)

        self.assertEqual(hp.peek(), 12)


    def test_heap_push_none_pop_none(self):
        hp = MaxHeap()

        hp.pop()

        self.assertEqual(hp.peek(), None)


    def test_heap_push_one_pop(self):
        hp = MaxHeap()

        hp.push(1, 1)
        hp.pop()

        self.assertEqual(hp.peek(), None)


    def test_heap_seven_pop_one_peek(self):
        hp = MaxHeap()

        hp.push(1, 4)
        hp.push(3, 8)
        hp.push(2, 19)
        hp.push(3, 7)
        hp.push(0, 2)
        hp.push(10, 12)
        hp.push(8, 32)

        hp.pop()

        self.assertEqual(hp.peek(), 32)


    def test_heap_seven_pop_one_not_contains(self):
        hp = MaxHeap()

        hp.push(1, 4)
        hp.push(3, 8)
        hp.push(2, 19)
        hp.push(3, 7)
        hp.push(0, 2)
        hp.push(10, 12)
        hp.push(8, 32)

        hp.pop()

        self.assertNotIn(12, hp)


    def test_heap_seven_pop_one_length_six(self):
        hp = MaxHeap()

        hp.push(1, 4)
        hp.push(3, 8)
        hp.push(2, 19)
        hp.push(3, 7)
        hp.push(0, 2)
        hp.push(10, 12)
        hp.push(8, 32)

        hp.pop()

        self.assertEqual(len(hp._que), 6)


    def test_heap_pop_in_order_still(self):
        hp = MaxHeap()

        hp.push(1, 3)
        hp.push(4, 6)
        hp.push(2, 4)
        hp.push(3, 5)
        hp.push(0, 2)
        hp.push(8, 7)

        popped = []

        for var in range(len(hp._que)):
            popped.append(hp.pop())

        self.assertEqual(popped, [7, 6, 5, 4, 3, 2])


if __name__ == "__main__":
    unittest.main()
