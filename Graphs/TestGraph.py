
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
from Graph import Graph


class TestGraph(unittest.TestCase):

    def testGraphIsNotNull(self):
        self.assertIsNotNone(Graph)


    def testGraphAddGetNode(self):
        n = GraphNode("A")
        n.add_edge("B", weight = 10)
        m = GraphNode("B")
        m.add_edge("A", weight = 5)
        o = GraphNode("C")
        o.add_edge("A", weight = 3)

        g = Graph(n, m, o)

        self.assertTrue("B" in g)


    def testGraphContains(self):
        n = GraphNode("A")
        n.add_edge("B", weight = 10)
        m = GraphNode("B")
        m.add_edge("A", weight = 5)
        o = GraphNode("C")
        o.add_edge("A", weight = 3)

        g = Graph(n, m, o)

        self.assertTrue("B" in g)


    def testGraphNotContains(self):
        n = GraphNode("A")
        n.add_edge("B", weight = 10)
        m = GraphNode("B")
        m.add_edge("A", weight = 5)
        o = GraphNode("C")
        o.add_edge("A", weight = 3)

        g = Graph(n, m, o)

        self.assertTrue("D" not in g)


    def testGraphCreateNode(self):
        g = Graph()
        g.create_node("A")

        self.assertTrue("A" in g)


    def testGraphRemoveNode(self):
        g = Graph()
        g.create_node("A")
        g.remove_node("A")

        self.assertTrue("A" not in g)


    def testGraphAddNodeAddEdge(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_edge("A", "B")

        self.assertTrue(g.has_edge("A", "B"))


    def testGraphAddNodeRemoveEdge(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_edge("A", "B")
        g.remove_edge("A", "B")

        self.assertFalse(g.has_edge("A", "B"))


    def testGraphGetEdgeProperty(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_edge("A", "B", weight = 10)

        self.assertEqual(g.get_edge_property("A", "B", "weight"), 10)


    def testGraphDFS(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("A"), ["A", "B", "C"])


    def testGraphDFSOne(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("C"), ["C"])


    def testGraphDFSTwo(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("B"), ["B", "C"])


    def testGraphDFSFive(self):
        g = Graph()
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


    def testGraphBFS(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("A"), ["A", "B", "C"])


    def testGraphBFSOne(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("C"), ["C"])


    def testGraphBFSTwo(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")
        g.create_node("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("B"), ["B", "C"])


    def testGraphBFSFive(self):
        g = Graph()
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


    def testPrim(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")

        g.create_edge("A", "B", weight = 10)

        g.prim("A", "weight")

    def testPrimNotInGraph(self):
        g = Graph()
        g.create_node("A")
        g.create_node("B")

        g.create_edge("A", "B", weight = 10)

        self.assertIsNone(g.prim("C", "weight"))

unittest.main()
