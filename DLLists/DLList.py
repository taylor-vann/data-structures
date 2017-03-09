"""
Brian Taylor Vann
github.com/taylor-vann

Descritpion:
- Doubly Linked List base class

Requires:
- DLNode.py

Methods:
- insert(<data>)
- remove()
- unshift(<data>)
- shift(<data>)
- insert_after(<new>, <data>)
- remove_data(<data>)
- peek()
- peek_last()
- search()
"""

from DLNode import DLNode


class DLList(object):

    _head = None
    _tail = None

    #overwritten methods
    def __init__(self, *args):
        for var in args:
            self.insert(var)


    def __contains__(self, bit):
        return self.find(bit) is not None


    #custom methods
    def insert(self, bit):
        node = DLNode(bit)

        if self._head is None:
            self._head = node
            self._tail = node

            return

        self._head.set_next(node)
        node.set_prev(self._head)
        self._head = node


    def remove(self):
        if self._head is None:
            return None

        bit = self._head
        self._head = bit.get_prev()
        bit.set_prev(None)

        return bit.get_data()


    def remove_data(self, bit):
        node = self.find(bit)

        if node is None:
            return None

        if node is self._head:
            self._head = self._head.get_prev()
            return node.get_data()

        if node is self._tail:
            self._tail = self._tail.get_next()
            return node.get_data()

        prev = node.get_prev()
        nxt = node.get_next()

        prev.set_next(nxt)
        nxt.set_prev(prev)

        return node.get_data()


    def unshift(self, bit):
        node = DLNode(bit)

        if self._tail is None:
            self._head = node
            self._tail = node

            return

        self._tail.set_prev(node)
        node.set_next(self._tail)
        self._tail = node


    def shift(self):
        if self._tail is None:
            return None

        bit = self._tail
        self._tail = bit.get_next()
        bit.set_next(None)

        return bit.get_data()


    def insert_after(self, bit, aft):
        node = DLNode(bit)

        if self._head is None:
            self._head = node
            self._tail = node

        found = self.find(aft)

        if found is None:
            node.set_next(self._tail)
            self._tail.set_prev(node)
            self._tail = node
            return

        node.set_next(found)
        node.set_prev(found.get_prev())
        found.set_prev(node)


    def peek(self):
        if self._head is None:
            return None

        return self._head.get_data()


    def peek_last(self):
        if self._tail is None:
            return None

        return self._tail.get_data()


    def find(self, bit):
        if self._head is None:
            return None

        index = self._head

        while index is not None:
            if index.get_data() == bit:
                return index

            index = index.get_prev()

        return None
