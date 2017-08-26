"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- BaseGraph structure unit tests

Requirements:
- BaseGraph.py
- unittest
"""

import unittest
from BaseGraph import BaseGraph


class TestGraph(unittest.TestCase):

    def testBaseGraphNotNone(self):
        self.assertIsNotNone(BaseGraph)

    def testBGInstanceNotNone(self):
        bg = BaseGraph()
        self.assertIsNotNone(bg)

    def testBGInsertNodeOnInit(self):
        bg = BaseGraph("A", "B")
        self.assertTrue("A" in bg)

    def testBGInsertNode(self):
        bg = BaseGraph()
        bg.create_vertices("A", "B")
        self.assertTrue("A" in bg)

    def testBGRemoveNode(self):
        bg = BaseGraph()
        bg.create_vertices("A", "B")
        bg.remove_vertices("A")
        self.assertFalse("A" in bg)

    def testBGHasEdge(self):
        bg = BaseGraph()
        bg.create_vertices("A", "B")
        bg.create_edge("A", "B", **{"weight": 10})
        self.assertTrue(bg._has_edge("A", "B"))

    def testBGHasBackEdge(self):
        bg = BaseGraph()
        bg.create_vertices("A", "B")
        bg.create_edge("A", "B", **{"weight": 10})
        self.assertTrue(bg._has_edge("B", "A"))

    def testBGNoEdgeAfterRemoveNode(self):
        bg = BaseGraph()
        bg.create_vertices("A", "B", "C")
        bg.create_edge("A", "B", **{"weight": 5})
        bg.create_edge("A", "A", **{"weight": 10})
        bg.create_edge("B", "C", **{"weight": 15})
        bg.remove_vertices("B")
        self.assertFalse(bg._has_edge("B", "A"))


    def testBGCreateEdges(self):
        bg = BaseGraph()
        bg.create_edges(["A", "B"], ["B", "C"], ["C", "A"])
        bg.remove_edge("B", "C")
        self.assertFalse(bg._has_edge("B", "C"))


    def testBGNoEdgeAfterRemoveNode(self):
        bg = BaseGraph()
        bg.create_vertices("A", "B", "C")
        bg.create_edge("A", "B", **{"weight": 5})
        v = bg.create_edge("A", "A", **{"weight": 10})
        bg.create_edge("B", "C", **{"weight": 15})
        bg.remove_edge_by_id(v)
        self.assertFalse(bg._has_edge("A", "A"))


    def testBGRemoveEdgesByProperty(self):
        bg = BaseGraph()
        bg.create_edges(["A", "B"], ["C", "A"])
        bg.create_edge("B", "C", **{"weight": 10})
        bg.remove_edge("B", "C", **{"weight": 10})
        print(bg._g)

        self.assertFalse(bg._has_edge("B", "C"))

unittest.main()
