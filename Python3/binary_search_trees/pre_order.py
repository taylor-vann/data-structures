"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def pre_order(n, func=lambda x: print(x)):
    if not n:
        return

    func(n)
    pre_order(n.left, func)
    pre_order(n.right, func)


def pre_order_iterative(n):
    if not n:
        return []

    stack = [n]
    results = []

    while stack:
        node = stack.pop()
        results.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return results
