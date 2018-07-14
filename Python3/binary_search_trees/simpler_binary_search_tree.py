"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class BSTNode(object):
    def __init__(self, value = None, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right


class SimplerBSTree(object):
    def __init__(self, *args):
        self._root = None

        for var in args:
            self.insert(var)


    def __contains__(self, value):
        return self._search(value)[-1]


    def _search(self, value):
        prev, curr = None, self._root

        while curr:
            if curr.data == value:
                return prev, curr

            if curr.data < value:
                prev, curr = curr, curr.right
            else:
                prev, curr = curr, curr.left

        return prev, curr


    def insert(self, value):
        if value == None:
            return

        node = BSTNode(value)

        if not self._root:
            self._root = node
            return

        self._bounce_and_insert(None, self._root, node)


    def _bounce_and_insert(self, prev, curr, node):
        if not curr:
            if prev.data < node.data:
                prev.right = node
            else:
                prev.left = node

        if curr.data < node.data:
            self._bounce_and_insert(curr, curr.right, node)
        else:
            self._bounce_and_insert(curr, curr.left, node)


    def remove(self, value):
        if not self._root:
            return

        prev, curr = self._search(value)

        if not curr:
            return

        if curr is self._root:
            return

        if prev.data < curr.data:
            prev.right = None
        else:
            prev.left = None

        left = curr.left
        right = curr.right







    def _get_rightmost_left(self, prev, curr):
        if not curr:
            return curr

        if not curr.right:
            if prev:
                prev.right = curr.left
            return curr

        return self._get_rightmost_left(curr, curr.right)
