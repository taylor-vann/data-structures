"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class SimpleHash(object):
    def __init__(self, prime = 137, delta = 31):
        self._prime = prime
        self._delta = delta
        self._length = 0
        self._bucket = [[] for _ in range(self._prime)]


    def __len__(self):
        return self._length


    def __contains__(self, key):
        for bit in self._bucket[self._hash(key)]:
            if bit[0] == key:
                return True

        return False


    def __getitem__(self, key):
        for bit in self._bucket[self._hash(key)]:
            if bit[0] == key:
                return bit[1]


    def _hash(self, key):
        return (id(key) * self._delta) % self._prime


    def insert(self, key, value):
        self.delete(key)
        self._length += 1
        self._bucket[self._hash(key)].append((key, value))


    def delete(self, key):
        hash = self._hash(key)

        for index, bit in enumerate(self._bucket[hash]):
            if bit[0] == key:
                self._length -= 1

                return self._bucket[hash].pop(index)[1]
