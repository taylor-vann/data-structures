"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Base class for a Binary Search Tree Structure

Requirements:
- BSTNode.py

Methods:
- search(<data>)
- insert(<data>)
- remove(<data>)

- _replace(parent, child)
- _replace_node(parent, child, replacement)
- _replace_root(child, replacement)
"""

from BSTNode import BSTNode


class BSTree(object):

    _root = None

    #overwritten methods
    def __init__(self, *args):
        for var in args:
            self.insert(var)


    def __contains__(self, bit):
        return self.search(bit)


    #custom methods
    def insert(self, bit):
        if self._root == None:
            self._root = BSTNode(bit)
            return

        p = None
        c = self._root

        while c != None:
            if c.get_data() == bit:
                return

            if c.get_data() > bit:
                p = c
                c = c.get_left()
            else:
                p = c
                c = c.get_right()
 
        if p.get_data() > bit:
            p.set_left(BSTNode(bit))
        else:
            p.set_right(BSTNode(bit))


    def search(self, bit):
        n = self._root

        while n != None:
            if n.get_data() == bit:
                return n

            if n.get_data() > bit:
                n = n.get_left()
            else:
                n = n.get_right()

        return None


    def remove(self, bit):
        p = None
        c = self._root

        while c != None:
            if c.get_data() == bit:
                break

            if c.get_data() > bit:
                p = c
                c = c.get_left()
            else:
                p = c
                c = c.get_right()

        if c == None:
            return

        self._replace(p, c)


    def _replace(self, p, c):
        if c.get_left() and c.get_right():
            m = self._find_pred(c.get_right())

            self.remove(m.get_data())

            m.set_left(c.get_left())
            m.set_right(c.get_right())

            self._replace_node(p, c, m)
        elif c.get_left():
            self._replace_node(p, c, c.get_left())
        elif c.get_right():
            self._replace_node(p, c, c.get_right())
        else:
            self._replace_node(p, c)


    def _replace_node(self, p, c, r = None):
        if p == None:
            self._replace_root(c, r)
            return
        else:
            if p.get_left() == c:
                p.set_left(r)
            else:
                p.set_right(r)

        c.set_left(None)
        c.set_right(None)


    def _replace_root(self, c, r = None):
        if r is not None:
            r.set_left(c.get_left())
            r.set_right(c.get_right())

        self._root = r


    def _find_pred(self, n):
        node = n

        while node.get_left() != None:
            node = node.get_left()

        return node
