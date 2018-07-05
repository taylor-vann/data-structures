"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class SLNode(object):
    def __init__(self, value = None, nxt = None):
        self.data = value
        self.nxt = nxt


class Stack(object):

    _head = None

    def __init__(self, *args):
        for value in args:
            self.push(value)


    def __contains__(self, value):
        return self.search(value)


    def push(self, value):
        node = SLNode(value)

        if not self._head:
            self._head = node
            return

        node.nxt = self._head
        self._head = node


    def pop(self):
        if not self._head:
            return None

        node = self._head
        self._head = self._head.nxt
        node.nxt = None

        return node.data


    def peek(self):
        if self._head:
            return self._head.data


    def search(self, value):
        index = self._head

        while index is not None:
            if index.data == value:
                break

            index = index.nxt;

        return index
