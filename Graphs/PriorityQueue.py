"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Priority Queue structure class

Methods:
- __len__
- __contains__

- peak()
- push(data, weight)
- pop()
- remove(data)
"""


class PriorityQueue(object):

    _h = None
    _k = None

    #overwritten methods
    def __init__(self):
        self._h = []
        self._k = 2


    def __contains__(self, bit):
        return self._search(bit)


    def __len__(self):
        return len(self._h)


    #custom methods
    def push(self, data = None, weight = None):
        self._h.insert(0, {"data": data, "weight": weight})
        self._perc_down(0)


    def pop(self):
        l = len(self._h)

        if l == 0:
            return None

        if l == 1:
            return self._h.pop()

        bit = self._h.pop(0)
        self._perc_down(0)

        return bit


    def remove(self, bit):
        l = len(self._h) - 1

        for i in range(0, len(self._h)):
            if self._h[i] == bit:
                self._h[i], self._h[l] = self._h[l], self._h[i]
                pip = self._h.pop()
                self._perc_down(i)

                return pip


    def peek(self):
        if len(self._h):
            return self._h[0]["data"]


    def _search(self, bit):
        for var in self._h:
            if var["data"] == bit:
                return var["data"]


    def _perc_down(self, i = 0):
        c = i
        n = self._k * c + 1

        while n < len(self._h):
            if n < len(self._h) - 1 and \
                self._h[n]["weight"] > self._h[n + 1]["weight"]:

                n += 1

            if self._h[c]["weight"] > self._h[n]["weight"]:
                self._h[c], self._h[n] = self._h[n], self._h[c]
                c = n
                n = n * self._k + 1
            else:
                break
