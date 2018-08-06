"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class DLNode(object):
    def __init__(self, value = None, prev = None, nxt = None):
        self.value = value
        self.prev = prev
        self.nxt = nxt


class DLList(object):
    def __init__(self, *args):
        self._head = DLNode()
        self._tail = DLNode(None, self._head, None)
        self._head.nxt = self._tail

        for var in args:
            self.append(var)


    def __contains__(self, value):
        return self.find(value) is not None


    def unshift(self, value):
        self._head.nxt = DLNode(value, self._head, self._head.nxt)
        self._head.nxt.nxt.prev = self._head.nxt


    def shift(self):
        if self._head.nxt is self._tail:
            return

        curr = self._head.nxt
        self._head.nxt = self._head.nxt.nxt
        self._head.nxt.nxt.prev = self._head.nxt

        curr.nxt = None
        curr.prev = None

        return curr.value


    def append(self, value):
        self._tail.prev = DLNode(value, self._tail.prev, self._tail)
        self._tail.prev.prev.nxt = self._tail.prev


    def pop(self):
        if self._tail.prev is self._head:
            return

        curr = self._tail.prev

        self._tail.prev.prev.nxt = self._tail
        self._tail.prev = self._tail.prev.prev

        curr.nxt = None
        curr.prev = None

        return curr.value


    def remove(self, value):
        past, curr = self._head.nxt, self._head.nxt.nxt

        while curr:
            if past.value == value:
                past.prev.nxt = past.nxt
                past.nxt.prev = past.prev
                past.nxt = None
                past.prev = None

            past = curr
            curr = curr.nxt


    def peek(self):
        if self._head.nxt is not self._tail:
            return self._head.nxt.value


    def peek_last(self):
        if self._tail.prev is not self._head:
            return self._tail.prev.value


    def find(self, value):
        curr = self._head.nxt

        while curr is not self._tail:
            if curr.value == value:
                return curr

            curr = curr.nxt
