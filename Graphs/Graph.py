"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph data structure

Requirements:
- GraphNode.py
"""

from BaseGraph import BaseGraph

class Graph(BaseGraph):

    def _create_edge_instance(self, d, a, **p):
        if a in self._g["_v"][d]:
            k = []
            for i in self._g["_v"][d][a].keys():
                k.append(i)

            for j in k:
                self.remove_edge_by_id(j)

        n = self._get_count()
        m = self._get_count()

        # create instances in edge list
        self._g["_e"][n] = { "_d": d, "_a": a, **p }
        self._g["_e"][m] = { "_d": a, "_a": d, **p }

        # add instances to _a and _d lists
        self._create_edge_space(a, d)
        self._create_edge_space(d, a)

        self._g["_v"][d][a][n] = m
        self._g["_v"][a][d][m] = n

        return n
