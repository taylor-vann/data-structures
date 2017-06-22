
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
        g = DiGraph()

        g.create_nodes("A", "B", "C")

        self.assertTrue("B" in g)


    def testDiGraphAddGetNotNode(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")

        self.assertFalse("D" in g)


    def testDiGraphRemoveNode(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")
        g.remove_nodes("A", "D")

        self.assertFalse("A" in g)


    def testDiGraphHasProperty(self):
        g = DiGraph()

        g.create_nodes("A")
        g.set_node_properties("A", data = "hello, world!")

        self.assertEqual(g.get_node_property("A", "data"), "hello, world!")


    def testDiGraphCreateEdge(self):
        g = DiGraph()

        g.create_nodes("A", "B")
        g.create_edges("A", "B", "C", "D")

        self.assertTrue(g.has_edge("A", "B"))


    def testDiGraphCreateNoEdge(self):
        g = DiGraph()

        g.create_nodes("A", "B")
        g.create_edges("A", "B", "C", "D")

        self.assertFalse(g.has_edge("B", "A"))


    def testDiGraphRemoveEdges(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D")
        g.create_edges("A", "B", "C")
        g.create_edges("B", "C", "D")
        g.create_edges("C", "D", "A")

        g.remove_edges("A", "B", "C")

        self.assertFalse(g.has_edge("A", "C"))


    def testDiGraphCreateEdgeProperty(self):
        g = DiGraph()

        g.create_nodes("A", "B")
        g.create_edges("A", "B", "C", "D")
        g.set_edge_properties("A", "B", weight = 10)

        self.assertEqual(g.get_edge_property("A", "B", "weight"), 10)


    def testDiGraphDFS(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")
        g.create_edges("A", "B")
        g.create_edges("B", "C")

        self.assertEqual(g.dfs("A"), ["A", "B", "C"])


    def testDiGraphDFSNone(self):
        g = DiGraph()

        self.assertIsNone(g.dfs("A"))


    def testDiGraphDFSOne(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")
        g.create_edges("A", "B")
        g.create_edges("B", "C")

        self.assertEqual(g.dfs("C"), ["C"])


    def testDiGraphDFSTwo(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")
        g.create_edges("A", "B")
        g.create_edges("B", "C")

        self.assertEqual(g.dfs("B"), ["B", "C"])


    def testDiGraphDFSFive(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D", "E", "F")
        g.create_edges("A", "B", "C")
        g.create_edges("B", "D", "E")
        g.create_edges("D", "F")
        g.create_edges("E", "C")
        g.create_edges("F", "E")

        self.assertEqual(g.dfs("A"), ["A", "B", "D", "F", "E", "C"])


    def testDiGraphBFS(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")
        g.create_edges("A", "B")
        g.create_edges("B", "C")

        self.assertEqual(g.bfs("A"), ["A", "B", "C"])


    def testDiGraphBFSNone(self):
        g = DiGraph()

        self.assertIsNone(g.bfs("A"))


    def testDiGraphBFSOne(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")
        g.create_edges("A", "B")
        g.create_edges("B", "C")

        self.assertEqual(g.bfs("C"), ["C"])


    def testDiGraphBFSTwo(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C")
        g.create_edges("A", "B")
        g.create_edges("B", "C")

        self.assertEqual(g.bfs("B"), ["B", "C"])


    def testDiGraphBFSFive(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D", "E", "F")
        g.create_edges("A", "B", "C")
        g.create_edges("B", "D", "E")
        g.create_edges("D", "F")
        g.create_edges("E", "C")
        g.create_edges("F", "E")

        self.assertEqual(g.bfs("A"), ["A", "B", "C", "D", "E", "F"])




unittest.main()
