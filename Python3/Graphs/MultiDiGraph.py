"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph data structure

Requirements:
- GraphNode.py
"""

from BaseGraph import BaseGraph


class MultiDiGraph(BaseGraph):

        def create_edge(self, d, a, **p):
            self.create_vertices(d, a)
            self._create_edge_space(d, a)
            return self._create_edge_instance(d, a, **p)


        def _create_edge_space(self, d, a):
            # create arrival list in _dure list
            if a not in self._g["_v"][d]:
                self._g["_v"][d][a] = {}


        def _create_edge_instance(self, d, a, **p):
            if a in self._g["_v"][d]:
                k = []
                for i in self._g["_v"][d][a].keys():
                    k.append(i)

                for j in k:
                    self.remove_edge_by_id(j)

            n = self._get_count()

            # create instances in edge list
            self._g["_e"][n] = { "_d": d, "_a": a, **p }

            # add instances to _a and _d lists
            self._create_edge_space(d, a)
            self._g["_v"][d][a][n] = None

            return n


        def _remove_edge_instance(self, d, a, i):
            e = self._g["_v"][d][a].pop(i, None)

            #self._g["_v"][a][d].pop(e, None)
            self._g["_e"].pop(i, None)
            #self._g["_e"].pop(e, None)
