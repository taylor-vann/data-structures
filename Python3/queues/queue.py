"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class DLNode(object):
    def __init__(self, value = None, prev = None, nxt = None):
        self.value = value
        self.prev = prev
        self.nxt = nxt


class Queue(object):
    def __init__(self, *args):
        self._head = DLNode()
        self._tail = DLNode(None, self._head)
        self._head.nxt = self._tail

        for arg in args:
            self.enqueue(arg)


    def __contains__(self, target):
        return self.find(target) is not None


    def enqueue(self, value):
        self._head.nxt = DLNode(value, self._head, self._head.nxt)
        self._head.nxt.nxt.prev = self._head.nxt


    def dequeue(self):
        if self._head.nxt is self._tail:
            return

        curr = self._tail.prev

        self._tail.prev = self._tail.prev.prev
        self._tail.prev.nxt = self._tail

        curr.nxt = None
        curr.prev = None

        return curr.value


    def peek(self):
        if self._head.nxt:
            return self._head.nxt.value


    def find(self, target):
        curr = self._head.nxt

        while curr is not self._tail:
            if curr.value == target:
                return curr

            curr = curr.nxt
