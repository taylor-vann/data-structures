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

    if n <= 1:
        return

    prv = 0

    for i in range(n):
        indx = i
        while a[prv] > a[indx] and indx > 0:
            a[indx], a[prv] = a[prv], a[indx]
            prv -=1
            indx -=1

        prv = i
