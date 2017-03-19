"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Base class for a Queue data structure.

Requirements:
- SLNode.py

Basic methods:
- enqueue
- dequeue
- peek
- search
"""

from SLNode import SLNode


class Queue(object):

    _head = None
    _tail = None

    #overwritten methods
    def __init__(self, *args):
        for var in args:
            self.enqueue(var)


    def __contains__(self, bit):
        return self.search(bit)


    #custom methods
    def enqueue(self, num):
        node = SLNode(num)

        if self._tail is None and self._head is None:
            self._tail = node
            self._head = node

            return

        self._head.set_next(node)
        self._head = node


    def dequeue(self):
        if self._tail is None:
            return None

        bit = self._tail.get_data()

        if self._tail == self._head:
            self._head = None

        self._tail = self._tail.get_next()

        return bit


    def peek(self):
        if self._head is None:
            return None

        return self._head.get_data()


    def search(self, bit):
        if self._head is None:
            return False

        index = self._tail

        while index is not None:
            if index.get_data() == bit:
                return True

            index = index.get_next()

        return False
