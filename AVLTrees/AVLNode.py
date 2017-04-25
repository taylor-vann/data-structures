"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Node class for the AVLTree structure

Requirements:
- None
"""

class AVLNode(object):

    _d = None
    _p = None
    _l = None
    _r = None


    #overrwritten methods
    def __init__(self, bit = None, par = None, lft = None, rht = None):
        self.set_data(bit)
        self.set_parent(par)
        self.set_left(lft)
        self.set_right(rht)


    #custom methods
    def get_data(self):
        return self._d


    def set_data(self, bit):
        self._d = bit


    def get_parent(self):
        return self._p


    def set_parent(self, par):
        if isinstance(par, AVLNode) or par == None:
            self._p = par


    def get_left(self):
        return self._l


    def set_left(self, lft):
        if isinstance(lft, AVLNode) or lft == None:
            self._l = lft


    def get_right(self):
        return self._r


    def set_right(self, rht):
        if isinstance(rht, AVLNode) or rht == None:
            self._r = rht


    def get_height(self):
        h = 1;
        l = 0;
        r = 0;

        if(self._l):
            l += self._l.get_height()

        if(self._r):
            r += self._r.get_height()

        h += max([l, r])

        return h


    def get_balance(self):
        b = 0;

        if(self._l):
            b -= 1

        if(self._r):
            b += 1

        return b
