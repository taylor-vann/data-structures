"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

from queue import PriorityQueue


def dijkstra(graph, start, finish):
    pq = PriorityQueue()

    for vertice in graph.keys():
        pq.put(float("-inf"), vertice)
