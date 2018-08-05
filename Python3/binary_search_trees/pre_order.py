"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def pre_order(n, order):
    if not n:
        return order

    order.append(n.data)
    pre_order(n.left, order)
    pre_order(n.right, order)

    return order


def iterative_pre_order(n):
    if not n:
        return []

    stack = [n]
    results = []

    while stack:
        node = stack.pop()
        results.append(node.data)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return results
