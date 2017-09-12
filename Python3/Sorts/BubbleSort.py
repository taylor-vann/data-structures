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
        return

    b = True

    while b:
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                b = False

        if b == True:
            break

        b = True
