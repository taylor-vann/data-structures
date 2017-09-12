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
    edges: {
        A: {
            # some attributes maybe
            destination: <node>
            weight: 10,
            directed: true,
            traveled: false,
        }
    },
    self: <reference to GraphNode self>
}
"""


class GraphNode(object):

    _node = None

    # overridden methods
    def __init__(self, n):
        self._node = {
            "id": n,
            "edges": {},
            "self": self,
        }


    def __contains__(self, n):
        if n in self._node["edges"]:
            return True

        return False


    # custom methods
    def create_edge(self, dest, **kwargs):
        self._node["edges"][dest] = {}

        for v in kwargs:
            self._node["edges"][dest][v] = kwargs[v]


    def remove_edge(self, dest):
        self._node["edges"].pop(dest, None)


    def get_edge(self, d):
        if d in self._node["edges"]:
            return self._node["edges"][d]


    def get_edges(self):
        return sorted(self._node["edges"])


    def get_edge_property(self, k, p):
        if k in self._node["edges"] and p in self._node["edges"][k]:
            return self._node["edges"][k][p]


    def get_edge_properties(self, k):
        if k in self._node["edges"]:
            return self._node["edges"][k].keys()


    def set_edge_properties(self, j, **kwargs):
        if j in self._node["edges"]:
            for k in kwargs:
                self._node["edges"][k] = kwargs[k]


    def set_id(self, n):
        self._node["id"] = n


    def get_id(self):
        return self._node["id"]


    def get_node_properties(self):
        return sorted(list(self._node.keys()))


    def get_node_property(self, p):
        if p in self._node:
            return self._node[p]


    def set_node_properties(self, **kwargs):
        for k in kwargs:
            if k != "id" and k != "edges" and k != "self":
                self._node[k] = kwargs[k]


    def remove_node_property(self, p):
        if p != "id" and p != "edges" and p!= "self":
            self._node.pop(p, None)


    def get_node(self):
        return self._node
