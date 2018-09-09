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


def post_order_iterative(curr, func=lambda x: print(x.value)):
    if not curr:
        return

    stack = [curr]
    posts = []

    while stack:
        posts.append(stack.pop())

        if posts[-1].left:
            stack.append(posts[-1].left)
        if posts[-1].right:
            stack.append(posts[-1].right)

    while p:
        func(p.pop())

    return f
