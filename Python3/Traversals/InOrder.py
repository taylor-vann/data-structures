"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- In order tree traversal

Requirements:
- None
"""

def in_order(n, s = []):
    if n == None:
        return

    in_order(n.get_left())
    s.append(n.get_data())
    in_order(n.get_right())

    return s


def rec_in_order(n):
    if n == None:
        return

    in_order(n.get_left())
    print(n.get_data())
    in_order(n.get_right())


def itr_in_order(n):
    s = [n]
    f = []

    while s:
        while n:
            n = n.get_left()
            s.append(n)

        t = s.pop()

        if t:
            f.append(t.get_data())

            if t.get_right():
                n = t.get_right()
                s.append(n)

    return f
