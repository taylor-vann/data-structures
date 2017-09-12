
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
from MultiDiGraph import MultiDiGraph


class TestMultiDiGraph(unittest.TestCase):

    def testMDGIsNotNull(self):
        self.assertIsNotNone(DiGraph)

    def testMDGIsNotNone(self):
        mdg = MultiDiGraph()
        self.assertIsNotNone(dg)

    def testGInsertNodeOnInit(self):
        mdg = DiGraph("A", "B")
        self.assertTrue("A" in dg)

    def testGInsertNode(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A", "B")
        self.assertTrue("A" in dg)

    def testGRemoveNode(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A", "B")
        mdg.remove_vertices("A")
        self.assertFalse("A" in dg)

    def testGHasEdge(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A", "B")
        mdg.create_edge("A", "B", **{"weight": 10})
        self.assertTrue(mdg._has_edge("A", "B"))

    def testGHasBackEdge(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A", "B")
        mdg.create_edge("A", "B", **{"weight": 10})
        self.assertFalse(mdg._has_edge("B", "A"))

    def testGOnlyOneEdge(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A", "B")
        one = mdg.create_edge("A", "B", **{"weight": 10})
        two = mdg.create_edge("A", "B", **{"weight": 20})
        print(one, two)
        print(mdg._g)
        self.assertFalse(mdg._has_edge_by_id(one))


    def testMDGDFSOne(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A")
        mdg.create_vertices("B")
        mdg.create_vertices("C")
        mdg.create_edge("A", "B")
        mdg.create_edge("B", "C")

        self.assertEqual(mdg.dfs("C"), ["C"])


    def testMDGDFSTwo(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A")
        mdg.create_vertices("B")
        mdg.create_vertices("C")
        mdg.create_edge("A", "B")
        mdg.create_edge("B", "C")

        self.assertEqual(mdg.dfs("B"), ["B", "C"])


    def testMDGDFSFive(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A")
        mdg.create_vertices("B")
        mdg.create_vertices("C")
        mdg.create_vertices("D")
        mdg.create_vertices("E")
        mdg.create_vertices("F")

        mdg.create_edge("A", "B")
        mdg.create_edge("A", "C")
        mdg.create_edge("B", "D")
        mdg.create_edge("B", "E")
        mdg.create_edge("D", "F")
        mdg.create_edge("E", "C")
        mdg.create_edge("F", "E")

        self.assertEqual(mdg.dfs("A"), ["A", "B", "D", "F", "E", "C"])


    def testMDGBFS(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A")
        mdg.create_vertices("B")
        mdg.create_vertices("C")
        mdg.create_edge("A", "B")
        mdg.create_edge("B", "C")

        self.assertEqual(mdg.bfs("A"), ["A", "B", "C"])


    def testMDGBFSOne(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A")
        mdg.create_vertices("B")
        mdg.create_vertices("C")
        mdg.create_edge("B", "A")
        mdg.create_edge("C", "B")

        self.assertEqual(mdg.bfs("C"), ["C", "B", "A"])


    def testMDGBFSTwo(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A")
        mdg.create_vertices("B")
        mdg.create_vertices("C")
        mdg.create_edge("A", "B")
        mdg.create_edge("B", "C")

        self.assertEqual(mdg.bfs("B"), ["B", "C"])


    def testMDGBFSFive(self):
        mdg = MultiDiGraph()
        mdg.create_vertices("A")
        mdg.create_vertices("B")
        mdg.create_vertices("C")
        mdg.create_vertices("D")
        mdg.create_vertices("E")
        mdg.create_vertices("F")

        mdg.create_edge("A", "B")
        mdg.create_edge("A", "C")
        mdg.create_edge("B", "D")
        mdg.create_edge("B", "E")
        mdg.create_edge("D", "F")
        mdg.create_edge("E", "C")
        mdg.create_edge("F", "E")

        self.assertEqual(mdg.bfs("A"), ["A", "B", "C", "D", "E", "F"])


    def testBGShortestPathSameNode(self):
        mdg = MultiDiGraph()

        mdg.create_vertices("A", "B", "C", "D", "E", "F")
        mdg.create_edge("A", "B", **{"weight": 5})
        mdg.create_edge("B", "D", **{"weight": 10})
        mdg.create_edge("B", "D", **{"weight": 15})
        mdg.create_edge("D", "F", **{"weight": 15})
        mdg.create_edge("E", "C", **{"weight": 20})
        mdg.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(mdg.get_shortest_path("A", "A", "weight"))


    def testBGShortestPathNodeNotInDiGraph(self):
        mdg = MultiDiGraph()

        mdg.create_vertices("A", "B", "C", "D", "E", "F")
        mdg.create_edge("A", "B", **{"weight": 5})
        mdg.create_edge("B", "D", **{"weight": 10})
        mdg.create_edge("B", "D", **{"weight": 15})
        mdg.create_edge("D", "F", **{"weight": 15})
        mdg.create_edge("E", "C", **{"weight": 20})
        mdg.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(mdg.get_shortest_path("G", "A", "weight"))


    def testBGShortestPathDestinationNotInDiGraph(self):
        mdg = MultiDiGraph()

        mdg.create_vertices("A", "B", "C", "D", "E", "F")
        mdg.create_edge("A", "B", **{"weight": 5})
        mdg.create_edge("B", "D", **{"weight": 10})
        mdg.create_edge("B", "D", **{"weight": 15})
        mdg.create_edge("D", "F", **{"weight": 15})
        mdg.create_edge("E", "C", **{"weight": 20})
        mdg.create_edge("F", "E", **{"weight": 25})

        self.assertIsNone(mdg.get_shortest_path("A", "G", "weight"))


    def testBGShortestPathSix(self):
        mdg = MultiDiGraph()

        mdg.create_vertices("A", "B", "C", "D", "E", "F")
        mdg.create_edge("A", "B", **{"weight": 5})
        mdg.create_edge("B", "D", **{"weight": 10})
        mdg.create_edge("B", "D", **{"weight": 15})
        mdg.create_edge("D", "F", **{"weight": 15})
        mdg.create_edge("E", "C", **{"weight": 20})
        mdg.create_edge("F", "E", **{"weight": 25})
        rslt = { "path": ["A", "B", "D"], "distance": 20 }
        self.assertEqual(mdg.get_shortest_path("A", "D", "weight"), rslt)



    def testBGNoPropertyShortestPath(self):
        mdg = MultiDiGraph()

        mdg.create_vertices("A", "B", "C", "D", "E", "F")
        mdg.create_edge("A", "B")
        mdg.create_edge("B", "D")
        mdg.create_edge("B", "D")
        mdg.create_edge("D", "F")
        mdg.create_edge("E", "C")
        mdg.create_edge("F", "E")
        rslt = { "distance": None, "path": ["A", "B", "D"] }
        self.assertEqual(mdg.get_shortest_path("A", "D"), rslt)


unittest.main()
