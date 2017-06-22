"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph data structure

Requirements:
- GraphNode.py


create graph from dictionary

{
    "A": {"B": {"weight": 10}
    "B": {"D": {"weight": 5}}
    "C": {"C": {"weight": 5}}
    "D": {"C": {"weight": 5}}
}
"""

from GraphNode import GraphNode
from PriorityQueue import PriorityQueue

class DiGraph (object):

    _g = None

    # overridden
    def __init__(self, *args):
        self._g = {}

        self.add_nodes(*args)


    def __contains__(self, n):
        if n in self._g:
            return True

        return False


    # custom methods
    def add_nodes(self, *args):
        for v in args:
            if isinstance(v, GraphNode):
                self._g[v.get_id()] = v


    def create_node(self, n, **kwargs):
        if n not in self._g:
            self._g[n] = GraphNode(n)
            self._g[n].set_node_properties(**kwargs)


    def remove_node(self, n):
        self._g.pop(n, None)


    def create_edge(self, n, d, **kwargs):
        if n in self._g and d in self._g:
            self._g[n].create_edge(d, **kwargs)


    def remove_edge(self, n, d):
        if n in self._g and d in self._g:
            self._g[n].remove_edge(d)


    def has_edge(self, n, d):
        if n in self._g and d in self._g:
            if d in self._g[n]:
                return True

        return False


    def get_node(self, n):
        if n in self._g:
            return self._g[n].get_node()


    def get_nodes(self):
        return self._g.keys()


    def get_edge_property(self, n, d, p):
        if self.has_edge(n, d):
            return self._g[n].get_edge_property(d, p)


    def dfs(self, n):
        if n not in self._g:
            return

        visited = {}
        order = []
        queue = [self._g[n].get_id()]

        while queue:
            current = queue.pop()

            if current not in visited:
                visited[current] = None
                order.append(current)
                queue.extend(reversed(sorted(self._g[current].get_edges())))

        return order


    def bfs(self, n):
        if n not in self._g:
            return

        visited = {}
        order = []
        queue = [self._g[n].get_id()]

        while queue:
            current = queue.pop(0)

            if current not in visited:
                visited[current] = None
                order.append(current)
                queue.extend(sorted(self._g[current].get_edges()))

        return order


    def dijkstra(self, n, d):
        pass


    def circuit(self):
        pass
