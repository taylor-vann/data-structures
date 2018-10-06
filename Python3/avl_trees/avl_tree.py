"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class AVLNode(object):
    def __init__(self, value=None, left=None, right=None, height=1):
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
        else:
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
        pass


    def _remove_rec(self, value):
        pass


    def _get_balance(self, node):
        if not node:
            return 0

        return (
            self._get_height(node.right)
            - self._get_height(node.left)
        )


    def _balance(self, node):
        if self._get_balance(node) < -1:
            print("about to rotate right")
            if self._get_balance(node.right) > 0:
                node.left = self._left(node.left)

            return self._right(node)
        else:
            print("about to rotate left")
            if self._get_balance(node.right) < 0:
                node.right = self._right(node.right)

            return self._left(node)


    def _left(self, curr):
        print("rotate left")

        node = curr.right
        curr.right = node.left
        node.left = curr

        self._tally(node.left)
        self._tally(node.right)

        return node


    def _right(self, curr):
        print("rotate left")

        node = curr.left
        curr.left = node.right
        node.right = curr

        self._tally(node.left)
        self._tally(node.right)

        return node


    def _get_height(self, node):
        if not node:
            return 0

        return node.height


    def _tally(self, node):
        if not node:
            return

        node.height = max(
            self._get_height(node.right),
            self._get_height(node.left)
        ) + 1

        return node
