"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class AVLNode(object):
    def __init__(self, value=None, left=None, right=None, balance=0):
        self.value = value
        self.left = left
        self.right = right
        self.balance = balance


class AVLTree(object):
    def __init__(self, *args):
        self._root = args[0]

        for value in args[1:]:
            self.insert(value)


    def __contains__(self, value):
        return self.search(self._root, value) is not None


    def search(self, node, value):
        if not self._root:
            return

        curr = self._root

        while curr:
            if curr.value == value:
                return curr

            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right


    def insert(self, value):
        pass


    def remove(self, value):
        pass


    def _left(self, e, a, p):
        # rotate left
        pass


    def _right(self, e, a, p, c):
        # rotate right
        pass


    def _clr(self, n):
        n.set_left(None)
        n.set_right(None)
