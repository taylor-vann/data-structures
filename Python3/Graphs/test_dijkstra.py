"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest

from base_graph import create_graph
from dijkstra import dijkstra


class TestGraph(unittest.TestCase):

    def test_dijkstra_not_none(self):
        self.assertIsNotNone(dijkstra)


    def test_dijkstra_simple_path(self):
        graph = create_graph(["A", "B"], [("A", "B", 10)])
        result = (10, ["A", "B"])

        self.assertEqual(result, dijkstra(graph, "A", "B"))


    def test_dijkstra_two_path(self):
        graph = create_graph(
            ["A", "B", "C"],
            [("A", "B", 10), ("A", "C", 10), ("B", "C", 10)])
        result = (10, ["A", "C"])

        self.assertEqual(result, dijkstra(graph, "A", "C"))


    def test_dijkstra_complicated(self):
        graph = create_graph(
            ["A", "B", "C", "D", "E", "F", "G"],
            [
                ("A", "B", 10),
                ("A", "C", 5),
                ("B", "C", 10),
                ("C", "D", 5),
                ("B", "D", 10),
                ("D", "E", 10),
                ("D", "F", 5),
                ("E", "G", 10),
                ("F", "G", 5)
            ]
        )
        result = (20, ["A", "C", "D", "F", "G"])

        self.assertEqual(result, dijkstra(graph, "A", "G"))

if __name__ == "__main__":
    unittest.main()
