"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class SLNode(object):
    def __init__(self, value = None, nxt = None):
        self.value = value
        self.nxt = nxt


class SLList(object):
    def __init__(self, *args):
        self._head = SLNode()

        for var in args:
            self.append(var)


    def __contains__(self, value):
        return self._find(value) is not None


    def append(self, value):
        self._head.nxt = SLNode(value, self._head.nxt)


    def pop(self):
        if not self._head.nxt:
            return

        curr = self._head.nxt
        self._head.nxt = self._head.nxt.nxt
        curr.nxt = None

        return curr.value


    def remove(self, value):
        past, curr = self._head, self._head.nxt

        while curr:
            if curr.value == value:
                past.nxt = past.nxt.nxt
                curr.nxt = None
                curr = past.nxt
            else:
                past = curr
                curr = curr.nxt


    def peek(self):
        if self._head.nxt:
            return self._head.nxt.value


    def _find(self, value):
        curr = self._head.nxt

        while curr:
            if curr.value == value:
                return curr

            curr = curr.nxt
