"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


class AVLNode(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 0


class AVLTree(object):
    def __init__(self, *args):
        for value in args:
            self.insert(value)


    def __contains__(self, value):
        return self.search(self._root, value)


    def search(self, node, value):
        if not node:
            return

        if node.value == value:
            return node

        if node.value < value:
            return self.search(node.right, value)

        return self.search(node.left, value)


    def insert(self, value):
        n = AVLNode(value)

        if self._root == None:
            self._root = n

            return

        s = [None, None, None]
        c = self._r

        while c != None:
            s.append(c)

            if c.value > value:
                c = c.left
            else:
                c = c.right

        l = len(s) - 1

        if s[l].value > value:
            s[l].set_left(n)
        else:
            s[l].set_right(n)

        s.append(n)

        self._balance(s)


    def remove(self, value):
        c = self._r

        s = [None, None, None]

        while c != None:
            s.append(c)

            if c.value == value:
                break

            if c.value > value:
                c = c.left
            else:
                c = c.right

        if c == None:
            return

        self._replace(s)


    def _replace(self, s):
        t = None
        l = len(s) - 1

        # two leaf branch, find the left most right leaf.
        if s[l].left and s[l].right:
            t = self._get_tail(s)

            t.set_left(s[l].left)
            t.set_right(s[l].right)

            if s[l - 1]:
                if s[l - 1].value > t.value:
                    s[l - 1].set_left(t)
                else:
                    s[l - 1].set_right(t)
            else:
                self._root = t
        # left leaf branch
        elif s[l].left:
            t = s[l].left

            self._replace_node(s[l - 1], s[l], t)
            self._balance(s)
        # leaf
        else:
            self._replace_node(s[l - 1], s[l])

            if s[l - 1].right:
                s.append(s[l - 1].right)
                self._balance(s)


    def _get_tail(self, s):
        stk = s
        l = len(stk) - 1
        c = stk[l].right

        stk.append(c)

        while c.left:
            c = c.left
            stk.append(c)

        l = len(stk) - 1

        if stk[l - 3]:
            stk[l - 1].set_left(None)
        else:
            stk[l - 1].set_right(None)

        if stk[l - 1].right:
            self._clr(stk.pop())

            stk.append(stk[l - 1].right)
            self._balance(stk)

        self._clr(c)

        return c


    def _replace_node(self, p, c, r = None):
        if p == None:
            self._replace_root(c, r)

            return
        else:
            if p.left == c:
                p.set_left(r)
            else:
                p.set_right(r)

        self._clr(c)


    def _replace_root(self, c, r = None):
        if r:
            r.set_left(c.left)
            r.set_right(c.right)

        self._root = r


    def _balance(self, s):
        l = len(s) - 1

        # no leafs
        if s[l - 1] == None:
           return

        # leaf is right heavy
        if s[l - 1].left == None and s[l - 1].right:
            self._shift(s[l - 2], s[l - 1], s[l])
            s[l - 1], s[l] = s[l], s[l - 1]

        # walk back stack, compare heights, rotate when necessary
        while s[l - 2] != None:
            left = 0
            rgt = 0

            # get branch heights
            if s[l - 2].left:
                left = s[l - 2].left
                left = left.get_height()
            if s[l - 2].right:
                rgt = s[l - 2].right
                rgt = rgt.get_height()

            # branch is right heavy, shit to left heavy
            if left - rgt > 1:
                p = s[l - 1].left
                c = s[l].right

                self._right(s[l - 3], s[l - 2], s[l - 1], s[l])
                s[l - 2], s[l - 1] = s[l - 1], s[l - 2]

            # branch is left heavy
            if left - rgt < -1:
                p = s[l - 1].right
                n = s[l].left

                self._left(s[l - 3], s[l - 2], s[l - 1])
                s[l - 2], s[l - 1] = s[l - 1], s[l - 2]

            self._clr(s.pop())

            l -= 1


    def _shift(self, a, p, c):
        if p == self._r:
            self._root = c

        if a:
            if a.value > c.value:
                a.set_left(c)
            else:
                a.set_right(c)

        c.set_left(p)
        p.set_right(None)


    def _left(self, e, a, p):
        l = p.left

        if self._root == a:
            self._root = p

        if e:
            if e.value > a.value:
                e.set_left(p)
            else:
                e.set_right(p)

        a.set_right(l)
        p.set_left(a)


    def _right(self, e, a, p, c):
        r = p.right

        if a == self._r:
            self._root = p

        if e:
            if e.value > p.value:
                e.set_left(p)
            else:
                e.set_right(p)

        a.set_left(r)
        p.set_right(a)


    def _clr(self, n):
        n.set_left(None)
        n.set_right(None)
