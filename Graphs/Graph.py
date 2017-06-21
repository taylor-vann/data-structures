"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph structure unit tests

Requirements:
- Graph.py
"""


class Graph (object):

    _nodes = {}


    def __init__(self, *args):
        for var in args:
            self.addNode(var)
