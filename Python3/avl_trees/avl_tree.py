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
            node.balance += 1
        else:
            node.left = self._insert_rec(node.left, value)
            node.balance -= 1

        if abs(node.balance) > 1:
            return self._balance(node)

        return node


    def _balance(self, node):
        if node.balance > 1:
            if node.right.balance < 0:
                node.right = self._tally(self._right(node.right))

            return self._tally(self._left(node))
        elif node.balance < -1:
            if node.left.balance > 0:
                node.left = self._tally(self._left(node.left))

            return self._tally(self._right(node))

        return node


    def remove(self, value):
        pass


    def _remove_rec(self, value):
        pass


    def _left(self, curr):
        node = curr.right
        curr.right = node.left
        node.left = curr

        node.left.balance -= 1
        node.balance -= 1

        return node


    def _right(self, curr):
        node = curr.left
        curr.left = node.right
        node.right = curr

        node.right.balance += 1
        node.balance += 1

        return node


    def _tally(self, node):
        if node.left:
            node.balance += node.left.balance

        if node.right:
            node.balance += node.right.balance

        return node
