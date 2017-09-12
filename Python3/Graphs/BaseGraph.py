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
    "A" = {
        "B" = {
            "100" = {
                "weight": 10,
                "return": "101"
            }
        }
    },

    "B" = {
        "A" = {
            "101" = {
                "weight": 10,
                "return": "100"
            }
        }
    }
}

or ...

graph = {

    vertices = {
        A = {
            B = {
                100: 101,
            }
        }

        B = {
            A = {
                101: 100,
            }
        }
    }

    edges = {
        100 = {
            start: A,
            destination: B,
            weight: 10,
        },

        101 = {
            _d: B,
            _a: A,
            weight: 10,
        }
    }

    properties = {
        A = {
            data: "yo, dawg"
        }

        B = {
            data: "what's good"
        }
    }
}
"""

from PriorityQueue import PriorityQueue


class BaseGraph(object):

    _g = None
    _cnt = None

    # overridden
    def __init__(self, *v):
        self._cnt = 0
        self._g = { "_v": {}, "_e": {}, "_p": {} }

        self.create_vertices(*v)


    def __contains__(self, n):
        if n in self._g["_v"]:
            return True

        return False


    # custom methods
    def create_vertices(self, *v):
        for n in v:
            if n not in self._g["_v"]:
                self._g["_v"][n] = {}


    def remove_vertices(self, *v):
        for n in v:
            self._remove_node_edges(n)

            self._g["_v"].pop(n, None)


    def create_edges(self, *args):
        for a in args:
            self.create_edge(a[0], a[1])


    def create_edge(self, d, a, **p):
        self.create_vertices(d, a)
        self._create_edge_space(d, a)
        return self._create_edge_instance(d, a, **p)


    def remove_edge(self, d, a, **p):
        if d in self._g["_v"] and a in self._g["_v"][d]:
            if p:
                e = self._get_edge_by_property(d, a, **p)

                if e:
                    self.remove_edge_by_id(e)
            else:
                for i in self._g["_v"][d][a]:
                    self._remove_edge_instance(d, a, i)
                    break

        self._remove_empty_sub_vertices(d, a)


    def remove_edge_by_id(self, i):
        if i in self._g["_e"]:
            d = self._g["_e"][i]["_d"]
            a = self._g["_e"][i]["_a"]
            self._remove_edge_instance(d, a, i)
            self._remove_empty_sub_vertices(d, a)


    def set_node_properties(self, node, **p):
        if node in self._g["_v"]:
            for k in p:
                if k != "edges":
                    self._g[node][k] = p[k]


    def _create_edge_space(self, d, a):
        # create arrival list in _dure list
        if a not in self._g["_v"][d]:
            self._g["_v"][d][a] = {}

        # create _dure list in arrival list
        if d not in self._g["_v"][a]:
            self._g["_v"][a][d] = {}


    def _create_edge_instance(self, d, a, **p):
        n = self._get_count()
        m = self._get_count()

        # create instances in edge list
        self._g["_e"][n] = { "_d": d, "_a": a, **p }
        self._g["_e"][m] = { "_d": a, "_a": d, **p }

        # add instances to _a and _d lists
        self._g["_v"][d][a][n] = m
        self._g["_v"][a][d][m] = n

        return n


    def _remove_empty_sub_vertices(self, d, a):
        if a in self._g["_v"][d] and not self._g["_v"][d][a]:
            self._g["_v"][d].pop(a, None)

        if d in self._g["_v"][a] and not self._g["_v"][a][d]:
            self._g["_v"][a].pop(d, None)


    def _remove_node_edges(self, node):
        for n in self._g["_v"][node]:
            self._remove_edges(self._g["_v"][n].pop(node, None))


    def _remove_edges(self, edges):
        if edges:
            for v in edges:
                self._g["_e"].pop(v, None)
                self._g["_e"].pop(edges[v], None)


    def _get_edge_by_property(self, d, a, **p):
        b = False

        for n in self._g["_v"][d][a]:
            for k in p:
                if n in self._g["_e"] and k in self._g["_e"][n]:
                    if p[k] == self._g["_e"][n][k]:
                        b = True
                else:
                    b = False
                    break

            if b == True:
                return n


    def _remove_edge_instance(self, d, a, i):
        e = self._g["_v"][d][a].pop(i, None)

        self._g["_v"][a][d].pop(e, None)
        self._g["_e"].pop(i, None)
        self._g["_e"].pop(e, None)


    def _has_edge(self, d, a):
        if d in self._g["_v"] and a in self._g["_v"][d]:
            return True

        return False

    def _has_edge_by_id(self, i):
        if i in self._g["_e"]:
            return True

        return False


    def _get_count(self):
        self._cnt += 1
        return self._cnt - 1


    def dfs(self, n):
        if n not in self._g["_v"]:
            return

        v = {}
        o = []
        q = [n]

        while q:
            c = q.pop()

            if c not in v:
                v[c] = None
                o.append(c)
                q.extend(reversed(sorted(self._g["_v"][c])))

        return o


    def bfs(self, n):
        if n not in self._g["_v"]:
            return

        v = {}
        o = []
        q = [n]

        while q:
            c = q.pop(0)

            if c not in v:
                v[c] = None
                o.append(c)
                q.extend(sorted(self._g["_v"][c]))

        return o


    def get_shortest_path(self, n, d, p = None):
        # if node or destination not in vertices, stop
        if n not in self._g["_v"] or d not in self._g["_v"]:
            return
        # if node equals destination, stop
        if n == d:
            return

        tp = "_weight"

        # if property is None, make one up and get sub graphs
        if p:
            sg = self._get_sub_graph(p)
        else:
            p = tp
            sg = self._get_sub_graph_no_property(p)

        # if d not in subgraph, stop
        if d not in sg:
            return

        # get shortest distance to relative nodes with dijkstra
        m = self._dijkstra(n, p, sg)
        l = m[d]

        # if no property, set distance to None
        if p == tp:
            o = { "distance": None, "path": [d] }
        else:
            o = { "distance": m[d]["_distance"], "path": [d] }

        # walk back and
        while l != n:
            l = m[d]["_parent"]
            d = l
            o["path"].insert(0, l)

        return o


    def _dijkstra(self, n, p, sg):
        if n not in sg:
            return

        pq = PriorityQueue()
        m = {}

        for v in sg:
            pq.push(v, float("inf"), parent = None)

        q = pq.remove(n)
        pq.push(q["data"], 0, parent = None)

        while len(pq) > 0:
            c = pq.pop()
            t = None

            for e, f in sg[c["data"]].items():
                t = pq.remove(e)

                if t != None and f[p] + c["weight"] < t["weight"]:
                    t["parent"] = c["data"]
                    t["weight"] = f[p] + c["weight"]

                    pq.push(t["data"], t["weight"], parent = c["data"])

                if t != None and t["parent"] != None:
                    m[t["data"]] = {
                        "_parent": t["parent"],
                        p: sg[t["parent"]][t["data"]][p],
                        "_distance": t["weight"]
                    }

        if m:
            return m


    def _get_sub_graph_no_property(self, p):
        sg = {}

        for i, j in self._g["_e"].items():
            if j["_d"] not in sg:
                sg[j["_d"]] = {}
            if j["_a"] == j["_d"]:
                continue
            if j["_a"] not in sg[j["_d"]]:
                sg[j["_d"]][j["_a"]] = { "edge": i, p: 1 }

        return sg


    def _get_sub_graph(self, p):
        sg = {}

        for i, j in self._g["_e"].items():
            if p in j:
                if j["_d"] not in sg:
                    sg[j["_d"]] = {}
                if j["_a"] == j["_d"]:
                    continue
                if j["_a"] not in sg[j["_d"]]:
                    sg[j["_d"]][j["_a"]] = { "edge": i, p: j[p] }
                elif self._g["_e"][i][p] > j[p]:
                    sg[j["_d"]][j["_a"]] = { "edge": i, p: j[p] }

        return sg
