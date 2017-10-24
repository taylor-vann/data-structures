"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to shell sort a list

Requirements:
- None

Methods:
- shell_sort
"""


def shell_sort(a):
    l = len(a)

    if l < 2:
        return a

    # make space half of list length
    spc = l // 2

    # while space is at least 1
    while spc > 0:
        # run through list from space index to list length
        for j in range(spc, l):
            # use a modified insertion sort based on space
            while j - spc > -1 and a[j - spc] > a[j]:
                a[j - spc], a[j] = a[j], a[j - spc]
                j -= spc

        # half space as int
        spc //= 2

    return a
