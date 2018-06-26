"""
Brian Taylor Vann
github.com/taylor-vann
"""

from DLNode import DLNode


class DLList(object):

    _head = None
    _tail = None

    def __init__(self, *args):
        for var in args:
            self.append(var)


    def __contains__(self, bit):
        return self.find(bit) != None


    def unshift(self, data):
        node = DLNode(data)

        if not self._head:
            self._head = node
            self._tail = node
            return
        
        node.nxt = self._head
        self._head.prev = node
        self._head = node


    def shift(self):
        if not self._head:
            return

        bit = self._head
        bit.prev = None
        self._head = self._head.nxt
        self._head.prev = None

        return bit.data


    def append(self, bit):
        node = DLNode(bit, self._tail)

        if not self._tail:
            self._head = node
            self._tail = node
            return

        self._tail.nxt = node
        self._tail = node


    def pop(self):
        if not self._tail:
            return
        if self._tail and self._head == self._tail:
            data = self._head.data
            self._head = None
            self._tail = None
            return data
        bit = self._tail
        self._tail = self._tail.prev
        self._tail.next = None
        bit.prev = None

        return bit.data


    def remove(self, bit):
        node = self.find(bit)
        
        while node:
            if node.prev:
                node.prev.nxt = node.nxt
            if node.nxt:
                node.nxt.prev = node.prev

            if self._head == node:
                self._head = self._head.nxt
                self._head.prev = None

            if self._tail == node:
                self._tail = self._tail.prev
                self._tail.nxt = None
            
            node.prev = None
            node.nxt = None

            node = self.find(bit)


    def peek(self):
        if self._head:
            return self._head.data


    def peek_last(self):
        if self._tail:
            return self._tail.data
        

    def find(self, bit):
        node = self._head

        while node:
            if node.data == bit:
                return node

            node = node.nxt
