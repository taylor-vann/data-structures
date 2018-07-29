"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class Node(object):
    def __init__(self, value = None, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
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
        if not value:
            return

        prev, curr = self._search(value)

        if curr:
            return

        node = Node(value)

        if not self._root:
            self._root = node
        elif prev.data < node.data:
            prev.right = node
        else:
            prev.left = node


    def remove(self, value):
        prev, curr = self._search(value)

        if not curr:
            return

        if curr is self._root:
            if not curr.left and not curr.right:
                self._root = None
            elif not curr.left:
                self._root = curr.right
            elif not curr.right:
                self._root = curr.left
            else:
                left = self._root.left
                right = self._root.right
                self._root = self._get_rightmost_left(None, curr.left)
                self._root.left = None
                self._root.right = right

                if self._root is not left:
                    self._root.left = left
        elif curr.data < prev.data:
            if not curr.left and not curr.right:
                prev.left = None
            elif not curr.left:
                prev.left = curr.right
            elif not curr.right:
                prev.left = curr.left
            else:
                replacement = self._get_rightmost_left(None, curr.left)
                replacement.left = curr.left
                prev.left = replacement
        else:
            if not curr.left and not curr.right:
                prev.right = None
            elif not curr.left:
                prev.right = curr.left
            elif not curr.right:
                prev.left = curr.right
            else:
                replacement = self._get_rightmost_left(None, curr.left)
                replacement.right = curr.right
                prev.right = replacement


    def _get_rightmost_left(self, prev, curr):
        if not curr:
            return curr

        if not curr.right:
            if prev:
                prev.right = curr.left
            return curr

        return self._get_rightmost_left(curr, curr.right)
