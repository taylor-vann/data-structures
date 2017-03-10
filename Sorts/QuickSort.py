"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to quick sort a list

Requirements:
- None

Methods:
- quick_sort
"""


def quick_sort(a, lo, hi):
    if len(a) <= 1:
        return

    if lo < hi:
        p = partition(a, lo, hi)
        quick_sort(a, lo, p - 1)
        quick_sort(a, p + 1, hi)


def partition(a, lo, hi):
    while True:
        while a[lo] < a[hi]:
            lo += 1

        while a[hi] > a[lo]:
            hi -= 1

        if lo >= hi:
            break
        else:
            a[lo], a[hi] = a[hi], a[lo]

    return lo
