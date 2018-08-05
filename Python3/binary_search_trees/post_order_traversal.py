"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def post_order(n, s = []):
    if n == None:
        return

    post_order(n.get_left())
    post_order(n.get_right())
    s.append(n.get_data())

    return s


def rec_post_order(n):
    if n == None:
        return

    rec_post_order(n.get_left())
    rec_post_order(n.get_right())
    print(n.get_data())


def itr_post_order(n):
    if n == None:
        return

    s = []
    p = []
    f = []

    s.append(n)

    while s:
        n = s.pop()
        p.append(n)

        if n.get_left():
            s.append(n.get_left())
        if n.get_right():
            s.append(n.get_right())

    while p:
        n = p.pop()
        f.append(n.get_data())

    return f
