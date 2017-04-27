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

        a = None
        p = None
        c = self._r

        while c != None:
            a = p
            p = c

            if c.get_data() > bit:
                c = c.get_left()
            else:
                c = c.get_right()

        n.set_parent(p)

        if p.get_data() > bit:
            p.set_left(n)
        else: 
            p.set_right(n)

        self._balance(a, p, n)


    def remove(self, bit):
        e = None
        a = None
        p = None
        c = self._r

        while c != None:
            if c.get_data() == bit:
                break

            e = a
            a = p
            p = c

            if c.get_data() > bit:
                c = c.get_left()
            else:
                c = c.get_right()

        if c == None:
            return

        self._replace(e, a, p, c)


    def _replace(self, e, a, p, c):
        t = None

        if c.get_left() and c.get_right():
            t = self._get_tail(c)

            t.set_left(c.get_left())
            t.set_right(c.get_right())

            if p:
                if p.get_data() > t.get_data():
                    p.set_left(t)
                else:
                    p.set_right(t)
            else:
                self._r = t
        elif c.get_left():
            t = c.get_left()

            self._replace_node(p, c, t)
            self._balance(a, p, t)
        else:
            self._replace_node(p, c)

            if p.get_right():
                self._balance(a, p, p.get_right())


    def _get_tail(self, n):
        a = None
        p = n
        c = n.get_right()
    
        while c.get_left():
            a = p
            p = c
            c = c.get_left()

        if a:
            p.set_left(None)
        else:
            p.set_right(None)

        if p.get_right():            
            self._balance(a, p, p.get_right())

        c.set_parent(None)

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

        if r:
            r.set_parent(p)

        c.set_parent(None)
        c.set_left(None)
        c.set_right(None)


    def _replace_root(self, c, r = None):
        if r:
            r.set_left(c.get_left())
            r.set_right(c.get_right())

        c.set_parent(r)

        self._r = r


    def _balance(self, a, p, c):
        # no nodes
        if p == None:
            return

        # right right heavy, move to left, less cases
        if p.get_left() == None and p.get_right():
            self._shift(a, p, c)
            p, c = c, p

        # walk back, compare heights, rotate when necessary
        while a:
            l = 0
            r = 0

            if a.get_left():
                l = a.get_left().get_height()
            if a.get_right():
                r = a.get_right().get_height()

            if l - r > 1:
                p = a.get_left()
                c = p.get_right()

                self._right(a, p, c)
                a, p = p, a

            if l - r < -1:
                p = a.get_right()
                n = p.get_left()

                self._left(a, p)
                a, p = p, a

            a = a.get_parent()


    def _shift(self, a, p, c):
        if p == self._r:
            self._r = c

        if a:
            if a.get_data() > c.get_data():
                a.set_left(c)
            else:
                a.set_right(c)

        c.set_left(p)
        p.set_parent(c)
        p.set_right(None)
        c.set_parent(a)


    def _left(self, a, p):
        e = a.get_parent()
        l = p.get_left()

        if a == self._r:
            self._r = p
            p.set_parent(None)

        if e:
            if e.get_data() > a.get_data():
                e.set_left(p)
            else:
                e.set_right(p)

            p.set_parent(e)

        if l:
            l.set_parent(a)

        a.set_right(l)
        a.set_parent(p)

        p.set_left(a)


    def _right(self, a, p, c):
        e = a.get_parent()
        r = p.get_right()

        if a == self._r:
            self._r = p
            p.set_parent(None)

        if e:
            if e.get_data() > p.get_data():
                e.set_left(p)
            else:
                e.set_right(p)

            p.set_parent(e)

        if r:
            r.set_parent(a)

        a.set_left(r)
        a.set_parent(p)
        p.set_right(a)
            

    def traverse(self, node):
        level = [node]
        sets = [node.get_data()]
        t = True

        while t:
            print(sets)

            t = False
            sets = []
            nxt_level = []

            for n in level:
                if n != None:
                    nxt_level.append(n.get_left())
                    nxt_level.append(n.get_right())
                else:
                    nxt_level.append(None)
                    nxt_level.append(None)

            for m in nxt_level:
                if m != None:
                    sets.append(m.get_data())
                else:
                    sets.append(m)

            for o in sets:
                if o != None:
                    t = True

            level = nxt_level
