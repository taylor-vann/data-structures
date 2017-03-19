"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Singly Linked Node class

Requirements:
- None

Methods:
- get_data()
- set_data(<data>)
- get_next()
- set_next(<SLNode>)
"""

class SLNode(object):

    _next = None
    _data = None

    #overridden methods
    def __init__(self, bit = None, nxt = None):
        self.set_data(bit);
        self.set_next(nxt);


    #custom methods
    def get_data(self):
        return self._data


    def set_data(self, bit):
        self._data = bit


    def get_next(self):
        return self._next


    def set_next(self, nxt):
        if isinstance(nxt, SLNode):
            self._next = nxt
