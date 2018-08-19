"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class PriorityQueue():
    def __init__(self, comparator=lambda x, y: x[0] > y[0]):
        self._q = []
        self._cmp = comparator


    def __contains__(self, value):
        for bit in self._q:
            if bit[1] == value:
                return True

        return False


    def __len__(self):
        return len(self._q)


    def push(self, weight, data):
        self._q.append((weight, data))
        self._perc_up()


    def pop(self):
        if not self._q:
            return None

        self._q[0], self._q[-1] = self._q[-1], self._q[0]

        bit = self._q.pop()
        self._perc_down()

        return bit[1]


    def peek(self):
        if self._q:
            return self._q[0][1]


    def _perc_up(self):
        curr = len(self._q) - 1
        nxt = curr // 2

        while curr and not self._cmp(self._q[curr], self._q[nxt]):
            self._q[curr], self._q[nxt] = self._q[nxt], self._q[curr]

            curr = nxt
            nxt = (curr - 1) // 2


    def _perc_down(self):
        l = len(self._q)
        curr = 0
        nxt = 2 * curr + 1

        while nxt < l:
            if nxt < l - 1 and self._cmp(self._q[nxt], self._q[nxt + 1]):
                nxt += 1

            if not self._cmp(self._q[curr], self._q[nxt]):
                return

            self._q[curr], self._q[nxt] = self._q[nxt], self._q[curr]

            curr = nxt
            nxt = curr * 2 + 1
