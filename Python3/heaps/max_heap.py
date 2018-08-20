"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

from priority_queue import PriorityQueue

class MaxHeap(PriorityQueue):
    def __init__(self):
        super().__init__(lambda x, y: x < y)
