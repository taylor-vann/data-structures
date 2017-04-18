"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Node class for the AVLTree structure

Requirements:
- None
"""

class AVLNode(object):

    _balance = None
    _parent = None
    _left = None
    _right = None


    #overrwritten methods
    def __init__(self, par = None, lft = None, rgt = None):
        if isinstance(par, AVLNode):
            self._parent = par
        if isinstance(lft, AVLNode):
            self._left = lft
        if isinstance(rgt, AVLNode):
            self._right = rgt

        self._height = self._find_height();


    #custom methods
    def getParent(self):
        return self._parent


    def getLeft(self):
        return self._left


    def getRight(self):
        return self._right


    def getHeight(self):
        return self._height


    def _find_height(self):
        height = 0;

        if(self._left):
            height += self._left._find_height()
        elif(self._right):
            height += self._right._find_height()

        return height


    def _find_balance(self):
        balance = 0;

        if(self._left):
            height += self._left._find_height()
        elif(self._right):
            height -= self._right._find_height()

        return balance
