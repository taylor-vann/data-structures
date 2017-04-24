"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Node class for the AVLTree structure

Requirements:
- None
"""

class AVLNode(object):

    _p = None
    _l = None
    _r = None


    #overrwritten methods
    def __init__(self, par = None, lft = None, rht = None):
        self.setParent(par)
        self.setLeft(lft)
        self.setRight(rht)


    #custom methods
    def getParent(self):
        return self._p


    def setParent(self, par):
        if isinstance(par, AVLNode):
            self._p = par


    def getLeft(self):
        return self._l


    def setLeft(self, lft):
        if isinstance(lft, AVLNode):
            self._l = lft


    def getRight(self):
        return self._r


    def setRight(self, rht):
        if isinstance(rht, AVLNode):
            self._r = rht


    def getHeight(self):
        h = 1;

        if(self._l):
            h += self._l.getHeight()
        elif(self._r):
            h += self._r.getHeight()

        return h


    def getBalance(self):
        b = 0;

        if(self._l):
            b -= 1
        elif(self._r):
            b += 1

        return b
