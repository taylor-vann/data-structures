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
            print(c.get_data())
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
        node = self._root

        while node != None:
            if node.get_data() == bit:
                return node

            if node.get_data() > bit:
                node = node.get_left()

            if node.get_data() < bit:
                node = node.get_right()

        return None
