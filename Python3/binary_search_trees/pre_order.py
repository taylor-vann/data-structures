"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def pre_order(curr, func=lambda x: print(x.value)):
    if not curr:
        return

    func(curr)
    pre_order(curr.left, func)
    pre_order(curr.right, func)


def pre_order_iterative(node):
    if not node:
        return []

    stack = [node]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
