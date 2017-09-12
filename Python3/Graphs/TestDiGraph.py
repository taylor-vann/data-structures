
"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- DiGraph structure unit tests

Requirements:
- DiGraphNode.py
- DiGraph.py
"""

import unittest
from DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def testDiGraphIsNotNull(self):
        self.assertIsNotNone(DiGraph)

    def testDiGraphIsNotNone(self):
        dg = DiGraph()
        self.assertIsNotNone(dg)

    def testGInsertNodeOnInit(self):
        dg = DiGraph("A", "B")
        self.assertTrue("A" in dg)

    def testGInsertNode(self):
        dg = DiGraph()
        dg.create_vertices("A", "B")
        self.assertTrue("A" in dg)

    def testGRemoveNode(self):
        dg = DiGraph()
        dg.create_vertices("A", "B")
        dg.remove_vertices("A")
        self.assertFalse("A" in dg)

    def testGHasEdge(self):
        dg = DiGraph()
        dg.create_vertices("A", "B")
        dg.create_edge("A", "B", **{"weight": 10})
        self.assertTrue(dg._has_edge("A", "B"))

    def testGHasBackEdge(self):
        dg = DiGraph()
        dg.create_vertices("A", "B")
        dg.create_edge("A", "B", **{"weight": 10})
        self.assertFalse(dg._has_edge("B", "A"))

    def testGOnlyOneEdge(self):
        dg = DiGraph()
        dg.create_vertices("A", "B")
        print(dg._g)
        one = dg.create_edge("A", "B", **{"weight": 10})
        print()
        print(dg._g)
        two = dg.create_edge("A", "B", **{"weight": 20})
        print()
        print(dg._g)
        self.assertFalse(dg._has_edge_by_id(one))


    def testDiGraphDFSOne(self):
        dg = DiGraph()
        dg.create_vertices("A")
        dg.create_vertices("B")
        dg.create_vertices("C")
        dg.create_edge("A", "B")
        dg.create_edge("B", "C")

        self.assertEqual(dg.dfs("C"), ["C"])


    def testDiGraphDFSTwo(self):
        dg = DiGraph()
        dg.create_vertices("A")
        dg.create_vertices("B")
        dg.create_vertices("C")
        dg.create_edge("A", "B")
        dg.create_edge("B", "C")

        self.assertEqual(dg.dfs("B"), ["B", "C"])


    def testDiGraphDFSFive(self):
        dg = DiGraph()
        dg.create_vertices("A")
        dg.create_vertices("B")
        dg.create_vertices("C")
        dg.create_vertices("D")
        dg.create_vertices("E")
        dg.create_vertices("F")

        dg.create_edge("A", "B")
        dg.create_edge("A", "C")
        dg.create_edge("B", "D")
        dg.create_edge("B", "E")
        dg.create_edge("D", "F")
        dg.create_edge("E", "C")
        dg.create_edge("F", "E")

        self.assertEqual(dg.dfs("A"), ["A", "B", "D", "F", "E", "C"])


    def testDiGraphBFS(self):
        dg = DiGraph()
        dg.create_vertices("A")
        dg.create_vertices("B")
        dg.create_vertices("C")
        dg.create_edge("A", "B")
        dg.create_edge("B", "C")

        self.assertEqual(dg.bfs("A"), ["A", "B", "C"])


    def testDiGraphBFSOne(self):
        dg = DiGraph()
        dg.create_vertices("A")
        dg.create_vertices("B")
        dg.create_vertices("C")
        dg.create_edge("B", "A")
        dg.create_edge("C", "B")

        self.assertEqual(dg.bfs("C"), ["C", "B", "A"])


    def testDiGraphBFSTwo(self):
        dg = DiGraph()
        dg.create_vertices("A")
        dg.create_vertices("B")
        dg.create_vertices("C")
        dg.create_edge("A", "B")
        dg.create_edge("B", "C")

        self.assertEqual(dg.bfs("B"), ["B", "C"])


    def testDiGraphBFSFive(self):
        dg = DiGraph()
        dg.create_vertices("A")
        dg.create_vertices("B")
        dg.create_vertices("C")
        dg.create_vertices("D")
        dg.create_vertices("E")
        dg.create_vertices("F")

        dg.create_edge("A", "B")
        dg.create_edge("A", "C")
        dg.create_edge("B", "D")
        dg.create_edge("B", "E")
        dg.create_edge("D", "F")
        dg.create_edge("E", "C")
        dg.create_edge("F", "E")

        self.assertEqual(dg.bfs("A"), ["A", "B", "C", "D", "E", "F"])


    def testBGShortestPathSameNode(self):
        dg = DiGraph()

        dg.create_vertices("A", "B", "C", "D", "E", "F")
        dg.create_edge("A", "B", **{"weight": 5})
        dg.create_edge("B", "D", **{"weight": 10})
        dg.create_edge("B", "D", **{"weight": 15})
        dg.create_edge("D", "F", **{"weight": 15})
        dg.create_edge("E", "C", **{"weight": 20})
        dg.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(dg.get_shortest_path("A", "A", "weight"))


    def testBGShortestPathNodeNotInDiGraph(self):
        dg = DiGraph()

        dg.create_vertices("A", "B", "C", "D", "E", "F")
        dg.create_edge("A", "B", **{"weight": 5})
        dg.create_edge("B", "D", **{"weight": 10})
        dg.create_edge("B", "D", **{"weight": 15})
        dg.create_edge("D", "F", **{"weight": 15})
        dg.create_edge("E", "C", **{"weight": 20})
        dg.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(dg.get_shortest_path("G", "A", "weight"))


    def testBGShortestPathDestinationNotInDiGraph(self):
        dg = DiGraph()

        dg.create_vertices("A", "B", "C", "D", "E", "F")
        dg.create_edge("A", "B", **{"weight": 5})
        dg.create_edge("B", "D", **{"weight": 10})
        dg.create_edge("B", "D", **{"weight": 15})
        dg.create_edge("D", "F", **{"weight": 15})
        dg.create_edge("E", "C", **{"weight": 20})
        dg.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(dg.get_shortest_path("A", "G", "weight"))


    def testBGShortestPathSix(self):
        dg = DiGraph()

        dg.create_vertices("A", "B", "C", "D", "E", "F")
        dg.create_edge("A", "B", **{"weight": 5})
        dg.create_edge("B", "D", **{"weight": 10})
        dg.create_edge("B", "D", **{"weight": 15})
        dg.create_edge("D", "F", **{"weight": 15})
        dg.create_edge("E", "C", **{"weight": 20})
        dg.create_edge("F", "E", **{"weight": 25})
        rslt = { "path": ["A", "B", "D"], "distance": 20 }
        self.assertEqual(dg.get_shortest_path("A", "D", "weight"), rslt)



    def testBGNoPropertyShortestPath(self):
        dg = DiGraph()

        dg.create_vertices("A", "B", "C", "D", "E", "F")
        dg.create_edge("A", "B")
        dg.create_edge("B", "D")
        dg.create_edge("B", "D")
        dg.create_edge("D", "F")
        dg.create_edge("E", "C")
        dg.create_edge("F", "E")
        rslt = { "distance": None, "path": ["A", "B", "D"] }
        self.assertEqual(dg.get_shortest_path("A", "D"), rslt)


unittest.main()
