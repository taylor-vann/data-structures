"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to Radix sort a list

Requirements:
- Assumes whole numbers
- Least Significant Digit (LSD) Radix Sort

Methods:
- radix_sort
- bucketish_sort
"""


def radix_sort(a, base = 10):
    if len(a) < 2:
        return a

    srtd = a[:]
    pos = base
    mod = 1
    max_num = max(srtd)

    while max_num // mod > 0:
        srtd = digit_sort(srtd, pos, mod, base)
        pos *= base
        mod *= base

    return srtd


def digit_sort(a, pos, mod, base):
    bckt = [[] for j in range(base)]

    for val in a:
        indx = (val % pos) // mod
        bckt[indx].append(val)

    return sum(bckt, [])
