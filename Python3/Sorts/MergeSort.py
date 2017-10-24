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
    if len(a) < 2:
        return a

    p = len(a) // 2

    l1 = merge_sort(a[:p])
    l2 = merge_sort(a[p:])

    return merge(l1, l2)


def merge(a, b):
    c = []

    while a and b:
        if a[0] < b[0]:
            c += a.pop(0)
        else:
            c += b.pop(0)

    c += a
    c += b

    return c
