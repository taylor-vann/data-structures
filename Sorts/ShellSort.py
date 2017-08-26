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
    n = len(a)

    if n <= 1:
        return

    spc = n

    while spc > 0:
        for i in range(spc):
            prv = i
            idx = i + spc

            while idx > 0 and a[idx - spc] > a[idx]:
                    a[idx], a[idx - spc] = a[idx - spc], a[idx]
                    idx -= spc
            prv += spc
            idx = prv + spc

        spc //= 2
