"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class SLNode(object):
    def __init__(self, value = None, nxt = None):
        self.data = value
        self.nxt = nxt


class Queue(object):

    _head = None
    _tail = None

    def __init__(self, *args):
        for arg in args:
            self.enqueue(arg)


    def __contains__(self, value):
        return self.search(value)


    def enqueue(self, value):
        node = SLNode(value)

        if self._tail and self._head:
            self._head.nxt = node
            self._head = node
            return

        self._tail = node
        self._head = node


    def dequeue(self):
        if self._tail is None:
            return None

        value = self._tail.data

        if self._tail is self._head:
            self._head = None

        self._tail = self._tail.nxt

        return value


    def peek(self):
        if self._head:
            return self._head.data


    def search(self, value):
        if not self._head:
            return False

        node = self._tail

        while node:
            if node.data == value:
                return True

            node = node.nxt

        return False
