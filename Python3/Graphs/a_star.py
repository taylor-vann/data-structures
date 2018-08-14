"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

from queue import PriorityQueue

def a_star(graph, start, finish):
    pq = PriorityQueue()
    visited = {}
    path = []

    pq.put((0, start))

    while not pq.empty():
        weight, vertice = pq.get()

        if vertice is finish:
            break

        for dest, dist in graph[vertice]:
            total_dist = weight + dist

            if not dest in visited or total_dist < visited[dest][0]:
                visited[dest] = (total_dist, vertice)
                pq.put((total_dist, dest))

    if not finish in visited:
        return float("-inf"), []

    curr = finish

    while finish in visited and not curr is start:
        path.append(curr)
        curr = visited[curr][1]

    path.append(start)

    return visited[finish][0], list(reversed(path))
