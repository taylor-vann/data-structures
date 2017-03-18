"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to Radix sort a list

Requirements:
- Assumes whole numbers (pos ints: 0, 1, 2, ...)

Methods:
- radix_sort
- bucketish_sort
- get_max
"""


def radix_sort(a, base = 10):
    if len(a) <= 1:
        return a

    bckt = a
    exp = base
    mod = 1
    max_num = get_max(a)

    while max_num//mod > 0:
        bckt = bucketish_sort(bckt, exp, mod)
        exp *= base
        mod *= base

    return bckt


def bucketish_sort(a, exp, mod, base = 10):
    bckt = []

    for i in range(base):
        bckt.append([])

    coll = []

    for val in a:
        index = (val % exp)//mod
        bckt[index].append(val)

    for var in bckt:
        coll += var

    return coll


def get_max(a):
    if len(a) == 0:
        return None

    n = a[0]

    for v in a:
        if n < v:
            n = v

    return n
