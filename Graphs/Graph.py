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

    _g = None

    # overridden
    def __init__(self, *args):
        self._g = {}

        self.add_g(*args)


    def __contains__(self, n):
        if n in self._g:
            return True

        return False


    # custom methods
    def add_g(self, *args):
        for v in args:
            if isinstance(v, GraphNode):
                self._g[v.get_id()] = v


    def create_node(self, n):
        if n not in self._g:
            self._g[n] = GraphNode(n)


    def remove_node(self, n):
        self._g.pop(n, None)


    def create_edge(self, n, d, *kwargs):
        if n in self._g and d in self._g:
            self._g[n].add_edge(d, *kwargs)


    def has_edge(self, n, d):
        if n in self._g and d in self._g:
            if d in self._g[n].get_edges():
                return True

        return False


    def dfs(self, n):
        if n not in self._g:
            return

        visited = {}
        order = []
        queue = [self._g[n].get_id()]

        while queue:
            current = queue.pop()

            if current not in visited:
                visited[current] = current
                order.append(current)
                tmp = reversed(sorted(self._g[current].get_edges()))
                queue.extend(tmp)

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
                print(current)
                visited[current] = current
                order.append(current)
                tmp = sorted(self._g[current].get_edges())
                queue.extend(tmp)

        return order


    def primm(self, n):
        pass


    def kruskal(self, n):
        pass


    def dijkstra(self, n, d):
        pass


    def circuit(self):
        pass
