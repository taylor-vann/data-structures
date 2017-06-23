
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


    def testSetGetEdgeNone(self):
        n = GraphNode("I")
        n.create_edge("A", weight = 10)
        self.assertEqual(n.get_edge("B"), None)


    def testSetGetEdge(self):
        n = GraphNode("I")
        n.create_edge("A", weight = 10)
        self.assertEqual(n.get_edge("A"), {"weight": 10})

    def testSetEdgeEdgeWeightProperty(self):
        gn = GraphNode("B")
        gn.create_edge("A", weight = 10)
        self.assertEqual(gn.get_edge_property("A", "weight"), 10)


    def testAddMultipleEdgeProperty(self):
        gn = GraphNode("Q")

        gn.create_edge(dest = "A", weight = 10, directed = True, legacy = False)

        self.assertEqual(gn.get_edge_property("A", "directed"), True)


    def testGetEdgeProperties(self):
        gn = GraphNode("Q")

        gn.create_edge(
            dest = "A",
            weight = 10,
            directed = True,
            legacy = False)

        self.assertEqual(sorted(list(gn.get_edge_properties("A"))),
            sorted(["weight", "directed", "legacy"]))


    def testGetEdges(self):
        gn = GraphNode("Z")

        gn.create_edge(
            dest = "A",
            weight = 10,
            directed = True,
            legacy = False)

        gn.create_edge(
            dest = "B",
            weight = 5,
            directed = False,
            legacy = True)

        self.assertEqual(sorted(list(gn.get_edges())), ["A", "B"])


    def testRemoveEdge(self):
        gn = GraphNode("L")

        gn.create_edge(
            dest = "A",
            weight = 10,
            directed = True,
            legacy = False)

        gn.create_edge(
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

        gn.create_edge("B", "A", 10, directed = True, legacy = False)

        self.assertEqual(n["edges"]["B"]["legacy"], False)


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


    def testSetGetNodeProperty(self):
        gn = GraphNode("P")
        gn.set_node_properties(**{"happy": "yes"})
        self.assertEqual(gn.get_node_property("happy"), "yes")


    def testSetGetRemoveNodeProperty(self):
        gn = GraphNode("P")
        gn.set_node_properties(**{"happy": "yes"})
        gn.remove_node_property("happy")
        gn.remove_node_property("frowny")
        self.assertIsNone(gn.get_node_property("happy"))


    def testGetNodeProperties(self):
        gn = GraphNode("P")
        gn.set_node_properties(**{"happy": "yes"})
        gn.set_node_properties(**{"frowny": "maybe"})
        self.assertEqual(gn.get_node_properties(),
            ["edges", "frowny", "happy", "id", "self"])


    def testNotSetGetNodeProperty(self):
        gn = GraphNode("P")
        gn.set_node_properties(**{"happy": "yes"})
        self.assertIsNone(gn.get_node_property("frowny"))


    def testSetNodeData(self):
        gn = GraphNode("P")
        gn.set_node_properties(**{"happy": "yes"})
        self.assertIsNone(gn.get_node_property("frowny"))


unittest.main()
