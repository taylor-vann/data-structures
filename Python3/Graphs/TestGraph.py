
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
from Graph import Graph


class TestGraph(unittest.TestCase):

    def testGraphIsNotNull(self):
        self.assertIsNotNone(Graph)

    def testGraphIsNotNone(self):
        g = Graph()
        self.assertIsNotNone(g)

    def testGInsertNodeOnInit(self):
        g = Graph("A", "B")
        self.assertTrue("A" in g)

    def testGInsertNode(self):
        g = Graph()
        g.create_vertices("A", "B")
        self.assertTrue("A" in g)

    def testGRemoveNode(self):
        g = Graph()
        g.create_vertices("A", "B")
        g.remove_vertices("A")
        self.assertFalse("A" in g)

    def testGHasEdge(self):
        g = Graph()
        g.create_vertices("A", "B")
        g.create_edge("A", "B", **{"weight": 10})
        self.assertTrue(g._has_edge("A", "B"))

    def testGHasBackEdge(self):
        g = Graph()
        g.create_vertices("A", "B")
        g.create_edge("A", "B", **{"weight": 10})
        self.assertTrue(g._has_edge("B", "A"))

    def testGOnlyOneEdge(self):
        g = Graph()
        g.create_vertices("A", "B")
        one = g.create_edge("A", "B", **{"weight": 10})
        two = g.create_edge("A", "B", **{"weight": 20})
        print(one, two)
        print(g._g)
        self.assertFalse(g._has_edge_by_id(one))


    def testGraphDFSOne(self):
        g = Graph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("C"), ["C", "B", "A"])


    def testGraphDFSTwo(self):
        g = Graph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.dfs("B"), ["B", "A", "C"])


    def testGraphDFSFive(self):
        g = Graph()
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
        g = Graph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("A"), ["A", "B", "C"])


    def testGraphBFSOne(self):
        g = Graph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("C"), ["C", "B", "A"])


    def testGraphBFSTwo(self):
        g = Graph()
        g.create_vertices("A")
        g.create_vertices("B")
        g.create_vertices("C")
        g.create_edge("A", "B")
        g.create_edge("B", "C")

        self.assertEqual(g.bfs("B"), ["B", "A", "C"])


    def testGraphBFSFive(self):
        g = Graph()
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


    def testBGShortestPathSameNode(self):
        g = Graph()

        g.create_vertices("A", "B", "C", "D", "E", "F")
        g.create_edge("A", "B", **{"weight": 5})
        g.create_edge("B", "D", **{"weight": 10})
        g.create_edge("B", "D", **{"weight": 15})
        g.create_edge("D", "F", **{"weight": 15})
        g.create_edge("E", "C", **{"weight": 20})
        g.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(g.get_shortest_path("A", "A", "weight"))


    def testBGShortestPathNodeNotInGraph(self):
        g = Graph()

        g.create_vertices("A", "B", "C", "D", "E", "F")
        g.create_edge("A", "B", **{"weight": 5})
        g.create_edge("B", "D", **{"weight": 10})
        g.create_edge("B", "D", **{"weight": 15})
        g.create_edge("D", "F", **{"weight": 15})
        g.create_edge("E", "C", **{"weight": 20})
        g.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(g.get_shortest_path("G", "A", "weight"))


    def testBGShortestPathDestinationNotInGraph(self):
        g = Graph()

        g.create_vertices("A", "B", "C", "D", "E", "F")
        g.create_edge("A", "B", **{"weight": 5})
        g.create_edge("B", "D", **{"weight": 10})
        g.create_edge("B", "D", **{"weight": 15})
        g.create_edge("D", "F", **{"weight": 15})
        g.create_edge("E", "C", **{"weight": 20})
        g.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(g.get_shortest_path("A", "G", "weight"))


    def testBGShortestPathSix(self):
        g = Graph()

        g.create_vertices("A", "B", "C", "D", "E", "F")
        g.create_edge("A", "B", **{"weight": 5})
        g.create_edge("B", "D", **{"weight": 10})
        g.create_edge("B", "D", **{"weight": 15})
        g.create_edge("D", "F", **{"weight": 15})
        g.create_edge("E", "C", **{"weight": 20})
        g.create_edge("F", "E", **{"weight": 25})
        rslt = { "path": ["A", "B", "D"], "distance": 20 }
        self.assertEqual(g.get_shortest_path("A", "D", "weight"), rslt)



    def testBGNoPropertyShortestPath(self):
        g = Graph()

        g.create_vertices("A", "B", "C", "D", "E", "F")
        g.create_edge("A", "B")
        g.create_edge("B", "D")
        g.create_edge("B", "D")
        g.create_edge("D", "F")
        g.create_edge("E", "C")
        g.create_edge("F", "E")
        rslt = { "distance": None, "path": ["A", "B", "D"] }
        self.assertEqual(g.get_shortest_path("A", "D"), rslt)


unittest.main()
