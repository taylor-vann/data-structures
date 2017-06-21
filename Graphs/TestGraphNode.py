
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
        self.assertEqual(n.getId(), "N")


    def testSetGetDataNone(self):
        n = GraphNode("A")
        self.assertEqual(n.getData(), None)


    def testSetGetData(self):
        n = GraphNode("A")
        s = "hello, world!"
        n.setData(s)
        self.assertEqual(n.getData(), s)


    def testSetEdgeEdgeWeightProperty(self):
        gn = GraphNode("B")
        name = "A"
        weight = 10
        gn.addEdge(name, weight)
        self.assertEqual(gn.getEdgeProperty(name, "weight"), 10)


    def testGetEdgeProperties(self):
        gn = GraphNode("Q")
        gn.addEdge(name = "A", weight = 10, directed = True, legacy = False)

        self.assertEqual(list(gn.getEdgeProperties("A")).sort(),
            ["weight", "directed", "legacy"].sort())


    def testAddMultipleEdgeProperties(self):
        gn = GraphNode("Q")
        gn.addEdge(name = "A", weight = 10, directed = True, legacy = False)
        self.assertEqual(gn.getEdgeProperty("A", "directed"), True)


    def testGetNode(self):
        gn = GraphNode("P")
        n = gn.getNode()
        gn.addEdge(name = "B", weight = 10, directed = True, legacy = False)
        self.assertEqual(n["edges"]["B"]["legacy"], False)


    def testGetNode(self):
        gn = GraphNode("P")
        n = gn.getNode()
        gn.addEdge(name = "B", weight = 10, directed = True, legacy = False)
        gn.setData("hello, world!")
        self.assertEqual(n["data"], "hello, world!")


unittest.main()
