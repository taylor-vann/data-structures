"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

class Node(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.prev = left
        self.nxt = right


class LRUCache(object):
    def __init__(self, count = 10):
        self._count = count
        self._entries = {}

        self._head = Node()
        self._tail = Node(None, self._head, None)
        self._head.nxt = self._tail


    def __contains__(self, value):
        return value in self._entries


    def insert(self, value):
        self._entries[value] = Node(value)
        self._send_to_head(self._entries[value])

        if self._count < len(self._entries):
            self._entries.pop(self._tail.prev.value, None)
            self._remove_from_list(self._tail.prev)


    def update(self, value, replacement):
        node = self._entries.pop(value, None)

        if node:
            node.value = replacement
            self._entries[replacement] = node
            self._send_to_head(node)


    def remove(self, value):
        if value in self._entries:
            self._remove_from_list(node)
            self._entries.pop(value, None)


    def _send_to_head(self, node):
        if node.prev and node.nxt:
            self._remove_from_list(node)

        self._head.nxt.prev = node
        node.nxt = self._head.nxt
        self._head.nxt = node
        node.prev = self._head


    def _remove_from_list(self, node):
        if self._head.nxt is self._tail:
            return

        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        node.prev = None
        node.nxt = None
