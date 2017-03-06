'''
Brian Taylor Vann
github.com/taylor-vann

Singly Linked Node
'''

class SLNode(object):
    #singly linked node
    __next = None
    __data = None

    #overridden methods
    def __init__(self, nxt = None, bit = None):
        self.set_next(nxt);
        self.set_data(bit);

    def __del__(self):
        print("Deleted a node, yay!")

    #custom methods
    def set_next(self, nxt):
        if isinstance(nxt, SLNode):
            self.__next = nxt
        else:
            self.__next = None

    def get_next(self):
        return self.__next

    def set_data(self, bit):
        self.__data = bit

    def get_data(self):
        return self.__data
