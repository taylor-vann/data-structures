"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


def radix_sort(arr, base = 10):
    if len(arr) < 2:
        return arr

    srtd = arr
    max_num = max(srtd)
    position = base
    modulo = 1

    while max_num // modulo > 0:
        srtd = digit_sort(srtd, position, modulo, base)
        position *= base
        modulo *= base

    return srtd


def digit_sort(arr, position, modulo, base):
    bckt = [[] for j in range(base)]

    for value in arr:
        indx = (value % position) // modulo
        bckt[indx].append(value)

    return sum(bckt, [])
