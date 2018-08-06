"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

from queue import PriorityQueue


def bellman_ford(graph, start):
    pq = PriorityQueue()
    visited = {}
    path = []

    pq.put((0, start))

    while not pq.empty():
        weight, vertice = pq.get()

        for dest, dist in graph[vertice]:
            total_dist = weight + dist

            if not dest in visited or total_dist < visited[dest][0]:
                visited[dest] = (total_dist, vertice)
                pq.put((total_dist, dest))

    return visited
