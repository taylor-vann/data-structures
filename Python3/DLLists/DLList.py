"""
Brian Taylor Vann
github.com/taylor-vann

Descritpion:
- Doubly Linked List base class
"""

from DLNode import DLNode


class DLList(object):

    _head = None
    _tail = None

    #overwritten methods
    def __init__(self, *args):
        for var in args:
            self.append(var)


    def __contains__(self, bit):
        return not self.find(bit)


    #custom methods
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
        self._head = self._head.nxt
        self._head.prev = None
        bit.prev = None

        return bit.data


    def remove(self, bit):
        node = self.find(bit)

        while node:
            if not node:
                return

            if self._head == node:
                self._head = self._head.nxt
                node.prev = None

            if self._tail == node:
                self._tail = self._tail.prev
                node.prev = None

            node.prev.nxt = node.nxt
            node.next.prev = node.prev

            node.nxt = None
            node.prev = None

            node = self.find(bit)


    def append(self, bit):
        node = DLNode(bit, self._tail)

        if not self._tail:
            self._head = node
            self._tail = node
            print(node.data)

            return

        self._tail.next = node
        self._tail = node
        print(self._tail.data)


    def pop(self):
        if not self._tail:
            return
        if self._head == self._tail:
            self._head = None
            self._tail = None
            return

        bit = self._tail
        self._tail = self._tail.prev
        bit.prev = None

        return bit.data


    def insert_after(self, bit, aft):
        node = DLNode(bit)
        found = self.find(aft)

        if not found:
            return


    def peek(self):
        if self._head is None:
            return None

        return self._head.data


    def peek_last(self):
        if self._tail is None:
            return None

        return self._tail.data


    def find(self, bit):
        if not self._head:
            return

        node = self._head

        while node:
            # print(node.data)
            if node.data == bit:
                return node

            node = node.nxt
