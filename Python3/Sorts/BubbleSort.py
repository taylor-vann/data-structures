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

    if n <= 1:
        return

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
