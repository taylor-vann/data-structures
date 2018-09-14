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
    curr = node
    # posts = []
    #
    # while stack:
    #     posts.append(stack.pop())
    #
    #     if posts[-1].left:
    #         stack.append(posts[-1].left)
    #     if posts[-1].right:
    #         stack.append(posts[-1].right)
    #
    # while p:
    #     func(p.pop())

    while stack:
        node = stack.pop()

        if stack and node.right != stack[-1]:
            stack.append(node.right)
            stack.append(node)
            print(node.value)
        else:
            # print(node.value)
            pass
