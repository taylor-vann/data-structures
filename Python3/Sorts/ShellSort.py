"""
Brian Taylor Vann
github.com/taylor-vann
"""


def shell_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    spc = length // 2

    while spc > 0:
        for j in range(spc, length):
            while j - spc > -1 and arr[j - spc] > arr[j]:
                arr[j - spc], arr[j] = arr[j], arr[j - spc]
                j -= spc

        spc //= 2

    return arr
