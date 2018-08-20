"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class SLNode(object):
    def __init__(self, value = None, nxt = None):
        self.value = value
        self.nxt = nxt


class Stack(object):
    def __init__(self, *args):
        self._head = SLNode()

        for value in args:
            self.push(value)


    def __contains__(self, target):
        return self.find(target)


    def push(self, value):
        self._head.nxt = SLNode(value, self._head.nxt)


    def pop(self):
        if not self._head.nxt:
            return

        node = self._head.nxt
        self._head.nxt = self._head.nxt.nxt
        node.nxt = None

        return node.value


    def peek(self):
        if self._head.nxt:
            return self._head.nxt.value


    def find(self, target):
        curr = self._head.nxt

        while curr:
            if curr.value == target:
                break

            curr = curr.nxt;

        return curr
