
"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph structure unit tests

Requirements:
- GraphNode.py

"""

import unittest
from GraphNode import GraphNode


class TestGraphNode(unittest.TestCase):

    def testGraphNodeNotNull(self):
        self.assertIsNotNone(GraphNode)


    def testCreateNode(self):
        n = GraphNode("yo")
        self.assertIsInstance(n, GraphNode)


    def testId(self):
        n = GraphNode("N")
        self.assertEqual(n.get_id(), "N")


    def testSetGetDataNone(self):
        n = GraphNode("A")
        self.assertEqual(n.get_data(), None)


    def testSetGetData(self):
        n = GraphNode("A")
        s = "hello, world!"
        n.set_data(s)
        self.assertEqual(n.get_data(), s)


    def testSetGetEdgeNone(self):
        n = GraphNode("I")
        n.add_edge("A", weight = 10)
        self.assertEqual(n.get_edge("B"), None)


    def testSetGetEdge(self):
        n = GraphNode("I")
        n.add_edge("A", weight = 10)
        self.assertEqual(n.get_edge("A"), {"weight": 10})

    def testSetEdgeEdgeWeightProperty(self):
        gn = GraphNode("B")
        gn.add_edge("A", weight = 10)
        self.assertEqual(gn.get_edge_property("A", "weight"), 10)


    def testAddMultipleEdgeProperty(self):
        gn = GraphNode("Q")

        gn.add_edge(dest = "A", weight = 10, directed = True, legacy = False)

        self.assertEqual(gn.get_edge_property("A", "directed"), True)


    def testGetEdgeProperties(self):
        gn = GraphNode("Q")

        gn.add_edge(
            dest = "A",
            weight = 10,
            directed = True,
            legacy = False)

        self.assertEqual(list(gn.get_edge_properties("A")).sort(),
            ["weight", "directed", "legacy"].sort())


    def testGetEdges(self):
        gn = GraphNode("Z")

        gn.add_edge(
            dest = "A",
            weight = 10,
            directed = True,
            legacy = False)

        gn.add_edge(
            dest = "B",
            weight = 5,
            directed = False,
            legacy = True)

        self.assertEqual(sorted(list(gn.get_edges())), ["A", "B"])


    def testRemoveEdge(self):
        gn = GraphNode("L")

        gn.add_edge(
            dest = "A",
            weight = 10,
            directed = True,
            legacy = False)

        gn.add_edge(
            dest = "B",
            weight = 5,
            directed = False,
            legacy = True)

        gn.remove_edge("C")
        gn.remove_edge("B")

        self.assertEqual(sorted(list(gn.get_edges())), ["A"])


    def testGetNode(self):
        gn = GraphNode("P")
        n = gn.getNode()

        gn.add_edge("B", "A", 10, directed = True, legacy = False)

        self.assertEqual(n["edges"]["B"]["legacy"], False)


    def testGetNode(self):
        gn = GraphNode("P")
        n = gn.get_node()
        gn.add_edge("B", "A", 10, directed = True, legacy = False)

        gn.set_data("hello, world!")
        self.assertEqual(n["data"], "hello, world!")


    def testSetGetID(self):
        gn = GraphNode("P")
        self.assertEqual(gn.get_id(), "P")


    def testSetGetIDNode(self):
        gn = GraphNode("P")
        n = gn.get_node()
        gn.set_id("A")
        self.assertEqual(n["id"], "A")


    def testGetNode(self):
        gn = GraphNode("P")
        n = gn.get_node()
        self.assertEqual(n["self"], gn)


unittest.main()
