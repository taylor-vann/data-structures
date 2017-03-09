"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Doubly Linked Node base class
"""

class DLNode(object):

    _nxt = None
    _prev = None
    _data = None

    #overwritten methods
    def __init__(self, bit = None, prev = None, nxt = None):
        self.set_data(bit)
        self.set_prev(prev)
        self.set_next(nxt)


    #custom methods
    def set_next(self, nxt):
        self._nxt = nxt


    def get_next(self):
        return self._nxt


    def set_prev(self, prev):
        self._prev = prev


    def get_prev(self):
        return self._prev


    def set_data(self, bit):
        self._data = bit


    def get_data(self):
        return self._data
