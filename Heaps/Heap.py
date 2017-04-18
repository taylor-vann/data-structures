"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Heap structure class

Methods:
- __len__
- __contains__

- push(<data>)
- pop() or pop(<index>)
- remove() or remove(<val>)
- peak()
"""


class Heap(object):

    _h = None
    _k = None

    #overwritten methods
    def __init__(self, *args):
        self._h = []
        self._k = 2

        for var in args:
            self.push(var)


    def __contains__(self, bit):
        return self._search(bit)


    def __len__(self):
        return len(self._h)


    #custom methods
    def push(self, bit):
        self._h.insert(0, bit)
        self._perc_down(0)


    def pop(self, n = 0):
        l = len(self._h)

        if l == 0:
            return None

        if l == 1:
            return self._h.pop()

        if l < n:
            return None

        bit = self._h.pop(n)
        self._perc_down(n)

        return bit


    def remove(self, bit):
        l = len(self._h) - 1

        for i in range(0, len(self._h)):
            if self._h[i] == bit:
                pip = self._h.pop(i)
                self._perc_down(i)

                return pip

        return None


    def peek(self):
        if len(self._h):
            return self._h[0]

        return None


    def _search(self, bit):
        for var in self._h:
            if var == bit:
                return var


    def _heapify(self):
        l = len(self._h) - 1
        b = l // 2

        while l > b:
            self._perc_up(b)
            l -= 1


    def _perc_down(self, i = 0):
        c = i
        n = self._k * c + 1

        while n < len(self._h):
            if n < len(self._h) - 1 and self._h[n] < self._h[n + 1]:
                n += 1

            if self._h[c] < self._h[n]:
                self._h[c], self._h[n] = self._h[n], self._h[c]
                c = n
                n = n * self._k + 1
            else:
                break
