"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph data structure

Requirements:
- GraphNode.py
"""

from GraphNode import GraphNode


class Graph (object):

    _nodes = None

    # overridden
    def __init__(self, *args):
        self._nodes = {}

        self.add_nodes(*args)


    def __contains__(self, n):
        if n in self._nodes:
            return True

        return False


    # custom methods
    def add_nodes(self, *args):
        for v in args:
            if isinstance(v, GraphNode):
                self._nodes[v.get_id()] = v


    def create_node(self, n):
        if n not in self._nodes:
            self._nodes[n] = GraphNode(n)


    def remove_node(self, n):
        self._nodes.pop(n, None)


    def create_edge(self, n, d, *kwargs):
        if n in self._nodes and d in self._nodes:
            self._nodes[n].add_edge(d, *kwargs)


    def has_edge(self, n, d):
        if n in self._nodes and d in self._nodes:
            if d in self._nodes[n].get_edges():
                return True

        return False


    def dfs(self, n):
        pass


    def bfs(self, n):
        pass


    def primm(self, n):
        pass


    def kruskal(self, n):
        pass


    def dijkstra(self, n, d):
        pass


    def circuit(self):
        pass
