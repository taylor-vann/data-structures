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

        self.assertFalse(bg._has_edge("B", "C"))

    def testGraphDFS(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("A"), ["A", "B", "C"])


    def testGraphDFSOne(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("C"), ["C", "B", "A"])


    def testGraphDFSTwo(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("B"), ["B", "A", "C"])


    def testGraphDFSFive(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_vertices("D")
        g.create_vertices("E")
        g.create_vertices("F")

        g.create_edge("A", "B")
        g.create_edge("A", "C")
        g.create_edge("B", "D")
        g.create_edge("B", "E")
        g.create_edge("D", "F")
        g.create_edge("E", "C")
        g.create_edge("F", "E")

        self.assertEqual(g.dfs("A"), ["A", "B", "D", "F", "E", "C"])


    def testGraphBFS(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("A"), ["A", "B", "C"])


    def testGraphBFSOne(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("C"), ["C", "B", "A"])


    def testGraphBFSTwo(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("B"), ["B", "A", "C"])


    def testGraphBFSFive(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_vertices("D")
        g.create_vertices("E")
        g.create_vertices("F")

        g.create_edge("A", "B")
        g.create_edge("A", "C")
        g.create_edge("B", "D")
        g.create_edge("B", "E")
        g.create_edge("D", "F")
        g.create_edge("E", "C")
        g.create_edge("F", "E")

        self.assertEqual(g.bfs("A"), ["A", "B", "C", "D", "E", "F"])


    def testDiGraphDijkstraNone(self):
        g = BaseGraph()

        g.create_vertices("A", "B", "C", "D", "E", "F")
        g.create_edge("A", "B", **{"weight": 5})
        g.create_edge("B", "D", **{"weight": 10})
        g.create_edge("D", "F", **{"weight": 15})
        g.create_edge("E", "C", **{"weight": 20})
        g.create_edge("F", "E", **{"weight": 25})
        print(g._g)
        self.assertIsNone(g._dijkstra("A", "weight"))
    """
    def testPrim(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")

        g.create_edge("A", "B", weight = 10)

        g.prim("A", "weight")


    def testPrimNotInGraph(self):
        g = BaseGraph()
        g.create_vertices("A")
        g.create_vertices("B")

        g.create_edge("A", "B", weight = 10)

        self.assertIsNone(g.prim("C", "weight"))
    """
unittest.main()
