"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Base class for a Stack data structure

Required:
- SLNode.py

Basic methods:
- push
- pop
- peek/access
- search
"""

from SLNode import SLNode


class Stack(object):

    _head = None

    #overwritten methods
    def __init__(self, *args):
        for var in args:
            self.push(var)


    def __contains__(self, bit):
        return self.search(bit)


    #custom methods
    def push(self, num):
        node = SLNode(num)

        if self._head is None:
            self._head = node
            return

        node.set_next(self._head)
        self._head = node


    def pop(self):
        if self._head is None:
            return None

        bit = self._head.get_data()
        self._head = self._head.get_next()

        return bit


    def peek(self):
        if self._head is None:
            return None

        return self._head.get_data();


    def search(self, bit):
        index = self._head

        while index is not None:
            if index.get_data() == bit:
                return True

            index = index.get_next();
            
        return False
