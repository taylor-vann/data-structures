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
    scout = curr.left

    while stack or scout:
        if scout:
            stack.append(scout)
            scout = scout.left
        else:
            curr = stack[-1].right

            if not curr:
                curr = stack.pop()
                func(curr)

                while stack and stack[-1].right != curr:
                    curr = stack.pop()
                    func(curr)
            else:
                scout = curr
