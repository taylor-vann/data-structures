"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Tree traversal by level

Requirements:
- None
"""

def level_order(self, n):
    lvl = [n]
    nxt_lvl = []
    sets = [n.get_data()]
    b = True

    while t:
        print(sets)

        b = False
        sets = []
        nxt_lvl = []

        for m in level:
            if  m= None:
                nxt_lvl.append(m.get_left())
                nxt_lvl.append(m.get_right())
            else:
                nxt_lvl.append(None)
                nxt_lvl.append(None)

        for o in nxt_lvl:
            if o != None:
                sets.append(o.get_data())
            else:
                sets.append(o)

        for o in sets:
            if o != None:
                b = True

        lvl = nxt_lvl
