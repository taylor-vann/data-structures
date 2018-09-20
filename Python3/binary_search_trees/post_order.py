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

    stack = []

    if curr.right:
        stack.append(curr.right)
    stack.append(curr)

    scout = curr.left

    while stack:
        if scout:
            if scout.right:
                stack.append(scout.right)

            stack.append(scout)
            scout = scout.left
        else:
            if len(stack) > 1 and stack[-2] == stack[-1].right:
                stack[-1], stack[-2] = stack[-2], stack[-1]
                scout = stack.pop()
            else:
                func(stack.pop())
