"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Base class for a Singly Linked List data structure.

Required:
-SLNode.py

Basic methods:
- access
- search
- insert
- insert after
- remove
- remove after
"""

from SLNode import SLNode


class SLList(object):

    _head = None

    #overridden methods
    def __init__(self, *args):
        for var in args:
            self.insert(var)


    def __contains__(self, bit):
        return self.search(bit)


    #custom methods
    def insert(self, num):
        node = SLNode(num)

        if self._head is None:
            self._head = node
            return

        index = self._head

        while index.get_next() is not None:
            index = index.get_next()

        index.set_next(node)


    def insert_after(self, num, bit):
        node = SLNode(num)

        if self._head is None:
            self._head = node
            return

        prev = self._head
        curr = self._head.get_next()

        while prev.get_data() != bit:
            if curr is None:
                break

            prev = curr
            curr = prev.get_next()

        prev.set_next(node)
        node.set_next(curr)


    def remove(self):
        if self._head is None:
            return None

        bit = self._head.get_data()
        self._head = self._head.get_next()

        return bit


    def remove_data(self, num):
        if self._head is None:
            return None
            
        prev = self._head
        curr = prev.get_next()

        if prev.get_data() == num:
            self._head = curr
            prev.set_next(None)

            return prev.get_data();

        while curr is not None:
            if curr.get_data() == num:
                break 

            prev = curr
            curr = prev.get_next()

        if curr is None:
            return None

        prev.set_next(curr.get_next())
        bit = curr.get_data()
        curr.set_next(None)

        return bit


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
