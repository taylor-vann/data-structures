"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def level_order(n):
    lvl = [n]
    nxt_lvl = []
    sets = [n.get_data()]
    b = True

    while b:
        print(sets)

        b = False
        sets = []
        nxt_lvl = []

        for m in lvl:
            if  m != None:
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
