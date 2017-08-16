"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph data structure

Requirements:
- PriorityQueue.py
"""

"""
graph = {
    "A": {
        "B": {
            "100": {
                "weight": 10,
            }

        }
    },

    "B": {
        "A": {
            "100": {
                "weight": 10,
            }
        }
    }
}
"""

from PriorityQueue import PriorityQueue


class BaseGraph(object):

    _g = None

    # overridden
    def __init__(self):
        self._g = {}


    def __contains__(self, n):
        if n in self._g:
            return True

        return False


    # custom methods
    def create_nodes(self, *args):
        for a in args:
            if a not in self._g:
                self._g[a] = {"edges": {}}


    def remove_nodes(self, *args):
        for a in args:
            for k in self._g:
                self._g[k]["edges"].pop(a, None)

            self._g.pop(a, None)


    def set_node_properties(self, n, **kwargs):
        if n in self._g:
            for k in kwargs:
                if k != "edges":
                    self._g[n][k] = kwargs[k]


    def remove_node_properties(self, n, **kwargs):
        if n in self._g:
            for k in kwargs:
                if k != "edges":
                    self._g[n].pop(k, None)


    def get_node_property(self, n, p):
        if n in self._g:
            if p in self._g[n]:
                return self._g[n][p]


    def create_edges(self, n, *args):
        if n in self._g:
            for a in args:
                if n == a:
                    continue
                if a in self._g:
                    self._g[n]["edges"][a] = {}
                    self._g[a]["edges"][n] = {}


    def remove_edges(self, n, *args):
        if n in self._g:
            for a in args:
                if a in self._g:
                    self._g[n]["edges"].pop(a, None)
                    self._g[a]["edges"].pop(n, None)


    def set_edge_properties(self, n, d, **kwargs):
        if n in self._g and d in self._g:
            if d in self._g[n]["edges"]:
                for k in kwargs:
                    self._g[n]["edges"][d][k] = kwargs[k]
                    self._g[d]["edges"][n][k] = kwargs[k]



    def get_edge_property(self, n, d, p):
        if n in self._g:
            if d in self._g[n]["edges"]:
                if p in self._g[n]["edges"][d]:
                    return self._g[n]["edges"][d][p]


    def has_edge(self, n, d):
        if n in self._g and d in self._g:
            if d in self._g[n]["edges"]:
                return True


    def dfs(self, n):
        if n not in self._g:
            return

        v = {}
        o = []
        q = [n]

        while q:
            c = q.pop()

            if c not in v:
                v[c] = None
                o.append(c)
                q.extend(reversed(sorted(self._g[c]["edges"].keys())))

        return o


    def bfs(self, n):
        if n not in self._g:
            return

        v = {}
        o = []
        q = [n]

        while q:
            c = q.pop(0)

            if c not in v:
                v[c] = None
                o.append(c)
                q.extend(sorted(self._g[c]["edges"].keys()))

        return o


    def get_shortest_path(self, n, d, p):
        if n == d:
            return

        m = self._dijkstra(n, p)

        if d not in m:
            return

        l = m[d]
        o = {
            "distance": m[d]["distance"],
            "path": [d],
        }

        while l != n:
            l = m[d]["parent"]
            d = l
            o["path"].insert(0, l)

        return o


    def _dijkstra(self, n, p):
        if n not in self._g:
            return

        pq = PriorityQueue()
        m = {}

        for k in self._g:
            pq.push(k, float("inf"), parent = None)

        pq.remove(n)
        pq.push(n, 0)

        while len(pq) > 0:
            c = pq.pop()
            e = self._g[c["data"]]["edges"]
            t = None

            for v in e:
                t = pq.remove(v)

                if p not in e[v]:
                    t = None
                    continue

                if t != None and e[v][p] < t["weight"]:
                    t["parent"] = c["data"]
                    t["weight"] = e[v][p] + c["weight"]
                    pq.push(t["data"], t["weight"], parent = t["parent"])

            if t != None and t["parent"] != None:
                m[t["data"]] = {
                    "parent": t["parent"],
                    "weight": self._g[t["parent"]]["edges"][t["data"]]["weight"],
                    "distance": t["weight"]
                }

        if m:
            return m
