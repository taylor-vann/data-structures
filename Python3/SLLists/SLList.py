"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Base class for a Singly Linked List data structure.
"""

from SLNode import SLNode


class SLList(object):

    _head = None

    def __init__(self, *args):
        for var in args:
            self.insert(var)


    def __contains__(self, bit):
        node = self._head

        while node:
            if node.data == bit:
                return True

            node = node.nxt

        return False


    def insert(self, data):
        if not self._head:
            self._head = SLNode(data)
            return

        node = self._head

        while node.nxt:
            node = node.nxt

        node.nxt = SLNode(data)


    def insert_after(self, data, bit):
        if not self._head:
            self._head = SLNode(data)
            return

        prev, curr = self._head, self._head.nxt

        while prev.data != bit:
            if not curr:
                break

            prev, curr = curr, prev.nxt

        prev.nxt = SLNode(data)
        prev.nxt.nxt = curr


    def remove(self):
        if not self._head:
            return

        bit = self._head.data
        self._head = self._head.nxt

        return bit


    def remove_data(self, data):
        if not self._head:
            return
        if self._head.data == data:
            self._head = self._head.nxt
            return data
            
        prev, curr = self._head, self._head.nxt

        while curr:
            if curr.data == data:
                prev.nxt = curr.nxt
                curr.nxt = None
                return data

            prev = curr
            curr = prev.nxt


    def peek(self):
        if self._head:
            return self._head.data
