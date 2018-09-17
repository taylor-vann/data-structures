"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def post_order(curr, func=lambda x: print(x.value)):
    if not curr:
        return

    post_order(curr.left, func)
    post_order(curr.right, func)
    func(curr)


def post_order_iterative(node, func=lambda x: print(x.value)):
    if not node:
        return

    stack = [node]
    curr = None
    sentinel = None

    while stack:
        curr = stack.pop()

        sentinel = None
        if stack:
            sentinel = stack[-1]

        if sentinel and sentinel.left != curr:
            print("post order start")
        else:
