"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to bubble sort a list

Requirements:
- None

Methods:
- bubble_sort
"""

def bubble_sort(a):
    n = len(a)

    if n < 2:
        return a

    not_swpd = True

    # until list is traversed without swapping ...
    while not_swpd:
        # compare one element to the next for the list ...
        for i in range(n - 1):
            # if prev is less than next then swap ...
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                not_swpd = False

        # if there was no swap then break ...
        if not_swpd == True:
            break

        # reset for next round
        not_swpd = True

    return a
