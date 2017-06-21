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


    def __init__(self, nid, data = None):
        self._node = {
            "id": nid,
            "data": data,
            "edges": {},
            "self": self,
        }


    def add_edge(self, name, weight = None, **kwargs):
        self._node["edges"][name] = {"weight": weight}

        for v in kwargs:
            self._node["edges"][name][v] = kwargs[v]


    def get_edges(self):
        return self._node["edges"]


    def get_edge_property(self, k, p):
        if k in self._node["edges"] and p in self._node["edges"][k]:
            return self._node["edges"][k][p]

        return None


    def get_edge_properties(self, k):
        if k in self._node["edges"]:
            return self._node["edges"][k].keys()

        return None


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
