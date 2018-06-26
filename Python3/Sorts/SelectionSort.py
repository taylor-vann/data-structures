"""
Brian Taylor Vann
github.com/taylor-vann
"""


def selection_sort(arr):
    if len(arr) < 2:
        return arr

    for i in range(len(arr) - 1):
        index = None

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j

        if index:
            arr[index], arr[i] = arr[i], arr[index]

    return arr
