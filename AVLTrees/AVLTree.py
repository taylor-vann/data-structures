"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- AVL tree structure class
- Based on AVL Tree design by Adelson-Velsky and Landis
- Published in their 1962 paper "An algorithm for the organization of information"

Requirements:
- AVLNode.py

Methods:
- search(<data>)
- insert(<data>)
- remove(<data>)

- _replace(<ancestor>, <parent>, <child>)
- _get_tail(<node>)
- _replace_node(<parent>, <child>, <replacement>)
- _replace_root(self, <child>, <replacement>)
- _balance(<ancestor>, <parent>, <child>)
- _shift(<ancestor>,<parent>, <child>)
- _left(<ancestor>, <parent>)
- _right(<ancestor>, <parent>, <child>)
"""

from AVLNode import AVLNode


class AVLTree(object):

    _r = None

    #overwritten methods
    def __init__(self, *args):
        for var in args:
            self.insert(var)


    def __contains__(self, bit):
        return self.search(bit)


    #custom methods
    def search(self, bit):
        n = self._r

        while n != None:
            if n.get_data() == bit:
                return n

            if n.get_data() > bit:
                n = n.get_left()
            else:
                n = n.get_right()

        return None


    def insert(self, bit):
        n = AVLNode(bit)

        if self._r == None:
            self._r = n

            return

        s = [None, None, None]
        c = self._r

        while c != None:
            s.append(c)

            if c.get_data() > bit:
                c = c.get_left()
            else:
                c = c.get_right()

        l = len(s) - 1

        if s[l].get_data() > bit:
            s[l].set_left(n)
        else: 
            s[l].set_right(n)

        s.append(n)

        self._balance(s)


    def remove(self, bit):
        c = self._r

        s = [None, None, None]

        while c != None:
            s.append(c)

            if c.get_data() == bit:
                break

            if c.get_data() > bit:
                c = c.get_left()
            else:
                c = c.get_right()

        if c == None:
            return

        self._replace(s)


    def _replace(self, s):
        t = None
        l = len(s) - 1

        # two leaf branch, find the left most right leaf.
        if s[l].get_left() and s[l].get_right():
            t = self._get_tail(s)

            t.set_left(s[l].get_left())
            t.set_right(s[l].get_right())

            if s[l - 1]:
                if s[l - 1].get_data() > t.get_data():
                    s[l - 1].set_left(t)
                else:
                    s[l - 1].set_right(t)
            else:
                self._r = t
        # left leaf branch
        elif s[l].get_left():
            t = s[l].get_left()

            self._replace_node(s[l - 1], s[l], t)
            self._balance(s)
        # no leaf branch
        else:
            self._replace_node(s[l - 1], s[l])

            if s[l - 1].get_right():
                s.append(s[l - 1].get_right())
                self._balance(s)


    def _get_tail(self, s):
        stk = s
        l = len(stk) - 1
        c = stk[l].get_right()

        stk.append(c)

        while c.get_left():
            c = c.get_left()
            stk.append(c)

        l = len(stk) - 1

        if stk[l - 3]:
            stk[l - 1].set_left(None)
        else:
            stk[l - 1].set_right(None)

        if stk[l - 1].get_right():
            self._clr(stk.pop())

            stk.append(stk[l - 1].get_right())
            self._balance(stk)

        self._clr(c)

        return c


    def _replace_node(self, p, c, r = None):
        if p == None:
            self._replace_root(c, r)

            return
        else:
            if p.get_left() == c:
                p.set_left(r)
            else:
                p.set_right(r)

        self._clr(c)


    def _replace_root(self, c, r = None):
        if r:
            r.set_left(c.get_left())
            r.set_right(c.get_right())

        self._r = r


    def _balance(self, s):
        l = len(s) - 1

        # no leafs
        if s[l - 1] == None:
           return

        # leaf is right heavy
        if s[l - 1].get_left() == None and s[l - 1].get_right():
            self._shift(s[l - 2], s[l - 1], s[l])
            s[l - 1], s[l] = s[l], s[l - 1]

        # walk back stack, compare heights, rotate when necessary
        while s[l - 2] != None:
            lft = 0
            rgt = 0

            # get branch heights
            if s[l - 2].get_left():
                lft = s[l - 2].get_left()
                lft = lft.get_height()
            if s[l - 2].get_right():
                rgt = s[l - 2].get_right()
                rgt = rgt.get_height()

            # branch is right heavy, shit to left heavy
            if lft - rgt > 1:
                p = s[l - 1].get_left()
                c = s[l].get_right()

                self._right(s[l - 3], s[l - 2], s[l - 1], s[l])
                s[l - 2], s[l - 1] = s[l - 1], s[l - 2]

            # branch is left heavy
            if lft - rgt < -1:
                p = s[l - 1].get_right()
                n = s[l].get_left()

                self._left(s[l - 3], s[l - 2], s[l - 1])
                s[l - 2], s[l - 1] = s[l - 1], s[l - 2]

            self._clr(s.pop())

            l -= 1
 

    def _shift(self, a, p, c):
        if p == self._r:
            self._r = c

        if a:
            if a.get_data() > c.get_data():
                a.set_left(c)
            else:
                a.set_right(c)

        c.set_left(p)
        p.set_right(None)


    def _left(self, e, a, p):
        l = p.get_left()

        if self._r == a:
            self._r = p

        if e:
            if e.get_data() > a.get_data():
                e.set_left(p)
            else:
                e.set_right(p)

        a.set_right(l)
        p.set_left(a)


    def _right(self, e, a, p, c):
        r = p.get_right()

        if a == self._r:
            self._r = p

        if e:
            if e.get_data() > p.get_data():
                e.set_left(p)
            else:
                e.set_right(p)

        a.set_left(r)
        p.set_right(a)


    def _clr(self, n):
        n.set_left(None)
        n.set_right(None)
