"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- SimpleHash structre class

Methods:
- __len__
- __contains__

- search
- insert
- delete
"""


class SimpleHash(object):

    m = None
    n = None
    bucket = None

    def __init__(self, m = 137, n = 31):
        self.m = m
        self.n = n
        self.bucket = []

        for i in range(self.m):
            self.bucket.append([])

        print(m, n, len(self.bucket))


    def hash(self, key):
        s = str(key)
        v = 0

        for c in s:
            v += ord(c)

        return (v * self.n) % self.m


    def search(self, key):
        k = self.hash(key)

        for n in self.bucket[k]:
            if n[0] == key:
                return n[1]


    def insert(self, key, value):
        k = self.hash(key)

        for n in self.bucket[k]:
            if n[0] == key:
                n[1] = value
                return

        self.bucket[k].append([key, value])


    def delete(self, key):
        k = self.hash(key)

        for i in range(len(self.bucket[k])):
            if self.bucket[k][i][0] == key:
                self.bucket[k].pop(i)
                return
