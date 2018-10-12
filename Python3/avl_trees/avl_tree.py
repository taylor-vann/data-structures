"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class AVLNode(object):
    def __init__(self, value=None, left=None, right=None, height=0):
        self.value = value
        self.left = left
        self.right = right
        self.height = height


class AVLTree(object):
    def __init__(self, *args):
        self._root = None

        if args:
            for value in args:
                self.insert(value)


    def __contains__(self, value):
        return self.search(self._root, value) is not None


    def search(self, node, value):
        if not node:
            return

        if node.value == value:
            return node

        if node.value < value:
            return self.search(node.right, value)

        return self.search(node.left, value)


    def insert(self, value):
        self._root = self._insert_rec(self._root, value)


    def _insert_rec(self, node, value):
        if not node:
            return AVLNode(value)

        if node.value < value:
            node.right = self._insert_rec(node.right, value)
        else:
            node.left = self._insert_rec(node.left, value)

        if abs(self._get_balance(node)) > 1:
            return self._tally(self._balance(node))

        return self._tally(node)


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

        if abs(self._get_balance(node)) > 1:
            return self._tally(self._balance(node))

        return self._tally(node)


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

        return self._tally(
            self._balance(
                self._get_rightmost(node.right)
            )
        )


    def _balance(self, node):
        if self._get_balance(node) < -1:
            if self._get_balance(node.left) > 0:
                node.left = self._left(node.left)

            return self._right(node)

        if self._get_balance(node.right) < 0:
            node.right = self._right(node.right)

        return self._left(node)


    def _get_balance(self, node):
        if not node:
            return 0

        return self._get_height(node.right) - self._get_height(node.left)


    def _left(self, curr):
        righter = curr.right
        curr.right = righter.left
        righter.left = curr

        self._tally(righter.left)

        return self._tally(righter)


    def _right(self, curr):
        lefter = curr.left
        curr.left = lefter.right
        lefter.right = curr

        self._tally(lefter.right)

        return self._tally(lefter)


    def _tally(self, node):
        if not node:
            return

        node.height = max(
            self._get_height(node.right),
            self._get_height(node.left)
        ) + 1

        return node


    def _get_height(self, node):
        if not node:
            return -1

        return node.height
