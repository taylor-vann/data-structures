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
            depart: B,
            arrive: A,
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
    def __init__(self, *vertices):
        self._cnt = 0
        self._g = { "vertices": {}, "edges": {}, "properties": {} }

        self.create_vertices(*vertices)


    def __contains__(self, n):
        if n in self._g["vertices"]:
            return True

        return False


    # custom methods
    def create_vertices(self, *vertices):
        for n in vertices:
            if n not in self._g["vertices"]:
                self._g["vertices"][n] = {}


    def remove_vertices(self, *vertices):
        for n in vertices:
            self._remove_node_edges(n)

            self._g["vertices"].pop(n, None)


    def create_edges(self, *args):
        for a in args:
            self.create_edge(a[0], a[1])


    def create_edge(self, d, a, **kwargs):
        self.create_vertices(d, a)
        self._create_edge_space(d, a)
        return self._create_edge_instance(d, a, **kwargs)


    def remove_edge(self, d, a, **kwargs):
        if d in self._g["vertices"] and a in self._g["vertices"][d]:
            if kwargs:
                # find by properties
                e = self._remove_edge_by_property(d, a, **kwargs)
                print(e)
                if e:
                    self.remove_edge_by_id(e)
                pass
            else:
                for i in self._g["vertices"][d][a]:
                    self._remove_edge_instance(d, a, i)
                    break

        self._remove_empty_sub_vertices(d, a)


    def remove_edge_by_id(self, i):
        if i in self._g["edges"]:
            d = self._g["edges"][i]["depart"]
            a = self._g["edges"][i]["arrive"]
            self._remove_edge_instance(d, a, i)
            self._remove_empty_sub_vertices(d, a)


    def set_node_properties(self, node, **kwargs):
        if node in self._g["vertices"]:
            for k in kwargs:
                if k != "edges":
                    self._g[node][k] = kwargs[k]


    def _create_edge_space(self, d, a):
        # create arrival list in departure list
        if a not in self._g["vertices"][d]:
            self._g["vertices"][d][a] = {}

        # create departure list in arrival list
        if d not in self._g["vertices"][a]:
            self._g["vertices"][a][d] = {}


    def _create_edge_instance(self, d, a, **kwargs):
        n = self._get_count()
        m = self._get_count()

        # create instances in vertex list
        self._g["edges"][n] = { "depart": d, "arrive": a, **kwargs }
        self._g["edges"][m] = { "depart": a, "arrive": d, **kwargs }

        # add instances to arrival and departure lists
        self._g["vertices"][d][a][n] = m
        self._g["vertices"][a][d][m] = n

        return n


    def _remove_empty_sub_vertices(self, d, a):
        if a in self._g["vertices"][d] and not self._g["vertices"][d][a]:
            self._g["vertices"][d].pop(a, None)

        if d in self._g["vertices"][a] and not self._g["vertices"][a][d]:
            self._g["vertices"][a].pop(d, None)


    def _remove_node_edges(self, node):
        for n in self._g["vertices"][node]:
            self._remove_edges(self._g["vertices"][n].pop(node, None))


    def _remove_edges(self, edges):
        if edges:
            for v in edges:
                self._g["edges"].pop(v, None)
                self._g["edges"].pop(edges[v], None)


    def _remove_edge_by_property(self, d, a, **kwargs):
        b = False

        return self._get_edge_by_property(d, a, **kwargs)


    def _get_edge_by_property(self, d, a, **kwargs):
        print("searching for ... ", d, a)
        b = False

        for n in self._g["vertices"][d][a]:
            for k in kwargs:
                if n in self._g["edges"] and k in self._g["edges"][n]:
                    if kwargs[k] == self._g["edges"][n][k]:
                        b = True
                else:
                    b = False
                    break

            if b == True:
                return n


    def _remove_edge_instance(self, d, a, i):
        e = self._g["vertices"][d][a].pop(i, None)
        #print(e)
        self._g["vertices"][a][d].pop(e, None)
        self._g["edges"].pop(i, None)
        self._g["edges"].pop(e, None)


    def _has_edge(self, d, a, i = None):
        if d in self._g["vertices"] and a in self._g["vertices"][d]:
            return True

        return False

    def _has_edge_by_id(self, i):
        if i and i in self._g["edges"]:
            return True

        return False


    def _get_count(self):
        self._cnt += 1
        return self._cnt - 1


########################################################

"""

    def remove_node_properties(self, n, **kwargs):
        if n in self._g:
            for k in kwargs:
                if k != "edges":
                    self._g[n].pop(k, None)


    def get_node_property(self, n, p):
        if n in self._g:
            if p in self._g[n]:
                return self._g[n][p]


#    def create_edges(self, n, *args):
#        if n in self._g:
#            for a in args:
#                    continue
#                if a in self._g:
#                    self._g[n]["edges"][a] = {}
#                    self._g[a]["edges"][n] = {}


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
"""
