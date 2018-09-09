"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

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
