"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to quick sort a list
- untraditional, copies list, more thread safe

Requirements:
- None

Methods:
- quick_sort
- partition
"""


def quick_sort(a):
    if len(a) < 2:
        return a

    p, q = partition(a[:])

    l1 = quick_sort(p)
    l2 = quick_sort(q)

    return l1 + l2


def partition(a):
    lo = 0
    hi = len(a) - 1

    while True:
        if a[lo] == a[hi]:
            lo += 1

        while a[lo] < a[hi]:
            lo += 1

        while a[hi] > a[lo]:
            hi -= 1

        if lo >= hi:
            return a[:lo], a[lo:]

        a[lo], a[hi] = a[hi], a[lo]
