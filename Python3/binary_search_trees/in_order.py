"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def in_order(curr, func=lambda x: print(x.value)):
    if not curr:
        return

    in_order(curr.left, func)
    func(curr)
    in_order(curr.right, func)


def in_order_iterative(curr, func=lambda x: print(x.value)):
    stack = []

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            func(curr)
            curr = curr.right
