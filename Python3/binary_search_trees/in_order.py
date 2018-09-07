"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def in_order(curr, func=lambda x: print(x.value)):
    if not curr:
        return

    in_order(curr.left)
    func(curr)
    in_order(curr.right)


def in_order_iterative(node):
    s = [node]
    f = []

    while s:
        while node:
            node = node.left
            s.append(node)

        t = s.pop()

        if t:
            f.append(t.value)

            if t.right:
                node = t.right
                s.append(node)

    return f
