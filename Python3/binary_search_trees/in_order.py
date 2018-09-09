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


def in_order_iterative(curr, func=lambda x: print(x.value)):
    stack = [curr]

    while stack or curr not None:
        if curr.left:
            curr = curr.left
            stack.append(curr.left)
        else:
            curr = stack.pop()
            func(curr)
            curr = curr.right
