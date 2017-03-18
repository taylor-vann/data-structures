"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to quick sort a list

Requirements:
- None

Methods:
- quick_sort
- partition
"""


def quick_sort(l, lo, hi):
    if len(l) <= 1:
        return

    if lo < hi:
        p = partition(l, lo, hi)
        quick_sort(l, lo, p - 1)
        quick_sort(l, p + 1, hi)


def partition(l, lo, hi):
    while True:
        while l[lo] < l[hi]:
            lo += 1

        while l[hi] > l[lo]:
            hi -= 1

        if lo >= hi:
            break
        else:
            l[lo], l[hi] = l[hi], l[lo]

    return lo
