"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Singly Linked Node class
"""

class SLNode(object):

    _next = None
    _data = None

    #overridden methods
    def __init__(self, bit = None, nxt = None):
        self.set_data(bit);
        self.set_next(nxt);


    #custom methods
    def set_next(self, nxt):
        self._next = nxt


    def get_next(self):
        return self._next


    def set_data(self, bit):
        self._data = bit


    def get_data(self):
        return self._data
