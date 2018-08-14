"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class MaxHeap(object):
    def __init__(self, *args):
        self._bucket = []
        self._k = 2

        for var in args:
            self.push(var)


    def __contains__(self, target):
        return target in self._bucket


    def __len__(self):
        return len(self._bucket)


    #custom methods
    def push(self, target):
        self._bucket.insert(0, target)
        self._perc_down(0)


    def pop(self):
        l = len(self._bucket)

        if l == 0:
            return None

        if l == 1:
            return self._bucket.pop()

        target = self._bucket.pop(0)
        self._perc_down(0)

        return target


    def remove(self, target):
        l = len(self._bucket) - 1

        for i in range(0, len(self._bucket)):
            if self._bucket[i] == target:
                self._bucket[i], self._bucket[l] = self._bucket[l], self._bucket[i]
                pip = self._bucket.pop(i)
                self._perc_down(i)

                return pip


    def peek(self):
        if len(self._bucket):
            return self._bucket[0]


    def _perc_down(self, i = 0):
        curr = i
        nxt = self._k * curr + 1

        while nxt < len(self._bucket):
            if nxt < len(self._bucket) - 1 and self._bucket[nxt] < self._bucket[nxt + 1]:
                nxt += 1

            if self._bucket[curr] < self._bucket[nxt]:
                self._bucket[curr], self._bucket[nxt] = self._bucket[nxt], self._bucket[curr]
                curr = nxt
                nxt = nxt * self._k + 1
            else:
                break
