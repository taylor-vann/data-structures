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
            if not node:
                level.append(None)
            elif node:
                if node.left:
                    nxt.append(node.left)
                else:
                    nxt.append(None)

                if node.right:
                    nxt.append(node.right)
                else:
                    nxt.append(None)

                level.append(node.value)

        if not any(level):
            break
        
        func(level)

        curr = nxt
        nxt = []
        level = []


def get_tree_height(node, height=0):
    if not node:
        return height

    return max(
        get_tree_height(node.left, height + 1),
        get_tree_height(node.right, height + 1)
    )
