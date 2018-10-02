
def post_order(curr, func=lambda x: print(x.value)):
    if not curr:
        return

    post_order(curr.left, func)
    post_order(curr.right, func)
    func(curr)


def level_order(n, func=lambda x: print(x)):
    if not n:
        return

    curr = [n]
    nxt = []
    level = []

    while curr:
        for node in curr:
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)

            level.append(node.value)

        func(level)

        curr = nxt
        nxt = []
        level = []
