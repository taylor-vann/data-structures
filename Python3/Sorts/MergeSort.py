"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to merge sort a list

Requirements:
- None

Methods:
- merge_sort
- merge
"""


def merge_sort(a):
    if len(a) <= 1:
        return a

    p = len(a) // 2

    l1 = a[:p]
    l2 = a[p:]

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

    return merge(l1, l2)


def merge(a, b):
    c = []

    while len(a) and len(b):
        if a[0] < b[0]:
            c.append(a.pop(0)) 
        else:
            c.append(b.pop(0))
            

    while len(a):
        c.append(a.pop(0))

    while len(b):
        c.append(b.pop(0))

    return c
