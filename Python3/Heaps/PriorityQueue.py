"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class PriorityQueue(object):
    def __init__(self, comparator):
        self._queue = []
        self._cmp = comparator
        self._k = 2


    def __contains__(self, value):
        def _search(self, bit):
            for var in self._queue:
                if var["data"] == bit:
                    return True

        return False


    def __len__(self):
        return len(self._queue)


    def push(self, data = None, weight = None):
        self._queue.insert(0, {"data": data, "weight": weight})
        self._perc_down(0)


    def pop(self):
        l = len(self._queue)

        if l == 0:
            return None

        if l == 1:
            return self._queue.pop()

        bit = self._queue.pop(0)
        self._perc_down(0)

        return bit


    def peek(self):
        if len(self._queue):
            return self._queue[0]["data"]


    def _perc_down(self, i = 0):
        c = i
        n = self._k * c + 1

        while n < len(self._queue):
            if n < len(self._queue) - 1 and \
                self._queue[n]["weight"] > self._queue[n + 1]["weight"]:

                n += 1

            if self._queue[c]["weight"] > self._queue[n]["weight"]:
                self._queue[c], self._queue[n] = self._queue[n], self._queue[c]
                c = n
                n = n * self._k + 1
            else:
                break
