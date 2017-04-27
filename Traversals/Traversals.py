"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Traversal algorithms for trees and graphs
- Pre Order, Post Order, In Order, Level

Requirements:
- BSTree.py
- BSTNode.py
- AVLTree.py
- AVLNode.py
- Graphs.py
"""


def level_traversal(self, n):
    lvl = [n]
    nxt_lvl
    sets = [n.get_data()]
    b = True

    while t:
        print(sets)

        b = False
        sets = []
        nxt_lvl = []

        for n in level:
            if n != None:
                nxt_lvl.append(n.get_left())
                nxt_lvl.append(n.get_right())
            else:
                nxt_lvl.append(None)
                nxt_lvl.append(None)

        for m in nxt_lvl:
            if m != None:
                sets.append(m.get_data())
            else:
                sets.append(m)

        for o in sets:
            if o != None:
                b = True

        lvl = nxt_lvl
