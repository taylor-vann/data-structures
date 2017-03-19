"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Doubly Linked Node base class

Requirements:
- None

Methods:
- get_data()
- set_data(<data>)
- get_next()
- set_next(DLNode)
- get_prev()
- set_prev(DLNode)
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
    def get_data(self):
        return self._data


    def set_data(self, bit):
        self._data = bit


    def get_next(self):
        return self._nxt


    def set_next(self, nxt):
        self._nxt = nxt


    def get_prev(self):
        return self._prev


    def set_prev(self, prev):
        self._prev = prev
