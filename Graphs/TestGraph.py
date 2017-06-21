
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




unittest.main()
