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

    data = None
    left = None
    right = None

    def __init__(self, bit = None, lft = None, rht = None):
        self.data = bit
        self.left = lft
        self.rht = rht


    def get_data(self):
        return self.data


    def set_data(self, bit):
        self.data = bit


    def get_left(self):
        return self.left


    def set_left(self, lft):
        if isinstance(lft, BSTNode):
            self.left = lft


    def get_right(self):
        return self.right


    def set_right(self, rht):
        if isinstance(rht, BSTNode):
            self.right = rht

