"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class PriorityQueue():
    def __init__(self, comparator=lambda x, y: x[0] > y[0]):
        self._que = []
        self._cmp = comparator


    def __contains__(self, value):
        for bit in self._que:
            if bit[1] == value:
                return True

        return False


    def push(self, weight, data):
        self._que.append((weight, data))
        self._perc_up()


    def pop(self):
        if not self._que:
            return None

        self._que[0], self._que[-1] = self._que[-1], self._que[0]

        bit = self._que.pop()
        self._perc_down()

        return bit[1]


    def peek(self):
        if self._que:
            return self._que[0][1]


    def _perc_up(self):
        curr = len(self._que) - 1
        nxt = curr // 2

        while curr and not self._cmp(self._que[curr], self._que[nxt]):
            self._que[curr], self._que[nxt] = self._que[nxt], self._que[curr]

            curr = nxt
            nxt = (curr - 1) // 2


    def _perc_down(self):
        l = len(self._que)
        curr = 0
        nxt = 2 * curr + 1

        while nxt < l:
            if nxt < l - 1 and self._cmp(self._que[nxt], self._que[nxt + 1]):
                nxt += 1

            if not self._cmp(self._que[curr], self._que[nxt]):
                return

            self._que[curr], self._que[nxt] = self._que[nxt], self._que[curr]

            curr = nxt
            nxt = curr * 2 + 1
