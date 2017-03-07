"""
Brian Taylor Vann
github.com/taylor-vann

Base class for the Queue data structure.

basic methods:
enqueue/insert
dequeue/delete
peek/access
search
"""

from SLNode import SLNode

class Queue(object):
    _head = None
    _tail = None

    #overwritten methods
    def __init__(self, nxt = None):
        self.enqueue(nxt)
        pass

    def __contains__(self, bit):
        return self.search(bit)

    #custom methods
    def enqueue(self, nxt):
        if isinstance(nxt, SLNode):
            #if empty
            if self._tail is None and self._head is None:
                self._tail = nxt
                self._head = nxt

                return

            self._head.set_next(nxt)
            self._head = nxt

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
