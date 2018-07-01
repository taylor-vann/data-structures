"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


def shell_sort(arr):
    if len(arr) < 2:
        return arr

    spc = len(arr) // 2

    while spc > 0:
        for j in range(spc, len(arr)):
            while j - spc > -1 and arr[j - spc] > arr[j]:
                arr[j - spc], arr[j] = arr[j], arr[j - spc]
                j -= spc

        spc //= 2

    return arr
