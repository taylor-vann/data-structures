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

    def __init__(self, *args):
        for var in args:
            self.insert(var)


    def __contains__(self, bit):
        return self.search(bit)


    def insert(self, data):
        if not self._head:
            self._head = SLNode(data)
            return

        index = self._head

        while index.nxt:
            index = index.nxt

        index.nxt = SLNode(data)


    def insert_after(self, data, bit):
        if self._head is None:
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
            
        prev, curr = self._head, self._head.nxt

        while curr:
            if curr.data == data:
                break 

            prev, curr = curr, prev.nxt

        if not curr:
            return

        if self._head == prev:
            self._head = curr
            prev.nxt = None

            return prev.data;

        prev.nxt = curr.nxt
        curr.nxt = None

        return curr.data


    def peek(self):
        if self._head is None:
            return None

        return self._head.data


    def search(self, bit):
        index = self._head

        while index is not None:
            if index.data == bit:
                return True

            index = index.nxt

        return False
