"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class Node(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self, *args):
        self._root = None

        for var in args:
            self.insert(var)

    def __contains__(self, value):
        return self._search(self._root, value) is not None

    def _search(self, node, value):
        if not node:
            return

        if node.value == value:
            return node

        if node.value < value:
            return self._search(node.right, value)

        return self._search(node.left, value)

    def insert(self, value):
        self._root = self._insert_rec(self._root, value)

    def _insert_rec(self, node, value):
        if not node:
            return Node(value)

        if node.value < value:
            node.right = self._insert_rec(node.right, value)
        else:
            node.left = self._insert_rec(node.left, value)

        return node

    def remove(self, value):
        self._root = self._remove_rec(self._root, value)

    def _remove_rec(self, node, value):
        if not node:
            return

        if node.value == value:
            return self._replace(node)

        if node.value < value:
            node.right = self._remove_rec(node.right, value)
        else:
            node.left = self._remove_rec(node.left, value)

        return node

    def _replace(self, node):
        if not node:
            return
        if not node.left:
            return node.right

        rightmost = self._get_rightmost(node.left)
        rightmost.right = node.right

        node.left = None
        node.right = None

        return rightmost

    def _get_rightmost(self, node):
        if not node.right:
            return node

        return self._get_rightmost(node.right)
