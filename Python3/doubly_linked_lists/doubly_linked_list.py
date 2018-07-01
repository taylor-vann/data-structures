"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class DLNode(object):
    def __init__(self, data = None, prev = None, nxt = None):
        self.data = data
        self.prev = prev
        self.nxt = nxt


class DLList(object):

    _head = None
    _tail = None

    def __init__(self, *args):
        for var in args:
            self.append(var)


    def __contains__(self, value):
        return self.find(value) != None


    def unshift(self, data):
        node = DLNode(data)

        if self._head and self._tail:
            node.nxt = self._head
            self._head.prev = node
            self._head = node
            return

        self._head = node
        self._tail = node


    def shift(self):
        if not self._head:
            return

        value = self._head.data

        self._head.prev = None
        self._head = self._head.nxt
        self._head.prev = None

        return value


    def append(self, value):
        node = DLNode(value, self._tail)

        if self._head and self._tail:
            self._tail.nxt = node
            self._tail = node
            return

        self._head = node
        self._tail = node


    def pop(self):
        if not self._tail:
            return

        value = self._tail.data

        if self._head is self._tail:
            self._head = None
            self._tail = None
            return value

        prev = self._tail.prev

        self._tail.prev = None
        self._tail = prev
        self._tail.next = None

        return value


    def remove(self, value):
        node = self._head

        while node:
            if node.data == value:
                if node.prev:
                    node.prev.nxt = node.nxt
                if node.nxt:
                    node.nxt.prev = node.prev

                if self._head is node:
                    self._head = self._head.nxt
                    self._head.prev = None

                if self._tail is node:
                    self._tail = self._tail.prev
                    self._tail.nxt = None

                node.prev = None
                node.nxt = None

            node = node.nxt


    def peek(self):
        if self._head:
            return self._head.data


    def peek_last(self):
        if self._tail:
            return self._tail.data


    def find(self, value):
        node = self._head

        while node:
            if node.data == value:
                return node

            node = node.nxt
