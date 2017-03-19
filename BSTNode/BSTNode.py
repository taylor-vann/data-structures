"""
Brian Taylory Van
github.com/taylor-vann

Description:
- Node for a Binary Search Tree

Requirements:
- None

Basic Methods:
- get_data()
- set_data(<data>)
- get_right()
- set_right(<BSTNode>)
- get_left()
- set_left(<BSTNode>)
"""

class BSTNode(object):

    _data = None
    _left = None
    _right = None

    def __init__(self, bit = None, lft = None, rht = None):
        self._data = bit
        self._left = lft
        self._right = rht


    def get_data(self):
        return self._data


    def set_data(self, bit):
        self._data = bit


    def get_left(self):
        return self._left


    def set_left(self, lft):
        if isinstance(lft, BSTNode):
            self._left = lft


    def get_right(self):
        return self._right


    def set_right(self, rht):
        if isinstance(rht, BSTNode):
            self._right = rht

