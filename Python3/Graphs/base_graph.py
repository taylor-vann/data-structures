"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


"""
graphs are represented as a list of nodes and edges
edges can have weight

["A", "B", "C", "D", "E"]
[("A", "B", 10), ...]
"""

def create_graph(vertices, edges):
    graph = dict(zip(vertices, [[] for _ in vertices]))

    for edge in edges:
        graph[edge[0]].append(tuple(edge[1:]))

    return graph
