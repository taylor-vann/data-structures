"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Tree traversal by level

Requirements:
- None
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
    s = []
    p = []
    f = []

    s.append(n)

    while s:
        while n:
            n = n.get_left()
            s.append(n)

        t = s.pop()

        if t:
            if t.get_right():
                n = t.get_right()
                s.append(n)
                p.append(t)
                print("p", t.get_data())
            else:
                print("f", t.get_data())
                f.append(t.get_data())

    return f
