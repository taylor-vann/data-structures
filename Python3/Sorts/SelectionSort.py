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

    if n <= 1:
        return a

    for i in range(n):
        mindx = i

        for j in range(i + 1, n):
            if a[j] < a[mindx]:
                mindx = j

        if mindx != i:
            a[mindx], a[i] = a[i], a[mindx]
