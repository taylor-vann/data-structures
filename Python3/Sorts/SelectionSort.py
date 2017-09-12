"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to selection sort a list

Requirements:
- None

Methods:
- selection_sort
"""


def selection_sort(a):
    n = len(a)

    if n < 2:
        return a

    # walk through list ...
    for i in range(n):
        # establish an index
        indx = i

        # walk through the rest of the list ...
        for j in range(i + 1, n):
            # if current is less than index, make index equal to current ...
            if a[j] < a[indx]:
                indx = j

        # if index is different than start, swap values ...
        if indx != i:
            a[indx], a[i] = a[i], a[indx]

    return a
