"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


def pre_order(n, s = []):
    if n == None:
        return

    s.append(n.get_data())
    pre_order(n.get_left())
    pre_order(n.get_right())

    return s


def rec_pre_order(n):
    if n == None:
        return

    print(n.get_data())
    pre_order(n.get_left())
    pre_order(n.get_right())


def itr_pre_order(n):
    s = [None]
    f = []

    s.append(n)

    while s:
        while n:
            f.append(n.get_data())
            n = n.get_left()
            s.append(n)

        t = s.pop()

        if t:
            if t.get_right():
                n = t.get_right()
                s.append(n)

    return f
