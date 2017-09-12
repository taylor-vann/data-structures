"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- SimpleHash structre class

Methods:
- __len__
- __contains__

- search(key)
- insert(key, value)
- delete(key)
"""


class SimpleHash(object):

    _m = None
    _n = None
    _bucket = None

    def __init__(self, m = 137, n = 31):
        self._m = m
        self._n = n
        self._bucket = []

        for i in range(self._m):
            self._bucket.append([])


    def __len__(self):
        l = 0
        for b in self._bucket:
            l += len(b)

        return l


    def __contains__(self, key):
        return self.search(key)


    def hash(self, key):
        s = str(key)
        v = 0

        for c in s:
            v += ord(c)

        return (v * self._n) % self._m


    def search(self, key):
        k = self.hash(key)

        for n in self._bucket[k]:
            if n[0] == key:
                return n[1]


    def insert(self, key, value):
        k = self.hash(key)

        for n in self._bucket[k]:
            if n[0] == key:
                n[1] = value
                return

        self._bucket[k].append([str(key), value])


    def delete(self, key):
        k = self.hash(key)

        for i in range(len(self._bucket[k])):
            if self._bucket[k][i][0] == key:
                v = self._bucket[k][i][1]
                self._bucket[k].pop(i)
                return v[0]
