'''
Brian Taylor Vann
github.com/taylor-vann

Base class for a Singly Linked List.

Basic methods:
access
search
insert
insert after
remove
delete after
'''

from SLNode import SLNode

class SLList(object):
    _head = None

    #overridden methods
    def __init__(self, nxt = None):
        self.insert(nxt)

    def __contains__(self, bit):
        return self.search(bit)

    #custom methods
    def peek(self):
        if self._head is None:
            return None

        return self._head.get_data()

    def search(self, bit):
        index = self._head

        while index is not None:
            if index.get_data() == bit:
                return True

            index = index.get_next()

        return False

    def insert(self, nxt):
        if isinstance(nxt, SLNode):
            if self._head is None:
                self._head = nxt
                return

            index = self._head

            while index.get_next() is not None:
                index = index.get_next()

            index.set_next(nxt)

    def insert_after(self, nxt, bit):
        if isinstance(nxt, SLNode):
            if self._head is None:
                self._head = nxt
                return

            prev = self._head
            curr = self._head.get_next()

            while prev.get_data() != bit:
                if curr is None:
                    break

                prev = curr
                curr = prev.get_next()

            prev.set_next(nxt)
            nxt.set_next(curr)

    def remove(self):
        if self._head is None:
            return None

        bit = self._head.get_data()
        self._head = self._head.get_next()

        return bit
