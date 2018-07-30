"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from base_graph import create_graph


class TestGraph(unittest.TestCase):

    def test_base_graph_not_none(self):
        self.assertIsNotNone(create_graph)


    def test_base_graph_returns_dictionary(self):
        self.assertIsInstance(create_graph([], []), dict)

    def test_base_graph_returns_correct_one(self):
        result = {
            "A": [("B", 10)],
            "B": []
        }

        vertices = ["A", "B"]
        edges = [("A", "B", 10)]

        self.assertEqual(create_graph(vertices, edges), result)

    def test_base_graph_returns_larger_set(self):
        result = {
            "A": [("B", 10), ("D", 5)],
            "B": [("C", 20)],
            "C": [],
            "D": [("B", 3)]
        }

        vertices = ["A", "B", "C", "D"]
        edges = [("A", "B", 10), ("A", "D", 5), ("B", "C", 20), ("D", "B", 3)]

        self.assertEqual(create_graph(vertices, edges), result)

if __name__ == "__main__":
    unittest.main()
