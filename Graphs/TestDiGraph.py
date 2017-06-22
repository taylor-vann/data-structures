
"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph structure unit tests

Requirements:
- GraphNode.py
- Graph.py
"""

import unittest
from GraphNode import GraphNode
from DiGraph import DiGraph


class testDiGraph(unittest.TestCase):

    def testDiGraphIsNotNull(self):
        self.assertIsNotNone(DiGraph)


    def testDiGraphAddGetNode(self):
        n = GraphNode("A")
        n.create_edge("B", weight = 10)
        m = GraphNode("B")
        m.create_edge("A", weight = 5)
        o = GraphNode("C")
        o.create_edge("A", weight = 3)

        g = DiGraph(n, m, o)

        self.assertTrue("B" in g)


    def testDiGraphContains(self):
        n = GraphNode("A")
        n.create_edge("B", weight = 10)
        m = GraphNode("B")
        m.create_edge("A", weight = 5)
        o = GraphNode("C")
        o.create_edge("A", weight = 3)

        g = DiGraph(n, m, o)

        self.assertTrue("B" in g)


    def testDiGraphNotContains(self):
        n = GraphNode("A")
        n.create_edge("B", weight = 10)
        m = GraphNode("B")
        m.create_edge("A", weight = 5)
        o = GraphNode("C")
        o.create_edge("A", weight = 3)

        g = DiGraph(n, m, o)

        self.assertTrue("D" not in g)


    def testDiGraphCreateNode(self):
        g = DiGraph()
        g.create_node("A")

        self.assertTrue("A" in g)


    def testDiGraphRemoveNode(self):
        g = DiGraph()
        g.create_node("A")
        g.remove_node("A")

        self.assertTrue("A" not in g)


    def testDiGraphAddNodeAddEdge(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_edge("A", "B")

        self.assertTrue(g.has_edge("A", "B"))


    def testDiGraphAddNodeRemoveEdge(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_edge("A", "B")
        g.remove_edge("A", "B")

        self.assertFalse(g.has_edge("A", "B"))


    def testDiGraphGetEdgeProperty(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_edge("A", "B", weight = 10)

        self.assertEqual(g.get_edge_property("A", "B", "weight"), 10)


    def testDiGraphDFS(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("A"), ["A", "B", "C"])


    def testDiGraphDFSOne(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("C"), ["C"])


    def testDiGraphDFSTwo(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("B"), ["B", "C"])


    def testDiGraphDFSFive(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_node("D")
        g.create_node("E")
        g.create_node("F")

        g.create_edge("A", "B")
        g.create_edge("A", "C")
        g.create_edge("B", "D")
        g.create_edge("B", "E")
        g.create_edge("D", "F")
        g.create_edge("E", "C")
        g.create_edge("F", "E")


        self.assertEqual(g.dfs("A"), ["A", "B", "D", "F", "E", "C"])


    def testDiGraphBFS(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("A"), ["A", "B", "C"])


    def testDiGraphBFSOne(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("C"), ["C"])


    def testDiGraphBFSTwo(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("B"), ["B", "C"])


    def testDiGraphBFSFive(self):
        g = DiGraph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_node("D")
        g.create_node("E")
        g.create_node("F")

        g.create_edge("A", "B")
        g.create_edge("A", "C")
        g.create_edge("B", "D")
        g.create_edge("B", "E")
        g.create_edge("D", "F")
        g.create_edge("E", "C")
        g.create_edge("F", "E")

        self.assertEqual(g.bfs("A"), ["A", "B", "C", "D", "E", "F"])





unittest.main()
