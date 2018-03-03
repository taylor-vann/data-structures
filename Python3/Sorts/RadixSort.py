"""
Brian Taylor Vann
github.com/taylor-vann
"""


def radix_sort(arr, base = 10):
    if len(arr) < 2:
        return arr

    srtd = arr[:]
    max_num = max(srtd)
    pos = base
    mod = 1

    while max_num // mod > 0:
        srtd = digit_sort(srtd, pos, mod, base)
        pos *= base
        mod *= base

    return srtd


def digit_sort(arr, pos, mod, base):
    bckt = [[] for j in range(base)]

    for val in arr:
        indx = (val % pos) // mod
        bckt[indx].append(val)

    return sum(bckt, [])
