"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to insertion sort a list

Requirements:
- None

Methods:
- insetion_sort
"""

def insertion_sort(a):
    n = len(a)

    if n < 2:
        return a

    # walk through the list
    for j in range(1, n):
        cur = j
        prv = j - 1

        # descend the list and swap elements if prev larger than next
        while a[prv] > a[cur] and prv > -1:
            a[prv], a[cur] = a[cur], a[prv]
            cur -= 1
            prv = cur - 1

    return a
