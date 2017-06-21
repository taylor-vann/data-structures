"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph Node for Graphs.py

Requirements:
- None
"""

"""
Graph Nodes will be represented in a dictionary.
When the dictionary is updated, the change will be reflected
in all references to the node and in other dictionaries.
Helps with threads and concurrent writes.
(Benefit of pass by reference)

{
    id: name,
    data: stuff,
    edges: {
        A: {
            # some attributes maybe
            destination: <node>
            weight: 10,
            directed: true,
            traveled: false,
        }
    },
    self: <reference to GraphNode>
}
"""


class GraphNode(object):

    _node = None

    # overridden methods
    def __init__(self, n, d = None):
        self._node = {
            "id": n,
            "data": d,
            "edges": {},
            "self": self,
        }


    def __contains__(self, n):
        if n in self._nodes["edges"]:
            return True

        return False


    # custom methods
    def add_edge(self, dest, **kwargs):
        self._node["edges"][dest] = {}

        for v in kwargs:
            self._node["edges"][dest][v] = kwargs[v]


    def remove_edge(self, dest):
        self._node["edges"].pop(dest, None)


    def get_edge(self, d):
        if d in self._node["edges"]:
            return self._node["edges"][d]


    def get_edges(self):
        return self._node["edges"]


    def get_edge_property(self, k, p):
        if k in self._node["edges"] and p in self._node["edges"][k]:
            return self._node["edges"][k][p]


    def get_edge_properties(self, k):
        if k in self._node["edges"]:
            return sorted(self._node["edges"][k].keys())


    def set_id(self, n):
        self._node["id"] = n


    def get_id(self):
        return self._node["id"]


    def set_data(self, d):
        self._node["data"] = d


    def get_data(self):
        return self._node["data"]


    def get_node(self):
        return self._node
