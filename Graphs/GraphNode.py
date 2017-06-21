"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph Node for Graphs.py

Requirements:
- None
"""

"""
{
    id: name,
    data: stuff,
    edges: {
        A: {
            weight: 10,
            directed: true,
            traveled: false,
        }
    }
}

"""


class GraphNode(object):

    _node = None
    _id = None
    _edges = None
    _data = None


    def __init__(self, nid, data = None):
        self._id = nid
        self._data = data
        self._edges = {}

        self._node = {
            "id": nid,
            "data": data,
            "edges": {},
        }


    def getId(self):
        return self._id


    def addEdge(self, name, weight = None, **kwargs):
        self._node["edges"][name] = { "weight": weight}

        for v in kwargs:
            self._node["edges"][name][v] = kwargs[v]


    def getEdges(self):
        return self._node["edges"].keys()


    def getEdgeProperty(self, k, p):
        if k in self._node["edges"] and p in self._node["edges"][k]:
            return self._node["edges"][k][p]

        return None


    def getEdgeProperties(self, k):
        if k in self._node["edges"]:
            return self._node["edges"][k].keys()

        return None


    def setData(self, d):
        self._data = d
        self._node["data"] = self._data


    def getData(self):
        return self._data


    def getNode(self):
        return self._node
