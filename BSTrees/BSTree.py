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

        self.replace(p, c)


    def replace(self, p, c):
        if c.get_left() and c.get_right():
            m = self.find_pred(c.get_right())
            m.set_left(c.get_left())
            m.set_right(c.get_right())

            c.set_left(None)
            c.set_right(None)

            self.replace_node(p, c, m)
        elif c.get_left():
            self.replace_node(p, c, c.get_left())
        elif c.get_right():
            self.replace_node(p, c, c.get_right())
        else:
            self.replace_node(p, c)


    def replace_node(self, p, c, val = None):
        if p == None:
            self.replace_root(c, val)
            return

        if p.get_left() == c:
            p.set_left(val)
        else:
            p.set_right(val)

        c.set_left(None)
        c.set_right(None)


    def replace_root(self, c, val = None):
        val.set_left(c.get_left())
        val.set_right(c.get_right())
        self._root = val

        c.set_left(None)
        c.set_right(None)


    def find_pred(self, n):
        node = n

        while node.get_left() != None:
            node = node.get_left()

        return node
