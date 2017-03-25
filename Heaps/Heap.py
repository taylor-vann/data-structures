"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Heap structure class

Methods:
- push()
- pop()
- remove()
- peak()
- search()
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
        return self.search(bit)


    #custom methods
    def push(self, bit):
        self._h.append(bit)
        self._perc_up(len(self._h) - 1)


    def pop(self, n = 0):
        l = len(self._h) - 1

        if l < 0:
            return None

        if l == 1:
            return self._h.pop()

        self._h[n], self._h[l] = self._h[l], self._h[n]
        bit = self._h.pop(l)

        self._perc_down(n)

        return bit


    def remove(self, bit):
        for i in range(self._h):
            if self._h[i] == bit:
               return self.pop(i)

        return None


    def peek(self):
        if len(self._h):
            return self._h[0]

        return None


    def search(self, bit):
        for var in self._h:
            if var == bit:
                return var


    def _perc_up(self, n):
        c = n
        p = c // 2

        while c > 0:
            if self._h[c] > self._h[p]:
                self._h[c], self._h[p] = self._h[p], self._h[c]
                c = p
                p = c // 2
            else:
                break


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
