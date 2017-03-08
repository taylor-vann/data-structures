'''
Brian Taylor Vann
github.com/taylor-vann

Singly Linked Node
'''

class SLNode(object):
    #singly linked node
    _next = None
    _data = None

    #overridden methods
    def __init__(self, nxt = None, bit = None):
        self.set_next(nxt);
        self.set_data(bit);

    #custom methods
    def set_next(self, nxt):
        if isinstance(nxt, SLNode):
            self._next = nxt
        else:
            self._next = None

    def get_next(self):
        return self._next

    def set_data(self, bit):
        self._data = bit

    def get_data(self):
        return self._data
