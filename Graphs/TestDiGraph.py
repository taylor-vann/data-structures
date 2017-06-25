
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


    def testDiGraphRemoveNode(self):
        g = DiGraph()

        g.create_nodes("A")
        g.set_node_properties("A", data = "hello, world!")
        g.set_node_properties("A", legacy = False)
        g.remove_node_properties("A", "legacy")

        self.assertIsNone(g.get_node_property("A", "legacy"))


    def testDiGraphRemoveNodeFail(self):
        g = DiGraph()

        g.create_nodes("A")
        g.set_node_properties("A", data = "hello, world!")
        g.set_node_properties("A", legacy = False)
        g.remove_node_properties("A", "traversed")

        self.assertIsNone(g.get_node_property("A", "traversed"))


    def testDiGraphCreateEdge(self):
        g = DiGraph()

        g.create_nodes("A", "B")
        g.create_edges("A", "B", "C", "D")

        self.assertTrue(g.has_edge("A", "B"))


    def testDiGraphCreateEdgeNone(self):
        g = DiGraph()

        g.create_nodes("A", "B")
        g.create_edges("A", "A")

        self.assertFalse(g.has_edge("A", "A"))


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


    def testDiGraphDijkstraNone(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D", "E", "F")
        g.create_edges("A", "B", "C")
        g.create_edges("B", "D", "E")
        g.create_edges("D", "F")
        g.create_edges("E", "C")
        g.create_edges("F", "E")

        self.assertIsNone(g._dijkstra("A", "weight"))


    def testDiGraph_dijkstra(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D", "E", "F")
        g.create_edges("A", "B")
        g.set_edge_properties("A", "B", weight = 1)
        g.create_edges("B", "C")
        g.set_edge_properties("B", "C", weight = 2)
        g.create_edges("C", "D")
        g.set_edge_properties("C", "D", weight = 3)
        g.create_edges("D", "E")
        g.set_edge_properties("D", "E", weight = 4)
        g.create_edges("E", "F")
        g.set_edge_properties("E", "F", weight = 5)

        answer = {
            'D': {
                'parent': 'C',
                'weight': 3,
                'distance': 6
            },
            'B': {
                'parent': 'A',
                'weight': 1,
                'distance': 1
            },
            'E': {
                'parent': 'D',
                'weight': 4,
                'distance': 10
            },
            'F': {
                'parent': 'E',
                'weight': 5,
                'distance': 15
            },
            'C': {
                'parent': 'B',
                'weight': 2,
                'distance': 3
            }
        }

        self.assertEqual(g._dijkstra("A", "weight"), answer)


    def testDiGraphGetShortestPath(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D", "E", "F")
        g.create_edges("A", "B")
        g.set_edge_properties("A", "B", weight = 1)
        g.create_edges("B", "C")
        g.set_edge_properties("B", "C", weight = 2)
        g.create_edges("C", "D")
        g.set_edge_properties("C", "D", weight = 3)
        g.create_edges("D", "E")
        g.set_edge_properties("D", "E", weight = 4)
        g.create_edges("E", "F")
        g.set_edge_properties("E", "F", weight = 5)


        answer = {
            "path": ["A", "B", "C", "D"],
            "distance": 6
        }

        self.assertEqual(g.get_shortest_path("A", "D", "weight"), answer)


    def testDiGraphGetShortestPath(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D", "E", "F")
        g.create_edges("A", "B")
        g.set_edge_properties("A", "B", weight = 1)
        g.create_edges("B", "C")
        g.set_edge_properties("B", "C", weight = 2)
        g.create_edges("C", "D")
        g.set_edge_properties("C", "D", weight = 3)
        g.create_edges("D", "E")
        g.set_edge_properties("D", "E", weight = 4)
        g.create_edges("E", "F")
        g.set_edge_properties("E", "F", weight = 5)


        answer = {
            "path": ["A", "B", "C", "D"],
            "distance": 6
        }

        self.assertEqual(g.get_shortest_path("A", "D", "weight"), answer)


    def testDiGraphGetShortestPathNone(self):
        g = DiGraph()

        g.create_nodes("A", "B", "C", "D", "E", "F")
        g.create_edges("A", "B")
        g.set_edge_properties("A", "B", weight = 1)
        g.create_edges("B", "C")
        g.set_edge_properties("B", "C", weight = 2)
        g.create_edges("C", "D")
        g.set_edge_properties("C", "D", weight = 3)
        g.create_edges("D", "E")
        g.set_edge_properties("D", "E", weight = 4)
        g.create_edges("E", "F")
        g.set_edge_properties("E", "F", weight = 5)

        self.assertEqual(g.get_shortest_path("F", "A", "weight"), None)



unittest.main()
